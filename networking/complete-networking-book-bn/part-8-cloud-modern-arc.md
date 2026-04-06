# PART 8: ক্লাউড ও মডার্ন নেটওয়ার্ক আর্কিটেকচার
## Cloud & Modern Network Architecture — টেক লিড হওয়ার পথে

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৫: Load Balancer — ট্র্যাফিক বণ্টনের কৌশল

## ২৫.১ Load Balancer কেন দরকার?

```
একটি সার্ভার সমস্যা:

লক্ষ ব্যবহারকারী → [Server 1] ← সব চাপ এখানে!
                     CPU 100%
                     Memory Full
                     Response Slow
                     Finally... Crash!

Load Balancer সমাধান:

                    ┌──────────────────┐
লক্ষ ব্যবহারকারী →│  Load Balancer   │
                    └──┬─────┬─────┬──┘
                       │     │     │
                       ▼     ▼     ▼
                   [S1]   [S2]   [S3]
                  (30%)  (30%)  (40%)
                  
প্রতিটি সার্ভার মাত্র ১/৩ চাপ বহন করছে।
একটি বন্ধ হলেও বাকিরা চালু থাকে।
```

## ২৫.২ L4 vs L7 Load Balancer

```
OSI Layer অনুযায়ী Load Balancer দুই ধরনের:

L4 Load Balancer (Transport Layer):
┌─────────────────────────────────────────────────────┐
│ শুধু IP ও Port দেখে                                │
│ Content বোঝে না                                     │
│                                                     │
│ TCP Connection এবং ─────────────────────────────►  │
│ [Server নির্বাচন] ←─ IP:Port ─────────────────    │
│                                                     │
│ দ্রুত, কম CPU                                      │
│ AWS NLB (Network Load Balancer)                    │
│ HAProxy (TCP mode)                                  │
└─────────────────────────────────────────────────────┘

L7 Load Balancer (Application Layer):
┌─────────────────────────────────────────────────────┐
│ HTTP Header, URL, Cookie সব বোঝে                   │
│                                                     │
│ /api/* → API Servers                                │
│ /static/* → CDN Servers                             │
│ /ws/* → WebSocket Servers                           │
│ মোবাইল User-Agent → Mobile Optimized Server         │
│                                                     │
│ TLS Termination করতে পারে                          │
│ SSL Offloading                                      │
│ AWS ALB (Application Load Balancer)                 │
│ Nginx, HAProxy (HTTP mode)                          │
└─────────────────────────────────────────────────────┘
```

## ২৫.৩ Load Balancing Algorithms

```
1. Round Robin (পালাক্রমে):
Request 1 → Server 1
Request 2 → Server 2
Request 3 → Server 3
Request 4 → Server 1 (চক্রাকারে)
...
সহজ, কিন্তু server-এর capacity বিবেচনা করে না

2. Weighted Round Robin:
Server 1: weight=3 (শক্তিশালী)
Server 2: weight=1 (দুর্বল)

Request 1,2,3 → Server 1
Request 4     → Server 2
Request 5,6,7 → Server 1
...

3. Least Connection:
সবসময় সবচেয়ে কম active connection-এর Server-এ পাঠায়।
Server 1: 50 connections
Server 2: 30 connections ← পরের request এখানে
Server 3: 45 connections

4. IP Hash (Consistent):
Client IP দিয়ে hash → সবসময় একই Server-এ যায়
Hash(203.0.113.5) % 3 = Server 2

Sticky Session-এর জন্য ভালো
কিন্তু একটি IP থেকে অনেক user থাকলে (NAT) সমস্যা

5. Least Response Time:
সবচেয়ে কম response time-এর Server-এ পাঠায়
Advanced, health monitoring দরকার

6. Random:
Randomly Server নির্বাচন
Surprisingly effective for large server pools!
```

## ২৫.৪ Health Check

