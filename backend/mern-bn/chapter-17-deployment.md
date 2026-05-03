# 📘 CHAPTER 17 — Deployment
### "12-Factor App থেকে Zero-Downtime — Production-এ যাওয়ার পথ"
#### Progress: [██████████████████░] 90%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 16](./chapter-16-performance.md) | [➡ Ch 18](./chapter-18-full-project.md)

---

## Process Manager — কেন দরকার?

Node.js application `node app.js` দিয়ে চালালে:
- Process crash করলে — application বন্ধ।
- Server restart হলে — application বন্ধ।
- Multiple CPU core ব্যবহার হয় না।
- Logs manage হয় না।

**PM2** (Process Manager 2) এই সমস্যাগুলো সমাধান করে।

**PM2-এর কাজ:**

**Auto-restart:** Application crash করলে automatically restart।

**Cluster Mode:** Node.js cluster module ব্যবহার করে সব CPU core-এ process চালানো। `pm2 start app.js -i max` — max হলো CPU count।

**Log Management:** stdout এবং stderr file-এ। `pm2 logs` দিয়ে দেখা।

**Startup Script:** `pm2 startup` — server restart-এ automatically PM2 শুরু।

**Monitoring:** `pm2 monit` — CPU, memory, request count real-time।

---

## 12-Factor App Methodology

Heroku-এর engineers 12-Factor App methodology তৈরি করেছেন — modern, scalable, maintainable application-এর 12টা principle।

**1. Codebase:** একটা codebase, অনেক deploy। Git-এ সব।

**2. Dependencies:** সব dependency explicit — `package.json`-এ। System-level package ধরে নেওয়া যাবে না।

**3. Config:** Configuration environment variable-এ। Code-এ hardcode নয়। Development, staging, production-এ আলাদা `.env`।

**4. Backing Services:** Database, Redis, email — treat as attached resource। URL পরিবর্তন করে swap করা যাবে।

**5. Build, Release, Run:** Build (code compile) → Release (config inject) → Run। আলাদা stage।

**6. Processes:** Stateless processes। Application state shared memory-তে নয় — Redis, database-এ।

**7. Port Binding:** App নিজে port-এ listen — web server (Apache/Nginx) dependency নেই।

**8. Concurrency:** Process model দিয়ে scale।

**9. Disposability:** Fast startup, graceful shutdown। Horizontal scaling সহজ।

**10. Dev/Prod Parity:** Development এবং production যতটা সম্ভব similar। "Works on my machine" problem কমে।

**11. Logs:** Event stream হিসেবে treat করো। App log file-এ না লিখে stdout-এ। Aggregation আলাদা সিস্টেমের কাজ।

**12. Admin Processes:** One-off admin task (database migration) — same codebase, same environment।

---

## CI/CD Philosophy

**CI (Continuous Integration):**

Developer code push করলে automatically:
- Tests run।
- Linting check।
- Build করা।

Code দ্রুত integrate হয় — long-lived branch এড়ানো যায়। Bug early detect।

**CD (Continuous Delivery):**

CI pass করলে automatically staging-এ deploy। Production deployment manual trigger।

**CD (Continuous Deployment):**

Tests pass করলে automatically production-এও deploy। High confidence test suite দরকার।

**Pipeline:**

Push → Build → Test → Staging Deploy → Manual Approve → Production Deploy।

---

## Blue-Green Deployment

Zero-downtime deployment-এর একটা strategy।

**Blue environment:** Current production।

**Green environment:** New version deploy।

Green ready হলে load balancer traffic blue থেকে green-এ switch। Instant। Bug হলে load balancer আবার blue-এ — instant rollback।

কিন্তু: দুটো environment চালানো expensive। Database migration সমস্যা — blue এবং green একই database ব্যবহার করলে migration backward compatible হতে হবে।

---

## Environment Promotion

**Dev → Staging → Production।**

**Development:** Local। Developer নিজের machine।

**Staging:** Production-এর mirror। Real data-এর মতো (sanitized) test। Final QA এখানে। External stakeholder demo।

**Production:** Real users।

প্রতিটা environment আলাদা database, আলাদা config। Code staging-এ tested হয়ে তারপর production-এ।

---

## Structured Logging

Application log হলো application-এর "কথা" — কী ঘটছে।

**Plain Text Log:**

```
2024-01-15 10:30:45 - User logged in: alice@example.com
```

Parse করা কঠিন। Filter করা কঠিন।

**Structured Log (JSON):**

```json
{
  "timestamp": "2024-01-15T10:30:45Z",
  "level": "info",
  "message": "User logged in",
  "userId": 123,
  "requestId": "abc-123"
}
```

Machine-readable। Filter, search, aggregate সহজ। Datadog, Elasticsearch-এ পাঠানো সহজ।

**Log Levels:**

`error` — Fix দরকার। Alert।
`warn` — Attention দরকার। Monitor।
`info` — Normal operations। Audit।
`debug` — Verbose। Development-এ।

Production-এ debug log disable — too noisy এবং sensitive data।

---

## Health Checks

Load balancer এবং orchestration system (Kubernetes) জানতে চায় application healthy কিনা।

**Liveness Check:** Application জীবিত কিনা। `GET /health` — 200 OK মানে alive। Fail করলে restart।

**Readiness Check:** Application request serve করতে ready কিনা। Database connection আছে কিনা, migrations run হয়েছে কিনা। Fail করলে traffic পাঠানো বন্ধ — কিন্তু restart নয়।

**Deep Health Check:** Database, Redis, external API সব dependency check করা।

---

## Zero-Downtime Deployment

Rolling Update: নতুন version একটা একটা করে instance deploy। সব instances একসাথে নামে না। কিছুটা সময় পুরনো এবং নতুন version একসাথে চলে — API backward compatible হতে হবে।

**Graceful Shutdown:**

SIGTERM signal পেলে (Kubernetes বা PM2 থেকে):
1. নতুন request accept বন্ধ।
2. Current request process শেষ (timeout-এর মধ্যে)।
3. Database connection close।
4. Process exit।

এটা না করলে in-flight request fail করবে।

---

## মূল উপলব্ধি

Deployment শুধু `git push` নয় — এটা একটা disciplined process। 12-Factor App principles শিখলে cloud-native application তৈরি হয়। CI/CD automation করলে deployment ভয়হীন হয়। Structured log এবং health check ছাড়া production debugging অন্ধকারে হাতড়ানো।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 16](./chapter-16-performance.md) | [➡ Ch 18](./chapter-18-full-project.md)
