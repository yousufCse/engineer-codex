
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 6 — Prisma ORM
# "Type-safe Database — SQL লেখার আর কষ্ট নেই"
# ⏱ ~120 মিনিট · Progress: [███████░░░] 35%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Prisma কী ও কেন Raw SQL-এর চেয়ে ভালো
- ✅ Prisma setup: install, init, datasource
- ✅ Prisma Schema Language সম্পূর্ণ গাইড
- ✅ Relations: one-to-one, one-to-many, many-to-many
- ✅ Migrations: create, apply, reset
- ✅ CRUD: create, findMany, findUnique, update, delete
- ✅ Filtering, Sorting, Pagination
- ✅ Transactions ও `$transaction`
- ✅ Prisma Studio GUI
- ✅ Prisma Client best practices

---

## 🏗️ Real-life Analogy

> Raw SQL লেখা = হাতে চিঠি লেখা। Prisma ORM = word processor — auto-correct, spell check, formatting সব আছে। একই কাজ, কিন্তু Prisma TypeScript autocomplete দেয়, typo ধরে, schema থেকে সব জানে।

```
🟢 Flutter তুলনা:
   Flutter-এ http package দিয়ে raw JSON parse করার
   চেয়ে Dio + Freezed ব্যবহার করা যেমন সহজ ও
   type-safe, Prisma-ও তেমনি raw SQL-এর চেয়ে
   অনেক সহজ এবং type-safe।
```

---

## 🗺️ Prisma Architecture

```mermaid
graph LR
    A["TypeScript Code\n(তোমার app)"] --> B["Prisma Client\n(Generated)"]
    B --> C["Prisma Engine\n(Rust binary)"]
    C --> D["PostgreSQL\n/ MongoDB\n/ MySQL"]
    
    E["schema.prisma\n(তোমার definition)"] --> F["prisma generate\n→ Creates Prisma Client"]
    E --> G["prisma migrate\n→ Creates SQL migrations"]
```

---

## ⚙️ Setup ও Installation

```bash
# Project setup
mkdir prisma-ecommerce && cd prisma-ecommerce
npm init -y

# Prisma install
npm install prisma --save-dev
npm install @prisma/client

# Express ও অন্যান্য
npm install express dotenv cors

# Prisma initialize করো
npx prisma init --datasource-provider postgresql
```

এটি তৈরি করবে:
```
prisma/
└── schema.prisma    ← তোমার database schema
.env                 ← DATABASE_URL এখানে
```

📄 File: `.env` · 🎯 উদ্দেশ্য: Database connection

```bash
DATABASE_URL="postgresql://postgres:yourpassword@localhost:5432/ecommerce_db?schema=public"
```

---

## 📝 Prisma Schema Language

📄 File: `prisma/schema.prisma` · 🎯 উদ্দেশ্য: E-commerce database schema