```
Health Check কিভাবে কাজ করে:

Load Balancer প্রতি ৩০ সেকেন্ডে:
┌─────────────────────────────────────────────────┐
│ GET /health → Server 1                          │
│ Response: 200 OK ✓ → Server 1 healthy           │
│                                                 │
│ GET /health → Server 2                          │
│ Response: 500 Error ✗ → Server 2 unhealthy!     │
│ → Server 2 traffic পাঠানো বন্ধ                 │
│                                                 │
│ GET /health → Server 3                          │
│ Timeout ✗ → Server 3 unreachable!              │
│ → Server 3 traffic পাঠানো বন্ধ                 │
└─────────────────────────────────────────────────┘

Health Check Endpoint উদাহরণ:
```

```dart
// Flutter Backend (Dart Shelf server):
import 'package:shelf/shelf.dart';

Response healthHandler(Request request) {
  // Database, cache, external service check
  final checks = {
    'database': _checkDatabase(),
    'redis': _checkRedis(),
    'status': 'healthy',
    'timestamp': DateTime.now().toIso8601String(),
    'version': '1.2.3',
  };
  
  final isHealthy = checks['database'] == true && checks['redis'] == true;
  
  return Response(
    isHealthy ? 200 : 503,
    body: jsonEncode(checks),
    headers: {'Content-Type': 'application/json'},
  );
}
// GET /health → {"database": true, "redis": true, "status": "healthy"}
```

## ২৫.৫ Sticky Session — Session সমস্যা

```
Session সমস্যা Load Balancer-এ:

User Login করল Server 1-এ।
Session data Server 1-এ আছে।
পরের request গেল Server 2-এ।
Server 2 session চেনে না → Logout!

সমাধান ১: Sticky Session (Session Affinity)
Load Balancer Cookie set করে:
SERVERID=server1

এরপর সব request Server 1-এ যায়।
সমস্যা: Server 1 বন্ধ হলে session হারায়

সমাধান ২: Centralized Session Store (ভালো)
Server 1 ─────┐
Server 2 ──────┼──► Redis (Shared Session Store)
Server 3 ─────┘

যেকোনো Server session read করতে পারে।
Server বন্ধ হলেও session থাকে।
```

## ২৫.৬ Nginx Load Balancer Configuration

```nginx
# /etc/nginx/nginx.conf

upstream api_servers {
    least_conn;  # Least Connection algorithm
    
    server 10.0.0.1:8080 weight=3;  # শক্তিশালী server
    server 10.0.0.2:8080 weight=1;  # দুর্বল server
    server 10.0.0.3:8080 backup;   # শুধু সবাই ডাউন হলে
    
    keepalive 32;  # Connection reuse
}

server {
    listen 443 ssl http2;
    server_name api.myapp.com;
    
    # TLS Termination এখানে হয়
    ssl_certificate /etc/ssl/cert.pem;
    ssl_certificate_key /etc/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    
    location /api/ {
        proxy_pass http://api_servers;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # Timeout
        proxy_connect_timeout 5s;
        proxy_read_timeout 30s;
        
        # Health check
        proxy_next_upstream error timeout http_500 http_502 http_503;
    }
    
    # WebSocket support
    location /ws/ {
        proxy_pass http://api_servers;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

**Tech Lead টিপস:**
- L7 Load Balancer TLS termination করুক — Backend-এ plain HTTP
- Health check endpoint-এ dependency check রাখুন
- Connection Draining: Server remove করার আগে existing connection শেষ করতে দিন
- Cross-AZ Load Balancing ব্যবহার করুন AWS-এ

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৬: CDN — কন্টেন্ট দ্রুত পৌঁছে দেওয়ার রহস্য

## ২৬.১ CDN কেন দরকার?

```
CDN ছাড়া:
ঢাকার User → API Server (সিঙ্গাপুর) → ছবি ডাউনলোড
দূরত্ব: ~3,000 km
Latency: ~80ms (শুধু যাওয়া-আসায়)

