# 📘 CHAPTER 9 — Authentication ও Authorization
### "পরিচয় নিশ্চিতকরণ এবং অনুমতি — JWT থেকে OAuth পর্যন্ত"
#### Progress: [██████████░░░░░░░░░] 50%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 8](./chapter-08-mongoose.md) | [➡ Ch 10](./chapter-10-validation.md)

---

## Authentication vs Authorization

এই দুটো concept প্রায়ই গুলিয়ে ফেলা হয় — কিন্তু এগুলো আলাদা।

**Authentication (প্রমাণীকরণ):** "তুমি কে?" — ব্যবহারকারীর পরিচয় নিশ্চিত করা। Username/password দিয়ে login করা authentication।

**Authorization (অনুমোদন):** "তুমি কী করতে পারো?" — authenticated ব্যবহারকারীর কী access আছে সেটা নির্ধারণ। Admin সব কিছু করতে পারে, regular user শুধু নিজের data দেখতে পারে।

Authentication সবসময় Authorization-এর আগে আসে — পরিচয় না জানলে অনুমতি দেওয়া অসম্ভব।

---

## Session-based vs Token-based Authentication

**Session-based Authentication (Traditional):**

User login করলে server একটা session তৈরি করে এবং session ID browser-এর cookie-তে পাঠায়। পরের প্রতিটা request-এ browser সেই cookie পাঠায়, server session store-এ (memory বা database) session খোঁজে এবং user identify করে।

সমস্যা: Server stateful — প্রতিটা session server-এ সংরক্ষণ। Multiple server থাকলে session sharing দরকার (Redis)। Horizontal scaling জটিল।

**Token-based Authentication (Modern):**

User login করলে server একটা token তৈরি করে এবং client-এ পাঠায়। Client পরের প্রতিটা request-এ token পাঠায় (`Authorization: Bearer <token>` header)। Server token verify করে user identify করে — database lookup ছাড়া।

সুবিধা: Server stateless। Multiple server-এ token verify করা যায় কারণ server-এ কিছু সংরক্ষণ নেই। Mobile app, third-party API-তে ভালো।

---

## JWT — JSON Web Token

JWT হলো token-based authentication-এর সবচেয়ে জনপ্রিয় standard।

একটা JWT তিনটা অংশ দিয়ে গঠিত — dot দিয়ে আলাদা:

**Header:** Algorithm এবং token type। Base64URL encoded।
```
{ "alg": "HS256", "typ": "JWT" }
```

**Payload:** Claims — user information এবং token metadata। Base64URL encoded।
```
{ "sub": "user123", "name": "Alice", "iat": 1700000000, "exp": 1700003600 }
```

**Signature:** Header এবং Payload-এর উপর secret key দিয়ে cryptographic signature।

**JWT কীভাবে কাজ করে:**

Server token তৈরির সময় header + payload + secret দিয়ে signature তৈরি করে। Client token পাঠালে server শুধু signature verify করে — secret জানলে যেকোনো server verify করতে পারে, database lookup লাগে না।

**জরুরি সতর্কতা:** Payload Base64URL encoded — encrypted নয়। যে কেউ payload decode করে content দেখতে পারে। Sensitive information (password, credit card) payload-এ রাখা উচিত নয়।

---

## JWT Signing Algorithms

**HS256 (HMAC-SHA256):** Symmetric। একটাই secret key — sign করতে এবং verify করতে। Simple কিন্তু secret সব service-এ share করতে হয়।

**RS256 (RSA-SHA256):** Asymmetric। Private key দিয়ে sign, public key দিয়ে verify। Auth service private key রাখে। অন্য service public key দিয়ে verify করতে পারে — private key share করতে হয় না। Microservice architecture-এ preferred।

---

## Access Token + Refresh Token Pattern

JWT-এর একটা সমস্যা — token revoke করা কঠিন। Token valid থাকাকালীন user কোনো কারণে block করলেও token দিয়ে access পাবে।

