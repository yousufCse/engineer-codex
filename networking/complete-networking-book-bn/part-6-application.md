# PART 6: অ্যাপ্লিকেশন লেয়ার প্রোটোকল
## Application Layer Protocols — সফটওয়্যার ইঞ্জিনিয়ারের সবচেয়ে গুরুত্বপূর্ণ অংশ

> **মনে রাখুন:** OSI-র সবচেয়ে উপরের লেয়ার। আপনি Flutter-এ যা কোড করেন, তার সবকিছু এই লেয়ারেই শুরু হয়।

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ১৬: DNS — ইন্টারনেটের ফোনবুক

## ১৬.১ DNS কেন দরকার?

আপনি `google.com` লিখলে ব্রাউজার জানে না এর মানে কী। কম্পিউটার শুধু IP address বোঝে। তাহলে `google.com` → `142.250.192.46` — এই রূপান্তর কে করে?

উত্তর: **DNS (Domain Name System)**

```
বাস্তব উদাহরণ:
┌─────────────────────────────────────────────────────────┐
│  ফোনবুক ছাড়া আপনি কি বন্ধুর নম্বর মনে রাখতে পারবেন?  │
│                                                         │
│  "রাহেলা" → 01711-XXXXXX    (ফোনবুক করে দেয়)          │
│  "google.com" → 142.250.192.46  (DNS করে দেয়)          │
└─────────────────────────────────────────────────────────┘
```

## ১৬.২ DNS Hierarchy — তিনটি স্তরের সিস্টেম

DNS একটি বিতরণকৃত (distributed) ডেটাবেস। কোনো একটি সার্ভার সব নাম জানে না।

```
DNS Hierarchy:
                        ┌──────────────┐
                        │  Root Server │  ← "." (dot) — সবকিছুর মূল
                        │  13টি গ্রুপ  │
                        └──────┬───────┘
               ┌───────────────┼────────────────┐
               ▼               ▼                ▼
        ┌─────────┐     ┌─────────┐      ┌─────────┐
        │ .com TLD│     │ .org TLD│      │ .bd TLD │
        │  Server │     │  Server │      │  Server │
        └────┬────┘     └─────────┘      └─────────┘
             │
    ┌────────┴──────────┐
    ▼                   ▼
┌──────────┐      ┌──────────┐
│ google   │      │ facebook │
│Authorit. │      │Authorit. │
│ Server   │      │ Server   │
└──────────┘      └──────────┘
```

**৩ ধরনের DNS Server:**
| ধরন | কাজ | উদাহরণ |
|-----|-----|---------|
| **Root Server** | TLD Server-এর ঠিকানা জানে | 13টি গ্রুপ, বিশ্বব্যাপী |
| **TLD Server** | Authoritative Server-এর ঠিকানা জানে | `.com`, `.org`, `.bd` |
| **Authoritative Server** | ডোমেইনের আসল IP জানে | Google, Cloudflare |

## ১৬.৩ DNS Query প্রক্রিয়া — ধাপে ধাপে

আপনি `www.flutter.dev` লিখলেন। এখন কী হয়?

```
DNS Resolution Flow:

আপনার Flutter App / Browser
        │
        │ ① "www.flutter.dev এর IP কী?"
        ▼
┌───────────────────┐
│  Recursive        │   ← আপনার ISP বা 8.8.8.8 (Google DNS)
│  Resolver         │      এটি আপনার হয়ে কাজ করে
└────────┬──────────┘
         │
         │ ② Cache-এ নেই → Root Server জিজ্ঞেস করি
         ▼
    ┌──────────┐
    │  Root    │ ③ ".dev এর TLD Server এই ঠিকানায়"
    │  Server  │ ────────────────────────────────────►
    └──────────┘
         │
         │ ④ TLD Server জিজ্ঞেস করি
         ▼
    ┌──────────┐
    │ .dev TLD │ ⑤ "flutter.dev এর Authoritative Server এই ঠিকানায়"
    │  Server  │ ────────────────────────────────────►
    └──────────┘
         │
         │ ⑥ Authoritative Server জিজ্ঞেস করি
         ▼
    ┌──────────────────┐
    │  flutter.dev     │ ⑦ "www.flutter.dev = 199.232.xx.xx"
    │  Authoritative   │ ◄────────────────────────────────────
    └──────────────────┘
         │
         │ ⑧ Cache করে রাখি (TTL অনুযায়ী)
         ▼
    আপনার App ← ⑨ IP Address পাঠায়
```

**Recursive vs Iterative Query:**
- **Recursive:** Resolver নিজেই সব কাজ করে, শুধু final উত্তর আপনাকে দেয়
- **Iterative:** প্রতিটি Server পরবর্তী Server-এর ঠিকানা দেয়, আপনাকে নিজেই যেতে হয়

সাধারণত Client → Recursive Resolver (recursive), Resolver → Root/TLD/Auth (iterative)

## ১৬.৪ DNS Record Types — সম্পূর্ণ তালিকা

```
DNS Zone File উদাহরণ (flutter.dev):

; Record Format: Name  TTL  Class  Type  Value
flutter.dev.      300   IN    A     199.232.68.181    ← IPv4
flutter.dev.      300   IN    AAAA  2600:1901::68:181 ← IPv6
www.flutter.dev.  300   IN   CNAME  flutter.dev.      ← Alias
flutter.dev.       60   IN    MX    10 mail.flutter.dev ← Email
flutter.dev.      300   IN    NS    ns1.flutter.dev.  ← Name Server
flutter.dev.      300   IN    TXT   "v=spf1 include:..." ← Text
```

| Record | পুরো নাম | কাজ | উদাহরণ |
|--------|----------|-----|---------|
| **A** | Address | Domain → IPv4 | `google.com → 142.250.x.x` |
| **AAAA** | IPv6 Address | Domain → IPv6 | `google.com → 2607:f8b0::` |
| **CNAME** | Canonical Name | Alias তৈরি | `www → example.com` |
| **MX** | Mail Exchange | Email সার্ভার | `@company.com → mail server` |
| **NS** | Name Server | Authoritative সার্ভার | কোন DNS সার্ভার জানে |
| **TXT** | Text | যেকোনো টেক্সট | SPF, DKIM, verification |
| **PTR** | Pointer | IP → Domain (Reverse) | `142.250.x.x → google.com` |
| **SOA** | Start of Authority | Zone তথ্য | Admin, serial number |
| **SRV** | Service | সার্ভিস location | gRPC, SIP |

## ১৬.৫ DNS Caching ও TTL

