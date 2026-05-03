
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX A — SQL Quick Reference
# "PostgreSQL এর সব Commands একনজরে"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 🗄️ Database & Table

```sql
-- Database
CREATE DATABASE ecommerce;
DROP DATABASE ecommerce;
\l                          -- List databases
\c ecommerce                -- Connect

-- Table
CREATE TABLE users (
  id         SERIAL PRIMARY KEY,
  email      VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

DROP TABLE users;
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users RENAME COLUMN old_name TO new_name;
\dt                         -- List tables
\d users                    -- Describe table
```

---

## 📝 CRUD

```sql
-- INSERT
INSERT INTO users (email, first_name) VALUES ('a@b.com', 'Ali');
INSERT INTO users (email) VALUES ('a@b.com'), ('c@d.com');  -- Multiple rows

-- SELECT
SELECT * FROM users;
SELECT id, email FROM users WHERE id = 1;
SELECT * FROM users WHERE email LIKE '%@gmail.com';
SELECT * FROM users ORDER BY created_at DESC LIMIT 10 OFFSET 20;
SELECT COUNT(*) FROM users;
SELECT role, COUNT(*) FROM users GROUP BY role;

-- UPDATE
UPDATE users SET first_name = 'Yousuf' WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;
TRUNCATE TABLE users;        -- All rows (faster)
```

---

## 🔗 JOINs

```sql
-- INNER JOIN
SELECT o.id, u.email, o.total
FROM orders o
INNER JOIN users u ON o.user_id = u.id;

-- LEFT JOIN (all orders, null if no user)
SELECT o.id, u.email
FROM orders o
LEFT JOIN users u ON o.user_id = u.id;

-- Multiple JOINs
SELECT o.id, u.email, oi.product_name, oi.quantity
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON oi.order_id = o.id
WHERE o.status = 'delivered';
```

---

## 📊 Aggregates

```sql
SELECT
  status,
  COUNT(*) AS order_count,
  SUM(total) AS revenue,
  AVG(total) AS avg_order_value,
  MIN(total) AS min_order,
  MAX(total) AS max_order
FROM orders
GROUP BY status
HAVING COUNT(*) > 10
ORDER BY revenue DESC;
```

---

## 🏷️ Indexes

```sql
CREATE INDEX idx_users_email ON users(email);
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);

DROP INDEX idx_users_email;
\di                          -- List indexes
```

---

## 🔍 Query Analysis

```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 1;
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 1;
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [➡ Appendix B](./appendix-b-mongodb.md)



# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX B — MongoDB Query Reference
# "mongosh Commands একনজরে"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 🗄️ Database & Collection

```javascript
show dbs                         // All databases
use ecommerce                    // Switch/create database
show collections                 // All collections
db.createCollection('products')  // Explicit create
db.products.drop()               // Drop collection
```

---

## 📝 CRUD

```javascript
// INSERT
db.products.insertOne({ name: 'iPhone', price: 999 })
db.products.insertMany([{ name: 'A' }, { name: 'B' }])

// READ
db.products.find()
db.products.find({ isActive: true })
db.products.findOne({ slug: 'iphone-15' })
db.products.find({ price: { $gte: 100, $lte: 1000 } })
db.products.find({ brand: { $in: ['Apple', 'Samsung'] } })
db.products.find({ name: { $regex: /iphone/i } })
db.products.find({}, { name: 1, price: 1, _id: 0 })    // Projection
db.products.find().sort({ price: -1 }).skip(10).limit(10)

// UPDATE
db.products.updateOne({ _id: ObjectId('...') }, { $set: { price: 899 } })
db.products.updateMany({ isActive: false }, { $set: { stock: 0 } })
db.products.findOneAndUpdate({ slug: 'iphone' }, { $inc: { stock: -1 } }, { returnNewDocument: true })

