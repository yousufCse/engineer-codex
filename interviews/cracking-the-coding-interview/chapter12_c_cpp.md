# Chapter 12 — C and C++ (প্রশ্ন 12.1 – 12.11)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। এই chapter-এর Code **C / C++** (concept বাংলায় বুঝিয়ে, দরকারে Dart/Python তুলনা)।
> এগুলো মূলত **knowledge/concept** প্রশ্ন — memory, pointer, OOP কীভাবে কাজ করে সেটা বোঝা জরুরি। তাই নিচের [Background](#bg) অংশটা আগে পড়ুন।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Testing](chapter11_testing.md) · [পরের: Java](chapter13_java.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
A. আগে Background (অবশ্যই পড়ুন): pointer, stack vs heap, malloc/free,
   C vs C++, OOP in C++ (virtual, vtable), reference vs pointer।
B. তারপর ১১টা প্রশ্ন:
   12.1   Last K Lines          — বড় file-এর শেষ K লাইন print
   12.2   Reverse String        — C-তে null-terminated string উল্টানো
   12.3   Hash Table vs STL Map  — দুটোর পার্থক্য
   12.4   Virtual Functions      — virtual function ভেতরে কীভাবে কাজ করে
   12.5   Shallow vs Deep Copy   — দুটোর পার্থক্য, কখন কোনটা
   12.6   Volatile               — volatile keyword কী করে
   12.7   Virtual Base Class     — virtual destructor কেন দরকার
   12.8   Copy Node              — pointer-যুক্ত structure deep copy
   12.9   Smart Pointer          — নিজে একটা smart pointer লেখা
   12.10  Align Malloc           — power-of-2 boundary-তে aligned malloc/free
   12.11  2D Alloc               — এক call/free দিয়ে 2D array
```

**প্রশ্নসমূহ:** [12.1 — Last K Lines](#q12-1) · [12.2 — Reverse String](#q12-2) · [12.3 — Hash Table vs STL Map](#q12-3) · [12.4 — Virtual Functions](#q12-4) · [12.5 — Shallow vs Deep Copy](#q12-5) · [12.6 — Volatile](#q12-6) · [12.7 — Virtual Base Class](#q12-7) · [12.8 — Copy Node](#q12-8) · [12.9 — Smart Pointer](#q12-9) · [12.10 — Align Malloc](#q12-10) · [12.11 — 2D Alloc](#q12-11)

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → মূল ধারণা (ASCII memory diagram) → ব্যাখ্যা/সমাধান → Code (C/C++) → Dart/Python তুলনা → Common mistake → Follow-up।**

---
---

<a id="bg"></a>
# Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

C/C++-এ যেসব প্রশ্ন আসে, সেগুলোর প্রায় সবগুলোই **memory নিজে manage করা** নিয়ে। Dart/Python-এ garbage collector নিজে memory পরিষ্কার করে দেয়, তাই আমরা pointer নিয়ে কম ভাবি। C/C++-এ আপনি নিজে memory চান (`malloc`/`new`), নিজে ফেরত দেন (`free`/`delete`) — ভুলে গেলে **memory leak**, দু'বার free করলে **crash**। এই দায়িত্বটাই C/C++ প্রশ্নের মূল।

## ১. Pointer আসলে কী?

Pointer হলো একটা variable যেটা অন্য কোনো জিনিসের **memory address** (ঠিকানা) ধরে রাখে। মান নয় — ঠিকানা।

```
int x = 42;        x আছে address 1000-এ
int* p = &x;       p ধরে রাখে 1000 (x-এর ঠিকানা)

         ┌─────────┐          ┌─────────┐
   p:    │  1000   │ ───────► │   42    │  : x
         └─────────┘          └─────────┘
       (address 2000)        (address 1000)

*p  →  42       (p যে address দেখাচ্ছে, সেখানকার মান — "dereference")
&x  →  1000     (x-এর ঠিকানা)
```

> Dart/Python-এ object variable আসলে গোপনে একটা reference (ঠিকানার মতো) ধরে রাখে — কিন্তু আপনি সেই address নিয়ে হিসাব করতে পারেন না, dereference operator নেই। C/C++-এ আপনি সরাসরি address নিয়ে কাজ করেন।

## ২. Stack vs Heap — দুই রকম memory

প্রোগ্রাম দুই জায়গায় memory পায়:

```
        ┌────────────────────────┐  উঁচু address
        │         STACK          │  ← function call, local variable
        │   (নিজে নিজে clean)     │     function শেষ = মুছে যায়, খুব দ্রুত
        │           │            │
        │           ▼            │
        │                        │
        │           ▲            │
        │           │            │
        │          HEAP          │  ← malloc/new দিয়ে চাওয়া memory
        │   (নিজে free করতে হবে)  │     আপনি free/delete না করলে থেকেই যায়
        └────────────────────────┘  নিচু address
```

- **Stack:** local variable, function-এর parameter। function থেকে বের হলেই **নিজে নিজে** মুছে যায়। দ্রুত, কিন্তু আকার ছোট ও fixed।
- **Heap:** `malloc`/`new` দিয়ে runtime-এ চাওয়া। যত খুশি বড়, কিন্তু **আপনাকে নিজে** `free`/`delete` করতে হবে। ভুলে গেলে **memory leak**।

```c
int* f() {
    int a = 5;              // stack — f() শেষ হলে a নাই
    int* b = malloc(4);     // heap — f() শেষেও থাকে; কে free করবে?
    return b;               // a-এর address ফেরত দিলে dangling হতো; b ঠিক আছে
}
```

## ৩. malloc/free আর new/delete

| | C | C++ |
|---|---|---|
| memory চাওয়া | `malloc(n)` (byte সংখ্যা) | `new T` / `new T[n]` |
| ফেরত দেওয়া | `free(p)` | `delete p` / `delete[] p` |
| constructor চলে? | না (শুধু raw bytes) | হ্যাঁ (`new` constructor ডাকে) |

> নিয়ম: যা `malloc` তা `free`; যা `new` তা `delete`; যা `new[]` তা `delete[]`। মিশিয়ে ফেললে undefined behavior।

## ৪. C vs C++ এক নজরে

- **C** — procedural, class নেই, OOP নেই। শুধু struct, function, pointer।
- **C++** — C-এর উপর class, inheritance, virtual function, template, STL (`vector`, `map`, `string`), constructor/destructor, reference, smart pointer যোগ করা।

## ৫. Reference vs Pointer (C++)

```cpp
int x = 10;
int* p = &x;     // pointer: নিজে একটা variable, NULL হতে পারে, পুনরায় অন্য কিছু দেখাতে পারে
int& r = x;      // reference: x-এর আরেক নাম (alias), NULL হয় না, একবার বাঁধলে আর বদলায় না

*p = 20;         // dereference লাগে
r  = 30;         // সরাসরি, x-ই বদলায়
```

> Reference = "ঠিকানার নিরাপদ, সহজ রূপ"। NULL হতে পারে না, dereference লাগে না।

## ৬. OOP in C++: virtual function ও vtable (পরের কয়েকটা প্রশ্নের ভিত্তি)

base class pointer দিয়ে derived object-এর সঠিক method ডাকতে হলে method-টা **`virtual`** হতে হয়। কীভাবে কাজ করে — সেটা [12.4](#q12-4)-এ বিস্তারিত, এখানে এক লাইনে: প্রতিটা polymorphic class-এর একটা **vtable** (function pointer-এর টেবিল) থাকে, object সেই টেবিলের দিকে একটা pointer (**vptr**) রাখে; runtime-এ ওই টেবিল দেখে ঠিক function বেছে নেয়।

> Dart/Python-এ **সব method by default virtual** (override করলেই dynamic dispatch হয়) — তাই ওই ভাষায় `virtual` keyword-ই নেই। C++-এ আপনাকে স্পষ্ট করে `virtual` লিখতে হয়।

---
---

<a id="q12-1"></a>
# 12.1 — Last K Lines

> Pattern/Topic: **File I/O · Circular Buffer** · Difficulty: **Easy–Medium** · মাঝারি common
> বইয়ের ভাষায়: Write a method to print the last K lines of an input file using C++.

## প্রশ্নটা সহজ বাংলায়
একটা text file-এর **শেষ K লাইন** print করতে হবে। ফাঁদটা হলো — file কত বড় তা আগে থেকে জানা নেই, হতে পারে gigabyte-এর; পুরোটা একসাথে memory-তে তোলা যাবে না।

## মূল ধারণা
পুরো file memory-তে তুলে শেষ K লাইন নেওয়া যায়, কিন্তু সেটা **O(file size)** memory খায় — বড় file-এ চলবে না। আমরা চাই শুধু **K লাইন** memory-তে রাখতে।

সমাধান: একটা **circular buffer** — K সাইজের একটা array, যেটা গোল করে ঘোরে। নতুন লাইন আসলে পুরোনো (K-এর বেশি আগের) লাইনের উপর লিখে ফেলে। file শেষ হলে buffer-এ ঠিক শেষ K লাইনই থাকে।

```
K = 3, একটা array[3], আর একটা index যেটা mod 3 করে ঘোরে:

লাইন পড়া হচ্ছে:  L1  L2  L3  L4  L5  (file শেষ)

array অবস্থা (index % 3 ঘরে লেখা):
 L1 আসে → [L1  -   - ]   pos 0
 L2 আসে → [L1  L2  - ]   pos 1
 L3 আসে → [L1  L2  L3]   pos 2
 L4 আসে → [L4  L2  L3]   pos 0  ← L1 overwrite (আর দরকার নেই)
 L5 আসে → [L4  L5  L3]   pos 1  ← L2 overwrite

শেষে buffer-এ আছে: L3, L4, L5  →  ঠিক শেষ ৩ লাইন
```

## ব্যাখ্যা / সমাধান
1. K-সাইজের একটা `string` array নিই।
2. file এক লাইন করে পড়ি (পুরোটা নয়), `lines[count % K]`-এ রাখি, `count` বাড়াই।
3. file শেষে দুটো case:
 - **মোট লাইন < K** হলে — `lines[0]` থেকে `count` পর্যন্ত print।
 - **নাহলে** — সবচেয়ে পুরোনো লাইন `count % K` index-এ; সেখান থেকে গোল করে K টা লাইন print।

মাত্র **একবার** file পড়ছি (single pass), memory লাগছে শুধু K লাইন।

## Code
```cpp
// C++ — circular buffer দিয়ে শেষ K লাইন
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void printLastKLines(const char* fileName, int K) {
    string* lines = new string[K];     // K-সাইজের circular buffer
    ifstream file(fileName);
    string line;
    int count = 0;

    while (getline(file, line)) {      // এক লাইন করে পড়ি (পুরো file নয়)
        lines[count % K] = line;       // গোল করে index, পুরোনোটা overwrite
        count++;
    }

    // কয়টা লাইন print করব, আর কোথা থেকে শুরু
    int start = count > K ? count % K : 0;
    int n     = count > K ? K : count;

    for (int i = 0; i < n; i++) {
        cout << lines[(start + i) % K] << endl;
    }
    delete[] lines;                    // heap memory ফেরত দিলাম (জরুরি)
}
```

## Dart/Python তুলনা
ধারণাটা ভাষা-নিরপেক্ষ; পার্থক্য শুধু memory নিজে free করতে হয় কিনা।

```python
# Python — collections.deque(maxlen=K) নিজেই circular buffer
from collections import deque

def print_last_k_lines(file_name: str, k: int) -> None:
    with open(file_name) as f:
        last = deque(f, maxlen=k)   # শুধু শেষ K লাইন রাখে, পুরোনো নিজে বাদ দেয়
    for line in last:
        print(line, end='')
```
> Python-এ `deque(maxlen=K)` ঠিক এই circular-buffer কাজটাই built-in করে দেয়, আর GC memory সামলায়। C++-এ আপনাকে নিজে `delete[]` করতে হয়।

## Common mistake
- পুরো file memory-তে তুলে fela (`vector<string>`-এ সব লাইন) — বড় file-এ memory blow up।
- circular index-এর off-by-one: মোট লাইন `< K` হলে `count % K` ভুল start দেয়; ওই case আলাদা handle করুন।
- `delete[] lines` ভুলে যাওয়া → memory leak।

## Follow-up
- **শেষ K byte?** — file-এর শেষে `seek` করে পিছন থেকে পড়ুন (line-নির্ভর নয়)।
- **খুব বড় K (memory-তে ধরে না)?** — তখন দুই pass: প্রথম pass-এ লাইন গুনুন, দ্বিতীয় pass-এ `count - K` লাইন skip করে বাকিটা print।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-2"></a>
# 12.2 — Reverse String

> Pattern/Topic: **Pointer · In-place two-pointer · C string** · Difficulty: **Easy** · খুব common (warm-up)
> বইয়ের ভাষায়: Implement a function `void reverse(char* str)` in C or C++ which reverses a null-terminated string.

## প্রশ্নটা সহজ বাংলায়
C-তে একটা string আসলে **char-এর array**, যার শেষে একটা বিশেষ চিহ্ন `'\0'` (null terminator) থাকে — এটাই বলে "string এখানে শেষ"। এই string-কে **জায়গায় বসেই (in-place)** উল্টে দিতে হবে।

## মূল ধারণা
```
"hello"  C-তে memory-তে:
 ┌───┬───┬───┬───┬───┬────┐
 │ h │ e │ l │ l │ o │ \0 │
 └───┴───┴───┴───┴───┴────┘
   0   1   2   3   4   5
                       ↑ null terminator — দৈর্ঘ্য এটাই বলে
```
দুটো pointer: একটা শুরুতে (`start`), একটা শেষ অক্ষরে (`end`)। দুটোর মান swap করি, তারপর `start` ডানে, `end` বামে — মাঝে মিলে গেলে থামি।

```
h e l l o          start→ h ... o ←end   swap →  o e l l h
  ↓ start, end এগোয়
o e l l h          start→ e l ←end       swap →  o l l e h
o l l e h          start, end মাঝে মিলল   →  শেষ: o l l e h
```

## ব্যাখ্যা / সমাধান
1. আগে string-এর শেষ খুঁজি (`'\0'` পর্যন্ত গিয়ে, `end` কে শেষ অক্ষরে রাখি)।
2. `start < end` যতক্ষণ — swap করি, দুজনকে কাছে আনি।
3. `'\0'` ছোঁব না — শুধু আসল অক্ষরগুলো উল্টাই।

## Code
```c
// C — null-terminated string in-place reverse
#include <stdio.h>

void reverse(char* str) {
    if (str == NULL) return;           // NULL guard

    char* end = str;
    while (*end) end++;                // '\0' পর্যন্ত গিয়ে শেষ খুঁজি
    end--;                             // শেষ আসল অক্ষরে নামি

    while (str < end) {                 // দুই pointer মাঝে মেলা পর্যন্ত
        char tmp = *str;               // swap *str ↔ *end
        *str = *end;
        *end = tmp;
        str++;                          // কাছে আনি
        end--;
    }
}
```

## Dart/Python তুলনা
Dart/Python-এ string **immutable** — তাই "in-place" সম্ভব নয়, নতুন string বানাতে হয়। C-তে char array পরিবর্তনযোগ্য বলেই in-place করা যায়।

```python
# Python — string immutable, তাই নতুন string ফেরত
def reverse(s: str) -> str:
    return s[::-1]          # slice দিয়ে উল্টানো (নতুন string)
```
```dart
// Dart — একইভাবে নতুন string
String reverse(String s) =>
    String.fromCharCodes(s.codeUnits.reversed);
```
> Python/Dart-এ null terminator নেই — দৈর্ঘ্য আলাদা করে রাখা থাকে। C-তে `'\0'` না থাকলে `while (*end)` কখনো থামবে না।

## Common mistake
- `end` কে `'\0'`-এর উপর রেখে দেওয়া (একবার `end--` করতে ভুলে যাওয়া) → null আর শেষ অক্ষর swap হয়ে string নষ্ট।
- NULL pointer চেক না করা → crash।
- `char str[]` literal পরিবর্তন করার চেষ্টা: `char* s = "hi";` read-only; পরিবর্তনযোগ্য চাইলে `char s[] = "hi";`।

## Follow-up
- **শব্দগুলো উল্টাও, অক্ষর নয়** (`"the cat"` → `"cat the"`) — পুরোটা reverse করে তারপর প্রতিটা word আবার reverse (CTCI 16-এর প্যাটার্ন)।
- **`strlen` ছাড়া করতে পারলে?** — উপরের code-ই `strlen` ব্যবহার করছে না, নিজে শেষ খুঁজছে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-3"></a>
# 12.3 — Hash Table vs STL Map

> Pattern/Topic: **Data structure trade-off** · Difficulty: **Easy (concept)** · common
> বইয়ের ভাষায়: Compare and contrast a hash table and an STL map. How is a hash table implemented? If the number of inputs is small, which data structure options can be used instead of a hash table?

## প্রশ্নটা সহজ বাংলায়
দুটো জিনিস তুলনা করতে হবে: **hash table** (যেমন `std::unordered_map`) আর **STL map** (`std::map`)। দুটোই key→value রাখে, কিন্তু ভেতরে আলাদা গঠন আর আলাদা পারফরম্যান্স।

## মূল ধারণা

**Hash table (`unordered_map`):** একটা hash function key-কে একটা bucket index-এ পাঠায়। গড়ে **O(1)** lookup/insert/delete। কিন্তু **কোনো order নেই** — key গুলো এলোমেলোভাবে ছড়ানো।

```
key "apple" ─hash()─► 3 ─► bucket[3]
key "banana"─hash()─► 7 ─► bucket[7]
            (collision হলে একই bucket-এ chain/linked list)

  bucket: [0][1][2][3:apple][4][5][6][7:banana]...
  খুঁজতে: hash করে সরাসরি bucket-এ যাই → গড়ে O(1)
```

**STL map (`std::map`):** ভেতরে একটা **balanced binary search tree** (সাধারণত red-black tree)। key **sorted** থাকে। সব operation **O(log n)**।

```
            [m]
           /   \
        [d]     [t]      ← key sorted order-এ রাখা
        /  \    /  \
     [b] [g] [p]  [z]
  খুঁজতে: tree-তে নামি → O(log n), কিন্তু in-order traversal = sorted
```

## ব্যাখ্যা / সমাধান — তুলনা টেবিল

| | `unordered_map` (hash table) | `std::map` (tree) |
|---|---|---|
| ভেতরে | hash table + buckets | balanced BST (red-black) |
| lookup/insert/delete | গড়ে **O(1)**, worst O(n) | সবসময় **O(log n)** |
| order | নেই (random) | **sorted by key** |
| key-তে দরকার | hash function + `==` | `<` (comparable) |
| range/sorted iteration | না | হ্যাঁ (সহজ) |
| memory | বেশি (buckets, খালি জায়গা) | কম, কিন্তু node-এ pointer overhead |

**Hash table কীভাবে implement হয়:** একটা array of buckets; key-কে hash করে index পাই; **collision** (দুই key একই index) হলে — সাধারণত ওই bucket-এ একটা **linked list (chaining)** রাখি, অথবা **open addressing** (পরের খালি ঘর খুঁজি)। load factor বেশি হলে array কে বড় করে rehash করি।

**input ছোট হলে বিকল্প:** খুব কম element হলে hash table-এর overhead অপ্রয়োজনীয়। তখন—
- একটা সাধারণ **array/`vector`** + linear search (O(n) কিন্তু n ছোট তাই দ্রুতই)।
- অথবা **`std::map`** (tree) — order বোনাস পাওয়া যায়, n ছোট হলে O(log n)-ও সস্তা।

## Dart/Python তুলনা
- **`unordered_map` ≈** Dart `HashMap` / Python `dict` (গড়ে O(1), order নেই — যদিও আধুনিক Python `dict` insertion-order রাখে, কিন্তু sorted নয়)।
- **`std::map` (sorted) এর সরাসরি equivalent Dart/Python core-এ নেই।** Python-এ `sortedcontainers.SortedDict`, Dart-এ `SplayTreeMap` (sorted, tree-based) দিয়ে মেলে।

```dart
// Dart — sorted, tree-based map (std::map-এর মতো)
import 'dart:collection';
final sorted = SplayTreeMap<String, int>();   // key sorted থাকবে
final fast   = HashMap<String, int>();          // hash, order নেই
```

## Common mistake
- "map = hash table" ধরে নেওয়া — C++-এ `std::map` কিন্তু **tree**, hash নয়; hash চাইলে `unordered_map`।
- hash table-এর worst case **O(n)** ভুলে যাওয়া (সব key একই bucket-এ collide করলে)।

## Follow-up
- **কখন `map` ভালো `unordered_map`-এর চেয়ে?** — যখন sorted order/range query দরকার, বা worst-case O(log n) guarantee চাই।
- **ভালো hash function-এর গুণ?** — দ্রুত, key গুলো সমানভাবে ছড়ায় (কম collision), deterministic।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-4"></a>
# 12.4 — Virtual Functions

> Pattern/Topic: **Polymorphism · vtable** · Difficulty: **Medium (concept)** · খুব common
> বইয়ের ভাষায়: How do virtual functions work in C++?

## প্রশ্নটা সহজ বাংলায়
C++-এ `virtual` keyword দিলে কী হয়, আর ভেতরে এটা **কীভাবে** কাজ করে — সেটা বোঝাতে হবে। মূল ব্যাপার: base class-এর pointer/reference দিয়ে ডাকলেও **আসল (derived) object-এর সঠিক method** চলে। একে বলে **dynamic dispatch** বা runtime polymorphism।

## মূল ধারণা — vtable আর vptr
```cpp
class Animal { public: virtual void speak(); };
class Dog : public Animal { public: void speak() override; };

Animal* a = new Dog();
a->speak();      // Dog::speak() চলবে (Animal::speak নয়) — কারণ virtual
```

প্রতিটা virtual-যুক্ত class-এর জন্য compiler একটা **vtable** (virtual table) বানায় — এটা সেই class-এর virtual function গুলোর **pointer-এর টেবিল**। প্রতিটা object-এর ভেতরে একটা গোপন pointer **vptr** থাকে, যেটা তার class-এর vtable-কে দেখায়।

```
Dog object:                vtable (Dog-এর)
 ┌──────────┐              ┌────────────────────┐
 │  vptr ───┼────────────► │ speak → Dog::speak │
 ├──────────┤              └────────────────────┘
 │  ...data │
 └──────────┘

a->speak() মানে:  a-এর vptr ধরো → vtable-এ speak slot দেখো →
                  সেখানে Dog::speak আছে → সেটাই ডাকো  (runtime-এ ঠিক হয়)
```

`virtual` **না** থাকলে compiler **compile time-এই** ঠিক করে ফেলে কোন function — pointer-এর declared type (`Animal`) দেখে `Animal::speak` ডাকবে, vtable লাগে না। একে বলে **static binding**।

## ব্যাখ্যা / সমাধান
1. class-এ অন্তত একটা `virtual` function থাকলে compiler ওই class-এর একটা vtable বানায়।
2. ওই class-এর প্রতিটা object-এ একটা vptr বসে (তাই object একটু বড় হয়, এক pointer পরিমাণ)।
3. virtual call হলে: object-এর vptr → vtable → ঠিক function-এর address → call। এই extra ধাপটুকুই virtual call-এর সামান্য খরচ।
4. derived class override করলে তার vtable-এর ওই slot-এ derived-এর function-এর address বসে।

## Code
```cpp
// C++ — virtual এর প্রভাব
#include <iostream>
using namespace std;

class Animal {
public:
    virtual void speak() { cout << "...\n"; }   // virtual = dynamic dispatch
    void name()          { cout << "Animal\n"; } // non-virtual = static binding
};
class Dog : public Animal {
public:
    void speak() override { cout << "Woof\n"; }
    void name()           { cout << "Dog\n"; }
};

int main() {
    Animal* a = new Dog();
    a->speak();   // "Woof"   — virtual, derived চলল
    a->name();    // "Animal" — non-virtual, declared type চলল
    delete a;
}
```

## Dart/Python তুলনা
Dart/Python-এ **সব method by default virtual** — override করলেই dynamic dispatch হয়, তাই `virtual` keyword-ই নেই।

```python
# Python — সব method এমনিতেই "virtual"
class Animal:
    def speak(self): print("...")
class Dog(Animal):
    def speak(self): print("Woof")

a: Animal = Dog()
a.speak()    # "Woof" — সবসময় আসল object-এর method চলে
```
> C++-এ performance-এর জন্য default static binding রাখা হয়েছে (vtable lookup এড়াতে); polymorphism চাইলে স্পষ্ট `virtual` লিখতে হয়। Dart/Python সবসময় dynamic, তাই আলাদা keyword লাগে না।

## Common mistake
- derived-এর behavior চাই কিন্তু base method-এ `virtual` দিতে ভুলে যাওয়া → base-এর version চলে যায় (silent bug)।
- vtable হলো **class-প্রতি একটা** (object-প্রতি নয়); object শুধু একটা **vptr** বহন করে — এই দুটো গুলিয়ে ফেলা।
- constructor-এর ভেতর থেকে virtual call করলে derived override **চলে না** (তখনো derived অংশ তৈরি হয়নি)।

## Follow-up
- **pure virtual function কী?** — `virtual void f() = 0;` মানে এই class **abstract**, object বানানো যায় না; derived-কে f() দিতেই হবে (interface-এর মতো)।
- **virtual call কি ধীর?** — সামান্য (এক pointer indirection); inline করা যায় না বলে hot loop-এ মাপা যায়, সাধারণত নগণ্য।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-5"></a>
# 12.5 — Shallow vs Deep Copy

> Pattern/Topic: **Memory · Pointer ownership** · Difficulty: **Easy–Medium (concept)** · common
> বইয়ের ভাষায়: What is the difference between deep copy and shallow copy? Explain how you would use each.

## প্রশ্নটা সহজ বাংলায়
একটা object কপি করার দুই অর্থ হতে পারে। **Shallow copy** শুধু উপরের মানগুলো (pointer-সহ) কপি করে — তাই দুই copy **একই** ভেতরের data-কে দেখায়। **Deep copy** ভেতরের data-রও **নতুন** কপি বানায় — দুই copy পুরোপুরি স্বাধীন।

## মূল ধারণা
```cpp
struct Node { int* data; };

Node original;  original.data → [42] (heap-এ)

// Shallow copy: শুধু pointer-এর মান কপি
Node shallow = original;
   original.data ─┐
                  ├──► [42]   ← দুজনেই একই heap-data দেখছে
   shallow.data  ─┘

// Deep copy: নতুন heap-data বানিয়ে মান কপি
   original.data ──► [42]
   deep.data     ──► [42]    ← আলাদা copy, স্বাধীন
```

**বিপদটা shallow copy-তে:** দুজনে একই memory share করছে। একজন `delete` করলে অন্যজনের pointer **dangling** (মুছে যাওয়া জায়গা দেখাচ্ছে) → পরে ব্যবহার করলে crash; আবার দুজনেই `delete` করলে **double free** → crash।

## ব্যাখ্যা / সমাধান — কখন কোনটা
- **Shallow copy** — যখন ভেতরের object আসলে **share** করতে চান (একই সম্পদ অনেকে ব্যবহার করবে), অথবা data নিতান্ত pointer নয় (শুধু value)। দ্রুত, কম memory। কিন্তু ownership স্পষ্ট রাখতে হবে (কে free করবে)।
- **Deep copy** — যখন দুই copy **স্বাধীন** চান; একটাকে বদলালে/মুছলে অন্যটায় প্রভাব পড়বে না। নিরাপদ, কিন্তু বেশি memory ও সময়।

## Code
```cpp
// C++ — shallow vs deep
#include <cstring>
struct Person {
    char* name;             // heap-এ string
    int   age;
};

// Shallow: pointer-ই কপি (একই name share করবে)
Person shallowCopy(const Person& p) {
    Person c;
    c.name = p.name;        // একই address — share!
    c.age  = p.age;
    return c;
}

// Deep: নতুন buffer বানিয়ে content কপি
Person deepCopy(const Person& p) {
    Person c;
    c.name = new char[strlen(p.name) + 1];   // নতুন memory
    strcpy(c.name, p.name);                   // content কপি
    c.age  = p.age;
    return c;                                 // free আলাদাভাবে করতে হবে
}
```
> C++-এ **copy constructor** আর **assignment operator** এই কাজটা নিয়ন্ত্রণ করে। default গুলো **shallow** (member-wise) করে — pointer member থাকলে নিজে deep copy লেখা লাগে (এটাই "Rule of Three/Five")।

## Dart/Python তুলনা
Dart/Python-এ assignment **সবসময় reference কপি** (একধরনের shallow) — দুটো variable একই object দেখায়। deep copy চাইলে স্পষ্ট করতে হয়।

```python
import copy
a = [[1, 2], [3]]
b = a                 # একই list (reference) — শুধু নাম আলাদা
c = copy.copy(a)      # shallow: বাইরের list নতুন, ভেতরের list গুলো share
d = copy.deepcopy(a)  # deep: পুরো independent copy
```
> মূল ধারণা একই; পার্থক্য — Dart/Python-এ GC থাকায় double-free/dangling-এর বিপদ নেই, তবু shallow-এ "একজন বদলালে অন্যজনে দেখা যায়" সমস্যাটা থেকেই যায়।

## Common mistake
- pointer member থাকা সত্ত্বেও default (shallow) copy constructor-এ নির্ভর করা → double free / dangling।
- "deep copy সবসময় ভালো" ভাবা — অপ্রয়োজনে বড় object deep copy করলে performance নষ্ট।

## Follow-up
- **Rule of Three কী?** — class-এ destructor, copy constructor, বা copy assignment-এর একটা লাগলে সাধারণত **তিনটাই** লাগে (manual resource managed বলে)।
- **circular reference থাকলে deep copy?** — সরল recursion infinite loop-এ পড়বে; visited map রেখে ঠিক করতে হয় (পরের প্রশ্ন 12.8 দেখুন)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-6"></a>
# 12.6 — Volatile

> Pattern/Topic: **Compiler · Memory semantics** · Difficulty: **Medium (concept)** · common
> বইয়ের ভাষায়: What is the significance of the keyword "volatile" in C?

## প্রশ্নটা সহজ বাংলায়
`volatile` compiler-কে বলে: "এই variable-এর মান **যেকোনো সময়, প্রোগ্রামের বাইরের কারণে** বদলে যেতে পারে — তাই তুমি optimize করে cache কোরো না, প্রতিবার মূল memory থেকে নতুন করে পড়ো।"

## মূল ধারণা
সাধারণত compiler গতি বাড়াতে variable-এর মান একবার register-এ তুলে রাখে, বারবার memory থেকে পড়ে না। কিন্তু কিছু variable-এর মান কোডের বাইরে থেকে বদলায় — hardware register, অন্য thread, interrupt handler, memory-mapped I/O। তখন cache করা মান **বাসি (stale)** হয়ে যায়।

```
volatile ছাড়া — compiler ভাবে মান বদলায় না, তাই একবার পড়ে register-এ রাখে:

  while (flag == 0) { }    // flag একবার পড়ে register-এ; loop কখনো থামবে না!
                           // অন্য thread/hardware flag=1 করলেও compiler দেখে না

volatile দিলে — প্রতিবার মূল memory থেকে পড়ে:

  volatile int flag;
  while (flag == 0) { }    // প্রতি iteration-এ memory থেকে নতুন করে পড়ে → থামতে পারে
```

## ব্যাখ্যা / সমাধান
`volatile` যা করে:
- প্রতিবার variable পড়ার সময় **মূল memory থেকে** পড়তে বাধ্য করে (register cache নয়)।
- variable-এর উপর compiler-এর **optimization বন্ধ** করে (read/write মুছে ফেলা বা পুনর্বিন্যাস করতে দেয় না)।

কখন লাগে:
- **Memory-mapped hardware register** (যার মান device বদলায়)।
- **Interrupt/signal handler**-এ পরিবর্তিত flag।
- **Multi-threaded** shared flag (তবে নিচের সতর্কতা দেখুন)।

> জরুরি সতর্কতা: `volatile` **thread-safety দেয় না**। এটা atomicity বা ordering guarantee করে না, শুধু "cache কোরো না"। আসল multithreading-এ `std::atomic`, mutex, বা memory barrier লাগে। অনেকে এই দুটো গুলিয়ে ফেলে — interview-তে এটা বললে আপনি এগিয়ে থাকবেন।

## Code
```c
// C — hardware/interrupt flag
volatile int sensor_ready = 0;   // interrupt এটা 1 করে দেয়

void wait_for_sensor(void) {
    while (sensor_ready == 0) {   // volatile বলে প্রতিবার memory থেকে পড়ে
        // busy wait
    }
    // sensor_ready volatile না হলে compiler এই loop কে চিরস্থায়ী করে দিতে পারত
}
```

## Dart/Python তুলনা
Dart/Python-এ **`volatile` নেই** এবং দরকারও নেই — এই ভাষাগুলো low-level register optimization এভাবে করে না, আর hardware register/interrupt সরাসরি ছোঁয় না। concurrency-তে Dart isolate **memory share করে না** (message passing); Python-এ GIL ও `threading`/`asyncio` primitives ব্যবহার হয়। অর্থাৎ `volatile`-এর সমস্যাটাই ওখানে ওঠে না।

## Common mistake
- `volatile` কে **thread synchronization** ভাবা — এটা mutex/atomic নয়, race condition ঠেকায় না।
- `const` আর `volatile`-কে বিপরীত ভাবা — একটা variable `const volatile` দুটোই হতে পারে (আপনি বদলাবেন না, কিন্তু বাইরে থেকে বদলায়, যেমন read-only hardware register)।

## Follow-up
- **`volatile` vs `std::atomic`?** — `atomic` atomicity + memory ordering দেয় (thread-safe); `volatile` শুধু optimization বন্ধ করে। Concurrency-তে `atomic` লাগে।
- **`const volatile int* p` মানে?** — p যে মান দেখায় তা আপনি বদলাতে পারবেন না, কিন্তু সেটা বাইরে থেকে বদলাতে পারে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-7"></a>
# 12.7 — Virtual Base Class (Virtual Destructor)

> Pattern/Topic: **Inheritance · Destructor · Polymorphism** · Difficulty: **Medium (concept)** · common
> বইয়ের ভাষায়: Why does a destructor in a base class need to be declared virtual?

## প্রশ্নটা সহজ বাংলায়
base class-এর pointer দিয়ে derived object `delete` করলে, base destructor `virtual` **না** হলে — শুধু base-এর অংশ মুছে যায়, derived-এর destructor **চলে না**। ফলে derived যে resource ধরেছিল (heap memory, file) সেগুলো **leak** হয়।

## মূল ধারণা
```cpp
class Base    { public:        ~Base()    { /* base cleanup */ } };
class Derived : public Base { int* buf; public: ~Derived() { delete[] buf; } };

Base* p = new Derived();   // base pointer, derived object
delete p;                  // কোন destructor চলবে?
```

```
~Base virtual নয়:
  delete p  →  শুধু ~Base() চলে  →  Derived::buf কখনো free হয় না  →  LEAK
                                     (~Derived চলেইনি)

~Base virtual:
  delete p  →  vtable দেখে ~Derived() চলে  →  তারপর ~Base()  →  সব clean
```

ঠিক virtual function-এর মতোই (12.4): destructor virtual হলে object-এর vtable দেখে **আসল (derived) destructor** আগে চলে, তারপর base destructor — উল্টো ক্রমে পুরো object পরিষ্কার হয়।

## ব্যাখ্যা / সমাধান
নিয়ম: **যে class-কে base হিসেবে (polymorphic-ভাবে) ব্যবহার করবেন এবং base pointer দিয়ে delete করবেন, তার destructor `virtual` করুন।** না করলে derived destructor skip হয় → undefined behavior / resource leak।

(নোট: "virtual base class" শব্দটা আরেকটা প্রসঙ্গেও আসে — diamond inheritance-এ duplicate base এড়াতে `virtual` inheritance, নিচের Follow-up দেখুন। CTCI-এর এই প্রশ্নটি মূলত **virtual destructor** নিয়ে।)

## Code
```cpp
// C++ — virtual destructor
#include <iostream>
using namespace std;

class Base {
public:
    virtual ~Base() { cout << "~Base\n"; }   // virtual — জরুরি
};
class Derived : public Base {
    int* buf;
public:
    Derived() : buf(new int[100]) {}
    ~Derived() override { delete[] buf; cout << "~Derived\n"; }
};

int main() {
    Base* p = new Derived();
    delete p;        // virtual বলে: "~Derived" তারপর "~Base" — সব clean
}                    // virtual না হলে শুধু "~Base", buf leak
```

## Dart/Python তুলনা
Dart/Python-এ **destructor নিজে ডাকতে হয় না** — garbage collector object আর কেউ ব্যবহার না করলে নিজে memory ফেরত দেয়। তাই এই "base destructor virtual করো" সমস্যাটাই নেই। (Python-এ `__del__` আছে কিন্তু কখন চলবে অনিশ্চিত; cleanup-এর জন্য `with`/context manager ব্যবহার করা হয়। Dart-এ `dispose()` প্যাটার্ন manual cleanup-এর জন্য।)

```python
# Python — cleanup-এর নিরাপদ উপায় destructor নয়, context manager
class File:
    def __enter__(self): ...
    def __exit__(self, *a): self.close()   # GC-র উপর নির্ভর না করে নিশ্চিত cleanup
```

## Common mistake
- polymorphic base class-এ virtual destructor দিতে ভুলে যাওয়া → derived resource leak (খুব common interview answer-এর পয়েন্ট)।
- **প্রতিটা** class-এ অপ্রয়োজনে virtual destructor দেওয়া — যে class base হিসেবে delete হবে না, তার vtable overhead অপ্রয়োজনীয়।

## Follow-up
- **Diamond problem ও "virtual base class" (virtual inheritance)** — `B` ও `C` দুজনেই `A` থেকে inherit, আর `D` দুজন থেকে; তাহলে `D`-তে `A`-এর **দুটো** copy চলে আসে। `class B : virtual public A` লিখলে `A`-এর **একটাই shared copy** থাকে। এটাই "virtual base class"-এর অন্য অর্থ।

```
       A                A (একটাই, virtual inheritance)
      / \              / \
     B   C    →       B   C
      \ /              \ /
       D                D   ← A duplicate হয় না
```

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-8"></a>
# 12.8 — Copy Node

> Pattern/Topic: **Deep copy · Graph/Pointer traversal · Hash map** · Difficulty: **Medium–Hard** · common
> বইয়ের ভাষায়: Write a method that takes a pointer to a `Node` structure as a parameter and returns a complete copy of the passed data structure. The `Node` data structure contains two pointers to other `Node`s.

## প্রশ্নটা সহজ বাংলায়
একটা `Node`-এর pointer দেওয়া; প্রতিটা Node-এর **দুটো pointer** আছে যেগুলো অন্য Node দেখায়। পুরো গঠনটার একটা **সম্পূর্ণ deep copy** বানাতে হবে — নতুন Node, নতুন pointer। ফাঁদ: গঠনটা গাছ নাও হতে পারে — **cycle** বা **shared node** থাকতে পারে (এটা আসলে একটা graph)।

## মূল ধারণা
যদি শুধু গাছ হতো, সরল recursion-ই যথেষ্ট। কিন্তু দুটো pointer থাকায় একই Node-এ একাধিক পথে পৌঁছানো যায় (shared), অথবা ঘুরে আবার আগের Node-এ ফেরা যায় (cycle)। সরল recursion তখন—
- একই Node **দুবার** কপি করে ফেলবে (shared হলে), অথবা
- cycle-এ **infinite loop**-এ পড়বে।

সমাধান: একটা **hash map** রাখি — "মূল Node → তার তৈরি copy"। কোনো Node-এ পৌঁছে আগে map-এ দেখি কপি আছে কিনা; থাকলে সেটাই ফেরত দিই (আবার বানাই না)।

```
original (cycle সহ):           map: original → copy
   A ──► B
   ▲     │
   └─────┘ (B → A ফিরে আসে)

copy A: map-এ নেই → নতুন A' বানাও, map[A]=A'
  copy B: নতুন B', map[B]=B'
    copy A আবার: map[A] পাওয়া গেল → A' ফেরত (আর recursion নয়) → cycle ঠিক
```

## ব্যাখ্যা / সমাধান
1. `node == NULL` হলে `NULL` ফেরত।
2. `node` map-এ থাকলে — তার copy ফেরত (পুনরায় বানিয়ো না)।
3. নতুন copy বানাই, **সাথে সাথে** map-এ রাখি (recursion-এর আগেই — নাহলে cycle-এ আবার বানাবে)।
4. দুই pointer-এর জন্য recursively copy বসাই।

## Code
```cpp
// C++ — দুই-pointer structure deep copy (cycle/shared safe)
#include <unordered_map>
using namespace std;

struct Node {
    int   value;
    Node* left;
    Node* right;
};

Node* copyNode(Node* node, unordered_map<Node*, Node*>& done) {
    if (node == nullptr) return nullptr;

    auto it = done.find(node);
    if (it != done.end()) return it->second;   // আগেই কপি হয়েছে → সেটাই দাও

    Node* copy = new Node{node->value, nullptr, nullptr};
    done[node] = copy;                          // recursion-এর আগেই map-এ রাখি

    copy->left  = copyNode(node->left, done);   // দুই pointer recursively
    copy->right = copyNode(node->right, done);
    return copy;
}

Node* copyNode(Node* node) {
    unordered_map<Node*, Node*> done;
    return copyNode(node, done);
}
```
- **Time: O(n)** (প্রতিটা node একবার) · **Space: O(n)** (map + recursion stack)।

## Dart/Python তুলনা
একই অ্যালগরিদম; map হিসেবে object-identity ব্যবহার করি।

```python
# Python — id() দিয়ে visited map
def copy_node(node, done=None):
    if done is None: done = {}
    if node is None: return None
    if id(node) in done: return done[id(node)]   # আগেই কপি
    copy = Node(node.value)
    done[id(node)] = copy                         # recursion-এর আগে রাখি
    copy.left  = copy_node(node.left,  done)
    copy.right = copy_node(node.right, done)
    return copy
```
> Python-এর `copy.deepcopy` ভেতরে ঠিক এই memo-dict কৌশলই ব্যবহার করে cycle handle করতে। C++-এ আপনাকে নিজে map রাখতে হয়, আর নতুন Node গুলো পরে `delete` করার দায়িত্বও আপনার।

## Common mistake
- map ছাড়া সরল recursion — cycle-এ infinite loop, shared node duplicate।
- copy বানিয়ে map-এ রাখার **আগেই** recursion করা → cycle-এ আবার একই node বানাবে (ক্রম গুরুত্বপূর্ণ: আগে map, পরে recurse)।
- copy-গুলো free করার পরিকল্পনা না রাখা (heap leak)।

## Follow-up
- **iterative version?** — BFS/DFS দিয়ে stack/queue + same map।
- **doubly/multi-pointer (n pointer)?** — একই কৌশল, প্রতিটা pointer-এর জন্য recurse।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-9"></a>
# 12.9 — Smart Pointer

> Pattern/Topic: **RAII · Reference counting · Operator overloading** · Difficulty: **Hard (concept+code)** · খুব common
> বইয়ের ভাষায়: Write a smart pointer class. A smart pointer is a data type, usually implemented with templates, that simulates a pointer while also providing automatic garbage collection. It automatically counts the number of references to a `SmartPointer<T*>` object and frees the object of type `T` when the reference count hits zero.

## প্রশ্নটা সহজ বাংলায়
একটা class বানাতে হবে যেটা সাধারণ pointer-এর মতো আচরণ করে, কিন্তু **নিজে নিজে memory free করে**। কৌশল: কয়জন এই object-কে দেখছে তার **count** রাখি (reference count)। নতুন কেউ দেখলে count বাড়ে, কেউ চলে গেলে কমে; count **শূন্য হলে** আসল object আর count দুটোই `delete` করি।

## মূল ধারণা — reference counting
```
SmartPointer<T> তিনজন share করছে:

  sp1 ─┐
  sp2 ─┼──► [ T object ]   refCount = 3
  sp3 ─┘         ▲
                 └── refCount আলাদা heap-এ, সবাই একই count share করে

sp3 scope ছাড়ল → refCount = 2
sp2 ছাড়ল       → refCount = 1
sp1 ছাড়ল       → refCount = 0  →  T object + count দুটোই delete
```

মূল বিষয়: **refCount নিজেও heap-এ, একটা pointer দিয়ে share করা** — তাই সব copy একই count দেখে। count আলাদা আলাদা হলে কাজ করবে না।

কোথায় count বাড়ে/কমে:
- **constructor** (নতুন object ধরল) → count = 1।
- **copy constructor / assignment** (আরেকজন একই object ধরল) → count++।
- **destructor** (একজন চলে গেল) → count--; শূন্য হলে delete।

## ব্যাখ্যা / সমাধান
তিনটা special function ঠিকঠাক লেখাই আসল (Rule of Three):
1. **Constructor** — object ও নতুন count(=1) ধরো।
2. **Copy constructor** — অন্যের object+count pointer কপি করো, count++।
3. **Assignment operator** — আগে নিজের পুরোনোটা release (count--, দরকারে delete), তারপর নতুনটা ধরো, count++। (self-assignment সাবধান।)
4. **Destructor** — count--; শূন্য হলে object ও count delete।
5. `*` ও `->` overload করে সাধারণ pointer-এর মতো ব্যবহার।

## Code
```cpp
// C++ — সরল reference-counted smart pointer
template <typename T>
class SmartPointer {
    T*   ref;        // আসল object
    int* refCount;   // shared count (heap-এ, তাই সব copy একই দেখে)

    void release() {                 // একজন কমল
        if (refCount && --(*refCount) == 0) {
            delete ref;              // শেষ জন গেল → object delete
            delete refCount;         // count-ও delete
        }
    }
public:
    SmartPointer(T* p) {             // 1. constructor
        ref = p;
        refCount = new int(1);       // প্রথম জন → count = 1
    }

    SmartPointer(const SmartPointer<T>& other) {   // 2. copy constructor
        ref = other.ref;
        refCount = other.refCount;
        ++(*refCount);               // আরেকজন ধরল
    }

    SmartPointer<T>& operator=(const SmartPointer<T>& other) {  // 3. assignment
        if (this == &other) return *this;   // self-assignment guard
        release();                            // নিজের পুরোনোটা ছাড়ো
        ref = other.ref;
        refCount = other.refCount;
        ++(*refCount);
        return *this;
    }

    ~SmartPointer() { release(); }   // 4. destructor

    T& operator*()  const { return *ref; }   // সাধারণ pointer-এর মতো ব্যবহার
    T* operator->() const { return ref; }
    int count()     const { return *refCount; }
};
```
ব্যবহার:
```cpp
SmartPointer<int> a(new int(42));   // count 1
{
    SmartPointer<int> b = a;        // count 2
}                                    // b গেল → count 1
                                     // a গেল (scope শেষে) → count 0 → delete
```

## Dart/Python তুলনা
Dart/Python-এ এটাই **ভাষার ভেতরে** আছে — সব object reference-counted/GC করা, নিজে count রাখতে হয় না। আসলে CPython-এর GC মূলত **reference counting** দিয়েই কাজ করে (plus cycle collector) — অর্থাৎ এই smart pointer যা করছে, CPython সব object-এর জন্য সেটাই করে।

```python
# Python — রেফারেন্স কাউন্ট নিজে দেখা যায়
import sys
x = [1, 2, 3]
y = x
print(sys.getrefcount(x))   # কয়টা reference (getrefcount নিজেও একটা ধরে)
```
> C++-এ বাস্তবে নিজে লিখতে হয় না — `std::shared_ptr<T>` ঠিক এই reference-counted কাজটাই করে; `std::unique_ptr<T>` single-owner; cycle ভাঙতে `std::weak_ptr`।

## Common mistake
- refCount কে object-এর ভেতরে value হিসেবে রাখা (share হয় না) — count আলাদা হয়ে যায়, কখনো 0-তে পৌঁছায় না বা আগেই delete হয়।
- **self-assignment** (`a = a`) handle না করা — release করে নিজের object মুছে ফেলে।
- assignment-এ আগের object release করতে ভুলে যাওয়া → leak।
- **circular reference** — দুটো smart pointer পরস্পরকে ধরলে count কখনো 0 হয় না → leak (এজন্যই `weak_ptr`)।

## Follow-up
- **thread-safe করতে?** — refCount বাড়ানো/কমানো **atomic** করতে হবে (`std::atomic<int>`), নাহলে race condition-এ count ভুল হয়ে double free/leak।
- **cycle leak ঠেকাতে?** — `weak_ptr`-এর মতো একটা version, যেটা count বাড়ায় না।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-10"></a>
# 12.10 — Align Malloc

> Pattern/Topic: **Memory alignment · Pointer arithmetic** · Difficulty: **Hard** · কম common কিন্তু classic
> বইয়ের ভাষায়: Write an aligned malloc and free function that supports allocating memory such that the memory address returned is divisible by a specific power of two. Example: `align_malloc(1000, 128)` returns a memory address that is a multiple of 128 and points to memory of size 1000 bytes. `aligned_free()` frees memory allocated by `align_malloc`.

## প্রশ্নটা সহজ বাংলায়
সাধারণ `malloc` যে address দেয় তা যেকোনো জায়গায় হতে পারে। আমাদের চাই এমন address যেটা **একটা নির্দিষ্ট power of 2** (যেমন 128) দিয়ে **নিঃশেষে ভাগ যায়** (aligned)। কিছু hardware/SIMD operation এমন aligned memory দাবি করে।

## মূল ধারণা — কেন বেশি allocate করি
`malloc` aligned address দেবে কিনা নিশ্চিত নয়। তাই আমরা **প্রয়োজনের চেয়ে বেশি** allocate করি, তারপর সেই বড় block-এর ভেতরে প্রথম aligned address-এ দিই। দুটো সমস্যা সমাধান করতে হয়:

1. **কত বেশি?** worst case-এ aligned point পেতে `(alignment - 1)` extra byte লাগে। আর `free`-এর জন্য আসল malloc-pointer মনে রাখতে আরও `sizeof(void*)` byte।
2. **free কীভাবে?** user-কে আমরা aligned pointer দিই, কিন্তু `free`-কে আসল malloc-pointer দিতে হবে। তাই aligned pointer-এর **ঠিক আগে** আসল pointer-টা লুকিয়ে রাখি।

```
malloc যা দিল (raw):
 ┌──────────────────────────────────────────────┐
 │   ...   [আসল ptr সংরক্ষণ]  [user-এর aligned মেমরি] │
 └──────────────────────────────────────────────┘
              ▲                ▲
        p2-এর ঠিক আগে        p2 (aligned, user-কে এটাই দিই)
        এখানে raw ptr রাখি

free-তে: p2-এর ঠিক আগে গিয়ে raw ptr পড়ি → সেটাই free করি
```

aligned address বের করার trick: `aligned = (raw + alignment - 1) & ~(alignment - 1)` — এটা raw-কে উপরের দিকে নিকটতম alignment-এর গুণিতকে নিয়ে যায় (power of 2 বলে bitmask কাজ করে)।

## ব্যাখ্যা / সমাধান
1. `malloc(required + alignment - 1 + sizeof(void*))` — যথেষ্ট বড় block।
2. raw pointer-এর পরে অন্তত `sizeof(void*)` জায়গা ছেড়ে, পরের aligned address বের করি।
3. সেই aligned address-এর ঠিক আগে raw pointer store করি।
4. user-কে aligned address দিই।
5. `free`-এ: aligned address-এর আগে থেকে raw pointer পড়ি, সেটা `free`।

## Code
```c
// C — aligned malloc / free
#include <stdlib.h>
#include <stdint.h>

void* aligned_malloc(size_t required_bytes, size_t alignment) {
    // alignment power of 2 ধরা; extra: align পেতে (alignment-1), raw ptr রাখতে sizeof(void*)
    size_t offset = alignment - 1 + sizeof(void*);
    void* raw = malloc(required_bytes + offset);
    if (raw == NULL) return NULL;

    // raw-এর পরে sizeof(void*) ছেড়ে পরের aligned address
    uintptr_t p = (uintptr_t)raw + sizeof(void*);
    uintptr_t aligned = (p + (alignment - 1)) & ~(uintptr_t)(alignment - 1);

    // aligned-এর ঠিক আগে raw pointer লুকিয়ে রাখি (free-এর জন্য)
    ((void**)aligned)[-1] = raw;

    return (void*)aligned;
}

void aligned_free(void* aligned_ptr) {
    if (aligned_ptr == NULL) return;
    void* raw = ((void**)aligned_ptr)[-1];   // আগে লুকানো raw ptr পড়ি
    free(raw);                                // আসলটাই free করি
}
```
যাচাই: `(uintptr_t)aligned % alignment == 0` সবসময় সত্য, কারণ bitmask নিচের bit গুলো মুছে দিয়েছে।

## Dart/Python তুলনা
Dart/Python-এ **সরাসরি memory address/alignment নিয়ন্ত্রণ নেই** — runtime ও GC নিজে allocation করে, আপনি raw pointer পান না। তাই এই কাজ ওই ভাষায় সাধারণত করা যায় না/দরকার হয় না। (নিচু স্তরের aligned buffer চাইলে FFI দিয়ে C-র `malloc`/aligned-alloc ডাকতে হয়।)

## Common mistake
- raw pointer free-এর জন্য store না করা — `free(aligned_ptr)` দিলে crash (aligned pointer malloc-এর দেওয়া নয়)।
- extra জায়গায় `sizeof(void*)` যোগ করতে ভুলে যাওয়া → raw store করার জায়গা থাকে না।
- alignment power-of-2 না হলে bitmask trick ভেঙে যায় (ধরে নেওয়া হয় power of 2)।

## Follow-up
- **alignment power of 2 না হলে?** — bitmask চলবে না; modulo দিয়ে round-up করতে হবে।
- **standard উপায়?** — C11-এ `aligned_alloc(alignment, size)`, POSIX-এ `posix_memalign` — এগুলো built-in (এই হাতে-লেখা version বুঝতে চাওয়া হয় ভেতরের mechanism জানার জন্য)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q12-11"></a>
# 12.11 — 2D Alloc

> Pattern/Topic: **Memory layout · Pointer-to-pointer · Single allocation** · Difficulty: **Medium–Hard** · classic
> বইয়ের ভাষায়: Write a function in C called `my2DAlloc` which allocates a two-dimensional array. Minimize the number of calls to malloc and make sure that the memory is accessible by the notation `arr[i][j]`.

## প্রশ্নটা সহজ বাংলায়
একটা 2D array (`arr[i][j]`-এভাবে ব্যবহার করা যায়) বানাতে হবে, কিন্তু **`malloc`-এর সংখ্যা যত কম সম্ভব** — আদর্শভাবে **একটাই** `malloc`, আর একটাই `free`। সাধারণ পদ্ধতিতে প্রতিটা row-এর জন্য আলাদা malloc লাগে (rows+1 বার), সেটা এড়াতে হবে।

## মূল ধারণা
সাধারণ (naive) উপায়: একটা `int**` (row pointer-এর array), তারপর প্রতিটা row আলাদা malloc — মোট **rows + 1** বার malloc, free-ও তত বার। সমস্যা: free করা ঝামেলা, memory ছড়ানো।

**একটাই-malloc কৌশল:** একটানা একটা block নিই যার **প্রথম অংশে row pointer-গুলো**, আর **পরের অংশে আসল int data** — দুটো একসাথে। তারপর row pointer-গুলোকে data-অংশের সঠিক জায়গায় তাক করাই। তাহলে `arr[i][j]` কাজ করে, কিন্তু malloc মাত্র একবার, free-ও একবার।

```
এক block (malloc একবার):
 ┌──────────────────────────┬───────────────────────────────────┐
 │  row pointers (rows টা)   │      আসল int data (rows×cols)       │
 └──────────────────────────┴───────────────────────────────────┘
     arr[0] ─┐                ▲
     arr[1] ─┼────────────────┘ (প্রতিটা pointer তার row-এর শুরুতে তাক করে)
     arr[2] ─┘

arr[i] = data + i*cols   →  arr[i][j] ঠিক জায়গায় পৌঁছায়
free(arr) একবারেই পুরো block ফেরত দেয়
```

## ব্যাখ্যা / সমাধান
1. মোট লাগবে: `rows * sizeof(int*)` (pointer অংশ) + `rows * cols * sizeof(int)` (data অংশ)। একবার malloc।
2. block-এর শুরুটা `int**` (pointer array)।
3. data অংশের শুরু = pointer অংশের ঠিক পরে।
4. প্রতিটা `arr[i]` কে `data + i*cols`-এ তাক করাই।
5. ফেরত দিই `arr`; free-এ শুধু `free(arr)` — পুরো block একসাথে।

## Code
```c
// C — একটাই malloc-এ 2D array, arr[i][j] ব্যবহারযোগ্য
#include <stdlib.h>

int** my2DAlloc(int rows, int cols) {
    int header  = rows * sizeof(int*);      // pointer অংশের আকার
    int data    = rows * cols * sizeof(int); // data অংশের আকার
    int** arr   = (int**)malloc(header + data);  // একবারই malloc
    if (arr == NULL) return NULL;

    // data অংশের শুরু = pointer অংশের ঠিক পরে
    int* buf = (int*)(arr + rows);

    for (int i = 0; i < rows; i++) {
        arr[i] = buf + i * cols;            // প্রতি row তার অংশে তাক করে
    }
    return arr;                              // arr[i][j] এখন কাজ করে
}

void my2DFree(int** arr) {
    free(arr);                               // একবারেই পুরো block free
}
```
ব্যবহার:
```c
int** m = my2DAlloc(3, 4);
m[1][2] = 99;          // স্বাভাবিক 2D indexing
my2DFree(m);           // একটাই free
```

## Dart/Python তুলনা
Dart/Python-এ এই pointer-গণিত করতে হয় না — list-of-lists/nested array নিজে memory সামলায়, free-ও নেই।

```python
# Python — list comprehension; memory নিজে GC সামলায়
def my_2d_alloc(rows, cols):
    return [[0] * cols for _ in range(rows)]   # arr[i][j] স্বাভাবিক
```
```dart
// Dart — nested List
List<List<int>> my2DAlloc(int rows, int cols) =>
    List.generate(rows, (_) => List.filled(cols, 0));
```
> Python list-of-lists ভেতরে আসলে আলাদা আলাদা list object (C-র naive `int**`-এর কাছাকাছি, contiguous নয়)। C-র এই single-block কৌশলের সুবিধা: contiguous memory (cache-friendly) + একটাই malloc/free। সত্যিকারের contiguous 2D চাইলে Python-এ NumPy array।

## Common mistake
- data অংশের শুরু হিসাব করতে `arr + rows` (pointer arithmetic) আর byte-offset গুলিয়ে ফেলা — `arr + rows` ঠিকই `rows` টা `int*` পরে নিয়ে যায়।
- naive পদ্ধতিতে row আলাদা malloc করে free-এ শুধু `free(arr)` দেওয়া → row গুলো leak (naive-এ প্রতিটা row আলাদা free লাগে)।
- pointer ও data অংশের alignment নিয়ে assumption (সাধারণ int-এ ঠিক, mixed type হলে সতর্ক)।

## Follow-up
- **3D array?** — একই ধারণা স্তরে স্তরে: pointer-to-pointer অংশ, তারপর pointer অংশ, তারপর data — সব এক block-এ।
- **naive বনাম এটা — সুবিধা?** — এটা: কম malloc/free, contiguous (cache locality ভালো)। naive: row-গুলো ভিন্ন আকারের (jagged) হতে পারে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 12 — সারসংক্ষেপ ও Concept Cheat Sheet

| # | প্রশ্ন | মূল ধারণা | মনে রাখার এক কথা |
|---|---|---|---|
| 12.1 | Last K Lines | Circular buffer + single file pass | K লাইন রাখো, পুরো file নয় |
| 12.2 | Reverse String | Two-pointer in-place, null terminator | `'\0'` ছুঁয়ো না, শেষ অক্ষর থেকে শুরু |
| 12.3 | Hash Table vs STL Map | `unordered_map`=hash O(1) random; `map`=tree O(log n) sorted | order চাই = map, গতি চাই = unordered_map |
| 12.4 | Virtual Functions | vtable + vptr দিয়ে runtime dispatch | virtual = derived method চলে |
| 12.5 | Shallow vs Deep Copy | shallow=pointer share; deep=নতুন copy | pointer member থাকলে deep লাগে |
| 12.6 | Volatile | "cache কোরো না, প্রতিবার memory থেকে পড়ো" | thread-safety দেয় না |
| 12.7 | Virtual Destructor | base destructor virtual না হলে derived leak | polymorphic base = virtual ~ |
| 12.8 | Copy Node | hash map(orig→copy) দিয়ে cycle-safe deep copy | recurse-এর আগে map-এ রাখো |
| 12.9 | Smart Pointer | shared refCount, 0 হলে delete | self-assign + cycle সাবধান |
| 12.10 | Align Malloc | বেশি malloc + bitmask round-up + raw ptr লুকাও | free-এ raw ptr উদ্ধার করো |
| 12.11 | 2D Alloc | এক block: pointer অংশ + data অংশ | malloc/free একবারই |

### "এটা শুনলে → এটা ভাবো" (concept signal → answer)
```
"কীভাবে কাজ করে" virtual              →  vtable + vptr, runtime dispatch
base pointer দিয়ে delete              →  virtual destructor নইলে leak
pointer member কপি                    →  default shallow, নিজে deep লেখো (Rule of Three)
বাইরে থেকে মান বদলায় (hardware/intr)  →  volatile (কিন্তু thread-safe নয়)
নিজে memory free হোক                  →  reference-counted smart pointer / shared_ptr
cycle/shared যুক্ত গঠন কপি            →  visited hash map
aligned address চাই                   →  বেশি malloc + bitmask + raw ptr লুকাও
কম malloc-এ 2D array                  →  pointer অংশ + data অংশ এক block
বড় file-এর শেষাংশ                     →  circular buffer / seek
```

### এই chapter-এর সোনার নিয়ম
1. **Memory আপনার দায়িত্ব** — যা `new`/`malloc` তা `delete`/`free`; পরিকল্পনা ছাড়া allocate কোরো না।
2. **Virtual** = runtime polymorphism (vtable); polymorphic base class-এ destructor virtual করুন।
3. **pointer member = deep copy ভাবুন** (Rule of Three/Five), নইলে double-free/dangling।
4. **`volatile` ≠ thread-safe** — শুধু compiler optimization বন্ধ করে; concurrency-তে `atomic`/mutex লাগে।
5. **Reference counting** (smart pointer/`shared_ptr`) auto-cleanup দেয়, কিন্তু **cycle leak করে** — তখন `weak_ptr`।
6. Dart/Python-এ GC এসব সামলায় বলে অনেক সমস্যা ওঠে না — কিন্তু shallow/deep, polymorphism-এর ধারণা সেখানেও খাটে।

> **পরের ধাপ:** [Chapter 13 — Java](chapter13_java.md) (13.1–13.8), যেখানে Java-র constructor, generics, reflection, lambda ইত্যাদি knowledge প্রশ্ন শিখব।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>
