# Section 20 — Mobile & App Security

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা** সহ, আর **link করা** — যাতে আপনি এদিক-ওদিক লাফ দিয়ে ধীরে ধীরে প্রস্তুতি নিতে পারেন। যেখানে দরকার সেখানে code/config দেওয়া আছে।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-20-mobile-security-bn.md](../software-engineer-flutter/section-20-mobile-security.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code সহ ধাপে ধাপে ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — যুক্ত প্রশ্নগুলোতে যান · **উপরে ফিরুন** — index-এ ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** Security-র ক্ষেত্রে আগে *threat*-টার নাম বলুন, তারপর *defense*। "একজন attacker SharedPreferences থেকে token পড়ে ফেলতে পারে, তাই আমি secure storage ব্যবহার করি" — শুধু একটা tool-এর নাম বলার চেয়ে এটা অনেক ভালো।

---

<a id="toc"></a>

## সূচিপত্র

**A. ভিত্তি**
1. [OWASP Mobile Top 10](#q1) · *Common*
2. [Encryption at rest বনাম in transit](#q2) · *Common*

**B. Secret নিরাপদে রাখা**
3. [SharedPreferences বনাম Secure Storage](#q3) · *Very common*
4. [API key কখনোই hardcode করবেন না](#q4) · *Very common*
5. [Sensitive data log করবেন না](#q5) · *Common*

**C. Network security**
6. [Certificate pinning](#q6) · *Common*
7. [Man-in-the-Middle (MITM) attack](#q7) · *Common*
8. [SQL injection (mobile)](#q8) · *Common*

**D. Authentication**
9. [Access token বনাম refresh token](#q9) · *Very common*
10. [OAuth 2.0 + PKCE](#q10) · *Common*
11. [JWT — গঠন ও verification](#q11) · *Very common*
12. [Biometric authentication](#q12) · *Common*

**E. App hardening**
13. [Code obfuscation](#q13) · *Common*
14. [Root / jailbreak detection](#q14) · *Common*
15. [Deep link hijacking](#q15) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---

<a id="study-plan"></a>

## ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — ভিত্তি (এখান থেকে শুরু করুন)।**
→ [Q1 OWASP Top 10](#q1) · [Q2 At rest বনাম in transit](#q2)

**পর্যায় ২ — Secret (সবচেয়ে বেশি জিজ্ঞেস করা হয়)।**
→ [Q3 Secure storage](#q3) · [Q4 API key](#q4) · [Q5 Logging](#q5)

**পর্যায় ৩ — Authentication।**
→ [Q9 Token](#q9) · [Q11 JWT](#q11) · [Q10 OAuth/PKCE](#q10) · [Q12 Biometrics](#q12)

**পর্যায় ৪ — Network defense।**
→ [Q6 Cert pinning](#q6) · [Q7 MITM](#q7) · [Q8 SQL injection](#q8)

**পর্যায় ৫ — App hardening।**
→ [Q13 Obfuscation](#q13) · [Q14 Root detection](#q14) · [Q15 Deep link](#q15)

**সময় কম?** দেখে নিন [Q1](#q1) · [Q3](#q3) · [Q4](#q4) · [Q9](#q9) · [Q11](#q11), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. ভিত্তি

---

<a id="q1"></a>
## 1. OWASP Mobile Top 10 কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"OWASP Mobile Top 10 হলো mobile app-এর সবচেয়ে গুরুতর security ঝুঁকিগুলোর industry-standard তালিকা। এতে থাকে insecure data storage, দুর্বল authentication, insecure communication, আর দুর্বল code protection-এর মতো বিষয়। প্রতিটা mobile security review এই checklist থেকেই শুরু হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা আসলে কী।**
OWASP (Open Worldwide Application Security Project) সবচেয়ে সাধারণ ও বিপজ্জনক mobile ঝুঁকিগুলোর একটা ranked তালিকা প্রকাশ করে। ফলে team জানে কোন জিনিস থেকে বাঁচতে হবে।

**ধাপ ২ — প্রধান category-গুলো (এখনকার মূল থিম)।**

| ঝুঁকি | সহজ ভাষায় |
|---|---|
| Improper credential usage | hardcode করা key, দুর্বল token handling ([Q4](#q4)) |
| Insecure data storage | plain storage-এ secret রাখা ([Q3](#q3)) |
| Insecure communication | HTTPS নেই / pinning নেই ([Q6](#q6), [Q7](#q7)) |
| Insufficient authentication | দুর্বল login, MFA নেই ([Q9](#q9)) |
| Insufficient cryptography | দুর্বল বা ভুলভাবে ব্যবহার করা encryption ([Q2](#q2)) |
| Insecure authorization | access check-এর জন্য client নিজেকেই বিশ্বাস করে |
| Poor code quality / tampering | obfuscation বা integrity check নেই ([Q13](#q13)) |
| Reverse engineering | সহজেই decompile করে পড়ে ফেলা যায় ([Q13](#q13)) |
| Extraneous functionality | পড়ে থাকা debug/test backdoor |

**ধাপ ৩ — বারবার আসা শিক্ষা।**
বেশিরভাগ mobile ঝুঁকি শেষমেশ তিনটা কথায় দাঁড়ায়: **device-কে বিশ্বাস করবেন না**, **at rest আর in transit দুই অবস্থাতেই data রক্ষা করুন**, আর **app-এর ভেতরে কখনোই secret রাখবেন না**। App চলে এমন একটা device-এ, যেটা attacker-এর পুরো নিয়ন্ত্রণে থাকতে পারে।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় mobile security নিয়ে আপনার একটা গোছানো ধারণা আছে, শুধু এলোমেলো টিপস নয়।

**সাধারণ ভুল:** Client-কে বিশ্বাসযোগ্য ধরে নেওয়া। App-এর ভেতরের সবকিছু পরীক্ষা করে দেখা সম্ভব। আসল security check server-এও থাকতেই হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter app-এ কোনটা সবচেয়ে বেশি দেখা যায়?"* → Insecure data storage আর hardcode করা secret — দুটোতেই ভুল করা সহজ।

**সম্পর্কিত:** [Q2 — encryption](#q2) · [Q3 — secure storage](#q3) · [Q4 — API key](#q4)

[↑ উপরে ফিরুন](#toc)

---

<a id="q2"></a>
## 2. Encryption at rest আর encryption in transit-এর পার্থক্য কী?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Encryption in transit data-কে রক্ষা করে যখন সেটা network দিয়ে যাচ্ছে — মানে HTTPS/TLS। Encryption at rest data-কে রক্ষা করে যখন সেটা device বা server-এ জমা থাকে — যেমন encrypted database বা secure storage। দুটোই দরকার: TLS তারের উপর আড়ি পাতা ঠেকায়, আর at-rest encryption চুরি যাওয়া device থেকে data ফাঁস হওয়া ঠেকায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — রক্ষা করার দুটো আলাদা মুহূর্ত।**
- **In transit** — app আর server-এর মাঝে data চলাচল করছে (রাস্তায় চলা বর্ম-লাগানো গাড়ি)।
- **At rest** — data storage-এ পড়ে আছে (বিল্ডিংয়ের ভেতরে তালাবদ্ধ সিন্দুক)।

**ধাপ ২ — In transit = HTTPS/TLS।**
সব network call-এ `https://` ব্যবহার করতেই হবে। TLS data-কে encrypt করে। ফলে কেউ connection ধরে ফেললেও এলোমেলো byte দেখে, আপনার token বা user data নয়।

```dart
// সবসময় HTTPS; আসল data-র জন্য কখনোই plain http নয়
final res = await dio.get('https://api.example.com/user');
```

**ধাপ ৩ — At rest = encrypted storage।**
Device-এ sensitive data অবশ্যই encrypt করা থাকতে হবে। তাহলে চুরি যাওয়া বা rooted phone থেকে data ফাঁস হবে না:
- Token/password → `flutter_secure_storage` (OS keychain/keystore) ([Q3](#q3))।
- Local database → encrypt করুন (যেমন SQLCipher)।

**ধাপ ৪ — দুটোই লাগবে।**
শুধু TLS দিয়ে লাভ নেই, যদি token-টা পরে disk-এ plain text-এ জমা হয়। আবার শুধু at-rest encryption-এও লাভ নেই, যদি সেটা plain HTTP দিয়ে পাঠানো হয়। Defense in depth দুই মুহূর্তকেই ঢেকে রাখে।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি data-র পুরো জীবনচক্র জুড়ে সুরক্ষা দেন কি না, শুধু একটা অংশে নয়।

**সাধারণ ভুল:** HTTPS ব্যবহার করা, কিন্তু token রাখা plain SharedPreferences-এ — তারের উপর নিরাপদ, disk-এ উন্মুক্ত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"TLS কী?"* → HTTPS-এর পেছনের protocol, যেটা connection-কে encrypt আর authenticate করে।

**সম্পর্কিত:** [Q3 — secure storage](#q3) · [Q6 — certificate pinning](#q6) · [Q7 — MITM](#q7)

[↑ উপরে ফিরুন](#toc)

---

# B. Secret নিরাপদে রাখা

---

<a id="q3"></a>
## 3. Token রাখার জন্য SharedPreferences কেন নিরাপদ নয়? Flutter Secure Storage কীভাবে ব্যবহার করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"SharedPreferences data রাখে plain text-এ — rooted Android device-এ বা backup-এর মাধ্যমে যে কেউ সেটা পড়তে পারে। তাই এতে কখনোই token, password বা ব্যক্তিগত data রাখা যাবে না। Secret-এর জন্য আমি `flutter_secure_storage` ব্যবহার করি। এটা সেগুলো রাখে iOS Keychain আর Android Keystore/EncryptedSharedPreferences-এ, যার পেছনে থাকে OS-level encryption।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Secret-এর জন্য SharedPreferences কেন অনিরাপদ।**
এটা লেখে একটা সাধারণ XML/plist file-এ। Rooted বা jailbroken device-এ, অথবা device backup-এর মাধ্যমে সেই file সরাসরি পড়া যায়। Theme setting-এর জন্য ঠিক আছে; token-এর জন্য কখনোই নয়।

**ধাপ ২ — নিরাপদ উপায়: flutter_secure_storage।**

```dart
final storage = FlutterSecureStorage();

// Token নিরাপদে save করুন
await storage.write(key: 'auth_token', value: token);

// আবার পড়ুন
final token = await storage.read(key: 'auth_token');

// Logout-এ মুছে ফেলুন
await storage.delete(key: 'auth_token');
```

ভেতরে এটা ব্যবহার করে **iOS Keychain** আর **Android Keystore** (বা EncryptedSharedPreferences) — hardware-backed encryption, যেটা OS নিজে সামলায়।

**ধাপ ৩ — কোন data কোথায় রাখবেন।**

| Data | Storage |
|---|---|
| Token, password, PII | `flutter_secure_storage` |
| Theme, language, flag | `SharedPreferences` (ঠিক আছে) |
| বড় structured data | encrypted database ([Q2](#q2)) |

**ধাপ ৪ — Secure storage-ও জাদু নয়।**
পুরোপুরি compromised (rooted) device-এ কখনো কখনো এতেও আক্রমণ করা যায়। Secure storage-এর সাথে short-lived token মিলিয়ে ব্যবহার করুন ([Q9](#q9))। তাহলে ফাঁস হওয়া token দ্রুত expire হয়ে যাবে।

**Interviewer কেন জিজ্ঞেস করে:** Insecure storage হলো সবচেয়ে সাধারণ mobile দুর্বলতাগুলোর একটা। তাঁরা দেখতে চান আপনি জানেন secret-এর জায়গা কোথায়।

**সাধারণ ভুল:** "সহজ বলে" auth token SharedPreferences-এ রাখা। এটা একটা ক্লাসিক ও গুরুতর leak।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Secure storage কি 100% নিরাপদ?"* → না — এটা অনেক শক্তিশালী, কিন্তু এর সাথে short token lifetime আর server-side check রাখুন।

**সম্পর্কিত:** [Q2 — at rest](#q2) · [Q9 — token](#q9) · [Q14 — root detection](#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q4"></a>
## 4. Flutter-এ API key কখনোই hardcode করা উচিত নয় কেন, আর নিরাপদ বিকল্প কী কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"App-এর ভেতরে compile হওয়া যেকোনো জিনিস decompile করে বের করা যায় — তাই hardcode করা key আসলে public। তাই secret কখনোই Dart source-এ রাখবেন না, git-এও commit করবেন না। নিরাপদ বিকল্প: `--dart-define` দিয়ে build-time-এ value pass করা, আসল secret এমন backend-এ রাখা যেটাকে app call করে, আর সত্যিই sensitive key হলে সেটা client-এ একেবারেই না আনা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Hardcode করা কেন অনিরাপদ।**
Ship করা app unzip করে decompile করা যায়। ভেতরের string-গুলো — যেমন `const apiKey = 'sk_live_...'` — পড়ে ফেলা যায়। এটা অনেকটা প্রকাশ্য দেয়ালে নিজের password লিখে রাখার মতো।

```dart
// এটা কখনোই করবেন না:
const apiKey = 'sk_live_123secret'; // app-এর ভেতরেই ship হয়, বের করা যায়
```

**ধাপ ২ — ভালো: --dart-define দিয়ে build-time injection।**
Key source code-এ রাখবেন না; build-এর সময় pass করুন (আর CI secrets-এ রাখুন):

```bash
flutter build apk --dart-define=API_KEY=$API_KEY
```

```dart
const apiKey = String.fromEnvironment('API_KEY'); // build-এর সময় inject হয়
```

এতে key git-এর বাইরে থাকে। কিন্তু খেয়াল রাখুন: value কিন্তু build হওয়া binary-তেই থাকে। তাই এটা শুধু কম sensitive key-এর জন্য উপযুক্ত।

**ধাপ ৩ — সবচেয়ে ভালো: আসল secret server-এ রাখুন।**
সত্যিই sensitive কিছুর জন্য (payment secret, admin key), app-এর *আপনার নিজের* backend-কে call করা উচিত। Backend-ই secret ধরে রাখে আর third party-র সাথে কথা বলে। Secret কখনোই device-এ ship হয় না।

```
App → your backend (holds the secret) → third-party API
```

**ধাপ ৪ — সাথে: key-গুলো restrict করুন।**
যে key app-এ রাখতেই হবে (যেমন কিছু map/analytics key), সেগুলো provider-এর দিকে lock করে দিন — app bundle ID, platform আর API scope দিয়ে restrict করুন — তাহলে leak হওয়া key দিয়ে বেশি কিছু করা যাবে না।

**Interviewer কেন জিজ্ঞেস করে:** Hardcode করা secret খুব সাধারণ আর গুরুতর একটা leak; তাঁরা দেখতে চান আপনি বোঝেন কি না যে client কোনো secret লুকিয়ে রাখতে পারে না।

**সাধারণ ভুল:** ভাবা যে `--dart-define` বা `.env` key-টা *লুকিয়ে* রাখে। এটা key-কে source control-এর বাইরে রাখে, কিন্তু binary-তে থেকেই যায় — সত্যিই sensitive secret-এর জায়গা server-এ।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা key commit করে ফেলেছেন — এখন কী?"* → সাথে সাথে rotate করুন (ধরে নিন এটা compromised) আর git history থেকে মুছে ফেলুন ([Q14 Git](section-17-git-bn.md#q14))।

**সম্পর্কিত:** [Q1 — OWASP](#q1) · [Q3 — secure storage](#q3) · [Q14 (Git) — .gitignore/secrets](section-17-git-bn.md#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q5"></a>
## 5. Sensitive data log করা কেন বিপজ্জনক, আর এটা কীভাবে আটকাবেন?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Log প্রায়ই device-এ পড়া যায়, crash tool সেগুলো ধরে রাখে, বা third-party service-এ চলে যায় — তাই token, password বা personal data log করলে সেটা leak হয়ে যায়। সমাধান: secret কখনোই log করব না, log করার আগে sensitive field মুছে দেব, আর release build-এ verbose logging বন্ধ রাখব।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Log কেন leak করে।**
- Android logcat root করা device-এ অন্য tool দিয়ে পড়া যায়।
- Crash reporter (Crashlytics/Sentry) log ধরে নিয়ে device-এর বাইরে পাঠায়।
- Log শেষে এমন dashboard-এ যায় যেটা অনেকে দেখতে পারেন।

```dart
// বিপজ্জনক: token এখন log আর crash report-এ বসে আছে
print('Logging in with token: $token');
```

**ধাপ ২ — এটা আটকান।**
- token, password, পুরো card number বা PII **কখনোই log করবেন না**।
- Log করার আগে sensitive field **mask/scrub করুন**:

```dart
String mask(String s) => s.length <= 4 ? '****' : '****${s.substring(s.length - 4)}';
log('Card ending ${mask(cardNumber)}'); // ****1234 log হয়, পুরো number নয়
```

**ধাপ ৩ — Release-এ logging কমিয়ে দিন।**
Log level ব্যবহার করুন আর production build-এ debug logging বন্ধ করুন। তাহলে verbose log ship হবে না।

```dart
if (kDebugMode) log(detailedInfo); // শুধু debug build-এ
```

**ধাপ ৪ — Crash tool-কে scrub করার জন্য configure করুন।**
Crashlytics/Sentry এমনভাবে setup করুন যেন পাঠানোর আগে sensitive key বাদ দিয়ে দেয়। তাহলে ভুল করে log হলেও secret device ছেড়ে যাবে না।

**Interviewer কেন জিজ্ঞেস করে:** ভুল করে log করা খুব সহজ আর সাধারণ একটা leak; তাঁরা দেখেন আপনি log-কে সত্যিকারের attack surface হিসেবে নিচ্ছেন কি না।

**সাধারণ ভুল:** Debug করার সময় request/response body `print` করা (যেগুলোতে token বা PII থাকে) আর সেটা রেখে দেওয়া, অথবা production-এ verbose log ship করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Production-এ log কোথায় যায়?"* → Crash reporter আর analytics-এ — তাই যা log করবেন তা device ছেড়ে যেতে পারে।

**সম্পর্কিত:** [Q3 — secure storage](#q3) · [Q1 — OWASP](#q1)

[↑ উপরে ফিরুন](#toc)

---

# C. Network security

---

<a id="q6"></a>
## 6. Certificate pinning কী, এটা কেন গুরুত্বপূর্ণ, আর Dio দিয়ে কীভাবে implement করবেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Certificate pinning মানে app শুধু একটা নির্দিষ্ট, পরিচিত server certificate (বা তার public key)-কেই বিশ্বাস করে। Device যে সব certificate বিশ্বাস করে, সবগুলোকে নয়। এটা গুরুত্বপূর্ণ কারণ এটা man-in-the-middle আক্রমণ ঠেকায়, যেখানে attacker একটা নকল trusted certificate বসিয়ে দেয়। Flutter-এ Dio দিয়ে আমি server-এর certificate fingerprint-কে app-এর ভেতরে রাখা একটা value-র সাথে মিলিয়ে দেখি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কোন সমস্যা সমাধান করে।**
সাধারণভাবে app যেকোনো trusted authority-র sign করা certificate বিশ্বাস করে। কিন্তু compromised device বা network-এ attacker একটা নকল trusted certificate বসাতে পারে। তারপর চুপচাপ আপনার "HTTPS" traffic পড়ে ফেলে ([MITM](#q7))। Pinning বলে "আমি শুধু *ঠিক এই* certificate-টাই বিশ্বাস করি" — তাই নকলটা reject হয়ে যায়।

**ধাপ ২ — বাস্তব জীবনের একটা ছবি।**
HTTPS দেখে "এটা কি একটা বৈধ ID card?" Pinning দেখে "এটা কি *ঠিক সেই মানুষটা* যাকে আমি আশা করছি?" — অনেক বেশি শক্তিশালী।

**ধাপ ৩ — Dio দিয়ে implement করা।**

```dart
final dio = Dio();
(dio.httpClientAdapter as IOHttpClientAdapter).createHttpClient = () {
  final client = HttpClient();
  client.badCertificateCallback = (cert, host, port) {
    // Server cert-এর fingerprint-কে pin করা fingerprint-এর সাথে মেলান
    final fingerprint = sha256.convert(cert.der).toString();
    return fingerprint == expectedFingerprint; // শুধু পরিচিত cert-কেই বিশ্বাস
  };
  return client;
};
```

(এর জন্য আলাদা package আর `certificate_pinning` পদ্ধতিও আছে; ধারণাটা একই — একটা পরিচিত value-র সাথে মিলিয়ে যাচাই করা।)

**ধাপ ৪ — Trade-off: pin rotation।**
Certificate-এর মেয়াদ শেষ হয় আর সেগুলো বদলায়। আপনি একটা pin করলেন, সেটা বদলে গেলে app কাজ করবে না — update না করা পর্যন্ত। এটা কমাতে **public key** pin করুন (cert-এর চেয়ে বেশি স্থিতিশীল), একটা backup key-ও pin করুন, আর update করার একটা পথ রাখুন।

**Interviewer কেন জিজ্ঞেস করে:** MITM-এর বিরুদ্ধে pinning-ই মূল প্রতিরক্ষা, আর এটা network security-তে আপনার গভীরতা দেখায়।

**সাধারণ ভুল:** Certificate rotation-এর কথা ভুলে যাওয়া — server cert renew করলে app হঠাৎ connect করতে পারে না। Key pin করুন আর একটা backup রাখুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Cert pin করবেন নাকি public key?"* → সাধারণত public key-ই ভালো — certificate renew হলেও এটা টিকে থাকে।

**সম্পর্কিত:** [Q7 — MITM](#q7) · [Q2 — in transit](#q2)

[↑ উপরে ফিরুন](#toc)

---

<a id="q7"></a>
## 7. Man-in-the-Middle (MITM) আক্রমণ কী, আর এটা কীভাবে আটকাবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"MITM আক্রমণ মানে attacker চুপচাপ app আর server-এর মাঝখানে বসে যায়। সে traffic পড়ে বা বদলে দেয় — যেমন একটা নকল public Wi-Fi-তে। এটা আটকাতে সব জায়গায় HTTPS ব্যবহার করি (যাতে traffic encrypt থাকে), certificate pinning করি (যাতে নকল certificate reject হয়), আর release-এ user-এর বসানো certificate কখনোই বিশ্বাস করি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি: চিঠি মাঝপথে খুলে পড়া।**
ভাবুন, কেউ আপনার চিঠি আপনার কাছে পৌঁছানোর আগে চুপচাপ খুলে পড়ে আবার সিল করে দিচ্ছে। MITM attacker আপনার network traffic-এর সাথে ঠিক এটাই করে। আপনি ভাবছেন server-এর সাথে কথা বলছেন, কিন্তু মাঝখানে সে বসে আছে।

**ধাপ ২ — এটা কীভাবে ঘটে।**
- Attacker-এর নিয়ন্ত্রণে থাকা public বা নকল Wi-Fi।
- Device-এ বসানো ক্ষতিকর বা নকল trusted certificate।
- সাধারণ HTTP traffic (কোনো encryption নেই)।

**ধাপ ৩ — প্রতিরক্ষাগুলো।**
1. **সব জায়গায় HTTPS** — সব traffic encrypt করুন; কখনোই সাধারণ HTTP নয় ([Q2](#q2))।
2. **Certificate pinning** — শুধু নিজের পরিচিত certificate বিশ্বাস করুন, তাহলে নকলটা fail করবে ([Q6](#q6))।
3. Release-এ **user-এর যোগ করা certificate বিশ্বাস করবেন না** (network security এমনভাবে configure করুন যেন সেগুলো উপেক্ষা করে)।
4. **সবকিছু server-side-এ validate করুন** — কখনোই শুধু client-এর উপর ভরসা করবেন না।

**ধাপ ৪ — এটা test করুন।**
Charles Proxy বা mitmproxy-র মতো tool একটা MITM নকল করে দেখায়। Pin করা app-এর ওগুলোর মধ্য দিয়ে connect করতে *ব্যর্থ* হওয়া উচিত — এভাবেই pinning কাজ করছে কি না নিশ্চিত হবেন।

**Interviewer কেন জিজ্ঞেস করে:** MITM হলো ক্লাসিক network আক্রমণ; তাঁরা দেখেন আপনি স্তরে স্তরে প্রতিরক্ষা জানেন কি না।

**সাধারণ ভুল:** ভাবা যে শুধু HTTPS-ই যথেষ্ট। HTTPS সাধারণ আড়ি পাতা থামায়, কিন্তু নকল trusted certificate সেটা হারিয়ে দেয় — ওটা থামায় pinning।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"MITM প্রতিরোধ কীভাবে test করবেন?"* → App-এর traffic proxy করার চেষ্টা করুন; pinning থাকলে সেটা connect করতে অস্বীকার করবে।

**সম্পর্কিত:** [Q6 — cert pinning](#q6) · [Q2 — in transit](#q2)

[↑ উপরে ফিরুন](#toc)

---

<a id="q8"></a>
## 8. Mobile-এর প্রেক্ষাপটে SQL injection কী, আর এটা কীভাবে আটকাবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"SQL injection মানে অবিশ্বস্ত input সরাসরি একটা SQL query-তে জোড়া লাগানো। তখন attacker query-র কাজ বদলে দিতে পারে — যে data পড়ার বা মোছার কথা নয়, সেটাও পারে। Mobile app-এ এটা local SQLite database বা backend দুটোতেই লাগতে পারে। এটা আটকাতে আমি সবসময় parameterized query (placeholder) ব্যবহার করি, string concatenation দিয়ে SQL বানাই না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুর্বলতাটা কোথায়।**
User input সরাসরি query-তে বসিয়ে দিলে সেই input বেরিয়ে এসে নিজের SQL ঢুকিয়ে দিতে পারে।

```dart
// বিপজ্জনক — input সরাসরি SQL-এ জোড়া হচ্ছে
final name = userInput; // যেমন  ' OR '1'='1
db.rawQuery("SELECT * FROM users WHERE name = '$name'");
// হয়ে যায়: ... WHERE name = '' OR '1'='1'  → সবাইকে return করে
```

**ধাপ ২ — সমাধান: parameterized query।**
Placeholder (`?`) ব্যবহার করুন আর value আলাদা করে pass করুন। তাহলে input সবসময় data হিসেবে গণ্য হয়, কখনোই code হিসেবে নয়।

```dart
// নিরাপদ — value bind হচ্ছে, concatenate নয়
db.rawQuery('SELECT * FROM users WHERE name = ?', [userInput]);
```

`sqflite`-এ query method-গুলো ঠিক এই কারণেই একটা `whereArgs` list নেয়:

```dart
db.query('users', where: 'name = ?', whereArgs: [userInput]); // নিরাপদ
```

**ধাপ ৩ — Defense in depth।**
- **সবসময় parameterize করুন** (মূল সমাধান)।
- **Input validate করুন** (type, length, অনুমোদিত character)।
- **Least privilege** — DB user/role শুধু যতটুকু দরকার ততটুকুই করতে পারবে।

**ধাপ ৪ — এটা backend-এও প্রযোজ্য।**
আপনার server-এর database-এও একই নিয়ম খাটে। বেশিরভাগ ORM default-ভাবেই parameterize করে — শুধু raw concatenated SQL-এ নেমে যাবেন না।

**Interviewer কেন জিজ্ঞেস করে:** এটা input handling-এর একটা মৌলিক অভ্যাস যাচাই করে, যা device আর server দুই জায়গাতেই লাগে।

**সাধারণ ভুল:** String interpolation (`'$input'`) দিয়ে SQL বানানো। সবসময় placeholder ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা কি NoSQL-এও প্রযোজ্য?"* → হ্যাঁ — "NoSQL injection"-ও আছে; কোনো query-তেই raw input বিশ্বাস করবেন না।

**সম্পর্কিত:** [Q8 (DSA) — none] · [Q12 (Networking) — sqflite/drift](section-07-networking-storage-bn.md#q12)

[↑ উপরে ফিরুন](#toc)

---

# D. Authentication

---

<a id="q9"></a>
## 9. Access token আর refresh token-এর পার্থক্য কী? এগুলো কোথায় রাখেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Access token হলো স্বল্পমেয়াদি একটা key। প্রতিটা API call-এ এটা প্রমাণ করে আমি কে। Refresh token একটু দীর্ঘমেয়াদি key। এটা শুধু তখনই লাগে যখন access token expire হয়ে যায় আর নতুন একটা দরকার হয়। Access token-এর আয়ু কম রাখলে leak হলেও ক্ষতি কম হয়। দুটোই secure storage-এ রাখা উচিত। আর access token expire হলে আমি চুপচাপ refresh করে নিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুটো token, দুটো কাজ।**
- **Access token** — প্রতিটা API request-এর সাথে পাঠানো হয়, পরিচয় প্রমাণ করতে। স্বল্পমেয়াদি (কয়েক মিনিট থেকে এক ঘণ্টা)।
- **Refresh token** — *শুধু* নতুন access token নিতে ব্যবহার হয়। দীর্ঘমেয়াদি (কয়েক দিন/সপ্তাহ)।

**ধাপ ২ — কেন দুই ভাগ করা হয়।**
স্বল্পমেয়াদি access token leak হলে সেটা দ্রুত expire হয়ে যায় — ক্ষতি সীমিত। দীর্ঘমেয়াদি refresh token খুব কমই ব্যবহার হয়। আর শুধু auth server-এর সাথেই ব্যবহার হয়। তাই এটা অনেক কম উন্মুক্ত হয়।

**ধাপ ৩ — কোথায় রাখবেন।**
দুটোই sensitive → **secure storage** ([Q3](#q3)):

```dart
await storage.write(key: 'access_token', value: access);
await storage.write(key: 'refresh_token', value: refresh);
```

**ধাপ ৪ — Expiry সামলানো (silent refresh)।**
কোনো API call 401 (token expired) ফেরত দিলে refresh token দিয়ে নতুন access token নিন। তারপর মূল request আবার পাঠান। Dio interceptor এই কাজটা নিজে নিজেই করে দেয়:

```
request → 401 → use refresh token → get new access token → retry original request
```

Refresh token নিজেই invalid/expired হলে user-কে আবার log in করতে বাধ্য করুন।

**Interviewer কেন জিজ্ঞেস করে:** প্রতিটা authenticated app-এ token handling মূল জিনিস। তাঁরা দেখেন আপনি short/long-lived ভাগটা আর secure storage বোঝেন কি না।

**সাধারণ ভুল:** চিরকালের জন্য একটাই long-lived token ব্যবহার করা (leak হলে ক্ষতির পরিধি বিশাল), অথবা token SharedPreferences-এ রাখা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Refresh token rotation?"* → প্রতিবার refresh-এ নতুন refresh token দিন আর পুরোনোটা invalid করে দিন। ফলে চুরি হওয়া refresh token দ্রুত অকেজো হয়ে যায়।

**সম্পর্কিত:** [Q3 — secure storage](#q3) · [Q11 — JWT](#q11) · [Q3 (Networking) — interceptor/refresh](section-07-networking-storage-bn.md#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q10"></a>
## 10. Mobile-এর জন্য OAuth 2.0 Authorization Code + PKCE flow ব্যাখ্যা করুন।

> Common · Hard · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"OAuth 2.0 দিয়ে user কোনো provider (Google, Facebook) দিয়ে log in করতে পারে। App-কে নিজের password দিতে হয় না। Mobile-এর জন্য নিরাপদ সংস্করণ হলো Authorization Code with PKCE। PKCE একটা এককালীন secret যোগ করে, যেটা app নিজে তৈরি করে। ফলে authorization code চুরি হলেও attacker ওই secret ছাড়া সেটা দিয়ে token নিতে পারবে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Mobile-এ কেন PKCE।**
Mobile app-এ client secret রাখা যায় না (যে কেউ app decompile করতে পারে, [Q4](#q4))। PKCE (Proof Key for Code Exchange) সেই secret-এর বদলে একটা নতুন, এককালীন proof ব্যবহার করে। প্রতিটা login-এ এটা নতুন করে তৈরি হয় — জমা রাখা secret ছাড়াই নিরাপদ।

**ধাপ ২ — Flow, ধাপে ধাপে।**

```
1. App makes a random 'code_verifier', and a 'code_challenge' = hash(verifier).
2. App opens the provider's login page, sending the code_challenge.
3. User logs in; provider redirects back with an authorization CODE.
4. App exchanges CODE + the original code_verifier for tokens.
5. Provider checks hash(verifier) == challenge → returns access + refresh tokens.
```

**ধাপ ৩ — Interception কেন ব্যর্থ হয়।**
উপরের 3 নম্বর ধাপে attacker যদি authorization code চুরি করে, তবুও সে 4 নম্বর ধাপ শেষ করতে পারবে না। তার কাছে `code_verifier` নেই (ওটা কখনো app ছেড়ে বের হয়নি)। Hash কোডটাকে ওই একটা login-এর সাথে বেঁধে রাখে।

**ধাপ ৪ — Flutter-এ।**
ভালোভাবে পরীক্ষিত package ব্যবহার করুন (যেমন `flutter_appauth` বা provider-এর SDK)। সাথে device-এর secure browser tab ব্যবহার করুন। নিজের হাতে OAuth লিখবেন না। embedded webview-ও ব্যবহার করবেন না (এটা credential leak করতে পারে)।

**Interviewer কেন জিজ্ঞেস করে:** Mobile-এর জন্য OAuth/PKCE-ই standard নিরাপদ login। এটা auth-এর গভীর বোঝাপড়া যাচাই করে।

**সাধারণ ভুল:** login-এর জন্য system browser বা যাচাই করা SDK-র বদলে embedded WebView ব্যবহার করা (অনিরাপদ, password ধরে ফেলতে পারে)। অথবা app-এর ভেতরে client secret রাখার চেষ্টা করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Implicit flow কেন নয়?"* → এটা redirect-এ সরাসরি token ফেরত দেয় (কম নিরাপদ)। Mobile-এর জন্য এটা deprecated। Authorization Code + PKCE-ই সুপারিশ করা হয়।

**সম্পর্কিত:** [Q9 — tokens](#q9) · [Q11 — JWT](#q11) · [Q4 — client secret রাখা যাবে না](#q4)

[↑ উপরে ফিরুন](#toc)

---

<a id="q11"></a>
## 11. JWT কী? এর গঠন, কীভাবে verify করবেন, আর এতে কী রাখা যাবে **না** — ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"JWT (JSON Web Token) হলো একটা signed token, তিন অংশে ভাগ করা: header, payload আর signature — মাঝে dot দিয়ে আলাদা। Signature দিয়ে server যাচাই করে token-এ কেউ হাত দেয়নি। সবচেয়ে জরুরি কথা: payload শুধু encoded, encrypted নয় — যে কেউ পড়তে পারে। তাই এতে কখনো secret বা sensitive data রাখবেন না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটা অংশ।**

```
header.payload.signature

eyJhbGc...  .  eyJzdWIi...  .  SflKxwRJ...
(algorithm)    (claims/data)   (signature)
```

- **Header** — signing algorithm (যেমন HS256, RS256)।
- **Payload** — claim গুলো: user id, role, expiry (`exp`)।
- **Signature** — প্রমাণ করে token আসল আর অপরিবর্তিত।

**ধাপ ২ — Verification কীভাবে কাজ করে।**
Server তার secret (বা public key) দিয়ে header+payload-এর উপর signature আবার হিসাব করে। এটা token-এর signature-এর সাথে মিলে গেলে token আসল আর অক্ষত। Server `exp`-ও check করে (expire হয়নি তো)।

**ধাপ ৩ — সবচেয়ে জরুরি কথা: payload পড়া যায়।**
Payload আসলে শুধু Base64-encoded JSON, encrypted নয়। যে কেউ এটা decode করতে পারে (jwt.io-তে paste করলেই হলো)। তাই:
- **কখনোই** payload-এ password, secret বা sensitive PII রাখবেন না।
- শুধু non-secret পরিচয়ের তথ্য রাখুন (user id, role, expiry)।

```
// Decoded payload — যে কেউ এটা পড়তে পারে:
{ "sub": "user_123", "role": "user", "exp": 1735689600 }   // কোনো secret নয়!
```

**ধাপ ৪ — বাস্তব নিয়ম।**
- এগুলো **স্বল্পমেয়াদি** রাখুন (বেশি সময়ের জন্য refresh token ব্যবহার করুন, [Q9](#q9))।
- **Server-side** verify করুন — app যে JWT verify করতে পারে না, সেটাকে বিশ্বাস করা উচিত নয়।
- **Secure storage**-এ রাখুন ([Q3](#q3))।

**Interviewer কেন জিজ্ঞেস করে:** Auth-এ JWT সব জায়গায় আছে। "payload পড়া যায়" — এই পয়েন্টটা তাঁদের প্রিয় ফাঁদ।

**সাধারণ ভুল:** payload-এ sensitive data রাখা, ভেবে যে এটা লুকানো — আসলে এটা শুধু encoded, পুরোপুরি পড়া যায়। আরেকটা ভুল: signature verify না করেই JWT-কে বিশ্বাস করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"HS256 vs RS256?"* → HS256 একটা shared secret ব্যবহার করে (symmetric)। RS256 private/public key জোড়া ব্যবহার করে (server private key দিয়ে sign করে, অন্যরা public key দিয়ে verify করে)।

**সম্পর্কিত:** [Q9 — tokens](#q9) · [Q10 — OAuth](#q10) · [Q3 — secure storage](#q3)

[↑ উপরে ফিরুন](#toc)

---

<a id="q12"></a>
## 12. Flutter-এ biometric authentication কীভাবে সামলান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Biometrics (fingerprint, Face ID) device-এর secure hardware দিয়ে user-কে authenticate করে। Flutter-এ আমি `local_auth` package ব্যবহার করি। এটা OS-কে বলে user যাচাই করতে। গুরুত্বপূর্ণ কথা: biometrics শুধু *local* access খুলে দেয় — আসল check হয় device-এর ভেতরেই। সত্যিকারের নিরাপত্তার জন্য server-side auth (token) লাগবেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Biometrics কী করে (আর কী করে না)।**
OS-এর secure enclave ব্যবহার করে এগুলো নিশ্চিত করে — "ঠিক মানুষটাই phone ধরে আছে।" এগুলো server authentication-এর বিকল্প **নয়**। এগুলো একটা সুবিধাজনক local gate (যেমন app unlock করা, বা জমা রাখা token বের করে দেওয়া)।

**ধাপ ২ — local_auth ব্যবহার।**

```dart
final auth = LocalAuthentication();

final canCheck = await auth.canCheckBiometrics; // hardware আছে কি না?

final didAuth = await auth.authenticate(
  localizedReason: 'Authenticate to access your account',
  options: const AuthenticationOptions(biometricOnly: true, stickyAuth: true),
);

if (didAuth) {
  // app unlock করুন / secure storage থেকে token পড়ুন
}
```

**ধাপ ৩ — নিরাপদ pattern।**
একটা সাধারণ ও নিরাপদ design: user একবার log in করে (server auth → secure storage-এ token)। পরে app খুললে biometrics *ওই জমা token-এ ঢোকার পথ* পাহারা দেয়। Biometric-এর ফলাফল নিজে শুধু একটা local হ্যাঁ/না।

**ধাপ ৪ — Edge case গুলো সামলান।**
- কোনো biometrics enroll করা নেই → PIN/password-এ fall back করুন।
- Rooted device-এ biometric check bypass করা যায় → শুধু biometrics যথেষ্ট নয়। Server-side check রাখুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তব mobile auth যাচাই করে। আর দেখে আপনি বোঝেন কি না যে biometrics একটা *local* সুবিধা, পূর্ণ নিরাপত্তা নয়।

**সাধারণ ভুল:** সফল biometric check-কে পূর্ণ authentication ধরে নেওয়া, পেছনে কোনো আসল server-side token বা পরিচয় ছাড়াই।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fingerprint কোথায় জমা থাকে?"* → device-এর secure hardware-এ। আপনার app কখনো সেটা দেখে না — শুধু একটা হ্যাঁ/না পায়।

**সম্পর্কিত:** [Q9 — tokens](#q9) · [Q3 — secure storage](#q3)

[↑ উপরে ফিরুন](#toc)

---

# E. App hardening

---

<a id="q13"></a>
## 13. Code obfuscation কী, আর Flutter-এ কীভাবে এটা enable করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Obfuscation আমার compiled code-কে এলোমেলো করে দেয় — class আর method-এর নাম বদলে অর্থহীন symbol বানায়। ফলে কারও জন্য app decompile করে বোঝা অনেক কঠিন হয়ে যায়। Flutter-এ release build-এর সময় `--obfuscate --split-debug-info` দিয়ে এটা enable করি। এটা reverse engineering-এর কষ্ট বাড়ায়, কিন্তু আসল security-র বিকল্প নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কী করে।**
একটা release app decompile করা যায়। Obfuscation পড়ার মতো নামগুলো (`AuthService.refreshToken`) বদলে অর্থহীন করে দেয় (`a.b`)। ফলে decompiled code অনুসরণ করা কঠিন — যেন blueprint-এর সব label ছিঁড়ে ফেলা হয়েছে।

**ধাপ ২ — Flutter-এ enable করুন।**

```bash
flutter build apk --obfuscate --split-debug-info=build/symbols
flutter build ipa --obfuscate --split-debug-info=build/symbols
```

- `--obfuscate` Dart code এলোমেলো করে দেয়।
- `--split-debug-info` একটা symbol map সেভ করে রাখে। ফলে crash report আবার de-obfuscate করা যায়। **এই symbol file-গুলো রেখে দিন** (নিজের কাছে, গোপনে) debugging-এর জন্য।

**ধাপ ৩ — Obfuscation যা নয়।**
এটা reverse engineering *কঠিন* করে, অসম্ভব করে না। আর এটা binary-র ভেতরের secret লুকায় **না** ([Q4](#q4))। একজন নাছোড় attacker এখনও app বিশ্লেষণ করতে পারে। এটা একটা স্তর, পুরো প্রতিরক্ষা নয়।

**ধাপ ৪ — অন্য স্তরের সাথে মিলিয়ে ব্যবহার করুন।**
এর সাথে রাখুন — কোনো hardcoded secret নয়, server-side check, আর দরকার হলে integrity/root check ([Q14](#q14))। Defense in depth।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তব release hardening যাচাই করে। সাথে এই বাস্তব দৃষ্টিভঙ্গিও — এটা একটা বাধা, guarantee নয়।

**সাধারণ ভুল:** ভাবা যে obfuscation secret লুকায় বা app-কে "secure" করে দেয়। এটা reverse engineering-এর খাটুনি বাড়ায়। App-এর ভেতরে যে data থাকতেই হবে, সেটা এটা রক্ষা করে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Symbol file-গুলো কেন রাখবেন?"* → Crash report de-obfuscate (symbolicate) করার জন্য, যাতে stack trace পড়া যায়।

**সম্পর্কিত:** [Q4 — API keys](#q4) · [Q14 — root detection](#q14)

[↑ উপরে ফিরুন](#toc)

---

<a id="q14"></a>
## 14. Root / jailbreak detection কী, আর basic detection কীভাবে implement করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Root (Android) বা jailbreak (iOS) মানে device-এর security control সরিয়ে ফেলা হয়েছে। ফলে আমি যে OS protection-এর উপর ভরসা করি (যেমন keystore), সেটা দুর্বল হয়ে যায়। Detection এমন device চিনতে চেষ্টা করে আর সেই অনুযায়ী আচরণ করে — user-কে সতর্ক করে, feature সীমিত করে, বা sensitive কাজ block করে। Flutter-এ `flutter_jailbreak_detection`-এর মতো package ব্যবহার করা যায়। কিন্তু detection bypass করা সম্ভব, তাই এটাকে একটা signal হিসেবে নিন, guarantee হিসেবে নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কেন এটা গুরুত্বপূর্ণ।**
Rooted/jailbroken device-এ attacker-এর গভীর access থাকে — তারা app storage পড়তে পারে, app-এ hook করতে পারে, আর কিছু OS protection পাশ কাটাতে পারে। উচ্চ-নিরাপত্তার app-এর (banking, payments) ক্ষেত্রে এটা detect করে ঝুঁকি কমাতে চাইতে পারেন।

**ধাপ ২ — Basic detection কীভাবে কাজ করে।**
এটা চেনা চিহ্ন খোঁজে: পরিচিত root/jailbreak file বা app, protected path-এ লেখার ক্ষমতা, বা সন্দেহজনক system property।

```dart
final isCompromised = await FlutterJailbreakDetection.jailbroken;
if (isCompromised) {
  // প্রতিক্রিয়া: সতর্ক করুন, feature সীমিত করুন, বা sensitive operation block করুন
}
```

**ধাপ ৩ — কীভাবে সাড়া দেবেন (মাত্রা বুঝে)।**
- **Banking/payments** — sensitive কাজ block বা সীমিত করতে পারেন।
- **বেশিরভাগ app** — user-কে সতর্ক করুন আর কম বিশ্বাস নিয়ে চালিয়ে যান।
আপনার app-এর ঝুঁকির মাত্রা দেখে সিদ্ধান্ত নিন। অকারণে প্রতিটা power user-কে আটকে দেবেন না।

**ধাপ ৪ — সৎ সতর্কতা।**
Detection একটা **ইঁদুর-বিড়ালের খেলা** — নাছোড় attacker root লুকাতে পারে বা আপনার check patch করে সরিয়ে দিতে পারে (কারণ check চলে তাদেরই নিয়ন্ত্রণে থাকা device-এ)। এটা বাধা বাড়ায়, কিন্তু নিখুঁত নয়। জরুরি security সবসময় server-এ রাখুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তব threat modeling যাচাই করে — client-side detection-এর মূল্য আর সীমা দুটোই জানা আছে কি না।

**সাধারণ ভুল:** Root detection-কে শক্ত security সীমানা হিসেবে বিশ্বাস করা। এটা এমন একটা signal যা bypass করা যায়। আসল security server-কেই প্রয়োগ করতে হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা কি bypass করা যায়?"* → হ্যাঁ — check চলে attacker-এর নিয়ন্ত্রণে থাকা device-এ, তাই তারা এটা হারাতে পারে; কখনোই শুধু এর উপর ভরসা করবেন না।

**সম্পর্কিত:** [Q3 — secure storage](#q3) · [Q13 — obfuscation](#q13)

[↑ উপরে ফিরুন](#toc)

---

<a id="q15"></a>
## 15. Deep link hijacking কী, আর Flutter-এ deep link কীভাবে নিরাপদ করবেন?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-20-mobile-security.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Deep link hijacking মানে একটা ক্ষতিকর app আপনার মতো একই custom URL scheme register করে ফেলে। ফলে আপনার app-এর জন্য আসা link সে ধরে ফেলতে পারে — এমনকি OAuth code-এর মতো data চুরি করতে পারে। এটা ঠেকাতে verified App Links (Android) আর Universal Links (iOS) ব্যবহার করি। এগুলো আমার domain-এর সাথে বাঁধা, তাই অন্য app দাবি করতে পারে না। আর deep-link data কখনোই validation ছাড়া বিশ্বাস করি না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Custom scheme-এর দুর্বলতা।**
`myapp://`-এর মতো custom scheme "আগে এলে আগে পাবে" নিয়মে চলে — যেকোনো app এটা ঘোষণা করতে পারে। `myapp://` ঘোষণা করা একটা ক্ষতিকর app আপনার জন্য আসা link পেয়ে যেতে পারে (যেমন code সহ একটা OAuth redirect)।

**ধাপ ২ — সমাধান: domain-এর সাথে বাঁধা verified link।**
- **Android App Links** আর **iOS Universal Links** আসল `https://yourdomain.com/...` URL ব্যবহার করে। আপনার domain-এ host করা একটা file দিয়ে এগুলো verify হয় (`assetlinks.json` / `apple-app-site-association`)।
- এগুলো আপনার নিজের domain-এর সাথে বাঁধা বলে অন্য app এগুলো দাবি করতে **পারে না**।

**ধাপ ৩ — আসা data validate করুন।**
Deep-link parameter-কে অবিশ্বস্ত input হিসেবে ধরুন:
- সব কিছু validate আর sanitize করুন ([Q8](#q8))।
- OAuth-এর ক্ষেত্রে PKCE ([Q10](#q10)) code-কে রক্ষা করে, link ধরা পড়লেও।
- Sensitive deep link-এ কাজ করার আগে auth বাধ্যতামূলক করুন (link বলেছে বলেই টাকা transfer করে ফেলবেন না)।

**ধাপ ৪ — Flutter-এ।**
Deep link-এর জন্য `go_router`-এর মতো router ব্যবহার করুন, App Links/Universal Links ঠিকমতো configure করুন, আর একটা guard/redirect যোগ করুন যেটা protected destination খোলার আগে auth check করে।

**Interviewer কেন জিজ্ঞেস করে:** Deep link mobile-এর একটা বাস্তব attack surface; এটা platform-নির্দিষ্ট security জ্ঞান যাচাই করে।

**সাধারণ ভুল:** Sensitive flow-এর জন্য custom URL scheme-এর উপর ভরসা করা (hijack করা যায়), বা validation ছাড়া deep-link parameter বিশ্বাস করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"App Links বনাম custom scheme?"* → App/Universal Links domain-verified (hijack করা যায় না); custom scheme যেকোনো app দাবি করতে পারে।

**সম্পর্কিত:** [Q10 — OAuth/PKCE](#q10) · [Q8 — input validation](#q8) · [Q4 (Navigation) — deep linking](section-04-navigation-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। আগে table, তারপর এক-লাইনের মনে করিয়ে দেওয়া কথাগুলো।

## Threat → defense

| Threat | Defense |
|---|---|
| চুরি যাওয়া device token পড়ে ফেলে | secure storage ([Q3](#q3)) |
| Hardcoded key বের করে নেওয়া | secret server-এ রাখুন ([Q4](#q4)) |
| Network-এ আড়িপাতা | HTTPS + cert pinning ([Q6](#q6)) |
| নকল certificate (MITM) | certificate pinning ([Q6](#q6), [Q7](#q7)) |
| ফাঁস হওয়া দীর্ঘমেয়াদি token | ছোট access + refresh token ([Q9](#q9)) |
| Reverse engineering | obfuscation ([Q13](#q13)) |
| Hijack হওয়া deep link | App/Universal Links ([Q15](#q15)) |
| SQL injection | parameterized query ([Q8](#q8)) |

## At rest বনাম in transit

| | In transit | At rest |
|---|---|---|
| কী রক্ষা করে | network-এ চলাচল করা data | device-এ জমা থাকা data |
| কীভাবে | HTTPS/TLS | secure storage / encrypted DB |

## এক-লাইনের মনে করিয়ে দেওয়া কথা

- **Client-কে বিশ্বাস করবেন না** — app-এর ভেতরের সব কিছু দেখে ফেলা যায়; server-এ প্রয়োগ করুন। ([Q1](#q1))
- **In transit (HTTPS) আর at rest (secure storage) — দুই জায়গাতেই encrypt করুন** — দুটোই দরকার। ([Q2](#q2))
- **SharedPreferences = plain text**; secret-এর জন্য `flutter_secure_storage` ব্যবহার করুন। ([Q3](#q3))
- **কখনোই secret hardcode করবেন না** — সেগুলো binary-তে চলে যায়; আসলগুলো server-এ রাখুন। ([Q4](#q4))
- **কখনোই token/PII log করবেন না**; release-এ scrub করুন আর verbose log বন্ধ রাখুন। ([Q5](#q5))
- **Certificate pinning** শুধু আপনার চেনা cert/key বিশ্বাস করে MITM হারিয়ে দেয়। ([Q6](#q6), [Q7](#q7))
- **সবসময় SQL parameterize করুন** (`?` + args); কখনোই input জোড়া লাগাবেন না। ([Q8](#q8))
- **ছোট access token + refresh token**; দুটোই secure storage-এ; 401-এ চুপচাপ refresh। ([Q9](#q9))
- **Mobile login-এ OAuth + PKCE**; system browser ব্যবহার করুন, webview নয়। ([Q10](#q10))
- **JWT payload পড়া যায়** (শুধু encoded) — ভেতরে কোনো secret নয়; server-side verify করুন। ([Q11](#q11))
- **Biometrics = local gate**, পুরো auth নয়; server-side token রাখুন। ([Q12](#q12))
- **Obfuscation** বাধা বাড়ায়, কিন্তু secret লুকায় না। ([Q13](#q13))
- **Root detection** একটা signal, guarantee নয় — এটা bypass করা যায়। ([Q14](#q14))
- **App/Universal Links ব্যবহার করুন** (domain-verified), যাতে deep link hijack করা না যায়। ([Q15](#q15))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Security interview-এ tool-এর পেছনের threat নিয়ে খোঁচানো হয়। জোরে বলে অনুশীলন করুন:

1. *"Auth token কোথায় রাখেন?"* → secure storage-এ (Keychain/Keystore), কখনোই SharedPreferences-এ নয়, আর token-এর মেয়াদ ছোট রাখি।
2. *"আপনি তো HTTPS ব্যবহার করছেন — এটাই কি যথেষ্ট?"* → না; একটা নকল trusted cert এটাকে হারিয়ে দেয়। Certificate pinning যোগ করুন।
3. *"App-এর ভেতরে API key লুকিয়ে রাখা যায়?"* → না; binary পড়ে ফেলা যায়। আসল secret server-এ রাখুন।
4. *"একটা JWT user-এর role বহন করছে — client-এ এটা বিশ্বাস করা কি নিরাপদ?"* → server-side verify করুন; payload পড়া যায় আর client অবিশ্বস্ত।
5. *"Mobile-এ OAuth redirect কীভাবে নিরাপদ করেন?"* → Authorization Code + PKCE + App/Universal Links, যাতে ধরা পড়া code কোনো কাজে না লাগে।

আগে *threat*-এর নাম বলা, তারপর *স্তরে স্তরে প্রতিরক্ষা* বলা — আর "client-কে বিশ্বাস করবেন না" কথাটায় জোর দেওয়া — এটাই ঠিক senior signal, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
