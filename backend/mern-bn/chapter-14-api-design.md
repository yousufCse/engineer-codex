
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 14 — API Design
# "Clean, Consistent, Production-ready APIs"
# ⏱ ~60 মিনিট · Progress: [█████████████░] 73%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ REST principles রিভিউ ও best practices
- ✅ API versioning strategy
- ✅ Consistent response format
- ✅ Pagination (cursor + offset)
- ✅ Filtering, sorting, searching
- ✅ Swagger/OpenAPI documentation

---

## 🏗️ REST URL Design Rules

```
✅ URL Design Best Practices:

সঠিক:
  GET     /api/v1/products            → সব products
  GET     /api/v1/products/:id        → একটি product
  POST    /api/v1/products            → product তৈরি
  PATCH   /api/v1/products/:id        → partial update
  PUT     /api/v1/products/:id        → full replace
  DELETE  /api/v1/products/:id        → delete

  GET     /api/v1/products/:id/images → product images
  POST    /api/v1/products/:id/images → image upload
  DELETE  /api/v1/images/:imageId     → image delete

  GET     /api/v1/orders/:id/items    → order items
  POST    /api/v1/auth/login          → login (action)

ভুল:
  ❌ GET /getProducts          (verb ব্যবহার)
  ❌ GET /product              (plural হওয়া উচিত)
  ❌ POST /products/create     (redundant)
  ❌ GET /Products             (uppercase)
  ❌ GET /products_list        (underscore)
```

---

## 📦 Consistent Response Format

📄 File: `src/utils/ApiResponse.js` · 🎯 উদ্দেশ্য: All response types

```javascript
class ApiResponse {
  // ============================================
  // Success Responses
  // ============================================
  static success(res, data = null, message = 'Success') {
    return res.status(200).json({
      success: true,
      message,
      data,
    });
  }

  static created(res, data = null, message = 'Created successfully') {
    return res.status(201).json({
      success: true,
      message,
      data,
    });
  }

  static noContent(res) {
    return res.status(204).send();
  }

  // ============================================
  // Paginated Response
  // ============================================
  static paginated(res, data, pagination) {
    return res.status(200).json({
      success: true,
      data,
      pagination: {
        total: pagination.total,
        page: pagination.page,
        limit: pagination.limit,
        totalPages: pagination.totalPages,
        hasNextPage: pagination.hasNextPage,
        hasPreviousPage: pagination.hasPreviousPage,
        // Optional: cursor for next page
        nextCursor: pagination.nextCursor || null,
      },
    });
  }

  // ============================================
  // Error Responses
  // ============================================
  static error(res, message = 'Something went wrong', statusCode = 500, errors = null) {
    const response = {
      success: false,
      message,
    };

    if (errors) {
      response.errors = errors;
    }

    return res.status(statusCode).json(response);
  }

  static validationError(res, errors) {
    return res.status(400).json({
      success: false,
      message: 'Validation failed',
      errors,
    });
  }

  static notFound(res, resource = 'Resource') {
    return res.status(404).json({
      success: false,
      message: `${resource} not found`,
    });
  }

  static unauthorized(res, message = 'Authentication required') {
    return res.status(401).json({
      success: false,
      message,
    });
  }

  static forbidden(res, message = 'Access denied') {
    return res.status(403).json({
      success: false,
      message,
    });
  }
}

module.exports = ApiResponse;
```

---

## 📖 API Versioning

```javascript
// src/app.js — Versioning setup

const v1Router = require('./routes/v1');
const v2Router = require('./routes/v2');  // future

// URL-based versioning (recommended)
app.use('/api/v1', v1Router);

// src/routes/v1/index.js
const router = express.Router();

router.use('/auth', require('./auth.routes'));
router.use('/products', require('./products.routes'));
router.use('/categories', require('./categories.routes'));
router.use('/orders', require('./orders.routes'));
router.use('/users', require('./users.routes'));
router.use('/uploads', require('./upload.routes'));

module.exports = router;
```

---

## 🔍 Advanced Filtering Pattern

```javascript
// Query: GET /api/v1/products?
//   category=phones&
//   brand=Apple&
//   minPrice=500&
//   maxPrice=2000&
//   inStock=true&
//   featured=true&
//   search=iphone&
//   sort=price&
//   order=asc&
//   page=2&
//   limit=20&
//   fields=id,name,price,brand   (field selection)

const buildProductFilter = (query) => {
  const {
    category, brand, minPrice, maxPrice,
    inStock, featured, search,
    sort = 'createdAt', order = 'desc',
    page = 1, limit = 10,
    fields,
  } = query;

  const filter = { isActive: true };
  const options = {
    sort: { [sort]: order === 'asc' ? 1 : -1 },
    skip: (parseInt(page) - 1) * parseInt(limit),
    limit: Math.min(parseInt(limit), 100),  // max 100
  };

  // Fields selection (projection)
  if (fields) {
    options.projection = fields.split(',').reduce((acc, field) => {
      acc[field.trim()] = 1;
      return acc;
    }, {});
  }

  if (category) filter['category.slug'] = category;
  if (brand) filter.brand = { $regex: brand, $options: 'i' };
  if (minPrice || maxPrice) {
    filter.price = {};
    if (minPrice) filter.price.$gte = parseFloat(minPrice);
    if (maxPrice) filter.price.$lte = parseFloat(maxPrice);
  }
  if (inStock === 'true') filter.stock = { $gt: 0 };
  if (featured === 'true') filter.isFeatured = true;

  if (search) {
    filter.$text = { $search: search };
    options.sort = { score: { $meta: 'textScore' } };
  }

  return { filter, options };
};
```