CDN সহ:
ঢাকার User → CDN Edge (ঢাকা) → ছবি ডাউনলোড
দূরত্ব: ~10 km
Latency: ~1ms!

CDN = Content Delivery Network
বিশ্বের বিভিন্ন স্থানে Edge Server রাখে।
User-এর কাছের Server থেকে content দেয়।
```

## ২৬.২ CDN Architecture

```
CDN Global Distribution:

                 [Origin Server]
                  (সিঙ্গাপুর)
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   [Edge: ঢাকা]  [Edge: মুম্বাই] [Edge: লন্ডন]
        │              │              │
        ▼              ▼              ▼
  ঢাকার Users  মুম্বাইর Users  লন্ডনের Users

Cache Hit (Content আছে):
User → Edge Server → Cache Hit → Content পাঠায়
(Origin Server-এর সাথে কথা বলতে হয় না!)

Cache Miss (Content নেই):
User → Edge Server → Cache Miss → Origin-এ যায়
Origin → Content → Edge (Cache করে) → User
(পরের User Cache থেকে পাবে)
```

## ২৬.৩ Pull vs Push CDN

```
Pull CDN (সবচেয়ে সহজ):
User → CDN Edge → "নেই" → Origin → Content
CDN নিজেই origin থেকে pull করে।
Lazy loading — প্রথম request ধীর, পরেরটা দ্রুত।

উদাহরণ: Cloudflare, AWS CloudFront (default)

Push CDN:
আপনি নিজে CDN-এ content upload করেন।
Origin-এর উপর নির্ভর কম।
Large file (video, software) distribution-এ ভালো।

উদাহরণ: AWS S3 + CloudFront (manual invalidation)
```

## ২৬.৪ Cache Invalidation — সবচেয়ে কঠিন সমস্যা

```
"There are only two hard things in Computer Science:
cache invalidation and naming things." — Phil Karlton

Cache Invalidation Strategies:

1. TTL (Time-to-Live):
Cache-Control: max-age=3600  ← ১ ঘণ্টা পর expire
সহজ কিন্তু stale content দেখাতে পারে।

2. Versioned URLs (সবচেয়ে ভালো!):
/static/app.js → /static/app.v1.2.js
নতুন version deploy করলে URL পরিবর্তন।
CDN পুরনো আর নতুন দুটোই রাখতে পারে।
Cache forever! (immutable content)

3. Manual Invalidation:
CloudFront Invalidation API:
POST /2020-05-31/distribution/DIST_ID/invalidation
{
  "Paths": {"Items": ["/images/*"]},
  "CallerReference": "unique-string"
}
সময় লাগে (~15 মিনিট), খরচ আছে।

4. Surrogate Keys / Cache Tags:
CDN content-এ tag দিন।
Tag দিয়ে একসাথে অনেক content invalidate।
Cloudflare, Fastly support করে।
```

## ২৬.৫ Flutter App-এ CDN Optimization

```dart
// Image Loading with CDN:
class CdnImageWidget extends StatelessWidget {
  final String imageId;
  final int width;
  final int height;
  
  const CdnImageWidget({
    required this.imageId,
    required this.width,
    required this.height,
  });
  
  // CDN-এ Image Transformation:
  // Cloudflare Image Resizing
  // AWS CloudFront + Lambda@Edge
  // Imgix
  
  String get cdnUrl {
    // Device pixel ratio অনুযায়ী সঠিক size
    final dpr = WidgetsBinding.instance.window.devicePixelRatio;
    final actualWidth = (width * dpr).round();
    final actualHeight = (height * dpr).round();
    
    // Cloudflare Image Resizing
    return 'https://cdn.myapp.com/cdn-cgi/image/'
        'width=$actualWidth,height=$actualHeight,'
        'format=auto,quality=85'
        '/images/$imageId';
  }
  
