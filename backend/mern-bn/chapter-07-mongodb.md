
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 7 — MongoDB
# "Document Database — Flexible Data Storage"
# ⏱ ~120 মিনিট · Progress: [████████░░] 40%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Document DB vs Relational DB — কখন কোনটা
- ✅ BSON data types সম্পূর্ণ গাইড
- ✅ mongosh দিয়ে CRUD operations
- ✅ Query operators: comparison, logical, array, element
- ✅ Aggregation pipeline — MongoDB-এর superpower
- ✅ Indexes: single, compound, text, geospatial
- ✅ Schema design patterns: embedding vs referencing
- ✅ E-commerce MongoDB schema

---

## 🏗️ Real-life Analogy

> PostgreSQL যদি হয় সুশৃঙ্খল ফাইলিং সিস্টেম যেখানে প্রতিটি কাগজের নির্দিষ্ট জায়গা আছে, MongoDB হলো একটি বড় বাক্স যেখানে যেকোনো আকারের document রাখা যায়। Product-এর কিছুতে color আছে, কিছুতে নেই — MongoDB-তে সমস্যা নেই।

```
🟢 Flutter তুলনা:
   PostgreSQL = Dart class (fixed fields)
   MongoDB   = Map<String, dynamic> (flexible)
   
   Flutter-এ API response parse করলে যেমন
   dynamic JSON আসে, MongoDB document-ও
   তেমনি flexible।
```

---

## 🗺️ MongoDB vs PostgreSQL — কখন কোনটা?

```mermaid
graph TD
    A[Data কী ধরনের?] --> B{Structure?}
    B -->|Fixed, Relational| C[PostgreSQL]
    B -->|Flexible, Hierarchical| D[MongoDB]
    
    C --> C1[Users, Orders, Payments]
    C --> C2[Financial Data]
    C --> C3[Complex Joins দরকার]
    
    D --> D1[Products, Reviews, Catalog]
    D --> D2[Real-time Analytics]
    D --> D3[Variable Schema]
```

```
🗄️ PostgreSQL vs MongoDB:

┌─────────────────┬──────────────────┬──────────────────┐
│ বিষয়           │ PostgreSQL       │ MongoDB          │
├─────────────────┼──────────────────┼──────────────────┤
│ Structure       │ Table/Row/Column │ Collection/Doc   │
│ Schema          │ Fixed, strict    │ Flexible         │
│ Relations       │ JOINs            │ Embedding/Ref    │
│ ACID            │ Full ACID        │ Partial (v4+)    │
│ Scalability     │ Vertical         │ Horizontal       │
│ Query Language  │ SQL              │ MQL (JSON-like)  │
│ Aggregation     │ Window Functions │ Pipeline         │
│ Best for        │ Orders, Users    │ Products, Catalog│
└─────────────────┴──────────────────┴──────────────────┘
```

---

## 📦 BSON Data Types

```
╭─────────────────────────────────────────────────────╮
│ 🔑 Concept: BSON                                    │
│ সহজ ভাষায়: Binary JSON — MongoDB internally        │
│            data যেভাবে store করে। JSON-এর চেয়ে    │
│            বেশি types support করে।                  │
╰─────────────────────────────────────────────────────╯
```

| BSON Type | JS Type | উদাহরণ |
|-----------|---------|---------|
| Double | `number` | `3.14` |
| String | `string` | `"iPhone"` |
| Object | `object` | `{ name: "Apple" }` |
| Array | `array` | `[1, 2, 3]` |
| ObjectId | `ObjectId` | `ObjectId("507f1...")` |
| Boolean | `boolean` | `true / false` |
| Date | `Date` | `new Date()` |
| Null | `null` | `null` |
| Integer (32/64 bit) | `number` | `42` |
| Decimal128 | `Decimal128` | Financial values |
| Binary | `Buffer` | Image data |

---

## 💻 mongosh — MongoDB Shell

### Connect ও Basic Commands

```javascript
// mongosh চালাও
mongosh

// অথবা connection string দিয়ে
mongosh "mongodb://localhost:27017"
mongosh "mongodb+srv://user:pass@cluster.mongodb.net/ecommerce"

// Databases দেখো
show dbs

// Database select করো বা তৈরি করো
use ecommerce_db

// Collections দেখো
show collections

// Current database
db

// Help
help
db.help()
```

