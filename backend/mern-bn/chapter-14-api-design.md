# 📘 CHAPTER 14 — API Design
### "Richardson Maturity Model থেকে OpenAPI পর্যন্ত — ভালো API-র শিল্পকলা"
#### Progress: [███████████████░░░░] 75%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 13](./chapter-13-file-upload-email.md) | [➡ Ch 15](./chapter-15-testing.md)

---

## API Design কেন গুরুত্বপূর্ণ?

API হলো contract — আপনার service এবং তার consumer-এর মধ্যে চুক্তি। একবার published হলে পরিবর্তন করা কঠিন — consumer আপনার API-এর উপর নির্ভর করে কাজ করে।

ভালো API design মানে:
- Developer-friendly — সহজে বোঝা এবং ব্যবহার করা।
- Consistent — সব endpoint একই pattern follow করে।
- Evolvable — ভবিষ্যতে পরিবর্তন করা সম্ভব।
- Secure — নিরাপদ।

---

## Richardson Maturity Model

Leonard Richardson REST API-কে চারটা maturity level-এ বিভক্ত করেছেন।

**Level 0 — The Swamp of POX:**

HTTP শুধু transport। সব request একটা endpoint-এ, সব operation একটাই HTTP method (POST)। XML-RPC, SOAP এই level-এ। `POST /api` এবং body-তে `{ "action": "getUser", "id": 1 }`।

**Level 1 — Resources:**

আলাদা resource-এর জন্য আলাদা URL। কিন্তু HTTP method এখনো সব POST। `POST /users`, `POST /products`।

**Level 2 — HTTP Verbs:**

HTTP method সঠিকভাবে ব্যবহার। GET for read, POST for create, PUT/PATCH for update, DELETE for delete। Status code সঠিক — 200, 201, 404, 400। বেশিরভাগ "REST API" এই level।

**Level 3 — Hypermedia Controls (HATEOAS):**

Response-এ next possible action-এর link থাকে। Client API documentation না দেখেও navigate করতে পারে।

---

## URL Design Philosophy

URL হলো resource-এর address। ভালো URL:

**Noun, verb নয়:** `/users` — resource। `/getUsers` নয়।

**Plural nouns:** `/users` একটা collection। `/users/123` নির্দিষ্ট user।

**Hierarchy:** `/users/123/orders` — user 123-এর orders। কিন্তু খুব deep করা উচিত নয় — `/users/123/orders/456/items/789` too deeply nested।

**Lowercase, hyphen-separated:** `/blog-posts` — camelCase নয়।

**Version prefix:** `/api/v1/users`।

---

## Versioning Strategies

API পরিবর্তন করতে হবে কিন্তু existing consumer break করা যাবে না — versioning এই সমস্যার সমাধান।

**URL Versioning:** `/api/v1/users`, `/api/v2/users`।
- সুবিধা: Explicit, durable link, cache-friendly, সহজ।
- অসুবিধা: URL "unclean" — REST purist বলবেন resource-এ version থাকা উচিত নয়।

**Header Versioning:** `Accept: application/vnd.myapi.v2+json` বা `API-Version: 2`।
- সুবিধা: URL clean।
- অসুবিধা: Browser-এ test কঠিন, caching জটিল।

**Query Parameter:** `/api/users?version=2`।
- সুবিধা: Simple।
- অসুবিধা: Accidental omission।

Real world-এ URL versioning সবচেয়ে popular — pragmatic choice।

---

## Pagination Strategies

লাখ লাখ record একবারে return করা যাবে না। Pagination দরকার।

**Offset-based Pagination:**

`GET /users?page=2&limit=20` অথবা `?offset=20&limit=20`।

Database-এ: `LIMIT 20 OFFSET 20`।

সুবিধা: Simple, যেকোনো page-এ jump সম্ভব।

অসুবিধা: Inconsistency — page 2 দেখার পর নতুন item insert হলে page 3-এ গেলে duplicate আসতে পারে বা item miss হতে পারে। Database-এ large offset expensive — `OFFSET 100000` মানে 100,000 row skip করতে হবে।

**Cursor-based Pagination:**

Cursor হলো last item-এর identifier (typically ID বা timestamp)। `GET /users?cursor=last_seen_id&limit=20`।

Database-এ: `WHERE id > last_seen_id LIMIT 20`।

সুবিধা: Consistent — new insert/delete cursor-এর accuracy নষ্ট করে না। Database efficient — index দিয়ে সরাসরি।

অসুবিধা: Random page access করা যায় না — only "next page"।

**কখন কোনটা:**

Admin dashboard — offset (random page access দরকার)।
Infinite scroll, social feed — cursor।

---

## HATEOAS

Hypermedia as the Engine of Application State — REST Level 3।

Response-এ শুধু data নয়, related action-এর link-ও থাকে।

```json
{
  "id": 123,
  "name": "Alice",
  "_links": {
    "self": { "href": "/users/123" },
    "orders": { "href": "/users/123/orders" },
    "delete": { "href": "/users/123", "method": "DELETE" }
  }
}
```

Client API structure না জেনেও navigate করতে পারে — self-documenting। Real world-এ পুরোপুরি HATEOAS implement করা হয় না — complex এবং consumer-এ extra parsing।

---

## OpenAPI/Swagger

OpenAPI (সাবেক Swagger) হলো REST API description-এর standard format। YAML বা JSON-এ API contract define করা।

**সুবিধা:**
- Auto-generated documentation (Swagger UI)।
- Client SDK generation (TypeScript, Python, Java)।
- API testing tool।
- Team communication — frontend developer backend-এর API আগেই জানে।

**NestJS:** `@nestjs/swagger` package দিয়ে decorator থেকে Swagger doc auto-generate।

**API-first Development:** Code-এর আগে API contract define করা। Frontend এবং backend parallel কাজ করতে পারে।

---

## Consumer-Driven Contracts

Microservice-এ multiple service একে অপরের API ব্যবহার করে। কোনো service API পরিবর্তন করলে dependent service break করতে পারে।

Consumer-driven contract testing: প্রতিটা consumer বলে তার কাছ থেকে কী expect করে। Provider সেই contract অনুযায়ী test করে। Pact এই pattern implement করে।

---

## মূল উপলব্ধি

ভালো API design সময় নেয় কিন্তু long-term maintenance সহজ করে। URL design, versioning, pagination — প্রতিটার trade-off বুঝে সঠিক choice করতে হবে। OpenAPI দিয়ে documentation API-এর সাথে sync থাকে। API একবার published হলে backward compatibility রক্ষা করা professional দায়িত্ব।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 13](./chapter-13-file-upload-email.md) | [➡ Ch 15](./chapter-15-testing.md)
