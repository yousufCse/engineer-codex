
# PART 10: সিস্টেম ডিজাইন ও আর্কিটেকচার
## System Design — Tech Lead ও Architect-এর দৃষ্টিভঙ্গি

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩৪: Scalable System Design — লক্ষ ব্যবহারকারীর জন্য ডিজাইন

## ৩৪.১ Scaling এর পর্যায়ক্রম

```
ব্যবহারকারীর সংখ্যা অনুযায়ী architecture পরিবর্তন:

Stage 1: 0 → 1,000 users
┌─────────────────────────────────────┐
│  [Flutter App] → [Single Server]   │
│                     │               │
│              [Single Database]      │
│                                     │
│  একটা VPS-ই যথেষ্ট                 │
└─────────────────────────────────────┘

Stage 2: 1,000 → 10,000 users
┌─────────────────────────────────────────────┐
│  [Flutter App] → [Load Balancer]           │
│                    ├─ [App Server 1]        │
│                    └─ [App Server 2]        │
│                          │                  │
│                   [Database + Replica]      │
│                   Read → Replica            │
│                   Write → Primary           │
└─────────────────────────────────────────────┘

Stage 3: 10,000 → 100,000 users
┌──────────────────────────────────────────────────────┐
│  [Flutter] → [CDN] → [API Gateway] → [LB]           │
│                                        ├─ [App 1]   │
│                                        ├─ [App 2]   │
│                                        └─ [App N]   │
│                                              │        │
│                               [Cache: Redis] │        │
│                                              │        │
│                        [DB Primary] + [DB Replicas]  │
│                                                      │
│             [Message Queue: Kafka/RabbitMQ]          │
│                    ├─ [Worker 1]                     │
│                    └─ [Worker 2]                     │
└──────────────────────────────────────────────────────┘

Stage 4: 100,000 → 1,000,000+ users
┌──────────────────────────────────────────────────────────┐
│  Microservices Architecture                             │
│  Multi-region deployment                                │
│  Database Sharding                                      │
│  Service Mesh (Istio)                                   │
│  Distributed Caching                                    │
│  Event-driven Architecture                              │
└──────────────────────────────────────────────────────────┘
```

## ৩৪.২ Horizontal vs Vertical Scaling

```
Vertical Scaling (Scale Up):
একটি সার্ভার আরও শক্তিশালী করা।

[2 CPU, 4GB RAM] → [8 CPU, 32GB RAM]

সীমাবদ্ধতা:
- Hardware limit আছে
- Single point of failure
- Downtime লাগে upgrade-এ
- ব্যয়বহুল

Horizontal Scaling (Scale Out):
আরও সার্ভার যোগ করা।

[Server 1]
[Server 2]  ← নতুন যোগ করা হলো
[Server 3]  ← নতুন যোগ করা হলো

সুবিধা:
- তাত্ত্বিকভাবে অসীম scaling
- High Availability
- কোনো downtime নেই
- Commodity hardware

অসুবিধা:
- Stateless app design দরকার
- Complexity বাড়ে
- Data consistency challenge

সিদ্ধান্ত:
Database → Vertical (কিছু সীমা পর্যন্ত, তারপর Sharding)
Application → Horizontal (Cloud-native approach)
```

## ৩৪.৩ Database Scaling

```
Read Replica:
                   ┌──────────────────────────┐
                   │   Primary DB (Write)     │
                   │   10.0.0.10              │
                   └─────────┬────────────────┘
              Replication ───┤
         ┌──────────┬───────┘
         ▼          ▼
 ┌──────────┐ ┌──────────┐
 │ Replica1 │ │ Replica2 │
 │(Read)    │ │(Read)    │
 └──────────┘ └──────────┘

Write → Primary
Read → Replicas (load distributed)
৮০% traffic usually reads!

Database Sharding (Horizontal Partition):
                   [Router/Coordinator]
                   /         |          \
          ┌───────┐    ┌───────┐    ┌───────┐
          │ Shard │    │ Shard │    │ Shard │
          │  1    │    │  2    │    │  3    │
          │User   │    │User   │    │User   │
          │ID 1-  │    │ID 334-│    │ID 667-│
          │333    │    │666    │    │1000   │
          └───────┘    └───────┘    └───────┘

Sharding Key নির্বাচন গুরুত্বপূর্ণ!
ভুল key → Hot Spot (একটি shard সব চাপ পায়)
```

## ৩৪.৪ Caching Strategy

