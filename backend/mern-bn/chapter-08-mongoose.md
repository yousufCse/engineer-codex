
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 8 — Mongoose ODM
# "MongoDB সাথে Type-safe, Validated Queries"
# ⏱ ~120 মিনিট · Progress: [█████████░] 45%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Mongoose কী ও কেন দরকার
- ✅ Connection: connect, events, options
- ✅ Schema: types, validators, default, virtual
- ✅ Model: create, query, update, delete
- ✅ Middleware hooks: pre/post save, remove, find
- ✅ Population: ref field-এর data আনা
- ✅ Pagination pattern
- ✅ Lean queries — performance
- ✅ Instance ও Static methods

---

## 🏗️ Real-life Analogy

> Prisma যেমন PostgreSQL-এর জন্য type-safe wrapper, Mongoose তেমনি MongoDB-এর জন্য। Prisma-তে schema.prisma-তে model define করো, Mongoose-এ JavaScript-এ Schema define করো। দুটোই raw query লেখার কষ্ট বাঁচায়।

```
🟢 Flutter তুলনা:
   Raw MongoDB queries = http package (manual JSON)
   Mongoose          = Dio + serialization (structured)
   
   Mongoose দিয়ে Flutter-এর Freezed-এর মতো
   type-safe, validated models পাও।
```

---

## 🗺️ Mongoose Architecture

```mermaid
graph TD
    A["JavaScript Code"] --> B["Mongoose Model"]
    B --> C["Mongoose Schema\n(validation, types)"]
    C --> D["Mongoose Driver"]
    D --> E["MongoDB Server"]

    F["Schema Middleware\n(pre/post hooks)"] --> C
    G["Virtuals\n(computed fields)"] --> C
    H["Instance Methods\n& Statics"] --> B
```

---

## ⚙️ Setup ও Connection

```bash
npm install mongoose
```

📄 File: `src/config/mongoose.js` · 🎯 উদ্দেশ্য: MongoDB connection with events

```javascript
const mongoose = require('mongoose');

const connectMongoDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGODB_URI, {
      // MongoDB Driver options
      maxPoolSize: 10,           // Maximum connections in pool
      serverSelectionTimeoutMS: 5000,  // 5 second server selection timeout
      socketTimeoutMS: 45000,    // Close sockets after 45 seconds of inactivity
      family: 4,                 // Use IPv4, skip trying IPv6
    });

    console.log(`✅ MongoDB Connected: ${conn.connection.host}`);
    console.log(`📂 Database: ${conn.connection.name}`);
  } catch (error) {
    console.error('❌ MongoDB connection error:', error.message);
    process.exit(1);
  }
};

// Connection Events
mongoose.connection.on('connected', () => {
  console.log('🟢 Mongoose connected to MongoDB');
});

mongoose.connection.on('error', (err) => {
  console.error('🔴 Mongoose connection error:', err);
});

mongoose.connection.on('disconnected', () => {
  console.log('🔴 Mongoose disconnected');
});

// Graceful shutdown
process.on('SIGINT', async () => {
  await mongoose.connection.close();
  console.log('MongoDB connection closed due to app termination');
  process.exit(0);
});

module.exports = connectMongoDB;
```

📄 File: `.env` · 🎯 উদ্দেশ্য: Environment variables

```bash
# Local
MONGODB_URI=mongodb://localhost:27017/ecommerce_db

# MongoDB Atlas (Production)
# MONGODB_URI=mongodb+srv://username:password@cluster0.abcde.mongodb.net/ecommerce_db?retryWrites=true&w=majority
```

📄 File: `src/index.js` · 🎯 উদ্দেশ্য: Connect MongoDB at startup

```javascript
const app = require('./app');
const connectMongoDB = require('./config/mongoose');
require('dotenv').config();

const PORT = process.env.PORT || 3000;

const startServer = async () => {
  // MongoDB connect করো
  await connectMongoDB();

  app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
  });
};

startServer();
```

---

## 📝 Schema Definition

📄 File: `src/models/Category.model.js` · 🎯 উদ্দেশ্য: Category schema