### Collection তৈরি ও Drop

```javascript
// Explicitly তৈরি করো
db.createCollection("products", {
  capped: false,
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "price", "sku"],
      properties: {
        name: { bsonType: "string", description: "must be a string" },
        price: { bsonType: "decimal", minimum: 0 },
        sku: { bsonType: "string" }
      }
    }
  }
});

// Drop করো
db.products.drop();

// Database drop করো (⚠️ সব data মুছে যাবে)
db.dropDatabase();
```

---

## 📝 CRUD Operations

### Insert

📄 File: `examples/ch07/mongosh-crud.js` · 🎯 উদ্দেশ্য: MongoDB CRUD in mongosh

```javascript
// ============================================
// INSERT
// ============================================

// একটি document insert করো
db.products.insertOne({
  sku: "APPL-IP15P-256-BLK",
  name: "iPhone 15 Pro",
  slug: "iphone-15-pro",
  price: NumberDecimal("999.99"),
  comparePrice: NumberDecimal("1099.99"),
  category: {
    _id: ObjectId("507f1f77bcf86cd799439011"),
    name: "Phones",
    slug: "phones"
  },
  brand: "Apple",
  stock: 50,
  images: [
    { url: "https://cdn.myshop.com/iphone15pro-1.jpg", isPrimary: true },
    { url: "https://cdn.myshop.com/iphone15pro-2.jpg", isPrimary: false }
  ],
  specs: {
    color: "Black Titanium",
    storage: "256GB",
    ram: "8GB",
    processor: "A17 Pro",
    camera: "48MP Triple System",
    battery: "3274 mAh"
  },
  tags: ["iphone", "apple", "smartphone", "5g"],
  isActive: true,
  isFeatured: true,
  ratings: {
    average: 0,
    count: 0
  },
  createdAt: new Date(),
  updatedAt: new Date()
});

// ফলাফল:
// { acknowledged: true, insertedId: ObjectId("...") }

// একাধিক documents insert করো
db.products.insertMany([
  {
    sku: "SAMS-GS24U-256-BLK",
    name: "Samsung Galaxy S24 Ultra",
    slug: "samsung-galaxy-s24-ultra",
    price: NumberDecimal("1199.99"),
    brand: "Samsung",
    stock: 30,
    category: { name: "Phones", slug: "phones" },
    specs: { color: "Titanium Black", storage: "256GB" },
    tags: ["samsung", "android", "smartphone"],
    isActive: true,
    isFeatured: false,
    ratings: { average: 0, count: 0 },
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    sku: "APPL-MBP-M3-512-SLV",
    name: "MacBook Pro M3",
    slug: "macbook-pro-m3",
    price: NumberDecimal("1999.99"),
    brand: "Apple",
    stock: 20,
    category: { name: "Laptops", slug: "laptops" },
    specs: { color: "Silver", storage: "512GB", ram: "18GB" },
    tags: ["macbook", "apple", "laptop"],
    isActive: true,
    isFeatured: true,
    ratings: { average: 0, count: 0 },
    createdAt: new Date(),
    updatedAt: new Date()
  }
]);
```

### Find (Read)