// DELETE
db.products.deleteOne({ _id: ObjectId('...') })
db.products.deleteMany({ isActive: false })
```

---

## 🔍 Query Operators

```javascript
// Comparison
$eq    // Equal:            { price: { $eq: 100 } }
$ne    // Not equal:        { status: { $ne: 'inactive' } }
$gt    // Greater than:     { price: { $gt: 100 } }
$gte   // Greater or equal: { stock: { $gte: 1 } }
$lt    // Less than:        { price: { $lt: 500 } }
$lte   // Less or equal:    { price: { $lte: 1000 } }
$in    // In array:         { brand: { $in: ['Apple', 'Samsung'] } }
$nin   // Not in array:     { status: { $nin: ['deleted', 'banned'] } }

// Logical
$and   // { $and: [{ price: { $gt: 100 } }, { isActive: true }] }
$or    // { $or: [{ brand: 'Apple' }, { brand: 'Samsung' }] }
$not   // { price: { $not: { $gt: 1000 } } }
$nor   // { $nor: [{ isActive: false }, { stock: 0 }] }

// Element
$exists  // { phone: { $exists: true } }
$type    // { price: { $type: 'number' } }

// Array
$all        // { tags: { $all: ['phone', 'ios'] } }
$elemMatch  // { reviews: { $elemMatch: { rating: { $gte: 4 } } } }
$size       // { images: { $size: 3 } }

// Update operators
$set    // { $set: { price: 899 } }
$unset  // { $unset: { oldField: '' } }
$inc    // { $inc: { stock: -1, views: 1 } }
$push   // { $push: { tags: 'newTag' } }
$pull   // { $pull: { tags: 'oldTag' } }
$addToSet  // { $addToSet: { tags: 'unique' } }  // no duplicates
```

---

## 📊 Aggregation Pipeline

```javascript
db.orders.aggregate([
  { $match: { status: 'delivered' } },
  { $group: {
    _id: '$userId',
    totalOrders: { $sum: 1 },
    totalSpent: { $sum: '$total' },
  }},
  { $sort: { totalSpent: -1 } },
  { $limit: 10 },
  { $lookup: {
    from: 'users',
    localField: '_id',
    foreignField: '_id',
    as: 'user',
  }},
  { $unwind: '$user' },
  { $project: {
    _id: 0,
    name: '$user.firstName',
    email: '$user.email',
    totalOrders: 1,
    totalSpent: 1,
  }},
])
```

---

## 🏷️ Indexes

```javascript
db.products.createIndex({ slug: 1 })              // Single
db.products.createIndex({ price: 1, stock: -1 })  // Compound
db.products.createIndex({ name: 'text', description: 'text' })  // Text
db.products.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 })  // TTL
db.products.getIndexes()
db.products.dropIndex('slug_1')
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Appendix A](./appendix-a-sql.md) | [➡ Appendix C](./appendix-c-nestjs.md)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX C — NestJS CLI Commands
# "nest CLI Cheatsheet"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 🏗️ Project

```bash
# Install NestJS CLI globally
npm install -g @nestjs/cli

# New project
nest new my-project
nest new my-project --package-manager npm

# Project info
nest info
```

---

## ⚙️ Generate (Scaffold)

```bash
# Module
nest generate module users
nest g mo users       # shorthand

# Controller
nest generate controller users
nest g co users

# Service
nest generate service users
nest g s users

# Full resource (CRUD boilerplate)
nest generate resource users
# → Creates: module, controller, service, DTOs, entities

# Guard
nest g guard jwt-auth

# Interceptor
nest g interceptor transform

# Filter
nest g filter http-exception

# Pipe
nest g pipe parse-object-id

# Decorator
nest g decorator current-user

# Middleware
nest g middleware logger

# DTO class
nest g class users/dto/create-user.dto --no-spec

# Interface
nest g interface users/interfaces/user
```

---

## 🔧 Build & Run

```bash
# Development (watch mode)
npm run start:dev

# Production build
npm run build

# Run production build
npm run start:prod

# Debug mode
npm run start:debug
```

---

## 🗂️ Prisma Commands

