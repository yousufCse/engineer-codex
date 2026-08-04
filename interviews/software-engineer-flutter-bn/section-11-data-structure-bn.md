
claude --resume abbeebc0-c14d-4e25-a217-43bcb48442f4

# Section 11 — Data Structures & Algorithms

> **Senior Flutter / Mobile Engineer — Interview Prep**
> **Remote** আর **বাংলাদেশ (BD)** কোম্পানির interview-এর জন্য।
> প্রতিটা উত্তর **সহজ ভাষায়**, **ধাপে ধাপে পুরো ব্যাখ্যা সহ**, আর **link করা** — তাই এদিক-ওদিক ঘুরে ধাপে ধাপে প্রস্তুতি নিতে পারবেন। (DSA সবচেয়ে বেশি কাজে লাগে remote/আন্তর্জাতিক interview-এ।)

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-11-data-structure-bn.md](../software-engineer-flutter/section-11-data-structure.md)

---

## এই Section কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষিপ্ত উত্তর (এটাই বলুন)** — interview-এ প্রথমে বলার মতো ২-৩ বাক্যের উত্তর।
- **এবার পুরোটা বুঝি** — বাস্তব উদাহরণ আর code সহ ধাপে ধাপে বিস্তারিত ব্যাখ্যা।
- **Interviewer কেন জিজ্ঞেস করে** · **সাধারণ ভুল** · **যে Follow-up প্রশ্ন আসতে পারে**
- **সম্পর্কিত** — সংশ্লিষ্ট প্রশ্নে যান · **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন জিজ্ঞেস করা হয় (**খুব সাধারণ / সাধারণ / গভীর**) আর তার কাঠিন্য (**সহজ / মাঝারি / কঠিন**)।

> **Interview Tip:** DSA-তে সবসময় আগে **মূল idea আর Big-O** বলুন, তারপর code লিখুন। কাজ করার সময় মুখে বলে বলে এগোন — interviewer আপনার চিন্তাভাবনায় নম্বর দেন, শুধু শেষ code-এ নয়।

---


## <a id="toc"></a>সূচিপত্র