```
Cache Layers:

[Flutter App]
    │
    ├── Client Cache (Memory: 10MB, Disk: 100MB)
    │   CachedNetworkImage, dio_cache_interceptor
    │
    ▼
[CDN Edge]
    │
    ├── CDN Cache (Static assets, 7 days)
    │
    ▼
[API Server]
    │
    ├── Application Cache (Redis: 1 hour)
    │
    ▼
[Database]
    │
    └── DB Buffer Cache (OS Page Cache)

Cache Write Strategies:

Write-Through:
Data → Cache + DB (একই সময়ে)
✓ Consistent
✗ Write latency বেশি

Write-Behind (Write-Back):
Data → Cache (তাৎক্ষণিক) → DB (পরে async)
✓ Write fast
✗ Data loss risk (cache crash)

Write-Around:
Data → DB directly (cache skip)
Cache invalidate করা হয়।
✓ Hot data cache pollute হয় না
✗ Cache miss পরে

Cache Eviction Policies:
LRU (Least Recently Used): সবচেয়ে কম ব্যবহৃত মুছো
LFU (Least Frequently Used): সবচেয়ে কম frequency মুছো
TTL (Time to Live): নির্দিষ্ট সময় পর মুছো
```

## ৩৪.৫ Message Queue — Async Communication

```
কেন Message Queue?

সমস্যা:
User অর্ডার করল → Order Service → Email Service
Email Service বন্ধ → Order fail!
User-কে কষ্ট দেওয়া হলো।

সমাধান: Message Queue
User → Order Service → [Queue] → Email Service
Order immediately confirm!
Email Service পরে process করবে।

Kafka Architecture:
┌──────────────────────────────────────────────────────────────┐
│                         Apache Kafka                         │
│                                                              │
│  Producer (Order Service)                                    │
│       │                                                      │
│       │  Publish to Topic "orders"                           │
│       ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Topic: orders                                      │    │
│  │  ┌──────────────┬──────────────┬──────────────┐    │    │
│  │  │ Partition 0  │ Partition 1  │ Partition 2  │    │    │
│  │  │ [msg1][msg4] │ [msg2][msg5] │ [msg3][msg6] │    │    │
│  │  └──────────────┴──────────────┴──────────────┘    │    │
│  └─────────────────────────────────────────────────────┘    │
│       │                    │                    │            │
│       ▼                    ▼                    ▼            │
│  Consumer Group "email-service"                              │
│  Consumer 1     Consumer 2     Consumer 3                    │
│  (Email)        (Inventory)    (Analytics)                   │
└──────────────────────────────────────────────────────────────┘

Kafka vs RabbitMQ:
Kafka: High throughput, Event streaming, Log retention
RabbitMQ: Complex routing, Low latency, Task queues
```

## ৩৪.৬ CAP Theorem

```
CAP Theorem:
Distributed system-এ এই তিনটির মধ্যে
একসাথে শুধু দুটো পাওয়া সম্ভব।

C = Consistency (সব node-এ একই data)
A = Availability (সবসময় response)
P = Partition Tolerance (network failure handle)

          C
         / \
        /   \
       /     \
      /       \
     A─────────P

CA (Consistency + Availability):
Network partition হলে system বন্ধ করে দেয়।
Traditional RDBMS (MySQL, PostgreSQL) single node

CP (Consistency + Partition Tolerance):
Network issue-এ কিছু request reject করে।
HBase, Zookeeper, MongoDB (strong consistency mode)

AP (Availability + Partition Tolerance):
Network issue-এ stale data দেয়।
Cassandra, DynamoDB, CouchDB

বাস্তবে:
Network Partition সবসময় হতে পারে।
তাই P বাদ দেওয়া সম্ভব নয়।
মূল প্রশ্ন: C নাকি A?

User-facing app: AP (availability বেশি গুরুত্বপূর্ণ)
Financial system: CP (consistency বেশি গুরুত্বপূর্ণ)
```

## ৩৪.৭ Rate Limiting Algorithms

```
1. Token Bucket:
একটি bucket আছে, প্রতি সেকেন্ডে N টি token যোগ হয়।
Request করলে token খরচ হয়।
Token শেষ → Request reject।

Bucket size: 100 tokens (burst allowed)
Refill rate: 10 tokens/second
User করতে পারবে: 10 req/second normal, 100 burst

2. Leaky Bucket:
Request একটি queue-এ জমে।
Queue থেকে fixed rate-এ process হয়।
Queue full → Request drop।

Rate: সবসময় fixed (কোনো burst নেই)
Smooth output

3. Fixed Window Counter:
প্রতি minute-এ সর্বোচ্চ N request।
Window reset হলে counter reset।

সমস্যা: Window boundary-তে 2x burst possible।
:59 → 100 requests + 1:00 → 100 requests = 200 in 2 seconds!

4. Sliding Window Log:
প্রতিটি request-এর timestamp রাখা হয়।
Last 1 minute-এর requests count করা হয়।
সবচেয়ে accurate কিন্তু memory বেশি লাগে।

5. Sliding Window Counter (সর্বোত্তম):
Fixed window + interpolation।
Memory efficient + accurate।

Implementation (Redis):
```

