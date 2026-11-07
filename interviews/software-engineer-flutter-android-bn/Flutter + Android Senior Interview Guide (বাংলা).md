# Flutter + Android Senior Interview Guide (বাংলা)

Nov 8, 2026 · @Md. Yousuf Ali

## ১. Roadmap: Senior Flutter + Android ইঞ্জিনিয়ারের কী কী জানা লাগে

---

**Q:** Senior Flutter + Android পজিশনে ইন্টারভিউয়ার আসলে কী যাচাই করে?

**A:** মূলত চারটি জিনিস:

1. **Depth** — একটা জিনিস ভেতরে কীভাবে কাজ করে (যেমন Flutter-এর build → layout → paint, বা Android-এর process death), শুধু API-র নাম নয়।
2. **Trade-off চিন্তা** — কেন Riverpod, কেন Room, কেন multi-module; বিকল্পের তুলনায় কী পেলাম আর কী হারালাম।
3. **Scale-এর অভিজ্ঞতা** — বড় codebase, একাধিক টিম, CI/CD, release strategy, crash monitoring।
4. **Ownership ও Communication** — সমস্যা debug করা, সিদ্ধান্ত নেওয়া, অন্যকে বোঝানো।

Junior জানে 'কীভাবে করতে হয়'। Senior জানে 'কেন এভাবে, কখন এভাবে নয়, আর ভুল হলে কী হবে'।

**Example:**

প্রশ্ন: 'Low-end Android ফোনে আপনার Flutter অ্যাপে scroll jank হচ্ছে। কী করবেন?'

- দুর্বল উত্তর: 'const ব্যবহার করব, ListView.builder দেব।'
- Senior উত্তরের কাঠামো:
  1. আগে মাপব — Profile mode-এ আসল ডিভাইসে DevTools Performance view খুলে দেখব সমস্যা UI thread-এ নাকি Raster thread-এ।
  2. UI thread ধীর হলে → অপ্রয়োজনীয় rebuild, build()-এর ভেতরে ভারী কাজ, বড় JSON parse (isolate-এ সরাব)।
  3. Raster thread ধীর হলে → saveLayer/clip/opacity-র অতিরিক্ত ব্যবহার, বিশাল image decode, shader compilation।
  4. Fix করার পর আবার মাপব, আগে-পরের frame time তুলনা করব।

**Why it matters:** ইন্টারভিউয়ার দেখতে চায় আপনি অনুমান করে ঠিক করেন, নাকি মেপে ঠিক করেন। 'Measure → Identify → Fix → Verify' পদ্ধতি senior মানসিকতার চিহ্ন।

**Common mistake:** টুল/প্যাকেজের নামের তালিকা বলে দেওয়া, কিন্তু কেন কাজ করে তা বলতে না পারা।

---

**Q:** Flutter ডেভেলপারের জন্য native Android কতটা জানা দরকার, আর কেন?

**A:** Flutter অ্যাপ আসলে একটা Android অ্যাপই — ভেতরে একটা `FlutterActivity` (বা `FlutterFragment`) চলে, যেটা Flutter Engine বসিয়ে Dart কোড চালায়। তাই Android-এর নিচের স্তরের সমস্যা (permission, background কাজ, notification, deep link, build, signing, crash) Dart দিয়ে সমাধান হয় না; সেখানে Android জ্ঞান লাগে।

প্রয়োজনীয় গভীরতা হলো **T-shape**: Flutter-এ খুব গভীর, Android-এ যথেষ্ট প্রশস্ত ও কয়েকটি জায়গায় গভীর (lifecycle, background execution, Gradle/build, platform channel, performance)।

```
+--------------------------------------------------+
|  Dart / Flutter  (UI, state, business logic)     |   <- আপনার মূল শক্তি
+--------------------------------------------------+
|  Flutter Engine (C++), Android Embedder          |
|  FlutterActivity, FlutterView, Platform Channels |   <- সংযোগের জায়গা
+--------------------------------------------------+
|  Android Framework (Kotlin/Java)                 |
|  Activity, Service, Manifest, Permissions, WM    |   <- Android জ্ঞান এখানে
+--------------------------------------------------+
|  ART (runtime) + Linux Kernel                    |
+--------------------------------------------------+
```

**Example:**

সমস্যা: Android 13+ ডিভাইসে Flutter অ্যাপে push notification দেখাচ্ছে না, অথচ Android 12-এ দেখাচ্ছে।

কারণ Dart কোডে নেই। Android 13 (API 33) থেকে `POST_NOTIFICATIONS` runtime permission লাগে, আর Android 8+ থেকে notification channel বাধ্যতামূলক। Manifest-এ permission ঘোষণা করতে হয় এবং runtime-এ চাইতে হয়:

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
```

**Why it matters:** 'Flutter + Android' রোলে ইন্টারভিউয়ার জানতে চায় আপনি production সমস্যায় Flutter স্তর ছেড়ে নিচে নেমে কারণ খুঁজতে পারেন কিনা।

**Common mistake:** 'প্লাগইন আছে তো, Android জানার দরকার নেই' বলা। প্লাগইন ভাঙলে বা কাস্টম কাজ লাগলে সেই ব্যক্তিই আটকে যায়।

---

**Q:** আমি এখন Java-তে Android করছি। Android-কে নতুন করে শেখার সবচেয়ে কার্যকর ক্রম কী?

**A:** পুরোনো Java/XML পদ্ধতির পাশাপাশি আজকের Android হলো **Kotlin + Coroutines/Flow + Jetpack (ViewModel, Room, WorkManager, Navigation, Hilt) + Compose**। প্রস্তাবিত ক্রম:

```
ধাপ ১  Kotlin মূল বিষয়: null safety, data class, extension, lambda, sealed class
ধাপ ২  Activity/Fragment lifecycle, Manifest, Intent, Task/Back stack
ধাপ ৩  Coroutines + Flow (Android-এর async-এর মেরুদণ্ড)
ধাপ ৪  ViewModel + StateFlow + Room (আধুনিক architecture)
ধাপ ৫  Jetpack Compose মূল বিষয়: state, recomposition, side-effect
ধাপ ৬  WorkManager, Services, Permissions, Notification, Doze
ধাপ ৭  Hilt (DI), Navigation, Paging
ধাপ ৮  Performance (ANR, leak, startup), R8, Testing
ধাপ ৯  Flutter ↔ Android: Platform channel, Pigeon, FFI, add-to-app
```

আপনার Java জ্ঞান কাজে লাগবে (ধাপ ১ দ্রুত শেষ হবে), আর Flutter-এর state/architecture অভিজ্ঞতা ধাপ ৪-৭ বুঝতে সাহায্য করবে।

**Example:** প্রথম ছোট প্রজেক্ট — Kotlin + Compose + ViewModel + Room দিয়ে একটা Notes অ্যাপ:

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Text("Hello Android")
            }
        }
    }
}
```

তারপর ধাপে ধাপে ViewModel (state ধরে রাখা), Room (local DB), Hilt (DI) যোগ করুন। প্রতিটি ধাপ Flutter-এর সাথে মিলিয়ে বুঝুন (এ বিষয়ে শেষ সেকশনে mapping টেবিল আছে)।

**Why it matters:** ইন্টারভিউয়ার দেখে আপনি আধুনিক Android-এর ভাষা (Kotlin, Flow, Compose, Jetpack) জানেন কিনা, নাকি ২০১৬ সালের Android-এ আটকে আছেন।

**Common mistake:** Java-তে থেকে যাওয়া। নতুন Android ইন্টারভিউয়ে Kotlin ধরে নেওয়া হয়; Java শুধু legacy প্রসঙ্গে আসে।

---

**Q:** Senior Flutter + Android ইন্টারভিউ সাধারণত কয়টি রাউন্ডে হয়, প্রতিটিতে কী জিজ্ঞেস করে?

**A:** কোম্পানিভেদে ভিন্ন, তবে সাধারণ কাঠামো:

| রাউন্ড | কী যাচাই করে | সাধারণ প্রশ্ন |
| --- | --- | --- |
| Screening (HR/Recruiter) | অভিজ্ঞতা, প্রত্যাশা | কোন অ্যাপ করেছেন, কেন চাকরি বদল |
| Coding / DSA | সমস্যা সমাধান | Array/String/Hashmap, ছোট Dart/Kotlin টাস্ক |
| Flutter deep dive | Framework বোঝাপড়া | Three trees, keys, state management, isolates |
| Android deep dive | Native ভিত্তি | Lifecycle, process death, Services, WorkManager |
| Mobile system design | Architecture, scale | Chat/Feed/Offline sync অ্যাপ ডিজাইন |
| Behavioral / Leadership | মানসিকতা, নেতৃত্ব | দ্বন্দ্ব, mentoring, সিদ্ধান্তের ব্যর্থতা |

**Example:** একটি বাস্তব ক্রম: 30 মিনিট screening → 60 মিনিট live coding → 60 মিনিট Flutter + Android technical → 60 মিনিট system design → 45 মিনিট culture/leadership।

**Why it matters:** প্রতিটি রাউন্ডের প্রস্তুতি আলাদা। শুধু Flutter প্রস্তুত করলে Android ও system design রাউন্ডে ধরা খাবেন।

**Common mistake:** শুধু technical topic মুখস্থ করা, behavioral ও system design উপেক্ষা করা — অথচ senior পজিশনে এগুলোই চূড়ান্ত সিদ্ধান্ত নেয়।

---

**Q:** কোন বিষয়গুলো থেকে সবচেয়ে বেশি প্রশ্ন আসে? কোথায় বেশি সময় দেব?

**A:** সময় ভাগ করার একটি বাস্তবসম্মত অগ্রাধিকার তালিকা (সাধারণ অভিজ্ঞতা অনুযায়ী, কোম্পানিভেদে বদলাবে):

| বিষয় | অগ্রাধিকার | কেন |
| --- | --- | --- |
| Flutter rendering, three trees, keys | খুব বেশি | Flutter ইন্টারভিউয়ের মূল ভিত্তি |
| Dart async, event loop, isolates | খুব বেশি | প্রায় প্রতি ইন্টারভিউয়ে আসে |
| State management + architecture | খুব বেশি | Senior-এর প্রধান পরিচয় |
| Android lifecycle, process death | বেশি | 'Android জানেন কিনা'র প্রথম পরীক্ষা |
| Coroutines/Flow, ViewModel, Room | বেশি | আধুনিক Android-এর ভিত্তি |
| Platform channel / native integration | বেশি | Flutter + Android রোলের বৈশিষ্ট্য |
| Performance (Flutter ও Android) | বেশি | Senior মাপকাঠি |
| CI/CD, release, modularization | মাঝারি-বেশি | Large-scale অভিজ্ঞতা বোঝায় |
| Jetpack Compose | মাঝারি | অনেক কোম্পানি চায়, সবাই নয় |
| Mobile system design | বেশি | Senior রাউন্ডের নির্ধারক |

**Example:** সপ্তাহে ১০ ঘণ্টা সময় থাকলে — ৪ ঘণ্টা Android মূল বিষয় (কারণ এটি নতুন), ৩ ঘণ্টা Flutter/Dart গভীরতা, ২ ঘণ্টা system design, ১ ঘণ্টা behavioral গল্প প্রস্তুতি।

**Why it matters:** সীমিত সময়ে কোন জায়গায় লাভ বেশি তা বুঝতে পারা নিজেই একটি senior দক্ষতা।

**Common mistake:** যা ভালো জানেন (Flutter UI) তাতেই বারবার সময় দেওয়া, আর দুর্বল জায়গা (Android native) এড়িয়ে যাওয়া।

---

**Q:** 'আপনি তো Flutter ডেভেলপার, এখন Android-এ কেন আসছেন?' — এই প্রশ্নের উত্তর কীভাবে দেবেন?

**A:** উত্তরে তিনটি জিনিস থাকবে: (১) আপনার আগের native Android/iOS অভিজ্ঞতা, (২) বাস্তব কারণ — বড় অ্যাপে Flutter এবং native একসাথে চলে, আর যে ইঞ্জিনিয়ার দুই স্তরই বোঝে সে সিদ্ধান্তে ও debugging-এ বেশি কার্যকর, (৩) আপনি সক্রিয়ভাবে সেই জ্ঞান আধুনিক করেছেন।

**Example:**

'আমি আট বছর মোবাইলে কাজ করছি। শুরুতে native Android ও iOS করেছি, গত চার-পাঁচ বছর মূলত Flutter। বড় অ্যাপে দেখেছি platform-specific সমস্যা (background execution, notification, build config) সমাধান করতে native স্তর জানা জরুরি। তাই আমি Kotlin, Coroutines/Flow, Jetpack ও Compose নতুন করে শিখেছি এবং Flutter অ্যাপে platform channel দিয়ে সেগুলো ব্যবহার করেছি। এখন আমি এমন ভূমিকা চাই যেখানে দুই স্তরের সিদ্ধান্ত আমি নিতে পারি।'

**Why it matters:** ইন্টারভিউয়ার আপনার প্রেরণা ও আত্মবিশ্বাস দেখে। Defensive না হয়ে ইতিবাচক ও নির্দিষ্ট উদাহরণসহ উত্তর বিশ্বাসযোগ্যতা বাড়ায়।

**Common mistake:** 'Android তো জানি না, শিখছি' — এমন দুর্বল ভঙ্গিতে বলা। বরং 'এই অংশে শক্ত, এই অংশ আধুনিক করেছি' এভাবে বলুন।

---

## ২. Android Platform Basics: Architecture, ART, Build System

---

**Q:** Android platform-এর architecture কয়টি layer-এ বিভক্ত? প্রতিটি layer কী কাজ করে?

**A:** Android একটি layered stack। নিচ থেকে উপরে:

1. **Linux Kernel** — process ও memory management, driver, security (প্রতিটি app আলাদা Linux user/UID), এবং **Binder** IPC driver।
2. **HAL (Hardware Abstraction Layer)** — camera, sensor, audio-র মতো hardware-এর standard interface।
3. **Android Runtime (ART) + Native C/C++ libraries** — app-এর কোড চালায়; native library যেমন libc, SQLite, OpenGL/Vulkan।
4. **Java API Framework** — আপনি যে API দিয়ে কাজ করেন: Activity Manager, Package Manager, Window Manager, Notification Manager, View System, Content Providers।
5. **Applications** — system app ও আপনার app।

```
+--------------------------------------------------+
|  Apps (আপনার app, system apps)                   |
+--------------------------------------------------+
|  Java API Framework (ActivityManager, WM, PM...) |
+------------------------+-------------------------+
|  ART (runtime)         |  Native libs (C/C++)    |
+------------------------+-------------------------+
|  HAL (camera, audio, sensors)                    |
+--------------------------------------------------+
|  Linux Kernel (drivers, Binder, memory, security)|
+--------------------------------------------------+
```

App যখন system service ব্যবহার করে (যেমন location, notification), তখন আসলে **Binder IPC** দিয়ে অন্য process-এর (system\_server) সাথে কথা বলে।

**Example:**

```kotlin
// নিচের লাইন আসলে Binder দিয়ে system_server-এর ConnectivityService-এ কল করে
val cm = getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
val network = cm.activeNetwork
```

**Why it matters:** ইন্টারভিউয়ার দেখে আপনি Android-কে 'শুধু Activity বানানোর ফ্রেমওয়ার্ক' ভাবেন, নাকি Linux process, IPC ও sandbox সহ একটি পূর্ণ OS হিসেবে বোঝেন।

**Common mistake:** 'Android মানে Java framework' বলা। Kernel, ART ও Binder বাদ দিলে security, process death, ANR কিছুই ব্যাখ্যা করা যায় না।

---

**Q:** ART কী? Java/Kotlin কোড কীভাবে Android-এ চলে? JVM-এর সাথে পার্থক্য কী?

**A:** Java/Kotlin কোড প্রথমে `.class` (JVM bytecode) হয়, তারপর **D8** টুল সেটিকে **DEX bytecode**-এ রূপান্তর করে। Device-এ **ART (Android Runtime)** সেই DEX চালায়। ART তিন কৌশল মিশিয়ে ব্যবহার করে: **JIT** (চলার সময় hot method compile), **AOT** (আগে থেকে native code-এ compile), এবং **profile-guided compilation** (যে অংশ বেশি চলে সেটা device idle থাকলে AOT compile)। JVM stack-based bytecode চালায়, DEX register-based এবং memory-সীমিত device-এর জন্য optimized।

Baseline Profiles ব্যবহার করলে app-এর প্রথম launch থেকেই গুরুত্বপূর্ণ কোড pre-compiled থাকে, ফলে startup দ্রুত হয়।

**গুরুত্বপূর্ণ Flutter সংযোগ:** Flutter release build-এ আপনার **Dart কোড ART-এ চলে না**। Dart AOT compile হয়ে native ARM কোড (`libapp.so`) হয় এবং Flutter Engine (`libflutter.so`, C++) সেটি চালায়। ART শুধু Android host অংশ (FlutterActivity, plugin-এর Kotlin/Java কোড) চালায়।

**Example:**

```
Kotlin/Java (.kt/.java)
   --kotlinc/javac-->  .class
   --D8/R8-->          .dex  (classes.dex)
   --ART-->            JIT/AOT/profile-guided native code

Dart (.dart)
   --dart AOT compiler (release)--> libapp.so (native ARM)
   --Flutter Engine (libflutter.so)--> চালায়
```

**Why it matters:** Flutter-এ বিভিন্ন সমস্যা (বড় APK, startup, native crash) কোন layer-এ হচ্ছে সেটা ধরতে এই মডেল দরকার।

**Common mistake:** 'Dart কোড ART-এ চলে' বা 'Android JVM চালায়' বলা। Android JVM চালায় না; ART DEX চালায়।

---

**Q:** Android-এ প্রতিটি app কীভাবে চলে? Zygote, main thread ও Looper কী?

**A:** প্রতিটি app নিজের **Linux process**-এ, নিজস্ব UID ও ART instance নিয়ে চলে (sandbox) — অন্য app-এর data সরাসরি দেখতে পারে না। নতুন app process শুরু করতে system **Zygote** নামের একটি pre-warmed process **fork** করে; Zygote আগে থেকেই framework class ও resource load করে রাখে, তাই fork করা process দ্রুত শুরু হয় (memory page copy-on-write দিয়ে share হয়)।

প্রতিটি app-এর একটি **main thread (UI thread)** থাকে, যেটা একটি **Looper** দিয়ে **MessageQueue** থেকে একের পর এক কাজ (input event, lifecycle callback, draw) চালায়। এই thread block হলে UI জমে যায়; input event ৫ সেকেন্ডের মধ্যে handle না হলে **ANR (Application Not Responding)** হয়।

```
 Main thread
 +-----------------------------+
 | Looper --loop--> MessageQueue|
 |   ^ post(Runnable/Message)   |
 |   |  Handler                 |
 +-----------------------------+
 Background thread --Handler.post--> Main thread
```

Flutter-এ Android-এর main thread-ই **Platform thread**। Flutter ৩.২৯ থেকে Android ও iOS-এ Dart কোডও (root isolate) এই **একই main thread**-এ চলে — আলাদা Dart UI thread আর নেই (পুরোনো ব্লগ/উত্তরে আলাদা UI thread পাবেন, সেটা পুরোনো মডেল)। Rasterization চলে আলাদা Raster thread-এ। তাই ভারী Dart কাজ **isolate**-এ না সরালে main thread block হয়ে jank এমনকি ANR হতে পারে ([Flutter breaking-change doc](https://docs.flutter.dev/release/breaking-changes/macos-windows-merged-threads/index.html.md) এই ইতিহাসের উল্লেখ করে)।

**Example:**

```kotlin
// ভুল: main thread-এ ভারী কাজ -> ANR ঝুঁকি
button.setOnClickListener {
    val data = heavyJsonParse(file)   // সেকেন্ড লাগলে UI জমে যাবে
}

// ঠিক: Dispatchers.Default / IO-তে কাজ, ফল main thread-এ
lifecycleScope.launch {
    val data = withContext(Dispatchers.Default) { heavyJsonParse(file) }
    textView.text = data.summary
}
```

**Why it matters:** ANR, jank ও crash-এর বেশিরভাগ ইন্টারভিউ প্রশ্নের ভিত্তি এই মডেল।

**Common mistake:** 'Zygote শুধু একটি service' বলা, অথবা ভাবা যে Flutter-এ ভারী Dart কাজ করলে শুধু আলাদা UI thread ধীর হয় আর Android main thread ঠিক থাকে। ৩.২৯-এর পর Android-এ দুটি একই thread — ভারী কাজ সরাসরি ANR পর্যন্ত গড়াতে পারে।

---

**Q:** APK ও AAB-এর পার্থক্য কী? Release build ও signing কীভাবে কাজ করে?

**A:** **APK** হলো installable package (DEX, resource, native library সব একসাথে)। **AAB (Android App Bundle, `.aab`)** হলো publish করার ফরম্যাট: Google Play এটি থেকে প্রতিটি device-এর জন্য (ভাষা, screen density, CPU architecture অনুযায়ী) **optimized split APK** তৈরি করে। ফলে user ছোট size ডাউনলোড করে। Google Play-তে নতুন app AAB ফরম্যাটে দিতে হয়।

Signing: প্রতিটি APK/AAB একটি **keystore**-এর private key দিয়ে sign করতে হয়। **Play App Signing** চালু থাকলে আপনি **upload key** দিয়ে sign করে upload করেন, আর Google আসল **app signing key** নিজের কাছে সুরক্ষিত রাখে — upload key হারালে reset করা যায়, কিন্তু app signing key হারালে app আর update করা যেত না (তাই Google-কে রাখতে দেওয়া নিরাপদ)।

**Example:**

```bash
# Flutter: release AAB, Dart obfuscation সহ
flutter build appbundle --release \
  --obfuscate --split-debug-info=build/symbols

# APK বানাতে (সরাসরি install/test)
flutter build apk --release --split-per-abi
```

`--split-debug-info` দিয়ে তৈরি symbol ফাইল সংরক্ষণ করুন; Crashlytics-এ stack trace ডিকোড করতে লাগবে।

**Why it matters:** Release pipeline, app size ও key management ছাড়া senior-এর কাজ অসম্পূর্ণ; keystore হারানো একটি ক্লাসিক production বিপর্যয়।

**Common mistake:** keystore ও `key.properties` Git-এ commit করা, অথবা debug key দিয়ে release দেওয়া।

---

**Q:** compileSdk, targetSdk ও minSdk-র পার্থক্য কী? Gradle ও build variant (flavor) কীভাবে কাজ করে?

**A:**

| Setting | অর্থ |
| --- | --- |
| `minSdk` | সর্বনিম্ন যে Android version-এ app install হবে |
| `targetSdk` | যে version-এর behavior-কে মাথায় রেখে app test ও declare করা হয়; নতুন OS-এর behavior change এর ভিত্তিতে system আপনার app-এর সাথে আচরণ করে |
| `compileSdk` | কোন SDK-র API দিয়ে compile হবে (সাধারণত সর্বশেষ) |

Google Play-র নিয়ম অনুযায়ী ৩১ আগস্ট ২০২৬ থেকে নতুন app ও update-কে **Android 16 (API 36)** বা তার বেশি target করতে হয় ([Play Console Help](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en-419)); এক্সটেনশনের শেষ তারিখ ছিল ১ নভেম্বর ২০২৬। তাই এখন নতুন update-এ `targetSdk = 36` আবশ্যক।

**Gradle** হলো build system; **AGP (Android Gradle Plugin)** Android-এর build task যোগ করে। `buildTypes` (debug/release) ও `productFlavors` (dev/staging/prod) মিলে **build variant** তৈরি হয় — যেমন `devDebug`, `prodRelease`।

**Example:**

```kotlin
// android/app/build.gradle.kts (সংক্ষিপ্ত)
android {
    namespace = "com.example.myapp"
    compileSdk = 36
    defaultConfig {
        applicationId = "com.example.myapp"
        minSdk = flutter.minSdkVersion
        targetSdk = 36
    }
    flavorDimensions += "env"
    productFlavors {
        create("dev")  { dimension = "env"; applicationIdSuffix = ".dev" }
        create("prod") { dimension = "env" }
    }
}
```

```bash
flutter run --flavor dev -t lib/main_dev.dart
```

**Why it matters:** CI/CD, আলাদা environment (dev/prod), এবং Play-র compliance deadline — সবই build config-এর উপর নির্ভর করে।

**Common mistake:** targetSdk ও compileSdk গুলিয়ে ফেলা, অথবা targetSdk বাড়িয়ে নতুন OS-এর behavior change (যেমন edge-to-edge, predictive back) test না করা।

---

**Q:** AndroidManifest.xml-এ কী থাকে? Flutter app-এর Manifest-এ কোন বিষয়গুলো গুরুত্বপূর্ণ?

**A:** Manifest হলো app-এর পরিচয়পত্র: package/namespace, চারটি component (activity, service, receiver, provider) ঘোষণা, permission, intent filter, hardware/feature requirement, এবং `application` সংক্রান্ত metadata। Build-এর সময় আপনার manifest, library-র manifest ও flavor-এর manifest মিলিয়ে একটি **merged manifest** তৈরি হয় (Android Studio-র Merged Manifest ট্যাব বা `app/build/outputs/logs/manifest-merger-*.txt` দেখে দ্বন্দ্ব ধরা যায়)।

Android 12 (API 31) target করলে intent filter আছে এমন প্রতিটি component-এ `android:exported` স্পষ্ট দিতে হয়, না হলে build ব্যর্থ হয়।

**Example:**

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <uses-permission android:name="android.permission.INTERNET"/>

  <application android:label="MyApp" android:icon="@mipmap/ic_launcher">
    <activity
        android:name=".MainActivity"
        android:exported="true"
        android:launchMode="singleTop"
        android:configChanges="orientation|keyboardHidden|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
        android:windowSoftInputMode="adjustResize">
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>
  </application>
</manifest>
```

Flutter-এর `configChanges` থাকায় rotation বা dark-mode বদলালে Activity recreate হয় না; Flutter নিজেই এগুলো handle করে।

**Why it matters:** Deep link, permission, notification, background service, launch mode — সব Manifest-এ শুরু হয়। Flutter ডেভেলপাররা সবচেয়ে বেশি এখানেই আটকায়।

**Common mistake:** `android:exported` ভুলে যাওয়া, বা unnecessary permission যোগ করা (Play review-এ সমস্যা হয়)।

---

**Q:** R8/ProGuard কী করে? Flutter app-এ code shrinking ও obfuscation কীভাবে হয়?

**A:** **R8** হলো Android-এর code shrinker: (১) **shrinking** — অব্যবহৃত class/method মুছে ফেলে, (২) **optimization**, (৩) **obfuscation** — class/method নাম ছোট করে (a, b, c)। Flutter docs অনুযায়ী release build-এ R8 ডিফল্টভাবে চালু থাকে (বন্ধ করতে `--no-shrink`)। R8 Android host অংশ (Java/Kotlin) ছোট করে; **Dart কোড obfuscate করতে আলাদা flag** `--obfuscate --split-debug-info` দিতে হয়।

সমস্যা হয় **reflection** বা JSON model-এ — R8 নাম বদলে ফেললে runtime-এ খুঁজে পায় না। তখন `proguard-rules.pro`-তে `-keep` rule দিতে হয়। Build-এর সাথে `mapping.txt` তৈরি হয়; production crash decode করতে এটি Play Console/Crashlytics-এ upload করতে হয়।

**Example:**

```
# android/app/proguard-rules.pro
-keep class com.mycompany.sdk.models.** { *; }   # reflection-নির্ভর SDK model
-keepclassmembers class * { @com.google.gson.annotations.SerializedName <fields>; }
```

নতুন নিয়ম: যে app Android 15+ target করে এবং native `.so` ব্যবহার করে, সেটিকে **16 KB page size** সমর্থন করতে হবে (native library 16 KB-aligned হতে হবে)। তাই AGP, NDK ও Flutter-এর সাম্প্রতিক version ব্যবহার করুন এবং third-party native SDK গুলো যাচাই করুন।

**Why it matters:** App size, security (reverse-engineering কঠিন করা) ও release-only crash — তিনটিই এর সাথে জড়িত।

**Common mistake:** 'Obfuscation = security' ভাবা। এটা শুধু reverse-engineering কঠিন করে, secret (API key) লুকায় না। আর release build debug mode-এর মতো test না করে সরাসরি ship করা (R8 বিগড়ালে শুধু release-এ crash হয়)।

---

## ৩. App Components ও Lifecycle: Activity, Fragment, Service, Receiver, Provider

---

**Q:** Android-এর চারটি app component কী কী? Flutter অ্যাপে এগুলোর ভূমিকা কী?

**A:** Component হলো app-এর entry point — system এগুলোর মাধ্যমে আপনার app চালু করে বা সাথে কথা বলে:

| Component | কাজ | উদাহরণ |
| --- | --- | --- |
| **Activity** | UI সহ একটি screen / user interaction-এর entry | MainActivity, login screen |
| **Service** | UI ছাড়া background কাজ | গান বাজানো, location tracking |
| **BroadcastReceiver** | system বা অন্য app-এর event শোনা | boot complete, battery low |
| **ContentProvider** | structured data share করা | Contacts, FileProvider |

চারটিই সাধারণত `AndroidManifest.xml`-এ declare করতে হয় (BroadcastReceiver কোডেও dynamically register করা যায়)। Flutter অ্যাপে সাধারণত **একটিই Activity** (`FlutterActivity`) থাকে — সব Flutter screen ওই একটি Activity-র ভেতরে Dart widget হিসেবে চলে। Push notification, background কাজ বা boot-এ কিছু চালানো লাগলে Service/Receiver সরাসরি Android native স্তরে লাগে।

**Example:**

```kotlin
class MyReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // হালকা কাজ; ভারী কাজ হলে WorkManager-এ হস্তান্তর করুন
    }
}
```

```xml
<receiver android:name=".MyReceiver" android:exported="false"/>
```

**Why it matters:** Interviewer দেখে আপনি জানেন কিনা Android app আসলে কোন কোন দরজা দিয়ে চালু হয় — সেটাই lifecycle, process priority ও background-limit বোঝার ভিত্তি।

**Common mistake:** 'Flutter-এ প্রতিটি screen একটি Activity' ভাবা। না; এক Activity, ভেতরে Flutter-এর নিজস্ব Navigator।

---

**Q:** Activity lifecycle-এর callback গুলো কী কী এবং প্রতিটিতে কী করা উচিত?

**A:** Activity-র অবস্থা বদলালে system নিচের callback গুলো ক্রমানুসারে ডাকে:

```
   onCreate()  ->  onStart()  ->  onResume()      [Running: foreground, focus আছে]
                                     |
                                  onPause()        [focus হারিয়েছে; আংশিক দেখা যেতে পারে]
                                     |
                                  onStop()         [আর দেখা যাচ্ছে না]
                                     |
          (ফিরে এলে) onRestart() -> onStart()
                                     |
                                 onDestroy()       [শেষ বা recreate]
```

- `onCreate`: UI তৈরি, ViewModel/binding সেটআপ — একবারই।
- `onStart/onStop`: Activity **দৃশ্যমান** কিনা — এখানে UI update শোনা শুরু/বন্ধ করুন।
- `onResume/onPause`: **interactive ও focus** আছে কিনা — camera, sensor-এর মতো exclusive resource এখানে।
- `onDestroy`: cleanup, কিন্তু process সরাসরি kill হলে এটি **ডাকা নাও হতে পারে** — তাই গুরুত্বপূর্ণ data এখানে save করবেন না।

multi-window (Android 7+)-এ Activity দৃশ্যমান কিন্তু `onPause` অবস্থায় থাকতে পারে, তাই 'দৃশ্যমান' বোঝাতে `onPause` নয়, `onStart/onStop` ভরসা করুন।

Flutter-এ `WidgetsBindingObserver.didChangeAppLifecycleState` এর `AppLifecycleState` (resumed, inactive, hidden, paused, detached) এই Android callback গুলোর সাথে মোটামুটি মেলে — যেমন focus হারালে `inactive`, ব্যাকগ্রাউন্ডে গেলে `paused`। সঠিক mapping ফ্রেমওয়ার্ক docs-এ দেখে নিন।

**Example:**

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onStart() {
        super.onStart()
        // দৃশ্যমান হলে location updates শুরু
    }
    override fun onStop() {
        super.onStop()
        // দৃশ্যমান না থাকলে বন্ধ — battery বাঁচে
    }
}
```

```dart
class _MyState extends State<MyWidget> with WidgetsBindingObserver {
  @override
  void initState() { super.initState(); WidgetsBinding.instance.addObserver(this); }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.paused) { /* draft save */ }
  }

  @override
  void dispose() { WidgetsBinding.instance.removeObserver(this); super.dispose(); }
}
```

**Why it matters:** Lifecycle ভুল বুঝলে leak, battery drain, duplicate request ও crash হয়।

**Common mistake:** `onDestroy`-তে data save করা, বা `onPause`-কে 'app ব্যাকগ্রাউন্ডে গেছে' ধরে নেওয়া।

---

**Q:** Configuration change ও process death-এর পার্থক্য কী? ViewModel ও saved state কোনটি কখন বাঁচায়?

**A:** দুটি আলাদা ঘটনা:

- **Configuration change** (rotation, dark mode, locale, font scale): default-এ Activity **destroy হয়ে নতুন করে create** হয়, কিন্তু process বেঁচে থাকে। `ViewModel` বেঁচে থাকে।
- **Process death**: app ব্যাকগ্রাউন্ডে থাকাকালীন system memory বাঁচাতে পুরো process kill করে দেয়। user ফিরলে system Activity আবার তৈরি করে, কিন্তু **ViewModel ও সব in-memory data হারিয়ে যায়**। কেবল saved instance state (`onSaveInstanceState` / `SavedStateHandle`) থেকে ছোট data ফেরত আসে।

| অবস্থা | ViewModel | `SavedStateHandle` / Bundle | Room / DataStore |
| --- | --- | --- | --- |
| Rotation | বাঁচে | বাঁচে | বাঁচে |
| Process death | **হারায়** | বাঁচে | বাঁচে |
| User নিজে app বন্ধ (swipe away/back-exit) | হারায় | হারায় | বাঁচে |

Bundle ছোট রাখতে হয় (অল্প KB) — বড় হলে `TransactionTooLargeException` হতে পারে। তাই বড় data Room-এ, শুধু ID/query/scroll position state-এ।

**Test করার উপায়:** Developer options-এ 'Don't keep activities' চালু করুন, অথবা app ব্যাকগ্রাউন্ডে পাঠিয়ে `adb shell am kill <package>`।

**Example:**

```kotlin
@HiltViewModel
class SearchViewModel @Inject constructor(
    private val state: SavedStateHandle,
    private val repo: SearchRepository
) : ViewModel() {
    // process death-এর পরেও query ফেরত আসবে
    var query: String
        get() = state["query"] ?: ""
        set(v) { state["query"] = v }
}
```

Flutter-এ process death হলে Dart state-ও হারায়। Flutter-এর `RestorationMixin` ও `restorationId` দিয়ে scroll position, form state, navigation stack restore করা যায়।

