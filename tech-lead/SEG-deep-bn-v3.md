# 📘 The Software Engineer's Guidebook
## গভীর বাংলা সংস্করণ — সমস্যা, কারণ ও সমাধানসহ
### Gergely Orosz রচিত | Expert-Level বাংলা গাইড

> এই বইটি শুধু Topic-এর তালিকা নয়। এটি একজন Engineer-এর ক্যারিয়ারে যে **আসল সমস্যাগুলো** আসে, সেগুলোর **কারণ** এবং **সমাধান** নিয়ে।

---

## 📑 সূচিপত্র (Table of Contents)

**[Part 1 — ক্যারিয়ারের ভিত্তি](#part-1)**
- [১.১ কোম্পানির ধরন ও আপনার ক্যারিয়ার](#11)
- [১.২ Engineering Ladder — সিঁড়ির প্রতিটি ধাপ](#12)
- [১.৩ নিজের ক্যারিয়ারের দায়িত্ব নিজে নিন](#13)
- [১.৪ Work Log — কেন রাখবেন ও কীভাবে রাখবেন](#14)
- [১.৫ Feedback — দেওয়া ও নেওয়ার আসল শিল্প](#15)
- [১.৬ Manager-এর সাথে সম্পর্ক](#16)
- [১.৭ Performance Review — কীভাবে সফল হবেন](#17)
- [১.৮ Promotion — কেন আটকায় ও কীভাবে পাবেন](#18)
- [১.৯ বিভিন্ন Environment-এ টিকে থাকা](#19)
- [১.১০ Job Change — কখন, কেন ও কীভাবে](#110)

**[Part 2 — দক্ষ Developer হওয়া](#part-2)**
- [২.১ কাজ সঠিকভাবে শেষ করার শিল্প](#21)
- [২.২ Coding-এর গভীর দক্ষতা](#22)
- [২.৩ Debugging — সমস্যা খোঁজার পদ্ধতি](#23)
- [২.৪ Software Development Practices](#24)
- [২.৫ Testing — সঠিকভাবে ও গভীরভাবে](#25)
- [২.৬ উৎপাদনশীলতার Tools ও Habits](#26)

**[Part 3 — Senior Engineer হওয়া](#part-3)**
- [৩.১ Senior Engineer-এর আসল পার্থক্য ও দায়িত্ব](#31)
- [৩.২ Code Review — সংস্কৃতি ও দক্ষতা](#32)
- [৩.৩ Mentoring — কার্যকর শেখানো](#33)
- [৩.৪ Technical Debt — চেনা, বোঝা ও সামলানো](#34)
- [৩.৫ Software Architecture — প্রথম পদক্ষেপ](#35)
- [৩.৬ Collaboration ও Teamwork — Senior স্তরে](#36)
- [৩.৭ Senior Software Engineering — গভীরে](#37)

**[Part 4 — Tech Lead হওয়া](#part-4)**
- [৪.১ Tech Lead-এর আসল ভূমিকা](#41)
- [৪.২ Project Planning ও Risk Management](#42)
- [৪.৩ Production-এ Ship করা](#43)
- [৪.৪ Stakeholder Management](#44)
- [৪.৫ Team গড়া ও Psychological Safety](#45)
- [৪.৬ Team Structure — Conway's Law ও Team Topology](#46)
- [৪.৭ Team Dynamics — গভীরে](#47)

**[Part 5 — Staff ও Principal Engineer](#part-5)**
- [৫.১ Staff Engineer-এর দুনিয়া](#51)
- [৫.২ Business বোঝা ও Technical সংযোগ](#52)
- [৫.৩ Influence Without Authority](#53)
- [৫.৪ Reliable Systems তৈরি করা](#54)
- [৫.৫ Large-Scale Architecture](#55)
- [৫.৬ Staff স্তরের Collaboration](#56)
- [৫.৭ Staff স্তরের Software Engineering](#57)

**[Appendix — দরকারি Reference](#appendix)**

**[শেষ কথা](#conclusion)**

---

<a name="part-1"></a>
# Part 1 — ক্যারিয়ারের ভিত্তি

---

<a name="11"></a>
## ১.১ কোম্পানির ধরন ও আপনার ক্যারিয়ার

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

অনেক Engineer ক্যারিয়ার শুরু করেন কোনো পরিকল্পনা ছাড়াই — "যেকোনো কোম্পানিতে Job পেলেই হয়।" কিন্তু কয়েক বছর পরে দেখেন — একই Level-এ আটকে আছেন, বেতন কম, শেখার সুযোগ নেই, অথচ অন্য জায়গায় গেলে আরও ভালো করতে পারতেন। সমস্যা হলো তারা জানতেন না কোন ধরনের কোম্পানিতে কী হয়।

### 🔍 কেন এই সমস্যা হয়?

কারণ Tech Industry একটা নয় — এখানে অনেক ধরনের কোম্পানি আছে এবং প্রতিটির নিজস্ব নিয়ম, Culture, Career Progression এবং Compensation Structure আছে। কোনো কোম্পানি জানার আগে Join করলে পরে হতাশ হতে হয়।

### ✅ বইয়ের সমাধান — কোম্পানির ধরন বোঝা

**Big Tech (Google, Meta, Amazon, Microsoft, Apple, Netflix):**

এই কোম্পানিগুলো Engineering-এর সর্বোচ্চ Standard বজায় রাখে। এখানে প্রতিটি Level-এর জন্য লিখিত Expectation আছে। Compensation সবচেয়ে বেশি — Base Salary, Bonus, Stock (RSU) মিলিয়ে একজন Senior Engineer বছরে $250,000–$500,000+ পেতে পারেন।

কিন্তু সমস্যা হলো — এখানে একটি Feature Ship করতে Months লাগতে পারে। Process ভারী। একটা ছোট্ট Change-এর জন্য ৫টি Team-এর Approval লাগতে পারে। আপনি হয়তো Google-এ একটি ছোট্ট Notification Service-এর দায়িত্বে আছেন — বাইরে বলতে ভালো লাগে, কিন্তু পুরো System সম্পর্কে কিছুই জানেন না।

**কী শিখবেন Big Tech-এ:** Scale কীভাবে কাজ করে, Distributed System, Code Quality-এর সর্বোচ্চ Standard, Large Codebase Navigate করা।

**Scaleup (Stripe, Airbnb, DoorDash, Shopify):**

এই কোম্পানিগুলো Product-Market Fit পেয়েছে, দ্রুত বাড়ছে। এখানে আপনি একটি Feature-এর Design থেকে Launch পর্যন্ত সব দেখবেন। Ownership অনেক বেশি। Equity (শেয়ার) পেলে পরে বড় অঙ্কের হতে পারে।

কিন্তু Career Ladder Big Tech-এর মতো স্পষ্ট নয়। Promotion অনেকটা নির্ভর করে Manager ও Visibility-র উপরে। প্রক্রিয়া কম স্বচ্ছ।

**Early-Stage Startup:**

এখানে সব করতে হয়। Backend, Frontend, DevOps, Customer Support। Pressure প্রচণ্ড। কিন্তু শেখার গতি সবচেয়ে বেশি। যদি কোম্পানি সফল হয়, আপনার Equity অনেক মূল্যবান হতে পারে।

ঝুঁকি হলো — ৯০% Startup ব্যর্থ হয়। Funding শেষ হলে চাকরি যাবে।

**Traditional/Enterprise:**

Bank, Insurance, বড় Manufacturing কোম্পানি। Stable চাকরি, কিন্তু Technology পুরানো (Legacy System), কাজের Pace ধীর।

**বড় বিপদ এখানে:** এখানে "Senior Software Engineer" Title পাওয়া যায়, কিন্তু আসলে যা করেন সেটা Big Tech-এর Mid-level Engineer-এর কাজের চেয়ে কম জটিল। পরে Job Change করতে গেলে অন্য কোম্পানিতে Downgrade হওয়ার ঝুঁকি আছে।

---

### ⚠️ Profit Center বনাম Cost Center — এই ভুল সবাই করে

এটা একটা গুরুত্বপূর্ণ বিষয় যা বেশিরভাগ Engineer জানে না এবং এই অজ্ঞতার মূল্য দিতে হয়।

**সমস্যা:** দুজন Engineer একই কোম্পানিতে একই Level-এ কাজ করছেন। একজন বেশি Promotion পাচ্ছেন, বেশি Bonus পাচ্ছেন। কেন?

**কারণ:** একজন Profit Center-এ, অন্যজন Cost Center-এ।

**Profit Center** হলো সেই Team যারা সরাসরি Revenue তৈরি করে। যেমন:
- Payment Team (সরাসরি Transaction Process করে)
- Core Product Team (User-রা এটার জন্যই Pay করে)
- Ads Team (প্রতিটি Click = Revenue)

**Cost Center** হলো সেই Team যারা Internal কাজ করে। যেমন:
- HR System Team
- Internal Tools Team
- Some Infrastructure Teams

Profit Center-এ কাজের Business Impact পরিষ্কার দেখা যায়। "আমি এই Feature তৈরি করেছি, এর ফলে Revenue ১০% বেড়েছে।" এটা বলা সহজ।

Cost Center-এ বলতে হয় "আমি Internal Tool তৈরি করেছি যা Developer-দের Productivity বাড়িয়েছে।" এটা Indirectly Impact — Prove করা কঠিন।

**বইয়ের পরামর্শ:** যদি সুযোগ থাকে, Profit Center-এ যান। এটা ক্যারিয়ারের উপর দীর্ঘমেয়াদী ইতিবাচক প্রভাব ফেলে।

---

<a name="12"></a>
## ১.২ Engineering Ladder — সিঁড়ির প্রতিটি ধাপ

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

অনেক Engineer জানেন না তাদের কাছ থেকে কী Expect করা হচ্ছে। তারা ভাবেন বেশি Coding করলেই Promotion হবে। কিন্তু এটা সত্য নয়। প্রতিটি Level-এ কী দরকার সেটা না জানলে কখনো এগোনো যায় না।

### 🔍 কেন এই সমস্যা হয়?

কারণ Engineering Ladder সম্পর্কে খোলামেলা কথা হয় না। অনেক Manager নিজেও এটা ভালো করে জানেন না। এবং প্রতিটি কোম্পানির Ladder আলাদা।

### ✅ বইয়ের সমাধান — প্রতিটি Level বোঝা

```
Junior Software Engineer (L3)
         ↓
Software Engineer (L4)
         ↓
Senior Software Engineer (L5)  ← Terminal Level — এখানে থামা স্বাভাবিক
         ↓
Staff Engineer (L6)
         ↓
Principal Engineer (L7)
         ↓
Distinguished Engineer / Fellow (L8+)
```

**Junior Engineer (L3) — কী Expect করা হয়?**

Junior Engineer মূলত Defined Task-এ কাজ করেন। তাকে বলা হয় "এই Feature বানাও" বা "এই Bug ঠিক করো।" তিনি Manager বা Senior-এর কাছ থেকে নির্দেশনা নেন।

এই Level-এ Success মানে:
- দেওয়া Task সময়মতো শেষ করা
- Block হলে সাহায্য চাওয়া এবং দ্রুত এগোনো
- Code Quality Standards মেনে চলা
- দ্রুত শেখা

**Mid-Level Engineer (L4) — কী পার্থক্য?**

Mid-level Engineer আর Fully Guided নন। তিনি Medium-complexity Task নিজে নিজে Handle করতে পারেন। Manager বলেন "এই সমস্যাটা সমাধান করো" — কীভাবে করবেন সেটা তাকে নিজেই বের করতে হয়।

**Senior Engineer (L5) — এটা একটা গুণগত পরিবর্তন**

এখানে পার্থক্যটা বড়।

Senior Engineer শুধু নিজের কাজ করেন না। তিনি:
- নিজেই বোঝেন কোন কাজটা Priority
- Ambiguous Requirements-কে Concrete Task-এ রূপান্তরিত করেন
- Team-এর অন্যদের Unblock করেন
- Junior-দের Mentor করেন
- Technical Decision নেন

Gergely একটা গুরুত্বপূর্ণ কথা বলেন: **Senior Engineer হওয়াটাই বেশিরভাগ মানুষের জন্য Terminal Level।** অর্থাৎ এখানে থেকে যাওয়া সম্পূর্ণ স্বাভাবিক এবং সম্মানজনক। Staff বা Principal হওয়া সবার জন্য দরকারও নয়, সম্ভবও নয়।

**Staff Engineer (L6) — Scope বদলে যায়**

Senior আর Staff-এর পার্থক্যটা Technical Depth-এ নয়, Scope-এ।

Senior Engineer একটি Team-এর জন্য অসাধারণ।
Staff Engineer Multiple Team-কে প্রভাবিত করেন।

Staff Engineer-এর Technical সিদ্ধান্ত ও কাজ পুরো Product Area বা Organization-কে প্রভাবিত করে।

**IC Track বনাম Management Track**

Senior হওয়ার পরে দুটো পথ:

IC Track-এ (Individual Contributor) আপনি Technical কাজ করতে থাকেন কিন্তু আরও বড় Scope-এ।

Management Track-এ আপনি মানুষ পরিচালনা করেন — Hiring, Performance Review, Team Culture।

**সবচেয়ে বড় ভুল:** অনেক Engineer Management-এ যান কারণ মনে হয় এটাই "এগিয়ে যাওয়ার" পথ। কিন্তু Gergely স্পষ্ট বলেন — Management ও IC দুটো সমান মর্যাদার পথ। যদি Coding ভালো লাগে এবং লোক পরিচালনায় আগ্রহ না থাকে, Management-এ গেলে দুই দিক থেকেই ক্ষতি হবে।

---

<a name="13"></a>
## ১.৩ নিজের ক্যারিয়ারের দায়িত্ব নিজে নিন

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Engineer ৩ বছর ধরে কঠোর পরিশ্রম করছেন। সময়মতো কাজ দিচ্ছেন, কখনো Deadline Miss করেননি। কিন্তু Promotion হচ্ছে না। তিনি Frustrated। Manager-কে জিজ্ঞেস করলে বলেন "আরও কিছুদিন দেখি।"

এটা একটা খুব সাধারণ পরিস্থিতি।

### 🔍 কেন এই সমস্যা হয়?

কারণ অনেক Engineer বিশ্বাস করেন — ভালো কাজ করলে Manager এবং কোম্পানি নিজে থেকে তার ক্যারিয়ার এগিয়ে দেবে। এটা একটা মৌলিক ভুল ধারণা।

আপনার Manager-এর নিজের দায়িত্ব আছে — টিমের ৬-৮ জন Engineer, Project Deadline, Budget, Hiring। আপনার ক্যারিয়ার তার Priority List-এ আছে, কিন্তু সর্বোচ্চ নয়।

### ✅ বইয়ের সমাধান

**সক্রিয়ভাবে ক্যারিয়ার Drive করুন।**

এর মানে:
- আপনার Goals Manager-কে Explicitly বলুন
- নিয়মিত Feedback নিন — বছরে একবার নয়, প্রতি মাসে
- প্রতি ৩ মাসে নিজের Progress নিজে মূল্যায়ন করুন

### Stretch, Execute, Coast Framework

Gergely একটা Framework দেন যা আপনাকে বুঝতে সাহায্য করবে এই মুহূর্তে আপনি কোথায় আছেন:

**Stretching Phase:**

আপনি এমন কাজ করছেন যা আপনার Current Capability-র বাইরে। নতুন Technology শিখছেন, বড় System Design করছেন, Team-কে Lead করছেন।

এই Phase-এ:
- Stress বেশি, কিন্তু শেখার গতি সর্বোচ্চ
- Failure হওয়ার ঝুঁকি আছে — এটা স্বাভাবিক
- Support দরকার — Manager ও Senior-এর কাছে সাহায্য চান

**Executing Phase:**

আপনি পরিচিত কাজ দক্ষতার সাথে করছেন। Comfortable Zone।

এই Phase-এ:
- কাজের Quality ও Speed সর্বোচ্চ
- Team-এর কাছে Reliable
- কিন্তু Growth ধীর

**Coasting Phase:**

কম চ্যালেঞ্জের কাজ করছেন। Recharge হচ্ছেন।

এই Phase-এ:
- দীর্ঘ Stretching-এর পরে প্রয়োজনীয়
- কিন্তু বেশি সময় এখানে থাকলে Skills Obsolete হয়

**বইয়ের পরামর্শ:** বেশিরভাগ সময় Executing-এ থাকুন। মাঝে মাঝে Stretching করুন। কোথায় আছেন সেটা সচেতনভাবে জানুন।

সবচেয়ে বড় ভুল হলো — বছরের পর বছর শুধু Coasting করা এবং মনে করা সব ঠিক আছে।

---

<a name="14"></a>
## ১.৪ Work Log — কেন রাখবেন ও কীভাবে রাখবেন

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

Performance Review-এর সময় Manager জিজ্ঞেস করলেন: "গত ৬ মাসে আপনি কী করেছেন?"

Engineer উত্তর দিতে পারলেন না। গত ২ মাসের কথা মনে আছে, আগেরটা ধোঁয়াশা। Manager-ও সব মনে রাখেননি। ফলে Performance Review হলো সবচেয়ে Recent ২-৩টি কাজের উপরে — পুরো বছরের নয়।

এটা অনেক Engineer-এর সাথে হয়। এবং এর ফলাফল হলো — তারা সঠিক Rating পান না।

### 🔍 কেন এই সমস্যা হয়?

কারণ মানুষের Memory Recency Bias আছে — সবচেয়ে Recent জিনিস সবচেয়ে বেশি মনে থাকে। ৬ মাস আগে যে দুর্দান্ত কাজটা করেছিলেন, সেটা Review-এর সময় কেউই মনে রাখে না।

### ✅ বইয়ের সমাধান — Work Log

Work Log হলো আপনার কাজের একটা Private ডায়েরি।

**কীভাবে রাখবেন:**

প্রতি সপ্তাহে ৫-১০ মিনিট সময় নিয়ে লিখুন:

```
তারিখ: [তারিখ]

এই সপ্তাহে কী করলাম:
- [কাজের বিবরণ — Specific হন]

Impact কী হলো বা হবে:
- [পরিমাপযোগ্য হলে সংখ্যা দিন]

কী শিখলাম:
- [নতুন Technical বা Soft Skill]

কোনো কঠিন সিদ্ধান্ত নিলাম কি?
- [কী সিদ্ধান্ত, কেন]

কোনো Feedback পেলাম কি?
- [কার কাছ থেকে, কী বললেন]
```

**Work Log কেন এত গুরুত্বপূর্ণ?**

১. **Performance Review-এ:** আপনার কাছে ৬ মাসের সম্পূর্ণ Record আছে। Impressive Self-Review লিখতে পারবেন।

২. **Promotion-এ:** আপনার Contribution Pattern দেখা যাবে — "আমি ধারাবাহিকভাবে Senior-level কাজ করেছি।"

৩. **নিজের Progress বোঝায়:** মাঝে মাঝে মনে হয় "আমি এগোচ্ছি না।" Work Log খুললে দেখবেন আসলে কতটা এগিয়েছেন।

৪. **Job Search-এ:** Resume তৈরি করতে সুবিধা।

Gergely বলেন এই Habit তার ক্যারিয়ারের সবচেয়ে মূল্যবান Habit-গুলোর একটি।

---

<a name="15"></a>
## ১.৫ Feedback — দেওয়া ও নেওয়ার আসল শিল্প

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা ১ — Feedback নেওয়ায় সমস্যা

একজন Junior Engineer প্রতি Performance Review-এ "Meets Expectations" পাচ্ছেন। Manager বলছেন "আরও ভালো করতে পারো।" কিন্তু কীভাবে ভালো করবেন সেটা বলছেন না। Engineer-ও জিজ্ঞেস করছেন না। ২ বছর একই অবস্থা।

### 🔴 সমস্যা ২ — Feedback দেওয়ায় সমস্যা

একজন Senior Engineer তার Peer-এর Code Review-এ লিখলেন: "এই পুরো Module আবার লিখতে হবে।" কোনো কারণ নেই, কোনো Suggestion নেই। Peer Frustrated হলেন, দুইজনের মধ্যে Tension তৈরি হলো।

### 🔍 কেন এই সমস্যা হয়?

Feedback একটা কঠিন Skill। কেউ শেখায় না। বেশিরভাগ মানুষ হয় খুব Vague Feedback দেয়, অথবা খুব Harsh।

Feedback নেওয়ার সময় সমস্যা হলো — Defensive Reaction। আমরা সহজাতভাবে নিজেদের রক্ষা করতে চাই।

### ✅ বইয়ের সমাধান — Feedback-এর Framework

**Feedback নেওয়ার সঠিক পদ্ধতি:**

**Step 1 — নিয়মিত চান, বছরে একবার নয়।**

প্রতি 1-on-1-এ Manager-কে জিজ্ঞেস করুন:
- "আমি কীভাবে আরও ভালো করতে পারি?"
- "আমার কাজে কোনো Pattern দেখছেন যেটা উন্নত করতে পারি?"

এটা অনেকের কাছে সাহসের কাজ মনে হয়। কিন্তু যারা নিয়মিত Feedback চায়, তারা দ্রুত এগোয়।

**Step 2 — প্রথমে শুনুন, Defend করবেন না।**

Feedback পাওয়ার সাথে সাথে "কিন্তু আমি তো..." বলা শুরু করবেন না। আগে পুরোটা শুনুন। প্রশ্ন করুন বোঝার জন্য।

"আপনি বললেন আমার Communication উন্নত করতে হবে — এটা কোন Specific পরিস্থিতিতে দেখেছেন?"

**Step 3 — সত্য কিনা ভাবুন।**

সব Feedback সত্য নয়। কিন্তু সব Feedback-এ কিছু না কিছু সত্য থাকে। বাড়িতে গিয়ে শান্তভাবে ভাবুন।

**Step 4 — Action নিন।**

Feedback নেওয়া এবং Action না নেওয়া মানে সময় নষ্ট। পরের 1-on-1-এ বলুন "আপনি বলেছিলেন Communication উন্নত করতে। আমি এই পদক্ষেপ নিয়েছি।"

---

**Feedback দেওয়ার সঠিক পদ্ধতি — SBI Framework:**

Gergely SBI (Situation, Behavior, Impact) Framework recommend করেন।

**Situation (পরিস্থিতি):** কোন নির্দিষ্ট পরিস্থিতিতে ঘটনাটা হয়েছে।
**Behavior (আচরণ):** তিনি ঠিক কী করলেন — Fact, Interpretation নয়।
**Impact (প্রভাব):** এর ফলে কী হলো বা হতে পারে।

**উদাহরণ:**

ভুল: "তুমি সবসময় Deadline Miss করো।"

সঠিক (SBI): "গত Sprint-এ (Situation) তুমি দুটো Task-এর Deadline-এর আগের দিন বললে যে সময় লাগবে (Behavior)। এর ফলে আমাদের Team-এর Sprint Goal পূরণ হয়নি এবং PM-এর সাথে একটা কঠিন Conversation করতে হয়েছে (Impact)।"

দ্বিতীয়টা অনেক বেশি Actionable। প্রথমটা শুনলে কেউ Defensive হবে, দ্বিতীয়টা শুনলে বোঝা যাবে ঠিক কোথায় সমস্যা।

---

**360° Feedback কী?**

শুধু Manager-এর কাছ থেকে Feedback নয়। Peers, Junior Teammates, এবং যাদের সাথে কাজ করেন তাদের কাছ থেকেও Feedback নিন।

প্রতি ৬ মাসে ২-৩ জনকে জিজ্ঞেস করুন:
- "আমার সাথে কাজ করতে কোনো সমস্যা হয়েছে?"
- "আমি কোন একটা জিনিস বদলালে তোমার কাজ সহজ হবে?"

এটা অনেক সাহসের কাজ — কিন্তু এই Information-ই আপনাকে দ্রুত বাড়াবে।

---

<a name="16"></a>
## ১.৬ Manager-এর সাথে সম্পর্ক

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

অনেক Engineer Manager-কে Ignore করেন বা দূরত্ব রাখেন। মনে করেন Technical কাজই সব, Manager-এর সাথে সম্পর্ক দরকার নেই। ফলে Performance Review-এ অবাক হন — "আমি এত ভালো কাজ করলাম, কিন্তু Rating কম কেন?"

কারণ Manager জানেনই না আপনি কী কী করেছেন।

### 🔍 কেন এই সমস্যা হয়?

Tech Culture-এ একটা প্রবণতা আছে — "কাজ বলে দেবে, নিজেকে Market করার দরকার নেই।" কিন্তু Manager-এর কাছে ১০ জন Engineer। প্রত্যেকের কাজ সমানভাবে Track করা সম্ভব নয়।

### ✅ বইয়ের সমাধান

**1-on-1 Meeting-কে সঠিকভাবে ব্যবহার করুন।**

প্রতি সপ্তাহে ৩০ মিনিটের 1-on-1 হওয়া উচিত। বেশিরভাগ Engineer এটাকে Status Update-এ পরিণত করে — "আমি এই সপ্তাহে এটা করেছি, ওটা করব।" এটা সময়ের অপচয়।

1-on-1 হলো আপনার জন্য Manager-এর Protected সময়। এখানে বলুন:
- আপনি কোথায় Block আছেন এবং সাহায্য দরকার
- ক্যারিয়ারে কোথায় যেতে চান
- Team বা Project নিয়ে কোনো Concern
- Manager-এর কাছ থেকে কোনো Guidance দরকার

Meeting-এর জন্য Agenda আগেভাগে Prepare করুন এবং Manager-কে পাঠান। এটা দুটো জিনিস করে — আপনি Prepared দেখান, এবং Manager জানেন কী নিয়ে কথা হবে।

---

**Manager-এর সাথে Goal Alignment করুন।**

অনেক Engineer কখনো Manager-কে বলেন না তারা কী চান। এটা বড় ভুল।

সরাসরি বলুন: "আমি পরের বছরের মধ্যে Senior Engineer হতে চাই। এর জন্য আমাকে কী করতে হবে বলে আপনি মনে করেন?"

এই একটা প্রশ্ন করলে অনেক কিছু বদলে যায়:
- Manager এখন জানেন আপনার Goal
- Manager সেই অনুযায়ী কাজ ও Opportunity দিতে পারবেন
- আপনার কাছে একটা স্পষ্ট দিকনির্দেশনা আছে

---

**"Managing Up" কী?**

এটা একটা Important Concept।

Managing Up মানে — আপনার Manager-এর কাজ সহজ করা।

কীভাবে?

**আপনার কাজের Update দিন আগে থেকে।** Manager যদি Meeting-এ আপনার কাজ নিয়ে জিজ্ঞেস করেন, তাহলে তার আগেই Update দিয়ে রাখুন। এতে Manager আপনার উপর Depend করতে পারেন।

**সমস্যা আসলে সমাধানসহ নিয়ে যান।** "একটা সমস্যা হয়েছে" বলার চেয়ে "একটা সমস্যা হয়েছে, আমার মনে হচ্ছে এই তিনটা উপায়ে সমাধান করা যাবে, আমি Option 2 নিতে চাই আপনার মতামত কী?" বলুন।

**Manager-এর Priority বুঝুন।** তিনি এই Quarter-এ কী নিয়ে Worried? সেই Direction-এ কাজ করুন।

---

**Skip-Level Manager-এর সাথে সম্পর্ক।**

আপনার Manager-এর Manager — এই মানুষটাকেও চেনাটা গুরুত্বপূর্ণ।

কেন? কারণ Calibration Meeting-এ (Performance Review Decision-এ) Skip-Level Manager প্রায়ই Present থাকেন। তিনি যদি আপনাকে না চেনেন, তাহলে আপনার Promotion Discussion-এ কোনো Context নেই।

বছরে অন্তত ১-২ বার Skip-Level Manager-এর সাথে কথা বলুন। তাদের Priority ও Vision জানুন। আপনার কাজ কীভাবে তাদের Goals-এ Contribute করছে সেটা জানান।

---

<a name="17"></a>
## ১.৭ Performance Review — কীভাবে সফল হবেন

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

দুজন Engineer একই Team-এ প্রায় সমান কাজ করেছেন। কিন্তু Performance Review-এ একজন "Exceeds Expectations" পেলেন, অন্যজন "Meets Expectations"।

কেন এই পার্থক্য?

একজন ভালো Self-Review লিখেছিলেন — Impact সহ, সংখ্যা সহ। অন্যজন শুধু কাজের নাম লিখেছিলেন।

### 🔍 কেন এই সমস্যা হয়?

Performance Review একটা Communication Exercise। আপনি কতটা ভালো কাজ করেছেন সেটা যদি ভালোভাবে Present করতে না পারেন, তাহলে সঠিক মূল্যায়ন হয় না।

### ✅ বইয়ের সমাধান

**ভালো Self-Review লেখার Framework — Impact-First পদ্ধতি:**

**ভুলটা কেমন দেখতে:**

"আমি এই Quarter-এ Payment Service-এর Authentication Module তৈরি করেছি। API Integration করেছি। Team Meeting-এ অংশগ্রহণ করেছি। Code Review করেছি।"

এটা শুনে Manager বুঝতে পারেন না আপনি ভালো ছিলেন নাকি গড়।

**সঠিকটা কেমন দেখতে:**

"**সমস্যা:** Payment Service-এর Checkout Flow-এ Authentication-এর কারণে প্রতি সপ্তাহে ২% Transaction Fail হচ্ছিল, যা মাসে প্রায় $50,000 Revenue Loss।

**আমি কী করলাম:** Root Cause Analysis করে বের করলাম যে JWT Token Expiry Handling-এ একটা Race Condition ছিল। নতুন Authentication Flow Design করলাম যেখানে Token Refresh Automatic।

**ফলাফল:** Transaction Failure Rate ২% থেকে ০.১%-এ নামল। Team-এর জন্য একটা Monitoring Dashboard তৈরি করলাম যাতে এই ধরনের সমস্যা আগেভাগে ধরা পড়ে।

**পরবর্তী:** এই প্যাটার্ন পুরো Backend-এ Apply করা যায় — আমি একটা Proposal লিখছি।"

পার্থক্য দেখুন — সমস্যা, কাজ, ফলাফল, ভবিষ্যৎ পরিকল্পনা — সব আছে।

---

**Goals কীভাবে Set করবেন — SMART পদ্ধতি:**

Review-এর পরে আসে Goal-setting।

অনেক Engineer Goals Set করেন না বা খুব Vague Goals করেন। ফলে কোনো Direction নেই।

SMART Goals মানে:
- **S**pecific — নির্দিষ্ট কী করব
- **M**easurable — কীভাবে বুঝব সফল হয়েছি
- **A**chievable — বাস্তবে সম্ভব কিনা
- **R**elevant — আমার ক্যারিয়ার Goal-এর সাথে মিলছে কিনা
- **T**ime-bound — কখন শেষ করব

**উদাহরণ:**

ভুল Goal: "আমি আরও ভালো Code লিখব।"

SMART Goal: "পরের Quarter-এর শেষে আমার নতুন Code-এ Unit Test Coverage ৮০%-এর উপরে থাকবে এবং আমি Team-এর Testing Standard Document তৈরি করব।"

---

**Calibration Process — এই Invisible Process বোঝুন**

অনেক কোম্পানিতে, বিশেষত Big Tech-এ, Rating শুধু আপনার Manager নির্ধারণ করেন না। একটা **Calibration Meeting** হয় যেখানে কয়েকজন Manager একসাথে বসে সবার Rating ঠিক করেন।

এই Meeting-এর নিয়ম:
- একটা Curve থাকে — সবাই Outstanding পেতে পারে না
- আপনার Manager আপনার হয়ে "Case" করেন
- অন্য Manager-রা Challenge করতে পারেন

**এর Implication কী?**

আপনার Manager যদি আপনার কাজ ভালো না জানেন, Calibration-এ আপনার পক্ষে ভালো করে কথা বলতে পারবেন না।

তাই নিয়মিত Manager-কে আপনার Impact জানান। 1-on-1-এ শুধু Status Update নয়, আপনার Significant Contributions Share করুন।

---

<a name="18"></a>
## ১.৮ Promotion — কেন আটকায় ও কীভাবে পাবেন

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

রাহেলা একজন দুর্দান্ত Engineer। ৩ বছর ধরে কাজ করছেন, সব Deadline মানছেন, Bug Fix করছেন, Team-কে সাহায্য করছেন। কিন্তু Promotion আসছে না। Manager বলছেন "সময় আসলে হবে।"

অথবা আরেকটা পরিস্থিতি — রহিম ১.৫ বছরেই Senior হলেন। রাহেলার চেয়ে কম কাজ করেন। কিন্তু Promotion হয়ে গেল। কেন?

### 🔍 কেন এই সমস্যা হয়?

Promotion শুধু ভালো কাজ করার পুরস্কার নয়। এটা একটা **Organizational Decision** — কোম্পানি বিশ্বাস করছে আপনি পরবর্তী Level Handle করতে পারবেন।

রাহেলা যা করেননি:
- Next Level-এর কাজ শুরু করেননি
- Sponsor তৈরি করেননি
- Visibility তৈরি করেননি

রহিম যা করেছেন:
- Senior-level কাজ নিয়েছেন যদিও Mid-level
- Tech Lead-কে Mentor হিসেবে বানিয়েছেন
- Team Meeting-এ Technical Decision নিয়েছেন

### ✅ বইয়ের সমাধান

**Rule 1: Promotion পাওয়ার আগেই Next Level-এর কাজ করুন**

এটা সবচেয়ে গুরুত্বপূর্ণ Insight।

Senior হতে চাইলে এখনই করুন:
- Junior Engineer-কে Mentor করা
- Technical Architecture Decision নেওয়া
- Project-এর Risk নিজে Identify করা
- Cross-team Collaboration করা

কেন? কারণ Promotion Decision-এ Manager বলেন "এই ব্যক্তি ইতিমধ্যে Senior-এর মতো কাজ করছেন, তাই Promote করা উচিত।" কিন্তু আপনি যদি এখনো Mid-level কাজ করছেন, তাহলে Manager বলতে পারবেন না।

**এটা কি অন্যায় নয়?** অনেকে প্রশ্ন করেন — Promotion ছাড়াই কেন Senior-এর কাজ করব?

Gergely বলেন — হ্যাঁ, এটা কিছুটা Unfair। কিন্তু এটাই Reality। Alternative হলো Promotion না পাওয়া। পছন্দটা আপনার।

---

**Rule 2: Mentor ও Sponsor-এর পার্থক্য বোঝা — Sponsor ছাড়া Promotion কঠিন**

অনেক Engineer Mentor খোঁজেন কিন্তু Sponsor-এর কথা ভাবেন না।

**Mentor** হলেন সেই মানুষ যিনি আপনাকে পরামর্শ দেন। "এটা করো, ওটা শিখো।" এটা মূল্যবান।

**Sponsor** হলেন সেই মানুষ যিনি আপনার **অনুপস্থিতিতে** আপনার হয়ে কথা বলেন। Calibration Meeting-এ "আমি মনে করি রাহেলা Senior-এর জন্য Ready" — এটা Sponsor বলেন।

Sponsor তৈরি করতে হলে:
- ভালো কাজ করুন — এটা ছাড়া Sponsor কাজ করবে না
- Sponsor-এর কাছে আপনার Work Visible রাখুন
- Sponsor-কে তাদের কাজে সাহায্য করুন — সম্পর্কটা একতরফা নয়

---

**Rule 3: Promotion-এর জন্য সরাসরি কথা বলুন**

অনেকে ভাবেন সরাসরি Promotion চাওয়া Unprofessional। এটা ভুল।

Manager-কে বলুন: "আমি এই বছরের মধ্যে Senior Engineer হতে চাই। আপনার মতে আমার কোথায় Gaps আছে? Promotion-এর জন্য কোন Criteria পূরণ করতে হবে?"

এটা বলার পরে আপনার কাছে একটা Clear List থাকবে। সেই List অনুযায়ী কাজ করুন।

প্রতি ৩ মাসে Progress নিয়ে কথা বলুন: "আপনি বলেছিলেন X, Y, Z করতে হবে। X ও Y করেছি। Z-তে কাজ চলছে। আমরা কি Promotion Timeline নিয়ে কথা বলতে পারি?"

---

**Rule 4: Promotion আটকে গেলে কী করবেন**

Manager বলছেন "আরও কিছুদিন দেখি" — কিন্তু কতদিন? কী করলে Promote করবেন?

এই কথাটা Specific করুন:

"আরও কতদিন? কোন নির্দিষ্ট কাজ বা Milestone দেখলে আপনি Promote করতে পারবেন?"

যদি Manager উত্তর দিতে না পারেন বা Timeline বারবার পিছায় — এটা একটা Signal যে হয় Manager ইচ্ছুক নন, অথবা এই কোম্পানিতে আপনার Promotion Structurally কঠিন।

এই পরিস্থিতিতে নতুন চাকরি খোঁজার কথা ভাবুন। অন্য কোম্পানি আপনার কাজ দেখে সঠিক Level-এ নেবে।

---

<a name="19"></a>
## ১.৯ বিভিন্ন Environment-এ টিকে থাকা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Engineer Big Tech থেকে একটা Startup-এ Join করলেন। প্রথম মাসে তিনি বললেন "এখানে কোনো Code Review Process নেই, Testing Coverage নেই, Documentation নেই।" তিনি সবার কাছে Complain করতে লাগলেন। ৩ মাসের মধ্যে তাকে বলা হলো "আপনি Culture Fit না।"

কী ভুল হলো?

### 🔍 কেন এই সমস্যা হয়?

ভিন্ন কোম্পানিতে ভিন্ন নিয়ম চলে। Big Tech-এ যা Best Practice, Startup-এ তা Overhead হতে পারে।

### ✅ বইয়ের সমাধান — Peacetime বনাম Wartime

**Peacetime কোম্পানি:**

কোম্পানি ভালো চলছে। Market Growing, Competition কম, Funding Strong।

এখানে কী ভালো কাজ করে:
- Long-term Planning, Roadmap
- Process তৈরি, Documentation
- Best Practices স্থাপন
- Technical Excellence-এ বিনিয়োগ

**Wartime কোম্পানি:**

কোম্পানি Survival Mode-এ। Market Share হারাচ্ছে, Funding শেষ হচ্ছে, বড় Competitor এসেছে।

এখানে কী কাজ করে:
- দ্রুত সিদ্ধান্ত, দ্রুত Ship
- Minimum Viable Process
- "Perfect"-এর চেয়ে "Done" বেশি গুরুত্বপূর্ণ
- Flexibility, Context Switching

**সমস্যা:** যদি Peacetime Mindset নিয়ে Wartime কোম্পানিতে যান, এবং সবসময় "Process কোথায়?" "Documentation কোথায়?" বলেন — আপনাকে "Context বোঝেন না" বলে মনে হবে।

উল্টোটাও সত্য — Wartime Mindset নিয়ে Peacetime কোম্পানিতে গেলে "কেন এত তাড়া করছেন?" মনে হবে।

**নতুন কোম্পানিতে যোগ দেওয়ার আগে বোঝার চেষ্টা করুন তারা এখন কোন Phase-এ আছে।**

---

**Remote ও Hybrid কাজের আসল চ্যালেঞ্জ**

Remote কাজে Technical Skill যথেষ্ট নয়। লিখিত যোগাযোগে দক্ষ না হলে Remote কাজে সফল হওয়া কঠিন।

**Remote-এর সবচেয়ে বড় সমস্যা — Visibility।**

Office-এ থাকলে আপনার কাজ স্বাভাবিকভাবে দেখা যায়। Remote-এ আপনি কী করছেন কেউ জানে না যদি না আপনি জানান।

**সমাধান:**

- **Daily Update দিন** — Slack-এ বা Email-এ: "আজকে এই কাজ করলাম, এই সমস্যায় পড়লাম, এভাবে সমাধান করলাম।"
- **Async Communication-এ দক্ষ হন** — লম্বা, Clear Message লিখুন যাতে পরের দিন Reply আসলেও কাজ এগোয়।
- **Video Call-এ Camera চালু রাখুন** — এটা ছোট জিনিস কিন্তু Team-এর সাথে Connection রাখে।
- **Meeting Summary লিখুন** — প্রতিটি Meeting-এর পরে Who does What by When একটা Message-এ লিখুন। এতে Accountability তৈরি হয়।

---

<a name="110"></a>
## ১.১০ Job Change — কখন, কেন ও কীভাবে

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

অনেক Engineer হয় খুব তাড়াতাড়ি Job Change করে (রাগের মাথায়, বা সামান্য বেশি Salary-র জন্য), অথবা অনেক দেরিতে (Comfortable হয়ে বছরের পর বছর একই জায়গায়)। দুটোই ক্যারিয়ারের জন্য ক্ষতিকর।

### 🔍 কেন এই সমস্যা হয়?

Job Change একটা কঠিন সিদ্ধান্ত। কখন সঠিক সময় — এটা বোঝার Framework কারো কাছে নেই।

### ✅ বইয়ের সমাধান

**কখন Job Change উচিত:**

**১. শেখার সুযোগ শেষ হয়ে গেলে।**

এটা সবচেয়ে গুরুত্বপূর্ণ Signal। যদি ৬ মাস ধরে নতুন কিছু শিখছেন না, চ্যালেঞ্জ নেই — এটা Warning Sign।

এর মানে এই নয় যে এখনই চলে যান। Manager-কে বলুন আরও চ্যালেঞ্জিং কাজ চান। যদি না দিতে পারেন — তখন বিবেচনা করুন।

**২. Compensation বাজারের তুলনায় অনেক কম।**

প্রতি ১-২ বছরে আপনার Market Rate জানুন — LinkedIn-এ, Glassdoor-এ, অথবা আলাদা কোম্পানিতে Interview দিয়ে।

যদি দেখেন আপনি Market Rate-এর ৩০% কম পাচ্ছেন — এটা সময় নষ্ট।

**৩. Promotion বারবার Delay হলে কোনো Concrete Reason ছাড়া।**

"সময় আসলে হবে" — এই উত্তর দুইবারের বেশি পেলে এটা নিছক Excuse।

**৪. Environment Toxic হলে।**

Blame Culture, Micromanagement, Psychological Unsafe Team — এগুলো আপনার Mental Health ও Career দুটোই নষ্ট করে। এখানে থাকার কোনো কারণ নেই।

---

**একটা কঠিন সত্য — Job Change = বেশি Salary Increase**

এটা অনেকে জানেন না। বেশিরভাগ কোম্পানিতে Internal Annual Raise ৩-৮%। কিন্তু Job Change করলে সাধারণত ২০-৫০% বেশি পাওয়া সম্ভব।

কেন? কারণ Internal Raise-এ Band Restriction থাকে। আপনাকে Grade-এর মধ্যে রাখতে হয়। কিন্তু নতুন কোম্পানি আপনাকে Fresh Market Rate-এ নেয়।

তাই প্রতি ২ বছরে অন্তত একবার বাজার যাচাই করুন। Interview দিন। Offer দেখুন। এমনকি যদি না যানও — আপনার Negotiation Position শক্তিশালী হবে।

---

**Interview Preparation — গভীরে যান**

**Coding Interview:**

শুধু সমস্যা সমাধান করলেই হবে না। Pattern বুঝতে হবে।

সবচেয়ে দরকারি Pattern-গুলো:

**Two Pointers:** Array বা String-এ দুটো Pointer ব্যবহার করে O(n²) কে O(n)-এ আনা।

**Sliding Window:** Subarray বা Substring-এর উপরে একটা Window সরানো।

**BFS/DFS:** Graph ও Tree Traversal-এর জন্য। BFS Level-by-Level, DFS Deep-First।

**Dynamic Programming:** Subproblem-এর Result মনে রেখে বড় সমস্যা সমাধান।

**HashMap Optimization:** O(n²) Lookup-কে O(n)-এ আনা।

**Interviewer-এর সাথে কথা বলুন।** চুপ করে Code লিখবেন না। বলুন:
- "আমি প্রথমে Brute Force দেখছি — Time Complexity হবে O(n²)।"
- "এটাকে HashMap দিয়ে O(n)-এ আনা যায় — এভাবে।"
- "Edge Case হিসেবে Empty Array এবং Single Element Handle করছি।"

Interviewer শুধু Solution দেখেন না, আপনার **Thinking Process** দেখেন।

---

**System Design Interview — Framework:**

**Step 1 — Clarify Requirements (5 মিনিট)**
- কত User? DAU (Daily Active Users)?
- কোন Features সবচেয়ে গুরুত্বপূর্ণ?
- Latency Requirement কত? Consistency কতটা দরকার?

**Step 2 — Capacity Estimation (5 মিনিট)**
- Read/Write Ratio কত?
- Storage কত লাগবে?
- Bandwidth কত?

**Step 3 — High-Level Design (10 মিনিট)**
- Client → Load Balancer → App Server → Database
- Cache কোথায় লাগবে?
- Async Processing কোথায়?

**Step 4 — Deep Dive (15 মিনিট)**
- Database Schema
- API Design
- Bottleneck কোথায়?
- Scale করলে কী হবে?

**Step 5 — Tradeoff নিয়ে কথা বলুন**
- SQL vs NoSQL কেন?
- Consistency vs Availability-তে কোনটা বেছেছেন কেন?

---

**Offer Negotiation — কীভাবে করবেন**

Initial Offer সবসময় Negotiate করুন। ৯০% ক্ষেত্রে Company-র কাছে Buffer থাকে।

কীভাবে:
১. Offer পাওয়ার পরে: "অনেক ধন্যবাদ। আমি এটা নিয়ে ভাবছি। কবের মধ্যে জানাতে হবে?"

২. ৪৮ ঘণ্টা পরে: "আমি এই Role-এ খুবই আগ্রহী। কিন্তু আমার Current Situation-এ [অথবা Other Offer-এ] Compensation একটু বেশি। কি $X সম্ভব?"

৩. যদি Base Salary বাড়ানো না যায়, চেষ্টা করুন:
- Signing Bonus বাড়ানো
- আরও Equity
- Vacation Days
- Remote Work Flexibility

**একাধিক Offer একসাথে থাকলে Leverage সবচেয়ে বেশি।** তাই একসাথে কয়েক জায়গায় Apply করুন।

---

<a name="part-2"></a>
# Part 2 — দক্ষ Developer হওয়া

---

<a name="21"></a>
## ২.১ কাজ সঠিকভাবে শেষ করার শিল্প

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Junior Engineer একটা Task পেয়ে ৩ দিন কাজ করলেন। চতুর্থ দিনে বললেন "এটা আমার পক্ষে সম্ভব নয়।" Manager হতবাক — কেন আগে বলেননি?

আরেকটা পরিস্থিতি — একজন Engineer Task দেওয়া হলো ১ সপ্তাহে শেষ করতে। তিনি ৩ সপ্তাহ কাজ করলেন এবং অনেক Extra Feature যোগ করলেন যা চাওয়া হয়নি। Manager খুশি নন।

### 🔍 কেন এই সমস্যা হয়?

Junior Engineer-দের দুটো সাধারণ সমস্যা:
১. Block হলে সাহায্য চাইতে ভয়
২. Scope Creep — চাওয়ার চেয়ে বেশি করা

### ✅ বইয়ের সমাধান

**Task পাওয়ার পরে প্রথমে যা করবেন — Clarify করুন:**

Task শুরু করার আগে নিশ্চিত করুন:
- **What:** ঠিক কী করতে হবে? Output কেমন হবে?
- **Why:** কেন এটা দরকার? Business Context কী?
- **When:** কখন লাগবে? Soft Deadline না Hard Deadline?
- **Scope:** কী কী এর মধ্যে নেই?

এই প্রশ্নগুলো করলে কাজের মাঝে Confusion কমে।

---

**Block হলে কী করবেন — 30/60 Rule:**

Gergely একটা Rule দেন:

- **৩০ মিনিট:** নিজে চেষ্টা করুন। Error Message পড়ুন, Google করুন, Documentation পড়ুন, Stack Overflow দেখুন।
- **৩০ মিনিট আরও:** এখনো না পারলে, সমস্যাটা লিখুন। ঠিক কোথায় আটকেছেন? কী চেষ্টা করেছেন?
- **তারপর:** সাহায্য চান।

সাহায্য চাওয়ার সময় বলুন:
```
"আমি [X] করতে চাইছিলাম।
এই পর্যন্ত চেষ্টা করেছি: [A, B, C]
Error দেখছি: [Error Message]
আমার Hypothesis হলো [D] কারণে হচ্ছে।
এখানে আটকে গেছি — একটু দেখবে?"
```

শুধু "এটা কাজ করছে না" বললে Senior-রা আপনাকে সাহায্য করতে পারবেন না।

---

**Estimation দেওয়ার কলাকৌশল:**

Estimation Software Development-এর সবচেয়ে কঠিন কাজ।

Gergely-র পরামর্শ:

**Step 1 — Task ভাগ করুন।**
"Payment Integration" একটা Task না। এটা হলো:
- API Documentation পড়া (2h)
- Sandbox Environment Setup (1h)
- Payment Request তৈরি (3h)
- Error Handling (2h)
- Testing (3h)
- Code Review ও Fix (2h)

**Step 2 — প্রতিটা Subtask-এ Buffer যোগ করুন।**
আপনার যা মনে হয় তার ১.৫-২ গুণ ধরুন। Unexpected সমস্যা সবসময় আসে।

**Step 3 — Dependencies চিহ্নিত করুন।**
কি অন্য কারো কাজ শেষ হলে তবে আপনার শুরু হবে?

**Step 4 — সৎ থাকুন।**
যদি মনে হয় Deadline সম্ভব নয় — আগেভাগে বলুন। কখন? যখন বুঝবেন তখনই।

"এটা শুনে Manager খুশি হবেন না" — এই ভয়ে চুপ থাকবেন না। Deadline-এর দিন সকালে বললে আরও সমস্যা।

---

**Reputation গড়ার আসল পদ্ধতি:**

Engineer-দের Reputation Technical Skill-এর উপরে নয়, **Reliability**-র উপরে তৈরি হয়।

যে Engineer বলে "কাল দেব" এবং কাল দেয় — তাকে সবাই বিশ্বাস করে।
যে বলে "কাল দেব" এবং তিনদিন পরে দেয় — তাকে কেউ বিশ্বাস করে না, সে যতই Talented হোক।

Reliable হওয়ার নিয়ম:
- Over-promise করবেন না। Under-promise, Over-deliver।
- যা বলেছেন তা করুন।
- করতে না পারলে আগেভাগে জানান।

এই তিনটা Habit দিয়ে Team-এ অনেক মূল্যবান হওয়া যায়।

---

<a name="22"></a>
## ২.২ Coding-এর গভীর দক্ষতা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা ১ — Readable Code না লেখা

একজন Engineer দ্রুত কাজ করেন। Code কাজ করে। কিন্তু ৩ মাস পরে তিনি নিজেই বুঝতে পারেন না নিজের Code। নতুন Engineer যোগ দিলে Codebase বুঝতে মাস লেগে যায়।

### 🔴 সমস্যা ২ — Code Review-এর সংস্কৃতি নেই

Code Review একটা Bureaucratic Process হয়ে গেছে। Reviewer দ্রুত "LGTM" (Looks Good to Me) দেন, সমস্যা ধরেন না। Bug Production-এ যায়।

### ✅ বইয়ের সমাধান

**Readable Code-এর তিনটা মূলনীতি:**

**১. Code যেন নিজেই বলে কী হচ্ছে।**

Variable ও Function নামে সময় দিন। ৩ মিনিট ভালো নাম দিতে পরে অনেক সময় বাঁচায়।

```python
# এই Code কী করছে বোঝা কঠিন:
def calc(d, t, r):
    return d + t * r / 100

# এটা পড়লেই বোঝা যায়:
def calculate_total_price_with_tax(base_price, item_count, tax_rate_percent):
    return base_price + item_count * tax_rate_percent / 100
```

**২. Comment শুধু "কেন" বোঝানোর জন্য।**

Code-ই বলবে "কী হচ্ছে।" Comment বলবে "কেন এটা করছি।"

```python
# এই Comment অর্থহীন — Code-ই বলছে:
counter = counter + 1  # counter-এ 1 যোগ করো

# এই Comment মূল্যবান — কারণ বলছে:
retry_count = retry_count + 1
# API সর্বোচ্চ ৩ বার Retry করে তারপর Fallback Cache থেকে নেয়।
# Payment Provider-এর Transient Error-এর জন্য এই নিয়ম।
```

**৩. Function ছোট রাখুন — Single Responsibility।**

একটা Function একটাই কাজ করুক। যদি Function-এর নাম দিতে "and" লিখতে হয়, ভাগ করুন।

`validate_and_save_user()` → ভুল।
`validate_user()` + `save_user()` → সঠিক।

---

**Code Review-এর সংস্কৃতি গড়া:**

**Reviewer হিসেবে — সত্যিকারের Review করুন:**

LGTM Culture হলো যখন সবাই দ্রুত Approve করে Conflict এড়াতে। এটা Team-কে দুর্বল করে।

ভালো Review করতে দেখুন:
- **Correctness:** Code কি ঠিকমতো কাজ করবে? Edge Case Handle হয়েছে?
- **Readability:** ৬ মাস পরে অন্য কেউ বুঝতে পারবে?
- **Performance:** কোনো Obvious Performance Issue আছে?
- **Security:** Injection, Authentication, Authorization-এ কোনো Issue?
- **Tests:** যথেষ্ট Test আছে?

**Tone সম্পর্কে সচেতন থাকুন:**

Text-এ Tone বোঝা কঠিন। Harsh মনে হতে পারে।

```
❌ "এটা ভুল উপায়।"
✅ "এই পদ্ধতিতে একটা সমস্যা দেখছি — Large Dataset-এ O(n²) হয়ে যাবে। HashMap ব্যবহার করলে O(n)-এ আনা যায়। কী মনে হয়?"
```

দ্বিতীয়টায় সমস্যা বলেছেন, সমাধান দিয়েছেন, এবং মতামত চেয়েছেন। এটা Collaborative।

**নিজের Code Review-এ:**

Defensive হবেন না। Code-এর সমালোচনা আপনার সমালোচনা নয়।

বুঝতে না পারলে জিজ্ঞেস করুন: "এই Comment-টা আরেকটু Explain করবে?" — এটা দুর্বলতা নয়।

---

**DRY Principle — Don't Repeat Yourself:**

একই Code বা Logic যদি দুটো জায়গায় থাকে, একদিন একটা ঠিক করবেন অন্যটা ভুলে যাবেন।

**কিন্তু সতর্কতা:** অনেকে DRY-কে ভুলভাবে Apply করেন। দুটো Code দেখতে Similar হলেই একটা Function বানানো ঠিক নয়।

Rule of Three: একই Logic তিনবার দেখলে তখন Extract করুন।

---

<a name="23"></a>
## ২.৩ Debugging — সমস্যা খোঁজার পদ্ধতি

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Engineer একটা Bug-এ ৩ ঘণ্টা কাজ করলেন। Random পরিবর্তন করলেন, কিছু হলো না। তারপর Senior-কে ডাকলেন, Senior ১০ মিনিটে ঠিক করলেন।

পার্থক্য কী? Senior Systematically কাজ করেছেন। Junior Random।

### ✅ বইয়ের সমাধান — Systematic Debugging

**Step 1 — Reproduce করুন। এটা সবচেয়ে জরুরি।**

"শুনেছি হয়" বা "আমার Machine-এ হচ্ছে না" — এই অবস্থায় Debugging শুরু করবেন না।

Bug Consistently Reproduce করতে পারা মানে আপনার হাতে একটা Lab আছে।

Reproduce করার সময় লিখুন:
- কোন Steps-এ হয়?
- কোন Input-এ হয়?
- কোন Environment-এ হয়? (OS, Browser, Version)
- কখন হয়? Always নাকি Intermittent?

**Step 2 — Binary Search দিয়ে Isolate করুন।**

"এই 500 লাইনের Code-এর কোথায় Bug" জানার পদ্ধতি:

মাঝখানে Log/Breakpoint দিন। ওখান পর্যন্ত ঠিক আছে কিনা দেখুন। থাকলে দ্বিতীয় অর্ধে Bug। না থাকলে প্রথম অর্ধে।

এভাবে ২-৩ চেষ্টায় Bug-এর Location ১/৮ এ নামিয়ে আনা যায়।

**Step 3 — Hypothesis করুন এবং একটা একটা Test করুন।**

কয়েকটা সম্ভাব্য কারণ লিখুন। তারপর একটা একটা করে Test করুন।

**সতর্কতা:** একসাথে দুটো পরিবর্তন করবেন না। তাহলে কোনটায় Bug ঠিক হলো বুঝবেন না।

**Step 4 — Fix-এর পরে Root Cause বুঝুন।**

Bug ঠিক হলেই শেষ নয়। জিজ্ঞেস করুন:
- কেন এই Bug হলো?
- এই Bug আর কোথায় থাকতে পারে?
- এই Bug আবার হওয়া ঠেকাতে Test লিখুন।

---

**Rubber Duck Debugging:**

এটা হাসির মনে হলেও সত্যিই কাজ করে।

আপনার Code-এর সমস্যা একটা Rubber Duck-কে (বা যেকোনো Object-কে) Line by Line বোঝানোর চেষ্টা করুন। কথায় বলার সময় মস্তিষ্ক নতুনভাবে Process করে এবং প্রায়ই নিজেই উত্তর খুঁজে পায়।

---

<a name="24"></a>
## ২.৪ Software Development Practices

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা — Git ভালো না জানা

একজন Engineer ভুল Branch-এ Commit করলেন। তারপর সব Mix হয়ে গেল। তিনি সব Delete করে নতুন করে শুরু করলেন — এবং সব কাজ হারালেন।

### ✅ বইয়ের সমাধান — Git-এর সঠিক ব্যবহার

**Commit Message লেখার নিয়ম — Conventional Commits:**

```
feat: add user authentication with JWT tokens
fix: resolve race condition in payment processing
refactor: simplify order calculation logic
docs: update API documentation for v2 endpoints
test: add missing unit tests for user service
chore: update dependencies to latest versions
```

**কেন এটা গুরুত্বপূর্ণ?**

৬ মাস পরে কেউ যখন `git log` দেখবে, বুঝবে কী পরিবর্তন হয়েছে। "Update code" বা "Fix stuff" লেখা Commit-এ কিছুই বোঝা যায় না।

**Branch Strategy:**

```
main (সবসময় Production-ready)
    ↑
feature/payment-jwt-auth
feature/user-profile-update
bugfix/checkout-null-pointer
```

- `main` বা `master`-এ সরাসরি Push করবেন না
- প্রতিটি Feature-এর জন্য আলাদা Branch
- Branch নাম Descriptive রাখুন

**ছোট, Focused Commit:**

একটা Commit-এ অনেক কিছু মিক্স করবেন না। "Fix payment + Add tests + Update docs" — তিনটা আলাদা Commit।

কারণ: কোনো একটা পরিবর্তন Revert করতে হলে অন্যগুলোও Revert হবে।

---

**Design Patterns — কখন ব্যবহার করবেন:**

Design Pattern হলো সাধারণ সমস্যার Proven সমাধান। কিন্তু Pattern শেখার পরে অনেকে সব জায়গায় Apply করতে চায় — এটা ভুল।

Pattern ব্যবহার করুন যখন সত্যিই দরকার।

**Observer Pattern — কোথায় দরকার?**

সমস্যা: Payment হলে Email Send করতে হবে, SMS পাঠাতে হবে, Inventory Update করতে হবে।

Observer ছাড়া: Payment Code-এ সব করতে হবে — অনেক Coupling।

Observer দিয়ে: Payment একটা Event Fire করবে। Email Service, SMS Service, Inventory Service — সবাই এই Event শুনবে এবং নিজের কাজ করবে। Payment Code-এর কিছু জানার দরকার নেই।

**Factory Pattern — কোথায় দরকার?**

সমস্যা: `if type == "pdf" create PDF, if type == "excel" create Excel` — এই if-else বাড়তেই থাকে।

Factory দিয়ে: `DocumentFactory.create(type)` — নতুন Type যোগ করলে শুধু Factory বদলাতে হবে।

---

<a name="25"></a>
## ২.৫ Testing — সঠিকভাবে ও গভীরভাবে

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা টিম দ্রুত কাজ করছে, Test লেখার সময় নেই। প্রতিটা Deployment-এ ভয়। কখনো Payment ভাঙে, কখনো Login ভাঙে। Rollback করতে হয়। বারবার।

আরেকটা সমস্যা — Test আছে, কিন্তু Test Meaningless। ১০০টা Test কিন্তু কোনো Bug Catch করে না। Coverage বেশি কিন্তু Confidence কম।

### 🔍 কেন এই সমস্যা হয়?

Test লেখা কঠিন মনে হয়, সময় লাগে, Immediate Value দেখা যায় না। তাই Skip করা হয়।

কিন্তু Test না লেখার Cost লুকানো থাকে — Production Bug বাড়ে, Refactoring ভয় লাগে, Debugging সময় বাড়ে।

### ✅ বইয়ের সমাধান

**Test Pyramid বোঝা:**

```
                △
               /E2E\        ← সবচেয়ে কম, সবচেয়ে ধীর, সবচেয়ে Realistic
              /──────\
             /Integra-\     ← মাঝারি, Service Layer পর্যন্ত
            /tion Tests\
           /────────────\
          /  Unit Tests  \  ← সবচেয়ে বেশি, সবচেয়ে দ্রুত, Isolated
         /────────────────\
```

**কেন এই Pyramid?**

Unit Test দ্রুত, সস্তা, Isolated। ১০০০টা Unit Test ৫ সেকেন্ডে চলে। তাই বেশি লিখুন।

E2E Test সবচেয়ে Realistic কিন্তু ধীর, Flaky (কখনো Pass কখনো Fail), এবং ঠিক করতে সময় লাগে। তাই কম।

---

**ভালো Unit Test কেমন হয় — AAA Pattern:**

```python
def test_calculate_order_total_applies_discount_for_premium_users():
    # Arrange — সব Setup করুন
    user = User(tier="premium")
    items = [Item(price=100), Item(price=200)]
    
    # Act — যা Test করছেন সেটা করুন
    total = calculate_order_total(user, items)
    
    # Assert — ফলাফল সঠিক কিনা দেখুন
    assert total == 270  # 300 - 10% premium discount
```

**ভালো Test-এর বৈশিষ্ট্য:**

- **Test Name-ই Documentation:** `test_calculate_order_total_applies_discount_for_premium_users` — নাম পড়লেই বোঝা যায় কী Test।
- **একটা Test একটাই জিনিস:** একটা Test-এ অনেক Assert দেবেন না।
- **Independent:** একটা Test অন্য Test-এর উপর নির্ভরশীল নয়।
- **Fast:** Unit Test মিলিসেকেন্ডে চলবে।

---

**TDD (Test-Driven Development) — কখন ব্যবহার করবেন:**

TDD মানে — আগে Test লিখুন, তারপর Code।

**Red → Green → Refactor Cycle:**

১. **Red:** একটা Failing Test লিখুন।
২. **Green:** Test Pass করার ন্যূনতম Code লিখুন।
৩. **Refactor:** Code Cleanup করুন।

**কোথায় TDD সবচেয়ে কার্যকর:**
- Complex Business Logic
- Algorithm Implementation
- Bug Fix (আগে Bug Reproduce করা Test, তারপর Fix)

**কোথায় TDD কম কার্যকর:**
- UI Development
- Exploratory Development (যখন জানেন না কী বানাবেন)

---

**Test Coverage — কত % দরকার?**

বইয়ের পরামর্শ: ৮০% Coverage একটা ভালো লক্ষ্য। ১০০% Coverage অর্থহীন।

**কিন্তু সতর্কতা:** High Coverage = No Bugs নয়।

```python
def divide(a, b):
    return a / b

def test_divide():
    assert divide(10, 2) == 5  # ✅ Test Pass, Coverage 100%
```

এই Test Coverage ১০০% কিন্তু `divide(10, 0)` — ZeroDivisionError কেউ Test করেনি।

**সঠিক পদ্ধতি:** Critical Path ও Edge Case-এ ভালো Test লিখুন। Coverage একটা Metric, লক্ষ্য নয়।

---

<a name="26"></a>
## ২.৬ উৎপাদনশীলতার Tools ও Habits

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

দুজন Engineer। একজন সারাদিন কাজ করেন কিন্তু কম Produce করেন। অন্যজন ৬ ঘণ্টা কাজ করে বেশি Produce করেন।

পার্থক্য কী? Tools ও Habits।

### ✅ বইয়ের সমাধান

**IDE-র সঠিক ব্যবহার — Keyboard Shortcuts:**

Mouse ব্যবহার না করে সব Keyboard-এ করুন। এটা শুনতে ছোট মনে হয় কিন্তু দিনে ঘণ্টাখানেক বাঁচায়।

কিছু গুরুত্বপূর্ণ Shortcut (VS Code):

| কাজ | Shortcut |
|-----|----------|
| Quick File Open | Ctrl+P |
| Command Palette | Ctrl+Shift+P |
| Find in All Files | Ctrl+Shift+F |
| Go to Definition | F12 |
| Rename Symbol | F2 |
| Multi-cursor | Ctrl+D |
| Move Line Up/Down | Alt+↑/↓ |

**একটা পরামর্শ:** প্রতি সপ্তাহে একটা নতুন Shortcut শিখুন। ৩ মাসে ১২টা — এতেই Productivity উল্লেখযোগ্য বাড়বে।

---

**Fast Iteration — Local Development ত্বরান্বিত করা:**

**Hot Reload:** Code পরিবর্তন করলে Manual Restart ছাড়াই Change দেখা।

**Docker Compose:** Local-এ পুরো System চালানো।

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports: ["3000:3000"]
    volumes: [".:/app"]  # Hot Reload-এর জন্য
  db:
    image: postgres:14
  redis:
    image: redis:7
```

এক Command-এ পুরো System চালু: `docker-compose up`

**Makefile — Common Command সংক্ষিপ্ত করা:**

```makefile
run:
    docker-compose up --build

test:
    pytest tests/ -v --coverage

lint:
    flake8 src/ && black src/ --check

migrate:
    python manage.py migrate

shell:
    docker-compose exec app python manage.py shell
```

এখন `make test` দিলেই Tests চলে। `make run` দিলেই System উঠে।

---

**AI Coding Tools — সঠিকভাবে ব্যবহার:**

GitHub Copilot, Cursor-এর মতো Tools ব্যবহার করুন। কিন্তু সতর্কভাবে।

**সঠিক ব্যবহার:**
- Boilerplate Code Generate করতে
- Test Case Generate করতে
- Documentation লিখতে
- নতুন Technology Exploration-এ

**ভুল ব্যবহার:**
- AI-এর Code বুঝে না শুনেই Accept করা
- Security-critical Code-এ AI-এর উপরে নির্ভর করা
- AI-এর পরামর্শ Critically না দেখা

AI হলো একটা Junior Intern — দ্রুত কাজ করে কিন্তু ভুলও করে। সব কিছু Check করতে হয়।

---

<a name="part-3"></a>
# Part 3 — Senior Engineer হওয়া

---

<a name="31"></a>
## ৩.১ Senior Engineer-এর আসল পার্থক্য ও দায়িত্ব

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Engineer Senior হওয়ার পরেও একইভাবে কাজ করতে থাকেন — Task পান, করেন, দেন। Manager Frustrated। "Senior হলে কী হলো? কোনো পরিবর্তন নেই।"

অন্যদিকে আরেকজন Engineer Senior হওয়ার আগেই Senior-এর মতো কাজ করছেন। Team তাকে Go-To Person মনে করে।

### 🔍 কেন এই সমস্যা হয়?

কেউ বলে দেয় না Senior Engineer-এর ঠিক কী Expectation। অনেক Engineer মনে করেন Level Change মানে শুধু বেশি বেতন, কাজ একই।

### ✅ বইয়ের সমাধান — Senior-এর আসল পরিবর্তন

**Junior/Mid থেকে Senior-এর পার্থক্য:**

| বিষয় | Junior/Mid | Senior |
|-------|------------|--------|
| কাজের Scope | Defined Task | Ambiguous Problem |
| Dependency | Manager/Senior-এর উপরে | Independent |
| Impact | নিজের কাজ | Team-এর Output |
| Failure | নিজের ব্যর্থতা | Team-এর সাফল্য |
| Priority | Manager ঠিক করে | নিজেই বোঝে |

**Ambiguity Handle করা — Senior-এর সবচেয়ে বড় Skill:**

PM বললেন "Checkout Experience উন্নত করতে হবে।" এটা অস্পষ্ট।

Mid-level Engineer বলবে: "এটা Vague। কী করব?"

Senior Engineer বলবে: "আমাকে ২ দিন দিন — User Session Recording দেখব, Error Log বিশ্লেষণ করব, Customer Support Ticket দেখব। তারপর বলব সবচেয়ে বড় Problem কোনটা।"

Senior Engineer Ambiguity-কে দেখে সুযোগ হিসেবে — এখানে আমি Value দিতে পারি।

---

**Ownership — পুরো Feature-এর দায়িত্ব নেওয়া:**

Ownership মানে শুধু নিজের Code-এর দায়িত্ব নয়।

একটা উদাহরণ:

Team একটা Feature Ship করছে। QA Testing-এ একটা Critical Bug পেল — কিন্তু এটা আপনার Code-এ নয়, অন্য একজনের Code-এ। আপনার কাজ কি?

**Non-owner Mindset:** "ওটা তো আমার Code না। ওকে বলো।"

**Ownership Mindset:** "এই Bug Feature-কে Block করছে। আমি এখনই দেখছি। যদি নিজে না ঠিক করতে পারি, তাহলে সঠিক মানুষকে পাই এবং নিশ্চিত করি এটা দ্রুত ঠিক হয়।"

পার্থক্যটা বড়। Ownership Mindset Team-কে দ্রুত Ship করতে সাহায্য করে।

---

**Visibility — ভালো কাজের কথা জানানো:**

এটা অনেক Engineer-এর কাছে Uncomfortable। মনে হয় Self-promotion করছি।

কিন্তু Gergely বলেন — এটা Self-promotion নয়, এটা Communication।

আপনি দিনে ১২ ঘণ্টা কাজ করছেন কিন্তু Manager জানেন না — এতে কারো লাভ নেই।

**কীভাবে Visibility তৈরি করবেন:**
- Weekly Update — "এই সপ্তাহে X, Y করলাম। Impact হলো Z।"
- Meeting-এ নিজের কাজ সংক্ষেপে Share করুন
- Significant Achievement হলে Team Channel-এ Post করুন
- Stakeholder-দের জানান যখন কিছু গুরুত্বপূর্ণ শেষ হয়

---

<a name="32"></a>
## ৩.২ Code Review — সংস্কৃতি ও দক্ষতা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা ১ — Rubber-stamp Review

Senior Engineer দ্রুত সব Approve করেন। "সব ঠিক আছে মনে হচ্ছে।" Bug Production-এ যায়।

### 🔴 সমস্যা ২ — Unnecessarily Harsh Review

Senior Engineer প্রতিটা ছোট জিনিসে Comment করেন। Junior Engineers ভয়ে Code Submit করতে চায় না।

### ✅ বইয়ের সমাধান

**Code Review-এর আসল লক্ষ্য:**

Code Review-এর লক্ষ্য শুধু Bug খোঁজা নয়। এটা:
- Knowledge Transfer (Reviewer শেখে, Writer শেখে)
- Code Quality নিশ্চিত করা
- Collective Ownership তৈরি করা
- Mentoring

**Comment-এর Priority দিন:**

সব Comment সমান নয়। Priority বলুন:

- **[Blocking]:** এটা Fix করতেই হবে।
- **[Suggestion]:** করলে ভালো হবে।
- **[Nit]:** Minor, Optional।
- **[Question]:** আমি বুঝিনি, একটু Explain করবে?

```
[Blocking] এই Database Query-তে Index নেই। Production-এ
Large Dataset-এ Full Table Scan হবে — Latency বাড়বে।

[Suggestion] এই Helper Function আলাদা Utility File-এ নিলে
অন্য জায়গায়ও ব্যবহার করা যাবে।

[Nit] Variable-এর নাম `d` → `discount_rate` হলে আরও পরিষ্কার।

[Question] এই Retry Logic কেন ৩ বার? কোনো Specific কারণ আছে?
```

---

**Asynchronous Review-এর Etiquette:**

**Response Time:** Code Review-এর জন্য ২৪ ঘণ্টার মধ্যে Response দিন। কারো কাজ Block হয়ে আছে।

**Batch করুন:** একটা PR-এ ৫ বার Comment করার চেয়ে একবারে সব Comment দিন।

**Approve করার পরে:** যদি Minor পরিবর্তন চেয়েছেন এবং Author ঠিক করেছেন — আবার দেখার দরকার নেই। Trust করুন।

---

<a name="33"></a>
## ৩.৩ Mentoring — কার্যকর শেখানো

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Senior Engineer সব কাজ নিজেই করে দেন Junior-দের। দ্রুত কাজ হয়। কিন্তু Junior-রা কিছু শেখে না, নির্ভরশীল থেকে যায়। Senior-এর সময় নষ্ট হতে থাকে।

আরেকটা পরিস্থিতি — Senior Engineer Junior-এর প্রশ্নে উত্তর না দিয়ে "নিজে চেষ্টা করো" বলে চলে যান। Junior কোথা থেকে শুরু করবে বোঝে না।

### ✅ বইয়ের সমাধান

**Mentoring-এর সঠিক Balance:**

Gergely একটা Scale দেন:

```
খুব বেশি সাহায্য ←————————→ খুব কম সাহায্য
"এইভাবে করো"           "নিজে বের করো"
```

সঠিক জায়গা মাঝখানে। প্রশ্ন করুন যা তাদের নিজেই ভাবতে বাধ্য করে।

**Socratic Mentoring:**

"এই সমস্যাটা সমাধান করব কীভাবে?" — এই প্রশ্নে সরাসরি উত্তর দেওয়ার আগে:

- "তুমি এই সমস্যাটা কীভাবে দেখছ?"
- "কোন কোন Approach মাথায় আসছে?"
- "প্রতিটার Trade-off কী মনে হচ্ছে?"

এই প্রশ্নগুলো দিয়ে তাদের নিজেই উত্তরের কাছাকাছি নিয়ে যান।

**Pair Programming দিয়ে Mentor করুন:**

একটা Pairing Session-এ Junior Code লিখবে, আপনি Side-এ থেকে মাঝে মাঝে Guide করবেন। এটা সবচেয়ে কার্যকর Teaching Method।

Junior একটা Real Problem Solve করছে, Real-time Feedback পাচ্ছে।

---

<a name="34"></a>
## ৩.৪ Technical Debt — চেনা, বোঝা ও সামলানো

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা কোম্পানিতে কোনো নতুন Feature যোগ করতে ৩ সপ্তাহ লাগে — যেটা ১ সপ্তাহে হওয়া উচিত। কারণ Codebase এত জটিল যে একটা পরিবর্তন করলে ৫টা জায়গায় ঠিক করতে হয়। এটাই Technical Debt-এর পরিণতি।

### 🔍 কেন Technical Debt তৈরি হয়?

Technical Debt দুই ধরনের:

**Intentional Debt (ইচ্ছাকৃত):** "এখন দ্রুত Ship করতে হবে, পরে ঠিক করব।" এটা একটা Business Decision। ভুল নয়।

**Unintentional Debt (অনিচ্ছাকৃত):** Engineer ভালো জানতেন না, তাই খারাপ Design করেছেন।

সমস্যা হলো — উভয় ধরনের Debt "পরে ঠিক করব" বলে জমতে থাকে। কখনো ঠিক হয় না।

### ✅ বইয়ের সমাধান

**Technical Debt চেনার চিহ্ন:**

- নতুন Feature যোগ করতে অনেক জায়গায় হাত দিতে হয়
- একটা পরিবর্তন করলে অন্য জায়গায় ভাঙে
- নতুন Engineer-রা Codebase বুঝতে মাস লাগে
- Bug Fix করতে গিয়ে নতুন Bug তৈরি হয়
- Test লিখতে গেলে Code Untestable মনে হয়

---

**Non-technical মানুষকে কীভাবে বোঝাবেন:**

এটা Senior Engineer-এর গুরুত্বপূর্ণ Skill।

"Technical Debt Refactor করতে হবে" বললে কেউ বোঝে না।

**Analogy দিন:** "আমাদের Codebase এখন ১৯৭০-এর পুরানো রাস্তার মতো। সেই সময়ের জন্য ঠিক ছিল, কিন্তু এখন তিনগুণ Traffic চলছে। প্রতিদিন Pothole বাড়ছে। এখন Major Road Work না করলে, ৬ মাস পরে Road বন্ধ করতে হবে।"

**Business Impact দিয়ে বলুন:** "এই Technical Debt-এর কারণে প্রতিটি নতুন Feature তৈরিতে ৪০% বেশি সময় লাগছে। গত Quarter-এ ৩টা Feature Late Ship হয়েছে এই কারণে। এটা Address না করলে পরের বছরে আরও খারাপ হবে।"

---

**Boy Scout Rule:**

Code যখন Open করবেন, একটু ভালো করে রেখে আসুন।

মানে — আপনি যে File-এ কাজ করতে এসেছেন, পাশেই যদি একটা পরিষ্কার করার মতো জিনিস দেখেন — করে রেখে যান। আলাদা Ticket না খুলে, আলাদা PR না করে।

এটা বড় Refactoring ছাড়াই ধীরে ধীরে Codebase Clean করার উপায়।

---

<a name="35"></a>
## ৩.৫ Software Architecture — প্রথম পদক্ষেপ

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা Team বড় Feature শুরু করল। ৩ সপ্তাহ পরে আবিষ্কার করল — তারা ভুল Approach নিয়েছে। সব আবার করতে হবে।

কারণ শুরুতে কেউ বসে Design নিয়ে ভাবেনি।

### ✅ বইয়ের সমাধান — Design Document

বড় কাজ শুরু করার আগে একটা Design Document লিখুন।

**ভালো Design Document Template:**

```markdown
# Feature Name: [নাম]

## Context (প্রেক্ষাপট)
কী সমস্যা সমাধান করছি? কেন এটা এখন গুরুত্বপূর্ণ?

## Goals (লক্ষ্য)
এই Design কী অর্জন করবে?

## Non-Goals (যা করব না)
এই Design কী করবে না? (Scope বন্ধ রাখে)

## Proposal (প্রস্তাব)
আমি কী করতে চাই — Diagram সহ।

## Alternatives Considered (যা বিবেচনা করেছিলাম)
অন্য কোন Approach বিবেচনা করেছিলাম? কেন এটা নিইনি?

## Tradeoffs (আপোষ)
এই Approach-এর সুবিধা ও অসুবিধা কী?

## Open Questions (অস্পষ্ট বিষয়)
এখনো কোন প্রশ্নের উত্তর জানি না?
```

**Design Document কেন দরকার:**

- লেখার সময় চিন্তা পরিষ্কার হয়
- Team এর সবাই একই Page-এ আসে
- পরে "কেন এটা এভাবে করেছিলে?" প্রশ্নের উত্তর আছে
- Onboarding-এ নতুন Engineer-রা Context পায়

---

**RFC (Request for Comments) প্রক্রিয়া:**

RFC হলো Design Document সবার কাছে Review-এর জন্য পাঠানো।

অনেকে এতে ভয় পান — "সবাই দেখবে, সমালোচনা করবে।" কিন্তু এটাই এর Point।

কোড লেখার আগে সমস্যা ধরা পড়লে ঠিক করা সস্তা। ৩ সপ্তাহ কাজ করার পরে ঠিক করা অনেক বেশি Expensive।

---

<a name="part-4"></a>
# Part 4 — Tech Lead হওয়া

---

<a name="41"></a>
## ৪.১ Tech Lead-এর আসল ভূমিকা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন দুর্দান্ত Senior Engineer Tech Lead হলেন। কিন্তু Lead হওয়ার পরেও একইভাবে কাজ করতে থাকলেন — সব গুরুত্বপূর্ণ কাজ নিজে করেন। Team কাজ পায় না, Learn করতে পারে না। প্রোজেক্ট Delay হয়।

### 🔍 কেন এই সমস্যা হয়?

Tech Lead হওয়া একটা Role Transition। অনেকে ভাবেন সবচেয়ে ভালো Coder = সবচেয়ে ভালো Tech Lead। এটা ভুল।

### ✅ বইয়ের সমাধান

**Tech Lead মানে কী?**

Tech Lead হলেন সেই মানুষ যিনি:
- Technical Direction দেন, সব কাজ করেন না
- Team-কে Block হওয়া থেকে বাঁচান
- Stakeholder-এর সাথে Bridge হিসেবে কাজ করেন
- Technical Risk Identify করেন এবং Manage করেন

**Tech Lead-এর সময় বন্টন:**

Gergely বলেন একজন ভালো Tech Lead-এর সময় এভাবে যায়:

- **Coding:** ৩০-৪০% — কম, কিন্তু Critical Path-এ
- **Architecture ও Design:** ২০-২৫%
- **Stakeholder Communication:** ১৫-২০%
- **Code Review ও Mentoring:** ১৫-২০%
- **Process ও Planning:** ১০-১৫%

এই Transition অনেকের জন্য কঠিন — কারণ Coding কমে যায়।

**সমাধান:** Delegate করতে শিখুন। Team-এর Senior Engineer-দের কাজ দিন। আপনি High-level Direction দিন এবং Block হলে সাহায্য করুন।

---

**Tech Lead বনাম Engineering Manager — পার্থক্য:**

অনেকে Confuse হন।

**Tech Lead:** Technical Authority। Design Review করেন, Architecture Decision নেন, Coding Standard ঠিক করেন। সাধারণত IC।

**Engineering Manager:** People Manager। Performance Review করেন, Hiring করেন, Career Development নিয়ে কাজ করেন। Code কম করেন।

একজন মানুষ দুটো Role একসাথে করতে পারেন — কিন্তু এটা কঠিন।

---

<a name="42"></a>
## ৪.২ Project Planning ও Risk Management

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা Project ৮ সপ্তাহে শেষ হওয়ার কথা। ১২ সপ্তাহে শেষ হলো। কেন? কারণ Planning-এ Risk বিবেচনা করা হয়নি।

### ✅ বইয়ের সমাধান

**Project Kickoff সঠিকভাবে করুন:**

Project শুরুর আগে সবার সাথে বসুন এবং নিশ্চিত করুন সবাই এক জায়গায়:

**Scope Definition:**
- কী করব? (In scope)
- কী করব না? (Out of scope) — এই দ্বিতীয় অংশ অনেক গুরুত্বপূর্ণ

**Milestone তৈরি করুন:**

```
Week 2: Database Schema ও API Contract Final
Week 4: Core Feature Ready for Internal Testing
Week 6: Beta Testing (10% Users)
Week 8: Full Production Rollout
```

Milestone থাকলে কখন কী হবে সবাই জানে এবং Progress Track করা যায়।

---

**Software Project Physics — এই সত্য জানুন:**

Gergely একটা গুরুত্বপূর্ণ কথা বলেন।

Project-এর তিনটা Constraint: **Scope, Time, Quality।**

এই তিনটার মধ্যে আপনি যেকোনো দুটো পাবেন, তিনটা নয়।

- **Fast + Good** → Scope কমাতে হবে
- **Fast + Full Scope** → Quality কমবে
- **Good + Full Scope** → বেশি সময় লাগবে

যখন Stakeholder বলেন "সব Feature দরকার, দ্রুত দরকার, Quality ভালো থাকবে" — এটা Physics-এর বিরুদ্ধে। Tech Lead-এর কাজ এটা ভদ্রভাবে বোঝানো এবং Tradeoff-এর সিদ্ধান্ত নিতে সাহায্য করা।

---

**Risk Management — সমস্যা আসার আগেই ভাবুন:**

**Risk Register তৈরি করুন:**

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Third-party API delay | High | High | Early integration, Fallback plan |
| Key engineer sick | Medium | High | Documentation, Knowledge sharing |
| Scope creep | High | Medium | Strict Change Control process |

**Most Important Risk — Dependency Risk:**

অন্য Team-এর কাজের উপরে নির্ভর করা সবচেয়ে বড় Risk।

**Solution — Early Integration:**

যত আগে সম্ভব অন্য Team-এর সাথে Integration করুন। Week 1-এ একটা Mock API দিয়ে শুরু করুন। Week 2-এ Real API দিয়ে Test করুন।

সমস্যা আগে ধরা পড়লে সমাধানের সময় থাকে।

---

<a name="43"></a>
## ৪.৩ Production-এ Ship করা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা Team নতুন Feature Launched করল। ১৫ মিনিটের মধ্যে ৫০,০০০ Users Error দেখল। Database Overload। ৩ ঘণ্টা Downtime। Revenue Loss।

কীভাবে এড়ানো যেত?

### ✅ বইয়ের সমাধান

**Feature Flag ব্যবহার করুন:**

Feature Flag মানে Code Production-এ আছে কিন্তু সবার কাছে চালু নয়।

```python
if feature_flags.is_enabled("new_checkout", user_id):
    return new_checkout_flow(cart)
else:
    return old_checkout_flow(cart)
```

**সুবিধা:**
- প্রথমে ১% User-এর কাছে চালু করুন। সমস্যা না হলে ৫%, ১০%, ১০০%।
- Production Bug হলে Flag বন্ধ করুন — নতুন Deployment লাগবে না।
- A/B Testing করতে পারবেন।

---

**Deployment Strategies:**

**Canary Deployment:**
নতুন Version-কে ১-৫% User-এর কাছে পাঠানো। সব ঠিক থাকলে ধীরে ধীরে বাড়ানো।

```
v1.0 → 95% Users
v1.1 → 5% Users (Canary)
↓
কিছুক্ষণ Monitor করুন
↓
v1.1 → 100% Users (সমস্যা না হলে)
```

**Blue-Green Deployment:**
দুটো Identical Environment রাখুন — Blue (Current) ও Green (New)।

নতুন Version Green-এ Deploy করুন। সব Test পাশ হলে Load Balancer-কে Green-এ Switch করুন।

Rollback মানে Load Balancer আবার Blue-তে নিয়ে যাওয়া — মাত্র কয়েক সেকেন্ড।

---

**Monitoring ও Alerting — Production-এর চোখ:**

Production-এ কী হচ্ছে না জানলে সমস্যা ধরা যায় না।

**তিনটা মূল Pillar:**

**Metrics:** সংখ্যাগত Data।
- Error Rate: প্রতি মিনিটে কতটা Error
- Latency: Request-এর Response Time (P50, P95, P99)
- Throughput: প্রতি সেকেন্ডে কত Request

**Logs:** ঘটনার Record।
- Structured Logging ব্যবহার করুন (JSON format)
- প্রতিটি Request-এর Trace ID থাকুক

**Traces:** Request-এর পুরো যাত্রা।
- একটা API Call Database, Cache, Third-party API — সব কোথায় কতটা সময় গেছে

---

**Incident Management:**

Production-এ সমস্যা হলে কী করবেন:

**Step 1 — Acknowledge:** "আমি দেখছি।" — এটাই প্রথম।

**Step 2 — Impact মূল্যায়ন:** কত User Affected? কোন Feature ভেঙেছে?

**Step 3 — Mitigate:** দ্রুত Impact কমান।
- Rollback করুন যদি সম্ভব হয়
- Feature বন্ধ করুন
- Traffic Divert করুন

**Step 4 — Root Cause:** সমস্যা কোথায় হলো?

**Step 5 — Post-Mortem লিখুন:**

Post-Mortem Blame করার জন্য নয়। শেখার জন্য।

```markdown
# Post-Mortem: [Incident Name] — [তারিখ]

## Summary
কী হয়েছিল? কতক্ষণ? Impact কতটা?

## Timeline
14:32 — Alert fired, Error rate 50%
14:35 — On-call engineer acknowledged
14:45 — Root cause identified: DB connection pool exhausted
15:10 — Rollback completed, service restored

## Root Cause
Database connection pool size ছিল 20।
নতুন Feature-এ প্রতিটা Request ৫টা DB Query করছিল।
High Traffic-এ Connection Exhausted।

## What Went Well
- Alert quickly fired
- Team সাথে সাথে Respond করেছে

## What Went Wrong
- Load Testing-এ এই Scenario Test হয়নি

## Action Items
- Connection Pool size বাড়ানো [Owner: X, Due: এই সপ্তাহে]
- Load Testing Pipeline-এ DB Connection Test যোগ করা [Owner: Y]
```

---

**SLO (Service Level Objective) — কী লক্ষ্য রাখবেন:**

SLO হলো আপনার Service-এর Quality Target।

উদাহরণ:
- Availability: ৯৯.৯% (মাসে সর্বোচ্চ ৪৪ মিনিট Downtime)
- Latency: P99 Latency ২ সেকেন্ডের কম
- Error Rate: ০.১%-এর কম

SLO না রাখলে "ভালো আছে কি না" বোঝার কোনো Benchmark নেই।

---

<a name="44"></a>
## ৪.৪ Stakeholder Management

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

Tech Lead একটা Feature-এর জন্য ৩ মাসের Timeline দিলেন। PM চান ১ মাসে। Tech Lead "না" বললেন কিন্তু কারণ বোঝাতে পারলেন না। PM Escalate করলেন VP-কে। VP-এর কাছে Tech Lead-এর Image খারাপ হলো।

অথবা উল্টো — Tech Lead PM-এর চাপে ১ মাসে হ্যাঁ বললেন। ১ মাসে Ship করতে পারলেন না। Team Overtime করল, Quality গেল, সবাই Stressed।

### ✅ বইয়ের সমাধান

**PM-এর সাথে Partnership তৈরি করুন:**

PM ও Tech Lead একটা Partnership।

PM-এর দায়িত্ব: **What** (কী Feature দরকার) এবং **Why** (Business Goal কী)।
Tech Lead-এর দায়িত্ব: **How** (কীভাবে করব) এবং **When** (কখন করা সম্ভব)।

সমস্যা তখন হয় যখন PM Technical Constraint বোঝেন না, বা Tech Lead Business Context বোঝেন না।

**সমাধান — Early Technical Involvement:**

Requirements আসার সময়েই Technical Feedback দিন।

PM বলছেন "এই Feature চাই।" সাথে সাথে জিজ্ঞেস করুন:
- "এই Feature কোন Business Problem Solve করছে?"
- "৮০% Feature দিলেও Problem Solve হবে?"
- "একটা Simple Version আগে Ship করে User Feedback নিতে পারি?"

এই কথোপকথন দিয়ে প্রায়ই দেখা যায় একটা Simpler Solution আছে যা দ্রুত করা যায়।

---

**"না" বলার শিল্প:**

কখনো কখনো Tech Lead-কে "না" বলতে হয়। কিন্তু শুধু "না" বললে কাজ হয় না।

**ভুলভাবে "না" বলা:**
"এটা ১ মাসে সম্ভব নয়।"

**সঠিকভাবে "না" বলা:**
"এই Full Feature ১ মাসে সম্ভব নয়। এর কারণ হলো [X, Y, Z Technical Dependency]। 

তবে আমাদের কাছে তিনটো Option আছে:
1. Core Feature ১ মাসে, বাকি ২ মাসে — এতে Business Value তাড়াতাড়ি পাবেন।
2. Full Feature ৩ মাসে — কিন্তু কোনো কমতি নেই।
3. Scope কমান — কোন Parts আপাতত বাদ দিলে Timeline কমানো যায়?

আপনি কোনটা Prefer করবেন?"

এভাবে বললে:
- আপনি Problem Acknowledge করেছেন
- Alternative Solution দিয়েছেন
- Decision-Making Power PM-এর কাছে দিয়েছেন

---

**Technical Debt ও Scope-এ Negotiation:**

"এই Feature-এর সাথে Refactoring-ও করতে চাই" — PM এটা শুনতে পছন্দ করেন না।

কীভাবে বলবেন:
"এই Feature করতে গেলে Payment Module-এর একটা অংশ Touch করতে হবে। সেখানে এখন একটা Technical Problem আছে যা আগামী ৬ মাসে আরও বড় সমস্যা হবে। এই Feature-এর সাথে এটাও ঠিক করলে মোট সময় ৩ সপ্তাহ — না করলে ২ সপ্তাহ। কিন্তু ৬ মাস পরে ওই সমস্যা Isolated করে ঠিক করতে ৫ সপ্তাহ লাগবে।

এখন ঠিক করলে ১ সপ্তাহ বেশি লাগে, কিন্তু ভবিষ্যতে ৩ সপ্তাহ বাঁচবে। কোনটা চান?"

---

<a name="45"></a>
## ৪.৫ Team গড়া ও Psychological Safety

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা Team-এ কেউ প্রশ্ন করতে ভয় পায়। Meeting-এ সবাই চুপ। একজন Senior Engineer কাউকে ছোট করে দিয়েছে — "এই প্রশ্নটা Stupid।" তারপর থেকে কেউ প্রশ্ন করে না। Bug লুকিয়ে যায়, সমস্যা বড় হয়।

### 🔍 কেন এই সমস্যা এত গুরুত্বপূর্ণ?

Google ৫ বছর ধরে Research করে দেখেছে — সবচেয়ে ভালো Team-এর সবচেয়ে বড় বৈশিষ্ট্য Technical Skill নয়। এটা **Psychological Safety।**

Psychological Safety মানে — Team-এর সবাই মনে করে ভুল করলে, প্রশ্ন করলে, নতুন Idea দিলে — শাস্তি হবে না।

### ✅ বইয়ের সমাধান

**Psychological Safety তৈরির পদক্ষেপ:**

**নিজে প্রথমে ভুল স্বীকার করুন:**
"আমি ভুল Design করেছিলাম। এটা থেকে শিখলাম — পরবর্তীতে Load Test আগে করব।"

এটা দেখে Team বুঝবে — এখানে ভুল স্বীকার করা Safe।

**Meeting-এ নিরাপদ পরিবেশ:**
কারো Idea Dismiss করবেন না। "এটা Stupid" কখনো বলবেন না।
যদি কারো Idea কাজ না করে, জিজ্ঞেস করুন: "এটা কীভাবে কাজ করবে এই Scenario-তে?" — এটা তাদের নিজেই বুঝতে দেয়।

**Junior-দের কথা বলার সুযোগ দিন:**
Meeting-এ Senior-রা সব কথা বলেন। Junior-দের জিজ্ঞেস করুন: "তোমার কী মনে হয়?"

---

**Tuckman's Model — Team Development:**

Gergely Tuckman-এর ৪ Stage উল্লেখ করেন:

**Forming:** Team নতুন। সবাই বিনয়ী, সতর্ক। কাজ ধীর।

**Storming:** Conflict শুরু হয়। "আমার পদ্ধতি ভালো, তোমারটা নয়।" এটা স্বাভাবিক। এখানে অনেক Team ভেঙে যায়।

**Norming:** Team নিজেদের পদ্ধতি খুঁজে পায়। Conflict কমে, Collaboration বাড়ে।

**Performing:** High Performance। সবাই একসাথে দুর্দান্ত কাজ করে।

Tech Lead-এর কাজ — Team-কে দ্রুত Performing Stage-এ নিয়ে যাওয়া।

**Storming Phase-এ কী করবেন:**
- Conflict Avoid করবেন না — এটা Necessary
- Safe Space তৈরি করুন যাতে Disagreement Productive হয়
- Clear Working Agreement তৈরি করুন

---

<a name="part-5"></a>
# Part 5 — Staff ও Principal Engineer

---

<a name="51"></a>
## ৫.১ Staff Engineer-এর দুনিয়া

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Senior Engineer Staff হওয়ার পরে বুঝলেন না কী করতে হবে। Manager বললেন "বড় Impact করুন।" কিন্তু কী করলে "বড় Impact" হয়? কোনো Clear Directive নেই।

### 🔍 কেন এই সমস্যা হয়?

Staff+ Level-এ কাজ Ambiguous হয়। Senior Engineer-এ কাজ Define থাকে। Staff Engineer-কে নিজেই বুঝতে হয় কোথায় Impact করা দরকার।

### ✅ বইয়ের সমাধান — Staff Engineer Archetype

Gergely বেশ কয়েকটি Archetype বর্ণনা করেন:

**Tech Lead Archetype:**
বড় Engineering Initiative বা Multiple Team-এর Technical দিক সামলান। এটা Scaled-up Tech Lead।

**Architect Archetype:**
System-এর Big Picture নিয়ে ভাবেন। কোনো নতুন System কীভাবে Design হবে, Technology Stack কী হবে — এই সিদ্ধান্ত নেন।

**Solver Archetype:**
কোম্পানির সবচেয়ে কঠিন, Hairy Technical সমস্যাগুলো Solve করেন। এক জায়গায় স্থায়ী নন — সমস্যা থেকে সমস্যায় যান।

**Right Hand Archetype:**
একজন Engineering Leader (CTO, VP of Engineering)-এর Technical Partner। Leader-এর দৃষ্টিভঙ্গি Implement করতে সাহায্য করেন।

---

**Staff Engineer-এর "Glue Work":**

Gergely একটা গুরুত্বপূর্ণ Concept আনেন — "Glue Work।"

Glue Work হলো সেই কাজ যা Team-কে একসাথে রাখে কিন্তু সরাসরি দেখা যায় না:
- Documentation লেখা
- Onboarding নতুন Engineer-দের
- Cross-team Meeting Facilitate করা
- Processes তৈরি ও Maintain করা

**সমস্যা:** Glue Work প্রায়ই Junior বা Mid-level Engineer-রা করে এবং Promotion-এ এটার Credit পায় না।

**Staff Engineer-এর ক্ষেত্রে:** Glue Work স্পষ্টভাবে Scope-এর অংশ। কিন্তু শুধু Glue Work করলে চলবে না — Technical Contribution-ও দরকার।

---

<a name="52"></a>
## ৫.২ Business বোঝা ও Technical সংযোগ

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Staff Engineer ৩ মাস ধরে একটা বড় Technical Improvement Project করলেন — Performance ৫০% উন্নত হলো। কিন্তু Leadership খুশি না। কারণ সেই Performance Improvement কোনো Business Metric-এ প্রভাব ফেলেনি।

### 🔍 কেন এই সমস্যা হয়?

Staff Engineer-রা প্রায়ই Technical Excellence-কে End Goal হিসেবে দেখেন। কিন্তু কোম্পানির End Goal হলো Business Outcome।

### ✅ বইয়ের সমাধান

**Technical Work = Business Outcome।**

Staff Engineer-কে সব সময় জিজ্ঞেস করতে হবে:
- "এই Technical কাজ কোন Business Goal-এ Contribute করছে?"
- "এটা না করলে Business-এ কী প্রভাব পড়বে?"
- "এর চেয়ে বেশি Impact করার অন্য কোনো Technical কাজ আছে?"

---

**Business Metrics জানুন:**

Staff Engineer হিসেবে এই Metrics বুঝুন:

**Revenue Metrics:**
- ARR (Annual Recurring Revenue) — বার্ষিক আবর্তনশীল আয়
- Churn Rate — মাসে কত % Customer চলে যাচ্ছে
- Customer LTV (Lifetime Value) — একজন Customer কত টাকার

**Product Metrics:**
- DAU/MAU — Daily/Monthly Active Users
- Retention Rate — User আবার আসছে কিনা
- Conversion Rate — কতজন Free থেকে Paid হচ্ছে

**Engineering Metrics:**
- Deployment Frequency
- Lead Time (Idea → Production)
- MTTR (Mean Time to Recovery)

---

**OKR ও Technical Roadmap Alignment:**

Company OKR: "Q2-তে User Retention ৫% বাড়ানো।"

Staff Engineer এটা দেখে ভাবেন:
- "কোন Technical Problem Retention কমাচ্ছে?"
- Error Rate বেশি → User Frustrated → চলে যাচ্ছে?
- Page Load ধীর → Poor Experience → চলে যাচ্ছে?
- Onboarding Flow জটিল → User বুঝছে না → চলে যাচ্ছে?

Technical Roadmap তৈরি করুন যা এই OKR-কে Directly Serve করে।

---

<a name="53"></a>
## ৫.৩ Influence Without Authority

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Staff Engineer বুঝলেন — পুরো Company-তে Authentication System দুর্বল। এটা ঠিক করা দরকার। কিন্তু এটা ৩টা আলাদা Team-এর সাথে জড়িত। তিনি কাউকে Order করতে পারেন না। কীভাবে পরিবর্তন আনবেন?

### 🔍 কেন এই সমস্যা হয়?

Staff Engineer Technical Authority আছে কিন্তু Organizational Authority নেই। "আমি Staff Engineer, তাই এটা করতে হবে" — এটা কাজ করে না।

### ✅ বইয়ের সমাধান

**Influence-এর পাঁচটা কৌশল:**

**১. আগে শুনুন — তারপর বলুন।**

প্রতিটি Team-এর Lead-এর সাথে বসুন। তাদের সমস্যা কী? তাদের Priority কী? আপনার Proposal তাদের কীভাবে সাহায্য করে?

না জেনে গিয়ে বললে "আপনি আমাদের সমস্যা বোঝেন না" শুনতে হবে।

**২. RFC লিখুন — সবাইকে Involve করুন।**

একটা সমস্যার Proposal লিখুন। সবাইকে পাঠান Review-এর জন্য।

এতে কী হয়:
- সবাই Feel করে তাদের মতামত নেওয়া হয়েছে
- Objection আগেই উঠে আসে ও Address হয়
- Final Decision-এ Collective Buy-in থাকে

**৩. Data দিয়ে কথা বলুন।**

"আমার মনে হয় Authentication System দুর্বল" → কেউ শুনবে না।

"গত ৬ মাসে ১২টা Security Incident হয়েছে Authentication Layer-এ। Engineer Hours Spend হয়েছে ৪০০ ঘণ্টা। ৩ Customer চলে গেছে Security Concern থেকে। এটা ঠিক করলে এই Risk কমবে।" → এটা Compelling।

**৪. ছোট শুরু করুন — Big Win দেখান।**

একটা Team-এ নতুন Approach Try করুন। সফল হলে অন্যরা নিজেই আসবে।

"আমরা Team X-এ নতুন Authentication Library Try করলাম। Security Incident ৮০% কমেছে। কেউ আগ্রহী?" — এটা অনেক বেশি কার্যকর।

**৫. Credit দিন — নিজের জন্য Advocate করবেন না।**

অন্য Team আপনার Idea থেকে সফল হলে — সেটা তাদের সাফল্য। আপনি Influence করেছিলেন — এটা আপনার।

Credit দেওয়া মানুষ Long-term-এ বেশি Trusted হন।

---

<a name="54"></a>
## ৫.৪ Reliable Systems তৈরি করা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা কোম্পানির Payment Service প্রতি মাসে একবার Down হয়। প্রতিবার Fix করা হয়, কিন্তু আবার হয়। Engineer-রা Reactive — সমস্যা হলে ঠিক করে, কিন্তু কেন হচ্ছে তা দেখে না।

### ✅ বইয়ের সমাধান

**Reliability-র মূল ধারণা:**

Reliability মানে শুধু "কাজ করছে" নয়। মানে System যখন দরকার তখন **সঠিকভাবে** কাজ করছে।

**Availability Numbers জানুন:**

| Availability | Monthly Downtime |
|-------------|-----------------|
| 99% | ৭.৩ ঘণ্টা |
| 99.9% | ৪৩.৮ মিনিট |
| 99.99% | ৪.৩ মিনিট |
| 99.999% | ২৬ সেকেন্ড |

Payment System-এ সাধারণত 99.99% Target থাকে।

---

**On-Call Engineering সঠিকভাবে করা:**

On-Call Engineering-এ সবচেয়ে বড় সমস্যা — **Alert Fatigue।**

প্রতি রাতে ৩টায় Alert আসলে এবং সেটা কোনো Real Action না চাইলে — Engineer Ignore করা শুরু করে। একদিন Real Alert Ignore হয়ে যায়।

**সমাধান — Alert Hygiene:**

প্রতিটা Alert এই Criteria পূরণ করতে হবে:
1. এই Alert আসলে কি কোনো Action নিতে হবে?
2. এই Action কি এখনই নিতে হবে (রাত ৩টায়)?
3. না হলে — Alert বন্ধ করুন বা ধীর করুন।

---

**Chaos Engineering:**

Netflix Chaos Monkey সবাই জানে। এর মূল Idea হলো — Production-এ ইচ্ছাকৃতভাবে Failure ঘটিয়ে দেখুন System কীভাবে Handle করে।

কেন? কারণ Real Failure আসার আগে দুর্বলতা জানা ভালো।

শুরু করুন ছোট করে:
- Development Environment-এ Database বন্ধ করুন — App কীভাবে Handle করে?
- একটা Third-party API ব্যর্থ হলে কী হয়?
- একটা Server বন্ধ হলে কী হয়?

---

**Runbook তৈরি করুন — ভবিষ্যতের নিজের জন্য:**

Runbook হলো — "এই সমস্যা হলে এই Steps Follow করো।"

```markdown
# Payment Service High Latency Runbook

## Symptoms
- Latency P99 > 2s
- Alert: payment-service-latency-high

## Immediate Actions
1. Check Dashboard: payment.grafana.com/payment-overview
2. Identify: Database? Third-party API? App Server?

## If Database:
   - Check DB Connection Pool: `kubectl exec -it db-pod -- psql -c "SELECT count(*) FROM pg_stat_activity"`
   - সমস্যা দেখলে: Connection Pool Size বাড়ান

## If Third-party API (Stripe):
   - Check Stripe Status: status.stripe.com
   - Switch to Fallback Mode: `kubectl set env deployment/payment PAYMENT_MODE=fallback`

## Escalation
30 মিনিটেও সমাধান না হলে: [Team Lead-এর নাম ও নম্বর]
```

---

<a name="55"></a>
## ৫.৫ Large-Scale Architecture

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা কোম্পানি Monolith থেকে Microservices-এ যেতে চায়। ৬ মাস পরে দেখা গেল — Complexity বেড়েছে, Bugs বেড়েছে, Team Slower হয়ে গেছে। কেন?

### 🔍 কেন এই সমস্যা হয়?

Microservices Trendy। অনেক কোম্পানি না বুঝেই যায়। কিন্তু Microservices একটা Scaling Pattern — যখন আসলেই Scale দরকার তখন।

### ✅ বইয়ের সমাধান

**Simplicity সবার আগে — Gergely-র সবচেয়ে গুরুত্বপূর্ণ Architecture Advice:**

"Premature Optimization is the root of all evil।"

জটিল Architecture তৈরি করার আগে জিজ্ঞেস করুন:
- এটা কি এখনই দরকার?
- Simple Solution কাজ করবে না?
- ৩ বছর পরে এই Architecture বুঝতে পারব?

**যে System সহজ, সে System Maintainable।**

---

**Strangler Fig Pattern — Safe Large-Scale Refactoring:**

পুরানো Monolith থেকে নতুন Architecture-এ যাওয়ার নিরাপদ পদ্ধতি।

```
পুরানো Monolith
        ↓
নতুন Service যোগ করুন পাশে
        ↓
আস্তে আস্তে Traffic Shift করুন
        ↓
পুরানো Code Retire করুন
```

**কেন Big Bang Rewrite ব্যর্থ হয়:**

"চলো সব ছেড়ে নতুন করে লিখি" — এটা ইতিহাসে বারবার ব্যর্থ হয়েছে।

Netscape Navigator পুরানো Code ছেড়ে নতুন করে লিখতে গিয়ে ৩ বছর কিছু Ship করতে পারেনি। এর মধ্যে Internet Explorer এগিয়ে গেছে।

Gergely পরামর্শ দেন — ছোট ছোট Incremental পরিবর্তন। প্রতিটা পরিবর্তন Test করুন। ধীরে ধীরে এগোন।

---

**Distributed Systems-এর চ্যালেঞ্জ — CAP Theorem:**

Distributed System-এ তিনটা Property একসাথে পাওয়া অসম্ভব:

- **Consistency:** সব Node-এ Same Data
- **Availability:** সব Request-এর Response পাওয়া যায়
- **Partition Tolerance:** Network ভাঙলেও System চলে

বাস্তবে Network ভাঙা (Partition) এড়ানো যায় না। তাই বেছে নিতে হয় — Consistency নাকি Availability?

**উদাহরণ:**

Banking System → Consistency Priority। একই Account থেকে দুটো জায়গায় একসাথে টাকা তোলা যাবে না।

Social Media Feed → Availability Priority। আপনার Feed-এ এখন নতুন Post না থাকলেও সমস্যা নেই — কয়েক সেকেন্ড পরে আসবে।

---

**Event Sourcing — কখন ব্যবহার করবেন:**

Event Sourcing মানে System-এর সব পরিবর্তন Event হিসেবে Store করা।

```
Traditional: Database-এ Current State রাখা
Event Sourcing: সব Event রাখা, Current State Derive করা

Traditional: Account Balance = 500
Event Sourcing:
  - Created Account: +1000
  - Withdrawal: -300
  - Deposit: +200
  - Fee: -400
  Final Balance = 500
```

**সুবিধা:**
- যেকোনো সময়ের State Reconstruct করা যায়
- Audit Trail স্বয়ংক্রিয়
- Bug হলে "কী হয়েছিল" পুরো History দেখা যায়

**অসুবিধা:**
- জটিল Implementation
- Storage বেশি লাগে
- কখনো কখনো Query কঠিন

---

<a name="36"></a>
## ৩.৬ Collaboration ও Teamwork — Senior স্তরে

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Senior Engineer Technical দিক থেকে অসাধারণ। কিন্তু Team-এর সাথে কাজ করতে গেলে সমস্যা হয়। Meeting-এ কথা বলতে পারেন না। লেখা দুর্বল। অন্য Team-এর সাথে Coordinate করতে পারেন না। ফলে তার Technical দক্ষতা পুরোপুরি কাজে লাগছে না।

### 🔍 কেন এই সমস্যা হয়?

Tech Education শুধু Technical Skill শেখায়। Communication, Collaboration — এগুলো কেউ শেখায় না। কিন্তু Senior হওয়ার পরে Technical Skill-এর চেয়ে এই Soft Skill-ই বেশি গুরুত্বপূর্ণ হয়ে যায়।

Gergely একটা গুরুত্বপূর্ণ কথা বলেন — **Senior Engineer-এর মোট Impact-এর ৫০%-এরও বেশি আসে Communication থেকে, Coding থেকে নয়।**

### ✅ বইয়ের সমাধান

**Technical Writing — Engineer-এর গোপন Superpower:**

Software Engineer হিসেবে যত ভালো লিখতে পারবেন, তত বেশি Impact করতে পারবেন।

কেন? কারণ:
- Design Doc লিখলে সবাই একই Page-এ আসে
- Email বা Slack Message স্পষ্ট হলে Meeting কমে
- Post-Mortem ভালো লিখলে সমস্যা Repeat হয় না
- RFC লিখলে Architecture Decision-এ Buy-in তৈরি হয়

**ভালো Technical Writing-এর নিয়ম:**

**BLUF (Bottom Line Up Front):**
সবচেয়ে গুরুত্বপূর্ণ কথা আগে বলুন। অনেকে Context দিতে দিতে মূল কথায় পৌঁছান না।

ভুল:
> "গত সপ্তাহে আমরা Payment Service-এ কাজ করলাম। বিভিন্ন Approach বিবেচনা করলাম। Team-এর সাথে আলোচনা করলাম। শেষে মনে হলো যে..."

সঠিক (BLUF):
> "Payment Service-এ আমার সুপারিশ হলো PostgreSQL-এর বদলে Redis ব্যবহার করা। কারণ..."

**Pyramid Principle:**
- প্রথম লাইনে Conclusion
- তারপর Main Points (৩টা)
- তারপর প্রতিটার Supporting Evidence

**Audience বুঝুন:**
- Technical Audience-এ Technical Detail দিন
- Non-technical Audience-এ Business Impact বলুন

---

**Effective Meeting — বেশিরভাগ Meeting অপ্রয়োজনীয়:**

Gergely বলেন — অনেক কোম্পানিতে Engineer-দের দিনের ৪০-৫০% Meeting-এ চলে যায়। এটা উৎপাদনশীলতার জন্য ক্ষতিকর।

**কোন Meeting দরকার নেই:**

- **Status Update Meeting:** এটা Async-এ করুন — Slack বা Email-এ।
- **Information Sharing Meeting:** Document পাঠান, সবাই পড়বে।
- **বড় Group-এ Decision Meeting:** ৭+ মানুষ থাকলে সিদ্ধান্ত হয় না, শুধু সময় নষ্ট।

**কোন Meeting দরকার আছে:**

- Complex Problem Discussion যেখানে Real-time Back-and-forth দরকার
- Team Alignment যেখানে Nuance আছে
- Relationship তৈরি

**ভালো Meeting চালানোর নিয়ম:**

Meeting-এর আগে Agenda পাঠান। Agenda না থাকলে Meeting করবেন না।

Meeting শুরুতে বলুন: "আজকে এই Meeting থেকে আমরা কী নিয়ে বের হব?"

Meeting শেষে: Action Items লিখুন — কে কী করবে কবের মধ্যে।

Meeting-এর পরে Summary পাঠান।

---

**Async Communication দক্ষতা:**

Remote বা Distributed Team-এ Async Communication সবচেয়ে গুরুত্বপূর্ণ।

**ভালো Async Message:**

সমস্যা, Context, এবং যা চান — তিনটাই একটা Message-এ বলুন।

ভুল:
> "একটু কথা বলতে পারব?"

সঠিক:
> "Payment Service-এ একটা Design Question আছে। Webhook Retry Logic-এ আমরা Exponential Backoff ব্যবহার করছি। কিন্তু Third-party API-এর Rate Limit ৬০ req/min। আমার মনে হচ্ছে Max Retry ৩ রাখলে আর ২ মিনিট Base Delay দিলে ভালো হবে। তোমার কী মনে হয়? [Code](link) এখানে।"

দ্বিতীয় Message পড়ে সঙ্গে সঙ্গে কাজ শুরু করা যায়।

---

**Knowledge Sharing — Team-কে Smarter করুন:**

Senior Engineer-এর একটা গুরুত্বপূর্ণ দায়িত্ব — Team-এর Collective Knowledge বাড়ানো।

**পদ্ধতিগুলো:**

**Tech Talk:** মাসে একবার ১৫-৩০ মিনিট — কিছু নতুন শিখলে Team-কে শেখান।

**Architecture Decision Records (ADR):** প্রতিটা বড় Technical সিদ্ধান্ত Document করুন:
```markdown
# ADR-001: Redis ব্যবহার Session Storage-এর জন্য

## Status: Accepted

## Context
User Session এখন Database-এ আছে। High Traffic-এ Bottleneck হচ্ছে।

## Decision
Redis ব্যবহার করব। In-memory, Fast, TTL Support আছে।

## Alternatives Considered
- Memcached: Redis-এর মতো কিন্তু Data Types কম
- JWT Token: Stateless কিন্তু Revocation কঠিন

## Consequences
- ভালো: DB Load কমবে, Latency কমবে
- খারাপ: নতুন Infrastructure Dependency
```

৬ মাস পরে কেউ প্রশ্ন করলে — "কেন Redis?" — এই ADR-ই উত্তর।

---

<a name="37"></a>
## ৩.৭ Senior Software Engineering — গভীরে যান

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### SOLID Principles — শুধু নাম নয়, আসল সমস্যা বুঝুন

SOLID Principles মুখস্থ করা সহজ। কিন্তু আসল সমস্যা কী এবং কীভাবে সমাধান করে সেটা না বুঝলে ব্যবহার করা যায় না।

---

**S — Single Responsibility Principle (SRP)**

**সমস্যা যা SRP সমাধান করে:**

```python
class UserService:
    def create_user(self, email, password):
        # User তৈরি
        user = User(email=email)
        
        # Email Validation
        if "@" not in email:
            raise ValueError("Invalid email")
        
        # Password Hashing
        hashed = bcrypt.hash(password)
        user.password = hashed
        
        # Database Save
        db.save(user)
        
        # Welcome Email পাঠানো
        smtp.send(email, "Welcome!", "...")
        
        # Analytics Log
        analytics.track("user_created", email)
        
        return user
```

এই Class-এ ৬টা দায়িত্ব। এখন যদি Email Sending বদলাতে হয় — UserService বদলাতে হবে। Analytics বদলাতে হলেও UserService বদলাতে হবে।

**SRP মেনে সমাধান:**

```python
class UserValidator:
    def validate(self, email, password): ...

class PasswordHasher:
    def hash(self, password): ...

class UserRepository:
    def save(self, user): ...

class EmailService:
    def send_welcome(self, email): ...

class UserAnalytics:
    def track_creation(self, email): ...

class UserService:
    def create_user(self, email, password):
        self.validator.validate(email, password)
        user = User(email=email, password=self.hasher.hash(password))
        self.repository.save(user)
        self.email_service.send_welcome(email)
        self.analytics.track_creation(email)
        return user
```

এখন প্রতিটা দায়িত্ব আলাদা। একটা বদলালে বাকিগুলো অপরিবর্তিত।

---

**O — Open/Closed Principle (OCP)**

**সমস্যা:**

```python
def calculate_discount(user, amount):
    if user.tier == "bronze":
        return amount * 0.05
    elif user.tier == "silver":
        return amount * 0.10
    elif user.tier == "gold":
        return amount * 0.20
    # নতুন Tier যোগ করতে হলে এখানে আরেকটা elif যোগ করতে হবে
    # এই Function বারবার বদলাতে হচ্ছে — OCP ভঙ্গ
```

**OCP মেনে সমাধান:**

```python
class DiscountStrategy:
    def calculate(self, amount): raise NotImplementedError

class BronzeDiscount(DiscountStrategy):
    def calculate(self, amount): return amount * 0.05

class SilverDiscount(DiscountStrategy):
    def calculate(self, amount): return amount * 0.10

class GoldDiscount(DiscountStrategy):
    def calculate(self, amount): return amount * 0.20

# নতুন Tier? শুধু নতুন Class যোগ করুন — পুরানো Code অপরিবর্তিত
class PlatinumDiscount(DiscountStrategy):
    def calculate(self, amount): return amount * 0.30
```

নতুন Tier যোগ করতে পুরানো Code ছোঁয়ার দরকার নেই।

---

**API Design — ভালো API তৈরির নিয়ম:**

**সমস্যা:**
```
GET /getUser?userId=123
POST /createNewOrder
GET /fetchAllProducts
DELETE /removeProduct?id=456
```

এটা দেখতে অসংগত। নিয়ম নেই।

**REST API-এর সঠিক নিয়ম:**

```
GET    /users/123          ← User পড়া
POST   /users              ← User তৈরি
PUT    /users/123          ← User সম্পূর্ণ Update
PATCH  /users/123          ← User আংশিক Update
DELETE /users/123          ← User মুছা

GET    /users/123/orders   ← User-এর Orders
POST   /orders             ← নতুন Order
```

**HTTP Status Code সঠিকভাবে ব্যবহার:**

| Code | কখন | উদাহরণ |
|------|-----|---------|
| 200 | সফল GET/PUT/PATCH | User পাওয়া গেছে |
| 201 | সফল POST | নতুন User তৈরি হয়েছে |
| 204 | সফল DELETE | User মুছা হয়েছে |
| 400 | ভুল Request | Email Format ভুল |
| 401 | Unauthenticated | Login করা নেই |
| 403 | Unauthorized | Permission নেই |
| 404 | Not Found | User নেই |
| 409 | Conflict | Email আগেই আছে |
| 500 | Server Error | Unexpected Error |

**Backward Compatibility রাখুন:**

একবার API Release করলে পুরানো Clients ভাঙা উচিত নয়।

ভুলটা — এক বছর পরে Field-এর নাম বদলানো:
```json
// আগে
{ "user_name": "John" }

// পরে (BREAKING CHANGE — পুরানো Client ভাঙবে)
{ "username": "John" }
```

সঠিক পদ্ধতি — নতুন Version তৈরি:
```
/api/v1/users  ← পুরানো, Deprecated হলেও চলে
/api/v2/users  ← নতুন
```

---

**Legacy Code নিয়ে কাজ করা:**

বেশিরভাগ Engineer Legacy Code দেখলে ভয় পায় বা রাগ করে। কিন্তু Gergely বলেন — Legacy Code হলো সফলতার চিহ্ন। পুরানো Code মানে এটা দীর্ঘদিন Production-এ চলেছে।

**Legacy Code-এ কাজ করার Strategy:**

**Rule 1 — প্রথমে বোঝার চেষ্টা করুন, Judgement পরে।**
"কেন এটা এভাবে করা হয়েছে?" — এই প্রশ্ন করুন। হয়তো ভালো কারণ ছিল।

**Rule 2 — Test আগে, Refactor পরে।**
Legacy Code-এ প্রথমে Characterization Test লিখুন — "এই Code এখন কী করে?" তারপর Refactor।

**Rule 3 — Strangler Pattern ব্যবহার করুন।**
পুরানো Code একসাথে Replace করবেন না। ধীরে ধীরে নতুন Behavior যোগ করুন।

---

<a name="46"></a>
## ৪.৬ Team Structure — Conway's Law ও Team Topology

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা কোম্পানি নতুন Microservices Architecture করল। কিন্তু ৬ মাস পরে দেখা গেল — Services-গুলো আসলে তাদের Team Structure-এর মতো। Payment Team-এর Service, User Team-এর Service, Order Team-এর Service। এগুলোর মধ্যে অনেক Dependency আর Coupling।

কেন এটা হলো?

### ✅ বইয়ের সমাধান — Conway's Law

**Conway's Law:**
> "Organizations which design systems are constrained to produce designs which are copies of the communication structures of those organizations."

সহজ বাংলায় — আপনার Software-এর Structure আপনার Organization-এর Communication Structure-এর মতো হবে।

**উদাহরণ:**

যদি আপনার Organization এরকম হয়:
```
Frontend Team | Backend Team | Database Team
```

তাহলে আপনার System হবে:
```
Frontend App → Backend API → Database Layer
```

এবং প্রতিটা Change-এ তিনটা Team-এর মধ্যে Coordinate করতে হবে।

**Inverse Conway Maneuver:**

Gergely বলেন — Architecture আগে ঠিক করুন, তারপর Team Structure সেই Architecture-এর মতো করুন।

যদি চান Independent Deploy করতে পারা Microservices, তাহলে Team Structure করুন:
```
Payment Team (Payment Service সম্পূর্ণ Own করে)
User Team (User Service সম্পূর্ণ Own করে)
Order Team (Order Service সম্পূর্ণ Own করে)
```

প্রতিটা Team তাদের Service End-to-End Own করে — Frontend থেকে Database পর্যন্ত।

---

**Team Topologies — চারটি Team Type:**

Gergely Team Topologies Framework উল্লেখ করেন (Skelton ও Pais-এর কাজ)।

**১. Stream-aligned Team:**

একটা Product Stream বা Feature Area-র জন্য সম্পূর্ণ দায়িত্বশীল।

- উদাহরণ: Checkout Team, User Onboarding Team
- End-to-end Ownership — Design থেকে Production পর্যন্ত
- Fast Flow — অন্য Team-এর জন্য অপেক্ষা কম

**২. Platform Team:**

অন্য Teams-দের কাজ সহজ করে এমন Platform তৈরি ও Maintain করে।

- উদাহরণ: DevOps/SRE Team, Developer Experience Team
- Stream-aligned Teams-কে "Self-service" Capability দেয়
- Abstraction করে — "Deploy করতে শুধু এই Command দাও"

**৩. Enabling Team:**

নতুন Technology বা Capability আনতে অন্য Teams-কে সাহায্য করে।

- উদাহরণ: Security Guild, Accessibility Team
- Temporary — কাজ শেষ হলে Dissolve হয় বা Embed হয়
- Coach ও Mentor হিসেবে কাজ করে

**৪. Complicated Subsystem Team:**

অত্যন্ত Complex Technical Area Handle করে।

- উদাহরণ: Machine Learning Infrastructure, Real-time Processing Engine
- Deep Specialist জ্ঞান দরকার
- অন্য Teams-কে Abstraction দেয়

---

**Hiring — সঠিক মানুষ আনুন:**

Tech Lead প্রায়ই Hiring-এ জড়িত থাকেন।

**Interview-এর সময় কী দেখবেন:**

**Technical Skill:** Coding, System Design — এটা সবাই দেখে।

**Problem Solving Approach:** "সমস্যাটা আমি এভাবে দেখছি" — কীভাবে ভাবছে সেটা দেখুন।

**Communication:** প্রশ্ন বুঝে Answer করছে কিনা, স্পষ্ট কথা বলতে পারছে কিনা।

**Growth Mindset:** "আমি ভুল করেছিলাম, এভাবে শিখেছি" — এই ধরনের কথা কি বলছে?

**Culture Add, Culture Fit নয়:**

"Culture Fit" শব্দটা প্রায়ই Bias-এর অজুহাত হিসেবে ব্যবহার হয়। এর বদলে জিজ্ঞেস করুন — "এই ব্যক্তি Team-এ নতুন কিছু যোগ করবে কিনা?"

Diverse Background, Different Perspective — এটা Team-কে Stronger করে।

---

**Onboarding — নতুন Engineer-এর প্রথম দিনগুলো:**

প্রথম ৩ মাসে একজন Engineer Team-এর সাথে কীভাবে Integrate হয় সেটা তার পুরো Experience নির্ধারণ করে।

**৩০-৬০-৯০ দিনের Plan:**

**Day 1-30 (Orientation):**
- সব Tool ও System Access
- Codebase-এর High-level Tour
- প্রথম ছোট Bug Fix বা Minor Feature
- Team-এর সবার সাথে 1:1

**Day 31-60 (Contributing):**
- Medium-complexity Feature
- Code Review-এ অংশগ্রহণ
- Team Meeting-এ Active Participation
- কোনো Process বা Documentation-এ Contribution

**Day 61-90 (Independent):**
- Full Feature Ownership
- Independently Problem Solve করা
- নতুন এলাকায় কাজ শুরু

---

<a name="47"></a>
## ৪.৭ Team Dynamics — গভীরে

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একটা Team-এ একজন Engineer আছেন যিনি Technically ভালো কিন্তু Collaboration-এ সমস্যা। Meeting-এ সবার কথা কেটে দেন। Code Review-এ Harsh। Junior-দের সাহায্য করেন না।

Tech Lead জানেন না কী করবেন। "এত ভালো Engineer, বের করে দেওয়া ঠিক হবে না।"

### ✅ বইয়ের সমাধান

**Brilliant Jerk সমস্যা:**

"Brilliant Jerk" হলো সেই মানুষ যিনি Individually দুর্দান্ত কিন্তু Team-কে Toxic করেন।

Gergely স্পষ্ট বলেন — **একজন Brilliant Jerk রাখা এবং Team-এর বাকি সবার Morale নষ্ট করা ঠিক নয়।** Research দেখায় Team-এ একজন Toxic মানুষ পুরো Team-এর Productivity ৩০-৪০% কমিয়ে দিতে পারে।

**কীভাবে Handle করবেন:**

১. **Private Conversation:** আচরণের Specific উদাহরণ দিয়ে বলুন কী সমস্যা হচ্ছে।

২. **Clear Expectation:** "এই Behavior বদলাতে হবে।" Vague নয়।

৩. **Support দিন:** কীভাবে বদলাবে সেটায় সাহায্য করুন।

৪. **Time Limit:** যদি না বদলায় — এস্কালেশন।

---

**Underperformer Handle করা:**

একজন Engineer Consistently Expectation পূরণ করছেন না।

Tech Lead প্রায়ই এই সমস্যা এড়িয়ে চলেন — কারণ Confrontation uncomfortable।

কিন্তু Gergely বলেন — এটা Avoid করা সবার জন্যই ক্ষতিকর। ওই Engineer নিজেই জানেন না সমস্যা কোথায়।

**Structured Approach:**

**Step 1 — Understand করুন।** কেন Performance কম? External Reason (Personal Issue, Health) নাকি Work Issue?

**Step 2 — Clear Feedback দিন।** "তোমার এই কাজে সমস্যা হচ্ছে। আমি দেখছি এই Pattern।"

**Step 3 — Support Plan তৈরি করুন।** কী Resources দরকার? কোথায় Skill Gap?

**Step 4 — Timeline ও Expectation।** "পরের ৩০ দিনে এটা দেখতে চাই।"

---

**Team-এর Working Agreement তৈরি করুন:**

Working Agreement হলো Team নিজেই তৈরি করা নিয়মের সেট।

উদাহরণ:
- Code Review: ২৪ ঘণ্টার মধ্যে Response
- Meeting: Agenda আগেভাগে পাঠাতে হবে
- On-call: Incident-এ সবাই Available থাকবে
- Communication: Technical Decision Slack-এ না, Document-এ

এটা Manager চাপিয়ে দেয় না — Team নিজে Agree করে তৈরি করে। ফলে সবাই Follow করে।

---

<a name="56"></a>
## ৫.৬ Staff স্তরের Collaboration

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

একজন Staff Engineer দুর্দান্ত Technical সিদ্ধান্ত নেন। কিন্তু Organization-এ তার কথা কেউ শোনে না। তিনি Frustrated — "আমার Idea-গুলো ভালো, কেউ মানছে না কেন?"

### 🔍 কেন এই সমস্যা হয়?

Technical Right হওয়া যথেষ্ট নয়। Organization-এর মধ্যে Trust তৈরি করতে হয়, Relationship রাখতে হয়, এবং Political Reality বুঝতে হয়।

### ✅ বইয়ের সমাধান

**Organizational Politics বোঝা — এটা অপরিহার্য:**

"Politics" শব্দটা নেতিবাচক শোনায়। কিন্তু Gergely বলেন — Politics মানে শুধু কীভাবে মানুষ Collective Decision নেয় তা বোঝা।

Staff Engineer হিসেবে বুঝতে হবে:
- কে কোন সিদ্ধান্ত নেওয়ার Authority রাখে?
- কোন Stakeholder কোন বিষয়ে Care করে?
- একটা Initiative কীভাবে Approval পাবে?

এই জ্ঞান ছাড়া সেরা Technical Idea-ও Implementation পায় না।

---

**Internal Network তৈরি করুন:**

Staff Engineer-কে শুধু নিজের Team-এর মধ্যে সীমাবদ্ধ থাকলে চলে না।

**কীভাবে Network তৈরি করবেন:**

- অন্য Team-এর Tech Lead-দের সাথে মাসে একবার Coffee Chat করুন
- Cross-team Working Group-এ যোগ দিন
- Company-wide Tech Talk দিন
- RFC লিখে সবাইকে Involve করুন

**Network-এর সুবিধা:**
- আপনার Initiative-এ Support পাবেন
- অন্য Team-এ কী হচ্ছে জানবেন — Duplicate কাজ এড়াবেন
- Opportunity এলে আপনার কথা মনে পড়বে

---

**External Visibility — Optional কিন্তু Valuable:**

Blog লেখা, Conference Talk, Open Source Contribution — এগুলো কাজে আসে।

কেন?
- Company-র বাইরেও Reputation তৈরি হয়
- Recruiting সহজ হয় — ভালো Engineer আপনার Team-এ আসতে চাইবে
- Internal-এও Credit বাড়ে
- নিজের চিন্তা গুছানোর সুযোগ

---

<a name="57"></a>
## ৫.৭ Staff স্তরের Software Engineering

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### 🔴 সমস্যা

Staff Engineer হওয়ার পরে একজন Codebase থেকে সরে গেলেন — "এখন আমি Strategy করি।" ১ বছর পরে তিনি আর Technical Discussion-এ Contribute করতে পারছেন না। Credibility কমে গেছে।

### 🔍 কেন এই সমস্যা হয়?

Staff Engineer-দের একটা বড় Trap হলো — Coding বন্ধ করে দেওয়া। কিন্তু Technical Credibility ছাড়া Staff Engineer-এর Influence কমে যায়।

### ✅ বইয়ের সমাধান

**Technical Depth বজায় রাখুন:**

Staff Engineer হিসেবে সব Code লিখবেন না — কিন্তু Technical Depth রাখুন।

কীভাবে:
- সপ্তাহে অন্তত কিছু Code লিখুন — Critical Path-এ
- Architecture Prototype নিজে করুন
- Code Review-এ Active থাকুন — শুধু High-level নয়, Detail-ও দেখুন
- নতুন Technology নিজে Trial করুন

---

**Technical Strategy তৈরি করা:**

Staff Engineer-এর একটা বড় দায়িত্ব — এক বছর বা তিন বছর পরে Technical Landscape কেমন হওয়া উচিত সেটা Define করা।

**ভালো Technical Strategy-র উপাদান:**

**Current State Assessment:**
- System-এর বর্তমান সমস্যা কী?
- Technical Debt কোথায়?
- কোথায় Bottleneck?
- Engineer-দের Pain Point কী?

**Future State Vision:**
- ১-৩ বছরে System কেমন হওয়া উচিত?
- Business Goal-এর সাথে কীভাবে Align?
- কোন Technology Adopt করব?

**Gap Analysis:**
- Current থেকে Future-এ যেতে কী কী করতে হবে?
- কোনটা আগে? (Priority)
- কোথায় Risk?

**Roadmap:**
- কোন Quarter-এ কী করব?
- কোন Team কোন কাজ নেবে?
- Success কীভাবে দেখব?

---

**Platform Thinking:**

Staff Engineer প্রায়ই Platform তৈরিতে জড়িত — এমন Infrastructure বা Tool যা অন্য Teams ব্যবহার করে।

**ভালো Platform-এর বৈশিষ্ট্য:**

- **Paved Road:** Default ভালো Path থাকে। Engineer-দের শুধু সেই Path Follow করলেই হয়।
- **Self-Service:** অন্য Team-এর কাছে যেতে না হলেও নিজেই করতে পারে।
- **Good Documentation:** কীভাবে ব্যবহার করতে হয় পরিষ্কার লেখা।
- **Versioning ও Backward Compatibility:** Platform Update হলে Existing User ভাঙবে না।

**উদাহরণ — Internal Deployment Platform:**

আগে: প্রতিটা Team নিজেদের মতো Deploy করত — ভিন্ন Script, ভিন্ন Process।

Platform তৈরির পরে:
```bash
# এক Command-এ Deploy
deploy my-service --env production --version 1.2.3
```

সব Team এক Command-এ Deploy করতে পারে। Platform Team Security, Rollback, Monitoring সব Handle করে।

---

**Engineering Principles প্রতিষ্ঠা করা:**

Staff Engineer একটা Company বা Division-এর Engineering Principles Define করেন।

উদাহরণ Principles:

```
Principle 1: Simplicity First
জটিল Solution-এর আগে Simple Solution বিবেচনা করুন।

Principle 2: Own Your Service
আপনি যা Build করেন, তার Reliability আপনার দায়িত্ব।

Principle 3: Data-Driven Decisions
"মনে হয়" নয়, Data দিয়ে সিদ্ধান্ত নিন।

Principle 4: API-First
Service তৈরির আগে API Contract Define করুন।

Principle 5: Security by Default
Security After-thought নয়, Design-এ Build করুন।
```

এই Principles-গুলো হলো North Star — যখন Tradeoff-এর সময় আসে, এগুলো Guide করে।

---

<a name="appendix"></a>
# Appendix — দরকারি Reference

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

## A. Career Progression Checklist

### Junior → Mid-level-এর জন্য প্রস্তুত?

- [ ] নির্দেশনা ছাড়াই Medium-complexity Task করতে পারি
- [ ] Estimation দিতে পারি এবং প্রায় সঠিক থাকি
- [ ] নিজের ভুল নিজে ধরতে পারি
- [ ] Code Review-এ Meaningful Feedback দিতে পারি
- [ ] Deadline Miss হলে আগেভাগে জানাই
- [ ] Documentation লিখতে পারি অন্যরা বুঝতে পারে এমন

### Mid-level → Senior-এর জন্য প্রস্তুত?

- [ ] Ambiguous Requirements থেকে নিজেই Concrete কাজ বের করতে পারি
- [ ] Junior Engineers-দের Effectively Mentor করি
- [ ] Technical Decision নিই এবং ব্যাখ্যা করতে পারি
- [ ] Cross-team Collaboration করতে পারি
- [ ] System Design বুঝি এবং প্রস্তাব করতে পারি
- [ ] Team-এর Output-এ Visible Impact করছি
- [ ] Technical Debt Identify ও বোঝাতে পারি

### Senior → Staff-এর জন্য প্রস্তুত?

- [ ] একাধিক Team-এ Technical Direction দিতে পারি
- [ ] Business Context বুঝে Technical Priority ঠিক করতে পারি
- [ ] Large-scale Technical Initiative Lead করতে পারি
- [ ] RFC লিখে Organization-wide Alignment তৈরি করতে পারি
- [ ] Executive-এর সাথে Technical Tradeoff আলোচনা করতে পারি
- [ ] Engineering Culture ও Process-এ Positive প্রভাব ফেলছি

---

## B. পরিস্থিতি ও বইয়ের পরামর্শ — Quick Reference

| পরিস্থিতি | বইয়ের পরামর্শ |
|-----------|----------------|
| Promotion আটকে আছে | Manager-কে জিজ্ঞেস করুন Specific Criteria কী। Sponsor তৈরি করুন। |
| Team Toxic মনে হচ্ছে | Psychological Safety আছে কিনা দেখুন। না থাকলে Change বিবেচনা করুন। |
| Blocked হয়ে আছি | ৩০ মিনিট নিজে চেষ্টা, তারপর স্পষ্টভাবে সাহায্য চান। |
| Technical Debt বাড়ছে | Business Impact-এ বোঝান, Incremental Fix Plan করুন। |
| Code Review Conflict | Data দিয়ে আলোচনা করুন, ছোট Experiment করুন। |
| Deadline Pressure | Scope কমানোর Option দিন, Quality vs Speed Trade-off বলুন। |
| Job Offer এসেছে | Total Compensation দেখুন, Negotiate করুন, Growth দেখুন। |
| Manager ভালো না | Skip-level-এর সাথে কথা বলুন অথবা Transfer বা Job Change। |
| New Tech শিখতে হবে | Small Project দিয়ে শুরু, Documentation পড়ুন, Community-তে যোগ দিন। |
| Remote-এ Visible নই | Daily Update দিন, Over-communicate করুন। |

---

## C. Gergely-র সুপারিশকৃত পড়ার তালিকা

### ক্যারিয়ার ও Leadership

| বই | লেখক | কেন পড়বেন |
|----|-------|------------|
| **The Staff Engineer's Path** | Tanya Reilly | Staff Engineering-এর সবচেয়ে ভালো Guide |
| **An Elegant Puzzle** | Will Larson | Engineering Management-এর Real-world Insight |
| **The Manager's Path** | Camille Fournier | IC থেকে Manager-এর পুরো Journey |
| **Staff Engineer** | Will Larson | Staff+ Role-এর Interviews ও Insights |

### Technical

| বই | লেখক | কেন পড়বেন |
|----|-------|------------|
| **Designing Data-Intensive Applications** | Martin Kleppmann | Distributed Systems-এর Best Book |
| **System Design Interview Vol 1 & 2** | Alex Xu | Interview Prep + Real Architecture |
| **Clean Code** | Robert C. Martin | Code Quality-র Foundation |
| **The Pragmatic Programmer** | Hunt & Thomas | Software Engineering Philosophy |
| **Accelerate** | Forsgren, Humble, Kim | Engineering Team Performance Research |

---

## D. মূল Framework সমূহ — এক পাতায়

**Self-Review লেখার Format:**
> সমস্যা কী ছিল → আমি কী করলাম → ফলাফল কী হলো (সংখ্যায়)

**Feedback দেওয়ার SBI Format:**
> Situation + Behavior + Impact

**Promotion চাওয়ার পদ্ধতি:**
> "আমি X হতে চাই → কোথায় Gap → Specific Plan → ৩ মাসে Review"

**"না" বলার পদ্ধতি:**
> সমস্যা স্বীকার → কারণ ব্যাখ্যা → ৩টা Alternative → সিদ্ধান্ত তাদের কাছে দিন

**Technical Debt বোঝানো:**
> Business Cost (সময়/টাকায়) → ভবিষ্যতের Risk → Fix-এর ROI

**RFC Format:**
> Context → Proposal → Alternatives → Tradeoffs → Open Questions

---

<a name="conclusion"></a>
# শেষ কথা — Gergely Orosz-এর মূল বার্তা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

Gergely Orosz বইয়ের শেষে এমন কিছু কথা বলেন যা সব স্তরের Engineer-এর জন্য প্রযোজ্য।

---

### কঠিন সত্য ১ — ভালো কাজ যথেষ্ট নয়

এটা অন্যায় মনে হতে পারে। কিন্তু এটাই বাস্তব।

ভালো কাজ করা Necessary কিন্তু Sufficient নয়। আপনাকে আরও করতে হবে:
- আপনার কাজ Visible করতে হবে
- Relationship তৈরি করতে হবে
- ক্যারিয়ার নিজে Drive করতে হবে

---

### কঠিন সত্য ২ — সব কোম্পানিতে সফল হওয়া যায় না

আপনার মূল্যবোধ, কাজের Style, Career Goal — এগুলো সব কোম্পানিতে Fit হয় না।

কিছু কোম্পানিতে আপনি Thrive করবেন, কিছুতে Survive করবেন।

মূল কাজ হলো — নিজেকে বোঝা, এবং সেই অনুযায়ী কোম্পানি বেছে নেওয়া।

---

### কঠিন সত্য ৩ — Burnout একটা Real Danger

Tech Industry "Hustle Culture"-কে Glorify করে। ৮০ ঘণ্টা কাজ করাকে Badge of Honor মনে করে।

Gergely বলেন — এটা Sustainable নয়। Burnout আসলে Performance কমায়, Creativity নষ্ট করে, এবং শেষে Career-ই ক্ষতিগ্রস্ত হয়।

নিজের যত্ন নেওয়া Professional Duty-র অংশ।

---

### সব স্তরের জন্য মূল Takeaway:

| Level | সবচেয়ে গুরুত্বপূর্ণ Focus |
|-------|---------------------------|
| **Junior** | শিখুন, Reliable হন, ভালো প্রশ্ন করুন |
| **Mid-level** | স্বাধীনভাবে কাজ করুন, Impact দেখান |
| **Senior** | Team-কে সফল করুন, Ambiguity Handle করুন |
| **Tech Lead** | Direction দিন, Stakeholder Manage করুন |
| **Staff** | Business ও Technical-এর Bridge হন |
| **Principal** | Company-র Long-term Technical Vision |

---

### শেষ পরামর্শ

> **প্রতিদিন একটু ভালো হওয়াই লক্ষ্য। কম্পাউন্ড ইন্টারেস্টের মতো — ছোট ছোট উন্নতি সময়ের সাথে বিশাল হয়।**

---

*Gergely Orosz রচিত The Software Engineer's Guidebook অবলম্বনে গভীর বাংলা সংস্করণ।*
*মূল বই: [engguidebook.com](https://www.engguidebook.com)*

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)