```dart
// Rate Limiting in Flutter Backend (Dart):
class RateLimiter {
  final Redis _redis;
  final int _maxRequests;
  final Duration _window;
  
  RateLimiter({
    required Redis redis,
    required int maxRequests,
    required Duration window,
  })  : _redis = redis,
        _maxRequests = maxRequests,
        _window = window;
  
  Future<RateLimitResult> checkLimit(String clientId) async {
    final key = 'rate_limit:$clientId';
    final now = DateTime.now().millisecondsSinceEpoch;
    final windowStart = now - _window.inMilliseconds;
    
    // Sliding window log with Redis Sorted Set
    final pipe = _redis.pipeline();
    pipe.zremrangebyscore(key, 0, windowStart); // পুরনো entries মুছো
    pipe.zadd(key, now.toDouble(), now.toString()); // নতুন request যোগ
    pipe.zcard(key); // Count
    pipe.expire(key, _window.inSeconds + 1);
    
    final results = await pipe.exec();
    final count = results[2] as int;
    
    final remaining = (_maxRequests - count).clamp(0, _maxRequests);
    final isAllowed = count <= _maxRequests;
    
    return RateLimitResult(
      allowed: isAllowed,
      remaining: remaining,
      resetAt: DateTime.fromMillisecondsSinceEpoch(
        now + _window.inMilliseconds,
      ),
    );
  }
}
```

## ৩৪.৮ Consistent Hashing

```
সমস্যা: Cache Server বাড়ালে সব cache invalid হয়!

সাধারণ Hashing:
Server 3টি: hash(key) % 3 = server index
Server 4টি হলে: hash(key) % 4 = সব index পরিবর্তন!
৭৫% cache miss!

Consistent Hashing সমাধান:

Hash Ring (0 থেকে 360):
           0/360
            │
         330│30
        300─┼─60
        270─┼─90
        240─┼─120
         210│150
            │
           180

Server A: hash("A") = 90°
Server B: hash("B") = 180°
Server C: hash("C") = 270°

Key "user:123": hash = 120° → clockwise পরের server = Server B
Key "product:456": hash = 200° → clockwise পরের server = Server C

Server যোগ হলে: D at 30°
শুধু 270°-30° range-এর keys affect!
বাকি সব unchanged!

Virtual Nodes (better distribution):
Server A → A1, A2, A3, A4... (multiple points)
Load evenly distributed
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩৫: High Availability ও Fault Tolerance

## ৩৫.১ Availability Calculation

```
Availability = Uptime / (Uptime + Downtime)

SLA তুলনা:
┌──────────┬──────────────┬───────────────┬───────────────────┐
│  SLA     │ Downtime/yr  │ Downtime/month│ Downtime/week     │
├──────────┼──────────────┼───────────────┼───────────────────┤
│ 99%      │  87.6 hours  │  7.3 hours    │  1.7 hours        │
│ 99.9%    │  8.76 hours  │  43.8 minutes │  10.1 minutes     │
│ 99.99%   │  52.6 min    │  4.4 minutes  │  1.0 minute       │
│ 99.999%  │  5.26 min    │  26.3 seconds │  6.1 seconds      │
└──────────┴──────────────┴───────────────┴───────────────────┘

Composite Availability:
দুটি component directly connected:
A1 (99%) × A2 (99%) = 98.01%

দুটি component parallel (redundant):
1 - (1-A1) × (1-A2) = 1 - (0.01 × 0.01) = 99.99%

Redundancy বাড়ালে availability বাড়ে!
```

## ৩৫.২ SPOF দূর করা

```
Single Point of Failure (SPOF):
যদি একটি component fail করলে পুরো system বন্ধ হয়,
সেটি SPOF।

সাধারণ SPOF এবং সমাধান:

❌ SPOF: Single Load Balancer
✓ সমাধান: Active-Active LB pair (AWS ALB redundant)

❌ SPOF: Single Database
✓ সমাধান: Primary + Replica (Auto-failover)

❌ SPOF: Single DNS Server
✓ সমাধান: Multiple NS records

❌ SPOF: Single Region
✓ সমাধান: Multi-Region deployment

❌ SPOF: Single Availability Zone
✓ সমাধান: Multi-AZ (AWS-এ at least 2 AZ)

❌ SPOF: Hardcoded external API
✓ সমাধান: Fallback, Circuit Breaker

