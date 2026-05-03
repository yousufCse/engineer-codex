# 📘 CHAPTER 5 — PostgreSQL
### "Relational Database-এর তত্ত্ব এবং অভ্যন্তরীণ কার্যপদ্ধতি"
#### Progress: [██████░░░░░░░░░░░░░] 30%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 4](./chapter-04-expressjs.md) | [➡ Ch 6](./chapter-06-prisma.md)

---

## Relational Model-এর জন্ম

1970 সালে IBM-এর গবেষক E.F. Codd একটা paper প্রকাশ করেন: "A Relational Model of Data for Large Shared Data Banks"। এই paper আধুনিক database-এর ভিত্তি তৈরি করে।

Codd-এর মূল প্রস্তাব ছিল — data গণিতের set theory-এর নিয়ম মেনে সংরক্ষণ করতে হবে। Table হলো একটা relation — mathematical set। Row হলো একটা tuple। Column হলো attribute। এই model-এ data কীভাবে physically সংরক্ষণ হচ্ছে সেটা না জেনেও logical query করা যাবে।

PostgreSQL এই relational model-এর সবচেয়ে সমৃদ্ধ open-source implementation।

---

## Tables, Rows, Columns — Set Theory

একটা database table হলো একটা relation — অর্থাৎ একটা set of tuples। Set theory-তে একটা set-এ কোনো duplicate element নেই — তাই table-এ প্রতিটা row unique হওয়া উচিত (Primary Key দিয়ে ensure করা হয়)।

**Schema:** Table-এর structure definition — column names, data types, constraints।

**Data Types:** PostgreSQL-এ `INTEGER`, `BIGINT`, `TEXT`, `VARCHAR`, `BOOLEAN`, `TIMESTAMP`, `JSONB`, `UUID`, `DECIMAL` সহ আরো অনেক। সঠিক data type ব্যবহার করা performance এবং data integrity-র জন্য গুরুত্বপূর্ণ।

**Constraints:** Data-এর নিয়ম — `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`, `PRIMARY KEY`, `FOREIGN KEY`। Database level-এ constraint থাকলে invalid data কখনো সংরক্ষণ হতে পারে না।

---

## ACID — Database-এর নির্ভরযোগ্যতার ভিত্তি

ACID হলো database transaction-এর চারটা গুরুত্বপূর্ণ property। এগুলো নিশ্চিত করে যে bank transfer, e-commerce order, বা যেকোনো critical operation সঠিকভাবে হবে।

**Atomicity (অবিভাজ্যতা):**

একটা transaction হলো অনেক operation-এর একটা logical unit। Bank transfer-এ দুটো operation: source account থেকে টাকা বাদ, destination account-এ যোগ। যদি প্রথম operation সফল হয় কিন্তু দ্বিতীয়টা fail করে, টাকা হারিয়ে যাবে। Atomicity নিশ্চিত করে — হয় সব operation সফল হবে (commit), অথবা কোনো change থাকবে না (rollback)।

**Consistency (সামঞ্জস্যতা):**

Transaction শুরু হওয়ার আগে database valid state-এ আছে। Transaction শেষ হওয়ার পরেও valid state-এ থাকবে। কোনো constraint বা rule ভাঙলে transaction commit হবে না।

**Isolation (বিচ্ছিন্নতা):**

একাধিক transaction একই সময়ে চললে একটা transaction অন্যটার intermediate state দেখতে পাবে না। প্রতিটা transaction যেন একাই চলছে।

**Durability (স্থায়িত্ব):**

Commit হওয়ার পর data পাকাপাকিভাবে সংরক্ষিত। Server crash হলেও committed transaction হারাবে না। PostgreSQL Write-Ahead Log (WAL) দিয়ে এটা নিশ্চিত করে।

---

## SQL vs NoSQL — Trade-offs

SQL database (PostgreSQL, MySQL) relational model follow করে — structured data, ACID transaction, complex join query। NoSQL (MongoDB, Redis, Cassandra) বিভিন্ন data model ব্যবহার করে — document, key-value, graph।

SQL-এর সুবিধা: Data integrity, complex relationship query, ACID, mature ecosystem।
SQL-এর অসুবিধা: Schema rigid, horizontal scaling কঠিন, hierarchical data-তে join heavy।

NoSQL-এর সুবিধা: Flexible schema, horizontal scaling সহজ, specific use case-এ performance।
NoSQL-এর অসুবিধা: ACID সীমিত (পরিস্থিতি ভেদে), complex relationship কঠিন।

বেশিরভাগ real application-এ SQL database-ই সঠিক choice — ACID আর data integrity অমূল্য।

---

## Primary Key ও Foreign Key

**Primary Key:** প্রতিটা row-কে uniquely identify করার column বা column combination। `NULL` হতে পারে না, duplicate হতে পারে না। সাধারণত `SERIAL` (auto-increment integer) বা `UUID` ব্যবহার হয়।

UUID সুবিধা: Globally unique — distributed system-এ conflict নেই। অসুবিধা: Index size বড়, random insertion B-tree fragmentation করে।

**Foreign Key ও Referential Integrity:**

Foreign Key হলো এক table-এর column যেটা অন্য table-এর Primary Key refer করে। `ON DELETE CASCADE` — parent delete হলে child automatically delete। `ON DELETE RESTRICT` — child থাকলে parent delete করা যাবে না। `ON DELETE SET NULL` — parent delete হলে child-এর foreign key `NULL`।