```prisma
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// ============================================
// ENUMS
// ============================================
enum UserRole {
  customer
  admin
  seller
}

enum OrderStatus {
  pending
  confirmed
  processing
  shipped
  delivered
  cancelled
  refunded
}

enum PaymentStatus {
  pending
  completed
  failed
  refunded
}

enum PaymentMethod {
  credit_card
  debit_card
  mobile_banking
  cod
}

// ============================================
// CATEGORY MODEL
// ============================================
model Category {
  id          Int        @id @default(autoincrement())
  name        String     @db.VarChar(100)
  slug        String     @unique @db.VarChar(100)
  description String?    @db.Text
  imageUrl    String?
  isActive    Boolean    @default(true)
  createdAt   DateTime   @default(now())
  updatedAt   DateTime   @updatedAt

  // Self-relation (parent-child categories)
  parentId    Int?
  parent      Category?  @relation("SubCategories", fields: [parentId], references: [id])
  children    Category[] @relation("SubCategories")

  // Relations
  products    Product[]

  @@map("categories")
}

// ============================================
// USER MODEL
// ============================================
model User {
  id                   Int       @id @default(autoincrement())
  email                String    @unique @db.VarChar(255)
  passwordHash         String    @map("password_hash") @db.VarChar(255)
  firstName            String    @map("first_name") @db.VarChar(100)
  lastName             String    @map("last_name") @db.VarChar(100)
  phone                String?   @db.VarChar(20)
  role                 UserRole  @default(customer)
  isEmailVerified      Boolean   @default(false) @map("is_email_verified")
  emailVerifyToken     String?   @map("email_verify_token")
  passwordResetToken   String?   @map("password_reset_token")
  passwordResetExpires DateTime? @map("password_reset_expires")
  refreshToken         String?   @map("refresh_token") @db.Text
  lastLoginAt          DateTime? @map("last_login_at")
  isActive             Boolean   @default(true) @map("is_active")
  createdAt            DateTime  @default(now()) @map("created_at")
  updatedAt            DateTime  @updatedAt @map("updated_at")

  // Relations
  addresses  Address[]
  orders     Order[]
  reviews    Review[]

  @@map("users")
}

// ============================================
// ADDRESS MODEL
// ============================================
model Address {
  id         Int      @id @default(autoincrement())
  label      String   @default("Home") @db.VarChar(50)
  street     String   @db.Text
  city       String   @db.VarChar(100)
  state      String?  @db.VarChar(100)
  postalCode String   @map("postal_code") @db.VarChar(20)
  country    String   @default("Bangladesh") @db.VarChar(100)
  isDefault  Boolean  @default(false) @map("is_default")
  createdAt  DateTime @default(now()) @map("created_at")

  // Relations
  userId  Int     @map("user_id")
  user    User    @relation(fields: [userId], references: [id], onDelete: Cascade)
  orders  Order[]

  @@map("addresses")
}

// ============================================
// PRODUCT MODEL
// ============================================
model Product {
  id                 Int       @id @default(autoincrement())
  sku                String    @unique @db.VarChar(100)
  name               String    @db.VarChar(255)
  slug               String    @unique @db.VarChar(255)
  description        String?   @db.Text
  price              Decimal   @db.Decimal(10, 2)
  comparePrice       Decimal?  @map("compare_price") @db.Decimal(10, 2)
  costPrice          Decimal?  @map("cost_price") @db.Decimal(10, 2)
  stock              Int       @default(0)
  lowStockThreshold  Int       @default(10) @map("low_stock_threshold")
  brand              String?   @db.VarChar(100)
  weight             Decimal?  @db.Decimal(8, 3)
  isActive           Boolean   @default(true) @map("is_active")
  isFeatured         Boolean   @default(false) @map("is_featured")
  metaTitle          String?   @map("meta_title") @db.VarChar(255)
  metaDescription    String?   @map("meta_description") @db.Text
  createdAt          DateTime  @default(now()) @map("created_at")
  updatedAt          DateTime  @updatedAt @map("updated_at")

  // Relations
  categoryId  Int?       @map("category_id")
  category    Category?  @relation(fields: [categoryId], references: [id], onDelete: SetNull)
  images      ProductImage[]
  orderItems  OrderItem[]
  reviews     Review[]

  @@index([categoryId])
  @@index([brand])
  @@index([isActive, isFeatured])
  @@map("products")
}

// ============================================
// PRODUCT IMAGE MODEL
// ============================================
model ProductImage {
  id         Int      @id @default(autoincrement())
  url        String   @db.Text
  altText    String?  @map("alt_text") @db.VarChar(255)
  isPrimary  Boolean  @default(false) @map("is_primary")
  sortOrder  Int      @default(0) @map("sort_order")
  createdAt  DateTime @default(now()) @map("created_at")

  productId  Int     @map("product_id")
  product    Product @relation(fields: [productId], references: [id], onDelete: Cascade)

  @@map("product_images")
}

// ============================================
// ORDER MODEL
// ============================================
model Order {
  id              Int         @id @default(autoincrement())
  orderNumber     String      @unique @map("order_number") @db.VarChar(50)
  status          OrderStatus @default(pending)
  subtotal        Decimal     @db.Decimal(10, 2)
  shippingCost    Decimal     @default(0) @map("shipping_cost") @db.Decimal(10, 2)
  discountAmount  Decimal     @default(0) @map("discount_amount") @db.Decimal(10, 2)
  taxAmount       Decimal     @default(0) @map("tax_amount") @db.Decimal(10, 2)
  totalAmount     Decimal     @map("total_amount") @db.Decimal(10, 2)
  shippingAddress Json        @map("shipping_address")
  notes           String?     @db.Text
  cancelledReason String?     @map("cancelled_reason") @db.Text
  createdAt       DateTime    @default(now()) @map("created_at")
  updatedAt       DateTime    @updatedAt @map("updated_at")

  // Relations
  userId     Int       @map("user_id")
  user       User      @relation(fields: [userId], references: [id])
  addressId  Int?      @map("address_id")
  address    Address?  @relation(fields: [addressId], references: [id])
  items      OrderItem[]
  payment    Payment?

  @@index([userId])
  @@index([status])
  @@index([createdAt])
  @@map("orders")
}

// ============================================
// ORDER ITEM MODEL
// ============================================
model OrderItem {
  id         Int     @id @default(autoincrement())
  quantity   Int
  unitPrice  Decimal @map("unit_price") @db.Decimal(10, 2)
  totalPrice Decimal @map("total_price") @db.Decimal(10, 2)
  createdAt  DateTime @default(now()) @map("created_at")

  orderId   Int     @map("order_id")
  order     Order   @relation(fields: [orderId], references: [id], onDelete: Cascade)
  productId Int     @map("product_id")
  product   Product @relation(fields: [productId], references: [id])

  @@map("order_items")
}

// ============================================
// PAYMENT MODEL
// ============================================
model Payment {
  id              Int           @id @default(autoincrement())
  transactionId   String?       @unique @map("transaction_id") @db.VarChar(255)
  amount          Decimal       @db.Decimal(10, 2)
  currency        String        @default("BDT") @db.VarChar(3)
  paymentMethod   PaymentMethod @map("payment_method")
  status          PaymentStatus @default(pending)
  gatewayResponse Json?         @map("gateway_response")
  paidAt          DateTime?     @map("paid_at")
  createdAt       DateTime      @default(now()) @map("created_at")
  updatedAt       DateTime      @updatedAt @map("updated_at")

  orderId Int   @unique @map("order_id")
  order   Order @relation(fields: [orderId], references: [id])

  @@map("payments")
}

// ============================================
// REVIEW MODEL
// ============================================
model Review {
  id        Int      @id @default(autoincrement())
  rating    Int
  title     String?  @db.VarChar(255)
  comment   String?  @db.Text
  isVerified Boolean @default(false) @map("is_verified")
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")

  userId    Int     @map("user_id")
  user      User    @relation(fields: [userId], references: [id])
  productId Int     @map("product_id")
  product   Product @relation(fields: [productId], references: [id])

  @@unique([userId, productId]) // একজন user একটি product-এ একটিই review
  @@index([productId])
  @@map("reviews")
}
```