SPOF Audit Checklist:
□ Load Balancer redundant?
□ Database replica আছে?
□ Cache cluster আছে?
□ DNS multiple nameservers?
□ CDN fallback আছে?
□ External API-এর Circuit Breaker?
□ All services multi-AZ?
```

## ৩৫.৩ Active-Active vs Active-Passive

```
Active-Passive (Failover):
                     ┌──────────────────┐
                     │  Load Balancer   │
                     └────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               │               │
       ┌────────────┐         │        ┌────────────┐
       │  Primary   │         │        │  Standby   │
       │  (Active)  │         │        │ (Passive)  │
       │  Traffic   │         │        │  No Traffic│
       │  পায়       │         │        │  Monitoring│
       └────────────┘         │        └────────────┘
              │               │               │
              │ Fails!        │               │
              │               │               │
              └─────────────────── Failover ──┘
                              │
                     Standby → Active হয়

সুবিধা: সহজ
অসুবিধা: Standby wasted, Failover time (30s-2min)

Active-Active:
                     ┌──────────────────┐
                     │  Load Balancer   │
                     └────────┬─────────┘
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
       ┌────────────┐  ┌────────────┐  ┌────────────┐
       │  Server 1  │  │  Server 2  │  │  Server 3  │
       │  (Active)  │  │  (Active)  │  │  (Active)  │
       │  33% load  │  │  33% load  │  │  33% load  │
       └────────────┘  └────────────┘  └────────────┘

সুবিধা: No wasted resources, instant failover
অসুবিধা: Data consistency challenge
```

## ৩৫.৪ Disaster Recovery

```
RTO vs RPO:

RPO (Recovery Point Objective):
কতটুকু data হারানো acceptable?
RPO = 1 hour → ১ ঘণ্টার data হারাতে পারি
Backup frequency = RPO or less

RTO (Recovery Time Objective):
কতক্ষণের মধ্যে system চালু করতে হবে?
RTO = 4 hours → ৪ ঘণ্টার মধ্যে চালু করতে হবে

Business Impact:
E-commerce: RTO < 1 hour (প্রতি মিনিটে টাকা হারাচ্ছে)
Blog: RTO < 24 hours (কম critical)

DR Strategies (Cost vs Recovery):

Backup & Restore (সস্তা, ধীর):
Backup → S3 → দুর্যোগে → Restore
RTO: ঘণ্টা/দিন | RPO: ঘণ্টা

Warm Standby (মাঝারি):
Smaller version চালু থাকে → দুর্যোগে Scale up
RTO: মিনিট | RPO: মিনিট

Hot Standby / Multi-Site Active-Active (ব্যয়বহুল, দ্রুত):
Full copy চালু থাকে → Immediate failover
RTO: সেকেন্ড | RPO: সেকেন্ড

Multi-region Architecture:
┌─────────────────┐              ┌─────────────────┐
│  Region: ap-    │◄──Replication│  Region: ap-    │
│  southeast-1    │──────────────│  south-1        │
│  (Singapore)    │              │  (Mumbai)       │
│                 │              │                 │
│  Primary DB     │              │  Replica DB     │
│  App Servers    │              │  App Servers    │
│  60% Traffic    │              │  40% Traffic    │
└─────────────────┘              └─────────────────┘
                   \             /
                    \           /
                     [Route 53]
                   Latency-based routing
```

## ৩৫.৫ Chaos Engineering

```
Chaos Engineering = Production-এ ইচ্ছাকৃতভাবে failure করা
উদ্দেশ্য: দুর্বলতা খুঁজে বের করা, আগে থেকে।

Netflix Chaos Monkey:
Production-এ random server terminate করে!
"যদি যেকোনো সময় server বন্ধ হতে পারে,
তাহলে আমাদের system সেটা handle করতে পারবে।"

Chaos Experiments:
- Server terminate করা
- Network latency inject করা (100ms, 500ms)
- Database connection সীমিত করা
- CPU max করে দেওয়া
- Disk full করে দেওয়া
- DNS failure simulate

Principles:
1. Production-এ করুন (staging কাজ করে, prod-এ নাও করতে পারে)
2. Small blast radius দিয়ে শুরু করুন
3. Alert ও Monitoring আগে ঠিক করুন
4. Rollback plan রাখুন
5. Team inform করুন

Tools:
- Chaos Monkey (Netflix)
- LitmusChaos (Kubernetes)
- Gremlin (Commercial)
- AWS Fault Injection Simulator
```

## ৩৫.৬ SLA, SLO, SLI

```
SLI (Service Level Indicator):
পরিমাপযোগ্য metric।
উদাহরণ: Response time, Error rate, Availability

SLO (Service Level Objective):
SLI-র target।
উদাহরণ:
- 99.9% availability
- 95% requests < 200ms
- Error rate < 0.1%

SLA (Service Level Agreement):
SLO-র legal commitment + penalty।
"99.9% uptime না হলে credit দেব"

Error Budget:
SLO 99.9% → 0.1% allowed downtime = 8.76 hours/year

Error Budget ব্যবহার কৌশল:
- Budget বেশি থাকলে: নতুন feature deploy করুন
- Budget কম থাকলে: Reliability কাজে focus করুন
- Budget শেষ হলে: Feature freeze, সব কিছু reliability-তে

