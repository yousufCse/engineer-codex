# 📘 CHAPTER 1 — Internet ও HTTP
### "ইন্টারনেট কীভাবে কাজ করে — মূলনীতি থেকে HTTP পর্যন্ত"
#### Progress: [██░░░░░░░░░░░░░░░░░] 10%

[⬆ TOC](./table-of-contents.md) | [⬅ Chapter 0](./chapter-00-environment-setup.md) | [➡ Chapter 2](./chapter-02-javascript-backend.md)

---

## ইন্টারনেট কী — মৌলিক ধারণা

ইন্টারনেট হলো পৃথিবীজুড়ে পরস্পর সংযুক্ত কম্পিউটারের একটা বিশাল নেটওয়ার্ক। এটা কোনো একটা কোম্পানির মালিকানা নয়, কোনো একটা কেন্দ্রীয় সার্ভার নেই। এটা হলো একটা বিকেন্দ্রীভূত (decentralized) সিস্টেম যেখানে হাজারো ভিন্ন নেটওয়ার্ক একসাথে কাজ করে।

ইন্টারনেটের মূল ভিত্তি হলো **packet switching**। ডেটা পাঠানোর সময় সেটাকে ছোট ছোট packet-এ ভেঙে পাঠানো হয়। প্রতিটা packet আলাদাভাবে গন্তব্যে পৌঁছায় এবং সেখানে গিয়ে পুনরায় জোড়া লাগে। কোনো একটা রাস্তা বন্ধ থাকলে packet অন্য পথে যেতে পারে — এটাই ইন্টারনেটকে ব্যর্থতা-প্রতিরোধী (fault-tolerant) করে।

---

## OSI Model — নেটওয়ার্কের স্তরীয় কাঠামো

নেটওয়ার্ক যোগাযোগ বোঝার জন্য OSI (Open Systems Interconnection) model ব্যবহার করা হয়। এটা ৭টা স্তরে ভাগ করা — প্রতিটা স্তর নির্দিষ্ট কাজ করে এবং উপরের স্তরকে service প্রদান করে।

**Layer 7 — Application Layer:** এটা সবচেয়ে উপরের স্তর। ব্যবহারকারী যে applications ব্যবহার করে সেগুলো এই স্তরে কাজ করে। HTTP, HTTPS, FTP, SMTP, DNS — এই protocols এই স্তরে থাকে। Backend developer হিসেবে তুমি মূলত এই স্তরেই কাজ করবে।

**Layer 6 — Presentation Layer:** ডেটার format, encoding, এবং encryption এই স্তরে হয়। SSL/TLS encryption এই স্তরে কাজ করে। JSON, XML serialization এখানে।

**Layer 5 — Session Layer:** দুটো application-এর মধ্যে session (conversation) শুরু, রক্ষণাবেক্ষণ, এবং শেষ করার দায়িত্ব এই স্তরের।

**Layer 4 — Transport Layer:** End-to-end data delivery নিশ্চিত করে। TCP এবং UDP এই স্তরে থাকে। Port number এই স্তরে ব্যবহার হয়।

**Layer 3 — Network Layer:** ডেটা packet-কে source থেকে destination-এ route করে। IP protocol এই স্তরে। IP address এই স্তরের।

**Layer 2 — Data Link Layer:** একই নেটওয়ার্কের দুটো device-এর মধ্যে সরাসরি communication। MAC address এই স্তরে।

**Layer 1 — Physical Layer:** Physical medium — তার, fiber optic cable, বা radio wave। Bit (0 এবং 1) পাঠানো এই স্তরের কাজ।

Web development-এর জন্য সবচেয়ে গুরুত্বপূর্ণ হলো Layer 4 (TCP/UDP), Layer 3 (IP), এবং Layer 7 (HTTP)।

---

## TCP/IP — ইন্টারনেটের মূল ভাষা

TCP/IP আসলে দুটো আলাদা protocol-এর সমষ্টি।

**IP (Internet Protocol):**

