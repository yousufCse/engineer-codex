# 📘 CHAPTER 3 — Node.js Core
### "Runtime-এর অন্দরমহল — Event Loop, Streams, Core Modules"
#### Progress: [████░░░░░░░░░░░░░░░] 20%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 2](./chapter-02-javascript-backend.md) | [➡ Ch 4](./chapter-04-expressjs.md)

---

## Node.js-এর Architecture

Node.js চারটা প্রধান অংশ নিয়ে গঠিত:

**V8 Engine:** JavaScript code machine code-এ compile করে। Memory management ও garbage collection এখানে।

**libuv:** C++ library। Cross-platform asynchronous I/O। Event Loop এবং Thread Pool এখানে।

**Node.js Bindings:** JavaScript এবং C++ (V8, libuv)-এর মধ্যে bridge।

**Core Modules:** Built-in modules — `fs`, `http`, `path`, `crypto`। JavaScript এবং C++ মিলিয়ে লেখা।

---

## Event Loop — বিস্তারিত

Event Loop single thread-এ হাজারো concurrent connection handle করে। এর phases:

**Timers Phase:** `setTimeout` ও `setInterval` callback যেগুলোর delay শেষ।

**Pending Callbacks Phase:** পূর্ববর্তী iteration-এ defer করা I/O callback।

**Idle, Prepare:** Internal use।

**Poll Phase:** নতুন I/O event-এর জন্য অপেক্ষা এবং I/O callback execute।

**Check Phase:** `setImmediate()` callback।

**Close Callbacks Phase:** Socket close, server close callback।

প্রতিটা phase-এর মাঝে **Microtask Queue** (Promise callback, `process.nextTick()`) drain হয়। `process.nextTick()` এর priority সর্বোচ্চ — পরের event loop iteration-এর আগেই চলে।

---

## Blocking vs Non-Blocking I/O

Traditional server একটা request-এর জন্য একটা thread তৈরি করে। ১০,০০০ concurrent connection মানে ১০,০০০ thread — প্রতিটা ১-৮MB, মোট ১০-৮০ GB memory।

Node.js এই সমস্যা সমাধান করে non-blocking I/O দিয়ে। Database query পাঠানো হলে OS-কে বলা হয় "কাজ করো, শেষ হলে জানাও"। OS-এর কাছে কাজ দিয়ে Node.js অন্য request handle করে। OS কাজ শেষ করলে Event Loop-এ callback আসে।

**Node.js-এর দুর্বলতা:** CPU-intensive কাজে (ভারী calculation, image processing)। কারণ thread তখন সত্যিই ব্যস্ত — অন্য request serve হয় না। সমাধান: Worker Threads বা separate microservice।

---

## Thread Pool — লুকানো Threads

Node.js single-threaded নয় সম্পূর্ণভাবে। libuv 4টা thread pool রাখে (default)। কিছু কাজ OS asynchronously করতে পারে না:
- File system operations
- DNS lookup (`dns.lookup`)
- কিছু crypto operations
- Native addons

Network I/O (TCP, UDP) thread pool ব্যবহার করে না — OS-এর native async mechanism ব্যবহার করে (Linux: epoll, macOS: kqueue, Windows: IOCP)।

`UV_THREADPOOL_SIZE` environment variable দিয়ে thread pool বাড়ানো যায়।

---

## Module System ও Caching

CommonJS-এ `require()` প্রথমবার module load করে cache করে। পরের বার file পড়া হয় না — cached version return। Module একবারই initialize হয় — **Singleton pattern** automatically।

এই কারণে database connection module-এ রাখলে একবারই connection হয়, সব request-এ reuse হয়।

**Circular Dependency:** Module A → Module B → Module A। Node.js partially exported object দিয়ে handle করে, কিন্তু অপ্রত্যাশিত behavior হতে পারে। এড়িয়ে চলাই ভালো।

---

## Core Modules

**`path`:** File path — OS-independent। Windows backslash, Unix forward slash — `path` module এই পার্থক্য handle করে। `join()`, `resolve()`, `dirname()`, `basename()`, `extname()`।

**`fs`:** File system। প্রতিটা operation-এর sync এবং async version। Production-এ সবসময় async — sync version Event Loop block করে। `fs.promises` API async/await-এর সাথে সহজে কাজ করে।

**`http`:** HTTP server তৈরির built-in module। Express এই module-এর উপরে তৈরি। সরাসরি ব্যবহার করলে routing, middleware manually করতে হয়।

**`crypto`:** Hash (SHA-256), HMAC, random bytes, encryption/decryption। Password hashing-এ সরাসরি না ব্যবহার করে `bcryptjs` — কারণ bcrypt timing-safe এবং automatically salt যোগ করে।

**`events`:** EventEmitter class — Node.js-এর event-driven architecture-এর মূল। HTTP server, streams সব EventEmitter extend করে। `emit()` দিয়ে event fire, `on()` দিয়ে listener।

**`os`:** CPU, memory, hostname, platform information।

---

## Streams — Efficient Data Processing

Stream হলো ডেটা টুকরো টুকরো (chunk) করে process করার mechanism। 1GB file একবারে load করলে 1GB RAM ব্যবহার হয়। Stream দিয়ে করলে শুধু current chunk memory-তে।

**চার ধরনের Stream:**

**Readable:** Data পড়া যায়। File read, HTTP request।

**Writable:** Data লেখা যায়। File write, HTTP response।

**Duplex:** পড়া এবং লেখা দুটোই। TCP socket।

**Transform:** Duplex-এর বিশেষ ধরন — ডেটা পরিবর্তন করে। Compression (zlib), encryption।

**Backpressure:** Readable stream যদি Writable-এর চেয়ে দ্রুত ডেটা উৎপাদন করে, memory-তে queue তৈরি হয়। Writable বলে "আমি ready না" এবং Readable pause করে। `pipe()` method automatically backpressure handle করে।

---

## Error Handling Patterns

**`process.on('uncaughtException')`:** Unhandled synchronous error। Graceful shutdown-এর জন্য ব্যবহার করা যায়, কিন্তু application state corrupt থাকতে পারে — restart করাই সঠিক।

**`process.on('unhandledRejection')`:** Unhandled Promise rejection। Node.js 15+-এ process exit করে।

**Graceful Shutdown:** নতুন connection বন্ধ → existing connection শেষের জন্য অপেক্ষা → database connection বন্ধ → process exit। এটা না করলে in-flight request ক্ষতিগ্রস্ত হতে পারে।

---

## Environment Variables

Application-এর configuration code-এ hardcode করা উচিত নয়:
- Development এবং production-এ ভিন্ন config দরকার।
- Secret (password, API key) Git-এ যাওয়া উচিত নয়।

`process.env` দিয়ে environment variable পড়া হয়। `.env` file-এ development config রাখা হয়, `dotenv` package সেটা `process.env`-এ load করে। `.env` সবসময় `.gitignore`-এ থাকবে। `.env.example` (value ছাড়া) commit করতে হয়।

---

## মূল উপলব্ধি

Node.js-এর শক্তি event-driven, non-blocking I/O architecture থেকে আসে। Event Loop-এ synchronous heavy কাজ করলে Node.js-এর সব সুবিধা নষ্ট হয়। Stream ব্যবহার করলে বড় ডেটা efficient-ভাবে handle হয়। Module caching বুঝলে Singleton pattern এবং database connection management স্বাভাবিকভাবে সঠিক হয়।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 2](./chapter-02-javascript-backend.md) | [➡ Ch 4](./chapter-04-expressjs.md)
