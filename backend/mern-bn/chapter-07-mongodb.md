# 📘 CHAPTER 7 — MongoDB
### "Document Database — Flexibility ও Scalability-র দর্শন"
#### Progress: [████████░░░░░░░░░░░] 40%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 6](./chapter-06-prisma.md) | [➡ Ch 8](./chapter-08-mongoose.md)

---

## Document Model Philosophy

Relational database data রাখে row-এ, column-এ — সমতল, structured। MongoDB data রাখে document-এ — JSON-like nested structure।

Real world-এ একটা blog post-এর সব তথ্য একসাথে থাকে: title, content, author, tags, comments। Relational database-এ এটা আলাদা আলাদা table-এ রাখতে হয়, query করতে JOIN দরকার। MongoDB-তে এই পুরো structure একটাই document-এ রাখা যায় — read করতে JOIN দরকার নেই।

এই philosophy-কে বলে **"locality of data"** — একসাথে access হবে এমন data একসাথে রাখো।

---

## BSON — কেন Plain JSON নয়?

MongoDB data store করে BSON (Binary JSON) format-এ। Plain JSON text-based, BSON binary। BSON-এর সুবিধা:

**Additional types:** JSON-এ Date নেই (string হিসেবে রাখতে হয়)। BSON-এ native Date type। Binary data (image) JSON-এ কঠিন, BSON-এ সহজ। ObjectId একটা BSON-specific type।

**Efficient traversal:** Binary format-এ field-এর length encode থাকে। নির্দিষ্ট field-এ যেতে string parse করতে হয় না।

**Size:** কিছু ক্ষেত্রে JSON-এর চেয়ে compact।

---

## CAP Theorem

CAP Theorem distributed system-এর একটা fundamental principle। তিনটা property-র মধ্যে যেকোনো দুটো নিশ্চিত করা যায়, তিনটা একসাথে নয়:

**Consistency (C):** সব node একই সময়ে একই data দেখে।

**Availability (A):** প্রতিটা request সবসময় response পায় (error ছাড়া)।

**Partition Tolerance (P):** Network partition হলেও system কাজ করে।

Distributed system-এ network partition অবশ্যম্ভাবী — তাই P সবসময় নিতে হয়। তাহলে choice হয় CA (consistency + availability) অথবা CP (consistency + partition tolerance) অথবা AP (availability + partition tolerance)।

MongoDB traditionally CP — network partition-এ availability sacrifice করে consistency রাখে। কিন্তু Read Concern এবং Write Concern configure করে behavior পরিবর্তন করা যায়।

---

## Eventual Consistency

MongoDB-তে replica set থাকলে write primary-তে হয়, secondary-তে replicate হয়। Replication asynchronous — write-এর পর কিছুটা সময় secondary-তে পুরনো data থাকতে পারে।

যদি secondary থেকে read করা হয়, সাময়িক পুরনো data পাওয়া যেতে পারে — কিন্তু eventually সব secondary primary-এর মতো হবে। এটাই **Eventual Consistency**।

Read Preference দিয়ে কোথা থেকে read করবে সেটা control করা যায়। `primary` — সবসময় latest data। `secondaryPreferred` — secondary থেকে read, secondary না থাকলে primary।

---

## Aggregation Pipeline

MongoDB-এর aggregation pipeline হলো data transformation-এর একটা শক্তিশালী tool। SQL-এর complex GROUP BY, JOIN, HAVING-এর equivalent।

Pipeline-এ একের পর এক stage থাকে। প্রতিটা stage আগের stage-এর output নেয়, নিজের কাজ করে, পরের stage-এ পাঠায়।

সাধারণ stages:

**`$match`:** Filter করা — SQL-এর WHERE।

**`$group`:** Group করা এবং aggregate — SQL-এর GROUP BY।

**`$sort`:** Sort করা।

**`$limit` / `$skip`:** Pagination।

**`$lookup`:** অন্য collection থেকে join — SQL-এর JOIN।

**`$project`:** Field select বা transform।

**`$unwind`:** Array field-কে আলাদা documents-এ ভাগ।

Aggregation pipeline data analysis, reporting, এবং complex transformation-এ অত্যন্ত শক্তিশালী।

---

## Index Types

MongoDB-তেও index দরকার — ছাড়া full collection scan।

**Single Field Index:** একটা field-এ।

**Compound Index:** একাধিক field-এ। Index field order গুরুত্বপূর্ণ — query pattern অনুযায়ী design করতে হয়।

**Multikey Index:** Array field-এ। Array-এর প্রতিটা element index হয়।

**Text Index:** Full-text search-এর জন্য। Tokenization, stemming সহ।

**Geospatial Index:** Geographic data — location-based query-র জন্য।

**TTL Index:** Time-to-live। নির্দিষ্ট সময় পর document automatically delete। Session, cache, temporary data-র জন্য।

---

## Sharding এবং Replication

**Replication:**

MongoDB Replica Set হলো একটা primary এবং একাধিক secondary-র group। Primary-তে write হয়, secondary-তে replicate। Primary fail করলে secondary স্বয়ংক্রিয়ভাবে নতুন primary হয় (election) — high availability।

**Sharding:**

এক server-এ data ধরে না — তখন horizontal scaling দরকার। Sharding মানে data বিভিন্ন server-এ ভাগ করা (shard)। Shard key নির্ধারণ করে কোন document কোন shard-এ যাবে। Mongos router client-এর request সঠিক shard-এ পাঠায়।

Shard key selection critical — ভুল key দিলে hotspot তৈরি হয় (সব data এক shard-এ)।

---

## কখন MongoDB, কখন PostgreSQL?

**MongoDB ভালো:**
- Flexible/evolving schema — startup, prototype।
- Hierarchical data যেখানে nested structure natural।
- High write throughput — logging, event data।
- Horizontal scaling দরকার।

**PostgreSQL ভালো:**
- Complex relationships এবং join দরকার।
- ACID transaction critical — financial, medical।
- Reporting এবং complex analytical query।
- Schema stable এবং well-defined।

অনেক application-এ দুটোই ব্যবহার হয় — primary data PostgreSQL-এ, session/cache Redis-এ, activity log MongoDB-তে।

---

## মূল উপলব্ধি

MongoDB relational database-এর replacement নয় — এটা ভিন্ন use case-এর জন্য ভিন্ন tool। Document model কখনো natural, কখনো problematic। CAP theorem বোঝলে distributed database-এর trade-off স্পষ্ট হয়। Aggregation pipeline শিখলে MongoDB দিয়ে complex analytics সম্ভব।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 6](./chapter-06-prisma.md) | [➡ Ch 8](./chapter-08-mongoose.md)