---

## 📚 Swagger / OpenAPI Documentation

```bash
npm install swagger-jsdoc swagger-ui-express
```

📄 File: `src/config/swagger.config.js` · 🎯 উদ্দেশ্য: Swagger setup

```javascript
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'MyShop E-commerce API',
      version: '1.0.0',
      description: 'Complete e-commerce backend API built with Node.js + Express',
      contact: {
        name: 'API Support',
        email: 'support@myshop.com',
      },
    },
    servers: [
      {
        url: 'http://localhost:3000/api/v1',
        description: 'Development server',
      },
      {
        url: 'https://api.myshop.com/v1',
        description: 'Production server',
      },
    ],
    components: {
      securitySchemes: {
        BearerAuth: {
          type: 'http',
          scheme: 'bearer',
          bearerFormat: 'JWT',
          description: 'JWT access token',
        },
      },
      schemas: {
        Product: {
          type: 'object',
          properties: {
            _id: { type: 'string', example: '507f1f77bcf86cd799439011' },
            name: { type: 'string', example: 'iPhone 15 Pro' },
            sku: { type: 'string', example: 'APPL-IP15P-256-BLK' },
            price: { type: 'number', example: 999.99 },
            stock: { type: 'integer', example: 50 },
            brand: { type: 'string', example: 'Apple' },
          },
        },
        PaginatedResponse: {
          type: 'object',
          properties: {
            success: { type: 'boolean', example: true },
            data: { type: 'array', items: {} },
            pagination: {
              type: 'object',
              properties: {
                total: { type: 'integer', example: 100 },
                page: { type: 'integer', example: 1 },
                limit: { type: 'integer', example: 10 },
                totalPages: { type: 'integer', example: 10 },
                hasNextPage: { type: 'boolean', example: true },
                hasPreviousPage: { type: 'boolean', example: false },
              },
            },
          },
        },
        ErrorResponse: {
          type: 'object',
          properties: {
            success: { type: 'boolean', example: false },
            message: { type: 'string', example: 'Resource not found' },
          },
        },
      },
    },
    security: [{ BearerAuth: [] }],
  },
  apis: ['./src/routes/**/*.js'],  // JSDoc comments scan করবে
};

const specs = swaggerJsdoc(options);

const setupSwagger = (app) => {
  app.use(
    '/api/docs',
    swaggerUi.serve,
    swaggerUi.setup(specs, {
      customSiteTitle: 'MyShop API Docs',
      customCss: '.swagger-ui .topbar { background-color: #1a1a2e; }',
      swaggerOptions: {
        persistAuthorization: true,
      },
    })
  );

  // JSON format
  app.get('/api/docs.json', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.send(specs);
  });

  console.log('📚 API Docs: http://localhost:3000/api/docs');
};

module.exports = { setupSwagger };
```

### JSDoc Annotations

📄 File: `src/routes/v1/products.routes.js` · 🎯 উদ্দেশ্য: Swagger JSDoc

```javascript
/**
 * @swagger
 * /products:
 *   get:
 *     summary: Get all products
 *     tags: [Products]
 *     security: []
 *     parameters:
 *       - in: query
 *         name: page
 *         schema: { type: integer, default: 1 }
 *       - in: query
 *         name: limit
 *         schema: { type: integer, default: 10 }
 *       - in: query
 *         name: category
 *         schema: { type: string }
 *         description: Category slug
 *       - in: query
 *         name: brand
 *         schema: { type: string }
 *       - in: query
 *         name: minPrice
 *         schema: { type: number }
 *       - in: query
 *         name: maxPrice
 *         schema: { type: number }
 *       - in: query
 *         name: search
 *         schema: { type: string }
 *     responses:
 *       200:
 *         description: Products list
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/PaginatedResponse'
 */
router.get('/', getAllProducts);

/**
 * @swagger
 * /products:
 *   post:
 *     summary: Create a new product
 *     tags: [Products]
 *     security:
 *       - BearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [name, sku, slug, price]
 *             properties:
 *               name: { type: string, example: "iPhone 15 Pro" }
 *               sku: { type: string, example: "APPL-IP15P" }
 *               slug: { type: string, example: "iphone-15-pro" }
 *               price: { type: number, example: 999.99 }
 *     responses:
 *       201:
 *         description: Product created
 *       400:
 *         description: Validation error
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/ErrorResponse'
 *       401:
 *         description: Unauthorized
 */
router.post('/', authenticate, authorize('admin', 'seller'), createProduct);
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| Inconsistent response format | Client parse করতে পারে না | একই format সর্বত্র |
| No pagination | Large data crash | সবসময় limit + skip |
| Sensitive fields expose | Data leak | select/projection দিয়ে filter |
| API versioning নেই | Breaking changes client ভাঙে | /api/v1/ prefix রাখো |
| Error message তে stack trace | Security issue | Production-এ hide করো |
| Swagger docs outdated | Developer confusion | JSDoc automatic |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 14 — তুমি শিখলে                         ║
╠══════════════════════════════════════════════════════╣
║  • REST URL design rules (plural, lowercase)        ║
║  • API versioning: /api/v1/                         ║
║  • Consistent response: success/data/pagination     ║
║  • Advanced filtering: query builder pattern        ║
║  • Pagination: skip+limit, cursor                   ║
║  • Swagger/OpenAPI: setup + JSDoc annotations       ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 13](./chapter-13-file-upload-email.md) | [➡ Chapter 15](./chapter-15-testing.md)
