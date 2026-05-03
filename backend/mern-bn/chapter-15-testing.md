
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 15 — Testing
# "Jest + Supertest দিয়ে Backend Test করো"
# ⏱ ~90 মিনিট · Progress: [██████████████░] 78%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Testing কেন দরকার
- ✅ Jest setup ও configuration
- ✅ Unit tests — services test করা
- ✅ Integration tests — API endpoints test করা
- ✅ Supertest দিয়ে HTTP test
- ✅ Mocking — Prisma, external services
- ✅ Test coverage report

---

## 🏗️ Real-life Analogy

> Testing = গাড়ি কেনার আগে test drive। Unit test = প্রতিটি part আলাদা check। Integration test = সব parts একসাথে চলে কিনা check।

```
🟢 Flutter তুলনা:
   Flutter Widget Test = NestJS Unit Test
   Flutter Integration Test = Supertest API Test
   Flutter test coverage = Jest --coverage
```

---

## ⚙️ Setup

```bash
npm install jest supertest @types/jest @types/supertest --save-dev

# jest.config.js তৈরি করো
```

📄 File: `jest.config.js` · 🎯 উদ্দেশ্য: Jest configuration

```javascript
module.exports = {
  testEnvironment: 'node',
  testMatch: ['**/__tests__/**/*.test.js', '**/*.spec.js'],
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/**/*.spec.js',
    '!src/index.js',
  ],
  coverageDirectory: 'coverage',
  coverageReporters: ['text', 'html', 'lcov'],
  coverageThreshold: {
    global: {
      branches: 70,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  setupFilesAfterFramework: ['./jest.setup.js'],
  testTimeout: 30000,
};
```

📄 File: `jest.setup.js`

```javascript
// Environment variables for tests
process.env.NODE_ENV = 'test';
process.env.JWT_ACCESS_SECRET = 'test_access_secret_minimum_32_chars_long';
process.env.JWT_REFRESH_SECRET = 'test_refresh_secret_minimum_32_chars_long';
process.env.DATABASE_URL = 'postgresql://postgres:password@localhost:5432/ecommerce_test';
process.env.MONGODB_URI = 'mongodb://localhost:27017/ecommerce_test';
```

📄 File: `package.json` (scripts)

```json
{
  "scripts": {
    "test": "jest --forceExit",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage --forceExit",
    "test:unit": "jest --testPathPattern=unit",
    "test:integration": "jest --testPathPattern=integration"
  }
}
```

---

## 🧪 Unit Tests

📄 File: `src/__tests__/unit/auth.service.test.js` · 🎯 উদ্দেশ্য: Auth service unit tests

```javascript
const bcrypt = require('bcryptjs');
const { generateTokenPair, verifyAccessToken } = require('../../utils/jwt.util');

// ============================================
// JWT Utility Tests
// ============================================
describe('JWT Utility', () => {
  const mockUser = {
    id: 1,
    email: 'test@example.com',
    role: 'customer',
  };

  describe('generateTokenPair', () => {
    it('should generate access and refresh tokens', () => {
      const { accessToken, refreshToken } = generateTokenPair(mockUser);

      expect(accessToken).toBeDefined();
      expect(refreshToken).toBeDefined();
      expect(typeof accessToken).toBe('string');
      expect(typeof refreshToken).toBe('string');
    });

    it('access token should contain user info', () => {
      const { accessToken } = generateTokenPair(mockUser);
      const decoded = verifyAccessToken(accessToken);

      expect(decoded.sub).toBe(mockUser.id.toString());
      expect(decoded.email).toBe(mockUser.email);
      expect(decoded.role).toBe(mockUser.role);
    });
  });

  describe('verifyAccessToken', () => {
    it('should verify a valid token', () => {
      const { accessToken } = generateTokenPair(mockUser);
      const decoded = verifyAccessToken(accessToken);

      expect(decoded).toBeTruthy();
      expect(decoded.email).toBe(mockUser.email);
    });

    it('should throw on invalid token', () => {
      expect(() => verifyAccessToken('invalid.token.here')).toThrow();
    });
  });
});

// ============================================
// Bcrypt Tests
// ============================================
describe('Password Hashing', () => {
  it('should hash password correctly', async () => {
    const password = 'TestPassword123!';
    const hash = await bcrypt.hash(password, 10);

    expect(hash).not.toBe(password);
    expect(hash.length).toBeGreaterThan(20);
  });

  it('should compare password and hash correctly', async () => {
    const password = 'TestPassword123!';
    const hash = await bcrypt.hash(password, 10);

    const isValid = await bcrypt.compare(password, hash);
    const isInvalid = await bcrypt.compare('WrongPassword', hash);

    expect(isValid).toBe(true);
    expect(isInvalid).toBe(false);
  });
});
```

📄 File: `src/__tests__/unit/product.service.test.js` · 🎯 উদ্দেশ্য: Product service with mocked Prisma

