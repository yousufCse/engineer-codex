# 📘 The Software Engineer's Guidebook
## বাংলা সংস্করণ — Gergely Orosz রচিত বইয়ের সম্পূর্ণ বাংলা গাইড

> **লেখক:** Gergely Orosz  
> **বাংলা রূপান্তর:** সহজ পাঠের জন্য  
> **উদ্দেশ্য:** Senior, Tech Lead, এবং Staff Engineer পদে সফলভাবে এগিয়ে যাওয়া

---

## 📑 সূচিপত্র (Table of Contents)

### 🔰 [ভূমিকা — এই বইটি কেন পড়বেন?](#ভূমিকা)

---

### 📦 [Part 1: Developer Career Fundamentals — ডেভেলপার ক্যারিয়ারের মূল ভিত্তি](#part-1-developer-career-fundamentals)

| অধ্যায় | বিষয় |
|--------|-------|
| [অধ্যায় ১](#অধ্যায়-১-career-paths) | Career Paths — ক্যারিয়ারের পথগুলো |
| [অধ্যায় ২](#অধ্যায়-২-owning-your-career) | Owning Your Career — নিজের ক্যারিয়ারের দায়িত্ব নেওয়া |
| [অধ্যায় ৩](#অধ্যায়-৩-performance-reviews) | Performance Reviews — পারফরম্যান্স মূল্যায়ন |
| [অধ্যায় ৪](#অধ্যায়-৪-promotions) | Promotions — পদোন্নতি |
| [অধ্যায় ৫](#অধ্যায়-৫-thriving-in-different-environments) | Thriving in Different Environments — বিভিন্ন পরিবেশে সফল হওয়া |
| [অধ্যায় ৬](#অধ্যায়-৬-switching-jobs) | Switching Jobs — চাকরি পরিবর্তন |

---

### 💻 [Part 2: The Competent Software Developer — দক্ষ Software Developer](#part-2-the-competent-software-developer)

| অধ্যায় | বিষয় |
|--------|-------|
| [অধ্যায় ৭](#অধ্যায়-৭-getting-things-done-junior-level) | Getting Things Done — কাজ সম্পন্ন করা (Junior স্তর) |
| [অধ্যায় ৮](#অধ্যায়-৮-coding) | Coding — কোড লেখার শিল্প |
| [অধ্যায় ৯](#অধ্যায়-৯-software-development) | Software Development — সফটওয়্যার ডেভেলপমেন্ট |
| [অধ্যায় ১০](#অধ্যায়-১০-tools-of-the-productive-engineer) | Tools of the Productive Engineer — উৎপাদনশীল Engineer-এর Tools |

---

### 🌟 [Part 3: The Well-Rounded Senior Engineer — সর্বগুণসম্পন্ন Senior Engineer](#part-3-the-well-rounded-senior-engineer)

| অধ্যায় | বিষয় |
|--------|-------|
| [অধ্যায় ১১](#অধ্যায়-১১-getting-things-done-senior-level) | Getting Things Done — Senior স্তরে কাজ সম্পন্ন করা |
| [অধ্যায় ১২](#অধ্যায়-১২-collaboration-and-teamwork) | Collaboration and Teamwork — সহযোগিতা ও Team কাজ |
| [অধ্যায় ১৩](#অধ্যায়-১৩-software-engineering-senior) | Software Engineering — Senior Engineer-এর Software Engineering |
| [অধ্যায় ১৪](#অধ্যায়-১৪-testing) | Testing — সফটওয়্যার পরীক্ষা |
| [অধ্যায় ১৫](#অধ্যায়-১৫-software-architecture) | Software Architecture — সফটওয়্যার স্থাপত্য |

---

### 🎯 [Part 4: The Pragmatic Tech Lead — বাস্তবমুখী Tech Lead](#part-4-the-pragmatic-tech-lead)

| অধ্যায় | বিষয় |
|--------|-------|
| [অধ্যায় ১৬](#অধ্যায়-১৬-project-management) | Project Management — প্রকল্প ব্যবস্থাপনা |
| [অধ্যায় ১৭](#অধ্যায়-১৭-shipping-in-production) | Shipping in Production — Production-এ Deploy করা |
| [অধ্যায় ১৮](#অধ্যায়-১৮-stakeholder-management) | Stakeholder Management — Stakeholder ব্যবস্থাপনা |
| [অধ্যায় ১৯](#অধ্যায়-১৯-team-structure) | Team Structure — Team-এর কাঠামো |
| [অধ্যায় ২০](#অধ্যায়-২০-team-dynamics) | Team Dynamics — Team-এর গতিশীলতা |

---

### 🚀 [Part 5: Role Model Staff and Principal Engineers — আদর্শ Staff ও Principal Engineers](#part-5-role-model-staff-and-principal-engineers)

| অধ্যায় | বিষয় |
|--------|-------|
| [অধ্যায় ২১](#অধ্যায়-২১-understanding-the-business) | Understanding the Business — ব্যবসা বোঝা |
| [অধ্যায় ২২](#অধ্যায়-২২-collaboration-staff-level) | Collaboration — Staff স্তরের সহযোগিতা |
| [অধ্যায় ২৩](#অধ্যায়-২৩-software-engineering-staff-level) | Software Engineering — Staff স্তরের Software Engineering |
| [অধ্যায় ২৪](#অধ্যায়-২৪-reliable-software-systems) | Reliable Software Systems — নির্ভরযোগ্য Software Systems |
| [অধ্যায় ২৫](#অধ্যায়-২৫-software-architecture-staff-level) | Software Architecture — Staff স্তরের Software Architecture |

---

### 🏁 [Part 6: উপসংহার — Conclusion](#part-6-conclusion)

---

## ভূমিকা

> *"আমার ক্যারিয়ারের প্রথম কয়েক বছরে আমি মনে করতাম শুধু কঠোর পরিশ্রম করলেই চলবে। তারপর একদিন দেখলাম আমাকে Promotion দেওয়া হলো না, আর আমার Manager আমাকে বলতে পারলেন না যে আমার কোথায় উন্নতি করতে হবে।"*
>
> — Gergely Orosz

এই বইটি সেই মানুষদের জন্য যারা Software Engineer হিসেবে ক্যারিয়ার গড়তে চান, Senior Engineer হতে চান, Tech Lead বা Staff Engineer পর্যন্ত পৌঁছাতে চান — কিন্তু কোথা থেকে শুরু করবেন বুঝতে পারছেন না।

### এই বইতে কী পাবেন?

- 🗺️ **Roadmap:** Entry-level থেকে Principal Engineer পর্যন্ত ক্যারিয়ারের পুরো নকশা
- 💡 **Practical Advice:** বাস্তবে কাজে লাগে এমন পরামর্শ
- 🔧 **Technical Skills:** Coding, Architecture, Testing — সব কিছু
- 🤝 **Soft Skills:** Communication, Teamwork, Leadership
- 🏢 **Company Insights:** Big Tech ও Startup-এ কীভাবে কাজ হয়

### এই বই কীভাবে পড়বেন?

এই বইয়ের ৬টি অংশ আছে। প্রতিটি অংশ **স্বাধীনভাবে** পড়া যায়।

- যদি আপনি নতুন Developer হন → **Part 1 ও Part 2** দিয়ে শুরু করুন
- যদি আপনি Senior হতে চান → **Part 3** পড়ুন
- যদি আপনি Tech Lead হতে চান → **Part 4** পড়ুন
- যদি আপনি Staff Engineer হতে চান → **Part 5** পড়ুন

---

# Part 1: Developer Career Fundamentals
## ডেভেলপার ক্যারিয়ারের মূল ভিত্তি

> এই অংশটি সব স্তরের Engineer-দের জন্য। চাই আপনি Fresher হোন বা Principal Engineer, এই অধ্যায়গুলো সবার কাজে আসবে।

---

## অধ্যায় ১: Career Paths
### ক্যারিয়ারের পথগুলো

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### টেক কোম্পানিগুলো কেমন হয়?

Software Engineer হিসেবে ক্যারিয়ার শুরু করার আগে বুঝতে হবে — কোন ধরনের কোম্পানিতে কাজ করতে চান।

#### কোম্পানির ধরনভেদ:

**১. Big Tech (FAANG/MAANG)**
- Microsoft, Google, Meta, Apple, Amazon, Netflix
- অনেক বেশি সুবিধা, বেতন ও শিক্ষার সুযোগ
- Process অনেক বেশি, কাজের গতি তুলনামূলক কম
- **Career Ladder** অনেক স্পষ্টভাবে সাজানো

**২. Scaleup / Growth-Stage Startup**
- উদাহরণ: Stripe, Airbnb, Uber (যখন ছোট ছিল)
- দ্রুত গতিতে কাজ, বেশি দায়িত্ব
- ভালো বেতন ও Equity (শেয়ার)
- Big Tech-এর মতো পরিষ্কার Career Ladder নেই

**৩. Early-Stage Startup**
- ছোট Team, খুব দ্রুত কাজ করতে হয়
- Equity থাকতে পারে যা পরে অনেক মূল্যবান হতে পারে
- Job Security কম, কিন্তু শেখার সুযোগ অনেক বেশি

**৪. Traditional/Enterprise কোম্পানি**
- Bank, Insurance, বড় Manufacturing কোম্পানি
- Stable চাকরি, কিন্তু ধীরে ধীরে কাজ হয়
- Legacy System নিয়ে কাজ করতে হয়
- Promotions অনেক সময়সাপেক্ষ

**৫. Agency/Consultancy**
- Client-এর কাজ করে দেওয়া হয়
- অনেক ধরনের Project ও Technology দেখার সুযোগ
- Career Growth সীমিত হতে পারে

---

### Software Engineer-এর Career Ladder কেমন?

বেশিরভাগ Tech কোম্পানিতে Career Ladder এভাবে থাকে:

```
Junior Software Engineer (L3 equivalent)
        ↓
Software Engineer (L4 equivalent)
        ↓
Senior Software Engineer (L5 equivalent)  ← এটি একটি গুরুত্বপূর্ণ ধাপ
        ↓
Staff Engineer (L6 equivalent)
        ↓
Principal Engineer (L7 equivalent)
        ↓
Distinguished Engineer / Fellow (L8+)
```

> 💡 **গুরুত্বপূর্ণ:** Senior Engineer পর্যন্ত পৌঁছানোটা সবার লক্ষ্য হওয়া উচিত। এর পরে আপনি **IC (Individual Contributor)** পথে (Staff/Principal) অথবা **Management** পথে যেতে পারবেন।

---

### Compensation (বেতন ও সুবিধা) বোঝা

Tech কোম্পানিতে Compensation সাধারণত ৪টি ভাগে থাকে:

| ভাগ | বিবরণ |
|-----|--------|
| **Base Salary** | মাসিক বেতন |
| **Bonus** | বার্ষিক বা ত্রৈমাসিক পুরস্কার |
| **Equity (RSU/Stock Options)** | কোম্পানির শেয়ার |
| **Benefits** | Health Insurance, Gym, Food ইত্যাদি |

> 💡 **Big Tech-এর "Tiers":** Gergely একটি অনানুষ্ঠানিক **Tier System** উল্লেখ করেন:
> - **Tier 1:** Google, Meta, Netflix — সর্বোচ্চ বেতন
> - **Tier 2:** Amazon, Microsoft, Apple, Stripe — খুবই ভালো বেতন
> - **Tier 3:** Scaleups ও Growth-stage Startup
> - **Tier 4:** Traditional কোম্পানি, Small Startups

---

### Cost Center বনাম Profit Center

এই ধারণাটি বোঝা অত্যন্ত গুরুত্বপূর্ণ:

**Profit Center:** যে Team সরাসরি টাকা আনে
- যেমন: Payment Team, Core Product Team
- এখানে বেতন ও Promotion সুযোগ বেশি

**Cost Center:** যে Team খরচ সাশ্রয় করে বা পরোক্ষভাবে সাহায্য করে
- যেমন: Internal Tools Team, HR Systems Team
- এখানে বেতন কম, Recognition কম পাওয়া যায়

> 💡 **পরামর্শ:** যদি সম্ভব হয়, Profit Center-এ যোগ দিন। এখানে আপনার কাজের মূল্য সরাসরি পরিমাপ করা যায়।

---

### IC Path বনাম Management Path

Senior Engineer হওয়ার পরে দুটি পথ আছে:

**Individual Contributor (IC) Path:**
- Staff Engineer → Principal Engineer → Distinguished Engineer
- Technical কাজ করতে ভালো লাগলে এই পথ নিন
- বড় Technical সিদ্ধান্ত নেওয়ার ক্ষমতা

**Management Path:**
- Engineering Manager → Senior Manager → Director → VP → CTO
- মানুষ পরিচালনা করতে ভালো লাগলে এই পথ নিন
- Team গড়া, Hiring, Budget নিয়ে কাজ

> 💡 **মনে রাখুন:** কোনো পথই অন্যটির চেয়ে শ্রেষ্ঠ নয়। যেটি আপনার ব্যক্তিত্ব ও আগ্রহের সাথে মিলে, সেটিই বেছে নিন।

---

## অধ্যায় ২: Owning Your Career
### নিজের ক্যারিয়ারের দায়িত্ব নেওয়া

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### আপনার ক্যারিয়ারের দায়িত্ব শুধু আপনারই

একটি সাধারণ ভুল ধারণা হলো — Manager ও কোম্পানি আমার ক্যারিয়ার দেখবে। **এটি সত্য নয়।**

আপনার Manager আপনাকে সাহায্য করতে পারেন, কিন্তু ক্যারিয়ার এগিয়ে নেওয়ার প্রধান দায়িত্ব আপনার নিজের।

---

### কাজ ভালোভাবে করা (Executing with Excellence)

ক্যারিয়ার বাড়ানোর প্রথম ধাপ হলো — **যে কাজ দেওয়া হয়েছে, তা অসাধারণভাবে করা।**

**ভালো Execution-এর বৈশিষ্ট্য:**
- ✅ Deadline মেনে চলা
- ✅ প্রয়োজনের বেশি কিছু দেওয়া (Under-promise, over-deliver)
- ✅ সমস্যা হলে আগেভাগে জানানো
- ✅ কাজের মান নিজেই যাচাই করা

---

### Work Log রাখা

**Work Log** হলো আপনার কাজের একটি ব্যক্তিগত রেকর্ড।

এটি গুরুত্বপূর্ণ কারণ:
- Performance Review-এর সময় নিজের কাজ মনে রাখা যায়
- Manager-কে আপনার Contribution সহজে দেখানো যায়
- নিজের অগ্রগতি নিজেই মূল্যায়ন করা যায়

**Work Log-এ কী লিখবেন:**
```
তারিখ: [তারিখ]
কী করলাম: [কাজের বিবরণ]
Impact: [এর ফলে কী হলো]
কী শিখলাম: [নতুন শিক্ষা]
```

---

### Feedback নেওয়া ও দেওয়া

**Feedback নেওয়ার সঠিক উপায়:**
- "আমি কীভাবে আরও ভালো করতে পারি?" — এই প্রশ্ন নিয়মিত জিজ্ঞেস করুন
- Feedback পাওয়ার পর তর্ক না করে মনোযোগ দিয়ে শুনুন
- Feedback-কে ব্যক্তিগতভাবে না নিয়ে কাজের উন্নতির সুযোগ হিসেবে দেখুন

**Feedback দেওয়ার সঠিক উপায়:**
- Specific হন: "তোমার Code ভালো হয়নি" নয়, বরং "এই Function-এর Error Handling আরও ভালো করা যায়"
- সময়মতো দিন: ঘটনার পরে বেশি দেরি না করে দিন
- Private-এ দিন: সবার সামনে কাউকে Criticize করবেন না

---

### Manager-এর সাথে ভালো সম্পর্ক রাখা

Manager আপনার বস, কিন্তু তিনি আপনার শত্রু নন। তিনি আপনার Career-এর সবচেয়ে গুরুত্বপূর্ণ Ally হতে পারেন।

**ভালো Manager Relationship-এর চাবিকাঠি:**

**১-on-1 Meeting কার্যকর করুন:**
- প্রতি সপ্তাহে ১-on-1 Meeting হওয়া উচিত
- Agenda আগেভাগে তৈরি করুন
- শুধু Status Update নয়, Career Goals ও Challenges নিয়ে কথা বলুন

**Manager-কে আপনার Goals জানান:**
- "আমি ৬ মাসের মধ্যে Senior Engineer হতে চাই" — এটি Manager-কে জানান
- Manager তখন সেই অনুযায়ী কাজ ও সুযোগ দিতে পারবেন

---

### Stretch, Execute, Coast মডেল

Gergely Orosz একটি সুন্দর মডেল দিয়েছেন:

**Stretching (প্রসারিত হওয়া):**
- নিজের Comfort Zone-এর বাইরে কাজ করা
- নতুন Technology বা বড় দায়িত্ব নেওয়া
- এই সময়টা কঠিন, কিন্তু সবচেয়ে বেশি শেখা যায়

**Executing (নিখুঁতভাবে করা):**
- পরিচিত কাজ দক্ষতার সাথে করা
- Team-এর জন্য Reliable হওয়া
- এই সময়টায় Quality ও Speed উভয়ই ভালো থাকে

**Coasting (বিশ্রাম নেওয়া):**
- কম চ্যালেঞ্জিং কাজ করা
- দীর্ঘ Stretching-এর পরে কিছুটা Recharge করা
- খুব বেশি সময় এই অবস্থায় থাকা ঠিক নয়

> 💡 **পরামর্শ:** বেশিরভাগ সময় **Executing**-এ থাকুন, মাঝে মাঝে **Stretching** করুন, এবং প্রয়োজনে **Coasting** করুন।

---

## অধ্যায় ৩: Performance Reviews
### পারফরম্যান্স মূল্যায়ন

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Performance Review কী এবং কেন গুরুত্বপূর্ণ?

**Performance Review** হলো এমন একটি প্রক্রিয়া যেখানে কোম্পানি নির্দিষ্ট সময় পরপর (সাধারণত ৬ মাস বা ১ বছর) আপনার কাজের মূল্যায়ন করে।

এটি গুরুত্বপূর্ণ কারণ:
- এর উপরে **Bonus** নির্ভর করে
- এর উপরে **Promotion** নির্ভর করে
- আপনার **Reputation** তৈরি হয়

---

### Performance Review-এর আগে কী করবেন?

**Self-Review লেখা:**
একটি ভালো Self-Review লেখার জন্য:

১. **Impact দিয়ে শুরু করুন** — "আমি X করেছি এবং এর ফলে Y হয়েছে"
   - খারাপ: "আমি Payment Service-এ কাজ করেছি"
   - ভালো: "আমি Payment Service-এর Latency ৪০% কমিয়েছি, যার ফলে User Satisfaction Score ১৫% বেড়েছে"

২. **Quantify করুন** — সংখ্যা দিন, বড় কথা নয়

৩. **Work Log ব্যবহার করুন** — পুরো বছরের কাজ মনে রাখতে

---

### Goals সেট করা

SMART Goals পদ্ধতি মনে রাখুন:
- **S**pecific — নির্দিষ্ট
- **M**easurable — পরিমাপযোগ্য
- **A**chievable — অর্জনযোগ্য
- **R**elevant — প্রাসঙ্গিক
- **T**ime-bound — সময়সীমাসহ

**উদাহরণ:**
- ❌ "আমি আরও ভালো Code লিখব"
- ✅ "আমি পরবর্তী Quarter-এ আমার সব Code-এ Unit Test Coverage ৮০%-এ নিয়ে যাব"

---

### Feedback Loop তৈরি করা

Performance Review-এর জন্য অপেক্ষা না করে নিয়মিত Feedback নিন:

**Informal Feedback:** প্রতিদিন বা প্রতি সপ্তাহে Manager ও সহকর্মীদের কাছ থেকে

**Formal Feedback:** ৩ মাস পরপর Mini Review করুন

**360° Feedback:** শুধু Manager নয়, Peers ও Junior-দের কাছ থেকেও Feedback নিন

---

### Calibration Process বোঝা

অনেক বড় কোম্পানিতে **Calibration** হয় — যেখানে বিভিন্ন Team-এর Manager-রা একসাথে বসে প্রত্যেক Engineer-এর Rating ঠিক করেন।

এই প্রক্রিয়ায় যা হয়:
- আপনার Manager আপনার হয়ে কথা বলেন
- অন্য Manager-রা প্রশ্ন করেন
- সবার Rating একটি নির্দিষ্ট **Distribution**-এ ফিট করানো হয়

> 💡 **কী করবেন:** আপনার Manager যেন আপনার Advocate হন। তার জন্য আপনার Impact সহজে বোঝানোর মতো তথ্য দিন।

---

### Rating Scale বোঝা

বেশিরভাগ কোম্পানিতে Rating কিছুটা এরকম থাকে:

| Rating | মানে |
|--------|------|
| Exceeds Expectations | Promotion-এর জন্য Strong প্রার্থী |
| Meets Expectations | কাজ ভালোভাবে হচ্ছে |
| Partially Meets | উন্নতি করতে হবে |
| Does Not Meet | PIP (Performance Improvement Plan) ঝুঁকি |

---

## অধ্যায় ৪: Promotions
### পদোন্নতি

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Promotion কীভাবে হয়?

Promotion পাওয়া শুধু ভালো কাজ করার বিষয় নয়। এটি একটি **Organizational Process।**

**Promotion-এর দুটি উপাদান:**

১. **Performance:** আপনি কতটা ভালো কাজ করছেন
২. **Readiness:** আপনি পরবর্তী Level-এর কাজ করতে পারছেন কিনা

---

### "Next Level" কাজ করা

সবচেয়ে বড় পরামর্শ হলো: **Promotion পাওয়ার আগেই Next Level-এর কাজ করুন।**

উদাহরণ:
- Senior Engineer হতে চাইলে → এখনই Junior Engineer-দের Mentor করুন, Technical Decision নিন
- Tech Lead হতে চাইলে → এখনই Project Coordination করুন, Stakeholder-এর সাথে যোগাযোগ করুন

---

### Promotion-এর জন্য যা লাগে

**Technical Skills:**
- Current Level-এর সব কাজ নিখুঁতভাবে করতে পারা
- Next Level-এর কাজ শুরু করা

**Impact:**
- Team-এর বাইরে Impact দেখানো
- Business-এর উপরে প্রভাব ফেলা

**Visibility:**
- আপনার কাজ সম্পর্কে সঠিক মানুষদের জানা দরকার
- "আমি নিজেকে বিক্রি করি না" — এই মানসিকতা ত্যাগ করুন

**Sponsorship:**
- একজন Senior Engineer বা Manager যিনি আপনার হয়ে কথা বলবেন
- Manager শুধু Mentor নয়, Sponsor হওয়া দরকার

---

### Promotion-এর সাধারণ সমস্যাগুলো

**সমস্যা ১: "আমি কাজ করছি, Promotion আপনা-আপনি হবে"**
- এটি হয় না। আপনাকে সক্রিয়ভাবে Promotion চাইতে হবে।

**সমস্যা ২: "আমার Manager আমাকে Promote করবেন না"**
- Manager-কে জিজ্ঞেস করুন: "আমাকে Promote করতে আপনার কী বাধা?"
- পরিষ্কার Timeline চান

**সমস্যা ৩: Level-এর বাইরে কাজ করছেন কিন্তু Promotion নেই**
- এটি ঠিক না। কথা বলুন।
- প্রয়োজনে Job Change বিবেচনা করুন।

---

### Promotion Timeline কেমন হওয়া উচিত?

| Level | সাধারণ সময় |
|-------|------------|
| Junior → Mid | ১.৫ - ২.৫ বছর |
| Mid → Senior | ২ - ৩ বছর |
| Senior → Staff | ৩ - ৫ বছর |
| Staff → Principal | ৫+ বছর |

> 💡 **মনে রাখুন:** এগুলো গড় সময়। আপনার Performance ভালো হলে দ্রুত হতে পারে।

---

## অধ্যায় ৫: Thriving in Different Environments
### বিভিন্ন পরিবেশে সফল হওয়া

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### প্রতিটি কোম্পানির Culture আলাদা

একটি কোম্পানিতে যা কাজ করে, অন্য কোম্পানিতে তা নাও করতে পারে।

**Fast-Paced Startup-এ টিকে থাকার উপায়:**
- Ambiguity মেনে নিন — সব সময় সব কিছু Clear থাকবে না
- Quickly Iterate করুন — Perfect নয়, Done হওয়া বেশি গুরুত্বপূর্ণ
- Context Switch করতে পারুন — একসাথে অনেক ধরনের কাজ করতে হবে

**Big Tech-এ সফল হওয়ার উপায়:**
- Process ও Documentation গুরুত্বপূর্ণ
- Data-driven সিদ্ধান্ত নিন
- Scale নিয়ে সব সময় চিন্তা করুন

**Remote Work-এ সফল হওয়ার উপায়:**
- Async Communication দক্ষতা বাড়ান
- লিখে যোগাযোগ করুন — কারণ সবাই একসাথে থাকে না
- Over-communicate করুন — "আমি এটা করছি" জানান

---

### Remote ও Hybrid কাজের পরিবেশ

Remote কাজে সফল Engineers যা করেন:
- লিখিত Update নিয়মিত দেন (Slack/Email)
- Timezone সম্পর্কে সচেতন থাকেন
- Video Call-এ Active থাকেন
- Documentation ভালো রাখেন

---

### Toxic Environment চেনা

কিছু লক্ষণ যা দেখলে সতর্ক থাকুন:
- 🚩 Blame Culture — কাউকে দোষ দিয়ে সমস্যা সমাধান করা হয়
- 🚩 No Psychological Safety — ভুল করলে শাস্তির ভয়
- 🚩 Micromanagement — কীভাবে কাজ করবেন তাও Manager ঠিক করে দেন
- 🚩 No Growth Opportunity — বছরের পর বছর একই কাজ

> 💡 **পরামর্শ:** Toxic Environment-এ বেশিদিন থাকবেন না। এটি আপনার Mental Health ও Career উভয়ের জন্যই ক্ষতিকর।

---

## অধ্যায় ৬: Switching Jobs
### চাকরি পরিবর্তন

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### কখন চাকরি পরিবর্তন করবেন?

**ভালো কারণ:**
- ✅ আর শেখার সুযোগ নেই
- ✅ বেতন Market Rate-এর চেয়ে অনেক কম
- ✅ Environment Toxic
- ✅ Career Growth থেমে গেছে
- ✅ Product বা Company আপনার মূল্যবোধের সাথে মেলে না

**খারাপ কারণ:**
- ❌ শুধু অল্প বেশি বেতনের জন্য
- ❌ ক্ষণিক রাগের মাথায়
- ❌ সমস্যা সমাধান না করেই পালানো

---

### Interview Preparation

**Coding Interview:**
- LeetCode, HackerRank, AlgoExpert-এ অনুশীলন করুন
- Data Structures: Array, Linked List, Tree, Graph, Hash Map
- Algorithms: Sorting, Searching, Dynamic Programming, BFS/DFS
- Time ও Space Complexity বোঝা

**System Design Interview:**
- Scalable System কীভাবে Design করতে হয় শিখুন
- Load Balancer, Database Sharding, Caching, Message Queue — এগুলো বুঝুন
- Alex Xu-এর "System Design Interview" বইটি পড়ুন

**Behavioral Interview (STAR পদ্ধতি):**
- **S**ituation: পরিস্থিতি কী ছিল
- **T**ask: আপনার কাজ কী ছিল
- **A**ction: আপনি কী করলেন
- **R**esult: ফলাফল কী হলো

---

### Offer Negotiation

**মনে রাখুন:** Initial Offer সবসময় Negotiate করুন।

**কীভাবে Negotiate করবেন:**
- একাধিক Offer থাকলে Leverage বেশি
- "আমি আপনার কোম্পানিতে খুব আগ্রহী, কিন্তু Compensation নিয়ে আলোচনা করতে চাই"
- Total Compensation দেখুন — শুধু Base Salary নয়

> 💡 **Rule of Thumb:** বেশিরভাগ ক্ষেত্রে, Job Change করলে আপনি Internally Promotion পাওয়ার চেয়ে বেশি Salary Increase পাবেন।

---

# Part 2: The Competent Software Developer
## দক্ষ Software Developer

> এই অংশটি Junior ও Mid-level Developer-দের জন্য বিশেষভাবে গুরুত্বপূর্ণ।

---

## অধ্যায় ৭: Getting Things Done (Junior Level)
### কাজ সম্পন্ন করা (Junior স্তর)

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Task Management দক্ষতা

**একটি Task পেলে কী করবেন:**

**১. বুঝুন প্রথমে:**
- কী তৈরি করতে হবে?
- কেন এটি দরকার?
- কখন লাগবে?
- কোন Standard মানতে হবে?

**২. Break Down করুন:**
- বড় Task-কে ছোট ছোট Subtask-এ ভাগ করুন
- প্রতিটি Subtask-এর Estimate দিন
- যদি কোনো Subtask অস্পষ্ট হয়, প্রশ্ন করুন

**৩. Communicate করুন:**
- আগেভাগে বলুন যদি Deadline মিস হওয়ার সম্ভাবনা থাকে
- Block হলে সাহায্য চান
- কাজ শেষ হলে সেটা জানান

---

### Estimation কীভাবে করবেন?

Estimation সবার জন্য কঠিন। কিছু Tips:

- **Optimistic নয়, Realistic হন:** "এটা ২ ঘণ্টার কাজ" বললে ৪ ঘণ্টা ধরুন
- **Buffer রাখুন:** Unexpected সমস্যার জন্য ২০-৩০% বেশি সময় ধরুন
- **পুরানো কাজ দেখুন:** আগে কতটা সময় লেগেছিল, সেটা Reference হিসেবে ব্যবহার করুন

---

### কার কাছে সাহায্য চাইবেন?

Junior Engineer হিসেবে সাহায্য চাওয়া দুর্বলতা নয়, বুদ্ধিমানের কাজ।

**তবে সাহায্য চাওয়ার আগে:**
- নিজে কমপক্ষে ৩০ মিনিট চেষ্টা করুন
- Error Message ভালো করে পড়ুন
- Google করুন
- Documentation পড়ুন

তারপরও না পারলে সাহায্য চান এবং বলুন:
- "আমি এটা করতে চাইছিলাম"
- "এই পর্যন্ত চেষ্টা করেছি"
- "এখানে আটকে গেছি"

---

## অধ্যায় ৮: Coding
### কোড লেখার শিল্প

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### ভালো Code কেমন হয়?

ভালো Code শুধু কাজ করে না — এটি **পড়া যায়, বোঝা যায় এবং পরিবর্তন করা যায়।**

**ভালো Code-এর বৈশিষ্ট্য:**

**১. Readable (পাঠযোগ্য):**
- ভালো Variable ও Function নাম দিন
- Code যেন নিজেই বলে কী হচ্ছে
- Comment শুধু "কেন" বোঝানোর জন্য, "কী" নয়

```python
# খারাপ
def calc(a, b, r):
    return a + b * r / 100

# ভালো
def calculate_total_with_tax(price, quantity, tax_rate_percent):
    return price + quantity * tax_rate_percent / 100
```

**২. Testable (পরীক্ষাযোগ্য):**
- Function ছোট রাখুন — একটি Function একটিই কাজ করুক
- Side Effects কমান
- Dependency Injection ব্যবহার করুন

**৩. Maintainable (রক্ষণাবেক্ষণযোগ্য):**
- DRY (Don't Repeat Yourself) নীতি মানুন
- Magic Numbers এড়িয়ে চলুন
- Constants ব্যবহার করুন

---

### Code Review

Code Review একটি Learning ও Quality Assurance Process।

**Code Review দেওয়ার সময়:**
- Respectful হন — মানুষকে নয়, Code-কে Review করুন
- "নিট-পিকিং" এড়িয়ে গুরুত্বপূর্ণ বিষয়ে Focus করুন
- Suggestion দিন, Command নয়: "এটা এভাবে করলে ভালো হবে না?" বনাম "এটা এভাবেই করো"

**Code Review পাওয়ার সময়:**
- Open-minded থাকুন
- Feedback Defensive হয়ে না নিয়ে শিখুন
- বুঝতে না পারলে জিজ্ঞেস করুন

---

### Debugging দক্ষতা

Debugging হলো একটি Systematic Process:

**Debugging-এর ধাপ:**
1. সমস্যাটি **Reproduce** করুন
2. **Isolate** করুন — সমস্যাটা কোথায়?
3. **Hypothesize** করুন — কী কারণ হতে পারে?
4. **Test** করুন — আপনার Hypothesis সঠিক?
5. **Fix** করুন
6. **Verify** করুন — সমস্যা সমাধান হয়েছে?

**Useful Debugging Tools:**
- Debugger (IDE-র Built-in বা Chrome DevTools)
- Logging (ঘটনাক্রম লিখে রাখা)
- Print Statements (সহজ কিন্তু কার্যকর)

---

### Refactoring

**Refactoring** মানে Code-এর Behavior না বদলে তার Structure উন্নত করা।

**কখন Refactor করবেন:**
- Code পড়তে কষ্ট হচ্ছে
- একই কোড বারবার Copy-Paste করতে হচ্ছে
- কোনো Change করতে অনেক জায়গায় বদলাতে হচ্ছে

**Boy Scout Rule:** কোড যখন Open করবেন, একটু হলেও Better করে রেখে আসুন

---

## অধ্যায় ৯: Software Development
### সফটওয়্যার ডেভেলপমেন্ট

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Programming Language দক্ষতা

**একটি Language ভালো জানার মানে:**
- ✅ Language-এর Idioms জানা (Pythonic code লেখা, Functional JavaScript ইত্যাদি)
- ✅ Standard Library ভালো করে জানা
- ✅ Performance implications জানা
- ✅ Common Pitfalls এড়ানো

**নতুন Language শেখার Tip:**
- "Hello World" নয়, একটি Real Project তৈরি করুন
- অন্যের Code পড়ুন
- Language-এর Official Documentation পড়ুন

---

### Version Control (Git)

Git ছাড়া আধুনিক Software Development সম্ভব নয়।

**Git Workflow:**
```
main branch (Production-এ যাবে)
    ↑
feature/my-feature branch (Feature Development)
    ↑
Commit করুন নিয়মিত
```

**Commit Message ভালো লেখার নিয়ম:**
```
feat: add user authentication with JWT
fix: resolve null pointer exception in payment service
docs: update API documentation
refactor: simplify order calculation logic
```

**Best Practices:**
- ছোট, Focused Commits করুন
- Meaningful Commit Messages লিখুন
- Main Branch-এ সরাসরি Push করবেন না

---

### Testing ধারণা (Basics)

**Test Pyramid:**
```
        /\
       /E2E\          ← কম, ধীর, কিন্তু Full Coverage
      /------\
     /Integration\    ← মাঝারি
    /------------\
   / Unit Tests   \   ← বেশি, দ্রুত, সহজ
  /----------------\
```

**Unit Test লেখার নিয়ম:**
- একটি Test একটিই জিনিস Test করুক
- Test নাম দিয়েই বোঝা যাক কী Test হচ্ছে
- AAA Pattern: Arrange, Act, Assert

```python
def test_calculate_total_with_tax():
    # Arrange
    price = 100
    quantity = 2
    tax_rate = 10

    # Act
    total = calculate_total_with_tax(price, quantity, tax_rate)

    # Assert
    assert total == 102  # 100 + 2 * 10/100 = 100 + 0.2 = ... 
    # এটি একটি উদাহরণ মাত্র
```

---

### Documentation লেখা

**কেন Documentation গুরুত্বপূর্ণ?**
- আপনি ৬ মাস পরে নিজেই ভুলে যাবেন
- নতুন Team Member দ্রুত বুঝতে পারবেন
- Debugging করা সহজ হবে

**কী ধরনের Documentation লিখবেন:**
- **README:** প্রজেক্টের Overview, Setup Instructions
- **API Documentation:** কীভাবে ব্যবহার করতে হয়
- **Architecture Document (ADR):** বড় সিদ্ধান্তগুলো কেন নেওয়া হয়েছে
- **Runbook:** Production সমস্যা হলে কী করতে হবে

---

## অধ্যায় ১০: Tools of the Productive Engineer
### উৎপাদনশীল Engineer-এর Tools

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Local Development Environment সাজানো

একটি ভালো Development Setup আপনার Productivity অনেক বাড়িয়ে দেয়।

**IDE বেছে নেওয়া:**
- **VS Code:** সব ধরনের কাজের জন্য ভালো, Extension-এ সমৃদ্ধ
- **JetBrains (IntelliJ, PyCharm, WebStorm):** Language-specific, অনেক বেশি Feature
- **Vim/Neovim:** অভিজ্ঞদের জন্য, অনেক দ্রুত

**IDE-র দরকারি Feature:**
- Code Completion (IntelliSense)
- Built-in Debugger
- Git Integration
- Terminal Integration
- Extensions/Plugins

---

### Terminal ও Command Line

Terminal দক্ষতা একজন Engineer-কে অনেক দ্রুত কাজ করতে সাহায্য করে।

**শিখে নিন:**
- Basic Shell Commands (ls, cd, grep, find, sed, awk)
- Shell Scripting (Bash)
- tmux বা Screen (Multiple Terminal Session)
- Zsh + Oh-My-Zsh (Terminal সুন্দর ও কার্যকর করা)

---

### Fast Iteration করার পদ্ধতি

**Hot Reload / Live Reload:** Code পরিবর্তন করার সাথে সাথে Result দেখা

**Makefile ব্যবহার:** Common Commands সংক্ষিপ্ত করা
```makefile
run:
    docker-compose up
test:
    pytest tests/
lint:
    flake8 src/
```

**Docker ব্যবহার:** Environment Consistency নিশ্চিত করা
- "My machine-এ কাজ করে" সমস্যা দূর হয়
- Production Environment Local-এ Replicate করা যায়

---

### Productivity Tools

**Communication:**
- **Slack/Teams:** Team Communication
- **Email:** আনুষ্ঠানিক যোগাযোগ
- **Notion/Confluence:** Documentation

**Task Management:**
- **Jira:** Software Development Project Management
- **Linear:** Modern, Fast Project Management
- **Trello:** Visual Task Board

**AI Coding Tools (২০২৪ সালের পরিপ্রেক্ষিতে):**
- **GitHub Copilot:** Code Suggestion
- **Cursor:** AI-first Code Editor
- **Claude/ChatGPT:** Code Explanation, Debugging Help

> 💡 **পরামর্শ:** AI Tools ব্যবহার করুন, কিন্তু AI-এর উৎপাদিত Code বুঝে নিন। Blindly Accept করবেন না।

---

# Part 3: The Well-Rounded Senior Engineer
## সর্বগুণসম্পন্ন Senior Engineer

> Senior Engineer হওয়া মানে শুধু ভালো Code লেখা নয়। এটি Technical Leadership, Collaboration, ও Broader Impact সম্পর্কে।

---

## অধ্যায় ১১: Getting Things Done (Senior Level)
### Senior স্তরে কাজ সম্পন্ন করা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Senior Engineer-এর দায়িত্ব বেশি

Junior Engineer শুধু নিজের কাজ করে। **Senior Engineer পুরো Team-কে সফল করে।**

**Senior Engineer-এর অতিরিক্ত দায়িত্ব:**
- নতুন Engineer-দের Mentor করা
- Technical Direction দেওয়া
- Ambiguous Requirements স্পষ্ট করা
- Cross-team Collaboration করা

---

### Task ও Project-এর মালিকানা নেওয়া (Ownership)

**Ownership মানে:**
- শুধু নিজের অংশ নয়, পুরো Project-এর দায়িত্ব নেওয়া
- যদি কোথাও সমস্যা হয়, Proactively সমাধান করা
- "এটা আমার কাজ না" বলে এড়িয়ে না যাওয়া

---

### Prioritization (অগ্রাধিকার নির্ধারণ)

Senior Engineer-কে বুঝতে হবে কোন কাজটি সবচেয়ে গুরুত্বপূর্ণ।

**Prioritization Framework:**

**Impact × Urgency Matrix:**
| | High Impact | Low Impact |
|--|--|--|
| **Urgent** | এখনই করুন | Delegate করুন |
| **Not Urgent** | Schedule করুন | বাদ দিন |

**Saying No:**
সব কাজ নেওয়া যাবে না। কোনো কাজ Decline করার সময়:
- কারণ বলুন
- Alternative দিন
- পরে করার সুযোগ থাকলে সেটা বলুন

---

### Perception বনাম Reality

একটি গুরুত্বপূর্ণ বিষয়: **অন্যরা আপনাকে কীভাবে দেখে, সেটাও গুরুত্বপূর্ণ।**

আপনি হয়তো দিনে ১২ ঘণ্টা কাজ করছেন, কিন্তু যদি কেউ না জানে — তাহলে কোনো লাভ নেই।

**Visibility বাড়ানোর উপায়:**
- Weekly Update পাঠান
- টিম Meeting-এ আপনার কাজ সংক্ষেপে শেয়ার করুন
- Slack-এ আপনার Progress Update করুন
- Stakeholder-দের সাথে সরাসরি যোগাযোগ রাখুন

---

## অধ্যায় ১২: Collaboration and Teamwork
### সহযোগিতা ও Team কাজ

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Technical Communication

**Writing Clearly (স্পষ্ট লেখা):**
Tech Engineer-দের মধ্যে সবচেয়ে Underrated Skill হলো ভালো লেখার দক্ষতা।

ভালো Technical Writing-এর নিয়ম:
- Simple ভাষা ব্যবহার করুন
- Bullet Points ও Headers দিন
- "Bottom Line Up Front" — প্রথমেই মূল কথা বলুন
- Audience বুঝে লিখুন (Technical বনাম Non-technical)

**Effective Meetings:**
Meeting-কে সবাই ভয় পায়। ভালো Meeting-এর বৈশিষ্ট্য:
- Clear Agenda থাকবে
- সঠিক মানুষ থাকবে
- সময়মতো শেষ হবে
- Action Items বের হবে

---

### Mentoring ও Coaching

Senior Engineer হিসেবে Junior-দের সাহায্য করা আপনারও উপকার করে:
- শেখার সেরা উপায় হলো শেখানো
- Team-এর Productivity বাড়ে
- Leadership Skills বিকশিত হয়

**Good Mentoring-এর উপায়:**
- উত্তর দেওয়ার আগে প্রশ্ন করুন
- শুধু Fish ধরে দেবেন না, মাছ ধরা শেখান
- তাদের Mistake থেকে শিখতে দিন

---

### Conflict Resolution

Engineering Team-এ Technical Disagreement স্বাভাবিক। কিন্তু কীভাবে Resolve করবেন?

**পদক্ষেপ:**
1. সবার মতামত শুনুন
2. Data দিয়ে আলোচনা করুন, Emotion নয়
3. যদি Agreement না হয় → ছোট Experiment করুন বা Senior-এর মতামত নিন
4. সিদ্ধান্ত হলে — "Disagree and Commit" — মেনে নিয়ে এগিয়ে যান

---

### Pair Programming

**Pair Programming** হলো দুজন একসাথে একটি Computer-এ কাজ করা।

**Driver:** Keyboard চালায়
**Navigator:** দেখে, পরামর্শ দেয়, বড় ছবি দেখে

**সুবিধা:**
- দ্রুত Knowledge Transfer
- Bug কম হয়
- Better Design সিদ্ধান্ত
- Junior-Senior-এর জন্য অসাধারণ

---

## অধ্যায় ১৩: Software Engineering (Senior)
### Senior Engineer-এর Software Engineering

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Design Patterns

**Design Pattern** হলো সাধারণ Software সমস্যার Proven সমাধান।

**সবচেয়ে প্রয়োজনীয় Patterns:**

**Creational Patterns (তৈরি করার Pattern):**
- **Singleton:** একটিমাত্র Instance
- **Factory:** Object তৈরির Logic আলাদা করা
- **Builder:** জটিল Object ধাপে ধাপে তৈরি করা

**Structural Patterns (কাঠামোর Pattern):**
- **Adapter:** বেমানান Interface কে একসাথে কাজ করানো
- **Decorator:** Object-এ নতুন Behavior যোগ করা
- **Facade:** জটিল System-কে সহজ Interface দেওয়া

**Behavioral Patterns (আচরণের Pattern):**
- **Observer:** Event হলে সবাইকে জানানো
- **Strategy:** Algorithm বদলানোর সুবিধা
- **Command:** Operation-কে Object হিসেবে Store করা

---

### SOLID Principles

**S — Single Responsibility Principle:**
একটি Class বা Function-এর শুধু একটিই দায়িত্ব থাকবে।

**O — Open/Closed Principle:**
নতুন Feature যোগ করতে পুরানো Code পরিবর্তন করা উচিত নয় — Extend করুন।

**L — Liskov Substitution Principle:**
Subclass-কে Parent Class-এর জায়গায় ব্যবহার করলেও কোনো সমস্যা হওয়া উচিত নয়।

**I — Interface Segregation Principle:**
বড় Interface-কে ছোট ছোট ভাগে ভাগ করুন।

**D — Dependency Inversion Principle:**
High-level Module Low-level Module-এর উপর নির্ভর করবে না — Abstraction-এর উপর নির্ভর করবে।

---

### API Design

ভালো API Design একটি গুরুত্বপূর্ণ Senior Engineer Skill।

**REST API Design নীতি:**
- Resource-based URL ব্যবহার করুন: `/users/123` (✅) বনাম `/getUser?id=123` (❌)
- Correct HTTP Methods: GET (পড়া), POST (তৈরি), PUT/PATCH (Update), DELETE (মুছা)
- Meaningful Status Codes: 200, 201, 400, 401, 403, 404, 500
- Versioning: `/api/v1/users`

**Backward Compatibility:**
- API পরিবর্তন করলে পুরানো Clients ভেঙে যাওয়া উচিত নয়
- Breaking Change হলে নতুন Version তৈরি করুন

---

## অধ্যায় ১৪: Testing
### সফটওয়্যার পরীক্ষা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### কেন Testing গুরুত্বপূর্ণ?

Testing ছাড়া Software Development একটি Blindfolded ব্যক্তির মতো কাজ করার মতো।

**Testing-এর সুবিধা:**
- Bug আগেভাগে ধরা পড়ে
- Refactoring নিরাপদ হয়
- Code Documentation হিসেবেও কাজ করে
- Confidence বাড়ে

---

### Test Types

**Unit Test:**
- একটি Function বা Class আলাদাভাবে Test করা
- দ্রুত, সহজ, কিন্তু সীমিত
- Dependencies Mock করা হয়

**Integration Test:**
- দুটি বা বেশি Component একসাথে Test করা
- Database, External API সহ
- Unit Test-এর চেয়ে ধীর

**End-to-End (E2E) Test:**
- পুরো System একজন Real User-এর মতো Test করা
- Browser Automation (Selenium, Playwright, Cypress)
- সবচেয়ে ধীর, কিন্তু Most Realistic

**Contract Test:**
- দুটি Service-এর মধ্যে Agreement Test করা
- Microservices-এ খুব গুরুত্বপূর্ণ

---

### TDD (Test-Driven Development)

**TDD পদ্ধতি:**
1. **Red:** প্রথমে একটি Failing Test লিখুন
2. **Green:** Test Pass করার ন্যূনতম Code লিখুন
3. **Refactor:** Code পরিষ্কার করুন

**TDD-র সুবিধা:**
- Design ভালো হয় — কারণ আপনি Testability নিয়ে আগেই ভাবছেন
- Over-engineering কমে
- Documentation হিসেবে কাজ করে

---

### Test Coverage

**Coverage মানে আপনার Code-এর কতটা অংশ Test-এ কভার হয়েছে।**

- ৮০% Coverage একটি ভালো লক্ষ্য
- ১০০% Coverage সবসময় সম্ভব বা দরকারি নয়
- **High Coverage = No Bugs নয়** — Tests-গুলো Meaningful হওয়া জরুরি

---

## অধ্যায় ১৫: Software Architecture
### সফটওয়্যার স্থাপত্য

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Architecture কী এবং কেন গুরুত্বপূর্ণ?

**Architecture** হলো Software-এর High-level Structure — Component গুলো কীভাবে সাজানো, কীভাবে একে অপরের সাথে কথা বলে।

ভালো Architecture:
- ✅ Change করা সহজ
- ✅ Scale করা যায়
- ✅ বুঝতে সহজ
- ✅ Test করা যায়

---

### Common Architecture Patterns

**Monolith:**
- সব কিছু একটি Application-এ
- শুরুতে Simple ও দ্রুত
- বড় হলে Maintenance কঠিন হয়

**Microservices:**
- ছোট ছোট Independent Service
- প্রতিটি Service আলাদা Deploy করা যায়
- Complexity বেশি, কিন্তু Scale ভালো

**Event-Driven Architecture:**
- Service গুলো Event দিয়ে কথা বলে
- Loose Coupling
- Async Processing

**Layered Architecture:**
```
Presentation Layer (UI, API)
        ↓
Business Logic Layer
        ↓
Data Access Layer
        ↓
Database
```

---

### Database Design

**Relational Database (SQL):**
- PostgreSQL, MySQL, SQLite
- ACID Properties (Atomicity, Consistency, Isolation, Durability)
- Complex Queries-এর জন্য ভালো

**NoSQL Database:**
- MongoDB (Document), Redis (Key-Value), Cassandra (Wide Column)
- Horizontal Scaling সহজ
- Schema Flexibility

**কখন কোনটি ব্যবহার করবেন:**
- Complex Relations, Transactions → SQL
- High Write Volume, Flexible Schema → NoSQL
- Caching, Session → Redis

---

### Caching

**Cache** ব্যবহার করে System অনেক দ্রুত হয়।

**Cache Strategy:**
- **Cache-Aside:** App Database থেকে আনে, Cache-এ রাখে
- **Write-Through:** Cache ও Database একসাথে Update হয়
- **Write-Behind:** Cache Update হয়, পরে Database-এ যায়

**Cache Eviction Policies:**
- LRU (Least Recently Used) — সবচেয়ে কম ব্যবহৃত বাদ দেওয়া
- LFU (Least Frequently Used) — সবচেয়ে কম ঘনঘন ব্যবহৃত বাদ দেওয়া

---

# Part 4: The Pragmatic Tech Lead
## বাস্তবমুখী Tech Lead

> Tech Lead হওয়া মানে সবচেয়ে Experienced Developer নন — এটি Technical Direction + People Leadership-এর সমন্বয়।

---

## অধ্যায় ১৬: Project Management
### প্রকল্প ব্যবস্থাপনা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Tech Lead-এর Project Management ভূমিকা

Tech Lead হলেন Engineering Team-এর Technical দিক পরিচালনাকারী ব্যক্তি।

**Tech Lead-এর দায়িত্ব:**
- Technical Decisions নেওয়া
- Project Planning ও Estimation
- Risk Management
- Stakeholder Communication
- Team Unblocking

---

### Agile ও Scrum

**Scrum Framework:**

**Sprint:** সাধারণত ২ সপ্তাহের একটি Development Cycle

**Sprint Planning:** Sprint শুরুতে কী কাজ করব ঠিক করা

**Daily Standup:** প্রতিদিন ১৫ মিনিটের Meeting
- আমি কাল কী করেছি?
- আমি আজ কী করব?
- কোনো Blocker আছে?

**Sprint Review:** Sprint শেষে কী তৈরি হলো দেখানো

**Sprint Retrospective:** কী ভালো হলো, কী উন্নত করতে হবে আলোচনা

---

### Project Planning

**Good Project Plan-এ কী থাকে:**

**১. Scope:** কী করা হবে এবং কী হবে না

**২. Timeline:** কখন কী শেষ হবে
- Milestone নির্ধারণ করুন
- Buffer রাখুন — সব সময় Expected-এর চেয়ে বেশি সময় লাগে

**৩. Dependencies:** কোন কাজ শুরু করতে হলে আগে কী দরকার

**৪. Risks:** কী কী সমস্যা হতে পারে এবং তার Plan কী

---

### Project Risk Management

**Risk Matrix:**
| Probability | Impact | করণীয় |
|------------|--------|--------|
| High | High | এখনই Address করুন |
| High | Low | Monitor করুন |
| Low | High | Contingency Plan রাখুন |
| Low | Low | Accept করুন |

**Common Project Risks:**
- Scope Creep — Project চলতে চলতে নতুন Requirements যোগ হওয়া
- Key Person Dependency — একজন মানুষ চলে গেলে সব থেমে যাওয়া
- Technical Debt — পরে ঠিক করব বলে রেখে দেওয়া সমস্যা

---

## অধ্যায় ১৭: Shipping in Production
### Production-এ Deploy করা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Deployment Process

**CI/CD Pipeline:**
```
Code Commit
    ↓
Automated Build
    ↓
Automated Tests (Unit, Integration)
    ↓
Code Review
    ↓
Deploy to Staging
    ↓
Manual/Automated QA
    ↓
Deploy to Production
```

**Feature Flags:**
New Feature Production-এ রেখে নির্দিষ্ট User-দের দেখানো
- ধীরে ধীরে Rollout করা যায়
- সমস্যা হলে তাৎক্ষণিক বন্ধ করা যায়

---

### Deployment Strategies

**Blue-Green Deployment:**
- দুটি Identical Environment (Blue ও Green)
- নতুন Version Green-এ Deploy, তারপর Traffic Switch
- Rollback তাৎক্ষণিক সম্ভব

**Canary Deployment:**
- মাত্র ১-৫% User-দের নতুন Version দেখানো
- সমস্যা না হলে ধীরে ধীরে বাড়ানো
- Risk অনেক কমে যায়

**Rolling Deployment:**
- একটি একটি করে Server Update করা
- Zero Downtime
- Rollback কিছুটা জটিল

---

### Incident Management

Production-এ সমস্যা হলে (Incident) কী করবেন:

**P1 (Critical):** সব Users Affected — এখনই ঠিক করতে হবে
**P2 (High):** অনেক User Affected — ঘণ্টার মধ্যে ঠিক
**P3 (Medium):** কিছু User Affected — ২৪ ঘণ্টার মধ্যে ঠিক
**P4 (Low):** Minor Issue — সময়মতো ঠিক

**Incident Response পদক্ষেপ:**
1. **Detect:** সমস্যা ধরা পড়া (Monitoring Alert)
2. **Respond:** On-call Engineer দায়িত্ব নেওয়া
3. **Mitigate:** দ্রুত সমাধান — পরিপূর্ণ না হলেও ক্ষতি কমানো
4. **Resolve:** স্থায়ী সমাধান
5. **Post-Mortem:** কী হলো, কেন হলো, ভবিষ্যতে কীভাবে ঠেকাবো

---

### Monitoring ও Observability

**তিনটি মূল স্তম্ভ:**

**Metrics:** সংখ্যাগত Data
- CPU Usage, Memory, Error Rate, Request Count
- Tools: Prometheus, Datadog, CloudWatch

**Logs:** ঘটনার রেকর্ড
- Structured Logging ব্যবহার করুন (JSON format)
- Tools: ELK Stack, Splunk, Loki

**Traces:** Request-এর পুরো যাত্রা
- Distributed System-এ Request কোথায় কতক্ষণ থাকল
- Tools: Jaeger, Zipkin, Datadog APM

---

### SLI, SLO, SLA

**SLI (Service Level Indicator):** আপনার Service কেমন চলছে তার Metric
- যেমন: Error Rate, Latency, Availability

**SLO (Service Level Objective):** আপনার Target
- যেমন: "৯৯.৯% সময় Service Available থাকবে"

**SLA (Service Level Agreement):** Customer-এর সাথে চুক্তি
- যদি SLO ভাঙা হয়, Customer-কে Credit দিতে হতে পারে

---

## অধ্যায় ১৮: Stakeholder Management
### Stakeholder ব্যবস্থাপনা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Stakeholder কারা?

**Stakeholder** হলেন যারা আপনার কাজের উপর প্রভাবিত হন বা আপনার কাজে প্রভাব ফেলেন।

**Common Stakeholders:**
- Product Manager (PM): কী তৈরি করতে হবে বলেন
- Engineering Manager (EM): Team-কে পরিচালনা করেন
- Designer: UI/UX Design করেন
- Business Leader: Business Goal নির্ধারণ করেন
- Customer/User: যারা আসলে Product ব্যবহার করেন

---

### Tech Lead ও Product Manager সম্পর্ক

**PM ও Tech Lead একটি Partnership:**
- PM: **What** ও **Why** (কী করতে হবে এবং কেন)
- Tech Lead: **How** ও **When** (কীভাবে এবং কখন)

**ভালো Partnership-এর চাবিকাঠি:**
- Early Technical Involvement — Requirements-এর সময়েই Technical Feedback দিন
- Tradeoff স্পষ্ট করুন — "এটা করতে ৩ মাস লাগবে, এই সহজ Alternative ৩ সপ্তাহে হবে"
- Business Context বুঝুন — কেন এই Feature দরকার?

---

### Technical Debt কীভাবে বোঝাবেন Non-technical Stakeholder-কে?

**Analogy ব্যবহার করুন:**
"Technical Debt হলো ঘরের ছাদে ছোট ফুটো থাকার মতো। এখন সমস্যা মনে না হলেও, বৃষ্টির সময় পুরো ঘর ভিজে যাবে।"

**Quantify করুন:**
"এই Technical Debt-এর কারণে প্রতিটি নতুন Feature তৈরিতে ২০% বেশি সময় লাগছে।"

---

### Difficult Conversations

Tech Lead-কে কঠিন কথা বলতে হয়:
- "এই Timeline সম্ভব নয়"
- "এই Feature-এর Technical Risk অনেক বেশি"
- "এই Design সঠিক নয়"

**কীভাবে বলবেন:**
- Data ও Evidence দিন
- Alternative সাজেস্ট করুন
- Respectful কিন্তু Clear থাকুন
- "না" বলার সময় কারণ বলুন

---

## অধ্যায় ১৯: Team Structure
### Team-এর কাঠামো

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Conway's Law

**Conway's Law:** যেকোনো Organization যে Software তৈরি করে, সেটি সেই Organization-এর Communication Structure-এর মতো হবে।

উদাহরণ: যদি ৪টি Team কাজ করে, তাহলে Software-ও ৪টি Component-এ ভাগ হবে।

**এর মানে:** Team Structure ঠিক করার সময় System Architecture মাথায় রাখুন।

---

### Team Topology

**Stream-aligned Team:**
- একটি Product বা Feature Area-র জন্য দায়িত্বশীল
- End-to-End Ownership
- উদাহরণ: Payment Team, User Profile Team

**Platform Team:**
- Other Team-দের কাজ সহজ করার জন্য
- Internal Tools, Infrastructure
- উদাহরণ: DevOps Team, Developer Experience Team

**Enabling Team:**
- New Technology বা Practices আনতে সাহায্য করে
- Temporary Basis-এ কাজ করে

**Complicated Subsystem Team:**
- অত্যন্ত জটিল Technical Area Handle করে
- উদাহরণ: Machine Learning, Real-time Processing

---

### Hiring

Tech Lead প্রায়ই Hiring Process-এ সম্পৃক্ত থাকেন।

**ভালো Engineer কীভাবে চিনবেন:**
- Technical Skills পরীক্ষা করুন (Coding, Design)
- Problem Solving পদ্ধতি দেখুন
- Communication দেখুন — কি তারা চিন্তা শেয়ার করতে পারে?
- Culture Fit দেখুন — কিন্তু "Culture Fit" কে Bias-এর অজুহাত বানাবেন না

---

## অধ্যায় ২০: Team Dynamics
### Team-এর গতিশীলতা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Psychological Safety

**Psychological Safety** মানে Team Member-রা ভুল করার, প্রশ্ন করার ও নতুন Idea দেওয়ার জন্য নিরাপদ মনে করেন।

Google-এর গবেষণায় দেখা গেছে, সবচেয়ে Effective Team-এর সবচেয়ে বড় বৈশিষ্ট্য হলো Psychological Safety।

**Psychological Safety তৈরির উপায়:**
- নিজেই ভুল স্বীকার করুন
- প্রশ্নের জন্য ধন্যবাদ দিন
- সমালোচনা সহানুভূতির সাথে করুন
- দোষ দেওয়া বন্ধ করুন, কারণ খোঁজুন

---

### Team Performance উন্নত করা

**Tuckman's Model:**
- **Forming:** Team নতুন — সবাই বিনয়ী, কিন্তু কাজ ধীর
- **Storming:** Conflict শুরু হয় — এটা স্বাভাবিক
- **Norming:** টিম নিজেদের মতো কাজের পদ্ধতি খুঁজে পায়
- **Performing:** High Performance — সবাই একসাথে দুর্দান্ত কাজ করে

Tech Lead-এর কাজ: Team-কে দ্রুত Performing Stage-এ নিয়ে যাওয়া।

---

### Onboarding নতুন Engineer

নতুন Engineer যোগ দিলে তাদের সঠিকভাবে Onboard করুন।

**ভালো Onboarding-এ কী থাকবে:**
- **Day 1:** Welcome, Setup (Computer, Access, Tools)
- **Week 1:** Codebase পরিচিতি, ছোট Task
- **Month 1:** একটি Real Feature তৈরি
- **Month 3:** Fully Autonomous হওয়া

---

# Part 5: Role Model Staff and Principal Engineers
## আদর্শ Staff ও Principal Engineers

> Staff Engineer পর্যায়ে Technical Excellence-এর পাশাপাশি Business Impact ও Organizational Influence অত্যন্ত গুরুত্বপূর্ণ।

---

## অধ্যায় ২১: Understanding the Business
### ব্যবসা বোঝা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### কেন একজন Engineer-কে Business বুঝতে হবে?

Staff Engineer শুধু Technical সমস্যা সমাধান করেন না — তারা **Business সমস্যার Technical সমাধান** করেন।

**Business বুঝলে যা হয়:**
- সঠিক Technical Priority নির্ধারণ করা যায়
- Stakeholder-দের সাথে কার্যকরভাবে কথা বলা যায়
- কোন Technical Debt এখন গুরুত্বপূর্ণ তা বোঝা যায়

---

### Key Business Metrics

**Revenue Metrics:**
- MRR (Monthly Recurring Revenue) — মাসিক আবর্তনশীল আয়
- ARR (Annual Recurring Revenue) — বার্ষিক আবর্তনশীল আয়
- Customer Acquisition Cost (CAC) — নতুন Customer আনার খরচ
- Customer Lifetime Value (LTV) — একজন Customer সারাজীবনে কত টাকা দেবে

**Product Metrics:**
- DAU/MAU (Daily/Monthly Active Users)
- Retention Rate — User ধরে রাখার হার
- Churn Rate — User চলে যাওয়ার হার
- Conversion Rate — Visitor থেকে Customer-এ রূপান্তরের হার

**Engineering Metrics:**
- Deployment Frequency — কতবার Deploy হয়
- Lead Time — Idea থেকে Production পর্যন্ত সময়
- MTTR (Mean Time to Recovery) — Incident থেকে Recovery-র গড় সময়

---

### OKR (Objectives and Key Results)

অনেক Tech কোম্পানি OKR ব্যবহার করে।

**Objective:** কী অর্জন করতে চাই (Qualitative)
**Key Results:** কীভাবে সফলতা পরিমাপ করব (Quantitative)

**উদাহরণ:**
- **Objective:** User Experience উল্লেখযোগ্যভাবে উন্নত করা
- **Key Result 1:** Page Load Time ৩ সেকেন্ড থেকে ১ সেকেন্ডে নামানো
- **Key Result 2:** Error Rate ২% থেকে ০.১%-এ নামানো
- **Key Result 3:** User Satisfaction Score ৬০ থেকে ৮০-এ নিয়ে যাওয়া

---

## অধ্যায় ২২: Collaboration (Staff Level)
### Staff স্তরের সহযোগিতা

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Influence Without Authority

Staff Engineer প্রায়ই অন্য Team-কে প্রভাবিত করেন কিন্তু তাদের Manager নন।

**Influence Without Authority-এর কৌশল:**

**১. Listen করুন গভীরভাবে:**
অন্যদের সমস্যা, প্রশ্ন ও চ্যালেঞ্জ মনোযোগ দিয়ে শুনুন।

**২. Actively Inquire করুন:**
অন্যদের Intention বোঝার জন্য প্রশ্ন করুন।

**৩. Clearly Articulate করুন:**
আপনার দৃষ্টিভঙ্গি পরিষ্কারভাবে বলুন — কারণসহ।

**৪. Champion Other's Ideas:**
অন্যের ভালো Idea-কে এগিয়ে নিয়ে যেতে সাহায্য করুন।

---

### RFC (Request for Comments) প্রক্রিয়া

**RFC** হলো একটি Technical Proposal যা অন্যদের Review ও Feedback-এর জন্য Open করা হয়।

**ভালো RFC-তে কী থাকে:**
- **Context:** কী সমস্যা সমাধান করছি?
- **Proposal:** আমার সমাধান কী?
- **Alternatives:** অন্য কী Options বিবেচনা করেছি?
- **Tradeoffs:** প্রতিটি Option-এর সুবিধা ও অসুবিধা কী?

---

### Cross-Team Collaboration

Staff Engineer প্রায়ই একাধিক Team-এর সাথে কাজ করেন।

**সফল Cross-team Collaboration-এর চাবিকাঠি:**
- প্রতিটি Team-এর Goals ও Constraints বোঝা
- Shared Vocabulary তৈরি করা
- Alignment-এর জন্য নিয়মিত Meeting
- Written Communication বেশি ব্যবহার করা (কারণ সবাই সব Meeting-এ থাকে না)

---

## অধ্যায় ২৩: Software Engineering (Staff Level)
### Staff স্তরের Software Engineering

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Technical Strategy

Staff Engineer-এর একটি বড় দায়িত্ব হলো Technical Direction নির্ধারণ করা।

**Technical Strategy তৈরির উপায়:**

**১. Current State বোঝা:**
- System-এর বর্তমান সমস্যাগুলো কী?
- Technical Debt কোথায়?
- কোথায় Bottleneck আছে?

**২. Future State ভাবুন:**
- ১-৩ বছরে System কেমন হওয়া উচিত?
- Business Goal-এর সাথে Align করুন

**৩. Roadmap তৈরি করুন:**
- Current থেকে Future-এ যাওয়ার পথ কী?
- কোন কাজটি আগে?
- Risk কোথায়?

---

### Large-Scale Refactoring

বড় System-এ Refactoring অনেক ঝুঁকিপূর্ণ।

**Safe Large-Scale Refactoring-এর পদ্ধতি:**

**Strangler Fig Pattern:**
- নতুন System ধীরে ধীরে পুরানো System-কে Replace করে
- Traffic ধীরে ধীরে নতুনে Shift হয়
- পুরানো System সঙ্গে সঙ্গে মুছা হয় না

**Feature Flag-এ মুড়িয়ে:**
- নতুন Implementation Feature Flag-এর পেছনে রাখুন
- Rollout ধীরে ধীরে করুন

---

## অধ্যায় ২৪: Reliable Software Systems
### নির্ভরযোগ্য Software Systems

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Reliability কী?

**Reliability** মানে System যখন দরকার তখন সঠিকভাবে কাজ করে।

**Availability:** System কতক্ষণ চালু থাকে
- ৯৯.৯% = প্রতি বছর ৮.৭৬ ঘণ্টা Downtime
- ৯৯.৯৯% = প্রতি বছর ৫২.৬ মিনিট Downtime

---

### On-Call Engineering

বড় Tech কোম্পানিতে প্রতিটি Engineering Team নিজের Service-এর জন্য **On-Call** থাকে।

**On-Call মানে:**
- ২৪/৭ Alert পাওয়া ও Respond করা
- Production Incident Handle করা

**ভালো On-Call Rotation:**
- কম তীব্র Alerts — বেশি Alert = Alert Fatigue
- Clear Runbook — Incident হলে কী করব লেখা থাকবে
- Fair Rotation — সবার সমান সুযোগ

---

### Chaos Engineering

**Chaos Engineering** হলো ইচ্ছাকৃতভাবে System-এ ব্যর্থতা ঘটিয়ে দেখা System কীভাবে মোকাবেলা করে।

Netflix-এর **Chaos Monkey** ছিল এই পদ্ধতির পথিকৃৎ — এটি Random Server বন্ধ করে দিত।

**লক্ষ্য:** দুর্ঘটনার আগে দুর্বলতা খুঁজে বের করা।

---

### Logging ও Monitoring Best Practices

**কী Log করবেন:**
- Request/Response (Important Fields)
- Errors সহ Stack Trace
- Security-relevant Events
- Performance Data

**কী Log করবেন না:**
- Password, Credit Card নম্বর (Sensitive Data)
- বড় Data Objects

**Alert Setup:**
- High Error Rate
- High Latency (P95/P99 Latency)
- Low Availability
- Unusual Traffic Pattern

---

## অধ্যায় ২৫: Software Architecture (Staff Level)
### Staff স্তরের Software Architecture

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### Distributed Systems-এর চ্যালেঞ্জ

**CAP Theorem:**
Distributed System-এ একসাথে তিনটি গ্যারান্টি দেওয়া সম্ভব নয়:
- **C**onsistency — সব Node একই Data দেখায়
- **A**vailability — সব সময় Request-এর Response পাওয়া যায়
- **P**artition Tolerance — Network ভেঙে গেলেও কাজ চলে

**বাস্তবে:** Partition Tolerance ছাড়া চলে না। তাই Consistency বনাম Availability-র মধ্যে Trade-off।

---

### Scalability

**Vertical Scaling (Scale Up):**
- আরও শক্তিশালী Machine ব্যবহার করা
- সহজ, কিন্তু সীমা আছে

**Horizontal Scaling (Scale Out):**
- আরও বেশি Machine যোগ করা
- জটিল, কিন্তু তাত্ত্বিকভাবে সীমাহীন

**Stateless vs. Stateful:**
- Stateless Service সহজে Horizontal Scale করা যায়
- State Database বা Cache-এ রাখুন

---

### Event Sourcing ও CQRS

**Event Sourcing:**
- System-এর সব পরিবর্তন Event হিসেবে Store করা
- যেকোনো সময়ের State Reconstruct করা যায়
- Audit Trail স্বয়ংক্রিয়ভাবে তৈরি হয়

**CQRS (Command Query Responsibility Segregation):**
- Read ও Write Operation আলাদা করা
- Read-এর জন্য Optimized Database, Write-এর জন্য আলাদা

---

### API Gateway ও Service Mesh

**API Gateway:**
- External Client-দের একটি Entry Point
- Authentication, Rate Limiting, Load Balancing

**Service Mesh:**
- Microservices-এর মধ্যে Communication ব্যবস্থাপনা
- Observability, Security, Traffic Management
- উদাহরণ: Istio, Linkerd

---

### Domain-Driven Design (DDD)

**DDD** হলো Software Design-এর একটি পদ্ধতি যেখানে Business Domain-কে কেন্দ্রে রাখা হয়।

**মূল ধারণা:**

**Bounded Context:**
- System-এর একটি অংশে একটি নির্দিষ্ট Vocabulary ও Model
- "Order" বিভিন্ন Context-এ আলাদা মানে থাকতে পারে

**Ubiquitous Language:**
- Developer ও Business Expert একই ভাষায় কথা বলেন
- Code-এ Business শব্দ ব্যবহার করুন

**Aggregate:**
- একসাথে Manage করা Entity-গুলোর Group
- একটি Aggregate-এর একটি Root থাকে

---

# Part 6: Conclusion
## উপসংহার

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)

---

### সব স্তরের জন্য মূল পাঠ

এই বইটির সব অংশ পড়ার পরে যে মূল শিক্ষাগুলো মনে রাখবেন:

---

**১. ক্যারিয়ারের দায়িত্ব নিজে নিন:**
আপনার Manager আপনাকে সাহায্য করতে পারেন, কিন্তু আপনার ক্যারিয়ার এগিয়ে নেওয়া শুধু আপনার দায়িত্ব।

**২. Impact দিয়ে চিন্তা করুন:**
"আমি কী করেছি" নয়, "আমার কাজে কী পরিবর্তন এসেছে" — এটি জিজ্ঞেস করুন।

**৩. Communication একটি Core Engineering Skill:**
Code লেখার মতোই Communication দক্ষতা জরুরি — বিশেষত Senior হওয়ার পরে।

**৪. Continuous Learning:**
Technology পরিবর্তন হয়, কিন্তু Fundamental Principles থাকে। Principles শিখুন।

**৫. People Matter:**
সবচেয়ে ভালো Code বা System কোনো মানুষ ছাড়া হয় না। Relationships বিনিয়োগ করুন।

---

### বিভিন্ন স্তরে মূল প্রত্যাশা

| Level | মূল দায়িত্ব | সাফল্যের মাপকাঠি |
|-------|------------|------------------|
| **Junior** | নির্দেশনা অনুযায়ী কাজ করা | Task সম্পন্ন করা, শেখা |
| **Mid** | স্বাধীনভাবে কাজ করা | Feature তৈরি করা |
| **Senior** | Team-কে সফল করা | Team-এর Output বাড়ানো |
| **Staff** | Multiple Team Influence | Company-wide Impact |
| **Principal** | Company Direction ঠিক করা | Long-term Technical Vision |

---

### Software Engineer হিসেবে বৃদ্ধির পথ

```
শেখা → অনুশীলন → শেখানো → নেতৃত্ব দেওয়া
  ↑                                    |
  |____________________________________|
              অনবরত চক্র
```

---

### শেষ কথা — Gergely Orosz-এর বার্তা

> *"আপনি যেখানেই আছেন আপনার ক্যারিয়ারে, আমি আশা করি এই বইটি আপনাকে একটি নতুন দৃষ্টিভঙ্গি এবং Engineer হিসেবে বৃদ্ধির নতুন ধারণা দিয়েছে।"*

**মনে রাখুন:**
- প্রতিটি দুর্দান্ত Engineer কোনো এক সময় Beginner ছিলেন
- Struggle করাটা Process-এর অংশ, দুর্বলতার চিহ্ন নয়
- আপনার Unique Experience ও Perspective মূল্যবান

---

## 📚 পরিশিষ্ট — দরকারি Resources

### বই (Books)

| বই | লেখক | বিষয় |
|----|-------|-------|
| The Staff Engineer's Path | Tanya Reilly | Staff Engineering |
| System Design Interview | Alex Xu | System Design |
| Clean Code | Robert C. Martin | Code Quality |
| The Pragmatic Programmer | Hunt & Thomas | Programming Philosophy |
| Designing Data-Intensive Applications | Martin Kleppmann | Distributed Systems |
| An Elegant Puzzle | Will Larson | Engineering Management |

---

### Online Resources

- **The Pragmatic Engineer Newsletter** (newsletter.pragmaticengineer.com) — Gergely Orosz-এর Newsletter
- **High Scalability** — Real-world Architecture Case Studies
- **Martin Fowler's Blog** — Software Architecture Patterns
- **LeadDev** — Engineering Leadership Articles

---

### দরকারি Technical Tools এর সারাংশ

| Category | Tool | ব্যবহার |
|----------|------|--------|
| Version Control | Git, GitHub, GitLab | Code Management |
| CI/CD | Jenkins, GitHub Actions, CircleCI | Automation |
| Containerization | Docker, Kubernetes | Deployment |
| Monitoring | Prometheus, Grafana, Datadog | Observability |
| Communication | Slack, Teams | Team Communication |
| Project Mgmt | Jira, Linear, Asana | Task Tracking |
| Cloud | AWS, GCP, Azure | Infrastructure |
| Databases | PostgreSQL, MongoDB, Redis | Data Storage |

---

## 🗺️ Quick Reference — Career Growth Checklist

### Junior Engineer হতে চাইলে:
- [ ] Programming Language ভালো করে শিখুন
- [ ] Data Structures & Algorithms শিখুন
- [ ] Git ভালো করে জানুন
- [ ] Unit Test লিখতে পারুন
- [ ] Code Review দিতে পারুন

### Senior Engineer হতে চাইলে:
- [ ] System Design জানুন
- [ ] Mentoring শুরু করুন
- [ ] Technical Leadership নিন
- [ ] Cross-team কাজ করুন
- [ ] Business Context বুঝুন

### Staff Engineer হতে চাইলে:
- [ ] Multiple Team-কে প্রভাবিত করতে পারুন
- [ ] Technical Strategy তৈরি করুন
- [ ] Executive Communication দক্ষতা গড়ুন
- [ ] Large-scale System Design করুন
- [ ] Organizational Impact দেখান

---

> **💡 শেষ পরামর্শ:** এই বইটি একটি Reference — বারবার ফিরে আসুন যখন নতুন চ্যালেঞ্জে পড়বেন।

---

*বাংলা রূপান্তর — Gergely Orosz রচিত The Software Engineer's Guidebook অবলম্বনে।*  
*মূল বই: [engguidebook.com](https://www.engguidebook.com)*

[🔝 সূচিপত্রে ফিরুন](#-সূচিপত্র-table-of-contents)
