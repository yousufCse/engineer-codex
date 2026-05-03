# 📘 CHAPTER 18 — Full Project ও System Design
### "সব কিছু একসাথে — Production-Ready Architecture"
#### Progress: [███████████████████] 100%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 17](./chapter-17-deployment.md)

---

## System Design Thinking

System Design হলো high-level architecture-এর decision — কোন component থাকবে, কীভাবে communicate করবে, কোথায় কোন technology ব্যবহার হবে।

একটা system design করতে গেলে প্রশ্নগুলো:

**Functional Requirements:** System কী করবে? User story কী? Core features কী?

**Non-Functional Requirements:** কতজন concurrent user? Latency কত acceptable? Availability কত চাই (99.9%? 99.99%)? Data কতটা consistent হতে হবে?

Requirements জানার আগে architecture design করা যায় না।

---

## Technology Selection

Technology choice-এ কোনো "best" নেই — context-dependent।

**PostgreSQL বেছে নেওয়ার কারণ:**
- Complex relationships।
- ACID transaction critical।
- Financial, medical data।
- Schema well-defined।

**MongoDB বেছে নেওয়ার কারণ:**
- Flexible/evolving schema।
- Document-like data natural।
- High write throughput।

**Redis-এর কারণ:**
- Session store।
- Cache।
- Real-time leaderboard।
- Job queue।

**Express বেছে নেওয়ার কারণ:**
- Simple API, prototype।
- Team familiar।
- Flexibility চাই।

**NestJS-এর কারণ:**
- Large team।
- Enterprise application।
- TypeScript mandatory।
- Modular structure দরকার।

---

## Separation of Concerns

Good architecture concerns আলাদা রাখে। প্রতিটা layer এক ধরনের responsibility।

**Layered Architecture:**

**Route/Controller Layer:** HTTP request/response handle। Business logic নেই।

**Service Layer:** Business logic। Database call সরাসরি করে না।

**Repository/Data Layer:** Database interaction। Business logic নেই।

**Domain Layer:** Business rules, entities। কোনো framework dependency নেই।

এই separation-এর সুবিধা:
- Database পরিবর্তন করলে শুধু Data Layer বদলায়।
- Service test করতে real database লাগে না।
- Business logic HTTP framework থেকে independent।

---

## Monolith vs Microservice

**Monolith:**

সব code একটা application-এ। Simple। Team small হলে faster development। Single deployment। Database shared।

সমস্যা বড় হলে:
- Deploy করলে সব এক সাথে deploy হয়।
- Scaling — সব feature-কে একসাথে scale করতে হয়।
- Technology choice locked in।
- Team autonomy কম।

**Microservice:**

প্রতিটা feature/domain আলাদা service। Independent deploy। Independent scale। Technology choice প্রতি service-এ।

সমস্যা:
- Distributed system complexity।
- Network latency।
- Data consistency across services।
- Operational overhead।

**সিদ্ধান্ত:**

Startup, small team — Monolith দিয়ে শুরু করো। "Modular Monolith" — একটাই deploy কিন্তু internally module-এ বিভক্ত। Scale এবং team বড় হলে microservice-এ migrate।

---

## API Gateway

Microservice-এ প্রতিটা service-এর আলাদা URL। Client কোনটায় কল করবে? API Gateway single entry point।

**API Gateway কী করে:**
- Request routing — কোন service-এ পাঠাবে।
- Authentication — সব service-এ আলাদা auth না করে gateway-তে।
- Rate limiting।
- Request/Response transformation।
- Load balancing।
- SSL termination।

Kong, AWS API Gateway, Nginx — popular choices।

---

## Database per Service

Microservice-এ প্রতিটা service-এর নিজস্ব database — shared database নয়।

**কেন:**
- Service independent deploy এবং scale হতে পারে।
- Database schema change অন্য service-কে affect করে না।
- Service নিজের data-এর owner।

**সমস্যা:**

Transaction একাধিক service span করলে — ACID transaction আর কাজ করে না। Saga pattern দিয়ে distributed transaction।

Join query — আলাদা database থেকে data combine করা application level-এ করতে হয় অথবা Event Sourcing/CQRS।

---

## Event-Driven Communication

Microservice-এর মধ্যে দুটো communication pattern:

**Synchronous (HTTP/gRPC):** Service A, Service B-কে call করে, B-এর response-এর জন্য অপেক্ষা করে। Simple। কিন্তু B down হলে A-ও fail।

**Asynchronous (Message Queue):** Service A event publish করে (Kafka, RabbitMQ), Service B সুবিধামতো consume করে। Decoupled। B down থাকলেও message queue-এ থাকে, পরে process হয়।

Use case:
- Payment processed → Send email (async)।
- Order created → Notify inventory service (async)।
- User registered → Welcome email (async)।

---

## Production Readiness Checklist

Application production-এ নেওয়ার আগে:

**Security:**
- HTTPS — সব communication encrypted।
- Helmet headers।
- Rate limiting।
- Input validation।
- SQL Injection / XSS protection।
- Secrets environment variable-এ।

**Reliability:**
- Health check endpoint।
- Graceful shutdown।
- Retry logic for transient failures।
- Circuit breaker।

**Observability:**
- Structured logging।
- Error tracking (Sentry)।
- Metrics (CPU, memory, request rate, error rate)।
- Distributed tracing (microservice-এ)।

**Performance:**
- Database index।
- N+1 query নেই।
- Connection pooling।
- Cache strategy।

**Operations:**
- CI/CD pipeline।
- Automated tests।
- Database backup strategy।
- Rollback plan।
- On-call documentation।

---

## Real-World Project Architecture — Example

একটা e-commerce API-র architecture চিন্তা করা যাক:

**Services:**
- Auth Service: Registration, login, JWT।
- Product Service: Product catalog, search।
- Order Service: Order management, payment।
- Notification Service: Email, SMS।

**Data:**
- Auth DB: PostgreSQL (user credentials)।
- Product DB: PostgreSQL (structured product data)।
- Order DB: PostgreSQL (ACID transaction critical)।
- Search: Elasticsearch (full-text search)।
- Cache: Redis (product catalog, session)।
- Queue: RabbitMQ (async notification)।

**Infrastructure:**
- API Gateway: Nginx।
- Container: Docker।
- Orchestration: Kubernetes।
- CDN: Cloudflare।
- Image Storage: Cloudinary।

এই architecture complex — startup-এ single Express + PostgreSQL + Redis দিয়ে শুরু করাই সঠিক।

---

## মূল উপলব্ধি

এই বইয়ের যাত্রা শুরু হয়েছিল HTTP protocol থেকে — এখন পৌঁছেছি distributed system পর্যন্ত। Backend engineering মানে শুধু API লেখা নয় — এটা data modeling, security, performance, reliability, operability এই সব বিষয়ে সচেতন সিদ্ধান্ত নেওয়া। প্রতিটা technology একটা tool — tool চেনো, problem চেনো, তারপর সিদ্ধান্ত নাও। Complexity-র প্রতি সম্মান রাখো — সহজ সমাধান দিয়ে শুরু করো, প্রয়োজনে জটিল করো।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 17](./chapter-17-deployment.md)
