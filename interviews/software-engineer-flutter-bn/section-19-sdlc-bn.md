# Section 19 — SDLC ও Software Engineering Process

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন। এটা একটা process-এর topic — উদাহরণগুলো বাস্তব scenario, code নয়।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-19-sdlc.md](../software-engineer-flutter/section-19-sdlc.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code দিয়ে ধাপে ধাপে পুরো ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে tag দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** Process-এর প্রশ্নে প্রতিটা phase-কে *quality আর risk*-এর সাথে যুক্ত করুন — "আমরা সমস্যা আগেই ধরি, কারণ তখন খরচ কম।" এই framing senior চিন্তা দেখায়।

---


## <a id="toc"></a>সূচিপত্র

**A. Overview ও requirements**
1. [SDLC কী? (phase-গুলো)](#q1) · *Very common*
2. [Requirement gathering (functional বনাম non-functional)](#q2) · *Very common*
3. [System design — HLD বনাম LLD](#q3) · *Common*

**B. Build ও verify**
4. [ভালো development practice](#q4) · *Common*
5. [Code review](#q5) · *Very common*
6. [Testing-এর phase (unit/integration/system/UAT)](#q6) · *Very common*

**C. Ship ও maintain**
7. [Deployment (staging বনাম production, checklist)](#q7) · *Common*
8. [Maintenance (bug tracking, hotfix, versioning)](#q8) · *Common*
9. [Production bug সামলানো (ধাপে ধাপে)](#q9) · *Very common*

**D. Quality, risk ও docs**
10. [পুরো SDLC জুড়ে quality](#q10) · *Common*
11. [Shift-Left testing](#q11) · *Common*
12. [DevOps culture](#q12) · *Common*
13. [Risk management](#q13) · *Common*
14. [Documentation (কী লিখবেন, কী লিখবেন না)](#q14) · *Common*

**E. ধারণা**
15. [Spike কী?](#q15) · *Deeper*
16. [Bug বনাম defect বনাম feature request](#q16) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — Lifecycle (এখান থেকে শুরু করুন)।**
→ [Q1 SDLC phase](#q1) · [Q2 Requirements](#q2) · [Q3 HLD বনাম LLD](#q3)

**পর্যায় ২ — ভালোভাবে build করা।**
→ [Q4 Dev practice](#q4) · [Q5 Code review](#q5) · [Q6 Testing-এর phase](#q6)

**পর্যায় ৩ — Ship ও support।**
→ [Q7 Deployment](#q7) · [Q8 Maintenance](#q8) · [Q9 Production bug](#q9)

**পর্যায় ৪ — Quality ও risk।**
→ [Q10 পুরো জুড়ে quality](#q10) · [Q11 Shift-left](#q11) · [Q12 DevOps](#q12) · [Q13 Risk](#q13)

**পর্যায় ৫ — বাকিগুলো।**
→ [Q14 Documentation](#q14) · [Q15 Spike](#q15) · [Q16 Bug বনাম defect](#q16)

**সময় কম?** দেখে নিন [Q1](#q1) · [Q2](#q2) · [Q5](#q5) · [Q6](#q6) · [Q9](#q9), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. Overview ও requirements

---

## <a id="q1"></a>1. SDLC কী, আর এর phase-গুলো কী কী?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"SDLC মানে Software Development Lifecycle। এটা software বানানোর একটা সাজানো process — planning থেকে শুরু করে retirement পর্যন্ত। ক্লাসিক phase-গুলো হলো: requirements, design, development, testing, deployment, আর maintenance। এটা team-কে একটা repeatable উপায় দেয়, যাতে quality software ঠিক সময়ে, ঠিকভাবে deliver করা যায়। আর আলাদা আলাদা model (Waterfall, Agile) এই phase-গুলোকে আলাদাভাবে সাজায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব উদাহরণ: একটা বাড়ি বানানো।**
আপনি এলোমেলোভাবে ইট গাঁথা শুরু করেন না। আগে requirement নেন (মালিক কী চান), তারপর blueprint design করেন, বানান, পরিদর্শন করেন, উঠে যান, তারপর রক্ষণাবেক্ষণ করেন। Software-ও একই যুক্তির পথ ধরে চলে।

**ধাপ ২ — Phase-গুলো।**

```
Requirements → Design → Development → Testing → Deployment → Maintenance
   (what)       (how)     (build)      (verify)   (release)    (support)
```

- **Requirements** — কী বানাতে হবে সেটা ঠিক করা ([Q2](#q2))।
- **Design** — architecture-এর পরিকল্পনা করা ([Q3](#q3))।
- **Development** — code লেখা ([Q4](#q4))।
- **Testing** — কাজ করছে কি না verify করা ([Q6](#q6))।
- **Deployment** — release করা ([Q7](#q7))।
- **Maintenance** — সময়ের সাথে ঠিক করা আর উন্নত করা ([Q8](#q8))।

**ধাপ ৩ — Model-গুলো phase আলাদাভাবে সাজায়।**
- **Waterfall** — phase একবারই চলে, কড়া ক্রমে।
- **Agile** — phase ছোট ছোট cycle-এ বারবার চলে, প্রতি loop-এ feedback আসে ([Q2 Agile](section-18-agile-scrum-bn.md#q2))।
- অন্যগুলো: V-model, Spiral, Iterative।

**ধাপ ৪ — Process রাখার আসল কারণ।**
একটা ঠিক করা lifecycle সমস্যা আগেই ধরে ফেলে (খরচ কম)। এটা delivery-কে আগে থেকে বোঝা যায় এমন করে। আর quality যেন শেষে মনে পড়ার জিনিস না হয়, সেটা নিশ্চিত করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা ভিত্তি। তাঁরা দেখতে চান আপনি software-কে শুধু coding নয়, একটা managed process হিসেবে দেখছেন কি না।

**সাধারণ ভুল:** phase-গুলো যান্ত্রিকভাবে বলে যাওয়া, কিন্তু সেগুলোর সম্পর্ক না বোঝা — যেমন, requirements-এর ভুল আগে ধরা release-এর পরে ধরার চেয়ে অনেক সস্তা, এটা না জানা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আপনি কোন model পছন্দ করেন?"* → Product-এর জন্য সাধারণত Agile (feedback-নির্ভর); fixed-scope বা regulated কাজের জন্য Waterfall।

**সম্পর্কিত:** [Q2 — requirements](#q2) · [Q2 (Agile) — Waterfall বনাম Agile](section-18-agile-scrum-bn.md#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Requirement gathering কী? Functional বনাম non-functional requirement?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Requirement gathering মানে বানানোর আগে জেনে নেওয়া — software-টা আসলে কী করবে। Functional requirement বলে system *কী* করে — feature আর আচরণ, যেমন 'user নিজের password reset করতে পারবে'। Non-functional requirement বলে system কাজটা *কতটা ভালোভাবে* করে — performance, security, scalability, usability। এগুলো জোগাড় করা হয় interview, user story আর prototype দিয়ে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Functional — system কী করে।**
Feature আর আচরণ: "user log in করতে পারবে," "app একটা receipt email পাঠাবে," "admin post delete করতে পারবে।"

**ধাপ ২ — Non-functional — কতটা ভালোভাবে করে।**
Quality-র গুণ, যেগুলো সব feature-এর ওপর দিয়ে যায়:
- **Performance** — screen 2 সেকেন্ডের কমে load হবে।
- **Security** — password encrypted থাকবে; data সুরক্ষিত থাকবে।
- **Scalability** — 10,000 concurrent user সামলাবে।
- **Usability, reliability, accessibility।**

```
Functional:     "the app shows the order history"   (a feature)
Non-functional: "...and loads within 1 second"       (how well)
```

**ধাপ ৩ — কীভাবে এগুলো বের করবেন।**
- Stakeholder-দের সাথে **interview/workshop**।
- **User story** আর acceptance criteria ([Q11 Agile](section-18-agile-scrum-bn.md#q11))।
- অস্পষ্ট ধারণাকে স্পষ্ট করতে **prototype/mockup**।
- না-বলা দরকার খুঁজে পেতে **আসল user-দের দেখা**।

**ধাপ ৪ — এই phase কেন এত গুরুত্বপূর্ণ।**
এখানে ভুল করলে সেটাই সবচেয়ে খরচ বেশি — ভুল জিনিস বানালে পুরো project নষ্ট হয়। আগেভাগে পরিষ্কার করে নিলে (এবং stakeholder-দের সাথে মিলিয়ে নিলে) ভারী rework এড়ানো যায়।

**Interviewer কেন জিজ্ঞেস করে:** ভুল বোঝা requirement project ব্যর্থ হওয়ার সবচেয়ে বড় কারণগুলোর একটা। তাঁরা দেখেন আপনি এটাকে গুরুত্ব দেন কি না।

**সাধারণ ভুল:** non-functional requirement (performance, security) শেষ পর্যন্ত ফেলে রাখা। তখন এগুলো পরে যোগ করা কঠিন এবং খরচ বেশি।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"অস্পষ্ট requirement কীভাবে সামলান?"* → প্রশ্ন করুন, একটা prototype বানান, আর পুরোপুরি বানানোর আগে stakeholder-এর সাথে মিলিয়ে নিন।

**সম্পর্কিত:** [Q1 — SDLC](#q1) · [Q3 — system design](#q3) · [Q11 (Agile) — user story](section-18-agile-scrum-bn.md#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. System design কী, আর HLD ও LLD-র মধ্যে পার্থক্য কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"System design মানে coding-এর আগে ঠিক করা — software-টা কীভাবে বানানো হবে। High-Level Design (HLD) হলো বড় ছবির architecture — প্রধান component-গুলো, সেগুলো কীভাবে যুক্ত, আর tech-এর পছন্দ। Low-Level Design (LLD) হলো প্রতিটা component-এর বিস্তারিত design — class, method, আর data structure। HLD হলো শহরের map; LLD হলো রাস্তা ধরে ধরে বানানো পরিকল্পনা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব উদাহরণ: map-এর দুটো zoom level।**
HLD হলো শহরের map — আপনি এলাকা আর প্রধান সড়ক দেখেন। LLD হলো এক এলাকার street map — ঠিক কোন রাস্তা, কোন বাড়ির নম্বর।

**ধাপ ২ — High-Level Design (HLD)।**
- প্রধান অংশগুলো: app, backend, database, third-party service।
- এরা কীভাবে কথা বলে (REST, GraphQL, message queue)।
- বড় technology-র পছন্দ আর trade-off।
- Architecture pattern (layered, Clean Architecture)।

**ধাপ ৩ — Low-Level Design (LLD)।**
- একটা component-এর ভেতরের class আর তাদের সম্পর্ক।
- Method signature, মূল algorithm, আর data structure।
- এতটাই বিস্তারিত যে একজন developer সেটা implement করতে পারবে।

```
HLD: "App ↔ API Gateway ↔ Auth Service + Order Service ↔ Database"
LLD: "OrderService has placeOrder(Order); Order has id, items, total..."
```

**ধাপ ৪ — দুটোই কেন দরকার।**
HLD পুরো team আর stakeholder-দের একই আকার আর বড় trade-off নিয়ে এক জায়গায় আনে। LLD নিশ্চিত করে প্রতিটা অংশ implement করা যাবে এবং coding শুরুর আগেই সবকিছু মিলে আছে।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি coding-এর আগে পরিকল্পনা করেন কি না, আর architecture ও বিস্তারিত — দুই স্তরেই ভাবতে পারেন কি না।

**সাধারণ ভুল:** কোনো HLD ছাড়াই সরাসরি code-এ ঝাঁপিয়ে পড়া। এতে architecture জট পাকিয়ে যায়, পরে বদলানো কঠিন হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Design কতটা বিস্তারিত হওয়া উচিত?"* → যতটা লাগে সবাইকে এক করতে আর ঝুঁকি কমাতে — এত বেশি নয় যে সেটা জমে যাওয়া, বাড়তি বিস্তারিত document হয়ে যায় (Agile-এ ওটা অপচয়)।

**সম্পর্কিত:** [Q2 — requirements](#q2) · [Q21 — mobile-এর জন্য system design](section-21-system-design-bn.md#q1) · [Q2 (Architecture) — Clean Architecture](section-13-architecture-patterns-bn.md#q2)

[↑ উপরে ফিরুন](#toc)

---

# B. Build ও verify

---

## <a id="q4"></a>4. ভালো development practice দেখতে কেমন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"ভালো development মানে ছোট ছোট, review হওয়া ধাপে পরিষ্কার আর tested code লেখা। বাস্তবে: ছোট branch-এ কাজ করা, coding standard আর linter মেনে চলা, test লেখা, স্পষ্ট message দিয়ে commit করা, code review করানো, আর CI দিয়ে ঘন ঘন integrate করা। লক্ষ্য হলো এমন code — যা সঠিক, পড়ার মতো, আর বদলাতে নিরাপদ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ছোট, ঘন ঘন, review হওয়া increment।**
- **Short-lived branch**-এ কাজ করুন। Review হওয়া PR দিয়ে merge করুন ([Q5](#q5))।
- **ঘন ঘন integrate করুন** (প্রতি push-এ CI test চালায়)। ফলে সমস্যা আগেই সামনে আসে।
- পরিবর্তন **ছোট** রাখুন — review করা সহজ হয়, ঝুঁকিও কম।

**ধাপ ২ — Quality পরে জোড়া নয়, ভেতরেই তৈরি।**
- **Coding standard** মেনে চলুন। **Linter/formatter** নিজে নিজেই চালান ([Q14 Clean Code](section-16-clean-code-bn.md#q14))।
- Code-এর সাথেই **test লিখুন** ([Q6](#q6))।
- একটা স্পষ্ট **Definition of Done** রাখুন। তাহলে "done" মানে সত্যিই done, "আমার machine-এ চলে" নয়।

**ধাপ ৩ — পরিষ্কার history আর যোগাযোগ।**
- **অর্থপূর্ণ commit** (conventional commits) আর PR description ([Q16 Git](section-17-git-bn.md#q16))।
- Ticket/docs update করুন, যাতে পুরো team দেখতে পায়।

**ধাপ ৪ — এটা কেন গুরুত্বপূর্ণ।**
এই অভ্যাসগুলো bug আগেই ধরে ফেলে (সস্তায়)। Codebase সুস্থ থাকে। অনেক মানুষ একসাথে কাজ করতে পারে, বিশৃঙ্খলা ছাড়াই। এগুলো বাদ দিলে debt জমে। পরে পুরো team ধীর হয়ে যায়।

**Interviewer কেন জিজ্ঞেস করে:** এটা আপনার দৈনন্দিন engineering শৃঙ্খলা যাচাই করে, শুধু code লিখতে পারেন কি না তা নয়।

**সাধারণ ভুল:** Big-bang merge (বিশাল branch, কালেভদ্রে integration)। এতে যন্ত্রণাদায়ক conflict হয়, আর bug দেরিতে ধরা পড়ে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CI কী?"* → Continuous Integration: প্রতিটা পরিবর্তন নিজে নিজেই build আর test করা, যাতে integration-এর সমস্যা সাথে সাথে দেখা যায়।

**সম্পর্কিত:** [Q5 — code review](#q5) · [Q6 — testing](#q6) · [Q4 (Clean Code) — clean function](section-16-clean-code-bn.md#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Code review-র উদ্দেশ্য কী? আপনি কী কী দেখেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Code review হলো merge করার আগে দ্বিতীয় একজোড়া চোখ। এর উদ্দেশ্য — bug ধরা, design আর readability উন্নত করা, team-এর মধ্যে জ্ঞান ছড়ানো, আর একটা অভিন্ন standard ধরে রাখা। আমি দেখি correctness, edge case, স্পষ্ট naming, ভালো design, আর test — আর শুধু style-এর কাজটা linter-কে করতে দিই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Review কেন দরকার।**
- **Bug ধরা** — user-এর কাছে পৌঁছানোর আগেই।
- **Design উন্নত করা** — একজন reviewer আরও ভালো পথ খুঁজে পান।
- **জ্ঞান ছড়ানো** — বেশি মানুষ code-টা বোঝে।
- **Consistency** — codebase একরকম থাকে।

**ধাপ ২ — কী কী দেখবেন (গুরুত্ব অনুযায়ী)।**
1. **Correctness** — এটা কি কাজ করে, edge case সহ (খালি, null, error)?
2. **Design** — এটা কি সঠিক জায়গায়, ভালোভাবে সাজানো, বাড়তি জটিল নয়?
3. **Readability** — স্পষ্ট নাম, ছোট function, কোনো চমক নেই।
4. **Tests** — পরিবর্তনগুলো কি test দিয়ে ঢাকা?
5. **Style** — formatter/linter-এর উপর ছেড়ে দিন, খুঁটিনাটি ধরবেন না।

**ধাপ ৩ — ভালো feedback কীভাবে দেবেন।**
- **প্রশ্ন করুন**, হুকুম নয়: "list খালি হলে কী হবে?"
- **ভদ্র আর নির্দিষ্ট** হোন। Code-এর দিকে তাকান, মানুষের দিকে নয়।
- **সময়মতো** দিন — একজন আটকে থাকা teammate খরচ বেশি।
- **যথেষ্ট ভালো হলেই approve করুন**, নিখুঁত হতে হবে না।

**ধাপ ৪ — লেখক হিসেবে।**
PR ছোট রাখুন, স্পষ্ট description লিখুন, আগে নিজে review করুন, আর review চাওয়ার আগে test pass করান ([Q18 Git](section-17-git-bn.md#q18))।

**Interviewer কেন জিজ্ঞেস করে:** Review একজন senior-এর প্রতিদিনের দায়িত্ব। এতে তাঁরা আপনার বুদ্ধি আর সহযোগিতা যাচাই করেন।

**সাধারণ ভুল:** Formatting নিয়ে খুঁটিনাটি ধরা (যেটা tool-এর কাজ), আর আসল correctness/design সমস্যা মিস করা। অথবা কড়া, অস্পষ্ট feedback দেওয়া ("this is wrong")।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Review-তে মতভেদ হলে কী করেন?"* → Trade-off নিয়ে আলোচনা করুন, data/standard-কে প্রাধান্য দিন, দরকার হলে team-এর কাছে নিয়ে যান — আলোচনাটা code নিয়েই রাখুন।

**সম্পর্কিত:** [Q18 (Git) — PR best practice](section-17-git-bn.md#q18) · [Q4 — dev practice](#q4) · [Q22 (Leadership) — code review](section-22-leadership-behavioral-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. Testing-এর পর্যায়গুলো কী কী? unit, integration, system, আর UAT ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Testing হয় কয়েকটা স্তরে, ছোট থেকে বড়। Unit test একটা অংশকে আলাদা করে যাচাই করে। Integration test দেখে অংশগুলো একসাথে কাজ করে কি না। System testing পুরো app-কে শুরু থেকে শেষ পর্যন্ত যাচাই করে। UAT (User Acceptance Testing) মানে আসল user বা client নিশ্চিত করেন যে এটা তাঁদের দরকার মেটায়। প্রতিটা স্তর আলাদা ধরনের bug ধরে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা বাড়ি বানানো।**
- **Unit** — একটা ইট পরীক্ষা করা।
- **Integration** — একটা দেয়াল পরীক্ষা করা (ইটগুলো একসাথে)।
- **System** — পুরো বাড়িটা ঘুরে দেখা।
- **UAT** — মালিক দেখে সই করে দেন।

**ধাপ ২ — চারটি স্তর।**

| স্তর | কী পরীক্ষা করে | উদাহরণ |
|---|---|---|
| Unit | একটা function/class একা | একটা `calculateTotal()` function |
| Integration | অংশগুলো একসাথে কাজ করছে কি না | repository + API layer |
| System | পুরো app শুরু থেকে শেষ | device-এ পুরো checkout flow |
| UAT | client/user-এর গ্রহণযোগ্যতা | customer নিশ্চিত করেন এটা তাঁর দরকার মেটায় |

**ধাপ ৩ — বেশিরভাগ test কোথায় থাকা উচিত (pyramid)।**
বেশিরভাগ test হওয়া উচিত দ্রুত **unit** test। তার চেয়ে কম **integration**। আর সবচেয়ে কম ধীর **end-to-end** test। এই "test pyramid" suite-টাকে দ্রুত আর ভরসা করা যায় এমন রাখে ([Q6 Flutter Testing](section-06-testing-bn.md#q1))।

**ধাপ ৪ — কে কী করে।**
Developer-রা unit/integration test লেখেন। System testing প্রায়ই QA চালান। **Client বা end user** UAT করেন। UAT-এর কথা হলো *কাজের উপযোগী কি না*, শুধু "কোনো bug নেই" নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি testing-কে স্তরভিত্তিক হিসেবে বোঝেন কি না, নাকি শুধু "শেষে test করি" ভাবেন।

**সাধারণ ভুল:** শুধু manual end-to-end testing-এর উপর নির্ভর করা (ধীর, অস্থির), আর খুব কম unit test রাখা — উল্টো pyramid।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Regression testing?"* → পরিবর্তনের পরে আবার test চালানো, যাতে নিশ্চিত হওয়া যায় পুরোনো আচরণ ভাঙেনি — automated test এটা সস্তা করে দেয়।

**সম্পর্কিত:** [Q6 (Flutter) — Flutter-এ testing](section-06-testing-bn.md#q1) · [Q11 — shift-left](#q11)

[↑ উপরে ফিরুন](#toc)

---

# C. Ship ও maintain

---

## <a id="q7"></a>7. Deployment process কী? Staging বনাম production, আর deployment checklist-এ কী কী থাকে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Deployment মানে software-টা একটা environment-এ release করা। Staging হলো production-এর প্রায় হুবহু কপি, শেষ test-এর জন্য (একটা ড্রেস রিহার্সাল)। Production হলো live environment, যেখানে আসল user আসে। Deployment checklist নিরাপদ release নিশ্চিত করে: test pass করেছে, backup/rollback পরিকল্পনা আছে, config আর secret ঠিক আছে, আর monitoring তৈরি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Environment-গুলো।**

```
Local (your machine) → Dev → Staging (like production) → Production (real users)
```

- **Staging** — যতটা সম্ভব production-এর মতো। শেষ testing এখানেই হয়।
- **Production** — আসল, live system। এখানে ভুল হলে user-রা ভোগেন।

**ধাপ ২ — Staging environment কেন দরকার।**
এটা এমন সমস্যা ধরে, যা শুধু production-এর মতো setup-এ দেখা যায় (আসল config, data-র পরিমাণ, integration) — মূল রাতের আগে ড্রেস রিহার্সাল।

**ধাপ ৩ — একটা deployment checklist।**
- সব test আর CI check pass করেছে।
- Database migration তৈরি (আর ফিরিয়ে নেওয়া যায় এমন)।
- লক্ষ্য environment-এর জন্য config আর secret ঠিক আছে।
- কিছু ভেঙে গেলে একটা **rollback plan** আছে।
- সমস্যা ধরতে monitoring/alert তৈরি।
- Stakeholder-দের জানানো হয়েছে। ঝুঁকির হলে কম traffic-এর সময়ে deploy করুন।

**ধাপ ৪ — আরও নিরাপদ release কৌশল।**
- **Blue-green** — দুটো production environment চালান, traffic সাথে সাথে switch করুন (rollback সহজ)।
- **Canary** — প্রথমে অল্প শতাংশে release করুন, দেখুন, তারপর সবার জন্য ছাড়ুন।
- **Feature flags** — code বন্ধ অবস্থায় ship করুন, ধীরে ধীরে চালু করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি rollback আর monitoring রেখে নিরাপদে release করেন কি না — "prod-এ push করে দোয়া করা" নয়।

**সাধারণ ভুল:** Rollback plan বা monitoring ছাড়া deploy করা। ফলে একটা খারাপ release লম্বা outage হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"দ্রুত rollback কীভাবে করবেন?"* → Blue-green switch করা, আগের build আবার deploy করা, অথবা একটা feature flag বন্ধ করে দেওয়া।

**সম্পর্কিত:** [Q10 (CI/CD) — release](section-10-cicd-release-bn.md#q1) · [Q9 — production bug](#q9)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Maintenance দেখতে কেমন? Bug tracking, hotfix, আর versioning কীভাবে সামলান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Maintenance মানে release-এর পরের সবকিছু — bug ঠিক করা, performance উন্নত করা, আর ছোট পরিবর্তন যোগ করা। Bug একটা tool-এ (Jira/GitHub Issues) priority সহ track করা হয়। Hotfix হলো জরুরি fix, যা production থেকে branch করে দ্রুত ship করা হয়। Versioning (semantic versioning: major.minor.patch) বলে দেয় প্রতিটা release কত বড়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — একটা product-এর জীবনের বেশিরভাগটাই maintenance।**
একটা product প্রথমবার বানানোর চেয়ে অনেক বেশি সময় maintenance-এ কাটায়। ভালো maintenance মানে issue track করা, priority অনুযায়ী ঠিক করা, আর app সুস্থ রাখা।

**ধাপ ২ — Bug tracking।**
- প্রতিটা bug লিখে রাখুন — কীভাবে reproduce করতে হয়, severity, আর priority সহ।
- নিয়মিত triage করুন — critical bug দ্রুত ঠিক করুন, বাকিগুলো সময়সূচিতে রাখুন।

**ধাপ ৩ — Hotfix।**
জরুরি production সমস্যার জন্য সরাসরি production থেকে branch করুন, সংকীর্ণভাবে fix করুন, test করুন, deploy করুন, তারপর main-এ merge করে ফেরত আনুন ([Q19 Git](section-17-git-bn.md#q19))।

**ধাপ ৪ — Semantic versioning (semver)।**

```
MAJOR.MINOR.PATCH   e.g. 2.4.1

PATCH (2.4.1 → 2.4.2)  bug fix, backward compatible
MINOR (2.4.1 → 2.5.0)  new feature, backward compatible
MAJOR (2.4.1 → 3.0.0)  breaking change
```

এটা user-দের এক নজরেই বলে দেয় upgrade করা কতটা ঝুঁকির কাজ।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি launch-এর পরের কথাও ভাবেন কি না — engineering-এর বেশিরভাগ পরিশ্রমই maintenance।

**সাধারণ ভুল:** Versioning-কে হালকাভাবে নেওয়া (যেমন খুশি নম্বর)। ফলে user বুঝতে পারেন না কোনটা breaking change আর কোনটা patch।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Regression কী?"* → একটা bug আবার ফিরে আসা, অথবা নতুন পরিবর্তন পুরোনো আচরণ ভেঙে দেওয়া — automated test এগুলো ধরে ফেলে।

**সম্পর্কিত:** [Q9 — production bug](#q9) · [Q19 (Git) — hotfix](section-17-git-bn.md#q19) · [Q16 (Git) — conventional commits/versioning](section-17-git-bn.md#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. Production bug কীভাবে handle করেন? পুরো process-টা বলুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি একটা পরিষ্কার order মেনে চলি: প্রথমে ক্ষতি আটকাই (mitigate করি, যাতে user-রা কষ্ট না পান), তারপর reproduce করে diagnose করি, তারপর fix করে test করি, তারপর fix-টা নিরাপদে deploy করি, আর শেষে blameless post-mortem করি যাতে এটা আবার না ঘটে। মূল ভাবনা হলো — 'আগে রক্তপাত থামাও, root cause পরে খোঁজো'।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — আগে contain করুন (রক্তপাত থামান)।**
User-এর উপর প্রভাব সাথে সাথে কমান: খারাপ release roll back করুন, feature flag বন্ধ করুন, বা ভাঙা feature-টা disable করুন। User-রা ভুগছেন আর আপনি এক ঘণ্টা ধরে debug করছেন — এটা করবেন না। আগে mitigate করুন।

**ধাপ ২ — Reproduce করুন আর diagnose করুন।**
- Bug-টা প্রতিবার একইভাবে reproduce করুন (report, log, আর Crashlytics/Sentry-র মতো crash report থেকে)।
- শুধু উপসর্গ নয়, **root cause** খুঁজে বের করুন।

**ধাপ ৩ — Fix করুন, test করুন, নিরাপদে deploy করুন।**
- একটা নির্দিষ্ট fix লিখুন, আর সাথে একটা **test** লিখুন যেটা এই bug ধরে ফেলত (যাতে এটা আর কখনো ফিরে না আসে)।
- Rollback plan সহ hotfix process দিয়ে deploy করুন ([Q19 Git](section-17-git-bn.md#q19))।

**ধাপ ৪ — Post-mortem (blameless)।**
সমস্যা মিটে যাওয়ার পরে team মিলে review করে: কী হয়েছিল, কেন হয়েছিল, আর কীভাবে ঠেকানো যায় (ভালো test, monitoring, alert)। **Blameless** মানে system আর process-এর দিকে নজর দেওয়া, কোনো মানুষকে শাস্তি দেওয়া নয় — এতে মানুষ সত্যি কথা বলে।

**ধাপ ৫ — পুরো সময় জুড়ে যোগাযোগ রাখুন।**
গুরুতর incident-এর সময় stakeholder আর user-দের জানিয়ে রাখুন — চুপ থাকা খারাপ খবরের চেয়েও খারাপ।

**Interviewer কেন জিজ্ঞেস করে:** Incident handle করা senior-দের একটা মূল দক্ষতা। তাঁরা দেখতে চান আপনি "আগে contain, পরে root cause, সবসময় প্রতিরোধ" ভাবেন কি না।

**সাধারণ ভুল:** User-রা ভুগছেন, অথচ সরাসরি debug করতে বসে যাওয়া (আগে mitigate করা উচিত)। অথবা উপসর্গ ঠিক করা, কিন্তু বারবার একই জিনিস ঠেকানোর test না লেখা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Blameless post-mortem কেন?"* → ভয় থাকলে তথ্য চাপা পড়ে যায়। Blameless review আসল কারণগুলো সামনে আনে, ফলে system উন্নত হয়।

**সম্পর্কিত:** [Q7 — deployment ও rollback](#q7) · [Q19 (Git) — hotfix](section-17-git-bn.md#q19)

[↑ উপরে ফিরুন](#toc)

---

# D. Quality, risk ও docs

---

## <a id="q10"></a>10. শুধু testing-এর সময় নয়, পুরো SDLC জুড়ে quality কীভাবে নিশ্চিত করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"শেষে test করে quality ঢোকানো যায় না — এটা প্রতিটা পর্যায়ে গড়ে তুলতে হয়। মানে পরিষ্কার requirement, ভালো design review, coding standard আর linter, code-এর সাথেই লেখা test, code review, CI check, আর production-এ monitoring। প্রতিটা পর্যায়ের নিজের quality gate থাকে, ফলে সমস্যা সেখানেই ধরা পড়ে যেখানে ঠিক করা সবচেয়ে সস্তা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মূল ধারণা: quality সবার কাজ, সবসময়।**
Bug আগে ধরলে ঠিক করা সবচেয়ে সস্তা। Design পর্যায়ে ধরা পড়া requirement-এর ভুলের খরচ সামান্য। একই ভুল release-এর পরে ধরা পড়লে খরচ বিশাল।

**ধাপ ২ — প্রতিটা পর্যায়ে quality gate।**

| পর্যায় | Quality gate |
|---|---|
| Requirements | পরিষ্কার, নিশ্চিত করা, testable acceptance criteria |
| Design | design review, edge case ও non-functional দরকার ভেবে দেখা |
| Development | linter, standard, test, code review |
| Testing | test pyramid + automated regression |
| Deployment | CI check, staging verification, rollback plan |
| Production | monitoring, alert, crash reporting |

**ধাপ ৩ — Gate-গুলো automate করুন।**
CI প্রতিটা change-এ format, lint আর test চালায়। কোনোটা fail করলে merge আটকে দেয়। Automation quality-কে সবসময় একরকম রাখে, আর মানুষের ভুলে যাওয়ার সুযোগ সরিয়ে দেয়।

**ধাপ ৪ — খরচের curve।**
Bug যত পর্যায় পার হয়, ঠিক করার খরচ প্রায় 10× করে বাড়ে। শুরুতেই quality গড়ে তোলা (shift-left, [Q11](#q11)) সবচেয়ে সস্তা কৌশল।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি quality-কে চলতে থাকা কাজ হিসেবে দেখেন, নাকি শেষের একটা QA ধাপ হিসেবে।

**সাধারণ ভুল:** "শেষে test করব" — ততক্ষণে design আর requirement-এর bug ভেতরে বসে গেছে, আর ঠিক করা খরচ বেশি।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Quality কীভাবে মাপেন?"* → Bug escape rate, test coverage (বুদ্ধি সহ), crash-free user, আর fix করার lead time।

**সম্পর্কিত:** [Q11 — shift-left](#q11) · [Q6 — testing phase](#q6) · [Q14 (Clean Code) — enforcing](section-16-clean-code-bn.md#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. Shift-Left testing কী, আর এটা কেন গুরুত্বপূর্ণ?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Shift-left মানে testing আর quality check-গুলোকে timeline-এর আগের দিকে ('বাঁ দিকে') সরিয়ে আনা, শেষের জন্য ফেলে না রাখা। আপনি build করতে করতেই test করেন, CI-তে check automate করেন, এমনকি design-এর সময়েও QA-কে যুক্ত করেন। এটা গুরুত্বপূর্ণ কারণ আগে ধরা পড়া bug ঠিক করা production-এ পাওয়া bug-এর চেয়ে অনেক সস্তা আর দ্রুত।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ছবিটা।**

```
Traditional:  build everything ............... then TEST at the end (right)
Shift-left:   TEST from the start → → → and all along the way (left)
```

**ধাপ ২ — বাস্তবে এটা দেখতে কেমন।**
- Developer-রা **code লেখার সাথে সাথেই unit test লেখেন** (বা TDD করেন)।
- **CI প্রতিটা commit-এ নিজে থেকেই test চালায়**।
- QA যুক্ত হন **requirements/design**-এর সময়ে, শুধু শেষে নয়।
- **Static analysis/linter** code চালু হওয়ার আগেই সমস্যা ধরে ফেলে।

**ধাপ ৩ — এটা কেন সস্তা।**
Code লেখার সময় পাওয়া bug ঠিক করতে হয়তো কয়েক মিনিট লাগে। একই bug production-এ পাওয়া গেলে সেটা মানে একটা incident, একটা hotfix, আর হারানো বিশ্বাস — খরচ বহু গুণ বেশি। Shift-left ধরা পড়ার জায়গাটাকে সস্তা দিকে সরিয়ে আনে।

**ধাপ ৪ — ফলাফল।**
দ্রুত feedback, production-এ কম bug, আর এমন developer যাঁরা quality-র মালিকানা নেন (শেষে QA-র দিকে "দেয়ালের ওপারে ছুড়ে দেওয়া" নয়)।

**Interviewer কেন জিজ্ঞেস করে:** এটা আধুনিক quality ভাবনা যাচাই করে, আর CI/CD ও DevOps-এর সাথে মিলে যায়।

**সাধারণ ভুল:** ভাবা যে shift-left মানে "developer-রাই সব test করবেন, QA লাগবে না।" এর মানে হলো *সবাই* *আগে* test করে, QA-ও।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CI কীভাবে shift-left সম্ভব করে?"* → এটা প্রতিটা change-এ check-গুলো নিজে থেকেই আগে চালায়, আর সাথে সাথে feedback দেয়।

**সম্পর্কিত:** [Q10 — পুরো জুড়ে quality](#q10) · [Q12 — DevOps](#q12) · [Q6 — testing](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. DevOps culture কী, আর এটা SDLC-র সাথে কীভাবে সম্পর্কিত?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"DevOps হলো এমন একটা culture যেখানে development আর operations এক team হিসেবে কাজ করে। Software build করা, release করা আর চালানোর দায়িত্ব তারা ভাগ করে নেয়। এতে automation ব্যবহার হয় — CI/CD, infrastructure as code, monitoring — যাতে দ্রুত আর নিশ্চিন্তে ship করা যায়। SDLC-র ভাষায়, এটা development, deployment আর maintenance-এর মধ্যের loop-টা শক্ত করে, ফলে feedback দ্রুত আসে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — DevOps কোন সমস্যা সমাধান করে।**
আগে developer-রা code বানিয়ে সেটা operations-এর দিকে "দেয়ালের ওপারে ছুড়ে দিতেন" চালানোর জন্য — আর কিছু ভাঙলে একে অপরকে দোষ দিতেন। DevOps সেই দেয়ালটা সরিয়ে দেয়: এক team পুরো lifecycle-এর মালিক।

**ধাপ ২ — মূল practice-গুলো।**
- **CI/CD** — নিজে থেকেই build, test আর deploy করা ([Q10 CI/CD](section-10-cicd-release-bn.md#q1))।
- **Infrastructure as Code** — server/config version-controlled file-এ লেখা থাকে।
- **Monitoring ও observability** — production-এ system কেমন আচরণ করছে তা দেখা।
- **সব জায়গায় automation** — কম হাতে করা কাজ, কম ভুল।

**ধাপ ৩ — Cultural অংশ (সবচেয়ে গুরুত্বপূর্ণ)।**
- ভাগ করা মালিকানা ("you build it, you run it")।
- দ্রুত feedback আর একটানা উন্নতি।
- Incident-এর জন্য blameless culture ([Q9](#q9))।

**ধাপ ৪ — SDLC-র সাথে সম্পর্ক।**
DevOps SDLC-কে এক-মুখী সরলরেখার বদলে একটা দ্রুত, চলতে থাকা loop বানায় — code দ্রুত আর নিরাপদে production-এ যায়, আর production-এর feedback সোজা development-এ ফিরে আসে।

**Interviewer কেন জিজ্ঞেস করে:** আধুনিক team-এ DevOps স্বাভাবিক ব্যাপার। তাঁরা দেখেন আপনি বোঝেন কি না যে এটা culture + automation, শুধু "একটা tools team" নয়।

**সাধারণ ভুল:** ভাবা যে DevOps মানে শুধু একটা job title বা কিছু tool। এটা মূলত ভাগ করা মালিকানার একটা culture, যেটা automation সম্ভব করে তোলে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CI vs CD?"* → CI = প্রতিটা change নিজে থেকেই integrate + test করা; CD = সেই test করা change নিজে থেকেই deliver/deploy করা।

**সম্পর্কিত:** [Q11 — shift-left](#q11) · [Q10 (CI/CD)](section-10-cicd-release-bn.md#q1) · [Q7 — deployment](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. Software project-এ risk management কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Risk management মানে কী কী ভুল হতে পারে সেটা ঘটার আগেই খুঁজে বের করা, আর তার জন্য পরিকল্পনা রাখা। আপনি risk চিহ্নিত করেন (technical, schedule, মানুষ, বাইরের), প্রতিটাকে বিচার করেন — কতটা সম্ভাবনা আর প্রভাব কতটা খারাপ হবে। তারপর গুরুত্বপূর্ণগুলো mitigate করেন — আর নজর রাখতে থাকেন। এটা ঠিক ভ্রমণের আগে আবহাওয়া দেখে নেওয়ার মতো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Risk চিহ্নিত করুন।**
সাধারণ ধরনগুলো: নতুন একটা technology যেটা কাজ নাও করতে পারে, একটা কড়া deadline, একজন গুরুত্বপূর্ণ মানুষের চলে যাওয়া, একটা third-party API যেটা বদলে যেতে পারে, অস্পষ্ট requirement।

**ধাপ ২ — সম্ভাবনা × প্রভাব দিয়ে যাচাই করুন।**

```
            Impact: Low        High
Likelihood
   High        monitor       ACT NOW (top priority)
   Low         ignore        have a plan ready
```

আপনার শক্তি ঢালুন high-likelihood, high-impact risk-গুলোর উপরে।

**ধাপ ৩ — Mitigate করুন।**
- **সম্ভাবনা কমান** — যেমন নতুন tech-এর ঝুঁকি কমাতে একটা spike করুন ([Q15](#q15))।
- **প্রভাব কমান** — যেমন একটা backup plan, বা schedule-এ বাড়তি buffer।
- **এড়িয়ে যান** — approach বদলে risk-টাকে পাশ কাটান।
- **মেনে নিন** — ছোট risk-গুলোর ক্ষেত্রে শুধু স্বীকার করে নিন।

**ধাপ ৪ — নজর রাখতে থাকুন।**
Project চলার সাথে সাথে risk বদলায়। নিয়মিত review করুন (একটা risk register রাখুন) আর plan update করুন। নতুন risk আসে; পুরোনোগুলো মিলিয়ে যায়।

**Interviewer কেন জিজ্ঞেস করে:** Senior engineer-রা সমস্যা আগেই আঁচ করেন। তাঁরা দেখতে চান আপনি আগে থেকে ভাবেন, শুধু আগুন নেভানোর কাজ করেন না।

**সাধারণ ভুল:** Risk-গুলোকে বিপদ হয়ে ওঠা পর্যন্ত বাদ দেওয়া। অথবা সম্ভাবনা × প্রভাব দিয়ে অগ্রাধিকার না দিয়ে সব risk-কে সমান ভাবা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"নতুন technology-র ঝুঁকি কীভাবে কমান?"* → পুরোপুরি নামার আগে একটা time-boxed spike দিয়ে প্রমাণ করে নিই যে এটা কাজ করে ([Q15](#q15))।

**সম্পর্কিত:** [Q15 — spike](#q15) · [Q2 — requirements (অস্পষ্ট = risk)](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. কী কী document করা উচিত, আর কী কী নিয়ে over-document করা উচিত নয়?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"যেসব জিনিস মানুষের দরকার কিন্তু code বলতে পারে না, সেগুলো document করি: architecture decision আর *কেন*, setup/onboarding-এর ধাপ, API contract, আর operation-এর জন্য runbook। যেসব জিনিস সারাক্ষণ বদলায় বা code নিজেই বলে দেয়, সেগুলো নিয়ে over-document করি না — যেমন line-by-line comment বা বিস্তারিত spec, যেগুলো পুরোনো হয়ে যায়। ভালো docs কাজে লাগে আর maintain করা হয়; খারাপ docs ভুল পথে নিয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — যা document করা মূল্যবান ('কেন' আর 'কীভাবে চালাতে হয়')।**
- **Architecture decision** আর *কেন* (ADR — Architecture Decision Record)।
- **Onboarding/setup** — project কীভাবে চালাতে হয়।
- **API contract** — endpoint, request/response-এর গঠন।
- **Runbook** — কীভাবে deploy করবেন, roll back করবেন, incident সামলাবেন।
- **যেসব business rule সহজে বোঝা যায় না।**

**ধাপ ২ — যা নিয়ে over-document করা উচিত নয়।**
- যেসব comment code-এর কথাই আবার বলে (`i++; // increment`)।
- বিশাল spec, যেগুলো দ্রুত বদলানো detail আটকে রাখে আর পুরোনো হয়ে যায়।
- যা ভালো নামের কারণে code নিজেই পরিষ্কার করে দেয় ([Q6 Clean Code](section-16-clean-code-bn.md#q6))।

**ধাপ ৩ — মূল নিয়ম।**
**কেন** document করুন, **কী** নয়। Code দেখায় *কী* করছে; docs-এ থাকা উচিত *কেন* একটা decision নেওয়া হলো, আর যে জ্ঞানটা code-এ নেই।

**ধাপ ৪ — Docs জীবিত রাখুন।**
পুরোনো docs না থাকার চেয়েও খারাপ — এগুলো ভুল পথে নিয়ে যায়। Docs code-এর কাছাকাছি রাখুন, হালকা রাখুন, আর কিছু বদলালে update করুন। যে doc maintain করা যাবে না, সেটা লিখবেন না।

**Interviewer কেন জিজ্ঞেস করে:** এটা judgment যাচাই করে — সাহায্য করার মতো যথেষ্ট documentation, কিন্তু এত বেশি নয় যে সেটা বোঝা হয়ে পচে যায়।

**সাধারণ ভুল:** হয় কোনো documentation-ই নেই (নতুন মানুষ হারিয়ে যায়), নয়তো বিশাল বিস্তারিত docs যেগুলো কেউ update করে না আর যেগুলো দ্রুত ভুল পথে নিয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ADR কী?"* → একটা গুরুত্বপূর্ণ decision আর তার যুক্তির ছোট record, যাতে পরের developer-রা *কেন* সেটা জানতে পারেন।

**সম্পর্কিত:** [Q6 (Clean Code) — comment](section-16-clean-code-bn.md#q6) · [Q3 — design](#q3)

[↑ উপরে ফিরুন](#toc)

---

# E. ধারণা

---

## <a id="q15"></a>15. Spike কী, আর কখন এটা ব্যবহার করবেন?

> Deeper · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Spike হলো ছোট, time-boxed একটা খোঁজখবর। আসল কাজে নামার আগে একটা প্রশ্নের উত্তর দিতে বা ধোঁয়াশা কমাতে এটা করা হয়। যখন estimate বা design করার মতো যথেষ্ট জানা নেই, তখন এটা ব্যবহার করি — যেমন নতুন library চেষ্টা করা, বা একটা approach সম্ভব কি না প্রমাণ করা। এর ফলাফল জ্ঞান, ship করার মতো code নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: scouting trip।**
সবাইকে একটা পথে নামানোর আগে আপনি একজন scout পাঠান, দেখতে যে পথটা পার হওয়া যায় কি না। একটা technical অজানা জিনিসের জন্য spike হলো সেই scouting trip।

**ধাপ ২ — কখন ব্যবহার করবেন।**
- নতুন technology/library, যেটা নিয়ে আপনি নিশ্চিত নন।
- যে story estimate করা যাচ্ছে না, কারণ সেটা খুব অনিশ্চিত।
- কঠিন একটা approach কাজ করে কি না, তার উপর কিছু বানানোর আগে প্রমাণ করা।

**ধাপ ৩ — Time-box রাখুন।**
Spike-এর একটা নির্দিষ্ট সীমা থাকে (যেমন "এটা কাজ করে কি না জানতে ২ দিন")। লক্ষ্য হলো *decide/estimate করার মতো যথেষ্ট শেখা*, তারপর থামা। Time-box না থাকলে খোঁজখবর অনন্তকাল চলতে পারে।

**ধাপ ৪ — ফলাফল একটা decision, feature নয়।**
Spike সাধারণত শেষ হয় একটা recommendation আর ভালো estimate দিয়ে — আর throwaway code প্রায়ই ফেলে দেওয়া হয়। আসল deliverable হলো কমে যাওয়া ধোঁয়াশা।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি কাজে নামার আগে অজানা জিনিসের ঝুঁকি কমান কি না — পরিপক্ব planning-এর লক্ষণ।

**সাধারণ ভুল:** Spike-কে সীমা ছাড়া চলতে দেওয়া (এটা তখন গর্তে পড়ে যাওয়ার মতো হয়), বা throwaway spike code-কেই আসল সমাধান হিসেবে ship করার চেষ্টা করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Spike আর সাধারণ story-র পার্থক্য?"* → Story একটা feature দেয়; spike দেয় জ্ঞান, যাতে পরের story estimate করা যায়।

**সম্পর্কিত:** [Q13 — risk management](#q13) · [Q12 (Agile) — story point](section-18-agile-scrum-bn.md#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Bug, defect আর feature request-এর মধ্যে পার্থক্য কী?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-19-sdlc.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Defect হলো software-এর একটা ভুল, যেকোনো পর্যায়ে পাওয়া যায়; bug হলো সেই defect-এর চলতি শব্দ, যেটা software চলার সময়ে ধরা পড়ে — এটা requirement-এর চেয়ে আলাদা আচরণ করে। Feature request হলো *নতুন* একটা ক্ষমতা, যেটা কেউ চায় কিন্তু requirement-এ কখনো ছিল না। মূল পার্থক্য: bug/defect মানে 'এটা ভেঙে গেছে'; feature request মানে 'আমি নতুন কিছু চাই'।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — পার্থক্যগুলো।**
- **Defect** — যা হওয়ার কথা ছিল তার তুলনায় একটা ভুল। প্রায়ই testing/review-তে পাওয়া সমস্যার জন্য ব্যবহার হয়।
- **Bug** — defect-এর দৈনন্দিন শব্দ, সাধারণত software চলার সময়ে পাওয়া যায়।
- **Feature request** — নতুন functionality-র জন্য অনুরোধ, যেটা specify করা ছিল না।

(অনেক team-এ "bug" আর "defect" একই অর্থে ব্যবহার হয়; গুরুত্বপূর্ণ সীমারেখা হলো *ভাঙা* বনাম *নতুন*।)

**ধাপ ২ — পার্থক্যটা কেন গুরুত্বপূর্ণ।**
- **Bug/defect** মানে software তার বর্তমান requirement পূরণ করছে না → ঠিক করুন (contract-এ প্রায়ই বাড়তি টাকা লাগে না)।
- **Feature request** মানে নতুন scope → এটা estimate হয়, prioritize হয়, আর বাড়তি খরচ/সময় লাগতে পারে।

```
Requirement: "users can reset their password"
Bug:         the reset email never arrives          → it's broken, fix it
Feature:     "also allow reset via SMS"              → new scope, plan it
```

**ধাপ ৩ — Team-রা কেন এটা নিয়ে ভাবে।**
একটা feature-কে "bug" নাম দিলে scope creep বিনামূল্যে ঢুকে পড়ে; একটা bug-কে "feature" নাম দিলে আসল defect পেছনে পড়ে যায়। পরিষ্কার শ্রেণিভাগ planning আর contract-কে সৎ রাখে।

**Interviewer কেন জিজ্ঞেস করে:** এটা সমস্যা নিয়ে নিখুঁত communication যাচাই করে — planning আর client সম্পর্কের জন্য গুরুত্বপূর্ণ।

**সাধারণ ভুল:** প্রতিটা নতুন অনুরোধকে "bug" বলা, যাতে দ্রুত কাজটা হয়ে যায়; অথবা একটা আসল defect-কে "শুধু একটা feature request" বলে উড়িয়ে দেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"'Enhancement' হলে কী?"* → বর্তমান functionality-তে ছোট একটা উন্নতি — তবুও এটা নতুন scope, defect নয়।

**সম্পর্কিত:** [Q8 — bug tracking](#q8) · [Q11 (Agile) — user story](section-18-agile-scrum-bn.md#q11)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর সকালে এটা পড়ুন। আগে table, তারপর এক লাইনের মনে করিয়ে দেওয়া কথাগুলো।

## SDLC-র পর্যায়

```
Requirements → Design → Development → Testing → Deployment → Maintenance
   (what)       (how)     (build)      (verify)   (release)    (support)
```

## Testing-এর স্তর (ছোট → বড়)

| স্তর | কী check করে |
|---|---|
| Unit | একটা অংশ একা |
| Integration | অংশগুলো একসাথে |
| System | পুরো app শুরু থেকে শেষ |
| UAT | client/user-এর অনুমোদন |

## যে জোড়াগুলো গুলিয়ে যায়

| | A | B |
|---|---|---|
| Functional বনাম non-functional | কী করে | কতটা ভালোভাবে করে |
| HLD বনাম LLD | architecture (শহরের মানচিত্র) | detail (রাস্তার মানচিত্র) |
| Staging বনাম production | মহড়া | live |
| Bug বনাম feature request | এটা ভাঙা | নতুন scope |

## এক লাইনের মনে করিয়ে দেওয়া কথা

- **SDLC** = requirements → design → build → test → deploy → maintain। ([Q1](#q1))
- **Functional** = কী; **non-functional** = কতটা ভালো (perf, security)। ([Q2](#q2))
- **HLD** = বড় ছবির architecture; **LLD** = বিস্তারিত class/method। ([Q3](#q3))
- **Code review** — আগে correctness আর design; style-এর কাজ linter-কে দিন। ([Q5](#q5))
- **Test pyramid** — অনেক unit, কম integration, খুব কম end-to-end। ([Q6](#q6))
- **Staging** production-এর মতো হয়; সবসময় একটা **rollback plan** রাখুন। ([Q7](#q7))
- **Semver**: PATCH=fix, MINOR=feature, MAJOR=breaking। ([Q8](#q8))
- **Production bug**: আগে contain → diagnose → fix+test → blameless post-mortem। ([Q9](#q9))
- **প্রতিটা পর্যায়ে quality তৈরি করা হয়**, শেষে test করে ঢোকানো হয় না। ([Q10](#q10))
- **Shift-left** = আগে test করুন; আগের bug অনেক সস্তা। ([Q11](#q11))
- **DevOps** = dev + ops এক team, automated (CI/CD), ভাগাভাগি করা মালিকানা। ([Q12](#q12))
- **Risk** = likelihood × impact; বড়গুলো mitigate করুন, নজর রাখতে থাকুন। ([Q13](#q13))
- ***কেন*** **document করুন**, *কী* নয়; docs জীবিত রাখুন। ([Q14](#q14))
- **Spike** = ধোঁয়াশা কমানোর জন্য time-boxed খোঁজখবর। ([Q15](#q15))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: interviewer-রা কীভাবে আরও গভীরে যান

Process interview চাপের মধ্যে judgment যাচাই করে। জোরে বলে অনুশীলন করুন:

1. *"আপনার SDLC-টা আমাকে বুঝিয়ে বলুন।"* → পর্যায়গুলো বলুন, কিন্তু জোর দিন সমস্যা আগে ধরার উপর (সস্তা)।
2. *"Production down — আপনার প্রথম কাজ কী?"* → contain (rollback/flag), তারপর diagnose, তারপর একটা test সহ fix।
3. *"আপনি quality কীভাবে নিশ্চিত করেন?"* → প্রতিটা পর্যায়ে তৈরি করা হয়, CI-তে automated, shift-left।
4. *"একটা library কাজ করবে কি না নিশ্চিত নন — আপনি কী করবেন?"* → কাজে নামার আগে ঝুঁকি কমাতে একটা time-boxed spike।
5. *"এটা কি bug না feature?"* → ভাঙা বনাম নতুন scope; এটা বদলে দেয় কে টাকা দেবে আর কীভাবে plan হবে।

প্রতিটা পর্যায়কে *খরচ, quality আর ঝুঁকির* সাথে যুক্ত করা — শুধু নাম বলা নয় — এটাই senior signal, remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
