
claude --resume abbeebc0-c14d-4e25-a217-43bcb48442f4

# Section 11 — Data Structures & Algorithms

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. (DSA matters most for remote/international interviews.)

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a detailed, step-by-step explanation with real-life examples and code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For DSA, always say the **idea and the Big-O first**, then write code. Talk out loud as you go — interviewers grade your thinking, not just the final code.

---

<a id="toc"></a>

## Table of Contents

**A. Complexity (Big-O)**
1. [Big-O notation — time complexity](#q1) · *Very common*
2. [Space complexity](#q2) · *Common*

**B. Linear structures**
3. [Arrays / Lists — how they work, complexity](#q3) · *Very common*
4. [Linked List — vs array, trade-offs](#q4) · *Common*
5. [Stack — LIFO](#q5) · *Very common*
6. [Queue — FIFO (and Deque)](#q6) · *Common*

**C. Hash-based structures**
7. [Map / HashMap — internals & collisions](#q7) · *Very common*
8. [Set — and when to use it](#q8) · *Common*

**D. Trees & graphs**
9. [Binary Tree — BFS vs DFS](#q9) · *Very common*
10. [Graphs — representation, BFS & DFS](#q10) · *Common*

**E. Searching & sorting**
11. [Binary Search](#q11) · *Very common*
12. [Sorting — Bubble, Insertion, Merge, Quick](#q12) · *Very common*

**F. Core techniques**
13. [Two Pointers](#q13) · *Common*
14. [Sliding Window](#q14) · *Common*
15. [Recursion — base case, call stack, tail recursion](#q15) · *Very common*
16. [Dynamic Programming — memoization vs tabulation](#q16) · *Common*

**G. Common coding problems (Dart)**
17. [Reverse a string](#q17) · *Common*
18. [Check a palindrome](#q18) · *Common*
19. [Find duplicates in a list](#q19) · *Common*
20. [FizzBuzz](#q20) · *Common*
21. [Fibonacci — iterative, recursive, memoized](#q21) · *Very common*
22. [Two Sum](#q22) · *Very common*
23. [Max in a list without `max()`](#q23) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need all 23 at once. Follow these stages in order. Tick a stage off only when you can give the **short answer** and write the code without looking.

**Stage 1 — The language of DSA (start here).** Everything is measured in this.
→ [Q1 Big-O](#q1) · [Q2 Space complexity](#q2)

**Stage 2 — The everyday structures.**
→ [Q3 Lists](#q3) · [Q7 Maps](#q7) · [Q5 Stack](#q5) · [Q6 Queue](#q6) · [Q8 Set](#q8)

**Stage 3 — The classic algorithms.**
→ [Q11 Binary search](#q11) · [Q12 Sorting](#q12) · [Q15 Recursion](#q15)

**Stage 4 — Patterns that solve most interview questions.**
→ [Q13 Two pointers](#q13) · [Q14 Sliding window](#q14) · [Q16 Dynamic programming](#q16) · [Q22 Two Sum](#q22)

**Stage 5 — Trees, graphs & the rest.**
→ [Q4 Linked list](#q4) · [Q9 Binary tree](#q9) · [Q10 Graphs](#q10) · [Q17](#q17)–[Q21](#q21), [Q23](#q23)

**Short on time (1 hour before the interview)?** Review these eight:
[Q1](#q1) · [Q3](#q3) · [Q7](#q7) · [Q11](#q11) · [Q12](#q12) · [Q13](#q13) · [Q15](#q15) · [Q22](#q22), then read the [Cheat Sheet](#cheatsheet).

---

# A. Complexity (Big-O)

---

<a id="q1"></a>
## 1. What is Big-O notation and why does it matter?

> Very common · Easy–Medium

**Short answer (say this):**
"Big-O describes how the work an algorithm does grows as the input grows. It ignores small details and machine speed, and focuses on the shape of the growth. We use it to compare two solutions before we even run them — for example, O(log n) is far better than O(n) for large inputs."

**Let's understand it fully:**

**Step 1 — A real-life picture: cooking for guests.**
Imagine a recipe. Big-O asks: "if the number of guests doubles, how much more work is it?"
- If you greet each guest once → work doubles when guests double. That is **O(n)**.
- If you turn on one oven no matter how many guests → work stays the same. That is **O(1)**.
- If every guest shakes hands with every other guest → work grows much faster. That is **O(n²)**.

**Step 2 — The common growth rates, slowest-growing first.**

| Big-O | Name | Example |
|---|---|---|
| O(1) | constant | read `list[5]`, add to a Map |
| O(log n) | logarithmic | binary search |
| O(n) | linear | loop through a list once |
| O(n log n) | linearithmic | good sorting (merge, quick) |
| O(n²) | quadratic | nested loop over the same list |
| O(2ⁿ) | exponential | naive recursive Fibonacci |

**Step 3 — How to read code and find its Big-O.**
Count how many times the work runs as `n` grows.

```dart
// O(1) — one step, no matter the size
int first(List<int> a) => a[0];

// O(n) — one loop over n items
int sum(List<int> a) {
  var total = 0;
  for (final x in a) total += x; // runs n times
  return total;
}

// O(n^2) — a loop inside a loop, both over n
void printPairs(List<int> a) {
  for (final x in a) {        // n times
    for (final y in a) {      // n times each
      print('$x,$y');         // n * n = n^2
    }
  }
}
```

**Step 4 — Two rules that simplify Big-O.**
1. **Drop constants:** O(2n) becomes O(n). We care about the shape, not the exact count.
2. **Keep the biggest term:** O(n² + n) becomes O(n²). For large n, the biggest term dominates.

**Step 5 — Why "log n" is so good.**
`log n` means "how many times can you cut n in half until you reach 1?" For a list of 1,000,000 items, that is only about 20 steps. That is why binary search feels almost instant.

**Why interviewers ask:** Big-O is the shared language of all algorithm questions. They want to know you can compare solutions and pick the efficient one.

**Common mistake:** Counting the exact number of operations instead of the growth shape (saying "O(2n+3)"). Just say O(n). Another mistake: ignoring the worst case.

**Follow-ups they may ask:**
- *"Best, average, worst case?"* → Best = luckiest input, worst = hardest input, average = typical. Interviews usually care about **worst case**.
- *"What is amortized time?"* → The average cost per operation over many operations. Adding to a dynamic list is amortized O(1) even though one resize is O(n) (see [Q3](#q3)).

**Related:** [Q2 — space complexity](#q2) · [Q11 — binary search (log n)](#q11) · [Q12 — sorting (n log n)](#q12)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is space complexity, and how is it different from time complexity?

> Common · Easy–Medium

**Short answer (say this):**
"Time complexity measures how the running time grows; space complexity measures how the extra memory grows as the input grows. We count the extra memory the algorithm creates, not the input itself. The call stack in recursion counts too — a recursion n levels deep uses O(n) space."

**Let's understand it fully:**

**Step 1 — The simple difference.**
- **Time** = how many steps as input grows.
- **Space** = how much extra memory as input grows.

**Step 2 — Count EXTRA memory, not the input.**
If a function takes a list of n items, that list is the input — we don't count it. We count what the function *creates*.

```dart
// O(1) extra space — only a couple of variables
int sum(List<int> a) {
  var total = 0;        // 1 variable, no matter how big a is
  for (final x in a) total += x;
  return total;
}

// O(n) extra space — builds a new list as big as the input
List<int> doubled(List<int> a) {
  final out = <int>[];  // grows to size n
  for (final x in a) out.add(x * 2);
  return out;
}
```

**Step 3 — Recursion uses stack space.**
Each recursive call waits on the stack until it finishes. So recursion that goes n deep uses O(n) memory, even if it creates no lists.

```dart
int factorial(int n) {
  if (n <= 1) return 1;        // base case
  return n * factorial(n - 1); // n calls stacked up → O(n) space
}
```

**Step 4 — The classic trade-off: time vs space.**
Often you can make something faster by using more memory, or save memory by spending more time. Example: [Two Sum](#q22) uses a Map (extra O(n) space) to drop from O(n²) time to O(n) time.

**Why interviewers ask:** Senior engineers think about memory, not just speed — important on mobile, where memory is limited.

**Common mistake:** Forgetting the recursion call stack counts as space, or counting the input as extra space.

**Follow-ups they may ask:**
- *"In-place algorithm?"* → One that uses O(1) extra space by modifying the input directly (e.g. swapping elements in the same list).

**Related:** [Q1 — time complexity](#q1) · [Q15 — recursion & the call stack](#q15) · [Q22 — Two Sum (space-for-time)](#q22)

[↑ Back to top](#toc)

---

# B. Linear structures

---

<a id="q3"></a>
## 3. How do Dart Lists (arrays) work internally, and what are the time complexities?

> Very common · Medium

**Short answer (say this):**
"A Dart `List` is a dynamic array — items sit next to each other in memory, so reading by index is instant, O(1). Adding at the end is usually O(1), but when it runs out of room it copies everything to a bigger block, which is O(n) once in a while — that averages out to amortized O(1). Inserting or removing in the middle is O(n) because everything after it must shift."

**Let's understand it fully:**

**Step 1 — A real-life picture: numbered lockers in a row.**
An array is a row of lockers, numbered from 0. Because they are numbered and the same size, you can jump straight to locker 5 — no searching. That is why index access is O(1).

**Step 2 — Reading by index is O(1).**

```dart
final list = [10, 20, 30, 40];
print(list[2]); // 30 — instant, the computer jumps straight there
```

**Step 3 — Why "dynamic" array, and amortized O(1).**
A `List` has a fixed block of memory under the hood. When it fills up and you add more, Dart makes a bigger block (usually double the size) and copies everything over. That one copy is O(n). But because doubling happens rarely, the *average* cost per `add` is still O(1) — we call this **amortized O(1)**.

```dart
final list = <int>[];
list.add(1); // usually O(1)
list.add(2); // usually O(1)
// ... occasionally O(n) when it doubles its capacity, but rare
```

**Step 4 — Insert/remove in the middle is O(n).**
If you insert at the front, every other item must shift one spot to the right.

```dart
final list = [10, 20, 30];
list.insert(0, 5); // [5, 10, 20, 30] — all items shifted → O(n)
list.removeAt(0);  // shifts everything back → O(n)
```

**Step 5 — The complexity table to memorize.**

| Operation | Complexity | Why |
|---|---|---|
| access `list[i]` | O(1) | jump straight to the index |
| add/remove at end | O(1) amortized | occasional resize |
| insert/remove at middle/front | O(n) | shift the rest |
| search (`contains`, `indexOf`) | O(n) | check items one by one |

**Why interviewers ask:** Lists are the most-used structure. They want to know you understand the hidden cost of inserting in the middle and searching.

**Common mistake:** Thinking `insert(0, x)` or `contains` is cheap. Both are O(n). If you search a lot, use a Map or Set instead ([Q7](#q7), [Q8](#q8)).

**Follow-ups they may ask:**
- *"How to make a fixed-size list?"* → `List.filled(n, 0)` or `List.generate(n, ...)`.
- *"List vs Linked List?"* → See [Q4](#q4).

**Related:** [Q4 — linked list](#q4) · [Q7 — Map for fast lookup](#q7) · [Q1 — Big-O](#q1)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. What is a Linked List, how is it different from an array, and what are the trade-offs?

> Common · Medium

**Short answer (say this):**
"A linked list is a chain of nodes, where each node holds a value and a pointer to the next node. Unlike an array, the items are not next to each other in memory. So inserting or deleting at a known spot is O(1) — you just change pointers — but reading the nth item is O(n) because you must walk the chain from the start."

**Let's understand it fully:**

**Step 1 — A real-life picture: a treasure hunt.**
In a treasure hunt, each clue tells you where the next clue is. To reach clue 5, you must follow clues 1, 2, 3, 4 first. That is a linked list — you cannot jump straight to the middle.

**Step 2 — The node structure.**

```dart
class Node<T> {
  T value;
  Node<T>? next; // points to the next node, or null at the end
  Node(this.value, [this.next]);
}

// Build: 1 -> 2 -> 3
final head = Node(1, Node(2, Node(3)));
```

**Step 3 — Why insert/delete can be O(1).**
If you already hold a node, inserting after it is just pointer changes — no shifting:

```dart
// Insert 99 after a node `n`
final newNode = Node(99, n.next);
n.next = newNode; // done — O(1), nothing else moved
```

**Step 4 — Why access is O(n).**
To reach the 5th item you must follow `next` five times from the head.

```dart
Node<T>? getAt<T>(Node<T>? head, int index) {
  var current = head;
  for (var i = 0; i < index && current != null; i++) {
    current = current.next; // walk the chain → O(n)
  }
  return current;
}
```

**Step 5 — Array vs Linked List.**

| | Array / List | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) |
| Insert/delete at known spot | O(n) (shift) | O(1) (pointers) |
| Memory | one block, compact | scattered + extra pointer per node |
| Cache friendly | yes | no |

**Why interviewers ask:** It tests whether you understand memory layout and pointers, and that you can pick a structure by its operations.

**Common mistake:** Saying linked lists are "faster." They are only faster for insert/delete at a known node. For everyday work, Dart's `List` is usually better (compact memory, fast access).

**Follow-ups they may ask:**
- *"Singly vs doubly linked?"* → Doubly linked nodes also point to the previous node, so you can walk backwards (used by Dart's `Queue`).
- *"When use one in Flutter?"* → Rarely directly; but `Queue` (from `dart:collection`) is backed by a linked structure.

**Related:** [Q3 — arrays](#q3) · [Q6 — Queue](#q6)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What is a Stack, how does it work, and how do you implement one in Dart?

> Very common · Easy–Medium

**Short answer (say this):**
"A stack is Last-In-First-Out (LIFO) — the last item you put in is the first one you take out. Push adds to the top, pop removes from the top, both O(1). In Dart, a plain `List` is a stack: `add` to push and `removeLast` to pop."

**Let's understand it fully:**

**Step 1 — A real-life picture: a pile of plates.**
You add a plate on top, and you take the top plate off first. You can't pull one from the bottom. That is LIFO.

**Step 2 — Implement it with a List.**

```dart
final stack = <int>[];
stack.add(1);          // push → [1]
stack.add(2);          // push → [1, 2]
final top = stack.removeLast(); // pop → 2, stack is [1]
final peek = stack.last;         // look without removing → 1
final isEmpty = stack.isEmpty;
```

All of push, pop, and peek are O(1).

**Step 3 — Where stacks are used (real examples).**
- **Undo/redo** — each action is pushed; undo pops the last one.
- **Browser back button** — pages are pushed; back pops.
- **Flutter's Navigator** — screens are pushed and popped (it is literally a stack).
- **Function calls** — the call stack itself is a stack (see [Q15](#q15)).
- **Checking balanced brackets** — push opening brackets, pop on closing.

**Step 4 — A classic stack problem: balanced brackets.**

```dart
bool isBalanced(String s) {
  final stack = <String>[];
  const pairs = {')': '(', ']': '[', '}': '{'};
  for (final ch in s.split('')) {
    if (ch == '(' || ch == '[' || ch == '{') {
      stack.add(ch);                 // push opening
    } else if (pairs.containsKey(ch)) {
      if (stack.isEmpty || stack.removeLast() != pairs[ch]) {
        return false;                // wrong/missing match
      }
    }
  }
  return stack.isEmpty;              // all opened were closed
}
```

**Why interviewers ask:** Stacks appear everywhere (navigation, undo, parsing). They check you know LIFO and can use it to solve problems.

**Common mistake:** Using `removeAt(0)` (front) instead of `removeLast()`. `removeAt(0)` is O(n) and turns your stack into the wrong order.

**Follow-ups they may ask:**
- *"Stack vs Queue?"* → Stack = LIFO (last out first). Queue = FIFO (first out first). See [Q6](#q6).
- *"How does the Navigator use a stack?"* → `push` adds a screen on top, `pop` removes the top — exactly LIFO.

**Related:** [Q6 — Queue](#q6) · [Q15 — the call stack](#q15) · [Q3 — List](#q3)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is a Queue, how is it different from a Stack, and how do you use it in Dart?

> Common · Easy–Medium

**Short answer (say this):**
"A queue is First-In-First-Out (FIFO) — the first item in is the first one out, like a line at a shop. In Dart, use `Queue` from `dart:collection`, which adds and removes from both ends in O(1). A plain List can act as a queue too, but `removeAt(0)` is O(n), so prefer `Queue`."

**Let's understand it fully:**

**Step 1 — A real-life picture: a line at a shop.**
The first person in line is served first. New people join the back. That is FIFO — the opposite of a stack.

**Step 2 — Use Dart's `Queue` (fast at both ends).**

```dart
import 'dart:collection';

final queue = Queue<int>();
queue.add(1);              // enqueue at back → [1]
queue.add(2);              // → [1, 2]
final first = queue.removeFirst(); // dequeue from front → 1, O(1)
final peek = queue.first;          // look at front
```

**Step 3 — Why not just use a List?**
A List can do `add` (back) in O(1), but `removeAt(0)` (front) is O(n) because every other item shifts. `Queue` is built to be O(1) at both ends, so use it for real queue work.

**Step 4 — A Deque (double-ended queue).**
`Queue` is also a deque: you can add/remove at both ends (`addFirst`, `addLast`, `removeFirst`, `removeLast`). Useful for sliding-window problems.

**Step 5 — Where queues are used.**
- **BFS** (breadth-first search) on trees/graphs uses a queue ([Q9](#q9), [Q10](#q10)).
- **Task/job processing** — handle tasks in the order they arrived.
- **Print/download queues**, message buffers.

**Why interviewers ask:** Queues power BFS and any "process in arrival order" task. They check you know FIFO and the O(1)-front detail.

**Common mistake:** Using `List.removeAt(0)` in a loop (O(n) each time → O(n²) total). Use `Queue.removeFirst()`.

**Follow-ups they may ask:**
- *"Priority queue?"* → A queue where the highest-priority item comes out first, usually built on a heap (O(log n) insert/remove). Dart has no built-in one; use the `collection` package's `HeapPriorityQueue`.

**Related:** [Q5 — Stack (LIFO)](#q5) · [Q9 — BFS uses a queue](#q9) · [Q10 — graphs](#q10)

[↑ Back to top](#toc)

---

# C. Hash-based structures

---

<a id="q7"></a>
## 7. How does Dart's `Map` (HashMap) work internally, and what are the time complexities?

> Very common · Medium

**Short answer (say this):**
"A Map stores key-value pairs and finds a key almost instantly — average O(1) — by running the key through a hash function to compute where to store it. Worst case is O(n) if many keys collide into the same spot. Dart's default Map keeps insertion order, and keys must have correct `==` and `hashCode`."

**Let's understand it fully:**

**Step 1 — A real-life picture: a coat-check with numbered tags.**
At a coat-check, instead of searching every coat, they give your coat a number and hang it on hook #number. To get it back, they jump straight to that hook. A Map does the same: the hash of the key tells it which "hook" (bucket) to use.

**Step 2 — How a lookup works (the hash function).**

```dart
final ages = {'Sara': 30, 'Rahim': 25};
print(ages['Sara']); // 30 — average O(1)
```

Internally: `hashCode` of `'Sara'` → a bucket number → go straight to that bucket. No scanning the whole map.

**Step 3 — Collisions and why worst case is O(n).**
Two different keys can hash to the same bucket — a *collision*. The map then stores both in that bucket and checks them with `==`. If almost all keys collide into one bucket, lookups degrade to O(n). Good hash functions make this rare, so we treat lookups as O(1) on average.

**Step 4 — Keys need correct `==` and `hashCode`.**
The map finds the bucket with `hashCode`, then confirms the exact key with `==`. If you use a custom object as a key without overriding both, lookups fail.

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
print(m[const Point(1, 2)]); // 'A' — works because == and hashCode are correct
```

**Step 5 — Complexity table.**

| Operation | Average | Worst |
|---|---|---|
| insert / update | O(1) | O(n) |
| lookup `m[key]` | O(1) | O(n) |
| delete | O(1) | O(n) |
| contains key | O(1) | O(n) |

**Why interviewers ask:** Maps are the #1 tool to turn O(n²) brute force into O(n) (see [Two Sum](#q22)). They want you to reach for a Map when you need fast lookups.

**Common mistake:** Searching a List with `contains`/`indexOf` (O(n)) inside a loop, when a Map/Set would make it O(1). Also: using a mutable object as a key, then mutating it.

**Follow-ups they may ask:**
- *"Default Map type?"* → `LinkedHashMap` — keeps insertion order. Use `SplayTreeMap` for sorted keys.
- *"Map vs Set?"* → A Set is a Map with keys only (no values). See [Q8](#q8).

**Related:** [Q8 — Set](#q8) · [Q22 — Two Sum with a Map](#q22) · [Q3 — List (slow search)](#q3)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is a Set, how is it different from a List, and when should you use it?

> Common · Easy–Medium

**Short answer (say this):**
"A Set is a collection of unique items with no duplicates, and it checks membership in O(1) on average. A List allows duplicates and checks membership in O(n). So use a Set whenever you need uniqueness or fast 'have I seen this?' checks."

**Let's understand it fully:**

**Step 1 — The two key differences.**
- A **List** keeps order and allows duplicates; `contains` is O(n).
- A **Set** has no duplicates and no guaranteed order (the default keeps insertion order); `contains` is O(1) average (it is hash-based, like a Map's keys).

```dart
final list = [1, 2, 2, 3];   // duplicates allowed
final set = {1, 2, 2, 3};    // {1, 2, 3} — duplicate removed
print(set.contains(2));       // O(1) average
```

**Step 2 — The classic use: remove duplicates.**

```dart
final names = ['a', 'b', 'a', 'c'];
final unique = names.toSet().toList(); // ['a', 'b', 'c']
```

**Step 3 — The other classic use: fast "seen before?" checks.**

```dart
bool hasDuplicate(List<int> nums) {
  final seen = <int>{};
  for (final n in nums) {
    if (!seen.add(n)) return true; // add returns false if already present
  }
  return false;
} // O(n) time, O(n) space — far better than a nested-loop O(n^2)
```

**Step 4 — Set math.**
Sets support union, intersection, and difference — handy for comparing groups.

```dart
final a = {1, 2, 3};
final b = {2, 3, 4};
print(a.intersection(b)); // {2, 3}
print(a.union(b));        // {1, 2, 3, 4}
print(a.difference(b));   // {1}
```

**Why interviewers ask:** Swapping a List for a Set is the simplest way to fix slow O(n²) "search inside a loop" code.

**Common mistake:** Using a List and `contains` to track seen items inside a loop — that is O(n²). A Set makes it O(n).

**Follow-ups they may ask:**
- *"Sorted set?"* → `SplayTreeSet` keeps items in sorted order.
- *"How does it stay unique?"* → It uses `hashCode`/`==`, just like a Map's keys ([Q7](#q7)).

**Related:** [Q7 — Map (same hashing)](#q7) · [Q19 — find duplicates](#q19) · [Q3 — List](#q3)

[↑ Back to top](#toc)

---

# D. Trees & graphs

---

<a id="q9"></a>
## 9. What is a Binary Tree, and how do BFS and DFS traversals work?

> Very common · Medium

**Short answer (say this):**
"A binary tree is nodes where each node has up to two children, left and right. BFS (breadth-first) visits the tree level by level using a queue. DFS (depth-first) goes as deep as possible down one branch first, using recursion or a stack. Both visit every node, so both are O(n)."

**Let's understand it fully:**

**Step 1 — The node.**

```dart
class TreeNode {
  int value;
  TreeNode? left;
  TreeNode? right;
  TreeNode(this.value, [this.left, this.right]);
}
```

**Step 2 — DFS (depth-first): go deep first, using recursion.**
DFS dives down one branch fully before backing up. The three orders differ only in *when* you visit the current node:
- **In-order** (left, node, right) — for a binary search tree, this gives sorted order.
- **Pre-order** (node, left, right).
- **Post-order** (left, right, node).

```dart
void inOrder(TreeNode? node) {
  if (node == null) return;     // base case
  inOrder(node.left);           // go left
  print(node.value);            // visit
  inOrder(node.right);          // go right
}
```

**Step 3 — BFS (breadth-first): go level by level, using a queue.**
BFS visits all nodes at depth 1, then depth 2, and so on. A queue holds the nodes waiting to be visited.

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

**Step 4 — When to use which.**
- **BFS** → shortest path in an unweighted graph; "level order"; nearest neighbours first.
- **DFS** → explore all paths; tree depth; detecting cycles; problems that feel recursive.

**Step 5 — Complexity.**
Both are **O(n)** time (every node once). Space: BFS uses O(width) for the queue; DFS uses O(height) for the call stack.

**Why interviewers ask:** Trees and these two traversals are the base for a huge number of interview problems.

**Common mistake:** Mixing them up. Remember: **BFS = queue (level by level)**, **DFS = recursion/stack (deep first)**.

**Follow-ups they may ask:**
- *"Binary Search Tree (BST)?"* → A binary tree where left < node < right. In-order DFS gives sorted output; search is O(log n) if balanced, O(n) if it degenerates into a chain.
- *"Recursive vs iterative DFS?"* → Recursion uses the call stack; iterative DFS uses an explicit stack ([Q5](#q5)).

**Related:** [Q10 — graphs (same BFS/DFS)](#q10) · [Q6 — Queue (BFS)](#q6) · [Q15 — recursion (DFS)](#q15)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is a Graph, how do you represent one, and how do BFS/DFS work on it?

> Common · Medium–Hard

**Short answer (say this):**
"A graph is nodes (vertices) connected by edges — like a map of cities and roads. The most common representation is an adjacency list: a Map from each node to a list of its neighbours. BFS and DFS work like on trees, but you must track visited nodes, because graphs can have cycles."

**Let's understand it fully:**

**Step 1 — A real-life picture: cities and roads.**
Cities are nodes; roads are edges. A graph can have cycles (you can drive in a loop), unlike a tree.

**Step 2 — Representation: adjacency list (most common).**

```dart
// Map: node -> its neighbours
final graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D'],
  'D': ['B', 'C'],
};
```

This uses O(V + E) space (V nodes + E edges) — efficient for most graphs.

**Step 3 — The key difference from trees: track visited.**
Because graphs can loop, you must remember which nodes you already visited, or you will loop forever.

```dart
import 'dart:collection';

void bfs(Map<String, List<String>> g, String start) {
  final visited = <String>{start};      // a Set to avoid revisiting
  final queue = Queue<String>()..add(start);
  while (queue.isNotEmpty) {
    final node = queue.removeFirst();
    print(node);
    for (final next in g[node] ?? []) {
      if (visited.add(next)) {          // add returns false if already seen
        queue.add(next);
      }
    }
  }
}
```

```dart
void dfs(Map<String, List<String>> g, String node, Set<String> visited) {
  if (!visited.add(node)) return; // already visited → stop
  print(node);
  for (final next in g[node] ?? []) {
    dfs(g, next, visited);
  }
}
```

**Step 4 — Complexity.**
Both BFS and DFS are **O(V + E)** — every node and every edge is looked at once.

**Step 5 — When to use which.**
- **BFS** → shortest path in an unweighted graph (fewest hops).
- **DFS** → detect cycles, find connected components, topological sort.

**Why interviewers ask:** Graph traversal underlies maps, social networks, dependency resolution, and many medium/hard problems.

**Common mistake:** Forgetting the `visited` set — on a graph with a cycle, that causes an infinite loop. (Trees don't need it; graphs do.)

**Follow-ups they may ask:**
- *"Adjacency list vs matrix?"* → List = Map of neighbours, O(V+E) space, good for sparse graphs. Matrix = 2D grid of true/false, O(V²) space, good for dense graphs and O(1) edge checks.
- *"Weighted shortest path?"* → Use Dijkstra's algorithm (BFS with a priority queue).

**Related:** [Q9 — trees (BFS/DFS)](#q9) · [Q6 — Queue (BFS)](#q6) · [Q8 — Set (visited)](#q8)

[↑ Back to top](#toc)

---

# E. Searching & sorting

---

<a id="q11"></a>
## 11. How does Binary Search work, and when can you use it?

> Very common · Medium

**Short answer (say this):**
"Binary search finds an item in a sorted list in O(log n) by repeatedly cutting the search range in half. You check the middle: if it's the target, done; if the target is smaller, search the left half; if bigger, the right half. The one rule: the list must already be sorted."

**Let's understand it fully:**

**Step 1 — A real-life picture: finding a word in a dictionary.**
You don't read a dictionary page by page. You open the middle, see if your word is before or after, and throw away half. Repeat. That is binary search.

**Step 2 — The algorithm.**

```dart
int binarySearch(List<int> sorted, int target) {
  var low = 0;
  var high = sorted.length - 1;
  while (low <= high) {
    final mid = low + (high - low) ~/ 2; // avoids overflow; ~/ is integer divide
    if (sorted[mid] == target) return mid;     // found
    if (sorted[mid] < target) {
      low = mid + 1;   // target is in the right half
    } else {
      high = mid - 1;  // target is in the left half
    }
  }
  return -1; // not found
}
```

**Step 3 — Why it's O(log n).**
Each step throws away half the items. For 1,000,000 items, you reach the answer in about 20 steps. That is the power of "halving."

**Step 4 — The one requirement: sorted input.**
Binary search only works on sorted data. If the data isn't sorted, you either sort first (O(n log n)) or use a different approach (a Set/Map for O(1) lookups).

**Step 5 — Watch the boundaries.**
The two classic bugs: using `<` instead of `<=` in the loop, and computing `mid` as `(low + high) ~/ 2` (can overflow in some languages — `low + (high - low) ~/ 2` is safe).

**Why interviewers ask:** It tests careful boundary handling (off-by-one bugs) and whether you recognize "sorted input" as a signal to use it.

**Common mistake:** Using binary search on unsorted data, or an off-by-one error in `low`/`high`/`mid`.

**Follow-ups they may ask:**
- *"What if there are duplicates?"* → You can adapt it to find the first or last occurrence.
- *"Recursive version?"* → Same logic, but recursion uses O(log n) stack space instead of O(1).

**Related:** [Q12 — sorting (needed first)](#q12) · [Q1 — Big-O (log n)](#q1)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. Explain Bubble, Insertion, Merge, and Quick Sort — approach and complexity.

> Very common · Medium–Hard

**Short answer (say this):**
"Bubble and Insertion sort are simple but O(n²) — fine only for tiny or nearly-sorted data. Merge sort is O(n log n) always and stable, but uses O(n) extra space. Quick sort is O(n log n) on average and sorts in place, but O(n²) in the worst case. In practice Dart's built-in `sort()` uses a tuned hybrid, so I rarely write my own."

**Let's understand it fully:**

**Step 1 — Bubble Sort — repeatedly swap neighbours. O(n²).**
Walk the list, swapping any pair that is out of order; repeat until no swaps. Simple, but slow.

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

**Step 2 — Insertion Sort — build a sorted part one item at a time. O(n²), but fast on nearly-sorted data.**
Like sorting playing cards in your hand: take the next card and slide it into its correct place among the ones already sorted.

**Step 3 — Merge Sort — divide and conquer. O(n log n) always, stable, O(n) space.**
Split the list in half, sort each half (recursively), then merge the two sorted halves.

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

**Step 4 — Quick Sort — pick a pivot, partition around it. O(n log n) average, O(n²) worst, in place.**
Choose a pivot, move smaller items left and bigger items right, then sort each side. Fast in practice; worst case happens with bad pivots (e.g. already-sorted input with a naive pivot).

**Step 5 — The comparison table.**

| Algorithm | Average | Worst | Space | Stable? |
|---|---|---|---|---|
| Bubble | O(n²) | O(n²) | O(1) | yes |
| Insertion | O(n²) | O(n²) | O(1) | yes |
| Merge | O(n log n) | O(n log n) | O(n) | yes |
| Quick | O(n log n) | O(n²) | O(log n) | no |

**Why interviewers ask:** Sorting is the classic way to test divide-and-conquer thinking and complexity analysis.

**Common mistake:** Claiming quick sort is "always O(n log n)" — its worst case is O(n²). Also, calling merge sort in-place — it needs O(n) extra space.

**Follow-ups they may ask:**
- *"What does 'stable' mean?"* → Equal items keep their original relative order. Matters when sorting by one field but wanting to preserve another's order.
- *"What does Dart's `list.sort()` use?"* → A tuned hybrid (insertion sort for small chunks, merge-style for the rest). You rarely hand-write a sort.

**Related:** [Q11 — binary search needs sorted data](#q11) · [Q1 — Big-O](#q1) · [Q15 — recursion (merge/quick)](#q15)

[↑ Back to top](#toc)

---

# F. Core techniques

---

<a id="q13"></a>
## 13. What is the Two Pointers technique, and when do you use it?

> Common · Medium

**Short answer (say this):**
"Two pointers means using two index variables that move through a list, instead of a nested loop. It turns many O(n²) problems into O(n). The two common styles are pointers starting at opposite ends and moving toward each other, or both moving in the same direction at different speeds."

**Let's understand it fully:**

**Step 1 — A real-life picture: two people reading from both ends.**
To check if a word reads the same forwards and backwards, one person reads from the start and another from the end, moving toward the middle. Two pointers.

**Step 2 — Opposite ends (works on sorted data).**
Example: in a sorted list, find two numbers that add up to a target.

```dart
List<int>? twoSumSorted(List<int> sorted, int target) {
  var left = 0;
  var right = sorted.length - 1;
  while (left < right) {
    final sum = sorted[left] + sorted[right];
    if (sum == target) return [left, right];
    if (sum < target) {
      left++;     // need a bigger sum → move left pointer up
    } else {
      right--;    // need a smaller sum → move right pointer down
    }
  }
  return null;
} // O(n) time, O(1) space — beats the O(n^2) nested loop
```

**Step 3 — Same direction (fast and slow pointers).**
Example: remove duplicates from a sorted list in place. A "slow" pointer marks where to write; a "fast" pointer scans ahead.

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
  return slow + 1; // length of the unique part
}
```

**Step 4 — How to spot it.**
Look for: a **sorted** list, finding **pairs**, comparing **both ends**, or **in-place** rearranging. These hint at two pointers.

**Why interviewers ask:** It is one of the most common patterns for turning brute force into linear time.

**Common mistake:** Using two pointers on unsorted data when the technique needs sorted input (the opposite-ends style).

**Follow-ups they may ask:**
- *"Two pointers vs sliding window?"* → Sliding window is a special two-pointer pattern where the gap between pointers is a "window" you grow and shrink ([Q14](#q14)).

**Related:** [Q14 — sliding window](#q14) · [Q22 — Two Sum](#q22) · [Q18 — palindrome](#q18)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What is the Sliding Window technique, and when should you use it?

> Common · Medium

**Short answer (say this):**
"Sliding window keeps a 'window' over part of a list and slides it instead of recomputing from scratch. When you move the window one step, you add the new item and remove the old one — so a problem that looks O(n²) becomes O(n). Use it for 'best subarray/substring of size k' or 'longest/shortest range that satisfies a rule' questions."

**Let's understand it fully:**

**Step 1 — A real-life picture: a moving train window.**
Looking out a train window, you see a fixed stretch of scenery. As the train moves, one new tree enters the view and one old tree leaves — you don't re-scan everything.

**Step 2 — Fixed window — max sum of k items in a row.**

```dart
int maxSumOfK(List<int> a, int k) {
  var windowSum = 0;
  for (var i = 0; i < k; i++) windowSum += a[i]; // first window
  var best = windowSum;
  for (var i = k; i < a.length; i++) {
    windowSum += a[i] - a[i - k]; // add new, remove old → O(1) per step
    if (windowSum > best) best = windowSum;
  }
  return best;
} // O(n) instead of O(n*k)
```

**Step 3 — Variable window — longest range that follows a rule.**
Grow the window by moving `right`; when the rule breaks, shrink it by moving `left`.

```dart
int longestUniqueSubstring(String s) {
  final seen = <String>{};
  var left = 0, best = 0;
  for (var right = 0; right < s.length; right++) {
    while (seen.contains(s[right])) {
      seen.remove(s[left]); // shrink from the left until valid
      left++;
    }
    seen.add(s[right]);     // grow on the right
    best = best > right - left + 1 ? best : right - left + 1;
  }
  return best;
}
```

**Step 4 — How to spot it.**
Look for: "subarray/substring", "consecutive", "of size k", "longest/shortest range with a condition". These signal a sliding window.

**Why interviewers ask:** It is the standard pattern for subarray/substring problems and a big efficiency win.

**Common mistake:** Recomputing the whole window each move (back to O(n·k)). The trick is updating in O(1): add the entering item, remove the leaving item.

**Follow-ups they may ask:**
- *"Fixed vs variable window?"* → Fixed = constant size k. Variable = grows/shrinks based on a condition.

**Related:** [Q13 — two pointers](#q13) · [Q8 — Set (tracking window contents)](#q8)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. How does recursion work? Explain the base case, the call stack, and tail recursion.

> Very common · Medium

**Short answer (say this):**
"Recursion is a function that calls itself to solve a smaller piece of the same problem. It needs a base case — a stopping condition — or it runs forever. Each call waits on the call stack until the deeper calls finish, so deep recursion uses O(n) stack memory and can overflow."

**Let's understand it fully:**

**Step 1 — A real-life picture: Russian nesting dolls.**
To find the smallest doll, you open a doll to reveal a smaller one, and repeat, until you reach the tiniest doll that doesn't open. That last doll is the **base case**.

**Step 2 — Every recursion needs two parts.**
1. **Base case** — when to stop.
2. **Recursive case** — call yourself on a smaller input, moving toward the base case.

```dart
int factorial(int n) {
  if (n <= 1) return 1;          // base case (stop)
  return n * factorial(n - 1);   // recursive case (smaller problem)
}
// factorial(3) = 3 * factorial(2) = 3 * 2 * factorial(1) = 3 * 2 * 1 = 6
```

**Step 3 — The call stack.**
Each call is stacked and paused until the call below it returns. `factorial(3)` waits for `factorial(2)`, which waits for `factorial(1)`. When the base case returns, they unwind back up. This stack is why recursion uses **O(depth) memory**.

**Step 4 — Stack overflow.**
If there is no base case, or the input is huge, the stack grows until it runs out of memory — a **StackOverflowError**. For very deep problems, an iterative loop (using your own stack or a queue) is safer.

**Step 5 — Tail recursion.**
A call is "tail recursive" if the recursive call is the very last thing the function does (nothing waits after it). Some languages optimize this into a loop (no growing stack). Note: Dart does **not** guarantee tail-call optimization, so for deep recursion in Dart, prefer a loop.

```dart
// Tail-recursive style (accumulator carries the result)
int factorialTail(int n, [int acc = 1]) {
  if (n <= 1) return acc;
  return factorialTail(n - 1, acc * n); // last action is the call
}
```

**Why interviewers ask:** Recursion is the natural tool for trees, graphs, and divide-and-conquer. They want to see you always define a base case and understand the stack cost.

**Common mistake:** Forgetting the base case (infinite recursion → stack overflow), or not moving toward the base case.

**Follow-ups they may ask:**
- *"Recursion vs iteration?"* → Same power. Recursion is cleaner for tree/graph problems; iteration avoids stack-overflow risk and uses less memory.
- *"How to make slow recursion fast?"* → Add memoization (see [Q16](#q16) and [Q21](#q21)).

**Related:** [Q16 — dynamic programming](#q16) · [Q9 — DFS (recursion)](#q9) · [Q2 — stack space](#q2)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. What is Dynamic Programming, and what is the difference between memoization and tabulation?

> Common · Medium–Hard

**Short answer (say this):**
"Dynamic programming (DP) solves a big problem by combining answers to smaller overlapping sub-problems, and it stores each sub-answer so it is computed only once. Memoization is top-down: normal recursion plus a cache. Tabulation is bottom-up: fill a table from the smallest cases up. Both turn slow exponential recursion into fast linear time."

**Let's understand it fully:**

**Step 1 — When DP applies.**
DP fits problems with two traits:
1. **Overlapping sub-problems** — the same smaller problem is solved many times.
2. **Optimal substructure** — the best answer is built from the best answers of sub-problems.

The classic example is Fibonacci: naive recursion recomputes the same values over and over (O(2ⁿ)).

**Step 2 — Memoization (top-down): recursion + a cache.**
Solve it recursively, but remember each answer in a Map so you never recompute it.

```dart
int fib(int n, [Map<int, int>? memo]) {
  memo ??= {};
  if (n <= 1) return n;                 // base case
  if (memo.containsKey(n)) return memo[n]!; // already computed → reuse
  return memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
} // O(n) time, O(n) space — down from O(2^n)
```

**Step 3 — Tabulation (bottom-up): fill a table from the start.**
Start from the smallest cases and build up, no recursion.

```dart
int fibTab(int n) {
  if (n <= 1) return n;
  final dp = List.filled(n + 1, 0);
  dp[1] = 1;
  for (var i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2]; // build from smaller answers
  }
  return dp[n];
} // O(n) time; can be reduced to O(1) space by keeping only the last two
```

**Step 4 — Which to use.**
- **Memoization** — easier to write (just add a cache to a natural recursion); uses stack space.
- **Tabulation** — no recursion (no stack-overflow risk); often easier to optimize the space.

**Why interviewers ask:** DP is a common medium/hard topic. They want to see you spot repeated work and cache it.

**Common mistake:** Using DP where there are no overlapping sub-problems (then it's just plain recursion). Or forgetting to actually store/reuse results.

**Follow-ups they may ask:**
- *"Give classic DP problems."* → Fibonacci, climbing stairs, coin change, longest common subsequence, knapsack.
- *"Top-down vs bottom-up trade-off?"* → Top-down only computes needed sub-problems; bottom-up computes all but avoids recursion overhead.

**Related:** [Q15 — recursion](#q15) · [Q21 — Fibonacci (the example)](#q21) · [Q7 — Map as the cache](#q7)

[↑ Back to top](#toc)

---

# G. Common coding problems (Dart)

---

<a id="q17"></a>
## 17. Write a function that reverses a string.

> Common · Easy

**Short answer (say this):**
"The simplest correct way in Dart is to split the string into characters, reverse the list, and join it back. That's O(n) time and O(n) space. If asked to do it in place on a list of characters, I'd use two pointers swapping from both ends."

**Let's understand it fully:**

**Step 1 — The clean Dart way.**

```dart
String reverse(String s) => s.split('').reversed.join();
// reverse('hello') -> 'olleh'
```

This is O(n) time and O(n) space (a new string is built).

**Step 2 — The two-pointer way (shows the underlying idea).**
Interviewers sometimes want the manual version to see you understand the mechanics.

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

**Step 3 — The gotcha: emojis and accents.**
Some characters (emojis, accented letters) are made of multiple code units, and a naive reverse can break them. For interview purposes, the simple version is fine; just mention you're aware that proper Unicode reversal needs the `characters` package (`s.characters.toList().reversed`).

**Why interviewers ask:** A warm-up that checks basic string handling and whether you know the two-pointer swap.

**Common mistake:** Trying to index a Dart `String` like an array to swap in place — strings are immutable, so you must convert to a list first.

**Follow-ups they may ask:**
- *"Reverse without built-ins?"* → Use the two-pointer version above.
- *"Reverse the words, not the letters?"* → `s.split(' ').reversed.join(' ')`.

**Related:** [Q13 — two pointers](#q13) · [Q18 — palindrome](#q18)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. Write a function to check if a string is a palindrome.

> Common · Easy

**Short answer (say this):**
"A palindrome reads the same forwards and backwards. The cleanest check uses two pointers — one from the start, one from the end — comparing characters as they move toward the middle. That's O(n) time and O(1) extra space."

**Let's understand it fully:**

**Step 1 — Two pointers from both ends.**

```dart
bool isPalindrome(String s) {
  var left = 0, right = s.length - 1;
  while (left < right) {
    if (s[left] != s[right]) return false; // mismatch → not a palindrome
    left++;
    right--;
  }
  return true;
} // O(n) time, O(1) extra space
```

**Step 2 — The "clean" real-world version (ignore case and non-letters).**
Interviewers often ask: is "A man, a plan, a canal: Panama" a palindrome? Yes — once you ignore spaces, punctuation, and case.

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

**Step 3 — The shorter (but more memory) version.**

```dart
bool isPalindromeSimple(String s) => s == s.split('').reversed.join();
```

This is O(n) space because it builds a reversed copy. The two-pointer version is better (O(1) space).

**Why interviewers ask:** A clean two-pointer warm-up. They may push you to handle case/punctuation, which tests attention to detail.

**Common mistake:** Forgetting to clean the input when the question implies it ("ignore spaces and case"), or building a reversed copy when O(1) space is possible.

**Follow-ups they may ask:**
- *"Check if a number is a palindrome?"* → Convert to a string, or reverse the number with math.

**Related:** [Q13 — two pointers](#q13) · [Q17 — reverse a string](#q17)

[↑ Back to top](#toc)

---

<a id="q19"></a>
## 19. Write a function to find all duplicate elements in a list.

> Common · Easy–Medium

**Short answer (say this):**
"Walk the list once, keeping a Set of items you've already seen. If an item is already in the Set, it's a duplicate. That's O(n) time and O(n) space — far better than comparing every pair, which is O(n²)."

**Let's understand it fully:**

**Step 1 — The efficient way: a 'seen' Set.**

```dart
Set<int> findDuplicates(List<int> nums) {
  final seen = <int>{};
  final duplicates = <int>{};
  for (final n in nums) {
    if (!seen.add(n)) {  // add returns false if n was already there
      duplicates.add(n);
    }
  }
  return duplicates;
} // O(n) time, O(n) space
```

**Step 2 — Why not nested loops?**
Comparing every item with every other item is O(n²) — much slower on big inputs. The Set turns the "have I seen this?" check into O(1).

```dart
// Avoid this O(n^2) approach:
// for each i, for each j, compare nums[i] and nums[j]
```

**Step 3 — Counting how many times each appears.**
If you need counts, not just which ones repeat, use a Map.

```dart
Map<int, int> counts(List<int> nums) {
  final map = <int, int>{};
  for (final n in nums) {
    map[n] = (map[n] ?? 0) + 1; // increment, default 0
  }
  return map; // e.g. {1: 3, 2: 1}
}
```

**Why interviewers ask:** It's the simplest demonstration of "use a Set/Map to avoid an O(n²) nested loop."

**Common mistake:** Using a List and `contains` to track seen items — that's O(n) per check, making it O(n²) overall. Use a Set.

**Follow-ups they may ask:**
- *"Find the first non-repeating element?"* → Count with a Map, then scan for the first item with count 1.
- *"Find duplicates with O(1) space?"* → Possible only with special constraints (e.g. values in a known range, or allowed to modify the input).

**Related:** [Q8 — Set](#q8) · [Q7 — Map (counting)](#q7)

[↑ Back to top](#toc)

---

<a id="q20"></a>
## 20. Write FizzBuzz.

> Common · Easy

**Short answer (say this):**
"For numbers 1 to n: print 'FizzBuzz' if divisible by both 3 and 5, else 'Fizz' if divisible by 3, else 'Buzz' if divisible by 5, else the number. The key is to check the both-case (15) first, otherwise it never runs."

**Let's understand it fully:**

**Step 1 — The straightforward solution.**

```dart
void fizzBuzz(int n) {
  for (var i = 1; i <= n; i++) {
    if (i % 15 == 0) {
      print('FizzBuzz');     // divisible by 3 AND 5 — check FIRST
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

**Step 2 — Why the order matters.**
If you check `i % 3` before `i % 15`, then 15 prints "Fizz" and the "FizzBuzz" branch never runs. Always check the most specific condition (both) first.

**Step 3 — A cleaner, extendable version.**
Build the string by appending, so it's easy to add new rules later.

```dart
void fizzBuzz2(int n) {
  for (var i = 1; i <= n; i++) {
    var out = '';
    if (i % 3 == 0) out += 'Fizz';
    if (i % 5 == 0) out += 'Buzz';
    print(out.isEmpty ? '$i' : out); // empty means no rule matched
  }
}
```

**Why interviewers ask:** A quick screen for basic control flow and the modulo operator — and whether you catch the ordering trap.

**Common mistake:** Checking 3 and 5 before the 15 case, so multiples of 15 never print "FizzBuzz".

**Follow-ups they may ask:**
- *"Add a new rule (e.g. 7 → 'Bazz')?"* → The second version makes this trivial: add another `if`.

**Related:** [Q1 — Big-O (this is O(n))](#q1)

[↑ Back to top](#toc)

---

<a id="q21"></a>
## 21. Compute the nth Fibonacci number — iterative, recursive, and memoized.

> Very common · Medium

**Short answer (say this):**
"Fibonacci is each number being the sum of the previous two. The naive recursion is O(2ⁿ) because it recomputes the same values endlessly. The iterative version is O(n) time and O(1) space — the best for an interview. Memoization also makes the recursion O(n)."

**Let's understand it fully:**

**Step 1 — The naive recursion (don't ship this).**

```dart
int fibSlow(int n) {
  if (n <= 1) return n;
  return fibSlow(n - 1) + fibSlow(n - 2); // recomputes the same calls → O(2^n)
}
```

It's clean but explodes: `fibSlow(50)` does over a billion calls.

**Step 2 — Iterative — the best answer (O(n) time, O(1) space).**
Just keep the last two numbers and roll forward.

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

**Step 3 — Memoized recursion (O(n) time, O(n) space).**
If they want a recursive solution, add a cache so each value is computed once (this is dynamic programming — see [Q16](#q16)).

```dart
int fibMemo(int n, [Map<int, int>? memo]) {
  memo ??= {};
  if (n <= 1) return n;
  if (memo.containsKey(n)) return memo[n]!;
  return memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
}
```

**Step 4 — The comparison.**

| Approach | Time | Space |
|---|---|---|
| Naive recursion | O(2ⁿ) | O(n) stack |
| Memoized recursion | O(n) | O(n) |
| Iterative | O(n) | O(1) |

**Why interviewers ask:** It's the cleanest way to show the cost of repeated work and how memoization/iteration fixes it.

**Common mistake:** Giving only the naive recursion and not mentioning it's exponential, or not knowing the O(1)-space iterative version.

**Follow-ups they may ask:**
- *"Which would you use in production?"* → The iterative version — fastest and lowest memory.

**Related:** [Q16 — dynamic programming](#q16) · [Q15 — recursion](#q15)

[↑ Back to top](#toc)

---

<a id="q22"></a>
## 22. Two Sum — find two indices whose values add up to a target.

> Very common · Medium

**Short answer (say this):**
"Walk the list once, keeping a Map from each value to its index. For each number, check if 'target minus this number' is already in the Map — if so, you've found the pair. That's O(n) time and O(n) space, versus the O(n²) nested-loop brute force."

**Let's understand it fully:**

**Step 1 — The brute force (mention it, then improve).**
Check every pair with two loops: O(n²). Works, but slow.

**Step 2 — The optimal: one pass with a Map.**
The trick: as you go, remember each number you've seen and where. For the current number, the partner you need is `target - current`. If you've already seen that partner, done.

```dart
List<int>? twoSum(List<int> nums, int target) {
  final seen = <int, int>{}; // value -> index
  for (var i = 0; i < nums.length; i++) {
    final need = target - nums[i];
    if (seen.containsKey(need)) {
      return [seen[need]!, i]; // found the pair
    }
    seen[nums[i]] = i;         // remember this number for later
  }
  return null;                 // no pair found
}
// twoSum([2, 7, 11, 15], 9) -> [0, 1]  because 2 + 7 = 9
```

**Step 3 — Why this is the classic "Map beats nested loop" example.**
The Map turns "is the partner somewhere in the list?" from an O(n) search into an O(1) lookup. Doing that O(1) check inside the single loop gives O(n) total.

**Step 4 — The time/space trade-off.**
We spend O(n) extra memory (the Map) to save time (O(n²) → O(n)). That trade is almost always worth it.

**Why interviewers ask:** It's the single most famous "use a hash map to drop from O(n²) to O(n)" question. They want to see you reach for a Map.

**Common mistake:** Returning the brute-force O(n²) and stopping. Also, adding the current number to the Map *before* checking — that can wrongly pair a number with itself.

**Follow-ups they may ask:**
- *"What if the list is sorted?"* → Use two pointers from both ends ([Q13](#q13)) for O(1) extra space.
- *"What if no pair exists?"* → Return null/empty, and say so explicitly.

**Related:** [Q7 — Map](#q7) · [Q13 — two pointers (sorted version)](#q13) · [Q1 — Big-O](#q1)

[↑ Back to top](#toc)

---

<a id="q23"></a>
## 23. Find the maximum value in a list without using `max()`.

> Common · Easy

**Short answer (say this):**
"Track a 'best so far' variable. Start it at the first element, then walk the list once and update it whenever you find something bigger. That's O(n) time and O(1) space. The key edge case is an empty list — decide whether to throw or return null."

**Let's understand it fully:**

**Step 1 — The single-pass solution.**

```dart
int findMax(List<int> nums) {
  if (nums.isEmpty) {
    throw ArgumentError('list is empty'); // handle the edge case explicitly
  }
  var best = nums[0];               // start with the first item
  for (var i = 1; i < nums.length; i++) {
    if (nums[i] > best) best = nums[i]; // update when we find something bigger
  }
  return best;
} // O(n) time, O(1) space
```

**Step 2 — Why start at `nums[0]`, not 0?**
If you start `best = 0` and all numbers are negative, you'd wrongly return 0. Starting at the first real element avoids that bug.

**Step 3 — A null-safe version for empty lists.**
If throwing is not wanted, return a nullable value:

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

**Why interviewers ask:** A simple test of looping, a "best so far" accumulator, and whether you handle the empty-list edge case.

**Common mistake:** Initializing `best = 0` (breaks on all-negative lists), or forgetting the empty-list case (crashes on `nums[0]`).

**Follow-ups they may ask:**
- *"Find the second largest?"* → Track two variables (largest and secondLargest) in one pass.
- *"Find both min and max?"* → Track two accumulators in the same loop.

**Related:** [Q1 — Big-O (O(n))](#q1) · [Q3 — List](#q3)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## Big-O of common operations

| Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| List (array) | O(1) | O(n) | O(n) (end: O(1) amortized) | O(n) (end: O(1)) |
| Linked List | O(n) | O(n) | O(1) at known node | O(1) at known node |
| Map / Set (hash) | — | O(1) avg | O(1) avg | O(1) avg |
| Stack / Queue | — | — | O(1) | O(1) |
| Binary Search Tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |

## Sorting at a glance

| Algorithm | Average | Worst | Space | Stable |
|---|---|---|---|---|
| Bubble / Insertion | O(n²) | O(n²) | O(1) | yes |
| Merge | O(n log n) | O(n log n) | O(n) | yes |
| Quick | O(n log n) | O(n²) | O(log n) | no |

## Which structure / technique to use

| Need | Use |
|---|---|
| Fast lookup by key | Map ([Q7](#q7)) |
| Uniqueness / "seen before?" | Set ([Q8](#q8)) |
| LIFO (undo, navigation) | Stack ([Q5](#q5)) |
| FIFO / BFS | Queue ([Q6](#q6)) |
| Search sorted data | Binary search ([Q11](#q11)) |
| Pair / both-ends on sorted data | Two pointers ([Q13](#q13)) |
| Best subarray/substring | Sliding window ([Q14](#q14)) |
| Repeated sub-problems | Dynamic programming ([Q16](#q16)) |

## One-line reminders

- **Big-O** = how work grows with input. Drop constants, keep the biggest term. ([Q1](#q1))
- **Space** counts EXTRA memory, including the recursion call stack. ([Q2](#q2))
- **List**: index O(1), search O(n), middle insert O(n). ([Q3](#q3))
- **Map/Set**: O(1) average lookup — the cure for O(n²) nested loops. ([Q7](#q7), [Q8](#q8))
- **Stack** = LIFO (`add`/`removeLast`); **Queue** = FIFO (`Queue.removeFirst`). ([Q5](#q5), [Q6](#q6))
- **Binary search** = O(log n), but only on sorted data. ([Q11](#q11))
- **Merge** = always O(n log n), O(n) space; **Quick** = avg O(n log n), worst O(n²), in place. ([Q12](#q12))
- **BFS = queue (level by level)**, **DFS = recursion/stack (deep first)**; both O(n) / O(V+E). ([Q9](#q9), [Q10](#q10))
- **Graphs need a `visited` set** or BFS/DFS loops forever. ([Q10](#q10))
- **Two pointers / sliding window** turn O(n²) into O(n). ([Q13](#q13), [Q14](#q14))
- **Recursion** needs a base case; deep recursion can overflow the stack. ([Q15](#q15))
- **DP** = cache overlapping sub-problems: memoization (top-down) or tabulation (bottom-up). ([Q16](#q16))
- **Two Sum** = one pass + a Map; the classic O(n²) → O(n) trick. ([Q22](#q22))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at "solve it." They push on efficiency. Practice this chain out loud:

1. *"Solve Two Sum."* → brute force with two loops, O(n²).
2. *"Can you do better?"* → use a Map of seen values → O(n) time.
3. *"What's the trade-off?"* → O(n) extra space for the Map; time-for-space.
4. *"What if the list is sorted?"* → two pointers from both ends → O(1) extra space.
5. *"What if there's no valid pair?"* → return null/empty and say so; handle the edge case.

Always state the Big-O of your first idea, then improve it out loud. Showing the journey from brute force to optimal is exactly what earns a senior signal — for both remote and BD interviews.

[↑ Back to top](#toc)
