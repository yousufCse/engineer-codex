# Chapter 16 — Moderate (প্রশ্ন 16.1 – 16.26)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Dart + Python** দুটোতেই।
> এই chapter একটা mixed bag — নানা topic-এর "moderate" সমস্যা। আগের chapter গুলোর technique (Hash Map, math, bit, two-pointer, simulation) এখানে ঘুরেফিরে লাগবে।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Threads & Locks](chapter15_threads_locks.md) · [পরের: Hard](chapter17_hard.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
এটা একটা mixed chapter — কোনো single topic নেই। নিচের ২৬টা প্রশ্ন:
   16.1  Number Swapper        — temp ছাড়া দুটো সংখ্যা swap
   16.2  Word Frequencies      — কোনো শব্দ কতবার আছে
   16.3  Intersection          — দুটো line segment-এর intersection point
   16.4  Tic Tac Win           — কেউ জিতেছে কিনা
   16.5  Factorial Zeros       — n!-এর শেষে কয়টা 0
   16.6  Smallest Difference   — দুই array-র সবচেয়ে কাছের জোড়া
   16.7  Number Max            — if/compare ছাড়া max(a,b)
   16.8  English Int           — সংখ্যাকে ইংরেজি শব্দে
   16.9  Operations            — শুধু + দিয়ে - × ÷
   16.10 Living People         — কোন সালে সবচেয়ে বেশি লোক বেঁচে ছিল
   16.11 Diving Board          — short/long plank দিয়ে সম্ভব length
   16.12 XML Encoding          — XML কে compact encoding-এ
   16.13 Bisect Squares        — দুটো square কে সমান দু'ভাগ করা line
   16.14 Best Line             — সবচেয়ে বেশি point যে line-এ
   16.15 Master Mind           — hits ও pseudo-hits গোনা
   16.16 Sub Sort              — কোন অংশটা sort করলে পুরোটা sorted
   16.17 Contiguous Sequence   — সবচেয়ে বড় sum-এর subarray
   16.18 Pattern Matching      — a/b pattern string-এ মেলে কিনা
   16.19 Pond Sizes            — connected জলের আকার (flood fill)
   16.20 T9                    — phone keypad থেকে শব্দ
   16.21 Sum Swap              — দুই array থেকে এক জোড়া swap করে sum সমান
   16.22 Langton's Ant         — grid-এ ant-এর simulation
   16.23 Rand7 from Rand5      — rand5() দিয়ে uniform rand7()
   16.24 Pairs with Sum        — sum = target এমন জোড়া
   16.25 LRU Cache             — least-recently-used cache
   16.26 Calculator           — expression evaluate (precedence সহ)
```

**প্রশ্নসমূহ:**
- [16.1 — Number Swapper](#q16-1)
- [16.2 — Word Frequencies](#q16-2)
- [16.3 — Intersection](#q16-3)
- [16.4 — Tic Tac Win](#q16-4)
- [16.5 — Factorial Zeros](#q16-5)
- [16.6 — Smallest Difference](#q16-6)
- [16.7 — Number Max](#q16-7)
- [16.8 — English Int](#q16-8)
- [16.9 — Operations](#q16-9)
- [16.10 — Living People](#q16-10)
- [16.11 — Diving Board](#q16-11)
- [16.12 — XML Encoding](#q16-12)
- [16.13 — Bisect Squares](#q16-13)
- [16.14 — Best Line](#q16-14)
- [16.15 — Master Mind](#q16-15)
- [16.16 — Sub Sort](#q16-16)
- [16.17 — Contiguous Sequence](#q16-17)
- [16.18 — Pattern Matching](#q16-18)
- [16.19 — Pond Sizes](#q16-19)
- [16.20 — T9](#q16-20)
- [16.21 — Sum Swap](#q16-21)
- [16.22 — Langton's Ant](#q16-22)
- [16.23 — Rand7 from Rand5](#q16-23)
- [16.24 — Pairs with Sum](#q16-24)
- [16.25 — LRU Cache](#q16-25)
- [16.26 — Calculator](#q16-26)

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → উদাহরণ → Listen → Brute force → Optimize → Code (Dart+Python) → Complexity → Pattern → Common mistake → Follow-up।**

---
---

<a id="background"></a>
# Background — এই chapter-এ যা বারবার লাগবে

এই chapter-এ কোনো একক topic নেই — তাই আগের chapter গুলোর কয়েকটা technique মনে করিয়ে দিই। প্রশ্ন পড়ার সময় "এটা কোন পরিবারের?" — এই চিন্তাটাই আসল কাজ।

## ১. কয়েকটা পুনরাবৃত্ত technique

```
Hash Map / Set      →  "কতবার আছে?", "আগে দেখেছি?", "জোড়া আছে?"
                       (16.2 Word Freq, 16.21 Sum Swap, 16.24 Pairs)
Bit manipulation    →  XOR swap, sign bit, branch ছাড়া (16.1, 16.7, 16.9)
Math / counting     →  factorization, digit গোনা (16.5 Factorial, 16.8 English)
Simulation          →  step-by-step অনুসরণ (16.4 TicTac, 16.19 Pond, 16.22 Ant)
Sorting + two ptr   →  দুটো sorted list একসাথে হাঁটা (16.6 Smallest Diff)
Geometry            →  line, point, square (16.3, 16.13, 16.14)
```

## ২. XOR swap — খুব দরকারি bit trick

দুটো সংখ্যা temp ছাড়া swap করতে XOR ব্যবহার হয়। মূল নিয়ম: `a XOR a = 0`, আর `a XOR 0 = a`।

```
a = 5  (101),  b = 3 (011)
a = a ^ b   →  a = 110
b = a ^ b   →  b = 101  = পুরোনো a
a = a ^ b   →  a = 011  = পুরোনো b
```

> এই trick 16.1-এ লাগবে। মনে রাখবেন — overflow-safe (যোগ-বিয়োগের মতো নয়)।

## ৩. Sign bit ও branch-less programming

কম্পিউটারে একটা signed integer-এর সবচেয়ে উপরের bit (most significant bit) হলো **sign bit** — negative হলে 1, নাহলে 0। এটা দিয়ে `if` ছাড়াই "কোনটা বড়" বলা যায় (16.7)।

## ৪. Counting / prefix idea

কোনো event-এর শুরু-শেষ থাকলে, সব শুরুতে +1 আর সব শেষে -1 করে running sum রাখলে যেকোনো মুহূর্তে কতগুলো active তা বের হয় (16.10 Living People)। এটা খুব common counting trick।

> মূল কথা: এই chapter-এ নতুন কিছু শেখার চেয়ে **চিনে ফেলা** বেশি জরুরি — কোন প্রশ্ন কোন পুরোনো pattern-এর।

---
---

<a id="q16-1"></a>
# 16.1 — Number Swapper

> Pattern: **Bit manipulation (XOR) / Arithmetic** · Difficulty: **Easy** · warm-up, common

> **বইয়ের ভাষায়:** Write a function to swap a number in place (that is, without temporary variables).

## সমস্যাটা সহজ বাংলায়
দুটো সংখ্যা `a` আর `b` আছে। কোনো **temporary variable ব্যবহার না করে** এদের value বদলাবদলি (swap) করতে হবে।

## উদাহরণ
```
a = 9, b = 4
swap এর পর  →  a = 4, b = 9
```

## ধাপ ১: Listen
- **integer-ই, নাকি float-ও?** XOR trick শুধু integer-এ কাজ করে; arithmetic trick float-এও চলে (কিন্তু precision সমস্যা)।
- **একই variable হলে?** (`a` আর `b` একই memory) — XOR করলে 0 হয়ে যাবে, সাবধান।

## ভাবনা ১: Arithmetic (যোগ-বিয়োগ)
পার্থক্যটাকে কাজে লাগাই।
```
a = 9, b = 4
a = a - b   →  a = 5   (পার্থক্য জমা রাখলাম a-তে)
b = a + b   →  b = 9   (পুরোনো a)
a = b - a   →  a = 4   (পুরোনো b)
```
- ঝুঁকি: যোগ করলে **overflow** হতে পারে।

## ভাবনা ২: XOR (সবচেয়ে পছন্দের)
Background-এর XOR নিয়ম দিয়ে। Overflow হয় না কারণ XOR bit-level operation।
```
a = a ^ b
b = a ^ b   (= পুরোনো a)
a = a ^ b   (= পুরোনো b)
```

## Code

```dart
// Dart — XOR swap (record দিয়ে দুটো value ফেরত)
(int, int) swapXor(int a, int b) {
  a = a ^ b;
  b = a ^ b;   // পুরোনো a
  a = a ^ b;   // পুরোনো b
  return (a, b);
}

// Arithmetic version
(int, int) swapArith(int a, int b) {
  a = a - b;
  b = a + b;   // পুরোনো a
  a = b - a;   // পুরোনো b
  return (a, b);
}
```
```python
# Python — XOR swap
def swap_xor(a: int, b: int) -> tuple:
    a = a ^ b
    b = a ^ b   # পুরোনো a
    a = a ^ b   # পুরোনো b
    return a, b

# Arithmetic version
def swap_arith(a: int, b: int) -> tuple:
    a = a - b
    b = a + b   # পুরোনো a
    a = b - a   # পুরোনো b
    return a, b
```
> Python-এ আসলে `a, b = b, a` করলেই হয় (tuple unpacking) — কিন্তু interview-তে চাচ্ছে "trick"-টা দেখাতে।

## Complexity
**Time: O(1)** · **Space: O(1)** (কোনো temp নেই)।

## Pattern চিনুন
> **"temp ছাড়া swap" → XOR trick (`a^=b; b^=a; a^=b`)।** Overflow-safe বলে XOR-ই preferred।

## Common mistake
- একই variable swap করতে গিয়ে (`a` আর `a`) XOR দিয়ে 0 বানিয়ে ফেলা।
- arithmetic version-এ overflow ভুলে যাওয়া।

## Follow-up
- **n-টা variable rotate করো** → একই idea generalize, বা একটা temp/loop।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-2"></a>
# 16.2 — Word Frequencies

> Pattern: **Hash Map (precompute)** · Difficulty: **Easy** · common

> **বইয়ের ভাষায়:** Design a method to find the frequency of occurrences of any given word in a book. What if we were running this algorithm multiple times?

## সমস্যাটা সহজ বাংলায়
একটা বই (অনেকগুলো word) আছে। কোনো একটা word সেখানে **কতবার এসেছে** বের করতে হবে। আর একটা টুইস্ট: যদি **অনেকবার** এই query চালাতে হয়, তাহলে কী করব?

## উদাহরণ
```
book = "the cat sat on the mat the end"
frequency("the")  →  3
frequency("cat")  →  1
frequency("dog")  →  0
```

## ধাপ ১: Listen
- **একবার নাকি বহুবার query?** এটাই আসল প্রশ্ন — উত্তর বদলে দেয়।
- **case-sensitive?** "The" আর "the" এক?
- **punctuation handle?** "end." আর "end" আলাদা?

## ভাবনা ১: একবার query — শুধু গুনে যাও
পুরো book scan করে গুনি।
- **Time: O(n)** প্রতি query। একবারের জন্য ঠিক আছে।

## ভাবনা ২: বহুবার query — Hash Map precompute (BUD)
যদি বারবার জিজ্ঞেস করা হয়, তাহলে প্রতিবার পুরো book পড়া অপচয় (repeated work)। **একবার** পুরো book ঘুরে একটা Hash Map বানাই: `word → count`। তারপর প্রতিটা query **O(1)**।
```
book একবার scan:
   {the:3, cat:1, sat:1, on:1, mat:1, end:1}
query "the" →  map["the"] = 3   (O(1))
```

## Code

```dart
// Dart — precompute করে বারবার query
class WordFrequencies {
  final Map<String, int> _counts = {};
  WordFrequencies(List<String> book) {
    for (final w in book) {
      final word = w.toLowerCase();
      _counts[word] = (_counts[word] ?? 0) + 1;
    }
  }
  int frequency(String word) => _counts[word.toLowerCase()] ?? 0;
}
```
```python
# Python — precompute করে বারবার query
from collections import Counter

class WordFrequencies:
    def __init__(self, book: list):
        self.counts = Counter(w.lower() for w in book)
    def frequency(self, word: str) -> int:
        return self.counts[word.lower()]
```

## Complexity
- একবার query: **O(n)** time, O(1) space।
- বহুবার (precompute): build **O(n)** একবার, তারপর প্রতি query **O(1)**; space **O(distinct words)**।

## Pattern চিনুন
> **"বারবার একই ধরনের query" → একবার precompute করে Hash Map বানাও, তারপর O(1) lookup।** "What if multiple times?" শুনলেই precompute ভাবুন।

## Common mistake
- "multiple times" অংশটা ধরতে না পারা — সেটাই প্রশ্নের আসল মজা।
- case/punctuation normalize না করা।

## Follow-up
- **বই খুব বড় (একটা machine-এ ধরে না)?** → distributed: book কে shard করে প্রতিটায় count, তারপর merge (MapReduce idea, Chapter 9)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-3"></a>
# 16.3 — Intersection

> Pattern: **Geometry (line segment intersection)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any.

## সমস্যাটা সহজ বাংলায়
দুটো **line segment** (প্রতিটা দুটো end-point দিয়ে দেওয়া) আছে। এরা যদি কোথাও **কাটে (intersect)**, সেই point বের করতে হবে; না কাটলে "নেই" বলতে হবে।

## উদাহরণ
```
   \   /
    \ /            segment 1: (0,0)→(4,4)
     X  ← এখানে কাটে   segment 2: (0,4)→(4,0)
    / \             intersection: (2,2)
   /   \
```

## ধাপ ১: Listen
- **segment নাকি infinite line?** segment হলে intersection point দুটোরই range-এর মধ্যে থাকতে হবে।
- **vertical line (x একই)?** slope infinite — আলাদা handle করতে হয়।
- **overlap (একই line-এ বসা)?** তখন intersection একটা পুরো অংশ।

## মূল insight — slope-intercept
প্রতিটা non-vertical line: `y = m·x + b`। দুটো line:
```
y = m1·x + b1
y = m2·x + b2

m1 == m2 হলে: parallel (b সমান হলে overlapping, নাহলে কখনো কাটে না)
নাহলে:  m1·x + b1 = m2·x + b2  →  x = (b2 - b1) / (m1 - m2)
```
x পেলে y বের করি, তারপর check করি point টা **দুই segment-এরই range**-এর মধ্যে কিনা।

## ধাপে ধাপে approach
1. দুটো segment-কে এমনভাবে সাজাই যাতে start ≤ end (x অনুযায়ী)।
2. slope (`m`) আর intercept (`b`) বের করি (vertical হলে আলাদা)।
3. parallel কিনা দেখি; নাহলে x বের করি।
4. intersection point দুই segment-এর bounding box-এর মধ্যে কিনা যাচাই করি।

## Code

```dart
// Dart — সরলীকৃত (vertical/overlap edge case সংক্ষেপে)
class Point { final double x, y; Point(this.x, this.y); }

Point? intersection(Point p1, Point p2, Point p3, Point p4) {
  // segment 1-এর slope ও intercept
  final denom = (p1.x - p2.x) * (p3.y - p4.y) - (p1.y - p2.y) * (p3.x - p4.x);
  if (denom == 0) return null;                 // parallel
  final px = ((p1.x * p2.y - p1.y * p2.x) * (p3.x - p4.x) -
              (p1.x - p2.x) * (p3.x * p4.y - p3.y * p4.x)) / denom;
  final py = ((p1.x * p2.y - p1.y * p2.x) * (p3.y - p4.y) -
              (p1.y - p2.y) * (p3.x * p4.y - p3.y * p4.x)) / denom;
  bool onSeg(Point a, Point b, double x, double y) =>
      x >= (a.x < b.x ? a.x : b.x) - 1e-9 && x <= (a.x > b.x ? a.x : b.x) + 1e-9 &&
      y >= (a.y < b.y ? a.y : b.y) - 1e-9 && y <= (a.y > b.y ? a.y : b.y) + 1e-9;
  if (onSeg(p1, p2, px, py) && onSeg(p3, p4, px, py)) return Point(px, py);
  return null;                                 // intersection segment-এর বাইরে
}
```
```python
# Python — same logic (line intersection formula)
def intersection(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:                  # parallel
        return None
    px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / denom
    def on_seg(ax, ay, bx, by, x, y):
        return (min(ax, bx) - 1e-9 <= x <= max(ax, bx) + 1e-9 and
                min(ay, by) - 1e-9 <= y <= max(ay, by) + 1e-9)
    if on_seg(x1, y1, x2, y2, px, py) and on_seg(x3, y3, x4, y4, px, py):
        return (px, py)
    return None
```

## Complexity
**Time: O(1)** · **Space: O(1)** — শুধু কয়েকটা arithmetic।

## Pattern চিনুন
> **"দুটো line/segment কাটে কিনা" → slope-intercept বা determinant formula, তারপর point টা range-এর মধ্যে কিনা যাচাই।** geometry-তে edge case (vertical, parallel, overlap) সবসময় ভাবুন।

## Common mistake
- vertical line (infinite slope) handle না করা।
- floating-point সমান তুলনায় `==` (epsilon `1e-9` ব্যবহার করুন)।
- segment নয় infinite line হিসেবে ধরা (range check বাদ)।

## Follow-up
- **overlapping segment** হলে intersection একটা range — আলাদা ফেরত দিতে হবে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-4"></a>
# 16.4 — Tic Tac Win

> Pattern: **Simulation / Board check** · Difficulty: **Easy–Medium** · common

> **বইয়ের ভাষায়:** Design an algorithm to figure out if someone has won a game of tic-tac-toe.

## সমস্যাটা সহজ বাংলায়
একটা tic-tac-toe board (3×3, বা N×N) দেওয়া। বলতে হবে কেউ **জিতেছে কিনা** — অর্থাৎ একই player-এর mark পুরো একটা row, column বা diagonal জুড়ে আছে কিনা।

## উদাহরণ
```
X O X
O X O      diagonal X X X (উপর-বাঁ → নিচ-ডান)  →  X জিতেছে
O O X
```

## ধাপ ১: Listen
- **একবার চেক নাকি বহুবার?** বহুবার হলে precompute ভাবা যায়।
- **শুধু শেষ move জানা আছে?** তাহলে শুধু ওই row/col/diagonal চেক করলেই হয় (অনেক দ্রুত)।
- **board কি সবসময় 3×3?** নাকি N×N?

## ভাবনা ১: সব line চেক (সরল)
৩টা row, ৩টা column, ২টা diagonal — মোট ৮টা line চেক করি। প্রতিটায় তিনটা ঘর সমান ও খালি নয় কিনা।

## ভাবনা ২: শেষ move জানা থাকলে
যে ঘরে শেষ mark পড়ল, শুধু সেই row, সেই column, আর (যদি diagonal-এ থাকে) diagonal চেক করি — O(N), পুরো board নয়।

## Code

```dart
// Dart — N×N, সব line চেক
String? hasWon(List<List<String>> b) {       // ' ' = খালি
  final n = b.length;
  bool same(List<String> cells) =>
      cells[0] != ' ' && cells.every((c) => c == cells[0]);
  for (int i = 0; i < n; i++) {
    if (same([for (int j = 0; j < n; j++) b[i][j]])) return b[i][0];  // row
    if (same([for (int j = 0; j < n; j++) b[j][i]])) return b[0][i];  // col
  }
  if (same([for (int i = 0; i < n; i++) b[i][i]])) return b[0][0];          // diag
  if (same([for (int i = 0; i < n; i++) b[i][n - 1 - i]])) return b[0][n-1]; // anti-diag
  return null;
}
```
```python
# Python — N×N, সব line চেক
def has_won(b):                      # ' ' = খালি
    n = len(b)
    def same(cells):
        return cells[0] != ' ' and all(c == cells[0] for c in cells)
    for i in range(n):
        if same([b[i][j] for j in range(n)]): return b[i][0]   # row
        if same([b[j][i] for j in range(n)]): return b[0][i]   # col
    if same([b[i][i] for i in range(n)]): return b[0][0]               # diag
    if same([b[i][n-1-i] for i in range(n)]): return b[0][n-1]         # anti-diag
    return None
```

## Complexity
**Time: O(N²)** (পুরো board দেখা) · **Space: O(1)** (constant extra)। শেষ move জানা থাকলে **O(N)**।

## Pattern চিনুন
> **"board-এ win condition" → সব row/col/diagonal চেক; শেষ move জানা থাকলে শুধু সেই line।** এটা পরিষ্কার case-analysis-এর প্রশ্ন।

## Common mistake
- খালি ঘর (`' '`) কে winner ধরা — `cells[0] != ' '` চেক জরুরি।
- দুটো diagonal-এর একটা ভুলে যাওয়া।

## Follow-up
- **N×N, K-in-a-row** (Gomoku) → sliding window দিয়ে চেক।
- **বহুবার call** → প্রতি move-এ incremental counter রাখা।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-5"></a>
# 16.5 — Factorial Zeros

> Pattern: **Math (factor counting)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Write an algorithm which computes the number of trailing zeros in n factorial.

## সমস্যাটা সহজ বাংলায়
`n!` (= 1×2×3×...×n) এর শেষে **কয়টা শূন্য (trailing zero)** থাকবে — সেটা বের করতে হবে। আসল `n!` হিসাব না করেই।

## উদাহরণ
```
5!  = 120        →  ১টা শূন্য
10! = 3628800    →  ২টা শূন্য
```

## মূল insight — শূন্য আসে কোথা থেকে?
একটা trailing zero তৈরি হয় একটা **10 = 2 × 5** থেকে। অর্থাৎ `n!`-এর গুণফলে যত জোড়া (2,5) আছে, তত শূন্য। 2-এর সংখ্যা সবসময় 5-এর চেয়ে অনেক বেশি, তাই **শুধু 5 কতবার factor হিসেবে আছে সেটাই গুনলে চলে**।
```
trailing zeros = n!-এ 5 কতবার factor হিসেবে আসে
              = n/5 + n/25 + n/125 + ...
(25 = 5×5 দুটো 5 দেয়, তাই /25-ও যোগ হয়; 125 তিনটা, এভাবে)
```

## উদাহরণে যাচাই
```
n = 100:
  100/5   = 20
  100/25  = 4
  100/125 = 0  → থামো
  মোট = 24 টা শূন্য
```

## Code

```dart
// Dart
int trailingZeros(int n) {
  int count = 0;
  for (int p = 5; n ~/ p > 0; p *= 5) {   // 5, 25, 125, ...
    count += n ~/ p;
  }
  return count;
}
```
```python
# Python
def trailing_zeros(n: int) -> int:
    count = 0
    p = 5
    while n // p > 0:        # 5, 25, 125, ...
        count += n // p
        p *= 5
    return count
```

## Complexity
**Time: O(log₅ n)** (5-এর power যতবার n ছাড়ায়) · **Space: O(1)**।

## Pattern চিনুন
> **"factorial-এর trailing zero" → 5-এর factor গোনো (n/5 + n/25 + ...)।** বড় গুণফল সরাসরি হিসাব করার দরকার নেই — factor-এর গঠন ভাবুন।

## Common mistake
- প্রতিটা সংখ্যায় শুধু একবার করে 5 গোনা (25, 125-এর extra 5 মিস)।
- আসল `n!` হিসাব করতে যাওয়া (overflow + ধীর)।

## Follow-up
- **কেন 2 নয়, 5?** → 2-এর factor সবসময় বেশি; bottleneck 5।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-6"></a>
# 16.6 — Smallest Difference

> Pattern: **Sort + Two Pointer** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.

## সমস্যাটা সহজ বাংলায়
দুটো integer array আছে। একটা করে উপাদান দুই array থেকে নিয়ে এমন এক **জোড়া** বের করতে হবে যাদের **পার্থক্য (difference) সবচেয়ে ছোট**। সেই ছোট পার্থক্যটা ফেরত দিতে হবে।

## উদাহরণ
```
A = {1, 3, 15, 11, 2}
B = {23, 127, 235, 19, 8}

সবচেয়ে কাছের জোড়া: (11, 8)  →  পার্থক্য = 3
```

## ভাবনা ১: Brute Force
প্রতিটা জোড়া (a, b) মিলিয়ে দেখি।
- **Time: O(A·B)** · **Space: O(1)**। ধীর।

## ভাবনা ২: Sort + Two Pointer (BUD)
দুটো array **sort** করি। তারপর দুটো pointer দিয়ে একসাথে হাঁটি। যেহেতু sorted, পার্থক্য কমাতে হলে **ছোট value-র pointer এগোতে** হবে।
```
A sorted: 1 2 3 11 15
B sorted: 8 19 23 127 235
          ↑a       ↑b
a=1, b=8 → diff 7;  a ছোট → a এগোও
... এভাবে চলতে চলতে a=11, b=8 → diff 3 (সবচেয়ে ছোট পাওয়া গেল)
```

## Code

```dart
// Dart
int smallestDifference(List<int> a, List<int> b) {
  a.sort();
  b.sort();
  int i = 0, j = 0, best = 1 << 62;
  while (i < a.length && j < b.length) {
    final diff = (a[i] - b[j]).abs();
    if (diff < best) best = diff;
    if (a[i] < b[j]) i++; else j++;   // ছোটটার pointer এগোও
  }
  return best;
}
```
```python
# Python
def smallest_difference(a: list, b: list) -> int:
    a.sort(); b.sort()
    i = j = 0
    best = float('inf')
    while i < len(a) and j < len(b):
        best = min(best, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1          # ছোটটার pointer এগোও
        else:
            j += 1
    return best
```

## Complexity
**Time: O(A log A + B log B)** (sort) · **Space: O(1)** (sort বাদে)।

## Pattern চিনুন
> **"দুই array-র সবচেয়ে কাছের জোড়া" → দুটোই sort করে two pointer।** sorted হলে কোন pointer এগোবে তা ছোট value দেখে ঠিক করুন।

## Common mistake
- pointer এগোনোর নিয়ম উল্টে ফেলা (বড়টা এগোলে কখনো কাছে আসবে না)।
- `abs` না নেওয়া / overflow (initial best খুব বড় নিন)।

## Follow-up
- **জোড়াটাও ফেরত দাও** → best update-এর সময় (a[i], b[j])-ও মনে রাখুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-7"></a>
# 16.7 — Number Max

> Pattern: **Bit manipulation (no comparison)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Write a method that finds the maximum of two numbers. You should not use if-else or any comparison operator.

## সমস্যাটা সহজ বাংলায়
দুটো সংখ্যা `a`, `b`-র মধ্যে **বড়টা** বের করতে হবে — কিন্তু কোনো `if-else` বা তুলনা operator (`<`, `>`) ব্যবহার করা যাবে না।

## উদাহরণ
```
max(5, 7)   →  7
max(9, 3)   →  9
```

## মূল insight — sign bit ব্যবহার
`a - b` করি। এর **sign bit** (সবচেয়ে উপরের bit) বলে দেয় কে বড়:
```
যদি a >= b  →  a - b ≥ 0  →  sign bit = 0
যদি a <  b  →  a - b < 0   →  sign bit = 1

k = (a - b)-এর sign bit  (0 বা 1)
max = a·(1-k) + b·k       (k=0 হলে a, k=1 হলে b)
```
sign bit বের করি: `((a - b) >> 31) & 1` (32-bit হলে; 64-bit হলে 63)।

## সতর্কতা — overflow
`a - b` overflow করতে পারে (a খুব বড় positive, b খুব বড় negative)। নিখুঁত উত্তরে এটা আলাদা handle করতে হয়, তবে মূল idea একই। নিচে সরল version।

## Code

```dart
// Dart — sign bit দিয়ে (comparison ছাড়া)
int getMax(int a, int b) {
  final diff = a - b;
  final k = (diff >> 63) & 1;   // Dart int 64-bit → sign bit
  return a * (1 - k) + b * k;   // k=0 → a, k=1 → b
}
```
```python
# Python — int unbounded, তাই sign বের করি bit দিয়ে
def get_max(a: int, b: int) -> int:
    diff = a - b
    k = (diff >> 63) & 1        # 64-bit ধরে sign bit
    return a * (1 - k) + b * k
```
> Python int unbounded, তাই বাস্তবে `(diff >> 63) & 1` সব ক্ষেত্রে কাজ করবে না; ধারণাটা বোঝার জন্য 64-bit ধরা হয়েছে।

## Complexity
**Time: O(1)** · **Space: O(1)**।

## Pattern চিনুন
> **"comparison/if ছাড়া বড়টা" → পার্থক্যের sign bit বের করে k (0/1) বানাও, তারপর a·(1-k)+b·k।** branch-less programming-এর classic।

## Common mistake
- `>>` arithmetic নাকি logical shift গুলিয়ে ফেলা।
- overflow case উপেক্ষা করা (interview-তে অন্তত উল্লেখ করুন)।

## Follow-up
- **overflow-safe বানাও** → a, b-র sign আলাদা হলে আলাদা যুক্তি (sign of a কে directly ব্যবহার)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-8"></a>
# 16.8 — English Int

> Pattern: **String building + grouping (3 digit)** · Difficulty: **Medium–Hard** · common

> **বইয়ের ভাষায়:** Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

## সমস্যাটা সহজ বাংলায়
একটা integer দেওয়া। সেটাকে **ইংরেজি শব্দে** লিখতে হবে। যেমন `1234` → "One Thousand Two Hundred Thirty Four"।

## উদাহরণ
```
0     →  "Zero"
19    →  "Nineteen"
1234  →  "One Thousand Two Hundred Thirty Four"
```

## মূল insight — তিন digit করে ভাগ
সংখ্যাকে ডান থেকে **তিন digit করে group** করি, প্রতিটা group-এর জন্য "Thousand", "Million", "Billion" suffix বসাই।
```
1,234,567
     └─567─┘  →  "Five Hundred Sixty Seven"
 └─234──┘     →  "Two Hundred Thirty Four Thousand"
└1┘          →  "One Million"
```
প্রতিটা ৩-digit chunk একভাবে শব্দে রূপান্তর করি (hundreds + tens + ones), শুধু suffix বদলায়।

## ধাপে ধাপে approach
1. লুকআপ table: ones (0–19), tens (20,30,...), powers ("Thousand", "Million", ...)।
2. সংখ্যাকে 1000 দিয়ে বারবার ভাগ করে chunk বের করি।
3. প্রতিটা non-zero chunk → শব্দ + ঠিক suffix।

## Code

```dart
// Dart
const _small = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
  'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen',
  'Eighteen','Nineteen'];
const _tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'];
const _bigs = ['','Thousand','Million','Billion'];

String _threeDigits(int n) {
  final parts = <String>[];
  if (n >= 100) { parts.add(_small[n ~/ 100]); parts.add('Hundred'); n %= 100; }
  if (n >= 20) { parts.add(_tens[n ~/ 10]); n %= 10; }
  if (n >= 1) parts.add(_small[n]);
  return parts.join(' ');
}

String englishInt(int num) {
  if (num == 0) return 'Zero';
  final chunks = <String>[];
  int chunkIndex = 0;
  while (num > 0) {
    final chunk = num % 1000;
    if (chunk != 0) {
      var s = _threeDigits(chunk);
      if (_bigs[chunkIndex].isNotEmpty) s += ' ${_bigs[chunkIndex]}';
      chunks.insert(0, s);          // বড় group আগে
    }
    num ~/= 1000;
    chunkIndex++;
  }
  return chunks.join(' ');
}
```
```python
# Python
SMALL = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
         'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen',
         'Seventeen','Eighteen','Nineteen']
TENS = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
BIGS = ['','Thousand','Million','Billion']

def three_digits(n: int) -> str:
    parts = []
    if n >= 100:
        parts += [SMALL[n // 100], 'Hundred']; n %= 100
    if n >= 20:
        parts.append(TENS[n // 10]); n %= 10
    if n >= 1:
        parts.append(SMALL[n])
    return ' '.join(parts)

def english_int(num: int) -> str:
    if num == 0:
        return 'Zero'
    chunks = []
    idx = 0
    while num > 0:
        chunk = num % 1000
        if chunk:
            s = three_digits(chunk)
            if BIGS[idx]:
                s += ' ' + BIGS[idx]
            chunks.insert(0, s)        # বড় group আগে
        num //= 1000
        idx += 1
    return ' '.join(chunks)
```

## Complexity
**Time: O(d)** (d = digit সংখ্যা) · **Space: O(d)**।

## Pattern চিনুন
> **"সংখ্যা → শব্দ" → তিন digit করে group, প্রতিটার জন্য একই helper + power suffix।** lookup table আর chunk-by-chunk processing — পরিষ্কার case handling-এর প্রশ্ন।

## Common mistake
- 11–19 (eleven...nineteen) আলাদাভাবে handle না করা।
- শূন্য chunk (যেমন 1,000,000-এর মাঝের 000) ভুলভাবে print করা।
- negative সংখ্যা / 0 edge case ভুলে যাওয়া।

## Follow-up
- **negative ও decimal** support → sign আলাদা handle, "Point" দিয়ে দশমিক।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-9"></a>
# 16.9 — Operations

> Pattern: **Bit/arithmetic — শুধু + দিয়ে বাকিগুলো** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Write methods to implement the multiply, subtract, and divide operations for integers. The results of all of these are integers. Use only the add operator.

## সমস্যাটা সহজ বাংলায়
শুধু **যোগ (`+`)** ব্যবহার করতে পারব। এটা দিয়ে **বিয়োগ, গুণ, ভাগ** তিনটাই বানাতে হবে।

## মূল insight
```
negate(a)   = -a  →  a কে বারবার (-1 বা +1) যোগ করে 0 থেকে উল্টোমুখে গুনে
subtract    = a + negate(b)
multiply    = b বার a যোগ করা  (b negative হলে negate করে handle)
divide      = a থেকে কতবার b বিয়োগ করা যায়, সেটাই উত্তর (subtract দিয়ে)
```
মূল কথা: প্রতিটা operation আগেরটার উপর দাঁড়ায় — negate → subtract → multiply → divide।

## ধাপে ধাপে
```
negate(7):  0 থেকে শুরু, প্রতিবার -1 যোগ → 7 বার → -7
multiply(3, 4): 0 + 3 + 3 + 3 + 3 = 12  (ছোটটাকে বার হিসেবে নিলে দ্রুত)
divide(13, 4): 13 - 4 - 4 - 4 = 1 (বাকি), ৩ বার → উত্তর 3
```

## Code

```dart
// Dart — শুধু + দিয়ে
int negate(int a) {
  int neg = 0, d = a > 0 ? -1 : 1;
  while (a != 0) { neg += d; a += d; }
  return neg;
}
int subtract(int a, int b) => a + negate(b);
int multiply(int a, int b) {
  if (a < b) return multiply(b, a);           // ছোটটাকে বার হিসেবে
  int sum = 0;
  for (int i = (b < 0 ? negate(b) : b); i > 0; i = subtract(i, 1)) {
    sum += a;
  }
  return b < 0 ? negate(sum) : sum;
}
int divide(int a, int b) {                     // b != 0 ধরা
  if (b == 0) throw ArgumentError('div by zero');
  final absA = a < 0 ? negate(a) : a;
  final absB = b < 0 ? negate(b) : b;
  int product = 0, count = 0;
  while (product + absB <= absA) { product += absB; count += 1; }
  return (a < 0) != (b < 0) ? negate(count) : count;
}
```
```python
# Python — শুধু + দিয়ে
def negate(a: int) -> int:
    neg, d = 0, -1 if a > 0 else 1
    while a != 0:
        neg += d
        a += d
    return neg

def subtract(a: int, b: int) -> int:
    return a + negate(b)

def multiply(a: int, b: int) -> int:
    if a < b:
        return multiply(b, a)          # ছোটটাকে বার হিসেবে
    total = 0
    i = negate(b) if b < 0 else b
    while i > 0:
        total += a
        i = subtract(i, 1)
    return negate(total) if b < 0 else total

def divide(a: int, b: int) -> int:
    if b == 0:
        raise ValueError('div by zero')
    abs_a = negate(a) if a < 0 else a
    abs_b = negate(b) if b < 0 else b
    product, count = 0, 0
    while product + abs_b <= abs_a:
        product += abs_b
        count += 1
    return negate(count) if (a < 0) != (b < 0) else count
```

## Complexity
- negate/multiply/divide প্রতিটা naive ভাবে **O(value)** — বড় সংখ্যায় ধীর।
- (faster negate: doubling দিয়ে O(log) করা যায় — follow-up।)

## Pattern চিনুন
> **"শুধু এক operation দিয়ে বাকিগুলো" → ছোট থেকে বড় build করো (negate → subtract → multiply → divide)।** প্রতিটা আগেরটার উপর দাঁড়ায়।

## Common mistake
- negative সংখ্যা handle না করা (sign আলাদা করে শেষে negate)।
- divide-এ `b == 0` চেক বাদ দেওয়া।

## Follow-up
- **দ্রুত negate** → 1 যোগ করার বদলে delta double করে (1,2,4,...) লাফিয়ে — O(log)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-10"></a>
# 16.10 — Living People

> Pattern: **Counting / Prefix sum on years** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Given a list of people with their birth and death years, implement a method to compute the year with the most number of people alive. You may assume that all people were born between 1900 and 2000 (inclusive).

## সমস্যাটা সহজ বাংলায়
কতগুলো মানুষের জন্ম-সাল ও মৃত্যু-সাল দেওয়া। বের করতে হবে **কোন সালে সবচেয়ে বেশি মানুষ একসাথে বেঁচে ছিল**।

## উদাহরণ
```
person A: 1900–1950
person B: 1920–1990
person C: 1940–1960

1940–1950 সময়ে তিনজনই বেঁচে  →  উত্তর 1940 (বা যেকোনো এক বছর ওই range-এ)
```

## ভাবনা ১: Brute Force
প্রতিটা বছরের জন্য কতজন বেঁচে গুনি।
- **Time: O(people × years)** — ধীর।

## ভাবনা ২: Delta array / counting (BUD)
একটা array `delta[year]` রাখি: জন্মে **+1**, মৃত্যুর **পরের বছর -1**। তারপর running sum নিলে যেকোনো বছরে কতজন বেঁচে তা পাওয়া যায়। সবচেয়ে বড় running sum যেখানে — সেই বছর উত্তর।
```
জন্মে +1, মৃত্যুর পরের বছরে -1
       1900 ... 1920 ... 1940 ...1951 ...1961 ...1991
delta:  +1       +1       +1     -1      -1      -1
running sum বাড়ে-কমে; সর্বোচ্চ যেখানে = উত্তর
```

## Code

```dart
// Dart
int maxAliveYear(List<List<int>> people, {int minYear = 1900, int maxYear = 2000}) {
  final span = maxYear - minYear + 2;
  final delta = List.filled(span, 0);
  for (final p in people) {
    delta[p[0] - minYear] += 1;            // জন্মে +1
    delta[p[1] - minYear + 1] -= 1;        // মৃত্যুর পরের বছর -1
  }
  int running = 0, best = 0, bestYear = minYear;
  for (int i = 0; i < span; i++) {
    running += delta[i];
    if (running > best) { best = running; bestYear = minYear + i; }
  }
  return bestYear;
}
```
```python
# Python
def max_alive_year(people, min_year=1900, max_year=2000):
    span = max_year - min_year + 2
    delta = [0] * span
    for birth, death in people:
        delta[birth - min_year] += 1            # জন্মে +1
        delta[death - min_year + 1] -= 1        # মৃত্যুর পরের বছর -1
    running = best = 0
    best_year = min_year
    for i in range(span):
        running += delta[i]
        if running > best:
            best, best_year = running, min_year + i
    return best_year
```

## Complexity
**Time: O(P + Y)** (P = মানুষ, Y = বছরের range) · **Space: O(Y)**।

## Pattern চিনুন
> **"কোন সময়ে সবচেয়ে বেশি active/overlap" → শুরুতে +1, শেষের পরে -1, তারপর running sum।** এটা interval overlap-এর সবচেয়ে পরিষ্কার trick।

## Common mistake
- মৃত্যুর **সালেই** -1 করা (ব্যক্তি ওই বছরও বেঁচে ছিল — তাই পরের বছর)।
- array size 1 কম নেওয়া (death+1 index out of range)।

## Follow-up
- **range অজানা/বিশাল** → সব birth/death event sort করে sweep line (O(P log P))।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-11"></a>
# 16.11 — Diving Board

> Pattern: **Combinatorics / সব sum বানানো** · Difficulty: **Easy–Medium** · common

> **বইয়ের ভাষায়:** You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, one of length shorter and one of length longer. You must use exactly K planks of wood. Write a method to generate all possible lengths for the diving board.

## সমস্যাটা সহজ বাংলায়
দুই রকম কাঠ আছে — `shorter` লম্বা আর `longer` লম্বা। ঠিক **K টা** কাঠ পরপর জুড়তে হবে। সম্ভাব্য **সব মোট length** বের করতে হবে।

## মূল insight
K টা কাঠের মধ্যে যদি `i` টা long আর `(K-i)` টা short হয়, তাহলে length = `i·longer + (K-i)·shorter`। `i` যাবে 0 থেকে K পর্যন্ত — তাই **মাত্র K+1 টা ভিন্ন length** সম্ভব (shorter ≠ longer হলে)।
```
K = 3:
  0 long, 3 short  →  3·s
  1 long, 2 short  →  l + 2s
  2 long, 1 short  →  2l + s
  3 long, 0 short  →  3·l
মোট 4 টা ভিন্ন length
```

## ভাবনা ১: Recursion (naive)
প্রতিটা plank-এ short/long — `2^K` শাখা। অপ্রয়োজনীয় (অনেক duplicate)।

## ভাবনা ২: সরাসরি গণনা (optimal)
উপরের formula দিয়ে K+1 টা length সরাসরি বানাই।

## Code

```dart
// Dart
Set<int> divingBoard(int shorter, int longer, int k) {
  final lengths = <int>{};
  if (k == 0) return lengths;
  if (shorter == longer) return {shorter * k};   // একই হলে একটাই length
  for (int nLonger = 0; nLonger <= k; nLonger++) {
    lengths.add(nLonger * longer + (k - nLonger) * shorter);
  }
  return lengths;
}
```
```python
# Python
def diving_board(shorter: int, longer: int, k: int) -> set:
    if k == 0:
        return set()
    if shorter == longer:
        return {shorter * k}              # একই হলে একটাই length
    return {n * longer + (k - n) * shorter for n in range(k + 1)}
```

## Complexity
**Time: O(K)** · **Space: O(K)**।

## Pattern চিনুন
> **"দুই ধরনের জিনিস ঠিক K বার, সম্ভাব্য sum" → কয়টা type-A তার উপর loop (0..K), বাকিটা type-B।** combination নয় — শুধু গণনা যথেষ্ট।

## Common mistake
- `2^K` recursion লেখা (বিশাল, অপ্রয়োজনীয়)।
- `shorter == longer` edge case ভুলে duplicate length দেওয়া।
- K = 0 case।

## Follow-up
- **N রকম plank** → এখন combination অনেক বেশি; recursion + memo লাগতে পারে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-12"></a>
# 16.12 — XML Encoding

> Pattern: **Tree traversal + string building** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Since XML is very verbose, you are given a way of encoding it where each tag maps to a pre-defined integer value. The (key, value) pairs are passed, along with element values and attributes, and the encoding is built recursively. End tags become token `0`. Encode the XML into the compact format.

## সমস্যাটা সহজ বাংলায়
XML অনেক verbose (`<family>...</family>` ইত্যাদি)। প্রতিটা tag-নামকে একটা পূর্বনির্ধারিত **integer** দিয়ে বদলাই (mapping দেওয়া আছে)। end tag-এর বদলে token `0` দিই। উদ্দেশ্য — XML কে compact encoding-এ রূপান্তর।
```
encoding format:
  element  →  tag_code  attributes  END  children  END
  attribute → attr_code value
  END = 0
```

## উদাহরণ
```
mapping: family→1, person→2, firstName→3, lastName→4, state→5

<family lastName="McDowell" state="CA">
  <person firstName="Gayle">Some Message</person>
</family>

encode →  1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
          │ └attr───┘ └attr┘ │ │ └attr─┘ │ └─value──┘ │ │
          tag                end tag      end person   end family
```

## মূল insight — recursive traversal
XML একটা **tree**। প্রতিটা element-এ: tag code → তার attribute গুলো → `0` (header শেষ) → value/children → `0` (element শেষ)। DFS করে string বানাই।

## Code

```dart
// Dart — সরল XML node model
class Element {
  String name;
  Map<String, String> attributes;
  List<Element> children;
  String value;
  Element(this.name, {this.attributes = const {}, this.children = const [], this.value = ''});
}

String encode(Element e, Map<String, int> codes, StringBuffer sb) {
  sb.write('${codes[e.name]} ');
  e.attributes.forEach((k, v) => sb.write('${codes[k]} $v '));
  sb.write('0 ');                       // header শেষ
  if (e.value.isNotEmpty) sb.write('$e.value ');
  for (final child in e.children) encode(child, codes, sb);
  sb.write('0 ');                       // element শেষ
  return sb.toString();
}
```
```python
# Python — সরল XML node model
class Element:
    def __init__(self, name, attributes=None, children=None, value=''):
        self.name = name
        self.attributes = attributes or {}
        self.children = children or []
        self.value = value

def encode(e, codes, parts):
    parts.append(str(codes[e.name]))
    for k, v in e.attributes.items():
        parts.append(str(codes[k])); parts.append(v)
    parts.append('0')                    # header শেষ
    if e.value:
        parts.append(e.value)
    for child in e.children:
        encode(child, codes, parts)
    parts.append('0')                    # element শেষ
    return ' '.join(parts)
```

## Complexity
**Time: O(n)** (প্রতিটা node/attribute একবার) · **Space: O(depth)** (recursion) + output।

## Pattern চিনুন
> **"nested structure → flat encoding" → recursive DFS, প্রতিটা node-এ header + children + terminator।** tree serialization-এর সাধারণ রূপ।

## Common mistake
- attribute আর value-এর code আলাদা না রাখা।
- end token `0` ভুল জায়গায় (header শেষ vs element শেষ — দুটো আলাদা 0)।

## Follow-up
- **decode করো** (compact → XML) → token stream পড়ে recursively rebuild।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-13"></a>
# 16.13 — Bisect Squares

> Pattern: **Geometry (center line)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Given two squares on a two-dimensional plane, find a line that would cut these two squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis.

## সমস্যাটা সহজ বাংলায়
দুটো square আছে (পাশ x-axis-এর সমান্তরাল)। এমন একটা **সরলরেখা** বের করতে হবে যা **দুটো square-কেই সমান দুই ভাগ** করে।

## মূল insight
যেকোনো রেখা একটা square-কে সমান দু'ভাগ করে **যদি ও কেবল যদি** সেটা square-এর **কেন্দ্র (center)** দিয়ে যায়। তাই দুই square-এর **দুই কেন্দ্র সংযোগকারী রেখাই** উত্তর।
```
   ┌─────┐
   │  ·  │        দুই center: (·) আর (×)
   └─────┘            সেই দুই center-এর মধ্যে দিয়ে যাওয়া রেখাই
          ┌────┐      দুটোকেই সমান ভাগ করে
          │  × │
          └────┘
```

## ধাপে ধাপে
1. প্রতিটা square-এর center = `(x + size/2, y + size/2)`।
2. দুই center দিয়ে যাওয়া রেখার সমীকরণ বের করি (slope + একটা point)।
3. দুই center একই হলে (concentric) — অসংখ্য রেখা; যেকোনো একটা দাও।

## Code

```dart
// Dart
class Square { double left, top, size; Square(this.left, this.top, this.size);
  double get midX => left + size / 2;
  double get midY => top + size / 2;
}

// রেখাকে (slope, yIntercept) হিসেবে ফেরত; vertical হলে null slope
({double? slope, double intercept}) cutLine(Square a, Square b) {
  final x1 = a.midX, y1 = a.midY, x2 = b.midX, y2 = b.midY;
  if (x1 == x2) return (slope: null, intercept: x1);     // vertical line x = x1
  final slope = (y2 - y1) / (x2 - x1);
  final intercept = y1 - slope * x1;
  return (slope: slope, intercept: intercept);
}
```
```python
# Python
class Square:
    def __init__(self, left, top, size):
        self.left, self.top, self.size = left, top, size
    @property
    def mid(self):
        return (self.left + self.size / 2, self.top + self.size / 2)

def cut_line(a: Square, b: Square):
    (x1, y1), (x2, y2) = a.mid, b.mid
    if x1 == x2:
        return ('vertical', x1)          # x = x1
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return (slope, intercept)
```

## Complexity
**Time: O(1)** · **Space: O(1)**।

## Pattern চিনুন
> **"shape কে সমান দুই ভাগ করা রেখা" → symmetric shape-এর center দিয়ে যেতে হবে; দুই center জোড়া দিলেই উত্তর।** geometry-তে symmetry খুঁজুন।

## Common mistake
- "সমান ভাগ" মানে শুধু center দিয়ে যাওয়া — এটা না বোঝা।
- vertical line (x1 == x2) handle না করা।
- দুই center একই (concentric) edge case।

## Follow-up
- **রেখাটাকে square-এর প্রান্ত পর্যন্ত segment হিসেবে দাও** → center line কে square boundary-তে clip করুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-14"></a>
# 16.14 — Best Line

> Pattern: **Geometry + Hash Map (slope counting)** · Difficulty: **Medium–Hard** · common

> **বইয়ের ভাষায়:** Given a two-dimensional graph with points on it, find a line which passes the most number of points.

## সমস্যাটা সহজ বাংলায়
একগুচ্ছ point (x, y) দেওয়া। এমন একটা সরলরেখা বের করতে হবে যার উপর **সবচেয়ে বেশি point** পড়ে।

## উদাহরণ
```
     ·          point: (0,0),(1,1),(2,2),(3,0),(0,3)
   ·            slope 1-এর line (y = x) তে (0,0),(1,1),(2,2) — ৩টা point
 ·              উত্তর: সেই line
```

## মূল insight — slope গোনা
দুটো point একটা line ঠিক করে। একটা point ধরে বাকি সবার সাথে **slope** বের করি; একই slope-এর point গুলো একই line-এ (যেহেতু সবাই এই একই point দিয়ে যাচ্ছে)। একটা Hash Map-এ `slope → count` রাখি।
```
point P থেকে সব point-এ slope বের করো:
   একই slope = একই line (P দিয়ে যাওয়া)
সব P-র জন্য সর্বোচ্চ count = উত্তর
```

## ভাবনা ১: Brute Force (সব জোড়া line)
প্রতি জোড়া line ধরে বাকি সবাই ওই line-এ কিনা — **O(n³)**।

## ভাবনা ২: প্রতি point থেকে slope map (BUD)
প্রতিটা point থেকে বাকিদের slope গুনি — **O(n²)**। floating slope-এ precision সমস্যা; তাই slope কে কিছুটা round করি বা reduced fraction (dy/dx) হিসেবে রাখি।

## Code

```dart
// Dart — slope গোনা (floating, round করে bucket)
double _slope(List<double> a, List<double> b) {
  if (a[0] == b[0]) return double.infinity;     // vertical
  return ((b[1] - a[1]) / (b[0] - a[0]) * 1000).roundToDouble() / 1000;
}

int bestLine(List<List<double>> pts) {
  int best = 0;
  for (int i = 0; i < pts.length; i++) {
    final counts = <double, int>{};
    for (int j = 0; j < pts.length; j++) {
      if (i == j) continue;
      final s = _slope(pts[i], pts[j]);
      counts[s] = (counts[s] ?? 0) + 1;
      if (counts[s]! + 1 > best) best = counts[s]! + 1;  // +1 = point i নিজে
    }
  }
  return best;
}
```
```python
# Python — slope গোনা
from collections import defaultdict

def slope(a, b):
    if a[0] == b[0]:
        return float('inf')                  # vertical
    return round((b[1] - a[1]) / (b[0] - a[0]), 4)

def best_line(pts):
    best = 0
    for i in range(len(pts)):
        counts = defaultdict(int)
        for j in range(len(pts)):
            if i == j:
                continue
            s = slope(pts[i], pts[j])
            counts[s] += 1
            best = max(best, counts[s] + 1)   # +1 = point i নিজে
    return best
```

## Complexity
**Time: O(n²)** · **Space: O(n)** (প্রতি outer loop-এ slope map)।

## Pattern চিনুন
> **"সবচেয়ে বেশি point যে line-এ" → প্রতি point থেকে slope বের করে Hash Map-এ গোনো (O(n²))।** "একই slope = একই line (এই point দিয়ে)" — মূল চাবি।

## Common mistake
- floating slope সরাসরি key বানানো (precision bug — round/fraction ব্যবহার করুন)।
- vertical line (dx=0) handle না করা।

## Follow-up
- **নিখুঁত precision** → slope কে reduced fraction `(dy/g, dx/g)` হিসেবে রাখুন (g = gcd)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-15"></a>
# 16.15 — Master Mind

> Pattern: **Frequency count (two pass)** · Difficulty: **Easy–Medium** · common

> **বইয়ের ভাষায়:** The Game of Master Mind: compute the number of hits (right color, right position) and pseudo-hits (right color, wrong position) given a solution and a guess. Colors are R, G, B, Y.

## সমস্যাটা সহজ বাংলায়
গোপন ৪-অক্ষরের solution (যেমন `RGGB`) আর একটা guess দেওয়া। গুনতে হবে:
- **hit** = ঠিক রং, ঠিক জায়গা।
- **pseudo-hit** = রং solution-এ আছে কিন্তু জায়গা ভুল (hit হিসেবে গোনা যাবে না)।

## উদাহরণ
```
solution = R G G B
guess    = Y R G B
position:  0 1 2 3
  pos 2 (G==G), pos 3 (B==B)  →  hit = 2
  guess-এর R (pos1) solution-এ আছে কিন্তু অন্য জায়গায়  →  pseudo-hit = 1
```

## মূল insight — দুই pass
1. **Pass 1:** position মিলে গেলে hit++। আর যে রংগুলো hit হয়নি, solution-এর সেই রং frequency map-এ গুনে রাখি।
2. **Pass 2:** guess-এর non-hit অক্ষরগুলো ওই map-এ থাকলে pseudo-hit++ (এবং count কমাই — যাতে double-count না হয়)।

## Code

```dart
// Dart
({int hits, int pseudo}) masterMind(String solution, String guess) {
  int hits = 0;
  final freq = <String, int>{};
  for (int i = 0; i < solution.length; i++) {
    if (solution[i] == guess[i]) {
      hits++;
    } else {
      freq[solution[i]] = (freq[solution[i]] ?? 0) + 1;   // non-hit রং গুনি
    }
  }
  int pseudo = 0;
  for (int i = 0; i < guess.length; i++) {
    if (solution[i] != guess[i]) {
      final c = freq[guess[i]] ?? 0;
      if (c > 0) { pseudo++; freq[guess[i]] = c - 1; }     // ব্যবহার করে কমাও
    }
  }
  return (hits: hits, pseudo: pseudo);
}
```
```python
# Python
from collections import defaultdict

def master_mind(solution: str, guess: str):
    hits = 0
    freq = defaultdict(int)
    for s, g in zip(solution, guess):
        if s == g:
            hits += 1
        else:
            freq[s] += 1                      # non-hit রং গুনি
    pseudo = 0
    for s, g in zip(solution, guess):
        if s != g and freq[g] > 0:
            pseudo += 1
            freq[g] -= 1                      # ব্যবহার করে কমাও
    return hits, pseudo
```

## Complexity
**Time: O(n)** · **Space: O(1)** (মাত্র ৪ রং)।

## Pattern চিনুন
> **"hit + পজিশন-বিহীন match" → আগে hit গোনো, বাকিদের রং frequency map-এ; পরে pseudo গোনো ও count কমাও।** double-count এড়াতে count কমানোই আসল।

## Common mistake
- hit হওয়া অক্ষরকেও pseudo-তে গোনা।
- frequency count না কমানো → একই রং বারবার গোনা।

## Follow-up
- **রং repeat হতে পারে** → এই দুই-pass count পদ্ধতি এমনিতেই সঠিক (frequency রাখছি বলে)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-16"></a>
# 16.16 — Sub Sort

> Pattern: **Array scan (boundary খোঁজা)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted. Minimize n - m (that is, find the smallest such sequence).

## সমস্যাটা সহজ বাংলায়
একটা array দেওয়া। এমন **সবচেয়ে ছোট মাঝের অংশ** `[m, n]` খুঁজতে হবে — যেটাকে sort করলে **পুরো array sorted** হয়ে যায়।

## উদাহরণ
```
[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
          m=3              n=9
sort করলে [3..9] → পুরোটা sorted।  উত্তর (3, 9)
```

## মূল insight
- বাঁ দিক থেকে যতক্ষণ increasing — ঠিক আছে; প্রথম যেখানে আগেরটার চেয়ে ছোট, সেখান থেকে সমস্যা শুরু।
- ডান দিক থেকে যতক্ষণ decreasing (পিছন থেকে) — ঠিক; প্রথম যেখানে পরেরটার চেয়ে বড়, সেখান থেকে সমস্যা।
- কিন্তু আসল boundary আরও বাড়তে পারে: মাঝের অংশের **min** আর **max** নিয়ে বাঁ/ডান প্রসারিত করতে হয়।

## ধাপে ধাপে
1. বাঁ থেকে left-sorted শেষ index, ডান থেকে right-sorted শুরু index বের করি।
2. মাঝের অংশের min ও max বের করি।
3. বাঁ দিকে min-এর চেয়ে বড় যত element আছে — m পিছিয়ে দাও; ডানে max-এর চেয়ে ছোট যত আছে — n এগিয়ে দাও।

## Code

```dart
// Dart
(int, int) subSort(List<int> a) {
  final n = a.length;
  int left = 0;
  while (left < n - 1 && a[left] <= a[left + 1]) left++;
  if (left == n - 1) return (-1, -1);              // already sorted
  int right = n - 1;
  while (right > 0 && a[right] >= a[right - 1]) right--;
  // মাঝের min ও max
  int minV = a[left], maxV = a[left];
  for (int i = left; i <= right; i++) {
    if (a[i] < minV) minV = a[i];
    if (a[i] > maxV) maxV = a[i];
  }
  while (left > 0 && a[left - 1] > minV) left--;        // বাঁ প্রসারণ
  while (right < n - 1 && a[right + 1] < maxV) right++;  // ডান প্রসারণ
  return (left, right);
}
```
```python
# Python
def sub_sort(a: list):
    n = len(a)
    left = 0
    while left < n - 1 and a[left] <= a[left + 1]:
        left += 1
    if left == n - 1:
        return (-1, -1)                       # already sorted
    right = n - 1
    while right > 0 and a[right] >= a[right - 1]:
        right -= 1
    min_v = min(a[left:right + 1])
    max_v = max(a[left:right + 1])
    while left > 0 and a[left - 1] > min_v:        # বাঁ প্রসারণ
        left -= 1
    while right < n - 1 and a[right + 1] < max_v:  # ডান প্রসারণ
        right += 1
    return (left, right)
```

## Complexity
**Time: O(n)** · **Space: O(1)**।

## Pattern চিনুন
> **"সবচেয়ে ছোট অংশ sort করলে পুরোটা sorted" → বাঁ/ডান sorted অংশ খুঁজে, মাঝের min/max দিয়ে boundary প্রসারিত করো।** array boundary-detection-এর সুন্দর উদাহরণ।

## Common mistake
- শুধু প্রথম out-of-order জোড়া নেওয়া — min/max দিয়ে প্রসারণ মিস করা।
- already-sorted case।

## Follow-up
- **প্রমাণ করো এটাই minimum** → বাঁ অংশের সব element মাঝের min-এর ছোট, ডানের সব max-এর বড় — তাই boundary আর ছোট করা যায় না।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-17"></a>
# 16.17 — Contiguous Sequence

> Pattern: **Kadane's algorithm (DP)** · Difficulty: **Medium** · খুব common

> **বইয়ের ভাষায়:** You are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum. Return the sum.

## সমস্যাটা সহজ বাংলায়
একটা array-তে positive-negative দুরকম সংখ্যা আছে। এমন একটানা (contiguous) subarray খুঁজতে হবে যার **যোগফল সবচেয়ে বড়**। সেই sum ফেরত দিতে হবে।

## উদাহরণ
```
[2, -8, 3, -2, 4, -10]
       └3 -2 4┘ = 5  →  সবচেয়ে বড় sum = 5
```

## মূল insight — Kadane
প্রতিটা element-এ একটা সিদ্ধান্ত: আগের running sum-এর সাথে যোগ করব, নাকি এখান থেকে **নতুন করে শুরু** করব? আগের sum যদি **negative** হয়, তাকে টেনে নেওয়া অর্থহীন — তাই ফেলে নতুন শুরু।
```
running = 0
প্রতিটা x-এ:  running += x
             running > best হলে best = running
             running < 0 হলে running = 0   (নতুন শুরু)
```

## Code

```dart
// Dart — Kadane
int maxSubArray(List<int> a) {
  int best = a[0], running = 0;
  for (final x in a) {
    running += x;
    if (running > best) best = running;
    if (running < 0) running = 0;        // negative হলে ফেলে দাও
  }
  return best;
}
```
```python
# Python — Kadane
def max_sub_array(a: list) -> int:
    best = a[0]
    running = 0
    for x in a:
        running += x
        best = max(best, running)
        if running < 0:
            running = 0                   # negative হলে ফেলে দাও
    return best
```
> সব element negative হলে: এই version `best = a[0]` দিয়ে শুরু করায় সবচেয়ে বড় (কম negative) element ফেরত দেয় — সঠিক।

## Complexity
**Time: O(n)** · **Space: O(1)**।

## Pattern চিনুন
> **"সবচেয়ে বড় sum-এর contiguous subarray" → Kadane: running sum, negative হলে reset।** subarray-sum সমস্যার সবচেয়ে গুরুত্বপূর্ণ pattern।

## Common mistake
- সব negative হলে 0 ফেরত দেওয়া (best কে a[0] দিয়ে init করুন, 0 দিয়ে নয়)।
- subarray-এর index দরকার হলে reset-এর সময় start mark করতে ভুলে যাওয়া।

## Follow-up
- **subarray-টাও ফেরত দাও** → running reset হলে নতুন start; best update হলে (start, i) রাখুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-18"></a>
# 16.18 — Pattern Matching

> Pattern: **Brute force over a-length + verify** · Difficulty: **Medium–Hard** · common

> **বইয়ের ভাষায়:** You are given two strings, pattern and value. The pattern string consists of just the letters a and b, describing a pattern within a string. Determine if value matches pattern.

## সমস্যাটা সহজ বাংলায়
দুটো string: `pattern` (শুধু `a` আর `b`) আর `value`। `a` আর `b` দুটো আলাদা substring-এর প্রতিনিধি। `value` কি `pattern` মেনে চলে — সেটা বলতে হবে।
```
pattern "aabab", value "catcatgocatgo"  →  a="cat", b="go" → মেলে → true
```

## উদাহরণ
```
pattern = "aaaa", value = "dogdogdogdog"  →  a="dog"  →  true
pattern = "abab", value = "GraphMoreGraphMore" → a="Graph", b="More" → true
pattern = "aabb", value = "xyzabcxzyabc"  →  মেলানো যায় না → false
```

## মূল insight
ধরি pattern-এ `a` আছে `countA` বার, `b` আছে `countB` বার। `a`-র দৈর্ঘ্য `lenA` ধরলে, `b`-র দৈর্ঘ্য নির্ধারিত:
```
countA·lenA + countB·lenB = value.length
```
তাই **lenA-র সব সম্ভাব্য মান** (0 থেকে যতটুকু) চেষ্টা করি; প্রতিটার জন্য lenB হিসাব করে value-কে টুকরো করে যাচাই করি `a` ও `b` consistent কিনা।

## Code

```dart
// Dart
bool patternMatches(String pattern, String value) {
  if (pattern.isEmpty) return value.isEmpty;
  final main = pattern[0];                       // pattern-কে normalize
  final countMain = pattern.split('').where((c) => c == main).length;
  final countOther = pattern.length - countMain;

  for (int lenMain = 0; lenMain * countMain <= value.length; lenMain++) {
    final rem = value.length - lenMain * countMain;
    if (countOther == 0 && rem != 0) continue;
    if (countOther != 0 && rem % countOther != 0) continue;
    final lenOther = countOther == 0 ? 0 : rem ~/ countOther;
    if (_build(pattern, main, lenMain, lenOther, value)) return true;
  }
  return false;
}

bool _build(String pattern, String main, int lenMain, int lenOther, String value) {
  String? mainStr, otherStr;
  int pos = 0;
  for (final c in pattern.split('')) {
    final len = (c == main) ? lenMain : lenOther;
    if (pos + len > value.length) return false;
    final sub = value.substring(pos, pos + len);
    if (c == main) {
      mainStr ??= sub;
      if (mainStr != sub) return false;
    } else {
      otherStr ??= sub;
      if (otherStr != sub) return false;
    }
    pos += len;
  }
  return pos == value.length && mainStr != otherStr;  // a ≠ b হওয়া উচিত
}
```
```python
# Python
def pattern_matches(pattern: str, value: str) -> bool:
    if not pattern:
        return value == ''
    main = pattern[0]
    count_main = pattern.count(main)
    count_other = len(pattern) - count_main

    for len_main in range(len(value) // count_main + 1):
        rem = len(value) - len_main * count_main
        if count_other == 0:
            if rem != 0:
                continue
            len_other = 0
        else:
            if rem % count_other != 0:
                continue
            len_other = rem // count_other
        if _build(pattern, main, len_main, len_other, value):
            return True
    return False

def _build(pattern, main, len_main, len_other, value):
    main_str = other_str = None
    pos = 0
    for c in pattern:
        length = len_main if c == main else len_other
        sub = value[pos:pos + length]
        if len(sub) != length:
            return False
        if c == main:
            if main_str is None: main_str = sub
            elif main_str != sub: return False
        else:
            if other_str is None: other_str = sub
            elif other_str != sub: return False
        pos += length
    return pos == len(value) and main_str != other_str
```

## Complexity
**Time: O(n²)** (lenMain-এর O(n) মান × প্রতিটায় O(n) verify) · **Space: O(n)**।

## Pattern চিনুন
> **"a/b pattern string-এ মেলে কিনা" → এক variable-এর length (lenA) brute force, অন্যটা সমীকরণ থেকে; তারপর consistency verify।** "unknown length → loop over সম্ভাব্য length" একটা দরকারি কৌশল।

## Common mistake
- `a == b` হলে false দেওয়া উচিত কিনা — বইয়ের ধারণায় a ও b আলাদা substring; consistency-তে চেক রাখা ভালো।
- countOther == 0 (শুধু a) edge case।
- খালি pattern/value।

## Follow-up
- **a বা b খালি string হতে পারে কিনা** clarify করুন — উত্তর বদলায়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-19"></a>
# 16.19 — Pond Sizes

> Pattern: **Flood fill (DFS/BFS on grid)** · Difficulty: **Medium** · খুব common

> **বইয়ের ভাষায়:** You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. The size of a pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.

## সমস্যাটা সহজ বাংলায়
একটা matrix-এ `0` মানে জল। পাশাপাশি (উপর-নিচ-পাশ-**কোণাকুণিসহ ৮ দিক**) যুক্ত জলের ঘরগুলো মিলে একটা **pond**। প্রতিটা pond-এ কয়টা ঘর — সব pond-এর size বের করতে হবে।

## উদাহরণ
```
0 2 1 0
0 1 0 1
1 1 0 1      ponds: {(0,0),(1,0)} = 2;  মাঝের জল connected = 4; ডানে = 1
0 1 0 1      উত্তর: [2, 4, 1]
```

## মূল insight — flood fill
প্রতিটা ঘর scan করি; জল (0) ও আগে দেখা হয়নি — এমন ঘর পেলে সেখান থেকে **DFS/BFS** করে পুরো connected জল গুনি (৮ দিকেই)। দেখা ঘর mark করি (যাতে আবার না গুনি)।

## Code

```dart
// Dart — DFS flood fill
List<int> pondSizes(List<List<int>> land) {
  final m = land.length, n = land[0].length;
  final visited = List.generate(m, (_) => List.filled(n, false));
  final sizes = <int>[];

  int dfs(int r, int c) {
    if (r < 0 || c < 0 || r >= m || c >= n) return 0;
    if (visited[r][c] || land[r][c] != 0) return 0;
    visited[r][c] = true;
    int size = 1;
    for (int dr = -1; dr <= 1; dr++) {
      for (int dc = -1; dc <= 1; dc++) {
        if (dr != 0 || dc != 0) size += dfs(r + dr, c + dc);   // ৮ দিক
      }
    }
    return size;
  }

  for (int r = 0; r < m; r++) {
    for (int c = 0; c < n; c++) {
      if (land[r][c] == 0 && !visited[r][c]) sizes.add(dfs(r, c));
    }
  }
  return sizes;
}
```
```python
# Python — DFS flood fill
def pond_sizes(land):
    m, n = len(land), len(land[0])
    visited = [[False] * n for _ in range(m)]
    sizes = []

    def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        if visited[r][c] or land[r][c] != 0:
            return 0
        visited[r][c] = True
        size = 1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr or dc:
                    size += dfs(r + dr, c + dc)      # ৮ দিক
        return size

    for r in range(m):
        for c in range(n):
            if land[r][c] == 0 and not visited[r][c]:
                sizes.append(dfs(r, c))
    return sizes
```

## Complexity
**Time: O(M·N)** (প্রতিটা ঘর একবার) · **Space: O(M·N)** (visited + recursion stack)।

## Pattern চিনুন
> **"grid-এ connected region-এর আকার/সংখ্যা" → flood fill (DFS/BFS), visited mark করো।** "island count", "connected component" — সব একই পরিবার। এখানে ৮ দিক (diagonal সহ)।

## Common mistake
- শুধু ৪ দিক করা (diagonal বাদ) — এই প্রশ্নে ৮ দিক।
- visited mark না করা → infinite loop / double count।

## Follow-up
- **বিশাল matrix (stack overflow)** → DFS-এর বদলে explicit stack/queue (BFS) ব্যবহার করুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-20"></a>
# 16.20 — T9

> Pattern: **Hash Map (precompute) / Trie** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** On old cell phones, users typed on a numeric keypad and the phone would provide a list of words that matched these numbers. Each digit mapped to a set of 0–4 letters. Given a sequence of digits, implement an algorithm to return a list of matching words from a valid dictionary.

## সমস্যাটা সহজ বাংলায়
পুরোনো ফোনের keypad: `2=abc, 3=def, ...`। একটা digit sequence (যেমন `8733`) দেওয়া হলে, dictionary থেকে সেই digit গুলোর সাথে মেলে এমন **সব শব্দ** ফেরত দিতে হবে।
```
8733  →  "tree", "used" (8=tuv,7=pqrs,3=def,3=def)
```

## ভাবনা ১: Brute Force (সব combination বানাও)
প্রতিটা digit-এর অক্ষর দিয়ে সব combination বানিয়ে dictionary-তে আছে কিনা দেখি — `4^n` শব্দ। ধীর।

## ভাবনা ২: Precompute map (BUD)
dictionary-র প্রতিটা শব্দকে আগেই তার **digit sequence**-এ রূপান্তর করে একটা Hash Map বানাই: `digits → [words]`। তারপর প্রতিটা query **O(1)** lookup।
```
"tree" → t=8,r=7,e=3,e=3 → "8733"
map["8733"] = ["tree", "used", ...]
query "8733" → সরাসরি list
```

## Code

```dart
// Dart — precompute digit → words
class T9 {
  final Map<String, List<String>> _map = {};
  static const _letterToDigit = {
    'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4',
    'j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7',
    's':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'};

  T9(List<String> dictionary) {
    for (final word in dictionary) {
      final digits = word.split('').map((c) => _letterToDigit[c] ?? '').join();
      _map.putIfAbsent(digits, () => []).add(word);
    }
  }
  List<String> getWords(String digits) => _map[digits] ?? [];
}
```
```python
# Python — precompute digit → words
from collections import defaultdict

LETTER_TO_DIGIT = {c: d for d, letters in
    {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}.items()
    for c in letters}

class T9:
    def __init__(self, dictionary):
        self.map = defaultdict(list)
        for word in dictionary:
            digits = ''.join(LETTER_TO_DIGIT.get(c, '') for c in word)
            self.map[digits].append(word)
    def get_words(self, digits: str) -> list:
        return self.map.get(digits, [])
```

## Complexity
- build: **O(total letters in dictionary)** একবার।
- প্রতি query: **O(1)** (+ output size)। Space **O(dictionary)**।

## Pattern চিনুন
> **"keypad/encoding → matching words, বারবার query" → প্রতিটা শব্দকে তার key-তে map করে precompute Hash Map।** 16.2 Word Frequencies-এর মতোই "precompute then O(1)"।

## Common mistake
- প্রতি query-তে সব combination generate করা (precompute না করা)।
- letter→digit mapping ভুল করা।

## Follow-up
- **prefix/incomplete digits** → Trie ব্যবহার করুন (যত digit type হচ্ছে তত prefix match)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-21"></a>
# 16.21 — Sum Swap

> Pattern: **Hash Set + math (target diff)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** Given two arrays of integers, find a pair of values (one from each array) that you can swap to give the two arrays the same sum.

## সমস্যাটা সহজ বাংলায়
দুটো integer array আছে। একটা করে value দুই array থেকে নিয়ে **swap** করতে হবে, যাতে swap-এর পর দুই array-র **যোগফল সমান** হয়ে যায়। এমন এক জোড়া বের করতে হবে।

## উদাহরণ
```
A = {4, 1, 2, 1, 1, 2}  sumA = 11
B = {3, 6, 3, 3}         sumB = 15

A থেকে 1, B থেকে 3 swap করলে:
   sumA = 11 - 1 + 3 = 13,  sumB = 15 - 3 + 1 = 13  →  সমান!  জোড়া (1, 3)
```

## মূল insight — কোন জোড়া?
swap-এর পর sum সমান হতে হলে: `a` সরিয়ে `b` আনলে A বাড়ে `(b - a)`, B কমে `(b - a)`। দুই sum সমান করতে দরকার:
```
sumA - a + b = sumB - b + a
→  b - a = (sumB - sumA) / 2
ধরি  target = (sumB - sumA) / 2
তাহলে প্রতিটা a-র জন্য খুঁজি  b = a + target
```
যদি `(sumB - sumA)` বিজোড় হয় — কখনো সম্ভব নয়।

## ধাপে ধাপে
1. দুই sum বের করি; `diff = sumB - sumA`। বিজোড় হলে `null`।
2. `target = diff / 2`। B-র সব value একটা Set-এ রাখি।
3. A-র প্রতিটা `a`-র জন্য `a + target` Set-এ আছে কিনা দেখি — থাকলে জোড়া।

## Code

```dart
// Dart
(int, int)? sumSwap(List<int> a, List<int> b) {
  final sumA = a.fold(0, (s, x) => s + x);
  final sumB = b.fold(0, (s, x) => s + x);
  final diff = sumB - sumA;
  if (diff % 2 != 0) return null;          // বিজোড় → অসম্ভব
  final target = diff ~/ 2;                 // b - a
  final setB = b.toSet();
  for (final x in a) {
    if (setB.contains(x + target)) return (x, x + target);
  }
  return null;
}
```
```python
# Python
def sum_swap(a: list, b: list):
    diff = sum(b) - sum(a)
    if diff % 2 != 0:
        return None                  # বিজোড় → অসম্ভব
    target = diff // 2               # b - a
    set_b = set(b)
    for x in a:
        if x + target in set_b:
            return (x, x + target)
    return None
```

## Complexity
**Time: O(A + B)** · **Space: O(B)** (Set)।

## Pattern চিনুন
> **"swap করে sum সমান" → math দিয়ে কাঙ্ক্ষিত পার্থক্য (target = diff/2) বের করো, তারপর Hash Set-এ খোঁজো।** "এক জোড়া খুঁজি যার নির্দিষ্ট সম্পর্ক" → Hash Set।

## Common mistake
- diff বিজোড় হলে অসম্ভব — এই check বাদ দেওয়া।
- target-এর সমীকরণ ভুল করা (b - a, না a - b)।

## Follow-up
- **multiple swap allowed?** → অনেক বড় সমস্যা; এটা single-swap-এর সরল রূপ।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-22"></a>
# 16.22 — Langton's Ant

> Pattern: **Simulation (sparse grid)** · Difficulty: **Medium** · common

> **বইয়ের ভাষায়:** An ant is sitting on an infinite grid of white and black squares. At a white square, flip the color, turn 90° right, and move forward one unit. At a black square, flip the color, turn 90° left, and move forward. Write a program to simulate the first K moves and print the board.

## সমস্যাটা সহজ বাংলায়
অসীম grid-এ একটা ant। সাদা ঘরে: রং উল্টে কালো, **ডানে** ঘুরে এক ঘর এগোয়। কালো ঘরে: রং উল্টে সাদা, **বাঁয়ে** ঘুরে এক ঘর এগোয়। K টা move simulate করে board আঁকতে হবে।

## মূল insight — sparse representation
Grid অসীম, তাই পুরো array রাখা যাবে না। শুধু **কালো ঘরগুলোর coordinate** একটা Set-এ রাখি (বাকি সব সাদা ধরে নিই)। ant-এর position আর direction track করি।
```
direction: 0=up, 1=right, 2=down, 3=left
সাদা ঘরে: dir = (dir + 1) % 4  (ডান)
কালো ঘরে: dir = (dir + 3) % 4  (বাঁ)
```

## Code

```dart
// Dart
Set<String> langtonsAnt(int k) {
  final black = <String>{};                 // "r,c" key
  int r = 0, c = 0, dir = 0;                 // 0=up,1=right,2=down,3=left
  const dr = [-1, 0, 1, 0], dc = [0, 1, 0, -1];
  for (int step = 0; step < k; step++) {
    final key = '$r,$c';
    if (black.contains(key)) { black.remove(key); dir = (dir + 3) % 4; } // কালো → বাঁ
    else { black.add(key); dir = (dir + 1) % 4; }                        // সাদা → ডান
    r += dr[dir]; c += dc[dir];
  }
  return black;                              // কালো ঘরগুলো
}
```
```python
# Python
def langtons_ant(k: int):
    black = set()                          # (r, c)
    r = c = 0
    dir = 0                                # 0=up,1=right,2=down,3=left
    dr = [-1, 0, 1, 0]; dc = [0, 1, 0, -1]
    for _ in range(k):
        if (r, c) in black:
            black.discard((r, c)); dir = (dir + 3) % 4    # কালো → বাঁ
        else:
            black.add((r, c)); dir = (dir + 1) % 4        # সাদা → ডান
        r += dr[dir]; c += dc[dir]
    return black                           # কালো ঘরগুলোর set
```
> Board print করতে হলে কালো ঘরগুলোর min/max row,col বের করে সেই bounding box আঁকুন।

## Complexity
**Time: O(K)** · **Space: O(কালো ঘর সংখ্যা)** ≤ O(K)।

## Pattern চিনুন
> **"অসীম grid-এ step-by-step rule" → simulation; পুরো grid নয়, শুধু বিশেষ ঘর (কালো) Set-এ রাখো (sparse)।** direction কে `(dir±1)%4` দিয়ে ঘোরানো — common।

## Common mistake
- পুরো 2D array allocate করা (অসীম, অসম্ভব)।
- ডান/বাঁ ঘোরানোর `% 4` index ভুল করা।
- color flip করার আগে/পরে move করার ক্রম গুলিয়ে ফেলা।

## Follow-up
- **board কত বড় হবে আগে থেকে জানি না** → কালো ঘর track করে শেষে bounding box বের করুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-23"></a>
# 16.23 — Rand7 from Rand5

> Pattern: **Rejection sampling (probability)** · Difficulty: **Medium–Hard** · common

> **বইয়ের ভাষায়:** Implement a method rand7() given rand5(). That is, given a method that generates a random number between 0 and 4 (inclusive), write a method that generates a random number between 0 and 6 (inclusive).

## সমস্যাটা সহজ বাংলায়
`rand5()` দেওয়া — 0..4 থেকে একটা **uniform random** সংখ্যা দেয়। এটা দিয়ে `rand7()` বানাতে হবে — 0..6 থেকে **uniform random**।

## মূল insight — rejection sampling
দুটো rand5() দিয়ে 0..24 (২৫টা সমান-সম্ভাব্য মান) বানাই: `5 * rand5() + rand5()`। এর মধ্যে 0..20 (২১টা = 7×3) রাখি, 21..24 হলে **ফেলে দিয়ে আবার চেষ্টা** (reject)। তারপর `% 7` করলে 0..6 uniform।
```
5*a + b  →  0..24  (২৫টা সমান সম্ভাবনা)
যদি ≥ 21 → reject, আবার চেষ্টা
নাহলে    → মান % 7  →  0..6 uniform (০..২০ → ঠিক ৩ বার করে প্রতিটা মান)
```
কেন 21? কারণ 7-এর গুণিতক হতে হবে যাতে `% 7` uniform থাকে; 0..20 = ২১টা মান, প্রতিটা 0..6 ঠিক ৩ বার।

## Code

```dart
// Dart
int rand5() => /* 0..4 random; ধরা আছে */ 0;

int rand7() {
  while (true) {
    final num = 5 * rand5() + rand5();   // 0..24
    if (num < 21) return num % 7;         // 0..20 → uniform 0..6
    // নাহলে reject, আবার চেষ্টা
  }
}
```
```python
# Python
import random
def rand5() -> int:
    return random.randint(0, 4)

def rand7() -> int:
    while True:
        num = 5 * rand5() + rand5()       # 0..24
        if num < 21:                       # 0..20 → uniform 0..6
            return num % 7
        # নাহলে reject, আবার চেষ্টা
```

## Complexity
- প্রতি call-এ গড়ে `25/21 ≈ 1.19` বার লুপ → **expected O(1)** (worst case unbounded কিন্তু সম্ভাবনা শূন্যের দিকে)।
- **Space: O(1)**।

## Pattern চিনুন
> **"ছোট random দিয়ে বড় uniform random" → বড় range বানাও (গুণ করে), target-এর গুণিতক অংশ রাখো, বাকিটা reject করে retry।** rejection sampling — uniformity রক্ষার মূল কৌশল।

## Common mistake
- 0..24-কে সরাসরি `% 7` করা (21..24 বাদ না দিলে কিছু মান বেশি আসে — non-uniform!)।
- কেন 21 (7×3) সেটা ব্যাখ্যা না করা।

## Follow-up
- **non-terminating কেন গ্রহণযোগ্য?** → প্রতিবার reject-এর সম্ভাবনা 4/25 < 1, তাই expected call সংখ্যা finite।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-24"></a>
# 16.24 — Pairs with Sum

> Pattern: **Hash Map / Two Pointer** · Difficulty: **Easy–Medium** · খুব common

> **বইয়ের ভাষায়:** Design an algorithm to find all pairs of integers within an array which sum to a specified value.

## সমস্যাটা সহজ বাংলায়
একটা array আর একটা target sum দেওয়া। এমন **সব জোড়া (pair)** বের করতে হবে যাদের যোগফল = target।

## উদাহরণ
```
arr = [1, 2, 3, 4, 5, 6],  target = 7
জোড়া: (1,6), (2,5), (3,4)
```

## ভাবনা ১: Brute Force
সব জোড়া মিলিয়ে — **O(n²)**।

## ভাবনা ২: Hash Set (BUD)
প্রতিটা x-এর জন্য খুঁজি `target - x` আগে দেখেছি কিনা। দেখে থাকলে জোড়া। একটা Set-এ দেখা সংখ্যা রাখি।
```
target=7:  x=1 → 6 দেখিনি, রাখো {1}
           x=2 → 5 দেখিনি, {1,2}
           ...
           x=6 → 1 দেখেছি! → জোড়া (1,6)
```

## ভাবনা ৩: Sort + Two Pointer
sort করে দুই প্রান্ত থেকে: sum বড় হলে ডান pointer বাঁয়ে, ছোট হলে বাঁ pointer ডানে।

## Code

```dart
// Dart — Hash Set
List<List<int>> pairsWithSum(List<int> arr, int target) {
  final seen = <int>{};
  final pairs = <List<int>>[];
  for (final x in arr) {
    final complement = target - x;
    if (seen.contains(complement)) pairs.add([complement, x]);
    seen.add(x);
  }
  return pairs;
}
```
```python
# Python — Hash Set
def pairs_with_sum(arr: list, target: int):
    seen = set()
    pairs = []
    for x in arr:
        if target - x in seen:
            pairs.append((target - x, x))
        seen.add(x)
    return pairs
```
```python
# Python — Sort + Two Pointer (duplicate handling সহজ)
def pairs_with_sum_2p(arr: list, target: int):
    arr = sorted(arr)
    i, j = 0, len(arr) - 1
    pairs = []
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            pairs.append((arr[i], arr[j])); i += 1; j -= 1
        elif s < target:
            i += 1
        else:
            j -= 1
    return pairs
```

## Complexity
- Hash Set: **O(n)** time, **O(n)** space।
- Sort + two pointer: **O(n log n)** time, **O(1)** extra space।

## Pattern চিনুন
> **"sum = target এমন জোড়া" → Hash Set (complement খোঁজা), বা sort + two pointer।** "two sum" — interview-র সবচেয়ে common pattern।

## Common mistake
- একই element নিজের সাথে জোড়া বানানো (`x + x`)।
- duplicate জোড়া বারবার দেওয়া (clarify করুন distinct লাগবে কিনা)।

## Follow-up
- **distinct জোড়া only** → sorted two-pointer-এ duplicate skip করুন।
- **triplet (3-sum)** → একটা ঠিক করে বাকি দুটোয় two-sum।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-25"></a>
# 16.25 — LRU Cache

> Pattern: **Hash Map + Doubly Linked List** · Difficulty: **Medium–Hard** · খুব common

> **বইয়ের ভাষায়:** Design and build a "least recently used" cache, which evicts the least recently used item. The cache should map from keys to values (allowing you to insert and retrieve a value associated with a particular key) and be initialized with a max size. When it is full, it should evict the least recently used item.

## সমস্যাটা সহজ বাংলায়
একটা cache বানাতে হবে যার একটা সর্বোচ্চ size আছে। `get(key)` ও `put(key, value)` দুটোই **O(1)**-এ চাই। ভরে গেলে সবচেয়ে **বহু আগে ব্যবহৃত (least recently used)** item সরিয়ে দিতে হবে।

## মূল insight — দুটো structure একসাথে
- **Hash Map** → key থেকে node-এ O(1) jump (lookup)।
- **Doubly Linked List** → ব্যবহারের ক্রম রাখে; head = সদ্য ব্যবহৃত, tail = সবচেয়ে পুরোনো। যেকোনো node O(1)-এ সরানো/সামনে আনা যায়।
```
ব্যবহার করলে → node কে head-এ নিয়ে আসো
ভরে গেলে    → tail-এর node সরাও (least recently used)

  head [সদ্য] <-> ... <-> [পুরোনো] tail
   ↑ get/put এখানে আনে        ↑ eviction এখান থেকে
Map: key → ওই node
```

## Code

```dart
// Dart
class _Node {
  int key, value;
  _Node? prev, next;
  _Node(this.key, this.value);
}

class LRUCache {
  final int capacity;
  final Map<int, _Node> _map = {};
  final _Node _head = _Node(0, 0), _tail = _Node(0, 0);   // dummy
  LRUCache(this.capacity) { _head.next = _tail; _tail.prev = _head; }

  void _remove(_Node n) { n.prev!.next = n.next; n.next!.prev = n.prev; }
  void _addFront(_Node n) {
    n.next = _head.next; n.prev = _head;
    _head.next!.prev = n; _head.next = n;
  }

  int? get(int key) {
    final n = _map[key];
    if (n == null) return null;
    _remove(n); _addFront(n);            // সদ্য ব্যবহৃত → সামনে
    return n.value;
  }

  void put(int key, int value) {
    if (_map.containsKey(key)) { _remove(_map[key]!); }
    final n = _Node(key, value);
    _map[key] = n; _addFront(n);
    if (_map.length > capacity) {
      final lru = _tail.prev!;            // সবচেয়ে পুরোনো
      _remove(lru); _map.remove(lru.key);
    }
  }
}
```
```python
# Python — OrderedDict দিয়ে সহজ (ভেতরে hashmap + linked list)
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)        # সদ্য ব্যবহৃত → শেষে
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # সবচেয়ে পুরোনো সরাও
```
> Python-এ `OrderedDict` ভেতরে ঠিক এই hashmap + doubly-linked-list-ই; interview-তে নিজে implement করতে বললে Dart-এর মতো করে লিখুন।

## Complexity
**Time: O(1)** প্রতি get/put · **Space: O(capacity)**।

## Pattern চিনুন
> **"O(1)-এ get/put + recency-ভিত্তিক eviction" → Hash Map (lookup) + Doubly Linked List (order)।** "O(1) lookup এবং order দুটোই চাই" দেখলেই এই জোড়া মাথায় আনুন।

## Common mistake
- শুধু list (lookup O(n)) বা শুধু map (order নেই) — দুটোই দরকার।
- get-এও node-কে সামনে আনতে ভুলে যাওয়া (recency update হয় না)।
- doubly linked list-এ pointer update-এ বাগ (dummy head/tail দিয়ে সহজ হয়)।

## Follow-up
- **thread-safe LRU** → lock যোগ করুন (Chapter 15)।
- **LFU (least frequently used)** → frequency count + bucket।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q16-26"></a>
# 16.26 — Calculator

> Pattern: **Stack / Expression parsing (precedence)** · Difficulty: **Hard** · common

> **বইয়ের ভাষায়:** Given an arithmetic equation consisting of positive integers, +, -, * and / (no parentheses), compute the result. Example: `2*3+5/6*3+15` → `23.5`.

## সমস্যাটা সহজ বাংলায়
একটা arithmetic expression (শুধু positive integer আর `+ - * /`, কোনো bracket নেই) — তার মান বের করতে হবে। চ্যালেঞ্জ: `* /` কে `+ -`-এর **আগে** (precedence) হিসাব করতে হবে।

## উদাহরণ
```
"2*3+5/6*3+15"
   = 6 + 2.5 + 15  (5/6*3 = 2.5)
   = 23.5
```

## মূল insight — precedence সামলানো
left-to-right পড়ার সময় `* /` সাথে সাথে আগের সংখ্যার সাথে মিলিয়ে ফেলি (কারণ এদের precedence বেশি), আর `+ -` কে পরে যোগ করার জন্য **stack**-এ জমা রাখি।
```
"2*3+5":
  2 দেখলাম → stack: [2]
  * পরের 3 → stack-এর top 2 কে 2*3=6 দিয়ে replace → [6]
  + পরের 5 → পরে যোগ হবে → stack: [6, 5]
শেষে stack যোগ করি: 6 + 5 = 11
(- হলে negative push করি, / হলে top কে ভাগ করি)
```

## Code

```dart
// Dart — single pass, stack দিয়ে precedence
double calculate(String expr) {
  final stack = <double>[];
  int i = 0;
  String op = '+';                            // আগের operator
  expr = '$expr+';                            // শেষ সংখ্যা flush করতে sentinel
  int num = 0;
  while (i < expr.length) {
    final code = expr.codeUnitAt(i);
    if (expr[i] == ' ') { i++; continue; }
    if (code >= 48 && code <= 57) {
      num = num * 10 + (code - 48);            // multi-digit সংখ্যা
    } else {
      switch (op) {
        case '+': stack.add(num.toDouble()); break;
        case '-': stack.add(-num.toDouble()); break;
        case '*': stack.add(stack.removeLast() * num); break;     // উচ্চ precedence
        case '/': stack.add(stack.removeLast() / num); break;
      }
      op = expr[i];
      num = 0;
    }
    i++;
  }
  return stack.fold(0.0, (s, x) => s + x);      // শেষে সব যোগ
}
```
```python
# Python — single pass, stack দিয়ে precedence
def calculate(expr: str) -> float:
    stack = []
    num = 0
    op = '+'                             # আগের operator
    expr = expr + '+'                    # শেষ সংখ্যা flush করতে sentinel
    for ch in expr:
        if ch == ' ':
            continue
        if ch.isdigit():
            num = num * 10 + int(ch)     # multi-digit সংখ্যা
        else:
            if op == '+': stack.append(num)
            elif op == '-': stack.append(-num)
            elif op == '*': stack.append(stack.pop() * num)   # উচ্চ precedence
            elif op == '/': stack.append(stack.pop() / num)
            op = ch
            num = 0
    return sum(stack)                    # শেষে সব যোগ
```

## Complexity
**Time: O(n)** (এক pass) · **Space: O(n)** (stack)।

## Pattern চিনুন
> **"precedence সহ expression evaluate" → stack; `* /` সাথে সাথে top-এর সাথে মিলাও, `+ -` জমিয়ে রাখো, শেষে যোগ।** parentheses থাকলে recursion/দুই stack লাগে।

## Common mistake
- precedence উপেক্ষা করে শুধু left-to-right হিসাব (`2*3+5/6*3` ভুল হবে)।
- multi-digit সংখ্যা (যেমন 15) এক digit করে পড়া।
- শেষ সংখ্যা flush করতে ভুলে যাওয়া (sentinel বা loop-পরে handle)।

## Follow-up
- **parentheses যোগ করো** → recursion (bracket দেখলে sub-expression), বা দুটো stack (operand + operator) দিয়ে shunting-yard।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 16 — সারসংক্ষেপ ও Pattern Cheat Sheet

| # | প্রশ্ন | মূল technique | Time | Space |
|---|---|---|---|---|
| 16.1 | Number Swapper | XOR / arithmetic swap | O(1) | O(1) |
| 16.2 | Word Frequencies | Hash Map precompute | build O(n), query O(1) | O(distinct) |
| 16.3 | Intersection | Line geometry (slope/determinant) | O(1) | O(1) |
| 16.4 | Tic Tac Win | Board line check | O(N²) | O(1) |
| 16.5 | Factorial Zeros | 5-factor counting | O(log n) | O(1) |
| 16.6 | Smallest Difference | Sort + two pointer | O(n log n) | O(1) |
| 16.7 | Number Max | Sign bit (no compare) | O(1) | O(1) |
| 16.8 | English Int | 3-digit grouping + table | O(d) | O(d) |
| 16.9 | Operations | শুধু + দিয়ে build up | O(value) | O(1) |
| 16.10 | Living People | Delta array + running sum | O(P+Y) | O(Y) |
| 16.11 | Diving Board | Combinatorics (K+1 sum) | O(K) | O(K) |
| 16.12 | XML Encoding | Recursive DFS serialize | O(n) | O(depth) |
| 16.13 | Bisect Squares | Center-to-center line | O(1) | O(1) |
| 16.14 | Best Line | Slope Hash Map | O(n²) | O(n) |
| 16.15 | Master Mind | Two-pass frequency | O(n) | O(1) |
| 16.16 | Sub Sort | Boundary + min/max প্রসারণ | O(n) | O(1) |
| 16.17 | Contiguous Sequence | Kadane | O(n) | O(1) |
| 16.18 | Pattern Matching | lenA brute + verify | O(n²) | O(n) |
| 16.19 | Pond Sizes | Flood fill (8-dir DFS) | O(M·N) | O(M·N) |
| 16.20 | T9 | Hash Map precompute (digit→words) | build O(L), query O(1) | O(dict) |
| 16.21 | Sum Swap | Math target + Hash Set | O(A+B) | O(B) |
| 16.22 | Langton's Ant | Sparse simulation | O(K) | O(K) |
| 16.23 | Rand7 from Rand5 | Rejection sampling | expected O(1) | O(1) |
| 16.24 | Pairs with Sum | Hash Set / two pointer | O(n) | O(n) |
| 16.25 | LRU Cache | Hash Map + DLL | O(1) | O(capacity) |
| 16.26 | Calculator | Stack + precedence | O(n) | O(n) |

### "এটা দেখলে → এটা ভাবো" (signal → technique)
```
temp ছাড়া swap                       →  XOR trick
"কতবার আছে?" / বারবার query           →  Hash Map precompute
if/compare ছাড়া                       →  sign bit, branch-less
factorial trailing zero               →  5-factor গোনা
দুই array সবচেয়ে কাছের জোড়া           →  sort + two pointer
সংখ্যা → শব্দ                          →  3-digit group + lookup table
শুধু এক operator দিয়ে বাকিগুলো        →  ছোট থেকে বড় build (negate→...)
"কোন সময়ে সবচেয়ে বেশি overlap"        →  +1/-1 delta + running sum
সবচেয়ে বড় sum subarray               →  Kadane (negative হলে reset)
grid-এ connected region               →  flood fill (DFS/BFS), visited mark
সবচেয়ে বেশি point যে line-এ           →  slope Hash Map (O(n²))
swap করে sum সমান                     →  target = diff/2, Hash Set
অসীম grid step rule                   →  sparse simulation (Set)
ছোট random → বড় uniform random        →  rejection sampling
sum = target জোড়া                     →  Hash Set / two pointer
O(1) get/put + recency eviction       →  Hash Map + Doubly Linked List
precedence সহ expression              →  stack (* / আগে, + - জমিয়ে)
```

### এই chapter-এর ৫টা সোনার নিয়ম
1. **প্রশ্ন চিনুন** — এই chapter-এ নতুন technique কম; "এটা কোন পুরোনো pattern?" — সেটাই আসল কাজ।
2. **Hash Map / Set** বারবার আসে — "কতবার?", "জোড়া?", "আগে দেখেছি?", precompute।
3. **Bit trick** (XOR swap, sign bit) — temp/compare ছাড়া করার দরকার হলে।
4. **Simulation** (TicTac, Pond, Ant) — পুরো state নয়, দরকারি অংশই (sparse Set) রাখুন।
5. **দুই structure একসাথে** — LRU (Map+DLL)-এর মতো, এক structure দিয়ে না হলে দুটো জোড়া দিন।

> **পরের ধাপ:** [Chapter 17 — Hard](chapter17_hard.md) (17.1–17.26) — এই moderate problem গুলোর কঠিন সংস্করণ ও আরও গভীর algorithm।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>