```javascript
const mongoose = require('mongoose');

const categorySchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, 'Category name is required'],
      trim: true,
      maxlength: [100, 'Name cannot exceed 100 characters'],
    },
    slug: {
      type: String,
      required: [true, 'Slug is required'],
      unique: true,
      lowercase: true,
      trim: true,
    },
    description: {
      type: String,
      trim: true,
    },
    imageUrl: String,
    isActive: {
      type: Boolean,
      default: true,
    },
    // Self-referencing for parent categories
    parent: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Category',
      default: null,
    },
  },
  {
    timestamps: true,  // createdAt ও updatedAt auto
    toJSON: { virtuals: true },
    toObject: { virtuals: true },
  }
);

// Virtual — children categories
categorySchema.virtual('children', {
  ref: 'Category',
  localField: '_id',
  foreignField: 'parent',
});

// Index
categorySchema.index({ slug: 1 }, { unique: true });
categorySchema.index({ isActive: 1 });

const Category = mongoose.model('Category', categorySchema);
module.exports = Category;
```

---

📄 File: `src/models/Product.model.js` · 🎯 উদ্দেশ্য: Complete Product schema with all Mongoose features

```javascript
const mongoose = require('mongoose');

// Nested Schema — ProductImage
const productImageSchema = new mongoose.Schema(
  {
    url: { type: String, required: true },
    altText: String,
    isPrimary: { type: Boolean, default: false },
    sortOrder: { type: Number, default: 0 },
  },
  { _id: true }
);

// Nested Schema — ProductRatings
const ratingsSchema = new mongoose.Schema(
  {
    average: { type: Number, default: 0, min: 0, max: 5 },
    count: { type: Number, default: 0 },
  },
  { _id: false }
);

// Nested Schema — Category (embedded snapshot)
const categoryRefSchema = new mongoose.Schema(
  {
    _id: { type: mongoose.Schema.Types.ObjectId, ref: 'Category' },
    name: String,
    slug: String,
  },
  { _id: false }
);

// ============================================
// Main Product Schema
// ============================================
const productSchema = new mongoose.Schema(
  {
    sku: {
      type: String,
      required: [true, 'SKU is required'],
      unique: true,
      uppercase: true,
      trim: true,
    },
    name: {
      type: String,
      required: [true, 'Product name is required'],
      trim: true,
      maxlength: [255, 'Name cannot exceed 255 characters'],
    },
    slug: {
      type: String,
      required: [true, 'Slug is required'],
      unique: true,
      lowercase: true,
      trim: true,
    },
    description: {
      type: String,
      trim: true,
    },
    price: {
      type: mongoose.Schema.Types.Decimal128,
      required: [true, 'Price is required'],
      get: (v) => v ? parseFloat(v.toString()) : null,  // getter for JSON
    },
    comparePrice: {
      type: mongoose.Schema.Types.Decimal128,
      get: (v) => v ? parseFloat(v.toString()) : null,
    },
    costPrice: {
      type: mongoose.Schema.Types.Decimal128,
      get: (v) => v ? parseFloat(v.toString()) : null,
    },
    stock: {
      type: Number,
      default: 0,
      min: [0, 'Stock cannot be negative'],
    },
    lowStockThreshold: {
      type: Number,
      default: 10,
    },
    brand: {
      type: String,
      trim: true,
    },
    weight: Number,
    images: [productImageSchema],
    specs: {
      type: mongoose.Schema.Types.Mixed,  // Flexible key-value
      default: {},
    },
    tags: [String],
    category: categoryRefSchema,
    ratings: {
      type: ratingsSchema,
      default: () => ({ average: 0, count: 0 }),
    },
    isActive: {
      type: Boolean,
      default: true,
    },
    isFeatured: {
      type: Boolean,
      default: false,
    },
    metaTitle: String,
    metaDescription: String,
  },
  {
    timestamps: true,
    toJSON: { getters: true, virtuals: true },  // getters for Decimal128
    toObject: { getters: true, virtuals: true },
  }
);

// ============================================
// INDEXES
// ============================================
productSchema.index({ slug: 1 }, { unique: true });
productSchema.index({ sku: 1 }, { unique: true });
productSchema.index({ 'category.slug': 1 });
productSchema.index({ brand: 1 });
productSchema.index({ isActive: 1, isFeatured: -1 });
productSchema.index({ price: 1 });
productSchema.index({ createdAt: -1 });
productSchema.index(
  { name: 'text', description: 'text', brand: 'text', tags: 'text' },
  {
    weights: { name: 10, brand: 5, tags: 3, description: 1 },
    name: 'product_text_index',
  }
);

// ============================================
// VIRTUAL FIELDS
// ============================================

// Discount percentage calculate
productSchema.virtual('discountPercentage').get(function () {
  if (this.comparePrice && this.comparePrice > this.price) {
    return Math.round(((this.comparePrice - this.price) / this.comparePrice) * 100);
  }
  return 0;
});

// isInStock
productSchema.virtual('isInStock').get(function () {
  return this.stock > 0;
});

// isLowStock
productSchema.virtual('isLowStock').get(function () {
  return this.stock > 0 && this.stock <= this.lowStockThreshold;
});

// primaryImage
productSchema.virtual('primaryImage').get(function () {
  if (!this.images || this.images.length === 0) return null;
  return this.images.find((img) => img.isPrimary) || this.images[0];
});

// ============================================
// MIDDLEWARE HOOKS
// ============================================

// Pre-save: slug auto-generate
productSchema.pre('save', function (next) {
  if (this.isModified('name') && !this.slug) {
    this.slug = this.name
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }
  next();
});

// Post-save: logging
productSchema.post('save', function (doc) {
  console.log(`Product saved: ${doc.sku} - ${doc.name}`);
});

// Pre-find: শুধু active products (globally apply করলে)
// productSchema.pre(/^find/, function (next) {
//   this.where({ isActive: true });  // সব find queries-এ apply
//   next();
// });

// ============================================
// STATIC METHODS — Model-level queries
// ============================================

// Active products
productSchema.statics.findActive = function (filter = {}) {
  return this.find({ ...filter, isActive: true });
};

// Featured products
productSchema.statics.findFeatured = function (limit = 10) {
  return this.find({ isActive: true, isFeatured: true }).limit(limit);
};

// Low stock products
productSchema.statics.findLowStock = function () {
  return this.find({
    isActive: true,
    $expr: { $lte: ['$stock', '$lowStockThreshold'] },
    stock: { $gt: 0 },
  });
};

// ============================================
// INSTANCE METHODS — Document-level
// ============================================

// Update ratings after review
productSchema.methods.updateRatings = async function (newRating) {
  const Review = mongoose.model('Review');
  const stats = await Review.aggregate([
    { $match: { productId: this._id, isVerified: true } },
    { $group: { _id: null, avg: { $avg: '$rating' }, count: { $sum: 1 } } },
  ]);

  if (stats.length > 0) {
    this.ratings.average = Math.round(stats[0].avg * 10) / 10;
    this.ratings.count = stats[0].count;
  } else {
    this.ratings.average = 0;
    this.ratings.count = 0;
  }

  return this.save();
};

// Decrement stock
productSchema.methods.decrementStock = async function (quantity) {
  if (this.stock < quantity) {
    throw new Error(`Insufficient stock. Available: ${this.stock}`);
  }
  this.stock -= quantity;
  return this.save();
};

const Product = mongoose.model('Product', productSchema);
module.exports = Product;
```

