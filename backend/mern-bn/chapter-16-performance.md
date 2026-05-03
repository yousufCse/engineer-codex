
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 16 — Performance & Caching
# "Fast API — Redis + Query Optimization"
# ⏱ ~90 মিনিট · Progress: [███████████████░] 82%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ N+1 Query Problem ও solution
- ✅ Database query optimization
- ✅ Connection pooling
- ✅ Redis caching — cache-aside pattern
- ✅ Cache invalidation strategies
- ✅ Response compression

---

## 🏗️ Real-life Analogy

> Redis cache = রান্নাঘরের prep table — সব কিছু ready, দেরাজ খুলতে হবে না (DB query করতে হবে না)। Frequently used items prep table-এ থাকে।

---

## ⚠️ N+1 Query Problem

```javascript
// ============================================
// ❌ N+1 Problem — 1 query for products + N queries for images
// ============================================
const getProductsBad = async () => {
  const products = await Product.find();  // 1 query

  // প্রতিটি product-এর জন্য আলাদা query → N queries!
  for (const product of products) {
    product.reviews = await Review.find({ productId: product._id });
  }

  return products;
};
// Total queries: 1 + N (N = products count)
// 100 products = 101 queries! 🔴

// ============================================
// ✅ Solution — Single aggregate query
// ============================================
const getProductsGood = async () => {
  return Product.aggregate([
    { $match: { isActive: true } },
    {
      $lookup: {
        from: 'reviews',
        localField: '_id',
        foreignField: 'productId',
        as: 'reviews',
      },
    },
    {
      $addFields: {
        reviewCount: { $size: '$reviews' },
        avgRating: { $avg: '$reviews.rating' },
      },
    },
    { $project: { reviews: 0 } },  // reviews array include করবে না
  ]);
};
// Total queries: 1 ✅

// ============================================
// Prisma N+1 Solution — include
// ============================================
// ❌ N+1 with Prisma
const ordersBad = await prisma.order.findMany();
for (const order of ordersBad) {
  order.user = await prisma.user.findUnique({ where: { id: order.userId } });
}

// ✅ Single query with include
const ordersGood = await prisma.order.findMany({
  include: {
    user: { select: { id: true, firstName: true, email: true } },
    items: {
      include: {
        product: { select: { id: true, name: true, sku: true } },
      },
    },
  },
});
```

---

## 🔗 Connection Pooling

```javascript
// Prisma — pgBouncer/connection pool settings
// prisma/schema.prisma:
// datasource db {
//   provider = "postgresql"
//   url       = env("DATABASE_URL")
//   relationMode = "prisma"
// }

// DATABASE_URL-এ pool size set করো:
// postgresql://user:pass@host/db?connection_limit=10&pool_timeout=30

// ============================================
// Mongoose Connection Pooling
// ============================================
mongoose.connect(process.env.MONGODB_URI, {
  maxPoolSize: 10,         // Maximum concurrent connections
  minPoolSize: 2,          // Minimum connections to keep
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
  connectTimeoutMS: 10000,
});
```

---

## ⚡ Redis Caching

```bash
npm install ioredis
```

📄 File: `src/config/redis.config.js` · 🎯 উদ্দেশ্য: Redis connection

```javascript
const Redis = require('ioredis');

const redis = new Redis({
  host: process.env.REDIS_HOST || 'localhost',
  port: parseInt(process.env.REDIS_PORT || '6379', 10),
  password: process.env.REDIS_PASSWORD || undefined,
  db: 0,
  maxRetriesPerRequest: 3,
  enableReadyCheck: true,
  lazyConnect: true,
});

redis.on('connect', () => console.log('✅ Redis connected'));
redis.on('error', (err) => console.error('❌ Redis error:', err));

module.exports = redis;
```

📄 File: `src/utils/cache.util.js` · 🎯 উদ্দেশ্য: Cache helper

```javascript
const redis = require('../config/redis.config');

const CACHE_TTL = {
  SHORT: 60,          // 1 minute
  MEDIUM: 5 * 60,     // 5 minutes
  LONG: 30 * 60,      // 30 minutes
  VERY_LONG: 60 * 60, // 1 hour
};

// ============================================
// Cache-Aside Pattern
// ============================================
const getOrSet = async (key, fetchFn, ttl = CACHE_TTL.MEDIUM) => {
  try {
    // 1. Cache check করো
    const cached = await redis.get(key);
    if (cached) {
      return JSON.parse(cached);
    }

    // 2. DB থেকে fetch করো
    const data = await fetchFn();

    // 3. Cache-এ store করো
    if (data !== null && data !== undefined) {
      await redis.setex(key, ttl, JSON.stringify(data));
    }

    return data;
  } catch (redisError) {
    // Redis down হলে DB থেকে সরাসরি return করো
    console.error('Redis error, falling back to DB:', redisError.message);
    return fetchFn();
  }
};

// Delete cache
const invalidate = async (...keys) => {
  try {
    if (keys.length > 0) {
      await redis.del(...keys);
    }
  } catch (error) {
    console.error('Cache invalidation error:', error);
  }
};

// Pattern-based delete (wildcard)
const invalidatePattern = async (pattern) => {
  try {
    const keys = await redis.keys(pattern);
    if (keys.length > 0) {
      await redis.del(...keys);
    }
  } catch (error) {
    console.error('Cache pattern invalidation error:', error);
  }
};

// Cache keys factory
const cacheKeys = {
  product: (id) => `product:${id}`,
  productSlug: (slug) => `product:slug:${slug}`,
  products: (query) => `products:${JSON.stringify(query)}`,
  category: (id) => `category:${id}`,
  categories: () => 'categories:all',
  user: (id) => `user:${id}`,
};

module.exports = { getOrSet, invalidate, invalidatePattern, cacheKeys, CACHE_TTL };
```

