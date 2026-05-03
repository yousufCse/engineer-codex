# 📘 CHAPTER 4 — Express.js
### "HTTP-এর উপরে একটা স্তর — Middleware Architecture ও Routing"
#### Progress: [█████░░░░░░░░░░░░░░] 25%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 3](./chapter-03-nodejs-core.md) | [➡ Ch 5](./chapter-05-postgresql.md)

---

## Express কী এবং কেন?

Node.js-এর built-in `http` module দিয়ে HTTP server তৈরি করা সম্ভব। কিন্তু প্রতিটা request-এ manually URL parse করতে হবে, method চেক করতে হবে, header পাঠাতে হবে — সব কিছু boilerplate code। একটা real application-এ এটা দ্রুত unmanageable হয়ে যায়।

Express.js হলো Node.js-এর উপরে একটা minimal, unopinionated web framework। এটা `http` module-কে wrap করে এবং routing, middleware, request/response abstraction সরবরাহ করে। "Unopinionated" মানে Express বলে না কোন folder structure ব্যবহার করো, কোন ORM ব্যবহার করো, কোথায় কী রাখো — developer সম্পূর্ণ স্বাধীন।

Express-এর philosophy সরল: request আসে, middleware chain-এর ভেতর দিয়ে যায়, একটা route handler response পাঠায়।

---

## Middleware — Express-এর মূল কাঠামো

Middleware হলো Express-এর সবচেয়ে গুরুত্বপূর্ণ concept। Middleware একটা function যেটা request এবং response object-এ access পায় এবং `next()` function call করে পরবর্তী middleware-এ control দেয়।

কল্পনা করো একটা airport। যাত্রী (request) প্রবেশ করে, প্রথমে ticket check (authentication middleware), তারপর security check (authorization middleware), তারপর baggage check (validation middleware), তারপর finally বিমানে ওঠে (route handler)। প্রতিটা checkpoint middleware। যেকোনো checkpoint যাত্রীকে ফেরত পাঠাতে পারে (response পাঠানো) অথবা পরবর্তী checkpoint-এ যেতে দিতে পারে (`next()` call)।

**Middleware-এর সিগনেচার:** `(req, res, next) => { ... }`

**`next()` function:**

`next()` call করলে Express পরবর্তী matching middleware বা route handler-এ যায়।
`next(error)` call করলে normal middleware chain skip করে error-handling middleware-এ যায়।
`next()` না call করে response না পাঠালে request hang করে — client indefinitely অপেক্ষা করে।

---

## Middleware-এর ধরন

**Application-level Middleware:** `app.use()` দিয়ে সব route-এ apply। যেমন: logging, JSON parsing, CORS।

**Router-level Middleware:** `router.use()` দিয়ে নির্দিষ্ট router-এ।

**Built-in Middleware:** Express-এর সাথে আসা — `express.json()` (request body JSON parse), `express.urlencoded()` (form data parse), `express.static()` (static file serve)।

**Third-party Middleware:** `morgan` (HTTP logging), `helmet` (security headers), `cors` (CORS handling), `compression` (response compression)।

**Error-handling Middleware:** চারটা parameter — `(err, req, res, next)`। Express এই 4-argument signature দেখলে বোঝে এটা error handler। Normal middleware chain-এ এটা চলে না, শুধু `next(error)` call হলে।

---

## Middleware Execution Order

Express-এ middleware execution order সম্পূর্ণভাবে code-এ লেখার order-এর উপর নির্ভরশীল। উপরে লেখা middleware আগে execute হয়।

এই কারণে কিছু নিয়ম:
- Logging middleware সবার আগে — সব request log করতে।
- Body parsing middleware (express.json) route-এর আগে — না হলে `req.body` থাকবে না।
- Authentication middleware protected route-এর আগে।
- Error handler সবার শেষে — তার আগে সব middleware error pass করে।

---

## Routing — Request-কে সঠিক Handler-এ পাঠানো

Express routing হলো URL pattern এবং HTTP method-এর combination দিয়ে নির্দিষ্ট handler function-এ request পাঠানো।

