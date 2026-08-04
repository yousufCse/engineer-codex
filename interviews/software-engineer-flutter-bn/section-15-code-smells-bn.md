# Section 15 — Code Smells & Refactoring

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়** লেখা, **ধাপে ধাপে পুরো ব্যাখ্যা করা**, আর **link দেওয়া** — তাই আপনি এদিক-ওদিক ঘুরে ধীরে ধীরে প্রস্তুতি নিতে পারবেন। প্রতিটা সমাধানে before/after Dart code দেওয়া আছে।

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-15-code-smells.md](../software-engineer-flutter/section-15-code-smells.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২–৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — ধাপে ধাপে ব্যাখ্যা, সাথে before/after code।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — যুক্ত প্রশ্নগুলোতে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে tag দেওয়া আছে — কত ঘন ঘন জিজ্ঞেস করা হয় (**Very common / Common / Deeper**) আর কতটা কঠিন (**Easy / Medium / Hard**)।

> **Interview Tip:** smell-টির নাম বলুন, তারপর বলুন *কেন* এটা ক্ষতি করে, শেষে যে refactoring এটা ঠিক করে তার নাম বলুন। Refactoring মানে গঠন উন্নত করা, **behaviour না বদলে** — সবসময় বলুন "behaviour একই থাকে।"

---


## <a id="toc"></a>সূচিপত্র

**A. ভিত্তি**
1. [Code smell বনাম bug](#q1) · *Very common*
2. [নিরাপদে কীভাবে refactor করবেন](#q2) · *Very common*
3. [Team-কে refactor করাতে কীভাবে রাজি করাবেন](#q3) · *Common*

**B. Bloater smells**
4. [Long Method](#q4) · *Very common*
5. [Large Class (God Object)](#q5) · *Very common*
6. [Long Parameter List](#q6) · *Common*
7. [Data Clumps](#q7) · *Common*
8. [Primitive Obsession](#q8) · *Common*

**C. Duplication ও অকেজো ভার**
9. [Duplicate Code](#q9) · *Very common*
10. [Magic Numbers আর Strings](#q10) · *Very common*
11. [Dead Code](#q11) · *Common*
12. [Comment যখন একটা smell](#q12) · *Common*

**D. Coupling smells**
13. [Feature Envy](#q13) · *Common*
14. [Shotgun Surgery বনাম Divergent Change](#q14) · *Common*

**E. Refactoring কৌশল**
15. [Extract Method](#q15) · *Very common*
16. [Extract Class](#q16) · *Common*
17. [Inline Method](#q17) · *Common*
18. [Move Method](#q18) · *Common*
19. [নিরাপদে Rename করা](#q19) · *Common*
20. [Introduce Parameter Object](#q20) · *Common*
21. [Replace Temp with Query](#q21) · *Deeper*

**F. Conditional refactorings**
22. [Replace Magic Number with Named Constant](#q22) · *Common*
23. [Replace Conditional with Polymorphism](#q23) · *Very common*
24. [Decompose Conditional](#q24) · *Common*
25. [Consolidate Conditional Expression](#q25) · *Deeper*

**G. Legacy code**
26. [Strangler Fig Pattern](#q26) · *Deeper*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের review)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

**পর্যায় ১ — ভিত্তি (এখান থেকেই শুরু করুন)।**
→ [Q1 Smell বনাম bug](#q1) · [Q2 নিরাপদে refactor](#q2) · [Q15 Extract Method](#q15)

**পর্যায় ২ — সবচেয়ে বেশি নাম আসা smell।**
→ [Q4 Long Method](#q4) · [Q5 Large Class](#q5) · [Q9 Duplicate Code](#q9) · [Q10 Magic Numbers](#q10)

**পর্যায় ৩ — গভীর smell।**
→ [Q6 Long Param List](#q6) · [Q7 Data Clumps](#q7) · [Q8 Primitive Obsession](#q8) · [Q13 Feature Envy](#q13) · [Q14 Shotgun Surgery](#q14)

**পর্যায় ৪ — Refactoring গুলো।**
→ [Q16 Extract Class](#q16) · [Q18 Move Method](#q18) · [Q20 Parameter Object](#q20) · [Q23 Replace Conditional with Polymorphism](#q23)

**পর্যায় ৫ — Advanced আর legacy।**
→ [Q21 Replace Temp with Query](#q21) · [Q24 Decompose](#q24) · [Q25 Consolidate](#q25) · [Q26 Strangler Fig](#q26) · [Q3 Team-কে রাজি করানো](#q3)

**সময় কম?** দেখুন [Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q9](#q9) · [Q10](#q10) · [Q23](#q23), তারপর [Cheat Sheet](#cheatsheet)।

---

# A. ভিত্তি

---

## <a id="q1"></a>1. Code smell কী, আর এটা bug থেকে কীভাবে আলাদা?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Code smell হলো একটা ইশারা যে code-এর কোনো অংশের গঠন খারাপ, আর পরে ঝামেলা হতে পারে — কিন্তু এখনো এটা ঠিকভাবেই কাজ করে। Bug মানে code আসলেই ভেঙে গেছে। তাই smell হলো *design* নিয়ে একটা সতর্কবার্তা, আর bug হলো *behaviour*-এর ব্যর্থতা।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: রান্নাঘরে বাজে গন্ধ।**
বাজে গন্ধ মানে এই নয় যে আপনি এখনই অসুস্থ। কিন্তু এটা সতর্ক করে যে কিছু একটা পচছে। Code smell সতর্ক করে যে অগ্রাহ্য করলে code বদলানো কঠিন হবে বা bug ভরে যাবে।

**ধাপ ২ — পার্থক্য।**
- **Bug** → program ভুল ফল দেয় বা crash করে। এখনই ঠিক করতে হবে।
- **Smell** → program কাজ করে, কিন্তু code এলোমেলো (৩০০ line-এর একটা method, copy-paste করা logic)। পরের কষ্ট ঠেকাতে এটা ঠিক করুন।

```dart
// একটা smell (কাজ করে, কিন্তু একটা 'God' method অনেক বেশি কাজ করছে):
void handleOrder() { /* validate, charge, email, log... 200 lines */ }

// একটা bug (behaviour ভুল):
double total(double price, int qty) => price - qty; // price * qty হওয়া উচিত
```

**ধাপ ৩ — Smell কেন গুরুত্বপূর্ণ।**
Smell team-এর গতি কমিয়ে দেয়: এলোমেলো code পড়া, test করা আর বদলানো কঠিন। সময়ের সাথে এটা আসল bug তৈরি করে। Smell খুঁজে বের করা আর তার নাম বলতে পারা একটা senior skill।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি code-এর *quality* বিচার করতে পারেন কি না, শুধু ঠিক-ভুল নয়।

**সাধারণ ভুল:** Smell-কে bug (জরুরি crash) ভেবে নেওয়া, বা পুরোপুরি অগ্রাহ্য করা। এগুলো আগাম সতর্কবার্তা — ধীরে ধীরে নিয়মিত ঠিক করতে হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Smell-এর কিছু উদাহরণ দিন।"* → Long Method, Duplicate Code, Large Class, Magic Numbers (এই section-এ আছে)।

**সম্পর্কিত:** [Q2 — নিরাপদে refactor](#q2) · [Q4 — Long Method](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. আপনি কীভাবে নিরাপদে refactor করেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Refactoring মানে code-এর গঠন উন্নত করা, কিন্তু এটা কী করে সেটা না বদলে। নিরাপদে করার নিয়ম: আগে নিশ্চিত করুন test আছে, ছোট ছোট ধাপে বদলান, আর প্রতি ধাপের পরে test চালান। কোনো ধাপে test ভাঙলে শুধু ওই ছোট ধাপটুকু undo করবেন — সারাদিনের কাজ নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সোনার নিয়ম: behaviour বদলানো যাবে না।**
Refactoring শুধু code-এর *আকার* বদলায়। Input আর output হুবহু একই থাকে। Behaviour বদলে গেলে সেটা feature change বা bug, refactor নয়।

**ধাপ ২ — নিরাপদ process।**
1. **Test রাখুন** — এটাই আপনার safety net যে behaviour বদলায়নি।
2. **ছোট ধাপ** — আগে rename, তারপর extract, তারপর move — একবারে একটাই ছোট বদল।
3. **প্রতি ধাপের পরে test চালান** — ভুল সাথে সাথে ধরা পড়বে, যখন undo করা সহজ।
4. **ঘন ঘন commit করুন** — ছোট commit থাকলে roll back করা সহজ।

**ধাপ ৩ — ছোট ধাপ কেন গুরুত্বপূর্ণ।**
পুরো একটা file একসাথে refactor করলে আর test fail করলে আপনি জানবেন না কোন বদলটা এটা ভেঙেছে। ছোট ধাপে ভাঙা ধাপটা স্পষ্ট বোঝা যায়।

**ধাপ ৪ — যদি কোনো test না থাকে।**
আগে কয়েকটা "characterization test" লিখুন — যে test *বর্তমান* behaviour আটকে রাখে (সেটা অদ্ভুত হলেও)। তারপর ওই safety net নিয়ে refactor করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা শৃঙ্খলা যাচাই করে। বেপরোয়া refactoring production ভেঙে দেয়। নিরাপদ refactoring একটা senior অভ্যাস।

**সাধারণ ভুল:** একই commit-এ refactor করা আর feature যোগ করা — এখন আপনি বলতে পারবেন না কোন বদল bug এনেছে। দুটো আলাদা রাখুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"যদি কোনো test না থাকে?"* → আগে characterization test লিখুন, যাতে বর্তমান behaviour ধরা থাকে।

**সম্পর্কিত:** [Q3 — team-কে রাজি করানো](#q3) · [Q15 — Extract Method](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q3"></a>3. পুরোনো code refactor করতে team-কে কীভাবে রাজি করান?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"আমি refactoring-কে business value-র সাথে যুক্ত করি, 'clean code শুধু clean code-এর জন্য' বলি না। আমি দেখাই এলোমেলো অংশটা কীভাবে delivery ধীর করে বা bug তৈরি করে। তারপর feature-এর কাজের পাশাপাশি ছোট ও নিরাপদ ধাপে refactor করি — 'boy scout rule', code-টা যেমন পেয়েছেন তার চেয়ে একটু পরিষ্কার রেখে যান — বড় ঝুঁকির rewrite চাওয়ার বদলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Team-এর ভাষায় কথা বলুন: value, সৌন্দর্য নয়।**
Manager-রা delivery-র গতি, bug আর ঝুঁকি নিয়ে ভাবেন — "elegance" নিয়ে নয়। Refactoring-কে এভাবে বলুন: "এই module-টাই আমাদের বেশিরভাগ bug তৈরি করে আর বদলাতে কয়েক দিন লাগে; এটা পরিষ্কার করলে পরের feature গুলো দ্রুত হবে।"

**ধাপ ২ — প্রমাণ ব্যবহার করুন।**
বাস্তব সংকেত দেখান: ওই file-এ কতগুলো bug হয়েছে, সাম্প্রতিক বদল গুলোতে কত সময় লেগেছে, কতবার hotfix দিতে হয়েছে। মতামতের চেয়ে data বেশি কাজ করে।

**ধাপ ৩ — ধাপে ধাপে refactor করুন, big-bang rewrite নয়।**
বড় rewrite ঝুঁকির আর প্রায়ই ব্যর্থ হয়। বরং যে feature-এ হাত দেবেন সেখানেই একটু করে উন্নত করুন (**boy scout rule**: "code-টা যেমন পেয়েছেন তার চেয়ে পরিষ্কার রেখে যান")। এতে খরচ ভাগ হয়ে যায় আর ঝুঁকি কমে।

**ধাপ ৪ — কাজটা নিরাপদ করুন আর সবাইকে দেখান।**
Test-এর আড়ালে কাজটা করুন, ছোট PR-এ করুন, আর before/after উন্নতিটা দেখান। ছোট ছোট জয় আস্থা তৈরি করে — পরে বড় পরিষ্কারের কাজ সহজ হয়।

**Interviewer কেন জিজ্ঞেস করে:** Senior engineer-রা team-কে প্রভাবিত করেন। এটা যোগাযোগ আর বাস্তববুদ্ধি যাচাই করে, শুধু coding নয়।

**সাধারণ ভুল:** বলা যে "সব কিছু rewrite করতে দুই সপ্তাহ feature বন্ধ রাখুন।" এতে stakeholder-রা ভয় পান আর প্রস্তাবটা সাধারণত বাতিল হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Boy scout rule কী?"* → Code-টা যেমন পেয়েছেন তার চেয়ে সবসময় একটু পরিষ্কার রেখে যান — ছোট ছোট উন্নতি চলতেই থাকে।

**সম্পর্কিত:** [Q2 — নিরাপদে refactor](#q2) · [Q26 — Strangler Fig](#q26)

[↑ উপরে ফিরুন](#toc)

---

# B. Bloater smells

---

## <a id="q4"></a>4. Long Method কী, আর এটা কীভাবে ঠিক করবেন?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Long Method এক জায়গায় অনেক বেশি কাজ করার চেষ্টা করে। তাই এটা পড়া আর test করা কঠিন। সমাধান হলো Extract Method — প্রতিটা আলাদা কাজকে নিজের ছোট, ভালো নামের method-এ সরিয়ে নিন। ভালো method একটা কাজ করে, আর ছোট একটা paragraph-এর মতো পড়া যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা কী।**
যে method কয়েক screen ধরে scroll করে, আর ভেতরে `// now validate`, `// now save` মতো comment দিয়ে অংশ ভাগ করা থাকে — প্রতিটা comment একটা ইশারা যে ভেতরে একটা method লুকিয়ে আছে।

**ধাপ ২ — আগে: একটা লম্বা method।**

```dart
void checkout(Cart cart) {
  // validate
  if (cart.items.isEmpty) throw Exception('empty');
  // total হিসাব
  var total = 0.0;
  for (final i in cart.items) total += i.price * i.qty;
  // discount বসানো
  if (total > 100) total *= 0.9;
  // ... charge, email, log ...
}
```

**ধাপ ৩ — পরে: প্রতিটা কাজ আলাদা করে নিন।**

```dart
void checkout(Cart cart) {
  _validate(cart);
  final total = _applyDiscount(_calculateTotal(cart));
  _charge(total);
}

void _validate(Cart cart) { if (cart.items.isEmpty) throw Exception('empty'); }
double _calculateTotal(Cart cart) =>
    cart.items.fold(0.0, (s, i) => s + i.price * i.qty);
double _applyDiscount(double total) => total > 100 ? total * 0.9 : total;
```

এখন `checkout` একটা সারাংশের মতো পড়া যায়। আর প্রতিটা অংশ আলাদাভাবে test করা যায়।

**Interviewer কেন জিজ্ঞেস করে:** Long method সবচেয়ে সাধারণ smell। তাঁরা দেখেন আপনি কাজকে ছোট ছোট নামওয়ালা অংশে ভাগ করতে পারেন কি না।

**সাধারণ ভুল:** চোখ বন্ধ করে extract করা, ফলে ছোট method-গুলো একে অপরের সাথে শক্তভাবে জড়িয়ে যায়। প্রতিটা extract করা method নিজে নিজেই অর্থবহ হওয়া উচিত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কতটা লম্বা হলে বেশি লম্বা?"* → line গুনে নয়, একটা কাজ করছে কি না তা দিয়ে বুঝুন। যদি section comment লাগে, তাহলে এটা বেশি লম্বা।

**সম্পর্কিত:** [Q15 — Extract Method (কীভাবে)](#q15) · [Q5 — Large Class](#q5)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Large Class (God Object) কী, আর এটা কীভাবে ঠিক করবেন?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Large Class, বা God Object, অনেক বেশি জানে আর অনেক বেশি কাজ করে — এতে অনেক সম্পর্ক নেই এমন field আর method থাকে। এটা Single Responsibility Principle ভাঙে। সমাধান হলো Extract Class: এটাকে ছোট ছোট class-এ ভাগ করুন, প্রতিটার একটা স্পষ্ট কাজ থাকবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা কী।**
একটা `User` class যেটা profile data রাখে *এবং* email পাঠায় *এবং* database-এর সাথে কথা বলে *এবং* date format করে। এই প্রতিটা কারণেই class-টা বদলাতে হতে পারে।

**ধাপ ২ — আগে: একটা God class।**

```dart
class User {
  String name = '';
  void saveToDb() {/* db code */}
  void sendEmail() {/* email code */}
  String formatJoinDate() {/* date code */}
}
```

**ধাপ ৩ — পরে: দায়িত্ব ভাগ করে দিন।**

```dart
class User { String name = ''; }
class UserRepository { void save(User u) {/* db */} }
class EmailService { void sendWelcome(User u) {/* email */} }
```

এখন প্রতিটা class-এর বদলানোর একটাই কারণ (high cohesion, [SRP](section-12-oop-principles-bn.md#q10))।

**Interviewer কেন জিজ্ঞেস করে:** God object হলো unmaintainable code-এর অন্যতম বড় কারণ। তাঁরা দেখেন আপনি SRP কাজে লাগাতে পারেন কি না।

**সাধারণ ভুল:** ছোট একটা app-এ কয়েক ডজন ক্ষুদ্র class বানিয়ে বেশি ভাগ করে ফেলা। ভাগ করুন *দায়িত্ব* অনুযায়ী, line সংখ্যা অনুযায়ী নয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কোন method-গুলো extract করবেন, সেটা কীভাবে বোঝেন?"* → যে field আর method একসাথে বদলায়, তাদের একসাথে রাখুন; প্রতিটা group একটা class হবে।

**সম্পর্কিত:** [Q16 — Extract Class (কীভাবে)](#q16) · [Q4 — Long Method](#q4)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. Long Parameter List কী, আর এটা কীভাবে ঠিক করবেন?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Long Parameter List মানে একটা method অনেক বেশি argument নেয়। এটা পড়া কঠিন, আর ভুল order-এ পাঠিয়ে ফেলা সহজ। সমাধান হলো Introduce Parameter Object — সম্পর্কিত parameter-গুলো একটা ছোট object-এ রাখুন। Dart-এ named parameter-ও অনেক সাহায্য করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা কী।**

```dart
void createUser(String first, String last, String street, String city, String zip, String country) {}
// ছয়টা positional arg — গুলিয়ে ফেলা সহজ; order-টা যেন কী ছিল?
```

**ধাপ ২ — সমাধান: সম্পর্কিতগুলো এক object-এ রাখুন।**

```dart
class Address {
  final String street, city, zip, country;
  Address(this.street, this.city, this.zip, this.country);
}

void createUser(String first, String last, Address address) {} // স্পষ্ট group
```

**ধাপ ৩ — Dart-এর বাড়তি সাহায্য: named parameter।**
Parameter object ছাড়াও named parameter order-এর ঝুঁকি সরিয়ে দেয়:

```dart
void createUser({required String first, required String last, required Address address}) {}
```

**Interviewer কেন জিজ্ঞেস করে:** এটা পড়ার উপযোগী API design যাচাই করে। আর কোন data একসাথে থাকা উচিত, সেটা আপনি বুঝতে পারেন কি না তাও দেখে।

**সাধারণ ভুল:** শুধু তালিকা ছোট করার জন্য সম্পর্ক নেই এমন parameter একসাথে এক object-এ ঢুকিয়ে দেওয়া — শুধু সেগুলোই একসাথে রাখুন যেগুলো সত্যিই একসাথে থাকে (দেখুন [Data Clumps](#q7))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কখন parameter object বানানো লাভজনক?"* → যখন একই parameter group কয়েকটা method-এ একসাথে ঘুরে বেড়ায়।

**সম্পর্কিত:** [Q20 — Introduce Parameter Object (কীভাবে)](#q20) · [Q7 — Data Clumps](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q7"></a>7. Data Clumps কী, আর এগুলো কীভাবে ঠিক করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Data Clumps হলো একই group-এর variable যেগুলো বারবার একসাথে আসে — যেমন `startDate` আর `endDate`, বা সব জায়গায় `x` আর `y`। এটা ইশারা দেয় যে এগুলো একটা object হওয়া উচিত। সমাধান হলো clump-টাকে একটা ছোট class-এ মুড়ে দেওয়া। এতে সম্পর্কিত behaviour-এরও একটা ঘর হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell: একই তিনজন সব জায়গায় একসাথে ঘোরে।**

```dart
void book(DateTime start, DateTime end) {}
bool overlaps(DateTime start, DateTime end, DateTime start2, DateTime end2) {}
// start + end বারবার জোড়া হয়ে আসছে
```

**ধাপ ২ — সমাধান: clump-টাকে একটা class বানান।**

```dart
class DateRange {
  final DateTime start, end;
  DateRange(this.start, this.end);
  bool overlaps(DateRange other) => start.isBefore(other.end) && other.start.isBefore(end);
}

void book(DateRange range) {}
```

এখন জোড়াটা একটাই concept। আর `overlaps`-এর মতো behaviour ঠিক জায়গায় থাকে।

**ধাপ ৩ — এটা কেন কাজে লাগে।**
এটা বারবার একই জিনিস সরিয়ে দেয়, signature ছোট করে, আর সম্পর্কিত logic-এর একটা জায়গা দেয় — ছড়ানো data-কে অর্থবহ object-এ পরিণত করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি আলগা variable-এর ভেতরে লুকিয়ে থাকা concept (একটা `DateRange`, একটা `Money`) খেয়াল করেন কি না।

**সাধারণ ভুল:** clump-টাকে ছড়ানো অবস্থায় রেখে দেওয়া। ফলে যেখানেই জোড়াটা আসে, সেখানেই একই validation/logic নকল হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Data Clumps আর Primitive Obsession-এর পার্থক্য?"* → Clumps = একটা *group* যেটা একসাথে থাকে; Primitive Obsession = *একটা* primitive যেটা typed value object হওয়া উচিত ([Q8](#q8))।

**সম্পর্কিত:** [Q6 — Long Parameter List](#q6) · [Q8 — Primitive Obsession](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Primitive Obsession কী, আর value object দিয়ে এটা কীভাবে ঠিক করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Primitive Obsession মানে এমন concept-এর জন্য raw primitive (String, int) ব্যবহার করা, যার নিজের একটা type প্রাপ্য — যেমন email-এর জন্য `String`, বা টাকার জন্য `int`। সমাধান হলো value object: একটা ছোট class, যেটা primitive-টাকে মুড়ে রাখে আর তার নিয়ম কাজে লাগায়। ফলে ভুল value থাকতেই পারে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা।**

```dart
void sendEmail(String email) {} // যেকোনো string পাস হয় — এমনকি "not-an-email"
double price = 999;             // এটা কি dollar? cent? টাকা?
```

Type-টা অর্থ বা নিয়ম কোনোটাই বহন করে না।

**ধাপ ২ — সমাধান: একটা value object যেটা validate করে।**

```dart
class Email {
  final String value;
  Email(this.value) {
    if (!value.contains('@')) throw ArgumentError('invalid email');
  }
}

void sendEmail(Email email) {} // এখন শুধু বৈধ Email-ই পাস করা যাবে
```

**ধাপ ৩ — কেন এটা সাহায্য করে।**
- ভুল state আর সম্ভব থাকে না (validation একটাই জায়গায় থাকে)।
- Type নিজেই অর্থ বলে দেয় (`Money`, `Email`, `PhoneNumber`)।
- সম্পর্কিত behaviour-এর একটা ঘর পায় (`Money.add`, `Email.domain`)।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি type system-কে দিয়ে নিজেকে রক্ষা করেন কি না। নাকি একই primitive সব জায়গায় validate করতে থাকেন।

**সাধারণ ভুল:** প্রতিটা primitive-কে value object-এ মুড়ে ফেলা, এমনকি তুচ্ছগুলোকেও — এতে শুধু noise বাড়ে। যেসব concept-এর সত্যিকারের নিয়ম বা behaviour আছে, সেগুলোর জন্য ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"আপনি কোথায় এটা ব্যবহার করেছেন?"* → `Money`, `Email`, `UserId` — যেখানেই validation বা unit আছে।

**সম্পর্কিত:** [Q7 — Data Clumps](#q7) · [Q10 — Magic Numbers](#q10)

[↑ উপরে ফিরুন](#toc)

---

# C. Duplication ও অকেজো ভার

---

## <a id="q9"></a>9. Duplicate Code কী, আর এটা কীভাবে ঠিক করবেন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Duplicate Code মানে একই logic কয়েক জায়গায় copy-paste করা। এটা বিপজ্জনক, কারণ একটা পরিবর্তন মানে প্রতিটা copy ঠিক করা, আর একটা আপনি মিস করবেনই। সমাধান হলো শেয়ার করা logic-টা একটা function বা class-এ টেনে আনা — DRY principle। তবে সাবধান, শুধু সেই code-ই একসাথে করুন যেটা একই *knowledge* বোঝায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা।**

```dart
double priceA(double p) => p - (p * 0.1);
double priceB(double p) => p - (p * 0.1); // একই logic, দুই জায়গায়
```

**ধাপ ২ — সমাধান: একটাই source of truth।**

```dart
double applyDiscount(double price, double rate) => price - (price * rate);
```

নিয়মটা একবার বদলান; সব জায়গায় update হয়ে যায়।

**ধাপ ৩ — সতর্কতা।**
আজ *দেখতে* এক লাগছে বলেই code একসাথে করে দেবেন না। দুটো অংশ যদি আলাদা নিয়ম বোঝায়, আর কাকতালীয়ভাবে মিলে যায়, তাহলে জোর করে মেলালে খারাপ coupling তৈরি হয়। DRY-এর কথা হলো duplicate *knowledge* সরানো, দেখতে-এক line সরানো নয়।

**Interviewer কেন জিজ্ঞেস করে:** Duplication সবচেয়ে সাধারণ, সবচেয়ে ক্ষতিকর smell। তাঁরা দেখেন আপনি এটা সঠিক উপায়ে ঠিক করেন কি না।

**সাধারণ ভুল:** বেশি DRY করা — সম্পর্ক নেই এমন code একসাথে করে অনেক flag-ওয়ালা একটা জট পাকানো function বানানো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"DRY-এর খারাপ দিক?"* → খুব আগে merge করলে এমন জিনিস coupled হয়ে যায় যেগুলোর আলাদা করে বেড়ে ওঠা উচিত; সামান্য duplication কখনো কখনো বেশি স্বাস্থ্যকর।

**সম্পর্কিত:** [Q15 — Extract Method](#q15) · [Q12 (OOP) — DRY](section-12-oop-principles-bn.md#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Magic Number আর Magic String কী, আর এগুলো কীভাবে ঠিক করবেন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Magic number আর string হলো code-এর মধ্যে ছড়িয়ে থাকা ব্যাখ্যাহীন literal value, যেমন `if (status == 3)` বা `'admin'`। এগুলোর মানে কেউ জানে না, আর একটা বদলাতে হলে পুরো codebase খুঁজতে হয়। সমাধান হলো এগুলোকে named constant বা enum দিয়ে বদলে দেওয়া।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা।**

```dart
if (user.role == 1) {}          // 1 মানে কী?
if (status == 'A') {}           // 'A' মানে কী?
final price = total * 0.15;     // 0.15 হলো... tax? discount?
```

**ধাপ ২ — সমাধান: এগুলোর নাম দিন।**

```dart
const taxRate = 0.15;
final price = total * taxRate;  // এখন স্পষ্ট

enum Role { user, admin, owner } // নির্দিষ্ট সেটের জন্য constant-এর চেয়েও ভালো
if (user.role == Role.admin) {}
```

**ধাপ ৩ — কেন এটা সাহায্য করে।**
- নামটাই অর্থ বুঝিয়ে দেয়।
- Value একটাই জায়গায় বদলান।
- একটা typo চুপচাপ bug না হয়ে compile error হয়ে যায় (enum হলে)।

**Interviewer কেন জিজ্ঞেস করে:** এটা readability-র একটা গোড়ার অভ্যাস, যা তাঁরা প্রতিটা engineer-এর কাছে আশা করেন।

**সাধারণ ভুল:** সত্যিই স্পষ্ট value-রও নাম দেওয়া (দ্বিগুণ করার জন্য `* 2`) — এতে noise বাড়ে। যে value *অর্থ* বহন করে, তার নাম দিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Constant না enum?"* → সম্পর্কিত option-এর একটা নির্দিষ্ট সেটের জন্য enum (role, status); একটামাত্র নামওয়ালা value-র জন্য constant।

**সম্পর্কিত:** [Q22 — Replace Magic Number with Named Constant](#q22) · [Q8 — Primitive Obsession](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q11"></a>11. Dead Code কী, আর এটা কেন বিপজ্জনক?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dead code হলো এমন code যা কখনো ব্যবহার হয় না — অব্যবহৃত function, variable, comment করে রাখা block, বা যেখানে পৌঁছানোই যায় না এমন branch। এটা বিপজ্জনক, কারণ পাঠককে বিভ্রান্ত করে, আসল logic ঢেকে দেয়, আর সময়ের সাথে পচে যায়। সমাধান সহজ: মুছে দিন। কখনো ফেরত লাগলে version control মনে রেখেছে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা।**

```dart
// final oldDiscount = 0.2; // এটা আর ব্যবহার করি না
void unusedHelper() {}      // কখনো call হয় না
if (false) { doThing(); }   // এখানে পৌঁছানো যায় না
```

**ধাপ ২ — কেন এটা বিপজ্জনক।**
- পাঠক সময় নষ্ট করেন এটা বুঝতে যে জিনিসটা আদৌ দরকারি কি না।
- এটা bug ঢেকে রাখতে পারে (আপনি dead code "ঠিক" করেন, ভেবে যে এটা চলে)।
- এটা পুরোনো হয়ে যায় আর ভুল বার্তা দেয়।

**ধাপ ৩ — সমাধান: মুছে দিন।**
"দরকার হতে পারে" ভেবে comment করে রাখবেন না — এটাই সবচেয়ে খারাপ। Git history রাখে; আপনি যেকোনো কিছু ফেরত আনতে পারবেন।

```dart
// অব্যবহৃত অংশগুলো শুধু মুছে দিন। Codebase হালকা আর পরিষ্কার হয়।
```

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি codebase পরিষ্কার রাখেন কি না, আর version control-কে বিশ্বাস করেন কি না।

**সাধারণ ভুল:** "রেফারেন্সের জন্য" comment করা code-এর বড় বড় block রেখে দেওয়া। এগুলো পচে যায় আর জঞ্জাল বাড়ায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Dead code কীভাবে খুঁজে বের করেন?"* → IDE warning, linter (`dart analyze`), আর coverage report।

**সম্পর্কিত:** [Q2 — নিরাপদে refactor](#q2) · [Q12 — smell হিসেবে comment](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Comment কখন একটা code smell হয়ে যায়?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Comment তখনই smell হয়, যখন খারাপভাবে লেখা code *কী* করে সেটা comment ব্যাখ্যা করে, code নিজে নিজেকে ব্যাখ্যা করার বদলে। যে comment code-টাই আবার বলে, বা এলোমেলো logic-এর জন্য ক্ষমা চায়, সেটা সাধারণত মানে code-টা refactor করা দরকার। ভালো comment *কেন* ব্যাখ্যা করে, *কী* নয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — খারাপ comment: অস্পষ্ট code ব্যাখ্যা করা।**

```dart
// user প্রাপ্তবয়স্ক কি না check করি
if (u.a >= 18) {} // comment-টা আছে কারণ code-টা বোঝা কঠিন
```

**ধাপ ২ — সমাধান: code-কেই নিজে-ব্যাখ্যাকারী বানান।**

```dart
if (user.isAdult) {} // কোনো comment লাগে না — নামই বলে দেয়
```

ভালো নামের একটা method বা variable extract করুন, comment-টা নিজেই উধাও হয়ে যাবে।

**ধাপ ৩ — Comment কখন ভালো।**
- **কেন** সেটা ব্যাখ্যা করা (অস্পষ্ট একটা সিদ্ধান্ত, একটা workaround, একটা business rule)।
- সতর্কবার্তা ("এটা X-এর আগে চলতে হবে")।
- Public API doc।

```dart
// Stripe half-up round করে, তাই off-by-one refund এড়াতে আমরাও তাই করি।
final cents = (amount * 100).round();
```

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি comment-এর উপর ভর না দিয়ে self-documenting code লেখেন কি না।

**সাধারণ ভুল:** এমন comment লেখা যা code-টাই আবার বলে (`i++; // increment i`), যা শুধু noise বাড়ায় আর পুরোনো হয়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ভালো comment কোনটা?"* → যেটা *কেন* ব্যাখ্যা করে, উদ্দেশ্য ধরে রাখে, বা সতর্ক করে — যা code নিজে বলতে পারে না।

**সম্পর্কিত:** [Q16 (Clean Code) — comments](section-16-clean-code-bn.md#q1) · [Q15 — Extract Method](#q15)

[↑ উপরে ফিরুন](#toc)

---

# D. Coupling smells

---

## <a id="q13"></a>13. Feature Envy কী, আর এটা কীভাবে ঠিক করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Feature Envy হলো যখন একটা method নিজের class-এর data-র চেয়ে অন্য class-এর data নিয়ে বেশি আগ্রহী — কাজ করতে গিয়ে সে বারবার অন্য object-এর field-এ হাত দেয়। সমাধান হলো Move Method: ওই logic-টা সেই class-এ সরিয়ে নিন যে data-র মালিক। তাহলে behaviour তার নিজের data-র পাশেই থাকে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell-টা।**

```dart
class Order {
  double total(Customer c) {
    // এই method বারবার Customer-এর field-এ হাত দিচ্ছে
    return c.cartSubtotal * (1 - c.loyaltyDiscount) + c.shippingFee;
  }
}
```

`Order.total` বেশিরভাগ `Customer` data ব্যবহার করছে — সে `Customer`-এর feature-গুলোকে হিংসা করছে।

**ধাপ ২ — সমাধান: logic-টা data যেখানে আছে সেখানে সরান।**

```dart
class Customer {
  double cartSubtotal = 0, loyaltyDiscount = 0, shippingFee = 0;
  double total() => cartSubtotal * (1 - loyaltyDiscount) + shippingFee; // এখন এখানে
}
```

**ধাপ ৩ — মূল ভাবনা।**
"যে data নিয়ে কাজ, behaviour তার পাশেই রাখুন।" এতে coupling কমে — class-গুলো একে অন্যের ভেতরে হাত দেওয়া বন্ধ করে।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি logic ঠিক জায়গায় রাখেন কি না। এটা ভালো object design-এর লক্ষণ।

**সাধারণ ভুল:** method-টা যেখানে আছে সেখানেই রেখে অন্য class থেকে আরও getter খুলে দেওয়া। এতে সমস্যা ঠিক হয় না, উল্টো coupling বাড়ে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"অন্য class-এ হাত দেওয়া কখন ঠিক আছে?"* → কখনো কখনো ঠিক আছে (যেমন একটা coordinator/service)। কিন্তু একটা method যদি বেশিরভাগ অন্য class-এর data ব্যবহার করে, তাহলে সেটা সরিয়ে দিন।

**সম্পর্কিত:** [Q18 — Move Method (কীভাবে)](#q18) · [Q14 — Shotgun Surgery](#q14)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. Shotgun Surgery কী, আর Divergent Change থেকে এটা কীভাবে আলাদা?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Shotgun Surgery হলো যখন একটা ছোট পরিবর্তনের জন্য অনেক আলাদা class-এ edit করতে হয় — logic ছড়িয়ে আছে। Divergent Change ঠিক উল্টো: একটা class-কে অনেক আলাদা কারণে বদলাতে হয়। Shotgun Surgery মানে 'খুব বেশি ছড়ানো'; Divergent Change মানে 'এক জায়গায় খুব বেশি'।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Shotgun Surgery — এক পরিবর্তন, অনেক file।**
উদাহরণ: tax কীভাবে হিসাব হয় সেটা বদলাতে গেলে ৮টা আলাদা class edit করতে হয়, কারণ প্রত্যেকে নিজের মতো tax-এর হিসাব করে। সমাধান হলো ছড়ানো logic-কে এক জায়গায় **জড়ো করা** (একটা `TaxCalculator`)।

**ধাপ ২ — Divergent Change — এক class, অনেক কারণ।**
উদাহরণ: একটা `UserManager`-কে বদলাতে হয় UI বদলালে, database বদলালে, আর email-এর নিয়ম বদলালে। সমাধান হলো দায়িত্ব অনুযায়ী সেটাকে **ভাগ করা** (Extract Class, [SRP](section-12-oop-principles-bn.md#q10))।

**ধাপ ৩ — সহজে মনে রাখার উপায়।**

| Smell | সমস্যা | সমাধান |
|---|---|---|
| Shotgun Surgery | এক পরিবর্তন → অনেক class (খুব ছড়ানো) | logic এক class-এ জড়ো করুন |
| Divergent Change | এক class → অনেক কারণ (খুব ভিড়) | class-টা ভাগ করুন |

এরা একে অন্যের আয়নার ছবি: একটা খুব বেশি ছড়ানো, অন্যটা খুব বেশি এক জায়গায় জমা।

**Interviewer কেন জিজ্ঞেস করে:** এই দুটো নিয়ে মানুষ প্রায়ই গুলিয়ে ফেলে। পার্থক্যটা ব্যাখ্যা করলে বোঝা যায় আপনি cohesion আর coupling সত্যিই বোঝেন।

**সাধারণ ভুল:** দুটোকে মিলিয়ে ফেলা। মনে রাখুন: shotgun = ছড়ানো (জড়ো করুন); divergent = ভিড় (ভাগ করুন)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"দুটোই কোন principle-এর সাথে যুক্ত?"* → দুটোই cohesion নিয়ে — সম্পর্কিত জিনিস একসাথে রাখা, আর অসম্পর্কিত জিনিস আলাদা রাখা।

**সম্পর্কিত:** [Q5 — Large Class](#q5) · [Q13 — Feature Envy](#q13) · [Q9 (coupling/cohesion)](section-12-oop-principles-bn.md#q9)

[↑ উপরে ফিরুন](#toc)

---

# E. Refactoring techniques

---

## <a id="q15"></a>15. Extract Method — কীভাবে আর কখন?

> Very common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Extract Method একটা code-এর টুকরো নিয়ে সেটাকে ভালো নামের আলাদা method বানায়। এটা করবেন যখন কোনো code-এর অংশ একটা আলাদা করে চেনা যায় এমন কাজ করে। অথবা যখন ওই block ব্যাখ্যা করতে আপনাকে একটা comment লিখতে হতো। তখন method-এর নামটাই comment-এর জায়গা নেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কখন ব্যবহার করবেন।**
- একটা method খুব লম্বা ([Q4](#q4))।
- একটা block-এর জন্য `// explanation` comment দরকার।
- একই কয়েকটা line দুই জায়গায় আছে।

**ধাপ ২ — কীভাবে (আগে/পরে)।**

```dart
// আগে
void printReport(List<Order> orders) {
  // total হিসাব করা
  var total = 0.0;
  for (final o in orders) total += o.amount;
  print('Total: $total');
}

// পরে — comment-টাই method-এর নাম হয়ে গেল
void printReport(List<Order> orders) {
  print('Total: ${_calculateTotal(orders)}');
}
double _calculateTotal(List<Order> orders) =>
    orders.fold(0.0, (s, o) => s + o.amount);
```

**ধাপ ৩ — নিরাপদে করুন।**
Extract করুন, test চালান, আবার করুন। আধুনিক IDE "Extract Method" নিজে থেকেই নিরাপদে করে দেয় — সেটাই ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটাই সবচেয়ে বেশি ব্যবহার করা refactoring, আর লম্বা method-এর ওষুধ।

**সাধারণ ভুল:** extract করা method-কে অস্পষ্ট নাম দেওয়া (`_doStuff`)। নামটা ঠিক কী কাজ করে সেটাই বলা উচিত।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Extract Method-এর উল্টোটা কী?"* → Inline Method ([Q17](#q17)) — যে method শুধু মানে নেই এমন indirection, সেটা সরিয়ে দেওয়া।

**সম্পর্কিত:** [Q4 — Long Method](#q4) · [Q17 — Inline Method](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Extract Class — কীভাবে আর কখন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Extract Class একটা class-কে ভাগ করে, যেটা দুটো কাজ করছে, দুটো class-এ। এটা করবেন যখন একটা class খুব বড় হয়ে গেছে। অথবা যখন তার কিছু field আর method স্পষ্টভাবে নিজেরাই একটা আলাদা concept। God Object-এর মূল সমাধান এটাই।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কখন ব্যবহার করবেন।**
একটা class-এ field/method-এর দুটো আলাদা গুচ্ছ আছে, যারা আলাদা কারণে বদলায় — এটা লুকিয়ে থাকা দ্বিতীয় class-এর লক্ষণ।

**ধাপ ২ — কীভাবে (আগে/পরে)।**

```dart
// আগে — Person phone-এর খুঁটিনাটিও সামলাচ্ছে
class Person {
  String name = '';
  String areaCode = '';
  String number = '';
  String phoneNumber() => '($areaCode) $number';
}

// পরে — phone নিজেই একটা class হলো
class Person {
  String name = '';
  Phone phone = Phone('', '');
}
class Phone {
  final String areaCode, number;
  Phone(this.areaCode, this.number);
  String formatted() => '($areaCode) $number';
}
```

**ধাপ ৩ — ধীরে ধীরে করুন।**
নতুন class বানান, একবারে একটা field/method সরান, test চালান, আবার করুন — ছোট নিরাপদ ধাপে।

**Interviewer কেন জিজ্ঞেস করে:** ফুলে যাওয়া class-এ SRP কাজে লাগানোর বাস্তব হাতিয়ার এটাই।

**সাধারণ ভুল:** এমনভাবে ভাগ করা যে নতুন class-গুলো এখনো একে অন্যের উপর অনেক নির্ভর করে। এমন একটা পরিষ্কার জোড়া খুঁজুন, যেখানে নতুন class মোটামুটি স্বাধীন থাকে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"জোড়াটা কীভাবে খুঁজে পাবেন?"* → এমন field আর method খুঁজুন যেগুলো একসাথে ব্যবহার হয়, আর বাকি অংশ সেগুলো ব্যবহার করে না।

**সম্পর্কিত:** [Q5 — Large Class](#q5) · [Q18 — Move Method](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q17"></a>17. Inline Method — একটা method কখন দরকার নেই এমন indirection?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Inline Method হলো Extract Method-এর উল্টো: যখন একটা method-এর body তার নামের মতোই পরিষ্কার আর কোনো মূল্য যোগ করে না, তখন call-গুলোর জায়গায় body বসিয়ে method-টা মুছে দিন। এটা করবেন মানে নেই এমন indirection সরাতে, যেটা code বুঝতে কঠিন করে তোলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell: যে method কিছুই যোগ করে না।**

```dart
// আগে — method শুধু একটা তুচ্ছ expression মুড়ে রেখেছে
int getRating(Driver d) => moreThanFiveLateDeliveries(d) ? 2 : 1;
bool moreThanFiveLateDeliveries(Driver d) => d.lateDeliveries > 5;
```

**ধাপ ২ — পরে: inline করে দিন।**

```dart
int getRating(Driver d) => d.lateDeliveries > 5 ? 2 : 1;
```

বাড়তি method-টা কিছুই পরিষ্কার করেনি। তাই সেটা সরালে code সহজ হয়।

**ধাপ ৩ — কখন inline করবেন না।**
Method-এর নাম যদি অর্থ যোগ করে, অনেক জায়গায় ব্যবহার হয়, বা override করা যেতে পারে — তাহলে সেটা রেখে দিন। indirection সত্যিই মানে নেই এমন হলে তবেই inline করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখায় আপনি "পরিষ্কার করতে extract" আর "বেশি টুকরো করবেন না" — দুটোর মাঝে balance রাখেন। দুই দিকই গুরুত্বপূর্ণ।

**সাধারণ ভুল:** এমন method inline করা যেটা অনেক জায়গায় ব্যবহার হয় বা উদ্দেশ্য বুঝিয়ে দেয় — এতে পড়ার সুবিধা নষ্ট হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কখন extract, কখন inline?"* → Extract করুন যখন একটা block-এর একটা নাম দরকার; inline করুন যখন method কোনো অর্থ যোগ করে না।

**সম্পর্কিত:** [Q15 — Extract Method](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. Move Method — কীভাবে আর কখন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Move Method একটা method-কে সেই class-এ সরিয়ে নেয়, যার data সে বেশি ব্যবহার করে। এটা করি Feature Envy ঠিক করতে। আর behaviour-কে তার data-র পাশে রাখতে। এতে class-গুলোর মধ্যে coupling কমে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কখন ব্যবহার করবেন।**
একটা method নিজের field-এর চেয়ে অন্য class-এর field বেশি ব্যবহার করে ([Feature Envy](#q13))। অথবা সেটা স্পষ্টভাবে অন্য জায়গায় বেশি মানায়।

**ধাপ ২ — কীভাবে (আগে/পরে)।**

```dart
// আগে — discount logic আছে Order-এ, কিন্তু ব্যবহার করে Account
class Order {
  double discount(Account account) => account.isPremium ? 0.2 : 0.0;
}

// পরে — Account-এ সরানো হলো, যেখানে data থাকে
class Account {
  bool isPremium = false;
  double discount() => isPremium ? 0.2 : 0.0;
}
```

**ধাপ ৩ — নিরাপদে করুন।**
Method-টা target class-এ copy করুন, reference ঠিক করুন, caller-গুলো update করুন, test চালান, তারপর পুরোনোটা মুছে দিন।

**Interviewer কেন জিজ্ঞেস করে:** এটা Feature Envy-র সরাসরি সমাধান। আর এটা behaviour-এর সঠিক জায়গা বাছার ক্ষমতা যাচাই করে।

**সাধারণ ভুল:** Method সরানো, কিন্তু caller-গুলো এখনো এক class থেকে আরেক class-এ হাত বাড়ায়। এতে coupling আসলে কমে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"সঠিক ঘর কোনটা, সেটা কীভাবে ঠিক করেন?"* → যে class-এর data method-টা সবচেয়ে বেশি ব্যবহার করে।

**সম্পর্কিত:** [Q13 — Feature Envy](#q13) · [Q16 — Extract Class](#q16)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q19"></a>19. কোনো method, variable বা class কীভাবে নিরাপদে Rename করবেন?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Rename করা সবচেয়ে সহজ, আর সবচেয়ে বেশি লাভের refactoring — একটা পরিষ্কার নাম comment-এর দরকারই মুছে দেয়। নিরাপদে করতে IDE-র Rename refactoring ব্যবহার করি, যাতে সব reference একসাথে update হয়। তারপর test চালাই। কখনোই find-and-replace text দিয়ে rename করি না, কারণ সেটা সম্পর্ক নেই এমন জায়গাতেও লেগে যেতে পারে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Rename কেন গুরুত্বপূর্ণ।**
অস্পষ্ট নাম (`data`, `temp`, `flag`, `process()`) পাঠককে খুঁড়তে বাধ্য করে। পরিষ্কার নাম (`unpaidInvoices`, `isExpired`, `sendReceipt()`) নিজেই নিজেকে ব্যাখ্যা করে। ভালো নাম হলো সবচেয়ে সস্তা documentation।

**ধাপ ২ — নিরাপদ পথ: IDE rename।**
IDE-র "Rename" code বোঝে। তাই এটা প্রতিটা আসল reference update করে (আর শুধু সেগুলোই)। সম্পর্ক নেই এমন text-এ হাত দেয় না।

```dart
// আগে
var d = users.where((u) => u.active).toList();
// পরে (স্পষ্টতার জন্য rename করা)
var activeUsers = users.where((u) => u.active).toList();
```

**ধাপ ৩ — Text find-and-replace এড়িয়ে চলুন।**
সাধারণ text replace একটা comment, একটা string, বা একই নামের অন্য একটা variable বদলে দিতে পারে। Language-aware rename ব্যবহার করুন। আর পরে test চালান।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি পরিষ্কার নামকে মূল্য দেন কি না, আর নিরাপদ tooling ব্যবহার করেন কি না।

**সাধারণ ভুল:** কাঁচা find-and-replace দিয়ে rename করা, আর ভুল করে সম্পর্ক নেই এমন code বা string বদলে ফেলা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"ভালো নাম কেমন হয়?"* → যেটা উদ্দেশ্য বলে দেয়: জিনিসটা কী বা কী করে, কোনো সংক্ষিপ্ত রূপ নেই, কোনো comment-এর দরকার নেই।

**সম্পর্কিত:** [Q12 — smell হিসেবে comment](#q12) · [Q1 (Clean Code) — naming](section-16-clean-code-bn.md#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q20"></a>20. Introduce Parameter Object — কখন আর কীভাবে?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q20)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Introduce Parameter Object একসাথে চলা কয়েকটা parameter-কে একটা object-এ জড়ো করে। এটা ব্যবহার করি লম্বা parameter list ছোট করতে। আর দলটাকে একটা নাম দিতে, আর সম্পর্কিত behaviour-এর জন্য একটা ঘর দিতে। এটাই Long Parameter List আর Data Clumps-এর সমাধান।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কখন ব্যবহার করবেন।**
একই parameter-এর সেট একের বেশি method signature-এ দেখা যায়। অথবা একটা method খুব বেশি argument নেয়।

**ধাপ ২ — কীভাবে (আগে/পরে)।**

```dart
// আগে
double amountInvoiced(DateTime start, DateTime end) => 0;
double amountReceived(DateTime start, DateTime end) => 0;

// পরে — জোড়াটাকে একটা DateRange-এ জড়ো করা হলো
class DateRange {
  final DateTime start, end;
  DateRange(this.start, this.end);
  int get days => end.difference(start).inDays; // behaviour এখন একটা ঘর পেল
}
double amountInvoiced(DateRange range) => 0;
double amountReceived(DateRange range) => 0;
```

**ধাপ ৩ — বাড়তি লাভ।**
Parameter-গুলো একবার object হয়ে গেলে, সম্পর্কিত logic সেটার উপরে সরাতে পারবেন (উপরের `days`-এর মতো)। এতে প্রায়ই আরও refactoring-এর সুযোগ বেরিয়ে আসে।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি লুকানো object চিনতে পারেন কি না, আর method signature পরিষ্কার করতে পারেন কি না।

**সাধারণ ভুল:** শুধু list ছোট করার জন্য সম্পর্ক নেই এমন parameter একসাথে বেঁধে ফেলা। শুধু সেই parameter-গুলোই জড়ো করুন, যেগুলো সত্যিই একসাথে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Data Clumps-এর সাথে সম্পর্ক কী?"* → Parameter-এ দেখা দেওয়া data clump-এর সমাধানই হলো parameter object।

**সম্পর্কিত:** [Q6 — Long Parameter List](#q6) · [Q7 — Data Clumps](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q21"></a>21. Replace Temp with Query — এটা কী?

> Deeper · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q21)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Replace Temp with Query একটা হিসাব ধরে রাখা temporary variable-কে ছোট একটা method-এ (একটা 'query') বদলে দেয়, যেটা হিসাবটা করে। এতে একই temp variable বারবার লেখা বন্ধ হয়। হিসাবটা আবার ব্যবহার করা যায় এমন হয়। আর প্রায়ই বড় method আলাদা করে বের করা সহজ হয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell: একটা temp, যেটা শুধু একটা হিসাব ধরে রাখে।**

```dart
double price() {
  final basePrice = quantity * itemPrice; // একটা temp
  if (basePrice > 1000) return basePrice * 0.95;
  return basePrice * 0.98;
}
```

**ধাপ ২ — সমাধান: এটাকে একটা query method বানান।**

```dart
double get _basePrice => quantity * itemPrice; // এখন এটা reusable query
double price() {
  if (_basePrice > 1000) return _basePrice * 0.95;
  return _basePrice * 0.98;
}
```

**ধাপ ৩ — কেন এটা সাহায্য করে।**
- হিসাবটা class-এর যেকোনো জায়গায় ব্যবহার করা যায়, একটা method-এ আটকে থাকে না।
- আশপাশের method ভাগ করা (Extract Method) সহজ হয়ে যায়, কারণ টেনে নেওয়ার মতো কোনো shared temp থাকে না।

**ধাপ ৪ — Trade-off।**
Query প্রতিবার call করলে আবার হিসাব করে। সস্তা হিসাবের জন্য এটা ঠিক আছে। ভারী হিসাবের জন্য temp রাখুন, বা cache করুন।

**Interviewer কেন জিজ্ঞেস করে:** এটা Fowler-এর একটা গভীর refactoring। এটা যাচাই করে আপনি local variable-এর জঞ্জাল পরিষ্কার করতে পারেন কি না।

**সাধারণ ভুল:** একটা ভারী হিসাবকে query দিয়ে বদলানো, যেটা অনেকবার call হয় — এতে performance খারাপ হতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা কেন Extract Method সহজ করে?"* → একই temp ভাগ করা method-গুলো ভাগ করা কঠিন; query সেই shared dependency সরিয়ে দেয়।

**সম্পর্কিত:** [Q15 — Extract Method](#q15) · [Q4 — Long Method](#q4)

[↑ উপরে ফিরুন](#toc)

---

# F. Conditional refactorings

---

## <a id="q22"></a>22. Replace Magic Number with Named Constant — Dart-এ এটা সঠিকভাবে কীভাবে করবেন?

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q22)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"ব্যাখ্যাহীন একটা literal-কে নাম দেওয়া constant বানাই, যাতে মানে পরিষ্কার হয় আর মানটা এক জায়গায় থাকে। Dart-এ compile-time মানের জন্য `const` ব্যবহার করি, আর class-level constant-এর জন্য `static const`। সম্পর্কিত মানের একটা নির্দিষ্ট সেটের জন্য enum আরও ভালো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — আগে: একটা magic number।**

```dart
double area(double r) => 3.14159 * r * r; // 3.14159 জিনিসটা কী?
if (attempts > 3) lockAccount();           // 3 কেন?
```

**ধাপ ২ — পরে: নাম দেওয়া constant।**

```dart
const double pi = 3.14159;
const int maxLoginAttempts = 3;

double area(double r) => pi * r * r;
if (attempts > maxLoginAttempts) lockAccount();
```

**ধাপ ৩ — Dart-এর নিজের দিক।**
- `const` — compile-time constant; নির্দিষ্ট মানের জন্য এটাই বেছে নিন।
- class-এর ভেতরে `static const` — একসাথে রাখা constant-এর জন্য (`AppColors.primary`)।
- Enum — magic int বা string-এর বদলে নির্দিষ্ট কিছু option-এর জন্য।

**Interviewer কেন জিজ্ঞেস করে:** এটা একদম গোড়ার একটা readability অভ্যাস, সবাই এটা আশা করে। আর তাঁরা দেখেন আপনি Dart-এর `const`/`static const`/enum বাছাই জানেন কি না।

**সাধারণ ভুল:** যে মান কখনো বদলায় না, তার জন্য non-const variable ব্যবহার করা। অথবা সত্যিই স্পষ্ট literal-কেও নাম দেওয়া (বাড়তি জঞ্জাল তৈরি করা)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Constant-এর জন্য const নাকি final?"* → `const` হলো compile-time আর canonicalized; নির্দিষ্ট constant-এর জন্য এটা ব্যবহার করুন। `final` runtime-এ একবারই set হয়।

**সম্পর্কিত:** [Q10 — Magic Numbers (smell-টা)](#q10) · [Q23 — Replace Conditional with Polymorphism](#q23)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q23"></a>23. Replace Conditional with Polymorphism — কখন আর কীভাবে?

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q23)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"যখন একটা বড় switch বা if/else থাকে যেটা type-এর উপর ভিত্তি করে আলাদা আচরণ করে, তখন সেটাকে polymorphism দিয়ে বদলানো যায়: প্রতিটা case-কে আলাদা class বানান, যারা একটা shared method implement করে। তখন নতুন case যোগ করা মানে একটা class যোগ করা, conditional edit করা নয় — এটাই Open/Closed Principle।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Smell: type-ভিত্তিক conditional।**

```dart
double pay(Employee e) {
  switch (e.type) {
    case 'engineer': return e.base;
    case 'manager': return e.base + e.bonus;
    case 'sales': return e.base + e.commission;
  }
  return 0;
}
```

প্রতিটা নতুন employee type এই method edit করতে বাধ্য করে।

**ধাপ ২ — সমাধান: প্রতি case-এর জন্য একটা class।**

```dart
abstract class Employee { double pay(); }
class Engineer extends Employee {
  final double base; Engineer(this.base);
  @override double pay() => base;
}
class Manager extends Employee {
  final double base, bonus; Manager(this.base, this.bonus);
  @override double pay() => base + bonus;
}
// Sales যোগ করতে শুধু একটা class যোগ করুন — পুরোনো code বদলায় না।

double pay(Employee e) => e.pay(); // conditional আর নেই
```

**ধাপ ৩ — কখন এটা করবেন না।**
যদি মাত্র দুটো case থাকে আর সেগুলো খুব কমই বদলায়, তাহলে সাধারণ `if` বেশি পরিষ্কার। Case বাড়লে বা প্রায়ই বদলালে polymorphism-এর আসল লাভ পাওয়া যায়। (নির্দিষ্ট সংখ্যক case-এর জন্য Dart-এর sealed class + switch একটা ভালো মাঝামাঝি পথ।)

**Interviewer কেন জিজ্ঞেস করে:** এটা সেই ক্লাসিক OOP চাল, যেটা refactoring-কে Open/Closed Principle-এর সাথে জুড়ে দেয় ([Q11 OCP](section-12-oop-principles-bn.md#q11))।

**সাধারণ ভুল:** ছোট আর স্থিতিশীল একটা conditional-এ এটা কাজে লাগানো — এটা over-engineering। বুদ্ধি খাটান।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"sealed class + switch কি ঠিক নয়?"* → হ্যাঁ ঠিক — এটা compile-time exhaustiveness দেয়; set নির্দিষ্ট হলে আর missing case compiler দিয়ে ধরাতে চাইলে এটাই বেছে নিন।

**সম্পর্কিত:** [Q11 (OCP)](section-12-oop-principles-bn.md#q11) · [Q24 — Decompose Conditional](#q24)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q24"></a>24. Decompose Conditional refactoring কী?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q24)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Decompose Conditional একটা জটিল if/else-কে ভালো নাম দেওয়া method-এ ভাগ করে — একটা condition-এর জন্য, আর একটা করে প্রতিটা branch-এর জন্য। ফলে logic পড়া যায়: জট পাকানো boolean-এর বদলে আপনি একটা বাক্য পড়েন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — আগে: পড়তে কঠিন একটা condition।**

```dart
if (date.isBefore(summerStart) || date.isAfter(summerEnd)) {
  charge = quantity * winterRate + winterServiceCharge;
} else {
  charge = quantity * summerRate;
}
```

**ধাপ ২ — পরে: অংশগুলোর নাম দিন।**

```dart
if (_isWinter(date)) {
  charge = _winterCharge(quantity);
} else {
  charge = _summerCharge(quantity);
}

bool _isWinter(DateTime d) => d.isBefore(summerStart) || d.isAfter(summerEnd);
double _winterCharge(int qty) => qty * winterRate + winterServiceCharge;
double _summerCharge(int qty) => qty * summerRate;
```

এখন `if`-টা প্রায় English-এর মতো পড়া যায়।

**ধাপ ৩ — কেন এটা কাজে লাগে।**
*উদ্দেশ্য* (winter নাকি summer pricing) স্পষ্ট হয়ে যায়, আর প্রতিটা অংশ আলাদা করে test করা যায়। এটা conditional-এর উপর Extract Method কাজে লাগানো।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি জটিল logic পড়ার উপযোগী করতে পারেন কি না — এটা প্রতিদিনের একটা মূল দক্ষতা।

**সাধারণ ভুল:** বিশাল একটা boolean expression inline রেখে দেওয়া, যেটা পাঠককে প্রতিবার নতুন করে বুঝতে হয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"এটা Consolidate Conditional থেকে কীভাবে আলাদা?"* → Decompose একটা condition-এর অংশগুলোর *নাম দেয়*; Consolidate একই ফলাফল দেওয়া কয়েকটা condition *একসাথে মেলায়* ([Q25](#q25))।

**সম্পর্কিত:** [Q15 — Extract Method](#q15) · [Q25 — Consolidate Conditional](#q25)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q25"></a>25. Consolidate Conditional Expression কী?

> Deeper · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q25)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Consolidate Conditional Expression কয়েকটা আলাদা check-কে এক condition-এ আনে, যেগুলোর ফলাফল *একই*, তারপর সেটার নাম দেয়। এটা বারবার একই জিনিস সরায় আর common ফলাফলটা পরিষ্কার করে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — আগে: কয়েকটা check, একই ফলাফল।**

```dart
double disabilityAmount(Employee e) {
  if (e.seniority < 2) return 0;
  if (e.monthsDisabled > 12) return 0;
  if (e.isPartTime) return 0;
  // ... আসল হিসাব
  return e.base * 0.5;
}
```

তিনটা আলাদা `if` সবই 0 return করে — বারবার একই জিনিস।

**ধাপ ২ — পরে: একসাথে করুন আর নাম দিন।**

```dart
double disabilityAmount(Employee e) {
  if (_isNotEligible(e)) return 0;
  return e.base * 0.5;
}
bool _isNotEligible(Employee e) =>
    e.seniority < 2 || e.monthsDisabled > 12 || e.isPartTime;
```

**ধাপ ৩ — কেন এটা কাজে লাগে।**
common ফলাফলটা ("eligible নয় → 0") এখন নাম সহ একটা পরিষ্কার ধারণা। তিনটা ছড়ানো check আর নেই।

**ধাপ ৪ — কখন এটা করবেন না।**
check-গুলো যদি সত্যিই আলাদা হয় (আলাদা ফলাফল, side effect), তাহলে আলাদাই রাখুন। শুধু সেই check-গুলো একসাথে করুন যাদের ফলাফল *একই*।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা গভীর refactoring, যেটা যাচাই করে আপনি conditional-এ পুনরাবৃত্ত ফলাফল চিনতে পারেন কি না।

**সাধারণ ভুল:** এমন condition একসাথে করা যাদের ফলাফল আসলে এক নয়। এতে গুরুত্বপূর্ণ আলাদা logic ঢাকা পড়ে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Decompose বনাম Consolidate?"* → Decompose একটা জটিল condition-কে নাম দেওয়া অংশে ভাগ করে; Consolidate এক ফলাফলের অনেক সহজ condition একসাথে মেলায়।

**সম্পর্কিত:** [Q24 — Decompose Conditional](#q24)

[↑ উপরে ফিরুন](#toc)

---

# G. Legacy code

---

## <a id="q26"></a>26. Strangler Fig Pattern কী, আর কখন ব্যবহার করেন?

> Deeper · Medium · [🇬🇧 English](../software-engineer-flutter/section-15-code-smells.md#q26)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Strangler Fig pattern পুরোনো system-কে ধীরে ধীরে, টুকরো টুকরো করে বদলায়। এক ধাক্কায় ঝুঁকির big-bang rewrite করে নয়। আপনি পুরোনোটার চারপাশে নতুন code বানান, একটু একটু করে traffic নতুনটায় পাঠান, আর ধীরে ধীরে পুরোনো system-কে 'strangle' করেন যতক্ষণ না সেটা মুছে ফেলা যায়। বড় legacy migration-এ এটা ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: strangler fig গাছ।**
একটা strangler fig গাছ host গাছের চারপাশে বাড়ে আর ধীরে ধীরে দখল নেয়। শেষে আসল গাছটা আর থাকে না, কিন্তু structure-টা থেকে যায়। এই pattern ঠিক একইভাবে legacy system বদলায় — ধীরে ধীরে।

**ধাপ ২ — এটা কীভাবে কাজ করে।**
1. পুরোনো system-এর সামনে একটা layer (facade বা router) বসান।
2. একটা feature-এর নতুন version বানান।
3. ওই এক feature-এর traffic নতুন code-এ পাঠান; বাকি সব এখনো পুরোনোটাই ব্যবহার করে।
4. feature ধরে ধরে একই কাজ করতে থাকুন।
5. পুরোনো system কেউ আর ব্যবহার না করলে সেটা মুছে ফেলুন।

```
Requests → [Router] → mostly OLD system
                    → a few features → NEW system
   (over time, more and more routes move to NEW, until OLD is gone)
```

**ধাপ ৩ — কেন এটা বড় rewrite-এর চেয়ে ভালো।**
- **ঝুঁকি কম** — ছোট ছোট টুকরো, প্রতিটাই ফিরিয়ে নেওয়া যায়।
- **Continuous delivery** — পুরো সময় app কাজ করতে থাকে।
- **আগেভাগে feedback** — প্রতিটা migrate করা টুকরো থেকে আপনি শেখেন।

Big-bang rewrite ব্যর্থ হওয়ার জন্য বিখ্যাত (পরিকল্পনার চেয়ে বেশি সময় লাগে, আর পুরোনো system বদলাতেই থাকে)। Strangler Fig এটা এড়ায়।

**Interviewer কেন জিজ্ঞেস করে:** "বড় একটা legacy app নিরাপদে কীভাবে আধুনিক করবেন?" — এই প্রশ্নের senior উত্তর এটাই।

**সাধারণ ভুল:** শূন্য থেকে পুরো rewrite প্রস্তাব করা — ঝুঁকি অনেক বেশি, প্রায়ই শেষ হয় না, আর ব্যবসা আটকে যায়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Mobile-এর উদাহরণ?"* → পুরোনো architecture থেকে নতুনটায় screen ধরে ধরে migrate করা (যেমন পুরোনো state management থেকে BLoC-এ), একটা routing বা feature-flag layer-এর পেছনে থেকে।

**সম্পর্কিত:** [Q3 — team-কে রাজি করানো](#q3) · [Q2 — নিরাপদে refactor](#q2)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের review)

Interview-এর দিন সকালে এটা পড়ুন। আগে টেবিলগুলো, তারপর এক লাইনের মনে রাখার কথা।

## Smell → যে refactoring এটা ঠিক করে

| Smell | সমাধান |
|---|---|
| Long Method | Extract Method ([Q15](#q15)) |
| Large Class / God Object | Extract Class ([Q16](#q16)) |
| Long Parameter List / Data Clumps | Introduce Parameter Object ([Q20](#q20)) |
| Primitive Obsession | value object ([Q8](#q8)) |
| Duplicate Code | Extract + DRY ([Q9](#q9)) |
| Magic Numbers | Named Constant / enum ([Q22](#q22)) |
| Feature Envy | Move Method ([Q18](#q18)) |
| Type-based switch | Replace Conditional with Polymorphism ([Q23](#q23)) |
| Complex conditional | Decompose Conditional ([Q24](#q24)) |

## যে জোড়াগুলো গুলিয়ে যায়

- **Shotgun Surgery vs Divergent Change** → ছড়িয়ে আছে (জড়ো করুন) বনাম ভিড় হয়ে গেছে (ভাগ করুন)। ([Q14](#q14))
- **Data Clumps vs Primitive Obsession** → একটা *group* একসাথে থাকার কথা বনাম একটা *একক* primitive-এর একটা type দরকার। ([Q7](#q7), [Q8](#q8))
- **Extract vs Inline Method** → একটা block-কে নাম দেওয়া বনাম মানে নেই এমন indirection সরানো। ([Q15](#q15), [Q17](#q17))
- **Decompose vs Consolidate Conditional** → একটা condition ভাগ করা বনাম একই result দেওয়া অনেকগুলোকে মেলানো। ([Q24](#q24), [Q25](#q25))

## এক লাইনের মনে রাখার কথা

- **Code smell** = design-এর একটা সতর্কবার্তা; code এখনো কাজ করে (bug-এর তুলনায়)। ([Q1](#q1))
- **Refactoring** = structure ভালো করা, **behaviour একই থাকে**; আগে tests, ছোট ছোট ধাপ। ([Q2](#q2))
- **Long Method** → Extract Method; **Large Class** → Extract Class। ([Q4](#q4), [Q5](#q5))
- **Duplicate Code** → একটাই সত্যের source (DRY) — কিন্তু একই *knowledge* হলেই মেলান। ([Q9](#q9))
- **Magic Numbers** → named constant / enum। ([Q10](#q10), [Q22](#q22))
- **Feature Envy** → behaviour-কে তার data-র পাশে রাখুন (Move Method)। ([Q13](#q13), [Q18](#q18))
- **বড় type-switch** → polymorphism (Open/Closed)। ([Q23](#q23))
- **Comments smell** তখনই যখন সেগুলো খারাপ code ব্যাখ্যা করে; ভালো comment ব্যাখ্যা করে *কেন*। ([Q12](#q12))
- **Team-কে রাজি করানো** → business value-র সাথে যুক্ত করুন, অল্প অল্প করে করুন (boy scout rule)। ([Q3](#q3))
- **Strangler Fig** → legacy ধীরে ধীরে migrate করুন, কখনোই big-bang rewrite নয়। ([Q26](#q26))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer-রা কীভাবে আরও গভীরে যান

Interviewer-রা আপনাকে এলোমেলো code দেখান, আর সেটা ভালো করতে বলেন। মুখে বলে বলে অনুশীলন করুন:

1. *"এই method 150 line-এর — আপনি কী করবেন?"* → smell-এর নাম বলুন (Long Method), প্রতিটা কাজের জন্য Extract Method।
2. *"আপনি কীভাবে নিশ্চিত হন যে কিছু ভাঙেনি?"* → আগে tests, ছোট ছোট ধাপ, প্রতি ধাপের পরে tests চালান।
3. *"`type`-এর উপর একটা বড় switch আছে — এটা ভালো করুন।"* → Replace Conditional with Polymorphism (open/closed)।
4. *"পুরো app পুরোনো architecture ব্যবহার করে — কীভাবে আধুনিক করবেন?"* → Strangler Fig, screen ধরে ধরে, rewrite নয়।
5. *"Team বলে refactor করার সময় নেই।"* → এটাকে bug rate আর delivery speed-এর সাথে যুক্ত করুন; feature-এর সাথে অল্প অল্প করে করুন।

Smell-এর নাম বলা, সমাধানের নাম বলা, আর "behaviour একই থাকে" কথাটায় জোর দেওয়া — এটাই আসল senior signal। remote আর BD, দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