```
Cache কিভাবে কাজ করে:

প্রথম Query (Cache Miss):
App → Resolver → Root → TLD → Auth → ✓ IP পাওয়া গেল
সময় লাগে: ~100-300ms

দ্বিতীয় Query (Cache Hit):
App → Resolver Cache → ✓ IP পাওয়া গেল
সময় লাগে: ~1-5ms

TTL (Time To Live):
┌─────────────────────────────────────────────┐
│ TTL = 300 মানে এই রেকর্ড ৩০০ সেকেন্ড     │
│ (৫ মিনিট) পর্যন্ত Cache-এ রাখা যাবে      │
│                                              │
│ TTL কম → Fresh data, বেশি query             │
│ TTL বেশি → Cached data, কম query            │
└─────────────────────────────────────────────┘
```

**কখন TTL কমাবেন?**
- Deploy-এর আগে TTL কমিয়ে দিন (যেমন 60 সেকেন্ড)
- IP পরিবর্তনের পরে TTL আবার বাড়ান

## ১৬.৬ DNS over HTTPS (DoH) ও DNS over TLS (DoT)

সাধারণ DNS UDP port 53-এ কাজ করে — **এনক্রিপ্টেড নয়!** ISP দেখতে পায় আপনি কোন সাইটে যাচ্ছেন।

```
সাধারণ DNS (অনিরাপদ):
App ──UDP:53──► DNS Resolver
     [plaintext, যে কেউ দেখতে পারে]

DNS over HTTPS (DoH):
App ──HTTPS:443──► DNS Resolver
     [এনক্রিপ্টেড, HTTPS ট্র্যাফিকের মধ্যে লুকানো]

DNS over TLS (DoT):
App ──TLS:853──► DNS Resolver
     [এনক্রিপ্টেড, কিন্তু port দেখলে বোঝা যায়]
```

**জনপ্রিয় DoH Providers:**
- Cloudflare: `https://1.1.1.1/dns-query`
- Google: `https://8.8.8.8/dns-query`

## ১৬.৭ Flutter-এ DNS

Flutter-এ সাধারণত OS-এর DNS ব্যবহার হয়। কিন্তু custom DNS লাগলে:

```dart
// Custom DNS Resolver with Dio
import 'dart:io';
import 'package:dio/dio.dart';

class CustomDnsHttpClient {
  static HttpClient createWithCustomDns() {
    return HttpClient()
      ..badCertificateCallback = (cert, host, port) => false;
  }
}

// DNS lookup manually
Future<String> dnsLookup(String hostname) async {
  final addresses = await InternetAddress.lookup(hostname);
  if (addresses.isNotEmpty) {
    return addresses.first.address; // IPv4 address
  }
  throw Exception('DNS lookup failed');
}

// Usage
void main() async {
  final ip = await dnsLookup('api.myapp.com');
  print('api.myapp.com = $ip');
  // Output: api.myapp.com = 203.0.113.42
}
```

## ১৬.৮ DNS Attack ও নিরাপত্তা

```
DNS Cache Poisoning Attack:
                          ┌──────────────┐
                          │  Attacker    │
                          └──────┬───────┘
                                 │ ভুয়া response পাঠায়
                                 ▼
Client → Resolver ──────────────► [ভুয়া IP Cache হয়ে যায়]
                                             │
                                             ▼
                                    ভুয়া সাইটে চলে যায়!

সমাধান: DNSSEC (DNS Security Extensions)
- Digital Signature দিয়ে DNS Record যাচাই করে
```

## ১৬.৯ গুরুত্বপূর্ণ DNS Tool

```bash
# Linux/Mac Terminal-এ:

# Basic DNS lookup
nslookup google.com

# Detailed DNS query
dig google.com

# Specific record type
dig google.com MX        # Email server
dig google.com AAAA      # IPv6
dig google.com NS        # Name servers

# Reverse lookup (IP → Domain)
dig -x 8.8.8.8

# Trace DNS resolution path
dig +trace google.com

# Query specific DNS server
dig @8.8.8.8 google.com
```

**Tech Lead টিপস:**
- Deployment-এর আগে সবসময় TTL কমান
- DNSSEC enable করুন গুরুত্বপূর্ণ ডোমেইনে
- DNS Monitoring রাখুন — DNS failure = সব ডাউন

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ১৭: HTTP/HTTPS — ওয়েবের প্রাণ

## ১৭.১ HTTP কী এবং কেন?

**HTTP (HyperText Transfer Protocol)** হলো ওয়েব ব্রাউজার এবং সার্ভারের মধ্যে কথা বলার ভাষা। এটি একটি **request-response** প্রোটোকল।

```
বাস্তব উদাহরণ — রেস্তোরাঁর অর্ডার:
┌──────────────────────────────────────────────────────┐
│                                                      │
│  আপনি (Client)     ওয়েটার (HTTP)    রান্নাঘর (Server)│
│       │                 │                  │         │
│       │── "মেনু দাও" ──►│── GET /menu ────►│         │
│       │                 │                  │         │
│       │◄── মেনু ────────│◄── 200 OK + Menu─│         │
│       │                 │                  │         │
│       │── "বিরিয়ানি" ──►│── POST /order ──►│         │
│       │                 │                  │         │
│       │◄── "অর্ডার হয়ছে"│◄── 201 Created ──│         │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## ১৭.২ HTTP-এর বিবর্তন

```
HTTP Timeline:

HTTP/0.9 (1991)        HTTP/1.0 (1996)        HTTP/1.1 (1997)
    │                       │                       │
    │ শুধু GET              │ Headers যোগ           │ Keep-Alive
    │ শুধু HTML             │ Status Codes          │ Pipelining
    │ No Headers            │ POST, HEAD            │ Virtual Hosting
    │                       │ Content-Type          │ Chunked Transfer
    ▼                       ▼                       ▼

HTTP/2 (2015)          HTTP/3 (2022)
    │                       │
    │ Multiplexing          │ QUIC (UDP-based)
    │ Header Compression    │ 0-RTT Connection
    │ Server Push           │ Built-in Encryption
    │ Binary Protocol       │ Connection Migration
    │ Stream Priority       │ No HOL Blocking
    ▼                       ▼
```

## ১৭.৩ HTTP Request গঠন — বিস্তারিত

```
HTTP Request Structure:

POST /api/v1/users HTTP/1.1              ← Request Line
Host: api.myapp.com                      │
Content-Type: application/json           │ Headers
Authorization: Bearer eyJhbGc...         │
Accept: application/json                 │
Content-Length: 45                       │
User-Agent: Dart/3.0 (dart:io)           │
                                         ▼
{"name": "রাহেল", "email": "r@a.com"}   ← Body (Payload)

