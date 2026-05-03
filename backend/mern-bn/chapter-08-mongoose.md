# 📘 CHAPTER 8 — Mongoose
### "ODM — Schema আর MongoDB-এর মধ্যে সেতু"
#### Progress: [█████████░░░░░░░░░░] 45%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 7](./chapter-07-mongodb.md) | [➡ Ch 9](./chapter-09-auth.md)

---

## ODM vs ORM

ORM (Object-Relational Mapper) relational database-এর table-কে object-এ map করে। ODM (Object-Document Mapper) document database-এর document-কে object-এ map করে।

MongoDB schema-less — যেকোনো structure-এর document রাখা যায়। কিন্তু real application-এ structured data দরকার। Mongoose MongoDB-তে schema enforced করার সুযোগ দেয় — application level-এ।

এটা নিয়ে debate আছে: MongoDB-এর flexibility কি Mongoose দিয়ে কমানো উচিত? উত্তর context-dependent। Team বড় হলে, codebase complex হলে, schema validation critical হলে Mongoose অমূল্য।

---

## Schema Definition

Mongoose-এ Schema হলো document-এর structure এবং rules-এর blueprint। Schema define করে কোন fields থাকবে, কী type হবে, কোনটা required, default value কী।

Schema types: `String`, `Number`, `Date`, `Boolean`, `ObjectId`, `Array`, `Map`, `Mixed`।

`Mixed` type দিলে সেই field-এ যেকোনো structure রাখা যায় — কিন্তু validation হারিয়ে যায়।

Schema options: `timestamps: true` দিলে Mongoose automatically `createdAt` এবং `updatedAt` field যোগ করে। `versionKey: false` দিলে `__v` field বাদ।

---

## Validation Layer

Mongoose validation আসলে একটা middleware। Document save করার আগে schema-এর rules অনুযায়ী validate করে। Validation fail করলে `ValidationError` throw হয়।

Built-in validators: `required`, `minlength`, `maxlength`, `min`, `max`, `enum`, `match` (regex)।

Custom validator: একটা function যেটা `true` (valid) বা `false` (invalid) return করে।

Validation MongoDB-তে পৌঁছানোর আগে application level-এ হয়। MongoDB-রও schema validation আছে (`$jsonSchema`) কিন্তু Mongoose-এর validation বেশি flexible।

---

## Middleware (Hooks)

Mongoose-এর middleware বা hooks হলো lifecycle hooks — নির্দিষ্ট operation-এর আগে (pre) বা পরে (post) custom code চালানো।

**Pre hooks:**

`pre('save')` — document save-এর আগে। Password hash করার ideal জায়গা — password পরিবর্তন হলে hash করো, না হলে skip।

`pre('find')`, `pre('findOne')` — query-এর আগে। Soft delete implement করার জন্য — automatically `deletedAt: null` filter যোগ।

**Post hooks:**

`post('save')` — save-এর পরে। Notification trigger, audit log।

**এই architecture-এর সুবিধা:** Business logic model-এর সাথে থাকে — controller-এ না। Password hash করার logic প্রতিটা controller-এ লিখতে হয় না।

---

## Virtuals — Computed Fields

Virtual field database-এ সংরক্ষণ হয় না — runtime-এ compute করা হয়।

`firstName` এবং `lastName` আলাদা আলাদা সংরক্ষণ থাকলে `fullName` virtual হতে পারে। Database-এ extra space নষ্ট হয় না, কিন্তু `user.fullName` কাজ করে।

Populate virtual — একটা model-এর document আরেকটা model-এ কতটা reference করছে সেটা virtual দিয়ে track করা।

JSON-এ virtual include করতে `toJSON: { virtuals: true }` schema option।

---

## Population vs Aggregation `$lookup`

MongoDB document-এ অন্য collection-এর ObjectId reference রাখা হয় — এটা relational database-এর foreign key-এর analog।

**Mongoose `populate()`:**

Reference resolve করে actual document দিয়ে replace করে। Application level-এ হয় — Mongoose আলাদা query করে related document fetch করে। Simple এবং readable — কিন্তু N+1 problem হতে পারে।

**MongoDB `$lookup` (aggregation):**

Database level-এ join। একটা query-তে data আসে। Complex join এবং transformation-এ efficient। কিন্তু query লেখা কঠিন।

Simple use case-এ `populate()`, performance-critical বা complex join-এ `$lookup`।

---

## Query Building

Mongoose query builder চেইন করা যায়:
`.find().where().select().sort().limit().skip()` — প্রতিটা method query object return করে। `.exec()` বা `await` করলে actual query execute হয়।

Lean query: `.lean()` — plain JavaScript object return করে, Mongoose document নয়। Mongoose document-এ methods, virtuals, change tracking থাকে। Lean faster — read-only use case-এ, API response-এ।

---

## মূল উপলব্ধি

Mongoose MongoDB-এর flexibility-র উপরে structure এবং predictability যোগ করে। Validation এবং hooks দিয়ে business logic model-এর কাছে রাখা যায় — DRY (Don't Repeat Yourself) principle মানা সহজ হয়। Population-এর N+1 সমস্যা সম্পর্কে সচেতন থাকলে এবং lean query ব্যবহার করলে performance ভালো থাকে।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 7](./chapter-07-mongodb.md) | [➡ Ch 9](./chapter-09-auth.md)
