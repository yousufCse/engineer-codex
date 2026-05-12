# 📘 CHAPTER 7 — MongoDB: সম্পূর্ণ গাইড
### "Basic থেকে Advanced — একটাই Resource"
#### Progress: [████████████████████] 100%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 6](./chapter-06-prisma.md) | [➡ Ch 8](./chapter-08-mongoose.md)

---

## 📋 সূচিপত্র

| অংশ | বিষয় |
|-----|-------|
| [Part 1](#part-1-foundation) | Foundation — MongoDB কী, কেন, Architecture |
| [Part 2](#part-2-crud-operations) | CRUD Operations |
| [Part 3](#part-3-query-language) | Query Language — Operators, Projection, Cursor |
| [Part 4](#part-4-update-operations) | Update Operations |
| [Part 5](#part-5-aggregation-pipeline) | Aggregation Pipeline |
| [Part 6](#part-6-data-modeling) | Data Modeling — Embedding, Referencing, Patterns |
| [Part 7](#part-7-indexes) | Indexes — Types, Strategy, ESR Rule |
| [Part 8](#part-8-transactions) | Transactions — ACID, Multi-Document |
| [Part 9](#part-9-replication) | Replication — Replica Set, Election |
| [Part 10](#part-10-sharding) | Sharding — Horizontal Scaling |
| [Part 11](#part-11-security) | Security — Auth, RBAC, Encryption |
| [Part 12](#part-12-performance--optimization) | Performance & Optimization |
| [Part 13](#part-13-advanced-features) | Advanced Features |
| [Part 14](#part-14-mongodb-atlas) | MongoDB Atlas |
| [Part 15](#part-15-cap--consistency-deep-dive) | CAP & Consistency Deep Dive |

---

# Part 1: Foundation

## MongoDB কী?

MongoDB হলো একটা **NoSQL document database**। Traditional relational database-এ data থাকে table-এ rows হিসেবে। MongoDB-তে data থাকে **collection**-এ **document** হিসেবে।

Document হলো JSON-like structure — key-value pair-এর একটা flexible object। নিচে দুটো পাশাপাশি তুলনা:

```
// Relational (SQL)               // MongoDB Document
TABLE: users                      Collection: users
+----+-------+-----+              {
| id | name  | age |                _id: ObjectId("..."),
+----+-------+-----+                name: "Rahim",
| 1  | Rahim | 25  |                age: 25,
+----+-------+-----+                address: {
                                      city: "Dhaka"
                                    }
                                  }
```

MongoDB-এর মূল দর্শন: **"Data যেভাবে ব্যবহার হয়, সেভাবে store করো"**।

---

## Document Model Philosophy

Real world object গুলো hierarchical। একটা Order-এর সাথে থাকে items (array), shipping address (embedded object), customer info। Relational database-এ এটা ভেঙে ৩-৪টা table-এ রাখতে হয়, JOIN করতে হয়।

MongoDB-তে পুরো Order একটাই document:

```json
{
  "_id": "ObjectId(...)",
  "customer": { "name": "Rahim", "email": "r@r.com" },
  "items": [
    { "product": "Laptop", "qty": 1, "price": 80000 }
  ],
  "total": 80000,
  "status": "delivered"
}
```

এই concept-কে বলে **"locality of data"** — যা একসাথে access হবে, একসাথে রাখো।

---

## MongoDB vs Relational — কোথায় কী ব্যবহার করব

```
┌─────────────────────────────────────────────────────────────┐
│                     Decision Tree                           │
│                                                             │
│  Complex JOIN দরকার?  ──Yes──▶  PostgreSQL                 │
│         │                                                   │
│         No                                                  │
│         │                                                   │
│  Schema কি rigid?  ──Yes──▶  PostgreSQL/MySQL              │
│         │                                                   │
│         No                                                  │
│         │                                                   │
│  ACID Transaction critical?  ──Yes──▶  PostgreSQL          │
│         │                                                   │
│         No                                                  │
│         │                                                   │
│  High write throughput / Flexible schema?                   │
│         │                                                   │
│         Yes──▶  MongoDB                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## MongoDB Architecture

```mermaid
graph TD
    A[Client Application] --> B[mongod / mongos]
    B --> C[Storage Engine - WiredTiger]
    C --> D[Data Files .wt]
    C --> E[Journal / WAL]
    B --> F[Memory - Buffer Pool]
    F --> C
```

**mongod** — MongoDB daemon process, actual database server।  
**mongos** — Sharded cluster-এ query router।  
**WiredTiger** — Default storage engine (version 3.2+)।  
**Journal (WAL)** — Write-Ahead Log — crash recovery নিশ্চিত করে।  
**Buffer Pool** — Hot data RAM-এ cache করে।

---

## BSON — কেন Plain JSON নয়?

MongoDB internally **BSON** (Binary JSON) ব্যবহার করে।

```
┌────────────────┬──────────────────────────────────────┐
│ JSON           │ BSON                                 │
├────────────────┼──────────────────────────────────────┤
│ Text-based     │ Binary — faster parse/traverse       │
│ No Date type   │ Native Date type                     │
│ No Binary      │ Binary data support                  │
│ No ObjectId    │ ObjectId (12-byte unique ID)         │
│ 64-bit float   │ Int32, Int64, Decimal128             │
│ No Regex type  │ Native Regex                         │
└────────────────┴──────────────────────────────────────┘
```

**ObjectId** structure (12 bytes):

```
┌──────────────┬────────────┬──────────────┐
│  4 bytes     │  5 bytes   │   3 bytes    │
│  Timestamp   │  Random    │  Increment   │
│  (seconds)   │  (process) │  Counter     │
└──────────────┴────────────┴──────────────┘
```

ObjectId timestamp extract করে creation time জানা যায়: `ObjectId("...").getTimestamp()`

---

## Installation ও Setup

**Option 1: Local Installation (macOS)**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

**Option 2: Docker (সবচেয়ে সহজ)**
```bash
docker run -d -p 27017:27017 --name mongo mongo:7
```

**Option 3: MongoDB Atlas (Cloud — recommended)**  
atlas.mongodb.com → Free tier (512 MB) → Connection string copy করো।

---

## mongosh — MongoDB Shell

mongosh হলো modern MongoDB CLI। Basic navigation:

```js
show dbs              // সব database list
use myapp             // database switch/create
show collections      // current db-র collections
db.stats()            // database statistics
```

---

## Key Terminology

```
┌─────────────────────────────────────────────┐
│  Relational     │  MongoDB                  │
├─────────────────┼───────────────────────────┤
│  Database       │  Database                 │
│  Table          │  Collection               │
│  Row            │  Document                 │
│  Column         │  Field                    │
│  Primary Key    │  _id                      │
│  JOIN           │  $lookup / Embedding      │
│  Index          │  Index                    │
│  View           │  View                     │
│  Stored Proc    │  Aggregation Pipeline     │
└─────────────────┴───────────────────────────┘
```

---

# Part 2: CRUD Operations

## Create — Document Insert

```js
// একটা document insert
db.users.insertOne({ name: "Rahim", age: 25, city: "Dhaka" })

// একাধিক document
db.users.insertMany([
  { name: "Karim", age: 30 },
  { name: "Salam", age: 22 }
])
```

**insertOne** সবসময় `{ acknowledged, insertedId }` return করে।  
**insertMany** `{ acknowledged, insertedIds }` return করে।

`_id` না দিলে MongoDB automatically ObjectId generate করে। নিজে দেওয়া যায়, যেকোনো unique value।

---

## Read — Document Query

```js
// সব document
db.users.find()

// condition দিয়ে
db.users.find({ city: "Dhaka" })

// একটাই document
db.users.findOne({ name: "Rahim" })
```

`find()` cursor return করে — lazy evaluation। Data আসে iterate করলে।

---

## Update — Document Modify

```js
// একটা update
db.users.updateOne(
  { name: "Rahim" },        // filter
  { $set: { age: 26 } }     // update
)

// সব matching update
db.users.updateMany(
  { city: "Dhaka" },
  { $set: { country: "BD" } }
)

// পুরো document replace
db.users.replaceOne(
  { name: "Rahim" },
  { name: "Rahim", age: 26, city: "Ctg" }  // _id বাদে সব replace
)
```

---

## Delete — Document Remove

```js
// একটা delete
db.users.deleteOne({ name: "Rahim" })

// সব matching delete
db.users.deleteMany({ city: "Dhaka" })

// সব document delete (collection থাকবে)
db.users.deleteMany({})
```

---

## findOneAndUpdate / findOneAndDelete

```js
// update করে পুরনো বা নতুন document return করে
db.users.findOneAndUpdate(
  { name: "Rahim" },
  { $inc: { age: 1 } },
  { returnDocument: "after" }  // "before" বা "after"
)
```

Atomic — find + update একই operation-এ। Race condition নেই।

---

## Upsert — Update or Insert

```js
db.users.updateOne(
  { email: "r@r.com" },
  { $set: { name: "Rahim", city: "Dhaka" } },
  { upsert: true }   // না পেলে insert করবে
)
```

`upsert: true` দিলে filter-এ কিছু না পেলে নতুন document create করে।

---

## Bulk Write

```js
db.users.bulkWrite([
  { insertOne: { document: { name: "A" } } },
  { updateOne: { filter: { name: "B" }, update: { $set: { age: 20 } } } },
  { deleteOne: { filter: { name: "C" } } }
])
```

Bulk write অনেক বেশি efficient — single network roundtrip।  
Default: **ordered** — কোনো error হলে পরেরগুলো stop। `ordered: false` দিলে সব চেষ্টা করবে।

---

# Part 3: Query Language

## Comparison Operators

```js
db.products.find({ price: { $gt: 100 } })          // price > 100
db.products.find({ price: { $gte: 100 } })         // price >= 100
db.products.find({ price: { $lt: 500 } })          // price < 500
db.products.find({ price: { $lte: 500 } })         // price <= 500
db.products.find({ price: { $eq: 200 } })          // price == 200
db.products.find({ price: { $ne: 200 } })          // price != 200
db.products.find({ status: { $in: ["A","B"] } })   // status in list
db.products.find({ status: { $nin: ["C"] } })      // status not in list
```

---

## Logical Operators

```js
// AND — সব condition satisfy করতে হবে
db.products.find({ $and: [{ price: { $gt: 100 } }, { stock: { $gt: 0 } }] })
// Shorthand AND (implicit)
db.products.find({ price: { $gt: 100 }, stock: { $gt: 0 } })

// OR — যেকোনো একটা condition
db.products.find({ $or: [{ price: { $lt: 50 } }, { sale: true }] })

// NOT
db.products.find({ price: { $not: { $gt: 500 } } })

// NOR — কোনোটাই না
db.products.find({ $nor: [{ status: "A" }, { status: "B" }] })
```

---

## Element Operators

```js
// field exist করে কিনা
db.users.find({ phone: { $exists: true } })
db.users.find({ phone: { $exists: false } })

// field-এর BSON type check
db.users.find({ age: { $type: "int" } })
db.users.find({ age: { $type: ["int", "double"] } })
```

---

## Evaluation Operators

```js
// Regex — pattern match
db.users.find({ name: { $regex: /^Rah/i } })

// $expr — aggregation expression query-তে ব্যবহার
db.orders.find({ $expr: { $gt: ["$total", "$discount"] } })

// $mod — modulo
db.products.find({ qty: { $mod: [4, 0] } })  // qty % 4 == 0
```

---

## Array Operators

```js
// $all — array-তে সব element থাকতে হবে
db.products.find({ tags: { $all: ["sale", "new"] } })

// $size — array-র exact length
db.products.find({ tags: { $size: 3 } })

// $elemMatch — array element-এ multiple condition
db.orders.find({
  items: { $elemMatch: { qty: { $gt: 2 }, price: { $lt: 100 } } }
})
```

`$elemMatch` ছাড়া array condition আলাদা elements-এ match হতে পারে।  
`$elemMatch` নিশ্চিত করে **একটাই** element সব condition satisfy করছে।

---

## Embedded Document Query (Dot Notation)

```js
// nested field
db.users.find({ "address.city": "Dhaka" })

// array of objects-এর nested field
db.orders.find({ "items.product": "Laptop" })

// deep nesting
db.users.find({ "profile.social.twitter": { $exists: true } })
```

---

## Projection — কোন Fields Return করবে

```js
// শুধু name এবং email (1 = include)
db.users.find({}, { name: 1, email: 1 })

// _id বাদে (0 = exclude)
db.users.find({}, { name: 1, email: 1, _id: 0 })

// কিছু field বাদ দাও
db.users.find({}, { password: 0, __v: 0 })
```

Include আর exclude একসাথে mix করা যায় না — শুধু `_id: 0` exception।

**$slice** — array-র কিছু element:
```js
db.posts.find({}, { comments: { $slice: 3 } })      // প্রথম ৩টা
db.posts.find({}, { comments: { $slice: -2 } })     // শেষ ২টা
db.posts.find({}, { comments: { $slice: [5, 3] } }) // 5 skip, 3 নাও
```

---

## Cursor Methods

```js
db.users.find().sort({ age: 1 })           // age ascending
db.users.find().sort({ age: -1 })          // age descending
db.users.find().sort({ age: -1, name: 1 }) // multi-field sort

db.users.find().limit(10)                  // সর্বোচ্চ ১০টা
db.users.find().skip(20).limit(10)         // page 3 (page size 10)
db.users.countDocuments({ city: "Dhaka" }) // exact count
db.users.estimatedDocumentCount()          // approximate, fast
```

**Pagination pattern:**
```js
const page = 2, pageSize = 10
db.users.find().skip((page - 1) * pageSize).limit(pageSize)
```

⚠️ বড় collection-এ `skip()` slow — বড় skip value-তে index ভালোভাবে কাজ করে না। Cursor-based pagination better।

---

# Part 4: Update Operations

## Field Update Operators

```js
$set          // field set বা add করো
$unset        // field remove করো:     { $unset: { field: "" } }
$inc          // numeric increment:    { $inc: { age: 1 } }
$mul          // multiply:             { $mul: { price: 1.1 } }
$rename       // field rename:         { $rename: { "old": "new" } }
$min          // current value-এর চেয়ে ছোট হলেই set
$max          // current value-এর চেয়ে বড় হলেই set
$currentDate  // current date set:     { $currentDate: { updatedAt: true } }
```

---

## Array Update Operators

```js
// array-তে element add
db.users.updateOne({ _id: id }, { $push: { tags: "vip" } })

// একাধিক element add + sort + slice
db.users.updateOne(
  { _id: id },
  { $push: { scores: { $each: [85, 90], $sort: -1, $slice: 5 } } }
)

// duplicate ছাড়া add (Set-এর মতো)
db.users.updateOne({ _id: id }, { $addToSet: { tags: "vip" } })

// element remove by value
db.users.updateOne({ _id: id }, { $pull: { tags: "vip" } })

// condition দিয়ে pull
db.users.updateOne({ _id: id }, { $pull: { scores: { $lt: 50 } } })

// $pop: 1 = last element, -1 = first element
db.users.updateOne({ _id: id }, { $pop: { tags: 1 } })
```

---

## Positional Operator — Array-র নির্দিষ্ট Element Update

```js
// $ — query-তে match হওয়া element update
db.orders.updateOne(
  { "items.product": "Laptop" },
  { $set: { "items.$.price": 75000 } }
)

// $[] — array-র সব element
db.students.updateOne(
  { _id: id },
  { $inc: { "grades.$[]": 10 } }
)

// $[identifier] — filtered positional
db.students.updateOne(
  { _id: id },
  { $set: { "grades.$[elem].score": 100 } },
  { arrayFilters: [{ "elem.subject": "Math" }] }
)
```

---

# Part 5: Aggregation Pipeline

Aggregation pipeline হলো data transformation-এর একটা sequence। প্রতিটা **stage** আগেরটার output নিয়ে কাজ করে।

```mermaid
graph LR
    A[Collection] --> B["$match\n(filter)"]
    B --> C["$group\n(aggregate)"]
    C --> D["$sort\n(order)"]
    D --> E["$project\n(shape)"]
    E --> F[Result]
```

```js
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customer", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } },
  { $limit: 5 }
])
```

---

## $match

SQL-এর WHERE-এর মতো। **যত আগে রাখবে, তত কম data process হবে।**

```js
{ $match: { status: "active", age: { $gte: 18 } } }
```

---

## $group

```js
{
  $group: {
    _id: "$category",              // group key
    totalSales: { $sum: "$price" },
    avgPrice:   { $avg: "$price" },
    maxPrice:   { $max: "$price" },
    minPrice:   { $min: "$price" },
    count:      { $sum: 1 },
    products:   { $push: "$name" }  // array বানাও
  }
}
```

`_id: null` দিলে সব document একসাথে group হবে।

---

## $project

Field shape করো — rename, compute, include/exclude।

```js
{
  $project: {
    fullName:         { $concat: ["$firstName", " ", "$lastName"] },
    year:             { $year: "$createdAt" },
    discountedPrice:  { $multiply: ["$price", 0.9] },
    password: 0   // exclude
  }
}
```

---

## $lookup — Join

```js
{
  $lookup: {
    from: "products",           // join করার collection
    localField: "productId",    // current collection-এর field
    foreignField: "_id",        // target collection-এর field
    as: "productDetails"        // result array field name
  }
}
```

`productDetails` একটা array — সাধারণত `$unwind` করে flatten করা হয়।

**Pipeline $lookup** (complex join):
```js
{
  $lookup: {
    from: "orders",
    let: { userId: "$_id" },
    pipeline: [
      { $match: { $expr: { $eq: ["$userId", "$$userId"] } } },
      { $match: { status: "completed" } }
    ],
    as: "completedOrders"
  }
}
```

---

## $unwind

Array field-কে আলাদা documents-এ ভাগ করে।

```
Before $unwind:                  After $unwind { path: "$tags" }:
{ name: "A", tags: [1,2,3] }  →  { name: "A", tags: 1 }
                                  { name: "A", tags: 2 }
                                  { name: "A", tags: 3 }
```

```js
{
  $unwind: {
    path: "$items",
    includeArrayIndex: "idx",
    preserveNullAndEmptyArrays: true
  }
}
```

---

## $addFields

নতুন field যোগ করো, existing field-ও override করা যায়।

```js
{
  $addFields: {
    totalWithTax:  { $multiply: ["$total", 1.15] },
    isExpensive:   { $gt: ["$price", 1000] }
  }
}
```

---

## $facet — Multiple Aggregations একসাথে

```js
{
  $facet: {
    "byCategory": [
      { $group: { _id: "$category", count: { $sum: 1 } } }
    ],
    "priceStats": [
      { $group: { _id: null, avg: { $avg: "$price" }, max: { $max: "$price" } } }
    ],
    "total": [
      { $count: "count" }
    ]
  }
}
```

একটাই query-তে বিভিন্ন aggregation — dashboard-এর জন্য perfect।

---

## $bucket ও $bucketAuto

Data-কে range-এ ভাগ করো।

```js
{
  $bucket: {
    groupBy: "$price",
    boundaries: [0, 100, 500, 1000, 5000],
    default: "Other",
    output: { count: { $sum: 1 }, avgPrice: { $avg: "$price" } }
  }
}
```

`$bucketAuto` — automatically n টা bucket তৈরি করে।

---

## $out ও $merge — Result Save করা

```js
// collection-এ write করো (replace করে)
{ $out: "monthly_report" }

// existing collection-এ merge (upsert)
{
  $merge: {
    into: "monthly_report",
    on: "_id",
    whenMatched: "merge",
    whenNotMatched: "insert"
  }
}
```

`$merge` দিয়ে Materialized View তৈরি করা যায় — cache হিসেবে।

---

## Accumulator Operators

```
$sum        — যোগ
$avg        — গড়
$min        — সর্বনিম্ন
$max        — সর্বোচ্চ
$count      — count (v5.0+)
$push       — array বানাও (duplicate সহ)
$addToSet   — array বানাও (unique only)
$first      — প্রথম element (sort করার পর)
$last       — শেষ element
$stdDevPop  — standard deviation (population)
$stdDevSamp — standard deviation (sample)
```

---

## Window Functions ($setWindowFields)

SQL-এর ROW_NUMBER(), RANK(), running total-এর equivalent। v5.0+।

```js
{
  $setWindowFields: {
    partitionBy: "$department",
    sortBy: { salary: -1 },
    output: {
      rank:         { $rank: {} },
      runningTotal: {
        $sum: "$salary",
        window: { documents: ["unbounded", "current"] }
      }
    }
  }
}
```

---

# Part 6: Data Modeling

## Embedding vs Referencing

```mermaid
graph TD
    A[Relationship?] --> B{Read বেশি নাকি Write?}
    B -->|একসাথে read| C[Embed করো]
    B -->|আলাদাভাবে access| D[Reference করো]
    C --> E{Data কতটা বাড়বে?}
    E -->|Bounded, ছোট| F[Embed ✅]
    E -->|Unbounded, বড়| G[Reference ✅]
```

**Embed করো যখন:**
- Data একসাথে read হবে সবসময়
- Child document independent অর্থ রাখে না
- Array size bounded (সর্বোচ্চ কয়েকশো)

**Reference করো যখন:**
- Data আলাদাভাবে access হবে
- Many-to-many relationship
- Array unbounded হতে পারে (comments, logs)
- Data share হয় — duplication wasteful

---

## One-to-One

```js
// Embed (একসাথে read হলে)
{ _id: 1, name: "Rahim", address: { city: "Dhaka", zip: "1207" } }

// Reference (address আলাদাভাবে access হলে)
{ _id: 1, name: "Rahim", addressId: ObjectId("...") }
```

---

## One-to-Many

```js
// Embed (few, bounded) — Blog post-এর tags
{ _id: 1, title: "Post", tags: ["tech", "web"] }

// Array of References — User-এর orders
{ _id: 1, name: "Rahim", orderIds: [ObjectId("a"), ObjectId("b")] }

// Parent Reference (অনেক child) — Comment-এ post reference
{ _id: 1, text: "Nice!", postId: ObjectId("..."), author: "Karim" }
```

16 MB document limit মনে রাখতে হবে — unbounded array embed করলে এই limit hit করতে পারে।

---

## Many-to-Many

```js
// Students ও Courses
{ _id: 1, name: "Rahim", courseIds: [ObjectId("c1"), ObjectId("c2")] }
{ _id: "c1", title: "MongoDB", studentIds: [ObjectId("1"), ObjectId("2")] }

// Junction collection (extra data থাকলে)
{ studentId: ObjectId("1"), courseId: ObjectId("c1"), enrolledAt: new Date(), grade: "A" }
```

---

## Schema Design Patterns

### 1. Bucket Pattern
Time series বা grouped data-র জন্য।

```js
// প্রতিটা bucket-এ ১ ঘণ্টার sensor data
{
  sensorId: "S1",
  hour: ISODate("2024-01-01T10:00:00Z"),
  readings: [23.1, 23.4, 23.2],  // max 60 readings
  count: 60, avg: 23.2, min: 22.9, max: 23.5
}
```

হাজারো individual documents-এর বদলে grouped bucket — কম documents, ভালো index performance।

---

### 2. Outlier Pattern
বেশিরভাগ document ছোট, কিছু outlier (যেমন celebrity-র followers)।

```js
// Normal user
{ _id: 1, name: "User", followerIds: [id1, id2] }

// Outlier — overflow flag
{ _id: 2, name: "Celebrity", followerIds: [...first_1000...], has_extras: true }
// Separate overflow documents
{ userId: 2, page: 2, followerIds: [...next_1000...] }
```

---

### 3. Computed Pattern
Frequently read হয় কিন্তু rarely update — computation pre-compute করে রাখো।

```js
// প্রতিটা product-এ average rating pre-computed
{ _id: 1, name: "Laptop", avgRating: 4.5, reviewCount: 230 }
// Review write হলে product document-ও atomic-এ update
```

Read ফাস্ট, write-এ একটু বেশি কাজ।

---

### 4. Attribute Pattern
Heterogeneous fields যেগুলোতে index দরকার।

```js
// Before — আলাদা আলাদা field (index nightmare)
{ color_en: "red", color_fr: "rouge", color_es: "rojo" }

// After — attribute array
{ attributes: [
  { k: "color_en", v: "red" },
  { k: "color_fr", v: "rouge" }
]}
// Index: { "attributes.k": 1, "attributes.v": 1 }
```

---

### 5. Subset Pattern
Document-এ সবচেয়ে access হওয়া data রাখো, বাকিটা আলাদা।

```js
// Product page-এ top 10 reviews দেখায়
{ _id: 1, name: "Laptop", topReviews: [...10 reviews...] }
// Full reviews আলাদা collection-এ
{ productId: 1, reviews: [...all reviews...] }
```

Working set ছোট রাখে — RAM-এ বেশি hot data fit করে।

---

### 6. Extended Reference Pattern
Frequently needed foreign data embed করো — JOIN কমাও।

```js
// Order-এ customer-এর কিছু info embed (denormalize)
{
  _id: 1,
  customer: { _id: ObjectId("..."), name: "Rahim", email: "r@r.com" },
  items: [...]
}
```

---

### 7. Tree Pattern

```js
// Parent Reference
{ _id: "electronics", parent: "root" }
{ _id: "laptops", parent: "electronics" }

// Array of Ancestors (Materialized Path — subtree query easy)
{ _id: "laptops", ancestors: ["root", "electronics"] }

// Nested Sets (subtree range query efficient)
{ _id: "laptops", left: 3, right: 8 }
```

---

## Anti-Patterns — যা করবে না

```
❌ Massive Arrays    — unbounded array embed করা
❌ Over-indexing     — প্রতিটা field-এ index (write slow হয়)
❌ Bloated Documents — সব data এক document-এ
❌ $where operator   — JavaScript execution: security + performance সমস্যা
❌ Unbounded growth  — document-এ append করতে থাকা
❌ Ignoring _id      — custom _id-তে shard key collision হতে পারে
```

---

# Part 7: Indexes

Index ছাড়া MongoDB প্রতিটা query-তে **COLLSCAN** (full collection scan) করে। Index দিলে **IXSCAN** — শুধু relevant entries।

```
Without Index:               With Index (B-Tree):
┌───────────────┐            ┌───────────────────────┐
│ Doc 1: age=25 │◄──check    │       B-Tree          │
│ Doc 2: age=30 │◄──check    │   age=22 → Doc3       │
│ Doc 3: age=22 │◄──check    │   age=25 → Doc1,Doc5  │
│ Doc 4: age=40 │◄──check    │   age=30 → Doc2       │
│ Doc 5: age=25 │◄──check    │   age=40 → Doc4       │
│  ...1M docs.. │◄──check    │                       │
└───────────────┘            │  Direct O(log n)!     │
O(n) scan                    └───────────────────────┘
```

---

## Index তৈরি করা

```js
// Single field
db.users.createIndex({ email: 1 })      // ascending
db.users.createIndex({ age: -1 })       // descending

// Unique
db.users.createIndex({ email: 1 }, { unique: true })

// Index list দেখো
db.users.getIndexes()

// Index drop করো
db.users.dropIndex("email_1")
```

---

## Compound Index

```js
db.users.createIndex({ city: 1, age: -1 })
```

**ESR Rule** — Compound index field order:
```
E → Equality first  (exact match fields)
S → Sort second
R → Range last

Example Query: { city: "Dhaka", age: { $gte: 20 } } sorted by name
Best Index:    { city: 1, name: 1, age: 1 }
               ↑Equality  ↑Sort    ↑Range
```

Compound index-এ **leftmost prefix** principle।  
Index `{a, b, c}` → `{a}`, `{a,b}`, `{a,b,c}` query-তে কাজ করবে। `{b}` বা `{c}` এককভাবে করবে না।

---

## Multikey Index

Array field-এ index। MongoDB automatically detect করে।

```js
db.products.createIndex({ tags: 1 })
// tags: ["sale", "new", "featured"] → তিনটা entry index-এ
```

Compound multikey index-এ maximum একটা array field থাকতে পারে।

---

## Text Index

Full-text search।

```js
db.articles.createIndex({ title: "text", content: "text" })

// Query
db.articles.find({ $text: { $search: "mongodb tutorial" } })

// Relevance score সহ sort
db.articles.find(
  { $text: { $search: "mongodb" } },
  { score: { $meta: "textScore" } }
).sort({ score: { $meta: "textScore" } })
```

Collection-এ একটাই text index থাকতে পারে। Language-specific stemming সাপোর্ট করে।

---

## Geospatial Index

```js
// 2dsphere — real world spherical geometry
db.places.createIndex({ location: "2dsphere" })

// Document format (GeoJSON)
{ name: "Dhaka", location: { type: "Point", coordinates: [90.4125, 23.8103] } }

// Nearby query
db.places.find({
  location: {
    $near: {
      $geometry: { type: "Point", coordinates: [90.4, 23.8] },
      $maxDistance: 5000  // meters
    }
  }
})
```

---

## TTL Index

Automatic document expiry।

```js
// createdAt থেকে ৩৬০০ seconds পরে delete
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 })
```

Background process প্রতি ৬০ seconds-এ expired documents delete করে। Exact timing guarantee নেই।

---

## Partial Index

Condition-এ match করা documents-এর জন্যই index।

```js
// শুধু active users-এর email index
db.users.createIndex(
  { email: 1 },
  { partialFilterExpression: { status: "active" } }
)
```

Index ছোট থাকে — faster, কম RAM।

---

## Sparse Index

`null` বা missing field যুক্ত documents বাদ দেয়।

```js
db.users.createIndex({ phone: 1 }, { sparse: true })
// phone field নেই এমন documents index-এ নেই
```

---

## Wildcard Index

Dynamic field name-এর জন্য।

```js
db.products.createIndex({ "attributes.$**": 1 })
// attributes-এর যেকোনো nested field index করবে
```

---

## Hashed Index

Sharding-এ hash-based distribution-এর জন্য।

```js
db.users.createIndex({ userId: "hashed" })
```

Equality query support করে। Range query support করে না।

---

## Covered Query

Query এবং projection শুধু index field — document-ই touch করে না। সবচেয়ে fast।

```js
// Index: { city: 1, name: 1 }
db.users.find({ city: "Dhaka" }, { name: 1, _id: 0 })
// শুধু index থেকে answer — IXSCAN, no FETCH
```

---

## explain() — Query Analysis

```js
db.users.find({ age: { $gt: 20 } }).explain("executionStats")
```

মূল metrics:
```
executionTimeMillis   — কত ms লাগলো
totalDocsExamined     — কত document scan হলো
totalKeysExamined     — কত index key scan হলো
winningPlan.stage     — IXSCAN ভালো, COLLSCAN খারাপ
nReturned             — কতটা return হলো
```

`totalDocsExamined == nReturned` — perfect। বেশি gap মানে index আরো ভালো করা দরকার।

---

# Part 8: Transactions

## Single Document Atomicity

MongoDB সবসময়ই single document-এ atomic। একটা document-এ embedded array update, multiple field change — সবই atomic। এজন্য document-এ embed করা প্রায়ই জটিলতা কমায়।

---

## Multi-Document Transactions

v4.0+ এ replica set-এ, v4.2+ এ sharded cluster-এ।

```js
const session = client.startSession()
session.startTransaction()

try {
  await accounts.updateOne({ _id: fromId }, { $inc: { balance: -amount } }, { session })
  await accounts.updateOne({ _id: toId },   { $inc: { balance: +amount } }, { session })
  await session.commitTransaction()
} catch (err) {
  await session.abortTransaction()
} finally {
  session.endSession()
}
```

Transaction-এ সব operation-এ `{ session }` pass করতে হবে।

---

## Read Concern

Transaction বা query-তে কোন data দেখবে তা নিয়ন্ত্রণ করে।

```
local       — নিজের node-এর latest data (default)। Rollback হতে পারে।
majority    — Majority-তে committed data। Durable।
snapshot    — Transaction শুরুর সময়ের consistent snapshot।
available   — Network partition-এ পুরনো data দিতে পারে।
linearizable— সবচেয়ে strict, single document, slow।
```

---

## Write Concern

Write কতটা acknowledged হলে success বলব।

```js
db.orders.insertOne(
  { item: "Laptop" },
  { writeConcern: { w: "majority", j: true, wtimeout: 5000 } }
)
```

```
w: 0          — acknowledge ছাড়াই (fire and forget)
w: 1          — primary acknowledge (default)
w: "majority" — majority node acknowledge
j: true       — journal-এ লেখার পর acknowledge (durability নিশ্চিত)
wtimeout      — max wait time (ms)
```

---

# Part 9: Replication

## Replica Set Architecture

```mermaid
graph TD
    Client -->|Write| P[Primary]
    P -->|Oplog Replication| S1[Secondary 1]
    P -->|Oplog Replication| S2[Secondary 2]
    Client -->|Read optional| S1
    Client -->|Read optional| S2
    S1 -.->|Election vote| P
    S2 -.->|Election vote| P
```

**Primary** — সব write নেয়।  
**Secondary** — Primary-র oplog replicate করে। Read serve করতে পারে।  
**Oplog** — Primary-র write operations-এর log। Secondary এটা follow করে।

---

## Election Process

Primary fail হলে:

```
1. Secondary-রা primary-কে ping করে — response নেই
2. electionTimeoutMillis (default 10s) পার হলে election start
3. Majority vote পেলে একটা secondary নতুন primary
4. সাধারণত কয়েক seconds-এর মধ্যে complete
```

**Odd number of members** রাখা ভালো — tie break avoid করতে।  
সর্বনিম্ন ৩টা (২ data node + ১ arbiter অথবা ৩ data node)।

**Arbiter** — Vote দেয় কিন্তু data রাখে না।

---

## Special Member Types

```
Priority 0  — Primary হবে না, কিন্তু vote দেবে, data রাখবে
Hidden      — Application থেকে invisible, backup/analytics-এর জন্য
Delayed     — X seconds পিছিয়ে — accidental data loss থেকে রক্ষা
Arbiter     — শুধু vote, data নেই (কম infrastructure cost)
```

---

## Read Preference

```js
MongoClient.connect(uri, { readPreference: "secondaryPreferred" })
```

```
primary            — সবসময় primary (default, latest data)
primaryPreferred   — primary, না থাকলে secondary
secondary          — সবসময় secondary (stale হতে পারে)
secondaryPreferred — secondary, না থাকলে primary
nearest            — network latency সবচেয়ে কম যেটা
```

---

# Part 10: Sharding

## কেন Sharding?

Single server-এ data ধরছে না বা write throughput বেশি — তখন horizontal scaling। Data বিভিন্ন server (shard)-এ ভাগ করা।

## Sharded Cluster Architecture

```mermaid
graph TD
    App[Application] --> MS[mongos Router]
    MS --> CS[Config Servers\nReplica Set]
    MS --> SH1[Shard 1\nReplica Set]
    MS --> SH2[Shard 2\nReplica Set]
    MS --> SH3[Shard 3\nReplica Set]
    CS -->|Metadata| MS
```

**mongos** — Query router। Client সরাসরি mongos-এর সাথে কথা বলে।  
**Config Servers** — Cluster metadata — কোন data কোন shard-এ।  
**Shard** — Actual data। প্রতিটা shard নিজেই একটা Replica Set।

---

## Shard Key

Shard key নির্ধারণ করে data কোন shard-এ যাবে। **Critical decision।**

```js
sh.shardCollection("myapp.orders", { customerId: 1 })   // range sharding
sh.shardCollection("myapp.logs",   { _id: "hashed" })   // hash sharding
```

**Good shard key:**
- High cardinality (অনেক unique value)
- Low frequency (single value-এ অনেক write নয়)
- Non-monotonic (যেমন incrementing timestamp-only খারাপ)
- Query pattern-এ frequently used

**Hotspot** — সব write এক shard-এ যাওয়া। Monotonic key এই সমস্যা করে।

---

## Range vs Hash Sharding

```
Range Sharding:                    Hash Sharding:
┌────────────────────────┐         ┌────────────────────────┐
│ Shard 1: key [A, M)    │         │ Shard 1: hash [0, 33%) │
│ Shard 2: key [M, Z)    │         │ Shard 2: hash [33,66%) │
│                         │         │ Shard 3: hash [66,100%)│
│ Range query efficient   │         │ Even distribution      │
│ Hotspot possible        │         │ Range query all shards │
└────────────────────────┘         └────────────────────────┘
```

---

## Zone Sharding

নির্দিষ্ট data নির্দিষ্ট shard-এ রাখো — data locality, compliance।

```js
sh.addShardToZone("shard1", "US")
sh.addShardToZone("shard2", "EU")
sh.updateZoneKeyRange("myapp.users", { region: "US" }, { region: "US" }, "US")
```

---

# Part 11: Security

## Authentication — SCRAM

Default authentication mechanism। Username/password।

```js
db.createUser({
  user: "appUser",
  pwd: "securePassword",
  roles: [{ role: "readWrite", db: "myapp" }]
})
```

Connection string: `mongodb://appUser:securePassword@localhost/myapp`

---

## x.509 Certificate Authentication

Client certificate দিয়ে authenticate। TLS-এর সাথে ব্যবহার। Production-এ recommended।

---

## RBAC — Role-Based Access Control

```
Built-in Roles:
┌─────────────────────────────────────────────┐
│ Database Level:                             │
│   read          — read only                 │
│   readWrite     — read + write              │
│   dbAdmin       — schema, index manage      │
│   userAdmin     — user manage               │
│   dbOwner       — all of above              │
│                                             │
│ Cluster Level:                              │
│   clusterAdmin  — cluster manage            │
│   clusterMonitor— monitoring only           │
│   backup        — backup operations         │
│   restore       — restore operations        │
│                                             │
│ Super:                                      │
│   root          — everything (avoid!)       │
└─────────────────────────────────────────────┘
```

---

## Custom Role

```js
db.createRole({
  role: "reportReader",
  privileges: [
    { resource: { db: "myapp", collection: "orders" },   actions: ["find"] },
    { resource: { db: "myapp", collection: "products" }, actions: ["find"] }
  ],
  roles: []
})
```

**Principle of Least Privilege** — শুধু দরকারি permission দাও।

---

## TLS/SSL

```bash
mongod --tlsMode requireTLS \
       --tlsCertificateKeyFile server.pem \
       --tlsCAFile ca.pem
```

Production-এ সবসময় TLS enable করো। Plain text connection কখনো নয়।

---

## Encryption at Rest

**WiredTiger Encryption** — Enterprise edition।  
**Atlas Encryption** — Customer-Managed Keys (AWS KMS, Azure Key Vault, GCP KMS)।

---

## Field Level Encryption (FLE)

Client-side encryption — server-ও plaintext দেখে না।

```js
// Schema-তে encrypted fields define করা হয়
// MongoDB Driver automatically encrypt/decrypt করে
// Database-এ শুধু encrypted bytes থাকে
```

PII data (SSN, credit card, medical) এর জন্য।

---

## Security Checklist

```
✅ Authentication enable করো (--auth flag)
✅ Default port (27017) change করো production-এ
✅ Firewall — শুধু trusted IP access
✅ TLS/SSL enable করো
✅ Least privilege roles ব্যবহার করো
✅ admin database-এ শুধু admin user
✅ MongoDB dedicated OS user-এ চালাও
✅ Audit logging enable করো
✅ Regular backup
✅ MongoDB version up to date রাখো
```

---

# Part 12: Performance & Optimization

## explain() Deep Dive

```js
// তিনটা verbosity level
db.collection.find({}).explain()                      // queryPlanner
db.collection.find({}).explain("executionStats")      // actual stats
db.collection.find({}).explain("allPlansExecution")   // all candidate plans
```

**Winning Plan stages:**

```
COLLSCAN    — Collection scan (large collection-এ bad)
IXSCAN      — Index scan (good)
FETCH       — Document fetch after index
SORT        — In-memory sort (index থাকলে এড়ানো যায়)
PROJECTION  — Field projection
LIMIT       — Limit applied
```

**Goal:** `IXSCAN` দেখতে চাই, `COLLSCAN` দেখলে index দাও।

---

## Index Hints

MongoDB wrong index choose করলে force করো:

```js
db.users.find({ age: { $gt: 20 }, city: "Dhaka" }).hint({ city: 1, age: 1 })
```

---

## Working Set

**Working Set** = frequently accessed data (hot data)। এটা RAM-এ fit করা উচিত।

```
RAM: 32 GB
Working Set আনুমানিক: < 28 GB (কিছুটা OS-এর জন্য রাখো)
Full dataset: 500 GB (disk-এ)
```

`db.stats()` এবং Atlas Metrics দিয়ে working set monitor করো।

---

## Connection Pooling

```js
MongoClient.connect(uri, {
  maxPoolSize: 100,       // max connections (default 100)
  minPoolSize: 10,        // min idle connections
  maxIdleTimeMS: 60000    // idle connection close হওয়ার সময়
})
```

প্রতিটা request-এ নতুন connection নয় — pool থেকে reuse।

---

## Optimization Tips

```
1. Index coverage — query-র সব field index-এ থাকুক
2. Projection    — দরকারি field-ই নাও
3. Limit         — সবসময় limit দাও
4. $match আগে   — aggregation-এ $match যত আগে তত ভালো
5. $lookup কমাও — embed করলে JOIN লাগে না
6. Bulk write    — single roundtrip-এ অনেক operation
7. Avoid $where  — JavaScript execution slow ও risky
8. TTL index     — auto cleanup, delete query দরকার নেই
9. Atlas Search  — full-text search-এ built-in text index-এর চেয়ে ভালো
10. Capped collection — fixed-size log, no manual cleanup
```

---

## Slow Query Log (Profiler)

```js
// 100ms এর বেশি লাগলে log করো
db.setProfilingLevel(1, { slowms: 100 })

// Profiler data দেখো
db.system.profile.find().sort({ millis: -1 }).limit(10)
```

---

## mongostat ও mongotop

```bash
mongostat --uri "mongodb://..." 1    # প্রতি 1s-এ cluster stats
mongotop  --uri "mongodb://..." 5    # collection-wise time
```

`mongostat` — operations/sec, connections, memory।  
`mongotop` — কোন collection-এ কত সময় ব্যয় হচ্ছে।

---

# Part 13: Advanced Features

## Change Streams

Collection, database, বা cluster-এ real-time changes subscribe করো।

```js
const changeStream = db.collection("orders").watch()

changeStream.on("change", (change) => {
  console.log(change.operationType)   // insert, update, delete, replace
  console.log(change.fullDocument)
  console.log(change.updateDescription.updatedFields)
})
```

Internally **oplog** ব্যবহার করে। Replica Set বা Sharded Cluster-এ কাজ করে।

**Resume Token** — disconnect হলে token দিয়ে resume:
```js
collection.watch([], { resumeAfter: lastResumeToken })
```

Use cases: Real-time dashboard, event-driven architecture, cache invalidation, audit trail।

---

## Time Series Collections

v5.0+ — Time series data-র জন্য optimized storage।

```js
db.createCollection("sensorData", {
  timeseries: {
    timeField: "timestamp",
    metaField: "sensorId",
    granularity: "seconds"   // seconds, minutes, hours
  },
  expireAfterSeconds: 86400 * 30  // 30 days TTL
})
```

Internally Bucket Pattern apply করে automatically। Normal collection-এর চেয়ে অনেক বেশি efficient for IoT/metrics data।

---

## Capped Collections

Fixed-size, circular buffer। পুরনো data automatically overwrite।

```js
db.createCollection("logs", {
  capped: true,
  size: 10485760,  // 10 MB (bytes)
  max: 10000       // max documents
})
```

Insert-only (delete/update limited)। High-speed logging-এর জন্য।

---

## Views

Virtual collection — aggregation pipeline-এর result।

```js
db.createView(
  "activeUsers",   // view name
  "users",         // source collection
  [{ $match: { status: "active" } }]
)

db.activeUsers.find({ city: "Dhaka" })  // normal collection-এর মতো query
```

View-এ write হয় না। Sensitive data hide করার উপায়।

---

## GridFS

16 MB-এর বড় file store করো।

```js
const bucket = new GridFSBucket(db)

// Upload
fs.createReadStream("video.mp4").pipe(bucket.openUploadStream("video.mp4"))

// Download
bucket.openDownloadStreamByName("video.mp4").pipe(res)
```

GridFS দুটো collection ব্যবহার করে: `fs.files` (metadata) ও `fs.chunks` (data, 255KB chunks)।

---

## Atlas Search (Full-Text)

Lucene-based full-text search।

```js
db.articles.aggregate([
  {
    $search: {
      index: "default",
      text: {
        query: "mongodb performance",
        path: ["title", "content"],
        fuzzy: { maxEdits: 1 }   // typo tolerance
      }
    }
  },
  { $limit: 10 },
  { $project: { title: 1, score: { $meta: "searchScore" } } }
])
```

Features: Fuzzy search, autocomplete, facets, highlight, synonyms, relevance scoring।

---

## Atlas Vector Search

Semantic/similarity search — AI/ML use cases।

```js
db.products.aggregate([
  {
    $vectorSearch: {
      index: "vector_index",
      path: "embedding",            // vector field
      queryVector: [0.1, 0.2, ...], // embedding of search query
      numCandidates: 100,
      limit: 10
    }
  }
])
```

Use cases: Semantic search, recommendation, RAG (Retrieval Augmented Generation)।

---

## On-Demand Materialized Views

`$merge` দিয়ে aggregation result একটা collection-এ save করো।

```js
// Run periodically (cron job)
db.orders.aggregate([
  { $group: { _id: "$month", total: { $sum: "$amount" } } },
  { $merge: {
      into: "monthly_summary",
      on: "_id",
      whenMatched: "replace",
      whenNotMatched: "insert"
  }}
])
```

---

# Part 14: MongoDB Atlas

## Atlas কী?

MongoDB-র managed cloud service। AWS, GCP, Azure-এ available। Infrastructure management-এর ঝামেলা নেই।

```mermaid
graph LR
    Dev[Developer] -->|Connection String| Atlas
    Atlas --> Cloud[AWS / GCP / Azure]
    Atlas --> Backup[Automated Backup]
    Atlas --> Monitor[Monitoring & Alerts]
    Atlas --> Search[Atlas Search / Vector]
    Atlas --> Trigger[Database Triggers]
```

---

## Cluster Tiers

```
M0      — Free (512 MB, shared) — development
M2/M5   — Shared (paid) — light workload
M10+    — Dedicated — production
M30+    — High throughput
M40+    — High memory
```

---

## Atlas CLI

```bash
brew install mongodb-atlas
atlas auth login
atlas clusters create myCluster --provider AWS --region US_EAST_1 --tier M10
atlas clusters connectionStrings describe myCluster
```

---

## Atlas Triggers

Event-driven serverless functions।

```js
// Database Trigger — document insert হলে চলে
exports = function(changeEvent) {
  const doc = changeEvent.fullDocument
  // Email পাঠাও, cache clear করো, event publish করো
}
```

Types: Database Trigger, Scheduled Trigger, Authentication Trigger।

---

## Atlas Backup

```
Continuous Backup  — Point-in-time restore (seconds granularity)
Cloud Backup       — Snapshots (hourly, daily, weekly, monthly)
Queryable Backup   — Backup-এ query করো — restore ছাড়াই
```

---

## Atlas Monitoring Metrics

```
Real-time:
- Operations/second (insert, update, delete, query)
- Query execution time (p50, p95, p99)
- Connection count
- Disk I/O, CPU, Memory utilization
- Replication lag

Alert thresholds (recommended):
- CPU > 80%
- Connections > 80% of max
- Replication lag > 60s
- Disk space < 20%
```

---

# Part 15: CAP & Consistency Deep Dive

## CAP Theorem

```
             C
           (Consistency)
              /\
             /  \
            / CP \
           /------\
          / CA  AP \
         /──────────\
        A            P
   (Availability) (Partition Tolerance)
```

**Consistency** — সব node একই সময়ে একই data দেখে।  
**Availability** — প্রতিটা request সবসময় response পায়।  
**Partition Tolerance** — Network partition হলেও system কাজ করে।

Network partition বাস্তব distributed system-এ অনিবার্য — তাই **P সবসময় নিতে হবে**।  
Real choice: **CP** (MongoDB default) বা **AP** (Cassandra, CouchDB)।

---

## MongoDB-র Consistency Model

MongoDB configurable:

```
Write Concern "majority" + Read Concern "majority"
→ Strongly Consistent (CP behavior)

Write Concern w:1 + Read Preference "secondary"
→ Eventual Consistency (more availability, possibly stale reads)
```

---

## Causal Consistency

একই session-এ "read your own writes" guarantee।

```js
const session = client.startSession({ causalConsistency: true })
// এই session-এ write করলে পরের read সেই write দেখবে
// even if reading from secondary
```

---

## Isolation Levels

```
Read Uncommitted  — Dirty read সম্ভব
Read Committed    — Default read concern "local"
Snapshot          — Transaction-এ consistent snapshot
Linearizable      — Strongest, single document, slow
```

---

## PACELC Model

CAP-এর extension — partition না হলেও Latency vs Consistency trade-off আছে।

```
PACELC:
  If Partition → (A or C)
  Else         → (L or C)
                  Latency or Consistency

MongoDB: PA/EC
  — Partition হলে Availability পছন্দ
  — নইলে Consistency পছন্দ (latency বেশি হলেও)
```

---

## Eventual Consistency

Write primary-তে হয়, secondary-তে asynchronously replicate। Secondary থেকে read করলে সাময়িক পুরনো data পাওয়া যেতে পারে। Eventually সব secondary primary-এর মতো হবে।

```
Time:     T1     T2     T3     T4
Primary:  W(5)   R(5)   R(5)   R(5)
Sec1:     R(4)   R(4)   R(5)   R(5)   ← replication lag
Sec2:     R(4)   R(5)   R(5)   R(5)   ← caught up faster
```

---

# Appendix: Quick Reference

## Shell Commands চিটশিট

```js
// Database
use mydb                     // switch/create
db.dropDatabase()
db.stats()

// Collection
db.createCollection("users")
db.users.drop()
db.users.stats()

// CRUD
db.c.insertOne({})
db.c.insertMany([])
db.c.find({}).pretty()
db.c.findOne({})
db.c.updateOne({filter}, {$set:{}})
db.c.updateMany({filter}, {update})
db.c.replaceOne({filter}, {newDoc})
db.c.deleteOne({})
db.c.deleteMany({})
db.c.countDocuments({})

// Index
db.c.createIndex({ field: 1 })
db.c.getIndexes()
db.c.dropIndex("name")
db.c.dropIndexes()

// Admin
db.adminCommand({ ping: 1 })
rs.status()     // replica set status
sh.status()     // shard status
```

---

## Update Operators চিটশিট

```
Field:
$set          field set/add
$unset        field remove
$inc          increment/decrement
$mul          multiply
$min          set if less than current
$max          set if greater than current
$rename       field rename
$currentDate  set current date

Array:
$push         array-তে add (duplicate সহ)
$addToSet     array-তে add (unique)
$pull         value দিয়ে remove
$pop          first/last remove
$each         multiple elements modifier
$sort         push সাথে sort modifier
$slice        push সাথে size limit

Positional:
$             matched element
$[]           all elements
$[identifier] filtered elements
```

---

## Aggregation Stages চিটশিট

```
Filtering:   $match, $limit, $skip, $sample
Grouping:    $group, $bucket, $bucketAuto
Shaping:     $project, $addFields, $unset, $replaceRoot, $replaceWith
Joining:     $lookup, $unwind
Sorting:     $sort
Writing:     $out, $merge
Counting:    $count
Window:      $setWindowFields
Time/Gap:    $densify, $fill
Search:      $search, $vectorSearch
```

---

## Mnemonic: MongoDB Core Concepts

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  D — Document Model (JSON-like, flexible)           │
│  I — Indexes (B-tree, Text, Geo, TTL, Wildcard)     │
│  A — Aggregation Pipeline (Transform & Analyze)     │
│  M — Modeling (Embed vs Reference, Patterns)        │
│  O — Ops (Replication + Sharding + Security)        │
│  N — No rigid schema (but design matters!)          │
│  D — Distributed (CAP, Consistency, Transactions)   │
│  B — Best fit for (Flexible, Hierarchical, Scale)   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## কোথায় যাবে এরপর

| Topic | Resource |
|-------|----------|
| Mongoose ODM | [Ch 8](./chapter-08-mongoose.md) — Schema, Validation, Middleware |
| Practice | MongoDB University (free courses) |
| Deep Dive | "MongoDB: The Definitive Guide" |
| Certification | MongoDB Associate Developer Exam |

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 6](./chapter-06-prisma.md) | [➡ Ch 8](./chapter-08-mongoose.md)
