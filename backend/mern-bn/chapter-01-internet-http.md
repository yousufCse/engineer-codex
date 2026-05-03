
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 1 — Internet & HTTP
# "ডেটা কীভাবে যাতায়াত করে — পর্দার আড়ালের গল্প"
# ⏱ ~60 মিনিট · Progress: [██░░░░░░░░] 10%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Client-Server architecture কী ও কীভাবে কাজ করে
- ✅ HTTP কী — Request ও Response এর structure
- ✅ HTTP Methods: GET, POST, PUT, PATCH, DELETE
- ✅ HTTP Status Codes: 2xx, 3xx, 4xx, 5xx
- ✅ HTTP Headers কী ও কেন দরকার
- ✅ REST API এর ৬টি নীতি
- ✅ JSON format ও parsing
- ✅ HTTPS কীভাবে SSL/TLS দিয়ে data সুরক্ষিত রাখে

---

## 🏗️ Real-life Analogy

> তুমি রেস্তোরাঁয় গিয়ে waiter-কে order দাও। Waiter রান্নাঘরে যায়, রান্না হয়, Waiter ফিরে আসে খাবার নিয়ে।
>
> - **তুমি** = Client (Browser / Flutter App)
> - **Waiter** = HTTP Protocol
> - **রান্নাঘর** = Server (Node.js / NestJS)
> - **Menu** = API Endpoints
> - **Order slip** = HTTP Request
> - **খাবার** = HTTP Response

```
🟢 Flutter তুলনা:
   Flutter-এ তুমি http.get('https://api.example.com/users') লিখলে
   Flutter হলো Client, api.example.com হলো Server।
   HTTP হলো মাঝের পরিবহন ব্যবস্থা।
```

---

## 📡 Client-Server Architecture

```mermaid
sequenceDiagram
    participant C as 📱 Flutter App (Client)
    participant N as 🌐 Internet
    participant S as 🖥️ Node.js Server
    participant D as 🗄️ Database

    C->>N: HTTP Request: GET /api/products
    N->>S: Request forward
    S->>D: SELECT * FROM products
    D-->>S: [product data]
    S-->>N: HTTP Response: 200 OK + JSON
    N-->>C: Response arrives
    C->>C: Display products in UI
```

### Layer Architecture

```
┌────────────────────────────────────────────────┐
│              APPLICATION LAYER                  │
│  Flutter App  ←→  Browser  ←→  Postman         │
├────────────────────────────────────────────────┤
│              TRANSPORT LAYER                    │
│         HTTP / HTTPS (Port 80 / 443)           │
├────────────────────────────────────────────────┤
│              NETWORK LAYER                      │
│              IP Address + DNS                   │
├────────────────────────────────────────────────┤
│              PHYSICAL LAYER                     │
│         WiFi / Ethernet / Mobile Data           │
└────────────────────────────────────────────────┘
```

---

## 🌍 URL এর গঠন

```
https://api.myshop.com:443/api/v1/products?category=phone&page=2#results
│       │               │   │              │                    │
│       │               │   │              │                    └─ Fragment (anchor)
│       │               │   │              └─ Query Parameters
│       │               │   └─ Path (Endpoint)
│       │               └─ Port
│       └─ Domain (Host)
└─ Protocol (Scheme)
```

```
╭─────────────────────────────────────────────────╮
│ 🔑 Concept: URL (Uniform Resource Locator)      │
│ সহজ ভাষায়: ইন্টারনেটে কোনো resource-এর        │
│            ঠিকানা, যেমন বাসার ঠিকানা            │
│ Flutter তুলনা: Route-এ যেমন '/home', '/profile' │
│            URI pattern থাকে, API-তে তেমনি       │
│            '/api/products', '/api/users'         │
╰─────────────────────────────────────────────────╯
```

---

## 📨 HTTP Request এর Structure

```
POST /api/products HTTP/1.1
Host: api.myshop.com
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
Accept: application/json
Content-Length: 89

{
  "name": "iPhone 15 Pro",
  "price": 999.99,
  "category": "phone"
}
```

**Request-এর ৪টি অংশ:**