  @override
  Widget build(BuildContext context) {
    return CachedNetworkImage(
      imageUrl: cdnUrl,
      width: width.toDouble(),
      height: height.toDouble(),
      fit: BoxFit.cover,
      placeholder: (context, url) => const ShimmerPlaceholder(),
      errorWidget: (context, url, error) => const ErrorImage(),
      cacheManager: CacheManager(
        Config(
          'cdn_cache',
          stalePeriod: const Duration(days: 7),
          maxNrOfCacheObjects: 200,
        ),
      ),
    );
  }
}

// CDN URL-এ version যোগ করা:
String getStaticAssetUrl(String filename) {
  const buildNumber = String.fromEnvironment('BUILD_NUMBER', defaultValue: '1');
  return 'https://cdn.myapp.com/static/v$buildNumber/$filename';
}
```

## ২৬.৬ CDN ও TLS

```
TLS Termination at CDN Edge:

User (ঢাকা) ──HTTPS──► CDN Edge (ঢাকা)
                              │
                        TLS Terminate এখানে
                              │
                         ──HTTP──► Origin (সিঙ্গাপুর)
                         (Private network হলে OK)
                         (Public হলে HTTPS রাখুন!)

CDN Origin Connection:
Full HTTPS: User→CDN (TLS) + CDN→Origin (TLS) — সবচেয়ে নিরাপদ
Flexible:  User→CDN (TLS) + CDN→Origin (HTTP) — শুধু user-facing secure
Off:       সব HTTP — ⚠️ বিপজ্জনক

Cloudflare SSL Modes:
- Off: No HTTPS
- Flexible: Edge only
- Full: End-to-end (self-signed OK)
- Full (Strict): End-to-end (valid cert required) ← recommended
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৭: Microservices Networking — সার্ভিসদের কথোপকথন

## ২৭.১ Monolith থেকে Microservices

```
Monolith:
┌─────────────────────────────────────────┐
│           একটি বড় Application           │
│  ┌──────────┬──────────┬──────────────┐ │
│  │   User   │ Product  │    Order     │ │
│  │  Module  │  Module  │    Module    │ │
│  └──────────┴──────────┴──────────────┘ │
│  একটি Database, একটি Deployment        │
└─────────────────────────────────────────┘

সমস্যা:
- একটি module-এ bug → পুরো app down
- একটি module scale করতে হলে সব scale করতে হয়
- Technology lock-in

Microservices:
┌──────────┐  ┌──────────┐  ┌──────────┐
│  User    │  │ Product  │  │  Order   │
│ Service  │  │ Service  │  │ Service  │
│ :8001    │  │ :8002    │  │ :8003    │
└────┬─────┘  └────┬─────┘  └────┬─────┘
     │              │              │
     ▼              ▼              ▼
  UserDB        ProductDB      OrderDB

নেটওয়ার্ক চ্যালেঞ্জ:
- সার্ভিসগুলো কিভাবে একে অপরকে খুঁজবে?
- একটি সার্ভিস বন্ধ হলে কী হবে?
- কিভাবে কথা বলবে?
- কিভাবে জানব কোন সার্ভিস healthy?
```

## ২৭.২ Service Discovery — সার্ভিস খোঁজার কৌশল

```
সমস্যা: Microservices Dynamic IP পায়
Container restart হলে IP পরিবর্তন হয়!
Hardcoded IP ব্যবহার করা সম্ভব নয়।

সমাধান: Service Registry

Client-side Discovery:
┌──────────────┐     ┌───────────────────┐
│ Order Service│────►│  Service Registry  │
│              │     │  (Consul, Eureka)  │
│              │◄────│  "User Service at  │
│              │     │  10.0.0.5:8001"   │
└──────┬───────┘     └───────────────────┘
       │ Load Balance নিজেই করে
       ▼
┌──────────────┐
│ User Service │
│ 10.0.0.5:8001│
└──────────────┘

Server-side Discovery:
┌──────────────┐     ┌────────────────┐     ┌──────────────┐
│ Order Service│────►│ Load Balancer  │────►│ User Service │
│              │     │ (knows all     │     │ 10.0.0.5:8001│
└──────────────┘     │  instances)    │     └──────────────┘
                     └────────────────┘
                     (AWS ALB, Kubernetes Service)

Kubernetes-এ Service Discovery:
# Service তৈরি করলে DNS entry তৈরি হয়:
user-service.default.svc.cluster.local → User Service Pod IPs
```

