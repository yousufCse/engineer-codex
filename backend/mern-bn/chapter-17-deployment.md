
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📘 CHAPTER 17 — Deployment
# "PM2 + Railway + GitHub Actions — Production Live"
# ⏱ ~90 মিনিট · Progress: [████████████████░] 88%
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc)

---

## 📌 এই Chapter এ তুমি শিখবে

- ✅ Winston logger setup
- ✅ PM2 process manager
- ✅ Health check endpoint
- ✅ Railway deployment
- ✅ Render deployment
- ✅ GitHub Actions CI/CD pipeline
- ✅ Environment variables management

---

## 🏗️ Real-life Analogy

> Deployment = রেস্টুরেন্ট open করা। Development = রান্না practice। PM2 = manager যে দোকান বন্ধ হতে দেয় না। Railway/Render = building rent।

---

## 📋 Winston Logger

```bash
npm install winston winston-daily-rotate-file
```

📄 File: `src/utils/logger.js` · 🎯 উদ্দেশ্য: Structured logging

```javascript
const winston = require('winston');
const DailyRotateFile = require('winston-daily-rotate-file');
const path = require('path');

const logFormat = winston.format.combine(
  winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
  winston.format.errors({ stack: true }),
  winston.format.json()
);

const consoleFormat = winston.format.combine(
  winston.format.colorize(),
  winston.format.timestamp({ format: 'HH:mm:ss' }),
  winston.format.printf(({ timestamp, level, message, ...meta }) => {
    const metaStr = Object.keys(meta).length ? JSON.stringify(meta, null, 2) : '';
    return `${timestamp} [${level}] ${message} ${metaStr}`;
  })
);

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: logFormat,
  transports: [
    // Console (development)
    ...(process.env.NODE_ENV !== 'production'
      ? [new winston.transports.Console({ format: consoleFormat })]
      : []
    ),
    // Error file
    new DailyRotateFile({
      filename: path.join('logs', 'error-%DATE%.log'),
      datePattern: 'YYYY-MM-DD',
      level: 'error',
      maxSize: '20m',
      maxFiles: '14d',
      zippedArchive: true,
    }),
    // Combined file
    new DailyRotateFile({
      filename: path.join('logs', 'combined-%DATE%.log'),
      datePattern: 'YYYY-MM-DD',
      maxSize: '20m',
      maxFiles: '30d',
      zippedArchive: true,
    }),
  ],
  exceptionHandlers: [
    new DailyRotateFile({
      filename: path.join('logs', 'exceptions-%DATE%.log'),
      datePattern: 'YYYY-MM-DD',
    }),
  ],
  rejectionHandlers: [
    new DailyRotateFile({
      filename: path.join('logs', 'rejections-%DATE%.log'),
      datePattern: 'YYYY-MM-DD',
    }),
  ],
});

// HTTP request logger (Morgan replacement)
const httpLogger = (req, res, next) => {
  const start = Date.now();

  res.on('finish', () => {
    const duration = Date.now() - start;
    const logData = {
      method: req.method,
      url: req.originalUrl,
      status: res.statusCode,
      duration: `${duration}ms`,
      ip: req.ip,
      userAgent: req.get('User-Agent'),
    };

    if (req.user) logData.userId = req.user.id;

    if (res.statusCode >= 500) {
      logger.error('HTTP Request', logData);
    } else if (res.statusCode >= 400) {
      logger.warn('HTTP Request', logData);
    } else {
      logger.info('HTTP Request', logData);
    }
  });

  next();
};

module.exports = { logger, httpLogger };
```

---

## 🏥 Health Check Endpoint

📄 File: `src/routes/health.routes.js` · 🎯 উদ্দেশ্য: Health check

