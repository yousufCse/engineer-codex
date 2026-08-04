# Section 7 — Networking & Local Storage

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** এবং **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা সহ**, আর **link করা** — তাই আপনি এদিক-সেদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-07-networking-storage-bn.md](../software-engineer-flutter/section-07-networking-storage.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার জন্য ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code সহ ধাপে ধাপে বিস্তারিত ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংযুক্ত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর তার কঠিনতা (**Easy / Medium / Hard**)।

> **Interview Tip:** সবসময় আগে **সংক্ষিপ্ত উত্তরটা** দিন (২–৩ বাক্য), তারপর থামুন। Interviewer-কে জিজ্ঞেস করতে দিন "আরও গভীরে যেতে পারেন?" সহজ আর পরিষ্কারভাবে কথা বলা নিজেই একটা senior skill — আর এটা remote আর BD দুই ধরনের কোম্পানিতেই সমানভাবে কাজ করে।

এই section-এ **দুটো এলাকা** আছে: **Networking** (server-এর সাথে কথা বলা) আর **Local Storage** (phone-এ data জমা রাখা)। এই দুটো একসাথে চলে, কারণ ভালো app network থেকে data আনে *এবং* সেটা locally জমা রাখে, যাতে offline-এও কাজ করে।

---

<a id="toc"></a>

## সূচিপত্র

**A. HTTP client আর configuration**
1. [`http` package বনাম Dio](#q1) · *Very common*
2. [Timeout আর retry strategy (connect বনাম receive)](#q2) · *Common*

**B. Auth, interceptor আর error handling**
3. [Dio interceptor — auth token, 401 refresh আর retry queue](#q3) · *Very common*
4. [Global error handling আর `DioException` type](#q4) · *Very common*

**C. API design আর সৎ error modeling**
5. [Mobile-এ REST বনাম GraphQL](#q5) · *Common*
6. [Either / Result pattern](#q6) · *Common*

**D. JSON আর data parsing**
7. [JSON parsing — `json_serializable` আর `freezed`](#q7) · *Very common*

**E. Security আর offline resilience**
8. [Certificate pinning](#q8) · *Deeper*
9. [Internet না থাকলে কী করবেন](#q9) · *Common*

**F. Local storage-এর বিকল্পগুলো**
10. [SharedPreferences — কী, thread-safety, সীমা](#q10) · *Very common*
11. [Hive — box আর TypeAdapter](#q11) · *Common*
12. [SQLite / Drift — relational data](#q12) · *Common*

**G. Secure storage আর encryption**
13. [flutter_secure_storage — ভেতরে কী হয়](#q13) · *Very common*
14. [Local data encrypt করা](#q14) · *Deeper*

**H. Offline-first আর syncing**
15. [Offline-first architecture](#q15) · *Common*
16. [Local data-কে server-এর সাথে sync রাখা](#q16) · *Deeper*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---

<a id="study-plan"></a>

## ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

১৬টা প্রশ্ন একসাথে পড়ার দরকার নেই। এই পর্যায়গুলো ক্রম অনুযায়ী অনুসরণ করুন — প্রতিটা আগেরটার উপর দাঁড়িয়ে আছে। একটা পর্যায় তখনই শেষ ধরুন, যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন।

**পর্যায় ১ — মূল networking (এখান থেকেই শুরু করুন)।** এগুলো প্রায় প্রতিটা interview-এ আসে।
→ [Q1 http বনাম Dio](#q1) · [Q3 Interceptor আর token refresh](#q3) · [Q4 Error handling](#q4) · [Q7 JSON parsing](#q7)

**পর্যায় ২ — মূল local storage।** Phone-এ data কোথায় রাখবেন।
→ [Q10 SharedPreferences](#q10) · [Q11 Hive](#q11) · [Q12 SQLite/Drift](#q12) · [Q13 Secure storage](#q13)

**পর্যায় ৩ — পরিষ্কার design আর মজবুতি।** একজন senior কীভাবে code সাজায়।
→ [Q2 Timeout আর retry](#q2) · [Q6 Either/Result](#q6) · [Q9 Internet নেই](#q9)

**পর্যায় ৪ — গভীরতা আর senior signal।**
→ [Q5 REST বনাম GraphQL](#q5) · [Q14 Local data encrypt করা](#q14) · [Q15 Offline-first](#q15)

**পর্যায় ৫ — গভীর tie-breaker (সবার শেষে করুন)।** এগুলোই শক্ত senior-দের বাকিদের থেকে আলাদা করে।
→ [Q8 Certificate pinning](#q8) · [Q16 Sync strategy](#q16)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** শুধু এই আটটা দেখে নিন:
[Q1](#q1) · [Q3](#q3) · [Q4](#q4) · [Q7](#q7) · [Q10](#q10) · [Q11](#q11) · [Q12](#q12) · [Q13](#q13), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. HTTP client আর configuration

---

<a id="q1"></a>
## 1. `http` package আর Dio-র মধ্যে পার্থক্য কী? Production-এ সাধারণত Dio কেন বেছে নেওয়া হয়?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`http` package হলো Dart-এর সাধারণ, হালকা client — সহজ GET বা POST-এর জন্য দারুণ। Dio হলো সেই একই ধারণার উপর তৈরি একটা পূর্ণাঙ্গ client, যার সাথে আছে interceptor, request cancellation, timeout, upload/download progress, আর সহজ retry। বাস্তব app-এ Dio যেগুলো এমনিতেই দিয়ে দেয় — যেমন এক জায়গায় auth আর logging — ঠিক সেগুলোই না হলে আমাকে হাতে বানাতে হতো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুই ধরনের delivery service ভাবুন।**
`http` package হলো নিজে পার্সেল পাঠানোর মতো: আপনি ঠিকানা লেখেন, stamp লাগান, আর প্রতিবার নিজেই খোঁজ নেন। Dio হলো একটা নিয়ম-মাফিক courier কোম্পানির মতো: নিয়মগুলো একবার ঠিক করে দেন (address book, tracking, ব্যর্থ হলে retry), আর প্রতিটা পার্সেল নিজে থেকেই সেই নিয়ম মেনে চলে।

**ধাপ ২ — `http` আপনাকে যা যা হাতে করতে বাধ্য করে।**
`http`-এ প্রতিটা call-এ একই setup বারবার লিখতে হয়। status code check আর JSON parse-ও আপনাকেই করতে হয়।

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

final response = await http.get(
  Uri.parse('https://api.example.com/users'),
  headers: {
    'Authorization': 'Bearer $token',   // প্রতিটা call-এ বারবার
    'Content-Type': 'application/json',
  },
);

if (response.statusCode == 200) {
  final data = jsonDecode(response.body); // JSON নিজেই parse করুন
} else {
  // error নিজেই handle করুন, প্রতিবার
}
```

**ধাপ ৩ — Dio যা দেয়: একবার configure করুন, সব জায়গায় ব্যবহার করুন।**
Base URL, timeout আর header একবারই `BaseOptions`-এ বসিয়ে দেন। Response body আগে থেকেই parse করা থাকে।

```dart
import 'package:dio/dio.dart';

final dio = Dio(BaseOptions(
  baseUrl: 'https://api.example.com',
  connectTimeout: const Duration(seconds: 10),
  receiveTimeout: const Duration(seconds: 15),
  headers: {'Content-Type': 'application/json'},
));

final response = await dio.get('/users');
// response.data আগে থেকেই JSON থেকে parse করা — jsonDecode লাগে না
```

**ধাপ ৪ — আসল পার্থক্য হলো feature-এর তালিকা।**
সবচেয়ে বড় লাভ হলো *interceptor* ([Q3](#q3) দেখুন): auth, logging আর retry-র মতো cross-cutting কাজ এক জায়গায় থাকে, প্রতিটা API call-এ copy-paste করতে হয় না।

| Feature | `http` | Dio |
|---|---|---|
| Interceptor (request/response/error) | না | হ্যাঁ |
| Request cancel করা | না | হ্যাঁ (`CancelToken`) |
| Timeout config | সীমিত | প্রতি request-এ আর global |
| Upload / download progress | না | হ্যাঁ (`onSendProgress` / `onReceiveProgress`) |
| FormData / multipart | হাতে | Built-in |
| Retry logic | হাতে | Interceptor দিয়ে সহজ |
| Base URL আর default header | হাতে | Built-in (`BaseOptions`) |
| Auto JSON parsing | হাতে | Built-in |

**ধাপ ৫ — কখন `http` এখনো ঠিক আছে।**
ছোট app, script, বা যে package বড় dependency চায় না — সেখানে `http` একদম ভালো। Auth, retry বা অনেক endpoint থাকলে তখনই Dio-র জায়গা তৈরি হয়।

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা জানতে চান আপনি বাস্তব app বানিয়েছেন কি না। যিনি production-এ token refresh, upload progress বা request cancellation সামলেছেন, তিনি জানেন `http`-এর মতো পাতলা wrapper একা যথেষ্ট নয়।

**সাধারণ ভুল:** "Dio ভালো কারণ এটা বেশি popular" — এটা বলা। এটা কোনো technical উত্তর নয়। Interceptor, cancellation, timeout আর progress নিয়ে কথা বলুন — এগুলোই আসল architectural সুবিধা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Dio-তে কি request cancel করা যায়?"* → হ্যাঁ — একটা `CancelToken` পাঠান আর `token.cancel()` call করুন (user load-এর মাঝপথে screen ছেড়ে গেলে কাজে লাগে)।
- *"`http` কি কখনো সঠিক পছন্দ হয়?"* → হ্যাঁ, খুব ছোট app বা কম-dependency package-এ, যেখানে Dio-র বাড়তি জিনিস লাগে না।

**সম্পর্কিত:** [Q2 — timeout আর retry](#q2) · [Q3 — interceptor](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q2"></a>
## 2. Timeout আর retry strategy কীভাবে ঠিক করেন? Connect timeout আর receive timeout-এর মধ্যে পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Connect timeout মানে server-এর সাথে connection *খুলতে* আমি কতক্ষণ অপেক্ষা করব। Receive timeout মানে connection খোলার পরে server-এর *data পাঠানোর* জন্য আমি কতক্ষণ অপেক্ষা করব। এই দুটো আলাদা ধরনের ব্যর্থতা থেকে বাঁচায়। Retry-র বেলায় আমি শুধু timeout আর 5xx server error-এ retry করি, 4xx-এ কখনোই না। আর exponential backoff ব্যবহার করি, যাতে কষ্টে থাকা server-কে আরও চাপ না দিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ফোন কলের একটা তুলনা।**
- **Connect timeout** = ফোন কতক্ষণ বাজতে দেবেন, তারপর ছেড়ে দেবেন। ১০ সেকেন্ডে কেউ না ধরলে server সম্ভবত down।
- **Receive timeout** = ধরার পরে তারা আসলে কথা বলার জন্য আপনি কতক্ষণ অপেক্ষা করবেন। তারা ধরেছে, কিন্তু চুপ — কিছুক্ষণ পরে ছেড়ে দিন।
- **Send timeout** = আপনার নিজের কথা শেষ করতে (request body upload করতে) কতক্ষণ সময় নিতে পারবেন। বড় file upload-এ এটা সবচেয়ে গুরুত্বপূর্ণ।

**ধাপ ২ — timeline-এ কোনটা কোথায় বসে।**

```
  |-- connectTimeout --|                       |-- receiveTimeout --|
  |                    |                       |                    |
  DNS > TCP handshake > TLS > Send request > Server thinks > Response
       \- connection -/                    \--- receiving data ----/
        opened here                          first byte to last byte

  sendTimeout covers: |- time to upload the request body -|
```

**ধাপ ৩ — যুক্তিসঙ্গত মান বেছে নিন।**
- *Connect timeout:* ছোট (5–10s)। দ্রুত ব্যর্থ হওয়া ভালো; এখানে retry করাটা যুক্তিসঙ্গত।
- *Receive timeout:* API-র আসল গতির সাথে মিলিয়ে নিন। একটা search-এ 15s লাগতে পারে; বড় download-এ 60s লাগতে পারে।
- *Send timeout:* বড় upload-এর জন্য উদার রাখুন।

```dart
final dio = Dio(BaseOptions(
  baseUrl: 'https://api.example.com',
  connectTimeout: const Duration(seconds: 8),
  receiveTimeout: const Duration(seconds: 15),
  sendTimeout: const Duration(seconds: 15),
));

// ধীর endpoint-এর জন্য প্রতি request-এ override করুন
final report = await dio.get(
  '/reports/generate',
  options: Options(receiveTimeout: const Duration(seconds: 60)),
);
```

**ধাপ ৪ — exponential backoff সহ একটা retry interceptor।**
"Exponential backoff" মানে প্রতিটা retry আগেরটার চেয়ে বেশি সময় অপেক্ষা করে (1s, তারপর 2s, তারপর 4s)। এতে ব্যস্ত server বন্যার বদলে সামলে ওঠার সুযোগ পায়।

```dart
import 'dart:math';

class RetryInterceptor extends Interceptor {
  final Dio dio;
  final int maxRetries;
  RetryInterceptor({required this.dio, this.maxRetries = 3});

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    if (_shouldRetry(err)) {
      final count = (err.requestOptions.extra['retryCount'] as int?) ?? 0;
      if (count < maxRetries) {
        // 1s, 2s, 4s — প্রতিবার বেশি সময় অপেক্ষা
        final delay = Duration(milliseconds: 1000 * pow(2, count).toInt());
        await Future.delayed(delay);

        err.requestOptions.extra['retryCount'] = count + 1;
        try {
          final response = await dio.fetch(err.requestOptions);
          handler.resolve(response); // সফল — এখানেই থামুন
          return;
        } catch (_) {
          // নিচের handler.next-এ চলে যাবে
        }
      }
    }
    handler.next(err); // হাল ছেড়ে দিন, error পরে পাঠিয়ে দিন
  }

  bool _shouldRetry(DioException err) {
    return err.type == DioExceptionType.connectionTimeout ||
        err.type == DioExceptionType.receiveTimeout ||
        err.type == DioExceptionType.connectionError ||
        (err.response?.statusCode ?? 0) >= 500; // 5xx server error
  }
}
```

**ধাপ ৫ — retry-র সোনালি নিয়ম।**
- Timeout আর 5xx-এ retry করুন (দোষ server-এর — সে সামলে উঠতে পারে)।
- 4xx-এ কখনোই retry করবেন না (আপনার request-ই ভুল; আবার পাঠালেও লাভ নেই)।
- সবসময় backoff ব্যবহার করুন, আর retry-র সংখ্যায় সীমা দিন।

**Interviewer কেন জিজ্ঞেস করে:** এতে বোঝা যায় আপনি network lifecycle বোঝেন আর trade-off নিতে পারেন। Backoff ছাড়া আক্রমণাত্মক retry outage-এর সময় ভুল করে নিজের server-কেই DDoS করে ফেলতে পারে।

**সাধারণ ভুল:** প্রতিটা ধরন আলাদা করে tune না করে একটাই বড় timeout (সবকিছুতে 60s) বসিয়ে দেওয়া। আর 400 বা 422-তে retry করা — এগুলো নির্দিষ্ট client error, আবার করলেও ব্যর্থই হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fixed delay নয়, exponential backoff কেন?"* → হাজার হাজার client একসাথে একই ছোট fixed delay দিলে server down-ই থেকে যায়। Backoff চাপটা ছড়িয়ে দেয়।
- *"আপনি কি jitter যোগ করবেন?"* → হ্যাঁ — backoff-এর উপর একটু random delay দিলে সব client ঠিক একই মুহূর্তে retry করে না (এটাই "thundering herd")।

**সম্পর্কিত:** [Q1 — http বনাম Dio](#q1) · [Q4 — error handling](#q4) · [Q3 — interceptor](#q3)

[↑ উপরে ফিরুন](#toc)

---

# B. Auth, interceptors ও error handling

---

<a id="q3"></a>
## 3. Dio interceptor কীভাবে কাজ করে? auth token কীভাবে inject করবেন, আর 401 এলে token refresh ও retry queue কীভাবে সামলাবেন?

> Very common · Medium–Hard — networking নিয়ে ক্লাসিক বাস্তব প্রশ্ন। · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Interceptor প্রতিটা request-এর মাঝখানে বসে থাকে, বিমানবন্দরের security-র মতো: প্রতিটা request যায় `onRequest` দিয়ে, প্রতিটা response যায় `onResponse` দিয়ে, প্রতিটা error যায় `onError` দিয়ে। আমি auth token যোগ করি `onRequest`-এ। 401 এলে আমি token *একবারই* refresh করি, তারপর নতুন token দিয়ে ব্যর্থ request-গুলো আবার পাঠাই। মূল কথা হলো `QueuedInterceptor` ব্যবহার করা, যাতে তিনটা 401 একসাথে তিনটা refresh শুরু না করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বিমানবন্দরের security-র উপমা।**
প্রতিটা যাত্রীকে (request) বোর্ডিং-এর আগে একটা security checkpoint (interceptor) পার হতে হয়। Checkpoint তাদের pass-এ সিল দিতে পারে (token যোগ), ফেরত পাঠাতে পারে (reject), বা পাশে সরিয়ে রাখতে পারে (retry)। সবাই একই checkpoint দিয়ে যায় বলে নিয়মটা একবার লিখলেই হয়, প্রতিটা gate-এ নয়।

**ধাপ ২ — তিনটা hook।**

```dart
class MyInterceptor extends Interceptor {
  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    // প্রতিটা request app থেকে বের হওয়ার আগে চলে
    handler.next(options); // চলতে দিন
  }

  @override
  void onResponse(Response response, ResponseInterceptorHandler handler) {
    // প্রতিটা সফল response-এর জন্য চলে
    handler.next(response);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    // প্রতিটা error-এর জন্য চলে
    handler.next(err);
  }
}
```

শেষটা সবসময় তিনটা কাজের একটা দিয়ে হয়: `handler.next(...)` (চলতে দিন), `handler.resolve(response)` (আগেভাগেই সফল), অথবা `handler.reject(err)` (ব্যর্থ)।

**ধাপ ৩ — auth token যোগ করা (সহজ অংশ)।**

```dart
@override
void onRequest(RequestOptions options, RequestInterceptorHandler handler) async {
  final token = await _tokenStorage.getAccessToken();
  if (token != null) {
    options.headers['Authorization'] = 'Bearer $token';
  }
  handler.next(options);
}
```

**ধাপ ৪ — কঠিন অংশ: 401 আর "একবারই refresh" সমস্যা।**
Token-এর মেয়াদ শেষ হয়। Server উত্তর দেয় **401 Unauthorized**। আপনাকে নতুন token নিয়ে আবার চেষ্টা করতে হবে। কিন্তু ভাবুন তিনটা request একসাথে গেল আর সবগুলোই 401 পেল। প্রতিটা যদি আলাদা করে token refresh করে, তাহলে তিনটা refresh চলবে — এটা একটা race condition, যেটা একে অন্যের token নষ্ট করে দিতে পারে।

আপনি যে ছবিটা চান:

```
  Request → onRequest (attach token) → Server
                                          |
                                     401 Unauthorized
                                          |
                                   onError fires
                                          |
                            Is a refresh already running?
                             |                    |
                            YES                   NO
                             |                    |
                      wait in the queue     lock + refresh once
                             |                    |
                             |               get new token
                             |                    |
                             +→ retry all with the new token
```

**ধাপ ৫ — সমাধান: `QueuedInterceptor`।**
`QueuedInterceptor` তার error handling **একটা একটা করে** চালায়। তাই তিনটা 401 এলে শুধু প্রথমটাই refresh শুরু করে। বাকি দুটো নিজের পালার জন্য অপেক্ষা করে আর নতুন token-টাই ব্যবহার করে।

```dart
class AuthInterceptor extends QueuedInterceptor {
  final Dio _dio;
  final TokenStorage _tokenStorage;
  AuthInterceptor(this._dio, this._tokenStorage);

  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) async {
    final token = await _tokenStorage.getAccessToken();
    if (token != null) {
      options.headers['Authorization'] = 'Bearer $token';
    }
    handler.next(options);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    if (err.response?.statusCode == 401) {
      try {
        // এটা QueuedInterceptor বলে একসাথে মাত্র একটা refresh চলে।
        final newToken = await _refreshToken();
        await _tokenStorage.saveAccessToken(newToken);

        // নতুন token দিয়ে মূল request আবার পাঠান
        final options = err.requestOptions;
        options.headers['Authorization'] = 'Bearer $newToken';
        final response = await _dio.fetch(options);
        handler.resolve(response); // সফল — caller 401 দেখেই না
      } catch (_) {
        await _tokenStorage.clear(); // refresh ব্যর্থ → জোর করে logout
        handler.reject(err);
      }
    } else {
      handler.next(err); // 401 নয় — পরেরটার কাছে পাঠান
    }
  }

  Future<String> _refreshToken() async {
    final refreshToken = await _tokenStorage.getRefreshToken();
    // গুরুত্বপূর্ণ: আলাদা Dio, কোনো auth interceptor ছাড়া — নইলে অসীম loop
    final freshDio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));
    final res = await freshDio.post('/auth/refresh', data: {
      'refresh_token': refreshToken,
    });
    return res.data['access_token'] as String;
  }
}

// Registration — order গুরুত্বপূর্ণ: আগে auth, পরে logging
final dio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));
dio.interceptors.add(AuthInterceptor(dio, tokenStorage));
dio.interceptors.add(LogInterceptor()); // auth token যোগ করার পরে চলে
```

**ধাপ ৬ — দুটো ছোট বিষয়, যেগুলো বাস্তবে bug তৈরি করে।**
- `QueuedInterceptor` ব্যবহার করুন, সাধারণ `Interceptor` নয়। নইলে multi-refresh race হবে।
- Refresh call-এর জন্য **আলাদা** Dio instance ব্যবহার করুন। মূল `dio` আবার ব্যবহার করলে refresh request-ও `AuthInterceptor` দিয়ে যাবে। আর *সেটা* যদি 401 দেয়, তাহলে অসীম loop হবে।

**Interviewer কেন জিজ্ঞেস করে:** retry queue সহ token refresh বাস্তব জীবনের সবচেয়ে সাধারণ চ্যালেঞ্জগুলোর একটা। তাঁরা দেখতে চান আপনি এটা সঠিকভাবে বানাবেন, নাকি race condition ঢুকিয়ে দেবেন।

**সাধারণ ভুল:** সাধারণ `Interceptor` ব্যবহার করা (multi-refresh race), অথবা refresh call-এর জন্য একই Dio instance ব্যবহার করা (অসীম loop)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"refresh token নিজেই যদি expire হয়ে যায়?"* → refresh call ব্যর্থ হবে, আপনি storage clear করবেন আর user-কে আবার log in করতে বাধ্য করবেন।
- *"Token কোথায় রাখেন?"* → `flutter_secure_storage`-এ, কখনোই SharedPreferences-এ নয় ([Q13](#q13) দেখুন)।

**সম্পর্কিত:** [Q4 — error handling](#q4) · [Q13 — token-এর জন্য secure storage](#q13) · [Q2 — retry](#q2)

[↑ উপরে ফিরুন](#toc)

---

<a id="q4"></a>
## 4. Dio-তে global error handling কীভাবে করেন? `DioException`-এর type-গুলো কী কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Global error handling মানে প্রতিটা network error এক জায়গায় ধরা — একটা interceptor-এ। ফলে প্রতিটা API call-এ একই try/catch বারবার লিখতে হয় না। Dio সব ব্যর্থতাকে `DioException`-এ মুড়ে দেয়, আর তার `type` field আমাকে ঠিক বলে দেয় কী ভুল হয়েছে: timeout, connection নেই, খারাপ response, cancel — এরকম। আমি প্রতিটা type-কে একটা পরিষ্কার, typed app error-এ map করি, যেটা দেখে UI প্রতিক্রিয়া দিতে পারে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কেন error এক জায়গায় আনবেন।**
কেন্দ্রীয় জায়গা না থাকলে প্রতিটা screen নিজের try/catch আর নিজের "কিছু একটা ভুল হয়েছে" message লেখে। এটা বারবার একই কাজ, আর অসামঞ্জস্যপূর্ণ। একটা interceptor পুরো app-এর জন্য কাঁচা network error-কে পরিষ্কার app error-এ বদলে দেয়।

**ধাপ ২ — `DioException`-এর type-গুলো (এগুলো মুখস্থ রাখুন)।**

```
connectionTimeout  → could not open the connection in time
sendTimeout        → uploading the request body took too long
receiveTimeout     → server took too long to respond
badCertificate     → SSL/TLS certificate check failed
badResponse        → server replied with an error status (4xx / 5xx)
cancel             → request was cancelled (CancelToken)
connectionError    → no connection at all (DNS failure, no internet)
unknown            → anything else (e.g. a parsing error)
```

**ধাপ ৩ — প্রতিটা type-কে একটা typed app failure-এ map করুন।**
Failure-এর জন্য Dart 3-এর `sealed` class ব্যবহার করুন, যাতে UI প্রতিটা ক্ষেত্র সামলাতে পারে ([Q6](#q6) আর Section 1-এর sealed class প্রশ্নটা দেখুন)।

```dart
class GlobalErrorInterceptor extends Interceptor {
  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    final failure = _mapToFailure(err);
    // typed failure যুক্ত করুন, যেন উপরের layer পরিষ্কার error পায়
    handler.next(err.copyWith(error: failure));
  }

  AppFailure _mapToFailure(DioException err) {
    switch (err.type) {
      case DioExceptionType.connectionTimeout:
      case DioExceptionType.sendTimeout:
      case DioExceptionType.receiveTimeout:
        return AppFailure.timeout('Server is taking too long. Try again.');
      case DioExceptionType.connectionError:
        return AppFailure.noConnection('No internet connection.');
      case DioExceptionType.badResponse:
        return _handleBadResponse(err.response!);
      case DioExceptionType.badCertificate:
        return AppFailure.security('Secure connection failed.');
      case DioExceptionType.cancel:
        return AppFailure.cancelled('Request was cancelled.');
      case DioExceptionType.unknown:
        return AppFailure.unexpected('Something went wrong: ${err.message}');
    }
  }

  AppFailure _handleBadResponse(Response response) {
    return switch (response.statusCode) {
      400 => AppFailure.badRequest(response.data['message'] ?? 'Invalid request'),
      401 => AppFailure.unauthorized('Session expired.'),
      403 => AppFailure.forbidden('Access denied.'),
      404 => AppFailure.notFound('Not found.'),
      422 => AppFailure.validation(response.data['errors']),
      429 => AppFailure.rateLimited('Too many requests.'),
      final code when code != null && code >= 500 =>
        AppFailure.server('Server error. Try again later.'),
      _ => AppFailure.unexpected('Error: ${response.statusCode}'),
    };
  }
}

// একটাই typed error model, পুরো app যেটা বোঝে
sealed class AppFailure {
  final String message;
  const AppFailure(this.message);

  factory AppFailure.timeout(String m) = TimeoutFailure;
  factory AppFailure.noConnection(String m) = NoConnectionFailure;
  factory AppFailure.server(String m) = ServerFailure;
  factory AppFailure.unauthorized(String m) = UnauthorizedFailure;
  factory AppFailure.forbidden(String m) = ForbiddenFailure;
  factory AppFailure.notFound(String m) = NotFoundFailure;
  factory AppFailure.badRequest(String m) = BadRequestFailure;
  factory AppFailure.validation(dynamic errors) = ValidationFailure;
  factory AppFailure.rateLimited(String m) = RateLimitedFailure;
  factory AppFailure.security(String m) = SecurityFailure;
  factory AppFailure.cancelled(String m) = CancelledFailure;
  factory AppFailure.unexpected(String m) = UnexpectedFailure;
}

class TimeoutFailure extends AppFailure { const TimeoutFailure(super.m); }
class NoConnectionFailure extends AppFailure { const NoConnectionFailure(super.m); }
// ...এবং উপরের প্রতিটা factory-র জন্য একটা করে ছোট subclass
```

**ধাপ ৪ — UI-তে এর ফায়দা।**
Failure typed বলে screen সেটার উপর switch করতে পারে। ফলে সঠিক message আর সঠিক কাজ দেখানো যায় (retry, offline banner, বা log out)। কোনো কাঁচা status code widget-এ ঢোকে না।

**Interviewer কেন জিজ্ঞেস করে:** এতে বোঝা যায় আপনি সব জায়গায় try/catch ছড়িয়ে দেন না। তাঁরা একটা কেন্দ্রীয়, typed error model চান, যেটার উপর UI pattern-match করতে পারে।

**সাধারণ ভুল:** প্রতিটা `DioException`-কে একটাই সাধারণ "network error" ধরে নেওয়া। প্রতিটা type-এর জন্য আলাদা message আর আলাদা recovery দরকার: timeout-এ retry, `connectionError`-এ offline banner, 401-এ জোর করে logout।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"401 বনাম 403?"* → 401 = log in করা নেই / token-এর মেয়াদ শেষ (refresh করুন বা log in করুন)। 403 = log in করা আছে কিন্তু অনুমতি নেই (retry করবেন না)।
- *"Message কোথায় দেখান?"* → UI layer typed failure পড়ে সিদ্ধান্ত নেয়। Network layer কখনো widget ছোঁয় না।

**সম্পর্কিত:** [Q3 — interceptor ও 401](#q3) · [Q6 — Either/Result](#q6) · [Q9 — offline handling](#q9)

[↑ উপরে ফিরুন](#toc)

---

# C. API design ও সৎ error modeling

---

<a id="q5"></a>
## 5. REST আর GraphQL-এর পার্থক্য কী? Mobile-এ trade-off কী কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"REST আপনাকে অনেকগুলো নির্দিষ্ট endpoint দেয়, প্রতিটা একটা নির্দিষ্ট আকারের data ফেরত দেয়। GraphQL দেয় একটাই endpoint, যেখানে client ঠিক যে field দরকার সেটাই চায়। GraphQL over-fetching এড়ায় আর round trip কমায়, যেটা ধীর mobile network-এ দারুণ। কিন্তু এর caching কঠিন, আর এটা সবসময় 200 ফেরত দেয়, তাই error handling বেশি জটিল। আমি hype দেখে নয়, app দেখে বেছে নিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা restaurant-এর উপমা।**
- **REST** হলো নির্দিষ্ট menu-র restaurant: প্রতিটা খাবার (endpoint) ঠিক যেমন লেখা আছে তেমনই আসে। শুধু ভাত চাইলেও পুরো plate-টাই পাবেন।
- **GraphQL** হলো নিজের bowl নিজে বানানোর দোকান: আপনি ঠিক কোন উপকরণ (field) চান সেটা বলে দেন, আর তারা শুধু সেটাই হাতে দেয়।

**ধাপ ২ — আকারের পার্থক্যটা দেখুন।**

```
REST: many endpoints, fixed responses

  GET /users/42           → { id, name, email, avatar, bio, ... }
  GET /users/42/posts     → [{ id, title, body, createdAt, ... }]
  GET /users/42/followers → [{ id, name, avatar, ... }]
  → 3 round trips, many unused fields on mobile

GraphQL: one endpoint, you choose the fields

  POST /graphql
  query {
    user(id: 42) {
      name
      avatar
      posts(first: 5) { title }
      followersCount
    }
  }
  → 1 round trip, only the fields the screen needs
```

**ধাপ ৩ — Mobile-এ যে trade-off গুলো আসলেই গুরুত্বপূর্ণ।**
- **Over-fetching / under-fetching:** REST নির্দিষ্ট payload ফেরত দেয় (প্রায়ই দরকারের চেয়ে বেশি)। GraphQL ঠিক যা চান তাই ফেরত দেয় — ধীর connection-এ এটা গুরুত্বপূর্ণ।
- **Round trips:** একটা screen-এ প্রায়ই কয়েকটা resource-এর data লাগে। REST = কয়েকটা call (বা একটা custom BFF endpoint)। GraphQL = একটাই query।
- **Caching:** REST URL দিয়ে সহজেই cache হয় (HTTP caching)। GraphQL-এ এটা কঠিন — সবকিছুই একটা URL-এ POST, তাই একটা normalized cache লাগে (`graphql_flutter` বা `ferry`)।
- **File uploads:** REST multipart নিজে থেকেই সামলায়। GraphQL-এ multipart spec লাগে, বা আলাদা একটা REST endpoint।
- **Error handling:** REST HTTP status code ব্যবহার করে। GraphQL প্রায় সবসময় 200 ফেরত দেয় আর error body-র ভেতরে রাখে, তাই global error interceptor-কে ([Q4](#q4) দেখুন) response-এর ভেতরে খুঁজে দেখতে হয়।
- **Tooling in Flutter:** REST + Dio পরিণত আর সহজ। GraphQL-এ `graphql_flutter` বা `ferry` লাগে — বেশি setup আর code generation, কিন্তু শক্ত type safety।

**ধাপ ৪ — পাশাপাশি code।**

```dart
// Dio দিয়ে REST: সম্পর্কিত data-র জন্য দ্বিতীয় call
final user = UserModel.fromJson((await dio.get('/users/42')).data);
final posts = (await dio.get('/users/42/posts')).data; // বাড়তি round trip

// graphql_flutter দিয়ে GraphQL: এক call, ঠিক যতটুকু দরকার
const q = r'''
  query GetProfile($id: ID!) {
    user(id: $id) { name avatar posts(first: 5) { title createdAt } }
  }
''';
final result = await client.query(
  QueryOptions(document: gql(q), variables: {'id': '42'}),
);
```

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি hype দেখে নয়, trade-off দেখে tool বাছেন কি না। অনেক mobile app-এর জন্য পুরো GraphQL-এর চেয়ে REST আর একটা পাতলা BFF (backend-for-frontend) বেশি ভালো কাজ করে।

**সাধারণ ভুল:** GraphQL over-fetching ঠিক করে বলে সেটাকে "সবসময় ভালো" বলা। সহজ CRUD app-এ এর caching জটিলতা, error-এর খুঁতখুঁতে আচরণ আর বড় query payload সুবিধার চেয়ে ভারী হয়ে যেতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"BFF কী?"* → আপনার app-এর জন্য বানানো ছোট একটা backend, যেটা কয়েকটা call একসাথে বেঁধে একটা করে দেয় — GraphQL-এর জটিলতা ছাড়াই REST-কে "প্রতি screen-এ এক call"-এর কাছাকাছি নিয়ে আসে।
- *"Flutter-এ GraphQL caching কীভাবে কাজ করে?"* → একটা normalized cache object-গুলো ID দিয়ে জমা রাখে, ফলে একই object সব query-তে ভাগাভাগি হয়; `ferry` আর `graphql_flutter` এটা দেয়।

**সম্পর্কিত:** [Q4 — error handling](#q4) · [Q7 — JSON parsing](#q7)

[↑ উপরে ফিরুন](#toc)

---

<a id="q6"></a>
## 6. Either / Result pattern কী? Layer-এর মাঝে exception ছোড়ার চেয়ে এটা কেন ভালো?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Either (বা Result) একটা function-এর return type-কে সৎ করে তোলে: এটা বলে 'এটা data ফেরত দেয় অথবা একটা failure।' এমন exception ছোড়ার বদলে যেটা caller ধরতে ভুলে যেতে পারে, আমি একটা value ফেরত দিই যেটা caller-কে দুটো ক্ষেত্রই সামলাতে বাধ্য করে। আমি exception রাখি boundary-তে — network আর database layer-এ। তার উপরের সব জায়গায় typed return value ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Exception-এর "লুকানো ফাঁদ" সমস্যা।**
`Future<User> getUser()` এমন একটা signature *দেখে মনে হয়* এটা সবসময় একটা `User` ফেরত দেয়। কিন্তু এটা চুপচাপ পাঁচ রকম exception ছুড়তে পারে। Caller type দেখে সেটা বুঝতে পারে না, আর ধরতে ভুলেও যেতে পারে — একটা লুকানো ফাঁদ।

```
Exception approach (hidden failure path):
  Future<User> getUser()   -- says "returns User"
                           -- but can throw several exceptions
                           -- caller may not handle any of them

Either approach (honest contract):
  Future<Either<Failure, User>> getUser()
                           -- says "returns Failure OR User"
                           -- caller MUST handle both
                           -- no hidden control flow
```

**ধাপ ২ — Dart 3 sealed class দিয়ে একটা সহজ Either।**
`Left` failure বহন করে, `Right` success বহন করে (নিয়মটা হলো "right মানে right/সঠিক")।

```dart
sealed class Either<L, R> {
  const Either();
}
class Left<L, R> extends Either<L, R> {
  final L value;
  const Left(this.value);
}
class Right<L, R> extends Either<L, R> {
  final R value;
  const Right(this.value);
}

// দুটো দিক একসাথে সামলানোর helper
extension EitherX<L, R> on Either<L, R> {
  T fold<T>(T Function(L) onLeft, T Function(R) onRight) => switch (this) {
        Left(:final value) => onLeft(value),
        Right(:final value) => onRight(value),
      };
}
```

**ধাপ ৩ — Repository-তে এটা ব্যবহার করুন (boundary-তে exception ধরুন)।**

```dart
class UserRepository {
  final Dio _dio;
  UserRepository(this._dio);

  Future<Either<AppFailure, User>> getUser(String id) async {
    try {
      final response = await _dio.get('/users/$id');
      return Right(User.fromJson(response.data)); // সফল
    } on DioException catch (e) {
      return Left(_mapError(e));                   // প্রত্যাশিত failure
    } catch (e) {
      return Left(AppFailure.unexpected(e.toString()));
    }
  }

  AppFailure _mapError(DioException e) =>
      e.type == DioExceptionType.connectionError
          ? AppFailure.noConnection('No internet')
          : AppFailure.server('Server error');
}
```

**ধাপ ৪ — Caller failure-টা উপেক্ষা করতে পারে না।**

```dart
class UserCubit extends Cubit<UserState> {
  final UserRepository _repo;
  UserCubit(this._repo) : super(UserInitial());

  Future<void> loadUser(String id) async {
    emit(UserLoading());
    final result = await _repo.getUser(id);
    result.fold(
      (failure) => emit(UserError(failure.message)), // সামলাতেই হবে
      (user) => emit(UserLoaded(user)),
    );
    // এখানে try/catch নেই — failure একটা VALUE, হঠাৎ ছোড়া throw নয়
  }
}
```

**ধাপ ৫ — কখন ব্যবহার করবেন (আর কখন নয়)।**
সত্যিই ব্যতিক্রমী আর অপ্রত্যাশিত জিনিসের জন্য exception রাখুন, আর boundary layer-এর জন্যও তাই। *প্রত্যাশিত* ফলাফলের জন্য Either ব্যবহার করুন, যেমন "user not found" বা "no internet"। ছোট ছোট internal helper function-কে Either-এ মুড়বেন না — ওখানে সাধারণ throw-ই ঠিক আছে।

**ধাপ ৬ — Production-এ পরীক্ষিত package ব্যবহার করুন।**
বেশিরভাগ team নিজে হাতে বানানোর বদলে `fpdart` (বা পুরোনো `dartz`) ব্যবহার করে। এতে পরীক্ষিত `Either` পাওয়া যায়, সাথে `map` আর `flatMap`-এর মতো helper।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি API boundary ইচ্ছে করে design করেন — অপ্রত্যাশিতের জন্য exception, প্রত্যাশিত failure-এর জন্য typed value। এটাই clean-architecture-এর চিন্তা।

**সাধারণ ভুল:** `Either` ব্যবহার করা, কিন্তু শুধু success দিকটা সামলানো আর failure দিকটা উপেক্ষা করা। আরেকটা ভুল — *সবকিছু* Either-এ মুড়ে ফেলা, এমনকি যেখানে সাধারণ throw বেশি পরিষ্কার।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Failure-এর জন্য `Left` কেন?"* → এটা functional programming-এর একটা নিয়ম মাত্র: `Right` মানে "right/সঠিক" value, `Left` হলো অন্য ক্ষেত্রটা।
- *"Sealed Result-এর সাথে পার্থক্য কী?"* → ধারণায় কোনো পার্থক্য নেই। `sealed Result { Success, Failure }` একই জিনিস, শুধু নামগুলো বেশি বন্ধুত্বপূর্ণ; Either হলো generic version।

**সম্পর্কিত:** [Q4 — typed failures](#q4) · [Q5 — REST error shapes](#q5)

[↑ উপরে ফিরুন](#toc)

---

# D. JSON আর data parsing

---

<a id="q7"></a>
## 7. Flutter-এ JSON কীভাবে parse করেন? manual parsing, `json_serializable`, আর `freezed`-এর তুলনা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"JSON আসে `Map<String, dynamic>` হিসেবে। আমি সেটাকে একটা typed Dart object-এ বদলে নিই, যাতে app-এর বাকি অংশ নিরাপদ থাকে। এক-দুইটা ছোট model-এর জন্য আমি `fromJson`/`toJson` হাতে লিখি। আসল project-এ আমি `json_serializable` দিয়ে ওই code generate করাই। আর immutability, `copyWith` আর value equality-ও চাইলে `freezed` ব্যবহার করি। হাতে লেখা parsing-এর ভেতরেই চুপচাপ bug লুকিয়ে থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Parse করার দরকার কেন? (একটা অনুবাদকের উদাহরণ।)**
Server থেকে আসা JSON হলো বিদেশি ভাষায় লেখা একটা চিঠির মতো: এটা শুধু text আর আলগা key-value জোড়া। Parsing মানে একজন অনুবাদক নিয়োগ করা, যে এটাকে একটা ঠিকঠাক Dart object বানিয়ে দেয় — নাম আর type সহ field নিয়ে। ফলে compiler আপনার code check করতে পারে, আর autocomplete কাজ করে।

**ধাপ ২ — Manual parsing (ছোট model-এর জন্য ঠিক আছে)।**
দুইটা method আপনি নিজেই লেখেন।

```dart
class User {
  final String id;
  final String name;
  final String? email; // ইচ্ছে করেই nullable
  const User({required this.id, required this.name, this.email});

  factory User.fromJson(Map<String, dynamic> json) => User(
        id: json['id'] as String,
        name: json['name'] as String,
        email: json['email'] as String?,
      );

  Map<String, dynamic> toJson() => {'id': id, 'name': name, 'email': email};
}
```

এটা কাজ করে। কিন্তু 20টা field-এর একটা model-এর জন্য এটা লম্বা আর ভুল হওয়া সহজ (key-তে একটা typo, বা null safety ভুলে যাওয়া — runtime-এ crash করবে)।

**ধাপ ৩ — `json_serializable` (একঘেয়ে code generate করান)।**
আপনি class-এ annotation দেন, আর build tool `fromJson`/`toJson` লিখে দেয়। `dart run build_runner build` চালান।

```dart
import 'package:json_annotation/json_annotation.dart';
part 'user.g.dart'; // generate করা file

@JsonSerializable()
class User {
  final String id;
  final String name;

  @JsonKey(name: 'email_address') // server-এর আলাদা key name map করা
  final String? email;

  const User({required this.id, required this.name, this.email});

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}
```

`@JsonKey` snake_case server key, default value আর custom converter সামলায় — হাতে map করার ভুল আর থাকে না।

**ধাপ ৪ — `freezed` (immutability + equality + copyWith, সবই generate করা)।**
`freezed` একই ধারণার উপর দাঁড়ানো। কিন্তু এটা একটা immutable class, value-ভিত্তিক `==`/`hashCode`, আর একটা `copyWith`-ও generate করে। State object-এর জন্য এটা আদর্শ (BLoC/Riverpod-এর সাথে দারুণ মেলে, equality নিয়ে Section 1 দেখুন)।

```dart
import 'package:freezed_annotation/freezed_annotation.dart';
part 'user.freezed.dart';
part 'user.g.dart';

@freezed
class User with _$User {
  const factory User({
    required String id,
    required String name,
    String? email,
  }) = _User;

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
}

// এই সবগুলো আপনি এমনিতেই পেয়ে যান:
final a = User(id: '1', name: 'Sara');
final b = a.copyWith(name: 'Sara Khan'); // immutable update
print(a == User(id: '1', name: 'Sara'));  // true (value equality)
```

**ধাপ ৫ — Nested object আর list সামলানো।**
Interview-এ একটা সাধারণ খুঁটিনাটি: object-এর একটা list-কে map করতে হয়, শুধু cast করলে হয় না।

```dart
// যে field-টা অন্য model-এর একটা list:
final tags = (json['tags'] as List<dynamic>)
    .map((e) => Tag.fromJson(e as Map<String, dynamic>))
    .toList();
```

`json_serializable` / `freezed` ব্যবহার করলে এই nested parsing আপনার জন্য নিজে থেকেই generate হয়ে যায়।

**ধাপ ৬ — দ্রুত তুলনা।**

| | Manual | `json_serializable` | `freezed` |
|---|---|---|---|
| Boilerplate | সবটা আপনি লেখেন | generate করা | generate করা |
| Immutability | শুধু `final` যোগ করলে | আপনার উপর | হ্যাঁ, ভেতরেই আছে |
| `==` / `hashCode` | হাতে | হাতে | generate করা |
| `copyWith` | হাতে | না | generate করা |
| কার জন্য ভালো | 1–2টা ছোট model | বেশিরভাগ DTO / API model | state ও domain model |

**Interviewer কেন জিজ্ঞেস করে:** তাঁরা দেখতে চান আপনি বড় model-এর জন্য ভঙ্গুর parsing হাতে লেখেন না। আর আপনি জানেন `freezed` immutability আর value equality দেয় (যা state management-এর rebuild-এর জন্য গুরুত্বপূর্ণ)।

**সাধারণ ভুল:** প্রতিটা item `fromJson` দিয়ে map না করে পুরো list-কে `as List<User>` দিয়ে cast করা। আর annotation দেওয়া model বদলানোর পরে `build_runner` চালাতে ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`json_serializable` বনাম `freezed` — কোনটা কখন?"* → শুধু parsing দরকার হলে `json_serializable`। immutability, `copyWith` আর equality-ও চাইলে `freezed` (state/domain model)।
- *"Server থেকে যে field `int` বা `String` দুইই হতে পারে, সেটা কীভাবে সামলাবেন?"* → একটা custom `JsonConverter`, অথবা `fromJson`-এ সেটাকে normalize করা।

**সম্পর্কিত:** [Q4 — typed error](#q4) · [Q5 — GraphQL type](#q5)

[↑ উপরে ফিরুন](#toc)

---

# E. Security আর offline resilience

---

<a id="q8"></a>
## 8. Certificate pinning কী, এটা কেন গুরুত্বপূর্ণ, আর Flutter-এ এটা কীভাবে করবেন?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Certificate pinning মানে আমার app শুধু *আমার* server-এর নির্দিষ্ট certificate বা public key-কে বিশ্বাস করে — কোনো trusted authority-র sign করা যেকোনো certificate-কে নয়। এটা man-in-the-middle আক্রমণ থামায়, যেখানে rogue authority certificate আছে এমন কেউ আমার HTTPS traffic মাঝপথে ধরে ফেলে। নিরাপদ ধরনটা হলো public key pin করা, কারণ certificate renew হলেও সেটা টিকে থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ID-card-এর উদাহরণ।**
সাধারণ HTTPS হলো এমন একজন guard, যে যেকোনো সরকারি office-এর দেওয়া যেকোনো ID card মেনে নেয়। Pinning হলো এমন একজন guard, যার কাছে *আপনার* ঠিক ID-র ছবি আছে, আর সে শুধু ওই একটাকেই ঢুকতে দেয়। নকল কিন্তু সরকারিভাবে sign করা ID সাধারণ guard-কে পার হয়ে যায়। কিন্তু ছবির সামনে সেটা ধরা পড়ে।

**ধাপ ২ — সাধারণ HTTPS কী check করে (আর ফাঁকটা কোথায়)।**

```
Normal HTTPS (trusts any valid CA):
  App → TLS handshake → server shows a certificate
                              |
                         Signed by ANY trusted CA?
                              |
                             YES → accepted
                             (an attacker with a rogue CA cert ALSO passes)

With certificate pinning:
  App → TLS handshake → server shows a certificate
                              |
                         Does its key match the PIN baked into the app?
                              |
                             YES → accepted
                             NO  → REJECTED  (rogue cert is blocked)
```

**ধাপ ৩ — Pinning-এর দুইটা ধরন।**
- **Certificate pinning:** পুরো certificate pin করা। সহজ, কিন্তু cert rotate হওয়ার প্রতিবার আপনাকে app update ship করতে হবে।
- **Public key pinning:** শুধু public key pin করা। Renew হলেও key সাধারণত একই থাকে। তাই cert rotate হলেও app চলতে থাকে। **এটাই পছন্দের।**

**ধাপ ৪ — Dio দিয়ে Dart-level একটা উপায়।**
Server certificate-এর fingerprint আপনার hardcoded pin-এর সাথে মিলিয়ে দেখেন।

```dart
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:dio/io.dart';

Dio createPinnedDio() {
  final dio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));

  (dio.httpClientAdapter as IOHttpClientAdapter).createHttpClient = () {
    final client = HttpClient();
    client.badCertificateCallback = (X509Certificate cert, String host, int port) {
      const pinnedSha256 = 'A1:B2:C3:D4:...'; // আপনার cert/key-এর SHA-256 fingerprint
      final serverSha256 = cert.sha256Fingerprint; // (helper / হিসাব করা value)
      return serverSha256 == pinnedSha256; // true = accept, false = reject
    };
    return client;
  };
  return dio;
}
```

**ধাপ ৫ — Team-রা কেন প্রায়ই native code-এ pin করে।**
Dart-এর `SecurityContext` সীমিত (বিশেষ করে public key বের করার ক্ষেত্রে)। তাই অনেক production app native layer-এ pin করে — Android-এ `OkHttp`-এর `CertificatePinner`, আর iOS-এ একটা `URLSession` delegate — method channel দিয়ে সেখানে পৌঁছায়। `http_certificate_pinning`-এর মতো package-ও এটা wrap করে দেয়।

**ধাপ ৬ — সবসময় একটা backup pin রাখুন।**
**দুইটা** key pin করুন: চালু থাকা key আর একটা backup। জরুরি অবস্থায় key rotate করা লাগলে backup pin app-কে চালু রাখে, যতক্ষণ না user-রা update করেন।

**Interviewer কেন জিজ্ঞেস করে:** আপনার security সচেতনতা মাপতে। টাকা, স্বাস্থ্য বা auth token নিয়ে কাজ করা app-এর pin করা উচিত। এটা দেখায় আপনি "HTTPS-ই যথেষ্ট"-এর বাইরে ভাবেন।

**সাধারণ ভুল:** public key-এর বদলে leaf certificate pin করা। Cert rotate হলে (Let's Encrypt-এ প্রতি 90 দিনে) app ভেঙে যায়, যদি না আপনি একটা update ship করেন। Public key pin করুন, আর একটা backup pin রাখুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"HTTPS তো আগেই MITM থামায়, তাই না?"* → শুধু তখনই, যখন প্রতিটা trusted CA সৎ আর অক্ষত থাকে। Pinning আপনার নিজের server-এর জন্য ওই "সবাইকে বিশ্বাস করো" ধারণাটা সরিয়ে দেয়।
- *"Pinning-এর ঝুঁকি?"* → Cert বদলানোর আগে নতুন pin ship করতে ভুলে গেলে আপনি সব user-কে আটকে দিতে পারেন। এই কারণেই একটা backup pin আর একটা rotation পরিকল্পনা রাখবেন।

**সম্পর্কিত:** [Q4 — badCertificate error](#q4) · [Q13 — secure storage](#q13)

[↑ উপরে ফিরুন](#toc)

---

<a id="q9"></a>
## 9. Internet connection না থাকলে কীভাবে সুন্দরভাবে সামলান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি এটা layer-এ ভাগ করে সামলাই: connectivity detect করি, user-কে জানাই কিন্তু আটকাই না, আর সম্ভব হলে cache করা data দেখাই। একটা মূল কথা — `connectivity_plus` শুধু *connection type* (wifi/mobile) জানায়, internet সত্যিই কাজ করছে কি না তা নয়। তাই এটা বদলানোর পরে আমি একটা ছোট আসল lookup দিয়ে confirm করি, তারপর ঠিক করি আমি online কি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটি layer।**

```
  UI layer       → offline banner, disable/enable actions, show cached data
       |  (reads state from)
  State layer    → a ConnectivityCubit watching a connectivity stream
       |  (driven by)
  Network layer  → a Dio interceptor that falls back to cache on failure
```

**ধাপ ২ — Connectivity detect করুন, তারপর যাচাই করুন এটা আসল কি না।**
ফাঁদটা হলো: wifi-তে থাকা মানেই internet কাজ করছে না। airport-এর wifi login page-এর কথা ভাবুন। তাই একটা ছোট DNS lookup দিয়ে confirm করুন।

```dart
class ConnectivityCubit extends Cubit<ConnectivityStatus> {
  late final StreamSubscription _sub;

  ConnectivityCubit() : super(ConnectivityStatus.online) {
    _sub = Connectivity().onConnectivityChanged.listen((_) async {
      // connectivity_plus INTERFACE (wifi/mobile) জানায়, আসল internet নয়।
      final hasInternet = await _reallyOnline();
      emit(hasInternet ? ConnectivityStatus.online : ConnectivityStatus.offline);
    });
  }

  Future<bool> _reallyOnline() async {
    try {
      final r = await InternetAddress.lookup('example.com')
          .timeout(const Duration(seconds: 3));
      return r.isNotEmpty && r.first.rawAddress.isNotEmpty;
    } catch (_) {
      return false;
    }
  }

  @override
  Future<void> close() {
    _sub.cancel();
    return super.close();
  }
}
```

**ধাপ ৩ — Network layer: call ব্যর্থ হলে cache থেকে দিন।**
"কাছের তাক বনাম দূরের গুদাম" — cache হলো কাছের তাক। গুদামে (server-এ) পৌঁছানো না গেলে fail না করে তাক থেকেই জিনিসটা নিন।

```dart
class OfflineCacheInterceptor extends Interceptor {
  final LocalCacheSource _cache;
  OfflineCacheInterceptor(this._cache);

  @override
  void onResponse(Response response, ResponseInterceptorHandler handler) {
    if (response.requestOptions.method == 'GET') {
      _cache.put(response.requestOptions.uri.toString(), response.data); // তাক ভরে রাখা
    }
    handler.next(response);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    final isGet = err.requestOptions.method == 'GET';
    if (err.type == DioExceptionType.connectionError && isGet) {
      final cached = _cache.get(err.requestOptions.uri.toString());
      if (cached != null) {
        // error না ছুঁড়ে তাক থেকেই দিন
        handler.resolve(Response(
          requestOptions: err.requestOptions,
          data: cached,
          statusCode: 200,
          statusMessage: 'FROM_CACHE',
        ));
        return;
      }
    }
    handler.next(err);
  }
}
```

**ধাপ ৪ — UI layer: পরিষ্কার একটা banner, যা কাজ আটকায় না।**

```dart
BlocBuilder<ConnectivityCubit, ConnectivityStatus>(
  builder: (context, status) => Column(
    children: [
      if (status == ConnectivityStatus.offline)
        const MaterialBanner(
          content: Text('You are offline. Showing cached data.'),
          actions: [SizedBox.shrink()],
          backgroundColor: Colors.orange,
        ),
      const Expanded(child: MainContent()),
    ],
  ),
);
```

**Interviewer কেন জিজ্ঞেস করে:** Mobile app-এর connectivity *যাবেই*। তাঁরা দেখতে চান আপনি সেটা ভেবেই design করেছেন — শুধু error ধরেননি, বরং একটা কম-সুবিধার অভিজ্ঞতা দিয়েছেন যা এখনও কাজ করে।

**সাধারণ ভুল:** "আমি online কি না" জানতে শুধু `connectivity_plus`-এর উপর ভরসা করা। এটা শুধু interface-এর ধরন জানায়। আপনি wifi-তে থেকেও আসল internet না পেতে পারেন — সবসময় DNS lookup বা ping দিয়ে confirm করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Response-গুলো কীভাবে cache করেন?"* → Hive, অথবা URL দিয়ে key করা একটা সাধারণ map। কিংবা `dio_cache_interceptor` ব্যবহার করুন, যেটা আপনার হয়ে HTTP-style caching করে।
- *"Offline থাকা অবস্থায় write হলে?"* → সেগুলো locally queue করুন, আর online ফিরলে sync করুন — এটাই offline-first (দেখুন [Q15](#q15))।

**সম্পর্কিত:** [Q4 — connectionError](#q4) · [Q15 — offline-first](#q15) · [Q11 — Hive cache](#q11)

[↑ উপরে ফিরুন](#toc)

---

# F. Local storage-এর বিকল্পগুলো

---

<a id="q10"></a>
## 10. `SharedPreferences` কী জমা রাখে? এটা কি thread-safe, আর এর সীমা কী কী?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"SharedPreferences হলো সাধারণ setting রাখার জন্য একটা ছোট key-value store — iOS-এ `NSUserDefaults` আর Android-এ একটা XML file এর পেছনে থাকে। এটা শুধু primitive রাখে: `String`, `int`, `double`, `bool`, আর `List<String>`। এক isolate-এর ভেতরে এটা নিরাপদ, কোনো encryption নেই, পুরো file memory-তে load করে, আর এটা database নয়। তাই এটা setting-এর জন্য, বড় বা sensitive data-র জন্য নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটাকে sticky note ভাবুন, filing cabinet নয়।**
SharedPreferences ছোট নোটের জন্য: "onboarding done = true," "language = en।" হাজার হাজার record রাখার জায়গা এটা নয় — তার জন্য আসল database লাগে (দেখুন [Q11](#q11), [Q12](#q12))।

**ধাপ ২ — এটা কী রাখে আর কোথায় রাখে।**

```
  Dart code
     |
  SharedPreferences plugin
     |→ iOS:     NSUserDefaults (a plist file)
     |→ Android: SharedPreferences (XML in /data/data/<pkg>/shared_prefs/)
```

শুধু এই type-গুলো: `String`, `int`, `double`, `bool`, `List<String>`। কোনো map নয়, কোনো custom object নয়।

**ধাপ ৩ — সাধারণ ব্যবহার।**

```dart
final prefs = await SharedPreferences.getInstance();

// লেখা
await prefs.setString('locale', 'en');
await prefs.setBool('onboarding_complete', true);
await prefs.setInt('launch_count', 5);

// পড়া (সবসময় একটা default দিন)
final locale = prefs.getString('locale') ?? 'en';
final onboarded = prefs.getBool('onboarding_complete') ?? false;

// মুছে ফেলা
await prefs.remove('locale');
```

**ধাপ ৪ — Thread safety।**
`getInstance()`-এ plugin পুরো file memory-তে পড়ে নেয়; write disk-এ যায় asynchronously। একটা isolate-এর ভেতরে এটা নিরাপদ। একাধিক isolate-এ, বা native code একই file লিখলে, race condition হতে পারে।

**ধাপ ৫ — যে সীমাগুলো মুখে বলবেন।**
কোনো encryption নেই (disk-এ plain text), শুধু primitive, পুরো file memory-তে load হয় (বড় হলে খারাপ), কোনো query নেই, বড় dataset-এর জন্য বানানো নয়। এটা setting store, database নয়।

```dart
// জটিল object রাখা মানে হাতে serialize করা — এখানে এটা একটা code smell:
await prefs.setString('cached_user', jsonEncode(user.toJson()));
// আসল object বা list-এর জন্য বরং Hive বা SQLite/Drift ব্যবহার করুন।
```

**Interviewer কেন জিজ্ঞেস করে:** নিশ্চিত হতে যে আপনি জানেন SharedPreferences *কীসের জন্য* — ছোট, সাধারণ setting — আর আপনি এতে 10,000 product রাখবেন না।

**সাধারণ ভুল:** Sensitive data (token, password) SharedPreferences-এ রাখা — এটা plain text। `flutter_secure_storage` ব্যবহার করুন (দেখুন [Q13](#q13))। আরেকটা ভুল — Hive বা SQLite ব্যবহার না করে এতে বড় JSON serialize করে রাখা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Token কোথায় রাখবেন?"* → এখানে কখনোই না। `flutter_secure_storage` ব্যবহার করুন ([Q13](#q13))।
- *"Object-এর list হলে?"* → Hive ([Q11](#q11)) বা Drift ([Q12](#q12)) ব্যবহার করুন; SharedPreferences শুধু `List<String>` রাখে।

**সম্পর্কিত:** [Q11 — Hive](#q11) · [Q12 — SQLite/Drift](#q12) · [Q13 — secure storage](#q13)

[↑ উপরে ফিরুন](#toc)

---

<a id="q11"></a>
## 11. Hive কী? Box আর TypeAdapter কী, আর কখন SharedPreferences-এর বদলে Hive বেছে নেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Hive হলো দ্রুত, pure-Dart একটা NoSQL key-value database। এটা দ্রুত কারণ এতে কোনো platform channel নেই আর data binary-তে রাখে। TypeAdapter দিয়ে এটা custom object সামলায়। একটা *box* হলো table-এর মতো — key-value জোড়ার একটা নাম দেওয়া container। একটা *TypeAdapter* Hive-কে বলে দেয় আমার object কীভাবে binary-তে যাবে আর ফিরে আসবে। Custom object, encryption, বা হাতে গোনার চেয়ে বেশি value লাগলে আমি SharedPreferences-এর বদলে Hive নিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এক নজরে Hive বনাম SharedPreferences।**

```
  Feature           SharedPreferences      Hive
  ----------------  --------------------   --------------------
  Data types        primitives only        any (via adapters)
  Speed             slower (XML parse)      fast (binary)
  Encryption        no                      yes (AES-256)
  Platform channels yes                     no (pure Dart)
  Lazy loading      no (loads all)          yes (LazyBox)
  Custom objects    JSON workaround         native support
  Best for          simple settings         structured cache
```

**ধাপ ২ — একটা box = একটা ড্রয়ার।**
Box হলো key-value জোড়ার নাম দেওয়া একটা ড্রয়ার। আপনি এটা open করেন, read/write করেন, আর app-এর পুরো জীবন এটা খোলা থাকে। Box encrypt করা যায়।

**ধাপ ৩ — একটা TypeAdapter = আপনার object-এর অনুবাদক।**
Hive binary রাখে, তাই তার জানা দরকার আপনার `Task`-কে কীভাবে byte-এ নেবে আর ফেরত আনবে। `hive_generator` সেই adapter আপনার হয়ে লিখে দেয়।

```dart
import 'package:hive/hive.dart';
part 'task.g.dart'; // generate করা

@HiveType(typeId: 0) // প্রতি type-এ আলাদা unique ID — একই number কখনোই আবার ব্যবহার করবেন না
class Task extends HiveObject {
  @HiveField(0)
  late String title;

  @HiveField(1)
  late bool completed;

  @HiveField(2) // নতুন field পাবে নতুন index; পুরোনোগুলো কখনোই বদলাবেন না
  late DateTime createdAt;
}
```

**ধাপ ৪ — Adapter register করুন, তারপর box খুলুন।**

```dart
void main() async {
  await Hive.initFlutter();
  Hive.registerAdapter(TaskAdapter()); // generate করা adapter; box খোলার আগে
  await Hive.openBox<Task>('tasks');
  runApp(const MyApp());
}
```

**ধাপ ৫ — CRUD (create, read, update, delete)।**

```dart
final box = Hive.box<Task>('tasks');

// তৈরি করা
final task = Task()
  ..title = 'Buy groceries'
  ..completed = false
  ..createdAt = DateTime.now();
await box.add(task); // auto-increment হওয়া int key

// পড়া
final all = box.values.toList();
final first = box.getAt(0);

// আপডেট (HiveObject .save() দেয়)
task.completed = true;
await task.save();

// মুছে ফেলা
await task.delete();
```

**ধাপ ৬ — Encrypted box (key নিরাপদে রাখুন)।**

```dart
final key = Hive.generateSecureKey();          // 32টি random byte
// গুরুত্বপূর্ণ: এই key flutter_secure_storage-এ রাখুন, code-এ নয় (দেখুন Q13/Q14)
await Hive.openBox<Task>(
  'secure_tasks',
  encryptionCipher: HiveAesCipher(key),
);
```

**ধাপ ৭ — কখন SharedPreferences-এর বদলে Hive বেছে নেবেন।**
Custom object লাগলে, encryption লাগলে, ~20টির বেশি value হলে, বড় dataset-এ lazy loading (`LazyBox`) লাগলে, অথবা platform-channel-এর বাড়তি খরচ এড়াতে চাইলে।

**Interviewer কেন জিজ্ঞেস করে:** দেখতে যে আপনি প্রয়োজন দেখে storage বাছেন। "সাধারণ setting" (SharedPreferences) আর "relational data" (SQLite/Drift) — এই দুইয়ের মাঝের ফাঁকটা Hive পূরণ করে।

**সাধারণ ভুল:** অন্য একটা class-এর জন্য পুরোনো `typeId` আবার ব্যবহার করা, বা release-এর পরে `@HiveField` index বদলানো — দুটোই জমা data নষ্ট করে। আরেকটা ভুল — typed box খোলার আগে `Hive.registerAdapter(...)` ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Box বনাম LazyBox?"* → একটা `Box` সব value memory-তে রাখে; একটা `LazyBox` প্রতিটা value disk থেকে পড়ে শুধু পড়ার সময়ে — বড় data-র জন্য ভালো।
- *"Hive বনাম Isar?"* → Isar একই লেখকের নতুন database, এতে query আর index আছে; এটা বললে বোঝা যায় আপনি হালনাগাদ আছেন। (Hive এখনও ব্যাপকভাবে ব্যবহার হয় আর key-value-র জন্য সবচেয়ে সহজ।)

**সম্পর্কিত:** [Q10 — SharedPreferences](#q10) · [Q12 — SQLite/Drift](#q12) · [Q14 — encryption](#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q12"></a>
## 12. SQLite / Drift কখন দরকার হয়, আর Drift-এ basic query কীভাবে লেখেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি relational database ধরি তখন, যখন data-র মধ্যে সম্পর্ক থাকে (users → posts → comments), জটিল query লাগে (join, grouping, search), বা transaction লাগে। Key-value store দক্ষভাবে উত্তর দিতে পারে না — 'গত 7 দিনের সব order, status অনুযায়ী grouped'। Drift হলো একটা reactive, type-safe SQLite wrapper: আমি table-গুলো Dart class হিসেবে define করি, আর ও query API, data class আর migration generate করে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা decision tree।**

```
  Need to store data?
       |
  Simple key-value (settings, flags)?      → SharedPreferences (Q10)
       |
  Structured objects, moderate size,
  no real relationships?                   → Hive (Q11)
       |
  Relationships, joins, complex queries,
  transactions?                            → SQLite / Drift (this question)
```

**ধাপ ২ — সহজ ভাষায় relational কেন।**
একটা spreadsheet ভাবুন, যার sheet-গুলো একে অন্যের সাথে যুক্ত: "posts"-এ একটা `authorId` আছে, যেটা "users"-এর দিকে দেখায়। Relational database দুটোকে join করে একটাই query-তে দুই দিকের প্রশ্নের উত্তর দিতে পারে — key-value store এটা দক্ষভাবে পারে না।

**ধাপ ৩ — Table-গুলো Dart class হিসেবে define করুন।**

```dart
import 'package:drift/drift.dart';
part 'database.g.dart'; // generated

class Users extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get name => text().withLength(min: 1, max: 100)();
  TextColumn get email => text().unique()();
  DateTimeColumn get createdAt => dateTime().withDefault(currentDateAndTime)();
}

class Posts extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get title => text()();
  IntColumn get authorId => integer().references(Users, #id)(); // foreign key
  BoolColumn get published => boolean().withDefault(const Constant(false))();
}
```

**ধাপ ৪ — Database class আর type-safe query।**

```dart
@DriftDatabase(tables: [Users, Posts])
class AppDatabase extends _$AppDatabase {
  AppDatabase(QueryExecutor e) : super(e);

  @override
  int get schemaVersion => 1;

  Future<List<User>> getAllUsers() => select(users).get();

  Future<User> getUserById(int id) =>
      (select(users)..where((u) => u.id.equals(id))).getSingle();

  // Reactive: table বদলালেই নতুন list আপনাআপনি emit হয়
  Stream<List<User>> watchAllUsers() => select(users).watch();

  Future<int> insertUser(UsersCompanion user) => into(users).insert(user);
}
```

**ধাপ ৫ — একটা join (post-এর সাথে তার author-এর নাম)।**

```dart
Future<List<({Post post, String authorName})>> getPostsWithAuthors() {
  final query = select(posts).join([
    innerJoin(users, users.id.equalsExp(posts.authorId)),
  ]);
  return query.map((row) => (
    post: row.readTable(posts),
    authorName: row.readTable(users).name,
  )).get();
}
```

**ধাপ ৬ — একটা transaction (সব, নয়তো কিছুই না)।**
Transaction মানে কয়েকটা write একসাথে সফল হবে, নয়তো একটাও হবে না। ফলে অর্ধেক save হয়ে থাকার অবস্থা কখনো আসে না।

```dart
Future<void> createUserWithPost(String name, String email, String title) {
  return transaction(() async {
    final userId = await into(users)
        .insert(UsersCompanion.insert(name: name, email: email));
    await into(posts)
        .insert(PostsCompanion.insert(title: title, authorId: userId));
  });
}
```

**ধাপ ৭ — Migration ভুলবেন না।**
Schema বদলালে (একটা column যোগ করলে) `schemaVersion` বাড়ান আর একটা `MigrationStrategy` লিখুন। নাহলে পুরোনো database নিয়ে থাকা user-দের app crash করবে।

**Interviewer কেন জিজ্ঞেস করে:** দেখতে চান আপনি সঠিক সময়ে SQLite ধরেন কি না — key-value store-কে জোর করে relational কাজে লাগাচ্ছেন না, আবার সাধারণ settings-এর জন্য database ব্যবহার করছেন না।

**সাধারণ ভুল:** Drift-এর type-safe API-র বদলে raw SQL string লেখা (compile-time check হারিয়ে যায়)। অথবা migration বাদ দেওয়া, আর schema বদলের সময় পুরোনো user-দের local data নষ্ট করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Drift বনাম `sqflite`?"* → `sqflite` হলো raw SQLite plugin (আপনি নিজে SQL string লেখেন)। Drift তার উপরে একটা typed, reactive layer — generated code আর `watch()` stream সহ।
- *"`watch()` আপনাকে কী দেয়?"* → একটা `Stream`, যা নিচের data বদলালেই আবার emit করে — এমন UI-র জন্য দারুণ, যেটা আপনাআপনি update হয় (offline-first-এর ভিত্তি, [Q15](#q15))।

**সম্পর্কিত:** [Q11 — Hive](#q11) · [Q15 — offline-first](#q15) · [Q14 — SQLCipher](#q14)

[↑ উপরে ফিরুন](#toc)

---

# G. Secure storage আর encryption

---

<a id="q13"></a>
## 13. `flutter_secure_storage` ভেতরে কী ব্যবহার করে, আর কখন এটা ব্যবহার করা উচিত?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`flutter_secure_storage` হলো encrypted key-value storage। iOS-এ এটা Keychain ব্যবহার করে। Android-এ Keystore দিয়ে একটা AES key বানায়, আর সেই key দিয়ে EncryptedSharedPreferences-এ value encrypt করে। আমি এটা secret-এর জন্য ব্যবহার করি — auth token, refresh token, API key, আর Hive-এর encryption key। বড় বা বারবার পড়া লাগে এমন data-র জন্য আমি এটা ব্যবহার করি *না*, কারণ encryption-এর জন্য এটা সাধারণ SharedPreferences-এর চেয়ে ধীর।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটাকে একটা সিন্দুক ভাবুন, ড্রয়ার নয়।**
SharedPreferences ([Q10](#q10)) হলো খোলা ড্রয়ার — যে কেউ file খুললেই পড়ে ফেলবে। `flutter_secure_storage` হলো তালাবদ্ধ সিন্দুক, যার চাবি রাখে operating system-এর hardware-backed security। Rooted phone-এও ভেতরের জিনিস encrypted থাকে।

**ধাপ ২ — কোন platform-এ কী ব্যবহার করে।**

```
  Dart API: read / write / delete
       |
       +-------------------+-----------------+
       |                                     |
   iOS                                   Android
   Keychain (hardware-backed)            Keystore makes an AES key
                                              |
                                         EncryptedSharedPreferences
                                         (AES-256 encrypted values)
```

**ধাপ ৩ — শুধু secret-এর জন্যই ব্যবহার করুন।**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'dart:convert';

class SecureTokenStorage {
  final _storage = const FlutterSecureStorage(
    aOptions: AndroidOptions(encryptedSharedPreferences: true), // গুরুত্বপূর্ণ
    iOptions: IOSOptions(accessibility: KeychainAccessibility.first_unlock),
  );

  Future<void> saveTokens({
    required String accessToken,
    required String refreshToken,
  }) async {
    await _storage.write(key: 'access_token', value: accessToken);
    await _storage.write(key: 'refresh_token', value: refreshToken);
  }

  Future<String?> getAccessToken() => _storage.read(key: 'access_token');

  Future<void> clearAll() => _storage.deleteAll(); // logout-এর সময়

  // Hive-এর encryption key এখানে রাখুন (code-এ নয়) — Q11/Q14-এর সাথে যুক্ত
  Future<void> saveHiveKey(List<int> key) =>
      _storage.write(key: 'hive_key', value: base64Encode(key));

  Future<List<int>?> getHiveKey() async {
    final v = await _storage.read(key: 'hive_key');
    return v == null ? null : base64Decode(v);
  }
}
```

**ধাপ ৪ — কখন ব্যবহার করবেন না।**
বড় dataset, বারবার পড়া লাগে এমন data (প্রতি read/write-এ encryption ধীর), বা সাধারণ non-sensitive settings। এগুলোর জায়গা SharedPreferences, Hive, বা Drift।

**Interviewer কেন জিজ্ঞেস করে:** Plain-text SharedPreferences-এ token রাখা rooted/jailbroken device-এ একটা আসল vulnerability। তাঁরা দেখতে চান আপনি জানেন secret-এর জায়গা ঠিক কোথায়।

**সাধারণ ভুল:** সব কিছুর জন্য `flutter_secure_storage` ব্যবহার করা (এটা ধীর)। আর Android-এ `encryptedSharedPreferences: true` দিতে ভুলে যাওয়া, যার ফলে পুরোনো device-এ দুর্বল implementation-এ নেমে যেতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`KeychainAccessibility.first_unlock` কী?"* → এটা ঠিক করে value কখন পড়া যাবে — এখানে, boot-এর পর device একবার unlock হওয়ার পরেই (security আর ব্যবহারযোগ্যতার ভালো ভারসাম্য)।
- *"Hive/SQLCipher-এর key কোথায় রাখেন?"* → এখানেই, secure storage-এ — কখনোই source-এ hardcode করে নয় ([Q14](#q14) দেখুন)।

**সম্পর্কিত:** [Q3 — auth-এর জন্য token](#q3) · [Q10 — SharedPreferences](#q10) · [Q14 — encryption](#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q14"></a>
## 14. Flutter-এ local data কীভাবে encrypt করেন?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি data অনুযায়ী tool বেছে নিই। Secret যায় `flutter_secure_storage`-এ (OS keychain/keystore)। Structured object যায় encrypted Hive box-এ (AES-256)। Relational data যায় SQLCipher-এ, `sqflite_sqlcipher` দিয়ে। যেকোনো file-এর জন্য `encrypt` package। সব কিছুকে বেঁধে রাখা নিয়মটা একটাই: encryption key কখনোই hardcode করবেন না — এটা generate করুন আর secure storage-এ রাখুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — আসল খেলাটা key নিয়ে (তালা-চাবির উপমা)।**
Data encrypt করা মানে একটা বাক্সে তালা দেওয়া। কিন্তু চাবিটা যদি ঢাকনার গায়ে টেপ দিয়ে লাগিয়ে রাখেন (code-এ hardcode করা, বা SharedPreferences-এ রাখা), তাহলে তালাটা অকেজো। পুরো security নির্ভর করে চাবি কোথায় থাকে তার উপর — আর সেই জায়গাটা হলো OS keychain/keystore, `flutter_secure_storage`-এর মাধ্যমে।

**ধাপ ২ — Data-র ধরন অনুযায়ী layer বাছুন।**

```
  Data type           Tool                       Encryption
  ------------------  -------------------------  ------------------------
  Secrets / tokens    flutter_secure_storage     Keychain/Keystore (OS)
  Structured objects  Hive encrypted box         AES-256 (key kept secure)
  Relational data     sqflite_sqlcipher          AES-256 on the whole DB
  Arbitrary files     encrypt / pointycastle     AES (manual)
```

**ধাপ ৩ — কৌশল ১: encrypted Hive box, key থাকবে secure storage-এ।**

```dart
class EncryptedHiveStorage {
  static const _secure = FlutterSecureStorage();
  static const _keyName = 'hive_aes_key';

  static Future<List<int>> _getOrCreateKey() async {
    final existing = await _secure.read(key: _keyName);
    if (existing != null) return base64Decode(existing);

    final newKey = Hive.generateSecureKey();            // 32টি random byte
    await _secure.write(key: _keyName, value: base64Encode(newKey));
    return newKey;
  }

  static Future<Box<T>> openEncryptedBox<T>(String name) async {
    final key = await _getOrCreateKey();
    return Hive.openBox<T>(name, encryptionCipher: HiveAesCipher(key));
  }
}
```

**ধাপ ৪ — কৌশল ২: encrypted SQLite database-এর জন্য SQLCipher।**
পুরো database file-টাই একটা password দিয়ে encrypt হয়, আর সেই password আপনি secure storage থেকে পড়েন।

```dart
import 'package:sqflite_sqlcipher/sqflite_sqlcipher.dart';

final db = await openDatabase(
  'app.db',
  password: await secureStorage.read(key: 'db_password'), // secure storage থেকে
  version: 1,
  onCreate: (db, _) => db.execute(
    'CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)',
  ),
);
```

**ধাপ ৫ — কৌশল ৩: unique IV সহ হাতে করা file encryption।**
যেকোনো file-এর জন্য `encrypt` package ব্যবহার করুন। IV (initialization vector) **প্রতিবার encryption-এ আলাদা** হওয়া উচিত, আর সেটা ciphertext-এর পাশে রেখে দিন।

```dart
import 'package:encrypt/encrypt.dart' as e;
import 'dart:typed_data';

class FileEncryptor {
  final e.Encrypter _encrypter;
  FileEncryptor(List<int> keyBytes)
      : _encrypter = e.Encrypter(e.AES(e.Key(Uint8List.fromList(keyBytes))));

  ({String cipher, String iv}) encryptText(String plaintext) {
    final iv = e.IV.fromSecureRandom(16); // প্রতিবার নতুন random IV
    final cipher = _encrypter.encrypt(plaintext, iv: iv).base64;
    return (cipher: cipher, iv: iv.base64); // দুটোই রাখুন
  }

  String decryptText(String cipher, String ivBase64) =>
      _encrypter.decrypt64(cipher, iv: e.IV.fromBase64(ivBase64));
}
```

**ধাপ ৬ — যে নীতিগুলো মুখস্থ বলবেন।**
Key runtime-এ generate করুন, সেগুলো `flutter_secure_storage`-এ রাখুন, প্রতি operation-এ unique IV ব্যবহার করুন, আর নিজের crypto না লিখে পরিচিত library ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** Health, finance আর government app-এ data-at-rest encryption একটা compliance শর্ত। তাঁরা যাচাই করেন আপনি key-management-এর শেকলটা বোঝেন কি না — encryption ততটাই শক্ত, যতটা শক্ত key-এর রাখার জায়গা।

**সাধারণ ভুল:** একটা key generate করে সেটা SharedPreferences-এ রাখা, বা source-এ hardcode করা — তখন encryption শুধুই লোক দেখানো, কারণ device-এ access আছে এমন যে কেউ key পড়ে ফেলবে। আরেকটা ভুল: AES-এ একই static IV বারবার ব্যবহার করা; প্রতি encryption-এ নতুন IV লাগবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Unique IV কেন?"* → একই key-এর সাথে একই IV বারবার ব্যবহার করলে pattern ফাঁস হয় — একই plaintext block একই ciphertext দেয়, আর attacker সেটা কাজে লাগাতে পারে।
- *"Data কি memory-তেও encrypted থাকে?"* → না — এখানকার encryption হলো "at rest" (disk-এ)। Memory-তে এটা plain; এটাই স্বাভাবিক।

**সম্পর্কিত:** [Q13 — secure storage](#q13) · [Q11 — encrypted Hive box](#q11) · [Q12 — SQLite](#q12)

[↑ উপরে ফিরুন](#toc)

---

# H. Offline-first ও syncing

---

<a id="q15"></a>
## 15. Flutter-এ offline-first architecture কীভাবে implement করবেন?

> Common · Hard · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Offline-first মানে UI-এর জন্য local database-ই একমাত্র source of truth। App local storage থেকে পড়ে আর সাথে সাথে দেখায়। তারপর background-এ server-এর সাথে sync করে। Write আগে local-এ save হয় ('pending' চিহ্ন দিয়ে), local stream থেকে UI সাথে সাথে update হয়। Network ফিরে এলে background sync পরিবর্তনগুলো push করে। Data দেখানোর জন্য UI কখনোই network-এর অপেক্ষা করে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মূল পরিবর্তন: local DB-ই সত্য।**
সাধারণ app আগে server-কে জিজ্ঞেস করে, অপেক্ষা করে, তারপর data দেখায় (মাঝের সময়টা ফাঁকা screen)। Offline-first এটা উল্টে দেয়: UI local database-কে watch করে, আর সেখানে *কিছু না কিছু* সবসময় দেখানোর মতো থাকে। Network শুধু ওই local data-কে তাজা রাখে।

```
  Local DB (source of truth)  →  UI  (UI watches the local DB)
        |
        |  Repository writes to the local DB
        |
  Repository  →  Remote API   (fetch / sync in the background)
```

**ধাপ ২ — Write-এর প্রবাহ।**

```
  1. User creates an item
  2. Save to local DB immediately (syncStatus = pending)
  3. UI updates instantly (from the local DB stream)
  4. Background: try to push to the server
  5. Success → syncStatus = synced
  6. Failure → keep pending, retry later
```

**ধাপ ৩ — এমন একটা model যেটা sync state বহন করে।**
প্রতিটা row মনে রাখে সেটা push হয়েছে কি না।

```dart
enum SyncStatus { pending, synced, failed }

class Task {
  final String id;
  final String title;
  final bool completed;
  final SyncStatus syncStatus;
  final DateTime updatedAt;
  const Task({
    required this.id,
    required this.title,
    required this.completed,
    required this.syncStatus,
    required this.updatedAt,
  });
}
```

**ধাপ ৪ — Repository: আগে local, পরে server।**

```dart
class TaskRepository {
  final TaskLocalSource _local;   // Drift অথবা Hive
  final TaskRemoteSource _remote; // Dio API client

  // UI এটাতেই subscribe করে — সবসময় local DB থেকে পড়ে
  Stream<List<Task>> watchTasks() => _local.watchAll();

  Future<void> createTask(String title) async {
    final task = Task(
      id: const Uuid().v4(),        // client-generated id, তাই offline-safe
      title: title,
      completed: false,
      syncStatus: SyncStatus.pending,
      updatedAt: DateTime.now(),
    );
    await _local.insert(task);      // stream-এর মাধ্যমে UI সাথে সাথে update

    try {
      await _remote.create(task);
      await _local.updateSyncStatus(task.id, SyncStatus.synced);
    } catch (_) {
      // pending-ই থাকুক; SyncManager পরে আবার চেষ্টা করবে
    }
  }

  Future<void> refresh() async {
    try {
      final serverTasks = await _remote.fetchAll();
      await _local.upsertAll(serverTasks); // local DB-তে merge
    } catch (_) {
      // Offline — UI তখনও local data দেখায়, crash নেই
    }
  }
}
```

**ধাপ ৫ — Background sync manager।**
Connectivity ফিরে এলে ([Q9](#q9)) যা যা pending আছে সব push করুন।

```dart
class SyncManager {
  final TaskLocalSource _local;
  final TaskRemoteSource _remote;
  final ConnectivityCubit _connectivity;

  void startSync() {
    _connectivity.stream
        .where((s) => s == ConnectivityStatus.online)
        .listen((_) => _pushPending());
  }

  Future<void> _pushPending() async {
    for (final task in await _local.getByStatus(SyncStatus.pending)) {
      try {
        await _remote.upsert(task);
        await _local.updateSyncStatus(task.id, SyncStatus.synced);
      } catch (_) {
        await _local.updateSyncStatus(task.id, SyncStatus.failed);
      }
    }
  }
}
```

**Interviewer কেন জিজ্ঞেস করে:** আধুনিক mobile app-এ offline-first এখন প্রত্যাশিত। তাঁরা দেখতে চান আপনি local-DB-as-source-of-truth pattern design করতে পারেন কি না। আর sync state সামলাতে পারেন কি না।

**সাধারণ ভুল:** network call-কে source of truth বানানো, আর cache-কে শুধু fallback হিসেবে রাখা। সেটা "offline-capable", "offline-first" নয়। সত্যিকারের offline-first মানে data দেখানোর জন্য UI কখনোই network-এর অপেক্ষা করে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Client-generated UUID কেন?"* → যাতে offline অবস্থাতেই একটা স্থায়ী id দিয়ে item তৈরি করা যায়, server কিছু assign করার আগেই — sync-এর সময় কোনো সংঘর্ষ হয় না।
- *"UI সাথে সাথে update হয় কীভাবে?"* → এটা একটা local `Stream` watch করে (Drift-এর `watch()` বা Hive listenable); local-এ insert করলেই সাথে সাথে নতুন list emit হয়।

**সম্পর্কিত:** [Q9 — connectivity](#q9) · [Q12 — Drift watch()](#q12) · [Q16 — sync strategies](#q16)

[↑ উপরে ফিরুন](#toc)

---

<a id="q16"></a>
## 16. Local cached data-কে server-এর সাথে sync-এ রাখবেন কীভাবে?

> Deeper question · Hard · [🇬🇧 English](../software-engineer-flutter/section-07-networking-storage.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"এটা conflict model আর data-র আকারের উপর নির্ভর করে। Production-এ সবচেয়ে প্রচলিত পছন্দ হলো timestamp-based delta sync: client তার `lastSyncedAt` পাঠায়, server শুধু তার পরের পরিবর্তনগুলো ফেরত দেয়, আর client তার pending local পরিবর্তনগুলো push করে। Sync-কে ভাঙে দুটো জিনিস — conflict resolution আর non-idempotent push। তাই আমি দুটোরই পরিকল্পনা করে রাখি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — চারটি কৌশল, সহজ থেকে উন্নত।**

```
  1. Pull-to-refresh         → client pulls everything on demand; no conflicts.
                               Good for read-heavy, rarely-changing data.

  2. Timestamp delta sync    → client sends lastSyncedAt; server returns only
                               changes since then. Good for moderate data,
                               server is the authority. (Most common.)

  3. Event queue / changelog → client queues each mutation locally, pushes when
                               online; server applies or rejects. Offline-heavy.

  4. CRDT / operational transform → automatic merge via clever data structures.
                               For real-time collaborative editing (complex).
```

**ধাপ ২ — Delta sync কেন সাধারণত বেছে নেওয়া হয়।**
এটা "শেষবার দেখার পর কী কী বদলেছে?" ধরনের পদ্ধতি। প্রতিবার সবকিছু download করার বদলে (যেটা অপচয়), client বলে "দুপুর ২টার পর থেকে পরিবর্তনগুলো দাও"। Server তখন একটা ছোট তালিকা পাঠায়। Data আর battery — দুটোতেই সস্তা।

**ধাপ ৩ — দুই ধাপের sync: আগে push, তারপর pull।**

```dart
class SyncService {
  final LocalDatabase _local;
  final ApiClient _remote;
  final SharedPreferences _prefs;

  Future<void> sync() async {
    await _pushLocalChanges(); // আগে আমার pending edit পাঠাও
    await _pullRemoteChanges(); // তারপর বাকি সবার edit আনো
  }

  Future<void> _pushLocalChanges() async {
    for (final item in await _local.getPending()) {
      try {
        final serverItem = await _remote.upsert(item); // server এটা বদলাতে পারে
        await _local.upsert(serverItem.copyWith(syncStatus: SyncStatus.synced));
      } on ConflictException catch (e) {
        // Conflict → server version জেতে (বা user-কে জিজ্ঞেস করুন)
        await _local.upsert(e.serverVersion.copyWith(syncStatus: SyncStatus.synced));
      }
    }
  }

  Future<void> _pullRemoteChanges() async {
    final lastSync = _prefs.getString('last_sync_at');
    final changes = await _remote.getChanges(since: lastSync); // শুধু delta

    for (final change in changes) {
      switch (change.type) {
        case ChangeType.upsert:
          await _local.upsert(change.item.copyWith(syncStatus: SyncStatus.synced));
        case ChangeType.delete:
          await _local.delete(change.itemId);
      }
    }
    // পরের বারের জন্য নতুন watermark save করুন
    await _prefs.setString('last_sync_at', DateTime.now().toUtc().toIso8601String());
  }
}
```

Pull-এর API contract দেখতে এমন:

```
GET /items?since=2026-06-01T00:00:00Z
Response:
{
  "changes": [
    { "type": "upsert", "item": { ... }, "updatedAt": "..." },
    { "type": "delete", "itemId": "abc",  "deletedAt": "..." }
  ]
}
```

**ধাপ ৪ — Conflict resolution-এর পছন্দগুলো।**
একই item দুই জায়গায় বদলে গেলে:
- *Last-write-wins:* সবচেয়ে নতুন `updatedAt` জেতে (সহজ, প্রচলিত)।
- *Server-wins:* server সবসময় ঠিক (নিরাপদ, অনুমানযোগ্য)।
- *Client-wins:* বিপজ্জনক, খুব কমই ব্যবহার হয়।
- *Manual merge:* user-কে দুটো version-ই দেখান (গুরুত্বপূর্ণ data-র জন্য)।

**ধাপ ৫ — Push-গুলোকে idempotent বানান।**
"Idempotent" মানে একই push দুইবার করলেও ফল একবারের মতোই থাকে। এটা দরকার কারণ push server-এ সফল হতে পারে, কিন্তু local-এ "mark as synced" ব্যর্থ হতে পারে — তখন পরের sync আবার সেটা পাঠাবে। একটা স্থায়ী client id ব্যবহার করুন ([Q15](#q15)-এর UUID)। তাহলে server duplicate চিনতে পারবে আর দ্বিতীয় copy বানাবে না।

**Interviewer কেন জিজ্ঞেস করে:** বেশিরভাগ offline architecture ভেঙে পড়ে ঠিক sync-এর জায়গাতেই। তাঁরা দেখতে চান আপনি conflict resolution, sync-এর মাঝপথে আংশিক ব্যর্থতা আর idempotency নিয়ে ভেবেছেন কি না।

**সাধারণ ভুল:** delta sync-এ `updatedAt`-এর বদলে `createdAt` ব্যবহার করা — তাহলে প্রতিটা edit বাদ পড়ে যাবে। আরেকটা ভুল non-idempotent push: সফল push-এর পরেও local status update ব্যর্থ হলে পরের sync item-টা duplicate করে ফেলবে, যদি না server সেটা সুন্দরভাবে সামলায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Device-এর ঘড়ি ভুল থাকলে কী হবে?"* → watermark-এর জন্য device clock-এর বদলে server-assigned timestamp বা version number ব্যবহার করুন।
- *"একাধিক device জুড়ে delete কীভাবে করবেন?"* → "soft delete" ব্যবহার করুন (একটা `deletedAt` flag)। তাহলে delete নিজেই একটা পরিবর্তন হয়ে sync হয়, row-টা শুধু হাওয়া হয়ে যায় না।

**সম্পর্কিত:** [Q15 — offline-first](#q15) · [Q9 — connectivity trigger](#q9) · [Q12 — local DB](#q12)

[↑ উপরে ফিরুন](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। প্রথমে দ্রুত তুলনার table-গুলো, তারপর এক লাইনের মনে করিয়ে দেওয়া পয়েন্টগুলো।

## দ্রুত তুলনার table

**`http` vs Dio**

| | `http` | Dio |
|---|---|---|
| Setup | প্রতিটা call-এ হাতে করতে হয় | একবার configure করলেই হয় (`BaseOptions`) |
| Interceptors | নেই | আছে (auth, logging, retry) |
| Cancel / progress | নেই | আছে |
| JSON parsing | হাতে করা `jsonDecode` | স্বয়ংক্রিয় (`response.data`) |
| কোন কাজে ভালো | ছোট app, script | production app |

**SharedPreferences vs Hive vs SQLite/Drift vs secure_storage**

| | SharedPreferences | Hive | SQLite / Drift | secure_storage |
|---|---|---|---|---|
| গড়ন | key-value (primitive) | key-value (object) | relational table | key-value (secret) |
| Encryption | নেই | আছে (AES) | আছে (SQLCipher) | আছে (OS keychain) |
| Query / join | নেই | নেই | আছে | নেই |
| গতি | ধীর (XML) | দ্রুত (binary) | দ্রুত, indexed | ধীর (encrypted) |
| কোন কাজে ভালো | setting, flag | structured cache | relation, জটিল query | token, key, PII |

**Timeout-এর ধরন**

| | মানে | সাধারণ মান |
|---|---|---|
| connectTimeout | connection খোলা | 5–10s |
| receiveTimeout | response data-র জন্য অপেক্ষা | API-র সাথে মিলিয়ে (15–60s) |
| sendTimeout | request body upload করা | বড় file-এর জন্য উদার রাখুন |

**Sync-এর কৌশল**

| কৌশল | কোন কাজে ব্যবহার করবেন |
|---|---|
| Pull-to-refresh | বেশি পড়া হয়, পরিবর্তন কম |
| Timestamp delta sync | মাঝারি data, server-এর কর্তৃত্ব (সবচেয়ে প্রচলিত) |
| Event queue / changelog | offline-নির্ভর app |
| CRDT / OT | real-time collaborative editing (একসাথে একই জিনিস সম্পাদনা) |

## এক লাইনের মনে করিয়ে দেওয়া

- **`http`** = হাতে করা আর সাদামাটা; **Dio** = interceptor, cancellation, progress, auto-JSON। আসল app-এর জন্য Dio বেছে নিন। ([Q1](#q1))
- **connectTimeout** = লাইন খোলা; **receiveTimeout** = উত্তরের জন্য অপেক্ষা। শুধু timeout আর 5xx-এ retry করুন, backoff সহ। ([Q2](#q2))
- **Interceptor** হলো airport security: `onRequest`-এ token জুড়ে দিন, 401-এ `QueuedInterceptor` দিয়ে একবারই refresh করুন, refresh call-এর জন্য আলাদা Dio ব্যবহার করুন। ([Q3](#q3))
- **প্রতিটা `DioException` type-কে** একটা typed `sealed` failure-এ map করুন; কাঁচা status code widget-এ ফাঁস করবেন না। ([Q4](#q4))
- **REST** = অনেকগুলো নির্দিষ্ট endpoint; **GraphQL** = একটাই endpoint, field আপনি বেছে নেন। GraphQL-এর caching আর সবসময় 200 দিয়ে error পাঠানোই হলো ফাঁদ। ([Q5](#q5))
- **Either / Result** signature-কে সৎ করে: ফেরত দেয় **Failure অথবা data**, তাই caller-কে দুটোই handle করতে হয়। ([Q6](#q6))
- **JSON**: `fromJson` হাতে লিখুন শুধু খুব ছোট model-এর জন্য; ব্যবহার করুন **`json_serializable`**, আর immutability + equality + `copyWith` একসাথে চাইলে **`freezed`**। ([Q7](#q7))
- **Certificate pinning** = শুধু *আপনার* key-কে বিশ্বাস করা, যেকোনো CA-কে নয়। **public key** pin করুন আর একটা backup pin রাখুন। ([Q8](#q8))
- **`connectivity_plus`** আপনাকে interface-এর খবর দেয়, আসল internet-এর নয় — একটা DNS lookup দিয়ে নিশ্চিত হোন; ব্যর্থ হলে cache দেখান। ([Q9](#q9))
- **SharedPreferences** = ছোট primitive setting-এর জন্য sticky note; encryption নেই, পুরো file load করে। ([Q10](#q10))
- **Hive** = দ্রুত pure-Dart object store; একটা **box** হলো table, একটা **TypeAdapter** হলো অনুবাদক; `typeId` কখনোই আবার ব্যবহার করবেন না। ([Q11](#q11))
- **SQLite / Drift** = relation, join, transaction আর reactive `watch()` stream; migration-এর কথা মনে রাখুন। ([Q12](#q12))
- **`flutter_secure_storage`** = token আর key রাখার সিন্দুক (Keychain/Keystore); ধীর, তাই শুধু secret-এর জন্য। ([Q13](#q13))
- **Encryption** ততটাই শক্ত, key যেখানে থাকে সেটা যতটা শক্ত — key generate করুন, secure storage-এ রাখুন, প্রতিবার নতুন IV ব্যবহার করুন। ([Q14](#q14))
- **Offline-first** = local DB-ই সত্যের উৎস; আগে locally save করুন (pending), UI সাথে সাথে update হয়, sync চলে background-এ। ([Q15](#q15))
- **Delta sync** `lastSyncedAt` পাঠায় আর শুধু পরিবর্তনগুলো নেয়; `updatedAt` ব্যবহার করুন, conflict মেটান, push-কে idempotent করুন। ([Q16](#q16))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Interviewer সাধারণত একটা প্রশ্নে থামেন না। আপনার গভীরতা পরীক্ষা করতে তাঁরা খুঁড়তেই থাকেন। এই ধারাবাহিক প্রশ্নগুলোর উত্তর মুখে বলে অনুশীলন করুন — শান্তভাবে, ধাপে ধাপে:

1. *"প্রতিটা request-এ auth token কীভাবে জোড়েন?"* → একটা interceptor-এর `onRequest` `Authorization` header যোগ করে।
2. *"Token মেয়াদ শেষ হলে কী হয়?"* → server 401 ফেরত দেয়; `onError` hook token refresh করে আবার চেষ্টা করে।
3. *"একসাথে তিনটা request 401 পেল — এখন কী?"* → `QueuedInterceptor` ব্যবহার করুন, যাতে একটাই refresh চলে; বাকিরা অপেক্ষা করে নতুন token কাজে লাগায়।
4. *"ওই token কোথায় রাখেন?"* → `flutter_secure_storage`-এ (Keychain/Keystore), কখনোই SharedPreferences-এ নয়।
5. *"User কাজ করার সময় app offline — তখন কী?"* → পরিবর্তনটা locally `pending` হিসেবে save করুন, সাথে সাথে দেখান, আর connection ফিরলে sync করুন।

এভাবে শান্তভাবে ধাপে ধাপে যেতে পারা — অনুমান না করে — ঠিক এই জিনিসটাই আপনাকে **senior** শোনায়, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