---

## 🚀 Migrations

```bash
# প্রথম migration তৈরি করো
npx prisma migrate dev --name init

# এটি করবে:
# 1. prisma/migrations/TIMESTAMP_init/ directory তৈরি করবে
# 2. migration.sql file তৈরি করবে
# 3. Database-এ apply করবে
# 4. Prisma Client generate করবে

# Migration দেখো
npx prisma migrate status

# Schema পরিবর্তনের পর নতুন migration
npx prisma migrate dev --name add_coupon_table

# Production-এ apply করো (dry run নয়)
npx prisma migrate deploy

# Database reset করো (⚠️ সব data মুছে যাবে)
npx prisma migrate reset

# Prisma Client regenerate করো (schema পরিবর্তনের পর)
npx prisma generate

# Prisma Studio — GUI database viewer
npx prisma studio
```

---

## 🔌 Prisma Client Singleton

📄 File: `src/config/prisma.js` · 🎯 উদ্দেশ্য: Prisma Client singleton

```javascript
const { PrismaClient } = require('@prisma/client');

// Global ব্যবহার করো development-এ hot reload issue এড়াতে
const globalForPrisma = global;

const prisma = globalForPrisma.prisma || new PrismaClient({
  log: process.env.NODE_ENV === 'development'
    ? ['query', 'error', 'warn']
    : ['error'],
  errorFormat: 'pretty',
});

if (process.env.NODE_ENV !== 'production') {
  globalForPrisma.prisma = prisma;
}

module.exports = prisma;
```

