
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 3 — Node.js Core
# "V8 থেকে Event Loop — Engine-এর ভেতরে"
# ⏱ ~90 মিনিট · Progress: [████░░░░░░] 20%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Node.js কী এবং V8 Engine কীভাবে কাজ করে
- ✅ Event Loop — Non-blocking I/O এর রহস্য
- ✅ Global objects: `__dirname`, `__filename`, `process`, `global`
- ✅ Core modules: `fs`, `path`, `os`, `http`, `events`, `crypto`
- ✅ npm ও package.json সম্পূর্ণ গাইড
- ✅ dotenv দিয়ে Environment Variables ম্যানেজ
- ✅ `nodemon` দিয়ে auto-restart development

---

## 🏗️ Real-life Analogy

> ভাবো Node.js হলো একটি দক্ষ রেস্তোরাঁর একজনমাত্র waiter। সে একসাথে ১০ জন customer-এর order নিতে পারে। রান্না হতে দেরি হলে সে অপেক্ষা না করে অন্যদের serve করে। রান্না শেষ হলে notification পায় এবং তখন serve করে। এটাই Non-blocking I/O।

```
🟢 Flutter তুলনা:
   Flutter-এর Dart VM যেমন Dart code চালায়,
   Node.js-এর V8 Engine তেমনি JavaScript চালায়।
   Flutter-এর Isolate যেমন heavy work করে,
   Node.js-এর Worker Threads তেমনি করে।
```

---

## 🔧 Node.js Architecture

```mermaid
graph TD
    A["JavaScript Code\n(তোমার code)"] --> B["V8 Engine\n(Google Chrome-এর JS engine)"]
    B --> C["Node.js Bindings\n(C++ layer)"]
    C --> D["libuv\n(async I/O, Event Loop)"]
    D --> E["OS\n(File System, Network, Timer)"]

    B --> F["Call Stack\n(sync code)"]
    D --> G["Event Loop"]
    G --> H["Callback Queue\n(setTimeout, setInterval)"]
    G --> I["Microtask Queue\n(Promise, queueMicrotask)"]
```

---

## ⚙️ Event Loop — সবচেয়ে গুরুত্বপূর্ণ ধারণা

```
╭──────────────────────────────────────────────────────────╮
│ 🔑 Concept: Event Loop                                   │
│ সহজ ভাষায়: Node.js-এর "দারোয়ান" — সে ঠিক করে         │
│            কোন কাজ কখন চলবে। Single thread হওয়া        │
│            সত্ত্বেও হাজার request handle করতে পারে।     │
│ Flutter তুলনা: Flutter-এর UI thread যেমন frame          │
│            render করে, Event Loop তেমনি              │
│            JavaScript execute করে।                       │
╰──────────────────────────────────────────────────────────╯
```

```mermaid
stateDiagram-v2
    [*] --> CallStack : Code শুরু
    CallStack --> Executing : Function call
    Executing --> CallStack : Return
    Executing --> WebAPIs : Async operation (fs.read, setTimeout, fetch)
    WebAPIs --> CallbackQueue : Operation complete
    CallbackQueue --> CallStack : Stack empty হলে
    CallStack --> [*] : সব শেষ
```

### Event Loop Phases (libuv)

```
┌─────────────────────────────────────────────────────┐
│                    Event Loop                        │
│                                                      │
│  ┌──────────────┐                                   │
│  │   timers      │ ← setTimeout, setInterval        │
│  └──────┬───────┘                                   │
│         ▼                                            │
│  ┌──────────────┐                                   │
│  │ pending I/O  │ ← previous I/O callbacks          │
│  └──────┬───────┘                                   │
│         ▼                                            │
│  ┌──────────────┐                                   │
│  │   poll        │ ← I/O events (fs, network)       │
│  └──────┬───────┘                                   │
│         ▼                                            │
│  ┌──────────────┐                                   │
│  │   check       │ ← setImmediate                   │
│  └──────┬───────┘                                   │
│         ▼                                            │
│  ┌──────────────┐                                   │
│  │close callbacks│ ← socket.on('close')             │
│  └──────────────┘                                   │
│                                                      │
│  ⚡ Microtasks (Promise, queueMicrotask) — প্রতি    │
│     phase-এর পরে সব microtask শেষ হয়              │
└─────────────────────────────────────────────────────┘
```

📄 File: `examples/ch03/event-loop.js` · 🎯 উদ্দেশ্য: Event Loop execution order বোঝা