Tracking উদাহরণ:
Month শুরু: 100% budget (43.8 min allowed)
Week 1 incident: 15 min downtime → 65% budget বাকি
Week 2 no incident: 65% budget বাকি
Week 3 deployment error: 30 min → Budget শেষ! Feature freeze!

```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ৩৬: Real-world Case Studies

## ৩৬.১ Case Study 1: Flutter Chat Application

```
চ্যালেঞ্জ: ১ লক্ষ concurrent user-এর Chat App বানান।
```

**Requirements:**
- Real-time messaging (< 100ms latency)
- Message delivery guarantee
- Offline message queue
- Read receipts
- Push Notification

**Architecture:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    Flutter Chat App Architecture                 │
│                                                                 │
│  [Flutter App]                                                  │
│       │                                                         │
│       │ HTTPS/WSS                                               │
│       ▼                                                         │
│  [Cloudflare] ← DDoS Protection, CDN                           │
│       │                                                         │
│       ├── Static Assets → CDN Edge                             │
│       │                                                         │
│       └── API/WS → [Load Balancer (L7)]                        │
│                         │                                       │
│              ┌──────────┴──────────┐                           │
│              ▼                     ▼                           │
│       [Chat Server 1]       [Chat Server 2]                    │
│       (WebSocket)           (WebSocket)                         │
│              │                     │                           │
│              └──────────┬──────────┘                           │
│                         ▼                                       │
│              [Redis Pub/Sub + Cache]                            │
│              │          │          │                            │
│         ┌────┘     ┌────┘     ┌────┘                           │
│         ▼          ▼          ▼                                 │
│   [Kafka Topic: messages]                                       │
│         │                                                       │
│    ┌────┴──────────────────┐                                    │
│    ▼                       ▼                                    │
│ [Message DB              [Notification                         │
│  (Cassandra)]             Worker]                              │
│  High write                   │                                │
│  throughput               [FCM/APNs]                           │
│                               │                                │
│                          Mobile Push                           │
└─────────────────────────────────────────────────────────────────┘
```

**প্রতিটি উপাদানের কারণ:**

| উপাদান | কেন? |
|--------|------|
| WebSocket | Real-time bidirectional |
| Redis Pub/Sub | Cross-server message routing |
| Kafka | Async, reliable message queue |
| Cassandra | High write throughput (chat messages) |
| FCM/APNs | Background push notification |

**Message Delivery Flow:**
```
১. User A sends "হ্যালো" to User B
২. Flutter → WebSocket → Chat Server 1
৩. Chat Server 1 → Redis Pub/Sub (room:xyz)
৪. Redis → Chat Server 2 (User B connected here)
৫. Chat Server 2 → WebSocket → User B's Flutter App
৬. Simultaneously: Chat Server 1 → Kafka
৭. Kafka → Message Consumer → Cassandra (persist)
৮. If User B offline: FCM/APNs push notification
```

**Dart Backend (Simplified):**
```dart
// WebSocket Chat Handler
class ChatWebSocketHandler {
  final RedisClient _redis;
  final KafkaProducer _kafka;
  
  Future<void> handleMessage(
    WebSocketConnection conn,
    String userId,
    ChatMessage message,
  ) async {
    // ১. Validate
    if (message.text.isEmpty || message.text.length > 4000) {
      conn.send(ErrorResponse('Invalid message'));
      return;
    }
    
    // ২. Add metadata
    final enriched = message.copyWith(
      id: Uuid().v4(),
      senderId: userId,
      timestamp: DateTime.now().toUtc(),
    );
    
    // ৩. Publish to Redis (real-time delivery)
    await _redis.publish(
      'room:${message.roomId}',
      jsonEncode(enriched.toJson()),
    );
    
    // ৪. Send to Kafka (persistence + notifications)
    await _kafka.send(
      topic: 'chat.messages',
      value: jsonEncode(enriched.toJson()),
      key: message.roomId, // Same room → same partition
    );
    
    // ৫. ACK to sender
    conn.send(MessageAck(messageId: enriched.id));
  }
}
```

---

## ৩৬.২ Case Study 2: E-Commerce App Payment Security

```
চ্যালেঞ্জ: Flutter E-commerce App-এর payment সম্পূর্ণ নিরাপদ করুন।
```

**Payment Flow Architecture:**
```
Flutter App
    │
    │ ① Product select, checkout
    ▼
[API Gateway] ← Auth validation
    │
    │ ② Create Payment Intent
    ▼
[Order Service]
    │
    │ ③ Generate payment session
    ▼
[Payment Gateway (Stripe/SSLCommerz)]
    │
    │ ④ User enters card info (directly to PG, not your server!)
    ▼
[Payment Gateway Server]
    │
    │ ⑤ Webhook: Payment success/fail
    ▼
[Your Backend Webhook Handler] ← Signature verify
    │
    │ ⑥ Order fulfill
    ▼
[Order DB, Email Queue, Inventory]
```