## ২৭.৩ Synchronous vs Asynchronous Communication

```
Synchronous (REST/gRPC):
┌──────────┐          ┌──────────┐
│  Order   │──────────│   User   │
│  Service │◄─────────│  Service │
└──────────┘          └──────────┘
সুবিধা: সহজ, তাৎক্ষণিক response
অসুবিধা: User Service বন্ধ → Order Service fail!
Tight coupling

Asynchronous (Message Queue):
┌──────────┐   publish   ┌─────────────┐  consume  ┌──────────┐
│  Order   │────────────►│   Message   │◄──────────│  Email   │
│  Service │             │    Queue    │           │  Service │
└──────────┘             │  (Kafka/    │           └──────────┘
                         │  RabbitMQ)  │  consume  ┌──────────┐
                         │             │◄──────────│Inventory │
                         └─────────────┘           │  Service │
                                                   └──────────┘
সুবিধা: Loose coupling, resilient
Email Service বন্ধ থাকলেও message queue-এ থাকে
পরে Email Service উঠলে process করবে
```

## ২৭.৪ Circuit Breaker Pattern

```
বাস্তব উদাহরণ:
ঘরের বৈদ্যুতিক সার্কিট ব্রেকার → অতিরিক্ত current → trip করে
বাকি circuit রক্ষা করে।

Software Circuit Breaker:

Closed State (Normal):
Order Service → User Service → OK

Open State (Circuit Broken):
User Service ৫ বার fail করেছে।
Circuit Breaker "Open" হয়ে গেছে।
Order Service → Circuit Breaker → Fallback Response (User Service-এ যায় না!)
User Service recover করার সুযোগ পায়।

Half-Open State (Testing):
কিছুক্ষণ পর Circuit Breaker test করে:
Order Service → Circuit Breaker → User Service → OK?
যদি OK → Closed হয়ে যায়
যদি Fail → আবার Open

States:
┌─────────┐  failures > threshold   ┌──────────┐
│ CLOSED  │──────────────────────►  │  OPEN    │
│(Normal) │                         │(No calls)│
└────┬────┘    ◄──────────────────── └────┬─────┘
     │          success                   │
     │                          timeout   │
     │         ┌───────────────┐          │
     └────────►│  HALF-OPEN   │◄─────────┘
               │ (Test call)  │
               └──────────────┘
```

```dart
// Dart-এ Circuit Breaker implementation:
class CircuitBreaker<T> {
  final int failureThreshold;
  final Duration timeout;
  final Duration halfOpenDuration;
  
  int _failures = 0;
  CircuitState _state = CircuitState.closed;
  DateTime? _openedAt;
  
  CircuitBreaker({
    this.failureThreshold = 5,
    this.timeout = const Duration(seconds: 30),
    this.halfOpenDuration = const Duration(seconds: 10),
  });
  
  Future<T> execute(Future<T> Function() action) async {
    switch (_state) {
      case CircuitState.open:
        if (DateTime.now().difference(_openedAt!) > halfOpenDuration) {
          _state = CircuitState.halfOpen;
          return await _tryExecute(action);
        }
        throw CircuitOpenException('Circuit is OPEN. Service unavailable.');
        
      case CircuitState.halfOpen:
      case CircuitState.closed:
        return await _tryExecute(action);
    }
  }
  
  Future<T> _tryExecute(Future<T> Function() action) async {
    try {
      final result = await action().timeout(timeout);
      _onSuccess();
      return result;
    } catch (e) {
      _onFailure();
      rethrow;
    }
  }
  
  void _onSuccess() {
    _failures = 0;
    _state = CircuitState.closed;
  }
  
  void _onFailure() {
    _failures++;
    if (_failures >= failureThreshold) {
      _state = CircuitState.open;
      _openedAt = DateTime.now();
      print('Circuit OPENED after $_failures failures');
    }
  }
}

enum CircuitState { closed, open, halfOpen }
```