```bash
# Init Prisma
npx prisma init

# Create migration
npx prisma migrate dev --name init
npx prisma migrate dev --name add_phone_to_users

# Apply migration (production)
npx prisma migrate deploy

# Reset database
npx prisma migrate reset

# Generate Prisma Client
npx prisma generate

# Open Prisma Studio
npx prisma studio

# Format schema
npx prisma format

# Validate schema
npx prisma validate
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Appendix B](./appendix-b-mongodb.md) | [➡ Appendix D](./appendix-d-packages.md)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX D — npm Packages Cheatsheet
# "এই Book-এ ব্যবহৃত সব Packages"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 🏗️ Core

| Package | Version | Purpose |
|---------|---------|---------|
| `express` | ^4.18 | Web framework |
| `@nestjs/core` | ^10 | NestJS core |
| `@nestjs/common` | ^10 | NestJS common |
| `@nestjs/platform-express` | ^10 | Express adapter |
| `@nestjs/config` | ^3 | Config module |

---

## 🗄️ Database

| Package | Version | Purpose |
|---------|---------|---------|
| `@prisma/client` | ^5 | Prisma client |
| `prisma` | ^5 | Prisma CLI (dev) |
| `mongoose` | ^8 | MongoDB ODM |
| `@nestjs/mongoose` | ^10 | Mongoose for NestJS |
| `ioredis` | ^5 | Redis client |

---

## 🔐 Auth & Security

| Package | Version | Purpose |
|---------|---------|---------|
| `bcryptjs` | ^2 | Password hashing |
| `jsonwebtoken` | ^9 | JWT (Express) |
| `@nestjs/jwt` | ^10 | JWT (NestJS) |
| `@nestjs/passport` | ^10 | Passport (NestJS) |
| `passport` | ^0.7 | Auth middleware |
| `passport-jwt` | ^4 | JWT strategy |
| `helmet` | ^7 | Security headers |
| `express-rate-limit` | ^7 | Rate limiting |
| `express-mongo-sanitize` | ^2 | NoSQL injection |
| `xss-clean` | ^0.1 | XSS prevention |
| `cors` | ^2 | CORS |

---

## ✅ Validation

| Package | Version | Purpose |
|---------|---------|---------|
| `express-validator` | ^7 | Express validation |
| `class-validator` | ^0.14 | NestJS validation |
| `class-transformer` | ^0.5 | DTO transformation |

---

## 📁 Files & Email

| Package | Version | Purpose |
|---------|---------|---------|
| `multer` | ^1 | File upload |
| `cloudinary` | ^1 | Cloudinary SDK |
| `multer-storage-cloudinary` | ^4 | Cloudinary storage |
| `nodemailer` | ^6 | Email sending |

---

## 📚 Docs & Logging

| Package | Version | Purpose |
|---------|---------|---------|
| `swagger-jsdoc` | ^6 | Swagger (Express) |
| `swagger-ui-express` | ^5 | Swagger UI |
| `@nestjs/swagger` | ^7 | Swagger (NestJS) |
| `winston` | ^3 | Logger |
| `winston-daily-rotate-file` | ^4 | Log rotation |

---

## 🧪 Testing

| Package | Version | Purpose |
|---------|---------|---------|
| `jest` | ^29 | Test runner |
| `supertest` | ^6 | HTTP testing |
| `@types/jest` | ^29 | Jest types |
| `@types/supertest` | ^6 | Supertest types |

---

## ⚡ Performance

| Package | Version | Purpose |
|---------|---------|---------|
| `compression` | ^1 | Response compression |

---

## 🚀 Install All (Express Project)

```bash
npm install express bcryptjs jsonwebtoken mongoose @prisma/client \
  express-validator helmet express-rate-limit cors express-mongo-sanitize \
  xss-clean multer cloudinary multer-storage-cloudinary nodemailer \
  swagger-jsdoc swagger-ui-express winston winston-daily-rotate-file \
  compression ioredis dotenv

