# Section 16 — Clean Code

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন। উদাহরণে before/after Dart code ব্যবহার করা হয়েছে।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-16-clean-code.md](../software-engineer-flutter/section-16-clean-code.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — before/after code সহ ধাপে ধাপে ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সম্পর্কিত প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে ট্যাগ দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** Clean code-এর আসল বিষয় হলো *পাঠক*। বলুন — "code লেখা হয় একবার, পড়া হয় বহুবার" — তারপর প্রতিটা নিয়ম (নাম, ছোট function, কোনো চমক নয়) এই এক কথা থেকেই আসে: পাঠকের জীবন সহজ করা।

---


## <a id="toc"></a>সূচিপত্র

**A. ভিত্তি**
1. [Clean code কী?](#q1) · *Very common*
2. [Naming convention](#q2) · *Very common*

**B. Function ও abstraction**
3. [Clean function (ছোট, একটাই কাজ, কোনো side effect নেই)](#q3) · *Very common*
4. [Single Level of Abstraction](#q4) · *Common*
5. [Command-Query Separation (CQS)](#q5) · *Deeper*

**C. Comment ও formatting**
6. [কখন comment লিখবেন (self-documenting code)](#q6) · *Very common*
7. [একই রকম formatting ও `dart format`](#q7) · *Common*

**D. নিরাপদ code**
8. [Error code বনাম exception বনাম result type](#q8) · *Common*
9. [`null` return করা কেন ঝুঁকির](#q9) · *Common*
10. [Boolean trap](#q10) · *Common*

**E. নীতি ও অভ্যাস**
11. [Flutter-এ DRY](#q11) · *Common*
12. [Boy Scout Rule](#q12) · *Common*
13. [Clean code বনাম over-engineered code](#q13) · *Very common*

**F. Team-এ কাজে লাগানো**
14. [Clean code কাজে লাগানো (linter, review, pairing)](#q14) · *Common*
15. [`analysis_options.yaml` ও lint package](#q15) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের রিভিশন)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — মূল ভিত্তি (এখান থেকে শুরু করুন)।**
→ [Q1 Clean code কী](#q1) · [Q2 Naming](#q2) · [Q3 Clean function](#q3)

**পর্যায় ২ — পড়ার সহজতা।**
→ [Q6 Comment](#q6) · [Q7 Formatting](#q7) · [Q4 Single level of abstraction](#q4)

**পর্যায় ৩ — নিরাপদ, আগে থেকে বোঝা যায় এমন code।**
→ [Q8 Exception বনাম result type](#q8) · [Q9 Null এড়ানো](#q9) · [Q10 Boolean trap](#q10) · [Q5 CQS](#q5)

**পর্যায় ৪ — অভ্যাস ও বিচারবোধ।**
→ [Q11 DRY](#q11) · [Q12 Boy Scout Rule](#q12) · [Q13 Clean বনাম over-engineered](#q13)

**পর্যায় ৫ — Team-এ কাজে লাগানো।**
→ [Q14 Linter ও review](#q14) · [Q15 analysis_options.yaml](#q15)

**সময় কম?** দেখে নিন [Q1](#q1) · [Q2](#q2) · [Q3](#q3) · [Q6](#q6) · [Q13](#q13), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. ভিত্তি

---

## <a id="q1"></a>1. Clean code কী, আর বাস্তবে আপনি এটাকে কীভাবে সংজ্ঞায়িত করেন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Clean code মানে এমন code যা পড়া, বোঝা, বদলানো আর মুছে ফেলা সহজ। এটা নিজের উদ্দেশ্য স্পষ্ট করে বলে দেয়। ফলে পরের মানুষটাকে reverse-engineer করতে হয় না। মূল কথা: code লেখা হয় একবার, পড়া হয় বহুবার। তাই আমি পাঠকের কথা ভেবে code লিখি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: গোছানো রান্নাঘর।**
গোছানো রান্নাঘরে সবকিছুতে label থাকে, সব জিনিস নিজের জায়গায় থাকে। তাই যে কেউ রান্না করতে পারে। এলোমেলো code-এ কোনটা কী করে তা খুঁজতেই সময় নষ্ট হয়। Clean code হলো ওই গোছানো রান্নাঘর।

**ধাপ ২ — বাস্তবে 'clean' মানে কী।**
- **স্পষ্ট নাম**, যা উদ্দেশ্য বলে দেয় ([Q2](#q2))।
- **ছোট function**, যা একটাই কাজ করে ([Q3](#q3))।
- **কোনো চমক নেই** — function-এর নাম যা বলে, ঠিক তাই করে, লুকানো কিছু নেই।
- **মুছে ফেলা সহজ** — coupling কম, তাই একটা feature সরালে আরও দশটা ভাঙে না।

**ধাপ ৩ — সহজ পরীক্ষা।**
একজন নতুন সহকর্মী কি একটা function পড়ে কয়েক সেকেন্ডেই বুঝে ফেলতে পারবেন, আপনাকে জিজ্ঞেস না করে? পারলে সেটা clean। তাঁকে ঘুরিয়ে দেখাতে হলে সেটা clean নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা সুর ঠিক করে দেয় — আপনি machine-এর জন্য লেখেন, নাকি মানুষের জন্য? তাঁরা "পাঠকের জন্য" শুনতে চান।

**সাধারণ ভুল:** "Clean"-কে "চালাক" ভেবে নেওয়া। চালাক one-liner প্রায়ই clean-এর *উল্টো* ([Q13](#q13))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ব্যবসার জন্য এটা কেন গুরুত্বপূর্ণ?"* → পড়তে সহজ code বদলানো সস্তা আর তাতে bug কম থাকে। ফলে দল দ্রুত ship করতে পারে।

**সম্পর্কিত:** [Q2 — naming](#q2) · [Q3 — clean function](#q3) · [Q13 — over-engineered-এর সাথে তুলনা](#q13)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Dart-এ ভালো naming convention কোনগুলো, আর একটা নামকে ভালো বানায় কী?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"ভালো নাম উদ্দেশ্য বলে দেয় — জিনিসটা কী বা কী করে — কোনো comment ছাড়াই। Dart-এ: class আর enum-এ UpperCamelCase, variable আর function-এ lowerCamelCase, constant-এও lowerCamelCase, আর private member শুরু হয় underscore দিয়ে। সংক্ষিপ্ত রূপ আর একটা অক্ষরের নাম এড়িয়ে চলি, শুধু ছোট loop counter ছাড়া।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Dart-এর naming নিয়ম।**

| জিনিস | Style | উদাহরণ |
|---|---|---|
| Class, enum, typedef | UpperCamelCase | `UserRepository` |
| Variable, function, parameter | lowerCamelCase | `activeUsers`, `sendEmail()` |
| Constant | lowerCamelCase | `maxRetries` |
| Private member | শুরুতে `_` | `_balance` |
| File-এর নাম | snake_case | `user_repository.dart` |

**ধাপ ২ — একটা নামকে ভালো বানায় কী: এটা উদ্দেশ্য বলে দেয়।**

```dart
// খারাপ — কোনো অর্থ নেই
var d = 30;
List<User> getThem() => users.where((u) => u.f).toList();

// ভালো — নামেই বোঝা যায় এটা কী
const sessionTimeoutSeconds = 30;
List<User> getActiveUsers() => users.where((u) => u.isActive).toList();
```

**ধাপ ৩ — ব্যবহারিক নিয়ম।**
- Boolean পড়তে হবে হ্যাঁ/না প্রশ্নের মতো: `isActive`, `hasPermission`, `canEdit`।
- Function হবে ক্রিয়া: `fetchUser()`, `calculateTotal()`।
- সংক্ষিপ্ত রূপ (`usr`, `calc`) আর "শব্দদূষণ" শব্দ (`data`, `info`, `manager`) এড়িয়ে চলুন।
- একটা লম্বা কিন্তু স্পষ্ট নাম ছোট বোঝা কঠিন নামের চেয়ে ভালো।

**Interviewer কেন জিজ্ঞেস করে:** Naming হলো সবচেয়ে সস্তা কিন্তু সবচেয়ে বেশি প্রভাব ফেলা readability-র হাতিয়ার। Code পড়া কঠিন হওয়ার এক নম্বর কারণ খারাপ নাম।

**সাধারণ ভুল:** ছোট loop-এর বাইরে এক অক্ষরের বা সংক্ষিপ্ত নাম ব্যবহার করা, আর এমন boolean নাম দেওয়া যা হ্যাঁ/না প্রশ্নের মতো পড়া যায় না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা নাম কত লম্বা হওয়া উচিত?"* → স্পষ্ট হতে যতটা দরকার ততটা; সংক্ষিপ্ততার চেয়ে স্পষ্টতা বড়।

**সম্পর্কিত:** [Q1 — clean code](#q1) · [Q19 (Refactoring) — Rename](section-15-code-smells-bn.md#q19)

[↑ উপরে ফিরুন](#toc)

---

# B. Function ও abstraction

---

## <a id="q3"></a>3. Clean function-এর নিয়ম কী — ছোট আকার, একটাই কাজ, কোনো side effect নেই?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা clean function ছোট হবে, একটাই কাজ করবে, আর কোনো লুকানো side effect থাকবে না। 'একটাই কাজ' মানে একটাই স্তরের কাজ। 'কোনো side effect নেই' মানে এটা চুপচাপ global state বদলায় না, আর নামে যা বলা নেই সেই বাড়তি কাজও করে না। ছোট, লক্ষ্যভিত্তিক function পড়া, test করা আর আবার ব্যবহার করা সহজ।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ছোট এবং একটাই কাজ।**

```dart
// খারাপ — validation, হিসাব, save আর notify সবই করে
void process(Order o) { /* 80 lines, four jobs */ }

// ভালো — প্রতিটা একটা করে কাজ করে
void process(Order o) {
  _validate(o);
  final total = _calculateTotal(o);
  _save(o, total);
  _notify(o);
}
```

**ধাপ ২ — কোনো লুকানো side effect নেই।**
Side effect মানে function এমন কিছু বদলে দেয় যা তার নিজের বাইরে, আর যার কথা তার নামে বলা নেই।

```dart
// খারাপ — checkPassword চুপচাপ user-কে log in করিয়ে দেয় (লুকানো side effect)
bool checkPassword(String pw) {
  final ok = pw == stored;
  if (ok) session.initialize(); // চমক! নামে এর কোনো ইশারা নেই
  return ok;
}

// ভালো — নাম ঠিক যা বলে, কাজও ঠিক তাই
bool isPasswordValid(String pw) => pw == stored;
```

**ধাপ ৩ — অল্প parameter।**
কম হলে সহজ। শূন্য, এক বা দুই parameter আদর্শ; এর বেশি হলে সেটা একটা smell ([Long Parameter List](section-15-code-smells-bn.md#q6))। স্পষ্টতার জন্য Dart-এ named parameter ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** Function design প্রতিদিনের কাজ। লুকানো side effect থেকেই সবচেয়ে বাজে bug আসে।

**সাধারণ ভুল:** এমন function যার নাম এক জিনিস বলে, কিন্তু চুপচাপ আরেক কাজ করে (log in করিয়ে দেয়, global state বদলায়)। চমক বিশ্বাস নষ্ট করে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ছোট মানে কত ছোট?"* → এতটুকু ছোট যাতে একটাই কাজ করে আর scroll না করে উপর থেকে নিচ পর্যন্ত পড়া যায়।

**সম্পর্কিত:** [Q4 — single level of abstraction](#q4) · [Q5 — CQS](#q5) · [Q4 (Refactoring) — Long Method](section-15-code-smells-bn.md#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. Single Level of Abstraction principle কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা function-এর ভেতরে সব ধাপ একই মাত্রার detail-এ থাকা উচিত। 'sendEmail()'-এর মতো high-level ধাপ আর SMTP header string-concatenate করার মতো low-level detail একই function-এ মেশাবেন না। মাত্রা মেশালে function পড়া কঠিন হয়ে যায়; প্রতিটা function-কে এক altitude-এ রাখুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: একটা রান্নার recipe।**
Recipe বলে "sauce বানান", বলে না "sauce বানান, আর সাথে লবণের ছিপি খুলে ৩০ ডিগ্রি ঘোরান"। High-level আর low-level ধাপ পাশাপাশি বসা উচিত নয়।

**ধাপ ২ — আগে: মেশানো মাত্রা।**

```dart
void checkout(Cart cart) {
  validate(cart);                    // high level
  var total = 0.0;                   // low level (detail ভেতরে ঢুকে পড়ছে)
  for (final i in cart.items) total += i.price * i.qty;
  sendConfirmation(cart);            // আবার high level
}
```

**ধাপ ৩ — পরে: প্রতি function-এ এক মাত্রা।**

```dart
void checkout(Cart cart) {
  validate(cart);
  final total = calculateTotal(cart); // low-level detail ভেতরে লুকানো
  sendConfirmation(cart, total);
}
```

এখন `checkout` পড়লে high-level ধাপের একটা পরিষ্কার ধারা দেখা যায়; loop-টা থাকে `calculateTotal`-এর ভেতরে।

**Interviewer কেন জিজ্ঞেস করে:** এটা ব্যাখ্যা করে *কেন* method extract করলে code পড়া সহজ হয় — এটা প্রতিটা function-কে এক altitude-এ রাখে।

**সাধারণ ভুল:** এমন একটা function যেটা "বড় ছবি" call আর "খুঁটিনাটি" loop-এর মাঝে লাফায়। পাঠককে বারবার gear বদলাতে হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা Extract Method-এর সাথে কীভাবে সম্পর্কিত?"* → low-level detail-গুলোকে নাম দেওয়া method-এ extract করাই হলো single level পাওয়ার উপায়।

**সম্পর্কিত:** [Q3 — clean function](#q3) · [Q15 (Refactoring) — Extract Method](section-15-code-smells-bn.md#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Command-Query Separation (CQS) কী?

> Deeper · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"CQS বলে একটা method হয় কিছু *করবে* (command, যেটা state বদলায়), নয়তো কিছুর *উত্তর দেবে* (query, যেটা একটা value return করে) — দুটো একসাথে নয়। Query-র কোনো side effect থাকা উচিত নয়। এতে code আগে থেকে বোঝা যায় এমন হয়: প্রশ্ন করলে উত্তরটা চুপচাপ বদলে যায় না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: সময় জিজ্ঞেস করা।**
"কয়টা বাজে?" জিজ্ঞেস করলে ঘড়ি নড়ে যাওয়া উচিত নয়। Query শুধু উত্তর দেবে, কিছু বদলাবে না।

**ধাপ ২ — দুই ধরন।**
- **Command** — state বদলায়, সাধারণত কিছু return করে না (`void save()`, `void addItem()`)।
- **Query** — একটা value return করে, কিছু বদলায় না (`int count()`, `bool isValid()`)।

**ধাপ ৩ — আগে: একটা method যেটা দুটোই করে (বিভ্রান্তিকর)।**

```dart
// value return করে আর state-ও বদলায় — একটা লুকানো চমক
int popAndCount() {
  _items.removeLast();   // command (state বদলায়)
  return _items.length;  // query (value return করে)
}
```

**ধাপ ৪ — পরে: দুটোকে আলাদা করুন।**

```dart
void pop() => _items.removeLast();   // command
int get count => _items.length;      // query
```

এখন `count` যেকোনো সময় call করা নিরাপদ, কোনো side effect নেই।

**ধাপ ৫ — বাস্তব ব্যতিক্রম।**
কিছু পরিচিত method ইচ্ছা করেই CQS ভাঙে (যেমন `list.removeLast()` remove করে *আর* return-ও করে)। এটা expected হলে ঠিক আছে। নীতিটা *চমকে দেওয়া* সংমিশ্রণ এড়ানো নিয়ে।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা গভীর নীতি। এটা যাচাই করে আপনি আগে থেকেই বোঝা যায়, side-effect-মুক্ত query লেখেন কি না।

**সাধারণ ভুল:** এমন একটা getter বা "is/has" method যেটা চুপচাপ state বদলায় — পাঠক ধরে নেন query call করা নিরাপদ।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CQS ভাঙা কখন ঠিক আছে?"* → যখন মেশানো আচরণটা একটা সুপরিচিত idiom (যেমন `pop()` যে item তুলল সেটাই return করে)।

**সম্পর্কিত:** [Q3 — কোনো side effect নয়](#q3) · [Q9 — null এড়ানো](#q9)

[↑ উপরে ফিরুন](#toc)

---

# C. Comment ও formatting

---

## <a id="q6"></a>6. কখন comment লেখা উচিত, আর self-documenting code কী?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Comment লিখুন *কেন* বোঝানোর জন্য — কোনো অস্পষ্ট সিদ্ধান্ত, কোনো workaround, বা কোনো business rule। Code *কী* করে সেটা বোঝাতে comment লিখবেন না; বরং ভালো নাম আর ছোট function দিয়ে code-টাকেই পরিষ্কার করুন। এটাই self-documenting code।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — খারাপ comment: অস্পষ্ট code ব্যাখ্যা করা।**

```dart
// due date পেতে 7 দিন যোগ করা হচ্ছে
final due = created.add(Duration(days: 7));
```

Comment-টা আছে কারণ magic `7` অস্পষ্ট। বরং code-টাই ঠিক করুন।

**ধাপ ২ — Self-documenting রূপ।**

```dart
const gracePeriod = Duration(days: 7);
final dueDate = created.add(gracePeriod); // নামই সব বলছে; comment লাগছে না
```

**ধাপ ৩ — ভালো comment: 'কেন', যেটা code বলতে পারে না।**

```dart
// Payment gateway half-up round করে, তাই 1-cent refund এড়াতে আমরাও মিলিয়ে দিচ্ছি।
final cents = (amount * 100).round();

// TODO(srana): v2 API পুরোপুরি roll out হওয়ার পরে সরিয়ে দিন।
```

ভালো comment ধরে রাখে intent, সতর্কতা, business rule, আর public API-র doc (`///`)।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি আগে পরিষ্কার code-এর দিকে হাত বাড়ান কি না, আর comment শুধু সেখানেই ব্যবহার করেন যেখানে code কথা বলতে পারে না।

**সাধারণ ভুল:** এমন comment যেটা code-টাই আবার বলে (`i++; // increment`) — এগুলো শুধু noise বাড়ায়, আর code বদলালে পুরোনো হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Doc comment-এর কী হবে?"* → public API-র জন্য `///` ব্যবহার করুন; tool এগুলো থেকে doc তৈরি করে।

**সম্পর্কিত:** [Q2 — naming](#q2) · [Q12 (Refactoring) — comment একটা smell হিসেবে](section-15-code-smells-bn.md#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. Consistent formatting কেন গুরুত্বপূর্ণ, আর `dart format` কীভাবে ব্যবহার করেন?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Consistent formatting code দ্রুত চোখ বুলিয়ে পড়া সহজ করে। এটা মানে নেই এমন তর্ক আর diff-এর noise দূর করে। Dart-এ এটা নিয়ে তর্ক করতে হয় না — আপনি `dart format` (বা `flutter format`) চালান, যেটা official style-এ নিজে থেকেই format করে দেয়। বেশিরভাগ team এটা save-এর সময় আর CI-তে নিজে থেকেই চালায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কেন এটা গুরুত্বপূর্ণ।**
- **Readability** — এক রকম indentation আর spacing থাকলে চোখ দ্রুত structure খুঁজে পায়।
- **ছোট diff** — সবাই এক নিয়মে format করলে code review-তে আসল পরিবর্তন দেখা যায়, whitespace-এর noise নয়।
- **Bikeshedding নেই** — brace বা comma নিয়ে কেউ সময় নষ্ট করে তর্ক করে না।

**ধাপ ২ — `dart format` কাজটা আপনার হয়ে করে দেয়।**

```bash
dart format .          # পুরো project format করুন
dart format --output=none --set-exit-if-changed .  # CI: format না থাকলে fail করবে
```

**ধাপ ৩ — Trailing-comma-র কৌশল।**
Flutter-এ একটা trailing comma দিলে `dart format` widget-গুলোকে উপর-নিচ করে সাজায় — পড়তে আর edit করতে অনেক সহজ।

```dart
Column(
  children: [
    Text('a'),
    Text('b'),   // trailing comma → প্রতিটা child আলাদা line-এ
  ],
);
```

**ধাপ ৪ — এটা automate করুন।**
IDE-তে save করার সময় format করান। আর CI-তে একটা format check চালান, যাতে unformatted code merge হতে না পারে।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি হাতে style নিয়ে তর্ক না করে tooling ব্যবহার করেন কি না — একটা পরিণত workflow-র লক্ষণ।

**সাধারণ ভুল:** হাতে format করা, বা style নিয়ে তর্ক করা, যখন `dart format` ব্যাপারটা আগেই মিটিয়ে দিয়েছে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা কীভাবে enforce করেন?"* → একটা CI step, যেটা fail করবে যদি `dart format` কিছু বদলাত।

**সম্পর্কিত:** [Q14 — team-এ enforce করা](#q14) · [Q15 — lint config](#q15)

[↑ উপরে ফিরুন](#toc)

---

# D. নিরাপদ code

---

## <a id="q8"></a>8. Error code খারাপ কেন? Dart-এ exception বনাম result type কখন ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Error code (-1 বা একটা status int return করা) সহজেই বাদ দেওয়া যায়। আর এটা calling code-কে check দিয়ে ভরে ফেলে। সত্যিকারের হঠাৎ আসা failure-এর জন্য exception ভালো — এগুলো চুপচাপ বাদ দেওয়া যায় না। *expected* failure-এর জন্য (যেমন একটা ব্যর্থ network call) result type ভালো। sealed `Result` বা `Either`-এর মতো type success/failure স্পষ্ট করে দেয়। এটা caller-কে দুটোই handle করতে বাধ্য করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Error code খারাপ কেন।**

```dart
int saveUser(User u) {
  // return করে 0 = ok, 1 = network error, 2 = validation error
}
final code = saveUser(user); // return বাদ দেয় error মিস করা সহজ
```

Caller check করতে ভুলে যেতে পারে। আর `1` বনাম `2`-এর মানে পরিষ্কার নয়।

**ধাপ ২ — Exception — হঠাৎ আসা failure-এর জন্য।**
Exception চুপচাপ বাদ দেওয়া যায় না। Handle না করা পর্যন্ত এগুলো উপরে উঠতে থাকে।

```dart
Future<User> fetchUser() async {
  final res = await http.get(uri);
  if (res.statusCode != 200) throw NetworkException(); // বাদ দেওয়া যাবে না
  return User.fromJson(jsonDecode(res.body));
}
```

**ধাপ ৩ — Result type — expected failure-এর জন্য।**
Failure যখন একটা স্বাভাবিক ফলাফল আর আপনি চান caller সেটা handle করুক, তখন return type-এ sealed class দিয়ে সেটা প্রকাশ করুন (Dart 3):

```dart
sealed class Result<T> {}
class Ok<T> extends Result<T> { final T value; Ok(this.value); }
class Err<T> extends Result<T> { final String message; Err(this.message); }

Result<User> parseUser(Map<String, dynamic> json) {
  if (json['id'] == null) return Err('missing id');
  return Ok(User.fromJson(json));
}

// Caller-কে দুটোই handle করতেই হবে — compiler check করে
final r = parseUser(data);
switch (r) {
  case Ok(:final value): showUser(value);
  case Err(:final message): showError(message);
}
```

**ধাপ ৪ — সহজ নিয়ম।**
- **Exception** → হঠাৎ ঘটে, খুব বিরল (network down, bug)। একটা boundary-তে catch করুন।
- **Result type** → expected, সামলানো যায় এমন ফলাফল, যেগুলো caller স্পষ্টভাবে handle করুক আপনি চান।

**Interviewer কেন জিজ্ঞেস করে:** এটা আধুনিক error-handling design আর Dart 3 sealed class-এর পরীক্ষা।

**সাধারণ ভুল:** Error code return করা, বা স্বাভাবিক control flow-এর জন্য exception throw করা (ভারী আর হঠাৎ ঘটে)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"dartz-এর Either?"* → sealed `Result`-এর মতোই ধারণা — `Left` (failure) / `Right` (success)। এখন Dart 3 sealed class প্রায়ই এর জায়গা নেয়।

**সম্পর্কিত:** [Q9 — null এড়ানো](#q9) · [Q6 (DSA/Dart) — exception বনাম error](section-11-data-structure-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q9"></a>9. `null` return করা ঝুঁকির কেন, আর Dart-এ এর বিকল্প কী কী?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`null` return করা মানে caller-এর ঘাড়ে একটা লুকানো মাইন চাপিয়ে দেওয়া — check করতে ভুলে গেলেই crash। Dart-এর null safety-তে compiler সাহায্য করে, কিন্তু যেখানে পারা যায় `null` এড়ানোই ভালো। খালি collection return করুন, সত্যিই অনুপস্থিত data-র জন্য throw করুন, বা result/optional type দিয়ে 'হয়তো নেই' ব্যাপারটা স্পষ্ট করুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ঝুঁকিটা।**

```dart
User? findUser(String id) { /* না পাওয়া গেলে null return করে */ }
final name = findUser('x').name; // null হলে crash — check ভুলে যাওয়া সহজ
```

Null safety একটা `?` বা check করতে বাধ্য করে, এতে সাহায্য হয় — কিন্তু `null` return করলে check সব জায়গায় ছড়িয়ে পড়ে।

**ধাপ ২ — বিকল্প ১: null নয়, খালি collection return করুন।**

```dart
// খারাপ: List<User>? getUsers() — caller-কে null-check করতে হয়
// ভালো: সবসময় একটা list return করুন (কিছু না থাকলে খালি)
List<User> getUsers() => _users; // caller নিরাপদে iterate করতে পারে
```

**ধাপ ৩ — বিকল্প ২: সত্যিই দরকারি data না থাকলে throw করুন।**
Value যদি *থাকতেই হয়*, তাহলে চুপচাপ null-এর চেয়ে একটা পরিষ্কার exception ভালো।

```dart
User getUserOrThrow(String id) =>
    _users[id] ?? (throw UserNotFoundException(id));
```

**ধাপ ৪ — বিকল্প ৩: 'হয়তো' ব্যাপারটা স্পষ্ট করুন।**
*ইচ্ছা করে* একটা nullable type ব্যবহার করুন (আর সেটা handle করুন), বা একটা result type ([Q8](#q8))। তাহলে "হয়তো নেই" ব্যাপারটা contract-এর অংশ হয়, চমক নয়।

**Interviewer কেন জিজ্ঞেস করে:** Null handling crash-এর সবচেয়ে বড় উৎসগুলোর একটা। তাঁরা দেখতে চান আপনি এমন API design করেন কি না, যেখানে null-এর চমক কম।

**সাধারণ ভুল:** "না পাওয়া গেলে" সব জায়গায় `null` return করা, আর null check ছড়িয়ে দেওয়া। খালি collection বা স্পষ্ট result বেছে নিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Null Object pattern?"* → null-এর বদলে একটা ক্ষতিহীন default object return করুন (যেমন একটা `GuestUser`)। তাহলে caller-কে null check করতে হয় না।

**সম্পর্কিত:** [Q8 — result type](#q8) · [Q1 (Dart) — null safety](section-01-dart-language-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Boolean trap কী, আর Dart-এ আপনি এটা কীভাবে এড়ান?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Boolean trap মানে একটা function-এ খালি `true`/`false` পাঠানো, যেখানে call site দেখে বোঝার উপায় থাকে না ওটার মানে কী — যেমন `setUser('Sara', true, false)`। Dart-এ আপনি এটা এড়ান named parameter বা enum দিয়ে, যাতে মানেটা call site-এই দেখা যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — ফাঁদটা।**

```dart
createUser('Sara', true, false);
// true আর false-এর মানে কী? জানতে হলে createUser পড়তে যেতে হবে।
```

**ধাপ ২ — সমাধান ১: named parameter (Dart-এর নিয়ম)।**

```dart
createUser(name: 'Sara', isAdmin: true, sendEmail: false);
// এখন call site নিজেই নিজেকে ব্যাখ্যা করে।
```

**ধাপ ৩ — সমাধান ২: সত্যিকারের state থাকলে enum।**
একটা boolean প্রায়ই এমন একটা ধারণা লুকিয়ে রাখে, যেটা আসলে enum হওয়া উচিত।

```dart
// bool isVertical-এর বদলে
enum Axis { horizontal, vertical }
void layout(Axis axis) {}
layout(Axis.vertical); // বেশি পরিষ্কার আর বাড়ানো যায়
```

**ধাপ ৪ — কেন এটা গুরুত্বপূর্ণ।**
Named argument আর enum code-কে self-documenting করে তোলে। এগুলো পরিবর্তনও সামলাতে পারে (enum-এ তৃতীয় একটা option যোগ করা যায়; boolean বাড়ে না)।

**Interviewer কেন জিজ্ঞেস করে:** এটা পড়ার উপযোগী API design-এর পরীক্ষা — clean-code অভ্যাসের ছোট কিন্তু স্পষ্ট লক্ষণ।

**সাধারণ ভুল:** এক call-এ একের বেশি positional boolean (`true, false, true`) — পরে পড়া অসম্ভব।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Boolean parameter কখন ঠিক আছে?"* → যখন সেটা একটাই named boolean আর মানে স্পষ্ট (`expanded: true`)। কয়েকটা positional boolean একসাথে জমানো এড়ান।

**সম্পর্কিত:** [Q2 — naming](#q2) · [Q3 — clean function](#q3) · [Q7 (Dart) — named parameter](section-01-dart-language-bn.md#q7)

[↑ উপরে ফিরুন](#toc)

---

# E. নীতি ও অভ্যাস

---

## <a id="q11"></a>11. DRY principle কী, আর Flutter-এ আপনি এটা কীভাবে কাজে লাগান?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"DRY মানে Don't Repeat Yourself — প্রতিটা জ্ঞান এক জায়গায় রাখুন। Flutter-এ আপনি এটা কাজে লাগান বারবার আসা widget-গুলোকে reusable widget class-এ বের করে এনে, helper বা extension-এ logic ভাগ করে, আর color ও text style-এর মতো constant-গুলো theme-এ এক জায়গায় রেখে। কিন্তু যে code শুধু *দেখতে* এক রকম, সেটা মেলাবেন না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Logic-এর জন্য DRY।**

```dart
// বারবার আসা formatting logic → একবার বের করে আনুন
String formatPrice(double p) => '\$${p.toStringAsFixed(2)}';
```

**ধাপ ২ — Widget-এর জন্য DRY (Flutter-এ খুব সাধারণ)।**

```dart
// একই styled button সব জায়গায় copy-paste করার বদলে:
class PrimaryButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;
  const PrimaryButton({required this.label, required this.onTap, super.key});
  @override
  Widget build(BuildContext context) =>
      ElevatedButton(onPressed: onTap, child: Text(label));
}
```

**ধাপ ৩ — Constant-এর জন্য DRY: theme ব্যবহার করুন।**
Color, spacing আর text style `ThemeData` বা একটা constants file-এ এক জায়গায় রাখুন। তাহলে design পরিবর্তন এক জায়গাতেই হয়।

**ধাপ ৪ — সাবধানতা।**
আজ দেখতে এক রকম লাগছে বলেই দুই টুকরো code জোর করে এক করবেন না। এগুলো আলাদা নিয়ম বোঝালে আলাদাই রাখুন। DRY হলো ডুপ্লিকেট *জ্ঞান* নিয়ে, দেখতে ডুপ্লিকেট line নিয়ে নয়।

**Interviewer কেন জিজ্ঞেস করে:** Duplication bug-এর সবচেয়ে বড় কারণগুলোর একটা। তাঁরা দেখতে চান আপনি Flutter-এর প্রসঙ্গে এটা বুদ্ধি খাটিয়ে সরান কি না।

**সাধারণ ভুল:** বেশি DRY করে ফেলা — একটা বিশাল shared widget বা function, যাতে সামান্য আলাদা কেস সামলাতে অনেক flag থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Duplication কখন ঠিক আছে?"* → যখন এক করলে এমন দুটো জিনিস জুড়ে যাবে, যেগুলোর আলাদাভাবে বদলানো উচিত।

**সম্পর্কিত:** [Q9 (Refactoring) — Duplicate Code](section-15-code-smells-bn.md#q9) · [Q15 (OOP) — DRY](section-12-oop-principles-bn.md#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Boy Scout Rule কী, আর আপনি এটা কীভাবে মেনে চলেন?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Boy Scout Rule বলে: code যেমন পেয়েছিলেন, তার চেয়ে একটু পরিষ্কার করে রেখে যান। যখনই কোনো file-এ হাত দেন, একটা ছোট উন্নতি করুন — একটা ভালো নাম, একটা extract করা method, একটা মুছে দেওয়া dead line। সময়ের সাথে এই ছোট ছোট পরিষ্কারের কাজই codebase-কে সুস্থ রাখে, কোনো বড় rewrite ছাড়াই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — মূল ধারণা।**
Scout-রা campsite যেমন পেয়েছিল, তার চেয়ে পরিষ্কার করে রেখে যায়। Code-এ এর মানে: কোনো feature বা bug-এর জন্য যখনই file edit করেন, সাথে একটা ছোট পরিষ্কারের কাজও করুন।

**ধাপ ২ — ছোট পরিষ্কারের উদাহরণ।**
- বিভ্রান্তিকর একটা variable-এর নাম বদলান।
- লম্বা একটা block-কে নাম দেওয়া method-এ extract করুন।
- dead বা comment করে রাখা line মুছে দিন।
- magic number-এর বদলে একটা constant বসান।

**ধাপ ৩ — এটা কেন কাজ করে।**
বড় refactor ঝুঁকির কাজ। আর এগুলো খুব কমই schedule-এ জায়গা পায়। ছোট ছোট নিয়মিত উন্নতি খরচটা ভাগ করে দেয়। ঝুঁকিও কম থাকে। আর ধীরে ধীরে code rot উল্টে যায় — আলাদা সময় না চেয়েই।

**ধাপ ৪ — সীমা ধরে রাখুন।**
এক line-এর bug fix-কে 500 line-এর refactor বানাবেন না — এতে PR ফুলে যায় আর আসল পরিবর্তন ঢাকা পড়ে। আপনি যেখানে এমনিতেই হাত দিচ্ছেন, তার আশেপাশে *ছোট* উন্নতি করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় code quality নিয়ে আপনার একটা টেকসই, team-বান্ধব উপায় আছে।

**সাধারণ ভুল:** হয় কখনোই পরিষ্কার না করা (rot বাড়তে থাকে), নয়তো সম্পর্ক নেই এমন জায়গায় বেশি পরিষ্কার করা (বিশাল, ঝুঁকির diff, যা review করা কঠিন)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"পরিষ্কারের কাজগুলো review করার মতো রাখেন কীভাবে?"* → ছোট রাখুন আর নিজের পরিবর্তনের কাছাকাছি রাখুন; অথবা বড় পরিষ্কারের কাজটা আলাদা PR-এ ভাগ করুন।

**সম্পর্কিত:** [Q3 (Refactoring) — team-কে রাজি করানো](section-15-code-smells-bn.md#q3) · [Q2 (Refactoring) — নিরাপদে refactor](section-15-code-smells-bn.md#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q13"></a>13. Clean code আর over-engineered code-এর পার্থক্য কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Clean code যতটা সম্ভব সহজ, কিন্তু তারপরও স্পষ্ট আর বদলানোর মতো। Over-engineered code এমন layer, pattern আর flexibility যোগ করে যা এখনো দরকার নেই — কাল্পনিক ভবিষ্যৎ requirement-এর জন্য abstraction। Clean code আজকের সমস্যাটা সহজভাবে সমাধান করে; over-engineering এমন সমস্যা সমাধান করে যা আপনার নেই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের একটা ছবি।**
Clean code হলো ঠিক মাপের যন্ত্র। Over-engineering হলো একটা আপেল কাটার জন্য 12-blade মেশিন কেনা — দেখতে দারুণ, কিন্তু শুধু পথে বাধা হয়।

**ধাপ ২ — Over-engineering দেখতে এমন।**

```dart
// Over-engineered: 5টা interface, একটা factory, আর একটা strategy...
// ...শুধু একটা date format করতে, যা মাত্র এক জায়গায় দেখা যায়।
```

লক্ষণ: যে abstraction-এর implementation মাত্র একটা, "configurable" system যা কেউ configure করে না, "just in case" ভেবে যোগ করা pattern (এটা YAGNI ভাঙা)।

**ধাপ ৩ — Clean মানে সহজ, কিন্তু অযত্ন নয়।**
Clean code মানে "কোনো structure নেই" নয় — এতে *ঠিক* পরিমাণ structure থাকে। দক্ষতাটা হলো structure-কে আসল প্রয়োজনের সাথে মেলানো: এখন সহজ, আর দরকার সত্যিই এলে *তখন* সহজে বাড়ানো যায় ([OCP](section-12-oop-principles-bn.md#q11))।

**ধাপ ৪ — balance।**
- Structure খুব কম → spaghetti, বদলানো কঠিন।
- Structure খুব বেশি → over-engineering, বোঝা কঠিন।
- Clean code → ঠিক যতটা দরকার, তার বেশি নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটাই senior-এর বুদ্ধির প্রশ্ন। Junior-রা pattern বেশি কাজে লাগান; senior-রা জানেন কখন *করতে হয় না*।

**সাধারণ ভুল:** দেখানোর জন্য design pattern আর abstraction layer যোগ করা। এতে সহজ জিনিস বোঝা কঠিন হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কতটা structure লাগবে সেটা কীভাবে ঠিক করেন?"* → App-এর আকার, আয়ু, আর আসল (কাল্পনিক নয়) requirement-এর সাথে মিলিয়ে ঠিক করুন ([YAGNI](section-12-oop-principles-bn.md#q17))।

**সম্পর্কিত:** [Q1 — clean code](#q1) · [Q17 (OOP) — YAGNI](section-12-oop-principles-bn.md#q17) · [Q14 (Architecture) — বেছে নেওয়া](section-13-architecture-patterns-bn.md#q14)

[↑ উপরে ফিরুন](#toc)

---

# F. Team-এ কাজে লাগানো

---

## <a id="q14"></a>14. Team-এ clean code কীভাবে কাজে লাগান? (linters, code review, pair programming)

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"ইচ্ছাশক্তির উপর ভরসা করা যায় না — এটা workflow-এর ভেতরে বসিয়ে দিতে হয়। Automated linter আর formatter style আর সাধারণ ভুল ধরে ফেলে। Code review ধরে design আর readability-র সমস্যা, যা কোনো tool ধরতে পারে না। আর pair programming জ্ঞান আর standard সাথে সাথেই ছড়িয়ে দেয়। সব মিলে clean code-ই default হয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Linter আর formatter (automated)।**
Tool style কাজে লাগায় আর review-এর আগেই সমস্যা ধরে। Flutter-এ: style-এর জন্য `dart format`, আর সমস্যার জন্য lint package সহ `dart analyze` ([Q15](#q15))। এগুলো save করার সময় আর CI-তে চালান, যাতে অপরিষ্কার code merge না হতে পারে।

**ধাপ ২ — Code review (মানুষের বুদ্ধি)।**
Tool যা ধরতে পারে না, review তা ধরে: অস্পষ্ট নাম, খারাপ design, বাদ পড়া edge case, দুর্বল test। Review ভদ্র আর একদম নির্দিষ্ট রাখুন — হুকুম না দিয়ে প্রশ্ন করুন ("list খালি হলে কী হবে?")।

**ধাপ ৩ — Pair programming (সাথে সাথে)।**
দুজন মানুষ একসাথে code লিখলে standard সাথে সাথে ভাগাভাগি হয়। সমস্যা ঘটার সাথে সাথেই ধরা পড়ে। আর জ্ঞান ছড়ায়, তাই quality একজন মানুষের উপর নির্ভর করে না।

**ধাপ ৪ — এটাকে team-এর standard বানান, একজনের মতামত নয়।**
Lint rule আর review checklist team হিসেবে ঠিক করে নিন। তাহলে feedback হবে যৌথ standard নিয়ে, ব্যক্তিগত পছন্দ নিয়ে নয়। এতে বিষয়টা নিরপেক্ষ থাকে আর ঘষাঘষি কমে।

**Interviewer কেন জিজ্ঞেস করে:** Senior/lead পদের জন্য তাঁরা দেখতে চান আপনি পুরো team-এ quality ছড়াতে পারেন কি না, শুধু নিজে clean code লেখা নয়।

**সাধারণ ভুল:** সহজ check-গুলো automate না করে শুধু review-র উপর ভরসা করা (ধীর, আর একেক জায়গায় একেক রকম)। অথবা formatter-এর কাজ করা style নিয়ে review-তে খুঁটিনাটি ধরা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"CI-তে কী কী থাকা উচিত?"* → Format check, analyzer/lint, আর test — এর কোনোটা fail করলে build fail করান।

**সম্পর্কিত:** [Q15 — lint config](#q15) · [Q7 — formatting](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. `analysis_options.yaml` কী, আর `flutter_lints` / `very_good_analysis` দিয়ে lint rule কীভাবে setup করেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-16-clean-code.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"`analysis_options.yaml` হলো সেই config file, যা Dart analyzer-কে বলে কোন lint rule কাজে লাগাতে হবে। আপনি একটা তৈরি rule set include করেন — `flutter_lints` (official baseline) বা `very_good_analysis` (আরো কড়া)। তারপর আলাদা rule যোগ করতে বা বন্ধ করতে পারেন। এরপর analyzer IDE-তে আর CI-তে সমস্যা দেখিয়ে দেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এটা কী করে।**
Dart analyzer `analysis_options.yaml` পড়ে ঠিক করে কী নিয়ে warning দেবে — ব্যবহার না হওয়া variable, বাদ পড়া `const`, খারাপ style, আর শত শত optional lint rule।

**ধাপ ২ — একটা lint package include করুন।**

```yaml
# analysis_options.yaml
include: package:flutter_lints/flutter.yaml   # official baseline
# or: include: package:very_good_analysis/analysis_options.yaml  # আরো কড়া

linter:
  rules:
    prefer_const_constructors: true
    avoid_print: true
    # একটা rule বন্ধ করতে:
    public_member_api_docs: false

analyzer:
  errors:
    invalid_annotation_target: ignore
```

`flutter_lints` হলো নরম, recommended default; `very_good_analysis` অনেক বেশি কড়া (যে team কড়া standard চায়, তাদের জন্য ভালো)।

**ধাপ ৩ — চালান।**

```bash
dart analyze   # অথবা: flutter analyze
```

এটা CI-তে চালান আর সমস্যা পেলে build fail করান, যাতে অপরিষ্কার code merge না হতে পারে।

**ধাপ ৪ — Team-এর জন্য মানিয়ে নিন।**
একটা package দিয়ে শুরু করুন। তারপর team-এর সম্মতিতে নির্দিষ্ট rule চালু বা বন্ধ করুন। Warning-কে ঠিক করার জিনিস হিসেবে দেখুন, বাদ দেওয়ার জিনিস নয়।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি আসল Flutter project-এ automated quality gate বসাতে জানেন কি না।

**সাধারণ ভুল:** Analyzer-এর warning বাদ দেওয়া, অথবা lint কখনোই configure না করা (সহজ, automatic quality-র সুবিধা হাতছাড়া করা)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"flutter_lints বনাম very_good_analysis?"* → `flutter_lints` = official, নরম baseline; `very_good_analysis` = আরো কড়া, বেশি মতামতওয়ালা rule।

**সম্পর্কিত:** [Q14 — clean code কাজে লাগানো](#q14) · [Q7 — dart format](#q7)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের রিভিশন)

Interview-এর দিন সকালে এটা পড়ুন। আগে table, তারপর এক line-এর মনে করিয়ে দেওয়া কথাগুলো।

## Dart naming এক নজরে

| জিনিস | Style |
|---|---|
| Class / enum / typedef | UpperCamelCase |
| Variable / function / constant | lowerCamelCase |
| Private member | শুরুতে `_` |
| File | snake_case.dart |

## Clean code-এর নিয়ম

| নিয়ম | এক line-এ |
|---|---|
| Names | উদ্দেশ্য স্পষ্ট করে; কোনো সংক্ষেপ নয় |
| Functions | ছোট, একটাই কাজ, লুকানো side effect নয় |
| Comments | *কেন* বোঝায়, *কী* নয় |
| Formatting | `dart format` চালান, তর্ক নয় |
| Errors | exception (হঠাৎ ঘটে) / result type (expected) |
| null | খালি collection / স্পষ্ট result বেছে নিন |
| Booleans | named param বা enum ব্যবহার করুন |

## এক লাইনের মনে রাখার তালিকা

- **Clean code** = পড়তে, বদলাতে, মুছতে সহজ; পাঠকের জন্য লেখা। ([Q1](#q1))
- **ভালো নাম** উদ্দেশ্য বলে দেয়, কোনো comment লাগে না। ([Q2](#q2))
- **Function**: ছোট, একটাই কাজ, কোনো চমক নয় (লুকানো side effect নয়)। ([Q3](#q3))
- **Single level of abstraction** — high-level আর low-level ধাপ মেশাবেন না। ([Q4](#q4))
- **CQS** — command state বদলায়; query একটা value ফেরত দেয়; দুটো মেশাবেন না। ([Q5](#q5))
- **Comment** ব্যাখ্যা করে *কেন*; নাম ব্যাখ্যা করুক *কী*। ([Q6](#q6))
- **`dart format`** style-এর ঝগড়া মিটিয়ে দেয়; CI-তে automate করুন। ([Q7](#q7))
- **Exception** হঠাৎ আসা failure-এর জন্য; **result type** expected failure-এর জন্য। ([Q8](#q8))
- **null ফেরত দেওয়া এড়ান** — খালি collection, throw, অথবা স্পষ্ট result। ([Q9](#q9))
- **Boolean trap** — named param / enum ব্যবহার করুন, যাতে call site পরিষ্কার থাকে। ([Q10](#q10))
- **DRY** বুদ্ধি করে মানুন; **Boy Scout Rule** — একটু পরিষ্কার করে রেখে যান। ([Q11](#q11), [Q12](#q12))
- **Clean ≠ চালাক**; over-engineering এড়ান — ঠিক যতটুকু structure দরকার ততটুকুই। ([Q13](#q13))
- **মানতে বাধ্য করুন** linter + review + pairing দিয়ে; `analysis_options.yaml` configure করুন। ([Q14](#q14), [Q15](#q15))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer কীভাবে আরও গভীরে যান

Interviewer এলোমেলো code দেখান, তারপর সেটা পরিষ্কার করতে বলেন। মুখে বলে বলে অনুশীলন করুন:

1. *"এই function-এ সমস্যা কী?"* → smell-এর নাম বলুন (খারাপ নাম, বেশি লম্বা, side effect)।
2. *"নামগুলো ঠিক করুন।"* → উদ্দেশ্য বোঝাতে rename করুন; এরপর কোনো comment লাগবে না।
3. *"এটা error-এ -1 ফেরত দেয় — ভালো উপায় কী?"* → হঠাৎ আসা হলে exception, expected হলে result type।
4. *"পুরো team-এ এটা কীভাবে মানাবেন?"* → CI-তে linter + `dart format`, code review, pairing।
5. *"এত structure কি আমাদের ধীর করে দিচ্ছে না?"* → clean ≠ over-engineered; আসল দরকার অনুযায়ী ঠিক ততটুকুই ব্যবহার করুন।

"Code লেখা হয় কম, পড়া হয় বেশি" — এটা বলা, তারপর "পাঠকের জীবন সহজ করুন" থেকে প্রতিটা নিয়ম বের করে আনা, এটাই আসল senior signal — remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