**Why it matters:** 'ফোনে অনেক app খুললে আমার app আগের জায়গায় ফেরে না' — এটি production-এর বাস্তব bug, যা Android জানলেই ধরা যায়।

**Common mistake:** 'ViewModel-এ রাখলেই সব নিরাপদ' বলা। ViewModel শুধু configuration change-এ বাঁচে।

---

**Q:** Fragment কী, তার lifecycle Activity থেকে কীভাবে আলাদা, এবং সাধারণ leak কোথায় হয়?

**A:** Fragment হলো Activity-র ভেতরের পুনর্ব্যবহারযোগ্য UI অংশ। এর দুটি lifecycle: **Fragment নিজের** (onCreate → onDestroy) এবং **এর View-এর** (onCreateView → onDestroyView)। Back stack-এ গেলে Fragment বেঁচে থাকে কিন্তু View destroy হয়। তাই View-সংক্রান্ত সবকিছু (binding, collector) **`viewLifecycleOwner`**-এর সাথে বাঁধতে হয়, `this`-এর সাথে নয়।

আধুনিক Android-এ সাধারণত **single-Activity + Navigation component/Compose Navigation** ব্যবহার হয়, Fragment-এর নতুন ব্যবহার কমছে; কিন্তু legacy codebase-এ Fragment অনেক থাকে।

**Example:**

```kotlin
class ProfileFragment : Fragment(R.layout.fragment_profile) {
    private var _binding: FragmentProfileBinding? = null
    private val binding get() = _binding!!

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        _binding = FragmentProfileBinding.bind(view)
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.state.collect { render(it) }
            }
        }
    }

    override fun onDestroyView() {
        _binding = null          // নাহলে View leak
        super.onDestroyView()
    }
}
```

**Why it matters:** Fragment leak ও 'collector দুইবার চলছে' জাতীয় bug খুবই common।

**Common mistake:** Fragment-এ `lifecycleScope` দিয়ে flow collect করা (view destroy হলেও সক্রিয় থাকে) এবং binding null না করা।

---

**Q:** Service-এর ধরন কী কী? Android 8 ও তার পরে background service-এর ওপর কী বিধিনিষেধ?

**A:** তিন ধরন:

- **Started service** — `startService()` দিয়ে চালু, নিজে `stopSelf()` না করা পর্যন্ত চলে।
- **Bound service** — client `bindService()` দিয়ে সংযুক্ত হয়ে API ব্যবহার করে; সব client unbind করলে বন্ধ।
- **Foreground service** — চলার সময় ব্যবহারকারীকে দৃশ্যমান notification দেখাতে হয়; system এটিকে kill করা থেকে বেশি রক্ষা করে।

Android 8 (API 26) থেকে app ব্যাকগ্রাউন্ডে থাকলে সাধারণ background service শুরু করা যায় না এবং কিছুক্ষণের মধ্যে বন্ধ হয়ে যায়। দীর্ঘ কাজের জন্য **WorkManager** বা user-visible কাজের জন্য **foreground service** ব্যবহার করতে হয়। Android 14 (API 34) থেকে প্রতিটি foreground service-কে manifest-এ **foreground service type** ঘোষণা করে সংশ্লিষ্ট permission নিতে হয়। বিস্তারিত সেকশন ৮-এ।

**Example:**

```xml
<service
    android:name=".TrackingService"
    android:foregroundServiceType="location"
    android:exported="false"/>
```

**Why it matters:** Flutter-এ location tracking, গান চালানো বা upload নির্ভরযোগ্য করতে এই বিধি জানা বাধ্যতামূলক; plugin ব্যর্থ হলে মূল কারণ এখানেই।

**Common mistake:** 'Service মানে আলাদা thread' ভাবা। Service default-এ main thread-এ চলে।

---

**Q:** BroadcastReceiver কীভাবে register করা হয়? Android-এর নতুন সংস্করণে কী বদলেছে?

**A:** দুই উপায়: **manifest-declared** (app বন্ধ থাকলেও কিছু broadcast পায়) এবং **context-registered** (`registerReceiver`, Activity/Service চলাকালীন)। Android 8 থেকে অধিকাংশ implicit broadcast manifest receiver-এ আসে না, তাই context-registered ব্যবহার করতে হয়। Android 14 target করলে context-registered receiver-এ `RECEIVER_EXPORTED` বা `RECEIVER_NOT_EXPORTED` flag দেওয়া বাধ্যতামূলক (system broadcast ছাড়া)।

`onReceive` main thread-এ চলে এবং দ্রুত ফিরতে হয় (প্রায় ১০ সেকেন্ডের মধ্যে, না হলে ANR); দীর্ঘ কাজ হলে `goAsync()` বা WorkManager।

**Example:**

```kotlin
val receiver = object : BroadcastReceiver() {
    override fun onReceive(c: Context, i: Intent) { /* connectivity বদলেছে */ }
}
ContextCompat.registerReceiver(
    context, receiver,
    IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION),
    ContextCompat.RECEIVER_NOT_EXPORTED
)
// onStop/onDestroy-তে unregisterReceiver() — নাহলে leak
```

**Why it matters:** Connectivity, boot, SMS, battery — অনেক native feature Receiver-নির্ভর; plugin বানানো বা debug করতে লাগে।

**Common mistake:** `unregisterReceiver` ভুলে যাওয়া, অথবা `onReceive`-এ network call করা।

---

**Q:** Context কত ধরনের? ContentProvider ও Application class startup-এর সাথে কীভাবে জড়িত?

**A:** `Application` context পুরো process-এর জীবনকাল ধরে থাকে; `Activity` context শুধু ওই Activity-র জীবনকাল ধরে এবং theme/UI-সচেতন। দীর্ঘজীবী object (singleton, repository)-এ Activity context রাখলে পুরো Activity **leak** করে। তাই সেখানে `applicationContext` ব্যবহার করুন।

প্রক্রিয়া চালুর ক্রম: `Application.attachBaseContext` → **ContentProvider-গুলোর `onCreate`** → `Application.onCreate` → প্রথম Activity। অনেক SDK (যেমন Firebase) নিজেদের init একটি ContentProvider দিয়ে করে — ফলে app startup ধীর হয়। `androidx.startup` (App Startup) এ একই provider দিয়ে সব initializer একত্র করা যায়।

**Example:**

```kotlin
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        // শুধু অত্যাবশ্যক init এখানে; বাকিটা lazy বা background-এ
    }
}
```

**Why it matters:** Cold start ধীর হলে প্রথম কারণ সাধারণত Application/Provider-এ ভারী init। Flutter অ্যাপেও Android host অংশের startup এই পথে যায়।

**Common mistake:** `Application.onCreate`-এ সব SDK একসাথে init করা, আর singleton-এ Activity context রাখা।

---

## ৪. Intent, Task/Back Stack, Launch Mode, Deep Link

---

**Q:** Explicit ও Implicit Intent-এর পার্থক্য কী? Intent filter ও PendingIntent কীভাবে কাজ করে?

**A:** **Intent** হলো 'কিছু করতে চাই' বার্তা — component চালু করা বা তথ্য পাঠানো।

- **Explicit intent**: নির্দিষ্ট class উল্লেখ করা হয় (নিজের app-এর ভেতরে)।
- **Implicit intent**: শুধু action/data বলা হয় (যেমন VIEW একটি URL), system ম্যাচিং **intent filter** আছে এমন component খোঁজে; একাধিক হলে chooser দেখায়।

**PendingIntent** হলো একটি Intent-কে অন্য কাউকে (notification, AlarmManager) আপনার হয়ে চালানোর অনুমতি দেওয়া। Android 12 (API 31) থেকে তৈরির সময় `FLAG_IMMUTABLE` অথবা `FLAG_MUTABLE` স্পষ্ট দিতে হয় — নিরাপত্তার জন্য ডিফল্ট `FLAG_IMMUTABLE` রাখুন।

Android 11+ এ অন্য app খুঁজে বের করতে (package visibility) manifest-এ `<queries>` ঘোষণা লাগে।

**Example:**

```kotlin
// Explicit
startActivity(Intent(this, DetailActivity::class.java).putExtra("id", 42))

// Implicit — ব্রাউজারে লিংক খোলা
val i = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))
if (i.resolveActivity(packageManager) != null) startActivity(i)   // Android 11+ এ <queries> লাগতে পারে

// PendingIntent (notification tap)
val pi = PendingIntent.getActivity(
    this, 0, Intent(this, MainActivity::class.java),
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)
```

**Why it matters:** Deep link, notification tap, share sheet, payment/OAuth redirect — সবই Intent। Security প্রশ্নও (exported component, mutable PendingIntent) এখান থেকে আসে।

**Common mistake:** implicit intent দিয়ে নিজের app-এর ভেতরের কাজ করা (অন্য app আটকে নিতে পারে), আর `PendingIntent`-এ flag না দেওয়া।

---

**Q:** Task, Back Stack এবং Launch Mode কী? Flutter-এর MainActivity কেন `singleTop`?

**A:** **Task** হলো ব্যবহারকারীর একটি কাজের জন্য Activity-র সমষ্টি; ভেতরের Activity-গুলো **back stack**-এ (LIFO) সাজানো থাকে। Launch mode ঠিক করে নতুন Activity instance তৈরি হবে কিনা:

| Launch mode | আচরণ |
| --- | --- |
| `standard` (ডিফল্ট) | প্রতিবার নতুন instance |
| `singleTop` | টপে একই Activity থাকলে নতুন instance না বানিয়ে `onNewIntent()` ডাকে |
| `singleTask` | task-এ একটিই instance; থাকলে তার উপরের সব Activity সরিয়ে সেটিকে সামনে আনে |
| `singleInstance` | নিজের আলাদা task-এ একা থাকে |
| `singleInstancePerTask` (API 31+) | প্রতি task-এ সর্বোচ্চ একটি instance |

Flutter template-এর `MainActivity` `singleTop` — যাতে notification tap বা deep link এলে নতুন Activity (এবং নতুন Flutter UI) না বানিয়ে চলমান Activity-তেই intent পৌঁছায়, আর Flutter Engine সেই intent-টি Dart-এ (যেমন `go_router`) পাঠাতে পারে।

```
Back stack (টপ = ডানে):  [Main] -> [List] -> [Detail]
singleTop: Detail টপে থাকলে আবার Detail লঞ্চ -> নতুন বানায় না, onNewIntent()
```

**Example:**

```xml
<activity android:name=".MainActivity"
          android:launchMode="singleTop" ... />
```

```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)   // নতুন intent-টি হাতে নিন
}
```

**Why it matters:** 'Notification ট্যাপ করলে app দুইবার খুলছে' জাতীয় bug launch mode না জানলে ধরা যায় না।

**Common mistake:** সব জায়গায় `singleTask` দিয়ে দেওয়া — এতে back আচরণ অপ্রত্যাশিত হয়।

---

**Q:** Deep Link আর Android App Link-এর পার্থক্য কী? কীভাবে verify হয়? Flutter-এ কীভাবে হ্যান্ডেল করবেন?

**A:**

- **Deep link**: যেকোনো URI scheme/URL যা app-এর নির্দিষ্ট screen খোলে (`myapp://product/12`)। একাধিক app একই scheme দাবি করতে পারে, তাই chooser আসতে পারে।
- **Android App Link**: `https` URL, যা আপনার ডোমেইনের সাথে **verified** — ব্যবহারকারী link ট্যাপ করলে সরাসরি আপনার app খোলে, chooser ছাড়াই।

Verify করতে: (১) Manifest-এ `android:autoVerify="true"` সহ `https` intent filter, (২) ডোমেইনে `https://example.com/.well-known/assetlinks.json` ফাইলে app package ও **signing certificate-এর SHA-256 fingerprint**। Play App Signing ব্যবহার করলে Play Console-এর **app signing certificate** fingerprint দিতে হবে (শুধু upload key নয়)।

Flutter-এ ডিফল্টভাবে engine intent-টি Dart-এ পাঠায় এবং `go_router`/Router সেটি route-এ রূপান্তর করে (Flutter 3.27 থেকে deep link handling ডিফল্ট চালু বলে ডকুমেন্টেশনে আছে; Navigator/Router নিজে হ্যান্ডেল করলে `flutter_deeplinking_enabled` meta-data দিয়ে বন্ধ করা যায় — আপনার Flutter version-এর docs দেখে নিন)।

**Example:**

```xml
<intent-filter android:autoVerify="true">
  <action android:name="android.intent.action.VIEW"/>
  <category android:name="android.intent.category.DEFAULT"/>
  <category android:name="android.intent.category.BROWSABLE"/>
  <data android:scheme="https" android:host="example.com" android:pathPrefix="/product"/>
</intent-filter>
```

```bash
# টেস্ট
adb shell am start -a android.intent.action.VIEW -d "https://example.com/product/12" com.example.app
adb shell pm get-app-links com.example.app          # verification অবস্থা
adb shell pm verify-app-links --re-verify com.example.app
```

```dart
final router = GoRouter(routes: [
  GoRoute(path: '/product/:id',
    builder: (_, s) => ProductPage(id: s.pathParameters['id']!)),
]);
```

**Why it matters:** Marketing link, referral, password reset, payment redirect — সবই deep link। Verify ব্যর্থ হওয়া production-এর খুব সাধারণ সমস্যা।

**Common mistake:** debug/upload key-র fingerprint দিয়ে `assetlinks.json` বানানো, অথচ Play-তে ইনস্টল হওয়া app-টি Google-এর app signing key দিয়ে signed। ফলে verify হয় না।

---

**Q:** `startActivityForResult` কেন deprecated? Activity Result API কীভাবে কাজ করে?

**A:** পুরোনো পদ্ধতিতে request code ও `onActivityResult`-এ সব ফলাফল একজায়গায় মিশে যেত, আর lifecycle/process death-এ ভঙ্গুর ছিল। **Activity Result API** (`registerForActivityResult`) প্রতিটি কাজের জন্য আলাদা, type-safe contract দেয় এবং lifecycle-aware। Permission চাওয়া, ছবি বাছাই, document খোলা — সবই এ পথে।

Flutter plugin লিখলে native দিকে `ActivityPluginBinding.addActivityResultListener(...)` ব্যবহার হয়; কারণ plugin নিজে Activity-র মালিক নয়।

**Example:**

```kotlin
val pickImage = registerForActivityResult(ActivityResultContracts.PickVisualMedia()) { uri ->
    uri?.let { showPreview(it) }     // Photo Picker — স্টোরেজ permission লাগে না
}

button.setOnClickListener {
    pickImage.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
}
```

**Why it matters:** Permission ও media বাছাই আধুনিক Android-এর নিত্যকাজ; পুরোনো API জানলে legacy plugin বুঝতেও সুবিধা হয়।

**Common mistake:** `registerForActivityResult` onCreate/Fragment তৈরির সময়ের আগেই (class property হিসেবে) না করে ক্লিকের ভেতরে register করা — এতে crash হয়।

---

**Q:** Android-এ Back হ্যান্ডেলিং কীভাবে বদলেছে? Predictive Back ও Flutter-এর `PopScope` কী?

**A:** `onBackPressed()` override করার পুরোনো পদ্ধতির বদলে এখন `OnBackPressedDispatcher` + `OnBackPressedCallback` ব্যবহার হয়। **Predictive Back** জেশ্চারে user ব্যাক সোয়াইপ শুরু করলেই আগে থেকে পূর্বরূপ (পেছনের screen/home) দেখা যায়, তাই app-কে আগেই জানাতে হয় সে back নিজে handle করে কিনা — সেজন্য callback-ভিত্তিক API।