```javascript
// ============================================
// FIND — সব documents
// ============================================
db.products.find()

// Pretty print
db.products.find().pretty()

// Projection — শুধু নির্দিষ্ট fields (1=show, 0=hide)
db.products.find({}, { name: 1, price: 1, brand: 1, _id: 0 })

// ============================================
// FIND — Filter করো
// ============================================

// Exact match
db.products.find({ brand: "Apple" })
db.products.find({ isActive: true, isFeatured: true })

// Comparison operators
db.products.find({ price: { $gt: 500 } })        // > 500
db.products.find({ price: { $gte: 500 } })       // >= 500
db.products.find({ price: { $lt: 1000 } })       // < 1000
db.products.find({ price: { $lte: 1000 } })      // <= 1000
db.products.find({ price: { $ne: 999.99 } })     // != 999.99
db.products.find({ price: { $in: [999.99, 1999.99] } }) // in array
db.products.find({ price: { $nin: [0, null] } }) // not in array

// Range
db.products.find({ price: { $gte: 500, $lte: 1500 } })

// Logical operators
db.products.find({
  $and: [
    { brand: "Apple" },
    { price: { $lt: 1500 } }
  ]
})

// $or
db.products.find({
  $or: [
    { brand: "Apple" },
    { brand: "Samsung" }
  ]
})

// $not
db.products.find({ price: { $not: { $gt: 1000 } } })

// ============================================
// Nested Field Query
// ============================================
// Dot notation দিয়ে
db.products.find({ "category.slug": "phones" })
db.products.find({ "specs.color": "Black Titanium" })
db.products.find({ "ratings.average": { $gte: 4 } })

// ============================================
// Array Query
// ============================================
// Array-এ element আছে কিনা
db.products.find({ tags: "apple" })  // array contains "apple"

// $all — সব elements থাকতে হবে
db.products.find({ tags: { $all: ["apple", "smartphone"] } })

// $elemMatch — array element-এ complex condition
db.reviews.find({
  comments: {
    $elemMatch: { rating: { $gte: 4 }, verified: true }
  }
})

// Array size
db.products.find({ images: { $size: 2 } })  // exactly 2 images

// ============================================
// Element Operators
// ============================================
// Field exists কিনা
db.products.find({ comparePrice: { $exists: true } })
db.products.find({ brand: { $exists: false } })

// Type check
db.products.find({ price: { $type: "decimal" } })
db.products.find({ tags: { $type: "array" } })

// ============================================
// Text Search
// ============================================
// আগে text index তৈরি করো:
db.products.createIndex({ name: "text", description: "text" })

// Then search:
db.products.find({ $text: { $search: "iPhone Pro" } })
db.products.find({ $text: { $search: "\"iPhone 15\"" } }) // exact phrase

// ============================================
// Regex
// ============================================
db.products.find({ name: { $regex: /iphone/i } }) // case-insensitive

// ============================================
// Sort, Limit, Skip (Pagination)
// ============================================
db.products
  .find({ isActive: true })
  .sort({ price: -1, name: 1 })  // price DESC, name ASC
  .skip(20)                       // page 3 (20 per page)
  .limit(10)

// Count
db.products.countDocuments({ brand: "Apple" })
db.products.estimatedDocumentCount()  // approximate (faster)

// findOne
db.products.findOne({ slug: "iphone-15-pro" })
db.products.findOne({ _id: ObjectId("507f1f77bcf86cd799439011") })
```

### Update

```javascript
// ============================================
// UPDATE
// ============================================

// $set — field update করো
db.products.updateOne(
  { sku: "APPL-IP15P-256-BLK" },
  {
    $set: {
      price: NumberDecimal("899.99"),
      "specs.color": "Natural Titanium",
      updatedAt: new Date()
    }
  }
)

// $inc — number increment করো
db.products.updateOne(
  { sku: "APPL-IP15P-256-BLK" },
  { $inc: { stock: -1 } }  // stock কমাও
)

// $push — array-এ element যোগ করো
db.products.updateOne(
  { sku: "APPL-IP15P-256-BLK" },
  {
    $push: {
      images: {
        url: "https://cdn.myshop.com/iphone15pro-3.jpg",
        isPrimary: false
      }
    }
  }
)

// $addToSet — duplicate ছাড়া array-এ add করো
db.products.updateOne(
  { sku: "APPL-IP15P-256-BLK" },
  { $addToSet: { tags: "pro" } }
)

// $pull — array থেকে element সরাও
db.products.updateOne(
  { sku: "APPL-IP15P-256-BLK" },
  { $pull: { tags: "old-tag" } }
)

// $unset — field delete করো
db.products.updateOne(
  { sku: "APPL-IP15P-256-BLK" },
  { $unset: { temporaryField: "" } }
)

// updateMany
db.products.updateMany(
  { brand: "Apple" },
  { $set: { "ratings.verified": true, updatedAt: new Date() } }
)

// Upsert — নেই তো তৈরি করো
db.products.updateOne(
  { sku: "NEW-SKU-001" },
  { $setOnInsert: { createdAt: new Date() }, $set: { name: "New Product", price: NumberDecimal("99.99") } },
  { upsert: true }
)

// findOneAndUpdate — updated document return করো
const updated = db.products.findOneAndUpdate(
  { sku: "APPL-IP15P-256-BLK" },
  { $set: { isFeatured: true } },
  { returnDocument: "after" }  // নতুন document return করো
)
```

### Delete