**গুরুত্বপূর্ণ নিরাপত্তা নিয়ম:**
```
❌ কখনো card number আপনার server-এ নেবেন না!
✓ Payment Gateway (Stripe, SSLCommerz) সরাসরি handle করবে।

❌ Payment amount Flutter app থেকে নেবেন না!
✓ Server-side amount calculate করুন।

❌ Webhook blind বিশ্বাস করবেন না!
✓ Signature verify করুন।
```

```dart
// Flutter Payment Integration (Stripe):
import 'package:flutter_stripe/flutter_stripe.dart';

class PaymentService {
  Future<PaymentResult> processPayment(Order order) async {
    try {
      // ১. Server থেকে PaymentIntent নাও (amount server-side!)
      final intent = await _api.createPaymentIntent(
        orderId: order.id,
        // amount Flutter-এ পাঠাবেন না!
        // Server order থেকে calculate করবে
      );
      
      // ২. Stripe SDK-তে initialize
      await Stripe.instance.initPaymentSheet(
        paymentSheetParameters: SetupPaymentSheetParameters(
          paymentIntentClientSecret: intent.clientSecret,
          merchantDisplayName: 'MyShop',
          style: ThemeMode.system,
          // ৩. Card info সরাসরি Stripe-এ যাবে, আপনার server-এ নয়!
        ),
      );
      
      // ৪. Payment Sheet দেখাই
      await Stripe.instance.presentPaymentSheet();
      
      // ৫. Success — order confirm
      return PaymentResult.success(intent.orderId);
      
    } on StripeException catch (e) {
      return PaymentResult.failed(e.error.localizedMessage);
    }
  }
}

// Backend Webhook Handler (Dart):
Future<Response> stripeWebhookHandler(Request request) async {
  final body = await request.readAsString();
  final signature = request.headers['stripe-signature']!;
  
  // Signature verify — এটি অবশ্যই করতে হবে!
  final event = stripe.webhooks.constructEvent(
    body,
    signature,
    webhookSecret, // Stripe Dashboard থেকে নিন
  );
  
  if (event.type == 'payment_intent.succeeded') {
    final paymentIntent = event.data.object as PaymentIntent;
    await orderService.fulfillOrder(paymentIntent.metadata['orderId']!);
  }
  
  return Response.ok('OK');
}
```

---

## ৩৬.৩ Case Study 3: Live Streaming App

```
চ্যালেঞ্জ: Flutter Live Streaming App — ১০,০০০ concurrent viewers
```

**Streaming Architecture:**
```
                    Streamer (Flutter)
                           │
                           │ RTMP/WebRTC
                           ▼
                    [Media Server]
                    (Wowza/Ant Media)
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       [Transcoding]              [Recording]
       720p, 480p, 360p           MP4 → S3
              │
              ▼
    [Streaming CDN] ← HLS/DASH segments
    (AWS CloudFront/
     Cloudflare Stream)
              │
    ┌─────────┴─────────┐
    ▼                   ▼
Viewer 1           Viewer N
(Flutter HLS)    (Flutter HLS)

Live Chat:
Viewer → WebSocket → Chat Server → Redis Pub/Sub → All viewers
```

**HLS (HTTP Live Streaming):**
```
HLS কিভাবে কাজ করে:
Streamer → Media Server → .ts segments (2-10 second chunks)
                          + .m3u8 playlist

Viewer:
GET /live/stream1.m3u8  ← playlist
#EXTM3U
#EXT-X-TARGETDURATION:6
#EXTINF:6.0,
/live/stream1-000001.ts   ← chunk 1
#EXTINF:6.0,
/live/stream1-000002.ts   ← chunk 2

প্রতি chunk CDN-এ cache হয়।
লক্ষ viewer CDN থেকে নেয় — origin server চাপ নেই!
```

```dart
// Flutter HLS Player:
import 'package:better_player/better_player.dart';

class LiveStreamPlayer extends StatefulWidget {
  final String streamUrl;
  
  @override
  State<LiveStreamPlayer> createState() => _LiveStreamPlayerState();
}

class _LiveStreamPlayerState extends State<LiveStreamPlayer> {
  late BetterPlayerController _controller;
  
  @override
  void initState() {
    super.initState();
    
    _controller = BetterPlayerController(
      BetterPlayerConfiguration(
        autoPlay: true,
        looping: false,
        fullScreenByDefault: false,
        controlsConfiguration: BetterPlayerControlsConfiguration(
          showControls: true,
          enableFullscreen: true,
          enablePlayPause: true,
          enableProgressBar: false, // Live streaming-এ নেই
        ),
      ),
      betterPlayerDataSource: BetterPlayerDataSource(
        BetterPlayerDataSourceType.network,
        widget.streamUrl,
        videoFormat: BetterPlayerVideoFormat.hls,
        liveStream: true,  // Live streaming mode!
        bufferingConfiguration: const BetterPlayerBufferingConfiguration(
          minBufferMs: 2000,   // কম buffer = কম latency
          maxBufferMs: 5000,
          bufferForPlaybackMs: 1500,
        ),
        cacheConfiguration: const BetterPlayerCacheConfiguration(
          useCache: false, // Live stream cache করবেন না!
        ),
      ),
    );
  }
}
```