```javascript
// Prisma mock করো
jest.mock('../../config/prisma', () => ({
  product: {
    findMany: jest.fn(),
    findUnique: jest.fn(),
    findFirst: jest.fn(),
    create: jest.fn(),
    update: jest.fn(),
    count: jest.fn(),
  },
  $transaction: jest.fn(),
}));

const prisma = require('../../config/prisma');
const { AppError } = require('../../middleware/error.middleware');

// Product controller import (direct function test)
const {
  createProduct,
  getProductById,
  deleteProduct,
} = require('../../controllers/prisma-product.controller');

// Mock req, res, next
const mockReq = (body = {}, params = {}, query = {}, user = null) => ({
  body,
  params,
  query,
  user,
});

const mockRes = () => {
  const res = {};
  res.status = jest.fn().mockReturnValue(res);
  res.json = jest.fn().mockReturnValue(res);
  res.send = jest.fn().mockReturnValue(res);
  return res;
};

const mockNext = jest.fn();

describe('Product Controller', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  // ============================================
  // createProduct
  // ============================================
  describe('createProduct', () => {
    it('should create a product successfully', async () => {
      const productData = {
        name: 'Test Product',
        sku: 'TEST-001',
        slug: 'test-product',
        price: 99.99,
        categoryId: 1,
      };

      const mockProduct = { id: 1, ...productData, images: [], category: null };

      prisma.product.findFirst.mockResolvedValue(null);  // No duplicate
      prisma.product.create.mockResolvedValue(mockProduct);

      const req = mockReq(productData);
      const res = mockRes();

      await createProduct(req, res, mockNext);

      expect(prisma.product.findFirst).toHaveBeenCalledWith({
        where: { OR: [{ sku: productData.sku }, { slug: productData.slug }] },
      });
      expect(prisma.product.create).toHaveBeenCalled();
      expect(res.status).toHaveBeenCalledWith(201);
      expect(mockNext).not.toHaveBeenCalled();
    });

    it('should return 409 when SKU already exists', async () => {
      prisma.product.findFirst.mockResolvedValue({
        id: 1,
        sku: 'EXISTING-SKU',
        slug: 'existing-slug',
      });

      const req = mockReq({ sku: 'EXISTING-SKU', slug: 'new-slug' });
      const res = mockRes();

      await createProduct(req, res, mockNext);

      expect(mockNext).toHaveBeenCalledWith(
        expect.objectContaining({ statusCode: 409 })
      );
    });
  });

  // ============================================
  // getProductById
  // ============================================
  describe('getProductById', () => {
    it('should return product when found', async () => {
      const mockProduct = {
        id: 1,
        name: 'Test Product',
        price: 99.99,
        images: [],
        reviews: [],
        _count: { reviews: 0 },
      };

      prisma.product.findUnique.mockResolvedValue(mockProduct);
      prisma.review = { aggregate: jest.fn().mockResolvedValue({ _avg: { rating: 0 }, _count: { rating: 0 } }) };

      const req = mockReq({}, { id: '1' });
      const res = mockRes();

      await getProductById(req, res, mockNext);

      expect(prisma.product.findUnique).toHaveBeenCalledWith(
        expect.objectContaining({ where: { id: 1 } })
      );
      expect(res.status).toHaveBeenCalledWith(200);
    });

    it('should return 404 when product not found', async () => {
      prisma.product.findUnique.mockResolvedValue(null);

      const req = mockReq({}, { id: '999' });
      const res = mockRes();

      await getProductById(req, res, mockNext);

      expect(mockNext).toHaveBeenCalledWith(
        expect.objectContaining({ statusCode: 404 })
      );
    });
  });
});
```

---

## 🔗 Integration Tests (Supertest)

📄 File: `src/__tests__/integration/auth.integration.test.js` · 🎯 উদ্দেশ্য: Auth API integration tests