```javascript
console.log('1 — Start (synchronous)');

setTimeout(() => {
  console.log('5 — setTimeout callback (timer phase)');
}, 0);

setImmediate(() => {
  console.log('6 — setImmediate (check phase)');
});

Promise.resolve().then(() => {
  console.log('3 — Promise.then (microtask)');
});

queueMicrotask(() => {
  console.log('4 — queueMicrotask (microtask)');
});

console.log('2 — End (synchronous)');
```

💻 Output:
```
1 — Start (synchronous)
2 — End (synchronous)
3 — Promise.then (microtask)
4 — queueMicrotask (microtask)
5 — setTimeout callback (timer phase)
6 — setImmediate (check phase)
```

> ⚠️ **সতর্কতা:** Event Loop-এ blocking code লিখলে সব request আটকে যাবে! `while(true){}` বা CPU-heavy computation Event Loop block করে।

---

## 🌍 Global Objects

📄 File: `examples/ch03/globals.js` · 🎯 উদ্দেশ্য: Node.js global objects

```javascript
// __dirname — বর্তমান file-এর directory path
console.log(__dirname);
// /Users/dev/projects/hello-backend/src

// __filename — বর্তমান file-এর পুরো path
console.log(__filename);
// /Users/dev/projects/hello-backend/src/globals.js

// process — Node.js process সম্পর্কে তথ্য
console.log(process.version);     // v20.11.0
console.log(process.platform);    // darwin (macOS) / linux / win32
console.log(process.env.NODE_ENV); // development / production
console.log(process.pid);         // process ID
console.log(process.cwd());       // current working directory
console.log(process.memoryUsage()); // memory usage stats
console.log(process.uptime());    // কতক্ষণ চলছে (seconds)

// process arguments
// node script.js --port=3000 --env=production
console.log(process.argv);
// ['node', '/path/to/script.js', '--port=3000', '--env=production']

// process.exit — program শেষ করো
// process.exit(0);  // সফলভাবে শেষ
// process.exit(1);  // error সহ শেষ

// Environment variables
process.env.MY_SECRET = 'test_value';
console.log(process.env.MY_SECRET); // test_value

// global — browser-এর window-এর মতো
global.myGlobalVar = 'I am global';
console.log(myGlobalVar); // I am global (global prefix ছাড়াও কাজ করে)
// ⚠️ global variables ব্যবহার করা bad practice

// Buffer — binary data handle করতে
const buf = Buffer.from('Hello Backend', 'utf8');
console.log(buf);           // <Buffer 48 65 6c 6c 6f ...>
console.log(buf.toString()); // Hello Backend
console.log(buf.length);    // 13

// URL class (built-in)
const myUrl = new URL('https://api.myshop.com/api/v1/products?page=2&limit=10');
console.log(myUrl.hostname);                    // api.myshop.com
console.log(myUrl.pathname);                    // /api/v1/products
console.log(myUrl.searchParams.get('page'));    // 2
console.log(myUrl.searchParams.get('limit'));   // 10
```

---

## 📁 fs Module (File System)

📄 File: `examples/ch03/file-system.js` · 🎯 উদ্দেশ্য: File পড়া ও লেখা

```javascript
const fs = require('node:fs');
const fsPromises = require('node:fs/promises');
const path = require('node:path');

// ============================================
// Synchronous — ⚠️ Server-এ ব্যবহার করো না
// ============================================
const syncContent = fs.readFileSync(
  path.join(__dirname, 'data.txt'),
  'utf8'
);
console.log(syncContent);

// ============================================
// Callback-based (old style)
// ============================================
fs.readFile(path.join(__dirname, 'data.txt'), 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err.message);
    return;
  }
  console.log('File content:', data);
});

// ============================================
// Promise-based (modern, recommended)
// ============================================
async function readAndWriteFile() {
  try {
    // File পড়ো
    const content = await fsPromises.readFile(
      path.join(__dirname, 'products.json'),
      'utf8'
    );
    const products = JSON.parse(content);
    console.log(`Found ${products.length} products`);

    // নতুন product যোগ করো
    products.push({ id: products.length + 1, name: 'New Product' });

    // File-এ লিখো
    await fsPromises.writeFile(
      path.join(__dirname, 'products.json'),
      JSON.stringify(products, null, 2),
      'utf8'
    );
    console.log('File updated successfully');

    // Directory তৈরি করো
    await fsPromises.mkdir(path.join(__dirname, 'uploads'), { recursive: true });

    // Directory contents দেখো
    const files = await fsPromises.readdir(__dirname);
    console.log('Files:', files);

    // File আছে কিনা check করো
    try {
      await fsPromises.access(path.join(__dirname, 'config.json'));
      console.log('config.json exists');
    } catch {
      console.log('config.json does not exist');
    }

    // File delete করো
    // await fsPromises.unlink(path.join(__dirname, 'temp.txt'));

    // File stats
    const stats = await fsPromises.stat(path.join(__dirname, 'products.json'));
    console.log('File size:', stats.size, 'bytes');
    console.log('Last modified:', stats.mtime);
  } catch (error) {
    console.error('File operation failed:', error.message);
  }
}

readAndWriteFile();

// ============================================
// Stream — বড় file পড়তে
// ============================================
const readStream = fs.createReadStream(
  path.join(__dirname, 'large-file.txt'),
  { encoding: 'utf8', highWaterMark: 64 * 1024 } // 64KB chunks
);

readStream.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes`);
});