## ২৭.৫ Retry ও Timeout Strategy

```
Retry with Exponential Backoff:

Attempt 1: Immediately
Attempt 2: 1 second wait
Attempt 3: 2 seconds wait
Attempt 4: 4 seconds wait
Attempt 5: 8 seconds wait (max)

+ Jitter (random offset) যোগ করুন:
সবাই একই সময়ে retry না করুক!
Wait = min(cap, base * 2^attempt) + random(0, 1000)ms

Timeout Strategy:
┌───────────────────────────────────────────────────┐
│  Connect Timeout: 3s  (connection establish)      │
│  Read Timeout: 10s    (response পাওয়া)             │
│  Write Timeout: 10s   (request পাঠানো)             │
│  Total Timeout: 30s   (সব মিলিয়ে)                 │
└───────────────────────────────────────────────────┘
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৮: API Gateway — সব API-এর প্রবেশদ্বার

## ২৮.১ API Gateway কী?

```
API Gateway ছাড়া:
Flutter App
    │
    ├──────── /users → User Service :8001
    ├──────── /products → Product Service :8002
    ├──────── /orders → Order Service :8003
    └──────── /payments → Payment Service :8004

সমস্যা:
- App অনেক IP/Port মনে রাখতে হয়
- Auth প্রতিটি service-এ আলাদা করতে হয়
- Rate limiting সব জায়গায় আলাদা
- SSL cert সব service-এ

API Gateway সহ:
Flutter App
    │
    ▼
[API Gateway] ← একটি Entry Point
    │           Auth, Rate Limit, Logging এখানে
    │
    ├────► User Service (Internal)
    ├────► Product Service (Internal)
    ├────► Order Service (Internal)
    └────► Payment Service (Internal)
```

## ২৮.২ API Gateway Features

```
1. Routing:
GET /v1/users → user-service
GET /v1/products → product-service
POST /v1/orders → order-service

2. Authentication:
JWT Token validate করে।
Invalid হলে 401 দেয়, services-এ পাঠায় না।

3. Rate Limiting:
প্রতি IP থেকে ১০০ request/minute।
X-RateLimit-Remaining header যোগ করে।

4. Request/Response Transformation:
Backend response → Client-friendly format
Header add/remove
Request validation

5. SSL Termination:
HTTPS → HTTP (internal)
Backend services plain HTTP ব্যবহার করতে পারে

6. Load Balancing:
Multiple instances-এ request ভাগ করে

7. Caching:
Same request-এর response cache করে

8. Logging & Monitoring:
সব request log করে
Metrics collect করে

9. API Composition:
একটি client request → Multiple backend calls
Results combine করে → একটি response
```

## ২৮.৩ BFF Pattern — Backend for Frontend

```
সমস্যা:
Flutter Mobile App চায়: compact JSON, mobile-optimized
Web Dashboard চায়: detailed data, rich format
Admin Panel চায়: full data with relations

General API সব client-এর জন্য compromise করে।

BFF Pattern:
                        ┌──────────────────────────────┐
                        │          Microservices        │
                        │  ┌──────┐ ┌──────┐ ┌──────┐ │
                        │  │User  │ │Order │ │Prod. │ │
                        │  │Svc   │ │Svc   │ │Svc   │ │
                        │  └──────┘ └──────┘ └──────┘ │
                        └──────────────────────────────┘
                               ▲        ▲        ▲
                               │        │        │
                    ┌──────────┴┐  ┌────┴─────┐  │
                    │Mobile BFF │  │ Web BFF  │  │
                    │(Flutter)  │  │(React)   │  │
                    └─────┬─────┘  └────┬─────┘  │
                          │              │        │
                    Flutter App       Web App  Admin App

