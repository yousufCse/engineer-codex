# Chapter 8 — Recursion & Dynamic Programming (প্রশ্ন 8.1 – 8.14)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Dart + Python** দুটোতেই।
> এটা সবচেয়ে কঠিন এবং সবচেয়ে গুরুত্বপূর্ণ chapter গুলোর একটি। ধৈর্য ধরে পড়ুন।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Object-Oriented Design](chapter07_object_oriented_design.md) · [পরের: System Design & Scalability](chapter09_system_design_scalability.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

- [8.1 — Triple Step](#q8-1)
- [8.2 — Robot in a Grid](#q8-2)
- [8.3 — Magic Index](#q8-3)
- [8.4 — Power Set](#q8-4)
- [8.5 — Recursive Multiply](#q8-5)
- [8.6 — Towers of Hanoi](#q8-6)
- [8.7 — Permutations without Dups](#q8-7)
- [8.8 — Permutations with Dups](#q8-8)
- [8.9 — Parens](#q8-9)
- [8.10 — Paint Fill](#q8-10)
- [8.11 — Coins](#q8-11)
- [8.12 — Eight Queens](#q8-12)
- [8.13 — Stack of Boxes](#q8-13)
- [8.14 — Boolean Evaluation](#q8-14)

---

## Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

এই background না বুঝলে পরের ১৪টা প্রশ্ন বোঝা কঠিন। মনোযোগ দিয়ে পড়ুন।

---

### ১. Recursion কী — "trust the recursion" মানসিকতা

Recursion মানে হলো **একটা function নিজেকেই ডাকা**, কিন্তু একটু **ছোট সমস্যার জন্য**।

মাথায় রাখুন: recursion ভালো করতে হলে একটাই মানসিকতা লাগে —

> **"ছোট সমস্যার উত্তর কেউ একজন আমাকে দিয়ে দেবে (আমার function নিজেই), আমাকে শুধু সেটা ব্যবহার করতে হবে।"**

এই বিশ্বাসের নামই **"trust the recursion"**।

উদাহরণ — `factorial(n)`:

```
factorial(5) = 5 × factorial(4)
factorial(4) = 4 × factorial(3)
factorial(3) = 3 × factorial(2)
factorial(2) = 2 × factorial(1)
factorial(1) = 1             ← এটাই base case, আর recursion নেই
```

আপনি শুধু ভাবুন: "factorial(n) = n × factorial(n-1)"।
factorial(n-1) কীভাবে বের হবে — সেটা আপনার কাজ না। আপনার function নিজেই বের করবে।

---

### ২. Base Case vs Recursive Case

প্রতিটা recursive function-এ দুটো অংশ থাকে:

```
function solve(n):
    if n <= 0:          ← BASE CASE: এখানে থামো, সরাসরি উত্তর দাও
        return 0
    return n + solve(n-1)  ← RECURSIVE CASE: ছোট করে নিজেকে ডাকো
```

**Base case না থাকলে কী হয়?**
Function থামে না — অনন্তকাল চলতে থাকে → **Stack Overflow** crash।

Base case খোঁজার সহজ উপায়: "সবচেয়ে ছোট input দিলে উত্তর কী?" — সেটাই base case।

---

### ৩. Recursion Tree — কীভাবে subproblem repeat হয়

Recursion tree মানে হলো function call গুলো গাছের মতো এঁকে দেখানো। এতে বোঝা যায় কোন subproblem বারবার হিসাব হচ্ছে।

উদাহরণ — Fibonacci(4):

```
                    fib(4)
                  /        \
            fib(3)          fib(2)
           /      \        /      \
       fib(2)   fib(1)  fib(1)  fib(0)
       /    \
   fib(1)  fib(0)

fib(2) দুইবার হিসাব হলো!
fib(1) তিনবার হিসাব হলো!
```

এই **repeated subproblem** মানেই DP-র সুযোগ।

---

### ৪. তিনটি Approach — Brute Recursion থেকে DP পর্যন্ত

**Approach 1: Brute Force Recursion**
- সহজ, intuitive
- কিন্তু ধীর — একই subproblem বারবার হিসাব করে
- fib(n) এ Time: O(2^n)

**Approach 2: Top-Down Memoization (Cache করা)**
- Recursion চলতে থাকে, কিন্তু প্রতিটা উত্তর **memo table-এ রেখে দাও**
- পরে একই subproblem এলে table থেকে পড়ো — আবার হিসাব করো না
- "Top-Down" কারণ বড় problem থেকে শুরু করে ছোটতে যাই
- fib(n) এ Time: O(n), Space: O(n)

```
memo = {}

fib(4)
  └─ fib(3)
      └─ fib(2)
          └─ fib(1) → 1  [memo তে রাখো]
          └─ fib(0) → 0  [memo তে রাখো]
          → 1  [memo তে রাখো]
      └─ fib(1) → memo তে আছে! সরাসরি 1
      → 2  [memo তে রাখো]
  └─ fib(2) → memo তে আছে! সরাসরি 1
  → 3
```

**Approach 3: Bottom-Up Tabulation (Table ভরা)**
- Recursion নেই — loop দিয়ে ছোট subproblem আগে solve করো
- উত্তর একটা table-এ রাখো, বড় problem সেটা থেকে নেয়
- "Bottom-Up" কারণ ছোট থেকে শুরু করে বড়তে যাই
- fib(n) এ Time: O(n), Space: O(n) বা O(1) (শুধু আগের দুটো রাখলে)

```
table[0] = 0
table[1] = 1
table[2] = table[1] + table[0] = 1
table[3] = table[2] + table[1] = 2
table[4] = table[3] + table[2] = 3
```

---

### ৫. কখন বুঝব এটা DP সমস্যা?

এই তিনটা signal দেখলেই DP ভাবুন:

```
Signal 1: "Optimal" কিছু চাওয়া (minimum, maximum, shortest, fewest)
Signal 2: "কতভাবে/কতরকমে করা যায়" — count of ways
Signal 3: "পারবে কিনা" — can you do X?

+ সাথে যদি: subproblem repeat হয় (recursion tree-তে দেখা যায়)
```

**DP-র চাবিকাঠি**: সমস্যাটাকে **subproblem-এ ভাঙো** এবং **recurrence relation** লিখুন — "বড় সমস্যার উত্তর = ছোট সমস্যার উত্তর দিয়ে বানানো"।

---
---

<a id="q8-1"></a>
# 8.1 — Triple Step

> Pattern: **1D DP / Fibonacci-style** · Difficulty: **Easy** · খুব common (DP-এর প্রথম প্রশ্ন হিসেবে)

> **বইয়ের ভাষায়:** A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

## সমস্যাটা সহজ বাংলায়

একটা সিঁড়িতে n টা ধাপ। একবারে ১, ২, বা ৩ ধাপ লাফ দেওয়া যায়। **কতভাবে** উপরে ওঠা যায় — সেটা বের করতে হবে।

## উদাহরণ

```
n = 3:
  ways:
    1+1+1
    1+2
    2+1
    3
  মোট = 4 ways

n = 4:
  1+1+1+1
  1+1+2
  1+2+1
  2+1+1
  2+2
  1+3
  3+1
  মোট = 7 ways
```

## ধাপ ১: Listen

- **n = 0 মানে কী?** ধাপ 0-তেই আছি — ১ ভাবে (কিছু না করে)? নাকি 0? বইয়ে base case হিসেবে `ways(0)=1` ধরা হয়েছে (শূন্য ধাপ মানে একটাই পথ: কিছু না করা)।
- **Overflow?** বড় n-এ answer খুব বড় হয়। ধরে নিচ্ছি int/long যথেষ্ট।

## ধাপ ২: Brute Force — সরাসরি Recursion

মূল insight: n নম্বর ধাপে পৌঁছাতে হলে আমি আসতে পারি:
- step `n-1` থেকে (১ লাফ দিয়ে), বা
- step `n-2` থেকে (২ লাফ দিয়ে), বা
- step `n-3` থেকে (৩ লাফ দিয়ে)

তাই: **ways(n) = ways(n-1) + ways(n-2) + ways(n-3)**

Recursion Tree (n=4):

```
                        ways(4)
               /           |           \
          ways(3)        ways(2)      ways(1)
          /   |   \      /    \          |
      w(2) w(1) w(0) w(1) w(0)       w(0)
      / \    |          |
   w(1) w(0) w(0)     w(0)

ways(2) দুইবার হিসাব হলো!
ways(1) দুইবার হিসাব হলো!
ways(0) চারবার হিসাব হলো!
```

এটাই repeated subproblem — DP-র সুযোগ।

Time: O(3^n) (প্রতিটা call ৩টা call করে) · Space: O(n) (call stack)

## ধাপ ৩: Optimize — Memoization (Top-Down)

একবার হিসাব করা subproblem map-এ রেখে দিই:

```dart
// Dart — Memoization
int countWays(int n, [Map<int, int>? memo]) {
  memo ??= {};
  if (n < 0) return 0;           // অসম্ভব path
  if (n == 0) return 1;          // ঠিক এখানে আছি = ১টা way
  if (memo.containsKey(n)) return memo[n]!;   // আগে হিসাব হয়েছে
  memo[n] = countWays(n - 1, memo)
           + countWays(n - 2, memo)
           + countWays(n - 3, memo);
  return memo[n]!;
}
```

```python
# Python — Memoization
def count_ways(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = count_ways(n-1, memo) + count_ways(n-2, memo) + count_ways(n-3, memo)
    return memo[n]
```

Time: O(n) · Space: O(n)

## ধাপ ৪: Optimize — Bottom-Up Tabulation

```dart
// Dart — Bottom-Up DP
int countWaysDP(int n) {
  if (n == 0) return 1;
  if (n == 1) return 1;
  if (n == 2) return 2;
  // table[i] = i ধাপে পৌঁছানোর ways
  final table = List<int>.filled(n + 1, 0);
  table[0] = 1;   // base: 0 ধাপে ১ way
  table[1] = 1;   // 1 ধাপে: {1}
  table[2] = 2;   // 2 ধাপে: {1+1, 2}
  for (int i = 3; i <= n; i++) {
    table[i] = table[i-1] + table[i-2] + table[i-3];
  }
  return table[n];
}
```

```python
# Python — Bottom-Up DP
def count_ways_dp(n: int) -> int:
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    table = [0] * (n + 1)
    table[0], table[1], table[2] = 1, 1, 2
    for i in range(3, n + 1):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    return table[n]
```

Time: O(n) · Space: O(n) — আরও কমিয়ে O(1) করা যায়: শুধু আগের তিনটা variable রাখুন।

## Complexity তুলনা

| Approach | Time | Space |
|---|---|---|
| Brute recursion | O(3^n) | O(n) |
| Memoization (top-down) | O(n) | O(n) |
| Bottom-up tabulation | O(n) | O(n) বা O(1) |

## Pattern চিনুন

> **"কতভাবে পৌঁছানো যায়, শেষ পদক্ষেপ ১/২/৩ রকম" → ways(n) = ways(n-1) + ways(n-2) + ways(n-3)।** এটা Fibonacci-র extension — সিঁড়ি, টাইলস, jump সব এই pattern।

## Common mistake

- `n < 0` return 0 ভুলে যাওয়া — n-3 করলে negative হতে পারে।
- base case `ways(0) = 1` না `0` — এটা নিয়ে সন্দেহ হলে interviewer-কে জিজ্ঞেস করুন।
- memoization-এ default mutable argument (Python-এ `memo={}` না লিখে `memo=None` + ভেতরে init করুন)।

## Follow-up

- **k রকম লাফ দিলে (variable step sizes)?** → `ways(n) = sum(ways(n-s) for s in steps if s <= n)`।
- **Modulo 10^9+7?** → প্রতিটা add-এর পরে mod নিন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-2"></a>
# 8.2 — Robot in a Grid

> Pattern: **2D DP / Grid Pathfinding + Backtracking** · Difficulty: **Medium** · Common

> **বইয়ের ভাষায়:** Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits." Design an algorithm to find a path for the robot from the top left to the bottom right.

## সমস্যাটা সহজ বাংলায়

একটা grid-এ robot উপরের বাঁয়ে (0,0) আছে। শুধু **ডানে বা নিচে** যেতে পারে। কিছু ঘর **blocked** (যাওয়া যাবে না)। নিচের ডানে (r-1, c-1) পর্যন্ত **একটা path** বের করতে হবে।

## উদাহরণ

```
Grid (0=free, X=blocked):

  0  0  0  0
  0  X  0  X
  0  0  0  0

Start: (0,0)  Goal: (2,3)

একটা path:
(0,0) → (0,1) → (0,2) → (0,3)
        অথবা
(0,0) → (1,0) → (2,0) → (2,1) → (2,2) → (2,3)
```

## ধাপ ১: Listen

- **path বের করতে হবে না শুধু আছে কিনা?** বইয়ে path-টা return করতে বলা হয়েছে।
- **Diagonal চলা যাবে?** না।
- **Grid-এ কী blocked?** `null`, `true`, বা একটা বিশেষ value।

## ধাপ ২: Brute Force — Recursion

শেষ cell (r-1, c-1)-এ পৌঁছাতে হলে আমি এসেছি হয় উপর থেকে (r-2, c-1) বা বাঁ থেকে (r-1, c-2)।

তাই: **hasPath(r, c) = hasPath(r-1, c) || hasPath(r, c-1)**

```
hasPath(2,3)
├── hasPath(1,3)
│   ├── hasPath(0,3) → ছোট করতে করতে (0,0) পর্যন্ত যাই
│   └── hasPath(1,2)
└── hasPath(2,2)
    ├── hasPath(1,2)  ← আবার! repeated subproblem
    └── hasPath(2,1)
```

Time: O(2^(r+c)) · Space: O(r+c) stack

## ধাপ ৩: Optimize — Memoization

Failed cell গুলো (যেখান থেকে goal-এ পৌঁছানো যায় না) একটা Set-এ রেখে দিই — আবার চেষ্টা করব না।

```dart
// Dart — Memoization + path tracking
List<(int, int)>? findPath(List<List<bool>> grid) {
  if (grid.isEmpty) return null;
  final path = <(int, int)>[];
  final failed = <(int, int)>{};
  if (_helper(grid, grid.length - 1, grid[0].length - 1, path, failed)) {
    return path;
  }
  return null;
}

bool _helper(
    List<List<bool>> grid, int row, int col,
    List<(int, int)> path, Set<(int, int)> failed) {
  // সীমার বাইরে বা blocked
  if (row < 0 || col < 0 || !grid[row][col]) return false;
  final p = (row, col);
  if (failed.contains(p)) return false;   // আগে fail হয়েছে
  final isOrigin = (row == 0 && col == 0);
  // উপর থেকে বা বাঁ থেকে পথ আছে কিনা
  if (isOrigin ||
      _helper(grid, row - 1, col, path, failed) ||
      _helper(grid, row, col - 1, path, failed)) {
    path.add(p);
    return true;
  }
  failed.add(p);   // এখান থেকে goal যাওয়া যায় না — মনে রাখো
  return false;
}
```

```python
# Python — Memoization + path tracking
def find_path(grid: list) -> list:
    if not grid:
        return None
    path = []
    failed = set()
    if _helper(grid, len(grid)-1, len(grid[0])-1, path, failed):
        return path
    return None

def _helper(grid, row, col, path, failed):
    if row < 0 or col < 0 or not grid[row][col]:
        return False
    p = (row, col)
    if p in failed:
        return False
    is_origin = (row == 0 and col == 0)
    if is_origin or _helper(grid, row-1, col, path, failed) \
                 or _helper(grid, row, col-1, path, failed):
        path.append(p)
        return True
    failed.add(p)
    return False
```

Time: O(r × c) · Space: O(r × c)

## Pattern চিনুন

> **"Grid-এ path খোঁজা, শুধু ডানে-নিচে" → 2D DP বা recursion + memoization।** failed cell মনে রাখাটাই optimization-এর চাবিকাঠি।

## Common mistake

- Memoization না করলে O(2^(r+c)) — blocked cell থাকলে বিশেষ করে ধীর।
- Recursion-এ path-tracking উল্টো হয় (শেষ থেকে শুরু করে build হয় — সঠিক)।
- Grid bounds check বাদ দেওয়া।

## Follow-up

- **সব path বের করো** → backtracking, memoization কাজ করবে না (সব পথ লাগবে)।
- **Minimum cost path** → DP দিয়ে `cost[r][c] = grid[r][c] + min(cost[r-1][c], cost[r][c-1])`।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-3"></a>
# 8.3 — Magic Index

> Pattern: **Binary Search (modified) / Recursion** · Difficulty: **Medium** · কম common

> **বইয়ের ভাষায়:** A magic index in an array `A[0..n-1]` is defined to be an index such that `A[i] = i`. Given a sorted array of distinct integers, write a method to find a magic index, if one exists.
> **Follow-up:** What if the values are not distinct?

## সমস্যাটা সহজ বাংলায়

Sorted array-তে এমন একটা index `i` খুঁজতে হবে যেখানে `A[i] == i`। এটাকেই "magic index" বলে।

## উদাহরণ

```
index:  0   1   2   3   4   5   6   7   8
array: -2  -1   0   3   5   6   7   8  10
                    ↑
              A[3] = 3 → magic index!
```

## Distinct values হলে: Binary Search

Array sorted এবং values distinct। যদি `A[mid] > mid` হয় → magic index বাঁয়ে থাকতে পারে না কেন?

```
কারণ: A[mid] > mid, এবং values distinct+sorted মানে
  A[mid-1] >= A[mid]-1 > mid-1
  তাই বাঁয়ে সব A[i] > i → magic index বাঁয়ে নেই।
তাই ডানে যাই।
```

```dart
// Dart — Distinct integers
int magicIndex(List<int> arr, [int? lo, int? hi]) {
  lo ??= 0;
  hi ??= arr.length - 1;
  if (lo > hi) return -1;
  final mid = (lo + hi) ~/ 2;
  if (arr[mid] == mid) return mid;
  if (arr[mid] > mid) return magicIndex(arr, lo, mid - 1);  // বাঁয়ে
  return magicIndex(arr, mid + 1, hi);                      // ডানে
}
```

```python
# Python — Distinct integers
def magic_index(arr: list, lo: int = 0, hi: int = None) -> int:
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == mid:
        return mid
    if arr[mid] > mid:
        return magic_index(arr, lo, mid - 1)
    return magic_index(arr, mid + 1, hi)
```

Time: O(log n) · Space: O(log n) stack

## Non-distinct values হলে: দুই দিকেই দেখতে হবে

```
index:  0   1   2   3   4   5   6   7   8
array: -2   0   2   2   2   5   7  10  10
        ↑           ↑           ↑
      A[0]=-2   A[2]=2!     A[5]=5!
```

Values distinct না হলে binary search ভাঙে — দুই দিকেই যেতে হতে পারে।

কিন্তু চালাকি: `A[mid] < mid` হলে বাঁয়ের শুধু index `A[mid]` পর্যন্ত দেখলেই চলে (তার আগে magic হওয়া অসম্ভব)।

```dart
// Dart — Non-distinct integers
int magicIndexND(List<int> arr, int lo, int hi) {
  if (lo > hi) return -1;
  final mid = (lo + hi) ~/ 2;
  if (arr[mid] == mid) return mid;
  // বাঁয়ে: mid-1 আর arr[mid] এর minimum পর্যন্ত
  final leftIdx = magicIndexND(arr, lo, mid - 1 < arr[mid] ? mid - 1 : arr[mid]);
  if (leftIdx != -1) return leftIdx;
  // ডানে: mid+1 আর arr[mid] এর maximum থেকে
  return magicIndexND(arr, arr[mid] > mid + 1 ? arr[mid] : mid + 1, hi);
}
```

```python
# Python — Non-distinct integers
def magic_index_nd(arr: list, lo: int, hi: int) -> int:
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == mid:
        return mid
    left = magic_index_nd(arr, lo, min(mid - 1, arr[mid]))
    if left != -1:
        return left
    return magic_index_nd(arr, max(mid + 1, arr[mid]), hi)
```

Time: O(log n) average (distinct), O(n) worst (non-distinct) · Space: O(log n)

## Pattern চিনুন

> **"Sorted array-এ কিছু খোঁজা" → Binary search, কিন্তু শর্ত বুঝে কোনদিকে যাবে সিদ্ধান্ত নাও।** Non-distinct হলে দুই দিকেই যেতে হতে পারে।

## Common mistake

- Non-distinct case-এ সরাসরি binary search করা — ভুল উত্তর দেয়।
- Pruning ভুল করা (বাঁয়ে কতটুকু দেখব সেটা `min(mid-1, arr[mid])`)।

## Follow-up

- **কয়টা magic index আছে?** Distinct হলে বড়জোর ১টা; non-distinct হলে একাধিক হতে পারে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-4"></a>
# 8.4 — Power Set

> Pattern: **Recursion / Bit Manipulation** · Difficulty: **Medium** · Common

> **বইয়ের ভাষায়:** Write a method to return all subsets of a set.

## সমস্যাটা সহজ বাংলায়

একটা set-এর **সব সম্ভাব্য subset** বের করতে হবে। খালি set `{}` এবং পুরো set নিজেও subset।

## উদাহরণ

```
input: {1, 2, 3}

সব subset:
{}
{1}
{2}
{3}
{1,2}
{1,3}
{2,3}
{1,2,3}

মোট = 2^3 = 8 টা
```

## ধাপ ১: Recursion দিয়ে ভাবা

প্রতিটা element-এর জন্য দুটো choice: **নেব বা নেব না।**

n elements-এর power set = n-1 elements-এর power set × (নতুন element যোগ করা বা না করা)

```
powerSet({1,2,3}) থেকে ভাবি:
  powerSet({1,2}) জানি
  এখন প্রতিটা existing subset-এ '3' যোগ করলে নতুন subset

  {}, {1}, {2}, {1,2}     ← powerSet({1,2})
  {3}, {1,3}, {2,3}, {1,2,3}  ← প্রতিটায় 3 যোগ করলে

  দুটো মিলে = powerSet({1,2,3})
```

```dart
// Dart — Recursive approach
List<List<int>> powerSet(List<int> set, [int index = 0]) {
  if (index == set.length) {
    return [[]];   // base case: খালি subset
  }
  // বাকি element গুলোর subset নিই
  final allSubsets = powerSet(set, index + 1);
  final newSubsets = <List<int>>[];
  final item = set[index];
  for (final subset in allSubsets) {
    // বর্তমান item টা যোগ করে নতুন subset বানাই
    newSubsets.add([item, ...subset]);
  }
  return [...allSubsets, ...newSubsets];
}
```

```python
# Python — Recursive approach
def power_set(s: list, index: int = 0) -> list:
    if index == len(s):
        return [[]]    # base case: শুধু খালি subset
    all_subsets = power_set(s, index + 1)
    item = s[index]
    new_subsets = [[item] + subset for subset in all_subsets]
    return all_subsets + new_subsets
```

Time: O(n × 2^n) · Space: O(n × 2^n) — আউটপুটেই এতটুকু লাগে

## ধাপ ২: Bit Manipulation দিয়ে (চালাক approach)

n elements-এর জন্য আমরা 0 থেকে 2^n-1 পর্যন্ত সব integer নিই। প্রতিটা integer-এর binary representation দেখি — k-th bit 1 হলে k-th element নেব।

```
n=3, elements={a, b, c}

decimal  binary  subset
0        000     {}
1        001     {c}
2        010     {b}
3        011     {b,c}
4        100     {a}
5        101     {a,c}
6        110     {a,b}
7        111     {a,b,c}
```

```dart
// Dart — Bit manipulation
List<List<int>> powerSetBits(List<int> set) {
  final n = set.length;
  final total = 1 << n;   // 2^n
  final result = <List<int>>[];
  for (int mask = 0; mask < total; mask++) {
    final subset = <int>[];
    for (int i = 0; i < n; i++) {
      if ((mask >> i) & 1 == 1) {   // i-th bit set?
        subset.add(set[i]);
      }
    }
    result.add(subset);
  }
  return result;
}
```

```python
# Python — Bit manipulation
def power_set_bits(s: list) -> list:
    n = len(s)
    total = 1 << n   # 2^n
    result = []
    for mask in range(total):
        subset = [s[i] for i in range(n) if (mask >> i) & 1]
        result.append(subset)
    return result
```

Time: O(n × 2^n) · Space: O(n × 2^n)

## Pattern চিনুন

> **"সব subset / combination / include-or-exclude" → recursion (এই element নেব না নেব না) অথবা bit mask (0 থেকে 2^n-1)।**

## Common mistake

- Base case ভুল করা — শেষ index-এ খালি list return করতে হয়, না করলে সব ভেঙে পড়ে।
- Bit mask approach-এ `1 << n` overflow হতে পারে বড় n-এ।

## Follow-up

- **Duplicate element থাকলে?** → আগে sort করুন, একই element পরপর দেখলে skip করুন।
- **নির্দিষ্ট size k-এর subset?** → Combination — recursion-এ size track করুন।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-5"></a>
# 8.5 — Recursive Multiply

> Pattern: **Recursion + Bit Shift (logarithmic)** · Difficulty: **Medium** · কম common

> **বইয়ের ভাষায়:** Write a recursive function to multiply two positive integers without using the `*` operator (or `/`). You can use addition, subtraction, and bit shifting.

## সমস্যাটা সহজ বাংলায়

`*` বা `/` ব্যবহার না করে শুধু **যোগ, বিয়োগ, bit shift** দিয়ে দুটো positive integer গুণ করতে হবে। Recursion ব্যবহার করতে হবে।

## ধাপ ১: সহজ approach — বারবার যোগ

`a × b = a কে b বার যোগ করা`। কিন্তু এটা O(b) — ধীর।

## ধাপ ২: চালাক Recursion — half করে ভাগ

`a × b` কে ভাবি:
- যদি `b` জোড়: `a × b = (a × b/2) + (a × b/2)` — একটা subproblem দুবার ব্যবহার
- যদি `b` বিজোড়: `a × b = (a × (b-1)/2) + (a × (b-1)/2) + a`

```
multiply(8, 7):
  7 বিজোড় → multiply(8, 3) + multiply(8, 3) + 8
             3 বিজোড় → multiply(8, 1) + multiply(8, 1) + 8
                        1 বিজোড় → multiply(8, 0) + multiply(8, 0) + 8
                                   0 → return 0
                        = 0 + 0 + 8 = 8
             = 8 + 8 + 8 = 24
  = 24 + 24 + 8 = 56  ← সঠিক (8×7=56)
```

Memoization দিয়ে `multiply(a, half)` একবারই হিসাব হবে।

```dart
// Dart — Recursive Multiply O(log b)
int multiply(int a, int b) {
  if (b == 0) return 0;
  if (b == 1) return a;
  final half = multiply(a, b >> 1);   // b/2 (bit shift = দ্রুত ভাগ)
  if (b & 1 == 0) {                   // b জোড়
    return half + half;
  } else {                            // b বিজোড়
    return half + half + a;
  }
}
```

```python
# Python — Recursive Multiply O(log b)
def multiply(a: int, b: int) -> int:
    if b == 0:
        return 0
    if b == 1:
        return a
    half = multiply(a, b >> 1)   # b//2
    if b & 1 == 0:               # b জোড়
        return half + half
    else:                        # b বিজোড়
        return half + half + a
```

Time: O(log b) · Space: O(log b) stack

## Pattern চিনুন

> **"গুণ / ঘাত — বারবার না করে অর্ধেক করে ভাগ করো" → Divide and Conquer, O(log n)।** এটা "fast exponentiation" বা "binary exponentiation"-এর সমতুল্য।

## Common mistake

- `half = multiply(a, b/2)` দুবার call করা — O(n) হয়ে যায়। একবার call করে result variable-এ রেখে দুবার যোগ করুন।
- b বিজোড় case-এ extra `a` যোগ করতে ভুলে যাওয়া।

## Follow-up

- **Negative integer হলে?** → sign আলাদা করুন, absolute value-এ multiply করুন।
- **Power(a, b) — ঘাত?** → একই চিন্তা: `pow(a, b) = pow(a, b/2) × pow(a, b/2)` (বিজোড় হলে আরেকটা `a`)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-6"></a>
# 8.6 — Towers of Hanoi

> Pattern: **Classic Recursion** · Difficulty: **Medium** · মাঝে মাঝে আসে

> **বইয়ের ভাষায়:** In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (the smallest at the top). Move all the disks to the last rod with these rules: (1) Only one disk can be moved at a time. (2) A disk can only be placed on top of a larger disk. (3) A move consists of taking the upper-most disk from one of the stacks and placing it on top of another stack.

## সমস্যাটা সহজ বাংলায়

৩টা খুঁটি (peg) আছে। শুরুতে সব disk প্রথম খুঁটিতে, ছোট-বড় ক্রমে (উপরে ছোট)। সব disk শেষ খুঁটিতে নিয়ে যাও — একবারে এক disk, বড়টার উপর ছোটটা রাখা যাবে না।

## মূল insight — Recursion কীভাবে ভাবব

n disk সরাতে হলে:

```
ধাপ ১: উপরের n-1 disk → source থেকে buffer-এ (destination ব্যবহার করে)
ধাপ ২: সবচেয়ে বড় disk (n-th) → source থেকে destination-এ
ধাপ ৩: n-1 disk → buffer থেকে destination-এ (source ব্যবহার করে)

n=3, Source=A, Buffer=B, Dest=C:

     ___          
    |_1_|         
    |_2_|         
    |_3_|         
      A      B      C

ধাপ ১: n-1=2 disk A → B (C ব্যবহার করে)
ধাপ ২: disk 3   A → C
ধাপ ৩: n-1=2 disk B → C (A ব্যবহার করে)
```

Recursion Tree (n=3):

```
hanoi(3, A→C via B)
├── hanoi(2, A→B via C)
│   ├── hanoi(1, A→C via B)  → move disk 1: A→C
│   ├── move disk 2: A→B
│   └── hanoi(1, C→B via A)  → move disk 1: C→B
├── move disk 3: A→C
└── hanoi(2, B→C via A)
    ├── hanoi(1, B→A via C)  → move disk 1: B→A
    ├── move disk 2: B→C
    └── hanoi(1, A→C via B)  → move disk 1: A→C
```

মোট moves: 2^n - 1 = 7 (n=3 এর জন্য)।

```dart
// Dart — Towers of Hanoi
void hanoi(int n, String source, String destination, String buffer) {
  if (n == 0) return;   // base case: কোনো disk নেই
  // উপরের n-1 disk source → buffer
  hanoi(n - 1, source, buffer, destination);
  // সবচেয়ে বড় disk source → destination
  print('Move disk $n from $source to $destination');
  // n-1 disk buffer → destination
  hanoi(n - 1, buffer, destination, source);
}
// ব্যবহার: hanoi(3, 'A', 'C', 'B');
```

```python
# Python — Towers of Hanoi
def hanoi(n: int, source: str, destination: str, buffer: str) -> None:
    if n == 0:
        return
    # উপরের n-1 disk source → buffer
    hanoi(n - 1, source, buffer, destination)
    # সবচেয়ে বড় disk source → destination
    print(f"Move disk {n} from {source} to {destination}")
    # n-1 disk buffer → destination
    hanoi(n - 1, buffer, destination, source)
# ব্যবহার: hanoi(3, 'A', 'C', 'B')
```

Time: O(2^n) · Space: O(n) stack — এর চেয়ে কম moves-এ সম্ভব না (প্রমাণ করা যায়)

## Pattern চিনুন

> **"Hanoi / 3 objects-এ সরানো" → classic recursion: n-1 সরাও, তারপর n-th কাজ করো, তারপর n-1 আবার সরাও।** এই pattern অনেক "move/rearrange" সমস্যায় দেখা যায়।

## Common mistake

- Source, destination, buffer গুলিয়ে ফেলা — parameter-এর ক্রম মাথায় রাখুন।
- Base case `n == 0` না `n == 1` — `n == 0` বেশি natural (0 disk মানে কিছু করো না)।

## Follow-up

- **Minimum কতটা move?** → 2^n - 1। এর কম সম্ভব না।
- **4টা peg থাকলে?** → Frame-Stewart algorithm (open problem for general case)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-7"></a>
# 8.7 — Permutations without Dups

> Pattern: **Recursion / Backtracking** · Difficulty: **Medium** · Common

> **বইয়ের ভাষায়:** Write a method to compute all permutations of a string of unique characters.

## সমস্যাটা সহজ বাংলায়

একটা string-এর সব character unique। এদের সব **সম্ভাব্য সাজানো (permutation)** বের করতে হবে।

## উদাহরণ

```
input: "abc"

সব permutation:
"abc"  "acb"  "bac"  "bca"  "cab"  "cba"

মোট: 3! = 6 টা
```

## Recursion দিয়ে ভাবা

n character-এর permutation = প্রথম position-এ একটা character বসাই, বাকি n-1 character-এর permutation পাই।

```
perm("abc"):
  ← 'a' প্রথমে → perm("bc") = "bc", "cb"
                   → "abc", "acb"
  ← 'b' প্রথমে → perm("ac") = "ac", "ca"
                   → "bac", "bca"
  ← 'c' প্রথমে → perm("ab") = "ab", "ba"
                   → "cab", "cba"
```

**Approach: prefix + remaining**

`permutations(prefix, remaining)` — prefix এ এতক্ষণ কী বানিয়েছি, remaining-এ কী বাকি।

```dart
// Dart
List<String> permutations(String str) {
  final result = <String>[];
  _permHelper('', str, result);
  return result;
}

void _permHelper(String prefix, String remaining, List<String> result) {
  if (remaining.isEmpty) {
    result.add(prefix);   // base case: কিছু বাকি নেই, একটা permutation পেলাম
    return;
  }
  for (int i = 0; i < remaining.length; i++) {
    final ch = remaining[i];
    final rest = remaining.substring(0, i) + remaining.substring(i + 1);
    _permHelper(prefix + ch, rest, result);   // ch নিলাম, বাকি rest
  }
}
```

```python
# Python
def permutations(s: str) -> list:
    result = []
    _perm_helper('', s, result)
    return result

def _perm_helper(prefix: str, remaining: str, result: list) -> None:
    if not remaining:
        result.append(prefix)
        return
    for i in range(len(remaining)):
        ch = remaining[i]
        rest = remaining[:i] + remaining[i+1:]
        _perm_helper(prefix + ch, rest, result)
```

Time: O(n! × n) — n! পারমুটেশন, প্রতিটা বানাতে O(n) · Space: O(n! × n)

## Pattern চিনুন

> **"সব arrangement / permutation" → recursion, প্রতিটা position-এ বাকি সব character try করো।** এটা backtracking-এর সহজ রূপ।

## Common mistake

- Remaining string থেকে selected character বাদ দিতে ভুলে যাওয়া।
- n=0 বা n=1 edge case।

## Follow-up

- **Duplicate character থাকলে?** → পরের প্রশ্ন 8.8।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-8"></a>
# 8.8 — Permutations with Dups

> Pattern: **Backtracking + Frequency Map** · Difficulty: **Medium** · Common

> **বইয়ের ভাষায়:** Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.

## সমস্যাটা সহজ বাংলায়

এখন string-এ character **repeat** হতে পারে। কিন্তু output permutation list-এ **duplicate** থাকা যাবে না।

## উদাহরণ

```
input: "aab"

সব unique permutation:
"aab"  "aba"  "baa"

(naive করলে 3!=6টা আসত, কিন্তু "aab" দুটো 'a' আলাদা ধরলে;
duplicate বাদ দিলে ৩টা)
```

## Approach: Frequency Map দিয়ে

প্রতিটা character কতবার আছে Map-এ রাখি। প্রতিটা step-এ map-এ যেসব character বাকি আছে, একটা একটা করে বেছে নিই (count কমাই), recurse করি, তারপর count ফেরত দিই (backtrack)।

এতে একই character পরপর দুবার একই position-এ বসানো হয় না — তাই duplicate permutation আসে না।

```dart
// Dart — with frequency map
List<String> permutationsWithDups(String str) {
  final result = <String>[];
  final freq = <String, int>{};
  for (final ch in str.split('')) {
    freq[ch] = (freq[ch] ?? 0) + 1;
  }
  _permDups('', str.length, freq, result);
  return result;
}

void _permDups(String prefix, int remaining,
    Map<String, int> freq, List<String> result) {
  if (remaining == 0) {
    result.add(prefix);
    return;
  }
  for (final ch in freq.keys) {
    final c = freq[ch]!;
    if (c > 0) {
      freq[ch] = c - 1;                          // এই character নিলাম
      _permDups(prefix + ch, remaining - 1, freq, result);
      freq[ch] = c;                              // backtrack
    }
  }
}
```

```python
# Python — with frequency map
from collections import Counter

def permutations_with_dups(s: str) -> list:
    result = []
    freq = Counter(s)
    _perm_dups('', len(s), freq, result)
    return result

def _perm_dups(prefix: str, remaining: int, freq: dict, result: list) -> None:
    if remaining == 0:
        result.append(prefix)
        return
    for ch in freq:
        if freq[ch] > 0:
            freq[ch] -= 1                    # এই character নিলাম
            _perm_dups(prefix + ch, remaining - 1, freq, result)
            freq[ch] += 1                    # backtrack
```

Time: O(n! / (dup1! × dup2! × ...)) permutation × O(n) = unique permutation count × n · Space: O(n)

## Pattern চিনুন

> **"Duplicate সহ permutation, কিন্তু output unique" → Frequency map + backtracking।** একই character বারবার একই slot-এ না দেওয়াই duplicate বাদ দেওয়ার চাবি।

## Common mistake

- Sort করে "একই character পরপর skip" করার approach ভুল output দিতে পারে — frequency map বেশি নির্ভরযোগ্য।

## Follow-up

- **Combination (order মাটি না খেয়ে) duplicate ছাড়া?** → Sort + skip-duplicate backtracking।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-9"></a>
# 8.9 — Parens

> Pattern: **Backtracking / Build valid combinations** · Difficulty: **Medium** · খুব common

> **বইয়ের ভাষায়:** Implement an algorithm to print all valid combinations of n pairs of parentheses.
> Example: n=3 → `((()))`, `(()())`, `(())()`, `()(())`, `()()()`

## সমস্যাটা সহজ বাংলায়

n জোড়া parenthesis দিয়ে সব **valid** combination বের করতে হবে। Valid মানে — সব opening `(` ঠিকমতো closing `)` দিয়ে বন্ধ।

## Insight — কখন কোন bracket রাখা যাবে?

প্রতি step-এ দুটো choice: `(` রাখি বা `)` রাখি। কিন্তু সব সময় দুটোই রাখা যায় না:

```
'(' রাখতে পারব → যদি open count < n (এখনো opening bracket বাকি)
')' রাখতে পারব → যদি close count < open count (যত '(' আছে তার কম ')' হয়েছে)
```

এই নিয়ম মেনে চললেই সব combination valid হবে — কোনো extra validity check লাগবে না।

```dart
// Dart — Backtracking
List<String> generateParens(int n) {
  final result = <String>[];
  _parens('', 0, 0, n, result);
  return result;
}

void _parens(String current, int open, int close, int n, List<String> result) {
  if (current.length == 2 * n) {
    result.add(current);
    return;
  }
  if (open < n) {
    _parens(current + '(', open + 1, close, n, result);   // '(' রাখি
  }
  if (close < open) {
    _parens(current + ')', open, close + 1, n, result);   // ')' রাখি
  }
}
```

```python
# Python — Backtracking
def generate_parens(n: int) -> list:
    result = []
    _parens('', 0, 0, n, result)
    return result

def _parens(current: str, open: int, close: int, n: int, result: list) -> None:
    if len(current) == 2 * n:
        result.append(current)
        return
    if open < n:
        _parens(current + '(', open + 1, close, n, result)
    if close < open:
        _parens(current + ')', open, close + 1, n, result)
```

Call tree (n=2):

```
_parens('', 0, 0)
├── _parens('(', 1, 0)
│   ├── _parens('((', 2, 0)
│   │   └── _parens('(()', 2, 1)
│   │       └── _parens('(())', 2, 2)  → valid!
│   └── _parens('()', 1, 1)
│       └── _parens('()(', 2, 1)
│           └── _parens('()()', 2, 2)  → valid!
```

Time: O(n × Catalan(n)) — Catalan number = 1/(n+1) × C(2n,n) · Space: O(n)

## Pattern চিনুন

> **"Valid combination build করো" → Backtracking, কিন্তু invalid choice-এই prune করো — পরে check করো না।** এই "constraint check করতে করতে build করা" হলো clean backtracking।

## Common mistake

- সব combination বানিয়ে পরে valid কিনা check করা — O(2^2n × n) হয়, বেশি ধীর।
- `open < n` আর `close < open` condition উল্টো করা।

## Follow-up

- **Combinations count কতটা?** → Catalan number: C(n) = C(2n,n)/(n+1)।
- **Different bracket types `()`, `[]`, `{}`?** → একই backtracking, আরেকটু বেশি choice।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-10"></a>
# 8.10 — Paint Fill

> Pattern: **DFS / BFS / Flood Fill** · Difficulty: **Easy–Medium** · Common (image editing)

> **বইয়ের ভাষায়:** Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a 2D array of Colors), a point, and a new color, fill in the surrounding area until you hit a color border.

## সমস্যাটা সহজ বাংলায়

MS Paint-এর "bucket fill" টুল। একটা ঘর-এ click করলে তার চারপাশে (উপর, নিচ, বাঁয়ে, ডানে) যতটুকু **একই color** আছে সব নতুন color হয়ে যাবে।

## উদাহরণ

```
screen (G=Green, R=Red, B=Blue):
  G G G R R
  G G R R B
  G R R B B
  R R B B B

click (0,0) → new color = Yellow (Y):

  Y Y Y R R
  Y Y R R B
  Y R R B B
  R R B B B

(সব G → Y হয়েছে, R border-এ থামে)
```

## DFS দিয়ে ভাবা (Recursive Flood Fill)

```dart
// Dart — Recursive DFS flood fill
void paintFill(List<List<String>> screen, int r, int c, String newColor) {
  if (r < 0 || r >= screen.length || c < 0 || c >= screen[0].length) return;
  final oldColor = screen[r][c];
  if (oldColor == newColor) return;   // ইতিমধ্যে নতুন রঙ, loop এড়াতে
  _fill(screen, r, c, oldColor, newColor);
}

void _fill(List<List<String>> screen, int r, int c,
    String oldColor, String newColor) {
  if (r < 0 || r >= screen.length || c < 0 || c >= screen[0].length) return;
  if (screen[r][c] != oldColor) return;   // ভিন্ন color → থামো
  screen[r][c] = newColor;
  _fill(screen, r - 1, c, oldColor, newColor);   // উপর
  _fill(screen, r + 1, c, oldColor, newColor);   // নিচ
  _fill(screen, r, c - 1, oldColor, newColor);   // বাঁয়ে
  _fill(screen, r, c + 1, oldColor, newColor);   // ডানে
}
```

```python
# Python — Recursive DFS flood fill
def paint_fill(screen: list, r: int, c: int, new_color: str) -> None:
    old_color = screen[r][c]
    if old_color == new_color:
        return
    _fill(screen, r, c, old_color, new_color)

def _fill(screen: list, r: int, c: int, old_color: str, new_color: str) -> None:
    if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0]):
        return
    if screen[r][c] != old_color:
        return
    screen[r][c] = new_color
    _fill(screen, r-1, c, old_color, new_color)
    _fill(screen, r+1, c, old_color, new_color)
    _fill(screen, r, c-1, old_color, new_color)
    _fill(screen, r, c+1, old_color, new_color)
```

Time: O(r × c) · Space: O(r × c) stack (worst case সব fill)

## Pattern চিনুন

> **"Grid-এ সংযুক্ত এলাকা খোঁজা / fill করা" → DFS বা BFS।** BFS (queue) ব্যবহার করলে stack overflow এড়ানো যায় (বড় grid-এ)।

## Common mistake

- `oldColor == newColor` হলে return করতে ভুলে যাওয়া → infinite recursion।
- 8-দিক (diagonal) না 4-দিক — সাধারণত 4-দিক। Clarify করুন।

## Follow-up

- **BFS দিয়ে করো** (stack overflow এড়াতে) → queue ব্যবহার করুন, recursion বাদ।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-11"></a>
# 8.11 — Coins

> Pattern: **DP — Coin Change (Count of ways)** · Difficulty: **Medium** · খুব common

> **বইয়ের ভাষায়:** Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.

## সমস্যাটা সহজ বাংলায়

25, 10, 5, আর 1 পয়সার কয়েন দিয়ে n পয়সা **কতভাবে** বানানো যায়?

## উদাহরণ

```
n = 10:
  10              (একটা dime)
  5+5             (দুটো nickel)
  5+1+1+1+1+1    (nickel + ৫ penny)
  1+1+...+1      (10টা penny)
  মোট = 4 ways
```

## Brute Force Recursion

প্রতিটা denomination-এর জন্য: "কতটা নেব?" — 0 থেকে যত নেওয়া যায়।

```
makeChange(amount, coinIndex):
  if coinIndex is last (penny): 1 way (সব penny দিয়ে বানাও)
  ways = 0
  for k = 0, 1, 2, ... (যতটা এই coin নেওয়া যায়):
    ways += makeChange(amount - k × coins[coinIndex], coinIndex+1)
  return ways
```

Recursion Tree (n=10, coins=[25,10,5,1]):

```
makeChange(10, 0) [quarter]
└── makeChange(10, 1) [dime — 0 quarter]
    ├── makeChange(10, 2) [nickel — 0 dime]
    │   ├── makeChange(10, 3) [penny — 0 nickel] → 1 way
    │   ├── makeChange(5, 3)  [penny — 1 nickel] → 1 way
    │   └── makeChange(0, 3)  [penny — 2 nickel] → 1 way
    └── makeChange(0, 2) [nickel — 1 dime]
        └── makeChange(0, 3) → 1 way
```

Repeated subproblem (amount=5, coinIndex=2) → DP-র সুযোগ।

## Memoization

```dart
// Dart — Memoization
const List<int> coins = [25, 10, 5, 1];

int makeChange(int amount, int coinIndex, Map<String, int> memo) {
  if (coinIndex >= coins.length - 1) return 1;   // শুধু penny বাকি: ১ way
  final key = '$amount-$coinIndex';
  if (memo.containsKey(key)) return memo[key]!;
  int ways = 0;
  int amountLeft = amount;
  while (amountLeft >= 0) {
    ways += makeChange(amountLeft, coinIndex + 1, memo);
    amountLeft -= coins[coinIndex];
  }
  memo[key] = ways;
  return ways;
}

// call: makeChange(n, 0, {})
```

```python
# Python — Memoization
COINS = [25, 10, 5, 1]

def make_change(amount: int, coin_index: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if coin_index >= len(COINS) - 1:
        return 1   # শুধু penny বাকি
    key = (amount, coin_index)
    if key in memo:
        return memo[key]
    ways = 0
    amount_left = amount
    while amount_left >= 0:
        ways += make_change(amount_left, coin_index + 1, memo)
        amount_left -= COINS[coin_index]
    memo[key] = ways
    return ways
```

## Bottom-Up DP

```dart
// Dart — Bottom-Up 2D DP
int makeChangeDP(int n) {
  const List<int> coins = [1, 5, 10, 25];
  // dp[i][j] = j পয়সা বানানোর ways, শুধু প্রথম i+1 ধরনের coin ব্যবহার করে
  final dp = List.generate(coins.length, (_) => List<int>.filled(n + 1, 0));
  // 1 penny দিয়ে যেকোনো amount বানানোর ঠিক ১ way
  for (int j = 0; j <= n; j++) dp[0][j] = 1;
  for (int i = 1; i < coins.length; i++) {
    for (int j = 0; j <= n; j++) {
      // এই coin না নেওয়া: dp[i-1][j]
      // এই coin নেওয়া: dp[i][j - coins[i]] (যদি j >= coins[i])
      dp[i][j] = dp[i - 1][j] + (j >= coins[i] ? dp[i][j - coins[i]] : 0);
    }
  }
  return dp[coins.length - 1][n];
}
```

```python
# Python — Bottom-Up 2D DP
def make_change_dp(n: int) -> int:
    coins = [1, 5, 10, 25]
    dp = [[0] * (n + 1) for _ in range(len(coins))]
    for j in range(n + 1):
        dp[0][j] = 1    # 1 penny দিয়ে সব amount: ১ way
    for i in range(1, len(coins)):
        for j in range(n + 1):
            dp[i][j] = dp[i-1][j]
            if j >= coins[i]:
                dp[i][j] += dp[i][j - coins[i]]
    return dp[-1][n]
```

Recurrence: `dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]`
- প্রথম term: এই coin না নেওয়া (পুরোনো coins থেকে)
- দ্বিতীয় term: এই coin একটা নেওয়া (নেওয়ার পরেও এই coin আরো নেওয়া যায়, তাই `dp[i]` — `dp[i-1]` নয়)

Time: O(n × k) (k = coin types) · Space: O(n × k) — 1D array-তে নামানো যায় O(n)

## Complexity তুলনা

| Approach | Time | Space |
|---|---|---|
| Brute recursion | Exponential | O(n) |
| Memoization | O(n × k) | O(n × k) |
| Bottom-up DP | O(n × k) | O(n × k) বা O(n) |

## Pattern চিনুন

> **"কতভাবে amount বানানো যায়, unlimited coin" → Coin Change DP।** Recurrence: এই coin না নেওয়া + এই coin নেওয়া (নিজেই ব্যবহারযোগ্য থাকে)।

## Common mistake

- `dp[i][j - coin] = dp[i-1]` ব্যবহার করা — coin একটাই নেওয়া হয়, ভুল। `dp[i]` ব্যবহার করুন (unbounded knapsack)।
- Coin denomination গুলো ascending order-এ না দেওয়া।

## Follow-up

- **Minimum কতটা coin?** → অন্য DP: `min_coins[j] = 1 + min_coins[j - coin]`।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-12"></a>
# 8.12 — Eight Queens

> Pattern: **Backtracking** · Difficulty: **Hard** · মাঝে মাঝে আসে

> **বইয়ের ভাষায়:** Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them share the same row, column, or diagonal. "Printing" a solution means printing the location of the queen in each of the 8 rows.

## সমস্যাটা সহজ বাংলায়

8×8 দাবার বোর্ডে ৮টা Queen রাখতে হবে যাতে কোনো Queen আরেকটাকে "attack" করতে না পারে। Queen একই row, column, বা diagonal-এ থাকলে attack করে।

## মূল insight

প্রতিটা row-এ ঠিক একটাই Queen থাকবে (৮টা row, ৮টা Queen)। তাই row-by-row build করি — প্রতিটা row-এ কোন column-এ Queen রাখব সেটা বেছে নিই।

```
columns[row] = col   মানে row-তম row-এ col-তম column-এ Queen আছে

row 0: column 0 → try করি
row 1: column 0 → same column → skip
        column 1 → diagonal attack? (0,0)-(1,1) → same diagonal → skip
        column 2 → ok, try করি
...
```

## Attack check

```
(r1, c1) আর (r2, c2) conflict যদি:
  c1 == c2          (same column)
  |r1-r2| == |c1-c2|  (same diagonal)
(row always different কারণ row-by-row রাখছি)
```

```dart
// Dart — Eight Queens Backtracking
List<List<int>> eightQueens() {
  final results = <List<int>>[];
  final columns = List<int>.filled(8, -1);
  _placeQueens(0, columns, results);
  return results;
}

void _placeQueens(int row, List<int> columns, List<List<int>> results) {
  if (row == 8) {               // সব row fill হয়েছে → solution পেলাম
    results.add(List.from(columns));
    return;
  }
  for (int col = 0; col < 8; col++) {
    if (_isValid(columns, row, col)) {
      columns[row] = col;
      _placeQueens(row + 1, columns, results);
      columns[row] = -1;        // backtrack
    }
  }
}

bool _isValid(List<int> columns, int row, int col) {
  for (int r = 0; r < row; r++) {
    final c = columns[r];
    if (c == col) return false;                         // same column
    if ((row - r).abs() == (col - c).abs()) return false; // same diagonal
  }
  return true;
}
```

```python
# Python — Eight Queens Backtracking
def eight_queens() -> list:
    results = []
    _place_queens(0, [-1] * 8, results)
    return results

def _place_queens(row: int, columns: list, results: list) -> None:
    if row == 8:
        results.append(list(columns))
        return
    for col in range(8):
        if _is_valid(columns, row, col):
            columns[row] = col
            _place_queens(row + 1, columns, results)
            columns[row] = -1   # backtrack

def _is_valid(columns: list, row: int, col: int) -> bool:
    for r in range(row):
        c = columns[r]
        if c == col:
            return False
        if abs(row - r) == abs(col - c):
            return False
    return True
```

Time: O(8! / pruning) ≈ O(8!) in worst case, কিন্তু pruning-এর কারণে অনেক দ্রুত · Space: O(8) = O(1)

মোট solutions: **92টা।**

## Pattern চিনুন

> **"N-Queens / constraint satisfaction" → Backtracking, row-by-row।** Constraint check করতে করতে build করো, invalid হলে সাথে সাথে prune।

## Common mistake

- Diagonal check-এ `|row1-row2| == |col1-col2|` ভুলে যাওয়া।
- Backtrack না করা (columns[row] = -1 বাদ দেওয়া)।

## Follow-up

- **N-Queens generalize করো** → একই code, 8 → N।
- **শুধু একটা solution চাই** → প্রথম solution পেলে return করো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-13"></a>
# 8.13 — Stack of Boxes

> Pattern: **DP / Recursion with Memoization** · Difficulty: **Hard** · কম common

> **বইয়ের ভাষায়:** You have a stack of n boxes, with widths wi, depths di, and heights hi. The boxes cannot be rotated and can only be stacked on top of another box if each of the lower box's dimensions is strictly larger. Implement a method to compute the height of the tallest possible stack.

## সমস্যাটা সহজ বাংলায়

কিছু box আছে। একটার উপর আরেকটা রাখতে হলে নিচেরটার **width, depth, height** — তিনটাই উপরেরটার চেয়ে **strictly বড়** হতে হবে। সবচেয়ে **উঁচু stack** বানানো যায়?

## উদাহরণ

```
boxes:
  Box A: w=4, d=4, h=4
  Box B: w=3, d=3, h=3
  Box C: w=2, d=2, h=2
  Box D: w=5, d=5, h=5

valid stack: D → A → B → C  (height = 4+4+3+2 = 13)
```

## Approach: Recursion + Memoization

প্রতিটা box-কে stack-এর **bottom** হিসেবে ধরি। তারপর তার উপর কোন box রাখা যায় — সেগুলো দিয়ে recursively best stack বানাই।

1. Boxes sort করো (height descending) — এতে invalid choice দ্রুত prune হয়।
2. `tallestStack(boxes, bottomIndex, memo)` = boxes[bottomIndex]-কে bottom ধরে সর্বোচ্চ height।

```dart
// Dart — Stack of Boxes DP
class Box {
  final int w, d, h;
  Box(this.w, this.d, this.h);
  bool canBeAbove(Box other) => w < other.w && d < other.d && h < other.h;
}

int tallestStack(List<Box> boxes) {
  boxes.sort((a, b) => b.h.compareTo(a.h));   // height descending sort
  final memo = <int, int>{};
  int best = 0;
  for (int i = 0; i < boxes.length; i++) {
    final h = _tallest(boxes, i, memo);
    if (h > best) best = h;
  }
  return best;
}

int _tallest(List<Box> boxes, int bottomIdx, Map<int, int> memo) {
  if (memo.containsKey(bottomIdx)) return memo[bottomIdx]!;
  final bottom = boxes[bottomIdx];
  int best = 0;
  for (int i = bottomIdx + 1; i < boxes.length; i++) {
    if (boxes[i].canBeAbove(bottom)) {
      final h = _tallest(boxes, i, memo);
      if (h > best) best = h;
    }
  }
  best += bottom.h;
  memo[bottomIdx] = best;
  return best;
}
```

```python
# Python — Stack of Boxes DP
class Box:
    def __init__(self, w, d, h):
        self.w, self.d, self.h = w, d, h
    def can_be_above(self, other):
        return self.w < other.w and self.d < other.d and self.h < other.h

def tallest_stack(boxes: list) -> int:
    boxes.sort(key=lambda b: b.h, reverse=True)
    memo = {}
    best = 0
    for i in range(len(boxes)):
        h = _tallest(boxes, i, memo)
        best = max(best, h)
    return best

def _tallest(boxes: list, bottom_idx: int, memo: dict) -> int:
    if bottom_idx in memo:
        return memo[bottom_idx]
    bottom = boxes[bottom_idx]
    best = 0
    for i in range(bottom_idx + 1, len(boxes)):
        if boxes[i].can_be_above(bottom):
            h = _tallest(boxes, i, memo)
            best = max(best, h)
    best += bottom.h
    memo[bottom_idx] = best
    return best
```

Time: O(n²) with memoization · Space: O(n)

## Pattern চিনুন

> **"চেইন/stack বানানো, প্রতিটা পরের চেয়ে strictly ছোট/বড়" → "Longest Increasing Subsequence"-এর variant। Sort + DP।**

## Common mistake

- Rotation allow করা না করা clarify না করা (বইয়ে না বলা আছে)।
- তিনটা dimension-ই strictly greater চেক করতে ভুলে যাওয়া।

## Follow-up

- **শুধু height sort করলে কি যথেষ্ট?** না — width/depth-ও sort করতে হবে (বা সব dimension check করতে হবে)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q8-14"></a>
# 8.14 — Boolean Evaluation

> Pattern: **DP / Interval DP** · Difficulty: **Hard** · কম common কিন্তু গুরুত্বপূর্ণ

> **বইয়ের ভাষায়:** Given a boolean expression consisting of the symbols `0`, `1`, `&`, `|`, and `^`, and a desired result value `result`, implement a function to count the number of ways of parenthesizing the expression such that it evaluates to `result`.
> Example: `countEval("1^0|0|1", false)` = 2, `countEval("0&0&0&1^1|0", true)` = 10

## সমস্যাটা সহজ বাংলায়

একটা boolean expression দেওয়া (`0`, `1`, `&`, `|`, `^` দিয়ে)। বিভিন্নভাবে parenthesis বসিয়ে evaluate করা যায়। কতভাবে parenthesis বসালে expression টা `true` (বা `false`) হবে — সেই সংখ্যা বের করতে হবে।

## উদাহরণ

```
"1^0|0|1", result=false:

parenthesization 1: (1^0)|(0|1) = 1|1 = 1  (true  → not counted)
parenthesization 2: (1^(0|0))|1 = (1^0)|1 = 1|1 = 1  (true → not counted)
... কয়টা false দেয়? = 2
```

## Recursion + Memoization

**মূল ধারণা:** Expression-কে কোনো একটা operator-এ ভাগ করি। বাঁ দিক আর ডান দিক আলাদা আলাদা evaluate হতে পারে — তারপর operator apply হয়।

```
countEval(expr, result):
  প্রতিটা operator position k-এ ভাগ করি:
    left  = expr[0..k-1]
    op    = expr[k]
    right = expr[k+1..]
    
    leftTrue  = countEval(left, true)
    leftFalse = countEval(left, false)
    rightTrue = countEval(right, true)
    rightFalse= countEval(right, false)
    
    operator অনুযায়ী total + result-এ কতটা contribute করে হিসাব করি
```

Operator logic:

```
op = '&': true  only if both true → leftTrue × rightTrue
op = '|': false only if both false → leftFalse × rightFalse
op = '^': true  if different → leftTrue×rightFalse + leftFalse×rightTrue
```

```dart
// Dart — Boolean Evaluation with Memoization
int countEval(String expr, bool result) {
  final memo = <String, int>{};
  return _eval(expr, result, memo);
}

int _eval(String expr, bool result, Map<String, int> memo) {
  if (expr.isEmpty) return 0;
  if (expr.length == 1) {
    return _boolToInt(expr == '1') == _boolToInt(result) ? 1 : 0;
  }
  final key = '$expr-$result';
  if (memo.containsKey(key)) return memo[key]!;

  int ways = 0;
  for (int i = 1; i < expr.length; i += 2) {   // operator positions: 1, 3, 5...
    final op = expr[i];
    final left = expr.substring(0, i);
    final right = expr.substring(i + 1);
    final lt = _eval(left, true, memo);
    final lf = _eval(left, false, memo);
    final rt = _eval(right, true, memo);
    final rf = _eval(right, false, memo);
    final total = (lt + lf) * (rt + rf);
    int trueWays;
    if (op == '&') {
      trueWays = lt * rt;
    } else if (op == '|') {
      trueWays = lt * rt + lt * rf + lf * rt;
    } else {  // '^'
      trueWays = lt * rf + lf * rt;
    }
    ways += result ? trueWays : (total - trueWays);
  }
  memo[key] = ways;
  return ways;
}

int _boolToInt(bool b) => b ? 1 : 0;
```

```python
# Python — Boolean Evaluation with Memoization
def count_eval(expr: str, result: bool, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if not expr:
        return 0
    if len(expr) == 1:
        return 1 if (expr == '1') == result else 0
    key = (expr, result)
    if key in memo:
        return memo[key]
    ways = 0
    for i in range(1, len(expr), 2):   # operator positions: 1, 3, 5...
        op = expr[i]
        left, right = expr[:i], expr[i+1:]
        lt = count_eval(left, True, memo)
        lf = count_eval(left, False, memo)
        rt = count_eval(right, True, memo)
        rf = count_eval(right, False, memo)
        total = (lt + lf) * (rt + rf)
        if op == '&':
            true_ways = lt * rt
        elif op == '|':
            true_ways = lt * rt + lt * rf + lf * rt
        else:  # '^'
            true_ways = lt * rf + lf * rt
        ways += true_ways if result else (total - true_ways)
    memo[key] = ways
    return ways
```

Time: O(n³) — n/2 operators, প্রতিটা split O(n²) subproblem, memoization দিয়ে · Space: O(n²)

## Pattern চিনুন

> **"Expression-কে ভিন্নভাবে parenthesize করা" → Interval DP।** প্রতিটা operator-এ ভাগ করো, subexpression-এর result combine করো। Matrix Chain Multiplication, Optimal BST এই pattern।

## Common mistake

- Operator positions উল্টো করা — operator position i-তে, i সবসময় odd (1, 3, 5...)।
- `|` operator-এ trueWays calculation: `lt×rt + lt×rf + lf×rt` (শুধু উভয়ই false হলে false — বাকি সব true)।
- Memoization-এ result-সহ key রাখতে ভুলে যাওয়া।

## Follow-up

- **শুধু true/false জানতে হলে (count না)?** → Simpler recursion, memoization-ও দরকার কমে।
- **NOT operator `!` যোগ করলে?** → Unary operator, আলাদাভাবে handle করতে হবে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

## Chapter সারসংক্ষেপ

### সব প্রশ্নের একনজর

| # | প্রশ্ন | Technique | Time | Space |
|---|---|---|---|---|
| 8.1 | Triple Step | 1D DP (Fibonacci-style) | O(n) | O(n) বা O(1) |
| 8.2 | Robot in a Grid | 2D DFS + Memoization | O(r×c) | O(r×c) |
| 8.3 | Magic Index | Binary Search / Modified | O(log n) | O(log n) |
| 8.4 | Power Set | Recursion / Bit Mask | O(n×2^n) | O(n×2^n) |
| 8.5 | Recursive Multiply | Divide & Conquer | O(log b) | O(log b) |
| 8.6 | Towers of Hanoi | Classic Recursion | O(2^n) | O(n) |
| 8.7 | Permutations without Dups | Backtracking | O(n!×n) | O(n!×n) |
| 8.8 | Permutations with Dups | Backtracking + Freq Map | O(unique perms × n) | O(n) |
| 8.9 | Parens | Constrained Backtracking | O(n×Catalan(n)) | O(n) |
| 8.10 | Paint Fill | DFS / Flood Fill | O(r×c) | O(r×c) |
| 8.11 | Coins | DP (Unbounded Knapsack) | O(n×k) | O(n×k) |
| 8.12 | Eight Queens | Backtracking | O(8!) | O(8) |
| 8.13 | Stack of Boxes | DP (LIS-variant) | O(n²) | O(n) |
| 8.14 | Boolean Evaluation | Interval DP + Memoization | O(n³) | O(n²) |

---

### DP Problem চেনার Cheat Sheet

```
Signal যদি দেখো:                             Technique ভাবো:
------------------------------------------------------------------
"কতভাবে করা যায়" (count of ways)           1D বা 2D DP
"minimum/maximum" চাওয়া হচ্ছে              DP (optimal substructure)
"পারবে কিনা" (can you do X)               DP (boolean)
Recursion tree-এ subproblem repeat         Memoization দাও
Interval / expression-এ ভাগ করা           Interval DP
"সব combination/subset"                    Backtracking / Bit mask
"Grid-এ path"                              2D DP / BFS / DFS
"Stack / chain, strictly increasing"       LIS-variant DP
```

### Backtracking vs DP — পার্থক্য

```
Backtracking:
  - সব সম্ভাব্য solution চাই (যেমন সব permutation)
  - Invalid হলে ফিরে আসি (undo করি)
  - Memoization সাধারণত কাজ করে না (কারণ path গুরুত্বপূর্ণ)

DP:
  - Optimal / count চাই
  - Subproblem repeat হয়
  - Memoization করলে দ্রুত হয়
```

### এই Chapter-এর ৫টা সোনার নিয়ম

1. **Base case** সবার আগে লিখুন — না থাকলে stack overflow।
2. **Trust the recursion** — "ছোট সমস্যার উত্তর আমার function দেবে" বিশ্বাস করুন।
3. **Recursion tree আঁকুন** — repeated subproblem দেখলেই memoization।
4. **Brute force → Memoization → Bottom-up** — এই ক্রমে ভাবুন।
5. **Backtracking-এ backtrack করতে ভুলবেন না** — state undo না করলে ভুল result।

> **পরের ধাপ:** [Chapter 9 — System Design & Scalability](chapter09_system_design_scalability.md) — distributed systems, scaling strategies।