**Route Parameters:** URL-এর dynamic part। `/users/:id` — এখানে `:id` একটা route parameter, `req.params.id` দিয়ে access।

**Query Parameters:** URL-এর `?` পরে আসে। `/users?page=2&limit=10` — `req.query.page` এবং `req.query.limit`।

**Request Body:** POST, PUT, PATCH request-এর body। `express.json()` middleware parse করার পরে `req.body`।

**Router:** Express-এর `Router` class দিয়ে routes group করা যায়। `/users` সংক্রান্ত সব route একটা file-এ, `/products` সংক্রান্ত আরেক file-এ। এটা code organize করার best practice।

---

## Express Routing — অভ্যন্তরীণ কার্যপদ্ধতি

Express ভেতরে একটা middleware stack রাখে। `app.use()` বা `app.get()` call করলে সেই middleware বা route handler stack-এ push হয়।

Request আসলে Express stack-এর উপর থেকে নিচে প্রতিটা middleware check করে — এই request-এর URL এবং method কি এই middleware-এর pattern-এর সাথে match করে? Match করলে execute, `next()` পেলে পরবর্তীটা check। Match না করলে skip।

Route matching-এ Express path-to-regexp library ব্যবহার করে — `/users/:id` ধরনের pattern-কে regular expression-এ convert করে।

---

## MVC Pattern Express-এ

MVC (Model-View-Controller) হলো সফটওয়্যার architecture pattern যেটা concern আলাদা করে:

**Model:** Database এবং data logic। Prisma/Mongoose model, database query।

**View:** Presentation। API-তে এটা JSON response, template engine হলে HTML।

**Controller:** Request handle করে, Model-এর সাথে কথা বলে, View-কে data দেয়।

Express-এ MVC implement করা হয় folder structure দিয়ে — `routes/`, `controllers/`, `models/`, `services/`। Service layer অনেক সময় controller এবং model-এর মধ্যে রাখা হয় — business logic controller-এ না রেখে service-এ।

---

## Express vs Koa vs Fastify

**Koa:** Express-এর creators-এর পরের কাজ। async/await-কে first-class citizen করে। Context object (`ctx`) দিয়ে req এবং res এক জায়গায়। Middleware layer পরিষ্কার — কিন্তু ecosystem Express-এর চেয়ে ছোট।

**Fastify:** Performance-focused। Validation build-in (JSON schema)। Serialization optimize করা। Benchmark-এ Express-এর চেয়ে কয়েকগুণ দ্রুত। TypeScript support ভালো।

**Express:** বিশাল ecosystem, documentation, community। প্রায় সব tutorial Express-এ। Simplicity এবং familiarity। Performance critical না হলে এখনো সেরা choice।

---

## Error Handling — Best Practice

Production Express application-এ error handling একটা গুরুত্বপূর্ণ বিষয়। Route handler-এ error হলে `next(err)` call করতে হবে — `try/catch` সহ async function-এ।

Error-handling middleware-এ error type check করে appropriate status code এবং message পাঠানো উচিত। Client-এ stack trace পাঠানো উচিত নয় — security risk। Development-এ detailed error, production-এ generic message।

Async route handler-এ `try/catch` না থাকলে unhandled rejection হবে। `express-async-errors` package অথবা custom async wrapper দিয়ে automatic error forwarding করা যায়।

---

## মূল উপলব্ধি

Express-এর সব শক্তি middleware architecture-এ। একটা HTTP request কীভাবে middleware chain ভেদ করে route handler পর্যন্ত পৌঁছায় এবং response ফেরত আসে — এই flow বোঝলে authentication, validation, logging সব কিছু স্বাভাবিকভাবে implement করা যায়। Express-এর unopinionated nature সুবিধা এবং অসুবিধা উভয়ই — structure নিজে তৈরি করতে হয়, কিন্তু flexibility সর্বোচ্চ।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 3](./chapter-03-nodejs-core.md) | [➡ Ch 5](./chapter-05-postgresql.md)