```javascript
const router = require('express').Router();
const prisma = require('../config/prisma');
const mongoose = require('mongoose');
const redis = require('../config/redis.config');
const { logger } = require('../utils/logger');

router.get('/', async (req, res) => {
  const checks = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: `${Math.floor(process.uptime())}s`,
    environment: process.env.NODE_ENV,
    version: process.env.npm_package_version,
    services: {},
  };

  // PostgreSQL check
  try {
    await prisma.$queryRaw`SELECT 1`;
    checks.services.postgresql = { status: 'ok' };
  } catch (e) {
    checks.services.postgresql = { status: 'error', message: e.message };
    checks.status = 'degraded';
  }

  // MongoDB check
  try {
    checks.services.mongodb = {
      status: mongoose.connection.readyState === 1 ? 'ok' : 'error',
      state: mongoose.STATES[mongoose.connection.readyState],
    };
    if (mongoose.connection.readyState !== 1) checks.status = 'degraded';
  } catch (e) {
    checks.services.mongodb = { status: 'error', message: e.message };
    checks.status = 'degraded';
  }

  // Redis check
  try {
    await redis.ping();
    checks.services.redis = { status: 'ok' };
  } catch (e) {
    checks.services.redis = { status: 'error', message: e.message };
    // Redis down হলেও degraded (not down)
    if (checks.status === 'ok') checks.status = 'degraded';
  }

  // Memory usage
  const mem = process.memoryUsage();
  checks.memory = {
    heapUsed: `${Math.round(mem.heapUsed / 1024 / 1024)}MB`,
    heapTotal: `${Math.round(mem.heapTotal / 1024 / 1024)}MB`,
    rss: `${Math.round(mem.rss / 1024 / 1024)}MB`,
  };

  const httpStatus = checks.status === 'ok' ? 200 : checks.status === 'degraded' ? 207 : 503;
  res.status(httpStatus).json(checks);
});

// Simple liveness probe (Kubernetes/Railway)
router.get('/live', (req, res) => {
  res.status(200).json({ status: 'alive' });
});

// Readiness probe
router.get('/ready', async (req, res) => {
  try {
    await prisma.$queryRaw`SELECT 1`;
    res.status(200).json({ status: 'ready' });
  } catch {
    res.status(503).json({ status: 'not ready' });
  }
});

module.exports = router;
```

---

## ⚙️ PM2 Process Manager

```bash
npm install pm2 -g
```

📄 File: `ecosystem.config.js` · 🎯 উদ্দেশ্য: PM2 configuration

```javascript
module.exports = {
  apps: [
    {
      name: 'myshop-api',
      script: './src/index.js',
      instances: 'max',        // CPU count অনুযায়ী instances
      exec_mode: 'cluster',    // Cluster mode
      watch: false,
      max_memory_restart: '512M',
      env: {
        NODE_ENV: 'development',
        PORT: 3000,
      },
      env_production: {
        NODE_ENV: 'production',
        PORT: 3000,
      },
      error_file: './logs/pm2-error.log',
      out_file: './logs/pm2-out.log',
      merge_logs: true,
      log_date_format: 'YYYY-MM-DD HH:mm:ss',
      // Graceful restart
      kill_timeout: 5000,
      wait_ready: true,
      listen_timeout: 10000,
      // Auto restart on crash
      autorestart: true,
      max_restarts: 10,
      restart_delay: 4000,
    },
  ],
};
```

```bash
# PM2 commands
pm2 start ecosystem.config.js --env production
pm2 status
pm2 logs myshop-api
pm2 restart myshop-api
pm2 stop myshop-api
pm2 delete myshop-api
pm2 save                     # Startup-এ auto start
pm2 startup                  # System startup config generate
```

---

## 🚂 Railway Deployment

```bash
# Railway CLI install
npm install -g @railway/cli

# Login
railway login

# New project
railway init

# Link existing project
railway link
```

📄 File: `railway.toml` · 🎯 উদ্দেশ্য: Railway config

```toml
[build]
builder = "NIXPACKS"
buildCommand = "npm install && npx prisma generate"

[deploy]
startCommand = "npm start"
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 3

[[services]]
name = "api"

[services.variables]
PORT = "3000"
```

📄 File: `package.json` (production start)

```json
{
  "scripts": {
    "start": "node src/index.js",
    "start:prod": "NODE_ENV=production node src/index.js",
    "dev": "nodemon src/index.js",
    "postinstall": "npx prisma generate"
  }
}
```

Railway-তে Environment Variables set করো:
```
DATABASE_URL=postgresql://...
MONGODB_URI=mongodb+srv://...
JWT_ACCESS_SECRET=...
JWT_REFRESH_SECRET=...
CLOUDINARY_CLOUD_NAME=...
```

---

## 🎨 Render Deployment

📄 File: `render.yaml` · 🎯 উদ্দেশ্য: Render.com config