Referential Integrity নিশ্চিত করে কোনো orphan record নেই — অর্থাৎ কোনো order নেই যার user নেই।

---

## Normalization — Data Redundancy কমানো

Normalization হলো database design-এর process যেটা data redundancy কমায় এবং integrity বাড়ায়।

**First Normal Form (1NF):** প্রতিটা cell একটাই value (atomic)। Repeating group নেই।

**Second Normal Form (2NF):** 1NF + non-key column সম্পূর্ণ primary key-এর উপর dependent (composite key থাকলে)।

**Third Normal Form (3NF):** 2NF + non-key column শুধু primary key-এর উপর dependent, অন্য non-key column-এর উপর নয় (transitive dependency নেই)।

Over-normalization (5NF, 6NF) করলে query-তে অনেক join দরকার হয় — performance কমে। Practical application-এ 3NF পর্যন্ত যথেষ্ট। কখনো কখনো performance-এর জন্য ইচ্ছাকৃতভাবে denormalize করা হয়।

---

## Index — Query Speed-এর চাবিকাঠি

Index ছাড়া একটা table-এর কোনো row খুঁজতে হলে সব row scan করতে হবে — Full Table Scan। ১০ লাখ row-এ ১০ লাখ comparison।

Index হলো একটা separate data structure যেটা নির্দিষ্ট column-এর value এবং সেই row-এর physical location সংরক্ষণ করে। Index দিয়ে search করলে সব row না দেখে সরাসরি সঠিক row-এ পৌঁছানো যায়।

**B-Tree Index (default):**

PostgreSQL-এর default index type। B-Tree (Balanced Tree) একটা self-balancing tree structure যেখানে প্রতিটা node-এ অনেক key এবং pointer থাকে। Search, Insert, Delete সব `O(log n)` সময়ে। `=`, `<`, `>`, `BETWEEN`, `LIKE 'prefix%'` query-তে কাজ করে।

**Index-এর মূল্য:**

Index read query দ্রুত করে কিন্তু write (INSERT, UPDATE, DELETE) ধীর করে — কারণ data পরিবর্তন হলে index-ও update করতে হয়। Write-heavy table-এ অপ্রয়োজনীয় index না রাখাই ভালো।

**Index Selectivity:**

যে column-এ index করা হচ্ছে সেটার unique values কতটা বেশি তাই selectivity। `gender` column-এ (শুধু 'M'/'F') index ineffective — half the table scan করতে হবে। `email` column-এ (প্রতিটা unique) index highly effective।

---

## Query Planner ও EXPLAIN ANALYZE

PostgreSQL-এর query planner বা query optimizer প্রতিটা SQL statement-এর জন্য সবচেয়ে efficient execution plan তৈরি করে। এটা বিভিন্ন plan তৈরি করে, তাদের cost estimate করে, সবচেয়ে কম cost-এর plan execute করে।

`EXPLAIN ANALYZE query` — query execution plan দেখায় এবং actual runtime measure করে। এটা দিয়ে কেন query ধীর সেটা বোঝা যায়। Seq Scan (full table scan) দেখলে index দরকার হতে পারে।

---

## Transaction Isolation Levels

একাধিক transaction concurrent-এ চললে বিভিন্ন সমস্যা হতে পারে:

**Dirty Read:** একটা transaction অন্য uncommitted transaction-এর data দেখে — সেই transaction rollback করলে ভুল data পড়া হয়েছে।

**Non-Repeatable Read:** Same transaction-এ একই row দুইবার পড়া — মাঝে অন্য transaction update করলে ভিন্ন result।

**Phantom Read:** Same query দুইবার চালালে মাঝে অন্য transaction insert/delete করলে ভিন্ন set of rows।

PostgreSQL-এ চারটা isolation level:

**Read Uncommitted:** PostgreSQL-এ এটা Read Committed হিসেবে কাজ করে।
**Read Committed (default):** Committed data-ই দেখা যায়। Dirty read নেই।
**Repeatable Read:** Transaction শুরুর snapshot দেখে। Non-repeatable read নেই।
**Serializable:** সর্বোচ্চ isolation। যেন transactions serially চলছে।

Higher isolation = more consistency + lower concurrency/performance।

---

## Connection Pooling

Database connection establish করা expensive — TCP handshake, authentication, SSL — প্রতিটা query-তে নতুন connection করলে অনেক time এবং resource নষ্ট হবে।

Connection Pool হলো pre-established connection-এর একটা pool। Query করতে হলে pool থেকে একটা connection নাও, কাজ শেষে return করো। নতুন connection establish করার overhead নেই।

`pg` library-তে `Pool` class, Prisma-তে connection pool built-in। Production-এ connection pool size database-এর max connection limit এবং application-এর load অনুযায়ী configure করতে হয়।

---

## মূল উপলব্ধি

PostgreSQL শুধু একটা database নয় — এটা relational algebra, set theory, এবং decades-এর engineering-এর ফসল। ACID, normalization, এবং index বোঝলে data modeling সঠিক হয় এবং performance issues সহজে debug করা যায়। অনেক backend performance problem-এর মূলে থাকে missing index বা poorly designed schema।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 4](./chapter-04-expressjs.md) | [➡ Ch 6](./chapter-06-prisma.md)