এই সমস্যার সমাধান: Short-lived access token + Long-lived refresh token।

**Access Token:** Short expiry (15 minutes - 1 hour)। API call-এ এটাই পাঠানো হয়। Expire হলে নতুন token দরকার।

**Refresh Token:** Long expiry (7-30 days)। Database-এ সংরক্ষণ। নতুন access token নিতে ব্যবহার।

**Flow:**
1. Login করলে access token + refresh token পাওয়া যায়।
2. API call-এ access token পাঠানো হয়।
3. Access token expire হলে refresh token দিয়ে নতুন access token নেওয়া হয়।
4. Logout করলে refresh token database থেকে delete করা হয় — এরপর আর নতুন access token নেওয়া যাবে না।

**Token Rotation:** প্রতিবার refresh করলে নতুন refresh token দেওয়া এবং পুরনোটা invalidate করা — refresh token চুরি হলেও সীমিত ক্ষতি।

---

## bcrypt — Password Hashing

Password কখনো plain text-এ সংরক্ষণ করা উচিত নয়। Database leak হলে সব ব্যবহারকারীর password ফাঁস।

Hash করলেও SHA-256 বা MD5 যথেষ্ট নয় — এগুলো দ্রুত। Attacker GPU দিয়ে প্রতি সেকেন্ডে বিলিয়ন hash calculate করতে পারে।

**bcrypt কেন ভালো:**

**Slow by design:** bcrypt ইচ্ছাকৃতভাবে ধীর — brute force attack কঠিন। Cost factor দিয়ে speed control করা যায়।

**Salt:** Random string যেটা password-এর সাথে যোগ করে hash করা হয়। এর ফলে একই password-এর আলাদা hash হয়। Rainbow table attack (pre-computed hash lookup) defeat করে।

**Cost Factor:** Work factor বা rounds। bcrypt লগারিদমিক — cost 10 মানে 2^10 = 1024 rounds। Cost 11 মানে 2^11 = 2048। প্রতি unit বাড়ালে computation দ্বিগুণ। Hardware দ্রুত হলে cost বাড়ানো যায়।

Production-এ cost 10-12 সাধারণত ভালো balance।

---

## OAuth 2.0 Overview

OAuth 2.0 হলো third-party authorization protocol। "Google দিয়ে login" বা "Facebook দিয়ে login" OAuth দিয়ে হয়।

Core idea: User তাদের password third-party app-কে না দিয়ে Google/Facebook-এ login করে এবং সীমিত permission grant করে।

**চারটা Roles:**
- Resource Owner: User।
- Client: আমাদের application।
- Authorization Server: Google, GitHub — token issue করে।
- Resource Server: Google API, GitHub API — protected resource।

**Authorization Code Flow:** Most secure। User Authorization Server-এ redirect, login করে permission দেয়। Authorization Code পাওয়া যায়। Code দিয়ে Access Token নেওয়া হয় (server-to-server, client-এ code না)।

---

## Common Auth Vulnerabilities

**Brute Force Attack:** অনেক password try করা। Rate limiting এবং account lockout দিয়ে defend।

**Credential Stuffing:** অন্য site-এর leaked username/password দিয়ে try। Strong hashing এবং MFA।

**JWT Algorithm Confusion:** `alg: none` attack — verify না করে token accept। Library-তে expected algorithm explicit করতে হবে।

**Token Leakage:** HTTPS ব্যবহার না করলে token intercepted। সবসময় HTTPS।

---

## মূল উপলব্ধি

Authentication এবং Authorization backend security-র ভিত্তি। JWT-এর payload public — sensitive data রাখা যাবে না। Short-lived access token + refresh token pattern হলো production-standard। bcrypt-এর cost factor hardware-এর সাথে তাল মিলিয়ে adjust করতে হবে। OAuth দিয়ে "social login" implement করা আধুনিক UX-এর অংশ।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 8](./chapter-08-mongoose.md) | [➡ Ch 10](./chapter-10-validation.md)