readStream.on('end', () => {
  console.log('File reading complete');
});

readStream.on('error', (err) => {
  console.error('Stream error:', err.message);
});
```

---

## 📂 path Module

📄 File: `examples/ch03/path-module.js` · 🎯 উদ্দেশ্য: File path manage করা

```javascript
const path = require('node:path');

// ============================================
// path.join — সঠিকভাবে path জোড়া দাও
// ============================================
const filePath = path.join(__dirname, 'uploads', 'images', 'product.jpg');
// macOS/Linux: /project/uploads/images/product.jpg
// Windows:    \project\uploads\images\product.jpg

// ============================================
// path.resolve — absolute path তৈরি করো
// ============================================
const absolutePath = path.resolve('src', 'index.js');
// /current/working/directory/src/index.js

// ============================================
// path methods
// ============================================
const fullPath = '/project/src/utils/helpers.js';

console.log(path.dirname(fullPath));   // /project/src/utils
console.log(path.basename(fullPath));  // helpers.js
console.log(path.extname(fullPath));   // .js
console.log(path.basename(fullPath, '.js')); // helpers (extension ছাড়া)

// Path parse করো
const parsed = path.parse(fullPath);
console.log(parsed);
/*
{
  root: '/',
  dir: '/project/src/utils',
  base: 'helpers.js',
  ext: '.js',
  name: 'helpers'
}
*/

// Path format করো
const formatted = path.format({
  dir: '/project/src/utils',
  name: 'helpers',
  ext: '.js',
});
console.log(formatted); // /project/src/utils/helpers.js

// OS separator
console.log(path.sep);     // / (macOS/Linux) বা \ (Windows)
console.log(path.delimiter); // : (macOS/Linux) বা ; (Windows)
```

---

## 💻 os Module

📄 File: `examples/ch03/os-module.js` · 🎯 উদ্দেশ্য: OS তথ্য পাওয়া

```javascript
const os = require('node:os');

console.log('Platform:', os.platform());         // linux, darwin, win32
console.log('Architecture:', os.arch());          // x64, arm64
console.log('OS Release:', os.release());         // kernel version
console.log('Hostname:', os.hostname());           // computer name
console.log('Total Memory:', (os.totalmem() / 1024 / 1024 / 1024).toFixed(2), 'GB');
console.log('Free Memory:', (os.freemem() / 1024 / 1024 / 1024).toFixed(2), 'GB');
console.log('CPUs:', os.cpus().length);            // CPU core count
console.log('Home Directory:', os.homedir());      // /Users/username
console.log('Temp Directory:', os.tmpdir());       // /tmp

// CPU info
const cpus = os.cpus();
console.log('CPU Model:', cpus[0].model);
console.log('CPU Speed:', cpus[0].speed, 'MHz');

// Network interfaces
const interfaces = os.networkInterfaces();
Object.entries(interfaces).forEach(([name, addrs]) => {
  addrs.forEach((addr) => {
    if (addr.family === 'IPv4' && !addr.internal) {
      console.log(`${name}: ${addr.address}`);
    }
  });
});
```

---

## 🔒 crypto Module

📄 File: `examples/ch03/crypto-module.js` · 🎯 উদ্দেশ্য: Hashing ও encryption

```javascript
const crypto = require('node:crypto');

// ============================================
// Hash তৈরি করো (password store করতে নয়! bcrypt ব্যবহার করো)
// ============================================
const hash = crypto.createHash('sha256').update('hello world').digest('hex');
console.log('SHA-256:', hash);
// b94d27b9934d3e08a52e52d7da7dabfac484efe04294e576e16f5f ...