---

## ৩৬.৪ Case Study 4: IoT Dashboard — Flutter + MQTT

```
চ্যালেঞ্জ: IoT sensors data real-time দেখান Flutter Dashboard-এ
           ১০,০০০ sensors, প্রতি ৫ সেকেন্ডে data পাঠায়।
```

**MQTT কী?**
```
MQTT = Message Queuing Telemetry Transport
IoT-র জন্য designed lightweight protocol।

HTTP vs MQTT:
HTTP: Client pull করে (polling)
MQTT: Publish-Subscribe (event-driven)

HTTP overhead: ~800 bytes headers + body
MQTT overhead: মাত্র 2 bytes header!

IoT-র জন্য perfect!
```

**Architecture:**
```
IoT Sensors (Temperature, Humidity, etc.)
    │
    │ MQTT Publish (Port 1883/8883 TLS)
    ▼
[MQTT Broker] ← (Mosquitto/AWS IoT Core/EMQX)
Topic: sensors/{deviceId}/data
    │
    │ Subscribe
    ├──────────────────┬─────────────────┐
    ▼                  ▼                 ▼
[Data Processor]  [Alert Service]  [Analytics]
(TimescaleDB)     (Email/SMS)       (Grafana)
    │
    │ WebSocket/REST
    ▼
[Flutter Dashboard]
Real-time charts, maps, alerts
```

```dart
// Flutter MQTT Client:
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';

class MqttDashboardService {
  late final MqttServerClient _client;
  final _dataController = StreamController<SensorData>.broadcast();
  
  Stream<SensorData> get sensorStream => _dataController.stream;
  
  Future<void> connect() async {
    _client = MqttServerClient.withPort(
      'mqtt.myapp.com',
      'flutter_dashboard_${Uuid().v4()}',
      8883, // TLS port
    )
      ..secure = true
      ..securityContext = SecurityContext.defaultContext
      ..keepAlivePeriod = 30
      ..connectTimeoutPeriod = 10000
      ..logging(on: false);
    
    _client.connectionMessage = MqttConnectMessage()
        .withClientIdentifier('dashboard')
        .withWillQos(MqttQos.atLeastOnce)
        .authenticateAs('dashboard_user', 'secret_password')
        .startClean();
    
    await _client.connect();
    
    // সব sensor subscribe করি:
    _client.subscribe('sensors/+/data', MqttQos.atLeastOnce);
    // '+' = single-level wildcard (যেকোনো deviceId)
    
    _client.updates!.listen((messages) {
      for (final message in messages) {
        final payload = message.payload as MqttPublishMessage;
        final data = MqttPublishPayload.bytesToStringAsString(
          payload.payload.message,
        );
        
        final sensor = SensorData.fromJson(jsonDecode(data));
        _dataController.add(sensor);
      }
    });
  }
  
  // Dashboard Chart:
  // StreamBuilder<SensorData>(
  //   stream: mqttService.sensorStream,
  //   builder: (context, snapshot) {
  //     if (snapshot.hasData) {
  //       chartData.add(snapshot.data!);
  //       return LineChart(data: chartData);
  //     }
  //     return const LoadingChart();
  //   },
  // )
}
```

**MQTT QoS Levels:**
```
QoS 0 (At Most Once):
Fire and forget। Message হারাতে পারে।
IoT sensor (non-critical data) উপযুক্ত।

QoS 1 (At Least Once):
ACK চাই। Duplicate পাঠাতে পারে।
Command, Control message উপযুক্ত।

QoS 2 (Exactly Once):
Handshake protocol। Exactly once।
Financial transaction উপযুক্ত। Overhead বেশি।
```

---

## ৩৬.৫ Tech Lead হিসেবে নেটওয়ার্ক ডিজাইন Framework