**A. Complexity (Big-O)**
1. [Big-O notation — time complexity](#q1) · *Very common*
2. [Space complexity](#q2) · *Common*

**B. Linear structure**
3. [Array / List — কীভাবে কাজ করে, complexity](#q3) · *Very common*
4. [Linked List — array-এর সাথে তুলনা, trade-off](#q4) · *Common*
5. [Stack — LIFO](#q5) · *Very common*
6. [Queue — FIFO (আর Deque)](#q6) · *Common*

**C. Hash-ভিত্তিক structure**
7. [Map / HashMap — ভেতরের কাজ ও collision](#q7) · *Very common*
8. [Set — আর কখন ব্যবহার করবেন](#q8) · *Common*

**D. Tree ও graph**
9. [Binary Tree — BFS বনাম DFS](#q9) · *Very common*
10. [Graph — representation, BFS ও DFS](#q10) · *Common*

**E. Searching ও sorting**
11. [Binary Search](#q11) · *Very common*
12. [Sorting — Bubble, Insertion, Merge, Quick](#q12) · *Very common*

**F. মূল কৌশল**
13. [Two Pointers](#q13) · *Common*
14. [Sliding Window](#q14) · *Common*
15. [Recursion — base case, call stack, tail recursion](#q15) · *Very common*
16. [Dynamic Programming — memoization বনাম tabulation](#q16) · *Common*

**G. সাধারণ coding সমস্যা (Dart)**
17. [একটা string উল্টে দেওয়া](#q17) · *Common*
18. [Palindrome কি না check করা](#q18) · *Common*
19. [List-এ duplicate খুঁজে বের করা](#q19) · *Common*
20. [FizzBuzz](#q20) · *Common*
21. [Fibonacci — iterative, recursive, memoized](#q21) · *Very common*
22. [Two Sum](#q22) · *Very common*
23. [`max()` ছাড়া list-এর সবচেয়ে বড় সংখ্যা](#q23) · *Common*

**দ্রুত link:** [ধাপে ধাপে প্রস্তুতি](#study-plan) · [Cheat Sheet (শেষ রাতের review)](#cheatsheet)

---


## <a id="study-plan"></a>ধাপে ধাপে প্রস্তুতি (পড়ার পরিকল্পনা)

২৩টা প্রশ্ন একসাথে লাগবে না। এই পর্যায়গুলো ক্রম অনুযায়ী শেষ করুন। একটা পর্যায় তখনই টিক দিন, যখন আপনি **সংক্ষিপ্ত উত্তর** বলতে পারবেন আর না দেখে code লিখতে পারবেন।

**ধাপ ১ — DSA-র ভাষা (এখান থেকেই শুরু)।** সবকিছু এই মাপকাঠিতেই মাপা হয়।
→ [Q1 Big-O](#q1) · [Q2 Space complexity](#q2)

**ধাপ ২ — প্রতিদিনের structure।**
→ [Q3 List](#q3) · [Q7 Map](#q7) · [Q5 Stack](#q5) · [Q6 Queue](#q6) · [Q8 Set](#q8)

**ধাপ ৩ — ক্লাসিক algorithm।**
→ [Q11 Binary search](#q11) · [Q12 Sorting](#q12) · [Q15 Recursion](#q15)

**ধাপ ৪ — যে pattern দিয়ে বেশিরভাগ interview প্রশ্নের সমাধান হয়।**
→ [Q13 Two pointers](#q13) · [Q14 Sliding window](#q14) · [Q16 Dynamic programming](#q16) · [Q22 Two Sum](#q22)

**ধাপ ৫ — Tree, graph আর বাকিগুলো।**
→ [Q4 Linked list](#q4) · [Q9 Binary tree](#q9) · [Q10 Graph](#q10) · [Q17](#q17)–[Q21](#q21), [Q23](#q23)

**সময় কম (interview-এর ১ ঘণ্টা আগে)?** এই আটটা দেখে নিন:
[Q1](#q1) · [Q3](#q3) · [Q7](#q7) · [Q11](#q11) · [Q12](#q12) · [Q13](#q13) · [Q15](#q15) · [Q22](#q22), তারপর [Cheat Sheet](#cheatsheet) পড়ুন।

---

# A. Complexity (Big-O)

---

## <a id="q1"></a>1. Big-O notation কী, আর এটা কেন গুরুত্বপূর্ণ?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q1)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Big-O বলে দেয় input বাড়লে একটা algorithm-এর কাজ কতটা বাড়ে। এটা ছোটখাটো detail আর machine-এর গতি ধরে না। এটা শুধু বৃদ্ধির আকারের দিকে তাকায়। code চালানোর আগেই দুটো সমাধান তুলনা করতে আমরা এটা ব্যবহার করি — যেমন, বড় input-এ O(log n) হলো O(n)-এর চেয়ে অনেক ভালো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: অতিথিদের জন্য রান্না।**
একটা রেসিপি কল্পনা করুন। Big-O জিজ্ঞেস করে: "অতিথির সংখ্যা দ্বিগুণ হলে কাজ কতটা বাড়ে?"
- প্রতিটা অতিথিকে একবার করে অভ্যর্থনা জানালে → অতিথি দ্বিগুণ হলে কাজও দ্বিগুণ। এটাই **O(n)**।
- যত অতিথিই হোক একটা oven চালু করলে → কাজ একই থাকে। এটাই **O(1)**।
- প্রতিটা অতিথি যদি বাকি সব অতিথির সাথে হাত মেলায় → কাজ অনেক দ্রুত বাড়ে। এটাই **O(n²)**।

**ধাপ ২ — সাধারণ বৃদ্ধির হারগুলো, সবচেয়ে ধীরে বাড়াটা আগে।**

| Big-O | নাম | উদাহরণ |
|---|---|---|
| O(1) | constant | `list[5]` পড়া, Map-এ যোগ করা |
| O(log n) | logarithmic | binary search |
| O(n) | linear | একটা list-এ একবার loop চালানো |
| O(n log n) | linearithmic | ভালো sorting (merge, quick) |
| O(n²) | quadratic | একই list-এর উপর nested loop |
| O(2ⁿ) | exponential | সাদামাটা recursive Fibonacci |

**ধাপ ৩ — code পড়ে তার Big-O বের করা।**
`n` বাড়লে কাজটা কতবার চলে সেটা গুনুন।

```dart
// O(1) — size যাই হোক, এক ধাপ
int first(List<int> a) => a[0];

// O(n) — n item-এর উপর একটা loop
int sum(List<int> a) {
  var total = 0;
  for (final x in a) total += x; // n বার চলে
  return total;
}

// O(n^2) — loop-এর ভেতরে loop, দুটোই n-এর উপর
void printPairs(List<int> a) {
  for (final x in a) {        // n বার
    for (final y in a) {      // প্রতিবার n বার
      print('$x,$y');         // n * n = n^2
    }
  }
}
```

**ধাপ ৪ — দুটো নিয়ম, যা Big-O সহজ করে দেয়।**
1. **Constant বাদ দিন:** O(2n) হয়ে যায় O(n)। আমরা আকার নিয়ে চিন্তা করি, সঠিক সংখ্যা নিয়ে নয়।
2. **সবচেয়ে বড় term রাখুন:** O(n² + n) হয়ে যায় O(n²)। বড় n-এ সবচেয়ে বড় term-ই সব ঠিক করে দেয়।

**ধাপ ৫ — "log n" কেন এত ভালো।**
`log n` মানে "n-কে অর্ধেক করতে করতে 1-এ পৌঁছাতে কতবার লাগে?" 1,000,000 item-এর একটা list-এ সেটা মাত্র প্রায় 20 ধাপ। এই কারণেই binary search প্রায় সাথে সাথে হয়ে যায় বলে মনে হয়।

**Interviewer কেন জিজ্ঞেস করে:** Big-O হলো সব algorithm প্রশ্নের সাধারণ ভাষা। তাঁরা জানতে চান আপনি সমাধান তুলনা করে দক্ষটা বেছে নিতে পারেন কি না।

**সাধারণ ভুল:** বৃদ্ধির আকারের বদলে ঠিক কতগুলো operation চলে সেটা গোনা ("O(2n+3)" বলা)। শুধু O(n) বলুন। আরেকটা ভুল: worst case বাদ দেওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Best, average, worst case?"* → Best = সবচেয়ে সৌভাগ্যের input, worst = সবচেয়ে কঠিন input, average = সাধারণ input। Interview-এ সাধারণত **worst case** নিয়েই কথা হয়।
- *"Amortized time কী?"* → অনেকগুলো operation মিলিয়ে প্রতি operation-এর গড় খরচ। একটা dynamic list-এ যোগ করা amortized O(1), যদিও একবারের resize O(n) ([Q3](#q3) দেখুন)।

**সম্পর্কিত:** [Q2 — space complexity](#q2) · [Q11 — binary search (log n)](#q11) · [Q12 — sorting (n log n)](#q12)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q2"></a>2. Space complexity কী, আর এটা time complexity থেকে কীভাবে আলাদা?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q2)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Time complexity মাপে চলার সময় কতটা বাড়ে; space complexity মাপে input বাড়লে অতিরিক্ত memory কতটা বাড়ে। আমরা algorithm যে বাড়তি memory বানায় সেটাই গুনি, input নিজে গুনি না। Recursion-এর call stack-ও এর মধ্যে পড়ে — n স্তর গভীর recursion O(n) space নেয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সহজ পার্থক্য।**
- **Time** = input বাড়লে কত ধাপ লাগে।
- **Space** = input বাড়লে কত বাড়তি memory লাগে।

**ধাপ ২ — বাড়তি memory গুনুন, input নয়।**
একটা function যদি n item-এর একটা list নেয়, সেই list হলো input — আমরা সেটা গুনি না। আমরা গুনি function যা *বানায়*।

```dart
// O(1) extra space — মাত্র কয়েকটা variable
int sum(List<int> a) {
  var total = 0;        // 1টা variable, a যত বড়ই হোক
  for (final x in a) total += x;
  return total;
}

// O(n) extra space — input-এর সমান বড় নতুন list বানায়
List<int> doubled(List<int> a) {
  final out = <int>[];  // size n পর্যন্ত বাড়ে
  for (final x in a) out.add(x * 2);
  return out;
}
```

**ধাপ ৩ — Recursion stack-এর জায়গা নেয়।**
প্রতিটা recursive call শেষ না হওয়া পর্যন্ত stack-এ অপেক্ষা করে। তাই n গভীর পর্যন্ত যাওয়া recursion O(n) memory নেয়, যদিও সেটা কোনো list বানায় না।

```dart
int factorial(int n) {
  if (n <= 1) return 1;        // base case
  return n * factorial(n - 1); // n-টা call stack-এ জমে → O(n) space
}
```

**ধাপ ৪ — ক্লাসিক trade-off: time বনাম space।**
প্রায়ই বেশি memory ব্যবহার করে কোনো কিছু দ্রুত করা যায়, বা বেশি সময় খরচ করে memory বাঁচানো যায়। উদাহরণ: [Two Sum](#q22) একটা Map ব্যবহার করে (বাড়তি O(n) space), আর তাতে O(n²) time থেকে O(n) time-এ নেমে আসে।

**Interviewer কেন জিজ্ঞেস করে:** Senior engineer শুধু গতি নয়, memory নিয়েও ভাবেন — mobile-এ এটা গুরুত্বপূর্ণ, কারণ সেখানে memory সীমিত।

**সাধারণ ভুল:** recursion-এর call stack-ও যে space হিসেবে গোনা হয় সেটা ভুলে যাওয়া, বা input-কে বাড়তি space হিসেবে গোনা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"In-place algorithm?"* → যেটা input-কে সরাসরি বদলে O(1) বাড়তি space ব্যবহার করে (যেমন একই list-এর ভেতরে element অদল-বদল করা)।

**সম্পর্কিত:** [Q1 — time complexity](#q1) · [Q15 — recursion ও call stack](#q15) · [Q22 — Two Sum (space দিয়ে time কেনা)](#q22)

[↑ উপরে ফিরুন](#toc)

---

# B. Linear structure

---

## <a id="q3"></a>3. Dart-এর List (array) ভেতরে ভেতরে কীভাবে কাজ করে, আর এর time complexity কী কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q3)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart-এর `List` হলো একটা dynamic array — item-গুলো memory-তে পাশাপাশি বসে থাকে। তাই index দিয়ে পড়া সাথে সাথেই হয়, O(1)। শেষে যোগ করা সাধারণত O(1)। কিন্তু জায়গা ফুরিয়ে গেলে সবকিছু একটা বড় block-এ copy হয়, সেটা মাঝে মাঝে O(n) — গড়ে হিসাব করলে দাঁড়ায় amortized O(1)। মাঝখানে insert বা remove করা O(n), কারণ তার পরের সব item সরাতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: এক সারিতে নম্বর দেওয়া locker।**
Array হলো এক সারি locker, 0 থেকে নম্বর দেওয়া। নম্বর দেওয়া আছে আর সবগুলোর মাপ এক, তাই সরাসরি locker 5-এ চলে যেতে পারেন — খোঁজাখুঁজি লাগে না। এই কারণেই index access O(1)।

**ধাপ ২ — Index দিয়ে পড়া O(1)।**

```dart
final list = [10, 20, 30, 40];
print(list[2]); // 30 — সাথে সাথে, computer সোজা ওখানেই লাফ দেয়
```

**ধাপ ৩ — কেন "dynamic" array, আর amortized O(1)।**
`List`-এর ভেতরে একটা নির্দিষ্ট মাপের memory block থাকে। সেটা ভরে যাওয়ার পর আরও যোগ করলে Dart একটা বড় block বানায় (সাধারণত দ্বিগুণ মাপ)। তারপর সবকিছু সেখানে copy করে দেয়। ওই একবারের copy O(n)। কিন্তু দ্বিগুণ করার ঘটনা খুব কম ঘটে। তাই প্রতিটা `add`-এর *গড়* খরচ এখনও O(1) — এটাকেই বলি **amortized O(1)**।

```dart
final list = <int>[];
list.add(1); // সাধারণত O(1)
list.add(2); // সাধারণত O(1)
// ... মাঝে মাঝে O(n), যখন capacity দ্বিগুণ হয়, কিন্তু সেটা বিরল
```

**ধাপ ৪ — মাঝখানে insert/remove করা O(n)।**
সামনে insert করলে বাকি প্রতিটা item-কে এক ঘর ডানে সরতে হয়।

```dart
final list = [10, 20, 30];
list.insert(0, 5); // [5, 10, 20, 30] — সব item সরে গেল → O(n)
list.removeAt(0);  // সব আবার পিছনে সরে → O(n)
```

**ধাপ ৫ — যে complexity table মুখস্থ রাখবেন।**

| Operation | Complexity | কেন |
|---|---|---|
| access `list[i]` | O(1) | সোজা index-এ লাফ |
| শেষে add/remove | O(1) amortized | মাঝে মাঝে resize |
| মাঝখানে/সামনে insert/remove | O(n) | বাকিগুলো সরাতে হয় |
| search (`contains`, `indexOf`) | O(n) | একটা একটা করে item দেখা |

**Interviewer কেন জিজ্ঞেস করে:** List সবচেয়ে বেশি ব্যবহৃত structure। তাঁরা জানতে চান, মাঝখানে insert করা আর search করার লুকানো খরচটা আপনি বোঝেন কি না।

**সাধারণ ভুল:** `insert(0, x)` বা `contains`-কে সস্তা ভাবা। দুটোই O(n)। অনেক বেশি search করলে বদলে Map বা Set ব্যবহার করুন ([Q7](#q7), [Q8](#q8))।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fixed-size list কীভাবে বানাবেন?"* → `List.filled(n, 0)` বা `List.generate(n, ...)`।
- *"List vs Linked List?"* → দেখুন [Q4](#q4)।

**সম্পর্কিত:** [Q4 — linked list](#q4) · [Q7 — দ্রুত lookup-এর জন্য Map](#q7) · [Q1 — Big-O](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q4"></a>4. Linked List কী, array থেকে এটা কীভাবে আলাদা, আর এর trade-off কী কী?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q4)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Linked list হলো node-এর একটা শিকল। প্রতিটা node-এ একটা value থাকে আর পরের node-এর দিকে একটা pointer থাকে। Array-র মতো item-গুলো memory-তে পাশাপাশি থাকে না। তাই জানা জায়গায় insert বা delete করা O(1) — শুধু pointer বদলাতে হয়। কিন্তু n-তম item পড়া O(n), কারণ শুরু থেকে শিকল ধরে হাঁটতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: গুপ্তধনের খোঁজ।**
গুপ্তধনের খোঁজে প্রতিটা সূত্র বলে দেয় পরের সূত্রটা কোথায়। সূত্র 5-এ পৌঁছাতে হলে আগে 1, 2, 3, 4 ধরে যেতে হবে। এটাই linked list — মাঝখানে সরাসরি লাফ দেওয়া যায় না।

**ধাপ ২ — Node-এর গঠন।**

```dart
class Node<T> {
  T value;
  Node<T>? next; // পরের node-কে point করে, শেষে null
  Node(this.value, [this.next]);
}

// বানানো: 1 -> 2 -> 3
final head = Node(1, Node(2, Node(3)));
```

**ধাপ ৩ — Insert/delete কেন O(1) হতে পারে।**
আপনার হাতে যদি একটা node আগে থেকেই থাকে, তার পরে insert করা মানে শুধু pointer বদল — কিছু সরাতে হয় না:

```dart
// একটা node `n`-এর পরে 99 insert করা
final newNode = Node(99, n.next);
n.next = newNode; // হয়ে গেল — O(1), আর কিছুই সরল না
```

**ধাপ ৪ — Access কেন O(n)।**
5ম item-এ পৌঁছাতে head থেকে পাঁচবার `next` ধরে যেতে হবে।

```dart
Node<T>? getAt<T>(Node<T>? head, int index) {
  var current = head;
  for (var i = 0; i < index && current != null; i++) {
    current = current.next; // শিকল ধরে হাঁটা → O(n)
  }
  return current;
}
```

**ধাপ ৫ — Array vs Linked List।**

| | Array / List | Linked List |
|---|---|---|
| Index দিয়ে access | O(1) | O(n) |
| জানা জায়গায় insert/delete | O(n) (সরাতে হয়) | O(1) (pointer) |
| Memory | এক block, ঘন | ছড়ানো + প্রতি node-এ বাড়তি pointer |
| Cache friendly | হ্যাঁ | না |

**Interviewer কেন জিজ্ঞেস করে:** এটা দেখে আপনি memory layout আর pointer বোঝেন কি না। আর operation দেখে structure বেছে নিতে পারেন কি না।

**সাধারণ ভুল:** linked list-কে "দ্রুত" বলে দেওয়া। জানা node-এ insert/delete করার বেলায় শুধু এটা দ্রুত। দৈনন্দিন কাজে Dart-এর `List` সাধারণত ভালো (ঘন memory, দ্রুত access)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Singly vs doubly linked?"* → Doubly linked node আগের node-কেও point করে, তাই পিছন দিকেও হাঁটা যায় (Dart-এর `Queue` এটা ব্যবহার করে)।
- *"Flutter-এ কখন ব্যবহার করবেন?"* → সরাসরি খুব কমই; তবে `Queue` (`dart:collection` থেকে) ভেতরে একটা linked structure দিয়েই বানানো।

**সম্পর্কিত:** [Q3 — array](#q3) · [Q6 — Queue](#q6)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q5"></a>5. Stack কী, এটা কীভাবে কাজ করে, আর Dart-এ কীভাবে একটা বানাবেন?

> Very common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q5)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Stack হলো Last-In-First-Out (LIFO) — সবার শেষে যেটা রাখলেন, সেটাই সবার আগে বের হয়। Push উপরে যোগ করে, pop উপর থেকে সরায়, দুটোই O(1)। Dart-এ সাধারণ একটা `List`-ই stack: push-এর জন্য `add`, আর pop-এর জন্য `removeLast`।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: থালার স্তূপ।**
আপনি উপরে একটা থালা রাখেন, আর উপরের থালাটাই আগে তুলে নেন। নিচ থেকে একটা টেনে বের করতে পারবেন না। এটাই LIFO।

**ধাপ ২ — List দিয়ে এটা বানান।**

```dart
final stack = <int>[];
stack.add(1);          // push → [1]
stack.add(2);          // push → [1, 2]
final top = stack.removeLast(); // pop → 2, stack এখন [1]
final peek = stack.last;         // না সরিয়ে দেখা → 1
final isEmpty = stack.isEmpty;
```

Push, pop আর peek — তিনটাই O(1)।

**ধাপ ৩ — Stack কোথায় ব্যবহার হয় (বাস্তব উদাহরণ)।**
- **Undo/redo** — প্রতিটা action push হয়; undo শেষেরটা pop করে।
- **Browser-এর back button** — page-গুলো push হয়; back pop করে।
- **Flutter-এর Navigator** — screen push আর pop হয় (এটা আক্ষরিক অর্থেই একটা stack)।
- **Function call** — call stack নিজেই একটা stack (দেখুন [Q15](#q15))।
- **Balanced bracket মেলানো** — opening bracket push করুন, closing এলে pop করুন।

**ধাপ ৪ — একটা ক্লাসিক stack সমস্যা: balanced bracket।**

```dart
bool isBalanced(String s) {
  final stack = <String>[];
  const pairs = {')': '(', ']': '[', '}': '{'};
  for (final ch in s.split('')) {
    if (ch == '(' || ch == '[' || ch == '{') {
      stack.add(ch);                 // opening push
    } else if (pairs.containsKey(ch)) {
      if (stack.isEmpty || stack.removeLast() != pairs[ch]) {
        return false;                // ভুল বা অনুপস্থিত match
      }
    }
  }
  return stack.isEmpty;              // সব opening বন্ধ হয়েছে
}
```

**Interviewer কেন জিজ্ঞেস করে:** Stack সব জায়গায় আসে (navigation, undo, parsing)। তাঁরা দেখেন আপনি LIFO জানেন কি না, আর সেটা দিয়ে সমস্যা সমাধান করতে পারেন কি না।

**সাধারণ ভুল:** `removeLast()`-এর বদলে `removeAt(0)` (সামনের দিক) ব্যবহার করা। `removeAt(0)` হলো O(n), আর এটা আপনার stack-এর order উল্টে দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Stack vs Queue?"* → Stack = LIFO (শেষেরটা আগে বের হয়)। Queue = FIFO (প্রথমটা আগে বের হয়)। দেখুন [Q6](#q6)।
- *"Navigator কীভাবে stack ব্যবহার করে?"* → `push` উপরে একটা screen বসায়, `pop` উপরেরটা সরায় — ঠিক LIFO।

**সম্পর্কিত:** [Q6 — Queue](#q6) · [Q15 — call stack](#q15) · [Q3 — List](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q6"></a>6. Queue কী, Stack থেকে এটা কীভাবে আলাদা, আর Dart-এ কীভাবে ব্যবহার করবেন?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q6)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Queue হলো First-In-First-Out (FIFO) — যে item প্রথমে ঢোকে, সেটাই প্রথমে বের হয়, দোকানের line-এর মতো। Dart-এ `dart:collection`-এর `Queue` ব্যবহার করি। এটা দুই প্রান্তেই O(1)-এ add আর remove করে। সাধারণ List-ও queue-এর কাজ করতে পারে, কিন্তু `removeAt(0)` হলো O(n)। তাই `Queue`-ই ভালো।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: দোকানের line।**
Line-এর প্রথম মানুষটি আগে service পান। নতুন মানুষ পেছনে যোগ হন। এটাই FIFO — stack-এর ঠিক উল্টো।

**ধাপ ২ — Dart-এর `Queue` ব্যবহার করুন (দুই প্রান্তেই দ্রুত)।**

```dart
import 'dart:collection';

final queue = Queue<int>();
queue.add(1);              // পেছনে enqueue → [1]
queue.add(2);              // → [1, 2]
final first = queue.removeFirst(); // সামনে থেকে dequeue → 1, O(1)
final peek = queue.first;          // সামনের item দেখা
```

**ধাপ ৩ — শুধু List ব্যবহার করলে সমস্যা কোথায়?**
List `add` (পেছনে) করতে পারে O(1)-এ, কিন্তু `removeAt(0)` (সামনে) হলো O(n)। কারণ বাকি প্রতিটা item সরে যায়। `Queue` বানানোই হয়েছে দুই প্রান্তে O(1) হওয়ার জন্য। তাই আসল queue-এর কাজে এটাই ব্যবহার করুন।

**ধাপ ৪ — Deque (double-ended queue)।**
`Queue` একই সাথে একটা deque: দুই প্রান্তেই add/remove করা যায় (`addFirst`, `addLast`, `removeFirst`, `removeLast`)। Sliding-window সমস্যায় এটা কাজে লাগে।

**ধাপ ৫ — Queue কোথায় ব্যবহার হয়।**
- **BFS** (breadth-first search) tree/graph-এ queue ব্যবহার করে ([Q9](#q9), [Q10](#q10))।
- **Task/job processing** — যে order-এ task এসেছে, সেই order-এ handle করা।
- **Print/download queue**, message buffer।

**Interviewer কেন জিজ্ঞেস করে:** Queue দিয়েই BFS চলে, আর "আসার order-এ process করা" যেকোনো কাজ চলে। তাঁরা দেখেন আপনি FIFO আর O(1)-front বিষয়টা জানেন কি না।

**সাধারণ ভুল:** Loop-এর ভেতরে `List.removeAt(0)` ব্যবহার করা (প্রতিবার O(n) → মোট O(n²))। `Queue.removeFirst()` ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Priority queue?"* → এমন queue যেখানে সবচেয়ে বেশি priority-র item আগে বের হয়। সাধারণত heap দিয়ে বানানো হয় (O(log n) insert/remove)। Dart-এ built-in কিছু নেই; `collection` package-এর `HeapPriorityQueue` ব্যবহার করুন।

**সম্পর্কিত:** [Q5 — Stack (LIFO)](#q5) · [Q9 — BFS queue ব্যবহার করে](#q9) · [Q10 — graph](#q10)

[↑ উপরে ফিরুন](#toc)

---

# C. Hash-ভিত্তিক structure

---

## <a id="q7"></a>7. Dart-এর `Map` (HashMap) ভেতরে কীভাবে কাজ করে, আর এর time complexity কী কী?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q7)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Map key-value pair রাখে আর একটা key প্রায় সাথে সাথেই খুঁজে দেয় — average O(1)। এটা key-কে একটা hash function-এ চালিয়ে বের করে কোথায় রাখতে হবে। Worst case হলো O(n), যদি অনেক key একই জায়গায় collide করে। Dart-এর default Map insertion order ধরে রাখে, আর key-এর সঠিক `==` ও `hashCode` থাকতে হয়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: number দেওয়া tag-সহ coat-check।**
Coat-check-এ প্রতিটা coat খোঁজার বদলে তাঁরা আপনার coat-কে একটা number দেন আর ওই number-এর hook-এ ঝুলিয়ে রাখেন। ফেরত নেওয়ার সময় সরাসরি ওই hook-এ চলে যান। Map ঠিক একই কাজ করে: key-এর hash বলে দেয় কোন "hook" (bucket) ব্যবহার করতে হবে।

**ধাপ ২ — Lookup কীভাবে কাজ করে (hash function)।**

```dart
final ages = {'Sara': 30, 'Rahim': 25};
print(ages['Sara']); // 30 — average O(1)
```

ভেতরে: `'Sara'`-র `hashCode` → একটা bucket number → সরাসরি ওই bucket-এ যাওয়া। পুরো map scan করার দরকার নেই।

**ধাপ ৩ — Collision আর worst case কেন O(n)।**
দুটো আলাদা key একই bucket-এ hash হতে পারে — একে বলে *collision*। তখন map দুটোকেই ওই bucket-এ রাখে আর `==` দিয়ে মিলিয়ে দেখে। প্রায় সব key যদি একটাই bucket-এ collide করে, lookup নেমে O(n) হয়ে যায়। ভালো hash function এটা বিরল করে দেয়। তাই আমরা lookup-কে average O(1) ধরি।

**ধাপ ৪ — Key-এর সঠিক `==` আর `hashCode` লাগে।**
Map প্রথমে `hashCode` দিয়ে bucket খোঁজে, তারপর `==` দিয়ে সঠিক key নিশ্চিত করে। দুটো override না করে custom object key হিসেবে ব্যবহার করলে lookup fail করবে।

```dart
class Point {
  final int x, y;
  const Point(this.x, this.y);
  @override
  bool operator ==(Object o) => o is Point && o.x == x && o.y == y;
  @override
  int get hashCode => Object.hash(x, y);
}
final m = {const Point(1, 2): 'A'};
print(m[const Point(1, 2)]); // 'A' — কাজ করে কারণ == আর hashCode সঠিক
```

**ধাপ ৫ — Complexity table।**

| Operation | Average | Worst |
|---|---|---|
| insert / update | O(1) | O(n) |
| lookup `m[key]` | O(1) | O(n) |
| delete | O(1) | O(n) |
| contains key | O(1) | O(n) |

**Interviewer কেন জিজ্ঞেস করে:** O(n²) brute force-কে O(n)-এ নামানোর সবচেয়ে বড় হাতিয়ার হলো Map ([Two Sum](#q22) দেখুন)। তাঁরা চান দ্রুত lookup দরকার হলে আপনি Map-এর দিকে হাত বাড়ান।

**সাধারণ ভুল:** Loop-এর ভেতরে `contains`/`indexOf` দিয়ে List খোঁজা (O(n)), যেখানে Map/Set ব্যবহার করলে এটা O(1) হতো। আরও একটা: mutable object-কে key বানিয়ে পরে সেটাকে mutate করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Default Map type?"* → `LinkedHashMap` — insertion order ধরে রাখে। Sorted key দরকার হলে `SplayTreeMap` ব্যবহার করুন।
- *"Map vs Set?"* → Set হলো এমন Map যেখানে শুধু key আছে (value নেই)। [Q8](#q8) দেখুন।

**সম্পর্কিত:** [Q8 — Set](#q8) · [Q22 — Map দিয়ে Two Sum](#q22) · [Q3 — List (ধীর search)](#q3)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q8"></a>8. Set কী, List থেকে এটা কীভাবে আলাদা, আর কখন ব্যবহার করবেন?

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q8)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Set হলো unique item-এর collection, এখানে duplicate থাকে না। এটা membership check করে average O(1)-এ। List-এ duplicate রাখা যায় আর membership check হয় O(n)-এ। তাই যখনই uniqueness দরকার বা দ্রুত 'এটা কি আগে দেখেছি?' check দরকার, তখন Set ব্যবহার করি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুটো মূল পার্থক্য।**
- **List** order ধরে রাখে আর duplicate allow করে; `contains` হলো O(n)।
- **Set**-এ duplicate নেই আর order-এর নিশ্চয়তা নেই (default insertion order ধরে রাখে); `contains` হলো average O(1) (এটা hash-based, Map-এর key-এর মতো)।

```dart
final list = [1, 2, 2, 3];   // duplicate allowed
final set = {1, 2, 2, 3};    // {1, 2, 3} — duplicate বাদ পড়ল
print(set.contains(2));       // average O(1)
```

**ধাপ ২ — সবচেয়ে পরিচিত ব্যবহার: duplicate সরানো।**

```dart
final names = ['a', 'b', 'a', 'c'];
final unique = names.toSet().toList(); // ['a', 'b', 'c']
```

**ধাপ ৩ — আরেকটা পরিচিত ব্যবহার: দ্রুত "আগে দেখেছি?" check।**

```dart
bool hasDuplicate(List<int> nums) {
  final seen = <int>{};
  for (final n in nums) {
    if (!seen.add(n)) return true; // আগে থেকে থাকলে add false return করে
  }
  return false;
} // O(n) time, O(n) space — nested-loop O(n^2) থেকে অনেক ভালো
```

**ধাপ ৪ — Set-এর অঙ্ক।**
Set union, intersection আর difference support করে — group তুলনা করতে কাজে লাগে।

```dart
final a = {1, 2, 3};
final b = {2, 3, 4};
print(a.intersection(b)); // {2, 3}
print(a.union(b));        // {1, 2, 3, 4}
print(a.difference(b));   // {1}
```

**Interviewer কেন জিজ্ঞেস করে:** ধীর O(n²) "loop-এর ভেতরে search" code ঠিক করার সবচেয়ে সহজ উপায় হলো List-এর বদলে Set ব্যবহার করা।

**সাধারণ ভুল:** Loop-এর ভেতরে দেখা item track করতে List আর `contains` ব্যবহার করা — এটা O(n²)। Set এটাকে O(n) করে দেয়।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Sorted set?"* → `SplayTreeSet` item-গুলো sorted order-এ রাখে।
- *"এটা unique থাকে কীভাবে?"* → এটা `hashCode`/`==` ব্যবহার করে, ঠিক Map-এর key-এর মতোই ([Q7](#q7))।

**সম্পর্কিত:** [Q7 — Map (একই hashing)](#q7) · [Q19 — duplicate খোঁজা](#q19) · [Q3 — List](#q3)

[↑ উপরে ফিরুন](#toc)

---

# D. Tree ও graph

---

## <a id="q9"></a>9. Binary Tree কী, আর BFS ও DFS traversal কীভাবে কাজ করে?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q9)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Binary tree হলো node-এর গঠন, যেখানে প্রতিটা node-এর সর্বোচ্চ দুটো child থাকে — left আর right। BFS (breadth-first) queue ব্যবহার করে tree-টা level ধরে ধরে ঘোরে। DFS (depth-first) আগে একটা branch ধরে যতদূর সম্ভব গভীরে যায়, recursion বা stack দিয়ে। দুটোই প্রতিটা node-এ যায়, তাই দুটোই O(n)।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Node।**

```dart
class TreeNode {
  int value;
  TreeNode? left;
  TreeNode? right;
  TreeNode(this.value, [this.left, this.right]);
}
```

**ধাপ ২ — DFS (depth-first): আগে গভীরে যাওয়া, recursion দিয়ে।**
DFS একটা branch পুরোপুরি নিচে নেমে যায়, তারপর ফিরে আসে। তিনটা order-এর পার্থক্য শুধু *কখন* আপনি current node-এ visit করছেন:
- **In-order** (left, node, right) — binary search tree-এর ক্ষেত্রে এটা sorted order দেয়।
- **Pre-order** (node, left, right)।
- **Post-order** (left, right, node)।

```dart
void inOrder(TreeNode? node) {
  if (node == null) return;     // base case
  inOrder(node.left);           // বামে যাও
  print(node.value);            // visit
  inOrder(node.right);          // ডানে যাও
}
```

**ধাপ ৩ — BFS (breadth-first): level ধরে ধরে যাওয়া, queue দিয়ে।**
BFS প্রথমে depth 1-এর সব node visit করে, তারপর depth 2, এভাবে চলতে থাকে। Queue-তে থাকে সেই node-গুলো, যাদের visit করা বাকি।

```dart
import 'dart:collection';

void bfs(TreeNode? root) {
  if (root == null) return;
  final queue = Queue<TreeNode>()..add(root);
  while (queue.isNotEmpty) {
    final node = queue.removeFirst(); // FIFO
    print(node.value);
    if (node.left != null) queue.add(node.left!);
    if (node.right != null) queue.add(node.right!);
  }
}
```

**ধাপ ৪ — কোনটা কখন ব্যবহার করবেন।**
- **BFS** → unweighted graph-এ shortest path; "level order"; আগে সবচেয়ে কাছের neighbour।
- **DFS** → সব path ঘুরে দেখা; tree-এর depth; cycle ধরা; যেসব সমস্যা recursive মনে হয়।

**ধাপ ৫ — Complexity।**
দুটোই **O(n)** time (প্রতিটা node একবার)। Space: BFS queue-এর জন্য O(width) নেয়; DFS call stack-এর জন্য O(height) নেয়।

**Interviewer কেন জিজ্ঞেস করে:** Tree আর এই দুটো traversal অনেক interview সমস্যার ভিত্তি।

**সাধারণ ভুল:** দুটোকে গুলিয়ে ফেলা। মনে রাখুন: **BFS = queue (level ধরে ধরে)**, **DFS = recursion/stack (আগে গভীরে)**।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Binary Search Tree (BST)?"* → এমন binary tree যেখানে left < node < right। In-order DFS sorted output দেয়; balanced হলে search হয় O(log n), আর একটা chain-এ পরিণত হলে O(n)।
- *"Recursive vs iterative DFS?"* → Recursion call stack ব্যবহার করে; iterative DFS আলাদা একটা stack ব্যবহার করে ([Q5](#q5))।

**সম্পর্কিত:** [Q10 — graph (একই BFS/DFS)](#q10) · [Q6 — Queue (BFS)](#q6) · [Q15 — recursion (DFS)](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q10"></a>10. Graph কী, একে কীভাবে represent করবেন, আর তাতে BFS/DFS কীভাবে কাজ করে?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q10)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Graph হলো কিছু node (vertices), যেগুলো edge দিয়ে যুক্ত — শহর আর রাস্তার মানচিত্রের মতো। সবচেয়ে সাধারণ representation হলো adjacency list: প্রতিটি node থেকে তার neighbour-দের list-এ একটা Map। BFS আর DFS tree-এর মতোই কাজ করে, কিন্তু visited node track করতে হয়। কারণ graph-এ cycle থাকতে পারে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: শহর আর রাস্তা।**
শহরগুলো node; রাস্তাগুলো edge। Graph-এ cycle থাকতে পারে (আপনি ঘুরে আবার একই জায়গায় আসতে পারেন), tree-তে যা হয় না।

**ধাপ ২ — Representation: adjacency list (সবচেয়ে সাধারণ)।**

```dart
// Map: node -> তার neighbour-রা
final graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D'],
  'D': ['B', 'C'],
};
```

এটা O(V + E) জায়গা নেয় (V node + E edge) — বেশিরভাগ graph-এর জন্য efficient।

**ধাপ ৩ — Tree থেকে মূল পার্থক্য: visited track করা।**
Graph-এ loop থাকতে পারে। তাই কোন node আগেই visit করেছেন সেটা মনে রাখতে হবে। না হলে অনন্তকাল loop চলবে।

```dart
import 'dart:collection';

void bfs(Map<String, List<String>> g, String start) {
  final visited = <String>{start};      // আবার visit ঠেকাতে একটা Set
  final queue = Queue<String>()..add(start);
  while (queue.isNotEmpty) {
    final node = queue.removeFirst();
    print(node);
    for (final next in g[node] ?? []) {
      if (visited.add(next)) {          // আগে দেখা থাকলে add false দেয়
        queue.add(next);
      }
    }
  }
}
```

```dart
void dfs(Map<String, List<String>> g, String node, Set<String> visited) {
  if (!visited.add(node)) return; // আগেই visited → থামুন
  print(node);
  for (final next in g[node] ?? []) {
    dfs(g, next, visited);
  }
}
```

**ধাপ ৪ — Complexity।**
BFS আর DFS দুটোই **O(V + E)** — প্রতিটি node আর প্রতিটি edge একবার করে দেখা হয়।

**ধাপ ৫ — কখন কোনটা ব্যবহার করবেন।**
- **BFS** → unweighted graph-এ shortest path (সবচেয়ে কম hop)।
- **DFS** → cycle ধরা, connected component বের করা, topological sort।

**Interviewer কেন জিজ্ঞেস করে:** Graph traversal-এর উপরেই দাঁড়িয়ে আছে map, social network, dependency resolution, আর অনেক medium/hard সমস্যা।

**সাধারণ ভুল:** `visited` set ভুলে যাওয়া — cycle আছে এমন graph-এ এটা infinite loop তৈরি করে। (Tree-তে এটা লাগে না; graph-এ লাগে।)

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Adjacency list vs matrix?"* → List = neighbour-দের Map, O(V+E) জায়গা, sparse graph-এর জন্য ভালো। Matrix = true/false-এর 2D grid, O(V²) জায়গা, dense graph আর O(1) edge check-এর জন্য ভালো।
- *"Weighted shortest path?"* → Dijkstra-র algorithm ব্যবহার করুন (priority queue সহ BFS)।

**সম্পর্কিত:** [Q9 — tree (BFS/DFS)](#q9) · [Q6 — Queue (BFS)](#q6) · [Q8 — Set (visited)](#q8)

[↑ উপরে ফিরুন](#toc)

---

# E. Searching ও sorting

---

## <a id="q11"></a>11. Binary Search কীভাবে কাজ করে, আর কখন এটা ব্যবহার করা যায়?

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q11)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Binary search একটা sorted list-এ item খুঁজে দেয় O(log n)-এ, বারবার search range অর্ধেক করে কেটে। আপনি মাঝেরটা check করেন: সেটাই target হলে কাজ শেষ; target ছোট হলে বাম অর্ধেকে খুঁজুন; বড় হলে ডান অর্ধেকে। একটাই নিয়ম: list আগে থেকেই sorted হতে হবে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: dictionary-তে একটা শব্দ খোঁজা।**
আপনি dictionary পাতা ধরে ধরে পড়েন না। মাঝখানে খোলেন, দেখেন আপনার শব্দ তার আগে না পরে, আর অর্ধেক বাদ দিয়ে দেন। আবার একই কাজ। এটাই binary search।

**ধাপ ২ — Algorithm-টা।**

```dart
int binarySearch(List<int> sorted, int target) {
  var low = 0;
  var high = sorted.length - 1;
  while (low <= high) {
    final mid = low + (high - low) ~/ 2; // overflow এড়ায়; ~/ মানে integer ভাগ
    if (sorted[mid] == target) return mid;     // পাওয়া গেছে
    if (sorted[mid] < target) {
      low = mid + 1;   // target ডান অর্ধেকে আছে
    } else {
      high = mid - 1;  // target বাম অর্ধেকে আছে
    }
  }
  return -1; // পাওয়া যায়নি
}
```

**ধাপ ৩ — কেন এটা O(log n)।**
প্রতি ধাপে অর্ধেক item বাদ পড়ে যায়। 1,000,000 item-এর জন্য প্রায় 20 ধাপেই উত্তরে পৌঁছে যাবেন। "অর্ধেক করা"-র শক্তি এটাই।

**ধাপ ৪ — একটাই শর্ত: sorted input।**
Binary search শুধু sorted data-তে কাজ করে। Data sorted না হলে হয় আগে sort করুন (O(n log n)), নয়তো অন্য পথ নিন (O(1) lookup-এর জন্য Set/Map)।

**ধাপ ৫ — boundary-র দিকে খেয়াল রাখুন।**
দুটো ক্লাসিক bug: loop-এ `<=`-এর বদলে `<` ব্যবহার করা, আর `mid` হিসাব করা `(low + high) ~/ 2` দিয়ে (কিছু ভাষায় overflow হতে পারে — `low + (high - low) ~/ 2` নিরাপদ)।

**Interviewer কেন জিজ্ঞেস করে:** এটা যাচাই করে আপনি boundary সাবধানে সামলান কি না (off-by-one bug), আর "sorted input" দেখলে এটা ব্যবহারের সংকেত ধরতে পারেন কি না।

**সাধারণ ভুল:** Unsorted data-তে binary search ব্যবহার করা, বা `low`/`high`/`mid`-এ off-by-one ভুল করা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Duplicate থাকলে কী হবে?"* → প্রথম বা শেষ occurrence খুঁজতে এটাকে মানিয়ে নেওয়া যায়।
- *"Recursive version?"* → একই logic, কিন্তু recursion O(1)-এর বদলে O(log n) stack জায়গা নেয়।

**সম্পর্কিত:** [Q12 — sorting (আগে দরকার)](#q12) · [Q1 — Big-O (log n)](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q12"></a>12. Bubble, Insertion, Merge, আর Quick Sort ব্যাখ্যা করুন — পদ্ধতি আর complexity।

> Very common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q12)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Bubble আর Insertion sort সহজ, কিন্তু O(n²) — শুধু খুব ছোট বা প্রায়-sorted data-র জন্য ঠিক আছে। Merge sort সবসময় O(n log n) আর stable, কিন্তু O(n) বাড়তি জায়গা লাগে। Quick sort গড়ে O(n log n) আর in place sort করে, কিন্তু worst case-এ O(n²)। বাস্তবে Dart-এর built-in `sort()` একটা tuned hybrid ব্যবহার করে, তাই আমি নিজে খুব কমই sort লিখি।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Bubble Sort — বারবার পাশাপাশি দুটো swap করা। O(n²)।**
List ধরে হাঁটুন, উল্টো order-এ থাকা প্রতিটা জোড়া swap করুন; আর কোনো swap না লাগা পর্যন্ত চালান। সহজ, কিন্তু ধীর।

```dart
void bubbleSort(List<int> a) {
  for (var i = 0; i < a.length; i++) {
    for (var j = 0; j < a.length - 1 - i; j++) {
      if (a[j] > a[j + 1]) {
        final t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; // swap
      }
    }
  }
}
```

**ধাপ ২ — Insertion Sort — একটা একটা করে item নিয়ে sorted অংশ বানানো। O(n²), কিন্তু প্রায়-sorted data-তে দ্রুত।**
হাতে তাস sort করার মতো: পরের তাসটা নিন, আর আগে থেকেই sorted তাসগুলোর মধ্যে তার সঠিক জায়গায় ঢুকিয়ে দিন।

**ধাপ ৩ — Merge Sort — ভাগ করো আর জয় করো। সবসময় O(n log n), stable, O(n) জায়গা।**
List-টা অর্ধেক করে ভাগ করুন, প্রতি অর্ধেক sort করুন (recursively), তারপর দুটো sorted অর্ধেক merge করুন।

```dart
List<int> mergeSort(List<int> a) {
  if (a.length <= 1) return a;            // base case
  final mid = a.length ~/ 2;
  final left = mergeSort(a.sublist(0, mid));
  final right = mergeSort(a.sublist(mid));
  return _merge(left, right);
}

List<int> _merge(List<int> l, List<int> r) {
  final out = <int>[];
  var i = 0, j = 0;
  while (i < l.length && j < r.length) {
    if (l[i] <= r[j]) { out.add(l[i++]); } else { out.add(r[j++]); }
  }
  out.addAll(l.sublist(i));
  out.addAll(r.sublist(j));
  return out;
}
```

**ধাপ ৪ — Quick Sort — একটা pivot বাছুন, তার চারপাশে partition করুন। গড়ে O(n log n), worst O(n²), in place।**
একটা pivot বাছুন, ছোট item বামে আর বড় item ডানে সরান, তারপর প্রতি পাশ sort করুন। বাস্তবে দ্রুত; খারাপ pivot হলে worst case আসে (যেমন naive pivot দিয়ে আগে থেকেই sorted input)।

**ধাপ ৫ — তুলনার টেবিল।**

| Algorithm | Average | Worst | Space | Stable? |
|---|---|---|---|---|
| Bubble | O(n²) | O(n²) | O(1) | হ্যাঁ |
| Insertion | O(n²) | O(n²) | O(1) | হ্যাঁ |
| Merge | O(n log n) | O(n log n) | O(n) | হ্যাঁ |
| Quick | O(n log n) | O(n²) | O(log n) | না |

**Interviewer কেন জিজ্ঞেস করে:** divide-and-conquer চিন্তা আর complexity analysis যাচাই করার ক্লাসিক উপায় হলো sorting।

**সাধারণ ভুল:** quick sort-কে "সবসময় O(n log n)" বলা — এর worst case O(n²)। আর merge sort-কে in-place বলা — এটার O(n) বাড়তি জায়গা লাগে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"'stable' মানে কী?"* → সমান item-গুলো তাদের আগের আপেক্ষিক order ধরে রাখে। এক field ধরে sort করে অন্য field-এর order রাখতে চাইলে এটা কাজে লাগে।
- *"Dart-এর `list.sort()` কী ব্যবহার করে?"* → একটা tuned hybrid (ছোট অংশের জন্য insertion sort, বাকিটার জন্য merge-এর ধরনের)। আপনি খুব কমই নিজে হাতে sort লিখবেন।

**সম্পর্কিত:** [Q11 — binary search-এর sorted data লাগে](#q11) · [Q1 — Big-O](#q1) · [Q15 — recursion (merge/quick)](#q15)

[↑ উপরে ফিরুন](#toc)

---

# F. মূল কৌশল (Core techniques)

---

## <a id="q13"></a>13. Two Pointers technique কী, আর কখন এটা ব্যবহার করবেন?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q13)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Two pointers মানে nested loop-এর বদলে দুটো index variable ব্যবহার করা, যেগুলো list-এর ভেতর দিয়ে চলে। এটা অনেক O(n²) সমস্যাকে O(n)-এ নামিয়ে আনে। সাধারণ দুটো ধরন আছে — দুই pointer দুই প্রান্ত থেকে শুরু হয়ে মাঝের দিকে আসে, অথবা দুটোই একই দিকে আলাদা গতিতে চলে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: দুইজন মানুষ দুই প্রান্ত থেকে পড়ছেন।**
একটা শব্দ সামনে থেকে আর পেছন থেকে একই রকম পড়া যায় কি না দেখতে, একজন শুরু থেকে পড়েন আর আরেকজন শেষ থেকে, দুজনেই মাঝের দিকে আসেন। এটাই two pointers।

**ধাপ ২ — বিপরীত দুই প্রান্ত (sorted data-তে কাজ করে)।**
উদাহরণ: একটা sorted list-এ এমন দুটো সংখ্যা খুঁজুন যাদের যোগফল target-এর সমান।

```dart
List<int>? twoSumSorted(List<int> sorted, int target) {
  var left = 0;
  var right = sorted.length - 1;
  while (left < right) {
    final sum = sorted[left] + sorted[right];
    if (sum == target) return [left, right];
    if (sum < target) {
      left++;     // বড় sum দরকার → left pointer উপরে সরান
    } else {
      right--;    // ছোট sum দরকার → right pointer নিচে সরান
    }
  }
  return null;
} // O(n) time, O(1) space — O(n^2) nested loop-এর চেয়ে ভালো
```

**ধাপ ৩ — একই দিকে (fast আর slow pointer)।**
উদাহরণ: একটা sorted list থেকে duplicate সরান, একই জায়গায় (in place)। "slow" pointer দেখায় কোথায় লিখতে হবে; "fast" pointer সামনে গিয়ে scan করে।

```dart
int removeDuplicates(List<int> sorted) {
  if (sorted.isEmpty) return 0;
  var slow = 0;
  for (var fast = 1; fast < sorted.length; fast++) {
    if (sorted[fast] != sorted[slow]) {
      slow++;
      sorted[slow] = sorted[fast];
    }
  }
  return slow + 1; // unique অংশের length
}
```

**ধাপ ৪ — কীভাবে চিনবেন।**
খেয়াল করুন: একটা **sorted** list, **pair** খোঁজা, **দুই প্রান্ত** তুলনা করা, বা **in-place** সাজানো। এগুলো two pointers-এর ইঙ্গিত দেয়।

**Interviewer কেন জিজ্ঞেস করে:** brute force-কে linear time-এ নামানোর সবচেয়ে সাধারণ pattern-গুলোর একটা এটা।

**সাধারণ ভুল:** unsorted data-তে two pointers ব্যবহার করা, যখন কৌশলটার sorted input দরকার (বিপরীত-প্রান্ত ধরনটায়)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Two pointers vs sliding window?"* → Sliding window হলো two-pointer pattern-এর একটা বিশেষ রূপ, যেখানে দুই pointer-এর মাঝের ফাঁকটা একটা "window" — আপনি সেটা বড় আর ছোট করেন ([Q14](#q14))।

**সম্পর্কিত:** [Q14 — sliding window](#q14) · [Q22 — Two Sum](#q22) · [Q18 — palindrome](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q14"></a>14. Sliding Window technique কী, আর কখন এটা ব্যবহার করা উচিত?

> Common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q14)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Sliding window একটা list-এর কিছু অংশের উপর একটা 'window' রাখে আর সেটাকে slide করায়, শুরু থেকে আবার হিসাব করে না। Window এক ধাপ সরালে নতুন item যোগ হয় আর পুরোনো item বাদ যায় — তাই যে সমস্যা O(n²) দেখায়, সেটা O(n) হয়ে যায়। 'size k-এর সেরা subarray/substring' বা 'একটা নিয়ম মানে এমন সবচেয়ে লম্বা/ছোট range' ধরনের প্রশ্নে এটা ব্যবহার করুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: চলন্ত train-এর জানালা।**
Train-এর জানালা দিয়ে তাকালে আপনি একটা নির্দিষ্ট অংশের দৃশ্য দেখেন। Train এগোলে একটা নতুন গাছ দৃশ্যে ঢোকে আর একটা পুরোনো গাছ বেরিয়ে যায় — আপনাকে সবকিছু আবার scan করতে হয় না।

**ধাপ ২ — Fixed window — পরপর k-টা item-এর সর্বোচ্চ যোগফল।**

```dart
int maxSumOfK(List<int> a, int k) {
  var windowSum = 0;
  for (var i = 0; i < k; i++) windowSum += a[i]; // প্রথম window
  var best = windowSum;
  for (var i = k; i < a.length; i++) {
    windowSum += a[i] - a[i - k]; // নতুনটা যোগ, পুরোনোটা বাদ → প্রতি ধাপে O(1)
    if (windowSum > best) best = windowSum;
  }
  return best;
} // O(n*k)-এর বদলে O(n)
```

**ধাপ ৩ — Variable window — নিয়ম মানে এমন সবচেয়ে লম্বা range।**
`right` সরিয়ে window বড় করুন; নিয়ম ভাঙলে `left` সরিয়ে window ছোট করুন।

```dart
int longestUniqueSubstring(String s) {
  final seen = <String>{};
  var left = 0, best = 0;
  for (var right = 0; right < s.length; right++) {
    while (seen.contains(s[right])) {
      seen.remove(s[left]); // valid না হওয়া পর্যন্ত বাঁ দিক থেকে ছোট করুন
      left++;
    }
    seen.add(s[right]);     // ডান দিকে বড় করুন
    best = best > right - left + 1 ? best : right - left + 1;
  }
  return best;
}
```

**ধাপ ৪ — কীভাবে চিনবেন।**
খেয়াল করুন: "subarray/substring", "consecutive", "of size k", "একটা শর্ত মানে এমন সবচেয়ে লম্বা/ছোট range"। এগুলো sliding window-এর সংকেত।

**Interviewer কেন জিজ্ঞেস করে:** subarray/substring সমস্যার এটাই আদর্শ pattern, আর efficiency-তে বড় লাভ দেয়।

**সাধারণ ভুল:** প্রতিবার সরানোর সময় পুরো window আবার হিসাব করা (আবার O(n·k)-এ ফিরে যাওয়া)। আসল কৌশল হলো O(1)-এ update করা: যে item ঢুকছে সেটা যোগ করুন, যে item বেরোচ্ছে সেটা বাদ দিন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Fixed vs variable window?"* → Fixed = size সবসময় k। Variable = শর্তের উপর ভিত্তি করে বড়/ছোট হয়।

**সম্পর্কিত:** [Q13 — two pointers](#q13) · [Q8 — Set (window-এর ভেতরের জিনিস track করা)](#q8)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q15"></a>15. Recursion কীভাবে কাজ করে? Base case, call stack, আর tail recursion ব্যাখ্যা করুন।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q15)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Recursion হলো এমন একটা function যা নিজেকেই call করে, একই সমস্যার ছোট একটা অংশ সমাধান করতে। এর একটা base case লাগে — থামার শর্ত — নাহলে এটা চিরকাল চলবে। প্রতিটা call, গভীরের call শেষ না হওয়া পর্যন্ত call stack-এ অপেক্ষা করে। তাই গভীর recursion O(n) stack memory খরচ করে আর overflow হতে পারে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — বাস্তব জীবনের ছবি: Russian nesting doll.**
সবচেয়ে ছোট পুতুলটা খুঁজতে আপনি একটা পুতুল খোলেন, ভেতরে আরেকটা ছোট পুতুল পান, আর এটাই বারবার করেন। শেষে এমন একটা ছোট্ট পুতুল আসে যেটা আর খোলে না। ওই শেষ পুতুলটাই **base case**।

**ধাপ ২ — প্রতিটা recursion-এ দুটো অংশ লাগে।**
1. **Base case** — কখন থামতে হবে।
2. **Recursive case** — ছোট input নিয়ে নিজেকে call করা, base case-এর দিকে এগোতে এগোতে।

```dart
int factorial(int n) {
  if (n <= 1) return 1;          // base case (থামুন)
  return n * factorial(n - 1);   // recursive case (ছোট সমস্যা)
}
// factorial(3) = 3 * factorial(2) = 3 * 2 * factorial(1) = 3 * 2 * 1 = 6
```

**ধাপ ৩ — Call stack.**
প্রতিটা call stack-এ জমা হয় আর থেমে থাকে, যতক্ষণ না তার নিচেরটা return করে। `factorial(3)` অপেক্ষা করে `factorial(2)`-এর জন্য, আর সেটা অপেক্ষা করে `factorial(1)`-এর জন্য। Base case return করলে সবগুলো উপরের দিকে খুলে আসে। এই stack-এর কারণেই recursion **O(depth) memory** খরচ করে।

**ধাপ ৪ — Stack overflow.**
Base case না থাকলে, বা input বিশাল হলে, stack বাড়তেই থাকে আর memory শেষ হয়ে যায় — এটাই **StackOverflowError**। খুব গভীর সমস্যার জন্য iterative loop (নিজের stack বা queue ব্যবহার করে) বেশি নিরাপদ।

**ধাপ ৫ — Tail recursion.**
একটা call "tail recursive" তখনই, যখন recursive call-টাই function-এর একদম শেষ কাজ (এর পরে আর কিছু অপেক্ষা করে না)। কিছু language এটাকে loop-এ পরিণত করে optimize করে (stack বাড়ে না)। খেয়াল রাখুন: Dart tail-call optimization-এর **কোনো** guarantee দেয় না। তাই Dart-এ গভীর recursion-এর জন্য loop-ই ভালো।

```dart
// Tail-recursive style (accumulator ফলাফল বয়ে নিয়ে যায়)
int factorialTail(int n, [int acc = 1]) {
  if (n <= 1) return acc;
  return factorialTail(n - 1, acc * n); // শেষ কাজটাই এই call
}
```

**Interviewer কেন জিজ্ঞেস করে:** tree, graph আর divide-and-conquer-এর জন্য recursion স্বাভাবিক হাতিয়ার। তাঁরা দেখতে চান আপনি সবসময় base case ঠিক করেন কি না, আর stack-এর খরচ বোঝেন কি না।

**সাধারণ ভুল:** base case ভুলে যাওয়া (অসীম recursion → stack overflow), বা base case-এর দিকে না এগোনো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Recursion vs iteration?"* → ক্ষমতা একই। Tree/graph সমস্যায় recursion বেশি পরিষ্কার; iteration stack-overflow-এর ঝুঁকি এড়ায় আর কম memory নেয়।
- *"ধীর recursion কীভাবে দ্রুত করবেন?"* → memoization যোগ করুন ([Q16](#q16) আর [Q21](#q21) দেখুন)।

**সম্পর্কিত:** [Q16 — dynamic programming](#q16) · [Q9 — DFS (recursion)](#q9) · [Q2 — stack space](#q2)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q16"></a>16. Dynamic Programming কী, আর memoization ও tabulation-এর পার্থক্য কী?

> Common · Medium–Hard · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q16)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dynamic programming (DP) একটা বড় সমস্যা সমাধান করে ছোট ছোট overlapping sub-problem-এর উত্তর জোড়া দিয়ে। আর প্রতিটা sub-answer জমা রাখে, যাতে সেটা একবারই হিসাব হয়। Memoization হলো top-down: সাধারণ recursion-এর সাথে একটা cache। Tabulation হলো bottom-up: সবচেয়ে ছোট case থেকে শুরু করে একটা table ভরা। দুটোই ধীর exponential recursion-কে দ্রুত linear time-এ নিয়ে আসে।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — DP কখন কাজে লাগে।**
DP এমন সমস্যায় খাটে যার দুটো বৈশিষ্ট্য আছে:
1. **Overlapping sub-problems** — একই ছোট সমস্যা বারবার সমাধান করতে হয়।
2. **Optimal substructure** — সেরা উত্তরটা sub-problem-গুলোর সেরা উত্তর দিয়ে তৈরি হয়।

সবচেয়ে পরিচিত উদাহরণ Fibonacci: সাধারণ recursion একই মান বারবার হিসাব করে (O(2ⁿ))।

**ধাপ ২ — Memoization (top-down): recursion + একটা cache.**
Recursion দিয়েই সমাধান করুন, কিন্তু প্রতিটা উত্তর একটা Map-এ মনে রাখুন। তাহলে কখনোই আবার হিসাব করতে হবে না।

```dart
int fib(int n, [Map<int, int>? memo]) {
  memo ??= {};
  if (n <= 1) return n;                 // base case
  if (memo.containsKey(n)) return memo[n]!; // আগেই হিসাব হয়েছে → আবার ব্যবহার
  return memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
} // O(n) time, O(n) space — O(2^n) থেকে নেমে এসেছে
```

**ধাপ ৩ — Tabulation (bottom-up): শুরু থেকে table ভরুন।**
সবচেয়ে ছোট case থেকে শুরু করে উপরের দিকে গড়ে তুলুন, কোনো recursion নেই।

```dart
int fibTab(int n) {
  if (n <= 1) return n;
  final dp = List.filled(n + 1, 0);
  dp[1] = 1;
  for (var i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2]; // ছোট উত্তর থেকে তৈরি
  }
  return dp[n];
} // O(n) time; শেষ দুটো মান রাখলে O(1) space-এ নামানো যায়
```

**ধাপ ৪ — কোনটা ব্যবহার করবেন।**
- **Memoization** — লেখা সহজ (স্বাভাবিক recursion-এ শুধু একটা cache যোগ করুন); stack space খরচ করে।
- **Tabulation** — recursion নেই (stack-overflow-এর ঝুঁকি নেই); space optimize করা প্রায়ই সহজ।

**Interviewer কেন জিজ্ঞেস করে:** DP একটা সাধারণ medium/hard বিষয়। তাঁরা দেখতে চান আপনি বারবার হওয়া কাজ ধরতে পারেন কি না, আর সেটা cache করেন কি না।

**সাধারণ ভুল:** যেখানে overlapping sub-problem নেই সেখানে DP ব্যবহার করা (তখন এটা শুধু সাধারণ recursion)। অথবা ফলাফল সত্যিই জমা/পুনরায় ব্যবহার করতে ভুলে যাওয়া।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"কিছু পরিচিত DP সমস্যা বলুন।"* → Fibonacci, climbing stairs, coin change, longest common subsequence, knapsack।
- *"Top-down vs bottom-up trade-off?"* → Top-down শুধু দরকারি sub-problem হিসাব করে; bottom-up সবগুলো হিসাব করে কিন্তু recursion-এর বাড়তি খরচ এড়ায়।

**সম্পর্কিত:** [Q15 — recursion](#q15) · [Q21 — Fibonacci (উদাহরণটা)](#q21) · [Q7 — Map cache হিসেবে](#q7)

[↑ উপরে ফিরুন](#toc)

---

# G. সাধারণ coding সমস্যা (Dart)

---

## <a id="q17"></a>17. একটা function লিখুন যেটা একটা string reverse করে।

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q17)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Dart-এ সবচেয়ে সহজ সঠিক উপায় হলো string-টাকে character-এ split করা, list-টা reverse করা, তারপর আবার join করা। এটা O(n) time আর O(n) space। যদি character-এর list-এ in place করতে বলা হয়, আমি দুই দিক থেকে swap করা two pointers ব্যবহার করব।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — পরিষ্কার Dart উপায়।**

```dart
String reverse(String s) => s.split('').reversed.join();
// reverse('hello') -> 'olleh'
```

এটা O(n) time আর O(n) space (একটা নতুন string তৈরি হয়)।

**ধাপ ২ — Two-pointer উপায় (ভেতরের ধারণাটা দেখায়)।**
Interviewer কখনো কখনো হাতে লেখা version চান, যাতে বোঝা যায় আপনি ভেতরের কাজটা বোঝেন।

```dart
String reverseManual(String s) {
  final chars = s.split('');
  var left = 0, right = chars.length - 1;
  while (left < right) {
    final t = chars[left]; chars[left] = chars[right]; chars[right] = t; // swap
    left++;
    right--;
  }
  return chars.join();
}
```

**ধাপ ৩ — ফাঁদ: emoji আর accent।**
কিছু character (emoji, accent দেওয়া অক্ষর) একাধিক code unit দিয়ে তৈরি। সাদামাটা reverse এগুলো ভেঙে ফেলতে পারে। Interview-এর জন্য সহজ version-টাই যথেষ্ট। শুধু বলুন যে আপনি জানেন — ঠিকমতো Unicode reverse করতে `characters` package লাগে (`s.characters.toList().reversed`)।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা warm-up প্রশ্ন। এটা মৌলিক string handling দেখে, আর দেখে আপনি two-pointer swap জানেন কি না।

**সাধারণ ভুল:** Dart `String`-কে array-র মতো index করে জায়গাতেই swap করার চেষ্টা করা — string immutable, তাই আগে list-এ convert করতেই হবে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Built-in ছাড়া reverse করুন?"* → উপরের two-pointer version ব্যবহার করুন।
- *"অক্ষর নয়, শব্দগুলো reverse করুন?"* → `s.split(' ').reversed.join(' ')`।

**সম্পর্কিত:** [Q13 — two pointers](#q13) · [Q18 — palindrome](#q18)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q18"></a>18. একটা function লিখুন যেটা check করে string-টা palindrome কি না।

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q18)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Palindrome সামনে থেকে আর পেছন থেকে একইরকম পড়া যায়। সবচেয়ে পরিষ্কার check-এ two pointers লাগে — একটা শুরু থেকে, একটা শেষ থেকে। দুটো মাঝের দিকে এগোতে এগোতে character তুলনা করে। এটা O(n) time আর O(1) extra space।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — দুই প্রান্ত থেকে two pointers।**

```dart
bool isPalindrome(String s) {
  var left = 0, right = s.length - 1;
  while (left < right) {
    if (s[left] != s[right]) return false; // মিল নেই → palindrome নয়
    left++;
    right--;
  }
  return true;
} // O(n) time, O(1) extra space
```

**ধাপ ২ — বাস্তব জীবনের "clean" version (case আর অ-অক্ষর বাদ দিন)।**
Interviewer প্রায়ই জিজ্ঞেস করেন: "A man, a plan, a canal: Panama" কি palindrome? হ্যাঁ — space, যতিচিহ্ন আর case বাদ দিলে।

```dart
bool isPalindromeClean(String s) {
  final cleaned = s.toLowerCase().replaceAll(RegExp(r'[^a-z0-9]'), '');
  var left = 0, right = cleaned.length - 1;
  while (left < right) {
    if (cleaned[left] != cleaned[right]) return false;
    left++;
    right--;
  }
  return true;
}
```

**ধাপ ৩ — ছোট version (কিন্তু বেশি memory)।**

```dart
bool isPalindromeSimple(String s) => s == s.split('').reversed.join();
```

এটা O(n) space, কারণ এটা একটা reverse করা copy তৈরি করে। Two-pointer version ভালো (O(1) space)।

**Interviewer কেন জিজ্ঞেস করে:** এটা একটা পরিষ্কার two-pointer warm-up। তাঁরা আপনাকে case/যতিচিহ্ন handle করতে চাপ দিতে পারেন। এতে খুঁটিনাটির প্রতি মনোযোগ যাচাই হয়।

**সাধারণ ভুল:** প্রশ্নে ইঙ্গিত থাকা সত্ত্বেও input clean করতে ভুলে যাওয়া ("space আর case বাদ দিন")। অথবা O(1) space সম্ভব হওয়া সত্ত্বেও reverse করা copy বানানো।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"একটা সংখ্যা palindrome কি না check করুন?"* → String-এ convert করুন, অথবা গণিত দিয়ে সংখ্যাটা reverse করুন।

**সম্পর্কিত:** [Q13 — two pointers](#q13) · [Q17 — string reverse](#q17)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q19"></a>19. একটা function লিখুন যেটা একটা list-এর সব duplicate element খুঁজে বের করে।

> Common · Easy–Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q19)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"List-টা একবার হাঁটুন, আর যেগুলো আগে দেখেছেন সেগুলোর একটা Set রাখুন। কোনো item আগে থেকেই Set-এ থাকলে সেটা duplicate। এটা O(n) time আর O(n) space — প্রতিটা জোড়া তুলনা করার চেয়ে অনেক ভালো, যেটা O(n²)।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — কার্যকর উপায়: একটা 'seen' Set।**

```dart
Set<int> findDuplicates(List<int> nums) {
  final seen = <int>{};
  final duplicates = <int>{};
  for (final n in nums) {
    if (!seen.add(n)) {  // n আগে থেকেই থাকলে add false return করে
      duplicates.add(n);
    }
  }
  return duplicates;
} // O(n) time, O(n) space
```

**ধাপ ২ — Nested loop কেন নয়?**
প্রতিটা item-কে বাকি প্রতিটা item-এর সাথে তুলনা করা O(n²) — বড় input-এ অনেক ধীর। Set "এটা কি আগে দেখেছি?" check-টাকে O(1) বানিয়ে দেয়।

```dart
// এই O(n^2) পদ্ধতিটা এড়িয়ে চলুন:
// প্রতিটা i-এর জন্য, প্রতিটা j-এর জন্য, nums[i] আর nums[j] তুলনা
```

**ধাপ ৩ — কোনটা কতবার আসে সেটা গোনা।**
শুধু কোনগুলো বারবার আসে তা নয়, count দরকার হলে Map ব্যবহার করুন।

```dart
Map<int, int> counts(List<int> nums) {
  final map = <int, int>{};
  for (final n in nums) {
    map[n] = (map[n] ?? 0) + 1; // এক বাড়ান, default 0
  }
  return map; // যেমন {1: 3, 2: 1}
}
```

**Interviewer কেন জিজ্ঞেস করে:** "O(n²) nested loop এড়াতে Set/Map ব্যবহার করুন" — এটার সবচেয়ে সহজ উদাহরণ এটাই।

**সাধারণ ভুল:** দেখা item track করতে List আর `contains` ব্যবহার করা — প্রতিটা check-এ O(n), ফলে মোট O(n²)। Set ব্যবহার করুন।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"প্রথম non-repeating element খুঁজুন?"* → Map দিয়ে count করুন, তারপর count 1 আছে এমন প্রথম item খুঁজতে scan করুন।
- *"O(1) space-এ duplicate খুঁজুন?"* → শুধু বিশেষ শর্তে সম্ভব (যেমন value একটা জানা range-এ, অথবা input বদলানোর অনুমতি আছে)।

**সম্পর্কিত:** [Q8 — Set](#q8) · [Q7 — Map (counting)](#q7)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q20"></a>20. FizzBuzz লিখুন।

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q20)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"1 থেকে n পর্যন্ত সংখ্যার জন্য: 3 আর 5 দুটো দিয়েই ভাগ গেলে 'FizzBuzz' print করুন, নাহলে 3 দিয়ে ভাগ গেলে 'Fizz', নাহলে 5 দিয়ে ভাগ গেলে 'Buzz', নাহলে সংখ্যাটাই। মূল কথা — দুটোর case (15) আগে check করা, নাহলে ওটা কখনোই চলে না।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সোজাসাপ্টা সমাধান।**

```dart
void fizzBuzz(int n) {
  for (var i = 1; i <= n; i++) {
    if (i % 15 == 0) {
      print('FizzBuzz');     // 3 আর 5 দুটো দিয়েই ভাগ যায় — আগে check করুন
    } else if (i % 3 == 0) {
      print('Fizz');
    } else if (i % 5 == 0) {
      print('Buzz');
    } else {
      print(i);
    }
  }
}
```

**ধাপ ২ — Order কেন গুরুত্বপূর্ণ।**
`i % 15`-এর আগে `i % 3` check করলে 15 "Fizz" print করবে। তখন "FizzBuzz" branch কখনোই চলবে না। সবচেয়ে নির্দিষ্ট শর্তটা (দুটোই) সবসময় আগে check করুন।

**ধাপ ৩ — পরিষ্কার, বাড়ানো যায় এমন version।**
String-টা যোগ করে করে বানান, যাতে পরে নতুন নিয়ম যোগ করা সহজ হয়।

```dart
void fizzBuzz2(int n) {
  for (var i = 1; i <= n; i++) {
    var out = '';
    if (i % 3 == 0) out += 'Fizz';
    if (i % 5 == 0) out += 'Buzz';
    print(out.isEmpty ? '$i' : out); // খালি মানে কোনো নিয়ম মেলেনি
  }
}
```

**Interviewer কেন জিজ্ঞেস করে:** এটা মৌলিক control flow আর modulo operator-এর দ্রুত যাচাই — আর আপনি order-এর ফাঁদটা ধরতে পারেন কি না তাও দেখে।

**সাধারণ ভুল:** 15-এর case-এর আগে 3 আর 5 check করা, ফলে 15-এর গুণিতক কখনোই "FizzBuzz" print করে না।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"নতুন একটা নিয়ম যোগ করুন (যেমন 7 → 'Bazz')?"* → দ্বিতীয় version-এ এটা খুব সহজ: আরেকটা `if` যোগ করুন।

**সম্পর্কিত:** [Q1 — Big-O (এটা O(n))](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q21"></a>21. n-তম Fibonacci সংখ্যা বের করুন — iterative, recursive, আর memoized।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q21)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"Fibonacci মানে প্রতিটা সংখ্যা আগের দুটোর যোগফল। সাধারণ recursion O(2ⁿ), কারণ এটা একই মান বারবার হিসাব করে। Iterative version O(n) time আর O(1) space — interview-এর জন্য সেরা। Memoization দিলেও recursion O(n) হয়ে যায়।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — সাধারণ recursion (এটা production-এ পাঠাবেন না)।**

```dart
int fibSlow(int n) {
  if (n <= 1) return n;
  return fibSlow(n - 1) + fibSlow(n - 2); // একই call বারবার হয় → O(2^n)
}
```

Code পরিষ্কার, কিন্তু খরচ বিস্ফোরিত হয়: `fibSlow(50)` একশো কোটির বেশি call করে।

**ধাপ ২ — Iterative — সেরা উত্তর (O(n) time, O(1) space)।**
শুধু শেষ দুটো সংখ্যা রাখুন, আর সামনে এগোতে থাকুন।

```dart
int fib(int n) {
  if (n <= 1) return n;
  var prev = 0, curr = 1;
  for (var i = 2; i <= n; i++) {
    final next = prev + curr;
    prev = curr;
    curr = next;
  }
  return curr;
}
```

**ধাপ ৩ — Memoized recursion (O(n) time, O(n) space)।**
তাঁরা recursive সমাধান চাইলে একটা cache যোগ করুন। তাহলে প্রতিটা মান একবারই হিসাব হবে (এটাই dynamic programming — দেখুন [Q16](#q16))।

```dart
int fibMemo(int n, [Map<int, int>? memo]) {
  memo ??= {};
  if (n <= 1) return n;
  if (memo.containsKey(n)) return memo[n]!;
  return memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
}
```

**ধাপ ৪ — তুলনা।**

| পদ্ধতি | Time | Space |
|---|---|---|
| সাধারণ recursion | O(2ⁿ) | O(n) stack |
| Memoized recursion | O(n) | O(n) |
| Iterative | O(n) | O(1) |

**Interviewer কেন জিজ্ঞেস করে:** বারবার একই কাজ করার খরচ দেখানোর সবচেয়ে পরিষ্কার উপায় এটা। আর memoization/iteration কীভাবে সেটা ঠিক করে, তাও বোঝা যায়।

**সাধারণ ভুল:** শুধু সাধারণ recursion দেওয়া, আর এটা exponential সেটা না বলা। অথবা O(1)-space iterative version না জানা।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"Production-এ কোনটা ব্যবহার করবেন?"* → Iterative version — সবচেয়ে দ্রুত আর সবচেয়ে কম memory।

**সম্পর্কিত:** [Q16 — dynamic programming](#q16) · [Q15 — recursion](#q15)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q22"></a>22. Two Sum — এমন দুটো index বের করুন যাদের মান যোগ করলে target হয়।

> Very common · Medium · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q22)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"List-টা একবার ঘুরুন, আর একটা Map-এ প্রতিটা মান আর তার index রাখুন। প্রতিটা সংখ্যার জন্য দেখুন 'target বিয়োগ এই সংখ্যা' Map-এ আগেই আছে কি না — থাকলে জোড়া পাওয়া গেল। এটা O(n) time আর O(n) space। অন্যদিকে nested-loop brute force O(n²)।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — Brute force (এটা বলুন, তারপর উন্নত করুন)।**
দুটো loop দিয়ে প্রতিটা জোড়া check করুন: O(n²)। কাজ করে, কিন্তু ধীর।

**ধাপ ২ — সেরা সমাধান: Map দিয়ে এক pass।**
কৌশলটা এই: এগোনোর সময় প্রতিটা দেখা সংখ্যা আর তার জায়গা মনে রাখুন। বর্তমান সংখ্যার জন্য দরকারি সঙ্গী হলো `target - current`। সেই সঙ্গীকে আগেই দেখে থাকলে কাজ শেষ।

```dart
List<int>? twoSum(List<int> nums, int target) {
  final seen = <int, int>{}; // value -> index
  for (var i = 0; i < nums.length; i++) {
    final need = target - nums[i];
    if (seen.containsKey(need)) {
      return [seen[need]!, i]; // জোড়া পাওয়া গেল
    }
    seen[nums[i]] = i;         // এই সংখ্যাটা পরের জন্য মনে রাখুন
  }
  return null;                 // কোনো জোড়া নেই
}
// twoSum([2, 7, 11, 15], 9) -> [0, 1]  কারণ 2 + 7 = 9
```

**ধাপ ৩ — কেন এটাই ক্লাসিক "Map nested loop-কে হারায়" উদাহরণ।**
"সঙ্গী কি list-এর কোথাও আছে?" — এই প্রশ্নটা Map O(n) search থেকে O(1) lookup-এ নামিয়ে আনে। একটাই loop-এর ভেতরে সেই O(1) check করলে মোট খরচ O(n) হয়।

**ধাপ ৪ — Time/space trade-off।**
সময় বাঁচাতে আমরা O(n) বাড়তি memory খরচ করি (Map-টা)। খরচ O(n²) থেকে O(n)-এ নামে। এই বদলটা প্রায় সবসময়ই লাভজনক।

**Interviewer কেন জিজ্ঞেস করে:** "hash map দিয়ে O(n²) থেকে O(n)-এ নামা" — এর সবচেয়ে বিখ্যাত প্রশ্ন এটাই। তাঁরা দেখতে চান আপনি Map-এর দিকে হাত বাড়ান কি না।

**সাধারণ ভুল:** brute-force O(n²) দিয়ে থেমে যাওয়া। আরেকটা ভুল — check করার *আগে* বর্তমান সংখ্যাটা Map-এ যোগ করা। এতে একটা সংখ্যা ভুলভাবে নিজের সাথেই জোড়া লেগে যেতে পারে।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"List sorted হলে কী করবেন?"* → দুই প্রান্ত থেকে two pointers ব্যবহার করুন ([Q13](#q13)), তাতে বাড়তি space O(1)।
- *"কোনো জোড়া না থাকলে?"* → null বা খালি ফেরত দিন, আর কথাটা স্পষ্ট করে বলুন।

**সম্পর্কিত:** [Q7 — Map](#q7) · [Q13 — two pointers (sorted version)](#q13) · [Q1 — Big-O](#q1)

[↑ উপরে ফিরুন](#toc)

---

## <a id="q23"></a>23. `max()` ব্যবহার না করে list-এর সবচেয়ে বড় মান বের করুন।

> Common · Easy · [🇬🇧 English](../software-engineer-flutter/section-11-data-structure.md#q23)

**সংক্ষিপ্ত উত্তর (এটাই বলুন):**
"একটা 'এখন পর্যন্ত সেরা' variable রাখুন। প্রথম element দিয়ে শুরু করুন। তারপর list-টা একবার ঘুরুন, আর বড় কিছু পেলেই সেটা update করুন। এটা O(n) time আর O(1) space। মূল edge case হলো খালি list — throw করবেন নাকি null ফেরত দেবেন, ঠিক করুন।"

**এবার পুরোটা বুঝি:**

**ধাপ ১ — এক pass-এর সমাধান।**

```dart
int findMax(List<int> nums) {
  if (nums.isEmpty) {
    throw ArgumentError('list is empty'); // edge case স্পষ্টভাবে handle করুন
  }
  var best = nums[0];               // প্রথম item দিয়ে শুরু
  for (var i = 1; i < nums.length; i++) {
    if (nums[i] > best) best = nums[i]; // বড় কিছু পেলে update করুন
  }
  return best;
} // O(n) time, O(1) space
```

**ধাপ ২ — `nums[0]` থেকে শুরু কেন, 0 থেকে নয় কেন?**
`best = 0` দিয়ে শুরু করলে আর সব সংখ্যা negative হলে ভুলভাবে 0 ফেরত আসবে। প্রথম আসল element দিয়ে শুরু করলে এই bug হয় না।

**ধাপ ৩ — খালি list-এর জন্য null-safe version।**
throw করা না চাইলে একটা nullable মান ফেরত দিন:

```dart
int? findMaxOrNull(List<int> nums) {
  if (nums.isEmpty) return null;
  var best = nums.first;
  for (final n in nums) {
    if (n > best) best = n;
  }
  return best;
}
```

**Interviewer কেন জিজ্ঞেস করে:** এটা loop চালানো, "এখন পর্যন্ত সেরা" accumulator রাখা, আর খালি list-এর edge case handle করার সহজ পরীক্ষা।

**সাধারণ ভুল:** `best = 0` দিয়ে শুরু করা (সব negative list-এ ভেঙে যায়)। অথবা খালি list-এর কথা ভুলে যাওয়া (`nums[0]`-এ crash করে)।

**যে Follow-up প্রশ্ন আসতে পারে:**
- *"দ্বিতীয় সবচেয়ে বড়টা বের করুন?"* → এক pass-এ দুটো variable রাখুন (largest আর secondLargest)।
- *"min আর max দুটোই বের করুন?"* → একই loop-এ দুটো accumulator রাখুন।

**সম্পর্কিত:** [Q1 — Big-O (O(n))](#q1) · [Q3 — List](#q3)

[↑ উপরে ফিরুন](#toc)

---


# <a id="cheatsheet"></a>Cheat Sheet (শেষ রাতের review)

Interview-এর দিন সকালে এটা পড়ুন। আগে table, তারপর এক লাইনের মনে করিয়ে দেওয়া কথা।

## সাধারণ operation-এর Big-O

| Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| List (array) | O(1) | O(n) | O(n) (শেষে: O(1) amortized) | O(n) (শেষে: O(1)) |
| Linked List | O(n) | O(n) | O(1) জানা node-এ | O(1) জানা node-এ |
| Map / Set (hash) | — | O(1) avg | O(1) avg | O(1) avg |
| Stack / Queue | — | — | O(1) | O(1) |
| Binary Search Tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |

## Sorting এক নজরে

| Algorithm | Average | Worst | Space | Stable |
|---|---|---|---|---|
| Bubble / Insertion | O(n²) | O(n²) | O(1) | হ্যাঁ |
| Merge | O(n log n) | O(n log n) | O(n) | হ্যাঁ |
| Quick | O(n log n) | O(n²) | O(log n) | না |

## কোন structure / technique ব্যবহার করবেন

| প্রয়োজন | যা ব্যবহার করবেন |
|---|---|
| Key দিয়ে দ্রুত lookup | Map ([Q7](#q7)) |
| Uniqueness / "আগে দেখেছি?" | Set ([Q8](#q8)) |
| LIFO (undo, navigation) | Stack ([Q5](#q5)) |
| FIFO / BFS | Queue ([Q6](#q6)) |
| Sorted data-তে search | Binary search ([Q11](#q11)) |
| Sorted data-তে pair / দুই প্রান্ত | Two pointers ([Q13](#q13)) |
| সেরা subarray/substring | Sliding window ([Q14](#q14)) |
| বারবার একই sub-problem | Dynamic programming ([Q16](#q16)) |

## এক লাইনের মনে রাখার কথা

- **Big-O** = input বাড়লে কাজ কতটা বাড়ে। Constant বাদ দিন, সবচেয়ে বড় term রাখুন। ([Q1](#q1))
- **Space** মানে EXTRA memory, recursion call stack সহ। ([Q2](#q2))
- **List**: index O(1), search O(n), মাঝখানে insert O(n)। ([Q3](#q3))
- **Map/Set**: গড়ে O(1) lookup — O(n²) nested loop-এর ওষুধ। ([Q7](#q7), [Q8](#q8))
- **Stack** = LIFO (`add`/`removeLast`); **Queue** = FIFO (`Queue.removeFirst`)। ([Q5](#q5), [Q6](#q6))
- **Binary search** = O(log n), কিন্তু শুধু sorted data-তে। ([Q11](#q11))
- **Merge** = সবসময় O(n log n), O(n) space; **Quick** = গড়ে O(n log n), সবচেয়ে খারাপ O(n²), in place। ([Q12](#q12))
- **BFS = queue (level ধরে ধরে)**, **DFS = recursion/stack (আগে গভীরে)**; দুটোই O(n) / O(V+E)। ([Q9](#q9), [Q10](#q10))
- **Graph-এ `visited` set লাগবেই**, নাহলে BFS/DFS অনন্তকাল ঘুরতে থাকবে। ([Q10](#q10))
- **Two pointers / sliding window** O(n²)-কে O(n) বানিয়ে দেয়। ([Q13](#q13), [Q14](#q14))
- **Recursion**-এ base case লাগে; খুব গভীর recursion stack overflow করতে পারে। ([Q15](#q15))
- **DP** = overlapping sub-problem cache করা: memoization (top-down) বা tabulation (bottom-up)। ([Q16](#q16))
- **Two Sum** = এক pass + একটা Map; ক্লাসিক O(n²) → O(n) কৌশল। ([Q22](#q22))

[↑ উপরে ফিরুন](#toc)

---

# অনুশীলন: Interviewer-রা কীভাবে আরও গভীরে যান

Interviewer-রা "সমাধান করুন" বলেই থেমে যান না। তাঁরা efficiency নিয়ে চাপ দেন। এই চেইনটা মুখে বলে অনুশীলন করুন:

1. *"Two Sum solve করুন।"* → দুটো loop দিয়ে brute force, O(n²)।
2. *"আরও ভালো করা যায়?"* → দেখা মানগুলোর একটা Map ব্যবহার করুন → O(n) time।
3. *"Trade-off কী?"* → Map-এর জন্য O(n) extra space; time-এর বদলে space।
4. *"List sorted হলে কী করবেন?"* → দুই প্রান্ত থেকে two pointers → O(1) extra space।
5. *"কোনো বৈধ pair না থাকলে?"* → null/খালি return করুন আর সেটা বলে দিন; edge case handle করুন।

আপনার প্রথম ধারণার Big-O সবসময় বলে দিন, তারপর মুখে বলতে বলতে সেটা উন্নত করুন। Brute force থেকে optimal পর্যন্ত যাত্রাটা দেখানোই senior signal এনে দেয় — remote আর BD দুই ধরনের interview-তেই।

[↑ উপরে ফিরুন](#toc)