// MD5 (file integrity check এর জন্য, security-critical নয়)
const md5 = crypto.createHash('md5').update('hello world').digest('hex');
console.log('MD5:', md5);

// ============================================
// Random Bytes — unique token তৈরি
// ============================================
// Sync
const token = crypto.randomBytes(32).toString('hex');
console.log('Token:', token); // 64 character hex string

// Async (preferred)
crypto.randomBytes(32, (err, buffer) => {
  if (err) throw err;
  console.log('Async Token:', buffer.toString('hex'));
});

// Promise-based
const { randomBytes } = require('node:crypto');

async function generateToken() {
  const bytes = await new Promise((resolve, reject) => {
    randomBytes(32, (err, buf) => {
      if (err) reject(err);
      else resolve(buf);
    });
  });
  return bytes.toString('hex');
}

// UUID-এর মতো random ID
const randomId = crypto.randomUUID();
console.log('UUID:', randomId); // e.g., 550e8400-e29b-41d4-a716-446655440000

// ============================================
// HMAC — secret key দিয়ে signature তৈরি
// ============================================
const secret = 'my-api-secret-key';
const message = 'user:1:action:purchase';
const hmac = crypto.createHmac('sha256', secret).update(message).digest('hex');
console.log('HMAC:', hmac);
```

---

## 🌐 http Module (Low-level)

📄 File: `examples/ch03/http-server.js` · 🎯 উদ্দেশ্য: Built-in HTTP server

```javascript
const http = require('node:http');
const url = require('node:url');

// Basic HTTP server (Express ছাড়া)
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;
  const query = parsedUrl.query;

  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Content-Type', 'application/json');

  if (req.method === 'GET' && pathname === '/health') {
    res.writeHead(200);
    res.end(JSON.stringify({ status: 'ok', uptime: process.uptime() }));
    return;
  }

  if (req.method === 'GET' && pathname === '/products') {
    const page = parseInt(query.page || '1', 10);
    const limit = parseInt(query.limit || '10', 10);

    res.writeHead(200);
    res.end(JSON.stringify({
      page,
      limit,
      products: ['iPhone', 'iPad', 'MacBook'].slice(0, limit),
    }));
    return;
  }

  // POST — body পড়তে হয়
  if (req.method === 'POST' && pathname === '/products') {
    let body = '';

    req.on('data', (chunk) => {
      body += chunk.toString();
    });

    req.on('end', () => {
      try {
        const data = JSON.parse(body);
        res.writeHead(201);
        res.end(JSON.stringify({
          success: true,
          message: 'Product created',
          data: { id: Date.now(), ...data },
        }));
      } catch {
        res.writeHead(400);
        res.end(JSON.stringify({ success: false, message: 'Invalid JSON' }));
      }
    });
    return;
  }

  // 404
  res.writeHead(404);
  res.end(JSON.stringify({ success: false, message: 'Route not found' }));
});

server.listen(3000, () => {
  console.log('✅ HTTP Server running on port 3000');
});

// Server gracefully shutdown করো
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Server closed gracefully');
    process.exit(0);
  });
});
```

> 💡 **PRO TIP:** Real project-এ সরাসরি `http` module ব্যবহার করো না। Express বা NestJS ব্যবহার করো। এটা শুধু বোঝার জন্য।

---

## 📦 npm ও package.json সম্পূর্ণ গাইড

### package.json সব fields

📄 File: `package.json` · 🎯 উদ্দেশ্য: Project configuration

```json
{
  "name": "ecommerce-backend",
  "version": "1.0.0",
  "description": "E-commerce backend API",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "build": "tsc",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/"
  },
  "keywords": ["nodejs", "express", "ecommerce"],
  "author": "Your Name <your@email.com>",
  "license": "MIT",
  "engines": {
    "node": ">=20.0.0",
    "npm": ">=10.0.0"
  },
  "dependencies": {
    "express": "^4.18.2",
    "prisma": "^5.9.1",
    "@prisma/client": "^5.9.1",
    "mongoose": "^8.1.1",
    "bcryptjs": "^2.4.3",
    "jsonwebtoken": "^9.0.2",
    "dotenv": "^16.4.1",
    "cors": "^2.8.5",
    "helmet": "^7.1.0",
    "express-rate-limit": "^7.1.5",
    "express-validator": "^7.0.1",
    "multer": "^1.4.5-lts.1",
    "nodemailer": "^6.9.9",
    "winston": "^3.11.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.3",
    "jest": "^29.7.0",
    "supertest": "^6.3.4",
    "eslint": "^8.57.0",
    "prettier": "^3.2.4"
  }
}
```

### npm Commands Cheatsheet

```bash
# Project initialize করো
npm init -y

