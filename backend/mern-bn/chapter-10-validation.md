# 📘 CHAPTER 10 — Validation ও Input Handling
### "Boundary-তে রক্ষা — Defense in Depth"
#### Progress: [███████████░░░░░░░░] 55%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 9](./chapter-09-auth.md) | [➡ Ch 11](./chapter-11-security.md)

---

## কেন Validate করতে হবে?

"Never trust user input" — backend security-র মূল নীতি। Client-side (browser) validation শুধু UX-এর জন্য — security-র জন্য নয়। যে কেউ Postman বা curl দিয়ে সরাসরি API call করতে পারে, browser-এর validation bypass করতে পারে।

Server-side validation ছাড়া:
- Invalid data database-এ যাবে — data integrity নষ্ট।
- SQL Injection, XSS, Buffer Overflow সম্ভব।
- Application crash করতে পারে অপ্রত্যাশিত input-এ।

---

## Defense in Depth

Security-র একটা প্রধান principle হলো Defense in Depth — একাধিক স্তরে রক্ষা। শুধু একটা স্তর ভেঙে গেলে সব শেষ — এই পরিস্থিতি এড়ানো।

Validation-এর স্তর:
1. **Client-side:** দ্রুত feedback, bandwidth save। Security নয়।
2. **API Gateway/Load Balancer:** Rate limiting, basic request filtering।
3. **Application/Controller:** Business logic validation।
4. **Service/Domain:** Business rule enforcement।
5. **Database:** Constraints, data type enforcement।

প্রতিটা স্তর independent — একটা ব্যর্থ হলে পরেরটা রক্ষা করবে।

---

## Input Validation vs Data Sanitization

**Input Validation:** Input কি expected format, type, range-এ আছে? যদি না থাকে, reject করো। Binary decision — valid অথবা invalid।

**Data Sanitization:** Input-এ dangerous content থাকলে সেটা remove বা escape করা। User-এর HTML input-এ `<script>` tag থাকলে escape করা।

দুটো আলাদা কাজ — validation fail করলে reject, sanitization input নিয়ে safe করে।

---

## Whitelist vs Blacklist Approach

**Blacklist:** জানা dangerous input reject করা। "এই তালিকার বাইরে সব allow।"

সমস্যা: Attacker নতুন technique বের করলে blacklist-এ নেই — bypass সম্ভব। `<SCRIPT>`, `<ScRiPt>`, `&#x3C;script&#x3E;` সব এড়ানো কঠিন।

**Whitelist:** শুধু expected, known-good input allow। "এই তালিকায় থাকলেই allow।"

অনেক বেশি secure। Email validation-এ email regex check করা whitelist approach।

Validation-এ সবসময় whitelist approach prefer করতে হয়।

---

## কোথায় Validate করবেন?

**Client-side:** UX-এর জন্য। Immediate feedback — form submit-এর আগেই error দেখানো। Network request কমানো।

**Server-side:** Security-র জন্য। সবসময় করতে হবে। Client-side bypass করলেও server block করবে।

**Database-level:** Last line of defense। Constraint violation হলে error throw হয়।

উত্তর: তিন জায়গায়ই — প্রতিটার আলাদা উদ্দেশ্য।

---

## Schema Validation Philosophy

Schema validation মানে data structure-কে একটা schema-র বিপরীতে validate করা। Schema বলে দেয় কোন field আছে, কী type, কোনটা required, কী constraint।

**Joi:** Hapi.js দলের তৈরি। Expressive, powerful. Fluent API। String, number, date, array, object সব ধরনের complex validation।

**Zod:** TypeScript-first। Schema থেকে TypeScript type infer হয়। Type-safe validation।

**Yup:** React community-তে popular। Formik-এর সাথে ভালো কাজ করে।

Schema validation centralize করা ভালো — validation logic এক জায়গায়, controller-এ না ছড়িয়ে।

---

## Pagination, Filtering — Input Handling

Query parameter থেকে আসা `page`, `limit`, `sort`, `filter` validate করতে হবে।

**page এবং limit:** Integer হওয়া উচিত, positive। Maximum limit enforce করতে হবে — `limit=999999` দিলে database-এ কত load!

**sort field:** Whitelist approach — শুধু allowed field-এ sort করতে দেওয়া। Arbitrary field-এ sort performance issue করতে পারে।

**filter values:** Type check করতে হবে। String injection এড়াতে parameterized query বা ORM।

---

## Error Message Design — Security vs Usability

Validation error message দুটো পরস্পরবিরোধী চাহিদার মাঝে:

**Usability:** User-কে বলো ঠিক কোথায় কী ভুল — "Email format সঠিক নয়।" Developer-কে বলো কী ঠিক করতে হবে।

**Security:** Attacker-কে system information দেওয়া উচিত নয়। "User found but password incorrect" বললে attacker জানে username valid। বরং: "Invalid credentials।"

নিয়ম: Validation error (format, required) — specific message। Authentication error — generic message। Internal server error — generic message, log করো।

---

## মূল উপলব্ধি

Validation হলো application-এর boundary রক্ষা। Server-side validation কখনো optional নয় — এটা mandatory security measure। Whitelist approach, schema validation, এবং Defense in Depth মিলে robust validation layer তৈরি হয়। Error message security-র সাথে usability balance করতে হয়।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 9](./chapter-09-auth.md) | [➡ Ch 11](./chapter-11-security.md)