```javascript
const request = require('supertest');
const app = require('../../app');
const prisma = require('../../config/prisma');

describe('Auth API Integration Tests', () => {
  let testUser;
  let accessToken;
  let refreshToken;

  // Test database clean করো
  beforeAll(async () => {
    await prisma.user.deleteMany({ where: { email: { contains: '@test.com' } } });
  });

  afterAll(async () => {
    await prisma.user.deleteMany({ where: { email: { contains: '@test.com' } } });
    await prisma.$disconnect();
  });

  // ============================================
  // REGISTER
  // ============================================
  describe('POST /api/v1/auth/register', () => {
    it('should register a new user successfully', async () => {
      const response = await request(app)
        .post('/api/v1/auth/register')
        .send({
          firstName: 'Test',
          lastName: 'User',
          email: 'test1@test.com',
          password: 'TestPass123!',
        })
        .expect(201);

      expect(response.body.success).toBe(true);
      expect(response.body.data.email).toBe('test1@test.com');
      expect(response.body.data.passwordHash).toBeUndefined();  // password expose হবে না
    });

    it('should return 409 on duplicate email', async () => {
      const response = await request(app)
        .post('/api/v1/auth/register')
        .send({
          firstName: 'Another',
          lastName: 'User',
          email: 'test1@test.com',  // same email
          password: 'AnotherPass123!',
        })
        .expect(409);

      expect(response.body.success).toBe(false);
    });

    it('should return 400 on invalid email', async () => {
      const response = await request(app)
        .post('/api/v1/auth/register')
        .send({
          firstName: 'Test',
          lastName: 'User',
          email: 'not-an-email',
          password: 'TestPass123!',
        })
        .expect(400);

      expect(response.body.success).toBe(false);
      expect(response.body.errors).toBeDefined();
    });

    it('should return 400 on weak password', async () => {
      const response = await request(app)
        .post('/api/v1/auth/register')
        .send({
          firstName: 'Test',
          lastName: 'User',
          email: 'test2@test.com',
          password: 'weak',  // too weak
        })
        .expect(400);

      expect(response.body.success).toBe(false);
    });
  });

  // ============================================
  // LOGIN
  // ============================================
  describe('POST /api/v1/auth/login', () => {
    it('should login successfully', async () => {
      const response = await request(app)
        .post('/api/v1/auth/login')
        .send({
          email: 'test1@test.com',
          password: 'TestPass123!',
        })
        .expect(200);

      expect(response.body.success).toBe(true);
      expect(response.body.data.accessToken).toBeDefined();
      expect(response.body.data.refreshToken).toBeDefined();
      expect(response.body.data.user).toBeDefined();

      // Later tests-এর জন্য save
      accessToken = response.body.data.accessToken;
      refreshToken = response.body.data.refreshToken;
    });

    it('should return 401 on wrong password', async () => {
      await request(app)
        .post('/api/v1/auth/login')
        .send({
          email: 'test1@test.com',
          password: 'WrongPassword!',
        })
        .expect(401);
    });

    it('should return 401 on non-existent email', async () => {
      await request(app)
        .post('/api/v1/auth/login')
        .send({
          email: 'nonexistent@test.com',
          password: 'TestPass123!',
        })
        .expect(401);
    });
  });

  // ============================================
  // PROTECTED ROUTE
  // ============================================
  describe('GET /api/v1/auth/me', () => {
    it('should return current user with valid token', async () => {
      const response = await request(app)
        .get('/api/v1/auth/me')
        .set('Authorization', `Bearer ${accessToken}`)
        .expect(200);

      expect(response.body.success).toBe(true);
      expect(response.body.data.email).toBe('test1@test.com');
    });

    it('should return 401 without token', async () => {
      await request(app)
        .get('/api/v1/auth/me')
        .expect(401);
    });

    it('should return 401 with invalid token', async () => {
      await request(app)
        .get('/api/v1/auth/me')
        .set('Authorization', 'Bearer invalid.token.here')
        .expect(401);
    });
  });

  // ============================================
  // REFRESH TOKEN
  // ============================================
  describe('POST /api/v1/auth/refresh', () => {
    it('should refresh tokens successfully', async () => {
      const response = await request(app)
        .post('/api/v1/auth/refresh')
        .send({ refreshToken })
        .expect(200);

      expect(response.body.data.accessToken).toBeDefined();
      expect(response.body.data.refreshToken).toBeDefined();
      // New refresh token should be different (rotation)
      expect(response.body.data.refreshToken).not.toBe(refreshToken);
    });
  });

  // ============================================
  // LOGOUT
  // ============================================
  describe('POST /api/v1/auth/logout', () => {
    it('should logout successfully', async () => {
      const response = await request(app)
        .post('/api/v1/auth/logout')
        .set('Authorization', `Bearer ${accessToken}`)
        .expect(200);

      expect(response.body.success).toBe(true);
    });
  });
});
```

---

## 📈 Test Coverage

```bash
# Coverage চালাও
npm run test:coverage

# ফলাফল:
# --------------------------------|---------|----------|---------|---------|
# File                            | % Stmts | % Branch | % Funcs | % Lines |
# --------------------------------|---------|----------|---------|---------|
# src/controllers/auth.js         |   82.3  |   75.0   |   88.9  |   82.3  |
# src/utils/jwt.util.js           |   94.1  |   85.7   |   100   |   94.1  |
# src/middleware/auth.middleware.js|   78.5  |   70.0   |   80.0  |   78.5  |
# --------------------------------|---------|----------|---------|---------|

# Coverage report browser-এ দেখো
open coverage/lcov-report/index.html
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| Real DB-তে test run | Test data pollutes production | Test database আলাদা |
| Async test await না করা | False positive results | সবসময় async/await |
| afterAll cleanup না করা | Test data accumulates | afterAll-এ delete করো |
| Sensitive data test-এ hardcode | Git-এ exposed | Test env vars ব্যবহার করো |
| Too many mocks | Nothing actually tested | Integration tests also write |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 15 — তুমি শিখলে                         ║
╠══════════════════════════════════════════════════════╣
║  • Jest setup ও configuration                       ║
║  • Unit tests: functions, services                  ║
║  • Mocking: jest.fn(), jest.mock()                  ║
║  • Mock req/res/next pattern                        ║
║  • Integration tests with Supertest                 ║
║  • Auth flow complete test                          ║
║  • beforeAll/afterAll cleanup                       ║
║  • Coverage threshold configuration                 ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 14](./chapter-14-api-design.md) | [➡ Chapter 16](./chapter-16-performance.md)