```javascript
// ============================================
// DELETE
// ============================================

// একটি delete করো
db.products.deleteOne({ sku: "OLD-SKU-001" })

// Multiple delete করো
db.products.deleteMany({ isActive: false })

// findOneAndDelete — deleted document return করো
const deleted = db.products.findOneAndDelete({ sku: "TEMP-SKU" })
```

---

## 🔥 Aggregation Pipeline

```
╭─────────────────────────────────────────────────────╮
│ 🔑 Concept: Aggregation Pipeline                    │
│ সহজ ভাষায়: Documents একের পর এক stages-এর          │
│            মধ্যে দিয়ে যায়, প্রতিটি stage           │
│            transform করে। SQL-এর complex           │
│            GROUP BY + JOIN এর equivalent।           │
╰─────────────────────────────────────────────────────╯
```

```mermaid
graph LR
    A["Collection\n(Products)"] --> B["$match\n(filter)"]
    B --> C["$group\n(aggregate)"]
    C --> D["$sort\n(order)"]
    D --> E["$limit\n(paginate)"]
    E --> F["$project\n(shape)"]
    F --> G["Result"]
```

### Aggregation Examples

📄 File: `examples/ch07/aggregation.js` · 🎯 উদ্দেশ্য: Aggregation pipeline

```javascript
// ============================================
// Category Statistics
// ============================================
db.products.aggregate([
  // Stage 1: Filter active products
  { $match: { isActive: true } },

  // Stage 2: Group by category
  {
    $group: {
      _id: "$category.slug",
      categoryName: { $first: "$category.name" },
      productCount: { $sum: 1 },
      avgPrice: { $avg: "$price" },
      maxPrice: { $max: "$price" },
      minPrice: { $min: "$price" },
      totalStock: { $sum: "$stock" },
      brands: { $addToSet: "$brand" }
    }
  },

  // Stage 3: Sort by product count
  { $sort: { productCount: -1 } },

  // Stage 4: Format output
  {
    $project: {
      _id: 0,
      category: "$_id",
      categoryName: 1,
      productCount: 1,
      avgPrice: { $round: ["$avgPrice", 2] },
      maxPrice: 1,
      minPrice: 1,
      totalStock: 1,
      brandCount: { $size: "$brands" }
    }
  }
]);

// ============================================
// Product Reviews Statistics (lookup)
// ============================================
db.reviews.aggregate([
  // Stage 1: Match verified reviews
  { $match: { isVerified: true, rating: { $gte: 1 } } },

  // Stage 2: Group by product
  {
    $group: {
      _id: "$productId",
      avgRating: { $avg: "$rating" },
      reviewCount: { $sum: 1 },
      ratings: { $push: "$rating" },
      recentReview: { $last: "$createdAt" }
    }
  },

  // Stage 3: Lookup product details
  {
    $lookup: {
      from: "products",
      localField: "_id",
      foreignField: "_id",
      as: "product",
      pipeline: [
        { $project: { name: 1, price: 1, brand: 1, sku: 1 } }
      ]
    }
  },

  // Stage 4: Unwind lookup result
  { $unwind: { path: "$product", preserveNullAndEmpty: false } },

  // Stage 5: Filter only well-rated products
  { $match: { avgRating: { $gte: 4.0 }, reviewCount: { $gte: 5 } } },

  // Stage 6: Sort and limit
  { $sort: { avgRating: -1, reviewCount: -1 } },
  { $limit: 10 },

  // Stage 7: Final projection
  {
    $project: {
      _id: 0,
      productId: "$_id",
      productName: "$product.name",
      sku: "$product.sku",
      price: "$product.price",
      avgRating: { $round: ["$avgRating", 1] },
      reviewCount: 1,
      recentReview: 1
    }
  }
]);

// ============================================
// Sales Report (last 30 days)
// ============================================
db.orders.aggregate([
  // Filter by date range
  {
    $match: {
      status: { $in: ["delivered", "shipped"] },
      createdAt: { $gte: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000) }
    }
  },

  // Unwind order items
  { $unwind: "$items" },

  // Group by product
  {
    $group: {
      _id: "$items.productId",
      totalQuantitySold: { $sum: "$items.quantity" },
      totalRevenue: { $sum: "$items.totalPrice" },
      orderCount: { $sum: 1 }
    }
  },

  // Lookup product info
  {
    $lookup: {
      from: "products",
      localField: "_id",
      foreignField: "_id",
      as: "product",
      pipeline: [{ $project: { name: 1, sku: 1, brand: 1, category: 1 } }]
    }
  },
  { $unwind: "$product" },

  { $sort: { totalRevenue: -1 } },
  { $limit: 20 },

  {
    $project: {
      productName: "$product.name",
      sku: "$product.sku",
      brand: "$product.brand",
      category: "$product.category.name",
      totalQuantitySold: 1,
      totalRevenue: { $round: ["$totalRevenue", 2] },
      orderCount: 1
    }
  }
]);

// ============================================
// $facet — Multiple pipelines in one query
// ============================================
db.products.aggregate([
  { $match: { isActive: true } },
  {
    $facet: {
      // Facet 1: Category breakdown
      byCategory: [
        { $group: { _id: "$category.slug", count: { $sum: 1 } } },
        { $sort: { count: -1 } }
      ],

      // Facet 2: Price ranges
      priceRanges: [
        {
          $bucket: {
            groupBy: "$price",
            boundaries: [0, 100, 500, 1000, 2000, 5000],
            default: "5000+",
            output: { count: { $sum: 1 }, avgPrice: { $avg: "$price" } }
          }
        }
      ],

      // Facet 3: Brand counts
      byBrand: [
        { $group: { _id: "$brand", count: { $sum: 1 } } },
        { $sort: { count: -1 } },
        { $limit: 10 }
      ],

      // Facet 4: Total count
      total: [{ $count: "count" }]
    }
  }
]);
```