┌─────────────────────────────────────────────────────┐
│  Request Line = Method + Path + HTTP Version        │
│  Headers = Key: Value pairs (metadata)              │
│  Body = Actual data (GET-এ সাধারণত থাকে না)        │
└─────────────────────────────────────────────────────┘
```

## ১৭.৪ HTTP Response গঠন

```
HTTP Response Structure:

HTTP/1.1 200 OK                          ← Status Line
Content-Type: application/json           │
Content-Length: 89                       │ Response Headers
Cache-Control: max-age=3600              │
Set-Cookie: session=abc123; HttpOnly     │
X-Request-ID: a1b2c3d4                   │
                                         ▼
{                                        ← Response Body
  "id": 1,
  "name": "রাহেল",
  "email": "r@a.com",
  "created_at": "2025-01-01T00:00:00Z"
}
```

## ১৭.৫ HTTP Methods — সম্পূর্ণ বিবরণ

| Method | কাজ | Body আছে? | Idempotent? | Safe? |
|--------|-----|-----------|-------------|-------|
| **GET** | ডেটা পড়া | না | হ্যাঁ | হ্যাঁ |
| **POST** | নতুন তৈরি | হ্যাঁ | না | না |
| **PUT** | সম্পূর্ণ আপডেট | হ্যাঁ | হ্যাঁ | না |
| **PATCH** | আংশিক আপডেট | হ্যাঁ | না | না |
| **DELETE** | মুছে ফেলা | না | হ্যাঁ | না |
| **HEAD** | শুধু Headers | না | হ্যাঁ | হ্যাঁ |
| **OPTIONS** | কী সাপোর্ট করে | না | হ্যাঁ | হ্যাঁ |

> **Idempotent মানে:** একই রিকোয়েস্ট বারবার করলেও ফলাফল একই।
> `DELETE /user/1` বারবার করলেও user 1 delete-ই থাকবে।

> **Safe মানে:** সার্ভারে কোনো পরিবর্তন করে না।

## ১৭.৬ HTTP Status Codes — সম্পূর্ণ তালিকা

```
Status Code Categories:
1xx → Informational (তথ্যমূলক)
2xx → Success (সফল)
3xx → Redirection (পুনর্নির্দেশনা)
4xx → Client Error (আপনার ভুল)
5xx → Server Error (সার্ভারের ভুল)
```

**2xx — সফলতা:**
| Code | নাম | কখন ব্যবহার |
|------|-----|-------------|
| 200 | OK | সাধারণ সফল GET |
| 201 | Created | নতুন resource তৈরি হয়েছে |
| 204 | No Content | সফল কিন্তু body নেই (DELETE) |
| 206 | Partial Content | Range request (video streaming) |

**3xx — Redirect:**
| Code | নাম | কখন ব্যবহার |
|------|-----|-------------|
| 301 | Moved Permanently | URL চিরতরে পরিবর্তন |
| 302 | Found | সাময়িক redirect |
| 304 | Not Modified | Cache valid, আবার ডাউনলোড না করুন |

**4xx — Client Error:**
| Code | নাম | কখন ব্যবহার |
|------|-----|-------------|
| 400 | Bad Request | ভুল request format |
| 401 | Unauthorized | Login করুন |
| 403 | Forbidden | Permission নেই |
| 404 | Not Found | Resource নেই |
| 409 | Conflict | ডুপ্লিকেট data |
| 422 | Unprocessable | Validation error |
| 429 | Too Many Requests | Rate limit ছাড়িয়েছে |

**5xx — Server Error:**
| Code | নাম | কখন ব্যবহার |
|------|-----|-------------|
| 500 | Internal Server Error | সার্ভারে কিছু ভেঙেছে |
| 502 | Bad Gateway | Upstream সার্ভার সমস্যা |
| 503 | Service Unavailable | সার্ভার বন্ধ/ব্যস্ত |
| 504 | Gateway Timeout | Upstream সময় শেষ |

## ১৭.৭ গুরুত্বপূর্ণ HTTP Headers

```
Request Headers:
┌────────────────────────────────────────────────────────┐
│ Host: api.example.com          ← কোন সার্ভার          │
│ Authorization: Bearer <token>  ← Authentication       │
│ Content-Type: application/json ← Body-র ধরন           │
│ Accept: application/json       ← কী ধরন চাই           │
│ Accept-Language: bn, en        ← ভাষা পছন্দ           │
│ Accept-Encoding: gzip, br      ← Compression          │
│ Cache-Control: no-cache        ← Cache নির্দেশনা      │
│ If-None-Match: "abc123"        ← ETag conditional     │
│ X-Request-ID: uuid-here        ← Tracing ID           │
└────────────────────────────────────────────────────────┘

Response Headers:
┌────────────────────────────────────────────────────────┐
│ Content-Type: application/json ← Body-র ধরন           │
│ Content-Length: 1234           ← Body-র size (bytes)  │
│ Content-Encoding: gzip         ← Compression ধরন      │
│ Cache-Control: max-age=3600    ← কতক্ষণ Cache করবে   │
│ ETag: "abc123"                 ← Resource version     │
│ Set-Cookie: session=x; Secure  ← Cookie সেট           │
│ X-RateLimit-Remaining: 95      ← বাকি request         │
│ Access-Control-Allow-Origin: * ← CORS permission      │
└────────────────────────────────────────────────────────┘
```

## ১৭.৮ CORS — Cross-Origin Resource Sharing

```
CORS সমস্যা:
                               Same Origin Policy:
Flutter Web App                Browser বলে:
(localhost:3000)  ────────►   "ভিন্ন origin-এ request?
                               নিরাপদ নয়, block করলাম!"
API Server
(api.example.com)

কেন? কারণ evil.com থেকেও আপনার API-তে
request যেতে পারে আপনার ব্রাউজার থেকে!

CORS দিয়ে সমাধান:
Browser → API: "OPTIONS /resource" (Preflight)
API → Browser: "Access-Control-Allow-Origin: https://myapp.com"
Browser: "ঠিক আছে, তাহলে real request পাঠাই"
Browser → API: "GET /resource"
```

**CORS Headers:**
```
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 86400  ← Preflight cache 1 দিন
```

## ১৭.৯ HTTP/2 — কী পরিবর্তন হলো?

```
HTTP/1.1 সমস্যা:
Client                    Server
  │──GET /style.css──────►│
  │◄─── CSS ──────────────│  (অপেক্ষা করতে হয়)
  │──GET /app.js──────────►│
  │◄─── JS ───────────────│  (এরপর)
  │──GET /image.png───────►│
  │◄─── Image ────────────│  (এরপর)
  HOL Blocking = একটি ব্লক হলে বাকি সব বন্ধ