প্রতিটা device যখন ইন্টারনেটে সংযুক্ত হয়, তাকে একটা unique address দেওয়া হয় — এটাই IP address। IPv4 address হলো চারটা সংখ্যার সমষ্টি (যেমন 192.168.1.1)। কিন্তু বিশ্বে device-এর সংখ্যা বাড়ায় IPv4 address শেষ হয়ে যাচ্ছে, তাই IPv6 তৈরি হয়েছে।

IP protocol ডেটা packet route করার কাজ করে — প্রতিটা packet-এ source IP এবং destination IP থাকে। Router এই IP দেখে packet কোথায় পাঠাতে হবে সেটা ঠিক করে।

IP protocol **connectionless** — প্রতিটা packet স্বাধীনভাবে যায়, পৌঁছাবে কিনা বা সঠিক ক্রমে যাবে কিনা নিশ্চয়তা নেই।

**TCP (Transmission Control Protocol):**

TCP IP-এর উপরে কাজ করে এবং **reliable, ordered, error-checked delivery** নিশ্চিত করে।

TCP connection তৈরিতে **Three-way handshake** হয়:
১. Client পাঠায় SYN (synchronize)
২. Server পাঠায় SYN-ACK (synchronize-acknowledge)
৩. Client পাঠায় ACK (acknowledge)

এই handshake-এর পর connection প্রতিষ্ঠিত হয়। Data পাঠানোর পর receiver ACK পাঠায়। ACK না পেলে sender আবার পাঠায়।

**UDP (User Datagram Protocol):**

UDP TCP-এর মতো reliable নয় — কোনো handshake নেই, কোনো ACK নেই। কিন্তু এটা অনেক দ্রুত। Video streaming, online gaming, DNS query-তে UDP ব্যবহার হয় কারণ সেখানে কিছু packet হারিয়ে গেলেও চলে, কিন্তু দেরি করলে চলে না।

---

## DNS — নামের আড়ালে সংখ্যা

তুমি browser-এ `google.com` টাইপ করো। কিন্তু computer IP address বোঝে, domain name নয়। DNS (Domain Name System) হলো ইন্টারনেটের phone book — domain name-কে IP address-এ translate করে।

**DNS resolution কীভাবে হয়:**

১. তুমি browser-এ `google.com` টাইপ করো।
২. Browser প্রথমে নিজের cache চেক করে — আগে কখনো গিয়েছিলে কিনা।
৩. না পেলে OS-এর DNS cache চেক করে।
৪. না পেলে configured DNS resolver-কে (সাধারণত ISP-এর) জিজ্ঞেস করে।
৫. DNS resolver root nameserver-এর কাছে যায়।
৬. Root nameserver .com TLD nameserver-এর address বলে।
৭. TLD nameserver google-এর authoritative nameserver-এর address বলে।
৮. Authoritative nameserver google.com-এর IP বলে।
৯. Browser সেই IP-তে HTTP request পাঠায়।

এই পুরো প্রক্রিয়া milliseconds-এ হয়। DNS record cache-এ রাখা হয় TTL (Time To Live) অনুযায়ী।

---

## HTTP — Web-এর ভাষা

HTTP (HyperText Transfer Protocol) হলো client এবং server-এর মধ্যে যোগাযোগের নিয়ম। এটা Application Layer-এর protocol।

HTTP **stateless** — প্রতিটা request সম্পূর্ণ স্বাধীন। Server আগের request মনে রাখে না। আজ login করলে কাল আবার login করতে হবে — যদি না কোনো mechanism (cookie, session, token) ব্যবহার করা হয়।

HTTP **text-based** — request এবং response human-readable text হিসেবে পাঠানো হয়।

**HTTP Request-এর গঠন:**

একটা HTTP request চারটা অংশে ভাগ:

**Request Line:** কোন method (GET, POST etc.), কোন URL, HTTP version।

**Headers:** Request সম্পর্কে metadata। `Host` (কোন server), `Content-Type` (data কোন format-এ), `Authorization` (authentication token), `Accept` (client কোন format চায়) ইত্যাদি।

**Blank Line:** Headers এবং body-এর মধ্যে বাধ্যতামূলক blank line।

**Body (optional):** Actual data। GET request-এ সাধারণত body থাকে না। POST/PUT-এ body-তে data থাকে।

