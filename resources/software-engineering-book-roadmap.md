# 📚 Software Engineering Book Roadmap — একটি সম্পূর্ণ পড়ার গাইড

> একজন software engineer-এর জন্য foundation থেকে tech lead পর্যন্ত — কোন বই, কখন, কীভাবে পড়বেন এবং কীভাবে practice করবেন তার একটি ধাপে ধাপে roadmap।
>
> এই ডকুমেন্টে **২৩টি বই** ৭টি category-তে সাজানো আছে। প্রতিটি বইয়ের overview, কেন পড়বেন, কীভাবে পড়বেন এবং practice strategy দেওয়া আছে। শেষে একটি step-by-step reading plan আছে — কোথা থেকে শুরু করবেন আর কোথায় শেষ করবেন।

---

<a id="toc"></a>
## 🧭 সূচিপত্র (Table of Contents)

1. [কীভাবে এই ডকুমেন্ট ব্যবহার করবেন](#how-to-use)
2. [Level system: বই কোন stage-এর জন্য](#levels)
3. [সব বইয়ের সারসংক্ষেপ টেবিল](#overview)
4. [ক্যাটাগরি ১ — Code Craft & Quality](#craft)
5. [ক্যাটাগরি ২ — Object-Oriented Design & Architecture](#design)
6. [ক্যাটাগরি ৩ — System Design & Scalability](#system)
7. [ক্যাটাগরি ৪ — Data Structures, Algorithms & Coding Interview](#dsa)
8. [ক্যাটাগরি ৫ — Mobile Engineering](#mobile)
9. [ক্যাটাগরি ৬ — Career, Leadership & Process](#career)
10. [ক্যাটাগরি ৭ — Adjacent / Optional](#adjacent)
11. [📅 ধাপে ধাপে রিডিং প্ল্যান (কোথা থেকে শুরু, কোথায় শেষ)](#roadmap)
12. [🧠 কীভাবে প্রতিটি বই পড়বেন (Reading Strategy)](#reading-strategy)
13. [🏋️ Practice Strategy — পড়া কীভাবে skill-এ রূপান্তর করবেন](#practice)
14. [⚡ Quick Reference — পড়ার ক্রম এক নজরে](#quick-reference)

---

<a id="how-to-use"></a>
## 1. কীভাবে এই ডকুমেন্ট ব্যবহার করবেন
[⬆️ উপরে](#toc)

এই ডকুমেন্ট একটি **reference + roadmap** দুটোই।

- **নতুন বই বাছাই করতে চান?** → [সারসংক্ষেপ টেবিল](#overview) দেখুন, তারপর category section-এ গিয়ে detail পড়ুন।
- **জানেন না কোথা থেকে শুরু করবেন?** → সরাসরি [রিডিং প্ল্যান](#roadmap)-এ চলে যান।
- **একটা বই পড়া শুরু করেছেন?** → সেই বইয়ের *"কীভাবে পড়বেন"* অংশ আর general [Reading Strategy](#reading-strategy) পড়ুন।

**একটি গুরুত্বপূর্ণ নীতি:** বই পড়া আর skill তৈরি হওয়া এক জিনিস নয়। বই হলো map, কিন্তু রাস্তা হাঁটতে হবে code লিখে, project বানিয়ে, problem solve করে। তাই প্রতিটি category-তে *"Practice"* অংশটা skip করবেন না।

---

<a id="levels"></a>
## 2. Level system: বই কোন stage-এর জন্য
[⬆️ উপরে](#toc)

প্রতিটি বইয়ের সাথে একটি level ট্যাগ দেওয়া আছে:

| Level | মানে | কার জন্য |
|---|---|---|
| 🟢 **Foundation** | মূল ভিত্তি | Junior / শুরুর দিকের engineer |
| 🟡 **Intermediate** | দক্ষতা গভীর করা | Mid-level engineer (২–৫ বছর) |
| 🔴 **Advanced** | system ও leadership চিন্তা | Senior → Tech Lead (৫+ বছর) |
| 🎯 **Interview** | চাকরির interview প্রস্তুতি | যেকোনো level, job hunt-এর সময় |
| 🔵 **Reference** | শুরু-থেকে-শেষ পড়ার দরকার নেই, দরকারমতো দেখুন | সবাই |

> 📱 **Mobile → Tech Lead track:** যারা mobile engineer (Flutter / React Native / Android / iOS) হিসেবে কাজ করছেন এবং tech lead হতে চান, তাদের জন্য roadmap-এ আলাদা করে 📱 চিহ্ন দিয়ে বিশেষ বইগুলো দেখানো হয়েছে।

---

<a id="overview"></a>
## 3. সব বইয়ের সারসংক্ষেপ টেবিল
[⬆️ উপরে](#toc)

| # | বই | Category | Level | এক লাইনে |
|---|---|---|---|---|
| 1 | [Clean Code](#b-clean-code) | Craft | 🟢 Foundation | পরিষ্কার, পড়ার-যোগ্য code লেখার নিয়ম |
| 2 | [Refactoring](#b-refactoring) | Craft | 🟡 Intermediate | বিদ্যমান code নিরাপদে উন্নত করা |
| 3 | [Code Complete 2](#b-code-complete) | Craft | 🔵 Reference | software construction-এর বিশাল encyclopedia |
| 4 | [The Pragmatic Programmer](#b-pragmatic) | Craft | 🟢 Foundation | পেশাদার engineer-এর mindset |
| 5 | [A Philosophy of Software Design](#b-aposd) | Craft | 🟡 Intermediate | complexity কমানোই ভালো design |
| 6 | [97 Things Every Programmer Should Know](#b-97things) | Craft | 🔵 Reference | অভিজ্ঞদের ৯৭টি ছোট পরামর্শ |
| 7 | [Head First Design Patterns](#b-hfdp) | Design | 🟢 Foundation | design pattern সহজভাবে শেখা |
| 8 | [Head First OOA&D](#b-hfooad) | Design | 🟢 Foundation | object-oriented analysis ও design |
| 9 | [Clean Architecture](#b-clean-arch) | Design | 🟡 Intermediate | system-level structure ও boundary |
| 10 | [Object-Oriented Design Interview](#b-ood-interview) | Design | 🎯 Interview | LLD / OO design interview প্রস্তুতি |
| 11 | [Designing Data-Intensive Applications](#b-ddia) | System | 🔴 Advanced | distributed system-এর গভীর ভিত্তি |
| 12 | [System Design Interview — Vol 1](#b-sdi1) | System | 🎯 Interview | common system design pattern |
| 13 | [System Design Interview — Vol 2](#b-sdi2) | System | 🎯 Interview | advanced system design কেস |
| 14 | [System Design: The Big Archive](#b-bigarchive) | System | 🔵 Reference | system design কেসের বড় সংকলন |
| 15 | [Mobile System Design Interview](#b-msdi) | System | 🎯📱 Interview | mobile-নির্দিষ্ট system design |
| 16 | [Cracking the Coding Interview](#b-ctci) | DSA | 🎯 Interview | DSA + interview process |
| 17 | [Programming Contest & DS/Algo (বাংলা)](#b-contest-bn) | DSA | 🟢 Foundation | বাংলায় DSA-র মূল ভিত্তি |
| 18 | [52 Programming Problems (বাংলা)](#b-52-bn) | DSA | 🟢 Foundation | বাংলায় problem-solving drill |
| 19 | [Building Mobile Apps at Scale](#b-bmaas) | Mobile | 🔴📱 Advanced | বড় স্কেলে mobile engineering |
| 20 | [The Software Engineer's Guidebook](#b-guidebook) | Career | 🔴 Advanced | career growth ও seniority |
| 21 | [Software Engineering at Google](#b-swe-google) | Career | 🔴 Advanced | scale-এ engineering practice ও culture |
| 22 | [User Stories Applied](#b-user-stories) | Career | 🟡 Intermediate | agile-এ requirement ও user story |
| 23 | [Machine Learning Algorithm (বাংলা)](#b-ml-bn) | Adjacent | 🔵 Optional | বাংলায় ML-এর মূল algorithm |

---

<a id="craft"></a>
## ক্যাটাগরি ১ — Code Craft & Quality
[⬆️ উপরে](#toc)

> এই category-র বইগুলো শেখায় কীভাবে **পরিষ্কার, maintainable, পেশাদার code** লিখতে হয়। যেকোনো ভালো engineer-এর ভিত্তি এখান থেকেই শুরু।

<a id="b-clean-code"></a>
### 1. Clean Code — Robert C. Martin
**Level:** 🟢 Foundation | **আনুমানিক সময়:** ২–৩ সপ্তাহ

**Overview:** কীভাবে naming, function, class, comment, error handling এমনভাবে লেখা যায় যাতে অন্য মানুষ (এবং ৬ মাস পরের আপনি) সহজে বুঝতে পারে। এই বই code-কে "কাজ করলেই হলো" থেকে "পড়লে আনন্দ লাগে" পর্যায়ে নিয়ে যায়।

**কেন পড়বেন:** এটি craftsmanship-এর প্রথম ধাপ। ভালো naming আর ছোট function-এর অভ্যাস সারাজীবন কাজে দেবে।

**কীভাবে পড়বেন:** তাড়াহুড়ো নয়। প্রতিটি rule পড়ার পর নিজের পুরোনো code-এ সেটি প্রয়োগ করে দেখুন। শেষের "code smell" অধ্যায়গুলো বারবার দেখার মতো।

**Practice:** নিজের একটি পুরোনো file নিন → naming ঠিক করুন, বড় function ভাঙুন। আগে-পরে diff মিলিয়ে দেখুন।

> ⚠️ **সতর্কতা:** Clean Code-এর কিছু পরামর্শ (যেমন খুব ছোট function) নিয়ে [A Philosophy of Software Design](#b-aposd) ভিন্নমত দেয়। দুটোই পড়লে নিজের balanced judgment তৈরি হবে।

---

<a id="b-refactoring"></a>
### 2. Refactoring — Martin Fowler
**Level:** 🟡 Intermediate | **আনুমানিক সময়:** ৩–৪ সপ্তাহ

**Overview:** behavior না বদলে code-এর internal structure ধাপে ধাপে উন্নত করার একটি catalog। প্রতিটি refactoring-এর নাম, কখন করবেন, এবং নিরাপদে করার ছোট ছোট step দেওয়া আছে।

**কেন পড়বেন:** বাস্তবে আপনি বেশিরভাগ সময় নতুন code নয়, পুরোনো code নিয়ে কাজ করবেন। এই বই সেই code নিরাপদে বদলানোর শৃঙ্খলা শেখায়।

**কীভাবে পড়বেন:** Catalog অংশ পুরোটা মুখস্থ করার দরকার নেই — প্রথম অধ্যায়গুলো ভালো করে পড়ুন, তারপর catalog reference হিসেবে রাখুন। প্রতিটি refactoring-এর আগে test থাকা জরুরি, তাই testing mindset নিয়ে পড়ুন।

**Practice:** একটি ছোট test suite লিখুন → তারপর "Extract Function", "Rename Variable", "Replace Conditional with Polymorphism" প্রয়োগ করে দেখুন test সবুজ থাকে কিনা।

---

<a id="b-code-complete"></a>
### 3. Code Complete 2 — Steve McConnell
**Level:** 🔵 Reference | **আনুমানিক সময়:** পুরোটা একবারে নয়, দরকারমতো

**Overview:** software construction-এর প্রায় সব দিক নিয়ে ~৯০০ পৃষ্ঠার বিশাল encyclopedia — variable, loop, defensive programming, construction quality সবকিছু।

**কেন পড়বেন:** কোনো নির্দিষ্ট বিষয়ে গভীর, গবেষণা-ভিত্তিক ব্যাখ্যা দরকার হলে এটি অসাধারণ reference।

**কীভাবে পড়বেন:** শুরু-থেকে-শেষ পড়ার চেষ্টা করবেন না — অভিজ্ঞ engineer-এর জন্য অনেক অংশই পরিচিত লাগবে। বরং একটি অধ্যায় বেছে দরকারমতো পড়ুন। একে shelf-এ reference হিসেবে রাখুন।

**Practice:** আলাদা practice দরকার নেই; কোনো বিষয়ে confusion হলে সেই অধ্যায় খুঁজে পড়ুন।

---

<a id="b-pragmatic"></a>
### 4. The Pragmatic Programmer — Hunt & Thomas
**Level:** 🟢 Foundation | **আনুমানিক সময়:** ২ সপ্তাহ

**Overview:** একজন পেশাদার, চিন্তাশীল engineer কীভাবে কাজ করে — DRY principle, orthogonality, automation, দায়িত্ব নেওয়া, continuous learning ইত্যাদি নিয়ে ছোট ছোট অধ্যায়।

**কেন পড়বেন:** এটি technical নয় শুধু — এটি একটি **mindset** বই। অল্প সময়ে সবচেয়ে বেশি ROI দেয়। career-এর শুরুতে পড়লে চিন্তার ধরন বদলে যায়।

**কীভাবে পড়বেন:** ছোট অধ্যায়, তাই রোজ একটা-দুটো করে পড়ুন। প্রতিটি tip নিজের কাজের সাথে মিলিয়ে নিন।

**Practice:** একটি repetitive কাজ বেছে সেটি automate করুন (script লিখুন)। DRY violation খুঁজে দূর করুন।

---

<a id="b-aposd"></a>
### 5. A Philosophy of Software Design — John Ousterhout
**Level:** 🟡 Intermediate | **আনুমানিক সময়:** ১ সপ্তাহ (~১৯০ পৃষ্ঠা)

**Overview:** ভালো design মানে **complexity কমানো**। "deep module" (সহজ interface, জটিলতা ভেতরে লুকানো) ধারণাটি এই বইয়ের কেন্দ্র। ছোট কিন্তু গভীর বই।

**কেন পড়বেন:** এটি Clean Code-এর কিছু নিয়মকে চ্যালেঞ্জ করে — যেমন comment আর function-এর আকার নিয়ে। দুই দৃষ্টিভঙ্গি জানলে আপনার design judgment পরিণত হবে।

**কীভাবে পড়বেন:** ধীরে পড়ুন, কারণ প্রতিটি ধারণা চিন্তা করার মতো। Clean Code পড়ার পর পড়লে সবচেয়ে বেশি উপকার।

**Practice:** নিজের কোনো module নিন → প্রশ্ন করুন: "এর interface কি যথেষ্ট সহজ? জটিলতা কি ভেতরে লুকানো নাকি caller-এর উপর চাপানো?" সেই অনুযায়ী redesign করুন।

---

<a id="b-97things"></a>
### 6. 97 Things Every Programmer Should Know — Kevlin Henney (ed.)
**Level:** 🔵 Reference | **আনুমানিক সময়:** চলতে চলতে, যখন ইচ্ছা

**Overview:** বিশ্বের অভিজ্ঞ programmer-দের লেখা ৯৭টি ছোট ছোট প্রবন্ধ (essay), প্রতিটি ১–২ পৃষ্ঠা।

**কেন পড়বেন:** হালকা কিন্তু চিন্তা-জাগানো। ক্লান্ত লাগলে বা inspiration দরকার হলে একটা-দুটো পড়া যায়।

**কীভাবে পড়বেন:** ধারাবাহিক পড়ার দরকার নেই। দিনে একটা essay — চা খেতে খেতে।

**Practice:** কোনো essay ভালো লাগলে সেটির idea এক সপ্তাহ নিজের কাজে প্রয়োগ করে দেখুন।

---

<a id="design"></a>
## ক্যাটাগরি ২ — Object-Oriented Design & Architecture
[⬆️ উপরে](#toc)

> code craft শেখার পরের ধাপ — কীভাবে class, module ও পুরো system-কে সুন্দরভাবে **structure** করা যায়।

<a id="b-hfdp"></a>
### 7. Head First Design Patterns
**Level:** 🟢 Foundation | **আনুমানিক সময়:** ৩–৪ সপ্তাহ

**Overview:** ছবি, উদাহরণ আর গল্পের মাধ্যমে classic design pattern (Strategy, Observer, Decorator, Factory, Singleton ইত্যাদি) শেখায়। ভারী GoF বইয়ের তুলনায় অনেক সহজবোধ্য।

**কেন পড়বেন:** design pattern হলো বারবার আসা সমস্যার পরীক্ষিত সমাধান — এবং interview-তেও কাজে লাগে। এই বই শেখার সবচেয়ে সহজ entry point।

**কীভাবে পড়বেন:** প্রতিটি pattern পড়ে নিজের ভাষায় লিখুন: "এটি কী সমস্যা সমাধান করে?" শুধু pattern মুখস্থ নয় — **কখন ব্যবহার করতে হয় না** সেটিও বোঝা জরুরি (over-engineering এড়াতে)।

**Practice:** প্রতিটি pattern নিজের ভাষায় (Dart/Kotlin/Swift/JS) ছোট করে implement করুন। তারপর নিজের project-এ একটা জায়গা খুঁজুন যেখানে pattern-টি মানানসই।

---

<a id="b-hfooad"></a>
### 8. Head First Object-Oriented Analysis & Design
**Level:** 🟢 Foundation | **আনুমানিক সময়:** ৩ সপ্তাহ

**Overview:** requirement থেকে শুরু করে কীভাবে ভালো object-oriented design-এ পৌঁছানো যায় — encapsulation, responsibility, cohesion, coupling-এর ব্যবহারিক প্রয়োগ।

**কেন পড়বেন:** Design Patterns শেখার আগে/সাথে এটি ভিত্তি গড়ে দেয় — কেন একটা class এভাবে হলো, সেই চিন্তা শেখায়।

**কীভাবে পড়বেন:** বইয়ের case study-গুলো নিজে হাতে করুন। শুধু পড়ে গেলে কম শিখবেন; কলম-কাগজে diagram আঁকলে বেশি।

**Practice:** একটি ছোট domain (যেমন: library, food delivery) নিয়ে নিজে class design করুন — responsibility ভাগ করুন, তারপর code-এ রূপ দিন।

---

<a id="b-clean-arch"></a>
### 9. Clean Architecture — Robert C. Martin
**Level:** 🟡 Intermediate | **আনুমানিক সময়:** ২ সপ্তাহ

**Overview:** class-level থেকে জুম-আউট করে পুরো application-এর structure — dependency rule, boundary, layer, এবং business logic-কে framework/database থেকে আলাদা রাখার নীতি।

**কেন পড়বেন:** mobile-এ এটি বিশেষভাবে প্রাসঙ্গিক — feature module, state management, clean/layered architecture-এর ভিত্তি এখান থেকে আসে। senior হতে হলে এই system-level চিন্তা জরুরি।

**কীভাবে পড়বেন:** SOLID principle অংশ মন দিয়ে পড়ুন। তারপর "dependency rule" বোঝার দিকে মনোযোগ দিন — এটাই বইয়ের আসল কথা।

**Practice:** নিজের একটি app-কে layer-এ ভাগ করুন (presentation / domain / data) এবং নিশ্চিত করুন dependency শুধু ভেতরের দিকে যাচ্ছে। 📱 Flutter/RN-এ এটি সরাসরি প্রয়োগযোগ্য।

---

<a id="b-ood-interview"></a>
### 10. Object-Oriented Design Interview
**Level:** 🎯 Interview | **আনুমানিক সময়:** ২ সপ্তাহ

**Overview:** Low-Level Design (LLD) interview-এর জন্য — "design a parking lot", "design an elevator system" টাইপ প্রশ্নের structured সমাধান পদ্ধতি।

**কেন পড়বেন:** অনেক কোম্পানির interview-তে আলাদা LLD round থাকে। এই বই সেই round-এর জন্য একটি repeatable framework দেয়।

**কীভাবে পড়বেন:** শুধু সমাধান মুখস্থ নয় — প্রতিটি problem নিজে আগে চেষ্টা করুন, তারপর বইয়ের সমাধানের সাথে মিলিয়ে দেখুন কোথায় পার্থক্য।

**Practice:** সাদা কাগজে বা whiteboard-এ ২০–৩০ মিনিটে একটি LLD problem solve করার অভ্যাস করুন। জোরে বলে বলে (think aloud) practice করুন, কারণ interview-তে সেটাই করতে হবে।

---

<a id="system"></a>
## ক্যাটাগরি ৩ — System Design & Scalability
[⬆️ উপরে](#toc)

> বড় ও distributed system কীভাবে কাজ করে — senior engineer ও global interview-এর জন্য অপরিহার্য।

> ⚠️ **গুরুত্বপূর্ণ পরামর্শ:** এই category-তে অনেকগুলো overlapping বই আছে। সবগুলো গভীরভাবে পড়ার দরকার নেই। **[DDIA](#b-ddia)**-কে মূল ভিত্তি (deep read) ধরুন; বাকিগুলো interview pattern practice ও reference হিসেবে ব্যবহার করুন।

<a id="b-ddia"></a>
### 11. Designing Data-Intensive Applications (DDIA) — Martin Kleppmann
**Level:** 🔴 Advanced | **আনুমানিক সময়:** ১০–১২ সপ্তাহ (সপ্তাহে ১ অধ্যায়)

**Overview:** আধুনিক backend ও distributed system-এর ভিত্তি — database, replication, partitioning, transaction, consistency, consensus, stream processing। এই domain-এর সবচেয়ে সম্মানিত বই।

**কেন পড়বেন:** mobile engineer হলেও global interview-তে backend trade-off (caching, consistency, offline sync conflict) নিয়ে কথা বলতে হয়। এই একটি বই সেই পুরো ভিত্তি দেয়। অন্য সব system design বই যা ইঙ্গিত করে, DDIA সেটাই ব্যাখ্যা করে।

**কীভাবে পড়বেন:** তাড়াহুড়ো করবেন না — **সপ্তাহে ১ অধ্যায়**। প্রতিটি অধ্যায়ের পর নিজের ভাষায় ১ পৃষ্ঠা summary লিখুন এবং নিজের system-এর সাথে মিলিয়ে চিন্তা করুন।

**Practice:** প্রতিটি ধারণা পড়ে প্রশ্ন করুন: "আমার বর্তমান app/backend-এ এটি কীভাবে প্রযোজ্য?" diagram এঁকে নিজের একটি system design করার চেষ্টা করুন।

---

<a id="b-sdi1"></a>
### 12. System Design Interview — Volume 1 — Alex Xu
**Level:** 🎯 Interview | **আনুমানিক সময়:** ৩–৪ সপ্তাহ

**Overview:** common system design interview problem-এর step-by-step সমাধান — URL shortener, rate limiter, news feed, chat system ইত্যাদি, পরিষ্কার diagram সহ।

**কেন পড়বেন:** interview-তে কীভাবে গুছিয়ে system design করতে হয় তার একটি repeatable কাঠামো শেখায়। DDIA-র theory-কে interview format-এ প্রয়োগ করে দেখায়।

**কীভাবে পড়বেন:** প্রতিটি problem পড়ার আগে নিজে ১৫ মিনিট চেষ্টা করুন, তারপর বইয়ের সমাধানের সাথে মিলিয়ে দেখুন। শুধু পড়ে গেলে interview-তে কাজ দেবে না।

**Practice:** একটি problem নিন → requirement, scale estimate, API, data model, high-level diagram, bottleneck — এই ধাপে জোরে বলে practice করুন।

---

<a id="b-sdi2"></a>
### 13. System Design Interview — Volume 2 — Alex Xu
**Level:** 🎯 Interview | **আনুমানিক সময়:** ৩–৪ সপ্তাহ

**Overview:** Vol 1-এর ধারাবাহিকতায় আরও জটিল ও বাস্তব কেস — proximity service, nearby friends, ad click aggregation, hotel reservation, payment system ইত্যাদি।

**কেন পড়বেন:** senior/staff level interview-এর জন্য Vol 1-এর চেয়ে গভীর problem দরকার হয়। এই বই সেই gap পূরণ করে।

**কীভাবে পড়বেন:** Vol 1 শেষ করার পরই ধরুন। একই approach — আগে নিজে চেষ্টা, পরে মিলিয়ে দেখা।

**Practice:** এক একটি problem-এর জন্য নিজের সমাধান একটি doc-এ লিখুন, যেন interview-তে বলার সময় কাঠামো মাথায় থাকে।

---

<a id="b-bigarchive"></a>
### 14. System Design: The Big Archive
**Level:** 🔵 Reference | **আনুমানিক সময়:** reference, ধারাবাহিক নয়

**Overview:** বিভিন্ন system design কেস ও concept-এর একটি বড় সংকলন — একসাথে অনেক উদাহরণ ও pattern।

**কেন পড়বেন:** বিস্তৃত reference হিসেবে ভালো — কোনো নির্দিষ্ট pattern বা কেস খুঁজতে কাজে দেয়।

**কীভাবে পড়বেন:** শুরু-থেকে-শেষ পড়বেন না (DDIA + SDI Vol 1/2 এর সাথে অনেক overlap)। নির্দিষ্ট topic দরকার হলে সেই অংশ দেখুন।

**Practice:** আলাদা practice নয়; অন্য বই পড়ার সময় কোনো concept আরও উদাহরণ দরকার হলে এখানে খুঁজুন।

---

<a id="b-msdi"></a>
### 15. Mobile System Design Interview 📱
**Level:** 🎯📱 Interview | **আনুমানিক সময়:** ৩ সপ্তাহ

**Overview:** mobile-নির্দিষ্ট system design — offline-first, sync, caching, image pipeline, chat, news feed client-side architecture, pagination, real-time update ইত্যাদি।

**কেন পড়বেন:** Uber, Meta, Booking-সহ অনেক কোম্পানির mobile interview-তে আলাদা mobile system design round থাকে। backend system design (DDIA/SDI) এই অংশ cover করে না — এটি mobile engineer-এর আসল পার্থক্যকারী।

**কীভাবে পড়বেন:** প্রতিটি কেসে client ও server-এর দায়িত্ব আলাদা করে বুঝুন। নিজের পরিচিত app (chat, feed) কীভাবে design করা যায় ভাবুন।

**Practice:** "Design the offline mode of a note-taking app" বা "Design an image-heavy feed" — এমন prompt নিয়ে নিজে whiteboard practice করুন।

---

<a id="dsa"></a>
## ক্যাটাগরি ৪ — Data Structures, Algorithms & Coding Interview
[⬆️ উপরে](#toc)

> coding interview-এর মেরুদণ্ড। মনে রাখবেন — এই category-তে বই পড়ার চেয়ে **problem solve করা (practice)** অনেক বেশি গুরুত্বপূর্ণ।

<a id="b-ctci"></a>
### 16. Cracking the Coding Interview — Gayle L. McDowell
**Level:** 🎯 Interview | **আনুমানিক সময়:** ২–৩ মাস (practice সহ)

**Overview:** DSA topic-wise ব্যাখ্যা + ১৮৯টি interview problem ও সমাধান, এবং interview process/behavioral নিয়ে পরামর্শ। coding interview-র "gold standard"।

**কেন পড়বেন:** এক জায়গায় DSA, problem এবং interview কৌশল — সব। remote/global চাকরির আগে এটি অপরিহার্য।

**কীভাবে পড়বেন:** topic ধরে এগোন। প্রতিটি problem আগে নিজে চেষ্টা করুন (অন্তত ২০–৩০ মিনিট), তারপর সমাধান দেখুন। behavioral অধ্যায়গুলোও পড়ুন — অনেকে এগুলো skip করে ভুল করে।

**Practice:** বই + LeetCode একসাথে চালান। সপ্তাহে নির্দিষ্ট সংখ্যক problem, এবং **জোরে বলে** সমাধান ব্যাখ্যা করার অভ্যাস করুন (mock interview)।

---

<a id="b-contest-bn"></a>
### 17. Programming Contest & Data Structure Algorithm (বাংলা) — Dimik
**Level:** 🟢 Foundation | **আনুমানিক সময়:** ~২ মাস (practice সহ)

**Overview:** বাংলায় DSA ও programming contest-এর মূল ভিত্তি — array, linked list, stack/queue, tree, graph, sorting, searching ইত্যাদি।

**কেন পড়বেন:** মাতৃভাষায় পড়লে DSA-র গাণিতিক অংশ ও যুক্তি অনেক সহজে গভীরভাবে বোঝা যায়। ভিত্তি দুর্বল হলে এটি দিয়ে শুরু করুন।

**কীভাবে পড়বেন:** শুধু পড়া নয় — প্রতিটি data structure নিজে হাতে implement করুন। তত্ত্ব বোঝার পর English resource (CTCI/LeetCode)-এ যেতে সহজ হবে।

**Practice:** প্রতিটি অধ্যায়ের সাথে সংশ্লিষ্ট problem solve করুন (online judge-এ)।

---

<a id="b-52-bn"></a>
### 18. 52 Programming Problems & Solutions (বাংলা) — Dimik
**Level:** 🟢 Foundation | **আনুমানিক সময়:** drill, ধারাবাহিক

**Overview:** বাছাই করা ৫২টি programming problem ও তাদের সমাধান — হাতে-কলমে অনুশীলনের জন্য।

**কেন পড়বেন:** তত্ত্ব শেখার পর problem-solving-এর অভ্যাস গড়তে সাহায্য করে। এটি পড়ার বই নয়, **practice-এর fuel**।

**কীভাবে পড়বেন:** প্রতিটি problem আগে নিজে সমাধানের চেষ্টা করুন, তারপর বইয়ের সমাধান দেখুন — কোথায় ভালো করা যেত তা বিশ্লেষণ করুন।

**Practice:** এটিই practice — সপ্তাহে কয়েকটি problem নিজে solve করে মিলিয়ে দেখুন।

---

<a id="mobile"></a>
## ক্যাটাগরি ৫ — Mobile Engineering 📱
[⬆️ উপরে](#toc)

> mobile-নির্দিষ্ট গভীর জ্ঞান — যা একজন general engineer থেকে একজন দক্ষ mobile engineer-কে আলাদা করে।

<a id="b-bmaas"></a>
### 19. Building Mobile Apps at Scale — Gergely Orosz 📱
**Level:** 🔴📱 Advanced | **আনুমানিক সময়:** ২ সপ্তাহ

**Overview:** বড় স্কেলে mobile engineering-এর চ্যালেঞ্জ — release train, feature flag, A/B testing, crash-free rate, build infrastructure, modularization, app size, platform team ইত্যাদি।

**কেন পড়বেন:** এটিই একমাত্র গুরুত্বপূর্ণ বই যা mobile engineering-কে একটি serious discipline হিসেবে দেখে। interview-তে এই জ্ঞান আপনাকে একজন পরিণত mobile engineer হিসেবে আলাদা করবে।

**কীভাবে পড়বেন:** প্রতিটি চ্যালেঞ্জ পড়ে ভাবুন আপনার বর্তমান app/team-এ এটি কীভাবে handle হয় (বা হয় না)। এটি সরাসরি কাজে প্রয়োগ করার মতো বই।

**Practice:** নিজের team-এর একটি দুর্বল জায়গা (যেমন CI/CD বা crash monitoring) বেছে নিন এবং উন্নতির একটি প্রস্তাব লিখুন — এটি tech lead-সুলভ কাজ।

---

<a id="career"></a>
## ক্যাটাগরি ৬ — Career, Leadership & Process
[⬆️ উপরে](#toc)

> senior থেকে **tech lead** হওয়ার পথ — technical skill-এর পাশাপাশি যা দরকার।

<a id="b-guidebook"></a>
### 20. The Software Engineer's Guidebook — Gergely Orosz
**Level:** 🔴 Advanced | **আনুমানিক সময়:** ৩ সপ্তাহ

**Overview:** junior থেকে senior/staff/tech lead পর্যন্ত career-এর প্রতিটি ধাপে কী প্রত্যাশিত, কীভাবে scope ও influence বাড়াতে হয়, এবং promotion কীভাবে আসে — শত শত engineer-এর অভিজ্ঞতা থেকে লেখা।

**কেন পড়বেন:** tech lead হতে চাইলে এটিই সবচেয়ে সরাসরি প্রাসঙ্গিক বই। কোন আচরণ ও কাজ আপনাকে পরবর্তী level-এ নিয়ে যাবে, তা স্পষ্ট করে দেয়।

**কীভাবে পড়বেন:** active reading — প্রতিটি অধ্যায়ের পর একটি **action** লিখুন: "এ সপ্তাহে আমি কী আলাদাভাবে করব?" (নিচের [Reading Strategy](#reading-strategy) দেখুন)।

**Practice:** কাজের জায়গায় একটি domain বেছে সেটির ownership নিন, design doc লিখুন, junior-দের mentor করুন — বইয়ের পরামর্শ বাস্তবে প্রয়োগ করুন।

---

<a id="b-swe-google"></a>
### 21. Software Engineering at Google — Winters, Manshreck, Wright
**Level:** 🔴 Advanced | **আনুমানিক সময়:** ৬–৮ সপ্তাহ (বেছে বেছে)

**Overview:** বিশাল স্কেলে engineering culture ও practice — code review, testing philosophy, documentation, dependency management, large-scale change ইত্যাদি। "programming আর software engineering-এর পার্থক্য হলো সময়।"

**কেন পড়বেন:** একজন tech lead-কে শুধু code নয়, team-এর engineering practice নিয়েও ভাবতে হয়। এই বই সেই সংস্কৃতিগত দিকটি শেখায়।

**কীভাবে পড়বেন:** পুরোটা না পড়ে আপনার কাজের সাথে প্রাসঙ্গিক অধ্যায় বেছে নিন (testing, code review, documentation, culture)। কিছু low-level tooling অধ্যায় mobile-এর জন্য কম প্রাসঙ্গিক — skip করতে পারেন।

**Practice:** আপনার team-এ একটি practice উন্নত করুন — যেমন একটি code review guideline বা testing standard প্রস্তাব করুন।

---

<a id="b-user-stories"></a>
### 22. User Stories Applied — Mike Cohn
**Level:** 🟡 Intermediate | **আনুমানিক সময়:** ২ সপ্তাহ

**Overview:** agile development-এ user story লেখা, requirement ভাঙা, estimation ও planning — product/business-এর চাহিদাকে engineering কাজে রূপান্তর করা।

**কেন পড়বেন:** tech lead-কে product ও team-এর মাঝে সেতু হতে হয়। কাজ ভালোভাবে ভাঙা, estimate করা ও planning করা leadership-এর গুরুত্বপূর্ণ দক্ষতা।

**কীভাবে পড়বেন:** নিজের চলমান project-এর সাথে মিলিয়ে পড়ুন — আপনার team এখন কীভাবে requirement handle করে, আর কীভাবে উন্নত করা যায়।

**Practice:** একটি বড় feature নিয়ে সেটিকে ছোট, স্বাধীন user story-তে ভাঙার অনুশীলন করুন।

---

<a id="adjacent"></a>
## ক্যাটাগরি ৭ — Adjacent / Optional
[⬆️ উপরে](#toc)

> মূল roadmap-এর বাইরে — আগ্রহ থাকলে আলাদা track হিসেবে।

<a id="b-ml-bn"></a>
### 23. Machine Learning Algorithm (বাংলা)
**Level:** 🔵 Optional | **আনুমানিক সময়:** আলাদা track

**Overview:** বাংলায় মৌলিক machine learning algorithm-এর পরিচিতি ও ব্যাখ্যা।

**কেন পড়বেন:** core software/mobile engineering বা tech lead path-এর জন্য জরুরি নয়। কিন্তু ML-এ আগ্রহ থাকলে বা ভবিষ্যতে AI-সংশ্লিষ্ট কাজে যেতে চাইলে এটি একটি ভালো বাংলা সূচনা।

**কীভাবে পড়বেন:** মূল roadmap-এর সাথে মেশাবেন না — আলাদা সময়ে, আগ্রহের বিষয় হিসেবে পড়ুন।

**Practice:** প্রতিটি algorithm ছোট dataset-এ (Python-এ) চালিয়ে দেখুন।

---

<a id="roadmap"></a>
## 📅 11. ধাপে ধাপে রিডিং প্ল্যান (কোথা থেকে শুরু, কোথায় শেষ)
[⬆️ উপরে](#toc)

> নিচের roadmap-টি general — junior থেকে tech lead পর্যন্ত। আপনি যেই level-এ আছেন, সেখান থেকে শুরু করতে পারেন। প্রতিটি phase-এর শেষে 📱 দিয়ে mobile engineer-দের জন্য বিশেষ পরামর্শ আছে।

### 🟢 Phase 0 — ভিত্তি / Foundation (যদি DSA বা basics দুর্বল হয়)
**লক্ষ্য:** শক্ত ভিত্তি তৈরি।
1. [Programming Contest & DS/Algo (বাংলা)](#b-contest-bn) — DSA ভিত্তি
2. [52 Programming Problems (বাংলা)](#b-52-bn) — সমান্তরালে practice
3. [The Pragmatic Programmer](#b-pragmatic) — পেশাদার mindset

> ✅ ভিত্তি শক্ত থাকলে এই phase দ্রুত পার করুন বা skip করুন।

### 🟡 Phase 1 — Code Craft (পরিষ্কার code লেখা)
**লক্ষ্য:** maintainable, পড়ার-যোগ্য code।
1. [Clean Code](#b-clean-code)
2. [Refactoring](#b-refactoring)
3. [A Philosophy of Software Design](#b-aposd) — Clean Code-এর ভারসাম্য হিসেবে
4. [97 Things](#b-97things) — হালকাভাবে, সমান্তরালে
5. [Code Complete 2](#b-code-complete) — reference হিসেবে রাখুন

### 🟡 Phase 2 — Design & Architecture
**লক্ষ্য:** class ও system-কে সুন্দরভাবে structure করা।
1. [Head First OOA&D](#b-hfooad)
2. [Head First Design Patterns](#b-hfdp)
3. [Clean Architecture](#b-clean-arch)

> 📱 **Mobile track:** এই phase-এর সাথে [Building Mobile Apps at Scale](#b-bmaas) পড়ুন — Clean Architecture-এর ধারণা সরাসরি mobile app structure-এ প্রয়োগ করুন।

### 🔴 Phase 3 — System Design (senior চিন্তা)
**লক্ষ্য:** বড় ও distributed system বোঝা।
1. [Designing Data-Intensive Applications](#b-ddia) — **মূল ভিত্তি, সপ্তাহে ১ অধ্যায়**
2. [System Design Interview — Vol 1](#b-sdi1)
3. [System Design Interview — Vol 2](#b-sdi2)
4. [The Big Archive](#b-bigarchive) — reference

> 📱 **Mobile track:** [Mobile System Design Interview](#b-msdi) এই phase-এ যোগ করুন — এটিই mobile engineer-এর system design পার্থক্যকারী।

### 🔴 Phase 4 — Leadership / Tech Lead
**লক্ষ্য:** senior থেকে tech lead-এ উত্তরণ।
1. [The Software Engineer's Guidebook](#b-guidebook) — **এই phase-এর সবচেয়ে গুরুত্বপূর্ণ বই**
2. [Software Engineering at Google](#b-swe-google) — বেছে বেছে
3. [User Stories Applied](#b-user-stories)

> 💡 এই phase-এ বই পড়ার পাশাপাশি কাজের জায়গায় tech-lead-সুলভ কাজ শুরু করুন: একটি domain-এর ownership, design doc লেখা, mentoring।

### 🎯 Phase 5 — Interview Sprint (চাকরি খোঁজার ২–৪ মাস আগে)
**লক্ষ্য:** interview-এর ঠিক আগে peak করা (আগে পড়লে ভুলে যাবেন)।
1. [Cracking the Coding Interview](#b-ctci) + LeetCode practice
2. [Object-Oriented Design Interview](#b-ood-interview) — LLD round
3. [System Design Interview Vol 1 & 2](#b-sdi1) — পুনরায় ঝালাই
4. 📱 [Mobile System Design Interview](#b-msdi) — পুনরায় ঝালাই
5. mock interview + জোরে বলে practice

### 🔵 Optional track (যেকোনো সময়)
- [Machine Learning Algorithm (বাংলা)](#b-ml-bn) — আগ্রহ থাকলে আলাদাভাবে।

---

### 🗺️ সংক্ষেপে: কোথা থেকে শুরু, কোথায় শেষ

```
শুরু → Phase 0 (ভিত্তি)
      → Phase 1 (Clean Code, craft)
      → Phase 2 (Design + 📱 Mobile at Scale)
      → Phase 3 (DDIA + System Design + 📱 Mobile SD)
      → Phase 4 (Tech Lead বই + বাস্তব leadership কাজ)
শেষ → Phase 5 (Interview sprint, চাকরির ঠিক আগে)
```

> ⏱️ **বাস্তব গতি:** চাকরি করতে করতে একজন engineer বছরে ~৬–৮টি serious বই শেষ করতে পারেন (DDIA একাই প্রায় ৩ মাস)। তাই তাড়াহুড়ো নয় — ক্রম ঠিক রেখে নিয়মিত পড়াই আসল।

---

<a id="reading-strategy"></a>
## 🧠 12. কীভাবে প্রতিটি বই পড়বেন (Reading Strategy)
[⬆️ উপরে](#toc)

### মূল নীতি: passive পড়া নয়, active পড়া
শুধু পড়ে গেলে ৭ দিনে ৮০% ভুলে যাবেন। তাই প্রতিটি বই **active** ভাবে পড়ুন।

### ৪-স্তরের নোট পদ্ধতি (প্রতিটি অধ্যায়ের জন্য)
প্রতিটি অধ্যায় শেষে ছোট করে লিখুন (১ পৃষ্ঠাই যথেষ্ট):

| স্তর | কী লিখবেন |
|---|---|
| **1. Insight** | মূল ধারণা — **নিজের ভাষায়** (বইয়ের লাইন copy নয়) |
| **2. Evidence** | কেন এটি সত্য — উদাহরণ বা যুক্তি |
| **3. My situation** | আমার কাজ/project/team-এর সাথে কীভাবে মেলে |
| **4. Action** | আগামী ১–২ সপ্তাহে আমি কী **করব** |

> যদি "Action" লিখতে না পারেন, তাহলে সেটি নোট নয় — শুধু highlight। **Action ছাড়া পড়া মানে বিনোদন, শেখা নয়।**

### পড়ার সময় বনাম পড়ার পরে
- **পড়ার সময়:** শুধু দাগ দিন বা margin-এ ২–৩ শব্দ লিখুন ("এটা আমি", "team-এ try করব")। থেমে বড় নোট লিখবেন না — পড়া চালিয়ে যান।
- **অধ্যায় শেষে (১০–২০ মিনিট):** বই বন্ধ করে স্মৃতি থেকে যা মনে আছে লিখুন (active recall), তারপর highlight মিলিয়ে পূরণ করুন। এই পদ্ধতি retention তিন গুণ বাড়ায়।

### সাপ্তাহিক ও মাসিক অভ্যাস
- **প্রতি সপ্তাহে:** এই সপ্তাহের "Action"-গুলো করেছেন কিনা মিলিয়ে দেখুন।
- **প্রতি মাসে:** মাসের সব "Insight" আবার পড়ুন; সেরা ৩টি বেছে চোখের সামনে রাখুন।

### বইভেদে কৌশল
- **Craft/Design বই (Clean Code, Refactoring, Patterns):** পড়ে সাথে সাথে নিজের code-এ প্রয়োগ করুন।
- **System Design বই (DDIA, SDI):** diagram আঁকুন; "আমার system হলে কীভাবে করতাম" ভাবুন।
- **Career বই (Guidebook, SWE@Google):** প্রতিটি ধারণাকে কাজের জায়গায় একটি concrete action-এ রূপ দিন।
- **Interview বই (CTCI, OOD, Mobile SD):** আগে নিজে solve, পরে সমাধান মিলিয়ে দেখা — এবং **জোরে বলে** practice।
- **Reference বই (Code Complete, Big Archive):** শুরু-থেকে-শেষ নয়; দরকারে খুঁজে পড়ুন।

---

<a id="practice"></a>
## 🏋️ 13. Practice Strategy — পড়া কীভাবে skill-এ রূপান্তর করবেন
[⬆️ উপরে](#toc)

বই হলো ইনপুট; skill তৈরি হয় আউটপুট থেকে। নিচের practice-গুলো বইয়ের সাথে চালান:

### ১. Coding / DSA practice
- বই + **LeetCode** একসাথে। সপ্তাহে নির্দিষ্ট সংখ্যক problem ঠিক করুন এবং ধরে রাখুন।
- প্রতিটি problem-এর পর জিজ্ঞাসা করুন: "আরও ভালো সমাধান কী হতে পারত?"
- **জোরে বলে (think aloud)** solve করুন — interview-তে এটাই করতে হয়।

### ২. Design / Architecture practice
- পড়া pattern/principle নিজের project-এ একটি জায়গায় প্রয়োগ করুন।
- ছোট ছোট LLD problem (parking lot, elevator) whiteboard-এ ২০ মিনিটে solve করার অভ্যাস।

### ৩. System Design practice
- প্রতিটি কেস: requirement → scale estimate → API → data model → diagram → bottleneck — এই ধাপে বলে বলে practice।
- 📱 mobile হলে client বনাম server দায়িত্ব আলাদা করে ভাবুন (offline, sync, cache)।

### ৪. বাস্তব কাজে (Tech Lead-এর জন্য সবচেয়ে গুরুত্বপূর্ণ)
- একটি **domain-এর ownership** নিন — সেটিকে "আমার" বানান।
- **Design doc / RFC** লিখুন — ভালো লেখা tech lead-এর প্রধান দক্ষতা।
- junior-দের **mentor** করুন; ভালো code review দিন (শুধু "LGTM" নয়)।
- নিজের শেখা কোনো বিষয় team-এ **উপস্থাপন** করুন (brown-bag session) — শেখানোই সবচেয়ে গভীর শেখা, এবং এটি visibility বাড়ায়।

### ৫. Mock interview
- Interview phase-এ নিয়মিত mock দিন (বন্ধু/online platform)। নিজের ব্যাখ্যা record করে শুনুন।

> 🎯 **মনে রাখুন:** tech lead হওয়া, mobile-এ গভীর হওয়া, আর interview পাস করা — তিনটির কোনোটিই শুধু বই পড়ে হয় না। বই দিকনির্দেশনা দেয়; দক্ষতা আসে প্রয়োগ থেকে।

---

<a id="quick-reference"></a>
## ⚡ 14. Quick Reference — পড়ার ক্রম এক নজরে
[⬆️ উপরে](#toc)

| ক্রম | Phase | বই | Level |
|---|---|---|---|
| 1 | Foundation | Programming Contest & DS/Algo (বাংলা) | 🟢 |
| 2 | Foundation | 52 Programming Problems (বাংলা) | 🟢 |
| 3 | Foundation | The Pragmatic Programmer | 🟢 |
| 4 | Craft | Clean Code | 🟢 |
| 5 | Craft | Refactoring | 🟡 |
| 6 | Craft | A Philosophy of Software Design | 🟡 |
| 7 | Craft | 97 Things (সমান্তরালে) | 🔵 |
| — | Craft | Code Complete 2 (reference) | 🔵 |
| 8 | Design | Head First OOA&D | 🟢 |
| 9 | Design | Head First Design Patterns | 🟢 |
| 10 | Design | Clean Architecture | 🟡 |
| 11 | Design 📱 | Building Mobile Apps at Scale | 🔴📱 |
| 12 | System | Designing Data-Intensive Applications | 🔴 |
| 13 | System | System Design Interview Vol 1 | 🎯 |
| 14 | System | System Design Interview Vol 2 | 🎯 |
| 15 | System 📱 | Mobile System Design Interview | 🎯📱 |
| — | System | The Big Archive (reference) | 🔵 |
| 16 | Leadership | The Software Engineer's Guidebook | 🔴 |
| 17 | Leadership | Software Engineering at Google | 🔴 |
| 18 | Leadership | User Stories Applied | 🟡 |
| 19 | Interview | Cracking the Coding Interview | 🎯 |
| 20 | Interview | Object-Oriented Design Interview | 🎯 |
| — | Optional | Machine Learning Algorithm (বাংলা) | 🔵 |

---

> 🌟 **শেষ কথা:** এই roadmap একটি ম্যারাথন, sprint নয়। একসাথে অনেক বই কেনা বা পড়ার চাপ নেবেন না। একটি বই নিন, active ভাবে পড়ুন, প্রয়োগ করুন — তারপর পরেরটি। ধারাবাহিকতাই (consistency) আসল চাবিকাঠি।

*Happy reading & keep building! 🚀*