# Package install করো
npm install express                    # production dependency
npm install --save-dev nodemon         # dev dependency only
npm install -g @nestjs/cli             # global install

# Package remove করো
npm uninstall express

# সব dependencies install করো (fresh clone)
npm install

# Production-only install করো
npm install --omit=dev

# Packages update করো
npm update
npm update express

# Outdated packages দেখো
npm outdated

# Package info দেখো
npm info express

# Security audit করো
npm audit
npm audit fix

# Cache clear করো
npm cache clean --force

# Global packages list দেখো
npm list -g --depth=0

# Script run করো
npm run dev
npm run build
npm test
```

---

## 🔐 dotenv — Environment Variables

```
╭──────────────────────────────────────────────────────────╮
│ 🔑 Concept: Environment Variables                        │
│ সহজ ভাষায়: Code-এর বাইরে রাখা configuration —         │
│            প্রতিটি environment-এ আলাদা value            │
│ Flutter তুলনা: flutter_dotenv package যেভাবে           │
│            .env থেকে config পড়ে, Node-এও তেমনি         │
╰──────────────────────────────────────────────────────────╯
```

📄 File: `.env` · 🎯 উদ্দেশ্য: Sensitive configuration

```bash
# Server Configuration
NODE_ENV=development
PORT=3000
API_VERSION=v1

# PostgreSQL Database
DATABASE_URL="postgresql://postgres:yourpassword@localhost:5432/ecommerce_db"
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=yourpassword

# MongoDB
MONGODB_URI=mongodb://localhost:27017/ecommerce_db

# JWT
JWT_SECRET=your-super-secret-jwt-key-minimum-32-characters-long
JWT_EXPIRES_IN=15m
JWT_REFRESH_SECRET=your-refresh-token-secret-minimum-32-chars
JWT_REFRESH_EXPIRES_IN=7d

# Cloudinary
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@gmail.com
SMTP_PASS=your-app-password

# Redis
REDIS_URL=redis://localhost:6379

# Frontend
FRONTEND_URL=http://localhost:4200
```

📄 File: `src/config/env.js` · 🎯 উদ্দেশ্য: Centralized, validated configuration

```javascript
const dotenv = require('dotenv');

// .env file load করো (সবার আগে করতে হবে)
dotenv.config();

// সব environment variables এক জায়গায় validate করো
const requiredEnvVars = [
  'DATABASE_URL',
  'JWT_SECRET',
  'JWT_REFRESH_SECRET',
];

const missingVars = requiredEnvVars.filter((key) => !process.env[key]);
if (missingVars.length > 0) {
  throw new Error(`Missing required environment variables: ${missingVars.join(', ')}`);
}

const config = {
  node: {
    env: process.env.NODE_ENV || 'development',
    port: parseInt(process.env.PORT || '3000', 10),
    isDevelopment: process.env.NODE_ENV === 'development',
    isProduction: process.env.NODE_ENV === 'production',
    isTest: process.env.NODE_ENV === 'test',
  },
  database: {
    url: process.env.DATABASE_URL,
    mongoUri: process.env.MONGODB_URI || 'mongodb://localhost:27017/ecommerce_db',
  },
  jwt: {
    secret: process.env.JWT_SECRET,
    expiresIn: process.env.JWT_EXPIRES_IN || '15m',
    refreshSecret: process.env.JWT_REFRESH_SECRET,
    refreshExpiresIn: process.env.JWT_REFRESH_EXPIRES_IN || '7d',
  },
  cloudinary: {
    cloudName: process.env.CLOUDINARY_CLOUD_NAME,
    apiKey: process.env.CLOUDINARY_API_KEY,
    apiSecret: process.env.CLOUDINARY_API_SECRET,
  },
  email: {
    host: process.env.SMTP_HOST || 'smtp.gmail.com',
    port: parseInt(process.env.SMTP_PORT || '587', 10),
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS,
  },
  frontend: {
    url: process.env.FRONTEND_URL || 'http://localhost:4200',
  },
};

module.exports = config;
```

📄 File: `src/index.js` · 🎯 উদ্দেশ্য: Config সবার আগে load করো

```javascript
// সবার প্রথমে!
const config = require('./config/env');

const express = require('express');

const app = express();
app.use(express.json());

app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    environment: config.node.env,
    port: config.node.port,
  });
});