---

## 📝 CRUD Operations

📄 File: `src/controllers/prisma-product.controller.js` · 🎯 উদ্দেশ্য: Complete CRUD with Prisma

```javascript
const prisma = require('../config/prisma');
const { AppError } = require('../middleware/error.middleware');
const ApiResponse = require('../utils/ApiResponse');

// ============================================
// CREATE
// ============================================
const createProduct = async (req, res, next) => {
  try {
    const { name, sku, slug, price, categoryId, brand, stock, description } = req.body;

    // Unique check (Prisma error থেকেও handle হবে, কিন্তু explicit check ভালো)
    const existing = await prisma.product.findFirst({
      where: {
        OR: [
          { sku },
          { slug },
        ],
      },
    });

    if (existing) {
      throw new AppError(
        existing.sku === sku ? 'SKU already exists' : 'Slug already exists',
        409
      );
    }

    const product = await prisma.product.create({
      data: {
        name,
        sku,
        slug,
        price,
        brand,
        stock: stock || 0,
        description,
        categoryId: categoryId || null,
      },
      include: {
        category: { select: { id: true, name: true, slug: true } },
        images: true,
      },
    });

    ApiResponse.created(res, product, 'Product created successfully');
  } catch (error) {
    next(error);
  }
};

// ============================================
// READ — List with Filtering, Sorting, Pagination
// ============================================
const getAllProducts = async (req, res, next) => {
  try {
    const {
      page = 1,
      limit = 10,
      sort = 'createdAt',
      order = 'desc',
      category,
      brand,
      minPrice,
      maxPrice,
      search,
      featured,
      inStock,
    } = req.query;

    const pageNum = parseInt(page, 10);
    const limitNum = parseInt(limit, 10);
    const skip = (pageNum - 1) * limitNum;

    // WHERE conditions build করো
    const where = {
      isActive: true,
    };

    if (category) {
      where.category = { slug: category };
    }

    if (brand) {
      where.brand = { equals: brand, mode: 'insensitive' };
    }

    if (minPrice || maxPrice) {
      where.price = {};
      if (minPrice) where.price.gte = parseFloat(minPrice);
      if (maxPrice) where.price.lte = parseFloat(maxPrice);
    }

    if (search) {
      where.OR = [
        { name: { contains: search, mode: 'insensitive' } },
        { description: { contains: search, mode: 'insensitive' } },
        { brand: { contains: search, mode: 'insensitive' } },
      ];
    }

    if (featured === 'true') {
      where.isFeatured = true;
    }

    if (inStock === 'true') {
      where.stock = { gt: 0 };
    }

    // Valid sort fields
    const validSortFields = ['createdAt', 'price', 'name', 'stock'];
    const sortField = validSortFields.includes(sort) ? sort : 'createdAt';
    const sortOrder = order === 'asc' ? 'asc' : 'desc';

    // Parallel queries (count + data)
    const [total, products] = await prisma.$transaction([
      prisma.product.count({ where }),
      prisma.product.findMany({
        where,
        skip,
        take: limitNum,
        orderBy: { [sortField]: sortOrder },
        include: {
          category: { select: { id: true, name: true, slug: true } },
          images: {
            where: { isPrimary: true },
            take: 1,
          },
          _count: { select: { reviews: true } },
        },
      }),
    ]);

    ApiResponse.paginated(res, products, {
      total,
      page: pageNum,
      limit: limitNum,
      totalPages: Math.ceil(total / limitNum),
      hasNextPage: skip + limitNum < total,
      hasPreviousPage: pageNum > 1,
    });
  } catch (error) {
    next(error);
  }
};

// ============================================
// READ — Single Product
// ============================================
const getProductById = async (req, res, next) => {
  try {
    const { id } = req.params;

    const product = await prisma.product.findUnique({
      where: { id: parseInt(id, 10) },
      include: {
        category: true,
        images: { orderBy: { sortOrder: 'asc' } },
        reviews: {
          take: 5,
          orderBy: { createdAt: 'desc' },
          include: {
            user: { select: { id: true, firstName: true, lastName: true } },
          },
        },
        _count: { select: { reviews: true } },
      },
    });

    if (!product) {
      throw new AppError(`Product with id ${id} not found`, 404);
    }

    // Review statistics
    const reviewStats = await prisma.review.aggregate({
      where: { productId: parseInt(id, 10) },
      _avg: { rating: true },
      _count: { rating: true },
    });

    ApiResponse.success(res, {
      ...product,
      avgRating: reviewStats._avg.rating || 0,
      totalReviews: reviewStats._count.rating,
    });
  } catch (error) {
    next(error);
  }
};

// GET by slug
const getProductBySlug = async (req, res, next) => {
  try {
    const { slug } = req.params;

    const product = await prisma.product.findUnique({
      where: { slug },
      include: {
        category: true,
        images: { orderBy: { sortOrder: 'asc' } },
      },
    });

    if (!product) {
      throw new AppError(`Product '${slug}' not found`, 404);
    }

    ApiResponse.success(res, product);
  } catch (error) {
    next(error);
  }
};

// ============================================
// UPDATE
// ============================================
const updateProduct = async (req, res, next) => {
  try {
    const { id } = req.params;

    // Exists check
    const existing = await prisma.product.findUnique({
      where: { id: parseInt(id, 10) },
    });

    if (!existing) {
      throw new AppError(`Product with id ${id} not found`, 404);
    }

    const product = await prisma.product.update({
      where: { id: parseInt(id, 10) },
      data: {
        ...req.body,
        id: undefined, // id change করা যাবে না
        createdAt: undefined, // createdAt change করা যাবে না
      },
      include: {
        category: { select: { id: true, name: true } },
        images: true,
      },
    });

    ApiResponse.success(res, product, 'Product updated successfully');
  } catch (error) {
    next(error);
  }
};

// ============================================
// DELETE (Soft Delete)
// ============================================
const deleteProduct = async (req, res, next) => {
  try {
    const { id } = req.params;

    const existing = await prisma.product.findUnique({
      where: { id: parseInt(id, 10) },
    });

    if (!existing) {
      throw new AppError(`Product with id ${id} not found`, 404);
    }

    // Soft delete — actually থাকে, শুধু hide হয়
    await prisma.product.update({
      where: { id: parseInt(id, 10) },
      data: { isActive: false },
    });

    ApiResponse.noContent(res);
  } catch (error) {
    next(error);
  }
};

module.exports = {
  createProduct,
  getAllProducts,
  getProductById,
  getProductBySlug,
  updateProduct,
  deleteProduct,
};
```