```
নতুন System Design করতে বসলে এই প্রশ্নগুলো করুন:

1. Scale বোঝুন:
   - কতজন concurrent user?
   - কত requests/second?
   - Data size কত?
   - Read:Write ratio কত?

2. Availability Requirements:
   - SLA কত? (99.9%? 99.99%?)
   - Downtime acceptable কতটুকু?
   - Data loss acceptable?

3. Latency Requirements:
   - API response time < কত?
   - Real-time দরকার?
   - Geography কোথায়?

4. Security Requirements:
   - কী ধরনের data? (PII? Payment?)
   - Compliance দরকার? (PCI-DSS? GDPR?)
   - Who can access what?

5. Network Design Decisions:
   - Sync vs Async communication
   - REST vs gRPC vs GraphQL
   - WebSocket vs Polling vs SSE
   - CDN strategy
   - Cache strategy
   - Database selection

Tech Lead Communication:
"আমি X পছন্দ করি কারণ Y। Trade-off হলো Z।
আমাদের use case-এ Y বেশি গুরুত্বপূর্ণ।"

সবসময় trade-off নিয়ে কথা বলুন।
কোনো perfect solution নেই।
Context অনুযায়ী সেরা সমাধান বেছে নিন।
```

---

## ৩৬.৬ সারসংক্ষেপ — আপনার নেটওয়ার্কিং যাত্রা

```
আপনি এই বই থেকে যা শিখলেন:

PART 1-3: ভিত্তি
├── Binary → কম্পিউটার কিভাবে কথা বলে
├── OSI/TCP-IP → নেটওয়ার্কের মানচিত্র
├── MAC/IP → ডিভাইস ও নেটওয়ার্ক পরিচয়
├── Switch/Router → ট্র্যাফিক নির্দেশনা
└── NAT → IP ভাগাভাগি

PART 4-5: Core Protocols
├── IP/Subnet → ঠিকানার বিজ্ঞান
├── TCP → নির্ভরযোগ্য যোগাযোগ
├── UDP → দ্রুত যোগাযোগ
└── Socket → প্রোগ্রামিং interface

PART 6: Application Layer
├── DNS → নাম থেকে ঠিকানা
├── HTTP/HTTPS → ওয়েবের ভাষা
├── WebSocket → Real-time যোগাযোগ
├── gRPC → উচ্চ-কার্যক্ষম microservice
└── SSH/SMTP → বিশেষ প্রোটোকল

PART 7: Security
├── TLS → এনক্রিপশনের বিজ্ঞান
├── Firewall/WAF → সুরক্ষা স্তর
├── VPN → নিরাপদ টানেল
└── JWT/OAuth → পরিচয় ও অনুমতি

PART 8: Modern Architecture
├── Load Balancer → ট্র্যাফিক বণ্টন
├── CDN → কন্টেন্ট বিতরণ
├── Microservices → আধুনিক কাঠামো
├── API Gateway → প্রবেশদ্বার
└── Service Mesh → অটোমেশন

PART 9: Flutter
├── HTTP/Dio → সঠিক implementation
├── WebSocket → Real-time app
├── gRPC/GraphQL → উন্নত protocol
└── Optimization → Performance ও Battery

PART 10: System Design
├── Scaling → বৃদ্ধির কৌশল
├── High Availability → সর্বদা চালু
└── Case Studies → বাস্তব অভিজ্ঞতা

পরবর্তী পদক্ষেপ:
□ Wireshark দিয়ে real traffic দেখুন
□ একটি Flutter app বানান সব concept apply করে
□ AWS/GCP Free Tier-এ cloud networking practice করুন
□ System Design সাক্ষাৎকারের জন্য prepare হন
□ CCNA বা AWS Networking Specialty বিবেচনা করুন
```

**একজন Tech Lead-এর মানসিকতা:**

> *"আমি জানি এই system কিভাবে কাজ করে, কোথায় সমস্যা হতে পারে, কিভাবে scale হবে, কিভাবে নিরাপদ থাকবে। আমি trade-off বুঝি এবং context অনুযায়ী সিদ্ধান্ত নিই।"*

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

## 📚 রেফারেন্স ও আরও পড়ুন

**বই:**
- Computer Networking: A Top-Down Approach — Kurose & Ross
- System Design Interview — Alex Xu
- Designing Distributed Systems — Burns
- High Performance Browser Networking — Grigorik

**অনলাইন:**
- RFC Documents (ietf.org) — সব প্রোটোকলের আনুষ্ঠানিক সংজ্ঞা
- Cloudflare Blog — Excellent networking articles
- ByteByteGo — System Design diagrams
- Martin Fowler's Blog — Architecture patterns

**Tools Practice:**
- Wireshark — Packet analysis
- Postman — API testing
- dig, nslookup — DNS debugging
- curl — HTTP debugging
- netstat, ss — Socket inspection
- iperf3 — Bandwidth testing
- traceroute/tracert — Route tracing

---
*🎉 সম্পূর্ণ বই পড়ার জন্য অভিনন্দন!*
*আপনি এখন নেটওয়ার্কিং-এ জিরো থেকে হিরো হওয়ার পথে।*

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)