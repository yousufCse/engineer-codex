# 📘 CHAPTER 0 — Development Environment
### "সঠিক পরিবেশ তৈরি করো — কোড লেখার আগে"
#### Progress: [█░░░░░░░░░░░░░░░░░░] 5%

[⬆ TOC](./table-of-contents.md) | [➡ Chapter 1](./chapter-01-internet-http.md)

---

## Development Environment কী এবং কেন দরকার?

একজন ছুতার মিস্ত্রি কাজ শুরু করার আগে তার করাত, হাতুড়ি, পেরেক — সব গুছিয়ে রাখে। সব হাতিয়ার যদি একটা নির্দিষ্ট জায়গায় না থাকে, কাজের মাঝে হাতিয়ার খুঁজতে হয় — সময় নষ্ট হয়, মনোযোগ ভাঙে।

একজন backend developer-এর "হাতিয়ার" হলো তার development environment। এটা হলো সেই পুরো সিস্টেম যেখানে সে কোড লেখে, চালায়, পরীক্ষা করে এবং ত্রুটি ধরে। Environment ভালো না হলে প্রতিটা ছোট কাজে বাধা আসে।

Development environment মূলত কয়েকটা স্তরে ভাগ করা যায়:

**Runtime (যে পরিবেশে কোড চলে):** JavaScript কোড চালাতে হলে একটা runtime দরকার। Browser-এ এই runtime built-in আছে। কিন্তু server-এ চালাতে হলে Node.js দরকার — এটাই server-side JavaScript runtime।

**Editor (যেখানে কোড লেখা হয়):** যেকোনো text editor-এ কোড লেখা যায়। তবে ভালো editor syntax highlight করে, ত্রুটি দেখায়, auto-complete দেয় — কাজ অনেক দ্রুত হয়।

**Package Manager:** আধুনিক software এককভাবে তৈরি হয় না। অনেক third-party library ব্যবহার করতে হয়। npm এই library গুলো download, install, update, এবং version manage করে।

**Version Control:** কোড লেখার সময় পরীক্ষা-নিরীক্ষা হয়। কোনো পরিবর্তন ভুল হলে আগের অবস্থায় ফিরতে হয়। Git এই কাজ করে।

---

## Node.js — কেন এবং কীভাবে?

JavaScript মূলত browser-এর ভাষা ছিল। 2009 সালে Ryan Dahl একটা প্রশ্ন করেছিলেন: browser-এর বাইরে, server-এ JavaScript চালানো গেলে কেমন হতো?

তিনি Chrome-এর V8 JavaScript engine নিলেন — যেটা Google তৈরি করেছে এবং অত্যন্ত দ্রুত JavaScript compile করে — এবং সেটাকে একটা C++ wrapper-এর মধ্যে রাখলেন। এর ফলে JavaScript server-এ চলতে পারে, file system access করতে পারে, network connection তৈরি করতে পারে। এটাই Node.js।

**Node.js একটা runtime, কোনো framework নয়, কোনো language-ও নয়।** এটা JavaScript কোড execute করার পরিবেশ। এটা libuv নামের একটা C library ব্যবহার করে asynchronous I/O করার জন্য, যা Node.js-এর non-blocking প্রকৃতির মূল কারণ।

**LTS (Long Term Support) কেন বেছে নিতে হয়:**

Node.js দুই ধরনের release দেয়। Current version-এ সর্বশেষ features থাকে, কিন্তু প্রতি কয়েক মাসে বড় পরিবর্তন হতে পারে — production-এ এটা ঝুঁকিপূর্ণ। LTS version নির্দিষ্ট সময়ের জন্য stable থাকে। Breaking change হয় না, শুধু security patch আসে। যেকোনো production system-এ সবসময় LTS version ব্যবহার করতে হয়।

**nvm (Node Version Manager) কেন দরকার:**

একটা computer-এ একাধিক project থাকতে পারে যেগুলো ভিন্ন Node.js version require করে। Project A চালাতে Node 18 দরকার, Project B চালাতে Node 20। nvm এক machine-এ একাধিক Node.js version install করতে এবং project-ভেদে switch করতে দেয়।

---

## npm — Package Management এর দর্শন

Software তৈরির সময় সবকিছু নিজে লেখা অর্থহীন। Authentication logic, database connection, email sending — এসব common সমস্যার solution হাজার জন developer আগেই লিখে open করে দিয়েছে। এই ready-made solution গুলোকে "package" বা "library" বলে।

npm হলো এই packages-এর বিশাল repository। ২০২৬ সালে npm registry-তে ২৫ লক্ষের বেশি package আছে।

**`package.json` ফাইলের ভূমিকা:**

একটা project-এ কোন packages দরকার, কোন version দরকার — এই তথ্য রাখা হয় `package.json`-এ। এই ফাইলটা হলো project-এর "পরিচয়পত্র" এবং "কেনাকাটার তালিকা"। কেউ তোমার project clone করলে শুধু `npm install` চালালেই সব dependencies automatically download হয়ে যায়।

**`node_modules` ফোল্ডার কখনো Git-এ push করা হয় না** — কারণ এটা পুনরায় generate করা যায়, এবং এর আকার হাজার হাজার ফাইলে পৌঁছাতে পারে।

**dependencies vs devDependencies পার্থক্য:**

dependencies হলো সেই packages যেগুলো production server-এও দরকার — যেমন express, mongoose। devDependencies শুধু development-এর সময় দরকার — যেমন nodemon (auto-restart), jest (testing)। Production server-এ devDependencies install না করলেও চলে।