Google-এর নথি অনুযায়ী Android 16 (API 36) target করলে এবং Android 16 ডিভাইসে predictive back animation ডিফল্টভাবে চালু থাকে এবং `onBackPressed` আর ডাকা হয় না; পুরোনো API-নির্ভর হলে `android:enableOnBackInvokedCallback="false"` দিয়ে সাময়িকভাবে বন্ধ করা যায় ([Android 16 behavior changes](https://developer.android.com/about/versions/16/behavior-changes-16))। Play-তে এখন target 36 লাগে, তাই এটি সরাসরি প্রযোজ্য।

Flutter-এ `WillPopScope` deprecated; তার জায়গায় **`PopScope`** (`canPop`, `onPopInvokedWithResult`)।

**Example:**

```kotlin
onBackPressedDispatcher.addCallback(this) {
    if (hasUnsavedChanges) showDiscardDialog() else { isEnabled = false; onBackPressedDispatcher.onBackPressed() }
}
```

```dart
PopScope(
  canPop: !hasUnsavedChanges,
  onPopInvokedWithResult: (didPop, result) {
    if (!didPop) showDiscardDialog(context);
  },
  child: const EditorPage(),
)
```

```xml
<application android:enableOnBackInvokedCallback="true" ...>
```

**Why it matters:** target 36-এর পরে back আচরণ ভেঙে যাওয়া একটি বাস্তব migration ঝুঁকি; Flutter dev-দের `PopScope` সঠিকভাবে ব্যবহার করতে হয়।

**Common mistake:** `WillPopScope` (async decision) ধরনের লজিক `PopScope`-এ সরাসরি কপি করা — `canPop` একটি সিঙ্ক্রোনাস মান, আগে থেকে ঠিক করে রাখতে হয়।

---

**Q:** Android Navigation Component, Compose Navigation এবং Flutter-এর `go_router` মিলিয়ে দেখলে কী মিল-অমিল?

**A:** তিনটিই 'route → screen' মানচিত্র ও back stack পরিচালনা করে। আধুনিক Android-এ সাধারণত **single Activity + NavHost**।

| বিষয় | Android Navigation | Flutter `go_router` |
| --- | --- | --- |
| Route সংজ্ঞা | NavGraph / `composable("route")` | `GoRoute(path: ...)` |
| আর্গুমেন্ট | SafeArgs / type-safe route (Kotlin Serialization) | `pathParameters`, `extra` |
| Deep link | `navDeepLink { uriPattern = ... }` | path match (URL = source of truth) |
| Back stack | NavController back stack | Navigator pages / `GoRouter.pop` |
| Nested/Bottom nav | nested graph | `ShellRoute`, `StatefulShellRoute` |

**Example:**

```kotlin
NavHost(navController, startDestination = "home") {
    composable("home") { HomeScreen(onOpen = { id -> navController.navigate("detail/$id") }) }
    composable("detail/{id}", arguments = listOf(navArgument("id") { type = NavType.IntType })) { DetailScreen() }
}
```

**Why it matters:** একই architecture-সিদ্ধান্ত (route-কে কে মালিকানা দেবে, deep link কীভাবে ম্যাপ হবে) দুই stack-এই আসে; তুলনা করতে পারলে দুই জায়গাতেই আপনি senior।

**Common mistake:** পুরো object route-এর আর্গুমেন্টে পাঠানো। শুধু ID পাঠিয়ে destination-এ data load করাই নিরাপদ (process death ও deep link-এ কাজ করে)।

---

## ৫. Kotlin ও Concurrency: Coroutines, Flow, Dart-এর সাথে তুলনা

---

**Q:** Java জানা থাকলে Kotlin-এর মোলিক পার্থক্যগুলো কী কী, এবং Dart-এর সাথে কোথায় মিল?

**A:** Kotlin-এ null safety, immutability ও সংক্ষিপ্ত সিনট্যাক্স মূল বৈশিষ্ট্য। Dart জানলে অনেককিছু পরিচিত লাগবে:

| বৈশিষ্ট্য | Java | Kotlin | Dart-এর মিল |
| --- | --- | --- | --- |
| Null safety | `@Nullable` নিয়মানুবর্তিতা | `String` vs `String?` (compile-time) | `String` vs `String?` একই |
| Immutable binding | `final` | `val` / `var` | `final` / `var` |
| Data class | boilerplate/`record` | `data class` | `freezed` বা Dart records |
| Extension | নেই | `fun String.x()` | `extension on String` |
| Default/named args | নেই | আছে | named parameters আছে |
| Sealed type | Java 17 sealed | `sealed class/interface` | Dart 3 `sealed class` |
| Smart cast | হয় না | `if (x is T) x.foo()` | type promotion |
| Singleton | বানাতে হয় | `object` | নেই (static/factory) |

**Example:**

```kotlin
data class User(val id: Int, val name: String?)

fun String.initials() = split(" ").filter { it.isNotBlank() }.joinToString("") { it.first().uppercase() }

sealed interface UiState {
    data object Loading : UiState
    data class Success(val items: List<String>) : UiState
    data class Error(val message: String) : UiState
}

fun render(s: UiState) = when (s) {        // exhaustive — নতুন case যোগ করলে compiler error
    UiState.Loading -> "..."
    is UiState.Success -> s.items.size.toString()
    is UiState.Error -> s.message
}

val name = user?.name ?: "Guest"           // safe-call + elvis
```

Scope function (`let`, `apply`, `run`, `also`, `with`) ও পরিচিত হতে হবে: `apply` অবজেক্ট configure করতে, `let` nullable-এর কাজে।

**Why it matters:** Kotlin জানা Android senior-এর ন্যূনতম শর্ত; sealed class + `when` দিয়ে UI state modeling সবচেয়ে বেশি জিজ্ঞাসা হয়।

**Common mistake:** `!!` (not-null assertion) বারবার ব্যবহার করা — এটি NPE ফিরিয়ে আনে। `?.`, `?:`, `let` ব্যবহার করুন।

---

**Q:** Coroutine কী? Thread-এর সাথে পার্থক্য কী? Structured concurrency বলতে কী বোঝায়?

**A:** Coroutine হলো হালকা, suspend করা যায় এমন কাজের একক। `suspend` function **thread block না করে** কাজ থামিয়ে রাখতে পারে এবং পরে আবার চালু হয়। লক্ষ লক্ষ coroutine কয়েকটি thread-এ চলতে পারে, কিন্তু লক্ষ thread বানানো যায় না।

**Structured concurrency**: প্রতিটি coroutine একটি **scope**-এর অধীনে চলে। Scope cancel হলে সব child cancel হয়; child-এ exception হলে parent জানতে পারে; parent তার সব child শেষ না হওয়া পর্যন্ত শেষ হয় না। ফলে 'ভুলে যাওয়া কাজ' (leak) কমে।

Android-এ তিনটি প্রধান scope: `viewModelScope` (ViewModel clear হলে cancel), `lifecycleScope` (lifecycle destroy হলে), এবং `rememberCoroutineScope` (Compose-এ)।

**Example:**

```kotlin
class ProfileViewModel(private val repo: UserRepo) : ViewModel() {
    fun load() = viewModelScope.launch {
        // দুটি call সমান্তরালে; একটি fail করলে অন্যটিও cancel
        val (user, posts) = coroutineScope {
            val u = async { repo.user() }
            val p = async { repo.posts() }
            u.await() to p.await()
        }
        _state.value = ProfileState(user, posts)
    }
}
```

**Why it matters:** Structured concurrency বোঝা মানে আপনি leak-free async কোড লিখতে পারেন।

**Common mistake:** `GlobalScope.launch` ব্যবহার করা — এটি lifecycle-সচেতন নয়, leak করে; আর 'সব coroutine = নতুন thread' বলা।

---

**Q:** Dispatcher কী? `Main`, `IO`, `Default` কখন কোনটি? `withContext` কী করে?

**A:** Dispatcher ঠিক করে coroutine কোন thread/pool-এ চলবে:

- `Dispatchers.Main` — UI thread (UI update, হালকা কাজ); `Main.immediate` অন্যথায় dispatch ছাড়াই চালায়।
- `Dispatchers.IO` — blocking I/O (network, disk, DB)।
- `Dispatchers.Default` — CPU-ভারী কাজ (sort, parse, image processing)।

`withContext(d) { }` বলে: এই অংশ `d`-এ চালাও, শেষ হলে আগের context-এ ফিরে এসো। **Main-safe** function বলতে বোঝায় যেটি main thread থেকে ডাকলে block করবে না — তাই repository/data layer নিজের dispatcher বেছে নেয়, caller-কে নয়। Test-এর জন্য dispatcher constructor-এ inject করুন।

**Example:**

```kotlin
class UserRepo(
    private val api: Api,
    private val io: CoroutineDispatcher = Dispatchers.IO
) {
    suspend fun user(): User = withContext(io) { api.getUser() }   // main-safe
}
```

**Why it matters:** প্রশ্ন: 'কেন IO ? Default নয়?' — উত্তর: IO pool বড়, blocking call-এর জন্য; Default CPU core সংখ্যার সমান, CPU-bound কাজের জন্য।

**Common mistake:** সব জায়গায় `Dispatchers.IO` hardcode করা (test কঠিন হয়), অথবা CPU-ভারী কাজ main-এ রাখা।

---

**Q:** Coroutine-এ exception ও cancellation কীভাবে হ্যান্ডেল করবেন? `SupervisorJob` কী?

**A:** নিয়মগুলো:

- `launch`-এ exception ওপরে parent-এ ছড়িয় পড়ে (uncaught হলে crash); `async`-এ exception `await()` করলে দেখা যায় (তবে parent-কেও জানায়)। `try/catch` coroutine **ভেতরে** রাখলে কাজ করে; `launch { }` ব্লকের বাইরে নয়।
- প্রতিটি child স্বাধীনভাবে fail করলে বাকিরা থামবে না — এমন চাইলে `SupervisorJob`/`supervisorScope`। `viewModelScope` সাধারণত SupervisorJob ব্যবহার করে।
- **Cancellation** cooperative: `CancellationException` স্বাভাবিক ঘটনা, `catch (e: Exception)` দিয়ে গিলে ফেললে cancel ভেঙে যায় — আবার throw করুন।
- `CoroutineExceptionHandler` শুধু root `launch`-এ কাজ করে, `async`-এ নয়।

**Example:**

```kotlin
viewModelScope.launch {
    try {
        val data = repo.fetch()
        _state.value = Success(data)
    } catch (e: CancellationException) {
        throw e                      // গিলবেন না
    } catch (e: IOException) {
        _state.value = Error("নেটওয়ার্ক সমস্যা")
    }
}

suspend fun loadBoth() = supervisorScope {
    val a = async { runCatching { apiA() } }
    val b = async { runCatching { apiB() } }   // একটি fail করলেও অন্যটি চলবে
    a.await() to b.await()
}
```

**Why it matters:** Production crash-এর বড় অংশ uncaught coroutine exception; interviewer exception propagation-এর মডেল বুঝেছেন কিনা দেখে।

**Common mistake:** `runCatching { suspendCall() }` দিয়ে `CancellationException` গিলে ফেলা।

---

**Q:** Flow, StateFlow ও SharedFlow-এর পার্থক্য কী? UI-তে কীভাবে সঠিকভাবে collect করবেন?

**A:**

|  | Flow | StateFlow | SharedFlow |
| --- | --- | --- | --- |
| প্রকৃতি | **Cold** (collect করলে শুরু) | **Hot**, সর্বদা একটি মান আছে | **Hot**, event stream |
| Initial value | না | লাগে | না (replay কনফিগারেবল) |
| সমান মান পাঠালে | পাঠায় | অগ্রাহ্য (distinct) | পাঠায় |
| ব্যবহার | repository stream, DB observe | **UI state** | একক event (toast, navigation) |

Room থেকে `Flow<List<T>>` পেলে ডেটা বদলালেই আপনি নতুন মান পাবেন। ViewModel-এ `stateIn(..., SharingStarted.WhileSubscribed(5_000), initial)` ব্যবহার করলে UI ব্যাকগ্রাউন্ডে গেলে upstream পাঁচ সেকেন্ড পর থামে (rotation-এ নয়)।

**Example:**

```kotlin
val uiState: StateFlow<UiState> = repo.observeItems()
    .map<List<Item>, UiState> { UiState.Success(it) }
    .catch { emit(UiState.Error(it.message ?: "")) }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), UiState.Loading)

// View system
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) { vm.uiState.collect(::render) }
}

// Compose
val state by vm.uiState.collectAsStateWithLifecycle()
```

**Why it matters:** সঠিক collect ছাড়া ব্যাকগ্রাউন্ডে বৃথা network/DB কাজ চলে, battery ও data নষ্ট হয়।

**Common mistake:** one-off event-কে StateFlow-এ রাখা (rotation-এ আবার toast দেখায়), আর `lifecycleScope.launch { flow.collect }` ব্যাকগ্রাউন্ডেও চালু রাখা।

---

**Q:** Dart-এর async মডেল (Future/Stream/Isolate) ও Kotlin-এর (suspend/Flow/Dispatcher) একসাথে বললে মিল-অমিল কী?

**A:**

| Dart/Flutter | Kotlin/Android | পার্থক্য |
| --- | --- | --- |
| `Future<T>` | `suspend fun` / `Deferred<T>` | Dart Future শুরুর সাথে সাথে eager; Kotlin-এ structured scope-এর ভেতর |
| `Stream<T>` | `Flow<T>` | Dart single-subscription/broadcast; Flow cold ও operator-সমৃদ্ধ |
| `async/await` | `suspend` + স্বাভাবিক কোড | Kotlin-এ `await` লাগে শুধু `async` Deferred-এ |
| Single-threaded event loop + microtask | Dispatcher/thread pool | Dart-এ একই isolate-এ সব এক thread; Kotlin এ বহু thread |
| `Isolate` (মেমোরি shared নয়, message pass) | `withContext(Dispatchers.Default)` (মেমোরি shared) | Dart-এ data race সম্ভব নয়; Kotlin-এ সম্ভব, synchronization দরকার |
| Cancellation সীমিত (Stream `cancel`, `CancelableOperation`) | Job cancellation সমৃদ্ধ | Kotlin-এ বড় সুবিধা |

**Example:**

```dart
// Dart: ভারী কাজ isolate-এ
final result = await Isolate.run(() => parseHugeJson(text));
```

```kotlin
// Kotlin: একই কাজ Default dispatcher-এ
val result = withContext(Dispatchers.Default) { parseHugeJson(text) }
```

**Why it matters:** এক প্ল্যাটফর্মের গভীর জ্ঞান অন্যটিতে রূপান্তর করার ক্ষমতাই 'Flutter + Android' রোলের মূলধন।

**Common mistake:** Dart isolate-কে thread ভাবা (মেমোরি shared নয়) অথবা Kotlin coroutine-কে Dart Future-এর মতো 'fire and forget' ভাবা।

---

**Q:** পুরোনো Android কোডবেসে AsyncTask, Handler, RxJava, Executor দেখলে কীভাবে মাইগ্রেট করবেন?

**A:** `AsyncTask` Android 11 (API 30) থেকে deprecated। Handler/Executor-এর বদলে সরাসরি coroutine, RxJava `Observable` বদলে `Flow`। প্রস্তাবিত কৌশল: (১) নতুন কোড coroutine-এ লিখুন, (২) পুরোনো কোডে adapter দিন — `kotlinx-coroutines-rx3` দিয়ে Rx ↔ Flow, callback-কে `suspendCancellableCoroutine`/`callbackFlow` দিয়ে মোড়ান, (৩) সবচেয়ে পরিসরে নির্ভরশীল অংশ আগে মাইগ্রেট করুন।

**Example:**

```kotlin
// callback API -> suspend
suspend fun Location.await(client: FusedLocationProviderClient): Location =
    suspendCancellableCoroutine { cont ->
        client.lastLocation
            .addOnSuccessListener { cont.resume(it) }
            .addOnFailureListener { cont.resumeWithException(it) }
    }
```

**Why it matters:** Legacy codebase-এ কাজ করার সময় সবচেয়ে বেশি লাগে incremental migration-এর দক্ষতা।

**Common mistake:** একবারে সব rewrite করার প্রস্তাব, যাতে রিস্ক ও সময় উভয়ই বেশি।

---

## ৬. Android UI: View System বনাম Jetpack Compose

---

**Q:** Android-এর পুরোনো View system স্ক্রিনে UI কীভাবে আঁকে? `invalidate()` আর `requestLayout()`-এর পার্থক্য কী?

**A:** সহজ ভাষায়: প্রতিটি frame আঁকার আগে Android তিনটি কাজ করে।

1. **Measure** — প্রতিটি View জিজ্ঞেস করা হয়: 'তোমার কত জায়গা লাগবে?'
2. **Layout** — প্রতিটি View-কে স্ক্রিনে তার জায়গা ঠিক করে দেওয়া হয়।
3. **Draw** — আসল ছবি আঁকা হয়।

উপমা: ঘর সাজানো — আগে মাপো (measure), তারপর কোন জিনিস কোথায় রাখবে ঠিক করো (layout), শেষে রং করো (draw)।

- `invalidate()` → শুধু **আবার আঁকো** (রং বদলেছে, size একই)। সস্তা।
- `requestLayout()` → **আবার মাপো ও সাজাও** (size বদলেছে)। ভারী, কারণ পুরো tree ঘুরে আসে।

View tree যত গভীর, measure/layout তত ধীর। তাই `ConstraintLayout` দিয়ে flat hierarchy রাখা ভালো।

```
FrameLayout
 └─ LinearLayout
     ├─ TextView
     └─ LinearLayout
         └─ Button        <- গভীর nesting = ধীর measure
```

**Example:**

```kotlin
class BadgeView(ctx: Context) : View(ctx) {
    var count = 0
        set(v) { field = v; invalidate() }      // শুধু রং/লেখা বদলেছে → invalidate

    var badgeSize = 24
        set(v) { field = v; requestLayout() }   // size বদলেছে → requestLayout
}
```

**Why it matters:** Interviewer দেখে আপনি 'কেন স্ক্রিন ধীর' তার কারণ বোঝেন কিনা। Flutter-এর build→layout→paint ঠিক এরই আধুনিক রূপ।

**Common mistake:** `onDraw()`-এর ভেতরে নতুন object (Paint, Path) বানানো — প্রতি frame-এ বানালে GC চাপ বাড়ে, jank হয়।

---

**Q:** RecyclerView কীভাবে কাজ করে? `DiffUtil` কেন লাগে? Flutter-এর `ListView.builder`-এর সাথে মিল কী?

**A:** ১০ হাজার item-এর list-এ ১০ হাজার View বানালে মেমরি শেষ। তাই RecyclerView শুধু **স্ক্রিনে দেখা যায় এমন কয়েকটি** View বানায়। item স্ক্রিনের বাইরে গেলে সেই View-টি **ফেলে না দিয়ে পুনরায় ব্যবহার (recycle)** করে নতুন item দেখাতে। উপমা: রেস্টুরেন্টে ১০টি প্লেট ধুয়ে বারবার ব্যবহার, ১০০০টি প্লেট কেনা নয়।

- **ViewHolder** — একটি row-এর View-গুলো ধরে রাখে (বারবার `findViewById` এড়ায়)।
- **Adapter** — data কে row-এ বসায়।
- **DiffUtil / ListAdapter** — পুরোনো ও নতুন list তুলনা করে শুধু **বদলানো অংশ** update করে (পুরো list redraw নয়)।

Flutter-এ `ListView.builder` লোড হওয়ার সময় শুধু দৃশ্যমান item-এর widget বানায় — একই ধারণা।

**Example:**

```kotlin
class UserAdapter : ListAdapter<User, UserVH>(Diff) {
    object Diff : DiffUtil.ItemCallback<User>() {
        override fun areItemsTheSame(a: User, b: User) = a.id == b.id      // একই item কিনা (id দিয়ে)
        override fun areContentsTheSame(a: User, b: User) = a == b         // ভেতরের data বদলেছে কিনা
    }
    override fun onCreateViewHolder(p: ViewGroup, t: Int) =
        UserVH(ItemUserBinding.inflate(LayoutInflater.from(p.context), p, false))
    override fun onBindViewHolder(h: UserVH, pos: Int) = h.bind(getItem(pos))
}
// ব্যবহার: adapter.submitList(newUsers)
```

**Why it matters:** ব্যবহারকারী যে list নিয়ে সবচেয়ে বেশি scroll করে, সেখানে performance-ই UX।

**Common mistake:** `notifyDataSetChanged()` দিয়ে সবসময় পুরো list refresh করা (animation হারায়, ধীর), আর `areItemsTheSame`-এ position ব্যবহার করা — id ব্যবহার করুন।

---

**Q:** Jetpack Compose কী? Flutter-এর সাথে মূল মিল ও পার্থক্য কী?

**A:** Compose হলো Android-এর আধুনিক **declarative UI**। XML লেখার বদলে Kotlin function দিয়ে UI বর্ণনা করা হয়। নিয়ম একটাই: **UI = f(state)** — state বদলালে UI নিজে নিজে নতুন করে আঁকে (ঠিক Flutter-এর মতো)।

| বিষয় | Jetpack Compose | Flutter |
| --- | --- | --- |
| ভাষা | Kotlin | Dart |
| UI একক | `@Composable` function | `Widget` class |
| State | `remember { mutableStateOf() }` | `setState` / Riverpod / BLoC |
| Rebuild | **Recomposition** (শুধু যে অংশ state পড়ে) | `build()` পুনরায় চলে |
| Layout | `Row`, `Column`, `Box` | `Row`, `Column`, `Stack` |
| List | `LazyColumn` | `ListView.builder` |
| Rendering | Android-এর নিজস্ব graphics stack | নিজস্ব Flutter Engine (Impeller) |
| প্ল্যাটফর্ম | শুধু Android | Android, iOS, web, desktop |

**Example:**

```kotlin
@Composable
fun Counter() {
    var count by rememberSaveable { mutableIntStateOf(0) }
    Column(horizontalAlignment = Alignment.CenterHorizontally) {
        Text("Count: $count")
        Button(onClick = { count++ }) { Text("+1") }
    }
}
```

```dart
class Counter extends StatefulWidget { /* ... */ }
class _CounterState extends State<Counter> {
  int count = 0;
  @override
  Widget build(BuildContext c) => Column(children: [
    Text('Count: $count'),
    ElevatedButton(onPressed: () => setState(() => count++), child: const Text('+1')),
  ]);
}
```

**Why it matters:** Flutter জানা থাকলে Compose শেখা সহজ — এটাই আপনার সুবিধা। এটা বলতে পারলে 'দুই stack-এ কাজ করতে পারি' প্রমাণ হয়।

**Common mistake:** Compose-কে 'শুধু XML-এর বিকল্প' ভাবা। আসলে এটা ভিন্ন চিন্তাধারা (state-driven)।

---

**Q:** Recomposition কী? কীভাবে অপ্রয়োজনীয় recomposition আটকাবেন? `remember`, `rememberSaveable`, state hoisting কী?

**A:** state বদলালে Compose সেই state পড়ে এমন function-গুলো **আবার চালায়** — একে recomposition বলে। ভালো কথা: Compose চালাক, যে অংশ বদলায়নি সেটা এড়িয়ে যায় (skip)।

- `remember { }` — recomposition-এর মধ্যেও মান মনে রাখে। কিন্তু **rotation বা process death-এ হারায়**।
- `rememberSaveable { }` — rotation ও process death-এও মান বাঁচায় (Bundle-এ সংরক্ষণ)।
- **State hoisting** — state নিজের ভেতরে না রেখে **উপরে (caller/ViewModel-এ)** তুলে দেওয়া; composable শুধু `state` ও `onEvent` নেয়। ফলে composable সহজে test ও reuse করা যায়।
- `LazyColumn`-এ `key` দিন, না হলে item সরলে ভুল state লেগে যেতে পারে।
- `derivedStateOf` — বারবার বদলানো state থেকে কম বদলানো মান বের করতে (যেমন scroll position থেকে 'top-এ যাও' বাটন)।
- নতুন Kotlin (২.০.২০+) compiler-এ strong skipping ডিফল্ট চালু, তাই stability নিয়ে আগের চেয়ে কম মাথা ঘামাতে হয়। তবুও list-এ অস্থির (unstable) type ও লম্বা lambda ধরে রাখলে recomposition বাড়ে — Layout Inspector-এর recomposition count দেখে যাচাই করুন।

**Example:**

```kotlin
@Composable
fun CounterScreen(vm: CounterViewModel = hiltViewModel()) {
    val state by vm.state.collectAsStateWithLifecycle()
    CounterContent(count = state.count, onIncrement = vm::increment)   // state উপরে, UI নিচে
}

@Composable
fun CounterContent(count: Int, onIncrement: () -> Unit) {              // stateless, test-friendly
    Button(onClick = onIncrement) { Text("Count: $count") }
}

LazyColumn {
    items(users, key = { it.id }) { UserRow(it) }
}

val showTopBtn by remember { derivedStateOf { listState.firstVisibleItemIndex > 3 } }
```

**Why it matters:** Compose performance প্রশ্নের মূল উত্তর এখানেই — 'কম অংশ recompose করুন, state নিচে নয়, উপরে রাখুন'।

**Common mistake:** `remember` দিয়ে সবকিছু ধরে রাখা (rotation-এ হারায়), অথবা composable-এর ভেতরে সরাসরি ভারী কাজ (sort, network) করা।

---

**Q:** Compose-এর Side-effect API (`LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope`) কেন লাগে? Flutter-এ এদের সমতুল্য কী?

**A:** Composable function বারবার চলতে পারে, তাই এর ভেতরে সরাসরি network call বা listener লাগালে সেটা বারবার চলবে। যে কাজ UI আঁকা নয় (side-effect), সেগুলোর জন্য আলাদা API:

| Compose API | কাজ | Flutter সমতুল্য |
| --- | --- | --- |
| `LaunchedEffect(key)` | key বদলালে coroutine চালু, leave করলে cancel | `initState` + `didUpdateWidget` |
| `DisposableEffect(key)` | setup + `onDispose` cleanup (listener) | `initState` + `dispose` |
| `rememberCoroutineScope()` | click-এর মতো event থেকে coroutine চালাতে | event handler-এ `async` call |
| `SideEffect` | প্রতি সফল recomposition-এর পর non-Compose কিছু জানাতে | `WidgetsBinding.addPostFrameCallback` |
| `rememberUpdatedState` | long-running effect-এ সর্বশেষ lambda ধরে রাখতে | — |

**Example:**

```kotlin
@Composable
fun UserScreen(userId: String, vm: UserViewModel) {
    LaunchedEffect(userId) { vm.load(userId) }       // userId বদলালে আবার load

    val owner = LocalLifecycleOwner.current
    DisposableEffect(owner) {
        val obs = LifecycleEventObserver { _, e -> if (e == Lifecycle.Event.ON_RESUME) vm.refresh() }
        owner.lifecycle.addObserver(obs)
        onDispose { owner.lifecycle.removeObserver(obs) }   // না দিলে leak
    }
}
```

**Why it matters:** Compose-এ সবচেয়ে সাধারণ bug — 'recomposition-এ বারবার API call' — এখান থেকেই আসে।

**Common mistake:** `LaunchedEffect(Unit)` দিয়ে সব কাজ করা, যখন key বদলালে আবার চালানো দরকার; অথবা composable body-তে সরাসরি `vm.load()` ডাকা।

---

**Q:** Compose ও Flutter-এর rendering pipeline তুলনা করুন। একটি Flutter অ্যাপে native Android View বা Compose কীভাবে বসান?

**A:** দুটোই তিন ধাপ মানে:

```
Compose:  Composition  ->  Layout  ->  Drawing
          (কী দেখাবে)     (কোথায়)      (আঁকা)

Flutter:  Build  ->  Layout  ->  Paint  ->  Composite/Raster
          (widget)   (RenderObject size/position)   (GPU)
```

পার্থক্য: Compose Android-এর নিজস্ব graphics stack-এর ওপর আঁকে, তাই native View-এর সাথে একই window-এ মিশে যায়। Flutter নিজের engine দিয়ে পুরো স্ক্রিন একটি canvas-এ আঁকে — Android-এর নিজের View নয়, নিজের pixel।

তাই Flutter-এ native Android View (Google Maps, WebView, ইত্যাদি) বসাতে **Platform View** লাগে (`AndroidView` / `PlatformViewLink`)। এতে বাড়তি খরচ আছে, তাই অপ্রয়োজনে ব্যবহার এড়ান। বিস্তারিত সেকশন ১৩-তে।

**Example:**

```dart
// Flutter-এ native view বসানো
AndroidView(
  viewType: 'native-chart',
  creationParams: {'title': 'Sales'},
  creationParamsCodec: const StandardMessageCodec(),
)
```

**Why it matters:** 'Flutter কেন native view সরাসরি দেখাতে পারে না' — এই প্রশ্ন Flutter ও Android একসাথে বোঝার পরীক্ষা।

**Common mistake:** Flutter widget আর Android View একই tree-র অংশ ভাবা। না, Flutter পুরো screen-এ নিজের আলাদা surface-এ আঁকে।

---

**Q:** Edge-to-edge, window insets আর Dark mode/Theme আধুনিক Android-এ কীভাবে সামলাবেন?

**A:** Android 15 (API 35) target করলে app ডিফল্টভাবে **edge-to-edge** (status/navigation bar-এর পেছন পর্যন্ত) আঁকে। Android 16 (API 36) target করলে opt-out করার অপশন (`windowOptOutEdgeToEdgeEnforcement`) আর কাজ করে না ([Android 16 behavior changes](https://developer.android.com/about/versions/16/behavior-changes-16))। Play Store-এ এখন target 36 লাগে, তাই কনটেন্ট যেন status bar বা gesture bar-এর নিচে ঢাকা না পড়ে সেটা **insets** দিয়ে ঠিক করতে হয়।

বড় স্ক্রিনেও (smallest width ≥ ৬০০dp) target 36 হলে orientation/resizability বাধা উপেক্ষিত হয়, তাই layout adaptive রাখতে হয়।

Dark mode: Material 3 theme-এ `ColorScheme` আলাদা (light/dark), `isSystemInDarkTheme()` দিয়ে বাছাই।

**Example:**

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()                      // androidx.activity
        super.onCreate(savedInstanceState)
        setContent {
            Scaffold { padding ->               // padding-এ insets আছে
                Content(Modifier.padding(padding))
            }
        }
    }
}
```

```dart
// Flutter
SystemChrome.setEnabledSystemUIMode(SystemUiMode.edgeToEdge);
// UI-তে: SafeArea(child: ...) বা MediaQuery.paddingOf(context)
```

**Why it matters:** target 36 মানে এখন এটা বাধ্যতামূলক — আপডেটের পর UI কেটে গেলে প্রোডাকশন bug।

**Common mistake:** শুধু কয়েকটি ফোনে টেস্ট করা। gesture navigation, 3-button navigation, বড় স্ক্রিন সব যাচাই করুন।

---

## ৭. Jetpack Architecture: ViewModel, Room, DataStore, Hilt, Retrofit, Paging

---

**Q:** Android-এ MVVM ও Unidirectional Data Flow (UDF) কী? ViewModel কী কাজ করে?

**A:** সহজভাবে বললে: UI শুধু **দেখায়**, সিদ্ধান্ত আর data সামলায় **ViewModel**। UI ঘটনা (click) ViewModel-এ পাঠায়, ViewModel state বদলায়, UI সেই state দেখে আঁকে। তথ্য একমুখী — এই হলো **UDF**।

```
   Events (click)                 State (UiState)
 UI  -------------->  ViewModel  ------------------> UI
 (Compose/View)        |   ^                          (আঁকে)
                       v   |
                    Repository  (data আনে/সংরক্ষণ করে)
```

ViewModel configuration change (rotation)-এ বেঁচে থাকে, কিন্তু process death-এ নয় (সেকশন ৩)। ViewModel-এ Context/View/Activity রাখবেন না (leak)।

Flutter-এ তুলনা: ViewModel ≈ BLoC/Cubit/Riverpod Notifier; `UiState` ≈ BLoC state; UDF একই ধারণা।

**Example:**

```kotlin
data class CounterUiState(val count: Int = 0, val loading: Boolean = false)

@HiltViewModel
class CounterViewModel @Inject constructor(private val repo: CounterRepo) : ViewModel() {
    private val _state = MutableStateFlow(CounterUiState())
    val state: StateFlow<CounterUiState> = _state.asStateFlow()   // বাইরে শুধু read-only

    fun increment() = _state.update { it.copy(count = it.count + 1) }
}
```

**Why it matters:** Architecture-এর প্রশ্নে UI-state modeling, testability ও leak এড়ানোর দক্ষতা দেখা হয়।

**Common mistake:** `MutableStateFlow` সরাসরি public করা (UI থেকে state বদলানো যায়), আর ViewModel-এ `Context` রাখা।

---

**Q:** Repository pattern, Single Source of Truth আর Clean Architecture কী? Domain layer কখন লাগে?

**A:** **Repository** হলো data-র একটি দরজা — UI জানে না data network থেকে এল নাকি database থেকে। **Single Source of Truth (SSOT)**: UI সবসময় **local DB** থেকে ডেটা দেখে; network ডেটা আগে DB-তে লেখে, তারপর UI নিজে আপডেট পায়। এতে offline কাজ করে এবং ডেটা বিরোধ হয় না।

**Clean Architecture** তিন স্তর: Presentation (UI + ViewModel) → Domain (business rule, use case) → Data (repo impl, API, DB)। Dependency সর্বদা ভিতরের দিকে (domain data-কে চিনে না)। Google-এর পরামর্শ: **Domain layer ঐচ্ছিক** — যখন একই লজিক একাধিক ViewModel-এ বা জটিল business rule আছে, তখন use case বানান। ছোট app-এ জোর করে domain বানালে শুধু ফাইল বাড়ে।

Flutter-এর `presentation / domain / data` ফোল্ডার ভাগ ঠিক একই আইডিয়া।

**Example:**

```kotlin
class ArticleRepository(
    private val dao: ArticleDao,
    private val api: ArticleApi
) {
    // UI শুধু DB থেকে পড়ে (SSOT)
    val articles: Flow<List<Article>> =
        dao.observeAll().map { list -> list.map { it.toDomain() } }

    suspend fun refresh() {
        val remote = api.fetchArticles()
        dao.upsertAll(remote.map { it.toEntity() })   // DB বদলালে Flow আপনি আপডেট হয়
    }
}
```

**Why it matters:** Offline-first ও স্থির data flow — বড় app-এর একটি মূল চাহিদা।

**Common mistake:** Entity (DB model), DTO (API model) ও Domain model একই class ধরে রাখা — API বদলালে UI ভাঙে। আলাদা করুন।

---

**Q:** Room কী? Entity/DAO/Database, migration ও Flow কীভাবে কাজ করে?

**A:** Room হলো SQLite-এর ওপর type-safe লেয়ার। compile-time-এ SQL যাচাই করে, ভুল query হলে build ব্যর্থ হয়।

- **Entity** — টেবিল। **DAO** — query-র interface। **Database** — সব একত্র করা ক্লাস।
- DAO method `Flow` ফেরত দিলে টেবিল বদলালেই নতুন মান আসে (observable)।
- **Migration**: schema বদলালে version বাড়ান ও `Migration(1,2)` বা auto-migration দিন; না হলে পুরোনো ব্যবহারকারীর ডেটা হারাবে বা crash হবে। `exportSchema = true` রাখুন যাতে schema history git-এ থাকে।
- একাধিক অপারেশন একসাথে সফল বা ব্যর্থ করতে `@Transaction`।
- Query main thread-এ চলে না (suspend/Flow দিলে Room নিজে background-এ চালায়)।

Flutter-এ সমতুল্য: `drift` (type-safe SQLite) বা `sqflite`।

**Example:**

```kotlin
@Entity(tableName = "articles")
data class ArticleEntity(@PrimaryKey val id: Long, val title: String, val updatedAt: Long)

@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY updatedAt DESC")
    fun observeAll(): Flow<List<ArticleEntity>>

    @Upsert
    suspend fun upsertAll(items: List<ArticleEntity>)
}

@Database(entities = [ArticleEntity::class], version = 2, exportSchema = true,
          autoMigrations = [AutoMigration(from = 1, to = 2)])
abstract class AppDb : RoomDatabase() { abstract fun articleDao(): ArticleDao }
```

**Why it matters:** Production-এ migration ভুল মানে হাজার ব্যবহারকারীর crash — তাই senior-দের কাছে এটি গুরুত্বপূর্ণ প্রশ্ন।

**Common mistake:** `fallbackToDestructiveMigration()` production-এ ব্যবহার করা — এটি সব user data মুছে দেয়।

---

**Q:** SharedPreferences-এর বদলে DataStore কেন? Flutter-এর `shared_preferences`-এর সাথে সম্পর্ক কী?

**A:** SharedPreferences-এর সমস্যা: পড়ার সময় main thread block করতে পারে, error জানায় না, transactional নয়। **DataStore** coroutine ও Flow দিয়ে asynchronous, transactional ও error-aware। দুই রকম: **Preferences DataStore** (key-value) ও **Proto DataStore** (typed object)। ছোট setting/flag-এর জন্য উপযুক্ত; বড় বা relational data-এ Room।

Flutter-এ `shared_preferences` Android-এ ভিতরে native storage-এর ওপর বসে। সাবধান: **সেন্সিটিভ ডেটা (token, password) plain preference-এ রাখবেন না**।

**Example:**

```kotlin
val Context.dataStore by preferencesDataStore(name = "settings")
private val DARK = booleanPreferencesKey("dark_mode")

val darkMode: Flow<Boolean> = context.dataStore.data.map { it[DARK] ?: false }

suspend fun setDark(v: Boolean) = context.dataStore.edit { it[DARK] = v }
```

**Why it matters:** Interviewer দেখে আপনি পুরোনো API-র সমস্যা জানেন কিনা আর সঠিক জিনিস বেছে নিতে পারেন কিনা।

**Common mistake:** Token SharedPreferences/DataStore-এ plain text রাখা। Keystore-বন্ধ key দিয়ে encrypt করুন (সেকশন ৮)।

---

**Q:** Dependency Injection (Hilt) কী ও কেন? Flutter-এর `get_it`/Riverpod-এর সাথে পার্থক্য কী?

**A:** DI মানে: যে class-এর যে জিনিস লাগে সেটা সে নিজে বানাবে না, বাইরে থেকে দেওয়া হবে (বানিয়ে দেওয়া হবে)। উপমা: রান্নাঘরে রাঁধুনি নিজে বাজার করতে যায় না, উপর্ণ সরবরাহ পায়। ফলে test-এ fake দেওয়া সহজ, class নরমাল গিলে থাকে।

**Hilt** (Dagger-এর উপরে তৈরি) Android-এর স্ট্যান্ডার্ড DI। **compile-time**-এ graph যাচাই করে — কোন dependency হারিয়ে গেলে build-এই error। `get_it` হলো **service locator** (runtime-এ খোঁজে, ভুল হলে runtime error)। Riverpod নিজে DI + state দুটোই দেয়।

| Hilt ধারণা | কাজ |
| --- | --- |
| `@HiltAndroidApp` | Application-এ DI শুরু |
| `@Inject constructor` | class নিজে জানায় কিভাবে বানানো যাবে |
| `@Module` + `@Provides` | third-party class (Retrofit, Room) বানানোর নিয়ম |
| `@Binds` | interface → implementation |
| `@Singleton`, `@ViewModelScoped` | কতক্ষণ বেঁচে থাকবে (scope) |

**Example:**

```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class RepoModule {
    @Binds abstract fun bindRepo(impl: ArticleRepositoryImpl): ArticleRepository
}

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides @Singleton
    fun retrofit(client: OkHttpClient): Retrofit = Retrofit.Builder()
        .baseUrl("https://api.example.com/").client(client).build()
}
```

**Why it matters:** Large-scale app-এ DI ছাড়া test ও module ভাগ করা কঠিন। Hilt vs Koin (runtime) vs manual DI — তুলনামূলক প্রশ্ন আসে।

**Common mistake:** সবকিছু `@Singleton` করে দেওয়া — মেমরি আটকে থাকে। প্রয়োজন অনুযায়ী সহজ scope সর্বনিম্ন রাখুন।

---

**Q:** Retrofit ও OkHttp কীভাবে কাজ করে? Token refresh, interceptor ও certificate pinning কীভাবে?

**A:** **OkHttp** হলো HTTP client (connection pool, cache, interceptor); **Retrofit** সেটির ওপর interface-ভিত্তিক সহজ API। Flutter-এর `dio` + interceptor-এর আধুনিক Android সমতুল্য।

- **Interceptor** — প্রতি request/response-এ কিছু যোগ করতে (header, logging)।
- **Authenticator** — 401 এলে স্বয়ংক্রিয়ভাবে token refresh করে request আবার পাঠায়। একাধিক request একসাথে 401 পেলে দুইবার refresh না করতে **synchronized/mutex** দিতে হয়।
- **Certificate pinning** — নির্দিষ্ট server certificate/public key ছাড়া অন্য কিছু মানবে না (MITM থেকে রক্ষা)। pin মেয়াদ শেষ হলে app কাজ না করার রিস্ক আছে, তাই backup pin রাখুন।

**Example:**

```kotlin
class TokenAuthenticator(private val auth: AuthRepo) : Authenticator {
    override fun authenticate(route: Route?, response: Response): Request? {
        synchronized(this) {
            val newToken = runBlocking { auth.refreshToken() } ?: return null   // refresh ব্যর্থ -> logout
            return response.request.newBuilder()
                .header("Authorization", "Bearer $newToken").build()
        }
    }
}

val client = OkHttpClient.Builder()
    .addInterceptor(AuthHeaderInterceptor())
    .authenticator(TokenAuthenticator(authRepo))
    .connectTimeout(15, TimeUnit.SECONDS)
    .build()

interface Api {
    @GET("articles") suspend fun articles(@Query("page") page: Int): List<ArticleDto>
}
```

**Why it matters:** Auth flow ও network security senior-এর কাজের অংশ; refresh race condition একটি ক্লাসিক প্রশ্ন।

**Common mistake:** প্রতি 401-এ আলাদা করে refresh করা (দুইবার refresh → পুরোনো refresh token বাতিল), আর pin করার সময় backup pin না রাখা।

---

**Q:** Paging 3 কী? অনেক data-র list কীভাবে কাজ করবে?

**A:** ১০ হাজার item একসাথে না আনে, পাতা পাতা করে আনার উপায় হলো Paging। Paging 3-এ: `PagingSource` (কোথা থেকে পাতা আনবে), `Pager` (কত আগে আনবে), `RemoteMediator` (network → DB ভরা, offline + SSOT)। UI-এ `collectAsLazyPagingItems()` (Compose) বা `PagingDataAdapter` (RecyclerView)। Flutter-এ সমতুল্য: `infinite_scroll_pagination` বা নিজের scroll listener।

**Example:**

```kotlin
val articles: Flow<PagingData<Article>> = Pager(
    config = PagingConfig(pageSize = 20),
    pagingSourceFactory = { dao.pagingSource() }      // Room থেকে PagingSource
).flow.cachedIn(viewModelScope)

// Compose
val items = vm.articles.collectAsLazyPagingItems()
LazyColumn { items(items.itemCount) { i -> items[i]?.let { ArticleRow(it) } } }
```

**Why it matters:** Feed/chat/search — প্রায় সব বড় app-এ প্রযোজ্য; system design round-ও এর উত্তর লাগে।

**Common mistake:** `cachedIn(viewModelScope)` না দেওয়া (rotation-এ সব আবার load) ও page-number-ভিত্তিক pagination-এ insert/delete-এ item দুবার বা বাদ পড়া (cursor ব্যবহার করুন)।

---

## ৮. Background Work, Notification, Permission, Storage ও Security

---

**Q:** Android app ব্যাকগ্রাউন্ডে গেলে কেন বন্ধ হয়ে যায়? Doze ও App Standby কী?

**A:** Android-এর লক্ষ্য battery বাঁচানো। তাই user যখন app সরায়, system ক্রমাগত কড়াকড়ি করে:

- **Doze**: ফোন স্থির ও স্ক্রিন বন্ধ থাকলে network, job, alarm সব কিছু বন্ধ রেখে শুধু মাঝে মাঝে 'মেন্টেনেন্স উইন্ডো'-তে চালানোর সুযোগ দেয়।
- **App Standby / Standby Buckets**: যে app user অনেকদিন খুলেনি, তার background কাজ কম সময় পায়।
- **Background execution limits**: ব্যাকগ্রাউন্ডে থাকার সময় সাধারণ service শুরু করা যায় না (Android 8+)।
- **OEM battery optimization** (Xiaomi, Oppo, Samsung ইত্যাদি): স্ট্যান্ডার্ড Android-এরও বেশি কড়া, app kill করে দেয়। Flutter ডেভেলপারদের 'আমার ফোনে তো চলে, গ্রাহকের ফোনে চলে না' সমস্যার বড় কারণ।

উপমা: রাতে বাসায় সব বাতি নিভিয়ে দেওয়া — শুধু যে কাজে জরুরি দরকার তার জন্য অনুমতি লাগে।

**Example:**

```kotlin
// Battery optimization থেকে বাদ চাইলে (শুধু যুক্তিসংগত use case-এ)
val pm = getSystemService(PowerManager::class.java)
val ignoring = pm.isIgnoringBatteryOptimizations(packageName)
if (!ignoring) startActivity(Intent(Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS))
```

**Why it matters:** 'Background-এ notification/sync কাজ করছে না' — production-এর সবচেয়ে ক্লাসিক সমস্যা।

**Common mistake:** বলা যে 'Timer.periodic দিয়ে background-এ কাজ চালাব' — app ব্যাকগ্রাউন্ডে গেলে থেমে যাবে।

---

**Q:** Background কাজের জন্য WorkManager, Foreground Service, AlarmManager কখন কোনটি?

**A:**

| কাজের ধরন | ব্যবহার করুন |
| --- | --- |
| পরে করলেও চলে, কিন্তু **নিশ্চিত হতে হবে** (sync, upload retry, log পাঠানো) | **WorkManager** |
| user দেখছে এবং লম্বা সময় ধরে চলে (গান, navigation, বড় upload, call) | **Foreground Service** (notification সহ) |
| ঠিক সময়ে জাগাতে হবে (alarm clock, calendar reminder) | **AlarmManager** (exact alarm অনুমতি/নিয়ম মানতে হয়) |
| app খোলা অবস্থায় ছোট কাজ | Coroutine (`viewModelScope`) |
| server থেকে ডেটা এসেছে জানাতে | **FCM** push |

**WorkManager** বৈশিষ্ট্য: constraint (network/charging), retry with backoff, chaining, unique work, periodic (সর্বনিম্ন ১৫ মিনিট পরপর), app restart/reboot-এও টিকে থাকে (নিজস্ব DB-তে job রাখে)। সময় সম্পূর্ণ ঠিক নয়; system আদর্শ সময়ে চালায়।

Flutter-এ `workmanager` plugin এই WorkManager-ই ব্যবহার করে; background callback-এ Dart কোড আলাদা একটি headless Flutter engine/isolate-এ চলে — তাই সেখানে UI-এর state বা Riverpod-এর in-memory object পাওয়া যাবে না; DI/DB আবার init করতে হয়।

**Example:**

```kotlin
class UploadWorker(ctx: Context, p: WorkerParameters) : CoroutineWorker(ctx, p) {
    override suspend fun doWork(): Result = try {
        repo.uploadPending()
        Result.success()
    } catch (e: IOException) {
        if (runAttemptCount < 3) Result.retry() else Result.failure()
    }
}

val req = OneTimeWorkRequestBuilder<UploadWorker>()
    .setConstraints(Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED).build())
    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
    .build()
WorkManager.getInstance(ctx).enqueueUniqueWork("upload", ExistingWorkPolicy.KEEP, req)
```

```dart
@pragma('vm:entry-point')
void callbackDispatcher() {
  Workmanager().executeTask((task, input) async {
    await initDependencies();      // UI-এর state এখানে নেই, নতুন করে init
    return true;
  });
}
```

**Why it matters:** Senior-রা সঠিক tool বেছে নেন; 'সবকিছুতে Service' বললে পুরোনো Android-এর চিন্তা বোঝা যায়।

**Common mistake:** WorkManager-কে 'ঠিক ১০:০০-টায় চালাবে' ভাবা। নিখুঁত সময় লাগলে exact alarm / FCM।

---

**Q:** Foreground Service-এর নিয়ম Android 14/15-এ কী বদলেছে?

**A:** প্রতিটি foreground service-এর দরকার এখন স্পষ্ট কারণ বলা:

- Android 14 (API 34) target: manifest-এ **foreground service type** (যেমন `location`, `mediaPlayback`, `dataSync`) এবং সংশ্লিষ্ট permission (`FOREGROUND_SERVICE_LOCATION` ইত্যাদি) লাগে। Type না দিলে crash।
- Android 15 (API 35) target: `dataSync` ও `mediaProcessing` type-এর একটি **timeout** আছে (২৪ ঘন্টায় ৬ ঘন্টা); সময় শেষ হলে system `onTimeout()` ডাকে। দীর্ঘ upload/download-এর জন্য WorkManager-এর long-running worker বা user-initiated data transfer job বিবেচনা করুন।
- ব্যাকগ্রাউন্ড থেকে foreground service শুরু করা সীমিত (কিছু ব্যতিক্রম আছে, যেমন user ক্লিক করা notification, high-priority FCM)।

(Android 15 timeout-এর সর্বশেষ বিস্তারিত developer.android.com-এর foreground service docs থেকে ইন্টারভিউর আগে সম্পাদন করে নিন।)

**Example:**

```xml
<uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_LOCATION"/>

<service android:name=".TrackingService"
    android:foregroundServiceType="location" android:exported="false"/>
```

```kotlin
ServiceCompat.startForeground(
    this, NOTIF_ID, notification,
    ServiceInfo.FOREGROUND_SERVICE_TYPE_LOCATION
)
```

**Why it matters:** Location tracking, music, ride-hailing ধরনের Flutter app-এ Play Console এবং runtime crash এই নিয়মের কারণে হয়।

**Common mistake:** type ঘোষণা না করা, অথবা সব কাজকে `dataSync` ধরে নেওয়া। নিজের use case-এর সহি ধরন বেছে নিন।

---

**Q:** Push notification (FCM) কীভাবে কাজ করে? App kill হলে কী হয়? Flutter-এ কী করতে হয়?

**A:** FCM-এ দুই ধরনের message:

- **Notification message** — app background/killed হলে system নিজেই notification দেখায় (আপনার কোড চলে না)। App foreground-এ থাকলে আপনার handler পায়।
- **Data message** — সবসময় আপনার handler-এ যায় (স্থানীয়ভাবে notification বানাতে পারেন)। কিন্তু user নিজে 'Force stop' করলে সব FCM বন্ধ — পরে user আবার app খোলা পর্যন্ত।

Android 13+ এ notification দেখাতে `POST_NOTIFICATIONS` runtime permission লাগে; Android 8+ এ **notification channel** না থাকলে notification আসে না। Priority ও sound channel-এর ওপর নির্ভর করে, পরে user বদলাতে পারে।

Flutter (`firebase_messaging`): background/terminated handler **top-level function** হতে হয়, `@pragma('vm:entry-point')` লাগে, আর এটি আলাদা isolate-এ চলে (UI state পাবেন না)।

**Example:**

```dart
@pragma('vm:entry-point')
Future<void> _bgHandler(RemoteMessage m) async {
  await Firebase.initializeApp();      // আলাদা isolate, আবার init
  // local notification দেখান বা DB-তে সংরক্ষণ করুন
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  FirebaseMessaging.onBackgroundMessage(_bgHandler);
  runApp(const App());
}