```
┌────────────────────────────────────────────────┐
│  1. Request Line: POST /api/products HTTP/1.1  │
│     (Method + Path + HTTP Version)             │
├────────────────────────────────────────────────┤
│  2. Headers:                                   │
│     Host: api.myshop.com                       │
│     Content-Type: application/json             │
│     Authorization: Bearer <token>              │
├────────────────────────────────────────────────┤
│  3. Blank Line (হেডার ও বডির মাঝে)            │
├────────────────────────────────────────────────┤
│  4. Body (শুধু POST/PUT/PATCH-এ থাকে):        │
│     { "name": "iPhone 15 Pro", ... }           │
└────────────────────────────────────────────────┘
```

## 📬 HTTP Response এর Structure

```
HTTP/1.1 201 Created
Content-Type: application/json
X-Request-Id: abc123def456
Date: Mon, 03 May 2026 10:00:00 GMT

{
  "success": true,
  "message": "Product created successfully",
  "data": {
    "id": 1,
    "name": "iPhone 15 Pro",
    "price": 999.99
  }
}
```

---

## 🔵 HTTP Methods (Verbs)

```mermaid
graph TD
    A[HTTP Methods] --> B[GET]
    A --> C[POST]
    A --> D[PUT]
    A --> E[PATCH]
    A --> F[DELETE]
    A --> G[HEAD]
    A --> H[OPTIONS]

    B --> B1["Data পড়া\n(Read)"]
    C --> C1["নতুন Data তৈরি\n(Create)"]
    D --> D1["পুরো Data replace\n(Update All)"]
    E --> E1["আংশিক Update\n(Update Part)"]
    F --> F1["Data মুছে ফেলা\n(Delete)"]
```

### E-Commerce উদাহরণ

| Method | Endpoint | কাজ | Body দরকার? |
|--------|----------|-----|------------|
| `GET` | `/api/products` | সব product দেখো | ❌ না |
| `GET` | `/api/products/1` | Product #1 দেখো | ❌ না |
| `POST` | `/api/products` | নতুন product তৈরি করো | ✅ হ্যাঁ |
| `PUT` | `/api/products/1` | Product #1 সম্পূর্ণ আপডেট | ✅ হ্যাঁ |
| `PATCH` | `/api/products/1` | Product #1 দাম শুধু পরিবর্তন | ✅ হ্যাঁ |
| `DELETE` | `/api/products/1` | Product #1 মুছে ফেলো | ❌ না |

### PUT vs PATCH পার্থক্য

```
❌ ভুল ধারণা: PUT ও PATCH একই
✅ সঠিক ধারণা:

PUT (সম্পূর্ণ replace):
Request body:
{
  "name": "iPhone 15 Pro Max",  ← পরিবর্তন
  "price": 1199.99,             ← পরিবর্তন
  "category": "phone",          ← MUST include করতে হবে
  "stock": 50                   ← MUST include করতে হবে
}
→ পুরানো object টি নতুন দিয়ে replace হয়

PATCH (আংশিক update):
Request body:
{
  "price": 1199.99              ← শুধু দাম পরিবর্তন
}
→ শুধু দাম আপডেট হয়, বাকি সব অপরিবর্তিত থাকে
```

---

## 🔢 HTTP Status Codes

```mermaid
graph LR
    A[Status Codes] --> B["2xx — সফল"]
    A --> C["3xx — Redirect"]
    A --> D["4xx — Client Error"]
    A --> E["5xx — Server Error"]
```

### 2xx — সফলতার কোড

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| `200` | OK | সফলভাবে data পাওয়া গেছে (GET) |
| `201` | Created | নতুন resource তৈরি হয়েছে (POST) |
| `204` | No Content | সফল কিন্তু কোনো response body নেই (DELETE) |

### 4xx — Client-এর ভুল

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| `400` | Bad Request | Request এর data ভুল/incomplete |
| `401` | Unauthorized | Login করা নেই |
| `403` | Forbidden | Login আছে কিন্তু permission নেই |
| `404` | Not Found | Resource পাওয়া যায়নি |
| `409` | Conflict | Duplicate data (যেমন: email already exists) |
| `422` | Unprocessable Entity | Validation ব্যর্থ হয়েছে |
| `429` | Too Many Requests | Rate limit অতিক্রম |

### 5xx — Server-এর ভুল

| Code | Name | কখন ব্যবহার |
|------|------|------------|
| `500` | Internal Server Error | Server-এ অপ্রত্যাশিত error |
| `502` | Bad Gateway | Upstream server সাড়া দেয়নি |
| `503` | Service Unavailable | Server সাময়িক বন্ধ |