---

## 🔄 Transactions

📄 File: `src/controllers/prisma-order.controller.js` · 🎯 উদ্দেশ্য: Order placement with transaction

```javascript
const prisma = require('../config/prisma');

const createOrder = async (req, res, next) => {
  try {
    const { items, addressId, notes } = req.body;
    const userId = req.user.id;

    // Items validation
    if (!items || items.length === 0) {
      throw new AppError('Order must have at least one item', 400);
    }

    // Transaction দিয়ে order create করো
    const order = await prisma.$transaction(async (tx) => {
      // 1. Product stock check
      const productIds = items.map((item) => item.productId);
      const products = await tx.product.findMany({
        where: { id: { in: productIds }, isActive: true },
      });

      // সব products আছে কিনা check
      if (products.length !== items.length) {
        throw new AppError('One or more products not found or inactive', 400);
      }

      // Stock check
      for (const item of items) {
        const product = products.find((p) => p.id === item.productId);
        if (product.stock < item.quantity) {
          throw new AppError(
            `Insufficient stock for product: ${product.name}. Available: ${product.stock}`,
            400
          );
        }
      }

      // 2. Subtotal calculate করো
      const subtotal = items.reduce((sum, item) => {
        const product = products.find((p) => p.id === item.productId);
        return sum + Number(product.price) * item.quantity;
      }, 0);

      const shippingCost = subtotal > 1000 ? 0 : 100;
      const totalAmount = subtotal + shippingCost;

      // 3. Order number তৈরি করো
      const orderNumber = `ORD-${new Date().getFullYear()}${String(new Date().getMonth() + 1).padStart(2, '0')}-${Date.now().toString().slice(-6)}`;

      // 4. Shipping address পাও
      const address = await tx.address.findFirst({
        where: { id: addressId, userId },
      });

      if (!address) {
        throw new AppError('Shipping address not found', 404);
      }

      // 5. Order তৈরি করো
      const newOrder = await tx.order.create({
        data: {
          orderNumber,
          userId,
          addressId,
          subtotal,
          shippingCost,
          totalAmount,
          shippingAddress: {
            street: address.street,
            city: address.city,
            postalCode: address.postalCode,
            country: address.country,
          },
          notes,
          items: {
            create: items.map((item) => {
              const product = products.find((p) => p.id === item.productId);
              return {
                productId: item.productId,
                quantity: item.quantity,
                unitPrice: product.price,
                totalPrice: Number(product.price) * item.quantity,
              };
            }),
          },
        },
        include: {
          items: {
            include: {
              product: { select: { id: true, name: true, sku: true } },
            },
          },
        },
      });

      // 6. Stock কমাও
      for (const item of items) {
        await tx.product.update({
          where: { id: item.productId },
          data: { stock: { decrement: item.quantity } },
        });
      }

      return newOrder;
    }); // Transaction শেষ

    ApiResponse.created(res, order, 'Order placed successfully');
  } catch (error) {
    next(error);
  }
};

module.exports = { createOrder };
```

