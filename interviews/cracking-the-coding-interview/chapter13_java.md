# Chapter 13 — Java (প্রশ্ন 13.1 – 13.8)

> **Cracking the Coding Interview — বাংলা গাইড**
> ব্যাখ্যা **বাংলায়**, technical term **ইংরেজিতে**। এই chapter-এ code **Java**-তে — প্রতিটা concept-এ **Dart-এর সাথে মিল/অমিল** নোট করা আছে (পাঠক Flutter/Dart জানেন)।
> এগুলো মূলত **knowledge / concept** প্রশ্ন — language কীভাবে কাজ করে সেটা বোঝা।

> [মূল Index](README.md) · [Foundation](chapter00_foundation.md) · [আগের: C & C++](chapter12_c_cpp.md) · [পরের: Databases](chapter14_databases.md)

---

<a id="toc"></a>
## এই Chapter-এর সূচি

```
আগে Background (অবশ্যই পড়ুন): JVM, garbage collection, everything-is-object, Java vs Dart
তারপর ৮টা প্রশ্ন:
   13.1  Private Constructor   — private constructor inheritance-এ কী প্রভাব ফেলে
   13.2  Return from Finally   — try/finally-তে return থাকলে কী হয়
   13.3  Final, Finally, Finalize — তিনটার পার্থক্য
   13.4  Generics vs Templates — Java generics বনাম C++ templates
   13.5  TreeMap/HashMap/LinkedHashMap — পার্থক্য ও কখন কোনটা
   13.6  Object Reflection     — reflection কী ও কেন
   13.7  Lambda Expressions    — lambda দিয়ে list filter/group
   13.8  Lambda Random         — lambda দিয়ে random subset
```