📄 File: `src/controllers/cached-product.controller.js` · 🎯 উদ্দেশ্য: Product controller with caching

```javascript
const Product = require('../models/Product.model');
const { getOrSet, invalidate, invalidatePattern, cacheKeys, CACHE_TTL } = require('../utils/cache.util');
const ApiResponse = require('../utils/ApiResponse');
const { AppError } = require('../middleware/error.middleware');

// ============================================
// GET ALL — Cache products list
// ============================================
const getAllProducts = async (req, res, next) => {
  try {
    const queryKey = { ...req.query };
    const cacheKey = cacheKeys.products(queryKey);

    const result = await getOrSet(
      cacheKey,
      async () => {
        const { page = 1, limit = 10, sort = '-createdAt', ...filters } = req.query;
        const skip = (page - 1) * limit;
        const filter = { isActive: true };

        if (filters.category) filter['category.slug'] = filters.category;
        if (filters.brand) filter.brand = new RegExp(filters.brand, 'i');

        const [total, data] = await Promise.all([
          Product.countDocuments(filter),
          Product.find(filter).sort(sort).skip(skip).limit(+limit).lean(),
        ]);

        return { data, total, page: +page, limit: +limit };
      },
      CACHE_TTL.MEDIUM  // 5 minutes cache
    );

    ApiResponse.paginated(res, result.data, {
      total: result.total,
      page: result.page,
      limit: result.limit,
      totalPages: Math.ceil(result.total / result.limit),
      hasNextPage: result.page * result.limit < result.total,
      hasPreviousPage: result.page > 1,
    });
  } catch (error) {
    next(error);
  }
};

// ============================================
// GET BY SLUG — Cache individual product
// ============================================
const getProductBySlug = async (req, res, next) => {
  try {
    const { slug } = req.params;
    const cacheKey = cacheKeys.productSlug(slug);

    const product = await getOrSet(
      cacheKey,
      () => Product.findOne({ slug, isActive: true }).lean(),
      CACHE_TTL.LONG  // 30 minutes cache
    );

    if (!product) {
      throw new AppError(`Product '${slug}' not found`, 404);
    }

    ApiResponse.success(res, product);
  } catch (error) {
    next(error);
  }
};

// ============================================
// UPDATE — Invalidate cache
// ============================================
const updateProduct = async (req, res, next) => {
  try {
    const { id } = req.params;

    const product = await Product.findByIdAndUpdate(
      id,
      { $set: req.body },
      { new: true, runValidators: true }
    );

    if (!product) {
      throw new AppError('Product not found', 404);
    }

    // Cache invalidate করো
    await Promise.all([
      invalidate(cacheKeys.productSlug(product.slug)),
      invalidatePattern('products:*'),  // সব product list cache clear
    ]);

    ApiResponse.success(res, product, 'Product updated');
  } catch (error) {
    next(error);
  }
};

// ============================================
// DELETE — Invalidate cache
// ============================================
const deleteProduct = async (req, res, next) => {
  try {
    const { id } = req.params;

    const product = await Product.findByIdAndUpdate(id, { isActive: false });

    if (!product) {
      throw new AppError('Product not found', 404);
    }

    // Cache clear করো
    await invalidatePattern('products:*');
    await invalidate(cacheKeys.productSlug(product.slug));

    ApiResponse.noContent(res);
  } catch (error) {
    next(error);
  }
};

module.exports = { getAllProducts, getProductBySlug, updateProduct, deleteProduct };
```

---

## 📦 Response Compression

```bash
npm install compression
```

```javascript
const compression = require('compression');

// app.js-এ যোগ করো
app.use(compression({
  level: 6,                // Compression level (1-9, 6 = balanced)
  threshold: 1024,         // 1KB এর কম compress করবে না
  filter: (req, res) => {
    // Already compressed (images, videos) skip করো
    if (req.headers['x-no-compression']) return false;
    return compression.filter(req, res);
  },
}));
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| N+1 queries | Lazy loading loop | Batch query বা include/lookup |
| No cache invalidation | Stale data | Update/delete-এ cache clear |
| Caching everything | Cache pollution | শুধু read-heavy data cache করো |
| No Redis error handling | App crash | Fallback to DB |
| Connection pool too small | Query queue | Pool size বাড়াও |
| No index | Full table scan | Frequently queried fields index করো |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 16 — তুমি শিখলে                         ║
╠══════════════════════════════════════════════════════╣
║  • N+1 Problem: identify ও fix                      ║
║  • Prisma include vs loop                           ║
║  • MongoDB aggregate vs multiple queries            ║
║  • Connection pooling: Prisma + Mongoose            ║
║  • Redis: connect, get, setex, del                  ║
║  • Cache-aside pattern                              ║
║  • Cache invalidation on update/delete              ║
║  • Response compression                             ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 15](./chapter-15-testing.md) | [➡ Chapter 17](./chapter-17-deployment.md)