npm install -D nodemon jest supertest @types/jest @types/supertest prisma
```

## 🚀 Install All (NestJS Project)

```bash
npm install @nestjs/config @nestjs/passport @nestjs/jwt @nestjs/mongoose \
  @nestjs/swagger swagger-ui-express \
  passport passport-jwt @prisma/client mongoose bcryptjs \
  class-validator class-transformer helmet express-rate-limit \
  cloudinary multer @nestjs/platform-express ioredis \
  winston winston-daily-rotate-file compression

npm install -D @types/passport-jwt @types/bcryptjs @types/multer prisma \
  @nestjs/testing jest supertest @types/jest @types/supertest ts-jest
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Appendix C](./appendix-c-nestjs.md) | [➡ Appendix E](./appendix-e-http-status.md)



# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX E — HTTP Status Codes
# "সব Status Codes একনজরে"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## ✅ 2xx Success

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 200 | OK | সফল GET, PATCH, PUT |
| 201 | Created | নতুন resource তৈরি (POST) |
| 202 | Accepted | Async operation শুরু হয়েছে |
| 204 | No Content | সফল DELETE (body নেই) |

---

## ↩️ 3xx Redirection

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 301 | Moved Permanently | Permanent redirect |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cache হিট |

---

## ❌ 4xx Client Errors

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 400 | Bad Request | Invalid input, validation fail |
| 401 | Unauthorized | Token নেই বা invalid |
| 403 | Forbidden | Token আছে, permission নেই |
| 404 | Not Found | Resource পাওয়া যায়নি |
| 405 | Method Not Allowed | GET-এর জায়গায় POST |
| 409 | Conflict | Duplicate (email already exists) |
| 410 | Gone | Resource permanently deleted |
| 413 | Payload Too Large | File too big |
| 415 | Unsupported Media Type | Wrong Content-Type |
| 422 | Unprocessable Entity | Semantic validation error |
| 429 | Too Many Requests | Rate limit exceeded |

---

## 💥 5xx Server Errors

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 500 | Internal Server Error | Unhandled exception |
| 502 | Bad Gateway | Upstream server error |
| 503 | Service Unavailable | Maintenance / overload |
| 504 | Gateway Timeout | Upstream timeout |

---

## 📊 REST Mapping

```
GET    /products      → 200 OK
POST   /products      → 201 Created
GET    /products/:id  → 200 OK or 404 Not Found
PATCH  /products/:id  → 200 OK or 404 Not Found
DELETE /products/:id  → 204 No Content or 404 Not Found

POST /auth/login      → 200 OK or 401 Unauthorized
POST /auth/register   → 201 Created or 409 Conflict
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Appendix D](./appendix-d-packages.md) | [➡ Appendix F](./appendix-f-vscode.md)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX E — HTTP Status Codes
# "সব Status Codes একনজরে"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## ✅ 2xx Success

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 200 | OK | সফল GET, PATCH, PUT |
| 201 | Created | নতুন resource তৈরি (POST) |
| 202 | Accepted | Async operation শুরু হয়েছে |
| 204 | No Content | সফল DELETE (body নেই) |

---

## ↩️ 3xx Redirection

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 301 | Moved Permanently | Permanent redirect |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cache হিট |

---

## ❌ 4xx Client Errors

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 400 | Bad Request | Invalid input, validation fail |
| 401 | Unauthorized | Token নেই বা invalid |
| 403 | Forbidden | Token আছে, permission নেই |
| 404 | Not Found | Resource পাওয়া যায়নি |
| 405 | Method Not Allowed | GET-এর জায়গায় POST |
| 409 | Conflict | Duplicate (email already exists) |
| 410 | Gone | Resource permanently deleted |
| 413 | Payload Too Large | File too big |
| 415 | Unsupported Media Type | Wrong Content-Type |
| 422 | Unprocessable Entity | Semantic validation error |
| 429 | Too Many Requests | Rate limit exceeded |

---

## 💥 5xx Server Errors

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| 500 | Internal Server Error | Unhandled exception |
| 502 | Bad Gateway | Upstream server error |
| 503 | Service Unavailable | Maintenance / overload |
| 504 | Gateway Timeout | Upstream timeout |

---

## 📊 REST Mapping

```
GET    /products      → 200 OK
POST   /products      → 201 Created
GET    /products/:id  → 200 OK or 404 Not Found
PATCH  /products/:id  → 200 OK or 404 Not Found
DELETE /products/:id  → 204 No Content or 404 Not Found