---

## 🔍 Indexes

```javascript
// ============================================
// Single Field Index
// ============================================
db.products.createIndex({ slug: 1 }, { unique: true })
db.products.createIndex({ brand: 1 })
db.products.createIndex({ createdAt: -1 })  // -1 = descending

// ============================================
// Compound Index
// ============================================
db.products.createIndex({ "category.slug": 1, price: 1 })
db.products.createIndex({ isActive: 1, isFeatured: -1, createdAt: -1 })

// ============================================
// Text Index (Full Text Search)
// ============================================
db.products.createIndex(
  { name: "text", description: "text", brand: "text", tags: "text" },
  {
    weights: {
      name: 10,         // name সবচেয়ে important
      brand: 5,         // brand মাঝারি
      tags: 3,
      description: 1
    },
    name: "product_text_search"
  }
)

// Text search with score
db.products.find(
  { $text: { $search: "apple iphone pro" } },
  { score: { $meta: "textScore" }, name: 1, price: 1 }
).sort({ score: { $meta: "textScore" } })

// ============================================
// Sparse Index — null values-এ index নেই
// ============================================
db.users.createIndex({ emailVerifyToken: 1 }, { sparse: true })

// ============================================
// TTL Index — auto-delete
// ============================================
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }  // 1 ঘণ্টা পর auto-delete
)

// ============================================
// Explain — query plan দেখো
// ============================================
db.products.find({ brand: "Apple", isActive: true }).explain("executionStats")
// COLLSCAN (full scan) → IXSCAN (index scan) হওয়া উচিত

// Indexes দেখো
db.products.getIndexes()
```

---

## 📐 Schema Design Patterns

### Embedding vs Referencing

```
╭─────────────────────────────────────────────────────────╮
│ 🔑 Concept: Embedding vs Referencing                    │
│ সহজ ভাষায়: Embedding = একটি document-এর ভেতরে         │
│            অন্য document রাখা (faster reads,           │
│            data duplication)                            │
│            Referencing = আলাদা collection-এ রাখা       │
│            (flexible, no duplication, joins লাগে)       │
╰─────────────────────────────────────────────────────────╯
```