---

📄 File: `src/models/Review.model.js` · 🎯 উদ্দেশ্য: Review schema with post-save hook

```javascript
const mongoose = require('mongoose');

const reviewSchema = new mongoose.Schema(
  {
    productId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Product',
      required: [true, 'Product ID is required'],
      index: true,
    },
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      required: [true, 'User ID is required'],
      index: true,
    },
    rating: {
      type: Number,
      required: [true, 'Rating is required'],
      min: [1, 'Rating must be at least 1'],
      max: [5, 'Rating cannot exceed 5'],
    },
    title: {
      type: String,
      trim: true,
      maxlength: [255, 'Title cannot exceed 255 characters'],
    },
    comment: {
      type: String,
      trim: true,
    },
    isVerified: {
      type: Boolean,
      default: false,
    },
  },
  {
    timestamps: true,
    toJSON: { virtuals: true },
  }
);

// Compound unique index: একজন user একটি product-এ একটি review
reviewSchema.index({ userId: 1, productId: 1 }, { unique: true });

// Post-save: product ratings update করো
reviewSchema.post('save', async function () {
  const Product = mongoose.model('Product');
  const product = await Product.findById(this.productId);
  if (product) {
    await product.updateRatings();
  }
});

// Post-remove: product ratings update করো
reviewSchema.post('findOneAndDelete', async function (doc) {
  if (doc) {
    const Product = mongoose.model('Product');
    const product = await Product.findById(doc.productId);
    if (product) {
      await product.updateRatings();
    }
  }
});

const Review = mongoose.model('Review', reviewSchema);
module.exports = Review;
```

---

## 🔌 CRUD with Mongoose

📄 File: `src/controllers/mongoose-product.controller.js` · 🎯 উদ্দেশ্য: Complete CRUD operations