Mobile BFF:
- Compact response (bandwidth save)
- Push notification integration
- Offline sync support
- Mobile-specific business logic

Web BFF:
- Rich, detailed data
- Server-side rendering data
- Web-specific features
```

## ২৮.৪ Kong API Gateway Configuration

```yaml
# Kong declarative config (deck)

services:
  - name: user-service
    url: http://user-service:8001
    routes:
      - name: user-routes
        paths: ["/v1/users"]
        methods: ["GET", "POST", "PUT", "DELETE"]

  - name: product-service
    url: http://product-service:8002
    routes:
      - name: product-routes
        paths: ["/v1/products"]

plugins:
  # JWT Authentication
  - name: jwt
    service: user-service
    config:
      key_claim_name: kid
      claims_to_verify: ["exp"]

  # Rate Limiting
  - name: rate-limiting
    config:
      minute: 100
      policy: local

  # Response Caching
  - name: proxy-cache
    service: product-service
    config:
      response_code: [200]
      request_method: ["GET"]
      content_type: ["application/json"]
      cache_ttl: 300

  # CORS
  - name: cors
    config:
      origins: ["https://myapp.com"]
      methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
      headers: ["Authorization", "Content-Type"]
```

## ২৮.৫ API Versioning Strategy

```
Versioning Approaches:

1. URL Versioning (সবচেয়ে সহজ):
/api/v1/users
/api/v2/users
ভালো: স্পষ্ট, Cacheable
খারাপ: URL পরিবর্তন

2. Header Versioning:
Accept: application/vnd.myapp.v2+json
ভালো: Clean URL
খারাপ: Browser-এ test কঠিন

3. Query Parameter:
/api/users?version=2
ভালো: সহজ
খারাপ: Cache করা কঠিন

Recommendation:
Public API → URL Versioning (/v1/, /v2/)
Internal API → Header Versioning

Breaking vs Non-breaking Changes:
Non-breaking (backward compatible):
✓ নতুন field যোগ
✓ Optional parameter যোগ
✓ নতুন endpoint যোগ

Breaking (new version দরকার):
✗ Field নাম পরিবর্তন
✗ Field মুছে ফেলা
✗ Response structure পরিবর্তন
```

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২৯: Service Mesh — মাইক্রোসার্ভিস নেটওয়ার্কের অটোমেশন

## ২৯.১ Service Mesh কেন?

```
Microservices বড় হলে সমস্যা:
- প্রতিটি service-এ retry logic লিখতে হয়
- প্রতিটি service-এ circuit breaker লিখতে হয়
- mTLS প্রতিটি service-এ configure করতে হয়
- Distributed tracing সব জায়গায় instrument করতে হয়
- Traffic routing manually manage করতে হয়

৫০টি microservice = ৫০ জায়গায় একই কাজ!

Service Mesh সমাধান:
এই সব responsibility Application থেকে বের করে
Infrastructure-এ নিয়ে যায়।
Developer শুধু Business Logic লেখে।
```

## ২৯.২ Sidecar Pattern

```
Sidecar Pattern:
প্রতিটি Service-এর পাশে একটি Proxy Container।

┌──────────────────────────────────────────────────────┐
│  Kubernetes Pod                                       │
│  ┌─────────────────┐  ┌──────────────────────────┐  │
│  │   Your Service  │  │    Sidecar Proxy         │  │
│  │   (Business     │  │    (Envoy/Linkerd)        │  │
│  │    Logic Only)  │  │                          │  │
│  │                 │  │  - mTLS                  │  │
│  │    Port: 8080   │◄─┤  - Retry                 │  │
│  │                 │  │  - Circuit Breaker        │  │
│  └─────────────────┘  │  - Load Balancing         │  │
│                        │  - Observability         │  │
│                        │                          │  │
│                        │    Port: 15001           │  │
│                        └──────────────────────────┘  │
└──────────────────────────────────────────────────────┘
            All traffic passes through Sidecar!