---

## 📊 Advanced Queries

```javascript
// ============================================
// Aggregations
// ============================================
const getProductStats = async () => {
  const stats = await prisma.product.aggregate({
    where: { isActive: true },
    _count: { id: true },
    _avg: { price: true, stock: true },
    _max: { price: true },
    _min: { price: true },
    _sum: { stock: true },
  });
  return stats;
};

// ============================================
// groupBy
// ============================================
const getProductsByCategory = async () => {
  return prisma.product.groupBy({
    by: ['categoryId', 'brand'],
    where: { isActive: true },
    _count: { id: true },
    _avg: { price: true },
    _sum: { stock: true },
    orderBy: { _count: { id: 'desc' } },
  });
};

// ============================================
// Raw SQL (যখন Prisma পারে না)
// ============================================
const getComplexStats = async () => {
  const result = await prisma.$queryRaw`
    SELECT
      c.name AS category,
      COUNT(p.id) AS product_count,
      SUM(p.stock * p.price) AS inventory_value,
      AVG(r.rating) AS avg_rating
    FROM categories c
    LEFT JOIN products p ON c.id = p.category_id AND p.is_active = TRUE
    LEFT JOIN reviews r ON p.id = r.product_id
    GROUP BY c.id, c.name
    ORDER BY inventory_value DESC NULLS LAST
  `;
  return result;
};

// Unsafe raw SQL (user input দিয়ে কখনো করো না!)
// SAFE way with parameters:
const searchProducts = async (searchTerm) => {
  return prisma.$queryRaw`
    SELECT id, name, price
    FROM products
    WHERE name ILIKE ${'%' + searchTerm + '%'}
    AND is_active = TRUE
    LIMIT 10
  `;
};

// ============================================
// Nested Write (Create with relations)
// ============================================
const createProductWithImages = async (data) => {
  return prisma.product.create({
    data: {
      name: data.name,
      sku: data.sku,
      slug: data.slug,
      price: data.price,
      category: {
        connect: { id: data.categoryId },
      },
      images: {
        create: data.images.map((img, index) => ({
          url: img.url,
          altText: img.altText,
          isPrimary: index === 0,
          sortOrder: index,
        })),
      },
    },
    include: { images: true, category: true },
  });
};

// ============================================
// Upsert — Create or Update
// ============================================
const upsertCategory = async (slug, data) => {
  return prisma.category.upsert({
    where: { slug },
    create: {
      ...data,
      slug,
    },
    update: {
      name: data.name,
      description: data.description,
    },
  });
};

// ============================================
// connectOrCreate
// ============================================
const createProductWithCategory = async (productData, categoryName) => {
  const slug = categoryName.toLowerCase().replace(/\s+/g, '-');
  return prisma.product.create({
    data: {
      ...productData,
      category: {
        connectOrCreate: {
          where: { slug },
          create: { name: categoryName, slug },
        },
      },
    },
  });
};
```

