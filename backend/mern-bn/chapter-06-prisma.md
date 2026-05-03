# 📘 CHAPTER 6 — Prisma ORM
### "Type-Safe Database Access — Schema-First Approach"
#### Progress: [███████░░░░░░░░░░░░] 35%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 5](./chapter-05-postgresql.md) | [➡ Ch 7](./chapter-07-mongodb.md)

---

## ORM কী এবং কেন দরকার?

Object-Relational Mapping (ORM) একটা concept যেটা programming language-এর object এবং relational database-এর table-এর মধ্যে সেতুবন্ধন তৈরি করে।

সমস্যাটা কোথায়? Programming language-এ আমরা object নিয়ে কাজ করি — `user.name`, `user.email`। কিন্তু relational database-এ data থাকে table-এ, row-এ, column-এ। এই দুটো paradigm-এর মধ্যে মিলানো কঠিন — এটাকে **Impedance Mismatch** বলে।

ORM ছাড়া প্রতিটা database operation-এ raw SQL লিখতে হয়। SQL লেখা error-prone — typo হলে runtime error, column name ভুল হলে runtime error। TypeScript ব্যবহার করলেও raw SQL string type-safe নয়।

Prisma এই সমস্যার আধুনিক সমাধান — type-safe, schema-first approach।

---

## Prisma vs Sequelize vs TypeORM

**Sequelize:** Node.js-এর সবচেয়ে পুরনো ORM। Model-first। JavaScript-এ ভালো, TypeScript support পরে যোগ হয়েছে। Callback-based API, promise support পরে। Extensive কিন্তু complex।

**TypeORM:** TypeScript-first। Decorator-based। Java-এর Hibernate-এর inspired। Active Record এবং Data Mapper pattern দুটোই support। TypeScript-এর সাথে ভালো — কিন্তু অনেক setup দরকার।

**Prisma:** সম্পূর্ণ নতুন approach। Schema-first — database schema একটা `.prisma` file-এ define করা হয়। Client auto-generate হয়, সম্পূর্ণ type-safe। Migration system sophisticated। VS Code extension দিয়ে autocomplete চমৎকার। Modern async/await API।

---

## Schema-First Approach

Prisma-এর মূল philosophy হলো schema-first। একটা `schema.prisma` file-এ data model define করা হয়, তারপর Prisma CLI থেকে database migration এবং type-safe client generate হয়।

`schema.prisma` file-এর তিনটা অংশ:

**Generator:** কী generate করবে — `prisma-client-js`।

**Datasource:** কোন database — PostgreSQL, MySQL, SQLite, MongoDB।

**Models:** Data model — table structure, relations, constraints।

এই একটা file থেকে Prisma দুটো জিনিস তৈরি করে: database migration (SQL DDL statements) এবং type-safe TypeScript client। Model পরিবর্তন করলে migration run করলে database schema update হয়, client regenerate করলে TypeScript types update হয়।

---

## Type-Safe Client

Prisma Client generate হওয়ার পরে প্রতিটা database operation সম্পূর্ণ type-safe। VS Code-এ autocomplete পাওয়া যায় — কোন model আছে, কোন field আছে, কোন operation available।

Typo হলে TypeScript compile time-এ ধরা পড়ে — runtime error নয়। `where` clause-এ valid field-ই দেওয়া যাবে, `include` দিয়ে কোন relation load করা যাবে সেটাও type-checked।

---

## Migration System

Database schema পরিবর্তন production-এ কীভাবে করবেন? Manual SQL লিখলে ভুল হতে পারে, কোন পরিবর্তন কখন হয়েছে track করা কঠিন।

Prisma-এর migration system:

`prisma migrate dev` — development-এ schema পরিবর্তন detect করে SQL migration file তৈরি করে এবং execute করে।

`prisma migrate deploy` — production-এ pending migration গুলো execute করে।

Migration file SQL-এ থাকে — version control-এ commit করা যায়, history দেখা যায়, rollback plan করা যায়।

---

## N+1 Problem এবং Prisma-র সমাধান

N+1 problem হলো backend performance-এর একটা classic সমস্যা।

ধরুন ১০টা blog post load করতে হবে এবং প্রতিটার author-এর নাম দেখাতে হবে। Naive approach:
1. প্রথমে ১০টা post fetch করা (1 query)।
2. প্রতিটা post-এর জন্য author fetch করা (10 queries)।

মোট ১১টা database query — এটাই N+1 problem। N টা related record-এর জন্য N+1 টা query।

**Prisma-এর `include` এবং `select`:**

Prisma-তে `include: { author: true }` দিলে Prisma একটা optimized query-তে posts এবং তাদের authors একসাথে fetch করে। SQL-এ `JOIN` বা সঠিক `IN` query ব্যবহার করে। N+1 problem automatically solve হয়।

`select` দিয়ে শুধু প্রয়োজনীয় field fetch করা যায় — over-fetching কমায়।

---

## Prisma-র Relation Handling

Prisma schema-তে relation explicit করে define করতে হয়। One-to-many, many-to-many, one-to-one সব ধরনের relation support।

Many-to-many relation-এ Prisma automatically implicit junction table তৈরি করে (explicit junction table-ও define করা যায় — extra field যোগ করতে)।

Nested write দিয়ে একটা operation-এ related records create করা যায়। Prisma এটা transaction-এ execute করে — atomicity নিশ্চিত।

---

## Prisma Middleware ও Soft Delete

Prisma Client-এ middleware যোগ করা যায় — প্রতিটা query-এর আগে বা পরে কোড চালানো। Soft delete implement করার জন্য — `DELETE` operation-কে `UPDATE { deletedAt: new Date() }` করে দেওয়া। Find query-তে automatically `WHERE deletedAt IS NULL` যোগ করা।

---

## মূল উপলব্ধি

Prisma একটা paradigm shift — ORM-কে নতুনভাবে ভাবার প্রচেষ্টা। Schema-first approach, type-safety, এবং migration system মিলে developer experience অনেক উন্নত করে। N+1 problem এবং over-fetching সচেতনভাবে এড়িয়ে চললে Prisma দিয়ে efficient এবং maintainable database layer তৈরি করা সম্ভব।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 5](./chapter-05-postgresql.md) | [➡ Ch 7](./chapter-07-mongodb.md)
