# Chapter 15 — Threads & Locks (প্রশ্ন 15.1 – 15.7)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। Code **Java threads** (Dart isolate / Python GIL নোট সহ)।
> এই chapter concurrency নিয়ে — একসাথে অনেক কাজ চললে যে সমস্যা (race condition, deadlock) হয় আর তা কীভাবে সামলায়।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: Databases](chapter14_databases.md) · [পরের: Moderate](chapter16_moderate.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
A. আগে Background (অবশ্যই পড়ুন): thread vs process, race condition,
   lock/synchronized, deadlock-এর ৪ শর্ত, Dart isolate, Python GIL
B. তারপর ৭টা প্রশ্ন:
   15.1  Thread vs Process     — পার্থক্য (concept)
   15.2  Context Switch        — দুই process-এর switch time মাপা (concept)
   15.3  Dining Philosophers   — deadlock সমস্যা ও সমাধান
   15.4  Deadlock-Free Class   — lock order দিয়ে deadlock এড়ানো
   15.5  Call In Order         — তিন thread পরপর (FooBarBaz)
   15.6  Synchronized Methods  — একই object-এ দুই synchronized method
   15.7  FizzBuzz              — multithreaded FizzBuzz
```

**প্রশ্নসমূহ:** [15.1 — Thread vs Process](#q15-1) · [15.2 — Context Switch](#q15-2) · [15.3 — Dining Philosophers](#q15-3) · [15.4 — Deadlock-Free Class](#q15-4) · [15.5 — Call In Order](#q15-5) · [15.6 — Synchronized Methods](#q15-6) · [15.7 — FizzBuzz](#q15-7)

প্রতিটা প্রশ্ন এই কাঠামোয়: **সহজ বাংলায় সমস্যা → মূল ধারণা (ASCII timeline/diagram) → সমাধান (ধাপে ধাপে) → Code (Java) → Dart isolate / Python GIL নোট → Common mistake → Follow-up।**

---
---

# Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

## ১. Thread আর Process — সহজ ছবি

একটা **process** হলো চলমান একটা program। এর নিজের **আলাদা memory** (address space) আছে। দুটো process আলাদা ঘরে আলাদা সংসারের মতো — একজনের জিনিস আরেকজন সরাসরি ছুঁতে পারে না।

একটা **thread** হলো একটা process-এর ভেতরের একটা "কাজের সুতো" — একটা process-এ একাধিক thread থাকতে পারে, আর তারা **একই memory ভাগ করে** (shared)।

```
Process A (নিজের memory)          Process B (নিজের memory)
┌─────────────────────────┐      ┌─────────────────────────┐
│  shared heap memory     │      │  shared heap memory     │
│   ┌──────┐ ┌──────┐     │      │   ┌──────┐               │
│   │Thread│ │Thread│ ... │      │   │Thread│ ...           │
│   │  1   │ │  2   │     │      │   │  1   │               │
│   └──────┘ └──────┘     │      │   └──────┘               │
│   (একই memory share করে)│      │                         │
└─────────────────────────┘      └─────────────────────────┘
   দুই process আলাদা memory — সরাসরি ছোঁয়া যায় না (IPC লাগে)
```

মূল কথা: **thread গুলো memory share করে** (তাই দ্রুত, কিন্তু বিপজ্জনক — race condition হয়), **process গুলো করে না** (তাই নিরাপদ, কিন্তু কথা বলতে IPC লাগে)।

## ২. কেন lock লাগে? — Race Condition

দুটো thread একই variable একসাথে বদলালে গন্ডগোল হয়। ধরুন `count = 0`, দুই thread প্রত্যেকে `count++` করছে। `count++` আসলে এক ধাপ নয় — **তিন ধাপ**: (১) পড়ো, (২) ১ যোগ করো, (৩) লিখো। OS যেকোনো সময় thread বদলে (switch) দিতে পারে:

```
শুরুতে count = 0।  আমরা চাই শেষে count = 2।

Thread A             Thread B            count
read count (0)                            0
                     read count (0)       0      ← B পুরোনো 0 পড়ে ফেলল!
add 1 (=1)                                0
write 1                                   1
                     add 1 (=1)           1
                     write 1              1      ← হারিয়ে গেল! (lost update)

ফলাফল: count = 1, অথচ হওয়ার কথা ছিল 2।  ← এটাই RACE CONDITION
```

সমস্যা: `count++` **atomic নয়** (মাঝপথে interrupt হতে পারে)। সমাধান: এই অংশটাকে (**critical section**) এমনভাবে রক্ষা করা যাতে একবারে একটা thread-ই ঢুকতে পারে।

## ৩. Lock / Mutex / synchronized — তালা দিয়ে রক্ষা

**Lock** (বা mutex = mutual exclusion) হলো একটা তালা। critical section-এ ঢোকার আগে thread তালা নেয়; বের হলে ছাড়ে। তালা একজনের হাতে থাকলে বাকিরা **অপেক্ষা** করে।

Java-তে দুই উপায়:

```java
// উপায় ১: synchronized keyword (object-এর intrinsic lock নেয়)
synchronized (lockObj) {
    count++;            // একবারে একটা thread
}

// উপায় ২: explicit Lock object (বেশি control)
lock.lock();
try { count++; }
finally { lock.unlock(); }   // unlock সবসময় finally-তে!
```

আরও কিছু tool:
- **semaphore** — তালা নয়, "permit"-এর গোনা। N permit থাকলে একসাথে N জন ঢুকতে পারে। (lock = ১-permit semaphore-এর মতো)।
- **wait() / notify()** — একটা thread-কে ঘুম পাড়ানো (`wait`) ও জাগানো (`notify`), যাতে busy-waiting না হয়।
- **volatile** — variable-টা সবসময় main memory থেকে পড়া হবে (cache নয়), তাই এক thread-এর লেখা আরেক thread সাথে সাথে দেখে।

## ৪. Deadlock — তালা দিয়ে আটকে যাওয়া

**Deadlock** হলো এমন অবস্থা যেখানে দুই (বা বেশি) thread একে অন্যের তালার জন্য চিরকাল অপেক্ষা করে — কেউই এগোয় না।

```
Thread 1 ধরে আছে  Lock A,  চাইছে  Lock B
Thread 2 ধরে আছে  Lock B,  চাইছে  Lock A

  Thread 1 ──ধরেছে──► Lock A
     ▲                  │
     │ চাইছে            │ চাইছে
     │                  ▼
  Lock B ◄──ধরেছে── Thread 2

কেউই ছাড়বে না, কেউই পাবে না → চিরকাল আটকে (deadlock cycle)
```

Deadlock হতে গেলে **চারটা শর্তই** একসাথে লাগে (Coffman conditions):
1. **Mutual exclusion** — resource একবারে একজনই ধরতে পারে।
2. **Hold and wait** — একটা ধরে রেখে আরেকটার জন্য অপেক্ষা করে।
3. **No preemption** — জোর করে কারো হাত থেকে resource কাড়া যায় না।
4. **Circular wait** — একটা গোল চক্র (1→2→...→1) তৈরি হয়।

> **নিয়ম:** এই ৪টার যেকোনো **একটা** ভাঙলেই deadlock হবে না। সবচেয়ে সহজ — **circular wait** ভাঙা: সব lock সবসময় **একই নির্দিষ্ট ক্রমে** নাও (15.4-এ এটাই করব)।

## ৫. Dart isolate — shared memory নেই, message passing

Dart-এ thread-এর বদলে **isolate**। প্রতিটা isolate-এর **নিজের আলাদা memory**, কেউ কারো variable ছুঁতে পারে না। তাই Dart-এ **race condition নেই, lock নেই, deadlock নেই** (shared state-এর কারণে) — কারণ shared state-ই নেই! Isolate-রা শুধু **message পাঠিয়ে** (`SendPort`/`ReceivePort`) কথা বলে। এটা অনেকটা process-এর মতো, thread নয়।

```dart
// Dart — দুটো isolate message দিয়ে কথা বলে (shared memory নয়)
final p = ReceivePort();
await Isolate.spawn((SendPort send) => send.send('হ্যালো'), p.sendPort);
print(await p.first);   // "হ্যালো"
```
> মনে রাখুন: Java thread = shared memory + lock; Dart isolate = আলাদা memory + message। তাই Java-র অনেক bug Dart-এ এমনিতেই হয় না।

## ৬. Python GIL — একসাথে এক thread-ই Python চালায়

Python (CPython)-এ একটা **GIL (Global Interpreter Lock)** আছে — একসাথে শুধু **একটা thread-ই** Python bytecode চালাতে পারে। তাই Python thread দিয়ে **CPU-bound** কাজে আসল parallelism পাওয়া যায় না (multiprocessing লাগে)। তবে **I/O-bound** কাজে (file/network অপেক্ষায়) thread উপকারী, কারণ অপেক্ষার সময় GIL ছেড়ে দেয়।
> GIL মানে এই নয় যে race condition নেই — `count++` এখনো atomic নয়, তাই Python-এও lock দরকার হয়।

---
---

<a id="q15-1"></a>
# 15.1 — Thread vs Process

> Topic: **Concept (OS basics)** · Difficulty: **Easy** · খুব common (warm-up, প্রায় সব interview-তে)

> **বইয়ের ভাষায়:** What's the difference between a thread and a process?

## প্রশ্নটা সহজ বাংলায়
Thread আর process — এই দুটোর পার্থক্য কী? এটা একটা theory প্রশ্ন; কোড লাগে না, কিন্তু পরিষ্কার ও গোছানো উত্তর দিতে হবে।

## মূল ধারণা
**Process** = চলমান একটা program-এর instance, যার নিজের **আলাদা memory (address space), resource (file handle, code, data, heap, stack)** আছে। OS process-গুলোকে একে অন্যের থেকে আলাদা (isolated) রাখে।

**Thread** = একটা process-এর ভেতরের একটা execution path। একই process-এর সব thread **memory (code, data, heap) ভাগ করে**, কিন্তু প্রত্যেকের **নিজের stack ও register/program counter** থাকে।

```
PROCESS (আলাদা সংসার)              THREAD (একই সংসারের সদস্য)
─────────────────────             ─────────────────────────
নিজের memory                      memory share করে (heap, data)
নিজের file/resource               process-এর resource share করে
একে অন্যের memory ছুঁতে পারে না   সরাসরি একই variable ছুঁতে পারে
যোগাযোগ: IPC (pipe, socket...)    যোগাযোগ: shared memory (সহজ)
তৈরি/switch ব্যয়বহুল (ভারী)       তৈরি/switch সস্তা (হালকা)
একটা crash করলে অন্যে বাঁচে       একটা thread crash → পুরো process পড়তে পারে
```

## সমাধান (গুছিয়ে বলার কাঠামো)
Interview-তে এই তিন দিক থেকে বলুন:
1. **Memory & isolation:** process আলাদা memory, thread shared memory। তাই thread-এ communication সহজ ও দ্রুত, কিন্তু **race condition**-এর ঝুঁকি (তাই lock লাগে); process নিরাপদ কিন্তু IPC লাগে।
2. **খরচ (overhead):** thread হালকা — তৈরি ও context switch দ্রুত (একই address space, তাই memory map বদলাতে হয় না)। process ভারী।
3. **স্বাধীনতা (independence):** process স্বাধীন; একটা crash করলে অন্যরা টেকে। একই process-এর thread একটা crash করলে গোটা process পড়ে যেতে পারে।

> এক বাক্যে: **thread একই memory ভাগ করা হালকা execution unit; process নিজের memory-ওয়ালা ভারী, স্বাধীন unit।**

## Code
এটা concept প্রশ্ন — কোড লাগে না। তবে বোঝাতে চাইলে: এক process-এ দুই thread একই variable দেখে।
```java
// দুই thread একই counter (shared memory) দেখছে — এটাই thread-এর বৈশিষ্ট্য
class Shared { int counter = 0; }   // process-এর heap-এ, সব thread দেখে
```

## Dart isolate / Python GIL নোট
- **Dart:** isolate আসলে thread নয় — process-এর কাছাকাছি (আলাদা memory)। তাই Dart-এ "thread share করে" কথাটা খাটে না; isolate **share করে না**, message পাঠায়।
- **Python:** thread আছে, কিন্তু GIL-এর কারণে একসাথে একটাই Python চালায় (CPU parallelism নেই)। process (multiprocessing) দিয়ে আসল parallelism পাওয়া যায়।

## Common mistake
- "thread আর process একই জিনিস" — না; মূল পার্থক্য **memory shared কিনা**।
- শুধু একটা দিক বলা; gold answer-এ **memory, overhead, isolation** তিন দিকই থাকে।
- thread switch process switch-এর চেয়ে দ্রুত — কেন তা না বলা (একই address space, TLB/cache flush কম)।

## Follow-up
- **Context switch কী, কত সময় লাগে?** → পরের প্রশ্ন 15.2।
- **কখন thread, কখন process বাছবেন?** → shared data বেশি ও communication ঘন ঘন হলে thread; isolation/নিরাপত্তা জরুরি হলে process।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q15-2"></a>
# 15.2 — Context Switch

> Topic: **Concept + পরিমাপ কৌশল** · Difficulty: **Medium** · Common

> **বইয়ের ভাষায়:** How would you measure the time spent in a context switch?

## প্রশ্নটা সহজ বাংলায়
**Context switch** হলো — CPU একটা process/thread চালানো থামিয়ে আরেকটায় যাওয়া। এই বদলে যেতে যে সময় লাগে, সেটা **কীভাবে মাপবেন**?

## মূল ধারণা
CPU যখন process A থেকে process B-তে যায়, OS-কে A-এর অবস্থা (register, program counter, memory map) **সংরক্ষণ** করে B-এরটা **পুনরুদ্ধার** করতে হয়। এই "save + restore" সময়টাই context switch overhead — এতে কোনো **useful কাজ** হয় না, তাই কম রাখা ভালো।

সমস্যা: এই switch খুবই দ্রুত (microsecond স্কেল) আর OS scheduler কখন switch করবে আমরা নিয়ন্ত্রণ করি না। তাই **সরাসরি মাপা কঠিন**। কৌশল: এমন একটা পরিস্থিতি বানাই যেখানে আমরা **জানি** switch হচ্ছে, আর "মোট সময়" থেকে "আসল কাজের সময়" বাদ দিই।

## সমাধান (ধাপে ধাপে — ping-pong কৌশল)
দুটো process নিই যারা একটা **pipe** দিয়ে একটা ছোট token পরস্পরকে পাঠায় (ping → pong → ping ...)। যখন P1 token পাঠিয়ে P2-এর উত্তরের জন্য block করে, OS বাধ্য হয়ে P1 → P2 switch করে। অর্থাৎ প্রতিবার token হাতবদলে অন্তত একটা context switch ঘটে।

```
P1  ──token──►  pipe  ──►  P2     (P1 block হয়, OS switch করে P2-তে)
P1  ◄──token──  pipe  ◄──  P2     (P2 block হয়, OS switch করে P1-তে)
   এক round-trip ≈ ২ context switch + সামান্য data পাঠানোর খরচ
```

ধাপ:
1. দুটো process pipe দিয়ে যুক্ত করো।
2. একটা টাইমার শুরু করে **অনেকবার (যেমন ১,০০,০০০ বার)** token ping-pong করাও।
3. মোট সময় মাপো → প্রতি round-trip গড় = মোট / সংখ্যা।
4. **ত্রুটি কমানো:** আলাদাভাবে data পাঠানো/পড়ার খরচ মেপে বাদ দাও; অবশিষ্টই মোটামুটি switch time। বহুবার চালিয়ে **গড়** নাও (একবারের noise এড়াতে)।

**সমস্যা ও সতর্কতা:**
- OS অন্য কাজেও switch করতে পারে — তাই দুটো process একই CPU core-এ **pin (affinity)** করলে মাপ পরিষ্কার হয়।
- token পাঠানোর I/O খরচও সময়ে ঢোকে — তাই সেটা আলাদা করে বাদ দিতে হয়।
- এতে যা পাই তা **আনুমানিক**; নিখুঁত নয়। সাধারণত switch time ~ ১–৫ microsecond।

## Code
এটা মূলত পদ্ধতির প্রশ্ন; ধারণা দেখানোর pseudo-Java:
```java
// ধারণা: ping-pong বহুবার করে গড় round-trip বের করা
long N = 100_000;
long start = System.nanoTime();
for (long i = 0; i < N; i++) {
    out.write(token);   // অন্য process-কে পাঠাও → আমি block → OS switch করে
    in.read(token);     // উত্তরের জন্য অপেক্ষা → আবার switch
}
long total = System.nanoTime() - start;
double perSwitch = (double) total / (N * 2);   // round-trip ≈ ২ switch
// এর থেকে আলাদাভাবে মাপা pure I/O খরচ বাদ দাও
```

## Dart isolate / Python GIL নোট
- **Dart:** isolate-এর মধ্যে message passing-ও pipe-এর মতো; তবে Dart দিয়ে OS-স্তরের switch মাপা সাধারণত করা হয় না — এটা OS-level প্রশ্ন।
- **Python:** GIL-এর কারণে thread switch-এর সাথে GIL হাতবদলও জড়িয়ে যায়, তাই মাপ আরও noisy; multiprocessing দিয়ে আসল process switch মাপা ভালো।

## Common mistake
- শুধু একবার মেপে উত্তর বলা — noise-এ ভুল হয়; **বহুবার চালিয়ে গড়** নিতে হবে।
- I/O/data পাঠানোর খরচ বাদ না দেওয়া (তাহলে switch time বেশি দেখাবে)।
- দুই process আলাদা core-এ থাকলে switch নাও হতে পারে — **CPU affinity** দিয়ে এক core-এ আনা জরুরি।

## Follow-up
- **এই overhead কমানো যায়?** → thread (process নয়) ব্যবহার (হালকা), অপ্রয়োজনীয় switch কমানো, batch করা।
- **Voluntary vs involuntary switch পার্থক্য?** → block হয়ে নিজে ছাড়া (voluntary) বনাম time-slice শেষে OS-এর জোরে কাড়া (involuntary)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q15-3"></a>
# 15.3 — Dining Philosophers

> Topic: **Deadlock — সমস্যা ও সমাধান** · Difficulty: **Medium–Hard** · খুব common (classic)

> **বইয়ের ভাষায়:** In the famous dining philosophers problem, a bunch of philosophers are sitting around a circular table with one chopstick between each of them. A philosopher needs both chopsticks to eat, and always picks up the left chopstick before the right one. A deadlock could potentially occur if all the philosophers reach for the left chopstick at the same time. Using threads and locks, implement a simulation of the dining philosophers problem that prevents deadlocks.

## প্রশ্নটা সহজ বাংলায়
গোল টেবিলে ৫ জন দার্শনিক (philosopher) বসা। প্রতি দুজনের মাঝে **একটা করে chopstick** — মোট ৫টা। খেতে হলে একজনের **দুই পাশের দুটো** chopstick লাগে। প্রতিজন আগে **বাঁ** পাশেরটা, পরে **ডান** পাশেরটা তোলে। সমস্যা: সবাই একসাথে বাঁ-টা তুলে ফেললে প্রত্যেকে ডান-টার জন্য চিরকাল অপেক্ষা করবে → **deadlock**। thread আর lock দিয়ে এমন simulation লেখো যাতে deadlock না হয়।

## মূল ধারণা — কেন deadlock হয় (circular wait)
প্রতিটা chopstick একটা **lock**। philosopher i বাঁ chopstick (lock i) তুলে ডান chopstick (lock i+1)-এর জন্য অপেক্ষা করে। সবাই একসাথে বাঁ ধরলে:

```
        P0 --হাতে--> C0(বাঁ),  চাইছে C1(ডান)
       /                              \
   P4 চাইছে C0                      P1 চাইছে C2(ডান), হাতে C1
      |                                |
   P4 হাতে C4                       ... গোল চক্র (circular wait) ...
       \                              /
        P3 হাতে C3, চাইছে C4 ... P2 ...

প্রত্যেকে বাঁ ধরে ডান-এর অপেক্ষায় → কেউ ছাড়বে না → DEADLOCK
```

এটাই Background-এর চার শর্তের **circular wait**। deadlock এড়াতে চক্রটা ভাঙতে হবে।

## সমাধান (ধাপে ধাপে)
দুটো জনপ্রিয় উপায় — দুটোই circular wait ভাঙে:

**উপায় ১ — Lock ordering (সবচেয়ে পরিষ্কার):** প্রতিটা chopstick-কে নম্বর দাও। প্রত্যেকে **সবসময় ছোট নম্বরের chopstick আগে** তোলে। তখন শেষ philosopher-এর জন্য ক্রম উল্টে যায় (সে আগে ডান, পরে বাঁ তোলে), ফলে গোল চক্র আর তৈরি হয় না।

**উপায় ২ — দুই chopstick atomically নাও (tryLock):** philosopher চেষ্টা করবে দুটো একসাথে পাওয়ার; বাঁ পেলেও ডান না পেলে **বাঁ-টা ছেড়ে দেবে** আর একটু পরে আবার চেষ্টা করবে। এতে "hold and wait" ভাঙে। (এতে livelock এড়াতে সামান্য random delay দরকার হতে পারে।)

নিচে **উপায় ১ (lock ordering)** দেখাচ্ছি — interview-তে এটাই সবচেয়ে নির্ভরযোগ্য উত্তর।

## Code
```java
// Java — Dining Philosophers, lock ordering দিয়ে deadlock-মুক্ত
import java.util.concurrent.locks.*;

class Philosophers {
    private final int n = 5;
    private final ReentrantLock[] chopsticks = new ReentrantLock[n];

    Philosophers() {
        for (int i = 0; i < n; i++) chopsticks[i] = new ReentrantLock();
    }

    void dine(int id) throws InterruptedException {
        int left = id;
        int right = (id + 1) % n;
        // মূল চাল: সবসময় ছোট নম্বরের lock আগে নাও → circular wait ভাঙে
        int first = Math.min(left, right);
        int second = Math.max(left, right);

        for (int round = 0; round < 3; round++) {   // ৩ বার খাবে (demo)
            chopsticks[first].lock();
            try {
                chopsticks[second].lock();
                try {
                    System.out.println("Philosopher " + id + " খাচ্ছে");
                } finally {
                    chopsticks[second].unlock();   // unlock সবসময় finally-তে
                }
            } finally {
                chopsticks[first].unlock();
            }
        }
    }

    public static void main(String[] args) {
        Philosophers table = new Philosophers();
        for (int i = 0; i < 5; i++) {
            final int id = i;
            new Thread(() -> {
                try { table.dine(id); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            }).start();
        }
    }
}
```
```java
// উপায় ২-এর মূল ধারণা (tryLock): বাঁ পেলেও ডান না পেলে বাঁ ছেড়ে দাও
if (left.tryLock()) {
    try {
        if (right.tryLock()) {        // দুটোই পেলে তবেই খাও
            try { /* eat */ } finally { right.unlock(); }
        }
    } finally { left.unlock(); }      // ডান না পেলে বাঁ ছেড়ে দিলাম → hold-and-wait ভাঙল
}
```

## Dart isolate / Python GIL নোট
- **Dart:** isolate shared memory ব্যবহার করে না, তাই এই classic deadlock Dart-এ "lock দিয়ে" হয় না। তবে সম্পদের জন্য পারস্পরিক অপেক্ষা (যেমন একে অন্যের message-এর জন্য) করলে logical deadlock হতে পারে — তখনও ক্রম/timeout লাগে।
- **Python:** `threading.Lock` দিয়ে একই deadlock তৈরি হয় (GIL এটা ঠেকায় না)। lock ordering সমাধান হুবহু কাজ করে।

## Common mistake
- `unlock()` `finally`-তে না রাখা — exception হলে lock চিরকাল আটকে থাকে।
- সব philosopher একই (left-then-right) ক্রমে lock নেওয়া — এতেই deadlock; **ক্রম uniform করতে হবে** (lock ordering)।
- উপায় ২-এ বাঁ ছেড়ে না দিয়ে শুধু retry — তাহলে আবার deadlock/livelock।

## Follow-up
- **livelock কী?** → সবাই বারবার ধরে-ছাড়ে কিন্তু কেউ এগোয় না; random backoff দিয়ে এড়ানো যায়।
- **starvation?** → কোনো philosopher কখনো chopstick না পেলে; fair lock (`new ReentrantLock(true)`) দিয়ে কমানো যায়।
- **arbiter/waiter সমাধান** → একজন "waiter"-এর অনুমতি ছাড়া কেউ chopstick তুলবে না (একসাথে ৪ জনকে অনুমতি = deadlock অসম্ভব)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q15-4"></a>
# 15.4 — Deadlock-Free Class

> Topic: **Lock ordering দিয়ে deadlock এড়ানো** · Difficulty: **Hard** · Medium-common

> **বইয়ের ভাষায়:** Design a class which provides a lock only if there are no possible deadlocks.

## প্রশ্নটা সহজ বাংলায়
এমন একটা class বানাও যেটা lock দেওয়ার আগে **নিশ্চিত করে** যে এই lock নিলে deadlock হতে পারে না। অর্থাৎ deadlock হওয়ার **সম্ভাবনাই** আগেভাগে আটকে দাও।

## মূল ধারণা — circular wait আটকালেই deadlock নেই
Background-এ দেখেছি deadlock-এর প্রাণ হলো **circular wait** (গোল চক্র)। যদি আমরা নিশ্চিত করি যে lock-গুলো নেওয়ার মধ্যে **কখনো গোল চক্র তৈরি হয় না**, তাহলে deadlock অসম্ভব।

দুই রকম strategy:

**Strategy A — Lock ordering (declare order আগেই ঠিক করা):** প্রতিটা thread আগেই ঘোষণা করে সে কোন কোন lock কোন ক্রমে নেবে। class একটা **graph** বানায়: "lock A-এর পরে lock B নেওয়া হয়" মানে A→B edge। নতুন order যোগ করার সময় যদি graph-এ **cycle** তৈরি হয় (DFS দিয়ে চেক), তাহলে সেই order **প্রত্যাখ্যান** করে — কারণ cycle = সম্ভাব্য deadlock।

```
order1: A → B → C   (A তারপর B তারপর C)
এখন কেউ চায়:  C → A   ?
graph:  A → B → C → A   ← cycle! → reject (নাহলে deadlock সম্ভব)
```

**Strategy B — global lock order মেনে চলা enforce করা:** সব lock-এর একটা ক্রম থাকবে; lock নেওয়ার সময় class চেক করে নতুন lock-টা thread-এর হাতে থাকা সবচেয়ে বড় ক্রমের lock-এর চেয়ে বড় কিনা। না হলে রাজি হয় না। এতে চক্র তৈরিই হতে পারে না।

## সমাধান (ধাপে ধাপে — Strategy A)
1. thread আগে `declare(threadId, order...)` দিয়ে জানায় কোন ক্রমে lock নেবে।
2. প্রতিটা পরপর জোড়া (A তারপর B)-এর জন্য graph-এ A→B edge যোগ করার চেষ্টা করো।
3. edge যোগ করার আগে DFS দিয়ে দেখো **cycle হয় কিনা**। হলে → এই declaration reject।
4. সব declaration valid হলেই তবে runtime-এ lock দেওয়া হবে; যেহেতu graph acyclic, deadlock অসম্ভব।

## Code
```java
// Java — declared lock-order graph থেকে cycle ধরে deadlock ঠেকানো (Strategy A)
import java.util.*;

class LockFactory {
    private final int n;                       // মোট lock সংখ্যা
    private final boolean[][] edges;           // edges[a][b] = "a-এর পরে b নেওয়া হয়"

    LockFactory(int count) {
        n = count;
        edges = new boolean[n][n];
    }

    // একটা thread তার lock-order ঘোষণা করছে। deadlock-মুক্ত হলে true।
    boolean declare(int[] order) {
        // অস্থায়ীভাবে edge যোগ করি
        for (int i = 1; i < order.length; i++) edges[order[i-1]][order[i]] = true;
        // এখন graph-এ cycle আছে কিনা চেক করি
        if (hasCycle()) {
            // cycle → এই declaration বিপজ্জনক → edge খুলে ফেলে reject করি
            for (int i = 1; i < order.length; i++) edges[order[i-1]][order[i]] = false;
            return false;
        }
        return true;   // acyclic → নিরাপদ
    }

    private boolean hasCycle() {
        int[] state = new int[n];   // 0=unvisited, 1=in-progress, 2=done
        for (int v = 0; v < n; v++)
            if (state[v] == 0 && dfs(v, state)) return true;
        return false;
    }

    private boolean dfs(int v, int[] state) {
        state[v] = 1;                       // এই path-এ আছি
        for (int u = 0; u < n; u++) {
            if (edges[v][u]) {
                if (state[u] == 1) return true;            // back-edge → cycle!
                if (state[u] == 0 && dfs(u, state)) return true;
            }
        }
        state[v] = 2;                       // সম্পূর্ণ
        return false;
    }
}
```
```java
// ব্যবহার:
LockFactory f = new LockFactory(4);
f.declare(new int[]{0, 1, 2});   // true  (0→1→2)
f.declare(new int[]{2, 0});      // false (2→0 দিলে 0→1→2→0 cycle হয়)
```

## Dart isolate / Python GIL নোট
- **Dart:** shared-memory lock নেই বলে এই pattern সরাসরি দরকার পড়ে না; তবে resource acquisition order-এর একই ধারণা isolate-জগতেও কাজে দেয়।
- **Python:** `threading.Lock`-এ একই cycle-detection ধারণা প্রযোজ্য; graph + DFS code হুবহু অনুবাদযোগ্য।

## Common mistake
- শুধু runtime-এ deadlock ধরার চেষ্টা (timeout/detection) — প্রশ্ন চায় **আগেই প্রতিরোধ (prevention)**, তাই lock-order graph approach সঠিক।
- cycle detection-এ `in-progress` (state 1) আর `done` (state 2) গুলিয়ে ফেলা — তাহলে ভুল cycle report হয়।
- reject করার সময় অস্থায়ী edge খুলে না ফেলা (graph নোংরা থেকে যায়)।

## Follow-up
- **runtime detection বনাম prevention?** → prevention (এই solution) deadlock হতেই দেয় না; detection হলে পরে ধরে recover করে (lock কেড়ে/thread মেরে)।
- **lock নম্বরে অর্ডার চাপালে?** → Strategy B; graph লাগে না, শুধু "বড় id-র lock পরে নাও" নিয়ম enforce করলেই চলে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q15-5"></a>
# 15.5 — Call In Order

> Topic: **Thread ordering (signaling)** · Difficulty: **Medium** · খুব common (LeetCode "Print FooBarBaz")

> **বইয়ের ভাষায়:** Suppose we have the following code:
> `class Foo { public Foo() {...} public void first() {...} public void second() {...} public void third() {...} }`
> The same instance of Foo will be passed to three different threads. ThreadA will call `first`, ThreadB will call `second`, and ThreadC will call `third`. Design a mechanism to ensure that `first` is called before `second`, and `second` is called before `third`.

## প্রশ্নটা সহজ বাংলায়
একই `Foo` object তিন thread-কে দেওয়া হবে। Thread A ডাকবে `first()`, B ডাকবে `second()`, C ডাকবে `third()`। কিন্তু OS যেকোনো ক্রমে thread চালাতে পারে। আমাদের নিশ্চিত করতে হবে output ক্রম সবসময় **first → second → third**, যে যখনই শুরু করুক না কেন।

## মূল ধারণা — অপেক্ষা করানো (signaling)
সমস্যা: thread গুলো যেকোনো ক্রমে আসতে পারে।

```
যদি কিছু না করি:
  C শুরু → third() চলে গেল  ← ভুল! first/second হয়নি
  A শুরু → first()
  B শুরু → second()
  output: third, first, second  (এলোমেলো)
```

সমাধান: পরের কাজটাকে **আগের কাজ শেষ হওয়া পর্যন্ত অপেক্ষা** করানো। প্রতিটা step শেষ হলে একটা "সংকেত" দেবে, পরেরটা সেই সংকেতের জন্য অপেক্ষা করবে। এর সবচেয়ে পরিষ্কার tool — **semaphore** (০ permit দিয়ে শুরু → অপেক্ষা; `release()` দিলে permit বাড়ে → পরের thread এগোয়)।

```
firstDone (semaphore, 0 permit)   secondDone (semaphore, 0 permit)

A: first() চালাও  → firstDone.release()  (এখন B এগোতে পারবে)
B: firstDone.acquire() (অপেক্ষা)  → second() → secondDone.release()
C: secondDone.acquire() (অপেক্ষা) → third()

ফলে যত এলোমেলোভাবেই শুরু হোক, ক্রম সবসময়: first → second → third
```

## সমাধান (ধাপে ধাপে)
1. দুটো semaphore নাও, দুটোই **০ permit** দিয়ে শুরু (মানে শুরুতেই `acquire` করলে block হবে)।
2. `first()`: কাজ করো, তারপর `firstDone.release()`।
3. `second()`: আগে `firstDone.acquire()` (first শেষ না হলে আটকে থাকবে), তারপর কাজ করে `secondDone.release()`।
4. `third()`: আগে `secondDone.acquire()`, তারপর কাজ করো।

## Code
```java
// Java — Semaphore দিয়ে ক্রম নিশ্চিত করা
import java.util.concurrent.Semaphore;

class Foo {
    private final Semaphore firstDone = new Semaphore(0);   // ০ permit → শুরুতে locked
    private final Semaphore secondDone = new Semaphore(0);

    public Foo() {}

    public void first(Runnable printFirst) {
        printFirst.run();        // "first" ছাপাও
        firstDone.release();     // সংকেত: first শেষ → second এগোতে পারবে
    }

    public void second(Runnable printSecond) throws InterruptedException {
        firstDone.acquire();     // first শেষ হওয়ার জন্য অপেক্ষা
        printSecond.run();       // "second" ছাপাও
        secondDone.release();    // সংকেত: second শেষ
    }

    public void third(Runnable printThird) throws InterruptedException {
        secondDone.acquire();    // second শেষ হওয়ার জন্য অপেক্ষা
        printThird.run();        // "third" ছাপাও
    }
}
```
```java
// বিকল্প: synchronized + wait/notify (semaphore ছাড়া)
class Foo2 {
    private int stage = 0;                       // কোন step পর্যন্ত হয়েছে
    public synchronized void first(Runnable r)  { r.run(); stage = 1; notifyAll(); }
    public synchronized void second(Runnable r) throws InterruptedException {
        while (stage < 1) wait();                // first শেষ না হলে অপেক্ষা
        r.run(); stage = 2; notifyAll();
    }
    public synchronized void third(Runnable r) throws InterruptedException {
        while (stage < 2) wait();                // second শেষ না হলে অপেক্ষা
        r.run();
    }
}
```
> `wait()` সবসময় `while` loop-এ রাখুন (`if` নয়) — spurious wakeup থেকে বাঁচতে।

## Dart isolate / Python GIL নোট
- **Dart:** একই isolate-এ event loop sequential, তাই এই সমস্যা সাধারণত হয় না; isolate-জুড়ে ক্রম দরকার হলে message/`Completer` দিয়ে chain করা হয় (A শেষ হলে B-কে message)।
- **Python:** `threading.Semaphore(0)` বা `threading.Event` দিয়ে হুবহু একই কাজ — `first` শেষে `event1.set()`, `second`-এ `event1.wait()`।

## Common mistake
- semaphore-কে ০-এর বদলে ১ permit দিয়ে শুরু করা — তাহলে অপেক্ষাই হয় না, ক্রম ভাঙে।
- `wait()` `if`-এ রাখা (`while` নয়) — spurious wakeup-এ ভুল হতে পারে।
- "thread গুলো ক্রমে শুরু হবেই" ধরে নেওয়া — হবে না; signaling-ই একমাত্র নিশ্চয়তা।

## Follow-up
- **N ধাপে generalize করো** → N-১টা semaphore, প্রতি step আগেরটার জন্য অপেক্ষা করে।
- **CountDownLatch দিয়ে?** → `latch1.countDown()` / `latch1.await()` — এক step-এর জন্য পরিষ্কার বিকল্প।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q15-6"></a>
# 15.6 — Synchronized Methods

> Topic: **synchronized-এর scope (intrinsic lock)** · Difficulty: **Easy–Medium** · Common (concept)

> **বইয়ের ভাষায়:** You are given a class with synchronized method A and a normal method B. If you have two threads in one instance of a program, can they both execute A at the same time? Can they execute A and B at the same time?

## প্রশ্নটা সহজ বাংলায়
একটা class-এ একটা `synchronized` method `A` আর একটা সাধারণ (non-synchronized) method `B` আছে। **একই instance**-এ দুই thread থাকলে:
1. দুজন কি একসাথে `A` চালাতে পারে?
2. একজন `A` আর আরেকজন `B` — একসাথে পারে?

## মূল ধারণা — synchronized মানে object-এর তালা নেওয়া
Java-তে instance method-এ `synchronized` মানে — method-টা চালানোর আগে thread ওই **object-এর intrinsic lock (monitor)** নেয়। একটা object-এর lock একসময় **একজনই** ধরতে পারে।

```
synchronized method A → ঢোকার আগে this object-এর lock চাই
normal method B       → কোনো lock লাগে না, যখন খুশি ঢোকে

         this object-এর একটাই lock (monitor)
              ┌───────────┐
   A চায় ───►│  LOCK      │◄─── A চায়  (একজন পেলে অন্যজন অপেক্ষা)
              └───────────┘
   B ─────────────────────────────► B-এর lock লাগেই না, এগিয়ে যায়
```

## সমাধান (দুই প্রশ্নের উত্তর)
**প্রশ্ন ১ — দুই thread একসাথে `A`?** → **না** (একই instance হলে)। `A` synchronized, দুজনেই `this`-এর একই lock চায়; একজন পেলে অন্যজন অপেক্ষা করে। তাই একই object-এ `A` একবারে একজনই চালায়।
> ব্যতিক্রম: যদি **আলাদা দুটো instance** হয়, তখন দুটো আলাদা lock — দুজন একসাথে নিজ নিজ object-এর `A` চালাতে পারে।

**প্রশ্ন ২ — একজন `A`, আরেকজন `B`?** → **হ্যাঁ, পারে।** `B` synchronized নয়, তাই lock-ই চায় না; `A`-এর lock তাকে আটকায় না। দুজন একসাথে একই object-এ `A` ও `B` চালাতে পারে। (এজন্যই যদি `B`-ও shared data ছোঁয়, `B`-কেও synchronize করা উচিত — নাহলে race condition।)

```
সারাংশ (একই instance):
  A + A  →  না (একই lock-এর জন্য লড়াই)
  A + B  →  হ্যাঁ (B-এর lock লাগে না)
  আলাদা instance হলে A + A → হ্যাঁ
```

## Code
```java
// Java — দেখানোর জন্য
class MyClass {
    public synchronized void A() {   // this object-এর lock নেয়
        // shared data ছোঁয়...
    }
    public void B() {                // কোনো lock নেয় না
        // ...
    }
}

// thread1: obj.A();   thread2: obj.A();  → একসাথে নয় (একই obj)
// thread1: obj.A();   thread2: obj.B();  → একসাথে হতে পারে
// thread1: objX.A();  thread2: objY.A(); → একসাথে হতে পারে (আলাদা obj)
```
```java
// static synchronized আলাদা: এটা CLASS-এর lock নেয় (MyClass.class), instance-এর নয়
class C {
    public static synchronized void S() { }  // সব instance-এর জন্য একটাই class-lock
}
```

## Dart isolate / Python GIL নোট
- **Dart:** `synchronized` keyword নেই; isolate আলাদা memory ব্যবহার করে, তাই এই lock-ভিত্তিক প্রশ্ন প্রযোজ্য নয়। একই isolate-এ কোড sequential, তাই দুটো method "সত্যিকারে একসাথে" চলেই না।
- **Python:** `synchronized` keyword নেই; নিজে `threading.Lock` নিতে হয়। সব method একই lock নিলে A+A আর A+B (যদি B-ও সেই lock নেয়) দুটোই serialize হবে। GIL bytecode-স্তরে রক্ষা দেয়, কিন্তু method-স্তরের mutual exclusion নয়।

## Common mistake
- ভাবা যে `synchronized` "পুরো class" lock করে — না, সাধারণ method-এ এটা **ওই instance (`this`)**-এর lock নেয়।
- `A` synchronized বলে ভাবা `B`-ও নিরাপদ — না, `B` lock নেয় না, তাই `A`-এর সাথে একসাথে চলে; shared data হলে bug।
- instance vs static synchronized গুলিয়ে ফেলা (একটা object lock, আরেকটা class lock — আলাদা)।

## Follow-up
- **`B`-কেও safe করতে চাইলে?** → `B`-কেও synchronized করো, বা একই lock object ব্যবহার করো।
- **শুধু কিছু অংশ rক্ষা করতে চাই?** → পুরো method নয়, `synchronized(lock){...}` block দিয়ে কেবল critical section মোড়ো।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q15-7"></a>
# 15.7 — FizzBuzz

> Topic: **Multithreaded coordination** · Difficulty: **Medium** · খুব common (LeetCode "Multithreaded FizzBuzz")

> **বইয়ের ভাষায়:** In the classic problem FizzBuzz, you are told to print the numbers from 1 to n. However, when the number is divisible by 3, print "Fizz". When it is divisible by 5, print "Buzz". When it is divisible by 3 and 5, print "FizzBuzz". In this problem, you are asked to do this in a multithreaded way. Implement a multithreaded version of FizzBuzz with four threads. One thread checks for divisibility of 3 and prints "Fizz". Another thread is responsible for divisibility of 5 and prints "Buzz". A third thread is responsible for divisibility of 3 and 5 and prints "FizzBuzz". A fourth thread does the numbers.

## প্রশ্নটা সহজ বাংলায়
সাধারণ FizzBuzz: ১ থেকে n পর্যন্ত — ৩ দিয়ে ভাগ গেলে "Fizz", ৫ দিয়ে গেলে "Buzz", দুটো দিয়েই গেলে "FizzBuzz", নাহলে সংখ্যাটাই। এবার **৪টা thread** দিয়ে করতে হবে: একটা শুধু "Fizz" (÷3), একটা "Buzz" (÷5), একটা "FizzBuzz" (÷15), আর একটা শুধু সংখ্যা ছাপায়। সমস্যা — চারজনে মিলে কিন্তু output **সঠিক ক্রমে (১,২,Fizz,৪,Buzz,...)** আসতে হবে।

## মূল ধারণা — একটাই কারেন্ট number, পালা করে কাজ
চারজনই একটা shared `current` number দেখছে। প্রতিটা thread একটা loop-এ ঘোরে আর দেখে — **এই number-টা কি আমার?** না হলে অপেক্ষা করে; হ্যাঁ হলে ছাপিয়ে number বাড়িয়ে অন্যদের জাগায়।

```
current = 1
number thread :  current%3≠0 ও %5≠0 হলে → আমার → ছাপাও number, current++
fizz   thread :  current%3==0 ও %5≠0  হলে → আমার → "Fizz", current++
buzz   thread :  current%5==0 ও %3≠0  হলে → আমার → "Buzz", current++
fizzbuzz thread: current%15==0         হলে → আমার → "FizzBuzz", current++

প্রতিটা thread: "আমার পালা?" → না হলে wait → হ্যাঁ হলে কাজ + notifyAll
```

এতে একবারে যে number-এর শর্ত মেলে কেবল সেই thread কাজ করে, বাকিরা অপেক্ষা করে। তাই ক্রম ঠিক থাকে।

## সমাধান (ধাপে ধাপে)
1. একটা shared monitor object আর `current = 1` রাখো।
2. প্রতিটা thread একটা loop-এ: lock নাও → "আমার number নয় কিন্তু এখনো শেষ হয়নি" হলে `wait()` → আমার হলে print করো, `current++`, `notifyAll()`।
3. `current > n` হলে সব thread loop থেকে বেরিয়ে যাবে (আর কেউ আটকে যেন না থাকে — তাই শেষেও `notifyAll`)।

## Code
```java
// Java — 4-thread FizzBuzz, synchronized + wait/notify
class FizzBuzz {
    private final int n;
    private int current = 1;        // shared
    private final Object lock = new Object();

    FizzBuzz(int n) { this.n = n; }

    // একটা thread-এর সাধারণ কাঠামো: শর্ত মিললে print, নাহলে অপেক্ষা
    private void run(java.util.function.IntPredicate mine, java.util.function.IntConsumer print)
            throws InterruptedException {
        while (true) {
            synchronized (lock) {
                while (current <= n && !mine.test(current)) lock.wait();  // আমার পালা নয় → অপেক্ষা
                if (current > n) { lock.notifyAll(); return; }            // শেষ → বেরিয়ে যাও
                print.accept(current);                                   // আমার কাজ
                current++;
                lock.notifyAll();                                        // অন্যদের জাগাও
            }
        }
    }

    void number()   throws InterruptedException { run(x -> x%3!=0 && x%5!=0, x -> System.out.println(x)); }
    void fizz()     throws InterruptedException { run(x -> x%3==0 && x%5!=0, x -> System.out.println("Fizz")); }
    void buzz()     throws InterruptedException { run(x -> x%5==0 && x%3!=0, x -> System.out.println("Buzz")); }
    void fizzbuzz() throws InterruptedException { run(x -> x%15==0,          x -> System.out.println("FizzBuzz")); }

    public static void main(String[] args) {
        FizzBuzz fb = new FizzBuzz(15);
        new Thread(() -> safe(fb::number)).start();
        new Thread(() -> safe(fb::fizz)).start();
        new Thread(() -> safe(fb::buzz)).start();
        new Thread(() -> safe(fb::fizzbuzz)).start();
    }

    interface Task { void run() throws InterruptedException; }
    static void safe(Task t) {
        try { t.run(); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }
}
```
> মূল চাল: প্রতিটা thread শুধু **তার শর্তের** number-গুলোতেই কাজ করে; বাকি সময় `wait()`-এ ঘুমায়। `current` একটাই বলে output ক্রম স্বয়ংক্রিয়ভাবে ঠিক থাকে।

## Dart isolate / Python GIL নোট
- **Dart:** এক isolate-এ async দিয়ে সহজেই sequential FizzBuzz লেখা যায়; "৪ thread" ধারণাটা isolate-এ অপ্রয়োজনীয় কারণ shared `current` নেই। চাইলে চারটা isolate বানিয়ে message দিয়ে turn pass করা যায়, কিন্তু তা জটিল ও অপ্রয়োজনীয়।
- **Python:** `threading.Condition` দিয়ে হুবহু এই কাঠামো — `with cond:` → `cond.wait()` / `cond.notify_all()`। GIL থাকলেও wait/notify দিয়ে coordination একইভাবে লাগে।

## Common mistake
- `wait()`-কে `if`-এ রাখা (`while` নয়) — spurious wakeup-এ ভুল thread print করতে পারে।
- শেষে `notifyAll()` না দেওয়া — `current > n` হলেও কিছু thread `wait()`-এ চিরকাল আটকে থাকতে পারে (hang)।
- `current` কে lock-এর বাইরে পড়া/বাড়ানো — race condition; পুরো check+print+increment একই `synchronized` block-এ রাখুন।
- "FizzBuzz" thread-এর শর্তে `%15` ভুলে `%3 && %5` আলাদা thread-এ ঢুকতে দেওয়া — তখন ১৫-এ Fizz+Buzz দুবার ছাপবে।

## Follow-up
- **আরও scalable চাই?** → `BlockingQueue`/turn-token দিয়ে busy-wait কমানো, বা single producer অনেক rule consumer।
- **ক্রম জরুরি না হলে?** → কাজ ভাগ করে parallel করা সহজ; কিন্তু FizzBuzz-এ ক্রম জরুরি বলেই coordination লাগে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 15 — সারসংক্ষেপ ও Concurrency Cheat Sheet

| # | প্রশ্ন | মূল ধারণা / technique | ধরন |
|---|---|---|---|
| 15.1 | Thread vs Process | shared memory vs আলাদা memory; overhead; isolation | Concept |
| 15.2 | Context Switch | ping-pong + বহুবার গড় + I/O বাদ | Concept + পরিমাপ |
| 15.3 | Dining Philosophers | lock ordering (বা tryLock) → circular wait ভাঙা | Deadlock |
| 15.4 | Deadlock-Free Class | lock-order graph + cycle detection (DFS) → prevention | Deadlock |
| 15.5 | Call In Order | semaphore/wait-notify দিয়ে signaling | Ordering |
| 15.6 | Synchronized Methods | synchronized = `this`-এর intrinsic lock | Concept |
| 15.7 | FizzBuzz | shared `current` + wait/notify, "আমার পালা?" | Coordination |

### "এটা দেখলে → এটা ভাবো" (signal → technique)
```
shared data একসাথে বদলানো / lost update     →  lock / synchronized (critical section)
দুই thread একে অন্যের lock-এর অপেক্ষায়         →  deadlock; lock ordering দিয়ে ভাঙো
deadlock আগেই ঠেকাও                          →  lock-order graph + cycle (DFS) detection
thread গুলো পরপর/নির্দিষ্ট ক্রমে চালাতে হবে     →  semaphore / wait-notify / CountDownLatch
"আমার পালা কিনা" দেখে কাজ                    →  shared state + wait()/notifyAll() loop
busy-waiting এড়াতে                          →  wait/notify বা semaphore (CPU spin নয়)
Dart-এ concurrency                          →  isolate + message passing (lock নেই)
Python CPU parallelism                       →  multiprocessing (GIL-এর কারণে thread নয়)
```

### এই chapter-এর ৫টা সোনার নিয়ম
1. **Thread = shared memory** (দ্রুত কিন্তু race condition-এর ঝুঁকি); **process = আলাদা memory** (নিরাপদ কিন্তু IPC লাগে)।
2. **Critical section**-কে lock/`synchronized` দিয়ে রক্ষা করো; `unlock()` সবসময় `finally`-তে।
3. **Deadlock-এর ৪ শর্তের একটা ভাঙো** — সবচেয়ে সহজ **lock ordering** (circular wait ভাঙে)।
4. **`wait()` সবসময় `while` loop-এ**, আর কাজ শেষে **`notifyAll()`** — নাহলে hang/spurious-wakeup bug।
5. **Dart isolate**-এ shared state নেই বলে lock/deadlock নেই (message passing); **Python GIL** parallelism সীমিত করে কিন্তু race condition মুছে দেয় না।

> **পরের ধাপ:** [Chapter 16 — Moderate](chapter16_moderate.md) (16.1–16.26), যেখানে নানা ধরনের mixed problem একসাথে আসে।
</content>
</invoke>