---

## 🎛️ Prisma Studio

```bash
# Browser-এ Prisma Studio খোলো
npx prisma studio

# এটি খুলবে: http://localhost:5555
# তুমি দেখতে পাবে:
# - সব tables ও তাদের data
# - Records add/edit/delete করতে পারবে
# - Relations navigate করতে পারবে
```

---

## 🏋️ Exercise

**কাজ: User Controller সম্পূর্ণ করো**

```javascript
// src/controllers/prisma-user.controller.js

const prisma = require('../config/prisma');
const bcrypt = require('bcryptjs');

// ১. getAllUsers — pagination + search
const getAllUsers = async (req, res, next) => {
  // তোমার কাজ: getAllProducts থেকে pattern নাও
  // include: orders count, addresses count
};

// ২. getUserById — user + orders + addresses
const getUserById = async (req, res, next) => {
  // তোমার কাজ
};

// ৩. updateUserProfile
const updateUserProfile = async (req, res, next) => {
  // তোমার কাজ
  // password change এর জন্য bcrypt.hash ব্যবহার করো
};

// ৪. getUserOrders — user-এর সব orders with items
const getUserOrders = async (req, res, next) => {
  // তোমার কাজ
};

module.exports = { getAllUsers, getUserById, updateUserProfile, getUserOrders };
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| Prisma Client প্রতিবার new করা | Connection pool শেষ হয় | Singleton pattern ব্যবহার করো |
| Transaction ছাড়া multi-step write | Partial update হতে পারে | `prisma.$transaction()` ব্যবহার করো |
| `include` সব জায়গায় দেওয়া | N+1 query ও over-fetching | শুধু দরকারি fields `select` করো |
| Error handle না করা | P2002/P2025 crash করবে | error.code check করো |
| Migration ছাড়া schema change | DB mismatch | সবসময় `prisma migrate dev` চালাও |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 6 — তুমি শিখলে                          ║
╠══════════════════════════════════════════════════════╣
║  • Prisma schema language সম্পূর্ণ                  ║
║  • Models, enums, relations define করা              ║
║  • Migrations: create, apply, reset                 ║
║  • CRUD: create/findMany/findUnique/update/delete   ║
║  • Filtering: where, contains, gte, lte, in, OR    ║
║  • Pagination: skip + take                          ║
║  • Include ও select দিয়ে relations                 ║
║  • Aggregations: aggregate, groupBy                 ║
║  • Raw SQL: $queryRaw                               ║
║  • Transactions: $transaction                       ║
║  • Nested writes: create with relations             ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 5](./chapter-05-postgresql.md) | [➡ Chapter 7](./chapter-07-mongodb.md)