**HTTP Response-এর গঠন:**

**Status Line:** HTTP version, status code, status message।

**Headers:** Response metadata। `Content-Type`, `Content-Length`, `Set-Cookie` ইত্যাদি।

**Body:** Server যে data পাঠাচ্ছে — HTML, JSON, image ইত্যাদি।

---

## HTTP Methods — CRUD-এর ভাষা

HTTP Methods (বা verbs) বলে request-এর উদ্দেশ্য কী।

**GET:** Data retrieve করার জন্য। Server-এর কোনো state পরিবর্তন হয় না। GET request idempotent — একই request বার বার পাঠালে result একই থাকে। URL-এ data visible থাকে। Browser bookmark করা যায়।

**POST:** নতুন resource তৈরি করার জন্য। Body-তে data পাঠানো হয়। POST idempotent নয় — একই request বার বার পাঠালে বার বার নতুন resource তৈরি হতে পারে।

**PUT:** Existing resource সম্পূর্ণভাবে replace করার জন্য। পুরো resource পাঠাতে হয়।

**PATCH:** Resource-এর কিছু অংশ update করার জন্য। শুধু পরিবর্তিত অংশ পাঠাতে হয়।

**DELETE:** Resource মুছে ফেলার জন্য।

**HEAD:** GET-এর মতো, কিন্তু শুধু headers ফেরত পাঠায়, body নয়। File size বা existence check করতে ব্যবহার হয়।

**OPTIONS:** Server কোন methods support করে সেটা জানতে। CORS preflight request-এ ব্যবহার হয়।

---

## HTTP Status Codes — Server কী বলছে?

Status code তিনটা সংখ্যার। প্রথম সংখ্যা category নির্দেশ করে:

**1xx — Informational:** Request receive হয়েছে, processing চলছে। `100 Continue` — server বলছে request এগিয়ে পাঠাও।

**2xx — Success:** Request সফলভাবে process হয়েছে।
- `200 OK`: সাধারণ সাফল্য।
- `201 Created`: নতুন resource তৈরি হয়েছে (POST response-এ)।
- `204 No Content`: সফল, কিন্তু ফেরত দেওয়ার কিছু নেই (DELETE response-এ)।

**3xx — Redirection:** Request অন্য URL-এ redirect করতে হবে।
- `301 Moved Permanently`: Resource চিরতরে নতুন URL-এ চলে গেছে।
- `304 Not Modified`: Cache valid আছে — browser নতুন করে download না করে cache ব্যবহার করতে পারে।

**4xx — Client Error:** Client-এর পাঠানো request-এ সমস্যা।
- `400 Bad Request`: Request malformed — সঠিক format-এ নয়।
- `401 Unauthorized`: Authentication দরকার কিন্তু নেই বা invalid।
- `403 Forbidden`: Authenticated কিন্তু permission নেই।
- `404 Not Found`: Resource পাওয়া যায়নি।
- `409 Conflict`: Resource ইতিমধ্যে আছে (duplicate)।
- `422 Unprocessable Entity`: Format ঠিক আছে কিন্তু validation fail।
- `429 Too Many Requests`: Rate limit অতিক্রম করেছে।

**5xx — Server Error:** Server-এর কোনো সমস্যা।
- `500 Internal Server Error`: Unhandled exception।
- `502 Bad Gateway`: Upstream server error।
- `503 Service Unavailable`: Server temporarily unavailable।

---

## HTTPS — HTTP এর নিরাপদ সংস্করণ

HTTP-এ ডেটা plaintext-এ যায় — যে কেউ network traffic sniff করে পড়তে পারে। HTTPS হলো HTTP over TLS (Transport Layer Security)।

**TLS Handshake কীভাবে হয়:**

১. Client, server-এ connection শুরু করে এবং নিজের supported TLS version এবং cipher suite জানায়।
২. Server তার SSL certificate পাঠায়। Certificate-এ server-এর public key আছে।
৩. Client Certificate Authority (CA) দিয়ে certificate verify করে — এটা কি legitimate server?
৪. Client একটা session key তৈরি করে এবং server-এর public key দিয়ে encrypt করে পাঠায়।
৫. Server তার private key দিয়ে decrypt করে session key পায়।
৬. এখন উভয়েই একই session key জানে — এই symmetric key দিয়ে পরবর্তী সব communication encrypt হয়।

