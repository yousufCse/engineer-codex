# Section 13 — Software Architecture Patterns

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **Bangladesh (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা সহ**, আর **link করা** — যাতে আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারেন।
> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-13-architecture-patterns-bn.md](../software-engineer-flutter/section-13-architecture-patterns.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব জীবনের উদাহরণ, diagram আর code সহ ধাপে ধাপে বিস্তারিত ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** Architecture-এর ক্ষেত্রে layer-গুলো এঁকে দেখান (শুধু কথায় হলেও) আর **dependency-র দিক** ব্যাখ্যা করুন। Senior interview জেতা যায় *কেন* একটা structure আছে সেটা বুঝিয়ে, শুধু নাম বলে নয়।

---


## <a id="toc"></a>সূচিপত্র

**A. Layer আর separation**
1. [Layered Architecture](#q1) · *Very common*
2. [Clean Architecture — ৩টি layer আর dependency rule](#q2) · *Very common*
3. [Separation of Concerns](#q3) · *Very common*

**B. UI architecture pattern (MVx)**
4. [MVC — Model-View-Controller](#q4) · *Common*
5. [MVVM — আর BLoC/Cubit কীভাবে এর সাথে মেলে](#q5) · *Very common*
6. [MVP — আর MVVM থেকে এর পার্থক্য](#q6) · *Common*

**C. মূল building block**
7. [Repository Pattern](#q7) · *Very common*
8. [Use Case / Interactor](#q8) · *Common*
9. [Dependency Injection (`get_it`)](#q9) · *Very common*
10. [Service Locator বনাম Dependency Injection](#q10) · *Common*
11. [Event-driven architecture আর BLoC](#q11) · *Common*

**D. Scale করা আর বেছে নেওয়া**
12. [Monorepo বনাম Multi-repo](#q12) · *Common*
13. [Modular architecture (feature package)](#q13) · *Common*
14. [Architecture কীভাবে বেছে নেবেন](#q14) · *Very common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের review)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

এই পর্যায়গুলো ক্রম অনুযায়ী শেষ করুন। একটা পর্যায় তখনই টিক দিন যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন আর layer-গুলো আঁকতে পারবেন।

**পর্যায় ১ — ভিত্তি (এখান থেকে শুরু করুন)।**
→ [Q1 Layered](#q1) · [Q2 Clean Architecture](#q2) · [Q3 Separation of concerns](#q3)

**পর্যায় ২ — যে UI pattern interviewer-রা পছন্দ করেন।**
→ [Q5 MVVM](#q5) · [Q4 MVC](#q4) · [Q6 MVP](#q6)

**পর্যায় ৩ — মূল building block-গুলো।**
→ [Q7 Repository](#q7) · [Q9 Dependency injection](#q9) · [Q8 Use case](#q8) · [Q11 Event-driven](#q11)

**পর্যায় ৪ — Trade-off আর scale।**
→ [Q10 Service locator বনাম DI](#q10) · [Q12 Monorepo](#q12) · [Q13 Modular](#q13) · [Q14 বেছে নেওয়া](#q14)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** এই ছয়টা দেখে নিন:
[Q1](#q1) · [Q2](#q2) · [Q5](#q5) · [Q7](#q7) · [Q9](#q9) · [Q14](#q14), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Layer আর separation

---

## <a id="q1"></a>1. Layered Architecture কী, আর একটা mobile app-এ সাধারণত কোন কোন layer থাকে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Layered architecture app-কে কয়েকটা আনুভূমিক layer-এ ভাগ করে। প্রতিটা layer-এর একটাই কাজ। আর একটা layer শুধু তার ঠিক নিচের layer-এর সাথে কথা বলে। Mobile app-এ layer-গুলো সাধারণত হয় Presentation (UI), Domain/Application (business logic), আর Data (API, database)। এতে দায়িত্ব আলাদা থাকে। ফলে প্রতিটা layer আলাদাভাবে বদলানো আর test করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা বিল্ডিংয়ের তলা।**
একটা বিল্ডিংয়ে অনেক তলা থাকে। প্রতিটা তলা নিজের কাজ করে। আর ঠিক নিচের তলার সাথে যুক্ত হয় নির্দিষ্ট সিঁড়ি দিয়ে — যেখানে-সেখানে ফুটো করে নয়। Layer-ও ঠিক এভাবেই কাজ করে।

**ধাপ ২ — সাধারণ layer-গুলো।**

```
+----------------------------------+
|       Presentation Layer         |  UI: widgets, screens, state management
+----------------------------------+
|     Domain / Application Layer   |  business rules, use cases
+----------------------------------+
|           Data Layer             |  APIs, database, cache
+----------------------------------+
```

নিয়মটা হলো: উপরের layer নিচের layer-এর উপর নির্ভর করে, উল্টোটা কখনোই না। UI business logic-কে call করে, business logic data-কে call করে — উল্টোদিকে নয়।

**ধাপ ৩ — কেন layer-এ ভাগ করা হয়।**
- **Separation** — UI code আর database code মিশে যায় না।
- **Testability** — UI ছাড়াই business logic test করা যায়।
- **Replaceability** — data source বদলে ফেলা যায় (REST → GraphQL), UI-তে হাত না দিয়েই।

**ধাপ ৪ — flow-এর ছোট একটা উদাহরণ।**
একটা button tap (Presentation) → একটা use case call করে (Domain) → সেটা একটা repository-কে জিজ্ঞেস করে (Data) → উত্তর layer-গুলো দিয়ে উপরে ফিরে এসে UI update করে।

**Interviewer কেন জিজ্ঞেস করে:** এটাই Clean Architecture আর বেশিরভাগ app structure-এর ভিত্তি ধারণা। তাঁরা দেখতে চান আপনি UI, logic আর data আলাদা রাখেন কি না।

**সাধারণ ভুল:** UI-কে সরাসরি database বা API-র সাথে কথা বলতে দেওয়া (layer টপকে যাওয়া)। এতে সবকিছু জট পাকিয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা Clean Architecture থেকে কীভাবে আলাদা?"* → Clean Architecture আরও কড়া একটা layered design, যার একটা নির্দিষ্ট dependency rule আছে ([Q2](#q2))।

**সম্পর্কিত:** [Q2 — Clean Architecture](#q2) · [Q3 — separation of concerns](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Flutter-এ Clean Architecture ব্যাখ্যা করুন — ৩টি layer আর dependency rule।

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Clean Architecture app-কে Presentation, Domain আর Data layer-এ ভাগ করে। একটাই কড়া নিয়ম: dependency ভেতরের দিকে, Domain-এর দিকে point করে। Domain হলো কেন্দ্র — খাঁটি business logic, কোনো Flutter বা package import নেই। Presentation আর Data দুটোই Domain-এর উপর নির্ভর করে, কিন্তু Domain কোনো কিছুর উপর নির্ভর করে না। এতে মূল logic স্থিতিশীল থাকে আর সহজে test করা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: পেঁয়াজ, যার কেন্দ্রে নিয়মগুলো।**
সবচেয়ে গুরুত্বপূর্ণ আর সবচেয়ে স্থিতিশীল জিনিস (আপনার business rule) বসে কেন্দ্রে। বাইরের layer (UI, database) প্রায়ই বদলায়। কিন্তু তারা কেন্দ্রকে বদলাতে বাধ্য করতে পারে না। সবকিছু ভেতরের দিকে point করে।

**ধাপ ২ — তিনটি layer।**

```
        +-------------------------+
        |   Presentation (UI)     |  widgets, BLoC/Cubit  ─┐
        +-------------------------+                         │ depend on
        |        Domain           |  entities, use cases,   │ (inward)
        |     (the center)        |  repository interfaces ←┘
        +-------------------------+                         │
        |         Data            |  repository impls,      │ depend on
        |                         |  API, database         ─┘ (inward)
        +-------------------------+
```

- **Domain** — entity, use case, আর repository *interface*। খাঁটি Dart, Flutter নেই, package নেই।
- **Data** — বাস্তব repository *implementation*, API client, database, model (`fromJson`)।
- **Presentation** — widget আর state management (BLoC, Riverpod)।

**ধাপ ৩ — dependency rule: ভেতরের দিকে point করুন।**
মূল কৌশলটা হলো — Domain একটা repository *interface* ঠিক করে দেয়, আর Data layer সেটা *implement* করে। ফলে Domain কখনোই Data layer import করে না। সে শুধু interface-টা চেনে।

```dart
// DOMAIN layer — খাঁটি, Flutter নেই, API code নেই
abstract class UserRepository {        // interface থাকে Domain-এ
  Future<User> getUser(String id);
}

class GetUser {                        // একটা use case
  final UserRepository repo;
  GetUser(this.repo);
  Future<User> call(String id) => repo.getUser(id);
}

// DATA layer — Domain-এর interface implement করে (ভেতরের দিকে point করে)
class UserRepositoryImpl implements UserRepository {
  final ApiClient api;
  UserRepositoryImpl(this.api);
  @override
  Future<User> getUser(String id) async => /* call api, map to User */ User(id);
}
```

**ধাপ ৪ — Domain কেন Data বা Presentation-এর উপর নির্ভর করতে পারে না।**
Domain হলো আপনার business rule — সবচেয়ে মূল্যবান আর সবচেয়ে দীর্ঘজীবী code। এটা যদি Flutter বা কোনো নির্দিষ্ট database-এর উপর নির্ভর করত, তাহলে প্রতিটা UI বা database পরিবর্তন এটাকে ভেঙে দিতে পারত। খাঁটি রাখলে আপনি সাধারণ Dart দিয়েই এটা test করতে পারবেন। আর যেকোনো জায়গায় আবার ব্যবহার করতে পারবেন।

**ধাপ ৫ — Trade-off।**
Clean Architecture boilerplate বাড়ায় (interface, use case, model বনাম entity)। বড় আর দীর্ঘদিন চলা app-এ এটা দারুণ কাজ করে। কিন্তু ছোট app-এ এটা বাড়াবাড়ি হয়ে যেতে পারে ([Q14](#q14))।

**Interviewer কেন জিজ্ঞেস করে:** এটাই Flutter-এর আদর্শ "সিরিয়াস" architecture। তাঁরা শুনতে চান *dependency rule* (ভেতরের দিকে) আর Domain কেন খাঁটি থাকে, তার *কারণ*।

**সাধারণ ভুল:** Domain layer-এ Flutter বা API/database code import করা — এতে পুরো উদ্দেশ্যটাই নষ্ট হয়ে যায়। আরেকটা ভুল — খুব সাধারণ একটা app-এ এটা প্রয়োগ করা, যেখানে এটা শুধুই বাড়তি বোঝা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Entity বনাম Model?"* → Entity = খাঁটি Domain object। Model = Data layer-এর object, যার `fromJson`/`toJson` আছে আর যেটা entity-তে/থেকে map করে।
- *"Use case কোথায় থাকে?"* → Domain layer-এ ([Q8](#q8))।

**সম্পর্কিত:** [Q1 — layered](#q1) · [Q7 — repository](#q7) · [Q8 — use case](#q8) · [Q14 — বেছে নেওয়া](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. "Separation of Concerns" কী? Flutter-এ একটা violation আর তার সমাধানের উদাহরণ দিন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Separation of concerns মানে code-এর প্রতিটা অংশ একটা concern সামলায় — UI, business logic, বা data — আর এগুলো মেশে না। একটা সাধারণ violation হলো widget-এর `build` method-এর ভেতরেই network call করা আর JSON parse করা। সমাধান হলো ওই কাজটা repository-তে সরিয়ে নেওয়া, আর widget-কে শুধু UI দেখানোর কাজে রাখা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ধারণাটা।**
একটা "concern" মানে একটা দায়িত্ব: UI আঁকা, business rule ঠিক করা, বা data আনা। এগুলো মিশিয়ে ফেললে code পড়া, test করা আর বদলানো কঠিন হয়ে যায়।

**ধাপ ২ — একটা violation: সবকিছু widget-এর ভেতরে।**

```dart
// খারাপ: widget fetch করছে, parse করছে, AND দেখাচ্ছে — তিনটা concern মেশানো
class UserScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: http.get(Uri.parse('https://api/user')), // UI-তে networking
      builder: (context, snapshot) {
        final json = jsonDecode(snapshot.data!.body);   // UI-তে parsing
        return Text(json['name']);                       // display
      },
    );
  }
}
```

আসল network ছাড়া এটা test করা অসম্ভব। আর UI data logic-এর সাথে জট পাকিয়ে গেছে।

**ধাপ ৩ — সমাধান: প্রতিটা concern তার নিজের জায়গায়।**

```dart
// Data concern — একটা repository
class UserRepository {
  final ApiClient api;
  UserRepository(this.api);
  Future<User> getUser() async => User.fromJson(await api.get('/user'));
}

// Logic/state concern — একটা Cubit
class UserCubit extends Cubit<UserState> {
  final UserRepository repo;
  UserCubit(this.repo) : super(UserLoading());
  Future<void> load() async => emit(UserLoaded(await repo.getUser()));
}

// UI concern — শুধু দেখায়
class UserScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) =>
      BlocBuilder<UserCubit, UserState>(builder: (c, s) => /* show s */ Text('...'));
}
```

**ধাপ ৪ — কেন এটা গুরুত্বপূর্ণ।**
এখন data layer আলাদাভাবে testable, logic আলাদাভাবে testable, আর UI শুধু render করে। এক concern-এ পরিবর্তন এলে সেটা অন্যগুলোতে ছড়ায় না।

**Interviewer কেন জিজ্ঞেস করে:** এটা প্রতিটা architecture pattern-এর বাস্তব প্রাণ। তাঁরা দেখতে চান আপনি UI-কে networking/parsing মুক্ত রাখেন কি না।

**সাধারণ ভুল:** widget-এর ভেতরে business logic আর network call রাখা। এতে widget untestable আর ভারী হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটার সাথে SRP-র সম্পর্ক কী?"* → Separation of concerns হলো পুরো app জুড়ে প্রয়োগ করা SRP, শুধু একটা class-এ নয়।

**সম্পর্কিত:** [Q1 — layered](#q1) · [Q2 — Clean Architecture](#q2) · [Q7 — repository](#q7)

[↑ উপরে ফিরুন](#toc)

---

# B. UI architecture patterns (MVx)

---

## <a id="q4"></a>4. MVC (Model-View-Controller) কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"MVC একটা app-কে তিন ভাগে ভাগ করে: Model data আর rule ধরে রাখে, View UI দেখায়, আর Controller input সামলায় এবং Model ও View update করে। লক্ষ্য হলো UI-কে data থেকে আলাদা রাখা। Flutter-এ বিশুদ্ধ MVC কম দেখা যায়, কারণ Flutter-এর reactive widget View/Controller-এর সীমারেখা ঝাপসা করে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা রেস্তোরাঁ।**
- **Model** = রান্নাঘর (খাবার আর রেসিপি — data আর rule)।
- **View** = খাওয়ার জায়গা (customer যা দেখেন)।
- **Controller** = ওয়েটার (আপনার order নেন, রান্নাঘরে বলেন, খাবার আনেন)।

**ধাপ ২ — তিনটা অংশ আর তারা কীভাবে কথা বলে।**

```
   input        updates
View  ───────►  Controller  ───────►  Model
  ▲                                     │
  └──────────── reads data ─────────────┘
```

Controller user-এর input নেয়, Model update করে, আর View Model-এর data দেখায়।

**ধাপ ৩ — Flutter-এ MVC কেন কম স্বাভাবিক।**
Flutter-এর widget reactive — এরা state থেকে rebuild হয়। তাই "View" আর "Controller"-এর ভূমিকা প্রায়ই মিশে যায়। বেশিরভাগ Flutter team-ই এর বদলে MVVM বা BLoC ব্যবহার করে ([Q5](#q5))। MVC এখনো web-এ আর পুরোনো mobile framework-এ খুব সাধারণ, তাই interviewer এটা জিজ্ঞেস করতে পারেন।

**Interviewer কেন জিজ্ঞেস করে:** এটা ক্লাসিক UI pattern। তাঁরা দেখেন আপনি তিনটা ভূমিকা জানেন কি না, আর MVVM-এর সাথে তুলনা করতে পারেন কি না।

**সাধারণ ভুল:** View (UI)-তে business logic রাখা। MVC-তে logic-এর জায়গা Model/Controller।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"MVC vs MVVM?"* → MVVM একটা ViewModel যোগ করে, যেটা দেখানোর জন্য প্রস্তুত state দেয়। ফলে View-কে সরাসরি Model জানতে হয় না ([Q5](#q5))।

**সম্পর্কিত:** [Q5 — MVVM](#q5) · [Q6 — MVP](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. MVVM কী, আর Cubit/BLoC এর সাথে কীভাবে মেলে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"MVVM মানে Model-View-ViewModel। ViewModel বসে UI আর data-র মাঝখানে: এটা screen-এর state ধরে রাখে আর দেখানোর জন্য প্রস্তুত রূপে প্রকাশ করে, আর View শুধু তার সাথে bind করে। Flutter-এ একটা Cubit বা BLoC ViewModel-এর কাজ করে — এটা state ধরে রাখে, state বদলালে widget rebuild হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একজন ব্যক্তিগত দোভাষী।**
ViewModel হলো কাঁচা data (Model) আর screen (View)-এর মাঝের একজন দোভাষী। View এলোমেলো data-র সাথে সরাসরি কথা বলে না। সে দোভাষীর কাছে পরিষ্কার, প্রস্তুত উত্তরটা চায়।

**ধাপ ২ — তিনটা অংশ।**

```
View (widget)  ◄── binds to ──  ViewModel (Cubit/BLoC)  ──► Model (repository)
   rebuilds on state change       holds & exposes state      data & rules
```

- **Model** — data আর business rule (repository, entity)।
- **View** — widget; এটা শুধু state দেখায় আর user-এর action পাঠায়।
- **ViewModel** — screen-এর state ধরে রাখে, Model-এর সাথে কথা বলে, View-কে পরিষ্কার state দেয়।

**ধাপ ৩ — Cubit-কে ViewModel হিসেবে (Flutter উদাহরণ)।**

```dart
// Model
class CounterRepository { int load() => 0; }

// ViewModel
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);
  void increment() => emit(state + 1); // state update করে; UI rebuild হয়
}

// View — শুধু ViewModel-এর সাথে bind করে
BlocBuilder<CounterCubit, int>(
  builder: (context, count) => Text('$count'),
);
```

widget কখনোই logic ধরে রাখে না। এটা শুধু `state` দেখায় আর `increment()` call করে। এটাই MVVM।

**ধাপ ৪ — MVVM কেন Flutter-এর সাথে এত ভালো মেলে।**
Flutter reactive: UI state থেকে rebuild হয়। ওই state ধরে রাখা একটা ViewModel (Cubit/BLoC/Riverpod notifier) নিখুঁতভাবে মিলে যায়। এই কারণেই Flutter-এ MVVM-ধাঁচের architecture সবচেয়ে বেশি চলে।

**Interviewer কেন জিজ্ঞেস করে:** MVVM হলো Flutter-এর সবচেয়ে সাধারণ architecture pattern। তাঁরা শুনতে চান BLoC/Cubit/Riverpod ViewModel-এর ভূমিকা পালন করে।

**সাধারণ ভুল:** ViewModel-এর বদলে widget-এ business logic রাখা, অথবা View-কে সরাসরি Model পড়তে দেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"MVVM vs MVP?"* → MVVM-এ View state-এর সাথে bind করে (reactive); MVP-তে Presenter একটা interface দিয়ে View-কে update পাঠায় ([Q6](#q6))।

**সম্পর্কিত:** [Q4 — MVC](#q4) · [Q6 — MVP](#q6) · [Q11 — event-driven BLoC](#q11)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. MVP (Model-View-Presenter) কী, আর এটা MVVM থেকে কীভাবে আলাদা?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"MVP-তে একটা Presenter থাকে যে সব logic করে আর একটা 'বোকা' View-কে ঠিক কী দেখাতে হবে তা বলে দেয়, সাধারণত একটা View interface দিয়ে। MVVM থেকে মূল পার্থক্য: MVP-তে Presenter সরাসরি View-কে update পাঠায়; MVVM-এ View observable state-এর সাথে bind করে আর নিজেই update হয়। MVVM বেশি reactive, তাই এটা Flutter-এর সাথে ভালো মেলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — তিনটা অংশ।**
- **Model** — data আর rule।
- **View** — নিষ্ক্রিয়; যা বলা হয় শুধু তাই দেখায় (প্রায়ই `showLoading()`, `showUser()`-এর মতো interface দিয়ে)।
- **Presenter** — সব logic ধরে রাখে; এটা Model-এর সাথে কথা বলে আর View-কে নির্দেশ দেয়।

**ধাপ ২ — MVP কীভাবে কাজ করে।**

```
View interface  ◄── commands (showUser) ──  Presenter  ──► Model
   (passive)                                  (logic)
```

Presenter একটা View interface-এর reference ধরে রাখে আর তার উপর method call করে।

```dart
abstract class UserView {
  void showLoading();
  void showUser(User user);
}

class UserPresenter {
  final UserView view;
  final UserRepository repo;
  UserPresenter(this.view, this.repo);

  Future<void> load() async {
    view.showLoading();
    view.showUser(await repo.getUser()); // Presenter View-কে push করে
  }
}
```

**ধাপ ৩ — MVVM থেকে মূল পার্থক্য।**
- **MVP** — Presenter View-এর method call করে update *push* করে। View নিষ্ক্রিয়।
- **MVVM** — View observable state-এর সাথে *pull/bind* করে; state বদলালে framework View rebuild করে। কোনো সরাসরি call নেই।

**ধাপ ৪ — Flutter কেন MVVM পছন্দ করে।**
Flutter-এর পুরো model হলো "state থেকে rebuild", যেটা MVVM-এর binding ধরন। Reactive framework-এ MVP-র হাতে লেখা `view.showX()` call অস্বাভাবিক লাগে। তাই MVP পুরোনো Android (Java) app-এ বেশি দেখা যায়।

**Interviewer কেন জিজ্ঞেস করে:** যাচাই করতে যে আপনি View-তে *push* করা (MVP) আর state-এর সাথে *bind* করার (MVVM) পার্থক্য বোঝেন।

**সাধারণ ভুল:** MVP আর MVVM এক বলা। Update-এর দিক (push vs bind) হলো আসল পার্থক্য।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Flutter-এ আপনি কোনটা ব্যবহার করবেন?"* → MVVM (BLoC/Cubit/Riverpod), কারণ এটা Flutter-এর reactive rebuild model-এর সাথে মেলে।

**সম্পর্কিত:** [Q5 — MVVM](#q5) · [Q4 — MVC](#q4)

[↑ উপরে ফিরুন](#toc)

---

# C. মূল building block-গুলো

---

## <a id="q7"></a>7. Repository Pattern কী, এটা কোন সমস্যা সমাধান করে, আর Clean Architecture-এ এটা কীভাবে বসে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Repository হলো একটা class, যেটা data কোথা থেকে আসে তা লুকিয়ে রাখে। App-এর বাকি অংশ repository-র কাছে data চায়। সেটা network, database নাকি cache থেকে এলো — তা নিয়ে মাথা ঘামায় না। এটা সেই সমস্যা সমাধান করে যেখানে UI আর logic একটা নির্দিষ্ট data source-এর সাথে বাঁধা পড়ে যায়। Clean Architecture-এ Domain repository interface ঠিক করে, আর Data layer সেটা implement করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একজন librarian।**
আপনি librarian-এর কাছে একটা বই চান। তিনি সেটা তাক থেকে আনলেন, পেছনের ঘর থেকে আনলেন, নাকি অন্য branch থেকে আনলেন — আপনি জানেন না, দরকারও নেই। আপনার data-র জন্য repository হলো সেই librarian।

**ধাপ ২ — এটা কোন সমস্যা সমাধান করে।**
Repository না থাকলে আপনার Cubit/BLoC সরাসরি API call করত আর JSON parse করত — ফলে সেটা ওই API-র সাথে আঠার মতো লেগে থাকত। Caching যোগ করলে বা API বদলালে logic নতুন করে লিখতে হতো। Repository এই সবকিছু একটা পরিষ্কার method-এর পেছনে লুকিয়ে রাখে।

**ধাপ ৩ — গঠন (interface + implementation)।**

```dart
// Domain layer: interface (কী, কীভাবে নয়)
abstract class UserRepository {
  Future<User> getUser(String id);
}

// Data layer: implementation (source ঠিক করে)
class UserRepositoryImpl implements UserRepository {
  final ApiClient api;
  final LocalCache cache;
  UserRepositoryImpl(this.api, this.cache);

  @override
  Future<User> getUser(String id) async {
    final cached = cache.get(id);
    if (cached != null) return cached;        // cache থেকে
    final user = await api.fetchUser(id);     // অথবা network থেকে
    cache.save(id, user);
    return user;
  }
}
```

Caller শুধু `repo.getUser(id)` করে — cache নাকি network, সেই সিদ্ধান্ত লুকানো থাকে।

**ধাপ ৪ — Clean Architecture-এ এটা কেন মানানসই।**
Domain-এর হাতে থাকে *interface* (তাই Domain খাঁটি থাকে), আর Data layer দেয় *implementation*। Presentation layer শুধু interface-এর উপর নির্ভর করে। তাই আপনি implementation বদলাতে পারেন, বা test-এর জন্য একটা fake inject করতে পারেন।

**Interviewer কেন জিজ্ঞেস করে:** বাস্তব Flutter app-এ repository সবচেয়ে বেশি ব্যবহৃত pattern। তাঁরা দেখতে চান আপনি "কোন data" আর "কোথা থেকে আসে" — এই দুটো আলাদা করতে পারেন কি না।

**সাধারণ ভুল:** repository বাদ দিয়ে API call আর JSON parsing সরাসরি Cubit/BLoC-এ রাখা — এতে আপনার logic একটা data source-এর সাথে বাঁধা পড়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা testing-এ কীভাবে সাহায্য করে?"* → আপনি একটা fake repository inject করেন, ফলে আসল network ছাড়াই logic test করা যায়।
- *"Single source of truth?"* → একটা repository network + local DB মিলিয়ে একটাই সামঞ্জস্যপূর্ণ view দিতে পারে (offline-first)।

**সম্পর্কিত:** [Q2 — Clean Architecture](#q2) · [Q9 — DI](#q9) · [Q8 — use case](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Use Case (Interactor) pattern কী? কখন এটা কাজে লাগে, আর কখন এটা বাড়াবাড়ি?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Use case হলো একটা class, যেটা ঠিক একটা business action করে — যেমন 'get user profile' বা 'place order'। এটা Domain layer-এ থাকে, state management আর repository-র মাঝখানে। আসল business rule আছে এমন জটিল app-এ এটা কাজে লাগে। কিন্তু সাধারণ CRUD app-এ এটা শুধু একটা বাড়তি layer হয়ে যায় যেটা call forward করে — সেটা বাড়াবাড়ি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা recipe।**
Use case হলো একটা নির্দিষ্ট recipe: "একটা cappuccino বানান।" ওই একটা কাজের সঠিক ধাপগুলো সে জানে। প্রতিটা business action পায় নিজের use case।

**ধাপ ২ — দেখতে কেমন।**
সাধারণত একটা class, যার একটাই `call` method থাকে। ফলে এটাকে function-এর মতো ব্যবহার করা যায়।

```dart
class GetUserProfile {
  final UserRepository repo;
  GetUserProfile(this.repo);

  Future<User> call(String id) {
    // এখানে business rule যোগ করা যায়: validation, একাধিক source মেলানো, ইত্যাদি
    return repo.getUser(id);
  }
}

// Cubit-এ ব্যবহার:
final user = await getUserProfile('123');
```

**ধাপ ৩ — কখন কাজে লাগে।**
- Action-টিতে আসল **business rule** আছে (validation, কয়েকটা repository মেলানো, হিসাব)।
- আপনি চান logic-টা কয়েকটা screen-এ **reusable** হোক।
- আপনি চান প্রতিটা action আলাদাভাবে **testable** হোক।

**ধাপ ৪ — কখন এটা বাড়াবাড়ি।**
Use case যদি শুধু `repo.getUser(id)` call করে আর কিছু না করে, তাহলে এটা একটা ফাঁকা মাঝের layer। সাধারণ app-এ Cubit সরাসরি repository call করতে পারে। শুধু একটা diagram মানার জন্য use case যোগ করবেন না (সেটা YAGNI সমস্যা)।

**Interviewer কেন জিজ্ঞেস করে:** এটা বিচারবোধ যাচাই করে — আপনি কি কারণ দেখে structure যোগ করেন, নাকি চোখ বন্ধ করে template মানেন?

**সাধারণ ভুল:** প্রতিটা repository call-এর জন্য use case যোগ করা, যদিও সেটা কিছুই করে না। এতে কোনো লাভ ছাড়াই boilerplate দ্বিগুণ হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা কোথায় থাকে?"* → Domain layer-এ, শুধু repository interface-এর উপর নির্ভর করে।
- *"`call` method কেন?"* → এটা object-কে function-এর মতো call করতে দেয়: `getUser('123')`।

**সম্পর্কিত:** [Q2 — Clean Architecture](#q2) · [Q7 — repository](#q7) · [Q14 — বেছে নেওয়া](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. Dependency Injection কী, আমরা কেন এটা ব্যবহার করি, আর `get_it` এটা কীভাবে implement করে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dependency Injection (DI) মানে একটা class তার দরকারি জিনিসগুলো বাইরে থেকে পায়, নিজে বানায় না। আমরা এটা ব্যবহার করি কম coupling আর testability-র জন্য — আপনি একটা আসল dependency-র বদলে fake বসাতে পারেন। `get_it` হলো একটা service locator। এটা startup-এ একবার dependency register করে, তারপর যেখানে দরকার সেখানে সেগুলো দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: socket-এ plug লাগানো।**
একটা lamp নিজের power plant বানায় না; সে socket-এ plug লাগিয়ে বিদ্যুৎ পায়। একটা class-এর নিজের database বানানো উচিত নয়; তার একটা database পাওয়া উচিত।

**ধাপ ২ — DI ছাড়া বনাম DI সহ।**

```dart
// DI ছাড়া — class নিজেই তার dependency বানায় (শক্ত করে বাঁধা, test করা কঠিন)
class OrderService {
  final api = HttpApiClient();
}

// DI সহ — dependency বাইরে থেকে দেওয়া হয় (বদলানো যায়, test করা যায়)
class OrderService {
  final ApiClient api;
  OrderService(this.api); // inject করা হলো
}
```

**ধাপ ৩ — `get_it` কীভাবে কাজ করে।**
`get_it` হলো একটা শেয়ার করা "toolbox": আপনি startup-এ প্রতিটা dependency একবার register করেন, তারপর যেকোনো জায়গা থেকে চেয়ে নেন — অনেকগুলো constructor দিয়ে পাস করার দরকার নেই।

```dart
final sl = GetIt.instance;

void setup() {
  sl.registerLazySingleton<ApiClient>(() => HttpApiClient());
  sl.registerLazySingleton<UserRepository>(() => UserRepositoryImpl(sl()));
  sl.registerFactory(() => UserCubit(sl())); // প্রতিবার নতুন instance
}

// যেকোনো জায়গায় ব্যবহার:
final cubit = sl<UserCubit>();
```

- `registerLazySingleton` → একটাই শেয়ার করা instance, প্রথম ব্যবহারে তৈরি হয়।
- `registerFactory` → যতবার চাইবেন, ততবার নতুন instance।

**ধাপ ৪ — DI কেন গুরুত্বপূর্ণ।**
- **Testability** — test-এ একটা fake `ApiClient` inject করুন; আসল network লাগবে না।
- **কম coupling** — class-গুলো interface-এর উপর নির্ভর করে, concrete class-এর উপর নয় ([DIP](#q10))।
- **এক জায়গায় wiring** — dependency বদলান setup-এ, 50টা file-এ নয়।

**Interviewer কেন জিজ্ঞেস করে:** testable আর layered app-এর জন্য DI অপরিহার্য। তাঁরা দেখতে চান আপনি class-এর ভেতরে `new` দিয়ে dependency শক্ত করে বাঁধছেন না।

**সাধারণ ভুল:** business logic-এর গভীরে সব জায়গায় `sl<X>()` call করা (লুকানো dependency)। constructor দিয়ে inject করাই ভালো; locator ব্যবহার করুন প্রান্তে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"DI-র জন্য get_it বনাম Provider/Riverpod?"* → `get_it` একটা সাধারণ service locator (`BuildContext` লাগে না)। Provider/Riverpod DI-কে widget tree-র সাথে বেঁধে দেয়।
- *"Singleton বনাম factory registration?"* → Singleton = একটাই শেয়ার করা instance; factory = প্রতি call-এ নতুন।

**সম্পর্কিত:** [Q10 — service locator বনাম DI](#q10) · [Q7 — repository](#q7) · [Q2 — Clean Architecture](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Service Locator আর Dependency Injection-এর মধ্যে পার্থক্য কী? এর trade-off কী কী?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"দুটোই dependency দেয়, কিন্তু উল্টো দিক থেকে। Dependency Injection-এ dependency constructor দিয়ে *ভেতরে ঠেলে দেওয়া* হয়, তাই সেগুলো class-এর signature-এ দেখা যায়। Service Locator-এ class একটা global registry-র কাছে চেয়ে dependency *টেনে আনে*। DI বেশি স্পষ্ট আর testable; service locator সুবিধাজনক, কিন্তু dependency লুকিয়ে ফেলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুটো ধরন।**

```dart
// Dependency Injection — dependency constructor-এ দেখা যায়
class OrderService {
  final ApiClient api;
  OrderService(this.api); // কী দরকার, তা আপনি দেখতে পাচ্ছেন
}

// Service Locator — dependency global registry থেকে আনা হয়
class OrderService {
  final api = sl<ApiClient>(); // দরকারটা লুকানো; জানতে হলে body পড়তে হবে
}
```

**ধাপ ২ — Trade-off গুলো।**

| | Dependency Injection | Service Locator |
|---|---|---|
| Dependency গুলো | constructor-এ দেখা যায় | class-এর ভেতরে লুকানো |
| Testability | সহজ (একটা fake পাস করে দিন) | কঠিন (global registry সাজাতে হয়) |
| সুবিধা | বেশি wiring | খুবই সুবিধাজনক |
| Coupling | কম, স্পষ্ট | locator-এর সাথে বেঁধে ফেলে |

**ধাপ ৩ — `get_it` আসলে একটা service locator।**
আমরা এটাকে "DI" বললেও `get_it` একটা service locator — আপনি `sl<X>()` থেকে টেনে আনেন। অনেক team দুটোরই সেরা দিকটা নেয়: `get_it`-এ register করে, কিন্তু resolve হওয়া object-গুলো constructor দিয়ে **inject** করে (ফলে class-গুলো নিজে DI ব্যবহার করে, আর শুধু setup locator ব্যবহার করে)।

**ধাপ ৪ — বাস্তব পরামর্শ।**
আপনার class-এর ভেতরে constructor injection-ই বেছে নিন (দেখা যায়, test করা যায়)। Service locator ব্যবহার করুন শুধু "প্রান্তে" (app setup, যেখানে আপনি object graph বানান)। এতে business class পরিষ্কার থাকে, আবার সুবিধাও থাকে।

**Interviewer কেন জিজ্ঞেস করে:** এটা senior-level বিচারবোধের প্রশ্ন — locator ব্যবহার করেও আপনি বোঝেন কি না স্পষ্ট dependency *কেন* ভালো?

**সাধারণ ভুল:** business logic-এর ভেতরে সব জায়গায় `sl<X>()` call করা। এতে কোন class কীসের উপর নির্ভর করে তা লুকিয়ে যায়, আর test করা কষ্টকর হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Service locator কি একটা anti-pattern?"* → স্বভাবতই নয়। logic-এর গভীরে ব্যবহার করলে, dependency লুকিয়ে ফেললে সেটা anti-pattern হয়ে যায়। Composition root-এ এটা ঠিক আছে।

**সম্পর্কিত:** [Q9 — DI / get_it](#q9) · [Q3 — separation of concerns](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. Event-driven architecture কী, আর BLoC এই ধারণাটা কীভাবে ব্যবহার করে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Event-driven মানে system-এর অংশগুলো একে অপরকে সরাসরি call না করে event পাঠায় আর event-এ react করে। BLoC এটাই ব্যবহার করে: UI ভেতরে event পাঠায়, BLoC সেগুলো process করে বাইরে state emit করে। এই one-way flow logic-কে predictable করে আর test করা সহজ করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা notice board।**
A সরাসরি B-কে হুকুম দেওয়ার বদলে A একটা note (event) board-এ টাঙিয়ে দেয়। যার দরকার সে এতে react করে। অংশগুলো event-এর মাধ্যমে আলগাভাবে যুক্ত থাকে।

**ধাপ ২ — BLoC-এর flow: event ভেতরে, state বাইরে।**

```
UI  ──(add Event)──►  BLoC  ──(emit State)──►  UI rebuilds
```

UI কখনোই সরাসরি state বদলায় না; সে একটা event পাঠায়। কোন নতুন state emit হবে সেটা BLoC ঠিক করে। UI শুধু নতুন state থেকে rebuild করে।

```dart
// Events (যা যা ঘটে)
sealed class CounterEvent {}
class Increment extends CounterEvent {}

// BLoC: event ভেতরে -> state বাইরে
class CounterBloc extends Bloc<CounterEvent, int> {
  CounterBloc() : super(0) {
    on<Increment>((event, emit) => emit(state + 1));
  }
}

// UI একটা event পাঠায়:
context.read<CounterBloc>().add(Increment());
```

**ধাপ ৩ — One-way flow কেন সাহায্য করে।**
- **Predictable** — প্রতিটা state change শুরু হয় একটা স্পষ্ট event থেকে।
- **Testable** — event দিন, emit হওয়া state check করুন (UI লাগে না)।
- **Traceable** — debugging-এর জন্য প্রতিটা event আর state log করা যায়।
- **Decoupled** — state *কীভাবে* তৈরি হয় UI সেটা জানে না।

**ধাপ ৪ — Cubit হলো সহজ ভাইটি।**
Cubit স্পষ্ট event বাদ দেয় আর সরাসরি method দেখায় (`increment()`)। সহজ flow-এর জন্য Cubit ব্যবহার করুন। Traceable event log চাইলে পুরো BLoC নিন।

**Interviewer কেন জিজ্ঞেস করে:** Event-driven, one-way data flow হলো BLoC, Redux আর Riverpod-এর মূল ধারণা। তাঁরা দেখতে চান আপনি "events in, states out" বোঝেন কি না।

**সাধারণ ভুল:** Event পাঠানো বা method call করার বদলে UI থেকে সরাসরি state বদলে দেওয়া। এতে one-way flow ভেঙে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"BLoC vs Cubit?"* → BLoC স্পষ্ট event ব্যবহার করে (বেশি traceable); Cubit সরাসরি method ব্যবহার করে (সহজ)।

**সম্পর্কিত:** [Q5 — MVVM](#q5) · [Q3 — separation of concerns](#q3)

[↑ উপরে ফিরুন](#toc)

---

# D. Scale করা আর বেছে নেওয়া

---

## <a id="q12"></a>12. মোবাইল টিমের জন্য Monorepo আর Multi-repo-র trade-off কী কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Monorepo সব code এক repository-তে রাখে; multi-repo সেটা অনেক repository-তে ভাগ করে। Monorepo-তে code share করা আর cross-cutting পরিবর্তন করা সহজ, একটাই source of truth থাকে — কিন্তু এটা বড় হয়ে যেতে পারে আর ভালো tooling লাগে। Multi-repo শক্ত আলাদা সীমানা আর স্বাধীন release দেয়, কিন্তু code share করা আর পরিবর্তন সমন্বয় করা কঠিন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি।**
- **Monorepo** = একটা বড় বাড়ি যেখানে প্রতিটা ঘরের (project) ঠিকানা একই। ঘরের মধ্যে জিনিস সরানো সহজ।
- **Multi-repo** = আলাদা আলাদা বাড়ি। সীমানা শক্ত, কিন্তু এক বাড়ি থেকে আরেক বাড়িতে জিনিস সরাতে পরিশ্রম লাগে।

**ধাপ ২ — Trade-off গুলো।**

| | Monorepo | Multi-repo |
|---|---|---|
| Code sharing | সহজ (এক জায়গায়) | কঠিন (package publish করতে হয়) |
| Cross-cutting পরিবর্তন | একটা commit/PR | অনেক সমন্বিত PR |
| সীমানা | নরম | শক্ত, বাধ্যতামূলক |
| স্বাধীন release | কঠিন | প্রতি repo-তে সহজ |
| যত tooling লাগে | বেশি (যেমন `melos`) | প্রতি repo-তে সহজ |

**ধাপ ৩ — Flutter-এ monorepo (`melos`)।**
Flutter টিমগুলো প্রায়ই `melos` দিয়ে monorepo ব্যবহার করে একাধিক package সামলাতে (একটা core package, feature package, app) এক repo-তে — local package link করে আর সবগুলোর উপর script চালায়।

**ধাপ ৪ — কীভাবে বাছবেন।**
- **Monorepo** — এক টিম বা ঘনিষ্ঠভাবে সম্পর্কিত project, যারা অনেক code share করে।
- **Multi-repo** — আলাদা টিম যারা স্বাধীনভাবে release করে আর শক্ত সীমানা চায়।

**Interviewer কেন জিজ্ঞেস করে:** এটা senior পদের জন্য scaling/team-structure-এর প্রশ্ন। তাঁরা trade-off শুনতে চান, "X সবসময় ভালো" এমন সরল কথা নয়।

**সাধারণ ভুল:** একটাকে সবসময় ভালো বলে দাবি করা। এটা টিমের আকার, release-এর গতি আর কতটা code share হয় তার উপর নির্ভর করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"`melos` কী?"* → Flutter monorepo সামলানোর একটা tool: local package link করে আর সবগুলোর উপর command চালায়।

**সম্পর্কিত:** [Q13 — modular architecture](#q13) · [Q14 — বেছে নেওয়া](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. Flutter-এ modular architecture (feature package) কী, আর বড় টিমগুলো কেন এটা নেয়?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Modular architecture app-কে আলাদা package-এ ভাগ করে — সাধারণত প্রতি feature-এ একটা, সাথে shared core package — একটা বিশাল lib folder-এর বদলে। বড় টিমগুলো এটা নেয় কারণ এতে স্পষ্ট সীমানা পাওয়া যায়, টিমগুলো একে অপরের গায়ে না লেগে সমান্তরালে কাজ করতে পারে, dependency-র নিয়ম বাধ্যতামূলক হয়, আর একটা feature-এর build ও test দ্রুত হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: Lego block।**
একটা বিশাল আঠা-লাগানো মূর্তির বদলে আপনি আলাদা block (feature) দিয়ে বানান। প্রতিটা block নিজে সম্পূর্ণ আর app-এ snap হয়ে বসে। একটা block বদলাতে অন্যগুলোতে হাত দিতে হয় না।

**ধাপ ২ — সাধারণ একটা structure।**

```
app/                  (the shell that wires features together)
packages/
  core/               (shared: networking, theming, utilities)
  domain/             (shared entities, repository interfaces)
  feature_auth/       (login feature — its own UI + logic)
  feature_profile/    (profile feature)
  feature_orders/     (orders feature)
```

সাধারণত একটা নিয়ম বাধ্যতামূলক করা হয়: feature package `core`/`domain`-এর উপর depend করতে পারে, কিন্তু **একে অপরের উপর নয়** — এতে feature গুলো স্বাধীন থাকে।

**ধাপ ৩ — বড় টিমগুলো কেন এটা নেয়।**
- **সমান্তরাল কাজ** — টিম A-র হাতে `feature_auth`, টিম B-র হাতে `feature_orders`, কোনো conflict নেই।
- **বাধ্যতামূলক সীমানা** — package system একটা feature-কে অন্য feature-এর ভেতরের জিনিস import করতে দেয় না।
- **দ্রুত build/test** — পুরো app ছাড়াই একটা feature test বা build করা যায়।
- **পুনর্ব্যবহার** — একটা feature package অন্য app-এ আবার ব্যবহার করা যায়।

**ধাপ ৪ — এর খরচ।**
বেশি setup আর tooling লাগে (প্রায়ই `melos` দিয়ে monorepo)। ছোট app-এর জন্য এটা বাড়তি বোঝা; বড় multi-team app-এর জন্য এটা বড় লাভ।

**Interviewer কেন জিজ্ঞেস করে:** এটা senior/lead পর্যায়ের scaling বিষয়। তাঁরা সীমানা আর সমান্তরাল টিম কাজের কথা শুনতে চান।

**সাধারণ ভুল:** Feature package গুলোকে একে অপরের উপর depend করতে দেওয়া। এতে যে জট এড়াতে চেয়েছিলেন সেটাই আবার তৈরি হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Feature গুলো একে অপরের সাথে কীভাবে কথা বলে?"* → `core`/`domain`-এর shared abstraction দিয়ে, বা app shell-এর একটা navigation/event layer দিয়ে — সরাসরি একে অপরকে import করে নয়।

**সম্পর্কিত:** [Q12 — monorepo](#q12) · [Q2 — Clean Architecture](#q2) · [Q14 — বেছে নেওয়া](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. নতুন একটা Flutter project-এর জন্য কোন architecture ব্যবহার করবেন, সেটা কীভাবে ঠিক করেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-13-architecture-patterns.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি architecture-টা project-এর আকার আর আয়ুর সাথে মিলিয়ে নিই। খুব ছোট app পায় সরল structure — Cubit আর একটা repository। মাঝারি app পায় layered MVVM, সাথে repository আর DI। বড়, দীর্ঘজীবী, multi-team app পায় পুরো Clean Architecture আর modular feature package। নিয়ম হলো: maintainable থাকার মতো যথেষ্ট structure, কিন্তু এত বেশি নয় যে কাজ ধীর হয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কোনো একটাই 'সেরা' architecture নেই।**
সঠিক পছন্দ নির্ভর করে আকার, টিম, আর app কতদিন বাঁচবে তার উপর। ছোট app-এ বেশি architecture দিলে সময় নষ্ট হয়; বড় app-এ কম architecture দিলে বিশৃঙ্খলা তৈরি হয়।

**ধাপ ২ — সহজ একটা সিদ্ধান্তের নির্দেশিকা।**

| Project | পরামর্শ |
|---|---|
| Prototype / খুব ছোট app | `setState` বা সরল Cubit + একটা repository |
| মাঝারি app | Layered MVVM: UI → Cubit/BLoC → repository, সাথে DI ([Q9](#q9)) |
| বড় / দীর্ঘজীবী | Clean Architecture ([Q2](#q2)) + use case + DI |
| বড় multi-team | Clean Architecture + modular feature package ([Q13](#q13)) |

**ধাপ ৩ — বাছাই করার আগে আমি যে প্রশ্নগুলো করি।**
- App কত বড় আর কতদিন চলবে?
- কতজন মানুষ বা কয়টা টিম এতে কাজ করবে?
- Business rule গুলো কতটা জটিল?
- Testability আর offline support কতটা গুরুত্বপূর্ণ?

**ধাপ ৪ — সরল দিয়ে শুরু করুন, তারপর বাড়ান।**
আপনি সরল structure দিয়ে শুরু করতে পারেন, আর app বড় হলে layer (use case, modular package) যোগ করতে পারেন। পরে structure যোগ করা ঠিক আছে; over-engineering উপড়ে ফেলা কষ্টকর। এটা architecture-এ প্রয়োগ করা YAGNI।

**Interviewer কেন জিজ্ঞেস করে:** এটা বাস্তব বিচারবুদ্ধি যাচাই করে — pattern অন্ধভাবে নকল না করে সমস্যার সাথে সমাধান মিলিয়ে নেওয়ার senior দক্ষতা।

**সাধারণ ভুল:** ৩ screen-এর app-এ পুরো Clean Architecture বসানো (boilerplate-এর বোঝা), বা বড় app-এ কোনো structure না রাখা (spaghetti)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Clean Architecture কখন বাড়াবাড়ি?"* → ছোট, স্বল্পায়ু app যাদের logic সরল — বাড়তি interface আর use case খরচ বাড়ায়, লাভ দেয় সামান্য।
- *"Project-এর মাঝপথে architecture বদলানো যায়?"* → হ্যাঁ, ধাপে ধাপে — আগে repository আনুন, তারপর DI, তারপর জটিলতা বাড়লে use case।

**সম্পর্কিত:** [Q2 — Clean Architecture](#q2) · [Q13 — modular](#q13) · [Q8 — use case (বাড়াবাড়ি?)](#q8)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতে দেখার জন্য)

Interview-এর দিন সকালে এটা পড়ুন। আগে table-গুলো, তারপর এক লাইনের reminder-গুলো।

## Clean Architecture-এর layer

| Layer | কী রাখে | কার উপর নির্ভর করে |
|---|---|---|
| Presentation | widget, BLoC/Cubit | Domain |
| Domain (কেন্দ্র) | entity, use case, repo interface | কারও উপর না (pure Dart) |
| Data | repo impl, API, DB, model | Domain |

নিয়ম: **dependency-গুলো ভেতরের দিকে যায়, Domain-এর দিকে।**

## UI pattern-গুলোর তুলনা

| Pattern | Update-এর ধরন | Flutter-এ কতটা মানায় |
|---|---|---|
| MVC | Controller, Model আর View দুটোই update করে | দুর্বল (দায়িত্ব ঘোলাটে হয়) |
| MVP | Presenter নিষ্ক্রিয় View-তে data push করে | পুরোনো Android |
| MVVM | View observable state-এর সাথে bind হয় | শক্তিশালী (BLoC/Cubit/Riverpod) |

## Service Locator বনাম DI

| | DI (constructor) | Service Locator |
|---|---|---|
| Dependency | দৃশ্যমান | লুকানো |
| Testability | সহজ | কঠিন |
| কোথায় ভালো | class-এর ভেতরে | শুধু app setup-এ |

## এক লাইনের reminder

- **Layered**: UI → Domain → Data; একটা layer শুধু নিচেরটার সাথে কথা বলে। ([Q1](#q1))
- **Clean Architecture**: Domain pure আর কেন্দ্রে; dependency-গুলো ভেতরের দিকে যায়। ([Q2](#q2))
- **Separation of concerns**: widget-এর ভেতরে networking বা parsing নয়। ([Q3](#q3))
- **MVVM** = ViewModel (Cubit/BLoC) state ধরে রাখে; View তার সাথে bind হয়। ([Q5](#q5))
- **MVP push করে** View-তে; **MVVM bind হয়** state-এর সাথে। ([Q6](#q6))
- **Repository** লুকিয়ে রাখে data কোথা থেকে আসে (network/cache/db)। ([Q7](#q7))
- **Use case** = একটা business action; শুধু call forward করলে এটা বাদ দিন। ([Q8](#q8))
- **DI** = dependency বাইরে থেকে ভেতরে পাঠান (testable); **get_it** একটা service locator। ([Q9](#q9), [Q10](#q10))
- **BLoC** = event ভেতরে, state বাইরে (এক-মুখী, testable flow)। ([Q11](#q11))
- **Monorepo** = share করা সহজ, tooling লাগে; **multi-repo** = শক্ত সীমানা, আলাদা release। ([Q12](#q12))
- **Modular package** = পরিষ্কার সীমানা + বড় app-এ team-এর সমান্তরাল কাজ। ([Q13](#q13))
- **আকার দেখে বাছুন**: সহজ app → Cubit+repo; বড় app → Clean + modular। Over-engineer করবেন না। ([Q14](#q14))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Interviewer "একটা pattern-এর নাম বলুন" থেকে ঠেলে নিয়ে যান "একটা বাস্তব app design করুন"-এ। জোরে বলে অনুশীলন করুন:

1. *"মাঝারি আকারের একটা Flutter app কীভাবে সাজাবেন?"* → layered MVVM: UI → Cubit → repository, সাথে DI।
2. *"API call কোথায় বসবে?"* → repository-তে (Data layer), কখনোই widget-এ নয়।
3. *"Logic কীভাবে test করবেন?"* → Cubit-এ একটা fake repository inject করুন; আসল network লাগবে না।
4. *"App বড় হয়ে ৫টা team হয়ে গেল — এখন কী?"* → feature package-এ ভাগ করুন (modular), সীমানা কড়াভাবে মানুন, melos দিয়ে monorepo ব্যবহার করুন।
5. *"ছোট app-এ Clean Architecture কি বাড়াবাড়ি নয়?"* → হ্যাঁ; structure-টা আকারের সাথে মেলান — সহজ দিয়ে শুরু করুন, বড় হলে layer যোগ করুন।

*Dependency-র দিক* আর প্রতিটা layer *কেন* আছে — এটা ব্যাখ্যা করাই senior উত্তরকে মুখস্থ উত্তর থেকে আলাদা করে। Remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