**Semantic Versioning (SemVer):**

npm packages তিনটা সংখ্যা দিয়ে version নির্ধারণ করে: `major.minor.patch` — যেমন `4.18.2`।
- Patch (শেষেরটা) বাড়লে bug fix হয়েছে।
- Minor (মাঝেরটা) বাড়লে নতুন feature এসেছে, কিন্তু পুরনো code ভাঙবে না।
- Major (প্রথমটা) বাড়লে breaking change এসেছে — পুরনো code কাজ নাও করতে পারে।

`^4.18.0` লেখার মানে হলো major version 4 ঠিক রেখে যেকোনো নতুন minor বা patch version acceptable।

**`package-lock.json` কেন দরকার:**

তুমি হয়তো লিখলে `"express": "^4.18.0"` — দুই সপ্তাহ পর নতুন express version আসলে অন্য developer-এর machine-এ ভিন্ন version install হতে পারে। `package-lock.json` ঠিক কোন version install হয়েছে সেটা lock করে রাখে। এটাও Git-এ commit করতে হয় যাতে সবার environment identical থাকে।

---

## VS Code — শুধু editor নয়, একটা ecosystem

VS Code Microsoft-এর তৈরি open-source editor। এটা Language Server Protocol (LSP) ব্যবহার করে — language-specific intelligence (autocomplete, error checking) আলাদা "language server" হিসেবে চলে। ফলে যেকোনো language support করা সম্ভব।

**ESLint কেন দরকার:**

JavaScript-এ অনেক ধরনের সাধারণ ভুল আছে যেগুলো code চালানোর আগেই ধরা সম্ভব। ESLint statically code analyze করে এবং সম্ভাব্য ত্রুটি বা bad practice দেখায়। এটা একটা automatic code reviewer — কোড চালানোর আগেই বলে দেয় "এখানে সমস্যা আছে"।

**Prettier কেন দরকার:**

Code formatting হলো code দেখতে কেমন হবে — indentation, semicolon, quote style। Team-এ ১০ জন developer থাকলে ১০ রকম formatting style হতে পারে। Prettier সবার কোড automatically একই format-এ নিয়ে আসে। Code review-এ formatting নিয়ে বিতর্ক শেষ হয়।

---

## Git ও Version Control — ইতিহাসের দর্শন

কল্পনা করো তুমি একটা document-এ কাজ করছো: `document_v1.docx`, `document_v2.docx`, `document_final.docx`, `document_final_ACTUAL_FINAL.docx` — এটা অব্যবস্থাপনার উদাহরণ। Git এই সমস্যার elegant সমাধান।

**Git-এর অভ্যন্তরীণ architecture:**

Git একটা content-addressable filesystem। এটা চারটা object type ব্যবহার করে:

**Blob:** একটা file-এর content। File-এর নাম বা অবস্থান সংরক্ষিত হয় না — শুধু content।

**Tree:** একটা directory-এর snapshot। কোন blob (file) কোন নামে আছে সেটা রাখে।

**Commit:** একটা tree-কে point করে এবং metadata রাখে — লেখক, সময়, এবং parent commit-এর reference।

**Tag:** একটা commit-এর named reference।

প্রতিটা object-এর SHA-1 hash তার content থেকে calculate করা হয়। ফলে কোনো ইতিহাস পরিবর্তন করলে সব পরবর্তী hash বদলে যায় — এটাই Git-এর data integrity নিশ্চিত করে।

**তিনটা অঞ্চল:**

Working Directory-তে তুমি সরাসরি file edit করো। `git add` করলে পরিবর্তন Staging Area (Index)-এ যায় — এখানে তুমি ঠিক করো পরের commit-এ কী কী যাবে। `git commit` করলে staged পরিবর্তন Repository-তে permanently সংরক্ষিত হয়।

**Branch কীভাবে কাজ করে:**

Branch আসলে শুধু একটা pointer — সর্বশেষ commit-কে point করে। Branch তৈরি করা মানে একটা নতুন pointer তৈরি। এটা কোনো file copy করে না। তাই branch তৈরি করা এবং switch করা প্রায় instant।

---

## Postman ও API Testing — কেন Frontend ছাড়া test করতে হয়?

Backend তৈরি করার সময় frontend এখনো তৈরি হয়নি। API ঠিকমতো কাজ করছে কিনা বুঝবে কীভাবে? Postman বা Thunder Client HTTP client হিসেবে কাজ করে — যেকোনো HTTP request পাঠানো যায়, response দেখা যায়।

Browser-এ শুধু GET request সহজে করা যায়। POST body দেওয়া, custom headers যোগ করা, authentication token পাঠানো — এসব browser-এ manually করা কঠিন। API testing tool এই সব সহজ করে।

---

## মূল উপলব্ধি

Development environment setup মানে শুধু software install নয়। এটা একটা professional কার্যপরিবেশ তৈরি — যেখানে প্রতিটা tool তার নির্দিষ্ট কাজ করে, সব tools একসাথে কাজ করে, পরিবর্তন track করা যায়, এবং অন্যরা সহজে তোমার environment reproduce করতে পারে।

এই পরিবেশ একবার ভালোভাবে সাজালে পরের সব কাজ মসৃণ হয়।

---

[⬆ TOC](./table-of-contents.md) | [➡ Chapter 1: Internet & HTTP](./chapter-01-internet-http.md)
