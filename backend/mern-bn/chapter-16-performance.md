# 📘 CHAPTER 16 — Performance Optimization
### "N+1 থেকে Caching — Backend Performance-এর বিজ্ঞান"
#### Progress: [█████████████████░░] 85%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 15](./chapter-15-testing.md) | [➡ Ch 17](./chapter-17-deployment.md)

---

## Performance-এর মূল সত্য

"Premature optimization is the root of all evil" — Donald Knuth।

আগে measure করো, তারপর optimize। কোথায় সময় যাচ্ছে না জেনে optimize করা সময় নষ্ট এবং কখনো কখনো ক্ষতিকর।

**Profiling:** Application কোথায় সময় ব্যয় করছে সেটা measure করা। Database query slow? HTTP call slow? CPU-heavy operation? জানার আগে optimization অনুমান।

---

## N+1 Problem — Database Performance-এর শত্রু

N+1 problem backend-এ সবচেয়ে সাধারণ performance issue।

**উদাহরণ:** ১০টা blog post দেখাতে হবে, প্রতিটার author-এর নাম সহ।

Naive implementation:
1. `SELECT * FROM posts LIMIT 10` — 1 query।
2. প্রতিটা post-এর জন্য `SELECT * FROM users WHERE id = ?` — 10 queries।

মোট 11 queries। ১০০ post হলে 101 queries। এটাই N+1।

**সমাধান — Eager Loading:**

SQL JOIN দিয়ে একটা query-তে posts এবং users একসাথে। অথবা `IN` clause: `SELECT * FROM users WHERE id IN (1,2,3,4,5,6,7,8,9,10)` — একটা query।

Prisma-এ `include`, Mongoose-এ `populate` এই optimization করে।

**ORMless N+1 detect করা:**

Query logging enable করো। একটা request-এ কতটা query হচ্ছে দেখো। Unexpected অনেক query N+1-এর লক্ষণ।

---

## Database Query Optimization

**Index ব্যবহার করো:**

WHERE clause-এ ব্যবহৃত column-এ index। Foreign key-তে index (JOIN fast হয়)। Sort column-এ index।

**SELECT * এড়াও:**

শুধু প্রয়োজনীয় column। Over-fetching memory এবং network bandwidth নষ্ট করে।

**EXPLAIN ANALYZE:**

PostgreSQL-এ `EXPLAIN ANALYZE query` দিয়ে query plan দেখো। Seq Scan (full table scan) দেখলে index বিবেচনা করো। High cost node-এ focus।

**Pagination:**

Offset-এর বদলে cursor-based pagination large dataset-এ দ্রুত।

---

## Caching — দ্বিতীয়বার একই কাজ না করা

Cache হলো frequently accessed data-র copy দ্রুত accessible জায়গায় রাখা।

Phil Karlton বলেছিলেন: "There are only two hard things in Computer Science: cache invalidation and naming things."

**Cache-Aside (Lazy Loading):**

Application পড়তে গিয়ে প্রথমে cache দেখে। Cache-এ নেই (cache miss) তো database থেকে পড়ে cache-এ রাখে। পরের request cache থেকে পায় (cache hit)।

সুবিধা: Cache শুধু actually requested data রাখে।
অসুবিধা: প্রথম request slow (cold start)।

**Write-Through:**

Database-এ লেখার সময় একই সাথে cache update। Cache এবং database সবসময় sync।

সুবিধা: Cache সবসময় fresh।
অসুবিধা: Write slow। Cache-এ unnecessary data।

**Write-Behind (Write-Back):**

Cache-এ লেখো, পরে asynchronously database update। Fast write।

ঝুঁকি: Cache fail হলে data হারানো।

---

## Cache Invalidation — কঠিন সমস্যা

Data update হলে cache stale (পুরনো) হয়। User data দেখে updated কিন্তু cache-এ পুরনো।

**TTL (Time-to-Live):**

Cache entry নির্দিষ্ট সময় পর expire হয়। Simple কিন্তু stale window থাকে।

**Event-based Invalidation:**

Data update হলে cache entry delete করো। Exact — কিন্তু জটিল।

**Cache Busting:**

Cache key-তে version বা hash যোগ করো। Content পরিবর্তন হলে নতুন key, পুরনো অটো stale।

---

## Redis — Data Structures ও Use Cases

Redis in-memory data store। অত্যন্ত fast (microsecond latency)।

**String:** Simple key-value। Session storage, counter।

**Hash:** Object store। User profile — individual field update।

**List:** Queue, stack। Job queue, activity feed।

**Set:** Unique elements। Unique visitors, tags।

**Sorted Set:** Score সহ unique elements। Leaderboard, rate limiting sliding window।

**Expiry:** প্রতিটা key-এ TTL set করা যায়। Auto-expire।

**Redis use cases:**

- Session store।
- Cache।
- Rate limiting।
- Job queue (Bull)।
- Pub/Sub।
- Distributed lock।

---

## Connection Pooling — কেন দরকার?

Database connection establish করা expensive — TCP handshake, authentication, SSL। প্রতিটা request-এ নতুন connection করলে:
- Latency বাড়ে।
- Database max connection পৌঁছে যায়।

Connection Pool হলো pre-established connection-এর pool। Request করতে pool থেকে connection নাও, শেষে return করো।

Pool size: Too small — requests queue হয়। Too large — database overwhelmed।

Database-এর max connection, application server count, এবং query duration — এই তিনটা দিয়ে optimal pool size calculate করা হয়।

---

## Horizontal vs Vertical Scaling

**Vertical Scaling (Scale Up):**

Server-এর hardware upgrade — বেশি CPU, RAM। Simple কিন্তু single point of failure। Hardware limit আছে। Expensive।

**Horizontal Scaling (Scale Out):**

আরো server যোগ করা — Load Balancer traffic distribute করে। Fault tolerant। Theoretically unlimited। Application stateless হতে হবে (session memory-তে রাখলে কাজ করে না — Redis-এ রাখতে হবে)।

**Node.js Cluster Mode:**

Node.js single-threaded — একটা CPU core ব্যবহার করে। Cluster mode দিয়ে সব CPU core ব্যবহার। PM2 cluster mode automatically করে।

---

## মূল উপলব্ধি

Performance optimization-এ measure first, optimize later। N+1 problem database-এ সবচেয়ে সাধারণ issue — eager loading দিয়ে সমাধান। Caching dramatic performance improvement দেয় কিন্তু invalidation জটিল। Redis একটা versatile tool — শুধু cache নয়, অনেক কাজে। Horizontal scaling-এর জন্য application stateless হওয়া আবশ্যক।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 15](./chapter-15-testing.md) | [➡ Ch 17](./chapter-17-deployment.md)