> 🔴 **এই ভুল করবে না:** সব কিছুতে `200 OK` return করো না। `POST` সফল হলে `201 Created`, delete হলে `204 No Content` return করো।

---

## 📋 HTTP Headers

```
╭─────────────────────────────────────────────────╮
│ 🔑 Concept: HTTP Headers                        │
│ সহজ ভাষায়: Request/Response-এর extra           │
│            information — চিঠির envelope-এর      │
│            উপর লেখা তথ্যের মতো                  │
│ Flutter তুলনা: http package-এ headers: {}       │
│            parameter যেভাবে pass করো            │
╰─────────────────────────────────────────────────╯
```

### গুরুত্বপূর্ণ Request Headers

| Header | উদ্দেশ্য | উদাহরণ |
|--------|---------|---------|
| `Content-Type` | Body-র data format | `application/json` |
| `Authorization` | Authentication token | `Bearer eyJhb...` |
| `Accept` | কোন format-এ response চাই | `application/json` |
| `Accept-Language` | কোন ভাষায় response চাই | `bn-BD, en-US` |
| `User-Agent` | কোন app/browser request করছে | `FlutterApp/1.0` |

### গুরুত্বপূর্ণ Response Headers

| Header | উদ্দেশ্য | উদাহরণ |
|--------|---------|---------|
| `Content-Type` | Response data format | `application/json; charset=utf-8` |
| `Content-Length` | Response এর byte size | `348` |
| `Cache-Control` | Browser cache নির্দেশনা | `no-cache, no-store` |
| `Set-Cookie` | Browser-এ cookie সেট করো | `session=abc; HttpOnly` |
| `X-Request-Id` | Request tracking ID | `req_abc123` |

---

## 🌐 REST API এর ৬টি নীতি

```mermaid
mindmap
  root((REST))
    Uniform Interface
      Resource-based URLs
      HTTP Methods
      Standard Responses
    Stateless
      প্রতি request স্বাধীন
      Server session রাখে না
    Client-Server
      UI ও Logic আলাদা
    Cacheable
      Response cache করা যায়
    Layered System
      Proxy, CDN layer থাকতে পারে
    Code on Demand
      Optional JS code
```

### RESTful URL Design Rules

```
❌ ভুল পদ্ধতি (Non-RESTful):
GET  /getProducts
POST /createNewProduct
GET  /deleteProduct?id=1
POST /updateProductPrice

✅ সঠিক পদ্ধতি (RESTful):
GET    /api/products          ← সব products
POST   /api/products          ← নতুন product তৈরি
GET    /api/products/:id      ← একটি product
PUT    /api/products/:id      ← পুরো product আপডেট
PATCH  /api/products/:id      ← আংশিক আপডেট
DELETE /api/products/:id      ← product মুছো

GET    /api/products/:id/reviews     ← product-এর reviews
POST   /api/products/:id/reviews     ← নতুন review যোগ করো
```

**নামকরণের নিয়ম:**
- URL-এ সবসময় **noun** ব্যবহার করো, **verb** নয়
- **Plural** ব্যবহার করো: `/products`, `/users`, `/orders`
- lowercase ও hyphen ব্যবহার করো: `/product-categories`
- Version prefix দাও: `/api/v1/products`

---

## 📄 JSON (JavaScript Object Notation)

```
╭─────────────────────────────────────────────────╮
│ 🔑 Concept: JSON                                │
│ সহজ ভাষায়: Data exchange-এর universal          │
│            ভাষা — সব platform বোঝে              │
│ Flutter তুলনা: Flutter-এ jsonDecode() দিয়ে     │
│            API response parse করো, সেই          │
│            JSON-ই Backend return করে            │
╰─────────────────────────────────────────────────╯
```

### JSON এর সব Data Types

📄 File: `examples/json-types.json` · 🎯 উদ্দেশ্য: JSON-এর সব ধরনের data দেখানো

```json
{
  "string": "iPhone 15 Pro",
  "number_integer": 999,
  "number_float": 999.99,
  "boolean_true": true,
  "boolean_false": false,
  "null_value": null,
  "array": ["phone", "tablet", "laptop"],
  "nested_object": {
    "brand": "Apple",
    "model": "15 Pro",
    "specs": {
      "ram": "8GB",
      "storage": "256GB"
    }
  },
  "array_of_objects": [
    { "id": 1, "color": "Black Titanium" },
    { "id": 2, "color": "White Titanium" }
  ]
}
```