```javascript
const Product = require('../models/Product.model');
const { AppError } = require('../middleware/error.middleware');
const ApiResponse = require('../utils/ApiResponse');

// ============================================
// CREATE
// ============================================
const createProduct = async (req, res, next) => {
  try {
    const product = await Product.create(req.body);
    ApiResponse.created(res, product, 'Product created');
  } catch (error) {
    // Mongoose validation error
    if (error.name === 'ValidationError') {
      const messages = Object.values(error.errors).map((e) => e.message);
      return next(new AppError(messages.join(', '), 400));
    }
    // Duplicate key error
    if (error.code === 11000) {
      const field = Object.keys(error.keyValue)[0];
      return next(new AppError(`${field} already exists`, 409));
    }
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
      sort = '-createdAt',
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

    // Filter object তৈরি করো
    const filter = { isActive: true };

    if (category) filter['category.slug'] = category;
    if (brand) filter.brand = new RegExp(brand, 'i');
    if (minPrice || maxPrice) {
      filter.price = {};
      if (minPrice) filter.price.$gte = parseFloat(minPrice);
      if (maxPrice) filter.price.$lte = parseFloat(maxPrice);
    }
    if (featured === 'true') filter.isFeatured = true;
    if (inStock === 'true') filter.stock = { $gt: 0 };

    // Search query
    let query;
    if (search) {
      query = Product.find({ ...filter, $text: { $search: search } }, {
        score: { $meta: 'textScore' },
      }).sort({ score: { $meta: 'textScore' } });
    } else {
      query = Product.find(filter).sort(sort);
    }

    // Parallel execution: count + data
    const [total, products] = await Promise.all([
      Product.countDocuments(filter),
      query
        .skip(skip)
        .limit(limitNum)
        .select('-__v')
        .lean(),  // Plain JS objects (faster)
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
// READ — Single
// ============================================
const getProductBySlug = async (req, res, next) => {
  try {
    const product = await Product.findOne({ slug: req.params.slug, isActive: true })
      .populate('category._id', 'name slug')  // populated reference
      .lean();

    if (!product) {
      throw new AppError(`Product '${req.params.slug}' not found`, 404);
    }

    ApiResponse.success(res, product);
  } catch (error) {
    next(error);
  }
};

const getProductById = async (req, res, next) => {
  try {
    const product = await Product.findById(req.params.id).lean();

    if (!product) {
      throw new AppError('Product not found', 404);
    }

    ApiResponse.success(res, product);
  } catch (error) {
    // Invalid ObjectId
    if (error.name === 'CastError') {
      return next(new AppError('Invalid product ID', 400));
    }
    next(error);
  }
};

// ============================================
// UPDATE
// ============================================
const updateProduct = async (req, res, next) => {
  try {
    const product = await Product.findByIdAndUpdate(
      req.params.id,
      { $set: req.body },
      {
        new: true,          // Updated document return করো
        runValidators: true, // Validation চালাও
      }
    );

    if (!product) {
      throw new AppError('Product not found', 404);
    }

    ApiResponse.success(res, product, 'Product updated');
  } catch (error) {
    if (error.name === 'ValidationError') {
      const messages = Object.values(error.errors).map((e) => e.message);
      return next(new AppError(messages.join(', '), 400));
    }
    if (error.name === 'CastError') {
      return next(new AppError('Invalid product ID', 400));
    }
    next(error);
  }
};

// ============================================
// DELETE (Soft)
// ============================================
const deleteProduct = async (req, res, next) => {
  try {
    const product = await Product.findByIdAndUpdate(
      req.params.id,
      { isActive: false },
      { new: true }
    );

    if (!product) {
      throw new AppError('Product not found', 404);
    }

    ApiResponse.noContent(res);
  } catch (error) {
    if (error.name === 'CastError') {
      return next(new AppError('Invalid product ID', 400));
    }
    next(error);
  }
};

module.exports = {
  createProduct,
  getAllProducts,
  getProductBySlug,
  getProductById,
  updateProduct,
  deleteProduct,
};
```

---

## 🔗 Population (Referencing)

```javascript
// ============================================
// Basic populate
// ============================================
// reviews collection-এ userId আছে, user-এর info আনবো
const reviews = await Review.find({ productId: req.params.id })
  .populate('userId', 'firstName lastName email')  // শুধু এই fields
  .sort('-createdAt')
  .limit(10)
  .lean();

// ============================================
// Deep populate
// ============================================
// Orders → User → Address
const orders = await Order.find({ userId })
  .populate({
    path: 'items.productId',
    select: 'name sku price brand',
    model: 'Product',
  })
  .sort('-createdAt');

// ============================================
// populate ছাড়া — manual lookup (আরো control)
// ============================================
const getProductWithReviews = async (productId) => {
  const [product, reviews, stats] = await Promise.all([
    Product.findById(productId).lean(),
    Review.find({ productId, isVerified: true })
      .sort('-createdAt')
      .limit(5)
      .lean(),
    Review.aggregate([
      { $match: { productId: mongoose.Types.ObjectId.createFromHexString(productId) } },
      {
        $group: {
          _id: '$rating',
          count: { $sum: 1 },
        },
      },
    ]),
  ]);

  // Rating distribution
  const ratingDistribution = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
  stats.forEach(({ _id, count }) => {
    ratingDistribution[_id] = count;
  });

  return { product, reviews, ratingDistribution };
};
```