// notification tap-এ app খুললে
final initial = await FirebaseMessaging.instance.getInitialMessage();      // terminated থেকে
FirebaseMessaging.onMessageOpenedApp.listen((m) => router.go(m.data['route'])); // background থেকে
```

**Why it matters:** Notification সব অ্যাপের সবচেয়ে বেশি বলা সমস্যা। 'terminated অবস্থায় কেন দেখায় না' উত্তর এই জ্ঞানে থাকে।

**Common mistake:** আশা করা যে notification-only message-এ custom handler চলবে, অথবা Android 13+ এ permission চাওয়াই ভুলে যাওয়া।

---

**Q:** Runtime permission কীভাবে কাজ করে? 'Don't ask again' ও Android 13/14-এর মিডিয়া permission কীভাবে সামলাবেন?

**A:** Dangerous permission (camera, location, contacts ইত্যাদি) manifest-এ ঘোষণা করার পরেও runtime-এ user-কে জিজ্ঞেস করতে হয়। সহজ নিয়ম:

1. যখন লাগবে তখনই চাইবেন (নির্দিষ্ট feature শুরু হওয়ার সময়), app খোলার সময় নয়।
2. কেন লাগে সেটা আগে বুঝিয়ে দিন (rationale)।
3. স্থায়ীভাবে দাবি বাতিল হলে (পরপর দুইবার deny) system dialog আর দেখায় না — user-কে Settings-এ পাঠাতে হয়।

বিশেষ: location-এ 'approximate' ও 'precise' আলাদা; 'only this time' (one-time) permission আছে; Android 13-এ `READ_EXTERNAL_STORAGE`-এর বদলে আলাদা `READ_MEDIA_IMAGES/VIDEO/AUDIO`; Android 14-এ user শুধু কিছু ছবি দিতে পারে (partial access, `READ_MEDIA_VISUAL_USER_SELECTED`)। সবচেয়ে সহজ উপায়: ছবি বাছাইয়ে **Photo Picker** ব্যবহার — কোন permission-ই লাগে না।

**Example:**

```dart
Future<void> openCamera() async {
  var status = await Permission.camera.status;
  if (status.isDenied) status = await Permission.camera.request();

  if (status.isGranted) {
    startCamera();
  } else if (status.isPermanentlyDenied) {
    showDialog(/* কেন লাগে বুঝিয়ে */);
    await openAppSettings();           // user-কে Settings-এ পাঠান
  }
}
```

**Why it matters:** Permission flow UX ও Play policy (অপ্রয়োজনীয় permission চাইলে review reject) — দুটিতেই প্রভাব ফেলে।

**Common mistake:** প্রথম launch-এ সব permission একসাথে চাওয়া, আর `permanentlyDenied` অবস্থা হ্যান্ডেল না করা।

---

**Q:** Android storage কীভাবে কাজ করে? Scoped Storage কী? Flutter-এর `path_provider`-এর সাথে মিলান।

**A:** সহজ ছবি: প্রতিটি app-এর নিজস্ব **private ঘর** আছে (কোন permission লাগে না), আর বাকি shared storage-এ (Downloads, Photos) যেতে হলে নিয়ম মানতে হয়।

- **Internal storage** (`filesDir`, `cacheDir`) — শুধু আপনার app পায়, uninstall-এ মুছে যায়।
- **App-specific external** — SD/shared জায়গায়, তবে app-এর নিজস্ব ফোল্ডার, permission লাগে না।
- **Scoped Storage** (Android 10 থেকে, Android 11-এ বাধ্যতামূলক): shared storage-এ সরাসরি পাথ দিয়ে সব ফাইল পড়া যায় না; **MediaStore** (ছবি/ভিডিও/অডিও), **Storage Access Framework (SAF)** (user ফাইল/ফোল্ডার বাছে) ব্যবহার করতে হয়।

| Flutter `path_provider` | Android সমতুল্য |
| --- | --- |
| `getApplicationDocumentsDirectory()` | app-এর internal files |
| `getTemporaryDirectory()` | `cacheDir` (system মুছতে পারে) |
| `getExternalStorageDirectory()` | app-specific external dir |

**Example:**

```kotlin
// ছবি Gallery-তে সংরক্ষণ (MediaStore) — Android 10+ এ permission লাগে না
val values = ContentValues().apply {
    put(MediaStore.Images.Media.DISPLAY_NAME, "photo.jpg")
    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
    put(MediaStore.Images.Media.RELATIVE_PATH, "Pictures/MyApp")
}
val uri = contentResolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)!!
contentResolver.openOutputStream(uri)?.use { bitmap.compress(Bitmap.CompressFormat.JPEG, 90, it) }
```

**Why it matters:** 'Storage permission চাইছে কিন্তু কাজ করছে না' — Android 10+ এর ক্লাসিক সমস্যা।

**Common mistake:** `MANAGE_EXTERNAL_STORAGE` (সব ফাইল) চাওয়া — Play নীতিতে কড়া সীমা, সাধারণ app-এ reject হয়।

---

**Q:** Android-এ sensitive data (token, key) কীভাবে নিরাপদে রাখবেন? Keystore, biometric, network security কী?

**A:** **Android Keystore** হলো একটি নিরাপদ সিন্দুক যেখানে encryption key তৈরি হয় ও থাকে; key-টি **বাইরে বের করা যায় না** (hardware-backed হতে পারে)। আপনি data encrypt করে নিজের জায়গায় রাখেন, key Keystore-এ।

সাম্প্রতিক খবর: Jetpack Security-র `EncryptedSharedPreferences` / `MasterKey` / `EncryptedFile` (`androidx.security:security-crypto`) **deprecated** ([Android API reference](https://developer.android.com/reference/kotlin/androidx/security/crypto/EncryptedSharedPreferences))। নতুন কোডে Keystore key + Tink (বা সরাসরি `javax.crypto`) দিয়ে encrypt করে DataStore/ফাইলে রাখাই এখনকার পথ। Flutter-এ token রাখতে `flutter_secure_storage`-এর বর্তমান version কী ব্যবহার করছে তা সর্বশেষ README দেখে নিন।

আরও:

- **BiometricPrompt** (Flutter: `local_auth`) — fingerprint/face। Keystore key-কে biometric-বন্ধ করা যায়।
- **Network Security Config** — cleartext (http) বন্ধ, pinning, কোন CA মানবে।
- **Play Integrity API** — ডিভাইস/app tamper যাচাই (server-side verify করতে হয়)।
- `FLAG_SECURE` — screenshot/screen recording বন্ধ (banking)।
- Exported component সীমাবদ্ধ রাখা, WebView সাবধানে ব্যবহার।

**Example:**

```kotlin
val keyGen = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore")
keyGen.init(
    KeyGenParameterSpec.Builder("token_key", KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
        .setKeySize(256)
        .build()
)
val key = keyGen.generateKey()      // key Keystore-এ; বাইরে নেওয়া যাবে না
```

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
  <base-config cleartextTrafficPermitted="false"/>
</network-security-config>
```

**Why it matters:** Fintech/health app-এ security round আলাদা করে হয়; OWASP MASVS কাঠামোকে ভিত্তি করে প্রশ্ন আসে।

**Common mistake:** API key/secret Dart কোডে লুকিয়ে রাখা (APK decompile করলে পাওয়া যায়) — গোপন জিনিস server-এ রাখুন।

---

## ৯. Android Performance ও Debugging: ANR, Memory Leak, Startup, App Size

---

**Q:** ANR কী? কেন হয়, কীভাবে ধরবেন ও সারাবেন?

**A:** **ANR (Application Not Responding)** মানে main thread অনেকক্ষণ আটকে আছে, system user-কে 'অ্যাপ সাড়া দিচ্ছে না' বলে দেখায়। সময়সীমা মোটামুটি:

- Input event (touch/key) → প্রায় **৫ সেকেন্ড**ে উত্তর না পেলে।
- BroadcastReceiver `onReceive` → foreground-এ প্রায় ১০ সেকেন্ড, background-এ আরও বেশি।
- Service শুরুর callback → foreground-এ প্রায় ২০ সেকেন্ড।

(সর্বশেষ সংখ্যা Android docs-এ দেখে নিন; সাধারণ ধারণাটাই গুরুত্বপূর্ণ।)

**কারণ**: main thread-এ network/disk/DB কাজ, বড় JSON parse, lock পাওয়ার অপেক্ষা (deadlock), `SharedPreferences.commit()`, ভারী `Application.onCreate`। Flutter-এ Android 3.29+ এ Dart কোডও main thread-এ চলে, তাই ভারী Dart কাজ isolate-এ না সরালে ANR হতে পারে।

**কীভাবে ধরবেন**: Play Console-এর *Android vitals* (প্রোডাকশন ANR ও stack trace), লোকালে **StrictMode**, Perfetto/Profiler, Crashlytics ANR report।

**Example:**

```kotlin
// Debug build-এ main thread-এ disk/network হলে লগে ধরিয়ে দেয়
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder().detectDiskReads().detectDiskWrites().detectNetwork().penaltyLog().build()
    )
}
```

**Why it matters:** ANR rate Play Store ranking-এ প্রভাব ফেলে; নির্দিষ্ট threshold ছাড়ালে visibility কমে। Senior-দের কাছে প্রত্যাশা: ধরা → কারণ বের → সারানো।

**Common mistake:** ANR-কে 'সাধারণ crash' ভাবা। আলাদা সমস্যা, তার আলাদা টেস্ট ও trace লাগে।

---

**Q:** Memory leak কী? Android-এ সবচেয়ে সাধারণ leak কোথায় হয়, কীভাবে ধরবেন?

**A:** Leak মানে যে object আর দরকার নেই, কিন্তু কেউ তাকে ধরে রেখেছে তাই GC মুছতে পারছে না। উপমা: হোটেলের ক্যানসেল হওয়া ঘর যেন ডিউটি শেষেও তালা দিয়ে রাখা। Android-এ সবচেয়ে বড় কারণ: **Activity/Fragment/View** রেফারেন্স দীর্ঘজীবী কিছুর ভেতরে থাকা।

সাধারণ উৎস:

1. Singleton/static field-এ Activity বা Context রাখা।
2. Listener/callback register করে unregister না করা।
3. Fragment-এ `binding` null না করা (`onDestroyView`)।
4. Inner class / anonymous Handler যা কোনো দীর্ঘ সময়ের message ধরে রাখে।
5. ভুল scope-এ coroutine (`GlobalScope`)।

**ধরার উপায়**: **LeakCanary** (debug build-এ স্বয়ংক্রিয়, leak trace দেখায়), Android Studio **Memory Profiler** (heap dump)। Flutter-এ DevTools Memory tab; Dart-এ সাধারণ leak: `StreamSubscription` cancel না করা, `AnimationController`/`TextEditingController` `dispose` না করা, বড় cache।

**Example:**

```kotlin
// ভুল: singleton Activity ধরে রাখে → Activity leak
object Analytics { lateinit var ctx: Context }       // Analytics.ctx = this (Activity)

// ঠিক: Application context
object Analytics { lateinit var ctx: Context }       // Analytics.ctx = applicationContext

// ভুল: unregister নেই
sensorManager.registerListener(listener, sensor, SensorManager.SENSOR_DELAY_UI)
// ঠিক: onStop-এ
override fun onStop() { super.onStop(); sensorManager.unregisterListener(listener) }
```

**Why it matters:** Leak → OutOfMemoryError → crash। অনেক কোম্পানি LeakCanary চালু রাখে।

**Common mistake:** শুধু `System.gc()` ডাকাকে সমাধান ভাবা। আসল সমস্যার রেফারেন্স ছিন্ন করতে হয়।

---

**Q:** App startup (cold/warm/hot) কী? কীভাবে দ্রুত করবেন? Baseline Profile কী?

**A:**

- **Cold start** — process নেই, সব নতুন (সবচেয়ে ধীর)।
- **Warm start** — process আছে, Activity নতুন।
- **Hot start** — Activity মেমরিতে, শুধু সামনে আনা।

মাপতে: **TTID** (Time To Initial Display — প্রথম frame) ও **TTFD** (Time To Full Display — `reportFullyDrawn()`)।

দ্রুত করার উপায়:

1. `Application.onCreate` ও ContentProvider-এর ভারী init সরান / lazy করুন (App Startup library)।
2. **Splash Screen API** ব্যবহার করুন — কোন ভারী সমবয়সীমা রাখবেন না।
3. **Baseline Profile** — আপনি নির্দিষ্ট করে দেন কোন কোড startup/scroll-এ গুরুত্বপূর্ণ; ইনস্টলের সময়ই সেই অংশ pre-compile হয়ে যায়। ফলে প্রথম বারেও দ্রুত চলে (Google স্বরূপ উল্লেখ করে অনেক শতাংশ উন্নতি)।
4. **Macrobenchmark** দিয়ে মাপুন, অনুমান নয়।

Flutter-এ: `main()`-এর আগে ভারী init সরান (কতকু লাগবে `runApp`-এর আগে তা সীমিত রাখুন), first frame দেখানোর পর background-এ বাকিটা করুন; বড় feature `deferred` import / Play Feature Delivery-তে। Add-to-app হলে `FlutterEngine` আগে থেকে warm-up করে cache করা যায় (সেকশন ১৩)।

**Example:**

```kotlin
// Macrobenchmark: cold startup মাপা
class StartupBenchmark {
    @get:Rule val rule = MacrobenchmarkRule()

    @Test fun coldStartup() = rule.measureRepeated(
        packageName = "com.example.app",
        metrics = listOf(StartupTimingMetric()),
        iterations = 5,
        startupMode = StartupMode.COLD,
        compilationMode = CompilationMode.None()
    ) { pressHome(); startActivityAndWait() }
}
```

```bash
# দ্রুত মাপা
adb shell am start -W -n com.example.app/.MainActivity     # TotalTime / WaitTime দেখায়
```

**Why it matters:** Startup ধীর হলে user uninstall করে; ইন্টারভিউয়ার দেখে আপনি মেপে দেখেন কিনা।

**Common mistake:** emulator-এ debug build দেখে startup মাপা। আসল ডিভাইসে, release/profile build-এ মাপুন।

---

**Q:** UI jank (frame drop) কীভাবে বুঝবেন ও কীভাবে ধরবেন? Flutter ও Android-এ?

**A:** ৬০ Hz স্ক্রিনে প্রতি frame-এ প্রায় **১৬ ms** সময়; ১২০ Hz-এ প্রায় ৮ ms। এর বেশি লাগলে frame ড্রপ ও কাঁপুনি (jank) হয়।

|  | Android native | Flutter |
| --- | --- | --- |
| মাপার টুল | Android Studio Profiler, **Perfetto**, JankStats, 'Profile GPU rendering' | **DevTools Performance**, `--profile` mode, frame chart (UI/Raster) |
| সাধারণ কারণ | main thread-এ ভারী কাজ, গভীর hierarchy, overdraw, অতিরিক্ত recomposition | অনাবশ্যক rebuild, `build()`-এ ভারী কাজ, `saveLayer`/`Opacity`, বড় image |
| সমাধান | background-এ সরান, flatten, `key` দিন | `const`, ছোট widget ভাগ, `RepaintBoundary`, `Isolate.run`, image `cacheWidth` |

Flutter-এ shader compilation jank আগে বড় সমস্যা ছিল। Impeller সেই shader আগে থেকেই compile করে রাখে, তাই এতে সমস্যা কমেছে। সাম্প্রতিক Flutter-এ Android 10+ ডিফল্টভাবে Impeller ([Shorebird-এর version তালিকা](https://docs.shorebird.dev/getting-started/flutter-version.md) ও Flutter release note দেখুন)।

**Example:**

```dart
// ভারী কাজ main isolate-এ নয়
final parsed = await Isolate.run(() => jsonDecode(hugeString));

// বড় image ছোট করে decode
Image.network(url, cacheWidth: 400);

// স্থির অংশ আলাদাভাবে আঁকিয়ে দেয়
RepaintBoundary(child: ComplexChart())
```

```bash
flutter run --profile      # jank মাপতে debug নয়, profile mode
```

**Why it matters:** 'মাপা → ধরা → সারানো → আবার মাপা' — এই পদ্ধতিই senior উত্তর।

**Common mistake:** debug mode-এ performance দেখা। Flutter debug mode স্বাভাবিকভাবে অনেক ধীর।

---

**Q:** App size কীভাবে কমাবেন?

**A:** প্রথমে মাপুন, কোথায় বেশি তা দেখুন। তারপর:

1. **AAB** ব্যবহার — Play প্রতি device-এর জন্য শুধু প্রয়োজনীয় ABI/ভাষা/density দেয়।
2. **R8 + resource shrinking** — অব্যবহৃত কোড/resource ফেলে দেয়।
3. ছবি WebP/সম্ভব হলে vector; বড় asset নেটওয়ার্ক থেকে লোড।
4. অপ্রয়োজনীয় package/SDK বাদ দিন (Flutter plugin native library সহ আসে)।
5. Flutter: `--analyze-size`, icon tree-shaking (ডিফল্ট), `--split-debug-info`, deferred components।

**Example:**

```bash
flutter build appbundle --release --analyze-size --target-platform android-arm64
# ফলাফল *-code-size-analysis_*.json -> DevTools App Size tool-এ খুলুন
```

**Why it matters:** ছোট size = আরও বেশি install, বিশেষ করে ডেটা সীমিত বাজারে (যেমন বাংলাদেশ)।

**Common mistake:** প্রথমে মাপা না করে অনুমানে অপটিমাইজ করা।

---

**Q:** ডিবাগিং টুলবক্স: Android ও Flutter-এ কোন কোন টুল জানা দরকার?

**A:** তালিকাটি মুখস্থ নয়, কোন সমস্যায় কোনটি — তা জানা জরুরি:

| সমস্যা | Android | Flutter |
| --- | --- | --- |
| Log / crash | Logcat, Crashlytics, Android vitals | `debugPrint`, Crashlytics, `FlutterError.onError` |
| UI hierarchy | Layout Inspector | Flutter Inspector (widget tree) |
| Network | Network Inspector, Charles/Proxyman | DevTools Network |
| DB | Database Inspector | Drift inspector / DevTools |
| Memory/CPU | Profiler, LeakCanary, Perfetto | DevTools Memory / CPU |
| Main-thread violation | StrictMode | — |

কাজের `adb` কমান্ড:

```bash
adb logcat -s MyTag                                  # শুধু একটি tag
adb shell dumpsys meminfo com.example.app             # memory অবস্থা
adb shell am force-stop com.example.app               # জোর করে বন্ধ
adb shell pm clear com.example.app                    # data মুছে দেওয়া
adb shell am kill com.example.app                     # process death সিমুলেট (backgroundে থাকলে)
adb bugreport                                         # পুরো সিস্টেম রিপোর্ট
```

**Example:** Flutter-এ দুই handler দরকার (framework error ও async error আলাদা ধরা পড়ে):

```dart
void main() {
  FlutterError.onError = (details) => FirebaseCrashlytics.instance.recordFlutterFatalError(details);
  PlatformDispatcher.instance.onError = (error, stack) {
    FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);
    return true;
  };
  runApp(const App());
}
```

**Why it matters:** Production issue-এ বলতে পারা যে 'কোন টুল দিয়ে কী দেখব' — এটা অভিজ্ঞতার প্রমাণ।

**Common mistake:** Flutter-এ শুধু `FlutterError.onError` সেট করা; async/platform error ধরতে `PlatformDispatcher.instance.onError`ও লাগে।

---

## ১০. Flutter Core Framework Deep Dive

---

**Q:** Flutter-এর architecture কেমন? Native বা React Native থেকে এটা মূলত কোথায় আলাদা?

**A:** Flutter তিনটি স্তরে গঠিত:

```
+--------------------------------------------------------+
| Framework (Dart)                                       |
|  Material / Cupertino                                  |
|  Widgets                                               |
|  Rendering (RenderObject, layout, paint)               |
|  Animation / Painting / Gestures / Foundation          |
+--------------------------------------------------------+
| Engine (C++)                                           |
|  Dart runtime, Impeller (বা Skia), text layout,        |
|  platform channel, accessibility                       |
+--------------------------------------------------------+
| Embedder (প্ল্যাটফর্ম-নির্দিষ্ট)                         |
|  Android: FlutterActivity/FlutterView + surface,       |
|  input, thread setup — প্ল্যাটফর্মের সাথে সেতু          |
+--------------------------------------------------------+
```

মূল পার্থক্য: **Flutter নিজের pixel নিজে আঁকে।** Android-এর `Button` বা `TextView` ব্যবহার করে না; একটি surface-এর ওপর engine সরাসরি আঁকে। React Native বিপরীতে প্ল্যাটফর্মের আসল native view ব্যবহার করে।

ফলাফল:

- দুই প্ল্যাটফর্মে UI প্রায় একরকম এবং আপনার নিয়ন্ত্রণে।
- কিন্তু প্ল্যাটফর্মের জিনিস (accessibility, text input, Google Maps-এর মতো native view, WebView) আলাদা integration লাগে — Platform View, platform channel (সেকশন ১৩)।

**Example:**

```kotlin
// Android-এ Flutter-এর প্রবেশদ্বার: একটি সাধারণ Activity
class MainActivity : FlutterActivity()
// ভেতরে FlutterEngine তৈরি হয়, Dart কোড চলে, UI আঁকা হয় FlutterView-তে
```

**Why it matters:** Architecture বুঝলে 'এই সমস্যা Dart-এর, engine-এর না platform-এর' — তা বলতে পারবেন। Senior মানেই লেয়ার ধরে debug করা।

**Common mistake:** 'Flutter native widget-কে wrap করে' বলা। ভুল — Flutter নিজে আঁকে। Platform View ব্যতিক্রম, নিয়ম নয়।

---

**Q:** Widget tree, Element tree ও RenderObject tree — তিনটি কী এবং আলাদা কেন?

**A:** তিনটি tree-র আলাদা কাজ:

```
Widget tree          Element tree                     RenderObject tree
(কনফিগারেশন)         (জীবন্ত instance)                 (layout + paint)
----------------     ------------------------------   ----------------------
Center          ---> SingleChildRenderObjectElement   --> RenderPositionedBox
  Padding       ---> SingleChildRenderObjectElement   --> RenderPadding
    Text        ---> StatelessElement (নিচে RichText  --> RenderParagraph)
```

(সরলীকৃত চিত্র)

- **Widget** — অপরিবর্তনীয় (immutable) বর্ণনা: 'এখানে এই config-এর একটি জিনিস চাই'। খুব সস্তা, প্রতি rebuild-এ নতুন তৈরি হয়।
- **Element** — widget-কে tree-র একটি নির্দিষ্ট জায়গায় বসানো instance। দীর্ঘস্থায়ী; `State` এখানে থাকে। প্রতিবার নতুন widget এলে element ঠিক করে: পুরোনো element আপডেট হবে, নাকি নতুন হবে।
- **RenderObject** — আসল layout, paint ও hit-test করে। তুলনামূলক ভারী, তাই যতটা সম্ভব পুনর্ব্যবহার হয়।

নিয়ম: নতুন widget আসলে `Widget.canUpdate(old, new)` দেখা হয় — **runtimeType ও key একই** হলে element রাখা হয়, শুধু আপডেট হয় (RenderObject-ও `updateRenderObject` দিয়ে আপডেট)। না হলে পুরোনো element ফেলে নতুন বানানো হয়।

মনে রাখবেন: শুধু `RenderObjectWidget` (যেমন `Padding`, `Align`) RenderObject তৈরি করে। `StatelessWidget`/`StatefulWidget` শুধু অন্য widget compose করে।

**Example:**

```dart
// প্রতি rebuild-এ Text নামের নতুন widget তৈরি হয়, কিন্তু Element ও RenderObject রয়ে যায়
Widget build(BuildContext context) => Text('Count: $count');

// runtimeType বদলালে element নতুন তৈরি হয় (state হারায়)
Widget build(BuildContext context) =>
    isLoading ? const CircularProgressIndicator() : ProfileView(user: user);
```

**Why it matters:** 'setState-এ পুরো UI ফেলে নতুন করে আঁকে?' — এই প্রশ্নের সঠিক উত্তর এখানে: widget সস্তা, element/render object পুনর্ব্যবহার হয়।

**Common mistake:** 'Widget মানেই স্ক্রিনে আঁকা জিনিস' বলা। Widget শুধু বর্ণনা; আঁকে RenderObject।

---

**Q:** Flutter layout কীভাবে কাজ করে? 'Constraints go down, sizes go up, parent sets position' বলতে কী বোঝায়?

**A:** Layout এক পাসে হয়:

```
Parent  ---- Constraints (minW,maxW,minH,maxH) ---->  Child
Parent  <--- Size (সীমার ভেতরে নিজের মাপ) ----------  Child
Parent  নিজে ঠিক করে child কোথায় বসবে (position)
```

1. **Constraints নিচে নামে** — parent child-কে বলে 'তুমি এই ন্যূনতম-সর্বোচ্চ সীমার মধ্যে থাকো'।
2. **Size ওপরে ওঠে** — child সীমার ভেতরে নিজের মাপ ঠিক করে parent-কে জানায়।
3. **Position parent ঠিক করে** — child নিজের জায়গা জানে না।

তাই child নিজে জোর করে নিজের মাপ ঠিক করতে পারে না — parent-এর constraint বাঁধা। *Tight* constraint (min = max) হলে child-এর কোনো স্বাধীনতা নেই। *Loose* constraint (min = 0) হলে child ছোট হতে পারে।

**সবচেয়ে সাধারণ ভুল**: 'Vertical viewport was given unbounded height' — `Column` তার child-কে অসীম উচ্চতা দেয়, ভেতরের `ListView` নিজের উচ্চতা জানতে চায় — পারে না।

**Example:**

```dart
// Root-এ screen-এর tight constraint, তাই width/height উপেক্ষিত — পুরো স্ক্রিন লাল
runApp(Container(width: 100, height: 100, color: const Color(0xFFFF0000)));

// Center constraint শিথিল (loose) করে দেয় — এবার ১০০x১০০
runApp(Center(child: Container(width: 100, height: 100, color: const Color(0xFFFF0000))));

// ভুল: Column-এর ভেতর ListView -> unbounded height error
Column(children: [ListView(children: items)]);

// ঠিক: বাকি জায়গা নিতে Expanded
Column(children: [Expanded(child: ListView(children: items))]);
```

**Why it matters:** অর্ধেক Flutter layout bug এখান থেকে আসে। Senior এই তিন লাইনের নিয়ম দিয়ে যেকোনো overflow বা unbounded error ব্যাখ্যা করতে পারে।

**Common mistake:** `Container(width: 200)` লিখলেই 200 হবে ধরে নেওয়া। Parent tight constraint দিলে আপনার মাপ উপেক্ষিত হয়।

---

**Q:** Flutter-এর একটি frame কীভাবে তৈরি হয়? Rendering pipeline ব্যাখ্যা করুন।

**A:** স্ক্রিন প্রতি vsync সংকেতে নতুন frame চায়। Engine তখন framework-কে frame তৈরি করতে বলে:

```
Vsync
  |
  v
[UI task runner — Dart]
  build   : dirty element-গুলো rebuild -> নতুন widget
  layout  : RenderObject-রা মাপ ঠিক করে
  paint   : drawing command -> Layer tree
  |
  v  (Layer tree পাঠানো হয়)
[Raster thread — engine]
  Layer tree -> Impeller/Skia -> GPU command
  |
  v
স্ক্রিন
```

- `setState`/`markNeedsBuild` শুধু element-কে **dirty** চিহ্নিত করে; আসল rebuild পরের frame-এ হয়।
- Dart-এর কাজ (build, layout, paint) UI task runner-এ; GPU-র জন্য কমান্ডে রূপান্তর raster thread-এ।
- Flutter 3.29+ থেকে Android ও iOS-এ Dart কোড প্ল্যাটফর্মের main thread-এই চলে (আলাদা UI thread নয়) — তাই ভারী Dart কাজ থাকলে ANR/jank দুটোই হতে পারে। বিস্তারিত Flutter 3.29 release note ও breaking-change doc-এ দেখুন।

তাই jank দুই ধরনের: **UI jank** (build/layout/paint ভারী) এবং **Raster jank** (জটিল effect, `saveLayer`, বড় image)।

**Example:**

```dart
// প্রথম frame শেষ হওয়ার পর size জানা
@override
void initState() {
  super.initState();
  WidgetsBinding.instance.addPostFrameCallback((_) {
    if (!mounted) return;
    final box = context.findRenderObject() as RenderBox;
    debugPrint('size = ${box.size}');
  });
}
```

**Why it matters:** 'ভারী কাজ কোথায় ধীর করছে' — UI না Raster — এই প্রশ্নের উত্তর DevTools-এর দুটি chart থেকে আসে।

**Common mistake:** `build()`-এর ভেতরে network call বা ভারী হিসাব রাখা। `build()` যেকোনো সময় বহুবার ডাকা হতে পারে, তাই এটা pure ও সস্তা হতে হবে।

---

**Q:** Key কেন লাগে? কখন ValueKey, ObjectKey, UniqueKey ও GlobalKey ব্যবহার করবেন?

**A:** Element আপডেটের নিয়ম মনে করুন: runtimeType ও key একই হলে পুরোনো element (এবং তার State) নতুন widget-এর সাথে জুড়ে যায়। যদি list-এর item-এর **order বদলায়** এবং item-গুলো **stateful** হয়, key না থাকলে State ভুল item-এ জুড়ে যায়।

| Key | কখন |
| --- | --- |
| `ValueKey(id)` | item-এর স্থিতিশীল id আছে (সবচেয়ে সাধারণ) |
| `ObjectKey(obj)` | কয়েকটি field মিলিয়ে পরিচয় |
| `UniqueKey()` | প্রতিবার নতুন, state ফেলে দিতে চান |
| `GlobalKey` | tree-র অন্য জায়গা থেকে State বা RenderObject-এ পৌঁছাতে (যেমন `Form`)। ভারী, কম ব্যবহার করুন |
| `PageStorageKey` | scroll position মনে রাখতে |

**Example:**

```dart
// key ছাড়া: প্রথম item মুছলে checkbox-এর state ভুল item-এ চলে যেতে পারে
ListView(
  children: [
    for (final t in todos) TodoTile(key: ValueKey(t.id), todo: t),
  ],
);

// ভুল: build-এর ভেতরে UniqueKey — প্রতি rebuild-এ state হারায়
TodoTile(key: UniqueKey(), todo: t);
```

**Why it matters:** 'কেন checkbox লাফিয়ে যাচ্ছে?'-র মতো বাস্তব bug-এর কারণ এখানে।

**Common mistake:** সব widget-এ key বসানো। Stateless widget-এ, যেখানে order বদলায় না, key লাগে না। আবার key list item-এর সবচেয়ে ওপরের widget-এ দিতে হয়, ভেতরের কোনো স্তরে নয়।

---

**Q:** StatefulWidget-এর lifecycle ব্যাখ্যা করুন। `setState` আসলে কী করে?

**A:** ক্রম:

```
createState()
   |
initState()               <- একবার; এখানে controller/subscription শুরু
   |
didChangeDependencies()   <- InheritedWidget বদলালে (প্রথমবারও)
   |
build()                   <- বহুবার
   |   ^
   |   +-- setState / didUpdateWidget (parent নতুন config দিলে)
   v
deactivate()
   |
dispose()                 <- একবার; এখানে cancel/dispose
```

- `initState`-এ `super.initState()` **প্রথমে**, `dispose`-এ `super.dispose()` **শেষে** ডাকুন।
- `initState`-এ `Theme.of(context)` বা `MediaQuery.of(context)`-এর মতো inherited জিনিস পড়া যায় না (assertion error); `didChangeDependencies`-এ পড়ুন।
- `setState(fn)` `fn` সাথে সাথে চালায় এবং element-কে dirty করে পরের frame-এ rebuild করায়। `fn` async হতে পারবে না।
- `await`-এর পর widget মুছে গেছে কিনা `mounted` দিয়ে দেখুন।

**Example:**

```dart
class _ClockState extends State<Clock> {
  Timer? _timer;
  String _text = '';

  @override
  void initState() {
    super.initState();
    _timer = Timer.periodic(const Duration(seconds: 1), (_) {
      setState(() => _text = DateTime.now().toIso8601String());
    });
  }

  Future<void> _load() async {
    final data = await repo.fetch();
    if (!mounted) return;              // await-এর পর অবশ্যই
    setState(() => _text = data);
  }

  @override
  void dispose() {
    _timer?.cancel();                  // ভুলে গেলে leak
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => Text(_text);
}
```

**Why it matters:** Resource cleanup ও `mounted` — এই দুটোই production crash ও leak-এর প্রধান কারণ।

**Common mistake:** `dispose`-এ controller বা subscription বন্ধ না করা; অথবা `await`-এর পর `mounted` না দেখে `setState` ডাকা ('setState() called after dispose()')।

---

**Q:** `BuildContext` কী? `InheritedWidget` কীভাবে কাজ করে এবং `of(context)` কেন rebuild ঘটায়?

**A:** `BuildContext` আসলে সেই widget-এর **Element-এর হ্যান্ডেল** — tree-তে আপনি কোথায় আছেন তার ঠিকানা। এটি ব্যবহার করে ওপরের দিকে (ancestor) খোঁজা যায়, নিচে নয়।

`InheritedWidget` tree-র ওপর থেকে নিচের যেকোনো descendant-এ ডেটা পৌঁছে দেয়। `context.dependOnInheritedWidgetOfExactType<T>()` ডাকলে ওই element **নির্ভরশীল (dependent)** হিসেবে নিবন্ধিত হয়; পরে `updateShouldNotify` সত্য হলে সে rebuild হয়। নিবন্ধন না করে শুধু পড়তে চাইলে `getInheritedWidgetOfExactType`।

এই ধারণার ওপরেই `Theme.of`, `MediaQuery.of`, `Provider`, `Riverpod`-এর scope দাঁড়িয়ে আছে।

**Example:**

```dart
class CounterScope extends InheritedWidget {
  const CounterScope({super.key, required this.count, required super.child});
  final int count;

  static CounterScope of(BuildContext context) {
    final scope = context.dependOnInheritedWidgetOfExactType<CounterScope>();
    assert(scope != null, 'No CounterScope found above this context');
    return scope!;
  }

  @override
  bool updateShouldNotify(CounterScope old) => count != old.count;
}

// ব্যবহার: count বদলালে শুধু এই widget rebuild হবে
Text('${CounterScope.of(context).count}');

// সূক্ষ্ম নির্ভরতা: শুধু size বদলালে rebuild (orientation ইত্যাদিতে নয়)
final size = MediaQuery.sizeOf(context);
```

**Why it matters:** State management library-গুলো ভেতরে কী করে — এটা বুঝলে লাইব্রেরির জাদু আর জাদু থাকে না।

**Common mistake:** ভুল context থেকে `Scaffold.of(context)` বা `Navigator.of(context)` ডাকা (যেমন `Scaffold` তৈরি করা একই `build`-এর context থেকে `Scaffold.of`)। সমাধান: `Builder` বা আলাদা widget।

---

**Q:** `build()` সস্তা হলেও Flutter UI ধীর হয় কেন? Rebuild কমাবেন কীভাবে?

**A:** `setState` একটি subtree-কে dirty করে। সেই subtree-র প্রতিটি widget-এর `build()` ডাকে, যদি না framework দেখে যে নতুন widget আগেরটির **একই instance** (identical)। তাই:

1. **`const` widget** — একই instance, তাই subtree এড়িয়ে যায়।
2. **ছোট ছোট widget-এ ভাগ করুন** — `setState` যত নিচে, rebuild তত সংকীর্ণ। বড় `build()`-কে helper method-এ না ভেঙে আলাদা widget class করুন (method-এর ফলে বাদ দেওয়ার সুযোগ থাকে না)।
3. **`ListView.builder`** — শুধু দৃশ্যমান item তৈরি হয় (lazy)। `ListView(children: [...])`-এ সব একসাথে তৈরি হয়।
4. **`RepaintBoundary`** — ঘন ঘন বদলানো অংশ আলাদা layer-এ, ফলে বাকি অংশ পুনরায় আঁকতে হয় না।
5. ভারী কাজ `build()` থেকে বাইরে; `Isolate.run` ব্যবহার করুন।

**Example:**

```dart
// যে অংশ বদলায় শুধু সেটি stateful
Column(
  children: const [
    Header(),                 // const — rebuild হয় না
    BigStaticDescription(),   // const
    LiveCounter(),            // ভেতরে নিজের State; একমাত্র এটাই বদলায়
  ],
);

// Lazy list
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, i) => ItemTile(key: ValueKey(items[i].id), item: items[i]),
);
```

**Why it matters:** 'Flutter ধীর' অভিযোগের বেশিরভাগ কারণ অনাবশ্যক rebuild — ইন্টারভিউয়ার জানতে চান আপনি কীভাবে খুঁজে বের করেন (DevTools-এর 'Track widget rebuilds')।

**Common mistake:** `const` বসানোকে 'মাইক্রো অপটিমাইজেশন' ভাবা। বড় tree-তে এটা বড় সাশ্রয়।

---

**Q:** Debug, Profile ও Release mode-এ পার্থক্য কী? Hot reload কীভাবে কাজ করে? Impeller কী?

**A:**

| Mode | কম্পাইল | ব্যবহার |
| --- | --- | --- |
| Debug | JIT (Dart VM) | development, hot reload, assert চালু, ধীর |
| Profile | AOT | performance মাপা (কিছু tracing চালু) |
| Release | AOT | production, দ্রুত, ছোট, hot reload নেই |

**Hot reload**: বদলানো source কোড চলমান Dart VM-এ ঢুকিয়ে framework-কে widget tree rebuild করতে বলে — **State থাকে**, `initState` আবার চলে না। **Hot restart** অ্যাপ নতুন করে শুরু করে (State যায়)। `main()` বদলালে, global/static initializer বা enum-সংক্রান্ত বড় বদল হলে restart লাগে।

**Impeller** Flutter-এর নতুন rendering engine (Skia-র বদলি)। এর মূল সুবিধা: shader আগে থেকে compile করা থাকে, তাই রানটাইমে shader compile-এর কারণে প্রথমবার animation-এ jank হয় না। Backend: iOS-এ Metal, Android-এ Vulkan (সক্ষম না হলে OpenGL ES)। সাম্প্রতিক Flutter-এ Android 10+ ডিভাইসে Impeller ডিফল্ট — আপনার Flutter version-এর release note দেখে নিন।

**Example:**

```bash
flutter run                    # debug (JIT, hot reload)
flutter run --profile          # performance মাপতে
flutter build appbundle --release   # AOT, production
```

**Why it matters:** 'Debug-এ ধীর লাগছে' — তা স্বাভাবিক; কিন্তু profile mode-এ মাপার অভ্যাস থেকেই বোঝা যায় আপনি production-মানের।

**Common mistake:** Emulator-এর debug build দেখে performance সিদ্ধান্ত নেওয়া; অথবা hot reload-এ State বদলায়নি ভেবে ভুল বাগ খোঁজা (সাধারণত hot restart লাগে)।

---

## ১১. Dart Language Deep Dive

---

**Q:** Dart-এর event loop কীভাবে কাজ করে? Microtask queue আর event queue-র পার্থক্য কী?

**A:** Dart-এর প্রতিটি isolate **একটি থ্রেডে** চলে এবং তার নিজস্ব event loop আছে। দুটি queue আছে:

```
  main() শেষ হলে loop শুরু
        |
        v
+---------------------------+
| 1. Microtask queue        |  <- খালি না হওয়া পর্যন্ত সবসময় আগে চলে
+---------------------------+
        | (খালি হলে)
        v
+---------------------------+
| 2. Event queue            |  <- timer, I/O, touch, Future(...) — একটি করে নেয়
+---------------------------+
        | (একটি event শেষে আবার microtask দেখে)
        v   (বারবার)
```

- **Microtask**: খুব ছোট, তাৎক্ষণিক কাজ (`Future.microtask`, `scheduleMicrotask`)। Future-এর `.then` callback সাধারণত এখানে চলে।
- **Event queue**: বাইরের ঘটনা — Timer, I/O, UI event, `Future(() => ...)`, `Future.delayed`।
- একটি ভারী synchronous কাজ loop আটকে দেয় — UI freeze বা ANR (সেকশন ৯)।

**Example:**

```dart
import 'dart:async';

void main() {
  print('1 main start');
  Future(() => print('5 event queue'));
  Future.microtask(() => print('3 microtask'));
  scheduleMicrotask(() => print('4 microtask 2'));
  Future.delayed(Duration.zero, () => print('6 delayed'));
  print('2 main end');
}
// আউটপুটের ক্রম: 1, 2, 3, 4, 5, 6
```

**Why it matters:** `async` মানে 'আলাদা থ্রেড' নয় — এই ভুল ধারণা ভাঙা ইন্টারভিউয়ের সবচেয়ে সাধারণ পরীক্ষা।

**Common mistake:** ভাবা যে `await` ভারী কাজকে background-এ নেয়। `await` শুধু অপেক্ষা করে; কাজটি যদি Dart কোডে CPU-ভারী হয়, তা একই থ্রেডে চলে এবং UI আটকায়। CPU-ভারী কাজে isolate লাগে।

---

**Q:** Future, async/await ও Stream কীভাবে কাজ করে? Error কীভাবে সামলাবেন?

**A:** `Future<T>` একটি ভবিষ্যৎ মান বা error। `async` ফাংশন সবসময় Future ফেরত দেয়; `await` Future শেষ হওয়া পর্যন্ত ওই ফাংশনকে থামিয়ে রাখে (বাকি অ্যাপ চলতে থাকে)। `Stream<T>` হলো একাধিক মানের ধারা।

|  | Future | Stream |
| --- | --- | --- |
| মান | একটি | অনেক (০ বা তার বেশি) |
| ব্যবহার | API call | WebSocket, location, DB পরিবর্তন |
| শোনা | `await` | `listen` / `await for` |

Stream দুই রকম: **single-subscription** (একজন শ্রোতা, ডিফল্ট) এবং **broadcast** (অনেক শ্রোতা, `asBroadcastStream()`/`StreamController.broadcast()`)।

Error: `await`-এর চারপাশে `try/catch` দিন। `await` ছাড়া ছেড়ে দেওয়া Future-এর error **unhandled** হয়ে যায়। একাধিক স্বাধীন কাজ একসাথে চালাতে `Future.wait` বা Dart 3-এর record `.wait`।

**Example:**

```dart
Future<void> load() async {
  try {
    // সমান্তরালে — ক্রমানুসারে await করলে সময় যোগ হতো
    final (user, posts) = await (fetchUser(), fetchPosts()).wait;
    print('${user.name}: ${posts.length}');
  } on SocketException {
    print('নেটওয়ার্ক নেই');
  } catch (e, st) {
    print('অন্য সমস্যা: $e\n$st');
  }
}

Stream<int> countdown(int from) async* {
  for (var i = from; i >= 0; i--) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;
  }
}

final sub = countdown(3).listen(print, onDone: () => print('শেষ'));
// দরকার শেষে: await sub.cancel();   // নাহলে leak
```

**Why it matters:** সিনিয়রদের কাছে প্রত্যাশা — সমান্তরাল বনাম ক্রমিক await, stream cancel, error propagation বোঝা।

**Common mistake:** স্বাধীন দুটি call-কে পরপর `await` করে সময় দ্বিগুণ করা; আর `StreamSubscription` cancel না করা।

---

**Q:** Isolate কী? কখন ও কীভাবে ব্যবহার করবেন? Isolate-এর সীমাবদ্ধতা কী?

**A:** Isolate হলো নিজস্ব memory ও event loop-সহ আলাদা Dart execution unit। **Isolate-এর মধ্যে mutable memory শেয়ার হয় না** — শুধু message পাঠানো যায় (সেজন্য data race/lock-এর ঝামেলা নেই)।

```
Main isolate                    Worker isolate
(UI + আপনার কোড)               (ভারী কাজ)
   |  -- message (SendPort) -->   |
   |  <-- result --------------   |
   নিজস্ব heap                   নিজস্ব heap
```

কখন লাগে: বড় JSON parse, ছবি প্রসেসিং, encryption, ভারী হিসাব — যা প্রায় ১৬ ms-এর বেশি লাগায়। ছোট কাজে isolate তৈরির খরচই বেশি।

- সহজ উপায়: `Isolate.run(() => ...)` (Dart 2.19+) — কাজ শেষে ফলাফল ফেরত আসে।
- Flutter-এ `compute()` একই উদ্দেশ্যে একটি সহায়ক ফাংশন।
- দীর্ঘস্থায়ী ওয়ার্কার লাগলে `Isolate.spawn` + `ReceivePort`/`SendPort`।

**সীমাবদ্ধতা**: Widget/UI অ্যাক্সেস নেই; ডিফল্টভাবে platform channel/plugin চলে না। Flutter 3.7+ থেকে background isolate-এ platform channel ব্যবহার করতে `RootIsolateToken` লাগে এবং plugin-কেও তা সমর্থন করতে হয়। Closure-এ যা ধরা আছে তা পাঠানো হয় — অকারণে বড় অবজেক্ট ধরলে খরচ বাড়ে।

**Example:**

```dart
import 'dart:convert';
import 'dart:isolate';

Future<List<Item>> parseItems(String raw) {
  return Isolate.run(() {
    final list = jsonDecode(raw) as List<dynamic>;
    return list.map((e) => Item.fromJson(e as Map<String, dynamic>)).toList();
  });
}

// Background isolate-এ platform channel লাগলে (plugin সমর্থন করলে)
final token = RootIsolateToken.instance!;
await Isolate.run(() async {
  BackgroundIsolateBinaryMessenger.ensureInitialized(token);
  // এখন সমর্থিত plugin কল করা যাবে
});
```

**Why it matters:** 'UI jank/ANR কীভাবে সারাবেন' প্রশ্নের মূল উত্তর (সেকশন ৯)।

**Common mistake:** প্রতিটি `async` ফাংশনের জন্য isolate ভাবা; অথবা `Isolate.run`-এর ভেতরে UI/Provider ধরা। আরেকটি ভুল — I/O-ভারী কাজ (network) isolate-এ নেওয়া; network নিজেই non-blocking, isolate লাগে CPU কাজে।

---

**Q:** Null safety, `late`, `final` ও `const` — পার্থক্য কী?

**A:** Dart-এ **sound null safety** (Dart 3-এ বাধ্যতামূলক): টাইপ `String` কখনো null হবে না; null রাখতে `String?`।

| সিনট্যাক্স | অর্থ |
| --- | --- |
| `a?.b` | a null হলে null, নাহলে b |
| `a ?? x` | a null হলে x |
| `a ??= x` | a null হলে x বসাও |
| `a!` | 'আমি নিশ্চিত null নয়' — ভুল হলে runtime exception |
| `late` | পরে সেট হবে; সেটের আগে পড়লে error |
| `late final x = compute()` | প্রথমবার পড়ার সময় একবার হিসাব (lazy) |

`final` — একবার সেট হয় (রানটাইমে)। `const` — **কম্পাইল-টাইমের ধ্রুবক** এবং একই মানের const অবজেক্ট একটাই instance (canonicalized)। এজন্য `const Widget()` rebuild এড়ায় (সেকশন ১০)।

Type promotion: `if (user != null)`-এর ভেতরে local variable স্বয়ংক্রিয়ভাবে non-null হয়ে যায়। (Dart 3.2+ থেকে private final field-ও promote হয়।)

**Example:**

```dart
String? nickname;

void greet() {
  final n = nickname;            // local কপি নিন, promote হবে
  if (n != null) {
    print(n.length);             // এখানে n নিরাপদে String
  }
  print(nickname ?? 'অতিথি');
}

class Repo {
  late final Database _db = _open();   // প্রথম ব্যবহারে একবার
  Database _open() => Database();
}

final now = DateTime.now();       // final: রানটাইমে মান
const pi2 = 3.14 * 2;             // const: কম্পাইল-টাইমে
```

**Why it matters:** `!` ও `late`-এর অপব্যবহার production crash-এর বড় কারণ; ইন্টারভিউয়ার আপনার ধারণার পরিপক্কতা দেখেন।

**Common mistake:** সমস্যা এড়াতে সর্বত্র `!` বা `late` ব্যবহার করা। বরং nullable রেখে ঠিকভাবে handle করুন, অথবা মডেল এমনভাবে বানান যেন null অসম্ভব হয়।

---

**Q:** Dart 3-এর নতুন ফিচার — records, patterns, sealed class, class modifiers — ব্যাখ্যা করুন।

**A:**

- **Records** — নাম-ছাড়া হালকা tuple: `(int, String)`, নামসহ `({int x, int y})`। Structural equality আছে (মান সমান হলে `==` সমান)।
- **Patterns** — ডেটা ভেঙে নেওয়া (destructuring) ও মিলিয়ে দেখা: `final (a, b) = pair;`, `if (json case {'id': int id})`।
- **Switch expression** — মান ফেরত দেয়, `sealed` টাইপে সব কেস না দিলে কম্পাইল error (exhaustiveness)।
- **Class modifiers** — `sealed` (একই library-র সাবটাইপ, exhaustive switch), `final` (বাইরে extend/implement নয়), `base` (extend করা যাবে, implement নয়), `interface` (implement করা যাবে, extend নয়), `mixin class`।

**Example:**

```dart
sealed class Result<T> {}
final class Success<T> extends Result<T> {
  Success(this.data);
  final T data;
}
final class Failure<T> extends Result<T> {
  Failure(this.error);
  final Object error;
}

String describe(Result<int> r) => switch (r) {
      Success(:final data) => 'ঠিক: $data',
      Failure(:final error) => 'ভুল: $error',
    }; // নতুন subtype যোগ করলে এখানে কম্পাইল error — কিছু বাদ পড়বে না

(String, int) userInfo() => ('Rahim', 30);
final (name, age) = userInfo();

void parse(Map<String, dynamic> json) {
  if (json case {'name': String name, 'age': int age}) {
    print('$name, $age');
  }
}
```

**Why it matters:** Sealed + switch দিয়ে UI state (loading/success/error) নিরাপদে মডেল করা আধুনিক Flutter-এর স্ট্যান্ডার্ড (সেকশন ১২)।

**Common mistake:** `sealed` আর `abstract`-কে এক ভাবা। `abstract` exhaustiveness দেয় না; `sealed` দেয়, কিন্তু সাবটাইপ শুধু একই library-তে।

---

**Q:** Dart-এর OOP: mixin, extension, interface, factory constructor ও value equality সংক্ষেপে বুঝিয়ে বলুন।

**A:**

- **Mixin** — একাধিক class-এ কোড পুনর্ব্যবহার (`with`), inheritance ছাড়া।
- **Extension** — বিদ্যমান টাইপে (এমনকি `String`/`DateTime`-এও) নতুন মেথড যোগ।
- **Implicit interface** — প্রতিটি class একটি interface; `implements` করলে সব মেম্বার নিজে লিখতে হয়। `extends` কোড পুনর্ব্যবহার করে।
- **Factory constructor** — নতুন instance না-ও বানাতে পারে (cache/singleton), বা subtype ফেরত দিতে পারে।
- **Value equality** — ডিফল্ট `==` হলো reference equality। মান ধরে তুলনা চাইলে `==` ও `hashCode` দুটোই override করতে হবে (বা `freezed`/`equatable`/record)। নাহলে state management-এ 'বদলায়নি' ভেবে UI আপডেট হয় না।

**Example:**

```dart
mixin Logger {
  void log(String m) => print('[$runtimeType] $m');
}
class Repo with Logger {
  void load() => log('লোড হচ্ছে');
}

extension DateX on DateTime {
  bool get isToday {
    final n = DateTime.now();
    return year == n.year && month == n.month && day == n.day;
  }
}

class Session {
  Session._();
  static final Session _instance = Session._();
  factory Session() => _instance;      // সবসময় একই instance
}

class Point {
  const Point(this.x, this.y);
  final int x, y;
  @override
  bool operator ==(Object other) =>
      other is Point && other.x == x && other.y == y;
  @override
  int get hashCode => Object.hash(x, y);
}
```

**Why it matters:** Equality ভুল হলে Riverpod/Bloc/`setState`-এ অদ্ভুত আচরণ — বাস্তব bug।

**Common mistake:** শুধু `==` override করে `hashCode` ভুলে যাওয়া — Set/Map-এ ভুল ফল হয়।

---

**Q:** Dart collections ও lazy `Iterable`-এ কী কী ফাঁদ আছে?

**A:** `List`, `Set`, `Map` — সাথে spread (`...`), collection `if`/`for`। সবচেয়ে বড় ফাঁদ: `map()`, `where()` **lazy** — `toList()` না ডাকা পর্যন্ত চলে না, এবং প্রতিবার iterate করলে আবার চলে। আরেকটি: `const [1, 2]` বা `List.unmodifiable` বদলানো যায় না (`UnsupportedError`)।

**Example:**

```dart
var calls = 0;
final lazy = [1, 2, 3].map((n) {
  calls++;
  return n * 2;
});
lazy.toList();
lazy.toList();
print(calls); // ৬ — ৩ নয়, কারণ দুবার iterate হয়েছে

final fixed = [1, 2, 3].map((n) => n * 2).toList(); // একবারই হিসাব

final menu = [
  'Home',
  if (isAdmin) 'Admin',
  for (final t in tabs) t.title,
  ...extraItems,
];
```

**Why it matters:** Lazy iterable `build()`-এর ভেতরে বারবার চললে অদৃশ্য performance খরচ হয়।

**Common mistake:** `map` ফলাফল ধরে রেখে বারবার ব্যবহার করা এবং ভাবা যে একবারই চলেছে।

---

**Q:** Dart-এ exception ও error handling কীভাবে করবেন? `Error` আর `Exception`-এর পার্থক্য কী?

**A:** `Exception` — প্রত্যাশিত, সামলানোর মতো ব্যর্থতা (নেটওয়ার্ক নেই, ভুল ইনপুট)। `Error` (যেমন `StateError`, `RangeError`) — প্রোগ্রামারের ভুল; সাধারণত ধরে চেপে না গিয়ে ঠিক করতে হয়। Dart-এ যেকোনো অবজেক্ট `throw` করা যায়, কিন্তু কনভেনশন মানুন।

- `on SomeType catch (e, st)` — নির্দিষ্ট টাইপ ধরা, stack trace সহ।
- `rethrow` — ধরে লগ করে stack trace অক্ষত রেখে আবার ছোড়া।
- `finally` — সবসময় চলে (cleanup)।
- Async-এ `await` ছাড়া Future-এর error ধরা যায় না। অধরা error সর্বশেষে `PlatformDispatcher.instance.onError`-এ আসে (সেকশন ৯)।
- Repository লেয়ারে exception-কে `Result`/sealed টাইপে রূপান্তর করলে UI-তে `try/catch` ছড়াতে হয় না।

**Example:**

```dart
class ApiException implements Exception {
  ApiException(this.message, {this.code});
  final String message;
  final int? code;
  @override
  String toString() => 'ApiException($code): $message';
}

Future<Result<User>> getUser(String id) async {
  try {
    final res = await client.get(Uri.parse('$base/users/$id'));
    if (res.statusCode != 200) {
      return Failure(ApiException('সার্ভার সমস্যা', code: res.statusCode));
    }
    return Success(User.fromJson(jsonDecode(res.body)));
  } on SocketException catch (e) {
    return Failure(e);
  } catch (e, st) {
    log.error('getUser failed', e, st);
    rethrow;                       // অপ্রত্যাশিত হলে ঢেকে ফেলবেন না
  }
}
```

**Why it matters:** সিনিয়র মানে শুধু 'try/catch দিই' নয় — কোথায় ধরব, কোথায় রূপান্তর করব, কোথায় ছাড়ব, তা জানা।

**Common mistake:** `catch (e) {}` — খালি catch দিয়ে error গিলে ফেলা; production-এ কিছুই বোঝা যায় না কেন ব্যর্থ হলো।

---

## ১২. Flutter State Management, Navigation ও Architecture

---

**Q:** Flutter-এ state কত রকমের? setState, Provider, Riverpod, Bloc — কোনটা কখন বেছে নেবেন?

**A:** আগে state-কে দুই ভাগে দেখুন:

- **Ephemeral (UI-local) state** — একটি widget-এর ভেতরেই সীমাবদ্ধ: ট্যাব ইনডেক্স, টেক্সট ফিল্ডের ফোকাস, animation। এখানে `StatefulWidget` + `setState` (বা `ValueNotifier`) যথেষ্ট।
- **App state** — একাধিক screen বা অংশ শেয়ার করে: লগইন করা ইউজার, কার্ট, সেটিংস, সার্ভার থেকে আনা ডেটা। এখানে state management সমাধান লাগে।

| সমাধান | সংক্ষেপে | কখন ভালো |
| --- | --- | --- |
| `setState` / `ValueNotifier` | সবচেয়ে সহজ, কোনো package নেই | ছোট, local state |
| `Provider` (`ChangeNotifier`) | `InheritedWidget`-এর ওপর সহজ মোড়ক | ছোট-মাঝারি অ্যাপ, শেখা সহজ |
| `Riverpod` | compile-time নিরাপদ, `BuildContext` ছাড়া, পরীক্ষা সহজ | মাঝারি-বড় অ্যাপ, async-ভারী কাজ |
| `Bloc` / `Cubit` | event → state, কঠোর কাঠামো, ট্রেস করা সহজ | বড় দল, কঠোর নিয়ম দরকার |

কোনোটিই 'সেরা' নয়। বেছে নিন দলের অভিজ্ঞতা, অ্যাপের আকার, টেস্টযোগ্যতা ও বিদ্যমান কোডবেস দেখে। ইন্টারভিউতে **যুক্তিসহ** বলুন, শুধু নাম নয়।

**Example:**

```dart
// Ephemeral — এখানে Riverpod/Bloc বাড়াবাড়ি
class LikeButton extends StatefulWidget {
  const LikeButton({super.key});
  @override
  State<LikeButton> createState() => _LikeButtonState();
}

class _LikeButtonState extends State<LikeButton> {
  bool _liked = false;
  @override
  Widget build(BuildContext context) => IconButton(
        icon: Icon(_liked ? Icons.favorite : Icons.favorite_border),
        onPressed: () => setState(() => _liked = !_liked),
      );
}
```

**Why it matters:** সিনিয়রের কাছে প্রত্যাশা — trade-off বুঝে সিদ্ধান্ত, ফ্যাশনে নয়।

**Common mistake:** 'আমি সবসময় X ব্যবহার করি' বলা, বা ছোট local state-এও বড় state management ঢোকানো।

---

**Q:** Provider ও `ChangeNotifier` কীভাবে কাজ করে? `watch`, `read`, `select`-এর পার্থক্য কী?

**A:** `ChangeNotifier` ডেটা ধরে রাখে এবং বদলালে `notifyListeners()` ডাকে। `Provider` সেটিকে widget tree-তে (`InheritedWidget`-এর মাধ্যমে — সেকশন ১০) নিচে পৌঁছে দেয়।

- `context.watch<T>()` — মান পড়ে **এবং** বদলালে widget rebuild করে। শুধু `build()`-এর ভেতরে।
- `context.read<T>()` — মান পড়ে, **শোনে না**। ইভেন্ট হ্যান্ডলারে (`onPressed`) ব্যবহার করুন।
- `context.select<T, R>((t) => ...)` — শুধু নির্বাচিত অংশ বদলালে rebuild। অপ্রয়োজনীয় rebuild কমায়।

**Example:**

```dart
class CartModel extends ChangeNotifier {
  final List<Item> _items = [];
  List<Item> get items => List.unmodifiable(_items);   // বাইরে থেকে বদলানো ঠেকায়

  void add(Item i) {
    _items.add(i);
    notifyListeners();                                   // না ডাকলে UI বদলাবে না
  }
}

void main() => runApp(
      ChangeNotifierProvider(create: (_) => CartModel(), child: const App()),
    );

// build-এর ভেতরে: শুধু সংখ্যা বদলালে rebuild
final count = context.select<CartModel, int>((c) => c.items.length);

// ইভেন্টে: read
onPressed: () => context.read<CartModel>().add(item),
```

**Why it matters:** rebuild-এর সীমা কীভাবে ঠিক করেন, সেটাই performance-এর প্রশ্ন (সেকশন ১০)।

**Common mistake:** `build()`-এ `read` ব্যবহার (UI আর আপডেট হয় না) বা `onPressed`-এ `watch` ব্যবহার; এবং list বদলিয়ে `notifyListeners()` ভুলে যাওয়া।

---

**Q:** Riverpod কেন জনপ্রিয়? Provider-এর তুলনায় কী সুবিধা?

**A:** Riverpod-এ provider-গুলো widget tree-র বাইরে গ্লোবাল ঘোষণা হয় কিন্তু state থাকে `ProviderScope`-এ — তাই:

- `BuildContext` ছাড়াই অন্য provider পড়া যায় (`ref`)।
- ভুল provider খুঁজে না পাওয়ার runtime error নেই (কম্পাইল-টাইমে ধরা পড়ে)।
- `AsyncValue` দিয়ে loading/data/error সুন্দরভাবে ধরা যায়।
- Auto-dispose, override (টেস্টে mock) সহজ।
- `ref.watch` (rebuild), `ref.read` (এক-বারের পড়া), `ref.listen` (side effect, যেমন snackbar)।

(নোট: Riverpod-এর নতুন মেজর ভার্সনে API-তে কিছু পরিবর্তন আসে; আপনার প্রজেক্টের ভার্সনের pub.dev ডকুমেন্টেশন দেখে নিন।)

**Example:**

```dart
final todosProvider =
    AsyncNotifierProvider<TodosNotifier, List<Todo>>(TodosNotifier.new);

class TodosNotifier extends AsyncNotifier<List<Todo>> {
  @override
  Future<List<Todo>> build() => ref.watch(todoRepoProvider).fetchAll();

  Future<void> add(String title) async {
    await ref.read(todoRepoProvider).add(title);
    ref.invalidateSelf();        // build() আবার চলবে
    await future;
  }
}

class TodoPage extends ConsumerWidget {
  const TodoPage({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final todos = ref.watch(todosProvider);
    return todos.when(
      data: (list) => ListView(children: [for (final t in list) Text(t.title)]),
      loading: () => const Center(child: CircularProgressIndicator()),
      error: (e, st) => Text('সমস্যা: $e'),
    );
  }
}
// main(): runApp(const ProviderScope(child: App()));
```

**Why it matters:** Android-এর `ViewModel + StateFlow`-এর সমতুল্য ধারণা — এভাবে মিলিয়ে বলতে পারলে দুই প্ল্যাটফর্মের জ্ঞান একসাথে দেখান।

**Common mistake:** `build()`-এর ভেতরে `ref.read` ব্যবহার করে রিঅ্যাক্টিভিটি হারানো; বা সবকিছু একটি বিশাল provider-এ রাখা।

---

**Q:** Bloc ও Cubit কী? কখন Bloc, কখন Cubit?

**A:** **Cubit** — সরাসরি মেথড ডেকে `emit(newState)`। **Bloc** — ইভেন্ট (`Event`) পাঠান, handler সেটি state-এ রূপান্তর করে। Bloc-এ ইভেন্টের লগ/ট্রেস ও `transformer` (debounce, `restartable`, `droppable` — `bloc_concurrency` প্যাকেজে) পাওয়া যায়।

```
UI --event--> Bloc --emit--> State --> BlocBuilder --> UI
```

- Bloc একই মানের পরপর দুটি state emit করলে দ্বিতীয়টি উপেক্ষা করে — তাই state-এ `==` (Equatable/freezed) ঠিক রাখা জরুরি।
- `BlocBuilder` — state দেখে UI আঁকে। `BlocListener` — একবারের কাজ (navigation, snackbar)।
- সহজ ক্ষেত্রে Cubit, জটিল ইভেন্ট-নির্ভর প্রবাহে Bloc।

**Example:**

```dart
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);
  void increment() => emit(state + 1);
}

BlocProvider(
  create: (_) => CounterCubit(),
  child: BlocBuilder<CounterCubit, int>(
    builder: (context, count) => Text('$count'),
  ),
);

// একবারের কাজ — UI-এ নয়, listener-এ
BlocListener<AuthCubit, AuthState>(
  listener: (context, state) {
    if (state is Unauthenticated) context.go('/login');
  },
  child: const HomeView(),
);
```

**Why it matters:** বড় দলে Bloc-এর কঠোর কাঠামো একই ধরনের কোড নিশ্চিত করে — এটি ট্রেড-অফ হিসেবে বলতে পারুন (বেশি boilerplate বনাম পূর্বানুমেয়তা)।

**Common mistake:** `BlocBuilder`-এ navigation/snackbar চালানো (rebuild-এ বারবার চলে); mutable state অবজেক্ট বদলে একই reference emit করা (UI আপডেট হয় না)।

---

**Q:** UI state কীভাবে মডেল করবেন? `isLoading`/`hasError` boolean কেন সমস্যা?

**A:** আলাদা boolean ফ্ল্যাগ থেকে অসম্ভব সংমিশ্রণ তৈরি হয় (`isLoading && hasError` একসাথে সত্য?)। বরং **sealed class** দিয়ে সম্ভাব্য অবস্থাগুলোকেই টাইপে ধরুন (সেকশন ১১)। কম্পাইলার নিশ্চিত করে সব অবস্থা সামলানো হয়েছে। State হবে **immutable** — বদলাতে হলে নতুন অবজেক্ট (`copyWith`)।

বাস্তব সূক্ষ্মতা: Pull-to-refresh-এ পুরোনো ডেটা দেখিয়েই লোডিং দেখানো ভালো; তাই `Loaded`-এর ভেতরে `isRefreshing` রাখা যায়। আর নেভিগেশন/টোস্টের মতো **এক-বারের ঘটনা** state-এ না রেখে আলাদা (listener/stream) মাধ্যমে পাঠান।

**Example:**

```dart
// ভুল: অসম্ভব সংমিশ্রণ সম্ভব
class FeedStateBad {
  bool isLoading = false;
  bool hasError = false;
  List<Item>? items;
}

// ঠিক
sealed class FeedState {}
class FeedLoading extends FeedState {}
class FeedLoaded extends FeedState {
  FeedLoaded(this.items, {this.isRefreshing = false});
  final List<Item> items;
  final bool isRefreshing;
}
class FeedError extends FeedState {
  FeedError(this.message);
  final String message;
}

Widget build(FeedState s) => switch (s) {
      FeedLoading() => const Center(child: CircularProgressIndicator()),
      FeedLoaded(:final items) => ItemList(items),
      FeedError(:final message) => ErrorView(message),
    };
```

**Why it matters:** State মডেলিংয়ের মান দেখায় আপনি বাগ কীভাবে 'ডিজাইনেই অসম্ভব' করেন।

**Common mistake:** state-এর ভেতরে mutable list সরাসরি বদলানো; বা সব অবস্থার জন্য একটি ক্লাসে nullable ফিল্ড ভরে রাখা।

---

**Q:** Flutter অ্যাপের architecture কেমন হওয়া উচিত? Android-এর MVVM/Clean Architecture-এর সাথে মিলিয়ে বলুন।

**A:** প্রচলিত কাঠামো:

```
UI (Widgets)
   |
State holder (Notifier / Cubit)      <- Android ViewModel-এর সমতুল্য
   |
[Domain: entity, use case]  (ঐচ্ছিক)  <- জটিল business logic থাকলে
   |
Repository                           <- একটিই 'সত্যের উৎস' (single source of truth)
   |
Data source: Remote (API) | Local (DB / prefs)
```

নিয়ম: নির্ভরতা শুধু ভেতরের দিকে — Repository জানে না কোন UI তাকে ডাকছে। UI সরাসরি API ডাকে না। Flutter-এর অফিসিয়াল app architecture গাইডও UI layer ও Data layer ভাগ করে, আর Domain layer ঐচ্ছিক রাখে।

| Android | Flutter |
| --- | --- |
| Activity / Composable | Widget |
| ViewModel + StateFlow | Notifier / Cubit + state |
| Repository | Repository (একই ধারণা) |
| Room | Drift / sqflite |
| Retrofit + OkHttp | dio / http + interceptor |
| Hilt | get\_it / Riverpod / Provider |

**Example:**

```
lib/
  core/            # network, storage, theme, error
  features/
    auth/
      data/        # api, dto, repository_impl
      domain/      # entity, repository (abstract), usecase
      presentation/# page, widget, notifier/cubit
    feed/
      data/ domain/ presentation/
  main.dart
```

```dart
abstract interface class FeedRepository {
  Future<List<Post>> getPosts({int page = 1});
}

class FeedRepositoryImpl implements FeedRepository {
  FeedRepositoryImpl(this._api, this._db);
  final FeedApi _api;
  final FeedDao _db;

  @override
  Future<List<Post>> getPosts({int page = 1}) async {
    try {
      final posts = await _api.fetch(page);
      await _db.save(posts);          // cache
      return posts;
    } on SocketException {
      return _db.load();              // offline fallback
    }
  }
}
```

**Why it matters:** বড় অ্যাপে feature-first কাঠামো দল-স্বাধীনতা ও modularization সহজ করে (সেকশন ১৪)।

**Common mistake:** Clean Architecture-এর সব স্তর ছোট অ্যাপেও চাপিয়ে দেওয়া (over-engineering); বা Repository-কে শুধু API wrapper বানিয়ে caching/error mapping উপরে ঠেলে দেওয়া।

---

**Q:** Flutter navigation: Navigator 1.0, Router (2.0) ও go\_router কীভাবে আলাদা? Auth guard ও deep link কীভাবে করবেন?

**A:** **Navigator 1.0** — imperative (`push`/`pop`)। **Router (Navigator 2.0)** — declarative, URL ও stack মেলানো যায় (ওয়েব ও deep link-বান্ধব), কিন্তু সরাসরি লেখা জটিল। **`go_router`** (Flutter team-এর প্যাকেজ) Router-এর ওপর সহজ declarative API দেয়: path-ভিত্তিক route, redirect, nested/shell route, deep link।

- `context.go('/product/42')` — path অনুযায়ী stack সাজায় (বিদ্যমান stack বদলে যেতে পারে)।
- `context.push('/product/42')` — বর্তমান stack-এর ওপর যোগ করে, `pop` করলে ফেরে।
- Bottom navigation-এ প্রতি ট্যাবের state ধরে রাখতে `StatefulShellRoute`।
- Auth guard: `redirect` + লগইন state বদলালে আবার চালাতে `refreshListenable`।
- Android-এ deep link কাজ করতে manifest/App Links সেটআপও লাগে (সেকশন ৪)।

**Example:**

```dart
final router = GoRouter(
  initialLocation: '/',
  refreshListenable: authNotifier,            // লগইন বদলালে redirect আবার চলে
  redirect: (context, state) {
    final loggedIn = authNotifier.isLoggedIn;
    final atLogin = state.matchedLocation == '/login';
    if (!loggedIn && !atLogin) return '/login';
    if (loggedIn && atLogin) return '/';
    return null;                              // কিছু করার নেই
  },
  routes: [
    GoRoute(
      path: '/',
      builder: (c, s) => const HomePage(),
      routes: [
        GoRoute(
          path: 'product/:id',                // পূর্ণ path: /product/:id
          builder: (c, s) => ProductPage(id: s.pathParameters['id']!),
        ),
      ],
    ),
    GoRoute(path: '/login', builder: (c, s) => const LoginPage()),
  ],
);

// MaterialApp.router(routerConfig: router);
```

**Why it matters:** Deep link + auth + back stack একসাথে ঠিক রাখা সিনিয়র-স্তরের সমস্যা।

**Common mistake:** বড় অবজেক্ট `extra`-তে পাঠানো — deep link, ওয়েব reload বা প্রসেস পুনরুদ্ধারে এটি পাওয়া যায় না। শুধু `id` পাঠিয়ে গন্তব্যে ডেটা আনুন।

---

**Q:** Async কোডের সাধারণ ফাঁদ কী কী? `BuildContext` async gap, race condition, debounce, double submit কীভাবে সামলাবেন?

**A:**

1. **Async gap-এর পর `BuildContext`** — `await`-এর পর widget মুছে যেতে পারে। ব্যবহারের আগে `context.mounted` (State-এ `mounted`) দেখুন।
2. **Race condition** — search-as-you-type-এ পুরোনো অনুরোধের উত্তর পরে এলে নতুন ফলাফল মুছে দেয়। প্রতিকার: debounce + শুধু সর্বশেষ অনুরোধের উত্তর গ্রহণ।
3. **Double submit** — লোডিং চলাকালীন বাটন নিষ্ক্রিয় করুন বা state দিয়ে ঠেকান।
4. **Dispose** — Timer, controller, subscription বন্ধ করুন (সেকশন ১০)।

**Example:**

```dart
onPressed: () async {
  await repo.save();
  if (!context.mounted) return;        // নতুন Flutter-এ context.mounted
  Navigator.of(context).pop();
}

class SearchCubit extends Cubit<SearchState> {
  SearchCubit(this._repo) : super(SearchIdle());
  final SearchRepo _repo;
  Timer? _debounce;
  int _latest = 0;

  void onChanged(String q) {
    _debounce?.cancel();
    _debounce = Timer(const Duration(milliseconds: 300), () => _search(q));
  }

  Future<void> _search(String q) async {
    final id = ++_latest;
    emit(SearchLoading());
    final res = await _repo.search(q);
    if (id != _latest) return;         // পুরোনো উত্তর ফেলে দাও
    emit(SearchLoaded(res));
  }

  @override
  Future<void> close() {
    _debounce?.cancel();
    return super.close();
  }
}
```

**Why it matters:** এগুলো প্রোডাকশনের 'মাঝে মাঝে ঘটা' বাগ — ইন্টারভিউতে এগুলো বলতে পারা অভিজ্ঞতার প্রমাণ।

**Common mistake:** শুধু লোডিং স্পিনার দেখিয়ে রেখে ভাবা race সমাধান হয়েছে; আর `await`-এর পর `context` নিশ্চিন্তে ব্যবহার করা।

---

## ১৩. Flutter + Android Integration

---

**Q:** Platform channel কী? `MethodChannel` কীভাবে কাজ করে এবং threading-এ কী খেয়াল রাখবেন?

**A:** Dart কোড Android-এর native API (Battery, Bluetooth, কোনো SDK) সরাসরি ডাকতে পারে না। দুই পাশের মধ্যে **বার্তা** পাঠানোই platform channel:

```
Dart  --invokeMethod('getBatteryLevel')-->  [BinaryMessenger]  -->  Kotlin handler
Dart  <------- result / error -------------                         (platform main thread)
```

- `MethodChannel` — এক-বার প্রশ্ন, এক-বার উত্তর (request/response)।
- `EventChannel` — native থেকে Dart-এ ধারাবাহিক stream (সেন্সর, কানেকশন স্ট্যাটাস)।
- `BasicMessageChannel` — সাধারণ দ্বিমুখী বার্তা।
- চ্যানেলের **নাম দুই পাশে হুবহু এক** হতে হবে (সাধারণত `com.example.app/feature`)। না মিললে `MissingPluginException`।
- ডেটা StandardMessageCodec দিয়ে যায়: সংখ্যা, String, bool, List, Map, `Uint8List` ইত্যাদি; নিজের class সরাসরি যায় না।
- Native handler ডিফল্টভাবে platform **main thread**-এ চলে। ভারী কাজ (ডিস্ক, নেটওয়ার্ক) background-এ করুন এবং `result.success/error` main thread থেকে ডাকুন — নইলে ANR বা crash।

**Example:**

```dart
class BatteryApi {
  static const _channel = MethodChannel('com.example.app/battery');

  Future<int?> level() async {
    try {
      return await _channel.invokeMethod<int>('getBatteryLevel');
    } on PlatformException catch (e) {
      debugPrint('ব্যর্থ: ${e.code} ${e.message}');
      return null;
    } on MissingPluginException {
      return null;               // native পাশে হ্যান্ডলার নেই
    }
  }
}
```

```kotlin
class MainActivity : FlutterActivity() {
    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example.app/battery")
            .setMethodCallHandler { call, result ->
                when (call.method) {
                    "getBatteryLevel" -> {
                        val bm = getSystemService(BATTERY_SERVICE) as BatteryManager
                        val level = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
                        if (level >= 0) result.success(level)
                        else result.error("UNAVAILABLE", "Battery level not available", null)
                    }
                    else -> result.notImplemented()
                }
            }
    }
}
```

**Why it matters:** Flutter + Android সিনিয়র ভূমিকার সবচেয়ে সাধারণ প্রশ্ন; এটি দুই জগতের সেতু।

**Common mistake:** চ্যানেলের ভেতরে ভারী কাজ main thread-এ করা; অথবা native পাশে `result` কখনো না ডাকা (Dart-এর Future চিরকাল ঝুলে থাকে)।

---

**Q:** `EventChannel` কীভাবে ব্যবহার করবেন? Pigeon কী এবং কেন ভালো?

**A:** **EventChannel** — native-এর ঘটনা Dart-এ stream হিসেবে পাঠায়। Dart `listen` করলে native-এ `onListen`, cancel করলে `onCancel` ডাকে — সেখানে receiver/listener register ও unregister করুন (নইলে leak)।

**Pigeon** — রো `MethodChannel`-এ method নাম ও argument স্ট্রিং/Map দিয়ে পাঠাতে হয়, ফলে টাইপ ভুল রানটাইমে ধরা পড়ে। Pigeon একটি Dart স্কিমা থেকে দুই পাশের **type-safe** কোড (Dart + Kotlin/Swift ইত্যাদি) জেনারেট করে — স্ট্রিং-নাম ও ম্যানুয়াল cast কমে যায়।

**Example:**

```kotlin
// EventChannel: চার্জিং স্ট্যাটাস stream
EventChannel(messenger, "com.example.app/charging")
    .setStreamHandler(object : EventChannel.StreamHandler {
        private var receiver: BroadcastReceiver? = null

        override fun onListen(args: Any?, sink: EventChannel.EventSink) {
            receiver = object : BroadcastReceiver() {
                override fun onReceive(c: Context, i: Intent) {
                    val status = i.getIntExtra(BatteryManager.EXTRA_STATUS, -1)
                    sink.success(status == BatteryManager.BATTERY_STATUS_CHARGING)
                }
            }
            registerReceiver(receiver, IntentFilter(Intent.ACTION_BATTERY_CHANGED))
        }

        override fun onCancel(args: Any?) {
            receiver?.let { unregisterReceiver(it) }
            receiver = null
        }
    })
```

```dart
const events = EventChannel('com.example.app/charging');
final charging = events.receiveBroadcastStream().map((e) => e as bool);
```

```dart
// pigeons/messages.dart  (চালান: dart run pigeon --input pigeons/messages.dart)
import 'package:pigeon/pigeon.dart';

@ConfigurePigeon(PigeonOptions(
  dartOut: 'lib/src/messages.g.dart',
  kotlinOut: 'android/app/src/main/kotlin/com/example/app/Messages.g.kt',
  kotlinOptions: KotlinOptions(package: 'com.example.app'),
))
@HostApi()
abstract class DeviceApi {
  String getModel();
}
```

```kotlin
// Kotlin-এ বাস্তবায়ন
DeviceApi.setUp(
    flutterEngine.dartExecutor.binaryMessenger,
    object : DeviceApi {
        override fun getModel(): String = Build.MODEL
    }
)
```

**Why it matters:** বড় টিমে raw channel-এর স্ট্রিং-নাম দ্রুত ভেঙে যায়; Pigeon জানা মানে আপনি maintainable integration করেন।

**Common mistake:** `EventChannel`-এ `onCancel`-এ cleanup না করা, ফলে Activity ঘুরলে বা stream বন্ধ হলে receiver leak করে।

---

**Q:** Dart FFI কী? Platform channel-এর চেয়ে কখন ভালো?

**A:** `dart:ffi` দিয়ে Dart সরাসরি **C/C++ লাইব্রেরির** ফাংশন ডাকে — বার্তা পাঠানো বা serialization ছাড়া। উপযোগী: ইমেজ/অডিও প্রসেসিং, crypto, বিদ্যমান C লাইব্রেরি (SQLite-ধাঁচের), যেখানে কম latency দরকার। Kotlin/Java API-র জন্য মূলত platform channel; Java/Kotlin বাইন্ডিং বানাতে `package:jni` ও `jnigen` আছে (প্রতিষ্ঠিত কিন্তু channel-এর চেয়ে কম প্রচলিত)।

শুরু করতে: `flutter create --template=plugin_ffi my_native` — এতে CMake বিল্ড সেটআপ থাকে।

**Example:**

```c
// native/add.c
int add(int a, int b) { return a + b; }
```

```dart
import 'dart:ffi';

typedef AddNative = Int32 Function(Int32, Int32);
typedef AddDart = int Function(int, int);

final DynamicLibrary _lib = DynamicLibrary.open('libnative_add.so'); // Android
final AddDart add = _lib.lookupFunction<AddNative, AddDart>('add');

void main() => print(add(2, 3)); // 5
```

**Why it matters:** channel বনাম FFI-র trade-off বলতে পারা অভিজ্ঞতার চিহ্ন: channel = সহজ, native SDK-র জন্য; FFI = দ্রুত, C লাইব্রেরির জন্য।

**Common mistake:** FFI ভারী কাজও UI isolate-এ চালানো। ভারী native ফাংশনও ব্লক করে — `Isolate.run`-এ ডাকুন (সেকশন ১১)। আর মেমরি ম্যানুয়ালি `free` না করা।

---

**Q:** Add-to-app কী? বিদ্যমান Android অ্যাপে Flutter screen কীভাবে যোগ করবেন?

**A:** Native অ্যাপের কিছু অংশ (বা একটি flow) Flutter-এ লেখা — পুরো অ্যাপ নতুন করে না লিখে ধাপে ধাপে মাইগ্রেশন। পদ্ধতি:

1. `flutter create -t module my_flutter_module`
2. Android অ্যাপের Gradle-এ module যুক্ত করুন (সোর্স হিসেবে বা AAR আকারে)।
3. Manifest-এ `FlutterActivity` ঘোষণা করুন।
4. `FlutterActivity.createDefaultIntent(context)` বা cached engine দিয়ে খুলুন।

প্রতিটি `FlutterEngine` Dart VM isolate ও মেমরি নেয় এবং প্রথমবার চালু হতে সময় লাগে। তাই cold-start ধীর হলে engine **আগে থেকে গরম (pre-warm)** করে `FlutterEngineCache`-এ রাখুন। একাধিক Flutter screen হলে `FlutterEngineGroup` মেমরি কমায়।

```
Native App (Kotlin)
   |-- Screen A, B (native)
   |-- startActivity(FlutterActivity)  --> Flutter module (Dart)
   |           ^                              |
   +---- MethodChannel / Pigeon ---------------+  (ডেটা আদান-প্রদান)
```

**Example:**

```kotlin
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        val engine = FlutterEngine(this)
        engine.dartExecutor.executeDartEntrypoint(
            DartExecutor.DartEntrypoint.createDefault()
        )
        FlutterEngineCache.getInstance().put("main", engine)
    }
}

// যেকোনো জায়গা থেকে
startActivity(FlutterActivity.withCachedEngine("main").build(this))
```

```xml
<activity
    android:name="io.flutter.embedding.android.FlutterActivity"
    android:theme="@style/Theme.MyApp"
    android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
    android:hardwareAccelerated="true"
    android:windowSoftInputMode="adjustResize" />
```

**Why it matters:** বহু বড় কোম্পানিতে পুরনো native অ্যাপের পাশে Flutter যোগ হয়; এই প্রশ্ন সেই বাস্তবতার।

**Common mistake:** `Application.onCreate`-এ ইঞ্জিন চালু করে সব ব্যবহারকারীর startup ধীর করা (যদি বেশিরভাগ Flutter screen না-ই খোলেন)। ব্যবহারের ঠিক আগে বা lazy-ভাবে গরম করুন। আর Flutter module-এর state ও native state আলাদা — অজান্তে sync ধরে নেওয়া।

---

**Q:** Platform View কী? কখন লাগে এবং খরচ কী?

**A:** Flutter নিজে আঁকে বলে Google Maps বা WebView-এর মতো আসল native view সরাসরি বসানো যায় না। **Platform View** Flutter widget tree-এর ভেতরে একটি আসল Android `View` বসায়।

দুই প্রধান পদ্ধতি (Android):

- **Texture-ভিত্তিক:** native view একটি texture-এ রেন্ডার হয়ে Flutter-এর সাথে compose হয় — Flutter animation মসৃণ, কিন্তু টেক্সট ইনপুট/accessibility-তে কিছু সীমাবদ্ধতা থাকতে পারে।
- **Hybrid Composition:** native view আসল view hierarchy-তে থাকে — আচরণ সঠিক, কিন্তু Flutter রেন্ডারিংয়ে বাড়তি খরচ।

কোনটি ডিফল্ট ও কোন বিকল্প আছে তা Flutter ভার্সনভেদে বদলায় — [Flutter-এর platform views ডক](https://docs.flutter.dev/platform-integration/android/platform-views) দেখে নিন। সাধারণ নিয়ম: যেখানে সম্ভব Flutter-নেটিভ সমাধান বা প্যাকেজ নিন; Platform View শেষ ভরসা।

**Example:**

```dart
const AndroidView(
  viewType: 'com.example.app/native_view',
  creationParams: {'text': 'Hello'},
  creationParamsCodec: StandardMessageCodec(),
);
```

```kotlin
class NativeViewFactory : PlatformViewFactory(StandardMessageCodec.INSTANCE) {
    override fun create(context: Context, viewId: Int, args: Any?): PlatformView {
        val text = (args as? Map<*, *>)?.get("text") as? String ?: ""
        return NativeView(context, text)
    }
}

class NativeView(context: Context, text: String) : PlatformView {
    private val view = TextView(context).apply { this.text = text }
    override fun getView(): View = view
    override fun dispose() {}
}

// MainActivity.configureFlutterEngine-এ:
flutterEngine.platformViewsController.registry
    .registerViewFactory("com.example.app/native_view", NativeViewFactory())
```

**Why it matters:** 'Flutter কীভাবে Google Maps দেখায়?' — এই প্রশ্নে আপনি architecture (সেকশন ১০) ও ট্রেড-অফ একসাথে বলতে পারেন।

**Common mistake:** তালিকার প্রতিটি আইটেমে Platform View বসানো — scroll ধীর ও মেমরি-ভারী হয়।

---

**Q:** Flavor (dev/staging/prod) কীভাবে সাজাবেন? Environment config ও secret কোথায় রাখবেন?

**A:** Flavor মানে একই কোডবেস থেকে আলাদা কনফিগের একাধিক বিল্ড। Android-এ `productFlavors`, Flutter-এ `--flavor`।

- আলাদা `applicationId` (suffix) — dev ও prod একই ফোনে একসাথে ইনস্টল করা যায়।
- আলাদা অ্যাপ নাম/আইকন, আলাদা Firebase প্রজেক্ট (`src/dev/google-services.json`)।
- কনফিগ মান (API URL ইত্যাদি) `--dart-define` বা `--dart-define-from-file` দিয়ে।
- **গোপন তথ্য (API secret) অ্যাপে রাখবেন না।** `dart-define`-এর মান বাইনারিতে ঢুকে যায় এবং বের করা সম্ভব — client-এ থাকা সবকিছুই ধরে নিন প্রকাশ্য। সত্যিকারের secret সার্ভারে।

**Example:**

```kotlin
// android/app/build.gradle.kts
android {
    flavorDimensions += "env"
    productFlavors {
        create("dev") {
            dimension = "env"
            applicationIdSuffix = ".dev"
            resValue("string", "app_name", "MyApp Dev")
        }
        create("prod") {
            dimension = "env"
            resValue("string", "app_name", "MyApp")
        }
    }
}
```

```bash
flutter run --flavor dev --dart-define-from-file=config/dev.json
flutter build appbundle --flavor prod --release --dart-define-from-file=config/prod.json
```

```dart
const apiUrl = String.fromEnvironment('API_URL');   // config/dev.json: {"API_URL": "https://dev.api.example.com"}
```

**Why it matters:** বড় অ্যাপে dev/staging/prod আলাদা না থাকা মানে প্রোডাকশন ডেটায় টেস্ট করা — বিপজ্জনক।

**Common mistake:** `.env` ফাইল asset হিসেবে বান্ডল করে সেটিকে 'নিরাপদ secret' ভাবা; আর `--flavor` দিলে `-t lib/main_dev.dart` মিলিয়ে নেওয়ার প্রয়োজন আছে কি না ভুলে যাওয়া (flavor ও entry point আলাদা বিষয়)।

---

**Q:** Release signing ও Play-তে পাঠানোর ধাপ কী? Obfuscation কীভাবে করবেন?

**A:** ধাপ:

1. **Upload keystore** তৈরি করুন (`keytool`), `key.properties`-এ তথ্য রাখুন — এই ফাইল ও keystore **কখনো git-এ নয়**।
2. `signingConfigs`-এ release কনফিগ দিন।
3. `flutter build appbundle --release` → `.aab` তৈরি।
4. Play Console-এ আপলোড। **Play App Signing** চালু থাকলে Google আসল signing key রাখে, আপনি শুধু upload key রাখেন (হারালে reset সম্ভব — সেকশন ১)।
5. ডিবাগ সিম্বল ও mapping ফাইল সংরক্ষণ/আপলোড করুন, যাতে crash রিপোর্ট পড়া যায়।

**Example:**

```properties
# android/key.properties  (git-ignore করুন)
storePassword=********
keyPassword=********
keyAlias=upload
storeFile=/secure/path/upload-keystore.jks
```

```kotlin
// android/app/build.gradle.kts  (উপরে: import java.util.Properties; import java.io.FileInputStream)
val keyProps = Properties().apply {
    load(FileInputStream(rootProject.file("key.properties")))
}

android {
    signingConfigs {
        create("release") {
            keyAlias = keyProps["keyAlias"] as String
            keyPassword = keyProps["keyPassword"] as String
            storeFile = file(keyProps["storeFile"] as String)
            storePassword = keyProps["storePassword"] as String
        }
    }
    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
        }
    }
}
```

```bash
flutter build appbundle --release \
  --obfuscate --split-debug-info=build/symbols
# build/symbols সংরক্ষণ করুন — crash stack trace পড়তে লাগবে
```

**Why it matters:** Signing ভুল হলে আপডেটই দেওয়া যায় না — এটি 'রিলিজ দায়িত্ব'-এর প্রমাণ।

**Common mistake:** keystore বা পাসওয়ার্ড হারানো/কমিট করে ফেলা; আর `--obfuscate` দিয়ে `--split-debug-info` সংরক্ষণ না করা (পরে crash ডিকোড করা যায় না)। মনে রাখুন, obfuscation reverse-engineering কঠিন করে, অসম্ভব নয় — নিরাপত্তা নয়, বাধা (সেকশন ১৫)।

---

**Q:** Flutter-Android integration-এর সাধারণ বিল্ড ও রানটাইম সমস্যা কী কী এবং কীভাবে সমাধান করবেন?

**A:**

| সমস্যা | সাধারণ কারণ | সমাধান |
| --- | --- | --- |
| `MissingPluginException` | নতুন plugin যোগের পরে hot reload; বা native হ্যান্ডলার নেই | পূর্ণ rebuild/restart, চ্যানেলের নাম মেলানো |
| Gradle/AGP/Kotlin/JDK অসঙ্গতি | ভার্সন মেলেনি | সামঞ্জস্য-টেবিল দেখে ভার্সন মেলান, `flutter clean`, Gradle cache মুছুন |
| `minSdkVersion` conflict | কোনো plugin-এর minSdk বেশি | `minSdk` বাড়ান বা বিকল্প plugin |
| Manifest merge error | দুই library একই attribute ঘোষণা করেছে | `tools:replace` / `tools:node` দিয়ে সমাধান |
| Release-এ কাজ করে না, debug-এ করে | R8 class মুছে ফেলেছে | `proguard-rules.pro`-এ keep rule |
| Native কোড বদলালো কিন্তু ফল নেই | Hot reload Dart-ই বদলায়, Kotlin নয় | পূর্ণ rebuild (`flutter run` আবার) |

দরকারি কমান্ড:

```bash
flutter doctor -v                     # টুলচেইন যাচাই
flutter clean && flutter pub get      # বিল্ড ক্যাশ পরিষ্কার
cd android && ./gradlew :app:dependencies   # dependency tree
cd android && ./gradlew assembleRelease --stacktrace
```

**Example:**

```
# android/app/proguard-rules.pro
-keep class com.example.sdk.** { *; }
```

**Why it matters:** সিনিয়র মানে 'আটকে গেলে কীভাবে ডিবাগ করেন' — Flutter লেয়ার, Gradle লেয়ার, নাকি native লেয়ার, তা আলাদা করে ধরতে পারা।

**Common mistake:** প্রতিবার লাইব্রেরি ভার্সন এলোমেলো বাড়ানো/নামানো। পদ্ধতিগতভাবে ভার্সন সামঞ্জস্য দেখুন এবং কোন লেয়ারে ব্যর্থ (Dart, Gradle, নাকি native) আগে ঠিক করুন।

---

## ১৪. Large-Scale App Engineering

---

**Q:** বড় Flutter অ্যাপে modularization কেন দরকার? কীভাবে করবেন?

**A:** একটি `lib/` ফোল্ডারে সব রাখলে দল বাড়লে ৩টি সমস্যা হয়: build ধীর, merge conflict আর সবকিছু সবকিছুর ওপর নির্ভরশীল (spaghetti)। সমাধান: অ্যাপকে **আলাদা Dart package**-এ ভাগ করা।

```
app/                     <- শুধু wiring: DI, router, flavor
packages/
  core/                  <- network, storage, error, utils
  design_system/         <- theme, কমপোনেন্ট
  feature_auth/          <- লগইন (data/domain/ui)
  feature_feed/
  feature_checkout/

নির্ভরতা: app -> feature_* -> core, design_system
          (feature_a  X->  feature_b  — সরাসরি নয়)
```

- Feature-গুলো একে অপরকে import করবে না; যোগাযোগ interface/route/event দিয়ে।
- Dart-এর pub workspaces (Dart 3.6+) বা Melos দিয়ে একাধিক package এক repo-তে চালানো সহজ।
- লাভ: পার্লেল টিম কাজ, শুধু পরিবর্তিত package টেস্ট, সীমানা স্পষ্ট।
- Android জগতের সমতুল্য: Gradle multi-module (`:feature:auth`, `:core:network`)।

**Example:**

```yaml
# pubspec.yaml (root)
name: my_workspace
environment:
  sdk: ^3.6.0
workspace:
  - app
  - packages/core
  - packages/feature_auth

# packages/feature_auth/pubspec.yaml
name: feature_auth
resolution: workspace
environment:
  sdk: ^3.6.0
dependencies:
  core: any        # workspace-এর ভেতরের package; আলাদা path লাগে না
```

**Why it matters:** '১০ জন থেকে ১০০ জন ডেভেলপার কীভাবে এক অ্যাপে কাজ করবে?' — এই প্রশ্নের মূল উত্তর।

**Common mistake:** শুরুতেই ২০টি package বানিয়ে ফেলা (সীমানা না বুঝে), অথবা feature-গুলো এক অপরকে import করতে দেওয়া, ফলে আবার সব জড়িয়ে যায়।

---

**Q:** Dependency Injection কীভাবে করবেন? get\_it (service locator) আর constructor injection-এর পার্থক্য কী?

**A:** DI-র উদ্দেশ্য: ক্লাস নিজে নিজের dependency বানাবে না, বাইরে থেকে পাবে — ফলে টেস্টে fake বসানো যায়।

- **Constructor injection** — সবচেয়ে সহজ ও স্পষ্ট: dependency কন্সট্রাকটরে দেখা যায়।
- **Service locator (`get_it`)** — গ্লোবাল রেজিস্ট্রি। সহজ, কিন্তু dependency লুকানো গেট কলের ভেতরে (ক্লাসের API দেখে বোঝা যায় না কী লাগবে)।
- **DI container (Riverpod/Provider)** — widget tree/scope-এর সাথে জীবনচক্র মিলিয়ে আসে।
- Lifetime: **singleton** (একবার), **lazy singleton** (প্রথম ব্যবহারে), **factory** (প্রতিবার নতুন) — Hilt-এর scope-র মতো ধারণা।

**Example:**

```dart
final getIt = GetIt.instance;

void setupDi() {
  getIt
    ..registerLazySingleton<Dio>(() => createDio())
    ..registerLazySingleton<AuthRepository>(
        () => AuthRepositoryImpl(getIt<Dio>(), getIt<TokenStore>()))
    ..registerFactory<LoginCubit>(() => LoginCubit(getIt<AuthRepository>()));
}

// ক্লাস নিজে getIt ডাকে না — constructor-এ পায় (টেস্ট সহজ)
class LoginCubit extends Cubit<LoginState> {
  LoginCubit(this._repo) : super(LoginInitial());
  final AuthRepository _repo;
}

// টেস্টে: final cubit = LoginCubit(FakeAuthRepository());
```

**Why it matters:** টেস্টযোগ্যতা ও মডিউলারিটি — দুটোই DI-এর উপর দাঁড়িয়ে।

**Common mistake:** বিজনেস কোডের ভেতরে ছড়িয়ে `getIt<...>()` ডাকা, যা নির্ভরতা অদৃশ্য করে দেয়। রেজিস্ট্রি শুধু composition root-এ রাখুন।

---

**Q:** Networking layer কীভাবে সাজাবেন? Token refresh কীভাবে সামলাবেন?

**A:** একটি কেন্দ্রীয় HTTP client (`dio` বা `http`) — যেখানে timeout, base URL, logging, auth header, retry, error mapping এক জায়গায়। Repository শুধু এই client ব্যবহার করে, নিজে `Dio()` বানায় না।

**Token refresh-এর নিরাপদ নকশা:** ৩টি প্রশ্ন একসাথে `401` পেলে ৩বার refresh নয়, **একবার** refresh, বাকিগুলো অপেক্ষা করে নতুন token-এ আবার চেষ্টা। (ডিফল্ট ডেটা refresh token হারিয়ে ফেললে → লগআউট।)

**Example:**

```dart
class TokenStore {
  String? access;
  Future<void>? _refreshing;

  // single-flight: একসাথে অনেকে ডাকলেও একটাই নেটওয়ার্ক কল
  Future<void> refresh() =>
      _refreshing ??= _doRefresh().whenComplete(() => _refreshing = null);

  Future<void> _doRefresh() async { /* refresh token দিয়ে নতুন access আনুন */ }
}

class AuthInterceptor extends QueuedInterceptor {
  AuthInterceptor(this._tokens, this._plainDio);
  final TokenStore _tokens;
  final Dio _plainDio;   // এই interceptor ছাড়া আলাদা Dio — নইলে queue-এ আটকে যায়

  @override
  void onRequest(RequestOptions o, RequestInterceptorHandler h) {
    final t = _tokens.access;
    if (t != null) o.headers['Authorization'] = 'Bearer $t';
    h.next(o);
  }

  @override
  Future<void> onError(DioException e, ErrorInterceptorHandler h) async {
    if (e.response?.statusCode != 401) return h.next(e);
    try {
      await _tokens.refresh();
      final req = e.requestOptions;
      req.headers['Authorization'] = 'Bearer ${_tokens.access}';
      h.resolve(await _plainDio.fetch(req));
    } catch (_) {
      h.next(e);        // refresh ও ব্যর্থ → UI লগআউট হ্যান্ডেল করবে
    }
  }
}
```

**Why it matters:** Token refresh race ও অনন্ত refresh loop — production-এর জনপ্রিয় বাগ।

**Common mistake:** সব request-এ সাথে সাথে refresh চালানো; অথবা refresh request-ও অথ interceptor দিয়ে যাওয়ানো (অনন্ত লুপ বা deadlock)।

---

**Q:** Offline-first অ্যাপ কীভাবে ডিজাইন করবেন? Sync ও conflict কীভাবে সামলাবেন?

**A:** মূল ধারণা: **UI সবসময় local DB থেকে পড়ে**; নেটওয়ার্ক শুধু DB আপডেট করে।

```
UI  <--stream--  Local DB  <--upsert--  Remote API
                    ^
    লিখতে চাইলে -+--> Outbox (pending প্রতিক্রিয়া) --Sync worker--> API
```

- **Outbox:** অফলাইনে করা কাজ লোকাল DB-তে `pending` হিসেবে রাখুন; নেট এলে পাঠান। Android-এ WorkManager-এর মতো background job (Flutter-এ `workmanager` প্যাকেজ) সহায়ক।
- **Idempotency key:** একই অনুরোধ দুইবার গেলেও সার্ভারে একবারই হবে (client-generated id)।
- **Conflict:** সহজ নিয়ম 'last-write-wins' বা 'server-authoritative'; জটিল ক্ষেত্রে ফিল্ড-স্তরে merge বা ইউজারকে জিজ্ঞাসা।
- 'connected' মানে 'internet আছে' নয় — আসল request ব্যর্থ হলে retry (backoff)।

**Example:**

```dart
class PostRepository {
  PostRepository(this._db, this._api, this._sync);
  final AppDatabase _db;
  final PostApi _api;
  final SyncQueue _sync;

  // UI সবসময় DB থেকে পড়ে
  Stream<List<Post>> watchPosts() => _db.watchPosts();

  Future<void> refresh() async {
    final remote = await _api.fetchPosts();
    await _db.upsertAll(remote);      // DB বদলালে stream UI আপডেট করে
  }

  Future<void> create(String text) async {
    final local = await _db.insertPending(text, clientId: const Uuid().v4());
    unawaited(_sync.enqueue(local));   // অফলাইনেও কাজ
  }
}
```

**Why it matters:** বাংলাদেশী বাজারে অস্থির নেটওয়ার্ক স্বাভাবিক — offline-first গুণগত UX পার্থক্য আনে। ইন্টারভিউতে প্রাসঙ্গিক অভিজ্ঞতা বললে শক্ত স্বার্থ।

**Common mistake:** UI সরাসরি API থেকে পড়া ও শুধু error হলে cache দেখানো (দুই সত্যের উৎস); আর conflict পরিকল্পনা ছাড়াই sync ধরে নেওয়া।

---

**Q:** CI/CD pipeline কেমন হওয়া উচিত? Play Store release কীভাবে করবেন?

**A:** ধাপ:

```
PR  -> format -> analyze -> unit/widget test -> (golden) -> build debug
main-> উপরেরগুলো -> build AAB (signed) -> Internal testing track
     -> QA পাস -> Staged rollout (১% -> ৫% -> ২০% -> ১০০%)
     -> crash-free / ANR metric দেখে এগোন বা halt
```

- Play track: Internal → Closed → Open → Production।
- Version: `pubspec.yaml`-এ `version: 1.4.0+57` — `+57` হলো `versionCode`, প্রতিবার **বাড়তে হবে**।
- Rollback: প্রোডাকশনে পুরোনো ভার্সন ফেরত দেওয়া যায় না — rollout halt করে উচ্চতর versionCode-এ সমাধান রিলিজ করতে হয়।
- Secrets (keystore, API key) CI-র secret store-এ, repo-তে নয়।
- টুল: GitHub Actions / GitLab CI / Codemagic, রিলিজে Fastlane। Flutter version pin করুন (FVM বা CI-তে নির্দিষ্ট channel/version)।

**Example:**

```yaml
# .github/workflows/ci.yml
name: ci
on: [pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          channel: stable
          cache: true
      - run: flutter pub get
      - run: dart format --output=none --set-exit-if-changed .
      - run: flutter analyze
      - run: flutter test --coverage
```

**Why it matters:** 'কিভাবে নিশ্চিত করবেন নতুন release প্রোডাকশন ভাঙবে না?' — staged rollout + metric + অটোমেশন।

**Common mistake:** হাতে build করে একজনের ল্যাপটপ থেকে আপলোড করা (reproducible নয়, দায়িত্ব এক ব্যক্তির ওপর)।

---

**Q:** Feature flag, Remote Config ও force update কী? কীভাবে নিরাপদে ব্যবহার করবেন?

**A:** Feature flag = কোড দিয়ে ফিচার বন্ধ/চালু করার সুইচ, নতুন release ছাড়াই। কাজ: ধাপে ধাপে চালু (১০% ব্যবহারকারী), সমস্যায় **kill switch**, A/B টেস্ট। Firebase Remote Config বা নিজস্ব সার্ভার।

নিয়ম: ডিফল্ট মান অ্যাপের ভেতরে রাখুন (অফলাইনে চলবে), fetch ব্যর্থ হলে ক্র্যাশ নয়, আর ফিচার স্থিতিশীল হলে flag **মুছে ফেলুন** (flag debt)।

**Force update**: সার্ভার/Remote Config-এ `min_version` রাখুন; অ্যাপ চালুর সময় বর্তমান ভার্সনের সঙ্গে তুলনা করে আপডেট স্ক্রিন দেখান। Play-র In-App Updates API ব্যবহারও সম্ভব।

OTA/code push (যেমন Shorebird) Dart কোড আপডেটের সুযোগ দেয়; এটি Play নীতিমালা ও সীমাবদ্ধতা মেনে ব্যবহার করতে হয় — ব্যবহারের আগে অফিসিয়াল ডক যাচাই করুন।

**Example:**

```dart
Future<void> initFlags() async {
  final rc = FirebaseRemoteConfig.instance;
  await rc.setConfigSettings(RemoteConfigSettings(
    fetchTimeout: const Duration(seconds: 10),
    minimumFetchInterval: const Duration(hours: 1),
  ));
  await rc.setDefaults({'new_checkout': false, 'min_version': '1.0.0'});
  try {
    await rc.fetchAndActivate();
  } catch (_) {/* ডিফল্টে চলবে */}
}

bool get useNewCheckout => FirebaseRemoteConfig.instance.getBool('new_checkout');
```

**Why it matters:** বড় অ্যাপে 'নতুন কোড বন্ধ করার দ্রুত উপায়' ঝুঁকি কমায় — রিলিজ ইঞ্জিনিয়ারিংয়ের মূল।

**Common mistake:** flag-এ গোপন তথ্য রাখা (Remote Config ক্লায়েন্টে পড়া যায়); বা flag কখনো পরিষ্কার না করা।

---

**Q:** Observability: crash, log, analytics ও performance monitoring কীভাবে সাজাবেন?

**A:** তিন স্তর: **Crash/ANR রিপোর্টিং** (Crashlytics/Sentry), **Analytics** (ব্যবহারকারী কী করছে), **Performance** (startup, network, screen rendering)। মূল নীতি:

- ভেন্ডর সরাসরি কোডজুড়ে ছড়াবেন না — নিজের `AnalyticsService`/`Logger` ইন্টারফেসের পেছনে রাখুন (ভেন্ডর বদল সহজ, টেস্টে fake)।
- ইভেন্টের নাম ও প্যারামিটার **একটি taxonomy** মেনে (`checkout_started`, `item_id`) — নইলে ডেটা অর্থহীন।
- **PII লগ করবেন না** (ফোন, ইমেইল, টোকেন)। ব্যবহারকারী আইডি হ্যাশ/অ্যানোনিমাস।
- Breadcrumb ও non-fatal error রিপোর্ট করুন — ক্র্যাশের আগের ধাপ বোঝা যায়।
- release health: crash-free users/sessions, ANR rate দেখে rollout সিদ্ধান্ত।
- Obfuscation করলে mapping/symbol ফাইল আপলোড না করলে স্ট্যাকট্রেস পড়া যায় না (সেকশন ১৩)।

**Example:**

```dart
abstract interface class AnalyticsService {
  void log(String event, [Map<String, Object?> params = const {}]);
  void setUser(String? anonymousId);
}

class FirebaseAnalyticsService implements AnalyticsService {
  FirebaseAnalyticsService(this._fa);
  final FirebaseAnalytics _fa;

  @override
  void log(String event, [Map<String, Object?> params = const {}]) {
    _fa.logEvent(name: event, parameters: params.map((k, v) => MapEntry(k, v as Object)));
  }

  @override
  void setUser(String? id) => _fa.setUserId(id: id);
}

class NoopAnalytics implements AnalyticsService { /* টেস্টে */ 
  @override void log(String event, [Map<String, Object?> params = const {}]) {}
  @override void setUser(String? anonymousId) {}
}
```

**Why it matters:** 'প্রোডাকশনে কিছু ভাঙলে কীভাবে জানবেন?' — সিনিয়রের মূল দায়িত্ব।

**Common mistake:** শুধু ক্র্যাশ ট্র্যাক করে ভাবা মনিটরিং হয়ে গেছে; এবং বিশ্লেষণে ব্যবহারকারীর ব্যক্তিগত তথ্য ঢুকিয়ে ফেলা।

---

**Q:** বড় টিমে কোড কোয়ালিটি ও ধারাবাহিকতা কীভাবে নিশ্চিত করবেন?

**A:**

- **Static analysis:** `analysis_options.yaml` — `flutter_lints` বা কঠোর সেট, strict mode; CI-তে `flutter analyze` ফেল হলে মার্জ নয়।
- **Format:** `dart format` বাধ্যতামূলক, তর্ক শেষ।
- **টেস্টের নিয়ম:** নতুন লজিকে unit test; গুরুত্বপূর্ণ UI-তে widget/golden (সেকশন ১৫)।
- **Code review:** ছোট PR, `CODEOWNERS`, আর্কিটেকচার সিদ্ধান্ত লিখে রাখা (ADR)।
- **Dependency নীতি:** অ্যাপে `pubspec.lock` কমিট; নিয়মিত আপগ্রেড; অপ্রয়োজনীয় প্যাকেজ নয়।
- **টুলচেইন পিন:** সবাই একই Flutter ভার্সনে (FVM/CI)।

**Example:**

```yaml
# analysis_options.yaml
include: package:flutter_lints/flutter.yaml

analyzer:
  language:
    strict-casts: true
    strict-inference: true
    strict-raw-types: true

linter:
  rules:
    avoid_print: true
    prefer_const_constructors: true
    always_declare_return_types: true
```

**Why it matters:** সিনিয়র শুধু ভালো কোড লেখে না — **দলের মান** ঠিক রাখার ব্যবস্থা বানায়।

**Common mistake:** নিয়ম শুধু ডকুমেন্টে রাখা, CI-তে বাস্তবায়ন না করা; বা লিন্ট ওয়ার্নিং `// ignore` দিয়ে চাপা দেওয়া।

---

**Q:** Design system, theming, localization (বাংলা সহ) ও accessibility বড় অ্যাপে কীভাবে সামলাবেন?

**A:**

- **Design system:** রং/টাইপ/স্পেসিং `ThemeData` ও `ThemeExtension`-এ; কমপোনেন্ট একটি `design_system` package-এ। হার্ডকোড রং/মাপ নয়।
- **Localization:** `flutter_localizations` + ARB ফাইল + `flutter gen-l10n`। `bn` লোকেল যোগ করা সহজ; তারিখ/সংখ্যা `intl` দিয়ে।
- **Accessibility:** `Semantics` লেবেল, ন্যূনতম টাচ টার্গেট (প্রায় 48dp), পর্যাপ্ত কনট্রাস্ট, টেক্সট স্কেলিংয়ে লেআউট না ভাঙা। TalkBack দিয়ে নিজে পরীক্ষা করুন।

**Example:**

```yaml
# l10n.yaml
arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
```

```json
{
  "greeting": "Hello {name}",
  "@greeting": { "placeholders": { "name": { "type": "String" } } }
}
```

```dart
MaterialApp(
  localizationsDelegates: AppLocalizations.localizationsDelegates,
  supportedLocales: AppLocalizations.supportedLocales,   // en, bn
  home: const Home(),
);

Text(AppLocalizations.of(context)!.greeting('Rahim'));

IconButton(
  tooltip: 'Delete',                       // TalkBack-এ পড়ে
  icon: const Icon(Icons.delete),
  onPressed: onDelete,
);

Semantics(
  label: 'Add to cart',
  button: true,
  child: GestureDetector(onTap: add, child: const CartIcon()),
);
```

**Why it matters:** বাংলাদেশি ও আন্তর্জাতিক দুই বাজারের অ্যাপে এগুলো আবশ্যক, আর accessibility আইনি/নৈতিক দায়ও।

**Common mistake:** স্ট্রিং কোডে হার্ডকোড করা; বাংলা টেক্সট বড় ফন্ট/স্কেলে ওভারফ্লো হচ্ছে কি না না দেখা; এবং শুধু রঙ দিয়ে অবস্থা বোঝানো।

---

## ১৫. Flutter Performance, Testing ও Security

---

**Q:** Flutter UI performance-এর বাস্তব checklist কী? List, image, animation কীভাবে দ্রুত করবেন?

**A:** সবাগে মাপুন: `flutter run --profile` + DevTools Performance (UI vs Raster chart), 'Track widget rebuilds', প্রয়োজনে `showPerformanceOverlay`। তারপর সাধারণ কারণগুলো দেখুন:

| সমস্যা | সমাধান |
| --- | --- |
| বড় list | `ListView.builder`, সমান উচ্চতার item হলে `itemExtent`/`prototypeItem` |
| বড় image decode | `cacheWidth`/`cacheHeight`, network image-এ cache package |
| অনাবশ্যক rebuild | `const`, ছোট widget, সঠিক state scope |
| বড় subtree-তে `Opacity`/অনাবশ্যক clip | `FadeTransition`/`AnimatedOpacity`, দরকার ছাড়া clip নয় (`saveLayer` খরচের) |
| প্রতি frame-এ স্থির অংশ rebuild | `AnimatedBuilder`-এর `child` প্যারামিটার, `RepaintBoundary` |
| main isolate-এ ভারী কাজ | `Isolate.run` (সেকশন ১১) |

**Example:**

```dart
// স্থির অংশ (child) প্রতি frame-এ পুনরায় তৈরি হয় না
AnimatedBuilder(
  animation: _controller,
  child: const ExpensiveStaticCard(),
  builder: (context, child) => Transform.rotate(
    angle: _controller.value * 2 * pi,
    child: child,
  ),
);

ListView.builder(
  itemExtent: 72,                       // সমান উচ্চতা হলে layout দ্রুত
  itemCount: items.length,
  itemBuilder: (context, i) => ItemTile(items[i]),
);

Image.network(url, cacheWidth: 400);     // decode-কৃত আকার ছোট
```

**Why it matters:** 'মাপা → ধরা → সারানো' — ইন্টারভিউয়ার পদ্ধতি দেখেন, মুখস্থ tip নয়।

**Common mistake:** debug mode-এ performance দেখা, অথবা প্রথমেই সবকিছু `RepaintBoundary` দিয়ে মোড়া (বেশি layer = বেশি মেমরি)।

---

**Q:** Flutter-এ memory কীভাবে নিয়ন্ত্রণ করবেন? Image cache কী?

**A:** Flutter-এর `ImageCache` ডিকোড করা ছবি মেমরিতে রাখে (ডিফল্টে প্রায় ১০০ MB / ১০০০ ছবি সীমা)। বড় ছবি বড় আকারে decode হলে মেমরি দ্রুত ভরে। সমাধান:

- `cacheWidth/cacheHeight` দিয়ে ডিসপ্লে আকারে decode।
- দরকার হলে cache সীমা কমানো, মেমরি চাপে পরিষ্কার করা।
- Dart দিকে: `AnimationController`, `TextEditingController`, `StreamSubscription`, `Timer` — সব `dispose` (সেকশন ১০)।
- DevTools Memory: snapshot নিন, স্ক্রিন খুলে বন্ধ করে আবার snapshot, তুলনা করুন — যে object রয়ে গেছে তা-ই leak।

**Example:**

```dart
class _AppState extends State<App> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    PaintingBinding.instance.imageCache.maximumSizeBytes = 50 << 20; // ~50 MB
  }

  @override
  void didHaveMemoryPressure() {
    PaintingBinding.instance.imageCache
      ..clear()
      ..clearLiveImages();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => const MaterialApp(home: Home());
}
```

**Why it matters:** সস্তা ডিভাইসে OOM crash বাংলাদেশে বাস্তব সমস্যা — কম RAM-বাঁধা ডিভাইসে টেস্ট করুন।

**Common mistake:** প্রতিটি ছবি পূর্ণ আকারে decode করা (২০০০×৩০০০ px ছবি ২০০dp কার্ডে দেখানো)।

---

**Q:** Flutter testing pyramid কী? Unit ও widget test কীভাবে লিখবেন?

**A:**

```
        /\
       /E2E\        <- কম, ধীর, সবকিছু একসাথে (integration_test)
      /------\
     / Widget \     <- UI আচরণ (testWidgets)
    /----------\
   /   Unit     \   <- সবচেয়ে বেশি, দ্রুত (লজিক, repository, cubit)
```

- **Unit test:** শুধু Dart কোড, Flutter ছাড়াই।
- **Widget test:** স্ক্রিন-ছোট widget-কে একটি কৃত্রিম পরিবেশে চালিয়ে দেখা — তালিকায় কোনো সেলফোন/emulator লাগে না, দ্রুত।
- `tester.pump()` একটি frame; `pumpAndSettle()` সব animation শেষ হওয়া পর্যন্ত — অসীম animation (যেমন ঘুরতে থাকা spinner) থাকলে timeout হয়।

**Example:**

```dart
test('10% discount', () {
  expect(applyDiscount(100, 10), 90);
});

testWidgets('counter increments', (tester) async {
  await tester.pumpWidget(const MaterialApp(home: CounterPage()));

  expect(find.text('0'), findsOneWidget);
  await tester.tap(find.byIcon(Icons.add));
  await tester.pump();                       // একটি frame আঁকুন
  expect(find.text('1'), findsOneWidget);
});
```

**Why it matters:** 'কী করলে আপনি অ্যাপ ভাঙেনি বলবেন' — তার বাস্তব উত্তর এখানে।

**Common mistake:** সব টেস্ট UI-লেভেলে লেখা (ধীর, flaky); অথবা coverage % পিছনে ছুটতে অর্থহীন টেস্ট লেখা।

---

**Q:** Mock/fake কীভাবে ব্যবহার করবেন? Bloc/Riverpod ও timer/debounce কীভাবে টেস্ট করবেন?

**A:** DI (সেকশন ১৪) থাকলে টেস্টে আসল repository-র জায়গায় fake বসানো যায়।

- **Fake** — হাতে লেখা সরল বাস্তবায়ন (মেমরির list)।
- **Mock** (`mocktail`/`mockito`) — কী ডাকা হলো তা যাচাই (`verify`)।
- **Bloc:** `bloc_test`। **Riverpod:** `ProviderContainer(overrides: [...])`।
- Timer/debounce: `fakeAsync` (`fake_async` package) — মিথ্যা সময় এগিয়ে দেয়, সত্যিকারে অপেক্ষা না করে।

**Example:**

```dart
class MockAuthRepo extends Mock implements AuthRepository {}

blocTest<LoginCubit, LoginState>(
  'সফল হলে Loading তারপর Success',
  build: () {
    final repo = MockAuthRepo();
    when(() => repo.login('a', 'b')).thenAnswer((_) async => const User('1'));
    return LoginCubit(repo);
  },
  act: (c) => c.submit('a', 'b'),
  expect: () => [isA<LoginLoading>(), isA<LoginSuccess>()],
);

// Riverpod: provider override
final container = ProviderContainer(
  overrides: [authRepoProvider.overrideWithValue(FakeAuthRepo())],
);
addTearDown(container.dispose);

// debounce: মিথ্যা সময়
test('300ms debounce', () {
  fakeAsync((async) {
    final cubit = SearchCubit(fakeRepo)..onChanged('a');
    async.elapse(const Duration(milliseconds: 300));
    async.flushMicrotasks();
    expect(fakeRepo.calls, ['a']);
  });
});
```

**Why it matters:** async কোড টেস্ট করতে পারা মানে deterministic টেস্ট — কোনো `Future.delayed` অপেক্ষা নয়।

**Common mistake:** টেস্টে সত্যিকারে `await Future.delayed(...)` দিয়ে অপেক্ষা করা (ধীর ও flaky)। আর `any()` ব্যবহার করলে mocktail-এ `registerFallbackValue` ভুলে যাওয়া।

---

**Q:** Golden test, integration test ও Android-সাইড টেস্ট CI-তে কীভাবে চালাবেন?

**A:**

- **Golden test** — widget-এর ছবিকে পূর্বসংরক্ষিত ছবির সাথে মেলায়। UI regression ধরে। সতর্কতা: ফন্ট/OS ভেদে pixel আলাদা — CI-র একই পরিবেশে চালান। আপডেট: `flutter test --update-goldens`।
- **Integration test** — `integration_test` package, আসল ডিভাইস/emulator-এ পুরো অ্যাপ চলে। Firebase Test Lab-এ বহু ডিভাইসে চালানো যায়।
- **Native Android অংশ** — platform channel handler-এর লজিকে Kotlin unit test (JUnit); পুরো UI-তে Espresso/UI Automator (add-to-app হলে বিশেষ করে)।

**Example:**

```dart
// golden
await tester.pumpWidget(const MaterialApp(home: Scaffold(body: ProfileCard())));
await expectLater(
  find.byType(ProfileCard),
  matchesGoldenFile('goldens/profile_card.png'),
);

// integration_test/app_test.dart
void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('login flow', (tester) async {
    app.main();
    await tester.pumpAndSettle();
    await tester.enterText(find.byKey(const Key('email')), 'a@b.com');
    await tester.tap(find.text('Login'));
    await tester.pumpAndSettle();
    expect(find.text('Home'), findsOneWidget);
  });
}
```

```bash
flutter test integration_test/app_test.dart -d <device_id>
```

**Why it matters:** বড় টিমে UI regression আর রিলিজ আস্থা আসে এই স্তরগুলো থেকে।

**Common mistake:** সব screen-এ golden রাখা (রকমতাস বাড়ে, ছোটখাটো বদলে সব ফেল) — শুধু গুরুত্বপূর্ণ কমপোনেন্টে।

---

**Q:** Token, গোপন তথ্য ও API key Flutter অ্যাপে কোথায় রাখবেন?

**A:**

- `SharedPreferences` — সাদা টেক্সট; root করা ডিভাইসে পড়া যায়। **গোপন তথ্য রাখবেন না।**
- `flutter_secure_storage` — Android Keystore-ভিত্তিক এনক্রিপশনে সংরক্ষণ (সার্ভার token, refresh token)।
- অ্যাপের কোডে/asset-এ/`dart-define`-এ রাখা সবকিছুই বের করা যায় (সেকশন ১৩)। সত্যিকারের secret সার্ভারে; অ্যাপে শুধু অল্পসময়ের token।
- Google Maps-এর মতো client-side API key অ্যাপে থাকতেই পারে — তাই কনসোলে package name + SHA-1 দিয়ে **restrict** করুন।
- **Auto Backup:** এনক্রিপ্টেড ডেটা ব্যাকআপে যেতে পারে কিন্তু Keystore key যায় না — নতুন ফোনে restore-এ decrypt ব্যর্থ হয়। `allowBackup="false"` বা নির্দিষ্ট exclude rule দিন।

**Example:**

```dart
const storage = FlutterSecureStorage();

Future<void> saveRefresh(String token) =>
    storage.write(key: 'refresh_token', value: token);

Future<String?> readRefresh() => storage.read(key: 'refresh_token');

Future<void> logout() => storage.deleteAll();   // লগআউটে মুছুন
```

```xml
<!-- AndroidManifest.xml -->
<application
    android:allowBackup="false"
    ... >
```

**Why it matters:** 'কী সংরক্ষণ করবেন আর কী করবেন না' — সিনিয়র সিকিউরিটি-চিন্তার সবচেয়ে সহজ পরীক্ষা।

**Common mistake:** `.env`/Dart কনস্ট্যান্টে সার্ভারের secret key রেখে obfuscation ভরসা করা।

---

**Q:** Network security: HTTPS, certificate pinning ও Network Security Config Flutter-এ কীভাবে কাজ করে?

**A:** Android 9+ (targetSdk 28+) অ্যাপে ডিফল্টে cleartext HTTP বন্ধ। সব API **HTTPS**-এ রাখুন।

**Certificate pinning** — শুধু আপনার সার্ভারের certificate/public key বিশ্বাস করা, যাতে MITM কঠিন হয়।

**Flutter-এর বিশেষ ফাঁদ:** Dart-এর `dart:io` নিজস্ব TLS stack ব্যবহার করে, Android-এর Java HTTP stack নয় — তাই `network_security_config.xml`-এর pin-set সাধারণত Dart-এর ট্রাফিকে প্রযোজ্য নয় (প্রতিটি Flutter version-এ পরীক্ষা করে নিন)। প্রতিকার Dart-এ: `SecurityContext(withTrustedRoots: false)` + আপনার certificate/CA পিন। `badCertificateCallback` দিয়ে pin করলে সমস্যা: এটি শুধু যখন certificate যাচাই ব্যর্থ হয় তখনই ডাকা হয়, বৈধ certificate-এ নয় — তাই নির্ভরযোগ্য pin নয়, আর `return true` রাখলে পুরো TLS নিরাপত্তা বন্ধ হয়ে যায়।

**Pinning-এর ঝুঁকি:** certificate মেয়াদ শেষ/বদলালে অ্যাপ কাজ বন্ধ হয়ে যায়। তাই ব্যাকআপ pin, মেয়াদ, ও দ্রুত আপডেট/force update পরিকল্পনা থাকতে হবে (সেকশন ১৪)।

**Example:**

```dart
Future<Dio> pinnedDio() async {
  final pem = await rootBundle.load('assets/certs/api_ca.pem');
  final ctx = SecurityContext(withTrustedRoots: false)
    ..setTrustedCertificatesBytes(pem.buffer.asUint8List());

  final dio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));
  dio.httpClientAdapter = IOHttpClientAdapter(
    createHttpClient: () => HttpClient(context: ctx),
  );
  return dio;
}
```

```xml
<!-- res/xml/network_security_config.xml : native (OkHttp/WebView) ট্রাফিকের জন্য -->
<network-security-config>
    <base-config cleartextTrafficPermitted="false" />
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2027-12-31">
            <pin digest="SHA-256">PRIMARY_PIN_BASE64=</pin>
            <pin digest="SHA-256">BACKUP_PIN_BASE64=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

**Why it matters:** Android native ও Flutter-এর প্রতিরক্ষা-স্তর আলাদা — এই পার্থক্য জানা সিনিয়র Flutter+Android ব্যক্তির চিহ্ন।

**Common mistake:** শুধু `network_security_config.xml` সেট করে ভাবা Flutter ট্রাফিক pinned; অথবা ডেভে `badCertificateCallback = (...) => true` রেখে প্রোডাকশনে পাঠিয়ে দেওয়া।

---

**Q:** Reverse engineering, root detection, Play Integrity, `FLAG_SECURE` ও biometric — বাস্তবে কী করবেন?

**A:** নিরাপত্তা পর্যায়ভিত্তিক (defense in depth) — কোনো একটি বাঁচাবে না:

- **Obfuscation + R8** — reverse engineering কঠিন করে, **অসম্ভব করে না**।
- **Root detection** — কিছু সংকেত, এড়ানো যায়; একক সিদ্ধান্তের ভিত্তি নয়।
- **Play Integrity API** — অ্যাপ আসল নাকি, ডিভাইস নিরাপদ নাকি — সার্ভারে প্রমাণ যাচাই করতে হয় (**client-এ সিদ্ধান্ত নয়**), নন্স ব্যবহার করে replay রোধ।
- **`FLAG_SECURE`** — screenshot ও Recents-এ preview বন্ধ (পেমেন্ট/সম্পদের স্ক্রিনে)।
- **Biometric** — `local_auth` দিয়ে UI gate; শক্ত সুরক্ষায় Keystore key-তে `setUserAuthenticationRequired` (native সাইড)।
- **অন্যান্য:** দরকার ছাড়া component `exported=false`, deep link input validate, WebView JS সীমিত, release-এ লগে PII নেই।
- Checklist: **OWASP MASVS**।

**Example:**

```kotlin
// MainActivity.kt — screenshot ও Recents preview বন্ধ
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    window.addFlags(WindowManager.LayoutParams.FLAG_SECURE)
}

// Play Integrity: nonce সার্ভার থেকে আসে, token সার্ভারে যাচাই হয়
val manager = IntegrityManagerFactory.create(applicationContext)
manager.requestIntegrityToken(
    IntegrityTokenRequest.builder().setNonce(nonceFromServer).build()
).addOnSuccessListener { response ->
    val token = response.token()    // সার্ভারকে পাঠান, সেখানে verify
}
```

```dart
final auth = LocalAuthentication();
final ok = await auth.authenticate(
  localizedReason: 'পেমেন্ট নিশ্চিত করতে পরিচয় দিন',
);
if (!ok) return;
```

**Why it matters:** সিনিয়র পরিষ্কার বলতে পারে — কোন সুরক্ষা কী বাঁচায়, কী বাঁচায় না। 'Obfuscation দিয়ে নিরাপদ' বলা সবচেয়ে পরিচিত ভুল।

**Common mistake:** client-side root/integrity check-কে চূড়ান্ত মনে করা (স্বার্থহান ডিভাইসে বাইপাসযোগ্য), আর বায়োমেট্রিক পাস হলেই সার্ভারে অনুমতি দেওয়া (সার্ভার নিজে token যাচাই করবে)।

---

## ১৬. Mobile System Design

---

**Q:** Mobile system design ইন্টারভিউতে কোন কাঠামো মেনে উত্তর দেবেন? Backend system design থেকে পার্থক্য কী?

**A:** Backend design-এ মূল প্রশ্ন হলো স্কেল (কত RPS, কয়টা সার্ভার)। Mobile design-এ মূল প্রশ্ন হলো ক্লায়েন্ট নিজে: অস্থির নেটওয়ার্ক, সীমিত ব্যাটারি ও মেমোরি, OS যেকোনো সময় অ্যাপ kill করতে পারে, আর UX (স্ক্রিনে কত দ্রুত কনটেন্ট দেখা যায়)। যেকোনো প্রশ্নে এই ছয় ধাপ মেনে চলুন:

```
1. Requirements : functional + non-functional (offline? realtime? ব্যাটারি? স্কেল?)
2. API ও data model : কী পাঠাবেন/আনবেন, pagination, id, versioning
3. Client architecture : UI -> state -> repository -> local DB + remote
4. Data flow ও caching : কোথায় cache, কখন invalidate
5. Failure handling : retry, backoff, offline, আংশিক ব্যর্থতা
6. Trade-off : কেন এটা বেছে নিলেন, বিকল্প কী ছিল
```

প্রায় সব মোবাইল ডিজাইনের মূল কাঠামো একই:

```
   UI (Widget / Compose)
        |  observe state
   State holder (Riverpod / Bloc / ViewModel)
        |
   Repository  <----  Single Source of Truth = Local DB
     |       \
     |        \__ Sync worker (outbox, WorkManager)
   Remote (REST / WebSocket / FCM)
```

**Example:** প্রশ্ন: "Instagram-এর মতো feed ডিজাইন করো।" শুরুতেই জিজ্ঞেস করুন: offline-এ পুরোনো পোস্ট দেখাতে হবে কি? লাইক/কমেন্ট offline-এ করা যাবে কি? ছবি/ভিডিও কত বড়? এই উত্তরগুলোই ঠিক করে দেয় আপনার design-এ local DB আর outbox লাগবে কি না।

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি requirement না জেনেই সমাধানে ঝাঁপ দেন কি না, আর মোবাইলের বাস্তব সীমাবদ্ধতা (offline, ব্যাটারি, process death) মাথায় রাখেন কি না।

**Common mistake:** Backend-এর মতো করে শুধু load balancer, sharding নিয়ে কথা বলা। ক্লায়েন্টের cache, state ও failure handling বাদ পড়ে যায়।

---

**Q:** একটি Feed (Facebook/Instagram টাইপ) অ্যাপের ক্লায়েন্ট সাইড কীভাবে ডিজাইন করবেন? Pagination, caching, optimistic UI?

**A:** তিনটি সিদ্ধান্ত সবচেয়ে গুরুত্বপূর্ণ।

**১. Pagination: cursor-based, offset নয়।** Offset (`page=2`) ব্যবহার করলে মাঝখানে নতুন পোস্ট এলে সব আইটেম সরে যায়, ফলে duplicate বা হারিয়ে যাওয়া আইটেম দেখা দেয়। Cursor (`after=<lastId বা token>`) স্থিতিশীল, কারণ সে "এই আইটেমের পর থেকে দাও" বলে।

**২. Local DB = single source of truth।** UI সরাসরি নেটওয়ার্ক রেসপন্স দেখায় না; নেটওয়ার্ক থেকে এনে DB-তে লেখা হয়, UI DB-র Stream দেখে। এতে অ্যাপ খুললেই পুরোনো ফিড সাথে সাথে দেখা যায় (দ্রুত TTID), আর offline-এও কাজ করে। Android-এ এটাই Paging 3 + RemoteMediator প্যাটার্ন।

**৩. Optimistic UI:** লাইক চাপলে সার্ভারের উত্তরের জন্য অপেক্ষা না করে সাথে সাথে UI বদলান, ব্যর্থ হলে rollback করুন।

```
  scroll শেষের কাছাকাছি
        |
  loadMore() --cursor--> API
        |                  |
        |<---- page + nextCursor
   DB.transaction( upsert posts + save cursor )
        |
   DB Stream --> UI আপডেট
```

**Example:**

```dart
class FeedRepository {
  FeedRepository(this._api, this._db);
  final FeedApi _api;
  final FeedDb _db;

  // UI শুধু DB দেখে
  Stream<List<Post>> watchFeed() => _db.watchPosts();

  Future<void> loadMore() async {
    final cursor = await _db.readCursor(); // শেষ cursor লোকাল DB-তে রাখা
    final page = await _api.getFeed(cursor: cursor, limit: 20);
    await _db.transaction(() async {
      await _db.upsertPosts(page.items);
      await _db.saveCursor(page.nextCursor);
    });
  }

  Future<void> toggleLike(Post p) async {
    final updated = p.copyWith(
      liked: !p.liked,
      likes: p.likes + (p.liked ? -1 : 1),
    );
    await _db.updatePost(updated); // সাথে সাথে UI বদলাবে
    try {
      await _api.setLike(p.id, liked: updated.liked);
    } catch (_) {
      await _db.updatePost(p); // rollback
    }
  }
}
```

ছবি লোডে `cached_network_image` ব্যবহার করুন এবং ছবি যে সাইজে দেখাবেন সেই সাইজে decode করুন (`cacheWidth`/`cacheHeight`, নাহলে বড় ছবি মেমোরি খায়)। তালিকায় `ListView.builder` (lazy) ব্যবহার করুন।

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি offset-এর সমস্যা জানেন কি না, UI-কে নেটওয়ার্ক থেকে আলাদা করতে পারেন কি না, আর UX-এর জন্য optimistic update বোঝেন কি না।

**Common mistake:** `page++` দিয়ে offset pagination করা; UI-তে সরাসরি API রেসপন্স রাখা (offline-এ ফাঁকা স্ক্রিন); optimistic update-এ rollback না রাখা।

---

**Q:** Real-time আপডেটের জন্য Polling, Long polling, SSE, WebSocket আর FCM — কোনটা কখন ব্যবহার করবেন?

**A:** প্রতিটির জায়গা আলাদা:

| পদ্ধতি | কীভাবে কাজ করে | কখন ভালো |
| --- | --- | --- |
| Polling | নির্দিষ্ট সময় পরপর ক্লায়েন্ট জিজ্ঞেস করে | সহজ কাজ, কম আপডেট; ব্যাটারি ও ডেটা বেশি খরচ |
| Long polling | সার্ভার আপডেট না থাকলে রেসপন্স ধরে রাখে | WebSocket সম্ভব না হলে বিকল্প |
| SSE | সার্ভার থেকে ক্লায়েন্টে একমুখী স্ট্রিম | লাইভ স্কোর, নোটিফিকেশন ফিড |
| WebSocket | দুই দিকে স্থায়ী সংযোগ | চ্যাট, লাইভ কোলাবোরেশন, অ্যাপ খোলা অবস্থায় |
| FCM push | Google-এর সার্ভিস ডিভাইসে বার্তা পৌঁছায় | অ্যাপ বন্ধ/ব্যাকগ্রাউন্ডে থাকলে |

মূল নিয়ম: **WebSocket শুধু অ্যাপ foreground-এ থাকলে চালু রাখুন।** ব্যাকগ্রাউন্ডে গেলে OS সংযোগ বন্ধ করে দিতে পারে এবং স্থায়ী সংযোগ ব্যাটারি খায়। অ্যাপ বন্ধ থাকলে নতুন বার্তা জানানোর কাজ FCM-এর; ইউজার নোটিফিকেশনে ট্যাপ করে অ্যাপ খুললে তখন WebSocket আবার চালু হয় এবং বাকি বার্তা sync হয়।

```
  Foreground : App <==== WebSocket ====> Server (তাৎক্ষণিক)
  Background : Server --FCM--> Device --> Notification
                                  |
                         ট্যাপ -> অ্যাপ খোলে -> WebSocket + sync
```

**Example:**

```dart
// অ্যাপ lifecycle অনুযায়ী সংযোগ নিয়ন্ত্রণ
class ChatLifecycle with WidgetsBindingObserver {
  ChatLifecycle(this._socket);
  final ChatSocket _socket;

  void start() => WidgetsBinding.instance.addObserver(this);
  void stop() => WidgetsBinding.instance.removeObserver(this);

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) {
      _socket.connect();
    } else if (state == AppLifecycleState.paused) {
      _socket.disconnect();
    }
  }
}
```

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি ব্যাটারি ও OS-এর সীমাবদ্ধতা বোঝেন কি না, আর ঠিক টুলটি বেছে নিতে পারেন কি না।

**Common mistake:** "WebSocket সব সময় খোলা রাখব" বলা; অথবা FCM-কে নির্ভরযোগ্য ডেটা পাইপ ভাবা। FCM শুধু "জাগানোর" সংকেত, বার্তা হারাতে বা দেরিতে আসতে পারে, তাই আসল ডেটা সবসময় API/sync থেকে নিতে হয়।

---

**Q:** একটি Chat অ্যাপ (WhatsApp/Messenger টাইপ) কীভাবে ডিজাইন করবেন? Message ordering, delivery status, offline কীভাবে সামলাবেন?

**A:** পাঁচটি বিষয়:

**১. Local-first:** পাঠানো বার্তা আগে লোকাল DB-তে `sending` অবস্থায় যায়, UI সাথে সাথে দেখায়। তারপর নেটওয়ার্কে যায়।

**২. Client-generated id:** প্রতিটি বার্তার জন্য ক্লায়েন্ট UUID বানায়। রিট্রাই করলেও সার্ভার একই id দেখে duplicate বুঝতে পারে (idempotency)।

**৩. Ordering:** ডিভাইসের ঘড়ি বিশ্বাসযোগ্য নয়। সার্ভার প্রতি কনভারসেশনে ক্রমিক sequence নম্বর দেয়; ক্লায়েন্ট সেটা দিয়ে সাজায়।

**৪. Delivery status:** `sending -> sent (সার্ভার পেয়েছে) -> delivered (ডিভাইসে পৌঁছেছে) -> read`। শেষ দুটো receipt হিসেবে আসে।

**৫. Reconnect:** সংযোগ ছিঁড়লে exponential backoff + jitter দিয়ে আবার সংযোগ, আর সংযোগের পর "আমার শেষ sequence এই, এর পরের সব দাও" বলে মিস হওয়া বার্তা নেওয়া।

```
  User পাঠায়
     |
  DB: msg(clientId, status=sending)  --> UI সাথে সাথে দেখায়
     |
  WebSocket send --> Server (seq বসায়)
     |                      |
  ack(clientId, seq) <------+  --> status=sent
     |
  receipt(delivered/read) ----> status আপডেট
```

**Example:**

```dart
import 'dart:math';

Future<void> connectWithRetry() async {
  var attempt = 0;
  while (!_disposed) {
    try {
      final ch = WebSocketChannel.connect(Uri.parse(url));
      await ch.ready; // সংযোগ সফল হলে সম্পন্ন হয়
      attempt = 0;
      // মিস হওয়া বার্তা চেয়ে নিন
      ch.sink.add(jsonEncode({'type': 'resume', 'afterSeq': await _db.lastSeq()}));
      await for (final raw in ch.stream) {
        await _handle(raw);
      }
    } catch (_) {
      // নিচে backoff
    }
    final seconds = min(30, pow(2, attempt++).toInt());
    final jitter = Random().nextInt(1000);
    await Future.delayed(Duration(seconds: seconds, milliseconds: jitter));
  }
}
```

Jitter কেন: হাজার হাজার ক্লায়েন্টের সংযোগ একসাথে ছিঁড়লে সবাই একই মুহূর্তে reconnect করলে সার্ভারে ঢেউ পড়ে (thundering herd)। র‍্যান্ডম দেরি সেটা ছড়িয়ে দেয়।

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি idempotency, ordering ও reconnect-এর মতো বাস্তব সমস্যা জানেন কি না।

**Common mistake:** ডিভাইসের timestamp দিয়ে ordering করা; retry-তে একই বার্তা দুবার যাওয়া ঠেকাতে id না রাখা; reconnect-এ fixed delay দেওয়া (jitter ছাড়া)।

---

**Q:** Offline-first sync কীভাবে ডিজাইন করবেন? Outbox pattern, conflict, delta sync কী?

**A:** Offline-first মানে: ইউজারের প্রতিটি কাজ আগে লোকাল DB-তে সফল হয়, নেটওয়ার্ক পরে আসে। তিনটি অংশ:

**১. Outbox:** লেখার কাজগুলো (লাইক, পোস্ট, এডিট) DB-র একটি `outbox` টেবিলে সারিবদ্ধ থাকে। Sync worker এক এক করে সার্ভারে পাঠায়।

**২. Idempotency key:** প্রতিটি outbox আইটেমের স্থায়ী id সার্ভারে হেডার হিসেবে যায়। নেটওয়ার্ক কেটে গেলে ক্লায়েন্ট জানে না রিকোয়েস্ট পৌঁছেছিল কি না, তাই retry করে; সার্ভার একই key দেখে দ্বিতীয়বার প্রয়োগ করে না।

**৩. Delta sync:** প্রতিবার সব ডেটা না এনে `GET /changes?since=<token>` দিয়ে শুধু পরিবর্তন আনা। মুছে ফেলা আইটেম জানাতে সার্ভার tombstone (মুছে ফেলার চিহ্ন) পাঠায়।

**Conflict (একই ডেটা দুই ডিভাইসে বদলালে):**

- Last-write-wins: সহজ, কিন্তু একটি পরিবর্তন হারাতে পারে।
- Server authoritative: সার্ভার সিদ্ধান্ত দেয়, ক্লায়েন্ট সেটা মেনে নেয়।
- Merge / CRDT: ক্ষেত্র ধরে বা কাঠামো ধরে মিলিয়ে দেওয়া; জটিল কিন্তু ডেটা হারায় না (যেমন কোলাবোরেটিভ এডিটর)।

কোনটা নেবেন তা ডেটার ধরনের ওপর নির্ভর করে; এটাই trade-off হিসেবে ব্যাখ্যা করুন।

```
  ইউজার কাজ --> DB (সফল ধরে নিন) --> outbox-এ সারি
                                         |
   Trigger: নেট ফিরলে / অ্যাপ resume / পর্যায়ক্রমিক worker
                                         |
                          drain: সার্ভারে পাঠাও (Idempotency-Key)
                                         |
                       সফল -> outbox থেকে সরাও | ব্যর্থ -> backoff
```

**Example:**

```dart
Future<void> drainOutbox() async {
  for (final item in await _db.pendingOutbox()) {
    try {
      await _api.send(item.payload, idempotencyKey: item.id);
      await _db.markDone(item.id);
    } on DioException catch (e) {
      final code = e.response?.statusCode;
      final permanent = code != null && code >= 400 && code < 500 && code != 408 && code != 429;
      if (permanent) {
        await _db.markFailed(item.id); // রিট্রাই করে লাভ নেই, ইউজারকে জানান
      } else {
        break; // নেটওয়ার্ক/5xx: পরে আবার চেষ্টা, ক্রম ঠিক রাখতে এখানেই থামুন
      }
    }
  }
}
```

Trigger হিসেবে `connectivity_plus` (নেট ফিরলে), অ্যাপ `resumed` হলে, আর ব্যাকগ্রাউন্ডের জন্য Android-এ WorkManager (Flutter-এ `workmanager` প্যাকেজ) ব্যবহার করা যায়। Periodic WorkManager-এর সর্বনিম্ন ব্যবধান ১৫ মিনিট। iOS-এ ব্যাকগ্রাউন্ড কাজের সময় OS ঠিক করে, গ্যারান্টি নেই, তাই অ্যাপ খোলার সময়ও sync চালানো জরুরি।

**Why it matters:** Senior ইন্টারভিউতে offline-first সবচেয়ে প্রিয় বিষয়। ইন্টারভিউয়ার দেখেন আপনি idempotency, retry-র ধরন (permanent বনাম transient) আর conflict-এর trade-off জানেন কি না।

**Common mistake:** Retry-তে idempotency key না রাখা (ডাবল পেমেন্ট/ডাবল পোস্ট); সব ব্যর্থতাকেই retry করা (400 ভুল ডেটা বারবার পাঠানো); সব ক্ষেত্রে "last write wins" বলে conflict এড়িয়ে যাওয়া।

---

**Q:** বড় ছবি/ভিডিও আপলোড কীভাবে ডিজাইন করবেন? Resumable upload, progress, background?

**A:** বড় ফাইলে সরাসরি একটি POST করলে নেটওয়ার্ক কেটে গেলে সব আবার শুরু করতে হয়। ঠিক নকশা:

**১. আগে compress করুন:** ছবি resize + কোয়ালিটি কমান, ভিডিও transcode করুন (যেমন `flutter_image_compress`, `video_compress` ধরনের প্যাকেজ)। ডেটা, সময় ও ব্যাটারি বাঁচে।

**২. সরাসরি স্টোরেজে আপলোড:** আপনার অ্যাপ সার্ভারের মধ্য দিয়ে না পাঠিয়ে সার্ভার থেকে presigned URL / upload session নিন, ক্লায়েন্ট সরাসরি স্টোরেজে (S3, GCS) পাঠায়। সার্ভারের ওপর চাপ কমে।

**৩. Resumable / chunked:** ফাইল টুকরো করে পাঠান (যেমন S3 multipart, GCS resumable upload, tus প্রোটোকল)। কোন টুকরো গেছে তা লোকাল DB-তে রাখুন; নেট কেটে গেলে বাকি টুকরো থেকে চালিয়ে যান।

**৪. Commit ধাপ:** আপলোড শেষ হলে সার্ভারকে জানান "ফাইল ready, এই পোস্টের সাথে জুড়ো"। এটা না করলে অর্ধেক আপলোড করা ফাইল ঝুলে থাকে।

**৫. Background:** ইউজার অ্যাপ বন্ধ করলেও আপলোড চলতে হবে। Android-এ দীর্ঘ কাজের জন্য WorkManager (প্রয়োজনে foreground notification সহ), আর Flutter-এ `background_downloader` এর মতো প্যাকেজ ব্যবহার করা যায়। OS-এর নিয়ম বদলায়, তাই এটা নিজের টার্গেট সংস্করণে যাচাই করে নিন।

```
  ফাইল বাছাই --> compress --> সার্ভার থেকে upload session
                                   |
                 chunk 1 -> chunk 2 -> chunk 3 ...  (অগ্রগতি DB-তে)
                      |  নেট কাটলে: বাকি chunk থেকে চালু
                                   |
                           commit API (পোস্টের সাথে জোড়া)
```

**Example:**

```dart
Future<void> uploadFile(File file, String uploadUrl, ValueNotifier<double> progress) async {
  final length = await file.length();
  await dio.put(
    uploadUrl, // presigned URL
    data: file.openRead(), // পুরো ফাইল মেমোরিতে না এনে stream করা
    options: Options(headers: {
      Headers.contentLengthHeader: length,
      Headers.contentTypeHeader: 'video/mp4',
    }),
    onSendProgress: (sent, total) {
      if (total > 0) progress.value = sent / total;
    },
  );
}
```

অগ্রগতি দেখানো, বাতিল করার বোতাম ও ব্যর্থ হলে "আবার চেষ্টা" দেওয়া UX-এর অংশ।

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি বড় ফাইল, দুর্বল নেটওয়ার্ক ও OS-এর ব্যাকগ্রাউন্ড সীমাবদ্ধতা একসাথে সামলাতে পারেন কি না।

**Common mistake:** পুরো ফাইল `readAsBytes()` দিয়ে মেমোরিতে নিয়ে আপলোড করা (OutOfMemory); resumable না করা; আপলোড শুধু স্ক্রিনের ভেতরের কোডে রাখা, ফলে ইউজার অন্য স্ক্রিনে গেলেই আপলোড বন্ধ হয়ে যাওয়া।

---

## ১৭. Senior / Tech Lead Behavioral ও Leadership

নিচের উদাহরণ উত্তরগুলোতে \[ \] চিহ্নিত জায়গায় আপনার নিজের বাস্তব অভিজ্ঞতা ও সংখ্যা বসান। বানানো সংখ্যা বা ঘটনা ইন্টারভিউয়ার ধরে ফেলে।

---

**Q:** Behavioral প্রশ্নের উত্তর কীভাবে গুছিয়ে দেবেন? STAR method কী?

**A:** Behavioral প্রশ্ন সাধারণত শুরু হয় ‘একটি ঘটনার কথা বলুন যেখানে…’ দিয়ে। এখানে ইন্টারভিউয়ার আপনার ভবিষ্যৎ আচরণ আন্দাজ করতে অতীতের আচরণ দেখেন। STAR কাঠামো উত্তরকে গোছানো রাখে:

```
S - Situation : পরিস্থিতি কী ছিল (১-২ বাক্য)
T - Task      : আপনার নিজের দায়িত্ব কী ছিল
A - Action    : আপনি নিজে কী কী করলেন (সবচেয়ে বড় অংশ, ~৬০%)
R - Result    : ফলাফল কী হলো + আপনি কী শিখলেন
```

Senior-এর উত্তরে দুটি জিনিস আলাদাভাবে চোখে পড়ে: ‘আমি’ বনাম ‘আমরা’ (নিজের অবদান স্পষ্ট বলা), এবং ফলাফলের পরিমাপ (সময়, ক্র্যাশ রেট, রিলিজ ফ্রিকোয়েন্সি ইত্যাদি, যা আপনার আসল সংখ্যা)।

**Example:** প্রশ্ন: ‘একটি বড় প্রোডাকশন সমস্যার কথা বলুন।’

- S: \[অ্যাপের কোন ফিচারে\] রিলিজের পর \[ক্র্যাশ বা পেমেন্ট ফেইল\] বাড়ল।
- T: আমি ওই মডিউলের owner ছিলাম, দ্রুত কারণ খুঁজে ঠিক করা আমার দায়িত্ব।
- A: প্রথমে crash report দেখে কারণ সীমাবদ্ধ করলাম, staged rollout থামালাম, ঠিক করে hotfix দিলাম, পরে একটি test ও alert যোগ করলাম।
- R: \[কত সময়ে\] সমাধান হলো; একই ধরনের সমস্যা ধরতে এখন \[কী ব্যবস্থা\] আছে।

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি নিজের ভূমিকা পরিষ্কার বলতে পারেন কি না, চাপে কীভাবে ভাবেন, এবং ঘটনা থেকে process উন্নত করেন কি না।

**Common mistake:** পরিস্থিতি বর্ণনায় অনেক সময় নষ্ট করা, Action-এ ‘আমরা করেছি’ বলে নিজের অবদান অস্পষ্ট রাখা, আর ফলাফল না বলা।

---

**Q:** ‘Tell me about yourself’ — ৮ বছরের অভিজ্ঞতা নিয়ে কীভাবে বলবেন? Native Android/iOS থেকে Flutter, এখন আবার Java, এই যাত্রা কীভাবে ব্যাখ্যা করবেন?

**A:** এটি জীবনী নয়, ৯০ সেকেন্ডের একটি পিচ। কাঠামো: **বর্তমান → অতীত → কেন এই পদ**।

```
১. এখন আমি কী করি (সবচেয়ে শক্তিশালী পরিচয়)
২. কীভাবে এখানে এলাম (নেটিভ -> Flutter, প্রধান অর্জন)
৩. কেন এই পদ/কোম্পানি (আপনি কী দেবেন, কী শিখতে চান)
```

যাত্রার গল্পটিকে দুর্বলতা না বানিয়ে শক্তি হিসেবে বলুন: নেটিভ Android/iOS-এ কাজ করেছেন বলে Flutter-এর নিচের স্তর (platform channel, lifecycle, performance) আপনি বোঝেন, আর বর্তমানে Java-তে কাজ আপনার Android প্ল্যাটফর্ম জ্ঞান গভীর করেছে।

**Example:** ‘আমি প্রায় ৮ বছর ধরে মোবাইল অ্যাপ বানাচ্ছি। প্রথমে নেটিভ Android ও iOS-এ কাজ শুরু করি, পরে Flutter-এ বিশেষজ্ঞ হই, যেখানে আমি \[কী ধরনের অ্যাপ/ফিচার\] বানিয়েছি ও \[কী অর্জন\]। বর্তমানে \[কোম্পানি/প্রজেক্টে\] Java দিয়ে Android-এ কাজ করছি, তাই Flutter ও নেটিভ দুই দিকের গভীর জ্ঞান আমার আছে। এখন এমন একটি senior ভূমিকা খুঁজছি যেখানে আমি architecture ও টিমকে দিকনির্দেশনা দিতে পারব।’

**Why it matters:** প্রথম ২ মিনিটেই ইন্টারভিউয়ার আপনার seniority, পরিষ্কার যোগাযোগ ও ক্যারিয়ারের দিকনির্দেশনা বিচার করেন।

**Common mistake:** সব কোম্পানির নাম ও প্রযুক্তি ধরে ধরে পড়ে যাওয়া; অতীত কাজ নিয়ে অজুহাতের সুরে (‘Java-তে আটকে গেছি’) কথা বলা।

---

**Q:** একটি বড় architecture সিদ্ধান্ত (যেমন state management বা offline strategy বাছাই) কীভাবে নেন এবং টিমকে কীভাবে রাজি করান?

**A:** Senior মানে ‘আমার পছন্দ’ নয়, ‘প্রমাণসহ trade-off’। প্রক্রিয়া:

```
সমস্যা পরিষ্কার করুন (কী ব্যথা? কেন এখন?)
        |
বিকল্প ২-৩টি + প্রতিটির সুবিধা/অসুবিধা
        |
ছোট একটি proof of concept বা spike
        |
লিখিত সিদ্ধান্ত (ADR) + টিমের মতামত
        |
সিদ্ধান্ত + পরে পুনর্মূল্যায়নের সময়
```

ADR (Architecture Decision Record) হলো ছোট একটি লিখিত নথি: প্রেক্ষাপট, সিদ্ধান্ত, বাদ দেওয়া বিকল্প ও কারণ। ছয় মাস পর নতুন সদস্য জানতে পারে কেন এভাবে করা হয়েছিল।

**Example:**

```
# ADR-007: State management হিসেবে Riverpod

প্রেক্ষাপট : স্ক্রিনগুলোর মধ্যে state শেয়ারিং জটিল, test করা কঠিন।
বিকল্প     : Provider, Bloc, Riverpod
সিদ্ধান্ত   : Riverpod (compile-time safety, ভালো test override)
ঝুঁকি       : টিমের নতুন শেখার খরচ -> ২টি workshop + উদাহরণ ফিচার
পুনর্মূল্যায়ন: ৩ মাস পরে
```

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি মতামত চাপিয়ে দেন, নাকি তথ্য দিয়ে টিমকে সঙ্গে নেন; আর সিদ্ধান্ত লিখে রাখার অভ্যাস আছে কি না।

**Common mistake:** ‘এটা industry standard’ বলে যুক্তি শেষ করা; বিকল্প ও খরচ (শেখার সময়, migration) উল্লেখ না করা।

---

**Q:** Code review ও junior-দের mentoring কীভাবে করেন?

**A:** Review-এর উদ্দেশ্য ভুল ধরা নয়, কোডের মান ও টিমের জ্ঞান একসাথে বাড়ানো।

- **প্রথমে automation:** formatting, lint, test CI-তে চলুক। মানুষ শুধু যা মেশিন পারে না (design, নামকরণ, edge case, security) তাই দেখবে।
- **ছোট PR:** বড় PR-এর ভালো review হয় না। কাজ ভেঙে ছোট PR-এ আনতে উৎসাহ দিন।
- **মন্তব্যের ধরন:** কী ঠিক করতে হবে (blocking) আর কী পরামর্শ (nit/optional) আলাদা করে লিখুন; কারণসহ লিখুন।
- **Mentoring:** উত্তর বলে দেওয়ার বদলে প্রশ্ন করে ভাবতে সাহায্য করুন, pair programming করুন, ছোট দায়িত্ব দিয়ে ধাপে ধাপে বাড়ান।

**Example:**

```
নিম্নমানের মন্তব্য : এটা ভুল, বদলাও।
ভালো মন্তব্য       : [blocking] এখানে dispose() না করলে controller লিক করবে
                     (state lifecycle দেখুন)। dispose-এ যোগ করবে?
                     [nit] নামটি isLoading হলে আরও পরিষ্কার হতো।
```

**Why it matters:** Senior/lead পদে আপনার ব্যক্তিগত কোডের চেয়ে টিমের সামগ্রিক মান বাড়ানোর ক্ষমতা বেশি দেখা হয়।

**Common mistake:** স্বাদ বা ব্যক্তিগত স্টাইল নিয়ে বারবার আপত্তি, কঠোর বা ব্যক্তিগত ভাষা, আর সব PR নিজে ঠিক করে দিয়ে junior-কে শেখার সুযোগ না দেওয়া।

---

**Q:** PM, designer বা backend টিমের সঙ্গে মতবিরোধ কীভাবে সামলান? অবাস্তব deadline-এ কী করেন?

**A:** নীতি: **ব্যক্তির সঙ্গে নয়, সমস্যার সঙ্গে লড়ুন; তথ্য ও বিকল্প নিয়ে যান।**

- মতবিরোধে আগে অপর পক্ষের উদ্দেশ্য বুঝুন (তারা কী অর্জন করতে চায়), তারপর নিজের উদ্বেগ তথ্যসহ বলুন।
- Deadline অবাস্তব হলে শুধু ‘না’ নয়; scope, সময় ও মান এই তিনটির ট্রেড-অফ দেখিয়ে বিকল্প দিন।
- সিদ্ধান্ত হয়ে গেলে ভিন্নমত থাকলেও সেটি সমর্থন করুন (disagree and commit), এবং ঝুঁকি লিখে রাখুন।

```
  ‘এই ফিচার ২ সপ্তাহে লাগবে’
        |
  বিকল্প A : পুরো ফিচার, ৬ সপ্তাহ
  বিকল্প B : মূল অংশ (MVP), ২ সপ্তাহ, বাকিটা পরের রিলিজে
  বিকল্প C : পুরো ফিচার ২ সপ্তাহে, কিন্তু test ও মান কম (ঝুঁকি: ক্র্যাশ)
        |
  পণ্যের মালিক ঝুঁকিসহ বেছে নেয়
```

**Example:** ‘\[PM\] একটি ফিচার ২ সপ্তাহে চাইছিলেন, আমার অনুমান ছিল ৫ সপ্তাহ। আমি কাজটি ভেঙে দেখালাম কোন অংশে সময় যাবে, এবং ২ সপ্তাহে মূল ব্যবহারযোগ্য অংশ দেওয়ার বিকল্প দিলাম। তিনি সেটি বেছে নিলেন, আর বাকি অংশ পরের sprint-এ গেল।’ (আপনার নিজের ঘটনা বসান)

**Why it matters:** Senior-কে প্রায়ই product, design ও backend-এর মাঝখানে দাঁড়াতে হয়। ইন্টারভিউয়ার আপনার যোগাযোগ, আপস করার ক্ষমতা ও ঝুঁকি স্বচ্ছ রাখার অভ্যাস দেখেন।

**Common mistake:** সবকিছুতে ‘হ্যাঁ’ বলে পরে ডেলিভারি মিস করা, অথবা সরাসরি ‘এটা সম্ভব না’ বলা, কোনো বিকল্প ছাড়া।

---

**Q:** আপনি নেটিভ Android/iOS ছেড়ে Flutter-এ এসেছিলেন, এখন কেন Android-এও গভীর হতে চান? Flutter বনাম নেটিভ কখন বেছে নেবেন?

**A:** সৎ ও সংক্ষিপ্ত যুক্তি দিন। Flutter একটি কোডবেসে দুই প্ল্যাটফর্মে দ্রুত UI ডেলিভারি দেয়। কিন্তু বড় প্রোডাক্টে প্রায়ই নেটিভ জ্ঞান লাগে: platform channel, নতুন OS API (Health, Bluetooth, Widget, Foreground service), ডিভাইস-নির্দিষ্ট সমস্যা, native SDK ইন্টিগ্রেশন, performance ডিবাগিং। তাই Flutter-এর সঙ্গে Android জানা মানে ‘দুই স্তরেই দায়িত্ব নিতে পারা’।

কখন কী বেছে নেবেন (সাধারণ নির্দেশনা, প্রতিটি প্রজেক্টে ভিন্ন হতে পারে):

| পরিস্থিতি | সাধারণত ভালো |
| --- | --- |
| দুই প্ল্যাটফর্মে প্রায় একই UI/ফিচার, ছোট-মাঝারি টিম | Flutter |
| গভীর OS ইন্টিগ্রেশন (অনেক hardware/system API, widget, wear) | নেটিভ বা Flutter + নেটিভ মডিউল |
| বিদ্যমান বড় নেটিভ অ্যাপে নতুন কিছু স্ক্রিন | Add-to-app (ধাপে ধাপে) |
| টিমের দক্ষতা শুধু নেটিভ, দ্রুত রিলিজ চাপ নেই | নেটিভ |

**Example:** ‘আমার ক্যারিয়ারে নেটিভ থেকে Flutter-এ যাওয়ার কারণ ছিল \[আপনার কারণ, যেমন দুই প্ল্যাটফর্মে ডেলিভারি গতি\]। Flutter-এ কাজ করতে গিয়ে বুঝেছি যে বড় অ্যাপে নেটিভ স্তরের জ্ঞান ছাড়া \[কোন সমস্যা\] সমাধান করা কঠিন। তাই আমি Android-ও গভীরভাবে ঝালিয়ে নিচ্ছি, যাতে প্রয়োজনে নিজেই platform অংশ লিখতে পারি।’

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি টুল নিয়ে ধর্মান্ধ কি না, নাকি প্রয়োজন অনুযায়ী যুক্তিসহ বাছাই করেন।

**Common mistake:** ‘Flutter সব কিছুর জন্য সেরা’ বা ‘নেটিভই সেরা’ জাতীয় চরম মত; Flutter-এ একাধিক বছর কাজ করে নেটিভ জ্ঞান না থাকার অজুহাত দেওয়া।

---

**Q:** আপনার করা একটি ভুল বা ব্যর্থতার কথা বলুন। Technical debt কীভাবে সামলান?

**A:** এখানে ইন্টারভিউয়ার ভুল নয়, **দায়িত্ববোধ ও শেখা** দেখেন। এমন একটি বাস্তব ঘটনা বাছুন যেখানে ক্ষতি ছিল কিন্তু বিপর্যয় নয়, আপনার ভূমিকা সত্যি ছিল, এবং আপনি এরপর process বদলেছেন। অন্যের দোষ দেবেন না।

Technical debt: সব ঋণ খারাপ নয়, যেমন আগে ডেলিভারি দিয়ে পরে ঠিক করা সচেতন সিদ্ধান্ত হতে পারে। শর্ত হলো ঋণটি দৃশ্যমান রাখা (backlog-এ লিখে), খরচ বোঝা (কত ধীর করছে, কত ঝুঁকি), এবং প্রতিটি sprint-এ নির্দিষ্ট সময় (যেমন অল্প শতাংশ) পরিশোধে রাখা।

**Example:** ‘\[একটি রিলিজে\] আমি পর্যাপ্ত test ছাড়া একটি পরিবর্তন দিয়েছিলাম এবং \[ছোট সমস্যা\] হয়েছিল। আমি দ্রুত rollback করি, কারণ বিশ্লেষণ লিখি, এবং এরপর থেকে ওই মডিউলের জন্য CI-তে test বাধ্যতামূলক করি। তারপর থেকে \[ফলাফল\]।’

**Why it matters:** ইন্টারভিউয়ার ভুল স্বীকার করার সততা, দোষ না দেওয়া, এবং পুনরাবৃত্তি ঠেকানোর পদ্ধতি দেখেন।

**Common mistake:** ‘আমি ভুল করি না’ বলা, বা ‘আমার সবচেয়ে বড় দুর্বলতা আমি বেশি পরিশ্রম করি’ ধরনের সাজানো উত্তর; অন্যের ঘাড়ে দোষ চাপানো।

---

**Q:** ইন্টারভিউর শেষে ইন্টারভিউয়ারকে কোন প্রশ্নগুলো করবেন?

**A:** প্রশ্ন আপনার আগ্রহ ও পরিপক্বতা দেখায়। ভালো প্রশ্নগুলো:

- মোবাইল টিমের গঠন কেমন, আর release প্রক্রিয়া কেমন (কত ঘন ঘন, staged rollout আছে কি)?
- বর্তমানে সবচেয়ে বড় technical চ্যালেঞ্জ কী (performance, test coverage, legacy)?
- এই পদে প্রথম ৩ মাসে সফলতা কীভাবে মাপা হবে?
- Flutter ও নেটিভের মধ্যে কাজ কীভাবে ভাগ হয়, কোডবেসের মান ও test কেমন?
- Production সমস্যা হলে on-call ও postmortem কীভাবে হয়?

বেতন, ছুটি ইত্যাদি আলোচনা সাধারণত পরের ধাপে (HR/offer পর্যায়ে) ভালো।

**Example:** ‘আপনারা Flutter অ্যাপে নেটিভ মডিউল কীভাবে রাখেন? আলাদা প্যাকেজ নাকি অ্যাপের ভেতরেই? এই নিয়ে টিমের কোন চ্যালেঞ্জ আছে?’

**Why it matters:** এগুলো দেখায় আপনি শুধু চাকরি খুঁজছেন না, বরং কাজের পরিবেশ ও মান যাচাই করছেন, যা senior-এর বৈশিষ্ট্য।

**Common mistake:** ‘কোনো প্রশ্ন নেই’ বলা, বা প্রথম প্রশ্নেই বেতন/ছুটি/ওয়ার্ক-ফ্রম-হোম নিয়ে জিজ্ঞেস করা।

---

## ১৮. Android ↔ Flutter Cheat Sheet ও ৮ সপ্তাহের Study Plan

---

**Q:** Native Android-এর কোন ধারণা Flutter-এ কিসের সমান? (Quick mapping)

**A:** Android জানা থাকলে Flutter শেখা সহজ, উল্টোটাও সত্য। নিচের টেবিল মুখস্থ নয়, ‘একই সমস্যা, দুই ভাষা’ হিসেবে দেখুন। কিছু জিনিস সম্পূর্ণ সমান নয়; ডানের তুলনাটা আনুমানিক।

| Android (native) | Flutter (প্রায় সমতুল্য) |
| --- | --- |
| Activity / Fragment | Route / Page (`Navigator`, `go_router`) |
| Activity lifecycle (`onResume`, `onPause`) | `AppLifecycleState` (`resumed`, `inactive`, `hidden`, `paused`, `detached`) |
| View / Composable | Widget |
| Compose recomposition | Widget rebuild (`build()` আবার চলে) |
| `remember` / state | `State` ফিল্ড, `setState`, Riverpod/Bloc |
| RecyclerView / LazyColumn | `ListView.builder` |
| ViewModel | `Notifier` / `Cubit` / `ChangeNotifier` |
| LiveData / StateFlow | `Stream`, `ValueNotifier`, Riverpod state |
| Coroutines + Flow | `Future` / `async-await` + `Stream` |
| Room | `drift`, `sqflite` |
| Retrofit + OkHttp | `dio`, `http` |
| Hilt / Dagger | `get_it`, Riverpod (DI) |
| WorkManager | `workmanager` প্যাকেজ (Android-এ WorkManager ব্যবহার করে) |
| DataStore / SharedPreferences | `shared_preferences` |
| Keystore / EncryptedSharedPreferences | `flutter_secure_storage` |
| Intent / App Links | `app_links` + `go_router` |
| Paging 3 | `infinite_scroll_pagination` বা নিজের cursor লজিক |
| Glide / Coil | `cached_network_image` |
| Firebase Crashlytics | `firebase_crashlytics` |
| Gradle `productFlavors` | একই + `flutter run --flavor` |
| R8 / ProGuard | Release-এ R8 চলে; Dart কোডের জন্য `--obfuscate` |
| Profiler / Layout Inspector | Flutter DevTools |

ডায়াগ্রামে Flutter অ্যাপ Android-এ কীভাবে চলে:

```
  Android OS
     |
  MainActivity (FlutterActivity)
     |
  FlutterEngine ---- Dart VM / compiled Dart কোড
     |
  Impeller/Skia দিয়ে নিজের UI আঁকে
     |
  MethodChannel দিয়ে নেটিভ Kotlin/Java কোডের সাথে কথা
```

**Example:** ইন্টারভিউতে প্রশ্ন আসতে পারে: ‘Android-এর ViewModel Flutter-এ কী?’ উত্তর: ‘UI থেকে আলাদা state holder। Flutter-এ সেটা `Notifier`/`Cubit`। তবে Android-এ ViewModel configuration change (যেমন rotation) থেকে বাঁচে, Flutter-এ widget state এমনিই rotation-এ থাকে, কিন্তু process death-এর জন্য দুই জায়গাতেই আলাদা ব্যবস্থা লাগে।’

**Why it matters:** ইন্টারভিউয়ার দেখেন আপনি দুই জগতের ধারণা সংযোগ করে বুঝেছেন কি না, শুধু নাম মুখস্থ নয়।

**Common mistake:** ‘এটা হুবহু সমান’ বলে ফেলা। যেমন Flutter-এর `AppLifecycleState` Activity lifecycle-এর হুবহু সমান নয়; একটি Flutter অ্যাপে একাধিক Activity বা Fragment ধারণা নেই।

---

**Q:** Android নতুন করে শেখার জন্য ৮ সপ্তাহের পরিকল্পনা কেমন হবে?

**A:** ধরে নেওয়া হয়েছে প্রতিদিন ২-৩ ঘণ্টা সময় আছে। নিজের Java কাজ চলাকালীনই প্রতিদিন কিছু Kotlin পড়ুন। প্রতি সপ্তাহের শেষে একটি ছোট deliverable বানান, কারণ শুধু পড়লে মনে থাকে না।

| সপ্তাহ | বিষয় (গাইডের সেকশন) | সপ্তাহ শেষে কী বানাবেন |
| --- | --- | --- |
| ১ | Android platform, components, lifecycle, Intent, Kotlin বেসিক (সেকশন ১-৫) | ছোট একটি Kotlin অ্যাপ, ২ স্ক্রিন, Intent দিয়ে ডেটা পাঠানো |
| ২ | Compose বেসিক, Jetpack architecture (ViewModel, Room) (সেকশন ৬-৭) | Compose-এ একটি To-do অ্যাপ, Room সহ |
| ৩ | Background work, permission, storage, security, performance tools (সেকশন ৮-৯) | WorkManager দিয়ে একটি পর্যায়ক্রমিক কাজ + LeakCanary দিয়ে একটি leak খোঁজা |
| ৪ | Flutter framework ও Dart গভীরে (সেকশন ১০-১১) | নিজের একটি ছোট রেন্ডার/লেআউট পরীক্ষা, event loop-এর আউটপুট ভবিষ্যদ্বাণী অনুশীলন |
| ৫ | State management, navigation, Flutter-Android integration (সেকশন ১২-১৩) | একটি Flutter অ্যাপে MethodChannel দিয়ে Kotlin কোড ডাকা |
| ৬ | Large-scale engineering, performance, testing, security (সেকশন ১৪-১৫) | অ্যাপে offline-first outbox + কিছু unit/widget test + CI workflow |
| ৭ | Mobile system design (সেকশন ১৬) | ৪টি ডিজাইন মুখে বলে অনুশীলন: feed, chat, offline sync, upload |
| ৮ | Behavioral (সেকশন ১৭) + mock interview + দুর্বল জায়গা পুনরাবৃত্তি | নিজের STAR গল্প ৫টি লিখে ফেলা, বন্ধুর সাথে ২টি mock |

প্রতিদিনের ছন্দ (সুপারিশ):

```
  ৬০ মিনিট : নতুন বিষয় পড়া
  ৬০ মিনিট : কোড লেখা / ছোট অনুশীলন
  ৩০ মিনিট : গতকালের প্রশ্ন নিজেকে মুখে বলা (active recall)
```

**Example:** ৩য় সপ্তাহে Section 8-এর WorkManager পড়ে সাথে সাথে একটি Worker লিখুন, `adb shell dumpsys jobscheduler` ইত্যাদি দিয়ে দেখুন কাজ শিডিউল হলো কি না। নিজে চালিয়ে দেখলে ইন্টারভিউতে ‘আমি করেছি’ বলতে পারবেন।

**Why it matters:** আপনার লক্ষ্য শুধু তথ্য জানা নয়, Android-এ কাজ করতে পারার আত্মবিশ্বাস। হাতে কাজ করা বিষয়ই ইন্টারভিউতে স্পষ্ট শোনায়।

**Common mistake:** শুধু পড়া ও ভিডিও দেখা (কোড না লেখা); একসাথে সবকিছু শুরু করা; নিজেকে মুখে উত্তর না বলা (পড়লে মনে হয় বুঝেছি, বলতে গেলে আটকে যায়)।

---

**Q:** ইন্টারভিউয়ের আগের দিন কোন জিনিসগুলো দ্রুত revise করবেন? (Last-day checklist)

**A:** নতুন কিছু শেখার দিন এটা নয়। শুধু নিজের দুর্বল জায়গা ও সবচেয়ে বেশি জিজ্ঞাসিত বিষয়গুলো ঝালিয়ে নিন। নিজেকে মুখে ১-২ মিনিটে বোঝাতে পারেন কি না দেখুন:

```
  Android   : Activity lifecycle, process death, Service vs WorkManager,
              ANR কেন হয়, permission model, Compose recomposition
  Flutter   : Widget/Element/RenderObject, কেন rebuild সস্তা,
              Key কখন লাগে, const-এর উপকার, Impeller কী
  Dart      : event loop (microtask আগে), Future vs Stream, Isolate,
              null safety, sealed class + switch
  State     : আপনার বেছে নেওয়া সমাধান (Riverpod/Bloc) কেন, কোথায় সীমাবদ্ধতা
  Integration: MethodChannel threading, Pigeon, add-to-app
  Large app : modularization, DI, token refresh single-flight,
              offline-first outbox, CI/CD staged rollout
  Security  : secure storage, certificate pinning সীমাবদ্ধতা,
              obfuscation ≠ security
  Design    : কাঠামো (৬ ধাপ), feed/chat/upload ডিজাইন
  Behavioral: ৫টি STAR গল্প, ‘কেন Flutter + Android’ উত্তর
```

তারপর নিজের ২-৩টি বাস্তব প্রজেক্ট সংক্ষেপে প্রস্তুত রাখুন: সমস্যা, আপনার সিদ্ধান্ত, ফলাফল।

**Example:** নিজেকে প্রশ্ন করুন: ‘Dart কি আলাদা UI থ্রেডে চলে?’ সঠিক উত্তর: Flutter 3.29 থেকে Dart কোড প্ল্যাটফর্মের main thread-এ চলে (আগে আলাদা UI thread ছিল); raster কাজ আলাদা thread-এ। সেকশন ২ ও ১০ আবার দেখুন।

**Why it matters:** শেষ মুহূর্তে নতুন বিষয় ঢোকালে আত্মবিশ্বাস কমে। যা ইতিমধ্যে জানেন সেটাই স্পষ্ট ও শান্তভাবে বলতে পারাটাই লক্ষ্য।

**Common mistake:** রাত জেগে নতুন প্যাকেজ বা নতুন আর্কিটেকচার শিখতে যাওয়া; ঘুম বাদ দেওয়া; এমন দাবি করা যা আপনি গভীরে ব্যাখ্যা করতে পারবেন না।

---

## Sources

আপডেটযোগ্য তথ্য (version, API, নীতি) যাচাইয়ের জন্য এই অফিসিয়াল ডকুমেন্টেশন দেখুন। ইন্টারভিউয়ের আগে সংস্করণ-নির্ভর বিষয় (Flutter/Dart version, Impeller, Play target API) এখান থেকে আরেকবার মিলিয়ে নিন।

- [Flutter documentation](https://docs.flutter.dev)
- [Dart documentation](https://dart.dev/guides)
- [Android Developers](https://developer.android.com)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer)
- [OWASP MASVS](https://mas.owasp.org/MASVS/)