### Node.js-এ JSON Parse ও Stringify

📄 File: `examples/json-demo.js` · 🎯 উদ্দেশ্য: JSON নিয়ে কাজ করার পদ্ধতি

```javascript
// JSON String → JavaScript Object
const jsonString = '{"name":"iPhone 15","price":999.99}';
const product = JSON.parse(jsonString);
console.log(product.name);   // iPhone 15
console.log(product.price);  // 999.99

// JavaScript Object → JSON String
const order = {
  id: 1,
  product: 'iPhone 15 Pro',
  quantity: 2,
  total: 1999.98,
  createdAt: new Date(),
};
const jsonOutput = JSON.stringify(order, null, 2);
console.log(jsonOutput);
```

💻 Output:
```json
{
  "id": 1,
  "product": "iPhone 15 Pro",
  "quantity": 2,
  "total": 1999.98,
  "createdAt": "2026-05-03T10:00:00.000Z"
}
```

---

## 🔒 HTTPS ও SSL/TLS

```mermaid
sequenceDiagram
    participant C as 📱 Client
    participant S as 🖥️ Server

    Note over C,S: TLS Handshake শুরু

    C->>S: ClientHello (supported TLS versions, ciphers)
    S->>C: ServerHello + SSL Certificate (Public Key)
    C->>C: Certificate verify করো (CA দিয়ে)
    C->>S: Pre-master Secret (Server-এর Public Key দিয়ে encrypt করা)
    S->>S: Private Key দিয়ে decrypt করো
    Note over C,S: উভয়ের কাছে এখন Session Key আছে

    C->>S: 🔐 Encrypted HTTP Request
    S->>C: 🔐 Encrypted HTTP Response
```

```
╭─────────────────────────────────────────────────╮
│ 🔑 Concept: HTTPS                               │
│ সহজ ভাষায়: HTTP + TLS Encryption =             │
│            ডেটা পাঠানোর নিরাপদ tunnel           │
│ Flutter তুলনা: App-এ https:// URL ব্যবহার       │
│            করলেই Flutter automatically          │
│            TLS verify করে।                      │
╰─────────────────────────────────────────────────╯
```

**HTTP vs HTTPS পার্থক্য:**

| বিষয় | HTTP | HTTPS |
|-------|------|-------|
| Port | 80 | 443 |
| Encryption | ❌ নেই | ✅ TLS |
| Data চুরি হতে পারে? | হ্যাঁ | না |
| Certificate লাগে? | না | হ্যাঁ (SSL cert) |
| Production-এ ব্যবহার | ❌ কখনো না | ✅ সবসময় |

---

## 🔍 HTTP Request in Practice (Node.js)

📄 File: `examples/http-client-demo.js` · 🎯 উদ্দেশ্য: Node.js থেকে HTTP request করা

```javascript
// Node.js 18+ built-in fetch API (node: prefix প্রয়োজন নেই)
async function fetchProducts() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts/1');

    // Status code check করো
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status} ${response.statusText}`);
    }

    // Headers দেখো
    console.log('Content-Type:', response.headers.get('content-type'));
    console.log('Status:', response.status);

    // Body parse করো
    const data = await response.json();
    console.log('Data:', data);

    return data;
  } catch (error) {
    console.error('Request failed:', error.message);
    throw error;
  }
}

fetchProducts();
```

💻 Output:
```
Content-Type: application/json; charset=utf-8
Status: 200
Data: {
  userId: 1,
  id: 1,
  title: 'sunt aut facere repellat provident occaecati ...',
  body: 'quia et suscipit\nsuscipit recusandae consequuntur...'
}
```

---

## 🏋️ Exercise: HTTP-কে বাস্তবে দেখো

**কাজ ১: Browser DevTools দিয়ে HTTP দেখো**
1. Chrome/Firefox খোলো
2. `F12` চেপে DevTools খোলো
3. `Network` tab-এ যাও
4. `https://jsonplaceholder.typicode.com/posts` এ যাও
5. Request headers, response headers, status code পর্যবেক্ষণ করো

**কাজ ২: নিজে API বানাও**

📄 File: `exercises/chapter-01/server.js` · 🎯 উদ্দেশ্য: HTTP methods অনুশীলন