এই process-এ **asymmetric encryption** (public/private key) ব্যবহার হয় session key বিনিময়ের জন্য। তারপর দ্রুততর **symmetric encryption** ব্যবহার হয় actual data transfer-এর জন্য।

---

## REST — Architecture Style, Protocol নয়

REST (Representational State Transfer) হলো web service design করার একটা architectural style — Roy Fielding তার 2000 সালের PhD dissertation-এ এটা প্রস্তাব করেছিলেন।

REST কোনো protocol বা standard নয়। এটা constraints বা নীতির সমষ্টি।

**REST-এর মূল নীতিগুলো:**

**Stateless:** Server প্রতিটা request-কে সম্পূর্ণ স্বাধীন মনে করে। Client-এর কোনো context server মনে রাখে না। প্রতিটা request-এ সব প্রয়োজনীয় তথ্য থাকতে হবে (authentication token সহ)। এটা server scaling সহজ করে — যেকোনো server instance যেকোনো request handle করতে পারে।

**Client-Server Separation:** Client (যে data চায়) এবং server (যে data দেয়) আলাদা। Client জানে না server কোন database ব্যবহার করে। Server জানে না client কীভাবে data display করে। উভয় পক্ষ স্বাধীনভাবে পরিবর্তন করতে পারে।

**Uniform Interface:** সব resource-এ একই ধরনের interface। Resource URL দিয়ে identify হয়। Resource নিজেকে represent করে (JSON/XML)। Representation দিয়ে resource modify করা যায়।

**Cacheable:** Server response cache করা যাবে কিনা সেটা indicate করে। Cacheable response client বা intermediate proxy-তে store থাকে — পরের request-এ server-এ না গিয়ে cache থেকে পাওয়া যায়।

**Layered System:** Client জানে না সে সরাসরি server-এর সাথে কথা বলছে নাকি intermediary (load balancer, cache server)-এর সাথে।

**REST API vs RESTful API পার্থক্য:**

অনেক API নিজেকে REST বলে কিন্তু সব REST constraint মানে না। পুরোপুরি REST constraint মেনে চলে এমন API-কে RESTful বলে। বাস্তবে বেশিরভাগ "REST API" partially RESTful।

---

## HTTP Versions — বিবর্তন

**HTTP/1.0 (1996):** প্রতিটা request-এর জন্য নতুন TCP connection। Request complete হলে connection বন্ধ। একটা page-এ ১০০টা resource থাকলে ১০০টা TCP handshake।

**HTTP/1.1 (1997):** Keep-alive connection — একই TCP connection-এ একাধিক request। Pipelining — response-এর জন্য না থেকে পরের request পাঠানো যায়। তবে Head-of-line blocking সমস্যা থাকে।

**HTTP/2 (2015):** Binary protocol — text-এর বদলে binary frame। Multiplexing — একই connection-এ একাধিক request/response parallel-এ। Header compression — একই header বার বার পাঠানো হয় না। Server push — client request করার আগেই server resource পাঠাতে পারে।

**HTTP/3 (2022):** TCP-এর বদলে QUIC protocol (UDP-এর উপরে)। Head-of-line blocking সম্পূর্ণ দূর হয়। Connection migration — IP পরিবর্তন হলেও connection maintain থাকে।

---

## মূল উপলব্ধি

HTTP বোঝাটা backend developer-এর জন্য যেমন chemistry বোঝা pharmacist-এর জন্য। তুমি Express বা NestJS দিয়ে API লিখলেও আসলে HTTP request handle করছো। Status code কেন 200 বা 201 — এটা জানলে আরো thoughtful API design করা যায়। HTTPS কীভাবে কাজ করে জানলে security সম্পর্কে সচেতন থাকা সহজ হয়।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Chapter 0](./chapter-00-environment-setup.md) | [➡ Chapter 2](./chapter-02-javascript-backend.md)