**প্রশ্নসমূহ:** [13.1 — Private Constructor](#q13-1) · [13.2 — Return from Finally](#q13-2) · [13.3 — Final, Finally, Finalize](#q13-3) · [13.4 — Generics vs Templates](#q13-4) · [13.5 — TreeMap, HashMap, LinkedHashMap](#q13-5) · [13.6 — Object Reflection](#q13-6) · [13.7 — Lambda Expressions](#q13-7) · [13.8 — Lambda Random](#q13-8)

প্রতিটা প্রশ্ন এই কাঠামোয়: **বইয়ের ভাষায় → সহজ বাংলায় → মূল ধারণা/উত্তর (ধাপে ধাপে) → Code (Java) → Dart-এর সাথে মিল/অমিল → Common mistake → Follow-up।**

---
---

# Background — প্রশ্নে যাওয়ার আগে এগুলো বুঝুন

এই chapter-এর প্রশ্নগুলো coding-এর চেয়ে **Java কীভাবে কাজ করে** সেটা বোঝার। তাই আগে কয়েকটা মূল ধারণা পরিষ্কার করি। আপনি যেহেতু Dart জানেন, প্রতিটা জায়গায় Dart-এর সাথে তুলনা দেওয়া হলো — অনেক কিছুই চেনা মনে হবে।

## ১. JVM — Java কোথায় চলে

Java কোড সরাসরি machine code-এ compile হয় না। প্রথমে **bytecode** (`.class` ফাইল) বানে, তারপর সেটা চলে **JVM (Java Virtual Machine)**-এর ওপর। তাই "write once, run anywhere" — যেকোনো OS-এ যদি JVM থাকে, একই bytecode চলবে।

```
.java  ──javac──►  .class (bytecode)  ──JVM──►  চলে (যেকোনো OS-এ)
 source            platform-independent          JVM machine code-এ অনুবাদ করে
```

> **Dart তুলনা:** Dart-ও দুইভাবে চলে — development-এ **JIT** (Dart VM, hot reload-এর জন্য), production-এ **AOT** (native machine code, Flutter release build)। ধারণাটা কাছাকাছি: একটা intermediate layer/VM থাকে।

## ২. Garbage Collection (GC) — memory নিজে নিজে মুক্ত হয়

Java-তে আপনি `new` দিয়ে object বানান, কিন্তু **মুছতে হয় না**। কোনো object-এর দিকে আর কোনো reference না থাকলে **garbage collector** নিজে থেকে তার memory ফেরত নেয়। C/C++-এর মতো `free`/`delete` করতে হয় না।

> **Dart তুলনা:** Dart-ও fully garbage-collected। দুটো ভাষাতেই memory leak-এর চিন্তা C++-এর চেয়ে অনেক কম — কিন্তু "reference ধরে রাখলে GC মুছতে পারে না" এই নিয়ম দুটোতেই খাটে (Flutter-এ listener dispose না করলে leak)।

## ৩. সবকিছুই Object (প্রায়)

Java-তে দুই রকম type:
- **Primitive:** `int`, `double`, `boolean`, `char`, `long` ... — এগুলো object নয়, সরাসরি value।
- **Reference/Object:** `String`, `Integer`, array, আপনার বানানো class — সব `Object`-এর descendant।

primitive কে object বানানোর জন্য **wrapper class** আছে: `int → Integer`, `double → Double`। Generics-এ (যেমন `List<Integer>`) শুধু object চলে, primitive চলে না — তাই **autoboxing** (`int` ↔ `Integer` স্বয়ংক্রিয় রূপান্তর) ঘটে।

> **Dart তুলনা:** Dart-এ **সবকিছুই object**, এমনকি `int`, `double`, `bool`-ও (`Object` থেকে আসা)। তাই Dart-এ wrapper class বা autoboxing-এর ঝামেলা নেই — `List<int>` সরাসরি কাজ করে। এটা Java-র চেয়ে পরিষ্কার।

## ৪. Java vs Dart — মূল পার্থক্য (এক নজরে)

| বিষয় | Java | Dart |
|---|---|---|
| primitive vs object | আলাদা (`int` vs `Integer`) | সব object (`int`-ও object) |
| run কোথায় | JVM (bytecode) | Dart VM (JIT) / native (AOT) |
| memory | garbage-collected | garbage-collected |
| null safety | পুরোনো Java-তে নেই (`null` যেকোনো object-এ); newer-এ `Optional`/annotation | ভাষাগতভাবে built-in (`String?` vs `String`) |
| generics | আছে, কিন্তু **type erasure** (runtime-এ মুছে যায়) | আছে, runtime-এও **reified** (type থাকে) |
| ক্লাস উত্তরাধিকার | single inheritance + `interface` | single inheritance + `mixin` + `interface` |
| lambda | `->` (Java 8+), functional interface দরকার | first-class function, native closure |
| constructor | class-নামেই method, return type নেই | নাম দেওয়া যায় (`Foo.named()`), `factory` আছে |

> এই পার্থক্যগুলো মাথায় রাখলে নিচের প্রশ্নগুলো অনেক সহজ লাগবে — বেশিরভাগ উত্তরই "Dart-এ যেমন, Java-তে একটু অন্যরকম, এই কারণে"।

---
---

<a id="q13-1"></a>
# 13.1 — Private Constructor

> Topic: **Class design / Inheritance** · Difficulty: **Easy** · মোটামুটি common (concept warm-up)

> **বইয়ের ভাষায়:** In terms of inheritance, what is the effect of keeping a constructor private?

## প্রশ্নটা সহজ বাংলায়
একটা class-এর constructor-কে `private` বানালে — উত্তরাধিকার (inheritance)-এর দিক থেকে এর কী প্রভাব পড়ে? অর্থাৎ অন্য class কি এটাকে `extends` করতে পারবে? object বানাতে পারবে?

## মূল ধারণা / উত্তর (ধাপে ধাপে)

**ধাপ ১ — constructor কী করে।** subclass-এর object বানানোর সময় Java প্রথমে parent-এর constructor ডাকে (`super(...)`)। এটা না ডাকলে subclass-এর object তৈরিই হয় না।

**ধাপ ২ — private মানে শুধু ভেতরে।** `private` member শুধু **ওই class-এর ভেতর থেকেই** access করা যায়। তাই parent-এর constructor private হলে subclass সেই `super()` ডাকতে পারে না।

**ধাপ ৩ — উপসংহার।**
> Private constructor মানে: class-টা **সরাসরি বাইরের কেউ instantiate করতে পারবে না**, এবং সাধারণভাবে **subclass করা যাবে না** (কারণ subclass parent-এর private constructor ডাকতে পারে না)।

**ব্যতিক্রম (গুরুত্বপূর্ণ nuance):** যদি **nested (inner) class** ওই একই outer class-এর ভেতরে থাকে, সে কিন্তু private constructor দেখতে পায় — তাই একই enclosing class-এর ভেতরে subclass করা **সম্ভব**। বাইরে থেকে নয়।

**তাহলে private constructor কখন ব্যবহার করি?**

```
1. Singleton          → একটাই instance; constructor private রেখে getInstance() দিয়ে দিই
2. Utility class       → সব static method (যেমন Math); object বানানোরই দরকার নেই
3. Factory method only → object শুধু static factory দিয়ে বানাও, new দিয়ে নয়
4. inheritance বন্ধ    → কেউ যেন subclass না করতে পারে
```

## Code (Java)

```java
// Singleton — private constructor-এর সবচেয়ে common ব্যবহার
public class Database {
    private static Database instance;     // একটাই instance

    private Database() { }                // বাইরের কেউ new করতে পারবে না

    public static Database getInstance() {
        if (instance == null) {
            instance = new Database();     // শুধু ভেতর থেকে বানানো যায়
        }
        return instance;
    }
}

// বাইরে থেকে:
// Database d = new Database();        // [হবে না] compile error (private constructor)
// Database d = Database.getInstance(); // [ঠিক] এভাবেই

// Utility class — instantiate করার দরকারই নেই
public class MathUtils {
    private MathUtils() { }            // কেউ যেন object না বানায়
    public static int square(int x) { return x * x; }
}
```

## Dart-এর সাথে মিল/অমিল

Dart-এ constructor-কে আলাদা করে `private` বানানোর syntax নেই, কিন্তু একই কাজ হয় **নাম দিয়ে** (`_` prefix = library-private):

```dart
class Database {
  static final Database _instance = Database._internal();
  Database._internal();          // _ দিয়ে শুরু → library-এর বাইরে দেখা যায় না
  factory Database() => _instance; // singleton
}
```

| | Java | Dart |
|---|---|---|
| private করার উপায় | `private` keyword | নামের শুরুতে `_` (library-private) |
| privacy-র scope | class-level (একই class) | **library/file-level** (একই file) |
| singleton idiom | private ctor + `getInstance()` | `factory` constructor + static instance |

> বড় পার্থক্য: Dart-এ privacy **file-level**, class-level নয়। তাই একই file-এর অন্য class `_internal()` দেখতে পায় — Java-তে যেমন একই class-এর ভেতরই কেবল দেখা যায়।

## Common mistake
- "private constructor মানে কোনোভাবেই subclass হবে না" — পুরোপুরি ঠিক নয়; **একই enclosing class-এর nested class** subclass করতে পারে।
- Singleton-কে thread-safe ভাবা — উপরের naive `getInstance()` multi-thread-এ দুটো instance বানাতে পারে (Ch15-এ আলোচনা; সমাধান: `synchronized` বা eager init)।

## Follow-up
- **"Singleton thread-safe কীভাবে করবে?"** → `synchronized getInstance()`, অথবা static initializer-এ eager init, অথবা enum singleton।
- **"private constructor থাকলে object কীভাবে বানাবে?"** → static factory method / `getInstance()` দিয়ে, যা class-এর ভেতরেই।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-2"></a>
# 13.2 — Return from Finally

> Topic: **Exception handling / control flow** · Difficulty: **Easy–Medium** · common (tricky প্রশ্ন)

> **বইয়ের ভাষায়:** In Java, does the `finally` block get executed if we insert a `return` statement inside the `try` block of a try-catch-finally?

## প্রশ্নটা সহজ বাংলায়
`try` block-এর ভেতরে `return` লিখলে — function তো সেখানেই ফিরে যাওয়ার কথা। তাহলে কি `finally` block-টা **তবুও চলবে**? নাকি skip হয়ে যাবে?

## মূল ধারণা / উত্তর (ধাপে ধাপে)

**মূল উত্তর:**
> **হ্যাঁ, `finally` block প্রায় সবসময় চলবে — এমনকি `try`-তে `return` থাকলেও।** `finally`-র পুরো উদ্দেশ্যই হলো "যাই ঘটুক, এটা চলবে" — তাই cleanup (file বন্ধ, connection ছাড়া) এখানে রাখা হয়।

**চলার ক্রম (`try`-তে return থাকলে):**

```
1. try block চলে, return value হিসাব হয় (একটা জায়গায় জমা রাখা হয়)
2. ঠিক return করার আগে → finally block চলে
3. তারপর জমিয়ে রাখা value return হয়
```

**কখন finally চলে না (একমাত্র ব্যতিক্রম):**

```
- System.exit() ডাকলে        → পুরো JVM থেমে যায়, finally চলে না
- JVM crash / infinite loop / daemon thread মারা গেলে
- শক্তি চলে গেলে :)
```

**একটা ফাঁদ (interviewer এটাই দেখতে চায়):** যদি `finally` block নিজেও `return` করে, সেটা `try`-র return-কে **override** করে দেয়! এজন্য `finally`-তে `return` লেখা bad practice।

```
try { return 1; } finally { return 2; }   →  function ফেরত দেয় 2 (try-র 1 হারিয়ে গেল!)
```

## Code (Java)

```java
public static int test() {
    try {
        System.out.println("try চলছে");
        return 1;                  // value 1 জমা হলো
    } finally {
        System.out.println("finally চলছে");  // return-এর আগেই চলবে
    }
}
// আউটপুট:
//   try চলছে
//   finally চলছে
//   (return করে 1)

public static int trap() {
    try {
        return 1;
    } finally {
        return 2;                  // [খারাপ] এটা try-র 1 কে override করে → ফেরত দেয় 2
    }
}
```

## Dart-এর সাথে মিল/অমিল

Dart-এ `try` / `catch` / `finally` হুবহু একই ভাবে কাজ করে — `finally`-র block কে বলে `finally` (Java-র মতোই)।

```dart
int test() {
  try {
    return 1;          // value জমা
  } finally {
    print('finally চলছে');   // return-এর আগে চলে — Java-র মতোই
  }
}
```

| | Java | Dart |
|---|---|---|
| keyword | `try` / `catch` / `finally` | একই |
| return-এও finally চলে? | হ্যাঁ | হ্যাঁ |
| finally থেকে return override | পারে (bad) | **Dart-এ finally থেকে `return` করলে warning/error-prone**, একই আচরণ |
| exception type | `catch (Type e)` | `on Type catch (e)` |

> মূল আচরণ একই — দুটো ভাষাতেই `finally` "যাই হোক চলবে"। Dart-এ catch syntax একটু আলাদা: `on FormatException catch (e)`।

## Common mistake
- ধরে নেওয়া যে `try`-তে `return` থাকলে `finally` skip হয় — **চলে**।
- `finally`-তে `return`/`throw` লেখা — original return বা exception **গিলে ফেলে** (swallow করে), bug-এর উৎস।

## Follow-up
- **"finally কখন চলে না?"** → `System.exit()`, JVM crash, infinite loop।
- **"try-with-resources কী?"** → Java 7+; `AutoCloseable` resource নিজে নিজে বন্ধ হয়, manual finally লাগে না।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-3"></a>
# 13.3 — Final, Finally, Finalize

> Topic: **Keyword / terminology** · Difficulty: **Easy** · খুব common (confusion প্রশ্ন)

> **বইয়ের ভাষায়:** What is the difference between `final`, `finally`, and `finalize()`?

## প্রশ্নটা সহজ বাংলায়
নামগুলো প্রায় একরকম, কিন্তু তিনটা সম্পূর্ণ আলাদা জিনিস। `final` (keyword), `finally` (block), আর `finalize()` (method) — এদের পার্থক্য কী?

## মূল ধারণা / উত্তর (ধাপে ধাপে)

### final — "আর বদলানো যাবে না" (keyword)
`final` তিন জায়গায় ব্যবহার হয়, প্রতিটার মানে "আর পরিবর্তন নয়":

```
final variable  →  একবার assign করলে আর বদলানো যায় না (constant)
final method    →  subclass এই method override করতে পারবে না
final class     →  এই class কে কেউ extends করতে পারবে না (যেমন String)
```

### finally — "যাই হোক চলবে" (block)
try-catch-এর সাথে আসা block, যা **exception হোক বা না হোক চলে** (13.2 দেখুন)। Cleanup কোডের জায়গা।

### finalize() — "মুছে ফেলার আগে শেষ ডাক" (method)
`Object` class-এর method, যা **garbage collector object মুছে ফেলার ঠিক আগে** ডাকত (cleanup-এর সুযোগ দিতে)।

> **সতর্কতা:** `finalize()` **deprecated** (Java 9+) এবং unreliable — GC কখন চালাবে বা আদৌ চালাবে কিনা তার কোনো গ্যারান্টি নেই। আধুনিক code-এ ব্যবহার করা হয় না; পরিবর্তে try-with-resources / `Cleaner` ব্যবহার করুন।

### এক টেবিলে

| | কী | কোথায় | কাজ |
|---|---|---|---|
| `final` | keyword (modifier) | variable/method/class-এর আগে | পরিবর্তন/override/extends বন্ধ |
| `finally` | block | try-catch-এর সাথে | যাই হোক cleanup চলবে |
| `finalize()` | method | object-এর ওপর (deprecated) | GC মুছে ফেলার আগে শেষ cleanup |

## Code (Java)

```java
final int MAX = 100;          // MAX = 200; → compile error
final class Constants { }     // class Sub extends Constants {} → error

class Parent {
    final void show() { }     // subclass override করতে পারবে না
}

void readFile() {
    BufferedReader r = null;
    try {
        r = new BufferedReader(new FileReader("a.txt"));
        // ...
    } finally {
        if (r != null) r.close();   // যাই হোক বন্ধ হবে
    }
}

@Override
protected void finalize() {   // deprecated — উদাহরণমাত্র
    // GC মুছে ফেলার আগে (যদি আদৌ ডাকে)
}
```

## Dart-এর সাথে মিল/অমিল

| Java | Dart সমতুল্য |
|---|---|
| `final variable` | **`final`** — হুবহু একই অর্থ! (একবার assign, আর নয়)। Dart-এ compile-time হলে `const` |
| `final method` (override বন্ধ) | Dart-এ আলাদা keyword নেই; convention/`@nonVirtual` (meta) |
| `final class` (extends বন্ধ) | Dart 3-এ **`final class`** / `sealed` keyword এসেছে — কাছাকাছি! |
| `finally` block | **`finally`** — হুবহু একই |
| `finalize()` | Dart-এ এমন কিছু নেই (GC hook নেই); cleanup-এর জন্য `Finalizer` (নতুন) আছে |

```dart
final int max = 100;     // Java-র final variable-এর মতোই
const double pi = 3.14;  // compile-time constant
// try { } finally { }   // Java-র মতোই
```

> মজার মিল: Java আর Dart দুটোতেই **`final`** শব্দটা একই অর্থে (variable আর নয়) ব্যবহার হয়। Dart 3-এ `final class`-ও এসেছে যা Java-র `final class`-এর কাছাকাছি।

## Common mistake
- তিনটাকে গুলিয়ে ফেলা — মনে রাখুন: **final = variable/method/class lock**, **finally = block**, **finalize = method**।
- `finalize()`-কে destructor (C++-এর মতো নিশ্চিত cleanup) ভাবা — এটা নিশ্চিত নয়, deprecated।

## Follow-up
- **"finalize() কেন খারাপ?"** → কখন/আদৌ চলবে গ্যারান্টি নেই, performance খারাপ করে, deprecated। বদলে try-with-resources।
- **"final দিয়ে immutable object বানানো যায়?"** → final field দিলে reference বদলায় না, কিন্তু object-এর ভেতরের state বদলাতে পারে (deep immutability নয়)।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-4"></a>
# 13.4 — Generics vs Templates

> Topic: **Generics / type system** · Difficulty: **Medium** · common (language comparison)

> **বইয়ের ভাষায়:** Explain the differences between Java's generic objects and C++'s templates.

## প্রশ্নটা সহজ বাংলায়
Java-র **generics** (`List<String>`) আর C++-এর **templates** (`vector<string>`) — দুটোই "যেকোনো type-এর জন্য একই code" লেখার উপায়। দেখতে একরকম, কিন্তু ভেতরে কাজ করে সম্পূর্ণ আলাদাভাবে। পার্থক্য কী?

## মূল ধারণা / উত্তর (ধাপে ধাপে)

**মূল পার্থক্যটা একটাই বড়:** Java generics = **type erasure** (compile-এর পর type মুছে যায়); C++ templates = **নতুন code generate** (প্রতিটা type-এর জন্য আলাদা class বানে)।

### Java — Type Erasure
`List<String>` আর `List<Integer>` — compile-এর সময় type-check হয়, কিন্তু compile-এর **পরে** type information **মুছে** যায় (erasure)। runtime-এ দুটোই শুধু `List`।

```
compile time:  List<String>, List<Integer>   ← type check হয়
                        ↓ erasure
runtime:       List, List                     ← type মুছে গেছে, একই class
```

ফলাফল:
- runtime-এ `T`-এর আসল type জানা যায় না (`new T()` করা যায় না)।
- `List<String>` আর `List<Integer>`-এর `getClass()` **একই**।
- primitive ব্যবহার করা যায় না (`List<int>` নয়, `List<Integer>` — wrapper লাগে)।

### C++ — Template Instantiation
`vector<string>` আর `vector<int>` ব্যবহার করলে compiler প্রতিটার জন্য **আলাদা সম্পূর্ণ নতুন class** generate করে (যেন আপনি হাতে দুটো লিখেছেন)।

```
vector<int>     →  compiler একটা পুরো int-version class বানায়
vector<string>  →  আরেকটা পুরো string-version class বানায়
                   দুটো সম্পূর্ণ আলাদা type, runtime-এও আলাদা
```

ফলাফল: primitive চলে, runtime-এ type আলাদা, কিন্তু binary বড় হয় ("code bloat")।

### টেবিলে পার্থক্য

| বিষয় | Java Generics | C++ Templates |
|---|---|---|
| ভেতরের কৌশল | type **erasure** | প্রতি type-এ নতুন **code generate** |
| runtime-এ type? | মুছে যায় (একই class) | আলাদা থাকে (আলাদা class) |
| primitive (`int`) চলে? | না — wrapper (`Integer`) লাগে | হ্যাঁ |
| `new T()` করা যায়? | না (type জানা নেই) | হ্যাঁ |
| code size | একই (একটাই class) | বাড়ে (code bloat) |
| `T` দিয়ে static member? | না | হ্যাঁ |
| type constraint | `<T extends Number>` | concept / SFINAE (পুরোনোতে ঢিলেঢালা) |

## Code (Java)

```java
// Java generic — type erasure
class Box<T> {
    private T value;
    public void set(T v) { value = v; }
    public T get() { return value; }
    // T x = new T();  // [অসম্ভব] — runtime-এ T-এর type জানা নেই
}

Box<String> a = new Box<>();
Box<Integer> b = new Box<>();
System.out.println(a.getClass() == b.getClass());  // true! (erasure-এর কারণে একই class)
```

```cpp
// C++ template — তুলনার জন্য
template <typename T>
class Box {
    T value;
public:
    void set(T v) { value = v; }
    T get() { return value; }
    // T x = T();  // [চলে] — compiler আসল type জানে
};
// Box<int> আর Box<string> → দুটো সম্পূর্ণ আলাদা class
```

## Dart-এর সাথে মিল/অমিল

Dart-এর generics Java-র **চেয়ে ভালো** এক দিক থেকে: Dart-এ generics **reified** — runtime-এও type থাকে, erasure হয় না।

```dart
class Box<T> {
  T? value;
  void set(T v) => value = v;
  T? get() => value;
}

var a = Box<String>();
var b = Box<int>();
print(a.runtimeType == b.runtimeType);  // false! (Dart-এ type runtime-এও আলাদা)
print(a is Box<String>);                // true — runtime check কাজ করে
```

| | Java | Dart | C++ |
|---|---|---|---|
| runtime-এ type | **মুছে যায়** (erasure) | **থাকে** (reified) | থাকে (নতুন class) |
| `List<int>` | না (Integer লাগে) | হ্যাঁ (int-ও object) | হ্যাঁ |
| `is Box<String>` runtime check | অসম্পূর্ণ (erasure) | পুরোপুরি কাজ করে | n/a |
| code bloat | নেই | নেই | আছে |

> Dart একটা সুন্দর মাঝামাঝি জায়গায়: Java-র মতো **একটাই code** (bloat নেই), কিন্তু C++-এর মতো **runtime-এ type জানা যায়** (reified)। এজন্য Dart-এ `T` নিয়ে runtime check করা Java-র চেয়ে সহজ।

## Common mistake
- ভাবা যে Java generics-ও C++-এর মতো প্রতি type-এ নতুন class বানায় — না, একটাই class, type erasure।
- Java-তে `new T[]` বা `new T()` করতে চাওয়া — erasure-এর কারণে অসম্ভব।

## Follow-up
- **"Java generics-এ wildcard কী?"** → `List<? extends Number>` (covariance), `List<? super Integer>` (contravariance) — PECS rule।
- **"erasure-এর কারণে কী সমস্যা?"** → runtime-এ type জানা যায় না; overloading-এ `List<String>` ও `List<Integer>` একই signature হয়ে যায়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-5"></a>
# 13.5 — TreeMap, HashMap, LinkedHashMap

> Topic: **Collections / data structures** · Difficulty: **Medium** · খুব common (প্রায় নিশ্চিত প্রশ্ন)

> **বইয়ের ভাষায়:** Explain the differences between a `TreeMap`, `HashMap`, and `LinkedHashMap`. Provide an example of when each one would be best.

## প্রশ্নটা সহজ বাংলায়
তিনটাই `Map` (key → value জমায়)। কিন্তু **iteration-এর order** আর ভেতরের গঠন আলাদা। তিনটার পার্থক্য কী, আর কখন কোনটা ব্যবহার করব?

## মূল ধারণা / উত্তর (ধাপে ধাপে)

মূল প্রশ্ন একটাই: **key গুলো কোন order-এ থাকবে?**

### HashMap — কোনো order নেই (সবচেয়ে দ্রুত)
ভেতরে **hash table**। key-কে hash করে bucket-এ রাখে। iteration-এর order **অনিশ্চিত** (যেকোনো রকম হতে পারে)।
- get/put/remove: গড়ে **O(1)**।
- কখন: order দরকার নেই, শুধু দ্রুত lookup চাই — **default পছন্দ**।

### TreeMap — key sorted (Red-Black tree)
ভেতরে **balanced binary search tree (Red-Black tree)**। key গুলো **sorted order**-এ থাকে।
- get/put/remove: **O(log n)**।
- bonus: `firstKey()`, `lastKey()`, `floorKey()`, `ceilingKey()`, range query (`subMap`)।
- কখন: key গুলো **sorted দরকার**, অথবা "এর চেয়ে ছোট/বড় nearest key" দরকার।

### LinkedHashMap — insertion order রাখে
HashMap + একটা **linked list** যা insertion order ধরে রাখে। তাই যেই order-এ ঢুকিয়েছেন, সেই order-এ iterate হয়।
- get/put/remove: গড়ে **O(1)** (HashMap-এর মতোই, একটু বেশি memory)।
- কখন: O(1) lookup চাই **কিন্তু order ধরে রাখতে হবে** (যেমন LRU cache — access-order mode আছে)।

### এক নজরে

```
HashMap        :  {c=3, a=1, b=2}   ← কোনো order নেই (যেকোনো রকম)
LinkedHashMap  :  {a=1, b=2, c=3}   ← যে order-এ ঢোকানো হয়েছে
TreeMap        :  {a=1, b=2, c=3}   ← key sorted (a<b<c)
```

| | HashMap | LinkedHashMap | TreeMap |
|---|---|---|---|
| ভেতরের গঠন | hash table | hash table + linked list | Red-Black tree |
| order | নেই | insertion (বা access) order | sorted (key) |
| get/put | O(1) avg | O(1) avg | O(log n) |
| extra | — | order রাখে | range/nearest-key query |
| null key | একটা allowed | একটা allowed | না (compare করতে হয়) |

## Code (Java)

```java
import java.util.*;

Map<String,Integer> hash   = new HashMap<>();
Map<String,Integer> linked = new LinkedHashMap<>();
TreeMap<String,Integer> tree = new TreeMap<>();

for (Map<String,Integer> m : List.of(hash, linked, tree)) {
    m.put("c", 3); m.put("a", 1); m.put("b", 2);
}
System.out.println(hash);    // অনিশ্চিত order, যেমন {a=1, b=2, c=3} বা অন্য
System.out.println(linked);  // {c=3, a=1, b=2}  ← insertion order
System.out.println(tree);    // {a=1, b=2, c=3}  ← sorted

// TreeMap-এর special power:
System.out.println(tree.firstKey());      // "a"
System.out.println(tree.ceilingKey("aa")); // "b" (aa-এর পরের nearest key)
```

## Dart-এর সাথে মিল/অমিল

Dart-এ এই তিনটার সরাসরি সমতুল্য:

| Java | Dart |
|---|---|
| `LinkedHashMap` | **default `Map` / `{}`** — Dart-এর literal Map **insertion order ধরে রাখে**! |
| `HashMap` | `HashMap` (`dart:collection`) — order নেই, একটু দ্রুত |
| `TreeMap` | `SplayTreeMap` (`dart:collection`) — key sorted |

```dart
import 'dart:collection';

var def  = <String,int>{};        // = LinkedHashMap, insertion order রাখে
var hash = HashMap<String,int>(); // order নেই
var tree = SplayTreeMap<String,int>(); // key sorted

for (var m in [def, hash, tree]) {
  m['c'] = 3; m['a'] = 1; m['b'] = 2;
}
print(def);   // {c: 3, a: 1, b: 2}  ← insertion order (Java LinkedHashMap-এর মতো)
print(tree);  // {a: 1, b: 2, c: 3}  ← sorted
```

> **মনে রাখার মতো পার্থক্য:** Java-তে **default `HashMap`** (order নেই), কিন্তু **Dart-এ default `{}` হলো LinkedHashMap** (insertion order রাখে)। তাই Dart থেকে আসা লোকেরা ধরে নেয় Map অর্ডার রাখে — Java-র `HashMap`-এ এটা ভুল ধারণা।

## Common mistake
- `HashMap`-এর iteration order-এর ওপর নির্ভর করা — এটা **অনিশ্চিত**, বদলে যেতে পারে।
- "sorted দরকার" বলেই HashMap নিয়ে পরে sort করা — TreeMap থাকলে সরাসরি sorted।
- TreeMap-এ comparable নয় এমন key বা `null` key দেওয়া।

## Follow-up
- **"LRU cache কীভাবে বানাবে?"** → `LinkedHashMap` access-order mode + `removeEldestEntry` override (Ch16.25-এ বিস্তারিত)।
- **"কোনটা thread-safe?"** → কোনোটাই না; `ConcurrentHashMap` বা `Collections.synchronizedMap` লাগে।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-6"></a>
# 13.6 — Object Reflection

> Topic: **Reflection / runtime metadata** · Difficulty: **Medium** · common (concept প্রশ্ন)

> **বইয়ের ভাষায়:** Explain what object reflection is in Java and why it is useful.

## প্রশ্নটা সহজ বাংলায়
**Reflection** মানে — program চলার সময় (runtime-এ) একটা class/object-এর ভেতরটা "দেখা" ও "ছোঁয়া": কী কী field আছে, কী কী method আছে, এমনকি নাম জানলে সেই method **ডাকা** বা object **বানানো**। Reflection কী, আর কেন কাজে লাগে?

## মূল ধারণা / উত্তর (ধাপে ধাপে)

**ধাপ ১ — সাধারণত আমরা কীভাবে কাজ করি।** সাধারণত code লেখার সময়েই (compile time) আমরা জানি কোন class, কোন method। `obj.doSomething()` লিখি।

**ধাপ ২ — reflection উল্টোটা করে।** Reflection দিয়ে compile time-এ **না জেনেও**, runtime-এ class-এর তথ্য বের করে কাজ করা যায়:

```
- class-এর সব field/method/constructor-এর তালিকা পাও
- নাম (String) দিয়ে method খুঁজে সেটা ডাকো
- নতুন object বানাও (class-এর নাম জানলেই হয়)
- private field/method পর্যন্ত access করো (setAccessible(true))
```

**ধাপ ৩ — কেন দরকার (কোথায় ব্যবহার হয়)।**

```
1. Framework / library  → Spring, Hibernate, JUnit — তারা আপনার class আগে থেকে জানে না,
                          runtime-এ reflection দিয়ে annotation পড়ে object বানায়/inject করে
2. Serialization        → JSON/XML লাইব্রেরি (Gson, Jackson) field গুলো reflection দিয়ে পড়ে
3. Dependency Injection  → নাম/type দেখে object তৈরি ও জোড়া দেওয়া
4. Testing / debugging   → private member পরীক্ষা, mock বানানো
5. Plugin architecture   → runtime-এ class নাম দিয়ে load ও চালানো
```

**দাম (trade-off):** reflection **ধীর** (সরাসরি call-এর চেয়ে), compile-time type safety **ভাঙে** (ভুল নাম দিলে runtime-এ crash), এবং encapsulation ভাঙতে পারে। তাই দরকার ছাড়া ব্যবহার করবেন না।

## Code (Java)

```java
import java.lang.reflect.*;

class Person {
    private String name = "Rahim";
    public void greet() { System.out.println("Hello " + name); }
}

public static void main(String[] args) throws Exception {
    // 1. class নাম দিয়ে object বানানো (compile-এ Person না লিখেও)
    Class<?> cls = Class.forName("Person");
    Object obj = cls.getDeclaredConstructor().newInstance();

    // 2. নাম দিয়ে method খুঁজে ডাকা
    Method greet = cls.getMethod("greet");
    greet.invoke(obj);                       // → "Hello Rahim"

    // 3. private field পর্যন্ত পড়া/বদলানো
    Field f = cls.getDeclaredField("name");
    f.setAccessible(true);                   // private-ও খুলে দাও
    System.out.println(f.get(obj));          // "Rahim"
    f.set(obj, "Karim");
    greet.invoke(obj);                       // → "Hello Karim"

    // 4. সব method-এর তালিকা
    for (Method m : cls.getDeclaredMethods())
        System.out.println(m.getName());
}
```

## Dart-এর সাথে মিল/অমিল

Dart-এ reflection আছে `dart:mirrors` দিয়ে — **কিন্তু এটা Flutter-এ কাজ করে না** (tree-shaking আর AOT-এর কারণে disabled)। তাই Flutter জগতে reflection-এর জায়গায় **code generation** ব্যবহার হয়।

| | Java | Dart / Flutter |
|---|---|---|
| reflection API | `java.lang.reflect` (সবসময় available) | `dart:mirrors` — **Flutter-এ নেই** |
| JSON parse | reflection (Gson/Jackson) | **code gen** (`json_serializable`, `build_runner`) |
| DI | reflection (Spring) | code gen / manual (`get_it`, `injectable`) |
| কেন আলাদা | JVM dynamic | Flutter AOT + tree-shaking reflection ভাঙে |

```dart
// Flutter-এ reflection নেই — তাই annotation + code generation:
@JsonSerializable()
class Person {
  final String name;
  Person(this.name);
  // build_runner compile-time-এ fromJson/toJson generate করে দেয়
}
```

> **বড় mental shift:** Java-তে runtime reflection দিয়ে যা করা হয় (JSON, DI), Flutter-এ তা **compile-time code generation** দিয়ে করা হয়। কারণ Flutter AOT-compiled — runtime-এ class metadata "খুলে দেখা"র সুযোগ থাকে না। এটাই দুই ecosystem-এর সবচেয়ে বড় practical পার্থক্য।

## Common mistake
- সব জায়গায় reflection ব্যবহার করা — ধীর, type-unsafe; দরকার হলেই (framework-level) ব্যবহার করুন।
- Flutter-এ `dart:mirrors` চালাতে চাওয়া — চলবে না; code gen ব্যবহার করুন।
- reflection-এ string নাম hard-code করা — typo হলে compile-এ ধরা পড়ে না, runtime-এ crash।

## Follow-up
- **"reflection ধীর কেন?"** → JVM প্রতিবার metadata খোঁজে, security check করে, JIT optimize করতে পারে না।
- **"annotation-এর সাথে সম্পর্ক?"** → framework annotation (`@Override`, `@Autowired`) reflection দিয়ে runtime-এ পড়া হয়।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-7"></a>
# 13.7 — Lambda Expressions

> Topic: **Lambda / Streams (functional)** · Difficulty: **Medium** · খুব common (Java 8+)

> **বইয়ের ভাষায়:** There is a list of people, each with an age. Implement a method `Country getMostPopulous(...)`- এর ধাঁচে — using lambda expressions, write methods to (a) get a list of people of a given minimum age, and (b) group/count people. (CTCI-তে `Country`-list-এর উদাহরণ; এখানে generic list filter ও group দেখানো হলো।)

## প্রশ্নটা সহজ বাংলায়
Java 8-এর **lambda** (`->`) ও **Stream** ব্যবহার করে একটা list থেকে: (ক) শর্ত মেনে কিছু element **filter** করা, আর (খ) element গুলোকে **group** করে count করা। লক্ষ্য: loop না লিখে functional style-এ পরিষ্কার করে করা।

## মূল ধারণা / উত্তর (ধাপে ধাপে)

**Lambda কী?** ছোট একটা নামহীন function। `(x) -> x + 1` মানে "x নাও, x+1 ফেরত দাও"। Java-তে lambda আসলে একটা **functional interface** (একটামাত্র abstract method-ওয়ালা interface, যেমন `Predicate`, `Function`)-এর implementation।

**Stream কী?** একটা collection-এর ওপর pipeline বানিয়ে চেইন করে কাজ করার উপায়: `filter → map → collect`। প্রতিটা ধাপ lambda নেয়।

```
list.stream()              ← stream শুরু
    .filter(p -> p.age>=18) ← শর্ত মেনে রাখো
    .map(p -> p.name)       ← রূপান্তর
    .collect(...)           ← আবার list/map-এ জমাও
```

## Code (Java)

```java
import java.util.*;
import java.util.stream.*;

class Person {
    String name; int age; String city;
    Person(String n, int a, String c) { name=n; age=a; city=c; }
    int getAge() { return age; }
    String getCity() { return city; }
}

// (ক) ন্যূনতম বয়সের লোকদের filter — lambda + stream
static List<Person> atLeast(List<Person> people, int minAge) {
    return people.stream()
                 .filter(p -> p.age >= minAge)   // lambda predicate
                 .collect(Collectors.toList());
}

// (খ) শহর অনুযায়ী group করে count
static Map<String,Long> countByCity(List<Person> people) {
    return people.stream()
                 .collect(Collectors.groupingBy(
                     Person::getCity,             // কোন key-তে group (method reference)
                     Collectors.counting()));     // প্রতি group-এ গোনো
}

// average বয়স বের করা (bonus)
static double avgAge(List<Person> people) {
    return people.stream().mapToInt(Person::getAge).average().orElse(0);
}
```

```java
// ব্যবহার:
List<Person> people = List.of(
    new Person("Asha", 30, "Dhaka"),
    new Person("Bilal", 15, "Dhaka"),
    new Person("Chumki", 22, "Khulna"));

atLeast(people, 18);     // [Asha, Chumki]
countByCity(people);     // {Dhaka=2, Khulna=1}
```

## Dart-এর সাথে মিল/অমিল

Dart-এ lambda **আরও সহজ** — কোনো `Predicate`/`Function` interface লাগে না, function first-class:

```dart
class Person {
  final String name; final int age; final String city;
  Person(this.name, this.age, this.city);
}

// (ক) filter
List<Person> atLeast(List<Person> people, int minAge) =>
    people.where((p) => p.age >= minAge).toList();

// (খ) group করে count (Dart-এ groupingBy built-in নেই, fold দিয়ে)
Map<String,int> countByCity(List<Person> people) {
  final m = <String,int>{};
  for (final p in people) {
    m[p.city] = (m[p.city] ?? 0) + 1;
  }
  return m;
  // অথবা collection package-এর groupBy() ব্যবহার করা যায়
}
```

| Java | Dart |
|---|---|
| `stream().filter(p -> ...)` | `.where((p) => ...)` |
| `.map(p -> p.name)` | `.map((p) => p.name)` |
| `.collect(toList())` | `.toList()` |
| `.reduce(...)` | `.reduce(...)` / `.fold(...)` |
| `groupingBy(...)` | built-in নেই; `fold` বা `package:collection`-এর `groupBy` |
| lambda-র দরকার | functional **interface** লাগে | function first-class, interface লাগে না |
| lazy? | Stream lazy | `Iterable` (`where`/`map`) lazy |

> **মূল পার্থক্য:** Java lambda-র পেছনে একটা functional interface (`Predicate<T>` ইত্যাদি) থাকতে হয় — compiler সেটা মেলায়। Dart-এ function নিজেই একটা value, তাই কোনো interface ছাড়াই `(x) => ...` লেখা যায় — অনেক হালকা। Dart-এ `where`/`map`-ও lazy (`Iterable`), Java Stream-এর মতোই।

## Common mistake
- Stream একবার consume হয়ে গেলে আবার ব্যবহার করা (terminal operation-এর পর stream শেষ)।
- `forEach` দিয়ে side-effect-এ list বানানো — বদলে `collect`/`map` ব্যবহার করুন।
- Dart-এ `where`/`map` lazy বলে `toList()` না ডাকলে কাজ "হয় না" — মনে রাখুন।

## Follow-up
- **"parallel stream কী?"** → `.parallelStream()` — multi-core-এ ভাগ করে চালায় (সাবধানে, সব কাজ parallel-উপযোগী নয়)।
- **"method reference (`Person::getCity`) মানে কী?"** → lambda-র শর্টহ্যান্ড; `p -> p.getCity()`-এর সমান।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---

<a id="q13-8"></a>
# 13.8 — Lambda Random

> Topic: **Lambda / random sampling** · Difficulty: **Medium** · common (13.7-এর ফলো-আপ)

> **বইয়ের ভাষায়:** How would you use a lambda expression to write a function that returns a random subset of arbitrary size? All subsets (of any size) should be equally likely to be chosen.

## প্রশ্নটা সহজ বাংলায়
একটা list থেকে একটা **random subset** ফেরত দিতে হবে — যেকোনো size-এর, এবং এমনভাবে যেন **সব subset সমান সম্ভাবনায়** বেছে নেওয়া হয়। আর এটা **lambda** দিয়ে করতে হবে।

## মূল ধারণা / উত্তর (ধাপে ধাপে)

**মূল insight (খুব দামি):** প্রতিটা element-এর জন্য আলাদাভাবে coin toss (৫০% সম্ভাবনা) করে ঠিক করি সে subset-এ থাকবে কিনা।

**কেন এটা সব subset সমান সম্ভাবনায় দেয়?**

```
n element আছে → মোট subset সংখ্যা = 2^n
প্রতিটা element স্বাধীনভাবে 50% chance-এ থাকে/থাকে না
একটা নির্দিষ্ট subset পাওয়ার সম্ভাবনা = (1/2) × (1/2) × ... n বার = 1/2^n
সব subset-ই 1/2^n → সমান সম্ভাবনা (এটাই চাওয়া)
```

তাই complicated কিছু লাগে না — শুধু প্রতিটা element-এ `random.nextBoolean()`। আর এটাই lambda দিয়ে এক লাইনে filter করা যায়।

## Code (Java)

```java
import java.util.*;
import java.util.stream.*;

static <T> List<T> randomSubset(List<T> list) {
    Random rand = new Random();
    return list.stream()
               .filter(item -> rand.nextBoolean())   // প্রতিটায় 50% coin toss — lambda
               .collect(Collectors.toList());
}

// ব্যবহার:
List<Integer> nums = List.of(1, 2, 3, 4, 5);
System.out.println(randomSubset(nums));  // যেমন [1, 4, 5] — প্রতিবার ভিন্ন, যেকোনো size
```

> এক লাইনের lambda `item -> rand.nextBoolean()` প্রতিটা element-এর জন্য স্বাধীন coin toss করছে — এতেই 2^n subset সমান সম্ভাবনায় আসে।

## Dart-এর সাথে মিল/অমিল

Dart-এ হুবহু একই idea, `where` + `Random.nextBool()`:

```dart
import 'dart:math';

List<T> randomSubset<T>(List<T> list) {
  final rand = Random();
  return list.where((_) => rand.nextBool()).toList();  // প্রতিটায় 50% — একই কৌশল
}

// ব্যবহার:
print(randomSubset([1, 2, 3, 4, 5]));  // যেমন [2, 3] — প্রতিবার ভিন্ন
```

| Java | Dart |
|---|---|
| `new Random().nextBoolean()` | `Random().nextBool()` |
| `.filter(x -> ...)` | `.where((x) => ...)` |
| `.collect(toList())` | `.toList()` |
| generic method `<T>` | generic method `<T>` |

> idea ও code প্রায় অভিন্ন — শুধু নাম আলাদা (`nextBoolean` vs `nextBool`, `filter` vs `where`)। মূল গণিতটা (প্রতি element-এ স্বাধীন 50% = সব subset 1/2^n) দুই ভাষাতেই একই।

## Common mistake
- "random size আগে বেছে, তারপর সেই কয়টা element নাও" — এতে সব subset **সমান সম্ভাবনায় আসে না** (ছোট/বড় size-এর bias তৈরি হয়)। per-element coin toss-ই সঠিক।
- সব element shuffle করে প্রথম k নেওয়া — এটা fixed-size subset-এর জন্য (অন্য সমস্যা), arbitrary-size equal-probability নয়।

## Follow-up
- **"ঠিক size k-এর random subset চাইলে?"** → reservoir sampling, অথবা shuffle করে প্রথম k (Ch17.3 Random Set)।
- **"প্রমাণ করো সব subset সমান সম্ভাবনায়।"** → প্রতিটা element স্বাধীন 1/2 → যেকোনো নির্দিষ্ট subset = 1/2^n, যা সব subset-এর জন্য সমান।

<sub>[↑ এই chapter-এর সূচি](#toc) · [মূল Index](README.md)</sub>

---
---

# Chapter 13 — সারসংক্ষেপ ও Java↔Dart Cheat Sheet

| # | প্রশ্ন | মূল উত্তর এক লাইনে |
|---|---|---|
| 13.1 | Private Constructor | বাইরে থেকে instantiate/subclass বন্ধ; singleton/utility-তে কাজে লাগে |
| 13.2 | Return from Finally | `try`-তে return থাকলেও `finally` চলে; `finally`-তে return original-কে override করে |
| 13.3 | Final, Finally, Finalize | final=lock (var/method/class), finally=block, finalize()=GC-আগের method (deprecated) |
| 13.4 | Generics vs Templates | Java=type erasure (runtime-এ মুছে যায়); C++=প্রতি type-এ নতুন class |
| 13.5 | TreeMap/HashMap/LinkedHashMap | sorted / no-order(O(1)) / insertion-order |
| 13.6 | Object Reflection | runtime-এ class পরীক্ষা ও ব্যবহার; framework/JSON/DI-তে দরকার, কিন্তু ধীর |
| 13.7 | Lambda Expressions | `stream().filter/map/collect` দিয়ে functional list প্রসেস |
| 13.8 | Lambda Random | প্রতি element-এ 50% coin toss → সব 2^n subset সমান সম্ভাবনায় |

### Java↔Dart দ্রুত মিলকরণ (cheat sheet)

```
Java                          →  Dart
─────────────────────────────────────────────────────
private ctor + getInstance()  →  Foo._() + factory (singleton)
final variable                →  final / const
try-catch-finally             →  try-catch-finally (একই)
catch (Type e)                →  on Type catch (e)
List<Integer> (wrapper লাগে)  →  List<int> (int-ও object)
generics: type erasure        →  generics: reified (runtime-এ type থাকে)
HashMap (default, no order)   →  HashMap (dart:collection)
LinkedHashMap (insertion)     →  default {} / Map  ← Dart-এ এটাই default!
TreeMap (sorted)              →  SplayTreeMap
reflection (java.lang.reflect)→  code generation (Flutter-এ mirrors নেই)
stream().filter(p -> ...)     →  .where((p) => ...)
.map / .collect(toList())     →  .map / .toList()
Random().nextBoolean()        →  Random().nextBool()
```

### এই chapter-এর ৫টা সোনার নিয়ম
1. **constructor private** = বাইরে থেকে object/subclass বন্ধ → singleton ও utility class-এর ভিত্তি।
2. **`finally` যাই হোক চলে** (একমাত্র `System.exit()`-এ নয়); `finally`-তে কখনো `return` দেবেন না।
3. **final ≠ finally ≠ finalize** — keyword vs block vs (deprecated) method; গুলিয়ে ফেলবেন না।
4. **Java generics = type erasure** (runtime-এ মুছে যায়); এই একটা শব্দ মনে রাখলেই C++ template-এর সাথে পার্থক্য পরিষ্কার। Dart-এর generics reified — মাঝামাঝি সেরা জায়গা।
5. **Map বাছাই = order-এর প্রশ্ন:** order লাগবে না → HashMap; insertion order → LinkedHashMap (Dart-এ default); sorted → TreeMap (Dart SplayTreeMap)।

> **পরের ধাপ:** [Chapter 14 — Databases](chapter14_databases.md) (14.1–14.7), যেখানে SQL query, join, normalization আর ER diagram শিখব।
</content>
</invoke>