HTTP/2 সমাধান — Multiplexing:
Client                    Server
  │──Stream 1: GET /style─►│
  │──Stream 2: GET /app───►│  (একই সময়ে!)
  │──Stream 3: GET /image─►│  (একই সময়ে!)
  │◄─Stream 2: JS─────────│
  │◄─Stream 1: CSS────────│  (যেটা আগে হয়, আগে আসে)
  │◄─Stream 3: Image──────│
```

**HTTP/2-এর সুবিধা:**
- **Multiplexing:** একই connection-এ অনেক request
- **Header Compression (HPACK):** Repeated headers compress হয়
- **Server Push:** Client request-এর আগেই সার্ভার পাঠায়
- **Binary:** Text-এর বদলে Binary — দ্রুত parse

## ১৭.১০ HTTP/3 — UDP-র উপর HTTP

```
HTTP/2 সমস্যা:
TCP-তে HOL Blocking এখনো আছে packet level-এ।
একটি packet হারালে সব stream অপেক্ষা করে।

HTTP/3 সমাধান:
┌─────────────────────────────────────────┐
│          HTTP/3 Stack                   │
├─────────────────────────────────────────┤
│              HTTP/3                     │
├─────────────────────────────────────────┤
│         QUIC Protocol                   │
├─────────────────────────────────────────┤
│          TLS 1.3 (built-in)             │
├─────────────────────────────────────────┤
│              UDP                        │
└─────────────────────────────────────────┘

QUIC Benefits:
- Independent streams (একটি হারালে অন্যগুলো চলে)
- 0-RTT connection (পুরনো server-এ reconnect দ্রুত)
- Connection Migration (Wi-Fi থেকে 4G-তে গেলেও connection টিকে)
- Built-in Encryption
```

## ১৭.১১ HTTPS — HTTP + TLS

```
HTTP (Port 80) — সব দেখা যায়:
GET /login HTTP/1.1
Host: bank.com
password=12345   ← যে কেউ পড়তে পারে!

HTTPS (Port 443) — এনক্রিপ্টেড:
[TLS Encrypted gibberish — কেউ পড়তে পারে না]

HTTPS মানে:
HTTP + TLS = HTTPS
(TLS বিস্তারিত Part 7-এ)
```

## ১৭.১২ Flutter-এ HTTP — সঠিক ব্যবহার

```dart
import 'package:dio/dio.dart';

class ApiService {
  late final Dio _dio;
  