POST /auth/login      → 200 OK or 401 Unauthorized
POST /auth/register   → 201 Created or 409 Conflict
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Appendix D](./appendix-d-packages.md) | [➡ Appendix F](./appendix-f-vscode.md)



# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 APPENDIX F — VS Code Shortcuts & Extensions
# "Backend Developer Setup"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## ⌨️ Essential Shortcuts (Mac)

| Shortcut | Action |
|----------|--------|
| `Cmd + P` | Quick file open |
| `Cmd + Shift + P` | Command palette |
| `Cmd + B` | Toggle sidebar |
| `Cmd + J` | Toggle terminal |
| `` Ctrl + ` `` | Open terminal |
| `Cmd + D` | Select next occurrence |
| `Alt + Up/Down` | Move line |
| `Shift + Alt + Down` | Duplicate line |
| `Cmd + /` | Toggle comment |
| `Cmd + Shift + K` | Delete line |
| `F12` | Go to definition |
| `Alt + F12` | Peek definition |
| `Shift + F12` | Find all references |
| `F2` | Rename symbol |
| `Cmd + Shift + F` | Search in files |

---

## 🔌 Recommended Extensions

```
# Install via terminal:
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension Prisma.prisma
code --install-extension mongodb.mongodb-vscode
code --install-extension humao.rest-client
code --install-extension rangav.vscode-thunder-client
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension eamodio.gitlens
code --install-extension PKief.material-icon-theme
code --install-extension zhuangtongfa.material-theme
```

| Extension | Purpose |
|-----------|---------|
| ESLint | JS/TS linting |
| Prettier | Code formatting |
| Prisma | Schema syntax highlight |
| MongoDB for VS Code | DB explorer |
| REST Client (.http files) | API testing |
| Thunder Client | API testing GUI |
| GitLens | Git history |

---

## 📝 .http File (REST Client)

```http
### Register
POST http://localhost:3000/api/v1/auth/register
Content-Type: application/json

{
  "firstName": "Test",
  "lastName": "User",
  "email": "test@example.com",
  "password": "TestPass123!"
}

### Login
POST http://localhost:3000/api/v1/auth/login
Content-Type: application/json

{
  "email": "test@example.com",
  "password": "TestPass123!"
}

### Get Products
GET http://localhost:3000/api/v1/products?page=1&limit=10
Accept: application/json

### Create Product (auth required)
POST http://localhost:3000/api/v1/products
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Test Product",
  "sku": "TEST-001",
  "slug": "test-product",
  "price": 99.99,
  "stock": 10,
  "categoryId": "507f1f77bcf86cd799439011"
}
```

---

## 🛠️ .eslintrc.js (Node.js/Express)

```javascript
module.exports = {
  env: { node: true, es2022: true },
  extends: ['eslint:recommended'],
  parserOptions: { ecmaVersion: 2022 },
  rules: {
    'no-console': 'warn',
    'no-unused-vars': 'error',
    'no-var': 'error',
    'prefer-const': 'error',
    'eqeqeq': 'error',
    'no-eval': 'error',
  },
};
```

## 🎨 .prettierrc

```json
{
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100,
  "semi": true,
  "tabWidth": 2
}
```

---

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Appendix E](./appendix-e-http-status.md)

---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🎉 অভিনন্দন! তুমি সম্পূর্ণ বইটি পড়েছ!                 ║
║                                                              ║
║   Backend Development সম্পূর্ণ গাইড — COMPLETE ✅           ║
║                                                              ║
║   Node.js · Express · NestJS · PostgreSQL · MongoDB          ║
║   Prisma · Mongoose · JWT · Testing · Deployment            ║
║                                                              ║
║   এখন একটি real project তৈরি করো।                          ║
║   Practice ছাড়া কোনো skill আসে না।                         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```
