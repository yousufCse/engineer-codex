# Section 21 — Mobile-এর জন্য System Design

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন। Design-গুলোতে সরল diagram আর মূল সিদ্ধান্ত আছে, code-এর পাহাড় নয়।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-21-system-design.md](../software-engineer-flutter/section-21-system-design.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — ধাপে ধাপে design, সাথে একটা diagram আর মূল সিদ্ধান্তগুলো।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** Design প্রশ্নে **আগে requirement পরিষ্কার করুন**, তারপর architecture নিয়ে জোরে জোরে কথা বলুন আর trade-off-গুলোর নাম বলুন। Interviewer আপনার *যুক্তি আর যোগাযোগ* দেখে নম্বর দেন, একটামাত্র "সঠিক" diagram দেখে নয়।

---


## <a id="toc"></a>সূচিপত্র

**A. মূল Framework**
1. [Mobile system design প্রশ্নের কাছে কীভাবে যাবেন](#q1) · *Very common*
2. [Live data-র জন্য REST vs WebSocket](#q2) · *Common*

**B. Design অনুশীলন**
3. [একটা real-time chat app design করুন](#q3) · *Common*
4. [একটা offline-first feed design করুন](#q4) · *Common*
5. [একটা authentication system design করুন](#q5) · *Very common*
6. [Photo upload design করুন (chunked, retry, compress)](#q6) · *Common*
7. [Push notification architecture design করুন](#q7) · *Common*
8. [একটা shopping cart design করুন](#q8) · *Common*

**C. বড় স্কেলে Architecture**
9. [Scalability-র জন্য design](#q9) · *Common*
10. [50+ screen আর 10+ dev-এর app-এর architecture](#q10) · *Common*
11. [একটা plugin / SDK design করুন](#q11) · *Deeper*

**D. Cross-cutting concerns**
12. [API versioning ও breaking change](#q12) · *Common*
13. [পুরো app জুড়ে error handling](#q13) · *Very common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিউ)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — উপায় (এখান থেকে শুরু করুন)।**
→ [Q1 মূল Framework](#q1) · [Q2 REST vs WebSocket](#q2)

**পর্যায় ২ — ক্লাসিক design-গুলো।**
→ [Q3 Chat](#q3) · [Q4 Offline feed](#q4) · [Q5 Authentication](#q5)

**পর্যায় ৩ — আরও design।**
→ [Q6 Photo upload](#q6) · [Q7 Push notification](#q7) · [Q8 Shopping cart](#q8)

**পর্যায় ৪ — বড় স্কেলে architecture।**
→ [Q9 Scalability](#q9) · [Q10 বড় app](#q10) · [Q11 Plugin/SDK](#q11)

**পর্যায় ৫ — Cross-cutting।**
→ [Q12 API versioning](#q12) · [Q13 Error handling](#q13)

**সময় কম?** পড়ুন [Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q13](#q13), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. মূল Framework

---

## <a id="q1"></a>1. Flutter/mobile context-এ system design প্রশ্নের কাছে আপনি কীভাবে যান?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি একটা সরল framework ব্যবহার করি: প্রথমে requirement আর scope পরিষ্কার করি, তারপর high-level architecture আঁকি, তারপর mobile-এর মূল বিষয়গুলোতে ঢুকি — data flow, state management, local storage, offline support, আর networking। পুরো সময় আমি trade-off নিয়ে জোরে জোরে কথা বলি। উদ্দেশ্য হলো গোছানো চিন্তা দেখানো, একটা সঠিক উত্তর মুখস্থ করা নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — আগে পরিষ্কার করুন (সমাধানে ঝাঁপ দেবেন না)।**
প্রশ্ন করুন: কত user? Real-time লাগবে কি না? Offline লাগবে? কোন platform? এতে পরিপক্বতা বোঝা যায়। আর ভুল জিনিস design করা থেকেও বাঁচা যায়।

**ধাপ ২ — পাঁচ ধাপের framework।**

```
1. Requirements   – functional + non-functional (scale, offline, latency)
2. High-level     – app ↔ API ↔ services ↔ database; the big boxes
3. Data flow      – how data moves; state management choice
4. Mobile concerns– local storage, offline/sync, caching, networking
5. Trade-offs     – discuss alternatives and why you chose what you did
```

**ধাপ ৩ — *mobile* অংশগুলোতে জোর দিন।**
Mobile system design মানে শুধু backend-এর box আঁকা নয়। সময় দিন এগুলোতে: offline-first, দুর্বল network, battery/data-র সীমা, local caching, আর device-এ state management। এগুলোই এটাকে *mobile* design প্রশ্ন বানায়।

**ধাপ ৪ — সারাক্ষণ কথা বলতে থাকুন।**
জোরে জোরে ভাবুন, box আঁকুন, ধরে নেওয়া কথাগুলো বলুন। সাথে trade-off-এর নাম বলুন ("WebSocket latency কমায়, কিন্তু একটা persistent connection খরচ করে")। Interviewer আপনার যুক্তি আর যোগাযোগ দেখে নম্বর দেন।

**Interviewer কেন জিজ্ঞেস করে:** এটা মূল দক্ষতা — তাঁরা দেখতে চান আপনি গোছানো, requirement-আগে উপায়ে চলেন কি না, মুখস্থ diagram আঁকেন কি না।

**সাধারণ ভুল:** Requirement পরিষ্কার না করেই সরাসরি সমাধানে চলে যাওয়া। অথবা mobile-এর নিজের বিষয় (offline, দুর্বল network) বাদ দিয়ে এটাকে শুধু backend প্রশ্নের মতো ভাবা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Mobile আর web design-এ পার্থক্য কী?"* → Offline support, ভরসা নেই এমন network, সীমিত battery/data, local storage, আর app lifecycle।

**সম্পর্কিত:** [Q2 — REST vs WebSocket](#q2) · [Q3 (SDLC) — HLD vs LLD](section-19-sdlc-bn.md#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Live data-র জন্য REST আর WebSocket-এর trade-off কী কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"REST হলো request/response — app জিজ্ঞেস করে, server উত্তর দেয়, তারপর connection বন্ধ হয়ে যায়। এটা সরল আর বেশিরভাগ data-র জন্য দারুণ। WebSocket একটাই connection খোলা রাখে দুই-মুখী, real-time message-এর জন্য — chat, live score বা presence-এর জন্য আদর্শ। WebSocket কম latency দেয়, কিন্তু একটা persistent connection আর বাড়তি জটিলতা খরচ করে; REST সরল, তবে নিজে থেকে update push করতে পারে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি।**
- **REST** = চিঠি পাঠানো: আপনি জিজ্ঞেস করেন, অপেক্ষা করেন, উত্তর পান। একবারে একটা লেনদেন।
- **WebSocket** = phone call: line খোলা থাকে, দুই পক্ষ যেকোনো সময় কথা বলে।

**ধাপ ২ — তুলনা।**

| | REST | WebSocket |
|---|---|---|
| ধরন | request/response | persistent, দুই-মুখী |
| Server push | নেই (poll করতে হয়) | আছে (সাথে সাথে) |
| Latency | বেশি | কম |
| জটিলতা | সরল | বেশি (reconnect, heartbeat) |
| কীসের জন্য সেরা | বেশিরভাগ CRUD data | chat, live update, presence |

**ধাপ ৩ — মাঝামাঝি option-গুলো।**
- **Polling** — timer ধরে REST call (সরল, কিন্তু অপচয় আর দেরি হয়)।
- **Long polling / SSE (Server-Sent Events)** — পুরো WebSocket ছাড়াই server এক-মুখী push করতে পারে।
- **WebSocket** — পুরো দুই-মুখী real-time।

**ধাপ ৪ — কীভাবে বেছে নেবেন।**
সাধারণ data-র জন্য REST ব্যবহার করুন (profile, order)। WebSocket যোগ করুন *শুধু* সেখানে, যেখানে live, কম latency-র দুই-মুখী update দরকার (chat, live tracking)। সবকিছুকে WebSocket বানাবেন না — এতে reconnection আর scaling-এর জটিলতা বাড়ে।

**Interviewer কেন জিজ্ঞেস করে:** অনেক design-এ সঠিক transport বেছে নেওয়াই প্রথম সিদ্ধান্ত (chat, live feed)।

**সাধারণ ভুল:** সবকিছুতে WebSocket ব্যবহার করা (বাড়তি জটিল)। অথবা সত্যিকারের real-time দরকারে polling ব্যবহার করা (দেরি হয়, battery খায়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"WebSocket ছুটে গেলে কী করবেন?"* → Backoff দিয়ে auto-reconnect, drop ধরার জন্য heartbeat, আর reconnect-এর পরে বাদ পড়া message আবার sync করা।

**সম্পর্কিত:** [Q3 — chat](#q3) · [Q7 — push notification](#q7) · [Q1 (Networking) — http vs Dio](section-07-networking-storage-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

# B. Design অনুশীলন

---

## <a id="q3"></a>3. Flutter-এ একটা real-time chat application design করুন।

> Common · Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি real-time messaging-এর জন্য WebSocket নেব, chat state সামলাতে একটা BLoC/Cubit নেব, আর message রাখতে একটা local database (যেমন Drift বা Hive) নেব — offline access আর সাথে সাথে load হওয়ার জন্য। Message আগে locally রাখা হয় (optimistic), তারপর socket দিয়ে পাঠানো হয়, আর server confirm করে। আমি reconnection, ordering, আর delivery/read receipt সামলাব।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Requirement পরিষ্কার করুন।**
1-to-1 না group? Media লাগবে? Read receipt? Offline? কত scale? ধরে নিলাম: 1-to-1 + group, text + image, read receipt, offline history।

**ধাপ ২ — High-level architecture।**

```
Flutter app  ── WebSocket ──►  Chat server  ──►  Message DB
   │  (live messages)              │
   │                              push (FCM) for offline users
   └─ Local DB (Drift/Hive): stores messages for offline + instant load
```

**ধাপ ৩ — মূল সিদ্ধান্তগুলো।**
- **Transport** — live message-এর জন্য WebSocket ([Q2](#q2)); history pagination-এর জন্য REST।
- **State** — BLoC/Cubit message list ধরে রাখে; নতুন message এলে UI rebuild হয় ([Q3 State Mgmt](section-03-state-management-bn.md#q1))।
- **Local storage** — একটা local DB সব message রাখে, তাই chat সাথে সাথে load হয় আর offline-এও চলে।
- **Optimistic UI** — message সাথে সাথে "sending" হিসেবে দেখান, তারপর server confirm করলে "sent/delivered/read" চিহ্ন দিন।

**ধাপ ৪ — কঠিন অংশগুলো সামলান।**
- **Ordering** — server-এর timestamp/sequence number ব্যবহার করুন; ওগুলো দিয়ে sort করুন, পৌঁছানোর order দিয়ে নয়।
- **Reconnection** — backoff দিয়ে auto-reconnect; reconnect-এর সময় offline থাকাকালীন বাদ পড়া message নিয়ে আসুন।
- **Offline send** — message locally queue করুন; socket আবার যুক্ত হলে পাঠান।
- **Notification** — user offline থাকলে server একটা **push** পাঠায় ([Q7](#q7))।

**ধাপ ৫ — Trade-off।**
WebSocket সাথে সাথে delivery দেয়, কিন্তু reconnection/heartbeat logic লাগে। আর অনেক খোলা connection-এর জন্য server resource-ও লাগে। Local DB জটিলতা বাড়ায়, কিন্তু offline আর সাথে সাথে load-এর জন্য এটা অবশ্যই লাগে এমন।

**Interviewer কেন জিজ্ঞেস করে:** Chat mobile-এর প্রতিটা কঠিন বিষয় ছুঁয়ে যায় — real-time, offline, state, storage, ordering।

**সাধারণ ভুল:** Offline/reconnection আর message ordering ভুলে যাওয়া। অথবা local storage বাদ দেওয়া (তখন network ছাড়া chat একদম ফাঁকা দেখায়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Message-এর order কীভাবে নিশ্চিত করবেন?"* → Server-এর দেওয়া sequence number/timestamp; ওগুলো দিয়েই sort করুন।
- *"Group chat-এর fan-out?"* → Server প্রতিটা message সব member-এর connection-এ পাঠায় (অথবা offline member-দের জন্য একটা push queue করে)।

**সম্পর্কিত:** [Q2 — WebSocket](#q2) · [Q4 — offline](#q4) · [Q7 — push](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. Flutter-এ একটা offline-first news feed design করুন।

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Offline-first মানে UI-এর জন্য local database-ই একমাত্র source of truth। App সবসময় local storage থেকে পড়ে (তাই এটা সাথে সাথে কাজ করে, offline-ও কাজ করে)। একটা background sync API থেকে নতুন data এনে local store update করে। UI শুধু local DB-তে listen করে, আর পরিবর্তন হলে rebuild হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মূল ধারণা: local DB-ই source of truth।**
UI কখনো network-এর জন্য অপেক্ষা করে না। এটা local database (Drift/Hive) থেকে পড়ে। Network-এর কাজ হলো background-এ ওই database *update* করা।

**ধাপ ২ — Architecture।**

```
UI  ◄── watches ──  Local DB (source of truth)  ◄── sync ──  API
                         ▲
            repository decides: read local first, refresh in background
```

**ধাপ ৩ — পুরো flow।**
1. App খুলল → local DB থেকে cache করা article সাথে সাথে দেখান।
2. Background-এ API থেকে নতুন article আনুন।
3. সেগুলো local DB-তে save করুন।
4. UI তো DB-তে watch করছে (একটা reactive stream), তাই এটা নিজে নিজেই update হয়।

```dart
// Repository: আগে local, তারপর refresh
Stream<List<Article>> watchFeed() => localDb.watchArticles(); // UI এটার সাথেই bind হয়
Future<void> refresh() async {
  final fresh = await api.getArticles();
  await localDb.upsertAll(fresh); // stream দিয়ে UI update হয়
}
```

**ধাপ ৪ — খুঁটিনাটি সামলান।**
- **Pagination** — page-গুলো local-এ রাখুন; load more করলে DB-তে যোগ হবে।
- **Stale data** — cache করা data সাথে সাথে দেখান, background-এ refresh করুন, চাইলে একটা "updated" indicator দেখান।
- **Conflict** — read-only feed-এর জন্য server জেতে; user data-র জন্য একটা merge strategy ঠিক করুন।
- **Images** — সেগুলোও cache করুন (`cached_network_image`)।

**ধাপ ৫ — Trade-off।**
Offline-first দ্রুত আর মজবুত UX দেয়। কিন্তু এটা sync-এর জটিলতা আর storage বাড়ায়। Feed-এর ক্ষেত্রে এই খরচটা ভালোই কাজে লাগে — খারাপ network-এ ফাঁকা screen user-রা একদম পছন্দ করেন না।

**Interviewer কেন জিজ্ঞেস করে:** Offline-first হলো mobile-এর সিগনেচার design pattern; এটা data flow আর sync নিয়ে আপনার চিন্তা যাচাই করে।

**সাধারণ ভুল:** Network-কে source of truth ধরা (ফলে offline-এ ফাঁকা screen)। এর বদলে local storage থেকে পড়ুন আর background-এ sync করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"নতুন কোনটা তা কীভাবে বুঝবেন?"* → timestamp/etag বা একটা "since" cursor ব্যবহার করুন, যাতে শুধু নতুন item আনা হয়।

**সম্পর্কিত:** [Q3 — chat (offline)](#q3) · [Q15 (Networking) — offline-first](section-07-networking-storage-bn.md#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Flutter-এ একটা authentication system design করুন (login, token storage, refresh, logout)।

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"User login করে, server একটা স্বল্পমেয়াদি access token আর একটা দীর্ঘমেয়াদি refresh token ফেরত দেয়। আমি দুটোই secure storage-এ রাখি। প্রতিটা request-এ access token যায়। এটার মেয়াদ শেষ হলে (401) একটা interceptor refresh token দিয়ে নতুন token নেয় এবং request আবার পাঠায়। Logout token মুছে দেয় আর server-কে refresh token revoke করতে বলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Login flow।**

```
User → enter credentials → POST /login
     ← access token (short) + refresh token (long)
App  → store BOTH in secure storage (Keychain/Keystore)
```

**ধাপ ২ — Request-এ token ব্যবহার।**
একটা Dio interceptor প্রতিটা request-এ access token জুড়ে দেয়:

```dart
dio.interceptors.add(InterceptorsWrapper(
  onRequest: (options, handler) async {
    final token = await secureStorage.read(key: 'access_token');
    options.headers['Authorization'] = 'Bearer $token';
    handler.next(options);
  },
));
```

**ধাপ ৩ — মেয়াদ শেষে silent refresh।**
কোনো request 401 ফেরত দিলে interceptor refresh করে আবার চেষ্টা করে — user-কে কোনো ঝামেলা না দিয়ে:

```
request → 401 → use refresh token → get new access token → retry original
       (if refresh also fails → log the user out)
```

একসাথে আসা 401-গুলোকে queue-তে রাখুন, যাতে একবারই refresh হয়, বারবার নয়।

**ধাপ ৪ — Logout আর security।**
- **Logout** → secure storage থেকে token মুছুন, আর server-কে call করে refresh token revoke করান।
- **Storage** → শুধু secure storage ([Q3 Security](section-20-mobile-security-bn.md#q3)); কখনোই SharedPreferences নয়।
- **Tokens** → স্বল্পমেয়াদি access + refresh, চাইলে rotation সহ ([Q9 Security](section-20-mobile-security-bn.md#q9))।
- **Biometric gate** → চাইলে app খোলার সময় biometrics দিয়ে জমানো token unlock করার নিয়ম রাখুন।

**ধাপ ৫ — Trade-off।**
ছোট token + refresh interceptor-এর জটিলতা বাড়ায়। কিন্তু token ফাঁস হলে ক্ষতি অনেক কমে যায়। Auto-refresh-কে concurrency খুব সাবধানে সামলাতে হয় (অনেক request একসাথে 401 হতে পারে)।

**Interviewer কেন জিজ্ঞেস করে:** প্রতিটা app-এ auth থাকে; এটা secure storage, interceptor আর token lifecycle একসাথে যাচাই করে।

**সাধারণ ভুল:** Token অনিরাপদভাবে রাখা, মেয়াদহীন একটামাত্র token ব্যবহার করা, অথবা "refresh token-ও শেষ" অবস্থাটা না সামলানো (তখন জোর করে আবার login করাতে হবে)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একসাথে অনেক request 401 পেলে?"* → একবার refresh করুন, বাকি request থামিয়ে রাখুন, তারপর নতুন token দিয়ে সেগুলো আবার পাঠান।

**সম্পর্কিত:** [Q9 (Security) — tokens](section-20-mobile-security-bn.md#q9) · [Q3 (Security) — secure storage](section-20-mobile-security-bn.md#q3) · [Q3 (Networking) — interceptors](section-07-networking-storage-bn.md#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. একটা photo upload feature design করুন (chunked upload, progress, retry, compression)।

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি আগে image compress করব, যাতে bandwidth বাঁচে। তারপর upload করব — বড় file হলে chunk করে, যাতে ব্যর্থ হলে শুধু একটা chunk আবার পাঠাতে হয়। Dio-র callback থেকে progress দেখাব, ব্যর্থ chunk backoff দিয়ে retry করব, আর upload এমনভাবে চালাব যাতে user অন্য screen-এ গেলেও সেটা টিকে থাকে। Server chunk-গুলো জোড়া লাগিয়ে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Upload-এর আগে compress করুন।**
Phone-এর একটা ছবি কয়েক MB হতে পারে। আগে সেটা compress/resize করুন, যাতে upload-এর সময় আর data খরচ কমে (যেমন `flutter_image_compress`)। quality-র দরকারটাও মাথায় রাখুন।

**ধাপ ২ — বড় file-এর জন্য chunked upload।**
File-টাকে chunk-এ ভাগ করুন আর প্রতিটা আলাদা করে upload করুন। একটা ব্যর্থ হলে শুধু ওই chunk আবার পাঠাবেন, পুরো file নয়।

```
file → [chunk 1][chunk 2][chunk 3] → upload each → server reassembles
       (retry only the failed chunk)
```

**ধাপ ৩ — Progress আর retry।**

```dart
await dio.post('/upload', data: formData,
  onSendProgress: (sent, total) {
    final percent = sent / total; // progress bar চালায়
  },
);
```

- **Progress** — UI update করতে `onSendProgress` ব্যবহার করুন।
- **Retry** — chunk ব্যর্থ হলে exponential backoff দিয়ে retry করুন; N বার চেষ্টার পরে থামুন আর user-কে নিজে retry করতে দিন।

**ধাপ ৪ — App lifecycle-এ টিকে থাকুন।**
Upload ধীর হতে পারে। একটা background upload ব্যবস্থা ভাবুন, যাতে user screen ছেড়ে গেলেও সেটা চলতে থাকে। Network চলে গেলে আবার শুরু করতে upload-গুলো queue-তে রাখুন। প্রতিটা upload-এর state (pending/uploading/failed/done) local-এ লিখে রাখুন।

**ধাপ ৫ — Trade-off।**
Chunking + retry জটিলতা বাড়ায়। কিন্তু দুর্বল mobile network-এ বড় file-এর জন্য এটা জরুরি। ছোট ছবির জন্য একটা single multipart upload-ই সহজ আর যথেষ্ট।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি ভরসা নেই এমন network-এ বড় data কীভাবে সামলান — এটা mobile-এর একটা বাস্তব চ্যালেঞ্জ।

**সাধারণ ভুল:** বিশাল uncompressed file একবারে upload করা, কোনো progress বা retry ছাড়া। ফলে এক মুহূর্তের network drop-এ পুরো upload নষ্ট হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Server কীভাবে বোঝে কোন chunk কার সাথে যায়?"* → প্রতিটা chunk-এর সাথে একটা upload/session id যায়, সাথে chunk index; server id আর order দেখে জোড়া লাগায়।

**সম্পর্কিত:** [Q4 — offline](#q4) · [Q2 — networking](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. একটা Flutter app-এর জন্য push notification architecture end-to-end design করুন।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"App FCM (Firebase Cloud Messaging)-এ register করে একটা device token পায়, আর সেটা আমার backend-এ পাঠায়। কিছু ঘটলে আমার backend FCM-কে বলে ওই token-এ একটা notification পৌঁছে দিতে। App তিনটা অবস্থায় notification সামলায় — foreground, background আর terminated। Tap করলে deep link দিয়ে user সঠিক screen-এ যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি।**
Push অনেকটা ডাক সেবার মতো: আপনার app (দোকান) বন্ধ থাকলেও এটা user-এর দরজায় পৌঁছে দেয়। App ডাক সেবাকে তার ঠিকানা দিয়ে দেয় (device token)।

**ধাপ ২ — End-to-end flow।**

```
App → register with FCM → gets device token
App → send token to your backend (store it per user)
Event → your backend → calls FCM with token + payload → device shows notification
User taps → app opens / deep-links to the right screen
```

**ধাপ ৩ — App-এর তিনটা অবস্থা সামলান।**
- **Foreground** — আপনার code একটা in-app banner দেখায় (control আপনার হাতে)।
- **Background** — OS notification দেখায়; tap করলে app খোলে।
- **Terminated** — OS-ই দেখায়; tap করলে app cold-start হয়; সঠিক route-এ যেতে launch payload পড়ুন।

```dart
FirebaseMessaging.onMessage.listen(handleForeground);
FirebaseMessaging.onMessageOpenedApp.listen(handleTapFromBackground);
final initial = await FirebaseMessaging.instance.getInitialMessage(); // terminated অবস্থায় tap
```

**ধাপ ৪ — গুরুত্বপূর্ণ খুঁটিনাটি।**
- **Token refresh** — device token বদলে যেতে পারে; `onTokenRefresh`-এ listen করুন আর backend update করুন।
- **Permissions** — iOS (আর Android 13+)-এ user-এর অনুমতি চাইতে হয়; না দিলে সেটাও সুন্দরভাবে সামলান।
- **Data vs notification messages** — "notification" message OS নিজে দেখায়; "data" message-এ সিদ্ধান্ত আপনার app নেয়। নিজের মতো handling দরকার হলে data message ব্যবহার করুন।
- **Deep linking** — payload-এ একটা route থাকে, যাতে tap করলে সঠিক screen-এ পৌঁছায় ([Q15 Security](section-20-mobile-security-bn.md#q15))।

**Interviewer কেন জিজ্ঞেস করে:** প্রায় সব app-এ push থাকে; এটা platform আর lifecycle বোঝাপড়া যাচাই করে।

**সাধারণ ভুল:** শুধু foreground অবস্থাটা সামলানো আর background/terminated ভুলে যাওয়া। অথবা device token refresh হলে backend update না করা (ফলে notification চুপচাপ বন্ধ হয়ে যায়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এক user-এর একের বেশি device থাকলে কীভাবে পাঠাবেন?"* → প্রতি user-এর জন্য একের বেশি token রাখুন; সবগুলোতে পাঠান (অথবা FCM topic/user-based fan-out ব্যবহার করুন)।

**সম্পর্কিত:** [Q3 — chat (offline push)](#q3) · [Q15 (Security) — deep links](section-20-mobile-security-bn.md#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. একটা shopping cart feature design করুন (state, persistence, backend sync)।

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Cart থাকে app state হিসেবে (BLoC/Cubit/Riverpod), যাতে UI সাথে সাথে update হয়। এটা locally persist করা হয়, যাতে app restart-এর পরেও টিকে থাকে। আর backend-এ sync করা হয়, যাতে সেটা user-এর সাথে অন্য device-এও চলে যায়। আমি আগে locally update করব (optimistic), তারপর sync করব। একই user দুই device-এ cart বদলালে conflict handle করব।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটি layer।**

```
UI ◄─ state (Cubit) ◄─ local storage (survives restart) ◄─ backend (cross-device)
```

- **State** — বর্তমান cart ধরে রাখে; পরিবর্তন হলে UI rebuild হয়।
- **Local persistence** — cart save করুন (Hive/Drift), যাতে restart-এর পরেও থাকে, offline থাকলেও।
- **Backend sync** — cart server-side রাখুন, যাতে user অন্য device-এ গেলেও সেটা সাথে যায়।

**ধাপ ২ — Update flow (optimistic)।**
1. User "add to cart" চাপল → সাথে সাথে Cubit state update হবে (UI-তে দেখা যাবে)।
2. Local storage-এ save করুন।
3. Background-এ backend-এ sync করুন।
4. Sync fail করলে locally রেখে দিন, পরে আবার চেষ্টা করুন (offline-tolerant)।

**ধাপ ৩ — কঠিন অংশগুলো সামলান।**
- **Guest বনাম logged-in** — guest-দের জন্য local cart রাখুন; login-এর সময়ে সেটা server cart-এ merge করুন।
- **Conflict** — একই user দুই device-এ cart edit করে। একটা strategy ঠিক করুন: last-write-wins, বা quantity merge, বা server-authoritative।
- **Stock/price পরিবর্তন** — checkout-এর সময়ে price আর availability আবার validate করুন; জমানো cart-কে চোখ বুজে বিশ্বাস করবেন না।

**ধাপ ৪ — Trade-off।**
Optimistic local-first update সাথে সাথে হয় আর offline-এও কাজ করে। দাম হলো sync আর conflict handle করার ঝামেলা। শুধু server-backed cart সহজ, কিন্তু ধীর আর offline-এ ভেঙে পড়ে।

**Interviewer কেন জিজ্ঞেস করে:** Cart-এ state, persistence, sync আর conflict একসাথে আসে — ছোট কিন্তু বাস্তব একটা design।

**সাধারণ ভুল:** Cart শুধু memory-তে রাখা (restart-এ হারিয়ে যায়) বা শুধু server-এ রাখা (ধীর, offline-এ ভাঙা)। আর guest→login merge-এর কথা ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Login-এর সময়ে guest cart merge করবেন কীভাবে?"* → item গুলো একসাথে করুন, একই item হলে quantity যোগ করুন, তারপর merged cart server-এ push করুন।

**সম্পর্কিত:** [Q4 — offline-first](#q4) · [Q5 — auth](#q5) · [Q1 (State Mgmt)](section-03-state-management-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

# C. বড় স্কেলে Architecture

---

## <a id="q9"></a>9. Mobile app architecture-এ scalability-র জন্য কীভাবে design করেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Mobile-এ scalability মানে দুটো জিনিস: *codebase* আরও feature আর আরও developer সামলাতে পারে, আর *app* আরও বেশি data/user মসৃণভাবে সামলাতে পারে। Code-এর জন্য: পরিষ্কার layered architecture, modular feature package, আর dependency injection। Runtime-এর জন্য: pagination, caching, lazy loading, দক্ষ state management, আর ভারী কাজ isolate-এ সরিয়ে দেওয়া।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুই ধরনের scale।**
- **Codebase scale** — অনেক feature আর অনেক developer, তবু বিশৃঙ্খলা নেই।
- **Runtime scale** — বড় data আর অনেক user, তবু lag নেই।

**ধাপ ২ — Codebase scale করা।**
- **Layered/Clean Architecture**, যাতে দায়িত্ব আলাদা থাকে ([Q2 Architecture](section-13-architecture-patterns-bn.md#q2))।
- **Modular feature package**, যাতে team গুলো একসাথে কাজ করতে পারে ([Q10](#q10))।
- **Dependency injection**, testability আর সহজে বদলানোর জন্য।
- **Consistent pattern**, যাতে নতুন code পুরোনো code-এর মতোই দেখতে হয়।

**ধাপ ৩ — Runtime scale করা (device-এ)।**
- **Pagination** — একবারে 10,000 item load করবেন না; page ধরে load করুন।
- **Caching** — response/image cache করুন, network কমবে আর গতি বাড়বে।
- **Lazy loading** — `ListView.builder`, deferred import, শুধু যা দেখা যাচ্ছে তাই build করুন।
- **Efficient state** — যা বদলেছে শুধু সেটাই rebuild করুন (selector, `const`)।
- **Isolate** — ভারী parsing/computation UI thread থেকে সরিয়ে দিন।

**ধাপ ৪ — Backend interaction scale করা।**
- দক্ষ API (শুধু দরকারি field চান; GraphQL বা মাপে বানানো REST)।
- দ্রুত user action-এ backpressure/debounce (search-as-you-type)।
- ধীর বা fail হওয়া network সুন্দরভাবে সামলানো।

**Interviewer কেন জিজ্ঞেস করে:** Senior/lead role-এ এমন লোক দরকার, যাঁরা বৃদ্ধির কথা ভেবে design করেন, শুধু প্রথম version-এর কথা ভেবে নয়।

**সাধারণ ভুল:** শুধু আজকের ছোট data-র জন্য design করা — সব একবারে load, কোনো caching নেই। Data আর user বাড়লে এটা ভেঙে পড়ে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"বড় list-এ app ধীর লাগছে — কী check করবেন?"* → Lazy build (`ListView.builder`), `const`, rebuild scope, image caching, আর UI thread-এ ভারী কাজ আছে কি না।

**সম্পর্কিত:** [Q10 — বড় app](#q10) · [Q5 (Performance)](section-05-performance-bn.md#q1) · [Q2 (Architecture)](section-13-architecture-patterns-bn.md#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. 50+ screen আর 10+ developer-এর একটা Flutter app কীভাবে architect করবেন?

> Common · Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি modular, feature-based architecture ব্যবহার করব: প্রতিটা feature নিজের package, স্পষ্ট সীমানা সহ, আর সবাই মিলে common 'core' ও 'domain' package share করে। পুরোটা একটা monorepo-তে, melos দিয়ে manage করা। প্রতিটা feature-এর ভেতরে Clean Architecture (presentation/domain/data) আর DI। এতে team গুলো একসাথে কাজ করতে পারে, সীমানা মানা হয়, আর প্রতিটা feature-এর build ও test দ্রুত থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মূল সমস্যা: বিশৃঙ্খলা ছাড়া একসাথে কাজ।**
10+ developer থাকলে একটা বড় `lib/` folder মানে অবিরাম merge conflict আর জট পাকানো dependency। সমাধান হলো শক্ত সীমানা।

**ধাপ ২ — Modular feature package।**

```
app/                  (shell: wires features + navigation)
packages/
  core/               (networking, theming, utils — shared)
  domain/             (shared entities, repository interfaces)
  feature_auth/       feature_profile/   feature_orders/   ...
```

নিয়ম: feature গুলো `core`/`domain`-এর উপর নির্ভর করবে, **একে অন্যের উপর নয়** ([Q13 Architecture](section-13-architecture-patterns-bn.md#q13))।

**ধাপ ৩ — প্রতিটা feature-এর ভেতরে।**
Clean Architecture (presentation → domain → data) আর DI ([Q2 Architecture](section-13-architecture-patterns-bn.md#q2))। পুরো app-এ একটাই state management পছন্দ রাখুন (যেমন BLoC), যাতে যেকোনো developer যেকোনো feature পড়তে পারেন।

**ধাপ ৪ — Tooling আর process।**
- **melos** দিয়ে monorepo manage করা (package link করা, সব জায়গায় script চালানো)।
- **CI**, যেটা বদলে যাওয়া package গুলো build/test করে।
- **Shared standard** — lint rule, convention, একটা design system, আর প্রতিটা feature-এর স্পষ্ট মালিকানা।
- **Navigation** এক জায়গায় রাখা (যেমন `go_router`), যাতে feature গুলো একে অন্যের সাথে শক্ত করে বাঁধা না পড়ে।

**ধাপ ৫ — Trade-off।**
Modularization শুরুতে setup আর tooling-এর জটিলতা বাড়ায়। ছোট app-এ এটা বাড়াবাড়ি। কিন্তু 50+ screen আর 10+ dev-এর ক্ষেত্রে এটাই ঠিক করে দেয় — আপনি মসৃণভাবে বাড়বেন, নাকি conflict-এ ডুবে যাবেন।

**Interviewer কেন জিজ্ঞেস করে:** এটা senior/lead প্রশ্ন — team আর codebase scale করা নিয়ে, বুদ্ধি আর গঠন দেখার জন্য।

**সাধারণ ভুল:** একটাই বিশাল module (সবার conflict হয়), অথবা feature গুলো একে অন্যের internal import করে (আবার সেই জট)। আরেকটা ভুল — অসংগত pattern, ফলে প্রতিটা feature আলাদা ভাবে লেখা হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Feature গুলো একে অন্যের সাথে কথা বলে কীভাবে?"* → `core`/`domain`-এ থাকা shared abstraction দিয়ে, অথবা app shell-এর event/navigation layer দিয়ে — কখনোই সরাসরি import দিয়ে নয়।

**সম্পর্কিত:** [Q13 (Architecture) — modular](section-13-architecture-patterns-bn.md#q13) · [Q12 (Architecture) — monorepo](section-13-architecture-patterns-bn.md#q12) · [Q9 — scalability](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. অন্য Flutter app যেটা ব্যবহার করবে, এমন plugin বা SDK কীভাবে design করেন?

> Deeper · Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"SDK হলো *developer*-দের জন্য একটা product। তাই অগ্রাধিকার হলো পরিষ্কার ও স্থিতিশীল public API, ভালো documentation, আর user-দের কিছু না ভাঙা। আমি ছোট ও সুন্দর নামের একটা surface দেব, internal লুকিয়ে রাখব, error সুন্দরভাবে handle করব, null safety আর বর্তমান Flutter version support করব, আর semver দিয়ে version দেব — যাতে breaking change স্পষ্টভাবে জানা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — চিন্তার বদল: আপনার user হলো developer।**
App-এ user একজন মানুষ। SDK-তে user আরেকজন developer। তাঁর app ভাঙলে তিনি খুব রেগে যাবেন। তাই **stability আর স্পষ্টতা** সবার আগে।

**ধাপ ২ — পরিষ্কার public API design করুন।**
- **ছোট surface** দিন — শুধু যা user-এর দরকার; internal লুকিয়ে রাখুন (`_private` / `src/`)।
- **স্পষ্ট নাম** আর যুক্তিসঙ্গত default, যাতে শুরু করা সহজ হয়।
- API দিয়ে third-party type **বাইরে বের হতে দেবেন না** (wrap করুন), তাহলে internal অংশ স্বাধীনভাবে বদলাতে পারবেন।

```dart
// Public, ছোট, স্থিতিশীল:
class PaymentSdk {
  Future<PaymentResult> pay({required double amount}) async { /* ... */ }
}
// Internal অংশ src/-এ লুকানো, export করা হয়নি।
```

**ধাপ ৩ — মজবুতি আর compatibility।**
- **সুন্দরভাবে error handle** — typed result/exception ফেরত দিন, host app কখনোই crash করবেন না।
- **Null safety** আর বর্তমান Flutter/Dart version-এর support।
- **Platform support** — platform channel/Pigeon দিয়ে Android/iOS (আর দরকার হলে web) পরিষ্কারভাবে সামলান।
- **হঠাৎ আসা side effect নয়** — global state দখল করবেন না, host-এর setup নিয়ে ধরে নেবেন না।

**ধাপ ৪ — Documentation, versioning, testing।**
- **Docs + example** — একটা example app আর পরিষ্কার README; SDK বাঁচে বা মরে docs-এর উপর।
- **Semantic versioning** — breaking change-এর জন্য MAJOR, যাতে user নিরাপদে upgrade করতে পারেন ([Q8 SDLC](section-19-sdlc-bn.md#q8))।
- **Deprecation path** — সরানোর আগে পুরোনো API-কে `@deprecated` চিহ্ন দিন, সাথে পরামর্শ দিন।
- **পুঙ্খানুপুঙ্খ test** — অনেক app-এ install হয়ে থাকা জিনিস সহজে hotfix করা যায় না।

**Interviewer কেন জিজ্ঞেস করে:** এটা API design-এর পরিপক্বতা আর অন্য developer-দের প্রতি সহানুভূতি যাচাই করে — একটা senior/staff signal।

**সাধারণ ভুল:** বিশাল, ফাঁস হওয়া public API, যেটা internal দেখিয়ে দেয়। ফলে যেকোনো internal পরিবর্তনে user-দের কাজ ভেঙে যায়। অথবা কোনো docs/example নেই, তাই কেউ এটা নিতে পারে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Breaking change নিরাপদে করবেন কীভাবে?"* → আগে deprecate করুন, সাথে migration path দিন, তারপর MAJOR version বাড়ান, আর upgrade-এর কথা document করুন।

**সম্পর্কিত:** [Q12 — API versioning](#q12) · [Q5 (Clean Code) — CQS / clean API](section-16-clean-code-bn.md#q5) · [Q11 (OOP) — constructor](section-12-oop-principles-bn.md#q18)

[↑ উপরে ফিরুন](#toc)

---

# D. Cross-cutting concerns

---

## <a id="q12"></a>12. API versioning কী, আর mobile app-এ breaking API change কীভাবে handle করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"API versioning server-কে বদলানোর সুযোগ দেয়, অথচ user-এর phone-এ থাকা পুরোনো app version ভাঙে না। আমি API-তে version দিই (যেমন `/v1/`, `/v2/`) আর পুরোনো version চালু রাখি যতদিন না পুরোনো app-গুলো ফুরিয়ে যায়। Mobile-এর মূল সীমাবদ্ধতা: সবাইকে সাথে সাথে update করাতে পারবেন না। তাই backend-কে একসাথে অনেক app version support করতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Mobile-এ এটা কেন কঠিন।**
Web-এ সবাই সাথে সাথে নতুন version পায়। Mobile-এ user মাসের পর মাস **পুরোনো app version** চালায়। তাই একটা breaking API change ওই সব পুরোনো app crash করাবে — পুরোনো আর নতুন দুটোকেই একসাথে support করতে হবে।

**ধাপ ২ — কীভাবে version করবেন।**
- **URL versioning** — `/v1/users`, `/v2/users` (সবচেয়ে প্রচলিত, স্পষ্ট)।
- **Header versioning** — একটা version header।
পুরোনো app যতদিন `v1` ব্যবহার করে, ততদিন সেটা বাঁচিয়ে রাখুন; নতুন behaviour-এর জন্য `v2` যোগ করুন।

```
Old app  → /v1/orders  (still works)
New app  → /v2/orders  (new fields/behaviour)
```

**ধাপ ৩ — যেখানে পারেন, পরিবর্তনগুলো backward-compatible রাখুন।**
- একটা field **যোগ করা** সাধারণত নিরাপদ (পুরোনো app সেটা বাদ দেয়)।
- **সরানো/নাম বদলানো/type বদলানো** breaking — এর জন্য নতুন version লাগবে।
- Response এমনভাবে design করুন যেন client অচেনা field সহ্য করতে পারে।

**ধাপ ৪ — Force-update শেষ উপায় হিসেবে।**
যে breaking change এড়ানো যায় না (বা security-র জন্য), app চালু হওয়ার সময় একটা minimum supported version check করতে পারে আর "please update" screen দেখাতে পারে। খুব কম ব্যবহার করুন — এটা user-এর জন্য কঠিন বাধা।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি জানেন কি না যে mobile client-কে ইচ্ছেমতো update করানো যায় না — বাস্তব একটা সীমাবদ্ধতা, যেটা web developer-রা প্রায়ই ভুলে যান।

**সাধারণ ভুল:** একটা shared endpoint-এ breaking change করা, আর তাতে বাইরে থাকা সব পুরোনো app version ভেঙে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"পুরোনো version কতদিন রাখেন?"* → যতদিন না পুরোনো app version-এর ব্যবহার যথেষ্ট কমে যায় (analytics দিয়ে track করুন), তারপর নোটিশ দিয়ে deprecate করুন।

**সম্পর্কিত:** [Q8 (SDLC) — versioning](section-19-sdlc-bn.md#q8) · [Q11 — SDK versioning](#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. পুরো একটা Flutter app-এ error handling কীভাবে design করবেন — API failure থেকে user-এর চোখে পড়া message পর্যন্ত?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-21-system-design.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি error layer-এ layer-এ handle করি। Data layer নিচু স্তরের error (network, parsing) ধরে আর সেগুলোকে পরিষ্কার domain failure-এ বদলায়। State layer সেগুলোকে UI state-এ map করে (error state)। UI একটা বন্ধুত্বপূর্ণ, কাজে লাগার মতো message দেখায় — কখনোই raw exception নয়। আমি uncaught error-ও globally ধরি আর crash tool-এ report করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Layer ধরে প্রবাহ।**

```
API/DB error → Data layer (catch, wrap) → domain Failure
            → State (Cubit emits Error state) → UI shows friendly message
```

প্রতিটা layer error-টাকে পরের layer-এর জন্য সঠিক রূপে অনুবাদ করে।

**ধাপ ২ — Data layer: exception-কে typed failure-এ বদলান।**
Raw error (DioException, FormatException) ধরুন আর সেগুলোকে অর্থপূর্ণ domain result-এ বদলে ফেলুন — একটা sealed `Result`/`Either` অথবা নির্দিষ্ট failure type ([Q8 Clean Code](section-16-clean-code-bn.md#q8))।

```dart
Future<Result<User>> getUser() async {
  try {
    return Ok(await api.fetchUser());
  } on DioException catch (e) {
    return Err(e.type == DioExceptionType.connectionError
        ? NetworkFailure() : ServerFailure());
  }
}
```

**ধাপ ৩ — State layer: failure-কে UI state-এ map করুন।**
Cubit/BLoC একটা পরিষ্কার error state emit করে, সাথে user-বান্ধব message থাকে। ফলে UI শুধু সেটা render করে।

```dart
on failure → emit(FeedError('No internet. Pull to retry.'));
```

**ধাপ ৪ — UI: বন্ধুত্বপূর্ণ, কাজে লাগার মতো, আর সব জায়গায় একই রকম।**
- একটা **পরিষ্কার message** দেখান ("No internet — pull to retry"), কখনোই stack trace নয়।
- যেখানে সম্ভব একটা **action** দিন (retry button)।
- **একই রকম** error widget ব্যবহার করুন (একটা shared error view)।

**ধাপ ৫ — Global নিরাপত্তা জাল।**
যা কিছু ফাঁক গলে বেরিয়ে যায়, সেটা ধরুন আর report করুন:

```dart
FlutterError.onError = (details) => crashReporter.record(details);
PlatformDispatcher.instance.onError = (error, stack) { crashReporter.record(...); return true; };
```

ফলে হঠাৎ আসা crash-ও log হয় (secret মুছে দিয়ে, [Q5 Security](section-20-mobile-security-bn.md#q5)) আর app সুন্দরভাবে degrade করে।

**Interviewer কেন জিজ্ঞেস করে:** পুরো app জুড়ে error handling ঝকঝকে app-কে ঠুনকো app থেকে আলাদা করে; এটা architecture আর UX চিন্তা একসাথে যাচাই করে।

**সাধারণ ভুল:** User-কে raw exception দেখানো, প্রতি screen-এ আলাদা আলাদা ভাবে error handle করা, অথবা চুপচাপ error গিলে ফেলা (কোনো message নেই, কোনো report নেই)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Uncaught async error কোথায় ধরেন?"* → `PlatformDispatcher.instance.onError` (আর framework error-এর জন্য `FlutterError.onError`); দুটোই report করুন।

**সম্পর্কিত:** [Q8 (Clean Code) — result types](section-16-clean-code-bn.md#q8) · [Q4 (Networking) — global error handling](section-07-networking-storage-bn.md#q4) · [Q9 (SDLC) — production bugs](section-19-sdlc-bn.md#q9)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিউ)

Interview-এর সকালে এটা পড়ুন। আগে table, তারপর এক-লাইনের মনে করিয়ে দেওয়া কথাগুলো।

## ৫ ধাপের design framework

```
1. Requirements (functional + non-functional)
2. High-level architecture (the big boxes)
3. Data flow + state management
4. Mobile concerns (offline, storage, caching, network)
5. Trade-offs (alternatives + why)
```

## Transport বেছে নেওয়া

| দরকার | যা ব্যবহার করবেন |
|---|---|
| সাধারণ CRUD data | REST |
| Live, দুই-মুখী (chat, presence) | WebSocket |
| App বন্ধ থাকলেও server push | Push (FCM) |

## Design-এর মূল উপাদান

| বিষয় | চটজলদি উত্তর |
|---|---|
| Offline | local DB-ই source of truth, background-এ sync |
| Auth | secure storage-এ short access + refresh token |
| বড় upload | compress + chunk + retry + progress |
| বড় team | modular feature package + monorepo (melos) |
| Error | layer ধরে: data → state → বন্ধুত্বপূর্ণ UI + global catch |

## এক-লাইনের মনে করিয়ে দেওয়া কথা

- **আগে requirement পরিষ্কার করুন**; trade-off মুখে বলে বলে আলোচনা করুন। ([Q1](#q1))
- বেশির ভাগ data-র জন্য **REST**; real-time হলেই কেবল **WebSocket**। ([Q2](#q2))
- **Chat** = WebSocket + local DB + optimistic UI + reconnect/ordering। ([Q3](#q3))
- **Offline-first** = local DB-ই source of truth; UI সেটা watch করে। ([Q4](#q4))
- **Auth** = short access + refresh token, secure storage, silent refresh। ([Q5](#q5))
- **Upload** = compress, chunk, progress, retry; lifecycle টিকে থাকুক। ([Q6](#q6))
- **Push** = FCM token → backend → foreground/background/terminated handle করুন। ([Q7](#q7))
- **Cart** = state + local persistence + backend sync; login-এ merge করুন। ([Q8](#q8))
- **Scale** = pagination, caching, lazy loading, isolate; modular code। ([Q9](#q9), [Q10](#q10))
- **SDK** = ছোট stable API, ভেতরের জিনিস লুকান, docs, semver। ([Q11](#q11))
- **API versioning** — mobile-এ জোর করে update করানো যায় না; পুরোনো + নতুন দুটোই support করুন। ([Q12](#q12))
- **Error** = data → state → বন্ধুত্বপূর্ণ UI message + global crash catch। ([Q13](#q13))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: interviewer কীভাবে আরও গভীরে যান

Design interview trade-off নিয়ে খোঁড়াখুঁড়ি করে। মুখে বলে বলে অনুশীলন করুন:

1. *"Chat design করুন।"* → আগে পরিষ্কার করুন, তারপর WebSocket + local DB + optimistic UI; ordering আর reconnection নিয়ে আলোচনা করুন।
2. *"এবার এটা offline-এ কাজ করান।"* → message locally queue করুন, reconnect হলে পাঠান, বাদ পড়াগুলো আবার sync করুন।
3. *"REST না WebSocket?"* → সাধারণ data-র জন্য REST, শুধু যেখানে real-time দরকার সেখানেই WebSocket।
4. *"50টা screen, 10 জন developer — কীভাবে সাজাবেন?"* → modular feature package, melos দিয়ে monorepo, কঠোরভাবে boundary মানা।
5. *"একটা API call fail করল — user কী দেখে?"* → layer ধরে error handling দিয়ে একটা বন্ধুত্বপূর্ণ, কাজে লাগার মতো message (stack trace নয়)।

আগে পরিষ্কার করা, তারপর মুখে বলে বলে trade-off নিয়ে যুক্তি সাজানো — এই *process-টাই* mobile system-design interview জেতায়, remote হোক বা BD, দুই জায়গাতেই।

[↑ উপরে ফিরুন](#toc)