---

## 🚀 Advanced Patterns

```javascript
// ============================================
// .lean() — Performance
// ============================================
// .lean() Mongoose document instance তৈরি করে না
// Plain JS object return করে — much faster!

// ❌ Slow — full Mongoose document
const products = await Product.find({ isActive: true });

// ✅ Fast — plain JS objects
const products = await Product.find({ isActive: true }).lean();

// কিন্তু lean()-এ:
// - Virtuals কাজ করে না
// - Instance methods কাজ করে না
// - .save() কাজ করে না

// ============================================
// Bulk Operations
// ============================================
const bulkUpdatePrices = async (updates) => {
  const bulkOps = updates.map(({ id, price }) => ({
    updateOne: {
      filter: { _id: id },
      update: { $set: { price } },
    },
  }));

  const result = await Product.bulkWrite(bulkOps, { ordered: false });
  return result;
};

// ============================================
// Aggregate with Mongoose
// ============================================
const getCategoryStats = async () => {
  return Product.aggregate([
    { $match: { isActive: true } },
    {
      $group: {
        _id: '$category.slug',
        name: { $first: '$category.name' },
        count: { $sum: 1 },
        avgPrice: { $avg: '$price' },
      },
    },
    { $sort: { count: -1 } },
  ]);
};

// ============================================
// Transactions — Multi-document
// ============================================
const createOrderWithMongo = async (orderData) => {
  const session = await mongoose.startSession();
  session.startTransaction();

  try {
    // Stock check and decrement
    for (const item of orderData.items) {
      const product = await Product.findById(item.productId).session(session);
      if (!product || product.stock < item.quantity) {
        throw new Error(`Insufficient stock for: ${product?.name || item.productId}`);
      }

      await Product.findByIdAndUpdate(
        item.productId,
        { $inc: { stock: -item.quantity } },
        { session }
      );
    }

    // Order create
    const order = await Order.create([orderData], { session });

    await session.commitTransaction();
    return order[0];
  } catch (error) {
    await session.abortTransaction();
    throw error;
  } finally {
    await session.endSession();
  }
};
```

---

## 🏋️ Exercise: Review System

**কাজ: Review Controller সম্পূর্ণ করো**

```javascript
// src/controllers/review.controller.js
const Review = require('../models/Review.model');
const Product = require('../models/Product.model');

// ১. createReview
//    - একজন user একটি product-এ একবারই review করতে পারবে
//    - 11000 duplicate error handle করো

// ২. getProductReviews
//    - productId দিয়ে সব reviews আনো
//    - pagination + sort (newest/oldest/highest/lowest rating)
//    - populate user info

// ৩. updateReview
//    - শুধু owner update করতে পারবে
//    - req.user.id === review.userId check

// ৪. deleteReview
//    - শুধু owner বা admin delete করতে পারবে

// ৫. getMyReviews
//    - current user-এর সব reviews
//    - populate product info
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| `mongoose.connect()` await না করা | Queries connection ছাড়া run করে | `await connectMongoDB()` করো |
| ObjectId string compare | Type mismatch | `mongoose.Types.ObjectId.createFromHexString(id)` |
| lean() এ save() call করা | Plain object-এ নেই | lean ছাড়া fetch করো |
| populate ছাড়া deep nested query | N+1 problem | populate বা aggregate ব্যবহার করো |
| runValidators: true না দেওয়া | Update-এ validation চলে না | `{ new: true, runValidators: true }` |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 8 — তুমি শিখলে                          ║
╠══════════════════════════════════════════════════════╣
║  • Mongoose connect ও connection events              ║
║  • Schema: types, validators, defaults               ║
║  • Nested schemas ও Mixed type                      ║
║  • Virtuals — computed fields                       ║
║  • Pre/Post middleware hooks                         ║
║  • Instance methods ও Static methods                ║
║  • CRUD: create/find/findById/update/delete         ║
║  • Filtering, sorting, pagination with .lean()      ║
║  • Population: populate() ও aggregate lookup        ║
║  • Transactions with session                        ║
║  • Bulk write operations                            ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 7](./chapter-07-mongodb.md) | [➡ Chapter 9](./chapter-09-auth.md)
