# 📘 CHAPTER 11 — Security
### "OWASP Top 10 ও Backend Defense — Attack ও Counter-Attack"
#### Progress: [████████████░░░░░░░] 60%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 10](./chapter-10-validation.md) | [➡ Ch 12](./chapter-12-nestjs.md)

---

## OWASP Top 10

OWASP (Open Web Application Security Project) একটা non-profit organization যেটা web application security নিয়ে গবেষণা করে। OWASP Top 10 হলো সবচেয়ে critical web application security risk-এর তালিকা — প্রতি কয়েক বছরে update হয়।

Backend developer হিসেবে এই risks জানা এবং এড়ানো professional দায়িত্ব।

---

## SQL Injection — কীভাবে কাজ করে, কীভাবে ঠেকাবেন

SQL Injection হলো সবচেয়ে পুরনো এবং এখনো সবচেয়ে বিপজ্জনক vulnerability।

**আক্রমণ কীভাবে হয়:**

ধরুন login query: `SELECT * FROM users WHERE email = '${email}' AND password = '${password}'`

Attacker যদি email হিসেবে দেয়: `' OR '1'='1' --`

Query হবে: `SELECT * FROM users WHERE email = '' OR '1'='1' --' AND password = '...'`

`--` SQL comment। `'1'='1'` সবসময় true। ফলে সব user return হবে, password check হবে না।

**প্রতিরোধ — Parameterized Query:**

SQL এবং data আলাদা রাখতে হবে। Parameterized query বা prepared statement ব্যবহার করলে database driver data-কে code হিসেবে নয়, শুধু data হিসেবে treat করে।

ORM (Prisma, Mongoose) বা `pg` library-এর parameterized query — `WHERE email = $1` এবং আলাদা parameter। Injection impossible।

---

## XSS — Cross-Site Scripting

XSS attack-এ attacker website-এ malicious JavaScript inject করে। অন্য user-এর browser-এ সেই JavaScript চলে।

**Reflected XSS:** Malicious script URL-এর মধ্যে থাকে। User সেই link-এ click করলে script execute হয়।

**Stored XSS:** Malicious script database-এ সংরক্ষণ হয়। যে user page দেখে, সবার browser-এ script চলে। Comment, forum post-এ HTML না escape করলে।

**DOM-based XSS:** Server-এর সাথে সম্পর্ক নেই। JavaScript code DOM থেকে input পড়ে সেটা directly execute করে।

**প্রতিরোধ:**
- User input database-এ যাওয়ার আগে sanitize করো — HTML escape।
- Content-Security-Policy header — browser-কে বলো কোন source থেকে script run করতে পারবে।
- `httpOnly` cookie — JavaScript দিয়ে cookie access করা যাবে না।

---

## CSRF — Cross-Site Request Forgery

CSRF attack-এ attacker user-কে দিয়ে তার অজান্তে action করায়।

**কীভাবে হয়:**

User bank.com-এ logged in। Attacker evil.com-এ একটা form রাখে যেটা bank.com-এ POST request পাঠায় (money transfer)। User evil.com visit করলে form automatically submit হয়। User-এর browser bank.com-এর cookie সাথে পাঠায়। Bank মনে করে legitimate request।

**প্রতিরোধ:**

**SameSite Cookie:** `SameSite=Strict` — cookie শুধু same site থেকে request-এ পাঠানো হবে। Cross-site request-এ cookie যাবে না।

**CSRF Token:** Server একটা random token generate করে, form-এ hidden field হিসেবে দেয়। Submit করলে server verify করে। Attacker এই token জানে না।

**Custom Header:** API-তে custom header (যেমন `X-Requested-With`) — browser-এর cross-site form submit এটা পাঠাতে পারে না।

---

## Rate Limiting — Abuse প্রতিরোধ

Rate limiting মানে নির্দিষ্ট সময়ে নির্দিষ্ট IP/user থেকে কতটা request allow করবে তার সীমা।

কেন দরকার:
- Brute force attack রোধ — প্রতি সেকেন্ডে অনেক login try।
- DoS (Denial of Service) protection।
- API abuse রোধ — unlimited scraping।

**Token Bucket Algorithm:**

প্রতিটা user-এর একটা "bucket" আছে। Bucket-এ token থাকে। Request করলে একটা token consume হয়। নির্দিষ্ট rate-এ token refill হয়। Bucket খালি হলে request reject।

**Sliding Window:**

শেষ N সেকেন্ডে কতটা request হয়েছে track করা। Fixed window-এর চেয়ে smooth।

`express-rate-limit` package Express-এ সহজে implement করা যায়।

---

## CORS — Same-Origin Policy

Same-Origin Policy browser-এর একটা security feature। একটা domain-এর JavaScript অন্য domain-এর resource access করতে পারে না — by default।

CORS (Cross-Origin Resource Sharing) হলো server-এর একটা mechanism যেটা বলে "এই domain থেকে request করা allowed।"

Backend API যদি `api.example.com`-এ থাকে এবং frontend `app.example.com`-এ, CORS configure না করলে browser request block করবে।

**CORS Headers:**

`Access-Control-Allow-Origin: https://app.example.com` — এই origin allow।

`Access-Control-Allow-Methods: GET, POST, PUT, DELETE` — এই methods allow।

`Access-Control-Allow-Headers: Authorization, Content-Type` — এই headers allow।

Wildcard `*` avoid করা উচিত — production-এ explicit origin list করো।

**Preflight Request:**

Complex request (non-simple headers বা methods) এর আগে browser OPTIONS request পাঠায় — "এই request করা কি allowed?" Server allow করলে actual request যায়।

---

## Helmet — HTTP Security Headers

Helmet.js Express-এর জন্য একটা middleware যেটা বিভিন্ন security-related HTTP header set করে।

**X-Content-Type-Options: nosniff** — Browser content type sniffing বন্ধ। Browser HTML file-কে script হিসেবে execute করবে না।

**X-Frame-Options: DENY** — Page কে iframe-এ load করা যাবে না। Clickjacking attack রোধ।

**Strict-Transport-Security (HSTS)** — Browser-কে বলে সবসময় HTTPS ব্যবহার করো।

**X-XSS-Protection** — Browser-এর built-in XSS filter enable।

**Content-Security-Policy** — কোন source থেকে script, style, image load হতে পারবে।

**Referrer-Policy** — Referrer header-এ কতটুকু information পাঠানো হবে।

---

## Environment Secrets Management

API key, database password, JWT secret — এগুলো code-এ hardcode করা যাবে না।

**কেন নয়:**
- Code repository (GitHub) public হলে secrets ফাঁস।
- Developer যোগ দিলে বা চলে গেলে access control কঠিন।
- Production এবং development-এ আলাদা secrets দরকার।

**Best practices:**
- `.env` file-এ local secrets — `.gitignore`-এ।
- Production-এ environment variable (cloud provider-এর secret manager)।
- AWS Secrets Manager, HashiCorp Vault, Doppler।
- Rotate secrets regularly।
- Least privilege — service শুধু যা দরকার তাই access পাবে।

---

## মূল উপলব্ধি

Security কোনো feature নয় — এটা fundamental requirement। SQL Injection, XSS, CSRF — এগুলো decades-পুরনো attack কিন্তু এখনো widespread। OWASP Top 10 জানা, parameterized query ব্যবহার, Helmet header, rate limiting, CORS সঠিকভাবে configure — এগুলো minimum hygiene। Security একটা ongoing process — নতুন vulnerability বের হয়, আপডেট রাখতে হয়।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 10](./chapter-10-validation.md) | [➡ Ch 12](./chapter-12-nestjs.md)