```javascript
// ============================================
// EMBEDDING — Product with images & specs
// (images সবসময় product সাথে আসে)
// ============================================
{
  _id: ObjectId("..."),
  name: "iPhone 15 Pro",
  price: 999.99,

  // EMBEDDED — সবসময় দরকার, frequently accessed
  images: [
    { url: "https://...", isPrimary: true },
    { url: "https://...", isPrimary: false }
  ],

  // EMBEDDED — সবসময় দরকার
  specs: {
    color: "Black Titanium",
    storage: "256GB",
    ram: "8GB"
  },

  // EMBEDDED — অল্প data, সবসময় দরকার
  category: {
    _id: ObjectId("..."),
    name: "Phones",
    slug: "phones"
  }
}

// ============================================
// REFERENCING — Reviews
// (reviews আলাদা, অনেক হতে পারে, pagination দরকার)
// ============================================
// products collection:
{
  _id: ObjectId("PRODUCT_ID"),
  name: "iPhone 15 Pro",
  ratings: { average: 4.8, count: 1250 }
  // reviews এখানে নেই — আলাদা collection-এ আছে
}

// reviews collection:
{
  _id: ObjectId("..."),
  productId: ObjectId("PRODUCT_ID"),   // ← Reference
  userId: ObjectId("USER_ID"),         // ← Reference
  rating: 5,
  title: "Best phone ever!",
  comment: "Amazing performance...",
  isVerified: true,
  createdAt: new Date()
}

// ============================================
// HYBRID — Order with embedded items
// (order items সবসময় order সাথে আসে, immutable)
// ============================================
{
  _id: ObjectId("ORDER_ID"),
  orderNumber: "ORD-20260503-001234",
  userId: ObjectId("USER_ID"),       // ← Reference

  // EMBEDDED — snapshot at time of purchase
  items: [
    {
      productId: ObjectId("PRODUCT_ID"),
      sku: "APPL-IP15P-256-BLK",
      name: "iPhone 15 Pro",    // snapshot — price later change হলেও ok
      price: 999.99,
      quantity: 1,
      totalPrice: 999.99
    }
  ],

  // EMBEDDED — shipping address snapshot
  shippingAddress: {
    street: "123 Main St",
    city: "Dhaka",
    postalCode: "1200"
  },

  total: 1049.99,
  status: "delivered",
  createdAt: new Date()
}
```

### কোনটি কখন ব্যবহার করবো?

| পরিস্থিতি | পরামর্শ |
|----------|---------|
| Data সবসময় একসাথে access হয় | Embed করো |
| Data অনেক বড় হতে পারে (unbounded) | Reference করো |
| Data frequently update হয় | Reference করো |
| Read performance critical | Embed করো |
| One-to-few relationship | Embed করো |
| One-to-many (>100) | Reference করো |
| Many-to-many | Reference করো |

---

## 🏋️ Exercise: MongoDB E-commerce

**কাজ ১: Products collection তৈরি করো**

```javascript
// mongosh এ নিচের queries চালাও:

// 1. Categories create করো
db.categories.insertMany([
  { name: "Electronics", slug: "electronics", isActive: true },
  { name: "Phones", slug: "phones", parentSlug: "electronics", isActive: true },
  { name: "Laptops", slug: "laptops", parentSlug: "electronics", isActive: true }
]);

// 2. Products create করো (minimum 5টি)

// 3. Reviews create করো (minimum 10টি, বিভিন্ন products-এ)

// 4. নিচের queries লিখো:
//    a. Brand "Apple"-এর সব products, price ascending
//    b. Rating ৪-এর বেশি reviews count সহ products
//    c. প্রতিটি category-তে avg price
//    d. গত ৭ দিনে review করা products
//    e. Stock ১০-এর কম active products
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| Unbounded array embedding | Array অনেক বড় হয় | Reference করো বা pagination যোগ করো |
| Index ছাড়া বড় collection query | Full collection scan | Frequently queried fields-এ index দাও |
| ObjectId string হিসেবে compare | Type mismatch | `ObjectId("...")` wrap করো |
| $unset এর বদলে $set null | Field থেকে যায় | `$unset: { field: "" }` ব্যবহার করো |
| Schema validation ছাড়া insert | Invalid data | Mongoose validation বা $jsonSchema |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 7 — তুমি শিখলে                          ║
╠══════════════════════════════════════════════════════╣
║  • Document DB vs Relational DB — কখন কোনটা        ║
║  • BSON types ও MongoDB data model                  ║
║  • mongosh CRUD: insertOne/Many, find, update, del  ║
║  • Query operators: comparison/logical/array        ║
║  • Aggregation Pipeline: match/group/lookup/unwind  ║
║  • $facet দিয়ে multiple analytics একসাথে           ║
║  • Indexes: single/compound/text/TTL/sparse         ║
║  • Embedding vs Referencing — schema design         ║
║  • E-commerce MongoDB schema design                 ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 6](./chapter-06-prisma.md) | [➡ Chapter 8](./chapter-08-mongoose.md)
