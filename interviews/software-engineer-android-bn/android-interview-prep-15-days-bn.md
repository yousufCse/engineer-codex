# Android Interview Prep — ৭, ১০ বা ১৫ দিনে (বাংলা)

> **কার জন্য:** যে mobile developer native Android-এর interview দেবেন, কিন্তু অনেক কিছু ভুলে গেছেন বা অন্য stack থেকে (যেমন Flutter) আসছেন। আর interview হবে **English-এ** — হয়তো বিদেশি interviewer বা client-এর সাথে।
> **কী আছে:** শুধু Android। প্রশ্ন **সহজ English-এ**। বোঝানো **বাংলায়**। বলার উত্তর **সহজ English-এ**। সাথে security camera, custom Android OS (AOSP), sensor আর multi-layer security-র প্রশ্ন। এসব নিয়ে কাজ করা কোম্পানির interview-এ এগুলো আসে।
> **কতটা নতুন:** সব তথ্য নভেম্বর ২০২৬ পর্যন্ত মিলিয়ে লেখা — Android 17 (API 37), Play-এর target API 36 নিয়ম, নতুন local network permission সহ।
> **গভীরে পড়তে চাইলে:** [Flutter + Android + iOS interview guide](../software-engineer-flutter-android-ios-bn/flutter-android-ios-interview-prep-bn.md) আর [Flutter-এর চোখে Android আর iOS](../../mobile/native/android-ios-for-flutter-devs-bn.md)। এই ফাইল হলো দ্রুত প্রস্তুতির জন্য।

---

## <a id="how-to-use"></a>এই গাইড কীভাবে পড়বেন

প্রতিটা part শুরু হয় **"আগে বুঝুন"** দিয়ে। এখানে পুরো বিষয়ের বড় ছবি আছে। এটা আগে পড়ুন। তারপর প্রশ্নগুলো ধরুন।

প্রতিটা প্রশ্নের গঠন একই:

| অংশ | কী থাকে | আপনি কী করবেন |
|---|---|---|
| প্রশ্ন (English) | interviewer যেভাবে বলবে | জোরে পড়ুন, যাতে কানে চেনা লাগে |
| **প্রশ্নটা মানে** | এক লাইনে, interviewer আসলে কী জানতে চায় | বুঝে নিন |
| **অন্যভাবেও জিজ্ঞেস করে** | একই প্রশ্নের অন্য English রূপ | এগুলোও চিনে রাখুন। Interviewer হুবহু একই কথা বলবে না |
| **বুঝে নিন** | বাংলায় concept | মন দিয়ে পড়ুন। মুখস্থ না, বুঝুন |
| **Answer (English)** | মুখে বলার উত্তর | ঢেকে রেখে নিজে বলুন, তারপর মিলিয়ে নিন |
| **Key words** | যে শব্দগুলো বললে বোঝা যায় আপনি জানেন | উত্তরে এগুলো যেন থাকে |
| **Follow-up** | পরের প্রশ্ন আর ছোট উত্তর | একইভাবে অনুশীলন করুন |
| **ভুল করবেন না** | সবচেয়ে সাধারণ ভুল | মনে রাখুন |

**Priority চিহ্ন:**

| চিহ্ন | মানে | কোন plan-এ |
|---|---|---|
| ★ | অবশ্যই জানতে হবে। প্রায় সব interview-এ আসে | ৭ দিন |
| ◆ | জরুরি। Senior হলে আসে | ১০ দিন |
| ○ | গভীর বা বাড়তি। সময় থাকলে | ১৫ দিন |

**প্রশ্নের নম্বর:** K = Kotlin, C = Core Android, F = Framework-এর ভেতরে, U = UI/Compose, P = Performance/release, R = Architecture/data, B = Flutter→Android সেতু, S = Security, V = Video/camera, O = AOSP/OS, N = Sensor/IoT, D = System design, L = Live coding, H = Behavioral/client।

---

> **অগ্রগতি দেখতে:** গাইডের শেষে আছে [অনুশীলনের খাতা](#tracker)। সব প্রশ্ন এক লাইনে, টিক দেওয়ার বাক্সসহ।

## <a id="study-method"></a>প্রতিদিন কীভাবে পড়বেন (এটাই সবচেয়ে জরুরি)

শুধু পড়লে interview-এ কথা বের হয় না। **মুখে বলার অনুশীলন** করতে হবে। প্রতিদিন এভাবে করুন:

1. **সকাল (৬০–৯০ মিনিট) — বুঝুন।** আজকের part-এর "আগে বুঝুন" পড়ুন। তারপর প্রতিটা প্রশ্নের "বুঝে নিন" পড়ুন। কোনো জায়গা না বুঝলে Android Studio খুলে ছোট code চালিয়ে দেখুন।
2. **দুপুর (৬০ মিনিট) — বলুন।** প্রতিটা প্রশ্নে "Answer (English)" ঢেকে রাখুন। প্রশ্নটা জোরে পড়ুন। নিজে উত্তর বলুন। তারপর লেখা উত্তরের সাথে মেলান। কোন key word বাদ গেল, দেখুন।
3. **ফোনে record করুন।** দিনে অন্তত ৫টা উত্তর record করে শুনুন। খেয়াল করুন: খুব দ্রুত বলছেন কি না, "umm" বেশি কি না, বাক্য অর্ধেক থেমে যাচ্ছে কি না।
4. **সন্ধ্যা (৩০ মিনিট) — মিশিয়ে প্রশ্ন।** আগের দিনগুলোর ★ প্রশ্ন থেকে random ১০টা নিন। প্রতিটার উত্তর ১ মিনিটে বলুন। এটাই আসল interview-এর মতো।
5. **ঘুমের আগে (১০ মিনিট)** — আজকের "ভুল করবেন না" লাইনগুলো একবার পড়ুন।

**মুখস্থ করবেন না।** লেখা উত্তর হলো একটা নমুনা। কথার ক্রম আর key word মনে রাখুন। তারপর নিজের ভাষায় বলুন। মুখস্থ উত্তর follow-up এলে ভেঙে পড়ে। বোঝা উত্তর ভাঙে না।

**হাতে-কলমে একটু করুন।** ৭ দিনের plan-এও অন্তত একটা ছোট Compose app বানান: একটা list, API call, ViewModel, Room, একটা permission। ১-২ ঘণ্টার কাজ। Interview-এ "I built a small sample last week to refresh" বলতে পারবেন — এটা সত্যি হবে, আর আত্মবিশ্বাস দেবে।

---

## <a id="plan-7"></a>৭ দিনের plan (শুধু ★ প্রশ্ন, দিনে ৫–৬ ঘণ্টা)

Kotlin আর Android framework সবচেয়ে বেশি আসে। তাই প্রথম দুই দিন শুধু এগুলো।

| দিন | কী পড়বেন | শেষে নিজেকে পরীক্ষা |
|---|---|---|
| ১ | [শুরুর অংশ](#speak-english) + [Part 1 Kotlin](#part-1)-এর ★ + [Part 1B Kotlin গভীরে](#part-1b)-এর ★ | "Tell me about yourself" ৯০ সেকেন্ডে record করুন। Coroutine vs thread ১ মিনিটে বলুন |
| ২ | [Part 2 Core Android](#part-2)-এর ★ + [Part 2B Framework-এর ভেতরে](#part-2b)-এর ★ + [Part 2C Jetpack আর basics](#part-2c)-এর ★ | Lifecycle, process death, "icon tap করলে কী হয়", "কোন Jetpack library ব্যবহার করেন" — প্রতিটা ১–২ মিনিটে |
| ৩ | [Part 3 Compose](#part-3)-এর ★ + [Part 5 Architecture](#part-5)-এর ★ | MVVM + Hilt + Room দিয়ে একটা ছোট screen বানান |
| ৪ | [Part 7 Security](#part-7)-এর ★ + [Part 6 Flutter→Android](#part-6)-এর ★ | "How do you secure an app?" ২ মিনিটে, স্তর ধরে ধরে |
| ৫ | [Part 8 Camera](#part-8)-এর ★ + [Part 10 Sensor](#part-10)-এর ★ | Camera grid আর sensor battery প্রশ্ন বলুন |
| ৬ | [Part 9 AOSP](#part-9)-এর ★ + [Part 4 Performance](#part-4)-এর ★ | Android version table মুখে বলুন (8 → 17) |
| ৭ | [Part 11 Design](#part-11) D1, D2 + [Part 12 Coding](#part-12)-এর ★ + [Part 13 Behavioral](#part-13)-এর ★ | পুরো mock interview (নিচে দেখুন) |

## <a id="plan-10"></a>১০ দিনের plan (★ + ◆)

| দিন | কী পড়বেন |
|---|---|
| ১ | শুরুর অংশ + Part 1 Kotlin |
| ২ | Part 1B Kotlin গভীরে + Part 2 (C1–C9, C19) |
| ৩ | Part 2 (C10–C18) + Part 6 Flutter→Android |
| ৪ | Part 2B Framework-এর ভেতরে + Part 2C Jetpack আর basics |
| ৫ | Part 3 Compose আর UI |
| ৬ | Part 5 Architecture, data, testing |
| ৭ | Part 7 Security |
| ৮ | Part 8 Camera আর video |
| ৯ | Part 9 AOSP + Part 10 Sensor + Part 4 Performance (★ আর ◆) |
| ১০ | Part 11 Design (D1–D4, D7) + Part 12 Coding + Part 13 Behavioral + mock interview |

## <a id="plan-15"></a>১৫ দিনের plan (সব প্রশ্ন, ধীরে, শক্ত করে)

| দিন | কী পড়বেন |
|---|---|
| ১ | শুরুর অংশ + Part 1 (K1–K7, K27, K28, K8–K10) |
| ২ | Part 1 (K11–K17) + Part 1B (K18–K26) |
| ৩ | Part 2 (C1–C3, C19, C4–C9) |
| ৪ | Part 2 (C10–C18) |
| ৫ | Part 2B Framework-এর ভেতরে + Part 2C Jetpack আর basics |
| ৬ | Part 3 Compose আর UI |
| ৭ | Part 5 Architecture, data, testing + Part 6 |
| ৮ | **Revision ১:** Day 1–7-এর সব ★ মুখে + একটা ছোট app বানান |
| ৯ | Part 7 Security |
| ১০ | Part 8 Camera আর video |
| ১১ | Part 9 AOSP |
| ১২ | Part 10 Sensor + Part 4 Performance |
| ১৩ | Part 11 Design + Part 12 Coding |
| ১৪ | Part 13 Behavioral + **Mock interview ১** |
| ১৫ | দুর্বল প্রশ্নগুলো আবার + **Mock interview ২** + [শেষ দিনের checklist](#last-day) |

## <a id="mock"></a>Mock interview কীভাবে করবেন

একজন বন্ধু বা পরিবারের কাউকে বসান। না পেলে প্রশ্নগুলো নিজের গলায় record করে চালান। ৪৫ মিনিট:

1. ৫ মিনিট — Tell me about yourself + Why Android
2. ১৫ মিনিট — যেকোনো ভাগ থেকে ৮টা random ★ প্রশ্ন (Kotlin, lifecycle, Compose, security)
3. ১০ মিনিট — একটা domain প্রশ্ন (camera বা AOSP বা sensor)
4. ১০ মিনিট — একটা system design (D1)
5. ৫ মিনিট — "Do you have any questions for us?"

পুরোটা record করুন। পরে শুনে তিনটা জিনিস লিখুন: কোথায় আটকালেন, কোন শব্দ খুঁজে পাননি, কোথায় খুব লম্বা বললেন।

---

## <a id="toc"></a>সূচিপত্র


**[Part 0 — শুরুর প্রশ্ন: নিজের পরিচয় আর কেন Android](#part-0)**

- [H0-1. ★ Tell me about yourself.](#h0-1)
- [H0-2. ★ Why do you want to move to native Android?](#h0-2)
- [H0-3. ★ Why should we hire you over a pure native Android developer?](#h0-3)
- [H0-4. ★ What do you know about our product / domain?](#h0-4)
- [H0-5. ◆ Client questions (freelance / contract / foreign client)](#h0-5)
- [H0-6. ★ What are your strengths and weaknesses?](#h0-6)

**[Part 1 — Kotlin, Coroutines আর Flow](#part-1)**

- [K1. ★ Why do Android teams use Kotlin and not Java? How does null safety work?](#k1)
- [K2. ★ What is the difference between val, var and const val? And lateinit vs by lazy?](#k2)
- [K3. ★ data class, sealed class / sealed interface, enum class, object and companion object — when do you use each?](#k3)
- [K4. ★ What are extension functions and scope functions (let, apply, run, also, with)?](#k4)
- [K5. ◆ Explain higher-order functions, lambdas, inline, noinline, crossinline and reified.](#k5)
- [K6. ○ Explain generics in Kotlin: in / out (variance) and star projection.](#k6)
- [K7. ◆ What is the difference between List and MutableList? And Collections vs Sequences?](#k7)
- [K27. ★ What is the difference between an interface and an abstract class in Kotlin? Why are classes final by default, and what do the visibility modifiers mean?](#k27)
- [K28. ◆ Where do you put helpers and constants: an object, a companion object, or top-level functions?](#k28)
- [K8. ★ What is a coroutine? How is it different from a thread? What does suspend mean?](#k8)
- [K9. ★ Explain Dispatchers (Main, IO, Default) and withContext. What is main-safety?](#k9)
- [K10. ★ What is the difference between launch and async? What are Job and Deferred?](#k10)
- [K11. ★ Explain structured concurrency: scopes, cancellation, SupervisorJob and exception handling.](#k11)
- [K12. ★ What is a cold Flow vs a hot Flow? Why do we use Flow and not LiveData now?](#k12)
- [K13. ★ What is the difference between StateFlow and SharedFlow? Explain stateIn / shareIn with SharingStarted.WhileSubscribed(5000).](#k13)
- [K14. ★ Which Flow operators do you use most? How do you collect a Flow safely in the UI?](#k14)
- [K15. ◆ What is the difference between Channels and Flow? How do you handle one-time UI events like navigation or a snackbar?](#k15)
- [K16. ◆ How do you make code thread-safe in Kotlin? Mutex, atomic types, @Volatile, synchronized, and a confined dispatcher.](#k16)
- [K17. ◆ Show how you build search-as-you-type with debounce and flatMapLatest, and explain it.](#k17)

**[Part 1B — Kotlin আরও গভীরে](#part-1b)**

- [K18. ★ How does a suspend function work inside?](#k18)
- [K19. ★ How do you turn a listener API into a Flow with callbackFlow?](#k19)
- [K20. ◆ How does delegation with `by` work in Kotlin?](#k20)
- [K21. ◆ What is a value class, and when does it help?](#k21)
- [K22. ★ Explain equality and data classes in Kotlin.](#k22)
- [K23. ◆ What do you need to know about Kotlin–Java interop?](#k23)
- [K24. ★ How do you model state and errors with sealed types?](#k24)
- [K25. ★ What is new in Kotlin 2.x?](#k25)
- [K26. ○ How do you test and debug coroutines?](#k26)

**[Part 2 — Android-এর মূল জিনিস: component, lifecycle, permission, background কাজ](#part-2)**

- [C1. ★ What are the four main Android components?](#c1)
- [C2. ★ Can you explain the Activity lifecycle?](#c2)
- [C3. ★ What is special about the Fragment lifecycle, and why do we use viewLifecycleOwner?](#c3)
- [C19. ★ How do Fragments (or screens) talk to each other? Why not use direct references?](#c19)
- [C4. ★ What is the difference between a configuration change and process death? How do you keep state?](#c4)
- [C5. ★ What is the difference between explicit and implicit intents? What is a PendingIntent?](#c5)
- [C6. ◆ What are tasks and launch modes?](#c6)
- [C7. ★ What types of Services are there? What are foreground service types?](#c7)
- [C8. ◆ How do BroadcastReceivers work today?](#c8)
- [C9. ◆ What is a ContentProvider, and why do we need FileProvider?](#c9)
- [C10. ★ Which tool do you use for background work?](#c10)
- [C11. ★ What is Context? How do Context leaks happen?](#c11)
- [C12. ★ How does the main thread work (Looper, Handler, MessageQueue)? What is an ANR?](#c12)
- [C13. ★ How do runtime permissions work?](#c13)
- [C14. ◆ What are the AndroidManifest essentials?](#c14)
- [C15. ★ How do notifications and push messages work on modern Android?](#c15)
- [C16. ◆ What is the difference between deep links and Android App Links?](#c16)
- [C17. ◆ How does storage work on modern Android?](#c17)
- [C18. ◆ How does an app process start, and how does Android decide which process to kill?](#c18)

**[Part 2B — Android framework-এর ভেতরে (internals)](#part-2b)**

- [F1. ★ What happens when you tap an app icon?](#f1)
- [F2. ★ How does ART run your code? (DEX, JIT, AOT, Baseline Profiles)](#f2)
- [F3. ★ What is Binder, and why does Android use it?](#f3)
- [F4. ★ Parcelable vs Serializable — which and why?](#f4)
- [F5. ★ How is a frame drawn on Android, and where does jank come from?](#f5)
- [F6. ◆ What are Window, Surface, and SurfaceView vs TextureView?](#f6)
- [F7. ◆ How does Intent resolution work?](#f7)
- [F8. ◆ How are runtime permissions enforced?](#f8)
- [F9. ◆ How does memory work for an Android app?](#f9)
- [F10. ◆ What threads does an Android app have?](#f10)
- [F11. ★ How do system services work? (getSystemService to the HAL)](#f11)
- [F12. ★ What is new in Android development in 2025–2026?](#f12)
- [F13. ○ What does the Android platform security model look like?](#f13)

**[Part 2C — Jetpack আর Android-এর basics](#part-2c)**

- [J1. ★ What is Android Jetpack / AndroidX? Why use it instead of only framework APIs?](#j1)
- [J2. ★ Walk me through an Android project structure.](#j2)
- [J3. ★ What is the Application class? When do you use it, and what should not go there?](#j3)
- [J4. ★ How do lifecycle-aware components work? (Lifecycle, LifecycleOwner, DefaultLifecycleObserver, ProcessLifecycleOwner)](#j4)
- [J5. ★ How do you support old Android versions? (AppCompat, Compat classes, SDK_INT, @RequiresApi)](#j5)
- [J6. ◆ What are the basics of the View system? (View vs ViewGroup, layouts, ViewBinding, custom views)](#j6)
- [J7. ◆ How do resources and configuration qualifiers work?](#j7)
- [J8. ◆ Toast vs Snackbar vs Dialog vs notification — when do you use each?](#j8)
- [J9. ◆ What is the Activity Result API, and why did it replace startActivityForResult?](#j9)
- [J10. ◆ How do you use the App Startup library and the SplashScreen API?](#j10)
- [J11. ★ Which Jetpack libraries do you use in a new app today, and why?](#j11)
- [J12. ◆ Which Android Studio tools do you use every day?](#j12)
- [J13. ○ How do you build home screen widgets with Glance, and Quick Settings tiles?](#j13)

**[Part 3 — Jetpack Compose আর UI](#part-3)**

- [U1. ★ What is Jetpack Compose, and why do teams move from XML Views to it?](#u1)
- [U2. ★ What is recomposition? How does Compose skip work, and what is stability?](#u2)
- [U3. ★ How do you handle state in Compose? (`remember`, `rememberSaveable`, state hoisting)](#u3)
- [U4. ★ What are side effects in Compose? When do you use each effect API?](#u4)
- [U5. ◆ What are `derivedStateOf` and `snapshotFlow`?](#u5)
- [U6. ★ How do you make a `LazyColumn` fast?](#u6)
- [U7. ◆ Why does Modifier order matter?](#u7)
- [U8. ★ How does navigation work in Compose?](#u8)
- [U9. ★ How do you connect Compose with a ViewModel?](#u9)
- [U10. ◆ How do you mix Compose and Views? (e.g. a video player or camera preview)](#u10)
- [U11. ◆ How do you find and fix Compose performance problems?](#u11)
- [U12. ○ How do you do theming in Compose? (Material 3, dynamic color, dark mode)](#u12)
- [U13. ★ What is edge-to-edge, how do you handle window insets, and what is predictive back?](#u13)
- [U14. ◆ How do you support large screens and foldables?](#u14)
- [U16. ★ dp vs sp vs px — how do you support different screen sizes and densities?](#u16)
- [U17. ◆ How do you make an app accessible, and how do you test it?](#u17)
- [U18. ◆ How do you localize an Android app? (strings, plurals, RTL, per-app language)](#u18)
- [U15. ◆ How do RecyclerView, ViewHolder and DiffUtil work? How does a View measure, lay out and draw?](#u15)

**[Part 4 — Performance, debugging আর release](#part-4)**

- [P1. ★ What is an ANR? What causes it, and how do you find and fix it?](#p1)
- [P2. ★ What causes memory leaks on Android, and how do you find them?](#p2)
- [P3. ★ How do you make app startup faster?](#p3)
- [P4. ◆ How do you find and fix jank and frame drops?](#p4)
- [P5. ★ What does R8 do? How do keep rules and mapping files work?](#p5)
- [P6. ★ APK vs AAB? How does Play App Signing work, and what if you lose the upload key?](#p6)
- [P7. ◆ How do you save battery? (Doze, wake locks, standby buckets)](#p7)
- [P8. ★ How do you monitor crashes and ANRs in production?](#p8)
- [P9. ◆ How do you set up CI/CD for an Android app?](#p9)
- [P10. ★ How do you debug a production bug you cannot reproduce?](#p10)
- [P11. ★ What changed in recent Android versions (8 to 17)? What do minSdk, targetSdk and compileSdk mean?](#p11)
- [P12. ◆ Explain Gradle basics: build types, flavors, version catalogs, KSP vs kapt, and build speed.](#p12)
- [P13. ◆ Which static analysis tools do you use? (Android Lint, detekt, ktlint)](#p13)

**[Part 5 — Architecture, data, network আর testing](#part-5)**

- [R1. ★ What goes in a ViewModel, and why does it survive screen rotation?](#r1)
- [R2. ★ What is MVI or unidirectional data flow? MVVM or MVI — which do you choose?](#r2)
- [R3. ★ Explain Clean Architecture layers. When is a use case class worth it?](#r3)
- [R4. ★ Explain the Repository pattern, single source of truth, and offline-first.](#r4)
- [R5. ★ How does dependency injection work with Hilt?](#r5)
- [R6. ◆ How do you split an app into modules?](#r6)
- [R7. ★ Explain Room: entities, DAOs, Flow queries, relations, transactions and migrations.](#r7)
- [R8. ★ DataStore or SharedPreferences? Preferences or Proto DataStore?](#r8)
- [R9. ★ How do you set up Retrofit and OkHttp? How do you refresh an expired token?](#r9)
- [R10. ★ How do you handle errors from the network to the UI?](#r10)
- [R19. ◆ How do you cache data and decide when it is stale?](#r19)
- [R11. ◆ How does Paging 3 work? When do you need RemoteMediator?](#r11)
- [R12. ◆ Coil or Glide? How do you avoid out-of-memory with images?](#r12)
- [R13. ◆ kotlinx.serialization, Moshi or Gson — which do you use?](#r13)
- [R14. ★ How do you unit test a ViewModel?](#r14)
- [R15. ◆ How do you write UI and integration tests? What is your test pyramid?](#r15)
- [R16. ◆ WebSocket, Server-Sent Events, MQTT or FCM — when do you use each?](#r16)
- [R17. ○ Which design patterns do you use in Android? Why are singletons dangerous?](#r17)
- [R18. ◆ Explain SOLID with Android examples.](#r18)
- [R20. ◆ Feature flags and remote config — how do you ship a feature safely?](#r20)

**[Part 6 — Flutter থেকে native Android: সেতুর প্রশ্ন](#part-6)**

- [B1. ★ You are a Flutter developer. Why should we trust you with native Android work?](#b1)
- [B2. ★ Flutter or native Android — when do you choose native?](#b2)
- [B3. ★ How do platform channels work? How would you stream sensor data to Flutter?](#b3)
- [B4. ◆ What are FFI, NDK and JNI? When would you write C or C++?](#b4)
- [B5. ◆ How do you add Flutter screens to an existing native Android app?](#b5)
- [B6. ◆ Kotlin Multiplatform or Flutter — an honest comparison.](#b6)
- [B7. ◆ Map Flutter concepts to Android. How did you ramp up on native Android?](#b7)

**[Part 7 — Security: কয়েক স্তরের নিরাপত্তা (multi-layer security)](#part-7)**

- [S1. ★ How do you secure an Android app?](#s1)
- [S17. ◆ What are the OWASP Mobile Top 10 risks?](#s17)
- [S2. ★ Where do you store tokens and secrets?](#s2)
- [S3. ◆ Can you explain the Android Keystore in depth?](#s3)
- [S4. ★ How do you build biometric login?](#s4)
- [S5. ★ How do you secure network traffic?](#s5)
- [S6. ★ How do you build login and auth securely?](#s6)
- [S7. ★ How do you detect root, tampering and emulators?](#s7)
- [S8. ◆ What can an attacker see in your APK?](#s8)
- [S9. ★ How do you secure app components?](#s9)
- [S10. ◆ How do you make a WebView safe?](#s10)
- [S11. ★ How do you protect data at rest and stop data leaks?](#s11)
- [S12. ◆ How do you secure IPC between your own apps or a system service?](#s12)
- [S13. ◆ What do you know about Android Enterprise and device management?](#s13)
- [S14. ◆ How do you test the security of an app?](#s14)
- [S15. ◆ How do you handle session security?](#s15)
- [S16. ○ How do you protect the software supply chain?](#s16)

**[Part 8 — Security camera, video আর streaming](#part-8)**

- [V1. ★ CameraX or Camera2 — when do you use each?](#v1)
- [V2. ★ What are the rules for camera permissions and background camera use?](#v2)
- [V3. ★ How do you play a live stream from an IP camera?](#v3)
- [V4. ★ How do you show many camera feeds at once?](#v4)
- [V14. ◆ How do you take a snapshot or thumbnail from a live stream or video?](#v14)
- [V5. ★ How do you record video on the device?](#v5)
- [V6. ◆ Can you explain video encoding basics?](#v6)
- [V7. ◆ How do you find cameras on the local network?](#v7)
- [V8. ◆ How do you do motion detection and AI on the device?](#v8)
- [V9. ★ How do you send motion alert notifications?](#v9)
- [V10. ★ How do you secure camera streams and recordings?](#v10)
- [V11. ◆ How do you build a 24/7 monitoring or recording app?](#v11)
- [V12. ○ How do you build two-way audio?](#v12)
- [V13. ◆ How do you handle a bad network during streaming?](#v13)

**[Part 9 — Custom Android OS (AOSP) আর platform](#part-9)**

- [O1. ★ What is AOSP, and how is it different from the Android on a Pixel or Samsung phone?](#o1)
- [O2. ★ Can you explain the Android platform layers, and how a call goes from an app to the hardware?](#o2)
- [O3. ★ How do you build AOSP and flash it on a device?](#o3)
- [O4. ★ What is the difference between a normal app, a system app, a privileged app and a platform-signed app?](#o4)
- [O5. ◆ How would you add a new system service or customise the framework?](#o5)
- [O6. ◆ What is a HAL, and what did Project Treble change? AIDL HAL vs HIDL?](#o6)
- [O7. ★ How does SELinux work on Android, and how do you fix an "avc: denied" error?](#o7)
- [O8. ◆ Can you explain the Android boot process? Where would you add custom startup?](#o8)
- [O9. ★ How do you build a kiosk or dedicated device? Can you do it without a custom ROM?](#o9)
- [O10. ★ How do you deliver OTA updates to your own devices?](#o10)
- [O11. ◆ What is verified boot (AVB) and why must test-keys never ship?](#o11)
- [O12. ★ How do you debug problems at the platform level?](#o12)
- [O16. ◆ What is ADB, and which ADB commands do you use most?](#o16)
- [O13. ◆ How would an app talk to custom hardware on your device?](#o13)
- [O14. ○ What are CTS, VTS and GMS certification? What changes if your device has no Google services?](#o14)
- [O15. ○ What is Android developer verification, and does it affect apps on your custom devices?](#o15)

**[Part 10 — Sensor, location, Bluetooth আর IoT](#part-10)**

- [N1. ★ How do you read sensor data on Android?](#n1)
- [N2. ★ What is the difference between accelerometer, gyroscope and magnetometer? How do you get device orientation?](#n2)
- [N3. ★ How do you use sensors without killing the battery?](#n3)
- [N4. ★ How do you read sensors in the background? What limits does Android have?](#n4)
- [N5. ◆ How do you handle noisy sensor data?](#n5)
- [N6. ◆ What is the difference between the step counter and the step detector? Where do Activity Recognition and Health Connect fit?](#n6)
- [N7. ★ How do you get location on Android?](#n7)
- [N8. ★ How do you work with Bluetooth Low Energy devices on Android?](#n8)
- [N9. ◆ What is Companion Device Manager and why use it?](#n9)
- [N10. ◆ How do you talk to USB and serial devices from an Android app?](#n10)
- [N13. ○ How does NFC work on Android? Reading tags and Host Card Emulation](#n13)
- [N11. ◆ Which IoT protocol would you choose — MQTT, CoAP or HTTP/WebSocket? How do you keep MQTT alive on Android?](#n11)
- [N12. ◆ How do you test sensor and hardware code?](#n12)

**[Part 11 — Mobile system design](#part-11)**

- [D1. ★ Design a security camera app](#d1)
- [D2. ★ Design an offline-first app that syncs with a server](#d2)
- [D3. ◆ Design a chat or real-time messaging feature](#d3)
- [D7. ◆ Design an image feed / gallery with caching and pagination](#d7)
- [D4. ◆ Design software for a fleet of custom Android devices](#d4)
- [D5. ◆ Design a large video/photo upload that survives app kill and bad network](#d5)
- [D6. ◆ Design a sensor data logger](#d6)

**[Part 12 — Live coding round](#part-12)**

- [L1. ★ Warm-up: reverse words, check palindrome, count characters](#l1)
- [L2. ★ Two Sum with a HashMap](#l2)
- [L3. ★ Valid parentheses with a stack](#l3)
- [L4. ◆ LRU cache](#l4)
- [L5. ★ Debounced search in a ViewModel with Flow](#l5)
- [L6. ★ Fetch a list from an API and show loading / data / error in Compose](#l6)
- [L7. ◆ Run 3 network calls in parallel and combine; cancel all if one fails](#l7)
- [L11. ◆ Implement a simple retry with exponential backoff in Kotlin](#l11)
- [L8. ◆ Find the bug in Android code](#l8)
- [L9. ○ Thread-safe in-memory cache with Mutex](#l9)
- [L10. ○ Merge intervals (and group anagrams)](#l10)

**[Part 13 — Behavioral, teamwork আর client-এর প্রশ্ন](#part-13)**

- [H1. ★ Tell me about a difficult bug you fixed.](#h1)
- [H2. ★ Tell me about a time you missed a deadline or were under pressure.](#h2)
- [H3. ★ Tell me about a disagreement with a teammate or lead.](#h3)
- [H4. ★ Tell me about a mistake you made.](#h4)
- [H5. ★ How do you work with designers, QA and backend developers?](#h5)
- [H6. ◆ How do you review code? How do you take review comments?](#h6)
- [H7. ◆ How do you learn new things and stay up to date?](#h7)
- [H8. ◆ Have you mentored or helped a junior developer?](#h8)
- [H13. ◆ How do you work in Agile / Scrum? (sprints, standups, estimates, demos)](#h13)
- [H14. ◆ Tell me about a time you had to learn something new very fast.](#h14)
- [H15. ◆ How do you work in a remote team? How do you communicate across time zones?](#h15)
- [H9. ★ Why are you leaving your current job?](#h9)
- [H10. ◆ Where do you see yourself in 3–5 years?](#h10)
- [H11. ★ Salary, notice period and availability](#h11)
- [H12. ★ Do you have any questions for us?](#h12)

---

## <a id="speak-english"></a>English-এ আত্মবিশ্বাসের সাথে বলার কৌশল

### সব উত্তরের জন্য একটা format

প্রতিটা technical উত্তর এই ৪ ধাপে বলুন। Format ঠিক থাকলে English-এ শব্দ খুঁজতে কম কষ্ট হয়।

| ধাপ | কী বলবেন | শুরুর বাক্য |
|---|---|---|
| ১. সরাসরি উত্তর | এক বাক্যে মূল কথা | "In short, ..." / "The main idea is ..." |
| ২. কীভাবে / কেন | ১–২ বাক্যে কারণ | "It works like this: ..." / "The reason is ..." |
| ৩. Trade-off বা ফাঁদ | একটা "কিন্তু" | "One thing to watch is ..." / "The trade-off is ..." |
| ৪. বাস্তব কাজ | আপনি কীভাবে করেন | "In my code, I usually ..." / "My default is ..." |

তারপর **থামুন**। Interviewer আরও চাইলে জিজ্ঞেস করবে। লম্বা উত্তর মানে বেশি জানা না। পরিষ্কার উত্তরই senior-এর চিহ্ন।

### সহজ English-এর নিয়ম

- **ছোট বাক্য।** একটা বাক্যে একটা কথা। "and... and... and..." দিয়ে লম্বা করবেন না।
- **ধীরে বলুন।** দ্রুত বললে ভুল বেশি হয়। ধীরে বললে confident শোনায়।
- **কঠিন শব্দ লাগবে না।** "use", "keep", "stop", "start", "save", "check" — এগুলোই যথেষ্ট। Technical শব্দ (ViewModel, Keystore) ঠিকভাবে বললেই হবে।
- **ভুল হলে নিজেই ঠিক করুন।** "Sorry, let me say that again." — এটা একদম স্বাভাবিক।
- **Present tense-এ বলুন।** "I use Hilt" — "I have been using" বলার দরকার নেই।

### যে বাক্যগুলো আপনাকে বাঁচাবে

**প্রশ্ন বুঝতে না পারলে:**
- "Sorry, could you repeat the question, please?"
- "Do you mean ... or ...?"
- "Just to be sure — you are asking about ..., right?"

**ভাবার সময় নিতে:**
- "Good point. Let me think for a second."
- "Let me start with the big picture."
- "There are two parts to this. First, ..."

**না জানলে (সৎ থাকুন, কিন্তু থেমে যাবেন না):**
- "I have not used that in production. But I know the idea: ..."
- "I am not 100% sure about the exact API name. The approach I would take is ..."
- "I would check the official docs for the latest detail, but my understanding is ..."

**অভিজ্ঞতা নিয়ে সৎ থাকা (Flutter থেকে এলে):**
- "My main work in the last few years was Flutter. But Flutter on Android runs on the same platform, so I work with Android every day — Gradle, manifest, permissions, native plugins in Kotlin."
- "I did native Android before Flutter, and I have refreshed it with Kotlin, coroutines and Compose."

> **সৎ থাকুন:** উত্তরগুলোতে "I use ...", "My approach is ..." আছে। যেটা আপনি নিজে করেননি, সেটা নিজের project-এর গল্প বানিয়ে বলবেন না। অভিজ্ঞ interviewer দুইটা follow-up দিয়েই ধরে ফেলে। তখন "I would do it this way" বলুন। এটাও সমান smart শোনায়।

### উচ্চারণ — যে শব্দগুলো ভুল হয়

| শব্দ | যেভাবে বলবেন |
|---|---|
| Kotlin | **কট**-লিন |
| coroutine | কো-রু-**টিন** |
| Gradle | **গ্রে**-ডল |
| cache | ক্যাশ (ক্যাশে না) |
| queue | কিউ |
| suite (test suite) | সুইট |
| Zygote | **জাই**-গোট |
| SELinux | এস-ই-**লি**-নাক্স |
| AOSP | এ-ও-এস-পি |
| GATT | গ্যাট |
| MQTT | এম-কিউ-টি-টি |
| ONVIF | **অন**-ভিফ |
| H.264 / H.265 | এইচ-টু-সিক্স-ফোর / এইচ-টু-সিক্স-ফাইভ |
| RTSP | আর-টি-এস-পি |
| Keystore | **কি**-স্টোর |
| idempotent | আই-ডেম-**পো**-টেন্ট |
| asynchronous | এ-**সিং**-ক্রো-নাস |
| Binder | **বাইন**-ডার (বিন্ডার না) |
| width / height | উইডথ / হাইট |

---


## <a id="part-0"></a>Part 0 — শুরুর প্রশ্ন: নিজের পরিচয় আর কেন Android

### আগে বুঝুন — প্রথম ৫ মিনিট কেন এত জরুরি

Interview-এর প্রথম ৫ মিনিটে interviewer আপনার সম্পর্কে একটা ধারণা করে ফেলে। আপনি যদি Flutter বা অন্য cross-platform থেকে আসেন, তার মনে একটা প্রশ্ন থাকবে: "native Android-এ কতটা পারবে?" এই সন্দেহ শুরুতেই দূর করতে হবে।

কী করবেন:

1. **নিজেকে "mobile engineer" বলুন, শুধু "Flutter developer" না।** আপনার অভিজ্ঞতা মোবাইলে। Flutter একটা tool মাত্র।
2. **Android-এর সাথে আপনার সত্যিকারের যোগ বলুন।** Flutter app-ও Android-এ চলে। Gradle, manifest, permission, signing, Play Console, native plugin, platform channel — এগুলো আপনি নিয়মিত সামলান। আগে native Android করে থাকলে সেটাও বলুন।
3. **আপডেট থাকার প্রমাণ দিন।** Kotlin coroutines, Flow, Compose, Hilt, Android 15–17-এর পরিবর্তন — এগুলোর নাম স্বাভাবিকভাবে বলুন।
4. **তাদের domain-এর সাথে যোগ করুন।** Camera, sensor, security — আপনি কী জানেন আর কী শিখতে আগ্রহী।

উত্তরে **[...]** অংশে নিজের সত্যি তথ্য বসান। নিচের উত্তরগুলো Flutter থেকে আসা কারো জন্য লেখা। আপনার পথ অন্য হলে সেভাবে বদলে নিন।

---

### <a id="h0-1"></a>H0-1. ★ Tell me about yourself.

**প্রশ্নটা মানে:** ৬০–৯০ সেকেন্ডে আপনার কাজের গল্প। জীবনী না।
**অন্যভাবেও জিজ্ঞেস করে:** "Walk me through your background." · "Can you introduce yourself?"

**বুঝে নিন:**
- ক্রম: এখন কী করেন → মোট অভিজ্ঞতা → Android-এর সাথে যোগ → বড় কাজের ১–২টা উদাহরণ → কেন এই job।
- পড়াশোনা, শখ — শুধু জিজ্ঞেস করলে।
- শেষে এমন একটা কথা রাখুন, যেটা নিয়ে interviewer প্রশ্ন করতে চাইবে। যেমন একটা কঠিন bug বা একটা native module।

**Answer (English):**
> "I am a mobile engineer with about [8] years of experience. For the last few years my main stack was Flutter, but I started with native Android, and Android is still a big part of my daily work. In Flutter apps I handle the Android side myself — Gradle setup, the manifest, permissions, signing, Play Store releases, and native code in Kotlin through platform channels. For example, [I wrote a native Kotlin plugin for ...]. Recently I refreshed my native skills with Kotlin coroutines, Flow, Jetpack Compose and Hilt. I like work that is close to the device — camera, sensors, security. That is why this role is interesting to me."

**Key words:** `mobile engineer` · `Android side` · `Kotlin` · `platform channels` · `Compose`

**Follow-up:**
- **Q:** What was your last native Android work?
  **A:** "[Be honest.] In my Flutter projects I wrote native Kotlin code for [...]. Before Flutter, I built full native apps with [...]. Last week I also built a small Compose sample with Hilt, Room and Retrofit to refresh the latest APIs."
- **Q:** How would you rate your Android skills from 1 to 10?
  **A:** "I would say [7]. I am strong on the core platform — lifecycle, background work, permissions, release. I am still building more daily experience with the newest Compose APIs, and I learn fast because the platform basics are the same."

**ভুল করবেন না:** "I am only a Flutter developer" বা "I forgot Android" বলবেন না। সত্যি বলুন, কিন্তু শক্তির দিক থেকে বলুন।

**আরও দেখুন:** [H0-2 · Why native Android](#h0-2) · [B1 · Flutter dev for native work](#b1) · [H0-6 · Strengths and weaknesses](#h0-6)

---

### <a id="h0-2"></a>H0-2. ★ Why do you want to move to native Android?

**প্রশ্নটা মানে:** আপনি কি Flutter ছেড়ে সত্যিই native করতে চান, নাকি শুধু job-এর জন্য?
**অন্যভাবেও জিজ্ঞেস করে:** "Why native and not Flutter?" · "Will you be happy working only on Android?"

**বুঝে নিন:**
- Flutter-কে খারাপ বলবেন না। দুটোই tool।
- আসল কারণ বলুন: device-এর কাছাকাছি কাজ (camera, sensor, OS), performance, platform-এর গভীরে যাওয়া।
- দেখান যে Flutter-এর অভিজ্ঞতা এখানে কাজে লাগবে: architecture, testing, release, UI-এর declarative চিন্তা (Compose-ও declarative)।

**Answer (English):**
> "Flutter is a great tool, and I still like it. But my favourite part of the work was always the native side — camera, sensors, background work, and security. In native Android I can go deeper into the platform and get full control. Also, many skills move over directly. Compose is declarative like Flutter, and architecture, testing and release work are the same ideas. So for me this is a natural next step, not a restart."

**Key words:** `close to the device` · `full control` · `declarative` · `natural next step`

**Follow-up:**
- **Q:** Will you miss Flutter?
  **A:** "Maybe a little. But I can still help if the team ever shares code with Flutter or KMP. My focus here will be native Android."

**আরও দেখুন:** [B2 · Flutter or native](#b2) · [B1 · Flutter dev for native work](#b1) · [H9 · Why leaving](#h9)

---

### <a id="h0-3"></a>H0-3. ★ Why should we hire you over a pure native Android developer?

**প্রশ্নটা মানে:** আপনার বাড়তি মূল্য কী?
**অন্যভাবেও জিজ্ঞেস করে:** "What makes you different?" · "What do you bring to the team?"

**বুঝে নিন:**
- তিনটা জিনিস বলুন: (১) মোবাইলে লম্বা অভিজ্ঞতা — release, crash, user, store, (২) cross-platform দৃষ্টি — iOS-এর দিকটাও বোঝেন, (৩) দ্রুত শেখার প্রমাণ।
- বড়াই করবেন না। শান্তভাবে বলুন।

**Answer (English):**
> "I bring three things. First, many years of shipping real mobile apps — releases, crash fixing, store reviews, and working with users. Second, I see the whole mobile picture, Android and iOS, so I can talk well with other teams and the backend. Third, I learn fast. I came back to native Android and picked up the modern stack quickly. I think a team gets a developer who can ship from day one and also think about the product."

**Key words:** `shipping` · `whole mobile picture` · `ship from day one`

**Follow-up:**
- **Q:** What is your weakest area in Android right now?
  **A:** "Daily speed with some newer Compose APIs. I know the concepts well, and I close the gap by building small samples and reading the official docs. In a few weeks of real work it will be normal."

**আরও দেখুন:** [B1 · Flutter dev for native work](#b1) · [H0-6 · Strengths and weaknesses](#h0-6) · [B7 · Flutter to Android map](#b7)

---

### <a id="h0-4"></a>H0-4. ★ What do you know about our product / domain?

**প্রশ্নটা মানে:** আপনি কি homework করে এসেছেন?
**অন্যভাবেও জিজ্ঞেস করে:** "Why our company?" · "Have you used our app?"

**বুঝে নিন:**
- Interview-এর আগে তাদের app install করুন। Play Store-এর review পড়ুন। Website দেখুন।
- একটা ভালো দিক বলুন। আর একটা ছোট জিনিস, যেটা আরও ভালো করা যায়। নরম ভাষায়।
- তাদের domain (camera, custom device, sensor) থেকে এক লাইনে বলুন কোন technical জিনিসটা আপনার ভালো লাগে।

**Answer (English):**
> "I installed your app and read about your products. You work with [security cameras / custom Android devices / sensors], so the app has to be fast, stable and secure, because people trust it with their home or business. I liked [one real thing]. I also noticed [one small thing, said softly], and I have some ideas there. This kind of work — live video, device connection and strong security — is exactly what I want to do."

**Key words:** `fast, stable and secure` · `trust` · `live video`

**Follow-up:**
- **Q:** What would you improve first?
  **A:** "I would first look at the data — crash rate, ANR rate, and the most common user complaints. Then I would pick the problem that hurts most users. I would not change things only by my opinion."

**আরও দেখুন:** [D1 · Security camera app](#d1) · [P8 · Crash and ANR monitoring](#p8) · [H12 · Questions for us](#h12)

---

### <a id="h0-5"></a>H0-5. ◆ Client questions (freelance / contract / foreign client)

**প্রশ্নটা মানে:** Client আপনার technical skill-এর সাথে সাথে দেখে — আপনার সাথে কাজ করা সহজ কি না, ভরসা করা যায় কি না।
**অন্যভাবেও জিজ্ঞেস করে:** নিচের table-এ প্রশ্নগুলো।

**বুঝে নিন:** Client-এর সবচেয়ে বড় ভয় তিনটা: কাজ সময়ে হবে না, যোগাযোগ বন্ধ হয়ে যাবে, code-এর মান খারাপ হবে। প্রতিটা উত্তরে এই ভয় দূর করুন — নিয়মিত update, স্পষ্ট estimate, test আর review।

| প্রশ্ন | ছোট উত্তর (English) |
|---|---|
| How do you keep me updated? | "I send a short update every day: what I did, what is next, and any blockers. I also share a test build every week, so you can see real progress." |
| What are your working hours? How much overlap with our time zone? | "I am in [Bangladesh, GMT+6]. I can keep [3–4] hours of overlap with your team every day for calls and quick questions." |
| How do you estimate a task? | "I split the work into small tasks, estimate each one, and add a buffer for unknowns. If I find a risk, I tell you early, not at the deadline." |
| What if requirements are not clear? | "I ask questions first and write down my understanding. Then I confirm it with you before I build. This saves time for both of us." |
| How do you make sure the code quality is good? | "I write unit tests for the logic, use code review, keep a clean architecture, and run lint and CI on every pull request." |
| How do you handle our source code and secrets? | "I keep everything in your repository and your accounts. I never put keys in the code or in public places. I am happy to sign an NDA, and I follow your security rules." |
| Can you work with our hardware / device? | "Yes. If you can ship me a test device, I can work directly on it. If not, I can start with mocks and the emulator, and then test on the device with your team." |
| What if you get stuck? | "I first try for a fixed time, then I ask. I share what I tried, so the other person can help quickly." |
| Can you start with a small paid task? | "Yes, that is a good idea. It helps both of us check the fit." |

**আরও দেখুন:** [H15 · Remote work](#h15) · [H13 · Agile / Scrum](#h13) · [H2 · Deadline pressure](#h2)

---

### <a id="h0-6"></a>H0-6. ★ What are your strengths and weaknesses?

**প্রশ্নটা মানে:** আপনি নিজেকে সৎভাবে চেনেন কি না। আর দুর্বলতা নিয়ে কাজ করছেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "What is your biggest strength?" · "What is one area you want to improve?"

**বুঝে নিন:**
- Strength: এই job-এর সাথে মেলে এমন ১–২টা বলুন। সাথে একটা ছোট প্রমাণ দিন।
- Weakness: সত্যি হতে হবে। কিন্তু job-এর মূল skill না।
- Weakness বলার পর থামবেন না। বলুন সেটা ঠিক করতে এখন কী করছেন।
- "I am a perfectionist" ধরনের ফাঁকা উত্তর দেবেন না। Interviewer এটা বহুবার শুনেছে।
- ভালো weakness-এর উদাহরণ: সব কাজ নিজে করে ফেলা, সাহায্য চাইতে দেরি করা, বড় meeting-এ কম কথা বলা। Flutter থেকে এলে: কিছু নতুন native API-তে daily speed ([H0-3](#h0-3)-এর follow-up দেখুন)।

**Answer (English):**
> "My main strength is that I own problems end to end. When a crash shows up in production, I find the root cause, fix it, and add a test, so it does not come back. I am also good at explaining technical things to designers and product people. One weakness: sometimes I try to solve everything myself and ask for help too late. I am working on it. Now I give myself a time limit. If I am still stuck after that, I ask. It saves time for the whole team."

**Key words:** `end to end` · `root cause` · `working on it` · `time limit`

**Follow-up:**
- **Q:** What would your last manager say about you?
  **A:** "I think they would say I am reliable and I finish what I start. They might also say I should share my progress more often. I improved that with short daily updates."
- **Q:** Why should we see that weakness as a small risk?
  **A:** "Because I already have a simple rule for it, the time limit, and it works. It does not affect the quality of my work, only how fast I ask."

**ভুল করবেন না:** এমন weakness বলবেন না যেটা job-এর মূল skill-কে আঘাত করে (যেমন "I am weak in Kotlin")।

**আরও দেখুন:** [H0-3 · What you bring](#h0-3) · [H4 · A mistake you made](#h4) · [H0-1 · Tell me about yourself](#h0-1)

---


## <a id="part-1"></a>Part 1 — Kotlin, Coroutines আর Flow

Android interview প্রায় সবসময় Kotlin দিয়ে শুরু হয়। এখানে দুর্বল হলে interviewer ধরে নেয় বাকি সবও দুর্বল।
Coroutines আর Flow আজকের Android-এর async মডেল। ViewModel, Room, Retrofit, Compose — সবাই এর উপর চলে।
তাই এই part ভালো করে বুঝলে পরের সব part সহজ হবে।

### আগে বুঝুন — Kotlin, Coroutines আর Flow

**বড় ছবি (৪ ধাপে):**
1. **Kotlin language** — type system-এ null আছে কি নেই, সেটা compiler জানে। তাই NullPointerException অনেক কমে।
2. **Kotlin-এর tools** — data class, sealed class, extension, scope function, lambda। এগুলো দিয়ে কম code-এ পরিষ্কার model আর UI state লেখা যায়।
3. **Coroutines** — একটা কাজ "suspend" হয়ে থামতে পারে, thread block না করে। পরে আবার সেখান থেকে চলে।
4. **Flow** — সময়ের সাথে একের পর এক value আসে, এমন stream। UI state, database change, sensor data — সব Flow হিসেবে আসে।

**মূল ধারণা (এগুলোর উপর বাকি সব দাঁড়িয়ে):**
- **Null safety:** `String` আর `String?` আলাদা type। null check না করে `String?` ব্যবহার করলে compile error।
- **Immutability আগে:** `val`, read-only `List`, `data class` + `copy()`। state বদলাতে নতুন object বানাই।
- **Sealed hierarchy:** `sealed interface UiState` দিয়ে সব রকম state লিখি। `when` সব case cover না করলে compiler ধরে।
- **suspend মানে "থামতে পারে", background thread না।** কোন thread-এ চলবে সেটা ঠিক করে **Dispatcher**।
- **Structured concurrency:** প্রতিটা coroutine একটা **scope**-এর ভিতরে চলে। scope cancel হলে সব child cancel হয়। leak হয় না।
- **Cancellation cooperative:** coroutine নিজে suspend point-এ cancel check করে। `CancellationException` গিলে ফেললে cancel ভেঙে যায়।
- **Cold vs hot:** সাধারণ `Flow` cold — collect করলে তবেই চালু হয়। `StateFlow` / `SharedFlow` hot — collector না থাকলেও থাকে।
- **UI state = StateFlow।** ViewModel একটা `StateFlow<UiState>` দেয়। UI lifecycle মেনে collect করে।
- **Lifecycle-aware collect:** Compose-এ `collectAsStateWithLifecycle()`, View-এ `repeatOnLifecycle(STARTED)`।

**ছোট diagram — data কোন দিকে যায়:**
```
Room / Retrofit / Sensor
        │  Flow<T>  (cold)
        ▼
Repository ──► ViewModel: map / combine / stateIn(viewModelScope)
                    │  StateFlow<UiState>  (hot)
                    ▼
UI: collectAsStateWithLifecycle()  ──user event──► viewModel.onX()
```

**Flutter থেকে এলে কী আলাদা:**
- Dart-এ একটা isolate-এ একটা event loop। Kotlin coroutine অনেক thread-এ চলতে পারে। তাই thread safety নিয়ে ভাবতে হয় (K16)।
- Dart-এর `async`/`await` ≈ Kotlin-এর `suspend` + direct call। Kotlin-এ `await` লাগে শুধু `async {}`-এর `Deferred`-এ।
- Dart `Stream` ≈ Kotlin `Flow`। Dart-এ single-subscription stream cold-এর কাছাকাছি, broadcast stream hot-এর কাছাকাছি।
- Dart-এ `Future` শুরু হলে চলতেই থাকে। Kotlin-এ scope cancel করলে coroutine থামে। এটা বড় পার্থক্য।
- Dart-এর null safety আর Kotlin-এর null safety প্রায় এক। তবে Kotlin-এ Java code থেকে আসা "platform type" নতুন জিনিস (K1)।

---

### <a id="k1"></a>K1. ★ Why do Android teams use Kotlin and not Java? How does null safety work?

**প্রশ্নটা মানে:** Kotlin কেন default, আর `?`, `?.`, `?:`, `!!`, platform type — এগুলো ঠিকভাবে জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What are the main benefits of Kotlin over Java for Android?" · "How does Kotlin prevent NullPointerException?"

**বুঝে নিন:**
- Google 2019 থেকে Android-কে **Kotlin-first** বলে। Jetpack Compose শুধু Kotlin-এ। নতুন Jetpack API আর docs আগে Kotlin-এ আসে।
- Kotlin-এর বড় সুবিধা: null safety, coroutines, data/sealed class, extension, কম boilerplate। Java-র সাথে ১০০% interop — একই project-এ দুটো চলে।
- এখন Kotlin 2.x, **K2 compiler**। annotation processing-এর জন্য **KSP** (kapt না)।
- **Null safety:**

| লেখা | মানে |
|---|---|
| `String` | কখনো null না |
| `String?` | null হতে পারে |
| `a?.length` | `a` null হলে পুরো expression null, crash না |
| `a ?: "x"` | Elvis — বাঁ দিক null হলে ডান দিক |
| `a!!` | "আমি নিশ্চিত null না" — null হলে NPE |
| `a?.let { }` | null না হলে block চালাও |

- **Smart cast:** `if (a != null)` এর পর compiler `a`-কে `String` ধরে। কিন্তু `var` property-তে smart cast হয় না, কারণ অন্য thread মাঝে বদলাতে পারে। তখন local `val` নিন।
- **Platform type (`String!`):** Java method থেকে আসা value-র nullability Kotlin জানে না। compiler check করে না। ভুল ধরলে runtime NPE।
- সমাধান: Java দিকে `@Nullable` / `@NonNull` annotation (AndroidX, JSpecify) থাকলে Kotlin সঠিক type দেখে। না থাকলে নিজে `String?` ধরে নিন।

**Answer (English):**
> "Google calls Android Kotlin-first, and Jetpack Compose is Kotlin only. So new APIs and docs come to Kotlin first. For me the biggest win is null safety. The type system knows if a value can be null, so most null bugs become compile errors. Kotlin also gives coroutines, data classes and sealed types, so I write less code and model state better. It works with Java in the same project, so moving step by step is easy. The weak spot is Java interop: values from Java are platform types, and the compiler does not check them. So I treat them as nullable unless the Java code has nullability annotations. And I almost never use `!!`."

**Key words:** `null safety` · `safe call ?.` · `Elvis ?:` · `platform type` · `smart cast` · `Kotlin-first`

**Follow-up:**
- **Q:** When is it OK to use `!!`?
  **A:** "Almost never in production code. Maybe in a test, or right after a check where the compiler cannot see the guarantee. Usually `requireNotNull` with a clear message is better, because the crash tells me why."
- **Q:** Why does smart cast not work on a `var` property?
  **A:** "Because another thread or a custom getter could change it between the check and the use. I copy it into a local `val` first, or use `?.let`."
- **Q:** Can Kotlin still throw NullPointerException?
  **A:** "Yes. With `!!`, with platform types from Java, with `lateinit` before it is set, or when a constructor leaks `this` and a field is read too early."

**ভুল করবেন না:** "Kotlin-এ NPE কখনো হয় না" বলবেন না — platform type আর `!!` দিয়ে হয়।

**আরও দেখুন:** [K23 · Java interop](#k23) · [K2 · lateinit vs lazy](#k2)

---

### <a id="k2"></a>K2. ★ What is the difference between val, var and const val? And lateinit vs by lazy?

**প্রশ্নটা মানে:** কোন variable কখন বদলাতে পারে, কখন init হয়, আর late init-এর দুই উপায়ের পার্থক্য জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Is a val immutable?" · "When would you use lateinit instead of lazy?"

**বুঝে নিন:**
- `var` — আবার assign করা যায়।
- `val` — একবার assign। কিন্তু **object নিজে immutable না**। `val list = mutableListOf()` — list-এ add করা যায়। আর custom getter থাকলে `val` প্রতিবার ভিন্ন value দিতে পারে।
- `const val` — **compile-time constant**। শুধু primitive আর `String`। শুধু top-level, `object` বা `companion object`-এ। value call site-এ সরাসরি বসে যায় (inline)।

| | `lateinit var` | `val x by lazy { }` |
|---|---|---|
| কী | পরে বাইরে থেকে set হবে | প্রথম পড়ার সময় নিজে হিসাব হবে |
| `var` / `val` | শুধু `var` | শুধু `val` |
| type | non-null, primitive না (`Int` চলে না) | যেকোনো |
| ভুল ব্যবহার | set-এর আগে পড়লে `UninitializedPropertyAccessException` | — |
| check | `::x.isInitialized` | — |
| thread | নিজে কিছু করে না | default `SYNCHRONIZED` (thread-safe) |

- `lateinit` সাধারণ ব্যবহার: DI field injection (`@Inject lateinit var`), test-এর `@Before`-এ set।
- `lazy` সাধারণ ব্যবহার: ভারী object, প্রথম দরকারে বানানো। শুধু main thread থেকে পড়লে `lazy(LazyThreadSafetyMode.NONE)` — lock খরচ বাঁচে।
- Fragment-এ View binding `lazy`-তে রাখলে বিপদ: view destroy হলেও পুরনো view ধরে থাকে → leak।

**Answer (English):**
> "`var` can be reassigned. `val` is assigned once, but it is read-only, not deeply immutable. The object inside can still change. `const val` is a compile-time constant, only for primitives and String, and it lives at top level or in an object. For late setup I have two tools. `lateinit var` is for a non-null value that someone else sets later, like field injection or a test setup. If I read it too early, it throws. `by lazy` is for a `val` that computes itself on first read, and it is thread-safe by default. My rule: if the value comes from outside, `lateinit`. If the class can build it itself, `lazy`."

**Key words:** `read-only` · `compile-time constant` · `lateinit` · `lazy` · `isInitialized` · `LazyThreadSafetyMode`

**Follow-up:**
- **Q:** Why can't `lateinit` be used with `Int`?
  **A:** "Because Kotlin uses null inside to mark 'not set yet', and a primitive `Int` cannot be null. For numbers I use a nullable type or a default value."
- **Q:** What is the cost of `lazy`?
  **A:** "By default it takes a lock on first access and keeps an extra object. If only the main thread reads it, I use `LazyThreadSafetyMode.NONE`."

**ভুল করবেন না:** "`val` মানে immutable" — না, `val` মানে শুধু reassign করা যায় না।

**আরও দেখুন:** [K20 · Delegation with by](#k20) · [K1 · Null safety](#k1) · [K28 · Helpers and constants](#k28)

---

### <a id="k3"></a>K3. ★ data class, sealed class / sealed interface, enum class, object and companion object — when do you use each?

**প্রশ্নটা মানে:** Kotlin-এর type tools দিয়ে domain আর UI state ঠিকভাবে model করতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you model UI state in Kotlin?" · "Sealed class vs enum — what is the difference?"

**বুঝে নিন:**
- **data class** — value রাখার জন্য। primary constructor-এর property থেকে compiler বানায়: `equals`, `hashCode`, `toString`, `copy`, `componentN`। body-র property এগুলোতে ধরা হয় না।
- **enum class** — ঠিক করা কয়েকটা instance, সবার shape এক। যেমন `CameraLens.FRONT / BACK`। সব value পেতে `entries` (পুরনো `values()` না)।
- **sealed class / sealed interface** — ঠিক করা কয়েকটা **subtype**, প্রতিটার data আলাদা হতে পারে। subtype একই module আর package-এ থাকতে হয়। `when` exhaustive — নতুন case যোগ করলে যেখানে handle নেই সেখানে compile error।
- **sealed interface** ভালো যখন একটা class দুই hierarchy-তে থাকবে, বা constructor state লাগবে না। আজকাল UI state-এ এটাই বেশি।
- **object** — singleton। প্রথম access-এ lazily আর thread-safe ভাবে তৈরি হয়। **data object** — sealed hierarchy-তে state-এর জন্য, সুন্দর `toString` দেয়।
- **companion object** — class-এর ভিতরে একটা object। Java-র static-এর জায়গায়। factory, constant রাখার জন্য। Java থেকে static হিসেবে ডাকতে `@JvmStatic`।

```kotlin
sealed interface CameraUiState {
    data object Loading : CameraUiState
    data class Streaming(val url: String, val fps: Int) : CameraUiState
    data class Error(val message: String) : CameraUiState
}

fun render(s: CameraUiState) = when (s) {   // else লাগে না
    CameraUiState.Loading -> "loading"
    is CameraUiState.Streaming -> "live ${s.fps}fps"
    is CameraUiState.Error -> s.message
}
```

**Answer (English):**
> "A data class holds values. It gives me equals, hashCode, toString and copy, so it is perfect for models and immutable UI state. An enum is a fixed set of instances with the same shape, like a lens type. A sealed class or sealed interface is a fixed set of types, and each type can carry different data. I use it for UI state and results: Loading, Success with data, Error with a message. The big win is that `when` is exhaustive, so if I add a new state, the compiler shows every place I must handle it. `object` is a singleton, and a companion object holds factory functions and constants, like static in Java."

**Key words:** `data class` · `copy()` · `exhaustive when` · `sealed interface` · `data object` · `companion object` · `entries`

**Follow-up:**
- **Q:** Why prefer sealed interface over sealed class?
  **A:** "A class can implement many interfaces, so one type can be part of two hierarchies. And it has no constructor, so it is lighter. I use sealed class only when the subtypes share state or code in a constructor."
- **Q:** Any problem with data class in an `equals` check?
  **A:** "Only primary constructor properties are used. And if a property is a mutable list or an array, equality can surprise me. Arrays compare by reference, so I use `List` instead."
- **Q:** Is `object` thread-safe?
  **A:** "Creating it is thread-safe, the JVM does that once. But its mutable fields are not. I still need to protect any shared state inside."

**ভুল করবেন না:** `when`-এ `else` দিলে sealed-এর exhaustive check-এর সুবিধা হারায় — নতুন case চুপচাপ `else`-এ চলে যায়।

**আরও দেখুন:** [K24 · State and errors with sealed types](#k24) · [K22 · Equality and data classes](#k22) · [K28 · object vs companion](#k28)

---

### <a id="k4"></a>K4. ★ What are extension functions and scope functions (let, apply, run, also, with)?

**প্রশ্নটা মানে:** extension কীভাবে কাজ করে (আর সীমা কী), আর কোন scope function কখন — সেটা জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between let and apply?" · "How do extension functions work under the hood?"

**বুঝে নিন:**
- **Extension function** — class না বদলে নতুন function যোগ করার মতো লেখা: `fun String.isValidIp(): Boolean`।
- ভিতরে এটা একটা **static function**, receiver প্রথম parameter। তাই:
  - private member access করতে পারে না।
  - **statically resolved** — variable-এর declared type দেখে ঠিক হয়, runtime type না। override হয় না।
  - একই নামের member function থাকলে **member জেতে**।
- Android-এ: `Context.dp(…)`, `Flow<T>.throttle()`, Compose `Modifier.xxx()` — সব extension।
- **Scope functions** — দুই প্রশ্ন: object-কে কী নামে দেখি (`this` / `it`)? কী return হয় (object / lambda result)?

| function | object ভিতরে | return | সাধারণ ব্যবহার |
|---|---|---|---|
| `let` | `it` | lambda result | `x?.let { }` null check, map |
| `run` | `this` | lambda result | object দিয়ে কিছু হিসাব |
| `with(x)` | `this` | lambda result | এক object-এ অনেক call (extension না) |
| `apply` | `this` | object নিজে | object configure / builder |
| `also` | `it` | object নিজে | side effect: log, validate |

```kotlin
val request = Request.Builder().apply {
    url(streamUrl)
    header("Authorization", token)
}.build()

user?.let { repo.save(it) }
val list = loadItems().also { Log.d(TAG, "count=${it.size}") }
```

**Answer (English):**
> "An extension function lets me add a function to a type I do not own, like `String.isValidIp()`. Under the hood it is a static function with the receiver as the first parameter. So it cannot see private members, and it is resolved by the declared type, not the runtime type. If a member with the same name exists, the member wins. Scope functions differ in two things: do I see the object as `this` or `it`, and do they return the object or the lambda result. I use `apply` to configure an object, `also` for side effects like logging, and `let` with `?.` for null checks. I avoid nesting them, because nested `it` and `this` get hard to read."

**Key words:** `extension function` · `statically resolved` · `receiver` · `this vs it` · `returns the object` · `returns the lambda result`

**Follow-up:**
- **Q:** Can an extension function be overridden?
  **A:** "No. It is resolved at compile time by the declared type. If I need runtime polymorphism, I need a real member function."
- **Q:** `apply` vs `also`?
  **A:** "Both return the object. In `apply` the object is `this`, so I call its setters directly. In `also` it is `it`, so it reads like 'and also do this', good for logging or checks."

**ভুল করবেন না:** `x?.let { } ?: run { }` তে let-এর ভিতর null return হলে run-ও চলে — এটা if/else-এর সমান না।

**আরও দেখুন:** [K5 · inline and lambdas](#k5) · [K28 · Helpers and constants](#k28)

---

### <a id="k5"></a>K5. ◆ Explain higher-order functions, lambdas, inline, noinline, crossinline and reified.

**প্রশ্নটা মানে:** lambda-র খরচ কোথায়, `inline` কেন সেটা কমায়, আর বাকি keyword-গুলো কোন সমস্যা মেটায়।
**অন্যভাবেও জিজ্ঞেস করে:** "Why are functions like `let` and `map` marked inline?" · "What does reified do?"

**বুঝে নিন:**
- **Higher-order function** — function parameter নেয় বা function return করে। `list.filter { }`, `onClick: () -> Unit`।
- সাধারণ lambda একটা **object** হিসেবে তৈরি হয়। বাইরের variable capture করলে প্রতি call-এ নতুন object। loop-এ খরচ বাড়ে।
- **inline** — compiler function-এর body আর lambda-র body call site-এ copy করে দেয়। ফলে:
  - lambda object তৈরি হয় না।
  - **non-local return** চলে: lambda-র ভিতরে `return` লিখলে বাইরের function থেকে return হয়।
  - খরচ: bytecode বড় হয়। ছোট function-এই `inline` দিন।
- **noinline** — inline function-এর একটা lambda-কে inline করবেন না। দরকার যখন lambda-কে store করবেন বা অন্য function-কে পাঠাবেন।
- **crossinline** — lambda inline হবে, কিন্তু ভিতরে non-local `return` চলে না। দরকার যখন lambda অন্য context-এ চলে (যেমন `Runnable` বা অন্য lambda-র ভিতরে)।
- **reified** — generic type erase হয়ে যায়, runtime-এ `T` জানা যায় না। `inline` + `reified T` দিলে compiler আসল type বসায়। তখন `T::class`, `is T` চলে।

```kotlin
inline fun <reified T : Activity> Context.start() =
    startActivity(Intent(this, T::class.java))

context.start<SettingsActivity>()
```

**Answer (English):**
> "A higher-order function takes or returns a function. A normal lambda becomes an object, so in hot code it costs allocations. When I mark a function `inline`, the compiler copies the function body and the lambda into the call site. So no lambda object is created, and a `return` inside the lambda can return from the outer function. The cost is bigger bytecode, so I inline only small functions. `noinline` keeps one lambda as an object, when I need to store it or pass it on. `crossinline` is for a lambda that runs in another context, so a non-local return is not allowed. `reified` works only with inline, and it keeps the real generic type, so I can write `T::class`."

**Key words:** `higher-order function` · `inline` · `non-local return` · `noinline` · `crossinline` · `reified` · `type erasure`

**Follow-up:**
- **Q:** Why does `reified` need `inline`?
  **A:** "Generics are erased at runtime. Only when the body is copied into the call site can the compiler put the real type there."
- **Q:** Should I make every function with a lambda inline?
  **A:** "No. Only small, often-called ones. A large inline function makes the APK bigger, and I cannot store the lambda."

**আরও দেখুন:** [K4 · Extension and scope functions](#k4) · [K6 · Generics and variance](#k6)

---

### <a id="k6"></a>K6. ○ Explain generics in Kotlin: in / out (variance) and star projection.

**প্রশ্নটা মানে:** `List<String>` কেন `List<Any>`-এর জায়গায় চলে, কিন্তু `MutableList<String>` চলে না — এটা বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is covariance and contravariance?" · "What does `List<*>` mean?"

**বুঝে নিন:**
- default-এ generic **invariant**: `Box<String>` আর `Box<Any>`-এর মধ্যে কোনো সম্পর্ক নেই।
- **out T (covariant)** — class শুধু `T` **বের করে** (return), নেয় না। তখন `Producer<String>` কে `Producer<Any>` হিসেবে দেওয়া safe। উদাহরণ: `List<out E>`, `Flow<out T>`।
- **in T (contravariant)** — class শুধু `T` **নেয়** (parameter), ফেরত দেয় না। তখন `Consumer<Any>` কে `Consumer<String>` হিসেবে দেওয়া safe। উদাহরণ: `Comparable<in T>`, `FlowCollector<in T>`।
- মনে রাখার নিয়ম: **Producer → out, Consumer → in।** Java-র `? extends` = `out`, `? super` = `in`।
- **Declaration-site variance** — class লেখার সময় `out`/`in` দেওয়া (Kotlin-এর সুবিধা)। **Use-site** — ব্যবহারের জায়গায় `fun copy(from: Array<out Any>)`।
- `MutableList<T>` invariant, কারণ এটা পড়েও, লিখেও।
- **Star projection `List<*>`** — "কোনো একটা type, জানি না কোনটা"। পড়লে `Any?` পাবেন, লিখতে পারবেন না।
- **Type erasure:** runtime-এ `List<String>` আর `List<Int>` এক। তাই `is List<String>` হয় না — `is List<*>` হয়।

**Answer (English):**
> "By default Kotlin generics are invariant, so a `Box<String>` is not a `Box<Any>`. Variance fixes this when it is safe. `out T` means the type only produces T, it only returns it. Then a `List<String>` can be used as a `List<Any>`. `in T` means the type only consumes T, like a Comparator, so a consumer of Any can be used where a consumer of String is needed. My simple rule is: producer is out, consumer is in. `MutableList` stays invariant because it reads and writes. Star projection, `List<*>`, means a list of some unknown type. I can read items as `Any?`, but I cannot add anything."

**Key words:** `invariant` · `covariant (out)` · `contravariant (in)` · `star projection` · `type erasure` · `declaration-site variance`

**Follow-up:**
- **Q:** Why is `MutableList<String>` not a `MutableList<Any>`?
  **A:** "If it were, I could add an Int through the `Any` reference, and the String list would break. So the compiler blocks it."

**আরও দেখুন:** [K5 · reified](#k5) · [K7 · List vs MutableList](#k7)

---

### <a id="k7"></a>K7. ◆ What is the difference between List and MutableList? And Collections vs Sequences?

**প্রশ্নটা মানে:** read-only আর immutable-এর পার্থক্য, আর eager বনাম lazy processing কখন কোনটা।
**অন্যভাবেও জিজ্ঞেস করে:** "Is a Kotlin List immutable?" · "When would you use a Sequence?"

**বুঝে নিন:**
- `List<T>` = **read-only interface**, immutable না। ভিতরে আসলে `ArrayList` থাকতে পারে। কেউ `MutableList` হিসেবে রেখে বদলালে আপনার `List`-ও বদলাবে।
- `MutableList<T>` — add/remove আছে।
- ভালো অভ্যাস: class-এর ভিতরে mutable, বাইরে `List` দিন। UI state-এ নতুন list বানান (`list + item`), পুরনোটা বদলাবেন না।
- সত্যিকারের immutable দরকার হলে `kotlinx.collections.immutable` (`PersistentList`)। Compose stability-র জন্য কখনো এটা দরকার হয়।

| | Collection (`list.map{}.filter{}`) | Sequence (`list.asSequence()…`) |
|---|---|---|
| চলে কীভাবে | **eager** — প্রতি ধাপ পুরো list শেষ করে | **lazy** — একটা item সব ধাপ পার হয়, তারপর পরেরটা |
| মাঝের list | প্রতি ধাপে নতুন list | তৈরি হয় না |
| কখন শুরু | সাথে সাথে | terminal operation (`toList`, `first`) এ |
| ভালো যখন | ছোট list, ১–২ ধাপ | বড় data, অনেক ধাপ, `first`/`take` দিয়ে আগে থামা |

```kotlin
val firstMotion = frames.asSequence()
    .filter { it.hasMotion }
    .map { it.timestamp }
    .first()          // প্রথম match পেলেই থামে
```

- Sequence-এর নিজের overhead আছে। ছোট list-এ সাধারণ collection প্রায়ই দ্রুত। মাপুন, অনুমান না।
- Flow-ও lazy, কিন্তু async। Sequence sync।

**Answer (English):**
> "`List` is a read-only view, not truly immutable. The object behind it can be an ArrayList that someone else changes. `MutableList` adds add and remove. I keep mutable lists private and expose `List`, and for UI state I create a new list instead of changing the old one. Collections are eager. Each step like map or filter runs on the whole list and creates a new list. Sequences are lazy. Each item goes through all steps, and nothing runs until a terminal call like `toList` or `first`. So a Sequence helps with big data, many steps, or when I stop early. For small lists, a normal collection is often faster."

**Key words:** `read-only` · `immutable` · `eager` · `lazy` · `intermediate collection` · `terminal operation`

**Follow-up:**
- **Q:** Why should UI state not hold a MutableList?
  **A:** "If I change the same list in place, the reference stays the same. StateFlow and Compose compare values, so they may not see the change, and the UI does not update."

**আরও দেখুন:** [K22 · Equality and data classes](#k22) · [U2 · Recomposition and stability](#u2)

---

### <a id="k27"></a>K27. ★ What is the difference between an interface and an abstract class in Kotlin? Why are classes final by default, and what do the visibility modifiers mean?

**প্রশ্নটা মানে:** Kotlin-এ inheritance-এর নিয়ম (`open`, `abstract`, `interface`) আর visibility (`private`, `protected`, `internal`, `public`) ঠিক জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why do you need `open` in Kotlin?" · "What does `internal` mean?"

**বুঝে নিন:**
- Kotlin-এ class আর member **default-এ final**। inherit বা override করতে দিতে হলে `open` লিখতে হয়।
- কারণ: যে class inheritance-এর জন্য বানানো হয়নি, subclass সেটা সহজে ভাঙে। base class বদলালে subclass-ও ভাঙে। final default এই ঝুঁকি কমায়।
- `override` করা member নিজে open থাকে। আর বন্ধ করতে চাইলে `final override` লিখুন।

| | `interface` | `abstract class` |
|---|---|---|
| state (backing field) | রাখতে পারে না | পারে |
| constructor | নেই | আছে |
| default method body | পারে | পারে |
| কয়টা নেওয়া যায় | একটা class অনেক interface | মাত্র একটা class extend |
| কখন | contract বা capability (`Repository`, `Clock`) | কয়েকটা subtype একই state আর code share করে |

| Visibility | কে দেখে |
|---|---|
| `public` (default) | সবাই |
| `internal` | একই **module** (Gradle module) |
| `protected` | class আর তার subclass। Java-র মতো same package দেখে না |
| `private` | class-এর ভিতরে। top-level হলে একই file |

```kotlin
interface StreamSource {               // contract, state নেই
    val name: String
    suspend fun open(): Stream
    fun label() = "Source: $name"      // default body চলে
}

abstract class BaseCamera(protected val id: CameraId) : StreamSource {
    private var retries = 0            // state রাখা যায়
    open fun maxRetries() = 3          // open না দিলে override হবে না
}
```

- Multi-module app-এ `internal` খুব কাজের। module-এর ভিতরের code লুকিয়ে শুধু interface public রাখা যায় (R6)।
- `internal` security না। bytecode-এ এটা public, Java থেকে ডাকা যায়।
- Test-এ: Mockito 5 আর MockK final class mock করতে পারে। তবু আগে fake ব্যবহার করুন।
- Flutter mapping: Dart-এ প্রতিটা class একটা implicit interface। Dart 3-এ `base`, `final`, `interface` class modifier আছে। Dart-এর `_` (library-private) Kotlin-এর file-level `private`-এর কাছাকাছি।

**Answer (English):**
> "In Kotlin, classes and members are final by default. I must mark them `open` to allow inheritance or override. A class not built for inheritance breaks easily. An interface is a contract. It can have default method bodies, but no state and no constructor, and a class can implement many interfaces. An abstract class can hold state and has a constructor, but a class can extend only one. So I use interfaces for capabilities, and an abstract class only when subtypes really share state. For visibility, public is the default. Internal means the same Gradle module. Protected means the class and its subclasses. Private means the class, or the file for top-level code."

**Key words:** `final by default` · `open` · `abstract class` · `interface` · `internal` · `protected` · `composition over inheritance`

**Follow-up:**
- **Q:** Can an interface have properties?
  **A:** "Yes, but with no backing field. The property is abstract, or it has a getter that computes the value. The class that implements it holds the real state."
- **Q:** What does `internal` give you in a multi-module app?
  **A:** "I can hide the implementation inside a module. Other modules see only the public interface, so they cannot depend on details. But it is not security. From Java, internal code is public in the bytecode."
- **Q:** Inheritance or composition?
  **A:** "I prefer composition. I give a class a helper object, or I use interface delegation with `by`. Deep class trees are hard to change."

**ভুল করবেন না:** "`protected` same package-ও দেখে" বলা — Java-তে দেখে, Kotlin-এ না। Kotlin-এ শুধু class আর subclass।

**আরও দেখুন:** [K20 · Delegation with by](#k20) · [K3 · data, sealed, object](#k3) · [R18 · SOLID](#r18)

---

### <a id="k28"></a>K28. ◆ Where do you put helpers and constants: an object, a companion object, or top-level functions?

**প্রশ্নটা মানে:** Kotlin-এ `static` নেই — তাহলে helper function আর constant কোথায় রাখেন, আর কেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you write a static method in Kotlin?" · "Is a companion object the same as static in Java?"

**বুঝে নিন:**
- Kotlin-এ `static` keyword নেই। তিনটা উপায়:

| উপায় | কী | কখন |
|---|---|---|
| top-level function / `val` | file-এ, class-এর বাইরে। JVM-এ `FileNameKt` class-এর static method | pure helper, extension, কোনো class-এর না এমন constant |
| `object` | singleton, প্রথম access-এ তৈরি | একটা নামের instance লাগে, যেমন interface implement করবে |
| `companion object` | class-এর ভিতরে একটা object | factory (`newInstance`), class-এর সাথে বাঁধা constant (`TAG`, `ARG_ID`) |

- আমার নিয়ম: আগে top-level, কারণ এটাই সবচেয়ে সহজ। class-এর সাথে জড়িত হলে companion। নিজের নাম বা interface লাগলে `object`।
- Constant: `const val` (শুধু primitive আর `String`)। file-এর উপরে `private const val TAG = "CameraRepo"` খুব চলে।
- Java থেকে ডাকা:
  - top-level → `CameraUtilsKt.foo()`। নাম বদলাতে `@file:JvmName("CameraUtils")`।
  - companion function → `@JvmStatic` না দিলে `Foo.Companion.create()`।
  - companion-এর `const val` → Java-তে সরাসরি static field।
- সাবধান: `object`-এ mutable state মানে global state। test-এ reset করা কঠিন, fake দিয়ে বদলানো যায় না। API client বা repository-কে `object` না বানিয়ে Hilt-এর `@Singleton` দিন (R5)।

```kotlin
// CameraUtils.kt
fun String.isRtspUrl() = startsWith("rtsp://")     // top-level extension

class PlayerFragment : Fragment() {
    companion object {
        private const val ARG_ID = "camera_id"
        fun newInstance(id: String) = PlayerFragment().apply {
            arguments = bundleOf(ARG_ID to id)
        }
    }
}
```

**Answer (English):**
> "Kotlin has no static. For a pure helper or a constant that does not belong to a class, I use a top-level function or a top-level const val. It is the simplest option. When something belongs to one class, like a Fragment factory or an argument key, I put it in a companion object. I use an object when I need one named instance, for example one that implements an interface. I avoid mutable state in an object, because it is global state. It is hard to test and hard to replace. For an API client, I use a DI singleton instead. For Java callers, I add JvmStatic or JvmName so the calls look clean."

**Key words:** `top-level function` · `object` · `companion object` · `const val` · `@JvmStatic` · `@file:JvmName`

**Follow-up:**
- **Q:** Is a companion object the same as Java static?
  **A:** "Not exactly. It is a real object, created with the class. From Kotlin its members look static. From Java I need JvmStatic, or const for constants, to get real static members."
- **Q:** Why not make the repository an `object`?
  **A:** "Then it is a global singleton. I cannot swap it in tests, and its dependencies are hidden. With Hilt and @Singleton I still get one instance, but I can replace it with a fake."

**ভুল করবেন না:** সব helper একটা বড় `Utils` object-এ জমানো — top-level function বা extension-ই যথেষ্ট।

**আরও দেখুন:** [K3 · data, sealed, object](#k3) · [K23 · Java interop](#k23) · [R17 · Singletons](#r17)

---

### <a id="k8"></a>K8. ★ What is a coroutine? How is it different from a thread? What does suspend mean?

**প্রশ্নটা মানে:** coroutine আসলে কী, কেন হালকা, আর `suspend` ঠিক কী করে — background thread ভাবছেন কিনা সেটা ধরা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why are coroutines lighter than threads?" · "Does a suspend function run on a background thread?"

**বুঝে নিন:**
- **Coroutine** = একটা কাজ যেটা মাঝপথে **suspend** হতে পারে, আর পরে সেখান থেকেই আবার চলে।
- **Thread** OS-এর জিনিস। প্রতিটার নিজের stack (প্রায় ~1 MB পর্যন্ত reserve), তৈরি আর switch করতে খরচ। হাজার হাজার thread চালানো যায় না।
- Coroutine library-র জিনিস। heap-এ একটা ছোট object। অল্প কয়েকটা thread-এ হাজার হাজার coroutine চলে।
- **suspend হলে কী হয়:** coroutine thread ছেড়ে দেয়। thread অন্য কাজ করে (যেমন main thread UI আঁকে)। কাজ শেষ হলে coroutine আবার কোনো thread-এ চলে।
- **Blocking vs suspending:** `Thread.sleep(1000)` thread আটকে রাখে। `delay(1000)` শুধু coroutine থামায়, thread মুক্ত।
- **ভিতরে কীভাবে:** compiler প্রতিটা `suspend` function-এ একটা লুকানো `Continuation` parameter যোগ করে, আর function-কে **state machine** বানায়। প্রতিটা suspend point একটা state। local variable continuation object-এ save হয়।
- **`suspend` মানে background না।** `suspend` শুধু বলে "এটা থামতে পারে, শুধু coroutine বা আরেক suspend function থেকে ডাকা যাবে"। কোন thread — সেটা Dispatcher ঠিক করে (K9)।
- Suspend function-এর ভিতরে blocking call (`Thread.sleep`, পুরনো JDBC, ভারী loop) দিলে thread তবুও block হবে।
- Flutter-এ: Dart `await` একই কাজ করে single event loop-এ। Kotlin-এ একই মডেল, কিন্তু অনেক thread-এর pool-এ।

**Answer (English):**
> "A coroutine is a piece of work that can pause and resume later without blocking a thread. Threads are OS objects with their own stack, so they are heavy. Coroutines are small objects on the heap, so I can run thousands of them on a few threads. `suspend` means the function can pause. When it waits, for example for the network, it gives the thread back, and it continues later. The compiler turns it into a state machine with a Continuation. One important point: suspend does not mean background thread. The dispatcher decides the thread. If I call blocking code inside a suspend function on Main, I still freeze the UI."

**Key words:** `suspend` · `non-blocking` · `Continuation` · `state machine` · `lightweight` · `suspension point`

**Follow-up:**
- **Q:** What is the difference between `delay` and `Thread.sleep`?
  **A:** "`delay` suspends only the coroutine, so the thread is free for other work. `Thread.sleep` blocks the whole thread. On Main that freezes the UI and can cause an ANR."
- **Q:** Can I call a suspend function from normal code?
  **A:** "No, only from a coroutine or another suspend function. From normal code I start a coroutine with a scope, like `viewModelScope.launch`. `runBlocking` exists, but I use it only in tests or main functions, never on the Android main thread."
- **Q:** How would you wrap a callback API as a suspend function?
  **A:** "I use `suspendCancellableCoroutine`. I resume with the result or the error in the callback, and in `invokeOnCancellation` I cancel the underlying request."

**ভুল করবেন না:** "suspend function background-এ চলে" — এই কথা বললেই interviewer ধরবে।

**আরও দেখুন:** [K18 · suspend inside](#k18) · [K9 · Dispatchers](#k9) · [C12 · Main thread and ANR](#c12)

---

### <a id="k9"></a>K9. ★ Explain Dispatchers (Main, IO, Default) and withContext. What is main-safety?

**প্রশ্নটা মানে:** কোন কাজ কোন thread pool-এ যায়, আর thread switch-এর দায়িত্ব কার — সেটা বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "When do you use Dispatchers.IO vs Default?" · "Who should switch threads — the ViewModel or the repository?"

**বুঝে নিন:**

| Dispatcher | কোথায় চলে | কোন কাজ |
|---|---|---|
| `Dispatchers.Main` | Android main thread | UI update, ছোট কাজ |
| `Dispatchers.Main.immediate` | main, আগে থেকে main-এ থাকলে সাথে সাথে চলে | `viewModelScope`, `lifecycleScope` এটাই ব্যবহার করে |
| `Dispatchers.IO` | বড় shared pool (default সর্বোচ্চ 64 বা core সংখ্যা, যেটা বেশি) | blocking I/O: file, socket, পুরনো blocking SDK |
| `Dispatchers.Default` | CPU core সংখ্যার সমান thread (কমপক্ষে 2) | CPU কাজ: JSON parse, image process, sort |

- IO আর Default একই thread pool share করে। তাই IO থেকে Default-এ গেলে প্রায়ই thread switch হয় না।
- **withContext(dispatcher) { }** — block-টা অন্য dispatcher-এ চালায়, শেষ হলে result নিয়ে আগের dispatcher-এ ফেরে। নতুন coroutine না, একই coroutine।
- **Main-safety নিয়ম:** যেকোনো suspend function **main থেকে ডাকা safe** হওয়া উচিত। ভারী কাজ যে function করে, সে নিজেই `withContext` করবে। caller (ViewModel) thread নিয়ে ভাববে না।
- Room-এর suspend DAO আর Retrofit-এর suspend function আগে থেকেই main-safe। তাদের উপর আবার `withContext(IO)` লাগে না।
- **Testing:** dispatcher hardcode না করে constructor-এ inject করুন। test-এ `StandardTestDispatcher` দিন। `Dispatchers.setMain()` দিয়ে Main বদলান।

```kotlin
class SnapshotRepository(
    private val io: CoroutineDispatcher = Dispatchers.IO,
) {
    suspend fun saveJpeg(bytes: ByteArray, file: File) = withContext(io) {
        file.writeBytes(bytes)          // blocking, তাই IO
    }
}
```

**Answer (English):**
> "Main is the UI thread. IO is a large pool for blocking work like files and sockets. Default has about one thread per CPU core, and it is for CPU work like parsing or image processing. `withContext` runs a block on another dispatcher and comes back with the result, in the same coroutine. I follow main-safety: every suspend function must be safe to call from Main. The function that does the heavy work switches the thread itself, so the ViewModel does not care about threads. Room and Retrofit suspend functions are already main-safe, so I do not wrap them again. I also inject dispatchers, so tests can use a test dispatcher."

**Key words:** `Dispatchers.Main.immediate` · `Dispatchers.IO` · `Dispatchers.Default` · `withContext` · `main-safe` · `inject dispatchers`

**Follow-up:**
- **Q:** Why not just use IO for everything?
  **A:** "IO has many threads because they mostly wait. CPU work does not wait, so many threads on few cores only add switching cost. Default matches the core count, so it fits CPU work better."
- **Q:** What is `Main.immediate`?
  **A:** "If we are already on the main thread, it runs the code right away instead of posting it to the queue. That avoids one frame of delay. `viewModelScope` uses it."
- **Q:** What does `flowOn` do compared to `withContext`?
  **A:** "`flowOn` changes the dispatcher of the upstream part of a flow. Inside a `flow {}` builder I must not use `withContext` to emit, it breaks context preservation. So I use `flowOn`."

**আরও দেখুন:** [K8 · Coroutines vs threads](#k8) · [K26 · Testing coroutines](#k26) · [P1 · ANR](#p1)

---

### <a id="k10"></a>K10. ★ What is the difference between launch and async? What are Job and Deferred?

**প্রশ্নটা মানে:** কখন শুধু কাজ চালু করবেন, কখন result লাগবে — আর parallel কাজ ঠিকভাবে লিখতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you run two network calls in parallel?" · "What happens to an exception in async?"

**বুঝে নিন:**
- **launch** — "চালাও, result লাগবে না"। return করে **Job**।
- **async** — "চালাও, পরে result দাও"। return করে **Deferred<T>** (Job + result)। `await()` দিয়ে result নিন।
- **Job** দিয়ে: `cancel()`, `join()` (শেষ হওয়া পর্যন্ত অপেক্ষা), `isActive`, `isCompleted`, `isCancelled`। Job-এর tree থাকে — parent/child।
- **Parallel কাজ** — `coroutineScope { }`-এর ভিতরে দুটো `async`, তারপর দুটো `await`:

```kotlin
suspend fun loadDashboard(): Dashboard = coroutineScope {
    val cameras = async { api.cameras() }
    val alerts  = async { api.alerts() }
    Dashboard(cameras.await(), alerts.await())
}   // একটা fail হলে অন্যটা cancel, exception উপরে যায়
```

- **Exception:**
  - `launch`-এ uncaught exception সাথে সাথে parent-এ যায়।
  - `async`-এ exception `await()`-এ throw হয়। কিন্তু সাধারণ (non-supervisor) scope-এ child fail করলে **parent-ও সাথে সাথে cancel হয়** — `await` না ডাকলেও।
- ভুল: `async { }.await()` সাথে সাথে লেখা = sequential, `async` এর মানে নেই। তখন সরাসরি suspend call বা `withContext` দিন।
- `GlobalScope.async` এড়ান — কোনো parent নেই, leak হয়।

**Answer (English):**
> "`launch` starts work when I do not need a result. It returns a Job, which I can cancel or join. `async` starts work that returns a value. It returns a Deferred, and I get the value with `await`. I use async for parallel work inside `coroutineScope`: I start two asyncs, then await both. If one fails, the scope cancels the other and the error goes up. That is structured concurrency. A common mistake is `async { }.await()` on one line. That is just sequential code with extra cost. Also, in a normal scope, a failed async cancels the parent even before anyone calls await."

**Key words:** `launch` · `async` · `Job` · `Deferred` · `await` · `coroutineScope` · `parallel decomposition`

**Follow-up:**
- **Q:** How do you wait for many asyncs?
  **A:** "I map them to a list of Deferred and call `awaitAll()`. It fails fast if any one fails."
- **Q:** `coroutineScope` vs `supervisorScope`?
  **A:** "In `coroutineScope` one failed child cancels all others. In `supervisorScope` children fail alone, so I use it when tasks are independent, like loading many camera thumbnails."

**আরও দেখুন:** [K11 · Structured concurrency](#k11) · [L7 · Parallel calls](#l7)

---

### <a id="k11"></a>K11. ★ Explain structured concurrency: scopes, cancellation, SupervisorJob and exception handling.

**প্রশ্নটা মানে:** coroutine কখন মরে, error কোথায় যায়, আর cancel ভাঙে এমন common bug জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What happens to coroutines when the ViewModel is cleared?" · "Why must you rethrow CancellationException?"

**বুঝে নিন:**
- **Structured concurrency:** প্রতিটা coroutine একটা scope-এ জন্মায়। parent সব child শেষ না হলে শেষ হয় না। parent cancel হলে সব child cancel। child-এর error parent-এ যায়। ফলে কোনো coroutine হারিয়ে যায় না।
- **Android scope:**
  - `viewModelScope` — `SupervisorJob() + Dispatchers.Main.immediate`। `onCleared()`-এ cancel।
  - `lifecycleScope` — Activity/Fragment destroy-এ cancel। Fragment-এ UI কাজে `viewLifecycleOwner.lifecycleScope`।
  - নিজের scope (যেমন Service বা app-wide কাজ): `CoroutineScope(SupervisorJob() + Dispatchers.Default)` — আর নিজেকেই `cancel()` করতে হবে।
  - `GlobalScope` এড়ান।
- **Cancellation cooperative:** cancel মানে একটা flag। coroutine suspend point-এ (`delay`, `withContext`, `yield`) check করে `CancellationException` throw করে। লম্বা CPU loop-এ নিজে `ensureActive()` ডাকুন।
- **CancellationException আবার throw করুন।** `catch (e: Exception)` এটাও ধরে ফেলে। গিলে ফেললে coroutine cancel হওয়ার পরও চলতে থাকে। `runCatching` একই সমস্যা করে।
- **SupervisorJob** — একটা child fail করলে বাকি child আর parent cancel হয় না। ViewModel-এ একটা request fail করলে পুরো screen-এর কাজ মরবে না।
- **Exception handling:**
  - Suspend call-এর চারপাশে `try/catch` — সবচেয়ে পরিষ্কার।
  - `CoroutineExceptionHandler` — শুধু **root** coroutine-এ (scope-এর সরাসরি `launch`) কাজ করে। শেষ ধাপ: log/crash report। recover করার জায়গা না।
  - `async`-এর error `await`-এ ধরুন।
- cleanup cancel হওয়ার পরও suspend করতে হলে: `finally { withContext(NonCancellable) { … } }`।

```kotlin
viewModelScope.launch {
    try {
        _state.value = UiState.Ready(repo.load())
    } catch (e: CancellationException) {
        throw e                          // cancel ভাঙবেন না
    } catch (e: IOException) {
        _state.value = UiState.Error("Network problem")
    }
}
```

**Answer (English):**
> "Structured concurrency means every coroutine lives in a scope. When the scope is cancelled, all its children stop, and a child's error goes up to the parent. So nothing leaks. On Android I use `viewModelScope`, cancelled in onCleared, and `lifecycleScope`. Cancellation is cooperative: the coroutine stops at the next suspension point by throwing CancellationException. So I must never swallow it. If I catch a general Exception, I rethrow CancellationException. ViewModel scope uses a SupervisorJob, so one failed child does not cancel the others. For errors I prefer try/catch around the call. CoroutineExceptionHandler only works on root coroutines, and I use it only as a last place to log."

**Key words:** `structured concurrency` · `viewModelScope` · `SupervisorJob` · `cooperative cancellation` · `CancellationException` · `CoroutineExceptionHandler` · `ensureActive`

**Follow-up:**
- **Q:** Why is `runCatching` risky in coroutines?
  **A:** "It catches every Throwable, including CancellationException. So a cancelled coroutine thinks it failed normally and keeps running. I rethrow cancellation or write my own helper."
- **Q:** Where does CoroutineExceptionHandler not work?
  **A:** "On child coroutines and on async. A child sends its error to the parent, so only the root's handler is used. Async keeps the error for await."
- **Q:** How do you run cleanup that must finish after cancel?
  **A:** "In `finally`, and if the cleanup itself suspends, I wrap it in `withContext(NonCancellable)`. For example, closing a camera session or saving the last state."

**ভুল করবেন না:** `catch (e: Exception)` লিখে log করে চুপ থাকা — এটাই সবচেয়ে common coroutine bug।

**আরও দেখুন:** [K10 · launch vs async](#k10) · [K24 · Errors with sealed types](#k24) · [R1 · ViewModel](#r1)

---

### <a id="k12"></a>K12. ★ What is a cold Flow vs a hot Flow? Why do we use Flow and not LiveData now?

**প্রশ্নটা মানে:** Flow কখন চালু হয় বোঝেন কিনা, আর LiveData কেন নতুন code-এ আর প্রথম পছন্দ না।
**অন্যভাবেও জিজ্ঞেস করে:** "Is LiveData deprecated?" · "What is the difference between Flow and StateFlow?"

**বুঝে নিন:**
- **Cold Flow** (`flow { }`, Room `Flow`, `callbackFlow`) — কেউ collect করলে তবেই code চলে। **প্রতিটা collector-এর জন্য আলাদা run।** collector না থাকলে কিছু হয় না।
- **Hot Flow** (`StateFlow`, `SharedFlow`) — collector থাকুক বা না থাকুক, এটা আছে। অনেক collector একই value পায়।
- উদাহরণ: cold flow-তে network call থাকলে আর দুটো screen collect করলে → দুটো network call। hot বানালে (`stateIn`/`shareIn`) একটা call, দুজন share।
- **Flow vs LiveData:**

| | LiveData | Flow / StateFlow |
|---|---|---|
| Lifecycle-aware | নিজে থেকেই | collect করার সময় (`repeatOnLifecycle`, `collectAsStateWithLifecycle`) |
| Thread | observe সবসময় main-এ | যেকোনো dispatcher, `flowOn` |
| Operators | অল্প (`map`, `switchMap`) | অনেক (`combine`, `debounce`, `flatMapLatest`, `retry`…) |
| Platform | শুধু Android | pure Kotlin — JVM test, KMP |
| Compose | adapter লাগে | সরাসরি |

- **LiveData deprecated না।** কিন্তু Google-এর architecture guide আর samples এখন `StateFlow` দেখায়। docs নিজেই বলে data layer-এ LiveData না রাখতে। তাই নতুন code-এ StateFlow — LiveData শুধু পুরনো code-এ।
- Flutter-এ: Dart `Stream` ≈ Flow। `StreamController.broadcast` ≈ SharedFlow।

**Answer (English):**
> "A cold Flow runs only when someone collects it, and each collector gets its own run. A hot flow, like StateFlow or SharedFlow, exists without collectors, and all collectors share the same values. For new code I use Flow instead of LiveData. LiveData is not deprecated, but it is Android-only, it always delivers on the main thread, and it has few operators. Flow is pure Kotlin, so it works in every layer, it is easy to unit test, and it has operators like combine and debounce. The trade-off is that Flow is not lifecycle-aware by itself, so in the UI I collect it with a lifecycle-aware API."

**Key words:** `cold flow` · `hot flow` · `collector` · `StateFlow` · `lifecycle-aware` · `flowOn` · `legacy`

**Follow-up:**
- **Q:** How do you turn a cold flow into a hot one?
  **A:** "With `stateIn` or `shareIn` in a scope like viewModelScope. Then all collectors share one upstream."
- **Q:** How do you wrap a callback API, like a sensor listener, into a Flow?
  **A:** "With `callbackFlow`. I register the listener and call `trySend` in the callback. In `awaitClose` I unregister it, so the listener is removed when collection stops."
- **Q:** Would you migrate all LiveData right away?
  **A:** "No. It works and is not deprecated. I write new screens with StateFlow and migrate old ones when I touch them. `asLiveData()` and `asFlow()` help in between."

**ভুল করবেন না:** "LiveData deprecated" বলবেন না — বলুন "legacy for new code, not deprecated"।

**আরও দেখুন:** [K13 · StateFlow vs SharedFlow](#k13) · [K19 · callbackFlow](#k19) · [K14 · Safe collect](#k14)

---

### <a id="k13"></a>K13. ★ What is the difference between StateFlow and SharedFlow? Explain stateIn / shareIn with SharingStarted.WhileSubscribed(5000).

**প্রশ্নটা মানে:** কোন hot flow কোন কাজে, আর ViewModel-এ upstream কখন চালু/বন্ধ হবে সেটা ঠিকভাবে সেট করতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why 5000 milliseconds in WhileSubscribed?" · "When would you use SharedFlow instead of StateFlow?"

**বুঝে নিন:**
- **StateFlow** — সবসময় **একটা current value** আছে (`.value`)। initial value লাগে। নতুন collector সাথে সাথে latest value পায়। **conflated** — দ্রুত অনেক update হলে slow collector মাঝেরগুলো মিস করে, শুধু latest পায়। **একই value (`equals`) আবার set করলে emit হয় না।**
- **SharedFlow** — value নাও থাকতে পারে। configure করা যায়: `replay` (নতুন collector কত পুরনো value পাবে), `extraBufferCapacity`, `onBufferOverflow`। default `replay = 0` — collector না থাকলে emit করা value হারিয়ে যায়।
- নিয়ম: **state → StateFlow। একাধিক জনকে broadcast করা event/stream → SharedFlow।**
- **stateIn / shareIn** — cold flow-কে hot বানায়, একটা scope-এ:

```kotlin
val uiState: StateFlow<CamerasUiState> = repo.observeCameras()   // Room Flow
    .map { CamerasUiState.Ready(it) }
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = CamerasUiState.Loading,
    )
```

- **SharingStarted:**
  - `Eagerly` — সাথে সাথে শুরু, scope শেষ পর্যন্ত চলে।
  - `Lazily` — প্রথম collector এলে শুরু, তারপর আর থামে না।
  - `WhileSubscribed(5000)` — collector থাকলে চলে। শেষ collector চলে যাওয়ার **5 সেকেন্ড পর** upstream থামে।
- **কেন 5000:** rotation-এ Activity কয়েকশো ms-এর জন্য collector হারায়। 5 সেকেন্ড অপেক্ষা করলে upstream (DB query, socket, sensor) restart হয় না। কিন্তু app background-এ গেলে 5 সেকেন্ড পর বন্ধ — battery বাঁচে।
- Room flow, location, sensor, camera status — এগুলোর জন্য `WhileSubscribed` সবচেয়ে ভালো।
- `MutableStateFlow` update করতে `_state.update { it.copy(...) }` — এটা atomic, race-safe (K16)।

**Answer (English):**
> "StateFlow always has one current value. It needs an initial value, a new collector gets the latest value right away, and it skips equal values. SharedFlow can have no value, and I can set replay and buffer. With replay zero, values sent when nobody listens are lost. So I use StateFlow for UI state, and SharedFlow to broadcast a stream to many listeners. `stateIn` turns a cold flow into a StateFlow inside a scope. I usually use `WhileSubscribed(5000)`. The upstream runs while the UI collects, and stops five seconds after the last collector leaves. A rotation takes less than five seconds, so the query does not restart. But in background it stops and saves battery."

**Key words:** `StateFlow` · `SharedFlow` · `replay` · `conflated` · `stateIn` · `SharingStarted.WhileSubscribed` · `upstream`

**Follow-up:**
- **Q:** What happens if I emit the same object twice to a StateFlow?
  **A:** "Nothing. StateFlow compares with equals, so equal values are not emitted. That is why I use immutable data classes and `copy`, not mutated objects."
- **Q:** Why not create the flow in a function like `fun getState() = repo.flow().stateIn(...)`?
  **A:** "Each call creates a new StateFlow and a new upstream. Recomposition can call it many times. I keep it as a property in the ViewModel, created once."
- **Q:** When would you use `Eagerly`?
  **A:** "When the data must be ready before any UI collects, and the work is cheap. For example, a small setting that many parts read. For DB or sensors I prefer WhileSubscribed."

**আরও দেখুন:** [K12 · Cold vs hot Flow](#k12) · [K14 · Safe collect](#k14) · [R1 · ViewModel](#r1)

---

### <a id="k14"></a>K14. ★ Which Flow operators do you use most? How do you collect a Flow safely in the UI?

**প্রশ্নটা মানে:** আসল কাজে operator বেছে নিতে পারেন কিনা, আর background-এ collect করে resource নষ্ট করেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between combine and zip?" · "Why is `lifecycleScope.launch { flow.collect {} }` not enough?"

**বুঝে নিন:**

| Operator | কাজ |
|---|---|
| `map` / `filter` | প্রতিটা value বদলানো / বাদ দেওয়া |
| `combine(a, b)` | যেকোনো একটা নতুন value দিলে দুটোর **latest** নিয়ে emit (প্রথমবার দুজনেরই একটা value লাগে) |
| `zip(a, b)` | জোড়া মিলিয়ে — a-র ১ম + b-র ১ম |
| `flatMapLatest` | নতুন value এলে আগের inner flow **cancel** করে নতুনটা চালায় |
| `debounce(300)` | 300ms চুপ থাকলে তবেই শেষ value পাঠায় |
| `distinctUntilChanged` | পরপর একই value বাদ দেয় |
| `catch { }` | **upstream**-এর error ধরে, fallback emit করা যায় |
| `retry(3) { it is IOException }` | error হলে upstream আবার চালায় |
| `onStart` / `onEach` / `onCompletion` | loading দেখানো, log, cleanup |
| `flowOn(Dispatchers.IO)` | upstream-এর dispatcher বদলায় |

- `catch` শুধু নিজের **উপরের** অংশের error ধরে। `collect { }`-এর ভিতরের error ধরে না।
- **নিরাপদে collect:**
  - সাধারণ `lifecycleScope.launch { flow.collect { } }` — app background-এ গেলেও collect চলে। Activity destroy পর্যন্ত। ফলে background-এ UI update, sensor/location চলতেই থাকে।
  - **View:** `repeatOnLifecycle(Lifecycle.State.STARTED)` — STARTED-এ collect শুরু, STOPPED-এ cancel, আবার STARTED-এ নতুন করে।
  - **Compose:** `collectAsStateWithLifecycle()` (`lifecycle-runtime-compose`)। শুধু `collectAsState()` lifecycle মানে না।
  - পুরনো `launchWhenStarted` deprecated — এটা শুধু pause করত, upstream চলতেই থাকত।

```kotlin
// Fragment (View system)
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { render(it) }
    }
}

// Compose
val state by viewModel.uiState.collectAsStateWithLifecycle()
```

- `stateIn(WhileSubscribed(5000))` + lifecycle-aware collect একসাথে কাজ করে: UI stop হলে collector চলে যায় → 5s পর upstream বন্ধ।

**Answer (English):**
> "I use map and filter for simple changes, combine to merge several sources into one UI state, and flatMapLatest when a new input should cancel old work. For user input I add debounce and distinctUntilChanged. For errors I use catch to emit a fallback state, and retry with a condition for network errors. Note that catch only handles errors from upstream, not from collect. For collecting, a plain `lifecycleScope.launch` keeps collecting in background. So in Views I use `repeatOnLifecycle(STARTED)`, and in Compose `collectAsStateWithLifecycle`. Together with `WhileSubscribed(5000)`, the upstream stops when the app goes to background."

**Key words:** `combine` · `flatMapLatest` · `debounce` · `catch` · `retry` · `repeatOnLifecycle` · `collectAsStateWithLifecycle`

**Follow-up:**
- **Q:** `combine` vs `zip`?
  **A:** "`combine` emits every time any source changes, using the latest of each. `zip` waits for a pair, one from each, so it can stall if one side is slow. For UI state I almost always use combine."
- **Q:** `flatMapLatest` vs `flatMapConcat` vs `flatMapMerge`?
  **A:** "Latest cancels the old inner flow, good for search. Concat runs them one after another in order. Merge runs them at the same time. I pick by whether old work still matters."
- **Q:** Why `collectAsStateWithLifecycle` and not `collectAsState`?
  **A:** "`collectAsState` keeps collecting while the composition exists, even in background. The lifecycle version stops below STARTED, which saves battery and stops sensor or location work."

**ভুল করবেন না:** Flow chain-এর একদম শেষে `catch` দিলে error-এর পর পুরো flow শেষ হয়ে যায় — দরকার হলে inner flow-তে catch দিন (K17 দেখুন)।

**আরও দেখুন:** [K13 · stateIn](#k13) · [K17 · Search with debounce](#k17) · [U9 · Compose and ViewModel](#u9)

---

### <a id="k15"></a>K15. ◆ What is the difference between Channels and Flow? How do you handle one-time UI events like navigation or a snackbar?

**প্রশ্নটা মানে:** Channel কী, আর "one-off event" নিয়ে Google-এর এখনকার guidance জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you show a snackbar from the ViewModel?" · "What is wrong with SingleLiveEvent or SharedFlow for events?"

**বুঝে নিন:**
- **Channel** — coroutine-দের মধ্যে value পাঠানোর queue। `send` / `receive`। **hot**। প্রতিটা value **একজন receiver**-ই পায় (fan-out — ভাগ হয়, copy না)।
- Capacity: `RENDEZVOUS` (default, buffer নেই), `BUFFERED`, `CONFLATED` (শুধু latest), `UNLIMITED`।
- **Flow** — stream-এর declarative API, অনেক operator। Channel হলো lower-level primitive। `callbackFlow`, `channelFlow`, `buffer()` ভিতরে Channel ব্যবহার করে।
- **One-time event — Google-এর এখনকার guidance (developer.android.com, UI events page):**
  - ViewModel থেকে আসা event **UI state-এ বদলে দিন।** যেমন `userMessage: String?`। UI snackbar দেখায়, তারপর `viewModel.userMessageShown()` ডাকে → state থেকে message মুছে যায়।
  - কারণ: Channel / SharedFlow দিয়ে event পাঠালে, producer (ViewModel) যদি consumer (UI)-এর চেয়ে বেশি দিন বাঁচে, delivery **guarantee নেই**। rotation বা background-এর সময় event হারাতে পারে।
  - UI থেকে শুরু হওয়া navigation (button click) — UI নিজেই করে, ViewModel-এর দরকার নেই।
  - ViewModel-এর logic-এর পর navigation (login সফল) — state-এ `isLoggedIn = true`, UI সেটা দেখে navigate করে।
- বাস্তবে অনেক team এখনো `Channel(BUFFERED)` + `receiveAsFlow()` ব্যবহার করে। ঝুঁকি জেনে করলে চলে। কিন্তু interview-এ আগে official guidance বলুন।
- পুরনো `SingleLiveEvent` — legacy hack, নতুন code-এ না।

```kotlin
data class UiState(val items: List<Item> = emptyList(), val userMessage: String? = null)

// Compose
uiState.userMessage?.let { msg ->
    LaunchedEffect(msg) {
        snackbarHostState.showSnackbar(msg)
        viewModel.userMessageShown()
    }
}
```

**Answer (English):**
> "A Channel is a hot queue between coroutines. Each value goes to only one receiver. Flow is the higher-level stream API with operators, and some flow builders use channels inside. For one-time events, I follow the current Android guidance: I turn ViewModel events into UI state. For a snackbar, the state has a `userMessage`. The UI shows it, then calls `userMessageShown()`, and the ViewModel clears it. The reason is that a Channel or SharedFlow does not guarantee delivery when the UI is gone for a moment, like during rotation. Navigation from a button click stays in the UI. Some teams still use a buffered Channel, and it can work, but I start with state."

**Key words:** `Channel` · `send / receive` · `fan-out` · `one-off event` · `event as state` · `userMessageShown` · `delivery guarantee`

**Follow-up:**
- **Q:** If you must use a Channel for events, how do you make it safer?
  **A:** "I use a buffered Channel with `receiveAsFlow`, so events wait until the UI collects. I collect with `repeatOnLifecycle` on `Dispatchers.Main.immediate`. Still, it is not fully guaranteed, so I keep it for small things."
- **Q:** Why not a SharedFlow with replay 0 for events?
  **A:** "If no one is collecting at that moment, the event is simply lost. With replay 1, a new collector gets the old event again after rotation. Both are wrong for events."

**আরও দেখুন:** [K13 · StateFlow vs SharedFlow](#k13) · [U4 · Side effects](#u4) · [R2 · MVI](#r2)

---

### <a id="k16"></a>K16. ◆ How do you make code thread-safe in Kotlin? Mutex, atomic types, @Volatile, synchronized, and a confined dispatcher.

**প্রশ্নটা মানে:** shared mutable state-এ race condition বুঝেন কিনা, আর coroutine-এর জন্য ঠিক tool বেছে নিতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Can you use synchronized inside a coroutine?" · "How would you protect a shared counter updated from many coroutines?"

**বুঝে নিন:**
- সমস্যা: `Dispatchers.Default`/`IO` অনেক thread। দুই coroutine একসাথে `count++` করলে update হারায় (read-modify-write atomic না)।
- **প্রথম পছন্দ: shared mutable state না রাখা।** immutable data + `StateFlow`। `MutableStateFlow.update { it.copy(...) }` — ভিতরে compare-and-set, তাই atomic।

| Tool | কী করে | কখন |
|---|---|---|
| `@Volatile` | সব thread latest value দেখে (visibility) | একটা flag (`isRunning`)। `count++` safe করে **না** |
| Atomic (`AtomicInteger`, `AtomicReference`) | একটা variable-এ lock ছাড়া atomic update | counter, একক reference |
| `synchronized` / `ReentrantLock` | thread block করা lock | ছোট, non-suspend critical section। ভিতরে suspend call দেওয়া যায় না |
| `Mutex` + `withLock` | coroutine lock — অপেক্ষার সময় **suspend** করে, thread block না | critical section-এর ভিতরে suspend call আছে |
| Confined dispatcher `Dispatchers.Default.limitedParallelism(1)` | সব কাজ একটার পর একটা চলে | একটা object-এর সব state access এক জায়গায় serialize করা |

```kotlin
private val mutex = Mutex()
private val cache = mutableMapOf<String, Token>()

suspend fun token(id: String): Token = mutex.withLock {
    cache[id] ?: api.fetchToken(id).also { cache[id] = it }  // suspend call ভিতরে
}
```

- `Mutex` **reentrant না** — একই coroutine আবার `withLock` করলে deadlock।
- `synchronized` block-এর ভিতরে suspend call দিলে Kotlin compiler error দেয় ("suspension point is inside a critical section")। `ReentrantLock`-এ compiler ধরে না — নিয়ম একই: thread lock-এর ভিতরে suspend না।
- `limitedParallelism(1)` মানে এক সময়ে একটা — কিন্তু সবসময় একই thread না। thread-local দরকার হলে এটা যথেষ্ট না।
- Kotlin-এর নিজের common atomic API (`kotlin.concurrent.atomics`, যেমন `AtomicInt`) এখনো **experimental** — `@OptIn(ExperimentalAtomicApi::class)` লাগে (kotlinlang.org দেখে নিন)। Android-এ `java.util.concurrent.atomic` সবচেয়ে বেশি চলে।

**Answer (English):**
> "First I try not to share mutable state. I use immutable data and update a MutableStateFlow with `update`, which is atomic. When I must share state, I pick the tool by the case. `@Volatile` only gives visibility, it is fine for a flag but not for `count++`. Atomic types are good for one counter or one reference. `synchronized` blocks the thread, so I use it only for short code with no suspend calls. If the critical section suspends, like a network call to refresh a token, I use a Mutex with `withLock`, which suspends instead of blocking. Another clean option is a confined dispatcher with `limitedParallelism(1)`, so all access runs one at a time."

**Key words:** `race condition` · `@Volatile` · `AtomicInteger` · `synchronized` · `Mutex.withLock` · `limitedParallelism(1)` · `MutableStateFlow.update`

**Follow-up:**
- **Q:** Why not use synchronized around a suspend call?
  **A:** "The lock is tied to a thread, but a coroutine can resume on another thread after suspending. And while it waits, it holds a thread. Mutex is made for coroutines."
- **Q:** Is `_state.value = _state.value.copy(...)` thread-safe?
  **A:** "No. Two coroutines can read the same old value and one update is lost. `_state.update { it.copy(...) }` retries until it wins, so it is safe."

**ভুল করবেন না:** `@Volatile` দিলেই `count++` safe — না, এটা শুধু visibility দেয়, atomicity না।

**আরও দেখুন:** [K13 · StateFlow update](#k13) · [L9 · Thread-safe cache](#l9)

---

### <a id="k17"></a>K17. ◆ Show how you build search-as-you-type with debounce and flatMapLatest, and explain it.

**প্রশ্নটা মানে:** Flow operator একসাথে জুড়ে বাস্তব feature বানাতে পারেন কিনা — আর error, empty, cancel ঠিক handle করেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you avoid sending a request on every key press?" · "How do you make sure old search results do not overwrite new ones?"

**বুঝে নিন:**
- লক্ষ্য: প্রতি key-তে request না। পুরনো request-এর result নতুনটাকে overwrite করবে না। error হলেও search চালু থাকবে।

```kotlin
@OptIn(FlowPreview::class, ExperimentalCoroutinesApi::class)
class SearchViewModel(private val repo: CameraRepository) : ViewModel() {
    private val query = MutableStateFlow("")
    val uiState: StateFlow<SearchUiState> = query
        .debounce(300)
        .map { it.trim() }
        .distinctUntilChanged()
        .flatMapLatest { q ->
            if (q.length < 2) flowOf(SearchUiState.Idle)
            else flow {
                emit(SearchUiState.Loading)
                emit(SearchUiState.Results(repo.search(q)))
            }.catch { emit(SearchUiState.Error) }
        }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), SearchUiState.Idle)

    fun onQueryChange(text: String) { query.value = text }
}
```

- **ধাপে ধাপে:**
  1. `MutableStateFlow` — user-এর text। UI প্রতি key-তে `onQueryChange` ডাকে।
  2. `debounce(300)` — user 300ms থামলে তবেই পরের ধাপে যায়।
  3. `map { trim }` + `distinctUntilChanged()` — "cam" → "cam " এর জন্য আবার request হবে না।
  4. `flatMapLatest` — নতুন query এলে **আগের search coroutine cancel**। পুরনো result আসেই না। race নেই।
  5. ২ অক্ষরের কম → `Idle`, কোনো request না।
  6. `catch` **inner flow-এর ভিতরে** — একটা search fail হলে শুধু সেটা `Error`, পুরো chain বেঁচে থাকে। বাইরে দিলে প্রথম error-এ search একেবারে বন্ধ।
  7. `stateIn(WhileSubscribed(5000))` — UI-তে StateFlow, background-এ থামে।
- `repo.search` suspend আর main-safe (Retrofit/Room) হতে হবে। cancel হলে Retrofit call-ও cancel হয়।
- TextField-এর text নিজে **debounce-এর আগের** state থেকে দেখান, নইলে typing lag করবে।
- `debounce` আর `flatMapLatest` আপনার kotlinx.coroutines version-এ এখনো opt-in চাইতে পারে — version অনুযায়ী `@OptIn` লাগে কিনা দেখে নিন।
- Test: `runTest` + test dispatcher, `advanceTimeBy(300)` দিয়ে সময় এগিয়ে দেখুন একটাই request হলো।

**Answer (English):**
> "I keep the query in a MutableStateFlow and update it on every key press. Then I apply `debounce(300)`, so I only search after the user stops typing for 300 milliseconds. I trim and use `distinctUntilChanged`, so the same query does not search twice. Then `flatMapLatest`: when a new query arrives, it cancels the old search. So old results can never overwrite new ones. Inside, I emit Loading, then Results, and I put `catch` inside the inner flow. That way one failed search shows an error, but the search keeps working for the next query. At the end I use `stateIn` with `WhileSubscribed(5000)`. I test it with `runTest` and virtual time."

**Key words:** `debounce` · `distinctUntilChanged` · `flatMapLatest` · `cancel previous request` · `inner catch` · `stateIn` · `virtual time`

**Follow-up:**
- **Q:** Why not use `flatMapConcat` or `flatMapMerge` here?
  **A:** "Concat would wait for old searches to finish, so it is slow. Merge would run them together, so an old slow result could arrive last and show the wrong list. Latest cancels the old one, which is what search needs."
- **Q:** How do you test the debounce?
  **A:** "I use `runTest` with a test dispatcher for the ViewModel. I send a few queries quickly, call `advanceTimeBy(300)`, and check the fake repository got only one call with the last query."

**ভুল করবেন না:** `catch`-কে `flatMapLatest`-এর বাইরে দিলে প্রথম error-এর পর search আর কাজ করবে না।

**আরও দেখুন:** [K14 · Flow operators](#k14) · [L5 · Debounced search](#l5) · [K26 · Testing coroutines](#k26)

---


## <a id="part-1b"></a>Part 1B — Kotlin আরও গভীরে

এই অংশে Kotlin-এর ভেতরের কাজ দেখব। Senior interview-এ শুধু "কী" জানলে হয় না, "ভেতরে কীভাবে হয়" জিজ্ঞেস করে।
suspend function-এর ভেতর, callback কে Flow বানানো, equality, Java interop, error modelling — এগুলো camera, sensor আর পুরনো Java SDK-এর কাজে প্রতিদিন লাগে।
শেষে Kotlin 2.x-এ কী নতুন, সেটা late 2026 অনুযায়ী দেওয়া আছে।

### আগে বুঝুন — Kotlin compiler আপনার code নিয়ে কী করে

Kotlin-এর অনেক সুবিধা আসলে **compiler-এর কাজ**। Runtime-এ JVM বা ART শুধু সাধারণ bytecode দেখে। এটা বুঝলে এই part-এর প্রায় সব প্রশ্নের উত্তর নিজে বের করতে পারবেন।

**বড় ছবি — ধাপে ধাপে:**
1. আপনি Kotlin লেখেন।
2. K2 compiler (Kotlin 2.x) code পড়ে, type check করে, তারপর JVM bytecode বানায়।
3. এই সময় compiler অনেক কিছু **নিজে লিখে দেয়**: `suspend` → state machine, `data class` → `equals/hashCode/copy`, `by` → forwarding code, `value class` → সাধারণ field।
4. Android build-এ D8 এই bytecode কে DEX বানায়। R8 ছোট ও optimize করে।
5. ART device-এ DEX চালায় (Part 2B-তে বিস্তারিত)।

**মূল ধারণাগুলো:**
- **suspend মানে thread block না।** Function মাঝপথে থেমে যায়। তার local state একটা object-এ জমা থাকে। Thread অন্য কাজে চলে যায়।
- **Continuation** = "এরপর কী করতে হবে" — একটা callback object। Compiler প্রতিটা suspend function-এ এটা লুকিয়ে পাঠায়।
- **Callback API → coroutine:** এক বার ফল দেয় এমন callback → `suspendCancellableCoroutine`। বার বার ফল দেয় এমন listener → `callbackFlow`।
- **Delegation (`by`)** = compiler forwarding code লেখে। `lazy`, `viewModels()`, `mutableStateOf` সব এই নিয়মে চলে।
- **Equality:** `==` মানে `equals()`। `===` মানে একই object। data class `equals` বানায় শুধু primary constructor-এর property থেকে।
- **Type দিয়ে ভুল আটকানো:** `value class` (ভুল ID আটকায়), `sealed` (সব state handle করতে বাধ্য করে)।
- **Java interop:** Java-র type-এ nullability জানা নেই → platform type (`String!`)। Bug-এর বড় উৎস।
- **Kotlin-এ checked exception নেই।** তাই জানা error (network নেই, 401) type দিয়ে দেখাই — `sealed` বা `Result`।

**ছোট diagram — একটা suspend call:**
```
loadUser() ──► api.get()  ── suspend ──► thread free (অন্য কাজ চলে)
                                   │
              network ফল আসে ──► continuation.resumeWith(result)
                                   │
loadUser() আবার চলে: label = 1 থেকে, আগের local value object থেকে নেয়
```

**Flutter থেকে এলে কী আলাদা:**
- Dart-এর `async/await`-ও compiler state machine বানায়। কিন্তু Dart-এ একটা isolate-এ একটাই thread। Kotlin-এ coroutine অনেক thread-এ চলতে পারে। তাই thread-safety আসল সমস্যা।
- Dart-এ cancel নেই বললেই চলে। Kotlin-এ **structured concurrency** আর cancellation আছে — scope বন্ধ হলে child কাজ থামে।
- Dart 3-এর `sealed class` + `switch` exhaustiveness আর Kotlin-এর `sealed` + `when` একই কাজ করে।
- Dart-এর `extension type` (Dart 3.3) আর Kotlin-এর `value class` কাছাকাছি জিনিস।
- `Stream` থেকে এলে: Kotlin `Flow` cold। `StreamController` থেকে listener-ভিত্তিক Flow বানাতে Kotlin-এ `callbackFlow`।

---

### <a id="k18"></a>K18. ★ How does a suspend function work inside?

**প্রশ্নটা মানে:** suspend function compile হয়ে কী হয়, আর কেন এটা thread আটকায় না — সেটা বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What does the compiler do with the suspend keyword?" · "How do you convert a callback API to a suspend function?"

**বুঝে নিন:**
- **CPS (Continuation-Passing Style):** compiler প্রতিটা `suspend fun` এ একটা লুকানো parameter যোগ করে: `Continuation<T>`। Return type হয়ে যায় `Any?`।
  - `suspend fun getUser(id: String): User` → bytecode-এ `getUser(id: String, cont: Continuation<User>): Any?`
- Function দুটোর একটা return করে: আসল ফল, অথবা একটা বিশেষ marker `COROUTINE_SUSPENDED`। Marker মানে "আমি থেমেছি, পরে continuation দিয়ে জানাব।"
- **State machine:** function-এর ভেতরে প্রতিটা suspend point একটা `label`। Compiler একটা continuation class বানায়। তাতে থাকে `label` আর যে local variable পরে লাগবে।
  - আবার চালু হলে `when (label)` দিয়ে ঠিক জায়গা থেকে চলে।
- **কেন thread block হয় না:** থামার সময় function আসলে **return করে**। Thread stack খালি হয়। Thread অন্য কাজ নেয়। ফল এলে `continuation.resumeWith()` dispatcher-এ কাজটা আবার পাঠায়।
- `suspend` নিজে কোনো thread বদলায় না। Thread বদলায় `Dispatcher` (`withContext(Dispatchers.IO)`)।
- **একবারের callback কে suspend বানাতে:** `suspendCancellableCoroutine`। এটা cancel support দেয়। `suspendCoroutine` cancel বোঝে না — নতুন code-এ এড়িয়ে চলুন।

Camera2-র `openCamera` callback কে suspend বানানো:
```kotlin
@RequiresPermission(Manifest.permission.CAMERA)
suspend fun CameraManager.openCameraAwait(id: String): CameraDevice =
    suspendCancellableCoroutine { cont ->
        openCamera(id, object : CameraDevice.StateCallback() {
            override fun onOpened(device: CameraDevice) {
                if (cont.isActive) cont.resume(device) else device.close() // cancel হলে leak না
            }
            override fun onDisconnected(device: CameraDevice) {
                device.close()
                if (cont.isActive) cont.resumeWithException(IllegalStateException("Camera disconnected"))
            }
            override fun onError(device: CameraDevice, error: Int) {
                device.close()
                if (cont.isActive) cont.resumeWithException(IllegalStateException("Camera error $error"))
            }
        }, null) // null handler = current thread-এর Looper
    }
```
- নিয়ম: **একবারই resume।** দুই বার resume করলে `IllegalStateException`। তাই `isActive` check।
- Cancel হলে কিছু বন্ধ করার থাকলে `cont.invokeOnCancellation { ... }` ব্যবহার করুন (যেমন request cancel)।

**Answer (English):**
> "The compiler changes every suspend function into continuation-passing style. It adds a hidden Continuation parameter, and the function can return a special COROUTINE_SUSPENDED value. Inside, the code becomes a state machine. Each suspend point is a label, and local variables are saved in the continuation object. When the function suspends, it really returns, so the thread is free for other work. When the result comes, resumeWith puts the work back on the dispatcher, and it continues from the saved label. To wrap a callback API, I use suspendCancellableCoroutine. I resume only once, and I clean up resources if the coroutine was cancelled."

**Key words:** `Continuation` · `CPS` · `state machine` · `COROUTINE_SUSPENDED` · `suspendCancellableCoroutine` · `resumeWith`

**Follow-up:**
- **Q:** Does a suspend function always run on a background thread?
  **A:** "No. Suspend only means it can pause. The thread is decided by the dispatcher. If I call blocking code inside a suspend function on Main, it still blocks Main."
- **Q:** Why not use suspendCoroutine?
  **A:** "suspendCoroutine does not support cancellation. If the screen closes, the coroutine keeps waiting. suspendCancellableCoroutine lets me react to cancel and free the resource."
- **Q:** What if the callback is called many times?
  **A:** "Then suspend is the wrong shape, because I can resume only once. I use callbackFlow for a stream of values."

**ভুল করবেন না:** "suspend মানে background thread" — এটা ভুল। Dispatcher thread ঠিক করে, suspend না।

**আরও দেখুন:** [K8 · Coroutines vs threads](#k8) · [K19 · callbackFlow](#k19) · [K11 · Cancellation](#k11)

---

### <a id="k19"></a>K19. ★ How do you turn a listener API into a Flow with callbackFlow?

**প্রশ্নটা মানে:** sensor বা location-এর মতো বার বার data দেওয়া listener কে নিরাপদে Flow বানাতে পারেন কিনা — unregister আর backpressure সহ।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you expose sensor data as a Flow?" · "What is awaitClose and why is it required?"

**বুঝে নিন:**
- `callbackFlow { }` ভেতরে একটা `Channel` রাখে। Listener থেকে `trySend(value)` দিয়ে value পাঠান।
- **`awaitClose { }` দিতেই হবে।** Collector বন্ধ হলে (cancel বা scope শেষ) এখানে listener unregister করবেন। না দিলে runtime-এ `IllegalStateException` হয়।
- Flow cold: প্রতিটা collector নিজের listener register করে। অনেক collector হলে `shareIn` / `stateIn` দিয়ে একটা ভাগ করুন।
- **Backpressure:** default buffer 64। Collector ধীর হলে buffer ভরে যায়, তখন `trySend` fail করে (value হারায়, crash না)।
  - Sensor-এ সাধারণত শুধু শেষ value দরকার → `.conflate()` বা `buffer(1, BufferOverflow.DROP_OLDEST)`।
  - সব value দরকার (যেমন log) → বড় buffer, আর collector দ্রুত রাখুন।
- **Sensor-এর বিশেষ ফাঁদ:** framework `SensorEvent` object **আবার ব্যবহার করে** (pool)। Object টা ধরে রাখা যাবে না। তাই `values.copyOf()` করে পাঠান।

```kotlin
data class Reading(val values: FloatArray, val timestampNs: Long)

fun SensorManager.readings(sensor: Sensor, delay: Int = SensorManager.SENSOR_DELAY_GAME): Flow<Reading> =
    callbackFlow {
        val listener = object : SensorEventListener {
            override fun onSensorChanged(e: SensorEvent) {
                trySend(Reading(e.values.copyOf(), e.timestamp)) // event reuse হয়, তাই copy
            }
            override fun onAccuracyChanged(s: Sensor, accuracy: Int) = Unit
        }
        registerListener(listener, sensor, delay)
        awaitClose { unregisterListener(listener) }
    }.conflate()
```
- UI-তে collect করুন `collectAsStateWithLifecycle()` দিয়ে। App background-এ গেলে collect থামে → listener unregister → battery বাঁচে।
- Location হলে একই আকার: `requestLocationUpdates(...)` আর `awaitClose { removeLocationUpdates(...) }`।

**Answer (English):**
> "I use callbackFlow. Inside, I create the listener, and in the callback I call trySend. Then I register the listener and call awaitClose, where I unregister it. awaitClose is required. It keeps the flow open and runs the cleanup when the collector stops, so there is no leak. For backpressure, I think about what the consumer needs. For sensors I usually want only the latest value, so I add conflate. One trap with sensors is that SensorEvent objects are reused, so I copy the values. In the UI I collect with lifecycle awareness, so the sensor stops in the background."

**Key words:** `callbackFlow` · `trySend` · `awaitClose` · `conflate` · `BufferOverflow` · `shareIn`

**Follow-up:**
- **Q:** What is the difference between send and trySend here?
  **A:** "send is a suspend function, but the listener callback is not a coroutine. So I use trySend. It returns a result and does not block. If the buffer is full, it fails instead of waiting."
- **Q:** Two screens need the same sensor. What do you do?
  **A:** "I share one upstream with shareIn or stateIn in a scope, with WhileSubscribed. Then only one listener is registered, and it stops a few seconds after the last collector goes."
- **Q:** When would you use channelFlow instead?
  **A:** "channelFlow is for when I start my own coroutines inside the builder and send from them. callbackFlow is the same thing but made for callback APIs, and it forces me to call awaitClose."

**ভুল করবেন না:** `awaitClose` ভুলে যাওয়া বা তার ভেতরে unregister না করা — sensor চলতেই থাকে, battery শেষ।

**আরও দেখুন:** [K18 · suspendCancellableCoroutine](#k18) · [N1 · Sensor data](#n1) · [N3 · Sensors and battery](#n3)

---

### <a id="k20"></a>K20. ◆ How does delegation with `by` work in Kotlin?

**প্রশ্নটা মানে:** interface delegation আর property delegate — দুটোই ভেতরে কী, আর Android-এ রোজ কোথায় দেখেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How does `by lazy` work?" · "What is `by viewModels()` actually doing?"

**বুঝে নিন:**
**১. Interface delegation:** `class A(inner: Repo) : Repo by inner` — compiler `Repo`-র সব method লিখে দেয়, যেগুলো `inner`-কে call করে। আপনি শুধু যেটা বদলাতে চান সেটা override করেন।
```kotlin
class LoggingRepo(private val inner: UserRepo) : UserRepo by inner {
    override suspend fun load(id: String): User {
        Log.d("Repo", "load $id")
        return inner.load(id)
    }
}
```
- ফাঁদ: `inner` নিজের ভেতরে অন্য method call করলে আপনার override **চলে না**। এটা inheritance না।

**২. Property delegate:** `val x by d` মানে get করলে `d.getValue(...)` call হয়, set করলে `d.setValue(...)`। যে object-এ এই operator আছে, সেটাই delegate।

| Delegate | কী করে |
|---|---|
| `by lazy { }` | প্রথম access-এ একবার চালায়। Default `SYNCHRONIZED` (thread-safe)। শুধু main thread হলে `LazyThreadSafetyMode.NONE` সস্তা। |
| `Delegates.observable(init) { _, old, new -> }` | value বদলালে callback |
| `Delegates.vetoable` | শর্ত না মিললে set বাতিল |
| `by map` | Map থেকে key-নামে value |
| `by viewModels()` | একটা `Lazy<VM>` দেয়। প্রথম access-এ `ViewModelProvider` থেকে VM নেয় — তাই `onCreate`-এর আগে access করলে crash হতে পারে। |
| `by mutableStateOf(x)` | Compose `State`-এর `getValue/setValue` extension। Read করলে snapshot system জানে কে পড়েছে, write করলে recomposition হয়। Import লাগে: `androidx.compose.runtime.getValue` / `setValue`। |

**Answer (English):**
> "Kotlin has two kinds of delegation. With interface delegation, the compiler writes all the forwarding methods for me, so I can wrap an object and override only one method. This is a clean way to add logging or caching without inheritance. With property delegates, reading the property calls getValue and writing calls setValue on the delegate object. lazy runs the block once on first access, and it is synchronized by default. by viewModels() returns a Lazy that gets the ViewModel from the provider. by mutableStateOf uses Compose state, so reads are tracked for recomposition. One trap: the wrapped object does not call my override internally."

**Key words:** `by` · `getValue/setValue` · `Lazy` · `LazyThreadSafetyMode` · `ReadWriteProperty` · `composition over inheritance`

**Follow-up:**
- **Q:** Is `by lazy` thread-safe?
  **A:** "Yes, by default it uses a lock, so only one thread runs the block. If I know only the main thread touches it, I can use the NONE mode to skip the lock."
- **Q:** Can you write your own property delegate?
  **A:** "Yes. I implement ReadWriteProperty, or just write getValue and setValue operators. A common example is a delegate that reads and writes a key in SavedStateHandle."

**আরও দেখুন:** [K2 · lateinit vs lazy](#k2) · [K27 · Interface vs abstract class](#k27) · [U3 · Compose state](#u3)

---

### <a id="k21"></a>K21. ◆ What is a value class, and when does it help?

**প্রশ্নটা মানে:** type-safe wrapper খরচ ছাড়া কীভাবে বানান, আর কখন খরচ (boxing) ফিরে আসে।
**অন্যভাবেও জিজ্ঞেস করে:** "What is an inline class in Kotlin?" · "How do you stop mixing up two String IDs?"

**বুঝে নিন:**
- `value class` একটা মাত্র property রাখে। Compile-এর পর বেশিরভাগ জায়গায় wrapper থাকে না — শুধু ভেতরের value থাকে। তাই extra object বা GC খরচ নেই।
```kotlin
@JvmInline value class CameraId(val raw: String)
@JvmInline value class UserId(val raw: String) {
    init { require(raw.isNotBlank()) }
}
fun openStream(camera: CameraId, owner: UserId) { /* ... */ }
// openStream(userId, cameraId) → compile error। দুটো String ভুলে উল্টো দেওয়া যায় না।
```
- **কখন সাহায্য করে:** দুই রকম ID, টাকা আর পরিমাণ, unit (ms বনাম ns) — যেখানে মিশে গেলে আসল bug হয়।
- **Boxing মানে:** কিছু জায়গায় compiler কে আসল wrapper object বানাতে হয়:
  - nullable type, যখন ভেতরের value primitive (যেমন `@JvmInline value class Millis(val v: Long)` → `Millis?` box হয়)। `String`-এর মতো reference type হলে `CameraId?` box হয় না — শুধু nullable `String` থাকে।
  - generic (`List<CameraId>`, `T`)
  - interface type বা `Any` হিসেবে পাঠালে
  তখন object allocate হয়। Hot loop-এ এটা মাথায় রাখুন।
- **Name mangling:** value class নেওয়া function-এর JVM নাম বদলে যায় (যেমন `openStream-abc123`)। তাই Java থেকে call করা কঠিন। Java থেকে দরকার হলে সাধারণ class বা `@JvmName` ভাবুন।
- Android-এ রোজ দেখেন: Compose-এর `Dp`, `Color`, `TextUnit`, `Offset` — সব value class।
- Flutter mapping: Dart 3.3-এর `extension type` প্রায় একই ধারণা।

**Answer (English):**
> "A value class wraps one value, but at runtime it is usually just that value, with no extra object. I use it for type-safe IDs. If CameraId and UserId are both value classes, the compiler stops me from passing them in the wrong order. I can also put validation in the init block. The cost is boxing. When I use it in a generic like List, as an interface type, or as nullable when it wraps a primitive, the compiler creates a real object. Also, function names get mangled, so calling them from Java is hard. Compose uses this idea a lot. Dp and Color are value classes."

**Key words:** `@JvmInline` · `value class` · `boxing` · `name mangling` · `type-safe ID`

**Follow-up:**
- **Q:** Why not just use a typealias?
  **A:** "A typealias is only a new name. The compiler still treats it as String, so it does not stop mix-ups. A value class is a real new type."

**ভুল করবেন না:** "value class কখনো allocate হয় না" — generic, interface, বা primitive-wrap করা nullable হলে box হয়।

**আরও দেখুন:** [K22 · Equality and data classes](#k22) · [K3 · data, sealed, object](#k3)

---

### <a id="k22"></a>K22. ★ Explain equality and data classes in Kotlin.

**প্রশ্নটা মানে:** `==`/`===`, `equals/hashCode`-এর চুক্তি, `copy()` — আর mutable key দিয়ে HashMap ভাঙার bug বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between == and === in Kotlin?" · "Why should a data class used as a Map key be immutable?"

**বুঝে নিন:**
- `a == b` → null-safe ভাবে `a?.equals(b)`। **Structural equality।**
- `a === b` → একই object কিনা। **Referential equality।**
- `data class` compiler দিয়ে বানায়: `equals`, `hashCode`, `toString`, `copy`, `componentN`।
  - শুধু **primary constructor-এর property** ধরে। Body-তে declare করা property `equals`-এ আসে না।
- **চুক্তি:** দুটো object equal হলে তাদের `hashCode` একই হতেই হবে। `HashMap`/`HashSet` আগে hashCode দিয়ে bucket খোঁজে, তারপর equals।
- **Mutable key-এর bug:**
```kotlin
data class Filter(var query: String)
val cache = hashMapOf(Filter("cam") to result)
val key = cache.keys.first()
key.query = "door"          // hashCode বদলে গেল
cache[key]                  // null! entry পুরনো bucket-এ আটকে আছে
```
  তাই key-তে শুধু `val` আর immutable type রাখুন।
- **`copy()` shallow।** ভেতরে `MutableList` থাকলে copy আর original একই list share করে।
- **Array ফাঁদ:** data class-এ `Array`/`FloatArray` থাকলে `equals` reference দেখে, content না। Override করুন বা `List` ব্যবহার করুন। (K19-এর `Reading`-এ এটা মনে রাখুন।)
- **Compose-এর সাথে যোগ:** state object immutable হলে আর `equals` ঠিক হলে Compose ঠিকমতো recomposition skip করে।

**Answer (English):**
> "In Kotlin, double equals calls equals, so it compares content. Triple equals checks if both are the same object. A data class gets equals, hashCode, toString and copy from the compiler, but only from the primary constructor properties. The rule is: equal objects must have the same hashCode. A HashMap finds the bucket by hashCode. So if I change a field of a key after I put it in the map, its hashCode changes, and I cannot find the entry anymore. That is why keys must be immutable. Also, copy is shallow, and arrays inside a data class compare by reference."

**Key words:** `structural equality` · `referential equality` · `equals/hashCode contract` · `shallow copy` · `immutable`

**Follow-up:**
- **Q:** Why does a data class with an Array give wrong equals?
  **A:** "Arrays in Kotlin use reference equality in equals. So two arrays with the same items are not equal. I use a List, or I override equals and hashCode with contentEquals and contentHashCode."
- **Q:** Why is immutability important for Compose state?
  **A:** "Compose compares old and new values to decide what to skip. If I mutate an object in place, the reference is the same, so Compose may not see the change. With immutable data and copy, a new value means a real change."
- **Q:** Should every model be a data class?
  **A:** "No. Data classes are good for plain values. For an object with identity, like a connection or a manager, value equality makes no sense, so I use a normal class."

**ভুল করবেন না:** body-তে রাখা property `equals`-এ আসে ভাবা — আসে না, শুধু primary constructor।

**আরও দেখুন:** [K3 · data class](#k3) · [K7 · List vs MutableList](#k7) · [U2 · Stability](#u2)

---

### <a id="k23"></a>K23. ◆ What do you need to know about Kotlin–Java interop?

**প্রশ্নটা মানে:** mixed codebase-এ (পুরনো Java SDK, camera vendor library) null crash আর awkward API কীভাবে এড়ান।
**অন্যভাবেও জিজ্ঞেস করে:** "What is a platform type?" · "How do you make Kotlin code nice to call from Java?"

**বুঝে নিন:**
- **Platform type (`String!`):** Java method-এর return-এ nullability জানা নেই। Kotlin check করে না। Null এলে পরে `NullPointerException`।
  - নিয়ম: Java থেকে আসা value-তে নিজে type লিখুন: `val name: String? = javaObj.getName()`।
  - Java code-এ nullability annotation দিন (`@Nullable`/`@NonNull`, নতুন standard **JSpecify**)। তখন Kotlin আসল type দেখে।
- **Kotlin কে Java-র জন্য সুন্দর করা:**

| Annotation | কাজ |
|---|---|
| `@JvmStatic` | companion-এর function Java-তে আসল static হয় (`Foo.create()`, `Foo.Companion.create()` না) |
| `@JvmOverloads` | default argument থেকে Java-র জন্য overload বানায়। Custom View constructor-এ সাধারণ — কিন্তু সাবধান, ভুল default style দিতে পারে। |
| `@JvmField` | getter/setter ছাড়া public field |
| `@JvmName` | JVM নাম বদলায় (নাম clash বা mangled নাম ঠিক করতে) |
| `@Throws(IOException::class)` | Java caller যেন checked exception ধরতে পারে |

- **SAM conversion:** Java-র এক-method interface (`Runnable`, `View.OnClickListener`) এ Kotlin lambda দেওয়া যায়। Kotlin interface-এর জন্য `fun interface` লিখতে হয়।
- **Checked exception:** Kotlin-এ নেই। Java method `IOException` throw করলে Kotlin compiler কিছু বলে না। Camera2-র `CameraAccessException`-এর মতো জিনিস নিজে ধরতে হবে।
- **Collections:** Kotlin `List` read-only, কিন্তু Java সেটা বদলাতে পারে। Java-কে list দিলে defensive copy ভাবুন।

**Answer (English):**
> "The biggest risk is platform types. When a Java method returns a String, Kotlin does not know if it can be null, so it does not check. I always write the type myself, usually nullable, at the boundary. If I own the Java code, I add nullability annotations like JSpecify. To make Kotlin easy to call from Java, I use JvmStatic for companion functions, JvmOverloads for default arguments, and Throws so Java can catch checked exceptions. Kotlin has no checked exceptions, so I must remember to catch things like CameraAccessException myself. SAM conversion lets me pass lambdas to Java single-method interfaces."

**Key words:** `platform type` · `JSpecify` · `@JvmStatic` · `@JvmOverloads` · `@Throws` · `SAM conversion` · `fun interface`

**Follow-up:**
- **Q:** Why can @JvmOverloads be risky on a custom View?
  **A:** "It creates all constructors that call the same one with default values. For a View, the three-argument constructor may get a default style of zero, so theme styles can be lost. I write the constructors myself when styles matter."

**ভুল করবেন না:** Java-র return value কে Kotlin-এ non-null ধরে নেওয়া — crash পরে, অন্য জায়গায় হয়, খুঁজে পাওয়া কঠিন।

**আরও দেখুন:** [K1 · Null safety](#k1) · [K28 · JvmStatic and helpers](#k28)

---

### <a id="k24"></a>K24. ★ How do you model state and errors with sealed types?

**প্রশ্নটা মানে:** UI state আর জানা error-কে type দিয়ে কীভাবে দেখান, আর কেন exception দিয়ে না।
**অন্যভাবেও জিজ্ঞেস করে:** "Result or exceptions — which do you use?" · "How do you make sure every UI state is handled?"

**বুঝে নিন:**
- `sealed interface` / `sealed class`: সব subtype compile time-এ জানা। তাই `when` **exhaustive** — নতুন state যোগ করলে যেখানে handle হয়নি সেখানে compile error।
```kotlin
sealed interface StreamState {
    data object Connecting : StreamState
    data class Playing(val fps: Int) : StreamState
    data class Failed(val reason: StreamError) : StreamState
}
enum class StreamError { Offline, AuthFailed, Unsupported }

fun label(s: StreamState) = when (s) {          // else নেই — ইচ্ছা করে
    StreamState.Connecting -> "Connecting…"
    is StreamState.Playing -> "${s.fps} fps"
    is StreamState.Failed -> "Error: ${s.reason}"
}
```
- **`else` লিখবেন না।** লিখলে নতুন subtype এলে compiler আর সাবধান করে না।
- **দুই রকম error:**
  - **জানা error (expected)** (network নেই, 401, camera offline, validation) → type দিয়ে return করুন। Caller handle করতে বাধ্য।
  - **Bug** (impossible state, programmer error) → exception, fail fast।
- **কেন জানা error-এ exception না:** Kotlin-এ checked exception নেই। Signature দেখে বোঝা যায় না কী throw হবে। ধরতে ভুলে গেলে crash।
- **`kotlin.Result`:** ছোট কাজে ভালো। কিন্তু error type শুধু `Throwable` — domain error বোঝায় না। Domain-এ নিজের sealed type (`Outcome<T, E>`) বেশি পরিষ্কার।
- **বড় ফাঁদ — `runCatching` আর coroutine:** `runCatching` `CancellationException`-ও ধরে ফেলে। তখন cancel থামে না। Suspend code-এ cancel আবার throw করুন, বা নিজের helper লিখুন।
- Kotlin team "rich errors" (error union type, KEEP-0462) নিয়ে কাজ করছে। Kotlin 2.4-এ এটা আসেনি, stable তো না-ই। পরের কোনো version-এ experimental হিসেবে আসার কথা — kotlinlang.org দেখে নিন।
- Flutter mapping: Dart 3-এর `sealed class` + `switch` একই exhaustive check দেয়।

**Answer (English):**
> "I model UI state as a sealed interface, and I handle it with when, without an else branch. Then if someone adds a new state, the compiler shows every place that must handle it. For errors, I split them into two groups. Expected errors, like no network or wrong password, are part of the result type. Bugs and impossible states are exceptions, and I let them fail fast. Kotlin has no checked exceptions, so if an expected error is an exception, the caller can easily forget it and the app crashes. One trap is runCatching in coroutines. It also catches CancellationException, so I rethrow it."

**Key words:** `sealed interface` · `exhaustive when` · `Result` · `domain error` · `CancellationException` · `fail fast`

**Follow-up:**
- **Q:** Why is sealed better than enum for UI state?
  **A:** "Enum values cannot carry different data. A sealed type lets each state hold its own data, like the fps for Playing or the error for Failed, and when is still exhaustive."
- **Q:** What is wrong with runCatching in a suspend function?
  **A:** "It catches every Throwable, including CancellationException. Then the coroutine does not stop when it should. I rethrow CancellationException or catch only the exceptions I expect."
- **Q:** Where do you convert exceptions into result types?
  **A:** "At the data layer boundary. The repository catches IOException or HTTP errors and maps them to a domain error. Above that layer, code works only with types."

**ভুল করবেন না:** sealed `when`-এ `else ->` দেওয়া — exhaustive check এর পুরো লাভ চলে যায়।

**আরও দেখুন:** [K3 · Sealed types](#k3) · [K11 · CancellationException](#k11) · [R10 · Network errors to UI](#r10)

---

### <a id="k25"></a>K25. ★ What is new in Kotlin 2.x?

**প্রশ্নটা মানে:** আপনি Kotlin-এর খবর রাখেন কিনা — K2, Compose compiler, KMP, আর নতুন language feature কোনটা stable।
**অন্যভাবেও জিজ্ঞেস করে:** "Which Kotlin version do you use, and what changed?" · "What is the K2 compiler?"

**বুঝে নিন:**
**বড় পরিবর্তন:**
- **Kotlin 2.0 (2024) — K2 compiler stable।** নতুন frontend। Compile দ্রুত। Smart cast আরও বুদ্ধিমান (যেমন local variable-এ check করা condition, `||` দিয়ে জোড়া `is` check)। IDE-তেও K2 mode।
- **Compose compiler Kotlin repo-তে চলে এসেছে (2.0 থেকে)।** এখন Compose Compiler Gradle plugin (`org.jetbrains.kotlin.plugin.compose`)। Kotlin version আর Compose compiler version আলাদা মেলাতে হয় না।
- **Strong skipping** default (2.0.20+)। পুরনো `StrongSkipping` flag deprecated — এটা আর বন্ধ করার জিনিস না।
- **KMP stable**, Google officially support করে (Room, DataStore KMP)। Compose Multiplatform for iOS stable (2025)।
- **Kotlin 2.4 থেকে K1 পুরো বাদ** — `-language-version 1.9` আর চলে না।
- **AGP 9 (2026)-এ built-in Kotlin:** আলাদা `org.jetbrains.kotlin.android` plugin লাগে না (Part 2B F12 দেখুন)।

**Language feature-এর অবস্থা (late 2026, kotlinlang.org "What's new" অনুযায়ী):**

| Feature | এসেছে | এখন |
|---|---|---|
| Guard condition in `when` (`is X if cond ->`) | 2.1 preview | **Stable — 2.2** |
| Non-local `break`/`continue` (inline lambda থেকে) | 2.1 preview | **Stable — 2.2** |
| Multi-dollar interpolation (`$$"""…"""`) | 2.1 preview | **Stable — 2.2** |
| Context parameters (`context(log: Logger)`) | 2.2 preview | **Stable — 2.4** (explicit context argument আর callable reference এখনো experimental) |
| Explicit backing fields | 2.3-এ experimental | **Stable — 2.4** |
| Collection literals (`val l: List<Int> = [1, 2]`) | — | **Experimental — 2.4** |

```kotlin
fun render(s: StreamState) = when (s) {
    is StreamState.Failed if s.reason == StreamError.Offline -> showRetry()   // guard
    is StreamState.Failed -> showError(s.reason)
    StreamState.Connecting, is StreamState.Playing -> Unit   // else না দিয়ে exhaustive
}
val schema = $$"""{ "$id": "camera", "name": "$$cameraName" }"""        // শুধু $$ interpolate হয়

context(log: Logger)
fun reconnect(cam: CameraId) { log.info("reconnect $cam") }
```
- Kotlin release: 2.2 (June 2025), 2.3 (December 2025), 2.4.0 (3 June 2026)। এরপর ছোট version এসেছে (2.4.10, 2.4.20, 2.4.21) — সর্বশেষটা kotlinlang.org-এ দেখুন।

**Answer (English):**
> "The biggest change in Kotlin 2 is the K2 compiler. It is faster and its smart casts are smarter. The Compose compiler now ships with Kotlin as a Gradle plugin, so I do not match versions by hand, and strong skipping is on by default. Kotlin Multiplatform is stable, and Google supports it for shared logic. In the language, Kotlin 2.2 made guard conditions in when, non-local break and continue, and multi-dollar strings stable. Kotlin 2.4 made context parameters stable, which helps pass things like a logger without long parameter lists. I check the What's New page before I use anything new, because some parts are still experimental."

**Key words:** `K2` · `smart cast` · `Compose Compiler Gradle plugin` · `guard conditions` · `context parameters` · `KMP`

**Follow-up:**
- **Q:** What did you need to change when moving to K2?
  **A:** "Mostly build setup: update the Kotlin version, use the Compose compiler plugin, and move kapt processors to KSP. Some code got new warnings or errors because K2 is stricter in a few places, so I fix those first."
- **Q:** Would you use context parameters everywhere now?
  **A:** "No. They are good for things passed through many layers, like a logger or a transaction scope. For normal dependencies, constructor injection is clearer. Too much hidden context makes code hard to read."
- **Q:** Is kapt still used?
  **A:** "Only for old processors. Room, Hilt and Moshi support KSP, which is faster and works well with K2. For new code I use KSP."

**ভুল করবেন না:** context parameters কে "এখনো experimental" বলা (2.4-এ stable), বা collection literals কে stable বলা (এখনো experimental)।

**আরও দেখুন:** [F12 · New in Android](#f12) · [P12 · Gradle and KSP](#p12) · [U2 · Strong skipping](#u2)

---

### <a id="k26"></a>K26. ○ How do you test and debug coroutines?

**প্রশ্নটা মানে:** coroutine code deterministic ভাবে test করতে পারেন কিনা, আর production-এ coroutine bug খুঁজতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you test a ViewModel that uses viewModelScope?" · "What is virtual time in runTest?"

**বুঝে নিন:**
- **`runTest`** (`kotlinx-coroutines-test`): test-এর জন্য coroutine চালায়। **Virtual time:** `delay(5_000)` আসলে অপেক্ষা করে না, scheduler সময় এগিয়ে দেয়। Test দ্রুত চলে, আর প্রতিবার একই ফল দেয়।
- **`Dispatchers.Main` test-এ নেই** (JVM unit test-এ Android Looper নেই)। তাই:
  - `Dispatchers.setMain(StandardTestDispatcher())` আগে, `Dispatchers.resetMain()` পরে। সাধারণত একটা JUnit rule-এ রাখি।
- **দুই রকম test dispatcher:**
  - `StandardTestDispatcher` — কাজ queue-তে রাখে। আপনি `advanceUntilIdle()`, `advanceTimeBy()`, `runCurrent()` দিয়ে চালান। Order control করা যায়।
  - `UnconfinedTestDispatcher` — সাথে সাথে চালায়। সহজ, কিন্তু order লুকিয়ে যায়।
- **Dispatcher inject করুন।** Code-এ `Dispatchers.IO` hard-code করলে test সেটা virtual time-এ আনতে পারে না। Constructor-এ `CoroutineDispatcher` নিন।
- **Flow test:** Turbine library (`flow.test { awaitItem() }`), অথবা `backgroundScope`-এ collect করে list-এ জমান।
```kotlin
@Test fun `retry waits 2 seconds after failure`() = runTest {
    val vm = StreamViewModel(FakeRepo(failFirst = true), StandardTestDispatcher(testScheduler))
    vm.connect()
    advanceTimeBy(1_999); runCurrent()
    assertEquals(StreamState.Connecting, vm.state.value)
    advanceTimeBy(1); runCurrent()
    assertTrue(vm.state.value is StreamState.Playing)
}
```
- **Debug:**
  - `CoroutineName("rtsp-reconnect")` দিন। Debug mode-এ thread নামে coroutine নাম দেখা যায়।
  - `kotlinx.coroutines.debug` system property বা `DebugProbes` (kotlinx-coroutines-debug) — চলমান coroutine-এর dump।
  - Android Studio / IntelliJ debugger-এ coroutine দেখার view আছে। Android device-এ এটা সব সময় পুরো কাজ নাও করতে পারে — নিজের setup-এ দেখে নিন।
  - Production-এ: `CoroutineExceptionHandler` দিয়ে না-ধরা exception log করুন।

**Answer (English):**
> "I use runTest from kotlinx-coroutines-test. It uses virtual time, so a delay of five seconds runs at once, and the test gives the same result every time. Unit tests have no Main dispatcher, so I set a test dispatcher as Main in a JUnit rule and reset it after. I inject dispatchers into my classes instead of using Dispatchers.IO directly, so tests can control them. With StandardTestDispatcher, I move time with advanceTimeBy and advanceUntilIdle, so I can test retry and timeout logic exactly. For flows, I use Turbine. For debugging, I name important coroutines with CoroutineName and use debug probes to dump running coroutines."

**Key words:** `runTest` · `virtual time` · `StandardTestDispatcher` · `Dispatchers.setMain` · `advanceUntilIdle` · `Turbine` · `CoroutineName`

**Follow-up:**
- **Q:** Why do you avoid Thread.sleep in coroutine tests?
  **A:** "It uses real time, so the test is slow and can be flaky. With runTest, delay uses virtual time, and I control it exactly."

**ভুল করবেন না:** class-এর ভেতরে `Dispatchers.IO` hard-code করা — তখন test virtual time কাজে লাগাতে পারে না।

**আরও দেখুন:** [R14 · ViewModel tests](#r14) · [K9 · Inject dispatchers](#k9) · [K17 · Testing debounce](#k17)

---


## <a id="part-2"></a>Part 2 — Android-এর মূল জিনিস: component, lifecycle, permission, background কাজ

এই part-টা Android-এর ভিত। প্রায় সব interview এখান থেকে শুরু হয়। Security camera বা custom OS-এর কাজে আরও বেশি জরুরি, কারণ সেখানে service, boot, background কাজ আর permission নিয়ে রোজ কাজ করতে হয়।
Flutter-এ এগুলো plugin আর engine লুকিয়ে রাখে। Native Android-এ আপনাকে নিজে সামলাতে হবে।

### আগে বুঝুন — Android app আসলে কীভাবে চলে

**বড় ছবি, ধাপে ধাপে:**
1. আপনার app একটা Linux process-এ চলে। প্রতিটা app-এর আলাদা Linux user id (UID) থাকে। তাই এক app অন্য app-এর file পড়তে পারে না।
2. Process-টা বানায় **Zygote**। Zygote আগেই ART আর framework class load করে রাখে। নতুন app লাগলে Zygote নিজেকে fork করে। তাই start দ্রুত হয়।
3. আপনার app নিজে `main()` লেখে না। System (`system_server`-এর ভেতরে ActivityManagerService / ActivityTaskManagerService) ঠিক করে কখন কোন **component** চালু হবে।
4. Component চার রকম: **Activity, Service, BroadcastReceiver, ContentProvider**। সবগুলো `AndroidManifest.xml`-এ declare করতে হয় (context-registered receiver ছাড়া)।
5. Component-গুলো **Intent** দিয়ে চালু হয়। Intent মানে "এই কাজটা করো" — একটা message, যা system-এর কাছে যায়, system ঠিক component খুঁজে চালায়।
6. System যেকোনো সময় আপনার process মেরে ফেলতে পারে (memory লাগলে)। তাই **lifecycle** আছে — system আপনাকে callback দিয়ে বলে "এখন visible", "এখন background", "এখন destroy"।
7. Battery বাঁচাতে Android প্রতি version-এ background কাজ আরও কড়া করেছে: Doze, App Standby bucket, background service limit, foreground service type।
8. Privacy-র জন্য বিপজ্জনক জিনিস (camera, mic, location, notification, local network) **runtime permission** দিয়ে চাইতে হয়।

**৮টা মূল ধারণা — বাকি সব এর ওপর দাঁড়িয়ে:**
| ধারণা | এক লাইনে |
|---|---|
| Component | system যেটা চালু/বন্ধ করে — আপনি `new` করে বানান না |
| Lifecycle | system callback দিয়ে state বদলের খবর দেয় |
| Process death | app background-এ থাকলে system process মারতে পারে; user ফিরে এলে state restore করতে হয় |
| Main thread | UI, lifecycle callback, receiver — সব এক thread-এ। Block করলে ANR |
| Intent | component-দের মধ্যে, app-দের মধ্যে message |
| Permission | install-time (normal), runtime (dangerous), signature, privileged |
| Background limit | background-এ কাজ = WorkManager বা foreground service; নিজে thread চালিয়ে রাখা নয় |
| targetSdk | নতুন নিয়ম বেশিরভাগই তখন লাগে যখন আপনি targetSdk বাড়ান |

**ছোট ছবি:**
```
Zygote --fork--> app process (UID 10xxx)
                    |
   Application.onCreate()  (ContentProvider.onCreate আগে চলে)
                    |
   Activity / Service / Receiver  <-- system Intent দিয়ে চালায়
                    |
   main thread: Looper -> MessageQueue -> Handler (সব callback এখানে)
```

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ সাধারণত একটা `FlutterActivity` আর সব screen Dart-এ। Native-এ Activity, Fragment, Service সবার আলাদা lifecycle।
- Flutter-এর `AppLifecycleState` (resumed / inactive / paused / detached / hidden) আসলে Activity lifecycle থেকেই আসে।
- Flutter-এ background কাজের জন্য `workmanager` plugin বা isolate ব্যবহার করেছেন — native-এ সরাসরি WorkManager, foreground service, AlarmManager।
- Permission plugin (`permission_handler`) যা করে, native-এ সেটা Activity Result API দিয়ে নিজে করবেন।
- Process death Flutter-এও হয়, কিন্তু অনেকে test করে না। Native interview-তে এই প্রশ্ন প্রায় সবসময় আসে।

---

### <a id="c1"></a>C1. ★ What are the four main Android components?

**প্রশ্নটা মানে:** Android app কোন কোন অংশ দিয়ে তৈরি, আর system এদের কীভাবে চালায় — সেটা জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What are the building blocks of an Android app?" · "Which components must be declared in the manifest?"

**বুঝে নিন:**
- **Activity** — একটা UI screen-এর entry point। User যা দেখে আর touch করে। আজকাল সাধারণত একটা Activity, ভেতরে Compose বা Fragment দিয়ে অনেক screen (single-activity app)।
- **Service** — UI ছাড়া কাজ। যেমন music চালানো, camera stream record করা। Service নিজে আলাদা thread নয় — main thread-এই চলে।
- **BroadcastReceiver** — system বা অন্য app-এর event শোনে। যেমন `BOOT_COMPLETED`, battery low। কাজ ছোট রাখতে হয়।
- **ContentProvider** — অন্য app-এর সাথে data share করার নিয়ম মানা interface (URI দিয়ে)। যেমন Contacts, MediaStore, FileProvider।
- চারটাই manifest-এ declare হয়। শুধু code-এ `registerReceiver()` করা receiver manifest-এ লাগে না।
- এরা সবাই **entry point** — system এদের যেকোনোটা দিয়ে আপনার process চালু করতে পারে। যেমন boot-এর পর receiver দিয়ে, UI ছাড়াই।
- `Application` class component না, কিন্তু process শুরু হলে একবার তৈরি হয়।

| Component | UI আছে? | কে চালু করে |
|---|---|---|
| Activity | হ্যাঁ | `startActivity(intent)` |
| Service | না | `startService` / `startForegroundService` / `bindService` |
| BroadcastReceiver | না | `sendBroadcast` বা system event |
| ContentProvider | না | `ContentResolver` query করলে |

**Answer (English):**
> "Android has four main components: Activity, Service, BroadcastReceiver and ContentProvider. An Activity is the entry point for a UI screen. A Service does work without UI, like playing media or recording camera video. A BroadcastReceiver reacts to events, like boot completed. A ContentProvider shares data with other apps through URIs. The key point is that the system creates these, not me. Each one is an entry point, so the system can start my process from any of them, even without UI. That is why I keep heavy setup out of these entry points."

**Key words:** `entry point` · `manifest` · `Intent` · `ContentResolver` · `system-managed`

**Follow-up:**
- **Q:** Is a Service a separate thread?
  **A:** "No. A Service runs on the main thread by default. I must move heavy work to a coroutine or a background thread myself."
- **Q:** Why do most apps now use a single Activity?
  **A:** "Navigation inside one Activity is easier to control, and screens can share state and animations. With Compose, screens are just composables, so many Activities add little value."
- **Q:** Can the system start your app without any UI?
  **A:** "Yes. A broadcast, a job, or a content provider query can start the process. So `Application.onCreate` must stay light."

**ভুল করবেন না:** "Service মানে background thread" — বলবেন না। Service main thread-এ চলে।

**আরও দেখুন:** [C7 · Services](#c7) · [C8 · BroadcastReceivers](#c8) · [C18 · Process start](#c18)

---

### <a id="c2"></a>C2. ★ Can you explain the Activity lifecycle?

**প্রশ্নটা মানে:** কোন callback কখন আসে, আর camera/sensor-এর মতো resource কোথায় খুলবেন, কোথায় ছাড়বেন — এটা জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What happens to the lifecycle when Activity A starts Activity B?" · "Where would you open and release the camera?"

**বুঝে নিন:**
```
onCreate -> onStart -> onResume   (এখন user interact করতে পারে)
          onPause  -> onStop -> onDestroy
onStop -> onRestart -> onStart   (ফিরে এলে)
```
- `onCreate` — একবার। UI set করা, ViewModel নেওয়া। `savedInstanceState` এখানে আসে।
- `onStart` — screen **visible**।
- `onResume` — সামনে, input পাচ্ছে।
- `onPause` — focus হারিয়েছে, কিন্তু হয়তো এখনো দেখা যাচ্ছে (dialog-style activity, multi-window)। এখানে ভারী কাজ করবেন না — পরের screen আসতে দেরি হবে।
- `onStop` — আর দেখা যাচ্ছে না। ভারী resource ছাড়ুন, data save করুন।
- `onDestroy` — finish হলে বা config change হলে। **সবসময় আসবে এমন guarantee নেই** — process সরাসরি মারা গেলে আসে না।
- `onSaveInstanceState` — API 28+ এ `onStop`-এর **পরে** আসে।

**A থেকে B খুললে order:**
```
A.onPause -> B.onCreate -> B.onStart -> B.onResume -> A.onStop (-> A.onSaveInstanceState)
```
Back চাপলে:
```
B.onPause -> A.onRestart -> A.onStart -> A.onResume -> B.onStop -> B.onDestroy
```
তাই A-র `onPause` ধীর হলে B দেরিতে দেখা যায়।

**Camera / sensor কোথায়:**
- **Sensor** (`SensorManager.registerListener`) — `onResume`-এ register, `onPause`-এ unregister। না হলে battery শেষ। Android 9+ এ background-এ continuous sensor event আসেই না।
- **Camera** — CameraX ব্যবহার করলে `bindToLifecycle(lifecycleOwner, ...)` দিলেই হয়। CameraX lifecycle দেখে camera খোলে/বন্ধ করে।
- নিজে Camera2 চালালে: সাধারণত `onResume`/`onStart`-এ খুলুন, `onPause`/`onStop`-এ বন্ধ। Multi-window-এ (Android 10+) একাধিক activity একসাথে resumed থাকতে পারে। Camera একটাই, তাই `onTopResumedActivityChanged()` আর `CameraManager.AvailabilityCallback` দেখুন — অন্য app camera নিলে সুন্দরভাবে ছেড়ে দিন।
- Modern উপায়: lifecycle-aware component (`DefaultLifecycleObserver`) বা `repeatOnLifecycle(Lifecycle.State.STARTED)`। Activity-তে সব logic না ঢুকিয়ে।

```kotlin
class SensorObserver(private val sm: SensorManager, private val l: SensorEventListener) :
    DefaultLifecycleObserver {
    override fun onResume(owner: LifecycleOwner) {
        sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)?.let {
            sm.registerListener(l, it, SensorManager.SENSOR_DELAY_GAME)
        }
    }
    override fun onPause(owner: LifecycleOwner) = sm.unregisterListener(l)
}
// lifecycle.addObserver(SensorObserver(sensorManager, listener))
```

**Flutter mapping:** `AppLifecycleState.resumed` ≈ `onResume`, `inactive` ≈ `onPause`, `hidden`/`paused` ≈ `onStop`।

**Answer (English):**
> "The main path is onCreate, onStart, onResume, then onPause, onStop, onDestroy. onStart means visible, onResume means in front and taking input. When A opens B, A gets onPause first, then B goes through create, start, resume, and only then A gets onStop. So I keep onPause very light, or B will appear late. I register sensors in onResume and unregister in onPause, to save battery. For the camera I use CameraX with bindToLifecycle, so it opens and closes with the lifecycle. One trap: onDestroy is not guaranteed if the process is killed, so I never save important data there."

**Key words:** `onPause` · `onStop` · `visible vs focused` · `bindToLifecycle` · `DefaultLifecycleObserver` · `multi-resume`

**Follow-up:**
- **Q:** When is onSaveInstanceState called?
  **A:** "On Android 9 and newer, it is called after onStop. It is not called when the user finishes the Activity with back, because the state is not needed."
- **Q:** What changes in multi-window mode?
  **A:** "Since Android 10, all visible activities can be resumed at the same time. Only one is the top resumed activity. The camera can be used by only one app at a time, so I listen to onTopResumedActivityChanged."
- **Q:** Where do you save user data?
  **A:** "In onStop at the latest, or better, right when it changes, through the ViewModel and repository. onDestroy may never run."

**ভুল করবেন না:** "onDestroy-এ data save করি" — এটা বললে বড় নম্বর কাটবে।

**আরও দেখুন:** [C3 · Fragment lifecycle](#c3) · [C4 · Process death](#c4) · [N3 · Sensors and battery](#n3)

---

### <a id="c3"></a>C3. ★ What is special about the Fragment lifecycle, and why do we use viewLifecycleOwner?

**প্রশ্নটা মানে:** Fragment-এর দুইটা lifecycle (fragment নিজে আর তার view) আলাদা — এটা বুঝে leak আর duplicate observer এড়াতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why should you not use `this` as the LifecycleOwner in a Fragment?" · "What happens to a Fragment's view when it goes to the back stack?"

**বুঝে নিন:**
- Fragment-এর order: `onAttach → onCreate → onCreateView → onViewCreated → onViewStateRestored → onStart → onResume → onPause → onStop → onSaveInstanceState → onDestroyView → onDestroy → onDetach`।
- `onActivityCreated` deprecated — `onViewCreated` ব্যবহার করুন।
- **মূল কথা:** Fragment back stack-এ গেলে তার **view destroy হয়** (`onDestroyView`), কিন্তু Fragment object বেঁচে থাকে। ফিরে এলে আবার `onCreateView` — নতুন view।
- তাই Fragment-এর দুইটা lifecycle: `lifecycle` (fragment) আর `viewLifecycleOwner.lifecycle` (view)।
- `this` দিয়ে Flow collect বা LiveData observe করলে: view চলে গেলেও observer থাকে → পুরনো view-তে লেখার চেষ্টা, leak। আবার ফিরে এলে নতুন observer যোগ হয় → **একই event দুইবার**।
- `viewLifecycleOwner` দিলে view destroy হলে observer নিজে থেকে বন্ধ।
- ViewBinding: `onDestroyView`-এ `_binding = null` করুন। না হলে পুরনো view tree ধরে রাখা হয় → leak।

```kotlin
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    viewLifecycleOwner.lifecycleScope.launch {
        viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
            viewModel.uiState.collect { render(it) }
        }
    }
}
override fun onDestroyView() { super.onDestroyView(); _binding = null }
```
- Compose-only app-এ Fragment প্রায় লাগে না। কিন্তু অনেক পুরনো codebase-এ আছে, তাই জানতেই হবে।

**Answer (English):**
> "A Fragment has two lifecycles: the Fragment itself and its view. When a Fragment goes to the back stack, its view is destroyed in onDestroyView, but the Fragment object stays alive. So if I observe data with the Fragment as owner, the observer outlives the view. That can leak the old view, and when I come back I add a second observer, so events run twice. That is why I always use viewLifecycleOwner for anything that touches the UI, together with repeatOnLifecycle. I also set the binding to null in onDestroyView."

**Key words:** `onDestroyView` · `viewLifecycleOwner` · `back stack` · `repeatOnLifecycle` · `binding = null`

**Follow-up:**
- **Q:** When can you access viewLifecycleOwner?
  **A:** "Only between onCreateView and onDestroyView. Outside that, it throws an exception."
- **Q:** How do two Fragments share data?
  **A:** "With a shared ViewModel scoped to the Activity or to a navigation graph, using `activityViewModels()` or a nav-graph scoped ViewModel. Not by calling each other directly."
- **Q:** Is setRetainInstance still used?
  **A:** "No, it is deprecated. ViewModel is the right way to keep data over configuration changes."

**ভুল করবেন না:** Fragment-এ `lifecycleScope` (fragment-এর) দিয়ে UI collect করা — `viewLifecycleOwner.lifecycleScope` লাগবে।

**আরও দেখুন:** [C19 · Screens talking](#c19) · [C4 · Process death](#c4) · [R1 · ViewModel](#r1)

---

### <a id="c19"></a>C19. ★ How do Fragments (or screens) talk to each other? Why not use direct references?

**প্রশ্নটা মানে:** এক screen থেকে আরেক screen-এ data পাঠানো, বা ফল ফেরত আনার ঠিক উপায় জানেন কিনা — leak আর crash ছাড়া।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you pass data between two Fragments?" · "How does a screen send a result back to the previous screen?"

**বুঝে নিন:**
তিন রকম দরকার, তিনটা উপায়:

| কী দরকার | উপায় |
|---|---|
| নতুন screen খোলার সময় input দেওয়া (যেমন id) | navigation argument |
| একবার একটা ফল ফেরত দেওয়া (picker, dialog) | Fragment Result API; Compose Navigation-এ back stack entry-র `SavedStateHandle` |
| দুই screen একই data একসাথে দেখে বা বদলায় | shared ViewModel (nav graph বা Activity scope) |

- **Navigation argument:** শুধু ছোট জিনিস পাঠান — id, filter। পুরো object না। Argument Bundle-এ যায়, তাই process death-এর পরেও ফেরত আসে। পরের screen id দিয়ে repository থেকে data load করে।
  - Navigation Compose-এ type-safe route (`@Serializable` class, `toRoute()`)। XML Navigation-এ Safe Args।
  - ViewModel-এ `SavedStateHandle` দিয়েও argument পড়া যায়।
- **Fragment Result API:** এক Fragment `setFragmentResult(key, bundle)` দেয়। অন্য Fragment একই key-তে `setFragmentResultListener` দিয়ে শোনে।
  - FragmentManager ফলটা রেখে দেয়। Listener-এর Fragment কমপক্ষে STARTED হলে তবেই দেয়। তাই back stack-এ থাকা Fragment-ও ঠিকমতো পায়।
  - Parent আর child Fragment-এর মধ্যে হলে parent তার `childFragmentManager`-এ listener দেয়।
- **Compose Navigation-এ ফল ফেরত:** `navController.previousBackStackEntry?.savedStateHandle?.set("key", value)`। আগের screen নিজের back stack entry-র `savedStateHandle` থেকে পড়ে।
- **Shared ViewModel:** `activityViewModels()` (পুরো Activity জুড়ে) বা `navGraphViewModels(R.id.checkout_graph)` (শুধু একটা flow-এর জন্য; flow শেষ হলে clear হয়)। Compose-এ parent graph-এর back stack entry দিয়ে `hiltViewModel(parentEntry)`। সবচেয়ে ছোট scope বাছুন।
- **কেন direct reference না:**
  - Rotation বা config change-এ Fragment নতুন instance হয়। পুরনো reference মরা object-এ লেখে → leak, পুরনো data, crash।
  - Process death-এ সব object নতুন। Reference হারায়, কিন্তু Bundle আর `SavedStateHandle` ফেরত আসে।
  - দুই screen শক্ত করে জুড়ে যায়। আলাদা করে test বা reuse করা কঠিন।
  - পুরনো `setTargetFragment()` deprecated। এর বদলেই Fragment Result API এসেছে।

```kotlin
// Picker screen: send the result, then go back
setFragmentResult("camera_pick", bundleOf("cameraId" to cameraId))
findNavController().popBackStack()

// Caller screen: listen with the same key (in onCreate)
setFragmentResultListener("camera_pick") { _, bundle ->
    viewModel.onCameraPicked(bundle.getString("cameraId"))
}

// Two screens in one flow share one ViewModel
private val checkoutVm: CheckoutViewModel by navGraphViewModels(R.id.checkout_graph)
```

**Flutter mapping:** constructor argument ≈ navigation argument; `Navigator.pop(context, result)` ≈ Fragment Result; একাধিক screen-এ একই Provider/Bloc ≈ shared ViewModel।

**Answer (English):**
> "To give input to a new screen, I pass a small navigation argument, usually just an id, and the next screen loads the data itself. To send back a one-time result, like a picked camera, I use the Fragment Result API, or the previous back stack entry's SavedStateHandle in Compose Navigation. When two screens work on the same data, like steps in one flow, I use a shared ViewModel scoped to the nav graph. I never keep a direct reference to another Fragment. Fragments are recreated on rotation and process death, so that reference can point to a dead object, leak memory, or crash. Arguments and results go through a Bundle, so they also survive process death."

**Key words:** `navigation arguments` · `Fragment Result API` · `setFragmentResultListener` · `activityViewModels` · `navGraphViewModels` · `SavedStateHandle`

**Follow-up:**
- **Q:** Why pass only an id and not the whole object?
  **A:** "Arguments go into a Bundle, so a big object can cause TransactionTooLargeException. With an id, the next screen reads fresh data from the single source of truth."
- **Q:** When is a shared ViewModel the wrong choice?
  **A:** "When the screens are not really one flow. An Activity-scoped ViewModel lives until the Activity ends, so it can keep old data and grow into one big shared object. I use the smallest scope, like a nav graph."
- **Q:** How does a dialog send a result to the screen that opened it?
  **A:** "With the Fragment Result API. The dialog sets a result with a key, and the caller listens with the same key. The caller gets it when it is at least started."

**ভুল করবেন না:** `(activity as MainActivity).otherFragment.update()` ধরনের code — rotation বা process death-এর পর পুরনো object-এ লেখা হবে।

**আরও দেখুন:** [C3 · Fragment lifecycle](#c3) · [U8 · Compose navigation](#u8) · [R1 · ViewModel](#r1)

---

### <a id="c4"></a>C4. ★ What is the difference between a configuration change and process death? How do you keep state?

**প্রশ্নটা মানে:** কোন ক্ষেত্রে কী হারায়, আর ViewModel, SavedStateHandle, rememberSaveable কোনটা কী বাঁচায় — আর আপনি এটা test করেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Does a ViewModel survive process death?" · "How do you test that your app restores state correctly?"

**বুঝে নিন:**
- **Configuration change** — rotation, dark mode, language, font size, window resize (foldable, multi-window)। Default-এ Activity destroy হয়ে নতুন করে তৈরি হয়। **Process বেঁচে থাকে।**
- **Process death** — app background-এ, memory দরকার, system process মেরে দিল। User Recents থেকে ফিরে এলে system **নতুন process** বানায়, task আর back stack ফিরিয়ে দেয়, saved Bundle দেয়। Memory-র সব object গেছে।

| জিনিস | Config change | Process death |
|---|---|---|
| ViewModel-এর field | ✅ থাকে | ❌ যায় |
| `SavedStateHandle` | ✅ | ✅ (Bundle-এ save হয়) |
| `rememberSaveable` | ✅ | ✅ |
| `remember` | ❌ | ❌ |
| Room / DataStore / file | ✅ | ✅ |

- ViewModel কেন বাঁচে: `ViewModelStore` config change-এর সময় retain করা হয় (non-config instance)। Process মরলে memory সহ সব যায়।
- **কী কোথায় রাখবেন:**
  - ছোট UI state (search text, selected tab, item id) → `SavedStateHandle` / `rememberSaveable`।
  - আসল data (list, user) → disk (Room/DataStore), id দিয়ে আবার load।
  - Bundle-এ বড় data (bitmap, পুরো list) রাখবেন না। Binder transaction buffer প্রায় 1MB, process-এর সব transaction মিলে (F3)। বেশি হলে `TransactionTooLargeException`। Google saved state 50KB-এর নিচে রাখতে বলে।
- `android:configChanges` দিয়ে recreate বন্ধ করা যায়, কিন্তু তখন সব change নিজে handle করতে হয়। Video player বা camera preview-এর মতো জায়গায় কখনো ব্যবহার হয়। সাধারণ fix হিসেবে না।
- Target 36 হলে বড় screen-এ (≥600dp) orientation lock কাজ করে না। Target 37-এ এর opt-out-ও নেই। তাই resize আর config change আরও বেশি হবে। State ঠিকমতো রাখা এখন বাদ দেওয়ার উপায় নেই।

```kotlin
class SearchViewModel(private val state: SavedStateHandle) : ViewModel() {
    val query: StateFlow<String> = state.getStateFlow("query", "")
    fun onQueryChange(q: String) { state["query"] = q }
}
```

**Process death test করার উপায়:**
1. App চালান, কোনো screen-এ state বানান, **Home চাপুন** (app background-এ)।
2. `adb shell am kill <package>` — শুধু background-এ থাকা process মারে।
3. Recents থেকে app খুলুন → state ফিরে এল কিনা দেখুন।
- অথবা Developer options → **"Don't keep activities"** — Activity stop হলেই destroy হয়। এটা Activity recreate test করে, পুরো process death না। দুটোই চেক করুন।
- Recents থেকে swipe করে বন্ধ করলে task-ই মুছে যায় — সেটা process death test না।
- Android Studio-র Logcat-এ "Terminate application" বাটনও কাজে লাগে (app background-এ থাকতে)।

**Answer (English):**
> "In a configuration change, like rotation or a window resize, the Activity is recreated but the process stays alive. In process death, the system kills the whole process while the app is in the background, and later restores the task with a saved Bundle. A ViewModel survives configuration changes, but not process death. So I keep small UI state, like a query or a selected id, in SavedStateHandle or rememberSaveable, and real data in Room or DataStore. I don't put big objects in the Bundle, because of TransactionTooLargeException. To test, I put the app in the background and run adb shell am kill, then reopen it from Recents."

**Key words:** `process death` · `SavedStateHandle` · `rememberSaveable` · `ViewModelStore` · `am kill` · `TransactionTooLargeException`

**Follow-up:**
- **Q:** Why not just set android:configChanges for everything?
  **A:** "Then I must handle every change myself, like new resources for dark mode or language. It also hides the real problem, because process death will still lose the state."
- **Q:** Does "Don't keep activities" test process death?
  **A:** "Not fully. It destroys Activities when they stop, but the process and singletons stay alive. For real process death I use am kill."
- **Q:** What happens to a running coroutine in viewModelScope on rotation?
  **A:** "It keeps running, because the ViewModel survives. On process death it is gone, so long work should go to WorkManager."

**ভুল করবেন না:** "ViewModel সব কিছু বাঁচায়" — না, process death-এ ViewModel-ও যায়।

**আরও দেখুন:** [R1 · ViewModel](#r1) · [U3 · Compose state](#u3) · [F3 · Binder limit](#f3)

---

### <a id="c5"></a>C5. ★ What is the difference between explicit and implicit intents? What is a PendingIntent?

**প্রশ্নটা মানে:** Intent কীভাবে target খুঁজে পায়, intent filter কী করে, আর PendingIntent-এর security নিয়ম (mutability flag) জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How does Android decide which app opens a link?" · "Why must a PendingIntent be immutable?"

**বুঝে নিন:**
- **Explicit intent** — target class/package নিজে বলে দেন। নিজের app-এর ভেতরে সবসময় এটা।
  `Intent(this, DetailActivity::class.java)`
- **Implicit intent** — শুধু action, data, category বলেন। System সব app-এর **intent filter** মিলিয়ে দেখে। একাধিক মিললে chooser।
  `Intent(Intent.ACTION_VIEW, uri)`
- **Intent filter** — manifest-এ `<action>`, `<category>`, `<data>`। Activity-কে implicit intent পেতে হলে `CATEGORY_DEFAULT` লাগে।
- Android 12+: intent filter থাকলে `android:exported` লিখতেই হবে।
- Android 14+ (target 34): implicit intent শুধু **exported** component-এ যায়। নিজের non-exported component-এ পাঠাতে চাইলে explicit করুন (`setPackage` বা class)।
- অন্য app-এর জন্য implicit intent পাঠানোর আগে Android 11+ এ package visibility (`<queries>`) লাগতে পারে (C14)।

**PendingIntent:**
- একটা token। অন্য process (NotificationManager, AlarmManager, অন্য app) **আপনার app-এর identity আর permission নিয়ে** পরে intent চালায়।
- Notification click, alarm, widget, geofence — সব জায়গায়।
- Android 12+ (target 31): `FLAG_IMMUTABLE` বা `FLAG_MUTABLE` বলতেই হবে। Default হিসেবে **IMMUTABLE** দিন।
- MUTABLE শুধু তখন যখন অন্য পক্ষ intent-এ data যোগ করবে — যেমন inline reply, bubble, কিছু location/geofence API।
- Android 14+ (target 34): **mutable PendingIntent + implicit intent** = exception। কারণ অন্য app intent বদলে আপনার নামে যেকোনো জায়গায় পাঠাতে পারত।
- `requestCode` আর intent-এর equality দিয়ে PendingIntent চেনা হয় — extras আলাদা হলেও একই PendingIntent ফেরত আসতে পারে। তাই আলাদা notification-এর জন্য আলাদা requestCode, আর দরকারে `FLAG_UPDATE_CURRENT`।

```kotlin
val intent = Intent(context, CameraDetailActivity::class.java)
    .putExtra("cameraId", cameraId)
val pi = PendingIntent.getActivity(
    context, cameraId.hashCode(), intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)
```

**Answer (English):**
> "An explicit intent names the exact component, so I use it inside my own app. An implicit intent only says the action and data, and the system matches it against intent filters of all apps. A PendingIntent is a token that lets another process, like the notification system or AlarmManager, run my intent later with my app's identity. Because of that, it is a security risk. Since Android 12 I must set FLAG_IMMUTABLE or FLAG_MUTABLE, and I use immutable by default. I use mutable only when the other side must fill in data, like inline reply. Since Android 14, a mutable PendingIntent with an implicit intent throws an exception."

**Key words:** `explicit` · `implicit` · `intent filter` · `exported` · `FLAG_IMMUTABLE` · `requestCode`

**Follow-up:**
- **Q:** Why is a mutable PendingIntent dangerous?
  **A:** "Another app can change the inner intent and run it with my identity and permissions. For example, it could reach my private components or my content provider."
- **Q:** Why did two notifications open the same data?
  **A:** "PendingIntents with the same request code and an equal intent are treated as the same one. Extras are not part of that check. So I use a different request code per item."
- **Q:** What happens if no app can handle an implicit intent?
  **A:** "startActivity throws ActivityNotFoundException. I catch it, or I check first with resolveActivity, which may need a queries entry on Android 11 and newer."

**ভুল করবেন না:** সব জায়গায় `FLAG_MUTABLE` দেওয়া "কারণ crash বন্ধ হয়" — এটা security hole।

**আরও দেখুন:** [F7 · Intent resolution](#f7) · [C16 · App Links](#c16) · [S9 · Secure components](#s9)

---

### <a id="c6"></a>C6. ◆ What are tasks and launch modes?

**প্রশ্নটা মানে:** Back stack কীভাবে কাজ করে, আর notification বা deep link থেকে খুললে duplicate screen কীভাবে এড়াবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between singleTop and singleTask?" · "How do you avoid opening the same screen twice from a notification?"

**বুঝে নিন:**
- **Task** — activity-দের একটা stack, যা user একটা কাজ হিসেবে দেখে। Recents-এ প্রতিটা task আলাদা কার্ড।
- **Launch mode** (manifest-এ `android:launchMode`):

| Mode | কী হয় |
|---|---|
| `standard` | প্রতিবার নতুন instance (default) |
| `singleTop` | একই activity যদি stack-এর **ওপরে** থাকে, নতুন না বানিয়ে `onNewIntent()` |
| `singleTask` | পুরো system-এ একটাই instance, নিজের task-এর root। থাকলে তার ওপরের সব clear করে `onNewIntent()` |
| `singleInstance` | singleTask-এর মতো, কিন্তু task-এ শুধু সে একা |
| `singleInstancePerTask` | Android 12+; প্রতি task-এ একটা instance, root হিসেবে |

- **Intent flags** — call site থেকে একই কাজ:
  - `FLAG_ACTIVITY_NEW_TASK` — Activity ছাড়া context (Service, Application) থেকে start করলে লাগে।
  - `FLAG_ACTIVITY_CLEAR_TOP` — target আগে থাকলে ওপরের সব সরায়।
  - `FLAG_ACTIVITY_SINGLE_TOP` — singleTop-এর মতো।
  - `FLAG_ACTIVITY_CLEAR_TASK` + `NEW_TASK` — logout-এর পর পুরো stack মুছে login screen।
- `onNewIntent()`-এ নতুন data নিতে `setIntent(intent)` করুন বা সরাসরি process করুন। Compose-এ `addOnNewIntentListener`।
- Single-activity + Compose app-এ বেশিরভাগ navigation Navigation library-র back stack-এ। Launch mode তখন মূলত notification/deep link-এর জন্য (প্রায়ই `singleTop`)।
- `taskAffinity` ঠিক করে activity কোন task-এ যাবে। ভুল affinity দিলে অন্য app আপনার task-এ নিজের screen ঢোকাতে পারে (task hijacking)। নতুন Android version-গুলো এটা আটকাতে নিয়ম কড়া করেছে।

**Answer (English):**
> "A task is a stack of activities that the user sees as one job in Recents. The launch mode decides if a new instance is created. standard always creates a new one. singleTop reuses the activity only if it is already on top, and calls onNewIntent. singleTask keeps one instance as the root of its task and clears everything above it. singleInstance is the same but alone in its task. In a single-activity Compose app, I mostly use singleTop, so a notification or deep link does not stack the same screen twice. Then I handle the new data in onNewIntent."

**Key words:** `task` · `back stack` · `singleTop` · `onNewIntent` · `FLAG_ACTIVITY_NEW_TASK` · `taskAffinity`

**Follow-up:**
- **Q:** Why do you need FLAG_ACTIVITY_NEW_TASK when starting from a Service?
  **A:** "A Service has no task of its own. The system needs to know which task to put the activity in, so I must ask for a new task."
- **Q:** How do you clear the back stack after logout?
  **A:** "I start the login screen with FLAG_ACTIVITY_NEW_TASK and FLAG_ACTIVITY_CLEAR_TASK. In Compose navigation, I pop up to the start destination with inclusive set to true."

**ভুল করবেন না:** singleTop আর singleTask গুলিয়ে ফেলা — singleTop শুধু "ওপরে থাকলে" reuse করে।

**আরও দেখুন:** [C5 · Intents](#c5) · [C16 · Deep links](#c16) · [U8 · Compose navigation](#u8)

---

### <a id="c7"></a>C7. ★ What types of Services are there? What are foreground service types?

**প্রশ্নটা মানে:** Started, bound, foreground service-এর পার্থক্য, আর Android 12/14/15-এর নতুন কড়া নিয়ম জানেন কিনা — camera app-এ এটা রোজের কাজ।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you keep recording camera video when the app goes to the background?" · "What changed for foreground services in Android 14?"

**বুঝে নিন:**
- **Started service** — `startService()`; কাজ শেষে `stopSelf()`। Android 8+ এ background থেকে প্রায় চালানো যায় না (`IllegalStateException`)।
- **Bound service** — `bindService()`; client-রা `IBinder` দিয়ে method call করে। শেষ client unbind করলে service শেষ।
  - একই app-এ সাধারণ `Binder`। অন্য process বা app-এ **AIDL** বা `Messenger`।
  - Custom OS / system service-এর কাজে AIDL খুব কমন।
- **Foreground service (FGS)** — চলমান notification দেখাতে হয়। User জানে কিছু চলছে, তাই system সহজে মারে না।
  - `startForegroundService()` এর পর কয়েক সেকেন্ডের মধ্যে (docs বলে "a few seconds"; বাস্তবে প্রায় 5s) `startForeground()` না ডাকলে ANR/crash।
  - Compat: `ServiceCompat.startForeground(service, id, notification, type)`।

**Android 14 (target 34) — type লাগবেই:**
- Manifest-এ `android:foregroundServiceType` + মিলানো permission: `FOREGROUND_SERVICE_CAMERA`, `..._MICROPHONE`, `..._LOCATION`, `..._DATA_SYNC`, `..._MEDIA_PLAYBACK`, `..._CONNECTED_DEVICE`, `..._HEALTH`, `..._SPECIAL_USE` ইত্যাদি। (সাধারণ `FOREGROUND_SERVICE` permission-ও লাগে।)
- Runtime prerequisite: `camera` type-এর জন্য `CAMERA` permission আগে granted থাকতে হবে, নইলে `SecurityException`।
- `shortService` — ছোট জরুরি কাজ, প্রায় ৩ মিনিট limit, permission লাগে না।
- `specialUse` হলে Play Console-এ কারণ লিখতে হয়।
- Play Console-এ প্রতিটা FGS type কেন লাগছে declare করতে হয় (ভিডিও সহ)।

**Android 12 (target 31) — background থেকে FGS start প্রায় বন্ধ:**
- `ForegroundServiceStartNotAllowedException`।
- Exception আছে: app-এর visible activity থাকলে, user notification-এ tap করলে, high-priority FCM পেলে, exact alarm থেকে, `BOOT_COMPLETED`-এর মতো কিছু broadcast, companion device ইত্যাদি।
- বিকল্প: WorkManager **expedited** work।

**Android 15 (target 35):**
- `dataSync` আর নতুন `mediaProcessing` — প্রতিটা type ২৪ ঘণ্টায় মোট ৬ ঘণ্টা চলতে পারে (একই type-এর সব service মিলিয়ে)।
- সময় শেষ হলে `Service.onTimeout(int, int)` আসে। কয়েক সেকেন্ডে `stopSelf()` না করলে crash।
- User app সামনে আনলে timer আবার শূন্য থেকে শুরু হয়।
- `BOOT_COMPLETED` receiver থেকে `camera`, `microphone`, `dataSync`, `mediaPlayback`, `phoneCall`, `mediaProjection` FGS চালানো যাবে না।
- `SYSTEM_ALERT_WINDOW` থাকলেই আর background-এ FGS চালানো যায় না — একটা **visible overlay window** থাকতে হবে।

**Camera app practical:**
- Background-এ recording চালাতে `camera` (+ দরকারে `microphone`) type FGS, user action থেকে শুরু করুন (app সামনে থাকা অবস্থায়)।
- Android 9+ এ background app camera ব্যবহার করতে পারে না — FGS-ই উপায়।
- Boot-এর পর auto-recording সাধারণ app-এ Android 15+ এ এভাবে হবে না। Dedicated device / custom OS-এ system বা privileged app হিসেবে ভিন্ন পথ লাগে (AOSP অংশে আলাদা করে আছে)।

```xml
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_CAMERA" />
<service android:name=".RecordService"
    android:foregroundServiceType="camera|microphone"
    android:exported="false" />
```

**Answer (English):**
> "There are started services, bound services, and foreground services. A started service runs a task and stops itself. A bound service gives clients an interface through a Binder, or AIDL across processes. A foreground service shows an ongoing notification, so the system keeps it alive. Since Android 14, every foreground service needs a type, like camera or dataSync, plus the matching permission. Since Android 12, I mostly cannot start one from the background, so I start it from a user action or use expedited WorkManager. Android 15 added a six-hour daily limit for dataSync, and boot receivers cannot start camera or microphone services. For background camera recording, I use a camera-type service started while the app is visible."

**Key words:** `startForeground` · `foregroundServiceType` · `FOREGROUND_SERVICE_CAMERA` · `ForegroundServiceStartNotAllowedException` · `onTimeout` · `AIDL`

**Follow-up:**
- **Q:** What happens if you call startForegroundService but never call startForeground?
  **A:** "The system throws an error and the app gets an ANR or crash after a few seconds. So I call startForeground right at the start of onStartCommand."
- **Q:** When would you use a bound service?
  **A:** "When a client needs a live connection and calls methods, like a UI that controls a camera session, or a system service that other apps use through AIDL."
- **Q:** Can the user stop your foreground service?
  **A:** "Yes. Since Android 13 there is a Task Manager in quick settings where the user can stop apps with foreground services. So my service must handle being stopped cleanly."

**ভুল করবেন না:** "Notification দিলেই FGS যেকোনো সময় চালাতে পারি" — Android 12+ এ background start বন্ধ, Android 14+ এ type ছাড়া চলবে না।

**আরও দেখুন:** [C10 · Background work](#c10) · [V2 · Camera in background](#v2) · [V11 · 24/7 recording](#v11)

---

### <a id="c8"></a>C8. ◆ How do BroadcastReceivers work today?

**প্রশ্নটা মানে:** Manifest আর runtime receiver-এর পার্থক্য, আর Android 8/14-এর limit জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why does my manifest receiver not get CONNECTIVITY_CHANGE anymore?" · "How do you start something after the device boots?"

**বুঝে নিন:**
- **Manifest-declared** — app না চললেও system process চালু করে receiver ডাকে।
  - Android 8+ (target 26): বেশিরভাগ **implicit** broadcast manifest receiver পায় না। Exception list আছে: `BOOT_COMPLETED`, `LOCKED_BOOT_COMPLETED`, `LOCALE_CHANGED`, `MY_PACKAGE_REPLACED`, কিছু USB/SMS ইত্যাদি।
  - Network change ইত্যাদির জন্য: `ConnectivityManager.NetworkCallback` বা WorkManager constraint।
- **Context-registered** — `registerReceiver()`। Component যতক্ষণ বেঁচে থাকে ততক্ষণ পায়। Unregister করতেই হবে (`onStart`-এ register, `onStop`-এ unregister)।
  - Android 14 (target 34): `RECEIVER_EXPORTED` বা `RECEIVER_NOT_EXPORTED` flag দিতেই হবে (system broadcast ছাড়া)। Compat: `ContextCompat.registerReceiver(..., ContextCompat.RECEIVER_NOT_EXPORTED)`।
- `onReceive()` main thread-এ চলে। ছোট রাখুন। বেশি কাজ → `goAsync()` (কয়েক সেকেন্ড) বা WorkManager। `goAsync()` এর পর `finish()` না ডাকলে ANR।
- **BOOT_COMPLETED**: `RECEIVE_BOOT_COMPLETED` permission। User একবার app না খুললে (stopped state) receiver পাবে না। Direct Boot (unlock-এর আগে) চাইলে `LOCKED_BOOT_COMPLETED` আর `directBootAware`। Android 15 এ boot receiver থেকে কিছু FGS type নিষেধ (C7)।
- নিজের app-এর ভেতরে event-এর জন্য broadcast না — `SharedFlow`/repository। (`LocalBroadcastManager` deprecated।)
- Sensitive broadcast পাঠাতে permission দিয়ে সুরক্ষা: `sendBroadcast(intent, "my.permission")`, permission `signature` level।

**Answer (English):**
> "A manifest receiver can start my app even when it is not running. A context-registered receiver works only while my component is alive, and I must unregister it. Since Android 8, most implicit broadcasts are not delivered to manifest receivers, to save battery. Boot completed and a few others are still allowed. For network changes I use NetworkCallback instead. Since Android 14, when I register at runtime, I must say RECEIVER_EXPORTED or RECEIVER_NOT_EXPORTED. onReceive runs on the main thread, so I keep it short and hand longer work to WorkManager."

**Key words:** `implicit broadcast` · `RECEIVER_NOT_EXPORTED` · `goAsync` · `BOOT_COMPLETED` · `LOCKED_BOOT_COMPLETED` · `NetworkCallback`

**Follow-up:**
- **Q:** Why might BOOT_COMPLETED not arrive after install?
  **A:** "A freshly installed app is in the stopped state until the user opens it once. Until then, it gets no broadcasts. Force stop by the user also puts it back in that state."
- **Q:** How do you protect your broadcast from other apps?
  **A:** "I use an explicit intent with setPackage, or require a signature-level permission. For receivers, I use RECEIVER_NOT_EXPORTED or exported false."

**ভুল করবেন না:** App-এর ভেতরের event-এর জন্য broadcast ব্যবহার করা — Flow যথেষ্ট।

**আরও দেখুন:** [C10 · Background work](#c10) · [S9 · Secure components](#s9)

---

### <a id="c9"></a>C9. ◆ What is a ContentProvider, and why do we need FileProvider?

**প্রশ্নটা মানে:** App-দের মধ্যে data/file নিরাপদে share করার নিয়ম, আর `file://` কেন বন্ধ — এটা বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you share a recorded video with another app?" · "What is FileUriExposedException?"

**বুঝে নিন:**
- **ContentProvider** — `content://authority/path` URI দিয়ে data দেয়। `query`, `insert`, `update`, `delete`, `openFile`। Client `ContentResolver` দিয়ে কথা বলে, process আলাদা হলেও।
- কোথায় দেখবেন: MediaStore, Contacts, Calendar, `Settings` — সব provider।
- নিজের app-এর ভেতরে data-র জন্য provider লাগে না — Room সরাসরি।
- Provider-এর `onCreate()` **`Application.onCreate()`-এর আগে** চলে। তাই App Startup library provider দিয়ে init করে। এখানে ভারী কাজ = ধীর app start।
- **FileProvider** — ContentProvider-এর তৈরি subclass। নিজের private file-কে `content://` URI বানিয়ে দেয়।
- **`file://` কেন বন্ধ:** Android 7 (target 24) থেকে অন্য app-কে `file://` URI দিলে `FileUriExposedException`। কারণ:
  - Receiver app-এর আপনার file পড়ার Linux permission নেই।
  - File-কে world-readable করলে সবাই পড়তে পারে — security hole।
  - `content://` URI-তে **temporary, নির্দিষ্ট permission** দেওয়া যায়: `FLAG_GRANT_READ_URI_PERMISSION`। কাজ শেষে চলে যায়।

```kotlin
val uri = FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", videoFile)
val share = Intent(Intent.ACTION_SEND).apply {
    type = "video/mp4"
    putExtra(Intent.EXTRA_STREAM, uri)
    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
}
startActivity(Intent.createChooser(share, null))
```
- Manifest-এ provider `exported="false"`, `grantUriPermissions="true"`, আর `res/xml/file_paths.xml`-এ কোন folder share হবে লিখুন। পুরো root share করবেন না।

**Answer (English):**
> "A ContentProvider shares data through content URIs, and other apps access it with ContentResolver, even from another process. MediaStore and Contacts are providers. FileProvider is a ready-made provider that turns my private files into content URIs. Since Android 7, sharing a file URI with another app throws FileUriExposedException. The reason is security. The other app has no Linux permission to read my file, and making it world-readable would let every app read it. With a content URI, I grant read access only to that app, only for that file, and only for a short time. I keep the provider not exported and limit the shared paths."

**Key words:** `content URI` · `ContentResolver` · `FileProvider` · `FLAG_GRANT_READ_URI_PERMISSION` · `FileUriExposedException` · `authority`

**Follow-up:**
- **Q:** Does a ContentProvider slow down app start?
  **A:** "It can. Providers are created before Application.onCreate. Many libraries used providers for auto-init, so the App Startup library merges them into one."
- **Q:** What is a common security bug with providers?
  **A:** "An exported provider without permissions, or path traversal in openFile. I keep providers not exported, or protect them with a signature permission and check paths."

**আরও দেখুন:** [C17 · Storage](#c17) · [S9 · Secure components](#s9)

---

### <a id="c10"></a>C10. ★ Which tool do you use for background work?

**প্রশ্নটা মানে:** কাজের ধরন দেখে WorkManager, foreground service, AlarmManager, নাকি শুধু coroutine — ঠিক বাছতে পারেন কিনা, আর Doze/Standby বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you upload camera clips reliably in the background?" · "What is Doze and how does it affect your app?"

**বুঝে নিন:**
**সিদ্ধান্তের ধাপ:**
1. কাজটা কি শুধু screen খোলা থাকা পর্যন্ত? → **coroutine** (`viewModelScope` / `lifecycleScope`)।
2. App বন্ধ বা restart হলেও কাজটা **অবশ্যই** শেষ হতে হবে, কিন্তু একটু পরে হলেও চলে? → **WorkManager** (persistent; reboot-এর পরেও থাকে; constraint, retry, chaining)।
3. এখনই শুরু হতে হবে, ছোট কাজ? → WorkManager **expedited** (`setExpedited(OutOfQuotaPolicy.RUN_AS_NON_EXPEDITED_WORK_REQUEST)`)।
4. User জানে আর চলমান কাজ — recording, navigation, music, call? → **foreground service** সঠিক type দিয়ে।
5. নির্দিষ্ট সময়ে ঘড়ি ধরে (alarm clock, reminder)? → **AlarmManager**। Exact হলে permission লাগে।
6. বড় user-শুরু করা download/upload? → Android 14+ এ **user-initiated data transfer job** (JobScheduler) একটা বিকল্প।

| Tool | কখন | সীমা |
|---|---|---|
| Coroutine | UI-র সাথে বাঁধা কাজ | process মরলে শেষ |
| WorkManager | কাজ শেষ হবেই, তবে পরে চলতে পারে | কখন চলবে system ঠিক করে; Doze/bucket মানে |
| Expedited work | এখনই, ছোট | quota আছে; Android 12+ এ expedited job, তার আগে FGS হিসেবে চলে (`getForegroundInfo` লাগে) |
| Foreground service | user-visible, লম্বা | type + permission; background start নিষেধ |
| AlarmManager | নির্দিষ্ট সময় | exact alarm-এ `SCHEDULE_EXACT_ALARM`/`USE_EXACT_ALARM` |

**Doze আর App Standby:**
- **Doze** — screen off, charger নেই, device স্থির। Network বন্ধ, job/alarm/wakelock পিছিয়ে যায়। মাঝে মাঝে ছোট **maintenance window**। Light doze (চলাফেরা করলেও) আর deep doze আছে।
- Doze-এর মধ্যে জাগাতে: high-priority FCM, `setExactAndAllowWhileIdle()` (সীমিত)।
- **App Standby buckets** (Android 9+): Active, Working set, Frequent, Rare, Restricted (Android 12-এ যোগ)। কম ব্যবহৃত app-এর job আর alarm কম চলে। Restricted-এ দিনে প্রায় একবার job আর একটা alarm।
- Check: `adb shell am get-standby-bucket <package>`। Doze test: `adb shell dumpsys deviceidle force-idle`।
- Exact alarm: Android 12 থেকে `SCHEDULE_EXACT_ALARM` (user বন্ধ করতে পারে), Android 14 এ নতুন install-এ default **denied**। `USE_EXACT_ALARM` শুধু alarm clock/calendar ধরনের app (Play policy)। `canScheduleExactAlarms()` চেক করুন।
- কিছু OEM (ফোন brand) নিজের কড়া battery killer যোগ করে। তখন WorkManager-ও দেরি করতে পারে। এটা সত্যি সমস্যা। এটা লিখে রাখুন, আর দরকার হলে user-কে ঠিক settings দেখান।

```kotlin
val upload = OneTimeWorkRequestBuilder<UploadClipWorker>()
    .setConstraints(Constraints(requiredNetworkType = NetworkType.UNMETERED))
    .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
    .setInputData(workDataOf("clipId" to clipId))
    .build()
WorkManager.getInstance(context)
    .enqueueUniqueWork("upload-$clipId", ExistingWorkPolicy.KEEP, upload)
```

**Answer (English):**
> "I choose by two questions: must the work finish if the app dies, and must it run right now? If it is tied to the screen, I use a coroutine in viewModelScope. If it must finish but can wait, like uploading a clip, I use WorkManager, because it survives restarts and follows the Doze rules. For short urgent work I use expedited WorkManager. If the user knows it is running, like live recording, I use a foreground service with the right type. AlarmManager is only for exact times, and exact alarms now need a permission. The trade-off is that WorkManager timing is not exact, because Doze and standby buckets delay it."

**Key words:** `WorkManager` · `expedited` · `Doze` · `maintenance window` · `App Standby buckets` · `SCHEDULE_EXACT_ALARM` · `unique work`

**Follow-up:**
- **Q:** Is WorkManager good for work every 5 minutes?
  **A:** "No. The minimum periodic interval is 15 minutes, and the system can delay it more. For continuous work I need a foreground service, or better, push from the server."
- **Q:** How do you test Doze?
  **A:** "I use adb shell dumpsys deviceidle force-idle, and I set a standby bucket with am set-standby-bucket. Then I check that work runs after the idle state ends."
- **Q:** Should you ask users to ignore battery optimization?
  **A:** "Only if it is the core function, and Google Play limits that permission. Most apps should work inside the rules with WorkManager and FCM."

**ভুল করবেন না:** "Background-এ thread চালিয়ে রাখি" বা "Service-এ while(true)" — modern Android-এ এটা মারা যাবে আর interview-এ বড় red flag।

**আরও দেখুন:** [C7 · Services](#c7) · [P7 · Battery](#p7) · [D5 · Big upload](#d5)

---

### <a id="c11"></a>C11. ★ What is Context? How do Context leaks happen?

**প্রশ্নটা মানে:** Application আর Activity context কখন কোনটা, আর memory leak কীভাবে হয় ও ধরেন — জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "When should you use applicationContext?" · "How do you find and fix memory leaks?"

**বুঝে নিন:**
- `Context` — app-এর environment-এর handle: resource, file, system service, theme, component start করা।
- **Application context** — process যতক্ষণ, ততক্ষণ বেঁচে থাকে। Theme/UI জানে না।
- **Activity context** — Activity-র সাথে মরে। Theme, window, configuration (dark mode, locale) জানে।

| কাজ | কোন context |
|---|---|
| Dialog, view inflate, theme-সহ UI | Activity |
| Singleton, Room, DataStore, WorkManager, repository | Application |
| `startActivity` | Activity ভালো (Application থেকে করলে `NEW_TASK` লাগে) |
| Toast | যেকোনো, তবে Application নিরাপদ |

**Leak কীভাবে হয়:** কোনো লম্বা-জীবনের object যদি Activity-কে ধরে রাখে, Activity destroy হলেও GC তুলতে পারে না। পুরো view tree + bitmap memory-তে থেকে যায়।
- Singleton বা `companion object`-এ Activity/View রাখা।
- Listener/callback register করে unregister না করা (sensor, location, receiver)।
- Activity-র ভেতরের non-static inner class বা lambda যা লম্বা সময় চলে (পুরনো Handler pattern, thread)।
- `GlobalScope`-এ coroutine যা Activity ধরে রাখে।
- ViewModel-এ Activity, View বা Activity context রাখা — ViewModel Activity-র চেয়ে বেশি বাঁচে।
- Fragment-এ binding null না করা (C3)।

**ধরবেন কীভাবে:**
- **LeakCanary** (debug build) — destroyed Activity/Fragment/ViewModel retain হলে leak trace দেখায়।
- Android Studio Memory Profiler — heap dump, "Activity/Fragment leaks" filter।

**ঠিক করার উপায়:** লম্বা-জীবনের জায়গায় `applicationContext`; lifecycle-aware observer; `viewModelScope`/`lifecycleScope`; DI (Hilt-এ `@ApplicationContext`)।

**Answer (English):**
> "Context gives access to resources, system services, and starting components. The Application context lives as long as the process. The Activity context dies with the Activity, but it knows the theme and configuration. So I use the Activity context for UI, like dialogs and inflating views, and the Application context for long-lived things like repositories and databases. A leak happens when something long-lived holds an Activity, like a singleton, a static field, an unregistered listener, or a ViewModel that keeps a View. Then the whole view tree stays in memory. I find leaks with LeakCanary in debug builds."

**Key words:** `applicationContext` · `Activity context` · `memory leak` · `LeakCanary` · `heap dump` · `@ApplicationContext`

**Follow-up:**
- **Q:** Why not use the Application context everywhere?
  **A:** "It has no theme and no Activity configuration. Inflating views or showing a dialog with it gives wrong styling or crashes."
- **Q:** Can a ViewModel have a Context?
  **A:** "It should not hold an Activity context. If it really needs one, AndroidViewModel gives the Application, but I prefer to inject a repository that hides it."
- **Q:** How does LeakCanary know there is a leak?
  **A:** "It watches objects that should be gone, like destroyed Activities. If they are still reachable after GC, it dumps the heap and shows the reference chain."

**ভুল করবেন না:** "Leak এড়াতে সব জায়গায় applicationContext" — UI-তে ভুল theme আর crash হবে।

**আরও দেখুন:** [P2 · Memory leaks](#p2) · [F9 · Memory](#f9)

---

### <a id="c12"></a>C12. ★ How does the main thread work (Looper, Handler, MessageQueue)? What is an ANR?

**প্রশ্নটা মানে:** Android-এর event loop কীভাবে চলে, আর ANR কেন হয়, কতক্ষণে হয়, কীভাবে খুঁজবেন — জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is a Looper?" · "What causes an ANR and how do you debug it?"

**বুঝে নিন:**
- Main thread একটা loop: **Looper** → **MessageQueue** থেকে একটা **Message** নেয় → তার **Handler**-এ পাঠায় → আবার পরেরটা।
- Input event, draw (Choreographer frame), lifecycle callback, `onReceive`, service callback — সব এই queue দিয়ে main thread-এ আসে।
- একটা message ধীর হলে পেছনের সব আটকে যায়: frame drop (jank), তারপর ANR।
- `Handler(Looper.getMainLooper()).post { }` — অন্য thread থেকে main-এ কাজ পাঠানো। No-arg `Handler()` deprecated।
- `HandlerThread` — নিজের Looper-সহ background thread। Camera2 callback-এর জন্য এখনো খুব কমন।
- Coroutine-এর `Dispatchers.Main` নিচে এই main Handler-ই ব্যবহার করে।
- Android 17-এ target 37 হলে নতুন **lock-free MessageQueue** — reflection দিয়ে MessageQueue-র ভেতরের field ধরা code ভেঙে যেতে পারে।

**ANR — কখন হয় (developer.android.com অনুযায়ী):**
| Trigger | সময় |
|---|---|
| Input event-এর উত্তর নেই | **5 সেকেন্ড** |
| BroadcastReceiver শেষ হয়নি | foreground broadcast **10 সেকেন্ড**, background broadcast **60 সেকেন্ড**। Android 14+-এ CPU চাপ থাকলে 10–20s আর 60–120s |
| Service `onCreate`/`onStartCommand`/`onBind` শেষ হয়নি | foreground service **20 সেকেন্ড**, background service **200 সেকেন্ড** (app-এর cold start-ও এর ভেতরে গোনা হয়) |
| `startForegroundService` এর পর `startForeground` হয়নি | **5 সেকেন্ড** (ANR docs-এ লেখা) |
| JobService `onStartJob`/`onStopJob` ফেরেনি | কয়েক সেকেন্ড |

(এগুলো AOSP আর Pixel-এর default। OEM device-এ আলাদা হতে পারে — interview-এ "about" বলুন।)

**কারণ:** main thread-এ disk/network I/O, ভারী হিসাব, অন্য process-এ ধীর sync binder call, lock-এর জন্য অপেক্ষা, deadlock।

**খুঁজবেন কীভাবে:**
- Play Console → Android vitals → ANR cluster আর stack trace। Bad-behaviour threshold: user-perceived ANR rate **0.47%**।
- `ApplicationExitInfo` (Android 11+) — আগের run কেন মরেছিল, ANR trace সহ।
- `StrictMode` (debug) — main thread-এ disk/network ধরলে log বা crash।
- `adb bugreport` বা `/data/anr/` trace; Perfetto trace।

**Answer (English):**
> "The main thread runs a Looper that takes messages from a MessageQueue one by one and gives each to its Handler. Input, drawing, and lifecycle callbacks all go through this queue. If one message takes too long, everything behind it waits. An ANR happens when input gets no response for 5 seconds, or a broadcast receiver or service callback does not finish in time, for example 10 seconds for a foreground broadcast. Common causes are disk or network on the main thread, heavy work, slow binder calls, and lock waits. I move I/O to Dispatchers.IO, turn on StrictMode in debug, and check Android vitals and ApplicationExitInfo in production."

**Key words:** `Looper` · `MessageQueue` · `Handler` · `HandlerThread` · `ANR` · `StrictMode` · `ApplicationExitInfo`

**Follow-up:**
- **Q:** Can a background thread have a Looper?
  **A:** "Yes. HandlerThread creates one. I use it for Camera2 callbacks or for an API that needs a Looper thread."
- **Q:** Can a coroutine cause an ANR?
  **A:** "Yes, if I do blocking work on Dispatchers.Main. A coroutine is not magic. Blocking I/O must use Dispatchers.IO."
- **Q:** Do ANRs affect the Play Store?
  **A:** "Yes. If the overall user-perceived ANR rate goes over 0.47 percent, Google Play can make the app less visible. If one device model goes over 8 percent, Play can also show a warning on the listing for that device."

**ভুল করবেন না:** "ANR মানে crash" — না, app আটকে আছে; system user-কে wait বা close করতে বলে।

**আরও দেখুন:** [P1 · ANR](#p1) · [K9 · Dispatchers](#k9) · [F10 · App threads](#f10)

---

### <a id="c13"></a>C13. ★ How do runtime permissions work?

**প্রশ্নটা মানে:** Permission চাওয়ার সঠিক flow, "denied forever" কীভাবে বুঝবেন, আর Android 11 থেকে 17 পর্যন্ত কী বদলেছে — জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you handle a user who denied camera permission?" · "What is shouldShowRequestPermissionRationale?"

**বুঝে নিন:**
**Permission-এর ধরন:** `normal` (install-এ পায়, যেমন INTERNET), `dangerous` (runtime-এ চাইতে হয়), `signature` (একই key-তে sign করা app পায়), আর system app-এর জন্য `privileged`।

**সঠিক flow:**
1. Feature-টা user চালু করার সময় চান (app খোলার সাথে সাথে সব না)।
2. `checkSelfPermission` → আছে? কাজ করুন।
3. নেই, আর `shouldShowRequestPermissionRationale()` **true** → আগে নিজের UI-তে কারণ বলুন, তারপর চান।
4. নইলে সরাসরি চান — Activity Result API দিয়ে।
5. Denied হলে feature-টা ছাড়া app চালু রাখুন।

**"Denied forever" বোঝা:**
- `shouldShowRequestPermissionRationale()` **প্রথমবার চাওয়ার আগেও false**, আর **স্থায়ীভাবে deny হলেও false**। তাই এটা একা যথেষ্ট না।
- Android 11+ এ user দুইবার deny করলে system আর dialog দেখায় না — launcher সাথে সাথে denied ফেরত দেয়।
- Practical: request-এর ফল denied **আর** rationale false হলে → "Settings-এ গিয়ে চালু করুন" UI দেখান (`Settings.ACTION_APPLICATION_DETAILS_SETTINGS`)।

```kotlin
private val cameraPermission =
    registerForActivityResult(ActivityResultContracts.RequestPermission()) { granted ->
        when {
            granted -> startPreview()
            !shouldShowRequestPermissionRationale(Manifest.permission.CAMERA) ->
                showOpenSettingsMessage()   // blocked: ask in Settings
            else -> showCameraNeededMessage()
        }
    }
// later, on button click: cameraPermission.launch(Manifest.permission.CAMERA)
```
- Launcher `onCreate`/field হিসেবে register করুন (STARTED-এর আগে), নইলে exception। Compose-এ `rememberLauncherForActivityResult`।
- পুরনো `onRequestPermissionsResult` deprecated পথ।

**Version অনুযায়ী বদল:**
| Version | বদল |
|---|---|
| Android 11 | one-time permission (location, camera, mic); দুইবার deny = আর dialog নেই; অনেকদিন ব্যবহার না হলে permission auto-reset; background location আলাদা ধাপে (Settings-এ) |
| Android 12 | approximate vs precise location; `BLUETOOTH_SCAN`/`CONNECT`/`ADVERTISE`; mic/camera indicator ও toggle |
| Android 13 | `POST_NOTIFICATIONS`; `READ_MEDIA_IMAGES`/`VIDEO`/`AUDIO`; `NEARBY_WIFI_DEVICES` |
| Android 14 | partial photo access (`READ_MEDIA_VISUAL_USER_SELECTED`); FGS type-এর runtime prerequisite |
| Android 17 | target 37 হলে LAN-এ device খুঁজতে/connect করতে **`ACCESS_LOCAL_NETWORK`** runtime permission (NEARBY_DEVICES group-এ) |

**Android 17 local network — camera app-এর জন্য খুব জরুরি:**
- IP camera খোঁজা (ONVIF/mDNS discovery), LAN-এ RTSP stream — target 37 হলে `ACCESS_LOCAL_NETWORK` লাগবে।
- Target 37-এর নিচে থাকলে আর `INTERNET` থাকলে app এটা নিজে থেকেই পায় (implicit grant)। Google বলেছে এটা কিছু দিনের জন্য।
- Target 37 করার আগে runtime-এ এই permission চাইবেন না — docs তাই বলে।
- `NsdManager` দিয়ে resolve করা address-এ connect করলে permission লাগে না (system picker পথ)।
- বিস্তারিত developer.android.com-এর "Local network permission" পাতায় মিলিয়ে নিন।

**Answer (English):**
> "I ask for a permission only when the user starts the feature that needs it. First I check if it is granted. If shouldShowRequestPermissionRationale is true, I explain why in my own UI, then I ask with the Activity Result API. If the result is denied and rationale is false, the user blocked it, so I show a button to open app settings. Since Android 11, two denials mean the dialog will not show again. Newer versions added more runtime permissions, like notifications in Android 13, partial photo access in 14, and local network access in Android 17. For a camera app, that last one matters for finding cameras on the LAN."

**Key words:** `dangerous permission` · `shouldShowRequestPermissionRationale` · `RequestPermission` · `one-time permission` · `ACCESS_LOCAL_NETWORK` · `app settings`

**Follow-up:**
- **Q:** How do you ask for background location?
  **A:** "First I get foreground location. Then I ask for ACCESS_BACKGROUND_LOCATION separately, and on Android 11 and newer the user must choose 'Allow all the time' in Settings. Google Play also needs a strong reason for it."
- **Q:** Can the system remove a permission you already have?
  **A:** "Yes. Auto-reset removes permissions from apps not used for months, and one-time permissions end when the app is closed. So I check every time, not once."
- **Q:** What breaks in a LAN camera app when you target Android 17?
  **A:** "Device discovery and direct LAN connections fail without ACCESS_LOCAL_NETWORK. I add the permission, ask for it at the right moment, and use NsdManager where it fits."

**ভুল করবেন না:** "rationale false মানে denied forever" — প্রথমবারেও false। ফলাফল আর rationale দুটো মিলিয়ে বুঝতে হয়।

**আরও দেখুন:** [F8 · Permission enforcement](#f8) · [V2 · Camera permissions](#v2) · [V7 · Find LAN cameras](#v7)

---

### <a id="c14"></a>C14. ◆ What are the AndroidManifest essentials?

**প্রশ্নটা মানে:** Manifest-এর security আর compatibility setting — exported, permission, queries, uses-feature — ঠিক জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between uses-permission and permission?" · "Why can't my app see other installed apps on Android 11?"

**বুঝে নিন:**
- **`android:exported`** — অন্য app এই component চালাতে পারবে কিনা। Android 12+ এ intent filter থাকলে লিখতেই হবে। Default ভাবনা: `false`; শুধু launcher activity, deep link activity, আর যা সত্যিই বাইরের জন্য — `true`।
- **`<uses-permission>`** — "আমার app এই permission চায়"।
- **`<permission>`** — "আমি নতুন permission **define** করছি", অন্যরা আমার component-এ ঢুকতে এটা লাগবে। `protectionLevel="signature"` দিলে শুধু আমার key-তে sign করা app পাবে — নিজের app-গুলোর মধ্যে নিরাপদ যোগাযোগের জন্য ভালো।
- **`<queries>`** (Android 11+, package visibility) — অন্য app আছে কিনা জানতে বা implicit intent resolve করতে declare করতে হয়। না হলে `PackageManager` সেই app দেখায় না।
  - `QUERY_ALL_PACKAGES` আছে, কিন্তু Play policy খুব কড়া — core কারণ ছাড়া reject।
  - শুধু `startActivity` করে ফেলার জন্য queries লাগে না; `resolveActivity`/check করার জন্য লাগে।
- **`<uses-feature>`** — কোন hardware লাগে। Play Store এটা দিয়ে device filter করে।
  - সাবধান: `CAMERA` permission চাইলে system ধরে নেয় `android.hardware.camera` **required**। Camera ছাড়া device-এও app দিতে চাইলে `android:required="false"` লিখুন আর runtime-এ `PackageManager.hasSystemFeature()` চেক করুন।
- **Manifest merger** — library-র manifest আপনারটার সাথে মেশে। Library কোনো permission যোগ করলে আপনার app-এও আসে। সরাতে `tools:node="remove"`। Release-এর আগে merged manifest দেখুন (Android Studio → Merged Manifest tab)।
- `minSdk`/`targetSdk`/`versionCode` এখন Gradle-এ, manifest-এ না।
- Network: `android:usesCleartextTraffic` / `networkSecurityConfig` — Android 9+ এ HTTP default বন্ধ। LAN camera-র HTTP/RTSP-এর জন্য নির্দিষ্ট domain/IP-তে সীমিত exception দিন, পুরো app-এ না।

```xml
<permission android:name="com.example.cam.permission.CONTROL"
    android:protectionLevel="signature" />
<queries>
    <intent><action android:name="android.media.action.IMAGE_CAPTURE" /></intent>
</queries>
<uses-feature android:name="android.hardware.camera" android:required="false" />
```

**Answer (English):**
> "The manifest declares components, permissions, and device needs. android:exported decides if other apps can start a component, and I keep it false unless it must be public. uses-permission means my app asks for a permission. The permission tag defines a new one, and with signature level only apps signed with my key get it. Since Android 11, I must list other apps or intents in queries to see them. uses-feature tells Play which hardware is needed. One trap: asking for CAMERA makes the camera feature required, so I set required to false if the app also works without a camera. I always check the merged manifest, because libraries can add permissions."

**Key words:** `exported` · `protectionLevel signature` · `<queries>` · `package visibility` · `uses-feature` · `merged manifest`

**Follow-up:**
- **Q:** How do two of your own apps talk securely?
  **A:** "I define a signature-level permission and protect the exported service or provider with it. Only apps signed with my key can bind."
- **Q:** A library added a permission you don't want. What do you do?
  **A:** "I remove it in my manifest with tools:node remove, then check the merged manifest and test the feature that library uses."

**আরও দেখুন:** [S9 · Secure components](#s9) · [F7 · Intent resolution](#f7) · [C13 · Permissions](#c13)

---

### <a id="c15"></a>C15. ★ How do notifications and push messages work on modern Android?

**প্রশ্নটা মানে:** Channel, notification permission, FCM message-এর ধরন, আর জরুরি alert (যেমন motion detect) সময়মতো দেখানোর নিয়ম জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you show a motion alert from a camera fast and reliably?" · "What is the difference between FCM data and notification messages?"

**বুঝে নিন:**
**Channel (Android 8+):**
- প্রতিটা notification একটা channel-এ যায়। Importance, sound, vibration channel-এর।
- Channel তৈরির পর importance app বদলাতে পারে না — user নিয়ন্ত্রণ করে। ভুল হলে নতুন id দিয়ে নতুন channel।
- ভাগ করুন কাজ দিয়ে: "Motion alerts" (high), "Recording status" (low), "Updates" (default)। User যেন বেছে বন্ধ করতে পারে।

**`POST_NOTIFICATIONS` (Android 13+):**
- Runtime permission। Target 33+ হলে নিজে চাইতে হবে; ঠিক context-এ চান।
- Denied হলেও foreground service চলে, তবে তার notification drawer-এ না দেখিয়ে Task Manager-এ দেখা যায়।
- `NotificationManagerCompat.areNotificationsEnabled()` দিয়ে চেক।

**FCM message ধরন:**
| | Notification message | Data message |
|---|---|---|
| App background-এ | system নিজে tray-তে দেখায়; `onMessageReceived` আসে না | `onMessageReceived` আসে |
| App foreground-এ | `onMessageReceived` | `onMessageReceived` |
| নিয়ন্ত্রণ | কম | পুরো (নিজে notification বানান) |

- **Priority:** `high` — Doze-এর মধ্যেও তাড়াতাড়ি আসে, app কিছু সময়ের জন্য চলার সুযোগ পায় (FGS start-এর exception-ও)। কিন্তু high-priority পেয়ে user-visible notification না দেখালে system পরে সেই app-এর message **deprioritize** করে।
- `normal` — battery বাঁচাতে Doze-এ পিছিয়ে যায়। Sync-এর জন্য।
- `onMessageReceived`-এ লম্বা কাজ না — ছোট সময় পায়। বড় কাজ WorkManager-এ।
- FCM token বদলায় — `onNewToken`-এ server-এ পাঠান।
- নতুন: Firebase একটা **FCM v2 (`android_v2`) preview** দেখাচ্ছে — `RemoteNotification` (জরুরি, user-visible) আর `BackgroundSync` (non-urgent) — priority-র জায়গায় message type। এটা এখনো preview; production-এ HTTP v1 আর high/normal priority-ই চলছে। Firebase docs দেখে নিন।

**Full-screen intent:**
- Lock screen-এর উপর পুরো screen জুড়ে দেখানো (incoming call, alarm)।
- Android 14+: `USE_FULL_SCREEN_INTENT` শুধু calling আর alarm app-এর জন্য Play সাধারণত দেয়। অন্যদের জন্য user Settings-এ চালু করতে হয়।
- চেক: `NotificationManager.canUseFullScreenIntent()`; না থাকলে `Settings.ACTION_MANAGE_APP_USE_FULL_SCREEN_INTENT`।
- Camera motion alert সাধারণত high-importance **heads-up** notification হিসেবে যথেষ্ট। Doorbell-কে "call" ধরা যাবে কিনা — Play policy মিলিয়ে দেখতে হবে।

**Security camera practical:** server থেকে high-priority data message → ছোট `onMessageReceived` → সাথে সাথে high channel-এ notification (thumbnail সহ হলে ছোট image আগে থেকে URL-এ) → tap করলে immutable PendingIntent দিয়ে ঠিক camera-র live view।

**Answer (English):**
> "Since Android 8, every notification belongs to a channel, and the user controls each channel. So I split channels by purpose, like motion alerts and recording status. Since Android 13, I must ask for POST_NOTIFICATIONS. With FCM, a notification message is shown by the system when the app is in the background, but a data message always reaches onMessageReceived, so I use data messages for full control. For urgent alerts I send high priority, which can wake the device from Doze. But I must show a visible notification each time, or FCM will lower my priority. Full-screen intents are now mostly only for calling and alarm apps, so for camera alerts I use heads-up notifications."

**Key words:** `NotificationChannel` · `POST_NOTIFICATIONS` · `data message` · `high priority` · `deprioritized` · `USE_FULL_SCREEN_INTENT` · `onNewToken`

**Follow-up:**
- **Q:** Why did your notification sound stop after you changed the code?
  **A:** "Channel settings are fixed after the channel is created. To change importance or sound, I must create a new channel with a new id, and maybe delete the old one."
- **Q:** What if the user denies notification permission in a security camera app?
  **A:** "The main feature is weaker, so I explain the value in the app and give a button to settings. I also show alerts inside the app when it is open."
- **Q:** Can you start a foreground service from an FCM message?
  **A:** "Yes, a high-priority message gives a short exemption from the background start limit. But if the type needs a while-in-use permission, like camera, there are more limits."

**ভুল করবেন না:** সব message `high` পাঠানো কিন্তু notification না দেখানো — FCM আপনার priority কমিয়ে দেবে।

**আরও দেখুন:** [V9 · Motion alerts](#v9) · [R16 · Push vs sockets](#r16) · [C5 · PendingIntent](#c5)

---

### <a id="c16"></a>C16. ◆ What is the difference between deep links and Android App Links?

**প্রশ্নটা মানে:** URL থেকে app-এর ঠিক screen খোলা, আর domain verify করে অন্য app-কে link নিতে না দেওয়া — জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why does my link open the browser instead of the app?" · "How do you verify a domain for your app?"

**বুঝে নিন:**
- **Deep link** — intent filter-এ `VIEW` + `BROWSABLE` + `DEFAULT` + `<data>`। Custom scheme (`mycam://camera/12`) বা http(s)।
  - সমস্যা: যেকোনো app একই scheme দাবি করতে পারে → hijack। তাই sensitive data (token) কখনো deep link-এ না।
- **Android App Link** — শুধু `https` link, `android:autoVerify="true"`, আর domain-এ ফাইল:
  `https://<domain>/.well-known/assetlinks.json` — package name + **signing certificate-এর SHA-256**।
  - Verify হলে link সরাসরি app-এ খোলে, chooser ছাড়া। অন্য app নিতে পারে না।
  - Play App Signing ব্যবহার করলে Play Console-এর **app signing key**-র fingerprint দিন, upload key-র না — এটা খুব কমন ভুল।
- Android 12+: verify না হওয়া http(s) link default-এ browser-এ খোলে (user নিজে "open supported links" চালু না করলে)।
- Test: `adb shell pm get-app-links <package>`, `adb shell pm verify-app-links --re-verify <package>`। Android Studio-তে App Links Assistant।
- Link থেকে আসা data **untrusted input** — id validate করুন, auth চেক করুন, তারপর screen খুলুন।
- Compose Navigation-এ `navDeepLink { uriPattern = ... }`।
- Firebase Dynamic Links বন্ধ হয়ে গেছে (2025)। Deferred deep link (install-এর পর link) লাগলে অন্য সমাধান লাগে।

**Answer (English):**
> "A deep link is any link that opens a screen in my app, through an intent filter. With a custom scheme, any app can claim the same scheme, so it is not secure. An App Link is an https link that the system verifies. I add autoVerify to the intent filter and host an assetlinks.json file on my domain with my package name and certificate fingerprint. Then the link opens my app directly, and no other app can take it. Since Android 12, unverified web links open in the browser. A common mistake is using the upload key fingerprint instead of the Play app signing key. I also treat link data as untrusted input."

**Key words:** `intent filter` · `autoVerify` · `assetlinks.json` · `SHA-256 fingerprint` · `BROWSABLE` · `verify-app-links`

**Follow-up:**
- **Q:** Your App Link works in debug but not from Play. Why?
  **A:** "Most likely the assetlinks file has only the debug or upload key fingerprint. The Play build is signed with the app signing key, so I add that fingerprint."
- **Q:** Is it safe to put a login token in a deep link?
  **A:** "No. Links can be logged or caught by other apps. I use a short one-time code and exchange it on the server."

**আরও দেখুন:** [F7 · Intent resolution](#f7) · [U8 · Compose navigation](#u8) · [S9 · Secure components](#s9)

---

### <a id="c17"></a>C17. ◆ How does storage work on modern Android?

**প্রশ্নটা মানে:** কোন data কোথায় রাখবেন, কোন permission লাগে, scoped storage আর Photo Picker-এর নিয়ম জানেন কিনা — recording save করা camera app-এর মূল কাজ।
**অন্যভাবেও জিজ্ঞেস করে:** "Where would you save recorded videos so the user can see them in the gallery?" · "Do you still need READ_EXTERNAL_STORAGE?"

**বুঝে নিন:**
| জায়গা | API | Permission | Uninstall-এ |
|---|---|---|---|
| Internal app storage | `filesDir`, `cacheDir`, Room, DataStore | লাগে না | মুছে যায় |
| App-specific external | `getExternalFilesDir()` | লাগে না | মুছে যায় |
| Shared media | **MediaStore** | নিজের file লিখতে লাগে না (Android 10+); অন্যের media পড়তে `READ_MEDIA_*` (13+) | থাকে |
| Document / যেকোনো file | **SAF**: `OpenDocument`, `CreateDocument`, `OpenDocumentTree` | লাগে না (user বেছে দেয়) | থাকে |
| Photo/video বাছাই | **Photo Picker** (`PickVisualMedia`) | লাগে না | — |

- **Scoped storage** — Android 10-এ এলো, Android 11-এ সবার জন্য চালু। App আর পুরো external storage ঘুরে বেড়াতে পারে না।
- `READ_EXTERNAL_STORAGE` Android 13+ এ media-র জন্য কাজ করে না → `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO` / `READ_MEDIA_AUDIO`।
- Android 14: user "শুধু কিছু ছবি" দিতে পারে (`READ_MEDIA_VISUAL_USER_SELECTED`)। আপনার app এটা ঠিকমতো handle করতে হবে।
- **Photo Picker** — permission ছাড়া, user যা বাছে শুধু সেটা। পুরনো Android-এ Google Play services দিয়ে backport আছে। `ActivityResultContracts.PickVisualMedia()`।
- **Google Play photo/video policy** — `READ_MEDIA_IMAGES`/`VIDEO` শুধু সেই app পায় যার মূল কাজই অনেক media পড়া (gallery, editor ইত্যাদি)। মাঝে মাঝে একটা ছবি নিলে Photo Picker ব্যবহার করতেই হবে।
- `MANAGE_EXTERNAL_STORAGE` ("All files access") — Play-তে খুব সীমিত (file manager, backup ধরনের)।
- Sensitive data (token, key) internal storage-এ, Keystore-ভিত্তিক encryption সহ (Tink); deprecated `EncryptedSharedPreferences` নতুন code-এ না।

**Recording gallery-তে save (MediaStore):**
```kotlin
val values = ContentValues().apply {
    put(MediaStore.Video.Media.DISPLAY_NAME, "cam_${System.currentTimeMillis()}.mp4")
    put(MediaStore.Video.Media.MIME_TYPE, "video/mp4")
    put(MediaStore.Video.Media.RELATIVE_PATH, "${Environment.DIRECTORY_MOVIES}/MyCam")
    put(MediaStore.Video.Media.IS_PENDING, 1)
}
val uri = resolver.insert(MediaStore.Video.Media.EXTERNAL_CONTENT_URI, values)
// write with resolver.openOutputStream(uri), then:
// resolver.update(uri, ContentValues().apply { put(MediaStore.Video.Media.IS_PENDING, 0) }, null, null)
```
(CameraX `Recorder` সরাসরি `MediaStoreOutputOptions` নেয় — নিজে লিখতে হয় না।)

**Answer (English):**
> "I pick storage by who owns the data. Private app data goes to internal storage, Room, or DataStore, with no permission. Media the user should keep, like recorded videos, goes to MediaStore, and since Android 10 I need no permission to write my own files there. For any document the user chooses, I use the Storage Access Framework. To let the user pick photos or videos, I use the Photo Picker, which needs no permission. Since Android 13, broad media reading needs READ_MEDIA_IMAGES or VIDEO, and Google Play only allows that for apps with a core need. Scoped storage means I cannot freely browse shared storage anymore."

**Key words:** `scoped storage` · `MediaStore` · `IS_PENDING` · `SAF` · `Photo Picker` · `READ_MEDIA_VIDEO` · `partial access`

**Follow-up:**
- **Q:** What happens to app-specific external files on uninstall?
  **A:** "They are deleted, like internal files. If the user must keep recordings after uninstall, I save them to MediaStore."
- **Q:** Why use IS_PENDING?
  **A:** "It hides the file from other apps while I am still writing it. When writing is done, I set it to zero so the gallery sees a complete file."

**ভুল করবেন না:** শুধু profile picture বাছতে `READ_MEDIA_IMAGES` চাওয়া — Play reject করবে; Photo Picker ব্যবহার করুন।

**আরও দেখুন:** [S11 · Data at rest](#s11) · [V5 · Record video](#v5)

---

### <a id="c18"></a>C18. ◆ How does an app process start, and how does Android decide which process to kill?

**প্রশ্নটা মানে:** Zygote থেকে প্রথম frame পর্যন্ত কী হয়, cold/warm/hot start কী, আর memory কম হলে কোন process আগে মরে — জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Which process does Android kill first when memory is low?" · "How would you improve cold start time?"

**বুঝে নিন:**
**Icon tap থেকে প্রথম frame (ছোট করে; পুরো পথ F1-এ):**
Launcher → `system_server` → process নেই হলে **Zygote** fork → `ActivityThread.main()` → `Application` তৈরি → সব **ContentProvider-এর `onCreate`** → `Application.onCreate()` → Activity `onCreate`/`onStart`/`onResume` → প্রথম frame।

**Start-এর ধরন:**
| ধরন | কী অবস্থা | ধীর কেন |
|---|---|---|
| **Cold** | process নেই | ওপরের পুরো পথ |
| **Warm** | process আছে কিন্তু Activity নতুন করে তৈরি (বা process নতুন, saved state থেকে) | Activity create + layout |
| **Hot** | process আর Activity দুটোই memory-তে, শুধু সামনে আনা | প্রায় কিছু না |

- Android vitals-এ "excessive" ধরা হয়: cold ≥ 5s, warm ≥ 2s, hot ≥ 1.5s।
- Cold start দ্রুত করার উপায়: `Application.onCreate` হালকা রাখুন (lazy init, App Startup), main thread-এ I/O নেই, **Baseline Profiles**, R8, SplashScreen API সঠিকভাবে, `reportFullyDrawn()`। মাপুন **Macrobenchmark** দিয়ে, অনুমানে না।
- Android 15+ এ `ApplicationStartInfo` দিয়ে start কেন আর কীভাবে হলো জানা যায়।

**Process priority (বেশি থেকে কম):**
1. **Foreground** — user যে activity ব্যবহার করছে, বা foreground-এ চলমান receiver/service callback।
2. **Visible** — দেখা যাচ্ছে কিন্তু focus নেই (dialog-এর পেছনে, multi-window)।
3. **Perceptible / service** — foreground service (music, recording); তারপর সাধারণ started service।
4. **Cached** — background-এ রাখা app; প্রথম মারা পড়ে (LRU order)।

- **Low memory killer** — আজকের Android-এ userspace daemon **lmkd**। প্রতিটা process-এর `oom_score_adj` দেখে (system priority অনুযায়ী সেট করে) আর memory pressure (PSI) বেশি হলে কম গুরুত্বের process মারে।
- মারার আগে কোনো callback আসবে, এমন guarantee নেই। `onTrimMemory()` আগে জানাতে পারে — তখন cache ছাড়ুন।
- তাই process death (C4) স্বাভাবিক ঘটনা, bug না।
- `android:process=":remote"` দিয়ে component আলাদা process-এ চালানো যায়। প্রতিটা process-এ `Application.onCreate` আবার চলে — singleton আলাদা, memory বেশি।

**Answer (English):**
> "When the user taps the icon, the launcher asks system_server to start my Activity. If there is no process, Zygote forks a new one, which is fast because the framework is already loaded. Then my Application is created, content providers run their onCreate, then Application.onCreate, and then the Activity draws its first frame. A cold start does all of this, a warm start recreates the Activity, and a hot start just brings it to the front. For memory, Android ranks processes: foreground, visible, service, then cached. lmkd kills cached ones first. To speed up cold start, I keep Application.onCreate light, add Baseline Profiles, and measure with Macrobenchmark."

**Key words:** `Zygote` · `ActivityThread` · `cold start` · `Baseline Profiles` · `lmkd` · `oom_score_adj` · `cached process`

**Follow-up:**
- **Q:** Why is a foreground service less likely to be killed?
  **A:** "Its process gets a higher priority, close to a visible app, because the user knows it is running. The system kills cached processes long before it."
- **Q:** What is the risk of using android:process for a component?
  **A:** "It creates a second process with its own Application instance and memory. Singletons are not shared, so I need IPC, and start time and memory go up."

**ভুল করবেন না:** "Application.onCreate সবার আগে চলে" — ContentProvider-এর `onCreate` তার আগে চলে।

**আরও দেখুন:** [F1 · Tap an app icon](#f1) · [P3 · Startup](#p3) · [F9 · Memory](#f9)

---


## <a id="part-2b"></a>Part 2B — Android framework-এর ভেতরে (internals)

এই অংশ app-এর নিচের layer নিয়ে: process কীভাবে শুরু হয়, Binder, ART, frame কীভাবে আঁকা হয়, system service কীভাবে কাজ করে।
Camera, sensor আর custom Android OS (AOSP) নিয়ে কাজ করা team এই প্রশ্নগুলো বেশি করে। কারণ তাদের bug প্রায়ই app আর system-এর মাঝখানে থাকে।
শেষে 2025–2026-এ Android development-এ কী নতুন, সেটা দেওয়া আছে।

### আগে বুঝুন — app-এর নিচে Android কীভাবে সাজানো

একটা Android app একা চলে না। প্রায় প্রতিটা কাজ (activity খোলা, camera, location, notification) আসলে **অন্য process-এ চলা system service**-কে অনুরোধ। এই অনুরোধ যায় **Binder** দিয়ে।

**Layer-গুলো, উপর থেকে নিচে:**
```
Your app process (ART: Kotlin/Java code, ActivityThread, main thread)
   │  Binder IPC
system_server (ActivityManagerService, ActivityTaskManagerService, WindowManagerService,
               PackageManagerService, LocationManagerService, SensorService ...)
cameraserver, surfaceflinger, mediaserver ... (আলাদা native process)
   │  AIDL / HIDL (পুরনো)
HAL (vendor-এর code: camera HAL, sensors HAL, GNSS HAL)
   │
Linux kernel (driver, Binder driver, SELinux, cgroups, lmkd-কে memory তথ্য)
```

**মূল ধারণাগুলো:**
1. **প্রতিটা app = একটা Linux process + নিজের UID।** এটাই sandbox। এক app আরেক app-এর file পড়তে পারে না।
2. **Zygote:** boot-এর সময় শুরু হয়, framework class আর resource আগে থেকে load করে রাখে। নতুন app process = Zygote-এর `fork()`। তাই app দ্রুত শুরু হয়।
3. **system_server:** বেশিরভাগ Java system service এখানে চলে। আপনার `XxxManager` class শুধু একটা Binder proxy।
4. **Binder:** kernel driver দিয়ে process-এর মধ্যে method call। Kernel caller-এর UID/PID বলে দেয়। Caller এটা নকল করতে পারে না, তাই permission check-এ ভরসা করা যায়।
5. **ART:** DEX bytecode চালায়। Interpreter + JIT + AOT মিশিয়ে। Profile দেখে কোন code আগে compile করবে ঠিক করে।
6. **Main thread = Looper + MessageQueue।** Lifecycle callback, input, drawing — সব এখানে। এখানে দেরি = jank বা ANR।
7. **Frame pipeline:** VSYNC → Choreographer → measure/layout/draw (main thread) → RenderThread GPU-তে পাঠায় → SurfaceFlinger সব window মিলিয়ে screen-এ দেয়।
8. **Memory চাপ হলে** kernel আর `lmkd` কম গুরুত্বের process মেরে ফেলে। Background app যেকোনো সময় মারা যেতে পারে।

**Flutter থেকে এলে কী আলাদা:**
- Flutter app-ও এই একই Android process-এ চলে। Flutter engine নিজের thread (UI, raster) চালায় আর একটা `SurfaceView` (বা TextureView)-এ আঁকে। Android-এর View pipeline শুধু সেই surface দেখে।
- Platform channel-এর ওপারে যে Kotlin code, সেটা এই part-এর সব নিয়ম মানে — main thread, Binder, permission।
- Flutter-এ "ANR" কম শোনা যায়। কিন্তু Android main thread (platform thread) আটকালে Flutter app-ও ANR পায়।
- Dart isolate memory, Java heap আর native heap আলাদা হিসাব হয়। Flutter app-এর বেশিরভাগ memory native।

---

### <a id="f1"></a>F1. ★ What happens when you tap an app icon?

**প্রশ্নটা মানে:** Launcher থেকে প্রথম frame পর্যন্ত পুরো পথ জানেন কিনা — কোন process কী করে।
**অন্যভাবেও জিজ্ঞেস করে:** "Explain the app startup flow from the system side." · "What is Zygote and why does Android use it?"

**বুঝে নিন:**
Cold start (process নেই) ধরে:
1. **Launcher** একটা app। Tap করলে সে `startActivity(intent)` call করে।
2. Call টা **Binder** দিয়ে যায় `system_server`-এর **ActivityTaskManagerService (ATMS)**-এ (Android 10-এর আগে এটা ActivityManagerService-এর ভেতরে ছিল)।
3. ATMS intent resolve করে (PackageManager দিয়ে), permission আর background-start নিয়ম check করে, Task/ActivityRecord বানায়। সাথে সাথে **starting window / splash screen** দেখায় — তাই user সাথে সাথে কিছু দেখে।
4. App-এর process নেই → **ActivityManagerService (AMS)** **Zygote**-কে নতুন process চায়। এই অনুরোধ যায় একটা **Unix domain socket** দিয়ে, Binder দিয়ে না।
5. Zygote `fork()` করে। নতুন process app-এর UID, SELinux context, seccomp filter পায়। তারপর **`ActivityThread.main()`** চলে: main Looper বানায়।
6. App AMS-কে জানায় "আমি তৈরি" (`attachApplication`, Binder)। AMS ফেরত বলে `bindApplication`।
7. App-এ: `Application` object বানানো (`attachBaseContext`) → **ContentProvider-গুলোর `onCreate`** (App Startup library এই ধাপ ব্যবহার করে) → **`Application.onCreate()`**।
8. ATMS activity launch পাঠায় → `Activity.onCreate` → `onStart` → `onResume`।
9. **প্রথম frame:** `ViewRootImpl` window যোগ করে, Choreographer পরের VSYNC-এ measure/layout/draw চালায়, RenderThread GPU-তে পাঠায়, SurfaceFlinger দেখায়। এরপর starting window সরে যায়।
- Logcat-এ `Displayed ...: +xxx ms` = TTID (time to initial display)। পুরো data এলে `reportFullyDrawn()` → TTFD।
- Warm start: process আছে, activity নতুন। Hot start: activity শুধু foreground-এ আসে।

**Answer (English):**
> "The launcher calls startActivity. That goes over Binder to ActivityTaskManagerService in system_server. It resolves the intent, checks rules, and shows a starting window. If the app has no process, ActivityManagerService asks Zygote over a socket to fork a new one. Zygote already has the framework loaded, so the fork is fast. The new process runs ActivityThread.main, starts the main looper, and attaches to the system. Then the app creates the Application, runs ContentProvider onCreate, then Application.onCreate. After that the activity goes through onCreate, onStart and onResume, and the first frame is drawn. So for fast startup, I keep Application.onCreate and providers light."

**Key words:** `Zygote` · `system_server` · `ActivityTaskManagerService` · `ActivityThread.main` · `bindApplication` · `TTID / TTFD` · `cold start`

**Follow-up:**
- **Q:** Why does Android use Zygote instead of starting each app from zero?
  **A:** "Zygote loads the runtime, common classes and resources once. Each fork shares those memory pages with copy-on-write, so apps start faster and use less memory."
- **Q:** What runs before Application.onCreate?
  **A:** "attachBaseContext and the onCreate of every ContentProvider in the app. Many libraries start themselves with a provider, so they can slow startup. I check them with the App Startup library or merge them."
- **Q:** How do you measure startup?
  **A:** "I use Macrobenchmark with StartupTimingMetric on a release-like build, and Perfetto traces to see what blocks the main thread. I also watch Android vitals for slow start."

**ভুল করবেন না:** "Zygote-এর সাথে Binder দিয়ে কথা হয়" বলা — AMS Zygote-কে socket দিয়ে fork করতে বলে।

**আরও দেখুন:** [C18 · Process start](#c18) · [P3 · Startup](#p3) · [F2 · ART](#f2)

---

### <a id="f2"></a>F2. ★ How does ART run your code? (DEX, JIT, AOT, Baseline Profiles)

**প্রশ্নটা মানে:** ART কীভাবে code compile করে, আর কেন install-এর পর প্রথম launch ধীর হতে পারে — Baseline Profile কীভাবে সাহায্য করে।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between Dalvik and ART?" · "What are Baseline Profiles and why do they help?"

**বুঝে নিন:**
- **DEX:** Kotlin → JVM bytecode → **D8** → DEX (register-based, Android-এর জন্য)। R8 এই সময় shrink/optimize/obfuscate করে।
- **Dalvik (Android 4.4 পর্যন্ত):** শুধু interpreter + JIT। প্রতিবার run-এ আবার compile।
- **ART (Android 5+):** শুরুতে install-এর সময় পুরো AOT (`dex2oat`)। Install ধীর, storage বেশি।
- **Android 7 থেকে hybrid (এখনকার নিয়ম):**
  1. Install-এ সাধারণত পুরো compile হয় না (শুধু verify, বা profile থাকলে সেটুকু)।
  2. App চলে **interpreter + JIT** দিয়ে। JIT গরম (hot) method compile করে আর একটা **profile** file লেখে।
  3. Device idle আর charging হলে background dexopt job profile দেখে hot code **AOT** compile করে (`speed-profile`)।
  4. পরের launch দ্রুত।
- **তাই install-এর পর প্রথম কয়েক launch ধীর** — তখনো profile নেই, code interpret বা JIT হচ্ছে।
- **সমাধান:**
  - **Cloud profiles (Android 9+):** Play অনেক user-এর থেকে profile জমিয়ে install-এর সময় দেয়। কিন্তু নতুন version-এর প্রথম দিকে থাকে না।
  - **Baseline Profiles:** আপনি নিজে APK/AAB-এ startup আর মূল journey-র method list পাঠান (`baseline-prof.txt`)। Install-এ (বা `ProfileInstaller` দিয়ে) সেটা AOT হয়। প্রথম launch থেকেই লাভ। Macrobenchmark-এর `BaselineProfileRule` দিয়ে বানান।
  - **Startup Profiles:** DEX layout ঠিক করে, যাতে startup code একসাথে থাকে।
- ART Android 12 থেকে **Mainline module** — Play system update দিয়ে device-এ ART নতুন হতে পারে।
- Compose library হিসেবে আসে (framework-এ না), তাই Compose app-এ Baseline Profile খুব বেশি লাভ দেয়।

**Answer (English):**
> "Kotlin code becomes DEX through D8, and R8 shrinks and optimizes it. ART runs DEX with a mix of interpreter, JIT and AOT. Since Android 7, the app usually is not fully compiled at install. It starts with the interpreter and JIT, the JIT writes a profile of hot code, and later, when the phone is idle and charging, ART compiles that hot code ahead of time. That is why the first runs after install can be slower. Play cloud profiles help, but not for a fresh release. So I ship Baseline Profiles. They tell ART which code to compile at install, so startup and key screens are fast from the first launch."

**Key words:** `DEX` · `D8 / R8` · `JIT` · `AOT` · `dex2oat` · `profile-guided compilation` · `cloud profiles` · `Baseline Profiles`

**Follow-up:**
- **Q:** How do you check if a Baseline Profile works?
  **A:** "I run Macrobenchmark with compilation mode None, then with the Baseline Profile, and compare startup and frame timing. I test on a real device with a release build."
- **Q:** What is the main difference between Dalvik and ART?
  **A:** "Dalvik compiled with JIT on every run. ART adds ahead-of-time compilation and better garbage collection. Modern ART mixes JIT and AOT using profiles."
- **Q:** Why are Baseline Profiles important for Compose apps?
  **A:** "Compose is a library inside the app, not part of the system image, so it is not precompiled on the device. Without a profile, a lot of Compose code is interpreted on first runs."

**ভুল করবেন না:** "ART install-এর সময় সব AOT করে" — এটা Android 5–6-এর কথা, এখন hybrid।

**আরও দেখুন:** [P3 · Startup](#p3) · [P5 · R8](#p5)

---

### <a id="f3"></a>F3. ★ What is Binder, and why does Android use it?

**প্রশ্নটা মানে:** Android-এর IPC কী, কেন socket বা pipe না, আর TransactionTooLargeException কোথা থেকে আসে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do two processes talk in Android?" · "Why do you get TransactionTooLargeException?"

**বুঝে নিন:**
- **Binder** = kernel driver (`/dev/binder`) + user-space library। এক process আরেক process-এর object-এর method call করে, local call-এর মতো দেখতে।
- **কেন socket না:**
  - **Identity:** Kernel প্রতিটা call-এ caller-এর UID/PID দেয় (`Binder.getCallingUid()`)। Caller মিথ্যা বলতে পারে না। Permission check এর উপর নির্ভর করে।
  - **One copy:** data sender থেকে receiver-এর mmap করা buffer-এ একবার copy হয়।
  - **Object reference:** Binder object (token, callback) process পার করে পাঠানো যায়। Kernel reference count রাখে।
  - **Death notification:** অন্য process মারা গেলে `linkToDeath` দিয়ে জানা যায়।
  - **Thread pool:** receiver-এর binder thread-গুলো call চালায় (F10)।
- **AIDL:** interface লিখলে tool proxy (client side) আর stub (server side) code বানায়। `oneway` মানে caller অপেক্ষা করে না। HAL-এর জন্যও এখন **stable AIDL**।
- **Transaction buffer limit:** প্রতিটা process-এর binder buffer প্রায় **1 MB**, আর সেটা ওই process-এর **সব চলমান transaction মিলে** ভাগ করা। একটা বড় call বা অনেক ছোট call একসাথে → `TransactionTooLargeException`।
- **কোথায় হয়:**
  - Intent extra-তে বড় data (bitmap, বড় list)।
  - `onSaveInstanceState` / `SavedStateHandle`-এ বড় data। Activity stop হলে saved state Binder দিয়ে system_server-এ যায়। Android 7+ target-এ এটা crash করে।
- **সমাধান:** Bundle-এ শুধু ID বা ছোট state রাখুন। বড় data disk/DB-তে, ViewModel-এ, বা `ContentProvider`/file URI দিয়ে দিন। বড় memory share করতে `SharedMemory`/`ParcelFileDescriptor`।

**Answer (English):**
> "Binder is Android's IPC system. It is a kernel driver plus a library, and it lets one process call methods on an object in another process. Android uses it instead of sockets for a few reasons. The kernel gives the receiver the real UID and PID of the caller, so system services can check permissions safely. It copies data only once, it can pass object references, and it can tell me when the other process dies. AIDL generates the proxy and stub code. The limit is a buffer of about one megabyte per process, shared by all calls in flight. Big Intent extras or big saved state cause TransactionTooLargeException, so I pass IDs, not data."

**Key words:** `Binder driver` · `getCallingUid` · `AIDL` · `proxy / stub` · `oneway` · `linkToDeath` · `TransactionTooLargeException`

**Follow-up:**
- **Q:** How do you find what makes the saved state too big?
  **A:** "I log the size of the Bundle in onSaveInstanceState, or use a tool like TooLargeTool. Usually it is a big list or a bitmap in saved state or in fragment arguments."
- **Q:** Is a Binder call fast enough to run on the main thread?
  **A:** "Most calls are fast, but it is still IPC, and the other side can be busy. A slow system service can block the main thread and cause an ANR. I keep heavy or many Binder calls off the main thread."
- **Q:** What is a oneway call?
  **A:** "The caller sends it and does not wait for a reply. It is good for events and callbacks. But calls to the same object are queued in order, and too many can fill the buffer."

**ভুল করবেন না:** "1 MB প্রতিটা transaction-এর জন্য" — না, পুরো process-এর সব চলমান transaction মিলে।

**আরও দেখুন:** [C4 · Saved state](#c4) · [F4 · Parcelable](#f4) · [S12 · Secure IPC](#s12)

---

### <a id="f4"></a>F4. ★ Parcelable vs Serializable — which and why?

**প্রশ্নটা মানে:** Android-এ object পাঠানোর দুই উপায়ের পার্থক্য, আর আজকাল কী ব্যবহার করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Why is Parcelable faster?" · "What does @Parcelize do?"

**বুঝে নিন:**
| | `Serializable` | `Parcelable` |
|---|---|---|
| কোথা থেকে | Java standard | Android-এর নিজের |
| কীভাবে | Reflection দিয়ে সব field লেখে | নিজের লেখা (বা generated) `writeToParcel` / `CREATOR` |
| গতি | ধীর, অনেক temporary object (GC চাপ) | দ্রুত, Binder-এর জন্য তৈরি |
| Disk-এ রাখা | যায় (কিন্তু ভালো না) | **না** — Parcel format version-এ বদলাতে পারে |
| Security | Java deserialization-এর পুরনো ঝুঁকি | সীমিত, কিন্তু untrusted data সাবধানে পড়ুন |

- **`@Parcelize`** (`kotlin-parcelize` plugin, id `org.jetbrains.kotlin.plugin.parcelize`): compiler `writeToParcel` আর `CREATOR` লিখে দেয়। Hand-written boilerplate লাগে না।
```kotlin
@Parcelize
data class CameraArgs(val cameraId: String, val channel: Int) : Parcelable
// Android 13+ type-safe read; পুরনো version-এ compat:
val args = IntentCompat.getParcelableExtra(intent, "args", CameraArgs::class.java)
```
- Android 13 (API 33) থেকে untyped `getParcelableExtra(name)` deprecated। Class দিয়ে typed version ব্যবহার করুন (বা `IntentCompat` / `BundleCompat`)।
- **আজকের practice:** Navigation-এ বড় object না পাঠিয়ে ID পাঠান। Type-safe navigation route-এ `@Serializable` (kotlinx.serialization) — এটা Java `Serializable` না, আলাদা জিনিস।
- Persistence বা network-এর জন্য: kotlinx.serialization / Moshi, Room, DataStore।

**Answer (English):**
> "Parcelable is Android's own way to write objects into a Parcel for Binder. Serializable is the Java way, and it uses reflection, so it is slower and creates more garbage. I use Parcelable, and with Kotlin I just add @Parcelize, so the compiler writes the code for me. Parcelable is only for passing data between components or processes. I never save it to disk, because the format is not stable between versions. Even with Parcelable, I try to pass only an ID and load the real data from the repository. That keeps the Bundle small and avoids TransactionTooLargeException."

**Key words:** `Parcelable` · `Serializable` · `@Parcelize` · `Parcel` · `reflection` · `IntentCompat`

**Follow-up:**
- **Q:** Is kotlinx.serialization the same as Serializable?
  **A:** "No. kotlinx.serialization uses a compiler plugin and generates code, no reflection. It writes JSON or other formats. Java Serializable is the old reflection-based binary format."
- **Q:** Why should you be careful reading a Parcelable from another app?
  **A:** "The data is untrusted. A bad app can send unexpected types or values. I validate input and use the typed getters, and I do not export components that do not need it."

**ভুল করবেন না:** Parcelable disk-এ save করা — OS update-এর পর পড়া না-ও যেতে পারে।

**আরও দেখুন:** [C4 · Saved state](#c4) · [F3 · Binder](#f3) · [C19 · Screens talking](#c19)

---

### <a id="f5"></a>F5. ★ How is a frame drawn on Android, and where does jank come from?

**প্রশ্নটা মানে:** VSYNC থেকে screen পর্যন্ত pipeline জানেন কিনা, আর jank কোথায় খুঁজবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What is Choreographer?" · "Why does the UI stutter, and how do you find the cause?"

**বুঝে নিন:**
```
VSYNC ─► Choreographer (main thread)
          input → animation → traversal (measure → layout → draw = display list record)
       ─► RenderThread: display list sync → GPU command (HWUI, Skia / Vulkan বা GL)
       ─► buffer queue-তে buffer দেয় ─► SurfaceFlinger + Hardware Composer সব layer মেলায় ─► display
```
- **VSYNC:** display-এর refresh signal। 60 Hz → প্রতি **16.6 ms**, 90 Hz → 11.1 ms, 120 Hz → **8.3 ms**।
- **Choreographer:** প্রতি VSYNC-এ main thread-এ callback চালায় — input, animation, তারপর traversal।
- **Main thread কাজ:** measure, layout, draw। Draw মানে আসল pixel না — একটা **display list** (RenderNode) রেকর্ড করা।
- **RenderThread:** display list নিয়ে GPU command বানায়। এতে main thread জলদি ছাড়া পায়। Hardware-accelerated animation (যেমন `RenderNode` property) RenderThread-এ চলতে পারে।
- **SurfaceFlinger:** সব app-এর window আর SurfaceView-এর buffer মিলিয়ে চূড়ান্ত ছবি বানায়। HWC (Hardware Composer) সম্ভব হলে GPU ছাড়া মেলায়।
- **Compose:** একই pipeline। শুধু main thread-এর ধাপ হলো composition → layout → drawing।
- **Jank কোথা থেকে:**
  - Main thread-এ ভারী কাজ: disk/DB, JSON parse, বড় bitmap decode, synchronous Binder call।
  - বেশি measure/layout (nested weight, deep hierarchy), বা Compose-এ অপ্রয়োজনীয় recomposition (unstable parameter, state পড়া উপরের দিকে)।
  - GC pause বা অনেক allocation (scroll-এর সময় object বানানো)।
  - GPU-তে বেশি কাজ: overdraw, বড় blur/shadow।
  - প্রথম run-এ JIT/interpreted code (F2) — Baseline Profile সাহায্য করে।
- **Tool:** Perfetto / System trace, Android Studio Profiler, JankStats (production), Macrobenchmark `FrameTimingMetric`, Compose Layout Inspector-এ recomposition count।

**Answer (English):**
> "On every VSYNC, Choreographer runs on the main thread. It handles input, then animations, then measure, layout and draw. Draw only records a display list. RenderThread turns that list into GPU commands and gives a buffer to SurfaceFlinger, which combines all layers and sends them to the display. At 60 Hz the whole frame must finish in about 16 milliseconds, and at 120 Hz in about 8. Jank happens when we miss that deadline. The usual causes are heavy work on the main thread, too much layout or recomposition, allocation and GC during scroll, or heavy GPU work. I find the cause with a Perfetto trace, not by guessing."

**Key words:** `VSYNC` · `Choreographer` · `display list / RenderNode` · `RenderThread` · `SurfaceFlinger` · `HWC` · `frame deadline` · `Perfetto`

**Follow-up:**
- **Q:** If the main thread is free, can you still have jank?
  **A:** "Yes. RenderThread or the GPU can be slow, for example with heavy blur or overdraw. The trace shows if the time is on the main thread, RenderThread, or GPU."
- **Q:** How do you track jank in production?
  **A:** "I use JankStats to report slow frames with the current screen state, and I watch Play vitals. In the lab I use Macrobenchmark with FrameTimingMetric."
- **Q:** What changes with a 120 Hz screen?
  **A:** "The budget is about 8 milliseconds, so work that was fine at 60 Hz can now drop frames. I should not assume 60 Hz in animations. I use the frame time given by the system."

**ভুল করবেন না:** "draw() মানে pixel আঁকা" — hardware acceleration-এ draw শুধু command রেকর্ড করে; আঁকে RenderThread/GPU।

**আরও দেখুন:** [P4 · Jank](#p4) · [U2 · Recomposition](#u2) · [U11 · Compose performance](#u11)

---

### <a id="f6"></a>F6. ◆ What are Window, Surface, and SurfaceView vs TextureView?

**প্রশ্নটা মানে:** screen-এ জিনিস কীভাবে সাজানো হয়, আর video/camera-র জন্য কোন view কেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Why use SurfaceView for video playback?" · "When would you pick TextureView?"

**বুঝে নিন:**
- **Window:** screen-এর একটা চারকোনা অংশ, যেটা WindowManagerService (WMS) চেনে। প্রতিটা Activity-র একটা `PhoneWindow` আছে, তার root `DecorView`। Dialog, toast, IME — প্রতিটা আলাদা window।
- **ViewRootImpl:** View tree আর WMS-এর মধ্যে যোগাযোগ। Input নেয়, traversal চালায়।
- **Surface:** একটা buffer queue-এর producer দিক। App এতে আঁকে, SurfaceFlinger পড়ে। প্রতিটা window-এর একটা Surface (SurfaceFlinger-এ একটা layer)।
- **SurfaceView:** নিজের **আলাদা Surface/layer** নেয়। Camera বা video decoder সরাসরি সেখানে buffer দেয়। App-এর main thread বা RenderThread পার হয় না। SurfaceFlinger/HWC সরাসরি মেলায়।
  - লাভ: কম latency, কম GPU কাজ, কম battery, DRM protected video (secure surface) চলে।
  - Android 7 থেকে SurfaceView-এর position বাকি UI-এর সাথে sync থাকে। আগে scroll/animation-এ সমস্যা ছিল।
- **TextureView:** content একটা GL texture-এ যায়, তারপর app-এর নিজের window-এ View-এর মতো আঁকা হয়।
  - লাভ: সাধারণ View-এর মতো alpha, rotation, scale, clip।
  - খরচ: extra GPU composition, বেশি memory আর battery, প্রায় এক-দুই frame বেশি latency, hardware acceleration লাগে, secure (DRM) content দেখাতে পারে না।
- **বাস্তবে:**
  - Media3 `PlayerView` default SurfaceView।
  - CameraX `PreviewView`: `PERFORMANCE` mode = SurfaceView, `COMPATIBLE` mode = TextureView (যখন transform বা পুরনো device লাগে)।
  - Compose-এ: `AndroidExternalSurface` (SurfaceView-ভিত্তিক) আর `AndroidEmbeddedExternalSurface` (TextureView-ভিত্তিক)। CameraX-এর `CameraXViewfinder`, Media3-এর compose UI module।
- একসাথে অনেক camera tile (security camera grid) হলে SurfaceView-এর কম খরচ অনেক বড় পার্থক্য করে।

**Answer (English):**
> "Each Activity has a window, and each window has a Surface that SurfaceFlinger shows as a layer. A SurfaceView gets its own separate Surface. The camera or video decoder writes frames straight into it, and SurfaceFlinger composes it, often with the hardware composer. So it has low latency, uses less GPU and battery, and supports DRM content. A TextureView puts the frames into a GPU texture inside the app's own window. That lets me animate, rotate or fade it like a normal view, but it costs extra GPU work, memory and some latency. For video and camera I use SurfaceView by default, and TextureView only when I really need view transforms."

**Key words:** `WindowManagerService` · `ViewRootImpl` · `Surface` · `SurfaceFlinger layer` · `SurfaceView` · `TextureView` · `secure surface`

**Follow-up:**
- **Q:** You show 16 camera streams in a grid. What do you watch for?
  **A:** "Each stream needs a decoder and a surface. I use SurfaceView-based players, lower resolution substreams for small tiles, and I stop streams that are off screen. The device has a limit on hardware decoders, so I test that limit on the target device."

**আরও দেখুন:** [U10 · Compose + Views](#u10) · [V4 · Many camera feeds](#v4)

---

### <a id="f7"></a>F7. ◆ How does Intent resolution work?

**প্রশ্নটা মানে:** implicit intent কোন app-এ যাবে সেটা system কীভাবে ঠিক করে, আর package visibility ও App Links কী।
**অন্যভাবেও জিজ্ঞেস করে:** "How does Android choose which app opens a link?" · "Why does queryIntentActivities return an empty list?"

**বুঝে নিন:**
- **Explicit intent** (component নাম দেওয়া): সরাসরি সেই component। তবু `exported` আর permission check হয়।
- **Implicit intent:** **PackageManagerService** (system_server-এ) সব installed app-এর manifest-এর **intent filter** জানে। মেলায় তিনটা জিনিস:
  1. **action** — filter-এ থাকতে হবে।
  2. **category** — intent-এর সব category filter-এ থাকতে হবে। `startActivity` implicit intent-এ `CATEGORY_DEFAULT` যোগ করে, তাই activity filter-এ `DEFAULT` লাগে।
  3. **data** — scheme, host, port, path, MIME type।
- একাধিক মিললে: disambiguation dialog বা user-এর আগের পছন্দ। একটাও না মিললে `ActivityNotFoundException`।
- Android 14+: implicit intent শুধু **exported** component-এ যায়।
- **Package visibility (Android 11+ target):** app অন্য app দেখতে পায় না যদি না manifest-এ `<queries>` থাকে। তাই `queryIntentActivities` বা `resolveActivity` খালি ফেরত দেয়। `QUERY_ALL_PACKAGES` Play policy-তে সীমিত। (শুধু `startActivity` করতে visibility লাগে না।)
- **App Links:**
  - Filter-এ `android:autoVerify="true"` + `https` scheme + host।
  - Website-এ `https://<host>/.well-known/assetlinks.json` রাখুন, app-এর signing cert-এর SHA-256 সহ। Play App Signing হলে Play-এর key-এর fingerprint দিন।
  - Verify হলে link সরাসরি app-এ খোলে, dialog নেই। Android 12+: verify না হলে web link সাধারণত browser-এ খোলে।
  - Debug: `adb shell pm get-app-links <package>`, `adb shell pm verify-app-links --re-verify <package>`।

**Answer (English):**
> "For an explicit intent, the system goes straight to the named component, but it still checks export and permissions. For an implicit intent, PackageManagerService compares it with the intent filters of installed apps. It matches the action, all categories, and the data, like scheme, host and MIME type. If several apps match, the user picks one. Since Android 11, my app cannot see other apps unless I declare them in the queries element, so queries can return empty lists. For App Links, I set autoVerify, and I host assetlinks.json with my signing certificate fingerprint. Then verified links open my app with no dialog."

**Key words:** `PackageManagerService` · `intent filter` · `CATEGORY_DEFAULT` · `<queries>` · `package visibility` · `autoVerify` · `assetlinks.json`

**Follow-up:**
- **Q:** App Links stopped working after moving to Play App Signing. Why?
  **A:** "assetlinks.json probably has the upload key fingerprint, not the Play signing key. I add the fingerprint from Play Console and re-verify."

**ভুল করবেন না:** Activity-র intent filter-এ `android.intent.category.DEFAULT` বাদ দেওয়া — implicit `startActivity` মিলবে না।

**আরও দেখুন:** [C5 · Intents](#c5) · [C16 · App Links](#c16) · [C14 · Manifest](#c14)

---

### <a id="f8"></a>F8. ◆ How are runtime permissions enforced?

**প্রশ্নটা মানে:** permission শুধু dialog না — system আসলে কোথায় আর কীভাবে check করে।
**অন্যভাবেও জিজ্ঞেস করে:** "If I skip checkSelfPermission, can I still use the camera?" · "What are app ops?"

**বুঝে নিন:**
- **Permission-এর ধরন:** normal (install-এ দেওয়া), dangerous/runtime (user দেয়), signature (একই key-এ sign করা app বা platform), privileged (`/system/priv-app` + allowlist), আর app-op ভিত্তিক special access (যেমন `SYSTEM_ALERT_WINDOW`, usage stats)।
- **Grant কোথায় থাকে:** system-এর permission service (PackageManager / PermissionManager, আর UI ও নিয়মের জন্য **PermissionController** Mainline module)। প্রতি UID-এর জন্য রাখে।
- **আসল check হয় service-এর ভেতরে, app-এ না:**
  1. App `CameraManager.openCamera()` call করে → Binder → cameraserver।
  2. Service `Binder.getCallingUid()` দিয়ে caller কে চেনে।
  3. Permission check করে (`checkCallingPermission` / native-এ same idea)। না থাকলে `SecurityException`।
- তাই `checkSelfPermission` শুধু **app-এর নিজের জানার জন্য** (UI ঠিক করতে)। Skip করলে সুরক্ষা ভাঙে না — শুধু crash হয়।
- **Kernel-level কিছু permission:** যেমন `INTERNET` permission process-কে একটা Linux group (`inet`) দেয়। Socket খুলতে kernel check করে।
- **App ops (AppOpsManager):** permission-এর উপরে আরেক layer। প্রতি operation-এর mode: allowed / ignored / foreground-only। যেমন:
  - "Only while using the app" location = foreground-only mode।
  - Mic/camera privacy toggle আর privacy indicator এখান থেকে।
  - Background-এ camera block (Android 9+)।
- Storage: scoped storage-এ access FUSE + MediaProvider enforce করে।

**Answer (English):**
> "The permission dialog only records the user's choice. The real check happens inside the system service. When my app calls the camera, the call goes over Binder to the camera service. The service gets my UID from Binder, which I cannot fake, and checks if that UID has the permission. If not, it throws a SecurityException. So checkSelfPermission is only for my own UI flow. Some permissions are also enforced by the kernel, like INTERNET through a Linux group. On top of permissions there are app ops. They handle things like foreground-only location, the camera and mic privacy toggles, and blocking the camera in the background."

**Key words:** `Binder.getCallingUid` · `SecurityException` · `AppOpsManager` · `PermissionController` · `signature permission` · `foreground-only`

**Follow-up:**
- **Q:** The user granted camera, but the camera fails in the background. Why?
  **A:** "Since Android 9, apps in the background cannot use the camera. An app op blocks it even with the permission. I need a visible activity, or a foreground service with the camera type started while the app is visible."

**ভুল করবেন না:** "`checkSelfPermission` হলো security" — security check system service-এর ভেতরে।

**আরও দেখুন:** [C13 · Runtime permissions](#c13) · [F13 · Security model](#f13)

---

### <a id="f9"></a>F9. ◆ How does memory work for an Android app?

**প্রশ্নটা মানে:** heap limit, native memory, GC, আর system কখন app মেরে ফেলে — এগুলো বুঝে memory সমস্যা ঠিক করতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why do you get OutOfMemoryError when the phone has free RAM?" · "What is the low memory killer?"

**বুঝে নিন:**
- **Java/Kotlin heap-এর limit আছে, প্রতি app-এ।** Device অনুযায়ী (`ActivityManager.getMemoryClass()`)। Limit পার হলে `OutOfMemoryError`, phone-এ RAM খালি থাকলেও।
  - `android:largeHeap="true"` বড় limit দেয় (`getLargeMemoryClass()`)। কিন্তু GC ধীর হয়, app background-এ আগে মারা যায়। Leak ঢাকে, ঠিক করে না। শেষ উপায়।
- **Native memory:** C/C++ (NDK, codec, Flutter engine, ML model) এর আলাদা। Java heap limit-এ গোনা হয় না, কিন্তু পুরো process memory-তে গোনা হয়।
- **Bitmap:** Android 8 থেকে bitmap-এর pixel data **native heap-এ**। Java heap-এ শুধু ছোট object। তাই Java OOM কম, কিন্তু process memory তবু বাড়ে। Hardware bitmap (`Bitmap.Config.HARDWARE`) GPU memory-তে থাকে।
- **ART GC:**
  - Android 8: Concurrent Copying (CC) collector — বেশিরভাগ কাজ app চলার সময়ই, pause খুব ছোট।
  - Android 10: generational (young object আলাদা, ঘন ঘন আর সস্তায় collect)।
  - নতুন ART module-এ (Android 14-এর সময় থেকে) Concurrent Mark-Compact (CMC) collector এসেছে, Linux `userfaultfd` দিয়ে। কোন device-এ কোনটা চলে, সেটা ART version-এর উপর নির্ভর করে — source.android.com দেখুন।
  - তবু অনেক allocation = বেশি GC = CPU আর jank।
- **System কখন app মারে:**
  - Kernel PSI (memory pressure) দেখে user-space **`lmkd`** process-গুলোর গুরুত্ব (`oom_score_adj`) অনুযায়ী মারে: cached/background আগে, foreground শেষে।
  - তাই background-এ গেলে process যেকোনো সময় শেষ — state save করুন (SavedStateHandle, DB)।
- **`onTrimMemory`:** system app-কে memory ছাড়তে বলে। Android 14 (API 34) থেকে app শুধু `TRIM_MEMORY_UI_HIDDEN` (UI চলে গেছে) আর `TRIM_MEMORY_BACKGROUND` পায়; বাকি level (`RUNNING_*`, `MODERATE`, `COMPLETE`) আর আসে না, API 35-এ deprecated। `onLowMemory()`-ও API 34 থেকে আর ডাকা হয় না। Cache ছাড়ুন।
- **Tool:** Android Studio Memory Profiler (heap dump), LeakCanary (debug build), `adb shell dumpsys meminfo <pkg>`, Perfetto heap profile (native-এর জন্য)।

**Answer (English):**
> "Each app has a limit for its Java and Kotlin heap, so I can get OutOfMemoryError even when the phone has free RAM. largeHeap raises the limit, but it hides leaks and makes GC slower, so I avoid it. Native memory, like codecs, NDK code and ML models, is separate from that limit, but it still counts for the whole process. Since Android 8, bitmap pixels live in native memory. ART uses a concurrent garbage collector with very short pauses, but lots of allocation still costs CPU and can cause jank. When memory is low, lmkd kills processes by priority, background first. So I free caches in onTrimMemory and always save state."

**Key words:** `memory class` · `largeHeap` · `native heap` · `concurrent GC` · `generational` · `lmkd` · `oom_score_adj` · `onTrimMemory`

**Follow-up:**
- **Q:** How do you find a memory leak?
  **A:** "In debug builds I use LeakCanary. It shows the reference chain that keeps an Activity or Fragment alive. Then I check with a heap dump in the Memory Profiler. Common causes are static references to Context and listeners that are never removed."
- **Q:** dumpsys meminfo shows a big native heap. What next?
  **A:** "Java tools will not show it. I use Perfetto's native heap profiler to see which code allocates. In camera apps it is often decoder buffers, bitmaps or image buffers that are not closed."

**ভুল করবেন না:** `largeHeap` দিয়ে OOM "ঠিক" করা — leak থেকেই যায়।

**আরও দেখুন:** [P2 · Memory leaks](#p2) · [C18 · Process kill](#c18) · [R12 · Images and OOM](#r12)

---

### <a id="f10"></a>F10. ◆ What threads does an Android app have?

**প্রশ্নটা মানে:** app process-এ কোন কোন thread থাকে, কোন callback কোন thread-এ আসে, আর StrictMode কেন দরকার।
**অন্যভাবেও জিজ্ঞেস করে:** "Which thread runs a bound service's AIDL method?" · "How does StrictMode help?"

**বুঝে নিন:**
| Thread | কী করে |
|---|---|
| **main (UI) thread** | Looper + MessageQueue। Lifecycle, input, View/Compose, `BroadcastReceiver.onReceive`, `Service.onStartCommand` |
| **Binder threads** (`binder:<pid>_N`) | অন্য process থেকে আসা call চালায়: AIDL service method, `ContentProvider` query (অন্য app থেকে) — **main thread-এ না** |
| **RenderThread** | GPU-তে frame পাঠায় (F5) |
| ART thread | `HeapTaskDaemon` (GC), `FinalizerDaemon`, JIT thread, `Signal Catcher` (ANR-এর সময় stack dump) |
| আপনার thread | `Dispatchers.Default` (CPU core সমান), `Dispatchers.IO` (বেশি, blocking কাজ), OkHttp, WorkManager executor, `HandlerThread` (Camera2 callback-এর জন্য সাধারণ) |

- **Binder thread মানে thread-safety:** AIDL method একসাথে অনেক binder thread-এ চলতে পারে। Shared state lock বা single thread-এ রাখুন।
- **ANR:** main thread আটকালে। মোটামুটি: input event-এ ~5 সেকেন্ড response নেই, বা broadcast/service নির্দিষ্ট সময়ে শেষ হয়নি। ANR-এর সময় system সব thread-এর stack dump নেয় (Play Console-এ দেখা যায়)।
- **StrictMode:** debug build-এ ভুল ধরে:
```kotlin
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder().detectDiskReads().detectDiskWrites()
            .detectNetwork().penaltyLog().build())
    StrictMode.setVmPolicy(
        StrictMode.VmPolicy.Builder().detectLeakedClosableObjects()
            .detectActivityLeaks().penaltyLog().build())
}
```
  - Main thread-এ disk/network, close না করা Cursor/stream, leak হওয়া Activity — এগুলোই লুকানো ANR আর leak-এর কারণ।

**Answer (English):**
> "Every app has the main thread with a Looper. It runs lifecycle callbacks, input, drawing and broadcast receivers. There is a pool of Binder threads that run incoming IPC calls, like AIDL methods or provider queries from other apps, so that code must be thread-safe. RenderThread sends frames to the GPU. ART has its own threads for GC, finalizers and JIT. Then there are my threads, mostly coroutine dispatchers and things like a HandlerThread for Camera2 callbacks. I turn on StrictMode in debug builds. It catches disk and network work on the main thread and leaked closeable objects before they become ANRs or leaks in production."

**Key words:** `main Looper` · `binder thread pool` · `RenderThread` · `HandlerThread` · `ANR` · `StrictMode`

**Follow-up:**
- **Q:** Why do Camera2 callbacks often use a HandlerThread?
  **A:** "Camera2 takes a Handler or Executor for callbacks. Using a background HandlerThread keeps camera events off the main thread, so a busy UI does not delay them, and the order of events stays the same."

**ভুল করবেন না:** "AIDL method main thread-এ চলে" — অন্য process থেকে এলে binder thread-এ চলে।

**আরও দেখুন:** [C12 · Main thread](#c12) · [K9 · Dispatchers](#k9) · [F3 · Binder](#f3)

---

### <a id="f11"></a>F11. ★ How do system services work? (getSystemService to the HAL)

**প্রশ্নটা মানে:** `getSystemService()` থেকে hardware পর্যন্ত পথ জানেন কিনা — camera আর sensor stack সহ।
**অন্যভাবেও জিজ্ঞেস করে:** "What happens when you call LocationManager.requestLocationUpdates?" · "Explain the Android camera stack."

**বুঝে নিন:**
**সাধারণ পথ:**
1. `context.getSystemService(CameraManager::class.java)` → `SystemServiceRegistry` cached একটা Manager দেয়।
2. Manager ভেতরে `ServiceManager` থেকে service-এর **Binder** নেয় (নাম দিয়ে, যেমন "location")। AIDL proxy বানায়।
3. Manager method → Binder call → service process।
4. Service UID/permission/app-op check করে, তারপর কাজ করে — প্রায়ই **HAL**-কে call করে।
5. Result বা callback ফেরত Binder দিয়ে app-এ (binder thread-এ, তারপর আপনার Handler/Executor-এ)।

**কোন service কোথায়:**
| Manager | Service | নিচে |
|---|---|---|
| `LocationManager` | LocationManagerService (system_server) | GNSS HAL, network/fused provider |
| `SensorManager` | SensorService (system_server-এর native অংশ) | Sensors HAL (AIDL `ISensors`, multi-HAL) → sensor hub/driver |
| `CameraManager` | **CameraService (`cameraserver` আলাদা process)** | Camera HAL (নতুন = AIDL, পুরনো = HIDL) → camera driver/ISP |

- **Sensor data কীভাবে আসে:** প্রতি event-এ Binder call হয় না। SensorService একটা event channel (socket pair) দিয়ে stream পাঠায়। App-এ `SensorEventListener` callback। Batching (`maxReportLatencyUs`) দিলে sensor hub data জমিয়ে পাঠায় — battery বাঁচে।
- **Camera data কীভাবে আসে:** frame Binder দিয়ে আসে না। HAL সরাসরি app-এর দেওয়া **Surface**-এ (SurfaceView, ImageReader, MediaCodec) buffer লেখে। Binder দিয়ে শুধু control (request, metadata, result)।
- **কেন জানা দরকার:** camera "busy", HAL crash, sensor rate কম — এসব debug করতে `adb shell dumpsys media.camera`, `dumpsys sensorservice`, `dumpsys location`। AOSP/custom device-এ HAL vendor লেখে, আর নতুন HAL-এ stable AIDL লাগে (HIDL Android 13 থেকে deprecated)।

**Answer (English):**
> "getSystemService gives me a manager class, but the manager is only a client. Inside, it gets a Binder from ServiceManager and calls the real service in another process. Most services live in system_server, like LocationManagerService and SensorService. The camera service runs in its own process, cameraserver. The service checks my UID and permissions, then talks to the hardware through a HAL, which the vendor writes. New HALs use stable AIDL. Big data does not go through Binder. Camera frames go straight from the HAL into my Surface, and sensor events come through an event channel. For debugging, I use dumpsys on the camera and sensor services."

**Key words:** `SystemServiceRegistry` · `ServiceManager` · `Binder proxy` · `system_server` · `cameraserver` · `SensorService` · `HAL` · `stable AIDL` · `dumpsys`

**Follow-up:**
- **Q:** openCamera fails with "camera in use". How do you debug it?
  **A:** "I run dumpsys media.camera to see which client holds the camera and its priority. A higher-priority client can take the camera, and I get onDisconnected. My app must handle that and reopen later."
- **Q:** Sensor events arrive slower than you asked. Why?
  **A:** "The rate is only a hint. The HAL and the hardware decide the real rate. Above 200 Hz I need the HIGH_SAMPLING_RATE_SENSORS permission, and in the background continuous sensors stop. I check the real rate with the event timestamps."
- **Q:** Where does a custom system service go in AOSP?
  **A:** "Usually as a service in system_server or as its own native process, registered with ServiceManager, with an AIDL interface and SELinux rules. Apps then reach it through a manager class or a signature permission."

**ভুল করবেন না:** "Camera frame Binder দিয়ে app-এ আসে" — না, buffer সরাসরি Surface-এ যায়।

**আরও দেখুন:** [O2 · Platform layers](#o2) · [V1 · CameraX vs Camera2](#v1) · [N1 · Sensors](#n1)

---

### <a id="f12"></a>F12. ★ What is new in Android development in 2025–2026?

**প্রশ্নটা মানে:** আপনি platform-এর খবর রাখেন কিনা — নতুন OS নিয়ম, Play-এর নিয়ম, Compose, tooling, AI।
**অন্যভাবেও জিজ্ঞেস করে:** "What changed in Android recently that affects your app?" · "How do you keep up with Android?"

**বুঝে নিন:**
(late 2026 পর্যন্ত। version নম্বর দ্রুত বদলায় — interview-এর আগে release page একবার দেখে নিন।)

**Platform:**
- **Android 16 (API 36, June 2025):** predictive back animation default (target 36), edge-to-edge opt-out শেষ, বড় screen (≥600dp)-এ orientation/resizability lock ignore (সাময়িক opt-out ছিল), progress-centric notification (`ProgressStyle`)। Google এখন বছরে দুই SDK release দেয় (Q2 বড়, Q4 ছোট)।
- **Android 17 (API 37, stable 16 June 2026)** — target 37 হলে:
  - বড় screen-এ resizability নিয়ম মানতেই হবে (opt-out নেই; `appCategory="game"` বাদ)।
  - **LAN-এ device খুঁজতে বা connect করতে `ACCESS_LOCAL_NETWORK` runtime permission** লাগে। IP camera আর ONVIF discovery-র জন্য বড় বিষয়।
  - Certificate transparency default চালু।
  - OTP-ওয়ালা সাধারণ SMS বেশিরভাগ app **৩ ঘণ্টা পরে** পায়। SMS Retriever / User Consent API ব্যবহার করুন।
  - Lock-free MessageQueue। Reflection দিয়ে `static final` field বদলানো যায় না।
- **16 KB page size:** Android 15+ target আর native code থাকলে Play-তে 16 KB support লাগবে (Nov 2025 থেকে)।
- **Play target API:** নতুন app আর update-কে **API 36** target করতে হবে (31 Aug 2026 থেকে)।
- **Developer verification:** certified device-এ install হওয়া app-এর developer verified হতে হবে। Enforcement শুরু 30 Sep 2026 — Brazil, Indonesia, Singapore, Thailand। 2027-এ বাকি দেশ। ADB দিয়ে install-এ verification লাগে না। Play-এর বাইরে distribute করলে Android Developer Console। (বিস্তারিত নিয়ম বদলাচ্ছে — official page দেখুন।)

**Jetpack / Compose:**
- **Navigation 3** stable (1.0.0, 19 Nov 2025; এখন 1.2.x): Compose-first, back stack নিজের হাতে একটা list।
- **Material 3 Expressive:** Wear OS-এ stable। Phone-এর `compose-material3` **1.5.0 stable (18 Nov 2026)** — Expressive-এর বেশিরভাগ component (button group, split button, toolbar, wavy progress ইত্যাদি) এখন stable। কিছু API এখনো experimental (যেমন `LoadingIndicator`, `MaterialShapes`) — ব্যবহারের আগে API page দেখুন।
- Compose BOM দিয়ে version মেলানো; strong skipping default; Compose compiler Kotlin-এর সাথে আসে।

**Kotlin / build:**
- **Kotlin 2.x + K2;** 2.4 (2026)-এ context parameters stable (K25)।
- **AGP 9 (early 2026): built-in Kotlin** — `org.jetbrains.kotlin.android` plugin লাগে না (দিলে build fail); নতুন DSL; KMP-এর জন্য `com.android.kotlin.multiplatform.library` plugin। Flutter plugin-গুলোরও migrate করতে হয়েছে।
- **KMP** Google-supported; **Compose Multiplatform for iOS stable** (2025)।
- KSP, R8 full mode, Baseline Profiles — default practice।

**AI:**
- **Gemini in Android Studio:** Agent Mode, অন্য LLM ব্যবহারের সুযোগ, MCP। Studio release-এর নাম প্রাণীর নামে, alphabet ক্রমে (Narwhal, Otter, Panda, Quail…)।
- **On-device:** Gemini Nano via **ML Kit GenAI APIs** (summarize, proofread, rewrite, image description) আর **Prompt API** (2026-এ beta)। Device support সীমিত। সাধারণ ML-এ ML Kit আর **LiteRT** (আগের TFLite)।

**Answer (English):**
> "A few things matter most to me. Android 16 made predictive back and edge-to-edge the default, and Android 17 removed the large-screen orientation opt-out. Android 17 also added the ACCESS_LOCAL_NETWORK permission, which is important for apps that talk to cameras on the local network. On Play, new apps and updates must target API 36 now, apps with native code must support 16 KB pages, and developer verification is starting in some countries. In Jetpack, Navigation 3 is stable. In tooling, AGP 9 has built-in Kotlin, and K2 is the normal compiler. For AI, there is Agent Mode in Android Studio and Gemini Nano on device through ML Kit. I follow the Android Developers blog and release notes."

**Key words:** `API 36 / 37` · `ACCESS_LOCAL_NETWORK` · `16 KB page size` · `developer verification` · `Navigation 3` · `AGP 9 built-in Kotlin` · `Gemini Nano` · `ML Kit GenAI`

**Follow-up:**
- **Q:** Which Android 17 change would hit a security camera app first?
  **A:** "Local network protection. When the app targets API 37, discovering or connecting to cameras on the LAN needs the ACCESS_LOCAL_NETWORK runtime permission. So I add the permission request, a clear reason screen, and a path for when the user says no."
- **Q:** What did you need to do for 16 KB pages?
  **A:** "Rebuild native libraries with a recent NDK and AGP so they are 16 KB aligned, update third-party SDKs with .so files, and test on a 16 KB emulator image. Play shows if the bundle is not compliant."
- **Q:** Would you move to Navigation 3 now?
  **A:** "For a new Compose app, yes, I would look at it first, because I own the back stack and it fits adaptive layouts. For a big working app on Navigation Compose, I would not migrate just for the sake of it."

**ভুল করবেন না:** "Play-তে API 35 target যথেষ্ট" — নতুন app/update-এ 31 Aug 2026 থেকে API 36 লাগে।

**আরও দেখুন:** [P11 · Android versions](#p11) · [K25 · Kotlin 2.x](#k25) · [U13 · Edge-to-edge](#u13)

---

### <a id="f13"></a>F13. ○ What does the Android platform security model look like?

**প্রশ্নটা মানে:** Android-এর security layer-গুলো এক ছবিতে বলতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How does Android isolate apps?" · "What protects the system if an app is compromised?"

**বুঝে নিন:**
Layer-গুলো একে অপরের উপর (defense in depth):
1. **App sandbox:** প্রতি app-এর আলাদা Linux **UID** আর private data dir। Kernel file permission দিয়ে আলাদা রাখে।
2. **SELinux (enforcing, Android 5 থেকে পুরো):** mandatory access control। UID ঠিক থাকলেও policy যা allow করে না, সেটা হবে না। App-রা `untrusted_app` domain-এ। AOSP-তে নতুন service/HAL-এর জন্য নিজের SELinux policy লিখতে হয়।
3. **seccomp-bpf (Android 8+):** app process কোন system call করতে পারবে সেটা সীমিত (Zygote থেকে আসে)। Kernel-এর attack surface কমে।
4. **Permissions + app ops:** system service-এ check (F8)।
5. **Verified Boot (AVB):** boot chain-এর প্রতিটা partition sign করা। `dm-verity` runtime-এ system partition check করে। Rollback protection পুরনো, bug-ওয়ালা image-এ ফেরত যাওয়া আটকায়।
6. **Encryption:** File-Based Encryption (FBE), user-এর lock screen credential-এর সাথে যুক্ত।
7. **Hardware-backed key:** Keystore — TEE বা StrongBox-এ key। Key বের করা যায় না। Key attestation।
8. **Update:** monthly security patch, আর Mainline module (ART, media, permission ইত্যাদি) Play দিয়ে update।

**Answer (English):**
> "Android uses several layers. Each app runs with its own Linux UID, so the kernel keeps its files private. SELinux in enforcing mode adds rules that even a correct UID cannot break. Seccomp limits which system calls an app process can make. On top, system services check permissions and app ops on every Binder call. Verified Boot checks that the system image is signed and not changed, and dm-verity keeps checking it at runtime. Data is protected with file-based encryption, and keys live in hardware through Keystore. If one layer fails, the next one still protects the device."

**Key words:** `UID sandbox` · `SELinux` · `seccomp` · `Verified Boot` · `dm-verity` · `FBE` · `Keystore / StrongBox` · `Mainline`

**Follow-up:**
- **Q:** You add a new native service in AOSP and it fails with "avc: denied". What is that?
  **A:** "It is an SELinux denial. The service's domain is not allowed that action. I read the denial in logcat or dmesg, then add a proper type and the smallest allow rule in the device policy. I do not switch SELinux to permissive in a product build."

**আরও দেখুন:** [S1 · App security](#s1) · [O7 · SELinux](#o7) · [O11 · Verified boot](#o11)

---


## <a id="part-2c"></a>Part 2C — Jetpack আর Android-এর basics

এই অংশ প্রতিদিনের Android কাজের ভিত্তি: Jetpack library, project-এর গঠন, Application class, lifecycle, পুরনো Android-এ support, View আর resource।
Interview-এ এগুলো প্রায়ই প্রথম ১০ মিনিটে আসে। ভালো উত্তর দিলে বোঝা যায় আপনি সত্যিই native project চালিয়েছেন।

### আগে বুঝুন — Jetpack আর Android app-এর গঠন

**Jetpack কী:** Google-এর বানানো library-র একটা বড় set। Package নাম `androidx.*`। আগে এর নাম ছিল Support Library (`android.support.*`)। সেটা version 28.0.0-এ থেমে গেছে। এখন সব নতুন কাজ AndroidX-এ।

**কেন আছে — দুইটা মূল কারণ:**
1. **Backward compatibility:** Framework API phone-এর Android version-এর সাথে আসে। User-এর phone পুরনো হলে নতুন API নেই। AndroidX একই API পুরনো version-এও দেয়, বা ভেতরে `SDK_INT` check করে সামলায়।
2. **OS থেকে আলাদা release:** Framework বদলায় বছরে একবার। AndroidX library আলাদা আলাদা version-এ, অনেক বেশিবার আসে। Bug fix পেতে user-এর OS update লাগে না — আপনি শুধু dependency বাড়ান।

**App-এর গঠন (উপর থেকে নিচে):**
```
UI          : Compose (+ Material 3)   বা  Views (XML, RecyclerView)
State       : ViewModel + StateFlow, SavedStateHandle
Navigation  : Navigation Compose / Navigation 3
Data        : Repository → Room, DataStore, Retrofit/OkHttp
Background  : WorkManager (+ foreground service যখন user দেখছে)
DI          : Hilt
Lifecycle   : Activity / Fragment = LifecycleOwner, সবাই এর ওপর ভর করে
```

**Jetpack library → কী করে → 2026-এ নতুন app-এ team ব্যবহার করে?**

| Library | কী করে | 2026-এ? |
|---|---|---|
| Core KTX (`core-ktx`) | Framework API-এর Kotlin extension, `ContextCompat`, `NotificationCompat`, `WindowCompat` | হ্যাঁ, সব app-এ |
| AppCompat | পুরনো Android-এ নতুন View feature, `AppCompatActivity`, per-app language backport | View app-এ হ্যাঁ। শুধু Compose app-এ প্রায়ই লাগে না |
| Activity (`activity-compose`) | `ComponentActivity`, `setContent`, Activity Result API, back handling, `enableEdgeToEdge()` | হ্যাঁ |
| Fragment | Screen-এর অংশ, নিজের lifecycle | পুরনো/View app-এ হ্যাঁ। নতুন Compose app-এ সাধারণত না |
| Lifecycle | `Lifecycle`, `LifecycleOwner`, `repeatOnLifecycle`, `collectAsStateWithLifecycle` | হ্যাঁ, সব app-এ |
| ViewModel | UI state রাখে, rotation-এ টিকে থাকে | হ্যাঁ |
| SavedState | `SavedStateHandle` — process death-এর পরও ছোট state ফেরত | হ্যাঁ |
| Navigation | Navigation Compose: type-safe `@Serializable` route | হ্যাঁ (অনেক app-এ এখনো এটা) |
| Navigation 3 | Compose-first; back stack আপনার নিজের list | হ্যাঁ, নতুন Compose app-এ বাড়ছে (1.0 stable Nov 2025) |
| Compose + Material 3 | Declarative UI আর design system | হ্যাঁ, নতুন UI-এর default |
| Room | SQLite-এর ওপর ORM, Flow query, migration, KMP support | হ্যাঁ |
| DataStore | Key-value বা Proto settings, coroutine/Flow ভিত্তিক | হ্যাঁ (SharedPreferences-এর জায়গায়) |
| WorkManager | যে কাজ app বন্ধ হলেও হতেই হবে (sync, upload) | হ্যাঁ |
| Paging 3 | বড় list পাতা পাতা করে load | যেখানে বড় list আছে |
| Hilt | DI (Dagger-এর ওপর); `androidx.hilt` ViewModel/WorkManager integration | হ্যাঁ, সবচেয়ে common DI |
| App Startup | Startup-এ library init এক জায়গায়, lazy করা যায় | হ্যাঁ, startup tuning-এ |
| SplashScreen (`core-splashscreen`) | Android 12-এর splash API পুরনো version-এও | হ্যাঁ |
| Activity Result API | `startActivityForResult` আর permission callback-এর জায়গায় | হ্যাঁ |
| CameraX | Camera-র সহজ API, Compose viewfinder | হ্যাঁ, camera app-এ default |
| Media3 | ExoPlayer, MediaSession, editing (Transformer) | হ্যাঁ; পুরনো `exoplayer2` deprecated |
| Biometric | `BiometricPrompt` | হ্যাঁ |
| Credential Manager (`androidx.credentials`) | Password, passkey, Sign in with Google | হ্যাঁ; পুরনো Google Sign-In/One Tap deprecated |
| Window / adaptive | Foldable info (`WindowManager`), window size class, adaptive layout | হ্যাঁ, large screen support-এ |
| Benchmark + Baseline Profiles | Macrobenchmark দিয়ে মাপা, profile দিয়ে startup/scroll দ্রুত | হ্যাঁ, ভালো team-এ |
| Glance | Compose-এর মতো code দিয়ে home screen widget | Widget লাগলে হ্যাঁ |
| Health Connect | Health/fitness data এক জায়গায় (Android 14+ এ OS-এর অংশ) | Health app-এ |
| RecyclerView / ConstraintLayout | View world-এর list আর layout | পুরনো/View screen-এ হ্যাঁ, নতুন Compose screen-এ না |
| LiveData | Lifecycle-aware observable | **Legacy** — নতুন code-এ StateFlow/Flow। Deprecated না, কিন্তু প্রথম পছন্দ না |
| security-crypto | `EncryptedSharedPreferences`, `EncryptedFile` | **Deprecated** — Keystore + Tink ব্যবহার করুন |

**৬টা মূল ধারণা:**
1. **AndroidX library আলাদা আলাদা version-এ চলে।** Compose-এর জন্য **BOM** (Bill of Materials) একসাথে মিলিয়ে রাখা version দেয়। Version গুলো রাখা হয় version catalog (`libs.versions.toml`)-এ।
2. **`Compat` class = backward compatibility।** `ContextCompat`, `NotificationCompat`, `ViewCompat` নিজে `SDK_INT` check করে।
3. **Lifecycle সবকিছুর ভিত্তি।** ViewModel, Flow collect, CameraX — সবাই `LifecycleOwner` দেখে চালু/বন্ধ হয়।
4. **Compose এখন UI-এর default।** কিন্তু অনেক পুরনো app-এ View, Fragment, RecyclerView আছে। দুটোই পড়তে জানতে হবে।
5. **"Legacy" মানে broken না।** LiveData, Fragment, DataBinding এখনো কাজ করে। নতুন code-এ শুধু ভালো বিকল্প আছে।
6. **Deprecated জিনিস নতুন code-এ নয়:** `security-crypto`, `startActivityForResult`, `onBackPressed()`, `AsyncTask`, kapt (KSP ব্যবহার করুন)।

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ `pubspec.yaml`-এ package যোগ করেন। Android-এ Gradle module-এর `dependencies {}` আর version catalog।
- Flutter-এ `AppLifecycleState` একটাই। Android-এ প্রতিটা Activity, Fragment আর পুরো process-এর আলাদা lifecycle আছে।
- Flutter plugin-এর ভেতরে (Android side) এই AndroidX library-গুলোই চলে — যেমন `camera` plugin CameraX ব্যবহার করে।
- Flutter-এ `ThemeData` আর asset। Android-এ `res/` folder, qualifier (`values-night`, `values-bn`) আর theme attribute।

---

### <a id="j1"></a>J1. ★ What is Android Jetpack / AndroidX? Why use it instead of only framework APIs?

**প্রশ্নটা মানে:** Jetpack কী, আর framework API থাকতে কেন আলাদা library লাগে — এর আসল কারণ জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between the Support Library and AndroidX?" · "Why is AndroidX released separately from Android?"

**বুঝে নিন:**
- **Framework API** (`android.*`) phone-এর OS-এর ভেতরে থাকে। User-এর phone যে version, API সেটাই। আপনি বদলাতে পারেন না।
- **AndroidX** (`androidx.*`) আপনার APK-এর ভেতরে যায়। তাই সব phone-এ একই code, একই behavior।
- লাভ:
  - **Backward compatibility:** নতুন feature পুরনো Android-এ (যেমন SplashScreen API, Photo Picker contract, edge-to-edge helper)।
  - **আলাদা release:** OS update ছাড়াই bug fix আর নতুন feature।
  - **Best practice বানানো আছে:** ViewModel, Room, WorkManager — Google-এর recommended architecture এগুলো দিয়েই।
  - **Kotlin-first:** coroutine, Flow, KTX extension।
- **Support Library → AndroidX:** `android.support.*` শেষ version 28.0.0। এখন সব `androidx.*`। পুরনো library-র জন্য Jetifier ছিল, এখন প্রায় লাগে না — নতুন project-এ বন্ধ রাখুন।
- খরচ: APK একটু বড় (R8 অব্যবহৃত code সরায়)। আর dependency version মেলাতে হয় — BOM আর version catalog এটা সহজ করে।

**Answer (English):**
> "Jetpack is a set of Google libraries under the androidx package. The main reason is backward compatibility. Framework APIs ship with the OS, so a user on an old phone does not get new APIs. AndroidX ships inside my APK, so I get the same behavior on old and new versions. It is also released separately from Android, so I get fixes without waiting for an OS update. It replaced the old Support Library. The trade-off is that I must keep many library versions in sync, so I use the Compose BOM and a version catalog."

**Key words:** `androidx` · `backward compatibility` · `unbundled` · `Support Library` · `BOM` · `version catalog`

**Follow-up:**
- **Q:** Do you still need Jetifier?
  **A:** "Usually no. Jetifier rewrote old Support Library imports. Almost all libraries use AndroidX now, so I keep it off. It also makes the build slower."
- **Q:** What is a BOM?
  **A:** "A Bill of Materials. It is one version that picks a tested set of versions for a group of libraries, like Compose. I set the BOM version and leave the single library versions empty."
- **Q:** Is Hilt part of Jetpack?
  **A:** "Hilt is built on Dagger by Google. The androidx.hilt libraries add Jetpack integration, for ViewModel, WorkManager and Navigation. Google recommends it for DI on Android."

**ভুল করবেন না:** "Jetpack মানে Compose" বলা — Compose Jetpack-এর একটা অংশ মাত্র।

**আরও দেখুন:** [J11 · Modern stack](#j11) · [J5 · Backward compatibility](#j5) · [P12 · Gradle basics](#p12)

---

### <a id="j2"></a>J2. ★ Walk me through an Android project structure.

**প্রশ্নটা মানে:** একটা Android project খুললে কোন file/folder কী কাজ করে, আর build কোথায় যায় — জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is in the res folder?" · "What is the difference between the project and the module build.gradle?"

**বুঝে নিন:**
```
MyApp/
├─ settings.gradle.kts        ← কোন module আছে (include(":app", ":core:data")), plugin/repo কোথা থেকে
├─ build.gradle.kts           ← root: plugin version declare (apply false), সাধারণত ছোট
├─ gradle/libs.versions.toml  ← version catalog: [versions] [libraries] [plugins]
├─ gradle.properties          ← JVM memory, android.useAndroidX, build flags
├─ gradle/wrapper/            ← Gradle version ঠিক করা (সবাই একই Gradle চালায়)
└─ app/
   ├─ build.gradle.kts        ← module: namespace, minSdk/targetSdk, buildTypes, flavors, dependencies
   ├─ proguard-rules.pro      ← R8 keep rule
   ├─ src/main/
   │  ├─ AndroidManifest.xml  ← component, permission, app-এর পরিচয়
   │  ├─ kotlin/ (বা java/)   ← source code
   │  └─ res/                 ← resource (নিচে)
   ├─ src/test/               ← JVM unit test
   ├─ src/androidTest/        ← device/emulator test
   └─ build/                  ← build output (git-এ যায় না)
```
**`res/` folder:**
| Folder | কী থাকে |
|---|---|
| `layout/` | XML layout (View world) |
| `drawable/` | Vector, shape, PNG, selector |
| `mipmap/` | শুধু launcher icon (adaptive icon) — launcher বড় density নিতে পারে, তাই আলাদা |
| `values/` | `strings.xml`, `colors.xml`, `dimens.xml`, `themes.xml` |
| `xml/` | Config XML: `network_security_config`, FileProvider paths, backup rules, widget info |
| `raw/` | File যেমন আছে তেমন (sound, JSON); `R.raw.x` দিয়ে খোলা যায় |
| `font/`, `menu/`, `anim/` | Font, menu, View animation |
- `assets/` (`res/`-এর বাইরে): কোনো ID নেই, path দিয়ে খোলেন (`assets.open("a.json")`)।
- **Build output:** `app/build/outputs/apk/<variant>/` (APK), `app/build/outputs/bundle/<variant>/` (AAB), `outputs/mapping/` (R8 mapping file)। `build/generated/` এ `R` class, KSP-এর code, BuildConfig।
- Source set: `src/debug/`, `src/<flavor>/` — variant অনুযায়ী আলাদা code/resource।

**Answer (English):**
> "At the root, settings.gradle lists the modules and the repositories. The root build file only declares plugins. Versions live in the version catalog, libs.versions.toml. Each module has its own build file with namespace, SDK levels, build types, flavors and dependencies. Inside src/main there is the manifest, the Kotlin code and the res folder. In res, layout and drawable are for UI, mipmap is only for launcher icons, values holds strings, colors and themes, xml holds config files like the network security config, and raw holds files I read as they are. Tests go in test and androidTest. The build output, like APK, AAB and the R8 mapping file, goes in the build folder."

**Key words:** `settings.gradle.kts` · `libs.versions.toml` · `namespace` · `source set` · `mipmap` · `res/raw vs assets` · `outputs/mapping`

**Follow-up:**
- **Q:** What is the difference between res/raw and assets?
  **A:** "Files in raw get a resource ID and can have qualifiers. Assets have no ID. I open them by path, and I can keep folders inside."
- **Q:** Why is mipmap separate from drawable?
  **A:** "Launchers sometimes show the icon bigger than the device density. Mipmap folders are kept even when the build removes unused densities."

**ভুল করবেন না:** `build/` folder বা `local.properties` git-এ রাখা — দুটোই machine-নির্ভর।

**আরও দেখুন:** [P12 · Gradle basics](#p12) · [C14 · Manifest](#c14) · [J7 · Resources](#j7)

---

### <a id="j3"></a>J3. ★ What is the Application class? When do you use it, and what should not go there?

**প্রশ্নটা মানে:** Application object কখন তৈরি হয়, এটা কী জন্য, আর কেন এখানে ভারী কাজ বা global state রাখা বিপদ।
**অন্যভাবেও জিজ্ঞেস করে:** "What do you put in Application.onCreate?" · "Can you keep global data in the Application class?"

**বুঝে নিন:**
- প্রতিটা app process-এ **একটা** `Application` object। কোনো component (Activity, Service, Receiver, Provider) চলার আগেই এটা তৈরি হয়।
- ক্রম: `attachBaseContext` → সব ContentProvider-এর `onCreate` → `Application.onCreate()`।
- Manifest-এ `android:name=".MyApp"` দিয়ে নিজের class দেন।
- **কী রাখবেন:**
  - Hilt-এর জন্য `@HiltAndroidApp` (এটা লাগবেই)।
  - Crash reporting, logging (Timber)-এর মতো যা প্রথম থেকেই লাগবে।
  - Notification channel তৈরি (হালকা, idempotent)।
  - `WorkManager` custom config (`Configuration.Provider`)।
- **কী রাখবেন না:**
  - **ভারী কাজ / I/O / network** — এটা main thread-এ চলে, প্রতিটা cold start ধীর করে। Broadcast বা job-এর জন্য process শুরু হলেও এটা চলে।
  - **Mutable global state** (যেমন logged-in user object) — process death-এ হারিয়ে যায়। Disk-এ (DataStore/Room) রাখুন।
  - **Activity-র reference** — leak।
- Multi-process app (যেমন `android:process=":camera"`)-এ প্রতিটা process-এ `onCreate` আবার চলে। দরকার হলে process নাম check করে init করুন।
- `onTerminate()` আসল device-এ কখনো call হয় না। Cleanup এর ওপর ভরসা করবেন না।

```kotlin
@HiltAndroidApp
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        if (BuildConfig.DEBUG) Timber.plant(Timber.DebugTree())
        createNotificationChannels(this) // হালকা কাজ
    }
}
```

**Answer (English):**
> "The Application object is created once per process, before any activity, service or receiver runs. I use it for app-wide setup that must happen first: Hilt with @HiltAndroidApp, crash reporting, logging, and notification channels. I keep it very light, because it runs on the main thread on every cold start, even when a broadcast or a job starts the process. I don't keep mutable global state there, because it is lost on process death. I also never keep an Activity reference there. Heavy SDKs I start lazily, or with the App Startup library."

**Key words:** `Application.onCreate` · `@HiltAndroidApp` · `cold start` · `process death` · `multi-process` · `lazy init`

**Follow-up:**
- **Q:** Is the Application context safe to keep in a singleton?
  **A:** "Yes. It lives as long as the process, so it does not leak. But I don't use it for UI work like inflating themed views or showing dialogs."
- **Q:** Why might Application.onCreate run twice?
  **A:** "If the app has more than one process, each process creates its own Application. So code that must run once per app needs a process check."
- **Q:** Where do you keep the logged-in user?
  **A:** "On disk, in DataStore or Room, behind a repository. Memory can be a cache, but it is not the source of truth."

**ভুল করবেন না:** "Application object app বন্ধ না হওয়া পর্যন্ত থাকে, তাই এখানে state নিরাপদ" — process death-এ সব যায়।

**আরও দেখুন:** [F1 · App start flow](#f1) · [P3 · Startup speed](#p3) · [C11 · Context](#c11)

---

### <a id="j4"></a>J4. ★ How do lifecycle-aware components work? (Lifecycle, LifecycleOwner, DefaultLifecycleObserver, ProcessLifecycleOwner)

**প্রশ্নটা মানে:** Activity-র callback-এ সব code না লিখে কীভাবে কোনো class নিজেই lifecycle দেখে চালু/বন্ধ হয় — দেখাতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you know when the whole app goes to the background?" · "How do you avoid putting everything in onStart and onStop?"

**বুঝে নিন:**
- **`Lifecycle`** = একটা object যার **state** (INITIALIZED, CREATED, STARTED, RESUMED, DESTROYED) আর **event** (ON_CREATE, ON_START ... ON_DESTROY) আছে।
- **`LifecycleOwner`** = যার lifecycle আছে: `ComponentActivity`, `Fragment`, Fragment-এর `viewLifecycleOwner`, `NavBackStackEntry`, `LifecycleService`।
- **`DefaultLifecycleObserver`** = interface। `onStart`, `onStop` ইত্যাদি override করেন। `lifecycle.addObserver(observer)` দিয়ে যুক্ত করেন। দেরিতে যুক্ত করলেও বর্তমান state পর্যন্ত event পায়।
- **`ProcessLifecycleOwner`** (`lifecycle-process`) = পুরো app-এর lifecycle। প্রথম activity START → app foreground। শেষ activity STOP → app background। ON_STOP একটু দেরিতে আসে, যাতে rotation-কে background ভুল না ধরে।
- লাভ: sensor/camera/location-এর start-stop logic নিজের class-এ থাকে। Activity ছোট থাকে। ভুলে stop না করার bug কমে।
- Coroutine-এ: `lifecycleScope`, `repeatOnLifecycle(STARTED)`। Compose-এ: `LifecycleEventEffect`, `collectAsStateWithLifecycle()`।
- Flutter-এ এর কাছের জিনিস `WidgetsBindingObserver.didChangeAppLifecycleState` — কিন্তু সেটা শুধু app-level, Android-এ প্রতিটা screen-এর আলাদা।

```kotlin
class AccelerometerListener(
    private val sensorManager: SensorManager,
    private val onData: (FloatArray) -> Unit,
) : DefaultLifecycleObserver, SensorEventListener {
    private val sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
    override fun onStart(owner: LifecycleOwner) {
        sensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_UI)
    }
    override fun onStop(owner: LifecycleOwner) = sensorManager.unregisterListener(this)
    override fun onSensorChanged(e: SensorEvent) = onData(e.values.clone())
    override fun onAccuracyChanged(s: Sensor?, accuracy: Int) = Unit
}
// Activity-তে: lifecycle.addObserver(AccelerometerListener(sensorManager) { ... })
```

**Answer (English):**
> "Activities and fragments are LifecycleOwners. They expose a Lifecycle with states and events. Instead of putting start and stop code in the activity, I write a class that implements DefaultLifecycleObserver and add it to the lifecycle. For example, a sensor listener registers in onStart and unregisters in onStop. So the activity stays small and I can't forget to stop it. For the whole app, I use ProcessLifecycleOwner to know when the app goes to the background. For coroutines, I use repeatOnLifecycle, and in Compose, collectAsStateWithLifecycle. One pitfall: in a fragment I use viewLifecycleOwner for UI work."

**Key words:** `LifecycleOwner` · `DefaultLifecycleObserver` · `ProcessLifecycleOwner` · `repeatOnLifecycle` · `viewLifecycleOwner` · `LifecycleEventEffect`

**Follow-up:**
- **Q:** Why does ProcessLifecycleOwner send ON_STOP with a delay?
  **A:** "During rotation, the activity stops and starts again fast. The small delay stops the app from thinking it went to the background."
- **Q:** CameraX uses a lifecycle too. How?
  **A:** "I call bindToLifecycle with a LifecycleOwner. CameraX opens the camera when the owner is started and closes it when it stops."
- **Q:** Should a ViewModel observe the lifecycle?
  **A:** "No. A ViewModel should not know about the activity lifecycle. The UI collects its state with a lifecycle-aware collector."

**ভুল করবেন না:** Fragment-এ UI observer-এর জন্য `this` (fragment) owner দেওয়া — view destroy হলেও observer থাকে, duplicate আর leak হয়।

**আরও দেখুন:** [C2 · Activity lifecycle](#c2) · [K14 · Collect Flow safely](#k14) · [N3 · Sensors and battery](#n3)

---

### <a id="j5"></a>J5. ★ How do you support old Android versions? (AppCompat, Compat classes, SDK_INT, @RequiresApi)

**প্রশ্নটা মানে:** minSdk কম রেখে নতুন API নিরাপদে কীভাবে ব্যবহার করেন — crash ছাড়া।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you use an API that only exists on Android 13?" · "What is the difference between ComponentActivity and AppCompatActivity?"

**বুঝে নিন:**
- **তিনটা SDK** (বিস্তারিত P11-এ): `minSdk` = সবচেয়ে পুরনো supported version; `compileSdk` = কোন API দেখা যায়; `targetSdk` = কোন version-এর behavior মেনে নিয়েছেন।
- minSdk-এর চেয়ে নতুন API সরাসরি call করলে পুরনো phone-এ `NoSuchMethodError` / crash। **Lint `NewApi`** এটা ধরে।
- **৩টা উপায়, এই ক্রমে:**
  1. **Compat class** আগে খুঁজুন: `ContextCompat.getColor()`, `ContextCompat.checkSelfPermission()`, `ContextCompat.registerReceiver(..., RECEIVER_NOT_EXPORTED)`, `NotificationCompat.Builder`, `ViewCompat`/`WindowCompat` (insets), `PendingIntentCompat`। ভেতরে version check করা আছে।
  2. **নিজে check:** `if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) { ... } else { ... }`।
  3. **`@RequiresApi(33)`** নতুন-API function-এর ওপর। Lint caller-কে check করতে বাধ্য করে। নিজের helper-এ `@ChecksSdkIntAtLeast` দিলে lint সেটা বোঝে।
- **AppCompat:** `AppCompatActivity` + `Theme.AppCompat`/`Theme.Material3` (MDC) — View app-এ material widget, toolbar, per-app language backport (`AppCompatDelegate.setApplicationLocales`)। শুধু Compose app-এ `ComponentActivity` যথেষ্ট।
- পুরনো version-এ feature নেই হলে: চুপচাপ বাদ দিন (graceful degradation), crash না।
- Test: minSdk-এর emulator-এ অন্তত একবার চালান।

```kotlin
fun askNotificationPermission(launcher: ActivityResultLauncher<String>) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
        launcher.launch(Manifest.permission.POST_NOTIFICATIONS)
    } // 33-এর নিচে runtime permission নেই, কিছু করার দরকার নেই
}
```

**Answer (English):**
> "minSdk is the oldest version I support, compileSdk decides which APIs I can see, and targetSdk decides which new behaviors I accept. If I call an API newer than minSdk, it crashes on old phones, and lint warns me with NewApi. First I look for a Compat class, like ContextCompat, NotificationCompat or ViewCompat, because they do the version check for me. If there is none, I check Build.VERSION.SDK_INT and mark the function with @RequiresApi. On old versions I skip the feature, I don't crash. I also run the app once on a minSdk emulator."

**Key words:** `minSdk / compileSdk / targetSdk` · `Build.VERSION.SDK_INT` · `@RequiresApi` · `ContextCompat` · `NotificationCompat` · `Lint NewApi`

**Follow-up:**
- **Q:** ComponentActivity or AppCompatActivity?
  **A:** "For a Compose-only app, ComponentActivity is enough. I use AppCompatActivity when I have Views with Material Components or I need things like the per-app language backport."
- **Q:** Does raising compileSdk change app behavior?
  **A:** "No. It only changes what I can compile against. Behavior changes come with targetSdk."
- **Q:** What minSdk do you choose?
  **A:** "I look at the users' devices and at library needs. Many AndroidX libraries now need minSdk 23, so I don't go lower than that."

**ভুল করবেন না:** `targetSdk` আর `compileSdk` গুলিয়ে ফেলা — behavior বদলায় শুধু targetSdk দিয়ে।

**আরও দেখুন:** [P11 · minSdk/targetSdk + versions](#p11) · [J1 · AndroidX](#j1) · [C13 · Runtime permissions](#c13)

---

### <a id="j6"></a>J6. ◆ What are the basics of the View system? (View vs ViewGroup, layouts, ViewBinding, custom views)

**প্রশ্নটা মানে:** পুরনো View-based code পড়তে আর ঠিক করতে পারবেন কিনা — অনেক company-তে এখনো এটা আছে।
**অন্যভাবেও জিজ্ঞেস করে:** "ViewBinding or DataBinding?" · "How do you write a custom view?"

**বুঝে নিন:**
- **View** = screen-এর একটা জিনিস (TextView, Button)। **ViewGroup** = অন্য View রাখে আর তাদের জায়গা ঠিক করে (layout)। পুরো screen একটা tree।
- **Common layout:**
  | Layout | কখন |
  |---|---|
  | `ConstraintLayout` | জটিল screen, flat tree (nesting কম = দ্রুত) |
  | `LinearLayout` | সহজ এক সারি/এক কলাম |
  | `FrameLayout` | একটার ওপর আরেকটা; fragment container, video-র ওপর overlay |
  | `CoordinatorLayout` | Scroll-এ toolbar লুকানো, Snackbar, FAB আচরণ |
- **View খোঁজার উপায়:**
  | উপায় | অবস্থা |
  |---|---|
  | `findViewById` | কাজ করে, কিন্তু null/type ভুলের ঝুঁকি, বেশি code |
  | Kotlin synthetics | **Removed** — ব্যবহার করা যায় না |
  | **ViewBinding** | View code-এ recommended: type-safe, null-safe, দ্রুত build |
  | DataBinding | XML-এ expression; build ধীর, debug কঠিন। নতুন code-এ সাধারণত না |
  | Compose | নতুন UI-এর জন্য; View-এ `ComposeView` দিয়ে মেশানো যায় |
- Fragment-এ ViewBinding: `onDestroyView`-এ `_binding = null` — না হলে view leak।
- **Custom view (সংক্ষেপে):**
  - `onMeasure(widthSpec, heightSpec)`: `MeasureSpec` mode — `EXACTLY`, `AT_MOST`, `UNSPECIFIED`। শেষে `setMeasuredDimension()` (helper: `resolveSize`)।
  - `onDraw(canvas)`: শুধু আঁকা। এখানে `Paint`/object allocate করবেন না — প্রতি frame-এ চলে।
  - Size বদলালে `requestLayout()`, শুধু চেহারা বদলালে `invalidate()`।
  - Custom attribute: `res/values/attrs.xml` + `context.withStyledAttributes`।

**Answer (English):**
> "A View is one element, and a ViewGroup holds other views and places them. For layouts I use ConstraintLayout for complex screens because it keeps the tree flat, LinearLayout for simple rows, and FrameLayout for overlays like controls on top of a video. To access views I use ViewBinding. It is type-safe and null-safe. I avoid DataBinding in new code because it slows the build and hides logic in XML. For a custom view, I override onMeasure and call setMeasuredDimension, and I draw in onDraw without creating objects there. For new screens I prefer Compose, but I am comfortable in View code."

**Key words:** `ViewGroup` · `ConstraintLayout` · `ViewBinding` · `MeasureSpec` · `onDraw` · `invalidate vs requestLayout`

**Follow-up:**
- **Q:** What is the difference between invalidate and requestLayout?
  **A:** "invalidate only redraws the view. requestLayout runs measure and layout again, because the size or position may change. requestLayout costs more."
- **Q:** Why set the binding to null in a fragment?
  **A:** "The fragment can live longer than its view. If I keep the binding, I keep the old view tree in memory."

**ভুল করবেন না:** গভীর nested `LinearLayout` + `layout_weight` — প্রতিটা level বারবার measure করে, screen ধীর হয়।

**আরও দেখুন:** [U15 · RecyclerView + measure/draw](#u15) · [U10 · Mix Compose and Views](#u10) · [C3 · Fragment lifecycle](#c3)

---

### <a id="j7"></a>J7. ◆ How do resources and configuration qualifiers work?

**প্রশ্নটা মানে:** Dark mode, ভাষা, tablet, landscape — Android কোন resource বেছে নেয়, আর theme আর style-এর পার্থক্য জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you support Bangla and English?" · "What is the difference between a theme and a style?"

**বুঝে নিন:**
- **Resource type:** `strings.xml` (plural-এর জন্য `<plurals>`, format `%1$s`), `colors.xml`, `dimens.xml` (`dp` layout-এ, `sp` text-এ), `themes.xml`/`styles.xml`।
- **Qualifier** = folder নামের শেষে condition:
  | Qualifier | উদাহরণ |
  |---|---|
  | ভাষা/region | `values-bn/strings.xml`, `values-en-rUS/` |
  | Smallest width | `values-sw600dp/` (tablet) |
  | Orientation | `layout-land/` |
  | Night mode | `values-night/colors.xml` |
  | Density | `drawable-xxhdpi/` (vector হলে লাগে না) |
  | API level | `values-v31/` |
- **Android কীভাবে বাছে:** (১) device-এর সাথে contradict করে এমন folder বাদ। (২) qualifier-গুলো একটা নির্দিষ্ট ক্রমে দেখে (ভাষা → ... → smallest width → ... → orientation → night → density ...)। প্রথম যে qualifier মেলে, সেটা যাদের আছে তারা থাকে। (৩) Density ব্যতিক্রম: exact না মিললে সবচেয়ে কাছেরটা নিয়ে scale করে।
- Default folder (`values/`) সবসময় রাখুন। না থাকলে অমিল device-এ crash (`Resources.NotFoundException`)।
- Configuration বদলালে (ভাষা, dark mode, rotation) Activity আবার তৈরি হয় — নতুন resource load করতে।
- **Per-app language:** Android 13+ system setting; পুরনোতে AppCompat backport। `locales_config.xml` দিয়ে ভাষার list দেন।
- **Style vs theme (View world):**
  - **Style** = একটা View-এর attribute-এর set (`style="@style/Title"`)। শুধু সেই view।
  - **Theme** = পুরো Activity/App-এ লাগে। **Theme attribute** দেয় (`?attr/colorPrimary`, `?attr/colorSurface`)। View সরাসরি color না নিয়ে attribute নিলে dark mode/dynamic color নিজে থেকেই কাজ করে।
  - `ThemeOverlay` দিয়ে একটা subtree-র theme বদলানো যায়।
- Compose-এ এর জায়গায় `MaterialTheme`; তবু string আর ভাষার জন্য `stringResource()` + `values-bn` একই।

**Answer (English):**
> "I keep text, colors and sizes in resources, not in code. Qualifiers on folder names give other versions: values-bn for Bangla, values-night for dark mode, sw600dp for tablets, layout-land for landscape. Android first removes folders that do not match the device, then checks qualifiers in a fixed order and keeps the best match. I always keep a default folder, or the app can crash on a device that matches nothing. A style sets attributes on one view. A theme applies to a whole activity or app and gives theme attributes like colorPrimary. I use theme attributes in views, so dark mode and dynamic color just work."

**Key words:** `qualifier` · `values-night` · `sw600dp` · `values-bn` · `theme attribute (?attr/)` · `per-app language`

**Follow-up:**
- **Q:** How do you add Bangla support?
  **A:** "I put every text in strings.xml, add values-bn/strings.xml, and add a locales config for the per-app language setting. I also test long text and plurals."
- **Q:** Why does the activity restart when the language changes?
  **A:** "Resources depend on the configuration. Recreating the activity is how Android loads the new strings and layouts."

**ভুল করবেন না:** Code-এ সরাসরি `Color.parseColor("#000")` বা hardcoded text — dark mode আর অনুবাদ দুটোই ভাঙে।

**আরও দেখুন:** [U12 · Compose theming](#u12) · [C4 · Config change](#c4) · [U14 · Large screens](#u14)

---

### <a id="j8"></a>J8. ◆ Toast vs Snackbar vs Dialog vs notification — when do you use each?

**প্রশ্নটা মানে:** User-কে খবর দেওয়ার ঠিক উপায় বাছতে পারেন কিনা — UX আর technical দুই দিক থেকে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you show an 'Undo' message?" · "How do you show a dialog that survives rotation?"

**বুঝে নিন:**
| উপায় | কখন | মনে রাখুন |
|---|---|---|
| **Toast** | ছোট system message, action নেই | Android 11+ এ custom view toast background থেকে দেখায় না; Android 12+ এ ছোট (২ লাইন) আর app icon সহ। Android 13+ এ clipboard copy-র নিজের message আছে — নিজে toast দেবেন না |
| **Snackbar** | App-এর ভেতরে, action সহ ("Undo", "Retry") | View-এ `Snackbar.make(view, ...)`; Compose-এ `Scaffold` + `SnackbarHostState.showSnackbar()` (suspend) |
| **Dialog** | User-কে থামিয়ে সিদ্ধান্ত চাই (delete confirm, permission rationale) | View-এ `DialogFragment` (rotation-এ টিকে থাকে); Compose-এ `AlertDialog` — ViewModel state থেকে দেখান |
| **Notification** | App খোলা না থাকলেও জানাতে হবে (motion alert, download শেষ) | Channel, Android 13+ এ `POST_NOTIFICATIONS` permission |
| **Inline UI** | Form error, empty state | প্রায়ই সবচেয়ে ভালো — popup না |
- Snackbar/dialog দেখানোর trigger ViewModel থেকে **one-time event** বা state হিসেবে আসে। Rotation-এ দুইবার দেখানো যেন না হয়।
- Plain `Dialog`/`AlertDialog.Builder` (View) rotation-এ হারায় — তাই `DialogFragment`।

**Answer (English):**
> "I use a Toast only for a short message with no action, and I use it less now because Android limits it. For in-app feedback with an action, like Undo or Retry, I use a Snackbar. In Compose that is SnackbarHostState in a Scaffold. When the user must decide something, like confirming a delete, I use a dialog. In Views I use DialogFragment so it survives rotation, and in Compose I show AlertDialog from ViewModel state. If the user must know when the app is not open, like a camera motion alert, I use a notification. For form errors, I prefer inline messages."

**Key words:** `Toast` · `Snackbar` · `SnackbarHostState` · `DialogFragment` · `AlertDialog` · `notification channel`

**Follow-up:**
- **Q:** How do you avoid showing a Snackbar twice after rotation?
  **A:** "I keep the message in UI state and clear it after it is shown, or I send it as a one-time event that is consumed once."
- **Q:** Can you show a Toast from a background thread?
  **A:** "I post it to the main thread, because a toast needs a thread with a Looper. A different case is when the whole app is in the background. Then a plain text toast still shows, but a custom view toast is blocked on Android 11 and up."

**ভুল করবেন না:** গুরুত্বপূর্ণ error Toast দিয়ে দেখানো — user মিস করে, আর retry করার উপায় থাকে না।

**আরও দেখুন:** [K15 · One-time UI events](#k15) · [C15 · Notifications](#c15) · [V9 · Motion alerts](#v9)

---

### <a id="j9"></a>J9. ◆ What is the Activity Result API, and why did it replace startActivityForResult?

**প্রশ্নটা মানে:** Camera, gallery, permission-এর result নেওয়ার আধুনিক উপায় জানেন কিনা, আর পুরনোটা কেন সমস্যা ছিল।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you take a photo and get the result?" · "How do you pick an image without storage permission?"

**বুঝে নিন:**
- **পুরনো:** `startActivityForResult` + `onActivityResult(requestCode, ...)`, `onRequestPermissionsResult`। সমস্যা: সব result এক জায়গায়, requestCode মেলানো, type-safe না, Fragment-এ গোলমাল। এখন **deprecated**।
- **নতুন:** একটা **contract** (input → output type) + **launcher**।
  - Activity/Fragment-এ: `registerForActivityResult(contract) { result -> }` — **field হিসেবে বা STARTED-এর আগে** register করতে হবে।
  - Compose-এ: `rememberLauncherForActivityResult(contract) { }`।
- Process death হলেও কাজ করে: result আসে register করা callback-এ, activity আবার তৈরি হলেও।
- **Common contract:**
  | Contract | Input → Output |
  |---|---|
  | `RequestPermission` | `String` → `Boolean` |
  | `RequestMultiplePermissions` | `Array<String>` → `Map<String, Boolean>` |
  | `TakePicture` | `Uri` (FileProvider দিয়ে বানানো) → `Boolean` |
  | `PickVisualMedia` | `PickVisualMediaRequest` → `Uri?` (Photo Picker, permission লাগে না) |
  | `GetContent` / `OpenDocument` | MIME type → `Uri?` |
  | `StartActivityForResult` | `Intent` → `ActivityResult` (generic) |
- নিজের contract: `ActivityResultContract<I, O>` extend করে `createIntent` আর `parseResult`।

```kotlin
@Composable
fun PhotoPickerButton(onPicked: (Uri) -> Unit) {
    val launcher = rememberLauncherForActivityResult(
        ActivityResultContracts.PickVisualMedia()
    ) { uri -> uri?.let(onPicked) }
    Button(onClick = {
        launcher.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
    }) { Text("Pick photo") }
}
```

**Answer (English):**
> "The Activity Result API replaced startActivityForResult and onRequestPermissionsResult, which are deprecated. I register a contract and get a launcher. The contract defines the input and output types, so it is type-safe and there are no request codes. I must register it early, as a field or before the screen is started, so the result still arrives after the activity is recreated. In Compose I use rememberLauncherForActivityResult. Common contracts are RequestPermission, TakePicture with a FileProvider URI, and PickVisualMedia for the Photo Picker, which needs no storage permission."

**Key words:** `registerForActivityResult` · `ActivityResultContract` · `rememberLauncherForActivityResult` · `PickVisualMedia` · `TakePicture` · `RequestPermission`

**Follow-up:**
- **Q:** Why must you register before the activity is started?
  **A:** "After recreation, the system needs the same callback ready to deliver the result. Registering late throws an exception."
- **Q:** Why use the Photo Picker instead of READ_MEDIA_IMAGES?
  **A:** "It needs no permission and the user picks only what they want. Google Play also limits broad photo access to apps with a core need."

**ভুল করবেন না:** Button-এর click-এর ভেতরে `registerForActivityResult` call করা — crash করে (STARTED-এর পরে register করা যায় না)।

**আরও দেখুন:** [C13 · Runtime permissions](#c13) · [C17 · Storage](#c17) · [C9 · FileProvider](#c9)

---

### <a id="j10"></a>J10. ◆ How do you use the App Startup library and the SplashScreen API?

**প্রশ্নটা মানে:** Startup-এ library init কীভাবে গুছিয়ে রাখেন, আর আধুনিক splash কীভাবে দেখান — practical জ্ঞান।
**অন্যভাবেও জিজ্ঞেস করে:** "Do you still create a SplashActivity?" · "How do you stop a library from starting itself at launch?"

**বুঝে নিন:**
**App Startup (`androidx.startup`):**
- সমস্যা: অনেক library নিজের `ContentProvider` দিয়ে auto-init হয়। প্রতিটা provider cold start-এ খরচ বাড়ায়।
- সমাধান: সব init একটা `InitializationProvider`-এ। প্রতিটা init একটা `Initializer<T>`: `create()` আর `dependencies()` (কে আগে চলবে)।
- **Lazy init:** Manifest-এ `tools:node="remove"` দিয়ে auto-init বন্ধ, পরে দরকার হলে `AppInitializer.getInstance(context).initializeComponent(MyInit::class.java)`।
- মনে রাখুন: Initializer-ও main thread-এ চলে। ভারী কাজ lazy করুন বা background-এ পাঠান।

**SplashScreen API:**
- Android 12+ এ system প্রতিটা cold/warm start-এ splash দেখায় — আপনি বন্ধ করতে পারেন না, শুধু সাজাতে পারেন।
- `core-splashscreen` library পুরনো version-এও একই API দেয়।
- আলাদা `SplashActivity` **বানাবেন না** — দুইটা splash দেখা যায়, startup ধীর হয়।
- ধাপ: theme `Theme.SplashScreen` (icon, background, `postSplashScreenTheme`) → `installSplashScreen()` **`super.onCreate()`-এর আগে** → দরকার হলে `setKeepOnScreenCondition { !viewModel.isReady }` (খুব অল্প সময়ের জন্য)।

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    val splash = installSplashScreen()
    super.onCreate(savedInstanceState)
    splash.setKeepOnScreenCondition { viewModel.isLoading.value }
    setContent { AppRoot() }
}
```

**Answer (English):**
> "Many libraries start themselves with their own content provider, and each one adds to cold start. App Startup puts them in one provider. Each library gets an Initializer with its dependencies, and I can turn off auto-start and start a library lazily when I first need it. For the splash, on Android 12 and up the system always shows one, so I don't make a separate splash activity. I use the core-splashscreen library, set a splash theme, and call installSplashScreen before super.onCreate. I keep the splash only while the first data loads, and never for long."

**Key words:** `Initializer` · `InitializationProvider` · `lazy init` · `installSplashScreen` · `setKeepOnScreenCondition` · `Theme.SplashScreen`

**Follow-up:**
- **Q:** What is wrong with a separate SplashActivity on Android 12+?
  **A:** "The user sees the system splash and then my splash, so two splashes. It also adds one more activity start, so the app opens slower."

**ভুল করবেন না:** Splash-কে loading screen বানিয়ে network call শেষ হওয়া পর্যন্ত আটকে রাখা — app ধীর মনে হয়; skeleton UI দেখান।

**আরও দেখুন:** [P3 · Startup speed](#p3) · [J3 · Application class](#j3) · [C9 · ContentProvider](#c9)

---

### <a id="j11"></a>J11. ★ Which Jetpack libraries do you use in a new app today, and why?

**প্রশ্নটা মানে:** আপনি আধুনিক Android stack জানেন কিনা, আর প্রতিটা পছন্দের কারণ বলতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is your tech stack for a new Android app?" · "If you start a project tomorrow, what do you choose?"

**বুঝে নিন:**
| Layer | পছন্দ | কেন |
|---|---|---|
| Language | Kotlin 2.x (K2), coroutines + Flow | Google-এর Kotlin-first; async সহজ |
| UI | Compose + Material 3, `collectAsStateWithLifecycle` | কম code, preview, theming |
| State | ViewModel + `StateFlow`, `SavedStateHandle` | Rotation আর process death সামলায় |
| Navigation | Navigation Compose (type-safe) বা Navigation 3 | Back stack, deep link, ViewModel scope |
| DI | Hilt (KSP দিয়ে) | কম boilerplate, ViewModel/WorkManager integration |
| Local data | Room (KSP), DataStore | Offline-first, Flow query |
| Network | Retrofit + OkHttp + kotlinx.serialization | Standard, interceptor, test সহজ |
| Image | Coil (Compose-friendly, coroutine) | হালকা, Kotlin-first |
| Background | WorkManager | Guaranteed কাজ, constraint, retry |
| Performance | Baseline Profiles + Macrobenchmark, R8 | Startup আর scroll দ্রুত |
| Test | JUnit, Turbine, kotlinx-coroutines-test, Compose UI test, Robolectric (দরকারে) | ViewModel আর UI test |
| Build | Version catalog, KSP (kapt না), convention plugin (multi-module হলে) | পরিষ্কার আর দ্রুত build |
- Domain অনুযায়ী যোগ: CameraX, Media3, Biometric, Credential Manager, Paging 3।
- **বলবেন না:** LiveData প্রথম পছন্দ, kapt, `EncryptedSharedPreferences`, পুরনো `exoplayer2`।
- Senior উত্তরের ভাব: "সব library দরকার নেই।" ছোট app-এ multi-module বা Paging লাগবে না।

**Answer (English):**
> "I start with Kotlin, coroutines and Flow. For UI I use Compose with Material 3. Each screen has a ViewModel that exposes a StateFlow, and the UI collects it with collectAsStateWithLifecycle. For navigation, Navigation Compose with type-safe routes, or Navigation 3 for a new Compose app. Hilt for DI, with KSP instead of kapt. Room and DataStore for local data, so the app works offline. Retrofit, OkHttp and kotlinx.serialization for the network, Coil for images, and WorkManager for sync. I add Baseline Profiles early for fast startup. But I add only what the app needs. A small app does not need Paging or many modules."

**Key words:** `Compose + Material 3` · `ViewModel + StateFlow` · `Hilt + KSP` · `Room / DataStore` · `WorkManager` · `Baseline Profiles`

**Follow-up:**
- **Q:** Why not LiveData?
  **A:** "LiveData still works, but it is Android-only and has few operators. Flow works with coroutines, has many operators, and also works in Kotlin Multiplatform."
- **Q:** Navigation Compose or Navigation 3?
  **A:** "Both are fine. Navigation 3 lets me own the back stack as a simple list, which helps with adaptive layouts. For an existing app on Navigation Compose, I would not migrate without a reason."
- **Q:** Would you use Koin instead of Hilt?
  **A:** "Koin is simpler and works in KMP, but errors show at runtime. Hilt checks the graph at compile time. For a large Android-only app, I choose Hilt."

**ভুল করবেন না:** শুধু library-র নাম গোনা — প্রতিটার "কেন" এক লাইনে বলুন।

**আরও দেখুন:** [R5 · Hilt](#r5) · [R4 · Offline-first](#r4) · [F12 · New in 2025–2026](#f12)

---

### <a id="j12"></a>J12. ◆ Which Android Studio tools do you use every day?

**প্রশ্নটা মানে:** Bug আর performance সমস্যা খুঁজতে আপনি tool দিয়ে কাজ করেন, নাকি শুধু log বসিয়ে অনুমান করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you debug a UI problem?" · "How do you find a memory leak in Android Studio?"

**বুঝে নিন:**
| Tool | কী জন্য |
|---|---|
| **Logcat** | Log দেখা; filter: `package:mine level:error tag:Camera`। Crash-এর stack trace |
| **Debugger** | Breakpoint, conditional breakpoint, Evaluate Expression, চলমান app-এ "Attach debugger" |
| **Layout Inspector** | View/Compose tree, attribute; Compose-এ recomposition count দেখা |
| **Profiler** | CPU (method/system trace), Memory (heap dump, allocation, leak), Power Profiler (Pixel-এ ODPM data; পুরনো Energy profiler-এর জায়গায়) |
| **App Inspection** | Database Inspector (Room live query), Network Inspector, Background Task Inspector (WorkManager) |
| **Device Explorer** | App-এর file দেখা (debug build) |
| **Emulator** | বিভিন্ন API level, foldable, rotation, location, sensor value, camera simulate |
| **Lint** | `NewApi`, leak, accessibility সমস্যা আগে ধরা |
- **adb basics:** `adb devices`, `adb install -r app.apk`, `adb logcat`, `adb shell am start -n pkg/.MainActivity`, `adb shell pm clear pkg`, `adb shell dumpsys activity`, `adb bugreport`।
- Process death test: app background-এ → `adb shell am kill <pkg>` → app-এ ফিরুন।
- **Gemini in Android Studio:** code ব্যাখ্যা, test খসড়া, crash বিশ্লেষণে সাহায্য করে; Agent Mode বড় কাজও করে। **সাবধানে:** সব suggestion review করুন, company-র policy মানুন (code বাইরে যাচ্ছে কিনা), secret কখনো paste করবেন না।
- Platform-level (Perfetto, `dumpsys`, tombstone, SELinux log) → O12।

**Answer (English):**
> "Every day I use Logcat with filters, like only my package and only errors. For logic bugs I use the debugger with conditional breakpoints and evaluate expression, often attached to a running app. For UI problems I use Layout Inspector, and in Compose I check recomposition counts. For speed and memory I use the CPU and memory profilers, and heap dumps to find leaks. App Inspection helps me see the Room database, network calls and WorkManager jobs live. I use adb to install, clear data, and kill the process to test process death. I use Gemini in Android Studio for help, but I review everything and follow the company's rules about code."

**Key words:** `Logcat filters` · `conditional breakpoint` · `Layout Inspector` · `heap dump` · `Database Inspector` · `adb shell am kill`

**Follow-up:**
- **Q:** How do you find a memory leak?
  **A:** "In debug I use LeakCanary. In Android Studio I take a heap dump after leaving the screen and look for activities or fragments that should be gone."
- **Q:** Do you trust AI-generated code?
  **A:** "I treat it like code from a new teammate. I read it, test it, and check it against our architecture. I never paste keys or private data."

**ভুল করবেন না:** Debug build-এ performance মাপা — debug build অনেক ধীর; release-এর মতো build (R8 সহ) আর আসল device-এ মাপুন।

**আরও দেখুন:** [O12 · Platform debugging](#o12) · [P2 · Memory leaks](#p2) · [P10 · Bug you cannot reproduce](#p10)

---

### <a id="j13"></a>J13. ○ How do you build home screen widgets with Glance, and Quick Settings tiles?

**প্রশ্নটা মানে:** App-এর বাইরে (home screen, notification shade) ছোট UI কীভাবে বানান আর update করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How does a widget update its data?" · "Can you show camera status in a Quick Settings tile?"

**বুঝে নিন:**
**Glance widget:**
- Widget launcher-এর process-এ দেখায়, আপনার app-এ না। তাই ভেতরে **RemoteViews** — সীমিত View।
- **Glance** Compose-এর মতো code লিখতে দেয় (`Column`, `Text`, `GlanceModifier`) আর সেটা RemoteViews-এ বদলে দেয়। এটা আসল Compose না — `androidx.glance.*` composable ব্যবহার করতে হয়।
- অংশ: `GlanceAppWidget` (`provideGlance { provideContent { ... } }`) + `GlanceAppWidgetReceiver` + `res/xml/` widget info (size, preview)।
- **Update:** `MyWidget().updateAll(context)` — data বদলালে call করুন। Periodic হলে WorkManager। XML-এর `updatePeriodMillis` কমপক্ষে 30 মিনিট।
- Click: `actionStartActivity<MainActivity>()` বা `actionRunCallback<...>()`।
- Live video বা খুব ঘনঘন update widget-এ হয় না — শুধু snapshot আর status।

**Quick Settings tile:**
- `TileService` extend করুন, manifest-এ `BIND_QUICK_SETTINGS_TILE` permission সহ declare করুন।
- `onStartListening()`-এ tile-এর state (`qsTile.state`, label) update, তারপর `updateTile()`। `onClick()`-এ কাজ।
- Android 13+: `StatusBarManager.requestAddTileService()` দিয়ে user-কে tile যোগ করতে বলা যায়।
- Android 14 target করলে tile থেকে activity খুলতে `startActivityAndCollapse(PendingIntent)` — Intent version আর চলে না।

**Answer (English):**
> "A widget runs in the launcher, not in my app, so it uses RemoteViews. I build it with Glance, which lets me write Compose-style code that becomes RemoteViews. I make a GlanceAppWidget and a receiver, and I call updateAll when the data changes. For regular refresh I use WorkManager, because the XML update period is at least thirty minutes. Widgets are for small status, not live content. A Quick Settings tile is a TileService. I update its state in onStartListening and handle onClick. On Android 14 and up, to open an activity from a tile, I must pass a PendingIntent."

**Key words:** `Glance` · `GlanceAppWidget` · `RemoteViews` · `updateAll` · `TileService` · `startActivityAndCollapse(PendingIntent)`

**Follow-up:**
- **Q:** Can you use normal Compose components in Glance?
  **A:** "No. Glance has its own composables, like androidx.glance Text and Column. Normal Compose UI does not work there."

**ভুল করবেন না:** Widget-এ ঘন ঘন (প্রতি সেকেন্ডে) update চালানো — battery খায় আর system আটকে দিতে পারে।

**আরও দেখুন:** [C10 · Background work](#c10) · [C8 · BroadcastReceivers](#c8) · [C5 · PendingIntent](#c5)

---


## <a id="part-3"></a>Part 3 — Jetpack Compose আর UI

নতুন Android কাজে UI মানেই এখন Jetpack Compose। Interviewer দেখতে চায় আপনি recomposition, state আর side effect ঠিকভাবে বোঝেন কিনা।
Flutter-এর declarative মডেল আপনি জানেন। তাই এখানে মূল কাজ হলো পার্থক্যগুলো ধরা: stability, lifecycle-aware collection, edge-to-edge আর নতুন Android version-এর UI নিয়ম।
পুরনো কোডে এখনো RecyclerView আর XML আছে, তাই শেষে সেটাও আছে।

### আগে বুঝুন — Compose কীভাবে কাজ করে

**বড় ছবি, ধাপে ধাপে:**
1. আপনি `@Composable` function লেখেন। Function টা data নেয় আর UI বর্ণনা করে।
2. Compose compiler plugin (Kotlin 2.0 থেকে Kotlin-এর সাথেই আসে) এই function গুলোকে বদলে দেয়। প্রতিটা call-এর একটা জায়গা (slot) মনে রাখে।
3. প্রথমবার চালালে Compose একটা UI tree বানায়। এর নাম **Composition**।
4. কোনো `State` বদলালে, যে composable সেই state **পড়েছিল** শুধু সেটা আবার চলে। এটাই **recomposition**।
5. Recomposition-এর সময় যে child-এর input বদলায়নি, Compose তাকে **skip** করে।

**প্রতি frame-এ তিনটা phase:**
```
Composition  →  Layout (measure + place)  →  Drawing
 (কী দেখাব)      (কোথায়, কত বড়)               (pixel আঁকা)
```
- State কোন phase-এ পড়া হচ্ছে, সেটা গুরুত্বপূর্ণ। Composition-এ পড়লে তিন phase-ই আবার চলে।
- Layout বা draw lambda-র ভেতরে পড়লে (`Modifier.offset { }`, `drawBehind { }`) শুধু ওই phase চলে। এটা বড় performance কৌশল।

**মূল ধারণা যার উপর সব দাঁড়িয়ে:**
- **State** — `mutableStateOf` হলো observable value। Compose snapshot system দিয়ে কে পড়ল তা track করে।
- **remember** — recomposition-এর মাঝে value ধরে রাখে। Composition থেকে বের হলে হারায়।
- **rememberSaveable** — configuration change আর process death-ও পার হয় (Bundle-এ রাখে)।
- **Stability** — Compose কোনো parameter-কে "stable" মনে করলে, equals() দিয়ে তুলনা করে skip করতে পারে।
- **Strong skipping mode** — Kotlin 2.0.20 থেকে default। এখন unstable parameter থাকলেও skip হতে পারে (instance equality `===` দিয়ে)।
- **Side effect** — composable-এর ভেতরে সরাসরি network call বা listener লাগানো যায় না। `LaunchedEffect`, `DisposableEffect` ইত্যাদি ব্যবহার করতে হয়।
- **Unidirectional data flow** — state নিচে নামে, event উপরে ওঠে। ViewModel একটা `StateFlow<UiState>` দেয়।
- **Lifecycle-aware collection** — `collectAsStateWithLifecycle()` দিয়ে flow collect করুন, যাতে background-এ কাজ থামে।

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ `build()` পুরো subtree আবার বানায়, আর Element tree diff করে। Compose-এ compiler আগে থেকেই জানে কোন জায়গা কোন state পড়ে, তাই শুধু সেই scope আবার চলে।
- Flutter-এর `const` widget-এর কাজ Compose-এ করে **stability + skipping**।
- Flutter-এর `StatefulWidget` state ≈ Compose-এর `remember { mutableStateOf() }`। `RestorationMixin` ≈ `rememberSaveable`।
- Flutter-এ `initState`/`dispose` আছে। Compose-এ সেই কাজ করে `LaunchedEffect` / `DisposableEffect`।
- Android-এ configuration change (rotation, fold, dark mode) হলে Activity আবার তৈরি হয়। Flutter-এ এটা হয় না, তাই Android-এ state কোথায় রাখবেন সেটা বেশি ভাবতে হয়।

---

### <a id="u1"></a>U1. ★ What is Jetpack Compose, and why do teams move from XML Views to it?

**প্রশ্নটা মানে:** Compose কী, declarative UI কেন ভালো, আর পুরনো View system থেকে সরার আসল কারণ কী।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between declarative and imperative UI?" · "Why should a team use Compose instead of XML layouts?"

**বুঝে নিন:**
- **Imperative (XML + View):** XML-এ layout লেখেন। তারপর code-এ `findViewById` বা ViewBinding দিয়ে view ধরে নিজে বদলান: `textView.text = ...`, `view.visibility = GONE`। UI আর state আলাদা থাকে, তাই sync ভুল হয়।
- **Declarative (Compose):** UI = f(state)। আপনি বলেন "এই state-এ UI এমন দেখাবে"। State বদলালে Compose নিজে UI আপডেট করে।
- Compose হলো Kotlin library + compiler plugin। কোনো XML নেই, কোনো View object নেই প্রতিটা element-এর জন্য।

| বিষয় | XML Views | Compose |
|---|---|---|
| Layout লেখা | XML + Kotlin দুই জায়গায় | শুধু Kotlin |
| UI আপডেট | হাতে view বদলাতে হয় | state বদলালেই হয় |
| List | RecyclerView + Adapter + ViewHolder | `LazyColumn` |
| Reuse | custom View, include, style | সাধারণ function |
| Preview | XML preview | `@Preview`, interactive |
| Animation | Animator, MotionLayout | `animate*AsState`, `AnimatedVisibility` |

- **কেন teams সরে:** কম code, কম bug (state আর UI এক জায়গায়), test সহজ, Google-এর নতুন library (Material 3, adaptive, Navigation 3) আগে Compose-এ আসে।
- **Trade-off:** debug build ধীর লাগে। Recomposition না বুঝলে performance খারাপ হয়। পুরনো custom View থাকলে interop লাগে। APK সামান্য বড় হয়।
- **Flutter mapping:** Flutter-এর widget tree আর Compose-এর composable tree একই idea। পার্থক্য: Compose native Android View system-এর উপর বসে (একটা `ComposeView` হলো আসল View), আর platform-এর accessibility, text, input সরাসরি ব্যবহার করে।

**Answer (English):**
> "Jetpack Compose is Android's modern UI toolkit. It is declarative: I describe what the UI should look like for a given state, and Compose updates the screen when the state changes. With XML, I had to find views and change them by hand, and the UI often got out of sync with the data. With Compose, the UI and the logic are in one language, Kotlin, so there is less code and fewer bugs. New Google libraries also come to Compose first. The trade-off is that I must understand recomposition and stability, or I can get slow screens. Coming from Flutter, the model felt very natural to me."

**Key words:** `declarative UI` · `UI = f(state)` · `recomposition` · `composable function` · `interop`

**Follow-up:**
- **Q:** Can you use Compose and XML in the same app?
  **A:** "Yes. I can put Compose inside a View with `ComposeView`, and a View inside Compose with `AndroidView`. This lets a team move one screen at a time."
- **Q:** Is Compose slower than Views?
  **A:** "In a debug build it can feel slower. In a release build with R8 and Baseline Profiles it is close to Views for most screens. Bad state reads cause most slowness, not Compose itself."
- **Q:** How is Compose different from Flutter under the hood?
  **A:** "Flutter draws everything with its own engine. Compose runs inside the normal Android View system and uses Android's own text, input and accessibility."

**ভুল করবেন না:** "Compose সব View মুছে দেয়" বলবেন না — Compose নিজেই একটা `ComposeView`-এর ভেতরে চলে।

**আরও দেখুন:** [U2 · Recomposition](#u2) · [U10 · Compose + Views](#u10) · [B7 · Flutter → Android](#b7)

---

### <a id="u2"></a>U2. ★ What is recomposition? How does Compose skip work, and what is stability?

**প্রশ্নটা মানে:** কখন composable আবার চলে, কখন চলে না, আর `@Stable`/`@Immutable`/strong skipping কী করে।
**অন্যভাবেও জিজ্ঞেস করে:** "Why is my composable recomposing too many times?" · "What makes a class stable in Compose?"

**বুঝে নিন:**
- **Recomposition:** কোনো `State` বদলালে, যে composable সেই state পড়েছিল, Compose শুধু সেই scope আবার চালায়।
- **Skip:** Recomposition-এর সময় parent একটা child call করে। Child-এর সব parameter আগের মতো হলে Compose child-এর body চালায় না।
- **Stable type মানে:** Compose ধরে নিতে পারে যে (১) একই input-এ `equals()` একই ফল দেবে, আর (২) public property বদলালে Compose জানতে পারবে।
- **Stable হিসেবে ধরা হয়:** primitive, `String`, function type, enum, সব `val` আর stable property সহ `data class`, `State<T>`।
- **Unstable হিসেবে ধরা হয়:** `var` property সহ class, `List`/`Map`/`Set` (interface, ভেতরে mutable হতে পারে), অন্য module-এর class যা Compose compiler দিয়ে build হয়নি।
- **`@Immutable`:** promise — তৈরি হওয়ার পর কিছুই বদলাবে না।
- **`@Stable`:** promise — বদলাতে পারে, কিন্তু বদলালে Compose জানবে (যেমন ভেতরে `mutableStateOf`)।
- এগুলো শুধু promise। Promise ভাঙলে UI পুরনো data দেখাবে।

**Strong skipping mode (Kotlin 2.0.20 থেকে default):**
| | আগে | Strong skipping-এ |
|---|---|---|
| Unstable parameter | কখনো skip হতো না | skip হয়, যদি instance একই (`===`) |
| Stable parameter | `equals()` দিয়ে তুলনা | একই, `equals()` |
| Lambda | নতুন instance → recompose | lambda নিজে থেকে remember হয় |

- তাই এখন stability কম ব্যথা দেয়। তবু প্রতিবার নতুন `List` instance বানালে (`items.filter {}` composable-এর ভেতরে) skip হবে না।
- অন্য module-এর class-কে stable বলতে compiler-এ **stability configuration file** দেওয়া যায়, বা `kotlinx.collections.immutable`-এর `ImmutableList` ব্যবহার করা যায়।

```kotlin
@Immutable
data class UserUi(val id: String, val name: String, val tags: List<String>)

@Composable
fun UserRow(user: UserUi, onClick: (String) -> Unit) { /* ... */ }
```

**Answer (English):**
> "Recomposition means Compose runs a composable again because a state it read has changed. Compose only re-runs the scopes that read that state. When a parent recomposes, Compose can skip a child if its parameters did not change. For that it needs stable types, where equals is reliable. Since Kotlin 2.0.20, strong skipping mode is on by default, so even unstable parameters can skip if it is the same instance, and lambdas are remembered for me. So I focus on two things: I keep UI models immutable, and I don't create new lists or objects inside the composable on every run. I check real counts in Layout Inspector before I add annotations."

**Key words:** `recomposition scope` · `skipping` · `stable / unstable` · `@Immutable` · `strong skipping mode`

**Follow-up:**
- **Q:** Why is `List<String>` unstable?
  **A:** "Because `List` is an interface. The real object could be a `MutableList` that changes without telling Compose. I can use `ImmutableList` or a stability config file."
- **Q:** What happens if you put `@Immutable` on a class that changes?
  **A:** "Compose trusts the promise and may skip. The screen can then show old data. So I only use it when the class really never changes."
- **Q:** Does recomposition run in order, on one thread?
  **A:** "I should not assume that. Composables can run often and in any order, so they must be fast and free of side effects."

**ভুল করবেন না:** "recomposition = পুরো screen আবার আঁকা" বলবেন না — শুধু যেখানে state পড়া হয়েছে সেই scope আবার চলে।

**আরও দেখুন:** [U11 · Compose performance](#u11) · [U6 · LazyColumn](#u6) · [K22 · Equality](#k22)

---

### <a id="u3"></a>U3. ★ How do you handle state in Compose? (`remember`, `rememberSaveable`, state hoisting)

**প্রশ্নটা মানে:** State কোথায় রাখবেন, কতক্ষণ বাঁচবে, আর stateless/stateful composable-এর পার্থক্য।
**অন্যভাবেও জিজ্ঞেস করে:** "What is state hoisting?" · "What is the difference between remember and rememberSaveable?"

**বুঝে নিন:**
- `mutableStateOf(x)` — একটা observable value। পড়লে Compose subscribe করে, লিখলে recompose হয়।
- `remember { }` — value টা composition-এ রাখে। Recomposition পার হয়। কিন্তু rotation বা process death-এ হারায়।
- `rememberSaveable { }` — Bundle-এ save হয়। Rotation আর process death পার হয়। শুধু Bundle-এ রাখা যায় এমন type (বা custom `Saver`)।
- **কোন state কোথায়:**

| State | কোথায় রাখবেন |
|---|---|
| ছোট UI state (expanded, text field-এর লেখা, scroll) | `rememberSaveable` বা `remember` |
| Screen data, business logic | `ViewModel` + `StateFlow` |
| ভারী বা বড় data | ViewModel/repository, Bundle-এ নয় |

- **State hoisting:** state composable থেকে বের করে caller-এ দেওয়া। Pattern: `value: T` আর `onValueChange: (T) -> Unit`।
- **Stateless composable:** নিজে state রাখে না। Preview আর test সহজ। Reuse সহজ।
- **Stateful composable:** নিজের ভেতরে `remember` করে। ব্যবহার সহজ, কিন্তু বাইরে থেকে control করা কঠিন।
- সাধারণ নিয়ম: state কে পড়ে আর কে বদলায় — তাদের **সবচেয়ে নিচের common parent**-এ hoist করুন।

```kotlin
@Composable
fun SearchBar(query: String, onQueryChange: (String) -> Unit) {  // stateless
    TextField(value = query, onValueChange = onQueryChange)
}

@Composable
fun SearchScreen() {                                               // stateful
    var query by rememberSaveable { mutableStateOf("") }
    SearchBar(query = query, onQueryChange = { query = it })
}
```

- **Flutter mapping:** `TextEditingController` বা `ValueNotifier` বাইরে রাখা = hoisting। `RestorationMixin` ≈ `rememberSaveable`।

**Answer (English):**
> "In Compose, state is an observable value, usually `mutableStateOf`. I wrap it in `remember` so it survives recomposition. If it must survive rotation or process death, I use `rememberSaveable`, which saves it in the Bundle. Screen data and business logic go in a ViewModel as a StateFlow. I use state hoisting: a composable takes the value and an `onChange` lambda, and the caller owns the state. This makes the composable stateless, easy to preview, test and reuse. I hoist state to the lowest common parent that needs it. The pitfall is putting big objects in `rememberSaveable`, because the Bundle has a size limit."

**Key words:** `mutableStateOf` · `remember` · `rememberSaveable` · `state hoisting` · `stateless composable`

**Follow-up:**
- **Q:** What happens to `remember` state when the composable leaves the screen?
  **A:** "It is forgotten. If the composable comes back, it starts again with the initial value."
- **Q:** Should you put a TextField's text in the ViewModel?
  **A:** "If business logic needs it, like search or validation, yes. Otherwise local `rememberSaveable` is fine. For text fields I also look at the new `TextFieldState` API."
- **Q:** How do you save a custom class with `rememberSaveable`?
  **A:** "I make it `@Parcelize` Parcelable, or I write a custom `Saver`, like `listSaver` or `mapSaver`."

**ভুল করবেন না:** `remember` ছাড়া `mutableStateOf` লিখবেন না — প্রতি recomposition-এ নতুন state তৈরি হবে, value হারাবে।

**আরও দেখুন:** [U9 · Compose + ViewModel](#u9) · [C4 · Process death](#c4) · [U4 · Side effects](#u4)

---

### <a id="u4"></a>U4. ★ What are side effects in Compose? When do you use each effect API?

**প্রশ্নটা মানে:** Composable-এর বাইরের কাজ (network, listener, analytics) নিরাপদে কীভাবে চালাবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between LaunchedEffect and rememberCoroutineScope?" · "How do you register a listener in a composable and clean it up?"

**বুঝে নিন:**
- Composable বারবার, যেকোনো সময় চলতে পারে। তাই body-তে সরাসরি side effect দিলে সেটা বারবার চলবে।
- Effect API গুলো lifecycle-aware: composition-এ ঢুকলে শুরু, বের হলে বন্ধ।

| API | কখন |
|---|---|
| `LaunchedEffect(key)` | composition-এ ঢুকলে coroutine চালায়। key বদলালে আগেরটা cancel করে নতুন চালায়। |
| `DisposableEffect(key)` | কিছু register করে `onDispose { }`-এ unregister। Listener, observer, sensor। |
| `SideEffect { }` | প্রতি সফল recomposition-এর পর চলে। Compose state-কে non-Compose object-এ পাঠাতে। |
| `rememberCoroutineScope()` | Click-এর মতো event থেকে coroutine চালাতে। Composition ছাড়লে cancel হয়। |
| `produceState` | non-Compose source (callback, suspend) থেকে `State` বানাতে। |
| `rememberUpdatedState(x)` | লম্বা effect-এর ভেতরে latest value পড়তে, effect restart না করে। |

```kotlin
@Composable
fun LifecycleLogger(onStart: () -> Unit) {
    val currentOnStart by rememberUpdatedState(onStart)
    val owner = LocalLifecycleOwner.current
    DisposableEffect(owner) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_START) currentOnStart()
        }
        owner.lifecycle.addObserver(observer)
        onDispose { owner.lifecycle.removeObserver(observer) }
    }
}
```

- **Key বাছাই:** `LaunchedEffect(Unit)` মানে একবারই। `LaunchedEffect(userId)` মানে userId বদলালে আবার।
- Business logic (data load) ViewModel-এ রাখুন। Effect দিয়ে UI-এর কাজ করুন: snackbar দেখানো, scroll, animation, focus।
- **Flutter mapping:** `initState` + `dispose` ≈ `DisposableEffect`। `didUpdateWidget`-এ কাজ restart ≈ `LaunchedEffect`-এর key।

**Answer (English):**
> "A side effect is any work that goes outside the composable, like a network call, a listener, or analytics. Composables can run many times, so I never do this work directly in the body. I use `LaunchedEffect` to run a coroutine tied to a key; when the key changes, it cancels and restarts. I use `DisposableEffect` when I need cleanup, like removing a lifecycle observer or a sensor listener. For clicks I use `rememberCoroutineScope`. `rememberUpdatedState` lets a long effect read the latest lambda without restarting. My rule is: data loading lives in the ViewModel, and effects only handle UI work like showing a snackbar or scrolling."

**Key words:** `LaunchedEffect` · `DisposableEffect` · `onDispose` · `rememberCoroutineScope` · `rememberUpdatedState` · `effect key`

**Follow-up:**
- **Q:** Why not use `LaunchedEffect` inside an `onClick`?
  **A:** "Effects are composables, and `onClick` is not a composable scope. For events I use `rememberCoroutineScope().launch`."
- **Q:** What is `produceState` for?
  **A:** "It turns a non-Compose source, like a callback or a suspend call, into a `State` that the UI can read. It runs in a coroutine tied to the composition."
- **Q:** What is the risk of `LaunchedEffect(Unit)`?
  **A:** "It runs only once. If it captures a value that later changes, it keeps the old one. I fix that with the right key or `rememberUpdatedState`."

**ভুল করবেন না:** `DisposableEffect`-এ `onDispose` বাদ দেওয়া যায় না — এটা দিতেই হবে, আর cleanup না করলে leak হয়।

**আরও দেখুন:** [U9 · Compose + ViewModel](#u9) · [K11 · Structured concurrency](#k11) · [U5 · derivedStateOf](#u5)

---

### <a id="u5"></a>U5. ◆ What are `derivedStateOf` and `snapshotFlow`?

**প্রশ্নটা মানে:** State থেকে নতুন state কখন বানাবেন, আর Compose state-কে Flow-তে কীভাবে নেবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you show a 'scroll to top' button only when the list is scrolled?" · "How do you convert Compose state to a Flow?"

**বুঝে নিন:**
- **`derivedStateOf`:** একটা state অনেক বার বদলায়, কিন্তু আপনার দরকার তার থেকে বের করা একটা ফল, যা কম বদলায়। তখন ব্যবহার করুন।
- উদাহরণ: `firstVisibleItemIndex` প্রতি scroll-এ বদলায়। কিন্তু "button দেখাব কি?" (`index > 0`) শুধু একবার বদলায়। `derivedStateOf` ফল একই থাকলে recompose করায় না।
- `remember`-এর সাথে ব্যবহার করুন, না হলে প্রতিবার নতুন হবে।
- ভুল ব্যবহার: input যতবার বদলায় ফলও ততবার বদলায় (যেমন `"$first $last"`) — তখন `derivedStateOf` লাভ দেয় না, শুধু খরচ বাড়ায়।

```kotlin
val listState = rememberLazyListState()
val showScrollToTop by remember {
    derivedStateOf { listState.firstVisibleItemIndex > 0 }
}
```

- **`snapshotFlow { }`:** Compose state-কে cold `Flow` বানায়। Block-এর ভেতরে পড়া state বদলালে নতুন value emit করে (একই value হলে emit করে না)।
- ব্যবহার: scroll position analytics-এ পাঠানো, debounce করা, ViewModel-এ পাঠানো।

```kotlin
LaunchedEffect(listState) {
    snapshotFlow { listState.firstVisibleItemIndex }
        .filter { it > 20 }
        .collect { analytics.logDeepScroll() }
}
```

**Answer (English):**
> "`derivedStateOf` creates a state from other states, and it only triggers recomposition when the result really changes. A good example is a scroll-to-top button: the scroll index changes all the time, but 'index greater than zero' changes rarely. I always wrap it in `remember`. I don't use it when the result changes as often as the input, because then it only adds cost. `snapshotFlow` goes the other way: it turns Compose state into a Flow. I use it inside a `LaunchedEffect` to send scroll events to analytics, or to debounce input."

**Key words:** `derivedStateOf` · `snapshotFlow` · `reduce recomposition` · `cold Flow`

**Follow-up:**
- **Q:** Why not just compute `index > 0` directly in the composable?
  **A:** "Then the composable reads the index directly, so it recomposes on every scroll pixel change. `derivedStateOf` limits that to real result changes."

**ভুল করবেন না:** প্রতিটা হিসাবেই `derivedStateOf` দেবেন না — শুধু যখন input ঘন ঘন বদলায় কিন্তু ফল কম বদলায়।

**আরও দেখুন:** [U6 · LazyColumn](#u6) · [U4 · Side effects](#u4) · [K12 · Cold vs hot Flow](#k12)

---

### <a id="u6"></a>U6. ★ How do you make a `LazyColumn` fast?

**প্রশ্নটা মানে:** লম্বা list-এ jank কেন হয়, আর key, contentType, stable model দিয়ে কীভাবে ঠিক করবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Your LazyColumn scrolls with jank. What do you check?" · "Why do you need keys in a LazyColumn?"

**বুঝে নিন:**
- `LazyColumn` শুধু দেখা যাওয়া item compose করে। Scroll করলে নতুন item compose হয়, পুরনোগুলোর node আবার ব্যবহার হয়।
- **`key`:** default-এ item-এর পরিচয় হলো তার position। মাঝে item ঢোকালে বা সরালে পরের সব item-এর state ভুল জায়গায় যায় আর সব recompose হয়। Stable id দিলে Compose item ঠিকভাবে চেনে, state (`remember`) item-এর সাথে থাকে, আর `Modifier.animateItem()` কাজ করে।
- **`contentType`:** আলাদা ধরনের row (header, ad, photo) থাকলে type বলে দিন। তাহলে একই ধরনের node-ই reuse হয়।
- **Item-এর ভেতরে ভারী কাজ নয়:** date format, sort, filter, JSON parse — এগুলো ViewModel-এ আগেই করে UI model বানান।
- **Stable item model:** immutable `data class`, ভেতরে শুধু দেখানোর জন্য প্রস্তুত data।
- **Image:** Coil-এর মতো library দিয়ে সঠিক size-এ load করুন। পুরো resolution bitmap নয়।
- **Nested scroll একই দিকে নয়:** `LazyColumn`-এর ভেতরে `verticalScroll` Column বা আরেকটা LazyColumn দেবেন না।
- **Scroll position পড়া:** `listState.firstVisibleItemIndex` সরাসরি পড়লে প্রতি scroll-এ recompose হয় — `derivedStateOf` ব্যবহার করুন।
- **মাপুন release build-এ।** Debug build-এ Compose অনেক ধীর।

```kotlin
LazyColumn {
    items(
        items = feed,                         // List<FeedItemUi>, immutable
        key = { it.id },
        contentType = { it.type }
    ) { item ->
        FeedRow(item, modifier = Modifier.animateItem())
    }
}
```

- **Flutter mapping:** `ListView.builder` + `itemExtent` + `ValueKey(id)` — একই idea।

**Answer (English):**
> "First I give every item a stable `key`, like the database id. Without a key, Compose uses the position, so an insert at the top makes every row recompose and can move state to the wrong row. If the list has different row types, I set `contentType` so Compose reuses the right nodes. I keep item models immutable and ready to show; formatting and sorting happen in the ViewModel, not in the row. I load images at the right size. I also avoid nested scrolling in the same direction. And I always measure in a release build, because a debug build is much slower and can fool you."

**Key words:** `key` · `contentType` · `item reuse` · `stable UI model` · `animateItem` · `release build`

**Follow-up:**
- **Q:** What happens if two items have the same key?
  **A:** "The app crashes. Keys must be unique in the list."
- **Q:** How do you test scroll performance?
  **A:** "I write a Macrobenchmark with `FrameTimingMetric` that flings the list, on a release build, and I look at frame times. Then I check a system trace for long frames."

**ভুল করবেন না:** key হিসেবে index দেবেন না — সেটা default-এর মতোই, কোনো লাভ নেই।

**আরও দেখুন:** [U2 · Stability](#u2) · [U11 · Compose performance](#u11) · [U15 · RecyclerView](#u15)

---

### <a id="u7"></a>U7. ◆ Why does Modifier order matter?

**প্রশ্নটা মানে:** Modifier chain কোন দিক থেকে কাজ করে, আর ভুল order-এ কী বাগ হয়।
**অন্যভাবেও জিজ্ঞেস করে:** "Is `padding().background()` the same as `background().padding()`?" · "Where do you put `clickable` in the chain?"

**বুঝে নিন:**
- Modifier chain বাঁ থেকে ডানে (উপর থেকে নিচে) প্রয়োগ হয়। প্রতিটা modifier পরেরটাকে wrap করে।
- Size/constraint বাইরে থেকে ভেতরে যায়। তাই আগের modifier পরেরটার জন্য জায়গা ঠিক করে।

| Chain | ফল |
|---|---|
| `.padding(16.dp).background(Red)` | Padding বাইরে, রং শুধু ভেতরের অংশে |
| `.background(Red).padding(16.dp)` | পুরো জায়গায় রং, content ভেতরে সরে |
| `.clickable{}.padding(16.dp)` | Padding সহ পুরো জায়গা click হয় (বড় touch target) |
| `.padding(16.dp).clickable{}` | শুধু ভেতরের অংশ click হয় |
| `.clip(CircleShape).background(..)` | গোল background |
| `.background(..).clip(CircleShape)` | Background চারকোণা থেকে যায় |

- `size()` আগে দিলে পরের `size()` কাজ করে না (প্রথম constraint জেতে), যদি না `requiredSize` দেন।
- **Performance:** state lambda modifier ব্যবহার করুন — `Modifier.offset { IntOffset(x, 0) }` composition skip করে শুধু layout চালায়। `graphicsLayer { alpha = a }` শুধু draw চালায়।
- Reusable composable-এর প্রথম optional parameter হবে `modifier: Modifier = Modifier`, আর সেটা root-এ সবার আগে লাগান।

**Answer (English):**
> "Modifier order matters because each modifier wraps the next one, from left to right. So `padding` then `background` gives a colored area inside the padding, while `background` then `padding` colors the whole area. The same is true for `clickable`: if I put it before `padding`, the whole padded area is clickable, which gives a bigger touch target. For `clip`, it must come before `background` to cut the shape. For performance, I use lambda versions like `offset { }` or `graphicsLayer { }`, so a changing value only re-runs layout or draw, not composition."

**Key words:** `modifier chain` · `order matters` · `touch target` · `graphicsLayer` · `deferred read`

**Follow-up:**
- **Q:** Why should a composable accept a `modifier` parameter?
  **A:** "So the caller can control size, padding and position. I apply it on the root element first, and I give it a default of `Modifier`."

**আরও দেখুন:** [U17 · Accessibility](#u17) · [U11 · Compose performance](#u11)

---

### <a id="u8"></a>U8. ★ How does navigation work in Compose?

**প্রশ্নটা মানে:** Type-safe route, argument পাঠানো, back stack, আর নতুন Navigation 3 সম্পর্কে জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you pass data between screens in Compose?" · "What is Navigation 3 and how is it different?"

**বুঝে নিন:**
- **Navigation Compose (2.8+)** — route এখন `@Serializable` class/object। String route আর হাতে argument parse লাগে না।

```kotlin
@Serializable object Home
@Serializable data class Camera(val cameraId: String)

NavHost(navController, startDestination = Home) {
    composable<Home> { HomeScreen(onOpen = { navController.navigate(Camera(it)) }) }
    composable<Camera> { entry ->
        val route: Camera = entry.toRoute()
        CameraScreen(route.cameraId)
    }
}
```

- ViewModel-এ argument পড়তে: `savedStateHandle.toRoute<Camera>()`।
- **ID পাঠান, object নয়।** কারণ:
  - Argument Bundle-এ save হয় — বড় object হলে `TransactionTooLargeException`-এর ঝুঁকি।
  - Object পুরনো হয়ে যেতে পারে। পরের screen repository থেকে id দিয়ে নতুন data নেবে — single source of truth।
  - Deep link আর process death-এ শুধু id দিয়েই screen আবার বানানো যায়।
- **Back stack:** `navigate()` push করে। `popBackStack()` সরায়। `popUpTo(Home) { inclusive = false }` দিয়ে login-এর পর পেছনের screen মুছুন। `launchSingleTop = true` দিয়ে একই screen দুবার না।
- **Navigation 3:** নতুন Compose-first library। এখানে back stack হলো **আপনার নিজের list** (`SnapshotStateList` of keys)। Push = `add`, pop = `removeLastOrNull()`। `NavDisplay` সেই list দেখে UI দেখায়। Adaptive layout (list-detail একসাথে দেখানো) সহজ, "scene" ধারণা দিয়ে। 1.0 stable হয় November 2025-এ। এখন (late 2026) stable version 1.2 — নতুন version Jetpack release page-এ দেখে নিন।

```kotlin
@Serializable data object HomeKey : NavKey
@Serializable data class DetailKey(val id: String) : NavKey

val backStack = rememberNavBackStack(HomeKey)
NavDisplay(
    backStack = backStack,
    onBack = { backStack.removeLastOrNull() },
    entryProvider = entryProvider {
        entry<HomeKey> { HomeScreen(onOpen = { backStack.add(DetailKey(it)) }) }
        entry<DetailKey> { key -> DetailScreen(key.id) }
    }
)
```

- **Flutter mapping:** Nav 2.8 ≈ `go_router` with typed routes। Navigation 3 ≈ Flutter Navigator 2.0, যেখানে `pages` list আপনি নিজে রাখেন।

**Answer (English):**
> "I use type-safe routes: each screen is a `@Serializable` class, and the arguments are its fields. I navigate with `navController.navigate(Camera(id))`, and read it with `toRoute()`, or with `savedStateHandle.toRoute()` in the ViewModel. I pass only IDs, not full objects. Arguments are saved in a Bundle, so big objects can crash, and the data can get old. The next screen loads fresh data by ID from the repository. For the back stack I use `popUpTo` and `launchSingleTop`, for example after login. For new apps I also look at Navigation 3, where I own the back stack as a simple list. That makes adaptive layouts easier."

**Key words:** `type-safe routes` · `@Serializable` · `toRoute()` · `pass IDs` · `popUpTo` · `Navigation 3` · `NavDisplay`

**Follow-up:**
- **Q:** How do you return a result to the previous screen?
  **A:** "With Navigation Compose I can set a value in `previousBackStackEntry?.savedStateHandle`. Often a better way is a shared ViewModel or the repository, so both screens read the same data."
- **Q:** How do you handle deep links?
  **A:** "I add a `deepLinks` list to the destination with a URI pattern, and add the intent filter in the manifest. Because I pass only IDs, the deep link can build the screen easily."
- **Q:** When would you pick Navigation 3?
  **A:** "For a new Compose-only app, or one with list-detail layouts on tablets. For an existing app on Navigation Compose, I would not migrate without a clear reason."

**ভুল করবেন না:** পুরো object JSON বানিয়ে route-এ পাঠাবেন না — id পাঠান, data repository থেকে নিন।

**আরও দেখুন:** [U9 · Compose + ViewModel](#u9) · [C16 · Deep links](#c16) · [U14 · Large screens](#u14)

---

### <a id="u9"></a>U9. ★ How do you connect Compose with a ViewModel?

**প্রশ্নটা মানে:** UiState মডেল, flow collect, আর one-time event (navigation, snackbar) ঠিকভাবে কীভাবে করবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you expose state from a ViewModel to Compose?" · "How do you handle one-time events like showing a snackbar?"

**বুঝে নিন:**
- ViewModel একটা `StateFlow<UiState>` দেয়। UI শুধু পড়ে, আর event lambda দিয়ে ViewModel-কে জানায়। এটাই unidirectional data flow (UDF)।
- **UiState রূপ:**
  - `data class` — যখন অনেক field একসাথে থাকে (loading + data + error)।
  - `sealed interface` — যখন একটা state থাকলে অন্যটা থাকে না (Loading / Success / Error)।
- **`collectAsStateWithLifecycle()`** — lifecycle STARTED-এর নিচে গেলে collect বন্ধ করে। সাধারণ `collectAsState()` background-এও চলতে থাকে, তাই battery আর upstream কাজ নষ্ট হয়।
- `stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), initial)` — UI চলে গেলে ৫ সেকেন্ড পরে upstream বন্ধ। Rotation-এ (৫ সেকেন্ডের কম) চালু থাকে।

```kotlin
data class CameraListUiState(
    val isLoading: Boolean = true,
    val cameras: List<CameraUi> = emptyList(),
    val errorMessage: String? = null,
)

class CameraListViewModel(repo: CameraRepository) : ViewModel() {
    val uiState: StateFlow<CameraListUiState> = repo.observeCameras()
        .map { CameraListUiState(isLoading = false, cameras = it) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), CameraListUiState())
}

@Composable
fun CameraListRoute(viewModel: CameraListViewModel) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    CameraListScreen(state)
}
```

- **One-time event:** Google-এর বর্তমান পরামর্শ: event-কে state হিসেবে রাখুন। যেমন `userMessage: String?`। UI দেখানোর পর `onMessageShown()` call করে null করে।
- অনেক team `Channel` + `receiveAsFlow()` ব্যবহার করে। এটা কাজ করে, কিন্তু lifecycle-এর ঠিক সীমায় event হারাতে পারে। জানুন, আর বলুন কেন আপনি কোনটা বাছেন।
- **Route/Screen ভাগ:** `CameraListRoute` ViewModel ধরে, `CameraListScreen` শুধু state নেয় — preview আর test সহজ।
- **Flutter mapping:** ViewModel + StateFlow ≈ `Cubit`/`Bloc` বা Riverpod `Notifier`। `collectAsStateWithLifecycle` ≈ `BlocBuilder`, কিন্তু lifecycle-aware।

**Answer (English):**
> "The ViewModel exposes one `StateFlow` of a UiState class, and the screen collects it with `collectAsStateWithLifecycle`. That stops collection when the app goes to the background, which saves work and battery. I build the flow with `stateIn` and `WhileSubscribed(5_000)`, so rotation does not restart the upstream. I use a data class when fields live together, and a sealed interface when states exclude each other. For one-time events like a snackbar, I prefer to keep them in the state, and the UI tells the ViewModel when it has shown them. I split the screen into a Route that holds the ViewModel and a stateless Screen that is easy to preview and test."

**Key words:** `StateFlow` · `UiState` · `collectAsStateWithLifecycle` · `WhileSubscribed` · `unidirectional data flow` · `one-time events`

**Follow-up:**
- **Q:** Why `WhileSubscribed(5000)` and not `Eagerly`?
  **A:** "`Eagerly` keeps the upstream running while the ViewModel lives, even in the background. Five seconds is longer than a rotation, so the flow survives config changes but stops when the user really leaves."
- **Q:** Do you pass the ViewModel down to child composables?
  **A:** "No. I pass state and lambdas. Only the top-level route knows the ViewModel. This keeps children reusable and testable."
- **Q:** What about LiveData?
  **A:** "It still works in old code, but for new code I use StateFlow. It is Kotlin-first, works with coroutines and is easy to test."

**ভুল করবেন না:** Compose-এ শুধু `collectAsState()` বলবেন না — Android-এ `collectAsStateWithLifecycle()` সঠিক উত্তর।

**আরও দেখুন:** [R1 · ViewModel](#r1) · [K13 · StateFlow](#k13) · [K15 · One-time events](#k15)

---

### <a id="u10"></a>U10. ◆ How do you mix Compose and Views? (e.g. a video player or camera preview)

**প্রশ্নটা মানে:** `ComposeView` আর `AndroidView` জানেন কিনা, আর SurfaceView-এর মতো ভারী view Compose-এ কীভাবে রাখবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you show an RTSP camera stream inside a Compose screen?" · "How do you add Compose to an old Fragment?"

**বুঝে নিন:**
- **View-এর ভেতরে Compose:** `ComposeView`। Fragment-এ `ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed` সেট করুন, যাতে Fragment-এর view lifecycle-এর সাথে composition মরে।
- **Compose-এর ভেতরে View:** `AndroidView(factory, update, onRelease)`।
  - `factory` — একবার view তৈরি।
  - `update` — state বদলালে view আপডেট।
  - `onRelease` — composition ছাড়লে cleanup (player release)।
- **Video (Media3):** `PlayerView` (একটা View, ভেতরে SurfaceView) `AndroidView`-এ রাখা যায়। নতুন option: `media3-ui-compose`-এর `PlayerSurface` composable।
- **SurfaceView vs TextureView:** SurfaceView আলাদা surface-এ সরাসরি compositor-এ যায় — কম battery, কম latency, DRM সাপোর্ট। TextureView সাধারণ view-এর মতো transform/alpha নেয়, কিন্তু খরচ বেশি। Video আর camera-র জন্য সাধারণত SurfaceView।
- Compose foundation-এ `AndroidExternalSurface` (SurfaceView-ভিত্তিক) আর `AndroidEmbeddedExternalSurface` (TextureView-ভিত্তিক) composable আছে — সরাসরি surface পেতে।
- **Camera:** CameraX-এর `PreviewView` `AndroidView`-এ, বা নতুন `camera-compose`-এর `CameraXViewfinder`।
- **Player কোথায় রাখবেন:** Player-এর মালিক composable নয়। ViewModel বা একটা holder-এ রাখুন, lifecycle (ON_STOP-এ pause/release) মেনে। Composable শুধু surface যুক্ত করে।

```kotlin
@Composable
fun CameraStream(player: Player, modifier: Modifier = Modifier) {
    AndroidView(
        factory = { context -> PlayerView(context).apply { useController = false } },
        update = { view -> view.player = player },
        onRelease = { view -> view.player = null },
        modifier = modifier,
    )
}
```

- RTSP stream-এর জন্য Media3-এর `RtspMediaSource` আছে (`media3-exoplayer-rtsp` module)।

**Answer (English):**
> "I use `ComposeView` to put Compose inside a View or Fragment, and `AndroidView` to put a View inside Compose. In `AndroidView`, `factory` creates the view once, `update` runs when state changes, and `onRelease` cleans up. For a camera stream I would use Media3: a `PlayerView` in `AndroidView`, or the newer `PlayerSurface` composable. Media3 supports RTSP with `RtspMediaSource`. I prefer SurfaceView for video because it is cheaper on battery and has lower delay than TextureView. The player itself does not live in the composable. I keep it in a holder tied to the lifecycle, and I release it on stop."

**Key words:** `ComposeView` · `AndroidView` · `ViewCompositionStrategy` · `SurfaceView` · `PlayerSurface` · `onRelease`

**Follow-up:**
- **Q:** What is the problem with a SurfaceView inside a scrolling list?
  **A:** "SurfaceView draws in a separate layer, so in old Android versions it could lag behind scroll or clip badly. On modern versions it is much better, but I still test it, and I avoid many live surfaces in one list."
- **Q:** Why does the Fragment need a special composition strategy?
  **A:** "A Fragment's view can be destroyed while the Fragment lives. The strategy disposes the composition with the view lifecycle, so there is no leak."

**ভুল করবেন না:** `factory`-তে state পড়ে view বানাবেন না — `factory` একবারই চলে, পরে state আপডেট `update`-এ দিন।

**আরও দেখুন:** [F6 · SurfaceView](#f6) · [V3 · IP camera stream](#v3) · [V4 · Many feeds](#v4)

---

### <a id="u11"></a>U11. ◆ How do you find and fix Compose performance problems?

**প্রশ্নটা মানে:** আন্দাজে নয়, tool দিয়ে কীভাবে মাপেন আর ঠিক করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "A Compose screen is slow. Walk me through your steps." · "How do you check recomposition counts?"

**বুঝে নিন:**
**ধাপ ১ — সঠিক build-এ মাপুন:** Debug build-এ Compose অনেক ধীর (R8 নেই, debug check আছে, code interpreted/JIT)। Release build (`isMinifyEnabled = true`) বা `benchmark` build type-এ পরীক্ষা করুন।

**ধাপ ২ — Tool:**
| Tool | কী দেখায় |
|---|---|
| Layout Inspector | প্রতিটা composable কতবার recompose হলো আর কতবার skip হলো |
| Compose compiler reports/metrics | কোন class stable/unstable, কোন function skippable |
| System trace (Perfetto) + composition tracing | কোন frame-এ কোন composable বেশি সময় নিল |
| Macrobenchmark (`FrameTimingMetric`, `StartupTimingMetric`) | Frame time আর startup, নিয়মিত মাপা |

```kotlin
// build.gradle.kts (app)
composeCompiler {
    reportsDestination = layout.buildDirectory.dir("compose_compiler")
    metricsDestination = layout.buildDirectory.dir("compose_compiler")
}
```

**ধাপ ৩ — সাধারণ কারণ আর সমাধান:**
- ঘন ঘন বদলানো state উপরের দিকে পড়া → যতটা নিচে সম্ভব পড়ুন, lambda modifier ব্যবহার করুন (`offset { }`, `graphicsLayer { }`)।
- প্রতি recomposition-এ নতুন list/object → `remember` বা ViewModel-এ বানান।
- Scroll state সরাসরি পড়া → `derivedStateOf`।
- LazyColumn-এ key নেই → key আর contentType দিন।
- Composition-এ ভারী কাজ (sort, format, parse) → ViewModel-এ, background-এ।
- প্রথম run ধীর (JIT) → **Baseline Profile**। এটা গুরুত্বপূর্ণ code আগে থেকে compile (AOT) করে রাখে।

**Answer (English):**
> "First, I measure in a release build, because a debug build is much slower and gives wrong results. Then I use Layout Inspector to see recomposition and skip counts, and I find the composables that recompose too often. I turn on Compose compiler reports to see which classes are unstable. For frame drops I take a system trace with Perfetto. Common fixes are: read fast-changing state as low as possible, use lambda modifiers like `graphicsLayer`, use `derivedStateOf` for scroll state, add keys to lazy lists, and move heavy work to the ViewModel. Finally, I add a Baseline Profile and a Macrobenchmark, so I can see if things get better or worse over time."

**Key words:** `Layout Inspector` · `recomposition count` · `compiler reports` · `release build` · `Baseline Profile` · `Macrobenchmark`

**Follow-up:**
- **Q:** What does a Baseline Profile do?
  **A:** "It lists the classes and methods used on key paths, like startup and scrolling. The device compiles them ahead of time at install, so the first run is fast and does not wait for JIT."
- **Q:** Should you add `@Stable` everywhere?
  **A:** "No. With strong skipping most cases are already fine. I add it only when reports and real counts show a problem."

**ভুল করবেন না:** Debug build-এ jank দেখে "Compose ধীর" বলবেন না — আগে release build-এ মাপুন।

**আরও দেখুন:** [U2 · Stability](#u2) · [P4 · Jank](#p4) · [F2 · Baseline Profiles](#f2)

---

### <a id="u12"></a>U12. ○ How do you do theming in Compose? (Material 3, dynamic color, dark mode)

**প্রশ্নটা মানে:** Material 3 theme কীভাবে সাজান, dynamic color আর dark mode কীভাবে দেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you support dark mode in Compose?" · "What is dynamic color?"

**বুঝে নিন:**
- `MaterialTheme(colorScheme, typography, shapes)` — পুরো app-কে wrap করে। Child-রা `MaterialTheme.colorScheme.primary` পড়ে। এটা `CompositionLocal` দিয়ে নিচে যায়।
- **Dark mode:** `isSystemInDarkTheme()` দিয়ে light বা dark `ColorScheme` বাছুন।
- **Dynamic color (Android 12+):** wallpaper থেকে রং নেয়। `dynamicLightColorScheme(context)` / `dynamicDarkColorScheme(context)`। পুরনো version-এ নিজের scheme।
- Brand রং কঠোর হলে dynamic color বন্ধ রাখা যায় — এটা product সিদ্ধান্ত।
- **Typography:** `Typography(bodyLarge = TextStyle(...))`। Font size `sp`-এ, যাতে user-এর font scale মানে (Android 14 থেকে non-linear font scaling 200% পর্যন্ত)।
- Hardcoded রং (`Color(0xFF...)`) সরাসরি UI-তে নয়, theme token ব্যবহার করুন — তাহলে dark mode আপনাআপনি ঠিক থাকে।
- Material 3 Expressive হলো নতুন design update (2025)। Phone-এর `compose-material3` 1.5.0 (stable, Nov 2026)-এ এর বেশিরভাগ component stable হয়েছে। কিছু API (যেমন `LoadingIndicator`, `MaterialShapes`) এখনো experimental — opt-in লাগে কিনা API page-এ দেখে নিন।

```kotlin
@Composable
fun AppTheme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
    val context = LocalContext.current
    val colors = when {
        Build.VERSION.SDK_INT >= Build.VERSION_CODES.S ->
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        darkTheme -> DarkColors
        else -> LightColors
    }
    MaterialTheme(colorScheme = colors, typography = AppTypography, content = content)
}
```

- **Flutter mapping:** `ThemeData` + `ColorScheme.fromSeed` ≈ `MaterialTheme` + `ColorScheme`। Flutter-এর `dynamic_color` package ≈ এখানে built-in API।

**Answer (English):**
> "I wrap the app in a `MaterialTheme` with a color scheme, typography and shapes. Composables read colors from the theme, never hard-coded values, so dark mode works everywhere. I pick the light or dark scheme with `isSystemInDarkTheme()`. On Android 12 and up I can use dynamic color, which builds the scheme from the user's wallpaper; on older versions I fall back to my own scheme. If the brand needs fixed colors, I turn dynamic color off. For text I use `sp` and test with large font sizes."

**Key words:** `MaterialTheme` · `ColorScheme` · `dynamic color` · `isSystemInDarkTheme` · `CompositionLocal` · `sp`

**Follow-up:**
- **Q:** How do you add a custom color that Material does not have?
  **A:** "I create my own data class of extra colors and provide it with a `staticCompositionLocalOf`, inside my app theme."

**আরও দেখুন:** [U17 · Accessibility](#u17) · [U16 · dp vs sp](#u16)

---

### <a id="u13"></a>U13. ★ What is edge-to-edge, how do you handle window insets, and what is predictive back?

**প্রশ্নটা মানে:** Android 15/16-এর mandatory UI নিয়ম জানেন কিনা, আর inset ঠিকভাবে সামলান কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "After targeting Android 15, our toolbar went under the status bar. Why?" · "How do you support predictive back gesture?"

**বুঝে নিন:**
**Edge-to-edge:**
- App-এর content status bar আর navigation bar-এর **পেছনে** আঁকা হয়।
- targetSdk 35 (Android 15) হলে Android 15 device-এ এটা **mandatory**। targetSdk 36 (Android 16)-এ opt-out attribute (`windowOptOutEdgeToEdgeEnforcement`) আর কাজ করে না।
- তাই আপনাকে নিজে **insets** সামলাতে হবে, না হলে button বা text system bar-এর নিচে ঢাকা পড়ে।
- Activity-তে `enableEdgeToEdge()` call করুন (পুরনো version-এও একই চেহারা পাবেন)।

**Compose-এ insets:**
- `Scaffold` নিজে `innerPadding` দেয় — content-এ সেটা লাগান।
- `Modifier.windowInsetsPadding(WindowInsets.safeDrawing)` — system bar, cutout, keyboard সব বাদ দেয়।
- `Modifier.imePadding()` — keyboard-এর জন্য। `navigationBarsPadding()`, `statusBarsPadding()`।
- List-এর জন্য padding `contentPadding`-এ দিন, যাতে list bar-এর পেছন দিয়ে scroll হয় কিন্তু শেষ item ঢাকা না পড়ে।
- Views-এ: `ViewCompat.setOnApplyWindowInsetsListener`।

**Predictive back:**
- Back gesture শুরু করলে system আগেই পেছনের screen (বা home) দেখায়। User ছাড়লে তবেই back হয়।
- targetSdk 36-এ এই system animation **default চালু**। `onBackPressed()` আর call হয় না, `KEYCODE_BACK`-ও আসে না।
- তাই back ধরতে: Views-এ `OnBackPressedDispatcher` + `OnBackPressedCallback`, Compose-এ `BackHandler` বা `PredictiveBackHandler` (gesture-এর progress পায়, নিজের animation বানানো যায়)।
- Navigation library আর Material component (sheet, drawer, search) নিজেরাই predictive back সাপোর্ট করে।

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContent { AppTheme { AppNavHost() } }
    }
}
```

- **Flutter mapping:** Flutter-এ `SafeArea` আর `MediaQuery.padding` / `viewInsets` — Compose-এ `WindowInsets` একই কাজ করে। Flutter app-ও targetSdk 35+-এ এই নিয়মে পড়ে।

**Answer (English):**
> "Edge-to-edge means the app draws behind the status bar and navigation bar. It is enforced when an app targets Android 15, and from Android 16 the opt-out no longer works. So I must handle insets myself. I call `enableEdgeToEdge()` in the Activity, use the `Scaffold` inner padding, and use `WindowInsets.safeDrawing` or `imePadding` where needed. For lists I put the insets in `contentPadding`. Predictive back shows a preview of the previous screen during the back gesture. When targeting Android 16 it is on by default, and `onBackPressed()` is not called. So I handle back with `OnBackPressedCallback`, or `BackHandler` in Compose. I always test with gesture and three-button navigation, and with the keyboard open."

**Key words:** `edge-to-edge` · `enableEdgeToEdge()` · `WindowInsets` · `safeDrawing` · `imePadding` · `predictive back` · `BackHandler`

**Follow-up:**
- **Q:** Why should you not just add a fixed 24dp top padding?
  **A:** "Bar height changes by device, cutout, orientation and gesture mode. Insets give the real values, so I always use them."
- **Q:** An old screen overrides `onBackPressed()`. What breaks on Android 16?
  **A:** "If the app targets 36, that method is not called on back, so the custom logic is skipped. I move it to an `OnBackPressedCallback` and enable it only when I need to stop the back."
- **Q:** How do you block back during an upload?
  **A:** "I register a callback or `BackHandler(enabled = isUploading)`. When enabled, it takes the back event; when the upload ends, I disable it so the system back works again."

**ভুল করবেন না:** "edge-to-edge optional" বলবেন না — targetSdk 35-এ mandatory, 36-এ opt-out-ও নেই।

**আরও দেখুন:** [U14 · Large screens](#u14) · [P11 · Android versions](#p11)

---

### <a id="u14"></a>U14. ◆ How do you support large screens and foldables?

**প্রশ্নটা মানে:** WindowSizeClass দিয়ে adaptive layout, আর Android 16/17-এর orientation/resize নিয়ম জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How does your app look on a tablet or foldable?" · "What changed for large screens in Android 16?"

**বুঝে নিন:**
- **Device type দেখে নয়, window size দেখে** layout বাছুন। Split-screen, freeform window, fold — সব ক্ষেত্রে window ছোট-বড় হয়।
- **WindowSizeClass width breakpoint:** Compact < 600dp, Medium 600–839dp, Expanded 840–1199dp। নতুন library-তে Large (1200–1599dp) আর Extra-large (≥1600dp)-ও আছে — চালু করতে `currentWindowAdaptiveInfo(supportLargeAndXLargeWidth = true)`।

```kotlin
val sizeClass = currentWindowAdaptiveInfo().windowSizeClass
val showTwoPanes = sizeClass.isWidthAtLeastBreakpoint(
    WindowSizeClass.WIDTH_DP_EXPANDED_LOWER_BOUND
)
```

- **Ready-made adaptive component (Material 3 adaptive):**
  - `NavigationSuiteScaffold` — ছোট screen-এ bottom bar, বড়তে navigation rail/drawer।
  - `ListDetailPaneScaffold` — ফোনে list → detail, ট্যাবে পাশাপাশি।
- **Foldable:** `WindowInfoTracker` দিয়ে `FoldingFeature` পান — hinge কোথায়, tabletop posture কিনা। যেমন camera app-এ tabletop-এ উপরে preview, নিচে control।
- **Configuration change:** resize/fold হলে Activity আবার তৈরি হতে পারে। State ViewModel আর `rememberSaveable`-এ রাখুন।
- **Android 16 (API 36):** smallest width ≥ 600dp display-এ `screenOrientation`, `resizeableActivity=false`, `minAspectRatio`/`maxAspectRatio` মানা হয় না। App-কে সব আকারে চলতে হবে। একটা temporary opt-out ছিল।
- **Android 17 (API 37):** সেই opt-out বাদ। Game (`android:appCategory="game"`) ছাড়া কেউ ছাড় পায় না।
- Camera preview-এর জন্য খেয়াল: orientation lock আর কাজ না করলে preview rotation আর aspect ratio নিজে ঠিক করতে হবে। CameraX এটা অনেকটা সামলায়।

**Answer (English):**
> "I choose the layout from the window size, not the device type, because of split screen and foldables. I use `WindowSizeClass`: compact under 600dp, medium up to 840, and expanded above that. Material 3 adaptive gives me `NavigationSuiteScaffold` and `ListDetailPaneScaffold`, so a phone shows one pane and a tablet shows two. For foldables I read `FoldingFeature` to handle the hinge or tabletop mode. Since Android 16, on screens of 600dp or more, apps that target 36 cannot lock orientation or resizing, and Android 17 removes the temporary opt-out, except for games. So I keep state in the ViewModel and test resizing on a tablet emulator."

**Key words:** `WindowSizeClass` · `breakpoints` · `ListDetailPaneScaffold` · `NavigationSuiteScaffold` · `FoldingFeature` · `resizability`

**Follow-up:**
- **Q:** Your app is portrait-only. What happens on a tablet with Android 16 and 17?
  **A:** "If it targets 36 or 37, the lock is ignored on large screens, so the app can rotate and resize. I must make the layout work in landscape and keep state across the change."
- **Q:** How do you test this?
  **A:** "I use resizable and foldable emulators, split screen, and Compose previews with different device sizes. I also run my UI tests on a tablet size."

**ভুল করবেন না:** "আমরা portrait lock করে দেই" — Android 16+ large screen-এ এটা আর কাজ করে না।

**আরও দেখুন:** [U16 · Screen sizes](#u16) · [C4 · Config change](#c4) · [U8 · Navigation](#u8)

---

### <a id="u16"></a>U16. ★ dp vs sp vs px — how do you support different screen sizes and densities?

**প্রশ্নটা মানে:** Unit গুলোর পার্থক্য জানেন কিনা, আর resource qualifier, density bucket আর vector drawable দিয়ে সব screen-এ UI ঠিক রাখেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why should you not use px in layouts?" · "How does Android pick the right image for a device?"

**বুঝে নিন:**
- **px** — screen-এর আসল pixel। Device ভেদে pixel-এর আকার আলাদা, তাই layout-এ px দিলে এক phone-এ বড়, আরেকটায় ছোট দেখায়।
- **dp (density-independent pixel)** — 160 dpi screen-এ 1dp = 1px। হিসাব: `px = dp × (dpi / 160)`। সব density-তে চোখে প্রায় একই সাইজ। Layout, padding, size সব dp-তে।
- **sp (scale-independent pixel)** — dp-এর মতোই, কিন্তু user-এর font size setting মানে। Text-এর জন্য শুধু sp।
- Android 14 থেকে font scaling non-linear, 200% পর্যন্ত। বড় text আগের চেয়ে কম বাড়ে, ছোট text বেশি বাড়ে। তাই text-এর container-এর height fix করবেন না।

**Density bucket:**

| Qualifier | dpi | 1dp = |
|---|---|---|
| `mdpi` | ~160 | 1px |
| `hdpi` | ~240 | 1.5px |
| `xhdpi` | ~320 | 2px |
| `xxhdpi` | ~480 | 3px |
| `xxxhdpi` | ~640 | 4px |

- Bitmap (PNG/WebP) দিলে প্রতি bucket-এর জন্য আলাদা file লাগে। না থাকলে system কাছের bucket থেকে scale করে — ঝাপসা বা ভারী হয়।
- **Vector drawable** (XML, SVG থেকে import) — একটা file, সব density-তে পরিষ্কার। Icon আর সাধারণ shape-এর জন্য এটাই প্রথম পছন্দ। খুব জটিল ছবি বা photo-র জন্য নয় (draw খরচ বেশি)।
- Launcher icon `mipmap-*` folder-এ থাকে।
- **AAB** দিলে Play প্রতি device-এ শুধু তার density-র resource পাঠায়।

**Resource qualifier — system নিজে ঠিক file বাছে:**
- `values-sw600dp/` — smallest width ≥ 600dp (tablet)। `w600dp` — এখনকার width।
- `layout-land/`, `values-night/` (dark mode), `values-bn/` (ভাষা), `drawable-xxhdpi/`।
- Compose-এ layout qualifier কম লাগে — সেখানে `WindowSizeClass` দিয়ে code-এ বাছাই করুন। কিন্তু string, dimen, drawable এখনো resource থেকে আসে।

```kotlin
Text(
    text = stringResource(R.string.camera_title),
    fontSize = 16.sp,                       // text → sp
    modifier = Modifier.padding(16.dp)      // size → dp
)
```

- **Flutter mapping:** Flutter-এর logical pixel = Android-এর dp। `MediaQuery.textScaler` = sp-এর font scale। Flutter-এর `2.0x/3.0x` asset folder = এখানে density bucket।

**Answer (English):**
> "px is a real screen pixel, and its size changes by device, so I never use it for layout. dp is density-independent: one dp is one pixel on a 160 dpi screen, so things look about the same size everywhere. I use dp for sizes and padding. sp is like dp, but it also follows the user's font size, so I use it only for text. For images, I prefer vector drawables, because one file stays sharp on every density. For photos I give versions for each density bucket, and the AAB sends each device only what it needs. For tablets I use `sw600dp` qualifiers, or `WindowSizeClass` in Compose. I always test with the largest font size."

**Key words:** `dp` · `sp` · `px` · `density bucket` · `xxhdpi` · `vector drawable` · `resource qualifier` · `sw600dp`

**Follow-up:**
- **Q:** How many pixels is 48dp on an xxhdpi phone?
  **A:** "xxhdpi is about 480 dpi, so the factor is three. 48dp is about 144 pixels."
- **Q:** Should you use sp for icon sizes?
  **A:** "No. sp is only for text. If icons grow with the font, the layout can break. I use dp for icons."
- **Q:** What happens if an image exists only in `drawable-mdpi`?
  **A:** "The system scales it up on high-density screens. It looks blurry and uses more memory at runtime. I use a vector, or add the higher-density files."

**ভুল করবেন না:** Text-এ dp দেবেন না — তাহলে user font বড় করলেও text বড় হবে না, এটা accessibility bug।

**আরও দেখুন:** [U14 · Large screens](#u14) · [U17 · Accessibility](#u17) · [P6 · AAB splits](#p6)

---

### <a id="u17"></a>U17. ◆ How do you make an app accessible, and how do you test it?

**প্রশ্নটা মানে:** TalkBack, contentDescription / Compose semantics, touch target, font scale আর color contrast — এগুলো জানেন কিনা আর কীভাবে test করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How does TalkBack read your Compose UI?" · "What accessibility checks do you do before a release?"

**বুঝে নিন:**
- **TalkBack** — Android-এর screen reader। Element focus করে তার label, role (button, checkbox) আর state (checked, selected) পড়ে শোনায়। Compose UI এটা পায় **semantics tree** থেকে। View-এ পায় `AccessibilityNodeInfo` থেকে।
- **Label:**
  - View-এ `android:contentDescription`। Compose-এ `Icon(contentDescription = "...")` / `Image(...)`।
  - শুধু সাজানোর ছবি হলে `contentDescription = null` — TalkBack skip করে।
  - Label-এ "button" লিখবেন না — role থেকে TalkBack নিজে বলে।
- **Compose semantics:**
  - `Modifier.semantics(mergeDescendants = true) { }` — একটা row-এর ছবি + নাম + status একসাথে একবারে পড়ায়।
  - `Modifier.clickable(onClickLabel = "Open camera")`, `stateDescription`, `heading()` — heading দিয়ে TalkBack user section ধরে লাফাতে পারে।
  - Custom component হলে `role = Role.Switch` ইত্যাদি দিন।
- **Touch target:** কমপক্ষে **48×48dp**। Material component নিজে এটা দেয়। ছোট icon হলেও clickable জায়গা বড় রাখুন।
- **Font scale:** text-এ `sp`, fixed height নয়, বড় font-এ text কেটে না যায় (Android 14+ এ 200% পর্যন্ত)।
- **Color contrast:** সাধারণ text-এ কমপক্ষে **4.5:1**, বড় text-এ 3:1 (WCAG)। শুধু রং দিয়ে অর্থ বোঝাবেন না (লাল = error) — সাথে icon বা লেখা দিন।
- **Test কীভাবে:**
  - নিজে **TalkBack** চালু করে মূল flow চালান (login, camera list, alert খোলা)।
  - **Accessibility Scanner** app — screen দেখে ছোট target, কম contrast, label নেই এমন সমস্যা বলে।
  - Android Studio **Layout Inspector / Compose preview**-এ বড় font scale দেখুন।
  - Automated: Espresso-তে `AccessibilityChecks.enable()`। Compose UI test-এ semantics দিয়ে node খুঁজুন (`onNodeWithContentDescription`), আর নতুন ui-test version-এ accessibility check চালু করা যায় (version release page-এ দেখে নিন)।

```kotlin
Row(
    modifier = Modifier
        .semantics(mergeDescendants = true) {}
        .clickable(onClickLabel = "Open live view") { onOpen(camera.id) }
        .heightIn(min = 48.dp)
) {
    Icon(Icons.Default.Videocam, contentDescription = null)   // শুধু সাজানো
    Text(camera.name)
    Text(if (camera.isOnline) "Online" else "Offline")
}
```

- **Flutter mapping:** Flutter-এর `Semantics` widget আর `MergeSemantics` = Compose-এর `semantics` আর `mergeDescendants`।

**Answer (English):**
> "I build accessibility in from the start. Every icon or image that means something gets a `contentDescription`, and decorative ones get null so TalkBack skips them. In Compose I use semantics: I merge a row so it is read as one item, add click labels, roles and headings. Touch targets are at least 48dp. Text uses sp, and I check the screen at the largest font size so nothing is cut. Text contrast is at least 4.5 to 1, and I never show meaning with color only. To test, I use TalkBack myself on the main flows, run Accessibility Scanner, and add accessibility checks to my UI tests."

**Key words:** `TalkBack` · `contentDescription` · `semantics` · `mergeDescendants` · `48dp touch target` · `font scale` · `contrast 4.5:1` · `Accessibility Scanner`

**Follow-up:**
- **Q:** A list row has an image, a name and a status. TalkBack reads three items. How do you fix it?
  **A:** "I add `semantics(mergeDescendants = true)` on the row, and set the image description to null if it is decorative. Then TalkBack reads the row as one item."
- **Q:** Your icon button is 24dp. Is that a problem?
  **A:** "The icon can be 24dp, but the touch area must be at least 48dp. `IconButton` already does this. For custom code I add padding or `minimumInteractiveComponentSize()`."

**ভুল করবেন না:** সব ছবিতে description দেবেন না — শুধু সাজানোর ছবি হলে `null` দিন, না হলে TalkBack অকারণে কথা বলে।

**আরও দেখুন:** [U7 · Modifier order](#u7) · [U12 · Theming](#u12) · [R15 · UI tests](#r15)

---

### <a id="u18"></a>U18. ◆ How do you localize an Android app? (strings, plurals, RTL, per-app language)

**প্রশ্নটা মানে:** String resource, plural, RTL layout আর Android 13-এর per-app language ঠিকভাবে করতে জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you add Bangla and Arabic support?" · "How does the user change the app language without changing the phone language?"

**বুঝে নিন:**
- **String resource:** সব লেখা `res/values/strings.xml`-এ। অনুবাদ `values-bn/`, `values-ar/` folder-এ। System device-এর locale দেখে ঠিক file বাছে। Code-এ hardcoded text নয়।
- **Placeholder:** `"Camera %1$s is offline"` — শব্দের ক্রম ভাষা ভেদে বদলায়, তাই string জোড়া লাগাবেন না।
- **Plurals:** `<plurals>` আর `quantity="zero|one|two|few|many|other"`। ভাষা ভেদে নিয়ম আলাদা (আরবিতে ছয়টা form)। শুধু `if (count == 1)` দিয়ে হবে না।

```xml
<plurals name="alerts_count">
    <item quantity="one">%d new alert</item>
    <item quantity="other">%d new alerts</item>
</plurals>
```
```kotlin
Text(pluralStringResource(R.plurals.alerts_count, count, count))
```

- **RTL (আরবি, হিব্রু, উর্দু):**
  - Manifest-এ `android:supportsRtl="true"`।
  - View-এ `start`/`end` ব্যবহার করুন, `left`/`right` নয়।
  - Compose নিজে `LayoutDirection` মানে — `Row` উল্টে যায়, padding `start`/`end` ঠিক থাকে।
  - দিক বোঝানো icon (back arrow) mirror হওয়া দরকার: `Icons.AutoMirrored.*`, বা vector-এ `android:autoMirrored="true"`।
  - Test: Developer options → "Force RTL layout direction", বা pseudo-locale `ar-XB`।
- **Pseudo-locale:** `en-XA` (লম্বা, accent-ওয়ালা text) আর `ar-XB` (RTL)। Debug build-এ `isPseudoLocalesEnabled = true` দিন। কাটা text আর hardcoded string সহজে ধরা পড়ে।
- **Per-app language (Android 13+):**
  - User system Settings থেকে শুধু আপনার app-এর ভাষা বদলাতে পারে।
  - কোন ভাষা আছে তা `locales_config.xml` দিয়ে জানাতে হয়। AGP 8.1+ এ `androidResources { generateLocaleConfig = true }` দিলে নিজে তৈরি হয়।
  - App-এর ভেতরে language picker: `AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags("bn"))`। এটা পুরনো Android-এও কাজ করে (AppCompat backport; Android 12 বা নিচে manifest-এ `autoStoreLocales` service লাগে)।
- **Locale change = configuration change** — Activity আবার তৈরি হয়। State ViewModel আর `rememberSaveable`-এ রাখুন।
- Date, number, currency format locale দিয়ে করুন (`DateTimeFormatter.ofLocalizedDate`, `NumberFormat.getInstance(locale)`)। বাংলা অঙ্ক (১২৩) locale থেকে আসতে পারে।
- **Flutter mapping:** Flutter-এর ARB file + `intl` = Android-এর `strings.xml` + `plurals`। `Directionality` = Compose-এর `LayoutDirection`।

**Answer (English):**
> "All user text lives in string resources, with one folder per language, like `values-bn`. I use placeholders, not string joining, because word order changes by language. For counts I use plurals, because each language has its own plural rules. For RTL I set `supportsRtl`, use start and end instead of left and right, and mirror direction icons. Compose flips layouts by itself. I test with the pseudo-locales `en-XA` and `ar-XB`. Since Android 13, users can pick a language per app in Settings. I generate the locale config with AGP, and for an in-app picker I use `AppCompatDelegate.setApplicationLocales`, which also works on older versions."

**Key words:** `strings.xml` · `values-bn` · `plurals` · `RTL` · `start / end` · `autoMirrored` · `pseudo-locale` · `per-app language` · `setApplicationLocales`

**Follow-up:**
- **Q:** What happens to the screen when the app language changes?
  **A:** "It is a configuration change, so the Activity is recreated. State in the ViewModel or `rememberSaveable` stays."
- **Q:** How do you find hardcoded strings?
  **A:** "Android Lint warns about hardcoded text. The pseudo-locale also shows it, because hardcoded text does not change."

**ভুল করবেন না:** `"You have " + count + " alerts"` এভাবে string জোড়া দেবেন না — অনুবাদ আর plural দুটোই ভাঙে।

**আরও দেখুন:** [U16 · Resources](#u16) · [U17 · Accessibility](#u17) · [C4 · Config change](#c4)

---

### <a id="u15"></a>U15. ◆ How do RecyclerView, ViewHolder and DiffUtil work? How does a View measure, lay out and draw?

**প্রশ্নটা মানে:** পুরনো View-ভিত্তিক code maintain করতে পারবেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why is ListAdapter better than notifyDataSetChanged?" · "What is the difference between requestLayout and invalidate?"

**বুঝে নিন:**
**RecyclerView:**
- শুধু দেখা যাওয়া item-এর জন্য View বানায়। Scroll-এ বাইরে যাওয়া View আবার ব্যবহার (recycle) করে।
- **ViewHolder** — একটা item View আর তার child reference ধরে রাখে, যাতে বারবার `findViewById` না লাগে।
- `onCreateViewHolder` (কম চলে, inflate) আর `onBindViewHolder` (বেশি চলে, শুধু data বসায় — এখানে ভারী কাজ নয়)।
- **DiffUtil** — পুরনো আর নতুন list তুলনা করে শুধু পরিবর্তন জানায় (insert/remove/move/change)। `areItemsTheSame` (id তুলনা) আর `areContentsTheSame` (data তুলনা)।
- **ListAdapter** — ভেতরে `AsyncListDiffer`, diff background thread-এ হয়। আপনি শুধু `submitList(newList)` দেন।
- `notifyDataSetChanged()` পুরো list আবার bind করে, animation নষ্ট হয়, ধীর।
- আরো কৌশল: `setHasFixedSize(true)` (size content-এ না বদলালে), nested RecyclerView-তে shared `RecycledViewPool`, image সঠিক size-এ।

**View rendering — তিন ধাপ:**
```
measure (onMeasure) → layout (onLayout) → draw (onDraw)
 কত বড় হবে?          কোথায় বসবে?          pixel আঁকা
```
- Parent child-কে `MeasureSpec` দেয়: `EXACTLY`, `AT_MOST`, `UNSPECIFIED`।
- `requestLayout()` — size/position বদলেছে → measure + layout + draw আবার।
- `invalidate()` — শুধু চেহারা বদলেছে → শুধু draw আবার।
- গভীর nested layout (বিশেষ করে weight সহ LinearLayout, RelativeLayout) child-কে একাধিকবার measure করে — ধীর। `ConstraintLayout` দিয়ে flat layout ভালো।
- `onDraw`-এ object allocate করবেন না (Paint, Path) — প্রতি frame-এ GC চাপ।
- **Compose-এর সাথে পার্থক্য:** Compose layout-এ child একবারই measure হয় (দুবার করলে exception)। Intrinsic measurement আলাদা পথ।

**Answer (English):**
> "RecyclerView creates views only for visible items and reuses them when they scroll off screen. A ViewHolder keeps references to the child views, so binding is cheap. I use `ListAdapter` with a `DiffUtil.ItemCallback`: it compares the old and new list on a background thread and only updates what changed, with animations. `notifyDataSetChanged` rebinds everything and is slow. A View draws in three steps: measure, layout, and draw. `requestLayout` runs all three again, and `invalidate` only redraws. For speed I keep layouts flat with ConstraintLayout and never allocate objects in `onDraw`."

**Key words:** `ViewHolder` · `DiffUtil` · `ListAdapter` · `submitList` · `MeasureSpec` · `requestLayout` · `invalidate`

**Follow-up:**
- **Q:** What goes in `areItemsTheSame` vs `areContentsTheSame`?
  **A:** "`areItemsTheSame` checks identity, usually the id. `areContentsTheSame` checks if the visible data is equal, usually with data class equals."
- **Q:** Why must you pass a new list to `submitList`?
  **A:** "If I change the same list object and submit it again, the differ sees the same reference and may skip the update. I always submit a new immutable list."

**ভুল করবেন না:** `onBindViewHolder`-এ click listener-এর ভেতরে `position` capture করবেন না — `bindingAdapterPosition` পড়ুন, কারণ position পরে বদলায়।

**আরও দেখুন:** [U6 · LazyColumn](#u6) · [F5 · Frame drawing](#f5) · [P4 · Jank](#p4)

---


## <a id="part-4"></a>Part 4 — Performance, debugging আর release

Senior interview-এ প্রায় সবসময় জিজ্ঞেস করে: ANR, leak, startup, crash কীভাবে খুঁজে ঠিক করেন, আর app কীভাবে নিরাপদে release করেন।
এখানে interviewer দেখে আপনি **মেপে** কাজ করেন কিনা, আর Play Console-এর নিয়ম (target API, vitals threshold, signing) জানেন কিনা।
Security camera বা custom device-এর কাজে battery, ANR আর long-running service আরো বেশি গুরুত্বপূর্ণ।

### আগে বুঝুন — Performance আর release-এর বড় ছবি

**কাজের ধাপ (সব performance সমস্যায় একই):**
1. **মাপুন** — release-এর মতো build-এ, আসল device-এ। Debug build-এর সংখ্যা বিশ্বাস করবেন না।
2. **খুঁজুন** — trace বা profiler দিয়ে দেখুন সময় বা memory কোথায় যাচ্ছে।
3. **ঠিক করুন** — একটা পরিবর্তন একবারে।
4. **আবার মাপুন** — আগের সাথে তুলনা।
5. **পাহারা দিন** — CI-তে benchmark, production-এ Play vitals/Crashlytics।

**মূল ধারণা:**
- **Main thread** — UI, input, lifecycle callback সব এখানে। এটা আটকালে jank (ছোট আটকানো) বা ANR (৫ সেকেন্ডের মতো বড় আটকানো)।
- **Frame budget** — 60Hz-এ প্রতি frame ~16.6ms, 120Hz-এ ~8.3ms। এর বেশি লাগলে frame পড়ে যায়।
- **ART: JIT vs AOT** — install-এর পর code প্রথমে interpreted/JIT হয়, তাই প্রথম run ধীর। **Baseline Profile** গুরুত্বপূর্ণ code আগেই compile করায়।
- **Process death** — Android যেকোনো সময় background process মেরে ফেলে। State save না করলে data হারায়, আর অনেক "reproduce হয় না" বাগ এখান থেকে আসে।
- **R8** — release build-এ code ছোট, rename আর optimize করে। Crash stack trace পড়তে **mapping file** লাগে।
- **AAB + Play App Signing** — আপনি upload key দিয়ে sign করেন, Google আসল app signing key দিয়ে device-এর জন্য APK বানায়।
- **Play vitals** — crash rate 1.09% আর ANR rate 0.47% (user-perceived, সব device মিলে) পার হলে Play-তে app কম দেখা যেতে পারে। একটা device model-এ 8%।
- **targetSdk** — কোন Android version-এর behavior আপনি মেনে নিয়েছেন। Play প্রতি বছর এটা বাড়াতে বলে।

**Tool-এর এক নজর:**
```
Startup   → Macrobenchmark (StartupTimingMetric), Play vitals startup
Jank      → Perfetto system trace, JankStats, FrameTimingMetric
Memory    → LeakCanary (debug), Android Studio heap dump
ANR       → Play vitals ANR clusters, ApplicationExitInfo, StrictMode (debug)
Crash     → Crashlytics + mapping file, Play vitals
Battery   → Play vitals wake lock metric, Battery Historian / Power Profiler
```

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ jank মানে সাধারণত UI বা raster thread। Native-এ main thread + RenderThread দেখতে হয়, আর binder call, disk I/O, lock-ও কারণ হয়।
- Flutter DevTools-এর বদলে এখানে Android Studio Profiler আর Perfetto।
- Flutter release-এও R8 চলে (Android অংশে), আর Dart code-এর জন্য `--obfuscate --split-debug-info` আলাদা। Native app-এ শুধু R8 mapping।
- Signing, AAB, Play track, vitals — Flutter app-এর মতোই। এই জ্ঞান আপনার আগে থেকেই আছে, শুধু native দিকের tool নতুন।

---

### <a id="p1"></a>P1. ★ What is an ANR? What causes it, and how do you find and fix it?

**প্রশ্নটা মানে:** Main thread কেন আটকায়, production-এ কীভাবে কারণ বের করেন, আর কীভাবে ঠিক করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Your ANR rate is above the Play threshold. What do you do?" · "How do you debug an ANR you cannot reproduce?"

**বুঝে নিন:**
- **ANR (Application Not Responding):** main thread নির্দিষ্ট সময় সাড়া না দিলে system dialog দেখায় বা report করে।
- **সাধারণ সীমা:**
  - Input event (touch, key) — ~5 সেকেন্ডে সাড়া নেই।
  - `BroadcastReceiver.onReceive` — foreground-এ ~10 সেকেন্ড (background-এ বেশি)।
  - Service lifecycle callback শেষ না হওয়া, বা `startForegroundService()`-এর পর সময়মতো `startForeground()` না ডাকা।
- **সাধারণ কারণ:**
  - Main thread-এ disk বা network I/O (database query, file read, বড় JSON parse)।
  - `SharedPreferences.apply()` — pause/stop-এ system pending লেখা শেষ হওয়ার জন্য অপেক্ষা করে। অনেক লেখা থাকলে ANR।
  - Lock contention বা deadlock — main thread এমন lock চায় যা background thread ধরে আছে।
  - ধীর binder call (system service, অন্য process)।
  - Main thread-এ `runBlocking`।
  - `Application.onCreate`-এ ভারী SDK init।
- **কীভাবে খুঁজবেন:**
  - **Play vitals → ANRs** — cluster আর main thread-এর stack দেখায়।
  - **Crashlytics** — ANR report দেয় (Android 11+ এ)।
  - **`ApplicationExitInfo`** (API 30+) — পরের launch-এ জানা যায় process কেন মরেছিল। `REASON_ANR` হলে `traceInputStream` দিয়ে trace পাওয়া যায়।
  - **ProfilingManager (Android 16)** — ANR trigger দিয়ে system নিজে trace ধরে রাখে।
  - **StrictMode** debug build-এ — main thread-এ disk/network হলে log বা crash করায়।
  - Local: `adb bugreport` বা `/data/anr/` trace।
- **ঠিক করা:** I/O `Dispatchers.IO`-তে, SharedPreferences থেকে **DataStore**-এ, receiver-এ লম্বা কাজ `goAsync()` বা WorkManager-এ, lazy SDK init, lock কম রাখা।

```kotlin
if (BuildConfig.DEBUG) {
    StrictMode.setThreadPolicy(
        StrictMode.ThreadPolicy.Builder().detectDiskReads().detectDiskWrites()
            .detectNetwork().penaltyLog().build()
    )
}
```

**Answer (English):**
> "An ANR happens when the main thread is blocked for too long, for example about five seconds without handling an input event. Common causes are disk or network work on the main thread, `SharedPreferences.apply` waiting at pause, lock contention with a background thread, slow binder calls, and heavy SDK init at startup. To find it, I look at ANR clusters in Play vitals and Crashlytics, and read the main thread stack. On Android 11 and up, `ApplicationExitInfo` gives me the ANR trace on the next launch. In debug I turn on StrictMode. To fix it, I move I/O to `Dispatchers.IO`, move from SharedPreferences to DataStore, and move long receiver work to WorkManager."

**Key words:** `main thread` · `input dispatch timeout` · `StrictMode` · `ApplicationExitInfo` · `Play vitals` · `lock contention`

**Follow-up:**
- **Q:** The ANR stack shows the main thread just waiting in `nativePollOnce`. What does that mean?
  **A:** "The main thread was idle at the moment of the dump. The blocking work may have finished already, or the problem is in another place, like a broadcast or service timeout. I check other threads and the ANR type, and I use ProfilingManager or more logs to catch it."
- **Q:** Can a background thread cause an ANR?
  **A:** "Yes, indirectly. If the main thread waits for a lock or a result from that thread, the main thread is blocked."
- **Q:** What is the Play ANR threshold?
  **A:** "The user-perceived ANR rate should stay under 0.47% overall, and under 8% on any single device model."

**ভুল করবেন না:** "coroutine-এ দিলেই ঠিক" বলবেন না — `Dispatchers.Main`-এ coroutine চালালে কাজ এখনো main thread-এই হয়।

**আরও দেখুন:** [C12 · Main thread](#c12) · [K9 · Dispatchers](#k9) · [P10 · Production bugs](#p10)

---

### <a id="p2"></a>P2. ★ What causes memory leaks on Android, and how do you find them?

**প্রশ্নটা মানে:** Leak-এর সাধারণ কারণ, LeakCanary আর Memory Profiler দিয়ে কীভাবে ধরেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you find out why an Activity is not garbage collected?" · "What is a heap dump and how do you read it?"

**বুঝে নিন:**
- **Leak মানে:** কোনো object আর দরকার নেই (যেমন destroy হওয়া Activity), কিন্তু কেউ তার reference ধরে আছে, তাই GC মুছতে পারে না।
- Activity leak হলে তার পুরো View tree, bitmap সব থেকে যায়। শেষে `OutOfMemoryError` বা ঘন ঘন GC-তে jank।
- **সাধারণ কারণ:**
  - Singleton বা `companion object`/static field-এ Activity, View বা Activity `Context` রাখা।
  - Listener/callback register করে unregister না করা — `SensorManager`, `LocationManager`, broadcast receiver, camera callback।
  - শেষ না হওয়া coroutine বা `GlobalScope` যা Activity ধরে আছে।
  - `Handler.postDelayed` যার Runnable Activity-কে ধরে।
  - Fragment-এ ViewBinding `onDestroyView`-এ null না করা।
  - ViewModel-এ View, Activity বা Fragment reference।
  - Camera/MediaPlayer/ExoPlayer release না করা (native memory-ও আটকায়)।
- **LeakCanary (debug build):**
  - শুধু `debugImplementation` dependency দিন, code লাগে না।
  - Destroy হওয়া Activity, Fragment, View, ViewModel, Service-কে "watch" করে।
  - কিছুক্ষণ পরে আর GC-এর পরেও থাকলে heap dump নেয়, analyze করে **leak trace** দেখায় — GC root থেকে leaked object পর্যন্ত reference chain।
- **Android Studio Memory Profiler:**
  - **Heap dump** — এই মুহূর্তে কোন class-এর কতগুলো instance, কে ধরে আছে।
  - Activity/Fragment leak filter আছে।
  - **Allocation tracking** — কোন code বেশি object বানাচ্ছে (GC চাপ)।
- **ধাপ:** screen খুলুন → বন্ধ করুন → GC চালান → heap dump → Activity instance এখনো আছে কিনা দেখুন → reference chain পড়ুন।

```kotlin
class CameraFragment : Fragment(R.layout.fragment_camera) {
    private var _binding: FragmentCameraBinding? = null
    private val binding get() = _binding!!

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        _binding = FragmentCameraBinding.bind(view)
    }
    override fun onDestroyView() {
        _binding = null          // Fragment বেঁচে থাকে, view মরে
        super.onDestroyView()
    }
}
```

**Answer (English):**
> "A memory leak is when an object we don't need is still referenced, so the GC cannot free it. The classic case is a destroyed Activity kept by a singleton, a static field, an unregistered listener, or a running coroutine. In debug builds I always add LeakCanary. It watches destroyed Activities, Fragments and ViewModels, and when one is not collected it shows the full reference chain to the leak. For deeper work I take a heap dump in the Android Studio Memory Profiler and check which instances are still alive and who holds them. To prevent leaks, I use lifecycle-aware scopes, unregister listeners in the matching callback, and use the application context for long-lived objects."

**Key words:** `memory leak` · `GC root` · `LeakCanary` · `heap dump` · `reference chain` · `application context`

**Follow-up:**
- **Q:** Is it fine to keep the Application context in a singleton?
  **A:** "Yes. The Application lives as long as the process, so it does not leak. But I don't use it to inflate views or show dialogs, because it has no theme or window."
- **Q:** How do sensor listeners leak?
  **A:** "`SensorManager` keeps a reference to the listener. If the listener is my Activity and I don't call `unregisterListener` in `onPause` or `onStop`, the Activity stays in memory and the sensor keeps using battery."

**ভুল করবেন না:** LeakCanary release build-এ দেবেন না — শুধু `debugImplementation`।

**আরও দেখুন:** [C11 · Context leaks](#c11) · [U4 · DisposableEffect](#u4) · [N3 · Sensors & battery](#n3)

---

### <a id="p3"></a>P3. ★ How do you make app startup faster?

**প্রশ্নটা মানে:** Startup কীভাবে মাপেন, আর কোন কৌশলে কমান।
**অন্যভাবেও জিজ্ঞেস করে:** "Our cold start takes 3 seconds. Where do you start?" · "What are Baseline Profiles?"

**বুঝে নিন:**
- **Startup ধরন:** Cold (process নেই, সবচেয়ে ধীর), Warm (process আছে, Activity নতুন), Hot (Activity শুধু সামনে আসে)। Cold start-এ মনোযোগ দিন।
- **মেট্রিক:** **TTID** (প্রথম frame দেখা গেল) আর **TTFD** (আসল content প্রস্তুত — `reportFullyDrawn()` ডেকে জানান)।
- **মাপা:**
  - **Macrobenchmark** — `StartupTimingMetric`, release-এর মতো build, আসল device, বারবার চালিয়ে median।
  - Play vitals-এ startup time।
  - দ্রুত দেখতে: `adb shell am start -W`।
- **কৌশল:**
  - **`Application.onCreate` হালকা রাখুন।** শুধু যা প্রথম screen-এর জন্য লাগে।
  - **Lazy init** — Hilt-এ `Lazy<T>` বা `Provider<T>` inject করুন, প্রথম ব্যবহারে তৈরি হবে।
  - **App Startup library** — অনেক library নিজের `ContentProvider` দিয়ে startup-এ init হয়। App Startup সবাইকে একটা provider-এ আনে, dependency order ঠিক করে, আর চাইলে auto-init বন্ধ করে পরে lazy init করা যায়।
  - কাজ background thread-এ — কিন্তু main thread যদি সেই ফলের জন্য অপেক্ষা করে, লাভ নেই।
  - **Baseline Profile** — startup আর মূল journey-র code AOT compile হয়। Baseline Profile Gradle plugin আর Macrobenchmark দিয়ে generate করুন। **Startup Profile** DEX layout-ও ঠিক করে।
  - **R8** release-এ চালু।
  - প্রথম screen-এর layout সহজ রাখুন, বড় image পরে load।
- **SplashScreen API (Android 12+, `core-splashscreen` দিয়ে পুরনোতেও):** `installSplashScreen()`। আলাদা Splash Activity বানাবেন না। `setKeepOnScreenCondition` দিয়ে সামান্য অপেক্ষা করা যায়, কিন্তু splash দিয়ে ধীর startup লুকাবেন না।

```kotlin
class MainActivity : ComponentActivity() {
    private val viewModel: MainViewModel by viewModels()
    override fun onCreate(savedInstanceState: Bundle?) {
        val splash = installSplashScreen()
        super.onCreate(savedInstanceState)
        splash.setKeepOnScreenCondition { viewModel.isLoadingSession.value }
        setContent { AppTheme { AppNavHost() } }
    }
}
```

**Answer (English):**
> "First I measure cold start with Macrobenchmark on a real device and a release-like build, and I also check startup in Play vitals. I track both time to first frame and time to full display, using `reportFullyDrawn`. Then I make `Application.onCreate` as light as possible: I init SDKs lazily, use Hilt `Lazy` or `Provider`, and use the App Startup library to control library init. I add a Baseline Profile, so startup code is compiled ahead of time and does not wait for JIT. R8 is always on for release. I use the SplashScreen API, not a separate splash Activity. The pitfall is moving work to a background thread while the main thread still waits for it."

**Key words:** `cold start` · `TTID / TTFD` · `Macrobenchmark` · `App Startup` · `lazy init` · `Baseline Profile` · `SplashScreen API`

**Follow-up:**
- **Q:** How do you generate a Baseline Profile?
  **A:** "I add a baseline profile module with the Gradle plugin, write a test that runs startup and key user journeys, and run it on a device or Gradle managed device. The profile is then packed into the release build."
- **Q:** Why not just show a splash screen longer?
  **A:** "It hides the problem but the user still waits. Users and Play vitals see the real time. I fix the cause first."
- **Q:** How do you stop a library's auto init?
  **A:** "With App Startup I can remove its initializer from the manifest with `tools:node="remove"`, then call `AppInitializer` when I first need it."

**ভুল করবেন না:** Debug build-এ startup মাপবেন না — debug-এ সংখ্যা অনেক খারাপ আর ভুল দিক দেখায়।

**আরও দেখুন:** [F2 · ART & Baseline Profiles](#f2) · [F1 · App launch](#f1) · [P5 · R8](#p5)

---

### <a id="p4"></a>P4. ◆ How do you find and fix jank and frame drops?

**প্রশ্নটা মানে:** Frame কেন পড়ে, কোন tool দিয়ে প্রমাণ করেন, আর কী ঠিক করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Scrolling is not smooth. How do you debug it?" · "How do you measure jank in production?"

**বুঝে নিন:**
- **Jank:** একটা frame সময়ের মধ্যে (60Hz-এ 16.6ms, 120Hz-এ 8.3ms) তৈরি হয়নি, তাই screen আটকে যায়।
- **Frame-এর পথ:** main thread (input, animation, measure/layout, record draw) → RenderThread (GPU-তে পাঠায়) → compositor।
- **Tool:**
  - **Perfetto / system trace** — Android Studio CPU profiler-এ "system trace" বা ui.perfetto.dev। Main thread-এ লম্বা slice খুঁজুন: `Choreographer#doFrame`, inflate, measure, GC, binder, lock wait।
  - **Macrobenchmark `FrameTimingMetric`** — CI-তে frame time মাপা।
  - **JankStats library** — production-এ jank frame ধরে, সাথে "state" (কোন screen, কোন কাজ) যোগ করা যায়। Analytics-এ পাঠান।
  - Developer options: **Debug GPU overdraw**, **Profile HWUI rendering**।
- **সাধারণ কারণ ও সমাধান:**
  - Main thread-এ I/O বা ভারী হিসাব → background-এ।
  - বড় image main thread-এ decode → Coil/Glide, সঠিক size।
  - Overdraw (একই pixel অনেকবার আঁকা) → অপ্রয়োজনীয় background সরান।
  - গভীর layout, বারবার `requestLayout` → flat layout।
  - `onDraw` বা composition-এ allocation → GC চাপ → আগে বানিয়ে রাখুন।
  - প্রথম run-এ JIT → Baseline Profile।
  - Compose-এ অতিরিক্ত recomposition → U11 দেখুন।

**Answer (English):**
> "Jank means a frame took longer than its budget, about 16 milliseconds at 60 hertz, or 8 at 120. To find the cause, I record a system trace with Perfetto and look for long work on the main thread or RenderThread, like disk I/O, image decoding, inflation, GC or lock waits. For lab numbers I use Macrobenchmark with `FrameTimingMetric`. In production I use the JankStats library, and I tag frames with the current screen, so I know where jank happens. Common fixes are moving work off the main thread, decoding images at the right size, removing overdraw, avoiding allocations in draw code, and adding a Baseline Profile."

**Key words:** `frame budget` · `Perfetto` · `system trace` · `JankStats` · `FrameTimingMetric` · `overdraw`

**Follow-up:**
- **Q:** What is overdraw?
  **A:** "It is when the same pixel is drawn many times in one frame, like a window background, then a screen background, then a card background. I check it with the GPU overdraw option and remove extra backgrounds."

**ভুল করবেন না:** শুধু অনুভূতি দিয়ে "এখন smooth" বলবেন না — trace বা frame metric দিয়ে আগে-পরে দেখান।

**আরও দেখুন:** [F5 · Frame drawing](#f5) · [U11 · Compose performance](#u11) · [U6 · LazyColumn](#u6)

---

### <a id="p5"></a>P5. ★ What does R8 do? How do keep rules and mapping files work?

**প্রশ্নটা মানে:** Release build-এ code কীভাবে ছোট আর সুরক্ষিত হয়, কী ভাঙে, আর crash stack trace কীভাবে পড়বেন।
**অন্যভাবেও জিজ্ঞেস করে:** "The app crashes only in release. What do you check?" · "What is the mapping file and why do you need it?"

**বুঝে নিন:**
- **R8** হলো Android-এর code shrinker/optimizer (ProGuard-এর বদলে)। একসাথে DEX-ও বানায়।
- **চার কাজ:**
  1. **Shrinking (tree shaking)** — ব্যবহার না হওয়া class, method, field মুছে দেয়।
  2. **Resource shrinking** — `isShrinkResources = true` দিলে ব্যবহার না হওয়া resource মুছে দেয়।
  3. **Obfuscation** — নাম ছোট করে (`a`, `b`)। APK ছোট হয়, reverse engineering কঠিন হয় (কিন্তু অসম্ভব নয় — এটা নিরাপত্তার মূল ব্যবস্থা নয়)।
  4. **Optimization** — inline, class merge, dead branch মোছা।
- **Full mode** — AGP 8.0 থেকে default। আরো aggressive। Reflection দিয়ে ব্যবহার হওয়া code ভাঙার ঝুঁকি বেশি।
- **AGP 9:** `proguard-android.txt` (optimization বন্ধ করা file) আর সাপোর্ট করে না — `proguard-android-optimize.txt` ব্যবহার করুন।
- **Keep rule কখন লাগে:** যে code R8 static ভাবে দেখতে পায় না —
  - Reflection (Gson-এর মতো reflection-ভিত্তিক JSON, `Class.forName`)
  - JNI থেকে call হওয়া Kotlin/Java method
  - Manifest-এর বাইরে নাম দিয়ে load হওয়া class
- Library সাধারণত নিজের **consumer rules** দেয়। Reflection-মুক্ত library (kotlinx.serialization, Moshi codegen) পছন্দ করুন।
- Keep rule যত সরু সম্ভব। `-keep class com.myapp.** { *; }` দিলে R8-এর লাভই চলে যায়।

```kotlin
// build.gradle.kts
buildTypes {
    release {
        isMinifyEnabled = true
        isShrinkResources = true
        proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
    }
}
```

- **Mapping file:** `build/outputs/mapping/release/mapping.txt` — পুরনো নাম ↔ নতুন নাম। এটা ছাড়া crash stack trace পড়া যায় না।
  - AAB upload করলে Play Console mapping file নিজে পায় আর vitals-এ stack trace deobfuscate করে।
  - Crashlytics Gradle plugin release build-এ mapping নিজে upload করে।
  - প্রতিটা release-এর mapping file রাখুন (CI artifact)। হাতে পড়তে `retrace` tool।
  - Native (.so) crash-এর জন্য native debug symbols আলাদা upload (`ndk { debugSymbolLevel = "FULL" }`)।

**Answer (English):**
> "R8 runs on release builds. It removes unused code and resources, renames classes and methods to short names, and optimizes the code, for example by inlining. Full mode is the default since AGP 8, so it removes and changes more code. The risk is code used only through reflection or JNI, which R8 cannot see, so it may remove or rename it and the app crashes only in release. I fix that with narrow keep rules, or better, by using libraries without reflection, like kotlinx.serialization. Because names are changed, crash stack traces are unreadable without the mapping file. Play gets it from the app bundle, Crashlytics uploads it with its Gradle plugin, and I keep each release's mapping file in CI."

**Key words:** `R8` · `shrinking` · `obfuscation` · `full mode` · `keep rules` · `consumer rules` · `mapping.txt` · `retrace`

**Follow-up:**
- **Q:** Is obfuscation enough to protect secrets in the app?
  **A:** "No. It only makes code harder to read. Secrets must not be in the app at all; they stay on the server, and I use Play Integrity and server checks."
- **Q:** How do you catch R8 problems before release?
  **A:** "QA tests a minified release-like build, not debug. I also run instrumented or Macrobenchmark tests on that build in CI."
- **Q:** What does `@Keep` do?
  **A:** "It tells R8 not to remove or rename that class or member. I use it on small, specific things, like a class used by JNI."

**ভুল করবেন না:** mapping file হারাবেন না — পুরনো release-এর crash তখন আর পড়া যাবে না।

**আরও দেখুন:** [P6 · App signing](#p6) · [S8 · APK attacker view](#s8) · [R13 · Serialization](#r13)

---

### <a id="p6"></a>P6. ★ APK vs AAB? How does Play App Signing work, and what if you lose the upload key?

**প্রশ্নটা মানে:** Release format আর signing-এর নিরাপত্তা মডেল বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between the upload key and the app signing key?" · "Why does Google Play need AAB?"

**বুঝে নিন:**
- **APK** — device-এ install হওয়া আসল file। Sign করা, একটা।
- **AAB (Android App Bundle)** — publish করার format, install করা যায় না। Play এটা থেকে প্রতিটা device-এর জন্য ছোট **split APK** বানায় (ABI, screen density, language আলাদা)। User কম download করে।
- নতুন app-এর জন্য Play-তে AAB mandatory (2021 থেকে)। AAB-এর সাথে Play Feature Delivery আর Play Asset Delivery পাওয়া যায়।
- **Play App Signing:**

| Key | কে রাখে | কাজ |
|---|---|---|
| App signing key | Google (নিরাপদ infrastructure-এ) | User-এর device-এ যাওয়া APK sign করে। App-এর পরিচয়। |
| Upload key | আপনি | AAB sign করে Play-তে পাঠান। Play যাচাই করে এটা আপনার। |

- **Upload key হারালে / চুরি হলে:** Play Console-এ account owner **upload key reset** request করে। নতুন keystore বানিয়ে তার certificate (PEM) জমা দেন। Google নতুন key রেজিস্টার করে, কিছু সময় পরে চালু হয়। App-এর পরিচয় বদলায় না, user update পায়।
- **পুরনো মডেলে** (Play App Signing ছাড়া) app signing key হারালে আর update দেওয়া যেত না — নতুন package name দিয়ে নতুন app লাগত। এটাই Play App Signing-এর বড় সুবিধা।
- **ঝুঁকি/নজর:**
  - একই app অন্য store-এ (বা sideload) নিজের key দিয়ে sign করলে signature আলাদা হয় — user এক জায়গা থেকে আরেক জায়গার update install করতে পারবে না।
  - Keystore কখনো git-এ নয়। CI secret-এ রাখুন, password আলাদা।
  - Custom OS/system app-এ আলাদা কথা: system app **platform key** দিয়ে sign হয়, Play-এর বাইরে।

**Answer (English):**
> "An APK is the file that gets installed. An AAB is a publishing format: Play uses it to build smaller split APKs for each device, by ABI, density and language. New apps on Play must use AAB. With Play App Signing, Google keeps the app signing key, which signs what users install. I keep only the upload key, which proves to Play that the upload is from me. If the upload key is lost or leaked, the account owner asks for an upload key reset in Play Console and registers a new certificate. The app identity stays the same, so users keep getting updates. I keep keystores out of git and store them as CI secrets."

**Key words:** `AAB` · `split APKs` · `Play App Signing` · `app signing key` · `upload key` · `upload key reset`

**Follow-up:**
- **Q:** What happens if the app signing key itself is leaked?
  **A:** "With Play App Signing, Google holds it, so that is very unlikely. Play also supports a key upgrade for new installs, with signature rotation on newer Android versions. I would check the current Play Console steps."
- **Q:** How do you test the real APKs that Play will make?
  **A:** "I use internal testing or internal app sharing, or `bundletool` to build APKs from the AAB locally."

**ভুল করবেন না:** "upload key হারালে app শেষ" বলবেন না — Play App Signing থাকলে reset করা যায়।

**আরও দেখুন:** [P9 · CI/CD](#p9) · [O4 · Platform-signed apps](#o4) · [S16 · Supply chain](#s16)

---

### <a id="p7"></a>P7. ◆ How do you save battery? (Doze, wake locks, standby buckets)

**প্রশ্নটা মানে:** System কীভাবে background কাজ limit করে, আর আপনি কীভাবে সেই নিয়মে কাজ করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Our app drains battery. How do you investigate?" · "What is Doze mode and how does it affect your app?"

**বুঝে নিন:**
- **Doze:** screen বন্ধ, charge-এ নেই, device স্থির — তখন system network বন্ধ করে, wake lock মানে না, job আর সাধারণ alarm পিছিয়ে দেয়। মাঝে মাঝে ছোট **maintenance window** দেয়।
- **App Standby Buckets:** user কতটা app ব্যবহার করে তার ভিত্তিতে — Active, Working set, Frequent, Rare, Restricted। নিচের bucket-এ job, alarm, FCM high-priority সীমিত।
- **Wake lock:** partial wake lock screen বন্ধেও CPU চালু রাখে। ছেড়ে দিতে ভুললে battery শেষ।
- **Play vitals-এ excessive wake lock metric:** একটা user session-এ 24 ঘণ্টায় 2 ঘণ্টার বেশি non-exempt wake lock হলে সেটা excessive। 28 দিনে 5% session excessive হলে bad behavior। 1 March 2026 থেকে এমন app Play-এর discovery থেকে বাদ পড়তে পারে আর listing-এ warning দেখাতে পারে। Audio, location আর user-initiated job-এর wake lock ছাড়।
- **ভালো অভ্যাস:**
  - Deferrable কাজ **WorkManager**-এ, constraint সহ (charging, unmetered network)।
  - Network call **batch** করুন। ঘন ঘন ছোট request radio চালু রাখে।
  - Polling-এর বদলে **FCM push**।
  - Exact alarm শুধু সত্যিই লাগলে (alarm clock)। Android 14 থেকে `SCHEDULE_EXACT_ALARM` বেশিরভাগ নতুন install-এ default-এ denied।
  - User-দেখা চলমান কাজ (camera recording, live stream) — সঠিক type-এর **foreground service**।
  - Location: সঠিক priority, interval বড়, কাজ শেষে update বন্ধ।
  - Sensor: যত কম দরকার তত কম sampling rate, batching (`maxReportLatencyUs`), `onPause`-এ unregister।
- **খুঁজতে:** Play vitals (wake lock, background usage), Android Studio-র Power Profiler (যে device-এ চলে), Battery Historian, `adb shell dumpsys batterystats`।
- **Custom OS/dedicated device:** নিজের device হলে system config-এ app-কে power-save allowlist-এ রাখা যায় — কিন্তু এটা শুধু নিজের build-এ, Play app-এ নয়।

**Answer (English):**
> "Android limits background work to save battery. In Doze, when the screen is off and the device is still, network is cut and jobs and alarms wait for short maintenance windows. Standby buckets limit jobs and alarms based on how often the user opens the app. Wake locks keep the CPU on, and since March 2026 Play vitals can flag apps with excessive wake locks and show them less in the store. So I put deferrable work in WorkManager with constraints, batch network calls, use FCM push instead of polling, and use a foreground service only for work the user sees, like live video. I check battery use with Play vitals and the Power Profiler."

**Key words:** `Doze` · `maintenance window` · `App Standby Buckets` · `partial wake lock` · `WorkManager constraints` · `FCM`

**Follow-up:**
- **Q:** A security camera app must keep a live connection. How do you handle Doze?
  **A:** "If the user is watching or recording, I run a foreground service with the right type, like camera or dataSync, so the work is visible and allowed. For alerts when the app is closed, I use high-priority FCM from the server instead of a constant connection."

**ভুল করবেন না:** wake lock নিয়ে timeout ছাড়া `acquire()` করবেন না — সবসময় timeout দিন আর `finally`-তে release করুন।

**আরও দেখুন:** [C10 · Background work](#c10) · [N3 · Sensors & battery](#n3) · [V11 · 24/7 recording](#v11)

---

### <a id="p8"></a>P8. ★ How do you monitor crashes and ANRs in production?

**প্রশ্নটা মানে:** Crashlytics আর Play vitals দিয়ে কীভাবে মান ধরে রাখেন, আর threshold জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What are Android vitals?" · "What do you do after a release when crashes go up?"

**বুঝে নিন:**
- **Crashlytics (Firebase):**
  - Fatal crash, ANR (Android 11+), non-fatal (`recordException`)।
  - **Custom keys** (screen, camera model, network type), **log** (শেষ কিছু ঘটনা), **user id** (personal data নয়)।
  - Velocity alert — নতুন release-এ হঠাৎ বাড়া crash জানায়।
  - Mapping file আর native symbols upload করলে stack trace পড়া যায়।
- **Play vitals (Play Console):**
  - সব Play device থেকে data, user-এর কোনো SDK লাগে না।
  - **Core vitals bad-behavior threshold:**

| Metric | সব device মিলে | একটা device model-এ |
|---|---|---|
| User-perceived crash rate | 1.09% | 8% |
| User-perceived ANR rate | 0.47% | 8% |

  - "User-perceived" মানে user সক্রিয়ভাবে app ব্যবহার করার সময় যা ঘটে।
  - Threshold পার হলে Play-তে app কম দেখা যেতে পারে আর listing-এ warning আসতে পারে।
  - Startup time, excessive wake lock, permission denial — এগুলোও vitals-এ।
- **Release অভ্যাস:** staged rollout (যেমন 1% → 5% → 20% → 100%), প্রতিটা ধাপে crash-free users দেখুন, খারাপ হলে rollout **halt** করুন।
- **গোপনীয়তা:** log-এ personal data বা token নয়। Play-এর Data safety form-এ crash data collection ঘোষণা করুন।
- Sentry বা অন্য tool-ও চলে। নিয়ম একই।

```kotlin
FirebaseCrashlytics.getInstance().apply {
    setCustomKey("camera_model", cameraModel)
    setCustomKey("stream_protocol", "rtsp")
    log("Stream started")
}
```

**Answer (English):**
> "I use two sources. Play vitals gives data from all Play users with no SDK, and it shows if we pass the bad-behavior thresholds: a user-perceived crash rate of 1.09% and an ANR rate of 0.47% overall, or 8% on one device model. Passing them can reduce the app's visibility on Play. Crashlytics gives me more detail: custom keys, logs before the crash, and non-fatal errors that I record myself. I upload mapping files so traces are readable. Every release goes out with a staged rollout, and I watch these numbers at each step. If crashes jump, I halt the rollout and fix first. I never log personal data or tokens."

**Key words:** `Crashlytics` · `non-fatal` · `custom keys` · `Play vitals` · `user-perceived crash rate` · `staged rollout` · `halt rollout`

**Follow-up:**
- **Q:** What is a non-fatal and when do you record one?
  **A:** "It is an error I catch and handle, but I still want to know about it, like a failed decode or a camera that refused to open. I record it with `recordException` and custom keys."
- **Q:** Crash-free users is 99.5%. Is that good?
  **A:** "It depends on the app and the trend. I look at the trend per release and per device, and at the top clusters. A small number can still hide one model that always crashes."
- **Q:** Why does Play vitals sometimes show crashes Crashlytics doesn't?
  **A:** "Play sees crashes at the system level, for example before Crashlytics starts, or native crashes without symbols. So I check both."

**ভুল করবেন না:** threshold ভুল বলবেন না — crash 1.09%, ANR 0.47%, প্রতি device 8%।

**আরও দেখুন:** [P1 · ANR](#p1) · [P10 · Production bugs](#p10) · [P9 · CI/CD](#p9)

---

### <a id="p9"></a>P9. ◆ How do you set up CI/CD for an Android app?

**প্রশ্নটা মানে:** Build, test, sign আর Play-তে release automate করতে জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you release an Android app to Play automatically?" · "How do you keep the signing key safe in CI?"

**বুঝে নিন:**
**Pipeline (GitHub Actions):**
```
PR:      checkout → JDK → Gradle cache → lint + detekt/ktlint → unit tests → assembleDebug
main:    + instrumented tests (emulator / Firebase Test Lab)
tag:     bundleRelease (signed) → upload mapping → Play internal track
manual:  promote internal → closed → production (staged rollout)
```
- **JDK:** AGP 8 আর 9-এর জন্য JDK 17 লাগে (`actions/setup-java`)।
- **Gradle:** `gradle/actions/setup-gradle` cache দেয়। Gradle wrapper commit করুন।
- **Signing:** keystore base64 করে GitHub secret-এ, CI-তে decode করে file বানান। Password environment variable থেকে। কখনো repo-তে নয়।
- **versionCode:** প্রতি upload-এ বাড়তে হবে। CI run number বা tag থেকে নিন।
- **Upload:** **Fastlane `supply`** বা **Gradle Play Publisher** (`publishReleaseBundle`)। দুটোই Google Play Developer API ব্যবহার করে, একটা **service account** JSON key দিয়ে (secret-এ)।
- **Play tracks:**
  - **Internal** — বেশি হলে 100 tester, খুব দ্রুত পাওয়া যায়।
  - **Closed** — নির্দিষ্ট group (email list / Google Group)।
  - **Open** — যে কেউ join করতে পারে।
  - **Production** — **staged rollout** % দিয়ে, দরকারে halt।
- নতুন personal developer account-এর জন্য production-এর আগে closed test-এ নির্দিষ্ট সংখ্যক tester নির্দিষ্ট দিন রাখার নিয়ম আছে (এখন 12 tester, 14 দিন বলে জানি — Play Console-এ দেখে নিন)।
- **In-app updates (Play Core `app-update` library):**
  - **Flexible** — background-এ download, user পরে restart করে।
  - **Immediate** — full-screen, update না করলে app চলবে না। জরুরি security fix-এর জন্য।

**Answer (English):**
> "I use GitHub Actions. On every pull request, CI sets up JDK 17 and the Gradle cache, then runs lint, static analysis, unit tests and a debug build. On main, it also runs instrumented tests on an emulator or Firebase Test Lab. For a release, CI builds a signed AAB. The keystore and passwords come from CI secrets, never from the repo. Then Gradle Play Publisher or Fastlane uploads the bundle to the internal track with a service account. After testing, we promote to closed testing and then to production with a staged rollout. In the app I use the in-app updates API: flexible updates normally, and immediate updates only for critical fixes."

**Key words:** `GitHub Actions` · `service account` · `Gradle Play Publisher` · `Fastlane supply` · `internal track` · `staged rollout` · `in-app updates`

**Follow-up:**
- **Q:** How do you make CI builds faster?
  **A:** "I use the Gradle build cache and configuration cache, cache dependencies, split jobs so tests run in parallel, and only run slow emulator tests on main, not on every commit."
- **Q:** What is the risk of an immediate in-app update?
  **A:** "It blocks the user until they update, which is bad on a slow network. I use it only for serious problems, and I control it with remote config."

**ভুল করবেন না:** keystore বা service account JSON কখনো git-এ রাখবেন না, private repo হলেও না।

**আরও দেখুন:** [P13 · Static analysis](#p13) · [P6 · App signing](#p6) · [R15 · UI tests](#r15)

---

### <a id="p10"></a>P10. ★ How do you debug a production bug you cannot reproduce?

**প্রশ্নটা মানে:** Data দিয়ে, ধাপে ধাপে, শান্তভাবে সমস্যা ধরতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Users report a crash but it works on your phone. What do you do?" · "Walk me through how you handle a hard production issue."

**বুঝে নিন:**
**ধাপ ১ — Data জোগাড়:**
- Crashlytics / Play vitals stack trace, cluster, কতজন user।
- **Pattern খুঁজুন:** কোন app version, Android version, OEM, device model, RAM, locale, network। একটা Samsung model? Android 14-এর পর? শুধু process death-এর পরে?
- Custom keys আর log থেকে crash-এর আগের ঘটনা।
- `ApplicationExitInfo` — process কেন মরেছিল (low memory, ANR, native crash, user)।

**ধাপ ২ — পরিস্থিতি নকল করা:**
- **Process death:** "Don't keep activities" চালু, বা app background-এ রেখে `adb shell am kill <package>`, তারপর ফিরে আসুন।
- Rotation, fold/resize, dark mode, font scale বড়, RTL locale।
- ধীর বা বন্ধ network, airplane mode-এর মাঝে।
- Low memory device / emulator, পুরনো Android version।
- সেই device model পেতে: Firebase Test Lab, OEM-এর remote test lab, বা physical device।
- Release (minified) build-এ চালান — R8-এর বাগ debug-এ দেখা যায় না।

**ধাপ ৩ — আরো তথ্য দরকার হলে:**
- সন্দেহের জায়গায় non-fatal log আর custom key যোগ করে ছোট release, বা remote config দিয়ে detailed logging চালু।
- Feature flag দিয়ে সমস্যার feature বন্ধ রাখা যায়, fix আসা পর্যন্ত।

**ধাপ ৪ — ঠিক করা আর check করা:**
- কারণ বুঝে fix, সাথে **regression test** (unit বা instrumented)।
- Staged rollout-এ ছাড়ুন, cluster-এর সংখ্যা কমছে কিনা দেখুন।

- **Domain-এর উদাহরণ:** camera বা sensor bug প্রায়ই একটা OEM-এর HAL-এর আচরণে — যেমন একটা model নির্দিষ্ট resolution বা format সাপোর্ট করে না। তাই CameraX/Camera2-এর supported config query করুন, ধরে নেবেন না।

**Answer (English):**
> "First I collect data, not guesses. I read the stack trace and cluster in Crashlytics and Play vitals, and I look for a pattern: app version, Android version, device maker, memory, or a specific flow. Then I try to rebuild the same conditions: process death with 'Don't keep activities', rotation, slow network, low memory, and a minified release build. If I still cannot see it, I ship extra logging or non-fatal reports, often behind remote config, and I can turn the feature off with a flag. When I find the cause, I add a regression test and ship the fix with a staged rollout, then check that the cluster goes down."

**Key words:** `pattern` · `custom keys` · `process death` · `Don't keep activities` · `remote config` · `feature flag` · `regression test`

**Follow-up:**
- **Q:** The crash is only on one device model. What then?
  **A:** "It is often an OEM difference, like a camera HAL or a power-saving rule. I get that device or use a test lab, check what the device really supports, and add a safe fallback for it."
- **Q:** How do you test process death?
  **A:** "I put the app in the background, kill the process with `adb shell am kill`, and open it again from recents. The app should restore the screen with saved state, not crash or show empty data."

**ভুল করবেন না:** "আমার phone-এ চলে, তাই বাগ নেই" — data-র pattern না দেখে বন্ধ করবেন না।

**আরও দেখুন:** [P8 · Crash monitoring](#p8) · [C4 · Process death](#c4) · [P1 · ANR](#p1)

---

### <a id="p11"></a>P11. ★ What changed in recent Android versions (8 to 17)? What do minSdk, targetSdk and compileSdk mean?

**প্রশ্নটা মানে:** কোন version-এ app developer-এর জন্য কী গুরুত্বপূর্ণ বদল এসেছে, আর SDK তিনটার পার্থক্য পরিষ্কার জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What do you need to do when you raise targetSdk?" · "What is the Play target API requirement this year?"

**বুঝে নিন:**
**তিনটা SDK:**
| | মানে | কী হয় |
|---|---|---|
| `minSdk` | সবচেয়ে পুরনো যে Android-এ install হবে | এর নিচে Play দেখায় না। নতুন API ব্যবহারে `SDK_INT` check লাগে। |
| `compileSdk` | কোন SDK-র API দিয়ে compile করছেন | শুধু build-time। নতুন API আর lint warning দেখা যায়। Behavior বদলায় না। |
| `targetSdk` | কোন version-এর **behavior** আপনি test করে মেনে নিয়েছেন | System নতুন নিয়ম (edge-to-edge, predictive back...) শুধু তখনই চালু করে যখন targetSdk ≥ সেই version। |

- নিয়ম: `minSdk ≤ targetSdk ≤ compileSdk`। সাধারণত compileSdk = targetSdk = latest stable।
- অনেক AndroidX library এখন minSdk 23 চায় — আপনার minSdk ঠিক করতে এটা মাথায় রাখুন।
- **Play target API নিয়ম:** 31 Aug 2026 থেকে নতুন app আর update-কে **API 36 (Android 16)** target করতে হবে (Wear OS/Automotive আলাদা)। পুরনো app নতুন device-এ দেখা যেতে কমপক্ষে API 35 লাগে। পরের বছর API 37 হওয়ার কথা — Play Console-এ দেখে নিন।

**Version অনুযায়ী মূল পরিবর্তন:**

| Version (API) | App developer-এর জন্য যা গুরুত্বপূর্ণ |
|---|---|
| 8.0 / 8.1 (26/27) | Background execution limits (background service চালানো যায় না)। Manifest-এ implicit broadcast বেশিরভাগ বন্ধ। Notification channel mandatory। |
| 9 (28) | Background-এ camera, mic, continuous sensor (accelerometer, gyro) বন্ধ। Cleartext HTTP default-এ বন্ধ। Non-SDK (hidden) API সীমা। |
| 10 (29) | Scoped storage শুরু (opt-out ছিল)। `ACCESS_BACKGROUND_LOCATION` আলাদা। Background থেকে Activity শুরু বন্ধ। IMEI/serial-এর মতো স্থায়ী ID সীমিত। |
| 11 (30) | Scoped storage mandatory। Package visibility (`<queries>`)। One-time permission। Background location আলাদা করে চাইতে হয়। `ApplicationExitInfo`। |
| 12 (31/32) | Background থেকে foreground service শুরু প্রায় বন্ধ। `android:exported` mandatory। PendingIntent-এ `FLAG_IMMUTABLE`/`FLAG_MUTABLE`। `BLUETOOTH_SCAN/CONNECT/ADVERTISE`। Approximate location। 200 Hz-এর বেশি sensor-এ `HIGH_SAMPLING_RATE_SENSORS`। Mic/camera indicator ও toggle। SplashScreen API। Exact alarm permission। |
| 13 (33) | `POST_NOTIFICATIONS` runtime permission। `READ_MEDIA_IMAGES/VIDEO/AUDIO`। `NEARBY_WIFI_DEVICES`। Per-app language। |
| 14 (34) | Partial photo access (`READ_MEDIA_VISUAL_USER_SELECTED`)। Foreground service **type** mandatory + মিলিয়ে `FOREGROUND_SERVICE_*` permission। Runtime receiver-এ `RECEIVER_EXPORTED/NOT_EXPORTED`। `SCHEDULE_EXACT_ALARM` default denied। `USE_FULL_SCREEN_INTENT` সীমিত। Implicit intent শুধু exported component-এ। |
| 15 (35) | **Edge-to-edge mandatory**। `dataSync` FGS 24 ঘণ্টায় 6 ঘণ্টা। নতুন `mediaProcessing` type। `BOOT_COMPLETED` থেকে camera/mic/dataSync/mediaPlayback ইত্যাদি FGS শুরু করা যায় না। 16 KB page size device সাপোর্ট। |
| 16 (36) | **Predictive back** animation default, `onBackPressed()` call হয় না। Edge-to-edge opt-out বন্ধ। Large screen (≥600dp)-এ orientation/resizability/aspect ratio lock মানা হয় না (temporary opt-out ছিল)। Local network permission opt-in হিসেবে আসে। |
| 17 (37) | Large screen-এর opt-out বাদ (game ছাড়া)। **`ACCESS_LOCAL_NETWORK`** runtime permission mandatory — LAN device খোঁজা/connect করতে (`NsdManager` resolve-এর address-এ লাগে না)। Certificate transparency default চালু। Target 37 হলে OTP-ওয়ালা SMS বেশিরভাগ app ৩ ঘণ্টা দেরিতে পায় — SMS Retriever / User Consent API ব্যবহার করুন। Lock-free MessageQueue। Reflection দিয়ে `static final` field বদলানো যায় না। বাকি বিষয় Android 17 behavior-changes page দেখুন। |

**16 KB page size:**
- নতুন device-এ memory page 4 KB-এর বদলে 16 KB হতে পারে। এতে app launch আর system performance ভালো হয়।
- 1 Nov 2025 থেকে Play-তে Android 15+ target করা নতুন app আর update, যাতে native code (`.so`) আছে, সেগুলো 16 KB সাপোর্ট করতে হবে। Target নিয়ম এখন API 36, তাই আসলে native code-ওয়ালা সব নতুন release-এ এটা লাগে।
- ঠিক করতে: নতুন AGP (uncompressed `.so` 16 KB align করে) আর নতুন NDK দিয়ে rebuild, third-party `.so` library update। Native code-এ page size hardcode (4096) থাকলে `sysconf(_SC_PAGESIZE)` ব্যবহার। Android Studio-র APK Analyzer alignment সমস্যা দেখায়।
- Flutter app-ও native code সহ আসে — Flutter, AGP, NDK update করে rebuild করতে হয়।
- শুধু Kotlin/Java app (কোনো `.so` নেই) হলে কিছু করতে হয় না।

**Answer (English):**
> "`minSdk` is the oldest Android version that can install the app. `compileSdk` is the SDK I build against; it only gives me new APIs and warnings. `targetSdk` says which Android behavior I have tested, and the system turns on new rules only when targetSdk reaches that version. Since August 2026, Play needs new apps and updates to target API 36. The big changes were: background limits in 8, background sensor and camera limits in 9, scoped storage and package visibility in 11, foreground service rules in 12 and 14, notification permission in 13, edge-to-edge in 15, predictive back and large-screen rules in 16, and local network permission in 17. Apps with native code must also support 16 KB pages."

**Key words:** `minSdk` · `compileSdk` · `targetSdk` · `target API requirement` · `behavior changes` · `16 KB page size` · `ACCESS_LOCAL_NETWORK`

**Follow-up:**
- **Q:** How do you raise targetSdk safely?
  **A:** "I read the behavior changes page for that version, list what touches our app, and fix it behind version checks. Then I test on a device with that Android version, and roll out slowly."
- **Q:** Our IP camera app finds cameras on Wi-Fi. What changes with Android 17?
  **A:** "If we target API 37, we must declare and ask for `ACCESS_LOCAL_NETWORK` before scanning or connecting to LAN devices, like ONVIF discovery or RTSP. I add a clear permission screen and handle denial."
- **Q:** Why does 16 KB matter if I don't write C++?
  **A:** "Many libraries ship `.so` files, like video, camera, ML or database libraries. I check the APK in the analyzer and update any library that is not aligned."

**ভুল করবেন না:** compileSdk বাড়ালে behavior বদলায় বলবেন না — behavior বদলায় **targetSdk** বাড়ালে।

**আরও দেখুন:** [U13 · Edge-to-edge](#u13) · [C7 · Foreground services](#c7) · [V7 · LAN camera discovery](#v7)

---

### <a id="p12"></a>P12. ◆ Explain Gradle basics: build types, flavors, version catalogs, KSP vs kapt, and build speed.

**প্রশ্নটা মানে:** Android build system দিয়ে কয়েকটা environment আর বড় project সামলাতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you have dev, staging and prod builds?" · "Why is KSP better than kapt?"

**বুঝে নিন:**
- **Build type** — কীভাবে build হবে: `debug` (debuggable, R8 নেই), `release` (R8, signing)। নিজেও বানানো যায়, যেমন `benchmark`।
- **Product flavor** — কোন version-এর app: `dev`/`staging`/`prod`, বা `free`/`paid`। `flavorDimensions` দিয়ে ভাগ।
- **Variant** = flavor × build type। যেমন `prodRelease`, `devDebug`। প্রতিটার আলাদা source set (`src/dev/`)।
- `applicationIdSuffix` দিলে একই phone-এ dev আর prod দুটোই install হয়।
- `buildConfigField` দিয়ে base URL ইত্যাদি। AGP 8 থেকে `buildFeatures { buildConfig = true }` চালু করতে হয়।

```kotlin
android {
    flavorDimensions += "env"
    productFlavors {
        create("dev") {
            dimension = "env"
            applicationIdSuffix = ".dev"
            buildConfigField("String", "API_URL", "\"https://dev.example.com\"")
        }
        create("prod") {
            dimension = "env"
            buildConfigField("String", "API_URL", "\"https://api.example.com\"")
        }
    }
}
```

- **Version catalog** — `gradle/libs.versions.toml`। সব dependency আর version এক জায়গায়। Multi-module-এ সব module একই version পায়। Code-এ `libs.androidx.room.runtime`।

```toml
[versions]
room = "2.8.0"          # উদাহরণ মাত্র
[libraries]
androidx-room-runtime = { module = "androidx.room:room-runtime", version.ref = "room" }
androidx-room-compiler = { module = "androidx.room:room-compiler", version.ref = "room" }
[plugins]
ksp = { id = "com.google.devtools.ksp", version = "2.3.0" }   # উদাহরণ মাত্র
```

- **KSP vs kapt:**
  - **kapt** — Java annotation processor চালাতে Kotlin থেকে Java stub বানায়। এই stub বানানো ধীর।
  - **KSP** — সরাসরি Kotlin code পড়ে, stub নেই। দ্রুত। Room, Hilt, Moshi KSP সাপোর্ট করে।
  - **AGP 9-এ built-in Kotlin** — আলাদা `org.jetbrains.kotlin.android` plugin লাগে না। পুরনো `kotlin-kapt` plugin এর সাথে চলে না। এখনো kapt লাগলে `com.android.legacy-kapt` আছে (বা সাময়িকভাবে `android.builtInKotlin=false` দিয়ে opt-out), কিন্তু লক্ষ্য KSP-তে যাওয়া।
- **Build speed:**
  - **Build cache** (`org.gradle.caching=true`) — আগের task output আবার ব্যবহার, CI-তে remote cache।
  - **Configuration cache** (`org.gradle.configuration-cache=true`) — configuration phase-এর ফল cache করে। Gradle এখন এটা ব্যবহার করতে বলে।
  - Modularization — বদলানো module-ই শুধু আবার build।
  - kapt সরানো, অপ্রয়োজনীয় plugin সরানো, non-transitive R class (AGP 8-এ default)।
  - **Build Analyzer** (Android Studio) — কোন task/plugin ধীর দেখায়।
  - Multi-module-এ **convention plugin** (`build-logic`) দিয়ে একই config বারবার না লেখা।

**Answer (English):**
> "Build types say how to build, like debug and release, and product flavors say which version of the app, like dev and prod. Together they make variants, such as `prodRelease`. I use `applicationIdSuffix` so dev and prod can sit on the same phone, and `buildConfigField` for things like the API URL. I keep all versions in a version catalog, `libs.versions.toml`, so every module uses the same versions. I use KSP, not kapt, because kapt builds Java stubs and is slow; Room and Hilt both support KSP. With AGP 9, the old kapt plugin does not work anyway. For speed, I turn on the build cache and configuration cache, split the app into modules, and check Build Analyzer."

**Key words:** `build type` · `product flavor` · `build variant` · `libs.versions.toml` · `KSP` · `kapt` · `configuration cache` · `build cache`

**Follow-up:**
- **Q:** Where do you keep secrets like API keys in the build?
  **A:** "Not in git. I read them from `local.properties` or CI environment variables into `buildConfigField`. But anything in the APK can be read, so real secrets stay on the server."
- **Q:** What is a convention plugin?
  **A:** "It is a small Gradle plugin in a `build-logic` folder that holds shared config, like compileSdk and Compose setup. Each module applies it, so I don't copy the same block into every module."

**ভুল করবেন না:** নতুন project-এ kapt-কে default বলবেন না — এখন KSP, আর AGP 9-এর built-in Kotlin-এ পুরনো `kotlin-kapt` plugin চলে না।

**আরও দেখুন:** [P13 · Static analysis](#p13) · [R6 · Modules](#r6) · [P9 · CI/CD](#p9)

---

### <a id="p13"></a>P13. ◆ Which static analysis tools do you use? (Android Lint, detekt, ktlint)

**প্রশ্নটা মানে:** Code চালানোর আগেই bug আর style সমস্যা ধরতে কোন tool ব্যবহার করেন, আর team-এ কীভাবে চালু রাখেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you keep code quality high in a team?" · "What is the difference between Lint and detekt?"

**বুঝে নিন:**

| Tool | কী ধরে | উদাহরণ |
|---|---|---|
| **Android Lint** (AGP-র সাথে আসে) | Android-নির্দিষ্ট সমস্যা | নতুন API পুরনো `minSdk`-এ call (`NewApi`), permission check নেই, hardcoded string, ব্যবহার না হওয়া resource, manifest ভুল, accessibility |
| **detekt** | Kotlin code smell আর জটিলতা | খুব লম্বা function, অনেক parameter, `GlobalScope`, খালি catch, magic number |
| **ktlint** | Kotlin style আর format | indent, import order, spacing — অনেক সময় নিজে ঠিকও করে দেয় (`ktlintFormat`) |

- **Lint config:** `lint { }` block-এ `warningsAsErrors`, `abortOnError`, `checkDependencies = true` (multi-module-এ)।
- **Baseline:** পুরনো project-এ শুরুতেই হাজার warning থাকে। `baseline = file("lint-baseline.xml")` দিলে পুরনো সমস্যা চুপ থাকে, শুধু **নতুন** সমস্যায় build fail হয়। detekt-এরও baseline আছে। তারপর ধীরে ধীরে পুরনোগুলো ঠিক করুন।
- **Custom rule:** team-এর নিয়ম (যেমন "ViewModel-এ `Context` নয়") নিজে Lint বা detekt rule হিসেবে লেখা যায়। Compose-এর জন্য আলাদা lint rule set-ও আছে (open source)।
- **কোথায় চালাবেন:**
  - IDE-তে লেখার সময় (Lint আর ktlint plugin)।
  - Git pre-commit hook-এ format check (দ্রুত, ছোট)।
  - CI-তে প্রতিটা PR-এ — fail হলে merge হবে না। Report (SARIF/HTML) PR-এ দেখান।
- Static analysis test-এর বদলে নয়। এটা সস্তা, দ্রুত ধরার প্রথম ধাপ।
- **Flutter mapping:** `flutter analyze` + `analysis_options.yaml` (lints package) = এখানে Lint + detekt config। `dart format` = ktlint।

```kotlin
// app/build.gradle.kts
android {
    lint {
        warningsAsErrors = true
        abortOnError = true
        baseline = file("lint-baseline.xml")
    }
}
```

**Answer (English):**
> "I use three tools. Android Lint comes with the Android Gradle plugin and finds Android problems, like calling a new API on an old minSdk, missing permission checks, or hardcoded strings. detekt finds Kotlin code smells, like very long functions or empty catch blocks. ktlint checks and fixes formatting, so we never argue about style in review. All three run on every pull request in CI, and a failure blocks the merge. On an old project I start with a baseline file, so only new problems fail the build, and we fix the old ones step by step. These tools don't replace tests, but they catch many bugs very cheaply."

**Key words:** `Android Lint` · `detekt` · `ktlint` · `baseline` · `warningsAsErrors` · `NewApi` · `custom lint rule` · `CI gate`

**Follow-up:**
- **Q:** Lint shows a `NewApi` error. What does it mean?
  **A:** "I call an API that does not exist on my minSdk. I add a `Build.VERSION.SDK_INT` check, or use an AndroidX compat helper that does the check for me."
- **Q:** The team says the rules are too strict. What do you do?
  **A:** "We agree on the rule set together and turn off rules that only make noise. A rule that everyone ignores is worse than no rule."

**ভুল করবেন না:** Warning চুপ করাতে সব জায়গায় `@Suppress` দেবেন না — কেন suppress করছেন সেটা এক লাইনে লিখুন, আর শুধু যেখানে সত্যিই দরকার।

**আরও দেখুন:** [P9 · CI/CD](#p9) · [P12 · Gradle](#p12) · [S14 · Security testing](#s14)

---


## <a id="part-5"></a>Part 5 — Architecture, data, network আর testing

এই part-এ senior interview-এর সবচেয়ে বড় অংশ। Interviewer দেখতে চায় আপনি একটা app-কে layer-এ ভাগ করতে পারেন কিনা, data কোথা থেকে আসে আর কোথায় থাকে সেটা পরিষ্কার বলতে পারেন কিনা, আর code-টা test করা যায় কিনা।
Camera / IoT / sensor-এর কাজে network ভাঙে, device offline হয়, data দেরিতে আসে। তাই offline-first, error handling আর real-time data এখানে খুব জরুরি।

### আগে বুঝুন — Android app-এর architecture, data আর testing

**বড় ছবি (ধাপে ধাপে):**

1. User screen-এ কিছু করে (tap, type)। এটা একটা **event**।
2. Event যায় **ViewModel**-এ। ViewModel ঠিক করে কী করতে হবে।
3. ViewModel দরকার হলে **use case** (optional) বা সরাসরি **Repository**-কে ডাকে।
4. Repository data আনে **data source** থেকে: Room (local DB), DataStore (ছোট settings), Retrofit/OkHttp (network)।
5. Data আবার উপরে ওঠে `Flow` হয়ে। ViewModel সেটাকে একটা **`UiState`** বানায়, `StateFlow`-এ রাখে।
6. Compose screen `collectAsStateWithLifecycle()` দিয়ে state পড়ে আর draw করে।
7. **Hilt** সব object তৈরি করে আর জোড়া লাগায়। Test-এ Hilt বা constructor দিয়ে fake বসানো যায়।

```
 Compose UI ──event──▶ ViewModel ──▶ (UseCase) ──▶ Repository ──▶ Room  (source of truth)
     ▲                     │                           │      └──▶ Retrofit/OkHttp (sync)
     └── StateFlow<UiState>◀──────── Flow ◀────────────┘      └──▶ DataStore (settings)
```

**যে ৮টা idea-র উপর সব দাঁড়িয়ে আছে:**

- **Unidirectional data flow (UDF):** state নিচে নামে, event উপরে ওঠে। UI নিজে state বদলায় না।
- **Single source of truth (SSOT):** একটা data-র একটাই মালিক। সাধারণত Room। Network data আগে DB-তে লেখা হয়, UI DB পড়ে।
- **Layer:** UI layer আর data layer লাগবেই। Domain layer (use case) optional — Google-এর official guide-ও এটাই বলে।
- **Dependency rule:** উপরের layer নিচেরটা জানে। নিচের layer UI-কে চেনে না। Domain-এ Android class থাকে না।
- **Main-safe:** Room আর Retrofit-এর `suspend` function নিজেই background-এ চলে। ভারী CPU কাজ `Dispatchers.Default`-এ।
- **Error একটা state:** error চুপচাপ গিলে ফেলা যাবে না। `UiState`-এ দেখাতে হবে, log করতে হবে।
- **DI:** class নিজে dependency বানায় না, constructor-এ পায়। এতে test-এ fake দেওয়া যায়।
- **Test pyramid:** অনেক JVM unit test (ViewModel, repository, mapper), কম UI test, খুব কম end-to-end test।

**২০২৬-এর নতুন কিছু জিনিস মাথায় রাখুন:**
- Annotation processing-এ **KSP**, kapt না।
- **Room 3.0** stable হয়েছে July 2026-এ (`androidx.room3` package, শুধু KSP, DAO হয় `suspend` নয়তো `Flow`)। অনেক app এখনো Room 2.x-এ — দুটোর annotation প্রায় এক।
- Compose-এ `hiltViewModel()` এখন `androidx.hilt:hilt-lifecycle-viewmodel-compose` artifact-এ।
- LiveData প্রথম পছন্দ না; `StateFlow` আর `Flow`।

**Flutter থেকে এলে কী আলাদা:**
- Riverpod/Bloc-এর জায়গায় **ViewModel + StateFlow**। ViewModel rotation-এ বেঁচে থাকে — Flutter-এ এই সমস্যা চোখে পড়ে না, কারণ Flutter template-এর manifest-এ `android:configChanges` দেওয়া থাকে, তাই rotation-এ `FlutterActivity` recreate হয় না।
- `get_it` বা Riverpod provider-এর জায়গায় **Hilt** — graph compile time-এ check হয়।
- `drift`/`sqflite` → **Room**, `shared_preferences` → **DataStore**, `dio` interceptor → **OkHttp interceptor**, `mocktail` → **MockK**।
- Flutter-এ Dart single-threaded + isolate। Android-এ coroutine-গুলো একই memory share করে, তাই thread safety নিজে ভাবতে হয়।

---

### <a id="r1"></a>R1. ★ What goes in a ViewModel, and why does it survive screen rotation?

**প্রশ্নটা মানে:** ViewModel-এর দায়িত্ব কী, আর rotation-এ ভেতরে আসলে কী হয় — এটা আপনি জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Explain MVVM on Android." · "How does a ViewModel keep its data after a configuration change?"

**বুঝে নিন:**

ViewModel-এ যা থাকে:
- Screen-এর **UI state** (`StateFlow<UiState>`)।
- User event handle করা (`onRefreshClick()`, `onQueryChange()`)।
- `viewModelScope`-এ repository / use case ডাকা।
- UI-র জন্য data সাজানো (format, filter)।

ViewModel-এ যা থাকে না:
- `Activity`, `Fragment`, `View`, Activity-র `Context` — leak হয়। ViewModel Activity-র চেয়ে বেশিদিন বাঁচে।
- Navigation বা Toast সরাসরি দেখানো — এগুলো state বা event হিসেবে UI-কে দিন।

**Rotation-এ কেন বাঁচে:**
- `ComponentActivity` হলো `ViewModelStoreOwner`। তার একটা **`ViewModelStore`** আছে — key → ViewModel-এর একটা map।
- Rotation-এ পুরনো Activity destroy হয়। কিন্তু system জানে এটা configuration change (`isChangingConfigurations == true`)।
- তখন `ViewModelStore`-টা non-configuration instance হিসেবে রেখে দেওয়া হয় (`onRetainNonConfigurationInstance`)। নতুন Activity একই store পায়, তাই একই ViewModel পায়।
- Activity সত্যি শেষ হলে (back, `finish()`) store `clear()` হয় → `onCleared()` → `viewModelScope` cancel।

**কোথায় বাঁচে না:** **process death**। System background-এ app মেরে ফেললে ViewModel যায়। তখন:
- ছোট জিনিস (search text, selected id) → **`SavedStateHandle`** (Bundle-এ যায়, ছোট রাখুন)।
- বড় data → Room থেকে আবার load।

```kotlin
@HiltViewModel
class CamerasViewModel @Inject constructor(
    repo: CameraRepository,
    private val savedState: SavedStateHandle,
) : ViewModel() {
    private val query = savedState.getStateFlow("q", "")

    val uiState: StateFlow<CamerasUiState> = query
        .flatMapLatest { repo.observeCameras(it) }
        .map<List<Camera>, CamerasUiState> { CamerasUiState.Content(it) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), CamerasUiState.Loading)

    fun onQueryChange(q: String) { savedState["q"] = q }
}
```

- `WhileSubscribed(5_000)`: UI না দেখলে ৫ সেকেন্ড পর upstream বন্ধ। Rotation ৫ সেকেন্ডের কম, তাই rotation-এ আবার load হয় না।
- Flutter-এ এর সরাসরি মিল নেই। Flutter app-এর manifest-এ `configChanges` থাকে বলে rotation-এ Activity recreate হয় না, Dart state engine-এ থাকে। Native Android-এ default হলো recreate।

**Answer (English):**
> "The ViewModel holds the screen state and handles user events. It calls the repository in viewModelScope and exposes one StateFlow of UI state. It must not hold an Activity, a View, or an Activity context, because it lives longer than them. It survives rotation because the Activity is a ViewModelStoreOwner. On a configuration change, the system keeps the ViewModelStore and gives it to the new Activity. When the Activity really finishes, the store is cleared and onCleared runs. But it does not survive process death. For that I put small values in SavedStateHandle and reload big data from Room."

**Key words:** `ViewModelStore` · `ViewModelStoreOwner` · `viewModelScope` · `SavedStateHandle` · `process death` · `stateIn`

**Follow-up:**
- **Q:** Why not pass a Context into the ViewModel?
  **A:** "An Activity context dies on rotation, but the ViewModel does not. So the ViewModel would leak the old Activity. If I need app-level things, I inject a class that uses the application context."
- **Q:** What happens to running coroutines when the user leaves the screen?
  **A:** "When the ViewModel is cleared, viewModelScope is cancelled, so its coroutines stop. Work that must finish even if the user leaves, like an upload, goes to WorkManager."
- **Q:** Why WhileSubscribed(5000)?
  **A:** "It keeps the flow alive for a short time with no collectors. A rotation is shorter than five seconds, so we do not restart the work. If the app goes to the background, it stops after five seconds and saves resources."

**ভুল করবেন না:** "ViewModel process death-এও বাঁচে" বলবেন না — বাঁচে না, এজন্যই `SavedStateHandle`।

**আরও দেখুন:** [C4 · Config change vs process death](#c4) · [K13 · StateFlow & stateIn](#k13) · [R14 · ViewModel test](#r14)

---

### <a id="r2"></a>R2. ★ What is MVI or unidirectional data flow? MVVM or MVI — which do you choose?

**প্রশ্নটা মানে:** State management-এর design আপনি বুঝে বেছে নেন কিনা, নাকি শুধু নাম জানেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What is UDF?" · "How do you handle one-time events like navigation or a snackbar?"

**বুঝে নিন:**

**UDF:** state এক দিকে নামে (ViewModel → UI), event এক দিকে ওঠে (UI → ViewModel)। UI নিজে state বদলায় না।

**MVI** হলো UDF-এর কড়া রূপ:
- **Intent / Action:** user কী চাইল (`Refresh`, `Select(id)`)। একটা sealed type।
- **Reducer:** `(oldState, result) -> newState`। Pure function, তাই test সহজ।
- **State:** screen-এর পুরো state একটা immutable data class-এ।
- **Side effect:** navigation, snackbar — এক বারের কাজ।

| | MVVM (Google-style) | MVI |
|---|---|---|
| Input | আলাদা function (`onRefresh()`) | একটা `onAction(Action)` |
| State | সাধারণত একটা `UiState`, কখনো কয়েকটা flow | সবসময় একটা state |
| State বদল | ViewModel-এর ভেতরে `update {}` | reducer দিয়ে |
| Boilerplate | কম | বেশি |
| কোথায় ভালো | সাধারণ screen | জটিল screen: form, video player, camera control |

**One-time event:**
- পুরনো উপায়: `Channel` / `SharedFlow`। ঝুঁকি — UI collect না করলে event হারাতে পারে।
- Google-এর guide বলে: event-কে state হিসেবে রাখুন (যেমন `userMessage: String?`), UI দেখানোর পর ViewModel-কে জানায় "consumed"।

**আমার পছন্দ:** MVVM + UDF + প্রতি screen-এ একটা `UiState`। এটা আসলে "MVI-lite"। খুব জটিল screen-এ পুরো reducer pattern।

Flutter-এ Bloc প্রায় MVI (event → bloc → state)। Riverpod `Notifier` প্রায় MVVM।

```kotlin
data class PlayerUiState(
    val isPlaying: Boolean = false,
    val isMuted: Boolean = false,
    val error: String? = null,
)
private val _state = MutableStateFlow(PlayerUiState())
val state = _state.asStateFlow()
fun onMuteClick() = _state.update { it.copy(isMuted = !it.isMuted) }
```

**Answer (English):**
> "Unidirectional data flow means state goes down to the UI and events go up to the ViewModel. The UI never changes state by itself. MVI is a strict form of this: one action type, one state object, and a reducer that makes the new state. My default is MVVM with UDF and one UiState per screen. It is simple and easy to test. For a complex screen, like a video player with many controls, I use a full reducer, because it makes every state change clear. The trade-off is more code. For one-time events, I prefer to keep them in state and mark them as handled, so they are not lost."

**Key words:** `unidirectional data flow` · `single UiState` · `reducer` · `immutable state` · `one-time event`

**Follow-up:**
- **Q:** Why is a Channel for events risky?
  **A:** "If the UI is not collecting at that moment, for example during rotation, the event can be lost or handled late. Keeping it in state is safer."
- **Q:** Why one UiState instead of many flows?
  **A:** "One state object cannot be half-updated. The UI always sees a valid combination, and tests can check one value."

**ভুল করবেন না:** "MVI সবসময় ভালো" বলবেন না — boilerplate-এর দাম আছে, কোথায় লাগে সেটা বলুন।

**আরও দেখুন:** [K15 · One-time events](#k15) · [K24 · Sealed state](#k24) · [U9 · Compose + ViewModel](#u9)

---

### <a id="r3"></a>R3. ★ Explain Clean Architecture layers. When is a use case class worth it?

**প্রশ্নটা মানে:** Layer কেন ভাগ করেন, আর অপ্রয়োজনীয় layer যোগ না করার judgment আছে কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is Google's recommended app architecture?" · "Do you always write use cases?"

**বুঝে নিন:**

**Google-এর recommended architecture (developer.android.com):**
- **UI layer** — Compose/View + ViewModel + UiState। লাগবেই।
- **Domain layer** — use case। **Optional।** দরকার হলে।
- **Data layer** — Repository + data source (Room, DataStore, API)। লাগবেই।

**Clean Architecture-এর মূল rule:** dependency ভেতরের দিকে। Domain pure Kotlin, Android জানে না। Data layer domain-এর interface implement করে।

```
ui ──▶ domain ◀── data
(Compose, VM)  (UseCase, model)  (RepositoryImpl, Room, Retrofit)
```

**Use case কখন লিখবেন:**
- এতে আসল **business rule** আছে (যেমন "camera offline ৫ মিনিটের বেশি হলে alert")।
- **দুই বা বেশি repository** মিলাতে হয়।
- **কয়েকটা ViewModel** একই logic ব্যবহার করে।

**কখন লিখবেন না:**
- শুধু `repo.getX()` forward করে — এটা খালি layer। পড়া কঠিন হয়, লাভ নেই।

**Model আলাদা রাখা:** `CameraDto` (network) → `CameraEntity` (Room) → `Camera` (domain) → UI-তে দরকার হলে `CameraUi`। Mapper pure function, সহজে test হয়। ছোট app-এ সব model আলাদা রাখা বাড়াবাড়ি হতে পারে।

**Package:** feature অনুযায়ী ভাগ করুন (`feature/cameras/`, `feature/alerts/`), শুধু layer অনুযায়ী না।

```kotlin
class GetOfflineCamerasUseCase @Inject constructor(
    private val cameras: CameraRepository,
    private val clock: Clock,
) {
    operator fun invoke(limit: Duration): Flow<List<Camera>> =
        cameras.observeAll().map { list ->
            list.filter { clock.now() - it.lastSeen > limit }
        }
}
```
(এখানে `Clock` = `kotlin.time.Clock`, `lastSeen` = `Instant` ধরে নেওয়া হয়েছে।)

**Answer (English):**
> "Google's guide has a UI layer, a data layer, and an optional domain layer. The rule is that dependencies point inward: the domain does not know Android, and the data layer hides where data comes from. I add a use case only when it is worth it: when it has a real business rule, combines two or more repositories, or is shared by several ViewModels. A use case that only forwards one call adds a layer with no value, so I skip it. I also keep separate models for network, database, and domain when they really differ. This keeps each layer easy to test and easy to change."

**Key words:** `UI layer` · `domain layer (optional)` · `data layer` · `dependency rule` · `use case` · `mapper`

**Follow-up:**
- **Q:** Where does the domain model live in a multi-module app?
  **A:** "In a small core model or domain module that has no Android dependency. Feature and data modules both depend on it."
- **Q:** Is Clean Architecture over-engineering for small apps?
  **A:** "It can be. For a small app I keep UI and data layers only and add domain logic when a real rule appears."
- **Q:** Why inject a Clock?
  **A:** "Time is an input. With a fake clock, my test can check the five-minute rule without waiting."

**ভুল করবেন না:** "প্রতিটা repository call-এর জন্য use case লিখি" বলবেন না — এটা senior-এর উত্তর না।

**আরও দেখুন:** [R4 · Repository](#r4) · [R6 · Modules](#r6) · [R18 · SOLID](#r18)

---

### <a id="r4"></a>R4. ★ Explain the Repository pattern, single source of truth, and offline-first.

**প্রশ্নটা মানে:** Network আর DB একসাথে কীভাবে সামলান, offline-এ app কীভাবে চলে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you make an app work offline?" · "How do you sync local and remote data?"

**বুঝে নিন:**

**Repository:** data layer-এর public দরজা। বাইরের কেউ জানে না data Room, network না cache থেকে এলো।

**Single source of truth (SSOT):**
- একটা data-র মালিক একটাই। সাধারণত **Room**।
- Network থেকে data এলে **আগে DB-তে লেখা হয়**। UI সবসময় DB-র `Flow` পড়ে।
- লাভ: সব screen একই data দেখে। Offline-এ শেষ data দেখায়। App restart-এও থাকে।

**Read path (offline-first):**
1. UI `observeCameras()` collect করে → Room থেকে সাথে সাথে পুরনো data।
2. পাশাপাশি `refresh()` network থেকে আনে → DB update → Flow নিজেই নতুন data দেয়।
3. Network fail করলে পুরনো data থাকে, সাথে error message।

**Write path:**
1. Local DB-তে লিখুন, সাথে একটা flag (`syncState = PENDING`)। UI সাথে সাথে বদলায়।
2. **WorkManager** (network constraint সহ) pending row server-এ পাঠায়। সফল হলে `SYNCED`।
3. Conflict: server version / `updatedAt` দেখে ঠিক করুন — last-write-wins নাকি server-wins। এটা business-এর সিদ্ধান্ত, আগে ঠিক করে নিন।

```kotlin
class CameraRepository @Inject constructor(
    private val dao: CameraDao,
    private val api: CameraApi,
) {
    fun observeCameras(query: String): Flow<List<Camera>> =
        dao.observeByName("%$query%").map { rows -> rows.map { it.toDomain() } }

    suspend fun refresh() {
        val remote = api.getCameras()          // suspend, main-safe
        dao.upsertAll(remote.map { it.toEntity() })
    }
}
```

Flutter-এ `drift` + `StreamBuilder` দিয়ে ঠিক একই pattern হয়।

**Answer (English):**
> "A repository is the only door to the data of one feature. The rest of the app does not know if data comes from the network or the database. I make the database the single source of truth. Network data is written to Room first, and the UI only observes Room through a Flow. So every screen shows the same data, and the app still works offline with the last data. For writes, I save locally with a pending flag and let WorkManager sync it when the network is back. The hard part is conflicts, so I agree the rule with the backend early, for example by using a version or updatedAt field."

**Key words:** `single source of truth` · `offline-first` · `pending sync` · `WorkManager` · `conflict resolution`

**Follow-up:**
- **Q:** Why not show network data directly and cache it later?
  **A:** "Then two sources can show different data, and offline the screen is empty. With the database as the source, the UI has one simple path."
- **Q:** How do you avoid refreshing too often?
  **A:** "I store the last fetch time and only refresh after a set time, or when the user pulls to refresh."

**ভুল করবেন না:** Repository-কে `Activity` বা ViewModel-এর scope-এ বানাবেন না — সাধারণত `@Singleton`, নইলে cache আর sync ভাগ হয়ে যায়।

**আরও দেখুন:** [D2 · Offline-first design](#d2) · [R7 · Room](#r7) · [C10 · Background work](#c10)

---

### <a id="r5"></a>R5. ★ How does dependency injection work with Hilt?

**প্রশ্নটা মানে:** Hilt-এর annotation আর component/scope বোঝেন কিনা, আর DI কেন দরকার।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between @Provides and @Binds?" · "Hilt or Koin — which one and why?"

**বুঝে নিন:**

**মূল annotation:**
| Annotation | কাজ |
|---|---|
| `@HiltAndroidApp` | `Application` class-এ। Hilt-এর root component তৈরি করে। |
| `@AndroidEntryPoint` | Activity, Fragment, Service, View, BroadcastReceiver-এ inject করতে দেয়। |
| `@HiltViewModel` + `@Inject constructor` | ViewModel-এ inject। Compose-এ `hiltViewModel()`। |
| `@Inject constructor` | Hilt জানে কীভাবে class বানাতে হয়। |
| `@Module` + `@InstallIn(X::class)` | যেসব class নিজে বানাতে পারে না (interface, third-party)। |
| `@Provides` | function body-তে object বানিয়ে দেন (Retrofit, Room)। |
| `@Binds` | abstract function: "এই interface চাইলে এই impl দাও"। কম generated code। |
| `@Qualifier` | একই type-এর দুটো আলাদা object (যেমন দুটো `OkHttpClient`)। |

**Component আর scope:**
| Component | Scope | কতদিন বাঁচে |
|---|---|---|
| `SingletonComponent` | `@Singleton` | পুরো app |
| `ActivityRetainedComponent` | `@ActivityRetainedScoped` | rotation পার হয় |
| `ViewModelComponent` | `@ViewModelScoped` | একটা ViewModel |
| `ActivityComponent` | `@ActivityScoped` | একটা Activity |
| `FragmentComponent` / `ViewComponent` / `ServiceComponent` | নিজ নিজ scope | ঐ object |

- Scope না দিলে প্রতি inject-এ **নতুন object**। Scope দিন শুধু যখন state share করতে হয় (DB, OkHttpClient)।
- Hilt চলে **KSP**-তে (kapt না)। Graph compile time-এ check হয় — missing binding হলে build fail।
- Compose-এ `hiltViewModel()` এখন `androidx.hilt:hilt-lifecycle-viewmodel-compose`-এ; পুরনো `hilt-navigation-compose`-এরটা deprecated।
- Test: `@HiltAndroidTest`, `@TestInstallIn` দিয়ে real module বদলে fake module।

```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class DataModule {
    @Binds abstract fun cameraRepo(impl: OfflineFirstCameraRepository): CameraRepository

    companion object {
        @Provides @Singleton
        fun db(@ApplicationContext ctx: Context): AppDatabase =
            Room.databaseBuilder(ctx, AppDatabase::class.java, "app.db").build()
    }
}
```

**Hilt vs Koin:**
- Hilt: Dagger-এর উপর, compile-time, Android lifecycle-এর সাথে বাঁধা, Google-এর official।
- Koin: Kotlin DSL, runtime-এ resolve, setup সহজ, **KMP** সাপোর্ট করে। Missing dependency runtime-এ ধরা পড়ে (Koin-এর annotation/compile-check option আছে — version দেখে নিন)।
- আমার পছন্দ: Android-only app → Hilt। KMP shared code → Koin।

**Answer (English):**
> "Hilt builds objects for me and gives each class its dependencies through the constructor. I mark the Application with HiltAndroidApp, Android classes with AndroidEntryPoint, and ViewModels with HiltViewModel. For interfaces I use Binds, because it is just a mapping and makes less code. For third-party objects like Retrofit or Room I use Provides. Each object lives in a component, like SingletonComponent or ViewModelComponent, and I add a scope only when the object must be shared. The big plus is that Hilt checks the graph at compile time, so a missing binding fails the build, not the app. For a Kotlin Multiplatform module, I would pick Koin instead."

**Key words:** `@HiltAndroidApp` · `@AndroidEntryPoint` · `@Binds vs @Provides` · `SingletonComponent` · `scope` · `KSP` · `compile-time graph`

**Follow-up:**
- **Q:** What happens if you forget a scope on the database provider?
  **A:** "Hilt makes a new database object for every inject. That wastes memory and can break Room's change tracking between instances. So the database must be a Singleton."
- **Q:** How do you inject into a class Hilt does not create, like a ContentProvider?
  **A:** "I use an EntryPoint interface and get it with EntryPointAccessors from the application context."
- **Q:** How do you swap a module in tests?
  **A:** "I use TestInstallIn to replace the real module with a fake one for all tests, or UninstallModules for one test class."

**ভুল করবেন না:** "সব কিছু `@Singleton` করি" বলবেন না — অপ্রয়োজনীয় singleton memory ধরে রাখে আর hidden shared state তৈরি করে।

**আরও দেখুন:** [R14 · ViewModel test](#r14) · [R17 · Singletons](#r17)

---

### <a id="r6"></a>R6. ◆ How do you split an app into modules?

**প্রশ্নটা মানে:** বড় codebase-এ build speed আর team কাজের জন্য module design পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What are convention plugins?" · "What is the difference between api and implementation in Gradle?"

**বুঝে নিন:**

**সাধারণ shape (Now in Android sample-এর মতো):**
```
:app                      → সব জোড়া লাগায়, navigation graph
:feature:cameras          → screen + ViewModel
:feature:alerts
:core:data                → repository
:core:database            → Room
:core:network             → Retrofit/OkHttp
:core:model               → pure Kotlin model
:core:designsystem        → theme, common composable
:core:testing             → fake, test rule
```
- Feature module একে অপরকে চেনে না। দরকার হলে ছোট `:feature:x:api` module (route, interface), আর আসল code `:feature:x:impl`-এ।

**Gradle `api` vs `implementation`:**
- `implementation(dep)`: dep শুধু এই module-এর ভেতরে দেখা যায়। dep বদলালে শুধু এই module recompile।
- `api(dep)`: যারা এই module ব্যবহার করে তারাও dep দেখে। বদলালে সবাই recompile।
- Default `implementation`। `api` শুধু যখন dep-এর type আপনার public API-তে আছে।

**Build speed কেন বাড়ে:**
- এক module বদলালে শুধু সেটা আর তার dependent recompile।
- Gradle parallel build, build cache, configuration cache কাজে লাগে।
- কিন্তু অনেক বেশি ছোট module = configuration-এর খরচ বাড়ে। মাপুন (`--scan` / Build Analyzer)।

**Convention plugin:**
- `build-logic/` নামে একটা included build। এখানে নিজের Gradle plugin লেখেন, যেমন `myapp.android.feature`।
- প্রতিটা feature module-এ ৩০ লাইন copy না করে এক লাইন: `plugins { id("myapp.android.feature") }`।
- Version এক জায়গায়: `gradle/libs.versions.toml` (version catalog)।

Flutter-এ এর কাছাকাছি হলো monorepo-তে আলাদা Dart package (melos / pub workspaces)।

**Answer (English):**
> "I split by feature and by core layer. Each feature module has its screens and ViewModels. Core modules hold data, database, network, model, and the design system. Feature modules do not depend on each other. If they must talk, I add a small api module with only routes or interfaces. In Gradle I use implementation by default, so a change does not force other modules to recompile. I use api only when a type is part of the public API. To avoid copy-pasted build files, I write convention plugins in a build-logic folder and keep versions in the version catalog. The trade-off is setup cost, so I do not create tiny modules without a reason."

**Key words:** `feature module` · `core module` · `api vs implementation` · `convention plugin` · `build-logic` · `version catalog`

**Follow-up:**
- **Q:** How do two feature modules navigate to each other?
  **A:** "The app module owns the navigation graph. Each feature exposes its route in a small api module, so features never depend on each other's implementation."
- **Q:** Does modularization always make builds faster?
  **A:** "Not always. Incremental builds get faster, but too many modules add configuration time. I measure with a build scan before and after."

**আরও দেখুন:** [P12 · Gradle basics](#p12) · [R5 · Hilt](#r5)

---

### <a id="r7"></a>R7. ★ Explain Room: entities, DAOs, Flow queries, relations, transactions and migrations.

**প্রশ্নটা মানে:** Local DB নিরাপদে ব্যবহার করতে পারেন কিনা — বিশেষ করে migration-এ user data না হারিয়ে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you change the database schema without losing data?" · "How do you test a Room migration?"

**বুঝে নিন:**

**মূল অংশ:**
- `@Entity` — একটা table। `@PrimaryKey`, `@ColumnInfo`, index।
- `@Dao` — query। `@Query`, `@Insert`, `@Update`, `@Delete`, `@Upsert`।
- `@Database(entities = [...], version = N)` — DB class।
- Kotlin-এ query হয় `suspend fun` (এক বার) বা `Flow` return (observe)। Table বদলালে Flow নিজেই নতুন data দেয় — Room-এর invalidation tracker এটা করে।

```kotlin
@Entity(tableName = "camera")
data class CameraEntity(
    @PrimaryKey val id: String,
    val name: String,
    val ip: String,
    val lastSeen: Long,
)

@Dao
interface CameraDao {
    @Query("SELECT * FROM camera WHERE name LIKE :q ORDER BY name")
    fun observeByName(q: String): Flow<List<CameraEntity>>

    @Upsert
    suspend fun upsertAll(items: List<CameraEntity>)
}
```

**Relation:** `@Embedded` parent + `@Relation` child list। Room দুটো query চালায়, তাই DAO function-এ `@Transaction` দিন — নইলে দুই query-র মাঝে data বদলে যেতে পারে।

**Transaction:** কয়েকটা write একসাথে, হয় সব হবে নয় কিছুই না। `@Transaction` DAO function, বা code থেকে: Room 2.x-এ `db.withTransaction {}`, Room 3-এ `db.withWriteTransaction {}`।

**Migration:**
- Schema বদলালে `version` বাড়ান।
- সহজ বদল (নতুন column, নতুন table) → **`@AutoMigration(from = 1, to = 2)`**। এজন্য `exportSchema = true` আর Room Gradle plugin-এ `schemaDirectory`। Schema JSON git-এ commit করুন।
- Rename/delete হলে `AutoMigrationSpec` (`@RenameColumn`, `@DeleteColumn`)।
- জটিল বদল → manual `Migration(1, 2)` SQL দিয়ে।
- `fallbackToDestructiveMigration()` = সব data মুছে ফেলে। শুধু pure cache DB-তে।

**Migration test:**
- `room-testing`-এর (Room 3-এ `androidx.room3:room3-testing`) **`MigrationTestHelper`**: পুরনো version-এ DB বানান, data ঢোকান, migration চালান, `runMigrationsAndValidate` schema মিলিয়ে দেখে। তারপর data ঠিক আছে কিনা query করুন।
- এটা না করলে update-এর পর user-এর app crash করে (`IllegalStateException: Migration didn't properly handle`)।

**Room 3.0 (stable July 2026):**
- Package `androidx.room3`, artifact `androidx.room3:room3-runtime`।
- শুধু KSP, শুধু Kotlin code generate করে।
- DAO function হয় `suspend`, নয়তো `Flow` (blocking DAO নিষেধ)।
- পুরোটা `SQLiteDriver` API-র উপর। পুরনো `SupportSQLite` code-এর জন্য migration-এর সময় `room3-sqlite-wrapper` artifact আছে।
- LiveData আর Paging return type এখন আলাদা artifact-এ (`room3-livedata`, `room3-paging`)।
- Type converter-এর নাম বদলেছে: `@TypeConverter` → `@ColumnTypeConverter`, `@TypeConverters` → `@ColumnTypeConverters`। Transaction: `runInTransaction` → `withWriteTransaction {}`; সরাসরি SQL-এর জন্য `useReaderConnection` / `useWriterConnection`।
- Annotation (`@Entity`, `@Dao`, `@Database`, `@Query`) একই আছে। Room 2.x এখন maintenance mode-এ।

Flutter-এ `drift`-এর `MigrationStrategy` আর schema version-এর মতোই ধারণা।

**Answer (English):**
> "In Room, an Entity is a table, a DAO holds the queries, and the Database class ties them together with a version number. I return Flow for data the UI observes, so the screen updates by itself when the table changes, and I use suspend functions for one-time reads and writes. For relations I use Embedded and Relation, and I mark the query with Transaction so both queries see the same data. When the schema changes, I bump the version and use AutoMigration for simple changes and a manual Migration for complex ones. I export the schema to git and test every migration with MigrationTestHelper. I never use destructive migration for user data."

**Key words:** `@Entity` · `@Dao` · `Flow query` · `@Relation` · `@Transaction` · `AutoMigration` · `MigrationTestHelper` · `exportSchema`

**Follow-up:**
- **Q:** Why must a relation query be in a transaction?
  **A:** "Room runs one query for parents and one for children. Without a transaction, another write can happen between them, and the result can be mixed."
- **Q:** What do you do if a migration fails in production?
  **A:** "I ship a fixed migration fast. To prevent it, every version step has a migration test in CI, starting from real old schemas."
- **Q:** Would you move to Room 3.0 now?
  **A:** "For a new project, yes. For an existing app, I first move to the SQLiteDriver APIs on Room 2.x, then change packages. It is a breaking change, so I do it in its own release."

**ভুল করবেন না:** Schema export বন্ধ রাখবেন না — schema JSON ছাড়া AutoMigration আর migration test কোনোটাই কাজ করে না।

**আরও দেখুন:** [R4 · Single source of truth](#r4) · [R11 · Paging 3](#r11)

---

### <a id="r8"></a>R8. ★ DataStore or SharedPreferences? Preferences or Proto DataStore?

**প্রশ্নটা মানে:** ছোট setting কোথায় রাখেন, আর SharedPreferences-এর সমস্যা জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why did Google replace SharedPreferences?" · "Where do you store a token securely?"

**বুঝে নিন:**

**SharedPreferences-এর সমস্যা:**
- API synchronous। প্রথম read-এ file load শেষ না হলে main thread আটকে যায়।
- `apply()` async মনে হয়, কিন্তু Activity/Service lifecycle-এর কিছু জায়গায় system pending write শেষ হওয়ার জন্য অপেক্ষা করে → **ANR** হতে পারে।
- Error জানানোর উপায় নেই। Type safety নেই। Transaction নেই।

**DataStore:**
- Coroutine + `Flow` দিয়ে read। Write `suspend` আর **atomic** (`edit {}` / `updateData {}`)।
- I/O error `Flow`-এ exception হিসেবে আসে — handle করতে হয়।
- **Preferences DataStore:** key-value, schema নেই। সহজ settings।
- **Proto / typed DataStore:** একটা typed object রাখে। Schema protobuf দিয়ে, বা নিজের `Serializer` লিখে kotlinx.serialization দিয়েও করা যায়। Type safe।
- KMP সাপোর্ট আছে।

**নিয়ম:**
- এক file-এর জন্য **একটাই DataStore instance** (Hilt `@Singleton` বা `preferencesDataStore` delegate top-level-এ)। দুটো হলে exception।
- বড় বা relational data → Room, DataStore না।
- পুরনো data আনতে: `SharedPreferencesMigration`।
- Multi-process হলে `MultiProcessDataStoreFactory`।

**Security:** DataStore নিজে encrypt করে না। `EncryptedSharedPreferences` (security-crypto) এখন **deprecated**। Token রাখতে: **Android Keystore**-এ key + **Tink** দিয়ে value encrypt করে DataStore বা file-এ রাখুন।

```kotlin
val Context.settings by preferencesDataStore(name = "settings")
private val MOTION_ALERTS = booleanPreferencesKey("motion_alerts")

val motionAlerts: Flow<Boolean> = context.settings.data
    .catch { if (it is IOException) emit(emptyPreferences()) else throw it }
    .map { it[MOTION_ALERTS] ?: true }

suspend fun setMotionAlerts(on: Boolean) =
    context.settings.edit { it[MOTION_ALERTS] = on }
```

Flutter-এর `shared_preferences` Android-এ আগে SharedPreferences ব্যবহার করত; নতুন `SharedPreferencesAsync` API Android-এ DataStore ব্যবহার করে (package version দেখে নিন)।

**Answer (English):**
> "For new code I use DataStore, not SharedPreferences. SharedPreferences has a sync API, and apply can still block the main thread at some lifecycle points, which can cause ANRs. It also has no way to report errors. DataStore reads with Flow and writes with suspend functions, and each write is atomic. I use Preferences DataStore for simple settings and typed or Proto DataStore when I want a schema and type safety. I keep only one instance per file. DataStore does not encrypt, so for a token I encrypt the value with Tink and a Keystore key. EncryptedSharedPreferences is deprecated now."

**Key words:** `Preferences DataStore` · `Proto DataStore` · `atomic edit` · `single instance` · `SharedPreferencesMigration` · `Tink + Keystore`

**Follow-up:**
- **Q:** Can you read DataStore synchronously at app start?
  **A:** "You can with runBlocking and first(), but it blocks the thread. I avoid it, or I read it once in a background coroutine early and cache the value."
- **Q:** When would you choose Room over DataStore?
  **A:** "When the data is a list, needs queries, or has relations. DataStore rewrites the whole file on each change, so it is for small data."

**ভুল করবেন না:** "Token-এর জন্য EncryptedSharedPreferences ব্যবহার করি" বলবেন না — এটা deprecated।

**আরও দেখুন:** [S2 · Tokens and secrets](#s2) · [R7 · Room](#r7)

---

### <a id="r9"></a>R9. ★ How do you set up Retrofit and OkHttp? How do you refresh an expired token?

**প্রশ্নটা মানে:** Network stack production-ready ভাবে বানাতে পারেন কিনা — বিশেষ করে token refresh-এর race condition।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between an interceptor and an Authenticator?" · "Ten requests get 401 at the same time. What happens?"

**বুঝে নিন:**

**ভাগ:**
- **Retrofit:** interface থেকে HTTP call বানায়। `suspend fun` সাপোর্ট করে, main-safe।
- **OkHttp:** আসল HTTP client — connection pool, HTTP/2, cache, interceptor, TLS।
- একটাই `OkHttpClient` (`@Singleton`) রাখুন। প্রতি request-এ নতুন client = connection pool আর thread নষ্ট।

**Interceptor:**
- **Application interceptor** (`addInterceptor`): প্রতি call-এ এক বার। Header যোগ (auth, user-agent), logging।
- **Network interceptor** (`addNetworkInterceptor`): প্রতি network hop-এ (redirect-এও)। Cache থেকে আসলে চলে না। Cache header বদলাতে।
- Logging শুধু debug build-এ। Token log করবেন না।

**Authenticator (token refresh):**
- Server **401** দিলে OkHttp `Authenticator.authenticate()` ডাকে। নতুন header সহ request return করলে OkHttp আবার চেষ্টা করে। `null` return = হাল ছেড়ে দাও।
- **সমস্যা:** ১০টা request একসাথে 401 পেলে ১০ বার refresh হতে পারে। অনেক server-এ refresh token এক বার ব্যবহারে বাতিল হয় → বাকিগুলো fail → user logout।
- **সমাধান:** lock নিন। Lock-এর ভেতরে দেখুন — এই request যে token নিয়ে গিয়েছিল, store-এ কি এখনো সেটাই? না হলে অন্য কেউ refresh করে ফেলেছে — নতুনটা নিয়ে retry। একই হলে তখনই refresh।
- Refresh call-এর জন্য আলাদা client (Authenticator ছাড়া), নইলে loop।
- Loop থামাতে: আগে একবার retry হয়ে থাকলে (`priorResponse != null`) `null` return।

```kotlin
class TokenAuthenticator @Inject constructor(
    private val tokens: TokenStore,
    private val authApi: AuthApi,          // uses a client WITHOUT this authenticator
) : Authenticator {
    override fun authenticate(route: Route?, response: Response): Request? {
        if (response.priorResponse != null) return null          // already retried once
        val sent = response.request.header("Authorization")?.removePrefix("Bearer ")
        val token = synchronized(this) {
            val current = tokens.accessToken()
            if (current != null && current != sent) current       // someone else refreshed
            else authApi.refreshBlocking(tokens.refreshToken())?.also(tokens::save)
        } ?: return null                                          // refresh failed → logout
        return response.request.newBuilder().header("Authorization", "Bearer $token").build()
    }
}
```
Authenticator OkHttp-এর background thread-এ চলে, তাই এখানে blocking call ঠিক আছে।

**Timeout:**
- `connectTimeout`, `readTimeout`, `writeTimeout` — default ১০ সেকেন্ড করে। `callTimeout` পুরো call-এর জন্য (default নেই)।
- Upload/বড় download-এ বাড়ান, সাধারণ API-তে default যথেষ্ট।

**HTTP cache:** `Cache(File(cacheDir, "http"), 10L * 1024 * 1024)`। Server-এর `Cache-Control` / `ETag` মেনে চলে। Offline-first app-এ আসল cache Room, HTTP cache শুধু সাহায্য।

**Version:** Retrofit 3.0 (2025) এসেছে, 2.x-এর সাথে প্রায় compatible। OkHttp 5 stable (2025)। কোন OkHttp version resolve হলো `./gradlew dependencies` দিয়ে দেখুন।

**Ktor client:** coroutine-first, **KMP**-এ চলে। Android-এ engine হিসেবে OkHttp ব্যবহার করতে পারে। KMP shared code-এ Ktor, Android-only app-এ Retrofit — আমার পছন্দ।

Flutter-এ `dio`-র `QueuedInterceptor` দিয়ে ঠিক এই "এক বারই refresh" সমস্যা সমাধান করা হয়।

**Answer (English):**
> "I use one shared OkHttpClient and Retrofit with suspend functions. An application interceptor adds headers like the access token, and logging is on only in debug builds. For token refresh I use OkHttp's Authenticator, which runs when the server returns 401. The danger is many requests failing at once and all of them refreshing. So I refresh inside a lock. In the lock I check if the token already changed; if yes, I just retry with the new one. The refresh call uses a separate client, and I stop after one retry to avoid a loop. If the refresh fails, I return null and log the user out cleanly."

**Key words:** `OkHttpClient singleton` · `application vs network interceptor` · `Authenticator` · `401` · `token refresh race` · `callTimeout` · `HTTP cache` · `Ktor`

**Follow-up:**
- **Q:** Why not refresh the token inside an interceptor?
  **A:** "You can, but the Authenticator is made for 401 responses and OkHttp retries for you. In both cases you still need the lock and the token check."
- **Q:** How do you handle SSL pinning?
  **A:** "I can use OkHttp's CertificatePinner or the network security config. I always pin a backup key too, because a wrong pin can block every user until an app update."
- **Q:** Retrofit or Ktor for a new app?
  **A:** "Android only, Retrofit, because the team knows it and it is stable. If the network code is shared with iOS through KMP, Ktor."

**ভুল করবেন না:** Lock ছাড়া refresh বলবেন না — "parallel 401" follow-up প্রায় নিশ্চিত আসে।

**আরও দেখুন:** [S5 · Network security](#s5) · [R10 · Network errors](#r10) · [S6 · Secure login](#s6)

---

### <a id="r10"></a>R10. ★ How do you handle errors from the network to the UI?

**প্রশ্নটা মানে:** Error চুপ করে গিলে ফেলেন না তো? Error-কে type দিয়ে model করেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you model loading, success and error states?" · "How do you retry a failed request?"

**বুঝে নিন:**

**১. Data layer-এ exception → নিজের error type:**
| Exception | মানে | Domain error |
|---|---|---|
| `IOException` (`UnknownHostException`, `SocketTimeoutException`) | network নেই / ধীর | `NoNetwork` / `Timeout` |
| `HttpException` 401/403 | auth | `Unauthorized` |
| `HttpException` 404 | নেই | `NotFound` |
| `HttpException` 5xx, 429 | server সমস্যা | `Server` (retry করা যায়) |
| `SerializationException` | server ভুল data দিল | `BadData` (bug — log করুন) |

**২. Result type:** Kotlin-এর `Result` বা নিজের sealed class। নিজেরটায় error type-safe থাকে।

**৩. UI-তে `UiState`:**
```kotlin
sealed interface CamerasUiState {
    data object Loading : CamerasUiState
    data class Content(val cameras: List<Camera>, val error: AppError? = null) : CamerasUiState
    data class Error(val error: AppError) : CamerasUiState
}
```
- পুরনো data থাকলে `Content` + error banner। পুরো screen error শুধু যখন কিছুই নেই।

**৪. `CancellationException` কখনো গিলবেন না।** `runCatching {}` এটাকেও ধরে — coroutine cancel ভেঙে যায়। Catch করলে আবার `throw` করুন।

**৫. Retry with exponential backoff:**
- শুধু **অল্প সময়ের** error-এ (IOException, 5xx, 429)। 400/401/404-এ retry নয়।
- শুধু **idempotent** request-এ (GET, PUT)। POST-এ retry করলে দুবার order হতে পারে — idempotency key লাগে।
- Delay দ্বিগুণ করুন, সর্বোচ্চ সীমা দিন, একটু random **jitter** যোগ করুন (সব device একসাথে retry না করে)।
- 429-এ `Retry-After` header মানুন।
- Background sync-এ WorkManager-এর নিজের backoff ব্যবহার করুন।

```kotlin
suspend fun <T> retryWithBackoff(
    times: Int = 3,
    initial: Duration = 500.milliseconds,
    max: Duration = 8.seconds,
    block: suspend () -> T,
): T {
    var wait = initial
    repeat(times - 1) {
        try { return block() } catch (e: IOException) { Log.w(TAG, "retry", e) }
        delay(wait + Random.nextLong(0, 250).milliseconds)
        wait = (wait * 2).coerceAtMost(max)
    }
    return block()   // last try: error goes up to the caller
}
```

**৬. No silent failure:** প্রতিটা error হয় user দেখে, নয়তো log/crash reporter-এ non-fatal হিসেবে যায়। খালি `catch {}` নিষেধ।

**Answer (English):**
> "I map errors at the edge of the data layer. Network exceptions and HTTP codes become my own small error types, like NoNetwork, Unauthorized, or Server. The ViewModel turns them into a sealed UiState. If I still have old data, I show it with an error message, not an empty screen. I never swallow CancellationException, so I avoid runCatching around suspend calls or I rethrow it. I retry only short-lived errors like timeouts and 5xx, only for safe requests, with exponential backoff and a little random jitter. Every error is either shown to the user or logged as a non-fatal. An empty catch block is a bug for me."

**Key words:** `sealed UiState` · `error mapping` · `CancellationException` · `exponential backoff` · `jitter` · `idempotent` · `non-fatal logging`

**Follow-up:**
- **Q:** Why add jitter?
  **A:** "If a server goes down, thousands of devices fail at the same time. Without jitter, they all retry at the same moment and hit the server again together."
- **Q:** Why is runCatching risky with coroutines?
  **A:** "It catches CancellationException too. Then a cancelled coroutine keeps running as if nothing happened, which breaks structured concurrency."

**ভুল করবেন না:** POST request অন্ধভাবে retry করার কথা বলবেন না — duplicate action হয়।

**আরও দেখুন:** [K11 · Coroutine exceptions](#k11) · [K24 · Sealed state](#k24) · [R9 · Retrofit & OkHttp](#r9)

---

### <a id="r19"></a>R19. ◆ How do you cache data and decide when it is stale?

**প্রশ্নটা মানে:** কোন data কোথায় cache করেন, আর কখন সেটাকে পুরনো ধরে আবার আনেন — এটা আপনি ভেবে করেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How does the HTTP cache work in OkHttp?" · "How do you avoid showing old data to the user?"

**বুঝে নিন:**

**তিন জায়গায় cache:**
| জায়গা | কী দিয়ে | ভালো দিক / সীমা |
|---|---|---|
| Memory | repository-র ভেতরে `StateFlow`, `LruCache` | সবচেয়ে দ্রুত। Process death-এ চলে যায়। |
| Disk | Room (বা file) | Offline-এ চলে, restart-এর পরেও থাকে। Offline-first app-এ এটাই আসল cache। |
| HTTP cache | OkHttp `Cache` | Server-এর header মেনে response রাখে। Room-এর পাশে শুধু সাহায্য। |

**Data কখন stale — তিন উপায়:**
- **Time-based (TTL):** প্রতিটা data-র সাথে `fetchedAt` রাখুন। `now - fetchedAt > ttl` হলে refresh। আগে পুরনো data দেখান, পেছনে refresh চালান (stale-while-revalidate)।
- **HTTP header:** `Cache-Control: max-age=60` মানে ৬০ সেকেন্ড network ছাড়াই cache থেকে। Response-এ `ETag` থাকলে OkHttp পরের বার `If-None-Match` পাঠায়। Data না বদলালে server `304` দেয় — body আসে না, data কম খরচ হয়।
- **Event-based:** server push (FCM / WebSocket) বলে "data বদলেছে" → তখন refresh। User pull-to-refresh করলে সবসময় refresh।

**নিয়ম:**
- TTL ঠিক করে product: camera online status-এর জন্য কয়েক সেকেন্ড, profile-এর জন্য কয়েক ঘণ্টা।
- Logout হলে সব cache মুছুন — memory, Room, HTTP cache (`cache.evictAll()`)। নইলে পরের user আগের user-এর data দেখে।
- Token বা private data HTTP cache-এ রাখবেন না। Server যেন `Cache-Control: no-store` পাঠায়।
- `now` inject করুন (`Clock`), তাহলে test-এ fake clock দিয়ে TTL check করা যায়।

```kotlin
suspend fun refreshIfStale(ttl: Duration = 5.minutes) {
    val last = dao.lastFetchedAt() ?: Instant.DISTANT_PAST
    if (clock.now() - last < ttl) return          // still fresh
    val remote = api.getCameras()
    dao.replaceAll(remote.map { it.toEntity() }, fetchedAt = clock.now())
}
```

Flutter-এ `dio_cache_interceptor` আর `cached_network_image`-এর disk cache — একই ধারণা।

**Answer (English):**
> "I think about cache in three layers. The memory cache is the fastest, but it is lost when the process dies. Room is my real cache, so the app works offline and after a restart. OkHttp's HTTP cache follows the server's Cache-Control and ETag headers, so an unchanged response comes back as a small 304. To decide when data is stale, I save a fetched-at time and refresh after a time limit. I show the old data first and refresh in the background. A push message or pull-to-refresh also forces a refresh. On logout I clear every cache, because the next user must never see old private data."

**Key words:** `memory cache` · `disk cache` · `TTL` · `stale-while-revalidate` · `Cache-Control` · `ETag` · `304 Not Modified` · `cache invalidation`

**Follow-up:**
- **Q:** What is the difference between max-age, no-cache and no-store?
  **A:** "max-age lets the app use the cached copy without asking the server for that time. no-cache means it can keep a copy, but must check with the server first, for example with an ETag. no-store means do not save it at all."
- **Q:** How do you choose the time limit?
  **A:** "I ask how bad old data is for the user. A camera's online status may need a few seconds. A user profile can wait hours."

**ভুল করবেন না:** Logout-এ cache clear করার কথা ভুলবেন না — এটা privacy bug, interviewer এটা ধরে।

**আরও দেখুন:** [R4 · Offline-first](#r4) · [R9 · OkHttp](#r9) · [R8 · DataStore](#r8)

---

### <a id="r11"></a>R11. ◆ How does Paging 3 work? When do you need RemoteMediator?

**প্রশ্নটা মানে:** লম্বা list (event log, recording list) page করে load করতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you load a long list from the network and cache it?" · "What is a PagingSource?"

**বুঝে নিন:**

**অংশগুলো:**
- **`PagingSource<Key, Value>`:** এক page load করে। `load(params)` return করে `LoadResult.Page(data, prevKey, nextKey)` বা `LoadResult.Error`। `getRefreshKey()` বলে refresh হলে কোথা থেকে শুরু।
- **`Pager(PagingConfig(pageSize = 30)) { source }.flow`** → `Flow<PagingData<T>>`।
- ViewModel-এ `.cachedIn(viewModelScope)` — rotation-এ আবার load হয় না।
- Compose-এ `collectAsLazyPagingItems()` + `LazyColumn`। `loadState` দিয়ে loading/error footer।

**শুধু network:** একটা PagingSource যা API ডাকে।

**Network + DB (offline-first):** **`RemoteMediator`**:
- UI পড়ে **Room-এর PagingSource** থেকে (Room নিজে বানিয়ে দেয়)। DB = source of truth।
- DB-র data শেষ হলে Paging `RemoteMediator.load(loadType, state)` ডাকে। এটা network থেকে এনে DB-তে লেখে।
- `LoadType`: `REFRESH`, `PREPEND`, `APPEND`।
- পরের page-এর key রাখতে আলাদা **remote keys table**।
- `initialize()`-এ ঠিক করুন app খোলার সময় refresh লাগবে কিনা।
- Room 3-এ PagingSource return করতে `PagingSourceDaoReturnTypeConverter` (`room3-paging`) register করতে হয়।

**Test:** `paging-testing` artifact-এর `asSnapshot()` দিয়ে flow থেকে list নিয়ে assert।

**কখন লাগবে না:** ছোট list (কয়েকশো row) — সরাসরি Room Flow যথেষ্ট। Paging জটিলতা বাড়ায়।

Flutter-এ `infinite_scroll_pagination`-এর `PagingController`-এর কাজ এখানে Paging library করে।

**Answer (English):**
> "Paging 3 loads a long list in pages. A PagingSource loads one page and returns the data with the previous and next keys. A Pager turns it into a Flow of PagingData, and I call cachedIn on viewModelScope so rotation does not reload. In Compose I use collectAsLazyPagingItems and show load states in the list. If the data must work offline, I use a RemoteMediator. The UI reads pages from Room, and the mediator fetches more from the network and writes it to Room when the local data ends. I keep the next page keys in a small table. For short lists I skip Paging, because it adds complexity."

**Key words:** `PagingSource` · `Pager` · `PagingData` · `cachedIn` · `RemoteMediator` · `remote keys` · `LoadType`

**Follow-up:**
- **Q:** How do you show a retry button at the end of the list?
  **A:** "I read loadState.append. If it is Error, I show a retry item that calls retry() on the paging items."
- **Q:** Can you map or filter PagingData?
  **A:** "Yes, with map and filter on PagingData inside the flow, before cachedIn. I can also add headers with insertSeparators."

**আরও দেখুন:** [R7 · Room](#r7) · [U6 · Fast LazyColumn](#u6)

---

### <a id="r12"></a>R12. ◆ Coil or Glide? How do you avoid out-of-memory with images?

**প্রশ্নটা মানে:** Image library বেছে নেওয়ার কারণ, আর bitmap memory হিসাব জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How much memory does a bitmap use?" · "What is downsampling?"

**বুঝে নিন:**

**Bitmap memory:** `width × height × bytes per pixel`। `ARGB_8888` = ৪ byte।
- 4000 × 3000 (12 MP) photo = ৪৮ MB প্রায়। একটা list-এ কয়েকটা হলেই OOM।
- File size (200 KB JPEG) memory-র হিসাব না। Decode হলে পুরো pixel লাগে।

**Downsampling:** দেখানোর size অনুযায়ী ছোট করে decode।
- পুরনো API: `BitmapFactory.Options.inSampleSize` (২-এর power)।
- নতুন: `ImageDecoder` + `setTargetSize()`।
- Coil আর Glide **নিজেই** view/composable-এর size দেখে downsample করে। তাই size জানা থাকা জরুরি — `wrapContent` হলে পুরো size decode হতে পারে।

**Coil:**
- Kotlin-first, coroutine-based, Compose-এ `AsyncImage`।
- Coil 3 KMP সাপোর্ট করে। Network-এর জন্য আলাদা artifact (`coil-network-okhttp`) যোগ করতে হয়।
- ছোট, modern API।

**Glide:**
- পুরনো, খুব mature, View-based app-এ শক্ত। Bitmap pool, শক্তিশালী cache।
- Compose integration আছে, তবে Coil-এর মতো native মনে হয় না।

**দুটোরই আছে:** memory cache + disk cache, request cancel (screen ছাড়লে), placeholder/error, transformation।

**আমার পছন্দ:** Compose app → Coil। পুরনো View app যেখানে Glide আছে → Glide রাখুন, শুধু library বদলের জন্য migrate না।

**Camera app note:** live RTSP frame image library দিয়ে না — সেটা Media3/decoder-এর কাজ। Snapshot/thumbnail grid-এ Coil, ঠিক thumbnail size চেয়ে।

**Answer (English):**
> "For a Compose app I use Coil. It is Kotlin-first, uses coroutines, and AsyncImage fits Compose well. Glide is also great and very mature, so in an old View app that already uses Glide, I keep it. The real memory issue is bitmap size: width times height times four bytes. A 12-megapixel photo is about 48 megabytes in memory, even if the file is small. So I always decode at the display size. Both libraries downsample for you, but only if they know the target size. I also use their memory and disk caches, and I make sure requests cancel when the item leaves the screen."

**Key words:** `bitmap memory` · `ARGB_8888` · `downsampling` · `inSampleSize` · `ImageDecoder` · `memory cache` · `disk cache` · `AsyncImage`

**Follow-up:**
- **Q:** Why can a fast-scrolling list still use too much memory?
  **A:** "If the image size is unknown, the library may decode the full image. I give the composable a fixed size or tell the request the exact size."
- **Q:** What is RGB_565?
  **A:** "Two bytes per pixel instead of four, with no alpha. It halves memory but lowers quality, so I use it only for big images where quality matters less."

**আরও দেখুন:** [P2 · Memory leaks](#p2) · [U6 · Fast LazyColumn](#u6)

---

### <a id="r13"></a>R13. ◆ kotlinx.serialization, Moshi or Gson — which do you use?

**প্রশ্নটা মানে:** JSON library-র Kotlin নিয়ে সমস্যা জানেন কিনা, বিশেষ করে Gson-এর null safety ভাঙা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why is Gson not good for Kotlin?" · "How do you parse JSON in Android today?"

**বুঝে নিন:**

| | kotlinx.serialization | Moshi | Gson |
|---|---|---|---|
| কীভাবে | compiler plugin, compile-time | codegen (KSP) বা reflection | reflection |
| Kotlin null safety | মানে | মানে | **ভাঙে** |
| Default value | মানে | মানে | মানে না |
| KMP | হ্যাঁ | না | না |
| R8 rule | প্রায় দরকার নেই | codegen-এ কম | reflection-এর জন্য দরকার |
| অবস্থা | active | active | maintenance mode |

**Gson কেন ভালো না:**
- Kotlin class-এ no-arg constructor না থাকলে Gson `Unsafe` দিয়ে constructor ছাড়াই object বানায়।
- ফলে JSON-এ field না থাকলে non-null `val name: String`-এ **null** বসে যায়। পরে কোথাও NPE — যেখানে Kotlin বলেছিল null হতেই পারে না।
- Default value (`val retries: Int = 3`) কাজ করে না।
- Reflection, তাই R8 obfuscation-এ field name বদলে গেলে parse ভাঙে — keep rule লাগে।

**kotlinx.serialization:**
- `@Serializable` data class। Plugin: `kotlin("plugin.serialization")`।
- `Json { ignoreUnknownKeys = true }` — server নতুন field যোগ করলে crash না।
- `@SerialName("camera_id")` নাম মেলাতে।
- Retrofit-এর official converter আছে: `converter-kotlinx-serialization` (Retrofit 2.11 থেকে)।
- Navigation type-safe route-ও `@Serializable` ব্যবহার করে — এক library সব জায়গায়।

```kotlin
@Serializable
data class CameraDto(
    @SerialName("camera_id") val id: String,
    val name: String,
    val online: Boolean = false,
)
val json = Json { ignoreUnknownKeys = true }
val camera = json.decodeFromString<CameraDto>(body)
```

Flutter-এ `json_serializable` + `build_runner`-এর code generation-এর মতোই compile-time, কিন্তু এখানে আলাদা build step লাগে না — compiler plugin।

**Answer (English):**
> "I use kotlinx.serialization. It works at compile time with a compiler plugin, so there is no reflection, it respects Kotlin null safety and default values, and it works in Kotlin Multiplatform. Retrofit has an official converter for it. Moshi with code generation is also a good choice. I avoid Gson for Kotlin, because it can create objects without calling the constructor. Then a non-null field can hold null, and the app crashes later in a strange place. Gson also ignores default values and needs keep rules for R8. I always set ignoreUnknownKeys, so a new field from the server does not break old app versions."

**Key words:** `@Serializable` · `compile-time` · `null safety` · `ignoreUnknownKeys` · `@SerialName` · `reflection` · `R8 keep rules`

**Follow-up:**
- **Q:** What happens if the server sends null for a non-null field?
  **A:** "kotlinx.serialization throws an error during parsing, which I map to a BadData error. That is better than a hidden null that crashes later. If the field can really be null, I make it nullable."
- **Q:** How do you handle an unknown enum value from the server?
  **A:** "I can set coerceInputValues so it uses the default value, or add an UNKNOWN entry with a custom serializer."

**আরও দেখুন:** [P5 · R8](#p5) · [R9 · Retrofit](#r9)

---

### <a id="r14"></a>R14. ★ How do you unit test a ViewModel?

**প্রশ্নটা মানে:** Coroutine আর Flow test করার নিয়ম জানেন কিনা — test deterministic হয় কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you test coroutines?" · "What is the difference between StandardTestDispatcher and UnconfinedTestDispatcher?"

**বুঝে নিন:**

**`runTest`:** test coroutine চালায় **virtual time**-এ। `delay(10_000)` সাথে সাথে শেষ হয়। Test-এর শেষে বাকি coroutine থাকলে fail করে।

**দুই dispatcher:**
| | `StandardTestDispatcher` | `UnconfinedTestDispatcher` |
|---|---|---|
| `launch` করলে | queue-তে যায়, এখনই চলে না | সাথে সাথে চলে (প্রথম suspend পর্যন্ত) |
| চালাতে | `advanceUntilIdle()`, `runCurrent()`, `advanceTimeBy()` | নিজে থেকেই |
| কখন | order ঠিকঠাক দেখতে চাইলে | সহজ test, `StateFlow` collect |

**Main dispatcher rule:**
- `viewModelScope` চলে `Dispatchers.Main`-এ। JVM test-এ Android Main নেই → crash।
- তাই `Dispatchers.setMain(testDispatcher)` আর শেষে `resetMain()` — একটা JUnit rule-এ।
- Main-এ test dispatcher বসালে `runTest` একই scheduler ব্যবহার করে।
- Repository-তে `Dispatchers.IO` hardcode না করে **inject** করুন, test-এ test dispatcher দিন।

**Turbine:** Flow test library। `flow.test { awaitItem(); awaitComplete() }`। প্রতিটা emission ধাপে ধাপে দেখা যায়।

**Fake vs MockK:**
- **Fake** = interface-এর ছোট আসল implementation (memory-তে list + `MutableStateFlow`)। Behaviour test করে। Refactor-এ ভাঙে না। **প্রথম পছন্দ।**
- **MockK** = যখন interaction-টাই আসল behaviour ("analytics event পাঠানো হয়েছে কিনা")। বেশি mock = সহজে ভাঙে এমন test।

```kotlin
class MainDispatcherRule(
    val dispatcher: TestDispatcher = UnconfinedTestDispatcher(),
) : TestWatcher() {
    override fun starting(description: Description) = Dispatchers.setMain(dispatcher)
    override fun finished(description: Description) = Dispatchers.resetMain()
}
```

```kotlin
class CamerasViewModelTest {
    @get:Rule val mainRule = MainDispatcherRule()
    private val repo = FakeCameraRepository()

    @Test fun `shows cameras after they load`() = runTest {
        val vm = CamerasViewModel(repo, SavedStateHandle())
        vm.uiState.test {
            assertEquals(CamerasUiState.Loading, awaitItem())
            repo.emit(listOf(frontDoor))
            assertEquals(CamerasUiState.Content(listOf(frontDoor)), awaitItem())
        }
    }
}
```

- `stateIn(WhileSubscribed)` হলে কেউ collect না করলে value বদলায় না। তাই Turbine দিয়ে collect করুন, বা `backgroundScope.launch { vm.uiState.collect() }`।

Flutter-এ `bloc_test` / `fake_async`-এর মতো — virtual time আর step-by-step state check।

**Answer (English):**
> "I test the ViewModel on the JVM with runTest, which uses virtual time, so delays finish at once. viewModelScope uses the Main dispatcher, so I replace Main with a test dispatcher in a JUnit rule and reset it after. I inject other dispatchers too, instead of hard-coding IO. StandardTestDispatcher queues coroutines until I advance it, which is good for checking order. UnconfinedTestDispatcher runs them at once, which is simpler. I collect state with Turbine and check each value step by step. I prefer fakes over mocks, like a fake repository with a MutableStateFlow, because they test behaviour and do not break on refactors. I use MockK only when the call itself is the behaviour."

**Key words:** `runTest` · `virtual time` · `StandardTestDispatcher` · `UnconfinedTestDispatcher` · `Dispatchers.setMain` · `Turbine` · `fake` · `MockK`

**Follow-up:**
- **Q:** Your StateFlow test never sees the new value. Why?
  **A:** "Probably the flow uses WhileSubscribed and nobody collects it, or the dispatcher is Standard and I did not advance it. I collect with Turbine or in backgroundScope, and call advanceUntilIdle if needed."
- **Q:** How do you test a five-second timeout?
  **A:** "With runTest and advanceTimeBy. The virtual clock moves five seconds at once, so the test is fast and not flaky."
- **Q:** What do you test in a ViewModel?
  **A:** "Success, empty, error, and the edge case that matters, like a retry that keeps the old list. I test through public state, not private functions."

**ভুল করবেন না:** Test-এ `Thread.sleep()` বা আসল `delay` অপেক্ষার কথা বলবেন না — flaky test।

**আরও দেখুন:** [K26 · Testing coroutines](#k26) · [R15 · UI tests](#r15)

---

### <a id="r15"></a>R15. ◆ How do you write UI and integration tests? What is your test pyramid?

**প্রশ্নটা মানে:** কোন test কোথায় চালান, আর speed vs confidence-এর trade-off বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Espresso or Compose testing?" · "What is Robolectric and why use it?"

**বুঝে নিন:**

**Pyramid:**
```
        ▲  E2E / instrumented (device) — কম, ধীর, আসল device
       ▲▲  UI / component test (Compose test, Robolectric) — মাঝারি
     ▲▲▲▲  Unit test (ViewModel, repository, mapper) — অনেক, দ্রুত
```

**Compose testing:**
- `createComposeRule()` / `createAndroidComposeRule<Activity>()`।
- Node খুঁজুন semantics দিয়ে: `onNodeWithText`, `onNodeWithContentDescription`, `onNodeWithTag`।
- `performClick()`, `assertIsDisplayed()`।
- Composable-কে state দিন (stateless screen), তাহলে ViewModel ছাড়াই test হয়।
- Compose 1.11 থেকে "v2" test API default, v1 deprecated। v2 composition চালায় `StandardTestDispatcher`-এ, তাই launch করা coroutine নিজে থেকে চলে না — `waitForIdle()` বা clock এগোতে হয়। Docs-এর migrate-v2 page দেখুন।

**Espresso:** View-based UI-র জন্য। `onView(withId(...)).perform(click())`। Compose + View মিশ্র app-এ দুটোই চলে।

**Robolectric:** Android framework JVM-এ simulate করে। Local test হিসেবে চলে — emulator লাগে না, দ্রুত। Compose test-ও চালানো যায়। কিন্তু আসল device না — rendering, GPU, OEM আচরণ ধরা পড়ে না।

**Instrumented test:** আসল device/emulator। CI-তে **Gradle Managed Devices** দিয়ে emulator চালানো যায়। Room migration, camera, permission flow এখানে।

**Screenshot test:** UI-র ছবি তুলে আগের ছবির সাথে মেলায়।
- Roborazzi (Robolectric-এ), Paparazzi (layoutlib), Google-এর Compose Preview Screenshot Testing (নতুন tool — status docs-এ দেখে নিন)।
- Theme, dark mode, font scale, বড় screen-এর regression ধরে।

**Hilt-এ UI test:** `@HiltAndroidTest` + `HiltAndroidRule` + `@TestInstallIn` দিয়ে fake repository।

Flutter mapping: unit test → `test`, widget test → Compose test/Robolectric, golden test → screenshot test, `integration_test` → instrumented test।

```kotlin
@get:Rule val compose = createComposeRule()

@Test fun showsOfflineBadge() {
    compose.setContent { CameraCard(camera = frontDoor.copy(online = false)) }
    compose.onNodeWithText("Offline").assertIsDisplayed()
}
```

**Answer (English):**
> "I follow the test pyramid. Most tests are fast JVM unit tests for ViewModels, repositories, and mappers. Then component tests for screens, written with the Compose testing APIs. I find nodes by text, content description, or test tag, and I keep screens stateless so I can test them with plain state. I run many of these on Robolectric, so they are fast and need no emulator. A few instrumented tests run on real devices or Gradle Managed Devices for things like migrations and permission flows. I add screenshot tests to catch visual changes in themes and font sizes. The trade-off is speed versus real behaviour."

**Key words:** `test pyramid` · `createComposeRule` · `semantics` · `Espresso` · `Robolectric` · `Gradle Managed Devices` · `screenshot test`

**Follow-up:**
- **Q:** When does Robolectric give you false confidence?
  **A:** "It simulates the framework, so device-specific bugs, real rendering, and hardware like the camera are not tested. Those need a real device."
- **Q:** How do you make a UI test not flaky?
  **A:** "I use fakes instead of the real network, let the Compose rule wait for idle, and avoid sleeps. If a test is flaky, I fix it at once."

**আরও দেখুন:** [R14 · ViewModel test](#r14) · [P9 · CI/CD](#p9)

---

### <a id="r16"></a>R16. ◆ WebSocket, Server-Sent Events, MQTT or FCM — when do you use each?

**প্রশ্নটা মানে:** Real-time data-র জন্য ঠিক protocol বেছে নিতে পারেন কিনা — IoT/camera company-তে এটা খুব জরুরি।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you get live updates from a server?" · "How do you get a motion alert when the app is closed?"

**বুঝে নিন:**

| | দিক | কিসের উপর | কখন |
|---|---|---|---|
| **WebSocket** | দুই দিকেই | একটা TCP connection, HTTP থেকে upgrade | chat, live control (camera PTZ command + status) |
| **SSE** | শুধু server → app | সাধারণ HTTP, text stream | live feed, status update, log stream; সহজ, proxy-friendly |
| **MQTT** | pub/sub, broker দিয়ে | TCP (বা WebSocket) | IoT device, sensor, অনেক device, খারাপ network |
| **FCM** | server → device | Google Play services | app background/বন্ধ থাকলে জাগানো, alert |

**MQTT-এর মূল বিষয়:**
- Broker-এ topic (`site/12/camera/3/motion`)। Device publish করে, app subscribe করে।
- **QoS 0** (একবার পাঠাও, হারাতে পারে), **QoS 1** (অন্তত একবার, duplicate হতে পারে), **QoS 2** (ঠিক একবার, ধীর)।
- **Retained message:** নতুন subscriber শেষ value সাথে সাথে পায় (device online/offline)।
- **Last Will (LWT):** device হঠাৎ বিচ্ছিন্ন হলে broker নিজেই "offline" publish করে।
- Packet ছোট, battery আর data কম।
- Client library: HiveMQ MQTT client-এর মতো maintained library নিন। পুরনো Paho Android Service আর maintained না।
- সবসময় TLS + device/user auth।

**FCM:**
- App বন্ধ থাকলেও message আসে। **Data message** নিজে handle (`onMessageReceived`), **notification message** system দেখায় (background-এ)।
- Payload ছোট (৪ KB পর্যন্ত)। Delivery-র সময় guaranteed না।
- High priority শুধু user-visible জরুরি কাজে, নইলে system priority কমিয়ে দেয়।
- Server-এ **HTTP v1 API** (পুরনো legacy API বন্ধ)।
- Android 13+-এ notification দেখাতে `POST_NOTIFICATIONS` permission।

**Lifecycle নিয়ম:**
- WebSocket/SSE/MQTT connection রাখুন শুধু app foreground-এ থাকলে (lifecycle-aware)। Background-এ রাখা battery নষ্ট, আর system মেরে ফেলবে।
- Background-এ alert → FCM। দরকার হলে FCM পেয়ে WorkManager দিয়ে detail sync।
- Reconnect: exponential backoff + jitter, network callback (`ConnectivityManager.NetworkCallback`) দেখে।

**LAN note:** Local network-এ broker বা camera-র সাথে কথা বললে, API 37 target করলে **`ACCESS_LOCAL_NETWORK`** runtime permission লাগে (Android 17)।

**Answer (English):**
> "It depends on direction and on the app state. WebSocket is for two-way, low-delay data, like sending camera controls and getting status back. Server-Sent Events are simpler when only the server sends, because they are plain HTTP. MQTT is my choice for IoT: a broker, topics, QoS levels, retained messages, and a last-will message to detect a device going offline. It is light on battery and data. All three run only while the app is in the foreground. When the app is in the background or closed, I use FCM to deliver the alert, and WorkManager for any follow-up sync. On Android 17, talking to LAN devices also needs the local network permission."

**Key words:** `WebSocket` · `SSE` · `MQTT` · `QoS` · `retained message` · `Last Will` · `FCM data message` · `HTTP v1` · `ACCESS_LOCAL_NETWORK`

**Follow-up:**
- **Q:** Which MQTT QoS do you use for motion alerts?
  **A:** "QoS 1, because an alert must arrive at least once. I make the handler idempotent with an event id, so a duplicate does not show twice."
- **Q:** Can you keep a WebSocket open in the background for live alerts?
  **A:** "Not reliably. The system limits background work and Doze cuts the network. FCM is the right tool for background delivery."

**ভুল করবেন না:** "FCM real-time, instant guaranteed" বলবেন না — delivery-র সময় guaranteed না।

**আরও দেখুন:** [C15 · Notifications & push](#c15) · [N11 · MQTT](#n11) · [V9 · Motion alerts](#v9)

---

### <a id="r17"></a>R17. ○ Which design patterns do you use in Android? Why are singletons dangerous?

**প্রশ্নটা মানে:** Pattern-এর নাম মুখস্থ না, Android-এ আসল জায়গায় চেনেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Give examples of design patterns in the Android SDK." · "What is wrong with a global singleton?"

**বুঝে নিন:**

| Pattern | Android-এ কোথায় |
|---|---|
| **Builder** | `NotificationCompat.Builder`, `OkHttpClient.Builder`, `Retrofit.Builder`, `Room.databaseBuilder` |
| **Factory** | `ViewModelProvider.Factory`, Hilt-এর `@AssistedFactory`, `WorkerFactory` |
| **Observer** | `Flow`/`StateFlow`, `LifecycleObserver`, Compose state |
| **Adapter** | `RecyclerView.Adapter` (data → View), Retrofit `CallAdapter`/`Converter` |
| **Singleton** | Kotlin `object`, Hilt `@Singleton` |
| **Strategy** | `Interceptor` chain, Compose `Arrangement` |
| **Facade** | Repository (কয়েকটা data source একটা সহজ API-র পেছনে) |

**Singleton-এর বিপদ:**
- **Memory leak:** singleton-এ Activity `Context` বা View রাখলে Activity কখনো GC হয় না। শুধু `applicationContext`।
- **Hidden global state:** যে কেউ বদলাতে পারে → bug খোঁজা কঠিন।
- **Test কঠিন:** `object`-কে fake দিয়ে বদলানো যায় না; এক test-এর state পরের test-এ থেকে যায়।
- **Process death:** singleton-এর data চলে যায়, app ভাবে আছে।

**ঠিক উপায়:** Kotlin `object` না, Hilt `@Singleton` + constructor injection। তাহলে test-এ বদলানো যায়।

**Answer (English):**
> "Android uses many patterns. Builder in NotificationCompat and OkHttpClient, Factory in ViewModelProvider.Factory, Observer in Flow and lifecycle observers, Adapter in RecyclerView, and Facade in a repository that hides several data sources. Singletons are useful for one shared database or HTTP client, but they are risky. If a singleton holds an Activity context, it leaks the Activity. It also hides global state and makes tests hard, because you cannot swap it. So I do not use a Kotlin object for shared services. I use a Hilt Singleton with constructor injection, so tests can give a fake."

**Key words:** `Builder` · `Factory` · `Observer` · `Adapter` · `Facade` · `Singleton` · `memory leak` · `global state`

**Follow-up:**
- **Q:** When is a Kotlin object fine?
  **A:** "For pure stateless helpers or constants. If it has state or talks to the outside world, I inject it instead."

**আরও দেখুন:** [C11 · Context leaks](#c11) · [R5 · Hilt](#r5)

---

### <a id="r18"></a>R18. ◆ Explain SOLID with Android examples.

**প্রশ্নটা মানে:** প্রতিটা অক্ষর Android code-এ কোথায় দেখা যায়, ছোট করে বলতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Which SOLID principle do you use most?" · "Give a real example of dependency inversion."

**বুঝে নিন:**

| অক্ষর | মানে | Android উদাহরণ |
|---|---|---|
| **S** — Single responsibility | এক class, একটা কারণে বদলায় | ViewModel state রাখে; network parse করে mapper; DB-র কাজ DAO। "God Activity" নয়। |
| **O** — Open/closed | নতুন feature যোগ, পুরনো code না ছুঁয়ে | OkHttp-এ নতুন `Interceptor` যোগ করুন, client code বদলাতে হয় না। |
| **L** — Liskov substitution | subtype base-এর জায়গায় নিরাপদে বসে | `FakeCameraRepository` real-এর জায়গায় বসে, একই contract মানে (খালি list দেয়, exception না ছোড়ে যেখানে real ছোড়ে না)। |
| **I** — Interface segregation | ছোট, কাজভিত্তিক interface | `CameraReader` আর `CameraController` আলাদা। শুধু list দেখানো screen PTZ method পায় না। |
| **D** — Dependency inversion | high-level code abstraction-এর উপর নির্ভর করে | ViewModel `CameraRepository` interface চায়, Retrofit চেনে না। Hilt `@Binds` দিয়ে impl দেয়। |

- SOLID-কে অন্ধভাবে নয়: এক implementation-এর জন্য interface বানানো দরকার নেই, যদি না layer boundary বা test-এর জন্য লাগে।

**Answer (English):**
> "Single responsibility: the ViewModel holds state, the mapper converts data, and the DAO talks to the database. Open-closed: I add a new OkHttp interceptor without changing existing code. Liskov: my fake repository can replace the real one because it keeps the same contract. Interface segregation: I split a big camera interface into a reader and a controller, so a list screen does not see control methods. Dependency inversion: the ViewModel depends on a repository interface, and Hilt binds the real class. I use these as guides, not rules. I do not add an interface for one class unless a layer boundary or a test needs it."

**Key words:** `single responsibility` · `open-closed` · `Liskov` · `interface segregation` · `dependency inversion`

**Follow-up:**
- **Q:** Which one helps testing most?
  **A:** "Dependency inversion. If the ViewModel depends on an interface, I can give it a fake in tests, with no network and no database."

**আরও দেখুন:** [R3 · Clean Architecture](#r3) · [R17 · Design patterns](#r17)

---

### <a id="r20"></a>R20. ◆ Feature flags and remote config — how do you ship a feature safely?

**প্রশ্নটা মানে:** নতুন feature সবাইকে একসাথে না দিয়ে ধাপে ধাপে দেন কিনা, আর সমস্যা হলে নতুন release ছাড়াই বন্ধ করতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is a staged rollout?" · "How do you turn off a broken feature without a new release?"

**বুঝে নিন:**

Mobile app-এ release ফেরত নেওয়া যায় না। User-এর phone-এ update চলে গেলে সেটা থেকে যায়। তাই দুই স্তরে সাবধান থাকুন:

1. **Feature flag (remote config):** code app-এর ভেতরে থাকে, কিন্তু চালু/বন্ধ হয় server থেকে। Firebase Remote Config, নিজের config API, বা LaunchDarkly-র মতো tool।
2. **Play Console staged rollout:** নতুন version প্রথমে অল্প % user পায় (যেমন ১% → ১০% → ৫০% → ১০০%)। Crash/ANR বাড়লে rollout **halt** করা যায়। কিন্তু যারা update পেয়ে গেছে, তাদের কাছ থেকে ফেরত নেওয়া যায় না — fix সহ নতুন version (বড় `versionCode`) দিতে হয়।

**Flag-এর নিয়ম:**
- **Safe default:** network নেই বা fetch fail হলে flag-এর default মান = পুরনো, নিরাপদ পথ।
- Fetch করুন background-এ, শেষ মান cache করুন। App start আটকে রাখবেন না। Firebase Remote Config-এ default fetch interval ১২ ঘণ্টা; real-time update listener-ও আছে (docs দেখুন)।
- User screen-এ থাকা অবস্থায় flag বদলালে UI হঠাৎ বদলাবেন না। পরের app start বা পরের screen-এ নতুন মান লাগান।
- **Kill switch:** ঝুঁকির feature-এ (নতুন player, নতুন sync) একটা off flag রাখুন।
- Flag **security না।** Client-এর flag root/tamper করে বদলানো যায়। Paid feature বা private data-র access server-এ check করুন।
- Rollout শেষ হলে flag আর পুরনো code মুছুন। নইলে flag জমে code জটিল হয়।
- Rollout-এর সময় Crashlytics আর Play vitals দেখুন — version আর flag ধরে ভাগ করে।

```kotlin
class FeatureFlags @Inject constructor(private val remote: FirebaseRemoteConfig) {
    // safe default (false) is set with setDefaultsAsync at app start
    val isNewPlayerEnabled: Boolean
        get() = remote.getBoolean("new_player_enabled")
}
```

Flutter-এও একই: `firebase_remote_config` package, একই নিয়ম।

**Answer (English):**
> "I ship risky features behind a remote flag, so I can turn them off without a new release. The code is in the app, but the switch is on the server, for example Firebase Remote Config. The default value is always the old, safe path, so a failed fetch does no harm. I fetch in the background and never block app start. Then I release with a staged rollout in Play Console. I start with a small percent of users and watch crash and ANR rates. If they go up, I halt the rollout and turn the flag off. I never use a client flag for security, and I delete old flags after the rollout."

**Key words:** `feature flag` · `remote config` · `kill switch` · `safe default` · `staged rollout` · `halt rollout` · `Play vitals`

**Follow-up:**
- **Q:** Can you roll back an app version on Google Play?
  **A:** "Not really. I can halt a rollout, but users who already updated keep that version. So I ship a fix with a higher version code. That is why flags matter."
- **Q:** How do you test code behind a flag?
  **A:** "I inject the flags class and use a fake in tests. I test both the on path and the off path."

**ভুল করবেন না:** "Play-তে rollback করে দেব" বলবেন না — halt করা যায়, কিন্তু যাদের কাছে গেছে তাদের থেকে ফেরত নেওয়া যায় না।

**আরও দেখুন:** [P8 · Crash monitoring](#p8) · [P9 · CI/CD](#p9) · [P10 · Production bugs](#p10)

---


## <a id="part-6"></a>Part 6 — Flutter থেকে native Android: সেতুর প্রশ্ন

Interviewer আপনার CV দেখে জানে আপনি Flutter developer। তাই এই প্রশ্নগুলো প্রায় নিশ্চিত আসবে।
এখানে লক্ষ্য দুটো: সৎ থাকা, আর দেখানো যে Flutter-এর কাজেও আপনি Android platform-এর উপরেই কাজ করেছেন। দুর্বলতা লুকাবেন না। বলবেন কীভাবে দ্রুত শিখে নিচ্ছেন।

### আগে বুঝুন — Flutter app আসলে Android-এ কীভাবে চলে

**বড় ছবি (ধাপে ধাপে):**

1. Flutter app একটা সাধারণ **Android app** — APK/AAB, `AndroidManifest.xml`, Gradle build, signing, Play Console।
2. `MainActivity` হলো `FlutterActivity` — একটা সাধারণ Android `Activity`।
3. Activity-র ভেতরে একটা **`FlutterEngine`** চলে। Engine Dart VM চালায় আর নিজে UI draw করে (Impeller / Skia) একটা surface-এ।
4. Android-এর কাছে পুরো Flutter UI একটা view। Button, list — সব Flutter নিজে আঁকে, Android View না।
5. Camera, Bluetooth, sensor, notification — এসব Android API। Dart সরাসরি ডাকতে পারে না। তাই **plugin**: Dart side + Kotlin/Java side, মাঝে **platform channel** (বা FFI / JNIgen)।
6. Plugin-এর Kotlin অংশ একটা Android library module। Gradle সেটা app-এর সাথে build করে।

```
 Dart (Widgets, Riverpod)                Kotlin (Android SDK)
 ───────────────────────                 ────────────────────
 MethodChannel.invoke ──binary msg──▶ MethodCallHandler ──▶ CameraManager / SensorManager
 EventChannel.stream  ◀──binary msg── EventSink.success ◀── listener callback
                 FlutterEngine  (inside FlutterActivity)
```

**যে ৬টা idea মনে রাখবেন:**
- Manifest, permission, lifecycle, Play policy, target API, signing — **Flutter আর native-এ একই**। এই জ্ঞান সরাসরি কাজে লাগে।
- Platform channel async আর serialization-এর খরচ আছে। খুব বেশি frequency-র data (প্রতি frame) channel দিয়ে পাঠানো ব্যয়বহুল।
- Flutter 3.29 থেকে Android-এ Dart **main (platform) thread-এই চলে** — আলাদা UI thread নেই। তাই native handler-এ main thread আটকালে Flutter UI-ও আটকায়।
- Native code-এ আপনি Android-এর সব কিছু পান: background service, foreground service type, WorkManager, CameraX, Media3।
- Native-এ যা নতুন শিখতে হয়: **Compose**, coroutine/Flow, Hilt, Room, multi-module Gradle, View system (পুরনো code-এ)।
- Flutter-এ engine নিজে UI আঁকে; native-এ Compose-ও নিজে আঁকে কিন্তু Android-এর অংশ — accessibility, IME, system theme সরাসরি পায়।

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ rotation-এ সাধারণত Activity recreate হয় না (`configChanges`)। Native-এ default recreate — তাই ViewModel আর `SavedStateHandle` জরুরি।
- Dart-এ এক isolate-এ memory share হয় না। Kotlin coroutine-এ thread memory share করে — race condition নিজে সামলাতে হয় (`Mutex`, immutable state)।
- `pubspec.yaml`-এর জায়গায় Gradle (Kotlin DSL) + version catalog। Build config অনেক বেশি শক্তিশালী, কিন্তু জটিলও।
- Hot reload নেই। Compose Preview আর Live Edit আছে, কিন্তু Flutter-এর মতো সব জায়গায় না।

---

### <a id="b1"></a>B1. ★ You are a Flutter developer. Why should we trust you with native Android work?

**প্রশ্নটা মানে:** আপনার native অভিজ্ঞতা কতটা আসল, আর ফাঁক থাকলে সেটা আপনি জানেন কিনা ও কীভাবে পূরণ করবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Your CV is mostly Flutter. Why native now?" · "How strong is your Kotlin?"

**বুঝে নিন:**

উত্তরের চারটা অংশ রাখুন:
1. **একই platform:** Flutter app Android app-ই। Manifest, permission, lifecycle, Gradle, signing, Play Console, target API update, crash/ANR — এসব আপনি করেছেন।
2. **Native code লিখেছেন:** plugin বা platform channel-এ Kotlin — শুধু সত্যি যা করেছেন সেটাই বলুন (camera, sensor, notification, background কাজ ইত্যাদি)।
3. **Architecture জ্ঞান transfer হয়:** state management, layer, offline-first, testing — ধারণা একই, শুধু API আলাদা।
4. **ফাঁক আর plan:** কী কম জানেন (যেমন বড় View-based codebase, AOSP) সেটা সৎভাবে বলুন, আর কীভাবে দ্রুত শিখছেন।

**যা বলবেন না:** মিথ্যা native বছর, মিথ্যা project। Interviewer একটা follow-up দিয়েই ধরে ফেলবে।

**Answer (English):**
> "A Flutter app is an Android app. For years I have handled the Android side myself: the manifest, permissions, Gradle, signing, target API updates, and Play Console issues. When Flutter could not do something, I wrote the Kotlin side through platform channels, so I have worked directly with Android APIs. Architecture also carries over: state, layers, offline-first data, and tests are the same ideas. What I am still building is depth in Compose, Hilt, and large native codebases. I am closing that gap on purpose, with real Kotlin projects and the official samples. I learn fast, and I would rather tell you my gaps honestly than surprise you later."

**Key words:** `same platform` · `platform channels` · `Kotlin` · `transferable architecture` · `honest gap` · `ramp-up plan`

**Follow-up:**
- **Q:** What was the hardest native part you wrote for a Flutter app?
  **A:** "(Pick one real case.) I would explain the Android API, the threading problem, and how I tested it. I keep it real and specific."
- **Q:** How long until you are fully productive?
  **A:** "I can fix bugs and build small features from the first weeks, because I know the platform. For deep areas of your codebase, I would pair with the team and read the code first."

**ভুল করবেন না:** "Flutter আর native একই, কোনো পার্থক্য নেই" বলবেন না — overconfident শোনায়। Gap স্বীকার করে plan বলুন।

**আরও দেখুন:** [B7 · Flutter → Android map](#b7) · [H0-3 · Why hire you](#h0-3) · [B2 · Flutter or native](#b2)

---

### <a id="b2"></a>B2. ★ Flutter or native Android — when do you choose native?

**প্রশ্নটা মানে:** আপনি tool-এর প্রেমে না পড়ে project-এর দরকার দেখে বেছে নেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why would a company build native instead of Flutter?" · "What are the limits of Flutter?"

**বুঝে নিন:**

**Native বেছে নিন যখন:**
- **Platform-এর গভীরে কাজ:** camera pipeline (Camera2/CameraX, frame analysis), RTSP/Media3 player, Bluetooth/USB, sensor stream, foreground service, background কাজ।
- **System / AOSP কাজ:** system app, privileged app (`priv-app`), custom ROM, HAL-এর সাথে কথা, platform signing। এখানে Flutter দিয়ে কাজ চলে না।
- **Only Android** (যেমন company-র নিজের device, kiosk, camera NVR box)। Cross-platform-এর লাভ নেই।
- **নতুন Android feature সাথে সাথে** দরকার (নতুন API, widget, Wear OS, Android Auto)।
- **App size / startup** খুব জরুরি।
- **OEM SDK** শুধু Android/Java-তে দেওয়া।

**Flutter বেছে নিন যখন:**
- Android + iOS দুটোই, একই UI, একটা team।
- UI-heavy business app, platform API কম।
- দ্রুত MVP।

**মাঝামাঝি:** Kotlin Multiplatform (logic share, UI native) বা add-to-app (native app-এ কিছু Flutter screen)।

**Answer (English):**
> "I choose native when the app lives close to the platform. For example, camera pipelines, live video, Bluetooth or USB, sensor streams, foreground services, or system and AOSP work like privileged apps. I also choose native when the product is Android only, like a company device, because cross-platform gives no gain there. Flutter is great when you need the same UI on Android and iOS with one team and the app is mostly business UI. The trade-off is clear: Flutter saves time on shared UI, but every deep platform feature needs a native bridge anyway. For a security camera product with a custom OS, I would pick native Android."

**Key words:** `platform depth` · `Android only` · `system app` · `cross-platform` · `native bridge` · `trade-off`

**Follow-up:**
- **Q:** Is Flutter slower than native?
  **A:** "For normal UI, users usually cannot tell. The cost shows up in heavy platform work, like passing many camera frames through a channel. That part should stay native."
- **Q:** Would you rewrite a working Flutter app in native?
  **A:** "Not without a real reason. I would first move only the hard platform parts to native and keep the rest."

**আরও দেখুন:** [B6 · KMP vs Flutter](#b6) · [B3 · Platform channels](#b3) · [O4 · System apps](#o4)

---

### <a id="b3"></a>B3. ★ How do platform channels work? How would you stream sensor data to Flutter?

**প্রশ্নটা মানে:** Flutter আর Android-এর মাঝে data কীভাবে যায়, thread-এর নিয়ম, আর type-safe উপায় জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between MethodChannel and EventChannel?" · "What is Pigeon and why use it?"

**বুঝে নিন:**

**তিন ধরনের channel:**
| Channel | কাজ | উদাহরণ |
|---|---|---|
| `MethodChannel` | এক বার call → এক উত্তর (async) | `startRecording()`, battery level |
| `EventChannel` | native → Dart **stream** | accelerometer, BLE scan result, connection state |
| `BasicMessageChannel` | দুই দিকে message, নিজের codec | custom protocol, string/binary message |

- Data `StandardMessageCodec` দিয়ে binary-তে serialize হয়: null, bool, int, double, String, `ByteArray`, List, Map।
- Channel name দুই দিকে **একই** হতে হবে। Typo = `MissingPluginException`।

**Thread-এর নিয়ম (Android):**
- Handler default-এ **main (platform) thread**-এ চলে। ভারী কাজ (file, network, decode) সেখানে করবেন না।
- Background-এ handler চালাতে: **Task Queue** — `binaryMessenger.makeBackgroundTaskQueue()` দিয়ে channel বানান।
- Native থেকে Dart-এ পাঠানো (`result.success`, `eventSink.success`, `invokeMethod`) **main thread থেকে** করুন। Background-এ থাকলে main `Looper`-এ post করুন।
- Flutter 3.29 থেকে Android-এ Dart main thread-এই চলে। তাই main thread block = Flutter UI জমে যায়, লম্বা হলে ANR।

**EventChannel দিয়ে sensor stream:**
```kotlin
class AccelStreamHandler(private val sm: SensorManager) :
    EventChannel.StreamHandler, SensorEventListener {
    private var sink: EventChannel.EventSink? = null

    override fun onListen(arguments: Any?, events: EventChannel.EventSink?) {
        sink = events
        val sensor = sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)
        if (sensor == null) { events?.error("NO_SENSOR", "No accelerometer", null); return }
        sm.registerListener(this, sensor, SensorManager.SENSOR_DELAY_GAME)
    }
    override fun onCancel(arguments: Any?) { sm.unregisterListener(this); sink = null }
    override fun onSensorChanged(e: SensorEvent) { sink?.success(e.values.toList()) }  // main thread
    override fun onAccuracyChanged(s: Sensor?, accuracy: Int) = Unit
}
// EventChannel(messenger, "app/accel").setStreamHandler(AccelStreamHandler(sm))
```
- Dart side-এ stream-এর listener না থাকলে `onCancel` → sensor বন্ধ → battery বাঁচে।
- খুব বেশি rate হলে native-এ batch করুন বা কমান, প্রতি event channel-এ পাঠাবেন না।

**Pigeon:**
- Dart-এ একটা API definition লেখেন → Pigeon Dart + Kotlin (+ Swift) code generate করে।
- লাভ: type-safe, channel name/typo-র ভুল নেই, `Map<String, dynamic>` cast নেই।
- Flutter docs এখন নতুন project-এ Pigeon, **FFIgen**, **JNIgen** recommend করে; raw channel থাকে low-level কাজে আর পুরনো code-এ।

**Answer (English):**
> "Platform channels send async binary messages between Dart and Kotlin. A MethodChannel is one call and one result, like start recording. An EventChannel is a stream from native to Dart, which I would use for sensor data: onListen registers the sensor listener, each reading goes to the event sink, and onCancel unregisters it. A BasicMessageChannel sends plain messages both ways with a codec. Handlers run on the main thread by default, so heavy work goes to a background task queue, and replies go back on the main thread. Since Flutter 3.29, Dart also runs on that main thread, so blocking it freezes the UI. For new code I use Pigeon, because it generates type-safe code on both sides."

**Key words:** `MethodChannel` · `EventChannel` · `BasicMessageChannel` · `StandardMessageCodec` · `TaskQueue` · `main thread` · `Pigeon`

**Follow-up:**
- **Q:** The sensor sends 200 events per second. Is a channel OK?
  **A:** "It works, but each message has a serialization cost. I would batch readings in native code, or process them natively and send only the result."
- **Q:** What happens if you call the event sink from a background thread?
  **A:** "It can fail or crash, because channel messages to Dart must be sent from the main thread. I post to the main looper first."
- **Q:** What causes MissingPluginException?
  **A:** "The channel name does not match, the plugin is not registered on this engine, for example a second engine in add-to-app, or I added a plugin and only hot-restarted, so the native side was not rebuilt."

**ভুল করবেন না:** "Channel synchronous" বলবেন না — সবসময় async, আর data copy হয়।

**আরও দেখুন:** [N1 · Sensors](#n1) · [B4 · FFI & JNI](#b4) · [C12 · Main thread & ANR](#c12)

---

### <a id="b4"></a>B4. ◆ What are FFI, NDK and JNI? When would you write C or C++?

**প্রশ্নটা মানে:** Native (C/C++) layer-এর বেসিক জানেন কিনা, আর কখন দরকার — camera/video company-তে এটা আসে।
**অন্যভাবেও জিজ্ঞেস করে:** "How does Kotlin call C++ code?" · "What is dart:ffi?"

**বুঝে নিন:**

**শব্দগুলো:**
- **NDK:** Android-এ C/C++ build করার toolchain। CMake (বা ndk-build) দিয়ে `.so` library।
- **JNI:** Java/Kotlin ↔ C/C++ এর সেতু। Kotlin-এ `external fun`, C++-এ `Java_<package>_<Class>_<method>` function (বা `RegisterNatives`)।
- **dart:ffi:** Dart থেকে সরাসরি C function ডাকা। Channel নেই, **synchronous**, serialization নেই। `ffigen` header থেকে binding বানায়।
- **JNIgen:** Dart থেকে Java/Kotlin API সরাসরি ডাকার binding generate করে (JNI-র উপর)।
- Flutter 3.38 থেকে **build hooks** stable — Dart package নিজেই native code compile/bundle করতে পারে (`flutter create --template=package_ffi`)।

```kotlin
class FrameFilter {
    external fun denoise(frame: ByteBuffer, width: Int, height: Int)
    companion object { init { System.loadLibrary("framefilter") } }
}
```

**কখন C/C++:**
- আগে থেকে C/C++ library আছে: FFmpeg, OpenCV, codec, crypto, vendor SDK।
- Video frame / image processing, sensor DSP — যেখানে প্রতি frame-এ ভারী গণিত।
- Low-latency audio (Oboe)।
- Android, iOS, firmware-এর মধ্যে একই core code share।

**খরচ:**
- Native crash (SIGSEGV) — debug কঠিন, symbol upload লাগে।
- প্রতি JNI call-এ খরচ আছে — ছোট ছোট অনেক call না করে বড় batch (`ByteBuffer` direct buffer)।
- ABI (`arm64-v8a`, `x86_64`) অনুযায়ী `.so`, app size বাড়ে।
- **16 KB page size:** Android 15+ target করা Play app-এ native code থাকলে 16 KB page support লাগে — নতুন NDK/AGP দিয়ে rebuild।
- Memory safety নিজের দায়িত্ব।

**Answer (English):**
> "The NDK lets me build C and C++ code into a .so library for Android. JNI is the bridge: I declare an external function in Kotlin and implement it in C++. In Flutter, dart:ffi calls C functions directly and synchronously, with no channel, and ffigen makes the bindings. I write C or C++ only when there is a clear reason: an existing library like FFmpeg or OpenCV, heavy per-frame video or sensor processing, low-latency audio, or code shared with firmware or iOS. The cost is real: native crashes are harder to debug, each JNI call has overhead, and the app size grows. Also, apps with native code must support 16 KB memory pages, so I build with a recent NDK."

**Key words:** `NDK` · `JNI` · `external fun` · `System.loadLibrary` · `dart:ffi` · `ffigen` · `JNIgen` · `16 KB page size` · `ABI`

**Follow-up:**
- **Q:** How do you pass a camera frame to C++ without copying?
  **A:** "I use a direct ByteBuffer, or the plane buffers from the image, and read them in C++ with GetDirectBufferAddress. I process the whole frame in one call."
- **Q:** How do you debug a native crash from Play?
  **A:** "I upload native debug symbols to Play Console, so the stack trace shows function names. Locally I use the Android Studio native debugger and address sanitizers."

**আরও দেখুন:** [B3 · Platform channels](#b3) · [V8 · On-device AI](#v8)

---

### <a id="b5"></a>B5. ◆ How do you add Flutter screens to an existing native Android app?

**প্রশ্নটা মানে:** Add-to-app-এর setup, engine-এর খরচ আর caching বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "What is FlutterEngine caching?" · "How do you share one Flutter module between Android and iOS apps?"

**বুঝে নিন:**

**Setup:**
- `flutter create -t module my_flutter` → একটা Flutter module।
- Android app-এ যোগ: **AAR** হিসেবে (`flutter build aar`, native team-এর Flutter SDK লাগে না) বা **source** হিসেবে (Gradle-এ include, development সহজ)।

**দেখানো:**
- `FlutterActivity` (full screen), `FlutterFragment` (screen-এর অংশ), বা `FlutterView` (নিজে control)।

**Engine-এর খরচ:**
- নতুন `FlutterEngine` চালু করতে সময় আর memory লাগে (Dart VM, isolate, first frame)। প্রতি বার নতুন engine → প্রথম screen দেরিতে আসে।
- **Pre-warm + cache:** `Application.onCreate()`-এ engine বানান, Dart entrypoint চালান, `FlutterEngineCache`-এ রাখুন। পরে `FlutterActivity.withCachedEngine(id)`।
- Pre-warm করলে memory সবসময় ধরা থাকে — trade-off।
- কয়েকটা Flutter screen আলাদা জায়গায় → **`FlutterEngineGroup`**: engine-গুলো resource share করে, প্রতি নতুন engine সস্তা।

```kotlin
class App : Application() {
    override fun onCreate() {
        super.onCreate()
        val engine = FlutterEngine(this).apply {
            dartExecutor.executeDartEntrypoint(DartExecutor.DartEntrypoint.createDefault())
        }
        FlutterEngineCache.getInstance().put("main", engine)
    }
}
// startActivity(FlutterActivity.withCachedEngine("main").build(context))
```

**খেয়াল রাখুন:**
- Navigation দুই জায়গায় (native back stack + Flutter Navigator) — back button কে handle করবে ঠিক করুন।
- Data/auth share: platform channel বা Pigeon দিয়ে native-এর token/repository Flutter-এ দিন, Flutter-এ আবার login না।
- App size বাড়ে (Flutter engine + Dart code)।
- এক app-এ একটাই Flutter version।

**Answer (English):**
> "I create a Flutter module and add it to the Android app, as an AAR if the native team should not need the Flutter SDK, or as source for easier development. I show it with FlutterActivity, FlutterFragment, or FlutterView. Starting a FlutterEngine takes time and memory, so I pre-warm one in Application onCreate, store it in FlutterEngineCache, and open the screen with withCachedEngine. The first screen then opens fast. The trade-off is that the warm engine uses memory all the time. If I need Flutter in several places, I use FlutterEngineGroup so the engines share resources. I also plan the back navigation and pass auth from native through Pigeon."

**Key words:** `Flutter module` · `AAR` · `FlutterActivity` · `FlutterFragment` · `FlutterEngineCache` · `withCachedEngine` · `FlutterEngineGroup` · `pre-warm`

**Follow-up:**
- **Q:** Why not create a new engine every time?
  **A:** "Each new engine starts the Dart VM work again, so the user sees a delay and memory jumps. A cached or grouped engine avoids that."

**আরও দেখুন:** [B3 · Platform channels](#b3) · [B6 · KMP vs Flutter](#b6)

---

### <a id="b6"></a>B6. ◆ Kotlin Multiplatform or Flutter — an honest comparison.

**প্রশ্নটা মানে:** আপনি শুধু Flutter-এর পক্ষে কথা বলবেন, নাকি দুটোর trade-off সৎভাবে বলতে পারবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Why is Google pushing KMP?" · "If we start an iOS app, would you use KMP or Flutter?"

**বুঝে নিন:**

| | Kotlin Multiplatform (KMP) | Flutter |
|---|---|---|
| কী share হয় | business logic (network, DB, rules); UI চাইলে Compose Multiplatform দিয়ে | UI + logic সব |
| UI | native (Compose / SwiftUI) বা Compose Multiplatform | Flutter নিজের engine-এ আঁকে |
| ভাষা | Kotlin | Dart |
| Native API | Android-এ সরাসরি; iOS-এ Kotlin থেকে Apple API (interop) | plugin / channel / FFI দিয়ে |
| Google-এর অবস্থান | shared business logic-এর জন্য officially supported; Room, DataStore, Paging, ViewModel KMP-তে চলে | Google-এর নিজের framework |
| পুরনো native app-এ যোগ | ধীরে ধীরে, module ধরে | add-to-app, তবে engine-এর খরচ |
| Compose Multiplatform iOS | stable (2025) | — |

**কখন কোনটা:**
- **আগে থেকে native Android app আছে**, iOS-ও লাগবে → KMP। Logic share, UI native রাখা যায়।
- **নতুন app, এক team, UI share করে দ্রুত** → Flutter।
- Platform-এর গভীর কাজ বেশি → KMP (Android side পুরো native)।
- Team-এর skill বড় বিষয় — Dart team থাকলে Flutter, Kotlin team থাকলে KMP।

**Answer (English):**
> "They solve different problems. Kotlin Multiplatform shares business logic in Kotlin and lets each platform keep a native UI, or share UI with Compose Multiplatform, which is now stable on iOS. Google supports KMP officially for shared logic, and Room, DataStore, and ViewModel work with it. Flutter shares everything, UI and logic, with its own rendering engine, so it is faster for one team building the same UI twice. If a company already has a native Android app and wants iOS, I would pick KMP, because it can be added module by module. For a new UI-heavy app with one small team, Flutter is often faster. I know Flutter deeply, and KMP feels natural because it is just Kotlin."

**Key words:** `Kotlin Multiplatform` · `shared business logic` · `Compose Multiplatform` · `native UI` · `expect/actual` · `team skills`

**Follow-up:**
- **Q:** What is expect/actual?
  **A:** "In common code I declare an expect function or class, and each platform gives the actual implementation, for example a different UUID or file API on Android and iOS."
- **Q:** What is the weak side of KMP?
  **A:** "iOS developers must work with a Kotlin library, and the iOS tooling and debugging are less smooth than pure Swift. It is improving, but it is a real cost."

**আরও দেখুন:** [B2 · Flutter or native](#b2) · [B5 · Add-to-app](#b5)

---

### <a id="b7"></a>B7. ◆ Map Flutter concepts to Android. How did you ramp up on native Android?

**প্রশ্নটা মানে:** আপনার Flutter জ্ঞান native-এ কীভাবে কাজে লাগাচ্ছেন — আর শেখার একটা পরিষ্কার plan আছে কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you learn a new platform fast?" · "What was hardest when you moved to Compose?"

**বুঝে নিন:**

এই table মুখস্থ না — প্রতিটা লাইনের "কী আলাদা" অংশটাই interview-এ কাজে লাগে।

| Flutter | Android (native) | কী আলাদা / খেয়াল রাখুন |
|---|---|---|
| `Widget` | `@Composable` function | Composable কোনো object return করে না, UI emit করে। Widget tree-র মতো element/render tree আপনি দেখেন না। |
| `StatelessWidget` / `StatefulWidget` | stateless composable / `remember { mutableStateOf() }` | State composable-এর ভেতরে `remember`-এ থাকে। Screen-level state ViewModel-এ। |
| `setState` | `MutableState` লিখলে recomposition | শুধু যে composable state পড়ে সেটাই আবার চলে। Strong skipping default-এ on। |
| Riverpod / Bloc / Provider | `ViewModel` + `StateFlow` + `collectAsStateWithLifecycle()` | ViewModel rotation পার হয়। Lifecycle-aware collect না করলে background-এও কাজ চলে। |
| `Future` + `async/await` | `suspend fun` | Structured concurrency: scope cancel হলে child-ও cancel। |
| `Stream` / `StreamController` | `Flow` / `MutableSharedFlow` / `Channel` | Flow cold; `StateFlow` সবসময় একটা value রাখে। |
| `ValueNotifier` | `StateFlow` / `MutableState` | `StateFlow` একই value দুবার emit করে না। |
| `Isolate` / `compute()` | coroutine on `Dispatchers.Default` | Isolate memory share করে না; coroutine thread memory share করে — race condition সম্ভব। |
| `Navigator` / `go_router` | Navigation Compose (type-safe `@Serializable` route) / Navigation 3 | Navigation 3-এ back stack আপনার নিজের list (stable since late 2025)। |
| `InheritedWidget` / `BuildContext` lookup | `CompositionLocal` | বেশি ব্যবহার না করে parameter দিয়ে পাঠানো ভালো। |
| `ListView.builder` | `LazyColumn` + `items(key = …)` | Stable key দিন, নইলে state ভুল item-এ যায়। |
| `ThemeData` | `MaterialTheme` (Material 3) | Dynamic color (Android 12+) native-এ সহজ। |
| `WidgetsBindingObserver` / `AppLifecycleState` | `Lifecycle` / `LifecycleObserver` / `ProcessLifecycleOwner` | Activity আর process lifecycle আলাদা। |
| `pubspec.yaml` | `build.gradle.kts` + `libs.versions.toml` | Gradle-এ build type, flavor, module — অনেক বেশি control। |
| flavors | `productFlavors` + `buildTypes` | Build variant = flavor × build type। |
| `get_it` / Riverpod DI | Hilt | Graph compile time-এ check হয়। |
| `sqflite` / `drift` | Room | Migration test লিখতেই হবে। |
| `shared_preferences` | DataStore | Flow-based, atomic write। |
| `dio` | Retrofit + OkHttp | Interceptor/Authenticator একই ধারণা। |
| `json_serializable` | kotlinx.serialization | আলাদা build_runner লাগে না। |
| widget test / golden test | Compose UI test / screenshot test | Robolectric দিয়ে JVM-এ চলে। |
| `mocktail` | MockK (তবে fake আগে) | একই নীতি। |
| platform channel | সরাসরি Android API call | Bridge নেই — native-এর বড় সুবিধা। |
| hot reload | Compose Preview, Live Edit, Apply Changes | Flutter-এর মতো দ্রুত না; preview-driven কাজের অভ্যাস করুন। |

**Ramp-up plan (সৎভাবে যা করছেন সেটাই বলুন):**
1. Official guide পড়া: "Guide to app architecture", Compose basics, coroutines/Flow।
2. Now in Android sample-এর code পড়া — module, convention plugin, test।
3. একটা ছোট আসল app: Compose + ViewModel + Hilt + Room + Retrofit + WorkManager, test সহ।
4. নিজের একটা Flutter plugin feature (যেমন sensor বা camera) পুরো native-এ আবার লেখা।
5. Target domain-এ: CameraX, Media3 (RTSP), foreground service, permission flow।

**Answer (English):**
> "I mapped what I already knew to the native tools. Widgets became composables, Riverpod became ViewModel with StateFlow, Futures became suspend functions, Streams became Flow, and drift became Room. Then I focused on what is really different. A ViewModel survives rotation. Coroutines share memory, unlike isolates, so I must think about thread safety. Gradle gives much more control than pubspec. To learn, I read the official architecture guide and the Now in Android sample, built a small app with Compose, Hilt, Room, and Retrofit with tests, and rewrote one of my Flutter plugin features fully in Kotlin. The hardest part was thinking in recomposition and lifecycle-aware collection."

**Key words:** `concept mapping` · `Composable` · `StateFlow` · `suspend` · `Flow` · `Dispatchers.Default` · `Navigation Compose` · `Now in Android` · `ramp-up plan`

**Follow-up:**
- **Q:** What surprised you most moving from Flutter to Compose?
  **A:** "In Flutter I rebuild a widget and see it. In Compose, recomposition is automatic and can skip work, so I had to learn which state each composable reads, and to keep parameters stable."
- **Q:** Is an Isolate the same as a coroutine?
  **A:** "No. An isolate has its own memory and talks by messages. Coroutines on Dispatchers.Default run on a shared thread pool with shared memory, so I protect shared state with immutable data or a Mutex."

**ভুল করবেন না:** "শুধু syntax আলাদা, বাকি সব একই" বলবেন না — lifecycle, threading আর Gradle-এর পার্থক্যই interviewer শুনতে চায়।

**আরও দেখুন:** [B1 · Trust as Flutter dev](#b1) · [K8 · Coroutines](#k8) · [U2 · Recomposition](#u2)

---


## <a id="part-7"></a>Part 7 — Security: কয়েক স্তরের নিরাপত্তা (multi-layer security)

এই কোম্পানি security camera বানায়। তাদের app-এ থাকে user-এর ঘরের live video। এই data লিক হলে বড় ক্ষতি, আর কোম্পানির নামও নষ্ট হয়।
তাই interview-এ তারা দেখবে: আপনি কি শুধু একটা library-র নাম জানেন, নাকি পুরো chain ধরে ভাবেন — device, app, storage, network, server, মানুষ।
এই part-এ প্রতিটা স্তর আলাদা করে শিখবেন। শেষে নিজের ভাষায় একটা পূর্ণ ছবি বলতে পারবেন।

### আগে বুঝুন — multi-layer security-র বড় ছবি

**মূল কথা:** কোনো একটা check একা যথেষ্ট না। প্রতিটা স্তর ধরে নেয় যে আগের স্তর ভেঙে যেতে পারে। একে বলে **defense in depth**।

**স্তরগুলো (উপর থেকে নিচে):**

```
User / মানুষ        → phishing, দুর্বল password, shared phone
Device / OS         → root, malware, verified boot, SELinux, patch level
App (APK)           → reverse engineering, exported component, WebView, tamper
Data at rest        → token, DB, file, backup, log, screenshot
Network             → TLS, pinning, CT, local network (LAN camera)
Backend             → auth, authorization, rate limit, integrity verdict check
Camera hardware     → default password, firmware signing, stream security
```

**যে ৮টা ধারণার উপর সব দাঁড়িয়ে:**

1. **Client-কে বিশ্বাস করবেন না।** APK attacker-এর হাতে। Rooted phone-এ সে সব code বদলাতে পারে। আসল সিদ্ধান্ত (কে কোন camera দেখতে পারবে) সবসময় **server** নেয়।
2. **Secret client-এ লুকানো যায় না।** APK-তে রাখা API key, R8 দিয়েও, বের করা যায়। Client-এ রাখা যায় শুধু **user-এর নিজের** token, আর সেটাও Keystore-wrapped key দিয়ে encrypt করে।
3. **Android Keystore** = key hardware-এর ভেতরে (TEE বা StrongBox)। Key বের করা যায় না (non-exportable)। App শুধু "এই data encrypt/sign করো" বলতে পারে।
4. **Tink** = Google-এর crypto library। ভুল করা কঠিন। `EncryptedSharedPreferences` (security-crypto) এখন **deprecated** — নতুন code-এ Keystore + Tink।
5. **Network:** TLS সবসময়। Android 9 থেকে cleartext HTTP default-এ বন্ধ। দরকার হলে **certificate pinning**, backup pin সহ। Android 17 target করলে **certificate transparency default চালু**।
6. **Auth:** OAuth 2.0 + PKCE, browser-এ (Custom Tabs)। ছোট-মেয়াদি access token, refresh token rotation। Passkey-র জন্য **Credential Manager**।
7. **Integrity:** SafetyNet বন্ধ (২০২৫-এর জানুয়ারি)। এখন **Play Integrity API**, আর verdict **server-এ** যাচাই। শুধু client-এ root check সহজে bypass হয়।
8. **Platform surface:** exported component, PendingIntent, WebView, backup, notification, screenshot — এগুলো দিয়েই সবচেয়ে বেশি লিক হয়।

**Standard:** OWASP **MASVS** (কী থাকা উচিত) আর **MASTG** (কীভাবে test করবেন)। MASVS v2-এর ভাগগুলো: STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, PRIVACY। Interview-এ এই নাম বললে বোঝা যায় আপনি structure মেনে কাজ করেন।

**Custom hardware (নিজেদের AOSP device) হলে আরও স্তর:** verified boot, SELinux enforcing, `user` build-এ adb বন্ধ, নিজের release key দিয়ে signing (AOSP-র test key না), signed OTA। আর এই device-এ Google Play services না থাকলে Play Integrity কাজ করবে না — তখন hardware **key attestation** নিজে যাচাই করতে হয়।

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ আপনি হয়তো `flutter_secure_storage` ব্যবহার করেছেন। পুরনো version-এ Android-এ `encryptedSharedPreferences: true` দিলে এটা `EncryptedSharedPreferences` ব্যবহার করত। v10-এ সেই option deprecated, v11-এ বাদ — এখন নিজের cipher (Keystore key + AES-GCM) দিয়ে SharedPreferences-এ রাখে। Native-এ আপনি সাধারণত সরাসরি Keystore + Tink দেখবেন।
- Dart code `libapp.so`-তে AOT হয়ে যায়, তাই পড়া একটু কঠিন। Kotlin code `jadx` দিয়ে প্রায় source-এর মতো পড়া যায়। তাই native-এ obfuscation-এর উপর ভরসা আরও কম।
- Manifest-এর component (`exported`, permission, intent filter) native-এ আপনার সরাসরি দায়িত্ব। Flutter-এ এগুলো প্রায়ই plugin লুকিয়ে রাখত।
- `network_security_config.xml`, backup rules, `FLAG_SECURE` — এগুলো Flutter app-এও একই, কিন্তু native interview-এ খুঁটিনাটি জিজ্ঞেস করে।

---

### <a id="s1"></a>S1. ★ How do you secure an Android app?

**প্রশ্নটা মানে:** আপনি কি পুরো system স্তর ধরে ভাবতে পারেন, নাকি শুধু "আমি HTTPS দিই" বলবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What is your security checklist for a new app?" · "What does defense in depth mean for mobile?"

**বুঝে নিন:**
- উত্তর সাজান **স্তর ধরে**, আর প্রতিটা স্তরে ১টা concrete কাজ বলুন:

| স্তর | কী করি |
|---|---|
| Device | Play Integrity verdict server-এ check; risky device-এ sensitive feature সীমিত |
| App | R8, exported component কমানো, PendingIntent immutable, WebView lock down |
| Data at rest | token Keystore-wrapped key + Tink দিয়ে encrypt; backup rules; `FLAG_SECURE` |
| Network | TLS only, cleartext বন্ধ, দরকারে pinning (backup pin), CT |
| Backend | প্রতি request-এ authorization, ছোট token, rate limit, audit log |
| People | passkey / MFA, phishing-resistant login, sensitive কাজে biometric step-up |

- শুরু করুন **threat model** দিয়ে: কী রক্ষা করছি (live video, recording, account), কার থেকে (চোর, malware app, নেটওয়ার্কে বসা লোক, rooted phone-এর মালিক নিজে), আর ক্ষতি কত বড়।
- Checklist: OWASP **MASVS**। কতটা কড়া হবেন, তার জন্য MAS testing profile আছে: L1 = সব app, L2 = বেশি sensitive app, R = resilience/anti-tamper। Camera app সাধারণত L2-এর কাছাকাছি। ঝুঁকির সহজ list চাইলে OWASP Mobile Top 10 (S17)।
- মূল নিয়ম: client-এ যেকোনো check bypass হতে পারে। তাই **শেষ সিদ্ধান্ত server-এ**।
- Android 17 target করলে কিছু নতুন default আপনাআপনি পাবেন: certificate transparency, ECH (TLS-এ SNI encrypt, library আর server support করলে), native library dynamic loading-এ read-only নিয়ম।

**Answer (English):**
> "I think in layers, because any single check can fail. First I write a short threat model: what we protect, like live video and the account, and who attacks it. Then I cover each layer. On the device, I check Play Integrity on the server. In the app, I keep components private and use R8. Data at rest is encrypted with a Keystore-backed key and Tink. On the network, I use TLS only, and pinning where it makes sense. The backend checks permission on every request. The main trade-off is that the client can always be broken, so the server makes the final decision. I use OWASP MASVS as my checklist."

**Key words:** `defense in depth` · `threat model` · `OWASP MASVS` · `server-side authorization`

**Follow-up:**
- **Q:** Which layer is the most important?
  **A:** "The backend. If the server checks who can see each camera on every request, a broken client cannot see other people's video."
- **Q:** How do you decide how much security is enough?
  **A:** "I look at the data and the risk. For live home video I aim near the MAS L2 level, and I add resilience checks only where they slow a real attack."
- **Q:** What is MASVS and MASTG?
  **A:** "MASVS is the OWASP list of security requirements for mobile apps. MASTG is the testing guide that shows how to check each requirement."

**ভুল করবেন না:** শুধু "HTTPS আর ProGuard" বলে থামবেন না — interviewer স্তর আর server-side check শুনতে চায়।

**আরও দেখুন:** [S17 · OWASP Mobile Top 10](#s17) · [F13 · Platform security model](#f13) · [D1 · Security camera app design](#d1)

---

### <a id="s17"></a>S17. ◆ What are the OWASP Mobile Top 10 risks?

**প্রশ্নটা মানে:** Mobile app-এর সবচেয়ে common ১০টা security ঝুঁকির list জানেন কিনা, আর প্রতিটার জন্য Android-এ কী করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What is the difference between the OWASP Mobile Top 10 and MASVS?" · "Name a few common mobile security risks."

**বুঝে নিন:**
- **Top 10** = awareness list — কোথায় সবচেয়ে বেশি ভুল হয়। **MASVS** = requirement checklist। **MASTG** = test guide। এই পার্থক্যটা বলতে পারলেই ভালো শোনায়।
- শেষ final list ২০২৪-এর। নতুন version এসেছে কিনা owasp.org-এ দেখে নিন।

| # | Risk | Android-এ আমি কী করি |
|---|---|---|
| M1 | Improper Credential Usage | APK-তে hardcoded key না; token Keystore + Tink দিয়ে (S2) |
| M2 | Inadequate Supply Chain Security | dependency scan আর verification, signing key সাবধানে রাখা (S16) |
| M3 | Insecure Authentication / Authorization | OAuth + PKCE; server প্রতি request-এ access check করে (S6) |
| M4 | Insufficient Input/Output Validation | intent extra, deep link, WebView, SQL — বাইরের সব input check (S9, S10) |
| M5 | Insecure Communication | শুধু TLS, দরকারে pinning (S5) |
| M6 | Inadequate Privacy Controls | কম data নেওয়া; log আর lock screen-এ private data না (S11) |
| M7 | Insufficient Binary Protections | R8, Play Integrity; কিন্তু secret server-এ (S7, S8) |
| M8 | Security Misconfiguration | exported component, backup, cleartext, `debuggable` ভুল setting (S9) |
| M9 | Insecure Data Storage | DB আর file encrypt, backup rules (S11) |
| M10 | Insufficient Cryptography | নিজের crypto বানাই না; Tink, AES-GCM; MD5 বা ECB না |

- নম্বর মুখস্থ লাগবে না। ৪–৫টা নাম আর প্রতিটার জন্য একটা concrete কাজ বলুন।
- Camera app-এ সবচেয়ে বড় ঝুঁকি: M3 (id বদলে অন্যের camera দেখা — IDOR), M1, M5।

**Answer (English):**
> "The OWASP Mobile Top 10 is a list of the most common mobile app risks. The latest final list is from 2024. It starts with improper credential usage, like keys hardcoded in the APK. Then come supply chain security and insecure authentication and authorization. It also covers input validation, insecure communication, privacy, binary protection, misconfiguration, insecure data storage and weak cryptography. I use it as an awareness list, and MASVS as the real checklist. For a camera app, the biggest risks are broken authorization, like seeing someone else's camera, and leaked credentials. So I keep secrets on the server and check access on every request."

**Key words:** `OWASP Mobile Top 10` · `improper credential usage` · `MASVS` · `broken authorization` · `IDOR`

**Follow-up:**
- **Q:** What is the difference between the Top 10 and MASVS?
  **A:** "The Top 10 says what goes wrong most often. MASVS says what a secure app must do, and MASTG shows how to test it."
- **Q:** Which risk do you see most in real apps?
  **A:** "Hardcoded secrets and weak access checks on the server. Both are easy to find with jadx and a proxy."

**ভুল করবেন না:** Web-এর OWASP Top 10 (SQL injection, XSS...) আর Mobile Top 10 গুলিয়ে ফেলবেন না — দুটো আলাদা list।

**আরও দেখুন:** [S1 · Secure an app](#s1) · [S14 · Security testing](#s14) · [S16 · Supply chain](#s16)

---

### <a id="s2"></a>S2. ★ Where do you store tokens and secrets?

**প্রশ্নটা মানে:** আপনি কি জানেন কোনটা client-এ রাখা যায়, কোনটা কখনোই না, আর ২০২৬-এর সঠিক tool কোনটা।
**অন্যভাবেও জিজ্ঞেস করে:** "Is EncryptedSharedPreferences still the right choice?" · "How do you protect an API key in the app?"

**বুঝে নিন:**
- **দুই ধরনের secret:**
  - **App-wide secret** (third-party API key, signing secret, admin key): client-এ নিরাপদ রাখা **যায় না**। APK খুললেই পাওয়া যায় — `BuildConfig`, `strings.xml`, native `.so`, এমনকি runtime-এ Frida দিয়ে memory থেকে। উপায় একটাই: secret **server-এ** রাখুন। App server-কে call করবে, server third-party-কে।
  - **User-এর নিজের secret** (access/refresh token): রাখতে হয়, কিন্তু encrypt করে।
- **২০২৬-এর সঠিক পথ:**
  - `androidx.security:security-crypto` (`EncryptedSharedPreferences`, `EncryptedFile`) **deprecated**। নতুন code-এ নয়।
  - Keystore-এ একটা AES key (বা Tink keyset-কে wrap করার master key) → **Tink** `Aead` দিয়ে value encrypt → **DataStore**-এ রাখুন।
  - DataStore **1.3.0 (stable, 21 Oct 2026)**-এ নতুন `androidx.datastore:datastore-tink` artifact এসেছে। এর `AeadSerializer` আপনার serializer-কে wrap করে পুরো DataStore file Tink `Aead` দিয়ে encrypt করে।
- **StrongBox:** আলাদা secure chip। বেশি নিরাপদ, কিন্তু ধীর আর সব phone-এ নেই। `setIsStrongBoxBacked(true)` দিন, `StrongBoxUnavailableException` পেলে TEE-তে fallback।
- **Client কখনো কী রাখতে পারে না:** server-এর private key, অন্য user-এর data দেখার "admin" flag, payment secret, camera-র master password।

```kotlin
AeadConfig.register()
val handle = AndroidKeysetManager.Builder()
    .withSharedPref(context, "token_keyset", "secure_prefs")
    .withKeyTemplate(KeyTemplates.get("AES256_GCM"))
    .withMasterKeyUri("android-keystore://token_master_key")
    .build().keysetHandle
val aead = handle.getPrimitive(RegistryConfiguration.get(), Aead::class.java)
val encrypted = aead.encrypt(token.toByteArray(), "auth_token".toByteArray())
// encrypted bytes → DataStore
```

- এখানে keyset নিজে Keystore master key দিয়ে encrypted থাকে। Associated data (`"auth_token"`) দিয়ে এক field-এর ciphertext অন্য field-এ বসানো আটকায়।

**Answer (English):**
> "First I split secrets into two kinds. App-wide secrets, like a third-party API key, cannot be kept safe in the client. Anyone can pull them from the APK, so I keep them on the server and the app calls my server. User secrets, like tokens, I store encrypted. I create a key in the Android Keystore, use Tink to encrypt the value, and save it in DataStore. I do not use EncryptedSharedPreferences in new code, because it is deprecated. If the device has StrongBox, I use it, with a fallback to the normal TEE. Even then, a rooted phone can read tokens at runtime, so I keep tokens short-lived."

**Key words:** `Android Keystore` · `Tink AEAD` · `StrongBox` · `no hardcoded secrets` · `DataStore`

**Follow-up:**
- **Q:** Why not just obfuscate the API key?
  **A:** "Obfuscation only slows people down. The app must use the key at runtime, so a tool like Frida can read it from memory."
- **Q:** What do you do with existing EncryptedSharedPreferences data?
  **A:** "It still works, so I migrate on app start: read the old value, write it with Tink into DataStore, then delete the old file. I test the migration path carefully, because a bug there logs users out."
- **Q:** What happens if the Keystore key is lost?
  **A:** "Data encrypted with it cannot be read anymore. So I treat local tokens as a cache: on failure I clear them and ask the user to log in again."

**ভুল করবেন না:** "EncryptedSharedPreferences ব্যবহার করি" বলবেন না নতুন app-এর জন্য — এটা পুরনো উত্তর।

**আরও দেখুন:** [S3 · Keystore](#s3) · [R8 · DataStore](#r8) · [S11 · Data at rest](#s11)

---

### <a id="s3"></a>S3. ◆ Can you explain the Android Keystore in depth?

**প্রশ্নটা মানে:** Keystore ভেতরে কীভাবে কাজ করে, key-কে কীভাবে শর্তে বাঁধা যায়, আর attestation কী প্রমাণ করে।
**অন্যভাবেও জিজ্ঞেস করে:** "What does hardware-backed key mean?" · "How can the server trust a key from the phone?"

**বুঝে নিন:**
- **Hardware-backed:** key তৈরি হয় আর থাকে **TEE** (KeyMint/Trusty-র মতো আলাদা secure OS) বা **StrongBox** chip-এ। Android OS key-এর bytes কখনো দেখে না। App শুধু operation চায়।
- **Non-exportable:** key বের করা যায় না। Root user-ও key copy করতে পারে না। তবে root user phone-এ বসে key **ব্যবহার** করাতে পারে — তাই user authentication শর্ত দরকার।
- **শর্ত দেওয়া যায় (`KeyGenParameterSpec`):**

| Setting | মানে |
|---|---|
| `setUserAuthenticationRequired(true)` | user biometric/PIN না দিলে key কাজ করবে না |
| `setUserAuthenticationParameters(0, AUTH_BIOMETRIC_STRONG)` | প্রতিবার auth লাগবে (timeout 0) |
| `setInvalidatedByBiometricEnrollment(true)` | নতুন fingerprint যোগ হলে key বাতিল |
| `setUnlockedDeviceRequired(true)` | phone lock থাকলে key কাজ করবে না |
| `setIsStrongBoxBacked(true)` | StrongBox chip-এ রাখো |

```kotlin
val spec = KeyGenParameterSpec.Builder("session_key",
        KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
    .setKeySize(256)
    .setUserAuthenticationRequired(true)
    .setUserAuthenticationParameters(0, KeyProperties.AUTH_BIOMETRIC_STRONG)
    .setInvalidatedByBiometricEnrollment(true)
    .build()
KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore")
    .apply { init(spec) }.generateKey()
```

- **Key attestation:** asymmetric key (EC/RSA) তৈরির সময় server-এর দেওয়া challenge দিন (`setAttestationChallenge(challenge)`)। Keystore একটা certificate chain দেয়, যা Google-এর attestation root পর্যন্ত যায়। Server chain যাচাই করে জানতে পারে:
  - key সত্যিই hardware-এ (TEE/StrongBox), software-এ না
  - challenge মিলছে (replay না)
  - verified boot state, bootloader locked কিনা, OS patch level
  - কোন app (package + signing cert) key বানিয়েছে
- Server-কে revocation list-ও check করতে হয়। Google root certificate সময়ের সাথে বদলায় — current root list docs থেকে নিন।
- **Camera company-র জন্য:** নিজেদের AOSP device-এ Play services না থাকলে attestation-ই device-কে চেনার মূল উপায়। Factory-তে attestation key provision ঠিক আছে কিনা (বা RKP) — এটা hardware team-এর সাথে দেখতে হয়।

**Answer (English):**
> "The Keystore keeps keys inside secure hardware, the TEE or StrongBox. The app never sees the key bytes. It only asks the hardware to encrypt or sign. Keys are non-exportable, so even root cannot copy them. I can bind a key to rules, for example the user must pass strong biometrics for each use, or the key dies when a new fingerprint is added. The weak point is that root can still use the key on the device, so I add user authentication for sensitive keys. For trust on the server, I use key attestation: the server sends a challenge and checks the certificate chain, the boot state, and which app made the key."

**Key words:** `TEE` · `StrongBox` · `non-exportable` · `KeyGenParameterSpec` · `key attestation`

**Follow-up:**
- **Q:** What is the difference between TEE and StrongBox?
  **A:** "TEE is a secure area on the main chip. StrongBox is a separate secure chip with its own CPU and storage. StrongBox is stronger but slower, and not every phone has it."
- **Q:** When do you use attestation in a real app?
  **A:** "For device binding. When a phone registers, the server checks the attested key and stores its public key. Later the phone signs requests with it, so a stolen token alone is not enough."

**ভুল করবেন না:** "Keystore মানে root-এ নিরাপদ" বলবেন না — key copy হয় না, কিন্তু rooted device-এ ব্যবহার করা যায়।

**আরও দেখুন:** [S4 · Biometric login](#s4) · [S7 · Play Integrity](#s7) · [O11 · Verified boot](#o11)

---

### <a id="s4"></a>S4. ★ How do you build biometric login?

**প্রশ্নটা মানে:** BiometricPrompt ঠিকভাবে ব্যবহার করতে পারেন কিনা, আর বোঝেন কিনা CryptoObject ছাড়া biometric শুধু একটা UI।
**অন্যভাবেও জিজ্ঞেস করে:** "What is CryptoObject and why does it matter?" · "BIOMETRIC_STRONG vs BIOMETRIC_WEAK?"

**বুঝে নিন:**
- **Library:** `androidx.biometric` এর `BiometricPrompt`। System dialog দেখায়, তাই সব phone-এ এক রকম।
- **Authenticator ধরন:**

| Type | মানে | Crypto ব্যবহার করা যায়? |
|---|---|---|
| `BIOMETRIC_STRONG` (Class 3) | কঠিন spoof-test পাস করা sensor | হ্যাঁ |
| `BIOMETRIC_WEAK` (Class 2) | কিছু face unlock ইত্যাদি | না |
| `DEVICE_CREDENTIAL` | PIN / pattern / password | হ্যাঁ (API 30+) |

- **CryptoObject কেন জরুরি:** CryptoObject ছাড়া app শুধু একটা callback পায় — "success"। Rooted phone-এ Frida দিয়ে সেই callback নকল করা যায়। CryptoObject থাকলে Keystore key **শুধু biometric পাস হলেই** unlock হয়। Callback নকল করলেও key কাজ করবে না, তাই token decrypt হবে না।
- **Flow:** login-এর পর refresh token একটা auth-required Keystore key দিয়ে encrypt করে রাখুন (S3)। পরে app খুললে `Cipher` init করুন → `BiometricPrompt`-এ CryptoObject দিন → success-এ সেই cipher দিয়ে decrypt।
- **Fallback:** `BIOMETRIC_STRONG or DEVICE_CREDENTIAL` দিলে user PIN দিতে পারে (API 30+; API 28–29-এ এই combination support নেই)। `DEVICE_CREDENTIAL` দিলে negative button দেওয়া যায় না। সবসময় **password দিয়ে login**-এর পথ রাখুন।
- **Edge case:** নতুন fingerprint যোগ হলে `KeyPermanentlyInvalidatedException` — key মুছে আবার login করান।
- আগে `BiometricManager.canAuthenticate(BIOMETRIC_STRONG)` দিয়ে check করুন।

```kotlin
val prompt = BiometricPrompt(activity, executor,
    object : BiometricPrompt.AuthenticationCallback() {
        override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
            val cipher = result.cryptoObject?.cipher ?: return
            val refreshToken = cipher.doFinal(encryptedToken)
            onUnlocked(refreshToken)
        }
    })
val info = BiometricPrompt.PromptInfo.Builder()
    .setTitle("Unlock your cameras")
    .setAllowedAuthenticators(BiometricManager.Authenticators.BIOMETRIC_STRONG)
    .setNegativeButtonText("Use password")
    .build()
prompt.authenticate(info, BiometricPrompt.CryptoObject(decryptCipher))
```

**Answer (English):**
> "I use BiometricPrompt from AndroidX with BIOMETRIC_STRONG. The key part is the CryptoObject. Without it, biometrics is only a yes or no callback, and on a rooted phone someone can fake that callback. With a CryptoObject, the Keystore key opens only after a real biometric match. So I encrypt the refresh token with an auth-bound key, and decrypt it inside the success callback. For fallback, I allow device PIN on Android 11 and up, and I always keep normal password login. If the user adds a new fingerprint, the key becomes invalid, so I clear it and ask for login again."

**Key words:** `BiometricPrompt` · `BIOMETRIC_STRONG` · `CryptoObject` · `KeyPermanentlyInvalidatedException` · `DEVICE_CREDENTIAL`

**Follow-up:**
- **Q:** Why not use BIOMETRIC_WEAK?
  **A:** "Weak biometrics cannot unlock Keystore keys, so I cannot use a CryptoObject. It is fine for a light screen lock, but not for unlocking tokens."
- **Q:** Where would you use biometrics in a camera app?
  **A:** "For step-up actions: opening live view after the app was idle, sharing a camera with someone, or deleting recordings. The server can send a challenge that the app signs with a biometric-bound key."
- **Q:** What if the device has no biometrics?
  **A:** "I check canAuthenticate first. If it is not available, I use device credential or the normal password flow."

**ভুল করবেন না:** CryptoObject ছাড়া শুধু `onAuthenticationSucceeded`-এ একটা boolean সেট করাকে "secure biometric login" বলবেন না।

**আরও দেখুন:** [S3 · Keystore](#s3) · [S6 · Login and auth](#s6)

---

### <a id="s5"></a>S5. ★ How do you secure network traffic?

**প্রশ্নটা মানে:** TLS, Network Security Config, pinning-এর ঝুঁকি, আর নতুন Android default (CT) জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Should we use certificate pinning?" · "How do you stop man-in-the-middle attacks?"

**বুঝে নিন:**
- **TLS সবসময়।** Target 28+ (Android 9) হলে cleartext HTTP default-এ বন্ধ। `cleartextTrafficPermitted="false"` রাখুন।
- **Network Security Config** (`res/xml/network_security_config.xml`): code ছাড়া XML দিয়ে trust নিয়ম — কোন domain-এ cleartext, কোন CA বিশ্বাস, pin-set, debug-only CA (`<debug-overrides>`)।
- Android 7+ target করলে app default-এ **user-installed CA বিশ্বাস করে না**। তাই সাধারণ user-এর phone-এ fake CA দিয়ে MITM কঠিন।
- **Certificate pinning:** server-এর public key-এর hash app-এ রাখা। অন্য CA-র দেওয়া valid cert-ও বাতিল।
  - **ঝুঁকি:** server team key বদলালে আর pin না মিললে **সব user-এর app কাজ বন্ধ**। App update ছাড়া ঠিক করা যায় না।
  - তাই: **leaf না, intermediate বা নিজের key-এর SPKI pin**, সবসময় **কমপক্ষে একটা backup pin** (আলাদা key, আগে থেকে তৈরি), আর XML-এ `expiration` তারিখ। Rotation plan server team-এর সাথে লিখে রাখুন।
- **Certificate Transparency (CT):** CA যে cert দেয়, তা public log-এ থাকতে হবে। ভুল করে বা চুরি করে দেওয়া cert ধরা পড়ে। Android 16-এ opt-in ছিল; **Android 17 target করলে default চালু**।
- **Android 17-এ ECH:** TLS handshake-এ domain নাম (SNI) encrypt হয়, যদি library আর server support করে। `<domainEncryption>` দিয়ে নিয়ন্ত্রণ।
- **Camera-specific:** LAN-এর camera প্রায়ই self-signed cert দেয়। এখানে public CA কাজ করে না। ভালো উপায়: pairing-এর সময় camera-র cert fingerprint নিয়ে রাখা (QR বা cloud থেকে), পরে সেটাই pin করা। "সব cert trust করো" কখনো না।
- **জানা কথা:** cleartext নিয়ম HTTP library মানে। Raw socket (যেমন RTSP) এই flag মানে না — তাই RTSP নিজে নিরাপদ না।

```xml
<network-security-config>
    <base-config cleartextTrafficPermitted="false" />
    <domain-config>
        <domain includeSubdomains="true">api.example.com</domain>
        <pin-set expiration="2027-06-30">
            <pin digest="SHA-256">PRIMARY_SPKI_HASH_BASE64=</pin>
            <pin digest="SHA-256">BACKUP_SPKI_HASH_BASE64=</pin>
        </pin-set>
    </domain-config>
</network-security-config>
```

- OkHttp-এ একই কাজ: `CertificatePinner.Builder().add("api.example.com", "sha256/...")` — দুইটা pin দিন।

**Answer (English):**
> "All traffic uses TLS, and cleartext is off in the Network Security Config. Apps targeting Android 7 and up do not trust user-added CAs, which already blocks simple man-in-the-middle tools. For high-risk APIs I add certificate pinning, but carefully. I pin the public key, not the leaf certificate, I always ship a backup pin, and I set an expiry date. The big risk is that a server key change can break every installed app, so the rotation plan must be agreed with the backend team. On Android 17, certificate transparency is on by default, which helps catch wrongly issued certificates. For LAN cameras with self-signed certificates, I pin the camera's own certificate during pairing."

**Key words:** `Network Security Config` · `certificate pinning` · `backup pin` · `certificate transparency` · `SPKI hash`

**Follow-up:**
- **Q:** Can pinning be bypassed?
  **A:** "Yes. On a rooted device, Frida or objection can turn it off. Pinning protects normal users on bad networks. It does not stop the phone owner."
- **Q:** How do you test with a proxy if pinning is on?
  **A:** "I use a debug build with debug-overrides that trusts my proxy CA. The release build never trusts it."
- **Q:** What happens if both pins are wrong after a server change?
  **A:** "Every request fails until users update. That is why the expiry date and a tested backup key matter."

**ভুল করবেন না:** backup pin ছাড়া pinning ship করবেন না — এটা পুরো app বন্ধ করার সবচেয়ে সহজ উপায়।

**আরও দেখুন:** [V10 · Secure streams](#v10) · [R9 · Retrofit and OkHttp](#r9) · [V7 · Find LAN cameras](#v7)

---

### <a id="s6"></a>S6. ★ How do you build login and auth securely?

**প্রশ্নটা মানে:** Mobile app-এর জন্য সঠিক OAuth flow, token-এর ধরন, আর passkey জানেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "Why not log in inside a WebView?" · "How do access and refresh tokens work together?"

**বুঝে নিন:**
- **OAuth 2.0 + PKCE** (Authorization Code flow): mobile app-এ client secret রাখা যায় না (public client)। PKCE তাই:
  1. App একটা random `code_verifier` বানায়, তার SHA-256 = `code_challenge`।
  2. Browser-এ login page খোলে challenge সহ।
  3. Redirect-এ `code` আসে। App `code` + `code_verifier` দিয়ে token নেয়।
  4. অন্য app `code` চুরি করলেও verifier নেই, তাই কাজে লাগে না।
- **Browser কেন, WebView কেন না:** WebView-এ app নিজেই password field পড়তে পারে (JS inject)। User-ও URL bar দেখে না। Google নিজের login WebView-এ block করে। তাই **Custom Tabs** — **AppAuth-Android** library এগুলো সামলায়। Redirect-এর জন্য **App Links** (verified https) custom scheme-এর চেয়ে ভালো।
- **Token:**

| | Access token | Refresh token |
|---|---|---|
| মেয়াদ | ছোট (মিনিট) | বড় (দিন/সপ্তাহ) |
| কোথায় যায় | প্রতিটা API call | শুধু token endpoint |
| চুরি হলে | অল্প সময় ক্ষতি | বড় ক্ষতি — তাই rotation |

- **Refresh token rotation:** প্রতিবার refresh-এ নতুন refresh token, পুরনোটা বাতিল। পুরনোটা আবার কেউ ব্যবহার করলে server বোঝে চুরি হয়েছে → ওই পুরো token family বাতিল।
- **Credential Manager** (`androidx.credentials`): password, **passkey**, আর Sign in with Google এক API-তে। পুরনো Google Sign-In / One Tap / Smart Lock deprecated। Passkey phishing-resistant — কারণ এটা domain-এর সাথে বাঁধা (Digital Asset Links)।

```kotlin
val credentialManager = CredentialManager.create(context)
val request = GetCredentialRequest(listOf(GetPublicKeyCredentialOption(requestJsonFromServer)))
val result = credentialManager.getCredential(activity, request)   // suspend
val passkey = result.credential as? PublicKeyCredential
api.verifyPasskey(passkey?.authenticationResponseJson)
```

- একসাথে দুটো request token refresh করতে গেলে rotation-এ একটা ব্যর্থ হয়। তাই refresh একটা `Mutex` দিয়ে একবারে একটাই চালান (OkHttp `Authenticator`-এর ভেতরে)।

**Answer (English):**
> "I use OAuth 2.0 authorization code flow with PKCE, opened in a Custom Tab with the AppAuth library. A mobile app cannot keep a client secret, so PKCE makes a stolen code useless. I never log in inside a WebView, because the app could read the password and the user cannot see the real URL. After login, I keep a short-lived access token and a refresh token. The server rotates the refresh token on every use, and if an old one comes back, it kills the whole session. For new apps, I add passkeys with Credential Manager, because passkeys cannot be phished. One pitfall: two parallel refresh calls can break rotation, so I refresh behind a mutex."

**Key words:** `OAuth 2.0 + PKCE` · `Custom Tabs` · `AppAuth` · `refresh token rotation` · `Credential Manager` · `passkeys`

**Follow-up:**
- **Q:** Why is a WebView login a problem?
  **A:** "The host app controls the WebView, so it can inject JavaScript and read the password. Also, Google and many identity providers block it."
- **Q:** Why are passkeys safer than passwords?
  **A:** "The private key never leaves the device, and it only works for the real domain. So a fake site cannot get anything useful."
- **Q:** Where do you store the refresh token?
  **A:** "Encrypted with a Keystore-backed key through Tink. For sensitive apps, I bind it to biometrics with a CryptoObject."

**ভুল করবেন না:** "Implicit flow" বা app-এ client secret রাখার কথা বলবেন না — mobile-এ এগুলো ভুল।

**আরও দেখুন:** [S15 · Session security](#s15) · [R9 · Token refresh](#r9) · [C16 · App Links](#c16)

---

### <a id="s7"></a>S7. ★ How do you detect root, tampering and emulators?

**প্রশ্নটা মানে:** আপনি জানেন কিনা client-side check সহজে ভাঙে, আর Play Integrity কীভাবে server-এ যাচাই হয়।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you use the Play Integrity API?" · "Is a root check enough?"

**বুঝে নিন:**
- **Client-side check** (su binary খোঁজা, Magisk package, build props, signature check, Frida port খোঁজা): attacker নিজের phone-এ বসে এই function-গুলোই hook করে `false` return করায়। তাই এগুলো শুধু "গতি কমানো", সুরক্ষা না।
- **Play Integrity API** (SafetyNet বন্ধ, Jan 2025): Google Play একটা **signed** verdict দেয়। App বিশ্বাস করে না — **server** Google-এর API দিয়ে token decode করে যাচাই করে।
- **Verdict-এর ভাগ:**
  - `appIntegrity` — Play থেকে আসা, আসল signing cert-এর binary কিনা (`PLAY_RECOGNIZED`)
  - `deviceIntegrity` — `MEETS_BASIC_INTEGRITY`, `MEETS_DEVICE_INTEGRITY`, `MEETS_STRONG_INTEGRITY`
  - `accountDetails` — Play থেকে license
  - Optional: app access risk (screen capture বা overlay করছে এমন app), Play Protect অবস্থা ইত্যাদি
- Android 13+ device-এ Google verdict কঠিন করেছে (May 2025, "improved verdicts"): সব verdict-এ hardware-backed key attestation লাগে। `DEVICE` = bootloader locked + certified OS। `STRONG` = তার সাথে গত এক বছরের security patch (সব partition-এ)। `BASIC` = শুধু আসল physical device — unlocked বা rooted device-ও এটা পেতে পারে।
- **Replay আটকানো:**
  - **Standard request** (Google এটাই বলে, latency কম): `prepareIntegrityToken` আগে করে রাখুন, প্রতি action-এ `requestHash` দিন = action-এর data-র hash। Server hash মিলিয়ে দেখে।
  - **Classic request:** server-এর দেওয়া একবারের `nonce`।
- **Server কী করে:** verdict ভালো না হলে block না করে **ধাপে ধাপে** — sensitive কাজ (camera share, recording delete) বন্ধ, step-up auth, বা শুধু log। False positive (পুরনো phone, custom ROM-এর ভালো user) মাথায় রাখুন।
- **Custom AOSP hardware-এ Play services না থাকলে** Play Integrity কাজ করবে না। তখন key attestation (S3) নিজে যাচাই করুন।

```kotlin
val manager = IntegrityManagerFactory.createStandard(context)
manager.prepareIntegrityToken(
    PrepareIntegrityTokenRequest.builder().setCloudProjectNumber(projectNumber).build()
).addOnSuccessListener { provider ->
    provider.request(
        StandardIntegrityTokenRequest.builder().setRequestHash(sha256(actionPayload)).build()
    ).addOnSuccessListener { response -> api.sendWithIntegrity(actionPayload, response.token()) }
}
```

**Answer (English):**
> "Client-side root checks are easy to bypass. The attacker controls the phone, so they hook my check and make it return false. I still add a few, but only to slow people down. The real signal is the Play Integrity API. The app gets a signed token, and my server decodes and checks it, never the app. I use standard requests with a request hash of the action, so a token cannot be reused for another action. On a bad verdict, I do not just block. I limit sensitive actions or ask for step-up auth, because some honest users have old or custom devices. On our own hardware without Play services, I would use key attestation instead."

**Key words:** `Play Integrity API` · `server-side verification` · `requestHash` · `MEETS_DEVICE_INTEGRITY` · `key attestation`

**Follow-up:**
- **Q:** Why must the verdict be checked on the server?
  **A:** "If the app reads the verdict, an attacker can patch the app to ignore it. The server is the only place they cannot change."
- **Q:** What is the difference between nonce and requestHash?
  **A:** "Classic requests use a one-time nonce from the server. Standard requests use a hash of the action data, which Google puts back in the signed verdict, so the server can match it."
- **Q:** Can Play Integrity be fooled?
  **A:** "Basic integrity is a weak signal. On Android 13 and up, even a rooted device with an unlocked bootloader can get it. Device and strong integrity are much harder to fake, because they use hardware-backed key attestation. Nothing is perfect, so the server stays the final judge."

**ভুল করবেন না:** SafetyNet-এর নাম current tool হিসেবে বলবেন না, আর verdict app-এর ভেতরে check করবেন না।

**আরও দেখুন:** [S3 · Key attestation](#s3) · [S8 · Reverse engineering](#s8) · [O11 · Verified boot](#o11)

---

### <a id="s8"></a>S8. ◆ What can an attacker see in your APK?

**প্রশ্নটা মানে:** Reverse engineering বাস্তবে কতটা সহজ, আর R8-এর সীমা কোথায়।
**অন্যভাবেও জিজ্ঞেস করে:** "Does R8 protect your code?" · "How do you protect business logic?"

**বুঝে নিন:**
- **Tools:** `jadx` (DEX → প্রায় পড়ার মতো Java/Kotlin), `apktool` (resources, manifest, smali; আবার build করা যায়), Ghidra (native `.so`), Frida (runtime-এ hook)।
- **কী দেখা যায়:**
  - সব API URL, endpoint path, request format
  - `strings.xml`, `BuildConfig`, `assets/` — hardcoded key থাকলে সেটাও
  - Manifest — সব component, permission, exported কী কী
  - Native `.so`-র JNI function নাম, string
  - Flutter app-এ Dart AOT `libapp.so` — কঠিন, কিন্তু tool আছে
- **R8 কী করে:** নাম ছোট করে (`a.b.c`), unused code সরায়, inline করে। **কী করে না:** string encrypt করে না, logic লুকায় না, resource লুকায় না। Flow পড়া কঠিন হয়, অসম্ভব না।
- **Native code (NDK):** পড়া কঠিন, কিন্তু Ghidra দিয়ে সম্ভব। Secret native-এ সরালে কয়েক ঘণ্টা বেশি লাগে, নিরাপদ হয় না।
- **সত্যিকারের সুরক্ষা = design:**
  - Secret আর গুরুত্বপূর্ণ নিয়ম **server-এ** (যেমন কোন user কোন camera দেখতে পারবে, subscription limit)
  - Client শুধু UI আর user-এর নিজের data
  - API ধরে নিন public — প্রতিটা endpoint server-এ auth আর authorization check করে
- Commercial tool (string encryption, anti-hook, RASP) আছে। এগুলো খরচ আর maintenance বাড়ায় — সত্যিকারের threat থাকলে তবেই।
- Android 17 target করলে native library dynamic loading-এ file read-only হতে হয় — runtime-এ code বদলানো কঠিন হয়।

**Answer (English):**
> "An attacker can see almost everything. jadx turns the DEX back into readable code. apktool shows the manifest, resources and strings. All my endpoints and any hardcoded key are visible. R8 helps a little: it renames classes and removes unused code, but it does not encrypt strings or hide logic. Native code is harder to read, but Ghidra can still do it. So my real defense is design. Secrets and important business rules live on the server. Every API checks auth and permission, because I assume the API is public. I add commercial hardening only if the threat really needs it, because it costs time to maintain."

**Key words:** `jadx` · `apktool` · `R8` · `server-side logic` · `Ghidra`

**Follow-up:**
- **Q:** Should we put the API key in native code?
  **A:** "It only adds a small delay. Someone can read it with Ghidra or hook the JNI call with Frida. A real secret belongs on the server."
- **Q:** What do you keep in the R8 keep rules?
  **A:** "Only what reflection needs, like some serialization models. Wide keep rules remove most of the benefit."

**ভুল করবেন না:** "R8 দিলে code কেউ পড়তে পারবে না" — এটা ভুল।

**আরও দেখুন:** [P5 · R8](#p5) · [S2 · Tokens and secrets](#s2) · [B4 · NDK and JNI](#b4)

---

### <a id="s9"></a>S9. ★ How do you secure app components?

**প্রশ্নটা মানে:** Activity, Service, Receiver, Provider অন্য app-এর কাছে কতটা খোলা, আর intent দিয়ে কোন বাগ হয়।
**অন্যভাবেও জিজ্ঞেস করে:** "What is intent redirection?" · "Why must PendingIntent be immutable?"

**বুঝে নিন:**
- **Exported:** `android:exported="true"` হলে অন্য যেকোনো app সেই component চালাতে পারে। Android 12 থেকে intent-filter থাকলে `exported` লিখতেই হয়। Default নিয়ম: **launcher activity আর deep link ছাড়া সব `false`**।
- **Signature permission:** নিজের দুই app-এর মধ্যে কথা বললে:
  ```xml
  <permission android:name="com.acme.permission.CAMERA_BRIDGE"
      android:protectionLevel="signature" />
  ```
  একই key-এ sign করা app-ই শুধু এটা পাবে।
- **Intent redirection:** exported activity অন্য app-এর পাঠানো একটা nested `Intent` extra নিয়ে `startActivity()` করে। তখন attacker আপনার app দিয়ে আপনার **private** component খোলায় বা আপনার `FileProvider`-এর URI permission পায়। ঠিক করার উপায়: বাইরে থেকে আসা intent সরাসরি launch করবেন না; component/package যাচাই করুন; `getCallingActivity()`-এর উপর ভরসা নয় (null দেওয়া যায়)। Android 16 এই exploit-এর বিরুদ্ধে default hardening এনেছে।
- **PendingIntent:** অন্য app (যেমন notification system) আপনার পরিচয়ে এটা চালায়। Mutable হলে অন্য app ভেতরের intent বদলাতে পারে।
  - Android 12: `FLAG_IMMUTABLE` বা `FLAG_MUTABLE` দিতেই হবে। Default **immutable** রাখুন।
  - Android 14: mutable PendingIntent-এ implicit intent দিলে exception।
  ```kotlin
  val intent = Intent(context, LiveViewActivity::class.java).putExtra("cameraId", cameraId)
  val pending = PendingIntent.getActivity(context, cameraId.hashCode(), intent,
      PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
  ```
- **Implicit intent data leak:** `Intent("com.acme.ACTION_TOKEN").putExtra("token", ...)` — যে কোনো app সেই action-এর জন্য filter বানিয়ে data পায়। Sensitive data সবসময় **explicit** intent-এ (`setPackage` / component)।
- **ContentProvider:** `exported="false"`; file share করতে `FileProvider` + সময়-সীমিত `FLAG_GRANT_READ_URI_PERMISSION`। Provider query-তে SQL injection আর path traversal check করুন।
- **Context-registered receiver** (Android 14): `RECEIVER_NOT_EXPORTED` দিন যদি শুধু নিজের app পাঠায়।
- **Tapjacking:** sensitive button-এ `filterTouchesWhenObscured`। Android 12 থেকে untrusted overlay-র উপর touch block হয়।

**Answer (English):**
> "I keep every component private by default. Only the launcher activity and real deep links are exported. If two of our own apps must talk, I protect the component with a signature-level permission. I watch for intent redirection: an exported activity must never launch an intent that came from outside without checking it. PendingIntents are immutable unless a feature really needs mutable, and then the inner intent must be explicit, which Android 14 enforces. I never send sensitive data in an implicit intent, because any app can register for it. For file sharing, I use FileProvider with a short URI grant. I check all this with lint and by reading the merged manifest."

**Key words:** `android:exported` · `signature permission` · `intent redirection` · `FLAG_IMMUTABLE` · `explicit intent` · `FileProvider`

**Follow-up:**
- **Q:** Why check the merged manifest?
  **A:** "Libraries can add their own exported components. The merged manifest shows what really ships."
- **Q:** When do you need a mutable PendingIntent?
  **A:** "For things like inline reply in a notification, where the system must add the reply text. Then the inner intent must be explicit."

**ভুল করবেন না:** library merge-এর পরে কোন component exported হলো সেটা না দেখে "আমাদের সব private" বলবেন না।

**আরও দেখুন:** [C5 · Intents and PendingIntent](#c5) · [C14 · Manifest](#c14) · [C9 · FileProvider](#c9)

---

### <a id="s10"></a>S10. ◆ How do you make a WebView safe?

**প্রশ্নটা মানে:** WebView-এর কোন setting বিপদ আনে, আর JS bridge কীভাবে সীমিত রাখেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What are the risks of addJavascriptInterface?" · "How do you load local files in a WebView safely?"

**বুঝে নিন:**
- **JavaScript interface:** `addJavascriptInterface(obj, "Android")` দিলে page-এর **যেকোনো** JS (iframe, ad, injected script সহ) সেই object-এর `@JavascriptInterface` method call করতে পারে। Page-এ XSS হলে attacker native method চালায়।
  - Bridge ছোট রাখুন। Token বা file access দেবেন না।
  - নিরাপদ বিকল্প: `WebViewCompat.addWebMessageListener(webView, "bridge", setOf("https://app.example.com"), listener)` — শুধু নির্দিষ্ট origin থেকে message আসে।
- **File access:** `allowFileAccess` (target 30+ এ default false), `allowFileAccessFromFileURLs` / `allowUniversalAccessFromFileURLs` — কখনো true না। Local content-এর জন্য **`WebViewAssetLoader`** — `https://appassets.androidplatform.net/...` দিয়ে, same-origin নিয়ম ঠিক থাকে।
- **URL allowlist:** `shouldOverrideUrlLoading`-এ host check করুন। অন্য domain হলে Custom Tab-এ খুলুন। Host check করবেন `Uri.parse(url).host` দিয়ে, `startsWith` string দিয়ে না।
- **Safe Browsing:** modern WebView-এ default চালু। বন্ধ করবেন না।
- **অন্যান্য:** `setSavePassword` আর login (S6) WebView-এ না; `onReceivedSslError`-এ কখনো `handler.proceed()` না (Play এটা reject করে); mixed content বন্ধ।
- Android 17-এ WebView-এর LAN traffic host app-এর local network permission মানে।

**Answer (English):**
> "I treat a WebView as untrusted content running inside my app. I avoid addJavascriptInterface, because any script on the page, even from an iframe, can call it. If I need a bridge, I use addWebMessageListener with an allowed origin list, and the bridge only exposes small, safe actions. File access settings stay off, and I load local content through WebViewAssetLoader over https. In shouldOverrideUrlLoading I check the host properly, and other sites open in a Custom Tab. I keep Safe Browsing on, and I never call proceed on an SSL error. And I never put login inside a WebView."

**Key words:** `addJavascriptInterface` · `addWebMessageListener` · `WebViewAssetLoader` · `URL allowlist` · `onReceivedSslError`

**Follow-up:**
- **Q:** Why is onReceivedSslError with proceed bad?
  **A:** "It accepts any certificate, so a man-in-the-middle can read and change everything. Google Play also flags it."

**ভুল করবেন না:** `url.contains("example.com")` দিয়ে allowlist করবেন না — `evil.com/?example.com` পাস হয়ে যায়।

**আরও দেখুন:** [S6 · Login and auth](#s6) · [C16 · Deep links](#c16)

---

### <a id="s11"></a>S11. ★ How do you protect data at rest and stop data leaks?

**প্রশ্নটা মানে:** Phone-এ রাখা data আর "অজান্তে বের হয়ে যাওয়া" data — দুটোই সামলাতে পারেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you encrypt a Room database?" · "What can leak from a phone without a hack?"

**বুঝে নিন:**
- **Database:** Room নিজে encrypt করে না। **SQLCipher** (`net.zetetic:sqlcipher-android`) + `SupportOpenHelperFactory(passphrase)` দিয়ে Room encrypt হয়। Passphrase random, Keystore/Tink দিয়ে wrap করে রাখা। (পুরনো `android-database-sqlcipher` artifact আর না।)
- **File / recording:** Tink **StreamingAead** (বড় file-এর জন্য, chunk করে encrypt)। App-specific storage (`filesDir`) — অন্য app পড়তে পারে না, কিন্তু rooted device-এ পারে, তাই encryption।
- **Backup:**
  - `android:allowBackup="false"` cloud backup বন্ধ করে। কিন্তু Android 12+ target করলে **device-to-device transfer তবুও হয়** — `dataExtractionRules`-এ `<device-transfer>`-এ exclude করুন।
  - Token, DB, keyset backup থেকে বাদ দিন। Keystore key backup হয় না, তাই restore-এর পর encrypted data এমনিতেও পড়া যায় না — crash না করে clean করুন।
- **Screen:**
  - `FLAG_SECURE` — screenshot, screen recording, non-secure display-তে দেখানো বন্ধ; recents-এর thumbnail-ও কালো। Live camera view-এ খুব দরকারি।
  - Android 17 target করলে `setContentCaptureEnabled(false)` আর content capture বন্ধ করে না (API deprecated)। Docs বলছে এখন `FLAG_SECURE` ব্যবহার করতে।
  - শুধু recents লুকাতে: `setRecentsScreenshotEnabled(false)` (API 33)।
  - Screenshot detect: `registerScreenCaptureCallback` (API 34)। Screen recording detect: API 35-এ callback আছে।
- **Clipboard:** password/OTP copy করলে `ClipDescription.EXTRA_IS_SENSITIVE` (API 33) দিন, যাতে preview-তে না দেখায়।
- **Logs:** release build-এ token, URL-এর query, RTSP URL-এর password log করবেন না। R8 `-assumenosideeffects` দিয়ে `Log.d` সরানো যায়। Crash report-এও PII scrub।
- **Notification on lock screen:** motion alert-এ snapshot ছবি lock screen-এ দেখানো privacy ঝুঁকি। `setVisibility(VISIBILITY_PRIVATE)` + `setPublicVersion(...)` দিয়ে lock screen-এ শুধু "Motion detected" দেখান।
- **Accessibility:** Android 14-এ sensitive view-এ `accessibilityDataSensitive` দিলে অ-accessibility-tool service সেটা পড়তে পারে না।
- **Keyboard:** password field-এ সঠিক `inputType`, যাতে keyboard শেখে না।

**Answer (English):**
> "For data at rest, I encrypt the Room database with SQLCipher, and the passphrase is wrapped by a Keystore key. Files and recordings use Tink streaming encryption. Then I close the quiet leaks. I exclude tokens and databases from backup, and I remember that on Android 12 and up, allowBackup false does not stop device-to-device transfer, so I use data extraction rules. Live camera screens use FLAG_SECURE, which also hides the recents thumbnail. Release builds do not log tokens or stream URLs. Lock screen notifications show a private version without the snapshot. The trade-off is user experience, for example FLAG_SECURE blocks screenshots users may want, so I use it only on sensitive screens."

**Key words:** `SQLCipher` · `StreamingAead` · `dataExtractionRules` · `FLAG_SECURE` · `VISIBILITY_PRIVATE` · `EXTRA_IS_SENSITIVE`

**Follow-up:**
- **Q:** Is file-based encryption of Android not enough?
  **A:** "It protects data when the phone is off or locked. Once unlocked, any process with root can read app files, so I add app-level encryption for sensitive data."
- **Q:** What happens to encrypted data after a backup restore on a new phone?
  **A:** "The Keystore key does not move, so the data cannot be decrypted. I detect that, delete it, and ask the user to sign in again."
- **Q:** Where would you use FLAG_SECURE in a camera app?
  **A:** "On live view, recording playback, and screens with pairing codes or passwords."

**ভুল করবেন না:** "`allowBackup=false` দিলেই কোনো data phone থেকে বের হয় না" — Android 12+ এ device transfer আলাদা।

**আরও দেখুন:** [S2 · Tokens and secrets](#s2) · [V5 · Record video](#v5) · [V9 · Motion alerts](#v9)

---

### <a id="s12"></a>S12. ◆ How do you secure IPC between your own apps or a system service?

**প্রশ্নটা মানে:** AIDL bound service-এ কে call করছে সেটা কীভাবে যাচাই করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How does a bound service check the caller?" · "How do you expose an API to a partner app safely?"

**বুঝে নিন:**
- Camera company-তে প্রায়ই এমন হয়: একটা system service camera hardware চালায়, আর কয়েকটা app (viewer, settings, cloud uploader) AIDL দিয়ে তার সাথে কথা বলে।
- **স্তর ১ — manifest:** service-এ `android:permission` দিন, আর সেই permission `signature` level (বা platform app হলে `signature|privileged`)।
  ```xml
  <service android:name=".CameraBridgeService" android:exported="true"
      android:permission="com.acme.permission.CAMERA_BRIDGE" />
  ```
- **স্তর ২ — প্রতি call-এ check:** manifest permission শুধু bind আটকায়। প্রতিটা method-এ caller যাচাই করুন:
  ```kotlin
  override fun openStream(cameraId: String): ParcelFileDescriptor {
      if (checkCallingPermission(PERM_CAMERA_BRIDGE) != PackageManager.PERMISSION_GRANTED) {
          throw SecurityException("Caller not allowed")
      }
      val uid = Binder.getCallingUid()
      require(isAllowedForCamera(uid, cameraId)) { "No access to $cameraId" }
      return streamManager.open(cameraId)
  }
  ```
- `Binder.getCallingUid()` / `getCallingPid()` binder transaction-এর ভেতরেই সঠিক। অন্য thread-এ গেলে আগে নিয়ে রাখুন। নিজের identity দিয়ে কাজ করতে হলে `Binder.clearCallingIdentity()` আর `finally`-তে `restoreCallingIdentity()`।
- **নির্দিষ্ট partner app (ভিন্ন key):** Android 12-এর `knownSigner` protection flag + `knownCerts` — নির্দিষ্ট cert digest-কে permission দেয়। অথবা uid থেকে package নিয়ে signing cert নিজে check।
- **Input validation:** AIDL-এর মাধ্যমে আসা সব data untrusted — size, path, id check।
- **System side (AOSP):** নতুন HAL **stable AIDL**-এ (HIDL deprecated)। SELinux policy-তে কোন domain কোন service খুঁজতে আর call করতে পারবে, তা বাঁধা থাকে — app check-এর পাশাপাশি এটাও একটা স্তর।
- Permission squatting: custom permission এমন app-এ define করুন যেটা আগে install হয় (বা দুই app-এই), signature level-এ রাখুন।

**Answer (English):**
> "I protect it in two layers. In the manifest, the service requires a signature-level permission, so only apps signed with our key can bind. Then inside every AIDL method, I check the caller again with checkCallingPermission and Binder.getCallingUid, and I check that this caller may use this camera. The manifest check only controls binding, not each call, so the per-call check matters. I treat all data from the caller as untrusted input. If a partner app with a different key needs access, I use the knownSigner permission flag with their certificate digest. On our own OS builds, SELinux policy is another layer on top."

**Key words:** `AIDL` · `signature permission` · `Binder.getCallingUid` · `checkCallingPermission` · `knownSigner` · `SELinux`

**Follow-up:**
- **Q:** Why save the calling UID before switching threads?
  **A:** "Binder only knows the caller during the incoming call on the binder thread. On another thread, getCallingUid returns my own UID."
- **Q:** What does clearCallingIdentity do?
  **A:** "It lets my service call other system APIs as itself, not as the caller. I always restore it in a finally block."

**আরও দেখুন:** [F3 · Binder](#f3) · [O5 · System service](#o5) · [O7 · SELinux](#o7)

---

### <a id="s13"></a>S13. ◆ What do you know about Android Enterprise and device management?

**প্রশ্নটা মানে:** Company-র phone বা dedicated device (যেমন guard room-এর monitor tablet) কীভাবে manage আর lock করা হয়।
**অন্যভাবেও জিজ্ঞেস করে:** "What is a Device Owner?" · "How does an MDM configure your app?"

**বুঝে নিন:**
- **Android Enterprise mode:**

| Mode | কার জন্য | কে control করে |
|---|---|---|
| Work profile (personal device) | BYOD | শুধু work profile (Profile Owner) |
| Work profile (company-owned) | company phone, personal ব্যবহারও | work profile + কিছু device policy |
| Fully managed (Device Owner) | শুধু কাজের phone | পুরো device |
| Dedicated device | kiosk, monitor, camera hub | পুরো device, lock task mode |

- **MDM/EMM** (যেমন Intune, Workspace ONE) একটা **DPC** app বা Google-এর **Android Management API** দিয়ে policy দেয়। Google নতুন EMM-কে Android Management API ব্যবহার করতে বলছে — বিস্তারিত Google-এর docs-এ।
- **Provisioning:** factory reset-এর পর QR code, zero-touch (company কেনা device), বা `afw#setup`। Test-এ: fresh device-এ `adb shell dpm set-device-owner com.acme/.AdminReceiver`।
- **Managed configurations:** IT admin console থেকে app-এর setting পাঠায় (যেমন server URL, কোন camera group দেখা যাবে, screenshot allowed কিনা)।
  - `res/xml/app_restrictions.xml` + manifest-এ `android.content.APP_RESTRICTIONS` meta-data
  - পড়া: `RestrictionsManager.applicationRestrictions`
  - বদল শোনা: `ACTION_APPLICATION_RESTRICTIONS_CHANGED` broadcast
- **Dedicated device / kiosk:** Device Owner `setLockTaskPackages()` → app `startLockTask()`; status bar, home, recents বন্ধ। `SystemUpdatePolicy` দিয়ে update window ঠিক করা।
- **Work profile-এ data আলাদা:** work app-এর data personal app দেখতে পারে না; admin profile মুছে দিলে শুধু work data যায়।
- Custom AOSP hardware-এ নিজের DPC-ও platform-signed system app হিসেবে আগে থেকে রাখা যায়।

**Answer (English):**
> "Android Enterprise has a few modes. A work profile keeps company apps and data separate on a personal or company phone. A fully managed device, with a Device Owner, gives the company full control. A dedicated device is a locked kiosk, like a monitoring tablet. The MDM sets policies through a DPC or the Android Management API. For my app, the main job is to support managed configurations: I define them in app_restrictions.xml, read them with RestrictionsManager, and listen for changes. For a kiosk, the Device Owner allows my package in lock task mode. I test Device Owner setup on a fresh device with adb dpm commands."

**Key words:** `work profile` · `Device Owner` · `managed configurations` · `RestrictionsManager` · `lock task mode` · `zero-touch`

**Follow-up:**
- **Q:** How would you set up a 24/7 camera monitor tablet?
  **A:** "Provision it as a dedicated device with a Device Owner, allow only our app in lock task mode, keep the screen on, and control system updates with an update policy."

**আরও দেখুন:** [O9 · Kiosk device](#o9) · [V11 · 24/7 monitoring](#v11)

---

### <a id="s14"></a>S14. ◆ How do you test the security of an app?

**প্রশ্নটা মানে:** নিজে attacker-এর মতো app ভাঙার চেষ্টা করেন কিনা, আর pen-test finding কীভাবে সামলান।
**অন্যভাবেও জিজ্ঞেস করে:** "What tools do you use for mobile security testing?" · "What do you do with a pen-test report?"

**বুঝে নিন:**
- **Static (code না চালিয়ে):**
  - **MobSF** — APK দিলে manifest, exported component, hardcoded secret, weak crypto, network config রিপোর্ট করে
  - `jadx` দিয়ে নিজের release APK পড়া — কী দেখা যাচ্ছে?
  - Android Lint security check, Semgrep-এর মতো tool, dependency scan
- **Dynamic (চালিয়ে):**
  - **Burp Suite / mitmproxy** — traffic দেখা আর বদলানো। Debug build-এ proxy CA trust (`debug-overrides`)
  - **Frida** — runtime-এ function hook। **objection** (Frida-র উপর) — `android sslpinning disable`, root detection bypass, Keystore/file দেখা
  - **adb** — `adb shell am start -n <pkg>/<exported activity>` দিয়ে exported component ঠিক কাজ করে কিনা; `run-as` দিয়ে debug build-এর storage দেখা; `dumpsys package`
- **Checklist:** OWASP **MASTG** test case, MASVS ধরে। সব release-এর আগে না, কিন্তু বড় release আর নতুন feature-এ।
- **API test** আসল জায়গা: অন্য user-এর camera id দিয়ে request (IDOR), token ছাড়া, মেয়াদ শেষ token দিয়ে।
- **Pen-test finding workflow:**
  1. প্রতিটা finding reproduce করুন
  2. Severity ঠিক করুন (exploit কতটা সহজ × ক্ষতি কত)
  3. Ticket, owner, deadline
  4. Fix + regression test (যেমন একটা unit test বা automated check)
  5. Pen-tester দিয়ে retest
  6. "Accepted risk" হলে লিখে রাখা, কারণ সহ
- Third-party যাচাই চাইলে App Defense Alliance-এর MASA (MASVS-ভিত্তিক) আছে — বিস্তারিত তাদের সাইটে।

**Answer (English):**
> "I test both statically and at runtime. For static checks, I run MobSF on the release APK and open it in jadx to see what an attacker sees. At runtime, I put traffic through Burp or mitmproxy, and I use Frida and objection to try to bypass pinning and root checks. With adb, I start exported components directly to see if they leak anything. The most important part is testing the API, for example asking for another user's camera with my token. I follow the OWASP MASTG checklist. For pen-test findings, I reproduce each one, rate it, fix it with a regression test, and ask for a retest."

**Key words:** `MobSF` · `Frida` · `objection` · `Burp Suite` · `OWASP MASTG` · `IDOR`

**Follow-up:**
- **Q:** If Frida can bypass pinning, why test it at all?
  **A:** "To see what a real attacker sees after the bypass. If the API is safe even then, pinning is just an extra layer, and that is fine."

**ভুল করবেন না:** শুধু app test করে থামবেন না — বেশিরভাগ বড় বাগ থাকে backend authorization-এ।

**আরও দেখুন:** [S17 · OWASP Mobile Top 10](#s17) · [S8 · Reverse engineering](#s8) · [S7 · Root detection](#s7)

---

### <a id="s15"></a>S15. ◆ How do you handle session security?

**প্রশ্নটা মানে:** Token চুরি হলে কী হয়, logout সত্যিই কাজ করে কিনা, device-এর সাথে session বাঁধেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How does 'log out of all devices' work?" · "How do you detect a stolen token?"

**বুঝে নিন:**
- **Expiry:** access token ছোট (কয়েক মিনিট)। Refresh token-এর মেয়াদ আর "idle timeout" (অনেকদিন ব্যবহার না হলে বাতিল)।
- **Logout:** শুধু local token মুছলে হয় না। Server-এ refresh token **revoke** করতে হয়। Access token ছোট বলে কিছুক্ষণ চলতে পারে — sensitive হলে server-এ deny-list বা token version check।
- **Logout everywhere:** user-এর সব refresh token family revoke; বা user-এর `tokenVersion` বাড়ানো — পুরনো version-এর token বাতিল। Password বদল বা "phone হারিয়েছি" হলে এটা চালু।
- **Device binding (sender-constrained token):**
  - Login-এ Keystore-এ একটা EC key pair বানান (attestation সহ হলে আরও ভালো)। Public key server-এ যায়।
  - প্রতি request-এ (বা refresh-এ) private key দিয়ে sign করা proof যায়। Standard: **DPoP** (RFC 9449)।
  - Token চুরি হয়ে অন্য device-এ গেলে signing key নেই → reject।
- **চুরি ধরার signal:**
  - Refresh token reuse (rotation, S6)
  - Device binding proof fail
  - হঠাৎ নতুন দেশ/network, অসম্ভব travel, Play Integrity verdict হঠাৎ খারাপ
  - একসাথে অনেক camera stream খোলা
- **Step-up:** sensitive কাজে (camera share, recording delete, password বদল) নতুন biometric বা password।
- **User-কে দেখান:** "Active sessions" list — device নাম, শেষ ব্যবহার, আলাদা করে remove। Camera app-এ "কে কখন live দেখেছে" log।

**Answer (English):**
> "Access tokens live only a few minutes, and refresh tokens rotate on every use. Logout must revoke the refresh token on the server, not just delete it on the phone. For 'log out everywhere', the server revokes all of the user's refresh tokens, or bumps a token version so old tokens fail. For high-value apps, I bind the session to the device: a Keystore key signs each request, for example with DPoP, so a stolen token is useless on another phone. To detect theft, the server watches for refresh token reuse, failed binding proofs, and strange locations. I also show the user a list of active sessions they can remove."

**Key words:** `token revocation` · `refresh token reuse detection` · `device binding` · `DPoP` · `step-up authentication`

**Follow-up:**
- **Q:** What is the cost of device binding?
  **A:** "More work on both client and server, and key loss means a new login. But for live home video, I think it is worth it."

**আরও দেখুন:** [S6 · Login and auth](#s6) · [S3 · Keystore](#s3)

---

### <a id="s16"></a>S16. ○ How do you protect the software supply chain?

**প্রশ্নটা মানে:** আপনার নিজের code ছাড়াও library, build, আর signing key কীভাবে রক্ষা করেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you check third-party dependencies?" · "What is Play App Signing?"

**বুঝে নিন:**
- **Dependency:**
  - Version catalog-এ fixed version; Dependabot/Renovate দিয়ে update PR
  - Vulnerability scan (OSV-Scanner বা এই রকম tool), Play Console-এ SDK Index warning দেখা
  - **Gradle dependency verification** (`gradle/verification-metadata.xml`) — download করা artifact-এর checksum/signature মেলায়
  - নতুন SDK যোগের আগে review: কী permission, কী data পাঠায়
- **Signing:**
  - **Play App Signing:** app signing key Google রাখে; আপনার কাছে শুধু **upload key**। Upload key হারালে reset করা যায়; signing key হারানোর ভয় নেই।
  - APK Signature Scheme v3 / v3.1 key rotation support করে।
  - Upload key CI secret-এ, কম লোকের access।
- **Build:** CI-তে clean build, পরিচিত runner; release build হাতে-বানানো laptop থেকে না। Reproducible build মানে একই source থেকে একই output — যাচাই সহজ।
- **SBOM:** CycloneDX Gradle plugin দিয়ে সব dependency-র list — নতুন CVE এলে দ্রুত দেখা যায় কোন app affected।
- **Custom AOSP hardware:** AOSP-র **test key** দিয়ে release build কখনো না — নিজের platform/release key বানান, HSM-এ রাখুন। OTA package sign করুন।
- Google-এর developer verification নিয়ম (sideload-এর জন্যও verified developer) ধাপে ধাপে চালু হচ্ছে — enterprise বা sideload distribution থাকলে current নিয়ম দেখে নিন।

**Answer (English):**
> "I treat dependencies and signing keys as part of the attack surface. Dependencies have fixed versions, update PRs from a bot, and a vulnerability scan in CI. I turn on Gradle dependency verification so a changed artifact fails the build. I also produce an SBOM, so when a new CVE comes out, I can see quickly which builds use it. For signing, I use Play App Signing, so Google keeps the app signing key and we only hold an upload key that can be reset. Releases are built only in CI. For our own Android builds, we must never ship with AOSP test keys."

**Key words:** `dependency verification` · `SBOM` · `Play App Signing` · `upload key` · `release keys`

**Follow-up:**
- **Q:** What happens if the upload key leaks?
  **A:** "We ask Google to reset the upload key. Because Google holds the real app signing key, users stay safe."

**আরও দেখুন:** [P6 · Play App Signing](#p6) · [O11 · Verified boot](#o11) · [O10 · OTA updates](#o10)

---


## <a id="part-8"></a>Part 8 — Security camera, video আর streaming

এই কোম্পানির মূল product-ই camera আর video। তাই এই part-এর প্রশ্নগুলো তাদের রোজের কাজ। এখানে ভালো উত্তর দিলে বোঝা যায় আপনি সত্যিই তাদের team-এ কাজ শুরু করতে পারবেন।
দুই ধরনের কাজ আসতে পারে: (১) phone/tablet app যা IP camera-র live stream আর recording দেখায়, (২) নিজেদের Android device যেটা নিজেই camera — ছবি তোলে, encode করে, পাঠায়।

### আগে বুঝুন — camera আর video-র বড় ছবি

**একটা video কোথা থেকে কোথায় যায়:**

```
Sensor → Camera HAL → Camera2/CameraX → Surface
   → Encoder (MediaCodec, H.264/H.265) → Muxer (MP4) → file
                                       → Packetizer (RTP/RTSP, WebRTC, HLS) → network
Network → Player (Media3 ExoPlayer / WebRTC) → Decoder (MediaCodec) → SurfaceView
```

**যে ৯টা ধারণার উপর সব দাঁড়িয়ে:**

1. **Surface-ই মূল পথ।** Camera frame, encoder input, decoder output — সবকিছু `Surface` দিয়ে GPU/hardware buffer-এ যায়। CPU-তে frame copy করলে battery আর গতি নষ্ট।
2. **CameraX** = সহজ, lifecycle-aware, use case ভিত্তিক। **Camera2** = পুরো control। CameraX নিজেই Camera2-এর উপর বানানো।
3. **Hardware codec সীমিত।** একটা phone একসাথে কয়টা video decode/encode করতে পারে, তার সীমা আছে। Grid view-এর সব সিদ্ধান্ত এই সীমা থেকে আসে।
4. **Codec:** H.264 সব জায়গায় চলে। H.265 একই quality-তে কম bitrate। AV1 আরও ভালো, কিন্তু hardware encoder নতুন chip-এ। **Keyframe (I-frame)** ছাড়া video শুরু বা কাটা যায় না।
5. **Protocol বাছাই মানে latency-র trade-off:** RTSP (LAN, ১ সেকেন্ডের কম), WebRTC (internet-এ খুব কম latency), HLS/LL-HLS (cloud, CDN, কয়েক সেকেন্ড)।
6. **Background নিয়ম কঠিন।** Android 9 থেকে background-এ camera নেই। Android 14 থেকে foreground service type `camera` লাগে। Android 15 থেকে boot-এর পর camera FGS চালু করা যায় না।
7. **Local network permission।** Android 17 target করলে LAN camera-র সাথে কথা বলতে `ACCESS_LOCAL_NETWORK` runtime permission লাগে।
8. **Media3** (`androidx.media3`) এখন standard player — HLS, DASH, RTSP সব। পুরনো `com.google.android.exoplayer2` deprecated।
9. **Security সব স্তরে:** stream encrypt (TLS/SRTP), ছোট-মেয়াদি signed URL, device pairing, default password না, recording encrypted।

**তিনটা সাধারণ architecture:**

| Setup | কীভাবে | কখন |
|---|---|---|
| LAN direct | app → camera RTSP | একই Wi-Fi, কম latency, internet লাগে না |
| Cloud relay | camera → cloud → app (HLS/WebRTC) | বাইরে থেকে দেখা, recording cloud-এ |
| P2P | WebRTC, STUN/TURN দিয়ে NAT পার | কম latency, cloud bandwidth খরচ কম |

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ `camera` বা `video_player` plugin সব লুকিয়ে রাখত। Native-এ আপনি নিজে Surface, codec, lifecycle সামলাবেন।
- Flutter-এ video দেখাতে `Texture` widget (TextureView-এর মতো GPU path) ব্যবহার হয়। Native-এ আপনি SurfaceView বেছে নিতে পারেন — battery-তে ভালো।
- Isolate-এর বদলে এখানে `Executor` / coroutine dispatcher দিয়ে frame analysis চলে।
- Permission, foreground service, notification — এখন সরাসরি আপনার manifest আর code-এ।

---

### <a id="v1"></a>V1. ★ CameraX or Camera2 — when do you use each?

**প্রশ্নটা মানে:** কোন কাজে কোন API ঠিক, আর CameraX-এর সীমা কোথায়।
**অন্যভাবেও জিজ্ঞেস করে:** "Why would you choose Camera2 over CameraX?" · "What are CameraX use cases?"

**বুঝে নিন:**
- **CameraX** (default পছন্দ): আপনি **use case** বলেন, CameraX device-অনুযায়ী resolution, format, quirk সামলায়। Lifecycle-এর সাথে নিজে open/close হয়।
  - `Preview` — viewfinder (Compose-এ `camera-compose`-এর `CameraXViewfinder`)
  - `ImageCapture` — ছবি
  - `ImageAnalysis` — প্রতিটা frame CPU-তে (motion detection, ML)
  - `VideoCapture` + `Recorder` — video recording
  - Extensions (night, HDR — device support থাকলে), concurrent camera (সামনে + পেছনে একসাথে, support থাকলে)
  - দরকার হলে `Camera2Interop` দিয়ে কিছু Camera2 setting দেওয়া যায়।

```kotlin
val preview = Preview.Builder().build()
    .also { it.setSurfaceProvider(previewView.surfaceProvider) }
val analysis = ImageAnalysis.Builder()
    .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
    .build()
    .also { it.setAnalyzer(analysisExecutor) { image -> motionDetector.check(image); image.close() } }
cameraProvider.bindToLifecycle(lifecycleOwner, CameraSelector.DEFAULT_BACK_CAMERA, preview, analysis)
```

- **Camera2** কখন:
  - Manual control — exposure time, ISO, focus distance, white balance প্রতি frame-এ
  - RAW capture, high-speed (slow motion) session, reprocessing
  - নির্দিষ্ট stream combination (যেমন একসাথে 4K record + low-res analysis + preview), যা CameraX-এর use-case limit পার হয়
  - Logical multi-camera-র physical camera আলাদা করে ধরা
  - **External / USB camera:** platform UVC support থাকলে Camera2-এ `LENS_FACING_EXTERNAL` হিসেবে আসে। আগে `PackageManager.FEATURE_CAMERA_EXTERNAL` check করুন। বেশিরভাগ phone-এ এটা নেই — তখন `UsbManager` দিয়ে নিজের UVC driver লাগে। CameraX-এ external support experimental।
- **নিজেদের AOSP camera device-এ:** camera HAL vendor বানায় (নতুন HAL AIDL-এ)। App-এ Camera2 বেশি control দেয়; HAL-এর ক্ষমতা `CameraCharacteristics` (যেমন `INFO_SUPPORTED_HARDWARE_LEVEL`) দিয়ে দেখুন।
- **IP camera viewer app-এ** phone-এর camera লাগেই না — সেখানে কাজ player আর decoder-এ (V3, V4)।

**Answer (English):**
> "CameraX is my default. I describe use cases like Preview, ImageCapture, ImageAnalysis and VideoCapture, and CameraX handles device differences and the lifecycle. That saves a lot of device-specific bugs. I move to Camera2 when I need full control: manual exposure and focus per frame, RAW, high-speed video, or a special mix of streams that CameraX does not support. Camera2 is also the path for external USB cameras, but only if the device supports external cameras, which most phones do not. CameraX is built on Camera2, so I can mix them a little with Camera2Interop. On our own hardware, Camera2 gives the most control over what the HAL offers."

**Key words:** `CameraX use cases` · `Camera2` · `Camera2Interop` · `LENS_FACING_EXTERNAL` · `hardware level`

**Follow-up:**
- **Q:** What does the camera hardware level tell you?
  **A:** "It says how much of Camera2 the device supports: LEGACY, LIMITED, FULL or LEVEL_3. LEGACY devices have very limited manual control, so I check it before showing pro features."
- **Q:** How would you use a USB camera on an Android box?
  **A:** "First I check FEATURE_CAMERA_EXTERNAL. If the platform supports it, the camera shows up in Camera2. If not, I need the USB host API and a UVC library, or we add UVC support in our own OS build."

**ভুল করবেন না:** "CameraX সব কিছু পারে" বা "Camera2 পুরনো" — দুটোই ভুল; দুটোই current, কাজ আলাদা।

**আরও দেখুন:** [V5 · Record video](#v5) · [U10 · Compose and Views](#u10) · [V8 · Motion detection](#v8)

---

### <a id="v2"></a>V2. ★ What are the rules for camera permissions and background camera use?

**প্রশ্নটা মানে:** Android version অনুযায়ী camera/mic-এর privacy নিয়ম জানেন কিনা — security camera app-এর জন্য এটা সবচেয়ে বড় বাধা।
**অন্যভাবেও জিজ্ঞেস করে:** "Can your app record from the camera in the background?" · "What changed for camera in Android 14 and 15?"

**বুঝে নিন:**
- **Runtime permission:** `CAMERA`, আর audio-র জন্য `RECORD_AUDIO`। কেন দরকার আগে বোঝান, তারপর চান। Deny হলে feature বন্ধ, app crash না।
- **Version অনুযায়ী নিয়ম:**

| Version | নিয়ম |
|---|---|
| Android 9 | background-এ (idle uid) camera/mic access নেই — frame আসে না বা error |
| Android 11 | background থেকে চালু করা FGS camera/mic পায় না ("while-in-use"); one-time permission |
| Android 12 | status bar-এ camera/mic indicator; Quick Settings-এ camera/mic **toggle** — off থাকলে কালো frame/silence |
| Android 14 | FGS-এ `foregroundServiceType="camera"` + `FOREGROUND_SERVICE_CAMERA`; startForeground-এর আগে CAMERA permission granted থাকতে হবে |
| Android 15 | `BOOT_COMPLETED` receiver থেকে `camera`/`microphone` FGS চালু করা যায় না |

- **ঠিক pattern:** user app খোলা অবস্থায় (visible) "Start monitoring" চাপলে তখন FGS শুরু করুন, ongoing notification সহ। এরপর screen off হলেও camera চলবে।
- **Toggle off থাকলে:** `SensorPrivacyManager` দিয়ে toggle support আছে কিনা দেখা যায়। Camera খুললে system user-কে toggle চালু করার dialog দেখায়। App-এ পরিষ্কার message দিন ("Camera is blocked in quick settings")।
- **Play policy:** FGS type-এর জন্য Play Console-এ declaration আর video লাগে; কারণ সত্যিকারের user-visible feature হতে হবে।

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_CAMERA" />
<service android:name=".MonitorService" android:exported="false"
    android:foregroundServiceType="camera|microphone" />
```

**Answer (English):**
> "I need the CAMERA runtime permission, and RECORD_AUDIO for sound. Since Android 9, an app in the background cannot use the camera at all. So for monitoring, the user starts it from a visible screen, and I start a foreground service with type camera and a clear notification. Since Android 14, that type and its FOREGROUND_SERVICE_CAMERA permission are required, and the camera permission must already be granted. Android 15 blocks starting a camera foreground service from BOOT_COMPLETED, so monitoring cannot auto-start after reboot on a normal phone. Since Android 12, users see a camera indicator and can block the camera with a toggle, so I handle black frames with a clear message."

**Key words:** `CAMERA` · `foregroundServiceType="camera"` · `while-in-use` · `privacy indicators` · `sensor privacy toggle` · `BOOT_COMPLETED`

**Follow-up:**
- **Q:** How do you restart monitoring after a reboot on Android 15?
  **A:** "On a normal phone, I show a notification asking the user to open the app and resume. On our own dedicated hardware, we can run as a system or device-owner app with different rules."
- **Q:** What happens if the user turns off the camera toggle while recording?
  **A:** "The camera keeps running but gives black frames. I detect it, stop or mark the recording, and tell the user."

**ভুল করবেন না:** "WorkManager দিয়ে background-এ camera চালাবো" — এটা কাজ করবে না।

**আরও দেখুন:** [C7 · Foreground services](#c7) · [C13 · Runtime permissions](#c13) · [V11 · 24/7 monitoring](#v11)

---

### <a id="v3"></a>V3. ★ How do you play a live stream from an IP camera?

**প্রশ্নটা মানে:** কোন protocol কখন, latency-র trade-off, আর Android-এ বাস্তবে কীভাবে চালান।
**অন্যভাবেও জিজ্ঞেস করে:** "RTSP vs HLS vs WebRTC?" · "How do you get low latency live video?"

**বুঝে নিন:**

| Protocol | সাধারণ latency | কোথায় ভালো | সমস্যা |
|---|---|---|---|
| RTSP (RTP over UDP/TCP) | ১ সেকেন্ডের কম | LAN, NVR, প্রায় সব IP camera-তে আছে | internet/NAT পার হয় না সহজে; নিজে encrypt না |
| WebRTC | ~০.৫ সেকেন্ড বা কম | internet-এ live view, two-way audio | signaling, STUN/TURN server লাগে, জটিল |
| HLS | কয়েক থেকে ৩০ সেকেন্ড | cloud playback, CDN, recording | latency বেশি |
| LL-HLS | কয়েক সেকেন্ড | cloud live, CDN scale | server support লাগে |
| RTMP | কয়েক সেকেন্ড | মূলত camera → server ingest | playback-এ আর জনপ্রিয় না |

(সংখ্যাগুলো সাধারণ ধারণা; network আর setup অনুযায়ী বদলায়।)

- **সাধারণ product design:** LAN-এ থাকলে RTSP direct; বাইরে থেকে live হলে WebRTC; পুরনো recording/timeline HLS।
- **Media3 ExoPlayer দিয়ে RTSP** (`media3-exoplayer-rtsp`):

```kotlin
val player = ExoPlayer.Builder(context).build()
val source = RtspMediaSource.Factory()
    .setForceUseRtpTcp(true)   // UDP firewall/NAT-এ আটকালে
    .createMediaSource(MediaItem.fromUri("rtsp://192.168.1.20:554/stream2"))
player.setMediaSource(source)
player.prepare()
player.play()
```

- Camera-র user/password URI-তে দেওয়া যায় (`rtsp://user:pass@host/...`) — তবে URL **log করবেন না**।
- HLS: `media3-exoplayer-hls`, `MediaItem.fromUri(".../index.m3u8")`। Live-এ `LiveConfiguration` দিয়ে target offset ঠিক করা যায়।
- WebRTC: Google-এর prebuilt `org.webrtc:google-webrtc` artifact অনেক আগেই বন্ধ (শেষ update 2020 সালের দিকে, JCenter-এর সাথে চলে গেছে)। দল সাধারণত নিজে libwebrtc build করে বা পরিচিত third-party build ব্যবহার করে। Team-এর setup জিজ্ঞেস করুন।
- **Android 17:** target 37 হলে LAN-এর camera-র সাথে TCP/UDP-তে `ACCESS_LOCAL_NETWORK` runtime permission লাগে (NEARBY_DEVICES group)। Permission না থাকলে TCP সাধারণত timeout দেয়, UDP `EPERM` — তাই error message ঠিক দিন। NsdManager-এর system picker দিয়ে পাওয়া address-এ permission লাগে না।
- Latency কমাতে: buffer ছোট (`DefaultLoadControl`), ছোট GOP camera-তে, UDP যেখানে সম্ভব।

**Answer (English):**
> "It depends on where the viewer is. On the same Wi-Fi, I use RTSP directly, because almost every IP camera supports it and latency is under a second. I play it with Media3 ExoPlayer and RtspMediaSource, and I can force RTP over TCP if UDP is blocked. From outside the home, I prefer WebRTC for live view, because it gets very low latency through NAT with STUN and TURN, but it needs signaling servers. For recorded clips and cloud playback, HLS is simple and works with a CDN, but latency is several seconds. On Android 17, a LAN camera also needs the ACCESS_LOCAL_NETWORK permission."

**Key words:** `RTSP` · `RtspMediaSource` · `WebRTC` · `LL-HLS` · `latency trade-off` · `ACCESS_LOCAL_NETWORK`

**Follow-up:**
- **Q:** Why not use RTSP over the internet?
  **A:** "It needs open ports on the home router, which is a big security risk, and plain RTSP is not encrypted. A cloud relay or WebRTC is safer."
- **Q:** The stream has 5 seconds delay. Where do you look?
  **A:** "First the protocol, HLS is slow by design. Then the player buffer, and then the camera's keyframe interval, because the player waits for a keyframe to start."
- **Q:** Does Media3 still use the old ExoPlayer package?
  **A:** "No. The old com.google.android.exoplayer2 is deprecated. Media3 under androidx.media3 is the current one."

**ভুল করবেন না:** প্রতিটা protocol-কে "best" বলবেন না — latency, scale আর security-র trade-off বলুন।

**আরও দেখুন:** [V13 · Bad network](#v13) · [V7 · Find LAN cameras](#v7) · [F6 · SurfaceView vs TextureView](#f6)

---

### <a id="v4"></a>V4. ★ How do you show many camera feeds at once?

**প্রশ্নটা মানে:** ৪/৯/১৬টা live tile দেখাতে phone-এর hardware সীমা বোঝেন কিনা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you build a 16-camera grid without crashing?" · "SurfaceView or TextureView for video?"

**বুঝে নিন:**
- **সীমা ১ — decoder:** hardware decoder instance আর মোট pixel-rate সীমিত। ১৬টা 4K stream কোনো phone চালাতে পারবে না।
  - Runtime-এ check: `MediaCodecInfo.CodecCapabilities.maxSupportedInstances`, আর `VideoCapabilities.supportedPerformancePoints` (API 29+, যেমন কতগুলো 1080p30 একসাথে)।
  - সংখ্যা chip অনুযায়ী আলাদা — hardcode না, measure করুন।
- **মূল কৌশল — substream:** বেশিরভাগ IP camera দুটো stream দেয়: **main** (যেমন 4K/1080p, H.265) আর **sub** (যেমন 640×360, কম fps)। Grid-এ sub, একটা tile tap করলে full screen-এ main।
- **SurfaceView vs TextureView:**

| | SurfaceView | TextureView |
|---|---|---|
| Path | আলাদা layer, hardware overlay হতে পারে | GPU texture-এ copy |
| Battery/GPU | কম খরচ | বেশি খরচ, বেশি memory |
| Animation, alpha, rotate | সীমিত | সহজ |
| পছন্দ | live video, grid | শুধু animation দরকার হলে |

  Compose-এ Media3-এর `PlayerSurface(player, surfaceType = SURFACE_TYPE_SURFACE_VIEW)` (`media3-ui-compose`)।
- **Off-screen pause:** দেখা যাচ্ছে না এমন tile-এর player stop/release। `LazyVerticalGrid`-এ `DisposableEffect` দিয়ে tile চলে গেলে `release()`।
- **Player pool:** দ্রুত scroll-এ বারবার create/release করলে খরচ বেশি — কয়েকটা player reuse করুন।
- **Audio:** grid-এ সব mute, focused tile-এ শুধু audio।
- **Thermal:** `PowerManager.addThermalStatusListener` — গরম হলে fps কমান বা কিছু tile-কে snapshot (প্রতি কয়েক সেকেন্ডে একটা ছবি) বানান।
- **Memory:** প্রতিটা player-এর buffer আছে — live-এ buffer ছোট রাখুন।
- **Software decoder fallback** (যেমন FFmpeg extension) CPU গরম করে — grid-এ এড়ান।

**Answer (English):**
> "The hard limit is the hardware decoder. A phone can decode only a few high-resolution streams at once, and the number depends on the chip. So I check codec capabilities at runtime instead of guessing. For the grid, I use each camera's low-resolution substream, and only the full-screen view uses the main stream. I render with SurfaceView because it uses less GPU and battery than TextureView. Tiles that go off screen release their player, and I reuse a small pool of players. All tiles are muted except the focused one. I also listen to thermal status, and if the phone gets hot, I lower frame rate or switch some tiles to snapshots."

**Key words:** `substream` · `maxSupportedInstances` · `SurfaceView` · `player pool` · `thermal status`

**Follow-up:**
- **Q:** When would you use TextureView?
  **A:** "When the video needs animation, transparency or rotation inside the UI. For a plain live grid, SurfaceView is better."
- **Q:** What if the camera has no substream?
  **A:** "Then I show fewer live tiles, and the rest show snapshots that refresh every few seconds. Or the server makes a low-res version."

**ভুল করবেন না:** প্রতিটা tile-এ main stream চালিয়ে "phone slow" বলা — আসল কারণ decoder limit।

**আরও দেখুন:** [F6 · SurfaceView vs TextureView](#f6) · [V14 · Snapshots](#v14) · [U6 · Fast lazy lists](#u6)

---

### <a id="v14"></a>V14. ◆ How do you take a snapshot or thumbnail from a live stream or video?

**প্রশ্নটা মানে:** Live view-এর "Snapshot" button, grid-এর thumbnail, বা recording timeline-এর ছোট ছবি — কোথা থেকে আর কীভাবে নেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you capture a frame from ExoPlayer?" · "How do you make thumbnails for a recording timeline?"

**বুঝে নিন:**
- আগে ভাবুন: ছবিটা কোথা থেকে নেওয়া সবচেয়ে সস্তা?

| কোথা থেকে | কীভাবে | কখন |
|---|---|---|
| Camera নিজে | ONVIF `GetSnapshotUri` বা vendor-এর snapshot URL → JPEG | grid thumbnail; phone-এ decode লাগে না |
| Server | event-এর সময় server JPEG বানিয়ে রাখে | motion alert (V9), timeline |
| SurfaceView (player) | `PixelCopy.request(surfaceView, bitmap, listener, handler)` | user "Snapshot" চাপলে — এখন যা দেখছে |
| TextureView | `textureView.getBitmap()` | সহজ, কিন্তু TextureView-এর GPU খরচ আছে (V4) |
| Recorded file | `MediaMetadataRetriever.getFrameAtTime(timeUs, OPTION_CLOSEST_SYNC)`, বা Media3 `FrameExtractor` (`media3-inspector-frame`, নতুন — version দেখে নিন) | timeline thumbnail |
| Phone-এর camera | CameraX `ImageCapture`, বা `PreviewView.bitmap` | নিজের camera থেকে ছবি |

- SurfaceView-এর pixel সাধারণ `View.draw()`-এ আসে না — কালো ছবি পাবেন। কারণ SurfaceView আলাদা surface-এ আঁকে। তাই `PixelCopy` (API 24+)।
- `OPTION_CLOSEST_SYNC` কাছের keyframe নেয় — দ্রুত। ঠিক ওই frame চাইলে `OPTION_CLOSEST` — ধীর, কারণ keyframe থেকে decode করতে হয়।
- Decode আর JPEG compress main thread-এ না। Bitmap ছোট করুন (যেমন 320px চওড়া), memory আর disk-এ cache করুন।
- Snapshot-ও video-র মতোই private: app-specific storage-এ encrypt করে রাখুন। Gallery-তে (`MediaStore`) শুধু user চাইলে। Share করতে `FileProvider`।

```kotlin
fun snapshot(view: SurfaceView, onDone: (Bitmap?) -> Unit) {
    val bitmap = Bitmap.createBitmap(view.width, view.height, Bitmap.Config.ARGB_8888)
    PixelCopy.request(view, bitmap, { result ->
        onDone(if (result == PixelCopy.SUCCESS) bitmap else null)
    }, Handler(Looper.getMainLooper()))
}
```

**Answer (English):**
> "First I pick the cheapest source. For grid thumbnails and alerts, I ask the camera or the server for a JPEG, for example with the ONVIF GetSnapshotUri call, so the phone does not decode video. When the user taps snapshot in live view, I copy the current frame from the SurfaceView with PixelCopy. A normal view draw gives a black image for a SurfaceView. For recordings, I use MediaMetadataRetriever with the closest keyframe, which is fast, or the Media3 frame extractor. I do this work off the main thread, scale the bitmap down and cache it. And I treat snapshots as private data, just like the video."

**Key words:** `PixelCopy` · `GetSnapshotUri` · `MediaMetadataRetriever` · `OPTION_CLOSEST_SYNC` · `thumbnail cache`

**Follow-up:**
- **Q:** Why is my SurfaceView screenshot black?
  **A:** "SurfaceView draws on its own surface, outside the normal view drawing. I use PixelCopy to read from that surface."
- **Q:** How do you show thumbnails on a 24-hour timeline fast?
  **A:** "The server makes small thumbnails at fixed times while it records. The app loads them like normal images with a cache, and does not decode video on the phone."

**ভুল করবেন না:** grid-এর thumbnail-এর জন্য প্রতিটা camera-র video phone-এ decode করবেন না — camera বা server-এর snapshot নিন।

**আরও দেখুন:** [V4 · Camera grid](#v4) · [V9 · Motion alerts](#v9) · [V3 · Live stream](#v3)

---

### <a id="v5"></a>V5. ★ How do you record video on the device?

**প্রশ্নটা মানে:** কোন API কোন level-এ, loop recording কীভাবে, file কোথায় আর কীভাবে নিরাপদ।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you build continuous loop recording?" · "MediaRecorder vs MediaCodec?"

**বুঝে নিন:**
- **তিন level:**

| API | কখন |
|---|---|
| CameraX `VideoCapture` + `Recorder` | phone-এর camera থেকে সহজ recording |
| `MediaRecorder` | পুরনো, সহজ, কম control |
| `MediaCodec` + `MediaMuxer` | পুরো control: custom pipeline, pre-roll buffer, stream আর file একসাথে |

```kotlin
val recorder = Recorder.Builder().setQualitySelector(QualitySelector.from(Quality.FHD)).build()
val videoCapture = VideoCapture.withOutput(recorder)
val output = FileOutputOptions.Builder(segmentFile)
    .setDurationLimitMillis(60_000)          // এক segment = ১ মিনিট
    .build()
recording = recorder.prepareRecording(context, output)
    .withAudioEnabled()                      // RECORD_AUDIO granted হতে হবে
    .start(mainExecutor) { event ->
        if (event is VideoRecordEvent.Finalize) segmentStore.onSegmentDone(event.outputResults.outputUri)
    }
```

- **Loop (continuous) recording:**
  - ছোট segment (যেমন ১ মিনিট) — app crash হলে শুধু শেষ segment হারায়।
  - মোট size-এর quota রাখুন। নতুন segment-এর আগে free space (`StatFs`) দেখুন, পুরনোটা মুছুন (event-এর সাথে যুক্ত clip "protected" রাখুন)।
  - CameraX-এ segment বদলাতে ছোট gap হয়। Gap-ছাড়া চাইলে MediaCodec-এর encoded output keyframe-এ কেটে নতুন file-এ লিখুন।
- **Pre-roll (event-এর আগের কয়েক সেকেন্ড):** encoded frame RAM-এ ring buffer-এ রাখুন। Motion হলে শেষ **keyframe থেকে** file-এ লেখা শুরু।
- **MP4 crash ঝুঁকি:** সাধারণ MP4-এর index (`moov`) শেষে লেখা হয়। হঠাৎ বন্ধ হলে file নষ্ট। উপায়: ছোট segment, বা **fragmented MP4** (Media3-এর muxer module-এ fragmented MP4 support আছে — version দেখে নিন)।
- **কোথায় রাখবেন:**
  - App-specific storage (`filesDir` বা `getExternalFilesDir`) — permission লাগে না, অন্য app দেখে না, uninstall-এ মুছে যায়। Security camera-র জন্য এটাই ঠিক।
  - `MediaStore` — user gallery-তে চাইলে (তখন private না)।
- **Encryption:** Tink **StreamingAead** (`AES256_GCM_HKDF_1MB`) — বড় file chunk করে encrypt, seek করেও পড়া যায়। Segment বন্ধ হলে encrypt, অথবা encrypting stream-এ সরাসরি লিখুন (muxer-এর seek দরকার হলে প্রথমটা সহজ)।

**Answer (English):**
> "For the phone camera, I use CameraX VideoCapture with Recorder. It is simple and handles device quirks. When I need full control, like a pre-event buffer, I use MediaCodec and MediaMuxer directly. For continuous recording, I write short segments, for example one minute each. A crash then loses only the last segment, because a normal MP4 is broken if its index is not written. I keep a storage quota, check free space, and delete the oldest segments first, but never clips linked to an event. Files go to app-specific storage, not the gallery, and I encrypt them with Tink streaming encryption."

**Key words:** `VideoCapture` · `Recorder` · `MediaCodec` · `MediaMuxer` · `loop recording` · `pre-roll buffer` · `StreamingAead`

**Follow-up:**
- **Q:** How do you save 10 seconds before a motion event?
  **A:** "I keep encoded frames in a ring buffer in memory. On motion, I start the file from the last keyframe in that buffer, then keep writing live frames."
- **Q:** Why short segments and not one big file?
  **A:** "A crash or power loss breaks only the last segment, and deleting old video is just deleting old files."

**ভুল করবেন না:** keyframe-এর মাঝখান থেকে file শুরু করবেন না — video প্রথম কয়েক সেকেন্ড ভাঙা দেখাবে।

**আরও দেখুন:** [V6 · Encoding basics](#v6) · [S11 · Data at rest](#s11) · [C17 · Storage](#c17)

---

### <a id="v6"></a>V6. ◆ Can you explain video encoding basics?

**প্রশ্নটা মানে:** Codec, bitrate, GOP-এর মতো setting বদলালে quality, storage আর latency-তে কী হয়।
**অন্যভাবেও জিজ্ঞেস করে:** "H.264 or H.265 for a camera?" · "What is a keyframe interval?"

**বুঝে নিন:**
- **Codec:**

| Codec | সুবিধা | অসুবিধা |
|---|---|---|
| H.264 (AVC) | সব জায়গায় decode হয় | একই quality-তে বেশি bitrate |
| H.265 (HEVC) | একই quality-তে অনেক কম bitrate | কিছু browser/পুরনো device-এ সমস্যা, patent licensing |
| AV1 | আরও ভালো compression, royalty-free | hardware encoder শুধু নতুন chip-এ |

- **Resolution × frame rate × bitrate** = quality আর storage। Security camera-তে প্রায়ই ১৫–২০ fps যথেষ্ট — movie-র মতো ৩০/৬০ লাগে না।
- **Bitrate mode:** CBR (stream-এর জন্য স্থির), VBR (storage-এ ভালো), CQ (quality স্থির)। Device সব mode support করে না — capability দেখুন।
- **GOP / keyframe interval:** I-frame পুরো ছবি; P/B frame শুধু পার্থক্য।
  - ছোট interval (১–২ সেকেন্ড): live view দ্রুত শুরু হয়, seek ভালো, কিন্তু বেশি bitrate।
  - বড় interval: কম storage, কিন্তু player বেশি অপেক্ষা করে আর একটা packet হারালে বেশিক্ষণ ভাঙা ছবি।
  - কিছু camera "smart codec" — scene স্থির থাকলে GOP বাড়ায়।
- **Hardware encoder:** দ্রুত আর কম battery; software encoder (যেমন `c2.android.*`) ধীর। API 29+ এ `MediaCodecInfo.isHardwareAccelerated`।

```kotlin
val format = MediaFormat.createVideoFormat(MediaFormat.MIMETYPE_VIDEO_HEVC, 1920, 1080).apply {
    setInteger(MediaFormat.KEY_COLOR_FORMAT, MediaCodecInfo.CodecCapabilities.COLOR_FormatSurface)
    setInteger(MediaFormat.KEY_BIT_RATE, 3_000_000)
    setInteger(MediaFormat.KEY_FRAME_RATE, 20)
    setInteger(MediaFormat.KEY_I_FRAME_INTERVAL, 2)   // seconds
}
val codecName = MediaCodecList(MediaCodecList.REGULAR_CODECS).findEncoderForFormat(format)
    ?: return useAvcFallback()
val encoder = MediaCodec.createByCodecName(codecName)
encoder.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
val inputSurface = encoder.createInputSurface()   // camera এই surface-এ লেখে
```

**Answer (English):**
> "H.264 plays everywhere, so it is the safe choice for sharing and the web. H.265 gives similar quality at a clearly lower bitrate, which saves storage and bandwidth, but some browsers and old devices have trouble with it. AV1 is even better, but hardware encoders are only on newer chips. For a security camera, I usually pick a medium frame rate, like 15 to 20, and a keyframe every one to two seconds, so live view starts fast. A longer keyframe interval saves space but makes start-up and recovery slower. I always check MediaCodecList for a hardware encoder and fall back to H.264 if HEVC is missing."

**Key words:** `H.264` · `HEVC` · `AV1` · `bitrate mode` · `GOP` · `MediaCodecList`

**Follow-up:**
- **Q:** Why does a live view start slowly sometimes?
  **A:** "The decoder needs a keyframe to start. If the camera sends one every 8 seconds, the user may wait up to 8 seconds. A shorter keyframe interval or asking the camera for a keyframe fixes it."

**আরও দেখুন:** [V5 · Record video](#v5) · [V3 · Live stream](#v3)

---

### <a id="v7"></a>V7. ◆ How do you find cameras on the local network?

**প্রশ্নটা মানে:** LAN discovery protocol, Android-এর permission/lock, আর নতুন camera setup-এর security।
**অন্যভাবেও জিজ্ঞেস করে:** "How does ONVIF discovery work?" · "How do you add a new camera in the app?"

**বুঝে নিন:**
- **ONVIF** (IP camera-র common standard):
  - **WS-Discovery:** app UDP **multicast** `239.255.255.250:3702`-এ একটা SOAP `Probe` পাঠায় (type `NetworkVideoTransmitter`)। Camera `ProbeMatch` দিয়ে উত্তর দেয় — তার device service URL (`XAddrs`) সহ।
  - এরপর SOAP call: `GetProfiles` → `GetStreamUri` (RTSP URL পাওয়া), WS-UsernameToken (digest) auth দিয়ে।
  - Profile: S (streaming), T (advanced streaming, H.265), G (recording) ইত্যাদি।
- **mDNS / DNS-SD:** `NsdManager.discoverServices("_rtsp._tcp", ...)` বা vendor-এর service type। API 34+ এ resolve-এর জন্য `registerServiceInfoCallback`।
- **MulticastLock:** অনেক Wi-Fi driver battery বাঁচাতে multicast packet ফেলে দেয়। উত্তর পেতে:
  ```kotlin
  val lock = wifiManager.createMulticastLock("onvif-discovery").apply { setReferenceCounted(false) }
  lock.acquire()
  try { sendProbeAndCollect(timeout = 3.seconds) } finally { lock.release() }
  ```
  Permission: `CHANGE_WIFI_MULTICAST_STATE`। শুধু discovery-র সময় ধরে রাখুন — battery।
- **Android 17 (target 37):** multicast, UDP, TCP — সব LAN traffic-এ `ACCESS_LOCAL_NETWORK` লাগে। দুই পথ:
  - `NsdManager` + `DiscoveryRequest.FLAG_SHOW_PICKER` — system picker, user একটা device বাছে; সেই address-এ permission লাগে না।
  - ONVIF WS-Discovery-র মতো raw multicast হলে permission চাইতেই হবে। কেন দরকার আগে বুঝিয়ে বলুন।
- **বিকল্প পথ:** QR code (camera-র গায়ে) বা manual IP — এটাই সবচেয়ে ভরসার পথ।
- **Default password ঝুঁকি:** বহু camera `admin/admin` নিয়ে আসে — botnet-এর সবচেয়ে বড় পথ। Setup-এ password বদলানো **জরুরি** করে দিন; নিজের camera হলে প্রতিটা device-এ আলাদা password বা pairing code। কিছু দেশে আইনও এটা চায় (যেমন UK-র PSTI নিয়ম universal default password নিষেধ করে) — বিস্তারিত legal team-এর কাছে।

**Answer (English):**
> "For ONVIF cameras, I send a WS-Discovery probe as UDP multicast to port 3702, and cameras reply with their service address. Then I call GetProfiles and GetStreamUri to get the RTSP URL. For cameras that use mDNS, I use NsdManager. Many Wi-Fi chips drop multicast to save battery, so I hold a MulticastLock only during discovery. When we target Android 17, all of this needs the ACCESS_LOCAL_NETWORK permission, unless I use the NsdManager system picker. Discovery can miss devices, so I also support QR code and manual IP. During setup, I force the user to change any default password, because default passwords are the main way cameras get hacked."

**Key words:** `ONVIF` · `WS-Discovery` · `NsdManager` · `MulticastLock` · `ACCESS_LOCAL_NETWORK` · `default password`

**Follow-up:**
- **Q:** Discovery works on one phone but not another. Why?
  **A:** "Often the Wi-Fi driver filters multicast, or the router blocks it, or the phone is on a guest network. The MulticastLock and a manual IP fallback help."

**আরও দেখুন:** [V10 · Secure streams](#v10) · [C13 · Runtime permissions](#c13) · [V3 · Live stream](#v3)

---

### <a id="v8"></a>V8. ◆ How do you do motion detection and AI on the device?

**প্রশ্নটা মানে:** Frame analysis pipeline, performance নিয়ন্ত্রণ, আর on-device vs cloud সিদ্ধান্ত।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you run ML on camera frames without killing the battery?" · "On-device or cloud detection?"

**বুঝে নিন:**
- **Pipeline (ধাপে ধাপে, সস্তা থেকে দামি):**
  1. **Motion:** Y (luma) plane-এ ছোট resolution-এ frame difference — খুব সস্তা।
  2. Motion হলে তবেই **ML:** person / vehicle / animal detection।
  3. Result পাকা হলে event পাঠান (V9)।
- **CameraX `ImageAnalysis`:**
  - `STRATEGY_KEEP_ONLY_LATEST` (default) — analyzer ধীর হলে পুরনো frame ফেলে শুধু নতুনটা দেয়; queue জমে না, latency বাড়ে না।
  - `image.close()` না দিলে নতুন frame আর আসে না — সবচেয়ে common bug।
  - ছোট target resolution (`ResolutionSelector`), দরকারে `OUTPUT_IMAGE_FORMAT_RGBA_8888`।
  - **Frame skipping:** ২–৫ fps-এ analysis যথেষ্ট।
- **IP camera stream-এ:** decoder output `ImageReader`-এ নিয়ে একই pipeline; অথবা substream decode করে analysis।
- **Tool:**
  - **ML Kit** — ready-made (object detection, face, barcode), সহজ।
  - **LiteRT** (আগের TensorFlow Lite নাম) — নিজের model; GPU/NPU accelerator দিয়ে দ্রুত। Model quantize (int8) করলে ছোট আর দ্রুত।
  - Gemini Nano (ML Kit GenAI) — নতুন, সীমিত device; clip-এর description বানানোর মতো কাজে ভাবা যায়।
- **Thermal ও battery:** `PowerManager.currentThermalStatus` / listener; গরম হলে fps কমান, model ছোট করুন।
- **On-device vs cloud:**

| | On-device | Cloud |
|---|---|---|
| Privacy | video বাইরে যায় না | video upload লাগে |
| Latency | কম | network-নির্ভর |
| Accuracy | ছোট model | বড় model |
| খরচ | device battery/heat | server খরচ, bandwidth |

  সাধারণ hybrid: device-এ motion + ছোট model filter, শুধু সন্দেহজনক clip cloud-এ।

**Answer (English):**
> "I build it as a cheap-to-expensive pipeline. First, simple motion detection on the luma plane at low resolution, which costs almost nothing. Only when there is motion, I run an ML model, with ML Kit for ready-made detection or LiteRT for our own model on the GPU or NPU. With CameraX ImageAnalysis, I use the keep-only-latest strategy so frames never queue up, and I always close each image. I analyze only a few frames per second and lower the rate when the thermal status rises. On-device is better for privacy and latency. Cloud gives bigger models. A hybrid often works best: filter on the device, confirm in the cloud."

**Key words:** `ImageAnalysis` · `STRATEGY_KEEP_ONLY_LATEST` · `ML Kit` · `LiteRT` · `frame skipping` · `thermal status`

**Follow-up:**
- **Q:** The analyzer stopped getting frames. What is the first thing you check?
  **A:** "Whether every ImageProxy is closed, on every path, including errors. If one is not closed, CameraX stops sending new frames."
- **Q:** How do you reduce false alarms from trees or rain?
  **A:** "Detection zones set by the user, a minimum object size, a person or vehicle model after motion, and a short cooldown between alerts."

**আরও দেখুন:** [V9 · Motion alerts](#v9) · [D1 · Security camera app design](#d1) · [P7 · Battery](#p7)

---

### <a id="v9"></a>V9. ★ How do you send motion alert notifications?

**প্রশ্নটা মানে:** Server থেকে phone-এ দ্রুত, ঠিকমতো পৌঁছানো, privacy-safe alert — Doze আর Android নিয়ম মেনে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you show a snapshot in the notification?" · "Why do some alerts arrive late?"

**বুঝে নিন:**
- **Flow:** camera event → server → FCM **high-priority data message** (`eventId`, `cameraId`, ছোট-মেয়াদি signed snapshot URL) → app `onMessageReceived` → notification।
- **High priority:** Doze-এর মধ্যেও phone জাগায়। কিন্তু high-priority message থেকে user-visible notification না দেখালে FCM পরে আপনার message **normal priority-তে নামিয়ে দিতে পারে**। `getPriority()` বনাম `getOriginalPriority()` দেখে বোঝা যায়।
- **সময় কম:** `onMessageReceived`-এ মাত্র কয়েক সেকেন্ড। আগে text notification দেখান, snapshot download হলে একই id-তে update। ভারী কাজ WorkManager expedited job-এ।
- **Notification:**
  - Android 13+: `POST_NOTIFICATIONS` runtime permission।
  - Channel: "Motion alerts" (high importance), "Device status" (low) — user আলাদা করে বন্ধ করতে পারে।
  - Snapshot: `BigPictureStyle`। Camera অনুযায়ী group।
  - **Lock screen privacy:** `VISIBILITY_PRIVATE` + public version-এ ছবি ছাড়া text (S11)।
- **Tap:** explicit intent, `FLAG_IMMUTABLE`, deep link → সেই camera-র live view বা event clip; `TaskStackBuilder` দিয়ে back stack ঠিক।

```kotlin
val openClip = Intent(context, MainActivity::class.java)
    .setAction(Intent.ACTION_VIEW)
    .setData("app://camera/$cameraId/event/$eventId".toUri())
val notification = NotificationCompat.Builder(context, CHANNEL_MOTION)
    .setSmallIcon(R.drawable.ic_motion)
    .setContentTitle("Motion at $cameraName")
    .setStyle(NotificationCompat.BigPictureStyle().bigPicture(snapshot))
    .setVisibility(NotificationCompat.VISIBILITY_PRIVATE)
    .setPublicVersion(publicNotification)          // ছবি ছাড়া
    .setContentIntent(PendingIntent.getActivity(context, eventId.hashCode(), openClip,
        PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT))
    .setAutoCancel(true)
    .build()
```

- **Full-screen intent:** Android 14 থেকে `USE_FULL_SCREEN_INTENT` সীমিত — Play policy-তে মূলত calling আর alarm app। Motion alert সাধারণত যোগ্য না। Doorbell "ring" call-এর মতো কিনা সেটা policy দেখে সিদ্ধান্ত। `NotificationManager.canUseFullScreenIntent()` দিয়ে check।
- **Server-এ:** একই camera-তে cooldown/merge (৩০ সেকেন্ডে ১০টা alert না), event store করে তারপর push, যাতে tap করলে clip সত্যিই থাকে।

**Answer (English):**
> "The server sends an FCM high-priority data message with the event id, camera id and a short-lived snapshot link. High priority wakes the phone even in Doze, but only if we really show a notification, otherwise FCM can lower our priority later. onMessageReceived has only a few seconds, so I show the text notification first, then update it with the snapshot. I use a high-importance motion channel and BigPictureStyle. On the lock screen, I show a private version without the image, because it is someone's home. Tapping opens the live view or the clip through an immutable PendingIntent and a deep link. Full-screen intents are only for calling and alarm apps, so I do not rely on them."

**Key words:** `FCM high priority` · `data message` · `BigPictureStyle` · `VISIBILITY_PRIVATE` · `full-screen intent` · `Doze`

**Follow-up:**
- **Q:** Some users get alerts late. Why?
  **A:** "Maybe FCM lowered the priority because messages did not show notifications, or the app is in a restricted battery bucket, or the OEM kills apps. I check delivery data and the priority fields."
- **Q:** Why not put the snapshot image inside the FCM message?
  **A:** "FCM payloads are small, around 4 KB. I send a short-lived signed URL instead."
- **Q:** How do you stop alert spam?
  **A:** "The server merges events per camera with a cooldown, and users can set schedules and zones."

**ভুল করবেন না:** lock screen-এ ঘরের ভেতরের ছবি দেখানো — এটা privacy bug।

**আরও দেখুন:** [C15 · Notifications and push](#c15) · [S11 · Lock screen privacy](#s11) · [V14 · Snapshots](#v14)

---

### <a id="v10"></a>V10. ★ How do you secure camera streams and recordings?

**প্রশ্নটা মানে:** Camera থেকে viewer পর্যন্ত পুরো পথের security — এই company-র সবচেয়ে গুরুত্বপূর্ণ প্রশ্ন হতে পারে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you make sure only the owner can watch a camera?" · "Would you offer end-to-end encryption?"

**বুঝে নিন:**
- **স্তর ধরে:**

| স্তর | কী করি |
|---|---|
| Transport | API-তে TLS; WebRTC-তে DTLS-SRTP (WebRTC-তে এটা লাগবেই); RTSP বাইরে খোলা না — cloud-এ RTSPS/TLS tunnel |
| Access | প্রতি stream request-এ server check: এই user এই camera দেখতে পারে কি? ছোট-মেয়াদি **signed URL / token** (মিনিট), নির্দিষ্ট camera আর user-এ বাঁধা |
| Pairing | camera ↔ account বাঁধা একবারের code/QR দিয়ে, physical access লাগে; camera-র নিজস্ব identity (device certificate, mTLS) |
| Camera | default password না; port forwarding/UPnP-র দরকার নেই — camera নিজে outbound connection খোলে; signed firmware, secure boot |
| Storage | recording encrypted at rest (cloud-এ আর phone-এ) |
| E2EE (option) | key শুধু user-এর device-এ; cloud শুধু encrypted bytes রাখে |
| Audit | কে কখন live দেখল, কে share করল, কে delete করল — user-কে দেখান |

- **Sharing:** role (owner / viewer / time-limited guest), access revoke করলে **চলমান stream-ও বন্ধ** — তাই token ছোট-মেয়াদি।
- **IDOR:** `/cameras/{id}/live` — id বদলে অন্যের camera? Server-এ সবসময় ownership check। এটা camera company-গুলোর সবচেয়ে common বড় বাগ।
- **E2EE-এর trade-off:** সবচেয়ে বেশি privacy, কিন্তু cloud AI detection, web viewer আর নতুন phone-এ key সরানো কঠিন; key হারালে recording হারায়। সাধারণত "option" হিসেবে দেওয়া হয়।
- **আইন/নিয়ম:** connected device-এর security নিয়ে নতুন আইন আসছে (UK PSTI, EU Cyber Resilience Act, EU radio equipment cybersecurity নিয়ম) — তারিখ আর শর্ত compliance team-এর কাছে দেখে নিন।

**Answer (English):**
> "I secure every hop. All traffic is encrypted: TLS for APIs, and DTLS-SRTP for WebRTC. The camera opens an outbound connection to our cloud, so users never open router ports. For access, every stream request goes through the server, which checks that this user may see this camera, and returns a token or signed URL that lives only a few minutes. Pairing needs a one-time code from the physical camera, and each camera has its own certificate. Cameras never ship with a shared default password. Recordings are encrypted at rest. I would offer end-to-end encryption as an option, but it has trade-offs, like no cloud AI. Finally, an audit log shows who watched what and when."

**Key words:** `DTLS-SRTP` · `signed URL` · `device pairing` · `mTLS` · `end-to-end encryption` · `audit log` · `IDOR`

**Follow-up:**
- **Q:** What is the most common security bug in camera platforms?
  **A:** "Broken access control, like changing a camera id in the request and seeing someone else's camera. I test that first."
- **Q:** If a user removes a shared viewer, how fast does access stop?
  **A:** "New tokens are refused at once, and because stream tokens live only minutes, the open stream ends soon. For instant cut-off, the server also closes the active session."
- **Q:** Why not let users connect to the camera with port forwarding?
  **A:** "It puts the camera directly on the internet, where bots scan for weak passwords and old firmware all day."

**ভুল করবেন না:** শুধু "TLS দিই" বলে থামবেন না — access control আর pairing-ই আসল জায়গা।

**আরও দেখুন:** [S5 · Network security](#s5) · [S15 · Session security](#s15) · [D1 · Security camera app design](#d1)

---

### <a id="v11"></a>V11. ◆ How do you build a 24/7 monitoring or recording app?

**প্রশ্নটা মানে:** Android-এর battery নিয়ম মেনে কীভাবে সারাদিন চালান, আর কখন phone-এর বদলে dedicated device ঠিক।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you keep the app alive all the time?" · "Old phone as a security camera — how?"

**বুঝে নিন:**
- **Normal phone-এ:**
  - Visible অবস্থায় user শুরু করবে → FGS (`camera`, দরকারে `microphone`) + ongoing notification (V2)।
  - **Battery optimization exemption** (`REQUEST_IGNORE_BATTERY_OPTIMIZATIONS`): Play policy-তে শুধু নির্দিষ্ট ক্ষেত্রে অনুমতি — core feature হলে যুক্তি দেখাতে হয়। অনেক OEM তবুও app মেরে ফেলে — user-কে setting দেখানো guide রাখুন।
  - **Wake lock:** FGS চললে আর camera active থাকলে CPU চলে; আলাদা partial wake lock শুধু যেখানে সত্যি দরকার। Android vitals-এ **excessive partial wake lock** এখন core metric — বেশি হলে Play-তে visibility কমতে পারে।
  - **Boot:** Android 15 থেকে `BOOT_COMPLETED` থেকে camera FGS না — reboot-এর পর user-কে notification দিয়ে আবার শুরু করতে বলুন।
  - **Storage, heat, charging:** loop recording quota (V5); thermal throttle হলে fps কমান; সবসময় charger-এ থাকলে battery ফুলে যাওয়ার ঝুঁকি — user-কে জানান।
  - Background IP-stream recording phone-এ কঠিন — `dataSync` আর `mediaProcessing` type-এ Android 15 থেকে সময়-সীমা আছে। এই কাজ server বা NVR-এ ভালো।
- **Dedicated device / custom hardware-এ:**
  - Device Owner + lock task (kiosk) (S13), বা নিজেদের AOSP build-এ **system/privileged app** — তখন অনেক background নিয়ম আলাদা।
  - System app-এ `android:persistent="true"` (শুধু system app-এ কাজ করে) — crash হলে system আবার চালায়।
  - Screen-এর জন্য `FLAG_KEEP_SCREEN_ON` (monitor wall)।
  - Watchdog: stream বন্ধ হলে নিজে reconnect; health heartbeat server-এ।
  - OTA, `SystemUpdatePolicy` — রাত ৩টায় update, recording-এর মাঝখানে না।

**Answer (English):**
> "On a normal phone, I follow the rules, not fight them. The user starts monitoring from a visible screen, and I run a camera-type foreground service with a clear notification. I ask for battery optimization exemption only if it is a core feature, because Play limits it, and I guide users through OEM battery settings. I avoid extra wake locks, because Android vitals now flags them. After reboot, Android 15 does not allow a camera service to start from boot, so I ask the user to resume. For true 24/7 use, I recommend a dedicated device: Device Owner and kiosk mode, or a system app on our own Android build, with a watchdog and a server heartbeat."

**Key words:** `foreground service` · `battery optimization exemption` · `partial wake lock` · `lock task mode` · `persistent system app` · `heartbeat`

**Follow-up:**
- **Q:** How do you know the device is still recording?
  **A:** "It sends a heartbeat to the server every minute with its status. If heartbeats stop, the server alerts the owner."

**ভুল করবেন না:** "Service-কে START_STICKY দিলেই সব ঠিক" — আধুনিক Android-এ এটা যথেষ্ট না।

**আরও দেখুন:** [C7 · Foreground services](#c7) · [P7 · Battery](#p7) · [O9 · Kiosk device](#o9)

---

### <a id="v12"></a>V12. ○ How do you build two-way audio?

**প্রশ্নটা মানে:** Doorbell/camera-তে কথা বলার feature — audio capture, playback, আর echo সমস্যা।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you stop echo in two-way talk?" · "AudioRecord or MediaRecorder for live talk?"

**বুঝে নিন:**
- **Low-level API:** `AudioRecord` (mic থেকে PCM) → encode (Opus/AAC/G.711, camera যা চায়) → network; উল্টো দিকে decode → `AudioTrack`। Live talk-এ `MediaRecorder` না — সে file লেখে।
- **Echo:** phone-এর speaker-এর আওয়াজ mic-এ ঢুকে আবার camera-তে যায়।
  - `AudioManager.mode = MODE_IN_COMMUNICATION` আর `AudioSource.VOICE_COMMUNICATION` — অনেক device-এ platform echo cancellation আর noise suppression চালু হয়।
  - `AcousticEchoCanceler.isAvailable()` হলে `AcousticEchoCanceler.create(audioRecord.audioSessionId)`।
  - Device অনুযায়ী মান আলাদা — বাস্তব phone-এ test।
- **WebRTC** নিজের audio pipeline (software AEC, noise suppression, jitter buffer) নিয়ে আসে — live video WebRTC-তে থাকলে audio-ও সেখানে রাখা সবচেয়ে সহজ।
- **Half-duplex বিকল্প:** "push to talk" — চাপলে শুধু পাঠায়, তখন playback mute। Echo প্রায় শেষ, UX সহজ।
- **Permission:** `RECORD_AUDIO`; background-এ talk চালাতে FGS type `microphone`।
- **Android 17 background audio hardening:** Android 17-এ সব app-এর জন্য background-এ audio চালাতে visible activity বা foreground service লাগে। Target 37 হলে সেই FGS-এর while-in-use capability লাগবে — মানে user-এর কাজে বা app দেখা যাওয়ার সময় শুরু হতে হবে। `BOOT_COMPLETED` থেকে শুরু FGS-এর audio চুপচাপ বন্ধ হয়ে যায়। বিস্তারিত Android 17 docs-এ।
- Audio routing: Bluetooth headset/speaker বদল — Android 12+ এ `setCommunicationDevice`।

**Answer (English):**
> "I capture with AudioRecord and play with AudioTrack, because live talk needs raw PCM, not files. The main problem is echo: the phone speaker leaks into the mic. I set the audio mode to communication and use the VOICE_COMMUNICATION source, which turns on platform echo cancellation on many devices, and I add AcousticEchoCanceler when it is available. Quality differs by device, so I test on real phones. If video already uses WebRTC, I use its audio too, because it has good echo cancellation and jitter handling. A simple option is push-to-talk, which removes most echo."

**Key words:** `AudioRecord` · `AudioTrack` · `VOICE_COMMUNICATION` · `AcousticEchoCanceler` · `push-to-talk`

**Follow-up:**
- **Q:** The camera side hears an echo. What do you try first?
  **A:** "Check that we use communication mode and the voice communication source, then lower speaker volume or switch to push-to-talk."

**আরও দেখুন:** [V3 · Live stream](#v3) · [C7 · Foreground services](#c7)

---

### <a id="v13"></a>V13. ◆ How do you handle a bad network during streaming?

**প্রশ্নটা মানে:** Mobile network-এ stream ভাঙবেই — আপনি কীভাবে recover করেন আর user-কে কী দেখান।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you reconnect a live stream?" · "What happens when Wi-Fi switches to mobile data?"

**বুঝে নিন:**
- **Network বদল শোনা:**
  ```kotlin
  connectivityManager.registerDefaultNetworkCallback(object : ConnectivityManager.NetworkCallback() {
      override fun onAvailable(network: Network) = streamController.reconnectNow()
      override fun onLost(network: Network) = streamController.showOffline()
      override fun onCapabilitiesChanged(network: Network, caps: NetworkCapabilities) {
          streamController.onMetered(!caps.hasCapability(NetworkCapabilities.NET_CAPABILITY_NOT_METERED))
      }
  })
  ```
  `NET_CAPABILITY_VALIDATED` দেখে বুঝুন সত্যিই internet আছে কিনা। Lifecycle-এর সাথে unregister।
- **Reconnect with backoff:** ১s, ২s, ৪s… সর্বোচ্চ ৩০s, সাথে random jitter (সব phone একসাথে server-এ আঘাত না করে)। Network ফিরলে backoff reset করে সাথে সাথে চেষ্টা।
  ```kotlin
  suspend fun <T> retryWithBackoff(block: suspend () -> T): T {
      var delayMs = 1_000L
      while (true) {
          try { return block() } catch (e: IOException) {
              delay(delayMs + Random.nextLong(delayMs / 2))
              delayMs = (delayMs * 2).coerceAtMost(30_000)
          }
      }
  }
  ```
- **Adaptive bitrate:**
  - HLS/DASH: player নিজে variant বদলায় (Media3 track selection)।
  - RTSP: নিজে সিদ্ধান্ত — বারবার buffering হলে substream-এ নামা।
  - WebRTC: congestion control নিজে bitrate কমায়; network বদলালে **ICE restart**।
- **Player error:** Media3 `Player.Listener.onPlayerError` — `ERROR_CODE_IO_*` হলে retry, `BEHIND_LIVE_WINDOW` হলে live edge-এ ফিরে যান (`seekToDefaultPosition()` + `prepare()`)।
- **User-কে দেখান:** "Connecting…", "Weak connection — showing lower quality", "Camera offline since 10:42" — শেষ frame ঝাপসা করে রাখুন, কালো screen না। Camera offline আর phone offline আলাদা message।
- **Metered network:** mobile data-তে default substream, user চাইলে HD।

**Answer (English):**
> "I listen to network changes with a default NetworkCallback. When the network drops, I show an offline state, and when a new network is available, I reconnect at once. Other failures retry with exponential backoff and jitter, up to about 30 seconds, so many phones do not hit the server at the same moment. For quality, HLS adapts by itself, WebRTC lowers bitrate by itself and needs an ICE restart after a network switch, and for RTSP I switch to the substream when buffering repeats. I always tell the user what is happening, like connecting, low quality, or camera offline, and I keep the last frame on screen instead of a black box."

**Key words:** `NetworkCallback` · `exponential backoff` · `jitter` · `adaptive bitrate` · `ICE restart` · `BEHIND_LIVE_WINDOW`

**Follow-up:**
- **Q:** How do you tell "camera offline" from "my phone is offline"?
  **A:** "If my network is validated and the API works but the camera has no recent heartbeat, the camera is offline. If my network is lost, it is the phone."
- **Q:** Why add jitter to backoff?
  **A:** "After a server outage, all clients would retry at the same seconds. Random jitter spreads the load."

**আরও দেখুন:** [R10 · Error handling](#r10) · [V3 · Live stream](#v3) · [D1 · Security camera app design](#d1)

---


## <a id="part-9"></a>Part 9 — Custom Android OS (AOSP) আর platform

এই company নিজের device (camera, sensor box) বানাতে পারে। তাহলে তারা নিজের Android build চালায়। তাই interview-এ AOSP, system app, SELinux, OTA, kiosk — এগুলো আসবে।
আপনি app developer। Platform engineer-এর মতো সব জানতে হবে না। কিন্তু দুইটা জিনিস পরিষ্কার বলতে হবে: layer-গুলো কীভাবে জোড়া লাগে, আর কোন কাজ কোন layer-এ করা উচিত। এটা পারলে platform team আপনাকে বিশ্বাস করবে।
ভালো answer pattern: "App side-এ আমি strong. Platform side-এ আমি জানি X কীভাবে কাজ করে, আর আমি Y এভাবে করতাম।"

### আগে বুঝুন — AOSP আর platform-এর বড় ছবি

এই part পড়ার নিয়ম: প্রথমে নিচের ৯টা point পড়ুন। তারপর প্রতিটা প্রশ্নের "এক কথায়" line পড়ুন। শেষে detail।

**১. AOSP কী।** Android-এর open source অংশ। Kernel থেকে Settings app পর্যন্ত। কিন্তু Google-এর app আর Play services (GMS) এর ভেতরে নেই। Pixel বা Samsung-এর Android = AOSP + vendor code + GMS।

**২. Layer-গুলো (উপর থেকে নিচে):**

```
Apps (আপনার app, system apps)
   │  Java/Kotlin API (android.*)
Framework  ── system_server (ActivityManager, PackageManager, LocationManager ...)
   │  Binder IPC
Native daemons + ART  (cameraserver, surfaceflinger, audioserver, ART runtime)
   │  Binder (AIDL HAL)
HAL  (vendor-এর code: camera, sensors, GPS ...)
   │  ioctl / sysfs / /dev/*
Linux kernel + drivers
```

**৩. Binder সব জোড়া লাগায়।** App সরাসরি hardware ছোঁয় না। ধাপগুলো:
1. App একটা manager class call করে (যেমন `CameraManager`)।
2. Call Binder দিয়ে অন্য process-এর service-এ যায়।
3. Service permission check করে, তারপর HAL call করে।
4. HAL kernel driver call করে।

**৪. Partition ভাগ (Treble)।** `system` = Google/AOSP অংশ। `vendor` = chip আর board-এর অংশ। দুইটার মাঝে একটা fixed interface (AIDL HAL + VINTF)। তাই vendor না ছুঁয়ে system update করা যায়।

**৫. Permission-এর স্তর।** Normal app < privileged app (`/system/priv-app`) < platform-signed app < `android.uid.system`। যত উপরে, তত ক্ষমতা, তত ঝুঁকি।

**৬. SELinux সবসময় on।** প্রতিটা process-এর একটা domain আছে। কোনো access-এর নিয়ম না থাকলে kernel block করে (`avc: denied`)। নতুন service বা daemon মানেই নতুন sepolicy।

**৭. Security chain।** Verified boot (AVB) প্রতিটা partition check করে। আপনার নিজের key দিয়ে sign করতে হয়। Test key দিয়ে ship করলে যে কেউ আপনার device-এ নিজের build বসাতে পারবে।

**৮. Update।** নিজের device = নিজের OTA। A/B বা Virtual A/B, `update_engine`, signed package, rollback protection, ধাপে ধাপে rollout।

**৯. 2026-এর অবস্থা।** Google এখন Android internal branch-এ বানায়। AOSP source বছরে দুইবার publish করে (Q2, Q4)। Build করুন `android-latest-release` থেকে। Monthly security patch আলাদা আসে। প্রতিটা নতুন release-এ নিজের change rebase করতে হয়। তাই custom change কম রাখুন।

**কোন কাজ কোথায় করবেন (সংক্ষেপে):**

| কাজ | সবচেয়ে সহজ জায়গা |
|---|---|
| Kiosk, auto-start, lock | Device Owner app (custom ROM লাগে না) |
| System setting বদলানো, silent install, reboot | Privileged / platform-signed app |
| নতুন hardware app-কে দেখানো | AIDL HAL + system service বা privileged service |
| Boot-এ native daemon | `init` `.rc` file + SELinux domain |

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ আপনি platform channel দিয়ে Android API call করতেন। এখানে আপনি সেই API-র নিচে কী আছে সেটা বদলাতে পারেন।
- Flutter app একটা APK। Platform কাজে আপনি পুরো OS image বানান (system.img, vendor.img, boot.img)।
- Build tool Gradle না। AOSP-এ Soong (`Android.bp`) আর `m`। Gradle app আলাদা build করে prebuilt হিসেবে বসানো যায়।
- Debug-এ `flutter logs` না, `adb logcat -b all`, `dumpsys`, tombstone, `dmesg`।

---

### <a id="o1"></a>O1. ★ What is AOSP, and how is it different from the Android on a Pixel or Samsung phone?

**প্রশ্নটা মানে:** আপনি কি জানেন AOSP-তে কী থাকে আর কী থাকে না, আর 2025–2026-এ কী বদলেছে?
**অন্যভাবেও জিজ্ঞেস করে:** "What do you get if you build Android from source?" · "What is GMS and why does it matter for a custom device?"

**বুঝে নিন:**
- **AOSP** = Android Open Source Project। Kernel (আলাদা repo), framework, ART, system apps (Settings, Launcher3, SystemUI), build system, CTS। License মূলত Apache 2.0 (kernel GPL)।
- **AOSP-তে যা নেই:** Google Play Store, Play services (GMS core), FCM, Fused Location Provider (Play-এর), Play Integrity, Google Maps, Gmail ইত্যাদি। এগুলো **GMS** — Google-এর closed অংশ। GMS পেতে Google-এর license আর certification (CTS/GTS পাস) লাগে।
- **Pixel/Samsung Android** = AOSP + vendor code (driver, HAL, BSP) + OEM-এর UI + GMS।
- আপনার camera device-এ GMS সাধারণত থাকে না। তাই FCM, Play Integrity, Fused location — এগুলোর বদলে অন্য উপায় নিজেকে বানাতে হয় (O14 দেখুন)।
- **কী বদলেছে:**
  - 2025 থেকে Google Android-এর development internal branch-এ করে। আগে `aosp-main` public ছিল, এখন সেটা চলমান কাজ দেখায় না।
  - 2026 থেকে AOSP source **বছরে দুইবার** publish হয় (Q2 আর Q4)। আগে quarterly ছিল।
  - Google বলে build করুন `android-latest-release` branch থেকে, `aosp-main` থেকে না।
  - Monthly security patch আলাদা security branch-এ আসতে থাকে।
  - সঠিক branch নাম আর schedule source.android.com-এ check করুন।
- **আপনার জন্য মানে:** নতুন feature source দেরিতে আসে। তাই নিজের change কম আর আলাদা রাখুন (overlay, vendor/product partition, নিজের repo)। তাহলে প্রতি release-এ rebase সহজ।
- আসল device-এর জন্য chip vendor (Qualcomm, MediaTek, Rockchip...) একটা **BSP** দেয়। এটা তাদের kernel আর HAL সহ AOSP tree। আপনি সাধারণত BSP-র উপর কাজ করেন, খালি AOSP-এর উপর না।

**Answer (English):**
> "AOSP is the open source part of Android. It has the kernel, the framework, ART, the system apps and the build system. It does not have Google Mobile Services — no Play Store, no FCM, no Play Integrity. A Pixel or Samsung phone is AOSP plus vendor drivers plus GMS, and GMS needs a license and certification. For a custom camera device, we usually ship without GMS, so we must replace push, location and integrity checks ourselves. One recent change: since 2026 Google publishes AOSP source only twice a year, and says to build from `android-latest-release`. So I would keep our own changes small and separate, to make each rebase easy."

**Key words:** `AOSP` · `GMS` · `BSP` · `android-latest-release` · `twice a year`

**Follow-up:**
- **Q:** Where does a real device's AOSP tree come from?
  **A:** "Usually from the chip vendor's BSP. It is AOSP plus their kernel, drivers and HALs. We build our product on top of that."
- **Q:** Can you put Google Play on your custom device?
  **A:** "Only with a GMS license from Google, and the device must pass CTS and Google's other tests. For a dedicated device we usually don't need it."
- **Q:** What does the twice-a-year source release mean for your team?
  **A:** "Rebases are bigger and less often. Security patches still come monthly. So we keep a clean list of our patches and merge security fixes every month."

**ভুল করবেন না:** "AOSP = Android যেটা phone-এ চলে" বলবেন না। GMS বাদ, vendor code বাদ।

**আরও দেখুন:** [O14 · No GMS](#o14) · [O3 · Build AOSP](#o3) · [O15 · Developer verification](#o15)

---

### <a id="o2"></a>O2. ★ Can you explain the Android platform layers, and how a call goes from an app to the hardware?

**প্রশ্নটা মানে:** App থেকে hardware পর্যন্ত পুরো রাস্তাটা আপনি জানেন কি না, আর Binder-এর কাজ বোঝেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "What happens when an app opens the camera, down to the driver?" · "What is Binder and why does Android use it?"

**বুঝে নিন:**
- **এক কথায়:** App কখনো hardware ছোঁয় না। App → system service → HAL → driver। প্রতিটা ধাপ Binder দিয়ে জোড়া।
- **Apps:** normal app, system app — সব আলাদা Linux user (UID) আর আলাদা process-এ।
- **Framework:** Java/Kotlin API (`android.*`)। এর পেছনে **system services**। বেশিরভাগ চলে এক process-এ: **`system_server`** (ActivityManagerService, PackageManagerService, WindowManagerService, LocationManagerService, SensorService ...)।
- **Native অংশ:** কিছু service আলাদা native daemon — `cameraserver`, `surfaceflinger`, `audioserver`, `mediaserver`। আর **ART** (app-এর DEX code চালায়), Bionic libc, native libs।
- **HAL:** vendor-এর code, একটা fixed interface-এর পেছনে। নতুন HAL = **AIDL HAL**, আলাদা process-এ (যেমন `android.hardware.camera.provider`)।
- **Kernel:** driver (V4L2 camera, IIO sensor, input, USB), Binder driver, SELinux।
- **Binder:** Android-এর IPC। Kernel driver (`/dev/binder`)। কেন:
  - Caller-এর UID/PID kernel দেয় — তাই service permission check করতে পারে (`Binder.getCallingUid()`)।
  - Object reference পাঠানো যায়, death notification (`linkToDeath`) আছে।
  - একটা copy-তে data যায়।
- **উদাহরণ — camera খোলা:**

```
App: CameraManager.openCamera()
  → Binder → cameraserver (native, permission check: CAMERA)
  → Binder (AIDL) → Camera provider HAL (vendor process)
  → ioctl → V4L2 / vendor kernel driver → sensor chip
Frames ফেরত আসে shared buffer (gralloc / AHardwareBuffer)-এ, copy ছাড়া।
```

- Sensor হলে: `SensorManager` → `SensorService` (system_server-এর ভেতর) → Sensors AIDL HAL → kernel (IIO/i2c) → sensor hub।
- Flutter mapping: platform channel হলো Dart ↔ Kotlin একই process-এ। Binder হলো process ↔ process, kernel দিয়ে।

**Answer (English):**
> "Android has five main layers. Apps on top. Then the framework, where most system services run inside `system_server`. Then native daemons like `cameraserver` and `surfaceflinger`, plus ART. Then the HAL, which is vendor code behind a fixed AIDL interface. And the Linux kernel with the drivers. Everything talks through Binder, which is a kernel IPC driver. For example, `openCamera()` goes by Binder to `cameraserver`, which checks the permission, then calls the camera HAL, which talks to the kernel driver. Binder is important because the kernel gives the caller's UID, so each service can check permissions safely. Big data like frames goes through shared buffers, not through Binder."

**Key words:** `system_server` · `Binder` · `HAL` · `cameraserver` · `calling UID`

**Follow-up:**
- **Q:** Why not let apps open `/dev/video0` directly?
  **A:** "Then there is no permission check, no sharing between apps, and no stable interface. SELinux blocks it too. The service in the middle controls access."
- **Q:** What happens if `system_server` crashes?
  **A:** "It is a critical process, so the whole framework restarts — a soft reboot. All apps die. That is why a bug in a custom system service is very serious."
- **Q:** Is Binder used for big data like video?
  **A:** "No. Binder has a small buffer, about 1 MB per process. Video uses shared memory buffers and Binder only passes the handle."

**ভুল করবেন না:** "সব system service system_server-এ" বলবেন না — camera, audio, surfaceflinger আলাদা native process।

**আরও দেখুন:** [F3 · Binder](#f3) · [F11 · System services](#f11) · [O6 · HAL and Treble](#o6)

---

### <a id="o3"></a>O3. ★ How do you build AOSP and flash it on a device?

**প্রশ্নটা মানে:** আপনি কখনো platform build করেছেন বা কীভাবে করতে হয় জানেন কি না — command আর ধারণা দুটোই।
**অন্যভাবেও জিজ্ঞেস করে:** "Walk me through building Android from source." · "What is the difference between user, userdebug and eng builds?"

**বুঝে নিন:**
- **এক কথায়:** তিন ধাপ — source আনুন (`repo`) → build করুন (`lunch` + `m`) → device-এ বসান (`fastboot`)।
- **Host:** Linux (Ubuntu) x86_64। অনেক disk (শত শত GB) আর অনেক RAM লাগে। সঠিক সংখ্যা source.android.com-এ দেখুন।
- **Source আনা:**
  ```
  repo init -u https://android.googlesource.com/platform/manifest -b android-latest-release
  repo sync -c -j8
  ```
  `repo` অনেক git repo একসাথে চালায় (manifest XML)। Company নিজের manifest রাখে — নিজের repo যোগ, কিছু repo বদল।
- **Build:**
  ```
  source build/envsetup.sh
  lunch <product>-<release>-<variant>   # যেমন Cuttlefish product + userdebug
  m                                     # পুরো image; m <module> শুধু একটা
  ```
  `<release>` হলো release config (trunk-stable model)। নাম docs থেকে নিন।
- **Build variant:**

| Variant | কোথায় | কী আছে |
|---|---|---|
| `user` | Production, customer device | root নেই, `ro.debuggable=0`, adb default off |
| `userdebug` | Internal test, dogfood | user-এর মতো, কিন্তু `adb root` আর debug tool আছে |
| `eng` | Platform development | সব debug, কম optimization |

- **Build file:** `Android.bp` (Soong, Blueprint format)। `Android.mk` legacy। Product config (কোন package image-এ যাবে) এখনো `.mk`-এ: `PRODUCT_PACKAGES += MyApp`।
  ```
  android_app {
      name: "CameraKiosk",
      srcs: ["src/**/*.kt"],
      certificate: "platform",
      privileged: true,
      platform_apis: true,
  }
  ```
- **Flash:**
  - `adb reboot bootloader` → `fastboot flashing unlock` (dev device) → `fastboot flashall -w` (`-w` data মুছে দেয়)।
  - Dynamic partition (`super`) আছে বলে system/vendor flash হয় **fastbootd**-এ (userspace fastboot)। `flashall` নিজে এটা সামলায়।
- **Device ছাড়া:** **Cuttlefish** — Google-এর virtual device (cloud বা local Linux)। CI-তে ভালো। পুরোনো Goldfish emulator-ও আছে।
- **ছোট change দ্রুত test (userdebug):** `m MyModule` → `adb root` → `adb remount` → `adb sync` → `adb reboot`। পুরো image flash লাগে না। (`adb remount` প্রথমবার verity বন্ধ করে, একবার reboot চায়।)

**Answer (English):**
> "First I get the source with `repo init` on `android-latest-release` and `repo sync`. In a company it is usually the chip vendor's BSP manifest with our repos added. Then `source build/envsetup.sh`, `lunch` with product, release and variant, and `m`. For daily work I use `userdebug`, because it is like production but I still have `adb root`. Customers get `user` builds only. Modules are defined in `Android.bp` files. To flash, I reboot to the bootloader and run `fastboot flashall`. For small changes I build one module and use `adb remount` and `adb sync`. Without hardware, I use Cuttlefish."

**Key words:** `repo sync` · `lunch` · `m` · `userdebug` · `Android.bp` · `fastboot` · `Cuttlefish`

**Follow-up:**
- **Q:** Why never ship `userdebug` to customers?
  **A:** "It allows `adb root`. Anyone with a cable can get full root, read data and change the system. Production must be `user`."
- **Q:** How do you add your own app to the image?
  **A:** "I add an `android_app` or `android_app_import` module in `Android.bp`, then add its name to `PRODUCT_PACKAGES` in the product makefile."
- **Q:** How do you keep build times OK?
  **A:** "Build only the module I changed, keep a warm `out/` folder, and use a strong build machine or remote cache. Full builds go to CI."

**ভুল করবেন না:** `aosp-main` থেকে product build বলবেন না — 2026-এ guidance হলো `android-latest-release` (বা আপনার BSP-র branch)।

**আরও দেখুন:** [O4 · System app types](#o4) · [O11 · Verified boot](#o11) · [O16 · ADB](#o16)

---

### <a id="o4"></a>O4. ★ What is the difference between a normal app, a system app, a privileged app and a platform-signed app?

**প্রশ্নটা মানে:** কোন app কতটা ক্ষমতা পায়, কেন, আর ঝুঁকি কোথায় — আপনি জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you give your app a permission like REBOOT or INSTALL_PACKAGES?" · "What is the risk of `android.uid.system`?"

**বুঝে নিন:**

| ধরন | কোথায় থাকে | কী পায় |
|---|---|---|
| Normal app | `/data/app` | normal + dangerous (runtime) permission |
| System app | `/system/app` (বা `/product/app`, `/vendor/app`) | uninstall করা যায় না, কিছু flag; বিশেষ permission না |
| Privileged app | `/system/priv-app` (বা `/product/priv-app`) | `privileged` flag-এর permission — কিন্তু **allowlist**-এ থাকতে হবে |
| Platform-signed | যেকোনো জায়গা, platform key দিয়ে sign | `signature` protection-এর permission |
| `android.uid.system` | platform-signed + sharedUserId | system_server-এর মতো একই UID — প্রায় সব কিছু |

- **Permission protection level:** `normal`, `dangerous`, `signature` (platform key-এ sign হলে), `signature|privileged` (platform key **অথবা** priv-app + allowlist)। যেমন `REBOOT`, `INSTALL_PACKAGES`, `WRITE_SECURE_SETTINGS` এগুলো signature বা privileged ধরনের।
- **privapp-permissions allowlist (Android 8+):** priv-app যে privileged permission চায় সেটা XML-এ লিখতে হয়:
  ```xml
  <permissions>
    <privapp-permissions package="com.acme.camera">
      <permission name="android.permission.REBOOT"/>
      <permission name="android.permission.INSTALL_PACKAGES"/>
    </privapp-permissions>
  </permissions>
  ```
  ফাইল যায় `/system/etc/permissions/` বা `/product/etc/permissions/`-এ। Enforce mode-এ কোনো privileged permission allowlist-এ না থাকলে device boot-ই হয় না। তাই ভুলটা প্রথম test-এই ধরা পড়ে, চুপচাপ থাকে না।
- **Platform signature:** AOSP build-এর `platform` key। `Android.bp`-তে `certificate: "platform"`। এই key-ই production-এ নিজের key হতে হবে (O11)।
- **`android:sharedUserId="android.uid.system"`:** App system UID (1000)-এ চলে। ঝুঁকি:
  - App-এর যেকোনো bug (যেমন exported component, WebView, deserialization) = system-level compromise।
  - Data আর permission system-এর সাথে share।
  - `sharedUserId` deprecated (API 29)। একবার দিলে পরে সরানো কঠিন। সরানোর জন্য Android 13-এ `sharedUserMaxSdkVersion` এসেছে।
- **আমার নিয়ম:** সবচেয়ে কম ক্ষমতা নিন। প্রথমে দেখুন Device Owner API দিয়ে হয় কি না। না হলে priv-app + শুধু দরকারি permission। `android.uid.system` একদম শেষ উপায়।

**Answer (English):**
> "A normal app gets normal and runtime permissions only. A system app is preinstalled and cannot be removed, but it does not get special power just from that. A privileged app lives in `priv-app` and can get `privileged` permissions, but only those listed in a `privapp-permissions` XML allowlist. A platform-signed app is signed with the same key as the OS, so it gets `signature` permissions. The strongest is `sharedUserId` `android.uid.system` — it runs as the system user. I avoid that, because any bug in the app becomes a system bug. My rule is least privilege: Device Owner APIs first, then a privileged app with a short allowlist."

**Key words:** `priv-app` · `privapp-permissions` · `signature|privileged` · `platform key` · `android.uid.system` · `least privilege`

**Follow-up:**
- **Q:** Can you update a privileged app with a normal APK install?
  **A:** "Yes, if the new APK has the same package name and the same signing key. The update goes to `/data`, but it keeps privileged status because the system copy exists."
- **Q:** How does an app get `WRITE_SECURE_SETTINGS`?
  **A:** "It is signature or privileged level. So platform signing or priv-app with the allowlist. For testing, you can grant it with `adb shell pm grant`."
- **Q:** Why is the allowlist a good idea?
  **A:** "It makes every privileged permission a visible, reviewed line in the build. Nobody can add power silently."

**ভুল করবেন না:** "System app মানেই সব permission" — না। Privileged হতে হবে আর allowlist লাগবে।

**আরও দেখুন:** [O9 · Kiosk](#o9) · [S12 · Secure IPC](#s12) · [O11 · Signing keys](#o11)

---

### <a id="o5"></a>O5. ◆ How would you add a new system service or customise the framework?

**প্রশ্নটা মানে:** Platform-এ নতুন API যোগ করার পুরো ধাপ জানেন কি না, আর কখন এটা করা উচিত না।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you expose a new hardware feature to apps?" · "How would you add a custom API to the SDK for your device?"

**বুঝে নিন:**
- **এক কথায়:** নতুন system service = AIDL interface + service class + register + SELinux rule + app-এর জন্য manager class। কিন্তু আগে সহজ উপায় খুঁজুন।
- **ধাপগুলো (framework service):**
  1. **AIDL interface:** `IAcmeLedService.aidl` (`frameworks/base/core/java/...` বা নিজের vendor/product module-এ)।
  2. **Service class:** `class AcmeLedService : IAcmeLedService.Stub()` — প্রতিটা method-এ permission check: `context.enforceCallingOrSelfPermission(...)`।
  3. **Register:** `SystemServer`-এ start করুন (`SystemService` subclass, `publishBinderService("acme_led", binder)`) — এটা ভিতরে `ServiceManager.addService` করে।
  4. **SELinux:** `service_contexts`-এ `acme_led u:object_r:acme_led_service:s0`। `.te`-তে type define আর কোন domain `find` করতে পারবে তার rule। না দিলে `add_service` fail করে।
  5. **App-এর জন্য manager:** `AcmeLedManager` class, `SystemServiceRegistry`-তে register, `context.getSystemService(...)` দিয়ে পাওয়া যায়।
  6. **API surface:** public/system API বদলালে API file update করতে হয় (build check করে)। অথবা hidden রেখে নিজের SDK library (`java_sdk_library`) দিয়ে app-কে দিন।
- **সহজ উপায় (আমি আগে এগুলো দেখি):**
  - **Privileged app-এর ভেতর bound service** + নিজের AIDL। Framework-এ হাত লাগে না। প্রতি release-এ rebase সহজ।
  - **Native vendor service / AIDL HAL** (vendor partition-এ) — hardware-এর কাছে।
  - **Runtime Resource Overlay (RRO)** — শুধু config বা UI resource বদলাতে (`config.xml` value), code ছাড়া।
- **কেন সাবধান:** `frameworks/base` বদলানো মানে প্রতি AOSP release (এখন বছরে দুইবার বড় drop) আর monthly security patch-এ merge conflict। আর system_server-এ crash = পুরো OS restart।
- **Design point:** Binder call blocking — caller অপেক্ষা করে। তাই service-এ লম্বা কাজ করবেন না। App-কে ফল দিন `oneway` callback interface দিয়ে। Client মারা গেলে `linkToDeath` দিয়ে cleanup করুন।

**Answer (English):**
> "For a framework service, I define an AIDL interface, write the service as a `Stub` that checks the caller's permission, and publish it from `SystemServer` with `publishBinderService`. Then I add SELinux rules: a `service_contexts` entry and allow rules for who can find it. For apps, I add a manager class and register it, so apps call `getSystemService`. But before I touch `frameworks/base`, I check simpler options. A bound service inside a privileged app, or a vendor AIDL service, is often enough. Framework changes cost a lot at every rebase, and a crash in `system_server` restarts the whole OS."

**Key words:** `AIDL` · `publishBinderService` · `ServiceManager` · `service_contexts` · `manager class` · `RRO`

**Follow-up:**
- **Q:** How do you keep the service safe from any app calling it?
  **A:** "Check a custom `signature` permission in every method, using the calling UID from Binder. And SELinux limits which domains can even find the service."
- **Q:** How do apps call it if it's not in the public SDK?
  **A:** "We ship a small client library or SDK stub to our app team. Our apps are platform-signed or privileged, so they can use system APIs."

**আরও দেখুন:** [O13 · Custom hardware](#o13) · [O7 · SELinux](#o7) · [F11 · System services](#f11)

---

### <a id="o6"></a>O6. ◆ What is a HAL, and what did Project Treble change? AIDL HAL vs HIDL?

**প্রশ্নটা মানে:** Vendor/system ভাগ আর আধুনিক HAL লেখা — 2026-এর সঠিক উপায় জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you add a HAL for a new sensor?" · "What is VINTF and what is a GSI?"

**বুঝে নিন:**
- **এক কথায়:** HAL = vendor-এর code, একটা fixed interface-এর পেছনে। Treble = Google-এর অংশ আর vendor-এর অংশ আলাদা, যাতে দুইটা আলাদা update করা যায়।
- **HAL** = framework আর driver-এর মাঝে vendor-এর code। Framework শুধু interface জানে, chip-এর detail জানে না।
- **Treble-এর আগে (Android 8-এর আগে):** HAL ছিল `.so` library, framework সরাসরি load করত। Android update মানে vendor-কেও সব rebuild করতে হতো।
- **Treble (Android 8+):**
  - `system` (AOSP/framework) আর `vendor` (BSP, HAL) আলাদা partition।
  - মাঝে versioned interface। HAL আলাদা process-এ চলে, framework Binder দিয়ে call করে।
  - **VINTF:** vendor-এর manifest বলে "আমি এই HAL-গুলো দিই"; framework-এর compatibility matrix বলে "আমার এগুলো লাগবে"। Build আর OTA-তে মিল check হয়।
  - **GSI** (Generic System Image): শুধু AOSP system image। যেকোনো Treble device-এ বসিয়ে দেখা যায় vendor ঠিক interface মানে কি না। VTS এটা দিয়ে test করে।
- **HIDL vs AIDL:**
  - HIDL ছিল Treble-এর প্রথম HAL ভাষা। **Android 13 থেকে deprecated।** নতুন HAL HIDL-এ লিখবেন না।
  - নতুন HAL = **stable AIDL** (`@VintfStability`)। Interface version freeze হয়, পরে শুধু নতুন method যোগ।
  ```
  aidl_interface {
      name: "vendor.acme.thermalcam",
      vendor_available: true,
      srcs: ["vendor/acme/thermalcam/*.aidl"],
      stability: "vintf",
      backend: { java: { enabled: false } },
  }
  ```
  Service register হয় নামে, যেমন `vendor.acme.thermalcam.IThermalCam/default`। VINTF manifest fragment আর SELinux (`hal_*` domain) লাগে।
- **নতুন sensor-এর জন্য:** আগে দেখুন standard HAL (Sensors AIDL HAL) দিয়ে হয় কি না — তাহলে `SensorManager` দিয়েই app পায়, নতুন API লাগে না। একদম নতুন ধরনের hardware হলে নিজের vendor AIDL HAL + system service বা priv-app (O13)।

**Answer (English):**
> "A HAL is the vendor code between the framework and the kernel driver. Project Treble split the system and vendor partitions and put a versioned interface between them. VINTF checks that the vendor provides the HALs the framework needs. A GSI is a plain AOSP system image to test that the vendor side follows the rules. HIDL was the first HAL language, but it is deprecated since Android 13. New HALs use stable AIDL with `vintf` stability. For a new sensor, I first try the standard Sensors HAL, so apps use `SensorManager` with no new API. Only for truly new hardware I write a vendor AIDL HAL."

**Key words:** `Treble` · `stable AIDL` · `VINTF` · `GSI` · `vendor partition` · `HIDL deprecated`

**Follow-up:**
- **Q:** Why is the split useful for your own device?
  **A:** "We can update the system part, like a new Android release or security fix, without touching the vendor HALs, as long as the interfaces match."
- **Q:** What happens when you need to change a frozen AIDL HAL?
  **A:** "I add a new version with the new methods. Old clients keep working. I never change a frozen version."

**ভুল করবেন না:** নতুন HAL-এর জন্য HIDL বলবেন না — এটা পুরোনো আর deprecated।

**আরও দেখুন:** [O13 · Custom hardware](#o13) · [O5 · New system service](#o5) · [O2 · Platform layers](#o2)

---

### <a id="o7"></a>O7. ★ How does SELinux work on Android, and how do you fix an "avc: denied" error?

**প্রশ্নটা মানে:** Platform-এ সবচেয়ে common block — আপনি কি ঠিক উপায়ে fix করবেন, না security বন্ধ করবেন?
**অন্যভাবেও জিজ্ঞেস করে:** "Your new daemon can't open a device file. What do you do?" · "Why not just set SELinux to permissive?"

**বুঝে নিন:**
- **এক কথায়:** SELinux ঠিক করে কোন process কোন file বা service ছুঁতে পারবে। নিয়ম না থাকলে block — root হলেও। Fix মানে একটা ছোট, ঠিক নিয়ম লেখা। SELinux বন্ধ করা fix না।
- Android-এ SELinux **enforcing** (Android 5 থেকে সব domain)। এটা **MAC** — Linux file permission (UID) ছাড়াও আলাদা নিয়ম। Root process-ও SELinux-এর বাইরে না।
- প্রতিটা process-এর **domain** (যেমন `system_server`, `untrusted_app`, `hal_camera_default`), প্রতিটা file/service-এর **type**। নিয়ম ছাড়া কোনো access চলে না।
- **Denial দেখতে:**
  ```
  adb logcat | grep avc        # বা: adb shell dmesg | grep avc
  avc: denied { read write } for comm="acmed" name="ttyS1"
       scontext=u:r:acmed:s0 tcontext=u:object_r:serial_device:s0 tclass=chr_file
  ```
  পড়ুন: **কে** (scontext) **কী** (read write) **কার উপর** (tcontext, tclass)।
- **ঠিক fix:**
  1. ঠিক type দিন: device file-এর জন্য `file_contexts`-এ নিজের type (`/dev/ttyS1 u:object_r:acme_serial_device:s0`), generic type না।
  2. নিজের domain-এর জন্য `.te` file:
     ```
     type acmed, domain;
     type acmed_exec, exec_type, vendor_file_type, file_type;
     init_daemon_domain(acmed)
     allow acmed acme_serial_device:chr_file rw_file_perms;
     ```
  3. Policy আপনার device tree-তে রাখুন (`BOARD_VENDOR_SEPOLICY_DIRS` বা product dir)। AOSP-এর policy edit করবেন না।
- **`audit2allow`** rule suggest করে। কিন্তু চোখ বন্ধ করে নেবেন না — প্রায়ই দরকারের চেয়ে বেশি access দেয়। **neverallow** rule ভাঙলে build fail করে, আর CTS-ও check করে।
- **কেন `setenforce 0` fix না:**
  - পুরো device-এর protection বন্ধ — সব process-এর জন্য।
  - `user` build-এ এটা চলেই না।
  - Debug-এর সময় অল্প সময়ের জন্য permissive করলে সব denial একসাথে দেখা যায়। কিন্তু শুধু userdebug-এ, শুধু খোঁজার জন্য। একটা domain permissive করাও (`permissive acmed;`) release-এ রাখা যাবে না।

**Answer (English):**
> "On Android, SELinux is always enforcing. Every process has a domain and every file or service has a type, and nothing is allowed without a rule — even for root. When I see an `avc: denied` in logcat or dmesg, I read who, what action, and on which target. Then I fix it properly: give the file its own type in `file_contexts`, and add a narrow `allow` rule in my own `.te` file in the device policy. I use `audit2allow` only as a hint, because it often gives too much. `setenforce 0` is not a fix. It turns off protection for the whole device, and it does not work on user builds anyway."

**Key words:** `enforcing` · `avc: denied` · `scontext` / `tcontext` · `.te file` · `file_contexts` · `neverallow`

**Follow-up:**
- **Q:** What is a `neverallow` rule?
  **A:** "A rule that says some access must never be allowed, like apps writing to system files. If my policy breaks it, the build fails. CTS checks it too."
- **Q:** Can a normal app hit SELinux denials?
  **A:** "Yes. Apps run in `untrusted_app`. For example, reading some `/proc` or `/sys` files is denied. The fix is to use the proper API, not change policy for apps."

**ভুল করবেন না:** "Permissive করে দিলাম, এখন কাজ করে" — interviewer এটা শুনলে বড় red flag।

**আরও দেখুন:** [O5 · New system service](#o5) · [O8 · Boot and init](#o8) · [F13 · Security model](#f13)

---

### <a id="o8"></a>O8. ◆ Can you explain the Android boot process? Where would you add custom startup?

**প্রশ্নটা মানে:** Power on থেকে launcher পর্যন্ত ধাপ, আর নিজের code কোন ধাপে চালাবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you start a native daemon at boot?" · "What is Zygote?"

**বুঝে নিন:**

**এক কথায়:** Power on → bootloader → kernel → `init` → native daemons → Zygote → `system_server` → launcher। নিজের code সবচেয়ে নিচের যে ধাপে মেলে, সেখানে চালান।

```
Boot ROM → Bootloader (AVB verify) → Kernel
  → init (first stage: partitions mount; second stage: SELinux load, .rc parse)
  → native daemons (servicemanager, hwservicemanager, HALs, surfaceflinger, cameraserver...)
  → Zygote (ART শুরু, common class preload)
  → system_server (Zygote fork করে; সব framework service start)
  → Launcher (HOME intent) + BOOT_COMPLETED broadcast
```

- **init আর `.rc`:** `init` প্রথম user-space process (PID 1)। `.rc` file-এ `service`, `on <trigger>` থাকে। নিজের daemon:
  ```
  # /vendor/etc/init/acmed.rc
  service acmed /vendor/bin/acmed
      class main
      user system
      group system
  on property:sys.boot_completed=1
      start acmed
  ```
  সাথে SELinux domain লাগবে (O7)।
- **Zygote:** একবার ART চালু করে class preload করে রাখে। নতুন app process = Zygote-এর **fork**। তাই app দ্রুত খোলে আর memory share হয়।
- **Custom startup — কোথায়:**

| কী চালাবেন | কোথায় |
|---|---|
| Native daemon, hardware init | `init` `.rc` (vendor partition) |
| Framework service | `SystemServer` (O5) |
| Java app যেটা সবসময় চালু | System app + `android:persistent="true"` |
| সাধারণ app কাজ boot-এর পর | `BOOT_COMPLETED` receiver → WorkManager / allowed FGS |
| Unlock-এর আগে | `LOCKED_BOOT_COMPLETED` + `directBootAware` |

- মনে রাখুন: Android 15-এ `BOOT_COMPLETED` থেকে camera, microphone বা dataSync type-এর foreground service start করা যায় না। তাই camera device-এ boot-এর পর recording শুরু করতে হলে system/privileged উপায় বা persistent app লাগবে।
- Boot time মাপুন: `adb shell dmesg`, `logcat -b events | grep boot_progress`, Perfetto boot trace।

**Answer (English):**
> "The bootloader verifies and loads the kernel. The kernel starts `init`, which mounts partitions, loads SELinux and runs the `.rc` scripts. `init` starts native daemons like `servicemanager`, the HALs and `surfaceflinger`, and then Zygote. Zygote starts ART and preloads classes, so every app is a fast fork. Zygote also forks `system_server`, which starts all framework services, and then the launcher shows. For custom startup I pick the lowest layer that fits: a native daemon goes in a vendor `.rc` file with its own SELinux domain, a framework service goes in `SystemServer`, and an always-on app can be a persistent system app. Normal apps use `BOOT_COMPLETED`."

**Key words:** `init.rc` · `Zygote` · `system_server` · `persistent` · `BOOT_COMPLETED` · `directBootAware`

**Follow-up:**
- **Q:** Why does Zygote make app start faster?
  **A:** "The runtime and common classes are already loaded. A fork shares that memory, so each app does not load them again."
- **Q:** How would you start camera recording right after boot on your device?
  **A:** "On our own OS I would use a persistent privileged app or a system service. A normal app can't start a camera foreground service from `BOOT_COMPLETED` on Android 15+."

**আরও দেখুন:** [F1 · App start](#f1) · [C18 · Process start](#c18) · [O9 · Kiosk](#o9)

---

### <a id="o9"></a>O9. ★ How do you build a kiosk or dedicated device? Can you do it without a custom ROM?

**প্রশ্নটা মানে:** Camera/sensor device একটা কাজই করবে — user বের হতে পারবে না। আপনি সঠিক API জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you lock a device to one app?" · "What is Device Owner and how do you set it up?"

**বুঝে নিন:**
- **Custom ROM ছাড়া (সাধারণ device):** **Device Owner** (Android Enterprise, `DevicePolicyManager`)।
  - Provision: factory-fresh device-এ QR code / NFC / zero-touch, অথবা test-এ:
    `adb shell dpm set-device-owner com.acme.kiosk/.AdminReceiver` (device-এ কোনো account থাকা চলবে না)।
  - Device Owner পারে:
  ```kotlin
  val dpm = getSystemService(DevicePolicyManager::class.java)
  val admin = ComponentName(this, AdminReceiver::class.java)
  dpm.setLockTaskPackages(admin, arrayOf(packageName))
  dpm.setLockTaskFeatures(admin, DevicePolicyManager.LOCK_TASK_FEATURE_NONE)
  dpm.setStatusBarDisabled(admin, true)
  dpm.setKeyguardDisabled(admin, true)
  dpm.addPersistentPreferredActivity(admin,
      IntentFilter(Intent.ACTION_MAIN).apply { addCategory(Intent.CATEGORY_HOME); addCategory(Intent.CATEGORY_DEFAULT) },
      ComponentName(this, KioskActivity::class.java))
  // Activity-তে: startLockTask()
  ```
  - আরও: `addUserRestriction` (factory reset, USB file transfer, safe boot বন্ধ), silent app install/update (`PackageInstaller`), system update policy।
- **Lock task mode:** `startLockTask()`। Allowlist-এ থাকলে user prompt ছাড়াই pin হয়। Home, Recents, notification বন্ধ। না থাকলে এটা শুধু "screen pinning" — user বের হতে পারে।
- **Custom launcher:** আপনার activity-তে `MAIN` + `HOME` + `DEFAULT` category। Device Owner `addPersistentPreferredActivity` দিয়ে default বানায়।
- **Auto start:** Launcher নিজেই boot-এর পর আসে। Crash হলে HOME আবার আপনার app খোলে।
- **নিজের ROM থাকলে আরও শক্ত করা যায়:**
  - Image-এ শুধু নিজের launcher রাখুন, Launcher3/Settings বাদ দিন বা disable।
  - SystemUI বদলান (status bar, navigation বাদ), বা overlay দিয়ে config বদলান।
  - QR/zero-touch ছাড়াই build-এর সময় device owner ঠিক করা যায়। অথবা নিজের privileged app দিয়ে একই কাজ করা যায়।
  - adb `user` build-এ বন্ধ, debug menu বন্ধ।
- **ঝুঁকি:** Kiosk-এ update আর বের হওয়ার রাস্তা রাখুন (remote command, PIN দিয়ে লুকানো admin exit)। নইলে একটা bug-এ পুরো fleet আটকে যায়।

**Answer (English):**
> "Without a custom ROM, I use Device Owner from Android Enterprise. I provision it with QR or zero-touch, or with `dpm set-device-owner` for testing. Then I allowlist my app with `setLockTaskPackages` and call `startLockTask`, so the user can't leave. I set my activity as the persistent HOME app, disable the status bar and keyguard, and add user restrictions like no factory reset. Device Owner can also install updates silently. With our own ROM I can go further: ship only our launcher, change SystemUI, and turn off adb in user builds. One thing I always keep is a safe way out — a remote admin command — so a bug can't lock the whole fleet."

**Key words:** `Device Owner` · `DevicePolicyManager` · `lock task mode` · `setLockTaskPackages` · `HOME intent` · `user restrictions`

**Follow-up:**
- **Q:** What is the difference between screen pinning and lock task with Device Owner?
  **A:** "Screen pinning asks the user and they can unpin. Lock task with an allowlisted app starts without a prompt and the user can't exit."
- **Q:** How do you update the kiosk app on many devices?
  **A:** "As Device Owner, the app can install updates silently with `PackageInstaller`. Or an MDM / EMM does it. On our own OS it can be part of OTA too."
- **Q:** Can you make an app Device Owner after the user set up the phone?
  **A:** "Not normally. It must be set on a fresh device with no accounts. That is why fleets use QR or zero-touch at setup."

**ভুল করবেন না:** শুধু `HOME` launcher বা Back button আটকানোকে kiosk বলবেন না — notification shade, Recents, Settings দিয়ে বের হওয়া যায়।

**আরও দেখুন:** [S13 · Android Enterprise](#s13) · [D4 · Device fleet design](#d4) · [O10 · OTA](#o10)

---

### <a id="o10"></a>O10. ★ How do you deliver OTA updates to your own devices?

**প্রশ্নটা মানে:** Fleet-এ OS update নিরাপদে পাঠানো — A/B, signing, rollback, staged rollout।
**অন্যভাবেও জিজ্ঞেস করে:** "What is A/B update and why is it safer?" · "How do you avoid bricking 10,000 devices with one bad update?"

**বুঝে নিন:**
- **এক কথায়:** Device-এ দুইটা slot। নতুন OS অন্য slot-এ লেখা হয়। নতুনটা boot না হলে device পুরোনোটায় ফিরে যায়।
- **A/B (seamless):** দুই slot (`_a`, `_b`)। Device চলতে চলতে inactive slot-এ update লেখা হয়। Reboot-এ নতুন slot। Boot fail করলে bootloader আগের slot-এ ফিরে যায়। Downtime শুধু একটা reboot।
- **Virtual A/B (Android 11+):** দুইটা পুরো copy-র জায়গা লাগে না। Snapshot (dm-snapshot, পরে compression সহ — VABC) দিয়ে করে। নতুন device-এর জন্য এটাই default।
- **`update_engine`:** Device-এর daemon যেটা payload slot-এ লেখে। App বা নিজের updater service এটা চালায় `UpdateEngine` API দিয়ে (system API — privileged app লাগে)। AOSP-এ sample: `SystemUpdaterSample`।
- **Package বানানো:**
  ```
  m dist                          # target-files.zip
  sign_target_files_apks ...      # নিজের release key দিয়ে sign
  ota_from_target_files ...       # full OTA
  ota_from_target_files -i old.zip ...  # incremental (ছোট)
  ```
  Device শুধু আপনার OTA key-তে sign করা package নেয়।
- **Rollback protection:** AVB-র **rollback index**। নতুন build-এ index বাড়ালে পুরোনো (vulnerable) build আর boot হবে না। তাই security fix-এর পর downgrade attack বন্ধ।
- **Boot success mark:** নতুন slot-এ boot হওয়ার পর `update_verifier` / boot control HAL slot-কে "successful" mark করে। না হলে কয়েকবার চেষ্টার পর পুরোনো slot।
- **Fleet rollout (আপনার server):**
  - Device ID / group অনুযায়ী ধাপে ধাপে: internal → 1% → 10% → 100%।
  - Health signal দেখুন: boot success, crash rate, app heartbeat। খারাপ হলে rollout থামান।
  - Update শুধু শর্ত মেনে: charging/battery, Wi‑Fi, idle সময় (camera recording চলার সময় reboot না)।
  - HTTPS + signed metadata; payload resume করা যায়।
- Vendor/3rd-party OTA solution-ও আছে, কিন্তু নীতি একই।

**Answer (English):**
> "I use A/B updates, or Virtual A/B on newer devices. The update goes to the inactive slot while the device keeps working. After a reboot it switches. If the new slot fails to boot, the bootloader goes back to the old one. `update_engine` applies the update, and our privileged updater app controls it. We sign the OTA with our own keys, so the device only accepts our packages. We raise the AVB rollback index for security fixes, to block downgrades. On the server I do a staged rollout — internal devices, then 1%, then more — and watch boot success and crashes. For cameras, I reboot only at a safe time, not during recording."

**Key words:** `A/B` · `Virtual A/B` · `update_engine` · `ota_from_target_files` · `rollback index` · `staged rollout`

**Follow-up:**
- **Q:** What is the difference between full and incremental OTA?
  **A:** "Full has the whole image and works from any version. Incremental only has the diff from one exact build, so it is small but needs that base build."
- **Q:** What if the update installs fine but our camera app is broken?
  **A:** "Boot success is not enough. Our app sends a health check after update. If it fails, we stop the rollout and push a fix. We can't roll back past the rollback index, so we test well first."

**ভুল করবেন না:** "Device যেকোনো package নেবে" — না। Signing key আর rollback index ছাড়া OTA খুব ঝুঁকির।

**আরও দেখুন:** [O11 · Verified boot](#o11) · [D4 · Device fleet design](#d4) · [P6 · App signing](#p6)

---

### <a id="o11"></a>O11. ◆ What is verified boot (AVB) and why must test-keys never ship?

**প্রশ্নটা মানে:** Boot chain-এর security আর key management বোঝেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How does Android know the system partition was not changed?" · "What is dm-verity?"

**বুঝে নিন:**
- **এক কথায়:** Boot-এর প্রতিটা ধাপ পরের ধাপের signature check করে। আপনার key ছাড়া বদলানো OS চলবে না।
- **Chain of trust:** Boot ROM → bootloader (OEM key fused/রাখা) → **vbmeta** (AVB metadata, signed) → boot, system, vendor partition-এর hash।
- **AVB (Android Verified Boot 2.0):**
  - ছোট partition (boot): পুরো hash check।
  - বড় partition (system, vendor): **dm-verity** — hash tree। Block পড়ার সময় kernel check করে। কেউ বদলালে read fail বা device reboot।
  - Rollback index: পুরোনো image বন্ধ (O10)।
- **Boot state:** `green` (locked, OEM key), `yellow` (locked, user key), `orange` (unlocked)। `ro.boot.verifiedbootstate`। Key attestation-এ এটা server দেখতে পারে।
- **Locked bootloader:** Production device locked থাকবে। Unlock করলে data মুছে যায় আর state orange।
- **Keys:** নিজের key বানান:
  - Platform/app key (`platform`, `shared`, `media`, `networkstack`, `releasekey`)।
  - AVB key, OTA key।
  - HSM-এ বা offline রাখুন। CI-তে signing একটা আলাদা step, আর খুব কম মানুষের access থাকে।
- **কেন test-keys ship করা যাবে না:** AOSP-এর test key-র **private key public** (`build/target/product/security/`-এ)। তাহলে:
  - যে কেউ "platform-signed" app বানিয়ে আপনার device-এ install করে system power পাবে।
  - যে কেউ OTA package sign করে device-এ চালাতে পারবে।
  - Build fingerprint-এ `test-keys` দেখায় — certification fail।

**Answer (English):**
> "Verified boot builds a chain of trust. The bootloader checks the signed vbmeta image with our key, and vbmeta has the hashes of boot, system and vendor. Big partitions use dm-verity, so the kernel checks each block when it reads it. If someone changes the system partition, the device will not use it. The rollback index blocks old images. Production devices must have a locked bootloader. And we must sign with our own keys. AOSP test keys have public private keys, so anyone could sign an app as 'platform' or sign an OTA for our device. I would keep release keys in an HSM, with signing as a separate, restricted CI step."

**Key words:** `AVB` · `vbmeta` · `dm-verity` · `locked bootloader` · `test-keys` · `HSM`

**Follow-up:**
- **Q:** How can a server know the device runs your real OS?
  **A:** "With hardware key attestation. The attestation certificate includes verified boot state and the boot key hash, so the server can check it."
- **Q:** What happens if you lose your platform key?
  **A:** "You can't update system apps with the same signature anymore, and moving to a new key is painful. So keys need backups and strict control."

**আরও দেখুন:** [O10 · OTA](#o10) · [S7 · Root and tamper](#s7) · [S3 · Keystore](#s3)

---

### <a id="o12"></a>O12. ★ How do you debug problems at the platform level?

**প্রশ্নটা মানে:** App log-এর বাইরে — system, native crash, kernel, performance — কোন tool কখন ব্যবহার করবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "A device in the field froze. How do you find out why?" · "How do you debug a native crash?"

**বুঝে নিন:**

| Tool | কী দেখায় | উদাহরণ |
|---|---|---|
| `logcat` | Log buffer: `main`, `system`, `events`, `crash`, `radio`, `kernel` | `adb logcat -b all -v threadtime` |
| `dumpsys` | Service-এর বর্তমান state | `dumpsys activity`, `dumpsys sensorservice`, `dumpsys media.camera`, `dumpsys meminfo <pkg>`, `dumpsys battery` |
| `bugreport` | সব একসাথে zip: logs, dumpsys, tombstones, ANR traces | `adb bugreport out.zip` |
| Perfetto | System-wide trace: CPU, scheduling, Binder, frame | `ui.perfetto.dev` বা `perfetto` command |
| `dmesg` / kernel log | Driver, kernel, SELinux denial | `adb shell dmesg`, `logcat -b kernel` |
| Tombstone | Native crash: signal, backtrace, register | `/data/tombstones/`, bugreport-এ আছে |
| ANR trace | সব thread-এর stack | `/data/anr/` |

- **Native crash:** Tombstone-এ `signal 11 (SIGSEGV)`, backtrace আসে address দিয়ে। Symbol পেতে unstripped library লাগে (`out/.../symbols/`)। Tool: `ndk-stack` বা `stack` script। Live process: `debuggerd -b <pid>` (stack dump)।
- **System hang / ANR:** `dumpsys activity` + ANR trace। Watchdog system_server আটকে গেলে "WATCHDOG KILLING SYSTEM PROCESS" log দেয়, stack সহ।
- **Field device (কোনো cable নেই):** Device Owner app দূর থেকে bugreport চাইতে পারে (`requestBugreport`)। নিজের OS-এ: dropbox (`dumpsys dropbox`) — crash, ANR, kernel panic এখানে জমা থাকে। Upload service বানান।
- **Kernel panic:** পরের boot-এ `/sys/fs/pstore/` (ramoops)-এ শেষ kernel log থাকে।
- **Boot problem:** adb আসার আগে UART/serial console দরকার।
- `user` build-এ `adb root` নেই — তাই field debugging-এর রাস্তা আগে থেকে design করুন।

**Answer (English):**
> "I start with `adb bugreport`, because it has everything: all log buffers, dumpsys output, tombstones and ANR traces. For live problems I use `logcat -b all`, and `dumpsys` for the service involved, like `media.camera` or `sensorservice`. For native crashes I read the tombstone and symbolize the backtrace with the unstripped libraries. For kernel and driver issues I check `dmesg`, and for panics, `pstore` after reboot. For slowness or jank I record a Perfetto trace, which shows CPU, scheduling and Binder calls. For field devices on user builds there is no root, so I plan ahead: collect dropbox entries and upload bugreports."

**Key words:** `logcat -b all` · `dumpsys` · `bugreport` · `Perfetto` · `tombstone` · `dmesg` · `pstore`

**Follow-up:**
- **Q:** The camera preview freezes after some hours. Where do you look?
  **A:** "`dumpsys media.camera` for camera state and errors, logcat for the HAL process, and a Perfetto trace for stuck threads. Also memory — a leak of buffers is common."
- **Q:** How do you find who holds a wakelock?
  **A:** "`dumpsys power` shows current wake locks, and `dumpsys batterystats` or Battery Historian shows them over time."
- **Q:** How do you get a tombstone from a user build?
  **A:** "It is inside the bugreport. Also, on Android 12 and later, the app can read its own native crash tombstone from `ApplicationExitInfo`."

**আরও দেখুন:** [O16 · ADB](#o16) · [P8 · Crash monitoring](#p8) · [P10 · Production bugs](#p10)

---

### <a id="o16"></a>O16. ◆ What is ADB, and which ADB commands do you use most?

**প্রশ্নটা মানে:** Device-এর সাথে রোজ কাজ করার basic tool আপনি হাতে-কলমে জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you debug a device without Android Studio?" · "How do you test Doze or a background job from the command line?"

**বুঝে নিন:**
- **এক কথায়:** ADB = computer থেকে device চালানোর command line tool। Install, log, shell, file copy — সব এখান থেকে।
- **তিনটা অংশ:**
  - `adb` client — আপনার computer-এ command।
  - adb server — computer-এ background-এ চলে, সব device সামলায়।
  - `adbd` daemon — device-এ চলে। `user` build-এ shell user হিসেবে চলে, root না।
- **Connect:** USB debugging on করলে device computer-এর RSA key accept করতে বলে। Android 11+-এ Wireless debugging: `adb pair <ip>:<port>` (pairing code দিয়ে), তারপর `adb connect`।
- **সবচেয়ে বেশি লাগে:**

| কাজ | Command |
|---|---|
| Install / update | `adb install -r -g app.apk` (`-g` = সব runtime permission দিয়ে দেয়) |
| Log | `adb logcat -v threadtime`, `adb logcat --pid=$(adb shell pidof -s <pkg>)` |
| App খোলা / বন্ধ | `adb shell am start -W -n <pkg>/.MainActivity` (startup time দেখায়), `adb shell am force-stop <pkg>` |
| Data মুছা | `adb shell pm clear <pkg>` |
| Permission | `adb shell pm grant <pkg> <permission>` / `pm revoke` |
| State দেখা | `adb shell dumpsys activity`, `dumpsys meminfo <pkg>`, `dumpsys battery` |
| Doze test | `adb shell dumpsys deviceidle force-idle`, শেষে `dumpsys deviceidle unforce` |
| Job চালানো | `adb shell cmd jobscheduler run -f <pkg> <jobId>` (WorkManager job-ও) |
| Process death test | App background-এ পাঠান → `adb shell am kill <pkg>` → app-এ ফিরে আসুন |
| File | `adb push` / `adb pull`; নিজের debuggable app-এর data: `adb shell run-as <pkg>` |
| Port | `adb reverse tcp:8080 tcp:8080` (device → আপনার laptop-এর server), `adb forward` উল্টো দিকে |
| Screen | `adb shell screencap`, `adb shell screenrecord`, `adb shell input tap x y` |
| সব একসাথে | `adb bugreport out.zip` |

- **Platform (userdebug):** `adb root`, `adb remount`, `adb sync` (O3)। `user` build-এ এগুলো চলে না।
- **Security:** Production device-এ ADB একটা বড় দরজা। `user` build-এ default বন্ধ রাখুন। Device Owner `DISALLOW_DEBUGGING_FEATURES` দিয়ে USB debugging বন্ধ করতে পারে। Field-এ debug লাগলে আগে থেকে অন্য রাস্তা বানান (O12)।

**Answer (English):**
> "ADB is the command line tool to control a device from my computer. It has a client, a server on my computer, and the `adbd` daemon on the device. I use it every day: `adb install` with `-g` to grant permissions, `logcat` filtered by my app's PID, and `am start -W` to check startup time. For testing I use `pm clear`, `pm grant`, `am kill` to test process death, `dumpsys deviceidle force-idle` to test Doze, and `cmd jobscheduler run` to run a job now. `adb reverse` lets the device reach a server on my laptop. On production devices I keep ADB off, because it is a big way into the device."

**Key words:** `adbd` · `logcat` · `am start -W` · `pm grant` · `dumpsys deviceidle` · `adb reverse` · `wireless debugging`

**Follow-up:**
- **Q:** How do you test that your app survives process death?
  **A:** "I open a screen, press Home, then run `adb shell am kill` with my package. When I go back to the app, the state must come back from `SavedStateHandle` or storage."
- **Q:** Can you use `adb root` on a customer device?
  **A:** "No. On `user` builds `adbd` runs without root, and `adb root` does not work. Only `userdebug` and `eng` builds allow it."

**ভুল করবেন না:** `adb install -g` দিয়ে test করে ভাববেন না permission flow ঠিক আছে — এটা সব permission আগেই দিয়ে দেয়। Runtime permission dialog আলাদা করে test করুন।

**আরও দেখুন:** [O12 · Platform debugging](#o12) · [O3 · Build AOSP](#o3) · [C4 · Process death](#c4)

---

### <a id="o13"></a>O13. ◆ How would an app talk to custom hardware on your device?

**প্রশ্নটা মানে:** কোন পথ ঠিক — system service + HAL, JNI, USB, serial — আর কেন।
**অন্যভাবেও জিজ্ঞেস করে:** "Our device has a custom IR sensor board. How does the app read it?" · "Why not just open the device file from the app with JNI?"

**বুঝে নিন:**

**এক কথায়:** App সরাসরি hardware খুলবে না। মাঝে একটা service থাকবে, যেটা permission check করে।

| পথ | কখন | ভালো | খারাপ |
|---|---|---|---|
| **System service + AIDL HAL** | নিজের OS, product feature | Permission check, SELinux, বহু app share, stable API | বেশি কাজ, platform change |
| **Privileged app-এর bound service + native lib** | নিজের OS, একটাই app | Framework বদল লাগে না | SELinux-এ app domain-কে device access দিতে হয় |
| **JNI/NDK সরাসরি `/dev/*`** | Prototype | দ্রুত | `untrusted_app` SELinux block করে; নিরাপদ না |
| **USB host** (`UsbManager`) | Hardware আলাদা USB device | Normal app-এ চলে, user permission | Cable, power, permission dialog |
| **Serial (UART)** | Board-এর সাথে UART | সহজ protocol | Normal app পারে না — system/SELinux লাগে |
| **BLE / network** | Wireless sensor | Normal app | Latency, pairing, Android 17-এ LAN-এর জন্য `ACCESS_LOCAL_NETWORK` |

- **আমার পছন্দ (নিজের OS-এ):** Vendor AIDL HAL (driver-এর সাথে কথা বলে) → ছোট system service বা privileged service (permission check) → app-এর জন্য manager/SDK।
- **কেন সরাসরি না:** App-কে device node দিলে hack হওয়া যেকোনো app hardware চালাতে পারে। আর hardware code app-এর ভেতরে আটকে যায় — app বদলালে সেটাও বদলাতে হয়।
- **Standard API থাকলে সেটাই:** Camera হলে Camera HAL → CameraX/Camera2 কাজ করবে। Sensor হলে Sensors HAL → `SensorManager`। নতুন API বানাবেন না।
- **Permission:** নিজের custom permission `protectionLevel="signature|privileged"` — শুধু আপনার app পায়।

**Answer (English):**
> "On our own OS, the clean path is a vendor AIDL HAL that talks to the driver, a small system or privileged service that checks a custom signature permission, and a manager class or SDK for apps. If the hardware fits a standard type, like a camera or a sensor, I implement the standard HAL so apps just use CameraX or `SensorManager`. Opening `/dev` from an app with JNI is fine for a prototype, but SELinux blocks it for normal apps, and it is not safe. If the hardware is a separate USB device, a normal app can use USB host mode with user permission. Serial ports need system-level access."

**Key words:** `AIDL HAL` · `system service` · `signature permission` · `JNI` · `USB host` · `SELinux`

**Follow-up:**
- **Q:** Where do you put the high-rate data path, like 100 MB/s from a sensor?
  **A:** "Not through Binder calls per sample. I use shared memory or `AHardwareBuffer` / FMQ-style buffers and pass only handles over Binder."

**আরও দেখুন:** [O6 · HAL](#o6) · [N10 · USB and serial](#n10) · [B4 · NDK and JNI](#b4)

---

### <a id="o14"></a>O14. ○ What are CTS, VTS and GMS certification? What changes if your device has no Google services?

**প্রশ্নটা মানে:** Certification-এর ধারণা, আর GMS ছাড়া push, integrity, location কীভাবে করবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you send push messages without FCM?" · "How do you check device integrity without Play Integrity?"

**বুঝে নিন:**
- **CDD** (Compatibility Definition Document) — "Android compatible" হতে কী লাগে।
- **CTS** — framework/API behavior test (app developer-এর দিক থেকে)। **VTS** — vendor interface, HAL, kernel test। **GTS** — Google-এর নিজের, GMS-এর জন্য।
- **GMS certification:** Google-এর সাথে চুক্তি + CTS/VTS/GTS পাস। তাহলে Play Store, Play services, "certified device"।
- GMS না নিলেও CTS/VTS চালানো ভালো — আপনার change platform ভাঙল কি না বোঝা যায়।
- **GMS ছাড়া কী থাকে না আর বদলি:**

| GMS জিনিস | বদলি |
|---|---|
| FCM push | নিজের MQTT/WebSocket connection (persistent), বা UnifiedPush। নিজের OS-এ app-কে Doze allowlist-এ (`sysconfig` `allow-in-power-save`) রাখা যায় |
| Play Integrity | **Hardware key attestation** (Keystore `setAttestationChallenge`) — server certificate chain আর verified boot state check করে। নিজের device-এ attestation key ঠিকমতো বসানো আছে কি না check করুন |
| Fused Location (Play) | `LocationManager` (`GPS_PROVIDER`, Android 12+ `FUSED_PROVIDER`) |
| Play Store update | নিজের OTA বা Device Owner/MDM দিয়ে app update |
| Firebase SDK (যেমন Crashlytics) | কিছু অংশ Play services ছাড়া চলে, কিছু চলে না — প্রতিটা non-GMS device-এ test করুন। বা self-hosted (Sentry, ACRA) |
| Google Maps | MapLibre / OSM |

- **Developer verification (O15):** এটা শুধু **certified** device-এ চলে। আপনার non-GMS custom device-এ এটা লাগে না।

**Answer (English):**
> "CTS tests that the framework behaves as the Android rules say. VTS tests the vendor side — HALs and kernel. GMS certification is a deal with Google plus passing those tests and Google's own tests, and then you get Play Store and Play services. For a custom device without GMS, I replace things one by one. Push goes over our own MQTT or WebSocket connection, and on our OS we can allowlist the app from Doze. Instead of Play Integrity, I use hardware key attestation and check it on our server. Location comes from `LocationManager` directly. App updates go through our OTA or a device owner app. I would still run CTS, to catch platform breakage."

**Key words:** `CDD` · `CTS` · `VTS` · `GMS` · `key attestation` · `MQTT push`

**Follow-up:**
- **Q:** Do Firebase libraries work without Play services?
  **A:** "Some parts do, but FCM needs Play services. I check each SDK on a non-GMS device before I depend on it."

**আরও দেখুন:** [O15 · Developer verification](#o15) · [R16 · Push without FCM](#r16) · [S7 · Integrity checks](#s7)

---

### <a id="o15"></a>O15. ○ What is Android developer verification, and does it affect apps on your custom devices?

**প্রশ্নটা মানে:** 2026-এর sideloading নিয়ম জানেন কি না, আর enterprise/custom device-এ এর প্রভাব।
**অন্যভাবেও জিজ্ঞেস করে:** "Can users still sideload apps in 2026?" · "Do we need to register our internal apps with Google?"

**বুঝে নিন:**
- **কী:** Certified Android device-এ app install করতে হলে developer-কে verified হতে আর package name + signing key register করতে হবে। Play-এর বাইরের app-এর জন্যও। Play Console বা **Android Developer Console** দিয়ে।
- **সময় (Google-এর plan অনুযায়ী):**
  - Aug 2026: ছাত্র/hobbyist-দের জন্য limited distribution account, আর power user-দের "advanced flow"-এর preview।
  - **30 Sep 2026:** প্রথম ধাপ — Brazil, Indonesia, Singapore, Thailand। প্রথমে শুধু কিছু "participating store" থেকে install-এ (Google Play, Samsung Galaxy Store, Xiaomi GetApps, OPPO, vivo, Honor, Transsion-এর store), certified device-এ। Student/hobbyist-এর "limited distribution" — identity verify ছাড়া সর্বোচ্চ 20টা device-এ।
  - **2027:** ধাপে ধাপে সারা বিশ্বে।
  - তারিখ আর নিয়ম বদলাতে পারে — developer.android.com-এর official page check করুন।
- **ছাড়:**
  - **ADB install** verification লাগে না।
  - **Enterprise:** managed device-এ organization-এর store দিয়ে দেওয়া app-এ লাগে না (IT admin vetted)। Google তবুও register করতে বলে।
  - **Advanced flow:** power user কিছু security ধাপ পার হয়ে unverified app install করতে পারে। ধাপগুলো scam-এর চাপ ঠেকাতে বানানো।
  - Verification চলে Play services দিয়ে, শুধু certified device-এ। **আপনার নিজের non-GMS AOSP device-এ এটা লাগে না।**
- **আপনার company-র জন্য:**
  - নিজের OS-এর device: নিজের OTA/MDM দিয়ে app দিন — প্রভাব নেই।
  - Customer-এর সাধারণ phone-এ companion app (camera দেখার app): Play-তে থাকলে সাধারণত auto-register হয়। APK সরাসরি দিলে register করুন।
  - Signing key হারাবেন না — register-এর জন্য key লাগে।

**Answer (English):**
> "Google now asks developers to verify who they are and register their package names and signing keys. Then their apps can install on certified Android devices, also outside Play. The first phase started on 30 September 2026 in Brazil, Indonesia, Singapore and Thailand, and Google plans to go global in 2027. Details still change, so I check the official page. ADB installs don't need it, managed devices in a company don't need it, and power users have an advanced flow. For our own non-GMS devices it does not apply, because it runs only on certified devices. For our companion app on customer phones, I would register it to be safe."

**Key words:** `developer verification` · `certified devices` · `Android Developer Console` · `advanced flow` · `managed devices`

**Follow-up:**
- **Q:** Will our field technicians still install test builds?
  **A:** "Yes. ADB installs don't need verification. For wider testing, registered builds or Play internal testing are easier."

**ভুল করবেন না:** "Sideloading বন্ধ হয়ে গেছে" বলবেন না। Advanced flow, ADB আর enterprise-এর ছাড় আছে, আর rollout ধাপে ধাপে হচ্ছে।

**আরও দেখুন:** [O14 · No GMS](#o14) · [P6 · App signing](#p6) · [S13 · Android Enterprise](#s13)

---


## <a id="part-10"></a>Part 10 — Sensor, location, Bluetooth আর IoT

Camera আর sensor device-এর company-তে app শুধু screen না। App sensor পড়ে, location নেয়, BLE বা USB দিয়ে hardware-এর সাথে কথা বলে, আর MQTT দিয়ে cloud-এ পাঠায়।
এখানে তিনটা জিনিস সবসময় পরীক্ষা হয়: ঠিক data, কম battery, আর background-এ Android-এর নিয়ম মানা।
প্রতিটা answer-এ lifecycle, permission আর battery — এই তিনটা বলার অভ্যাস করুন।

### আগে বুঝুন — sensor, location, BLE আর IoT-এর বড় ছবি

**১. সব hardware data একই pattern-এ আসে।** আপনি register করেন → system callback দেয় → আপনি unregister করেন। Register-এর সময় rate ঠিক করেন। Unregister ভুলে গেলে battery শেষ।

**২. Sensor-এর রাস্তা:**
```
Sensor chip → Sensor hub / HAL → SensorService (system_server)
   → SensorManager → আপনার SensorEventListener (onSensorChanged)
```
অনেক device-এ sensor hub (ছোট আলাদা processor) আছে। এটা CPU ঘুমিয়ে থাকলেও data জমায় (batching)। তাই batching battery বাঁচায়।

**৩. Hardware vs composite sensor।** Accelerometer, gyroscope, magnetometer আসল chip। Rotation vector, gravity, linear acceleration, step counter — এগুলো fusion করে বানানো (HAL বা hub-এ)।

**৪. সময়।** `event.timestamp` nanosecond, boot থেকে (elapsedRealtime base)। Wall clock না। Calculation-এ এটাই ব্যবহার করুন।

**৫. Background-এর নিয়ম (মুখস্থ রাখুন):**
- Android 9: background-এ app sensor event পায় না (continuous আর on-change দুটোই)।
- Android 12: 200 Hz-এর বেশি চাইলে `HIGH_SAMPLING_RATE_SENSORS`।
- Android 11: background location আলাদা করে চাইতে হয়।
- Android 14: foreground service-এ type লাগে (`location`, `connectedDevice`, `health` ...)।
- Android 17 (target 37): LAN device খুঁজতে/connect করতে `ACCESS_LOCAL_NETWORK`।

**৬. Location।** GMS থাকলে `FusedLocationProviderClient`। GMS না থাকলে (custom device) `LocationManager` (`GPS_PROVIDER`, Android 12+ `FUSED_PROVIDER`)। Priority আর interval-ই battery ঠিক করে।

**৭. BLE।** Scan → connect → service discover → characteristic read/write/notify। GATT একসাথে একটাই operation চালায় — তাই queue লাগে। Android 12+ এ `BLUETOOTH_SCAN` আর `BLUETOOTH_CONNECT`।

**৮. IoT protocol।** MQTT = broker দিয়ে pub/sub, ছোট header, QoS। CoAP = UDP-র উপর ছোট REST। HTTP/WebSocket = সহজ, সব জায়গায় চলে।

**৯. Test।** Hardware-কে interface-এর পেছনে রাখুন। Fake আর recorded data দিয়ে unit test। আসল device-এ শেষ test।

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ `sensors_plus`, `geolocator`, `flutter_blue_plus` plugin সব আড়াল করত। Native-এ lifecycle, thread আর permission নিজে সামলাতে হয়।
- Plugin-এর stream cancel = native-এ `unregisterListener` / `stopScan` / `gatt.close()`। এগুলো ভুললে leak।
- Native-এ `callbackFlow` দিয়ে callback-কে Flow বানান — `awaitClose`-এ unregister। এটা Dart stream-এর `onCancel`-এর সমান জায়গা।
- Sensor callback অনেক দ্রুত আসে (100+ Hz)। UI-তে সরাসরি পাঠাবেন না; আগে filter বা sample করুন।

---

### <a id="n1"></a>N1. ★ How do you read sensor data on Android?

**প্রশ্নটা মানে:** SensorManager-এর basic, lifecycle, rate আর hardware/composite sensor জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you read the accelerometer in a Compose app?" · "What happens if you forget to unregister a sensor listener?"

**বুঝে নিন:**
- `SensorManager.getDefaultSensor(Sensor.TYPE_...)` — না থাকলে `null`। আগে check করুন। Manifest-এ `<uses-feature android:name="android.hardware.sensor.gyroscope" android:required="false"/>` দিয়ে Play filter ঠিক করুন।
- `registerListener(listener, sensor, samplingPeriodUs, maxReportLatencyUs)`।
  - `SENSOR_DELAY_NORMAL` (200 ms), `UI`, `GAME` (20 ms), `FASTEST` (0) বা নিজের microsecond।
  - Rate একটা **hint**। System বেশি বা কম দিতে পারে। নিজে timestamp দেখে মাপুন।
- Callback default main thread-এ। High rate হলে `Handler` (HandlerThread) দিন।
- **Lifecycle:** UI-র জন্য হলে screen দেখা গেলেই register, না দেখা গেলে unregister।

```kotlin
fun SensorManager.events(sensor: Sensor, periodUs: Int): Flow<SensorEvent> = callbackFlow {
    val listener = object : SensorEventListener {
        override fun onSensorChanged(e: SensorEvent) { trySend(e) }
        override fun onAccuracyChanged(s: Sensor, accuracy: Int) = Unit
    }
    registerListener(listener, sensor, periodUs)
    awaitClose { unregisterListener(listener) }
}
// UI: flow.collectAsStateWithLifecycle() — STOPPED হলে collection বন্ধ → unregister
```

- **সাবধান:** `SensorEvent` object system reuse করতে পারে। `event.values` পরে লাগলে copy করুন (`values.copyOf()`)।
- **Hardware vs composite:** Accelerometer, gyro, magnetometer, light, pressure = hardware। Rotation vector, gravity, linear acceleration, step counter = composite (fusion)। `sensor.vendor`/`name` দেখে বোঝা যায় না সবসময় — শুধু জানুন composite-এর পেছনে কয়েকটা chip চলে, তাই battery বেশি।
- Debug: `adb shell dumpsys sensorservice` — কোন app কোন sensor কোন rate-এ চালাচ্ছে।

**Answer (English):**
> "I get the sensor from `SensorManager` and check for null, because not every device has it. Then I register a `SensorEventListener` with a sampling period and, if possible, a max report latency for batching. The rate is only a hint, so I measure real timing from `event.timestamp`. Lifecycle is the key part. I wrap the listener in a `callbackFlow` and unregister in `awaitClose`, then collect with `collectAsStateWithLifecycle`, so it stops when the screen is not visible. If you forget to unregister, the sensor keeps running and drains the battery. For high rates, I deliver callbacks on a background thread, not the main thread."

**Key words:** `SensorManager` · `SensorEventListener` · `samplingPeriodUs` · `callbackFlow` · `unregisterListener` · `composite sensor`

**Follow-up:**
- **Q:** Why copy `event.values`?
  **A:** "The system can reuse the event object for the next reading. If I keep a reference, the values may change under me."
- **Q:** How do you check what sensors a device has?
  **A:** "`getSensorList(Sensor.TYPE_ALL)` in code, or `adb shell dumpsys sensorservice`, which also shows active connections and rates."
- **Q:** Where do callbacks run?
  **A:** "On the main thread by default. I pass a `Handler` on a `HandlerThread` for high rates, so the UI does not jank."

**ভুল করবেন না:** `onResume`-এ register করে `onPause`-এ unregister ভুলে যাওয়া — সবচেয়ে common battery bug।

**আরও দেখুন:** [N3 · Sensor battery](#n3) · [K19 · callbackFlow](#k19) · [B3 · Sensors to Flutter](#b3)

---

### <a id="n2"></a>N2. ★ What is the difference between accelerometer, gyroscope and magnetometer? How do you get device orientation?

**প্রশ্নটা মানে:** প্রতিটা sensor কী মাপে, কোথায় দুর্বল, আর fusion কেন লাগে।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you build a compass?" · "What is the rotation vector sensor?"

**বুঝে নিন:**

| Sensor | কী মাপে | একক | দুর্বলতা |
|---|---|---|---|
| Accelerometer | মোট acceleration, gravity সহ | m/s² | Noise বেশি; নড়লে gravity আর movement আলাদা করা কঠিন |
| Gyroscope | ঘোরার গতি (angular velocity) | rad/s | Integrate করলে **drift** — সময়ের সাথে ভুল জমে |
| Magnetometer | Magnetic field (north কোন দিকে) | µT | কাছে metal, motor, speaker থাকলে ভুল |

- **Sensor fusion:** তিনটা মিলিয়ে ভালো ফল। Gyro দ্রুত আর smooth, accelerometer gravity দিয়ে tilt ঠিক করে, magnetometer north দিয়ে heading ঠিক করে।
- **Composite (fused) sensor — Android নিজে দেয়:**
  - `TYPE_ROTATION_VECTOR`: accel + gyro + mag → পুরো orientation (north সহ)।
  - `TYPE_GAME_ROTATION_VECTOR`: mag ছাড়া → heading ধীরে drift করে, কিন্তু metal-এর কাছে ঠিক থাকে।
  - `TYPE_GEOMAGNETIC_ROTATION_VECTOR`: gyro ছাড়া → কম battery, কম smooth।
  - `TYPE_GRAVITY`, `TYPE_LINEAR_ACCELERATION` (gravity বাদ দেওয়া)।
- **Orientation পাওয়া:**

```kotlin
val r = FloatArray(9); val remapped = FloatArray(9); val angles = FloatArray(3)
SensorManager.getRotationMatrixFromVector(r, event.values)
// screen ঘোরানো থাকলে axis বদলান (display rotation অনুযায়ী)
SensorManager.remapCoordinateSystem(r, SensorManager.AXIS_X, SensorManager.AXIS_Z, remapped)
SensorManager.getOrientation(remapped, angles)  // azimuth, pitch, roll (radian)
val azimuthDeg = Math.toDegrees(angles[0].toDouble())
```

- **Coordinate system:** Axis ঠিক হয় device-এর natural orientation দিয়ে। Screen landscape হলেও axis বদলায় না — তাই `remapCoordinateSystem` লাগে। কোন axis দেবেন সেটা use case-এর উপর। উপরের code-টা device সোজা ধরে camera-র দিকে তাকানোর জন্য (AR/camera)।
- **Magnetic north vs true north:** `GeomagneticField(lat, lon, alt, time).declination` যোগ করুন।
- Camera device-এ আসল use case: PTZ বা tilt detect, আর tamper detect (কেউ camera সরালে accelerometer spike)।

**Answer (English):**
> "The accelerometer measures acceleration including gravity, so it gives tilt but it is noisy when the device moves. The gyroscope measures rotation speed. It is smooth and fast, but if you integrate it, it drifts. The magnetometer gives the direction of north, but metal and motors disturb it. So we fuse them. Android already does this in the rotation vector sensor. I use `TYPE_ROTATION_VECTOR`, convert it with `getRotationMatrixFromVector`, remap for the screen rotation, and call `getOrientation` to get azimuth, pitch and roll. If magnetic noise is a problem, I use the game rotation vector, which has no magnetometer but slowly drifts in heading."

**Key words:** `accelerometer` · `gyroscope` · `magnetometer` · `drift` · `rotation vector` · `remapCoordinateSystem`

**Follow-up:**
- **Q:** How do you detect that someone moved a fixed security camera?
  **A:** "I watch the accelerometer for a spike, and compare the gravity direction to a saved baseline. A change in tilt that stays means the camera was moved."
- **Q:** Why does the compass jump near a laptop?
  **A:** "The magnetometer picks up the laptop's magnetic field. I watch the accuracy callback and ask the user to calibrate, or use game rotation vector if north is not needed."

**আরও দেখুন:** [N5 · Noisy data](#n5) · [N1 · Read sensors](#n1)

---

### <a id="n3"></a>N3. ★ How do you use sensors without killing the battery?

**প্রশ্নটা মানে:** Batching, wake-up sensor, trigger sensor — battery-friendly design জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "What is sensor batching?" · "How do you detect movement all day with low power?"

**বুঝে নিন:**
- **সবচেয়ে বড় কথা:** দরকার যত কম rate, তত কম battery। 50 Hz লাগলে 200 Hz চাইবেন না।
- **Batching (`maxReportLatencyUs`):** Sensor hub event FIFO-তে জমায়, একসাথে পাঠায়। CPU কম জাগে।
  ```kotlin
  sensorManager.registerListener(listener, accel,
      20_000,          // 50 Hz sampling
      10_000_000)      // 10 s পর্যন্ত জমাতে পারে
  ```
  Hardware FIFO না থাকলে (`sensor.fifoMaxEventCount == 0`) batching হয় না — event একটা একটা করে আসে। দরকারে `sensorManager.flush(listener)`।
- **Wake-up vs non-wake-up:**
  - **Non-wake-up:** CPU ঘুমালে CPU জাগায় না। FIFO ভরলে পুরোনো event হারায়।
  - **Wake-up:** দরকারে CPU জাগিয়ে event দেয়, হারায় না। কিন্তু বেশি battery।
  - `getDefaultSensor(type, true)` দিয়ে wake-up version চান (সব device-এ থাকে না)।
- **Trigger sensor — Significant motion:** একবার fire হয়, তারপর নিজে বন্ধ। নড়াচড়া শুরু হলে জানায়, খুব কম power।
  ```kotlin
  val sig = sensorManager.getDefaultSensor(Sensor.TYPE_SIGNIFICANT_MOTION)
  val trigger = object : TriggerEventListener() {
      override fun onTrigger(e: TriggerEvent) { startDetailedTracking() }  // দরকারে আবার request
  }
  sig?.let { sensorManager.requestTriggerSensor(trigger, it) }
  ```
- **Pattern:** কম-power sensor (significant motion / step detector) দিয়ে জানুন নড়াচড়া শুরু হলো → তখন কিছুক্ষণ high-rate sensor চালান → আবার বন্ধ করুন।
- **Main thread বা UI-তে প্রতিটা event পাঠাবেন না।** Process background thread-এ, UI-তে throttled state।
- মাপুন: `dumpsys sensorservice`, `dumpsys batterystats`, Battery Historian / Perfetto power।

**Answer (English):**
> "First, I use the lowest rate that works. Then I use batching: I pass `maxReportLatencyUs` so the sensor hub stores events in its FIFO and delivers them together, and the CPU can sleep. Non-wake-up sensors don't wake the CPU, so events can be lost when the FIFO is full; wake-up sensors don't lose them but cost more power. For all-day detection I use significant motion with a `TriggerEventListener`. It fires once when movement starts, at very low power, and then I turn on high-rate sensors for a short time. I always check the result with `dumpsys sensorservice` and batterystats, not by guessing."

**Key words:** `batching` · `maxReportLatencyUs` · `FIFO` · `wake-up sensor` · `significant motion` · `TriggerEventListener`

**Follow-up:**
- **Q:** What if the device has no FIFO?
  **A:** "Then batching is ignored and events come one by one. The code still works, it just costs more. I check `fifoMaxEventCount`."
- **Q:** Can batching break real-time features?
  **A:** "Yes. A 10-second latency is fine for logging, but not for a live tilt alarm. I pick latency per feature."

**আরও দেখুন:** [N4 · Background sensors](#n4) · [P7 · Battery](#p7) · [N1 · Read sensors](#n1)

---

### <a id="n4"></a>N4. ★ How do you read sensors in the background? What limits does Android have?

**প্রশ্নটা মানে:** Android 9, 12, 14-এর নিয়ম মেনে background-এ sensor চালানো।
**অন্যভাবেও জিজ্ঞেস করে:** "Your app stops getting accelerometer data when the screen is off. Why?" · "Why is my sensor rate capped at 200 Hz?"

**বুঝে নিন:**
- **Android 9+:** Background app (কোনো foreground component নেই) sensor event পায় না — continuous (accelerometer, gyro) আর on-change দুটোই। Register থাকে, শুধু event আসে না।
- **উপায়: Foreground service** (notification সহ)। Android 14+-এ type লাগবে:
  - Fitness / health → `health` (`FOREGROUND_SERVICE_HEALTH` + নিচের যেকোনো একটা: `HIGH_SAMPLING_RATE_SENSORS` declare, বা `ACTIVITY_RECOGNITION` / body sensor permission granted)।
  - External device-এর সাথে → `connectedDevice`।
  - Location-এর সাথে → `location`।
  - আর কিছু না মিললে → `specialUse` (Play-তে কারণ লিখতে হয়)।
- **Android 12+ background থেকে FGS start** বেশিরভাগ ক্ষেত্রে বন্ধ। User action থেকে start করুন।
- **Android 12 rate limit:** target 31+ হলে sensor rate **200 Hz**-এ cap (direct channel-এ `RATE_NORMAL`)। বেশি চাইলে:
  ```xml
  <uses-permission android:name="android.permission.HIGH_SAMPLING_RATE_SENSORS"/>
  ```
  Normal permission (install-time)। কিন্তু user mic toggle বন্ধ করলে আবার cap হতে পারে।
- **Android 16 health permission:** target 36 হলে `BODY_SENSORS`-এর জায়গায় আলাদা আলাদা ছোট permission (যেমন `android.permission.health.READ_HEART_RATE`, `READ_OXYGEN_SATURATION`, `READ_SKIN_TEMPERATURE`)। `BODY_SENSORS_BACKGROUND`-এর জায়গায় `READ_HEALTH_DATA_IN_BACKGROUND`।
- **Custom device-এ (নিজের OS):** System/persistent app-এ এই সমস্যা কম। কিন্তু তবুও ঠিক design: native daemon বা system service sensor পড়ে, app শুধু ফল দেখায়।
- **কখন FGS লাগে না:**
  - Step count: step counter sensor hardware-এ সারাদিন গোনে, CPU ঘুমালেও (N6)। App ফিরে এলে মোট value পায়।
  - দিনে কয়েকবার অল্প data: সাবধান। WorkManager-এর কাজ background-এ চলে, তাই সেখানে sensor event না-ও আসতে পারে। Real device-এ test করুন; না এলে ছোট সময়ের জন্য FGS লাগবে।

**Answer (English):**
> "Since Android 9, an app in the background does not get sensor events at all. So for continuous reading I use a foreground service with a notification. On Android 14 and later it needs a type, for example `health` for fitness data or `connectedDevice` for an external device, with the matching permission. And since Android 12, I must start it from a user action, not from the background. Also since Android 12, rates above 200 Hz need the `HIGH_SAMPLING_RATE_SENSORS` permission. If I need data only now and then, I avoid a long service. For steps, the step counter keeps counting in hardware, even while the CPU sleeps."

**Key words:** `background sensor limit` · `foreground service type` · `health` · `HIGH_SAMPLING_RATE_SENSORS` · `200 Hz`

**Follow-up:**
- **Q:** Does `HIGH_SAMPLING_RATE_SENSORS` need a runtime prompt?
  **A:** "No, it is a normal permission, granted at install. But Play may ask why you need it, so only declare it when you really need high rates."
- **Q:** On your own OS, how would you run sensor logging 24/7?
  **A:** "I would run it in a system-level component — a persistent privileged app or a native service — and expose results to apps. That avoids app background limits by design, not by tricks."

**ভুল করবেন না:** "Service-এ register করলেই background-এ চলবে" — না, foreground service না হলে event আসে না।

**আরও দেখুন:** [C7 · Foreground services](#c7) · [C10 · Background work](#c10) · [N3 · Sensor battery](#n3)

---

### <a id="n5"></a>N5. ◆ How do you handle noisy sensor data?

**প্রশ্নটা মানে:** Filter, calibration, timestamp আর accuracy — data ঠিক রাখার practical জ্ঞান।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you separate gravity from movement?" · "Why should you not use System.currentTimeMillis() for sensor math?"

**বুঝে নিন:**
- **Low-pass filter:** ধীর অংশ রাখে (যেমন gravity)। ঝাঁকুনি বাদ।
- **High-pass filter:** দ্রুত অংশ রাখে (movement)। = আসল value − low-pass।

```kotlin
private val gravity = FloatArray(3)
private const val ALPHA = 0.8f  // বেশি = বেশি smooth, কিন্তু দেরি বেশি

fun onAccel(v: FloatArray): FloatArray {
    for (i in 0..2) gravity[i] = ALPHA * gravity[i] + (1 - ALPHA) * v[i]   // low-pass
    return FloatArray(3) { v[it] - gravity[it] }                          // high-pass = linear accel
}
```
  Android-এর `TYPE_GRAVITY` আর `TYPE_LINEAR_ACCELERATION` এটা আরও ভালো (fusion দিয়ে) করে — থাকলে সেটা নিন।
- **Trade-off:** বেশি smoothing = কম noise কিন্তু বেশি latency। ALPHA একটা fixed number না — sample rate বদলালে ফল বদলায়। ঠিক উপায় হলো time constant আর আসল `dt` দিয়ে alpha হিসাব।
- **Timestamp:** `event.timestamp` nanosecond, `SystemClock.elapsedRealtimeNanos()` base। Event আসলে মাপা হয়েছে কখন সেটা বলে (batching হলে callback অনেক পরে আসে)। `dt` = দুই event-এর timestamp-এর পার্থক্য। Wall clock বদলাতে পারে (NTP, user) — তাই ব্যবহার করবেন না।
- **Accuracy callback:** `onAccuracyChanged` → `SENSOR_STATUS_UNRELIABLE`, `ACCURACY_LOW/MEDIUM/HIGH`। Magnetometer-এ low হলে user-কে calibrate করতে বলুন (ফোন ঘোরানো)। `event.accuracy`-ও আছে।
- **Calibration:**
  - Android calibrated value দেয়। Raw লাগলে `TYPE_*_UNCALIBRATED` (bias আলাদা দেয়)।
  - নিজের device-এ factory calibration (offset, scale) — HAL বা নিজের config-এ রাখুন।
  - App-level: স্থির অবস্থায় কিছুক্ষণ পড়ে offset বের করা (যেমন camera mount-এর "zero")।
- **Outlier:** Median filter spike বাদ দেয়। Threshold-এ hysteresis দিন যাতে alarm বারবার on/off না হয়।

**Answer (English):**
> "I use a low-pass filter to keep the slow part, like gravity, and a high-pass filter — the value minus the low-pass — to get movement. If the device has `TYPE_GRAVITY` or `TYPE_LINEAR_ACCELERATION`, I use those, because they are fused and better. The trade-off is smoothing against delay, so I set the filter from the real time step, not a magic number. For time I always use `event.timestamp`, which is in nanoseconds since boot and shows when the sample was taken. Wall clock can jump and batched events arrive late. I also listen to `onAccuracyChanged` and ask for calibration when the magnetometer is unreliable."

**Key words:** `low-pass filter` · `high-pass filter` · `event.timestamp` · `elapsedRealtimeNanos` · `onAccuracyChanged` · `uncalibrated`

**Follow-up:**
- **Q:** How do you avoid an alarm that flickers on and off?
  **A:** "I add hysteresis — one threshold to turn on and a lower one to turn off — and require the condition for a short time before firing."

**আরও দেখুন:** [N2 · Orientation](#n2) · [N12 · Test sensor code](#n12)

---

### <a id="n6"></a>N6. ◆ What is the difference between the step counter and the step detector? Where do Activity Recognition and Health Connect fit?

**প্রশ্নটা মানে:** Step আর activity data নেওয়ার সঠিক API, আর কোনটা GMS-এ নির্ভর করে।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you count steps all day with low battery?" · "How do you know if the user is walking or driving?"

**বুঝে নিন:**

| | Step counter | Step detector |
|---|---|---|
| Type | `TYPE_STEP_COUNTER` | `TYPE_STEP_DETECTOR` |
| Value | Boot থেকে মোট step (float) | প্রতিটা step-এ একটা event (value 1.0) |
| Latency | বেশি (batched), কিন্তু ঠিক হিসাব | কম, প্রতিটা step-এ |
| ভালো | দৈনিক মোট, কম power | Live UI, step-এর সময় |

- Step counter **reboot-এ 0** হয়। তাই নিজের baseline রাখুন: শেষ value আর reboot detect (`BOOT_COMPLETED` বা value কমে গেলে)।
- Register থাকলে CPU ঘুমালেও hardware গুনতে থাকে। App পরে value পড়লে মাঝের সব step পায়। তাই সারাদিনের জন্য ভালো।
- Android 10+: `ACTIVITY_RECOGNITION` runtime permission লাগে।
- **Activity Recognition API** (Google Play services): walking, running, cycling, in vehicle, still। **Transition API** — শুধু বদলের সময় জানায় (enter/exit), কম battery। GMS লাগে — custom non-GMS device-এ নেই।
- **Health Connect:** Android-এর health data store। Android 14+-এ platform-এর অংশ (তার আগে আলাদা app)। App-গুলো step, heart rate ইত্যাদি এখানে লেখে আর পড়ে, user permission দিয়ে। নিজে sensor থেকে গোনার বদলে এখান থেকে পড়লে অন্য app/wearable-এর data-ও পাবেন।
- Custom device (GMS নেই): sensor (step counter / significant motion) + নিজের simple classifier, বা on-device ML (LiteRT)।

**Answer (English):**
> "The step counter gives the total steps since boot. It is batched, low power and accurate, so it is best for daily totals. It resets on reboot, so I store my own baseline. The step detector sends one event for each step with low delay, so it is good for live UI. Both need the `ACTIVITY_RECOGNITION` permission since Android 10. To know walking or driving, I use the Activity Recognition Transition API, which only tells me when the activity changes — but it needs Play services. For health apps, I read and write through Health Connect, which is part of the platform since Android 14, so the user controls the data."

**Key words:** `TYPE_STEP_COUNTER` · `TYPE_STEP_DETECTOR` · `ACTIVITY_RECOGNITION` · `Transition API` · `Health Connect`

**Follow-up:**
- **Q:** What do you do on a device without Play services?
  **A:** "I use the raw sensors — step counter and significant motion — and maybe a small on-device model for activity type."

**আরও দেখুন:** [N3 · Sensor battery](#n3) · [N4 · Background sensors](#n4) · [N7 · Location](#n7)

---

### <a id="n7"></a>N7. ★ How do you get location on Android?

**প্রশ্নটা মানে:** Fused location, priority, permission (foreground/background/approximate), geofence, mock — সব জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you track location in the background?" · "How do you detect fake GPS?"

**বুঝে নিন:**
- **`FusedLocationProviderClient`** (Play services): GPS, Wi‑Fi, cell, sensor মিলিয়ে দেয়। Battery বুঝে কাজ করে।
  ```kotlin
  val request = LocationRequest.Builder(Priority.PRIORITY_BALANCED_POWER_ACCURACY, 60_000L)
      .setMinUpdateIntervalMillis(30_000L)
      .setMinUpdateDistanceMeters(20f)
      .build()
  client.requestLocationUpdates(request, callback, Looper.getMainLooper())
  // বন্ধ: client.removeLocationUpdates(callback)
  ```
- **Priority:** `HIGH_ACCURACY` (GPS, বেশি battery) · `BALANCED_POWER_ACCURACY` (~block level) · `LOW_POWER` (~city) · `PASSIVE` (অন্য app-এর location চুপচাপ নেয়)।
- **Permission:**
  - `ACCESS_COARSE_LOCATION` + `ACCESS_FINE_LOCATION` একসাথে চান। Android 12+-এ user শুধু approximate দিতে পারে — app-কে সেটা মেনে চলতে হবে।
  - Background: `ACCESS_BACKGROUND_LOCATION` — Android 11+-এ **আলাদা** ধাপে, user Settings-এ গিয়ে "Allow all the time" দেয়। Play policy-তে কঠিন review।
  - বিকল্প: background permission না নিয়ে **foreground service type `location`** — user জানে, notification আছে।
  - Background-এ (FGS ছাড়া) app ঘণ্টায় কয়েকবার মাত্র update পায় (Android 8+)।
- **Geofencing:** `GeofencingClient`। Circle region, ENTER/EXIT/DWELL। App প্রতি সর্বোচ্চ 100 geofence। Background location permission লাগে। Event কয়েক মিনিট দেরিতে আসতে পারে। Reboot-এ আবার register করতে হয়।
- **Mock location:** `location.isMock` (API 31+; আগে `isFromMockProvider`)। এটার উপর পুরো ভরসা করবেন না। Server-এও check করুন (হঠাৎ লাফ, অসম্ভব speed)।
- **GMS ছাড়া (custom device):** `LocationManager` — `GPS_PROVIDER`, `NETWORK_PROVIDER` (থাকলে), Android 12+ `FUSED_PROVIDER` (AOSP-এর নিজের fused)। `LocationManagerCompat` সাহায্য করে।
- Fixed camera-র জন্য: location একবার setup-এ নিন, সবসময় track না।

**Answer (English):**
> "With Play services, I use `FusedLocationProviderClient` and build a `LocationRequest` with a priority and an interval. Priority is the main battery choice — high accuracy uses GPS, balanced is often enough. I ask for coarse and fine together, and my app must work if the user gives only approximate. Background location since Android 11 is a separate step in Settings and Play reviews it hard, so I prefer a foreground service of type `location` while tracking. For regions I use geofencing, with a limit of 100 per app. I check `isMock` to detect fake GPS, but I also check it on the server. On a device without GMS, I use `LocationManager` directly."

**Key words:** `FusedLocationProviderClient` · `Priority` · `ACCESS_BACKGROUND_LOCATION` · `approximate location` · `geofencing` · `isMock`

**Follow-up:**
- **Q:** Why is my location update slow in the background?
  **A:** "Since Android 8, background apps get location only a few times an hour. A foreground service fixes it, if the use case really needs it."
- **Q:** How do you save battery while tracking a moving device?
  **A:** "Use balanced priority, a minimum distance, and batching with `setMaxUpdateDelayMillis`. Switch to high accuracy only when needed."
- **Q:** What if the user denies fine location?
  **A:** "The app must still work with approximate location, or explain clearly why precise is needed and ask again at the right moment."

**আরও দেখুন:** [C13 · Runtime permissions](#c13) · [C7 · Foreground services](#c7) · [N4 · Background sensors](#n4)

---

### <a id="n8"></a>N8. ★ How do you work with Bluetooth Low Energy devices on Android?

**প্রশ্নটা মানে:** BLE-র পুরো flow আর Android-এর বাস্তব সমস্যা (permission, queue, MTU, reconnect, scan limit)।
**অন্যভাবেও জিজ্ঞেস করে:** "Your BLE writes randomly fail. Why?" · "What permissions do you need for BLE on Android 12+?"

**বুঝে নিন:**
- **Flow:** Scan → `connectGatt()` → `discoverServices()` → characteristic read / write / notify → disconnect + `close()`।
- **GATT:** Device-এ **service** (UUID), service-এর ভেতর **characteristic** (value + property: read/write/notify)। Notify চালু করতে `setCharacteristicNotification` + CCCD descriptor (`0x2902`)-এ write।
- **Permission (Android 12+):**
  ```xml
  <uses-permission android:name="android.permission.BLUETOOTH_SCAN"
      android:usesPermissionFlags="neverForLocation" />
  <uses-permission android:name="android.permission.BLUETOOTH_CONNECT" />
  <!-- Android 11 এবং নিচে: BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION (maxSdkVersion দিয়ে) -->
  ```
  `neverForLocation` দিলে location permission লাগে না, কিন্তু কিছু beacon result system ফিল্টার করে দিতে পারে।
- **এক সময়ে একটাই GATT operation:** আগের callback (`onCharacteristicWrite` ইত্যাদি) না আসা পর্যন্ত পরেরটা দিলে `false` বা চুপচাপ fail। তাই **command queue** বানান (Channel/Mutex + timeout)।
- **নতুন API (Android 13+):** `writeCharacteristic(characteristic, value, writeType)` — পুরোনো `characteristic.value = ...` deprecated।
- **MTU:** Default 23 → payload 20 byte। `requestMtu(517)` বড় করে; ফল = দুই দিকের ছোটটা; payload = MTU − 3। Android 14+-এ stack প্রথম request-এ 517 চায় (আপনি যা-ই দিন) — কিছু firmware এতে সমস্যা করে; negotiated value থেকেই size নিন।
- **Reconnect:** `connectGatt(ctx, autoConnect = false, cb, TRANSPORT_LE)` দ্রুত প্রথম connect। `autoConnect = true` ধীর কিন্তু device ফিরে এলে নিজে connect করে। Status 133 (`GATT_ERROR`) common — `close()` করে একটু পরে আবার চেষ্টা, backoff সহ। প্রতিবার disconnect-এ `gatt.close()` — না হলে client slot leak।
- **Scan limit:**
  - 30 সেকেন্ডে 5 বারের বেশি scan start করলে system scan চুপচাপ বন্ধ রাখে।
  - Screen off হলে unfiltered scan বন্ধ — `ScanFilter` দিন (service UUID / MAC)।
  - Background scan: `PendingIntent` দিয়ে `startScan` বা CDM (N9)।
- GATT callback Binder thread-এ আসে। UI update main thread-এ নিন।

**Answer (English):**
> "I scan with a filter, connect with `connectGatt` using the LE transport, discover services, and then read, write or enable notifications on characteristics. On Android 12 and later I need `BLUETOOTH_SCAN` and `BLUETOOTH_CONNECT`, and I mark scan as `neverForLocation` when I don't use it for location. The biggest trap is that GATT allows one operation at a time, so I put all operations in a queue and wait for each callback, with a timeout. I request a bigger MTU and size packets from the negotiated value. For reconnects I always `close()` the old GATT and retry with backoff. And I don't start scans more than five times in thirty seconds, or Android blocks them."

**Key words:** `GATT` · `characteristic` · `CCCD` · `operation queue` · `MTU` · `BLUETOOTH_CONNECT` · `status 133`

**Follow-up:**
- **Q:** What causes status 133?
  **A:** "It is a generic error. Often too many open GATT clients, a connect timeout, or the device out of range. I close the GATT, wait a bit, and retry."
- **Q:** How do you send a 10 KB firmware file over BLE?
  **A:** "Split it into chunks of MTU minus 3, use write-without-response with flow control, or write-with-response for safety, and check a CRC at the end."
- **Q:** Why does scanning return nothing when the screen is off?
  **A:** "Android stops unfiltered scans when the screen is off. I add a `ScanFilter` with the service UUID."

**ভুল করবেন না:** একসাথে কয়েকটা `writeCharacteristic` call করা — দ্বিতীয়টা fail করে, আর bug random মনে হয়।

**আরও দেখুন:** [N9 · Companion Device Manager](#n9) · [K16 · Thread safety](#k16) · [N10 · USB and serial](#n10)

---

### <a id="n9"></a>N9. ◆ What is Companion Device Manager and why use it?

**প্রশ্নটা মানে:** BLE/Wi‑Fi device pair করার system-level সঠিক উপায় জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How can your app talk to its device in the background?" · "How do you pair a device without asking for location?"

**বুঝে নিন:**
- `CompanionDeviceManager` (CDM): System নিজের dialog দেখায়, user device বেছে নেয়। App-কে নিজে scan করতে হয় না।
- **কেন ভালো:**
  - Scan-এর জন্য location/scan permission লাগে না (system scan করে)।
  - Associate হলে app কিছু **background সুবিধা** চাইতে পারে: `REQUEST_COMPANION_RUN_IN_BACKGROUND`, `REQUEST_COMPANION_USE_DATA_IN_BACKGROUND`, আর background থেকে foreground service start (`REQUEST_COMPANION_START_FOREGROUND_SERVICES_FROM_BACKGROUND`)।
  - **Presence:** `CompanionDeviceService` — device কাছে এলে বা চলে গেলে system app-কে জাগায় (Android 12+)। নতুন Android version-এ এই API-র রূপ বদলেছে — docs দেখুন।
  - Device profile (watch, glasses ইত্যাদি) দিলে আরও permission সহজ।
- **Flow:**
  ```kotlin
  val request = AssociationRequest.Builder()
      .addDeviceFilter(BluetoothLeDeviceFilter.Builder()
          .setScanFilter(ScanFilter.Builder().setServiceUuid(ParcelUuid(MY_SERVICE)).build())
          .build())
      .setSingleDevice(true)
      .build()
  cdm.associate(request, mainExecutor, object : CompanionDeviceManager.Callback() {
      override fun onAssociationPending(sender: IntentSender) { launcher.launch(IntentSenderRequest.Builder(sender).build()) }
      override fun onFailure(error: CharSequence?) { /* show error */ }
  })
  ```
  (`associate(..., Executor, Callback)` API 33+; পুরোনো version-এ Handler overload।)
- Connect-এর জন্য তবুও `BLUETOOTH_CONNECT` লাগে।

**Answer (English):**
> "Companion Device Manager lets the system show the pairing dialog. I give a filter, like my service UUID, and the user picks the device. The app does not scan by itself, so it does not need location or scan permission for that. After association the app can ask for companion permissions to run and use data in the background, and even start a foreground service from the background. With `CompanionDeviceService`, the system can wake my app when the device comes in range. For a camera or sensor companion app, this is the cleanest way to keep a link without fighting background limits."

**Key words:** `CompanionDeviceManager` · `AssociationRequest` · `CompanionDeviceService` · `device presence` · `REQUEST_COMPANION_RUN_IN_BACKGROUND`

**Follow-up:**
- **Q:** Does CDM replace BLE code?
  **A:** "No. It handles discovery, pairing approval and background rights. I still use GATT for the data."

**আরও দেখুন:** [N8 · BLE](#n8) · [C7 · Foreground services](#c7)

---

### <a id="n10"></a>N10. ◆ How do you talk to USB and serial devices from an Android app?

**প্রশ্নটা মানে:** USB host mode, permission, device filter, আর serial library — practical জ্ঞান।
**অন্যভাবেও জিজ্ঞেস করে:** "How does your app open automatically when a device is plugged in?" · "How do you read a USB-to-serial sensor?"

**বুঝে নিন:**
- **USB host mode:** Android device host, বাইরের device peripheral। `UsbManager` দিয়ে device list, `openDevice()` → `UsbDeviceConnection`, তারপর `bulkTransfer` / `controlTransfer`।
- **Permission:** প্রতিটা device-এর জন্য user permission।
  ```kotlin
  val pi = PendingIntent.getBroadcast(ctx, 0,
      Intent(ACTION_USB_PERMISSION).setPackage(ctx.packageName),
      PendingIntent.FLAG_MUTABLE)   // system extra যোগ করে, তাই MUTABLE + explicit
  usbManager.requestPermission(device, pi)
  ```
  Receiver register-এ Android 14+-এ `RECEIVER_NOT_EXPORTED`-এর মতো flag দিন (ContextCompat)।
- **Auto-open + device filter:** Activity-তে `USB_DEVICE_ATTACHED` intent-filter আর meta-data:
  ```xml
  <!-- res/xml/device_filter.xml -->
  <resources><usb-device vendor-id="1027" product-id="24577" /></resources>
  ```
  User "always open" দিলে পরেরবার dialog আসে না।
- **Serial (CDC-ACM, FTDI, CP210x, CH34x, PL2303):** Android-এ built-in serial API নেই। Open-source library `usb-serial-for-android` এগুলোর driver দেয় (baud rate, read/write)।
- **Board-এর UART (`/dev/ttyS*`):** Normal app খুলতে পারে না (file permission + SELinux)। নিজের OS-এ: system service/HAL (O13) বা ঠিক SELinux + group সহ privileged app।
- **Practical:**
  - Read loop আলাদা thread বা coroutine-এ (`Dispatchers.IO`)।
  - Unplug (`USB_DEVICE_DETACHED`) সামলান।
  - Protocol-এ framing আর CRC রাখুন।
  - Power: phone কতটা current দিতে পারে দেখুন।

**Answer (English):**
> "I use USB host mode with `UsbManager`. I find the device by vendor and product ID, ask the user for permission with a mutable, explicit `PendingIntent`, then open a connection and use bulk transfers. To open the app automatically when the device is plugged in, I add a `USB_DEVICE_ATTACHED` intent filter with a device filter XML. For USB-to-serial chips like FTDI or CP210x there is no built-in API, so I use the `usb-serial-for-android` library. I run reads on a background thread and handle unplug events. A board UART like `/dev/ttyS1` is different — a normal app can't open it, so on our own OS I would expose it through a system service."

**Key words:** `USB host` · `UsbManager` · `requestPermission` · `device_filter` · `USB_DEVICE_ATTACHED` · `usb-serial-for-android`

**Follow-up:**
- **Q:** Why must the permission PendingIntent be mutable?
  **A:** "The system adds the result extras, like whether permission was granted, to that intent. An immutable one can't be filled, so I make it mutable but explicit with `setPackage`."

**আরও দেখুন:** [O13 · Custom hardware](#o13) · [N8 · BLE](#n8) · [C5 · PendingIntent](#c5)

---

### <a id="n13"></a>N13. ○ How does NFC work on Android? Reading tags and Host Card Emulation

**প্রশ্নটা মানে:** NFC tag পড়া/লেখা আর phone-কে card বানানো (HCE) — basic আর নিরাপত্তা জানেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you set up a camera by tapping an NFC tag?" · "What is HCE and when do you use it?"

**বুঝে নিন:**
- **এক কথায়:** NFC = খুব কাছের (কয়েক cm) wireless। Android-এ দুইটা কাজ: tag পড়া/লেখা, আর phone নিজে card হওয়া (HCE)।
- **Setup:** Manifest-এ `android.permission.NFC` (normal permission) আর `<uses-feature android:name="android.hardware.nfc" android:required="false"/>`। `NfcAdapter.getDefaultAdapter(context)` null হলে NFC নেই। `isEnabled` false হলে user-কে Settings-এ পাঠান।
- **Tag পড়ার দুই উপায়:**
  - **Intent dispatch:** System tag পড়ে intent পাঠায়। ক্রম: `NDEF_DISCOVERED` → `TECH_DISCOVERED` → `TAG_DISCOVERED`। App বন্ধ থাকলেও manifest filter দিয়ে খুলতে পারে।
  - **Reader mode (screen খোলা থাকলে ভালো):** `enableReaderMode` — শুধু আপনার app tag পায়, system-এর sound/dialog ছাড়া। `onResume`-এ চালু, `onPause`-এ `disableReaderMode`।
  ```kotlin
  nfcAdapter.enableReaderMode(this, { tag ->
      val ndef = Ndef.get(tag) ?: return@enableReaderMode
      ndef.connect()
      val msg = ndef.cachedNdefMessage   // NDEF records: URI, text, MIME
      ndef.close()
      msg?.let(::handleMessage)
  }, NfcAdapter.FLAG_READER_NFC_A or NfcAdapter.FLAG_READER_NFC_B, null)
  ```
  Callback background (Binder) thread-এ আসে। I/O সেখানেই করুন, UI update main thread-এ।
- **NDEF:** Tag-এর ভেতরের standard data format। Record হতে পারে URI, text বা নিজের MIME type। লিখতে `Ndef.writeNdefMessage(...)`।
- **HCE (Host Card Emulation):** Phone একটা card-এর মতো কাজ করে। `HostApduService` বানান, XML-এ AID (application ID) দিন। Reader APDU command পাঠায়, আপনার service উত্তর দেয়। Use case: access card, transit, loyalty। Payment হলে আলাদা category আর অনেক নিয়ম।
- **Security:**
  - Tag-এর UID গোপন না — copy করা যায়। শুধু UID দিয়ে দরজা খোলা বা login করবেন না।
  - Tag-এর data সাধারণ text। Setup-এর জন্য (যেমন camera-র Wi‑Fi info) data sign বা encrypt করুন, আর app-এ check করুন।
  - HCE-তে secret Keystore-এ রাখুন, server দিয়ে challenge-response করুন।

**Answer (English):**
> "NFC is very short range wireless. On Android I use it in two ways: reading or writing tags, and Host Card Emulation, where the phone acts like a card. For tags, the system can start my app with an `NDEF_DISCOVERED` intent, or, when my screen is open, I use `enableReaderMode` so only my app gets the tag. Most tags hold NDEF records, like a URI or a MIME type. For HCE, I write a `HostApduService` with an AID, and it answers APDU commands from the reader. For security, I never trust the tag UID alone, because it can be copied. If a tag sets up a device, I sign the data and check it in the app."

**Key words:** `NfcAdapter` · `NDEF` · `enableReaderMode` · `NDEF_DISCOVERED` · `HostApduService` · `AID`

**Follow-up:**
- **Q:** How would tap-to-setup work for a camera?
  **A:** "The camera box has a tag with a signed setup record. The app reads it in reader mode, checks the signature, and then connects to the camera over Wi-Fi or BLE."

**ভুল করবেন না:** Tag UID-কে password ভাববেন না — এটা যে কেউ পড়তে আর copy করতে পারে।

**আরও দেখুন:** [N8 · BLE](#n8) · [C5 · PendingIntent](#c5) · [S3 · Keystore](#s3)

---

### <a id="n11"></a>N11. ◆ Which IoT protocol would you choose — MQTT, CoAP or HTTP/WebSocket? How do you keep MQTT alive on Android?

**প্রশ্নটা মানে:** Protocol-এর পার্থক্য, MQTT-র মূল feature, আর Android-এ long connection-এর বাস্তবতা।
**অন্যভাবেও জিজ্ঞেস করে:** "Explain MQTT QoS levels." · "How do your cameras send events to the cloud?"

**বুঝে নিন:**
- **MQTT:** TCP-র উপর (TLS সহ), **broker** দিয়ে publish/subscribe। Topic যেমন `site/42/cam/7/motion`। ছোট header — দুর্বল network-এ ভালো।
  - **QoS 0** = একবার পাঠাও, হারাতে পারে। **QoS 1** = অন্তত একবার — duplicate আসতে পারে, তাই receiver একই message দুবার পেলেও ফল যেন একই থাকে। **QoS 2** = ঠিক একবার (চার ধাপ, ধীর)।
  - **Retained message:** Broker topic-এর শেষ message রাখে; নতুন subscriber সাথে সাথে পায় (যেমন device-এর বর্তমান state)।
  - **Last Will (LWT):** Connect-এর সময় দেওয়া message; device হঠাৎ হারালে broker publish করে (`status = offline`)।
  - **Keep alive:** একটা ঠিক করা সময় পরপর PING যায়। না এলে broker ধরে নেয় connection মারা গেছে।
  - **Persistent session** (MQTT 5: `cleanStart=false` + session expiry) — offline থাকার সময়ের QoS 1/2 message পরে পায়।
- **CoAP:** UDP-র উপর ছোট REST (GET/PUT, observe)। খুব ছোট, battery-চালিত sensor-এর জন্য। NAT/firewall-এ কঠিন, mobile app-এ কম ব্যবহার।
- **HTTP/REST:** মাঝে মাঝে data, সহজ, সব infra চলে। **WebSocket:** দুই দিকে live, browser/dashboard-এর জন্য ভালো।
- **কীভাবে বেছে নিই:** অনেক device, event stream, দুর্বল network, offline/online state → MQTT। মাঝে মাঝে upload, config → HTTP। Constrained sensor node → CoAP। Live UI → WebSocket বা MQTT over WebSocket। বড় video → এগুলো না; RTSP/WebRTC/HLS।
- **Android-এ MQTT চালু রাখা:**
  - Phone app: সারাক্ষণ socket খোলা রাখা যায় না। Doze network বন্ধ করে, আর background-এ process মারা যায়। তাই app খোলা থাকলে connect করুন; background-এ push (FCM) দিয়ে জাগান। খুব দরকার হলে FGS — কিন্তু সীমা আছে (Android 15-এ `dataSync` 24 ঘণ্টায় 6 ঘণ্টা)।
  - Network change-এ reconnect (`ConnectivityManager.NetworkCallback`), exponential backoff + jitter।
  - Library: পুরোনো Paho Android Service maintained না — HiveMQ MQTT client বা Paho Java client নিজের lifecycle দিয়ে।
  - **নিজের OS-এর device:** persistent system app বা native service; Doze allowlist (`sysconfig`); keep alive network অনুযায়ী (cellular NAT timeout-এর চেয়ে ছোট)।
  - **Android 17 (target 37):** broker LAN-এ থাকলে (local IP) `ACCESS_LOCAL_NETWORK` permission লাগবে।
- Security: TLS, প্রতি device আলাদা credential বা client certificate, topic ACL (device শুধু নিজের topic)।

**Answer (English):**
> "For many devices sending events, I choose MQTT. It is pub/sub through a broker, with a small header, so it works well on weak networks. QoS 0 can lose messages, QoS 1 can send duplicates, and QoS 2 is exactly once but slower. Retained messages give new subscribers the last state. Last Will tells everyone when a device drops. I use HTTP for config and uploads, CoAP for tiny battery sensors, and WebSocket for live dashboards. On a phone, I don't keep MQTT open in the background, because Doze breaks it. I use push to wake the app. On our own device, a system service keeps it alive with reconnect and backoff."

**Key words:** `MQTT` · `QoS 0/1/2` · `retained` · `Last Will` · `keep alive` · `CoAP` · `Doze`

**Follow-up:**
- **Q:** How do you show if a camera is online?
  **A:** "The camera publishes a retained `online` status when it connects, and sets a Last Will with `offline`. The broker sends the will if the camera drops."
- **Q:** QoS 1 delivered the same alarm twice. What do you do?
  **A:** "That is expected with at-least-once. I put an event ID in the message and ignore IDs I already handled."

**আরও দেখুন:** [R16 · WebSocket, MQTT, FCM](#r16) · [V9 · Motion alerts](#v9) · [P7 · Battery](#p7)

---

### <a id="n12"></a>N12. ◆ How do you test sensor and hardware code?

**প্রশ্নটা মানে:** Hardware ছাড়া logic test করার design, আর আসল device-এ কীভাবে test করবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you unit test BLE code?" · "How do you reproduce a bug that only happens on a moving vehicle?"

**বুঝে নিন:**
- **Hardware-কে interface-এর পেছনে রাখুন:** এখানে interface দরকারি — test-এ fake লাগে, আর দুইটা আসল implementation আছে (real আর replay)।
  ```kotlin
  interface MotionSource { fun samples(): Flow<MotionSample> }   // MotionSample(tNanos, x, y, z)

  class FakeMotionSource(private val data: List<MotionSample>) : MotionSource {
      override fun samples() = data.asFlow()
  }
  ```
  Logic (filter, step/tilt/tamper detection) আলাদা **pure function** বা class — শুধু sample list নেয়। Android ছাড়া JVM unit test।
- **Time:** `event.timestamp` data-র ভেতরে আসে, তাই test প্রতিবার একই ফল দেয়। Coroutine হলে `runTest` + virtual time। আসল clock বা `sleep` না।
- **Edge case test:** খালি stream, sensor নেই (`null`), accuracy unreliable, timestamp gap (batching), spike/outlier, reboot-এ step counter reset।
- **Recorded data replay:** আসল device থেকে CSV/protobuf-এ record (timestamp সহ) → test fixture। Field bug-এর data record করে regression test বানান — এটাই সবচেয়ে কাজের।
- **BLE:** GATT-কে interface-এর পেছনে রাখুন; fake দিয়ে queue, timeout, disconnect, status 133 test। Hardware-এ: nRF Connect app দিয়ে আরেকটা phone বা dev board peripheral বানিয়ে test।
- **Emulator:** Extended controls → Virtual sensors (accelerometer, rotation ইত্যাদি), location route/GPX playback। Emulator-এ Bluetooth অল্প কাজ করে (নতুন emulator-এ virtual BLE আছে, কিন্তু আসল hardware-এ test লাগবেই)। Cuttlefish-এও virtual sensor।
- **Real device:** Device farm (Firebase Test Lab, নিজের lab-এর rack)। নিজের hardware-এর জন্য নিজের lab — USB hub, power control, adb দিয়ে automation।
- **Platform (নিজের OS):** HAL-এর জন্য VTS-ধরনের test, `dumpsys sensorservice` output check, CTS sensor test।

**Answer (English):**
> "I put the hardware behind a small interface that returns a Flow of samples. The logic — filters and detection rules — lives in pure functions. So I can unit test on the JVM with fake data. The timestamp is inside each sample, so tests give the same result every time. I test edges like no sensor, empty data, gaps from batching, spikes and a counter reset. The most useful trick is replay: I record real sensor data to files, and every field bug becomes a replay test. For BLE, I fake the GATT layer to test the queue and timeouts. Then emulator virtual sensors for quick checks, and real devices for the final test."

**Key words:** `fake` · `interface` · `replay recorded data` · `pure function` · `virtual sensors` · `device farm`

**Follow-up:**
- **Q:** Why not mock `SensorManager` directly?
  **A:** "That tests Android calls, not my logic, and it breaks on refactor. A fake stream at my own interface tests real behaviour."
- **Q:** How do you test BLE reconnect without hardware?
  **A:** "My fake GATT can drop the connection or return error 133 on command. Then I check that the queue resets and reconnect uses backoff."

**আরও দেখুন:** [R14 · ViewModel tests](#r14) · [K26 · Coroutine tests](#k26) · [N5 · Noisy data](#n5)

---


## <a id="part-11"></a>Part 11 — Mobile system design

Senior round-এ প্রায় সবসময় একটা design প্রশ্ন আসে। এখানে তারা code দেখে না। তারা দেখে আপনি বড় কাজ ভাগ করতে পারেন কি না, trade-off বলতে পারেন কি না, আর security ও failure নিয়ে ভাবেন কি না।
Company যদি camera, custom device বা sensor নিয়ে কাজ করে, তাহলে D1, D4, D6 তাদের কাজের সাথে সরাসরি মেলে। এগুলো ভালো করে তৈরি রাখুন।

### আগে বুঝুন — design প্রশ্নের উত্তর কীভাবে দেবেন

**বড় ছবি:** design round-এ "সঠিক উত্তর" বলে কিছু নেই। Interviewer দেখে আপনার চিন্তার পথ। তাই সব প্রশ্নে একই ৬ ধাপ ব্যবহার করুন। মুখস্থ রাখুন:

```
1. Clarify      → কী বানাবো, কী বানাবো না (প্রশ্ন করুন)
2. Scale        → কত user, কত data, কোন device, কোন network
3. Big picture  → বক্স আর তীর: App ↔ Server ↔ অন্য সিস্টেম
4. Data & API   → কোন data কোথায় থাকে, কোন API লাগে
5. Hard parts   → ২–৩টা কঠিন জায়গা + trade-off
6. Safe & sure  → security, testing, monitoring
```

**প্রতিটা ধাপে কী বলবেন:**
- **ধাপ ১ (৩–৫ মিনিট):** ৩–৫টা প্রশ্ন করুন। Must-have আর nice-to-have আলাদা করুন। তারপর জোরে বলুন "So the scope is ..."। এতে বাকি সময় ঠিক জিনিসে যায়।
- **ধাপ ২:** সংখ্যা আন্দাজ করুন। ঠিক না হলেও চলে। যেমন "ধরি একজন user-এর ৪টা camera, দিনে ৫০টা event"। সংখ্যা থেকে design-এর সিদ্ধান্ত আসে (paging লাগবে কি না, cache কত বড়)।
- **ধাপ ৩:** মোবাইলের ভেতরের layer দেখান: UI (Compose) → ViewModel → Repository → local (Room/DataStore/file) + remote (API/WebSocket/FCM)। Server-কে একটা-দুটো বক্সে রাখুন। আপনি mobile engineer, server-এর ভেতরে বেশি ঢুকবেন না।
- **ধাপ ৪:** Room-এর মূল table আর ২–৪টা API endpoint বলুন। "Source of truth কে" — এটা পরিষ্কার বলুন।
- **ধাপ ৫:** এখানেই senior আলাদা হয়। ২–৩টা কঠিন জিনিস বেছে গভীরে যান। প্রতিটায় দুটো option আর একটা choice + কারণ বলুন।
- **ধাপ ৬:** Security (token কোথায়, TLS, permission), testing (কোন layer কীভাবে test), monitoring (কোন metric দেখবেন)।

**মূল ধারণাগুলো, যেগুলোর উপর সব design দাঁড়িয়ে:**
1. **Single source of truth** — UI সবসময় local DB থেকে পড়ে। Network শুধু DB update করে।
2. **Unidirectional data flow** — event উপরে যায় (UI → ViewModel), state নিচে আসে (StateFlow → UI)।
3. **Background work মানে WorkManager** — যে কাজ app বন্ধ হলেও শেষ করতে হবে। User দেখছে এমন লম্বা কাজে foreground notification লাগে।
4. **Push আর pull দুটোই লাগে** — app খোলা থাকলে WebSocket/poll, বন্ধ থাকলে FCM (GMS না থাকলে MQTT বা নিজের push)।
5. **Network ভরসার না** — retry with backoff, idempotent request (client-generated id), resume।
6. **Battery আর data সীমিত** — batch করুন, constraint দিন (charging, unmetered), দরকার না হলে stream বন্ধ রাখুন।
7. **Security কয়েক layer-এ** — transport (TLS), identity (short-lived token, Keystore), data at rest (Tink + Keystore key), server-side check (Play Integrity verdict server-এ verify)।
8. **Server সিদ্ধান্ত নেয়** — permission, sharing, conflict-এর শেষ কথা server-এর। App শুধু UI-তে লুকায়।

**Interview-এ কথা চালানোর English phrase:**
- "Can I ask a few questions first?"
- "So the scope is: ... I will not cover ... for now."
- "Let me assume some numbers. Please stop me if they are wrong."
- "Let me draw the big picture."
- "The source of truth is the local database."
- "The hard part here is ..."
- "There are two options. Option one is ... Option two is ... I would pick ... because ..."
- "The trade-off is ..."
- "If I had more time, I would also look at ..."
- "Does this match what you had in mind?" (মাঝে মাঝে জিজ্ঞেস করুন, interviewer কোন দিকে নিতে চায় বুঝতে)

**Flutter থেকে এলে কী আলাদা:**
- Flutter-এ background কাজ প্রায়ই plugin-এর পেছনে লুকানো থাকে। Native-এ আপনাকে WorkManager, foreground service type, Doze — সরাসরি বলতে হবে।
- Room + Flow মিলে Flutter-এর `drift` + `Stream`-এর কাজ করে। Repository pattern একই।
- Platform channel লাগে না। Camera (CameraX), player (Media3), Keystore সব সরাসরি ব্যবহার করবেন। তাই এগুলোর নাম design-এ সরাসরি বলুন।
- Interviewer native API-এর নাম শুনতে চায় (WorkManager, FCM, Media3, Keystore)। শুধু "a background task" বললে দুর্বল শোনায়।

---

### <a id="d1"></a>D1. ★ Design a security camera app

(Live view of many cameras, motion alerts, cloud + local recordings, playback timeline, sharing with family, security.)

**প্রশ্নটা মানে:** আপনি video streaming, push alert, বড় timeline data আর access control — চারটা কঠিন জিনিস একসাথে ভাবতে পারেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you build an app like Ring or Nest for our cameras?" · "Design the mobile side of a home camera system."

**Diagram:**
```
                    ┌──────────────── Cloud ────────────────┐
 Camera ──RTSP/LAN──┐│ Auth/Users   Device registry  Sharing │
   │  (substream +  ││ Signaling (WebRTC)   TURN relay       │
   │   main stream) ││ Event service ──► FCM push            │
   │                ││ Recording store (HLS segments, S3)    │
   └──WebRTC/TLS────┼┤ Timeline API (segments by time range) │
                    │└──────────────┬────────────────────────┘
                    │               │ HTTPS / WSS
 ┌──────────────── Android app ─────┴──────────────────────┐
 │ Compose UI: Grid · Fullscreen live · Timeline · Events  │
 │ ViewModels (StateFlow)                                  │
 │ Repos: CameraRepo · EventRepo · RecordingRepo · Access  │
 │ Room cache (cameras, events, segments) · DataStore      │
 │ Player: Media3 (RTSP on LAN, HLS for cloud) / WebRTC    │
 │ FCM service → notification with snapshot + deep link    │
 │ Keystore + Tink (tokens) · BiometricPrompt app lock     │
 └─────────────────────────────────────────────────────────┘
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:** জিজ্ঞেস করুন —
- Camera কি নিজেদের তৈরি? (হলে protocol আমরা ঠিক করি; না হলে ONVIF/RTSP।)
- Live view-এ latency কত কম লাগবে? Two-way audio লাগবে?
- Recording কোথায় — cloud, camera-র SD card, নাকি NVR/হাব?
- Sharing-এ কী কী role? Viewer কি recording দেখতে পারে?
- Scope ঠিক করুন: "Live, alerts, timeline, sharing করবো। Camera setup (Wi-Fi provisioning) আর billing বাদ।"

**২. Scale:** ধরি একজন user-এর ১–১৬টা camera। প্রতি camera দিনে ২০–২০০টা motion event। Cloud-এ ৭–৩০ দিন রাখা। এর মানে timeline-এ হাজারো segment — একবারে সব আনা যাবে না, time window ধরে paging লাগবে। Grid-এ ৪–৯টা stream একসাথে — data আর decoder সীমিত।

**৩. Big picture:** উপরের diagram। মূল কথা:
- **Live:** একই LAN-এ থাকলে সরাসরি RTSP (Media3 `RtspMediaSource`)। বাইরে থাকলে WebRTC — P2P চেষ্টা করে, না পারলে TURN relay। কম latency (১ সেকেন্ডের নিচে সম্ভব)।
- **Recording playback:** cloud থেকে HLS (Media3 HLS)। Latency সমস্যা না, seek আর cache সহজ।
- **Alert:** camera motion ধরে → cloud event service → FCM high-priority message → app notification।

**৪. Data & API:**
- Room table: `camera(id, name, status, lastSnapshotUrl, role)`, `event(id, cameraId, startAt, type, thumbUrl, seen)`, `segment(cameraId, startAt, endAt, kind[cloud/local])`।
- API:
  - `GET /cameras`
  - `GET /cameras/{id}/events?from=&to=&cursor=`
  - `GET /cameras/{id}/segments?from=&to=` (timeline)
  - `POST /cameras/{id}/live-session` → WebRTC offer বা signed stream URL
  - `GET /recordings/{segmentId}/playback` → short-lived signed HLS URL
  - `POST /cameras/{id}/shares` {email, role}, `DELETE /shares/{id}`
- Timeline: দেখা অংশ ±১ দিন আনুন, Room-এ cache করুন। Scroll করলে পাশের window আনুন।

**৫. Hard parts:**
- **অনেক camera-র grid:** Grid-এ main stream না, **substream** (কম resolution, কম bitrate)। Fullscreen-এ গেলে main stream। Screen-এর বাইরে যাওয়া tile-এর player release করুন। একসাথে কত decoder চলবে device-ভেদে আলাদা — একটা সীমা রাখুন (যেমন ৪–৬), বাকিগুলোতে শেষ snapshot দেখান। App background-এ গেলে সব stream বন্ধ।
- **Latency vs cost:** WebRTC P2P সস্তা আর দ্রুত, কিন্তু NAT-এর কারণে সব সময় হয় না → TURN relay লাগে, যেটা server bandwidth খায়। HLS সস্তা কিন্তু কয়েক সেকেন্ড দেরি। তাই live = WebRTC, playback = HLS।
- **Alert ঠিক সময়ে পৌঁছানো:** FCM high-priority message Doze-এও আসে, কিন্তু বেশি পাঠালে Android priority কমিয়ে দিতে পারে। তাই message-এ শুধু event id + ছোট data; notification দেখানোর পর thumbnail আনুন। আলাদা notification channel (Person, Motion, Offline)। Android 13+-এ `POST_NOTIFICATIONS` চাইতে হবে। একই camera-র অনেক alert হলে group/throttle করুন।
- **Timeline UI:** হাজারো segment একটা custom Canvas-এ আঁকুন, প্রতিটা segment আলাদা composable না। Zoom level অনুযায়ী segment merge করুন।

**৬. Security, testing, monitoring:**
- **Security (কয়েক layer):**
  - TLS সব জায়গায়। Cleartext বন্ধ (network security config)। Pinning চাইলে backup pin সহ।
  - Access token short-lived; refresh token Tink দিয়ে encrypt করে DataStore-এ; key থাকে Android Keystore-এ।
  - Playback URL signed আর কয়েক মিনিট valid।
  - Sharing-এর সব check server-এ। Revoke করলে সাথে সাথে session বন্ধ।
  - App lock (BiometricPrompt), sensitive screen-এ `FLAG_SECURE` (recent apps-এ live frame না দেখাতে)।
  - Login-এ Play Integrity verdict server-এ verify।
  - LAN-এ camera খুঁজতে (mDNS/ONVIF) API 37 target করলে `ACCESS_LOCAL_NETWORK` runtime permission লাগবে।
  - Log-এ token, video URL বা user data না।
  - চাইলে end-to-end encryption (camera-তে encrypt, শুধু user-এর device-এ decrypt) — তখন cloud-এ AI detection করা যায় না। এটা একটা product trade-off।
- **Testing:** Repository আর timeline-merge logic unit test (fake API, in-memory Room)। Player state ViewModel-এ test। FCM handler-এ fake payload। আসল camera দিয়ে খারাপ network (throttling) test।
- **Monitoring:** time-to-first-frame, stall rate, stream error rate, alert delay (event time → notification time), crash/ANR rate (Play vitals: crash ১.০৯%, ANR ০.৪৭% সীমা)।

**How to say it (English):**
> "Can I ask a few questions first? Are the cameras our own hardware, how low must the live latency be, and where are recordings stored?
> OK, so the scope is live view, motion alerts, recordings with a timeline, and sharing, and I will skip camera setup and billing.
> Let me assume one user has up to 16 cameras and each camera makes up to 200 events a day.
> Let me draw the big picture. The app has Compose screens, ViewModels with StateFlow, repositories, and a Room cache.
> For live view on the same Wi-Fi, I play RTSP directly with Media3. Outside the home, I use WebRTC, with a TURN relay when peer-to-peer fails.
> For recordings, I play HLS from the cloud with short-lived signed URLs.
> For alerts, the camera sends the event to the cloud, and the cloud sends a high-priority FCM message with only the event id.
> The timeline data is big, so I load it by time window, cache it in Room, and draw it on one Canvas.
> The hard part here is the grid of many cameras. I use the low-resolution substream in the grid, limit how many players run at once, and release players that go off screen.
> The trade-off is latency against cost: WebRTC is fast but relay traffic costs money, and HLS is cheap but a few seconds late.
> For sharing, the server checks every role, not the app.
> For security, I keep tokens encrypted with a Keystore key, use TLS everywhere, add an app lock, and verify Play Integrity on the server.
> To test, I unit test repositories and timeline logic with fakes, and I test real cameras on a slow network.
> In production, I watch time to first frame, stall rate, alert delay, and crash and ANR rates."

**Key words:** `substream` · `WebRTC + TURN` · `RtspMediaSource` · `HLS signed URL` · `high-priority FCM` · `timeline paging` · `ACCESS_LOCAL_NETWORK`

**Follow-up:**
- **Q:** The user opens a motion alert but the video is not uploaded yet. What do you show?
  **A:** "I show the snapshot and the event time first, with a 'clip is processing' state. The app listens for the clip to be ready, or retries in a few seconds, and then starts playback. I never show an empty black player."
- **Q:** How do you stop 9 live streams from killing the battery?
  **A:** "I use the substream in the grid, I cap the number of active players, and I show a still snapshot for the rest. When the app goes to the background, I stop every stream. Fullscreen gets the main stream only for the camera the user taps."
- **Q:** A family member's access is removed. What happens on their phone right now?
  **A:** "The server marks the share as revoked and ends their live sessions. Their signed playback URLs expire in minutes. The next API call returns 403, and the app removes that camera from Room and the screen."

**ভুল করবেন না:** grid-এ সব camera-র full HD main stream চালানোর কথা বলবেন না, আর "app-এ role check করবো" বলবেন না — role check সবসময় server-এ।

**আরও দেখুন:** [V3 · IP camera live stream](#v3) · [V4 · Many camera feeds](#v4) · [V9 · Motion alerts](#v9)

---

### <a id="d2"></a>D2. ★ Design an offline-first app that syncs with a server

**প্রশ্নটা মানে:** আপনি জানেন কি না local DB-কে source of truth রেখে, network না থাকলেও app চালু রাখা যায়, আর পরে conflict ছাড়া sync করা যায়।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you make the app work without internet?" · "How would you design sync between Room and the backend?"

**Diagram:**
```
 Compose UI ──events──► ViewModel ──► Repository
      ▲                                │  write: 1) Room row (syncState=PENDING)
      │ Flow<List<Note>>               │         2) Outbox row (op, payload, idempotencyKey)
      │                                │         3) enqueue SyncWorker (unique)
      └──────── Room (source of truth) ◄┘
                     ▲         │
          pull: upsert         │ push: read outbox in order
                     │         ▼
               SyncWorker (WorkManager, NetworkType.CONNECTED, backoff)
                     │   1) PUSH outbox  → POST /changes   (idempotency key)
                     │   2) PULL changes → GET /changes?since=cursor
                     ▼
                 Server (version per record, tombstones, cursor)
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:**
- কোন data offline-এ লিখতে হবে, নাকি শুধু পড়তে?
- একই data কি অনেক device বা অনেক user edit করে? (conflict-এর ঝুঁকি এখান থেকেই)
- কতটা fresh লাগবে — সাথে সাথে, নাকি কয়েক মিনিটে চলবে?
- Delete কি আছে?

**২. Scale:** ধরি user-প্রতি কয়েক হাজার record, দিনে কয়েকশো change। এর মানে পুরো data বারবার আনা যাবে না। **Delta sync** লাগবে (`since=cursor`)।

**৩. Big picture:**
- UI শুধু Room-এর `Flow` দেখে। Network কখনো সরাসরি UI-তে data দেয় না।
- User কিছু লিখলে: Room-এ লেখা হয় সাথে সাথে (UI তখনই update)। সাথে একটা **outbox** row। তারপর `SyncWorker` enqueue হয়।
- `SyncWorker` আগে push (outbox), তারপর pull (server-এর নতুন change)।

**৪. Data & API:**
- Table:
  - `note(id: UUID, title, body, updatedAt, serverVersion, syncState, isDeleted)`
  - `outbox(seq, entityId, op[CREATE/UPDATE/DELETE], payloadJson, idempotencyKey, attempts)`
  - `sync_meta(cursor)`
- ID client-এ তৈরি (UUID)। তাই offline-এ তৈরি record-এরও স্থায়ী id থাকে।
- API:
  - `POST /changes` [ {key, op, entity, baseVersion} ] → প্রতিটার result (ok / conflict + server copy)
  - `GET /changes?since=<cursor>` → changed records + tombstones + newCursor
- Delete মানে **soft delete (tombstone)**। না হলে অন্য device জানবে না যে record মুছে গেছে।

**৫. Hard parts:**
- **Conflict:** দুই device একই record বদলালে।
  - Option ১: **Last-write-wins** (server version দিয়ে)। সহজ, কিন্তু একজনের edit হারায়।
  - Option ২: **Field-level merge** — আলাদা field বদলালে দুটোই রাখো, একই field হলে নিয়ম।
  - Option ৩: User-কে দেখাও ("keep mine / keep theirs")।
  - আমার choice: client `baseVersion` পাঠায়। Server দেখে version মেলে কি না। না মিললে conflict ফেরত দেয়। Note-এর মতো data-তে field merge, বাকিতে last-write-wins। দরকার হলে user-কে দেখানো।
- **Duplicate:** request গেল কিন্তু response হারালো → worker আবার পাঠাবে। তাই প্রতিটা op-এ **idempotency key**। Server একই key দুবার পেলে একবারই apply করে।
- **কখন sync চালাবো:**
  - লেখার পর `enqueueUniqueWork("sync", ExistingWorkPolicy.APPEND_OR_REPLACE, ...)` (বা KEEP + worker শেষে আবার চেক)।
  - App খোলার সময়।
  - `PeriodicWorkRequest` (minimum ১৫ মিনিট)।
  - Server change হলে FCM "tickle" message → sync।
- **Order:** outbox `seq` অনুযায়ী পাঠান। Create-এর আগে update গেলে server ভুল করবে।
- **Migration:** Room schema বদলালে migration লিখুন আর test করুন। Offline data হারানো মানে user-এর data হারানো।

**৬. Security, testing, monitoring:**
- **Security:** sensitive data হলে DB encrypt (যেমন SQLCipher, key Keystore-এ wrap করা)। Token Tink + Keystore দিয়ে encrypt। Logout-এ DB আর outbox মুছুন।
- **Testing:** in-memory Room দিয়ে repository test। `TestListenableWorkerBuilder` দিয়ে worker test। Fake server দিয়ে conflict, duplicate, network fail — প্রতিটার test। `MigrationTestHelper` দিয়ে migration test।
- **Monitoring:** outbox কত বড়, পুরনো pending item-এর বয়স, sync fail rate, conflict rate।

**How to say it (English):**
> "Can I ask a few questions first? Do users edit offline or only read? Can two devices edit the same item? And do we have deletes?
> OK, I assume users edit offline, on more than one device, and we have deletes.
> Let me draw the big picture. Room is the single source of truth. The UI only observes Flows from Room.
> When the user saves, I write to Room right away, so the UI updates at once. In the same transaction, I add a row to an outbox table.
> Then I enqueue a unique WorkManager job with a network constraint and exponential backoff.
> The worker first pushes the outbox in order, then pulls changes from the server with a cursor.
> I create ids on the client as UUIDs, so offline items have a real id from the start.
> Every outbox item has an idempotency key, so a retry never creates a duplicate on the server.
> Deletes are soft deletes, called tombstones, so other devices also learn about them.
> The hard part here is conflicts. I send the base version with each change. If the server version is newer, the server returns a conflict.
> For simple data I use last-write-wins. For notes I merge by field. In rare cases I ask the user.
> The trade-off is simple code against lost edits, so I choose per data type.
> I also sync on app start, every 15 minutes, and when an FCM message says something changed.
> To test, I use an in-memory Room, a fake server, and the WorkManager test tools. I test conflict, retry and migration.
> In production, I watch the outbox size, the age of the oldest pending change, and the sync failure rate."

**Key words:** `single source of truth` · `outbox` · `idempotency key` · `delta sync cursor` · `tombstone` · `baseVersion conflict` · `unique work`

**Follow-up:**
- **Q:** Why not just call the API from the ViewModel and cache the result?
  **A:** "Then the UI has two sources, the network and the cache, and they can disagree. With Room as the only source, the UI is simple and works the same offline and online."
- **Q:** The worker crashes in the middle of the push. What happens?
  **A:** "Outbox rows are deleted only after the server says OK. WorkManager runs the worker again later. Thanks to the idempotency keys, items that already reached the server are not applied twice."
- **Q:** How do you show the user that something is not synced yet?
  **A:** "Each row has a sync state column. The UI shows a small 'pending' or 'failed' mark from that column. For a failed item, I give a retry button."

**ভুল করবেন না:** "conflict হবে না" ধরে নেবেন না, আর delete-কে hard delete বলবেন না — tombstone না থাকলে অন্য device-এ মুছে যাওয়া data ফিরে আসে।

**আরও দেখুন:** [R4 · Repository and offline-first](#r4) · [R7 · Room](#r7) · [C10 · Background work](#c10)

---

### <a id="d3"></a>D3. ◆ Design a chat or real-time messaging feature

**প্রশ্নটা মানে:** real-time connection, message-এর state, offline অবস্থায় পাঠানো, আর app বন্ধ থাকলে push — এগুলো একসাথে মেলাতে পারেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you build WhatsApp-like messaging?" · "Design in-app chat between users and support."

**Diagram:**
```
 Compose Chat UI ◄── Flow<PagingData<Message>> ── Room (messages, conversations)
      │ send                                          ▲          ▲
      ▼                                               │ upsert   │ upsert
 ChatRepository ── insert (state=SENDING, clientId) ──┘          │
      │                                                          │
      ├── WebSocket (OkHttp, app in foreground) ◄──► Chat server ─┤
      │      send / ack(serverId, seq) / new msg / receipts      │
      ├── SendWorker (WorkManager) when socket is down ──────────┘
      └── FCM (app in background) → notify + fetch missed by seq
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:** ১-১ নাকি group? Media (ছবি) আছে? Delivered/read receipt লাগবে? End-to-end encryption? Scope: "১-১ আর ছোট group, text + ছবি, receipt আছে; voice call নেই।"

**২. Scale:** ধরি একজন user-এর একশোর বেশি conversation, conversation-এ হাজারো message। তাই history **Paging 3** দিয়ে, Room থেকে। নতুন message সেকেন্ডের মধ্যে আসতে হবে।

**৩. Big picture:**
- App foreground-এ: একটা **WebSocket** (OkHttp)। ভেতর-বাইরে দুই দিকে message চলে।
- App background-এ: socket বন্ধ। নতুন message আসে **FCM** দিয়ে।
- UI সবসময় Room দেখে। Socket, FCM, API — সব শুধু Room-এ লেখে।

**৪. Data & API:**
- `message(clientId, serverId?, conversationId, senderId, body, createdAt, seq?, state[SENDING/SENT/DELIVERED/READ/FAILED])`
- `conversation(id, lastSeq, unreadCount, lastMessagePreview)`
- Socket event: `send{clientId, convId, body}` → `ack{clientId, serverId, seq}`; `message{...}`; `receipt{serverId, state}`।
- REST: `GET /conversations/{id}/messages?beforeSeq=&limit=` (history), `GET /sync?afterSeq=` (missed)।

**৫. Hard parts:**
- **Message state:** পাঠানোর সময় Room-এ `SENDING` + client-generated `clientId`। Server ack দিলে `serverId` আর `seq` বসে, state `SENT`। অন্য user-এর device পেলে `DELIVERED`, দেখলে `READ`।
- **Duplicate আর order:** retry হলে একই `clientId` যায়, server dedupe করে। Order ঠিক হয় server-এর `seq` দিয়ে, phone-এর ঘড়ি দিয়ে না (phone-এর সময় ভুল হতে পারে)।
- **Offline queue:** socket না থাকলে `SendWorker` (network constraint) pending message REST দিয়ে পাঠায়।
- **Reconnect:** network ফিরলে exponential backoff + jitter দিয়ে reconnect। তারপর `afterSeq=lastSeq` দিয়ে মাঝের missed message আনুন।
- **Push:** FCM-এ পুরো message না, শুধু conversation id আর seq (বা encrypted payload)। App নিজে fetch করে। Notification-এ `MessagingStyle` আর inline reply।
- **Trade-off:** WebSocket বনাম শুধু FCM + poll। WebSocket দ্রুত কিন্তু খোলা রাখলে battery খায় — তাই শুধু foreground-এ। Background-এ socket ধরে রাখতে foreground service চালানো ঠিক না।

**৬. Security, testing, monitoring:**
- **Security:** WSS (TLS)। Socket connect-এ short-lived token। E2E চাইলে Signal protocol-এর মতো library (তখন server message পড়তে পারে না, search server-এ হবে না)। Notification-এ lock screen-এ content লুকানোর option।
- **Testing:** fake socket দিয়ে repository test: ack আসার পর state, duplicate ack, out-of-order message। `MockWebServer` WebSocket support করে।
- **Monitoring:** send→ack সময়, fail হওয়া message rate, reconnect সংখ্যা, push delivery delay।

**How to say it (English):**
> "Can I ask a few questions first? Is it one-to-one or group, do we need read receipts, and do we need end-to-end encryption?
> OK, I will design one-to-one and small groups, with text, images and receipts.
> Let me draw the big picture. The UI reads messages from Room with Paging 3. Room is the source of truth.
> When the app is in the foreground, I keep one WebSocket open with OkHttp. In the background, I close it and new messages come with FCM.
> When the user sends, I insert the message in Room with state 'sending' and a client id. The UI shows it at once.
> The server answers with an ack that has the server id and a sequence number. Then I mark it 'sent'.
> Later, receipts move it to 'delivered' and 'read'.
> I order messages by the server sequence number, not by the phone clock, because the phone clock can be wrong.
> If the socket is down, a WorkManager job sends pending messages when the network comes back.
> The hard part here is not losing or doubling messages. Retries use the same client id, so the server can remove duplicates.
> After a reconnect, I ask for all messages after my last sequence number, so I fill any gap.
> The FCM message carries only ids. The app fetches the content, so there is no private text in the push.
> The trade-off is speed against battery, so I keep the socket open only while the user is in the app.
> I test with a fake socket for acks, duplicates and out-of-order events, and I watch send time and failed sends in production."

**Key words:** `WebSocket` · `clientId dedupe` · `server sequence` · `delivery states` · `offline queue` · `FCM tickle` · `Paging 3`

**Follow-up:**
- **Q:** Why not keep the WebSocket open all the time in a service?
  **A:** "It costs battery, and modern Android limits background services. FCM is made for this case and works in Doze, so I use the socket only in the foreground."
- **Q:** How do you handle a message that fails many times?
  **A:** "After a few attempts I mark it 'failed' and show a retry icon. The user decides. I do not retry forever in the background."

**ভুল করবেন না:** phone-এর timestamp দিয়ে message sort করার কথা বলবেন না — server seq ব্যবহার করুন।

**আরও দেখুন:** [R16 · WebSocket, SSE, MQTT or FCM](#r16) · [C15 · Notifications and push](#c15) · [R11 · Paging 3](#r11)

---

### <a id="d7"></a>D7. ◆ Design an image feed / gallery with caching and pagination

(Infinite scroll grid, full-screen view, fast scrolling, offline first pages, low memory use.)

**প্রশ্নটা মানে:** হাজারো ছবির list কীভাবে smooth scroll করাবেন, memory শেষ না করে, আর network কম খরচ করে — paging আর image cache একসাথে বোঝেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "How would you build an Instagram-like photo feed?" · "Design a gallery screen that shows thousands of images smoothly."

**Diagram:**
```
 Compose: LazyVerticalGrid (key = id) ──► full screen: HorizontalPager + zoom
      ▲ Flow<PagingData<Photo>>
 ViewModel (.cachedIn(viewModelScope))
      ▲
 Pager ── PagingSource from Room ◄── RemoteMediator ── GET /photos?cursor=&limit=30
                  │                       │ REFRESH: clear + insert in one transaction
                  ▼                       ▼ APPEND: insert next page + save nextCursor
           Room: photo(id, sortKey, thumbUrl, fullUrl, width, height) · remote_key(nextCursor)

 Image loading (Coil): memory cache (LRU) → disk cache (app cacheDir) → network/CDN
 Grid asks for the thumbnail size · full screen asks for the full image
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:**
- ছবি কোথা থেকে — server feed, নাকি phone-এর নিজের ছবি (MediaStore)?
- Offline-এ কিছু দেখাতে হবে কি না?
- ছবি private কি না (signed URL লাগবে কি না)?
- Upload এই scope-এ আছে কি না? (না থাকলে বলুন, D5-এ আলাদা।)
- Scope: "server feed, grid, infinite scroll, full-screen view, প্রথম কয়েক page offline। Upload আর edit বাদ।"

**২. Scale:** ধরি feed-এ ১০,০০০+ ছবি। একটা thumbnail ৩০–৮০ KB, full ছবি ১–৫ MB। Screen-এ একসাথে ২০–৩০টা cell, user দ্রুত fling করে। এর মানে: সব একবারে আনা যাবে না (paging লাগবে), আর grid-এ কখনো full ছবি নামানো যাবে না।

**৩. Big picture:**
- **Paging 3 + RemoteMediator:** network page আনে → Room-এ লেখে → UI Room থেকে পড়ে। Room source of truth, তাই offline-এও আগের page দেখা যায়।
- **Image loader: Coil** (Compose-first, coroutine দিয়ে বানানো)। এর নিজের memory cache আর disk cache আছে। নিজে image cache লিখবেন না।
- **Server ছবির কয়েকটা size দেয়** (বা CDN-এ width parameter)। Grid ছোট size চায়, full screen বড়।

**৪. Data & API:**
- API: `GET /photos?cursor=<c>&limit=30` → `{items: [{id, thumbUrl, fullUrl, width, height}], nextCursor}`
- Room: `photo(id, sortKey, thumbUrl, fullUrl, width, height)`, `remote_key(nextCursor)`।
- **Offset না, cursor।** Offset দিলে মাঝে নতুন ছবি এলে সব সরে যায়। তখন একই ছবি দুবার আসে বা কিছু বাদ পড়ে।
- `width` আর `height` API থেকে নিন। এতে ছবি load হওয়ার আগেই cell-এর ঠিক aspect ratio জানা যায়।

**৫. Hard parts:**
- **Memory (OOM):** Bitmap-এর memory = width × height × 4 byte। একটা 4000×3000 ছবি ≈ ৪৮ MB। তাই decode করুন cell-এর size-এ। Coil composable-এর size দেখে নিজেই ছোট করে decode করে। Server-ও ছোট thumbnail দিক — এতে network আর decode দুটোই কমে।
- **Cache-এর layer:**
  - Memory cache (LRU) — scroll করে ফিরে এলে সাথে সাথে দেখায়।
  - Disk cache — app বন্ধ করে খুললেও network লাগে না।
  - Room — list-এর data (কোন ছবি, কোন ক্রমে)।
- **Smooth scroll:**
  - `LazyVerticalGrid`-এ stable `key = id`।
  - Cell-এর size আগে থেকে ঠিক (aspect ratio দিয়ে)। তাই ছবি এলে layout লাফায় না।
  - Placeholder আর ছোট crossfade।
  - Cell screen থেকে বের হলে Coil request cancel করে।
  - Paging-এর `prefetchDistance` দিয়ে শেষে পৌঁছানোর আগেই পরের page আনুন।
- **Full screen:** `HorizontalPager` + zoom। বড় ছবি load হওয়ার সময় memory cache-এর thumbnail-টা placeholder হিসেবে দেখান। তাই খালি screen আসে না।
- **Refresh:** RemoteMediator-এর REFRESH-এ পুরনো row মুছে নতুন page লেখা — একটা transaction-এ। না হলে list কিছুক্ষণ খালি দেখায়।

**৬. Security, testing, monitoring:**
- **Security:**
  - Private ছবি হলে short-lived signed URL। কিন্তু URL প্রতিবার বদলায়, তাই cache key হবে ছবির `id`, URL না। Coil-এ `memoryCacheKey` আর `diskCacheKey` দিয়ে এটা করা যায়।
  - Disk cache app-এর private `cacheDir`-এ। Logout-এ cache আর Room মুছুন।
  - TLS সব জায়গায়।
- **Testing:**
  - RemoteMediator test: in-memory Room + fake API (REFRESH, APPEND, error, শেষ page)।
  - Paging-এর `paging-testing` library-র `asSnapshot()` দিয়ে ViewModel-এর paging flow test।
  - Macrobenchmark দিয়ে scroll-এর jank মাপুন।
- **Monitoring:** প্রথম ছবি দেখাতে কত সময়, image load fail rate, cache hit rate, feed screen-এ jank %, OOM crash।

**How to say it (English):**
> "Can I ask a few questions first? Do the photos come from our server or from the phone? Do we need offline support, and are the photos private?
> OK, I will design a server feed with a grid, infinite scroll, a full-screen view, and the first pages offline. I will skip upload.
> Let me assume ten thousand photos or more, and twenty to thirty cells on screen at once.
> Let me draw the big picture. I use Paging 3 with a RemoteMediator. It loads pages from the API and writes them to Room. The grid reads from Room, so Room is the source of truth.
> The API uses a cursor, not an offset, so new photos do not create duplicates.
> The API also gives width and height, so each cell has the right size before the image loads, and the layout does not jump.
> For images I use Coil. It has a memory cache and a disk cache, and it decodes each image at the size of the cell.
> The hard part here is memory. A full photo can take about 48 MB as a bitmap, so the grid only loads small thumbnails. Full size is only for the full-screen view.
> If the URLs are signed, I use the photo id as the cache key, because the URL changes every time.
> I test the RemoteMediator with an in-memory Room and a fake API, and I measure scroll jank with Macrobenchmark.
> In production, I watch image load time, failure rate and OOM crashes."

**Key words:** `Paging 3 + RemoteMediator` · `cursor pagination` · `Coil memory + disk cache` · `decode at view size` · `stable keys` · `aspect ratio placeholder` · `cache key by id`

**Follow-up:**
- **Q:** Why a cursor and not page numbers?
  **A:** "With page numbers, a new photo at the top shifts every item. Then the next page repeats or skips items. A cursor points to an exact place in the list, so pages stay correct."
- **Q:** The user flings very fast and sees empty cells. What do you do?
  **A:** "I make sure the grid uses small thumbnails and the right decode size. I increase the prefetch distance and show a light placeholder color. I also check with a profiler that nothing heavy runs on the main thread."
- **Q:** Glide or Coil?
  **A:** "For a Compose app I pick Coil, because it is built on coroutines and has a good Compose API. Glide is also fine, and it is common in older View-based apps. Both have memory and disk caches."

**ভুল করবেন না:** grid-এ full-size ছবি load করার কথা বলবেন না, আর নিজের image cache লেখার কথা বলবেন না — Coil/Glide এটা ভালোভাবে করে। Signed URL-কে cache key বানালে cache কখনো কাজে লাগে না।

**আরও দেখুন:** [R11 · Paging 3](#r11) · [R12 · Coil or Glide](#r12) · [U6 · Fast LazyColumn](#u6)

---

### <a id="d4"></a>D4. ◆ Design software for a fleet of custom Android devices

(Kiosk, OTA updates, remote config, logs and crash upload, device health, remote commands, security.)

**প্রশ্নটা মানে:** আপনি phone app-এর বাইরে ভাবতে পারেন কি না — হাজারো device যেগুলো কেউ হাতে ধরে ঠিক করবে না, সেগুলো দূর থেকে নিরাপদে চালানো আর update করা।
**অন্যভাবেও জিজ্ঞেস করে:** "We ship our own Android-based devices. How do you manage them remotely?" · "Design an MDM-like system for our kiosks or cameras."

**Diagram:**
```
 ┌──────────────────── Device (custom AOSP build, user variant) ─────────────────┐
 │ Kiosk launcher app (HOME) + lock task mode                                    │
 │ Agent app (privileged / platform-signed, or Device Owner)                     │
 │   ├─ Command client (MQTT over TLS, mutual TLS) ◄── commands / config        │
 │   ├─ Config store (signed JSON, version) → apply                             │
 │   ├─ Health reporter (heartbeat: battery, temp, storage, net, uptime)        │
 │   ├─ Log/crash collector (rotating files, ApplicationExitInfo, tombstones)   │
 │   ├─ App updater (PackageInstaller session)                                  │
 │   └─ OS updater (UpdateEngine, A/B or virtual A/B)                           │
 │ Device identity key in Keystore/StrongBox + key attestation                   │
 └────────────────────────────────────┬──────────────────────────────────────────┘
                                      │ mTLS
 ┌─────────────────────── Fleet backend ──────────────────────────────────────────┐
 │ Provisioning · Device registry · MQTT broker · Config service · Command queue │
 │ OTA server (signed packages, staged rollout) · Log store · Dashboard/alerts  │
 └────────────────────────────────────────────────────────────────────────────────┘
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:**
- Device-এ কি **GMS (Google Play services)** আছে? Custom AOSP device-এ প্রায়ই থাকে না। তাহলে FCM, Play Integrity, Android Management API — এগুলো নেই। নিজের push আর নিজের attestation লাগবে।
- OS কি আমরাই build করি? করলে আমাদের app platform key দিয়ে sign করা privileged app হতে পারে। না করলে Device Owner (DPC) পথে যেতে হবে।
- কত device? কোথায় থাকে (দোকান, রাস্তায়, বাড়িতে)? Network কেমন (Wi-Fi, LTE, মাঝে মাঝে বন্ধ)?
- Scope: kiosk, OTA (OS + app), config, command, log, health।

**২. Scale:** ধরি ১০,০০০ device। প্রতি device প্রতি ৫ মিনিটে heartbeat → সেকেন্ডে প্রায় ৩৩টা message। ঠিক আছে। কিন্তু সব device একসাথে OTA নামালে server আর network চাপে পড়বে → **staged rollout** লাগবে।

**৩. Big picture:**
- **Kiosk:** আমাদের app HOME launcher। **Lock task mode** দিয়ে user অন্য app-এ যেতে পারে না। Device Owner হলে `setLockTaskPackages`, `setStatusBarDisabled`, `setKeyguardDisabled` দিয়ে status bar, lock screen বন্ধ। নিজের OS হলে system UI build থেকেই সরিয়ে দেওয়া যায়।
- **Agent app:** সব remote কাজ এক জায়গায়। Boot-এ চালু হয়। Privileged হলে বেশিরভাগ সীমা থাকে না, তবে privileged permission-এর জন্য `privapp-permissions` XML allowlist লাগে।
- **Command channel:** GMS না থাকলে **MQTT over TLS** (persistent connection, কম data)। GMS থাকলে FCM শুধু "wake up" হিসেবে, আসল command server থেকে টেনে আনা।

**৪. Data & API:**
- **Config:** `{version, payload, signature}`। Device শুধু নতুন version নেয়, signature verify করে, তারপর apply। Apply ব্যর্থ হলে আগের version-এ ফেরে। Device reported config version server-এ পাঠায়।
- **Command:** `{commandId, type, args, expiresAt, signature}`। শুধু allowlist-এ থাকা type চলে (`REBOOT`, `UPLOAD_LOGS`, `SET_CONFIG`, `INSTALL_APP`, `CLEAR_APP_DATA`)। কোনো "shell command চালাও" না। Device ack দেয়: received → done/failed। একই `commandId` দুবার এলে একবারই চলে।
- **Health heartbeat:** battery, charging, temperature, free storage, RAM, uptime, network type/signal, app version, OS build, security patch level, last error।
- **Logs:** device-এ rotating file (সীমিত size)। Server চাইলে বা দিনে একবার compress করে upload। Crash: নিজের `UncaughtExceptionHandler` + পরের চালুতে `ActivityManager.getHistoricalProcessExitReasons()` (`ApplicationExitInfo`, API 30+) দিয়ে ANR/native crash-এর কারণ। নিজের OS হলে tombstone আর dropbox-ও তোলা যায়।

**৫. Hard parts:**
- **OS OTA নিরাপদে:**
  - **A/B (বা virtual A/B)** update। Device চালু অবস্থায় অন্য slot-এ install হয়। Reboot করে নতুন slot। Boot ব্যর্থ হলে bootloader আগের slot-এ ফেরে। তাই device "brick" হয় না।
  - Privileged updater app system API `UpdateEngine` দিয়ে payload apply করে (এটা public SDK API না; system/platform app লাগে)।
  - OTA package build key দিয়ে sign। Device শুধু আমাদের key-এর package নেয়।
  - **Staged rollout:** ১% → ১০% → ১০০%। প্রতিটা ধাপে health metric দেখে এগোনো। খারাপ হলে থামানো।
  - শুধু নির্দিষ্ট সময়ে install (যেমন রাতে), charging-এ বা battery বেশি থাকলে।
  - Device Owner পথে থাকলে `setSystemUpdatePolicy()` দিয়ে কখন update হবে ঠিক করা যায় (freeze period সীমিত — চিরদিন আটকানো যায় না)।
- **App update:** `PackageInstaller` session। Device Owner বা privileged app user prompt ছাড়া install করতে পারে। নতুন APK-এর signature মিলতে হবে।
- **Device offline:** command-এ `expiresAt`। Device ফিরলে pending command টেনে আনে। মেয়াদ শেষ হলে চলে না।
- **Trade-off:** MQTT সারাক্ষণ connect রাখা দ্রুত কিন্তু battery/data খরচ। Mains power-এর device-এ ঠিক আছে। Battery device-এ লম্বা keep-alive বা poll।

**৬. Security, testing, monitoring:**
- **Security (কয়েক layer):**
  - **Device identity:** প্রতিটা device-এর নিজের key pair, Keystore-এ (StrongBox থাকলে সেখানে)। **Key attestation** দিয়ে server যাচাই করে key আসল hardware-এ, আর verified boot ঠিক আছে।
  - **mTLS:** device আর server দুই দিকেই certificate দেখায়।
  - **Signed everything:** config, command, OTA, APK — সব sign করা। Device verify করে।
  - **OS hardening:** `user` build (userdebug/eng না), adb বন্ধ বা শুধু factory-তে, verified boot + locked bootloader, SELinux enforcing, অপ্রয়োজনীয় app/service build থেকে বাদ।
  - **Least privilege:** agent শুধু দরকারি privileged permission পায়। Remote command allowlist।
  - **Security patch:** monthly patch merge করে OTA দিয়ে পাঠানো। Patch level heartbeat-এ রিপোর্ট।
- **Testing:** command handler আর config apply-এর unit test (bad signature, expired command, duplicate)। OTA: lab-এ device-এ upgrade, rollback, মাঝপথে power cut test। Staged rollout নিজেই একটা production test।
- **Monitoring:** online device %, OTA success/rollback rate, crash/ANR per build, heartbeat-এ temperature/storage alert, last-seen পুরনো device-এর list।

**How to say it (English):**
> "Can I ask a few questions first? Do the devices have Google Play services? Do we build the OS ourselves? How many devices, and what network do they have?
> I will assume we build our own AOSP image, there is no GMS, and we have about ten thousand devices.
> Let me draw the big picture. On the device, a kiosk launcher runs in lock task mode, and a privileged agent app does all remote work.
> The agent keeps an MQTT connection over mutual TLS to our backend. That is how commands and config arrive.
> Config is versioned and signed. The device checks the signature, applies it, and rolls back if it fails.
> Commands come from a small allowlist, like reboot or upload logs. Each has an id and an expiry, and the device sends an ack.
> Every few minutes the agent sends a heartbeat with battery, temperature, storage, network, versions and patch level.
> Logs go to rotating files and are uploaded in batches. For crashes, I also read ApplicationExitInfo on the next start.
> The hard part here is OS updates. I use A/B updates, so if the new image does not boot, the device goes back to the old slot.
> The updater uses UpdateEngine, and we only accept OTA packages signed with our key.
> I roll out in stages, like one percent, then ten, then everyone, and I stop if health metrics get worse.
> For security, each device has a key in the Keystore with key attestation, we ship a user build with adb off and SELinux enforcing, and everything we send is signed.
> To test, I unit test command and config handling, and in the lab I test upgrade, rollback and power loss during an update.
> In production, I watch online devices, OTA success and rollback rate, and crashes per build."

**Key words:** `lock task mode` · `Device Owner / privileged app` · `MQTT over mTLS` · `A/B OTA + UpdateEngine` · `staged rollout` · `key attestation` · `signed config and commands`

**Follow-up:**
- **Q:** What if a device has no network for a week?
  **A:** "It keeps working with its last good config. Commands have an expiry, so old ones do not run. When it comes back, it sends a heartbeat, pulls pending commands, and uploads the logs it kept, within a size limit."
- **Q:** How do you stop someone from sending a fake command to a device?
  **A:** "The connection uses mutual TLS, so only our server can talk to it. On top of that, each command is signed, and the device only runs commands from a fixed allowlist."
- **Q:** If the devices did have Google Play services, what would you change?
  **A:** "I could use Android Management API or a Device Owner app for kiosk and policy, FCM to wake devices, and Play Integrity for checks. I would still keep signed config and staged rollout."

**ভুল করবেন না:** ধরে নেবেন না যে custom device-এ FCM/Play services আছে — প্রথমেই জিজ্ঞেস করুন। আর OTA-র কথা বললে rollback (A/B) অবশ্যই বলুন।

**আরও দেখুন:** [O9 · Kiosk devices](#o9) · [O10 · OTA updates](#o10) · [S13 · Android Enterprise](#s13)

---

### <a id="d5"></a>D5. ◆ Design a large video/photo upload that survives app kill and bad network

**প্রশ্নটা মানে:** বড় file upload-কে আপনি "একটা POST call" ভাবেন, নাকি chunk, resume, background limit আর notification — সব জানেন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you upload a 2 GB video reliably?" · "The upload restarts from zero when the app is killed. How would you fix it?"

**Diagram:**
```
 Photo Picker ─► uri ─► UploadRepository
                         │ 1) Room: upload(id, uri, size, sessionUrl?, offset=0, state=QUEUED)
                         │ 2) enqueueUniqueWork("upload-<id>", KEEP)
                         ▼
             UploadWorker (CoroutineWorker, network constraint, backoff)
                 │ setForeground(progress notification, type=dataSync)
                 │ a) no session? → POST /uploads {size, sha256, mime} → sessionUrl
                 │ b) ask server offset → HEAD/GET sessionUrl → offset
                 │ c) loop: read chunk [offset, offset+8MB) → PUT with Content-Range
                 │          save new offset in Room after each OK
                 │ d) finalize → POST /uploads/{id}/complete → mediaId
                 ▼
             Server (resumable session: tus / S3 multipart / GCS resumable)
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:** file কত বড় (MB নাকি GB)? Upload আগে compress/transcode করতে হবে? Mobile data-তে চলবে নাকি শুধু Wi-Fi? একসাথে কয়টা file? Server কোন resumable protocol সাপোর্ট করে?

**২. Scale:** ধরি ২ GB পর্যন্ত video, খারাপ network-এ ১ Mbps → কয়েক ঘণ্টা লাগতে পারে। মানে app kill, network switch, phone restart — সব মাঝপথে হবে। তাই প্রতিবার শুরু থেকে পাঠানো চলবে না।

**৩. Big picture:**
- File বাছাই **Photo Picker** দিয়ে। এতে `READ_MEDIA_VIDEO` permission লাগে না (Play policy-ও এটাই চায়)।
- URI পরে worker-এ পড়তে হবে। তাই হয় persistable URI permission নিন, নয়তো file app-এর নিজের storage-এ copy করুন। Copy নিরাপদ কিন্তু storage দ্বিগুণ লাগে — বড় video-তে সাবধানে।
- প্রতিটা file-এর জন্য একটা unique WorkManager job। State Room-এ।

**৪. Data & API:**
- Room: `upload(id, uri, size, sha256, sessionUrl, offset, state[QUEUED/UPLOADING/PAUSED/DONE/FAILED], attempts, mediaId)`
- API (resumable):
  - `POST /uploads` → session URL/uploadId
  - `HEAD <session>` → server-এ কত byte আছে
  - `PUT/PATCH <session>` chunk + offset
  - `POST complete` → server checksum মেলায়
- Standard protocol ব্যবহার করুন — **tus**, **S3 multipart**, বা **GCS resumable upload**। নিজে নতুন protocol বানাবেন না।

**৫. Hard parts:**
- **Resume ঠিক জায়গা থেকে:** প্রতিটা chunk শেষে offset Room-এ লিখুন। কিন্তু **আসল সত্য server-এর offset**। Resume-এর সময় আগে server-কে জিজ্ঞেস করুন। কারণ chunk হয়তো server-এ পৌঁছেছে কিন্তু response হারিয়েছে।
- **Chunk size:** ছোট (১ MB) হলে request বেশি, overhead বেশি। বড় (৫০ MB) হলে fail হলে অনেক আবার পাঠাতে হয়। ৫–১০ MB মাঝামাঝি। Network ভালো হলে বাড়ানো যায়।
- **App kill / background:**
  - Worker `setForeground()` দিয়ে progress notification দেখায়, foreground service type `dataSync` (manifest-এ `FOREGROUND_SERVICE_DATA_SYNC` permission + WorkManager-এর `SystemForegroundService`-এ type দিতে হবে)।
  - Android 15+-এ `dataSync` দিনে মোট ৬ ঘণ্টার সীমা। তাই resume design-টাই আসল নিরাপত্তা — সময় শেষ হলে থামবে, পরে আবার চলবে।
  - Android 14+-এ **user-initiated data transfer (UIDT) job** আছে: `JobInfo.Builder.setUserInitiated(true)` + `RUN_USER_INITIATED_JOBS`। User নিজে শুরু করা বড় transfer-এর জন্য বানানো, notification লাগে, লম্বা চলতে পারে। Official docs অনুযায়ী কোনো Jetpack library (WorkManager-ও) এটা সাপোর্ট করে না। তাই Android 14+-এ সরাসরি JobScheduler, আর পুরনো version-এ WorkManager + foreground দিয়ে চালান। (নতুন WorkManager release notes একবার দেখে নিন।)
- **Network:** `NetworkType.CONNECTED` (বা Wi-Fi-only setting থাকলে `UNMETERED`)। Network switch-এ request ব্যর্থ হয় → `Result.retry()` + exponential backoff। Server-এর 4xx (যেমন file বাতিল) হলে retry না, `FAILED`।
- **Memory:** পুরো file memory-তে না। `ContentResolver.openInputStream` থেকে chunk পড়ে stream করুন (OkHttp-এ custom `RequestBody`)।
- **Compression:** আগে video ছোট করতে Media3 Transformer দিয়ে transcode। এতে upload ছোট, কিন্তু CPU আর battery খায়, আর এটাও kill হতে পারে — এটাকে আলাদা resumable ধাপ রাখুন।

**৬. Security, testing, monitoring:**
- **Security:** HTTPS; session URL short-lived আর এই user-এর সাথে বাঁধা; checksum (SHA-256) দিয়ে server integrity যাচাই; upload-এর আগে EXIF-এ location থাকলে user-কে জানানো বা সরানো।
- **Testing:** fake server দিয়ে: মাঝপথে fail, response হারানো (server offset বেশি), 4xx, 5xx। `TestListenableWorkerBuilder` দিয়ে worker test। আসল device-এ airplane mode চালু/বন্ধ আর `adb shell am kill` দিয়ে kill test।
- **Monitoring:** upload success rate, গড় সময়, কতবার resume হলো, fail-এর কারণ (network, 4xx, timeout)।

**How to say it (English):**
> "Can I ask a few questions first? How big are the files, can we upload on mobile data, and does the server support resumable upload?
> I will assume videos up to 2 GB, on any network, and a resumable protocol like tus or S3 multipart.
> Let me draw the big picture. The user picks the file with the Photo Picker, so we do not need the media read permission.
> I save an upload row in Room with the uri, size, checksum and state. Then I enqueue a unique WorkManager job for that file.
> The worker first creates an upload session on the server and saves the session URL in Room.
> Then it asks the server how many bytes it already has, and sends the file in chunks of about 8 MB from that point.
> After each chunk, I save the new offset. But the server offset is the real truth, so on every resume I ask the server first.
> The hard part here is surviving app kill and long uploads. The worker calls setForeground with a progress notification, using the dataSync type.
> On Android 15, dataSync has a 6-hour daily limit, so resume is my real safety net. On Android 14 and up, a user-initiated data transfer job is also a good option.
> If the network drops, I return retry with exponential backoff. If the server says the file is not allowed, I stop and mark it failed.
> I stream each chunk from the content resolver, so I never load the whole file in memory.
> The trade-off in chunk size is fewer requests against less re-sending after a failure, so I pick the middle.
> At the end the server checks the SHA-256, so we know the file is complete.
> I test with a fake server for lost responses and errors, and on a device with airplane mode and process kill."

**Key words:** `resumable upload` · `chunk + offset` · `server offset is truth` · `setForeground dataSync` · `UIDT job` · `Photo Picker` · `checksum`

**Follow-up:**
- **Q:** Why ask the server for the offset if you already saved it locally?
  **A:** "Because a chunk can reach the server while the response is lost. Then my local offset is behind. Asking the server first avoids sending wrong bytes."
- **Q:** The user uploads 20 photos at once. One job or 20 jobs?
  **A:** "I keep one row per file and one unique job per file, but I limit how many run in parallel, maybe two or three. One bad file then does not block the others, and I can show progress per file."
- **Q:** What happens after the phone restarts?
  **A:** "WorkManager keeps its jobs across reboot and runs them again. The worker reads the session from Room, asks the server for the offset, and continues."

**ভুল করবেন না:** "একটা foreground service-এ পুরো file এক request-এ পাঠাবো" বলবেন না — Android 15-এর ৬ ঘণ্টা সীমা আর network fail দুটোতেই এটা ভেঙে যায়।

**আরও দেখুন:** [C7 · Foreground services](#c7) · [C10 · Background work](#c10) · [L11 · Retry with backoff](#l11)

---

### <a id="d6"></a>D6. ◆ Design a sensor data logger

(High-rate data, batching, local buffer, compression, upload, battery.)

**প্রশ্নটা মানে:** আপনি জানেন কি না সেকেন্ডে শত শত sample data কীভাবে না হারিয়ে, battery না খেয়ে, phone/device-এ জমিয়ে server-এ পাঠানো যায়।
**অন্যভাবেও জিজ্ঞেস করে:** "We record accelerometer and gyro data all day. How would you build it?" · "Design data collection from our sensors to the cloud."

**Diagram:**
```
 SensorManager ──(samplingPeriodUs, maxReportLatencyUs = HW batching)──►
   SensorEventListener on a HandlerThread
      │ copy values + event.timestamp (ns) into a ring buffer / Channel
      ▼
   Writer coroutine (single thread)
      │ every 1 s or N samples: append binary records to current segment file
      │ every 1 min or 5 MB: close segment → compress (gzip) → mark READY in Room
      ▼
   files/segments/*.bin.gz  +  Room: segment(id, start, end, count, sha256, state)
      │
   UploadWorker (WorkManager: unmetered + charging, or every 15 min)
      │ POST segment (idempotent by segment id) → on 200: delete file, mark DONE
      ▼
   Ingest server → time-series store
 (Long-running capture runs in a foreground service, or as a system service on our own OS)
```

**ধাপে ধাপে (Bangla walk-through):**

**১. Clarify:**
- কোন sensor, কত Hz? (accelerometer ১০০ Hz নাকি ১ kHz?)
- কতক্ষণ — কয়েক মিনিট, নাকি সারাদিন background-এ?
- Data কত দ্রুত server-এ লাগবে — real-time, নাকি কয়েক ঘণ্টা দেরিতে চলবে?
- Phone নাকি আমাদের নিজের device (নিজের OS)? External sensor (BLE) নাকি built-in?
- Data হারানো কতটা সহ্য হয়?

**২. Scale:** ধরি ৩টা sensor × ২০০ Hz × ৩ axis × ৪ byte float + ৮ byte timestamp ≈ প্রতি sample ~২০ byte → সেকেন্ডে ~১২ KB → ঘণ্টায় ~৪৩ MB, দিনে ~১ GB (compress-এর আগে)। এই সংখ্যা থেকেই সিদ্ধান্ত: প্রতি sample-এ Room-এ একটা row রাখা যাবে না; binary file + compression লাগবে; upload batch-এ।

**৩. Big picture:**
- **Capture:** `SensorManager.registerListener(listener, sensor, samplingPeriodUs, maxReportLatencyUs, handler)`। `maxReportLatencyUs` দিলে sensor hardware FIFO-তে জমিয়ে একসাথে দেয় — CPU কম জাগে, battery বাঁচে। Callback একটা আলাদা `HandlerThread`-এ, main thread-এ না।
- **Buffer:** callback-এ ভারী কাজ না। শুধু value copy করে ring buffer বা `Channel`-এ দিন। `SensorEvent` object system আবার ব্যবহার করতে পারে, তাই reference রাখবেন না — value copy করুন।
- **Write:** একটা writer coroutine batch করে append-only file-এ binary লেখে। Segment file নির্দিষ্ট সময়/size-এ বন্ধ, compress, Room-এ metadata।
- **Upload:** WorkManager, constraint দিয়ে। সফল হলে file মুছে দিন।

**৪. Data & API:**
- Segment file format: header (deviceId, sensor type, sample rate, boot-time→wall-clock offset, format version) + fixed-size binary records। চাইলে Protobuf।
- `SensorEvent.timestamp` nanosecond-এ, আর সাধারণত `SystemClock.elapsedRealtimeNanos()`-এর একই base (boot থেকে)। প্রতি segment-এর header-এ একবার wall-clock-এর সাথে mapping রাখুন। প্রতি sample-এ `System.currentTimeMillis()` নেবেন না — user ঘড়ি বদলালে data ভুল হয়।
- Room: `segment(id, sensor, startNs, endNs, sampleCount, bytes, sha256, state[OPEN/READY/UPLOADED])`।
- API: `POST /segments/{segmentId}` (body = compressed file)। একই id আবার এলে server ignore করে (idempotent)।

**৫. Hard parts:**
- **Background-এ sensor:** Android 9+-এ background app accelerometer/gyro-র মতো continuous sensor-এর event পায় না। তাই লম্বা logging মানে **foreground service** আর চলমান notification। Type বাছাই use case অনুযায়ী (fitness হলে `health`, BLE sensor হলে `connectedDevice`, না হলে `specialUse`)। কোনটা ঠিক মিলবে, official foreground service types page-এ মিলিয়ে নিন। নিজের OS-এর device হলে এটা boot-এ চালু system service বা privileged app হতে পারে।
- **High rate:** ২০০ Hz-এর বেশি চাইলে `HIGH_SAMPLING_RATE_SENSORS` permission (Android 12+)। Device সত্যি কত Hz দেয় তা `sensor.minDelay` আর আসল timestamp দেখে মাপুন।
- **Battery:**
  - Hardware batching (`maxReportLatencyUs`) → CPU কম জাগে।
  - Disk-এ লেখা batch-এ (প্রতি sample-এ না)।
  - Upload শুধু charging + unmetered-এ (দরকার হলে urgent data আলাদা)।
  - Wake lock কম সময়ের জন্য। Screen বন্ধে CPU ঘুমালে non-wakeup sensor-এর FIFO ভরে গেলে data হারাতে পারে — তাই wakeup sensor বা partial wake lock ব্যবহারের কথা ভাবুন। তবে এতে battery বেশি খরচ হয়।
- **Data হারানো vs performance:** প্রতি কয়েক সেকেন্ডে flush করুন। Crash হলে শেষ কয়েক সেকেন্ড হারাতে পারে — এটা মেনে নেওয়া trade-off। প্রতি record-এ `fsync` করলে disk আর battery খরচ অনেক।
- **Storage full:** সর্বোচ্চ size রাখুন (যেমন ২ GB)। ভরে গেলে সবচেয়ে পুরনো uploaded/বা পুরনো segment মুছুন, আর metric পাঠান।
- **Compression:** gzip সব জায়গায় আছে, সহজ। Sensor data-তে আগে delta encoding করলে compression অনেক ভালো হয়। CPU vs size trade-off।

**৬. Security, testing, monitoring:**
- **Security:** sensor data user-এর আচরণ (চলাফেরা, অবস্থান) প্রকাশ করতে পারে। তাই file app-private storage-এ। দরকারে file encrypt (Tink, key Keystore-এ)। Upload HTTPS + device/user token। Server-এ শুধু দরকারি data।
- **Testing:** writer আর segment rotation-এর unit test (fake clock, fake sensor event)। File format reader/writer round-trip test। Upload worker test (fail, retry, duplicate)। আসল device-এ: কয়েক ঘণ্টা চালিয়ে battery আর dropped sample মাপা।
- **Monitoring:** expected vs actual sample count (gap ধরতে), pending data size, upload delay, battery drain per hour, foreground service কতবার বন্ধ হলো।

**How to say it (English):**
> "Can I ask a few questions first? Which sensors and at what rate, for how long, and how fast does the server need the data?
> I will assume three sensors at 200 Hz, all day, and the server can wait a few hours.
> Let me do quick math. That is about 12 KB per second, so around 1 GB per day before compression. So I cannot store one Room row per sample.
> Let me draw the big picture. I register the sensors with a sampling period and a max report latency. The sensor hub then batches events in hardware, and the CPU wakes up less.
> The callback runs on a HandlerThread. It only copies the values and the timestamp into a buffer.
> A single writer coroutine appends binary records to a segment file. Every minute, it closes the file, compresses it, and saves its metadata in Room.
> A WorkManager job uploads ready segments when the device is charging and on Wi-Fi. Each upload uses the segment id, so retries are safe. After the server says OK, I delete the file.
> The hard part here is running for a long time. Since Android 9, background apps do not get these sensor events, so I need a foreground service with a notification. On our own OS, it can be a system service.
> For timestamps, I use the sensor event time, which counts from boot. I map it to wall clock once per file, not per sample.
> The trade-off is data safety against battery. I flush every few seconds, so a crash may lose a few seconds of data, but I do not write to disk for every sample.
> I also cap the storage and drop the oldest data if the disk is full.
> I test the writer and file format with a fake clock and fake events, and I run long tests on real devices to measure battery and dropped samples.
> In production, I compare expected and real sample counts to find gaps."

**Key words:** `maxReportLatencyUs` · `hardware FIFO batching` · `HandlerThread` · `segment files` · `elapsedRealtimeNanos` · `foreground service` · `HIGH_SAMPLING_RATE_SENSORS`

**Follow-up:**
- **Q:** Why not save each sample in Room?
  **A:** "At hundreds of samples per second, one insert per sample costs too much CPU and battery, and the database grows fast. Append-only binary files with batches are much cheaper. I keep only the file metadata in Room."
- **Q:** How do you know if you lost data?
  **A:** "I know the sample rate, so I can compute the expected count per segment. I compare it with the real count and look for big gaps between timestamps. I send this as a metric."
- **Q:** The sensor is an external BLE device, not built in. What changes?
  **A:** "Capture moves to a BLE connection with the BLUETOOTH_CONNECT permission and a connectedDevice foreground service. The device itself should batch samples into bigger packets. The buffer, files and upload part stay the same."

**ভুল করবেন না:** sensor callback-এর ভেতরে disk-এ লেখা বা network call করবেন না, আর প্রতি sample-এ wall-clock time নেবেন না।

**আরও দেখুন:** [N3 · Sensors and battery](#n3) · [N4 · Sensors in the background](#n4) · [N5 · Noisy sensor data](#n5)

---


## <a id="part-12"></a>Part 12 — Live coding round

Live coding-এ তারা দেখে আপনি চাপের মধ্যে পরিষ্কার Kotlin লিখতে পারেন কি না, আর জোরে ভাবতে পারেন কি না। কঠিন algorithm কম আসে। বেশি আসে ছোট problem আর Android-এর রোজকার কাজ (Flow, ViewModel, Compose, coroutine)।
English দুর্বল হলেও চলবে, যদি চুপ করে না থাকেন। নিচের phrase-গুলো মুখস্থ রাখলে কথা থামবে না।

### আগে বুঝুন — live coding round কীভাবে চলে

**সাধারণ ক্রম (৪৫–৬০ মিনিট):**
```
1. Read + clarify (2–4 min)  → input কী, output কী, edge case কী
2. Example (1–2 min)          → একটা ছোট example হাতে চালান
3. Approach (3–5 min)         → আগে সহজ (brute force), তারপর ভালো; complexity বলুন
4. Code (15–25 min)           → জোরে ভেবে লিখুন
5. Test (3–5 min)             → নিজের example দিয়ে line ধরে চালান, edge case
6. Follow-up                  → "What if the input is huge?" "Thread-safe?" "How to test?"
```

**মূল নিয়ম:**
1. **Code লেখার আগে approach বলুন।** Interviewer "ok" বললে তারপর লিখুন। ভুল পথে ১৫ মিনিট নষ্ট হয় না।
2. **চুপ থাকবেন না।** ৩০ সেকেন্ডের বেশি চুপ মানে interviewer আপনার চিন্তা দেখতে পায় না।
3. **Brute force লজ্জার না।** আগে কাজ করা উত্তর, তারপর optimize। "First a simple version, then I make it faster."
4. **Edge case নিজে বলুন:** empty input, এক element, duplicate, negative, খুব বড় input, null।
5. **Complexity বলুন:** time আর space, Big-O তে। কেন — এক লাইনে।
6. **Test নিজে করুন:** লেখা শেষে একটা example দিয়ে variable-গুলোর মান ধাপে ধাপে বলুন। অনেক bug এখানেই ধরা পড়ে।

**আটকে গেলে কী করবেন:**
- প্রশ্নটা নিজের ভাষায় আবার বলুন: "Let me say the problem again in my words."
- ছোট example হাতে চালান। Pattern প্রায়ই দেখা যায়।
- Data structure ভাবুন: দ্রুত খোঁজা → HashMap/HashSet; শেষে যা ঢুকেছে তা আগে বের → stack; sort করলে সহজ হয় কি? → sort।
- সৎভাবে hint চান: "I am stuck on this part. Can I get a small hint?" — এটা খারাপ দেখায় না। চুপ থাকাটাই খারাপ দেখায়।
- Syntax ভুলে গেলে বলুন আর এগিয়ে যান: "I don't remember the exact name, I think it is `removeLastOrNull`. I will check it in the IDE."

**জোরে ভাবার English phrase:**
- "Let me make sure I understand. The input is ..., and the output is ..."
- "Can the list be empty? Can there be duplicates?"
- "A simple way is ... It is O(n²). I think I can do better with a HashMap."
- "I will start with the function signature."
- "Here I check the edge case first."
- "This loop goes over each item once, so it is O(n)."
- "Let me test it with this small example."
- "I see a bug here. Let me fix it."
- "If I had more time, I would add tests for ..."

**পরিষ্কার Kotlin — যা interviewer লক্ষ্য করে:**
- `val` আগে, `var` শুধু দরকারে। Function ছোট, নাম পরিষ্কার (`seen`, `left`, `right`, `result`)।
- `!!` না। `?:`, `?.let`, early return ব্যবহার করুন।
- State-এর জন্য `sealed interface` + `when` (exhaustive)।
- Coroutine-এ `GlobalScope` না; `viewModelScope` বা `coroutineScope`। `catch (e: Exception)` দিয়ে `CancellationException` গিলে ফেলবেন না — নির্দিষ্ট exception ধরুন।
- Standard library জানুন: `groupingBy{}.eachCount()`, `groupBy`, `associateBy`, `sortedBy`, `ArrayDeque`, `withIndex()`, `buildList`।
- IDE থাকলে চালিয়ে দেখান। না থাকলে (shared doc) syntax নিখুঁত না হলেও logic পরিষ্কার রাখুন।

**Flutter থেকে এলে কী আলাদা:**
- Dart-এর `Map`/`List` থেকে Kotlin-এ mutable আর read-only আলাদা: `List` বনাম `MutableList`। Return-এ read-only দিন।
- Dart-এর `Stream` + `StreamController` ≈ Kotlin `Flow` + `MutableStateFlow`/`MutableSharedFlow`। `switchMap` (rxdart) ≈ `flatMapLatest`।
- Dart-এ `Future.wait` ≈ Kotlin-এ `coroutineScope { async {} ... awaitAll() }`, কিন্তু Kotlin-এ structured concurrency — একটা fail হলে বাকিগুলো cancel হয়।
- Null safety প্রায় একই, তবে Kotlin-এ `when` expression আর extension function অনেক বেশি ব্যবহার হয়।

---

### <a id="l1"></a>L1. ★ Warm-up: reverse words, check palindrome, count characters

**Task (English):**
1. "Reverse the order of words in a sentence. Remove extra spaces." `"  hello   big world "` → `"world big hello"`
2. "Check if a string is a palindrome. Ignore case and non-letter/digit characters." `"A man, a plan, a canal: Panama"` → `true`
3. "Count how many times each character appears."

**বুঝে নিন (approach):**
- Reverse words: `trim` → space দিয়ে split (একাধিক space-এর জন্য regex `\s+`) → `reversed()` → `joinToString(" ")`।
- Palindrome: নতুন string না বানিয়ে **two pointers** — বাঁ আর ডান থেকে একসাথে ভেতরে আসুন। অক্ষর/সংখ্যা না হলে skip। এতে extra memory লাগে না।
- Count: `HashMap`-এ গুনুন। Kotlin-এ এক লাইনে `groupingBy { it }.eachCount()`। Interviewer অনেক সময় হাতে লেখা loop দেখতে চায় — দুটোই জানুন।

```kotlin
fun reverseWords(sentence: String): String =
    sentence.trim().split(Regex("\\s+")).reversed().joinToString(" ")

fun isPalindrome(text: String): Boolean {
    var left = 0
    var right = text.lastIndex
    while (left < right) {
        when {
            !text[left].isLetterOrDigit() -> left++
            !text[right].isLetterOrDigit() -> right--
            text[left].lowercaseChar() != text[right].lowercaseChar() -> return false
            else -> {
                left++
                right--
            }
        }
    }
    return true
}

fun countChars(text: String): Map<Char, Int> {
    val counts = HashMap<Char, Int>()
    for (c in text) counts[c] = (counts[c] ?: 0) + 1
    return counts
}
// Short version: text.groupingBy { it }.eachCount()

fun firstUniqueChar(text: String): Char? {
    val counts = countChars(text)
    return text.firstOrNull { counts[it] == 1 }
}
```

**Complexity:** তিনটাই time O(n)। Space: reverseWords O(n) (নতুন list), isPalindrome O(1), countChars O(k) — k = আলাদা character সংখ্যা।

**Say while coding (English):**
> "For reverse words, I trim first and split on one or more spaces, so extra spaces go away."
> "For the palindrome, I use two pointers, so I don't need a new string. Space is O(1)."
> "If a character is not a letter or digit, I skip it."
> "For counting, I use a HashMap. In real code I would use groupingBy and eachCount."
> "Edge case: an empty string is a palindrome, and it returns true here."

**Follow-up:**
- **Q:** What about emoji or other characters outside the basic range?
  **A:** "A Kotlin Char is one UTF-16 unit, so some emoji take two Chars. For full Unicode I would work with code points instead of Chars."

**আরও দেখুন:** [K7 · Collections and Sequences](#k7) · [L2 · Two Sum](#l2)

---

### <a id="l2"></a>L2. ★ Two Sum with a HashMap

**Task (English):** "Given an array of integers and a target, return the indices of the two numbers that add up to the target. Assume one answer exists. You cannot use the same element twice." `[2, 7, 11, 15]`, target `9` → `[0, 1]`

**বুঝে নিন (approach):**
- Brute force: দুটো loop, সব জোড়া দেখা → O(n²)। আগে এটা মুখে বলুন।
- ভালো: একবার loop। প্রতিটা number-এর জন্য দেখুন `target - n` আগে দেখেছি কি না। দেখার জন্য `HashMap<value, index>`। খোঁজা O(1)।
- আগে খুঁজুন, তারপর map-এ রাখুন। এতে একই element দুবার ব্যবহার হয় না।
- উত্তর না থাকলে `null` ফেরত দিন (exception-এর চেয়ে পরিষ্কার)।

```kotlin
fun twoSum(nums: IntArray, target: Int): IntArray? {
    val indexByValue = HashMap<Int, Int>()
    for ((i, n) in nums.withIndex()) {
        val partnerIndex = indexByValue[target - n]
        if (partnerIndex != null) return intArrayOf(partnerIndex, i)
        indexByValue[n] = i
    }
    return null
}
```

**Complexity:** time O(n), space O(n)।

**Say while coding (English):**
> "The simple way is two loops, which is O(n squared)."
> "I can do it in one pass with a HashMap from value to index."
> "For each number, I check if target minus the number is already in the map."
> "I check first and then put, so I never use the same element twice."
> "If there is no answer, I return null."

**Follow-up:**
- **Q:** What if the array is already sorted?
  **A:** "Then I can use two pointers from both ends. If the sum is too small, I move the left pointer; if it is too big, I move the right one. That is O(n) time and O(1) space."
- **Q:** Any risk with very large numbers?
  **A:** "Target minus n can overflow Int. If the values can be that big, I would use Long."

**আরও দেখুন:** [L1 · Warm-up strings](#l1) · [K7 · Collections and Sequences](#k7)

---

### <a id="l3"></a>L3. ★ Valid parentheses with a stack

**Task (English):** "Given a string with only `()[]{}`, return true if every bracket is closed in the right order." `"([]{})"` → `true`, `"(]"` → `false`, `"(("` → `false`

**বুঝে নিন (approach):**
- খোলা bracket দেখলে stack-এ রাখুন। বন্ধ bracket দেখলে stack-এর উপরেরটা বের করে মেলান।
- মিলল না, বা stack খালি → `false`।
- শেষে stack খালি হতে হবে। না হলে কিছু খোলা রয়ে গেছে।
- Kotlin-এ stack মানে `ArrayDeque` (`addLast`, `removeLastOrNull`)। Java-র পুরনো `Stack` class ব্যবহার করবেন না (synchronized, পুরনো)।
- ছোট optimization: length বিজোড় হলে সাথে সাথে `false`।

```kotlin
private val openFor = mapOf(')' to '(', ']' to '[', '}' to '{')

fun isValidBrackets(text: String): Boolean {
    if (text.length % 2 != 0) return false
    val stack = ArrayDeque<Char>()
    for (c in text) {
        when (c) {
            '(', '[', '{' -> stack.addLast(c)
            ')', ']', '}' -> if (stack.removeLastOrNull() != openFor[c]) return false
            else -> return false
        }
    }
    return stack.isEmpty()
}
```

**Complexity:** time O(n), space O(n) (সবচেয়ে খারাপ ক্ষেত্রে সব খোলা bracket)।

**Say while coding (English):**
> "The last bracket I open must be the first one I close, so a stack fits."
> "I use Kotlin's ArrayDeque as the stack."
> "When I see a closing bracket, I pop and compare with the matching opening one."
> "If the stack is empty when I pop, removeLastOrNull gives null, so it returns false."
> "At the end, the stack must be empty."

**Follow-up:**
- **Q:** What if the string also has letters, like code?
  **A:** "I would skip any character that is not a bracket, instead of returning false. I would also remove the odd-length check, because letters change the length. The rest stays the same."

**আরও দেখুন:** [L2 · Two Sum](#l2) · [K7 · Collections and Sequences](#k7)

---

### <a id="l4"></a>L4. ◆ LRU cache

**Task (English):** "Build a cache with a fixed capacity. `get(key)` returns the value or null. `put(key, value)` adds or updates. When the cache is full, remove the least recently used item. Both should be O(1)."

**বুঝে নিন (approach):**
- **দ্রুত পথ:** Java/Kotlin-এর `LinkedHashMap`-এ `accessOrder = true` দিলে প্রতিটা `get`/`put` item-কে list-এর শেষে নেয়। `removeEldestEntry` override করলে size বেশি হলে সবচেয়ে পুরনোটা আপনাআপনি বাদ যায়। আগে এটা বলুন — এটা দেখায় আপনি standard library জানেন।
- Android-এ আসলে তৈরি `android.util.LruCache` আছে (thread-safe, `sizeOf` override করে byte হিসেবেও মাপা যায় — bitmap cache-এ কাজে লাগে)।
- **হাতে বানানো (interviewer প্রায়ই চায়):** `HashMap<K, Node>` + **doubly linked list**।
  - HashMap দেয় O(1) খোঁজা।
  - Linked list দেয় O(1) সরানো: head = সবচেয়ে নতুন, tail = সবচেয়ে পুরনো।
  - `get`: node খুঁজে head-এ সরান।
  - `put`: থাকলে value বদলে head-এ সরান; না থাকলে নতুন node head-এ; capacity পার হলে tail সরান আর map থেকে মুছুন।
  - কেন doubly: মাঝখান থেকে node সরাতে আগের node জানা লাগে।

```kotlin
class LruCache<K, V>(private val capacity: Int) {
    init { require(capacity > 0) { "capacity must be > 0" } }

    private val map = object : LinkedHashMap<K, V>(16, 0.75f, true) {
        override fun removeEldestEntry(eldest: MutableMap.MutableEntry<K, V>?): Boolean =
            size > capacity
    }

    fun get(key: K): V? = map[key]
    fun put(key: K, value: V) { map[key] = value }
}
```

হাতে বানানো version:

```kotlin
class ManualLruCache<K, V>(private val capacity: Int) {
    private class Node<K, V>(val key: K, var value: V) {
        var prev: Node<K, V>? = null
        var next: Node<K, V>? = null
    }

    private val nodes = HashMap<K, Node<K, V>>()
    private var head: Node<K, V>? = null // most recently used
    private var tail: Node<K, V>? = null // least recently used

    init { require(capacity > 0) { "capacity must be > 0" } }

    fun get(key: K): V? {
        val node = nodes[key] ?: return null
        moveToFront(node)
        return node.value
    }

    fun put(key: K, value: V) {
        val existing = nodes[key]
        if (existing != null) {
            existing.value = value
            moveToFront(existing)
            return
        }
        val node = Node(key, value)
        nodes[key] = node
        addToFront(node)
        if (nodes.size > capacity) {
            tail?.let { lru ->
                unlink(lru)
                nodes.remove(lru.key)
            }
        }
    }

    private fun moveToFront(node: Node<K, V>) {
        if (node === head) return
        unlink(node)
        addToFront(node)
    }

    private fun addToFront(node: Node<K, V>) {
        node.prev = null
        node.next = head
        head?.prev = node
        head = node
        if (tail == null) tail = node
    }

    private fun unlink(node: Node<K, V>) {
        val before = node.prev
        val after = node.next
        if (before != null) before.next = after else head = after
        if (after != null) after.prev = before else tail = before
        node.prev = null
        node.next = null
    }
}
```

**Complexity:** `get` আর `put` দুটোই O(1)। Space O(capacity)।

**Say while coding (English):**
> "First, the short version: LinkedHashMap with access order true, and I override removeEldestEntry."
> "On Android, there is also android.util.LruCache, which is thread-safe."
> "By hand, I use a HashMap for O(1) lookup and a doubly linked list for O(1) moves."
> "The head is the most recent item, and the tail is the least recent."
> "On get, I move the node to the front. On put, if we are over capacity, I remove the tail."
> "This class is not thread-safe. If many threads use it, I would add a lock."

**Follow-up:**
- **Q:** How would you limit the cache by memory size, not by item count?
  **A:** "I would keep a running total size. Each item has a size, like the byte count of a bitmap. After put, I remove from the tail until the total is under the limit. android.util.LruCache does this with sizeOf."
- **Q:** Why use sentinel nodes?
  **A:** "A dummy head and a dummy tail remove the null checks, so the link code is shorter and has fewer bugs."

**ভুল করবেন না:** singly linked list বলবেন না — মাঝের node O(1)-এ সরাতে doubly লাগে। আর map থেকে মুছতে ভুলবেন না (তাই node-এ key রাখা হয়)।

**আরও দেখুন:** [R12 · Coil or Glide](#r12) · [L9 · Thread-safe cache](#l9)

---

### <a id="l5"></a>L5. ★ Debounced search in a ViewModel with Flow

**Task (English):** "Build a search screen's ViewModel. The user types in a text field. Call the API only after the user stops typing for 300 ms. Do not search the same text twice. If a new query comes, cancel the old request. Expose loading, results, empty and error states."

**বুঝে নিন (approach):**
- User-এর লেখা রাখুন একটা `MutableStateFlow<String>`-এ। TextField এটা থেকেই সরাসরি value পায় — **TextField-এর text debounce করবেন না**, না হলে typing আটকে যায়।
- Pipeline:
  - `map { trim }` → spaces বাদ।
  - `debounce(300)` → user থামার পর ৩০০ ms অপেক্ষা।
  - `distinctUntilChanged()` → একই query আবার না।
  - `flatMapLatest` → নতুন query এলে আগের search cancel (Dart rxdart-এর `switchMap`)।
  - ভেতরের `flow { emit(Loading); emit(result) }.catch { emit(Error) }` → error ভেতরে ধরুন, যাতে বাইরের stream মরে না যায়।
  - `stateIn(viewModelScope, WhileSubscribed(5_000), Idle)` → UI-র জন্য `StateFlow`।
- `debounce` এখনও `@FlowPreview` আর `flatMapLatest` `@ExperimentalCoroutinesApi` চিহ্নিত — তাই `@OptIn` (version-ভেদে বদলাতে পারে)।
- Test: `runTest` + virtual time (`advanceTimeBy`) + Turbine দিয়ে real সময় অপেক্ষা ছাড়াই debounce test করা যায়।

```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.FlowPreview
import kotlinx.coroutines.flow.*

data class Product(val id: String, val name: String)

interface SearchRepository {
    suspend fun search(query: String): List<Product>
}

sealed interface SearchUiState {
    data object Idle : SearchUiState
    data object Loading : SearchUiState
    data object Empty : SearchUiState
    data class Success(val items: List<Product>) : SearchUiState
    data class Error(val message: String) : SearchUiState
}

@OptIn(FlowPreview::class, ExperimentalCoroutinesApi::class)
class SearchViewModel(private val repository: SearchRepository) : ViewModel() {

    private val _query = MutableStateFlow("")
    val query: StateFlow<String> = _query.asStateFlow()

    val uiState: StateFlow<SearchUiState> = _query
        .map { it.trim() }
        .debounce(DEBOUNCE_MS)
        .distinctUntilChanged()
        .flatMapLatest { text ->
            if (text.length < MIN_QUERY_LENGTH) flowOf<SearchUiState>(SearchUiState.Idle) else search(text)
        }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), SearchUiState.Idle)

    fun onQueryChange(text: String) {
        _query.value = text
    }

    private fun search(text: String): Flow<SearchUiState> = flow {
        emit(SearchUiState.Loading)
        val items = repository.search(text)
        emit(if (items.isEmpty()) SearchUiState.Empty else SearchUiState.Success(items))
    }.catch { e -> emit(SearchUiState.Error(e.message ?: "Something went wrong")) }

    private companion object {
        const val DEBOUNCE_MS = 300L
        const val MIN_QUERY_LENGTH = 2
    }
}
```

**Complexity:** algorithm-এর কিছু না; মূল কথা — প্রতি "থামা"-তে সর্বোচ্চ একটা network call, আর পুরনো call cancel হয়।

**Say while coding (English):**
> "I keep the raw text in a StateFlow, and the text field reads it directly, so typing stays fast."
> "I debounce for 300 milliseconds, so I call the API only when the user stops typing."
> "distinctUntilChanged stops a second search for the same text."
> "flatMapLatest cancels the old request when a new query comes."
> "I catch errors inside the inner flow, so one failed search does not stop the whole stream."
> "stateIn with WhileSubscribed keeps the work alive for 5 seconds, so a rotation does not restart it."

**Follow-up:**
- **Q:** Why flatMapLatest and not flatMapConcat or flatMapMerge?
  **A:** "Concat waits for the old search, and merge runs both and the old result can come last and show wrong data. Latest cancels the old one, which is what search needs."
- **Q:** How do you test the debounce without waiting for real time?
  **A:** "I use runTest with a test dispatcher for Main. Virtual time lets me call advanceTimeBy, and I check the states with Turbine."

**ভুল করবেন না:** `.catch` পুরো chain-এর শেষে দিলে প্রথম error-এর পর search পুরোপুরি বন্ধ হয়ে যায় — তাই inner flow-তে দিন।

**আরও দেখুন:** [K17 · Search with debounce](#k17) · [K13 · StateFlow and stateIn](#k13) · [R14 · Test a ViewModel](#r14)

---

### <a id="l6"></a>L6. ★ Fetch a list from an API and show loading / data / error in Compose

**Task (English):** "Load a list of users from `GET /users`. Show a spinner while loading, the list on success, and an error message with a Retry button on failure. Use Retrofit, a repository, a ViewModel with StateFlow, and a Composable."

**বুঝে নিন (approach):**
- Layer: `UserApi` (Retrofit interface) → `UserRepository` (DTO থেকে domain model) → `UsersViewModel` (`StateFlow<UsersUiState>`) → `UsersScreen` (Compose)।
- Retrofit-এর `suspend` function নিজেই background thread-এ network চালায় (main-safe)। তাই আলাদা `withContext(Dispatchers.IO)` লাগে না।
- Error ধরুন নির্দিষ্টভাবে: `IOException` (network নেই) আর `HttpException` (server-এর 4xx/5xx)। `catch (e: Exception)` দিলে `CancellationException`-ও ধরা পড়ে — এটা bug।
- Screen দুই ভাগ: `UsersScreen` (ViewModel থেকে state নেয়) আর `UsersContent` (শুধু state + callback)। Content stateless, তাই Preview আর UI test সহজ।
- `collectAsStateWithLifecycle()` — app background-এ গেলে collect থামে।
- আসল project-এ ViewModel-এ Hilt (`@HiltViewModel` + `@Inject constructor`), Retrofit-এ kotlinx-serialization বা Moshi converter, DI module। এখানে ছোট রাখতে বাদ।

```kotlin
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import kotlinx.serialization.Serializable
import retrofit2.HttpException
import retrofit2.http.GET
import java.io.IOException

// --- Data ---
@Serializable
data class UserDto(val id: Long, val name: String)

interface UserApi {
    @GET("users")
    suspend fun getUsers(): List<UserDto>
}

data class User(val id: Long, val name: String)

class UserRepository(private val api: UserApi) {
    suspend fun getUsers(): List<User> = api.getUsers().map { User(it.id, it.name) }
}

// --- ViewModel ---
sealed interface UsersUiState {
    data object Loading : UsersUiState
    data class Success(val users: List<User>) : UsersUiState
    data class Error(val message: String) : UsersUiState
}

class UsersViewModel(private val repository: UserRepository) : ViewModel() {
    private val _state = MutableStateFlow<UsersUiState>(UsersUiState.Loading)
    val state: StateFlow<UsersUiState> = _state.asStateFlow()

    init { load() }

    fun load() {
        viewModelScope.launch {
            _state.value = UsersUiState.Loading
            _state.value = try {
                UsersUiState.Success(repository.getUsers())
            } catch (e: IOException) {
                UsersUiState.Error("No internet connection")
            } catch (e: HttpException) {
                UsersUiState.Error("Server error (${e.code()})")
            }
        }
    }
}

// --- UI ---
@Composable
fun UsersScreen(viewModel: UsersViewModel) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    UsersContent(state = state, onRetry = viewModel::load)
}

@Composable
fun UsersContent(state: UsersUiState, onRetry: () -> Unit, modifier: Modifier = Modifier) {
    when (state) {
        UsersUiState.Loading -> Box(modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
            CircularProgressIndicator()
        }
        is UsersUiState.Error -> Column(
            modifier = modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Text(state.message)
            Spacer(Modifier.height(8.dp))
            Button(onClick = onRetry) { Text("Retry") }
        }
        is UsersUiState.Success -> LazyColumn(modifier.fillMaxSize()) {
            items(state.users, key = { it.id }) { user ->
                Text(user.name, Modifier.padding(16.dp))
            }
        }
    }
}
```

**Complexity:** O(n) — list map করা আর দেখানো। `LazyColumn` শুধু screen-এ দেখা item compose করে।

**Say while coding (English):**
> "I split it into four layers: API, repository, ViewModel and UI."
> "Retrofit suspend functions are main-safe, so I don't switch to the IO dispatcher here."
> "The UI state is a sealed interface, so the when in the UI covers every case."
> "I catch IOException and HttpException only. I do not catch all exceptions, because that would also catch cancellation."
> "The screen collects with collectAsStateWithLifecycle, so it stops when the app is in the background."
> "UsersContent is stateless, so I can preview it and test each state easily."

**Follow-up:**
- **Q:** Why load in init and not in the Composable with LaunchedEffect?
  **A:** "The ViewModel survives rotation, so init runs once per screen. A LaunchedEffect would run again after a config change unless I guard it. Some teams prefer loading inside stateIn on first subscribe — that also works."
- **Q:** How would you add pull-to-refresh without hiding the old list?
  **A:** "I would add an isRefreshing flag to the Success state, or use one data class with data, isLoading and error fields. Then the old list stays on screen while new data loads."
- **Q:** How do you test the ViewModel?
  **A:** "I give it a fake repository, set the Main dispatcher to a test dispatcher, and check that the state goes from Loading to Success or Error."

**ভুল করবেন না:** Composable-এর ভেতরে সরাসরি API call করবেন না, আর Loading/Error-কে আলাদা `Boolean` + nullable field-এ ছড়িয়ে দিয়ে অসম্ভব state (loading আর error একসাথে) তৈরি করবেন না।

**আরও দেখুন:** [U9 · Compose and ViewModel](#u9) · [R9 · Retrofit and OkHttp](#r9) · [R10 · Network errors to UI](#r10)

---

### <a id="l7"></a>L7. ◆ Run 3 network calls in parallel and combine; cancel all if one fails

**Task (English):** "A dashboard needs the user, their orders and their alerts from three APIs. Load them at the same time, not one after another. If one call fails, cancel the other two and show an error."

**বুঝে নিন (approach):**
- `coroutineScope { }` + তিনটা `async { }` → তিনটা একসাথে চলে। `await()` দিয়ে ফল।
- **Structured concurrency:** `coroutineScope`-এর ভেতরে একটা child fail করলে scope বাকি child-দের cancel করে, তারপর exception উপরে ছুড়ে দেয়। তাই "cancel all if one fails" আপনাআপনি হয়।
- মোট সময় ≈ সবচেয়ে ধীর call-এর সময় (যোগফল না)।
- উল্টো চাহিদা ("একটা fail হলেও বাকিগুলো দেখাও"): হয় সেই `async`-এর ভেতরে নির্দিষ্ট exception ধরে default দিন, নয়তো `supervisorScope`। `runCatching` সাবধানে — এটা `CancellationException`-ও ধরে।
- `GlobalScope.async` বা scope ছাড়া `async` দিলে cancel ঠিকমতো হয় না।
- Timeout লাগলে পুরোটা `withTimeout(10.seconds) { ... }`-এ মুড়ুন।

```kotlin
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import java.io.IOException

data class User(val id: Long, val name: String)
data class Order(val id: Long, val total: Long)
data class Alert(val id: Long, val text: String)
data class Dashboard(val user: User, val orders: List<Order>, val alerts: List<Alert>)

interface DashboardApi {
    suspend fun getUser(): User
    suspend fun getOrders(): List<Order>
    suspend fun getAlerts(): List<Alert>
}

class DashboardRepository(private val api: DashboardApi) {

    // All or nothing: if one call fails, the others are cancelled and the error is thrown.
    suspend fun loadDashboard(): Dashboard = coroutineScope {
        val user = async { api.getUser() }
        val orders = async { api.getOrders() }
        val alerts = async { api.getAlerts() }
        Dashboard(user.await(), orders.await(), alerts.await())
    }

    // Variant: alerts are optional, so their failure must not break the screen.
    suspend fun loadDashboardWithOptionalAlerts(): Dashboard = coroutineScope {
        val user = async { api.getUser() }
        val orders = async { api.getOrders() }
        val alerts = async {
            try { api.getAlerts() } catch (e: IOException) { emptyList() }
        }
        Dashboard(user.await(), orders.await(), alerts.await())
    }
}
```

ViewModel-এ ডাকা: `viewModelScope.launch { _state.value = try { Success(repo.loadDashboard()) } catch (e: IOException) { Error(...) } }`। User screen ছাড়লে `viewModelScope` cancel → তিনটা call-ই cancel।

**Complexity:** সময় ≈ max(t1, t2, t3), sequential হলে t1 + t2 + t3।

**Say while coding (English):**
> "I use coroutineScope with three async blocks, so the calls run at the same time."
> "The total time is the slowest call, not the sum."
> "If one call fails, coroutineScope cancels the other two and throws the error. That is structured concurrency."
> "If one part is optional, I catch its specific error inside its own async and return a default."
> "I don't use GlobalScope, because then nothing cancels the calls when the user leaves."

**Follow-up:**
- **Q:** What is the difference between coroutineScope and supervisorScope?
  **A:** "In coroutineScope, one failed child cancels all the others. In supervisorScope, children fail on their own, and I handle each result myself."
- **Q:** What if there are 20 calls, not 3?
  **A:** "I map the ids to async calls and use awaitAll. To avoid too many requests at once, I limit them with a Semaphore or a limited dispatcher."

**ভুল করবেন না:** `async { }` লিখে সাথে সাথে `.await()` করবেন না (`async { a() }.await()` তারপর পরেরটা) — তাহলে আবার একটার পর একটা চলে।

**আরও দেখুন:** [K10 · launch vs async](#k10) · [K11 · Structured concurrency](#k11) · [L11 · Retry with backoff](#l11)

---

### <a id="l11"></a>L11. ◆ Implement a simple retry with exponential backoff in Kotlin

**Task (English):** "Write a function that runs a suspend block. If it fails with a network error, wait and try again. Each wait should be about twice as long as the last one. Stop after a max number of attempts, and never wait longer than a max delay. Add some random jitter."

**বুঝে নিন (approach):**
- **Exponential backoff:** প্রতিবার fail হলে অপেক্ষা দ্বিগুণ — 500 ms → 1 s → 2 s → 4 s। একটা `maxDelay` দিয়ে উপরের সীমা।
- **Jitter:** অপেক্ষায় একটু random যোগ করুন। Server down হলে হাজারো phone একসাথে fail করে। Jitter না থাকলে সবাই একই সেকেন্ডে আবার request পাঠায়, server আবার পড়ে যায়।
- **কোন error-এ retry:** network error (`IOException`), 5xx, 429। 400/404-এ retry করে লাভ নেই। 401 গেলে token refresh-এর পথে যান (R9)।
- **শুধু নিরাপদ request retry:** GET, অথবা idempotency key সহ POST। না হলে একই order দুবার হতে পারে।
- **`CancellationException` কখনো ধরে রাখবেন না।** User screen ছাড়লে retry loop-ও থামতে হবে।
- `delay` coroutine-কে suspend করে, thread block করে না। Test-এ `runTest`-এর virtual time এই অপেক্ষা সাথে সাথে পার করে দেয়।
- Flow-তে একই কাজ `retryWhen { cause, attempt -> ... }` দিয়ে। Background কাজে WorkManager-এর `BackoffPolicy.EXPONENTIAL` আছে — নিজে loop লিখতে হয় না।

```kotlin
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.delay
import java.io.IOException
import kotlin.random.Random
import kotlin.time.Duration
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.Duration.Companion.seconds

suspend fun <T> retryWithBackoff(
    maxAttempts: Int = 4,
    initialDelay: Duration = 500.milliseconds,
    maxDelay: Duration = 10.seconds,
    shouldRetry: (Throwable) -> Boolean = { it is IOException },
    block: suspend () -> T,
): T {
    require(maxAttempts > 0) { "maxAttempts must be > 0" }
    var nextDelay = initialDelay
    repeat(maxAttempts - 1) {
        try {
            return block()
        } catch (e: Throwable) {
            if (e is CancellationException || !shouldRetry(e)) throw e
        }
        delay(nextDelay * Random.nextDouble(0.5, 1.0)) // jitter: wait 50–100% of the delay
        nextDelay = (nextDelay * 2).coerceAtMost(maxDelay)
    }
    return block() // last attempt: its error goes to the caller
}

// Use: val users = retryWithBackoff { api.getUsers() }
```

**Complexity:** সর্বোচ্চ `maxAttempts` বার call। সবচেয়ে খারাপ ক্ষেত্রে মোট অপেক্ষা ≈ সব delay-এর যোগফল (এখানে ৩টা অপেক্ষা, মোট ৩.৫ সেকেন্ডের কম)।

**Say while coding (English):**
> "I take the block as a suspend lambda, so I can retry any call."
> "After each failure, I wait, and then I double the delay. I cap it with maxDelay."
> "I multiply the delay by a random number between 0.5 and 1. This jitter stops all phones from retrying at the same moment."
> "By default I only retry IOException, because a 400 or 404 will fail again."
> "I always rethrow CancellationException, so the loop stops when the user leaves the screen."
> "The last attempt is outside the loop, so its error goes to the caller."
> "delay suspends and does not block the thread. In tests, runTest skips the waiting with virtual time."

**Follow-up:**
- **Q:** How do you test this?
  **A:** "I use runTest, so delay takes no real time. A fake call fails two times and then works. I check that the result is correct and that it was called three times. For exact timing, I would pass in the Random so the test is the same every time."
- **Q:** The server sends 429 with a Retry-After header. What do you do?
  **A:** "I respect the header. I wait the time the server asks for, not my own delay, and I still keep a max number of attempts."
- **Q:** Should OkHttp or the ViewModel do the retry?
  **A:** "I keep it in the repository or the data layer, close to the call. The ViewModel stays simple. For work that must finish in the background, I let WorkManager do the backoff."

**ভুল করবেন না:** `catch (e: Exception)` দিয়ে সব error-এ retry করবেন না — এতে `CancellationException`-ও ধরা পড়ে, আর 400-এর মতো error-এ বারবার অকারণে request যায়। POST retry করলে idempotency key-এর কথা বলুন।

**আরও দেখুন:** [R10 · Network errors to UI](#r10) · [K11 · Structured concurrency](#k11) · [D5 · Resumable upload](#d5)

---

### <a id="l8"></a>L8. ◆ Find the bug in Android code

**Task (English):** "Here are three short pieces of code. Find the bug in each, explain what goes wrong, and fix it."

**বুঝে নিন (approach):** "Find the bug" round-এ ধাপ: (১) bug-এর নাম বলুন, (২) কী খারাপ হয় (leak, crash, ANR, ভুল data), (৩) fix, (৪) কীভাবে ধরা যায় (LeakCanary, StrictMode, lint)।

**Bug 1 — Activity leak in a singleton**
```kotlin
object ImageLoader {
    private var context: Context? = null
    fun init(context: Context) { this.context = context }
}

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        ImageLoader.init(this) // BUG
    }
}
```
- সমস্যা: `object` app যতক্ষণ চলে ততক্ষণ থাকে। এটা Activity ধরে রাখে। Rotation-এ পুরনো Activity আর তার পুরো View tree garbage collect হয় না → memory leak।
- Fix: শুধু application context রাখুন, বা context রাখবেনই না (দরকারে parameter হিসেবে নিন, বা DI দিয়ে `@ApplicationContext`)।
```kotlin
object ImageLoader {
    private lateinit var appContext: Context
    fun init(context: Context) { appContext = context.applicationContext }
}
```
- ধরবেন কীভাবে: LeakCanary।

**Bug 2 — collecting a Flow without lifecycle**
```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        lifecycleScope.launch {
            viewModel.locationUpdates.collect { render(it) } // BUG
        }
    }
}
```
- সমস্যা: `lifecycleScope` শুধু destroy-তে cancel হয়। App background-এ গেলেও collect চলতে থাকে → GPS/network চালু থাকে, battery খায়, আর stopped UI update করতে গিয়ে crash হতে পারে।
- Fix: `repeatOnLifecycle(Lifecycle.State.STARTED)` — STARTED-এ collect শুরু, STOPPED-এ cancel। Fragment-এ `viewLifecycleOwner.lifecycleScope`। Compose-এ `collectAsStateWithLifecycle()`।
```kotlin
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.locationUpdates.collect { render(it) }
    }
}
```

**Bug 3 — GlobalScope and blocking the main thread**
```kotlin
class NoteViewModel(private val dao: NoteDao) : ViewModel() {
    fun onSave(note: Note) {
        GlobalScope.launch(Dispatchers.Main) {
            val json = File(BACKUP_PATH).readText() // BUG: disk on main thread
            dao.insertBlocking(note.copy(backup = json)) // BUG: blocking DB call on main
            _saved.value = true
        }
    }
}
```
- সমস্যা ১: `GlobalScope` — ViewModel clear হলেও কাজ চলে, cancel হয় না, leak, আর ভুল সময়ে state update।
- সমস্যা ২: Main thread-এ disk আর blocking DB call → UI জমে যায়, বড় file হলে ANR। (Room main thread-এ query দিলে exception দেয়, যদি না `allowMainThreadQueries()` দেওয়া থাকে।)
- Fix: `viewModelScope` + blocking কাজ `Dispatchers.IO`-তে, আর Room-এর `suspend` DAO function। সবচেয়ে ভালো: repository নিজেই main-safe হোক।
```kotlin
class NoteViewModel(private val repository: NoteRepository) : ViewModel() {
    fun onSave(note: Note) {
        viewModelScope.launch {
            repository.save(note) // main-safe: switches to IO inside
            _saved.value = true
        }
    }
}

class NoteRepository(private val dao: NoteDao, private val io: CoroutineDispatcher = Dispatchers.IO) {
    suspend fun save(note: Note) {
        val json = withContext(io) { File(BACKUP_PATH).readText() }
        dao.insert(note.copy(backup = json)) // suspend DAO, Room runs it off the main thread
    }
}
```
- ধরবেন কীভাবে: debug build-এ StrictMode (disk/network on main), Android Studio-র lint (GlobalScope delicate API warning), Play vitals-এ ANR।

**Complexity:** এখানে লাগে না।

**Say while coding (English):**
> "In the first one, a singleton keeps the Activity, so the Activity leaks after rotation. I keep the application context instead."
> "In the second one, the collect keeps running in the background. I wrap it in repeatOnLifecycle with STARTED."
> "In the third one, GlobalScope is never cancelled, and the file read blocks the main thread, which can cause an ANR."
> "I move it to viewModelScope, and the repository switches to the IO dispatcher, so it is main-safe."
> "I inject the dispatcher, so in tests I can pass a test dispatcher."
> "To catch these early, I use LeakCanary and StrictMode in debug builds."

**Follow-up:**
- **Q:** Why is `lateinit var appContext` in an object OK, but the Activity is not?
  **A:** "The application context lives as long as the process, the same as the object. So it never holds something that should have died. An Activity dies on rotation, so holding it is a leak."

**ভুল করবেন না:** শুধু "এটা খারাপ" বলবেন না — প্রতিটা bug-এর ফল (leak / battery / ANR) নাম ধরে বলুন। Interviewer এটাই শুনতে চায়।

**আরও দেখুন:** [P2 · Memory leaks](#p2) · [K14 · Collect a Flow safely](#k14) · [P1 · ANR](#p1)

---

### <a id="l9"></a>L9. ○ Thread-safe in-memory cache with Mutex

**Task (English):** "Write an in-memory cache that many coroutines can use at the same time. It should have `get`, `put`, and `getOrLoad(key) { load }` that loads the value only if it is missing."

**বুঝে নিন (approach):**
- `HashMap` thread-safe না। একসাথে লিখলে data নষ্ট হতে পারে।
- Coroutine-এ lock = `kotlinx.coroutines.sync.Mutex`। `synchronized` thread block করে, আর তার ভেতরে `suspend` call দেওয়া যায় না। `Mutex.withLock` thread block করে না, coroutine-কে suspend করে।
- **Lock-এর ভেতরে ধীর কাজ (network) করবেন না।** তাহলে সব key-র সব caller অপেক্ষা করে। তাই: lock নিয়ে দেখুন → lock ছেড়ে load করুন → আবার lock নিয়ে রাখুন।
- Trade-off: একই key দুটো coroutine একসাথে চাইলে দুবার load হতে পারে। দরকার হলে per-key `Deferred` রাখুন (নিচে follow-up)।
- `Mutex` reentrant না — `withLock`-এর ভেতরে আবার একই mutex-এর `withLock` দিলে deadlock।
- শুধু get/put লাগলে `ConcurrentHashMap`-ও যথেষ্ট। Mutex লাগে যখন কয়েকটা ধাপ একসাথে atomic রাখতে হয়।

```kotlin
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

class MemoryCache<K : Any, V : Any> {
    private val mutex = Mutex()
    private val entries = HashMap<K, V>()

    suspend fun get(key: K): V? = mutex.withLock { entries[key] }

    suspend fun put(key: K, value: V) {
        mutex.withLock { entries[key] = value }
    }

    suspend fun getOrLoad(key: K, load: suspend (K) -> V): V {
        mutex.withLock { entries[key] }?.let { return it }
        val loaded = load(key) // outside the lock, so a slow load does not block other keys
        return mutex.withLock { entries.getOrPut(key) { loaded } }
    }

    suspend fun clear() {
        mutex.withLock { entries.clear() }
    }
}
```

**Complexity:** প্রতিটা operation গড়ে O(1) (+ lock-এর অপেক্ষা)। Space O(n)।

**Say while coding (English):**
> "A plain HashMap is not safe when many coroutines write at once, so I guard it with a Mutex."
> "I use Mutex and not synchronized, because Mutex suspends instead of blocking the thread."
> "I never call the slow load inside the lock. I check, release, load, and then lock again to save."
> "At the end I use getOrPut, so if another coroutine saved first, we keep the first value."
> "The trade-off is that two callers can load the same key at the same time."
> "Mutex is not reentrant, so I never lock it again inside withLock."

**Follow-up:**
- **Q:** How do you make sure the same key is loaded only once?
  **A:** "I keep a map from key to Deferred. Under the lock, I return the existing Deferred or create a new async load and save it. All callers await the same Deferred. If it fails, I remove it so the next call can retry."

**আরও দেখুন:** [K16 · Thread safety](#k16) · [L4 · LRU cache](#l4)

---

### <a id="l10"></a>L10. ○ Merge intervals (and group anagrams)

**Task (English):** "Given a list of time intervals, merge all overlapping ones." `[1,3] [2,6] [8,10] [15,18]` → `[1,6] [8,10] [15,18]`

**বুঝে নিন (approach):**
- আগে `start` দিয়ে sort করুন। তাহলে overlap শুধু পাশাপাশি interval-এ হয়।
- Result-এর শেষ interval-এর সাথে বর্তমানটা মিলান: `current.start <= last.end` হলে merge (`end = max`), না হলে নতুন যোগ।
- আসল কাজে: camera timeline-এ (D1) recording segment জোড়া লাগাতে ঠিক এই code লাগে। Interview-এ এটা বললে ভালো লাগে।
- `<=` নাকি `<` — `[1,2]` আর `[2,3]` জোড়া হবে কি না, interviewer-কে জিজ্ঞেস করুন।

```kotlin
data class Interval(val start: Int, val end: Int)

fun mergeIntervals(intervals: List<Interval>): List<Interval> {
    if (intervals.isEmpty()) return emptyList()
    val sorted = intervals.sortedBy { it.start }
    val merged = mutableListOf(sorted.first())
    for (current in sorted.drop(1)) {
        val last = merged.last()
        if (current.start <= last.end) {
            merged[merged.lastIndex] = last.copy(end = maxOf(last.end, current.end))
        } else {
            merged.add(current)
        }
    }
    return merged
}

// Bonus classic: group anagrams. Words with the same sorted letters share a key.
fun groupAnagrams(words: List<String>): List<List<String>> =
    words.groupBy { word -> word.toCharArray().sorted().joinToString("") }.values.toList()
```

**Complexity:** merge — time O(n log n) (sort), space O(n)। Group anagrams — time O(n · k log k) (k = শব্দের দৈর্ঘ্য), space O(n · k)।

**Say while coding (English):**
> "First I sort by start time. Then overlaps can only happen between neighbours."
> "I compare each interval with the last one in the result."
> "If it starts before the last one ends, I merge and keep the bigger end."
> "Sorting is O(n log n), and the loop is O(n)."
> "This is the same logic I would use to join recording segments on a camera timeline."

**Follow-up:**
- **Q:** Can you make group anagrams faster for long words?
  **A:** "Yes. Instead of sorting each word, I count the 26 letters and use the counts as the key. That is O(k) per word, for lowercase English letters."

**ভুল করবেন না:** sort না করে merge শুরু করবেন না, আর `maxOf(last.end, current.end)` ভুলবেন না — একটা interval অন্যটার পুরো ভেতরে থাকতে পারে (`[1,10]` আর `[2,3]`)।

**আরও দেখুন:** [D1 · Security camera app](#d1) · [L1 · Warm-up strings](#l1)

---


## <a id="part-13"></a>Part 13 — Behavioral, teamwork আর client-এর প্রশ্ন

### আগে বুঝুন — behavioral প্রশ্নে interviewer কী খোঁজে

Technical প্রশ্নে দেখে আপনি কী জানেন। Behavioral প্রশ্নে দেখে **আপনার সাথে কাজ করা কেমন হবে**। বিদেশি team-এ এটা খুব জরুরি। অনেক সময় এখানেই ঠিক হয় আপনি job পাবেন কি না।

তারা পাঁচটা জিনিস খোঁজে:

1. **Ownership** — সমস্যা হলে আপনি নিজে দায়িত্ব নেন কি না।
2. **Communication** — খারাপ খবর আগে জানান কি না। স্পষ্ট লেখেন কি না।
3. **Learning** — ভুল থেকে শেখেন কি না।
4. **Teamwork** — মতের অমিল ভদ্রভাবে সামলান কি না।
5. **Judgment** — তাড়াহুড়োর মধ্যেও quality আর সময় দুটোই ঠিক রাখতে পারেন কি না।

**STAR format** — প্রতিটা গল্প এই ৪ ভাগে বলুন:

| ভাগ | মানে | কত লম্বা |
|---|---|---|
| **S**ituation | কোথায়, কী অবস্থা | ১–২ বাক্য |
| **T**ask | আপনার দায়িত্ব কী ছিল | ১ বাক্য |
| **A**ction | **আপনি** কী করলেন ("we" না, "I") | ৩–৪ বাক্য — সবচেয়ে বড় অংশ |
| **R**esult | ফল কী হলো, কী শিখলেন | ১–২ বাক্য |

**এখনই কাজ:** নিজের কাজ থেকে ৬টা সত্যি গল্প লিখে ফেলুন: (১) একটা কঠিন bug, (২) একটা deadline-এর চাপ, (৩) একটা মতের অমিল, (৪) একটা ভুল, (৫) কাউকে সাহায্য করা বা শেখানো, (৬) খুব দ্রুত নতুন কিছু শেখা। এই ৬টা গল্প দিয়েই প্রায় সব behavioral প্রশ্নের উত্তর দেওয়া যায়। নিচের উত্তরগুলো নমুনা। **[...]** জায়গায় নিজের সত্যি ঘটনা বসান। বানানো গল্প বলবেন না। Follow-up-এ ধরা পড়ে।

---

### <a id="h1"></a>H1. ★ Tell me about a difficult bug you fixed.

**প্রশ্নটা মানে:** আপনি কীভাবে debug করেন — ধাপে ধাপে, নাকি অনুমানে।
**অন্যভাবেও জিজ্ঞেস করে:** "Tell me about a hard technical problem." · "What is the toughest issue you solved?"

**বুঝে নিন:**
- গল্পের মূল হলো **পদ্ধতি**: reproduce → data দেখা (log, crash report, trace) → কারণ আন্দাজ করা → সেটা পরীক্ষা করা → fix → regression test → আবার যেন না হয়, তার ব্যবস্থা।
- Android-এর ভালো উদাহরণ: শুধু কিছু device-এ crash, process death-এর পরে state হারানো, ANR, memory leak, release build-এ R8-এর কারণে crash।

**Answer (English):**
> "In one app, [users on some Android devices saw a crash after coming back to the app]. I could not reproduce it at first. So I checked the crash reports and saw it happened after the app was killed in the background. I reproduced it with the 'Don't keep activities' option. The problem was [state that was not saved]. I moved the state to SavedStateHandle and added a test. After the release, the crash went away. Since then, I always test process death before a release."

**Key words:** `reproduce` · `crash reports` · `root cause` · `regression test`

**Follow-up:**
- **Q:** How did you make sure it does not happen again?
  **A:** "I added a test for that case and added process-death testing to our release checklist."
- **Q:** What tools do you use to debug?
  **A:** "Logcat, the debugger, Crashlytics or Play vitals for production, Perfetto for performance, and LeakCanary for leaks."

**আরও দেখুন:** [P10 · Bug you cannot reproduce](#p10) · [C4 · Process death](#c4) · [P8 · Crash and ANR monitoring](#p8)

---

### <a id="h2"></a>H2. ★ Tell me about a time you missed a deadline or were under pressure.

**প্রশ্নটা মানে:** চাপে আপনি কী করেন — চুপ থাকেন, নাকি আগে জানান?
**অন্যভাবেও জিজ্ঞেস করে:** "How do you handle tight deadlines?" · "What do you do when a task takes longer than planned?"

**বুঝে নিন:**
- মূল কথা: **আগে জানানো**, **scope ভাগ করা** (কোনটা এখন, কোনটা পরে), quality-র মূল জিনিস (test, crash) বাদ না দেওয়া।
- "আমি রাত জেগে সব করেছি" — এটা ভালো উত্তর না। এতে দেখায় plan করতে পারেন না।

**Answer (English):**
> "In one project, a feature took longer because [an API was not ready]. When I saw the risk, I told the team the same day, not at the deadline. I suggested a plan: release the main flow first and move two small parts to the next version. The team agreed. We shipped on time with good quality, and the rest came one week later. I learned to share risks early."

**Key words:** `raised the risk early` · `cut the scope` · `shipped on time`

**Follow-up:**
- **Q:** Do you ever skip tests to meet a deadline?
  **A:** "I don't skip tests for the important logic. If time is very short, I may delay small UI tests and write a ticket for them, so it is tracked."

**আরও দেখুন:** [H13 · Agile / Scrum](#h13) · [H4 · A mistake you made](#h4)

---

### <a id="h3"></a>H3. ★ Tell me about a disagreement with a teammate or lead.

**প্রশ্নটা মানে:** মতের অমিল হলে আপনি ভদ্র থাকেন কি না, আর যুক্তি দিয়ে কথা বলেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "Have you had a conflict at work?" · "What do you do if you disagree with a technical decision?"

**বুঝে নিন:**
- ভালো গল্প: technical বিষয়ে অমিল (যেমন কোন library, কোন architecture)। ব্যক্তিগত ঝগড়া না।
- পদ্ধতি: অন্যের যুক্তি শোনা → data বা ছোট prototype দিয়ে তুলনা → team সিদ্ধান্ত নিলে মেনে নেওয়া ("disagree and commit")।

**Answer (English):**
> "A teammate wanted to [add a big new library], and I thought it was too much for our need. Instead of arguing, I asked about their reasons. Then I suggested we try both ways in a small prototype and compare build size and code. The data showed [the simpler way was enough]. We agreed together. If the result was the other way, I would have accepted it. For me the goal is the best result for the product, not winning."

**Key words:** `listened first` · `small prototype` · `data` · `disagree and commit`

**Follow-up:**
- **Q:** What if your manager decides against you?
  **A:** "I share my concern once, clearly, with facts. If the decision stays, I follow it fully and help it succeed."

**আরও দেখুন:** [H6 · Code review](#h6) · [H5 · Working with other roles](#h5)

---

### <a id="h4"></a>H4. ★ Tell me about a mistake you made.

**প্রশ্নটা মানে:** আপনি কি নিজের ভুল স্বীকার করেন আর তা থেকে শেখেন?
**অন্যভাবেও জিজ্ঞেস করে:** "Tell me about a failure." · "What would you do differently?"

**বুঝে নিন:**
- সত্যিকারের, কিন্তু মারাত্মক না, এমন ভুল বেছে নিন। যেমন release-এ একটা bug গেল, ভুল estimate।
- তিনটা জিনিস: দ্রুত স্বীকার, দ্রুত ঠিক, আর **পদ্ধতি বদলানো**, যাতে আবার না হয়।

**Answer (English):**
> "Once I released an update without testing on [an older Android version], and a screen crashed for some users. I saw it in the crash report within hours. I told my lead, fixed it, and released a hotfix the same day with a staged rollout. After that, I added older Android versions to our test devices and started using staged rollouts for every release. The mistake made our process better."

**Key words:** `owned it` · `hotfix` · `staged rollout` · `changed the process`

**Follow-up:**
- **Q:** How do you prevent such issues now?
  **A:** "CI tests on several API levels, a release checklist, staged rollout, and watching crash rates in the first hours after release."

**আরও দেখুন:** [P8 · Crash and ANR monitoring](#p8) · [H1 · A difficult bug](#h1) · [H0-6 · Strengths and weaknesses](#h0-6)

---

### <a id="h5"></a>H5. ★ How do you work with designers, QA and backend developers?

**প্রশ্নটা মানে:** Team-এর অন্যদের সাথে আপনার যোগাযোগ কেমন।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you handle API changes from the backend?" · "What if the design is hard to build?"

**বুঝে নিন:**
- Designer: শুরুতেই বলুন কোনটা কঠিন বা platform-এর নিয়মের বাইরে। বিকল্প দিন।
- Backend: API contract আগে ঠিক করা (OpenAPI), mock দিয়ে কাজ শুরু।
- QA: পরিষ্কার test build, release note, কী বদলেছে তা জানানো।

**Answer (English):**
> "I try to talk early. With designers, I check the design before I build, and if something is hard on Android, I suggest an option that looks close and follows Material rules. With backend, we agree on the API contract first, and I build with a mock until the real API is ready. With QA, I share clear builds and notes about what changed. Early talk saves a lot of time later."

**Key words:** `talk early` · `API contract` · `mock` · `release notes`

**Follow-up:**
- **Q:** What if the backend changes the API without telling you?
  **A:** "First I fix the app safely. Then I suggest API versioning and contract tests, so it does not happen again."

**আরও দেখুন:** [H13 · Agile / Scrum](#h13) · [H15 · Remote work](#h15) · [H6 · Code review](#h6)

---

### <a id="h6"></a>H6. ◆ How do you review code? How do you take review comments?

**প্রশ্নটা মানে:** Code review-তে আপনি কী দেখেন, আর সমালোচনা কীভাবে নেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What do you look for in a pull request?"

**বুঝে নিন:**
- কী দেখেন: আগে দেখুন code ঠিক কাজ করে কি না (bug, edge case, threading, lifecycle)। তারপর security, test, readability। Format দেখার কাজ lint-এর।
- কীভাবে বলেন: প্রশ্ন আকারে, কারণসহ, ভদ্রভাবে।
- নিজে comment পেলে: ব্যক্তিগতভাবে না নেওয়া, ধন্যবাদ দেওয়া, না মানলে কারণ বলা।

**Answer (English):**
> "First I check if the code is correct — edge cases, threading, lifecycle and error handling. Then security, tests, and if the next person can read it easily. Style is the linter's job. I write comments as questions with a reason, like 'What happens if this list is empty?'. When I get comments, I don't take them personally. I fix them or explain my reason politely."

**Key words:** `correctness first` · `edge cases` · `linter` · `explain the reason`

**আরও দেখুন:** [H3 · Disagreement](#h3) · [H8 · Mentoring](#h8)

---

### <a id="h7"></a>H7. ◆ How do you learn new things and stay up to date?

**প্রশ্নটা মানে:** আপনি কি নিজে থেকে শেখেন? Android খুব দ্রুত বদলায়।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you keep up with Android changes?"

**বুঝে নিন:** সত্যিকারের source-এর নাম বলুন: Android Developers Blog, প্রতিটা Android version-এর "behavior changes" page, Kotlin blog, Google I/O talks, official samples (যেমন Now in Android app)। আর বলুন: ছোট sample বানিয়ে হাতে-কলমে শেখেন।

**Answer (English):**
> "I follow the Android Developers Blog and read the behavior-changes page for every new Android version, because those changes can break apps. I watch Google I/O talks and look at official samples like Now in Android. But I learn best by building. For example, when I refreshed my native skills, I built a small app with Compose, Hilt, Room and coroutines. I also use AI tools in Android Studio, but I always check the result myself."

**Key words:** `behavior changes` · `official samples` · `learn by building`

**আরও দেখুন:** [H14 · Learning fast](#h14) · [F12 · New in 2025–2026](#f12)

---

### <a id="h8"></a>H8. ◆ Have you mentored or helped a junior developer?

**প্রশ্নটা মানে:** Senior হিসেবে আপনি অন্যদের বড় করতে পারেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "Tell me about a time you helped a teammate."

**বুঝে নিন:** তিনটা জিনিস দেখান। উত্তর সরাসরি না দিয়ে প্রশ্ন করে ভাবতে সাহায্য করা। Pair programming। ছোট দায়িত্ব দিয়ে আত্মবিশ্বাস বাড়ানো।

**Answer (English):**
> "Yes. [A junior developer] was stuck with [state handling / a crash]. Instead of giving the answer, I asked questions to help them find the cause, and we did some pair programming. Later I gave them a small feature to own fully, with reviews from me. After a few weeks they were working on their own. I enjoy this part of senior work."

**Key words:** `pair programming` · `ask questions` · `own a feature`

**আরও দেখুন:** [H6 · Code review](#h6) · [H3 · Disagreement](#h3)

---

### <a id="h13"></a>H13. ◆ How do you work in Agile / Scrum? (sprints, standups, estimates, demos)

**প্রশ্নটা মানে:** তাদের team-এর কাজের নিয়মে আপনি সহজে মিশে যেতে পারবেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "What is your experience with Scrum?" · "How do you estimate a user story?"

**বুঝে নিন:**
- **Sprint:** সাধারণত ১–২ সপ্তাহ। শুরুতে sprint planning। শেষে review (demo) আর retrospective (retro)।
- **Daily standup:** ১৫ মিনিটের মধ্যে। তিনটা কথা: কাল কী করেছি, আজ কী করব, কোথায় আটকে আছি (blocker)। সমস্যার সমাধান standup-এ না, পরে আলাদা করে।
- **Estimate:** story points বা দিন। Story point মানে ঘণ্টা না। কাজটা কত বড়, কত জটিল, কত ঝুঁকি — সব মিলিয়ে একটা সংখ্যা। বড় story ভেঙে ছোট করুন।
- **Demo:** শেষ হওয়া কাজ চালিয়ে দেখানো। Mobile-এ real device বা test build দিয়ে (Firebase App Distribution, Play internal testing)।
- **Definition of done:** code review, test, QA pass — সব হলে তবেই "done"।
- কিছু team sprint ছাড়া **Kanban** চালায়: কাজ একটা board-এ চলতে থাকে। Remote team-এ standup অনেক সময় Slack-এ লিখে হয়।

**Answer (English):**
> "Most of my teams used Scrum with two-week sprints. In sprint planning, we pick stories from the backlog and estimate them with story points. I split big stories into small tasks, so the risk is clear early. In the daily standup, I keep it short: what I did, what I will do, and any blocker. I raise blockers the same day. At the end of the sprint, I demo the feature on a real device or a test build. In the retro, I try to bring one clear idea to improve. If a team uses Kanban instead, that works for me too."

**Key words:** `sprint planning` · `story points` · `standup` · `blocker` · `demo` · `retro`

**Follow-up:**
- **Q:** What do you do when your estimate is wrong?
  **A:** "I tell the team as soon as I see it, not at the end of the sprint. I explain why. Then we decide together: cut the scope or move the rest to the next sprint."
- **Q:** What is a story point?
  **A:** "It is the size of the work, not hours. It includes how complex and how risky the task is. The team compares a new story with stories it already did."

**ভুল করবেন না:** Standup-এ লম্বা technical আলোচনা শুরু করবেন না। বলুন: "Let's discuss this after the standup."

**আরও দেখুন:** [H2 · Deadline pressure](#h2) · [H5 · Working with other roles](#h5) · [H15 · Remote work](#h15)

---

### <a id="h14"></a>H14. ◆ Tell me about a time you had to learn something new very fast.

**প্রশ্নটা মানে:** নতুন জিনিসে আপনি কত দ্রুত কাজের মানুষ হয়ে ওঠেন। আর আপনার শেখার পদ্ধতি কী।
**অন্যভাবেও জিজ্ঞেস করে:** "How do you learn a new technology quickly?" · "Tell me about a time you worked with something you did not know."

**বুঝে নিন:**
- STAR format-এ বলুন। কিন্তু মূল জিনিস হলো **পদ্ধতি**: official docs আর sample → ছোট prototype → আসল কাজ ছোট ছোট ধাপে → যে জানে তাকে দিয়ে review করানো।
- ছোট prototype দিয়ে কঠিন জায়গাগুলো আগেই ধরা পড়ে। এটা বলতে ভুলবেন না।
- ভালো উদাহরণ: প্রথমবার BLE, camera, নতুন native plugin, নতুন CI setup, নতুন Play policy মানা। Native Android-এ ফিরে আসাটাও একটা গল্প হতে পারে।

**Answer (English):**
> "In one project, we needed [Bluetooth Low Energy support], and I had not used it before. We had [two weeks]. First, I read the official docs and ran the official sample, so I understood the basic flow. Then I built a small prototype that only connected and read one value. It showed me the hard parts early, like permissions and reconnects. I asked a teammate to review my plan. Then I built the real feature step by step, with tests for the data parsing. We shipped on time. My method is simple: docs, a small prototype, then real code."

**Key words:** `official docs` · `small prototype` · `hard parts early` · `step by step`

**Follow-up:**
- **Q:** How do you know you understood it well enough?
  **A:** "When I can explain it simply to a teammate, and my prototype handles the error cases, not only the happy path."

**আরও দেখুন:** [H7 · Learning and staying up to date](#h7) · [N8 · Bluetooth Low Energy](#n8) · [H0-1 · Tell me about yourself](#h0-1)

---

### <a id="h15"></a>H15. ◆ How do you work in a remote team? How do you communicate across time zones?

**প্রশ্নটা মানে:** বাসা থেকে কাজ করলেও আপনার উপর ভরসা করা যায় কি না, আর আপনার যোগাযোগ পরিষ্কার কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "Have you worked remotely before?" · "How do you handle the time zone difference?"

**বুঝে নিন:**
- Remote-এ কেউ আপনার কাজ চোখে দেখে না। তাই লিখে জানাতে হয়: ticket update, পরিষ্কার PR description, ছোট daily update।
- প্রশ্ন এমনভাবে লিখুন যাতে এক message-এই উত্তর দেওয়া যায়: context, কী চেষ্টা করেছেন, কী চান।
- কয়েক ঘণ্টা overlap ঠিক রাখুন। Calendar-এ নিজের working hours দিয়ে রাখুন।
- Call-এর পরে কী ঠিক হলো, সেটা ছোট করে লিখে পাঠান।
- English-এ দুর্বল লাগলে: লেখার সময় একটু সময় নিন। Call-এ বলুন: "Let me summarize to make sure I understood."

**Answer (English):**
> "I have worked [remotely with teams in other time zones]. In remote work, people cannot see my work, so I make it visible. I update tickets, write clear pull request descriptions, and post a short daily update. I keep a few fixed overlap hours for calls. When I ask a question, I write the full context in one message — what I tried and what I need — so the other person can answer without a meeting. After a call, I send a short summary of what we decided. So everyone knows the same plan."

**Key words:** `make work visible` · `overlap hours` · `full context` · `written summary`

**Follow-up:**
- **Q:** What if you are blocked and the team is asleep?
  **A:** "I write the question clearly, so they see it in the morning. Meanwhile, I move to another task or work with a mock, so I do not lose the day."
- **Q:** How do you stay productive at home?
  **A:** "I keep fixed working hours, a quiet place, and a backup internet connection. I plan my day from the sprint board."

**আরও দেখুন:** [H0-5 · Client questions](#h0-5) · [H13 · Agile / Scrum](#h13) · [H5 · Working with other roles](#h5)

---

### <a id="h9"></a>H9. ★ Why are you leaving your current job?

**প্রশ্নটা মানে:** কোনো সমস্যা আছে কি না, আর আপনি পুরোনো কোম্পানিকে খারাপ বলেন কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "Why are you looking for a change?"

**বুঝে নিন:** পুরোনো কোম্পানি নিয়ে কখনো খারাপ কথা বলবেন না। সামনের দিকের কারণ বলুন: নতুন domain, native-এ গভীর কাজ, বড় product।

**Answer (English):**
> "I learned a lot in my current role, and I am thankful for it. Now I want to work deeper on native Android and on products that are close to the hardware, like cameras and sensors. This role gives me exactly that, so it feels like the right next step."

**Key words:** `thankful` · `next step` · `deeper native work`

**আরও দেখুন:** [H0-2 · Why native Android](#h0-2) · [H10 · 3–5 years](#h10)

---

### <a id="h10"></a>H10. ◆ Where do you see yourself in 3–5 years?

**প্রশ্নটা মানে:** আপনি কি কিছুদিন থাকবেন, আর বড় হতে চান কি না।
**অন্যভাবেও জিজ্ঞেস করে:** "What are your career goals?"

**বুঝে নিন:** এমন লক্ষ্য বলুন যেটা এই job-এর ভেতরেই পূরণ হয়। "নিজের company খুলব" বা "অন্য field-এ যাব" বলবেন না।

**Answer (English):**
> "I want to become a strong senior or lead Android engineer in this domain — someone the team trusts with the hard parts, like video, device security or the platform side. I also want to help other developers grow. I hope to do that here."

**Key words:** `senior or lead` · `hard parts` · `help others grow`

**আরও দেখুন:** [H9 · Why leaving](#h9) · [H8 · Mentoring](#h8)

---

### <a id="h11"></a>H11. ★ Salary, notice period and availability

**প্রশ্নটা মানে:** টাকা আর কবে যোগ দিতে পারবেন।
**অন্যভাবেও জিজ্ঞেস করে:** "What are your salary expectations?" · "When can you start?"

**বুঝে নিন:**
- Interview-এর আগে market দেখে একটা range ঠিক করে রাখুন।
- প্রথমে তাদের range জানতে চাওয়া ভদ্রতা। তারপর নিজের range বলুন। একটা সংখ্যার বদলে range।
- Remote job হলে মোট package (ছুটি, equipment, payment পদ্ধতি) জিজ্ঞেস করুন।

**Answer (English):**
> "I would like to know the range you have for this role first. Based on my experience and the market, I am looking for something in the range of [X to Y]. But I am flexible for the right role, and the whole package matters to me too. I can start in [N weeks] after the offer."

**Key words:** `range` · `flexible` · `whole package` · `notice period`

**Follow-up:**
- **Q:** What is your notice period? Can you join earlier?
  **A:** "My notice period is [N weeks]. I will try to make it shorter, but I want to finish my handover properly. I think you would expect the same from me."

**আরও দেখুন:** [H12 · Questions for us](#h12) · [H0-5 · Client questions](#h0-5)

---

### <a id="h12"></a>H12. ★ Do you have any questions for us?

**প্রশ্নটা মানে:** আপনি কতটা আগ্রহী আর কতটা ভেবে এসেছেন। **"No" বলা ভুল।**
**অন্যভাবেও জিজ্ঞেস করে:** "Anything you want to ask?"

**বুঝে নিন:** ২–৩টা প্রশ্ন বেছে নিন। Technical আর team দুই রকমই রাখুন। প্রথম interview-এ টাকা বা ছুটি নিয়ে প্রশ্ন করবেন না।

**জিজ্ঞেস করার মতো প্রশ্ন (English):**
- "What does the Android stack look like today — Compose or Views, and which architecture?"
- "What is the biggest technical challenge for the Android team right now?"
- "Do you build on your own custom Android devices, or on normal phones? How do you test on hardware?"
- "How do you handle security reviews — internal team or external pen tests?"
- "How do releases work — how often, and how do you roll out to devices?"
- "What would success look like for me in the first 3 months?"
- "How big is the team, and how do you work together — code reviews, standups?"

**আরও দেখুন:** [H0-4 · Our product](#h0-4) · [H11 · Salary and notice](#h11)

---

## <a id="last-day"></a>শেষ দিনের checklist — interview-এর আগের দিন আর সেদিন

**আগের দিন:**

1. [Tell me about yourself](#h0-1) জোরে ৩ বার বলুন। ৯০ সেকেন্ডের বেশি না।
2. নিচের [এক পাতার revision](#one-page)-এর প্রতিটা লাইন মুখে বলুন।
3. সব ★ প্রশ্নের শুধু **Key words** পড়ুন। প্রতিটা থেকে একটা বাক্য বানিয়ে বলুন।
4. তাদের app আর website আবার দেখুন। H12-এর ২–৩টা প্রশ্ন ঠিক করুন।
5. Remote interview হলে: camera, mic, internet, charger, শান্ত ঘর, পেছনে পরিষ্কার দেয়াল — সব পরীক্ষা করুন। Android Studio খুলে একটা project তৈরি রাখুন (live coding হতে পারে)।
6. তাড়াতাড়ি ঘুমান। শেষ রাতে নতুন কিছু পড়বেন না।

**সেদিন:**

1. ৩০ মিনিট আগে ৫টা ★ প্রশ্ন জোরে বলুন। গলা আর English দুটোই "warm" হবে।
2. পানি রাখুন। ধীরে বলুন।
3. প্রশ্ন না বুঝলে বলুন: "Sorry, could you repeat that, please?" এটা দুর্বলতা না।
4. না জানলে: "I have not used that in production, but here is how I would approach it ..."
5. শেষে ধন্যবাদ দিন। পরে একটা ছোট thank-you email পাঠান।

---

## <a id="one-page"></a>এক পাতার revision — interview-এর আগে এক নজরে

| বিষয় | মুখে বলার এক লাইন (English) |
|---|---|
| Null safety | "Types are non-null by default; I use `?.` and `?:`, and avoid `!!`." |
| Coroutine | "A coroutine suspends instead of blocking a thread, so one thread can run many of them." |
| Dispatchers | "Main for UI, IO for network and disk, Default for CPU work; I switch with `withContext`." |
| Structured concurrency | "Every coroutine lives in a scope; when the scope is cancelled, its children are cancelled too." |
| StateFlow vs SharedFlow | "StateFlow keeps the latest state; SharedFlow is for events with no current value." |
| Lifecycle | "Start and stop things in pairs: `onStart`/`onStop` for visible work." |
| Process death | "ViewModel survives rotation, not process death; I use SavedStateHandle for small state." |
| Background work | "WorkManager for work that can wait but must finish; a foreground service with the right type for long work the user can see." |
| Compose recomposition | "Compose re-runs only the composables whose inputs changed, and skips the rest." |
| State hoisting | "Keep composables stateless; move state up to the caller or the ViewModel." |
| Architecture | "UI → ViewModel → Repository → data sources; data flows down, events flow up." |
| Hilt | "Hilt gives constructor injection, with scopes that follow Android lifecycles." |
| Room | "Room checks SQL at compile time and gives Flow queries; I write and test migrations." |
| Token storage | "A key in the Android Keystore encrypts the token; EncryptedSharedPreferences is deprecated." |
| Network security | "TLS everywhere, no cleartext, pinning only with backup pins and a rotation plan." |
| Play Integrity | "The app gets a verdict, but my server checks it — never trust the client alone." |
| Camera | "CameraX for most apps; Camera2 for low-level control; no camera in the background." |
| Live video | "RTSP with Media3 on the LAN, WebRTC for low delay over the internet, HLS when a few seconds of delay is OK." |
| Camera grid | "Low-res substreams for the grid, main stream only in full screen, SurfaceView for video." |
| Sensors | "Register in onStart, unregister in onStop, use batching to save battery." |
| AOSP | "Build with envsetup, lunch and m; a priv-app needs an allowlist for privileged permissions." |
| SELinux | "Fix a denial with a proper policy rule, never by turning SELinux off." |
| Android 17 | "Apps targeting API 37 must ask for ACCESS_LOCAL_NETWORK to talk to LAN devices, like IP cameras." |
| Play target API | "Since 31 August 2026, new apps and updates must target API 36." |
| 16 KB pages | "On Google Play, apps with native code that target Android 15+ must support 16 KB pages." |
| Developer verification | "Since 30 September 2026, in Brazil, Indonesia, Singapore and Thailand, apps on certified devices must come from verified developers. It goes global in 2027. ADB installs and the advanced flow still work." |

---

---

## <a id="tracker"></a>অনুশীলনের খাতা — প্রশ্ন-তালিকা আর অগ্রগতি

এই তালিকায় শুধু English প্রশ্ন আছে। উত্তর নেই। এভাবে ব্যবহার করুন:

1. প্রশ্নটা জোরে পড়ুন। তারপর **না দেখে** ১ মিনিটে উত্তর বলুন।
2. পারলে বাক্সে টিক দিন (`[ ]` বদলে `[x]` করুন, বা কাগজে লিখে রাখুন)। না পারলে নামের link-এ গিয়ে আবার পড়ুন।
3. Mock interview-এর জন্য: এই তালিকা থেকে random প্রশ্ন বেছে নিন।
4. ৭ দিনের plan-এ শুধু ★ প্রশ্নগুলো ধরুন। দিনে প্রায় ১৭টা। ১০ দিনে ★ আর ◆। ১৫ দিনে সব।


**Part 0 — শুরুর প্রশ্ন: নিজের পরিচয় আর কেন Android**

- [ ] [H0-1. ★ Tell me about yourself.](#h0-1)
- [ ] [H0-2. ★ Why do you want to move to native Android?](#h0-2)
- [ ] [H0-3. ★ Why should we hire you over a pure native Android developer?](#h0-3)
- [ ] [H0-4. ★ What do you know about our product / domain?](#h0-4)
- [ ] [H0-5. ◆ Client questions (freelance / contract / foreign client)](#h0-5)
- [ ] [H0-6. ★ What are your strengths and weaknesses?](#h0-6)

**Part 1 — Kotlin, Coroutines আর Flow**

- [ ] [K1. ★ Why do Android teams use Kotlin and not Java? How does null safety work?](#k1)
- [ ] [K2. ★ What is the difference between val, var and const val? And lateinit vs by lazy?](#k2)
- [ ] [K3. ★ data class, sealed class / sealed interface, enum class, object and companion object — when do you use each?](#k3)
- [ ] [K4. ★ What are extension functions and scope functions (let, apply, run, also, with)?](#k4)
- [ ] [K5. ◆ Explain higher-order functions, lambdas, inline, noinline, crossinline and reified.](#k5)
- [ ] [K6. ○ Explain generics in Kotlin: in / out (variance) and star projection.](#k6)
- [ ] [K7. ◆ What is the difference between List and MutableList? And Collections vs Sequences?](#k7)
- [ ] [K27. ★ What is the difference between an interface and an abstract class in Kotlin? Why are classes final by default, and what do the visibility modifiers mean?](#k27)
- [ ] [K28. ◆ Where do you put helpers and constants: an object, a companion object, or top-level functions?](#k28)
- [ ] [K8. ★ What is a coroutine? How is it different from a thread? What does suspend mean?](#k8)
- [ ] [K9. ★ Explain Dispatchers (Main, IO, Default) and withContext. What is main-safety?](#k9)
- [ ] [K10. ★ What is the difference between launch and async? What are Job and Deferred?](#k10)
- [ ] [K11. ★ Explain structured concurrency: scopes, cancellation, SupervisorJob and exception handling.](#k11)
- [ ] [K12. ★ What is a cold Flow vs a hot Flow? Why do we use Flow and not LiveData now?](#k12)
- [ ] [K13. ★ What is the difference between StateFlow and SharedFlow? Explain stateIn / shareIn with SharingStarted.WhileSubscribed(5000).](#k13)
- [ ] [K14. ★ Which Flow operators do you use most? How do you collect a Flow safely in the UI?](#k14)
- [ ] [K15. ◆ What is the difference between Channels and Flow? How do you handle one-time UI events like navigation or a snackbar?](#k15)
- [ ] [K16. ◆ How do you make code thread-safe in Kotlin? Mutex, atomic types, @Volatile, synchronized, and a confined dispatcher.](#k16)
- [ ] [K17. ◆ Show how you build search-as-you-type with debounce and flatMapLatest, and explain it.](#k17)

**Part 1B — Kotlin আরও গভীরে**

- [ ] [K18. ★ How does a suspend function work inside?](#k18)
- [ ] [K19. ★ How do you turn a listener API into a Flow with callbackFlow?](#k19)
- [ ] [K20. ◆ How does delegation with `by` work in Kotlin?](#k20)
- [ ] [K21. ◆ What is a value class, and when does it help?](#k21)
- [ ] [K22. ★ Explain equality and data classes in Kotlin.](#k22)
- [ ] [K23. ◆ What do you need to know about Kotlin–Java interop?](#k23)
- [ ] [K24. ★ How do you model state and errors with sealed types?](#k24)
- [ ] [K25. ★ What is new in Kotlin 2.x?](#k25)
- [ ] [K26. ○ How do you test and debug coroutines?](#k26)

**Part 2 — Android-এর মূল জিনিস: component, lifecycle, permission, background কাজ**

- [ ] [C1. ★ What are the four main Android components?](#c1)
- [ ] [C2. ★ Can you explain the Activity lifecycle?](#c2)
- [ ] [C3. ★ What is special about the Fragment lifecycle, and why do we use viewLifecycleOwner?](#c3)
- [ ] [C19. ★ How do Fragments (or screens) talk to each other? Why not use direct references?](#c19)
- [ ] [C4. ★ What is the difference between a configuration change and process death? How do you keep state?](#c4)
- [ ] [C5. ★ What is the difference between explicit and implicit intents? What is a PendingIntent?](#c5)
- [ ] [C6. ◆ What are tasks and launch modes?](#c6)
- [ ] [C7. ★ What types of Services are there? What are foreground service types?](#c7)
- [ ] [C8. ◆ How do BroadcastReceivers work today?](#c8)
- [ ] [C9. ◆ What is a ContentProvider, and why do we need FileProvider?](#c9)
- [ ] [C10. ★ Which tool do you use for background work?](#c10)
- [ ] [C11. ★ What is Context? How do Context leaks happen?](#c11)
- [ ] [C12. ★ How does the main thread work (Looper, Handler, MessageQueue)? What is an ANR?](#c12)
- [ ] [C13. ★ How do runtime permissions work?](#c13)
- [ ] [C14. ◆ What are the AndroidManifest essentials?](#c14)
- [ ] [C15. ★ How do notifications and push messages work on modern Android?](#c15)
- [ ] [C16. ◆ What is the difference between deep links and Android App Links?](#c16)
- [ ] [C17. ◆ How does storage work on modern Android?](#c17)
- [ ] [C18. ◆ How does an app process start, and how does Android decide which process to kill?](#c18)

**Part 2B — Android framework-এর ভেতরে (internals)**

- [ ] [F1. ★ What happens when you tap an app icon?](#f1)
- [ ] [F2. ★ How does ART run your code? (DEX, JIT, AOT, Baseline Profiles)](#f2)
- [ ] [F3. ★ What is Binder, and why does Android use it?](#f3)
- [ ] [F4. ★ Parcelable vs Serializable — which and why?](#f4)
- [ ] [F5. ★ How is a frame drawn on Android, and where does jank come from?](#f5)
- [ ] [F6. ◆ What are Window, Surface, and SurfaceView vs TextureView?](#f6)
- [ ] [F7. ◆ How does Intent resolution work?](#f7)
- [ ] [F8. ◆ How are runtime permissions enforced?](#f8)
- [ ] [F9. ◆ How does memory work for an Android app?](#f9)
- [ ] [F10. ◆ What threads does an Android app have?](#f10)
- [ ] [F11. ★ How do system services work? (getSystemService to the HAL)](#f11)
- [ ] [F12. ★ What is new in Android development in 2025–2026?](#f12)
- [ ] [F13. ○ What does the Android platform security model look like?](#f13)

**Part 2C — Jetpack আর Android-এর basics**

- [ ] [J1. ★ What is Android Jetpack / AndroidX? Why use it instead of only framework APIs?](#j1)
- [ ] [J2. ★ Walk me through an Android project structure.](#j2)
- [ ] [J3. ★ What is the Application class? When do you use it, and what should not go there?](#j3)
- [ ] [J4. ★ How do lifecycle-aware components work? (Lifecycle, LifecycleOwner, DefaultLifecycleObserver, ProcessLifecycleOwner)](#j4)
- [ ] [J5. ★ How do you support old Android versions? (AppCompat, Compat classes, SDK_INT, @RequiresApi)](#j5)
- [ ] [J6. ◆ What are the basics of the View system? (View vs ViewGroup, layouts, ViewBinding, custom views)](#j6)
- [ ] [J7. ◆ How do resources and configuration qualifiers work?](#j7)
- [ ] [J8. ◆ Toast vs Snackbar vs Dialog vs notification — when do you use each?](#j8)
- [ ] [J9. ◆ What is the Activity Result API, and why did it replace startActivityForResult?](#j9)
- [ ] [J10. ◆ How do you use the App Startup library and the SplashScreen API?](#j10)
- [ ] [J11. ★ Which Jetpack libraries do you use in a new app today, and why?](#j11)
- [ ] [J12. ◆ Which Android Studio tools do you use every day?](#j12)
- [ ] [J13. ○ How do you build home screen widgets with Glance, and Quick Settings tiles?](#j13)

**Part 3 — Jetpack Compose আর UI**

- [ ] [U1. ★ What is Jetpack Compose, and why do teams move from XML Views to it?](#u1)
- [ ] [U2. ★ What is recomposition? How does Compose skip work, and what is stability?](#u2)
- [ ] [U3. ★ How do you handle state in Compose? (`remember`, `rememberSaveable`, state hoisting)](#u3)
- [ ] [U4. ★ What are side effects in Compose? When do you use each effect API?](#u4)
- [ ] [U5. ◆ What are `derivedStateOf` and `snapshotFlow`?](#u5)
- [ ] [U6. ★ How do you make a `LazyColumn` fast?](#u6)
- [ ] [U7. ◆ Why does Modifier order matter?](#u7)
- [ ] [U8. ★ How does navigation work in Compose?](#u8)
- [ ] [U9. ★ How do you connect Compose with a ViewModel?](#u9)
- [ ] [U10. ◆ How do you mix Compose and Views? (e.g. a video player or camera preview)](#u10)
- [ ] [U11. ◆ How do you find and fix Compose performance problems?](#u11)
- [ ] [U12. ○ How do you do theming in Compose? (Material 3, dynamic color, dark mode)](#u12)
- [ ] [U13. ★ What is edge-to-edge, how do you handle window insets, and what is predictive back?](#u13)
- [ ] [U14. ◆ How do you support large screens and foldables?](#u14)
- [ ] [U16. ★ dp vs sp vs px — how do you support different screen sizes and densities?](#u16)
- [ ] [U17. ◆ How do you make an app accessible, and how do you test it?](#u17)
- [ ] [U18. ◆ How do you localize an Android app? (strings, plurals, RTL, per-app language)](#u18)
- [ ] [U15. ◆ How do RecyclerView, ViewHolder and DiffUtil work? How does a View measure, lay out and draw?](#u15)

**Part 4 — Performance, debugging আর release**

- [ ] [P1. ★ What is an ANR? What causes it, and how do you find and fix it?](#p1)
- [ ] [P2. ★ What causes memory leaks on Android, and how do you find them?](#p2)
- [ ] [P3. ★ How do you make app startup faster?](#p3)
- [ ] [P4. ◆ How do you find and fix jank and frame drops?](#p4)
- [ ] [P5. ★ What does R8 do? How do keep rules and mapping files work?](#p5)
- [ ] [P6. ★ APK vs AAB? How does Play App Signing work, and what if you lose the upload key?](#p6)
- [ ] [P7. ◆ How do you save battery? (Doze, wake locks, standby buckets)](#p7)
- [ ] [P8. ★ How do you monitor crashes and ANRs in production?](#p8)
- [ ] [P9. ◆ How do you set up CI/CD for an Android app?](#p9)
- [ ] [P10. ★ How do you debug a production bug you cannot reproduce?](#p10)
- [ ] [P11. ★ What changed in recent Android versions (8 to 17)? What do minSdk, targetSdk and compileSdk mean?](#p11)
- [ ] [P12. ◆ Explain Gradle basics: build types, flavors, version catalogs, KSP vs kapt, and build speed.](#p12)
- [ ] [P13. ◆ Which static analysis tools do you use? (Android Lint, detekt, ktlint)](#p13)

**Part 5 — Architecture, data, network আর testing**

- [ ] [R1. ★ What goes in a ViewModel, and why does it survive screen rotation?](#r1)
- [ ] [R2. ★ What is MVI or unidirectional data flow? MVVM or MVI — which do you choose?](#r2)
- [ ] [R3. ★ Explain Clean Architecture layers. When is a use case class worth it?](#r3)
- [ ] [R4. ★ Explain the Repository pattern, single source of truth, and offline-first.](#r4)
- [ ] [R5. ★ How does dependency injection work with Hilt?](#r5)
- [ ] [R6. ◆ How do you split an app into modules?](#r6)
- [ ] [R7. ★ Explain Room: entities, DAOs, Flow queries, relations, transactions and migrations.](#r7)
- [ ] [R8. ★ DataStore or SharedPreferences? Preferences or Proto DataStore?](#r8)
- [ ] [R9. ★ How do you set up Retrofit and OkHttp? How do you refresh an expired token?](#r9)
- [ ] [R10. ★ How do you handle errors from the network to the UI?](#r10)
- [ ] [R19. ◆ How do you cache data and decide when it is stale?](#r19)
- [ ] [R11. ◆ How does Paging 3 work? When do you need RemoteMediator?](#r11)
- [ ] [R12. ◆ Coil or Glide? How do you avoid out-of-memory with images?](#r12)
- [ ] [R13. ◆ kotlinx.serialization, Moshi or Gson — which do you use?](#r13)
- [ ] [R14. ★ How do you unit test a ViewModel?](#r14)
- [ ] [R15. ◆ How do you write UI and integration tests? What is your test pyramid?](#r15)
- [ ] [R16. ◆ WebSocket, Server-Sent Events, MQTT or FCM — when do you use each?](#r16)
- [ ] [R17. ○ Which design patterns do you use in Android? Why are singletons dangerous?](#r17)
- [ ] [R18. ◆ Explain SOLID with Android examples.](#r18)
- [ ] [R20. ◆ Feature flags and remote config — how do you ship a feature safely?](#r20)

**Part 6 — Flutter থেকে native Android: সেতুর প্রশ্ন**

- [ ] [B1. ★ You are a Flutter developer. Why should we trust you with native Android work?](#b1)
- [ ] [B2. ★ Flutter or native Android — when do you choose native?](#b2)
- [ ] [B3. ★ How do platform channels work? How would you stream sensor data to Flutter?](#b3)
- [ ] [B4. ◆ What are FFI, NDK and JNI? When would you write C or C++?](#b4)
- [ ] [B5. ◆ How do you add Flutter screens to an existing native Android app?](#b5)
- [ ] [B6. ◆ Kotlin Multiplatform or Flutter — an honest comparison.](#b6)
- [ ] [B7. ◆ Map Flutter concepts to Android. How did you ramp up on native Android?](#b7)

**Part 7 — Security: কয়েক স্তরের নিরাপত্তা (multi-layer security)**

- [ ] [S1. ★ How do you secure an Android app?](#s1)
- [ ] [S17. ◆ What are the OWASP Mobile Top 10 risks?](#s17)
- [ ] [S2. ★ Where do you store tokens and secrets?](#s2)
- [ ] [S3. ◆ Can you explain the Android Keystore in depth?](#s3)
- [ ] [S4. ★ How do you build biometric login?](#s4)
- [ ] [S5. ★ How do you secure network traffic?](#s5)
- [ ] [S6. ★ How do you build login and auth securely?](#s6)
- [ ] [S7. ★ How do you detect root, tampering and emulators?](#s7)
- [ ] [S8. ◆ What can an attacker see in your APK?](#s8)
- [ ] [S9. ★ How do you secure app components?](#s9)
- [ ] [S10. ◆ How do you make a WebView safe?](#s10)
- [ ] [S11. ★ How do you protect data at rest and stop data leaks?](#s11)
- [ ] [S12. ◆ How do you secure IPC between your own apps or a system service?](#s12)
- [ ] [S13. ◆ What do you know about Android Enterprise and device management?](#s13)
- [ ] [S14. ◆ How do you test the security of an app?](#s14)
- [ ] [S15. ◆ How do you handle session security?](#s15)
- [ ] [S16. ○ How do you protect the software supply chain?](#s16)

**Part 8 — Security camera, video আর streaming**

- [ ] [V1. ★ CameraX or Camera2 — when do you use each?](#v1)
- [ ] [V2. ★ What are the rules for camera permissions and background camera use?](#v2)
- [ ] [V3. ★ How do you play a live stream from an IP camera?](#v3)
- [ ] [V4. ★ How do you show many camera feeds at once?](#v4)
- [ ] [V14. ◆ How do you take a snapshot or thumbnail from a live stream or video?](#v14)
- [ ] [V5. ★ How do you record video on the device?](#v5)
- [ ] [V6. ◆ Can you explain video encoding basics?](#v6)
- [ ] [V7. ◆ How do you find cameras on the local network?](#v7)
- [ ] [V8. ◆ How do you do motion detection and AI on the device?](#v8)
- [ ] [V9. ★ How do you send motion alert notifications?](#v9)
- [ ] [V10. ★ How do you secure camera streams and recordings?](#v10)
- [ ] [V11. ◆ How do you build a 24/7 monitoring or recording app?](#v11)
- [ ] [V12. ○ How do you build two-way audio?](#v12)
- [ ] [V13. ◆ How do you handle a bad network during streaming?](#v13)

**Part 9 — Custom Android OS (AOSP) আর platform**

- [ ] [O1. ★ What is AOSP, and how is it different from the Android on a Pixel or Samsung phone?](#o1)
- [ ] [O2. ★ Can you explain the Android platform layers, and how a call goes from an app to the hardware?](#o2)
- [ ] [O3. ★ How do you build AOSP and flash it on a device?](#o3)
- [ ] [O4. ★ What is the difference between a normal app, a system app, a privileged app and a platform-signed app?](#o4)
- [ ] [O5. ◆ How would you add a new system service or customise the framework?](#o5)
- [ ] [O6. ◆ What is a HAL, and what did Project Treble change? AIDL HAL vs HIDL?](#o6)
- [ ] [O7. ★ How does SELinux work on Android, and how do you fix an "avc: denied" error?](#o7)
- [ ] [O8. ◆ Can you explain the Android boot process? Where would you add custom startup?](#o8)
- [ ] [O9. ★ How do you build a kiosk or dedicated device? Can you do it without a custom ROM?](#o9)
- [ ] [O10. ★ How do you deliver OTA updates to your own devices?](#o10)
- [ ] [O11. ◆ What is verified boot (AVB) and why must test-keys never ship?](#o11)
- [ ] [O12. ★ How do you debug problems at the platform level?](#o12)
- [ ] [O16. ◆ What is ADB, and which ADB commands do you use most?](#o16)
- [ ] [O13. ◆ How would an app talk to custom hardware on your device?](#o13)
- [ ] [O14. ○ What are CTS, VTS and GMS certification? What changes if your device has no Google services?](#o14)
- [ ] [O15. ○ What is Android developer verification, and does it affect apps on your custom devices?](#o15)

**Part 10 — Sensor, location, Bluetooth আর IoT**

- [ ] [N1. ★ How do you read sensor data on Android?](#n1)
- [ ] [N2. ★ What is the difference between accelerometer, gyroscope and magnetometer? How do you get device orientation?](#n2)
- [ ] [N3. ★ How do you use sensors without killing the battery?](#n3)
- [ ] [N4. ★ How do you read sensors in the background? What limits does Android have?](#n4)
- [ ] [N5. ◆ How do you handle noisy sensor data?](#n5)
- [ ] [N6. ◆ What is the difference between the step counter and the step detector? Where do Activity Recognition and Health Connect fit?](#n6)
- [ ] [N7. ★ How do you get location on Android?](#n7)
- [ ] [N8. ★ How do you work with Bluetooth Low Energy devices on Android?](#n8)
- [ ] [N9. ◆ What is Companion Device Manager and why use it?](#n9)
- [ ] [N10. ◆ How do you talk to USB and serial devices from an Android app?](#n10)
- [ ] [N13. ○ How does NFC work on Android? Reading tags and Host Card Emulation](#n13)
- [ ] [N11. ◆ Which IoT protocol would you choose — MQTT, CoAP or HTTP/WebSocket? How do you keep MQTT alive on Android?](#n11)
- [ ] [N12. ◆ How do you test sensor and hardware code?](#n12)

**Part 11 — Mobile system design**

- [ ] [D1. ★ Design a security camera app](#d1)
- [ ] [D2. ★ Design an offline-first app that syncs with a server](#d2)
- [ ] [D3. ◆ Design a chat or real-time messaging feature](#d3)
- [ ] [D7. ◆ Design an image feed / gallery with caching and pagination](#d7)
- [ ] [D4. ◆ Design software for a fleet of custom Android devices](#d4)
- [ ] [D5. ◆ Design a large video/photo upload that survives app kill and bad network](#d5)
- [ ] [D6. ◆ Design a sensor data logger](#d6)

**Part 12 — Live coding round**

- [ ] [L1. ★ Warm-up: reverse words, check palindrome, count characters](#l1)
- [ ] [L2. ★ Two Sum with a HashMap](#l2)
- [ ] [L3. ★ Valid parentheses with a stack](#l3)
- [ ] [L4. ◆ LRU cache](#l4)
- [ ] [L5. ★ Debounced search in a ViewModel with Flow](#l5)
- [ ] [L6. ★ Fetch a list from an API and show loading / data / error in Compose](#l6)
- [ ] [L7. ◆ Run 3 network calls in parallel and combine; cancel all if one fails](#l7)
- [ ] [L11. ◆ Implement a simple retry with exponential backoff in Kotlin](#l11)
- [ ] [L8. ◆ Find the bug in Android code](#l8)
- [ ] [L9. ○ Thread-safe in-memory cache with Mutex](#l9)
- [ ] [L10. ○ Merge intervals (and group anagrams)](#l10)

**Part 13 — Behavioral, teamwork আর client-এর প্রশ্ন**

- [ ] [H1. ★ Tell me about a difficult bug you fixed.](#h1)
- [ ] [H2. ★ Tell me about a time you missed a deadline or were under pressure.](#h2)
- [ ] [H3. ★ Tell me about a disagreement with a teammate or lead.](#h3)
- [ ] [H4. ★ Tell me about a mistake you made.](#h4)
- [ ] [H5. ★ How do you work with designers, QA and backend developers?](#h5)
- [ ] [H6. ◆ How do you review code? How do you take review comments?](#h6)
- [ ] [H7. ◆ How do you learn new things and stay up to date?](#h7)
- [ ] [H8. ◆ Have you mentored or helped a junior developer?](#h8)
- [ ] [H13. ◆ How do you work in Agile / Scrum? (sprints, standups, estimates, demos)](#h13)
- [ ] [H14. ◆ Tell me about a time you had to learn something new very fast.](#h14)
- [ ] [H15. ◆ How do you work in a remote team? How do you communicate across time zones?](#h15)
- [ ] [H9. ★ Why are you leaving your current job?](#h9)
- [ ] [H10. ◆ Where do you see yourself in 3–5 years?](#h10)
- [ ] [H11. ★ Salary, notice period and availability](#h11)
- [ ] [H12. ★ Do you have any questions for us?](#h12)