Service A → Sidecar A → [Network] → Sidecar B → Service B
```

## ২৯.৩ Istio Architecture

```
Istio Components:

Data Plane:
┌─────────────────────────────────────────────────────────┐
│  Service A Pod          Service B Pod                    │
│  ┌────────┐ ┌───────┐  ┌────────┐ ┌───────┐            │
│  │Service │ │Envoy  │  │Service │ │Envoy  │            │
│  │A       │ │Proxy  │  │B       │ │Proxy  │            │
│  └────────┘ └───────┘  └────────┘ └───────┘            │
│               │                     ▲                   │
│               └─────────────────────┘                   │
│                    mTLS Encrypted                       │
└─────────────────────────────────────────────────────────┘

Control Plane:
┌─────────────────────────────────────────────────────────┐
│  istiod                                                 │
│  ┌────────────┐ ┌───────────┐ ┌────────────────┐       │
│  │   Pilot    │ │  Citadel  │ │    Galley      │       │
│  │(Routing    │ │(Certificate│ │(Configuration  │       │
│  │ Rules)     │ │ Management)│ │  Validation)   │       │
│  └────────────┘ └───────────┘ └────────────────┘       │
│          │              │              │                │
│          └──────────────┴──────────────┘                │
│                    Config push to Envoy                 │
└─────────────────────────────────────────────────────────┘
```

## ২৯.৪ Traffic Management — Canary Deployment

```
Canary Deployment with Istio:
নতুন version ধীরে ধীরে traffic পাঠান।

Step 1: v1 = 100% traffic
Step 2: v2 deploy করি (কেউ জানে না)
Step 3: v2 = 5% traffic (canary users)
Step 4: মনিটর করি — error rate, latency
Step 5: OK হলে → v2 = 50%
Step 6: OK হলে → v2 = 100%
Step 7: v1 সরিয়ে ফেলি

Istio VirtualService:
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: user-service
spec:
  http:
  - match:
    - headers:
        x-canary:
          exact: "true"
    route:
    - destination:
        host: user-service
        subset: v2
  - route:
    - destination:
        host: user-service
        subset: v1
      weight: 95  # 95% → v1
    - destination:
        host: user-service
        subset: v2
      weight: 5   # 5% → v2 (canary)
```

## ২৯.৫ Distributed Tracing

```
একটি Request-এর যাত্রা Track করা:

Flutter App → API Gateway → Order Service → User Service → DB
              ↘ Product Service → DB
              ↘ Payment Service → External API

কোথায় সময় বেশি লাগছে? কোথায় error?
Distributed Tracing দিয়ে বোঝা যায়।

Trace ID: a1b2c3d4
┌─────────────────────────────────────────────────────┐
│ API Gateway    [████████████████████████] 250ms      │
│   Order Svc     [████████████] 180ms                │
│     User Svc      [████] 60ms                       │
│       DB            [██] 40ms                       │
│     Product Svc   [██████] 90ms                     │
│       DB             [████] 55ms                    │
│   Payment Svc   [███████████████] 200ms ← Slow!     │
│     Ext. API      [████████████] 180ms ← Bottleneck!│
└─────────────────────────────────────────────────────┘

Tools: Jaeger, Zipkin, AWS X-Ray, Datadog APM

OpenTelemetry (Standard):
- Vendor-neutral tracing/metrics/logs
- যেকোনো backend-এ পাঠানো যায়
```

**Tech Lead টিপস:**
- Service Mesh না লাগলেও শুরুতে ব্যবহার করবেন না — complexity বাড়ে
- ৫-১০টি service-এর নিচে manual করুন
- Observability আগে ঠিক করুন (logging, metrics, tracing)
- Canary deployment সব production deploy-এ ব্যবহার করুন

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---
*PART 8 সম্পন্ন। পরবর্তী: PART 9 — Flutter ও Mobile Networking*