app.listen(config.node.port, () => {
  console.log(`✅ Server running in ${config.node.env} mode on port ${config.node.port}`);
});
```

---

## 🔄 nodemon — Auto-restart

```bash
# Install করো
npm install --save-dev nodemon

# package.json-এ script যোগ করো:
# "dev": "nodemon src/index.js"

# চালাও
npm run dev

# Custom config (nodemon.json)
```

📄 File: `nodemon.json` · 🎯 উদ্দেশ্য: nodemon configuration

```json
{
  "watch": ["src"],
  "ext": "js,json",
  "ignore": ["src/**/*.test.js", "node_modules"],
  "delay": "200",
  "env": {
    "NODE_ENV": "development"
  }
}
```

---

## 🏋️ Exercise

**কাজ: File-based Product Store**

📄 File: `exercises/ch03/file-store.js` · 🎯 উদ্দেশ্য: fs module দিয়ে CRUD

```javascript
const fsPromises = require('node:fs/promises');
const path = require('node:path');
const crypto = require('node:crypto');

const DB_FILE = path.join(__dirname, 'products.json');

// Initialize empty database
async function initDb() {
  try {
    await fsPromises.access(DB_FILE);
  } catch {
    await fsPromises.writeFile(DB_FILE, JSON.stringify([], null, 2));
  }
}

async function readDb() {
  const content = await fsPromises.readFile(DB_FILE, 'utf8');
  return JSON.parse(content);
}

async function writeDb(data) {
  await fsPromises.writeFile(DB_FILE, JSON.stringify(data, null, 2));
}

// CRUD Operations
async function createProduct(productData) {
  const products = await readDb();
  const product = {
    id: crypto.randomUUID(),
    ...productData,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
  products.push(product);
  await writeDb(products);
  return product;
}

async function getAllProducts() {
  return readDb();
}

async function getProductById(id) {
  const products = await readDb();
  return products.find((p) => p.id === id) || null;
}

async function updateProduct(id, updates) {
  const products = await readDb();
  const index = products.findIndex((p) => p.id === id);
  if (index === -1) return null;

  products[index] = {
    ...products[index],
    ...updates,
    updatedAt: new Date().toISOString(),
  };
  await writeDb(products);
  return products[index];
}

async function deleteProduct(id) {
  const products = await readDb();
  const index = products.findIndex((p) => p.id === id);
  if (index === -1) return false;

  products.splice(index, 1);
  await writeDb(products);
  return true;
}

// Test করো
async function main() {
  await initDb();

  const p1 = await createProduct({ name: 'iPhone 15', price: 999, category: 'phone' });
  console.log('Created:', p1.id);

  const p2 = await createProduct({ name: 'MacBook', price: 1999, category: 'laptop' });

  const all = await getAllProducts();
  console.log('All products:', all.length);

  const found = await getProductById(p1.id);
  console.log('Found:', found.name);

  const updated = await updateProduct(p1.id, { price: 899 });
  console.log('Updated price:', updated.price);

  const deleted = await deleteProduct(p2.id);
  console.log('Deleted:', deleted);

  const remaining = await getAllProducts();
  console.log('Remaining:', remaining.length);
}

main().catch(console.error);
```

---

## 📊 Common Mistakes Table

| ভুল | কারণ | সমাধান |
|-----|------|---------|
| Event Loop block করা | CPU-heavy sync code | Worker Threads বা async code ব্যবহার |
| `.env` file commit করা | .gitignore নেই | .gitignore-এ `.env` যোগ করো |
| process.exit() বেপরোয়া | Resource cleanup নেই | SIGTERM handle করো gracefully |
| fs.readFileSync() server-এ | Event Loop block হয় | fs/promises ব্যবহার করো |
| Config validation না করা | Runtime error | Startup-এ required vars check করো |

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 3 — তুমি শিখলে                          ║
╠══════════════════════════════════════════════════════╣
║  • V8 Engine ও Node.js Architecture                  ║
║  • Event Loop phases ও execution order              ║
║  • Global objects: __dirname, process, Buffer       ║
║  • fs/promises: async file read/write/delete        ║
║  • path module: cross-platform path handling        ║
║  • os module: system information                    ║
║  • crypto: hashing, random bytes, UUID, HMAC        ║
║  • http: low-level server (concept only)            ║
║  • npm: install/update/audit commands               ║
║  • dotenv + centralized config validation           ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 2](./chapter-02-javascript-backend.md) | [➡ Chapter 4](./chapter-04-expressjs.md)
