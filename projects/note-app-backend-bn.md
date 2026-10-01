# 📝 Note App Backend — শূন্য থেকে Production

> **Flutter ডেভেলপারের জন্য লেখা Node.js + Express + PostgreSQL কোর্স।**
> থিওরি নয় — একটা আসল Note Taking App এর backend, ২২টা ধাপে।
> এক ধাপ = এক মাইলস্টোন। নতুন concept আসে ঠিক তখনই, যখন সেটা ছাড়া পরের লাইন লেখা যায় না।

---

## 🙋 এই কোর্স কার জন্য

তুমি Flutter দিয়ে অ্যাপ বানাও। তুমি জানো —

- ✅ API call করতে হয় কীভাবে
- ✅ JSON response parse করতে হয় কীভাবে
- ✅ JWT token কোথায় জমা রাখতে হয়

তুমি জানো না —

- ❌ ওই API-টা আসলে **কোথায় চলে**
- ❌ `POST /login` এ hit করলে **ভিতরে কী ঘটে**
- ❌ Token টা **কে বানায়, কীভাবে বানায়, কে যাচাই করে**
- ❌ Password ডেটাবেজে **কী অবস্থায় পড়ে থাকে**

এই কোর্স ঠিক ওই না-জানা অংশটার জন্য।

---

## 🚫 যা থাকবে না · ✅ যা থাকবে

| থাকবে না | থাকবে |
|---|---|
| "Node.js এর ইতিহাস" জাতীয় অধ্যায় | কোড আগে, ব্যাখ্যা সাথে সাথে |
| ৫ লেসন theory তারপর কোড | এক lesson = এক কাজ করা ফিচার |
| "পরে বুঝবে" বলে এড়িয়ে যাওয়া | প্রতিটা লাইনের ব্যাখ্যা + **মুছলে কী হবে** |
| একসাথে ২০টা নতুন শব্দ | শব্দ আসবে প্রয়োজনের মুহূর্তে |

প্রতিটা lesson এ ৮টা অংশ থাকবে:

```
1. 🎯 Goal              — এই ধাপে কী দাঁড়াবে
2. 💻 Code              — পুরো কোড
3. 🔍 লাইন-বাই-লাইন    — প্রতিটা লাইন + মুছলে কী ভাঙবে
4. 🔄 Internal Flow     — request কোন পথে যায় (ASCII)
5. 🗄️ PostgreSQL        — DB এর ভিতরে কী ঘটে (প্রযোজ্য হলে)
6. 🧪 Postman Testing   — কী পাঠাবে, কী ফিরবে
7. ⚠️ Common Mistakes   — সবাই যে ভুলগুলো করে
8. 🏋️ Practice          — নিজে ভাবার প্রশ্ন
```

---

## 🧭 Flutter ↔ Node.js অনুবাদ টেবিল

| Flutter / Dart | Node.js | এক জিনিস? |
|---|---|---|
| Dart SDK | Node.js | ✅ কোড চালায় |
| `pub get` | `npm install` | ✅ package নামায় |
| `pubspec.yaml` | `package.json` | ✅ dependency তালিকা |
| `pubspec.lock` | `package-lock.json` | ✅ version লক করে |
| `.dart_tool/` | `node_modules/` | ✅ নামানো কোড |
| `void main()` | `server.js` | ✅ শুরুর বিন্দু |
| `flutter run` | `node server.js` | ✅ চালু করা |
| Hot reload | `nodemon` | ⚠️ কাছাকাছি (এটা full restart) |
| `pub.dev` | `npmjs.com` | ✅ package ভাণ্ডার |
| `http.get()` | `app.get()` | ❌ **উল্টো!** |

শেষ লাইনটাই সবচেয়ে বড় mindset পরিবর্তন —

```
Flutter এ তুমি:  "আমাকে ডেটা দাও"      → চাওয়ার পক্ষ  (client)
Node এ তুমি:     "কে কী চায়? শুনছি।"   → দেওয়ার পক্ষ  (server)
```

Flutter app বন্ধ হলে কিছু যায় আসে না। **Server বন্ধ হলে পুরো অ্যাপ মরে যায়** — তাই server কোড লেখার সময় "এটা কি ২৪ ঘণ্টা টিকবে?" প্রশ্নটা সবসময় মাথায় রাখতে হয়।

---

<a id="toc" name="toc"></a>

## 📚 সূচিপত্র

### পর্ব ১ — ভিত্তি
| # | Lesson | নতুন যা শিখবে |
|---|---|---|
| 01 | [Project তৈরি](#lesson-01) | Node runtime, npm, `package.json`, `.gitignore` |
| 02 | [Dependencies ইনস্টল](#lesson-02) | dependency vs devDependency, `node_modules`, version range |
| 03 | [Express Server](#lesson-03) | server কী, port, `require`, `app.listen()`, event loop |
| 04 | [প্রথম API](#lesson-04) | route, `req`/`res`, HTTP method, status code, JSON |

### পর্ব ২ — Database
| # | Lesson | নতুন যা শিখবে |
|---|---|---|
| 05 | [PostgreSQL Connect](#lesson-05) | `pg`, Connection Pool, `.env`, Promise, `async/await` |
| 06 | [users টেবিল](#lesson-06) | `CREATE TABLE`, `SERIAL`, `UNIQUE`, index, migration |

### পর্ব ৩ — Authentication
| # | Lesson | নতুন যা শিখবে |
|---|---|---|
| 07 | [Register API](#lesson-07) | `express.json()`, request body, `INSERT`, `$1` placeholder |
| 08 | [Password Hashing](#lesson-08) | hash vs encryption, salt, cost factor, bcrypt |
| 09 | [Login API](#lesson-09) | `SELECT`, `bcrypt.compare()`, error message নীতি |
| 10 | [JWT তৈরি](#lesson-10) | JWT এর ৩ অংশ, signature, `sign()`, expiry |
| 11 | [Auth Middleware](#lesson-11) | middleware চেইন, `next()`, `verify()`, `req.user` |

### পর্ব ৪ — Notes CRUD
| # | Lesson | নতুন যা শিখবে |
|---|---|---|
| 12 | [Create Note](#lesson-12) | Foreign Key, ownership, `RETURNING`, validation |
| 13 | [Read Notes](#lesson-13) | `WHERE`, `ORDER BY`, list vs single, 404 |
| 14 | [Update Note](#lesson-14) | `UPDATE`, PUT vs PATCH, `rowCount`, `COALESCE` |
| 15 | [Delete Note](#lesson-15) | `DELETE`, hard vs soft delete, idempotency |

### পর্ব ৫ — বাস্তব ফিচার
| # | Lesson | নতুন যা শিখবে |
|---|---|---|
| 16 | [Search](#lesson-16) | `ILIKE`, query param, SQL Injection, index সীমা |
| 17 | [Pagination](#lesson-17) | `LIMIT`/`OFFSET`, `COUNT`, meta object, cursor |
| 18 | [Refresh Token](#lesson-18) | দুই token কেন, DB storage, rotation, reuse detection |
| 19 | [Logout](#lesson-19) | JWT কেন বাতিল হয় না, revoke কৌশল, logout-all |

### পর্ব ৬ — Production
| # | Lesson | নতুন যা শিখবে |
|---|---|---|
| 20 | [Error Handling](#lesson-20) | try/catch, error middleware, `AppError`, status map |
| 21 | [Project Structure](#lesson-21) | route → controller → service → repository |
| 22 | [Production Checklist](#lesson-22) | helmet, CORS, rate limit, log, graceful shutdown |

### 📎 Reference
| অংশ | কী আছে |
|---|---|
| [সব Flow Diagram](#ref-flows) | Request, Auth, Token refresh — এক জায়গায় |
| [SQL Reference](#ref-sql) | এই প্রজেক্টের সব query, ব্যাখ্যাসহ |
| [Postman Guide](#ref-postman) | সেটআপ + সব request |
| [Troubleshooting](#ref-trouble) | Error বার্তা → কারণ → সমাধান |
| [Glossary](#ref-glossary) | সব English term এর বাংলা মানে |

---

## 🏁 কোর্স শেষে যে API গুলো দাঁড়াবে

```
POST   /api/auth/register     নতুন ইউজার
POST   /api/auth/login        লগইন → access + refresh token
POST   /api/auth/refresh      নতুন access token
POST   /api/auth/logout       token বাতিল
GET    /api/auth/me           নিজের তথ্য              🔒

POST   /api/notes             নোট তৈরি                🔒
GET    /api/notes             তালিকা (search + page)  🔒
GET    /api/notes/:id         একটা নোট                🔒
PATCH  /api/notes/:id         নোট আপডেট               🔒
DELETE /api/notes/:id         নোট মুছে ফেলা           🔒

GET    /health                সার্ভার বেঁচে আছে কিনা

🔒 = Authorization header এ token লাগবে
```

---

## 🖼️ পুরো সিস্টেমের ছবি (কোর্স শেষের অবস্থা)

```
┌──────────────────┐
│     Postman      │   (পরে এখানে তোমার Flutter app বসবে)
└────────┬─────────┘
         │ HTTP
         │ POST /api/notes
         │ Authorization: Bearer eyJhbGci...
         │ Body: { "title": "...", "content": "..." }
         ▼
╔══════════════════════════════════════════════════════╗
║                  Node.js Process                     ║
║                    (port 5000)                       ║
║   ┌────────────────────────────────────────────┐     ║
║   │ Express App                                │     ║
║   │                                            │     ║
║   │  helmet / cors / rate-limit  ← নিরাপত্তা    │     ║
║   │            ↓                               │     ║
║   │  express.json()              ← body পড়ে    │     ║
║   │            ↓                               │     ║
║   │  Router                      ← পথ বাছে      │     ║
║   │            ↓                               │     ║
║   │  authMiddleware              ← token যাচাই  │     ║
║   │            ↓                               │     ║
║   │  Controller                  ← req/res      │     ║
║   │            ↓                               │     ║
║   │  Service                     ← নিয়মকানুন    │     ║
║   │            ↓                               │     ║
║   │  Repository                  ← SQL লেখে     │     ║
║   │            ↓                               │     ║
║   │  pg Pool                     ← connection   │     ║
║   │            ↓                               │     ║
║   │  errorMiddleware             ← সব error     │     ║
║   └────────────┬───────────────────────────────┘     ║
╚════════════════╪═════════════════════════════════════╝
                 │ SQL over TCP (port 5432)
                 ▼
        ┌────────────────────┐
        │    PostgreSQL      │
        │  users             │
        │  notes             │
        │  refresh_tokens    │
        └────────┬───────────┘
                 │ Rows (ফলাফল)
                 ▼
        একই পথে উল্টো ফিরে JSON হয়ে Postman এ
```

---

## 📊 অগ্রগতি ট্র্যাকার

```
পর্ব ১  [ ] 01   [ ] 02   [ ] 03   [ ] 04
পর্ব ২  [ ] 05   [ ] 06
পর্ব ৩  [ ] 07   [ ] 08   [ ] 09   [ ] 10   [ ] 11
পর্ব ৪  [ ] 12   [ ] 13   [ ] 14   [ ] 15
পর্ব ৫  [ ] 16   [ ] 17   [ ] 18   [ ] 19
পর্ব ৬  [ ] 20   [ ] 21   [ ] 22
```

---
---

<a id="lesson-01" name="lesson-01"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 Lesson 01 — Project তৈরি
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■□□□□□□□□□□□□□□□□□□□□□]  1/22`

| | |
|---|---|
| **আগে যা লাগবে** | কিছু না |
| **এই ধাপ শেষে** | একটা খালি Node project, `package.json` সহ |
| **নতুন শব্দ** | runtime, npm, package.json, LTS, .gitignore |

---

## 🎯 Goal

একটা folder বানাব যেটা Node.js "চিনতে" পারে — অর্থাৎ যার ভিতরে `package.json` আছে।
এখনো কোনো কোড চলবে না। এটা ভিত্তি।

---

## 🧠 আগে বুঝে নাও — Node.js জিনিসটা আসলে কী

**Node.js কোনো ভাষা নয়।** এটা একটা **runtime** (রানটাইম) — যে প্রোগ্রামটা তোমার JavaScript কোড পড়ে চালায়।

```
Dart কোড   →  চালায়  →  Dart VM
JS কোড     →  চালায়  →  Node.js
```

গল্পটা এরকম:

```
আগে:      JavaScript শুধু browser এর ভিতরে চলত।
          browser এর ভিতরে V8 নামে একটা engine ছিল।

2009:     একজন V8 engine টা browser থেকে খুলে বের করে আনল,
          কম্পিউটারে বসাল, আর যোগ করল —
             • ফাইল পড়া/লেখার ক্ষমতা
             • নেটওয়ার্ক port এ শোনার ক্ষমতা
          নাম দিল Node.js

আজ:      সেই কারণেই তুমি JavaScript দিয়ে server লিখতে পারো।
```

তাই `node server.js` লিখলে যা ঘটে — Node.js প্রোগ্রামটা চালু হয়, `server.js` ফাইলটা পড়ে, ভিতরের JavaScript কোড চালায়।

---

## 💻 Code (কমান্ড)

### ধাপ ১ — Node আছে কিনা দেখো

```bash
node -v
npm -v
```

যা দেখতে চাই:

```
v22.14.0
10.9.2
```

না থাকলে [nodejs.org](https://nodejs.org) থেকে **LTS** version নামাও।

> **LTS** = Long Term Support (দীর্ঘমেয়াদি সাপোর্ট)। মানে এই version টা কোম্পানিগুলো production এ ব্যবহার করে, বহুদিন নিরাপত্তা-প্যাচ পাবে। Flutter এর `stable` channel এর মতো। উল্টোটা হলো `Current` — নতুন ফিচার আছে কিন্তু অস্থির।

Node 20 বা তার উপরে হলেই এই কোর্সের সব চলবে।

> **npm** কেন আলাদা ইনস্টল করতে হলো না? কারণ Node ইনস্টল করলে npm সাথেই আসে। Dart SDK নামালে `pub` যেভাবে সাথে আসে।

---

### ধাপ ২ — Folder বানাও

```bash
mkdir note-app-backend
cd note-app-backend
```

- `mkdir` = make directory → ফোল্ডার বানাও
- `cd` = change directory → ফোল্ডারের ভিতরে ঢোকো

⚠️ Folder এর নামে **space, বাংলা অক্ষর বা বড় হাতের অক্ষর দিও না**। `note-app-backend` — ছোট হাতের ইংরেজি + hyphen। কারণ পরে deploy করার সময় Linux server এ space থাকা path নিয়ে ঝামেলা হয়।

---

### ধাপ ৩ — package.json বানাও

```bash
npm init -y
```

Folder এ `package.json` নামে একটা ফাইল তৈরি হলো:

```json
{
  "name": "note-app-backend",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

---

## 🔍 লাইন-বাই-লাইন

### কমান্ডের ব্যাখ্যা

| অংশ | কী করে | না দিলে কী হবে |
|---|---|---|
| `npm init` | নতুন Node project শুরু করে | `package.json` তৈরি হবে না → npm এই folder কে project ভাববে না |
| `-y` | সব প্রশ্নের ডিফল্ট উত্তর ধরে নেয় | Terminal এ ৮টা প্রশ্ন আসবে (নাম? version? author?) — Enter চেপে চেপে পার হতে হবে। ফলাফল একই |

### package.json এর প্রতিটা ফিল্ড

| ফিল্ড | কী কাজ | মুছে ফেললে কী হবে |
|---|---|---|
| `"name"` | Project এর নাম | Local এ কিছু হবে না, কিন্তু npm কিছু কমান্ডে warning দেবে |
| `"version"` | `major.minor.patch` — যেমন `1.0.0` | কিছু হবে না, তবে রাখাই নিয়ম |
| `"description"` | এক লাইনে কী কাজ করে | কিছুই না, শুধু ডকুমেন্টেশন |
| `"main"` | অন্য কেউ এই project কে import করলে কোন ফাইল খুলবে | আমরা library বানাচ্ছি না, তাই প্রভাব নেই |
| `"scripts"` | Shortcut কমান্ড — `npm run <নাম>` | **মুছলে `npm start` / `npm run dev` কাজ করবে না** |
| `"keywords"` | npm এ search এর জন্য | কিছু হবে না |
| `"license"` | কে কীভাবে ব্যবহার করতে পারবে | কিছু হবে না |

**সবচেয়ে জরুরি ফিল্ড `scripts`।** Lesson 03 এ আমরা এখানে যোগ করব:

```json
"scripts": {
  "dev": "nodemon server.js",
  "start": "node server.js"
}
```

তখন লম্বা কমান্ড না লিখে শুধু `npm run dev` লিখলেই সার্ভার চালু হবে।

---

## 🛡️ ধাপ ৪ — .gitignore বানাও (এটা বাদ দিও না)

Project folder এ `.gitignore` নামে ফাইল বানিয়ে ভিতরে লেখো:

```gitignore
# নামানো package গুলো — npm install দিলেই ফিরে আসে
node_modules/

# গোপন তথ্য — DB password, JWT secret
.env

# log ফাইল
*.log
npm-debug.log*

# OS এর জঞ্জাল
.DS_Store
```

| লাইন | কেন | না রাখলে কী হবে |
|---|---|---|
| `node_modules/` | কয়েকশো MB, হাজারো ফাইল। `npm install` দিলেই আবার তৈরি হয় | Git repo ফুলে যাবে, `git status` অপাঠ্য হবে, PR review অসম্ভব হবে |
| `.env` | এখানে DB password আর JWT secret থাকবে | **GitHub এ push হয়ে গেলে যে কেউ তোমার database এ ঢুকতে পারবে।** এটা কোডের বাগ না, এটা security incident |
| `*.log` | error log, কারো দরকার নেই | অকারণে ফাইল জমবে |
| `.DS_Store` | macOS এর নিজস্ব ফাইল | টিমমেটদের PR এ অদ্ভুত ফাইল দেখা যাবে |

> **`.env` লাইনটা নিয়ে সিরিয়াস কথা:** বাস্তবে প্রতিদিন হাজার হাজার `.env` ফাইল ভুল করে GitHub এ চলে যায়। স্বয়ংক্রিয় bot গুলো নতুন commit স্ক্যান করে সেকেন্ডের মধ্যে ওই credential তুলে নেয়। তাই `.gitignore` কোড লেখার **আগে** বানাতে হয়, পরে নয়।

---

## 🔄 Internal Flow — `npm init -y` চালালে ভিতরে কী ঘটে

```
তুমি লিখলে:  npm init -y
        │
        ▼
┌───────────────────────────────────────────────┐
│ npm বর্তমান folder এর নাম দেখে                │
│ → "note-app-backend"                          │
└───────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────┐
│ ডিফল্ট মান বসায়:                              │
│   version → 1.0.0                             │
│   main    → index.js                          │
│   license → ISC                               │
└───────────────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────────────┐
│ package.json ফাইল লিখে ফেলে                   │
└───────────────────────────────────────────────┘
        │
        ▼
   এখন এই folder = একটা Node project
```

**"Node project" হওয়ার মানে কী?** — এর পর থেকে এই folder এ `npm install <কিছু>` চালালে npm বুঝবে কোথায় ইনস্টল করতে হবে আর কোন ফাইলে হিসাব লিখতে হবে। `package.json` না থাকলে npm উপরের folder এ খুঁজতে খুঁজতে চলে যাবে আর ভুল জায়গায় ইনস্টল করবে।

---

## 🗄️ PostgreSQL

এই ধাপে প্রযোজ্য নয়। Database আসবে Lesson 05 এ।

---

## 🧪 Postman Testing

এই ধাপে প্রযোজ্য নয় — এখনো কোনো server নেই, কোনো API নেই। Postman খোলার দরকার নেই।

তবে যাচাই করার উপায় আছে:

```bash
ls -a
```

দেখা যাবে:

```
.gitignore    package.json
```

---

## ⚠️ Common Mistakes

| ভুল | কী ঘটে | সমাধান |
|---|---|---|
| ভুল folder এ `npm init` | Home directory তে `package.json` তৈরি হয়ে যায়, সব গুলিয়ে যায় | আগে `pwd` চালিয়ে দেখো কোথায় আছো |
| Folder এর নামে space (`Note App`) | পরে deploy/script এ path error | hyphen ব্যবহার করো |
| `.gitignore` পরে বানানো | ততক্ষণে `node_modules` git এ ঢুকে গেছে | কোড লেখার আগেই `.gitignore` বানাও |
| `sudo npm init` চালানো | ফাইলের মালিকানা root হয়ে যায়, পরে permission error | npm এ কখনো `sudo` না |
| package.json হাতে এলোমেলো এডিট | JSON syntax ভাঙলে npm এর সব কমান্ড fail করবে | comma আর quote সাবধানে |

---

## 🏋️ Practice

**১.** `package.json` এর `description` ফিল্ডে লেখো:
`"Note taking app backend with Node, Express and PostgreSQL"`

**২.** ভাবো: `package.json` ফাইলটা মুছে ফেললে `node_modules` folder টা কি নষ্ট হবে? আর `node_modules` মুছলে `package.json` কি নষ্ট হবে?

<details>
<summary>উত্তর দেখো</summary>

দুটোই টিকে থাকবে, কিন্তু ফলাফল ভিন্ন —

- `package.json` মুছলে: `node_modules` এ কোড থেকে যাবে, কিন্তু npm আর জানবে না তোমার কী কী দরকার। নতুন মেশিনে project টা আর তৈরি করা যাবে না। **এটাই বেশি ক্ষতিকর।**
- `node_modules` মুছলে: `npm install` চালালেই পুরোটা ফিরে আসবে, কারণ তালিকাটা `package.json` এ লেখা আছে।

মনে রাখার নিয়ম: **`package.json` হলো রেসিপি, `node_modules` হলো রান্না করা খাবার।** রেসিপি থাকলে খাবার আবার বানানো যায়, উল্টোটা নয়।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-02" name="lesson-02"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📥 Lesson 02 — Dependencies ইনস্টল
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■□□□□□□□□□□□□□□□□□□□□]  2/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 01 (package.json তৈরি) |
| **এই ধাপ শেষে** | Express ইনস্টল হবে, `node_modules` তৈরি হবে |
| **নতুন শব্দ** | dependency, devDependency, registry, semver, lock file |

---

## 🎯 Goal

Server লেখার জন্য দরকারি package গুলো নামানো। এবং বোঝা — `node_modules` ফোল্ডারটা আসলে কী, ওখানে কীভাবে জিনিস আসে।

---

## 💻 Code

```bash
npm install express dotenv
npm install --save-dev nodemon
```

Output:

```
added 69 packages, and audited 70 packages in 3s
found 0 vulnerabilities
```

---

## 🤔 কেন এখন শুধু এই তিনটা? বাকি package কোথায়?

তোমার stack এ ৫টা package আছে — express, pg, bcrypt, jsonwebtoken, dotenv। আমি ইচ্ছা করেই সব একসাথে নামাচ্ছি না।

কারণ, senior হিসেবে আমি চাই প্রতিটা package তুমি ইনস্টল করো **ঠিক যেদিন সেটার দরকার পড়বে** — তাহলে "এটা কেন আছে" প্রশ্নের উত্তর মাথায় গেঁথে যাবে:

```
express        →  এখনই     →  server বানাতে হবে (Lesson 03)
dotenv         →  এখনই     →  port নম্বর কোডের বাইরে রাখব (Lesson 03)
nodemon        →  এখনই     →  বারবার হাতে restart করার কষ্ট বাঁচাবে
─────────────────────────────────────────────────────────────
pg             →  Lesson 05 →  PostgreSQL এ কথা বলার দিন
bcrypt         →  Lesson 08 →  password hash করার দিন
jsonwebtoken   →  Lesson 10 →  token বানানোর দিন
```

এটা কেবল পড়ানোর কৌশল নয় — বাস্তব প্রজেক্টেও এই অভ্যাসটাই ভালো। যে package এখনো দরকার নেই, সেটা আগে থেকে নামিয়ে রাখলে project ভারী হয়, আর ৬ মাস পর কেউ জিজ্ঞেস করে "এই package টা কে এনেছিল, কী কাজে?"

---

## 🔍 লাইন-বাই-লাইন

### `npm install express dotenv`

| অংশ | মানে |
|---|---|
| `npm` | Node Package Manager — package নামানোর টুল |
| `install` | নামাও (সংক্ষেপে `i` লিখলেও চলে) |
| `express` | HTTP request handle করার framework |
| `dotenv` | `.env` ফাইল থেকে গোপন তথ্য পড়ার library |

**express কী করে, এক লাইনে:** Raw Node.js দিয়ে server লিখলে URL parse করা, method চেনা, body পড়া — সব হাতে করতে হয়, ২০০+ লাইন। Express ওই কাজগুলো করে দেয়, তুমি ৫ লাইনে route লিখে ফেলো।

**dotenv কী করে, এক লাইনে:** `PORT=5000` লেখা একটা ফাইল পড়ে সেটাকে প্রোগ্রামের ভিতরে `process.env.PORT` হিসেবে ঢুকিয়ে দেয়। ফলে password/secret কোডে লিখতে হয় না।

---

### `npm install --save-dev nodemon`

| অংশ | মানে | না দিলে কী হবে |
|---|---|---|
| `--save-dev` (সংক্ষেপে `-D`) | এটা **devDependency** — শুধু ডেভেলপমেন্টে লাগবে | nodemon সাধারণ dependency হয়ে যাবে। কাজ করবে ঠিকই, কিন্তু production server এ অপ্রয়োজনীয় কোড deploy হবে |
| `nodemon` | node + monitor — ফাইল save করলে server নিজে restart হয় | প্রতিবার কোড বদলে `Ctrl+C` চেপে আবার `node server.js` লিখতে হবে। দিনে ২০০ বার |

> **dependency vs devDependency — সহজ নিয়ম:**
> *"Production server এ এই কোডটা কি চলবে?"*
> হ্যাঁ → `dependencies`  (express, pg, bcrypt)
> না → `devDependencies` (nodemon, jest, eslint)

---

## 🔄 Internal Flow — `npm install express` এ ভিতরে কী ঘটে

```
তুমি লিখলে:  npm install express
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ১. ইন্টারনেটে npm registry তে যায়                  │
│    (registry.npmjs.org — package এর গুদাম)         │
│    জিজ্ঞেস করে: "express এর সর্বশেষ version কী?"   │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ২. উত্তর পায়: express@5.1.0                        │
│    সাথে দেখে express নিজে কোন কোন package ব্যবহার  │
│    করে → তাদেরও তালিকা নেয় (dependency tree)       │
│                                                    │
│    express                                         │
│      ├── body-parser                               │
│      │     └── bytes                               │
│      ├── router                                    │
│      └── ... আরও ৬০+                               │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ৩. সবগুলো নামিয়ে node_modules/ এ রাখে              │
│    (তাই ১টা package চাইলে ৬৯টা folder আসে)         │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ৪. package.json এ লিখে দেয়:                        │
│    "dependencies": { "express": "^5.1.0" }         │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ৫. package-lock.json বানায় —                       │
│    প্রতিটা package এর হুবহু version + hash লিখে রাখে│
└────────────────────────────────────────────────────┘
```

---

## 📄 এখন package.json এ নতুন অংশ

```json
{
  "name": "note-app-backend",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "dotenv": "^17.2.3",
    "express": "^5.1.0"
  },
  "devDependencies": {
    "nodemon": "^3.1.10"
  }
}
```

### `^` চিহ্নটার মানে (semver — Semantic Versioning)

```
     5  .  1  .  0
     │     │     │
     │     │     └── patch  → শুধু বাগ ফিক্স, কিছু ভাঙে না
     │     └──────── minor  → নতুন ফিচার, পুরনো কোড চলবে
     └────────────── major  → breaking change, পুরনো কোড ভাঙতে পারে


"^5.1.0"  মানে:  ✅ 5.1.0, 5.1.9, 5.4.2 — সব চলবে
                 ❌ 6.0.0 — চলবে না

কারণ major বদলালে তোমার কোড ভাঙার ঝুঁকি আছে।
```

Flutter এর `pubspec.yaml` এ `^1.2.0` হুবহু একই অর্থ। চেনা লাগছে?

| চিহ্ন | মানে |
|---|---|
| `^5.1.0` | 5.x.x এর মধ্যে যেকোনো নতুন (ডিফল্ট) |
| `~5.1.0` | শুধু 5.1.x — আরও কড়া |
| `5.1.0` | ঠিক এই version, নড়চড় নয় |

---

## 📁 তিনটা জিনিসের পার্থক্য (এটা খুব গুরুত্বপূর্ণ)

| জিনিস | কী ধরে রাখে | git এ যাবে? |
|---|---|---|
| `package.json` | **কী চাই** — নাম + version range | ✅ অবশ্যই |
| `package-lock.json` | **ঠিক কী বসেছে** — হুবহু version + hash | ✅ অবশ্যই |
| `node_modules/` | **আসল কোড** — হাজার হাজার ফাইল | ❌ কখনো না |

**`package-lock.json` কেন দরকার?** ধরো তোমার `package.json` এ লেখা `"express": "^5.1.0"`. আজ তুমি install দিলে বসল 5.1.0। তিন মাস পর তোমার টিমমেট install দিল — ততদিনে 5.4.0 বেরিয়েছে, তার মেশিনে 5.4.0 বসল। এখন তোমার মেশিনে কাজ করে, তার মেশিনে করে না — **"কিন্তু আমার মেশিনে তো চলে!"** সমস্যা।

`package-lock.json` git এ থাকলে npm ওই ফাইল দেখে হুবহু একই version বসায়। সবার মেশিনে এক জিনিস।

---

## 🗄️ PostgreSQL

প্রযোজ্য নয়। Lesson 05 এ।

---

## 🧪 Postman Testing

এখনো নয়। তবে যাচাই করো:

```bash
npm ls --depth=0
```

Output:

```
note-app-backend@1.0.0
├── dotenv@17.2.3
├── express@5.1.0
└── nodemon@3.1.10
```

`--depth=0` মানে — শুধু তোমার সরাসরি চাওয়া package দেখাও, তাদের ভিতরের ৬৬টা নয়।

---

## ⚠️ Common Mistakes

| ভুল | কী ঘটে | সমাধান |
|---|---|---|
| `npm init` না করে `npm install` | npm উপরের folder এ package.json খোঁজে, ভুল জায়গায় ইনস্টল করে | আগে `npm init -y` |
| `sudo npm install` | ফাইল permission নষ্ট, পরে ভুতুড়ে EACCES error | কখনো sudo না |
| `node_modules` git এ push | Repo ২০০MB+, clone করতে ৫ মিনিট | `.gitignore` আগে বানাও |
| `package-lock.json` git এ না রাখা | টিমে version mismatch, "আমার মেশিনে চলে" সমস্যা | Commit করো |
| version হাতে এডিট করা | package.json বলে এক, node_modules এ অন্য | `npm install pkg@version` দিয়ে বদলাও |
| অফলাইনে install চেষ্টা | `ENOTFOUND registry.npmjs.org` | ইন্টারনেট লাগবে, cache না থাকলে |

---

## 🏋️ Practice

**১.** ভাবো: তুমি `node_modules` folder টা পুরো `rm -rf` দিয়ে মুছে ফেললে। Project কি মরে গেল?

<details>
<summary>উত্তর</summary>

না। `npm install` চালালেই npm `package-lock.json` পড়ে হুবহু আগের version গুলো আবার নামিয়ে দেবে।

আসলে এটা একটা পরিচিত সমাধান — কিছু অদ্ভুত error এ ডেভেলপাররা `node_modules` আর `package-lock.json` মুছে আবার install দেয়। Flutter এর `flutter clean` এর মতো।
</details>

**২.** ভাবো: `"express": "^5.1.0"` এর জায়গায় `"express": "5.1.0"` লিখলে কী পার্থক্য হবে?

<details>
<summary>উত্তর</summary>

`^` ছাড়া লিখলে npm ঠিক 5.1.0 বসাবে, কখনো 5.2.0 নয় — এমনকি নিরাপত্তা-প্যাচ বেরোলেও না।

সুবিধা: সম্পূর্ণ নিশ্চয়তা।
অসুবিধা: security fix গুলো আপনাআপনি আসবে না, হাতে আপডেট করতে হবে।

বাস্তবে বেশিরভাগ প্রজেক্ট `^` রাখে, আর নিশ্চয়তার জন্য `package-lock.json` এর উপর ভরসা করে।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-03" name="lesson-03"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 Lesson 03 — Express Server চালু
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■□□□□□□□□□□□□□□□□□□□]  3/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 02 (express ইনস্টল) |
| **এই ধাপ শেষে** | সার্ভার চালু থাকবে, terminal এ বার্তা দেখাবে |
| **নতুন শব্দ** | server, port, require, module, callback, event loop, .env |

---

## 🎯 Goal

প্রথম `server.js` ফাইল লিখব। সার্ভার চালু হবে আর একটা port এ **শুনতে** থাকবে। এখনো কোনো API নেই — শুধু সার্ভার বেঁচে থাকবে।

---

## 🧠 "Server চালু হওয়া" মানে আসলে কী

Flutter app চালালে UI দেখা যায়। Server চালালে **কিছুই দেখা যায় না** — terminal একটা লাইন লিখে চুপ করে বসে থাকে। এটাই স্বাভাবিক।

```
সাধারণ প্রোগ্রাম:               Server প্রোগ্রাম:
────────────────                ────────────────
শুরু হয়                          শুরু হয়
কাজ করে                          port 5000 এ "শোনা" শুরু করে
শেষ হয়ে বন্ধ                      ┌──────────────────────┐
                                 │ অপেক্ষা...            │
                                 │ কেউ request পাঠাক    │
                                 │ অপেক্ষা...            │
                                 └──────────────────────┘
                                 (Ctrl+C না চাপা পর্যন্ত চলতেই থাকে)
```

**Port (পোর্ট) কী?** একটা কম্পিউটারের একটাই IP ঠিকানা, কিন্তু ভিতরে অনেক প্রোগ্রাম চলে। কোন প্রোগ্রামের কাছে ডেটা যাবে সেটা ঠিক করে port নম্বর।

```
তোমার কম্পিউটার = একটা বিল্ডিং (IP = 127.0.0.1)
Port            = ওই বিল্ডিং এর ফ্ল্যাট নম্বর

  Port 5000  →  তোমার Node server
  Port 5432  →  PostgreSQL
  Port 3000  →  React app (যদি চালাও)
  Port 80    →  সাধারণ ওয়েবসাইট (http)
  Port 443   →  নিরাপদ ওয়েবসাইট (https)
```

তাই `http://localhost:5000` মানে — "এই কম্পিউটারের ৫০০০ নম্বর ফ্ল্যাটে যাও"।

---

## 💻 Code

### ফাইল ১ — `.env` (project root এ)

```env
PORT=5000
NODE_ENV=development
```

### ফাইল ২ — `server.js` (project root এ)

```js
require('dotenv').config();

const express = require('express');

const app = express();

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

### ফাইল ৩ — `package.json` এ script যোগ করো

```json
"scripts": {
  "dev": "nodemon server.js",
  "start": "node server.js"
}
```

### চালাও

```bash
npm run dev
```

Terminal এ দেখবে:

```
[nodemon] 3.1.10
[nodemon] watching path(s): *.*
[nodemon] starting `node server.js`
✅ Server running on http://localhost:5000
```

এরপর কার্সার ব্লিঙ্ক করতে থাকবে, prompt ফিরে আসবে না। **এটাই সফলতা** — সার্ভার বেঁচে আছে।

---

## 🔍 লাইন-বাই-লাইন

### `require('dotenv').config();`

```js
require('dotenv').config();
```

দুটো কাজ একসাথে:

1. `require('dotenv')` → dotenv package টা `node_modules` থেকে খুঁজে এনে load করে
2. `.config()` → `.env` ফাইল পড়ে ভিতরের প্রতিটা লাইন `process.env` এ ঢুকিয়ে দেয়

```
.env ফাইল                    process.env (মেমরিতে)
──────────────               ─────────────────────
PORT=5000            →       process.env.PORT      = "5000"
NODE_ENV=development →       process.env.NODE_ENV  = "development"
```

**`require` কী?** Node এর ফাইল/package আনার পদ্ধতি। Dart এর `import` এর সমতুল্য।

```dart
// Dart
import 'package:http/http.dart' as http;
```
```js
// Node (CommonJS)
const http = require('http');
```

**সবচেয়ে উপরে কেন?** কারণ `.env` এর মান পরের লাইনগুলোতে লাগবে। নিচে লিখলে ততক্ষণে `process.env.PORT` পড়া হয়ে গেছে, মান পাবে `undefined`।

| এই লাইন মুছে দিলে | কী হবে |
|---|---|
| পুরো লাইন | `.env` পড়া হবে না → `process.env.PORT` হবে `undefined` → fallback 5000 এ চলবে। এখন সমস্যা হবে না, কিন্তু Lesson 05 এ DB password পড়তে না পেরে সার্ভার ক্র্যাশ করবে |

---

### `const express = require('express');`

Express package টা এনে `express` নামের একটা variable এ রাখল।

**`const` কেন, `let` নয়?** কারণ এই মান আর কখনো বদলাবে না। `const` দিলে ভুল করে বদলে ফেলার সম্ভাবনা থাকে না। Dart এর `final` এর মতো।

| মুছে দিলে | `ReferenceError: express is not defined` — পরের লাইনেই ক্র্যাশ |

---

### `const app = express();`

```js
const app = express();
```

`express` একটা **ফাংশন**। ওটা কল করলে একটা "app object" ফেরত দেয়। এই `app` অবজেক্টটাই তোমার পুরো সার্ভার — এর গায়ে তুমি route লাগাবে, middleware লাগাবে।

```
express()  →  একটা কারখানা (factory)
   ↓
  app     →  কারখানার বানানো জিনিস
              যার গায়ে আছে:
                app.get()     — GET route
                app.post()    — POST route
                app.use()     — middleware
                app.listen()  — চালু করা
```

| মুছে দিলে | কিছুই বানানো হবে না, পরের লাইনে `app is not defined` |

---

### `const PORT = process.env.PORT || 5000;`

```js
const PORT = process.env.PORT || 5000;
```

- `process` → Node এর built-in object, চলমান প্রোগ্রামের তথ্য রাখে
- `process.env` → সব environment variable এর তালিকা
- `||` → "অথবা"। বাঁ পাশের মান খালি/undefined হলে ডান পাশেরটা নেবে

```
যদি .env এ PORT থাকে      → PORT = 5000 (ফাইল থেকে)
যদি না থাকে               → PORT = 5000 (fallback)
যদি hosting সার্ভার দেয়   → PORT = 43217 (তাদেরটা)
```

**Fallback কেন দরকার?** Production hosting (Render, Railway, Heroku) তোমাকে port নম্বর নিজে ঠিক করতে দেয় না — তারা `process.env.PORT` এ একটা নম্বর ঢুকিয়ে দেয়। তোমার কোড ওটা মেনে নিলে যেকোনো জায়গায় deploy হবে।

| মুছে/বদলালে | কী হবে |
|---|---|
| `\|\| 5000` অংশ মুছলে | `.env` না থাকলে `PORT` হবে `undefined` → সার্ভার এলোমেলো একটা port এ চালু হবে |
| পুরো লাইন হার্ডকোড করলে (`const PORT = 5000`) | Local এ চলবে, কিন্তু deploy করলে hosting এর দেওয়া port ধরবে না → সাইট খুলবে না |

---

### `app.listen(PORT, callback)`

```js
app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

**এই লাইনটাই সার্ভারকে জীবিত করে।** এখানে তিনটা নতুন ধারণা:

**১. `app.listen(PORT)`** — অপারেটিং সিস্টেমকে বলে: "৫০০০ নম্বর port টা আমাকে দাও, ওখানে যা আসবে আমি ধরব।"

**২. `() => { ... }` — Arrow function / Callback**
এটা একটা ফাংশন যেটা তুমি এখন লিখছ কিন্তু **এখন চালাচ্ছ না** — Express এটা চালাবে, যখন সার্ভার সফলভাবে চালু হবে।

```dart
// Dart এ তুমি এটা রোজ লেখো:
onPressed: () { print('চাপ পড়ল'); }
```
```js
// JS এ হুবহু একই জিনিস:
app.listen(PORT, () => { console.log('চালু হলো'); });
```

**৩. `` `...${PORT}` `` — Template literal**
ব্যাকটিক (`) দিয়ে লেখা string, ভিতরে `${}` দিয়ে variable বসানো যায়। Dart এর `'Port: $PORT'` এর সমান।

| মুছে দিলে | কী হবে |
|---|---|
| পুরো `app.listen(...)` | **সার্ভার চালু হবে না।** প্রোগ্রাম শুরু হয়ে সাথে সাথে শেষ হয়ে যাবে, terminal prompt ফিরে আসবে। কোনো error দেখাবে না — এটাই বিভ্রান্তিকর |
| শুধু `console.log` | সার্ভার ঠিকই চলবে, কিন্তু তুমি জানতে পারবে না চালু হয়েছে কিনা |

---

### package.json এর script

```json
"scripts": {
  "dev": "nodemon server.js",
  "start": "node server.js"
}
```

| Script | কমান্ড | কখন |
|---|---|---|
| `npm run dev` | nodemon চালায় — ফাইল save করলে auto restart | ডেভেলপমেন্টে |
| `npm start` | সাধারণ node — restart নেই | Production এ |

> `start` একটা বিশেষ নাম — `npm run start` না লিখে শুধু `npm start` লিখলেও চলে। বাকি সবগুলোতে `run` লাগে। Production hosting গুলোও ডিফল্টে `npm start` খোঁজে।

---

## 🔄 Internal Flow — `npm run dev` চালালে কী ঘটে

```
তুমি লিখলে:  npm run dev
        │
        ▼
┌──────────────────────────────────────────────────┐
│ npm  package.json এর scripts এ "dev" খোঁজে       │
│ পায়: "nodemon server.js"                         │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ nodemon চালু হয়, folder এর সব ফাইল watch করে     │
│ তারপর চালায়: node server.js                      │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ Node.js প্রক্রিয়া (process) শুরু হয়               │
│   • server.js ফাইল পড়ে                           │
│   • উপর থেকে নিচে প্রতিটা লাইন চালায়              │
└──────────────────────────────────────────────────┘
        │
        ├─→ dotenv .env পড়ে process.env ভরে
        ├─→ express package মেমরিতে আসে
        ├─→ app object তৈরি হয়
        │
        ▼
┌──────────────────────────────────────────────────┐
│ app.listen(5000) চলে                             │
│   → OS কে বলে: "port 5000 আমাকে দাও"             │
│   → OS দেয় (যদি খালি থাকে)                       │
│   → callback চলে → console.log ছাপে              │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ ফাইলের শেষ লাইন শেষ। কিন্তু প্রোগ্রাম বন্ধ হয় না! │
│                                                  │
│ কারণ Event Loop (ইভেন্ট লুপ) দেখে —              │
│ "একটা খোলা port আছে, কাজ এখনো বাকি" → ঘুরতে থাকে │
└──────────────────────────────────────────────────┘
        │
        ▼
    ┌───────────────────────────┐
    │  অপেক্ষা... অপেক্ষা...      │  ← এখন এখানে আছি
    │  request আসলেই জেগে উঠবে   │
    └───────────────────────────┘
```

> **Event Loop** = Node এর অন্তহীন চক্র। প্রতি পাক ঘুরে দেখে: "কোনো কাজ কি এসেছে? নতুন request? ফাইল পড়া শেষ? DB উত্তর দিয়েছে?" — কাজ থাকলে করে, না থাকলে অপেক্ষা করে। **কোনো অসমাপ্ত কাজ না থাকলেই কেবল প্রোগ্রাম বন্ধ হয়।** খোলা port একটা অসমাপ্ত কাজ, তাই সার্ভার চলতেই থাকে।

---

## 🗄️ PostgreSQL

প্রযোজ্য নয়। পরের-পরের lesson এ।

---

## 🧪 Postman Testing

Browser এ `http://localhost:5000` খুলে দেখো।

**যা দেখবে:**

```
Cannot GET /
```

**এটা কি error?** না — এটা **সুখবর**। এই বার্তাটা Express নিজে পাঠিয়েছে, মানে তোমার সার্ভার বেঁচে আছে এবং request পেয়েছে। শুধু `/` route টা এখনো বানানো হয়নি।

Server বন্ধ থাকলে দেখতে অন্যরকম:

```
This site can't be reached
ERR_CONNECTION_REFUSED
```

| যা দেখলে | মানে |
|---|---|
| `Cannot GET /` | ✅ সার্ভার চলছে, route নেই |
| `ERR_CONNECTION_REFUSED` | ❌ সার্ভার চলছে না |

---

## ⚠️ Common Mistakes

| ভুল | Error | সমাধান |
|---|---|---|
| Port আগে থেকে ব্যবহৃত | `EADDRINUSE: address already in use :::5000` | পুরনো সার্ভার বন্ধ করো: `lsof -ti:5000 \| xargs kill -9` অথবা `.env` এ অন্য port দাও |
| ফাইলের নাম ভুল (`Server.js`) | `Cannot find module` | Linux/deploy এ case-sensitive। ছোট হাতে `server.js` |
| `require('Express')` বড় হাতে | `Cannot find module 'Express'` | package এর নাম হুবহু ছোট হাতে |
| `app.listen()` লিখতে ভুলে যাওয়া | কোনো error নেই, প্রোগ্রাম চুপচাপ শেষ | prompt ফিরে এলে বুঝবে listen নেই |
| dotenv এর `.config()` না লেখা | `process.env.PORT` = undefined | `require('dotenv').config()` — `.config()` অংশটা লাগবেই |
| `.env` ফাইলে `PORT = 5000` (space সহ) | মান হতে পারে `" 5000"` | space ছাড়া: `PORT=5000` |
| `.env` ফাইলে quote (`PORT="5000"`) | সাধারণত চলে, কিন্তু বিভ্রান্তিকর | quote ছাড়াই লেখো |

---

## 🏋️ Practice

**১.** `.env` এ `PORT=4000` করে দেখো — সার্ভার কোন port এ চালু হয়? তারপর `.env` থেকে `PORT` লাইনটা মুছে দিয়ে আবার চালাও। কী হয়?

**২.** ভাবো: `app.listen(PORT, callback)` লাইনটার নিচে যদি `console.log('শেষ')` লিখি, সেটা কি ছাপা হবে? কখন?

<details>
<summary>উত্তর</summary>

হ্যাঁ, ছাপা হবে — এবং প্রায় সাথে সাথেই।

কারণ `app.listen()` **blocking নয়**। ও port ধরার কাজটা শুরু করে দিয়ে সাথে সাথে পরের লাইনে চলে যায়। তাই ক্রম এরকম হতে পারে:

```
শেষ
✅ Server running on http://localhost:5000
```

এটাই Node এর asynchronous (অ্যাসিনক্রোনাস) স্বভাব — "কাজটা শুরু করে দাও, শেষ হলে callback ডাকব"। Lesson 05 এ এটা নিয়ে বিস্তারিত হবে, কারণ database এর সাথে কথা বলতে গেলে এই ধারণাটা লাগবেই।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-04" name="lesson-04"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎯 Lesson 04 — প্রথম API
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■□□□□□□□□□□□□□□□□□□]  4/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 03 (সার্ভার চলছে) |
| **এই ধাপ শেষে** | Postman এ প্রথম JSON response পাবে |
| **নতুন শব্দ** | route, endpoint, req, res, HTTP method, status code |

---

## 🎯 Goal

দুটো API বানাব:

```
GET /health        → সার্ভার বেঁচে আছে কিনা
GET /api/ping      → JSON ফেরত দেওয়ার প্রথম উদাহরণ
```

Postman দিয়ে hit করে JSON response দেখব। এবং **request কোন পথে যায়** সেটা পুরোপুরি বুঝব।

---

## 💻 Code

`server.js` — নতুন লাইনগুলো 👉 চিহ্ন দিয়ে দেখানো:

```js
require('dotenv').config();

const express = require('express');

const app = express();

const PORT = process.env.PORT || 5000;

// 👉 নতুন — সার্ভার বেঁচে আছে কিনা জানার route
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'ok',
    uptime: process.uptime(),
  });
});

// 👉 নতুন — প্রথম আসল API
app.get('/api/ping', (req, res) => {
  res.status(200).json({
    success: true,
    message: 'pong',
  });
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

---

## 🔍 লাইন-বাই-লাইন

### `app.get('/health', (req, res) => { ... })`

এই এক লাইনে চারটা জিনিস আছে। এক এক করে:

```
app  .  get  (  '/health'  ,  (req, res) => { ... }  )
 │       │         │                    │
 │       │         │                    └── handler — কী কাজ হবে
 │       │         └── path — কোন URL
 │       └── HTTP method — কোন ধরনের request
 └── আমাদের Express app
```

**১. `app.get` — HTTP Method**

| Method | কাজ | Note App এ ব্যবহার |
|---|---|---|
| `GET` | ডেটা **পড়া** | নোট তালিকা দেখা |
| `POST` | নতুন ডেটা **বানানো** | নোট তৈরি, login, register |
| `PUT` | পুরো ডেটা **বদলানো** | পুরো নোট replace |
| `PATCH` | আংশিক **বদলানো** | শুধু title বদলানো |
| `DELETE` | **মুছে ফেলা** | নোট ডিলিট |

তুমি Flutter এ `http.get()` / `http.post()` লেখো — ওটা চাওয়ার দিক। এখানে `app.get()` মানে **"কেউ GET পাঠালে আমি ধরব"** — শোনার দিক।

**২. `'/health'` — Path (পথ)**

```
http://localhost:5000/health
└──────┬──────┘└─┬─┘└──┬──┘
   protocol    port   path  ← Express শুধু এই অংশটা মেলায়
```

**৩. `(req, res) => {}` — Handler function**

Express এই ফাংশনটা চালাবে যখন কেউ `GET /health` এ আসবে। দুটো জিনিস হাতে ধরিয়ে দেবে:

| Parameter | পুরো নাম | কী ধরে রাখে |
|---|---|---|
| `req` | request | ক্লায়েন্ট **যা পাঠিয়েছে** — URL, header, body, token |
| `res` | response | তুমি **যা ফেরত পাঠাবে** — এটা দিয়েই উত্তর দেবে |

> নাম `req`/`res` হতেই হবে এমন না — `(request, response)` লিখলেও চলে। কিন্তু পুরো Node দুনিয়া `req, res` লেখে, তাই এটাই লেখো।

---

### `res.status(200).json({ ... })`

```js
res.status(200).json({ status: 'ok' });
     │          │
     │          └── ২. body হিসেবে JSON পাঠাও
     └── ১. HTTP status code বসাও
```

**`.status(200)` — HTTP Status Code**

তুমি Flutter এ `if (response.statusCode == 200)` লেখো — এই নম্বরটা তুমিই এখন বসাচ্ছ।

```
2xx  ✅ সফল
     200 OK              — সব ঠিক (GET, PATCH, DELETE)
     201 Created         — নতুন কিছু বানানো হলো (POST)
     204 No Content      — সফল, কিন্তু ফেরত দেওয়ার কিছু নেই

4xx  ⚠️ ক্লায়েন্টের ভুল
     400 Bad Request     — ভুল ডেটা পাঠিয়েছ
     401 Unauthorized    — token নেই বা ভুল      ← Lesson 11
     403 Forbidden       — token আছে, কিন্তু অনুমতি নেই
     404 Not Found       — জিনিসটা নেই
     409 Conflict        — যেমন: ইমেইল আগেই আছে   ← Lesson 07
     422 Unprocessable   — validation ব্যর্থ

5xx  ❌ সার্ভারের ভুল (তোমার দোষ)
     500 Internal Error  — কোড ক্র্যাশ করেছে
     503 Unavailable     — DB ডাউন
```

**`.json({...})` — কী করে**

তিনটা কাজ একসাথে:

1. JavaScript object টাকে JSON string এ রূপান্তর করে
2. Header বসায়: `Content-Type: application/json`
3. Response পাঠিয়ে দেয়

```js
{ success: true, message: 'pong' }        // JS object (মেমরিতে)
        ↓  .json() রূপান্তর করে
'{"success":true,"message":"pong"}'        // JSON string (তারে যায়)
        ↓  Flutter এ পৌঁছে
jsonDecode(response.body)                  // আবার Map হয়ে যায়
```

| এই অংশ বাদ দিলে | কী হবে |
|---|---|
| `.status(200)` | কিছু ভাঙবে না — Express ডিফল্টে 200 ধরে নেয়। তবে 201/404 এর ক্ষেত্রে অবশ্যই লিখতে হবে |
| `.json()` এর বদলে `.send()` | Object দিলে Express নিজেই JSON করে দেয়। তবু `.json()` লেখো — উদ্দেশ্য স্পষ্ট থাকে |
| পুরো `res.` লাইনটা | **সবচেয়ে বাজে অবস্থা** — কোনো উত্তর যাবে না। Postman ঘুরতেই থাকবে যতক্ষণ না timeout হয়। Express জানে না তুমি শেষ করেছ কিনা |

> **সোনার নিয়ম: প্রতিটা handler এ ঠিক একবার response পাঠাতে হবে।**
> শূন্যবার → ক্লায়েন্ট ঝুলে থাকে।
> দুইবার → `Cannot set headers after they are sent` error।

---

### `process.uptime()`

Node process কত সেকেন্ড ধরে চলছে সেটা ফেরত দেয়। `/health` route এ এটা রাখলাম কারণ বাস্তবে এই তথ্যটা কাজে লাগে — সার্ভার বারবার restart হচ্ছে কিনা বোঝা যায়।

> **`/health` route কেন বানালাম?** Production এ hosting আর load balancer প্রতি ৩০ সেকেন্ডে এই route এ hit করে দেখে সার্ভার জীবিত কিনা। 200 না পেলে ধরে নেয় সার্ভার মরে গেছে, ট্রাফিক অন্য জায়গায় পাঠায় বা restart করে। প্রায় প্রতিটা production backend এ এই route থাকে।

---

## 🔄 Internal Flow — সম্পূর্ণ পথ

এবার সবচেয়ে গুরুত্বপূর্ণ অংশ। Postman এ Send চাপলে ঠিক কী কী ঘটে:

```
┌─────────────────────────────────────────────────────────┐
│  ১. Postman                                             │
│     তুমি লিখলে: GET http://localhost:5000/api/ping      │
│     Send চাপলে                                          │
└──────────────────────┬──────────────────────────────────┘
                       │  HTTP request তৈরি হয়:
                       │
                       │    GET /api/ping HTTP/1.1
                       │    Host: localhost:5000
                       │    Accept: */*
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ২. Operating System                                    │
│     দেখে port 5000 → এই port কার?                       │
│     → Node process এর                                   │
│     → ডেটা তার হাতে দেয়                                 │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ৩. Node Event Loop                                     │
│     "নতুন কাজ এসেছে!" → Express কে জাগায়                │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ৪. Express — req আর res object বানায়                   │
│                                                         │
│     req.method  = 'GET'                                 │
│     req.path    = '/api/ping'                           │
│     req.headers = { host: 'localhost:5000', ... }       │
│     req.query   = {}                                    │
│                                                         │
│     res = খালি খাম, তুমি ভরবে                            │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ৫. Router — উপর থেকে নিচে মেলাতে থাকে                  │
│                                                         │
│     app.get('/health')    →  path মেলে না ❌ পরেরটা দেখো │
│     app.get('/api/ping')  →  method GET ✅               │
│                              path মেলে   ✅ → এইটা!      │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ৬. Handler চলে                                         │
│     (req, res) => {                                     │
│        res.status(200).json({ success: true, ... })     │
│     }                                                   │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ৭. Express HTTP response বানায়                         │
│                                                         │
│     HTTP/1.1 200 OK                                     │
│     Content-Type: application/json                      │
│     Content-Length: 38                                  │
│                                                         │
│     {"success":true,"message":"pong"}                   │
└──────────────────────┬──────────────────────────────────┘
                       ▼
┌─────────────────────────────────────────────────────────┐
│  ৮. Postman পায়, সুন্দর করে সাজিয়ে দেখায়                │
│     (Flutter হলে এখানে jsonDecode হতো)                   │
└─────────────────────────────────────────────────────────┘

সময় লাগে: ২-৫ মিলিসেকেন্ড
```

**সংক্ষেপে মনে রাখার ছক** (এটাই বাকি পুরো কোর্সের কাঠামো):

```
Postman → Express → Router → Handler → res.json() → Postman
```

Lesson 12 এ এর মাঝখানে ঢুকবে Database:

```
Postman → Express → Router → Middleware → Controller → SQL → PostgreSQL
                                              ↑                  │
                                              └──── Rows ────────┘
                                              ↓
                                        res.json() → Postman
```

---

## 🗄️ PostgreSQL

এখনো নয় — পরের lesson এ।

---

## 🧪 Postman Testing

### Test ১ — Health check

```
Method : GET
URL    : http://localhost:5000/health
```

Response (Status **200 OK**):

```json
{
  "status": "ok",
  "uptime": 42.318
}
```

### Test ২ — Ping

```
Method : GET
URL    : http://localhost:5000/api/ping
```

Response (Status **200 OK**):

```json
{
  "success": true,
  "message": "pong"
}
```

### Test ৩ — নেই এমন route (ইচ্ছা করে ভুল করো)

```
Method : GET
URL    : http://localhost:5000/api/nothing
```

Response (Status **404 Not Found**) — Express এর ডিফল্ট HTML পাতা।

> লক্ষ্য করো — এটা HTML, JSON নয়। তোমার Flutter app `jsonDecode()` করতে গিয়ে ক্র্যাশ করবে। Lesson 20 এ আমরা এটা ঠিক করব যাতে সব উত্তরই JSON হয়।

### Test ৪ — ভুল method

```
Method : POST
URL    : http://localhost:5000/api/ping
```

Response: **404**। কারণ আমরা শুধু `app.get()` লিখেছি, `app.post()` নয়। **Route মেলে path + method দুটো একসাথে মিলিয়ে।**

---

## ⚠️ Common Mistakes

| ভুল | কী ঘটে | সমাধান |
|---|---|---|
| Route এর path এ `/` ভুলে যাওয়া (`'health'`) | Express মেলাতে পারে না, সবসময় 404 | সবসময় `/` দিয়ে শুরু |
| `res` পাঠাতে ভুলে যাওয়া | Postman অনন্তকাল ঘুরতে থাকে | প্রতিটা পথে একটা `res` নিশ্চিত করো |
| দুইবার `res` পাঠানো | `Cannot set headers after they are sent to the client` | `res` পাঠানোর পর `return` দাও |
| `app.listen()` এর **নিচে** route লেখা | আসলে কাজ করে (JS আগে পুরো ফাইল পড়ে), কিন্তু পড়তে বিভ্রান্তিকর | route আগে, listen সবার শেষে |
| Route বদলে Postman এ পুরনো ফল | nodemon restart হয়নি | Terminal এ `[nodemon] restarting` দেখো |
| `/api/ping` লিখতে গিয়ে `/api/Ping` | 404 — path case-sensitive | ছোট হাতের অক্ষর, hyphen ব্যবহার করো |

---

## 🏋️ Practice

**১.** ভাবো: নিচের দুটো route থাকলে `GET /api/notes/5` কোনটায় যাবে?

```js
app.get('/api/notes/:id', handlerA);
app.get('/api/notes/5', handlerB);
```

<details>
<summary>উত্তর</summary>

`handlerA` চলবে — কারণ Express **উপর থেকে নিচে** মেলায়, প্রথম মিল পেলেই থেমে যায়। `:id` একটা wildcard, `5` কেও ধরে ফেলে।

শিক্ষা: **নির্দিষ্ট route সবসময় wildcard route এর উপরে লিখতে হয়।** এই ভুলটা Lesson 13 এ আবার সামনে আসবে।
</details>

**২.** ভাবো: `res.status(201).json({...})` আর `res.status(200).json({...})` — Postman এ চোখে কী পার্থক্য দেখবে, আর Flutter এ কী পার্থক্য হবে?

<details>
<summary>উত্তর</summary>

Postman এ উপরে সবুজ লেখাটা বদলাবে (`201 Created` vs `200 OK`), body একই থাকবে।

Flutter এ পার্থক্য বড় — যদি তুমি `if (res.statusCode == 200)` লিখে থাকো, তাহলে 201 পেলে তোমার সফল-কেসটা চলবেই না। তাই বাস্তবে `if (res.statusCode >= 200 && res.statusCode < 300)` লেখা হয়।

শিক্ষা: status code শুধু সাজসজ্জা নয় — ক্লায়েন্টের কোড ওটার উপর সিদ্ধান্ত নেয়।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-05" name="lesson-05"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🐘 Lesson 05 — PostgreSQL Connect
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■□□□□□□□□□□□□□□□□□]  5/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 04 (API কাজ করছে) |
| **এই ধাপ শেষে** | Node থেকে PostgreSQL এ query চলবে |
| **নতুন শব্দ** | driver, Connection Pool, Promise, async/await, module.exports |

---

## 🎯 Goal

Node.js কে PostgreSQL এর সাথে যুক্ত করব। একটা test route বানাব যেটা database কে জিজ্ঞেস করবে "এখন কয়টা বাজে?" আর উত্তরটা Postman এ দেখাবে।

এটাই কোর্সের সবচেয়ে গুরুত্বপূর্ণ lesson — কারণ এখানেই backend আসলে backend হয়।

---

## 🧠 আগে বুঝে নাও — Database একটা আলাদা প্রোগ্রাম

সবচেয়ে বড় ভুল ধারণা: "database মানে একটা ফাইল"। না।

```
তোমার কম্পিউটারে দুটো আলাদা প্রোগ্রাম চলছে:

┌──────────────────────┐         ┌──────────────────────┐
│   Node.js Server     │         │   PostgreSQL Server  │
│   port 5000          │◄───────►│   port 5432          │
│                      │  TCP    │                      │
│   তোমার লেখা কোড      │ নেটওয়ার্ক│  ডেটা ধরে রাখে       │
└──────────────────────┘         └──────────────────────┘
```

দুটো **আলাদা প্রক্রিয়া (process)**, নিজেদের মধ্যে নেটওয়ার্ক দিয়ে কথা বলে — ঠিক যেভাবে Flutter app তোমার server এর সাথে কথা বলে। শুধু ভাষাটা HTTP নয়, PostgreSQL এর নিজস্ব wire protocol, আর বার্তাগুলো SQL।

তাই তিনটা জিনিস আলাদা:

| জিনিস | কী |
|---|---|
| **PostgreSQL server** | চলমান প্রোগ্রাম, port 5432 এ শোনে |
| **Database** | ওই server এর ভিতরে একটা নামের বাক্স (`noteapp`) |
| **Table** | ওই বাক্সের ভিতরে একটা টেবিল (`users`) |

---

## 🛠️ ধাপ ১ — PostgreSQL ইনস্টল ও database বানাও

**macOS:**
```bash
brew install postgresql@16
brew services start postgresql@16
```

**Ubuntu:**
```bash
sudo apt install postgresql
sudo systemctl start postgresql
```

**Windows:** [postgresql.org/download](https://www.postgresql.org/download/windows/) থেকে installer, সাথে pgAdmin পাবে।

**চলছে কিনা যাচাই করো:**
```bash
psql --version
```

**Database বানাও:**
```bash
psql postgres
```

ভিতরে ঢুকে (`postgres=#` prompt আসবে):

```sql
CREATE DATABASE noteapp;
\l
\q
```

| কমান্ড | কাজ |
|---|---|
| `psql postgres` | PostgreSQL এর টার্মিনাল ক্লায়েন্টে ঢোকা |
| `CREATE DATABASE noteapp;` | নতুন database বানানো (**semicolon বাধ্যতামূলক**) |
| `\l` | সব database এর তালিকা |
| `\q` | বেরিয়ে আসা |

> `\` দিয়ে শুরু কমান্ডগুলো psql এর নিজের, SQL নয় — তাই semicolon লাগে না।

---

## 💻 Code

### ফাইল ১ — `.env` (নতুন লাইন যোগ)

```env
PORT=5000
NODE_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=তোমার_পাসওয়ার্ড
DB_NAME=noteapp
```

> macOS এ brew দিয়ে ইনস্টল করলে `DB_USER` সাধারণত তোমার নিজের mac username হয়, আর password খালি থাকে। `psql postgres` এ ঢুকে `\conninfo` লিখলে বলে দেবে কোন user দিয়ে ঢুকেছ।

### ফাইল ২ — `src/config/db.js` (নতুন ফোল্ডার + ফাইল)

```js
const { Pool } = require('pg');

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,

  max: 10,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
});

pool.on('error', (err) => {
  console.error('❌ Unexpected DB pool error:', err);
});

const query = (text, params) => pool.query(text, params);

module.exports = { pool, query };
```

### ফাইল ৩ — `server.js` (test route যোগ)

```js
require('dotenv').config();

const express = require('express');
const { query } = require('./src/config/db');   // 👉 নতুন

const app = express();
const PORT = process.env.PORT || 5000;

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', uptime: process.uptime() });
});

// 👉 নতুন — DB সত্যিই কথা বলে কিনা পরীক্ষা
app.get('/api/db-test', async (req, res) => {
  try {
    const result = await query('SELECT NOW() AS server_time');

    res.status(200).json({
      success: true,
      dbTime: result.rows[0].server_time,
    });
  } catch (error) {
    console.error('DB test failed:', error.message);
    res.status(500).json({
      success: false,
      message: 'Database connection failed',
    });
  }
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

### ইনস্টল করো

```bash
npm install pg
```

> **pg কী?** PostgreSQL এর Node **driver** (ড্রাইভার) — অনুবাদক। তোমার লেখা JavaScript কে PostgreSQL এর নিজস্ব ভাষায় বদলে দেয়, আর ফেরত আসা উত্তরকে আবার JavaScript object বানায়।

---

## 🔍 লাইন-বাই-লাইন

### `const { Pool } = require('pg');`

**`{ }` দিয়ে ঘেরা কেন?** এটা **destructuring** (ডিস্ট্রাকচারিং) — একটা object থেকে নির্দিষ্ট জিনিস টেনে বের করা।

```js
// pg package টা এরকম একটা object দেয়:
//   { Pool: ..., Client: ..., types: ... }

const pg = require('pg');
const Pool = pg.Pool;        // লম্বা পথ

const { Pool } = require('pg');   // ছোট পথ — একই জিনিস
```

Dart এ `final (a, b) = record;` বা `show` clause এর সাথে মিল আছে।

| মুছলে | `Pool is not defined` — পরের লাইনেই ক্র্যাশ |

---

### Connection Pool — এটা কোর্সের সবচেয়ে বড় ধারণাগুলোর একটা

**সমস্যাটা আগে দেখো।** Database এ একটা connection খুলতে সময় লাগে — TCP handshake, ব্যবহারকারী যাচাই, session তৈরি। প্রায় **২০-৫০ মিলিসেকেন্ড**।

```
প্রতি request এ নতুন connection খুললে:

Request আসে  →  connection খোলো (৩০ms)  →  query চালাও (২ms)
             →  connection বন্ধ করো (৫ms)
             মোট: ৩৭ms, যার মধ্যে আসল কাজ মাত্র ২ms

১০০ request/সেকেন্ড হলে → ১০০ বার এই অপচয়
আর PostgreSQL এর ডিফল্ট সীমা ১০০ connection — শেষ হয়ে গেলে সব বন্ধ
```

**সমাধান — Pool (পুল)।** আগে থেকে কয়েকটা connection খুলে রাখো, request এলে ধার দাও, কাজ শেষে ফেরত নাও।

```
                    ┌─────────── Pool (max: 10) ───────────┐
                    │                                       │
Request A ─────────▶│  🔌 conn-1  (A ব্যবহার করছে)          │
Request B ─────────▶│  🔌 conn-2  (B ব্যবহার করছে)          │
                    │  🔌 conn-3  (খালি, অপেক্ষায়)          │
Request C ─────────▶│  🔌 conn-4  (C ব্যবহার করছে)          │
                    │  ...                                  │
                    │  🔌 conn-10 (খালি)                    │
Request K ──⏳──────▶│  সব ব্যস্ত → K লাইনে দাঁড়ায়            │
                    └───────────────────────────────────────┘

A এর কাজ শেষ → conn-1 ফেরত আসে → K পেয়ে যায়
```

Flutter এর সাথে মিলিয়ে: এটা অনেকটা `http.Client()` একবার বানিয়ে বারবার ব্যবহার করার মতো — প্রতিবার নতুন client না বানানো।

### Pool এর প্রতিটা option

| Option | মান | কী করে | ভুল দিলে কী হবে |
|---|---|---|---|
| `host` | `localhost` | DB কোন মেশিনে | ভুল হলে `ECONNREFUSED` |
| `port` | `5432` | কোন port এ | ভুল হলে `ECONNREFUSED` |
| `user` | `postgres` | কোন ব্যবহারকারী | ভুল হলে `password authentication failed` |
| `password` | `.env` থেকে | পাসওয়ার্ড | ভুল হলে একই error |
| `database` | `noteapp` | কোন database | ভুল হলে `database "x" does not exist` |
| `max: 10` | সর্বোচ্চ connection | একসাথে কয়টা খোলা থাকবে | খুব বেশি (যেমন 200) দিলে PostgreSQL এর সীমা ছাড়িয়ে সব fail করবে |
| `idleTimeoutMillis: 30000` | ৩০ সেকেন্ড | খালি connection কতক্ষণ ধরে রাখবে | না দিলে অকারণে connection দখল হয়ে থাকবে |
| `connectionTimeoutMillis: 5000` | ৫ সেকেন্ড | connection পেতে কতক্ষণ অপেক্ষা করবে | না দিলে DB ডাউন থাকলে request **অনন্তকাল** ঝুলে থাকবে |

> **`max` কত হওয়া উচিত?** সহজ নিয়ম: PostgreSQL এর সীমা ১০০। তোমার যদি ৪টা server instance চলে, প্রতিটার `max: 10` মানে ৪০ — নিরাপদ। ছোট প্রজেক্টে ১০ যথেষ্ট।

---

### `pool.on('error', ...)`

```js
pool.on('error', (err) => {
  console.error('❌ Unexpected DB pool error:', err);
});
```

Pool এ **খালি পড়ে থাকা** connection এ যদি হঠাৎ সমস্যা হয় (DB restart হলো, নেটওয়ার্ক কাটল), তখন এটা চলে।

| মুছলে কী হবে | **পুরো Node process ক্র্যাশ করবে।** Node এর নিয়ম — কোনো EventEmitter এ `error` ঘটল কিন্তু কেউ শুনছে না, মানে অপ্রত্যাশিত মৃত্যু। এই ৩ লাইন না থাকলে DB একবার restart হলেই তোমার সার্ভার মরে যাবে |

---

### `const query = (text, params) => pool.query(text, params);`

একটা ছোট মোড়ক (wrapper)। কেন?

- সব ফাইলে `pool` import না করে শুধু `query` import করলেই চলে
- পরে এখানে log/timing যোগ করা যাবে এক জায়গায়:

```js
const query = async (text, params) => {
  const start = Date.now();
  const result = await pool.query(text, params);
  console.log('SQL:', text, `(${Date.now() - start}ms)`);
  return result;
};
```

---

### `module.exports = { pool, query };`

এই ফাইলের বাইরে কী কী দেখা যাবে সেটা ঠিক করে। Dart এ সব public হয় ডিফল্টে; Node এ **যা export করবে শুধু সেটাই বাইরে যাবে**।

```js
// db.js এ
module.exports = { pool, query };

// server.js এ
const { query } = require('./src/config/db');
```

| মুছলে | `require()` করলে খালি object `{}` পাবে → `query is not a function` |

---

### `async` এবং `await` — এবার এটা বুঝতেই হবে

```js
app.get('/api/db-test', async (req, res) => {
  const result = await query('SELECT NOW() AS server_time');
});
```

**সমস্যাটা কী?** Database এ query পাঠালে উত্তর সাথে সাথে আসে না — ২ থেকে ২০০ মিলিসেকেন্ড লাগে। ততক্ষণ Node কী করবে?

Node **একটা মাত্র thread** এ চলে। যদি সে DB এর উত্তরের জন্য দাঁড়িয়ে থাকে, তাহলে ওই সময়ে অন্য কোনো ব্যবহারকারীর request ধরতে পারবে না। ১০০ জন ব্যবহারকারী থাকলে সবাই আটকে যাবে।

**সমাধান:**

```
                 তুমি: "DB, সময়টা বলো তো"
Node ─────────────────────────────────────▶ PostgreSQL
  │                                              │
  │  ⚡ Node দাঁড়িয়ে থাকে না —                    │ (কাজ করছে)
  │     অন্য request গুলো সামলায়                  │
  │                                              │
  │◀─────────────────────────────────────────────┘
                 "এই নাও: 2026-07-27 10:30:00"
  │
  ▼
await এর পরের লাইন এখন চলে
```

| কীওয়ার্ড | মানে |
|---|---|
| `async` | এই ফাংশনের ভিতরে `await` ব্যবহার করা যাবে |
| `await` | "উত্তর না আসা পর্যন্ত **এই ফাংশনটা** থামিয়ে রাখো, কিন্তু বাকি সার্ভার চালু থাকুক" |

Dart এর সাথে **হুবহু** মিল:

```dart
// Dart
Future<void> load() async {
  final res = await http.get(url);
}
```
```js
// JS
async function load() {
  const res = await query('SELECT ...');
}
```

**`await` না লিখলে কী হবে?** — এটা নতুনদের সবচেয়ে বড় ফাঁদ:

```js
const result = query('SELECT NOW()');
console.log(result.rows);   // ❌ TypeError: Cannot read property 'rows' of undefined
```

কারণ `await` ছাড়া তুমি ফলাফল পাও না, পাও একটা **Promise** — "ভবিষ্যতে উত্তর দেব" লেখা একটা রসিদ। রসিদের গায়ে `rows` থাকে না।

> **Promise** = ভবিষ্যতে আসবে এমন মানের প্রতিশ্রুতি। Dart এর `Future` এর হুবহু সমান। তিনটা অবস্থা: pending (অপেক্ষমাণ) → fulfilled (সফল) / rejected (ব্যর্থ)।

| ভুল | ফল |
|---|---|
| `await` বাদ | `undefined` নিয়ে কাজ করতে গিয়ে ক্র্যাশ |
| `async` বাদ কিন্তু `await` আছে | `SyntaxError: await is only valid in async functions` |

---

### `try / catch`

```js
try {
  const result = await query('SELECT NOW() AS server_time');
  res.status(200).json({ success: true, dbTime: result.rows[0].server_time });
} catch (error) {
  console.error('DB test failed:', error.message);
  res.status(500).json({ success: false, message: 'Database connection failed' });
}
```

Database এর সাথে কথা বলার সময় হাজার কারণে ভুল হতে পারে — DB বন্ধ, পাসওয়ার্ড ভুল, টেবিল নেই, নেটওয়ার্ক গেছে।

- `try { }` — এখানে ঝুঁকিপূর্ণ কাজ
- `catch (error) { }` — ভুল হলে এখানে আসবে, প্রোগ্রাম মরবে না

| `try/catch` না থাকলে | Promise reject হবে, কেউ ধরবে না → **পুরো Node process ক্র্যাশ**। এক ব্যবহারকারীর ভুল query তে গোটা সার্ভার সবার জন্য বন্ধ। Lesson 20 এ আমরা এটা এক জায়গায় সামলানোর ব্যবস্থা করব যাতে প্রতিটা route এ try/catch লিখতে না হয় |

> **নিরাপত্তার নিয়ম:** `catch` এ `error.message` সরাসরি ক্লায়েন্টকে পাঠিও না। ওই বার্তায় টেবিলের নাম, column এর নাম, কখনো query টাই থাকে — আক্রমণকারীর জন্য মানচিত্র। Log এ পুরোটা লেখো, ক্লায়েন্টকে দাও সাধারণ বার্তা।

---

### `result.rows[0].server_time`

`pg` যা ফেরত দেয় সেটা এরকম:

```js
{
  command: 'SELECT',
  rowCount: 1,
  rows: [ { server_time: 2026-07-27T10:30:00.000Z } ],   // ← আসল ডেটা
  fields: [ { name: 'server_time', dataTypeID: 1114 } ]
}
```

| অংশ | কী |
|---|---|
| `rows` | ফলাফলের সারিগুলো — **সবসময় একটা array** |
| `rowCount` | কয়টা সারি এল (বা কয়টা বদলাল) |
| `command` | কোন ধরনের query ছিল |
| `fields` | প্রতিটা column এর তথ্য |

`rows[0]` = প্রথম সারি। **একটা মাত্র ফল আশা করলেও `rows` array-ই থাকে** — এটা মনে না রাখলে `result.server_time` লিখে `undefined` পাবে।

---

## 🔄 Internal Flow — সম্পূর্ণ পথ (Postman → PostgreSQL → Postman)

এই ছবিটা মুখস্থ করার দরকার নেই, কিন্তু বোঝা দরকার:

```
┌──────────────────────────────────────────────────────────────┐
│ ১. Postman                                                   │
│    GET http://localhost:5000/api/db-test                     │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ২. Express Router                                            │
│    path মেলে → async handler চালু                            │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৩. await query('SELECT NOW() AS server_time')                │
│    → pool কে বলে: "একটা connection দাও"                      │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৪. Pool                                                      │
│    খালি connection আছে? → হ্যাঁ, conn-3 দিল                  │
│    (না থাকলে নতুন খুলত, max এ পৌঁছালে অপেক্ষা করাত)          │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৫. pg driver                                                 │
│    SQL string কে PostgreSQL wire protocol এ বদলায়            │
│    TCP দিয়ে port 5432 এ পাঠায়                                │
└───────────────────────────┬──────────────────────────────────┘
                            │
        ⚡ এই মুহূর্তে Node অপেক্ষা করছে না —
           অন্য request থাকলে সেগুলো সামলাচ্ছে
                            ▼
╔══════════════════════════════════════════════════════════════╗
║ ৬. PostgreSQL এর ভিতরে ৪টা ধাপ                               ║
║                                                              ║
║    ক) Parser    — SQL টা ব্যাকরণ অনুযায়ী ঠিক আছে কিনা দেখে   ║
║    খ) Rewriter  — view/rule থাকলে query বদলে দেয়             ║
║    গ) Planner   — সবচেয়ে দ্রুত পথ বাছে                       ║
║                   (index ব্যবহার করব? নাকি পুরো টেবিল পড়ব?)  ║
║    ঘ) Executor  — আসল কাজটা করে, ফল বানায়                    ║
║                                                              ║
║    আমাদের SELECT NOW() এ কোনো টেবিল লাগে না —                ║
║    সার্ভারের ঘড়ি দেখে সময় ফেরত দেয়                          ║
╚═══════════════════════════┬══════════════════════════════════╝
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৭. ফলাফল TCP দিয়ে ফেরত আসে (binary আকারে)                    │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৮. pg driver অনুবাদ করে JavaScript object বানায়              │
│    PostgreSQL timestamp → JS Date object                     │
│    { rows: [ { server_time: Date } ], rowCount: 1 }          │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৯. connection pool এ ফেরত যায় (বন্ধ হয় না!)                  │
│    Event Loop আমাদের await করা ফাংশনটা আবার চালু করে         │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ১০. res.status(200).json({ success: true, dbTime: ... })     │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ১১. Postman এ JSON দেখা যায়                                  │
└──────────────────────────────────────────────────────────────┘
```

সংক্ষেপে, যেটা তুমি চেয়েছিলে:

```
Postman
   ↓
Express Server
   ↓
Route
   ↓
Controller (এখানে handler)
   ↓
Database Query (pg → pool)
   ↓
PostgreSQL (parse → plan → execute)
   ↓
Query Result (rows)
   ↓
Controller
   ↓
JSON Response
   ↓
Postman
```

---

## 🗄️ PostgreSQL — এই query তে কী ঘটল

```sql
SELECT NOW() AS server_time;
```

| অংশ | মানে |
|---|---|
| `SELECT` | "আমাকে দাও" |
| `NOW()` | PostgreSQL এর built-in ফাংশন — বর্তমান সময় |
| `AS server_time` | ফলাফলের column এর নাম বদলে দাও (alias) |

**`AS` না লিখলে?** column এর নাম হতো `now`, তখন কোডে লিখতে হতো `result.rows[0].now`। কাজ করত, কিন্তু পড়তে অস্পষ্ট।

**PostgreSQL ভিতরে যা করল:** কোনো টেবিল স্পর্শ করেনি, কোনো disk পড়েনি। শুধু সার্ভারের ঘড়ি দেখে একটা সারি একটা column বানিয়ে ফেরত দিয়েছে। তাই এটা connection পরীক্ষার আদর্শ query — সবচেয়ে সস্তা।

---

## 🧪 Postman Testing

```
Method : GET
URL    : http://localhost:5000/api/db-test
```

**সফল হলে (200):**

```json
{
  "success": true,
  "dbTime": "2026-07-27T10:30:00.123Z"
}
```

**এই একটা response তিনটা জিনিস প্রমাণ করে:**
1. Node সার্ভার চলছে
2. PostgreSQL চলছে
3. দুজন একে অপরের সাথে কথা বলতে পারছে

**ব্যর্থ হলে (500):**

```json
{
  "success": false,
  "message": "Database connection failed"
}
```

তখন **terminal দেখো** — আসল কারণ ওখানে লেখা আছে।

---

## ⚠️ Common Mistakes

| Error বার্তা | আসল কারণ | সমাধান |
|---|---|---|
| `ECONNREFUSED 127.0.0.1:5432` | PostgreSQL চলছে না | `brew services start postgresql@16` |
| `password authentication failed for user "postgres"` | `.env` এ ভুল user/password | `psql postgres` এ ঢুকে `\conninfo` দেখে ঠিক নাম বসাও |
| `database "noteapp" does not exist` | Database বানানো হয়নি | `CREATE DATABASE noteapp;` |
| `Cannot find module 'pg'` | ইনস্টল হয়নি | `npm install pg` |
| `Cannot find module './src/config/db'` | path ভুল বা ফাইল অন্য জায়গায় | relative path `./` দিয়ে শুরু হতেই হবে |
| `client password must be a string` | `.env` এ password এর ঘর খালি | খালি রাখলে ওই লাইনটাই মুছে দাও |
| `TypeError: Cannot read properties of undefined (reading 'rows')` | `await` লিখতে ভুলে গেছ | `await query(...)` |
| Request অনন্তকাল ঝুলে থাকে | `connectionTimeoutMillis` দাওনি আর DB ডাউন | option টা যোগ করো |
| `.env` এ password এ `#` আছে | dotenv `#` এর পর সব বাদ দেয় | quote এ মুড়ে দাও: `DB_PASSWORD="ab#cd"` |

---

## 🏋️ Practice

**১.** `db.js` এ `max: 10` কে `max: 1` করে দাও। তারপর Postman এ দ্রুত ৫ বার `/api/db-test` চালাও। কী পার্থক্য মনে হয়?

<details>
<summary>উত্তর</summary>

আমাদের query এত দ্রুত যে চোখে পার্থক্য বোঝা যাবে না। কিন্তু ভিতরে যা ঘটছে — একটা মাত্র connection, তাই request গুলো লাইনে দাঁড়িয়ে একের পর এক চলছে, সমান্তরালে নয়।

আসল প্রজেক্টে query যদি ৫০ms লাগে, তাহলে `max: 1` মানে সেকেন্ডে সর্বোচ্চ ২০টা request — বাকি সবাই অপেক্ষায়। এভাবেই pool size একটা performance এর সিদ্ধান্ত হয়ে দাঁড়ায়।
</details>

**২.** ভাবো: `SELECT NOW()` এর বদলে `SELECT * FROM users` লিখলে এখন কী হবে?

<details>
<summary>উত্তর</summary>

`relation "users" does not exist` error আসবে — কারণ আমরা এখনো কোনো টেবিল বানাইনি। Database আছে, কিন্তু ভিতরটা খালি।

ঠিক সেই কাজটাই পরের lesson এ।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-06" name="lesson-06"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗃️ Lesson 06 — users টেবিল তৈরি
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■□□□□□□□□□□□□□□□□]  6/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 05 (DB connect হয়েছে) |
| **এই ধাপ শেষে** | `users` টেবিল তৈরি থাকবে |
| **নতুন শব্দ** | table, column, data type, PRIMARY KEY, SERIAL, UNIQUE, index, migration |

---

## 🎯 Goal

ব্যবহারকারীদের তথ্য রাখার টেবিল বানাব। এবং বুঝব — প্রতিটা column এর ধরন কেন ওইটাই বেছে নিলাম।

---

## 🧠 Table জিনিসটা কী

Relational database এ ডেটা থাকে টেবিল আকারে — Excel শিটের মতো:

```
                    ↓ column (কলাম / field)
        ┌──────┬──────────────────┬─────────────┬────────────────────┐
        │  id  │      email       │    name     │     created_at     │
        ├──────┼──────────────────┼─────────────┼────────────────────┤
row →   │  1   │ yousuf@mail.com  │   Yousuf    │ 2026-07-27 10:00   │
        │  2   │ rana@mail.com    │   Rana      │ 2026-07-27 10:05   │
        └──────┴──────────────────┴─────────────┴────────────────────┘
```

| শব্দ | মানে | Flutter এর সাথে মিল |
|---|---|---|
| Table | একই ধরনের অনেক রেকর্ডের সংগ্রহ | `List<User>` |
| Column | প্রতিটা রেকর্ডের একটা বৈশিষ্ট্য | class এর field |
| Row | একটা রেকর্ড | একটা `User` object |
| Data type | ওই column এ কী ধরনের মান বসবে | Dart এর `String`, `int` |

**সবচেয়ে বড় পার্থক্য:** Dart এ তুমি চাইলে `dynamic` দিয়ে যা খুশি রাখতে পারো। PostgreSQL এ তা পারবে না — `INTEGER` column এ `"hello"` ঢোকাতে গেলে error দিয়ে আটকে দেবে। এই কড়াকড়িটাই তোমার ডেটাকে বাঁচায়।

---

## 💻 Code

### ফাইল — `src/db/migrations/001_create_users.sql`

```sql
CREATE TABLE IF NOT EXISTS users (
  id            SERIAL          PRIMARY KEY,
  name          VARCHAR(100)    NOT NULL,
  email         VARCHAR(255)    NOT NULL UNIQUE,
  password_hash TEXT            NOT NULL,
  created_at    TIMESTAMPTZ     NOT NULL DEFAULT NOW(),
  updated_at    TIMESTAMPTZ     NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
```

### চালাও

```bash
psql -d noteapp -f src/db/migrations/001_create_users.sql
```

| অংশ | মানে |
|---|---|
| `psql` | PostgreSQL এর টার্মিনাল ক্লায়েন্ট |
| `-d noteapp` | কোন database এ |
| `-f <ফাইল>` | ওই ফাইলের SQL চালাও |

Output:

```
CREATE TABLE
CREATE INDEX
```

---

## 🔍 লাইন-বাই-লাইন

### `CREATE TABLE IF NOT EXISTS users (...)`

| অংশ | মানে | বাদ দিলে |
|---|---|---|
| `CREATE TABLE` | নতুন টেবিল বানাও | — |
| `IF NOT EXISTS` | আগে থেকে থাকলে চুপচাপ ছেড়ে দাও | দ্বিতীয়বার চালালে `relation "users" already exists` error দেবে। script বারবার চালানো নিরাপদ থাকবে না |
| `users` | টেবিলের নাম, **বহুবচনে** | নিয়ম নয়, প্রথা — `users`, `notes`, `orders` |

---

### `id SERIAL PRIMARY KEY`

```sql
id  SERIAL  PRIMARY KEY
│     │          │
│     │          └── এই column দিয়ে প্রতিটা row আলাদা চেনা যাবে
│     └── স্বয়ংক্রিয় বাড়তে থাকা সংখ্যা (1, 2, 3, ...)
└── column এর নাম
```

**`SERIAL` আসলে যা করে** — এটা কোনো data type নয়, এটা একটা শর্টকাট। PostgreSQL ভিতরে এটাকে তিনটা জিনিসে ভেঙে ফেলে:

```sql
-- তুমি লিখলে:
id SERIAL PRIMARY KEY

-- PostgreSQL আসলে করে:
CREATE SEQUENCE users_id_seq;                       -- একটা গণক (counter) বানায়
id INTEGER NOT NULL DEFAULT nextval('users_id_seq') -- প্রতিবার গণক থেকে পরের সংখ্যা নেয়
ALTER TABLE users ADD PRIMARY KEY (id);
```

তাই তুমি `INSERT` এ `id` না দিলেও PostgreSQL নিজে ১, ২, ৩ বসিয়ে দেয়।

**`PRIMARY KEY` তিনটা প্রতিশ্রুতি দেয়:**
1. কখনো `NULL` হবে না
2. কখনো দুটো row এ একই মান হবে না
3. এর উপর স্বয়ংক্রিয়ভাবে একটা index তৈরি হয় (খোঁজা দ্রুত হয়)

| বাদ দিলে | কী হবে |
|---|---|
| `PRIMARY KEY` | দুটো row এ `id = 5` বসে যেতে পারে। তখন `WHERE id = 5` দিলে কোনটা আসবে? বিশৃঙ্খলা |
| `SERIAL` | প্রতিবার `INSERT` এ তোমাকে হাতে `id` দিতে হবে, আর দুই request একসাথে এলে সংঘর্ষ হবে |

> **কেন `SERIAL`, `UUID` নয়?** `SERIAL` সহজ, ছোট (৪ বাইট), পড়তে সুবিধা। অসুবিধা — বাইরের লোক `/api/notes/1` দেখে `/api/notes/2` অনুমান করতে পারে, আর মোট কতগুলো আছে আঁচ করতে পারে। বড় বা সংবেদনশীল সিস্টেমে `UUID` ব্যবহার হয়। শেখার জন্য `SERIAL` ঠিক আছে; Lesson 22 এ এই ট্রেড-অফে ফিরব।

---

### `name VARCHAR(100) NOT NULL`

| অংশ | মানে |
|---|---|
| `VARCHAR(100)` | সর্বোচ্চ ১০০ অক্ষরের লেখা |
| `NOT NULL` | খালি রাখা যাবে না |

**`VARCHAR(100)` vs `TEXT` — পার্থক্য কী?**

PostgreSQL এ performance এর দিক থেকে **কোনো পার্থক্য নেই** (MySQL এ আছে)। `VARCHAR(n)` শুধু একটা সীমা যোগ করে।

তাহলে ব্যবহার করব কেন? — **ভুল ডেটা ঠেকাতে।** কেউ যদি বাগ বা আক্রমণের কারণে ১০ লাখ অক্ষরের নাম পাঠায়, PostgreSQL নিজেই আটকে দেবে। এটা প্রতিরক্ষার শেষ স্তর।

| `NOT NULL` বাদ দিলে | নাম ছাড়াই ব্যবহারকারী তৈরি হয়ে যাবে। পরে Flutter এ `user.name.length` লিখলে null নিয়ে ক্র্যাশ |

---

### `email VARCHAR(255) NOT NULL UNIQUE`

**`UNIQUE` — এই কোর্সের সবচেয়ে গুরুত্বপূর্ণ constraint।**

দুটো row এ একই ইমেইল বসতে দেবে না। চেষ্টা করলে PostgreSQL error দেয়:

```
duplicate key value violates unique constraint "users_email_key"
```

**কোডেও তো চেক করতে পারতাম, তাহলে এটা কেন?** — কারণ কোডের চেক ফাঁকি দেওয়া যায়:

```
সময়      Request A                    Request B
─────────────────────────────────────────────────────────
t=0ms     "ইমেইল আছে কি?" → নেই
t=1ms                                  "ইমেইল আছে কি?" → নেই
t=2ms     INSERT করল ✅
t=3ms                                  INSERT করল ✅ ❌ দুটো একই ইমেইল!
```

এটাকে **race condition** (রেস কন্ডিশন) বলে। দুটো request এত কাছাকাছি এল যে দুজনেই "নেই" দেখল।

`UNIQUE` constraint থাকলে database নিজে atomically চেক করে — দ্বিতীয়টা অবশ্যই fail করবে। **শেষ রক্ষাকবচ সবসময় database এ থাকতে হয়, কোডে নয়।**

**২৫৫ কেন?** ঐতিহাসিক প্রথা (পুরনো MySQL এ index এর সীমা ছিল)। ইমেইল এর প্রকৃত সর্বোচ্চ দৈর্ঘ্য ৩২০, কিন্তু বাস্তবে ২৫৫ যথেষ্ট।

---

### `password_hash TEXT NOT NULL`

**নামটা লক্ষ্য করো — `password` নয়, `password_hash`।**

এটা ইচ্ছাকৃত। এই column এ কখনোই আসল পাসওয়ার্ড থাকবে না, থাকবে bcrypt এর তৈরি hash:

```
ব্যবহারকারী লেখে:  mySecret123
DB তে জমা হয়:      $2b$10$N9qo8uLOickgx2ZMRZoMye1J/HxQ...
```

**`TEXT` কেন, `VARCHAR(60)` নয়?** bcrypt এর hash এখন ৬০ অক্ষরের, কিন্তু ভবিষ্যতে algorithm বদলালে (argon2 এ গেলে) দৈর্ঘ্য বদলাবে। `TEXT` দিলে তখন টেবিল বদলাতে হবে না।

| এই column এ আসল পাসওয়ার্ড রাখলে | কোনোদিন DB ফাঁস হলে সব ব্যবহারকারীর পাসওয়ার্ড খোলা অবস্থায় বেরিয়ে যাবে। আর মানুষ একই পাসওয়ার্ড অন্য সাইটেও ব্যবহার করে — ক্ষতি তোমার অ্যাপের বাইরেও ছড়াবে। Lesson 08 এ এটা নিয়ে বিস্তারিত |

---

### `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`

| অংশ | মানে |
|---|---|
| `TIMESTAMPTZ` | timestamp **with time zone** — সময় + সময় অঞ্চল |
| `DEFAULT NOW()` | তুমি মান না দিলে PostgreSQL বর্তমান সময় বসাবে |

**`TIMESTAMPTZ` না নিয়ে `TIMESTAMP` নিলে কী সমস্যা?**

```
TIMESTAMP    →  "2026-07-27 10:30"  — কোন দেশের ১০:৩০? জানা নেই
TIMESTAMPTZ  →  ভিতরে UTC তে জমা থাকে, দেখানোর সময় অঞ্চল অনুযায়ী বদলায়
```

তোমার সার্ভার হয়তো আমেরিকায়, ব্যবহারকারী বাংলাদেশে। `TIMESTAMP` হলে নোট তৈরির সময় ৬ ঘণ্টা এদিক-ওদিক দেখাবে। **সবসময় `TIMESTAMPTZ` ব্যবহার করো** — এটা এমন একটা ভুল যেটা ৬ মাস পর ঠিক করা ভয়ংকর কষ্টের।

| `DEFAULT NOW()` বাদ দিলে | প্রতিটা `INSERT` এ হাতে সময় দিতে হবে। ভুলে গেলে `NOT NULL` violation error |

---

### `CREATE INDEX idx_users_email ON users(email);`

**Index (ইনডেক্স) কী?** বইয়ের পিছনের নির্ঘণ্ট।

```
Index ছাড়া — "yousuf@mail.com" খুঁজতে:
┌───────────────────────────────────────────┐
│ row 1 দেখো... মেলে না                     │
│ row 2 দেখো... মেলে না                     │
│ ...                                       │
│ row 50000 দেখো... পেলাম! ✅               │
└───────────────────────────────────────────┘
একে বলে Sequential Scan — ৫০,০০০ row = ধীর

Index সহ:
┌───────────────────────────────────────────┐
│ B-tree তে সাজানো আছে → সরাসরি লাফিয়ে যাও  │
│ ~১৭ ধাপে পেয়ে যাবে ✅                      │
└───────────────────────────────────────────┘
একে বলে Index Scan — ৫০,০০০ row = তাৎক্ষণিক
```

**Login এ প্রতিবার `WHERE email = ...` চলবে** — তাই এই index টা সরাসরি login এর গতি বাড়ায়।

> **একটা সূক্ষ্ম কথা:** `UNIQUE` লেখার কারণে PostgreSQL এমনিতেই `email` এ একটা index বানিয়ে ফেলেছে। তাই এই `CREATE INDEX` লাইনটা কার্যত অতিরিক্ত। আমি ইচ্ছা করে রেখেছি যাতে index জিনিসটা তুমি স্পষ্ট দেখতে পাও। Lesson 12 এ `notes` টেবিলে যে index বানাব, সেটা সত্যিই দরকারি হবে।

**Index এর দাম আছে:** প্রতিটা index disk জায়গা নেয়, আর প্রতিটা `INSERT`/`UPDATE` কে একটু ধীর করে (index টাও তো আপডেট করতে হয়)। তাই যেখানে খোঁজা হয় শুধু সেখানেই index।

---

## 🔄 Internal Flow — `CREATE TABLE` চালালে PostgreSQL ভিতরে যা করে

```
psql -f 001_create_users.sql
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ১. Parser — SQL এর ব্যাকরণ যাচাই                   │
│    ভুল থাকলে এখানেই থামে                           │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ২. System catalog এ লেখে (pg_class, pg_attribute)  │
│    এগুলো PostgreSQL এর নিজের টেবিল, যেখানে         │
│    সে "কী কী টেবিল আছে" তার হিসাব রাখে             │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ৩. Disk এ খালি জায়গা বরাদ্দ করে (heap file)        │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ৪. SEQUENCE বানায় (users_id_seq) — SERIAL এর জন্য  │
└────────────────────────────────────────────────────┘
        │
        ▼
┌────────────────────────────────────────────────────┐
│ ৫. Constraint নথিভুক্ত করে                         │
│    users_pkey        (PRIMARY KEY)                 │
│    users_email_key   (UNIQUE)                      │
│    সাথে দুটো B-tree index                          │
└────────────────────────────────────────────────────┘
        │
        ▼
   "CREATE TABLE" ছাপে → টেবিল প্রস্তুত
```

---

## 🗄️ যাচাই করো

```bash
psql -d noteapp
```

```sql
\dt
```
```
        List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+---------
 public | users | table | postgres
```

```sql
\d users
```
```
                              Table "public.users"
    Column     |           Type           | Nullable |      Default
---------------+--------------------------+----------+--------------------
 id            | integer                  | not null | nextval('users_id_seq')
 name          | character varying(100)   | not null |
 email         | character varying(255)   | not null |
 password_hash | text                     | not null |
 created_at    | timestamp with time zone | not null | now()
 updated_at    | timestamp with time zone | not null | now()

Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "users_email_key" UNIQUE CONSTRAINT, btree (email)
    "idx_users_email" btree (email)
```

লক্ষ্য করো — `SERIAL` লেখাটা নেই, তার জায়গায় `integer` + `nextval(...)`. এই প্রমাণটাই দেখাচ্ছে `SERIAL` আসলে শর্টকাট ছিল।

**হাতে একটা row ঢুকিয়ে দেখো:**

```sql
INSERT INTO users (name, email, password_hash)
VALUES ('Test User', 'test@mail.com', 'fake_hash_for_now');

SELECT * FROM users;
```

```
 id |   name    |     email      | password_hash     |         created_at
----+-----------+----------------+-------------------+----------------------------
  1 | Test User | test@mail.com  | fake_hash_for_now | 2026-07-27 10:30:00.123+06
```

`id` আর `created_at` তুমি দাওনি — PostgreSQL নিজে বসিয়েছে।

**এখন `UNIQUE` পরীক্ষা করো** — একই ইমেইল আবার ঢোকাও:

```sql
INSERT INTO users (name, email, password_hash)
VALUES ('আরেকজন', 'test@mail.com', 'hash2');
```
```
ERROR:  duplicate key value violates unique constraint "users_email_key"
DETAIL:  Key (email)=(test@mail.com) already exists.
```

চমৎকার — database নিজেই পাহারা দিচ্ছে। এই error টা Lesson 07 এ আমরা ধরে সুন্দর বার্তায় বদলাব।

**পরীক্ষার row মুছে ফেলো:**

```sql
DELETE FROM users WHERE email = 'test@mail.com';
```

---

## 📁 Migration নিয়ে দুটো কথা

SQL টা ফাইলে রাখলাম কেন, সরাসরি psql এ টাইপ না করে?

```
সরাসরি টাইপ করলে:
  ❌ ৩ মাস পর মনে থাকবে না টেবিল কেমন বানিয়েছিলে
  ❌ নতুন টিমমেট কীভাবে বানাবে?
  ❌ Production সার্ভারে কী চালাবে?

ফাইলে রাখলে (migration):
  ✅ git এ থাকে, ইতিহাস দেখা যায়
  ✅ যে কেউ চালিয়ে হুবহু একই DB পাবে
  ✅ ক্রম স্পষ্ট: 001, 002, 003...
```

> **Migration** = database এর গঠন বদলানোর লিখিত, ক্রমানুসারী ধাপ। বড় প্রজেক্টে এর জন্য টুল থাকে (node-pg-migrate, Knex)। আমরা সাধারণ SQL ফাইলেই রাখব — ভিতরে কী ঘটছে তা স্পষ্ট থাকবে।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| শেষে `;` না দেওয়া | psql পরের লাইনের অপেক্ষায় ঝুলে থাকে | প্রতিটা SQL বিবৃতির শেষে semicolon |
| `TIMESTAMP` ব্যবহার (TZ ছাড়া) | সময় অঞ্চলের বিভ্রাট, ঠিক করা কষ্টকর | সবসময় `TIMESTAMPTZ` |
| Column এর নাম `password` রাখা | পরে কেউ ভেবে বসবে আসল পাসওয়ার্ড রাখা যায় | `password_hash` |
| `UNIQUE` না দেওয়া | একই ইমেইলে ৫টা অ্যাকাউন্ট, login এ কোনটা? | দাও |
| বড় হাতে টেবিলের নাম (`Users`) | পরে `"Users"` লিখতে quote লাগবে | ছোট হাতের snake_case |
| `IF NOT EXISTS` বাদ | দ্বিতীয়বার চালালে script fail | দাও |
| ভুল database এ চালানো | টেবিল অন্য জায়গায় তৈরি হয় | `-d noteapp` নিশ্চিত করো |

---

## 🏋️ Practice

**১.** ভাবো: `email` column এ `UNIQUE` না দিয়ে শুধু Node কোডে "ইমেইল আগে থেকে আছে কিনা" চেক করলে কোন পরিস্থিতিতে দুটো একই ইমেইল ঢুকে যেতে পারে?

<details>
<summary>উত্তর</summary>

দুটো request প্রায় একই মুহূর্তে এলে। দুজনেই চেক করে "নেই" দেখল, তারপর দুজনেই INSERT করল — race condition।

বাস্তবে এটা ঘটে যখন ব্যবহারকারী "Sign Up" বোতামে দুইবার দ্রুত চাপ দেয়, বা মোবাইল নেটওয়ার্কে request retry হয়।

**নিয়ম: validation কোডে রাখো ভালো বার্তা দেওয়ার জন্য, কিন্তু আসল নিশ্চয়তা সবসময় database এ constraint দিয়ে দাও।**
</details>

**২.** ভাবো: `updated_at` column টা `DEFAULT NOW()` দিয়ে বানালাম। ব্যবহারকারী নাম বদলালে এটা কি নিজে থেকে আপডেট হবে?

<details>
<summary>উত্তর</summary>

না। `DEFAULT` কেবল `INSERT` এর সময় কাজ করে, `UPDATE` এর সময় নয়।

দুটো উপায় আছে:
1. প্রতিটা `UPDATE` query তে হাতে লেখা: `SET name = $1, updated_at = NOW()` ← আমরা এটাই করব
2. PostgreSQL এ trigger বসানো, যেটা প্রতিটা UPDATE এ নিজে সময় বসাবে

Lesson 14 এ প্রথম পদ্ধতিটা দেখবে।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-07" name="lesson-07"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✍️ Lesson 07 — Register API
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■□□□□□□□□□□□□□□□]  7/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 06 (users টেবিল আছে) |
| **এই ধাপ শেষে** | `POST /api/auth/register` কাজ করবে, DB তে row ঢুকবে |
| **নতুন শব্দ** | express.json(), request body, INSERT, `$1` placeholder, RETURNING, Router, Controller |

> ⚠️ **এই lesson এ পাসওয়ার্ড খোলা অবস্থায় জমা হবে — ইচ্ছা করে।**
> কারণ আমি চাই তুমি নিজের চোখে database এ পাসওয়ার্ডটা পড়তে পারো, আর অস্বস্তিটা টের পাও।
> Lesson 08 এ (পরের lesson-ই) আমরা এটা ঠিক করব। **এই অবস্থায় কখনো deploy করবে না।**

---

## 🎯 Goal

Postman থেকে নাম, ইমেইল, পাসওয়ার্ড পাঠাব → Node সেটা নেবে → PostgreSQL এ নতুন row ঢোকাবে → নতুন ব্যবহারকারীর তথ্য ফেরত দেবে।

সাথে project কে ফোল্ডারে ভাগ করা শুরু করব — কারণ `server.js` এ সব লিখলে ২০টা API এর পর ফাইলটা ৮০০ লাইন হয়ে যাবে।

---

## 💻 Code

### ফাইল ১ — `src/controllers/auth.controller.js` (নতুন)

```js
const { query } = require('../config/db');

const register = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
      return res.status(400).json({
        success: false,
        message: 'name, email and password are required',
      });
    }

    if (password.length < 6) {
      return res.status(400).json({
        success: false,
        message: 'Password must be at least 6 characters',
      });
    }

    const result = await query(
      `INSERT INTO users (name, email, password_hash)
       VALUES ($1, $2, $3)
       RETURNING id, name, email, created_at`,
      [name, email.toLowerCase().trim(), password]
    );

    return res.status(201).json({
      success: true,
      message: 'User registered successfully',
      data: result.rows[0],
    });
  } catch (error) {
    if (error.code === '23505') {
      return res.status(409).json({
        success: false,
        message: 'Email already registered',
      });
    }

    console.error('Register error:', error);
    return res.status(500).json({
      success: false,
      message: 'Something went wrong',
    });
  }
};

module.exports = { register };
```

### ফাইল ২ — `src/routes/auth.routes.js` (নতুন)

```js
const express = require('express');
const { register } = require('../controllers/auth.controller');

const router = express.Router();

router.post('/register', register);

module.exports = router;
```

### ফাইল ৩ — `server.js` (আপডেট)

```js
require('dotenv').config();

const express = require('express');
const authRoutes = require('./src/routes/auth.routes');   // 👉 নতুন

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());                                  // 👉 নতুন — সবচেয়ে জরুরি লাইন

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', uptime: process.uptime() });
});

app.use('/api/auth', authRoutes);                         // 👉 নতুন

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

### এখন folder এর অবস্থা

```
note-app-backend/
├── src/
│   ├── config/
│   │   └── db.js
│   ├── controllers/
│   │   └── auth.controller.js     👈 নতুন — কাজটা করে
│   ├── routes/
│   │   └── auth.routes.js         👈 নতুন — পথ দেখায়
│   └── db/migrations/
│       └── 001_create_users.sql
├── server.js
├── .env
└── package.json
```

---

## 🤔 Route আর Controller আলাদা কেন?

```
Route       →  "কোন URL এ কোন ফাংশন চলবে"      (মানচিত্র)
Controller  →  "সেই ফাংশনটা আসলে কী করবে"      (কাজ)
```

একটা রেস্তোরাঁর সাথে মিলিয়ে:

```
Route      = মেনু কার্ড    ("বিরিয়ানি চাইলে রান্নাঘরে যাবে")
Controller = রাঁধুনি      (সত্যিই রান্না করে)
```

এখন ১টা API তে এই ভাগটা বাড়াবাড়ি মনে হচ্ছে। ২০টা API হলে বুঝবে — route ফাইল দেখেই এক নজরে পুরো API তালিকা পড়া যায়, কোনো কোড না ঘেঁটে।

---

## 🔍 লাইন-বাই-লাইন

### `app.use(express.json())` — এই লাইনটা না থাকলে কিছুই কাজ করবে না

```js
app.use(express.json());
```

**সমস্যাটা কী?** নেটওয়ার্ক দিয়ে ডেটা আসে **কাঁচা বাইট** হিসেবে, টুকরো টুকরো করে:

```
তারে যা আসে:
  {"name":"Yousuf","email":"y@mail.com","password":"secret123"}
  ↑ এটা একটা লম্বা string, JavaScript object নয়
```

`express.json()` একটা **middleware** — প্রতিটা request এর উপর দিয়ে যায় আর এই কাজগুলো করে:

```
১. Header দেখে: Content-Type কি application/json?
       │
       ├── না  → কিছু না করে ছেড়ে দেয়, req.body হয় undefined
       │
       └── হ্যাঁ ↓
২. সব টুকরো জোড়া লাগিয়ে পুরো string বানায়
       ↓
৩. JSON.parse() করে JavaScript object বানায়
       ↓
৪. req.body তে বসিয়ে দেয়
       ↓
৫. next() ডেকে পরের ধাপে পাঠায়
```

| এই লাইনটা মুছলে | **`req.body` হবে `undefined`।** তারপর `const { name } = req.body` লাইনে ক্র্যাশ: `Cannot destructure property 'name' of 'undefined'`। প্রতিটা POST API ভাঙবে |
| লাইনটা route এর **নিচে** লিখলে | একই সমস্যা — Express উপর থেকে নিচে চালায়, route আগে চললে ততক্ষণে body parse হয়নি |

> **`app.use()` কী?** "প্রতিটা request এ এটা চালাও" — path না দিলে সব request এ, path দিলে ওই path এর সব request এ।

---

### `const { name, email, password } = req.body;`

Destructuring — object থেকে তিনটা জিনিস টেনে বের করা।

```js
// লম্বা পথ:
const name = req.body.name;
const email = req.body.email;
const password = req.body.password;

// ছোট পথ (একই কাজ):
const { name, email, password } = req.body;
```

Postman থেকে যা পাঠানো হয়েছিল, সেটাই এখন এখানে:

```
Postman body                    req.body (Node এর ভিতরে)
─────────────────────           ────────────────────────
{                               {
  "name": "Yousuf",       →       name: 'Yousuf',
  "email": "y@mail.com",  →       email: 'y@mail.com',
  "password": "secret123" →       password: 'secret123'
}                               }
```

---

### Validation ব্লক

```js
if (!name || !email || !password) {
  return res.status(400).json({ success: false, message: '...' });
}
```

| অংশ | মানে |
|---|---|
| `!name` | name যদি খালি/undefined/`""` হয় |
| `\|\|` | অথবা |
| `return` | **সবচেয়ে জরুরি শব্দ** — এখানেই ফাংশন শেষ |
| `400` | Bad Request — ক্লায়েন্টের পাঠানো ডেটা ভুল |

| `return` মুছলে | ফাংশন থামবে না, নিচের `INSERT` ও চলবে। তারপর দ্বিতীয়বার `res` পাঠাতে গিয়ে: `Cannot set headers after they are sent to the client`। এটা নতুনদের #১ ভুল |

**কেন validation দরকার?** `name` না দিলে DB এর `NOT NULL` ধরে ফেলত ঠিকই, কিন্তু তখন ক্লায়েন্ট পেত 500 error আর দুর্বোধ্য বার্তা। আগে ধরে ফেললে পরিষ্কার 400 আর বোধগম্য বার্তা দেওয়া যায়।

> এখন হাতে লিখছি। Lesson 20 এ এটা আরও গোছানো হবে; বড় প্রজেক্টে `zod` বা `joi` লাইব্রেরি ব্যবহার হয়।

---

### `email.toLowerCase().trim()`

```js
[name, email.toLowerCase().trim(), password]
```

| Method | কী করে | না দিলে |
|---|---|---|
| `.toLowerCase()` | সব ছোট হাতের অক্ষর | `Yousuf@mail.com` আর `yousuf@mail.com` — দুটো আলাদা অ্যাকাউন্ট হয়ে যাবে, `UNIQUE` ও ঠেকাতে পারবে না |
| `.trim()` | সামনে-পিছনে space মুছে দেয় | `" y@mail.com"` জমা হবে, পরে login এ কিছুতেই মিলবে না |

মোবাইল কীবোর্ড প্রায়ই প্রথম অক্ষর বড় হাতে করে দেয় আর শেষে space যোগ করে — এই দুই লাইন বাস্তবে অসংখ্য support ticket বাঁচায়।

---

### SQL — এবার আসল অংশ

```js
const result = await query(
  `INSERT INTO users (name, email, password_hash)
   VALUES ($1, $2, $3)
   RETURNING id, name, email, created_at`,
  [name, email.toLowerCase().trim(), password]
);
```

#### `INSERT INTO users (name, email, password_hash)`

কোন টেবিলে, কোন কোন column এ বসাব। এখানে `id`, `created_at`, `updated_at` লিখিনি — কারণ PostgreSQL নিজে বসাবে (`SERIAL` আর `DEFAULT NOW()` মনে আছে?)।

#### `VALUES ($1, $2, $3)` — **এই অংশটা সবচেয়ে গুরুত্বপূর্ণ**

`$1, $2, $3` হলো **placeholder** (স্থানধারক)। আসল মান আসে দ্বিতীয় প্যারামিটারের array থেকে:

```
$1  ←  array এর ১ম উপাদান  ←  name
$2  ←  array এর ২য় উপাদান  ←  email
$3  ←  array এর ৩য় উপাদান  ←  password
```

**কেন সরাসরি string জোড়া দিলাম না?** কারণ তাহলে **SQL Injection** হয়।

```js
// ❌ কখনো এভাবে লিখবে না:
await query(`INSERT INTO users (name) VALUES ('${name}')`);
```

কেউ যদি `name` হিসেবে পাঠায়:

```
'); DROP TABLE users; --
```

তাহলে চূড়ান্ত query দাঁড়ায়:

```sql
INSERT INTO users (name) VALUES (''); DROP TABLE users; --')
```

**তোমার পুরো users টেবিল মুছে যাবে।**

**`$1` কীভাবে বাঁচায়?** pg driver query আর data **আলাদা করে** PostgreSQL এ পাঠায়:

```
Node ──── "INSERT INTO users (name) VALUES ($1)" ────▶ PostgreSQL
                                                       │ প্রথমে query টা
                                                       │ parse করে ফেলে,
                                                       │ কাঠামো ঠিক হয়ে যায়
Node ──── ["'); DROP TABLE users; --"] ──────────────▶ │
                                                       │ এখন এটা কেবল
                                                       │ একটা text মান
                                                       ▼
                                        নাম হিসেবে ওই অদ্ভুত লেখাটাই জমা হয়
                                        কোনো ক্ষতি হয় না ✅
```

কাঠামো আগে ঠিক হয়ে যায়, তাই ডেটা কখনো কমান্ড হয়ে উঠতে পারে না। একে বলে **parameterized query** বা **prepared statement**।

> **নিয়ম, ব্যতিক্রমহীন: ব্যবহারকারীর দেওয়া কোনো মান কখনো SQL string এ জোড়া দেবে না। সবসময় `$1, $2` ব্যবহার করবে।**

#### `RETURNING id, name, email, created_at`

এটা PostgreSQL এর দারুণ একটা সুবিধা — `INSERT` করার পর সদ্য তৈরি row এর কিছু column ফেরত দাও।

```
RETURNING ছাড়া:                    RETURNING সহ:
─────────────────                   ──────────────
1. INSERT চালাও                     1. INSERT চালাও, একই সাথে ফল নাও
2. আবার SELECT চালিয়ে              ✅ এক চক্করেই কাজ শেষ
   নতুন row টা আনো
❌ দুইবার DB তে যাওয়া
```

**`password_hash` কেন `RETURNING` এ নেই?** কারণ পাসওয়ার্ড কখনো response এ ফেরত দিতে নেই — লগে জমা হতে পারে, ব্রাউজার cache এ থেকে যেতে পারে।

> **নিয়ম: কোনো API যেন কখনো password বা password_hash ফেরত না দেয়।** `SELECT *` এড়িয়ে চলার এটাই মূল কারণ।

---

### Error handling — `error.code === '23505'`

```js
if (error.code === '23505') {
  return res.status(409).json({ success: false, message: 'Email already registered' });
}
```

`23505` হলো PostgreSQL এর **unique_violation** error code — অর্থাৎ `UNIQUE` constraint ভেঙেছে।

কাজে লাগে এমন কিছু কোড:

| Code | নাম | কখন |
|---|---|---|
| `23505` | unique_violation | ইমেইল আগেই আছে |
| `23503` | foreign_key_violation | যে user নেই তার নোট বানাতে চাইছ (Lesson 12) |
| `23502` | not_null_violation | NOT NULL column খালি |
| `22P02` | invalid_text_representation | `/api/notes/abc` — id তে অক্ষর |
| `42P01` | undefined_table | টেবিল নেই |

**409 কেন, 400 নয়?** 400 = "তোমার পাঠানো ডেটার গঠন ভুল"। 409 Conflict = "ডেটা ঠিকই আছে, কিন্তু বর্তমান অবস্থার সাথে সংঘর্ষ করছে"। ইমেইল আগে থেকে থাকা ঠিক তাই।

| এই চেক না থাকলে | ব্যবহারকারী পেত 500 Internal Server Error — যেন সার্ভার ভেঙে গেছে। অথচ দোষটা তার, আর সমাধানও তার হাতে |

---

## 🔄 Internal Flow — সম্পূর্ণ পথ

```
┌─────────────────────────────────────────────────────────────┐
│ ১. Postman                                                  │
│    POST http://localhost:5000/api/auth/register             │
│    Content-Type: application/json                           │
│    Body: {"name":"Yousuf","email":"y@mail.com",             │
│           "password":"secret123"}                           │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ২. express.json() middleware                                │
│    কাঁচা বাইট → JSON.parse() → req.body তে object           │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ৩. app.use('/api/auth', authRoutes)                         │
│    path শুরু হয় /api/auth দিয়ে? হ্যাঁ                       │
│    বাকি অংশ '/register' নিয়ে authRoutes এ পাঠায়             │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ৪. router.post('/register', register)                       │
│    method POST ✅  path মেলে ✅ → controller ডাকো            │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ৫. Controller                                               │
│    • req.body থেকে তিনটা মান নিল                            │
│    • validation পাস করল                                     │
│    • email ছোট হাতে + trim করল                              │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ৬. await query(sql, values)                                 │
│    pool থেকে connection নিল → pg driver এ গেল               │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
╔═════════════════════════════════════════════════════════════╗
║ ৭. PostgreSQL এর ভিতরে                                      ║
║                                                             ║
║    ক) Parse   — "INSERT INTO users ... VALUES ($1,$2,$3)"   ║
║                 কাঠামো ঠিক হয়ে গেল                          ║
║    খ) Bind    — এখন মানগুলো বসাও (নিরাপদে, text হিসেবে)      ║
║    গ) Plan    — INSERT, সোজা কাজ                            ║
║    ঘ) Execute —                                             ║
║         • users_id_seq থেকে পরের সংখ্যা নিল → id = 1        ║
║         • created_at, updated_at এ NOW() বসাল               ║
║         • email এর UNIQUE index চেক করল → খালি ✅            ║
║         • disk এ নতুন row লিখল                              ║
║         • WAL (write-ahead log) এ লিখল — বিদ্যুৎ গেলেও      ║
║           ডেটা হারাবে না                                    ║
║    ঙ) RETURNING — চাওয়া column গুলো ফেরত পাঠাল              ║
╚══════════════════════════╪══════════════════════════════════╝
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ৮. pg driver → JS object                                    │
│    { rowCount: 1,                                           │
│      rows: [ { id: 1, name: 'Yousuf',                       │
│                email: 'y@mail.com',                         │
│                created_at: Date } ] }                       │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ৯. res.status(201).json({ success, message, data })         │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│ ১০. Postman এ 201 Created + JSON                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧪 Postman Testing

### Test ১ — সফল নিবন্ধন

```
Method  : POST
URL     : http://localhost:5000/api/auth/register
Headers : Content-Type: application/json
Body    : raw → JSON

{
  "name": "Yousuf Ali",
  "email": "yousuf@mail.com",
  "password": "secret123"
}
```

**Response — 201 Created:**

```json
{
  "success": true,
  "message": "User registered successfully",
  "data": {
    "id": 1,
    "name": "Yousuf Ali",
    "email": "yousuf@mail.com",
    "created_at": "2026-07-27T10:30:00.000Z"
  }
}
```

> Postman এ Body ট্যাবে **raw** বেছে ডান পাশের ড্রপডাউন থেকে **JSON** নির্বাচন করতে ভুলো না — নাহলে Content-Type ঠিক যাবে না আর `express.json()` কাজ করবে না।

### Test ২ — একই ইমেইলে আবার

একই body আবার পাঠাও। **409 Conflict:**

```json
{
  "success": false,
  "message": "Email already registered"
}
```

`UNIQUE` constraint কাজ করছে ✅

### Test ৩ — পাসওয়ার্ড ছাড়া

```json
{ "name": "Test", "email": "t@mail.com" }
```

**400 Bad Request** — validation কাজ করছে ✅

### Test ৪ — এখন database এ দেখো (এটাই আসল শিক্ষা)

```bash
psql -d noteapp -c "SELECT id, name, email, password_hash FROM users;"
```

```
 id |    name    |      email      | password_hash
----+------------+-----------------+---------------
  1 | Yousuf Ali | yousuf@mail.com | secret123
```

😱 **পাসওয়ার্ডটা খোলা অবস্থায় পড়া যাচ্ছে।**

Database এ যার প্রবেশাধিকার আছে — DBA, backup ফাইল যার হাতে পড়ল, বা কোনোদিন যে হ্যাক করে ঢুকল — সবাই সবার পাসওয়ার্ড দেখতে পাবে। আর মানুষ একই পাসওয়ার্ড Facebook, Gmail এও ব্যবহার করে।

এই অস্বস্তিটাই পরের lesson এর কারণ।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `express.json()` না লেখা | `Cannot destructure property 'name' of 'undefined'` | `app.use(express.json())` route এর **আগে** |
| Postman এ Body raw+JSON না করা | `req.body` খালি object `{}` | raw → JSON বেছে নাও |
| validation এ `return` না লেখা | `Cannot set headers after they are sent` | প্রতিটা `res.` এর আগে `return` |
| `$1` এর বদলে string জোড়া | SQL Injection — টেবিল মুছে যেতে পারে | সবসময় placeholder |
| array এর ক্রম উল্টানো | নাম এর জায়গায় ইমেইল জমা হবে, error দেবে না! | `$1,$2,$3` আর array এর ক্রম মিলিয়ে দেখো |
| `RETURNING` এ `password_hash` রাখা | পাসওয়ার্ড response এ ফাঁস | কখনো না |
| `require` path এ `../` ভুল | `Cannot find module` | controller থেকে config এ যেতে `../config/db` |
| Router এ `/api/auth/register` লেখা | path হয়ে যাবে `/api/auth/api/auth/register` | router এ শুধু `/register` |

---

## 🏋️ Practice

**১.** ভাবো: `app.use('/api/auth', authRoutes)` এ prefix টা `/api/v1/auth` করে দিলে Postman এ URL কী হবে? router ফাইলে কি কিছু বদলাতে হবে?

<details>
<summary>উত্তর</summary>

URL হবে `http://localhost:5000/api/v1/auth/register`। Router ফাইলে **কিছুই বদলাতে হবে না** — সে শুধু `/register` অংশটা জানে।

এটাই এই ভাগাভাগির সুবিধা। বাস্তবে API এর নতুন version আনার সময় (`/api/v2/...`) এই সুবিধাটা কাজে লাগে।
</details>

**২.** ভাবো: `RETURNING` লাইনটা মুছে দিলে কী হবে? `result.rows` এ তখন কী থাকবে?

<details>
<summary>উত্তর</summary>

`result.rows` হবে খালি array `[]`, আর `result.rowCount` হবে `1`।

তখন `result.rows[0]` = `undefined`, আর response এ `data: undefined` যাবে (JSON এ `data` কী-টাই অদৃশ্য হয়ে যাবে)। Flutter এ `data['id']` পড়তে গিয়ে null error।

শিক্ষা: `INSERT` নিজে থেকে কোনো সারি ফেরত দেয় না — `RETURNING` লিখলে তবেই দেয়।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-08" name="lesson-08"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 Lesson 08 — Password Hashing (bcrypt)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■□□□□□□□□□□□□□□]  8/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 07 (register কাজ করছে) |
| **এই ধাপ শেষে** | DB তে পাসওয়ার্ড আর পড়া যাবে না |
| **নতুন শব্দ** | hash, salt, cost factor, rainbow table, one-way function |

---

## 🎯 Goal

গত lesson এর নিরাপত্তা গর্তটা বন্ধ করা। পাসওয়ার্ড আর কখনো খোলা অবস্থায় জমা হবে না।

---

## 🧠 Hash জিনিসটা কী

**Hash (হ্যাশ)** = এক দিকে যাওয়া রূপান্তর। যাওয়া যায়, ফেরা যায় না।

```
   ┌──────────────┐                    ┌────────────────────────────────┐
   │  secret123   │ ──── bcrypt ────▶  │ $2b$10$N9qo8uLOickgx2ZMRZoMy... │
   └──────────────┘                    └────────────────────────────────┘
                                                     │
                    ◀───── ❌ অসম্ভব ─────────────────┘
```

**Encryption এর সাথে পার্থক্যটা বুঝে নাও — এটা খুব জরুরি:**

| | Encryption (এনক্রিপশন) | Hashing (হ্যাশিং) |
|---|---|---|
| ফেরানো যায়? | ✅ হ্যাঁ, চাবি থাকলে | ❌ না, কখনোই না |
| উদ্দেশ্য | গোপনে পাঠানো, পরে পড়া | যাচাই করা, কখনো পড়া নয় |
| উদাহরণ | WhatsApp বার্তা | পাসওয়ার্ড |

**তাহলে ফেরানো না গেলে login মিলাব কীভাবে?**

এখানেই মূল কৌশল — আমরা পাসওয়ার্ড **উদ্ধার করি না**, নতুন করে **হ্যাশ করে মিলিয়ে দেখি**:

```
নিবন্ধনের সময়:
  "secret123"  →  hash  →  "$2b$10$N9qo..."  →  DB তে জমা

লগইনের সময়:
  ব্যবহারকারী লিখল "secret123"
        ↓ একই লবণ (salt) দিয়ে আবার hash
  "$2b$10$N9qo..."
        ↓ DB এর সাথে মিলিয়ে দেখো
  মিলল? ✅ ঢুকতে দাও      মিলল না? ❌ ফিরিয়ে দাও
```

**সার্ভার কখনো আসল পাসওয়ার্ডটা জানে না — জানার দরকারও নেই।**

---

## 🧂 Salt (লবণ) — কেন লাগে

শুধু hash যথেষ্ট নয়। কারণ একই পাসওয়ার্ড সবসময় একই hash দেয়:

```
"123456"  →  SHA256  →  8d969eef6ecad3c29a3a629280e686cf...
```

আক্রমণকারীর কাছে আগে থেকেই লাখ লাখ পাসওয়ার্ডের hash এর তালিকা থাকে (**rainbow table**)। তোমার DB চুরি করে সে শুধু মিলিয়ে নেবে।

আরও খারাপ — DB দেখেই বোঝা যাবে কারা একই পাসওয়ার্ড ব্যবহার করে:

```
id | email          | password_hash
 1 | a@mail.com     | 8d969eef6eca...   ← একই
 2 | b@mail.com     | 8d969eef6eca...   ← একই  → দুজনেই "123456"
```

**Salt** হলো প্রতিটা পাসওয়ার্ডের সাথে জোড়া দেওয়া এলোমেলো একটা string:

```
"123456" + salt "xY7kP2mQ..."  →  hash  →  $2b$10$xY7kP2mQ...abc
"123456" + salt "zL9nR4tW..."  →  hash  →  $2b$10$zL9nR4tW...xyz
                                              ↑ একই পাসওয়ার্ড, ভিন্ন hash ✅
```

**Salt কোথায় রাখব?** এটাই সবচেয়ে সুন্দর অংশ — bcrypt salt টা hash এর **ভিতরেই** রেখে দেয়:

```
$2b$10$N9qo8uLOickgx2ZMRZoMye  IjZAgcfl7p92ldGxad68LJZdL17lhWy
│  │  │ └──────── salt ──────┘  └──────────── hash ───────────┘
│  │  └── cost factor (10)
│  └── bcrypt এর সংস্করণ
└── শুরুর চিহ্ন
```

তাই salt আলাদা column এ রাখতে হয় না। `bcrypt.compare()` নিজেই hash থেকে salt বের করে নেয়।

---

## ⏱️ Cost Factor — ধীর হওয়াটাই এখানে গুণ

```js
await bcrypt.hash(password, 10);
                            └── cost factor
```

Cost factor ১ বাড়লে সময় **দ্বিগুণ** হয় (2^n বার চক্র চলে):

| Cost | সময় | মন্তব্য |
|---|---|---|
| 8 | ~২৫ms | দুর্বল |
| **10** | **~১০০ms** | **এখনকার আদর্শ** |
| 12 | ~৪০০ms | বেশি নিরাপদ, ধীর |
| 14 | ~১.৬s | ব্যবহারকারী বিরক্ত হবে |

**ধীর কেন ভালো?**

```
তোমার ব্যবহারকারী:      login এ ১০০ms বেশি — টেরই পাবে না

আক্রমণকারী:            ১ কোটি পাসওয়ার্ড চেষ্টা করতে চায়
                       SHA256 হলে   → সেকেন্ডে ১০০ কোটি চেষ্টা 😱
                       bcrypt(10)   → সেকেন্ডে ১০টা চেষ্টা 🐌
                       → ১ কোটি চেষ্টায় লাগবে ১১ দিন, একটা পাসওয়ার্ডের জন্য
```

**তাই MD5/SHA256 দিয়ে পাসওয়ার্ড hash করা যায় না** — ওগুলো দ্রুত হওয়ার জন্য বানানো, আর দ্রুত মানেই আক্রমণকারীর সুবিধা। bcrypt ইচ্ছা করে ধীর।

---

## 💻 Code

### ইনস্টল

```bash
npm install bcrypt
```

> **`bcrypt` না `bcryptjs`?** `bcrypt` C++ দিয়ে লেখা, দ্রুত — কিন্তু ইনস্টলে compile করতে হয়, কিছু মেশিনে ঝামেলা করে। `bcryptjs` পুরোটা JavaScript, ইনস্টল সবসময় নির্ঝঞ্ঝাট, কিন্তু ধীর। ইনস্টলে সমস্যা হলে `bcryptjs` নাও — API হুবহু এক, শুধু `require('bcryptjs')` লিখবে।

### ফাইল — `src/controllers/auth.controller.js` (আপডেট)

```js
const bcrypt = require('bcrypt');                    // 👉 নতুন
const { query } = require('../config/db');

const SALT_ROUNDS = 10;                              // 👉 নতুন

const register = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    if (!name || !email || !password) {
      return res.status(400).json({
        success: false,
        message: 'name, email and password are required',
      });
    }

    if (password.length < 6) {
      return res.status(400).json({
        success: false,
        message: 'Password must be at least 6 characters',
      });
    }

    const passwordHash = await bcrypt.hash(password, SALT_ROUNDS);   // 👉 নতুন

    const result = await query(
      `INSERT INTO users (name, email, password_hash)
       VALUES ($1, $2, $3)
       RETURNING id, name, email, created_at`,
      [name, email.toLowerCase().trim(), passwordHash]               // 👉 password → passwordHash
    );

    return res.status(201).json({
      success: true,
      message: 'User registered successfully',
      data: result.rows[0],
    });
  } catch (error) {
    if (error.code === '23505') {
      return res.status(409).json({
        success: false,
        message: 'Email already registered',
      });
    }

    console.error('Register error:', error);
    return res.status(500).json({
      success: false,
      message: 'Something went wrong',
    });
  }
};

module.exports = { register };
```

**বদলেছে মাত্র ৩ জায়গা** — কিন্তু নিরাপত্তার দিক থেকে এটাই সবচেয়ে বড় পরিবর্তন।

---

## 🔍 লাইন-বাই-লাইন

### `const SALT_ROUNDS = 10;`

Cost factor টা আলাদা নাম দিয়ে রাখলাম।

| কেন | সংখ্যাটা কোডের মাঝে ছড়িয়ে না থাকলে ভবিষ্যতে এক জায়গায় বদলানো যায়। কোড পড়ে বোঝাও যায় ১০ টা কীসের সংখ্যা |

### `const passwordHash = await bcrypt.hash(password, SALT_ROUNDS);`

```js
await bcrypt.hash(password, SALT_ROUNDS)
  │        │         │           │
  │        │         │           └── কতটা ধীর করব
  │        │         └── আসল পাসওয়ার্ড
  │        └── hash বানাও
  └── সময় লাগে (~১০০ms), তাই await
```

ভিতরে যা ঘটে:

```
১. ক্রিপ্টোগ্রাফিকভাবে নিরাপদ এলোমেলো salt বানায় (১৬ বাইট)
২. password + salt একসাথে করে
৩. 2^10 = ১০২৪ বার Blowfish চক্র চালায়   ← এখানেই সময়টা যায়
৪. ফলাফল সাজিয়ে দেয়: $2b$10$<salt><hash>
```

| `await` না লিখলে | `passwordHash` হবে একটা Promise object। DB তে জমা হবে `"[object Promise]"` — এবং **কেউ কোনোদিন login করতে পারবে না**। কোনো error ও দেখাবে না, তাই ধরাও কঠিন |
| `bcrypt.hash` এর বদলে সরাসরি `password` | Lesson 07 এর অবস্থায় ফিরে যাবে — খোলা পাসওয়ার্ড |

> **`bcrypt.hashSync()` ও আছে — ব্যবহার করবে না।** `Sync` মানে পুরো Node thread ওই ১০০ms আটকে থাকবে, ওই সময়ে অন্য কোনো ব্যবহারকারীর কোনো request প্রক্রিয়া হবে না। ১০ জন একসাথে register করলে শেষজনকে ১ সেকেন্ড অপেক্ষা করতে হবে।

---

## 🔄 Internal Flow — hash যোগ হওয়ার পর

```
Postman
   │  { "password": "secret123" }
   ▼
express.json()  →  req.body.password = "secret123"
   │
   ▼
Controller — validation পাস
   │
   ▼
┌──────────────────────────────────────────────────┐
│ await bcrypt.hash("secret123", 10)               │
│                                                  │
│   ১. salt বানাল: "N9qo8uLOickgx2ZMRZoMye"        │
│   ২. "secret123" + salt জোড়া দিল                 │
│   ৩. ১০২৪ বার Blowfish চালাল  ⏱️ ~১০০ms          │
│   ৪. ফেরত: "$2b$10$N9qo8uLOickgx2ZMRZoMye1J..."  │
│                                                  │
│   ⚡ এই ১০০ms এ Node আটকে থাকে না —              │
│      অন্যদের request সামলায় (await এর কারণে)     │
└─────────────────────┬────────────────────────────┘
                      ▼
┌──────────────────────────────────────────────────┐
│ INSERT INTO users (..., password_hash)           │
│ VALUES ($1, $2, $3)                              │
│   $3 = "$2b$10$N9qo8uLOickgx2ZMRZoMye1J..."      │
│                                                  │
│  ⚠️ আসল "secret123" এখানে আর নেই।                │
│     মেমরিতে ছিল, request শেষে মুছে যাবে           │
└─────────────────────┬────────────────────────────┘
                      ▼
              PostgreSQL এ জমা
                      │
                      ▼
       RETURNING (password_hash ছাড়া) → 201 → Postman
```

---

## 🧪 Postman Testing

### Test ১ — নতুন ইমেইলে register করো

```json
{
  "name": "Rana",
  "email": "rana@mail.com",
  "password": "secret123"
}
```

**201 Created** — response আগের মতোই দেখাবে (পাসওয়ার্ড তো ফেরত দিই না)।

### Test ২ — এখন database এ দেখো

```bash
psql -d noteapp -c "SELECT id, email, password_hash FROM users;"
```

```
 id |      email      |                        password_hash
----+-----------------+--------------------------------------------------------------
  1 | yousuf@mail.com | secret123
  2 | rana@mail.com   | $2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy
```

উপরের row টা পুরনো (Lesson 07 এর), নিচেরটা নতুন। পার্থক্যটা স্পষ্ট।

**পুরনো row টা মুছে ফেলো** — নাহলে ওটা দিয়ে কখনো login করা যাবে না:

```sql
DELETE FROM users WHERE password_hash NOT LIKE '$2%';
```

> এই query টা বলছে: যেসব hash `$2` দিয়ে শুরু হয় না (মানে bcrypt নয়) সেগুলো মুছে দাও।

### Test ৩ — একই পাসওয়ার্ডে দুই অ্যাকাউন্ট

`a@mail.com` আর `b@mail.com` — দুটোতেই password `secret123` দিয়ে register করো।

```sql
SELECT email, password_hash FROM users;
```

```
 a@mail.com | $2b$10$xY7kP2mQ8vN3wR5tL...
 b@mail.com | $2b$10$zL9nR4tW6cM8pK2sX...
                    ↑ সম্পূর্ণ ভিন্ন!
```

একই পাসওয়ার্ড, তবু ভিন্ন hash — **salt কাজ করছে ✅**

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `await` না লেখা | DB তে `[object Promise]` জমা হয়, login চিরতরে ভাঙে | `await bcrypt.hash(...)` |
| `hashSync()` ব্যবহার | সার্ভার প্রতি hash এ ১০০ms জমে থাকে | async version |
| Cost factor খুব কম (৪) | কয়েক মিলিসেকেন্ডে ভাঙা যায় | ১০ বা ১২ |
| Cost factor খুব বেশি (১৬) | login এ ৫ সেকেন্ড, ব্যবহারকারী চলে যাবে | ১০ |
| Salt আলাদা column এ রাখা | অপ্রয়োজনীয় — bcrypt hash এর ভিতরেই রাখে | রেখো না |
| MD5/SHA256 দিয়ে পাসওয়ার্ড | খুব দ্রুত = আক্রমণে সুবিধা | bcrypt / argon2 |
| Hash কে response এ পাঠানো | ফাঁস, লগে জমা হয় | `RETURNING` এ কখনো না |
| `password.length` চেক না করা | `123` ও গ্রহণ করবে | ন্যূনতম ৬-৮ |
| Hash আগেই বানানো পুরনো row রাখা | ওই ব্যবহারকারী কখনো login করতে পারবে না | পরীক্ষার ডেটা মুছে দাও |

---

## 🏋️ Practice

**১.** একই পাসওয়ার্ড দুইবার hash করলে ফল কি এক হবে?

<details>
<summary>উত্তর</summary>

না — প্রতিবার নতুন salt তৈরি হয়, তাই ফল সবসময় ভিন্ন।

তাহলে login মিলবে কীভাবে? কারণ `bcrypt.compare()` দুটো hash তুলনা করে না — সে জমা থাকা hash থেকে **salt বের করে**, ওই salt দিয়ে নতুন পাসওয়ার্ডটা hash করে, তারপর মেলায়। পরের lesson এ এটাই দেখব।

**তাই SQL এ কখনো `WHERE password_hash = $1` লেখা যায় না।**
</details>

**২.** ভাবো: কেউ তোমার পুরো `users` টেবিল চুরি করে নিল। সে কি ব্যবহারকারীদের অ্যাকাউন্টে ঢুকতে পারবে?

<details>
<summary>উত্তর</summary>

সরাসরি না। Hash দিয়ে login করা যায় না — login এর সময় আসল পাসওয়ার্ড লাগে।

তবে সে **অফলাইনে চেষ্টা চালাতে পারে** — সাধারণ পাসওয়ার্ডের তালিকা নিয়ে একটা একটা hash করে মেলাতে। bcrypt ধীর হওয়ায় এটা অত্যন্ত ব্যয়বহুল, কিন্তু কারো পাসওয়ার্ড `123456` হলে সেটা মিনিটেই বেরিয়ে যাবে।

তাই স্তরে স্তরে প্রতিরক্ষা: bcrypt + শক্তিশালী পাসওয়ার্ডের নিয়ম + rate limiting (Lesson 22) + ফাঁস হলে সবার পাসওয়ার্ড বদলানোর ব্যবস্থা।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-09" name="lesson-09"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔑 Lesson 09 — Login API
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■□□□□□□□□□□□□□]  9/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 08 (hash কাজ করছে) |
| **এই ধাপ শেষে** | `POST /api/auth/login` — পাসওয়ার্ড যাচাই হবে |
| **নতুন শব্দ** | SELECT, WHERE, bcrypt.compare(), user enumeration |

---

## 🎯 Goal

ইমেইল-পাসওয়ার্ড নিয়ে যাচাই করব। এই lesson এ **token দেব না** — শুধু "সঠিক না ভুল" বলব। Token আসবে পরের lesson এ, যাতে দুটো ধারণা আলাদা করে বোঝা যায়।

---

## 💻 Code

### `src/controllers/auth.controller.js` এ যোগ করো

```js
const login = async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({
        success: false,
        message: 'email and password are required',
      });
    }

    const result = await query(
      `SELECT id, name, email, password_hash
       FROM users
       WHERE email = $1`,
      [email.toLowerCase().trim()]
    );

    if (result.rows.length === 0) {
      return res.status(401).json({
        success: false,
        message: 'Invalid email or password',
      });
    }

    const user = result.rows[0];

    const isMatch = await bcrypt.compare(password, user.password_hash);

    if (!isMatch) {
      return res.status(401).json({
        success: false,
        message: 'Invalid email or password',
      });
    }

    return res.status(200).json({
      success: true,
      message: 'Login successful',
      data: {
        id: user.id,
        name: user.name,
        email: user.email,
      },
    });
  } catch (error) {
    console.error('Login error:', error);
    return res.status(500).json({
      success: false,
      message: 'Something went wrong',
    });
  }
};

module.exports = { register, login };     // 👉 login যোগ করলাম
```

### `src/routes/auth.routes.js` (আপডেট)

```js
const express = require('express');
const { register, login } = require('../controllers/auth.controller');

const router = express.Router();

router.post('/register', register);
router.post('/login', login);              // 👉 নতুন

module.exports = router;
```

---

## 🔍 লাইন-বাই-লাইন

### SQL — `SELECT ... WHERE email = $1`

```sql
SELECT id, name, email, password_hash
FROM users
WHERE email = $1
```

| অংশ | মানে |
|---|---|
| `SELECT id, name, ...` | কোন কোন column চাই |
| `FROM users` | কোন টেবিল থেকে |
| `WHERE email = $1` | শুধু যে row এর email মেলে |

**`SELECT *` লিখলাম না কেন?**

```
SELECT *              →  সব column আসে, ভবিষ্যতে নতুন column যোগ হলে
                         সেটাও অজান্তে চলে আসবে (হয়তো সংবেদনশীল)
SELECT id, name, ...  →  ঠিক যা দরকার, তাই। কম ডেটা, কম ঝুঁকি
```

Production কোডে `SELECT *` প্রায় সবসময় খারাপ অভ্যাস।

**তবে `password_hash` এখানে নিতেই হবে** — কারণ পাসওয়ার্ড মেলাতে ওটা লাগবে। শুধু খেয়াল রাখতে হবে যেন response এ না যায়।

**PostgreSQL ভিতরে কী করল:**

```
১. Parse    → query ব্যাকরণ ঠিক আছে
২. Plan     → "email এ index আছে (users_email_key)
               → Sequential Scan না করে Index Scan করব"
৩. Execute  → B-tree তে email খুঁজে সরাসরি ওই row এ লাফ দিল
৪. Return   → ৪টা column সহ ০ বা ১টা row ফেরত
```

Index না থাকলে ১০ লাখ ব্যবহারকারী থাকলে ১০ লাখ row পড়তে হতো। index থাকায় ~২০ ধাপে কাজ শেষ।

---

### `if (result.rows.length === 0)`

`rows` সবসময় array। ইমেইল না মিললে array খালি।

```js
result.rows.length === 0   →  এই ইমেইলে কোনো ব্যবহারকারী নেই
```

| চেক না করলে | পরের লাইনে `result.rows[0]` = `undefined`, তারপর `user.password_hash` পড়তে গিয়ে ক্র্যাশ → 500 error |

---

### 🔒 `'Invalid email or password'` — বার্তাটা ইচ্ছা করে অস্পষ্ট

লক্ষ্য করো, **দুটো ক্ষেত্রেই একই বার্তা**:
- ইমেইল নেই → "Invalid email or password"
- পাসওয়ার্ড ভুল → "Invalid email or password"

**কেন? আলাদা বললে তো ব্যবহারকারীর সুবিধা হতো।**

```
❌ যদি আলাদা বার্তা দাও:

আক্রমণকারী চেষ্টা করে:  rakib@mail.com
সার্ভার বলে:            "Email not found"
                        → এই ইমেইল নিবন্ধিত নেই, পরেরটা দেখি

আক্রমণকারী চেষ্টা করে:  sabbir@mail.com
সার্ভার বলে:            "Wrong password"
                        → 🎯 পেয়ে গেছি! এই ইমেইল আছে।
                          এখন শুধু পাসওয়ার্ড ভাঙলেই হবে
```

একে বলে **user enumeration** (ইউজার এনিউমারেশন) — কোন ইমেইলগুলো নিবন্ধিত তার তালিকা বানিয়ে ফেলা। ওই তালিকা তখন brute-force বা phishing এ ব্যবহার হয়। ডেটিং বা স্বাস্থ্য অ্যাপে এটা আরও ভয়ানক — "এই ব্যক্তি এই সাইটে আছে" নিজেই একটা গোপন তথ্য।

| আলাদা বার্তা দিলে | ব্যবহারকারীর সামান্য সুবিধা, আক্রমণকারীর বিরাট সুবিধা। ব্যবসা-সিদ্ধান্ত হিসেবে অনেক কোম্পানি ঝুঁকিটা নেয়, কিন্তু নিরাপত্তার আদর্শ হলো একই বার্তা |

**401 কেন?**

| Code | কখন |
|---|---|
| `400` | ইমেইল ফিল্ডটাই পাঠাওনি (গঠনগত ভুল) |
| `401 Unauthorized` | পরিচয় প্রমাণ করতে ব্যর্থ ← **এটা** |
| `403 Forbidden` | পরিচয় ঠিক আছে, কিন্তু এই কাজের অনুমতি নেই |
| `404` | ❌ এখানে ব্যবহার করবে না — ইমেইল আছে কিনা ফাঁস হয়ে যাবে |

---

### `const isMatch = await bcrypt.compare(password, user.password_hash);`

```js
bcrypt.compare(
  password,             // ← ব্যবহারকারী এইমাত্র যা লিখল ("secret123")
  user.password_hash    // ← DB তে যা জমা আছে ("$2b$10$N9qo...")
)
```

**ভিতরে যা ঘটে:**

```
১. জমা থাকা hash এর গঠন ভাঙে:
   $2b$10$N9qo8uLOickgx2ZMRZoMye | IjZAgcfl7p92ldGxad...
   │  │   └──── salt ──────────┘   └──── আসল hash ───┘
   │  └── cost = 10
   └── সংস্করণ

২. সেই salt আর cost নিয়ে ব্যবহারকারীর দেওয়া পাসওয়ার্ড hash করে
   "secret123" + "N9qo8uLO..." → ১০২৪ চক্র → নতুন hash

৩. নতুন hash আর জমা থাকা hash তুলনা করে
   (constant-time তুলনা — timing attack ঠেকাতে)

৪. true / false ফেরত দেয়
```

**তাই SQL এ কখনো এভাবে লেখা যায় না:**

```sql
-- ❌ এটা কোনোদিন কাজ করবে না
WHERE email = $1 AND password_hash = $2
```

কারণ প্রতিবার hash আলাদা হয় (salt এর কারণে)। **hash মেলানো SQL এর কাজ নয়, bcrypt এর কাজ।**

| ভুল | ফল |
|---|---|
| `await` বাদ | `isMatch` হবে একটা Promise object। Promise সবসময় truthy → **যেকোনো পাসওয়ার্ডে login হয়ে যাবে!** ভয়ংকর নিরাপত্তা গর্ত |
| প্যারামিটারের ক্রম উল্টানো | `compare(hash, password)` → সবসময় `false`, কেউ login করতে পারবে না |

> **`await` বাদ পড়ার ঘটনাটা বাস্তবে ঘটেছে** — একাধিক কোম্পানির প্রোডাকশনে। কোনো error দেখায় না, সব টেস্ট পাস করে (সঠিক পাসওয়ার্ডেও তো `true` আসে), শুধু ভুল পাসওয়ার্ডেও ঢুকে যায়।

---

### Response এ `password_hash` নেই

```js
data: {
  id: user.id,
  name: user.name,
  email: user.email,
}
```

`user` object এ `password_hash` আছে (SELECT এ এনেছিলাম), কিন্তু হাতে বেছে বেছে তিনটা ফিল্ড পাঠালাম।

| `data: user` লিখলে | পুরো object যাবে, **hash সহ**। Postman এ দেখা যাবে, Flutter এর লগে থাকবে, হয়তো ব্যবহারকারীর ফোনে জমাও হবে |

---

## 🔄 Internal Flow — Login এর সম্পূর্ণ পথ

```
┌──────────────────────────────────────────────────────────────┐
│ ১. Postman                                                   │
│    POST /api/auth/login                                      │
│    { "email": "rana@mail.com", "password": "secret123" }     │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ২. express.json() → req.body তে object                       │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৩. Router → login controller                                 │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৪. email ছোট হাতে + trim                                     │
│    SELECT ... WHERE email = $1                               │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
╔══════════════════════════════════════════════════════════════╗
║ ৫. PostgreSQL                                                ║
║    Index Scan on users_email_key                             ║
║    → ১টা row পেল                                             ║
║    → { id: 2, name: 'Rana', email: '...',                    ║
║        password_hash: '$2b$10$N9qo...' }                     ║
╚═══════════════════════════╪══════════════════════════════════╝
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৬. rows.length === 0 ?                                       │
│      হ্যাঁ → 401 "Invalid email or password" (এখানেই শেষ)     │
│      না   → এগিয়ে যাও                                        │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৭. await bcrypt.compare("secret123", "$2b$10$N9qo...")       │
│                                                              │
│    hash থেকে salt বের করল                                    │
│    সেই salt দিয়ে "secret123" hash করল  ⏱️ ~১০০ms             │
│    দুটো মিলিয়ে দেখল                                          │
│    → true                                                    │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৮. isMatch === false ?                                       │
│      হ্যাঁ → 401 (একই বার্তা)                                 │
│      না   → 200 + ব্যবহারকারীর তথ্য                           │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৯. Postman এ 200 OK                                          │
│                                                              │
│    ⚠️ কিন্তু এখানে একটা বড় সমস্যা আছে —                       │
│       পরের request এ সার্ভার আবার ভুলে যাবে এ কে!             │
│       এই সমস্যার সমাধানই পরের lesson (JWT)                   │
└──────────────────────────────────────────────────────────────┘
```

---

## 🤔 এখানে থেমে সমস্যাটা বুঝে নাও

Login সফল হলো। এখন ব্যবহারকারী `GET /api/notes` এ যাবে।

```
Request 1:  POST /api/auth/login    → "তুমি Rana, স্বাগতম" ✅
Request 2:  GET  /api/notes         → "তুমি কে?" ❓
```

**HTTP stateless (স্টেটলেস)** — প্রতিটা request সম্পূর্ণ স্বাধীন। সার্ভারের কোনো স্মৃতি নেই যে আগের request টা কে পাঠিয়েছিল।

```
┌──────────┐  request 1  ┌──────────┐
│  Client  │ ──────────▶ │  Server  │  "ঠিক আছে, তুমি Rana"
└──────────┘             └──────────┘
                              │
                         (সব ভুলে গেল)
                              │
┌──────────┐  request 2  ┌──────────┐
│  Client  │ ──────────▶ │  Server  │  "আপনি কে?"
└──────────┘             └──────────┘
```

**সমাধানের দুটো পথ:**

| পদ্ধতি | কীভাবে | সমস্যা |
|---|---|---|
| **Session** | সার্ভার মনে রাখে কে কে ঢুকেছে, ক্লায়েন্টকে একটা id দেয় | সার্ভারের মেমরি লাগে; একাধিক সার্ভার হলে সবার মধ্যে ভাগ করতে হয় |
| **JWT** | সার্ভার একটা **স্বাক্ষরিত পরিচয়পত্র** দেয়, কিছুই মনে রাখে না | Token বাতিল করা কঠিন (Lesson 19 এ দেখব) |

Mobile app এর জন্য **JWT** ই মানানসই — কারণ সার্ভারকে কিছু মনে রাখতে হয় না, আর যত খুশি সার্ভার যোগ করা যায়।

পরের lesson এ ঠিক এটাই।

---

## 🧪 Postman Testing

### Test ১ — সঠিক তথ্য

```
POST http://localhost:5000/api/auth/login

{ "email": "rana@mail.com", "password": "secret123" }
```

**200 OK:**

```json
{
  "success": true,
  "message": "Login successful",
  "data": { "id": 2, "name": "Rana", "email": "rana@mail.com" }
}
```

### Test ২ — ভুল পাসওয়ার্ড

```json
{ "email": "rana@mail.com", "password": "wrongpass" }
```

**401 Unauthorized** — "Invalid email or password"

### Test ৩ — নেই এমন ইমেইল

```json
{ "email": "nobody@mail.com", "password": "secret123" }
```

**401 Unauthorized** — হুবহু একই বার্তা ✅ (তুলনা করে দেখো — ভিতরের কারণ আলাদা, বাইরে থেকে বোঝার উপায় নেই)

### Test ৪ — বড় হাতের ইমেইল

```json
{ "email": "RANA@MAIL.COM", "password": "secret123" }
```

**200 OK** ✅ — `.toLowerCase()` কাজ করছে।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `await bcrypt.compare` এ await বাদ | **যেকোনো পাসওয়ার্ডে login হয়ে যাবে** | সবসময় await |
| SQL এ `AND password_hash = $2` | কখনো মিলবে না | bcrypt.compare ব্যবহার করো |
| আলাদা error বার্তা | user enumeration | একই বার্তা |
| `SELECT *` | password_hash অজান্তে response এ চলে যেতে পারে | column বেছে নাও |
| login এ email lowercase না করা | register এ করেছ, login এ করোনি → মিলবে না | দুই জায়গায় একই নিয়ম |
| 404 ফেরত দেওয়া | ইমেইল নিবন্ধিত কিনা ফাঁস | 401 |
| `data: user` পুরো object | hash ফাঁস | ফিল্ড বেছে নাও |

---

## 🏋️ Practice

**১.** ভাবো: ইমেইল না পেলে ৫ms এ 401 ফেরত যায়, কিন্তু ইমেইল পেলে bcrypt চালাতে ১০০ms লাগে তারপর 401 যায়। এই সময়ের পার্থক্য থেকে আক্রমণকারী কী বুঝতে পারে?

<details>
<summary>উত্তর</summary>

সে বুঝতে পারে ইমেইলটা নিবন্ধিত কিনা — শুধু সময় মেপে। একে বলে **timing attack**।

আমরা বার্তা একই রেখেছি, কিন্তু সময়টা এখনো ফাঁস করছে।

সমাধান: ইমেইল না পেলেও একটা ডামি hash এর সাথে `bcrypt.compare` চালিয়ে দেওয়া, যাতে দুই পথেই সমান সময় লাগে:

```js
const DUMMY_HASH = '$2b$10$abcdefghijklmnopqrstuv...';
const hashToCompare = user ? user.password_hash : DUMMY_HASH;
const isMatch = await bcrypt.compare(password, hashToCompare);
if (!user || !isMatch) return res.status(401).json({...});
```

ব্যাংক বা স্বাস্থ্য অ্যাপে এই সতর্কতা নেওয়া হয়। সাধারণ অ্যাপে অনেকে নেয় না — কিন্তু জেনে রাখা ভালো।
</details>

**২.** ভাবো: কেউ যদি সেকেন্ডে ১০০০ বার login চেষ্টা করে?

<details>
<summary>উত্তর</summary>

এখন কিছুই তাকে থামাবে না — সে যত খুশি পাসওয়ার্ড চেষ্টা করতে পারবে (brute force)।

bcrypt ধীর হওয়ায় সার্ভার নিজেই হাঁপিয়ে যাবে (প্রতি চেষ্টায় ১০০ms CPU), যা আসলে **আরেকটা সমস্যা** — সার্ভার সবার জন্য ধীর হয়ে যাবে।

সমাধান: **rate limiting** — একই IP থেকে ১৫ মিনিটে সর্বোচ্চ ৫ বার login চেষ্টা। Lesson 22 এ করব।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-10" name="lesson-10"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎫 Lesson 10 — JWT তৈরি
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■□□□□□□□□□□□□]  10/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 09 (login কাজ করছে) |
| **এই ধাপ শেষে** | Login করলে token পাবে |
| **নতুন শব্দ** | JWT, header/payload/signature, base64url, secret, expiry, claim |

---

## 🎯 Goal

Login সফল হলে একটা **JWT token** বানিয়ে ফেরত দেব। এবং token টা ভিতরে আসলে কী — সেটা খুলে দেখব।

---

## 🧠 JWT কী — সহজ উপমা দিয়ে

**JWT** = JSON Web Token। এটা একটা **স্বাক্ষরিত পরিচয়পত্র**।

কনসার্টের হাতের ব্যান্ডের সাথে মিলিয়ে ভাবো:

```
১. টিকিট কাউন্টারে গেলে (login)
   → পরিচয় দেখালে (ইমেইল + পাসওয়ার্ড)
   → তারা হাতে ব্যান্ড পরিয়ে দিল (JWT)

২. ভিতরে যতবার যা করবে (প্রতিটা API call)
   → শুধু ব্যান্ডটা দেখাবে
   → আর পরিচয় দিতে হবে না

৩. দারোয়ান ব্যান্ড দেখে বুঝে নেয় এটা আসল
   → কারণ ওতে হলোগ্রাম (signature) আছে
   → কোনো তালিকা মেলাতে হয় না ← এটাই মূল কথা
```

**সবচেয়ে গুরুত্বপূর্ণ বৈশিষ্ট্য: সার্ভার কিছু মনে রাখে না।** Token নিজেই তার সব তথ্য বহন করে, আর signature দিয়ে প্রমাণ করে যে সেটা সার্ভারেরই দেওয়া।

---

## 🔬 JWT এর গঠন — তিন টুকরা

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImVtYWlsIjoicmFuYUBtYWlsLmNvbSIsImlhdCI6MTc1MzYwMDAwMCwiZXhwIjoxNzUzNjA3MjAwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
└──────────── HEADER ────────────┘ └──────────────────── PAYLOAD ────────────────────┘ └────────── SIGNATURE ──────────┘
                                 ↑                                                    ↑
                              বিন্দু (.)                                          বিন্দু (.)
```

তিনটা অংশ, দুটো বিন্দু দিয়ে আলাদা।

### অংশ ১ — HEADER

```json
{ "alg": "HS256", "typ": "JWT" }
```

"এই token টা HS256 পদ্ধতিতে স্বাক্ষর করা হয়েছে।" — যাচাইকারীকে বলে দেয় কীভাবে মেলাতে হবে।

### অংশ ২ — PAYLOAD (তোমার ডেটা)

```json
{
  "userId": 2,
  "email": "rana@mail.com",
  "iat": 1753600000,
  "exp": 1753607200
}
```

| ফিল্ড | মানে |
|---|---|
| `userId` | তুমি যা রেখেছ |
| `email` | তুমি যা রেখেছ |
| `iat` | issued at — কখন তৈরি হয়েছিল (স্বয়ংক্রিয়) |
| `exp` | expiry — কখন মেয়াদ শেষ (স্বয়ংক্রিয়) |

> 🚨 **সবচেয়ে জরুরি কথা: PAYLOAD এনক্রিপ্টেড নয়, শুধু base64 এ লেখা।** যে কেউ token টা কপি করে [jwt.io](https://jwt.io) এ পেস্ট করলেই ভিতরের সব পড়তে পারবে।
>
> **তাই payload এ কখনো রাখবে না:** পাসওয়ার্ড, hash, ফোন নম্বর, ঠিকানা, ক্রেডিট কার্ড, বা যেকোনো গোপন তথ্য।
> **রাখবে:** userId, email, role — যা জানলে কারো ক্ষতি নেই।

### অংশ ৩ — SIGNATURE (স্বাক্ষর)

```
HMACSHA256(
  base64url(header) + "." + base64url(payload),
  SECRET_KEY          ← শুধু তোমার সার্ভার জানে
)
```

**এটাই পুরো ব্যবস্থার ভিত্তি।** Secret ছাড়া কেউ বৈধ signature বানাতে পারবে না।

**কেউ payload বদলে ফেললে কী হয়?**

```
আক্রমণকারী token নিল, payload এ userId 2 → 1 বদলে দিল
(অন্যের নোট দেখার আশায়)
        │
        ▼
সার্ভার যাচাই করে:
    নতুন payload + SECRET  →  নতুন signature হিসাব করল
    "abc123..."
        │
    token এ যে signature ছিল: "xyz789..."
        │
    মেলে না ❌  →  401 Unauthorized
```

সে নতুন signature বানাতে পারবে না, কারণ SECRET তার কাছে নেই। **তাই JWT জালিয়াতি-প্রতিরোধী।**

---

## 💻 Code

### ইনস্টল

```bash
npm install jsonwebtoken
```

### `.env` এ যোগ করো

```env
JWT_SECRET=এখানে_খুব_লম্বা_এলোমেলো_একটা_গোপন_লেখা_বসাও
JWT_EXPIRES_IN=2h
```

**Secret বানানোর সঠিক উপায়:**

```bash
node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
```

এটা ১২৮ অক্ষরের এলোমেলো একটা string দেবে। ওটাই বসাও।

> ❌ কখনো `secret123`, `mysecret`, `jwtkey` জাতীয় কিছু দিও না। আক্রমণকারী সাধারণ শব্দের তালিকা নিয়ে চেষ্টা করে দেখে (এই আক্রমণের নাম **JWT cracking**) — দুর্বল secret কয়েক সেকেন্ডে ভেঙে যায়। তখন সে নিজেই যেকোনো ব্যবহারকারী সেজে token বানিয়ে ফেলতে পারবে।

### ফাইল — `src/utils/jwt.js` (নতুন)

```js
const jwt = require('jsonwebtoken');

const generateAccessToken = (user) => {
  return jwt.sign(
    {
      userId: user.id,
      email: user.email,
    },
    process.env.JWT_SECRET,
    {
      expiresIn: process.env.JWT_EXPIRES_IN || '2h',
    }
  );
};

module.exports = { generateAccessToken };
```

### `src/controllers/auth.controller.js` (login আপডেট)

```js
const { generateAccessToken } = require('../utils/jwt');   // 👉 নতুন

// ... login এর ভিতরে, isMatch চেকের পর:

    const accessToken = generateAccessToken(user);          // 👉 নতুন

    return res.status(200).json({
      success: true,
      message: 'Login successful',
      data: {
        user: {
          id: user.id,
          name: user.name,
          email: user.email,
        },
        accessToken,                                        // 👉 নতুন
      },
    });
```

---

## 🔍 লাইন-বাই-লাইন

### `jwt.sign(payload, secret, options)`

```js
jwt.sign(
  { userId: user.id, email: user.email },   // ১. PAYLOAD — যা token এ থাকবে
  process.env.JWT_SECRET,                   // ২. SECRET — যা দিয়ে স্বাক্ষর
  { expiresIn: '2h' }                       // ৩. OPTIONS — মেয়াদ
)
```

**ভিতরে যা ঘটে:**

```
১. Header বানাল:  {"alg":"HS256","typ":"JWT"}
   base64url করল: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

২. Payload এ iat আর exp যোগ করল:
   {"userId":2,"email":"rana@mail.com","iat":1753600000,"exp":1753607200}
   base64url করল: eyJ1c2VySWQiOjIsImVtYWlsIjoi...

৩. দুটো জোড়া দিল বিন্দু দিয়ে:
   "eyJhbGci....eyJ1c2VySWQ..."

৪. HMAC-SHA256 দিয়ে SECRET সহ স্বাক্ষর করল:
   "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

৫. তিনটা জুড়ে দিল:
   header.payload.signature
```

⚠️ `jwt.sign()` **সমকালীন (synchronous)** — এখানে `await` লাগে না, কারণ কাজটা মাত্র ~১ms এর।

| ভুল | ফল |
|---|---|
| `process.env.JWT_SECRET` না থাকা (`.env` এ লেখা নেই) | `Error: secretOrPrivateKey must have a value` — সার্ভার ক্র্যাশ |
| Payload এ `password_hash` রাখা | jwt.io এ যে কেউ পড়ে ফেলবে, চরম গর্ত |
| `expiresIn` না দেওয়া | Token **কখনো মেয়াদোত্তীর্ণ হবে না**। একবার চুরি হলে সারাজীবনের প্রবেশাধিকার |
| Secret কোডে হার্ডকোড | GitHub এ push হলেই সব শেষ |

---

### `expiresIn: '2h'` — মেয়াদ কত হওয়া উচিত

```
মেয়াদ ছোট (১৫ মিনিট)          মেয়াদ বড় (৩০ দিন)
────────────────────           ──────────────────
✅ চুরি হলে ক্ষতি কম            ❌ চুরি হলে ৩০ দিন খোলা
❌ ব্যবহারকারীকে বারবার         ✅ ব্যবহারকারীর আরাম
   login করতে হয়
```

দুটো সুবিধা একসাথে পাওয়ার কৌশলই **refresh token** — Lesson 18 এ।

আপাতত `2h` রাখলাম, যাতে Postman এ পরীক্ষা করতে করতে বারবার মেয়াদ শেষ না হয়।

গ্রহণযোগ্য মান: `'15m'`, `'2h'`, `'7d'`, বা সংখ্যায় সেকেন্ড (`7200`)।

---

## 🔄 সম্পূর্ণ Authentication Flow (তুমি যেটা চেয়েছিলে)

```
┌────────────────────────────────────────────────────────────────┐
│                        ধাপ ১ — LOGIN                           │
└────────────────────────────────────────────────────────────────┘

    Flutter / Postman                          Node Server
          │                                          │
          │  POST /api/auth/login                    │
          │  { email, password }                     │
          │─────────────────────────────────────────▶│
          │                                          │
          │                          ┌───────────────▼──────────────┐
          │                          │ SELECT ... WHERE email = $1  │
          │                          └───────────────┬──────────────┘
          │                                          │
          │                                    PostgreSQL
          │                                          │
          │                          ┌───────────────▼──────────────┐
          │                          │ user পাওয়া গেল?              │
          │                          │   না → 401                   │
          │                          └───────────────┬──────────────┘
          │                                          │ হ্যাঁ
          │                          ┌───────────────▼──────────────┐
          │                          │ bcrypt.compare(              │
          │                          │   দেওয়া পাসওয়ার্ড,           │
          │                          │   জমা থাকা hash)             │
          │                          │   false → 401                │
          │                          └───────────────┬──────────────┘
          │                                          │ true
          │                          ┌───────────────▼──────────────┐
          │                          │ jwt.sign({userId, email},    │
          │                          │          SECRET,             │
          │                          │          {expiresIn:'2h'})   │
          │                          │                              │
          │                          │ → eyJhbGci.eyJ1c2Vy.SflKxw   │
          │                          └───────────────┬──────────────┘
          │                                          │
          │  200 OK                                  │
          │  { user: {...}, accessToken: "eyJ..." }  │
          │◀─────────────────────────────────────────│
          │                                          │
   ┌──────▼─────────────────────┐                    │
   │ Flutter টোকেন জমা রাখে      │                    │
   │ (flutter_secure_storage)   │                    │
   └────────────────────────────┘                    │


┌────────────────────────────────────────────────────────────────┐
│                  ধাপ ২ — সুরক্ষিত API কল                        │
│                     (পরের lesson এ বানাব)                       │
└────────────────────────────────────────────────────────────────┘

    Flutter / Postman                          Node Server
          │                                          │
          │  GET /api/notes                          │
          │  Authorization: Bearer eyJhbGci...       │
          │─────────────────────────────────────────▶│
          │                                          │
          │                          ┌───────────────▼──────────────┐
          │                          │      authMiddleware          │
          │                          │                              │
          │                          │ ১. header আছে?  না → 401     │
          │                          │ ২. "Bearer " কেটে token নাও  │
          │                          │ ৩. jwt.verify(token, SECRET) │
          │                          │      signature মেলে?         │
          │                          │      মেয়াদ আছে?              │
          │                          │      না → 401                │
          │                          │ ৪. req.user = payload        │
          │                          │ ৫. next() → এগিয়ে যাও        │
          │                          └───────────────┬──────────────┘
          │                                          ▼
          │                          ┌──────────────────────────────┐
          │                          │        Controller            │
          │                          │  req.user.userId ব্যবহার করে │
          │                          │  SELECT ... WHERE user_id=$1 │
          │                          └───────────────┬──────────────┘
          │                                          │
          │  200 OK  { notes: [...] }                │
          │◀─────────────────────────────────────────│
```

---

## 🧪 Postman Testing

### Test ১ — Login করে token নাও

```
POST http://localhost:5000/api/auth/login
{ "email": "rana@mail.com", "password": "secret123" }
```

**200 OK:**

```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "user": { "id": 2, "name": "Rana", "email": "rana@mail.com" },
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImVtYWlsIjoicmFuYUBtYWlsLmNvbSIsImlhdCI6MTc1MzYwMDAwMCwiZXhwIjoxNzUzNjA3MjAwfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
  }
}
```

### Test ২ — Token টা খুলে দেখো (এটা অবশ্যই করো)

[jwt.io](https://jwt.io) এ গিয়ে token টা পেস্ট করো। ডান পাশে দেখাবে:

```json
HEADER:   { "alg": "HS256", "typ": "JWT" }
PAYLOAD:  { "userId": 2, "email": "rana@mail.com",
            "iat": 1753600000, "exp": 1753607200 }
SIGNATURE: ❌ Invalid Signature (কারণ jwt.io তোমার secret জানে না)
```

**তুমি নিজের চোখে দেখলে — payload যে কেউ পড়তে পারে।** এই কারণেই সেখানে গোপন তথ্য রাখা যায় না।

### Test ৩ — Payload বদলানোর চেষ্টা

jwt.io তে `userId` ২ থেকে ১ করে দাও, নতুন token কপি করো। পরের lesson এ যখন middleware বানাব, এই বদলানো token দিয়ে চেষ্টা করে দেখবে — **401 পাবে**, কারণ signature মিলবে না।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| Secret কোডে হার্ডকোড | GitHub এ ফাঁস → যে কেউ token বানাতে পারবে | `.env` এ রাখো |
| দুর্বল secret (`secret123`) | কয়েক সেকেন্ডে ভাঙা যায় | ৬৪ বাইট এলোমেলো |
| `expiresIn` না দেওয়া | অমর token | সবসময় দাও |
| Payload এ সংবেদনশীল তথ্য | base64, যে কেউ পড়বে | শুধু id, email, role |
| Payload এ পুরো user object | Token অকারণে বড় হয়, প্রতি request এ যায় | ন্যূনতম রাখো |
| Token কে "এনক্রিপ্টেড" ভাবা | ভুল ধারণা থেকে গোপন তথ্য রাখা | এটা শুধু **স্বাক্ষরিত**, গোপন নয় |
| `.env` git এ push | সব শেষ | `.gitignore` |
| Production এ secret বদলানো | সবাই এক ধাক্কায় logout হয়ে যাবে | জেনে বুঝে করো |

---

## 🏋️ Practice

**১.** ভাবো: JWT payload যদি যে কেউ পড়তে পারে, তাহলে এটা নিরাপদ কীভাবে?

<details>
<summary>উত্তর</summary>

কারণ JWT এর উদ্দেশ্য **গোপনীয়তা নয়, সত্যতা** (authenticity)।

উপমা: তোমার NID কার্ড। যে কেউ ওটা দেখে তোমার নাম-জন্মতারিখ পড়তে পারে — সেটা গোপন নয়। কিন্তু কেউ নকল বানাতে পারে না, কারণ ওতে সরকারের নিরাপত্তা-চিহ্ন আছে।

JWT ঠিক তাই — **"এই তথ্যগুলো আমিই দিয়েছি, কেউ বদলায়নি"** এটুকুই প্রমাণ করে।

গোপনীয়তা আসে অন্য জায়গা থেকে — HTTPS। তাতে তারের মধ্য দিয়ে যাওয়ার সময় কেউ token টা দেখতেই পায় না।
</details>

**২.** ভাবো: কেউ পুরো token টা চুরি করে ফেলল (payload বদলায়নি, হুবহু কপি)। সে কি তোমার অ্যাকাউন্টে ঢুকতে পারবে?

<details>
<summary>উত্তর</summary>

**হ্যাঁ, পারবে।** এটাই JWT এর সবচেয়ে বড় দুর্বলতা — token যার হাতে, ক্ষমতা তার।

তাই তিনটা প্রতিরক্ষা লাগে:
1. **HTTPS বাধ্যতামূলক** — নাহলে wifi তে যে কেউ token টা তুলে নিতে পারবে
2. **ছোট মেয়াদ** — চুরি হলেও ১৫ মিনিট পর অকেজো (Lesson 18 এ refresh token দিয়ে এটা সম্ভব হবে)
3. **নিরাপদ সংরক্ষণ** — Flutter এ `SharedPreferences` নয়, `flutter_secure_storage` (iOS Keychain / Android Keystore)
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-11" name="lesson-11"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛡️ Lesson 11 — Auth Middleware
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■□□□□□□□□□□□]  11/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 10 (token পাচ্ছ) |
| **এই ধাপ শেষে** | সুরক্ষিত API — token ছাড়া ঢোকা যাবে না |
| **নতুন শব্দ** | middleware, next(), Authorization header, Bearer, jwt.verify(), req.user |

---

## 🎯 Goal

একটা প্রহরী বানাব যেটা প্রতিটা সুরক্ষিত API এর সামনে দাঁড়িয়ে token পরীক্ষা করবে। বৈধ হলে ঢুকতে দেবে, নাহলে 401।

---

## 🧠 Middleware কী

**Middleware (মিডলওয়্যার)** = request আর controller এর মাঝখানে বসে থাকা কোড।

```
Request ──▶ [MW 1] ──▶ [MW 2] ──▶ [MW 3] ──▶ Controller ──▶ Response
             json      auth       log
```

প্রতিটা middleware তিনটা কাজের একটা করে:

```
১. request কে সমৃদ্ধ করে   →  req.body বসায়, req.user বসায়
২. পরের ধাপে পাঠায়        →  next()
৩. অথবা এখানেই থামিয়ে দেয় →  res.status(401).json(...)
```

Flutter এর সাথে মিলিয়ে: Dio এর `Interceptor` — request যাওয়ার আগে token যোগ করে দেয়। Express এর middleware ঠিক উল্টো দিকের কাজটা করে — আসা request থেকে token বের করে যাচাই করে।

**তুমি ইতিমধ্যেই middleware ব্যবহার করেছ:**

```js
app.use(express.json());   // ← এটাই একটা middleware
```

---

## 💻 Code

### ফাইল ১ — `src/middlewares/auth.middleware.js` (নতুন)

```js
const jwt = require('jsonwebtoken');

const authenticate = (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({
        success: false,
        message: 'Access token is required',
      });
    }

    const token = authHeader.split(' ')[1];

    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    req.user = {
      userId: decoded.userId,
      email: decoded.email,
    };

    next();
  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        success: false,
        message: 'Token expired',
        code: 'TOKEN_EXPIRED',
      });
    }

    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        success: false,
        message: 'Invalid token',
      });
    }

    console.error('Auth middleware error:', error);
    return res.status(500).json({
      success: false,
      message: 'Authentication failed',
    });
  }
};

module.exports = { authenticate };
```

### ফাইল ২ — `src/controllers/auth.controller.js` এ যোগ করো

```js
const getMe = async (req, res) => {
  try {
    const result = await query(
      `SELECT id, name, email, created_at
       FROM users
       WHERE id = $1`,
      [req.user.userId]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        message: 'User not found',
      });
    }

    return res.status(200).json({
      success: true,
      data: result.rows[0],
    });
  } catch (error) {
    console.error('Get me error:', error);
    return res.status(500).json({
      success: false,
      message: 'Something went wrong',
    });
  }
};

module.exports = { register, login, getMe };
```

### ফাইল ৩ — `src/routes/auth.routes.js` (আপডেট)

```js
const express = require('express');
const { register, login, getMe } = require('../controllers/auth.controller');
const { authenticate } = require('../middlewares/auth.middleware');

const router = express.Router();

router.post('/register', register);
router.post('/login', login);
router.get('/me', authenticate, getMe);     // 👉 দুটো ফাংশন — প্রহরী, তারপর কাজ

module.exports = router;
```

---

## 🔍 লাইন-বাই-লাইন

### `const authenticate = (req, res, next) => {`

Middleware এর হাতে **তিনটা** জিনিস আসে (controller এর দুটো, এখানে একটা বেশি):

| Parameter | কাজ |
|---|---|
| `req` | request — পড়া যাবে, বদলানোও যাবে |
| `res` | response — চাইলে এখানেই থামিয়ে উত্তর দিতে পারে |
| `next` | **পরের ধাপে যাওয়ার ফাংশন** |

---

### `const authHeader = req.headers.authorization;`

HTTP header একটা key-value তালিকা যা request এর সাথে যায়:

```
GET /api/auth/me HTTP/1.1
Host: localhost:5000
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json
```

`req.headers` এ Express সব header ছোট হাতের অক্ষরে রাখে — তাই `Authorization` লিখলেও `req.headers.authorization` দিয়েই পড়তে হয়।

**Token কেন header এ, body তে নয়?**

| কারণ | ব্যাখ্যা |
|---|---|
| GET/DELETE এ body থাকে না | কিন্তু header সবসময় থাকে |
| এটাই আন্তর্জাতিক মান | RFC 6750 |
| Proxy/gateway চেনে | Load balancer, API gateway এই header বোঝে |
| Body তো ডেটার জায়গা | পরিচয় আর ডেটা আলাদা থাকাই পরিচ্ছন্ন |

---

### `if (!authHeader || !authHeader.startsWith('Bearer '))`

```js
!authHeader                          // header টাই নেই
!authHeader.startsWith('Bearer ')    // আছে, কিন্তু ভুল ফরম্যাট
```

**`Bearer` শব্দটা কেন?** এটা authentication এর ধরন বলে — "যে এটা বহন করছে (bearer), সে-ই অধিকারী"।

```
Authorization: Bearer eyJhbGci...     ← JWT / OAuth
Authorization: Basic dXNlcjpwYXNz     ← username:password base64
Authorization: Digest ...             ← পুরনো পদ্ধতি
```

| ভুল | ফল |
|---|---|
| `Bearer` এর পর space না দেওয়া | `startsWith('Bearer ')` fail করবে (space সহ মেলাচ্ছি) |
| দুই চেকের প্রথমটা বাদ | header না থাকলে `undefined.startsWith()` → `TypeError` → 500 |
| `bearer` ছোট হাতে | `startsWith` case-sensitive → fail। সহনশীল করতে চাইলে আগে `.toLowerCase()` |

**`||` এর ক্রমটাও গুরুত্বপূর্ণ** — JavaScript বাঁ থেকে ডানে যাচাই করে, প্রথমটা সত্য হলে দ্বিতীয়টা চালায়ই না। তাই `undefined.startsWith()` এর বিপদ এড়ানো যায়।

---

### `const token = authHeader.split(' ')[1];`

```
"Bearer eyJhbGciOiJIUzI1NiIs..."
        │
   .split(' ') করলে:
        │
   ["Bearer", "eyJhbGciOiJIUzI1NiIs..."]
       [0]              [1]  ← এটা চাই
```

| ভুল | ফল |
|---|---|
| `[0]` লেখা | token এর জায়গায় `"Bearer"` string যাবে → সবসময় Invalid token |
| `split` না করে পুরো header টা verify এ পাঠানো | `"Bearer eyJ..."` বৈধ JWT নয় → JsonWebTokenError |

---

### `const decoded = jwt.verify(token, process.env.JWT_SECRET);`

**এই এক লাইনেই আসল নিরাপত্তা।** ভিতরে যা ঘটে:

```
১. Token কে তিন টুকরো করে: header . payload . signature

২. header + payload নিয়ে SECRET দিয়ে নিজে একটা signature হিসাব করে

৩. হিসাব করা signature ≟ token এর signature
      মেলে না → JsonWebTokenError ছুড়ে দেয় ❌
      মেলে   → এগোয় ✅

৪. payload এর exp দেখে: এখনকার সময় > exp ?
      হ্যাঁ → TokenExpiredError ছুড়ে দেয় ❌
      না   → এগোয় ✅

৫. payload টা object আকারে ফেরত দেয়:
   { userId: 2, email: 'rana@mail.com', iat: ..., exp: ... }
```

> **`jwt.decode()` আর `jwt.verify()` — এই পার্থক্যটা মনে রাখো।**
> `decode()` শুধু payload খুলে দেখায়, **signature যাচাই করে না** — যে কেউ বানানো token ও পাস করে যাবে।
> `verify()` স্বাক্ষর মেলায়।
> **কখনো `decode()` দিয়ে authentication করবে না।** এটা একটা পরিচিত নিরাপত্তা দুর্ঘটনা।

| ভুল | ফল |
|---|---|
| `verify` এর বদলে `decode` | **যে কেউ নিজের হাতে token বানিয়ে যেকোনো ব্যবহারকারী সেজে ঢুকে যাবে।** ভয়ংকরতম গর্ত |
| ভুল secret দেওয়া | সব token invalid দেখাবে |
| `try/catch` না দেওয়া | verify ব্যর্থ হলে exception ছুড়বে, কেউ ধরবে না → সার্ভার ক্র্যাশ |

---

### `req.user = { userId: decoded.userId, email: decoded.email };`

**এখানেই middleware তার আসল উপহারটা রেখে যায়।**

`req` object টা এই request এর পুরো যাত্রায় একই থাকে। তাই middleware যা বসাবে, controller তা পাবে:

```
      Middleware                        Controller
  req.user = {userId: 2}   ────────▶   req.user.userId  → 2
```

এর ফলে controller এ আর token নিয়ে ভাবতে হয় না — শুধু `req.user.userId` ব্যবহার করলেই হয়।

| না বসালে | Controller জানবেই না কে request পাঠিয়েছে। তখন ক্লায়েন্টকে `userId` পাঠাতে বলতে হতো — **আর তখন যে কেউ অন্যের userId পাঠিয়ে অন্যের ডেটা পড়ে ফেলত** |

> 🚨 **এই কথাটা গেঁথে নাও: userId সবসময় token থেকে নেবে, কখনো request body বা query থেকে নয়।**
> Body থেকে নিলে `{ "userId": 999 }` পাঠিয়ে যে কেউ অন্যের নোট পড়ে ফেলবে। এই দুর্বলতার নাম **IDOR** (Insecure Direct Object Reference) — বাস্তবে সবচেয়ে বেশি ঘটা API দুর্বলতাগুলোর একটা।

---

### `next();`

"আমার কাজ শেষ, পরের ধাপে যাও।"

```
router.get('/me', authenticate, getMe);
                       │           │
                       │           └── next() ডাকলে এটা চলে
                       └── প্রথমে এটা চলে
```

| ভুল | ফল |
|---|---|
| `next()` না লেখা | Middleware চলবে, কিন্তু controller কখনো ডাকা হবে না। **Postman অনন্তকাল ঘুরতে থাকবে**, কোনো error নেই — ধরা কঠিন |
| `next()` এর পরেও `res` পাঠানো | `Cannot set headers after they are sent` |
| Error এর পর `return` না দিয়ে `next()` | দুইবার response যাবে |

---

### Error এর ধরন আলাদা করে ধরা

```js
if (error.name === 'TokenExpiredError') {
  return res.status(401).json({ ..., code: 'TOKEN_EXPIRED' });
}
if (error.name === 'JsonWebTokenError') {
  return res.status(401).json({ message: 'Invalid token' });
}
```

| Error | কখন | Flutter কী করবে |
|---|---|---|
| `TokenExpiredError` | মেয়াদ শেষ | নীরবে refresh করবে (Lesson 18) |
| `JsonWebTokenError` | signature ভুল / গঠন ভাঙা | ব্যবহারকারীকে logout করাবে |
| `NotBeforeError` | `nbf` claim ভবিষ্যতে | বিরল |

**`code: 'TOKEN_EXPIRED'` কেন যোগ করলাম?** কারণ Flutter এ বার্তার লেখা মিলিয়ে সিদ্ধান্ত নেওয়া ভঙ্গুর:

```dart
// ❌ ভঙ্গুর — বার্তা বদলালেই ভাঙবে
if (response.body['message'] == 'Token expired') { ... }

// ✅ মজবুত — code কখনো বদলাবে না
if (response.body['code'] == 'TOKEN_EXPIRED') { await refreshToken(); }
```

---

## 🔄 Internal Flow — সুরক্ষিত request এর পূর্ণ পথ

```
┌──────────────────────────────────────────────────────────────┐
│ ১. Postman                                                   │
│    GET /api/auth/me                                          │
│    Authorization: Bearer eyJhbGci...                         │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ২. express.json()  → GET এ body নেই, কিছু না করে ছেড়ে দিল    │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৩. Router: '/api/auth' + '/me' মিলল, method GET ✅            │
│    দুটো handler আছে → প্রথমটা চালাও                          │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
╔══════════════════════════════════════════════════════════════╗
║ ৪. authenticate middleware                                   ║
║                                                              ║
║    ক) req.headers.authorization পড়ল                          ║
║       → "Bearer eyJhbGci..."                                 ║
║                                                              ║
║    খ) "Bearer " দিয়ে শুরু? ✅                                 ║
║       না হলে → 401, এখানেই শেষ ⛔                             ║
║                                                              ║
║    গ) split(' ')[1] → "eyJhbGci..."                          ║
║                                                              ║
║    ঘ) jwt.verify(token, SECRET)                              ║
║       • signature হিসাব করল, মেলাল ✅                         ║
║       • exp দেখল, মেয়াদ আছে ✅                                ║
║       • payload ফেরত দিল                                     ║
║       ব্যর্থ হলে → 401, এখানেই শেষ ⛔                          ║
║                                                              ║
║    ঙ) req.user = { userId: 2, email: 'rana@mail.com' }        ║
║                                                              ║
║    চ) next()  →  🚪 দরজা খুলে দিল                             ║
╚═══════════════════════════╪══════════════════════════════════╝
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৫. getMe controller                                          │
│    SELECT id, name, email FROM users WHERE id = $1            │
│    $1 = req.user.userId = 2   ← token থেকে এসেছে, নিরাপদ     │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
                      PostgreSQL → row
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৬. 200 OK + ব্যবহারকারীর তথ্য → Postman                       │
└──────────────────────────────────────────────────────────────┘
```

**Token না থাকলে পথটা কত ছোট, লক্ষ্য করো:**

```
Postman → express.json() → Router → authenticate → 401 ⛔
                                          │
                                    Controller কখনো চলল না
                                    Database স্পর্শও করল না
```

এটাই middleware এর সৌন্দর্য — অবৈধ request খরচের আগেই কেটে যায়।

---

## 🧪 Postman Testing

### Test ১ — Token সহ (সঠিক পথ)

```
Method  : GET
URL     : http://localhost:5000/api/auth/me
Headers : Authorization: Bearer <login থেকে পাওয়া token>
```

**200 OK:**

```json
{
  "success": true,
  "data": {
    "id": 2,
    "name": "Rana",
    "email": "rana@mail.com",
    "created_at": "2026-07-27T10:30:00.000Z"
  }
}
```

> Postman এ Headers ট্যাবে গিয়ে Key তে `Authorization`, Value তে `Bearer eyJ...` লেখো। **`Bearer` এর পর একটা space।**

### Test ২ — Token ছাড়া

Header টা মুছে দাও। **401:**

```json
{ "success": false, "message": "Access token is required" }
```

### Test ৩ — বিকৃত token

Token এর শেষ ৩টা অক্ষর বদলে দাও। **401:**

```json
{ "success": false, "message": "Invalid token" }
```

**Signature যাচাই কাজ করছে ✅** — এটাই প্রমাণ যে কেউ token জাল করতে পারবে না।

### Test ৪ — jwt.io তে payload বদলে দেখো

jwt.io তে গিয়ে `userId` কে ২ থেকে ১ করে দাও (অন্যের তথ্য দেখার আশায়)। নতুন token টা Postman এ ব্যবহার করো।

**401 Invalid token** ✅

কারণ payload বদলালে signature আর মেলে না, আর নতুন signature বানাতে SECRET লাগবে — যেটা তার কাছে নেই।

### Test ৫ — মেয়াদোত্তীর্ণ token

`.env` এ `JWT_EXPIRES_IN=10s` করে সার্ভার restart করো, login করো, ১৫ সেকেন্ড অপেক্ষা করে `/me` কল করো।

```json
{ "success": false, "message": "Token expired", "code": "TOKEN_EXPIRED" }
```

পরীক্ষা শেষে আবার `2h` করে দাও।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `next()` না লেখা | Request অনন্তকাল ঝুলে থাকে | সফল পথে অবশ্যই `next()` |
| `verify` এর বদলে `decode` | যে কেউ token বানিয়ে ঢুকে যাবে | সবসময় `verify` |
| `split(' ')[0]` | সবসময় Invalid token | `[1]` |
| Postman এ `Bearer ` লিখতে ভুলে যাওয়া | 401, যদিও token ঠিক | prefix লাগবে |
| userId body থেকে নেওয়া | IDOR — অন্যের ডেটা পড়া যাবে | `req.user.userId` |
| Route এ middleware বসাতে ভুলে যাওয়া | API উন্মুক্ত থেকে গেল | প্রতিটা সুরক্ষিত route চেক করো |
| Middleware কে controller এর পরে বসানো | প্রহরী দরজার পিছনে দাঁড়িয়ে | `authenticate` আগে |
| Error বার্তায় কারণ বিস্তারিত বলা | আক্রমণকারীকে সাহায্য | সংক্ষিপ্ত বার্তা |
| `try/catch` না দেওয়া | verify ব্যর্থ হলে সার্ভার ক্র্যাশ | try/catch |

---

## 🏋️ Practice

**১.** ভাবো: `next()` এর বদলে যদি সরাসরি controller ফাংশনটা কল করে দিই?

<details>
<summary>উত্তর</summary>

কাজ করবে, কিন্তু middleware এর পুরো সুবিধাটাই নষ্ট হবে —

- Middleware টা তখন ওই একটা controller এর সাথে বাঁধা পড়ে যাবে, পুনঃব্যবহার করা যাবে না
- চেইনে তৃতীয় কোনো middleware (যেমন logging) যোগ করা যাবে না
- Express এর error handling কাজ করবে না

`next()` এর পুরো ব্যাপারটাই হলো **শিথিল সংযোগ (loose coupling)** — প্রহরী জানে না তার পরে কে আছে, শুধু জানে "পরেরজনকে ডাকো"।
</details>

**২.** ভাবো: `/api/notes` এর সব route এ middleware লাগাতে হবে। প্রতিটা লাইনে `authenticate` লেখা ছাড়া উপায় আছে?

<details>
<summary>উত্তর</summary>

আছে — router এর উপরেই একবার বসিয়ে দাও:

```js
router.use(authenticate);          // ← এর নিচের সব route সুরক্ষিত

router.post('/', createNote);
router.get('/', getNotes);
router.delete('/:id', deleteNote);
```

সুবিধা: নতুন route যোগ করলে সেটা **আপনাআপনি** সুরক্ষিত থাকবে — কেউ middleware লাগাতে ভুলে গিয়ে API উন্মুক্ত করে ফেলবে না।

Lesson 12 এ notes route এ ঠিক এটাই করব। **নিরাপত্তায় ডিফল্ট সবসময় "বন্ধ" হওয়া উচিত, "খোলা" নয়।**
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-12" name="lesson-12"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📝 Lesson 12 — Create Note
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■□□□□□□□□□□]  12/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 11 (middleware কাজ করছে) |
| **এই ধাপ শেষে** | `POST /api/notes` — নিজের নামে নোট তৈরি হবে |
| **নতুন শব্দ** | Foreign Key, ON DELETE CASCADE, relationship, ownership |

---

## 🎯 Goal

নোট রাখার টেবিল বানাব, আর নোট তৈরির API লিখব। প্রতিটা নোট **কোন ব্যবহারকারীর** সেটা যুক্ত থাকবে।

---

## 🗄️ ধাপ ১ — notes টেবিল

### ফাইল — `src/db/migrations/002_create_notes.sql`

```sql
CREATE TABLE IF NOT EXISTS notes (
  id         SERIAL       PRIMARY KEY,
  user_id    INTEGER      NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title      VARCHAR(200) NOT NULL,
  content    TEXT         NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_notes_user_id ON notes(user_id);
CREATE INDEX IF NOT EXISTS idx_notes_user_created ON notes(user_id, created_at DESC);
```

```bash
psql -d noteapp -f src/db/migrations/002_create_notes.sql
```

---

### `user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE`

এই এক লাইনেই দুটো টেবিলের সম্পর্ক তৈরি হয়।

```
     users                          notes
┌────┬────────────┐          ┌────┬─────────┬──────────┐
│ id │   email    │          │ id │ user_id │  title   │
├────┼────────────┤          ├────┼─────────┼──────────┤
│ 1  │ a@mail.com │◀────┐    │ 1  │    1    │ বাজার    │
│ 2  │ b@mail.com │◀──┐ ├────│ 2  │    1    │ মিটিং    │
└────┴────────────┘   │ └────│ 3  │    1    │ পড়া      │
                      └──────│ 4  │    2    │ কেনাকাটা │
                             └────┴─────────┴──────────┘
                                       ↑
                              Foreign Key — কোন user এর নোট
```

একে বলে **one-to-many** সম্পর্ক: এক ব্যবহারকারীর অনেক নোট, কিন্তু প্রতিটা নোট ঠিক একজনের।

| অংশ | কাজ | না দিলে |
|---|---|---|
| `REFERENCES users(id)` | **Foreign Key** — এখানে যা বসবে তা `users` এ থাকতেই হবে | যে ব্যবহারকারী নেই তার নামেও নোট ঢুকে যাবে (**orphan row** — অনাথ সারি) |
| `NOT NULL` | মালিকবিহীন নোট চলবে না | `user_id = NULL` নোট তৈরি হবে, কেউ কখনো দেখতে পাবে না |
| `ON DELETE CASCADE` | ব্যবহারকারী মুছলে তার সব নোটও মুছে যাবে | ব্যবহারকারী মুছতে গেলে PostgreSQL আটকে দেবে (`foreign_key_violation`), কারণ নোটগুলো তাকে ধরে আছে |

**`ON DELETE` এর বিকল্পগুলো:**

| বিকল্প | আচরণ | কখন |
|---|---|---|
| `CASCADE` | সন্তানও মুছে যায় | নোট, comment — মালিক ছাড়া অর্থহীন |
| `RESTRICT` | মুছতেই দেয় না | Order — গ্রাহক মুছলেও ইতিহাস রাখতে হয় |
| `SET NULL` | `user_id` কে NULL করে দেয় | Optional সম্পর্ক |

> **সাবধান:** `CASCADE` নীরবে ডেটা মুছে ফেলে। একজন ব্যবহারকারী মুছলে তার ৫০০টা নোট এক নিমেষে চলে যাবে, কোনো সতর্কবার্তা ছাড়া। ব্যবহারকারীর ডেটা সংরক্ষণ জরুরি হলে soft delete ব্যবহার হয় (Lesson 15 এ দেখব)।

### `CREATE INDEX idx_notes_user_created ON notes(user_id, created_at DESC);`

এটা **composite index** (যৌগিক ইনডেক্স) — দুই column একসাথে।

আমাদের সবচেয়ে ঘন ঘন চলা query হবে:

```sql
SELECT * FROM notes WHERE user_id = 2 ORDER BY created_at DESC;
```

এই index টা ঠিক ওই কাজের জন্য বানানো:

```
Index ছাড়া:
  ১. ১ লাখ নোটের সব পড়ো
  ২. user_id = 2 বাছো
  ৩. created_at দিয়ে সাজাও  ← আলাদা করে sort, ব্যয়বহুল

Index সহ:
  ১. user_id = 2 এর কাছে সরাসরি লাফাও
  ২. ভিতরেই created_at DESC ক্রমে সাজানো আছে → সোজা পড়ে নাও
     ✅ কোনো sort করতে হলো না
```

column এর ক্রম গুরুত্বপূর্ণ — `(user_id, created_at)` কাজ করে, `(created_at, user_id)` করত না। নিয়ম: **আগে সমতা মেলানোর column (`=`), পরে সাজানোর column।**

---

## 💻 ধাপ ২ — API

### ফাইল ১ — `src/controllers/note.controller.js` (নতুন)

```js
const { query } = require('../config/db');

const createNote = async (req, res) => {
  try {
    const { title, content } = req.body;
    const userId = req.user.userId;

    if (!title || title.trim().length === 0) {
      return res.status(400).json({
        success: false,
        message: 'title is required',
      });
    }

    if (title.length > 200) {
      return res.status(400).json({
        success: false,
        message: 'title must be under 200 characters',
      });
    }

    const result = await query(
      `INSERT INTO notes (user_id, title, content)
       VALUES ($1, $2, $3)
       RETURNING id, title, content, created_at, updated_at`,
      [userId, title.trim(), content || '']
    );

    return res.status(201).json({
      success: true,
      message: 'Note created',
      data: result.rows[0],
    });
  } catch (error) {
    console.error('Create note error:', error);
    return res.status(500).json({
      success: false,
      message: 'Something went wrong',
    });
  }
};

module.exports = { createNote };
```

### ফাইল ২ — `src/routes/note.routes.js` (নতুন)

```js
const express = require('express');
const { createNote } = require('../controllers/note.controller');
const { authenticate } = require('../middlewares/auth.middleware');

const router = express.Router();

router.use(authenticate);          // 👈 এর নিচের সব route সুরক্ষিত

router.post('/', createNote);

module.exports = router;
```

### ফাইল ৩ — `server.js`

```js
const noteRoutes = require('./src/routes/note.routes');   // 👉 নতুন

app.use('/api/notes', noteRoutes);                        // 👉 নতুন
```

---

## 🔍 লাইন-বাই-লাইন

### `router.use(authenticate);` — এই এক লাইনের গুরুত্ব

```js
router.use(authenticate);        // এর নিচের সব route এ প্রযোজ্য

router.post('/', createNote);    // সুরক্ষিত ✅
router.get('/', getNotes);       // সুরক্ষিত ✅ (পরের lesson এ যোগ হবে)
```

প্রতিটা লাইনে `authenticate` লেখার চেয়ে এটা ভালো কারণ — **ভবিষ্যতে নতুন route যোগ করলে সেটা আপনাআপনি সুরক্ষিত থাকবে।** কেউ ভুলে গিয়ে API উন্মুক্ত করে ফেলতে পারবে না।

নিরাপত্তায় নিয়মটা হলো: **ডিফল্ট বন্ধ, ব্যতিক্রম খোলা** — উল্টোটা নয়।

---

### `const userId = req.user.userId;` — সবচেয়ে গুরুত্বপূর্ণ লাইন

```js
const userId = req.user.userId;     // ✅ token থেকে — জাল করা যায় না
```

```js
const userId = req.body.userId;     // ❌ কখনো না — ক্লায়েন্ট যা খুশি পাঠাবে
```

**দ্বিতীয়টা লিখলে কী হয়:**

```
আক্রমণকারী পাঠায়:
{ "title": "হ্যাক", "content": "...", "userId": 1 }

→ অন্য ব্যবহারকারীর অ্যাকাউন্টে নোট তৈরি হয়ে যাবে
→ ওই নোটে ক্ষতিকর লিংক দিলে ভুক্তভোগী বিশ্বাস করে ক্লিক করবে
```

`req.user.userId` জাল করতে হলে বৈধ signature সহ token বানাতে হবে — SECRET ছাড়া অসম্ভব।

> **এটাই authentication (তুমি কে?) আর authorization (তুমি কী করতে পারো?) এর সংযোগস্থল।** Middleware প্রথমটা করেছে, controller দ্বিতীয়টা প্রয়োগ করছে।

---

### `title.trim().length === 0`

```js
if (!title || title.trim().length === 0)
```

| চেক | কী ধরে |
|---|---|
| `!title` | `undefined`, `null`, `""` |
| `title.trim().length === 0` | `"   "` — শুধু space |

দ্বিতীয়টা না থাকলে `"   "` একটা বৈধ শিরোনাম হয়ে যাবে, আর অ্যাপে খালি নোট দেখাবে।

---

### `content || ''`

```js
[userId, title.trim(), content || '']
```

`content` না পাঠালে `undefined` যেত, আর pg সেটাকে `NULL` বানাত — কিন্তু আমাদের column এ `NOT NULL` আছে, তাই error হতো।

`|| ''` দিয়ে খালি string বসিয়ে দিলাম। ফলে শুধু শিরোনাম দিয়েও নোট বানানো যাবে।

---

## 🔄 Internal Flow

```
┌──────────────────────────────────────────────────────────────┐
│ ১. Postman                                                   │
│    POST /api/notes                                           │
│    Authorization: Bearer eyJ...                              │
│    { "title": "বাজারের তালিকা", "content": "চাল, ডাল" }        │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
        express.json() → req.body ভরল
                            ▼
        Router: /api/notes → note.routes
                            ▼
╔══════════════════════════════════════════════════════════════╗
║ ২. router.use(authenticate)                                  ║
║    token যাচাই ✅ → req.user = { userId: 2, ... }             ║
║    next()                                                    ║
╚═══════════════════════════╪══════════════════════════════════╝
                            ▼
┌──────────────────────────────────────────────────────────────┐
│ ৩. createNote controller                                     │
│    title = "বাজারের তালিকা"     (body থেকে)                   │
│    userId = 2                  (token থেকে) ← জাল করা যায় না │
│    validation পাস                                            │
└───────────────────────────┬──────────────────────────────────┘
                            ▼
╔══════════════════════════════════════════════════════════════╗
║ ৪. PostgreSQL                                                ║
║                                                              ║
║    INSERT INTO notes (user_id, title, content)               ║
║    VALUES ($1, $2, $3)                                       ║
║                                                              ║
║    ক) Foreign Key যাচাই:                                     ║
║       "users টেবিলে id = 2 আছে?"                             ║
║       → users_pkey index এ দেখল → আছে ✅                      ║
║       না থাকলে → error 23503 (foreign_key_violation)         ║
║                                                              ║
║    খ) notes_id_seq থেকে নতুন id নিল → 1                      ║
║    গ) created_at, updated_at এ NOW() বসাল                    ║
║    ঘ) row লিখল                                               ║
║    ঙ) দুটো index আপডেট করল                                   ║
║       (idx_notes_user_id, idx_notes_user_created)            ║
║    চ) RETURNING → column গুলো ফেরত                            ║
╚═══════════════════════════╪══════════════════════════════════╝
                            ▼
                201 Created + নোটের তথ্য → Postman
```

লক্ষ্য করো — `RETURNING` এ `user_id` রাখিনি। ক্লায়েন্ট তো জানেই এটা তার নিজের নোট, অকারণে ভিতরের id পাঠানোর দরকার নেই।

---

## 🧪 Postman Testing

### Test ১ — নোট তৈরি

```
POST http://localhost:5000/api/notes
Authorization: Bearer <token>

{ "title": "বাজারের তালিকা", "content": "চাল, ডাল, তেল" }
```

**201 Created:**

```json
{
  "success": true,
  "message": "Note created",
  "data": {
    "id": 1,
    "title": "বাজারের তালিকা",
    "content": "চাল, ডাল, তেল",
    "created_at": "2026-07-27T11:00:00.000Z",
    "updated_at": "2026-07-27T11:00:00.000Z"
  }
}
```

### Test ২ — Token ছাড়া

**401** — controller পর্যন্ত পৌঁছালই না ✅

### Test ৩ — শিরোনাম ছাড়া

```json
{ "content": "শুধু লেখা" }
```

**400 Bad Request**

### Test ৪ — userId জাল করার চেষ্টা

```json
{ "title": "হ্যাক করার চেষ্টা", "userId": 1 }
```

DB তে দেখো:

```sql
SELECT id, user_id, title FROM notes ORDER BY id DESC LIMIT 1;
```

```
 id | user_id |      title
----+---------+------------------
  2 |    2    | হ্যাক করার চেষ্টা
```

`user_id` = 2, তার পাঠানো 1 নয় ✅ — কারণ আমরা body এর `userId` ছুঁয়েও দেখিনি।

### Test ৫ — CASCADE কাজ করে কিনা (সাবধানে)

```sql
-- একটা পরীক্ষামূলক user আর তার নোট বানাও, তারপর:
DELETE FROM users WHERE email = 'test-cascade@mail.com';
SELECT * FROM notes WHERE user_id = <ওই user এর id>;
-- খালি — নোটগুলোও মুছে গেছে
```

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `req.body.userId` ব্যবহার | অন্যের নামে নোট বানানো যাবে | `req.user.userId` |
| Foreign key না দেওয়া | অনাথ নোট জমতে থাকবে | `REFERENCES users(id)` |
| `ON DELETE` ঠিক না করা | ব্যবহারকারী মুছতে গিয়ে error | ভেবে `CASCADE` বা `RESTRICT` |
| `router.use(authenticate)` route এর **পরে** | নিচের route গুলো অরক্ষিত | সবার উপরে |
| `content` এর fallback না দেওয়া | NOT NULL violation | `content \|\| ''` |
| index না বানানো | নোট বাড়লে তালিকা ধীর | user_id এ index |
| 200 ফেরত দেওয়া | REST নিয়মে নতুন সৃষ্টি = 201 | `res.status(201)` |

---

## 🏋️ Practice

**১.** ভাবো: `user_id` এ Foreign Key না দিলে কী কী ভুল ডেটা ঢুকতে পারত?

<details>
<summary>উত্তর</summary>

- `user_id = 9999` — এমন ব্যবহারকারী নেই, নোটটা চিরকাল অদৃশ্য থাকবে
- ব্যবহারকারী মুছে গেলে তার নোটগুলো থেকে যাবে, কেউ কখনো দেখবে না, শুধু জায়গা খাবে
- `SELECT` এ join করলে অদ্ভুত ফলাফল আসবে

Foreign Key হলো database এর নিজের হাতে ধরা নিয়ম — কোড যত ভুলই করুক, ভুল সম্পর্ক তৈরি হতে দেবে না।
</details>

**২.** ভাবো: দুটো index বানালাম — `(user_id)` আর `(user_id, created_at DESC)`. প্রথমটা কি অপ্রয়োজনীয়?

<details>
<summary>উত্তর</summary>

প্রায় হ্যাঁ। PostgreSQL যৌগিক index এর **বাঁ দিকের অংশ** আলাদাভাবেও ব্যবহার করতে পারে — তাই `(user_id, created_at)` index টা `WHERE user_id = 2` এর জন্যও কাজ করে।

তাহলে প্রথম index টা রাখার একমাত্র কারণ হতে পারে — এটা ছোট, তাই কিছু ক্ষেত্রে সামান্য দ্রুত। বাস্তব প্রজেক্টে আমি এটা বাদ দিতাম।

শিক্ষা: **অতিরিক্ত index শুধু জায়গা নেয় না, প্রতিটা INSERT/UPDATE কেও ধীর করে।** কোন index সত্যি কাজে লাগছে তা `EXPLAIN ANALYZE` দিয়ে দেখা যায়।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-13" name="lesson-13"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📖 Lesson 13 — Read Notes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■□□□□□□□□□]  13/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 12 (নোট তৈরি হচ্ছে) |
| **এই ধাপ শেষে** | তালিকা আর একক নোট — দুটোই পড়া যাবে |
| **নতুন শব্দ** | route parameter, ORDER BY, 404 vs 403, ownership check |

---

## 🎯 Goal

```
GET /api/notes       →  আমার সব নোট
GET /api/notes/:id   →  আমার একটা নির্দিষ্ট নোট
```

---

## 💻 Code

### `src/controllers/note.controller.js` এ যোগ করো

```js
const getNotes = async (req, res) => {
  try {
    const userId = req.user.userId;

    const result = await query(
      `SELECT id, title, content, created_at, updated_at
       FROM notes
       WHERE user_id = $1
       ORDER BY created_at DESC`,
      [userId]
    );

    return res.status(200).json({
      success: true,
      count: result.rows.length,
      data: result.rows,
    });
  } catch (error) {
    console.error('Get notes error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};

const getNoteById = async (req, res) => {
  try {
    const userId = req.user.userId;
    const noteId = Number(req.params.id);

    if (!Number.isInteger(noteId) || noteId <= 0) {
      return res.status(400).json({
        success: false,
        message: 'Invalid note id',
      });
    }

    const result = await query(
      `SELECT id, title, content, created_at, updated_at
       FROM notes
       WHERE id = $1 AND user_id = $2`,
      [noteId, userId]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({
        success: false,
        message: 'Note not found',
      });
    }

    return res.status(200).json({
      success: true,
      data: result.rows[0],
    });
  } catch (error) {
    console.error('Get note error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};

module.exports = { createNote, getNotes, getNoteById };
```

### `src/routes/note.routes.js`

```js
router.post('/', createNote);
router.get('/', getNotes);           // 👉 নতুন
router.get('/:id', getNoteById);     // 👉 নতুন
```

---

## 🔍 লাইন-বাই-লাইন

### `WHERE user_id = $1` — এই শর্তটাই পুরো নিরাপত্তা

```sql
SELECT ... FROM notes WHERE user_id = $1
```

এই একটা শর্ত না থাকলে **প্রত্যেকে সবার নোট দেখতে পেত**।

```
WHERE ছাড়া:  SELECT * FROM notes
             → পৃথিবীর সব ব্যবহারকারীর সব নোট 😱

WHERE সহ:    SELECT * FROM notes WHERE user_id = 2
             → শুধু Rana এর নোট ✅
```

আর `$1` আসছে `req.user.userId` থেকে — অর্থাৎ token থেকে। শৃঙ্খলটা এরকম:

```
Token (স্বাক্ষরিত, জাল করা যায় না)
   ↓
req.user.userId  (middleware বসিয়েছে)
   ↓
SQL এর WHERE শর্ত
   ↓
শুধু নিজের ডেটা ফেরত আসে
```

---

### `ORDER BY created_at DESC`

| অংশ | মানে |
|---|---|
| `ORDER BY created_at` | তৈরির সময় অনুযায়ী সাজাও |
| `DESC` | descending — নতুন আগে |
| `ASC` (ডিফল্ট) | ascending — পুরনো আগে |

| না দিলে | PostgreSQL **কোনো ক্রমের নিশ্চয়তা দেয় না**। আজ হয়তো ঠিক ক্রমে আসবে, কিন্তু row আপডেট হলে বা VACUUM চললে ক্রম বদলে যাবে। ফলে Flutter এ তালিকা এলোমেলো লাফাবে। **তালিকা ফেরত দিলে সবসময় `ORDER BY` দাও** |

আর আমাদের `idx_notes_user_created` index টা ঠিক এই ক্রমেই সাজানো — তাই আলাদা করে sort করতেই হয় না।

---

### `req.params.id` — Route Parameter

```js
router.get('/:id', getNoteById);
                │
                └── এখানে যা-ই আসুক, req.params.id তে ঢুকবে
```

```
GET /api/notes/5    →  req.params.id === "5"   ← লক্ষ্য করো, string!
GET /api/notes/abc  →  req.params.id === "abc"
```

Express সবসময় **string** দেয়, কারণ URL এ সবই text।

**তিন ধরনের ইনপুট গুলিয়ে ফেলো না:**

| উৎস | কোথা থেকে | উদাহরণ |
|---|---|---|
| `req.params` | URL এর পথ | `/notes/5` → `{ id: "5" }` |
| `req.query` | প্রশ্নচিহ্নের পরে | `/notes?page=2` → `{ page: "2" }` |
| `req.body` | Request এর দেহ | `{ "title": "..." }` |

---

### `Number(req.params.id)` আর যাচাই

```js
const noteId = Number(req.params.id);

if (!Number.isInteger(noteId) || noteId <= 0) {
  return res.status(400).json({ success: false, message: 'Invalid note id' });
}
```

| ইনপুট | `Number()` এর ফল | ধরা পড়ে? |
|---|---|---|
| `"5"` | `5` | ✅ পাস |
| `"abc"` | `NaN` | ✅ 400 |
| `"5.5"` | `5.5` | ✅ 400 (পূর্ণসংখ্যা নয়) |
| `"-1"` | `-1` | ✅ 400 |

| এই যাচাই না করলে | `"abc"` সরাসরি PostgreSQL এ যেত → `invalid input syntax for type integer` (error 22P02) → 500 Internal Server Error। অথচ দোষটা ক্লায়েন্টের, উত্তর হওয়া উচিত 400 |

---

### `WHERE id = $1 AND user_id = $2` — দুটো শর্ত একসাথে কেন

```sql
WHERE id = $1 AND user_id = $2
```

এক ধাপে দুটো প্রশ্নের উত্তর হয়ে যায়:

```
১. এই id এর নোট আছে কি?
২. সেটা কি এই ব্যবহারকারীর?
```

**বিকল্প (খারাপ) পদ্ধতি:**

```js
// ❌ দুই ধাপে
const note = await query('SELECT * FROM notes WHERE id = $1', [noteId]);
if (note.rows[0].user_id !== userId) return res.status(403)...
```

সমস্যা: দুইবার কাজ, আর ভুলে যাওয়ার সুযোগ থাকে। এক query তে দুটো শর্ত দিলে ভুল করার উপায়ই থাকে না।

### 🤔 অন্যের নোট চাইলে 404 না 403?

```
ব্যবহারকারী ২ চাইল নোট ৭, যেটা আসলে ব্যবহারকারী ১ এর
```

| উত্তর | বার্তা যা বলে | সমস্যা |
|---|---|---|
| `403 Forbidden` | "নোটটা আছে, কিন্তু তোমার নয়" | ফাঁস — সে জেনে গেল ৭ নম্বর নোট বিদ্যমান। id বাড়িয়ে বাড়িয়ে সে মোট কতগুলো নোট আছে গুনে ফেলতে পারবে |
| **`404 Not Found`** | **"এমন কিছু নেই"** | **কোনো তথ্য ফাঁস হয় না ✅** |

আমাদের `WHERE id = $1 AND user_id = $2` স্বাভাবিকভাবেই 404 দেয় — কারণ শর্ত মেলে না, তাই row আসে না। **নিরাপদ আচরণটা এখানে কোডের গঠন থেকেই বেরিয়ে আসছে**, আলাদা করে ভাবতে হচ্ছে না। ভালো ডিজাইন এমনই হয়।

---

### ⚠️ Route এর ক্রম — একটা ফাঁদ

```js
router.get('/', getNotes);
router.get('/:id', getNoteById);
```

`:id` একটা wildcard — যেকোনো কিছু ধরে ফেলে। তাই ভবিষ্যতে যদি লেখো:

```js
router.get('/:id', getNoteById);
router.get('/search', searchNotes);    // ❌ কখনো চলবে না!
```

`GET /api/notes/search` এলে Express প্রথমে `/:id` এ মিল পাবে, `id = "search"` ধরে নেবে।

**নিয়ম: নির্দিষ্ট path সবসময় wildcard এর উপরে।**

```js
router.get('/search', searchNotes);   // ✅ আগে
router.get('/:id', getNoteById);      // ✅ পরে
```

---

## 🔄 Internal Flow

```
GET /api/notes/3  +  Bearer token
        │
        ▼
express.json() → Router (/api/notes) → note.routes
        │
        ▼
router.use(authenticate) → token ✅ → req.user = {userId: 2}
        │
        ▼
router.get('/:id') মিলল → req.params = { id: "3" }
        │
        ▼
Controller:
   noteId = Number("3") = 3 ✅
   userId = 2 (token থেকে)
        │
        ▼
╔══════════════════════════════════════════════════════════╗
║ PostgreSQL                                               ║
║                                                          ║
║ SELECT ... WHERE id = 3 AND user_id = 2                  ║
║                                                          ║
║  Planner ভাবল:                                           ║
║   "id হলো PRIMARY KEY → notes_pkey index এ সরাসরি যাই"    ║
║   → row পেলাম                                            ║
║   → এখন user_id = 2 কিনা দেখি                            ║
║                                                          ║
║  মেলে   → ১ সারি ফেরত                                    ║
║  মেলে না → ০ সারি ফেরত  (নোটটা অন্যের)                    ║
╚══════════════════════╪═══════════════════════════════════╝
                       ▼
       rows.length === 0 ?  →  404 Note not found
       নাহলে               →  200 + নোট
```

---

## 🧪 Postman Testing

### Test ১ — সব নোট

```
GET http://localhost:5000/api/notes
Authorization: Bearer <token>
```

```json
{
  "success": true,
  "count": 2,
  "data": [
    { "id": 2, "title": "মিটিং", "content": "১০টায়", "created_at": "...", "updated_at": "..." },
    { "id": 1, "title": "বাজারের তালিকা", "content": "চাল, ডাল", "created_at": "...", "updated_at": "..." }
  ]
}
```

নতুন নোট আগে — `ORDER BY created_at DESC` কাজ করছে ✅

### Test ২ — একটা নোট

```
GET http://localhost:5000/api/notes/1
```

**200 OK** — একটা object (array নয়)।

### Test ৩ — অন্যের নোট (এটাই আসল পরীক্ষা)

1. দ্বিতীয় একটা অ্যাকাউন্ট বানাও, তার token নাও
2. ওই token দিয়ে `GET /api/notes/1` চাও (নোটটা প্রথম ব্যবহারকারীর)

**404 Not Found** ✅ — মালিকানা সুরক্ষিত

### Test ৪ — নেই এমন নোট

```
GET http://localhost:5000/api/notes/9999
```

**404** — একই বার্তা। বাইরে থেকে "নেই" আর "তোমার নয়" এর পার্থক্য বোঝার উপায় নেই ✅

### Test ৫ — অক্ষরযুক্ত id

```
GET http://localhost:5000/api/notes/abc
```

**400 Bad Request** (500 নয় ✅)

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `WHERE user_id` বাদ | সবাই সবার নোট দেখবে | কখনো বাদ দিও না |
| `ORDER BY` না দেওয়া | তালিকার ক্রম অনির্দেশ্য | সবসময় দাও |
| id যাচাই না করা | 500 error | `Number.isInteger` |
| অন্যের নোটে 403 | নোটের অস্তিত্ব ফাঁস | 404 |
| একক নোটে array ফেরত | Flutter এ parse ভাঙে | `rows[0]` |
| `/:id` কে `/search` এর উপরে রাখা | search কখনো চলবে না | নির্দিষ্ট আগে |
| খালি তালিকায় 404 | "কোনো নোট নেই" ≠ error | `200` + `data: []` |

---

## 🏋️ Practice

**১.** ব্যবহারকারীর কোনো নোট না থাকলে কী ফেরত দেওয়া উচিত — 404 নাকি 200 + খালি array?

<details>
<summary>উত্তর</summary>

**200 + `data: []`**

কারণ `/api/notes` মানে "আমার নোটের সংগ্রহ" — সংগ্রহটা বিদ্যমান, শুধু খালি। খালি ঘর আর ঘর না থাকা এক জিনিস নয়।

Flutter এও এটা সহজ করে দেয়:

```dart
// 200 + [] হলে:
if (notes.isEmpty) showEmptyState();     // সরল

// 404 হলে:
// error handling এর ভিতরে গিয়ে "এটা কি আসল error না খালি তালিকা?" বুঝতে হতো
```

404 প্রযোজ্য হয় **একক জিনিসের** ক্ষেত্রে — `/api/notes/9999` এ, তালিকায় নয়।
</details>

**২.** ভাবো: `SELECT` এ `user_id` column টা ফেরত দিই না। Flutter এর কি ওটা দরকার হতে পারে?

<details>
<summary>উত্তর</summary>

সাধারণত না — ব্যবহারকারী তো জানেই এগুলো তার নিজের নোট, প্রতিটা নোটে নিজের id দেখার দরকার নেই।

তবে ভবিষ্যতে যদি "শেয়ার করা নোট" ফিচার আসে, তখন কোন নোট কার সেটা দেখাতে হবে — তখন `user_id` বা বরং লেখকের নামটা লাগবে।

নিয়ম: **এখন যা দরকার তাই পাঠাও।** কম ডেটা = দ্রুত response + কম ফাঁসের ঝুঁকি।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-14" name="lesson-14"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✏️ Lesson 14 — Update Note
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■□□□□□□□□]  14/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 13 |
| **এই ধাপ শেষে** | `PATCH /api/notes/:id` কাজ করবে |
| **নতুন শব্দ** | UPDATE, SET, PUT vs PATCH, COALESCE, rowCount |

---

## 🎯 Goal

নোট সম্পাদনার API। শুধু যে ফিল্ডটা পাঠানো হয়েছে সেটাই বদলাবে।

---

## 🤔 PUT না PATCH?

| | PUT | PATCH |
|---|---|---|
| অর্থ | পুরো জিনিসটা **প্রতিস্থাপন** করো | **আংশিক** বদলাও |
| না পাঠানো ফিল্ড | মুছে যাবে / খালি হবে | অপরিবর্তিত থাকবে |
| উদাহরণ | `{title}` পাঠালে content মুছে যাবে | `{title}` পাঠালে content থাকবে |

মোবাইল অ্যাপের জন্য **PATCH** ই বাস্তবসম্মত — ব্যবহারকারী শুধু শিরোনাম বদলাতে চাইলে পুরো নোট আবার পাঠাতে বাধ্য করা অর্থহীন।

---

## 💻 Code

```js
const updateNote = async (req, res) => {
  try {
    const userId = req.user.userId;
    const noteId = Number(req.params.id);
    const { title, content } = req.body;

    if (!Number.isInteger(noteId) || noteId <= 0) {
      return res.status(400).json({ success: false, message: 'Invalid note id' });
    }

    if (title === undefined && content === undefined) {
      return res.status(400).json({
        success: false,
        message: 'Nothing to update. Send title or content',
      });
    }

    if (title !== undefined && title.trim().length === 0) {
      return res.status(400).json({ success: false, message: 'title cannot be empty' });
    }

    const result = await query(
      `UPDATE notes
       SET title      = COALESCE($1, title),
           content    = COALESCE($2, content),
           updated_at = NOW()
       WHERE id = $3 AND user_id = $4
       RETURNING id, title, content, created_at, updated_at`,
      [
        title !== undefined ? title.trim() : null,
        content !== undefined ? content : null,
        noteId,
        userId,
      ]
    );

    if (result.rowCount === 0) {
      return res.status(404).json({ success: false, message: 'Note not found' });
    }

    return res.status(200).json({
      success: true,
      message: 'Note updated',
      data: result.rows[0],
    });
  } catch (error) {
    console.error('Update note error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};

module.exports = { createNote, getNotes, getNoteById, updateNote };
```

```js
// route
router.patch('/:id', updateNote);
```

---

## 🔍 লাইন-বাই-লাইন

### SQL — `UPDATE ... SET ... WHERE`

```sql
UPDATE notes
SET title = COALESCE($1, title),
    content = COALESCE($2, content),
    updated_at = NOW()
WHERE id = $3 AND user_id = $4
RETURNING ...
```

| অংশ | মানে |
|---|---|
| `UPDATE notes` | কোন টেবিল বদলাব |
| `SET column = মান` | কোন column কী হবে |
| `WHERE` | **কোন row গুলো** |
| `RETURNING` | বদলানোর পর নতুন অবস্থা ফেরত দাও |

> 🚨 **`WHERE` ছাড়া `UPDATE` লিখলে টেবিলের প্রতিটা row বদলে যাবে।** সব ব্যবহারকারীর সব নোটের শিরোনাম এক হয়ে যাবে। এটা এমন ভুল যা প্রতি বছর কোনো না কোনো কোম্পানির প্রোডাকশনে ঘটে। psql এ হাতে UPDATE লেখার আগে সবসময় প্রথমে একই `WHERE` দিয়ে `SELECT` চালিয়ে দেখো কয়টা row আসছে।

---

### `COALESCE($1, title)` — চতুর কৌশলটা

**`COALESCE`** = প্রথম non-NULL মানটা নাও।

```sql
COALESCE(NULL, 'পুরনো')     →  'পুরনো'
COALESCE('নতুন', 'পুরনো')   →  'নতুন'
```

আমাদের ক্ষেত্রে:

```
title পাঠানো হয়েছে   →  $1 = 'নতুন শিরোনাম'  →  COALESCE = 'নতুন শিরোনাম'  (বদলাল)
title পাঠানো হয়নি    →  $1 = NULL           →  COALESCE = title           (অপরিবর্তিত)
```

এভাবে **একটা মাত্র query দিয়েই PATCH এর আচরণ** পাওয়া গেল। নাহলে লিখতে হতো:

```js
// ❌ এই পথে গেলে জটিল হয়ে যায়
if (title && content)   sql = 'UPDATE ... SET title=$1, content=$2 ...';
else if (title)         sql = 'UPDATE ... SET title=$1 ...';
else if (content)       sql = 'UPDATE ... SET content=$1 ...';
```

৫টা ফিল্ড হলে ৩২টা সমন্বয় — অসম্ভব।

> **COALESCE এর একটা সীমা:** এভাবে কোনো ফিল্ডকে ইচ্ছা করে `NULL` করা যায় না, কারণ NULL মানেই "বদলিও না"। আমাদের কোনো column NULL হয় না, তাই সমস্যা নেই। যেখানে দরকার, সেখানে dynamic query বানাতে হয়।

---

### `title !== undefined ? title.trim() : null`

```js
title !== undefined ? title.trim() : null
```

JavaScript এর `undefined` কে SQL এর `NULL` এ রূপান্তর করছি।

**কেন `!title` নয়, `title !== undefined`?**

```
title = ""        →  !title সত্য       →  ভুল করে "বদলিও না" ধরে নিত
title = undefined →  !title সত্য       →  ঠিক
```

খালি string আর "পাঠানোই হয়নি" — এই দুটো আলাদা জিনিস। `!==  undefined` সেটা সঠিকভাবে আলাদা করে।

---

### `updated_at = NOW()`

মনে আছে Lesson 06 এ বলেছিলাম — `DEFAULT NOW()` শুধু `INSERT` এ কাজ করে? তাই `UPDATE` এ হাতে লিখতে হচ্ছে।

| না লিখলে | `updated_at` চিরকাল তৈরির সময়েই আটকে থাকবে। Flutter এ "সর্বশেষ সম্পাদনা" ভুল দেখাবে, আর ভবিষ্যতে sync ফিচার বানালে সেটা ভাঙবে |

---

### `result.rowCount === 0`

| ফিল্ড | UPDATE এর ক্ষেত্রে |
|---|---|
| `rowCount` | কয়টা row বদলাল |
| `rows` | `RETURNING` এর কারণে বদলানো row গুলো |

`rowCount === 0` মানে কোনো row মেলেনি — হয় নোটটা নেই, নয় অন্যের। দুই ক্ষেত্রেই **404**, কারণ Lesson 13 এর যুক্তি এখানেও খাটে।

---

## 🔄 Internal Flow — PostgreSQL এর ভিতরে UPDATE

```
PATCH /api/notes/1  { "title": "হালনাগাদ তালিকা" }
        │
        ▼
authenticate → req.user.userId = 2
        │
        ▼
Controller:
   title = "হালনাগাদ তালিকা"  → $1
   content = undefined       → $2 = null
   noteId = 1                → $3
   userId = 2                → $4
        │
        ▼
╔══════════════════════════════════════════════════════════════╗
║ PostgreSQL                                                   ║
║                                                              ║
║ ১. WHERE id=1 AND user_id=2 → notes_pkey দিয়ে row খুঁজল      ║
║                                                              ║
║ ২. COALESCE হিসাব করল:                                       ║
║      title   = COALESCE('হালনাগাদ তালিকা', 'পুরনো') = নতুনটা  ║
║      content = COALESCE(NULL, 'চাল, ডাল')          = পুরনোটা ║
║                                                              ║
║ ৩. MVCC — এখানে একটা মজার ব্যাপার:                            ║
║      PostgreSQL পুরনো row টা জায়গায় বদলায় না।                ║
║      নতুন একটা row লেখে, পুরনোটাকে "মৃত" চিহ্নিত করে।         ║
║      (তাই পুরনো transaction গুলো এখনো পুরনো ডেটা দেখতে পায়)  ║
║      মৃত row গুলো পরে VACUUM এসে পরিষ্কার করে।                ║
║                                                              ║
║ ৪. index গুলো আপডেট করল                                       ║
║ ৫. WAL এ লিখল (দুর্ঘটনায় ডেটা বাঁচানোর জন্য)                  ║
║ ৬. RETURNING → নতুন অবস্থা ফেরত                               ║
╚══════════════════════╪═══════════════════════════════════════╝
                       ▼
              200 OK + হালনাগাদ নোট
```

---

## 🧪 Postman Testing

### Test ১ — শুধু শিরোনাম বদলাও

```
PATCH http://localhost:5000/api/notes/1
Authorization: Bearer <token>

{ "title": "হালনাগাদ বাজারের তালিকা" }
```

```json
{
  "success": true,
  "message": "Note updated",
  "data": {
    "id": 1,
    "title": "হালনাগাদ বাজারের তালিকা",
    "content": "চাল, ডাল, তেল",          ← অপরিবর্তিত ✅
    "created_at": "2026-07-27T11:00:00.000Z",
    "updated_at": "2026-07-27T11:45:00.000Z"   ← বদলেছে ✅
  }
}
```

`content` পাঠাইনি, তবু টিকে আছে — **COALESCE কাজ করছে** ✅

### Test ২ — অন্যের নোট বদলানোর চেষ্টা

দ্বিতীয় অ্যাকাউন্টের token দিয়ে `PATCH /api/notes/1`

**404** ✅ — মালিকানা সুরক্ষিত

### Test ৩ — খালি body

```json
{}
```

**400** — "Nothing to update"

### Test ৪ — খালি শিরোনাম

```json
{ "title": "   " }
```

**400** — "title cannot be empty"

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `WHERE` ছাড়া UPDATE | **সব row বদলে যাবে** | কখনো ভুলো না |
| `WHERE` এ `user_id` বাদ | যে কেউ অন্যের নোট বদলাবে | দুটো শর্তই |
| `updated_at` না বদলানো | ভুল সময় দেখাবে | `NOW()` লেখো |
| `!title` দিয়ে চেক | খালি string আর অনুপস্থিত গুলিয়ে যাবে | `!== undefined` |
| `rowCount` না দেখা | নেই এমন নোটেও "সফল" বলবে | চেক করো |
| PATCH এর জায়গায় PUT | না পাঠানো ফিল্ড মুছে যাবে | PATCH |

---

## 🏋️ Practice

**১.** ভাবো: `COALESCE` এর বদলে `SET title = $1` লিখলে, আর ব্যবহারকারী শুধু `content` পাঠালে কী হবে?

<details>
<summary>উত্তর</summary>

`title` হয়ে যাবে `NULL`। কিন্তু আমাদের column এ `NOT NULL` আছে, তাই PostgreSQL error দেবে (23502) → 500।

`NOT NULL` না থাকলে আরও খারাপ হতো — শিরোনাম নীরবে মুছে যেত, ব্যবহারকারী শুধু লেখা সম্পাদনা করতে গিয়ে শিরোনাম হারাত।

এটাই PUT আর PATCH এর আসল পার্থক্য, বাস্তব রূপে।
</details>

**২.** দুজন ব্যবহারকারী (বা একই ব্যবহারকারীর দুই ডিভাইস) একই নোট একই সময়ে সম্পাদনা করলে?

<details>
<summary>উত্তর</summary>

শেষে যে লিখবে সে জিতবে — **last write wins**। প্রথমজনের সম্পাদনা নীরবে হারিয়ে যাবে।

সমাধানের পথ:
1. **Optimistic locking** — একটা `version` column রাখো, `WHERE id=$1 AND version=$2` দিয়ে আপডেট করো। version না মিললে 409 Conflict দাও ("অন্য কেউ এটা বদলেছে")
2. **updated_at মিলিয়ে দেখা** — একই ধারণা, timestamp দিয়ে

শেখার প্রজেক্টে দরকার নেই, কিন্তু সহযোগিতামূলক (collaborative) অ্যাপে অপরিহার্য।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-15" name="lesson-15"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗑️ Lesson 15 — Delete Note
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■□□□□□□□]  15/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 14 |
| **এই ধাপ শেষে** | CRUD সম্পূর্ণ |
| **নতুন শব্দ** | DELETE, hard vs soft delete, idempotency |

---

## 💻 Code

```js
const deleteNote = async (req, res) => {
  try {
    const userId = req.user.userId;
    const noteId = Number(req.params.id);

    if (!Number.isInteger(noteId) || noteId <= 0) {
      return res.status(400).json({ success: false, message: 'Invalid note id' });
    }

    const result = await query(
      `DELETE FROM notes
       WHERE id = $1 AND user_id = $2
       RETURNING id`,
      [noteId, userId]
    );

    if (result.rowCount === 0) {
      return res.status(404).json({ success: false, message: 'Note not found' });
    }

    return res.status(200).json({
      success: true,
      message: 'Note deleted',
      data: { id: result.rows[0].id },
    });
  } catch (error) {
    console.error('Delete note error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};

module.exports = { createNote, getNotes, getNoteById, updateNote, deleteNote };
```

```js
// route
router.delete('/:id', deleteNote);
```

---

## 🔍 লাইন-বাই-লাইন

### `DELETE FROM notes WHERE id = $1 AND user_id = $2`

সবচেয়ে বিপজ্জনক SQL, কারণ ফেরার পথ নেই।

```sql
DELETE FROM notes;                      -- 💀 সব নোট শেষ
DELETE FROM notes WHERE id = 5;         -- 💀 অন্যের নোটও মুছে যেতে পারে
DELETE FROM notes WHERE id=$1 AND user_id=$2;  -- ✅ শুধু নিজেরটা
```

> **অভ্যাস করো:** psql এ `DELETE` লেখার আগে সবসময় একই `WHERE` দিয়ে `SELECT` চালাও। যা দেখবে, ঠিক তা-ই মুছবে।

### `RETURNING id`

মুছে ফেলা row এর id ফেরত দেয়। কাজে লাগে —
- ক্লায়েন্টকে নিশ্চিত করতে ঠিক কোনটা মুছল
- `rowCount` এর সাথে মিলিয়ে দেখতে

### `result.rowCount === 0` → 404

কিছু মুছল না মানে হয় নোটটা নেই, নয় অন্যের। **404** — Lesson 13 এর একই যুক্তি।

---

## 🤔 Hard Delete vs Soft Delete

আমরা যেটা করলাম সেটা **hard delete** — সত্যিই মুছে গেল।

**Soft delete** হলো মুছে ফেলার ভান করা:

```sql
ALTER TABLE notes ADD COLUMN deleted_at TIMESTAMPTZ;

-- মুছে ফেলা:
UPDATE notes SET deleted_at = NOW() WHERE id=$1 AND user_id=$2;

-- পড়ার সময় লুকানো:
SELECT ... FROM notes WHERE user_id = $1 AND deleted_at IS NULL;
```

| | Hard Delete | Soft Delete |
|---|---|---|
| ডেটা | সত্যিই যায় | থেকে যায়, লুকানো থাকে |
| ফেরানো যায়? | ❌ (backup ছাড়া) | ✅ "Trash" ফিচার |
| জায়গা | মুক্ত হয় | দখল থাকতেই থাকে |
| প্রতিটা query | সরল | **প্রতিবার `deleted_at IS NULL` লিখতে হবে** |
| ভুলে গেলে | — | মুছে ফেলা জিনিস আবার দেখা যাবে 😱 |

**কোনটা কখন:**

```
Hard delete  →  ব্যবহারকারী নিজে মুছছে, ফেরানোর দরকার নেই
Soft delete  →  Trash/Undo ফিচার আছে
                অথবা আইনি কারণে ইতিহাস রাখতে হয় (আর্থিক লেনদেন)
```

শেখার প্রজেক্টে hard delete ই ঠিক আছে। বাস্তব নোট অ্যাপে (Google Keep এর মতো) soft delete ব্যবহার হয় — "Trash এ ৩০ দিন থাকবে"।

---

## ♻️ Idempotency — একটা সূক্ষ্ম ধারণা

**Idempotent (আইডেমপোটেন্ট)** = একবার করো বা দশবার করো, ফলাফল এক।

```
DELETE /api/notes/5   →  ২০০ (মুছল)
DELETE /api/notes/5   →  ৪০৪ (আর নেই)
```

**অবস্থার দিক থেকে idempotent** — নোটটা নেই, দুবারই। কিন্তু status code আলাদা।

মোবাইল অ্যাপে এটা বাস্তব সমস্যা: নেটওয়ার্ক খারাপ থাকায় request পাঠানো হলো, উত্তর আসার আগেই retry হলো। প্রথমটা সফল, দ্বিতীয়টা 404 পেল — ব্যবহারকারী "নোট পাওয়া যায়নি" error দেখল, অথচ কাজটা হয়ে গেছে।

**Flutter এ সমাধান:** delete এর ক্ষেত্রে 404 কেও সাফল্য ধরে নাও —

```dart
if (res.statusCode == 200 || res.statusCode == 404) {
  removeNoteFromList(id);   // দুই ক্ষেত্রেই নোটটা আর নেই
}
```

---

## 🔄 Internal Flow

```
DELETE /api/notes/1  +  Bearer token
        │
        ▼
authenticate → req.user.userId = 2
        │
        ▼
╔══════════════════════════════════════════════════════════╗
║ PostgreSQL                                               ║
║                                                          ║
║ DELETE FROM notes WHERE id=1 AND user_id=2               ║
║                                                          ║
║ ১. notes_pkey দিয়ে row খুঁজল                              ║
║ ২. user_id মিলিয়ে দেখল ✅                                 ║
║ ৩. row টাকে "মৃত" চিহ্নিত করল                             ║
║    (এখনই disk থেকে মোছে না — MVCC)                        ║
║ ৪. index থেকে entry সরাল                                  ║
║ ৫. WAL এ লিখল                                            ║
║ ৬. RETURNING id → 1                                      ║
║                                                          ║
║ 🧹 পরে VACUUM এসে জায়গাটা সত্যিই মুক্ত করবে                ║
╚══════════════════════╪═══════════════════════════════════╝
                       ▼
                200 OK { id: 1 }
```

---

## 🧪 Postman Testing

| Test | Request | ফল |
|---|---|---|
| ১ | `DELETE /api/notes/1` নিজের token | **200** — মুছল |
| ২ | আবার একই request | **404** — আর নেই |
| ৩ | অন্যের নোট মুছতে চেষ্টা | **404** — সুরক্ষিত ✅ |
| ৪ | Token ছাড়া | **401** |
| ৫ | `GET /api/notes` | মুছে যাওয়া নোট তালিকায় নেই ✅ |

---

## 🎉 CRUD সম্পূর্ণ

```
POST   /api/notes       ✅  তৈরি
GET    /api/notes       ✅  তালিকা
GET    /api/notes/:id   ✅  একটা
PATCH  /api/notes/:id   ✅  সম্পাদনা
DELETE /api/notes/:id   ✅  মুছে ফেলা
```

**এই পাঁচটা API দিয়ে তুমি এখনই একটা Flutter নোট অ্যাপ বানিয়ে ফেলতে পারো।** বাকি lesson গুলো এটাকে বাস্তবের চাপ সামলানোর যোগ্য করে তুলবে।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `WHERE` ছাড়া DELETE | **পুরো টেবিল খালি** | কখনো না |
| `user_id` শর্ত বাদ | যে কেউ অন্যের নোট মুছবে | দুটো শর্ত |
| `rowCount` না দেখা | কিছু না মুছেও "সফল" | চেক করো |
| Soft delete করে `deleted_at IS NULL` ভুলে যাওয়া | মুছে ফেলা নোট ফিরে আসবে | প্রতিটা query তে |
| DELETE এ body আশা করা | অনেক ক্লায়েন্ট DELETE এ body পাঠায় না | URL এ id |

---

## 🏋️ Practice

**১.** ব্যবহারকারী নিজের অ্যাকাউন্ট মুছলে তার নোটগুলোর কী হবে?

<details>
<summary>উত্তর</summary>

সব মুছে যাবে — `ON DELETE CASCADE` এর কারণে (Lesson 12)।

```sql
DELETE FROM users WHERE id = 2;
-- PostgreSQL নিজে থেকে চালায়:
-- DELETE FROM notes WHERE user_id = 2;
```

এটা সুবিধা এবং বিপদ দুটোই। বাস্তব অ্যাপে তাই সাধারণত:
- ব্যবহারকারীকে সতর্ক করা হয় ("সব ডেটা মুছে যাবে")
- আগে ডেটা রপ্তানির সুযোগ দেওয়া হয় (GDPR এর দাবি)
- অ্যাকাউন্ট soft delete করে ৩০ দিন রাখা হয়, তারপর সত্যিই মোছা হয়
</details>

**২.** ভাবো: `RETURNING id` না লিখে শুধু `rowCount` দেখলে কি চলত?

<details>
<summary>উত্তর</summary>

চলত — `rowCount` ই যথেষ্ট বলে দেয় কিছু মুছেছে কিনা।

`RETURNING` রাখলাম কারণ response এ id টা ফেরত দিলে Flutter এর কাজ সহজ হয় (কোন নোটটা তালিকা থেকে সরাবে, নিশ্চিত হওয়া যায়) — বিশেষত যখন একসাথে কয়েকটা delete চলছে।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-16" name="lesson-16"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔎 Lesson 16 — Search Notes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■□□□□□□]  16/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 15 (CRUD সম্পূর্ণ) |
| **এই ধাপ শেষে** | `GET /api/notes?search=বাজার` কাজ করবে |
| **নতুন শব্দ** | query parameter, LIKE, ILIKE, wildcard, dynamic query |

---

## 🎯 Goal

শিরোনাম বা লেখার ভিতরে খুঁজে নোট বের করা। নতুন কোনো route নয় — বিদ্যমান `GET /api/notes` কেই ক্ষমতা দেব।

---

## 💻 Code

`getNotes` কে বদলে দাও:

```js
const getNotes = async (req, res) => {
  try {
    const userId = req.user.userId;
    const search = (req.query.search || '').trim();

    let sql = `
      SELECT id, title, content, created_at, updated_at
      FROM notes
      WHERE user_id = $1
    `;
    const params = [userId];

    if (search) {
      sql += ` AND (title ILIKE $2 OR content ILIKE $2)`;
      params.push(`%${search}%`);
    }

    sql += ` ORDER BY created_at DESC`;

    const result = await query(sql, params);

    return res.status(200).json({
      success: true,
      count: result.rows.length,
      search: search || null,
      data: result.rows,
    });
  } catch (error) {
    console.error('Get notes error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};
```

---

## 🔍 লাইন-বাই-লাইন

### `req.query.search` — Query Parameter

```
GET /api/notes?search=বাজার&page=2
              └──────┬───────┘
                query string

req.query = { search: 'বাজার', page: '2' }
```

| উৎস | কোথায় | Express এ |
|---|---|---|
| Route param | `/notes/5` | `req.params.id` |
| **Query param** | `/notes?search=x` | **`req.query.search`** |
| Body | JSON দেহে | `req.body` |

**Query parameter কখন ব্যবহার হয়:** ছাঁকনি (filter), সাজানো (sort), পাতা (pagination) — অর্থাৎ যা **ঐচ্ছিক** এবং যা সম্পদটাকে চিহ্নিত করে না, শুধু রূপ বদলায়।

### `(req.query.search || '').trim()`

| অংশ | কেন |
|---|---|
| `\|\| ''` | search না পাঠালে `undefined` আসত, তার উপর `.trim()` চালালে ক্র্যাশ |
| `.trim()` | `"  বাজার  "` → `"বাজার"` |

---

### `ILIKE` — PostgreSQL এর বিশেষ সুবিধা

```sql
title ILIKE '%বাজার%'
```

| Operator | আচরণ |
|---|---|
| `=` | হুবহু মিল। `'বাজার' = 'বাজারের তালিকা'` → false |
| `LIKE` | প্যাটার্ন মিল, **বড়-ছোট হাতের পার্থক্য মানে** |
| `ILIKE` | প্যাটার্ন মিল, **পার্থক্য মানে না** (I = Insensitive) |

**Wildcard চিহ্ন:**

```
%  →  যেকোনো সংখ্যক অক্ষর (শূন্যও)
_  →  ঠিক একটা অক্ষর

'%বাজার%'   →  ভিতরে কোথাও 'বাজার' আছে
'বাজার%'    →  'বাজার' দিয়ে শুরু
'%বাজার'    →  'বাজার' দিয়ে শেষ
```

`ILIKE` না ব্যবহার করলে `Note` খুঁজলে `note` পাওয়া যাবে না — ব্যবহারকারী বিরক্ত হবে।

> বাংলায় বড়-ছোট হাতের ব্যাপার নেই, কিন্তু ইংরেজি লেখা থাকলে `ILIKE` ই লাগবে।

---

### `$2` কে দুইবার ব্যবহার

```sql
AND (title ILIKE $2 OR content ILIKE $2)
```

একই placeholder দুই জায়গায় — array তে একবারই দিতে হয়। PostgreSQL নিজেই দুই জায়গায় বসিয়ে নেয়।

**বন্ধনী `( )` কেন?** না দিলে যুক্তি ভেঙে যেত:

```sql
-- ❌ বন্ধনী ছাড়া
WHERE user_id = $1 AND title ILIKE $2 OR content ILIKE $2

-- PostgreSQL AND কে OR এর আগে চালায়, তাই এর মানে দাঁড়ায়:
WHERE (user_id = $1 AND title ILIKE $2) OR (content ILIKE $2)
                                            ↑
              এই অংশে user_id এর শর্ত নেই → অন্যের নোটও চলে আসবে! 😱
```

**একটা ভুলে যাওয়া বন্ধনী = নিরাপত্তা গর্ত।** এটা কাল্পনিক নয়, বাস্তবে ঘটা ভুল।

---

### `params.push(\`%${search}%\`)` — এখানেও SQL Injection নেই

```js
params.push(`%${search}%`);
```

লক্ষ্য করো — `%` চিহ্নগুলো **JavaScript এ** যোগ করছি, SQL string এ নয়। মানটা এখনো parameter হিসেবেই যাচ্ছে।

```js
// ✅ নিরাপদ — মান আলাদা করে যাচ্ছে
sql += ` AND title ILIKE $2`;
params.push(`%${search}%`);

// ❌ বিপজ্জনক — মান SQL এর ভিতরে ঢুকছে
sql += ` AND title ILIKE '%${search}%'`;
```

**নিয়মটা আবার:** query এর **কাঠামো** তুমি বানাও, **মান** সবসময় parameter দিয়ে যায়।

> **একটা সূক্ষ্ম কথা:** ব্যবহারকারী যদি `%` বা `_` খোঁজে, সেগুলো wildcard হিসেবে ধরা পড়বে। যেমন `%` খুঁজলে সব নোট আসবে। কড়া করতে চাইলে `search.replace(/[%_]/g, '\\$&')` দিয়ে escape করতে হয়। নিরাপত্তার ঝুঁকি নেই, শুধু ফলাফল অপ্রত্যাশিত।

---

## 🔄 Internal Flow — PostgreSQL এখানে কী করে

```
GET /api/notes?search=বাজার
        │
        ▼
req.query.search = "বাজার"
        │
        ▼
SQL গড়ে উঠল:
  SELECT ... FROM notes
  WHERE user_id = $1
    AND (title ILIKE $2 OR content ILIKE $2)
  ORDER BY created_at DESC

params = [2, '%বাজার%']
        │
        ▼
╔══════════════════════════════════════════════════════════════╗
║ PostgreSQL Planner এর সিদ্ধান্ত                               ║
║                                                              ║
║ ১. user_id = 2  → idx_notes_user_created দিয়ে সরাসরি লাফ ✅  ║
║                                                              ║
║ ২. ILIKE '%বাজার%'  → 😐 index কাজে লাগবে না                 ║
║                                                              ║
║    কারণ B-tree index শুরু থেকে সাজানো থাকে।                  ║
║    'বাজার%' হলে index কাজ করত (শুরু জানা)।                    ║
║    কিন্তু '%বাজার%' এ শুরুটাই অজানা —                         ║
║    তাই প্রতিটা row পড়ে মেলাতে হবে।                            ║
║                                                              ║
║    ✅ তবু ভয় নেই: user_id ছাঁকনি আগে চলে,                     ║
║       তাই মাত্র ওই ব্যবহারকারীর নোটগুলোর মধ্যেই খুঁজবে —      ║
║       পুরো টেবিলে নয়                                          ║
╚══════════════════════════════════════════════════════════════╝
        │
        ▼
    মিলে যাওয়া row গুলো → 200 OK
```

**কখন এটা সমস্যা হবে?** একজন ব্যবহারকারীর যদি ৫০,০০০ নোট থাকে। তখন সমাধান:

| সমাধান | কী |
|---|---|
| **Full-Text Search** | PostgreSQL এর `tsvector` + GIN index — শব্দভিত্তিক খোঁজা, অতি দ্রুত |
| **pg_trgm** | ত্রি-অক্ষর index, `%...%` কেও দ্রুত করে |
| **Elasticsearch** | আলাদা search ইঞ্জিন, বিশাল স্কেলে |

আমাদের অ্যাপে দরকার নেই — কিন্তু জেনে রাখা ভালো যে `ILIKE '%...%'` এর একটা সীমা আছে।

---

## 🧪 Postman Testing

| Test | URL | ফল |
|---|---|---|
| ১ | `/api/notes?search=বাজার` | শুধু মিলে যাওয়া নোট |
| ২ | `/api/notes` | সব নোট (search উপেক্ষিত) |
| ৩ | `/api/notes?search=চাল` | লেখার ভিতরে মিললেও পাবে ✅ |
| ৪ | `/api/notes?search=xyzabc` | `count: 0`, `data: []`, status **200** |
| ৫ | `/api/notes?search=` | সব নোট (খালি string) |

```json
// Test ১ এর response
{
  "success": true,
  "count": 1,
  "search": "বাজার",
  "data": [ { "id": 1, "title": "বাজারের তালিকা", ... } ]
}
```

> কিছু না মিললে **200 + খালি array**, 404 নয় — "খোঁজার ফলাফল খালি" কোনো error নয়।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| বন্ধনী না দেওয়া | **অন্যের নোট ফাঁস** | `AND (... OR ...)` |
| `LIKE` ব্যবহার | বড়-ছোট হাতে মিলবে না | `ILIKE` |
| `%` ছাড়া | হুবহু মিল ছাড়া কিছু পাবে না | `%${search}%` |
| String জোড়া দেওয়া | SQL Injection | parameter |
| `.trim()` না করা | `" বাজার"` কিছুই মেলাবে না | trim |
| খালি ফলাফলে 404 | ক্লায়েন্টে অকারণ error | 200 + `[]` |
| `req.query` কে number ভাবা | সবসময় string | দরকারে `Number()` |

---

## 🏋️ Practice

**১.** `%বাজার%` এ index কাজ করে না, কিন্তু `বাজার%` এ করে। কেন?

<details>
<summary>উত্তর</summary>

B-tree index অভিধানের মতো — শুরুর অক্ষর দিয়ে সাজানো।

`'বাজার%'` — শুরুটা জানা, তাই সরাসরি ওই পাতায় লাফ দেওয়া যায়। ✅

`'%বাজার%'` — শুরু অজানা। "যেসব শব্দের **মাঝখানে** বাজার আছে" — অভিধানে এভাবে খোঁজা যায় না, প্রতিটা শব্দ পড়তে হয়। ❌

তাই "নাম দিয়ে শুরু" ধরনের খোঁজা সবসময় "ভিতরে কোথাও আছে" এর চেয়ে দ্রুত।
</details>

**২.** ভাবো: শুধু শিরোনামে না খুঁজে লেখার ভিতরেও খুঁজছি। এটা কি সবসময় ভালো?

<details>
<summary>উত্তর</summary>

না, ট্রেড-অফ আছে।

**ভালো দিক:** ব্যবহারকারী শিরোনাম ভুলে গেলেও ভিতরের শব্দ দিয়ে খুঁজে পাবে।

**খারাপ দিক:** `content` অনেক বড় হতে পারে (হাজার হাজার অক্ষর) — প্রতিটা row এর পুরো লেখা স্ক্যান করতে হয়, ধীর হয়। আর অপ্রাসঙ্গিক ফলাফলও বেশি আসে।

বাস্তব অ্যাপে প্রায়ই দুটো আলাদা করা হয় — ডিফল্টে শিরোনামে খোঁজা, `?deep=true` দিলে লেখার ভিতরেও।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-17" name="lesson-17"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📄 Lesson 17 — Pagination
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■■□□□□□]  17/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 16 |
| **এই ধাপ শেষে** | `?page=2&limit=10` কাজ করবে |
| **নতুন শব্দ** | LIMIT, OFFSET, COUNT, meta object, cursor pagination |

---

## 🎯 Goal

সব নোট একসাথে না পাঠিয়ে পাতায় পাতায় পাঠানো।

**কেন দরকার?**

```
ব্যবহারকারীর ৫,০০০ নোট আছে

Pagination ছাড়া:
  • PostgreSQL ৫,০০০ row পড়ে
  • Node ৫,০০০ object মেমরিতে রাখে
  • JSON হয় ~১০ MB
  • মোবাইল ডেটায় ৩০ সেকেন্ড
  • Flutter ৫,০০০ widget বানাতে গিয়ে হ্যাং
  • ব্যবহারকারী দেখে মাত্র প্রথম ২০টা

Pagination সহ:
  • ২০ row, ~৪০ KB, তাৎক্ষণিক ✅
```

---

## 💻 Code

```js
const getNotes = async (req, res) => {
  try {
    const userId = req.user.userId;
    const search = (req.query.search || '').trim();

    const page = Math.max(1, Number(req.query.page) || 1);
    const limit = Math.min(100, Math.max(1, Number(req.query.limit) || 10));
    const offset = (page - 1) * limit;

    const where = [`user_id = $1`];
    const params = [userId];

    if (search) {
      params.push(`%${search}%`);
      where.push(`(title ILIKE $${params.length} OR content ILIKE $${params.length})`);
    }

    const whereClause = where.join(' AND ');

    const countResult = await query(
      `SELECT COUNT(*) AS total FROM notes WHERE ${whereClause}`,
      params
    );
    const total = Number(countResult.rows[0].total);

    params.push(limit, offset);

    const result = await query(
      `SELECT id, title, content, created_at, updated_at
       FROM notes
       WHERE ${whereClause}
       ORDER BY created_at DESC
       LIMIT $${params.length - 1} OFFSET $${params.length}`,
      params
    );

    return res.status(200).json({
      success: true,
      data: result.rows,
      meta: {
        total,
        page,
        limit,
        totalPages: Math.ceil(total / limit),
        hasNextPage: page * limit < total,
        hasPrevPage: page > 1,
      },
    });
  } catch (error) {
    console.error('Get notes error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};
```

---

## 🔍 লাইন-বাই-লাইন

### `LIMIT` আর `OFFSET`

```sql
ORDER BY created_at DESC
LIMIT 10 OFFSET 20
```

| অংশ | মানে |
|---|---|
| `LIMIT 10` | সর্বোচ্চ ১০টা row দাও |
| `OFFSET 20` | প্রথম ২০টা বাদ দিয়ে শুরু করো |

```
সব নোট (নতুন → পুরনো):
┌─────────────────────────────────────────────────┐
│ ১  ২  ৩  ...  ১০ │ ১১ ... ২০ │ ২১ ... ৩০ │ ...  │
└──── পাতা ১ ──────┴─ পাতা ২ ──┴─ পাতা ৩ ──┴──────┘
   OFFSET 0           OFFSET 10   OFFSET 20
   LIMIT 10           LIMIT 10    LIMIT 10
```

**হিসাবটা:** `offset = (page - 1) * limit`

```
পাতা ১ → (1-1) × 10 = 0
পাতা ২ → (2-1) × 10 = 10
পাতা ৩ → (3-1) × 10 = 20
```

> ⚠️ **`ORDER BY` ছাড়া pagination অর্থহীন।** ক্রম নিশ্চিত না হলে পাতা ১ আর পাতা ২ এ একই নোট আসতে পারে, আবার কোনোটা কোথাওই না আসতে পারে।

---

### ইনপুট যাচাই — খুব গুরুত্বপূর্ণ

```js
const page = Math.max(1, Number(req.query.page) || 1);
const limit = Math.min(100, Math.max(1, Number(req.query.limit) || 10));
```

**page এর সুরক্ষা:**

```
?page=abc  →  Number("abc") = NaN  →  || 1  →  1  ✅
?page=-5   →  -5  →  Math.max(1, -5) = 1  ✅
              (না ঠেকালে OFFSET -60 → SQL error)
?page=0    →  0 → || চলে না (0 falsy) → 1 ✅
```

**limit এর সুরক্ষা (এটাই বেশি জরুরি):**

```
?limit=99999999
   ↓ Math.min(100, ...) না থাকলে
PostgreSQL কে বললাম ১ কোটি row দাও
   ↓
DB ধীর হয়ে গেল, Node এর মেমরি শেষ, সার্ভার ক্র্যাশ
   ↓
এটাই DoS আক্রমণ — একটা মাত্র URL দিয়ে
```

| এই সীমা না দিলে | যে কেউ `?limit=999999999` পাঠিয়ে তোমার সার্ভার বসিয়ে দিতে পারবে। **প্রতিটা pagination এ সর্বোচ্চ সীমা বাধ্যতামূলক** |

---

### গতিশীল (dynamic) placeholder নম্বর

```js
params.push(`%${search}%`);
where.push(`(title ILIKE $${params.length} OR content ILIKE $${params.length})`);
```

`$${params.length}` দেখতে অদ্ভুত, কিন্তু সরল:

```
প্রথম $  →  SQL এর placeholder চিহ্ন
${params.length}  →  JS এ array এর দৈর্ঘ্য

params = [userId]                → length 1
push করলাম search                → length 2  → `$2`
push করলাম limit, offset         → length 4  → limit=$3, offset=$4
```

**কেন হাতে `$3`, `$4` লিখলাম না?** কারণ search থাকা-না থাকার উপর নম্বর বদলে যায়:

```
search ছাড়া:  params = [userId, limit, offset]           → limit = $2
search সহ:    params = [userId, search, limit, offset]   → limit = $3
```

হাতে লিখলে একটা ক্ষেত্রে অবশ্যই ভুল হতো। `params.length` দিয়ে হিসাব করলে সবসময় ঠিক।

---

### `COUNT(*)` — আলাদা query কেন

```sql
SELECT COUNT(*) AS total FROM notes WHERE user_id = $1
```

`LIMIT 10` দেওয়া query কখনো বলবে না মোট কতগুলো আছে — সে তো ১০টার পর থেমে গেছে। তাই আলাদা করে গুনতে হয়।

**`Number(...)` কেন লাগল?**

```js
const total = Number(countResult.rows[0].total);
```

PostgreSQL এ `COUNT()` এর ধরন `bigint` (৮ বাইট)। JavaScript এর সাধারণ number ৮ বাইট পূর্ণসংখ্যা নিরাপদে ধরতে পারে না, তাই `pg` driver সতর্কতাবশত **string** হিসেবে দেয়:

```js
countResult.rows[0].total    // "42"  ← string!
"42" / 10                    // 4.2   (JS জোর করে বদলে নেয়, কাজ করে)
"42" + 1                     // "421" ← 😱 জোড়া লেগে গেল
```

| `Number()` না দিলে | `totalPages` হয়তো ঠিক আসবে, কিন্তু কোথাও `+` করলেই string জোড়া লেগে অদ্ভুত ফল দেবে |

---

### `meta` object — ক্লায়েন্টের জন্য উপহার

```json
"meta": {
  "total": 42,
  "page": 2,
  "limit": 10,
  "totalPages": 5,
  "hasNextPage": true,
  "hasPrevPage": true
}
```

| ফিল্ড | Flutter এ কী কাজে লাগে |
|---|---|
| `total` | "৪২টি নোট" দেখানো |
| `totalPages` | পাতার নম্বর দেখানো |
| `hasNextPage` | infinite scroll — আরও লোড করব কিনা |
| `hasPrevPage` | "আগের পাতা" বোতাম সক্রিয় কিনা |

`hasNextPage` না দিলে Flutter কে হিসাব করতে হতো `page * limit < total` — সেই একই যুক্তি দুই জায়গায় লেখা হতো। **যা সার্ভার সহজে জানে, তা সার্ভারই পাঠাক।**

---

## 🔄 Internal Flow

```
GET /api/notes?page=2&limit=10&search=বাজার
        │
        ▼
page = 2, limit = 10, offset = 10
        │
        ▼
╔══════════════════════════════════════════════════════════╗
║ Query ১ — গোনা                                            ║
║   SELECT COUNT(*) FROM notes                             ║
║   WHERE user_id=$1 AND (title ILIKE $2 OR ...)           ║
║   → total = 42                                           ║
╚══════════════════════════════════════════════════════════╝
        │
        ▼
╔══════════════════════════════════════════════════════════╗
║ Query ২ — ডেটা আনা                                        ║
║   SELECT ... WHERE ... ORDER BY created_at DESC           ║
║   LIMIT 10 OFFSET 10                                      ║
║                                                          ║
║   PostgreSQL ভিতরে:                                       ║
║     • idx_notes_user_created দিয়ে সাজানো ক্রমে পড়ল       ║
║     • প্রথম ১০টা গুনে বাদ দিল (OFFSET)                    ║
║     • পরের ১০টা নিল (LIMIT)                               ║
║     • থেমে গেল — বাকিগুলো ছুঁলোও না ✅                     ║
╚══════════════════════════════════════════════════════════╝
        │
        ▼
   { data: [১০টা নোট], meta: {...} }
```

> **দুটো query চালানো কি অপচয়?** সামান্য, কিন্তু `COUNT` খুব দ্রুত (index থেকেই হয়ে যায়)। বিকল্প আছে — `COUNT(*) OVER()` window function দিয়ে এক query তেই করা যায়। শুরুতে দুটো আলাদা রাখাই পরিষ্কার।

---

## 🧪 Postman Testing

আগে ১৫টা নোট বানাও (Postman এ ১৫ বার POST, বা psql এ একবারে):

```sql
INSERT INTO notes (user_id, title, content)
SELECT 2, 'নোট ' || i, 'লেখা ' || i FROM generate_series(1, 15) AS i;
```

> `generate_series(1,15)` PostgreSQL এর দারুণ ফাংশন — ১ থেকে ১৫ পর্যন্ত সারি বানায়। পরীক্ষার ডেটা তৈরিতে অসাধারণ।

| Test | URL | ফল |
|---|---|---|
| ১ | `/api/notes` | ১০টা (ডিফল্ট limit) |
| ২ | `/api/notes?page=2` | বাকি ৫টা, `hasNextPage: false` |
| ৩ | `/api/notes?limit=5&page=3` | ১১-১৫ নম্বর নোট |
| ৪ | `/api/notes?limit=99999` | সর্বোচ্চ ১০০ ✅ |
| ৫ | `/api/notes?page=999` | খালি array, 200 |
| ৬ | `/api/notes?page=abc` | পাতা ১ ✅ |
| ৭ | `/api/notes?search=নোট&page=2&limit=5` | search + pagination একসাথে ✅ |

```json
// Test ২ এর response
{
  "success": true,
  "data": [ ...৫টা নোট... ],
  "meta": {
    "total": 15, "page": 2, "limit": 10,
    "totalPages": 2, "hasNextPage": false, "hasPrevPage": true
  }
}
```

---

## 🤔 OFFSET এর একটা সীমা (জেনে রাখো)

```sql
LIMIT 10 OFFSET 1000000
```

PostgreSQL কে ১০ লক্ষ row পড়ে **ফেলে দিতে** হয়, তারপর ১০টা দিতে হয়। যত গভীর পাতা, তত ধীর।

আর একটা সমস্যা — মাঝপথে নতুন নোট যোগ হলে ক্রম সরে যায়:

```
তুমি পাতা ১ দেখলে (নোট ১-১০)
   ↓ কেউ নতুন নোট যোগ করল, সেটা সবার উপরে এল
তুমি পাতা ২ চাইলে (OFFSET 10)
   ↓ সবাই এক ঘর নিচে সরে গেছে
   → পুরনো ১০ নম্বর নোটটা আবার দেখবে 😐
```

**সমাধান — Cursor pagination:**

```sql
-- "শেষ যে নোটটা দেখেছ, তার পরেরগুলো দাও"
WHERE user_id = $1 AND created_at < $2
ORDER BY created_at DESC
LIMIT 10
```

| | OFFSET | Cursor |
|---|---|---|
| পাতা নম্বরে লাফ | ✅ পারে | ❌ পারে না |
| গভীর পাতায় গতি | 🐌 ধীর | ⚡ সবসময় দ্রুত |
| নতুন ডেটা এলে | 😐 পুনরাবৃত্তি | ✅ ঠিক থাকে |
| উপযুক্ত | পাতা-নম্বর UI | Infinite scroll |

মোবাইল অ্যাপ প্রায় সবসময় infinite scroll ব্যবহার করে — তাই বাস্তবে cursor pagination ই বেশি মানানসই। শুরুতে OFFSET শেখা সহজ, তাই এখানে সেটাই রাখলাম।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `limit` এ সর্বোচ্চ সীমা না দেওয়া | **DoS — সার্ভার বসে যাবে** | `Math.min(100, ...)` |
| `page` ঋণাত্মক ঠেকানো না | `OFFSET -10` → SQL error | `Math.max(1, ...)` |
| `ORDER BY` না দেওয়া | পাতায় পাতায় পুনরাবৃত্তি | সবসময় দাও |
| `COUNT` কে number না করা | string জোড়া লেগে ভুল হিসাব | `Number()` |
| `offset` এর সূত্র ভুল (`page * limit`) | পাতা ১ এ প্রথম ১০টা বাদ পড়বে | `(page-1) * limit` |
| `meta` না পাঠানো | Flutter জানবে না আর পাতা আছে কিনা | পাঠাও |
| Count query তে limit/offset পাঠানো | parameter সংখ্যায় গোলমাল | আলাদা রাখো |

---

## 🏋️ Practice

**১.** `?page=2&limit=0` পাঠালে কী হবে?

<details>
<summary>উত্তর</summary>

`Number("0")` = `0`, যা falsy — তাই `|| 10` চলে `limit = 10` হয়ে যাবে।

কাকতালীয়ভাবে ঠিক আচরণ পেলাম। কিন্তু `Math.max(1, ...)` টা তবু রেখেছি, কারণ `-5` এর মতো মান `||` এড়িয়ে যেতে পারত (`-5` truthy)।

শিক্ষা: **সীমা যাচাই স্তরে স্তরে করো** — একটা কৌশলের উপর ভরসা কোরো না।
</details>

**২.** ৫০ লাখ নোট থাকলে `COUNT(*)` কেমন হবে?

<details>
<summary>উত্তর</summary>

ধীর — PostgreSQL এ `COUNT(*)` MVCC এর কারণে সব দৃশ্যমান row গুনে দেখে (index থাকলেও index-only scan এ পুরোটা হাঁটে)।

আমাদের ক্ষেত্রে ভয় নেই, কারণ `WHERE user_id = $1` আগে ছেঁকে দেয় — একজনের নোট গোনা।

বাস্তবে বড় সিস্টেমে কৌশল:
- আনুমানিক গণনা (`pg_class.reltuples`)
- ৫০০ পর্যন্ত গুনে থেমে "৫০০+" দেখানো
- Cursor pagination — মোট সংখ্যা লাগেই না
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-18" name="lesson-18"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Lesson 18 — Refresh Token
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■■■□□□□]  18/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 17 |
| **এই ধাপ শেষে** | দুই token ব্যবস্থা — মেয়াদ শেষেও ব্যবহারকারী logout হবে না |
| **নতুন শব্দ** | access token, refresh token, rotation, reuse detection |

---

## 🎯 সমস্যাটা আগে বুঝে নাও

```
access token এর মেয়াদ ২ ঘণ্টা
        ↓
২ ঘণ্টা পর ব্যবহারকারী নোট খুলতে গেল
        ↓
401 Token expired
        ↓
আবার ইমেইল-পাসওয়ার্ড লিখতে হলো 😤
```

**সহজ সমাধান — মেয়াদ ৩০ দিন করে দাও?**

```
❌ Token চুরি হলে আক্রমণকারী ৩০ দিন ঢুকতে পারবে
❌ Token বাতিল করার উপায় নেই (JWT stateless)
❌ ব্যবহারকারী পাসওয়ার্ড বদলালেও পুরনো token চলবে
```

**আসল সমাধান — দুটো token:**

```
┌──────────────────────────┬──────────────────────────────┐
│    ACCESS TOKEN          │      REFRESH TOKEN           │
├──────────────────────────┼──────────────────────────────┤
│ মেয়াদ: ১৫ মিনিট          │ মেয়াদ: ৭-৩০ দিন              │
│ প্রতিটা API কলে যায়      │ শুধু /refresh এ যায়           │
│ DB তে রাখা হয় না         │ DB তে রাখা হয় ← গুরুত্বপূর্ণ  │
│ বাতিল করা যায় না         │ বাতিল করা যায় ✅              │
│ চুরি → ১৫ মিনিটের ক্ষতি   │ চুরি → বাতিল করে দাও          │
└──────────────────────────┴──────────────────────────────┘
```

দুই জগতের সেরাটাই পাওয়া গেল — **ছোট ঝুঁকির জানালা, তবু ব্যবহারকারীকে বারবার login করতে হয় না।**

---

## 🗄️ ধাপ ১ — refresh_tokens টেবিল

### `src/db/migrations/003_create_refresh_tokens.sql`

```sql
CREATE TABLE IF NOT EXISTS refresh_tokens (
  id         SERIAL      PRIMARY KEY,
  user_id    INTEGER     NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  token_hash TEXT        NOT NULL UNIQUE,
  expires_at TIMESTAMPTZ NOT NULL,
  revoked_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_refresh_user ON refresh_tokens(user_id);
CREATE INDEX IF NOT EXISTS idx_refresh_hash ON refresh_tokens(token_hash);
```

```bash
psql -d noteapp -f src/db/migrations/003_create_refresh_tokens.sql
```

| Column | কেন |
|---|---|
| `token_hash` | **আসল token নয়, তার hash।** DB ফাঁস হলে আক্রমণকারী token গুলো ব্যবহার করতে পারবে না — ঠিক পাসওয়ার্ডের মতো যুক্তি |
| `expires_at` | কবে মেয়াদ শেষ |
| `revoked_at` | বাতিল হয়েছে কিনা (logout এ বসবে)। `NULL` = এখনো বৈধ |
| `ON DELETE CASCADE` | ব্যবহারকারী মুছলে তার সব token ও যাক |

> **Token hash করতে bcrypt নয়, SHA-256 কেন?** bcrypt ইচ্ছা করে ধীর — পাসওয়ার্ডের জন্য ভালো, কারণ মানুষের পাসওয়ার্ড অনুমানযোগ্য। কিন্তু refresh token নিজেই ৬৪ বাইট এলোমেলো — অনুমান করার প্রশ্নই নেই। তাই দ্রুত SHA-256 যথেষ্ট, আর প্রতিটা API কলে ১০০ms নষ্ট হয় না।

---

## 💻 ধাপ ২ — Code

### `.env`

```env
JWT_SECRET=<আগের লম্বা secret>
JWT_EXPIRES_IN=15m

REFRESH_TOKEN_SECRET=<আলাদা আরেকটা লম্বা secret>
REFRESH_TOKEN_EXPIRES_IN=7d
```

> **দুটো secret আলাদা কেন?** একটা ফাঁস হলেও অন্যটা বাঁচে। আর ভুল করে access token কে refresh হিসেবে ব্যবহার করা (বা উল্টোটা) আপনাআপনি আটকে যায়।

### `src/utils/jwt.js`

```js
const jwt = require('jsonwebtoken');
const crypto = require('crypto');

const generateAccessToken = (user) =>
  jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '15m' }
  );

const generateRefreshToken = (user) =>
  jwt.sign(
    { userId: user.id, type: 'refresh' },
    process.env.REFRESH_TOKEN_SECRET,
    { expiresIn: process.env.REFRESH_TOKEN_EXPIRES_IN || '7d' }
  );

const hashToken = (token) =>
  crypto.createHash('sha256').update(token).digest('hex');

module.exports = { generateAccessToken, generateRefreshToken, hashToken };
```

### `src/controllers/auth.controller.js` — login আপডেট

```js
const {
  generateAccessToken,
  generateRefreshToken,
  hashToken,
} = require('../utils/jwt');

// login এর ভিতরে, পাসওয়ার্ড মিলে যাওয়ার পর:

    const accessToken = generateAccessToken(user);
    const refreshToken = generateRefreshToken(user);

    await query(
      `INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
       VALUES ($1, $2, NOW() + INTERVAL '7 days')`,
      [user.id, hashToken(refreshToken)]
    );

    return res.status(200).json({
      success: true,
      message: 'Login successful',
      data: {
        user: { id: user.id, name: user.name, email: user.email },
        accessToken,
        refreshToken,
      },
    });
```

### নতুন controller — `refresh`

```js
const jwt = require('jsonwebtoken');

const refresh = async (req, res) => {
  try {
    const { refreshToken } = req.body;

    if (!refreshToken) {
      return res.status(400).json({ success: false, message: 'refreshToken is required' });
    }

    let decoded;
    try {
      decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET);
    } catch (err) {
      return res.status(401).json({ success: false, message: 'Invalid refresh token' });
    }

    const tokenHash = hashToken(refreshToken);

    const stored = await query(
      `SELECT id, user_id, revoked_at, expires_at
       FROM refresh_tokens
       WHERE token_hash = $1`,
      [tokenHash]
    );

    if (stored.rows.length === 0) {
      return res.status(401).json({ success: false, message: 'Invalid refresh token' });
    }

    const row = stored.rows[0];

    if (row.revoked_at !== null) {
      await query(
        `UPDATE refresh_tokens SET revoked_at = NOW()
         WHERE user_id = $1 AND revoked_at IS NULL`,
        [row.user_id]
      );
      return res.status(401).json({
        success: false,
        message: 'Refresh token reuse detected. Please login again',
      });
    }

    if (new Date(row.expires_at) < new Date()) {
      return res.status(401).json({ success: false, message: 'Refresh token expired' });
    }

    const userResult = await query(
      `SELECT id, name, email FROM users WHERE id = $1`,
      [row.user_id]
    );

    if (userResult.rows.length === 0) {
      return res.status(401).json({ success: false, message: 'User no longer exists' });
    }

    const user = userResult.rows[0];

    const newAccessToken = generateAccessToken(user);
    const newRefreshToken = generateRefreshToken(user);

    await query(`UPDATE refresh_tokens SET revoked_at = NOW() WHERE id = $1`, [row.id]);

    await query(
      `INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
       VALUES ($1, $2, NOW() + INTERVAL '7 days')`,
      [user.id, hashToken(newRefreshToken)]
    );

    return res.status(200).json({
      success: true,
      data: { accessToken: newAccessToken, refreshToken: newRefreshToken },
    });
  } catch (error) {
    console.error('Refresh error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};
```

```js
// route
router.post('/refresh', refresh);       // 👈 authenticate লাগবে না!
```

---

## 🔍 লাইন-বাই-লাইন

### `/refresh` এ `authenticate` middleware নেই কেন?

কারণ ব্যবহারকারী এখানে আসেই তখন, যখন তার **access token এর মেয়াদ শেষ**। Middleware বসালে সে কখনোই ঢুকতে পারত না — মুরগি-ডিমের সমস্যা।

তার পরিচয় এখানে প্রমাণ হয় refresh token দিয়ে।

---

### `crypto.createHash('sha256')`

```js
crypto.createHash('sha256').update(token).digest('hex')
```

| অংশ | কাজ |
|---|---|
| `createHash('sha256')` | SHA-256 hasher বানাও |
| `.update(token)` | token টা খাওয়াও |
| `.digest('hex')` | ফলাফল ৬৪ অক্ষরের hex string আকারে নাও |

`crypto` Node এর **built-in** module — `npm install` লাগে না।

| Hash না করে আসল token রাখলে | DB ফাঁস হলে আক্রমণকারী সরাসরি সবার token পেয়ে যাবে, আর সবার অ্যাকাউন্টে ঢুকে যাবে |

---

### 🔁 Token Rotation — সবচেয়ে গুরুত্বপূর্ণ ধারণা

```js
await query(`UPDATE refresh_tokens SET revoked_at = NOW() WHERE id = $1`, [row.id]);
await query(`INSERT INTO refresh_tokens ... `, [user.id, hashToken(newRefreshToken)]);
```

প্রতিবার refresh করলে **পুরনো refresh token বাতিল, নতুন একটা ইস্যু**।

```
Login       →  refresh_token_A  (বৈধ)
Refresh ১   →  A বাতিল, refresh_token_B পেল
Refresh ২   →  B বাতিল, refresh_token_C পেল
```

**কেন এই ঝামেলা?** কারণ এতে চুরি ধরা পড়ে যায়।

---

### 🚨 Reuse Detection — চুরি ধরার কৌশল

```js
if (row.revoked_at !== null) {
  // এই token আগেই ব্যবহৃত হয়ে বাতিল হয়েছে — অথচ আবার আসছে!
  await query(
    `UPDATE refresh_tokens SET revoked_at = NOW()
     WHERE user_id = $1 AND revoked_at IS NULL`,
    [row.user_id]
  );
  return res.status(401).json({ message: 'Refresh token reuse detected...' });
}
```

**পরিস্থিতিটা কল্পনা করো:**

```
১. আক্রমণকারী কোনোভাবে refresh_token_B চুরি করল
   (ব্যবহারকারীর কাছেও B আছে)

২. আক্রমণকারী B দিয়ে refresh করল
   → B বাতিল হলো, সে C পেল

৩. এখন আসল ব্যবহারকারী B দিয়ে refresh করতে এল
   → B পাওয়া গেল, কিন্তু revoked_at ভরা 🚨

৪. সার্ভার বুঝল: একই token দুইবার ব্যবহৃত হয়েছে
   মানে কারো কাছে কপি আছে!
   → ওই ব্যবহারকারীর সব token বাতিল করে দিল
   → আক্রমণকারীর C ও অকেজো হয়ে গেল ✅
   → ব্যবহারকারীকে আবার login করতে হলো (সামান্য অসুবিধা,
      কিন্তু অ্যাকাউন্ট বাঁচল)
```

**Rotation ছাড়া চুরিটা কখনো ধরাই পড়ত না** — আক্রমণকারী চুপচাপ ৭ দিন ব্যবহার করে যেত।

এই কৌশল OAuth 2.0 এর নিরাপত্তা নির্দেশিকার (RFC 9700) সুপারিশ, আর Google/Auth0 এর মতো প্রতিষ্ঠান এটাই ব্যবহার করে।

---

### `NOW() + INTERVAL '7 days'`

PostgreSQL এর সময় গণনা:

```sql
NOW() + INTERVAL '7 days'      -- ৭ দিন পর
NOW() - INTERVAL '30 minutes'  -- ৩০ মিনিট আগে
NOW() + INTERVAL '1 year 2 months'
```

সময়ের হিসাব **database এই** করা ভালো — Node আর PostgreSQL এর ঘড়িতে সামান্য পার্থক্য থাকতে পারে।

---

## 🔄 সম্পূর্ণ Token Flow

```
┌───────────────────────────────────────────────────────────────┐
│                         LOGIN                                 │
└───────────────────────────────────────────────────────────────┘
  Flutter                                    Server
     │  POST /login {email, password}          │
     │────────────────────────────────────────▶│
     │                                    bcrypt.compare ✅
     │                                    access  (১৫ মিনিট)
     │                                    refresh (৭ দিন)
     │                                    refresh এর hash → DB
     │  { accessToken, refreshToken }          │
     │◀────────────────────────────────────────│
     │                                         │
 secure storage এ দুটোই রাখল                    │


┌───────────────────────────────────────────────────────────────┐
│                    স্বাভাবিক API কল                            │
└───────────────────────────────────────────────────────────────┘
     │  GET /api/notes                         │
     │  Authorization: Bearer <access>         │
     │────────────────────────────────────────▶│
     │                                    verify ✅
     │  200 { notes }                          │
     │◀────────────────────────────────────────│


┌───────────────────────────────────────────────────────────────┐
│               ১৫ মিনিট পর — মেয়াদ শেষ                          │
└───────────────────────────────────────────────────────────────┘
     │  GET /api/notes  (পুরনো access)         │
     │────────────────────────────────────────▶│
     │  401 { code: 'TOKEN_EXPIRED' }          │
     │◀────────────────────────────────────────│
     │                                         │
  Flutter কোনো UI দেখায় না — নীরবে:            │
     │                                         │
     │  POST /auth/refresh {refreshToken}      │
     │────────────────────────────────────────▶│
     │                              ১. JWT signature যাচাই
     │                              ২. hash বানিয়ে DB তে খোঁজো
     │                              ৩. revoked? → 🚨 সব বাতিল
     │                              ৪. expired? → 401
     │                              ৫. পুরনোটা বাতিল করো
     │                              ৬. নতুন জোড়া বানাও
     │  200 { accessToken, refreshToken }      │
     │◀────────────────────────────────────────│
     │                                         │
  নতুন token জমা রাখল, আগের request টা retry করল│
     │  GET /api/notes  (নতুন access)          │
     │────────────────────────────────────────▶│
     │  200 { notes } ✅                        │
     │◀────────────────────────────────────────│

  👤 ব্যবহারকারী কিচ্ছু টের পেল না
```

> **Flutter এ এটা কীভাবে লেখে?** Dio এর `InterceptorsWrapper` এর `onError` এ — 401 + `TOKEN_EXPIRED` পেলে refresh করে মূল request টা আবার পাঠায়। খেয়াল রাখতে হয় যেন একসাথে ১০টা request fail করলে ১০ বার refresh না হয় (একটা mutex/lock লাগে)।

---

## 🧪 Postman Testing

### Test ১ — Login

দুটো token পাবে:

```json
{
  "data": {
    "user": {...},
    "accessToken": "eyJ...",
    "refreshToken": "eyJ..."
  }
}
```

### Test ২ — Refresh

```
POST http://localhost:5000/api/auth/refresh
{ "refreshToken": "<login থেকে পাওয়া refresh token>" }
```

**200** — নতুন জোড়া ✅

### Test ৩ — একই refresh token আবার (এটাই আসল পরীক্ষা)

Test ২ এর **একই** token আবার পাঠাও:

```json
{
  "success": false,
  "message": "Refresh token reuse detected. Please login again"
}
```

**Reuse detection কাজ করছে ✅**

এখন DB তে দেখো:

```sql
SELECT id, user_id, revoked_at FROM refresh_tokens ORDER BY id;
```

সব `revoked_at` ভরা — ওই ব্যবহারকারীর সব token বাতিল হয়ে গেছে ✅

### Test ৪ — Access token এর মেয়াদ শেষ হওয়া দেখা

`.env` এ `JWT_EXPIRES_IN=10s` করে, login করে, ১৫ সেকেন্ড পরে `/api/notes` চাও → **401 TOKEN_EXPIRED**। তারপর refresh করে নতুন token নিয়ে আবার চাও → **200** ✅

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| Refresh token DB তে না রাখা | কখনো বাতিল করা যাবে না | রাখো |
| আসল token রাখা (hash না করে) | DB ফাঁস = সব অ্যাকাউন্ট দখল | hash করো |
| Rotation না করা | চুরি কখনো ধরা পড়বে না | প্রতিবার নতুন |
| দুই token এ একই secret | একটা ফাঁস = দুটোই শেষ | আলাদা secret |
| `/refresh` এ authenticate বসানো | কখনো ঢোকা যাবে না | বসিও না |
| Reuse এ শুধু ওই token বাতিল | আক্রমণকারীর নতুন token টা টিকে যাবে | ওই ব্যবহারকারীর **সব** বাতিল |
| Access token এর মেয়াদ লম্বা রাখা | দুই token রাখার উদ্দেশ্যই ব্যর্থ | ১৫ মিনিট |
| মেয়াদোত্তীর্ণ row কখনো না মোছা | টেবিল ফুলে যাবে | নিয়মিত পরিষ্কার (Lesson 22) |

---

## 🏋️ Practice

**১.** ব্যবহারকারী দুটো ডিভাইসে login করলে refresh_tokens টেবিলে কী থাকবে?

<details>
<summary>উত্তর</summary>

দুটো আলাদা row — প্রতিটা ডিভাইসের জন্য একটা। দুটোই বৈধ, দুটোই আলাদাভাবে rotate হবে।

এটাই কাম্য — এক ডিভাইসে logout করলে অন্যটা চালু থাকবে।

উন্নত করতে চাইলে টেবিলে `device_info` আর `ip_address` column যোগ করা যায় — তখন "সক্রিয় সেশন" তালিকা দেখানো যাবে (Facebook/Google এর মতো)।
</details>

**২.** Reuse detected হলে ওই ব্যবহারকারীর **সব** token বাতিল করি কেন? শুধু ওইটা করলে হতো না?

<details>
<summary>উত্তর</summary>

না, কারণ আমরা জানি না কে আসল আর কে চোর।

দুটো সম্ভাবনা:
- চোর আগে refresh করেছে, তার কাছে এখন নতুন token আছে
- ব্যবহারকারী আগে refresh করেছে, চোরের কাছে পুরনোটা

শুধু পুরনোটা বাতিল করলে চোরের নতুন token টা টিকে যেত।

সব বাতিল করা মানে — **দুজনকেই বের করে দাও।** আসল ব্যবহারকারী আবার login করতে পারবে (তার পাসওয়ার্ড আছে), চোর পারবে না।

নিরাপত্তায় এই নীতিটাই ঠিক: **সন্দেহ হলে বন্ধ করে দাও, খোলা রেখো না।**
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-19" name="lesson-19"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚪 Lesson 19 — Logout
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■■■■□□□]  19/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 18 |
| **এই ধাপ শেষে** | Logout আর logout-all কাজ করবে |
| **নতুন শব্দ** | revoke, stateless এর সীমা, blacklist |

---

## 🤔 প্রথমে অস্বস্তিকর সত্যটা জেনে নাও

**JWT কে "বাতিল" করা যায় না।**

```
সার্ভার token টা মনে রাখে না।
প্রতিবার শুধু signature মিলিয়ে দেখে।

তাই "এই token টা আর গ্রহণ কোরো না" — এটা বলার জায়গাই নেই।
Token মেয়াদ শেষ না হওয়া পর্যন্ত কাজ করেই যাবে।
```

**তাহলে logout কী করে?**

```
১. Refresh token বাতিল করে (DB তে আছে, তাই পারা যায়) ✅
২. Access token নিজে থেকে মরার অপেক্ষা করে (১৫ মিনিট) ⏳
৩. Flutter নিজের কাছ থেকে দুটোই মুছে ফেলে ✅
```

তাই logout এর পর সর্বোচ্চ ১৫ মিনিটের একটা ফাঁক থাকে যেখানে চুরি করা access token কাজ করবে। **এই কারণেই access token এর মেয়াদ ছোট রাখা এত জরুরি।**

---

## 💻 Code

```js
const logout = async (req, res) => {
  try {
    const { refreshToken } = req.body;
    const userId = req.user.userId;

    if (!refreshToken) {
      return res.status(400).json({ success: false, message: 'refreshToken is required' });
    }

    const result = await query(
      `UPDATE refresh_tokens
       SET revoked_at = NOW()
       WHERE token_hash = $1 AND user_id = $2 AND revoked_at IS NULL
       RETURNING id`,
      [hashToken(refreshToken), userId]
    );

    return res.status(200).json({
      success: true,
      message: 'Logged out successfully',
      revoked: result.rowCount,
    });
  } catch (error) {
    console.error('Logout error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};

const logoutAll = async (req, res) => {
  try {
    const userId = req.user.userId;

    const result = await query(
      `UPDATE refresh_tokens
       SET revoked_at = NOW()
       WHERE user_id = $1 AND revoked_at IS NULL
       RETURNING id`,
      [userId]
    );

    return res.status(200).json({
      success: true,
      message: 'Logged out from all devices',
      revoked: result.rowCount,
    });
  } catch (error) {
    console.error('Logout all error:', error);
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};
```

```js
// route
router.post('/logout', authenticate, logout);
router.post('/logout-all', authenticate, logoutAll);
```

---

## 🔍 লাইন-বাই-লাইন

### `WHERE token_hash = $1 AND user_id = $2 AND revoked_at IS NULL`

তিনটা শর্ত, তিনটাই জরুরি:

| শর্ত | কেন |
|---|---|
| `token_hash = $1` | ঠিক এই token টা |
| `user_id = $2` | **নিজেরটা** — নাহলে অন্যের token বাতিল করে তাকে জোর করে logout করানো যেত |
| `revoked_at IS NULL` | আগেই বাতিল হয়ে থাকলে সময়টা আবার বদলাবে না (মূল বাতিলের সময় সংরক্ষিত থাকবে) |

দ্বিতীয় শর্তটা না দিলে একটা মজার আক্রমণ সম্ভব — কারো refresh token জানা থাকলে (হয়তো লগে দেখেছ) তাকে বারবার logout করিয়ে দেওয়া যেত।

### `logout` এ `authenticate` আছে, কিন্তু `refresh` এ ছিল না

| Route | Middleware | কেন |
|---|---|---|
| `/refresh` | ❌ | access token এর মেয়াদ শেষ, তাই ঢুকতে পারত না |
| `/logout` | ✅ | logout করার সময় access token সাধারণত এখনো বৈধ, আর `user_id` মিলিয়ে দেখা দরকার |

### `revoked: result.rowCount`

কয়টা token বাতিল হলো তা ফেরত দিই।

```
logout      →  revoked: 1
logout-all  →  revoked: 3   (তিন ডিভাইস)
revoked: 0  →  token আগেই বাতিল ছিল, বা ভুল token
```

`revoked: 0` হলেও আমরা 200 দিই — logout করতে গিয়ে ব্যবহারকারীকে error দেখানোর মানে হয় না। **যা চেয়েছিল তা হয়ে গেছে** (সে আর ঢুকতে পারছে না)।

---

## 🔧 কখন "সব ডিভাইস থেকে logout" দরকার

```
• ব্যবহারকারী পাসওয়ার্ড বদলাল      →  logoutAll জরুরি
• "আমার অ্যাকাউন্ট হ্যাক হয়েছে"     →  logoutAll
• অ্যাডমিন কাউকে নিষিদ্ধ করল        →  logoutAll
• ফোন হারিয়ে গেছে                  →  logoutAll
```

> **পাসওয়ার্ড বদলানোর পর logoutAll না করা একটা পরিচিত নিরাপত্তা ভুল।** কেউ যদি অ্যাকাউন্ট দখল করে থাকে, আসল মালিক পাসওয়ার্ড বদলালেও চোরের token চলতেই থাকবে — যতক্ষণ না মেয়াদ শেষ হয়।

---

## 🔄 Internal Flow

```
POST /api/auth/logout
Authorization: Bearer <access token>
{ "refreshToken": "eyJ..." }
        │
        ▼
authenticate → req.user.userId = 2
        │
        ▼
hashToken(refreshToken) → "a3f5b2c8..."
        │
        ▼
╔══════════════════════════════════════════════════════════╗
║ UPDATE refresh_tokens                                    ║
║ SET revoked_at = NOW()                                   ║
║ WHERE token_hash = 'a3f5b2c8...'                         ║
║   AND user_id = 2                                        ║
║   AND revoked_at IS NULL                                 ║
║                                                          ║
║ → idx_refresh_hash দিয়ে সরাসরি row পেল                    ║
║ → revoked_at বসাল                                        ║
║ → rowCount = 1                                           ║
╚══════════════════════╪═══════════════════════════════════╝
                       ▼
              200 { revoked: 1 }
                       ▼
        ┌──────────────────────────────────┐
        │ Flutter এখন যা করবে:              │
        │  • secure storage থেকে দুটো token │
        │    মুছে ফেলবে                     │
        │  • login স্ক্রিনে নিয়ে যাবে        │
        │  • মেমরির cache পরিষ্কার করবে      │
        └──────────────────────────────────┘

এরপর ওই refresh token দিয়ে চেষ্টা করলে:
  → revoked_at ভরা → 401 (reuse detection)
```

---

## 🧪 Postman Testing

| Test | কী করবে | ফল |
|---|---|---|
| ১ | Login → logout | `200 { revoked: 1 }` |
| ২ | বাতিল করা refreshToken দিয়ে `/refresh` | **401** ✅ |
| ৩ | পুরনো accessToken দিয়ে `/api/notes` | **200** 😐 মেয়াদ শেষ না হওয়া পর্যন্ত চলবে |
| ৪ | তিন ডিভাইসে login → `/logout-all` | `200 { revoked: 3 }` |
| ৫ | logout এর পর আবার logout | `200 { revoked: 0 }` |

**Test ৩ ভালো করে বুঝে নাও** — এটাই JWT এর মৌলিক সীমা। Logout করার পরেও access token ১৫ মিনিট বেঁচে থাকে।

---

## 🤔 তাৎক্ষণিক বাতিল চাইলে কী করব?

কিছু অ্যাপে (ব্যাংক, স্বাস্থ্য) ১৫ মিনিটের ফাঁকও গ্রহণযোগ্য নয়। তখন কৌশলগুলো:

### ১. Blacklist (কালো তালিকা)

```sql
CREATE TABLE token_blacklist (
  jti        TEXT PRIMARY KEY,     -- token এর অনন্য id
  expires_at TIMESTAMPTZ NOT NULL
);
```

প্রতিটা request এ দেখো token টা কালো তালিকায় আছে কিনা।

**দাম:** প্রতিটা API কলে একটা অতিরিক্ত DB query — JWT এর "কিছু মনে রাখতে হয় না" সুবিধাটাই চলে গেল। Redis এ রাখলে দ্রুত হয়, কিন্তু জটিলতা বাড়ে।

### ২. `token_version` column

```sql
ALTER TABLE users ADD COLUMN token_version INTEGER NOT NULL DEFAULT 0;
```

JWT payload এ `tokenVersion` রাখো। Middleware এ DB এর সাথে মিলিয়ে দেখো। Logout-all এ `token_version` এক বাড়িয়ে দাও — সব পুরনো token মুহূর্তে অকেজো।

**দাম:** একই — প্রতিটা request এ DB পড়া।

### ৩. খুব ছোট মেয়াদ

Access token ৫ মিনিট করে দাও। ফাঁকটা ছোট হলো, refresh বেশি হবে — কিন্তু জটিলতা বাড়ল না।

**আমাদের নোট অ্যাপে ৩ নম্বরই যথেষ্ট।** নিরাপত্তার সিদ্ধান্ত সবসময় "কতটা ঝুঁকি বনাম কতটা জটিলতা" — অন্ধভাবে সর্বোচ্চ নিরাপত্তা নেওয়া প্রকৌশলগত ভুল।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| শুধু ক্লায়েন্টে token মুছে দেওয়া | Refresh token সার্ভারে বৈধ থেকে যায় | DB তে revoke করো |
| `user_id` শর্ত বাদ | অন্যকে জোর করে logout করানো যাবে | দুটো শর্তই |
| Logout এ 404 দেওয়া | ব্যবহারকারী বিভ্রান্ত হবে | সবসময় 200 |
| পাসওয়ার্ড বদলে logoutAll না করা | চোরের সেশন টিকে থাকে | বদলানোর সাথে সাথে |
| "JWT logout করলে সাথে সাথে বাতিল" ভাবা | ভুল ধারণা | মেয়াদ শেষ হতে হয় |
| বাতিল করা row মুছে ফেলা | নিরীক্ষার (audit) সুযোগ নষ্ট | `revoked_at` বসাও, মুছো না |

---

## 🏋️ Practice

**১.** Logout করার পরেও access token কাজ করে — এটা কি নিরাপত্তা দুর্বলতা?

<details>
<summary>উত্তর</summary>

দুর্বলতা নয়, **সচেতন ট্রেড-অফ**।

JWT এর মূল সুবিধাটাই হলো সার্ভারকে কিছু মনে রাখতে হয় না — তাই যত খুশি সার্ভার যোগ করা যায়, প্রতিটা request এ DB পড়তে হয় না। এর দাম হলো তাৎক্ষণিক বাতিল করা যায় না।

ঝুঁকি নিয়ন্ত্রণের উপায়: মেয়াদ ছোট রাখা। ১৫ মিনিটের জানালা বেশিরভাগ অ্যাপের জন্য গ্রহণযোগ্য।

গ্রহণযোগ্য না হলে session-ভিত্তিক ব্যবস্থা বা blacklist বেছে নিতে হয় — এবং তার দামও মেনে নিতে হয়।
</details>

**২.** পাসওয়ার্ড বদলানোর API বানালে সেখানে কী কী করতে হবে?

<details>
<summary>উত্তর</summary>

```
১. বর্তমান পাসওয়ার্ড যাচাই করো (bcrypt.compare)
   ← এটা বাদ দিলে চুরি করা token দিয়ে কেউ পাসওয়ার্ড বদলে
     অ্যাকাউন্ট চিরতরে দখল করে নেবে

২. নতুন পাসওয়ার্ডের শক্তি যাচাই করো

৩. নতুন hash বানিয়ে UPDATE করো

৪. logoutAll চালাও — সব refresh token বাতিল

৫. ব্যবহারকারীকে নতুন token জোড়া দাও (নাহলে সে নিজেই বেরিয়ে যাবে)

৬. (ভালো অভ্যাস) ইমেইলে জানাও: "আপনার পাসওয়ার্ড বদলানো হয়েছে"
```

৪ নম্বর ধাপটাই সবচেয়ে বেশি বাদ পড়ে।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-20" name="lesson-20"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧯 Lesson 20 — Error Handling
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■■■■■□□]  20/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 19 |
| **এই ধাপ শেষে** | সব error এক জায়গায়, প্রতিটা controller ছোট হয়ে যাবে |
| **নতুন শব্দ** | error middleware, AppError, asyncHandler, 404 handler |

---

## 🎯 সমস্যাটা দেখো

এই মুহূর্তে প্রতিটা controller দেখতে এরকম:

```js
const getNotes = async (req, res) => {
  try {
    // ৫ লাইন আসল কাজ
  } catch (error) {
    console.error('...');
    return res.status(500).json({ success: false, message: 'Something went wrong' });
  }
};
```

**সমস্যাগুলো:**

```
❌ ৯টা controller = ৯টা একই try/catch (~৪৫ লাইন পুনরাবৃত্তি)
❌ কেউ একটায় try/catch লিখতে ভুলে গেলে পুরো সার্ভার ক্র্যাশ
❌ Error response এর গঠন প্রতি জায়গায় হাতে লেখা — অসামঞ্জস্যের ঝুঁকি
❌ নেই এমন route এ Express এর HTML পাতা আসে, JSON নয়
```

**সমাধান — তিনটা টুকরা:**

```
১. AppError      →  ইচ্ছাকৃত error এর একটা শ্রেণি
২. asyncHandler  →  try/catch স্বয়ংক্রিয় করার মোড়ক
৩. errorHandler  →  সব error শেষমেশ যেখানে এসে জমা হয়
```

---

## 💻 Code

### ফাইল ১ — `src/utils/AppError.js`

```js
class AppError extends Error {
  constructor(message, statusCode, code = null) {
    super(message);
    this.statusCode = statusCode;
    this.code = code;
    this.isOperational = true;
    Error.captureStackTrace(this, this.constructor);
  }
}

module.exports = AppError;
```

### ফাইল ২ — `src/utils/asyncHandler.js`

```js
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

module.exports = asyncHandler;
```

### ফাইল ৩ — `src/middlewares/error.middleware.js`

```js
const notFound = (req, res, next) => {
  res.status(404).json({
    success: false,
    message: `Route not found: ${req.method} ${req.originalUrl}`,
  });
};

const errorHandler = (err, req, res, next) => {
  console.error('❌ Error:', {
    method: req.method,
    url: req.originalUrl,
    message: err.message,
    stack: process.env.NODE_ENV === 'development' ? err.stack : undefined,
  });

  if (err.isOperational) {
    return res.status(err.statusCode).json({
      success: false,
      message: err.message,
      ...(err.code && { code: err.code }),
    });
  }

  if (err.code === '23505') {
    return res.status(409).json({ success: false, message: 'Duplicate value not allowed' });
  }

  if (err.code === '23503') {
    return res.status(400).json({ success: false, message: 'Related record does not exist' });
  }

  if (err.code === '22P02') {
    return res.status(400).json({ success: false, message: 'Invalid input format' });
  }

  if (err.name === 'TokenExpiredError') {
    return res.status(401).json({ success: false, message: 'Token expired', code: 'TOKEN_EXPIRED' });
  }

  if (err.name === 'JsonWebTokenError') {
    return res.status(401).json({ success: false, message: 'Invalid token' });
  }

  return res.status(500).json({
    success: false,
    message: 'Internal server error',
    ...(process.env.NODE_ENV === 'development' && { debug: err.message }),
  });
};

module.exports = { notFound, errorHandler };
```

### ফাইল ৪ — Controller এখন কত ছোট হলো দেখো

```js
const asyncHandler = require('../utils/asyncHandler');
const AppError = require('../utils/AppError');
const { query } = require('../config/db');

const getNoteById = asyncHandler(async (req, res) => {
  const noteId = Number(req.params.id);

  if (!Number.isInteger(noteId) || noteId <= 0) {
    throw new AppError('Invalid note id', 400);
  }

  const result = await query(
    `SELECT id, title, content, created_at, updated_at
     FROM notes WHERE id = $1 AND user_id = $2`,
    [noteId, req.user.userId]
  );

  if (result.rows.length === 0) {
    throw new AppError('Note not found', 404);
  }

  res.status(200).json({ success: true, data: result.rows[0] });
});
```

**কোনো try/catch নেই। কোনো `return res.status(500)` নেই।** শুধু আসল কাজ।

### ফাইল ৫ — `server.js` (ক্রমটা খুব জরুরি)

```js
require('dotenv').config();

const express = require('express');
const authRoutes = require('./src/routes/auth.routes');
const noteRoutes = require('./src/routes/note.routes');
const { notFound, errorHandler } = require('./src/middlewares/error.middleware');

const app = express();
const PORT = process.env.PORT || 5000;

app.use(express.json());

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', uptime: process.uptime() });
});

app.use('/api/auth', authRoutes);
app.use('/api/notes', noteRoutes);

app.use(notFound);        // 👉 সব route এর পরে
app.use(errorHandler);    // 👉 সবার শেষে — এটাই নিয়ম

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

---

## 🔍 লাইন-বাই-লাইন

### `class AppError extends Error`

```js
class AppError extends Error {
  constructor(message, statusCode, code = null) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
  }
}
```

| লাইন | কাজ |
|---|---|
| `extends Error` | JavaScript এর built-in Error থেকে উত্তরাধিকার — তাই `throw` করা যাবে |
| `super(message)` | মূল Error এর constructor ডাকে, `message` বসায় |
| `this.statusCode` | কোন HTTP code পাঠাব — **এটাই মূল সংযোজন** |
| `this.isOperational = true` | **"এটা আমার ইচ্ছাকৃত error, বাগ নয়"** |

**`isOperational` কেন গুরুত্বপূর্ণ?** দুই ধরনের error আলাদা করতে:

```
Operational error (প্রত্যাশিত):        Programmer error (বাগ):
──────────────────────────           ────────────────────────
"Note not found"                     undefined.title পড়া
"Invalid email"                      টাইপো করা variable
"Token expired"                      DB টেবিলের নাম ভুল

→ ব্যবহারকারীকে বার্তা দেখাও ✅        → ভিতরের কথা লুকাও,
                                        শুধু "Internal error" বলো ✅
                                        (নাহলে টেবিলের নাম, ফাইলের
                                         path সব ফাঁস হয়ে যাবে)
```

Dart এর সাথে মিলিয়ে: এটা তোমার নিজের `class NotFoundException implements Exception` বানানোর মতো।

---

### `asyncHandler` — এই ৩ লাইন বোঝা জরুরি

```js
const asyncHandler = (fn) => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};
```

ধাপে ধাপে ভাঙি:

```js
const asyncHandler = (fn) => { ... }
//                   ↑ একটা ফাংশন নেয় (তোমার controller)

const asyncHandler = (fn) => (req, res, next) => { ... }
//                          ↑ আরেকটা ফাংশন ফেরত দেয় (Express এটা চালাবে)
```

**সমস্যাটা কী ছিল?** Express (৪.x) async ফাংশনের ভিতরের error নিজে ধরতে পারে না:

```js
// try/catch ছাড়া async controller
app.get('/notes', async (req, res) => {
  throw new Error('বিপদ');       // ← Express এটা কখনো জানবে না
});
// → Promise rejected, কেউ ধরল না → request ঝুলে থাকে / process ক্র্যাশ
```

**asyncHandler যা করে:**

```
Promise.resolve( fn(req, res, next) )
        └── controller চালাও, ফলটা একটা Promise বানাও

.catch(next)
        └── কোনো error হলে next(error) ডাকো
                    ↓
        Express দেখে next() এ argument আছে
                    ↓
        সাধারণ middleware সব বাদ দিয়ে সরাসরি
        error handler এ লাফ দেয়
```

| না ব্যবহার করলে | প্রতিটা controller এ হাতে try/catch লিখতে হবে, আর একবার ভুলে গেলে সার্ভার ক্র্যাশ |

> Express 5 এ async error স্বয়ংক্রিয়ভাবে ধরা পড়ে। তবু `asyncHandler` জানা দরকার — কারণ বিপুল পরিমাণ বাস্তব কোড Express 4 এ চলছে, আর এটা দেখলেই চিনতে পারবে।

---

### `errorHandler` এর **চারটা** প্যারামিটার

```js
const errorHandler = (err, req, res, next) => { ... };
//                    ↑ এই প্রথমটাই সব পার্থক্য গড়ে দেয়
```

**Express ফাংশনের প্যারামিটার গুনে সিদ্ধান্ত নেয়:**

```
৩টা (req, res, next)        →  সাধারণ middleware
৪টা (err, req, res, next)   →  error handling middleware ✅
```

| ভুল | ফল |
|---|---|
| `err` বাদ দিয়ে ৩টা লেখা | Express একে সাধারণ middleware ভাববে, error কখনো এখানে আসবে না |
| শেষের `next` মুছে দেওয়া | **৩টা প্যারামিটার হয়ে যাবে → error handler কাজ করা বন্ধ করে দেবে।** ব্যবহার না করলেও `next` লিখে রাখতেই হবে |

---

### ক্রম — `notFound` আর `errorHandler` সবার শেষে কেন

```js
app.use('/api/auth', authRoutes);
app.use('/api/notes', noteRoutes);
app.use(notFound);        // ← কোনো route মেলেনি
app.use(errorHandler);    // ← সবচেয়ে শেষে
```

Express উপর থেকে নিচে চলে:

```
Request → json → routes → মিলল?
                            │
                    হ্যাঁ ──┴── controller → response ✅
                     │
                     না → notFound → 404 JSON ✅

যেকোনো জায়গায় error → সব লাফিয়ে → errorHandler ✅
```

| ভুল ক্রম | ফল |
|---|---|
| `notFound` route এর **উপরে** | প্রতিটা request 404 পাবে, কোনো API চলবে না |
| `errorHandler` route এর উপরে | error কখনো ওখানে পৌঁছাবে না |

---

### `process.env.NODE_ENV` দিয়ে দুই আচরণ

```js
stack: process.env.NODE_ENV === 'development' ? err.stack : undefined
...(process.env.NODE_ENV === 'development' && { debug: err.message })
```

| পরিবেশ | কী দেখাব |
|---|---|
| development | পুরো stack trace — ডিবাগ করতে লাগে |
| production | কিছু না — নাহলে ফাইলের path, টেবিলের নাম, ভিতরের গঠন সব ফাঁস |

**`...(শর্ত && { key: value })` কৌশলটা:** শর্ত মিথ্যা হলে `false` ছড়ায়, যা কিছুই যোগ করে না। শর্ত সত্য হলে key টা যোগ হয়। শর্তসাপেক্ষ ফিল্ড যোগ করার পরিচ্ছন্ন উপায়।

---

### PostgreSQL error code এক জায়গায়

```js
if (err.code === '23505') return res.status(409)...
if (err.code === '23503') return res.status(400)...
if (err.code === '22P02') return res.status(400)...
```

আগে এই চেকগুলো প্রতিটা controller এ ছড়ানো ছিল। এখন **এক জায়গায়** — নতুন controller লিখলে সে এমনিতেই এই সুবিধা পাবে।

---

## 🔄 Internal Flow — একটা error এর যাত্রা

```
GET /api/notes/9999   (নোটটা নেই)
        │
        ▼
authenticate → ✅ → asyncHandler এর মোড়কে controller
        │
        ▼
SELECT ... → rows.length === 0
        │
        ▼
throw new AppError('Note not found', 404)
        │
        ▼
┌────────────────────────────────────────────────┐
│ asyncHandler এর .catch(next) ধরল               │
│ → next(err) ডাকল                               │
└────────────────────┬───────────────────────────┘
                     ▼
┌────────────────────────────────────────────────┐
│ Express দেখল next() এ argument আছে             │
│ → বাকি সব middleware লাফিয়ে পার হলো            │
│ → ৪-প্যারামিটার middleware খুঁজল                │
└────────────────────┬───────────────────────────┘
                     ▼
┌────────────────────────────────────────────────┐
│ errorHandler(err, req, res, next)              │
│                                                │
│ ১. লগ করল (method, url, message)               │
│ ২. err.isOperational === true ✅                │
│ ৩. res.status(404).json({                      │
│      success: false,                           │
│      message: 'Note not found'                 │
│    })                                          │
└────────────────────┬───────────────────────────┘
                     ▼
              Postman এ 404 JSON
```

**একটা অপ্রত্যাশিত বাগের যাত্রা:**

```
কোডে টাইপো: result.rowz[0]
        │
        ▼
TypeError: Cannot read properties of undefined
        │
        ▼
asyncHandler ধরল → next(err) → errorHandler
        │
        ▼
isOperational নেই → PostgreSQL code ও নয়
        │
        ▼
500 { success: false, message: 'Internal server error' }
        │
        ├─ ব্যবহারকারী: শুধু সাধারণ বার্তা দেখল ✅
        └─ তুমি: terminal এ পুরো stack trace পেলে ✅
        └─ সার্ভার: বেঁচে আছে ✅ ← সবচেয়ে জরুরি
```

---

## 🧪 Postman Testing

| Test | Request | ফল |
|---|---|---|
| ১ | `GET /api/nothing` | **404 JSON** (HTML নয় ✅) |
| ২ | `GET /api/notes/9999` | **404** "Note not found" |
| ৩ | `GET /api/notes/abc` | **400** "Invalid note id" |
| ৪ | একই ইমেইলে register | **409** "Duplicate value not allowed" |
| ৫ | মেয়াদোত্তীর্ণ token | **401** `code: TOKEN_EXPIRED` |

```json
// Test ১
{
  "success": false,
  "message": "Route not found: GET /api/nothing"
}
```

**Flutter এর জন্য এটা বিরাট স্বস্তি** — এখন প্রতিটা উত্তরই JSON, একই গঠনের। `jsonDecode` আর কখনো HTML পেয়ে ক্র্যাশ করবে না।

---

## ⚠️ Common Mistakes

| ভুল | ফল | সমাধান |
|---|---|---|
| `errorHandler` এ ৩ প্যারামিটার | Express একে সাধারণ middleware ভাববে | ৪টা লাগবেই |
| `errorHandler` route এর উপরে | error কখনো পৌঁছাবে না | সবার শেষে |
| `notFound` route এর উপরে | সব request 404 | route এর পরে |
| `asyncHandler` ছাড়া async controller (Express 4) | Promise rejection, সার্ভার ক্র্যাশ | মুড়ে দাও |
| Production এ stack trace পাঠানো | ভিতরের গঠন ফাঁস | NODE_ENV দিয়ে ভাগ করো |
| `err.message` সরাসরি পাঠানো | DB এর বার্তায় টেবিল/column এর নাম | AppError হলেই কেবল |
| error handler এ `next` লিখতে ভুলে যাওয়া | নীরবে কাজ করা বন্ধ | রেখে দাও |

---

## 🏋️ Practice

**১.** `throw new AppError(...)` লিখলে সার্ভার ক্র্যাশ করে না কেন?

<details>
<summary>উত্তর</summary>

কারণ `asyncHandler` এর `.catch(next)` সেটাকে ধরে ফেলে। ধরা পড়া error আর "অধরা error" নয়, তাই process টিকে থাকে।

`asyncHandler` ছাড়া (Express 4 এ) throw করলে Promise rejected হতো, কেউ ধরত না, আর Node "unhandled rejection" বলে প্রক্রিয়া বন্ধ করে দিত।

এই কারণেই মোড়কটা ঐচ্ছিক নয় — এটাই ব্যবস্থাটাকে ধরে রেখেছে।
</details>

**২.** Database একেবারে বন্ধ হয়ে গেলে ব্যবহারকারী কী দেখবে?

<details>
<summary>উত্তর</summary>

`query()` ছুড়বে `ECONNREFUSED` → asyncHandler ধরবে → errorHandler এ যাবে।

`isOperational` নেই, চেনা PostgreSQL code ও নয় → **500 "Internal server error"**।

ঠিক আচরণ, কারণ:
- ব্যবহারকারী জানল কিছু একটা ভেঙেছে, কিন্তু ভিতরের কথা জানল না
- তুমি লগে পুরোটা পেলে
- সার্ভার বেঁচে রইল, DB ফিরে এলে আবার কাজ করবে

আরও ভালো করতে চাইলে `503 Service Unavailable` দেওয়া যেত — "সাময়িক সমস্যা, একটু পরে চেষ্টা করুন"। তাতে Flutter নিজে থেকে retry করতে পারত।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-21" name="lesson-21"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏗️ Lesson 21 — Project Structure
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■■■■■■□]  21/22`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 20 |
| **এই ধাপ শেষে** | Production-এর মতো স্তরে সাজানো প্রজেক্ট |
| **নতুন শব্দ** | layered architecture, service, repository, separation of concerns |

---

## 🎯 এখনকার সমস্যা

Controller একসাথে তিনটা কাজ করছে:

```js
const createNote = asyncHandler(async (req, res) => {
  const { title } = req.body;
  if (!title) throw new AppError('title is required', 400);   // ← HTTP এর কাজ
                                                              // ← নিয়মের কাজ
  const result = await query(`INSERT INTO notes ...`, [...]);  // ← SQL এর কাজ
  res.status(201).json({ success: true, data: result.rows[0] });
});
```

**কেন এটা সমস্যা:**

```
❌ SQL query controller এর ভিতরে — একই query দুই জায়গায় লাগলে কপি করতে হবে
❌ ব্যবসার নিয়ম আর HTTP এর কাজ মেশানো
❌ Test লিখতে হলে পুরো Express চালাতে হবে
❌ কাল যদি PostgreSQL ছেড়ে অন্য কিছুতে যাও — controller ও বদলাতে হবে
```

---

## 🏛️ Layered Architecture — চার স্তর

```
┌──────────────────────────────────────────────────────────┐
│  ROUTE          "কোন URL এ কোন ফাংশন"                    │
│  note.routes.js  → পথ, middleware লাগানো                 │
└────────────────────────┬─────────────────────────────────┘
                         ▼
┌──────────────────────────────────────────────────────────┐
│  CONTROLLER     "HTTP এর কথাবার্তা"                       │
│                  req পড়ে, service ডাকে, res পাঠায়        │
│                  ⚠️ কোনো SQL নেই, কোনো ব্যবসার নিয়ম নেই   │
└────────────────────────┬─────────────────────────────────┘
                         ▼
┌──────────────────────────────────────────────────────────┐
│  SERVICE        "ব্যবসার নিয়ম"                            │
│                  validation, সিদ্ধান্ত, একাধিক ধাপ        │
│                  ⚠️ req/res জানেই না                     │
└────────────────────────┬─────────────────────────────────┘
                         ▼
┌──────────────────────────────────────────────────────────┐
│  REPOSITORY     "শুধু SQL"                                │
│                  query চালায়, row ফেরত দেয়                │
│                  ⚠️ HTTP জানে না, নিয়ম জানে না            │
└────────────────────────┬─────────────────────────────────┘
                         ▼
                   PostgreSQL
```

**প্রতিটা স্তরের একটাই দায়িত্ব।** Flutter এর সাথে মিলিয়ে:

```
Flutter                      Backend
────────────                 ────────────
Widget          ←→           Controller   (বাইরের জগতের সাথে কথা)
Bloc / Cubit    ←→           Service      (যুক্তি, সিদ্ধান্ত)
Repository      ←→           Repository   (ডেটার উৎস)
```

চেনা লাগছে? Clean Architecture এর ধারণা backend আর frontend দুই জায়গায় একই।

---

## 💻 Code — একই ফিচার, তিন স্তরে ভাগ

### স্তর ৪ — `src/repositories/note.repository.js`

```js
const { query } = require('../config/db');

const create = async ({ userId, title, content }) => {
  const result = await query(
    `INSERT INTO notes (user_id, title, content)
     VALUES ($1, $2, $3)
     RETURNING id, title, content, created_at, updated_at`,
    [userId, title, content]
  );
  return result.rows[0];
};

const findById = async (noteId, userId) => {
  const result = await query(
    `SELECT id, title, content, created_at, updated_at
     FROM notes WHERE id = $1 AND user_id = $2`,
    [noteId, userId]
  );
  return result.rows[0] || null;
};

const findAll = async ({ userId, search, limit, offset }) => {
  const where = [`user_id = $1`];
  const params = [userId];

  if (search) {
    params.push(`%${search}%`);
    where.push(`(title ILIKE $${params.length} OR content ILIKE $${params.length})`);
  }

  const whereClause = where.join(' AND ');

  const countResult = await query(
    `SELECT COUNT(*) AS total FROM notes WHERE ${whereClause}`,
    params
  );

  params.push(limit, offset);
  const result = await query(
    `SELECT id, title, content, created_at, updated_at
     FROM notes WHERE ${whereClause}
     ORDER BY created_at DESC
     LIMIT $${params.length - 1} OFFSET $${params.length}`,
    params
  );

  return { rows: result.rows, total: Number(countResult.rows[0].total) };
};

const update = async ({ noteId, userId, title, content }) => {
  const result = await query(
    `UPDATE notes
     SET title = COALESCE($1, title),
         content = COALESCE($2, content),
         updated_at = NOW()
     WHERE id = $3 AND user_id = $4
     RETURNING id, title, content, created_at, updated_at`,
    [title, content, noteId, userId]
  );
  return result.rows[0] || null;
};

const remove = async (noteId, userId) => {
  const result = await query(
    `DELETE FROM notes WHERE id = $1 AND user_id = $2 RETURNING id`,
    [noteId, userId]
  );
  return result.rowCount > 0;
};

module.exports = { create, findById, findAll, update, remove };
```

### স্তর ৩ — `src/services/note.service.js`

```js
const noteRepository = require('../repositories/note.repository');
const AppError = require('../utils/AppError');

const MAX_TITLE_LENGTH = 200;
const DEFAULT_LIMIT = 10;
const MAX_LIMIT = 100;

const createNote = async ({ userId, title, content }) => {
  if (!title || title.trim().length === 0) {
    throw new AppError('title is required', 400);
  }
  if (title.length > MAX_TITLE_LENGTH) {
    throw new AppError(`title must be under ${MAX_TITLE_LENGTH} characters`, 400);
  }

  return noteRepository.create({
    userId,
    title: title.trim(),
    content: content || '',
  });
};

const getNoteById = async (noteId, userId) => {
  if (!Number.isInteger(noteId) || noteId <= 0) {
    throw new AppError('Invalid note id', 400);
  }

  const note = await noteRepository.findById(noteId, userId);
  if (!note) throw new AppError('Note not found', 404);

  return note;
};

const getNotes = async ({ userId, search, page, limit }) => {
  const safePage = Math.max(1, Number(page) || 1);
  const safeLimit = Math.min(MAX_LIMIT, Math.max(1, Number(limit) || DEFAULT_LIMIT));
  const offset = (safePage - 1) * safeLimit;

  const { rows, total } = await noteRepository.findAll({
    userId,
    search: (search || '').trim(),
    limit: safeLimit,
    offset,
  });

  return {
    notes: rows,
    meta: {
      total,
      page: safePage,
      limit: safeLimit,
      totalPages: Math.ceil(total / safeLimit),
      hasNextPage: safePage * safeLimit < total,
      hasPrevPage: safePage > 1,
    },
  };
};

const updateNote = async ({ noteId, userId, title, content }) => {
  if (!Number.isInteger(noteId) || noteId <= 0) {
    throw new AppError('Invalid note id', 400);
  }
  if (title === undefined && content === undefined) {
    throw new AppError('Nothing to update. Send title or content', 400);
  }
  if (title !== undefined && title.trim().length === 0) {
    throw new AppError('title cannot be empty', 400);
  }

  const note = await noteRepository.update({
    noteId,
    userId,
    title: title !== undefined ? title.trim() : null,
    content: content !== undefined ? content : null,
  });

  if (!note) throw new AppError('Note not found', 404);
  return note;
};

const deleteNote = async (noteId, userId) => {
  if (!Number.isInteger(noteId) || noteId <= 0) {
    throw new AppError('Invalid note id', 400);
  }

  const deleted = await noteRepository.remove(noteId, userId);
  if (!deleted) throw new AppError('Note not found', 404);

  return { id: noteId };
};

module.exports = { createNote, getNoteById, getNotes, updateNote, deleteNote };
```

### স্তর ২ — `src/controllers/note.controller.js`

```js
const asyncHandler = require('../utils/asyncHandler');
const noteService = require('../services/note.service');

const createNote = asyncHandler(async (req, res) => {
  const note = await noteService.createNote({
    userId: req.user.userId,
    title: req.body.title,
    content: req.body.content,
  });

  res.status(201).json({ success: true, message: 'Note created', data: note });
});

const getNotes = asyncHandler(async (req, res) => {
  const { notes, meta } = await noteService.getNotes({
    userId: req.user.userId,
    search: req.query.search,
    page: req.query.page,
    limit: req.query.limit,
  });

  res.status(200).json({ success: true, data: notes, meta });
});

const getNoteById = asyncHandler(async (req, res) => {
  const note = await noteService.getNoteById(Number(req.params.id), req.user.userId);
  res.status(200).json({ success: true, data: note });
});

const updateNote = asyncHandler(async (req, res) => {
  const note = await noteService.updateNote({
    noteId: Number(req.params.id),
    userId: req.user.userId,
    title: req.body.title,
    content: req.body.content,
  });

  res.status(200).json({ success: true, message: 'Note updated', data: note });
});

const deleteNote = asyncHandler(async (req, res) => {
  const result = await noteService.deleteNote(Number(req.params.id), req.user.userId);
  res.status(200).json({ success: true, message: 'Note deleted', data: result });
});

module.exports = { createNote, getNotes, getNoteById, updateNote, deleteNote };
```

**প্রতিটা controller এখন ৩-৫ লাইন।** পড়লেই বোঝা যায় কী হচ্ছে।

---

## 📁 চূড়ান্ত Folder Structure

```
note-app-backend/
│
├── src/
│   ├── config/
│   │   ├── db.js                    # PostgreSQL Pool
│   │   └── env.js                   # environment variable যাচাই (Lesson 22)
│   │
│   ├── routes/
│   │   ├── auth.routes.js           # /api/auth/*
│   │   └── note.routes.js           # /api/notes/*
│   │
│   ├── controllers/                 # HTTP এর কথাবার্তা
│   │   ├── auth.controller.js
│   │   └── note.controller.js
│   │
│   ├── services/                    # ব্যবসার নিয়ম
│   │   ├── auth.service.js
│   │   └── note.service.js
│   │
│   ├── repositories/                # শুধু SQL
│   │   ├── user.repository.js
│   │   ├── note.repository.js
│   │   └── refreshToken.repository.js
│   │
│   ├── middlewares/
│   │   ├── auth.middleware.js       # JWT যাচাই
│   │   └── error.middleware.js      # 404 + সব error
│   │
│   ├── utils/
│   │   ├── AppError.js
│   │   ├── asyncHandler.js
│   │   └── jwt.js
│   │
│   ├── db/
│   │   └── migrations/
│   │       ├── 001_create_users.sql
│   │       ├── 002_create_notes.sql
│   │       └── 003_create_refresh_tokens.sql
│   │
│   └── app.js                       # Express app বানায়
│
├── server.js                        # app চালু করে
├── .env                             # গোপন তথ্য (git এ নয়)
├── .env.example                     # কী কী লাগবে তার তালিকা
├── .gitignore
└── package.json
```

### `app.js` আর `server.js` আলাদা কেন

```js
// src/app.js — শুধু app বানায়, চালু করে না
const express = require('express');
const authRoutes = require('./routes/auth.routes');
const noteRoutes = require('./routes/note.routes');
const { notFound, errorHandler } = require('./middlewares/error.middleware');

const app = express();

app.use(express.json());
app.get('/health', (req, res) => res.json({ status: 'ok', uptime: process.uptime() }));
app.use('/api/auth', authRoutes);
app.use('/api/notes', noteRoutes);
app.use(notFound);
app.use(errorHandler);

module.exports = app;
```

```js
// server.js — app চালু করে
require('dotenv').config();
const app = require('./src/app');

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
```

**এই ভাগটার আসল উপকার — test লেখার সময়:**

```js
// test ফাইলে
const request = require('supertest');
const app = require('../src/app');       // ← port দখল না করেই test চালানো যায়

test('GET /health', async () => {
  const res = await request(app).get('/health');
  expect(res.status).toBe(200);
});
```

`app.listen()` মেশানো থাকলে প্রতিটা test ফাইল port 5000 দখল করার চেষ্টা করত আর সংঘর্ষ হতো।

---

## 🤔 এই ভাগাভাগি কি বাড়াবাড়ি নয়?

সৎ উত্তর: **ছোট প্রজেক্টে হ্যাঁ, বাড়াবাড়ি।**

```
৩টা API, একজন ডেভেলপার     →  service স্তর অকারণ ঝামেলা
২০+ API, টিমে কাজ           →  এই ভাগ ছাড়া অসম্ভব
```

**কখন স্তর যোগ করবে:**

| লক্ষণ | কী করবে |
|---|---|
| একই SQL দুই জায়গায় লিখতে হচ্ছে | Repository স্তর আনো |
| Controller ৫০+ লাইন হয়ে যাচ্ছে | Service স্তর আনো |
| একই validation বারবার | Service এ সরাও |
| Test লিখতে গিয়ে Express চালাতে হচ্ছে | ভাগটা তোমার দরকার |

আমি এখানে পুরোটা দেখালাম যাতে **কাঠামোটা চিনতে পারো** — যেকোনো production Node প্রজেক্টে ঢুকলে এই ভাগটাই দেখবে। কোথায় কী খুঁজতে হবে জানা থাকবে।

---

## 🔄 Internal Flow — চার স্তরের মধ্য দিয়ে

```
POST /api/notes  { "title": "নতুন নোট" }
        │
        ▼
┌────────────────────────────────────────────────────────┐
│ ROUTE — note.routes.js                                 │
│   router.use(authenticate)  → token যাচাই ✅            │
│   router.post('/', createNote)                         │
└────────────────────┬───────────────────────────────────┘
                     ▼
┌────────────────────────────────────────────────────────┐
│ CONTROLLER — HTTP থেকে ডেটা বের করা                     │
│   req.user.userId → 2                                  │
│   req.body.title  → "নতুন নোট"                          │
│   noteService.createNote({...})                        │
│   ⚠️ SQL এর নামগন্ধ নেই                                 │
└────────────────────┬───────────────────────────────────┘
                     ▼
┌────────────────────────────────────────────────────────┐
│ SERVICE — নিয়ম প্রয়োগ                                   │
│   title খালি? → throw AppError(400)                    │
│   title ২০০ এর বেশি? → throw AppError(400)             │
│   title.trim(), content ফাঁকা হলে ''                    │
│   noteRepository.create({...})                         │
│   ⚠️ req/res কী জিনিস জানেই না                          │
└────────────────────┬───────────────────────────────────┘
                     ▼
┌────────────────────────────────────────────────────────┐
│ REPOSITORY — শুধু SQL                                   │
│   INSERT INTO notes ... RETURNING ...                  │
│   return result.rows[0]                                │
│   ⚠️ HTTP status কী জানে না                             │
└────────────────────┬───────────────────────────────────┘
                     ▼
               PostgreSQL
                     │
                     ▼  row
     Repository → Service → Controller → res.json() → Postman
```

**লক্ষ্য করো:** error যেকোনো স্তরে `throw` হলে asyncHandler ধরে errorHandler এ পাঠায়। মাঝের স্তরগুলোকে error নিয়ে ভাবতেই হয় না।

---

## 🧪 Testing

**আচরণে কোনো পরিবর্তন নেই।** সব API আগের মতোই কাজ করবে — এটাই প্রমাণ করে refactor সফল হয়েছে।

Postman এ আগের সব request আবার চালিয়ে মিলিয়ে দেখো।

> এটাকেই বলে **refactoring** — বাইরের আচরণ এক রেখে ভিতরের গঠন উন্নত করা।

---

## ⚠️ Common Mistakes

| ভুল | কেন খারাপ | সমাধান |
|---|---|---|
| Service এ `req`/`res` ব্যবহার | স্তরের সীমা ভেঙে গেল, test করা কঠিন | সাধারণ argument পাঠাও |
| Repository তে ব্যবসার নিয়ম | নিয়ম দুই জায়গায় ছড়াবে | Service এ রাখো |
| Controller এ সরাসরি SQL | স্তর থাকার মানেই থাকল না | Repository |
| একই ফাইলে সব স্তর | ভাগ করার উদ্দেশ্য ব্যর্থ | আলাদা ফাইল |
| Service এ HTTP status ফেরত দেওয়া | HTTP জ্ঞান নিচে নেমে গেল | `AppError` throw করো |
| শুরুতেই অতিরিক্ত স্তর | ছোট প্রজেক্টে বাড়তি বোঝা | দরকার হলে যোগ করো |

---

## 🏋️ Practice

**১.** ভাবো: PostgreSQL ছেড়ে MongoDB তে যেতে হবে। কোন কোন ফাইল বদলাতে হবে?

<details>
<summary>উত্তর</summary>

**শুধু `repositories/` ফোল্ডার আর `config/db.js`।**

Controller, service, route, middleware — কিচ্ছু ছোঁয়া লাগবে না, কারণ তারা জানেই না ডেটা কোথা থেকে আসে। তারা শুধু `noteRepository.findById(...)` ডাকে আর একটা object পায়।

এটাই স্তরে ভাগ করার সবচেয়ে বড় লাভ — **পরিবর্তন এক জায়গায় আটকে থাকে।**

(বাস্তবে অবশ্য SQL vs document এর পার্থক্যে service এও কিছু সমন্বয় লাগত, কিন্তু ধারণাটা সত্যি।)
</details>

**২.** Service এ `throw new AppError('Note not found', 404)` লিখছি — কিন্তু service তো HTTP জানার কথা নয়। এটা কি নীতিভঙ্গ?

<details>
<summary>উত্তর</summary>

কড়া বিচারে হ্যাঁ — `404` একটা HTTP ধারণা।

কঠোর বিশুদ্ধ পথ হতো: service ছুড়বে `NoteNotFoundError`, আর controller/errorHandler সেটাকে 404 এ অনুবাদ করবে।

বাস্তবে বেশিরভাগ Node প্রজেক্ট এই ব্যবহারিক আপসটা মেনে নেয়, কারণ এতে কোড অনেক কম আর পড়তে সহজ।

**শিক্ষা: স্থাপত্যের নিয়ম হলো দিকনির্দেশ, ধর্মগ্রন্থ নয়।** কখন নিয়ম ভাঙলে লাভ বেশি — সেটা বোঝাই অভিজ্ঞতা।
</details>

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="lesson-22" name="lesson-22"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚢 Lesson 22 — Production Checklist
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

`[■■■■■■■■■■■■■■■■■■■■■■]  22/22  ✅`

| | |
|---|---|
| **আগে যা লাগবে** | Lesson 21 |
| **এই ধাপ শেষে** | সার্ভার deploy করার যোগ্য |
| **নতুন শব্দ** | helmet, CORS, rate limit, graceful shutdown, structured logging |

---

## 🎯 Goal

তোমার সার্ভার এখন কাজ করে। কিন্তু ইন্টারনেটে ছাড়ার আগে আরও কিছু লাগে — কারণ ইন্টারনেট ভদ্র জায়গা নয়।

---

## 💻 ইনস্টল

```bash
npm install helmet cors express-rate-limit compression morgan
```

---

## 1️⃣ Environment Variable যাচাই

### `src/config/env.js`

```js
const required = [
  'PORT',
  'DB_HOST', 'DB_PORT', 'DB_USER', 'DB_NAME',
  'JWT_SECRET', 'REFRESH_TOKEN_SECRET',
];

const validateEnv = () => {
  const missing = required.filter((key) => !process.env[key]);

  if (missing.length > 0) {
    console.error('❌ Missing environment variables:', missing.join(', '));
    process.exit(1);
  }

  if (process.env.JWT_SECRET.length < 32) {
    console.error('❌ JWT_SECRET must be at least 32 characters');
    process.exit(1);
  }

  if (process.env.JWT_SECRET === process.env.REFRESH_TOKEN_SECRET) {
    console.error('❌ JWT_SECRET and REFRESH_TOKEN_SECRET must be different');
    process.exit(1);
  }
};

module.exports = { validateEnv };
```

**কেন এটা প্রথমেই?** কারণ ভুল ধরা পড়ার সবচেয়ে ভালো সময় হলো **সার্ভার চালুর মুহূর্তে**, ব্যবহারকারীর request আসার সময় নয়।

```
যাচাই ছাড়া:  সার্ভার চালু ✅ → ব্যবহারকারী login করতে গেল
             → JWT_SECRET undefined → ক্র্যাশ 💥
             → রাত ৩টায় ফোন আসবে

যাচাই সহ:    সার্ভার চালুই হলো না, পরিষ্কার বার্তা দিল ✅
             → deploy pipeline এই ধরা পড়ল
```

**`process.exit(1)`** — প্রোগ্রাম বন্ধ করো, error code ১ দিয়ে। `0` = সফল, অন্য যেকোনো সংখ্যা = ব্যর্থ। Docker/CI এই code দেখে বুঝে নেয়।

### `.env.example` (এটা git এ যাবে)

```env
PORT=5000
NODE_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=
DB_NAME=noteapp

JWT_SECRET=
JWT_EXPIRES_IN=15m
REFRESH_TOKEN_SECRET=
REFRESH_TOKEN_EXPIRES_IN=7d

CORS_ORIGIN=*
```

**উদ্দেশ্য:** নতুন কেউ (বা ৬ মাস পরের তুমি) দেখেই বুঝবে কী কী লাগে। **মান ফাঁকা** — শুধু চাবিগুলো।

---

## 2️⃣ helmet — HTTP Header নিরাপত্তা

```js
const helmet = require('helmet');
app.use(helmet());
```

এক লাইনে ১৫টার মতো নিরাপত্তা-header বসায়:

| Header | কী ঠেকায় |
|---|---|
| `X-Content-Type-Options: nosniff` | browser কে ফাইলের ধরন অনুমান করা থেকে আটকায় |
| `X-Frame-Options: DENY` | তোমার সাইট iframe এ ঢুকিয়ে clickjacking |
| `Strict-Transport-Security` | সবসময় HTTPS ব্যবহার করতে বাধ্য করে |
| `X-Powered-By` **মুছে দেয়** | "Express" লেখা থাকলে আক্রমণকারী জানত কী আক্রমণ করবে |

শেষেরটা গুরুত্বপূর্ণ — ডিফল্টে Express প্রতিটা response এ নিজের নাম লিখে দেয়। সেটা আক্রমণকারীকে বিনামূল্যে তথ্য দেওয়া।

---

## 3️⃣ CORS

```js
const cors = require('cors');

app.use(cors({
  origin: process.env.CORS_ORIGIN?.split(',') || '*',
  credentials: true,
}));
```

**CORS** = Cross-Origin Resource Sharing। **এটা browser এর নিয়ম** — কোন ওয়েবসাইট তোমার API তে request পাঠাতে পারবে।

```
Flutter মোবাইল app  →  CORS প্রযোজ্য নয় (browser নয়)
Flutter Web         →  প্রযোজ্য ✅
React/Vue           →  প্রযোজ্য ✅
Postman             →  প্রযোজ্য নয়
```

তাই মোবাইল-only অ্যাপে CORS ছাড়াও চলে। কিন্তু ভবিষ্যতে web যোগ হলে লাগবে।

> ⚠️ Production এ `origin: '*'` দিও না — নির্দিষ্ট ডোমেইন লেখো: `https://myapp.com`। `*` মানে পৃথিবীর যেকোনো সাইট তোমার API কল করতে পারবে।

---

## 4️⃣ Rate Limiting — brute force ঠেকানো

```js
const rateLimit = require('express-rate-limit');

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,   // ১৫ মিনিট
  max: 100,                    // প্রতি IP তে ১০০ request
  standardHeaders: true,
  legacyHeaders: false,
  message: { success: false, message: 'Too many requests, please try again later' },
});

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,                      // login এ মাত্র ৫ বার
  skipSuccessfulRequests: true,
  message: { success: false, message: 'Too many login attempts, please try again later' },
});

app.use('/api', apiLimiter);
app.use('/api/auth/login', authLimiter);
app.use('/api/auth/register', authLimiter);
```

**কেন login এ আলাদা, কড়া সীমা?**

```
Rate limit ছাড়া:
  আক্রমণকারী সেকেন্ডে ১০০০ পাসওয়ার্ড চেষ্টা করবে
  → দুর্বল পাসওয়ার্ড কয়েক মিনিটে ভেঙে যাবে
  → আর bcrypt এর কারণে তোমার CPU ১০০% হয়ে সার্ভার সবার জন্য বসে যাবে

Rate limit সহ:
  ১৫ মিনিটে ৫ চেষ্টা → ব্যবহারিকভাবে brute force অসম্ভব ✅
```

**`skipSuccessfulRequests: true`** — সফল login গোনায় ধরে না। ফলে বৈধ ব্যবহারকারী বারবার login করলেও আটকাবে না, শুধু **ব্যর্থ** চেষ্টা গোনা হবে।

> ⚠️ **সীমা:** এই package টা মেমরিতে হিসাব রাখে। একাধিক সার্ভার instance চালালে প্রত্যেকের আলাদা হিসাব হবে। তখন Redis-ভিত্তিক store লাগে (`rate-limit-redis`)।

---

## 5️⃣ Compression আর Logging

```js
const compression = require('compression');
const morgan = require('morgan');

app.use(compression());

app.use(morgan(process.env.NODE_ENV === 'production' ? 'combined' : 'dev'));
```

**compression** — JSON response কে gzip করে পাঠায়। ১০০ KB এর JSON প্রায়ই ১০ KB হয়ে যায়। মোবাইল ব্যবহারকারীর ডেটা আর সময় দুটোই বাঁচে।

**morgan** — প্রতিটা request লগ করে:

```
GET /api/notes 200 45.231 ms - 1250
POST /api/auth/login 401 102.442 ms - 68
```

কখন কোন API কত সময় নিল, কোনটা fail করল — সব দেখা যায়।

---

## 6️⃣ Graceful Shutdown — সবচেয়ে বেশি অবহেলিত অংশ

```js
// server.js
require('dotenv').config();

const { validateEnv } = require('./src/config/env');
validateEnv();

const app = require('./src/app');
const { pool } = require('./src/config/db');

const PORT = process.env.PORT || 5000;

const server = app.listen(PORT, () => {
  console.log(`✅ Server running on port ${PORT} [${process.env.NODE_ENV}]`);
});

const shutdown = async (signal) => {
  console.log(`\n${signal} received. Shutting down gracefully...`);

  server.close(async () => {
    console.log('✅ HTTP server closed');
    try {
      await pool.end();
      console.log('✅ Database pool closed');
      process.exit(0);
    } catch (err) {
      console.error('❌ Error closing pool:', err);
      process.exit(1);
    }
  });

  setTimeout(() => {
    console.error('❌ Forced shutdown after 10s');
    process.exit(1);
  }, 10000);
};

process.on('SIGTERM', () => shutdown('SIGTERM'));
process.on('SIGINT', () => shutdown('SIGINT'));

process.on('unhandledRejection', (reason) => {
  console.error('❌ Unhandled Rejection:', reason);
  shutdown('unhandledRejection');
});

process.on('uncaughtException', (err) => {
  console.error('❌ Uncaught Exception:', err);
  process.exit(1);
});
```

**সমস্যাটা কী:**

```
Graceful shutdown ছাড়া:

deploy শুরু → SIGTERM পাঠাল → process সাথে সাথে মরল 💀
     │
     ├── ৫ জন ব্যবহারকারীর চলমান request মাঝপথে কাটা পড়ল
     ├── DB connection গুলো অসম্পূর্ণ অবস্থায় ঝুলে রইল
     └── অর্ধেক লেখা transaction

Graceful shutdown সহ:

SIGTERM → নতুন request নেওয়া বন্ধ
        → চলমান request গুলো শেষ হতে দাও
        → DB pool পরিচ্ছন্নভাবে বন্ধ করো
        → তারপর মরো ✅
```

| Signal | কে পাঠায় |
|---|---|
| `SIGTERM` | Docker, Kubernetes, hosting — "ভদ্রভাবে বন্ধ হও" |
| `SIGINT` | তুমি, `Ctrl+C` চেপে |

**১০ সেকেন্ডের timeout কেন?** কোনো request যদি আটকে থাকে, অনন্তকাল অপেক্ষা করা যাবে না — তখন জোর করে বন্ধ করতে হয়।

---

## 7️⃣ চূড়ান্ত `src/app.js`

```js
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const compression = require('compression');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');

const authRoutes = require('./routes/auth.routes');
const noteRoutes = require('./routes/note.routes');
const { notFound, errorHandler } = require('./middlewares/error.middleware');

const app = express();

app.set('trust proxy', 1);

app.use(helmet());
app.use(cors({ origin: process.env.CORS_ORIGIN?.split(',') || '*', credentials: true }));
app.use(compression());
app.use(morgan(process.env.NODE_ENV === 'production' ? 'combined' : 'dev'));
app.use(express.json({ limit: '100kb' }));

const apiLimiter = rateLimit({ windowMs: 15 * 60 * 1000, max: 100 });
const authLimiter = rateLimit({ windowMs: 15 * 60 * 1000, max: 5, skipSuccessfulRequests: true });

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', uptime: process.uptime() });
});

app.use('/api', apiLimiter);
app.use('/api/auth/login', authLimiter);
app.use('/api/auth/register', authLimiter);

app.use('/api/auth', authRoutes);
app.use('/api/notes', noteRoutes);

app.use(notFound);
app.use(errorHandler);

module.exports = app;
```

### দুটো সূক্ষ্ম কিন্তু জরুরি লাইন

**`app.set('trust proxy', 1)`**

Production এ সার্ভার সাধারণত reverse proxy (Nginx, Cloudflare) এর পিছনে থাকে। তখন সব request এর IP দেখায় proxy এর IP।

| না দিলে | rate limiter সবাইকে একই ব্যক্তি ভাববে — **একজনের বেশি request এ সবাই ব্লক হয়ে যাবে** |

**`express.json({ limit: '100kb' })`**

| না দিলে | ডিফল্ট সীমা 100kb, কিন্তু স্পষ্ট করে লেখা ভালো। কেউ ৫০ MB এর JSON পাঠিয়ে মেমরি শেষ করে দিতে পারে |

---

## ✅ Deploy করার আগে চূড়ান্ত তালিকা

### নিরাপত্তা
```
[ ] .env কখনো git এ যায়নি (git log --all -- .env দিয়ে যাচাই করো)
[ ] JWT_SECRET ৬৪+ বাইট এলোমেলো, production এ আলাদা
[ ] দুটো secret ভিন্ন
[ ] HTTPS বাধ্যতামূলক (hosting সাধারণত দেয়)
[ ] helmet চালু
[ ] CORS এ নির্দিষ্ট ডোমেইন, '*' নয়
[ ] login/register এ rate limit
[ ] সব SQL এ $1 placeholder (কোথাও string জোড়া নেই)
[ ] কোনো API response এ password_hash নেই
[ ] Production এ stack trace ক্লায়েন্টে যায় না
[ ] DB ব্যবহারকারীর শুধু দরকারি অনুমতি (superuser নয়)
```

### নির্ভরযোগ্যতা
```
[ ] /health route আছে
[ ] Graceful shutdown লেখা
[ ] Connection pool এ সীমা ও timeout সেট
[ ] সব migration production DB তে চালানো হয়েছে
[ ] Database এর স্বয়ংক্রিয় backup চালু
[ ] unhandledRejection / uncaughtException ধরা হয়েছে
[ ] NODE_ENV=production সেট
```

### পর্যবেক্ষণ
```
[ ] Request logging (morgan)
[ ] Error logging
[ ] Error tracking (Sentry ইত্যাদি)
[ ] ধীর query চিহ্নিত করার ব্যবস্থা
```

### পরিচ্ছন্নতা
```
[ ] .env.example হালনাগাদ
[ ] README এ চালানোর নিয়ম লেখা
[ ] package.json এ start script ঠিক
[ ] মেয়াদোত্তীর্ণ refresh_token পরিষ্কারের ব্যবস্থা
```

**শেষটার জন্য একটা query:**

```sql
DELETE FROM refresh_tokens
WHERE expires_at < NOW() - INTERVAL '30 days';
```

দিনে একবার চালালেই যথেষ্ট (cron বা hosting এর scheduled job দিয়ে)।

---

## 🚀 কোথায় deploy করবে

| সেবা | সুবিধা | অসুবিধা |
|---|---|---|
| **Railway** | সবচেয়ে সহজ, PostgreSQL সাথেই | সীমিত ফ্রি |
| **Render** | ফ্রি স্তর আছে, Postgres দেয় | ফ্রি instance ঘুমিয়ে পড়ে |
| **Fly.io** | ব্যবহারকারীর কাছাকাছি চালানো যায় | একটু জটিল |
| **VPS (DigitalOcean)** | পূর্ণ নিয়ন্ত্রণ, সস্তা | Nginx, PM2, SSL নিজে সামলাতে হবে |

শেখার জন্য **Railway বা Render** দিয়ে শুরু করো — GitHub এর সাথে যুক্ত করলে push করলেই deploy হয়ে যায়।

**Deploy এর সময় মনে রাখো:**
1. Hosting এর dashboard এ সব environment variable বসাও (`.env` ফাইল যায় না)
2. `PORT` তারা নিজে দেবে — তোমার কোড ইতিমধ্যেই `process.env.PORT` পড়ে ✅
3. Migration গুলো production DB তে একবার চালাও
4. `NODE_ENV=production` সেট করো

---

## 🎓 তুমি কী শিখলে

```
✅ Node.js server চালু হওয়া, event loop
✅ Express — route, middleware, req/res চক্র
✅ PostgreSQL সংযোগ, connection pool
✅ SQL — CREATE, INSERT, SELECT, UPDATE, DELETE, JOIN-ছাড়া সম্পর্ক
✅ Index কীভাবে query দ্রুত করে
✅ bcrypt — hash, salt, cost factor
✅ JWT — গঠন, signature, মেয়াদ
✅ Middleware দিয়ে API সুরক্ষা
✅ Refresh token, rotation, reuse detection
✅ Logout এবং JWT এর সীমা
✅ SQL Injection ঠেকানো
✅ IDOR ঠেকানো (মালিকানা যাচাই)
✅ Error handling এক জায়গায়
✅ Layered architecture
✅ Production কঠোরীকরণ
```

**এই জ্ঞান দিয়ে তুমি এখন যেকোনো CRUD backend বানাতে পারো।** নোট এর জায়গায় product, order, chat — কাঠামো একই।

---

## 🎯 এরপর কী শিখবে

| বিষয় | কেন |
|---|---|
| **Validation library** (zod) | হাতে লেখা validation এর বদলে |
| **Testing** (Jest + supertest) | পরিবর্তন করলে কিছু ভাঙল কিনা জানা |
| **File upload** (multer + S3) | নোটে ছবি যোগ করতে |
| **Transaction** | একাধিক query একসাথে সফল বা একসাথে ব্যর্থ |
| **Redis** | cache, distributed rate limit |
| **WebSocket** | রিয়েল-টাইম sync |
| **Docker** | "আমার মেশিনে চলে" সমস্যার সমাধান |
| **CI/CD** | push করলেই test + deploy |
| **ORM** (Prisma) | SQL না লিখে DB এর কাজ (তবে SQL আগে শেখাই ঠিক ছিল) |

---

## 🏋️ চূড়ান্ত Practice

তোমার Flutter অ্যাপের জন্য এই backend টা ব্যবহার করো:

```
১. Flutter এ একটা নোট অ্যাপ বানাও
২. Login → দুটো token জমা রাখো (flutter_secure_storage)
৩. Dio interceptor বানাও যেটা প্রতিটা request এ token যোগ করে
৪. 401 + TOKEN_EXPIRED পেলে নীরবে refresh করে retry করো
৫. Infinite scroll — meta.hasNextPage দেখে
৬. Search bar — ?search= দিয়ে
৭. Logout → দুটো token মুছো + সার্ভারে revoke করো
```

এই সাতটা করতে পারলে তুমি পূর্ণ full-stack ডেভেলপার।

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---
---

<a id="ref-flows" name="ref-flows"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📎 Reference 1 — সব Flow Diagram
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## A. সাধারণ Request এর পথ

```
Postman
   ↓
Express Server (port 5000)
   ↓
express.json()          ← body কে object বানায়
   ↓
Router                  ← path + method মিলিয়ে পথ বাছে
   ↓
Middleware              ← token যাচাই
   ↓
Controller              ← req পড়ে, service ডাকে
   ↓
Service                 ← নিয়ম প্রয়োগ
   ↓
Repository              ← SQL লেখে
   ↓
pg Pool                 ← connection ধার দেয়
   ↓
PostgreSQL              ← parse → plan → execute
   ↓
Query Result (rows)
   ↓
Repository → Service → Controller
   ↓
res.json()
   ↓
Postman
```

## B. Register — Password Hash সহ

```
Postman  { name, email, password }
   ↓
express.json() → req.body
   ↓
validation (খালি? ছোট?)
   ↓
bcrypt.hash(password, 10)   ⏱️ ~১০০ms
   ├─ এলোমেলো salt বানায়
   ├─ password + salt
   └─ ১০২৪ চক্র → $2b$10$...
   ↓
INSERT INTO users (name, email, password_hash)
VALUES ($1, $2, $3) RETURNING id, name, email
   ↓
PostgreSQL
   ├─ UNIQUE(email) চেক
   ├─ SERIAL থেকে id
   └─ DEFAULT NOW() → created_at
   ↓
201 Created  (password_hash ছাড়া)
```

## C. Login → JWT

```
Postman  { email, password }
   ↓
SELECT id, name, email, password_hash
FROM users WHERE email = $1
   ↓
PostgreSQL — Index Scan (users_email_key)
   ↓
rows.length === 0 ? → 401 "Invalid email or password"
   ↓
bcrypt.compare(দেওয়া পাসওয়ার্ড, জমা hash)
   ├─ hash থেকে salt বের করে
   ├─ সেই salt দিয়ে নতুন hash বানায়
   └─ তুলনা
   ↓
false ? → 401 (হুবহু একই বার্তা)
   ↓
jwt.sign({userId, email}, JWT_SECRET, {expiresIn:'15m'})
jwt.sign({userId, type:'refresh'}, REFRESH_SECRET, {expiresIn:'7d'})
   ↓
INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
   ↓
200 { user, accessToken, refreshToken }
   ↓
Flutter → flutter_secure_storage এ জমা
```

## D. সুরক্ষিত API — Middleware যাচাই

```
Flutter
   │  GET /api/notes
   │  Authorization: Bearer eyJhbGci...
   ▼
express.json()
   ▼
Router → /api/notes
   ▼
╔═══════════════════════════════════════════════╗
║ authenticate middleware                       ║
║                                               ║
║  ১. req.headers.authorization আছে?            ║
║       না → 401 ⛔                              ║
║  ২. "Bearer " দিয়ে শুরু?                       ║
║       না → 401 ⛔                              ║
║  ৩. split(' ')[1] → token                     ║
║  ৪. jwt.verify(token, SECRET)                 ║
║       • signature হিসাব করে মেলায়              ║
║       • exp দেখে                              ║
║       ব্যর্থ → 401 ⛔                            ║
║  ৫. req.user = { userId, email }              ║
║  ৬. next() 🚪                                  ║
╚═══════════════════╪═══════════════════════════╝
                    ▼
Controller — req.user.userId ব্যবহার করে
                    ▼
SELECT ... WHERE user_id = $1
                    ▼
200 { data }
```

## E. Token Refresh (নীরবে)

```
Flutter                              Server
   │  GET /api/notes (মেয়াদোত্তীর্ণ)    │
   │───────────────────────────────────▶│
   │  401 { code: 'TOKEN_EXPIRED' }     │
   │◀───────────────────────────────────│
   │                                    │
 (ব্যবহারকারী কিছুই দেখে না)             │
   │                                    │
   │  POST /auth/refresh {refreshToken} │
   │───────────────────────────────────▶│
   │                        ১. JWT verify
   │                        ২. sha256 hash → DB খোঁজো
   │                        ৩. revoked? → 🚨 সব বাতিল
   │                        ৪. expired? → 401
   │                        ৫. পুরনোটা revoke
   │                        ৬. নতুন জোড়া ইস্যু
   │  200 { accessToken, refreshToken } │
   │◀───────────────────────────────────│
   │                                    │
   │  GET /api/notes (নতুন token, retry)│
   │───────────────────────────────────▶│
   │  200 { notes } ✅                   │
   │◀───────────────────────────────────│
```

## F. Error এর যাত্রা

```
যেকোনো স্তরে throw new AppError('Note not found', 404)
        ↓
asyncHandler এর .catch(next) ধরল
        ↓
next(err) → Express সব middleware লাফিয়ে পার হলো
        ↓
errorHandler(err, req, res, next)   ← ৪ প্যারামিটার
        ↓
লগ করল
        ↓
err.isOperational ?
   ├─ হ্যাঁ → err.statusCode + err.message
   ├─ PostgreSQL code (23505/23503/22P02) → মানানসই code
   ├─ JWT error → 401
   └─ কিছুই না → 500 "Internal server error"
        ↓
JSON response → Postman / Flutter
```

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---

<a id="ref-sql" name="ref-sql"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📎 Reference 2 — এই প্রজেক্টের সব SQL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## টেবিল তৈরি

```sql
-- 001_create_users.sql
CREATE TABLE IF NOT EXISTS users (
  id            SERIAL       PRIMARY KEY,
  name          VARCHAR(100) NOT NULL,
  email         VARCHAR(255) NOT NULL UNIQUE,
  password_hash TEXT         NOT NULL,
  created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

-- 002_create_notes.sql
CREATE TABLE IF NOT EXISTS notes (
  id         SERIAL       PRIMARY KEY,
  user_id    INTEGER      NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title      VARCHAR(200) NOT NULL,
  content    TEXT         NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_notes_user_created ON notes(user_id, created_at DESC);

-- 003_create_refresh_tokens.sql
CREATE TABLE IF NOT EXISTS refresh_tokens (
  id         SERIAL      PRIMARY KEY,
  user_id    INTEGER     NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  token_hash TEXT        NOT NULL UNIQUE,
  expires_at TIMESTAMPTZ NOT NULL,
  revoked_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_refresh_hash ON refresh_tokens(token_hash);
```

## অ্যাপের সব query

```sql
-- Register
INSERT INTO users (name, email, password_hash)
VALUES ($1, $2, $3)
RETURNING id, name, email, created_at;

-- Login
SELECT id, name, email, password_hash FROM users WHERE email = $1;

-- নিজের তথ্য
SELECT id, name, email, created_at FROM users WHERE id = $1;

-- নোট তৈরি
INSERT INTO notes (user_id, title, content)
VALUES ($1, $2, $3)
RETURNING id, title, content, created_at, updated_at;

-- নোট তালিকা (search + pagination)
SELECT id, title, content, created_at, updated_at
FROM notes
WHERE user_id = $1 AND (title ILIKE $2 OR content ILIKE $2)
ORDER BY created_at DESC
LIMIT $3 OFFSET $4;

-- মোট সংখ্যা
SELECT COUNT(*) AS total FROM notes WHERE user_id = $1;

-- একটা নোট
SELECT id, title, content, created_at, updated_at
FROM notes WHERE id = $1 AND user_id = $2;

-- নোট আপডেট (PATCH)
UPDATE notes
SET title = COALESCE($1, title),
    content = COALESCE($2, content),
    updated_at = NOW()
WHERE id = $3 AND user_id = $4
RETURNING id, title, content, created_at, updated_at;

-- নোট মুছে ফেলা
DELETE FROM notes WHERE id = $1 AND user_id = $2 RETURNING id;

-- Refresh token জমা
INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
VALUES ($1, $2, NOW() + INTERVAL '7 days');

-- Refresh token খোঁজা
SELECT id, user_id, revoked_at, expires_at
FROM refresh_tokens WHERE token_hash = $1;

-- একটা token বাতিল (logout)
UPDATE refresh_tokens SET revoked_at = NOW()
WHERE token_hash = $1 AND user_id = $2 AND revoked_at IS NULL
RETURNING id;

-- সব বাতিল (logout-all)
UPDATE refresh_tokens SET revoked_at = NOW()
WHERE user_id = $1 AND revoked_at IS NULL
RETURNING id;

-- পুরনো token পরিষ্কার (নিয়মিত চালাও)
DELETE FROM refresh_tokens WHERE expires_at < NOW() - INTERVAL '30 days';
```

## psql এর দরকারি কমান্ড

```
psql -d noteapp          ডেটাবেজে ঢোকো
psql -d noteapp -f x.sql ফাইল চালাও
psql -d noteapp -c "SQL" এক লাইনের query

\l          সব database
\c noteapp  database বদলাও
\dt         সব টেবিল
\d users    টেবিলের গঠন
\di         সব index
\x          প্রশস্ত ফলাফল সুন্দরভাবে দেখাও
\q          বেরিয়ে যাও
```

## Query কেমন চলছে দেখা

```sql
EXPLAIN ANALYZE
SELECT * FROM notes WHERE user_id = 2 ORDER BY created_at DESC LIMIT 10;
```

আউটপুটে খোঁজো:

| যা দেখবে | মানে |
|---|---|
| `Index Scan using ...` | ✅ index কাজে লাগছে |
| `Seq Scan on notes` | ⚠️ পুরো টেবিল পড়ছে — index লাগতে পারে |
| `actual time=0.05..0.12` | কত মিলিসেকেন্ড লাগল |
| `rows=10` | কয়টা সারি ফিরল |

## PostgreSQL Data Type — কোনটা কখন

| Type | কখন | মন্তব্য |
|---|---|---|
| `SERIAL` | auto-increment id | ভিতরে INTEGER + SEQUENCE |
| `INTEGER` | সাধারণ সংখ্যা | ±২১০ কোটি |
| `BIGINT` | বিশাল সংখ্যা | ID খুব বেশি হলে |
| `VARCHAR(n)` | সীমিত দৈর্ঘ্যের লেখা | নাম, ইমেইল |
| `TEXT` | দীর্ঘ লেখা | নোটের content, hash |
| `BOOLEAN` | সত্য/মিথ্যা | is_active |
| `TIMESTAMPTZ` | **সময়** | ✅ সবসময় এটা, TIMESTAMP নয় |
| `NUMERIC(10,2)` | টাকা-পয়সা | ❌ FLOAT কখনো নয় |
| `JSONB` | কাঠামোহীন ডেটা | index করা যায় |
| `UUID` | অনুমান-অযোগ্য id | বড় সিস্টেমে |

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---

<a id="ref-postman" name="ref-postman"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📎 Reference 3 — Postman Guide
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## সেটআপ (একবার করলেই হবে)

**১. Collection বানাও:** `Note App Backend`

**২. Environment বানাও:** `Local` — দুটো variable:

```
baseUrl      = http://localhost:5000
accessToken  = (খালি রাখো)
refreshToken = (খালি রাখো)
```

**৩. Login request এ Tests ট্যাবে এই script বসাও** — token স্বয়ংক্রিয়ভাবে জমা হবে:

```javascript
const res = pm.response.json();
if (res.data && res.data.accessToken) {
  pm.environment.set('accessToken', res.data.accessToken);
  pm.environment.set('refreshToken', res.data.refreshToken);
}
```

**৪. Collection এর Authorization ট্যাবে:**

```
Type   : Bearer Token
Token  : {{accessToken}}
```

এখন প্রতিটা request এ হাতে token বসাতে হবে না ✅

---

## সব Request

### 1. Health
```
GET {{baseUrl}}/health
```

### 2. Register
```
POST {{baseUrl}}/api/auth/register
Body → raw → JSON

{ "name": "Yousuf Ali", "email": "yousuf@mail.com", "password": "secret123" }
```

### 3. Login
```
POST {{baseUrl}}/api/auth/login

{ "email": "yousuf@mail.com", "password": "secret123" }
```

### 4. আমি কে
```
GET {{baseUrl}}/api/auth/me
Authorization: Bearer {{accessToken}}
```

### 5. Refresh
```
POST {{baseUrl}}/api/auth/refresh

{ "refreshToken": "{{refreshToken}}" }
```

### 6. Logout
```
POST {{baseUrl}}/api/auth/logout
Authorization: Bearer {{accessToken}}

{ "refreshToken": "{{refreshToken}}" }
```

### 7. নোট তৈরি
```
POST {{baseUrl}}/api/notes
Authorization: Bearer {{accessToken}}

{ "title": "বাজারের তালিকা", "content": "চাল, ডাল, তেল" }
```

### 8. নোট তালিকা
```
GET {{baseUrl}}/api/notes
GET {{baseUrl}}/api/notes?page=2&limit=5
GET {{baseUrl}}/api/notes?search=বাজার
GET {{baseUrl}}/api/notes?search=বাজার&page=1&limit=10
```

### 9. একটা নোট
```
GET {{baseUrl}}/api/notes/1
```

### 10. নোট আপডেট
```
PATCH {{baseUrl}}/api/notes/1

{ "title": "হালনাগাদ তালিকা" }
```

### 11. নোট মুছে ফেলা
```
DELETE {{baseUrl}}/api/notes/1
```

---

## নিরাপত্তা পরীক্ষা (এগুলো অবশ্যই চালাও)

| # | পরীক্ষা | প্রত্যাশিত |
|---|---|---|
| ১ | Token ছাড়া `/api/notes` | 401 |
| ২ | Token এর শেষ ৩ অক্ষর বদলে দাও | 401 Invalid token |
| ৩ | jwt.io তে userId বদলে token বানাও | 401 |
| ৪ | দ্বিতীয় অ্যাকাউন্ট দিয়ে প্রথমজনের নোট চাও | 404 |
| ৫ | Body তে `"userId": 1` পাঠাও | উপেক্ষিত, token এর id ব্যবহার হয় |
| ৬ | `?limit=999999` | সর্বোচ্চ ১০০ |
| ৭ | একই refreshToken দুইবার | 401 reuse detected |
| ৮ | `title` এ `'); DROP TABLE notes; --` | সাধারণ লেখা হিসেবে জমা হয় |
| ৯ | ৬ বার ভুল পাসওয়ার্ডে login | 429 Too many requests |

---

## Status Code — কখন কোনটা

| Code | নাম | আমাদের API তে |
|---|---|---|
| 200 | OK | GET, PATCH, DELETE সফল |
| 201 | Created | register, নোট তৈরি |
| 400 | Bad Request | validation ব্যর্থ |
| 401 | Unauthorized | token নেই/ভুল/মেয়াদ শেষ, ভুল পাসওয়ার্ড |
| 403 | Forbidden | পরিচয় ঠিক, অনুমতি নেই |
| 404 | Not Found | নোট নেই বা অন্যের |
| 409 | Conflict | ইমেইল আগেই আছে |
| 429 | Too Many Requests | rate limit |
| 500 | Internal Error | সার্ভারের বাগ |
| 503 | Unavailable | DB ডাউন |

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---

<a id="ref-trouble" name="ref-trouble"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📎 Reference 4 — Troubleshooting
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Node / Express

| Error | কারণ | সমাধান |
|---|---|---|
| `EADDRINUSE: address already in use :::5000` | port দখলে | `lsof -ti:5000 \| xargs kill -9` |
| `Cannot find module 'express'` | ইনস্টল হয়নি | `npm install` |
| `Cannot find module './src/config/db'` | path ভুল | relative path `./` দিয়ে শুরু |
| `Cannot destructure property 'name' of 'undefined'` | `express.json()` নেই বা Postman এ raw+JSON নয় | দুটোই ঠিক করো |
| `Cannot set headers after they are sent` | দুইবার response | `res.` এর আগে `return` |
| Postman অনন্তকাল ঘুরছে | কোনো `res` পাঠানো হয়নি, বা `next()` নেই | সব পথে response নিশ্চিত করো |
| `await is only valid in async functions` | `async` লিখতে ভুলে গেছ | ফাংশনের আগে `async` |
| `Cannot read properties of undefined (reading 'rows')` | `await` বাদ | `await query(...)` |

## PostgreSQL

| Error | কারণ | সমাধান |
|---|---|---|
| `ECONNREFUSED 127.0.0.1:5432` | PostgreSQL চলছে না | `brew services start postgresql@16` |
| `password authentication failed` | ভুল user/password | `psql postgres` → `\conninfo` |
| `database "noteapp" does not exist` | বানানো হয়নি | `CREATE DATABASE noteapp;` |
| `relation "users" does not exist` | migration চালানো হয়নি | `psql -d noteapp -f ...sql` |
| `duplicate key value violates unique constraint` | ইমেইল আগেই আছে | 409 হিসেবে ধরো (code `23505`) |
| `invalid input syntax for type integer` | `/notes/abc` | id যাচাই করো (code `22P02`) |
| `insert or update violates foreign key` | user নেই | code `23503` → 400 |
| `null value violates not-null constraint` | দরকারি ফিল্ড খালি | code `23502` |
| `too many clients already` | pool এর `max` বেশি বা connection ফাঁস | `max` কমাও |

## JWT / Auth

| উপসর্গ | কারণ | সমাধান |
|---|---|---|
| `secretOrPrivateKey must have a value` | `.env` এ `JWT_SECRET` নেই | যোগ করো, সার্ভার restart |
| সবসময় "Invalid token" | `split(' ')[0]` লিখেছ, বা Postman এ `Bearer ` নেই | `[1]` + prefix |
| যেকোনো পাসওয়ার্ডে login হয়ে যাচ্ছে | `bcrypt.compare` এ `await` নেই | 🚨 এখনই ঠিক করো |
| কেউ login করতে পারছে না | পুরনো ব্যবহারকারীর পাসওয়ার্ড hash করা নেই | পরীক্ষার ডেটা মুছে আবার register |
| Login এর সাথে সাথে token expired | `JWT_EXPIRES_IN` এ ভুল ফরম্যাট (`15` = ১৫ সেকেন্ড) | `'15m'` লেখো |
| Token বদলালেও পাস করছে | `verify` এর বদলে `decode` | 🚨 `verify` ব্যবহার করো |

## ডিবাগ করার কৌশল

**১. SQL query দেখো** — `db.js` এ:

```js
const query = async (text, params) => {
  const start = Date.now();
  const result = await pool.query(text, params);
  console.log('SQL:', text.replace(/\s+/g, ' ').trim());
  console.log('Params:', params, `→ ${result.rowCount} rows, ${Date.now() - start}ms`);
  return result;
};
```

**২. Request কোথা পর্যন্ত পৌঁছাল দেখো:**

```js
app.use((req, res, next) => {
  console.log(`→ ${req.method} ${req.originalUrl}`);
  next();
});
```

**৩. Middleware চলছে কিনা:**

```js
const authenticate = (req, res, next) => {
  console.log('🔐 authenticate চলছে');
  // ...
  console.log('✅ token বৈধ, userId:', decoded.userId);
  next();
};
```

**৪. DB তে সরাসরি দেখো:**

```bash
psql -d noteapp -c "SELECT id, email FROM users;"
psql -d noteapp -c "SELECT id, user_id, title FROM notes ORDER BY id DESC LIMIT 5;"
psql -d noteapp -c "SELECT id, user_id, revoked_at FROM refresh_tokens;"
```

[⬆ সূচিপত্রে ফিরে যাও](#toc)

---

<a id="ref-glossary" name="ref-glossary"></a>

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📎 Reference 5 — শব্দকোষ
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Node / Express

| Term | বাংলা মানে |
|---|---|
| **Runtime** | যে প্রোগ্রাম তোমার কোড পড়ে চালায় (Node = JS এর জন্য) |
| **npm** | Node Package Manager — package নামানোর টুল |
| **Package / Dependency** | অন্যের লেখা কোড যা তুমি ব্যবহার করো |
| **devDependency** | শুধু ডেভেলপমেন্টে লাগে, production এ নয় |
| **Module** | একটা ফাইল, যা `require()` দিয়ে আনা যায় |
| **Server** | সবসময় চালু থেকে request এর অপেক্ষা করে যে প্রোগ্রাম |
| **Port** | একই কম্পিউটারে কোন প্রোগ্রাম, তার নম্বর |
| **Route** | কোন URL এ কোন কোড চলবে তার মানচিত্র |
| **Endpoint** | একটা নির্দিষ্ট API ঠিকানা (`POST /api/notes`) |
| **Middleware** | request আর controller এর মাঝে বসা কোড |
| **Controller** | request নিয়ে কাজ করে response ফেরায় যে ফাংশন |
| **Handler** | একটা route এ যে ফাংশন চলে |
| **Event Loop** | Node এর অন্তহীন চক্র, কাজ থাকলে করে |
| **Callback** | পরে চালানোর জন্য দিয়ে রাখা ফাংশন |
| **Promise** | ভবিষ্যতে আসবে এমন মানের প্রতিশ্রুতি (Dart এর Future) |
| **async / await** | Promise কে সরলভাবে লেখার উপায় |
| **Environment Variable** | কোডের বাইরে রাখা সেটিংস/গোপন তথ্য |

## HTTP

| Term | বাংলা মানে |
|---|---|
| **Request** | ক্লায়েন্ট যা পাঠায় |
| **Response** | সার্ভার যা ফেরত দেয় |
| **Header** | request/response এর সাথে যাওয়া অতিরিক্ত তথ্য |
| **Body** | request/response এর আসল ডেটা |
| **Query Parameter** | `?search=x` — URL এর ঐচ্ছিক অংশ |
| **Route Parameter** | `/notes/:id` — URL এর ভিতরের মান |
| **Status Code** | ফলাফল বোঝানোর সংখ্যা (200, 404, 500) |
| **Stateless** | সার্ভার আগের request মনে রাখে না |
| **CORS** | কোন ওয়েবসাইট তোমার API কল করতে পারবে |
| **Rate Limiting** | নির্দিষ্ট সময়ে সর্বোচ্চ কত request |

## Database

| Term | বাংলা মানে |
|---|---|
| **Table** | একই ধরনের অনেক রেকর্ডের সংগ্রহ |
| **Row / Record** | একটা রেকর্ড |
| **Column / Field** | একটা বৈশিষ্ট্য |
| **Query** | Database কে করা প্রশ্ন (SQL) |
| **Primary Key** | প্রতিটা row কে আলাদা চেনার column |
| **Foreign Key** | অন্য টেবিলের row কে নির্দেশ করা column |
| **Constraint** | Database এর নিয়ম (NOT NULL, UNIQUE) |
| **Index** | দ্রুত খোঁজার জন্য আলাদা সাজানো কাঠামো |
| **Connection Pool** | আগে থেকে খুলে রাখা DB সংযোগের ভাণ্ডার |
| **Migration** | Database এর গঠন বদলানোর লিখিত ধাপ |
| **Transaction** | একগুচ্ছ query — সব সফল বা সব বাতিল |
| **MVCC** | একই ডেটার একাধিক সংস্করণ রাখার পদ্ধতি |
| **WAL** | Write-Ahead Log — দুর্ঘটনায় ডেটা বাঁচায় |
| **VACUUM** | মৃত row পরিষ্কার করা |

## নিরাপত্তা

| Term | বাংলা মানে |
|---|---|
| **Authentication** | তুমি কে? (পরিচয় প্রমাণ) |
| **Authorization** | তুমি কী করতে পারো? (অনুমতি) |
| **Hash** | এক দিকে যাওয়া রূপান্তর, ফেরানো যায় না |
| **Salt** | Hash এর সাথে মেশানো এলোমেলো লেখা |
| **Cost Factor** | bcrypt কতটা ধীর হবে (২^n চক্র) |
| **Token** | পরিচয়পত্র হিসেবে দেওয়া স্বাক্ষরিত লেখা |
| **JWT** | JSON Web Token — header.payload.signature |
| **Payload** | Token এর ভিতরের ডেটা (এনক্রিপ্টেড নয়!) |
| **Signature** | Token জাল কিনা প্রমাণ করার স্বাক্ষর |
| **Access Token** | ছোট মেয়াদ, প্রতিটা API কলে যায় |
| **Refresh Token** | বড় মেয়াদ, নতুন access token আনে |
| **Rotation** | প্রতিবার refresh এ নতুন token, পুরনোটা বাতিল |
| **Reuse Detection** | একই refresh token দুইবার এলে চুরি ধরা |
| **SQL Injection** | ইনপুট দিয়ে SQL কমান্ড ঢুকিয়ে দেওয়া |
| **IDOR** | অন্যের id পাঠিয়ে অন্যের ডেটা পড়া |
| **Brute Force** | একের পর এক পাসওয়ার্ড চেষ্টা |
| **User Enumeration** | কোন ইমেইল নিবন্ধিত তা বের করে ফেলা |
| **Rainbow Table** | আগে থেকে বানানো hash এর তালিকা |

## স্থাপত্য

| Term | বাংলা মানে |
|---|---|
| **Layered Architecture** | কাজ অনুযায়ী স্তরে ভাগ |
| **Service Layer** | ব্যবসার নিয়ম যেখানে থাকে |
| **Repository Layer** | শুধু database এর কাজ |
| **Separation of Concerns** | এক জিনিস এক জায়গায় |
| **Refactoring** | আচরণ এক রেখে গঠন উন্নত করা |
| **Graceful Shutdown** | চলমান কাজ শেষ করে তারপর বন্ধ হওয়া |
| **Idempotent** | একবার বা দশবার — ফলাফল এক |
| **Race Condition** | দুই কাজ একসাথে চলে গোলমাল করা |

---

# 🎓 সমাপ্তি

```
২২টা lesson  ·  ৬টা পর্ব  ·  ১টা কাজ করা backend

Postman ─── Express ─── PostgreSQL
    সবটা তুমি নিজে বুঝে বানালে
```

এখন এই backend টা চালু রেখে তোমার Flutter অ্যাপ থেকে কল করো।
যে জিনিসটা এতদিন "রহস্যময় API" ছিল, সেটা এখন তোমার নিজের লেখা কোড।

**[⬆ সূচিপত্রে ফিরে যাও](#toc)**