  ApiService() {
    _dio = Dio(BaseOptions(
      baseUrl: 'https://api.myapp.com/v1',
      connectTimeout: const Duration(seconds: 10),
      receiveTimeout: const Duration(seconds: 30),
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
    ));
    
    // Interceptor দিয়ে auth token যোগ করি
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await SecureStorage.getToken();
          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          handler.next(options);
        },
        onError: (error, handler) async {
          // 401 হলে token refresh করি
          if (error.response?.statusCode == 401) {
            await refreshToken();
            // Retry original request
            handler.resolve(await _dio.fetch(error.requestOptions));
            return;
          }
          handler.next(error);
        },
        onResponse: (response, handler) {
          // Response logging
          print('${response.statusCode} ${response.requestOptions.uri}');
          handler.next(response);
        },
      ),
    );
  }
  
  // GET Request
  Future<User> getUser(int id) async {
    try {
      final response = await _dio.get('/users/$id');
      return User.fromJson(response.data);
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }
  
  // POST Request
  Future<User> createUser(CreateUserDto dto) async {
    try {
      final response = await _dio.post('/users', data: dto.toJson());
      return User.fromJson(response.data);
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }
  
  // File Upload (Multipart)
  Future<String> uploadImage(File file) async {
    final formData = FormData.fromMap({
      'file': await MultipartFile.fromFile(
        file.path,
        filename: 'image.jpg',
        contentType: MediaType('image', 'jpeg'),
      ),
    });
    
    final response = await _dio.post('/upload', data: formData);
    return response.data['url'];
  }
  
  AppException _handleError(DioException e) {
    switch (e.response?.statusCode) {
      case 400: return BadRequestException(e.response?.data);
      case 401: return UnauthorizedException();
      case 403: return ForbiddenException();
      case 404: return NotFoundException();
      case 429: return RateLimitException();
      case 500: return ServerException();
      default: return NetworkException(e.message);
    }
  }
}
```

## ১৭.১৩ REST API Design Best Practices

```
ভালো REST API URL Design:

❌ খারাপ:
GET /getUsers
POST /createUser
GET /getUserById?id=1
POST /deleteUser

✅ ভালো:
GET    /users           ← সব user
POST   /users           ← নতুন user তৈরি
GET    /users/{id}      ← নির্দিষ্ট user
PUT    /users/{id}      ← সম্পূর্ণ আপডেট
PATCH  /users/{id}      ← আংশিক আপডেট
DELETE /users/{id}      ← মুছে ফেলা
GET    /users/{id}/posts ← user-এর posts

API Versioning:
/api/v1/users   ← URL versioning (সবচেয়ে সহজ)
Accept: application/vnd.api+json;version=1  ← Header versioning
```

**Tech Lead টিপস:**
- সবসময় HTTPS ব্যবহার করুন
- HTTP/2 enable করুন (Nginx/server config)
- Request/Response logging করুন কিন্তু sensitive data exclude করুন
- Timeout সবসময় set করুন
- Retry Logic implement করুন exponential backoff সহ

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ১৮: WebSocket — রিয়েল-টাইম দ্বিমুখী যোগাযোগ

## ১৮.১ HTTP-এর সমস্যা কোথায়?

HTTP হলো **request-response** — মানে Client চাইলে Server দেয়। কিন্তু Server কি নিজে থেকে কিছু পাঠাতে পারে? না!

```
HTTP দিয়ে Chat App বানানোর চেষ্টা:

Polling (প্রতি ১ সেকেন্ডে জিজ্ঞেস):
Client → "নতুন message আছে?" → Server
Client ← "না" ←
Client → "নতুন message আছে?" → Server
Client ← "না" ←
Client → "নতুন message আছে?" → Server
Client ← "হ্যাঁ, এই message" ←

সমস্যা:
- অপ্রয়োজনীয় network traffic
- Latency বেশি
- Server-এ অনেক load
- Battery drain (mobile-এ)
```

**WebSocket** এই সমস্যা সমাধান করে।

## ১৮.২ WebSocket কিভাবে কাজ করে?

```
WebSocket = একবার সংযোগ, তারপর দুদিক থেকেই কথা

WebSocket Lifecycle:
                                               
Client                         Server
  │                               │
  │ 1. HTTP Upgrade Request       │
  │─────────────────────────────►│
  │   GET /chat HTTP/1.1          │
  │   Upgrade: websocket          │
  │   Connection: Upgrade         │
  │   Sec-WebSocket-Key: xyz==    │
  │                               │
  │ 2. HTTP 101 Switching         │
  │◄─────────────────────────────│
  │   HTTP/1.1 101 Switching      │
  │   Upgrade: websocket          │
  │   Sec-WebSocket-Accept: abc== │
  │                               │
  │ ═══ WebSocket Connected ════  │
  │                               │
  │ 3. Client → Server Message    │
  │──── "হ্যালো!" ───────────────►│
  │                               │
  │ 4. Server → Client Message    │
  │◄─── "কেমন আছেন?" ────────────│
  │                               │
  │ 5. Server → Client (Push!)    │
  │◄─── "নতুন order এলো!" ────────│
  │     (Client না চাইলেও!)       │
  │                               │
  │ 6. Close                      │
  │──── Close Frame ─────────────►│
  │◄─── Close Frame ──────────────│
```

## ১৮.৩ WebSocket vs HTTP Polling তুলনা

```
Performance Comparison (Chat App, 1000 users):

HTTP Polling (প্রতি 1 সেকেন্ড):
Requests/hour = 1000 users × 3600 sec = 3,600,000 requests!
Headers প্রতিটিতে: ~800 bytes
মোট bandwidth: 3,600,000 × 800 = 2.88 GB/hour (শুধু headers!)

WebSocket:
Initial handshake: 1,000 connections
Messages শুধু তখন যখন data আছে
Headers: মাত্র 2-10 bytes per frame
মোট bandwidth: ৯০%+ কম!
```

## ১৮.৪ WebSocket Frame Structure

```
WebSocket Frame:
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
┌─┬─┬─┬─┬───────┬─┬───────────────┬───────────────────────────────┐
│F│R│R│R│ Opcode│M│  Payload Len  │     Extended Payload Length   │
│I│S│S│S│ (4)   │A│   (7 bits)   │            (if needed)        │
│N│V│V│V│       │S│               │                               │
│ │1│2│3│       │K│               │                               │
└─┴─┴─┴─┴───────┴─┴───────────────┴───────────────────────────────┘

Opcodes:
0x0 = Continuation frame
0x1 = Text frame
0x2 = Binary frame
0x8 = Connection Close
0x9 = Ping
0xA = Pong
```

## ১৮.৫ Heartbeat — সংযোগ জীবিত রাখা

```
WebSocket Heartbeat (Ping/Pong):

Client                    Server
  │                         │
  │◄─── Ping ───────────────│  (Server প্রতি 30s পাঠায়)
  │──── Pong ──────────────►│  (Client জবাব দেয়)
  │                         │
  │  [যদি Pong না আসে]      │
  │                         │
  │ Connection dead → Close & Reconnect
```

## ১৮.৬ Server-Sent Events (SSE) — একমুখী Real-time

```
SSE = Server → Client শুধু (একমুখী)
WebSocket = Client ↔ Server (দুমুখী)

SSE কখন ব্যবহার করবেন:
✓ Live news feed
✓ Stock price update
✓ Build/deploy progress
✓ Notification push

WebSocket কখন ব্যবহার করবেন:
✓ Chat application
✓ Multiplayer game
✓ Collaborative editing
✓ Live auction

SSE Request:
GET /events HTTP/1.1
Accept: text/event-stream

SSE Response:
data: {"price": 4500}\n\n
data: {"price": 4510}\n\n
event: alert\ndata: {"msg": "নতুন অর্ডার!"}\n\n
```

## ১৮.৭ Flutter-এ WebSocket

```dart
import 'dart:async';
import 'dart:convert';
import 'package:web_socket_channel/web_socket_channel.dart';

class ChatWebSocketService {
  WebSocketChannel? _channel;
  final _messageController = StreamController<ChatMessage>.broadcast();
  Timer? _heartbeatTimer;
  Timer? _reconnectTimer;
  int _reconnectAttempts = 0;
  static const int _maxReconnectAttempts = 5;
  
  Stream<ChatMessage> get messages => _messageController.stream;
  
  // Connect করি
  Future<void> connect(String userId) async {
    final uri = Uri.parse(
      'wss://api.myapp.com/ws?userId=$userId'
    );
    
    try {
      _channel = WebSocketChannel.connect(uri);
      
      // TLS certificate custom handling
      // wss:// ব্যবহার করলে স্বয়ংক্রিয়ভাবে TLS হয়
      
      _channel!.stream.listen(
        _onMessage,
        onError: _onError,
        onDone: _onDisconnected,
        cancelOnError: false,
      );
      
      _reconnectAttempts = 0;
      _startHeartbeat();
      print('WebSocket connected!');
      
    } catch (e) {
      print('Connection failed: $e');
      _scheduleReconnect(userId);
    }
  }
  
  // Message পাঠানো
  void sendMessage(String text, String roomId) {
    final message = {
      'type': 'message',
      'room': roomId,
      'text': text,
      'timestamp': DateTime.now().toIso8601String(),
    };
    _channel?.sink.add(jsonEncode(message));
  }
  
  // Message পাওয়া
  void _onMessage(dynamic data) {
    final json = jsonDecode(data as String);
    
    switch (json['type']) {
      case 'message':
        _messageController.add(ChatMessage.fromJson(json));
        break;
      case 'pong':
        // Heartbeat response — সংযোগ জীবিত
        break;
      case 'error':
        print('Server error: ${json['message']}');
        break;
    }
  }
  
  // Heartbeat শুরু
  void _startHeartbeat() {
    _heartbeatTimer?.cancel();
    _heartbeatTimer = Timer.periodic(
      const Duration(seconds: 30),
      (_) => _channel?.sink.add('{"type":"ping"}'),
    );
  }
  
  // Disconnect হলে
  void _onDisconnected() {
    _heartbeatTimer?.cancel();
    print('WebSocket disconnected. Reconnecting...');
    _scheduleReconnect('userId'); // userId store করে রাখুন
  }
  
  // Error হলে
  void _onError(dynamic error) {
    print('WebSocket error: $error');
  }
  
  // Exponential Backoff Reconnect
  void _scheduleReconnect(String userId) {
    if (_reconnectAttempts >= _maxReconnectAttempts) {
      print('Max reconnect attempts reached');
      return;
    }
    
    // 1s, 2s, 4s, 8s, 16s — exponential backoff
    final delay = Duration(seconds: (1 << _reconnectAttempts).clamp(1, 30));
    _reconnectAttempts++;
    
    _reconnectTimer?.cancel();
    _reconnectTimer = Timer(delay, () => connect(userId));
    print('Reconnecting in ${delay.inSeconds}s (attempt $_reconnectAttempts)');
  }
  
  // Disconnect করি
  void disconnect() {
    _heartbeatTimer?.cancel();
    _reconnectTimer?.cancel();
    _channel?.sink.close();
    _channel = null;
  }
  
  void dispose() {
    disconnect();
    _messageController.close();
  }
}
```

## ১৮.৮ WebSocket Scaling — বড় সিস্টেমে

```
একটি Server-এ WebSocket Scaling সমস্যা:

User A (Server 1)    User B (Server 2)
     │                    │
     │ Message পাঠাল      │
     ▼                    │
  Server 1 ──────────────?│
  (Server 2 জানে না!)     │

সমাধান: Redis Pub/Sub

User A → Server 1 → Redis Publish → Server 2 → User B

┌──────────────────────────────────────────────┐
│  Load Balancer (Sticky Session ON)           │
│       ↙              ↓              ↘        │
│  Server 1        Server 2        Server 3    │
│    ↕                 ↕                ↕      │
│          Redis Pub/Sub (Shared)              │
└──────────────────────────────────────────────┘

অথবা: Socket.IO with Redis Adapter
```

**Tech Lead টিপস:**
- সবসময় `wss://` (WebSocket Secure) ব্যবহার করুন
- Reconnection logic অবশ্যই implement করুন
- Heartbeat রাখুন, নইলে idle connection কেটে যায়
- Message ordering guarantee করুন যদি দরকার হয়
- Horizontal scaling-এ Redis Pub/Sub অপরিহার্য

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ১৯: gRPC — মডার্ন মাইক্রোসার্ভিস কমিউনিকেশন

## ১৯.১ REST-এর সীমাবদ্ধতা

```
REST-এর সমস্যা:

1. Over-fetching:
GET /user/1
Response: {id, name, email, address, phone, bio, avatar, ...}
(আপনার শুধু name দরকার ছিল!)

2. Under-fetching:
GET /user/1         → user data
GET /user/1/posts   → posts
GET /user/1/friends → friends
(৩টি request লাগল!)

3. No Type Safety:
JSON এ কোনো schema নেই
Client-Server agreement শুধু documentation-এ

4. Performance:
Text-based JSON → বড় payload
HTTP/1.1 সাধারণত → sequential requests
```

## ১৯.২ gRPC কী?

**gRPC** = **g**oogle **R**emote **P**rocedure **C**all

```
gRPC Stack:
┌─────────────────────────────────────┐
│         Your Application            │
├─────────────────────────────────────┤
│    gRPC Framework (Generated Code)  │
├─────────────────────────────────────┤
│    Protocol Buffers (Serialization) │
├─────────────────────────────────────┤
│           HTTP/2                    │
├─────────────────────────────────────┤
│          TLS (Optional)             │
├─────────────────────────────────────┤
│              TCP                    │
└─────────────────────────────────────┘
```

## ১৯.৩ Protocol Buffers (Protobuf) — Schema Definition

```protobuf
// user.proto ফাইল

syntax = "proto3";

package user;

// Message = Data Structure
message User {
  int32 id = 1;          // ফিল্ড নম্বর (১, ২, ৩...)
  string name = 2;
  string email = 3;
  repeated string roles = 4;  // Array
  UserAddress address = 5;    // Nested message
  UserStatus status = 6;      // Enum
}

message UserAddress {
  string city = 1;
  string country = 2;
}

enum UserStatus {
  ACTIVE = 0;
  INACTIVE = 1;
  BANNED = 2;
}

// Service = API endpoints
service UserService {
  // Unary RPC (HTTP GET/POST এর মতো)
  rpc GetUser (GetUserRequest) returns (User);
  rpc CreateUser (CreateUserRequest) returns (User);
  
  // Server Streaming (SSE এর মতো)
  rpc ListUsers (ListUsersRequest) returns (stream User);
  
  // Client Streaming (File upload এর মতো)
  rpc UploadUsers (stream CreateUserRequest) returns (UploadResult);
  
  // Bidirectional Streaming (WebSocket এর মতো)
  rpc Chat (stream ChatMessage) returns (stream ChatMessage);
}

message GetUserRequest {
  int32 id = 1;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
}
```

## ১৯.৪ Protobuf vs JSON — Performance তুলনা

```
একই data: JSON vs Protobuf

JSON (text):
{
  "id": 1,
  "name": "রাহেলা আক্তার",
  "email": "rahela@example.com",
  "status": "ACTIVE"
}
Size: ~85 bytes

Protobuf (binary):
08 01 12 1e e0 a6 b0 e0 a6 be ... (binary)
Size: ~35 bytes (60% ছোট!)

Speed Comparison:
JSON Serialization:   ~1.5 μs
Protobuf Serialize:   ~0.3 μs (5x দ্রুত)

JSON Parse:           ~1.8 μs
Protobuf Parse:       ~0.4 μs (4.5x দ্রুত)
```

## ১৯.৫ ৪ ধরনের gRPC Pattern

```
1. Unary RPC (সবচেয়ে সাধারণ):
Client ──GetUser(id=1)──────────────► Server
Client ◄──User(name="রাহেল")──────── Server

2. Server Streaming:
Client ──ListUsers(filter)──────────► Server
Client ◄──User(1)─────────────────── Server
Client ◄──User(2)─────────────────── Server
Client ◄──User(3)─────────────────── Server
Client ◄──END─────────────────────── Server

3. Client Streaming:
Client ──UserRow(1)─────────────────► Server
Client ──UserRow(2)─────────────────► Server
Client ──UserRow(3)─────────────────► Server
Client ──END────────────────────────► Server
Client ◄──UploadResult(count=3)────── Server

4. Bidirectional Streaming:
Client ──Message("হ্যালো")──────────► Server
Client ◄──Message("কেমন আছেন?")────── Server
Client ──Message("ভালো!")───────────► Server
Client ◄──Message("আমিও ভালো")────── Server
(দুদিক থেকে একই সময়ে!)
```

## ১৯.৬ Flutter-এ gRPC

```dart
// pubspec.yaml
// dependencies:
//   grpc: ^3.2.4
//   protobuf: ^3.1.0

// 1. Proto file থেকে code generate:
// protoc --dart_out=grpc:lib/generated -I. user.proto

// 2. gRPC Client ব্যবহার:
import 'package:grpc/grpc.dart';
import 'generated/user.pbgrpc.dart';

class UserGrpcService {
  late final UserServiceClient _client;
  late final ClientChannel _channel;
  
  UserGrpcService() {
    _channel = ClientChannel(
      'api.myapp.com',
      port: 443,
      options: ChannelOptions(
        credentials: ChannelCredentials.secure(),  // TLS
        codecRegistry: CodecRegistry(codecs: [GzipCodec(), IdentityCodec()]),
      ),
    );
    
    _client = UserServiceClient(
      _channel,
      options: CallOptions(
        timeout: const Duration(seconds: 10),
        metadata: {'authorization': 'Bearer token'},
      ),
    );
  }
  
  // Unary call
  Future<User> getUser(int id) async {
    final request = GetUserRequest()..id = id;
    return await _client.getUser(request);
  }
  
  // Server Streaming
  Stream<User> listUsers() {
    final request = ListUsersRequest();
    return _client.listUsers(request);
  }
  
  // Bidirectional Streaming (Chat)
  void startChat() {
    final requestStream = StreamController<ChatMessage>();
    final responseStream = _client.chat(requestStream.stream);
    
    // Message পাঠান
    requestStream.add(ChatMessage()..text = 'হ্যালো!');
    
    // Message পান
    responseStream.listen(
      (message) => print('Received: ${message.text}'),
      onError: (e) => print('Error: $e'),
    );
  }
  
  Future<void> dispose() async {
    await _channel.shutdown();
  }
}
```

## ১৯.৭ REST vs gRPC vs GraphQL — কোনটি কখন?

```
┌─────────────┬──────────────┬──────────────┬──────────────┐
│  বৈশিষ্ট্য │     REST     │     gRPC     │   GraphQL    │
├─────────────┼──────────────┼──────────────┼──────────────┤
│ Protocol    │ HTTP/1.1+    │ HTTP/2       │ HTTP/1.1+    │
│ Format      │ JSON/XML     │ Protobuf     │ JSON         │
│ Schema      │ OpenAPI      │ .proto file  │ SDL          │
│ Type Safety │ কম           │ সর্বোচ্চ     │ মাঝারি       │
│ Performance │ মাঝারি       │ সর্বোচ্চ     │ মাঝারি       │
│ Browser     │ হ্যাঁ        │ কঠিন        │ হ্যাঁ        │
│ Streaming   │ SSE/WS       │ Native       │ Subscriptions│
│ Learning    │ সহজ          │ মাঝারি       │ মাঝারি       │
└─────────────┴──────────────┴──────────────┴──────────────┘

কখন কী ব্যবহার করবেন:

REST: Public API, Browser client, Simple CRUD
gRPC: Microservice-to-Microservice, High performance, Mobile client
GraphQL: Complex data requirements, Rapid frontend dev, Multiple clients
```

**Tech Lead টিপস:**
- Internal microservices-এ gRPC ব্যবহার করুন — performance অনেক ভালো
- Flutter mobile app-এ gRPC ভালো কাজ করে
- Public API-তে REST রাখুন — সবাই বুঝতে পারে

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---

# অধ্যায় ২০: SMTP, FTP, SSH ও অন্যান্য প্রোটোকল

## ২০.১ SMTP — ইমেইল পাঠানোর প্রোটোকল

```
ইমেইল যাত্রার সম্পূর্ণ ছবি:

আপনি (sender@gmail.com)
        │
        │ SMTP (Port 587/465)
        ▼
  Gmail SMTP Server
  (smtp.gmail.com)
        │
        │ SMTP (Port 25) — server to server
        ▼
  Yahoo Mail Server
  (yahoo.com MX record)
        │
        │ IMAP/POP3
        ▼
  প্রাপক (receiver@yahoo.com)

প্রোটোকল ভূমিকা:
SMTP → পাঠানো (Send)
IMAP → পড়া, server-এ থাকে, sync হয়
POP3 → পড়া, download করে, local-এ থাকে
```

**SMTP Commands:**
```
EHLO myserver.com       ← পরিচয় দাও
AUTH LOGIN              ← Login করতে চাই
334 VXNlcm5hbWU6        ← Username দাও (base64)
334 UGFzc3dvcmQ6        ← Password দাও (base64)
235 Authentication OK   ← Login সফল
MAIL FROM:<me@gmail.com>
RCPT TO:<you@yahoo.com>
DATA
Subject: টেস্ট মেইল
...email body...
.                       ← একটি dot মানে email শেষ
250 OK: Message queued
QUIT
```

**SMTP Ports:**
| Port | ব্যবহার |
|------|---------|
| 25 | Server-to-Server (relay) |
| 587 | Client Submission (STARTTLS) |
| 465 | Client Submission (SSL/TLS) |

## ২০.২ FTP vs SFTP vs SCP

```
FTP (File Transfer Protocol) — Port 21:
❌ No Encryption — username, password, files সব plaintext
❌ Firewall-এ সমস্যা (Passive/Active mode)
⚠️ Legacy system-এ এখনো আছে

SFTP (SSH File Transfer Protocol) — Port 22:
✅ SSH-এর উপর — সম্পূর্ণ এনক্রিপ্টেড
✅ Firewall-বান্ধব (একটি port)
✅ আধুনিক সার্ভারে ব্যবহার করুন

SCP (Secure Copy Protocol) — Port 22:
✅ SSH-এর উপর
✅ Simple copy command
❌ Progress tracking নেই
❌ Resume নেই

FTP Data Transfer Modes:
Active Mode:
Client ─────────────────────────► Server (Command: Port 21)
Client ◄──────────────────────── Server (Data: Client-এর port-এ)
সমস্যা: NAT/Firewall Client-কে পৌঁছাতে দেয় না!

Passive Mode:
Client ─────────────────────────► Server (Command: Port 21)
Client ─────────────────────────► Server (Data: Server-এর high port)
✅ NAT/Firewall-বান্ধব
```

```bash
# SFTP ব্যবহার:
sftp user@server.com
sftp> ls                 # ফাইল তালিকা
sftp> get file.txt       # Download
sftp> put local.txt      # Upload
sftp> mkdir newfolder    # ফোল্ডার তৈরি

# SCP ব্যবহার:
scp file.txt user@server.com:/home/user/  # Upload
scp user@server.com:/file.txt ./          # Download
scp -r folder/ user@server.com:/dest/    # Folder upload
```

## ২০.৩ SSH — নিরাপদ রিমোট অ্যাক্সেস

```
SSH (Secure Shell) — Port 22:

সংযোগ প্রক্রিয়া:
Client                         Server
  │                               │
  │── TCP SYN ───────────────────►│
  │◄─ SYN-ACK ────────────────────│
  │── ACK ────────────────────────►│ (TCP Connected)
  │                               │
  │◄─ Server Public Key ──────────│
  │   "আমি এই server"             │
  │                               │
  │   [Key Fingerprint যাচাই]     │
  │                               │
  │── Session Key Exchange ───────►│ (Diffie-Hellman)
  │◄─ Session Key Confirmed ──────│
  │                               │
  │   [এখন সব কিছু Encrypted]    │
  │                               │
  │── Username + Password ─(enc)─►│  অথবা
  │── Public Key Auth ──── (enc)─►│
  │◄─ Authentication OK ──(enc)──│
  │                               │
  │   [Secure Shell Session]      │
```

**SSH Key-based Authentication (বেশি নিরাপদ):**
```bash
# Step 1: Key pair তৈরি
ssh-keygen -t ed25519 -C "your@email.com"
# এতে তৈরি হয়:
# ~/.ssh/id_ed25519       ← Private Key (কখনো শেয়ার করবেন না!)
# ~/.ssh/id_ed25519.pub   ← Public Key (সার্ভারে দেবেন)

# Step 2: Public key সার্ভারে পাঠান
ssh-copy-id user@server.com
# অথবা manually:
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys

# Step 3: Login (password ছাড়া!)
ssh user@server.com

# SSH Tunneling (Port Forwarding):
# Local: localhost:8080 → Remote: server:80
ssh -L 8080:localhost:80 user@server.com

# Remote: server:9090 → Local: localhost:3000
ssh -R 9090:localhost:3000 user@server.com

# SOCKS Proxy
ssh -D 1080 user@server.com
```

**SSH Config ফাইল (~/.ssh/config):**
```
Host myserver
    HostName 203.0.113.42
    User deploy
    IdentityFile ~/.ssh/id_ed25519
    Port 22
    ServerAliveInterval 60

# ব্যবহার:
ssh myserver   ← পুরো command না লিখেই!
```

## ২০.৪ DHCP — IP Auto-Assignment

```
DHCP (Dynamic Host Configuration Protocol) — Port 67/68:

আপনার ফোন Wi-Fi-তে connect হলে কী হয়?

Phone                          DHCP Server (Router)
  │                                    │
  │── DHCP Discover ─────────────────►│ (Broadcast: "কেউ আছেন?")
  │   [src: 0.0.0.0, dst: 255.255.255.255]
  │                                    │
  │◄─ DHCP Offer ─────────────────────│ ("এই IP নিন: 192.168.1.100")
  │   IP: 192.168.1.100               │
  │   Subnet: 255.255.255.0           │
  │   Gateway: 192.168.1.1            │
  │   DNS: 8.8.8.8                    │
  │   Lease: 24 hours                 │
  │                                    │
  │── DHCP Request ──────────────────►│ ("192.168.1.100 নেব")
  │                                    │
  │◄─ DHCP ACK ───────────────────────│ ("ঠিক আছে, ৮৮৫৮ ঘণ্টা আপনার")
  │                                    │
  │   [এখন IP use করতে পারবেন]       │

DHCP দেয়:
✓ IP Address
✓ Subnet Mask
✓ Default Gateway
✓ DNS Server
✓ Lease Duration (কতক্ষণ IP রাখতে পারবেন)
```

## ২০.৫ SNMP — নেটওয়ার্ক মনিটরিং

```
SNMP (Simple Network Management Protocol) — Port 161/162:

Network monitoring করার জন্য।
Router, Switch, Server-এর স্বাস্থ্য চেক করে।

┌─────────────────────────────────────────────┐
│           SNMP Manager (Monitoring Tool)     │
│           (Grafana, Zabbix, PRTG)            │
└────────────────┬────────────────────────────┘
                 │ SNMP Get/Set (UDP 161)
    ┌────────────┼─────────────────────────┐
    ▼            ▼                         ▼
┌────────┐  ┌────────┐              ┌────────┐
│Router  │  │Switch  │              │Server  │
│(Agent) │  │(Agent) │              │(Agent) │
└────────┘  └────────┘              └────────┘
    │
    │ SNMP Trap (UDP 162)
    │ "আমার CPU 95%!"
    ▼
SNMP Manager (Alert!)

OID (Object Identifier):
1.3.6.1.2.1.2.2.1.10 = Interface Bytes In
1.3.6.1.2.1.2.2.1.16 = Interface Bytes Out
প্রতিটি metric-এর একটি unique OID আছে
```

## ২০.৬ NTP — সময় সিঙ্ক্রোনাইজেশন

```
NTP (Network Time Protocol) — Port 123/UDP:

কেন দরকার?
- Distributed system-এ সব server-এর সময় এক না হলে:
  ✗ Log analysis ভুল হয়
  ✗ Certificate expiry ভুল হয়
  ✗ Database transaction ordering ভুল হয়
  ✗ Authentication token expire হয়

NTP Hierarchy (Stratum):
                    ┌──────────────────┐
     Stratum 0 →   │  Atomic Clock /  │  (GPS, Cesium)
                    │  GPS Receiver    │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
     Stratum 1 →   │  Primary Server  │  (time.google.com)
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
     Stratum 2 →   │ Secondary Server │  (pool.ntp.org)
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
     Stratum 3 →   │  Your Server     │
                    └──────────────────┘

NTP Accuracy:
Stratum 1: ~1 microsecond
Stratum 2: ~1 millisecond
Stratum 3: ~10 milliseconds

Flutter-এ NTP:
```

```dart
// ntp package ব্যবহার
import 'package:ntp/ntp.dart';

Future<void> syncTime() async {
  final ntpTime = await NTP.now();
  final offset = await NTP.getNtpOffset(localTime: DateTime.now());
  print('NTP Time: $ntpTime');
  print('Offset: ${offset}ms');
  // Server time-এর সাথে পার্থক্য জানা যাচ্ছে
}
```

**Tech Lead টিপস:**
- সব সার্ভারে NTP sync রাখুন (chrony বা ntpd)
- SSH-এ Password auth বন্ধ করুন, শুধু Key auth রাখুন
- SSH Port 22 থেকে পরিবর্তন করুন (Security through obscurity)
- SFTP ব্যবহার করুন, FTP নয়

[🔝 উপরে যান](#-মূল-সূচিপত্র-table-of-contents)

---
*PART 6 সম্পন্ন। পরবর্তী: PART 7 — নেটওয়ার্ক নিরাপত্তা*