```javascript
const express = require('express');
const app = express();
app.use(express.json());

// in-memory "database" (এখনো real DB নেই)
let products = [
  { id: 1, name: 'iPhone 15 Pro', price: 999.99, category: 'phone' },
  { id: 2, name: 'iPad Air', price: 599.99, category: 'tablet' },
];

// GET সব products
app.get('/api/products', (req, res) => {
  res.status(200).json({
    success: true,
    count: products.length,
    data: products,
  });
});

// GET একটি product
app.get('/api/products/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const product = products.find((p) => p.id === id);

  if (!product) {
    return res.status(404).json({
      success: false,
      message: `Product with id ${id} not found`,
    });
  }

  res.status(200).json({ success: true, data: product });
});

// POST নতুন product
app.post('/api/products', (req, res) => {
  const { name, price, category } = req.body;

  if (!name || !price || !category) {
    return res.status(400).json({
      success: false,
      message: 'name, price, category are required',
    });
  }

  const newProduct = {
    id: products.length + 1,
    name,
    price,
    category,
  };

  products.push(newProduct);

  res.status(201).json({
    success: true,
    message: 'Product created successfully',
    data: newProduct,
  });
});

// PATCH product আপডেট
app.patch('/api/products/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const index = products.findIndex((p) => p.id === id);

  if (index === -1) {
    return res.status(404).json({
      success: false,
      message: `Product with id ${id} not found`,
    });
  }

  // শুধু পাঠানো fields আপডেট করো
  products[index] = { ...products[index], ...req.body };

  res.status(200).json({
    success: true,
    message: 'Product updated successfully',
    data: products[index],
  });
});

// DELETE product
app.delete('/api/products/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const index = products.findIndex((p) => p.id === id);

  if (index === -1) {
    return res.status(404).json({
      success: false,
      message: `Product with id ${id} not found`,
    });
  }

  products.splice(index, 1);

  res.status(204).send(); // No Content
});

app.listen(3000, () => console.log('✅ Server on http://localhost:3000'));
```

**Postman দিয়ে test করো:**
```
GET    http://localhost:3000/api/products
GET    http://localhost:3000/api/products/1
POST   http://localhost:3000/api/products   body: {"name":"MacBook","price":1299,"category":"laptop"}
PATCH  http://localhost:3000/api/products/1 body: {"price":899.99}
DELETE http://localhost:3000/api/products/2
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| GET request-এ body পাঠানো | GET semantically stateless | Query parameters ব্যবহার করো |
| সব response-এ `200` return | Status code শেখেনি | Table অনুযায়ী সঠিক code ব্যবহার করো |
| `/getUser` endpoint নাম | REST নীতি না জানা | Noun ব্যবহার করো: `/users/:id` |
| HTTP URL production-এ | Security জ্ঞান নেই | HTTPS certificate ব্যবহার করো |
| Error response-এ `200` | Bad practice | Error হলে `4xx` বা `5xx` পাঠাও |

---

## ✅ Key Concepts Summary

| Concept | সংক্ষিপ্ত বিবরণ |
|---------|----------------|
| Client-Server | Client request করে, Server response দেয় |
| HTTP | Application layer protocol |
| URL | Internet resource-এর ঠিকানা |
| HTTP Method | Resource-এ কী করতে চাই তা বলে |
| Status Code | Server কী ঘটেছে তা জানায় |
| Headers | Request/Response এর metadata |
| REST | API design-এর আর্কিটেকচারাল নীতি |
| JSON | Data exchange format |
| HTTPS | HTTP + TLS encryption |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════╗
║  ✅ Chapter 1 — তুমি শিখলে                      ║
╠══════════════════════════════════════════════════╣
║  • Client-Server architecture বুঝলে             ║
║  • HTTP Request ও Response-এর structure         ║
║  • ৫টি HTTP method ও তাদের সঠিক ব্যবহার         ║
║  • Status codes 200/201/204/400/401/404/500      ║
║  • RESTful URL design নীতি                      ║
║  • JSON parse ও stringify                       ║
║  • HTTPS ও TLS encryption-এর ধারণা              ║
║  • Complete CRUD API নিজে বানালে               ║
╚══════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 0](./chapter-00-environment-setup.md) | [➡ Chapter 2](./chapter-02-javascript-backend.md)