```yaml
services:
  - type: web
    name: myshop-api
    env: node
    region: oregon
    plan: starter
    buildCommand: npm install && npx prisma generate
    startCommand: npm start
    healthCheckPath: /health
    envVars:
      - key: NODE_ENV
        value: production
      - key: DATABASE_URL
        fromDatabase:
          name: myshop-db
          property: connectionString
      - key: JWT_ACCESS_SECRET
        generateValue: true
      - key: JWT_REFRESH_SECRET
        generateValue: true

databases:
  - name: myshop-db
    databaseName: myshop
    user: myshop_user
    plan: starter
```

---

## 🔄 GitHub Actions CI/CD

📄 File: `.github/workflows/deploy.yml` · 🎯 উদ্দেশ্য: Auto deploy on push

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # ============================================
  # CI — Test
  # ============================================
  test:
    name: Run Tests
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: ecommerce_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      mongodb:
        image: mongo:7
        ports:
          - 27017:27017

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Generate Prisma client
        run: npx prisma generate

      - name: Run migrations
        run: npx prisma migrate deploy
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/ecommerce_test

      - name: Run tests
        run: npm test
        env:
          NODE_ENV: test
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/ecommerce_test
          MONGODB_URI: mongodb://localhost:27017/ecommerce_test
          JWT_ACCESS_SECRET: test_access_secret_minimum_32_chars_long
          JWT_REFRESH_SECRET: test_refresh_secret_minimum_32_chars_long

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        if: github.ref == 'refs/heads/main'
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  # ============================================
  # CD — Deploy (main branch only)
  # ============================================
  deploy:
    name: Deploy to Railway
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install Railway CLI
        run: npm install -g @railway/cli

      - name: Deploy to Railway
        run: railway up --service myshop-api
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}

      - name: Notify deployment
        if: success()
        run: echo "Deployed successfully to Railway!"
```

---

## 🔒 Environment Variables (.env template)

📄 File: `.env.example` · 🎯 উদ্দেশ্য: Template for setup

```dotenv
# App
NODE_ENV=development
PORT=3000
API_VERSION=v1
FRONTEND_URL=http://localhost:3001

# PostgreSQL
DATABASE_URL=postgresql://postgres:password@localhost:5432/ecommerce_dev

# MongoDB
MONGODB_URI=mongodb://localhost:27017/ecommerce_dev

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# JWT
JWT_ACCESS_SECRET=your_very_long_random_access_secret_here_min_32_chars
JWT_REFRESH_SECRET=your_very_long_random_refresh_secret_here_min_32_chars
JWT_ACCESS_EXPIRES_IN=15m
JWT_REFRESH_EXPIRES_IN=7d

# Cloudinary
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# Email (Gmail)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your@gmail.com
EMAIL_PASS=your_app_password

# Logging
LOG_LEVEL=info
```

---

## 📊 Deployment Checklist

```
✅ Production checklist:
  □ NODE_ENV=production set
  □ All secrets in environment variables (not code)
  □ .env ফাইল .gitignore-এ আছে
  □ HTTPS enabled (hosting provider করে)
  □ Database connection pooling set
  □ Redis connection error handling
  □ PM2 cluster mode OR hosting auto-scale
  □ Health check endpoint working
  □ Logs rotation configured
  □ Error monitoring (Sentry optional)
  □ Database backups configured
  □ Rate limiting enabled
  □ CORS configured for production domain
```

---

## ✅ Chapter Summary

```
╔══════════════════════════════════════════════════════╗
║  ✅ Chapter 17 — তুমি শিখলে                         ║
╠══════════════════════════════════════════════════════╣
║  • Winston structured logging                       ║
║  • Health check: /health, /health/live, /ready      ║
║  • PM2: cluster mode, ecosystem.config.js           ║
║  • Railway deployment: railway.toml                 ║
║  • Render deployment: render.yaml                   ║
║  • GitHub Actions: test + deploy pipeline           ║
║  • Environment variables management                 ║
║  • Production deployment checklist                  ║
╚══════════════════════════════════════════════════════╝
```

[⬆ TOC এ ফিরে যাও](./table-of-contents.md#toc) | [⬅ Chapter 16](./chapter-16-performance.md) | [➡ Chapter 18](./chapter-18-full-project.md)
