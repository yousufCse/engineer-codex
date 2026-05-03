# 📘 CHAPTER 2 — JavaScript for Backend
### "Modern JavaScript — async, modules, closures"
#### Progress: [███░░░░░░░░░░░░░░░░] 15%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 1](./chapter-01-internet-http.md) | [➡ Ch 3](./chapter-03-nodejs-core.md)

---

## JavaScript কেন Backend-এ?

JavaScript মূলত Netscape-এ Brendan Eich 1995 সালে মাত্র 10 দিনে তৈরি করেছিলেন — browser-এর ভেতরে interactive webpage তৈরির জন্য। তখন কেউ ভাবেনি এটা server-এও চলবে। Node.js আসার পর একই language-এ frontend এবং backend দুটোই লেখা সম্ভব হয়েছে।

---

## V8 Engine — JavaScript কীভাবে চলে?

JavaScript একটা interpreted language ছিল — প্রতিটা line সরাসরি execute হতো। কিন্তু V8 engine এটা বদলে দিয়েছে।

V8 JavaScript-কে সরাসরি machine code-এ compile করে — এটাকে JIT (Just-In-Time) compilation বলে।

V8 দুটো compiler ব্যবহার করে:

**Ignition (baseline compiler):** Code প্রথমবার চললে দ্রুত bytecode-এ compile করে।

**TurboFan (optimizing compiler):** যে code বার বার চলে সেটা "hot" হিসেবে চিহ্নিত হয় এবং TurboFan highly optimized machine code-এ compile করে।

এই কারণে JavaScript অনেক ক্ষেত্রে Python বা PHP-এর চেয়ে দ্রুত।

---

## Execution Context ও Call Stack

JavaScript single-threaded — একবারে একটাই কাজ করতে পারে, এটা Call Stack দিয়ে manage হয়।

**Execution Context:** প্রতিটা function call একটা নতুন execution context তৈরি করে। এতে থাকে local variables, scope chain, এবং `this` binding।

**Call Stack:** LIFO (Last In, First Out) stack। Function call হলে context push হয়, শেষ হলে pop হয়। অসীম recursion-এ stack overflow হয়।

---

## Scope ও Closure

**Scope:** কোথা থেকে কোন variable দেখা যাবে। Global, Function, এবং Block (ES6+) scope আছে।

`var` function-scoped — for loop-এর মধ্যে declare করা `var` loop-এর বাইরেও দেখা যায়, এটা একটা সাধারণ bug-এর উৎস। `let` এবং `const` block-scoped, তাই আধুনিক JavaScript-এ `var` ব্যবহার করা হয় না।

**Lexical Scoping:** Function কোথায় define হয়েছে সেটার উপর ভিত্তি করে outer variable accessible — কোথায় call হয়েছে সেটা দিয়ে নয়।

**Closure:** একটা function তার lexical scope মনে রাখে — এমনকি সেই scope-এর বাইরে execute হলেও। Backend-এ middleware, callback, এবং module pattern-এ closure অপরিহার্য। Private variable তৈরি করতেও closure ব্যবহার হয়।

---

## Asynchronous JavaScript — কেন দরকার?

JavaScript single-threaded। Database query করতে ৫০০ms লাগলে, সেই সময় অন্য কোনো request serve করা যাবে না — যদি synchronously করা হয়। Asynchronous programming এই সমস্যার সমাধান।

**Event Loop:**

Event Loop হলো JavaScript-এর concurrency mechanism। এর অংশগুলো:

- **Call Stack:** Synchronous code চলে এখানে।
- **Web APIs / Node.js APIs:** setTimeout, HTTP request — এগুলো JavaScript engine-এর বাইরে OS level-এ চলে।
- **Microtask Queue:** Promise callback এখানে আসে। Highest priority।
- **Callback Queue (Task Queue):** setTimeout এর callback এখানে।
- **Event Loop:** Call Stack খালি হলে Microtask Queue drain করে, তারপর Callback Queue থেকে একটা নেয়।

**Callbacks:** Async কাজ শেষ হলে যে function call হয়। Nested callback-এর সমস্যাকে "Callback Hell" বলে — code পড়া এবং error handling কঠিন হয়।

**Promise:** ভবিষ্যতে আসবে এমন value-এর object। তিনটা state: Pending, Fulfilled, Rejected। একবার settled হলে পরিবর্তন হয় না। `.then()` এবং `.catch()` দিয়ে chaining করা যায় — callback hell এড়ানো যায়।

**async/await:** Promise-এর syntactic sugar। Asynchronous code-কে synchronous-এর মতো দেখায়। `async` function-এ `await` ব্যবহার করা যায়। `try/catch` দিয়ে error handle করা যায়।

---

## Modules — কোড Organize করার পদ্ধতি

**CommonJS (CJS):** Node.js-এর পুরনো system। `require()` synchronous। Module একবার load হলে cache হয় — Singleton pattern automatically।

**ES Modules (ESM):** Modern standard। `import`/`export`। Static analysis সম্ভব — tree shaking (unused code বাদ) করা যায়। Top-level-এ লিখতে হয়।

Module caching গুরুত্বপূর্ণ: database connection module-এ রাখলে একবারই connection হয়, সব জায়গায় reuse হয়।

---

## Error Handling

**Synchronous:** `try/catch`।

**Asynchronous:** async/await function-এ `try/catch`। Promise-এ `.catch()`।

**Unhandled Promise Rejection:** সব Promise-এর error handle করা আবশ্যক। Production-এ unhandled rejection process crash করে।

**Custom Error:** Error class extend করে নির্দিষ্ট error type তৈরি করা হয় — `message`, `statusCode`, `isOperational` property সহ।

---

## Prototype ও `this`

JavaScript prototype-based OOP। প্রতিটা object-এর `[[Prototype]]` hidden link। Property খুঁজলে object-এ না পেলে prototype-এ যায় — `null` পর্যন্ত এটাই prototype chain।

`this`-এর মান নির্ভর করে function কীভাবে call হচ্ছে তার উপর। Arrow function-এ নিজস্ব `this` নেই — surrounding scope-এর `this` inherit করে। এই কারণে callback-এ arrow function ব্যবহার করলে `this` confusion এড়ানো যায়।

---

## মূল উপলব্ধি

Backend-এ async programming বোঝাটা সবচেয়ে গুরুত্বপূর্ণ — প্রায় প্রতিটা কাজ (database query, HTTP request, file operation) asynchronous। `var`-এর বদলে `let`/`const`, callback-এর বদলে async/await, CommonJS-এর পাশাপাশি ESM — এই modern practices জানলে পরিষ্কার এবং predictable code লেখা সম্ভব।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 1](./chapter-01-internet-http.md) | [➡ Ch 3](./chapter-03-nodejs-core.md)
