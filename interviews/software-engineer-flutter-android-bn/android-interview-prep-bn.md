# Android Interview Prep — Senior Engineer (বাংলা)

> **Senior Android / Mobile Engineer — Interview Prep**
> যিনি Flutter-এ senior, আর এখন **native Android (Kotlin)** interview দিতে চান — তাঁর জন্য।
> প্রতিটা উত্তর **স্বাভাবিক ভাষায়**, **Kotlin code সহ** লেখা, আর মুখে বলার উত্তর **বাংলা ও English** দুই ভাষাতেই। যেখানে কাজে লাগে, সেখানে **Flutter-এর সাথে মিল** দেখানো আছে — যাতে আপনার জানা জিনিসের উপর নতুনটা বসাতে পারেন।

---

## এই গাইড কীভাবে ব্যবহার করবেন

প্রতিটা প্রশ্নের গঠন একই রকম:

- **সংক্ষেপে** — জিনিসটা কী আর কেন আছে, কয়েক বাক্যে। Dart বা Flutter-এ মিল থাকলে সেটাও।
- **ব্যাখ্যা** — আগে সমস্যা, তারপর সমাধান। Code দিয়ে, আর নিয়মগুলোর পেছনের "কেন" সহ।
- **Interview-এ এভাবে বলুন** — মুখে বলার মতো উত্তর, *বাংলায়* আর *English*-এ। দুইটাতেই একই কথা, একই ক্রমে। মুখস্থ করবেন না। কথাগুলোর ক্রম আর মূল point ধরুন, তারপর নিজের ভাষায় বলুন।
- **সাধারণ ভুল** — যেখানে মানুষ সবচেয়ে বেশি আটকায়।
- **Follow-up প্রশ্ন** — interviewer পরের যে প্রশ্নটা করতে পারে, তার উত্তরও বাংলা আর English-এ।
- **উপরে ফিরুন** — সূচিপত্রে ফিরে যান।

প্রতিটা প্রশ্নে লেখা আছে সেটা কত ঘন ঘন আসে (**Very common / Common / Deeper**) আর কঠিনতা (**Easy / Medium / Hard**)।

---

## <a id="senior-voice"></a>Senior-এর মতো উত্তর কীভাবে দেবেন

একই জিনিস junior আর senior দুইজনেই জানে। পার্থক্য হয় **কীভাবে বলেন** তাতে। Senior উত্তরে চারটা জিনিস থাকে:

1. **এক লাইনে মূল কথা।** প্রথম বাক্যেই উত্তর দিন। ভূমিকা দেবেন না।
2. **ভেতরে কীভাবে কাজ করে।** একটা "কেন" বলুন। যেমন: "ViewModel বাঁচে, **কারণ** ViewModelStore নতুন Activity-কে দেওয়া হয়।"
3. **Trade-off বা ফাঁদ।** "এটা ভালো, কিন্তু..." — এটাই সবচেয়ে বড় senior signal।
4. **বাস্তব অভিজ্ঞতা।** "Production-এ আমি দেখেছি..." / "Code review-এ আমি খেয়াল রাখি..." / "আমি মেপে দেখেছি..."

তারপর **থামুন**। Interviewer চাইলে গভীরে যাবে। লম্বা করে বলা মানে বেশি জানা না — পরিষ্কার করে বলাটাই senior skill।

**যে কথাগুলো শুনলে senior মনে হয়:**

| Junior-এর মতো | Senior-এর মতো |
|---|---|
| "আমি সবসময় X ব্যবহার করি।" | "আমার default X, কারণ ... কিন্তু যদি ... হয়, তাহলে Y।" |
| "এটা best practice।" | "এটা এই সমস্যার সমাধান করে: ..." |
| "এটা দ্রুত।" | "আমি release build-এ Macrobenchmark দিয়ে মেপেছি, startup ২০% কমেছে।" |
| "জানি না।" | "আমি এটা production-এ ব্যবহার করিনি। কিন্তু আমার ধারণা এটা এভাবে কাজ করে, কারণ ... আমি এভাবে যাচাই করতাম: ..." |
| শুধু definition | Definition + কেন + কখন না + কীভাবে test/measure |

**কাজের কিছু শুরুর বাক্য:**

| বাংলায় | English |
|---|---|
| "ছোট করে বললে ... কারণটা হলো ..." | "The short answer is ... The reason is ..." |
| "আমার default হলো ..., তবে নির্ভর করে ...-এর উপর।" | "My default is ..., but it depends on ..." |
| "এখানে trade-off-টা হলো ..." | "The trade-off here is ..." |
| "Production-এ একটা ফাঁদ আমি দেখেছি ..." | "One pitfall I've seen in production is ..." |
| "আমি এটা ... দিয়ে মেপে নিশ্চিত হতাম।" | "I'd verify that by measuring ... with ..." |
| "এটা আমি production-এ ব্যবহার করিনি, তবে আমি এভাবে ভাবতাম ..." | "I haven't used that in production, but here's how I'd reason about it." |

> **সৎ থাকুন:** "Interview-এ এভাবে বলুন" অংশে "I've seen", "In my projects" জাতীয় বাক্য আছে। যেটা আপনি নিজে করেননি, সেটা নিজের অভিজ্ঞতা বলে বলবেন না। Senior interviewer follow-up দিয়ে সহজেই ধরে ফেলে। তখন "I'd do it this way" বলুন — এতেও সমান smart শোনায়।

> **সতর্কতা:** Android প্রতি বছর বদলায়। এই গাইডে Android 17 (API 37) পর্যন্ত behavior change আছে। Android 18 বা তার পরের পরিবর্তন interview-এর আগে [developer.android.com/about/versions](https://developer.android.com/about/versions) থেকে একবার দেখে নিন।

---

## এই গাইড দুই কাজে লাগে

1. **Senior Flutter job-এ Android প্রশ্ন।** Senior Flutter পদের circular-এ প্রায়ই Android আর iOS-এর native জ্ঞান চায়। Interview-এ তখন সাধারণ Android প্রশ্ন আসে: lifecycle, process death, background কাজ, permission, Gradle, release। এর জন্য নিচের **"আগে এগুলো"** list যথেষ্ট।
2. **আলাদা native Android interview।** তখন পুরো গাইড পড়ুন, [৪ সপ্তাহের পরিকল্পনা](#study-plan) অনুযায়ী।

Flutter-এর নিজের প্রশ্ন (platform channel, Pigeon, add-to-app, Flutter-এর system design) এখানে নেই। সেগুলো আছে [Flutter interview guide](../software-engineer-flutter-bn/section-00-toc-cheatsheet-bn.md)-এ। এখানে শুধু Android।

### Senior Flutter interview-এর জন্য — আগে এগুলো (প্রায় ১ সপ্তাহ)

| Priority | প্রশ্ন | কেন আসে |
|---|---|---|
| ১ | [Q17 Activity lifecycle](#q17) · [Q19 Process death](#q19) | App-এর lifecycle আর state restore — সব mobile app-এর ভিত্তি |
| ১ | [Q24 Main thread আর ANR](#q24) · [Q23 Context leak](#q23) | Platform channel আর plugin লেখার সময় লাগে |
| ১ | [Q53 Permission](#q53) · [Q21 Foreground service](#q21) · [Q42 Background কাজ](#q42) | Flutter-এর background কাজ শেষে native-এ গিয়ে আটকায় |
| ২ | [Q20 Intent, launch mode](#q20) · [Q55 Deep link](#q55) | Notification tap আর deep link-এর bug |
| ২ | [Q50 Gradle](#q50) · [Q51 R8](#q51) · [Q52 Release](#q52) | Release build crash, flavor, signing |
| ২ | [Q9–Q12 Coroutine](#q9) · [Q1–Q3 Kotlin](#q1) | Native plugin code পড়তে আর লিখতে |
| ২ | [Q67 Notification আর FCM](#q67) | Push notification প্রায় সব app-এ আছে |
| ৩ | [Q54 Security](#q54) · [Q47 Startup](#q47) · [Q48 Size](#q48) | Senior level-এ আসে |
| ৩ | [Q65 Mutex আর shared state](#q65) · [Q68 Accessibility](#q68) | Senior level-এ আসে |
| ৪ | Compose, Hilt, Room (D, E, F) | শুধু native Android role-এর জন্য |

> iOS-এর জন্য একই রকম একটা আলাদা গাইড পরে বানানো যায় (UIApplication lifecycle, AppDelegate/SceneDelegate, Info.plist, signing, background mode)।

---

## Android interview-এ সাধারণত কী কী round হয়

| Round | কী দেখে | এই গাইডের কোন অংশ |
|---|---|---|
| **Kotlin + Android fundamentals** | Kotlin, coroutines, lifecycle, Compose — মুখে প্রশ্ন-উত্তর | A, B, C, D |
| **Architecture / deep dive** | MVVM/MVI, DI, modularization, আপনার আগের project | E, F |
| **Live coding (Android)** | ৪৫–৬০ মিনিটে একটা ছোট screen: API থেকে list দেখানো | [Q63](#q63) |
| **Live coding (DSA)** | Array, string, hashmap, tree — Kotlin-এ | [Q63](#q63) + repo-র DSA guide |
| **Take-home** | ২–৪ দিনে ছোট app, সাথে test | E, F, J |
| **Mobile system design** | "একটা chat app / feed app design করুন" | L |
| **Behavioral** | Conflict, ownership, mentoring, ভুল থেকে শেখা | [Flutter guide-এর Section 22](../software-engineer-flutter-bn/section-22-leadership-behavioral-bn.md) |

**Remote কোম্পানি** সাধারণত system design আর take-home-এ বেশি জোর দেয়। **BD কোম্পানি** সাধারণত fundamentals আর live coding-এ বেশি প্রশ্ন করে। দুটোর জন্যই প্রস্তুত থাকুন।

---

## Flutter থেকে Android — এক নজরে মিল

আপনি অর্ধেক পথ আগেই হেঁটে এসেছেন। Compose-এর চিন্তা প্রায় Flutter-এর মতো।

| Flutter | Android (Kotlin) | মন্তব্য |
|---|---|---|
| Dart | Kotlin | দুটোই null-safe। Kotlin-এ `?.`, `?:`, `!!` প্রায় একই |
| `Future` / `async-await` | `suspend` function / coroutine | coroutine-এ structured concurrency আছে, Dart-এ নেই |
| `Stream` | `Flow` | Flow default-এ **cold** |
| `ValueNotifier` / `BehaviorSubject` | `StateFlow` | সবসময় একটা current value থাকে |
| `Isolate` | `Dispatchers.Default` / thread | Kotlin-এ shared memory, Isolate-এ নেই |
| Widget | `@Composable` function | দুটোই declarative |
| `StatefulWidget` + `setState` | `remember { mutableStateOf() }` | |
| `initState` / `dispose` | `LaunchedEffect` / `DisposableEffect` | |
| `InheritedWidget` / `Provider` | `CompositionLocal` / Hilt | |
| Bloc / Cubit / Riverpod Notifier | `ViewModel` + `StateFlow` | |
| `get_it` | Koin (runtime) | |
| `injectable` (codegen) | Hilt / Dagger (compile-time) | |
| `go_router` | Navigation Compose | |
| `sqflite` / `drift` | Room | |
| `shared_preferences` | DataStore | |
| `dio` + interceptor | Retrofit + OkHttp interceptor | |
| `workmanager` plugin | WorkManager | plugin টা আসলে এটাই call করে |
| `flutter_test` / `mocktail` | JUnit + MockK / fake | |
| Flavors | Product flavors + build types | একই ধারণা |
| `pubspec.yaml` | `build.gradle.kts` + `libs.versions.toml` | |

---

## <a id="study-plan"></a>৪ সপ্তাহের পড়ার পরিকল্পনা

একটা পর্যায় তখনই শেষ ধরবেন, যখন না দেখে **সংক্ষিপ্ত উত্তর** বলতে পারবেন আর code লিখতে পারবেন।

**সপ্তাহ ১ — ভাষা আর async (সবচেয়ে বেশি প্রশ্ন এখান থেকে)।**
→ A. Kotlin ([Q1](#q1)–[Q8](#q8)) · B. Coroutines আর Flow ([Q9](#q9)–[Q16](#q16))
→ প্রতিদিন Kotlin-এ ২টা DSA সমস্যা।

**সপ্তাহ ২ — Android-এর ভিত্তি আর Compose।**
→ C. Core components ([Q17](#q17)–[Q24](#q24)) · D. Compose ([Q25](#q25)–[Q32](#q32))
→ একটা ছোট Compose app বানান (list + detail)।

**সপ্তাহ ৩ — Architecture, data, performance।**
→ E ([Q33](#q33)–[Q38](#q38)) · F ([Q39](#q39)–[Q44](#q44)) · G ([Q45](#q45)–[Q49](#q49))
→ সপ্তাহ ২-এর app-এ Hilt, Room, Retrofit, test যোগ করুন। এটাই আপনার take-home practice।

**সপ্তাহ ৪ — Build, security, test, system design, mock interview।**
→ H, I, J, K ([Q50](#q50)–[Q58](#q58)) · L. System design ([Q59](#q59)–[Q61](#q61)) · M ([Q62](#q62)–[Q63](#q63)) · N ([Q64](#q64)–[Q69](#q69))
→ ২টা mock interview দিন (বন্ধু বা AI দিয়ে)। জোরে জোরে উত্তর বলুন।
→ শেষ রাতে: [Cheat Sheet](#cheatsheet)।

---

## <a id="toc"></a>সূচিপত্র

**A. Kotlin ভাষা**
1. [Null safety, `lateinit` vs `lazy`](#q1) · *Very common*
2. [`data class`, `sealed`, `enum`, `object`](#q2) · *Very common*
3. [Extension function আর scope function](#q3) · *Very common*
4. [`inline`, `crossinline`, `noinline`, `reified`](#q4) · *Common*
5. [Generics: `in`, `out`, variance](#q5) · *Common*
6. [Collection vs Sequence](#q6) · *Common*
7. [Delegation (`by`) আর `value class`](#q7) · *Common*
8. [Kotlin-এর ছোট ছোট দ্রুত প্রশ্ন](#q8) · *Very common*

**B. Coroutines আর Flow**
9. [Coroutine কী, `suspend` ভেতরে কীভাবে কাজ করে](#q9) · *Very common*
10. [Dispatchers, `withContext`, main-safety](#q10) · *Very common*
11. [Structured concurrency, Job, SupervisorJob, scope](#q11) · *Very common*
12. [Coroutine-এ exception handling](#q12) · *Very common*
13. [Cancellation](#q13) · *Common*
14. [Flow, StateFlow, SharedFlow, Channel, LiveData](#q14) · *Very common*
15. [Flow operator: `flatMapLatest`, `combine`, `stateIn`](#q15) · *Common*
16. [UI-তে Flow নিরাপদে collect করা](#q16) · *Very common*

**C. Android-এর মূল component**
17. [Activity lifecycle আর configuration change](#q17) · *Very common*
18. [Fragment lifecycle আর `viewLifecycleOwner`](#q18) · *Common*
19. [Process death আর state restore](#q19) · *Very common*
20. [Intent, task, launch mode, PendingIntent](#q20) · *Common*
21. [Service, foreground service, background limit](#q21) · *Common*
22. [BroadcastReceiver আর ContentProvider](#q22) · *Common*
23. [Context-এর ধরন আর leak](#q23) · *Very common*
24. [Main thread, Looper, Handler, ANR](#q24) · *Common*

**D. Jetpack Compose**
25. [Compose ভেতরে কীভাবে কাজ করে](#q25) · *Very common*
26. [State, `remember`, state hoisting, UDF](#q26) · *Very common*
27. [Side effect API](#q27) · *Very common*
28. [Stability, skipping, strong skipping](#q28) · *Common · Hard*
29. [Compose performance](#q29) · *Common*
30. [Modifier order আর CompositionLocal](#q30) · *Common*
31. [View আর Compose একসাথে (interop, migration)](#q31) · *Common*
32. [Navigation Compose](#q32) · *Common*

**E. Architecture**
33. [MVVM vs MVI, UiState, one-off event](#q33) · *Very common*
34. [Google-এর recommended architecture](#q34) · *Very common*
35. [ViewModel ভেতরে কীভাবে বাঁচে](#q35) · *Common*
36. [Dependency Injection: Hilt, Dagger, Koin](#q36) · *Very common*
37. [Modularization](#q37) · *Common*
38. [Clean Architecture আর UseCase — কখন দরকার](#q38) · *Common*

**F. Data, network, background কাজ**
39. [Retrofit + OkHttp, interceptor, token refresh](#q39) · *Very common*
40. [Room আর DataStore](#q40) · *Very common*
41. [Offline-first আর Paging 3](#q41) · *Common*
42. [Background কাজ: WorkManager, FGS, AlarmManager](#q42) · *Very common*
43. [JSON serialization: kotlinx, Moshi, Gson](#q43) · *Common*
44. [Image loading আর bitmap memory](#q44) · *Common*

**G. Performance আর memory**
45. [Memory leak আর LeakCanary](#q45) · *Very common*
46. [Jank আর ANR খুঁজে বের করা](#q46) · *Common*
47. [App startup দ্রুত করা, Baseline Profile](#q47) · *Common*
48. [App size কমানো](#q48) · *Common*
49. [Battery: Doze আর App Standby](#q49) · *Deeper*

**H. Build আর release**
50. [Gradle, KSP, version catalog, flavor](#q50) · *Common*
51. [R8 / ProGuard](#q51) · *Common*
52. [Signing, Play release, targetSdk policy](#q52) · *Common*
53. [Runtime permission](#q53) · *Very common*

**I. Security**
54. [Data আর network security](#q54) · *Common*
55. [Component, WebView, deep link security](#q55) · *Deeper*

**J. Testing**
56. [ViewModel, coroutine, Flow-এর unit test](#q56) · *Very common*
57. [UI test, Robolectric, screenshot test](#q57) · *Common*

**K. Android version**
58. [সাম্প্রতিক Android version-এর বড় পরিবর্তন](#q58) · *Common*

**L. Mobile system design**
59. [System design interview-এর কাঠামো](#q59) · *Very common*
60. [উদাহরণ: offline-first feed app](#q60) · *Very common*
61. [উদাহরণ: chat app](#q61) · *Common*

**M. শেষ ধাপ**
62. [Native vs cross-platform — Android interviewer আপনার background নিয়ে যা জিজ্ঞেস করবে](#q62) · *Very common*
63. [Live coding round: পুরো সমাধান](#q63) · *Very common*

**N. আরও যা senior interview-এ আসে**
64. [RecyclerView, ListAdapter, DiffUtil](#q64) · *Very common (native)*
65. [Shared mutable state, Mutex, Flow backpressure](#q65) · *Common · Hard*
66. [Custom View আর Compose custom layout](#q66) · *Common*
67. [Notification আর FCM — গভীরে](#q67) · *Very common*
68. [Accessibility](#q68) · *Common*
69. [দ্রুত প্রশ্ন: Parcelable, Binder, animation, Credential Manager](#q69) · *Common*

**দ্রুত link:** [Senior-এর মতো উত্তর](#senior-voice) · [পড়ার পরিকল্পনা](#study-plan) · [Cheat Sheet](#cheatsheet) · [Interviewer-কে কী জিজ্ঞেস করবেন](#ask-them) · [ভালো resource](#resources)

---

# A. Kotlin ভাষা

### <a id="q1"></a>Q1. Null safety, `lateinit` আর `lazy` — আসলে কী?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy

**সংক্ষেপে:** Dart-এর sound null safety-র মতোই Kotlin-এ nullability type-এর অংশ। `String` কখনো null হবে না, `String?` হতে পারে। `lateinit` আর `lazy` দুটোই compiler-কে বলে "value পরে আসবে"। পার্থক্য হলো value কে দেয়। `lateinit`-এ আপনি নিজে পরে assign করেন। `lazy`-তে একটা block থাকে, যেটা প্রথমবার পড়ার সময় একবার চলে, তারপর result রেখে দেয়।

---

#### Null safety — Dart থেকে এলে প্রায় সবই চেনা

```kotlin
val name: String = "Rahim"     // non-null
val nick: String? = null       // nullable

nick.length          // compile error — null হলে কী হবে, বলেননি
nick?.length         // safe call: null হলে পুরো expression null
nick?.length ?: 0    // Elvis: বাম দিক null হলে ডান দিক
nick!!.length        // "null না, আমি জানি" — ভুল হলে NullPointerException
```

Dart-এর সাথে মিলিয়ে নিন: `?.` একই। Kotlin-এর `?:` হলো Dart-এর `??`। Kotlin-এর `!!` হলো Dart-এর `!`।

একটা বড় পার্থক্য আছে: **Java interop।** Java code-এ nullability-র তথ্য নেই। তাই Java থেকে আসা value-কে Kotlin "platform type" (`String!`) ধরে। মানে Kotlin check করে না, দায়িত্ব আপনার। Android SDK-র অনেক API এখনো Java-তে লেখা, তাই এটা বাস্তবে প্রায়ই সামনে আসে। Dart-এ এই ঝামেলা নেই।

---

#### সমস্যাটা কোথায়

Kotlin-এ non-null property-তে object তৈরির সময়েই value দিতে হয়। কিন্তু Android-এ Activity-র constructor আপনি চালান না, system চালায়। আসল setup হয় পরে, `onCreate()`-এ। তাই `binding` বা inject করা dependency, constructor-এর সময় হাতে থাকে না।

Nullable করে দিলে কাজ চলে। কিন্তু তখন প্রতিটা ব্যবহারে `binding?.` বা `binding!!` লিখতে হয়। এটা noise, আর আসল ভুল লুকিয়ে ফেলে। এই জায়গাতেই `lateinit` আর `lazy` আসে।

---

#### `lateinit` — "আমি পরে assign করব"

এটা Dart-এর `late String name;`-এর মতো। আপনি compiler-কে কথা দিচ্ছেন যে ব্যবহারের আগে value দেবেন।

```kotlin
class ProfileActivity : AppCompatActivity() {

    private lateinit var binding: ActivityProfileBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityProfileBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.name.text = "Rahim"     // ?. লাগছে না — type non-null
    }
}
```

ভেতরে যা হয়: backing field শুরুতে null থাকে। প্রতিটা read-এ getter check করে। Field null হলে throw করে `UninitializedPropertyAccessException`। Dart-এ একই ভুলে আসে `LateInitializationError`।

নিয়মগুলো, কারণসহ:
- **শুধু `var`।** পরে assign করতে হয়, তাই `val` হবে না।
- **Primitive (`Int`, `Boolean`) চলে না।** "এখনো set হয়নি" বোঝাতে field-এ null রাখা হয়। কিন্তু JVM-এর primitive null রাখতে পারে না।
- **Nullable type-এও চলে না।** `lateinit var x: String?` অর্থহীন, কারণ null তো এখানে "set হয়নি"-র চিহ্ন।
- Set হয়েছে কি না জানতে: `::binding.isInitialized`। তবে এটা বারবার লাগলে design আরেকবার দেখুন।

কোথায় দেখবেন: Activity-র `binding`, Hilt-এর field injection (`@Inject lateinit var`), test-এর `@Before`-এ set করা object।

---

#### `lazy` — "প্রথমবার লাগলে বানাও, তারপর রেখে দাও"

এটা Dart-এর `late final formatter = DateFormat(...);`-এর মতো। Initializer-সহ `late` field-ও প্রথম read-এ একবার চলে।

```kotlin
class ReportScreen {

    private val formatter by lazy {
        println("formatter তৈরি হচ্ছে")
        DateTimeFormatter.ofPattern("dd MMM yyyy")
    }

    fun show(date: LocalDate) = formatter.format(date)
}

val screen = ReportScreen()   // block এখনো চলেনি
screen.show(today)            // প্রথম read → block চলল → print হলো
screen.show(tomorrow)         // cache করা value → আর print হয় না
```

`by` keyword মানে property delegation। Property-র getter-এর কাজ আপনি `Lazy` object-কে দিয়ে দিচ্ছেন। প্রথম `get`-এ সে block চালায় আর result রেখে দেয়। পরের সব `get`-এ রাখা value-টাই ফেরত দেয়।

যা জানা দরকার:
- **শুধু `val`।** Value একবার তৈরি হয়, পরে বদলায় না।
- **Default-এ thread-safe** (`SYNCHRONIZED`)। দুইটা thread একসাথে প্রথমবার পড়লেও block একবারই চলে।
- **কাজে লাগে** যেখানে object বানাতে খরচ আছে, কিন্তু সবসময় লাগে না। যেমন formatter, `Regex`, বড় config। দরকার না হলে খরচটাই হয় না।
- Android-এ আপনি এটা না জেনেই ব্যবহার করছেন: `private val viewModel: MainViewModel by viewModels()`। এটাও একটা lazy delegate। ViewModel তৈরি হয় প্রথম access-এ।

---

#### কখন কোনটা

- Value **বাইরে থেকে আসে**, আর কখন আসবে তা lifecycle ঠিক করে (`onCreate()`, DI, test setup)। তাহলে `lateinit`।
- Value আপনি **নিজেই বানাতে পারেন**, শুধু দেরিতে বানাতে চান। তাহলে `lazy`।

| | `lateinit` | `lazy` |
|---|---|---|
| Value কে দেয়? | আপনি, পরে assign করে | `lazy` block, প্রথম read-এ |
| `var` / `val` | `var` | `val` |
| পরে বদলানো যায়? | হ্যাঁ | না |
| Set হওয়ার আগে read করলে | Exception | সমস্যা নেই, তখনই তৈরি হয় |
| Primitive চলে? | না | হ্যাঁ |
| Thread-safe? | না | হ্যাঁ (default) |
| Dart-এ সমতুল্য | `late T x;` | `late final x = ...;` |

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Kotlin-এ nullability type-এরই অংশ। `String` কখনো null হবে না, `String?` হতে পারে। তাই বেশিরভাগ null-এর ভুল compile time-এই ধরা পড়ে। কোথাও `!!` লাগলে আমি সেটাকে সতর্ক সংকেত ধরি — সাধারণত তার মানে model-টাই ঠিকমতো বানানো হয়নি।
>
> Value দেরিতে দেওয়ার দুইটা উপায় আছে। Value বাইরে থেকে এলে, যেমন DI বা `onCreate()` থেকে, আমি `lateinit` নিই। আর read-only value, যেটা বানাতে খরচ আছে, সেটার জন্য `by lazy` — প্রথমবার লাগলে একবার তৈরি হয়, তারপর সেটাই থাকে।
>
> একটা জায়গায় আমি সবসময় সাবধান থাকি: Java থেকে আসা platform type। Kotlin সেটা check করতে পারে না, তাই Java থেকে value ঢোকার জায়গাতেই আমি null handle করে ফেলি।

*English:*
> In Kotlin, nullability is part of the type. A `String` is never null, a `String?` can be, so most null bugs become compile errors. If I need `!!` somewhere, I take it as a warning sign — usually the model is wrong.
>
> For values that come later, I have two tools. When something outside sets the value, like DI or `onCreate()`, I use `lateinit`. For a read-only value that is expensive to build, I use `by lazy` — it's created once on first use and then cached.
>
> One place I'm always careful is platform types from Java. Kotlin can't check them, so I handle null right where the value enters from Java.

**সাধারণ ভুল:**
- `!!` দিয়ে compiler-কে চুপ করানো। Crash-টা তখন শুধু পরে সরে যায়।
- Fragment-এ `lateinit var binding` রাখা। `lateinit`-কে আবার "খালি" করা যায় না, তাই `onDestroyView()`-এ পুরনো view ছেড়ে দেওয়া যায় না। ফলে binding পুরনো view ধরে রাখে, আর সেটা leak হয় ([Q18](#q18))। Fragment-এ nullable `_binding` রেখে `onDestroyView()`-এ `null` করুন।
- `lazy` block-এ Activity বা View capture করা। যে object `lazy` ধরে আছে, সেটা Activity-র চেয়ে বেশিদিন বাঁচলে Activity-ও memory-তে আটকে থাকে ([Q23](#q23))।

**Follow-up প্রশ্ন:** "`lazy` কি সবসময় thread-safe?"

*বাংলায়:*
> Default-এ হ্যাঁ। Mode হলো `SYNCHRONIZED` — একটা thread block চালায়, বাকিরা অপেক্ষা করে, তাই value একবারই তৈরি হয়। আমি নিশ্চিত হলে যে শুধু main thread পড়বে, তখন `LazyThreadSafetyMode.NONE` দিই, তাতে lock-এর খরচটা বাঁচে।

*English:*
> By default, yes. The mode is `SYNCHRONIZED` — one thread runs the block and the others wait, so the value is built once. If I'm sure only the main thread reads it, I use `LazyThreadSafetyMode.NONE` to skip the lock.

[উপরে ফিরুন](#toc)

---

### <a id="q2"></a>Q2. `data class`, `sealed class/interface`, `enum`, `object` — কোনটা কখন?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** চারটাই data বা state model করার tool, কিন্তু কাজ আলাদা।
- `data class` value রাখার class। Compiler নিজে `equals`, `hashCode`, `toString`, `copy` বানিয়ে দেয়। Dart-এ যেটা `freezed` দিয়ে করতেন, সেটা এখানে built-in।
- `sealed` এমন একটা type, যার সব subtype compiler আগে থেকে জানে। তাই `when`-এ সব case handle হয়েছে কি না, compiler নিজেই check করে।
- `enum` হলো কয়েকটা নির্দিষ্ট value, যাদের সবার গঠন একই।
- `object` হলো singleton, মানে পুরো app-এ একটাই instance।

---

#### `data class` — value-এর মতো আচরণ করা class

```kotlin
data class User(val id: String, val name: String) {
    var lastSeen: Long = 0            // body-তে — equals/hashCode-এ ধরা হবে না
}

val a = User("1", "Rahim")
val b = a.copy(name = "Karim")        // নতুন object, id একই থাকল
a == User("1", "Rahim")               // true — content দিয়ে তুলনা, reference দিয়ে না
```

খেয়াল করার মতো দুইটা জিনিস:
- **শুধু primary constructor-এর property** দিয়ে `equals`, `hashCode`, `toString` তৈরি হয়। Body-তে লেখা `lastSeen` এগুলোতে নেই। তাই দুইটা `User`-এর `lastSeen` আলাদা হলেও তারা "equal"।
- **`copy()` shallow।** ভেতরে `MutableList` থাকলে, নতুন আর পুরনো object একই list শেয়ার করে। একটায় বদলালে অন্যটাতেও বদলায়। তাই data class-এ `val` আর read-only `List` রাখুন।

---

#### `sealed` — বন্ধ একটা family

সাধারণ interface যে কেউ যেকোনো জায়গা থেকে implement করতে পারে। তাই compiler কখনো জানে না, মোট কয়টা subtype আছে। `sealed` হলে সব subtype একই module আর package-এ থাকতে হয়। ফলে compiler পুরো তালিকা জানে।

এর সবচেয়ে বড় লাভ হলো **exhaustive `when`**:

```kotlin
sealed interface UiState {
    data object Loading : UiState
    data class Success(val users: List<User>) : UiState
    data class Error(val message: String) : UiState
}

fun render(state: UiState) = when (state) {   // else লাগে না
    UiState.Loading -> showSpinner()
    is UiState.Success -> showList(state.users)   // smart cast — state.users সরাসরি পাওয়া যায়
    is UiState.Error -> showError(state.message)
}
```

পরে কেউ `data object Empty : UiState` যোগ করলে, যত জায়গায় `when (state)` আছে, সব জায়গায় compile error আসবে। Compiler নিজেই দেখিয়ে দেয় কোথায় কোথায় নতুন case handle করতে হবে। `else` রাখলে এই সুবিধাটা হারিয়ে যায়।

এটা ঠিক Dart 3-এর `sealed class` আর `switch` pattern matching-এর মতো।

**`sealed class` না `sealed interface`?** এখন সাধারণত `sealed interface` বেশি পছন্দ করা হয়। কারণ একটা class একাধিক interface implement করতে পারে, কিন্তু একটাই class extend করতে পারে। সব case-এ common state বা constructor parameter লাগলে তখন `sealed class` নিন।

---

#### `enum` না `sealed`?

- সব value-এর গঠন একই, আর প্রতিটার একটাই instance। তাহলে `enum`। যেমন `Theme.LIGHT`, `Theme.DARK`। Enum-এ `entries` দিয়ে সব value-এর list পাওয়া যায়, আর `name` দিয়ে save করা যায়।
- প্রতিটা case আলাদা data রাখে (`Success`-এ list, `Error`-এ message)। তাহলে `sealed`।

---

#### `object`, `data object`, `companion object`

| | কী |
|---|---|
| `object` | Singleton। প্রথম access-এ তৈরি হয়, আর JVM class loading-এর কারণে thread-safe ভাবে তৈরি হয়। |
| `data object` | Sealed family-র ভেতরে data ছাড়া case-এর জন্য (`Loading`)। এটা পড়ার মতো `toString()` দেয়, `"UiState$Loading@1a2b"`-এর বদলে `"Loading"` (Kotlin 1.9+)। |
| `companion object` | Class-এর সাথে যুক্ত একটা object। Java বা Dart-এর `static`-এর জায়গায় বসে। Factory function আর constant রাখতে ব্যবহার হয়। |

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> সাধারণ value রাখার জন্য আমি `data class` নিই — `equals`, `hashCode`, `copy` compiler নিজেই বানিয়ে দেয়। আর যেখানে state-এর একটা নির্দিষ্ট তালিকা আছে, যেমন UI state বা API result, সেখানে `sealed interface`।
>
> Sealed-এর সবচেয়ে বড় লাভ হলো exhaustive `when`। কেউ নতুন state যোগ করলে compiler নিজেই দেখিয়ে দেয় কোথায় কোথায় handle করতে হবে। তাই ওখানে আমি `else` রাখি না।
>
> Enum নিই যখন সব value-এর গঠন একই। প্রতিটা case আলাদা data রাখলে তখন sealed। আর একটা জিনিস খেয়াল রাখি: `copy()` shallow, তাই data class-এ `val` আর read-only collection রাখি।

*English:*
> I use data classes for plain values — the compiler gives me `equals`, `hashCode` and `copy`. For a closed set of states, like UI state or results, I use a sealed interface.
>
> The big win of sealed types is an exhaustive `when`. When someone adds a new state, the compiler shows every place that must handle it, so I don't add an `else` there.
>
> Enum is for fixed values with the same shape; sealed is for cases that carry different data. One thing I watch: `copy()` is shallow, so I keep data classes immutable, with `val` and read-only collections.

**সাধারণ ভুল:**
- Sealed type-এর `when`-এ `else` রাখা। নতুন case যোগ হলে compiler তখন আর কিছু বলে না।
- Data class-কে `HashMap`-এর key বা `HashSet`-এ রেখে পরে তার `var` field বদলানো। `hashCode` বদলে যায়, তাই object আর খুঁজে পাওয়া যায় না।

**Follow-up প্রশ্ন:** "`object` কি thread-safe?"

*বাংলায়:*
> তৈরি হওয়াটা thread-safe, কারণ JVM class initialize করার সময় lock নেয়। কিন্তু `object`-এর ভেতরের mutable state নিজে থেকে safe না — সেটা আমাকে `Mutex` বা `StateFlow` দিয়ে রক্ষা করতে হয় ([Q65](#q65))।

*English:*
> Creating it is thread-safe, because the JVM locks during class initialization. But mutable state inside the `object` isn't safe by itself — I protect it with a `Mutex` or a `StateFlow`.

[উপরে ফিরুন](#toc)

---

### <a id="q3"></a>Q3. Extension function আর scope function (`let`, `run`, `with`, `apply`, `also`)

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy

**সংক্ষেপে:** Extension function দিয়ে কোনো class-এর code না ছুঁয়েই তাতে নতুন function যোগ করা যায়। Dart-এর `extension ... on String`-এর মতোই। এটা statically resolve হয়, মানে কোন function চলবে সেটা ঠিক হয় variable-এর declared type দেখে, runtime type দেখে না। Scope function পাঁচটা, কিন্তু পার্থক্য মাত্র দুইটা প্রশ্নে: block-এর ভেতরে object-কে `this` বলে ডাকবেন না `it`, আর শেষে object নিজে ফেরত আসবে না lambda-র result।

---

#### Extension function — class না বদলে helper যোগ করা

```kotlin
fun String.isValidEmail(): Boolean =
    Patterns.EMAIL_ADDRESS.matcher(this).matches()
```

`String` class আপনার না, তবু `"a@b.com".isValidEmail()` লেখা যাচ্ছে। ভেতরে `this` হলো যে `String`-এর উপর call হয়েছে।

---

#### "Statically resolve" মানে কী

```kotlin
open class Shape
class Circle : Shape()

fun Shape.name() = "Shape"
fun Circle.name() = "Circle"

val s: Shape = Circle()
println(s.name())   // "Shape" — কারণ s-এর declared type Shape
```

Object আসলে `Circle`, তবু `"Shape"` print হলো। কারণটা বুঝলে বাকি নিয়ম নিজেই বোঝা যায়।

Extension আসলে একটা static function, যার প্রথম parameter হলো receiver (যে object-এর উপর call হচ্ছে)। মানে `s.name()` ভেতরে হয়ে যায় `name(s)`। Static function বাছাই হয় compile time-এ, declared type দেখে। এর দুইটা ফল:
- **Override হয় না।** Subclass-এর extension থাকলেও runtime-এ সেটা বাছাই হয় না।
- **Private member পড়তে পারে না।** এটা class-এর বাইরের একটা সাধারণ function মাত্র।

Dart-এর extension method-ও একইভাবে static type দেখে চলে, তাই এই আচরণ আপনার চেনা।

---

#### Scope function — দুইটা প্রশ্নেই পার্থক্য

| Function | ভেতরে object | কী ফেরত দেয় | সাধারণ ব্যবহার |
|---|---|---|---|
| `let` | `it` | lambda-র result | null check: `user?.let { show(it) }` |
| `run` | `this` | lambda-র result | object নিয়ে কিছু হিসাব করে result নেওয়া |
| `with(x)` | `this` | lambda-র result | extension নয়; একটা object-এর অনেক কিছু পড়া |
| `apply` | `this` | object নিজে | object configure করা (builder-এর মতো) |
| `also` | `it` | object নিজে | পাশের কাজ: log, validation |

```kotlin
// apply — object configure করে সেটাই ফেরত দেয়
val intent = Intent(context, DetailActivity::class.java).apply {
    putExtra("id", id)
    flags = Intent.FLAG_ACTIVITY_SINGLE_TOP
}

// also — মূল value বদলায় না, শুধু পাশে একটা কাজ করে
val user = repository.load(id)
    .also { Log.d(TAG, "loaded ${it.id}") }
```

বাছাই করার সহজ উপায়:
- Object বানিয়ে তার field set করবেন? `apply`। Dart-এর cascade (`..`)-এর অনেকটা কাছাকাছি।
- Value না বদলে log বা check করবেন? `also`।
- Nullable value থাকলে তবেই কিছু করবেন? `?.let`।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Extension দিয়ে আমি class না ছুঁয়ে ছোট, focused helper যোগ করি। তবে মাথায় রাখি যে এটা statically resolve হয়। ভেতরে এটা একটা static function মাত্র, তাই কিছু override করে না, আর private member-ও দেখতে পায় না।
>
> Scope function বাছি দুইটা জিনিস দেখে: ভেতরে object `this` না `it`, আর শেষে object ফেরত চাই না lambda-র result। বাস্তবে object configure করতে `apply`, logging-এর মতো পাশের কাজে `also`, আর null check-এ `let` নিই।
>
> এগুলো আমি একটার ভেতরে আরেকটা দিই না। দুই স্তর পার হলেই code পড়া কঠিন হয়ে যায়।

*English:*
> Extensions let me add small, focused helpers without touching a class. But they are resolved statically — under the hood it's just a static function — so they don't override anything and can't see private members.
>
> For scope functions I decide by two things: is the object `this` or `it`, and do I return the object or the lambda result. In practice I use `apply` to configure objects, `also` for side effects like logging, and `let` for null checks.
>
> I don't nest them, because readability drops fast.

**সাধারণ ভুল:**
- একটার ভেতরে আরেকটা scope function (`let`-এর ভেতরে `apply`-এর ভেতরে `run`)। পড়া কঠিন হয়, আর কোন `this` বা কোন `it` কাকে বোঝাচ্ছে, গুলিয়ে যায়। দুই স্তরের বেশি হলে সাধারণ variable ব্যবহার করুন।

**Follow-up প্রশ্ন:** "`?.let {}` আর `if (x != null)` — কোনটা ভালো?"

*বাংলায়:*
> সাধারণ check-এ আমি `if` নিই, ওটাই বেশি পরিষ্কার। তবে class-এর mutable (`var`) property-তে `?.let` কাজে লাগে। ওখানে smart cast কাজ করে না, কারণ check আর ব্যবহারের মাঝে অন্য thread মান বদলে দিতে পারে। Local `var`-এ smart cast চলে, যদি কোনো lambda সেটা বদলে না দেয়।

*English:*
> For a simple check, I use `if` — it's clearer. `?.let` is useful on a class's mutable `var` property, because smart cast doesn't work there: another thread could change the value between the check and the use. On a local `var`, smart cast works, as long as no lambda changes it.

[উপরে ফিরুন](#toc)

---

### <a id="q4"></a>Q4. `inline`, `crossinline`, `noinline`, `reified` কী?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** `inline` function-এর body আর তার lambda, যেখানে call করা হয় সেখানে copy হয়ে বসে যায়। ফলে lambda-র জন্য আলাদা object তৈরি হয় না। আর lambda-র ভেতর থেকে বাইরের function-এ `return` করা যায় (non-local return)। `reified` দিয়ে runtime-এ generic type পাওয়া যায়, তবে এটা শুধু `inline` function-এ কাজ করে। `noinline` আর `crossinline` হলো inline-এর দুইটা ব্যতিক্রম।

---

#### সমস্যাটা কোথায়

সাধারণ higher-order function-এ (যে function lambda নেয়) প্রতিটা lambda একটা object, যেমন `Function1`। Loop-এর ভেতরে হাজার বার call হলে হাজারটা object তৈরি হয়। `inline` এটা বন্ধ করে, কারণ lambda-র code সরাসরি call-এর জায়গায় বসে যায়, object লাগে না।

```kotlin
inline fun <T> measure(tag: String, block: () -> T): T {
    val start = System.nanoTime()
    return block().also { Log.d(tag, "took ${System.nanoTime() - start} ns") }
}
```

Code copy হয় বলে একটা বাড়তি সুবিধাও আসে: lambda-র ভেতরে `return` লিখলে বাইরের function থেকেই বের হয়ে যায়। একে বলে non-local return।

---

#### `noinline` আর `crossinline` — কখন inline পুরোপুরি চলে না

- **`noinline`** — কোনো একটা lambda-কে inline করবেন না। দরকার হয় যখন lambda-টা কোথাও রেখে দিতে চান, যেমন field-এ রাখা বা অন্য function-এ পাঠানো। Copy হয়ে গেলে রাখার মতো কোনো object থাকে না, তাই এখানে object-টাই লাগে।
- **`crossinline`** — lambda inline হবে, কিন্তু তার ভেতর থেকে non-local `return` করা যাবে না। দরকার হয় যখন lambda-টা অন্য একটা context-এ চলে, যেমন `Runnable` বা অন্য lambda-র ভেতরে। ওই lambda পরে অন্য সময়ে চলবে, তখন বাইরের function অনেক আগেই শেষ। তাই সেখান থেকে "বাইরের function-এ return" করার কোনো মানে থাকে না।

```kotlin
inline fun runOnUi(crossinline action: () -> Unit) {
    handler.post { action() }     // অন্য lambda-র ভেতরে, তাই crossinline লাগবে
}
```

---

#### `reified` — type erasure-এর সমাধান

JVM-এ runtime-এ generic type মুছে যায় (একে বলে type erasure)। `List<String>` আর `List<Int>` runtime-এ একই। তাই সাধারণ function-এ `T::class` লেখা যায় না। `inline` + `reified` দিলে compiler প্রতিটা call-এর জায়গায় আসল type বসিয়ে দেয়।

```kotlin
inline fun <reified T : Activity> Context.start() {
    startActivity(Intent(this, T::class.java))
}

context.start<SettingsActivity>()
```

`reified` কেন শুধু `inline`-এ চলে? কারণ code call-এর জায়গায় copy হয় বলেই compiler সেখানে আসল type লিখে দিতে পারে। Copy না হলে সেই সুযোগ নেই।

**Flutter-এর সাথে মিল:** Dart-এর generic runtime-এ থাকে (reified), তাই Dart-এ এই সমস্যা নেই। Kotlin-এ এটা JVM-এর সীমাবদ্ধতা, আর `reified` তার সমাধান।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> `inline` function-এর body আর তার lambda call-এর জায়গায় copy হয়ে যায়। তাই lambda-র জন্য কোনো object তৈরি হয় না, আর আমি non-local return করতে পারি। এজন্যই বেশিরভাগ collection operator inline।
>
> `reified` শুধু inline-এর সাথে চলে। এটা runtime-এ আসল generic type দেয়, মানে type erasure-এর সমাধান। যেমন activity চালানোর জন্য typed `start<T>()`।
>
> Inline function আমি ছোট রাখি। Code প্রতিটা call-এ copy হয়, তাই বড় function inline করলে binary বড় হয়ে যায়।

*English:*
> `inline` copies the function body and its lambdas into the call site, so there is no lambda allocation and I can use non-local returns. That's why most collection operators are inline.
>
> `reified` only works with inline and gives me the real generic type at runtime, which solves type erasure — for example a typed `start<T>()` for activities.
>
> I keep inline functions small, because the code is copied at every call site and the binary grows.

**সাধারণ ভুল:**
- বড় function-কে `inline` করা। Code প্রতিটা call-এ copy হয়, তাই APK বড় হয়, অথচ lambda না থাকলে লাভও প্রায় নেই। শুধু ছোট, lambda নেওয়া function `inline` করুন।

**Follow-up প্রশ্ন:** "Kotlin standard library-র কোন function inline?"

*বাংলায়:*
> `let`, `apply`, `map`, `filter`, `forEach` — প্রায় সব collection function। এর একটা ফল আছে, যেটা আমি খেয়াল রাখি: `forEach`-এর ভেতরে `return` লিখলে পুরো function থেকে বের হয়ে যায়। শুধু lambda থেকে বের হতে চাইলে `return@forEach` লিখি।

*English:*
> `let`, `apply`, `map`, `filter`, `forEach` — almost all collection functions. One effect I watch for: a `return` inside `forEach` exits the whole function. To leave only the lambda, I write `return@forEach`.

[উপরে ফিরুন](#toc)

---

### <a id="q5"></a>Q5. Generics-এ `in`, `out` (variance) কী?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** Variance একটা প্রশ্নের উত্তর দেয়: `Box<String>`-কে কি `Box<Any>`-এর জায়গায় দেওয়া যায়? `out T` মানে class-টা শুধু T **দেয়** (producer)। তাই `List<String>`-কে `List<Any>` হিসেবে ব্যবহার করা যায়। একে বলে covariant। `in T` মানে class-টা শুধু T **নেয়** (consumer)। তাই `Comparator<Any>`-কে `Comparator<String>`-এর জায়গায় দেওয়া যায়। একে বলে contravariant। কোনোটাই না থাকলে type invariant — যেমন `MutableList<String>` কখনোই `MutableList<Any>` না।

---

#### `out` আর `in` — কেন safe

মনে রাখার সহজ নিয়ম — **PECS**: Producer `out`, Consumer `in`।

```kotlin
interface Source<out T> { fun next(): T }        // শুধু দেয়
interface Sink<in T> { fun put(item: T) }         // শুধু নেয়

val strings: Source<String> = ...
val anys: Source<Any> = strings                  // ঠিক আছে, String তো Any

val anySink: Sink<Any> = ...
val stringSink: Sink<String> = anySink           // ঠিক আছে, যে Any নেয় সে String-ও নিতে পারে
```

- `Source<String>` শুধু `String` দেয়। যে `Any` আশা করে, সে `String` পেলে কোনো সমস্যা নেই।
- `Sink<Any>` যেকোনো কিছু নিতে পারে। তাই যে শুধু `String` পাঠাবে, তার জন্য এটা নিরাপদ।

---

#### `MutableList` কেন invariant

`MutableList` একসাথে দেয় আর নেয়। যদি `MutableList<String>`-কে `MutableList<Any>` বলা যেত, তাহলে কেউ তাতে `Int` ঢুকিয়ে দিতে পারত। তখন যে code ওই list থেকে `String` আশা করে, সে crash করত। তাই compiler দুই দিকের কোনোটাতেই যেতে দেয় না।

---

#### Use-site variance আর star projection

Class নিজে invariant, কিন্তু একটা function-এ আপনি শুধু পড়বেন। তখন সেই parameter-এ `out` লিখে দিন:

```kotlin
fun copy(from: Array<out Any>, to: Array<Any>) { ... }
```

`from` থেকে শুধু পড়া হবে, তাই এখানে `Array<String>`-ও পাঠানো যায়।

**Star projection `List<*>`:** মানে "কোনো একটা type-এর list, কোনটা জানি না।" পড়লে `Any?` পাবেন, কিন্তু লিখতে পারবেন না, কারণ আসল type জানা নেই।

**Flutter-এর সাথে মিল:** Dart-এর generics default-এ covariant, আর check করে runtime-এ। এই কারণে Dart-এ `List<Object> x = <String>[]; x.add(1);` runtime-এ crash করে। Kotlin এই ভুলটা compile time-এই আটকায়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Variance একটা প্রশ্নের উত্তর দেয়: `Box<String>`-কে কি `Box<Any>`-এর জায়গায় দেওয়া যায়? `out` থাকলে type শুধু value দেয়, তাই সেটা covariant আর safe। এজন্যই `List<String>` একটা `List<Any>`। `in` থাকলে type শুধু value নেয়, তাই contravariant, যেমন `Comparator`।
>
> Mutable collection invariant, কারণ তা না হলে ভুল type ঢুকিয়ে দেওয়া যেত। আমি এটা PECS দিয়ে মনে রাখি: producer `out`, consumer `in`।

*English:*
> Variance answers one question: can a `Box<String>` be used where a `Box<Any>` is expected? With `out`, the type only produces values, so it's covariant and safe — that's why `List<String>` is a `List<Any>`. With `in`, it only consumes values, so it's contravariant, like a `Comparator`.
>
> Mutable collections are invariant, because otherwise you could insert the wrong type. I remember it as PECS: producer out, consumer in.

**Follow-up প্রশ্ন:** "Generic type runtime-এ কেন পাওয়া যায় না?"

*বাংলায়:*
> JVM type erasure-এর কারণে — runtime-এ generic type মুছে যায়। আমি দুইভাবে এটা সামলাই: `inline` function-এ `reified` ([Q4](#q4)), অথবা `Class<T>` parameter হিসেবে পাঠিয়ে।

*English:*
> Because of type erasure on the JVM. I solve it with `reified` in an inline function, or by passing a `Class<T>` parameter.

[উপরে ফিরুন](#toc)

---

### <a id="q6"></a>Q6. Collection আর Sequence-এর পার্থক্য কী?

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** Collection-এর operator **eager** — প্রতিটা ধাপ পুরো list-এর উপর চলে, আর প্রতি ধাপে একটা নতুন list বানায়। Sequence **lazy** — একটা element সব ধাপ পার হয়, তারপর পরেরটা আসে, মাঝখানে কোনো list বানায় না। বড় data আর লম্বা chain-এ, বিশেষ করে `first()` বা `take()` থাকলে, Sequence ভালো। ছোট list-এ Collection-ই দ্রুত। Dart-এর `Iterable` অনেকটা Sequence-এর মতো।

---

#### একই কাজ, দুইভাবে

```kotlin
val result = (1..1_000_000)
    .map { it * 2 }          // ১০ লাখ element-এর নতুন list
    .filter { it % 3 == 0 }  // আবার নতুন list
    .first()                 // শুধু একটা দরকার ছিল!

val fast = (1..1_000_000).asSequence()
    .map { it * 2 }
    .filter { it % 3 == 0 }
    .first()                 // মাত্র ৩টা element process হয়েই থেমে যায়
```

প্রথমটায় দশ লাখ element-এর উপর `map` চলে, তারপর আবার দশ লাখের উপর `filter`। অথচ দরকার ছিল একটাই।

দ্বিতীয়টায় `1` আসে, `map` হয়ে `2`, `filter`-এ বাদ। তারপর `2` আসে, `4` হয়, বাদ। তারপর `3` আসে, `6` হয়, পাস করে, আর `first()` সাথে সাথে থামিয়ে দেয়।

আরেকটা কথা: Sequence-এ terminal operation (`toList`, `first`, `sum`-এর মতো যেটা আসল result চায়) না আসা পর্যন্ত কিছুই চলে না।

---

#### তুলনা

| | Collection | Sequence |
|---|---|---|
| কখন চলে | সাথে সাথে | terminal operation (`toList`, `first`, `sum`) এ |
| ক্রম | ধাপ ধরে ধরে (সব map, তারপর সব filter) | element ধরে ধরে |
| মাঝখানের list | প্রতিটা ধাপে | নেই |
| কখন ভালো | ছোট data, ১–২ ধাপ | বড় data, অনেক ধাপ, আগে থামার সম্ভাবনা |

**Flutter-এর সাথে মিল:** Dart-এর `Iterable` (`where`, `map`) default-এ lazy — অনেকটা Kotlin Sequence-এর মতো। Dart-এ `.toList()` দিয়ে eager করেন। Kotlin-এ উল্টো: default eager, `asSequence()` দিয়ে lazy।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Collection eager — প্রতিটা ধাপ পুরো list-এর উপর চলে আর একটা নতুন list বানায়। Sequence lazy — প্রতিটা element পুরো chain পার হয়, আর terminal operation না আসা পর্যন্ত কিছুই চলে না।
>
> তাই বড় data, লম্বা chain, বা `first`/`take` দিয়ে আগে থামলে Sequence সময় আর memory দুটোই বাঁচায়। কিন্তু ছোট list-এ সাধারণ collection-ই সাধারণত দ্রুত। তাই আমি default-এ Sequence-এ যাই না, দরকার হলে আগে মেপে দেখি।

*English:*
> Collections are eager: each step runs over the whole list and creates a new list. Sequences are lazy: each element goes through the whole chain, and nothing runs until a terminal operation.
>
> So for large data, long chains, or when I stop early with `first` or `take`, sequences save time and memory. For small lists, plain collections are usually faster, so I don't switch by default — I measure when it matters.

**সাধারণ ভুল:**
- সব জায়গায় Sequence ব্যবহার করা। ছোট list-এ Sequence-এর নিজস্ব overhead আছে, তাই উল্টো ধীর হয়।

**Follow-up প্রশ্ন:** "Sequence আর Flow-এর পার্থক্য?"

*বাংলায়:*
> দুটোই lazy। পার্থক্য হলো Sequence synchronous, আর Flow `suspend` করতে পারে, মানে async কাজ করতে পারে।

*English:*
> Both are lazy. A Sequence is synchronous; a Flow can suspend, so it handles async work.

[উপরে ফিরুন](#toc)

---

### <a id="q7"></a>Q7. Delegation (`by`) আর `value class`

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** `by` দুই জায়গায় কাজ করে। **Class delegation**-এ একটা interface-এর কাজ অন্য একটা object-কে দিয়ে দেওয়া হয় — inheritance ছাড়াই composition। **Property delegation**-এ property-র get/set অন্য একটা object করে, যেমন `by lazy`, `by viewModels()`, Compose-এ `by remember`। আর `value class` হলো একটা value-এর চারপাশে type-safe wrapper, যার runtime-এ প্রায় কোনো খরচ নেই। Dart-এর extension type এর কাছের জিনিস।

---

#### Class delegation — শুধু যা বদলাতে চান, সেটাই লিখুন

ধরুন `MutableList`-এর শুধু `add`-এ log চান। Inheritance দিয়ে করতে গেলে একটা নির্দিষ্ট list class extend করতে হয়। আর হাতে লিখে forward করতে গেলে interface-এর সব method লিখতে হয়। `by inner` বললে বাকি সব method compiler নিজেই `inner`-এর কাছে পাঠিয়ে দেয়।

```kotlin
// Class delegation — শুধু যা বদলাতে চান সেটা override করুন
class LoggingList<T>(private val inner: MutableList<T>) : MutableList<T> by inner {
    override fun add(element: T): Boolean {
        Log.d("List", "add $element")
        return inner.add(element)
    }
}
```

---

#### Property delegation — Android-এ রোজ দেখেন

এখানে property-র getter (আর `var` হলে setter) আরেকটা object-এর হাতে থাকে। সে ঠিক করে value কোথা থেকে আসবে আর কীভাবে রাখা হবে।

```kotlin
// Property delegation — Android-এ রোজ দেখবেন
class HomeFragment : Fragment() {
    private val viewModel: HomeViewModel by viewModels()
    private val shared: CartViewModel by activityViewModels()
}

@Composable
fun Counter() {
    var count by remember { mutableIntStateOf(0) }   // getValue/setValue delegate
}

// Observable delegate — প্রতিটা পরিবর্তনে callback
var query: String by Delegates.observable("") { _, old, new ->
    Log.d("Search", "$old -> $new")
}
```

---

#### `value class` — দুইটা id যেন গুলিয়ে না যায়

দুইটা id-ই যদি সাধারণ `String` হয়, তাহলে ভুল করে উল্টো ক্রমে পাঠালেও compiler কিছু বলে না। `value class` দিয়ে প্রতিটাকে আলাদা type বানানো যায়।

```kotlin
@JvmInline
value class UserId(val value: String)

@JvmInline
value class OrderId(val value: String)

fun loadOrder(user: UserId, order: OrderId) { ... }
// loadOrder(orderId, userId) → compile error। ভুল জায়গায় ভুল id দেওয়া যায় না।
```

খরচের দিক: runtime-এ এটা সাধারণত শুধু `String` হিসেবেই থাকে, আলাদা object হয় না। কিন্তু nullable হলে, generic-এ রাখলে, বা interface হিসেবে পাঠালে box হয়, মানে আসল object তৈরি হয়।

**Interviewer কেন জিজ্ঞেস করে:** "Composition over inheritance" আপনি বাস্তবে জানেন কি না।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Kotlin-এ `by` দিয়ে delegation language-এর ভেতরেই পাওয়া যায়। Class delegation-এ আমি একটা interface implement করি অন্য object-এর কাছে forward করে, আর শুধু যেটা দরকার সেটা override করি — inheritance-এর বদলে composition।
>
> Property delegate দিয়ে চলে এমন জিনিস আমি রোজ ব্যবহার করি, যেমন `by lazy`, `by viewModels()`, `by remember`।
>
> Domain id-এর জন্য আমি value class পছন্দ করি। তাহলে `OrderId`-এর জায়গায় ভুল করে `UserId` পাঠানো যায় না, আর runtime-এ খরচ প্রায় নেই।

*English:*
> Kotlin's `by` gives me delegation as a language feature. Class delegation lets me implement an interface by forwarding to another object and override only what I need — composition instead of inheritance.
>
> Property delegates power things I use every day, like `by lazy`, `by viewModels()` and `by remember`.
>
> For domain ids I like value classes, so a `UserId` can't be passed where an `OrderId` is expected, with almost no runtime cost.

**Follow-up প্রশ্ন:** "নিজের property delegate কীভাবে বানাবেন?"

*বাংলায়:*
> `ReadOnlyProperty` বা `ReadWriteProperty` implement করি। অথবা সরাসরি `operator fun getValue(thisRef, property)` লিখি — `var` হলে সাথে `setValue`-ও।

*English:*
> I implement `ReadOnlyProperty` or `ReadWriteProperty`, or I write an `operator fun getValue(thisRef, property)` directly — plus `setValue` for a `var`.

[উপরে ফিরুন](#toc)

---

### <a id="q8"></a>Q8. Kotlin-এর ছোট ছোট দ্রুত প্রশ্ন

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy

**সংক্ষেপে:** Interview-এর শুরুতে এগুলো দ্রুত জিজ্ঞেস করে। লম্বা ব্যাখ্যা চায় না, চায় এক-দুই লাইনের পরিষ্কার উত্তর। নিচে প্রতিটার ছোট ব্যাখ্যা আর মুখে বলার উত্তর দেওয়া আছে। যেখানে Dart-এ একই জিনিস আছে, সেটাও বলা আছে, তাতে মনে রাখা সহজ।

---

#### `==` vs `===`

`==` ভেতরে `equals()` call করে, মানে value তুলনা। `===` দেখে দুইটা একই object কি না, মানে reference তুলনা। Dart-এ `==` আর `identical()`।

*বাংলায়:*
> `==` হলো `equals()`, value তুলনা করে। `===` দেখে দুইটা একই object কি না।

*English:*
> `==` calls `equals()`, so it compares values. `===` checks if both are the same object.

#### `val` vs `const val`

`val` একবার set হয়, কিন্তু runtime-এ। `const val` হলো compile time constant — value code-এর ভেতরেই বসে যায়। তাই এটা শুধু primitive আর `String` হতে পারে, আর থাকতে হয় top-level-এ বা `object`-এর ভেতরে। Dart-এর `final` আর `const`-এর পার্থক্যের মতোই।

*বাংলায়:*
> `val` runtime-এ একবার set হয়। `const val` compile time constant — শুধু primitive আর `String`, আর থাকতে হয় top-level বা `object`-এর ভেতরে।

*English:*
> `val` is set once at runtime. `const val` is a compile-time constant — only primitives and `String`, at top level or inside an `object`.

#### Class default-এ কী?

Kotlin-এ class default-এ `final`। কেউ inherit করুক চাইলে `open` লিখতে হয়। Dart-এ উল্টো — class default-এ extend করা যায়।

*বাংলায়:*
> Default-এ `final`। Inherit করতে দিতে চাইলে আমাকে `open` লিখতে হয়।

*English:*
> Classes are `final` by default. To allow inheritance, I mark them `open`.

#### `internal`

`internal` জিনিস শুধু একই Gradle module-এর ভেতরে দেখা যায়। Module-এর বাইরে শুধু public API দেখাতে চাইলে এটাই কাজে লাগে, তাই modularization-এ খুব দরকারি।

*বাংলায়:*
> `internal` মানে শুধু একই Gradle module-এর ভেতরে দেখা যায়। Modularization-এ আমি এটা দিয়ে module-এর ভেতরের code লুকিয়ে রাখি।

*English:*
> `internal` means visible only inside the same Gradle module. I use it a lot in modular apps to hide a module's internals.

#### `Unit` vs `Nothing`

`Unit` মানে function কিছু ফেরত দেয় না, Java-র `void`-এর মতো। `Nothing` মানে function কখনো ফেরতই আসে না — সবসময় throw করে, বা অনন্ত loop চালায়। `TODO()`-এর type `Nothing`। Dart-এ এটা `Never`।

*বাংলায়:*
> `Unit` মানে কিছু ফেরত দেয় না, Java-র `void`-এর মতো। `Nothing` মানে কখনো ফেরতই আসে না, যেমন সবসময় throw করে। `TODO()`-এর type `Nothing`।

*English:*
> `Unit` means it returns nothing useful, like Java's `void`. `Nothing` means it never returns — it always throws or loops forever. `TODO()` returns `Nothing`.

#### `Any` vs `Any?`

সব non-null type-এর parent হলো `Any`। আর null সহ সব type-এর parent হলো `Any?`। Dart-এর `Object` আর `Object?`-এর মতো।

*বাংলায়:*
> `Any` হলো সব non-null type-এর parent। `Any?` হলো সব type-এর parent, null সহ।

*English:*
> `Any` is the parent of all non-null types. `Any?` is the parent of every type, including null.

#### `@JvmStatic`, `@JvmOverloads`, `@JvmField`

তিনটাই Java থেকে Kotlin code সুন্দরভাবে call করার জন্য। `@JvmStatic` companion-এর function-কে Java-তে সত্যিকারের static method বানায়। `@JvmField` property-কে getter/setter ছাড়া সরাসরি field হিসেবে দেখায়। `@JvmOverloads` default parameter থেকে Java-র জন্য আলাদা আলাদা overload বানায় — custom View constructor-এ এটা লাগে।

*বাংলায়:*
> এগুলো Java থেকে Kotlin code সুন্দরভাবে call করার জন্য। সবচেয়ে বেশি লাগে `@JvmOverloads` — default parameter থেকে overload বানায়, যেমন custom View-এর constructor-এ।

*English:*
> They make Kotlin code nicer to call from Java. The one I use most is `@JvmOverloads`: it generates overloads from default parameters, for example in custom View constructors.

#### `typealias`

`typealias` শুধু একটা নতুন নাম দেয়, নতুন type বানায় না। তাই `typealias UserId = String` দিলেও যেকোনো `String` সেখানে চলে যায়। Type safety চাইলে `value class` ([Q7](#q7))। Dart-এর `typedef`-এর মতো।

*বাংলায়:*
> `typealias` শুধু একটা নতুন নাম, নতুন type না। Type safety লাগলে আমি `value class` নিই।

*English:*
> A `typealias` is just a new name, not a new type. For type safety I use a value class.

#### `when` vs `switch`

`when` একটা expression, মানে value ফেরত দেয়। যেকোনো type-এ চলে, আর range (`in 1..5`), type check (`is`) সবই এর ভেতরে লেখা যায়।

*বাংলায়:*
> `when` একটা expression, value ফেরত দেয়। যেকোনো type, range (`in 1..5`) আর `is` দিয়ে type check — সব চলে।

*English:*
> `when` is an expression, so it returns a value. It works with any type, ranges like `in 1..5`, and `is` type checks.

#### `init` block

`init` block primary constructor-এর অংশ হিসেবে চলে। Class body-তে property initializer আর `init` block যে ক্রমে লেখা, সেই ক্রমেই চলে। তাই `init`-এ এমন property পড়বেন না, যেটা তার নিচে declare করা।

*বাংলায়:*
> `init` primary constructor-এর সাথে চলে। Property initializer আর `init` block যে ক্রমে লেখা, সেই ক্রমেই চলে।

*English:*
> `init` runs as part of the primary constructor, in the same order as the property initializers written in the class body.

#### `object` expression vs declaration

`object : Listener {}` হলো anonymous object — প্রতিবার নতুন একটা তৈরি হয়। `object Foo` হলো declaration — একটাই instance, মানে singleton।

*বাংলায়:*
> `object : Listener {}` হলো anonymous object, প্রতিবার নতুন তৈরি হয়। `object Foo` হলো singleton।

*English:*
> `object : Listener {}` is an anonymous object, created new each time. `object Foo` is a singleton.

#### `Array<Int>` vs `IntArray`

`Array<Int>` ভেতরে boxed `Integer` রাখে, মানে প্রতিটা সংখ্যা আলাদা object। `IntArray` হলো primitive `int[]` — দ্রুত আর কম memory লাগে।

*বাংলায়:*
> `Array<Int>` boxed `Integer` রাখে। `IntArray` হলো primitive `int[]`, তাই দ্রুত আর memory কম লাগে।

*English:*
> `Array<Int>` holds boxed `Integer`s. `IntArray` is a primitive `int[]`, so it's faster and uses less memory.

#### `String` immutable?

হ্যাঁ। প্রতিটা জোড়া দেওয়ায় নতুন `String` তৈরি হয়। তাই loop-এ জোড়া দিতে `buildString {}` বা `StringBuilder` নিন।

*বাংলায়:*
> হ্যাঁ, immutable। Loop-এ জোড়া দিতে হলে আমি `buildString {}` বা `StringBuilder` নিই।

*English:*
> Yes, it's immutable. To build one in a loop, I use `buildString {}` or `StringBuilder`.

#### Kotlin 2.0-এর বড় পরিবর্তন

নতুন **K2 compiler** — দ্রুত compile, আর আরও ভালো smart cast। আর Compose compiler এখন Kotlin repo-র অংশ।

*বাংলায়:*
> সবচেয়ে বড় পরিবর্তন নতুন K2 compiler — compile দ্রুত, smart cast আরও ভালো। আর Compose compiler এখন Kotlin repo-র অংশ।

*English:*
> The big change is the new K2 compiler — faster builds and smarter smart casts. And the Compose compiler now lives in the Kotlin repo.

[উপরে ফিরুন](#toc)

---

# B. Coroutines আর Flow

> এই অংশ থেকে প্রায় প্রতিটা Android interview-এ ৩–৫টা প্রশ্ন আসে। সবচেয়ে বেশি সময় এখানে দিন।

### <a id="q9"></a>Q9. Coroutine কী? `suspend` ভেতরে কীভাবে কাজ করে?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** Coroutine হলো এমন একটা কাজ, যেটা মাঝপথে থামতে (suspend) পারে আর পরে আবার চালু হতে পারে। কিন্তু থামার সময় thread **block** করে না, thread ছেড়ে দেয়। Compiler প্রতিটা `suspend` function-কে একটা **state machine**-এ বদলে দেয়, আর একটা লুকানো `Continuation` parameter যোগ করে। Coroutine অনেক হালকা — এক লাখ coroutine চালানো যায়, এক লাখ thread চালানো যায় না। Dart-এর `async/await`-ও ভেতরে একই রকম state machine।

---

#### আপনি যা লেখেন

```kotlin
suspend fun loadProfile(id: String): Profile {
    val user = api.getUser(id)          // suspend point 1
    val posts = api.getPosts(user.id)   // suspend point 2
    return Profile(user, posts)
}
```

দেখতে সাধারণ, উপর থেকে নিচে চলা code। কিন্তু দুইটা জায়গায় function থেমে যেতে পারে। এগুলোকে বলে suspend point।

---

#### Compiler যা বানায়

মোটামুটি এরকম (সহজ করে দেখানো):

```kotlin
fun loadProfile(id: String, cont: Continuation<Profile>): Any? {
    // cont-এর ভেতরে একটা label থাকে: কোন ধাপে আছি
    when (cont.label) {
        0 -> {
            cont.label = 1
            val r = api.getUser(id, cont)
            if (r == COROUTINE_SUSPENDED) return r
        }
        1 -> { /* user পেয়েছি */ cont.label = 2; /* getPosts call */ }
        2 -> { /* posts পেয়েছি */ return Profile(user, posts) }
    }
}
```

এখানে দুইটা নতুন জিনিস:
- **`Continuation`** — একটা object, যেটা জানে "এরপর কোথা থেকে চালু করতে হবে"। এর ভেতরে `label` (কোন ধাপে আছি) আর local variable-গুলো রাখা থাকে। অনেকটা একটা callback-এর মতো, যেটা নিজের অবস্থাও মনে রাখে।
- **`COROUTINE_SUSPENDED`** — একটা বিশেষ marker। এটা ফেরত এলে বোঝা যায়, result এখনো আসেনি, function এখন থামবে।

ধাপগুলো:
1. `api.getUser` network call শুরু করে আর `COROUTINE_SUSPENDED` ফেরত দেয়।
2. Function-টা return করে। Thread মুক্ত হয়ে অন্য কাজ করে (main thread হলে UI আঁকে)।
3. Response এলে `cont.resumeWith(result)` call হয়। Function আবার চলে, কিন্তু এবার `label = 1` থেকে।
4. Local variable-গুলো `Continuation` object-এর ভেতরে রাখা থাকে, তাই হারায় না।

এজন্যই coroutine সস্তা। এটা thread না, heap-এ রাখা একটা ছোট object মাত্র।

---

#### Thread vs Coroutine

| | Thread | Coroutine |
|---|---|---|
| Memory | প্রতিটায় ~১ MB stack | কয়েকশো byte-এর object |
| Switch | OS করে, দামি | Library করে, সস্তা |
| Wait করলে | thread block | thread মুক্ত |
| Cancel | কঠিন | built-in, structured |

**Flutter-এর সাথে মিল:** Dart-এর `async/await`-ও compiler-এর বানানো state machine। পার্থক্য হলো: Dart-এ এক isolate-এ একটাই thread (event loop)। Kotlin-এ coroutine বিভিন্ন thread-এ যেতে পারে (`Dispatchers`)। তাই Kotlin-এ shared mutable state-এ race condition হতে পারে, Dart-এ একটা isolate-এর ভেতরে হয় না।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Coroutine হলো এমন একটা কাজ, যেটা thread block না করেই থামতে পারে। ভেতরে compiler প্রতিটা suspend function-কে একটা state machine বানায়, আর একটা লুকানো `Continuation` parameter যোগ করে। প্রতিটা suspension point-এ সে local state রেখে return করে, পরে ঠিক ধাপ থেকে আবার চালু হয়।
>
> এজন্যই coroutine সস্তা — এগুলো object, thread না।
>
> একটা কথা আমি সবসময় পরিষ্কার করে বলি: `suspend` মানে background না। কোন thread-এ চলবে, সেটা ঠিক করে dispatcher।

*English:*
> A coroutine is a piece of work that can suspend without blocking its thread. Under the hood, the compiler turns every suspend function into a state machine and adds a hidden `Continuation` parameter. At each suspension point it saves the local state and returns, and later it resumes from the right step.
>
> That's why coroutines are cheap — they are objects, not threads.
>
> One thing I always make clear: `suspend` does not mean background. The dispatcher decides the thread.

**সাধারণ ভুল:**
- "`suspend` লিখলেই background thread-এ চলে" — ভুল। `suspend` শুধু বলে "এটা থামতে পারে"। কোন thread-এ চলবে সেটা ঠিক করে Dispatcher ([Q10](#q10))। এই ভুল ধারণায় main thread-এ ভারী কাজ চলে যায়, আর UI আটকে যায়।

**Follow-up প্রশ্ন:** "Callback-based API-কে suspend বানাবেন কীভাবে?"

*বাংলায়:*
> একবারের callback হলে আমি `suspendCancellableCoroutine` দিয়ে wrap করি — success-এ `resume`, failure-এ `resumeWithException`। আর যে listener বারবার call হয়, মানে stream-এর মতো, সেখানে `callbackFlow` নিই, আর `awaitClose`-এ listener সরিয়ে দিই।

*English:*
> For a one-shot callback, I wrap it with `suspendCancellableCoroutine` — `resume` on success, `resumeWithException` on failure. For a listener that fires many times, I use `callbackFlow` and remove the listener in `awaitClose`.

```kotlin
suspend fun FusedLocationProviderClient.awaitLastLocation(): Location? =
    suspendCancellableCoroutine { cont ->
        lastLocation
            .addOnSuccessListener { cont.resume(it) }
            .addOnFailureListener { cont.resumeWithException(it) }
    }
```

Stream-এর মতো callback (listener বারবার call হয়) হলে `callbackFlow` + `awaitClose { removeListener() }`।

[উপরে ফিরুন](#toc)

---

### <a id="q10"></a>Q10. Dispatchers কী? `withContext` আর main-safety কী?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** Dispatcher ঠিক করে coroutine কোন thread-এ চলবে। `Main` হলো UI thread। `IO` হলো disk আর network-এর মতো অপেক্ষার কাজের জন্য। `Default` হলো CPU-ভারী কাজের জন্য (JSON parse, sort, image process)। **Main-safe** মানে function-টা main thread থেকে call করা নিরাপদ, কারণ ভারী কাজটা সে নিজেই `withContext` দিয়ে অন্য thread-এ সরিয়ে নেয়।

---

#### কোন dispatcher কী কাজে

| Dispatcher | Thread | কী কাজ |
|---|---|---|
| `Dispatchers.Main` | UI thread | UI update, ছোট কাজ |
| `Dispatchers.Main.immediate` | UI thread, কিন্তু আগে থেকেই main-এ থাকলে সাথে সাথে চলে | `viewModelScope` এটাই ব্যবহার করে |
| `Dispatchers.IO` | বড় pool — একসাথে সর্বোচ্চ ৬৪টা বা CPU core-এর সমান (যেটা বড়)। Thread দরকার হলে তৈরি হয় | file, database, network |
| `Dispatchers.Default` | CPU core-এর সংখ্যার সমান thread | হিসাব, parse, sort |
| `Dispatchers.Unconfined` | যে thread-এ resume হয় সেখানেই | প্রায় কখনো না (test-এ কখনো কখনো) |

`IO` বড় কেন, আর `Default` ছোট কেন? IO কাজে thread বেশিরভাগ সময় শুধু অপেক্ষা করে, তাই অনেক thread রাখা যায়। CPU কাজে প্রতিটা thread সত্যিই core ব্যস্ত রাখে, তাই core-এর চেয়ে বেশি thread রাখলে লাভ নেই।

`IO` আর `Default` ভেতরে একই thread pool শেয়ার করে। তাই `Default` থেকে `IO`-তে যেতে প্রায়ই thread বদলাতে হয় না।

**Flutter-এর সাথে মিল:** Dart-এ ভারী CPU কাজ আপনি `Isolate.run` বা `compute`-এ পাঠান। Kotlin-এ একই কাজ `withContext(Dispatchers.Default)`। পার্থক্য হলো, এখানে memory শেয়ার হয়, data copy করতে হয় না।

---

#### Main-safe repository — সঠিক নিয়ম

```kotlin
class NewsRepository @Inject constructor(
    private val api: NewsApi,
    private val dao: NewsDao,
    @IoDispatcher private val io: CoroutineDispatcher,   // inject করুন, hardcode না
) {
    suspend fun refresh() = withContext(io) {
        val articles = api.latest()
        dao.upsertAll(articles.map { it.toEntity() })
    }
}

// ViewModel-এ কোনো dispatcher চিন্তা লাগে না
fun onRefresh() = viewModelScope.launch {
    repository.refresh()       // main থেকে call — তবুও নিরাপদ
}
```

Thread বদলানোর দায়িত্ব যে কাজ করে, তার। Caller-কে thread নিয়ে ভাবতে হয় না। তাই ViewModel-এর code পরিষ্কার থাকে।

**কেন dispatcher inject করবেন:** Test-এ `StandardTestDispatcher` দিতে পারবেন। Hardcode `Dispatchers.IO` থাকলে test-এ আসল thread চলে, আর test flaky হয়।

আরও দুইটা কথা, যেটা senior হিসেবে জানা দরকার:
- Retrofit-এর `suspend` function আর Room-এর `suspend` DAO নিজেরাই main-safe। ওদের চারপাশে `withContext(IO)` দেওয়া অপ্রয়োজনীয় — ক্ষতি নেই, কিন্তু দরকারও নেই।
- `Dispatchers.IO.limitedParallelism(1)` দিয়ে একটা "একবারে একটা" queue বানানো যায়, নতুন thread pool না বানিয়েই।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Dispatcher ঠিক করে coroutine কোথায় চলবে: UI-র জন্য Main, blocking IO-র জন্য IO, CPU কাজের জন্য Default।
>
> আমার নিয়ম হলো, data layer-এর প্রতিটা suspend function main-safe হবে। সে নিজের কাজ `withContext` দিয়ে সরিয়ে নেয়, তাই caller-কে thread নিয়ে ভাবতে হয় না। Dispatcher আমি hardcode না করে inject করি, যাতে test-এ test dispatcher দেওয়া যায়।
>
> আর Room বা Retrofit-এর suspend call-কে আবার wrap করি না, কারণ ওরা আগেই main-safe।

*English:*
> Dispatchers decide where a coroutine runs: Main for UI, IO for blocking IO, Default for CPU work.
>
> My rule is that every suspend function in the data layer is main-safe — it moves its own work with `withContext`, so callers never think about threads. I inject the dispatcher instead of hardcoding it, so tests can use a test dispatcher.
>
> And I don't wrap Room or Retrofit suspend calls again, because they are already main-safe.

**সাধারণ ভুল:**
- `withContext(Dispatchers.Main)` দিয়ে ViewModel-এ বারবার main-এ ফেরা। `viewModelScope` আগে থেকেই main-এ আছে, তাই এটা শুধু noise আর অকারণ context switch।

**Follow-up প্রশ্ন:** "`runBlocking` কখন ব্যবহার করবেন?"

*বাংলায়:*
> প্রায় কখনো না। এটা thread block করে, আর main thread-এ দিলে ANR হয়। আমি শুধু `main()` function-এ, অথবা কিছু পুরনো synchronous API-র ভেতরে নিই — যেমন OkHttp-এর `Authenticator` — তাও খুব সাবধানে।

*English:*
> Almost never. It blocks the thread, and on the main thread it causes an ANR. I only use it in a `main()` function or inside some old synchronous APIs, like OkHttp's `Authenticator`, and very carefully.

[উপরে ফিরুন](#toc)

---

### <a id="q11"></a>Q11. Structured concurrency কী? Job, SupervisorJob, scope

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** Structured concurrency মানে প্রতিটা coroutine একটা **scope**-এর ভেতরে জন্মায়, আর এভাবে একটা parent-child গাছ তৈরি হয়। Parent তার সব child শেষ না হওয়া পর্যন্ত শেষ হয় না। Parent cancel হলে সব child cancel হয়। সাধারণ `Job`-এ একটা child fail করলে parent আর বাকি সব sibling cancel হয়। `SupervisorJob`-এ একটা child fail করলে বাকিরা চলতে থাকে।

---

#### সমস্যাটা কোথায়

Coroutine চালু করা সহজ। কঠিন হলো, কাজটা কখন থামবে সেটা নিশ্চিত করা। User screen থেকে চলে গেলে তার জন্য চালু হওয়া network call-গুলো চলতে থাকলে memory আর battery নষ্ট হয়, আর পুরনো screen-এ result দিতে গিয়ে bug হয়। Structured concurrency এই প্রশ্নের উত্তর দেয়: প্রতিটা coroutine-এর একজন মালিক থাকবে, আর মালিক চলে গেলে সব কাজ থামবে।

---

#### গাছটা দেখতে এরকম

```
viewModelScope (SupervisorJob + Main.immediate)
├── launch { loadUser() }
├── launch { loadFeed() }
│     └── async { loadAds() }
└── launch { observeCart() }
```

ViewModel clear হলে (`onCleared`) → `viewModelScope` cancel → গাছের সব coroutine cancel। কোনো কাজ ঝুলে থাকে না, leak হয় না।

`viewModelScope`-এ `SupervisorJob` কেন? কারণ `loadFeed` fail করলে `loadUser` আর `observeCart`-ও মরে যাক, এটা কেউ চায় না। একটা screen-এর আলাদা আলাদা কাজ একে অপরের থেকে আলাদা থাকা উচিত।

---

#### কোন scope কখন

| Scope | কতদিন বাঁচে |
|---|---|
| `viewModelScope` | ViewModel clear হওয়া পর্যন্ত |
| `lifecycleScope` | Activity / Fragment destroy পর্যন্ত |
| `viewLifecycleOwner.lifecycleScope` | Fragment-এর view destroy পর্যন্ত |
| `rememberCoroutineScope()` | Composable composition থেকে বের হওয়া পর্যন্ত |
| নিজের application scope | পুরো app process। DI দিয়ে inject করুন: `CoroutineScope(SupervisorJob() + Dispatchers.Default)` |
| `GlobalScope` | কোনো মালিক নেই। ব্যবহার করবেন না। Cancel হয় না, test করা যায় না। |

---

#### Parallel call — `coroutineScope` vs `supervisorScope`

```kotlin
// একটা fail করলে পুরোটা fail — দুটো data-ই লাগবে
suspend fun loadDashboard(): Dashboard = coroutineScope {
    val user = async { api.user() }
    val stats = async { api.stats() }
    Dashboard(user.await(), stats.await())
}

// একটা fail করলেও বাকিটা দেখাতে চাই
suspend fun loadHome(): Home = supervisorScope {
    val feed = async { api.feed() }
    val ads = async { runCatching { api.ads() }.getOrNull() }   // ad না এলেও চলবে
    Home(feed.await(), ads.await())
}
```

কোনটা নেবেন, সেটা business প্রশ্ন: সব data ছাড়া কি screen অর্থহীন? তাহলে `coroutineScope`। কিছু অংশ না এলেও screen দেখানো যায়? তাহলে `supervisorScope`।

**Flutter-এর সাথে মিল:** Dart-এ এরকম কিছু নেই। Dart-এ `Future` শুরু হলে কেউ তাকে cancel করে না। Widget dispose হলেও `Future` চলে, আর পরে `setState() called after dispose()` error দেয়। Kotlin-এ এই পুরো সমস্যা structured concurrency দিয়ে সমাধান হয়ে যায়। Interview-এ এই তুলনা বললে ভালো impression পড়ে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Structured concurrency মানে প্রতিটা coroutine-এর একটা মালিক scope আছে, আর scope-গুলো মিলে একটা গাছ তৈরি করে। মালিক চলে গেলে, যেমন ViewModel clear হলে, তার সব child cancel হয়। তাই কিছু leak হয় না, অকারণে চলতেও থাকে না।
>
> সাধারণ Job-এ একটা child fail করলে parent আর তার sibling-রাও cancel হয়। SupervisorJob-এ failure আলাদা থাকে — এজন্যই `viewModelScope` এটা ব্যবহার করে।
>
> আমি `GlobalScope` এড়িয়ে চলি। Inject করা application scope একই কাজ করে, কিন্তু সেটা আমি control আর test করতে পারি। আর যে কাজ process মরে গেলেও শেষ হতে হবে, তার জন্য WorkManager।

*English:*
> Structured concurrency means every coroutine has an owner scope, and the scopes form a tree. When the owner goes away — for example a ViewModel is cleared — all its children are cancelled, so nothing leaks or keeps running.
>
> With a normal Job, one failing child cancels the parent and its siblings; with a SupervisorJob, failures stay isolated, which is why `viewModelScope` uses one.
>
> I avoid `GlobalScope`: an injected application scope does the same job, and I can control and test it. For work that must survive the process, I use WorkManager.

**সাধারণ ভুল:**
- `launch(SupervisorJob()) { ... }` লেখা। এতে নতুন Job-টা parent হয়ে যায়, আর scope-এর সাথে সম্পর্ক ভেঙে যায় — scope cancel হলেও এই coroutine আর cancel হয় না। `SupervisorJob` scope তৈরির সময় দিন, অথবা `supervisorScope {}` ব্যবহার করুন।

**Follow-up প্রশ্ন:** "User 'Save' চাপল, তারপর screen থেকে বের হয়ে গেল। কাজটা শেষ হবে কীভাবে?"

*বাংলায়:*
> `viewModelScope`-এ চালালে ViewModel clear হতেই কাজটা cancel হয়ে যাবে। তাই এই কাজ আমি inject করা application scope-এ `launch` করি। আর যদি app বন্ধ হয়ে গেলেও কাজটা শেষ হতে হয়, তাহলে WorkManager ([Q42](#q42)) নিই।

*English:*
> In `viewModelScope` it would be cancelled as soon as the ViewModel is cleared. So I launch it in an injected application scope. If it must finish even after the app process dies, I use WorkManager.

[উপরে ফিরুন](#toc)

---

### <a id="q12"></a>Q12. Coroutine-এ exception কীভাবে handle করবেন?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Hard

**সংক্ষেপে:** `launch`-এর ভেতরে না-ধরা exception সাথে সাথে parent-এর দিকে যায়। Parent cancel হয়, আর root-এ গিয়ে handler না থাকলে app crash করে। `async` exception-টা ধরে রাখে আর `await()`-এ throw করে — কিন্তু সাধারণ scope-এ সে parent-কেও fail করায়। `CoroutineExceptionHandler` শুধু **root** coroutine-এ কাজ করে। আর `CancellationException` কখনো গিলে ফেলবেন না।

---

#### ১. সবচেয়ে সহজ আর ভালো: suspend call-এর চারপাশে try/catch

```kotlin
fun load() = viewModelScope.launch {
    _state.value = UiState.Loading
    try {
        val users = repository.users()
        _state.value = UiState.Success(users)
    } catch (e: IOException) {
        _state.value = UiState.Error("ইন্টারনেট নেই")
    } catch (e: HttpException) {
        _state.value = UiState.Error("Server error ${e.code()}")
    }
}
```

এখানে exception কখনো coroutine-এর বাইরে যায় না। ঠিক যেখানে ঘটে, সেখানেই ধরা হয়, আর UI state-এ পরিণত হয়। নির্দিষ্ট exception ধরা হয়েছে, তাই `CancellationException` ভুল করে ধরা পড়ে না।

---

#### ২. `CoroutineExceptionHandler` — শেষ ভরসা (log, crash report)

```kotlin
private val handler = CoroutineExceptionHandler { _, e -> Log.e(TAG, "unhandled", e) }

viewModelScope.launch(handler) { ... }      // root launch — কাজ করবে
viewModelScope.launch {
    launch(handler) { ... }                 // child — কাজ করবে না! parent-এর দিকে যাবে
}
```

Child-এ কেন কাজ করে না? কারণ child নিজে exception handle করে না, সে exception parent-এর হাতে তুলে দেয়। Exception উপরে উঠতে উঠতে root-এ পৌঁছায়, আর শুধু সেখানেই handler দেখা হয়। তাই handler দিয়ে "error handle" হয় না — এটা শুধু শেষ মুহূর্তে log করার জায়গা।

---

#### ৩. `CancellationException`-এর ফাঁদ — খুব গুরুত্বপূর্ণ

Cancel হলে coroutine `CancellationException` throw করে। এটা স্বাভাবিক ব্যাপার, error না। এর মাধ্যমেই coroutine জানে যে তাকে থামতে হবে। কিন্তু `catch (e: Exception)` বা `runCatching {}` এটাকেও ধরে ফেলে। তাহলে coroutine বুঝতে পারে না যে তাকে থামতে হবে, আর কাজ চলতে থাকে।

```kotlin
// ভুল
try { repository.sync() } catch (e: Exception) { log(e) }    // cancel-ও গিলে ফেলল

// ঠিক
try {
    repository.sync()
} catch (e: CancellationException) {
    throw e                                                    // আবার ছুড়ে দিন
} catch (e: Exception) {
    log(e)
}
```

---

#### ৪. `async`-এর লুকানো আচরণ

```kotlin
coroutineScope {
    val a = async { error("boom") }
    try { a.await() } catch (e: Exception) { /* ধরলাম */ }
    // তবুও coroutineScope fail করবে! async parent-কেও জানিয়ে দিয়েছে।
}
```

অনেকে ভাবেন `await()`-এ ধরলেই হলো। কিন্তু `async` fail করার সাথে সাথেই parent-কে জানিয়ে দেয়, `await()`-এর জন্য অপেক্ষা করে না। তাই ধরতে চাইলে `supervisorScope`-এর ভেতরে `async` দিন, অথবা `async`-এর **ভেতরে** try/catch দিন।

---

#### Repository থেকে result ফেরত দেওয়া

Repository থেকে `Result<T>` বা নিজের sealed type ফেরত দেওয়া একটা ভালো pattern। তাহলে ViewModel-এ exception নিয়ে চিন্তা কম লাগে, শুধু result-এর উপর `when` চালালেই হয়। কিন্তু Kotlin-এর built-in `runCatching` ব্যবহার করলে `CancellationException` আলাদা করে আবার throw করতে মনে রাখবেন, কারণ `runCatching` সেটাও ধরে ফেলে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> `launch`-এ না-ধরা exception সরাসরি parent-এর দিকে যায়, আর root-এ handler না থাকলে app crash করে। `async`-এ exception `await`-এ throw হয়, কিন্তু সাধারণ scope-এ সেটা parent-কেও cancel করে — এটা অনেককে অবাক করে।
>
> `CoroutineExceptionHandler` শুধু root coroutine-এ কাজ করে। তাই আমি এটাকে error handling না, শেষ ভরসার logger হিসেবে দেখি।
>
> আমার default হলো suspend call-এর চারপাশে try/catch, অথবা repository থেকে একটা Result। আর `CancellationException` আমি সবসময় আবার throw করি, কারণ সেটা গিলে ফেললে cancellation ভেঙে যায়।

*English:*
> With `launch`, an uncaught exception goes straight to the parent and, at the root, crashes the app unless there's a handler. With `async`, the exception is thrown on `await`, but in a normal scope it also cancels the parent — that surprises many people.
>
> `CoroutineExceptionHandler` only works on root coroutines, so I treat it as a last-resort logger, not as error handling.
>
> My default is try/catch around the suspend call, or a Result from the repository — and I always rethrow `CancellationException`, because swallowing it breaks cancellation.

**সাধারণ ভুল:**
- `catch (e: Exception)` বা `runCatching {}` দিয়ে `CancellationException` গিলে ফেলা। Coroutine থামে না, screen চলে যাওয়ার পরেও কাজ চলতে থাকে।
- Child `launch`-এ `CoroutineExceptionHandler` দেওয়া। সেখানে এটা কখনো call হয় না, exception parent-এর দিকে চলে যায়।
- `coroutineScope`-এর ভেতরে শুধু `await()`-এর চারপাশে try/catch দেওয়া। Parent তবুও fail করে।

**Follow-up প্রশ্ন:** "`SupervisorJob` থাকলে child-এর exception কোথায় যায়?"

*বাংলায়:*
> Parent cancel হয় না, কিন্তু exception-টা হারিয়েও যায় না — সেটা `CoroutineExceptionHandler`-এ যায়। Handler না থাকলে thread-এর uncaught exception handler-এ যায়, আর Android-এ তার মানে crash। তাই `viewModelScope.launch`-এর ভেতরে না-ধরা exception এখনো app crash করায়।

*English:*
> The parent isn't cancelled, but the exception still goes to the `CoroutineExceptionHandler`. Without one, it goes to the thread's uncaught exception handler — on Android, that's a crash. So an uncaught exception inside `viewModelScope.launch` still crashes the app.

[উপরে ফিরুন](#toc)

---

### <a id="q13"></a>Q13. Coroutine cancellation কীভাবে কাজ করে?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Coroutine-এ cancellation হলো **cooperative**। মানে বাইরে থেকে কেউ জোর করে থামায় না। Coroutine নিজেই মাঝে মাঝে check করে, তাকে থামতে বলা হয়েছে কি না। `kotlinx.coroutines`-এর সব suspend function (`delay`, `withContext`, `emit`) এই check নিজেরাই করে। কিন্তু একটা লম্বা CPU loop, যেখানে কোনো suspend call নেই, নিজে থেকে থামে না।

---

#### সমস্যাটা কোথায়

`job.cancel()` call করলে coroutine-এর state শুধু "cancelled" হয়ে যায়। কোড তখনই থামে না। থামে পরের check point-এ, মানে পরের suspend call-এ। সেখানে `CancellationException` throw হয়, আর coroutine সেখান থেকে বের হয়ে যায়।

তাই যে loop শুধু CPU-র কাজ করে (image compress, বড় list parse), সেখানে কোনো check point নেই। Screen বন্ধ হয়ে গেলেও loop শেষ পর্যন্ত চলতে থাকে। CPU আর battery নষ্ট হয়।

Dart থেকে এলে: সাধারণ `Future` cancel করার built-in উপায় Dart-এ নেই। Kotlin-এ cancellation প্রথম দিন থেকেই structured concurrency-র অংশ, তাই এটা আপনাকে সত্যিই বুঝতে হবে।

---

#### নিজে check point দেওয়া — `ensureActive()` আর `yield()`

```kotlin
suspend fun processImages(files: List<File>) = withContext(Dispatchers.Default) {
    for (file in files) {
        ensureActive()                    // cancel হলে এখানে CancellationException
        compress(file)                    // ভারী, কিন্তু suspend না
    }
}
```

- `ensureActive()` শুধু check করে। Cancel হয়ে থাকলে throw করে।
- `yield()` check-ও করে, আর একই dispatcher-এর অন্য coroutine-কে চলার সুযোগও দেয়।

---

#### Cancel হওয়ার পরেও cleanup

Cancel হলে `CancellationException` আসে, তাই `finally` block তখনও চলে। সমস্যা হলো, cancel হওয়া coroutine-এ আবার suspend call করলে সেটাও সাথে সাথে throw করে। তাই cleanup-এ যদি database-এ লিখতে হয়, সেটা `NonCancellable`-এর ভেতরে রাখতে হয়।

```kotlin
try {
    upload()
} finally {
    withContext(NonCancellable) {         // cancel হওয়া coroutine-এ suspend call করতে
        dao.markUploadStopped()
    }
}
```

`NonCancellable` শুধু `finally`-র ভেতরে ছোট cleanup-এর জন্য। অন্য কোথাও ব্যবহার করবেন না। কারণ এর ভেতরের কাজ cancel মানে না — ভুল জায়গায় দিলে কাজটা আর থামানো যায় না।

---

#### Timeout

হাতে timer বানানোর দরকার নেই। `withTimeout` সময় পার হলে throw করে। `withTimeoutOrNull` throw না করে `null` ফেরত দেয়।

```kotlin
val result = withTimeoutOrNull(5_000) { api.slowCall() }   // ৫ সেকেন্ডে না এলে null
```

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Coroutine-এ cancellation cooperative। `kotlinx.coroutines`-এর সব suspend function নিজেরাই check করে। কিন্তু একটা লম্বা CPU loop নিজে থেকে থামে না, তাই সেখানে আমি `ensureActive()` বা `yield()` দিই।
>
> Cancel হলে `CancellationException` আসে, আর `finally` তখনও চলে। Cleanup-এ suspend call লাগলে আমি সেটা `withContext(NonCancellable)`-এর ভেতরে রাখি — শুধু ওই জায়গাতেই।
>
> ধীর call-এর জন্য নিজে timer বানাই না। `withTimeout` বা `withTimeoutOrNull` নিই।

*English:*
> Cancellation is cooperative. All suspend functions in kotlinx.coroutines check for it, but a tight CPU loop won't stop by itself, so I add `ensureActive()` or `yield()`.
>
> A cancelled coroutine throws `CancellationException`, and `finally` blocks still run. If the cleanup needs to suspend, I wrap it in `withContext(NonCancellable)` — and only there.
>
> For slow calls I use `withTimeout` or `withTimeoutOrNull` instead of manual timers.

**সাধারণ ভুল:**
- Coroutine-এর ভেতরে `Thread.sleep()`। এটা পুরো thread block করে, আর cancel বোঝে না। `delay()` ব্যবহার করুন — এটা thread ছেড়ে দেয়, আর cancel হলে সাথে সাথে থামে।

**Follow-up প্রশ্ন:** "`catch (e: Exception)` দিলে cancellation-এর কী হয়?"

*বাংলায়:*
> `CancellationException`-ও একটা `Exception`, তাই সাধারণ catch এটাকেও ধরে ফেলে। তখন coroutine জানতেই পারে না যে তাকে থামতে বলা হয়েছিল, আর কাজ চালিয়ে যায়। তাই আমি broad catch-এ `CancellationException` আবার throw করে দিই।

*English:*
> `CancellationException` is an `Exception`, so a broad catch swallows it, and the coroutine keeps running as if nothing happened. In a broad catch I always rethrow `CancellationException`.

[উপরে ফিরুন](#toc)

---

### <a id="q14"></a>Q14. Flow, StateFlow, SharedFlow, Channel, LiveData — পার্থক্য কী?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** পাঁচটাই async value-এর stream, কিন্তু আচরণ আলাদা।
- `Flow` **cold** — কেউ collect না করলে কিছু চলে না। প্রতিটা collector নিজের আলাদা run পায়।
- `StateFlow` **hot** — সবসময় একটা current value রাখে, একই value দুইবার পাঠায় না। UI state-এর জন্য।
- `SharedFlow` hot — initial value নেই, replay ঠিক করা যায়। Broadcast event-এর জন্য।
- `Channel` একটা queue — প্রতিটা value ঠিক একজন receiver পায়।
- `LiveData` পুরনো, lifecycle-aware, কিন্তু শুধু Android আর main thread-এর।

---

#### Cold আর hot — আসল পার্থক্য

**Cold** মানে producer-এর কোড collect-এর সময় চলে। দুইজন collect করলে কোডটা দুইবার চলে, দুইজন আলাদা value পায়। Network call-এর `Flow` দুইবার collect করলে দুইটা request যায়।

**Hot** মানে producer কারো জন্য অপেক্ষা করে না। সে নিজের মতো চলে, আর যারা তখন শুনছে, তারা সবাই একই value পায়।

---

#### পাশাপাশি তুলনা

| | Flow | StateFlow | SharedFlow | Channel | LiveData |
|---|---|---|---|---|---|
| Cold / Hot | Cold | Hot | Hot | Hot | Hot |
| Initial value | না | **হ্যাঁ, বাধ্যতামূলক** | না | না | ঐচ্ছিক |
| Collector-রা | প্রত্যেকে আলাদা run | সবাই একই value | সবাই একই value | **একজনই** প্রতিটা পায় | সবাই |
| একই value আবার | পাঠায় | **পাঠায় না** (equals দিয়ে check) | পাঠায় | পাঠায় | পাঠায় |
| দ্রুত value এলে | হারায় না — collector শেষ না করা পর্যন্ত `emit` অপেক্ষা করে | মাঝখানেরগুলো হারায় (conflated) | config অনুযায়ী | buffer অনুযায়ী | হারায় |
| Lifecycle-aware | না | না | না | না | হ্যাঁ |
| Platform | Kotlin (KMP-ও) | Kotlin | Kotlin | Kotlin | শুধু Android |

"Conflated" মানে: collector ধীর হলে মাঝখানের value বাদ যায়, শুধু সর্বশেষটা পৌঁছায়। UI state-এর জন্য এটাই ঠিক — পুরনো state দেখানোর কোনো দরকার নেই।

---

#### ViewModel-এ সাধারণ ব্যবহার

```kotlin
@HiltViewModel
class CartViewModel @Inject constructor(repo: CartRepository) : ViewModel() {

    // state — StateFlow
    private val _uiState = MutableStateFlow(CartUiState())
    val uiState: StateFlow<CartUiState> = _uiState.asStateFlow()   // বাইরে শুধু read-only

    fun onQuantityChange(itemId: String, qty: Int) {
        _uiState.update { it.copy(items = it.items.changeQty(itemId, qty)) }   // atomic update
    }
}
```

**`_uiState.value = _uiState.value.copy(...)` না লিখে `update {}` কেন?** দুইটা coroutine একসাথে পড়ে আর লেখে। দুজনেই পুরনো value পড়ল, দুজনেই নিজের copy লিখল — একজনের পরিবর্তন হারিয়ে গেল। `update {}` compare-and-set loop ব্যবহার করে। মানে লেখার আগে check করে value মাঝখানে বদলেছে কি না, বদলালে আবার চেষ্টা করে। তাই নিরাপদ।

---

#### StateFlow কেন event-এর জন্য খারাপ

"Snackbar দেখাও" message পরপর দুইবার একই হলে দ্বিতীয়বার আসবে না, কারণ StateFlow equals দিয়ে check করে। আর দ্রুত দুইটা এলে conflation-এর কারণে প্রথমটা হারাতে পারে। Event নিয়ে পুরো আলোচনা [Q33](#q33)-এ।

---

#### LiveData এখন কি চলে?

পুরনো View-based code-এ অনেক আছে, তাই জানতে হবে। নতুন code-এ `StateFlow` বেশি পছন্দ — কারণ Flow-এর operator আছে, test করা সহজ, আর KMP-তে চলে।

**Flutter-এর সাথে মিল:** Dart `Stream` default-এ single-subscription (cold-এর কাছাকাছি)। `StreamController.broadcast()` হলো SharedFlow-এর মতো। RxDart-এর `BehaviorSubject` হলো StateFlow-এর মতো। Bloc-এর `state` stream আসলে StateFlow-এর মতো — একই state দুইবার emit করে না।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Flow cold — প্রতিটা collector-এর জন্য কোডটা নতুন করে চলে। StateFlow hot, আর সবসময় সর্বশেষ value রাখে। এটা conflated, আর একই value আবার পাঠায় না। তাই UI state-এর জন্য এটা একদম ঠিক।
>
> SharedFlow hot, initial value নেই, replay ঠিক করা যায় — broadcast-এর জন্য ভালো। Channel প্রতিটা value ঠিক একজন receiver-কে দেয়।
>
> LiveData পুরনো code-এ এখনো আছে। কিন্তু নতুন code-এ আমি StateFlow নিই, কারণ operator আছে, test করা সহজ, আর KMP-তে চলে।

*English:*
> Flow is cold — the code runs again for each collector. StateFlow is hot and always holds the latest value; it's conflated and skips equal values, which makes it a great fit for UI state.
>
> SharedFlow is hot, has no initial value and a configurable replay, so it's good for broadcasts. A Channel delivers each value to exactly one receiver.
>
> LiveData is still in older code, but for new code I prefer StateFlow, because it has operators, is easy to test and works in KMP.

**সাধারণ ভুল:**
- `_uiState.value = _uiState.value.copy(...)` লেখা। দুইটা coroutine একসাথে লিখলে একজনের পরিবর্তন হারায়। `update {}` ব্যবহার করুন।
- One-time event (Snackbar, navigation) StateFlow-এ রাখা। একই event দ্বিতীয়বার আসে না, আর দ্রুত এলে হারাতে পারে ([Q33](#q33))।

**Follow-up প্রশ্ন:** "Cold Flow-কে hot বানাবেন কীভাবে?"

*বাংলায়:*
> `stateIn` দিয়ে StateFlow বানাই, অথবা `shareIn` দিয়ে SharedFlow। UI state-এর জন্য সাধারণত `stateIn` ([Q15](#q15))।

*English:*
> With `stateIn` for a StateFlow, or `shareIn` for a SharedFlow. For UI state I usually use `stateIn`.

[উপরে ফিরুন](#toc)

---

### <a id="q15"></a>Q15. দরকারি Flow operator: `flatMapLatest`, `combine`, `debounce`, `stateIn`

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** `map` আর `filter` সাধারণ রূপান্তর। `combine` কয়েকটা flow-এর সর্বশেষ value জুড়ে দেয়। `flatMapLatest` নতুন value এলে আগের ভেতরের কাজ cancel করে নতুনটা শুরু করে — search-এর জন্য সেরা। `stateIn` একটা cold flow-কে StateFlow বানায়, যাতে UI সবসময় শেষ value পায়। আর `flowOn` শুধু **উপরের (upstream)** অংশের dispatcher বদলায়।

---

#### একটা search screen — সব operator একসাথে

Search-এ তিনটা সমস্যা আছে। প্রতিটা অক্ষর টাইপে request যাওয়া উচিত না। একই query দুইবার পাঠানো উচিত না। আর পুরনো request-এর উত্তর নতুন query-র উপর বসে যাওয়া উচিত না। নিচের chain তিনটাই সমাধান করে।

```kotlin
@OptIn(FlowPreview::class, ExperimentalCoroutinesApi::class)
@HiltViewModel
class SearchViewModel @Inject constructor(
    private val repo: ProductRepository,
    private val savedState: SavedStateHandle,
) : ViewModel() {

    private val query = savedState.getStateFlow("query", "")   // process death-এর পরেও থাকে

    val uiState: StateFlow<SearchUiState> = query
        .debounce(300)                       // টাইপ থামার ৩০০ ms পরে
        .map { it.trim() }
        .distinctUntilChanged()              // একই query আবার হলে বাদ
        .flatMapLatest { q ->                // নতুন query এলে পুরনো request cancel
            if (q.isEmpty()) flowOf(SearchUiState.Idle)
            else repo.search(q)
                .map<List<Product>, SearchUiState> { SearchUiState.Results(it) }
                .onStart { emit(SearchUiState.Loading) }
                .catch { emit(SearchUiState.Error) }   // ভেতরে — নিচে কারণ দেখুন
        }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5_000),
            initialValue = SearchUiState.Idle,
        )

    fun onQueryChange(text: String) { savedState["query"] = text }
}
```

---

#### `flatMap` পরিবার

তিনটাই প্রতিটা value থেকে একটা নতুন flow বানায়। পার্থক্য হলো, আগের flow তখনও চললে কী হবে।

| Operator | নতুন value এলে |
|---|---|
| `flatMapLatest` | আগেরটা **cancel**, নতুনটা চালাও (search, selected id) |
| `flatMapConcat` | আগেরটা শেষ হোক, তারপর নতুনটা (ক্রম জরুরি) |
| `flatMapMerge` | সব একসাথে চালাও (parallel) |

---

#### `combine` vs `zip`

- `combine` — যেকোনো একটা বদলালে দুটোর **সর্বশেষ** value দিয়ে নতুন result দেয়। UI state বানাতে এটাই লাগে: `combine(userFlow, cartFlow) { u, c -> ... }`।
- `zip` — জোড়ায় জোড়ায় মেলায়: প্রথমটার ১ম + দ্বিতীয়টার ১ম। এটা কম লাগে।

---

#### `stateIn` আর `SharingStarted`

`stateIn` তিনটা জিনিস চায়: কোন scope-এ চলবে, কখন শুরু আর থামবে, আর শুরুতে কী value থাকবে।

| | মানে |
|---|---|
| `Eagerly` | সাথে সাথে শুরু, কখনো থামে না |
| `Lazily` | প্রথম collector এলে শুরু, কখনো থামে না |
| `WhileSubscribed(5_000)` | Collector থাকলে চলে। শেষ collector চলে যাওয়ার ৫ সেকেন্ড পরে থামে |

**৫ সেকেন্ড কেন?** Screen rotate হলে UI কিছুক্ষণের জন্য unsubscribe করে, তারপর আবার আসে। ৫ সেকেন্ড অপেক্ষা থাকলে upstream (database query, location) আবার শুরু করতে হয় না। কিন্তু app background-এ গেলে ৫ সেকেন্ড পরে থামে — battery বাঁচে।

---

#### `catch` কোথায় বসবে — এটা senior পয়েন্ট

দুইটা নিয়ম মনে রাখুন। `catch` শুধু তার **উপরের** error ধরে। আর error ধরার পরে ওই flow শেষ হয়ে যায়।

তাই উপরের code-এ `catch` দিয়েছি `flatMapLatest`-এর **ভেতরে**। Error হলে শুধু ওই একটা search-এর ভেতরের flow শেষ হয়। বাইরের `query` flow বেঁচে থাকে, তাই পরের search কাজ করে। বাইরে দিলে একবার error-এর পরে search পুরো বন্ধ হয়ে যেত।

**Flutter-এর সাথে মিল:** RxDart ব্যবহার করে থাকলে এগুলো চেনা: `switchMap` = `flatMapLatest`, `combineLatest` = `combine`, `debounceTime` = `debounce`।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি সবচেয়ে বেশি ব্যবহার করি তিনটা: কয়েকটা source থেকে UI state বানাতে `combine`, পুরনো কাজ cancel করতে `flatMapLatest` — search এর classic উদাহরণ — আর cold flow-কে UI-র জন্য StateFlow বানাতে `stateIn`।
>
> `stateIn` সাধারণত `WhileSubscribed(5_000)` দিয়ে শুরু করি। Rotation-এ upstream আবার শুরু হয় না, কিন্তু app সত্যিই background-এ গেলে থেমে যায়।
>
> আর `catch` রাখি `flatMapLatest`-এর ভেতরে, যাতে একটা request fail করলে পুরো stream শেষ না হয়ে যায়।

*English:*
> The operators I use most are `combine` to build UI state from several sources, `flatMapLatest` to cancel stale work — search is the classic case — and `stateIn` to turn a cold flow into a StateFlow for the UI.
>
> I usually start it with `WhileSubscribed(5_000)`: it survives a rotation without restarting the upstream, but stops when the app is really in the background.
>
> I also put `catch` inside `flatMapLatest`, so one failed request doesn't end the whole stream.

**সাধারণ ভুল:**
- `catch` পুরো chain-এর শেষে, `flatMapLatest`-এর বাইরে রাখা। প্রথম error-এর পরেই flow শেষ, search আর কাজ করে না।
- Search-এ `flatMapLatest`-এর বদলে `flatMapMerge` বা `flatMapConcat`। পুরনো query-র উত্তর পরে এসে নতুন result-এর উপর বসে যেতে পারে, বা অপ্রয়োজনীয় request চলতে থাকে।

**Follow-up প্রশ্ন:** "`stateIn` আর `shareIn`-এর পার্থক্য কী?"

*বাংলায়:*
> `stateIn` দেয় StateFlow — initial value লাগে, সবসময় একটা current value থাকে, একই value আবার পাঠায় না। `shareIn` দেয় SharedFlow — initial value নেই, কয়টা value replay হবে আমি ঠিক করি। UI state-এর জন্য `stateIn`, আর state না এমন shared stream-এর জন্য `shareIn`।

*English:*
> `stateIn` gives a StateFlow: it needs an initial value, always has a current one, and skips equal values. `shareIn` gives a SharedFlow: no initial value, and I choose the replay. I use `stateIn` for UI state and `shareIn` for shared streams that aren't state.

[উপরে ফিরুন](#toc)

---

### <a id="q16"></a>Q16. UI-তে Flow নিরাপদে কীভাবে collect করবেন?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** UI-তে flow collect হওয়া উচিত শুধু যখন screen দেখা যাচ্ছে। View system-এ এর জন্য `repeatOnLifecycle(Lifecycle.State.STARTED)` — app background-এ গেলে collect থামে, ফিরে এলে আবার শুরু হয়। Compose-এ `collectAsStateWithLifecycle()`। শুধু `lifecycleScope.launch { flow.collect {} }` লিখলে app background-এ থাকলেও collect চলতে থাকে — resource নষ্ট হয়, আর কখনো crash হয়।

---

#### সমস্যাটা কোথায়

`lifecycleScope` cancel হয় শুধু `onDestroy`-তে। তাই app background-এ গেলেও (`onStop`) collector চলতেই থাকে। Upstream-এ location বা sensor থাকলে সেগুলোও চলতে থাকে। আর stop থাকা অবস্থায় UI update করতে গেলে, যেমন Fragment transaction, crash হতে পারে।

---

#### View system — `repeatOnLifecycle`

```kotlin
// Fragment — ঠিক
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    viewLifecycleOwner.lifecycleScope.launch {
        viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
            launch { viewModel.uiState.collect(::render) }
            launch { viewModel.events.collect(::handleEvent) }   // একাধিক flow = আলাদা launch
        }
    }
}
```

`repeatOnLifecycle(STARTED)` যা করে: `onStart`-এ block শুরু করে। `onStop`-এ block-এর সব coroutine **cancel** করে। আবার `onStart` এলে block নতুন করে চালায়।

প্রতিটা flow-এর জন্য আলাদা `launch` কেন? কারণ `StateFlow`-এর `collect` কখনো নিজে থেকে শেষ হয় না। একই coroutine-এ পরপর দুইটা `collect` লিখলে দ্বিতীয়টা কখনো চলে না।

---

#### Compose — `collectAsStateWithLifecycle()`

```kotlin
// Compose — ঠিক
@Composable
fun CartRoute(viewModel: CartViewModel = hiltViewModel()) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()
    CartScreen(state = state, onQuantityChange = viewModel::onQuantityChange)
}
```

**`collectAsState()` vs `collectAsStateWithLifecycle()`:** প্রথমটা lifecycle বোঝে না। Composable screen-এ থাকলে app background-এ গেলেও collect চালায়। Android-এ সবসময় দ্বিতীয়টা ব্যবহার করুন (`androidx.lifecycle:lifecycle-runtime-compose`)।

---

#### কেন `launchWhenStarted` বাদ (deprecated)

এটা background-এ গেলে coroutine **suspend** করত, cancel না। মানে upstream (যেমন location updates) চলতেই থাকত, শুধু UI value নিত না। `repeatOnLifecycle` আসলেই cancel করে, আর পরে নতুন করে শুরু করে।

**Flutter-এর সাথে মিল:** Flutter-এ `StreamBuilder` widget tree থেকে সরলে subscription cancel করে। কিন্তু app background-এ গেলে নিজে থেকে থামে না। Android-এ এই "background-এ থামো" অংশটাই `repeatOnLifecycle` দেয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> UI-তে আমি শুধু তখনই collect করি, যখন screen দেখা যাচ্ছে। View-এ এর জন্য view lifecycle owner-এর উপর `repeatOnLifecycle(STARTED)`, আর Compose-এ `collectAsStateWithLifecycle()`।
>
> পুরনো `launchWhenStarted` collector-কে শুধু pause করত, তাই upstream চলতেই থাকত — এজন্যই এটা deprecated।
>
> Code review-তে একটা bug আমি প্রায়ই খুঁজি: একই block-এ দুইটা `collect`। দ্বিতীয়টা কখনো চলে না, তাই প্রতিটা flow-এর নিজের `launch` লাগে।

*English:*
> In the UI I collect only while the screen is visible. With Views that's `repeatOnLifecycle(STARTED)` on the view lifecycle owner; in Compose it's `collectAsStateWithLifecycle()`.
>
> The old `launchWhenStarted` only paused the collector, so the upstream kept working — that's why it was deprecated.
>
> A common bug I look for in code review is two `collect` calls in one block: the second one never runs, so each flow needs its own `launch`.

**সাধারণ ভুল:**
- Fragment-এ Fragment-এর `lifecycleScope` ব্যবহার করা, `viewLifecycleOwner.lifecycleScope` না। Fragment back stack-এ গেলে view destroy হয়, কিন্তু Fragment বেঁচে থাকে। তখন collect চলতেই থাকে আর পুরনো view update করতে চায় ([Q18](#q18))।
- একটা `repeatOnLifecycle`-এর ভেতরে পরপর দুইটা `collect` লেখা। প্রথম `collect` কখনো শেষ হয় না, তাই দ্বিতীয়টা কখনো চলে না।

**Follow-up প্রশ্ন:** "`STARTED` কেন, `RESUMED` না?"

*বাংলায়:*
> `STARTED` মানে screen দেখা যাচ্ছে। `RESUMED` মানে focus-ও আছে। Multi-window-এ বা উপরে dialog-এর মতো activity থাকলে screen দেখা যায় কিন্তু focus থাকে না। তখনও আমি UI update চাই, তাই `STARTED` নিই ([Q17](#q17))।

*English:*
> `STARTED` means the screen is visible; `RESUMED` also means it has focus. In multi-window, or behind a dialog-like activity, the screen is visible without focus, and I still want it updated. So I use `STARTED`.

[উপরে ফিরুন](#toc)

---

# C. Android-এর মূল component

### <a id="q17"></a>Q17. Activity lifecycle আর configuration change

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** Activity-র callback ক্রম: `onCreate → onStart → onResume` (চালু), তারপর `onPause → onStop → onDestroy` (বন্ধ)। দুইটা জোড়া সবচেয়ে জরুরি। `onStart`/`onStop` মানে screen দেখা যাচ্ছে কি না। `onResume`/`onPause` মানে focus আছে কি না। Rotation, ভাষা বদল, dark mode বদল — এগুলো configuration change। এমন হলে default-এ Activity **destroy হয়ে আবার তৈরি হয়**। ViewModel এই change পার হয়ে বেঁচে থাকে।

---

#### পুরো ক্রম

```
      onCreate()
          ↓
      onStart()   ← onRestart() ← (stop থেকে ফিরলে)
          ↓
      onResume()   — এখন user-এর সাথে কথা বলছে
          ↓
      onPause()    — অন্য কিছু সামনে এল (dialog-এর মতো activity, multi-window)
          ↓
      onStop()     — আর দেখা যায় না
          ↓
      onDestroy()  — finish() বা config change
```

---

#### A থেকে B Activity খুললে ক্রম (খুব বেশি জিজ্ঞেস করে)

1. `A.onPause()`
2. `B.onCreate()` → `B.onStart()` → `B.onResume()`
3. `A.onStop()`

খেয়াল করুন, B শুরু হয় A-এর `onPause` শেষ হওয়ার পরে। তাই `onPause`-এ ভারী কাজ করবেন না — B দেখাতে দেরি হবে।

**Back চাপলে (B থেকে A):** `B.onPause` → `A.onRestart` → `A.onStart` → `A.onResume` → `B.onStop` → `B.onDestroy`।

**Home চাপলে:** `onPause` → `onStop`। তারপর `onSaveInstanceState` (API 28+-এ `onStop`-এর পরে)। `onDestroy` সাধারণত call হয় না।

---

#### কোন কাজ কোথায়

নিয়মটা হলো জোড়া মেনে চলা। যেটা `onStart`-এ শুরু, সেটা `onStop`-এ বন্ধ।

| Callback | কী করবেন |
|---|---|
| `onCreate` | UI setup (`setContent {}`), ViewModel নেওয়া |
| `onStart` / `onStop` | যা screen দেখা গেলেই লাগে: location, sensor, flow collect (`repeatOnLifecycle` এটা নিজে করে) |
| `onResume` / `onPause` | camera, যা focus-এর সাথে যুক্ত |
| `onDestroy` | শেষ cleanup। কিন্তু এর উপর ভরসা করবেন না — process kill হলে এটা call হয় না |

---

#### Configuration change সামলানোর উপায়

1. **ViewModel** — data রাখে। এটাই সবচেয়ে সাধারণ উপায়।
2. **`rememberSaveable` / `onSaveInstanceState`** — ছোট UI state (scroll position, টাইপ করা text)।
3. **`android:configChanges` manifest-এ** — Activity আবার তৈরি হয় না, শুধু `onConfigurationChanged` call হয়। পুরো Compose app-এ এটা কখনো কখনো ব্যবহার হয়, কারণ Compose নিজেই নতুন configuration-এ recompose করে। কিন্তু resource (string, layout) নিজে থেকে reload হয় না — সাবধান।

---

#### `onPause` মানে "দেখা যাচ্ছে না" — এই ধারণা ভুল

Android 10 থেকে multi-window-এ একসাথে অনেক Activity "resumed" থাকতে পারে (multi-resume)। আবার পাশের window-এ focus গেলে আপনার Activity pause হয়, কিন্তু তখনও পুরোপুরি দেখা যায়। তাই দেখা যাচ্ছে কি না জানতে `onStop` ব্যবহার করুন। এটা senior-level পয়েন্ট।

**Flutter-এর সাথে মিল:** Flutter-এর `AppLifecycleState` (`resumed`, `inactive`, `paused`, `detached`, `hidden`) আসলে এই Activity callback থেকেই আসে। Flutter app সাধারণত একটাই Activity (`FlutterActivity`)। আর Flutter configuration change-এ Activity recreate হতে দেয় না — manifest-এ `configChanges` দেওয়া থাকে। এটা খেয়াল করেছেন কি না, interview-এ বলতে পারেন।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> দুইটা জোড়া সবচেয়ে জরুরি: দেখা যাচ্ছে কি না তার জন্য `onStart`/`onStop`, আর focus-এর জন্য `onResume`/`onPause`। A থেকে B খুললে আগে A pause হয়, তারপর B পুরো শুরু হয়, শেষে A stop হয়। তাই `onPause`-এ ভারী কাজ রাখলে পরের screen দেরিতে আসে।
>
> Configuration change-এ Activity destroy হয়ে আবার তৈরি হয়। ViewModel বেঁচে থাকে, আর ছোট UI state আমি saved state-এ রাখি।
>
> Android 10 থেকে multi-window-এ একসাথে কয়েকটা activity resumed থাকতে পারে। তাই user screen দেখছে না — এটা বুঝতে আমি `onStop` ব্যবহার করি, `onPause` না।

*English:*
> Two pairs matter most: `onStart`/`onStop` for visibility, and `onResume`/`onPause` for focus. When A opens B, A pauses first, B fully starts, and only then A stops — so heavy work in `onPause` delays the next screen.
>
> On a configuration change the Activity is destroyed and recreated; the ViewModel survives it, and small UI state goes into saved state.
>
> Since Android 10, several activities can be resumed at once in multi-window, so I use `onStop`, not `onPause`, to know the user can't see the screen.

**সাধারণ ভুল:**
- `onPause`-এ ভারী কাজ (বড় save, network)। পরের Activity এই কাজ শেষ হওয়ার জন্য অপেক্ষা করে।
- `onDestroy`-এর উপর জরুরি save-এর ভরসা রাখা। Process kill হলে এটা call-ই হয় না।
- `android:configChanges` দিয়ে rotation "ঠিক" করা, কিন্তু resource reload না হওয়ার কথা ভুলে যাওয়া। নতুন ভাষা বা orientation-এর string আর layout আসে না।

**Follow-up প্রশ্ন:** "`onSaveInstanceState` কখন call হয়?"

*বাংলায়:*
> Activity stop হওয়ার সময়, যেমন Home চাপলে। API 28 থেকে এটা `onStop`-এর পরে call হয়। User back চেপে Activity শেষ করলে এটা call হয় না, কারণ তখন state ফিরিয়ে আনার দরকার নেই।

*English:*
> When the Activity is being stopped, for example on Home. From API 28 it runs after `onStop`. It isn't called when the user finishes the Activity with Back, because there's nothing to restore.

[উপরে ফিরুন](#toc)

---

### <a id="q18"></a>Q18. Fragment lifecycle আর `viewLifecycleOwner`

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Fragment-এর দুইটা lifecycle আছে: Fragment নিজের, আর তার **View**-এর। View-এর lifecycle ছোট। Back stack-এ গেলে view destroy হয় (`onDestroyView`), কিন্তু Fragment বেঁচে থাকে। তাই UI-সংক্রান্ত সব observe `viewLifecycleOwner` দিয়ে করতে হয়, আর `onDestroyView`-এ binding null করতে হয়।

---

#### দুইটা lifecycle কেন

Fragment A থেকে B-তে গেলে A back stack-এ যায়। A-এর View তখন আর লাগে না, তাই memory বাঁচাতে system View-টা ফেলে দেয়। কিন্তু A object নিজে থাকে, যাতে back চাপলে ফিরে আসা যায়। ফিরে এলে নতুন View তৈরি হয়।

ফলে একই Fragment-এর জীবনে অনেকগুলো View আসে আর যায়। পুরনো View-এর reference কোথাও থেকে গেলে সেটাই leak।

```
onAttach → onCreate → onCreateView → onViewCreated → onStart → onResume
                                                                   ↓
onDetach ← onDestroy ← onDestroyView ← onStop ← onPause ←──────────┘
                           ↑
           back stack-এ গেলে এখানে থামে; ফিরে এলে আবার onCreateView থেকে
```

---

#### ঠিক pattern

```kotlin
class ProfileFragment : Fragment(R.layout.fragment_profile) {
    private var _binding: FragmentProfileBinding? = null
    private val binding get() = _binding!!     // শুধু onViewCreated আর onDestroyView-এর মাঝে পড়ুন

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        _binding = FragmentProfileBinding.bind(view)
        viewLifecycleOwner.lifecycleScope.launch {           // View-এর lifecycle, Fragment-এর না
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                viewModel.state.collect { binding.name.text = it.name }
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null              // না করলে পুরনো view-টা leak হয়
    }
}
```

দুইটা জিনিস একসাথে কাজ করছে। `viewLifecycleOwner` দিয়ে collect করলে View destroy হলেই collector থামে। আর `_binding = null` করলে Fragment পুরনো View ধরে রাখে না।

---

#### আরও যা জানা দরকার

- **Fragment-এ empty constructor বাধ্যতামূলক।** System process death-এর পরে Fragment নিজে আবার তৈরি করে, তখন খালি constructor call করে। Constructor-এ data দিলে সেটা তখন হারিয়ে যায়। তাই data পাঠান `arguments` Bundle দিয়ে, অথবা `FragmentFactory` ব্যবহার করুন।
- **Fragment Result API** — দুই Fragment-এর মধ্যে result পাঠাতে: `setFragmentResult("key", bundleOf(...))` আর `setFragmentResultListener`।
- **`commit()` vs `commitNow()`** — `commit` পরে চলে (async), `commitNow` সাথে সাথে চলে, কিন্তু back stack-এ যোগ করা যায় না।
- **`commitAllowingStateLoss`** — `onSaveInstanceState`-এর পরে commit করলে crash এড়াতে। কিন্তু এতে state হারানোর ঝুঁকি আছে, তাই খুব কম ব্যবহার করুন।

**Interviewer কেন জিজ্ঞেস করে:** অনেক কোম্পানির পুরনো code Fragment-এ লেখা। Compose-এ পুরো migrate হতে বছর লাগে। তাই এটা এখনো আসে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Fragment-এর দুইটা lifecycle: Fragment-এর নিজের, আর তার view-এর। Fragment back stack-এ থাকা অবস্থায় view destroy হয়ে যেতে পারে। তাই আমি সবসময় `viewLifecycleOwner` দিয়ে observe করি, আর `onDestroyView`-এ binding clear করি — না করলে পুরনো view leak হয়।
>
> Fragment-এ empty constructor লাগে, কারণ process death-এর পরে system নিজেই এটা আবার তৈরি করে। তাই data আমি arguments দিয়ে পাঠাই।
>
> দুই Fragment-এর মধ্যে result পাঠাতে shared listener না রেখে Fragment Result API ব্যবহার করি।

*English:*
> A Fragment has two lifecycles: its own and its view's. The view can be destroyed while the Fragment stays on the back stack, so I always observe with `viewLifecycleOwner` and clear the binding in `onDestroyView` — otherwise the old view leaks.
>
> Fragments also need an empty constructor, because the system recreates them after process death, so data goes through arguments.
>
> To pass results between fragments I use the Fragment Result API instead of shared listeners.

**সাধারণ ভুল:**
- Fragment-এর `lifecycleScope` বা `this` দিয়ে observe করা। View চলে গেলেও collector চলে, আর পুরনো view update করতে চায়।
- `onDestroyView`-এ binding null না করা। Back stack-এ থাকা প্রতিটা Fragment পুরো একটা view hierarchy memory-তে ধরে রাখে।
- Constructor-এ data পাঠানো। Process death-এর পরে system খালি constructor call করে, data হারিয়ে যায়।
- `commitAllowingStateLoss` দিয়ে crash চাপা দেওয়া। Crash যায়, কিন্তু user-এর state নীরবে হারায়।

**Follow-up প্রশ্ন:** "Fragment-এ binding `lateinit` না করে nullable কেন?"

*বাংলায়:*
> `lateinit`-কে আবার খালি করা যায় না। তাই `onDestroyView`-এ পুরনো view ছেড়ে দেওয়ার উপায় থাকে না, আর Fragment back stack-এ থাকার সময় view leak হয়। Nullable `_binding` রাখলে আমি সেটা `null` করে দিতে পারি ([Q1](#q1))।

*English:*
> A `lateinit` can't be cleared, so I can't release the old view in `onDestroyView`, and it leaks while the Fragment sits on the back stack. A nullable `_binding` lets me set it to `null`.

[উপরে ফিরুন](#toc)

---

### <a id="q19"></a>Q19. Process death কী? State কীভাবে ফিরিয়ে আনবেন?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** App background-এ থাকলে memory বাঁচাতে system পুরো process মেরে ফেলতে পারে। User আবার app-এ ফিরলে Android শেষ Activity আর Fragment আবার তৈরি করে — দেখে মনে হয় app কখনো বন্ধ হয়নি। কিন্তু **ViewModel আর memory-র সব data হারিয়ে যায়**। শুধু saved state Bundle থাকে। তাই ছোট আর জরুরি UI state রাখতে হয় `SavedStateHandle` বা `rememberSaveable`-এ, আর বড় data database-এ।

---

#### সমস্যাটা কোথায়

User-এর চোখে কিছুই হয়নি। সে checkout screen-এ ছিল, অন্য app-এ গেল, ফিরে এল — আবার checkout screen। কিন্তু ভেতরে এটা একদম নতুন process। ViewModel নতুন, singleton নতুন, সব খালি।

যে code ধরে নেয় "আগের screen-এ এটা set করা হয়েছিল", সেটা এখানে null পায়। এই bug সাধারণ testing-এ ধরা পড়ে না, কারণ rotation-এ সব ঠিক থাকে।

---

#### কী কোথায় বাঁচে

| ঘটনা | ViewModel | SavedStateHandle / `rememberSaveable` | Database / DataStore |
|---|---|---|---|
| Rotation (config change) | বাঁচে | বাঁচে | বাঁচে |
| Process death (system মেরেছে) | **হারায়** | বাঁচে | বাঁচে |
| User back চেপে বের হলো / swipe করে বন্ধ করল | হারায় | **হারায়** | বাঁচে |

শেষ সারিটা খেয়াল করুন। User নিজে বন্ধ করলে saved state-ও যায়, কারণ তখন ফিরিয়ে আনার কিছু নেই। যা সব অবস্থায় থাকতে হবে, সেটা database-এ।

---

#### ViewModel-এ — `SavedStateHandle`

```kotlin
@HiltViewModel
class CheckoutViewModel @Inject constructor(
    private val savedState: SavedStateHandle,
    private val repo: OrderRepository,
) : ViewModel() {

    // process death-এর পরেও ফিরে আসবে
    val selectedAddressId: StateFlow<String?> = savedState.getStateFlow("addressId", null)

    fun selectAddress(id: String) { savedState["addressId"] = id }
}
```

#### Compose-এ — `rememberSaveable`

```kotlin
@Composable
fun CommentBox() {
    var text by rememberSaveable { mutableStateOf("") }   // টাইপ করা লেখা হারাবে না
    TextField(value = text, onValueChange = { text = it })
}
```

---

#### কী রাখবেন, কী রাখবেন না

- রাখুন: id, selected tab, filter, টাইপ করা text, scroll position।
- রাখবেন না: list-এর পুরো data, bitmap। Bundle binder transaction-এর মাধ্যমে যায়, যার মোট limit ~১ MB। বেশি হলে `TransactionTooLargeException` crash হয়। Id রাখুন, আর data database থেকে আবার load করুন।

---

#### কীভাবে test করবেন

1. App-এ একটা screen-এ যান, কিছু টাইপ করুন।
2. Home button চাপুন (app background-এ যাবে)।
3. Terminal-এ চালান: `adb shell am kill com.your.package`
4. Recent apps থেকে app-এ ফিরুন। State আছে কি না দেখুন।

"Don't keep activities" developer option শুধু Activity destroy test করে — process death না। এই দুইটা আলাদা, এটা interview-এ বললে ভালো।

**Flutter-এর সাথে মিল:** Flutter-এও process death হয়, কিন্তু বেশিরভাগ Flutter app এটা handle করে না — user ফিরলে app শুরু থেকে চলে। Flutter-এর সমাধান হলো `RestorationMixin` আর `restorationScopeId`। Native Android-এ এটা অনেক বেশি স্বাভাবিক আর আশা করা হয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Process death মানে system app-কে background-এ মেরে ফেলে, আর user ফিরলে শেষ screen আবার তৈরি করে। Memory-র সব কিছু হারায় — ViewModel, singleton সবই। শুধু saved-state Bundle বাঁচে।
>
> তাই ছোট আর জরুরি UI state আমি `SavedStateHandle` বা `rememberSaveable`-এ রাখি, আর আসল data database-এ।
>
> Test করি app background-এ পাঠিয়ে `adb shell am kill` দিয়ে। কারণ "Don't keep activities" শুধু activity destroy test করে, process death না।

*English:*
> Process death is when the system kills the app in the background and later recreates the last screen when the user comes back. Everything in memory is gone — ViewModels and singletons too — and only the saved-state Bundle survives.
>
> So I keep small, critical UI state in `SavedStateHandle` or `rememberSaveable`, and real data in the database.
>
> I test it with `adb shell am kill` after sending the app to the background, because 'Don't keep activities' only tests activity destruction, not process death.

**সাধারণ ভুল:**
- "Singleton-এ রেখেছি, তাই নিরাপদ।" Process death-এ singleton-ও মরে যায়। ফিরে এসে null পায়, আর app crash করে। এটা Play Console-এ সবচেয়ে সাধারণ "rare crash"-গুলোর একটা।
- পুরো list বা bitmap Bundle-এ রাখা। ~১ MB limit পার হলে `TransactionTooLargeException`।

**Follow-up প্রশ্ন:** "'Don't keep activities' দিয়ে test করলে হবে না?"

*বাংলায়:*
> না। ওটা শুধু Activity destroy করে, process থেকে যায়। তাই ViewModel হারালেও singleton আর static data বেঁচে থাকে, আর singleton-এর bug ধরা পড়ে না। আসল process death দেখতে আমি background-এ পাঠিয়ে `adb shell am kill` চালাই।

*English:*
> No. It only destroys the Activity; the process stays alive, so singletons and static data survive and those bugs stay hidden. For real process death I background the app and run `adb shell am kill`.

[উপরে ফিরুন](#toc)

---

### <a id="q20"></a>Q20. Intent, task, back stack, launch mode, PendingIntent

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Intent হলো "কিছু করো" message। **Explicit** intent নির্দিষ্ট class খোলে। **Implicit** intent শুধু একটা action বলে ("এই URL খোলো"), আর system ঠিক করে কোন app খুলবে। **Task** হলো Activity-র একটা stack — user-এর চোখে এটাই back stack। Launch mode ঠিক করে নতুন Activity নতুন instance হবে, নাকি পুরনোটা আবার ব্যবহার হবে। **PendingIntent** মানে অন্য app-কে (notification, alarm) অনুমতি দেওয়া, যাতে সে পরে আপনার হয়ে একটা intent চালাতে পারে।

---

#### Launch mode — back stack কীভাবে বদলায়

Default-এ প্রতিবার Activity খুললে নতুন instance stack-এর উপরে বসে। একই notification তিনবার tap করলে একই screen তিনবার stack-এ জমে। Launch mode এই আচরণ বদলায়।

| Mode | আচরণ | কখন |
|---|---|---|
| `standard` (default) | প্রতিবার নতুন instance | বেশিরভাগ screen |
| `singleTop` | উপরে একই Activity থাকলে নতুন তৈরি না করে `onNewIntent()` call | notification থেকে খোলা screen, search |
| `singleTask` | Task-এ একটাই instance। থাকলে তার উপরের সবগুলো সরিয়ে দেয় | খুব কম, সাবধানে। Main Activity-তে দিলে launcher icon থেকে আবার খোলার সময় উপরের সব screen মুছে যায় — user তার জায়গা হারায় |
| `singleInstance` | নিজের আলাদা task-এ একা | খুব কম (launcher, call screen) |
| `singleInstancePerTask` (API 31+) | প্রতিটা task-এ একটা | multi-window document app |

Flag দিয়েও একই কাজ করা যায়: `FLAG_ACTIVITY_NEW_TASK`, `FLAG_ACTIVITY_CLEAR_TOP`, `FLAG_ACTIVITY_SINGLE_TOP`।

---

#### PendingIntent — Android 12 থেকে নিয়ম

PendingIntent অন্য app-এর হাতে যায়, আর সে এটা **আপনার app-এর identity আর permission নিয়ে** চালায়। তাই এটা কে বদলাতে পারবে, সেটা গুরুত্বপূর্ণ।

```kotlin
val pending = PendingIntent.getActivity(
    context,
    requestCode,
    Intent(context, OrderActivity::class.java).putExtra("orderId", id),   // explicit intent
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
)
```

- Android 12 (API 31) থেকে `FLAG_IMMUTABLE` বা `FLAG_MUTABLE` একটা দিতেই হবে, না দিলে crash।
- Default হিসেবে `IMMUTABLE` দিন। `MUTABLE` শুধু তখন, যখন অন্য app-কে intent বদলাতে দিতে হয় (যেমন inline reply notification)।
- Mutable PendingIntent একটা security ঝুঁকি ([Q55](#q55))। অন্য app এর ভেতরের intent বদলে আপনার identity দিয়ে চালাতে পারে।
- Android 14 (target 34) থেকে mutable PendingIntent-এ **implicit** intent দিলে crash হয়। তাই সবসময় explicit intent (component সহ) দিন।

---

#### আরও জানা দরকার

- **Package visibility (Android 11+):** অন্য app আছে কি না জানতে বা implicit intent query করতে manifest-এ `<queries>` লিখতে হয়।
- **`android:exported` (Android 12+):** যে component-এ intent-filter আছে, সেখানে `exported` স্পষ্ট করে লিখতে হয়।
- **Activity Result API:** `startActivityForResult` deprecated। এখন `registerForActivityResult(ActivityResultContracts.X)`।

**Flutter-এর সাথে মিল:** Flutter-এ `url_launcher` আসলে implicit intent পাঠায়। Notification থেকে app খোলার সময় Flutter-এ `singleTop` launch mode (default `FlutterActivity` setup-এ থাকে) কেন লাগে, সেটা এখান থেকে বোঝা যায়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Intent হলো message। Explicit intent নির্দিষ্ট component-কে target করে। Implicit intent শুধু action বলে, আর system app বেছে নেয়।
>
> Launch mode back stack নিয়ন্ত্রণ করে। Entry activity আর notification থেকে খোলা screen-এ আমি `singleTop` দিই, যাতে duplicate না হয়ে `onNewIntent` আসে। `singleTask` নিয়ে সাবধান থাকি, কারণ launcher থেকে আবার খুললে root-এর উপরের সব মুছে যায়।
>
> PendingIntent-এ Android 12 থেকে mutability বলে দিতেই হয়। আমি default-এ `FLAG_IMMUTABLE` নিই, কারণ mutable একটা অন্য app বদলে দিতে পারে। আর Android 14 থেকে implicit intent-সহ mutable PendingIntent এমনিতেই crash করে।

*English:*
> Intents are messages: explicit ones target a specific component, implicit ones describe an action and let the system choose the app.
>
> Launch modes control the back stack — I use `singleTop` for the entry activity and for screens opened from notifications, so I get `onNewIntent` instead of duplicates. I'm careful with `singleTask`, because relaunching from the launcher clears everything above the root.
>
> For PendingIntents, since Android 12 I must choose mutability; I default to `FLAG_IMMUTABLE`, because another app can change a mutable one, and since Android 14 a mutable one with an implicit intent crashes anyway.

**সাধারণ ভুল:**
- Main Activity-তে `singleTask` দেওয়া। Launcher icon থেকে ফিরলে উপরের সব screen মুছে যায়, user তার জায়গা হারায়।
- কারণ ছাড়া `FLAG_MUTABLE` দেওয়া। অন্য app intent বদলাতে পারে — security hole ([Q55](#q55))।
- Intent-filter থাকা component-এ `android:exported` না লেখা (Android 12+)।

**Follow-up প্রশ্ন:** "`singleTop` Activity-তে নতুন data কীভাবে পাবেন?"

*বাংলায়:*
> Activity আগে থেকেই উপরে থাকলে নতুন instance তৈরি হয় না, তাই `onCreate` আবার চলে না। নতুন intent আসে `onNewIntent()`-এ। আমি সেখানে নতুন data পড়ে screen update করি।

*English:*
> If the Activity is already on top, no new instance is created, so `onCreate` doesn't run again. The new intent arrives in `onNewIntent()`, and I read the new data and update the screen there.

[উপরে ফিরুন](#toc)

---

### <a id="q21"></a>Q21. Service, foreground service আর background limit

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** Service হলো UI ছাড়া কাজ চালানোর Android component। এর তিন ধরন আছে: **Started**, **Bound** (অন্য component তার সাথে যুক্ত হয়), আর **Foreground** (notification দেখায়, তাই user জানে কিছু চলছে)। Android 8 থেকে app background-এ থাকলে সাধারণ service চালানো যায় না। Android 14 থেকে প্রতিটা foreground service-কে একটা **type** বলতে হয়। তাই আজকাল বেশিরভাগ background কাজ WorkManager-এ যায়।

---

#### প্রথমে একটা ভুল ধারণা: Service মানে background thread না

Service default-এ **main thread**-এ চলে। "Service = background thread" ধারণাটা ভুল। Service শুধু system-কে বলে "এই app-এর একটা কাজ চলছে, process-টা রেখে দাও"। কাজটা কোন thread-এ চলবে, সেটা আপনাকেই ঠিক করতে হয়।

তাই ভেতরে coroutine বা thread নিজে চালাতে হয়। `LifecycleService` extend করলে `lifecycleScope` পাওয়া যায়। Service বন্ধ হলে সেই scope-এর coroutine-ও cancel হয়।

---

#### Background limit — version ধরে কী বদলেছে

User দেখতে পায় না এমন service battery আর memory খায়। তাই Google প্রায় প্রতিটা release-এ নিয়ম কড়া করেছে।

| Version | পরিবর্তন |
|---|---|
| Android 8 (API 26) | Background app সাধারণ service শুরু করতে পারে না। `startForegroundService()` এর পর অল্প সময়ের মধ্যে `startForeground()` call করতে হয়, না হলে crash/ANR। |
| Android 12 (API 31) | Background থেকে foreground service শুরু করা নিষেধ (কিছু ব্যতিক্রম ছাড়া)। |
| Android 13 (API 33) | Notification দেখাতে `POST_NOTIFICATIONS` permission লাগে। User চাইলে FGS বন্ধ করতে পারে (Task Manager থেকে)। |
| Android 14 (API 34) | Manifest-এ `foregroundServiceType` বাধ্যতামূলক, আর প্রতিটা type-এর নিজস্ব permission (`FOREGROUND_SERVICE_LOCATION` ইত্যাদি)। নতুন `shortService` type — ছোট জরুরি কাজ (প্রায় ৩ মিনিট), আলাদা permission ছাড়া। |
| Android 15 (API 35) | `dataSync` আর `mediaProcessing` type-এর সময়সীমা আছে (২৪ ঘণ্টায় মোট প্রায় ৬ ঘণ্টা)। `BOOT_COMPLETED` receiver থেকে `dataSync`, `camera`, `mediaPlayback`, `phoneCall`, `microphone` ইত্যাদি type-এর FGS শুরু করা যায় না। |

FGS মানে foreground service। Type দেওয়ার কারণ হলো, system জানতে চায় service-টা আসলে কী করছে। Type অনুযায়ী permission আর সময়সীমা আলাদা।

---

#### Foreground service ঘোষণা করা

Manifest-এ দুইটা permission আর service-এর type:

```xml
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<!-- type-এর নিজস্ব permission (Android 14+) -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />

<service
    android:name=".PlayerService"
    android:foregroundServiceType="mediaPlayback"
    android:exported="false" />
```

Service-এর ভেতরে শুরুতেই `startForeground()` call করুন, notification আর type দিয়ে:

```kotlin
class PlayerService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        // শুরুতেই — দেরি হলে crash/ANR
        ServiceCompat.startForeground(
            this, NOTIFICATION_ID, buildNotification(),
            ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK,   // manifest-এর type
        )
        return START_STICKY
    }
    override fun onBind(intent: Intent?): IBinder? = null   // bound না, তাই null
}
```

**`onStartCommand`-এর return value** — system service মেরে ফেললে কী হবে, সেটা এখানে বলে দেন:
- `START_STICKY` — system মারলে আবার চালু করে, কিন্তু intent ছাড়া। Music player-এর জন্য ঠিক।
- `START_NOT_STICKY` — আবার চালু করে না।
- `START_REDELIVER_INTENT` — আবার চালু করে, আর শেষ intent আবার দেয়।

---

#### কখন কোনটা

- **Foreground service:** music, navigation, call, workout tracking। মানে চলমান কাজ, যেটা user দেখছে।
- **WorkManager** ([Q42](#q42)): upload, sync, backup। দেরিতে চললেও সমস্যা নেই, কিন্তু শেষ হতেই হবে।
- **User-initiated data transfer job** (Android 14+): user নিজে শুরু করা বড় download বা upload। `JobInfo.Builder.setUserInitiated(true)`, permission `RUN_USER_INITIATED_JOBS`।
- `IntentService` deprecated। নতুন code-এ লিখবেন না।

**Flutter-এর সাথে মিল:** Flutter-এ এর সরাসরি জোড়া নেই। Background audio বা background কাজের plugin-গুলো ভেতরে এই native API-গুলোই ব্যবহার করে। তাই এই নিয়ম Flutter app-এও খাটে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Service UI ছাড়া কাজ চালায়, কিন্তু default-এ এটা main thread-এ চলে। অনেকে এটা ভুল বোঝে। তাই ভেতরের কাজের জন্য আমি নিজে coroutine চালাই।
>
> প্রতিটা release-এ background limit কড়া হয়েছে। Android 8 থেকে background app সাধারণ service শুরু করতে পারে না। 12 থেকে background থেকে foreground service-ও শুরু করা যায় না। আর 14 থেকে প্রতিটা foreground service-কে type আর তার permission ঘোষণা করতে হয়।
>
> তাই আমি foreground service রাখি শুধু চলমান কাজের জন্য, যেটা user দেখছে — যেমন media বা navigation। Sync আর upload যায় WorkManager-এ।

*English:*
> A Service runs work without UI, but by default it runs on the main thread — that's a common misunderstanding. So I start my own coroutine for the real work.
>
> Background limits got stricter with each release: since Android 8 background apps can't start normal services, since 12 they can't start foreground services from the background, and since 14 every foreground service must declare a type and its permission.
>
> So I use a foreground service only for ongoing work the user can see, like media or navigation, and WorkManager for sync and uploads.

**সাধারণ ভুল:**
- Service-এর ভেতরে সরাসরি ভারী কাজ করা। Service main thread-এ চলে, তাই UI আটকে যায়, ANR হতে পারে।
- `startForegroundService()`-এর পর `startForeground()` দেরিতে call করা। অল্প সময় পার হলেই crash বা ANR।
- Sync বা upload-এর জন্য foreground service চালানো। এটা WorkManager-এর কাজ। Android 15-এ `dataSync` type-এর সময়সীমাও আছে।
- `IntentService` ব্যবহার করা। এটা deprecated।

**Follow-up প্রশ্ন:** "User নিজে একটা বড় file download শুরু করলে কী ব্যবহার করবেন?"

*বাংলায়:*
> Android 14+ হলে আমি user-initiated data transfer job নিই — `JobInfo.Builder.setUserInitiated(true)`, সাথে `RUN_USER_INITIATED_JOBS` permission। কাজটা user নিজে শুরু করেছে, তাই system এটাকে সেভাবেই দেখে। এর জন্য আলাদা foreground service বানাতে হয় না।

*English:*
> On Android 14+, I use a user-initiated data transfer job — `JobInfo.Builder.setUserInitiated(true)` with the `RUN_USER_INITIATED_JOBS` permission. The user started the work, so the system treats it that way, and I don't need my own foreground service for it.

[উপরে ফিরুন](#toc)

---

### <a id="q22"></a>Q22. BroadcastReceiver আর ContentProvider

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** BroadcastReceiver system বা অন্য app-এর event শোনে, যেমন battery low, boot complete, network change। Android 8 থেকে বেশিরভাগ implicit broadcast manifest-এ register করা যায় না, runtime-এ code দিয়ে করতে হয়। ContentProvider অন্য app-এর সাথে data শেয়ার করার নিয়মিত উপায়। আজকাল এর সবচেয়ে বেশি ব্যবহার হলো `FileProvider`, মানে অন্য app-কে file দেওয়া।

---

#### BroadcastReceiver — runtime-এ register

Implicit broadcast মানে যে broadcast নির্দিষ্ট কোনো app-কে পাঠানো হয় না, সবার জন্য পাঠানো হয়। আগে অনেক app manifest-এ এগুলো শুনত। তাই একটা event-এ একসাথে অনেক app জেগে উঠত। এই কারণেই Android 8 থেকে বেশিরভাগ implicit broadcast শুধু runtime-এ register করা যায়। তখন receiver শুধু app চলার সময়েই শোনে।

```kotlin
// Runtime-এ register — Android 14 থেকে exported flag বাধ্যতামূলক
ContextCompat.registerReceiver(
    context, receiver,
    IntentFilter(Intent.ACTION_BATTERY_LOW),
    ContextCompat.RECEIVER_NOT_EXPORTED,   // অন্য app এই receiver-এ পাঠাতে পারবে না
)
// আর অবশ্যই: onStop / onDestroy-তে unregisterReceiver(receiver)
```

যা মনে রাখবেন:
- **`onReceive()` main thread-এ চলে।** আর এটা অল্প সময়ে শেষ করতে হয় (প্রায় ১০ সেকেন্ড, না হলে ANR)। লম্বা কাজ হলে WorkManager-এ পাঠান, অথবা `goAsync()` দিয়ে একটু বাড়তি সময় নিন।
- **`BOOT_COMPLETED` এখনো manifest-এ চলে।** এটা ব্যতিক্রমগুলোর একটা।
- **নিজের app-এর ভেতরে event পাঠাতে broadcast লাগে না।** Flow বা callback দিয়ে করুন। `LocalBroadcastManager` deprecated।

---

#### ContentProvider — app-এর বাইরে data দেওয়া

- Contacts, MediaStore, Calendar — এগুলো সব system-এর ContentProvider।
- এরা `content://` URI দিয়ে কাজ করে। Query করা হয় `ContentResolver` দিয়ে।
- **`FileProvider`:** Android 7 থেকে `file://` URI অন্য app-কে দিলে `FileUriExposedException` হয়। কারণ `file://` দিলে অন্য app-কে আপনার file system-এর path দিতে হয়। তাই Camera-কে ছবি রাখার জায়গা দিতে বা PDF share করতে `FileProvider.getUriForFile()` দিয়ে `content://` URI বানান।

**মজার তথ্য:** অনেক library (Firebase, WorkManager) আগে নিজের ContentProvider দিয়ে app শুরুর সময় নিজেকে initialize করত। কিন্তু প্রতিটা provider app startup ধীর করে। তাই Google **App Startup** library বানিয়েছে — সব initializer একটা provider-এ চলে ([Q47](#q47))।

**Flutter-এর সাথে মিল:** Battery বা network-এর মতো Flutter plugin ভেতরে এই receiver-ই register করে। আর file share বা camera-র plugin-এর জন্য Android-এ `FileProvider` setup লাগে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> BroadcastReceiver system বা app-এর event-এ সাড়া দেয়। Android 8 থেকে বেশিরভাগ implicit broadcast manifest-এ register করা যায় না, তাই আমি runtime-এ register করি। Android 14 থেকে সাথে exported বা not exported বলে দিই।
>
> `onReceive` main thread-এ চলে, আর সময়ও কম পায়। তাই লম্বা কিছু হলে আমি WorkManager-এ পাঠাই।
>
> ContentProvider app-এর মধ্যে data শেয়ার করে। আজকাল আমি মূলত `FileProvider` ব্যবহার করি, যাতে file নিরাপদে `file://`-এর বদলে `content://` URI দিয়ে শেয়ার হয়।

*English:*
> BroadcastReceivers react to system or app events, but since Android 8 most implicit broadcasts can't be registered in the manifest, so I register them at runtime and, since Android 14, mark them exported or not exported.
>
> `onReceive` runs on the main thread with a short time limit, so anything long goes to WorkManager.
>
> ContentProviders share data between apps; today I mostly use `FileProvider` to share files safely with `content://` URIs instead of `file://`.

**সাধারণ ভুল:**
- Runtime-এ register করে unregister না করা। Receiver context ধরে রাখে, তাই leak হয় ([Q23](#q23))।
- `onReceive()`-এ network বা disk-এর লম্বা কাজ করা। সময় পার হলে ANR।
- নিজের app-এর ভেতরে event পাঠাতে broadcast ব্যবহার করা। এটা দরকার ছাড়াই ভারী, আর `LocalBroadcastManager` deprecated। Flow বা callback যথেষ্ট।
- অন্য app-কে `file://` URI দেওয়া। Android 7 থেকে `FileUriExposedException`।

**Follow-up প্রশ্ন:** "App Startup library কেন এল?"

*বাংলায়:*
> আগে অনেক library নিজের ContentProvider দিয়ে app শুরুর সময় নিজেকে initialize করত। প্রতিটা provider startup-এ খরচ যোগ করে। App Startup সব initializer একটা provider-এ নিয়ে আসে, তাই startup দ্রুত হয়।

*English:*
> Many libraries used their own ContentProvider to initialize at app start, and every provider adds to startup time. App Startup runs all initializers through a single provider, so startup gets faster.

[উপরে ফিরুন](#toc)

---

### <a id="q23"></a>Q23. Context-এর ধরন কী কী? Context leak কীভাবে হয়?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** মূল Context দুইটা। **Application context** পুরো app-এর সমান বাঁচে। **Activity context** শুধু Activity-র সমান বাঁচে, আর এতে theme ও UI-র তথ্য থাকে। যে object Activity-র চেয়ে বেশি বাঁচে (singleton, ViewModel, repository), সে যদি Activity context ধরে রাখে, তাহলে destroy হওয়া Activity আর তার পুরো view tree garbage collect হতে পারে না। এটাই leak। Flutter-এর `BuildContext`-এর সাথে নাম মিললেও কাজ আলাদা — এখানে মূল প্রশ্ন হলো lifetime।

---

#### কোন কাজে কোন Context

| কাজ | কোন Context |
|---|---|
| View inflate, Dialog দেখানো, theme-এর রং পড়া | **Activity** (Application দিলে theme ভুল হবে, Dialog crash করবে) |
| Singleton, database, DataStore, WorkManager, analytics | **Application** |
| Activity শুরু করা | Activity (Application দিয়ে করলে `FLAG_ACTIVITY_NEW_TASK` লাগবে) |
| Resource string পড়া (locale ঠিক রাখতে) | Activity / configuration-aware context |

সহজ নিয়ম: UI-র কাজে Activity context। যা Activity-র চেয়ে বেশিদিন বাঁচে, তাকে Application context।

---

#### Leak কীভাবে হয় — চারটা সাধারণ উদাহরণ

সব leak-এর গল্প একই। লম্বা সময় বাঁচা কোনো object একটা ছোট সময় বাঁচা Activity-র reference ধরে রাখে। Activity destroy হয়, কিন্তু GC তাকে ছাড়তে পারে না।

```kotlin
// ১. Singleton-এ Activity রাখা
object ImageCache {
    lateinit var context: Context          // Activity দিলে leak
}

// ২. ViewModel-এ View বা Activity রাখা
class BadViewModel : ViewModel() {
    var activity: Activity? = null         // rotation-এর পরে পুরনো Activity আটকে থাকে
}

// ৩. Listener register করে unregister না করা
locationManager.requestLocationUpdates(provider, 1000L, 0f, activityListener)

// ৪. Anonymous / inner class Handler, যে delay দিয়ে message রেখেছে
handler.postDelayed({ textView.text = "done" }, 60_000)   // এক মিনিট Activity ধরে রাখে
```

দ্বিতীয়টা খেয়াল করুন। ViewModel rotation পার হয়ে বাঁচে, কিন্তু Activity নতুন করে তৈরি হয়। তাই ViewModel পুরনো Activity ধরে রাখে।

---

#### সমাধান

- লম্বা সময় বাঁচা object-কে `applicationContext` দিন।
- Lifecycle-aware component ব্যবহার করুন।
- যা register করেন, `onStop`/`onDestroy`-তে unregister করুন।
- ViewModel-এ কখনো View বা Activity রাখবেন না।
- Context লাগলে Hilt-এ `@ApplicationContext` inject করুন।
- Debug build-এ LeakCanary বাকিগুলো ধরে।

**Flutter-এর সাথে মিল:** Flutter plugin লেখার সময় `ActivityAware` interface-এর কারণ এটাই। Plugin-এ Activity reference রাখতে হয় attach/detach অনুযায়ী, না হলে leak হয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> পুরো ব্যাপারটা lifetime-এর। Application context process-এর সমান বাঁচে। Activity context শুধু Activity-র সমান বাঁচে, আর theme বহন করে।
>
> Singleton, ViewModel বা static field-এর মতো লম্বা সময় বাঁচা কিছু যদি Activity context ধরে রাখে, তাহলে পুরো Activity আর তার view tree garbage collect হতে পারে না।
>
> তাই UI-র কাজে আমি Activity context নিই, আর লম্বা সময় বাঁচা object-কে Application context দিই। যত listener register করি, প্রতিটার একটা unregister রাখি। বাকিটা debug build-এ LeakCanary ধরে।

*English:*
> It's all about lifetime. The application context lives as long as the process; an activity context lives as long as the activity and carries the theme.
>
> If something long-lived — a singleton, a ViewModel, a static field — holds an activity context, the whole activity and its view tree can't be garbage collected.
>
> So UI work uses the activity context, long-lived objects get the application context, and every listener I register has a matching unregister. LeakCanary catches the rest in debug builds.

**সাধারণ ভুল:**
- Singleton-এ Activity context রাখা। Singleton process-এর সমান বাঁচে, তাই Activity কখনো ছাড়া পায় না।
- ViewModel-এ View বা Activity রাখা। Rotation-এর পরে পুরনো Activity আটকে থাকে।
- Listener register করে unregister না করা। System service listener ধরে রাখে, listener ধরে রাখে Activity।
- লম্বা delay দিয়ে `postDelayed` করা lambda-তে View ধরা। Delay শেষ না হওয়া পর্যন্ত Activity memory-তে থাকে।
- উল্টো ভুল: Dialog বা inflate-এ Application context দেওয়া। Theme ভুল হয়, Dialog crash করে।

**Follow-up প্রশ্ন:** "Application context দিয়ে Activity শুরু করলে কী হয়?"

*বাংলায়:*
> Application context-এর কোনো task নেই, তাই `FLAG_ACTIVITY_NEW_TASK` দিতে হয়। সাধারণত আমি Activity context দিয়েই শুরু করি। Application context দিয়ে করলে flag-টা মনে করে দিই।

*English:*
> The application context has no task of its own, so I have to add `FLAG_ACTIVITY_NEW_TASK`. Normally I start activities from an activity context; if I use the application context, I add that flag.

[উপরে ফিরুন](#toc)

---

### <a id="q24"></a>Q24. Main thread, Looper, Handler আর ANR

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Main thread-এ একটা **Looper** চলে। সে একটা **MessageQueue** থেকে একটা একটা করে কাজ নিয়ে চালায় — touch event, frame আঁকা, lifecycle callback, সব। **Handler** দিয়ে এই queue-তে কাজ পাঠানো যায়। Main thread কোনো কাজে আটকে থাকলে queue-র বাকি কাজ চলে না। Input event ৫ সেকেন্ডের মধ্যে handle না হলে system **ANR** (App Not Responding) দেখায়। Dart-এর event loop-এর সাথে ধারণাটা মেলে: একটা thread, একটা queue, একবারে একটা কাজ।

---

#### Main thread কীভাবে কাজ করে

```
Main Thread
  └── Looper.loop()
        └── MessageQueue: [touch] [frame] [onResume] [your post{}] ...
              ↑
           Handler.post { } / View.post { } / coroutine Dispatchers.Main
```

- সব কাজ একই লাইনে দাঁড়িয়ে থাকে। সামনের কাজ লম্বা হলে পেছনের সবাই অপেক্ষা করে।
- `Dispatchers.Main` ভেতরে আসলে main Looper-এর Handler ব্যবহার করে।
- **Choreographer** প্রতিটা vsync-এ frame আঁকার কাজ queue-তে দেয়। 60 Hz screen-এ একটা frame-এর বাজেট ~১৬ ms, 120 Hz-এ ~৮ ms। কাজ এর চেয়ে বেশি সময় নিলে frame বাদ পড়ে — এটাই **jank**।

অর্থাৎ একই সমস্যার দুই মাত্রা আছে। কয়েক ms বেশি নিলে jank। কয়েক সেকেন্ড আটকে থাকলে ANR।

---

#### ANR কখন হয়

- Input event (touch, key) ~৫ সেকেন্ডে handle না হলে।
- BroadcastReceiver-এর `onReceive` অনেকক্ষণ চললে।
- Service শুরু হতে অনেক দেরি হলে, অথবা `startForeground()` সময়মতো call না হলে।

**সাধারণ কারণ:**
- Main thread-এ disk বা network IO।
- বড় JSON parse।
- `SharedPreferences.commit()` — এটা disk-এ লেখা শেষ না হওয়া পর্যন্ত আটকে থাকে।
- Lock-এর জন্য অপেক্ষা (অন্য thread lock ধরে রেখেছে)।
- Main thread থেকে সরাসরি binder call (system service)। এটা অন্য process-এ যায়, তাই সময় নিতে পারে।

---

#### Play Console আর খোঁজার উপায়

Android vitals-এ ANR rate দেখায়। User-perceived ANR rate প্রায় ০.৪৭%-এর বেশি হলে Google Play app-এর visibility কমিয়ে দিতে পারে। Crash rate-এর জন্য এই সীমা প্রায় ১.০৯%। তাই ANR শুধু UX-এর সমস্যা না, business-এর সমস্যাও।

কীভাবে খুঁজবেন: [Q46](#q46) দেখুন (StrictMode, Perfetto, Play Console-এর ANR trace)।

**Flutter-এর সাথে মিল:** Flutter-এর "platform thread" হলো এই Android main thread। Method channel handler-এ ভারী কাজ করলে Flutter app-এও ANR হয়। Flutter-এর UI আর raster thread আলাদা, তাই Dart-এ jank আর Android ANR দুইটা আলাদা জিনিস।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Main thread-এ একটা Looper চলে, যে MessageQueue থেকে কাজ নেয় — input, frame, lifecycle callback, আর Handler দিয়ে post করা সব কিছু। একটা message বেশি সময় নিলে পেছনের সবাই অপেক্ষা করে।
>
> Frame budget পার হলে — 60 Hz-এ প্রায় 16 ms — frame বাদ পড়ে। আর input প্রায় ৫ সেকেন্ডে handle না হলে ANR হয়।
>
> সাধারণ কারণ হলো main thread-এ disk বা network, lock-এর জন্য অপেক্ষা, আর ভারী parsing। আমি StrictMode দিয়ে আগেভাগে ধরি, তারপর Perfetto trace আর Play Console-এর ANR report দিয়ে নিশ্চিত হই।

*English:*
> The main thread runs a Looper that processes a MessageQueue — input, frames, lifecycle callbacks and anything posted with a Handler. If one message takes too long, everything behind it waits.
>
> Over the frame budget, about 16 ms at 60 Hz, frames drop; if input isn't handled in about 5 seconds, we get an ANR.
>
> The usual causes are disk or network on the main thread, lock contention and heavy parsing. I catch them early with StrictMode and confirm them with Perfetto traces and the ANR reports in Play Console.

**সাধারণ ভুল:**
- Main thread-এ `SharedPreferences.commit()` করা। Disk-এ লেখা শেষ না হওয়া পর্যন্ত UI আটকে থাকে।
- Main thread থেকে system service-এ binder call। অন্য process-এর উত্তরের জন্য অপেক্ষা করতে হয়।
- Flutter-এ method channel handler-এ ভারী কাজ করা। Handler platform thread-এ চলে, তাই পুরো app-এ ANR হয়।
- Jank আর ANR গুলিয়ে ফেলা। Jank হলো frame বাদ পড়া (ms), ANR হলো সেকেন্ডের পর সেকেন্ড আটকে থাকা।

**Follow-up প্রশ্ন:** "ANR কেন business-এর জন্যও গুরুত্বপূর্ণ?"

*বাংলায়:*
> Play Console-এর Android vitals ANR rate মাপে। User-perceived ANR rate প্রায় ০.৪৭%-এর বেশি হলে Google Play app-এর visibility কমিয়ে দিতে পারে। Crash rate-এর জন্য সীমা প্রায় ১.০৯%। তাই আমি এই দুইটা সংখ্যা release-এর পরে নিয়মিত দেখি।

*English:*
> Android vitals in Play Console tracks the ANR rate. If the user-perceived ANR rate goes above about 0.47%, Google Play can reduce the app's visibility; for the crash rate, the line is about 1.09%. So I watch both numbers after every release.

[উপরে ফিরুন](#toc)

---

# D. Jetpack Compose

> Flutter থেকে আসা আপনার সবচেয়ে বড় সুবিধা এই অংশে। Declarative UI-র চিন্তা আপনার আগে থেকেই আছে। শুধু নাম আর কিছু নিয়ম শিখতে হবে।

### <a id="q25"></a>Q25. Compose ভেতরে কীভাবে কাজ করে?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** `@Composable` function UI-র বর্ণনা দেয়, ঠিক Flutter-এর `build()`-এর মতো। Compose compiler plugin প্রতিটা composable-এ একটা লুকানো `Composer` parameter যোগ করে। প্রথমবার চালালে Compose একটা tree বানায়, আর সেটা **slot table**-এ রাখে। কোনো `State` বদলালে, যে composable সেই state **পড়েছিল**, শুধু সেটা আবার চলে — এটাকে বলে **recomposition**। প্রতিটা frame-এ তিনটা phase চলে: **Composition** (কী দেখাব), **Layout** (কোথায় আর কত বড়), **Drawing** (কীভাবে আঁকব)।

---

#### Flutter থেকে এলে — পাশাপাশি দেখুন

Interview-এ এই তুলনাটা খুব কাজে আসে:

| Flutter | Compose |
|---|---|
| Widget (immutable config object) | Composable function call (কোনো object থাকে না) |
| Element tree | Slot table + composition |
| RenderObject tree | `LayoutNode` tree |
| `setState()` → পুরো `build()` আবার চলে | State পড়া scope-টাই শুধু আবার চলে |
| `const` constructor → rebuild skip | Stable parameter → recomposition skip |
| `Key` | `key()` composable, Lazy list-এ `key =` |
| `BuildContext` | নেই। `CompositionLocal` দিয়ে ঢেকে দেওয়া |

সবচেয়ে বড় পার্থক্য চার নম্বর লাইনে। Flutter-এ `setState()` পুরো `build()` আবার চালায়। Compose আরও সূক্ষ্ম: যে scope state পড়েছিল, শুধু সেটাই আবার চলে।

---

#### State কীভাবে recomposition চালায় — Snapshot system

Compose জানে কোন composable কোন state পড়েছে। এটা হয় এভাবে:

1. `mutableStateOf()` একটা snapshot state object বানায়।
2. Composable চলার সময় যে state পড়ে, Compose তা লিখে রাখে ("এই scope এই state পড়েছে")।
3. State-এর value বদলালে Compose ওই scope-গুলোকে "invalid" দাগ দেয়।
4. পরের frame-এ শুধু invalid scope-গুলো আবার চলে। যে child-এর input বদলায়নি, সে **skip** হয় ([Q28](#q28))।

তাই আপনাকে `setState()` call করতে হয় না। State-এ লিখলেই হয়।

---

#### তিন phase — কোথায় state পড়ছেন, সেটা গুরুত্বপূর্ণ

| Phase | কী হয় | যদি এখানে state পড়েন |
|---|---|---|
| Composition | composable function চলে, UI tree তৈরি বা update হয় | state বদলালে ৩টা phase-ই আবার চলে |
| Layout | measure আর place (`Modifier.offset {}`, `Layout`) | শুধু layout + draw আবার চলে |
| Drawing | Canvas-এ আঁকা (`drawBehind {}`, `graphicsLayer {}`) | শুধু draw আবার চলে |

তাই দ্রুত বদলানো state (scroll, animation) যত পরের phase-এ পড়বেন, তত কম কাজ হবে ([Q29](#q29))।

---

#### দুইটা নিয়ম, যেগুলো এখান থেকেই আসে

- **Side effect সরাসরি রাখবেন না।** Composable function যেকোনো ক্রমে, parallel-এ, আর অনেকবার চলতে পারে বলে ধরে নিন। তাই এর ভেতরে network call বা global variable বদলানোর মতো কাজ সরাসরি রাখা যাবে না ([Q27](#q27))।
- **ভারী হিসাব `remember` দিয়ে cache করুন।** Composable-এর ভেতরের হিসাব প্রতিটা recomposition-এ আবার হয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Composable function UI-র বর্ণনা দেয়। Compose compiler একটা লুকানো Composer parameter যোগ করে, আর runtime tree-টা slot table-এ রাখে।
>
> Snapshot system মনে রাখে কোন scope কোন state পড়েছে। সেই state বদলালে শুধু ওই scope-গুলো recompose হয়। আর যে child-এর stable input বদলায়নি, সে skip হয়। প্রতিটা frame-এ তিনটা phase — composition, layout আর drawing। State যত পরের phase-এ পড়ি, কাজ তত কম।
>
> Composable অনেকবার আর যেকোনো ক্রমে চলতে পারে। তাই আমি এগুলোকে side effect থেকে মুক্ত রাখি।

*English:*
> Composable functions describe the UI. The Compose compiler adds a hidden Composer parameter, and the runtime keeps the tree in a slot table.
>
> The snapshot system tracks which scope read which state; when that state changes, only those scopes recompose, and children with unchanged stable inputs are skipped. Every frame has three phases — composition, layout and drawing — and reading state in a later phase means less work.
>
> Because composables can run often and in any order, I keep them free of side effects.

**সাধারণ ভুল:**
- Composable body-তে সরাসরি network call বা global variable বদলানো। Function অনেকবার চলে, তাই কাজটাও অনেকবার হয় ([Q27](#q27))।
- ভারী হিসাব `remember` ছাড়া রাখা। প্রতিটা recomposition-এ আবার হিসাব হয়।
- Scroll বা animation-এর মতো দ্রুত বদলানো state composition-এ পড়া। তখন প্রতিবার তিনটা phase-ই চলে, যেখানে শুধু layout বা draw যথেষ্ট ছিল।

**Follow-up প্রশ্ন:** "Recomposition কতবার হচ্ছে কীভাবে দেখবেন?"

*বাংলায়:*
> Android Studio-র Layout Inspector-এ recomposition count দেখা যায় — কোন composable কতবার চলেছে, আর কতবার skip হয়েছে। অনুমান না করে আমি আগে এটা দেখি।

*English:*
> The Layout Inspector in Android Studio shows recomposition counts — how many times each composable ran and how many times it was skipped. I check that first instead of guessing.

[উপরে ফিরুন](#toc)

---

### <a id="q26"></a>Q26. State, `remember`, `rememberSaveable`, state hoisting, UDF

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** `remember` recomposition পার হয়ে একটা value রাখে, কিন্তু configuration change আর process death-এ হারায়। `rememberSaveable` এগুলোর পরেও বাঁচে, কারণ এটা value Bundle-এ রাখে। **State hoisting** মানে state-কে composable থেকে বের করে caller-এ নিয়ে যাওয়া। তখন composable পায় শুধু `value` আর `onValueChange`। এতে composable stateless হয়, reuse আর test সহজ হয়। **UDF** (unidirectional data flow) মানে state নিচে নামে, event উপরে ওঠে।

---

#### `remember` বনাম `rememberSaveable`

Composable একটা function। প্রতিবার চললে ভেতরের local variable নতুন করে তৈরি হয়। `remember` value-টাকে composition-এ রেখে দেয়, তাই recomposition পার হয়ে বাঁচে।

কিন্তু rotation-এ Activity নতুন করে তৈরি হয়, composition-ও নতুন হয়। তখন `remember`-এর value হারায়। `rememberSaveable` value Bundle-এ রাখে, তাই configuration change আর process death-এর পরেও ফিরে আসে।

---

#### State hoisting — stateless আর stateful দুইটা রূপ

```kotlin
// Stateless — শুধু দেখায়। Preview আর test সহজ।
@Composable
fun QuantityPicker(
    quantity: Int,
    onQuantityChange: (Int) -> Unit,
    modifier: Modifier = Modifier,
) {
    Row(modifier) {
        IconButton(onClick = { onQuantityChange(quantity - 1) }, enabled = quantity > 1) {
            Icon(Icons.Default.Remove, contentDescription = "কমাও")
        }
        Text("$quantity")
        IconButton(onClick = { onQuantityChange(quantity + 1) }) {
            Icon(Icons.Default.Add, contentDescription = "বাড়াও")
        }
    }
}

// Stateful wrapper — দরকার হলে
@Composable
fun QuantityPicker() {
    var quantity by rememberSaveable { mutableIntStateOf(1) }
    QuantityPicker(quantity = quantity, onQuantityChange = { quantity = it })
}
```

Stateless রূপটা নিজে কিছু বদলায় না। Value আসে উপর থেকে, click গেলে event উপরে যায়। এটাই UDF। ফলে একই composable ViewModel-এর state দিয়েও চলে, preview-তে একটা fixed সংখ্যা দিয়েও চলে।

---

#### State কোথায় রাখবেন

| State | কোথায় |
|---|---|
| শুধু UI-র (expanded, animation, focus) | Composable-এ `remember` |
| UI-র কিন্তু হারানো যাবে না (টাইপ করা text, selected tab) | `rememberSaveable` |
| Business data (user, cart, list) | ViewModel-এ `StateFlow` |
| অনেক UI state একসাথে (জটিল form, scaffold) | একটা plain **state holder class** + `remember` (যেমন `rememberLazyListState()`) |

---

#### `derivedStateOf` — কখন লাগে

```kotlin
val listState = rememberLazyListState()

// ভুল: প্রতিটা item পার হলেই recomposition (index বদলায়), অথচ ফল শুধু true/false
val showButton = listState.firstVisibleItemIndex > 0

// ঠিক: শুধু true/false বদলালে recomposition
val showButton by remember { derivedStateOf { listState.firstVisibleItemIndex > 0 } }
```

নিয়ম: input যত ঘন ঘন বদলায়, output তার চেয়ে **কম** বদলালে `derivedStateOf` দিন। এখানে index প্রতিটা item-এ বদলায়, কিন্তু ফল বদলায় শুধু একবার — 0 থেকে বেশি হলে।

**Flutter-এর সাথে মিল:** `remember { mutableStateOf() }` ≈ `StatefulWidget`-এর state field + `setState`। State hoisting ≈ Flutter-এ "lift state up", যেমন `TextField`-এ controller বাইরে থেকে দেওয়া।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> `remember` recomposition পার হয়ে value রাখে। `rememberSaveable` configuration change আর process death-এর পরেও বাঁচে।
>
> আমি state hoist করি, যাতে বেশিরভাগ composable stateless থাকে — এরা একটা value আর একটা event callback নেয়। এতে reuse, preview আর test সহজ হয়। State নিচে নামে, event উপরে ওঠে। Business state থাকে ViewModel-এ। আর expanded flag-এর মতো শুধু UI-র state composable-এই থাকে।
>
> Input যখন result-এর চেয়ে অনেক বেশি বদলায়, তখন আমি `derivedStateOf` নিই। যেমন scroll position থেকে একটা "button দেখাও" flag।

*English:*
> `remember` keeps a value across recompositions; `rememberSaveable` also survives configuration changes and process death.
>
> I hoist state so most composables are stateless — they take a value and an event callback — which makes them reusable, easy to preview and easy to test. State flows down, events go up. Business state lives in the ViewModel; pure UI state, like an expanded flag, stays in the composable.
>
> And I use `derivedStateOf` when the input changes much more often than the result, like scroll position turning into a 'show button' flag.

**সাধারণ ভুল:**
- `remember { mutableListOf<Item>() }` লেখা। List-এর ভেতরে item যোগ করলে Compose জানে না, তাই UI বদলায় না। হয় `mutableStateListOf()` ব্যবহার করুন, নয়তো immutable list রাখুন আর পুরো list বদলান (`items = items + newItem`)।
- `Modifier` parameter না রাখা, অথবা প্রথম optional parameter হিসেবে না রাখা। এটা Compose API-র নিয়ম। না রাখলে caller বাইরে থেকে padding বা size দিতে পারে না।
- টাইপ করা text বা selected tab শুধু `remember`-এ রাখা। Rotation-এ user-এর লেখা হারিয়ে যায়।

**Follow-up প্রশ্ন:** "`derivedStateOf` সব জায়গায় দিলে সমস্যা কী?"

*বাংলায়:*
> এর নিজের একটা খরচ আছে। Output যদি input-এর মতোই ঘন ঘন বদলায়, তাহলে কোনো recomposition বাঁচে না, শুধু খরচটা যোগ হয়। তাই আমি এটা দিই শুধু যখন output input-এর চেয়ে কম বদলায়।

*English:*
> It has its own cost. If the output changes as often as the input, it saves no recompositions and only adds overhead. So I use it only when the output changes less often than the input.

[উপরে ফিরুন](#toc)

---

### <a id="q27"></a>Q27. Side effect API: `LaunchedEffect`, `DisposableEffect`, `SideEffect`, `rememberUpdatedState`

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** Side effect হলো composable-এর বাইরের জগতে কিছু করা — network, analytics, listener। Composable অনেকবার চলে, তাই এগুলো নিয়ন্ত্রিত জায়গায় রাখতে হয়। `LaunchedEffect(key)` composition-এ ঢুকলে একটা coroutine চালায়। Key বদলালে আগেরটা cancel করে নতুনটা চালায়। `DisposableEffect` এমন কাজের জন্য, যার cleanup লাগে (`onDispose`)। আর `rememberCoroutineScope` click-এর মতো event থেকে coroutine চালাতে। Flutter-এ এগুলোর কাজ করে `initState`, `didUpdateWidget` আর `dispose`।

---

#### সমস্যাটা কোথায়

Composable body প্রতিটা recomposition-এ আবার চলে। Body-তে সরাসরি `viewModel.load()` লিখলে প্রতিবার load হবে। Listener যোগ করলে প্রতিবার নতুন listener যোগ হবে, আর কেউ সরাবে না।

তাই Compose কয়েকটা API দেয়। এরা ঠিক করে দেয়, কাজটা কখন শুরু হবে, কখন আবার শুরু হবে, আর কখন বন্ধ হবে।

---

#### কোন API কখন

| API | কখন | Flutter-এ কাছাকাছি |
|---|---|---|
| `LaunchedEffect(key)` | Composition-এ ঢুকে suspend কাজ। Key বদলালে restart | `initState` + `didUpdateWidget` |
| `DisposableEffect(key)` | Listener register/unregister | `initState` + `dispose` |
| `rememberCoroutineScope()` | Click বা callback থেকে coroutine (scroll, snackbar) | — |
| `SideEffect {}` | প্রতিটা সফল recomposition-এর পরে, non-Compose জিনিস update | `WidgetsBinding.addPostFrameCallback` |
| `rememberUpdatedState(x)` | লম্বা effect-এর ভেতরে সর্বশেষ value চাই, কিন্তু restart চাই না | — |
| `produceState` | Non-Compose source থেকে `State` বানানো | `FutureBuilder` / `StreamBuilder` |
| `snapshotFlow {}` | Compose state-কে Flow বানানো | — |

Key-টাই আসল জিনিস। Key মানে "এটা বদলালে কাজটা নতুন করে করো"। Composable composition থেকে বের হলে effect-এর coroutine নিজে থেকেই cancel হয়।

---

#### এক screen-এ চারটা ব্যবহার

```kotlin
@Composable
fun ProductScreen(productId: String, onTimeout: () -> Unit, viewModel: ProductViewModel) {

    // productId বদলালে আবার load
    LaunchedEffect(productId) {
        viewModel.load(productId)
    }

    // onTimeout বদলাতে পারে, কিন্তু timer restart চাই না
    val currentOnTimeout by rememberUpdatedState(onTimeout)
    LaunchedEffect(Unit) {
        delay(30_000)
        currentOnTimeout()        // সর্বশেষ lambda call হবে
    }

    // Lifecycle observer — cleanup জরুরি
    val lifecycleOwner = LocalLifecycleOwner.current
    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_RESUME) viewModel.refresh()
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }

    // Click থেকে coroutine
    val scope = rememberCoroutineScope()
    val snackbar = remember { SnackbarHostState() }
    Button(onClick = { scope.launch { snackbar.showSnackbar("Cart-এ যোগ হয়েছে") } }) {
        Text("Add")
    }
}
```

`rememberUpdatedState`-এর অংশটা আলাদা করে দেখুন। Timer-এর key `Unit`, তাই এটা একবারই চলে। কিন্তু এর মধ্যে parent নতুন `onTimeout` দিতে পারে। `onTimeout`-কে key বানালে timer আবার শূন্য থেকে শুরু হতো। `rememberUpdatedState` timer না থামিয়ে সর্বশেষ lambda-টা হাতে রাখে।

> **নোট:** নতুন version-এ `LocalLifecycleOwner` আসে `androidx.lifecycle.compose` package থেকে। আর ON_RESUME-এর কাজ আরও সহজে লেখা যায়: `LifecycleResumeEffect(Unit) { viewModel.refresh(); onPauseOrDispose { } }`।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Composable অনেকবার চলতে পারে, তাই side effect-এর জন্য নিয়ন্ত্রিত entry point লাগে। `LaunchedEffect` composition-এর সাথে বাঁধা একটা coroutine চালায়, আর key বদলালে restart হয়। Listener-এর মতো যেটার cleanup লাগে, তার জন্য `DisposableEffect`। আর click-এর মতো event থেকে launch করতে `rememberCoroutineScope`।
>
> লম্বা চলা effect-এ সর্বশেষ callback দরকার হলে, restart না করে, আমি `rememberUpdatedState` নিই।
>
> সবচেয়ে বেশি যে bug দেখি, সেটা ভুল key। Parameter-এর উপর নির্ভর করা কাজে `LaunchedEffect(Unit)` দেওয়া।

*English:*
> Composables can run many times, so side effects need controlled entry points. `LaunchedEffect` runs a coroutine tied to the composition and restarts when its key changes; `DisposableEffect` is for anything that needs cleanup, like listeners; `rememberCoroutineScope` is for launching from events like a click.
>
> `rememberUpdatedState` lets a long-running effect use the latest callback without restarting.
>
> The most common bug I see is a wrong key — `LaunchedEffect(Unit)` for work that depends on a parameter.

**সাধারণ ভুল:**
- `LaunchedEffect(true)` বা `LaunchedEffect(Unit)` দিয়ে এমন কাজ করা, যেটা একটা parameter-এর উপর নির্ভর করে। Parameter বদলালেও effect আবার চলে না, তাই screen পুরনো data দেখায়। Key-তে সেই parameter দিন।
- Composable body-তে সরাসরি `viewModel.load()` লেখা। প্রতিটা recomposition-এ call হবে।
- Data load-এর জন্য `LaunchedEffect`-এর চেয়ে ভালো: ViewModel-এর `init {}` অথবা `stateIn(WhileSubscribed)`। তাহলে rotation-এ আবার load হয় না, কারণ ViewModel rotation পার হয়ে বাঁচে কিন্তু composition নতুন হয়।

**Follow-up প্রশ্ন:** "`onTimeout`-কে key বানালেই তো হয়, `rememberUpdatedState` কেন?"

*বাংলায়:*
> Key বানালে প্রতিবার নতুন lambda এলে effect restart হয়। তাতে 30 সেকেন্ডের timer আবার শূন্য থেকে শুরু হয়। আমি চাই timer চলতে থাকুক, শুধু শেষে সর্বশেষ lambda-টা call হোক। `rememberUpdatedState` ঠিক এটাই করে।

*English:*
> If it's a key, every new lambda restarts the effect, and the 30-second timer starts again from zero. I want the timer to keep running and only call the latest lambda at the end. That's exactly what `rememberUpdatedState` does.

[উপরে ফিরুন](#toc)

---

### <a id="q28"></a>Q28. Stability, skipping আর strong skipping mode

**কত ঘন ঘন:** Common · **কঠিনতা:** Hard

**সংক্ষেপে:** Recomposition-এর সময় Compose একটা child composable **skip** করতে পারে, যদি তার সব parameter আগের মতোই থাকে। এর জন্য parameter-গুলো **stable** হতে হয়। Stable মানে Compose বিশ্বাস করতে পারে যে value বদলালে সে জানতে পারবে। আগে unstable parameter থাকলে composable কখনো skip হতো না। **Strong skipping mode** (Kotlin 2.0.20 থেকে default) এটা বদলেছে: এখন unstable parameter-ও instance (`===`) দিয়ে তুলনা হয়, আর lambda নিজে থেকে remember হয়। Flutter-এর `const` widget rebuild skip করার মতো একই চিন্তা।

---

#### সমস্যাটা কোথায়

Skip করতে হলে Compose-কে বলতে হয় "আগের আর এখনের parameter একই"। কিন্তু parameter যদি mutable হয়, ভেতরে বদলে গেলেও object একই থাকতে পারে। তখন `equals()`-এর উপর ভরসা করা যায় না। তাই Compose শুধু stable type-এর বেলায় এই check বিশ্বাস করে।

**Stable কী:**
- Primitive, `String`, function type (lambda)।
- সব property `val` আর stable type — এমন class (যেমন `data class User(val id: String, val name: String)`)।
- `@Immutable` বা `@Stable` annotation দেওয়া class।
- Compose-এর `State<T>`, `MutableState<T>`। এগুলো বদলালে Compose নিজেই জানতে পারে।

**Unstable কী:**
- `var` property আছে এমন class।
- `List<T>`, `Map`, `Set` — কারণ এগুলো interface, ভেতরে `MutableList` থাকতে পারে।
- অন্য module-এর class, যে module Compose compiler দিয়ে build হয়নি (যেমন pure Kotlin `domain` module)। Compiler সেই class দেখেনি, তাই নিশ্চিত হতে পারে না।

---

#### Strong skipping-এর পরে কী বদলেছে

| | আগে | Strong skipping (এখন default) |
|---|---|---|
| Unstable parameter আছে | কখনো skip না | `===` (একই instance) হলে skip |
| Stable parameter | `equals()` দিয়ে তুলনা | একই, `equals()` |
| Lambda | Unstable জিনিস capture করলে প্রতিবার নতুন | নিজে থেকে `remember` হয় |

---

#### তাহলে এখনো সমস্যা কোথায়?

প্রতিবার নতুন instance বানালে। যেমন ViewModel-এ `state.copy(items = items.filter {...})`। `filter` নতুন list বানায়, তাই `===` মেলে না, আর skip হয় না — content একই হলেও।

সমাধান তিনটা:

```kotlin
// ১. kotlinx.collections.immutable ব্যবহার করুন — Compose এটাকে stable জানে
data class PostsUiState(val posts: ImmutableList<Post> = persistentListOf())

// ২. নিজের class-এ annotation দিন (আপনি নিশ্চিত হলে)
@Immutable
data class Post(val id: String, val title: String, val tags: List<String>)

// ৩. Stability config file — অন্য module-এর class-কে stable ঘোষণা
// compose_compiler_config.conf:
// com.example.domain.model.*
```

প্রথম দুইটায় type stable হয়, তাই তুলনা হয় `equals()` দিয়ে। নতুন instance হলেও content একই হলে skip হয়।

**কীভাবে দেখবেন:** Compose compiler report চালু করুন। এটা প্রতিটা composable-এর পাশে লেখে `restartable skippable` কি না, আর প্রতিটা parameter `stable` না `unstable`। অনুমান না করে report দেখুন।

**Flutter-এর সাথে মিল:** Flutter-এ `const` widget rebuild skip করে। Compose-এ stable + equal parameter একই কাজ করে। Flutter-এ `==` override না করলে identity দিয়ে তুলনা হয় — strong skipping-এর `===`-এর মতো।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Input না বদলালে Compose একটা composable skip করতে পারে। আর সেই check-এর উপর ভরসা করা যাবে কি না, সেটা ঠিক করে stability। Strong skipping-এর আগে একটা unstable parameter, যেমন `List`, থাকলেই composable কখনো skip হতো না।
>
> Strong skipping এখন default। এতে unstable parameter instance দিয়ে তুলনা হয়, আর lambda নিজে থেকে remember হয়। যে ফাঁদটা বাকি থাকে, তা হলো প্রতিটা state update-এ নতুন instance বানানো। তাই আমি immutable collection বা stability config ব্যবহার করি, আর অনুমান না করে compiler report দেখি।
>
> Mutable অংশ থাকলে আমি কখনো class-এ `@Immutable` দিই না। তাতে performance-এর সমস্যা correctness bug হয়ে যায়।

*English:*
> Compose can skip a composable when its inputs haven't changed, and stability decides whether it can trust that check. Before strong skipping, one unstable parameter, like a `List`, meant the composable never skipped.
>
> With strong skipping, which is now the default, unstable parameters are compared by instance and lambdas are remembered automatically. The trap that's left is creating new instances on every state update, so I use immutable collections or a stability config, and I check compiler reports instead of guessing.
>
> I never mark a class `@Immutable` if it has mutable parts — that turns a performance problem into a correctness bug.

**সাধারণ ভুল:**
- সব class-এ `@Immutable` বসিয়ে দেওয়া, ভেতরে `var` থাকা সত্ত্বেও। তখন Compose ভুল করে skip করবে, আর UI পুরনো data দেখাবে। এটা performance bug-এর চেয়ে খারাপ, কারণ এটা correctness bug।
- ধরে নেওয়া যে strong skipping সব সমস্যা মিটিয়ে দিয়েছে। প্রতিবার `filter` বা `map` দিয়ে নতুন list বানালে `===` মেলে না, তাই skip হয় না।
- Compiler report না দেখে অনুমানে optimize করা।

**Follow-up প্রশ্ন:** "`List` কেন unstable, অথচ `String` stable?"

*বাংলায়:*
> `String` immutable, তাই একই value মানে সবসময় একই content। `List` একটা interface। এর পেছনে `MutableList` থাকতে পারে, যেটা object না বদলেই ভেতরে বদলে যায়। তাই Compose `List`-এর `equals()`-এ ভরসা করতে পারে না। আমি `ImmutableList` দিই, যাতে compiler নিশ্চিত হতে পারে।

*English:*
> `String` is immutable, so the same value always means the same content. `List` is an interface — there might be a `MutableList` behind it that changes without the object changing. So Compose can't trust its `equals()`. I use `ImmutableList` so the compiler can be sure.

[উপরে ফিরুন](#toc)

---

### <a id="q29"></a>Q29. Compose performance কীভাবে ভালো করবেন?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** আগে মাপুন, তারপর ঠিক করুন। আর মাপুন **release build**-এ, কারণ debug build-এ Compose অনেক ধীর চলে, তাই ছবিটা ভুল আসে। এরপর বড় লাভ আসে পাঁচটা জায়গা থেকে: দ্রুত বদলানো state পরের phase-এ পড়া, lazy list-এ `key`, ভারী হিসাব `remember` করা, `derivedStateOf` দিয়ে বাড়তি recomposition কমানো, আর Baseline Profile। Flutter-এ যেমন profile mode ছাড়া performance মাপেন না, এখানেও ঠিক তাই।

---

#### আগে বুঝুন: Compose-এর তিনটা phase

প্রতিটা frame-এ Compose তিনটা ধাপ চালায়:
- **Composition** — কোন UI থাকবে, সেটা ঠিক করে। Composable function এখানে চলে।
- **Layout** — প্রতিটা জিনিসের মাপ আর জায়গা ঠিক করে।
- **Draw** — pixel আঁকে।

একটা state কোন phase-এ পড়া হচ্ছে, সেটাই ঠিক করে state বদলালে কোন phase আবার চলবে। Composition-এ পড়লে তিনটাই আবার চলে। শুধু layout বা draw-এ পড়লে composition পুরোটা skip হয়। Performance-এর বেশিরভাগ কৌশল এই একটা কথা থেকেই আসে।

---

#### ১. State পড়া পিছিয়ে দিন (defer reads)

Scroll offset বা animation value প্রতি frame-এ বদলায়। এটা composition-এ পড়লে প্রতি frame-এ recomposition হয়। সমাধান হলো value-টা lambda হিসেবে পাঠানো, আর lambda-ওয়ালা modifier-এর ভেতরে পড়া। তখন value শুধু layout বা draw phase-এ পড়া হয়।

```kotlin
// ভুল: scroll-এর প্রতিটা pixel-এ Header recompose হয়
@Composable
fun Header(scrollOffset: Int) {
    Box(Modifier.offset(y = (-scrollOffset / 2).dp)) { ... }
}

// ঠিক: শুধু layout phase চলে, composition skip
@Composable
fun Header(scrollOffset: () -> Int) {
    Box(Modifier.offset { IntOffset(0, -scrollOffset() / 2) }) { ... }
}

// alpha বা scale: শুধু draw phase
Box(Modifier.graphicsLayer { alpha = scrollProgress() })
```

পার্থক্যটা ছোট দেখায়: `offset(y = ...)` বনাম `offset { ... }`। কিন্তু প্রথমটায় value composition-এ পড়া হয়, দ্বিতীয়টায় layout-এ।

---

#### ২. Lazy list-এ `key` আর `contentType`

```kotlin
LazyColumn {
    items(items = posts, key = { it.id }, contentType = { it.type }) { post ->
        PostCard(post)
    }
}
```

Key না দিলে Compose item চেনে তার position দিয়ে। তাই উপরে একটা item যোগ হলে সবার position সরে যায়, আর Compose ভাবে সব item বদলে গেছে। ফল দুইটা:
- সব item আবার recompose হয়।
- Item-এর ভেতরে `remember` করা state ভুল item-এ চলে যায়। এটা শুধু ধীর না, এটা bug।

`contentType` বলে দেয় কোন item কোন ধরনের। তাই Compose একই ধরনের item-এর composition আবার কাজে লাগাতে পারে।

---

#### ৩. Composition-এ ভারী কাজ নয়

Composable function অনেকবার চলতে পারে। তাই ভেতরে sort বা filter করলে প্রতিবার সেই খরচ হয়।

```kotlin
val sorted = remember(contacts) { contacts.sortedBy { it.name } }   // contacts বদলালেই শুধু
```

আরও ভালো: ViewModel-এ আগে থেকেই sort করে রাখুন। তখন UI শুধু দেখায়, হিসাব করে না।

---

#### ৪. `derivedStateOf` — input বেশি বদলায়, output কম

কিছু state প্রতি frame-এ বদলায়, কিন্তু আপনার শুধু দরকার একটা হ্যাঁ/না। যেমন list scroll হলে index বদলায়, কিন্তু "scroll-to-top button দেখাব কি না" শুধু মাঝে মাঝে বদলায়। `derivedStateOf { listState.firstVisibleItemIndex > 0 }` দিলে result বদলালেই শুধু recomposition হয়, প্রতিটা index-এ না।

---

#### ৫. Backwards write করবেন না

যে state composition-এ পড়েছেন, সেটা একই composition-এ লিখলে সমস্যা। লেখার ফলে state বদলায়, তাতে আবার recomposition হয়, সেখানে আবার লেখা হয়। এভাবে অসীম recomposition loop হয়।

---

#### ৬. Baseline Profile

Baseline Profile app-এর গুরুত্বপূর্ণ code path (startup, scroll) আগে থেকে compile করে রাখে। Compose একটা library হিসেবে app-এর সাথে আসে, তাই প্রথম চালানোয় তার code এখনো compile হয়নি। Profile সেই খরচটা আগেই মিটিয়ে দেয়। Compose app-এ এটা প্রায় বাধ্যতামূলক ([Q47](#q47))।

---

#### সমস্যা কোথায়, কীভাবে খুঁজবেন

- Layout Inspector → recomposition count। কোন composable বেশি চলছে, সরাসরি দেখা যায়।
- Compose compiler report → stability ([Q28](#q28))। কোন class unstable, তাই skip হচ্ছে না।
- Perfetto / System trace-এ composition tracing।
- Macrobenchmark দিয়ে scroll-এর frame time ([Q46](#q46))।

**Flutter-এর সাথে মিল:** Flutter-এ `AnimatedBuilder`-এর `child` parameter দিয়ে আপনি একই কাজ করেন — যা বদলায় না, সেটা rebuild থেকে বাঁচানো। আর Flutter-এও debug mode-এ performance মাপা ভুল, profile mode লাগে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি আগে release build-এ মাপি। Debug-এ Compose অনেক ধীর, তাই ওখানে মাপলে ভুল জায়গায় সময় নষ্ট হয়।
>
> তারপর বড় লাভগুলো নিই। দ্রুত বদলানো state, যেমন scroll offset, আমি `offset {}` বা `graphicsLayer {}`-এর মতো lambda modifier-এ পড়ি, যাতে composition skip হয়। Lazy item-এ stable key আর content type দিই। ভারী কাজ `remember` করি, আর বাড়তি recomposition কমাতে `derivedStateOf` ব্যবহার করি।
>
> শেষে Baseline Profile যোগ করি, এতে startup আর প্রথম scroll অনেক ভালো হয়। প্রতিটা পরিবর্তন আমি Layout Inspector-এর recomposition count আর Macrobenchmark দিয়ে নিশ্চিত করি।

*English:*
> First I measure in a release build, because debug Compose is much slower and gives the wrong picture.
>
> Then the big wins are: read fast-changing state in layout or draw with lambda modifiers like `offset {}` and `graphicsLayer {}`, give lazy items stable keys and content types, remember expensive work, and use `derivedStateOf` to cut extra recompositions.
>
> Last, I add Baseline Profiles, which help startup and the first scroll a lot. I confirm every change with Layout Inspector recomposition counts and Macrobenchmark.

**সাধারণ ভুল:**
- Debug build-এ মেপে সিদ্ধান্ত নেওয়া। যে জিনিস debug-এ ধীর, release-এ হয়তো কোনো সমস্যাই না।
- Lazy list-এ `key` না দেওয়া। শুধু বাড়তি recomposition না, item-এর `remember` করা state ভুল item-এ চলে যায়।
- Composable-এর ভেতরে সরাসরি sort বা filter করা। প্রতিটা recomposition-এ সেই খরচ আবার হয়।
- যে state composition-এ পড়েছেন, সেটা একই composition-এ লেখা। Recomposition loop তৈরি হয়।

**Follow-up প্রশ্ন:** "`remember` আর `derivedStateOf`-এর পার্থক্য কী?"

*বাংলায়:*
> `remember(key)` একটা হিসাব cache করে, আর key বদলালে আবার হিসাব করে। `derivedStateOf` অন্য state থেকে নতুন state বানায়, আর result বদলালেই শুধু reader-কে recompose করায়। Input যখন output-এর চেয়ে অনেক বেশি বদলায়, যেমন scroll index থেকে একটা boolean, তখন আমি `derivedStateOf` নিই।

*English:*
> `remember(key)` caches a calculation and redoes it when the key changes. `derivedStateOf` builds a state from other states and only recomposes readers when the result changes. I use it when the input changes much more often than the output, like a scroll index turned into a boolean.

[উপরে ফিরুন](#toc)

---

### <a id="q30"></a>Q30. Modifier-এর ক্রম আর CompositionLocal

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** Modifier বাম থেকে ডানে, বাইরে থেকে ভেতরে প্রয়োগ হয়। তাই ক্রম বদলালে ফল বদলায়: আগে `padding` তারপর `background` দিলে রং padding-এর ভেতরে থাকে, উল্টো দিলে padding সহ পুরোটা রঙিন হয়। `CompositionLocal` হলো tree-র নিচে parameter না পাঠিয়ে data পৌঁছানোর উপায়। Theme, `LocalContext`, `LocalLifecycleOwner` এভাবেই আসে। Flutter-এ এটা `InheritedWidget`।

---

#### Modifier-এর ক্রম — প্রতিটা modifier পরেরটাকে মুড়ে রাখে

Chain-টাকে Flutter-এর widget nesting-এর মতো ভাবুন। বাম দিকের modifier বাইরের wrapper, ডান দিকেরটা ভেতরের। প্রতিটা modifier তার পরের সবকিছুকে মুড়ে রাখে। তাই `padding` আগে এলে, তার পরের `background` ছোট জায়গা পায়।

```kotlin
// রং পুরো ১০০dp জুড়ে, লেখা ভেতরে ১৬dp সরে
Box(Modifier.size(100.dp).background(Color.Red).padding(16.dp))

// আগে ১৬dp ফাঁকা, তারপর বাকি অংশে রং
Box(Modifier.size(100.dp).padding(16.dp).background(Color.Red))
```

ক্রম শুধু দেখতে কেমন লাগে তা না, আচরণও বদলায়। Touch target-এ এটা সবচেয়ে বেশি চোখে পড়ে:

```kotlin
// clickable আগে: padding সহ পুরোটা চাপা যায় (বড় touch target — ভালো)
Text("Retry", Modifier.clickable { retry() }.padding(16.dp))

// clickable পরে: শুধু লেখাটুকু চাপা যায়
Text("Retry", Modifier.padding(16.dp).clickable { retry() })
```

---

#### CompositionLocal — parameter না পাঠিয়ে নিচে value পৌঁছানো

সমস্যাটা হলো, theme বা spacing-এর মতো জিনিস প্রায় সব composable-এর লাগে। প্রতিটা function-এ parameter হিসেবে পাঠালে signature ভরে যায়। CompositionLocal একটা value tree-র উপরে একবার provide করে, আর নিচের যে কেউ `.current` দিয়ে পড়ে।

```kotlin
data class Spacing(val small: Dp = 4.dp, val medium: Dp = 8.dp, val large: Dp = 16.dp)

val LocalSpacing = staticCompositionLocalOf { Spacing() }

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    CompositionLocalProvider(LocalSpacing provides Spacing()) {
        MaterialTheme(content = content)
    }
}

// যেকোনো জায়গায়
val spacing = LocalSpacing.current
```

দুই রকম CompositionLocal আছে। পার্থক্য হলো value বদলালে কে recompose হয়:

| | `staticCompositionLocalOf` | `compositionLocalOf` |
|---|---|---|
| Value বদলালে | Provider-এর নিচের **পুরো** tree recompose | শুধু যারা `.current` পড়েছে |
| কখন | প্রায় কখনো বদলায় না (theme token, spacing) | মাঝে মাঝে বদলায় |

`static` কেন ভালো, যদি পুরো tree recompose হয়? কারণ এটা কে পড়ছে তার হিসাব রাখে না, তাই পড়ার খরচ কম। Value প্রায় কখনো না বদলালে এটাই লাভ।

---

#### কখন CompositionLocal ব্যবহার করবেন না

Screen-এর business data বা ViewModel পাঠাতে না। এতে dependency লুকিয়ে যায়: function-এর signature দেখে বোঝা যায় না সে কী চায়। Preview আর test-ও কঠিন হয়, কারণ সেখানে আলাদা করে provide করতে হয়। সাধারণ parameter বেশি পরিষ্কার।

**Flutter-এর সাথে মিল:** `CompositionLocal` = `InheritedWidget`। `LocalSpacing.current` = `Theme.of(context)`। Flutter-এ `Padding` আর `Container` widget nesting-এর ক্রম যেমন ফল বদলায়, Modifier chain-ও তেমন।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Modifier ক্রম অনুযায়ী, বাইরে থেকে ভেতরে প্রয়োগ হয়। তাই ক্রম বদলালে দেখতে কেমন লাগে আর আচরণ — দুটোই বদলায়। যেমন `clickable` আগে দিয়ে তারপর `padding` দিলে touch target বড় হয়।
>
> CompositionLocal tree-র নিচে value পৌঁছায় parameter ছাড়াই। আমি এটা theme, spacing বা lifecycle owner-এর মতো সব জায়গায় লাগে এমন জিনিসের জন্য নিই। প্রায় কখনো বদলায় না এমন value-এর জন্য `staticCompositionLocalOf` দিই, কারণ বদলালে পুরো subtree recompose হয়।
>
> Screen-এর data-র জন্য আমি CompositionLocal নিই না। এতে dependency লুকিয়ে যায়, আর preview আর test কঠিন হয়।

*English:*
> Modifiers apply in order, from outside to inside, so the order changes both the look and the behavior — for example `clickable` before `padding` gives a bigger touch target.
>
> CompositionLocal passes values down the tree implicitly, which is right for cross-cutting things like theme, spacing or the lifecycle owner. I use `staticCompositionLocalOf` for values that almost never change, because a change recomposes the whole subtree.
>
> I avoid CompositionLocal for screen data, because it hides dependencies and makes previews and tests harder.

**সাধারণ ভুল:**
- `clickable` শেষে দেওয়া। Touch target ছোট হয়ে যায়, ব্যবহারকারী বোতাম মিস করে।
- ViewModel বা screen data CompositionLocal দিয়ে পাঠানো। Composable কী চায় তা লুকিয়ে যায়, preview ভাঙে।
- ঘন ঘন বদলানো value-এ `staticCompositionLocalOf` দেওয়া। প্রতিবার provider-এর নিচের পুরো tree recompose হয়।

**Follow-up প্রশ্ন:** "`staticCompositionLocalOf` আর `compositionLocalOf` — কোনটা কখন?"

*বাংলায়:*
> `compositionLocalOf` মনে রাখে কে `.current` পড়েছে, তাই value বদলালে শুধু তারাই recompose হয়। `static` এই হিসাব রাখে না, তাই বদলালে পুরো subtree recompose হয়, কিন্তু পড়া সস্তা। Theme token-এর মতো প্রায় স্থির value-এ আমি `static` নিই, মাঝে মাঝে বদলায় এমন value-এ `compositionLocalOf`।

*English:*
> `compositionLocalOf` tracks who read `.current`, so only those readers recompose on a change. The static one doesn't track, so a change recomposes the whole subtree, but reads are cheaper. I use static for near-constant values like theme tokens, and `compositionLocalOf` for values that change now and then.

[উপরে ফিরুন](#toc)

---

### <a id="q31"></a>Q31. View আর Compose একসাথে — interop আর migration

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Interop দুই দিকেই চলে। Compose-এর ভেতরে পুরনো View দেখাতে `AndroidView` (MapView, AdView, WebView)। XML বা Fragment-এর ভেতরে Compose দেখাতে `ComposeView`। বড় app একবারে rewrite হয় না, ধাপে ধাপে migrate হয়: নতুন screen Compose-এ, তারপর ছোট reusable component, শেষে পুরনো screen। সবার আগে design system Compose-এ বানানো সবচেয়ে কাজের। Flutter-এ native view embed করতে যেমন platform view লাগে, `AndroidView` সেই জায়গার কাজ করে।

---

#### দুই দিকের interop

```kotlin
// Compose-এর ভেতরে View
@Composable
fun MapBox(location: LatLng) {
    AndroidView(
        factory = { context -> MapView(context).apply { onCreate(null) } },
        update = { mapView -> mapView.moveTo(location) },   // recomposition-এ চলে
    )
}
```

`AndroidView`-এর দুইটা অংশ:
- `factory` View তৈরি করে। এটা একবার চলে।
- `update` চলে recomposition-এ। State থেকে View-কে update করার কাজ এখানে হয়। তাই এখানে নতুন View বানাবেন না, শুধু আগেরটা বদলান।

```kotlin
// Fragment-এর ভেতরে Compose
override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, saved: Bundle?) =
    ComposeView(requireContext()).apply {
        setViewCompositionStrategy(ViewCompositionStrategy.DisposeOnViewTreeLifecycleDestroyed)
        setContent { AppTheme { ProfileScreen() } }
    }
```

---

#### `ViewCompositionStrategy` কেন লাগে

Fragment-এর দুইটা lifecycle আছে: Fragment-এর নিজের, আর তার **view**-এর। Back stack-এ গেলে view destroy হয়, কিন্তু Fragment বেঁচে থাকে। Composition-কে view lifecycle-এর সাথে বাঁধতে হয়। না বাঁধলে view destroy হলেও composition বেঁচে থাকে, আর সেটা leak।

---

#### Migration plan

Big-bang rewrite-এ অনেক দিন নতুন কিছু ship হয় না, আর ঝুঁকি বেশি। তাই ধাপে ধাপে:

1. Compose dependency আর theme যোগ করুন। পুরনো XML theme-এর রং থেকে Compose theme বানান।
2. সব **নতুন** screen Compose-এ লিখুন।
3. Design system (button, card, text style) Compose-এ বানান।
4. পুরনো screen-এর ছোট অংশ (list item, dialog) `ComposeView` দিয়ে বদলান।
5. যে screen-এ সবচেয়ে বেশি bug বা পরিবর্তন হয়, সেটা পুরো migrate করুন।
6. শেষে Fragment সরিয়ে Navigation Compose।

প্রতিটা ধাপে screenshot test রাখুন, যাতে UI চুপচাপ বদলে না যায়।

যে screen বেশি বদলায়, সেটা আগে কেন? কারণ ওখানেই migration-এর লাভ সবচেয়ে বেশি ফেরত আসে। যে screen কেউ ছোঁয় না, সেটা পরে করলেও চলে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Interop দুই দিকেই চলে। Compose-এর ভেতরে পুরনো View রাখতে `AndroidView`, আর XML বা Fragment-এর ভেতরে Compose রাখতে `ComposeView`। Fragment-এ আমি ঠিক `ViewCompositionStrategy` দিই, যাতে view lifecycle-এর সাথে composition-ও dispose হয়।
>
> Migration আমি ধাপে ধাপে করি। আগে theme আর design system, তারপর সব নতুন screen Compose-এ, তারপর যে screen সবচেয়ে বেশি বদলায়। পুরো সময় screenshot test রাখি, যাতে চোখে না পড়া UI পরিবর্তন ধরা পড়ে।

*English:*
> Interop works both ways: `AndroidView` puts a classic View inside Compose, and `ComposeView` puts Compose inside XML or a Fragment. In a Fragment I set the right `ViewCompositionStrategy`, so the composition is disposed with the view lifecycle.
>
> For migration I go step by step: theme and design system first, every new screen in Compose, then the screens that change most often — with screenshot tests to catch visual changes.

**সাধারণ ভুল:**
- Fragment-এ `ViewCompositionStrategy` না দেওয়া। View destroy হলেও composition বেঁচে থাকে, leak হয়।
- `AndroidView`-এর `update`-এ ভারী কাজ বা নতুন View তৈরি করা। `update` প্রতিটা recomposition-এ চলে।
- Design system ছাড়া screen migrate শুরু করা। প্রতিটা screen নিজের মতো button আর রং বানায়, পরে সব আবার মেলাতে হয়।

**Follow-up প্রশ্ন:** "পুরো app একবারে Compose-এ rewrite করবেন না কেন?"

*বাংলায়:*
> একবারে rewrite মানে অনেক দিন feature ship বন্ধ, আর শেষে একসাথে অনেক ঝুঁকি। ধাপে ধাপে করলে প্রতিটা ধাপ ছোট, আলাদা release হয়, আর screenshot test দিয়ে ধরা যায় কিছু বদলাল কি না। Interop আছে বলেই দুইটা একসাথে চালানো যায়।

*English:*
> A full rewrite stops feature work for a long time and puts all the risk in one release. Step by step, each change is small, ships on its own, and screenshot tests show if anything changed. Interop is what lets both run side by side.

[উপরে ফিরুন](#toc)

---

### <a id="q32"></a>Q32. Navigation Compose

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** `NavHost` একটা graph রাখে, আর `NavController` back stack চালায়। Navigation 2.8 থেকে route হলো `@Serializable` class, তাই argument type-safe, string জোড়া দিতে হয় না। Screen-এর মধ্যে পুরো object না পাঠিয়ে শুধু **id** পাঠান, আর পরের screen-এর ViewModel database বা repository থেকে data নেয়। প্রতিটা back stack entry-র নিজের ViewModel scope আছে। Flutter-এ এটা `go_router` আর `go_router_builder`-এর typed route-এর মতো।

---

#### Type-safe route আর ViewModel-এ argument পড়া

আগে route ছিল string, যেমন `"product/{id}"`। Typo হলে compile হতো, কিন্তু runtime-এ ভাঙত। এখন route একটা class, তাই compiler argument check করে।

```kotlin
@Serializable object Home
@Serializable data class ProductDetail(val productId: String)

@Composable
fun AppNavHost(navController: NavHostController = rememberNavController()) {
    NavHost(navController, startDestination = Home) {
        composable<Home> {
            HomeScreen(onProductClick = { id -> navController.navigate(ProductDetail(id)) })
        }
        composable<ProductDetail> {
            ProductDetailRoute(onBack = navController::popBackStack)
        }
    }
}

@HiltViewModel
class ProductDetailViewModel @Inject constructor(
    savedStateHandle: SavedStateHandle,
    repo: ProductRepository,
) : ViewModel() {
    // route-এর argument SavedStateHandle-এ থাকে
    private val productId = savedStateHandle.toRoute<ProductDetail>().productId
    val product = repo.observe(productId).stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), null)
}
```

---

#### কেন id, object না

দুইটা কারণ:
- Argument `SavedStateHandle`-এ, মানে Bundle-এ যায়। Process death-এ এটা বাঁচে, কিন্তু Bundle-এর size limit আছে ([Q19](#q19))। বড় object রাখলে crash হতে পারে।
- পুরো object পাঠালে দুই screen-এ data-র দুইটা copy থাকে। একটা বদলালে অন্যটা পুরনো থাকে। Single source of truth ভাঙে।

---

#### Back stack-এর দরকারি option

```kotlin
navController.navigate(Home) {
    popUpTo(Login) { inclusive = true }   // login screen back stack থেকে সরাও
    launchSingleTop = true                // উপরে Home থাকলে আরেকটা বানিও না
}

// Bottom navigation-এ tab বদলানো
navController.navigate(tab.route) {
    popUpTo(navController.graph.findStartDestination().id) { saveState = true }
    launchSingleTop = true
    restoreState = true                   // tab-এর আগের scroll আর stack ফিরিয়ে আনো
}
```

Bottom tab-এ `saveState` আর `restoreState` না দিলে tab বদলালেই আগের tab-এর stack আর scroll হারিয়ে যায়। ব্যবহারকারী ফিরে এসে আবার শুরু থেকে দেখে।

Checkout-এর মতো কয়েক screen-এর flow-এ একটা ViewModel শেয়ার করতে চাইলে, সেটাকে nested graph-এর back stack entry-তে scope করুন ([Q35](#q35))।

---

#### Navigation 3 (নভেম্বর ২০২৫ থেকে stable)

এটা Compose-এর জন্য নতুন করে বানানো library। নতুন Compose project-এ Google এটাই ব্যবহার করতে বলে।

মূল পার্থক্য: back stack এখানে **আপনার নিজের** একটা observable list। Library-র ভেতরে লুকানো না।
- `NavDisplay` সেই list দেখায়।
- `entryProvider` ঠিক করে কোন key-তে কোন screen।
- Navigate মানে list-এ key যোগ করা। Back মানে list থেকে সরানো।
- **Scene** দিয়ে বড় screen-এ list আর detail পাশাপাশি দেখানো যায়।

```kotlin
@Serializable data object HomeKey : NavKey
@Serializable data class DetailKey(val productId: String) : NavKey

@Composable
fun AppNav() {
    val backStack = rememberNavBackStack(HomeKey)
    NavDisplay(
        backStack = backStack,
        onBack = { backStack.removeLastOrNull() },
        entryProvider = entryProvider {
            entry<HomeKey> { HomeScreen(onProductClick = { id -> backStack.add(DetailKey(id)) }) }
            entry<DetailKey> { key -> ProductDetailRoute(productId = key.productId) }
        },
    )
}
```

প্রতিটা entry-র নিজের ViewModel চাইলে `entryDecorators`-এ ViewModel store decorator যোগ করতে হয়। উপরের Navigation 2 code পুরনো project-এ সবচেয়ে বেশি দেখবেন। তাই দুইটাই জানুন, আর migration নিয়ে কথা বলতে পারলে ভালো।

**Flutter-এর সাথে মিল:** `go_router`-এর typed route (`go_router_builder`) = type-safe route। `context.go()` vs `context.push()` ≈ `popUpTo` দিয়ে stack বদলানো vs সাধারণ `navigate`। Bottom tab-এর `restoreState` ≈ go_router-এর `StatefulShellRoute`।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Navigation Compose-এ আমি type-safe route নিই — serializable class — তাই argument compile time-এই check হয়। Screen-এর মধ্যে আমি শুধু id পাঠাই। পরের screen-এর ViewModel `SavedStateHandle` থেকে id পড়ে, আর repository থেকে data আনে। এতে source of truth একটাই থাকে, আর process death-এও কাজ করে।
>
> প্রতিটা back stack entry একটা ViewModel scope। Checkout-এর মতো কয়েক ধাপের flow-এ আমি shared ViewModel nested graph-এ scope করি। Bottom navigation-এ `saveState` আর `restoreState` দিই, যাতে প্রতিটা tab নিজের stack রাখে।
>
> নতুন, শুধু-Compose project-এ আমি Navigation 3 নেব, যেটা ২০২৫-এর শেষে stable হয়েছে। সেখানে back stack শুধু আমার নিজের একটা list, তাই adaptive list-detail layout অনেক সহজ হয়।

*English:*
> With Navigation Compose I use type-safe routes — serializable classes — so arguments are checked at compile time. I pass only ids between screens; the destination ViewModel reads the id from `SavedStateHandle` and loads the data from the repository. That keeps one source of truth and survives process death.
>
> Each back stack entry is a ViewModel scope, and for multi-step flows like checkout I scope a shared ViewModel to a nested graph. For bottom navigation I use `saveState` and `restoreState`, so each tab keeps its own stack.
>
> For new Compose-only projects I'd go with Navigation 3, stable since late 2025: the back stack is just a list I own, which makes adaptive list-detail layouts much simpler.

**সাধারণ ভুল:**
- Argument-এ পুরো object পাঠানো। Bundle-এর size limit-এ crash হতে পারে, আর data-র দুইটা copy তৈরি হয়।
- Bottom tab-এ `saveState`/`restoreState` না দেওয়া। Tab বদলালেই আগের stack আর scroll হারায়।
- Login-এর পরে `popUpTo(Login) { inclusive = true }` না দেওয়া। Back চাপলে ব্যবহারকারী আবার login screen-এ ফিরে যায়।

**Follow-up প্রশ্ন:** "Navigation 2 থেকে Navigation 3-এ আসল পার্থক্য কী?"

*বাংলায়:*
> Navigation 2-তে back stack `NavController`-এর ভেতরে থাকে, আমি শুধু তাকে command দিই। Navigation 3-এ back stack আমার নিজের observable list — যোগ করলে navigate, সরালে back। List আমার হাতে, তাই Scene দিয়ে বড় screen-এ list আর detail পাশাপাশি দেখানো সহজ।

*English:*
> In Navigation 2 the back stack lives inside `NavController` and I send it commands. In Navigation 3 the back stack is my own observable list — add to navigate, remove to go back. Because I own the list, showing list and detail side by side with Scenes on large screens is simple.

[উপরে ফিরুন](#toc)

---

# E. Architecture

### <a id="q33"></a>Q33. MVVM vs MVI, UiState আর one-off event

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** MVVM-এ ViewModel কয়েকটা observable state আর কয়েকটা public function দেয়। MVI-তে পুরো screen-এর **একটাই immutable state** থাকে, আর UI সবকিছু **intent/action** হিসেবে একটা জায়গায় পাঠায়। আজকের Android-এ বেশিরভাগ team দুটোর মিশ্রণ ব্যবহার করে: MVVM ViewModel, কিন্তু একটা `UiState` data class আর UDF (unidirectional data flow — state নিচে নামে, action উপরে ওঠে)। Flutter-এ MVI মানে Bloc, MVVM মানে Cubit বা Riverpod `Notifier`।

---

#### একটা state, একটা entry point

কয়েকটা আলাদা `StateFlow` রাখলে সমস্যা হয়। যেমন `isLoading` একটা flow-এ, `errorMessage` আরেকটায়। দুইটা আলাদা সময়ে update হয়, তাই UI এক মুহূর্তের জন্য অমিল state দেখতে পারে। একটা `UiState` রাখলে পুরো screen এক সাথে, এক বারে বদলায়।

```kotlin
data class LoginUiState(
    val email: String = "",
    val password: String = "",
    val isLoading: Boolean = false,
    val errorMessage: String? = null,
    val isLoggedIn: Boolean = false,          // navigation-ও state
)

// UI যা যা করতে পারে, সব এখানে
sealed interface LoginAction {
    data class EmailChanged(val value: String) : LoginAction
    data class PasswordChanged(val value: String) : LoginAction
    data object Submit : LoginAction
    data object ErrorShown : LoginAction
}

@HiltViewModel
class LoginViewModel @Inject constructor(private val auth: AuthRepository) : ViewModel() {
    private val _state = MutableStateFlow(LoginUiState())
    val state: StateFlow<LoginUiState> = _state.asStateFlow()

    fun onAction(action: LoginAction) {
        when (action) {
            is LoginAction.EmailChanged -> _state.update { it.copy(email = action.value) }
            is LoginAction.PasswordChanged -> _state.update { it.copy(password = action.value) }
            LoginAction.Submit -> submit()
            LoginAction.ErrorShown -> _state.update { it.copy(errorMessage = null) }
        }
    }

    private fun submit() = viewModelScope.launch {
        _state.update { it.copy(isLoading = true) }
        auth.login(_state.value.email, _state.value.password)
            .onSuccess { _state.update { it.copy(isLoading = false, isLoggedIn = true) } }
            .onFailure { e -> _state.update { it.copy(isLoading = false, errorMessage = e.message) } }
    }
}
```

`update {}` কেন, `_state.value = ...` না? `update` atomic: পুরনো value পড়া, নতুন বানানো আর লেখা — একসাথে হয়। দুইটা coroutine একসাথে লিখলেও একজনের পরিবর্তন হারায় না।

UI-র দিকে navigation-ও state থেকে আসে:

```kotlin
@Composable
fun LoginRoute(onLoggedIn: () -> Unit, viewModel: LoginViewModel = hiltViewModel()) {
    val state by viewModel.state.collectAsStateWithLifecycle()

    LaunchedEffect(state.isLoggedIn) {
        if (state.isLoggedIn) onLoggedIn()
    }
    LoginScreen(state = state, onAction = viewModel::onAction)
}
```

---

#### One-off event — সমস্যাটা কোথায়

Snackbar বা navigation একবারই হওয়ার কথা। কিন্তু UI সবসময় শুনছে না। Rotation-এর সময়, বা app background-এ গেলে, collector কিছুক্ষণ থাকে না। ওই সময় event পাঠালে সেটা হারাতে পারে। তিনটা পথ আছে, আর interview-এ এই trade-off বলাটাই আসল:

| পথ | ভালো | খারাপ |
|---|---|---|
| **State হিসেবে** (`errorMessage`, পরে `ErrorShown`) | কখনো হারায় না। Process death-এও থাকতে পারে। Test সহজ | একটু বেশি code। UI-কে "দেখানো হয়েছে" জানাতে হয় |
| **`Channel` + `receiveAsFlow()`** | কম code, সহজ লাগে | Collector না থাকলে buffer-এ থাকে, কিন্তু কিছু edge case-এ (config change-এর ঠিক মুহূর্তে) হারাতে পারে |
| **`SharedFlow(replay = 0)`** | — | Collector না থাকলে event সরাসরি হারায়। Event-এর জন্য এড়িয়ে চলুন |

Google-এর পরামর্শ হলো event-কেও state হিসেবে রাখা, আর UI handle করার পরে ViewModel-কে জানানো। উপরের code-এ `errorMessage` দেখানোর পরে UI `ErrorShown` পাঠায়, তখন ViewModel সেটা `null` করে।

---

#### MVVM vs MVI

| | MVVM | MVI |
|---|---|---|
| State | কয়েকটা আলাদা flow হতে পারে | একটাই immutable state |
| Input | অনেক public function | একটা `onAction(Action)` |
| ভালো | সহজ, কম boilerplate | Predictable, debug সহজ (প্রতিটা action log করা যায়) |
| খারাপ | State ছড়িয়ে যেতে পারে | বড় state object, অনেক `copy()` |

**Flutter-এর সাথে মিল:** MVI ≈ Bloc (Event → Bloc → State)। MVVM ≈ Cubit বা Riverpod `Notifier` (function call → state)। Bloc-এর `BlocListener` দিয়ে navigation করা হলো "event as state"-এর মতো চিন্তা।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> বাস্তবে আমি দুটোর মিশ্রণ নিই। ViewModel MVVM-এর মতো, কিন্তু প্রতিটা screen-এ একটাই immutable UiState আর unidirectional data flow — এটাই MVI-এর কাজের অংশ। User action একটা entry point দিয়ে আসে, ViewModel `update {}` দিয়ে state বদলায়, আর UI শুধু সেটা দেখায়।
>
> Navigation বা snackbar-এর মতো one-off event-কে আমি state হিসেবে রাখতে পছন্দ করি। UI handle করার পরে ViewModel-কে জানায়। কারণ SharedFlow-এ event পাঠালে, তখন কেউ collect না করলে সেটা হারিয়ে যায়। ছোট app-এ Channel একটা চলনসই trade-off।

*English:*
> In practice I use a hybrid: MVVM ViewModels, but with one immutable UiState per screen and unidirectional data flow, which is the useful part of MVI. User actions come in through one entry point, the ViewModel updates the state with `update {}`, and the UI just renders it.
>
> For one-off events like navigation or a snackbar, I prefer to model them as state and let the UI tell the ViewModel when it's handled, because events in a SharedFlow can be lost when nobody is collecting. A Channel is a fair trade-off in simpler apps.

**সাধারণ ভুল:**
- One-off event-এর জন্য `SharedFlow(replay = 0)`। Rotation-এর মুহূর্তে collector না থাকলে event চুপচাপ হারিয়ে যায়।
- Error দেখানোর পরে state clear না করা (`ErrorShown` না পাঠানো)। Rotation-এর পরে একই snackbar আবার দেখায়।
- `_state.value = _state.value.copy(...)` লেখা। দুইটা coroutine একসাথে লিখলে একজনের পরিবর্তন হারায়, তাই `update {}`।

**Follow-up প্রশ্ন:** "Channel দিয়ে event পাঠালে সমস্যা কী?"

*বাংলায়:*
> Channel buffer রাখে, তাই collector না থাকলেও event সাধারণত অপেক্ষা করে — SharedFlow-এর চেয়ে ভালো। কিন্তু config change-এর ঠিক মুহূর্তে কিছু edge case-এ হারাতে পারে। তাই যেখানে event হারানো চলে না, যেমন payment-এর পরে navigation, সেখানে আমি state নিই।

*English:*
> A Channel buffers, so an event usually waits when nobody collects — better than SharedFlow. But in some edge cases, right at a config change, it can still be lost. Where losing an event is not okay, like navigating after a payment, I model it as state.

[উপরে ফিরুন](#toc)

---

### <a id="q34"></a>Q34. Google-এর recommended app architecture কী?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** তিনটা layer: **UI layer** (Composable/Activity + ViewModel), ঐচ্ছিক **Domain layer** (UseCase), আর **Data layer** (Repository + data source)। নিয়ম তিনটা। এক, **single source of truth** — প্রতিটা data-র একটাই মালিক, সাধারণত local database। দুই, **unidirectional data flow** — state নিচে নামে, event উপরে ওঠে। তিন, dependency এক দিকে — UI data-কে জানে, data UI-কে জানে না। Flutter-এর official architecture guide প্রায় হুবহু একই।

---

#### তিনটা layer

```
┌──────────── UI layer ─────────────┐
│ Composable  ──action──▶ ViewModel │
│     ▲                      │      │
│     └──── UiState ◀────────┘      │
└───────────────────│───────────────┘
                    ▼
┌──── Domain layer (ঐচ্ছিক) ────────┐
│ GetFeedUseCase, PlaceOrderUseCase │
└───────────────────│───────────────┘
                    ▼
┌──────────── Data layer ───────────┐
│ FeedRepository                    │
│   ├── FeedLocalDataSource (Room)  │  ← single source of truth
│   └── FeedRemoteDataSource (API)  │
└───────────────────────────────────┘
```

Dependency কেন এক দিকে? কারণ তখন data layer UI ছাড়াই test করা যায়, আর UI বদলালে data layer-এ হাত দিতে হয় না।

Domain layer ঐচ্ছিক কেন? এটা তখনই লাগে যখন business logic জটিল, বা একই logic কয়েকটা ViewModel ব্যবহার করে। যে UseCase শুধু repository-র একটা function forward করে, সেটা শুধু একটা বাড়তি file।

---

#### Repository-র কাজ

- UI-কে data দেয়, কিন্তু data কোথা থেকে আসে সেটা লুকায়।
- Network আর database মেলায় (cache, refresh)।
- API model (DTO) থেকে app model-এ বদলায়। DTO কখনো UI-তে যায় না। না হলে backend-এর একটা field-এর নাম বদলালে UI পর্যন্ত ভাঙে।
- Error আর thread সামলায়। মানে repository **main-safe**: main thread থেকে call করা নিরাপদ, ভারী কাজ সে নিজেই background-এ পাঠায়।

---

#### Offline-first নিয়ম

UI শুধু database **observe** করে। Network data আসলে database-এ লেখা হয়। তারপর database নিজে থেকে UI-কে নতুন data দেয় (Room Flow)। এতে offline-এও app চলে, আর data-র একটাই জায়গা থাকে ([Q41](#q41))।

মূল কথা: UI কখনো সরাসরি network result দেখায় না। দেখালে network আর database — দুইটা "সত্য" তৈরি হয়, আর তারা আলাদা হতে পারে।

---

#### Model কয়টা

- `NetworkArticle` (JSON-এর আকার) → `ArticleEntity` (database-এর আকার) → `Article` (app-এর model)।
- ছোট app-এ দুইটা যথেষ্ট হতে পারে। প্রতিটা নতুন model-এর জন্য mapper লাগে, তাই অপ্রয়োজনে বাড়াবেন না।

**Reference:** Google-এর [Now in Android](https://github.com/android/nowinandroid) app — এই architecture-এর সবচেয়ে ভালো বাস্তব উদাহরণ। Interview-এর আগে এর module structure একবার দেখুন।

**Flutter-এর সাথে মিল:** Flutter-এর official architecture guide (docs.flutter.dev/app-architecture) প্রায় একই — UI (View + ViewModel), Data (Repository + Service)। আপনি আগে থেকেই এটা জানেন, শুধু Android-এর নামগুলো বসান।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Google-এর guide-এ তিনটা layer: UI, ঐচ্ছিক domain, আর data। মূল নিয়মগুলো হলো single source of truth — সাধারণত local database — unidirectional data flow, আর dependency শুধু এক দিকে।
>
> Repository লুকিয়ে রাখে data কোথা থেকে আসে। Network model-কে app model-এ বদলায়, আর main-safe থাকে।
>
> Offline-first-এ UI শুধু database observe করে, আর network-এর result database-এ লেখা হয়। তাই app offline-এও চলে, আর data এক জায়গায় থাকে।

*English:*
> Google's guide has three layers: UI, an optional domain layer, and data. The key principles are a single source of truth — usually the local database — unidirectional data flow, and dependencies that point one way.
>
> Repositories hide where the data comes from, map network models to app models, and are main-safe.
>
> For offline-first, the UI only observes the database and network results are written into it, so the app works offline and the data lives in one place.

**সাধারণ ভুল:**
- DTO সরাসরি UI-তে পাঠানো। Backend বদলালে UI পর্যন্ত ভাঙে।
- Network result সরাসরি UI-তে দেখানো, আবার database-এও রাখা। দুইটা source of truth, দুই জায়গায় আলাদা data।
- প্রয়োজন ছাড়া model আর mapper বাড়ানো। প্রতিটা নতুন model মানে নতুন mapper আর নতুন test।

**Follow-up প্রশ্ন:** "Domain layer কখন যোগ করবেন?"

*বাংলায়:*
> যখন business logic জটিল, কয়েকটা repository মেলাতে হয়, বা একই logic কয়েকটা ViewModel ব্যবহার করে। যে UseCase শুধু repository-র একটা call forward করে, সেটা আমি বানাই না — ওটা শুধু বাড়তি layer।

*English:*
> When the business logic is complex, combines several repositories, or is reused by several ViewModels. A use case that only forwards one repository call, I don't add — it's just an extra layer.

[উপরে ফিরুন](#toc)

---

### <a id="q35"></a>Q35. ViewModel ভেতরে কীভাবে configuration change পার হয়?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** প্রতিটা Activity, Fragment আর Navigation back stack entry একটা `ViewModelStoreOwner`। তার ভেতরে একটা `ViewModelStore` আছে — একটা map, key থেকে ViewModel। Configuration change-এ Activity destroy হয়, কিন্তু system এই store-টা `NonConfigurationInstances`-এর মাধ্যমে নতুন Activity-কে দিয়ে দেয়। তাই নতুন Activity একই ViewModel পায়। Activity সত্যিই শেষ হলে (`isChangingConfigurations == false`) store clear হয়, আর `onCleared()` call হয়। Flutter-এ এই সমস্যা নেই, কারণ rotation-এ শুধু widget rebuild হয়, State object থেকে যায়।

---

#### দুইটা destroy, দুই রকম ফল

Rotation-এ Activity মরে, কিন্তু store বাঁচে। Back চাপলে দুটোই মরে। পার্থক্য বোঝা যায় `isChangingConfigurations` দিয়ে।

```
Rotation:
Old Activity.onDestroy()  ──store রাখা হলো──▶  New Activity.onCreate()
       (changing config = true)                    by viewModels() → একই instance

Back চেপে বের হওয়া:
Activity.onDestroy()  ──changing config = false──▶  store.clear() → vm.onCleared()
                                                    → viewModelScope cancel
```

`by viewModels()` আসলে store-এ খোঁজে: এই key-তে ViewModel আছে? থাকলে সেটাই দেয়, না থাকলে নতুন বানায়। তাই rotation-এর পরে একই object আসে।

---

#### Scope — ViewModel কার সাথে বাঁচে

| কীভাবে নেন | কার সাথে বাঁচে |
|---|---|
| `by viewModels()` (Activity-তে) | Activity |
| `by viewModels()` (Fragment-এ) | Fragment |
| `by activityViewModels()` | Activity — একাধিক Fragment শেয়ার করে |
| `hiltViewModel()` (Compose, NavHost-এর ভেতরে) | ওই navigation destination |
| `hiltViewModel(navController.getBackStackEntry(Graph))` | পুরো nested nav graph — checkout flow-এর মতো কয়েক screen-এ শেয়ার |

---

#### নিয়ম, কারণসহ

- **ViewModel-এ কখনো `Activity`, `Fragment`, `View` বা Compose `State` holder রাখবেন না** ([Q23](#q23))। ViewModel Activity-র চেয়ে বেশিদিন বাঁচে। তাই rotation-এর পরে সে পুরনো, মরা Activity ধরে রাখে, আর সেটা leak।
- **`Context` সাধারণত দরকার নেই।** লাগলে repository-তে `@ApplicationContext` দিন, কারণ Application context পুরো app-এর সমান বাঁচে, leak করে না। `AndroidViewModel` প্রায় কখনো লাগে না।
- **ViewModel process death-এ বাঁচে না** ([Q19](#q19))। Store memory-তে থাকে, process মরলে সেটাও যায়। তাই ছোট দরকারি state `SavedStateHandle`-এ রাখুন।
- **Runtime parameter** (যেমন `productId`) লাগলে `SavedStateHandle` থেকে নিন, অথবা Hilt-এর assisted injection ব্যবহার করুন।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> প্রতিটা Activity, Fragment আর back stack entry-র নিজের একটা `ViewModelStore` থাকে। Configuration change-এ system সেই store-টা non-configuration instance দিয়ে নতুন Activity-কে দিয়ে দেয়, তাই `by viewModels()` একই object ফেরত দেয়। Activity সত্যিই শেষ হলে store clear হয়, `onCleared` চলে, আর `viewModelScope` cancel হয়।
>
> দুইটা জিনিস আমি সবসময় মাথায় রাখি। ViewModel-এ কখনো View বা Activity রাখি না। আর ViewModel process death-এ বাঁচে না — সেজন্যই `SavedStateHandle`।

*English:*
> Every Activity, Fragment and back stack entry owns a `ViewModelStore`. On a configuration change, the system hands that store to the new Activity through non-configuration instances, so `by viewModels()` returns the same object. When the Activity really finishes, the store is cleared, `onCleared` runs and `viewModelScope` is cancelled.
>
> Two things I keep in mind: a ViewModel must never hold a View or an Activity, and it does not survive process death — that's what `SavedStateHandle` is for.

**সাধারণ ভুল:**
- ViewModel-এ Activity, View বা Activity context রাখা। Rotation-এর পরে পুরনো Activity memory-তে আটকে থাকে।
- ধরে নেওয়া যে ViewModel process death-এও বাঁচে। Background থেকে ফিরে ব্যবহারকারী খালি screen বা হারানো form দেখে।
- শুধু context-এর জন্য `AndroidViewModel` নেওয়া। Test-এ Application লাগে, আর ViewModel Android-এর সাথে বাঁধা পড়ে।

**Follow-up প্রশ্ন:** "Process death-এর পরে ViewModel-এর কী হয়?"

*বাংলায়:*
> ViewModel পুরো নতুন করে তৈরি হয়, কারণ store memory-তে ছিল, process-এর সাথে সেটাও গেছে। `SavedStateHandle`-এর data Bundle-এ save হয়, তাই সেটা ফিরে আসে। তাই আমি id বা search query-র মতো ছোট state ওখানে রাখি, আর বাকিটা repository থেকে আবার আনি।

*English:*
> The ViewModel is created from scratch, because its store lived in memory and died with the process. `SavedStateHandle` data is saved in a Bundle, so it comes back. So I keep small state like an id or a search query there, and reload the rest from the repository.

[উপরে ফিরুন](#toc)

---

### <a id="q36"></a>Q36. Dependency Injection: Hilt, Dagger, Koin

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** DI মানে class নিজে তার dependency তৈরি করে না, বাইরে থেকে পায়। এতে test-এ fake দেওয়া যায়, আর code loosely coupled হয়। **Dagger** compile time-এ পুরো dependency graph বানায় আর check করে, তাই ভুল হলে build fail করে, runtime-এ crash না। **Hilt** হলো Android-এর জন্য Dagger-এর সহজ রূপ, component আর scope আগে থেকে বানানো। **Koin** runtime-এ resolve করে — setup সহজ, কিন্তু ভুল হলে app চলার সময় ধরা পড়ে। Flutter-এ `get_it` হলো Koin-এর মতো, আর `injectable` হলো Hilt-এর মতো।

---

#### Hilt setup

```kotlin
@HiltAndroidApp
class App : Application()

@AndroidEntryPoint
class MainActivity : ComponentActivity()

// Interface → implementation
@Module
@InstallIn(SingletonComponent::class)
abstract class DataModule {
    @Binds
    abstract fun bindFeedRepository(impl: OfflineFirstFeedRepository): FeedRepository
}

// যা আপনি নিজে বানাতে পারেন না (third-party builder)
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides @Singleton
    fun okHttp(): OkHttpClient = OkHttpClient.Builder().build()

    @Provides @Singleton
    fun api(client: OkHttpClient): FeedApi = Retrofit.Builder()
        .baseUrl(BuildConfig.API_URL)
        .client(client)
        .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
        .build()
        .create(FeedApi::class.java)
}

// একই type-এর দুইটা — qualifier দিয়ে আলাদা
@Qualifier @Retention(AnnotationRetention.BINARY) annotation class IoDispatcher

@Module @InstallIn(SingletonComponent::class)
object DispatcherModule {
    @Provides @IoDispatcher fun io(): CoroutineDispatcher = Dispatchers.IO
}
```

Qualifier কেন লাগে: Hilt type দেখে dependency খোঁজে। `Dispatchers.IO` আর `Dispatchers.Default` দুটোই `CoroutineDispatcher`। Qualifier ছাড়া Hilt বুঝবে না কোনটা দিতে হবে।

---

#### `@Binds` vs `@Provides`

- `@Binds` শুধু বলে "এই interface চাইলে এই class দাও"। কোনো code generate করে না, তাই দ্রুত। Implementation-এর নিজের `@Inject constructor` থাকলে এটাই নিন।
- `@Provides` একটা function চালিয়ে object বানায়। Builder দিয়ে বানানো third-party object-এর জন্য, যেমন OkHttp বা Retrofit।

---

#### Hilt-এর component আর scope

প্রতিটা component একটা Android জিনিসের lifecycle-এর সাথে বাঁধা। Scope দিলে ওই component-এর ভেতরে একটাই instance থাকে।

| Component | Scope annotation | কতদিন বাঁচে |
|---|---|---|
| `SingletonComponent` | `@Singleton` | পুরো app |
| `ActivityRetainedComponent` | `@ActivityRetainedScoped` | Activity, config change পার হয়ে |
| `ViewModelComponent` | `@ViewModelScoped` | একটা ViewModel |
| `ActivityComponent` | `@ActivityScoped` | একটা Activity instance |
| `FragmentComponent` | `@FragmentScoped` | একটা Fragment |
| `ServiceComponent` | `@ServiceScoped` | একটা Service |

**Scope না দিলে কী হয়:** প্রতিবার inject করার সময় নতুন instance। এটাই default, আর বেশিরভাগ class-এর জন্য এটাই ঠিক। শুধু যেখানে state শেয়ার করতে হয় বা object দামি (OkHttpClient, Database), সেখানে scope দিন। সব কিছু `@Singleton` করলে object-গুলো পুরো app-এর সমান বাঁচে, memory ধরে রাখে, আর scoped object-এর জন্য Dagger-কে বাড়তি lock-এর খরচও দিতে হয়।

---

#### Hilt vs Koin vs manual

| | Hilt/Dagger | Koin | Manual (constructor + নিজের container) |
|---|---|---|---|
| Error কখন ধরা পড়ে | Compile time | Runtime (test দিয়ে verify করা যায়) | Compile time |
| Build time | বেশি (annotation processing) | কম | কম |
| শেখা | কঠিন | সহজ | সহজ |
| KMP | না (Android/JVM) | হ্যাঁ | হ্যাঁ |
| বড় team-এ | সবচেয়ে বেশি ব্যবহার | মাঝারি | ছোট app |

**Flutter-এর সাথে মিল:** `get_it` = Koin-এর মতো service locator (runtime)। `injectable` = Hilt-এর মতো codegen। Riverpod-এর `Provider` graph compile-time-safe, কিছুটা Dagger-এর চিন্তার মতো।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> DI মানে class নিজের dependency নিজে বানায় না, বাইরে থেকে পায়। এতে test করা সহজ হয়, আর code loosely coupled থাকে।
>
> আমি সাধারণত Hilt নিই। এটা Dagger-এর উপর বানানো, তাই graph compile time-এই check হয়, আর Android component আর scope তৈরি করাই থাকে। বেশিরভাগ binding আমি unscoped রাখি। শুধু দামি বা শেয়ার করা object, যেমন OkHttpClient বা database, scope করি।
>
> Koin সহজ, আর KMP-তে চলে। কিন্তু ভুল ধরা পড়ে runtime-এ। তাই Koin নিলে আমি একটা test রাখি, যেটা পুরো graph verify করে।

*English:*
> DI means a class receives its dependencies instead of creating them, which makes it testable and loosely coupled.
>
> I usually choose Hilt: it's built on Dagger, so the graph is checked at compile time, and Android components and scopes come ready-made. I keep most bindings unscoped and only scope expensive or shared objects, like the OkHttpClient or the database.
>
> Koin is simpler and works in KMP, but errors show up at runtime, so with Koin I'd add a test that verifies the graph.

**সাধারণ ভুল:**
- সব কিছু `@Singleton` করা। Object পুরো app-এর সমান বাঁচে আর memory ধরে রাখে, অথচ বেশিরভাগ class-এর শেয়ার করা state নেই।
- Koin-এ graph verify করার test না রাখা। একটা binding বাদ পড়লে সেটা ধরা পড়ে শুধু ওই screen খোলার সময়, ব্যবহারকারীর হাতে।
- নিজের class-এর জন্য `@Provides` লেখা, যেখানে `@Inject constructor` আর `@Binds` যথেষ্ট। বাড়তি code, বাড়তি generated factory।

**Follow-up প্রশ্ন:** "Hilt-এ WorkManager Worker-এ inject কীভাবে?"

*বাংলায়:*
> Worker WorkManager নিজে বানায়, তাই সাধারণ constructor injection চলে না। আমি Worker-এ `@HiltWorker` দিই আর constructor-এ `@AssistedInject`, কারণ `Context` আর `WorkerParameters` runtime-এ WorkManager দেয়। তারপর WorkManager-কে `HiltWorkerFactory` দিয়ে configure করি, যাতে সে Hilt-এর factory দিয়ে Worker বানায়।

*English:*
> WorkManager creates the Worker itself, so plain constructor injection doesn't work. I annotate the Worker with `@HiltWorker` and use an `@AssistedInject` constructor, because `Context` and `WorkerParameters` come from WorkManager at runtime. Then I configure WorkManager with `HiltWorkerFactory`, so it builds Workers through Hilt.

**Follow-up প্রশ্ন:** "Test-এ আসল module বদলাবেন কীভাবে?"

*বাংলায়:*
> আমি test source-এ একটা fake module লিখি, আর তাতে `@TestInstallIn(components = [...], replaces = [DataModule::class])` দিই। তখন সব test-এ আসল `DataModule`-এর জায়গায় fake binding বসে, production code-এ কোনো পরিবর্তন লাগে না ([Q57](#q57))।

*English:*
> I write a fake module in the test source set with `@TestInstallIn(components = [...], replaces = [DataModule::class])`. Every test then gets the fake bindings instead of the real `DataModule`, with no change to production code.

[উপরে ফিরুন](#toc)

---

### <a id="q37"></a>Q37. Modularization কেন আর কীভাবে?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** Modularization মানে app-কে কয়েকটা Gradle module-এ ভাগ করা। লাভ তিনটা: build দ্রুত হয়, feature-গুলোর মাঝে আসল সীমানা তৈরি হয়, আর প্রতিটা team নিজের module-এর মালিক হয়। খরচও আছে: setup জটিল হয়, আর অনেক ছোট module হলে Gradle-এর configuration ধাপটাই ধীর হয়ে যায়। Flutter-এ melos দিয়ে monorepo আর local package বানানো একই ধারণা।

---

#### সমস্যাটা কোথায়

সব code একটা module-এ থাকলে দুইটা ঝামেলা হয়।

প্রথমটা build time। Module ভাগ করলে যে module বদলায়নি, সেটা আবার compile হয় না। আর আলাদা module parallel-এ build হতে পারে। এক module-এ এই সুবিধা পাওয়া যায় না।

দ্বিতীয়টা সীমানা। Kotlin-এর `internal` মানে "শুধু এই module-এর ভেতরে দেখা যাবে"। সব কিছু এক module-এ থাকলে `internal` কিছুই লুকায় না। তখন যেকোনো screen যেকোনো class সরাসরি ধরে ফেলতে পারে। Module ভাগ করলে feature-এর ভেতরের জিনিস সত্যিই লুকানো যায়।

তৃতীয় একটা লাভ team-এর দিক থেকে: প্রতিটা team নিজের module-এর মালিক, তাই কে কোন code-এর দায়িত্বে, সেটা পরিষ্কার থাকে।

---

#### সাধারণ structure

```
:app                         ← সব feature জোড়া দেয়, navigation graph
:feature:home
:feature:product
:feature:checkout
:core:designsystem           ← theme, button, card
:core:ui                     ← shared composable
:core:data                   ← repository
:core:database               ← Room
:core:network                ← Retrofit
:core:model                  ← pure Kotlin model
:core:testing                ← fake, test rule
build-logic/convention       ← Gradle convention plugin
```

---

#### নিয়মগুলো, কারণসহ

- **Feature module একে অন্যকে সরাসরি depend করবে না।** করলে এক feature বদলালে অন্যটাও আবার compile হয়, আর feature-গুলো একটার সাথে আরেকটা জট পাকিয়ে যায়। Navigation হয় `:app`-এর মাধ্যমে, অথবা `:feature:x:api` module-এর মাধ্যমে। ওই `api` module-এ থাকে শুধু route আর interface।
- **api / impl ভাগ।** `:feature:checkout:api`-তে interface আর route। `:feature:checkout:impl`-এ আসল কাজ। অন্য module শুধু `api` দেখে। তাই `impl` বদলালে বাকিদের আবার compile হতে হয় না।
- **Convention plugin।** প্রতিটা module-এর `build.gradle.kts`-এ একই config (compileSdk, Compose, Hilt) copy করবেন না। `build-logic`-এ একটা plugin বানান, তারপর module-এ শুধু লিখুন `plugins { id("myapp.android.feature") }`। Config বদলাতে হলে এক জায়গায় বদলালেই হয়।
- **`api(...)` vs `implementation(...)` dependency।** `implementation` দিলে ওই dependency বাইরের module দেখতে পায় না। ফলে library বদলালে কম module আবার compile হয়, build দ্রুত থাকে। `api` দিন শুধু তখন, যখন আপনার public type-এ ওই library-র type আছে।

---

#### কখন modularize করবেন না

ছোট app, এক-দুইজন developer — তখন module ভাগ করার খরচ লাভের চেয়ে বেশি। "Proof of need" মেনে চলুন: আগে build time মাপুন, সত্যিই সমস্যা হলে তখন ভাগ করুন।

**Flutter-এর সাথে মিল:** Flutter-এ melos দিয়ে monorepo আর local package (`packages/core`, `packages/feature_x`) একই ধারণা। পার্থক্য হলো Dart package-এ `internal` নেই। সেখানে `src/` folder-এ রেখে, আর শুধু দরকারি জিনিস export করে লুকাতে হয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি তিনটা কারণে modularize করি: incremental আর parallel build দ্রুত হয়, `internal` দিয়ে আসল সীমানা তৈরি হয়, আর team-এর ownership পরিষ্কার থাকে।
>
> সাধারণত layout হয় একটা app module, কয়েকটা feature module, আর data, network, database, design system-এর মতো core module। Feature-গুলো একে অন্যকে depend করে না। বড় app-এ আমি api আর impl আলাদা করি, যাতে implementation বদলালে ব্যবহারকারী module-গুলো আবার compile না হয়। আর build config রাখি convention plugin-এ।
>
> তবে ছোট app-কে আমি প্রথম দিনেই ভাগ করি না। আগে build time মাপি, সত্যিকারের দরকার হলে তখন ভাগ করি।

*English:*
> I modularize for three reasons: faster incremental and parallel builds, real boundaries with `internal`, and clear team ownership.
>
> A typical layout is the app module, feature modules, and core modules like data, network, database and design system — and features don't depend on each other. In bigger apps I split api and impl, so changing an implementation doesn't recompile the modules that use it, and I keep build config in convention plugins.
>
> But I don't modularize a small app on day one — I measure build times and split when there's a real need.

**সাধারণ ভুল:**
- এক feature module থেকে আরেক feature module সরাসরি depend করা। এক feature বদলালে অন্যটাও আবার build হয়, আর সীমানার লাভটাই চলে যায়।
- সব জায়গায় `api(...)` দেওয়া। Dependency সব module-এ ছড়িয়ে পড়ে, তাই একটা library বদলালে অনেক module আবার compile হয়।
- ছোট app-কে প্রথম দিনেই অনেক ছোট module-এ ভাঙা। Setup জটিল হয়, আর Gradle configuration নিজেই ধীর হয়ে যায়।
- প্রতিটা `build.gradle.kts`-এ একই config copy করা। একটা বদলাতে হলে সব file-এ হাত দিতে হয়, আর কোনোটা বাদ পড়ে যায়।

**Follow-up প্রশ্ন:** "`api` আর `implementation` dependency-র পার্থক্য কী?"

*বাংলায়:*
> `implementation` দিলে dependency-টা module-এর ভেতরেই থাকে, বাইরের module সেটা দেখে না। তাই library বদলালে কম module আবার compile হয়। আমি `api` দিই শুধু তখন, যখন আমার public type-এ ওই library-র type বের হয়ে আসে।

*English:*
> With `implementation`, the dependency stays inside the module, and other modules can't see it, so fewer modules recompile when it changes. I use `api` only when my public types expose that library's types.

[উপরে ফিরুন](#toc)

---

### <a id="q38"></a>Q38. Clean Architecture আর UseCase — কখন দরকার?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Clean Architecture-এর মূল কথা দুইটা: business rule framework থেকে আলাদা থাকবে, আর dependency ভেতরের দিকে যাবে। UseCase রাখুন তখনই, যখন এতে আসল কাজ আছে — business rule, দুই বা তার বেশি repository মেলানো, অথবা অনেক ViewModel একই logic ব্যবহার করছে। যে UseCase শুধু একটা repository function call করে ফেরত দেয়, সেটা বাড়তি layer ছাড়া কিছু না।

---

#### মূল ধারণা

"Dependency ভেতরের দিকে" মানে: ভেতরের layer (business rule) বাইরের layer-কে চেনে না। UI আর data layer domain-কে চেনে, কিন্তু domain Android, Room বা Retrofit-কে চেনে না। তাই framework বদলালেও business rule-এ হাত দিতে হয় না।

সমস্যা শুরু হয় যখন এই ধারণাটাকে নিয়ম বানিয়ে ফেলা হয়: "প্রতিটা repository call-এর জন্য একটা UseCase"। তখন অনেক class তৈরি হয়, যেগুলো কিছুই করে না, শুধু call পার করে দেয়।

---

#### কোন UseCase-এর দাম আছে, কোনটার নেই

```kotlin
// দরকারি UseCase — দুই source মেলায় আর একটা rule আছে
class GetCheckoutSummaryUseCase @Inject constructor(
    private val cart: CartRepository,
    private val promo: PromoRepository,
) {
    operator fun invoke(): Flow<CheckoutSummary> =
        combine(cart.items(), promo.activePromo()) { items, promo ->
            val subtotal = items.sumOf { it.price * it.quantity }
            val discount = promo?.discountFor(subtotal) ?: Money.ZERO
            CheckoutSummary(subtotal, discount, total = subtotal - discount)
        }
}

// অদরকারি UseCase — শুধু forward করে
class GetUserUseCase @Inject constructor(private val repo: UserRepository) {
    operator fun invoke(id: String) = repo.getUser(id)      // কোনো লাভ নেই
}
```

প্রথমটা দুইটা repository মেলায় আর discount-এর rule রাখে। এই logic ViewModel-এ থাকলে দুইটা screen-এ copy হতো। দ্বিতীয়টা শুধু একটা call পার করে। ViewModel সরাসরি `UserRepository` ডাকলে ঠিক একই কাজ হয়, এক class কম লাগে।

এটা Google-এর architecture guide-এর সাথেও মেলে — সেখানে domain layer ঐচ্ছিক।

**Flutter-এর সাথে মিল:** Flutter-এ Bloc বা Riverpod project-এও একই নিয়ম খাটে। Bloc বা Notifier সরাসরি repository ডাকতে পারে। UseCase আনুন শুধু যখন logic reuse হয় বা জটিল হয়।

---

#### Domain module pure Kotlin রাখলে

Domain module-এ Android dependency না থাকলে দুইটা লাভ: JVM-এ দ্রুত unit test চলে, আর KMP দিয়ে iOS-এর সাথে শেয়ার করা যায়। কিন্তু একটা দাম আছে: অন্য module-এর class Compose-এর কাছে unstable দেখাতে পারে, তাই অকারণে recomposition হতে পারে ([Q28](#q28))।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Clean Architecture-এর মূল ধারণাটা আমার পছন্দ — business rule framework থেকে আলাদা, আর dependency ভেতরের দিকে। কিন্তু UseCase নিয়ে আমি বাস্তববাদী।
>
> আমরা domain layer রাখি, কিন্তু সব কিছুর জন্য UseCase বানাই না। UseCase আনি যখন এতে business rule আছে, কয়েকটা repository মেলাতে হয়, বা কয়েকটা ViewModel একই logic ব্যবহার করে। যে UseCase শুধু একটা repository call পার করে দেয়, সেটা কোনো লাভ ছাড়াই একটা layer বাড়ায়। তাই সেখানে ViewModel সরাসরি repository ব্যবহার করে।
>
> এটা Google-এর guide-এর সাথেও মেলে, যেখানে domain layer ঐচ্ছিক।

*English:*
> I like the core idea of Clean Architecture — business rules independent of frameworks, dependencies pointing inward — but I'm pragmatic about use cases.
>
> I add one when it holds a business rule, combines several repositories, or is reused by several ViewModels. A use case that only forwards one repository call adds a layer without value, so ViewModels can talk to repositories directly.
>
> That matches Google's guidance, where the domain layer is optional.

**সাধারণ ভুল:**
- প্রতিটা repository function-এর জন্য একটা UseCase বানানো। অনেক class হয়, কিন্তু কোনোটা কোনো কাজ করে না। Code পড়তে আর বদলাতে সময় বেশি লাগে।
- আসল business rule (যেমন discount হিসাব) ViewModel-এ রেখে দেওয়া। দ্বিতীয় screen-এ একই rule লাগলে copy হয়, আর দুই copy আলাদা হয়ে যায়।

**Follow-up প্রশ্ন:** "Domain module pure Kotlin রাখবেন কেন?"

*বাংলায়:*
> Pure Kotlin হলে test JVM-এ দ্রুত চলে, emulator লাগে না। আর KMP দিয়ে iOS-এর সাথে শেয়ার করা যায়। তবে একটা জিনিস খেয়াল রাখি: অন্য module-এর class Compose-এর কাছে unstable দেখাতে পারে, তাই সেটা আলাদা করে handle করি।

*English:*
> Pure Kotlin means fast JVM unit tests and the option to share the code with iOS through KMP. The trade-off I watch is Compose stability — classes from another module can look unstable to Compose, so I handle that explicitly.

[উপরে ফিরুন](#toc)

---

# F. Data, network, background কাজ

### <a id="q39"></a>Q39. Retrofit + OkHttp: interceptor, token refresh, error handling

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** Retrofit একটা interface থেকে typed HTTP client বানিয়ে দেয়। আসল network-এর কাজ করে নিচের OkHttp। **Interceptor** দিয়ে প্রতিটা request বা response-এ কিছু যোগ করা যায় — header, logging, retry। **Authenticator** চলে যখন server 401 দেয় — token refresh করার সঠিক জায়গা এটাই। অনেক request একসাথে 401 পেলে refresh যেন **একবারই** হয়, সেটা নিশ্চিত করতে হয়। Flutter-এ Dio-র interceptor আর `QueuedInterceptor` একই সমস্যার সমাধান।

---

#### Retrofit interface

```kotlin
interface OrderApi {
    @GET("orders")
    suspend fun orders(@Query("cursor") cursor: String?): OrderPageDto

    @POST("orders")
    suspend fun create(@Body body: CreateOrderDto): OrderDto
}
```

আপনি শুধু interface লেখেন। Retrofit এর implementation বানিয়ে দেয়, আর `suspend` function সরাসরি coroutine-এ চলে।

---

#### Interceptor — application vs network

Interceptor হলো request আর response-এর পথে বসানো একটা ধাপ। প্রতিটা interceptor request হাতে পায়, চাইলে বদলায়, তারপর `chain.proceed()` দিয়ে পরের ধাপে পাঠায়।

OkHttp-এ দুই জায়গায় interceptor বসানো যায়। পার্থক্যটা হলো কোন স্তরে বসছে:

| | `addInterceptor` (application) | `addNetworkInterceptor` (network) |
|---|---|---|
| কতবার চলে | প্রতি call-এ একবার | প্রতিটা আসল network request-এ (redirect, retry সহ) |
| Cache থেকে এলে | চলে | চলে না |
| সাধারণ ব্যবহার | Auth header, logging | Network-level header, compression দেখা |

```kotlin
class AuthHeaderInterceptor @Inject constructor(private val tokens: TokenStore) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        // token না থাকলে request যেমন আছে তেমনই পাঠাই
        val token = tokens.accessToken() ?: return chain.proceed(chain.request())
        return chain.proceed(
            chain.request().newBuilder().header("Authorization", "Bearer $token").build()
        )
    }
}
```

---

#### Token refresh — সমস্যাটা কোথায়

Access token-এর মেয়াদ শেষ হলে server 401 দেয়। একটা screen খুললে প্রায়ই একসাথে কয়েকটা request যায়। তাই পাঁচটা request একসাথে 401 পেতে পারে। সাবধান না হলে পাঁচবার refresh হবে। আর প্রথম refresh-এর পরে পুরনো refresh token প্রায়ই অচল হয়ে যায়, তাই বাকি চারটা fail করে user logout হয়ে যেতে পারে।

OkHttp-এর `Authenticator` ঠিক 401-এর সময় চলে। এটা synchronous, OkHttp-এর নিজের thread-এ চলে। তাই এখানে `synchronized` দিয়ে একবারে একটা refresh নিশ্চিত করা যায়।

```kotlin
class TokenAuthenticator @Inject constructor(
    private val tokens: TokenStore,
    private val refreshApi: RefreshApi,          // আলাদা OkHttpClient, এই authenticator ছাড়া
) : Authenticator {

    override fun authenticate(route: Route?, response: Response): Request? {
        if (response.priorResponse != null) return null    // একবার চেষ্টা করেছি, আর না

        synchronized(this) {
            val sentToken = response.request.header("Authorization")?.removePrefix("Bearer ")
            val current = tokens.accessToken()

            // অন্য request এর মধ্যেই refresh করে ফেলেছে
            val fresh = if (current != null && current != sentToken) {
                current
            } else {
                val refreshToken = tokens.refreshToken() ?: return null
                val result = refreshApi.refresh(refreshToken).execute()   // synchronous call
                val body = result.body() ?: run { tokens.clear(); return null }   // logout
                tokens.save(body.accessToken, body.refreshToken)
                body.accessToken
            }
            return response.request.newBuilder().header("Authorization", "Bearer $fresh").build()
        }
    }
}
```

`null` return করা মানে "আর চেষ্টা করো না" — তখন original 401 response-টাই caller-এর কাছে যায়।

মূল তিনটা কথা:
1. **একবারই refresh।** `synchronized` একবারে একটা thread-কে ঢুকতে দেয়। ভেতরে ঢুকে আগে দেখি, "যে token পাঠিয়েছিলাম, store-এর token কি এর মধ্যে বদলে গেছে?" বদলে গেলে অন্য কেউ refresh করে ফেলেছে, আমি শুধু নতুন token দিয়ে আবার পাঠাই।
2. **Refresh-এর জন্য আলাদা client।** একই client হলে refresh call নিজেই 401 পেলে আবার এই authenticator চলবে, আর অসীম loop হবে।
3. **Refresh fail হলে** token মুছে দিন, আর একটা session-expired event দিয়ে user-কে login-এ পাঠান।

---

#### Error map করা

UI যেন কখনো raw `IOException` বা `HttpException` না দেখে। Repository-তে এগুলোকে একটা typed error-এ বদলে নিন:

```kotlin
sealed interface DataError {
    data object NoInternet : DataError
    data object Unauthorized : DataError
    data class Server(val code: Int) : DataError
    data object Unknown : DataError
}

class DataException(val error: DataError) : Exception()

suspend fun <T> safeCall(block: suspend () -> T): Result<T> = try {
    Result.success(block())
} catch (e: CancellationException) {
    throw e          // cancellation গিলে ফেললে coroutine ঠিকমতো থামে না
} catch (e: IOException) {
    Result.failure(DataException(DataError.NoInternet))
} catch (e: HttpException) {
    Result.failure(DataException(if (e.code() == 401) DataError.Unauthorized else DataError.Server(e.code())))
}
```

`CancellationException` আগে ধরে আবার throw করা হচ্ছে। কারণ coroutine cancel হওয়ার খবরটা এই exception দিয়েই উপরে যায়। এটাকে failure বানিয়ে দিলে cancel হওয়া কাজও "error" হিসেবে UI-তে চলে আসে।

---

#### আরও যা বলার মতো

- **Timeout:** `connectTimeout`, `readTimeout`, `writeTimeout`, আর পুরো call-এর জন্য `callTimeout`।
- **পুরো app-এ একটাই `OkHttpClient`** (`@Singleton`)। প্রতিটা client-এর নিজের connection pool আর thread pool থাকে, তাই অনেক client মানে অনেক pool। আলাদা config লাগলে `client.newBuilder()` দিয়ে বানান — তাতে pool শেয়ার হয়।
- **Logging interceptor শুধু debug build-এ।** Release-এ token আর user data log-এ চলে যেতে পারে।
- **HTTP cache:** `Cache(dir, size)` দিলে OkHttp server-এর `Cache-Control` header মেনে চলে।

**Flutter-এর সাথে মিল:** Dio-র `Interceptor` আর `QueuedInterceptor` (একবারে একটা refresh) একই সমস্যার সমাধান। OkHttp-এ `synchronized` সেই queue-এর কাজটা করে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Retrofit আমাকে interface থেকে একটা typed API দেয়, আর নিচে আসল কাজ করে OkHttp। সব request-এ যা লাগে, সেগুলো আমি interceptor-এ রাখি — auth header, common header, আর logging, সেটাও শুধু debug-এ। Token refresh করি OkHttp-এর `Authenticator`-এ, কারণ এটা ঠিক তখনই চলে যখন server 401 দেয়।
>
> কঠিন জায়গাটা হলো concurrency। পাঁচটা request একসাথে fail করলে আমি পাঁচটা না, একটাই refresh চাই। তাই synchronize করি, আর আগে দেখে নিই অন্য কোনো request এর মধ্যেই নতুন token এনে ফেলেছে কি না। Refresh call-এর জন্য আলাদা client রাখি, নইলে loop হতে পারে।
>
> Repository-তে `IOException` আর `HttpException`-কে একটা typed error-এ map করি, যাতে UI কখনো raw network exception না দেখে।

*English:*
> Retrofit gives me a typed API from an interface, and OkHttp does the real work underneath. I put cross-cutting concerns in interceptors — auth headers, logging in debug only, common headers — and I handle token refresh in an OkHttp `Authenticator`, because it runs exactly when the server returns 401.
>
> The tricky part is concurrency: if five requests fail at once, I want one refresh, not five, so I synchronize and first check whether another request already got a new token. The refresh call uses a separate client, so it can't loop.
>
> In the repository I map `IOException` and `HttpException` into a typed error, so the UI never sees raw network exceptions.

**সাধারণ ভুল:**
- Refresh call একই client দিয়ে করা। Refresh নিজে 401 পেলে আবার authenticator চলে, আর loop শুরু হয়।
- `synchronized` বা "token কি আগেই বদলেছে?" check ছাড়া refresh করা। একসাথে কয়েকটা refresh হয়, আর পুরনো refresh token অচল হলে user অকারণে logout হয়।
- প্রতিটা জায়গায় নতুন `OkHttpClient` বানানো। প্রতিটার আলাদা connection pool আর thread pool, তাই memory আর connection নষ্ট হয়।
- Release build-এ logging interceptor রেখে দেওয়া। Token আর user data log-এ চলে যায়।
- `catch (e: Exception)` দিয়ে সব ধরে ফেলা। `CancellationException`-ও ধরা পড়ে, আর cancel হওয়া কাজ error হিসেবে দেখায়।

**Follow-up প্রশ্ন:** "Application interceptor আর network interceptor-এর পার্থক্য কী?"

*বাংলায়:*
> Application interceptor প্রতি call-এ একবার চলে, response cache থেকে এলেও চলে। তাই auth header আর logging আমি সেখানে রাখি। Network interceptor চলে প্রতিটা আসল network request-এ, redirect আর retry সহ, কিন্তু cache থেকে এলে চলে না। Network-level header বা compression দেখতে হলে তখন ওটা নিই।

*English:*
> An application interceptor runs once per call, even when the response comes from the cache, so I put auth headers and logging there. A network interceptor runs for every real network request, including redirects and retries, but not for cached responses — I use it for network-level headers or to look at compression.

[উপরে ফিরুন](#toc)

---

### <a id="q40"></a>Q40. Room আর DataStore

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** Room হলো SQLite-এর উপর একটা layer। এটা compile time-এ SQL query check করে, আর DAO `Flow` return করলে table বদলালেই নতুন data দেয়। Schema বদলালে **migration** লিখতে হয়। না লিখলে user-এর data হারায় বা app crash করে। **DataStore** হলো `SharedPreferences`-এর বদলি: coroutine আর Flow দিয়ে কাজ করে, main thread-এ disk IO করে না, আর update transactional। Flutter-এ Room-এর কাছাকাছি হলো drift।

---

#### Room — দুইটা বড় সুবিধা

প্রথমটা **compile-time check**। Query-তে column-এর নাম ভুল হলে app চালানোর আগে build-এই error আসে।

দ্বিতীয়টা **observable query**। DAO `Flow` return করলে Room table-টা নজরে রাখে। ওই table-এ কিছু লেখা হলেই query আবার চলে, নতুন list আসে। তাই offline-first UI সহজ হয়: UI শুধু database দেখে, network database-এ লেখে, বাকিটা Room নিজেই করে ([Q41](#q41))।

```kotlin
@Entity(tableName = "articles", indices = [Index("publishedAt")])
data class ArticleEntity(
    @PrimaryKey val id: String,
    val title: String,
    val body: String,
    val publishedAt: Long,
    val isBookmarked: Boolean = false,
)

@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY publishedAt DESC")
    fun observeAll(): Flow<List<ArticleEntity>>          // table বদলালে আবার emit

    @Upsert
    suspend fun upsertAll(items: List<ArticleEntity>)

    @Query("UPDATE articles SET isBookmarked = :value WHERE id = :id")
    suspend fun setBookmarked(id: String, value: Boolean)

    @Transaction
    suspend fun replaceAll(items: List<ArticleEntity>) {   // দুইটা কাজ একসাথে, অর্ধেক না
        deleteAll()
        upsertAll(items)
    }

    @Query("DELETE FROM articles")
    suspend fun deleteAll()
}

@Database(entities = [ArticleEntity::class], version = 2, exportSchema = true)
abstract class AppDatabase : RoomDatabase() {
    abstract fun articleDao(): ArticleDao
}
```

`@Transaction` দেওয়া `replaceAll`-এ delete আর insert একসাথে হয়। মাঝপথে কিছু fail করলে দুইটাই বাতিল হয়। তাই কখনো "পুরনো data মুছে গেছে, নতুন data আসেনি" — এমন অর্ধেক অবস্থা হয় না।

---

#### Migration — যেখানে সবচেয়ে সাবধান থাকতে হয়

User-এর phone-এ পুরনো version-এর database আছে। নতুন version-এ column যোগ করলে Room-কে বলে দিতে হয়, পুরনো database-কে কীভাবে নতুন রূপে আনবে। এটাই migration।

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE articles ADD COLUMN isBookmarked INTEGER NOT NULL DEFAULT 0")
    }
}

Room.databaseBuilder(context, AppDatabase::class.java, "app.db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

> **সতর্কতা — data loss:** `fallbackToDestructiveMigration()` দিলে migration না পেলে Room পুরো database মুছে নতুন করে বানায়। User-এর offline data, draft, bookmark সব চলে যায়। এটা শুধু তখন দিন, যখন database পুরোটা server থেকে আবার আনা যায় (pure cache)। আর ব্যবহার করলে interview-এ এই ঝুঁকিটা নিজে থেকে বলুন।

---

#### Room-এর আরও দরকারি কথা

- **`exportSchema = true`** দিলে প্রতিটা version-এর schema একটা JSON file হয়। এটা git-এ রাখুন। Auto-migration আর migration test (`MigrationTestHelper`) — দুইটাতেই এই file লাগে।
- **Main thread-এ query চলে না।** Room default-এ এটা আটকায়, crash করে। `suspend` বা `Flow` ব্যবহার করুন।
- **Relation:** `@Relation` আর `@Transaction` দিয়ে one-to-many data একবারে আনা যায়।
- **KMP:** Room এখন KMP support করে, তাই iOS-এর সাথে database code শেয়ার করা যায়।

---

#### DataStore vs SharedPreferences

`SharedPreferences`-এর মূল সমস্যা হলো এটা synchronous। প্রথম read disk থেকে হয়, আর সেটা main thread-এ হতে পারে। আর `apply()` দেখতে async হলেও Activity stop-এর সময় system অপেক্ষা করে লেখা শেষ হওয়ার জন্য — সেখান থেকে ANR আসতে পারে। DataStore এই দুইটাই সমাধান করে।

| | SharedPreferences | DataStore |
|---|---|---|
| API | Synchronous read | `Flow` আর `suspend` |
| Main thread | প্রথম read disk থেকে main-এ হতে পারে | কখনো না |
| `apply()` | Async, কিন্তু Activity stop-এর সময় অপেক্ষা করায় → ANR হতে পারে | — |
| Error | চুপচাপ ব্যর্থ হয় | Exception দেয় (`IOException`) |
| Transaction | না | `updateData {}` / `edit {}` atomic |
| Type safety | না | Proto DataStore-এ হ্যাঁ |

```kotlin
private val Context.settings by preferencesDataStore(name = "settings")   // একটাই instance

class SettingsRepository @Inject constructor(@ApplicationContext private val context: Context) {
    private val darkModeKey = booleanPreferencesKey("dark_mode")

    val darkMode: Flow<Boolean> = context.settings.data.map { it[darkModeKey] ?: false }

    suspend fun setDarkMode(enabled: Boolean) {
        context.settings.edit { it[darkModeKey] = enabled }
    }
}
```

Top-level `preferencesDataStore` delegate ব্যবহার করা হয়েছে, যাতে পুরো process-এ এই file-এর জন্য একটাই instance থাকে।

**Flutter-এর সাথে মিল:** Room ≈ drift (compile-time query, stream query, migration)। DataStore ≈ `shared_preferences`-এর async API।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Structured data-র জন্য আমি Room-কে single source of truth হিসেবে রাখি। এর সবচেয়ে বড় দুইটা সুবিধা হলো compile-time query check আর observable query। DAO `Flow` return করলে table বদলালেই নতুন data আসে, তাই offline-first UI বানানো সহজ।
>
> সবচেয়ে সাবধান থাকি migration নিয়ে। Schema export করি, migration লিখি বা auto-migration নিই, আর `MigrationTestHelper` দিয়ে test করি। কারণ একটা ভুল migration মানে user-এর data হারানো। `fallbackToDestructiveMigration()` দিই শুধু তখন, যখন database-টা pure cache।
>
> ছোট key-value setting-এর জন্য `SharedPreferences`-এর বদলে DataStore নিই, কারণ এটা async, transactional, আর main thread আটকায় না।

*English:*
> I use Room as the single source of truth for structured data. Its biggest strengths are compile-time query checks and observable queries — a DAO that returns a Flow re-emits whenever the table changes, which makes offline-first UIs simple.
>
> Migrations are where I'm most careful: I export the schema, write migrations or use auto-migrations, and test them with `MigrationTestHelper`, because a bad migration means lost user data. I only use destructive migration when the database is a pure cache.
>
> For small key-value settings I use DataStore instead of SharedPreferences, because it's async, transactional and doesn't block the main thread.

**সাধারণ ভুল:**
- একই file-এর জন্য দুইটা DataStore instance বানানো। এতে crash হয়। তাই top-level property delegate বা DI singleton দিয়ে একটাই রাখুন।
- `fallbackToDestructiveMigration()` দিয়ে migration লেখা এড়ানো। Migration না পেলে পুরো database মুছে যায় — user-এর draft, bookmark, offline data সব।
- Schema export না করা বা git-এ না রাখা। তখন auto-migration আর migration test কোনোটাই করা যায় না।

**Follow-up প্রশ্ন:** "Migration ঠিক আছে কি না, কীভাবে নিশ্চিত হন?"

*বাংলায়:*
> `exportSchema = true` দিয়ে প্রতিটা version-এর schema JSON git-এ রাখি। তারপর `MigrationTestHelper` দিয়ে পুরনো version-এর database বানিয়ে migration চালাই, আর দেখি data ঠিকমতো আছে কি না। Release-এর আগে এটা test-এ ধরা পড়লে user-এর data হারানোর ঝুঁকি থাকে না।

*English:*
> I export the schema for every version and keep the JSON in git. Then I test with `MigrationTestHelper`: create the database at the old version, run the migration, and check the data survived. Catching it in a test is much cheaper than losing user data in production.

[উপরে ফিরুন](#toc)

---

### <a id="q41"></a>Q41. Offline-first আর Paging 3

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** Offline-first মানে local database হলো আসল source। UI শুধু database দেখে। Network থেকে data এলে database-এ লেখা হয়। User-এর পরিবর্তনও আগে database-এ যায়, তারপর background-এ server-এ যায়। **Paging 3** বড় list অল্প অল্প করে load করে। `RemoteMediator` থাকলে network থেকে page এনে database-এ রাখে, আর UI page পড়ে database থেকে।

---

#### Read path — UI কখনো network-এর জন্য অপেক্ষা করে না

```kotlin
class OfflineFirstArticleRepository @Inject constructor(
    private val dao: ArticleDao,
    private val api: ArticleApi,
) : ArticleRepository {

    override fun observeArticles(): Flow<List<Article>> =
        dao.observeAll().map { list -> list.map { it.toDomain() } }

    override suspend fun refresh(): Result<Unit> = safeCall {
        val remote = api.latest()
        dao.upsertAll(remote.map { it.toEntity() })
    }
}
```

UI সাথে সাথে database-এ থাকা পুরনো data দেখায়। `refresh()` শেষ হলে Room নিজে থেকেই নতুন list দেয়, কারণ `observeAll()` একটা `Flow` ([Q40](#q40))। Refresh fail করলেও screen খালি হয় না — পুরনো data থেকে যায়।

---

#### Write path — outbox pattern

সমস্যা: user একটা comment লিখল, কিন্তু network নেই। User-কে অপেক্ষা করানো যাবে না, আবার comment হারানোও যাবে না। সমাধান হলো আগে local-এ লেখা, পরে পাঠানো:

1. User একটা comment লিখল → database-এ `syncState = PENDING` দিয়ে রাখুন। UI সাথে সাথে দেখায়।
2. `enqueueUniqueWork("sync-comments", ExistingWorkPolicy.APPEND_OR_REPLACE, ...)` দিয়ে network constraint-সহ একটা Worker চালান। এখানে `KEEP` দেবেন না। Worker চলার মাঝখানে নতুন comment এলে `KEEP` সেটাকে পরের trigger পর্যন্ত আটকে রাখবে। `APPEND_OR_REPLACE` চলতি কাজের পরে আরেকটা run যোগ করে।
3. Worker pending item-গুলো server-এ পাঠায়। সফল হলে `SYNCED` আর server id দিয়ে update করে।
4. Fail হলে `Result.retry()` → WorkManager backoff দিয়ে আবার চেষ্টা করে।
5. **Idempotency:** প্রতিটা item-এর সাথে একটা client-generated id (UUID) পাঠান। Idempotent মানে একই request দুইবার গেলেও ফল একই। তাহলে retry-তে server-এ duplicate হয় না।

---

#### Conflict resolution

কঠিন জায়গা এটাই: একই data local-এ আর server-এ দুই রকম হয়ে গেলে কোনটা টিকবে? এটা backend-এর সাথে আগে থেকে ঠিক করে নিতে হয়।

| কৌশল | কখন |
|---|---|
| Server wins | বেশিরভাগ app। সহজ |
| Last write wins (timestamp) | ছোট field (settings, status) |
| Version number (optimistic locking) | একই data একাধিক device থেকে বদলায় |
| Merge / user-কে জিজ্ঞেস | Note, document — খুব কম |

---

#### Paging 3

```kotlin
@Dao
interface ArticleDao {
    @Query("SELECT * FROM articles ORDER BY publishedAt DESC")
    fun pagingSource(): PagingSource<Int, ArticleEntity>
}

@OptIn(ExperimentalPagingApi::class)
val articles: Flow<PagingData<Article>> = Pager(
    config = PagingConfig(pageSize = 20),
    remoteMediator = ArticleRemoteMediator(api, db),
    pagingSourceFactory = { db.articleDao().pagingSource() },
).flow
    .map { paging -> paging.map { it.toDomain() } }
    .cachedIn(viewModelScope)                // rotation-এ আবার load হবে না
```

```kotlin
// Compose
val items = viewModel.articles.collectAsLazyPagingItems()
LazyColumn {
    items(count = items.itemCount, key = items.itemKey { it.id }) { index ->
        items[index]?.let { ArticleRow(it) } ?: ArticlePlaceholder()
    }
}
```

এখানে দুইটা source কাজ করে। `PagingSource` আসে Room থেকে — UI শুধু এটাই পড়ে। `RemoteMediator`-এর কাজ হলো database-এর শেষে পৌঁছালে পরের page network থেকে এনে database-এ লেখা। Database বদলালে Room নতুন `PagingSource` দেয়, আর list update হয়। পরের page-এর cursor মনে রাখতে একটা আলাদা `RemoteKeys` table লাগে।

`items[index]` null হতে পারে — তখন item এখনো load হয়নি, তাই placeholder দেখানো হয়।

এই বিষয়ের system design দিক (feed, sync) আপনার Flutter guide-এর [Section 21](../software-engineer-flutter-bn/section-21-system-design-bn.md)-এও আছে। এখানে শুধু Android-এর tool।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Offline-first-এ database হলো single source of truth। UI database দেখে, তাই read সাথে সাথে হয়, আর network শুধু database-টাকে refresh করে। Write আগে database-এ যায় একটা 'pending' flag দিয়ে। তারপর একটা WorkManager job retry-সহ সেগুলো server-এ পাঠায়। তাই user কখনো network-এর জন্য অপেক্ষা করে না। Retry-তে duplicate এড়াতে প্রতিটা item-এ client-generated id দিই।
>
> কঠিন অংশ হলো conflict। এর strategy আমি backend-এর সাথে ঠিক করি — সাধারণত version বা `updatedAt` দিয়ে server-wins, আর ছোট field-এর জন্য last-write-wins।
>
> লম্বা list-এর জন্য Paging 3 আর RemoteMediator নিই। Page আসে network থেকে, কিন্তু UI সবসময় পড়ে database থেকে।

*English:*
> For offline-first, the database is the single source of truth: the UI observes it, reads are instant, and the network only refreshes it. Writes go to the database first with a 'pending' flag, and a WorkManager job pushes them to the server with retries, so the user never waits for the network. Each item carries a client-generated id, so a retry can't create a duplicate.
>
> The hard part is conflicts — I agree with the backend on a strategy, usually server-wins with a version or `updatedAt`, or last-write-wins for simple fields.
>
> For long lists I use Paging 3 with a RemoteMediator, so pages come from the network but the UI always reads from the database.

**সাধারণ ভুল:**
- Sync worker-এ `ExistingWorkPolicy.KEEP` দেওয়া। Worker চলার সময় আসা নতুন item পরের trigger পর্যন্ত পড়ে থাকে।
- Client-generated id ছাড়া retry করা। Network মাঝপথে কাটলে server-এ একই comment দুইবার তৈরি হয়।
- UI-কে network response সরাসরি দেখানো। Network fail করলে screen খালি হয়ে যায়, offline-এ কিছুই দেখা যায় না।
- Paging flow-তে `cachedIn(viewModelScope)` না দেওয়া। Rotation-এ পুরো list আবার load হয়।

**Follow-up প্রশ্ন:** "Offset pagination না cursor pagination?"

*বাংলায়:*
> আমি cursor নিই। Offset-এ উপরে নতুন item যোগ হলে সব page এক ঘর সরে যায়। তখন কোনো item দুইবার আসে, আবার কোনোটা বাদ পড়ে। Cursor শেষ দেখা item থেকে শুরু করে, তাই এই সমস্যা হয় না।

*English:*
> Cursor. With offset, a new item at the top shifts every page, so you get duplicates or skipped items. A cursor continues from the last item you saw, so the list stays consistent.

[উপরে ফিরুন](#toc)

---

### <a id="q42"></a>Q42. Background কাজ: coroutine, WorkManager, foreground service, AlarmManager — কোনটা কখন?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** দুইটা প্রশ্ন দিয়ে ঠিক করুন। (১) User app থেকে বের হয়ে গেলেও কি কাজটা শেষ হতে হবে? (২) কাজটা কি এখনই, নাকি একটা নির্দিষ্ট সময়ে? শুধু screen থাকা পর্যন্ত লাগলে `viewModelScope`। অবশ্যই শেষ হতে হবে কিন্তু একটু দেরি চলে, তাহলে **WorkManager**। User এখন দেখছে আর লম্বা সময় চলবে (music, navigation), তাহলে **foreground service**। ঠিক নির্দিষ্ট সময়ে (alarm, calendar reminder), তাহলে **AlarmManager**।

---

#### সমস্যাটা কোথায়

Android app-এর process যেকোনো সময় মারা যেতে পারে। User app থেকে বের হলে system memory-র জন্য process বন্ধ করে দিতে পারে। আর battery বাঁচাতে Android background কাজকে সীমিত করে রাখে। তাই "background-এ একটা coroutine চালিয়ে দিই" সব কাজের জন্য চলে না। কাজের ধরন অনুযায়ী tool বাছতে হয়।

| কাজ | Tool | কেন |
|---|---|---|
| Screen-এর data load | `viewModelScope.launch` | Screen গেলে কাজের দরকার নেই |
| "Save" চাপার পরে, screen বন্ধ হলেও শেষ হোক (কয়েক সেকেন্ড) | Application scope | ছোট, কিন্তু screen-এর চেয়ে বেশি বাঁচতে হবে |
| Photo upload, data sync, log পাঠানো | **WorkManager** | Process death আর reboot-এর পরেও হয় |
| প্রতি ৬ ঘণ্টায় sync | **PeriodicWorkRequest** | সর্বনিম্ন interval ১৫ মিনিট |
| Music, workout tracking, navigation | **Foreground service** | User জানে, notification দেখায় |
| ঠিক সকাল ৭টায় alarm | **AlarmManager** `setExactAndAllowWhileIdle` | Exact time |
| Server থেকে "এখন sync করো" | **FCM** high-priority message → WorkManager | App বন্ধ থাকলেও জাগায় |

---

#### WorkManager code

```kotlin
@HiltWorker
class UploadWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted params: WorkerParameters,
    private val repo: PhotoRepository,
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        val photoId = inputData.getString(KEY_ID) ?: return Result.failure()
        return try {
            repo.upload(photoId)
            Result.success()
        } catch (e: IOException) {
            // network-এর সমস্যা — কয়েকবার আবার চেষ্টা, তারপর হাল ছাড়ো
            if (runAttemptCount < 5) Result.retry() else Result.failure()
        }
    }

    companion object { const val KEY_ID = "photo_id" }
}

fun enqueueUpload(context: Context, photoId: String) {
    val request = OneTimeWorkRequestBuilder<UploadWorker>()
        .setInputData(workDataOf(UploadWorker.KEY_ID to photoId))
        .setConstraints(
            Constraints.Builder()
                .setRequiredNetworkType(NetworkType.CONNECTED)
                .setRequiresBatteryNotLow(true)
                .build()
        )
        .setBackoffCriteria(BackoffPolicy.EXPONENTIAL, 30, TimeUnit.SECONDS)
        .build()

    WorkManager.getInstance(context)
        .enqueueUniqueWork("upload-$photoId", ExistingWorkPolicy.KEEP, request)
}
```

`@Assisted` parameter দুইটা (`context`, `params`) WorkManager নিজে দেয়। বাকিটা (`repo`) Hilt inject করে। Unique name-এ `photoId` আছে, আর policy `KEEP` — তাই একই photo দুইবার queue-তে যায় না।

---

#### WorkManager-এর দরকারি কথা

- **Unique work** — একই কাজ দুইবার queue-তে না যাওয়ার জন্য (`KEEP`, `REPLACE`, `APPEND`)।
- **Chaining** — `beginWith(compress).then(upload).then(cleanup).enqueue()`।
- **Expedited work** — `setExpedited(...)` দিয়ে জরুরি ছোট কাজ (যেমন message পাঠানো) দ্রুত চালানো যায়। কিন্তু এর quota আছে।
- **Progress দেখানো** — `setProgress()` আর `getWorkInfoByIdFlow()`।
- **ভেতরে কী আছে** — নতুন Android-এ এটা JobScheduler ব্যবহার করে। কাজের তালিকা নিজের database-এ রাখে, তাই reboot-এর পরেও কাজ মনে থাকে।
- **কখন চলবে তার নিশ্চয়তা নেই।** Doze আর standby bucket ([Q49](#q49)) এটাকে পিছিয়ে দিতে পারে। WorkManager নিশ্চিত করে কাজটা হবে, ঠিক কখন হবে সেটা না।
- **সময়সীমা:** একটা worker একবারে প্রায় ১০ মিনিট চলতে পারে। তারপর system থামিয়ে দেয় আর পরে আবার চালায়। বেশি লম্বা কাজ হলে worker-এর ভেতরে `setForeground()` দিয়ে long-running worker বানান। Android 14+-এ তখন manifest-এ WorkManager-এর `SystemForegroundService`-এ `foregroundServiceType` দিতে হয়, আর Android 15-এর `dataSync` সময়সীমাও খাটে ([Q21](#q21))।
- **Force-stop:** User Settings থেকে app force-stop করলে সব scheduled কাজ বাতিল হয়। User আবার app না খোলা পর্যন্ত কিছু চলে না।

---

#### Exact alarm-এর নিয়ম

Android 12 থেকে exact alarm-এর জন্য `SCHEDULE_EXACT_ALARM` permission লাগে। Android 14 থেকে নতুন install-এ এটা default-এ বন্ধ থাকে। শুধু alarm clock আর calendar ধরনের app `USE_EXACT_ALARM` পায়। কারণটা battery: exact alarm device-কে ঠিক ওই সময়ে জাগায়। তাই বেশিরভাগ app-এর জন্য inexact alarm বা WorkManager-ই যথেষ্ট।

**Flutter-এর সাথে মিল:** Flutter-এর `workmanager` plugin ভেতরে এই WorkManager-ই চালায়, একটা আলাদা background Flutter engine দিয়ে। তাই plugin-এর নিয়মগুলো আসলে এখান থেকেই আসে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি দুইটা প্রশ্ন দিয়ে ঠিক করি: user app থেকে বের হলেও কি কাজটা শেষ হতে হবে, আর কাজটা কি একটা নির্দিষ্ট সময়ে চলতে হবে? Screen-এর সাথে বাঁধা কাজ থাকে `viewModelScope`-এ।
>
> যে কাজ অবশ্যই হতে হবে কিন্তু অপেক্ষা করতে পারে — sync, upload, cleanup — সেটা যায় WorkManager-এ। এটা process death আর reboot-এর পরেও টিকে থাকে, আর network বা battery-র মতো constraint মানে। তবে force-stop করলে কাজ বাতিল হয়, আর Doze বা standby bucket এটাকে পিছিয়ে দিতে পারে।
>
> User জানে এমন চলমান কাজ, যেমন playback বা navigation, সেটা ঠিক type-সহ foreground service। Exact সময় লাগলে AlarmManager। Android 12 থেকে exact alarm-এ আলাদা permission লাগে, তাই product-এ সত্যিই দরকার হলেই এটা নিই।

*English:*
> I choose by two questions: must the work finish even if the user leaves the app, and does it need to run at an exact time? Screen-bound work stays in `viewModelScope`.
>
> Work that must be guaranteed but can wait — sync, uploads, cleanup — goes to WorkManager, which survives process death and reboots and respects constraints like network and battery — though a force-stop cancels it, and Doze or standby buckets can delay it.
>
> Ongoing work the user is aware of, like playback or navigation, is a foreground service with the right type. Exact timing is AlarmManager, and since Android 12 exact alarms need a special permission, so I only use them when the product truly needs it.

**সাধারণ ভুল:**
- যে কাজ screen বন্ধ হলেও শেষ হতে হবে, সেটা `viewModelScope`-এ চালানো। Screen গেলে কাজ cancel হয়, data অর্ধেক থেকে যায়।
- WorkManager থেকে exact timing আশা করা। Doze আর standby bucket কাজটা পিছিয়ে দিতে পারে।
- দরকার ছাড়া exact alarm নেওয়া। Android 12+-এ permission লাগে, Android 14+-এ নতুন install-এ সেটা default-এ বন্ধ।
- ১০ মিনিটের বেশি লম্বা কাজ সাধারণ worker-এ রাখা। System মাঝপথে থামিয়ে দেয়। এর জন্য `setForeground()` দিয়ে long-running worker লাগে।

**Follow-up প্রশ্ন:** "User force-stop করলে WorkManager-এর কাজের কী হয়?"

*বাংলায়:*
> Settings থেকে force-stop করলে সব scheduled কাজ বাতিল হয়ে যায়। User আবার app না খোলা পর্যন্ত কিছুই চলে না। তাই আমি ধরে নিই না যে কাজ "অবশ্যই" চলবে — app খোলার সময় pending কাজ আছে কি না দেখে আবার enqueue করি।

*English:*
> A force-stop from Settings cancels all scheduled work, and nothing runs until the user opens the app again. So I don't treat WorkManager as absolute — on app start I check for pending work and enqueue it again.

[উপরে ফিরুন](#toc)

---

### <a id="q43"></a>Q43. JSON serialization: kotlinx.serialization, Moshi, Gson

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** নতুন Kotlin project-এ **kotlinx.serialization** সবচেয়ে ভালো। এটা compile time-এ code বানায়, Kotlin-এর nullability আর default value মানে, আর KMP-তে চলে। **Moshi** (codegen সহ) একটা ভালো বিকল্প। **Gson** Kotlin-এর জন্য বিপজ্জনক: এটা reflection দিয়ে constructor এড়িয়ে object বানায়। তাই non-null field-এ null চলে আসতে পারে, আর default value কাজ করে না। Flutter-এ `json_serializable`-এর মতো — compile time-এ code generate হয়।

---

#### Gson-এর ফাঁদ

Kotlin-এ non-null আর default value-এর নিশ্চয়তা আসে constructor থেকে। Constructor-ই check করে field null কি না, আর default বসায়। Gson constructor call-ই করে না। সে reflection দিয়ে খালি object বানিয়ে সরাসরি field-এ value বসায়। তাই Kotlin-এর দুইটা নিশ্চয়তাই চুপচাপ ভেঙে যায়:

```kotlin
data class User(val name: String, val role: String = "member")

// JSON: {"name": null}
val user = Gson().fromJson(json, User::class.java)
println(user.role)          // null! default "member" আসেনি
println(user.name.length)   // NullPointerException — অথচ type বলছে non-null
```

সবচেয়ে খারাপ দিক: crash-টা parsing-এর সময় হয় না। হয় অনেক পরে, অন্য কোনো screen-এ, যেখানে `name` ব্যবহার হয়। তাই bug খুঁজে পাওয়া কঠিন।

---

#### kotlinx.serialization

```kotlin
@Serializable
data class UserDto(
    val name: String,
    val role: String = "member",
    @SerialName("avatar_url") val avatarUrl: String? = null,
)

val json = Json {
    ignoreUnknownKeys = true      // backend নতুন field যোগ করলে পুরনো app crash করবে না
    coerceInputValues = true      // ভুল/null value এলে default ব্যবহার
    explicitNulls = false
}
val user = json.decodeFromString<UserDto>(text)
```

`@Serializable` দেখে compiler plugin build-এর সময় serializer বানিয়ে দেয়। Reflection নেই, তাই R8-এর সাথে খুব কম config লাগে। আর এটা Kotlin-এর type নিয়ম মানে: non-null field-এ null এলে parsing-এর সময়েই পরিষ্কার error আসে।

---

#### Backward compatibility — mobile-এর আসল চিন্তা

Mobile app-এর পুরনো version বছরের পর বছর user-এর phone-এ চলে। Backend সেই সময়ে বদলাতে থাকে। তাই:
- `ignoreUnknownKeys = true` রাখুন। Backend নতুন field যোগ করলে পুরনো app ভাঙবে না।
- নতুন field-এ default value দিন। পুরনো backend response-এ field না থাকলেও parse হবে।
- Enum-এ অজানা value এলে crash না করে একটা `UNKNOWN` case-এ নিন।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> নতুন Kotlin code-এ আমি kotlinx.serialization নিই। এটা compile time-এ serializer বানায়, nullability আর default value মানে, R8-এর সাথে কম config লাগে, আর multiplatform।
>
> Kotlin-এর সাথে Gson ঝুঁকির, কারণ এটা constructor call না করেই object বানায়। ফলে non-null property null হয়ে যেতে পারে, আর default উপেক্ষা হয়। Crash-টা হয় parsing code থেকে অনেক দূরে, তাই ধরা কঠিন।
>
> যে library-ই ব্যবহার করি, unknown key ignore করতে set করি। তাতে backend নতুন field যোগ করলেও পুরনো app version ভাঙে না।

*English:*
> For new Kotlin code I use kotlinx.serialization: it generates serializers at compile time, respects nullability and default values, works with R8 with little config, and it's multiplatform.
>
> Gson is risky with Kotlin, because it creates objects without calling the constructor, so a non-null property can end up null and defaults are ignored — that leads to crashes far from the parsing code.
>
> Whatever library I use, I set it to ignore unknown keys, so the backend can add fields without breaking old app versions.

**সাধারণ ভুল:**
- Kotlin data class-এর সাথে Gson ব্যবহার করা। Non-null field null হয়ে যায়, আর crash হয় এমন জায়গায়, যেখানে কেউ খুঁজবে না।
- `ignoreUnknownKeys` বন্ধ রাখা। Backend একটা field যোগ করলেই পুরনো সব app version-এ parsing ভেঙে যায়।
- Enum-এ `UNKNOWN` case না রাখা। Backend নতুন enum value পাঠালে পুরনো app crash করে।

**Follow-up প্রশ্ন:** "Backend একটা নতুন enum value পাঠালে পুরনো app-এর কী হবে?"

*বাংলায়:*
> কিছু না করলে parsing fail করবে, আর পুরনো version crash করতে পারে। তাই আমি enum-এ একটা `UNKNOWN` case রাখি, আর অজানা value সেখানে নিই। UI-তে `UNKNOWN` এলে নিরাপদ একটা fallback দেখাই। পুরনো version বহুদিন চলে, তাই এটা শুরু থেকেই রাখি।

*English:*
> If I do nothing, parsing fails and old versions can crash. So I give the enum an `UNKNOWN` case and map unknown values to it, and the UI shows a safe fallback for it. Old versions stay in use for years, so I add this from the start.

[উপরে ফিরুন](#toc)

---

### <a id="q44"></a>Q44. Image loading আর bitmap memory

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Image নিজে load করবেন না। **Coil** (Kotlin-first, coroutine, Compose) বা **Glide** ব্যবহার করুন। এরা memory cache আর disk cache রাখে, view-এর size অনুযায়ী ছোট করে decode করে, আর list scroll-এ পুরনো request cancel করে। Bitmap-এর memory = width × height × 4 byte (ARGB_8888)। তাই 4000×3000-এর একটা ছবি decode করলে প্রায় ৪৮ MB লাগে — এটাই OOM-এর সবচেয়ে সাধারণ কারণ।

---

#### সমস্যাটা কোথায়

JPEG বা WebP file ছোট হয়, কারণ সেটা compressed। কিন্তু screen-এ দেখাতে হলে ছবিকে bitmap-এ decode করতে হয়। Bitmap-এ প্রতিটা pixel আলাদা জায়গা নেয় — ARGB_8888-এ pixel প্রতি 4 byte। তাই file size যাই হোক, memory ঠিক হয় pixel-এর সংখ্যা দিয়ে।

একটা 12-megapixel ছবি (4000×3000) bitmap হিসেবে প্রায় ৪৮ MB। অথচ 300 pixel-এর একটা thumbnail-এর জন্য এর খুব সামান্য অংশই লাগে। List-এ এমন কয়েকটা full-size ছবি decode হলেই OOM (OutOfMemoryError)।

এজন্যই library-র সবচেয়ে বড় কাজ হলো **target-এর size-এ decode করা, original size-এ না।**

---

#### Coil দিয়ে Compose-এ

```kotlin
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data(product.imageUrl)
        .crossfade(true)
        .build(),
    contentDescription = product.name,
    placeholder = painterResource(R.drawable.placeholder),
    error = painterResource(R.drawable.image_error),
    contentScale = ContentScale.Crop,
    modifier = Modifier.size(96.dp).clip(RoundedCornerShape(8.dp)),
)
```

`Modifier.size(96.dp)` থাকায় Coil জানে ঠিক কত বড় দরকার, তাই ততটুকুই decode করে। Placeholder থাকায় ছবি আসার আগেও জায়গাটা ধরা থাকে, layout লাফায় না।

---

#### Memory বাঁচানোর নিয়ম

- **Size দিন।** Size জানা থাকলে library ঠিক ততটুকুই decode করে।
- **Server-কে ছোট ছবি দিতে বলুন** (বা CDN-এর size parameter)। Thumbnail-এর জন্য full ছবি download করলে network আর memory দুইটাই নষ্ট।
- **নিজে decode করলে** `BitmapFactory.Options.inSampleSize` দিয়ে ছোট করুন, অথবা `ImageDecoder` (API 28+) ব্যবহার করুন।
- **Format:** WebP বা AVIF ছোট হয়। App-এর icon আর illustration vector drawable হিসেবে রাখুন।
- **Hardware bitmap** (API 26+) GPU memory-তে থাকে, Java heap-এ না। Coil default-এ এটা ব্যবহার করে। কিন্তু pixel পড়তে হলে (যেমন palette-এর রং বের করতে) এটা বন্ধ করতে হয়।

**Flutter-এর সাথে মিল:** Flutter-এ `Image.network`-এর `cacheWidth`/`cacheHeight` একই কাজ করে — ছোট করে decode। আর `cached_network_image` হলো disk cache।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি কখনো হাতে image decode করি না। Compose app-এ Coil নিই, পুরনো View code-এ Glide।
>
> এই library-গুলোর আসল কাজ হলো ছবিকে target-এর size-এ decode করা, original size-এ না। একটা 12-megapixel ছবি bitmap হিসেবে প্রায় ৪৮ MB, কিন্তু 300 pixel-এর thumbnail খুবই ছোট। এর সাথে এরা memory আর disk cache রাখে, আর list item scroll করে চলে গেলে request cancel করে।
>
> আমার দিক থেকে আমি image composable-কে fixed size দিই, layout লাফানো আটকাতে placeholder রাখি, আর backend-কে resized ছবি বা CDN-এর size parameter দিতে বলি।

*English:*
> I never decode images by hand; I use Coil in Compose apps, or Glide in older View code.
>
> The key thing these libraries do is decode the image at the size of the target, not the original size — a 12-megapixel photo is about 48 MB as a bitmap, but a 300-pixel thumbnail is tiny. They also keep memory and disk caches and cancel requests when a list item scrolls away.
>
> On my side, I give image composables a fixed size, use placeholders to avoid layout jumps, and ask the backend for resized images or a CDN size parameter.

**সাধারণ ভুল:**
- Image-কে কোনো size না দেওয়া। Library তখন জানে না কত ছোট করবে, তাই অনেক বড় করে decode হতে পারে।
- Thumbnail-এর জন্য full-size ছবি download করা। Network আর memory দুইটাই নষ্ট হয়, আর list-এ OOM-এর ঝুঁকি বাড়ে।
- Hardware bitmap চালু রেখে pixel পড়ার চেষ্টা করা (যেমন palette-এর রং)। Hardware bitmap GPU memory-তে থাকে, তাই pixel পড়তে হলে এটা বন্ধ করতে হয়।

**Follow-up প্রশ্ন:** "একটা bitmap কত memory নেয়, কীভাবে হিসাব করেন?"

*বাংলায়:*
> Width × height × pixel প্রতি byte। ARGB_8888-এ pixel প্রতি 4 byte, তাই 4000×3000-এর ছবি প্রায় ৪৮ MB। File-এর size এখানে কোনো ব্যাপার না — decode হওয়ার পরে pixel-এর সংখ্যাই memory ঠিক করে। এজন্যই আমি সবসময় দেখানোর size-এ decode করাই।

*English:*
> Width times height times bytes per pixel. ARGB_8888 is 4 bytes per pixel, so a 4000×3000 image is about 48 MB. The file size doesn't matter — once decoded, the pixel count decides the memory. That's why I always decode at the display size.

[উপরে ফিরুন](#toc)

---

# G. Performance আর memory

### <a id="q45"></a>Q45. Memory leak কী, কীভাবে খুঁজবেন? LeakCanary কীভাবে কাজ করে?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** Leak মানে একটা object-এর আর দরকার নেই, কিন্তু বেশিদিন বাঁচা অন্য কোনো object তাকে ধরে রেখেছে। তাই garbage collector (GC) তাকে মুছতে পারে না। Android-এ সবচেয়ে সাধারণ leak হলো destroy হওয়া Activity, Fragment-এর view, আর unregister না করা listener। **LeakCanary** debug build-এ নজর রাখে, কোন object destroy হওয়ার পরেও মুছে যায়নি। তারপর heap dump নিয়ে দেখায় কোন reference chain তাকে ধরে রেখেছে।

---

#### সমস্যাটা কোথায়

GC একটা object মোছে তখনই, যখন কোনো GC root থেকে তার কাছে আর পৌঁছানো যায় না। GC root মানে এমন জিনিস যা সবসময় বেঁচে থাকে — static field, চলমান thread, এগুলো।

Activity অনেক ভারী object। সে পুরো view tree, bitmap আর resource ধরে রাখে। Rotation-এ Activity নতুন করে তৈরি হয়। পুরনোটা কোনো static field বা singleton-এ আটকে থাকলে, প্রতিবার rotate করলে একটা পুরো screen memory-তে জমে যায়।

সব leak-এর মূল কথা একই: **বেশিদিন বাঁচা কিছু, কম দিন বাঁচা কিছুকে ধরে রেখেছে।**

---

#### LeakCanary কীভাবে কাজ করে

1. Activity `onDestroy` হলে, Fragment-এর view destroy হলে, বা ViewModel clear হলে, সেই object-কে একটা `WeakReference`-এ রাখে। `WeakReference` GC-কে আটকায় না — তাই GC-র পরেও object থাকলে বোঝা যায়, অন্য কেউ তাকে শক্ত করে ধরে আছে।
2. কয়েক সেকেন্ড অপেক্ষা করে, তারপর GC চালায়।
3. Object তখনো বেঁচে থাকলে, সেটা সম্ভাব্য leak। কয়েকটা জমলে heap dump নেয়।
4. Heap analyze করে **leak trace** দেখায়: কোন GC root থেকে কোন কোন field ধরে ধরে ওই object পর্যন্ত পৌঁছানো যায়।

```
┬───
│ GC Root: Static field
├─ com.example.ImageCache class
│    ↓ static ImageCache.context
╰→ com.example.ProfileActivity instance   ← destroy হয়ে গেছে, কিন্তু আটকে আছে
```

Trace উপর থেকে নিচে পড়ুন: root → field → আটকে থাকা object। এখানে `ImageCache`-এর static `context` field destroy হওয়া Activity ধরে আছে। সমাধান: `ImageCache`-এ `applicationContext` রাখুন। ওটা পুরো app-এর সমান সময় বাঁচে, তাই কাউকে আটকে রাখে না।

---

#### সাধারণ leak আর সমাধান

| Leak | সমাধান |
|---|---|
| Singleton/static-এ Activity context | `applicationContext` |
| Fragment-এ binding রেখে দেওয়া | `onDestroyView`-এ `_binding = null` |
| Listener / callback / receiver unregister না করা | Lifecycle-এর একই জোড়ায় register আর unregister (`onStart`/`onStop`) |
| `Handler.postDelayed` বা inner class থ্রেড | `removeCallbacksAndMessages(null)`, অথবা coroutine + lifecycle scope |
| `GlobalScope`-এ coroutine, যে View ধরে রেখেছে | Lifecycle-aware scope |
| ViewModel-এ View, Activity বা Compose `State` holder | কখনো রাখবেন না |

সমাধানগুলো দেখলে একটা pattern পাবেন: link-টা কাটতে হয় বেশিদিন বাঁচা দিকটায়। হয় ওখানে ছোট-জীবনের object রাখবেন না, নয়তো ঠিক lifecycle-এ ছেড়ে দেবেন।

---

#### Leak ছাড়া অন্য memory সমস্যা

- **OOM** বড় bitmap থেকে ([Q44](#q44))।
- **Memory churn** — লুপে বা `onDraw`-এ অনেক ছোট object তৈরি হলে GC বারবার চলে। এতে jank হয়।
- **Native memory** — NDK library, বা পুরনো Android-এ bitmap।

**Tool:** LeakCanary (debug), Android Studio **Memory Profiler** (heap dump, allocation tracking), আর production-এ Play Console আর Crashlytics-এর OOM crash।

**Flutter-এর সাথে মিল:** Flutter-এ `dispose()`-এ controller আর stream subscription বন্ধ না করলে যে leak হয়, এটা একই সমস্যা। Flutter DevTools-এর memory tab ≈ Memory Profiler।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Leak মানে এমন object, যার আর দরকার নেই, কিন্তু কোনো long-lived root থেকে এখনো পৌঁছানো যায়, তাই GC তাকে ছাড়তে পারে না। Android-এ classic case হলো singleton, static field বা unregister না করা listener destroy হওয়া Activity ধরে রাখছে। আরেকটা হলো `onDestroyView`-এর পরেও Fragment-এর binding থেকে যাওয়া।
>
> LeakCanary সেই object-গুলোর ওপর নজর রাখে, যেগুলোর চলে যাওয়ার কথা — destroy হওয়া Activity, Fragment-এর view, ViewModel। GC-র পরেও টিকে থাকলে সে heap dump নেয় আর root পর্যন্ত সবচেয়ে ছোট reference path দেখায়। Fix প্রায় সবসময় long-lived দিকে: `applicationContext` দেওয়া, বা ঠিক lifecycle callback-এ unregister করা।
>
> আমি প্রতিটা debug build-এ LeakCanary রাখি। নতুন leak report এলে সেটাকে failing test-এর মতো ধরি।

*English:*
> A leak is an object that's no longer needed but is still reachable from a long-lived root, so the GC can't free it. On Android the classic cases are a destroyed Activity held by a singleton, a static field or an unregistered listener, and a Fragment binding kept after `onDestroyView`.
>
> LeakCanary watches objects that should be gone — destroyed activities, fragment views, ViewModels. If they survive a GC, it dumps the heap and shows the shortest reference path to the root. The fix is almost always on the long-lived side: use the application context, or unregister in the matching lifecycle callback.
>
> I keep LeakCanary in every debug build, and I treat a new leak report like a failing test.

**সাধারণ ভুল:**
- Singleton বা static cache-এ Activity-র `context` পাঠানো। Activity destroy হলেও singleton তাকে ছাড়ে না, তাই পুরো screen memory-তে থেকে যায়।
- Fragment-এ `onDestroyView`-এ `_binding = null` না করা। Fragment বেঁচে থাকে, কিন্তু তার view চলে গেছে — binding পুরনো view tree ধরে রাখে।
- `GlobalScope`-এ coroutine চালিয়ে ভেতরে View ধরা। Screen চলে গেলেও coroutine চলতে থাকে, আর View-কে আটকে রাখে।

**Follow-up প্রশ্ন:** "Leak না থাকলেও memory-র কারণে jank হতে পারে?"

*বাংলায়:*
> হ্যাঁ, memory churn থেকে। লুপে বা `onDraw`-এ অনেক ছোট object বানালে GC বারবার চলে, আর তাতে frame দেরি হয়। Leak-এ memory বাড়তেই থাকে; churn-এ memory বাড়ে না, কিন্তু GC-র চাপ বাড়ে। আমি এটা Memory Profiler-এর allocation tracking দিয়ে ধরি।

*English:*
> Yes, from memory churn. Allocating lots of small objects in a loop or in `onDraw` makes the GC run again and again, and frames get late. A leak makes memory keep growing; churn doesn't, but it puts pressure on the GC. I find it with allocation tracking in the Memory Profiler.

[উপরে ফিরুন](#toc)

---

### <a id="q46"></a>Q46. Jank আর ANR কীভাবে খুঁজে বের করবেন?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** **Jank** মানে একটা frame সময়মতো তৈরি হয়নি (60 Hz-এ ১৬ ms-এর বেশি লেগেছে), তাই scroll আটকে যায়। **ANR** মানে main thread কয়েক সেকেন্ড ধরে আটকে আছে। দুটোর মূল কারণ একই: main thread-এ এমন কাজ, যেটা ওখানে থাকার কথা না। Flutter-এ jank-এর ধারণা পুরোপুরি একই, শুধু tool আলাদা।

---

#### সমস্যাটা কোথায়

Input, layout আর draw — UI-র সব কাজ main thread-এ হয়। ওখানে disk IO, network বা ভারী হিসাব চললে frame দেরি হয়। দেরি খুব লম্বা হলে সেটা ANR।

অনুমান করে ঠিক করতে গেলে সাধারণত ভুল জায়গায় সময় যায়। তাই একটা নির্দিষ্ট ক্রমে খুঁজুন:

1. **Play Console-এর Android vitals** — সমস্যা আসলেই আছে কি না, আর কোন screen বা device-এ।
2. **StrictMode** — development-এই main thread-এর IO ধরে ফেলা।
3. **Perfetto / System Trace** — frame-এর সময় আসলে কে খাচ্ছে।
4. **Macrobenchmark** — ঠিক করার আগে আর পরে মেপে প্রমাণ করা।

---

#### StrictMode — শুধু debug build-এ

StrictMode main thread-এ disk বা network কাজ হলে সেটা ধরে। নিচে `penaltyLog()` মানে logcat-এ লিখবে, app crash করবে না।

```kotlin
class App : Application() {
    override fun onCreate() {
        super.onCreate()
        if (BuildConfig.DEBUG) {
            StrictMode.setThreadPolicy(
                StrictMode.ThreadPolicy.Builder().detectDiskReads().detectDiskWrites()
                    .detectNetwork().penaltyLog().build()
            )
            StrictMode.setVmPolicy(
                StrictMode.VmPolicy.Builder().detectLeakedClosableObjects()
                    .detectActivityLeaks().penaltyLog().build()
            )
        }
    }
}
```

`ThreadPolicy` main thread-এর কাজ দেখে। `VmPolicy` পুরো process দেখে — যেমন বন্ধ না করা `Closeable` বা leak হওয়া Activity।

---

#### কোন tool কী কাজে

| Tool | কাজ |
|---|---|
| Android vitals (Play Console) | আসল user-দের ANR, crash, slow frame, slow startup |
| StrictMode | Development-এ main thread IO ধরে |
| Perfetto / Android Studio System Trace | প্রতিটা thread কী করছে, ms ধরে ধরে |
| CPU Profiler (method trace) | কোন function সময় নিচ্ছে |
| Macrobenchmark | Startup আর scroll-এর frame time মাপা (CI-তে চালানো যায়) |
| JankStats | Production-এ jank-এর তথ্য, কোন screen-এ |
| Layout Inspector | View hierarchy, Compose recomposition count |

---

#### Trace-এ কী খুঁজবেন

লম্বা frame-গুলোতে main thread আর RenderThread কী করছে, সেটা দেখুন।

- **Main thread-এ লম্বা টুকরা:** `inflate`, `measure`, `RecyclerView` bind, `Compose:recompose`।
- **Main thread "sleeping"।** মানে সে কাজ করছে না, অপেক্ষা করছে — অন্য thread-এর lock, বা binder call (অন্য process-এ call)।
- **ঘন ঘন GC।** মানে অনেক allocation হচ্ছে ([Q45](#q45)-এর memory churn)।

**ANR trace পড়া:** Play Console-এ ANR-এর সময় main thread-এর stack দেখা যায়। সেখানে প্রায়ই পাবেন `SharedPreferences`, `SQLite`, `synchronized`, অথবা কোনো SDK-এর initialization।

**Flutter-এর সাথে মিল:** Flutter DevTools-এর Performance overlay আর timeline ≈ Perfetto। পার্থক্য: Flutter-এ UI thread আর raster thread আলাদা। Native-এ main thread আর RenderThread।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি অনুমান দিয়ে না, data দিয়ে শুরু করি। Play Console-এর Android vitals আমাকে আসল ANR আর slow-frame rate দেখায়, আর কোন screen বা device-এ সমস্যা। Development-এ StrictMode আগেভাগেই main thread-এর disk আর network কাজ ধরে ফেলে।
>
> আসল কারণ খুঁজতে আমি Perfetto দিয়ে system trace নিই। লম্বা frame-গুলোতে main thread আর RenderThread কী করছে, সেটা দেখি। সাধারণত পাওয়া যায় IO, ভারী layout বা measure, lock-এর জন্য অপেক্ষা, অথবা অনেক allocation থেকে GC।
>
> তারপর fix করি, আর Macrobenchmark-এর frame timing দিয়ে প্রমাণ করি যে উন্নতি হয়েছে। Production-এ JankStats দিয়ে নজর রাখা যায়।

*English:*
> I start with data, not guesses. Android vitals in Play Console tells me the real ANR and slow-frame rates, and which screens or devices are affected. In development, StrictMode catches disk and network work on the main thread early.
>
> To find the actual cause, I record a system trace with Perfetto and look at what the main thread and RenderThread are doing in the long frames. It's usually IO, heavy layout or measure, lock contention, or GC from too many allocations.
>
> Then I fix it and prove it with Macrobenchmark's frame timing. In production I can track it with JankStats.

**সাধারণ ভুল:**
- না মেপে "optimize" করা। ভুল জায়গায় সময় যায়, আর আসল কারণ থেকে যায়।
- Main thread "sleeping" দেখে ভাবা সে free। আসলে সে lock বা binder call-এর জন্য আটকে আছে — এটাও jank আর ANR-এর কারণ।

**Follow-up প্রশ্ন:** "StrictMode কি release build-এ রাখবেন?"

*বাংলায়:*
> না, আমি শুধু `BuildConfig.DEBUG`-এ চালু করি। এর কাজ development-এই ভুল ধরা। Release-এ আসল user-দের তথ্যের জন্য আমি Android vitals আর JankStats দেখি।

*English:*
> No, I enable it only under `BuildConfig.DEBUG`. Its job is to catch mistakes during development. For real users in release, I rely on Android vitals and JankStats.

[উপরে ফিরুন](#toc)

---

### <a id="q47"></a>Q47. App startup কীভাবে দ্রুত করবেন? Baseline Profile কী?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Startup তিন রকম। **Cold**: process নেই, সব শুরু থেকে — এটাই সবচেয়ে ধীর, আর এটাই মাপা হয়। **Warm**: process আছে, কিন্তু Activity নতুন করে তৈরি হয়। **Hot**: Activity memory-তে আছে, শুধু সামনে আনা হয়। দ্রুত করার মূল উপায়: `Application.onCreate`-এ কাজ কমানো, SDK lazy initialize করা, প্রথম screen হালকা রাখা, আর **Baseline Profile** দেওয়া। Baseline Profile হলো গুরুত্বপূর্ণ code path-এর একটা তালিকা, যেটা install-এর সময়েই আগে compile (AOT) হয়ে যায়।

---

#### Cold start-এ আসলে কী হয়

1. Process তৈরি (zygote fork)।
2. `Application` object তৈরি → সব ContentProvider-এর `onCreate` → `Application.onCreate`।
3. প্রথম Activity তৈরি → `onCreate` → layout/composition → প্রথম frame।

খেয়াল করুন, ContentProvider-গুলো `Application.onCreate`-এরও আগে চলে। অনেক library নিজের ContentProvider দিয়ে নিজেকে চুপচাপ initialize করে। তাই আপনি কিছু না লিখলেও startup ধীর হতে পারে।

---

#### দুইটা metric

- **TTID** (Time To Initial Display) — প্রথম frame কখন আঁকা হলো। System নিজেই logcat-এ `Displayed` লাইনে লেখে।
- **TTFD** (Time To Full Display) — আসল content কখন এল। এটা আপনি `reportFullyDrawn()` call করে জানান (Compose-এ `ReportDrawnWhen {}`)।

দুইটাই লাগে। TTID ভালো হলেও user যদি অনেকক্ষণ খালি screen দেখে, সেটা TTFD-তে ধরা পড়ে।

---

#### কী করবেন

| সমস্যা | সমাধান |
|---|---|
| `Application.onCreate`-এ অনেক SDK | Lazy init, অথবা প্রথম frame-এর পরে। শুধু crash reporter আগে রাখুন |
| অনেক library-র নিজের ContentProvider | **App Startup** library — সব initializer একটা provider-এ |
| প্রথম screen-এ ভারী layout | Compose-এ হালকা প্রথম screen। পুরনো View-এ layout সমতল রাখা |
| Splash-এর জন্য আলাদা Activity | **SplashScreen API** (Android 12+, `core-splashscreen` দিয়ে পুরনোতেও) |
| প্রথমবার চালাতে code interpret/JIT হয় | **Baseline Profile** + **Startup Profile** |
| DI graph বড় | Hilt-এ দামি object `Lazy<T>` বা `Provider<T>` দিয়ে |

Crash reporter কেন আগে? কারণ startup-এর মধ্যেই crash হলে সেটাও ধরা দরকার।

---

#### Baseline Profile — কেন আর কীভাবে

সমস্যা: install-এর পরে প্রথম কয়েকবার চালানোর সময় ART (Android runtime) অনেক code interpret বা JIT compile করে। তাই প্রথম দিকের চালানো ধীর হয়। Baseline Profile app-এর সাথে একটা তালিকা পাঠায় — "এই class আর method-গুলো গরম, এগুলো আগে compile করে রাখো"।

Compose app-এ লাভটা বেশি। কারণ Compose একটা library, framework-এর মতো device-এ আগে থেকে compile করা থাকে না।

```kotlin
// :baselineprofile module — Macrobenchmark দিয়ে আসল user journey চালায়
@RunWith(AndroidJUnit4::class)
class BaselineProfileGenerator {
    @get:Rule val rule = BaselineProfileRule()

    @Test
    fun generate() = rule.collect(packageName = "com.example.app") {
        pressHome()
        startActivityAndWait()                       // startup
        device.findObject(By.res("feed")).fling(Direction.DOWN)   // প্রধান scroll
    }
}
```

এটা চালালে `baseline-prof.txt` তৈরি হয়। ফাইলটা app-এর সাথে যায়। Play install-এর সময় এই code আগেই compile করে ফেলে। Google-এর হিসাবে প্রথম চালানো থেকেই code execution প্রায় ৩০% দ্রুত হতে পারে। তবে interview-এ নিজের app-এ মাপা সংখ্যা বলুন।

**Flutter-এর সাথে মিল:** Flutter app-এর cold start-এ engine আর Dart VM শুরু হওয়ার খরচ যোগ হয়। Add-to-app-এ `FlutterEngine` আগে থেকে warm করে রাখার কারণ এটাই।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি আগে Macrobenchmark দিয়ে cold start মাপি। দেখি time to initial display আর time to full display — দ্বিতীয়টা আমি `reportFullyDrawn()` দিয়ে জানাই।
>
> সাধারণ লাভগুলো হলো: SDK initialization `Application.onCreate` থেকে সরানো — lazy করে, অথবা App Startup দিয়ে। প্রথম screen হালকা রাখা। আর প্রথম frame-এর আগে disk বা network না ছোঁয়া।
>
> তারপর Baseline Profile। এটা app-এর সাথে গরম class আর method-এর তালিকা পাঠায়, তাই ART install-এর সময়েই সেগুলো compile করে রাখে — প্রথম কয়েকবার interpret বা JIT করতে হয় না। Compose app-এ এটা বড় লাভ, কারণ Compose একটা library, framework-এর মতো আগে থেকে compile করা না।

*English:*
> I measure cold start first, with Macrobenchmark, looking at time to initial display and time to full display, which I report with `reportFullyDrawn()`.
>
> The usual wins are moving SDK initialization out of `Application.onCreate` — lazily, or with App Startup — keeping the first screen light, and avoiding disk or network before the first frame.
>
> Then Baseline Profiles: they ship a list of hot classes and methods with the app, so ART compiles them ahead of time at install instead of interpreting or JIT-compiling them on the first runs. For Compose apps that's a big win, because Compose is a library and isn't precompiled like the framework.

**সাধারণ ভুল:**
- Splash screen-এ `setKeepOnScreenCondition { true }` দিয়ে network data-র জন্য অপেক্ষা করানো। এতে startup ধীর **দেখায়**, কারণ user splash-এই আটকে থাকে। প্রথম screen দ্রুত দেখান, আর data-র জন্য skeleton বা placeholder ব্যবহার করুন।
- সব SDK `Application.onCreate`-এ একসাথে initialize করা। প্রতিটা SDK প্রথম frame-কে আরেকটু পিছিয়ে দেয়।

**Follow-up প্রশ্ন:** "Baseline Profile Compose app-এ কেন বেশি কাজে দেয়?"

*বাংলায়:*
> কারণ framework-এর code device-এ আগে থেকেই compile করা থাকে, কিন্তু Compose একটা library, app-এর সাথে আসে। Profile ছাড়া প্রথম কয়েকবার Compose-এর code interpret বা JIT হয়, তাই startup আর প্রথম scroll ধীর লাগে। Profile দিলে সেই অংশ install-এর সময়েই compile হয়ে যায়।

*English:*
> Because framework code is already compiled on the device, but Compose is a library that ships with the app. Without a profile, its code is interpreted or JIT-compiled on the first runs, so startup and the first scroll feel slow. With a profile, that code is compiled at install time.

[উপরে ফিরুন](#toc)

---

### <a id="q48"></a>Q48. App size কীভাবে কমাবেন?

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** সবচেয়ে বড় লাভ আসে চারটা জায়গা থেকে। (১) **App Bundle (AAB)** — Play প্রতিটা device-কে শুধু তার ABI, screen density আর ভাষার অংশ দেয়। (২) **R8** — ব্যবহার না হওয়া code মুছে দেয়, নাম ছোট করে, optimize করে। (৩) **`shrinkResources`** — ব্যবহার না হওয়া resource মুছে দেয়। (৪) বড় asset আর native library কমানো — WebP, vector, অপ্রয়োজনীয় SDK বাদ। আরও লাগলে **Play Feature Delivery** দিয়ে কম ব্যবহৃত feature পরে download করানো যায়।

---

#### আগে দেখুন কোনটা বড়

অনুমান করে কমাতে গেলে প্রায়ই ছোট জিনিসে সময় যায়। তাই আগে মাপুন।

- Android Studio → Build → **Analyze APK**। এটা dex, res, lib, assets আলাদা করে দেখায়।
- Play Console-এর **App size** report দেখায় user আসলে কত MB download করে।

---

#### Release build-এর setting

```kotlin
android {
    buildTypes {
        release {
            isMinifyEnabled = true            // R8: code shrink + obfuscate + optimize
            isShrinkResources = true          // ব্যবহার না হওয়া resource বাদ
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }
    androidResources {
        localeFilters += listOf("en", "bn")   // শুধু যে ভাষা support করেন
    }
}
```

`isShrinkResources` একা কাজ করে না, `isMinifyEnabled` লাগে। কারণ কোন resource ব্যবহার হচ্ছে, সেটা জানা যায় code দেখে — আগে R8 code ছাঁটে, তারপর বোঝা যায় কোন resource আর কেউ ছোঁয় না। R8-এর বিস্তারিত [Q51](#q51)-এ।

`localeFilters` দরকার, কারণ বড় library (যেমন AppCompat, Play Services) অনেক ভাষার string নিয়ে আসে। আপনি দুইটা ভাষা support করলে বাকিগুলো শুধু জায়গা নেয়।

---

#### Native library

`lib/` folder প্রায়ই সবচেয়ে বড়, কারণ প্রতিটা ABI-র জন্য আলাদা `.so` থাকে। AAB নিজেই ABI ভাগ করে দেয়, তাই device শুধু নিজের ABI-র `.so` পায়। Flutter app-এ `libflutter.so` আর `libapp.so` এখানেই থাকে।

---

#### Download size কেন জরুরি

বড় app-এর install conversion কমে যায়, বিশেষ করে ধীর network-এর দেশে। BD market-এর জন্য এটা একটা ভালো product পয়েন্ট — interview-এ size-কে শুধু technical না, business-এর কথা হিসেবেও বলুন।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি অনুমান না করে আগে দেখি আসলে কোনটা বড় — APK Analyzer বা Play Console-এর size report দিয়ে।
>
> সাধারণত সবচেয়ে বড় লাভ আসে App Bundle থেকে, কারণ তখন প্রতিটা device শুধু নিজের ABI, density আর ভাষার অংশ পায়। তারপর release-এ R8 আর resource shrinking চালু করা, আর বড় image-কে WebP বা vector করা।
>
> এরপর dependency। একটা ভারী SDK আমাদের সব code-এর চেয়েও বেশি জায়গা নিতে পারে, তাই নতুন library যোগ করার আগে আমি তার transitive dependency দেখি। বড় কিন্তু কম ব্যবহৃত feature থাকলে, Play Feature Delivery দিয়ে সেটা on-demand module-এ সরানো যায়।

*English:*
> I first look at what's actually big, using the APK Analyzer or Play Console's size report, instead of guessing.
>
> The usual biggest wins are publishing an App Bundle so each device only gets its own ABI, density and language splits; enabling R8 with resource shrinking in release; and converting large images to WebP or vectors.
>
> After that it's dependencies — one heavy SDK can cost more than all our code, so I check transitive dependencies before adding a library. For rarely used, large features, Play Feature Delivery can move them into on-demand modules.

**সাধারণ ভুল:**
- না মেপে কমানো শুরু করা। ছোট PNG নিয়ে সময় যায়, অথচ আসল জায়গা খায় `lib/` বা কোনো SDK।
- Transitive dependency না দেখে library যোগ করা। একটা ছোট library ভেতরে অনেক বড় জিনিস টেনে আনতে পারে।

**Follow-up প্রশ্ন:** "Flutter app-এর size কোথায় যায়?"

*বাংলায়:*
> বড় অংশটা native library-তে — `lib/` folder-এ `libflutter.so` (engine) আর `libapp.so` (compile করা Dart code)। প্রতিটা ABI-র জন্য আলাদা কপি থাকে। তাই আমি AAB দিয়ে publish করি, যাতে প্রতিটা device শুধু নিজের ABI-র `.so` পায়।

*English:*
> Most of it is native libraries — `libflutter.so` (the engine) and `libapp.so` (the compiled Dart code) in the `lib/` folder, one copy per ABI. So I publish an App Bundle, and each device only gets the `.so` files for its own ABI.

[উপরে ফিরুন](#toc)

---

### <a id="q49"></a>Q49. Battery: Doze, App Standby bucket, wake lock

**কত ঘন ঘন:** Deeper · **কঠিনতা:** Medium

**সংক্ষেপে:** Phone অনেকক্ষণ পড়ে থাকলে (screen বন্ধ, charge-এ না, নড়ছে না) **Doze** চালু হয়। তখন network বন্ধ থাকে, job আর alarm পিছিয়ে যায়, শুধু মাঝে মাঝে ছোট একটা "maintenance window" আসে। **App Standby bucket** ঠিক করে আপনার app কত ঘন ঘন background কাজ চালাতে পারবে — user app যত কম খোলে, তত কম সুযোগ। তাই background কাজ WorkManager দিয়ে করুন, যাতে system অনেক app-এর কাজ একসাথে চালাতে পারে।

---

#### সমস্যাটা কোথায়

প্রতিটা app যদি নিজের সময়ে phone জাগায়, phone কখনো ঘুমাতে পারে না। Radio আর CPU বারবার জাগলে battery দ্রুত শেষ হয়। তাই Android কাজগুলোকে জমিয়ে একসাথে চালাতে চায়। Doze আর bucket এই নিয়ম জোর করে চাপায়।

---

#### App Standby bucket

| Bucket | মানে |
|---|---|
| Active | এখন ব্যবহার হচ্ছে |
| Working set | প্রায়ই ব্যবহার হয় |
| Frequent | নিয়মিত, কিন্তু রোজ না |
| Rare | কম ব্যবহার — job আর alarm অনেক সীমিত |
| Restricted | খুব কম, বা খারাপ আচরণ — প্রায় কিছুই চলে না |

Bucket আপনি বেছে নেন না। User কত সম্প্রতি app ব্যবহার করেছে, সেটা দেখে system বসায়।

---

#### Battery-বান্ধব নিয়ম

- **Polling না।** Server থেকে push (FCM) নিন। Polling মানে কোনো খবর না থাকলেও বারবার radio জাগানো।
- **Location:** যতটুকু accuracy দরকার ততটুকু, আর batching।
- **Wake lock নিজে নেবেন না।** দরকার হলে timeout দিয়ে নিন, আর `finally`-তে ছেড়ে দিন। না ছাড়লে CPU জেগেই থাকে। WorkManager নিজেই wake lock সামলায়।
- **High-priority FCM** শুধু user-কে এখনই দেখানোর মতো message-এর জন্য। অপব্যবহার করলে system সেগুলো normal priority-তে নামিয়ে দেয়।
- **Test:** `adb shell dumpsys deviceidle force-idle` দিয়ে device-কে Doze-এ পাঠিয়ে দেখুন app কেমন আচরণ করে।

**Flutter-এর সাথে মিল:** Flutter-এ `workmanager` বা background plugin ব্যবহার করলেও নিচে এই একই Doze আর bucket-এর নিয়ম খাটে। Plugin নিয়ম এড়াতে পারে না।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Android battery বাঁচায় মূলত Doze আর App Standby bucket দিয়ে। Doze-এ network বন্ধ হয়ে যায়, আর job ও সাধারণ alarm ছোট maintenance window পর্যন্ত পিছিয়ে যায়। Bucket — active, working set, frequent, rare আর restricted — ঠিক করে app কত ঘন ঘন background কাজ চালাতে পারবে। এটা নির্ভর করে user কত সম্প্রতি app ব্যবহার করেছে তার ওপর।
>
> তাই আমি system-এর বিরুদ্ধে লড়ি না। Constraint দিয়ে WorkManager ব্যবহার করি, যাতে কাজ batch হয়। High-priority FCM শুধু সেই message-এ, যেটা user-কে এখনই দেখতে হবে। আর লম্বা wake lock এড়িয়ে চলি।
>
> Doze-এর মধ্যেও ঠিক সময়ে কিছু চালাতে হলে `setExactAndAllowWhileIdle` আছে, তবে সেটা rate-limited।

*English:*
> Android protects battery mainly with Doze and App Standby buckets. In Doze, network access is cut, and jobs and normal alarms are deferred to short maintenance windows. Buckets — active, working set, frequent, rare and restricted — limit how often an app can run background work, based on how recently the user used it.
>
> So I don't fight the system. I use WorkManager with constraints so work is batched, high-priority FCM only for messages the user must see now, and I avoid long wake locks.
>
> If something must run at an exact time even in Doze, that's `setExactAndAllowWhileIdle`, and it's rate-limited.

**সাধারণ ভুল:**
- Server-এ নতুন কিছু আছে কি না জানতে polling করা। কাজ না থাকলেও radio জাগে, battery যায়।
- Timeout ছাড়া wake lock নেওয়া, বা `finally`-তে না ছাড়া। একটা exception হলেই CPU জেগে থাকে।
- সব FCM high-priority পাঠানো। System পরে আসল জরুরি message-ও normal priority-তে নামিয়ে দেয়।

**Follow-up প্রশ্ন:** "Doze-এ থাকা অবস্থায় ঠিক সময়ে কিছু চালাতে হলে কী করবেন?"

*বাংলায়:*
> প্রথমে দেখি সত্যিই exact সময় লাগে কি না — বেশিরভাগ কাজ WorkManager-এ একটু দেরিতে চললেও চলে। সত্যিই লাগলে `setExactAndAllowWhileIdle`। কিন্তু এটা rate-limited, তাই বারবার চালানোর কাজে এর ওপর ভরসা করি না।

*English:*
> First I check if it really needs an exact time — most work is fine a little later in WorkManager. If it really does, I use `setExactAndAllowWhileIdle`. But it's rate-limited, so I don't rely on it for frequent work.

[উপরে ফিরুন](#toc)

---

# H. Build আর release

### <a id="q50"></a>Q50. Gradle build, KSP vs kapt, version catalog, build variant

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Gradle build-এর তিন ধাপ। **Initialization** — কোন কোন module আছে। **Configuration** — সব build script চালিয়ে task graph বানানো। **Execution** — দরকারি task চালানো। Build দ্রুত করার মূল tool হলো **configuration cache**, **build cache**, আর **kapt থেকে KSP**-তে যাওয়া। **Version catalog** (`libs.versions.toml`) সব dependency version এক জায়গায় রাখে। **Build type** (debug/release) × **product flavor** (dev/prod) = **build variant**। Flutter-এ `--flavor` দিয়ে যেটা চালান, সেটা নিচে এই product flavor-ই।

---

#### Build ধীর হয় কোথায়

দুইটা জায়গায় সাধারণত সময় যায়।

- **Configuration ধাপ।** প্রতিটা build-এ সব module-এর build script চলে, আপনি একটা task চালালেও। Script-এ ভারী কাজ থাকলে প্রতিবার সেই খরচ। Configuration cache এই ধাপের ফল রেখে দেয়, তাই পরের বার পুরোটা আবার চালাতে হয় না।
- **Annotation processing।** Room, Hilt-এর মতো library code generate করে। kapt এটা করে Kotlin থেকে আগে Java stub বানিয়ে, তারপর Java-র annotation processor চালিয়ে। এই বাড়তি ধাপটাই ধীর। KSP সরাসরি Kotlin code পড়ে, তাই অনেক দ্রুত।

আরেকটা জিনিস: module-এ `api` দিলে dependency-টা ওই module-এর user-দের কাছেও "ফাঁস" হয়। তখন ভেতরে কিছু বদলালে অনেক module আবার compile হয়। `implementation` দিলে পরিবর্তন module-এর ভেতরেই থাকে।

---

#### Version catalog

```toml
# gradle/libs.versions.toml
[versions]
kotlin = "2.2.0"
hilt = "2.56"

[libraries]
hilt-android = { module = "com.google.dagger:hilt-android", version.ref = "hilt" }
hilt-compiler = { module = "com.google.dagger:hilt-compiler", version.ref = "hilt" }

[plugins]
ksp = { id = "com.google.devtools.ksp", version = "2.3.0" }
```

> Version number গুলো শুধু উদাহরণ। আসল project-এ সর্বশেষ stable version দেখে বসান।

```kotlin
// app/build.gradle.kts
dependencies {
    implementation(libs.hilt.android)
    ksp(libs.hilt.compiler)
}
```

লাভ: সব module একই version পায়, আর upgrade এক জায়গায় হয়। Flutter-এর `pubspec.yaml`-এর মতো, কিন্তু অনেক module-এর জন্য একটা।

---

#### Build variant

```kotlin
android {
    buildTypes {
        debug { applicationIdSuffix = ".debug" }
        release { isMinifyEnabled = true }
    }
    flavorDimensions += "env"
    productFlavors {
        create("dev") {
            dimension = "env"
            applicationIdSuffix = ".dev"
            buildConfigField("String", "API_URL", "\"https://dev.api.example.com\"")
        }
        create("prod") {
            dimension = "env"
            buildConfigField("String", "API_URL", "\"https://api.example.com\"")
        }
    }
    buildFeatures { buildConfig = true }
}
// ফল: devDebug, devRelease, prodDebug, prodRelease
```

`applicationIdSuffix` দিলে dev আর prod একই phone-এ পাশাপাশি install করা যায়, কারণ application id আলাদা।

- **Source set:** `src/dev/`, `src/prod/`, `src/debug/` — variant অনুযায়ী আলাদা code বা resource (যেমন আলাদা `google-services.json`)।
- **`debugImplementation`** — library শুধু debug-এ (যেমন LeakCanary)।

---

#### Build দ্রুত করার checklist

- `gradle.properties`-এ `org.gradle.configuration-cache=true`, `org.gradle.caching=true`, `org.gradle.parallel=true`।
- kapt → KSP (Room, Hilt, Moshi সব KSP support করে)।
- Build script-এ configuration ধাপে network বা দামি কাজ নয়।
- `./gradlew assembleDebug --scan` দিয়ে build scan দেখে আসল সমস্যা খুঁজুন।

---

#### AGP, Gradle, Kotlin version মেলানো

Android Gradle Plugin (AGP)-এর প্রতিটা version একটা নির্দিষ্ট সর্বনিম্ন Gradle version চায়। পুরনো KSP (2.3.0-এর আগে)-এর version Kotlin version-এর সাথে মেলাতে হতো (যেমন `2.2.0-2.0.2`)। KSP 2.3.0 থেকে এর version আলাদা, আর পুরনো KSP1 deprecated। Upgrade-এর সময় সবচেয়ে বেশি build error এখান থেকেই আসে — Flutter project-এর Android build-এও একই কথা।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Gradle build-এর তিনটা ধাপ: initialization, configuration আর execution। Build ধীর হয় সাধারণত configuration-এ বেশি কাজ থাকলে, অথবা annotation processing থেকে।
>
> তাই আমার প্রথম কাজ: configuration cache আর build cache চালু করা, আর kapt থেকে KSP-তে যাওয়া। kapt-কে Java stub বানাতে হয়, KSP সরাসরি Kotlin-এ কাজ করে, তাই অনেক দ্রুত। আর module-এ `api`-এর বদলে `implementation` রাখি, যাতে একটা পরিবর্তন সব জায়গায় ছড়িয়ে না পড়ে।
>
> Version রাখি version catalog-এ, আর common config convention plugin-এ, যাতে প্রতিটা module একইভাবে build হয়। কিছু বদলানোর আগে build scan দিয়ে আসল bottleneck খুঁজি।

*English:*
> A Gradle build has three phases: initialization, configuration and execution. Slow builds usually come from configuration doing too much, or from annotation processing.
>
> So my first steps are enabling the configuration cache and build cache, moving from kapt to KSP — kapt has to generate Java stubs, KSP works on Kotlin directly and is much faster — and keeping modules on `implementation` instead of `api` so changes don't spread.
>
> I keep versions in a version catalog and shared config in convention plugins, so every module is built the same way. And I use build scans to find the real bottleneck before changing anything.

**সাধারণ ভুল:**
- Build script-এ configuration ধাপে network call বা ভারী কাজ রাখা। এটা প্রতিটা build-এ চলে, এমনকি ছোট একটা task-এও।
- সব জায়গায় `api` দেওয়া। একটা module বদলালে অনেক module আবার compile হয়।
- AGP, Gradle, Kotlin আর KSP-কে আলাদা আলাদা upgrade করা, compatibility না দেখে। তখন build error আসে, যার কারণ খুঁজতে সময় লাগে।

**Follow-up প্রশ্ন:** "kapt কেন KSP-র চেয়ে ধীর?"

*বাংলায়:*
> kapt Java-র annotation processor চালায়, যেটা Kotlin বোঝে না। তাই kapt আগে Kotlin code থেকে Java stub বানায়, তারপর processor চালায়। এই stub বানানোটাই বাড়তি খরচ। KSP সরাসরি Kotlin code পড়ে, এই ধাপ লাগে না। Room, Hilt, Moshi — সবাই এখন KSP support করে, তাই আমি নতুন project-এ kapt রাখি না।

*English:*
> kapt runs Java annotation processors, which don't understand Kotlin. So kapt first generates Java stubs from the Kotlin code, then runs the processors — that stub step is the extra cost. KSP reads Kotlin code directly and skips it. Room, Hilt and Moshi all support KSP now, so I don't keep kapt in a new project.

[উপরে ফিরুন](#toc)

---

### <a id="q51"></a>Q51. R8 / ProGuard কী? Release build-এ crash কেন হয়?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** R8 release build-এ তিনটা কাজ করে। **Shrink** — ব্যবহার না হওয়া class আর method মুছে দেয়। **Obfuscate** — নাম ছোট করে, যেমন `a.b.c`। **Optimize** — inline করা, dead code বাদ। R8 শুধু static code দেখে বোঝে কী ব্যবহার হচ্ছে। তাই যা **reflection** দিয়ে ব্যবহার হয় (Gson model, কিছু SDK, JNI), সেটা সে মুছে বা rename করে ফেলতে পারে। তখন crash হয় শুধু release build-এ। সমাধান: **keep rule** লেখা, আর crash পড়ার জন্য **mapping file** রাখা।

---

#### সমস্যাটা কোথায়

Reflection মানে runtime-এ নাম দিয়ে class বা field খোঁজা। যেমন Gson JSON-এর `"user_name"` key দেখে model-এর field-এর নাম মেলায়। R8 code পড়ে দেখে, কেউ সরাসরি এই field ছোঁয় না — তাই rename করে `a` বানিয়ে দেয়, বা মুছে দেয়। Runtime-এ Gson আর field খুঁজে পায় না।

Debug build-এ R8 চলে না, তাই সেখানে সব ঠিক দেখায়। ঠিক এই কারণেই crash শুধু release-এ আসে।

Flutter-এর `--obfuscate` flag Dart code-এর নাম লুকায়। কিন্তু Flutter app-এর Android অংশে plugin-এর Java/Kotlin code R8-এর মধ্য দিয়েই যায়, তাই এই সমস্যা Flutter-এও আসে।

---

#### Keep rule

```proguard
# proguard-rules.pro

# Reflection দিয়ে পড়া model — নাম আর field রাখো
-keep class com.example.data.remote.dto.** { *; }

# শুধু নাম রাখো, কিন্তু ব্যবহার না হলে মুছতে পারো
-keepnames class com.example.payment.PaymentCallback

# Annotation দিয়ে
# @Keep annotation দেওয়া class নিজে থেকে রাখা হয়
```

নিয়মগুলো, কারণসহ:
- **যতটা সম্ভব সংকীর্ণ।** `-keep class com.example.** { *; }` দিলে R8 প্রায় কিছুই করতে পারে না — app বড় আর ধীর হয়।
- **Library-র নিজের rule** (`consumerProguardFiles`) library-র সাথেই আসে। আপনি library module লিখলে তার rule সেখানেই দিন, যাতে যে app ব্যবহার করে তাকে আলাদা করে লিখতে না হয়।
- AGP 8 থেকে R8 **full mode** default। এটা বেশি aggressive। তাই upgrade-এর পরে নতুন release crash আসতে পারে।

সবচেয়ে ভালো উপায় হলো reflection-ই এড়ানো: kotlinx.serialization বা Moshi codegen compile time-এ code বানায়, তাই keep rule প্রায় লাগে না।

---

#### Mapping file

Obfuscate করার পরে crash-এর stack trace-এ আসল নাম থাকে না। Mapping file হলো "নতুন নাম → আসল নাম"-এর তালিকা।

- Build-এর পরে `build/outputs/mapping/release/mapping.txt` তৈরি হয়।
- Play Console-এ upload করুন (AAB-এর সাথে নিজে থেকেই যায়)। Crashlytics plugin নিজে upload করে।
- না থাকলে crash stack trace পড়া যায় না: `at a.b.c(Unknown Source)`।
- হাতে পড়তে: `retrace mapping.txt stacktrace.txt`।

প্রতিটা release-এর mapping আলাদা। তাই প্রতিটা release-এর জন্য রাখতে হয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> R8 release build-কে shrink, obfuscate আর optimize করে। কোনটা ব্যবহার হচ্ছে, সেটা সে ঠিক করে static analysis দিয়ে। তাই reflection দিয়ে যা ছোঁয়া হয় — Gson model, কিছু SDK class, JNI method — সেগুলো মুছে বা rename হয়ে যেতে পারে, আর তখন app crash করে শুধু release-এ।
>
> আমি এটা আটকাই তিনভাবে। Codegen library পছন্দ করি, যেমন kotlinx.serialization বা Moshi codegen। যেখানে reflection এড়ানো যায় না, সেখানে সংকীর্ণ keep rule দিই। আর CI-তে minified build-এর ওপর UI test চালাই।
>
> প্রতিটা release-এর mapping file আমি upload করি, যাতে Play Console বা Crashlytics-এর crash report পড়া যায়।

*English:*
> R8 shrinks, obfuscates and optimizes the release build. It decides what's used by static analysis, so anything reached through reflection — Gson models, some SDK classes, JNI methods — can be removed or renamed, and then the app crashes only in release.
>
> I prevent that by preferring codegen libraries like kotlinx.serialization or Moshi codegen, adding narrow keep rules where reflection is unavoidable, and running UI tests against a minified build in CI.
>
> I also upload the mapping file for every release, so crash reports in Play Console or Crashlytics are readable.

**সাধারণ ভুল:**
- শুধু debug build test করে release করা। Debug-এ R8 চলে না, তাই reflection-এর crash সেখানে কখনো দেখা যায় না। Release-এ একবার পুরো app চালিয়ে দেখুন, অথবা CI-তে minified build-এ test চালান।
- Crash ঠিক করতে পুরো package `-keep` করে দেওয়া। Crash যায়, কিন্তু R8-এর প্রায় সব লাভও চলে যায়।

**Follow-up প্রশ্ন:** "Release-এ crash এল, stack trace-এ শুধু `a.b.c` — কী করবেন?"

*বাংলায়:*
> ওই release-এর `mapping.txt` দিয়ে `retrace` চালাই, তাহলে আসল class আর method-এর নাম পাই। Play Console আর Crashlytics-এ mapping আগে থেকে upload থাকলে ওরা নিজেই এটা করে দেয়। তারপর দেখি কোন class reflection দিয়ে ছোঁয়া হচ্ছিল, আর শুধু সেটার জন্য সংকীর্ণ keep rule দিই।

*English:*
> I run `retrace` with that release's `mapping.txt` to get the real class and method names. If the mapping is already uploaded, Play Console and Crashlytics do this for me. Then I find which class was reached through reflection, and add a narrow keep rule just for it.

[উপরে ফিরুন](#toc)

---

### <a id="q52"></a>Q52. Signing, Play release, targetSdk policy

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** **Play App Signing**-এ দুইটা key থাকে। **App signing key** Google রাখে — user-এর device-এ যে app যায়, সেটা এটা দিয়ে sign হয়। **Upload key** আপনি রাখেন — এটা দিয়ে AAB sign করে Play-তে পাঠান। Upload key হারালে Google-কে বলে reset করা যায়। আগস্ট ২০২১ থেকে নতুন app-এর জন্য AAB আর Play App Signing বাধ্যতামূলক। শুধু তার আগের কিছু পুরনো app নিজের key রাখে — তাদের key হারালে app আর update করা যায় না। Play প্রতি বছর **targetSdk** বাড়াতে বাধ্য করে। আর Android 15+ target করা app-এ native code থাকলে **16 KB page size** support লাগে।

---

#### দুইটা key কেন

Android শুধু সেই update নেয়, যেটা আগের version-এর একই key দিয়ে sign করা। তাই signing key হারানো মানে ওই app আর কোনোদিন update না হওয়া।

Play App Signing এই ঝুঁকি দুই ভাগ করে। আসল key Google-এর কাছে নিরাপদ থাকে। আপনার হাতে থাকে শুধু upload key, যেটা হারালে বা ফাঁস হলে বদলানো যায়।

---

#### Release-এর ধাপ

1. `versionCode` বাড়ান — প্রতিটা upload-এ নতুন, আগের চেয়ে বড় একটা সংখ্যা। `versionName` হলো user যা দেখে।
2. Upload key দিয়ে signed AAB বানান। Keystore আর password **git-এ রাখবেন না** — CI secret-এ রাখুন।
3. Internal testing track-এ দিন → closed → production।
4. **Staged rollout**: ১% → ১০% → ৫০% → ১০০%। প্রতিটা ধাপে crash আর ANR দেখুন।
5. সমস্যা হলে rollout **halt** করুন, তারপর নতুন `versionCode`-এ fix পাঠান। একবার install হয়ে যাওয়া version ফেরত নেওয়া যায় না।

Staged rollout-এর কারণ ৫ নম্বরেই: যেটা device-এ চলে গেছে, সেটা আর ফেরানো যায় না। তাই ক্ষতি ছোট দলে সীমিত রাখতে হয়।

---

#### Policy যা জানা দরকার

- **targetSdk:** ৩১ আগস্ট ২০২৬ থেকে নতুন app আর update-কে **API 36** target করতে হয়। যে পুরনো app API 35-এর নিচে target করে, নতুন Android version-এর নতুন user-রা তাকে Play-তে খুঁজে পায় না। প্রতি বছর আগস্টের শেষে সীমা এক ধাপ বাড়ে। তারিখ দেখে নিন Play-র [target API page](https://developer.android.com/google/play/requirements/target-sdk)-এ।
- **targetSdk বাড়ানো শুধু একটা সংখ্যা বদলানো না।** নতুন target-এ behavior বদলায়, যেমন foreground service type বা edge-to-edge। তাই এটা আসল কাজ হিসেবে plan করুন।
- **16 KB page size:** ১ নভেম্বর ২০২৫ থেকে Android 15+ target করা নতুন app আর update-এ এটা লাগে, যদি app-এ native `.so` থাকে। NDK, পুরনো native SDK, আর Flutter-এর পুরনো version-এ এটা সমস্যা করে। সমাধান: নতুন NDK/AGP দিয়ে build করা, আর library update করা।
- **নতুন personal developer account:** production-এ যাওয়ার আগে closed testing-এ কমপক্ষে ১২ জন tester-কে ১৪ দিন একটানা রাখতে হয়।
- **Data safety form** আর **privacy policy** — app কী data নেয়, সেটা সত্যি করে লিখতে হয়।

**Signing-এর বিস্তারিত (keystore, CI, Fastlane)** আপনার Flutter guide-এর [Section 10](../software-engineer-flutter-bn/section-10-cicd-release-bn.md)-এ আছে, আর Play Console-এর ধাপ আছে [mobile/release](../../mobile/release/)-এ।

> **সতর্কতা:** পুরনো (২০২১-এর আগের) app-এ Play App Signing চালু না থাকলে আর নিজের signing key হারালে, ওই package name-এ আর কোনোদিন update দেওয়া যায় না। Play App Signing থাকলেও upload keystore-এর অন্তত দুইটা নিরাপদ backup রাখুন — reset করতে Google-এর support লাগে, তাতে কয়েক দিন release আটকে থাকে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমরা Play App Signing ব্যবহার করি — নতুন app-এর জন্য এটা এমনিতেই বাধ্যতামূলক। App signing key Google রাখে, আমরা রাখি শুধু upload key, যেটা হারালে reset করা যায়। এতে সবচেয়ে খারাপ ঝুঁকিটা চলে যায় — app আর কখনো update করতে না পারা।
>
> Release যায় track ধরে — internal, closed, open, production — staged rollout দিয়ে। Percentage বাড়ানোর আগে আমি Android vitals দেখি। কারণ খারাপ release halt করা যায়, কিন্তু যে device-এ update চলে গেছে, সেখান থেকে ফেরত নেওয়া যায় না।
>
> বছরের targetSdk bump-কে আমি আসল কাজ হিসেবে plan করি, কারণ এতে behavior বদলায়, যেমন foreground service type বা edge-to-edge। এখন নতুন app আর update-কে API 36 target করতে হয়। আর নভেম্বর ২০২৫ থেকে, native code আছে এমন app Android 15 বা তার বেশি target করলে 16 KB memory page support করতে হয়।

*English:*
> We use Play App Signing — it's mandatory for new apps anyway. Google holds the app signing key, and we keep only an upload key, which can be reset if it's lost. That removes the worst-case risk of never being able to update the app.
>
> Releases go through tracks — internal, closed, open, production — with staged rollouts. I watch Android vitals before increasing the percentage, because a bad release can be halted but not taken back from devices that already updated.
>
> I plan the yearly targetSdk bump as real work, since it brings behavior changes like foreground service types or edge-to-edge. Today new apps and updates must target API 36, and since November 2025, apps with native code that target Android 15 or higher must support 16 KB memory pages.

**সাধারণ ভুল:**
- Keystore বা তার password git-এ রাখা। Repo যার হাতে যায়, সে আপনার নামে sign করা build বানাতে পারে। CI secret-এ রাখুন।
- Upload keystore-এর backup না রাখা। Reset করা যায় ঠিকই, কিন্তু Google support লাগে, আর কয়েক দিন release আটকে থাকে।
- Staged rollout ছাড়া সরাসরি ১০০%-এ দেওয়া। খারাপ build সবার device-এ চলে যায়, আর ফেরানো যায় না।

**Follow-up প্রশ্ন:** "Upload key হারিয়ে গেলে কী হবে?"

*বাংলায়:*
> Play App Signing থাকলে app বাঁচে, কারণ আসল signing key Google-এর কাছে। আমি নতুন upload key বানিয়ে Google support-এর মাধ্যমে reset করাই। তবে তাতে কয়েক দিন release আটকে থাকে, তাই upload keystore-এর অন্তত দুইটা নিরাপদ backup রাখি। ২০২১-এর আগের কোনো app Play App Signing ছাড়া থাকলে, নিজের key হারানো মানে ওই package name-এ আর কোনোদিন update না।

*English:*
> With Play App Signing the app is safe, because Google holds the real signing key. I create a new upload key and get it reset through Google support. That blocks releases for a few days, so I keep at least two safe backups of the upload keystore. For a pre-2021 app without Play App Signing, losing its own key means no more updates on that package name, ever.

[উপরে ফিরুন](#toc)

---

### <a id="q53"></a>Q53. Runtime permission কীভাবে কাজ করে?

**কত ঘন ঘন:** Very common · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** Permission তিন রকম। **Normal** (যেমন internet) — install-এই পাওয়া যায়। **Dangerous** (camera, location, notification) — runtime-এ user-কে জিজ্ঞেস করতে হয়। **Special** (exact alarm, overlay, all files) — user-কে Settings screen-এ পাঠাতে হয়। ঠিক flow হলো: আগে check করুন, দরকার হলে কেন লাগে সেটা বুঝিয়ে বলুন (rationale), তারপর চান। User দুইবার না বললে system আর dialog দেখায় না — তখন Settings-এ পাঠানো ছাড়া পথ নেই। Flutter-এর `permission_handler` নিচে এই flow-ই চালায়।

---

#### Flow-টা কেন এমন

System dialog আপনি কতবার দেখাতে পারবেন, সেটা system ঠিক করে। User একবার না বললে আপনি একবার কারণ বুঝিয়ে আবার চাইতে পারেন। দ্বিতীয়বার না বললে system ধরে নেয় user সত্যিই চায় না, আর dialog দেখানো বন্ধ করে দেয়। তখন `launch()` call করলে কিছুই দেখা যায় না, সরাসরি "denied" আসে।

তাই কোন অবস্থায় আছেন, সেটা বোঝার চাবি হলো `shouldShowRequestPermissionRationale`:
- Deny-এর পরে এটা `true` → প্রথমবার না বলেছে। কারণ বুঝিয়ে আবার চাওয়া যায়।
- Deny-এর পরে এটা `false` → আর dialog আসবে না। Settings-এ পাঠাতে হবে।

---

#### Compose-এ পুরো flow

```kotlin
private enum class CameraDialog { Rationale, OpenSettings }

@Composable
fun CameraButton(onPermissionGranted: () -> Unit) {
    val context = LocalContext.current
    val activity = LocalActivity.current                      // androidx.activity.compose
    var dialog by remember { mutableStateOf<CameraDialog?>(null) }

    val launcher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { granted ->
        dialog = when {
            granted -> { onPermissionGranted(); null }
            // প্রথমবার না বলেছে → কেন লাগে বুঝিয়ে আবার চাওয়া যায়
            activity != null && ActivityCompat.shouldShowRequestPermissionRationale(
                activity, Manifest.permission.CAMERA,
            ) -> CameraDialog.Rationale
            // আবার না বলেছে → system আর dialog দেখাবে না, Settings ছাড়া পথ নেই
            else -> CameraDialog.OpenSettings
        }
    }

    Button(onClick = {
        val granted = ContextCompat.checkSelfPermission(context, Manifest.permission.CAMERA) ==
            PackageManager.PERMISSION_GRANTED
        if (granted) onPermissionGranted() else launcher.launch(Manifest.permission.CAMERA)
    }) { Text("ছবি তুলুন") }

    when (dialog) {
        CameraDialog.Rationale -> RationaleDialog(
            text = "Profile-এর ছবি তুলতে camera লাগবে।",
            onConfirm = { dialog = null; launcher.launch(Manifest.permission.CAMERA) },
            onDismiss = { dialog = null },
        )
        CameraDialog.OpenSettings -> OpenSettingsDialog(
            onOpenSettings = { dialog = null; context.openAppSettings() },
            onDismiss = { dialog = null },
        )
        null -> Unit
    }
}
```

পড়ার সময় খেয়াল করুন:
- Button চাপলে আগে `checkSelfPermission`। Permission আগেই থাকলে কোনো dialog ছাড়াই কাজ শুরু।
- Result আসার পরেই `shouldShowRequestPermissionRationale` দেখা হচ্ছে — উপরে যে কারণ বললাম, deny-এর পরেই এর মান অর্থ বহন করে।
- `RationaleDialog`, `OpenSettingsDialog` আর `context.openAppSettings()` এই app-এর নিজের helper, framework-এর API না।

---

#### Version ধরে বড় পরিবর্তন

| Version | পরিবর্তন |
|---|---|
| Android 6 (API 23) | Runtime permission শুরু |
| Android 10 | Background location আলাদা permission |
| Android 11 | One-time permission ("শুধু এবার"), ব্যবহার না করলে auto-reset। Background location আলাদা ধাপে, Settings দিয়ে |
| Android 12 | Approximate vs precise location। Bluetooth-এর নতুন permission |
| Android 13 | `POST_NOTIFICATIONS` runtime permission। Media আলাদা: `READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`, `READ_MEDIA_AUDIO` |
| Android 14 | Partial photo access — user কয়েকটা ছবি বেছে দিতে পারে (`READ_MEDIA_VISUAL_USER_SELECTED`) |

---

#### ভালো নিয়ম

- **Photo Picker** (`PickVisualMedia`) ব্যবহার করলে কোনো storage permission লাগে না। Play এখন বেশিরভাগ app-এর জন্য ব্যাপক photo/video permission নিষেধ করছে।
- শুধু একটা ছবি তুলতে `ACTION_IMAGE_CAPTURE` intent দিলে camera permission লাগে না — যদি manifest-এ camera permission declare না করেন। (Declare করলে তখন এই intent-এর জন্যও permission লাগে।)
- **Location:** আগে foreground, পরে আলাদা করে background। Background চাইবেন শুধু তখনই, যখন feature-এর সত্যিই দরকার। Play review-এ এটার জন্য কারণ দেখাতে হয়।

---

#### Flutter-এর সাথে মিল

`permission_handler` plugin ভেতরে এই একই flow চালায়। কিন্তু Android-এ "permanently denied" বলে সরাসরি কোনো API নেই। তাই `isPermanentlyDenied` আসলে অনুমান: "denied + rationale দেখানো যাবে না"। এটা সবসময় ঠিক না-ও হতে পারে। Native জানা থাকলে এটা ভালো একটা senior পয়েন্ট।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি permission চাই ঠিক তখন, যখন user feature-টা ব্যবহার করতে যায় — startup-এ সব একসাথে কখনো না।
>
> Flow হলো: আগে check করি। `shouldShowRequestPermissionRationale` বললে কারণ বুঝিয়ে দিই। তারপর Activity Result API দিয়ে চাই। User দুইবার না বললে system আর dialog দেখায় না, তাই তখন Settings-এ যাওয়ার পথ দিই, আর permission ছাড়াও app যেন ব্যবহারযোগ্য থাকে, সেটা দেখি।
>
> যেখানে platform-এর ভালো বিকল্প আছে, সেখানে permission-ই নিই না — Photo Picker-এ কোনো storage permission লাগে না। আর প্রতিটা release-এ নতুন নিয়ম দেখি: Android 13-এ notification runtime permission হয়েছে, আর 14-এ media access partial হয়েছে।

*English:*
> I ask for a permission only at the moment the user needs the feature, never all at once at startup.
>
> The flow is: check, show a rationale if `shouldShowRequestPermissionRationale` says so, and request with the Activity Result API. If the user denies twice, the system stops showing the dialog, so I offer a path to Settings and keep the app usable without it.
>
> I also avoid permissions where the platform has a better option — the Photo Picker needs no storage permission at all. And every release I check the new rules: notifications became a runtime permission in Android 13, and media access became partial in 14.

**সাধারণ ভুল:**
- App খোলার সাথে সাথে সব permission একসাথে চাওয়া। User কারণ বোঝে না, তাই না বলে — আর দুইবার না বললে আর চাওয়ারও সুযোগ থাকে না।
- Permanently denied অবস্থায় বারবার `launch()` call করা। Dialog আসে না, button চাপলে কিছুই হয় না, user ভাবে app ভাঙা।
- শুধু ছবি বাছতে storage বা media permission চাওয়া, যেখানে Photo Picker কোনো permission ছাড়াই কাজ করে। Play review-এও এটা সমস্যা করে।

**Follow-up প্রশ্ন:** "`permission_handler`-এর `isPermanentlyDenied`-এ কি পুরো ভরসা করা যায়?"

*বাংলায়:*
> পুরোপুরি না। Android-এ "permanently denied" জানার সরাসরি API নেই। Plugin অনুমান করে — permission denied, আর `shouldShowRequestPermissionRationale` false। কিন্তু একবারও না চাওয়া permission-এও rationale false থাকে। তাই আমি request-এর result আসার পরেই এই check করি, আগে না।

*English:*
> Not fully. Android has no direct API for "permanently denied". The plugin infers it — the permission is denied and `shouldShowRequestPermissionRationale` is false. But rationale is also false for a permission that was never requested. So I only trust that check right after a request result, not before.

[উপরে ফিরুন](#toc)

---

# I. Security

> সাধারণ mobile security (OWASP, token, JWT, OAuth PKCE, MITM) আপনার Flutter guide-এর [Section 20](../software-engineer-flutter-bn/section-20-mobile-security-bn.md)-এ আছে। এখানে শুধু Android platform-এর দিক।

### <a id="q54"></a>Q54. Android-এ data আর network কীভাবে নিরাপদ রাখবেন?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** দুইটা আলাদা জায়গা নিয়ে কথা। Device-এ পড়ে থাকা data (data at rest) আর network-এ যাওয়া data (transport)। Device-এর জন্য গোপন key রাখুন **Android Keystore**-এ, আর token-এর মতো data সেই key দিয়ে encrypt করুন। Network-এর জন্য শুধু HTTPS, নিয়ম লিখুন Network Security Config-এ, আর certificate pinning করুন শুধু ঝুঁকি বুঝে। আর একটা কথা মাথায় রাখুন: APK-এর ভেতরে যা আছে, তা আসলে public।

---

#### সমস্যাটা কোথায়

Phone-টা user-এর হাতে, আপনার হাতে না। Device rooted হতে পারে। App-এর data cloud backup হয়ে অন্য phone-এ যেতে পারে। আর APK যে কেউ নামিয়ে খুলে দেখতে পারে। তাই প্রশ্নটা হলো: এই অবস্থায় কোন জিনিস সত্যিই গোপন রাখা যায়, আর কোনটা যায় না।

---

#### Keystore — key থাকে, কিন্তু বের করা যায় না

Keystore-এ key তৈরি হলে সেটা hardware-এর ভেতরে থাকে। App key দিয়ে encrypt বা decrypt করতে পারে, কিন্তু key-টা নিজে বের করে আনতে পারে না। তাই কেউ app-এর file কপি করে নিলেও key সাথে যায় না।

```kotlin
val keyGenerator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, "AndroidKeyStore")
keyGenerator.init(
    KeyGenParameterSpec.Builder("token_key", KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)   // GCM-এ padding লাগে না
        .setKeySize(256)
        .build()
)
keyGenerator.generateKey()
```

আরও তিনটা জিনিস জানা দরকার:
- **StrongBox** (কিছু device-এ আছে)। Key থাকে আলাদা একটা secure chip-এ।
- **Biometric দিয়ে বাঁধা key।** `setUserAuthenticationRequired(true)` দিলে fingerprint ছাড়া key ব্যবহারই করা যায় না। এটা `BiometricPrompt` + `CryptoObject` দিয়ে ব্যবহার করুন। শুধু "fingerprint সফল হলো" একটা boolean-এর উপর ভরসা করবেন না। Rooted device-এ ওই boolean বদলে দেওয়া যায়। কিন্তু key নিজেই যখন fingerprint ছাড়া খোলে না, তখন বদলানোর কিছু থাকে না।
- **`androidx.security:security-crypto`** (`EncryptedSharedPreferences`) Google deprecated করেছে। নতুন code-এ Keystore key + Tink দিয়ে নিজে encrypt করুন, আর DataStore-এ রাখুন। পুরনো code-এ এটা দেখলে migration-এর কথা বলুন।

**Flutter-এর সাথে মিল:** Flutter-এ `flutter_secure_storage` এই কাজটাই করে। Android-এ ভেতরে Keystore-এর key দিয়েই encrypt করে।

---

#### Backup থেকে গোপন data বাদ দিন

এখানে একটা ফাঁদ আছে। Keystore key backup হয় না। কিন্তু encrypted file backup হয়ে যায়। নতুন phone-এ restore হলে file আসে, key আসে না। তখন decrypt করা যায় না, আর app crash করে। তাই encrypted data backup থেকে বাদ দিন।

```xml
<!-- res/xml/data_extraction_rules.xml (Android 12+) -->
<data-extraction-rules>
    <cloud-backup>
        <exclude domain="sharedpref" path="secure_prefs.xml" />
        <exclude domain="file" path="datastore/tokens.preferences_pb" />
    </cloud-backup>
    <device-transfer>
        <exclude domain="file" path="datastore/tokens.preferences_pb" />
    </device-transfer>
</data-extraction-rules>
```

---

#### Network — শুধু HTTPS, নিয়ম এক জায়গায়

Android 9 থেকে cleartext (plain HTTP) default-এ বন্ধ। Network Security Config দিয়ে এটা পরিষ্কার করে লিখে রাখুন। Debug build-এ proxy tool চালাতে user certificate বিশ্বাস করতে হয়, সেটা `debug-overrides`-এ রাখুন, যাতে release-এ না যায়।

```xml
<!-- res/xml/network_security_config.xml -->
<network-security-config>
    <base-config cleartextTrafficPermitted="false" />
    <debug-overrides>
        <trust-anchors>
            <certificates src="user" />   <!-- শুধু debug-এ Charles/Proxyman চলবে -->
        </trust-anchors>
    </debug-overrides>
</network-security-config>
```

---

#### Certificate pinning — কাজের, কিন্তু ঝুঁকি আছে

Pinning মানে app বলে দেয়, "এই server-এর শুধু এই key-টাই আমি মানব।" এতে কেউ মাঝখানে নকল certificate বসাতে পারে না। সমস্যা হলো উল্টো দিকে।

```kotlin
val pinner = CertificatePinner.Builder()
    .add("api.example.com", "sha256/PRIMARY_KEY_HASH=")
    .add("api.example.com", "sha256/BACKUP_KEY_HASH=")    // backup pin বাধ্যতামূলক
    .build()
```

> **সতর্কতা:** Server-এর certificate বদলালে আর app-এ নতুন pin না থাকলে, পুরনো সব app-এর network একসাথে বন্ধ হয়ে যায়। User update না করা পর্যন্ত app কাজ করে না। তাই সবসময় backup pin রাখুন, leaf certificate না বরং intermediate বা public key pin করুন, আর backend team-এর সাথে rotation plan করুন।

---

#### আরও যা বলার মতো

- **Release build-এ log বন্ধ।** Logcat-এ token বা user data লিখবেন না।
- **`FLAG_SECURE`।** Banking বা OTP screen-এ screenshot আর recent-apps preview বন্ধ করে।
- **Play Integrity API।** Server বুঝতে পারে request আসল app আর আসল device থেকে আসছে কি না। SafetyNet বন্ধ হয়ে গেছে। Verdict সবসময় **server-এ** check করুন, app-এ না। App-এর ভেতরের check তো attacker বদলে দিতে পারে।
- **Root detection** শুধু একটা বাধা, সমাধান না। দক্ষ attacker এটা পার হয়ে যায়।
- **Obfuscation (R8) security না।** এটা শুধু code পড়া কঠিন করে।
- **APK-এর ভেতরের secret আসলে secret না।** API key-সহ সবকিছু APK খুলে বের করা যায়। আসল secret server-এ থাকে।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Device-এর data-র জন্য আমি key রাখি Android Keystore-এ, সম্ভব হলে hardware-backed। তাতে key ব্যবহার করা যায়, কিন্তু বের করা যায় না। Refresh token-এর মতো জিনিস আমি ওই key দিয়ে encrypt করি — এখন Tink আর DataStore দিয়ে, কারণ Jetpack-এর EncryptedSharedPreferences deprecated। আর এগুলো backup থেকে বাদ দিই, নইলে নতুন phone-এ restore হয়ে decrypt হয় না।
>
> Network-এ শুধু HTTPS, আর সেটা Network Security Config দিয়ে enforce করি। Certificate pinning করলে সবসময় backup pin আর rotation plan রাখি। একটা ভুল pin সব user-কে একসাথে আটকে দিতে পারে।
>
> আর আমি পরিষ্কার জানি, APK-তে যা যায় — API key-সহ — সব public। তাই আসল secret server-এ থাকে, আর backend যেন client-কে বিশ্বাস করতে পারে, তার জন্য Play Integrity, যার verdict server-এ check হয়।

*English:*
> For data at rest, keys live in the Android Keystore, ideally hardware-backed, so they can be used but never extracted. I encrypt sensitive values like refresh tokens with such a key — today with Tink and DataStore, since Jetpack's EncryptedSharedPreferences has been deprecated — and I exclude them from backups.
>
> For transport, it's HTTPS only, enforced by the Network Security Config, and certificate pinning only with backup pins and a rotation plan, because a wrong pin can lock every user out.
>
> And I'm clear that anything shipped in the APK, including API keys, is public, so real secrets stay on the server, and Play Integrity helps the backend trust the client.

**সাধারণ ভুল:**
- Biometric-এর পর শুধু একটা "success" boolean দেখে কাজ চালানো। Rooted device-এ ওটা বদলানো যায়। Key-টাই biometric দিয়ে বাঁধুন।
- Encrypted data backup-এ রেখে দেওয়া। নতুন phone-এ key নেই, তাই decrypt হয় না, app crash করে।
- Backup pin ছাড়া, বা শুধু leaf certificate pin করা। Certificate বদলালেই সব পুরনো app-এর network বন্ধ।
- API key বা অন্য secret APK-এ রেখে ভাবা যে R8 সেটা লুকিয়ে রাখবে। R8 শুধু পড়া কঠিন করে, লুকায় না।
- Play Integrity-র verdict app-এর ভেতরে check করা। Attacker সেই check-টাই বদলে দেয়।

**Follow-up প্রশ্ন:** "Certificate pinning কি সবসময় করা উচিত?"

*বাংলায়:*
> না, আমি এটা ঝুঁকি মেপে করি। Pinning মাঝখানের attack আটকায়, কিন্তু server-এর certificate বদলালে আর app-এ নতুন pin না থাকলে সব পুরনো app একসাথে বন্ধ হয়ে যায়। তাই করলে backup pin রাখি, intermediate বা public key pin করি, আর backend-এর সাথে rotation plan ঠিক করি।

*English:*
> No, I weigh the risk first. Pinning blocks man-in-the-middle attacks, but if the server certificate changes and the app has no matching pin, every old install loses the network at once. So when I pin, I keep a backup pin, pin the intermediate or public key, and agree on a rotation plan with the backend.

[উপরে ফিরুন](#toc)

---

### <a id="q55"></a>Q55. Exported component, PendingIntent, WebView আর deep link security

**কত ঘন ঘন:** Deeper · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** অন্য app আপনার app-এ ঢুকতে পারে চারটা দরজা দিয়ে: **exported component** (Activity, Service, Receiver, Provider), **mutable PendingIntent**, **WebView**-এর JavaScript bridge, আর **deep link**। মূল নিয়ম একটাই: বাইরে থেকে যা আসে, সব user input-এর মতো অবিশ্বস্ত। যা বাইরে দরকার নেই সেটা `exported="false"`। PendingIntent `IMMUTABLE`। WebView-এ শুধু নিজের domain। আর deep link-এর parameter কখনো বিশ্বাস করবেন না।

---

#### Intent redirection — একটা পরিচিত bug

`exported="false"` Activity বাইরের app সরাসরি খুলতে পারে না। কিন্তু আপনার একটা exported Activity যদি বাইরের পাঠানো intent হুবহু চালিয়ে দেয়, তাহলে সেটা চলে আপনার app-এর পরিচয়ে। মানে private Activity-ও খুলে যায়।

```kotlin
// বিপজ্জনক: বাইরের app একটা intent পাঠাল, আমরা চোখ বন্ধ করে চালালাম
val forward = IntentCompat.getParcelableExtra(intent, "next", Intent::class.java)
startActivity(forward)      // attacker আপনার private (exported=false) Activity খুলতে পারে
```

সমাধান: বাইরের intent থেকে শুধু data নিন (id, string)। সেটা validate করুন। তারপর নিজে নতুন intent বানান।

---

#### App Links — verified deep link

সাধারণ deep link যে কোনো app দাবি করতে পারে। App Link-এ Android domain-এর কাছে গিয়ে check করে, link-টা সত্যিই আপনার app-এর কি না।

```xml
<activity android:name=".MainActivity" android:exported="true">
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https" android:host="example.com" android:pathPrefix="/product" />
    </intent-filter>
</activity>
```

- Domain-এ `https://example.com/.well-known/assetlinks.json` রাখুন। সেখানে থাকে app-এর package আর **signing certificate-এর SHA-256**। Play App Signing ব্যবহার করলে Play Console-এর **app signing key**-র SHA-256 দিন, upload key-র না। Play আপনার app নিজের key দিয়ে আবার sign করে, তাই user-এর phone-এ ওই key-টাই থাকে। এটা খুব সাধারণ ভুল।
- Android 12 থেকে verify না হওয়া `https` link সরাসরি app খোলে না, browser-এ যায়।
- Custom scheme (`myapp://`) যেকোনো app দাবি করতে পারে। তাই গোপন কিছু (যেমন OAuth code) custom scheme দিয়ে পাঠাবেন না, অথবা PKCE ব্যবহার করুন।
- Test: `adb shell pm get-app-links com.example.app`।

আর একটা নিয়ম: deep link শুধু navigate করে। এটা কখনো login পার করে যায় না, আর user-এর confirm ছাড়া কোনো action চালায় না।

**Flutter-এর সাথে মিল:** Flutter app-এও এই manifest আর `assetlinks.json` একই। Router-এ link আসার পর parameter validate করার দায়িত্বও একই।

---

#### WebView — শুধু নিজের domain

```kotlin
webView.settings.apply {
    javaScriptEnabled = true          // দরকার হলেই শুধু
    allowFileAccess = false
    allowContentAccess = false
}
webView.webViewClient = object : WebViewClient() {
    override fun shouldOverrideUrlLoading(view: WebView, request: WebResourceRequest): Boolean {
        val host = request.url.host ?: return true
        return host !in setOf("example.com", "help.example.com")   // বাইরের domain আটকাও
    }
}
```

`shouldOverrideUrlLoading` থেকে `true` মানে "এই URL WebView-এ খুলবে না"। তাই list-এর বাইরের সব host আটকে যায়।

`addJavascriptInterface` দিলে ওই page-এর JavaScript আপনার Kotlin method call করতে পারে। বাইরের কোনো page সেখানে খুললে সেই page-ও পারবে। তাই এটা শুধু নিজের page-এর জন্য।

---

#### ContentProvider

`exported="false"` রাখুন। অন্য app-কে file দিতে হলে `FileProvider` + `FLAG_GRANT_READ_URI_PERMISSION` দিয়ে শুধু ওই একটা URI-র সাময়িক অনুমতি দিন। পুরো provider খুলে দেওয়ার দরকার নেই।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> App-এর বাইরে থেকে যা আসে, আমি সব অবিশ্বস্ত input ধরি। Component দরকার না হলে export করি না। আর যেগুলো exported, সেগুলো intent validate করে, বা signature permission দিয়ে সুরক্ষিত থাকে। PendingIntent default-এ immutable। বাইরের intent আমি কখনো সরাসরি `startActivity`-তে পাঠাই না — এটাই সেই পরিচিত intent redirection bug।
>
> Deep link-এর জন্য আমি verified App Links নিই, `autoVerify` আর domain-এ `assetlinks.json` দিয়ে। Deep link শুধু navigate করে — login পার করে না, user confirm না করলে কোনো action চালায় না।
>
> WebView-এ শুধু allow-list করা URL খুলি, আর JavaScript interface শুধু নিজের page-কে দিই।

*English:*
> I treat every entry point from outside the app as untrusted input. Components are not exported unless they must be, and exported ones validate their intents or are protected by a signature permission. PendingIntents are immutable by default, and I never forward an incoming intent blindly to `startActivity`, because that's the classic intent redirection bug.
>
> For deep links I use verified App Links with `autoVerify` and an `assetlinks.json` on the domain, and a deep link can only navigate — it never skips authentication or performs an action without the user confirming.
>
> In WebViews I load only allow-listed URLs and expose JavaScript interfaces only to my own pages.

**সাধারণ ভুল:**
- `assetlinks.json`-এ upload key-র SHA-256 দেওয়া। Play App Signing-এ phone-এর app অন্য key দিয়ে sign হয়, তাই verify fail করে আর link browser-এ চলে যায়।
- বাইরের intent থেকে পাওয়া `Intent` হুবহু `startActivity`-তে দেওয়া। Attacker আপনার private Activity খুলে ফেলে।
- OAuth code custom scheme দিয়ে পাঠানো, PKCE ছাড়া। অন্য app একই scheme দাবি করে code নিয়ে নিতে পারে।
- যে WebView বাইরের page খোলে, সেখানে `addJavascriptInterface` দেওয়া। বাইরের JavaScript তখন আপনার Kotlin code চালায়।

**Follow-up প্রশ্ন:** "Custom scheme আর App Link-এর পার্থক্য কী?"

*বাংলায়:*
> Custom scheme (`myapp://`) যে কোনো app নিজের বলে দাবি করতে পারে, কেউ check করে না। App Link হলো `https` link, যেটা Android domain-এর `assetlinks.json` দেখে verify করে। তাই গোপন কিছু আমি custom scheme দিয়ে পাঠাই না, আর পাঠাতেই হলে PKCE দিই।

*English:*
> Any app can claim a custom scheme like `myapp://` — nobody checks it. An App Link is an `https` link that Android verifies against `assetlinks.json` on the domain. So I never send secrets through a custom scheme, and if I must, I use PKCE.

[উপরে ফিরুন](#toc)

---

# J. Testing

### <a id="q56"></a>Q56. ViewModel, coroutine আর Flow-এর unit test

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** ViewModel test করুন তার public API দিয়ে: action পাঠান, তারপর কোন state এল তা দেখুন। Coroutine test চলে `runTest`-এ, যেটা **virtual time** ব্যবহার করে, তাই `delay(5000)` সাথে সাথে শেষ হয়। `Dispatchers.Main` একটা JUnit rule দিয়ে test dispatcher-এ বদলান। Repository-র জন্য mock না, **fake** (ছোট in-memory implementation)। আর Flow test করতে **Turbine**।

---

#### সমস্যাটা কোথায়

দুইটা জিনিস test-কে কঠিন করে। প্রথমত, ViewModel `viewModelScope` ব্যবহার করে, যেটা চলে `Dispatchers.Main`-এ। কিন্তু JVM unit test-এ Android-এর main thread নেই। দ্বিতীয়ত, আসল `delay` বা আসল thread থাকলে test ধীর হয়, আর ফল একেক বার একেক রকম আসে।

সমাধানও দুইটা: Main dispatcher বদলে দিন, আর সময়টা virtual করে দিন।

---

#### Main dispatcher বদলানোর rule

প্রতিটা test class-এ হাতে `setMain` / `resetMain` না লিখে একটা rule বানিয়ে নিন। Test শুরুতে বদলায়, শেষে ফিরিয়ে দেয়।

```kotlin
class MainDispatcherRule(
    val dispatcher: TestDispatcher = UnconfinedTestDispatcher(),
) : TestWatcher() {
    override fun starting(description: Description) = Dispatchers.setMain(dispatcher)
    override fun finished(description: Description) = Dispatchers.resetMain()
}
```

Repository-তেও dispatcher inject করুন। তাহলে test-এ কোনো কিছুই আসল thread ছোঁয় না।

---

#### যে ViewModel test করছি

```kotlin
sealed interface FeedUiState {
    data object Loading : FeedUiState
    data class Success(val articles: List<Article>, val showRefreshError: Boolean = false) : FeedUiState
}

@HiltViewModel
class FeedViewModel @Inject constructor(private val repo: ArticleRepository) : ViewModel() {
    private val refreshFailed = MutableStateFlow(false)

    val uiState: StateFlow<FeedUiState> = combine(repo.observeArticles(), refreshFailed) { list, failed ->
        FeedUiState.Success(list, showRefreshError = failed)
    }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), FeedUiState.Loading)

    fun onRefresh() = viewModelScope.launch {
        refreshFailed.value = repo.refresh().isFailure
    }
}
```

Refresh fail করলে পুরনো list থাকে, শুধু `showRefreshError` true হয়। এটাই আমরা test-এ প্রমাণ করব।

---

#### Fake repository — mock না

Fake হলো interface-এর একটা ছোট, আসল implementation। Test নিজের ইচ্ছামতো data দেয়, আর ফল বদলায়।

```kotlin
class FakeArticleRepository @Inject constructor() : ArticleRepository {   // @Inject: Hilt test-এও লাগবে (Q57)
    private val articles = MutableSharedFlow<List<Article>>(replay = 1)   // শুরুতে কোনো value নেই
    var refreshResult: Result<Unit> = Result.success(Unit)

    suspend fun emit(list: List<Article>) = articles.emit(list)
    override fun observeArticles(): Flow<List<Article>> = articles
    override suspend fun refresh(): Result<Unit> = refreshResult
}
```

`MutableSharedFlow(replay = 1)` বেছে নেওয়ার কারণ: এর শুরুতে কোনো value নেই। তাই test প্রথমে `Loading` দেখতে পায়, তারপর `emit` করলে `Success`। আর `replay = 1` থাকায় পরে subscribe করলেও শেষ list-টা পাওয়া যায়।

কেন fake ভালো: পড়তে সহজ। আর ViewModel-এর ভেতরের code refactor করলে test ভাঙে না, কারণ test কোন method কতবার call হলো তা দেখে না, শুধু ফল দেখে।

---

#### Test

```kotlin
class FeedViewModelTest {
    @get:Rule val mainRule = MainDispatcherRule()
    private val repo = FakeArticleRepository()

    @Test
    fun `shows articles from the repository`() = runTest {
        val viewModel = FeedViewModel(repo)
        viewModel.uiState.test {
            assertEquals(FeedUiState.Loading, awaitItem())
            repo.emit(listOf(article("1")))
            assertEquals(FeedUiState.Success(listOf(article("1"))), awaitItem())
        }
    }

    @Test
    fun `a failed refresh keeps the old list and shows an error`() = runTest {
        repo.emit(listOf(article("1")))
        repo.refreshResult = Result.failure(IOException())
        val viewModel = FeedViewModel(repo)

        viewModel.uiState.test {
            viewModel.onRefresh()
            val state = expectMostRecentItem() as FeedUiState.Success   // stateIn — তাই collect করে পড়ছি
            assertEquals(listOf(article("1")), state.articles)
            assertTrue(state.showRefreshError)
        }
    }
}
```

Test-এর নাম behavior বলে ("a failed refresh keeps the old list..."), method-এর নাম না। আর প্রতিটা feature-এ আমি success, empty, failure আর যে edge case-এর জন্য change হলো — এগুলো cover করি।

---

#### `StandardTestDispatcher` vs `UnconfinedTestDispatcher`

| | Standard | Unconfined |
|---|---|---|
| নতুন coroutine কখন চলে | Queue-তে বসে। `advanceUntilIdle()` বা `runCurrent()` দিলে চলে | সাথে সাথে |
| কখন ভালো | ক্রম আর timing নিয়ন্ত্রণ করতে চাইলে | সহজ test, `StateFlow` collect |

---

#### `stateIn(WhileSubscribed)` test-এর ফাঁদ

`WhileSubscribed` মানে কেউ collect না করলে upstream flow চলেই না। তাই test-এ শুধু `uiState.value` পড়লে সবসময় initial value (`Loading`) দেখায়, repository যা-ই দিক। সমাধান: Turbine দিয়ে collect করুন, অথবা test-এ `backgroundScope.launch { viewModel.uiState.collect() }` চালান।

---

#### Mock কখন

শুধু যখন interaction-টাই behavior। যেমন "analytics event ঠিক একবার পাঠানো হলো কি না"। তখন MockK-এর `verify(exactly = 1)`। বাকি সব জায়গায় fake।

**Flutter-এর সাথে মিল:** `runTest` + virtual time ≈ `fakeAsync`। Turbine ≈ `expectLater(stream, emitsInOrder([...]))`। `bloc_test`-এর `act`/`expect` ধারণাও একই।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> ViewModel আমি test করি তার public API দিয়ে: একটা action পাঠাই, তারপর কোন state এল তা assert করি। Coroutine চলে `runTest`-এ, virtual time-এ। একটা JUnit rule `Dispatchers.Main`-কে test dispatcher দিয়ে বদলে দেয়। Repository-তেও dispatcher inject করি, তাই test-এ কিছুই আসল thread ছোঁয় না।
>
> আমি mock-এর চেয়ে fake পছন্দ করি। ছোট একটা in-memory repository পড়তে সহজ, আর ভেতরের code refactor করলে test ভাঙে না। Flow-এর জন্য Turbine।
>
> একটা ফাঁদ খেয়াল রাখি: `stateIn(WhileSubscribed)` হলে collect না করে `.value` পড়লে শুধু initial value পাওয়া যায়। আর সবসময় success, empty, failure আর যে edge case-এর জন্য change হলো — চারটাই cover করি।

*English:*
> I test ViewModels through their public API: send an action, assert the emitted state. Coroutines run under `runTest`, which uses virtual time, and a JUnit rule swaps `Dispatchers.Main` for a test dispatcher; I also inject dispatchers into repositories, so nothing in a test touches real threads.
>
> I prefer fakes over mocks — a small in-memory repository is easier to read, and tests don't break when I refactor internals. For flows I use Turbine.
>
> One trap I watch for: with `stateIn(WhileSubscribed)`, reading `.value` without collecting only gives the initial value. And I always cover success, empty, failure and the edge case that motivated the change.

**সাধারণ ভুল:**
- `stateIn(WhileSubscribed)`-এর পর collect না করে `uiState.value` assert করা। Flow চলেই না, তাই test সবসময় `Loading` দেখে।
- `Dispatchers.Main` না বদলানো। JVM test-এ main thread নেই, তাই `viewModelScope`-এর coroutine চলে না বা fail করে।
- সব কিছুর জন্য mock, আর প্রতিটা call `verify` করা। Test তখন implementation-এর সাথে বাঁধা, refactor করলেই ভাঙে।
- Test-এ আসল `delay` বা `Thread.sleep`। Test ধীর হয়, আর মাঝে মাঝে fail করে।

**Follow-up প্রশ্ন:** "`StandardTestDispatcher` আর `UnconfinedTestDispatcher`-এর মধ্যে কোনটা নেন?"

*বাংলায়:*
> Standard-এ নতুন coroutine queue-তে বসে থাকে, `advanceUntilIdle()` বা `runCurrent()` দিলে চলে। তাই ক্রম আর timing আমার হাতে থাকে। Unconfined সাথে সাথে চালায়, সহজ test আর `StateFlow` collect করতে সুবিধা। Timing-ই যখন test-এর বিষয়, তখন আমি Standard নিই।

*English:*
> With Standard, new coroutines wait in a queue until I call `advanceUntilIdle()` or `runCurrent()`, so I control order and timing. Unconfined runs them right away, which is handy for simple tests and collecting a `StateFlow`. When timing is what I'm testing, I pick Standard.

[উপরে ফিরুন](#toc)

---

### <a id="q57"></a>Q57. UI test, Robolectric, screenshot test, Hilt test

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Test pyramid মেনে চলুন: অনেক **unit test** (JVM-এ, দ্রুত), কিছু **UI/component test**, আর অল্প কয়টা **end-to-end test** (আসল device-এ)। Compose-এ `createComposeRule()` দিয়ে একটা screen আলাদা করে test করা যায়। **Robolectric** Android framework-কে JVM-এ চালায়, তাই device ছাড়াই UI test চলে। **Screenshot test** (Roborazzi, Paparazzi) UI-র ছবি তুলে আগের ছবির সাথে মেলায়, তাই design ভেঙে গেলে ধরে ফেলে।

**Flutter-এর সাথে মিল:** Compose test ≈ widget test। Screenshot test ≈ golden test। Device-এর end-to-end test ≈ `integration_test`।

---

#### Compose screen test — stateless screen, fake state

Screen যদি state আর `onAction` নেয় (stateless), তাহলে ViewModel ছাড়াই test করা যায়। যে state চান, সেটা দিয়ে দিন, তারপর দেখুন।

```kotlin
class LoginScreenTest {
    @get:Rule val compose = createComposeRule()

    @Test
    fun submitButtonIsDisabledWhileLoading() {
        compose.setContent {
            LoginScreen(state = LoginUiState(isLoading = true), onAction = {})
        }
        compose.onNodeWithText("Login").assertIsNotEnabled()
    }

    @Test
    fun typingEmailSendsAnAction() {
        val actions = mutableListOf<LoginAction>()
        compose.setContent { LoginScreen(state = LoginUiState(), onAction = { actions += it }) }

        compose.onNodeWithTag("email").performTextInput("a@b.com")

        assertEquals(LoginAction.EmailChanged("a@b.com"), actions.last())
    }
}
```

Node খোঁজা হয় semantics বা text দিয়ে। Screen reader-ও এই semantics পড়ে। তাই test যদি node খুঁজে না পায়, accessibility-তেও সম্ভবত সমস্যা আছে। একই test দুইটা কাজ করে।

---

#### কোন tool কোথায়

| Tool | কোথায় চলে | কী কাজে |
|---|---|---|
| JUnit + Turbine + fake | JVM | ViewModel, repository, mapper |
| Compose test (`createComposeRule`) | Device বা Robolectric | একটা screen বা component |
| Robolectric | JVM | Android API লাগে এমন test, device ছাড়া |
| Espresso | Device | পুরনো View UI |
| UI Automator | Device | App-এর বাইরে (notification, permission dialog, অন্য app) |
| Roborazzi / Paparazzi | JVM | Screenshot test |
| Macrobenchmark | Device | Performance |

Robolectric-এর বড় লাভ CI-তে। Emulator ছাড়াই অনেক UI test চলে। আর screenshot test সেই visual ভুল ধরে, যা assertion দিয়ে লেখা কঠিন — যেমন padding বা color বদলে যাওয়া।

---

#### Hilt দিয়ে integration test

Integration test-এ পুরো app চালাতে চান, কিন্তু আসল network বা database ছাড়া। `@TestInstallIn` production module-কে fake module দিয়ে বদলে দেয়, পুরো test build-এ।

```kotlin
@TestInstallIn(components = [SingletonComponent::class], replaces = [DataModule::class])
@Module
abstract class FakeDataModule {
    @Binds abstract fun repo(fake: FakeArticleRepository): ArticleRepository
}

@HiltAndroidTest
class FeedFlowTest {
    @get:Rule(order = 0) val hilt = HiltAndroidRule(this)
    @get:Rule(order = 1) val compose = createAndroidComposeRule<MainActivity>()
    // ...
}
```

Rule-এর `order` খেয়াল করুন। Hilt rule আগে চলে (`order = 0`), যাতে Activity চালু হওয়ার আগেই injection তৈরি থাকে। এখানে `FakeArticleRepository` সেই [Q56](#q56)-এর fake, যার constructor-এ `@Inject` আছে বলেই Hilt এটা বানাতে পারে।

---

#### Flaky test — কেন হয়, কী করবেন

Flaky test মানে একই code-এ কখনো pass, কখনো fail। সাধারণ কারণ: আসল network, আসল সময় (`System.currentTimeMillis`), `Thread.sleep`, animation, আর test-এর মধ্যে শেয়ার করা state।

সমাধান: সময় inject করা, idling/`waitUntil`, test-এ animation বন্ধ করা, আর প্রতিটা test-এর নিজের data।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি pyramid মেনে চলি। বেশিরভাগ test দ্রুত JVM unit test, তারপর screen-এর component test, আর login বা checkout-এর মতো গুরুত্বপূর্ণ journey-র জন্য device-এ অল্প কয়টা end-to-end test।
>
> Compose-এ আমি stateless screen-টা সরাসরি fake state দিয়ে test করি, node খুঁজি semantics বা text দিয়ে — তাতে accessibility-ও check হয়ে যায়। Robolectric দিয়ে এর অনেকগুলো CI-তে JVM-এই চলে, আর screenshot test সেই visual ভুল ধরে যা assertion ধরে না।
>
> Hilt দিয়ে integration test-এ `@TestInstallIn` দিয়ে production module বদলে দিই, যাতে app fake নিয়ে চলে। Flaky test দেখলে সাথে সাথে ঠিক করি — সাধারণত কারণ আসল সময়, আসল network, `sleep` বা animation।

*English:*
> I follow the pyramid: most tests are fast JVM unit tests, then component tests for screens, and a few end-to-end tests on a device for critical journeys like login and checkout.
>
> For Compose I test the stateless screen directly with a fake state, finding nodes by semantics or text, which doubles as an accessibility check. Robolectric lets many of those UI tests run on the JVM in CI, and screenshot tests catch visual regressions that assertions miss.
>
> For integration tests with Hilt, I replace production modules with `@TestInstallIn`, so the app runs with fakes. When a test is flaky, I fix it right away — usually the cause is real time, real network, a `sleep` or an animation.

**সাধারণ ভুল:**
- Test-এ `Thread.sleep` দিয়ে UI-র জন্য অপেক্ষা করা। Device ধীর হলে fail, দ্রুত হলে সময় নষ্ট। Idling বা `waitUntil` ব্যবহার করুন।
- `System.currentTimeMillis` সরাসরি code-এ। Test-এ সময় নিয়ন্ত্রণ করা যায় না। সময় inject করুন।
- Test-গুলো একই state শেয়ার করা। একটার ফল অন্যটাকে বদলায়, আর order বদলালে fail করে।
- Animation চালু রেখে UI test। Animation শেষ হওয়ার আগে assert হয়ে যায়।
- Hilt rule-এর `order` না দেওয়া। Activity আগে চালু হলে injection তৈরি থাকে না।

**Follow-up প্রশ্ন:** "Notification বা permission dialog test করবেন কীভাবে?"

*বাংলায়:*
> ওগুলো app-এর বাইরের UI, তাই Compose test বা Espresso সেখানে পৌঁছায় না। এর জন্য আমি UI Automator নিই, device-এ। তবে এমন test অল্প রাখি, শুধু গুরুত্বপূর্ণ journey-তে।

*English:*
> Those are outside the app, so Compose tests and Espresso can't reach them. I use UI Automator on a device for that, and I keep those tests few, only for critical journeys.

[উপরে ফিরুন](#toc)

---

# K. Android version

### <a id="q58"></a>Q58. সাম্প্রতিক Android version-এর বড় পরিবর্তন কী কী?

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium

**সংক্ষেপে:** Senior interview-এ প্রশ্নটা প্রায়ই এভাবে আসে: "targetSdk বাড়ানোর সময় কী কী ভাঙে?" মূল ধারা চারটা। Background কাজ আরও সীমিত। Permission আরও ছোট ছোট ভাগে। Edge-to-edge বাধ্যতামূলক। আর বড় screen-এ app-কে resize হতে দিতে হবে। পুরো table মুখস্থ না করে **প্রতিটা version থেকে ২–৩টা জিনিস** মনে রাখুন।

---

#### targetSdk bump-কে একটা ছোট project ধরুন

নতুন version-এর অনেক পরিবর্তন শুধু তখনই চালু হয়, যখন আপনি targetSdk বাড়ান। আর Play-এর একটা deadline আছে, তার পরে পুরনো target-এ update দেওয়া যায় না। তাই কাজটা হলো: behavior changes পড়া, codebase-এ affected API খোঁজা, আর deadline-এর আগে নতুন version-এ test করা।

---

#### Version অনুযায়ী পরিবর্তন

| Version | API | মনে রাখার মতো পরিবর্তন |
|---|---|---|
| Android 12 | 31 | SplashScreen API। `android:exported` বাধ্যতামূলক। PendingIntent mutability flag। Approximate location। Background থেকে FGS শুরু নিষেধ। Exact alarm permission। Verified App Links ছাড়া link browser-এ যায় |
| Android 13 | 33 | `POST_NOTIFICATIONS` runtime permission। আলাদা media permission। Per-app language। Predictive back-এর শুরু (opt-in) |
| Android 14 | 34 | FGS type বাধ্যতামূলক। Partial photo access। Runtime receiver-এ exported flag। নতুন install-এ exact alarm default-এ বন্ধ। খুব পুরনো targetSdk-এর app install করা যায় না |
| Android 15 | 35 | target 35-এ **edge-to-edge বাধ্যতামূলক**। 16 KB page size device। `dataSync` FGS-এর সময়সীমা। Private space |
| Android 16 | 36 | বড় screen-এ (≥600dp) orientation আর resizability lock উপেক্ষা হয়। Edge-to-edge থেকে opt-out আর নেই। Predictive back animation default-এ। Progress-centric notification |
| Android 17 | 37 | (জুন ২০২৬-এ stable) Local network-এ device খুঁজতে নতুন `ACCESS_LOCAL_NETWORK` runtime permission। Certificate Transparency default-এ চালু। OTP চুরি ঠেকাতে নতুন আসা SMS বেশিরভাগ app কিছু সময় পড়তে পারে না। Reflection দিয়ে `static final` field বদলানো যায় না। নতুন lock-free `MessageQueue` — যে code reflection দিয়ে এটা ঘাঁটে, সেটা ভাঙে |
| Android 18+ | — | Interview-এর আগে [developer.android.com/about/versions](https://developer.android.com/about/versions) দেখুন |

> Android 17-এর row নতুন। কোন পরিবর্তন সব app-এ খাটে আর কোনটা শুধু target 37-এ, সেটা interview-এর আগে [behavior changes page](https://developer.android.com/about/versions/17/behavior-changes-17)-এ একবার মিলিয়ে নিন।

---

#### Edge-to-edge-এর জন্য কী করবেন (Android 15+)

Edge-to-edge মানে app-এর content status bar আর navigation bar-এর নিচ পর্যন্ত আঁকা হয়। তাই আপনাকে নিজে insets (system bar-এর জায়গা) ছেড়ে দিতে হয়, নইলে button বা text bar-এর নিচে ঢাকা পড়ে।

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    enableEdgeToEdge()
    super.onCreate(savedInstanceState)
    setContent {
        Scaffold { innerPadding ->              // Scaffold insets দেয়
            Content(Modifier.padding(innerPadding))
        }
    }
}
// Scaffold ছাড়া: Modifier.windowInsetsPadding(WindowInsets.safeDrawing)
```

**Flutter-এর সাথে মিল:** Flutter-এ এটা `SafeArea` বা `MediaQuery`-র padding-এর কাজ।

---

#### Predictive back

`onBackPressed()` override করার বদলে `OnBackPressedCallback` বা Compose-এ `BackHandler` / `PredictiveBackHandler` ব্যবহার করুন। কারণ predictive back-এ system আগে থেকেই জানতে চায় back আপনি handle করবেন কি না, যাতে animation দেখাতে পারে। নতুন target-এ পুরনো `onBackPressed()` আর ঠিকমতো call হয় না।

---

#### Adaptive layout

Window size class (`currentWindowAdaptiveInfo()`) দেখে layout বদলান: phone-এ এক কলাম, tablet বা foldable-এ list + detail পাশাপাশি। Android 16 থেকে বড় screen-এ "শুধু portrait" lock কাজ করে না। তাই এটা এখন optional না।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> প্রতিটা targetSdk bump-কে আমি একটা ছোট project ধরি। Behavior changes পড়ি, codebase-এ affected API খুঁজি, আর Play-এর deadline-এর আগে নতুন version-এ test করি।
>
> গত কয়েকটা release-এর ধারা পরিষ্কার। Background limit আরও কড়া, যেমন 14-এ FGS type। Permission আরও ছোট ভাগে, যেমন 13-এ notification আর 14-এ partial photo access। 15 থেকে edge-to-edge বাধ্যতামূলক। 16-এ বড় screen-এ orientation বা resizability lock করা যায় না। আর 17-এ local network permission এসেছে, Certificate Transparency default-এ চালু।
>
> তাই আমি feature বানাই এই দিকগুলো মেনেই — লম্বা service-এর বদলে WorkManager, storage permission-এর বদলে photo picker, আর insets-aware, adaptive layout।

*English:*
> I treat every targetSdk bump as a small project: read the behavior changes, search the codebase for affected APIs, and test on the new version before the Play deadline.
>
> The trend over the last releases is clear — tighter background limits, like foreground service types in 14; finer-grained permissions, like notifications in 13 and partial photo access in 14; edge-to-edge enforced from 15; in 16, apps on large screens can no longer lock orientation or resizability; and 17 adds a local network permission and turns on Certificate Transparency by default.
>
> So I build features that already respect those directions — WorkManager instead of long services, the photo picker instead of storage permissions, and insets-aware, adaptive layouts.

**সাধারণ ভুল:**
- targetSdk শুধু একটা সংখ্যা ভেবে বাড়িয়ে দেওয়া, behavior changes না পড়ে। Release-এর পর crash বা ভাঙা feature ধরা পড়ে।
- Edge-to-edge-এ insets না দেওয়া। Content status bar বা navigation bar-এর নিচে ঢাকা পড়ে।
- এখনো `onBackPressed()` override করা। নতুন target-এ ওটা ঠিকমতো call হয় না, back কাজ করে না।
- বড় screen-এ portrait lock-এর উপর ভরসা করা। Android 16 থেকে সেটা উপেক্ষা হয়, layout ভেঙে যায়।

**Follow-up প্রশ্ন:** "Android 17-এর কোন পরিবর্তন আপনার app-কে ভাঙতে পারে?"

*বাংলায়:*
> আমি প্রথমে দেখি app local network-এ device খোঁজে কি না — তাহলে নতুন `ACCESS_LOCAL_NETWORK` permission লাগবে। তারপর দেখি কোনো library reflection দিয়ে `static final` field বা `MessageQueue` ঘাঁটে কি না, কারণ ওগুলো এখন ভাঙে। SMS থেকে OTP পড়লে সেটাও দেখি। আর কোনটা সব app-এ খাটে আর কোনটা শুধু target 37-এ, সেটা behavior changes page-এ মিলিয়ে নিই।

*English:*
> First I check whether the app discovers devices on the local network — then it needs the new `ACCESS_LOCAL_NETWORK` permission. Then I check whether any library uses reflection on `static final` fields or on `MessageQueue`, since that now breaks. If we read OTPs from SMS, I check that too. And I confirm on the behavior changes page which changes hit all apps and which only apply when targeting 37.

[উপরে ফিরুন](#toc)

---

# L. Mobile system design (Android দিক)

> সাধারণ design framework, REST vs WebSocket, auth, photo upload, push notification, cart — এগুলো আপনার Flutter guide-এর [Section 21](../software-engineer-flutter-bn/section-21-system-design-bn.md)-এ আছে। এখানে দেখানো হয়েছে, Android interviewer একই design-এ **কোন Android component** শুনতে চায়।

### <a id="q59"></a>Q59. Android system design interview-এর কাঠামো

**কত ঘন ঘন:** Very common · **কঠিনতা:** Hard

**সংক্ষেপে:** ৪৫ মিনিটকে চার ভাগে ভাগ করুন: **requirement** (৫–৭ মিনিট) → **high-level diagram** (১০ মিনিট) → **২–৩টা জায়গায় গভীরে** (২০ মিনিট) → **trade-off আর পরের ধাপ** (৫ মিনিট)। Flutter interview-এর framework-ই, শুধু component-এর নাম Android-এর। Android interviewer বিশেষ করে শুনতে চায়: data কোথায় থাকে (single source of truth), process death আর offline-এ কী হয়, background কাজ কোন tool দিয়ে, battery আর data খরচ, আর সফলতা কীভাবে মাপবেন (metric)।

---

#### কেন এই ভাগ

Requirement আগে, কারণ scope না জেনে আঁকলে ভুল জিনিস design করবেন। ১০০ item আর ১ লাখ item-এর design আলাদা। Offline লেখা লাগলে sync-এর পুরো একটা অংশ যোগ হয়। আর গভীরে সব জায়গায় যাওয়ার সময় নেই। তাই এই product-এর জন্য সবচেয়ে কঠিন ২–৩টা জায়গা বেছে নিন — যেমন sync আর conflict, background কাজ আর notification, বা মূল list-এর performance।

---

#### যে প্রশ্নগুলো আপনি নিজে জিজ্ঞেস করবেন

| বিষয় | প্রশ্ন |
|---|---|
| Feature | মূল ৩টা feature কী? কোনটা version 1-এ না? |
| Scale | কত user? একজন user-এর কত data (১০০ item না ১ লাখ)? |
| Offline | Offline-এ পড়া? লেখা? |
| Real-time | কত দ্রুত update দেখাতে হবে — সাথে সাথে, না কয়েক মিনিটে? |
| Device | minSdk কত? কম দামের phone, ধীর network (BD market)? Tablet? |
| Backend | API আছে, না আমরা design করব? |

---

#### Android-specific checklist — প্রতিটা design-এ একবার ছুঁয়ে যান

- **Source of truth:** Room। UI শুধু Flow observe করে।
- **Process death:** কোন state `SavedStateHandle`-এ, কোনটা database-এ।
- **Background:** WorkManager (sync, upload), FCM (server push), FGS শুধু user-visible হলে।
- **Pagination:** Paging 3 + cursor।
- **Image:** Coil, server-side resize, disk cache size।
- **Network:** OkHttp cache, retry with backoff, timeout, ধীর network-এ ছোট payload।
- **Security:** Token Keystore-এ, backup থেকে বাদ ([Q54](#q54))।
- **Modularization:** Feature module যদি team বড় হয়।
- **Observability:** Crashlytics, Android vitals, startup আর frame metric, analytics funnel।
- **Rollout:** Feature flag (Remote Config), staged rollout, পুরনো app version-এর জন্য API backward compatible। পুরনো app update না করেও চলতে থাকে, তাই API এক ধাক্কায় বদলানো যায় না।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> কিছু আঁকার আগে আমি scope পরিষ্কার করে নিই: মূল feature, scale, offline-এ চলতে হবে কি না, real-time কতটা লাগবে, আর কোন device ও Android version support করব।
>
> তারপর client architecture আঁকি — UI, ViewModel, repository, source of truth হিসেবে local database, আর network ও sync layer। Backend-এর সাথে API-র shape ঠিক করি। এরপর এই product-এর সবচেয়ে কঠিন ২–৩টা জায়গায় গভীরে যাই, যেমন sync আর conflict, background কাজ আর notification, বা মূল list-এর performance।
>
> শেষে trade-off বলি, সফলতা কীভাবে মাপব, আর version 2-এ কী করব।

*English:*
> Before drawing anything, I'd like to clarify scope: the core features, scale, whether it must work offline, real-time needs, and which devices and Android versions we support.
>
> Then I'll sketch the client architecture — UI, ViewModel, repository, local database as the source of truth, and the network and sync layer — and agree on the API shape with the backend. I'd go deep on two or three areas that are hardest for this product, for example sync and conflicts, background work and notifications, and performance of the main list.
>
> I'll finish with trade-offs, how we measure success, and what I'd do in a second version.

**সাধারণ ভুল:**
- Requirement না জিজ্ঞেস করেই diagram আঁকা শুরু। ভুল scale বা ভুল feature-এর জন্য design হয়।
- সব box-এ একটু একটু গভীরে যাওয়া। কোথাও আসল গভীরতা দেখানো হয় না, সময়ও শেষ।
- Process death আর offline-এ কী হয়, সেটা না বলা। Android interviewer ঠিক এটাই শুনতে চায়।
- Metric আর rollout বাদ দেওয়া। Senior level-এ "কীভাবে মাপব আর নিরাপদে ছাড়ব" design-এরই অংশ।

**Follow-up প্রশ্ন:** "কোন জায়গায় গভীরে যাবেন, সেটা কীভাবে ঠিক করেন?"

*বাংলায়:*
> যেটা এই product-এর জন্য সবচেয়ে কঠিন বা সবচেয়ে ঝুঁকির, সেটা। Feed-এ সাধারণত pagination আর cache, chat-এ real-time আর delivery, offline app-এ sync আর conflict। আর interviewer কোনো দিকে আগ্রহ দেখালে আমি সেদিকেই যাই।

*English:*
> The parts that are hardest or riskiest for this product. For a feed, that's usually pagination and caching; for chat, real-time delivery; for an offline app, sync and conflicts. And if the interviewer shows interest in an area, I go there.

[উপরে ফিরুন](#toc)

---

### <a id="q60"></a>Q60. উদাহরণ: offline-first news/social feed app (Android)

**কত ঘন ঘন:** Very common · **কঠিনতা:** Hard

**সংক্ষেপে:** Room হলো source of truth। Paging 3 + `RemoteMediator` network থেকে page এনে Room-এ রাখে। UI শুধু Room থেকে `PagingData` পড়ে, তাই offline-এও শেষ দেখা feed দেখায়। Like/bookmark আগে Room-এ (optimistic), তারপর WorkManager দিয়ে server-এ। নতুন post-এর খবর FCM দিয়ে আসে, আর "নতুন post আছে" pill দেখায় — list হঠাৎ নিজে সরে যায় না।

**Flutter-এর সাথে মিল:** Flutter-এও একই কাঠামো: local database source of truth, repository stream দেয়, UI শুধু সেই stream দেখে। পার্থক্য শুধু library-র নামে।

---

#### পুরো ছবি

```
┌──────────── :feature:feed ─────────────┐
│ FeedScreen (LazyColumn + PagingItems)  │
│        ▲ PagingData      │ action      │
│ FeedViewModel ◀──────────┘             │
└────────│───────────────────────────────┘
         ▼
┌──────────── :core:data ────────────────┐
│ FeedRepository                         │
│   Pager(RemoteMediator, Room source)   │
│   toggleLike() → Room + enqueue sync   │
└───┬──────────────────┬─────────────────┘
    ▼                  ▼
:core:database      :core:network
 Room: posts,        Retrofit: GET /feed?cursor=
 remote_keys,        POST /likes (idempotency key)
 pending_actions
    ▲
    └── SyncWorker (WorkManager, network constraint)
            ▲
         FCM data message ("feed_updated")
```

UI কখনো network থেকে সরাসরি পড়ে না। Network শুধু Room-এ লেখে, আর UI Room দেখে। তাই data আসার রাস্তা একটাই, আর offline-এ কিছু আলাদা করে handle করতে হয় না।

---

#### গভীরে ১ — Pagination আর cache

- API: `GET /feed?cursor=abc&limit=20` → `{ items, nextCursor }`। Cursor নেওয়ার কারণ: নতুন post এলে offset সরে যায়, কিন্তু cursor সরে না।
- `RemoteMediator.load()`: `REFRESH` হলে প্রথম page আনুন আর পুরনো cache বদলে দিন (একটা `@Transaction`-এ, যাতে মাঝপথে খালি list না দেখায়)। `APPEND` হলে `remote_keys` table থেকে cursor নিয়ে পরের page।
- `initialize()`-এ দেখুন cache কত পুরনো। ৫ মিনিটের কম হলে `SKIP_INITIAL_REFRESH` — network call বাঁচে।
- Database অসীম বড় হতে দেবেন না। শেষ কয়েকশো post রাখুন, পুরনোগুলো WorkManager দিয়ে মুছুন।

---

#### গভীরে ২ — Optimistic like

Optimistic মানে server-এর উত্তরের অপেক্ষা না করে UI আগেই বদলে দেওয়া।

1. Room-এ `isLiked = true`, `likeCount + 1`, আর `pending_actions`-এ একটা row (client UUID সহ)।
2. UI সাথে সাথে বদলায়, কারণ UI Room Flow দেখছে।
3. `SyncWorker` pending row পাঠায়। Server একই UUID দুইবার পেলে একবারই গোনে (idempotent)। তাই retry হলেও like দুইবার গোনা হয় না।
4. Server চূড়ান্তভাবে না বললে (যেমন post মুছে গেছে) → Room-এ আগের অবস্থায় ফিরিয়ে দিন আর ছোট একটা message দেখান।

Sync job unique রাখুন, যাতে একসাথে দুইটা worker একই row না পাঠায়।

---

#### গভীরে ৩ — Performance

- Item-এ `key` আর `contentType` দিন ([Q29](#q29))। Image fixed size, server থেকে ছোট version।
- Baseline Profile-এ feed scroll journey রাখুন ([Q47](#q47))।
- ধীর network-এ: ছোট page, `Accept-Encoding: gzip`, শুরুতে text আগে, image পরে।
- মাপব: cold start, প্রথম post দেখাতে কত সময়, scroll jank, আর sync fail rate।

---

#### Trade-off যা বলবেন

- Room cache মানে বেশি storage আর বেশি code। কিন্তু বিনিময়ে instant open আর offline পাওয়া যায়।
- Optimistic UI মানে মাঝে মাঝে rollback। কিন্তু app দ্রুত লাগে।
- FCM-এ পুরো ভরসা করা যায় না (delay হতে পারে, কিছু device-এ আটকে যায়)। তাই open-এ refresh-ও রাখুন।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> এখানে database-ই source of truth। Paging 3-এর RemoteMediator cursor API দিয়ে page এনে Room-এ লেখে, আর UI শুধু Room থেকে paged data পড়ে। তাই feed সাথে সাথে খোলে, offline-এও চলে।
>
> Like আর bookmark আগে Room-এ বদলায়, optimistic ভাবে। তারপর একটা unique WorkManager job retry আর idempotency key দিয়ে server-এ sync করে, যাতে duplicate না হয়। Data কয়েক মিনিটের বেশি পুরনো হলে open-এ refresh করি, আর FCM data message background refresh চালাতে পারে। নতুন post এলে list লাফায় না, একটা "new posts" pill দেখাই।
>
> মাপি cold start, প্রথম post কত দ্রুত আসে, scroll jank আর sync fail rate।

*English:*
> The database is the source of truth: Paging 3 with a RemoteMediator fetches pages with a cursor API and writes them into Room, and the UI only reads paged data from Room, so the feed opens instantly and works offline.
>
> Likes and bookmarks update Room first, optimistically, and a unique WorkManager job syncs them with retries and idempotency keys. For freshness, I refresh on open if the data is older than a few minutes, and an FCM data message can trigger a background refresh; the UI shows a 'new posts' pill instead of jumping the list.
>
> I'd measure cold start, time to first post, scroll jank and sync failure rate.

**সাধারণ ভুল:**
- UI-কে network আর database দুই জায়গা থেকেই পড়তে দেওয়া। দুইটা source মিলে না, আর offline-এ আলাদা code লাগে।
- Offset pagination। নতুন post এলে page সরে যায়, তাই item বাদ পড়ে বা দুইবার আসে।
- Like sync-এ idempotency key না রাখা। Retry হলে server like দুইবার গোনে।
- Database-কে অসীম বড় হতে দেওয়া। Storage ভরে যায়, query ধীর হয়।
- শুধু FCM-এর উপর ভরসা করে fresh data আনা। FCM দেরি করলে বা আটকে গেলে feed পুরনো থাকে।
- নতুন data এলে list নিজে নিজে উপরে লাফানো। User যা পড়ছিল তা হারিয়ে যায়।

**Follow-up প্রশ্ন:** "Like করার পর server যদি না বলে?"

*বাংলায়:*
> UI আগেই বদলে গেছে, তাই আমি Room-এ আগের অবস্থা ফিরিয়ে দিই — `isLiked` আর count দুইটাই — আর ছোট একটা message দেখাই, যেমন post মুছে গেছে। এই মাঝে মাঝে rollback-ই optimistic UI-র দাম, কিন্তু বিনিময়ে app অনেক দ্রুত লাগে।

*English:*
> The UI has already changed, so I roll back Room — both `isLiked` and the count — and show a short message, for example that the post was deleted. That occasional rollback is the price of optimistic UI, and the app feels much faster for it.

[উপরে ফিরুন](#toc)

---

### <a id="q61"></a>Q61. উদাহরণ: chat app (Android দিক)

**কত ঘন ঘন:** Common · **কঠিনতা:** Hard

**সংক্ষেপে:** Chat screen সামনে থাকলে **WebSocket** দিয়ে real-time message। App background-এ বা বন্ধ থাকলে **FCM** দিয়ে message আর notification। Background-এ WebSocket ধরে রাখবেন না — battery আর system limit দুইটাই বাধা দেয়। সব message আগে Room-এ যায়, একটা client id আর status (`SENDING → SENT → DELIVERED → READ`) সহ। পাঠানোর queue চালায় WorkManager, তাই network না থাকলেও পরে চলে যায়।

---

#### দুইটা রাস্তা, কেন

Foreground-এ WebSocket সবচেয়ে দ্রুত। কিন্তু background-এ Android নিজেই app-এর network আর CPU সীমিত করে, আর খোলা socket battery খায়। তাই background-এ কাজটা FCM-কে দিন। FCM-এর connection system আগে থেকেই সব app-এর জন্য একটা রাখে।

দুই রাস্তাই শেষে একই জায়গায় লেখে: Room। UI শুধু Room দেখে।

---

#### Android-এ কোন জিনিস কীভাবে

| বিষয় | Android-এ কীভাবে |
|---|---|
| Socket-এর জীবন | `ProcessLifecycleOwner` দিয়ে app foreground-এ connect, background-এ disconnect |
| Background message | FCM **data** message → `FirebaseMessagingService.onMessageReceived` → Room-এ লেখা → notification |
| Notification | `NotificationCompat.MessagingStyle`, conversation channel, conversation shortcut (Android 11+ conversation section-এ দেখায়) |
| Direct reply | `RemoteInput` action। এখানে PendingIntent **mutable** হতে হয় — system reply text যোগ করে। এটাই ঠিক ব্যতিক্রম ([Q20](#q20)) |
| পাঠানোর queue | Room-এ `status = SENDING` → unique `SendMessagesWorker` (expedited, network constraint) |
| Duplicate ঠেকানো | Client UUID। Server echo এলে UUID মিলিয়ে local message update |
| ক্রম | Server-এর sequence number বা timestamp। Device-এর ঘড়ি ভুল হতে পারে |
| পুরনো message | Paging 3, উল্টো দিকে (`reverseLayout = true`), cursor দিয়ে আগের page |
| Image/video | আগে compress, তারপর আলাদা `UploadWorker`, progress notification। বড় video হলে Android 14+-এ user-initiated data transfer job ([Q21](#q21)) |
| Read receipt | Screen দেখা গেলে (`onStart`) batch করে পাঠানো, প্রতিটা message-এ আলাদা call না |
| Notification permission | Android 13+-এ `POST_NOTIFICATIONS` চাইতে হয় — প্রথম chat খোলার সময়, startup-এ না |

দুইটা জিনিস একটু ব্যাখ্যা চায়:
- **Duplicate:** Message পাঠানোর আগেই client একটা UUID দেয়। Server সেই message ফেরত পাঠালে (echo) UUID মিলিয়ে local row update হয়, নতুন row তৈরি হয় না।
- **Permission-এর সময়:** Startup-এ চাইলে user কারণ বোঝে না, তাই প্রায়ই না বলে দেয়। প্রথম chat খোলার সময় কারণটা স্পষ্ট।

---

#### Trade-off যা বলবেন

- **FCM data message vs notification message:** Data message-এ app নিজে notification বানায়, তাই আগে Room-এ লেখা যায়। কিন্তু app force-stop করা থাকলে data message আসে না।
- **End-to-end encryption:** চাইলে key থাকে Keystore-এ ([Q54](#q54)), আর server শুধু encrypted blob দেখে। কিন্তু তখন search আর multi-device অনেক জটিল হয়।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Chat screen-এ থাকলে আমি একটা WebSocket খোলা রাখি, lifecycle-এর সাথে বাঁধা, যাতে app background-এ গেলে বন্ধ হয়ে যায়। Background-এ socket রাখলে battery শেষ হয় আর system limit-এর সাথে লড়াই করতে হয়। Background-এ message আসে FCM দিয়ে: data message Room-এ লেখে, তারপর direct-reply action-সহ একটা MessagingStyle notification দেখায়।
>
> প্রতিটা message আগে Room-এ যায়, client-এর বানানো id আর status নিয়ে। একটা unique WorkManager job outbox পাঠায়, তাই offline-এ লেখা message network ফিরলে চলে যায়, duplicate ছাড়া।
>
> Media upload আলাদা worker, progress-সহ। আর message-এর ক্রম আমি নিই server-এর sequence number থেকে, device-এর ঘড়ি থেকে না।

*English:*
> While the chat is on screen, I keep a WebSocket open, tied to the lifecycle, so it closes when the app goes to the background — keeping sockets alive in the background drains the battery and fights system limits. In the background, FCM delivers messages: a data message writes into Room and posts a MessagingStyle notification with a direct-reply action.
>
> Every message is stored in Room first with a client-generated id and a status, and a unique WorkManager job sends the outbox, so offline messages go out when the network returns, without duplicates.
>
> Media uploads are separate workers with progress, and ordering comes from server sequence numbers, not device clocks.

**সাধারণ ভুল:**
- Background-এ WebSocket চালু রাখা, বা FGS দিয়ে ধরে রাখা। Battery শেষ হয়, আর system যেকোনো সময় বন্ধ করে দেয়।
- Device-এর ঘড়ি দিয়ে message সাজানো। ঘড়ি ভুল থাকলে message ভুল ক্রমে দেখায়।
- Client id ছাড়া পাঠানো। Retry বা server echo-তে একই message দুইবার দেখায়।
- Direct reply-র PendingIntent immutable রাখা। System reply text যোগ করতে পারে না, reply কাজ করে না।
- Startup-এ `POST_NOTIFICATIONS` চাওয়া। User কারণ বোঝে না, না বলে দেয়।
- প্রতিটা message-এর read receipt আলাদা call-এ পাঠানো। অকারণে অনেক network call আর battery খরচ।

**Follow-up প্রশ্ন:** "FCM data message নেবেন, না notification message?"

*বাংলায়:*
> Chat-এ আমি data message নিই। তাতে notification আমি নিজে বানাই, তাই আগে message Room-এ লিখে ফেলতে পারি, আর MessagingStyle আর direct reply দিতে পারি। দামটা হলো: app force-stop করা থাকলে data message আসে না। তাই app খুললে আমি server থেকে sync-ও করি।

*English:*
> For chat I use data messages. I build the notification myself, so I can write the message into Room first and use MessagingStyle with direct reply. The cost is that data messages don't arrive while the app is force-stopped, so I also sync from the server when the app opens.

[উপরে ফিরুন](#toc)

---

# M. শেষ ধাপ

### <a id="q62"></a>Q62. Native vs cross-platform — আপনার background নিয়ে Android interviewer যা জিজ্ঞেস করবে

**কত ঘন ঘন:** Very common (আপনার CV-তে Flutter থাকলে প্রায় নিশ্চিত) · **কঠিনতা:** Medium

**সংক্ষেপে:** CV-তে Flutter দেখলে Android interviewer সাধারণত তিনটা প্রশ্ন করে। (১) "কখন Flutter, কখন native বেছে নেবেন?" (২) "Native Android-এ আপনার আসল অভিজ্ঞতা কতটা?" (৩) "Native role কেন চান?" এখানে কোনো পক্ষ নেবেন না। দেখান যে আপনি **product আর team-এর প্রয়োজন** দেখে বেছে নেন। আর platform জ্ঞানের **নির্দিষ্ট উদাহরণ** দিন — plugin লেখা, native crash ঠিক করা, Gradle বা release-এর সমস্যা সমাধান।

---

#### Interviewer আসলে কী যাচাই করছে

তিনি জানতে চান আপনি কোনো framework-এর "fan" কি না। Fan-রা সবকিছু এক tool দিয়ে করতে চায়। Senior engineer আগে প্রয়োজন দেখে, তারপর tool বাছে। দ্বিতীয় যাচাই হলো: Android-এর নিচের layer — lifecycle, Gradle, permission — এগুলো আপনি সত্যিই হাতে-কলমে চেনেন কি না, নাকি শুধু plugin ব্যবহার করেছেন।

---

#### ১. "কখন কোনটা?" — সিদ্ধান্তের table

| প্রয়োজন | পছন্দ |
|---|---|
| ছোট team, দুই platform, সাধারণ screen, দ্রুত বাজারে | Flutter |
| Platform-এর গভীর feature (background, media, widget, Wear, Auto) | Native |
| নতুন Android API প্রথম দিন থেকেই | Native |
| শক্তিশালী native codebase আর team আগে থেকেই আছে | Native, অথবা ধীরে ধীরে KMP |
| Business logic শেয়ার, কিন্তু UI প্রতিটা platform-এর নিজের মতো | Kotlin Multiplatform |
| খুব custom design, game-এর মতো UI, একই রকম pixel | Flutter |
| App size আর startup খুব জরুরি (কম দামের phone) | Native একটু এগিয়ে |

মাঝামাঝি একটা পথও আছে: Kotlin Multiplatform (KMP)। এতে logic শেয়ার হয়, UI native থাকে। আর Compose Multiplatform এখন iOS-এ stable, তাই চাইলে UI-ও শেয়ার করা যায়।

---

#### ২. "Native-এ আপনার আসল অভিজ্ঞতা?" — সৎ আর নির্দিষ্ট থাকুন

- নিজে কী কী করেছেন, তার একটা তালিকা আগে থেকে বানিয়ে রাখুন। যেমন: Kotlin-এ plugin বা platform channel, `AndroidManifest`, Gradle flavor, signing, R8 rule, notification channel, deep link, Play release, এমন crash যেটা শুধু Android-এ ছিল।
- প্রতিটার জন্য একটা ছোট গল্প রাখুন: **সমস্যা → আপনি কী খুঁজলেন → কী করলেন → ফল**। গল্প থাকলে কথা বিশ্বাসযোগ্য শোনায়।
- যা করেননি, সেটাও সোজাসুজি বলুন। যেমন: "Production-এ Compose screen আমি কম লিখেছি, কিন্তু declarative UI-র model আমার কাছে নতুন না — Flutter-এ এটাই রোজ করি। আর এই কয়েক সপ্তাহে আমি Compose-এ একটা পুরো app বানিয়েছি (GitHub link)।"
- শেষ কথাটা ঠিক তখনই বলুন, যখন সত্যিই বানিয়েছেন। তাই বানিয়ে রাখাই সবচেয়ে ভালো প্রস্তুতি।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি এটাকে Flutter বনাম native হিসেবে দেখি না — এটা product-এর সিদ্ধান্ত। একটা team দিয়ে দুই platform-এ একই UI দ্রুত ship করতে হলে, আর app-টা মূলত সাধারণ screen হলে, Flutter খুব ভালো।
>
> Native এগিয়ে যায় যখন product platform-এর গভীর feature-এর ওপর দাঁড়িয়ে — background location, media, widget, wearable, ভারী camera কাজ। অথবা যখন নতুন platform API প্রথম দিন থেকেই লাগে, বা আগে থেকেই শক্ত native codebase আর team আছে। Kotlin Multiplatform মাঝামাঝি একটা ভালো পথ — logic শেয়ার, UI native। আর Compose Multiplatform এখন iOS-এ stable, তাই UI শেয়ারও সম্ভব।
>
> আর Flutter আমাকে Android-এ আরও ভালো বানিয়েছে। কারণ সবচেয়ে কঠিন bug-গুলো প্রায়ই native দিকেই ছিল — lifecycle, permission, Gradle, R8, background limit।

*English:*
> I don't see it as Flutter versus native — it's a product decision. Flutter is a great fit when one team needs to ship the same UI on both platforms fast, and the app is mostly standard screens.
>
> Native wins when the product depends on deep platform features — background location, media, widgets, wearables, heavy camera work — or needs the newest platform APIs on day one, or when there's already a strong native codebase and team. Kotlin Multiplatform is an interesting middle ground — shared logic with native UI — and with Compose Multiplatform now stable on iOS, shared UI is an option there too.
>
> Flutter also made me better at Android, because many of the hardest bugs ended up on the native side: lifecycles, permissions, Gradle, R8, background limits.

**সাধারণ ভুল:**
- "Flutter খারাপ" বা "native পুরনো হয়ে গেছে" বলা। দুইটাই অপরিপক্ব শোনায়। আর interviewer-এর team হয়তো দুইটাই ব্যবহার করে।
- অভিজ্ঞতা বাড়িয়ে বলা। একটা follow-up প্রশ্নেই ধরা পড়ে যায়, আর তখন বাকি সব কথাও সন্দেহের মধ্যে পড়ে।
- নির্দিষ্ট উদাহরণ ছাড়া সাধারণ কথা বলা ("আমি native-ও জানি")। গল্প না থাকলে কথার ওজন থাকে না।

**Follow-up প্রশ্ন:** "Native Android-এ আপনার আসল অভিজ্ঞতা কতটা?"

*বাংলায়:*
> Flutter project-এ native দিকের কাজ আমি নিজেই করেছি — Kotlin-এ plugin, Gradle flavor, signing, R8 rule, Play release, আর এমন crash ঠিক করা যেটা শুধু Android-এ হতো। Production-এ Compose screen আমি কম লিখেছি, কিন্তু declarative UI আমার রোজকার কাজ। তাই এর মধ্যে Compose-এ একটা পুরো app বানিয়েছি, link দিতে পারি।

*English:*
> On my Flutter projects I owned the native side myself — Kotlin plugins, Gradle flavors, signing, R8 rules, Play releases, and fixing crashes that only happened on Android. I've written fewer Compose screens in production, but declarative UI is what I do every day, and I've built a full Compose app recently — I can share the link.

(শেষ বাক্যটা শুধু তখনই বলুন, যখন সত্যিই বানিয়েছেন। আপনার নিজের তালিকা থেকে বাকিটা বদলে নিন।)

**Follow-up প্রশ্ন:** "Native role কেন চান?"

*বাংলায়:*
> আমি platform-এর আরও গভীরে যেতে চাই। Flutter-এর কাজে সবচেয়ে মজার সমস্যাগুলো প্রায়ই native দিকে ছিল। এখন আমি ওই layer-টা পুরো নিজের হাতে নিতে চাই — performance, background কাজ, platform API — শুধু bridge বানিয়ে থেমে থাকতে চাই না।

*English:*
> I want to go deeper into the platform. In Flutter work, many of the most interesting problems were on the native side, and I want to own that layer fully — performance, background work, platform APIs — not only bridge to it.

[উপরে ফিরুন](#toc)

---

### <a id="q63"></a>Q63. Live coding round: পুরো সমাধান

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** সবচেয়ে সাধারণ কাজ: "একটা API থেকে list আনুন, দেখান, loading আর error সামলান, item-এ click করলে detail।" ৪৫–৬০ মিনিটে interviewer তিনটা জিনিস দেখে। আপনি কাঠামো ঠিক রাখেন কি না (ViewModel, state, repository)। Loading, error, empty — সব অবস্থা ভাবেন কি না। আর **জোরে জোরে চিন্তা** করেন কি না। সব নিখুঁত করার দরকার নেই — আগে কাজ করা সহজ version, তারপর উন্নতি। Flutter-এ যেমন repository + Cubit/Bloc + stateless widget, এখানে কাঠামোটা একই।

---

#### প্রথম পাঁচ মিনিট — scope ঠিক করুন

Code লেখার আগে কাজটা নিজের ভাষায় আবার বলুন। এতে ভুল বোঝাবুঝি শুরুতেই ধরা পড়ে। আর interviewer বুঝতে পারেন আপনি কোন পথে যাচ্ছেন, দরকার হলে আগেই থামাতে পারেন।

**সময় ভাগ (৪৫ মিনিট):**
1. ০–৫ মিনিট: প্রশ্ন জিজ্ঞেস, scope ঠিক করা, plan বলা।
2. ৫–১৫: Model + API + repository।
3. ১৫–২৫: ViewModel + UiState।
4. ২৫–৩৮: Screen (loading, error, empty, list)।
5. ৩৮–৪৫: একটা test, আর "সময় পেলে কী করতাম" বলা।

---

#### পুরো code

একটা file-এ রাখার মতো ছোট, কিন্তু layer আলাদা। পড়ার সময় কয়েকটা সিদ্ধান্ত খেয়াল করুন:
- DTO আর domain model আলাদা। API বদলালে শুধু `toDomain()` বদলায়, UI না।
- Repository `Result` ফেরত দেয়, তাই ViewModel-এ try/catch লাগে না।
- `CancellationException` আবার throw করা হয়েছে। এটা গিলে ফেললে coroutine cancel হওয়াটা ভেঙে যায়।
- `UsersUiState` একটা sealed interface — একসাথে শুধু একটা state সম্ভব, আর `when` exhaustive ([Q2](#q2))।
- Screen দুই ভাগে: `UsersRoute` ViewModel-এর সাথে কথা বলে, `UsersScreen` stateless। Stateless অংশ preview আর test করা সহজ।

```kotlin
// ---------- Model + API ----------
@Serializable
data class UserDto(val id: Int, val name: String, val email: String)

data class User(val id: Int, val name: String, val email: String)

fun UserDto.toDomain() = User(id, name, email)

interface UserApi {
    @GET("users")
    suspend fun users(): List<UserDto>
}

// ---------- Repository ----------
interface UserRepository {
    suspend fun users(): Result<List<User>>
}

class DefaultUserRepository @Inject constructor(private val api: UserApi) : UserRepository {
    override suspend fun users(): Result<List<User>> = try {
        Result.success(api.users().map { it.toDomain() })
    } catch (e: CancellationException) {
        throw e
    } catch (e: Exception) {
        Result.failure(e)
    }
}

// ---------- ViewModel ----------
sealed interface UsersUiState {
    data object Loading : UsersUiState
    data object Empty : UsersUiState
    data class Success(val users: List<User>) : UsersUiState
    data class Error(val message: String) : UsersUiState
}

@HiltViewModel
class UsersViewModel @Inject constructor(private val repo: UserRepository) : ViewModel() {

    private val _state = MutableStateFlow<UsersUiState>(UsersUiState.Loading)
    val state: StateFlow<UsersUiState> = _state.asStateFlow()

    init { load() }

    fun retry() = load()

    private fun load() {
        _state.value = UsersUiState.Loading
        viewModelScope.launch {
            _state.value = repo.users().fold(
                onSuccess = { if (it.isEmpty()) UsersUiState.Empty else UsersUiState.Success(it) },
                onFailure = { UsersUiState.Error("লোড করা যায়নি। আবার চেষ্টা করুন।") },
            )
        }
    }
}

// ---------- UI ----------
@Composable
fun UsersRoute(onUserClick: (Int) -> Unit, viewModel: UsersViewModel = hiltViewModel()) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    UsersScreen(state = state, onRetry = viewModel::retry, onUserClick = onUserClick)
}

@Composable
fun UsersScreen(state: UsersUiState, onRetry: () -> Unit, onUserClick: (Int) -> Unit) {
    when (state) {
        UsersUiState.Loading -> Box(Modifier.fillMaxSize(), Alignment.Center) {
            CircularProgressIndicator()
        }
        UsersUiState.Empty -> Box(Modifier.fillMaxSize(), Alignment.Center) {
            Text("কোনো user নেই")
        }
        is UsersUiState.Error -> Column(
            Modifier.fillMaxSize(),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Text(state.message)
            Button(onClick = onRetry) { Text("Retry") }
        }
        is UsersUiState.Success -> LazyColumn {
            items(state.users, key = { it.id }) { user ->
                ListItem(
                    headlineContent = { Text(user.name) },
                    supportingContent = { Text(user.email) },
                    modifier = Modifier.clickable { onUserClick(user.id) },
                )
            }
        }
    }
}

// ---------- Test ----------
class UsersViewModelTest {
    @get:Rule val mainRule = MainDispatcherRule()

    @Test
    fun `an empty response shows the empty state`() = runTest {
        val vm = UsersViewModel(FakeUserRepository(Result.success(emptyList())))
        assertEquals(UsersUiState.Empty, vm.state.value)
    }

    @Test
    fun `a failure shows an error, and retry loads again`() = runTest {
        val repo = FakeUserRepository(Result.failure(IOException()))
        val vm = UsersViewModel(repo)
        assertTrue(vm.state.value is UsersUiState.Error)

        repo.result = Result.success(listOf(User(1, "Rahim", "r@x.com")))
        vm.retry()

        assertEquals(UsersUiState.Success(listOf(User(1, "Rahim", "r@x.com"))), vm.state.value)
    }
}

class FakeUserRepository(var result: Result<List<User>>) : UserRepository {
    override suspend fun users() = result
}
```

Test নিয়ে একটা কথা: এখানে `MainDispatcherRule` ([Q56](#q56)) `UnconfinedTestDispatcher` ব্যবহার করে। তাই `init`-এর coroutine সাথে সাথে শেষ হয়, আর `state.value` সরাসরি পড়া যায়। Fake repository-তে `result` একটা `var`, তাই একই test-এ আগে failure, পরে success দেখানো যায়।

---

#### শেষে নিজে থেকে যা বলবেন ("সময় পেলে")

- Room cache দিয়ে offline-first ([Q41](#q41))।
- Pull-to-refresh, যেখানে refresh fail করলে পুরনো list থাকে।
- Error-এর ধরন অনুযায়ী message (internet নেই vs server error) ([Q39](#q39))।
- Rotation-এ আবার load হয় না, কারণ load হয় `init`-এ, আর ViewModel rotation-এ বেঁচে থাকে। এটা interviewer জিজ্ঞেস করার আগেই নিজে বলুন।
- UI test আর screenshot test।

---

#### Live coding-এ senior signal

- কিছু লেখার আগে প্রশ্ন করুন।
- Stateless screen আলাদা রাখুন, আর কারণটাও বলুন: "এতে preview আর test সহজ হয়"।
- Error আর empty state ভুলবেন না। Junior-রা প্রায়ই এগুলো বাদ দেয়।
- আটকে গেলে চুপ থাকবেন না। বলুন: "I don't remember the exact API, I'd check the docs — here's the idea."

---

#### DSA round — Kotlin-এর দরকারি জিনিস

কিছু company আলাদা DSA round রাখে। তখন Kotlin-এর এই জিনিসগুলো হাতের কাছে থাকলে সময় বাঁচে।

| কাজ | Kotlin |
|---|---|
| Stack / Queue | `ArrayDeque<Int>()` — `addLast`, `removeLast`, `removeFirst` |
| Heap | `PriorityQueue<Int>(compareByDescending { it })` |
| Frequency map | `map[key] = map.getOrDefault(key, 0) + 1` অথবা `groupingBy { it }.eachCount()` |
| Default list-এর map | `map.getOrPut(key) { mutableListOf() }.add(x)` |
| Sort | `sortedBy { it.age }`, `sortedWith(compareBy({ it.a }, { it.b }))` |
| Primitive array | `IntArray(n)`, `Array(n) { IntArray(m) }` (2D grid) |
| String | `buildString {}`, `s.toCharArray()`, `c - 'a'` (index) |
| Pair destructure | `val (a, b) = pair` |
| Infinity | `Int.MAX_VALUE`, overflow-এর জন্য `Long` |

DSA-র পুরো প্রস্তুতি repo-তে আছে: [cs-fundamentals/dsa](../../cs-fundamentals/dsa/) আর [Cracking the Coding Interview (বাংলা)](../cracking-the-coding-interview/README.md)।

**Behavioral round:** [Flutter guide-এর Section 22](../software-engineer-flutter-bn/section-22-leadership-behavioral-bn.md) — platform বদলালেও প্রশ্ন একই।

---

**Interview-এ এভাবে বলুন (শুরুতে):**

*বাংলায়:*
> শুরু করার আগে scope-টা একবার মিলিয়ে নিই: এই endpoint থেকে list দেখাব, সাথে loading, retry-সহ error, আর empty state। Item-এ tap করলে detail খুলবে।
>
> প্রথমে আমি সহজ রাখব — একটা repository, একটা ViewModel যেটা একটাই UiState দেয়, আর একটা stateless screen। সময় থাকলে pull-to-refresh, একটা test আর caching যোগ করব।
>
> কাজ করতে করতে আমি আমার সিদ্ধান্তগুলো জোরে বলব। আপনি অন্য কিছুতে focus চাইলে থামিয়ে দেবেন।

*English:*
> Before I start, let me confirm the scope: show a list from this endpoint, with loading, error with retry, and empty states, and open a detail on tap.
>
> I'll keep it simple first — a repository, a ViewModel exposing one UiState, and a stateless screen — and if we have time, I'll add pull-to-refresh, a test, and caching.
>
> I'll talk through my decisions as I go; please stop me if you'd like me to focus on something else.

**সাধারণ ভুল:**
- Scope না মিলিয়েই code শুরু করা। পরে দেখা যায় interviewer অন্য কিছু চেয়েছিলেন, আর সময় শেষ।
- শুধু success path বানানো। Error আর empty state না থাকলে সেটা junior signal।
- প্রথম থেকেই সব নিখুঁত করতে চাওয়া (cache, paging, animation)। ৪৫ মিনিটে কাজ করা কিছু না দেখাতে পারলে বাকিটার দাম থাকে না।
- আটকে গিয়ে চুপ হয়ে যাওয়া। Interviewer আপনার চিন্তা দেখতে চান। চুপ থাকলে তিনি কিছুই দেখেন না।

**Follow-up প্রশ্ন:** "Screen rotate করলে কী হবে? আবার network call হবে?"

*বাংলায়:*
> না। Load হয় ViewModel-এর `init`-এ, আর ViewModel rotation-এ বেঁচে থাকে। নতুন Activity শুধু একই `StateFlow` আবার collect করে, আর শেষ state সাথে সাথে পায়।

*English:*
> No. The load runs in the ViewModel's `init`, and the ViewModel survives rotation. The new Activity just collects the same `StateFlow` again and gets the latest state right away.

[উপরে ফিরুন](#toc)

---

# N. আরও যা senior interview-এ আসে

### <a id="q64"></a>Q64. RecyclerView কীভাবে কাজ করে? ListAdapter আর DiffUtil

**কত ঘন ঘন:** Very common (native round-এ) · **কঠিনতা:** Medium

**সংক্ষেপে:** RecyclerView screen ভরার মতো View বানায়, সাথে অল্প কিছু বাড়তি। কোনো item screen থেকে বের হলে তার **ViewHolder** একটা pool-এ যায়। নতুন item এলে সেটাই আবার ব্যবহার হয়। **ListAdapter + DiffUtil** পুরনো আর নতুন list তুলনা করে শুধু যা বদলেছে সেটুকু update করে — background thread-এ, animation-সহ। Flutter-এর `ListView.builder` যেমন শুধু দেখা widget বানায়, ধারণাটা কাছাকাছি।

---

#### সমস্যাটা কোথায়

১০,০০০ item-এর list-এ ১০,০০০ View বানালে memory শেষ, আর scroll আটকে যায়। কারণ View inflate করা দামি। তাই RecyclerView কয়েকটা View বানিয়ে সেগুলো বারবার ব্যবহার করে। শুধু data বদলায়।

---

#### দুইটা callback, দুই রকম খরচ

- **`onCreateViewHolder`** — layout inflate করে। দামি, কিন্তু কম call হয়।
- **`onBindViewHolder`** — View-এ data বসায়। Scroll-এর সময় প্রায়ই call হয়। তাই এটা হালকা রাখতে হবে: কোনো allocation না, কোনো formatting না। Formatting-এর কাজ ViewModel-এ করে রাখুন।

---

#### DiffUtil — কী বদলেছে, সেটা হিসাব করা

`notifyDataSetChanged()` সব item আবার bind করে, আর কোনো animation হয় না। কারণ RecyclerView জানে না আসলে কী বদলেছে। DiffUtil এই প্রশ্নের উত্তর দেয় দুই ধাপে:
- `areItemsTheSame` — এটা কি একই item? সাধারণত id দিয়ে।
- `areContentsTheSame` — একই item, কিন্তু ভেতরের data বদলেছে কি?

আর `getChangePayload` দিয়ে বলা যায় ঠিক কোন অংশ বদলেছে। তখন পুরো row আবার bind না করে শুধু সেই অংশ update করা যায়, যেমন শুধু like count।

```kotlin
class ArticleAdapter(
    private val onClick: (Article) -> Unit,
) : ListAdapter<Article, ArticleAdapter.Holder>(Diff) {

    object Diff : DiffUtil.ItemCallback<Article>() {
        override fun areItemsTheSame(old: Article, new: Article) = old.id == new.id        // একই item?
        override fun areContentsTheSame(old: Article, new: Article) = old == new           // ভেতরে বদলেছে?
        override fun getChangePayload(old: Article, new: Article) =
            if (old.copy(likes = new.likes) == new) LIKES_CHANGED else null                // শুধু like বদলেছে
    }

    class Holder(val binding: ItemArticleBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val binding = ItemArticleBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return Holder(binding).also { holder ->
            binding.root.setOnClickListener {                       // listener এখানে একবার, bind-এ না
                holder.bindingAdapterPosition.takeIf { it != RecyclerView.NO_POSITION }
                    ?.let { onClick(getItem(it)) }
            }
        }
    }

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val item = getItem(position)
        holder.binding.title.text = item.title
        holder.binding.likes.text = item.likes.toString()
    }

    override fun onBindViewHolder(holder: Holder, position: Int, payloads: List<Any>) {
        if (LIKES_CHANGED in payloads) holder.binding.likes.text = getItem(position).likes.toString()
        else super.onBindViewHolder(holder, position, payloads)    // পুরো bind
    }

    private companion object { const val LIKES_CHANGED = "likes" }
}

// ব্যবহার
adapter.submitList(newList)     // DiffUtil background-এ তুলনা করে
```

---

#### Senior-রা যা খেয়াল রাখে

- **Click listener `onCreateViewHolder`-এ।** তাহলে প্রতিবার bind-এ নতুন lambda তৈরি হয় না। Position নিন click-এর সময় `bindingAdapterPosition` থেকে, কারণ bind-এর পরে item-এর position বদলাতে পারে।
- **Nested RecyclerView** (vertical-এর ভেতরে horizontal): সব inner list-এ একটাই `RecycledViewPool` দিন। তাহলে এক row-এর View অন্য row-তে reuse হয়। আর `LinearLayoutManager.initialPrefetchItemCount` ঠিক করুন, যাতে inner list আগে থেকেই কয়েকটা item তৈরি রাখে।
- **`setHasFixedSize(true)`** — item বদলালেও যদি RecyclerView-এর নিজের size না বদলায়, তাহলে পুরো layout আবার করতে হয় না।
- **Multiple view type:** `getItemViewType()`। প্রতিটা type-এর আলাদা pool থাকে, তাই এক type-এর View অন্য type-এ যায় না।
- **`ConcatAdapter`** — header, list আর footer আলাদা adapter রেখে জোড়া দেওয়া যায়।

**Compose-এর সাথে মিল:** `LazyColumn`-এর `key` = DiffUtil-এর `areItemsTheSame`। `contentType` = `getItemViewType` (একই type-এর composition reuse হয়)।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> RecyclerView screen ভরার মতো View বানায়, সাথে অল্প buffer। Item scroll করে বের হলে তার ViewHolder recycled pool-এ যায়, আর পরের item-এর জন্য আবার bind হয়। তাই `onCreateViewHolder` দামি কিন্তু কম চলে, আর `onBindViewHolder` হালকা রাখতে হয় — কোনো allocation না, এমন কোনো formatting না যেটা ViewModel-এ করা যেত।
>
> আমি `notifyDataSetChanged`-এর বদলে ListAdapter আর DiffUtil callback নিই। এটা background thread-এ সবচেয়ে কম পরিবর্তনগুলো হিসাব করে, আর animation-ও ঠিক থাকে।
>
> Nested horizontal list-এ আমি একটা `RecycledViewPool` শেয়ার করি আর initial prefetch দিই। আর শুধু একটা field বদলালে, যেমন like count, তখন payload ব্যবহার করি।

*English:*
> RecyclerView only creates enough views to fill the screen plus a small buffer; when an item scrolls off, its ViewHolder goes into a recycled pool and gets rebound for the next item. So `onCreateViewHolder` is the expensive, rare call and `onBindViewHolder` must stay cheap — no allocations, no formatting work that could be done in the ViewModel.
>
> I use ListAdapter with a DiffUtil callback instead of `notifyDataSetChanged`. It computes the minimal set of changes on a background thread and gives correct animations.
>
> For nested horizontal lists I share a RecycledViewPool and set initial prefetch, and I use payloads when only one field changes, like a like count.

**সাধারণ ভুল:**
- `notifyDataSetChanged()` ডাকা। সব item আবার bind হয়, animation হারায়, আর বড় list-এ scroll আটকায়।
- **একই list object আবার `submitList`-এ দেওয়া।** List mutate করে একই reference দিলে DiffUtil কোনো পার্থক্য দেখে না, তাই UI বদলায় না। সবসময় নতুন list দিন।
- `onBindViewHolder`-এ click listener বসানো। প্রতিবার bind-এ নতুন lambda তৈরি হয়। আর bind-এর সময়ের `position` ধরে রাখলে পরে ভুল item click হতে পারে।

**Follow-up প্রশ্ন:** "Payload কেন লাগে?"

*বাংলায়:*
> Payload না দিলে, item-এর content বদলালে পুরো row আবার bind হয়, আর একটা change animation চলে। শুধু like count বদলালে সেটা অপচয়, আর row একটু blink-ও করতে পারে। Payload দিয়ে আমি বলে দিই কী বদলেছে, তখন শুধু সেই TextView update হয়।

*English:*
> Without a payload, a content change rebinds the whole row and runs a change animation. If only the like count changed, that's wasted work and the row can flicker. With a payload I say exactly what changed, so only that TextView updates.

[উপরে ফিরুন](#toc)

---

### <a id="q65"></a>Q65. Shared mutable state, Mutex আর Flow backpressure

**কত ঘন ঘন:** Common · **কঠিনতা:** Hard

**সংক্ষেপে:** `Dispatchers.Default` বা `IO`-তে অনেক coroutine একসাথে বিভিন্ন thread-এ চলে। তাই একই variable-এ দুইজন লিখলে **race condition** হয় — ফল নির্ভর করে কে আগে লিখল তার ওপর। **Backpressure** আলাদা সমস্যা: producer এত দ্রুত value দিচ্ছে যে collector তাল রাখতে পারছে না। Dart-এর main isolate single-threaded, তাই Flutter-এ race প্রায় দেখাই যায় না। Kotlin-এ এটা আসল সমস্যা।

---

#### সমস্যাটা — race condition

```kotlin
var counter = 0
coroutineScope {
    repeat(1_000) { launch(Dispatchers.Default) { counter++ } }   // read-modify-write — atomic না
}
println(counter)   // প্রায়ই ১০০০-এর কম
```

`counter++` আসলে তিনটা ধাপ: পড়া, এক যোগ করা, লেখা। দুইটা thread একসাথে একই পুরনো value পড়লে, দুইজনই একই নতুন value লেখে। একটা যোগ হারিয়ে যায়।

---

#### চারটা সমাধান, পছন্দের ক্রমে

1. **State share না করা।** State এক thread-এ রাখুন — Main, বা `limitedParallelism(1)` দিয়ে dispatcher-এর একটা single-threaded view। Lock-ই লাগে না।
2. **`Mutex`।** `synchronized`-এর মতো, কিন্তু thread block করে না, suspend করে। তাই ভেতরে suspend call রাখা যায়।
3. **Atomic জিনিস।** একটা value হলে `AtomicInteger`, `MutableStateFlow.update {}` যথেষ্ট।
4. **`synchronized`।** শুধু ছোট, non-suspend অংশে।

---

#### Mutex দিয়ে token একবারই load

দশটা request একসাথে token চাইলে, Mutex না থাকলে দশবার network call হতে পারে। Mutex থাকলে প্রথমজন load করে, বাকিরা অপেক্ষা করে আর cache থেকে পায়।

```kotlin
class TokenCache @Inject constructor(private val api: AuthApi) {
    private val mutex = Mutex()
    private var cached: Token? = null

    suspend fun token(): Token = mutex.withLock {
        cached?.takeIf { !it.isExpired() } ?: api.fetchToken().also { cached = it }
    }
}
```

`synchronized` এখানে চলবে না — এর ভেতরে `suspend` call (`api.fetchToken()`) দেওয়া যায় না।

একটা ফাঁদ: Kotlin-এর `Mutex` **reentrant না**। মানে একই coroutine lock ধরে থাকা অবস্থায় আবার `withLock` ডাকলে, সে নিজের জন্যই অপেক্ষা করে — deadlock।

**কোনটা কখন:**

| Tool | কখন |
|---|---|
| Thread confinement (Main / `limitedParallelism(1)`) | সবচেয়ে সহজ, lock নেই |
| `Mutex` | ভেতরে suspend call আছে |
| `AtomicInteger`, `AtomicReference`, `StateFlow.update {}` | একটা value |
| `synchronized` / `ReentrantLock` | ছোট, non-suspend অংশ, Java code-এর সাথে |
| `ConcurrentHashMap` | অনেক thread থেকে map |

---

#### Backpressure — producer দ্রুত, collector ধীর

Flow default-এ নিরাপদ: collector কাজ শেষ না করা পর্যন্ত producer অপেক্ষা করে। কিন্তু সবসময় এটা চাই না। যেমন location-এ পুরনো value-এর দাম নেই, শুধু সর্বশেষটা লাগে। তখন operator দিয়ে আচরণ বদলান:

| Operator | আচরণ | কখন |
|---|---|---|
| (কিছু না) | Producer অপেক্ষা করে | Default, নিরাপদ |
| `buffer(n)` | Producer আগে এগিয়ে যায়, n পর্যন্ত জমা রাখে | হঠাৎ অনেক value (burst) |
| `conflate()` | মাঝখানেরগুলো বাদ, শুধু সর্বশেষ | Sensor, location, progress |
| `collectLatest {}` | নতুন value এলে চলতি কাজ cancel | Search result, render |
| `MutableSharedFlow(extraBufferCapacity, onBufferOverflow = DROP_OLDEST)` | Hot flow-এর buffer নিয়ন্ত্রণ | Event bus |

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> Default বা IO-তে coroutine অনেক thread-এ parallel চলে। তাই shared mutable state-কে thread-এর মতোই রক্ষা করতে হয়। আমার প্রথম পছন্দ share না করা — state এক thread-এ রাখা, অথবা `limitedParallelism(1)` দিয়ে dispatcher-এর single-threaded view।
>
> Share করতেই হলে suspend code-এর চারপাশে `Mutex` দিই। কারণ `synchronized` thread block করে, আর ভেতরে suspend করা যায় না। সাধারণ value-এর জন্য atomic বা `MutableStateFlow.update` যথেষ্ট। একটা জিনিস খেয়াল রাখি: Kotlin-এর `Mutex` reentrant না, একই coroutine-এ দুইবার lock নিলে deadlock।
>
> Backpressure-এ case দেখে বাছি: শুধু সর্বশেষ value দরকার হলে `conflate`, হঠাৎ burst-এর জন্য `buffer`, আর নতুন data এলে পুরনো কাজ অর্থহীন হলে `collectLatest`।

*English:*
> Coroutines on Default or IO run in parallel on several threads, so shared mutable state needs protection just like with threads. My first choice is to avoid sharing — confine the state to one thread, or to a single-threaded view of a dispatcher with `limitedParallelism(1)`.
>
> When I must share, I use a `Mutex` around suspend code, because `synchronized` blocks the thread and you can't suspend inside it; for simple values, atomics or `MutableStateFlow.update` are enough. One detail: Kotlin's `Mutex` is not reentrant, so locking it twice in the same coroutine deadlocks.
>
> For backpressure I pick per case: `conflate` when only the latest value matters, `buffer` for bursts, and `collectLatest` when new data makes old work useless.

**সাধারণ ভুল:**
- "Coroutine তো হালকা, তাই race হয় না" ভাবা। Coroutine হালকা, কিন্তু Default আর IO-তে সত্যিকারের একাধিক thread-এ চলে।
- `synchronized`-এর ভেতরে suspend call রাখার চেষ্টা। এটা চলে না। আর lock ধরে thread block করলে dispatcher-এর thread-ও আটকে থাকে।
- Mutex-এর ভেতর থেকে আবার একই Mutex-এর `withLock` ডাকা। Reentrant না বলে deadlock হয়।
- `StateFlow`-এ `value = value + 1` লেখা। এটাও read-modify-write। `update {}` ব্যবহার করুন।

**Follow-up প্রশ্ন:** "`callbackFlow` আর `channelFlow`-এর পার্থক্য কী?"

*বাংলায়:*
> দুইটাই ভেতরে Channel ব্যবহার করে, তাই অন্য coroutine বা callback থেকে `send` বা `trySend` করা যায়। `callbackFlow` বানানো হয়েছে callback API-কে Flow বানানোর জন্য। এর শেষে `awaitClose { unregister() }` বাধ্যতামূলক — না দিলে listener খোলা থেকে যায়।

*English:*
> Both use a Channel inside, so you can `send` or `trySend` from other coroutines or callbacks. `callbackFlow` is meant for wrapping callback APIs, and it requires `awaitClose { unregister() }` at the end — otherwise the listener stays registered.

[উপরে ফিরুন](#toc)

---

### <a id="q66"></a>Q66. Custom View আর Compose-এ custom layout

**কত ঘন ঘন:** Common · **কঠিনতা:** Medium–Hard

**সংক্ষেপে:** View system-এ custom view তিন ধাপে কাজ করে: **`onMeasure`** (parent-এর দেওয়া `MeasureSpec` মেনে নিজের size ঠিক করা), **`onLayout`** (ViewGroup হলে child-দের জায়গা দেওয়া), **`onDraw`** (Canvas-এ আঁকা)। Compose-এ একই কাজ হয় `Layout` composable বা `Modifier.layout {}` দিয়ে, আর আঁকা হয় `Canvas` বা `drawBehind {}` দিয়ে। Flutter-এর `RenderBox` যারা লিখেছেন, তাদের কাছে ধারণাটা চেনা।

---

#### MeasureSpec — parent কী বলছে

Parent child-কে শুধু একটা সংখ্যা দেয় না, সাথে একটা mode দেয়। Mode বলে সংখ্যাটার মানে কী:

| Mode | মানে | কখন আসে |
|---|---|---|
| `EXACTLY` | ঠিক এই size | `match_parent` বা নির্দিষ্ট dp |
| `AT_MOST` | এর বেশি না | `wrap_content` |
| `UNSPECIFIED` | যত খুশি | ScrollView-এর ভেতরে |

`onMeasure`-এর শেষে অবশ্যই `setMeasuredDimension` ডাকতে হয়। `resolveSize` আপনার পছন্দের size আর MeasureSpec মিলিয়ে ঠিক উত্তরটা দেয়।

---

#### `invalidate()` না `requestLayout()`?

- **`invalidate()`** — "আবার আঁকো"। শুধু চেহারা বদলালে, যেমন রং বা progress।
- **`requestLayout()`** — "আবার measure আর layout করো"। শুধু তখন, যখন size বদলাতে পারে। এটা অনেক বেশি দামি, কারণ পুরো tree-তে measure ছড়িয়ে পড়তে পারে।

আর `onDraw` প্রতি frame-এ চলতে পারে। তাই এর ভেতরে কোনো object (`Paint`, `RectF`) তৈরি করবেন না। নিচের code-এ সেগুলো field হিসেবে একবার তৈরি হয়েছে।

```kotlin
class ProgressRing @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null,
) : View(context, attrs) {

    private val paint = Paint(Paint.ANTI_ALIAS_FLAG).apply {    // onDraw-এর বাইরে তৈরি
        style = Paint.Style.STROKE
        strokeWidth = 12f
    }
    private val bounds = RectF()

    var progress: Float = 0f
        set(value) { field = value.coerceIn(0f, 1f); invalidate() }   // শুধু আবার আঁকো

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        val desired = (48 * resources.displayMetrics.density).toInt()
        setMeasuredDimension(
            resolveSize(desired, widthMeasureSpec),
            resolveSize(desired, heightMeasureSpec),
        )
    }

    override fun onDraw(canvas: Canvas) {
        val inset = paint.strokeWidth / 2
        bounds.set(inset, inset, width - inset, height - inset)
        canvas.drawArc(bounds, -90f, 360f * progress, false, paint)
    }
}
```

---

#### Compose-এ custom layout

Compose-এ measure আর place একটা lambda-তেই হয়। প্রথমে প্রতিটা child-কে constraints দিয়ে measure করুন, তারপর `layout {}`-এর ভেতরে বসান।

```kotlin
// সব child পাশাপাশি, সবাই সমান চওড়া
@Composable
fun EqualWidthRow(modifier: Modifier = Modifier, content: @Composable () -> Unit) {
    Layout(content = content, modifier = modifier) { measurables, constraints ->
        val count = measurables.size.coerceAtLeast(1)
        val childWidth = constraints.maxWidth / count
        val placeables = measurables.map {
            it.measure(constraints.copy(minWidth = childWidth, maxWidth = childWidth))   // প্রতিটা একবার
        }
        val height = placeables.maxOfOrNull { it.height } ?: 0
        layout(constraints.maxWidth, height) {
            placeables.forEachIndexed { i, p -> p.placeRelative(x = i * childWidth, y = 0) }
        }
    }
}
```

**Compose-এর নিয়ম:** একটা child একবারের বেশি measure করা যায় না (single-pass measurement)। এই নিয়মের কারণেই গভীর tree-তেও layout দ্রুত থাকে — View system-এ বারবার measure হয়ে যেটা ধীর হতো। Child-এর size আগে জানতে হলে **intrinsic** measurement (`Modifier.height(IntrinsicSize.Min)`) বা `SubcomposeLayout` ব্যবহার করুন — কিন্তু দুইটাই দামি।

**Flutter-এর সাথে মিল:** `MeasureSpec` ≈ Flutter-এর `BoxConstraints`। Compose-এর `Layout` ≈ `CustomMultiChildLayout` বা `RenderBox.performLayout`। "Constraints go down, sizes go up" — তিন জায়গাতেই একই নিয়ম।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> View system-এ custom view চলে measure, layout, draw — এই ক্রমে। `onMeasure`-এ আমি parent-এর MeasureSpec মানি — exactly, at most, বা unspecified — আর `setMeasuredDimension` ডাকি। ViewGroup হলে `onLayout`-এ child বসাই। আর `onDraw`-এ কোনো allocation করি না, কারণ এটা প্রতি frame-এ চলতে পারে।
>
> শুধু চেহারা বদলালে `invalidate()`। Size বদলাতে পারলে তবেই `requestLayout()`, কারণ ওটা অনেক বেশি দামি।
>
> Compose-এ একই ধারণা আরও সহজ: measure আর place-এর জন্য `Modifier.layout` বা `Layout` composable — প্রতিটা child একবারই measure হয় — আর আঁকার জন্য `Canvas` বা `drawBehind`।

*English:*
> In the View system, a custom view follows measure, layout, draw. In `onMeasure` I respect the parent's MeasureSpec — exactly, at most, or unspecified — and call `setMeasuredDimension`; a ViewGroup also positions children in `onLayout`; and `onDraw` must not allocate, because it can run every frame.
>
> I call `invalidate()` when only the look changes and `requestLayout()` only when the size can change, since that's much more expensive.
>
> In Compose the same ideas are simpler: `Modifier.layout` or the `Layout` composable for measuring and placing — each child is measured only once — and `Canvas` or `drawBehind` for drawing.

**সাধারণ ভুল:**
- `onDraw`-এ `Paint` বা `RectF` তৈরি করা। প্রতি frame-এ garbage তৈরি হয়, GC চলে, animation আটকায়।
- শুধু রং বা progress বদলালেও `requestLayout()` ডাকা। দরকার ছিল শুধু redraw, কিন্তু খরচ হলো পুরো measure-layout।
- `onMeasure`-এ MeasureSpec উপেক্ষা করে নিজের size বসিয়ে দেওয়া। `match_parent` বা নির্দিষ্ট dp দিলেও view তা মানে না।
- Compose-এ একই child দুইবার measure করার চেষ্টা। এটা runtime-এ exception দেয়।

**Follow-up প্রশ্ন:** "Compose-এ child-এর size আগে জেনে তারপর layout ঠিক করতে চাইলে কী করবেন?"

*বাংলায়:*
> Single-pass নিয়মের কারণে child-কে দুইবার measure করা যায় না। তাই আগে intrinsic measurement দেখি, যেমন `Modifier.height(IntrinsicSize.Min)`। সেটায় না হলে `SubcomposeLayout`। দুইটাই দামি, তাই শুধু যেখানে সত্যিই লাগে সেখানে দিই, list item-এর ভেতরে এড়িয়ে চলি।

*English:*
> Because of single-pass measurement, I can't measure a child twice. So first I try intrinsic measurement, like `Modifier.height(IntrinsicSize.Min)`, and if that's not enough, `SubcomposeLayout`. Both are expensive, so I use them only where really needed and avoid them inside list items.

[উপরে ফিরুন](#toc)

---

### <a id="q67"></a>Q67. Notification আর FCM — গভীরে

**কত ঘন ঘন:** Very common · **কঠিনতা:** Medium

**সংক্ষেপে:** Android 8 থেকে প্রতিটা notification একটা **channel**-এ যায়। Channel-এর importance (sound, heads-up) একবার তৈরি হলে code দিয়ে আর বদলানো যায় না — user Settings থেকে বদলায়। Android 13 থেকে notification দেখাতে **`POST_NOTIFICATIONS`** runtime permission লাগে। FCM-এ message দুই রকম: notification message আর data message। কোনটা নেবেন, তার ওপর নির্ভর করে আপনার code আদৌ চলবে কি না। Flutter-এ `firebase_messaging` আর `flutter_local_notifications` দিয়ে যা করতেন, এটা তার native দিক।

---

#### Channel — user কী নিয়ন্ত্রণ করবে

Channel হলো user-এর হাতে দেওয়া একটা switch। User আলাদা করে বন্ধ করতে চাইতে পারে, এমন প্রতিটা ধরনের জন্য একটা channel দিন — যেমন chat, order, promotion। সব এক channel-এ রাখলে, promo বন্ধ করতে গিয়ে user chat-ও বন্ধ করে ফেলে।

Importance একবার তৈরির পরে code দিয়ে বদলানো যায় না। তাই শুরুতেই ঠিকটা বাছুন। একই id দিয়ে আবার `createNotificationChannels` ডাকলে সমস্যা নেই — কিছুই বদলায় না।

---

#### Permission — কখন চাইবেন

Android 13 থেকে `POST_NOTIFICATIONS` runtime permission। App খোলার সাথে সাথে চাইলে user প্রায়ই "না" বলে, কারণ সে এখনো জানে না কেন লাগবে। Context-এ চান — যেমন user-এর প্রথম order-এর পরে, "order-এর খবর জানাব?"

---

#### FCM — notification message vs data message

- **Notification message:** App background-এ থাকলে system নিজেই দেখায়। আপনার code চলে না।
- **Data message:** সবসময় `onMessageReceived`-এ আসে। Notification আপনি নিজে বানান।

Data message-এ পুরো নিয়ন্ত্রণ আপনার। আগে database-এ লিখে নিতে পারেন, তারপর deep link আর ঠিক back stack-সহ notification বানাতে পারেন।

| | Notification message | Data message |
|---|---|---|
| App background-এ | System নিজে দেখায়, `onMessageReceived` চলে না | `onMessageReceived` চলে |
| App foreground-এ | `onMessageReceived` চলে | `onMessageReceived` চলে |
| নিয়ন্ত্রণ | কম | পুরোটা আপনার |
| Force-stop করা app | আসে না | আসে না |

---

#### Code — channel, data message, deep link

```kotlin
// App শুরুতে (একাধিকবার call করলেও সমস্যা নেই)
fun createChannels(context: Context) {
    val manager = context.getSystemService(NotificationManager::class.java)
    manager.createNotificationChannels(
        listOf(
            NotificationChannel("chat", "Messages", NotificationManager.IMPORTANCE_HIGH),
            NotificationChannel("orders", "Order updates", NotificationManager.IMPORTANCE_DEFAULT),
            NotificationChannel("promo", "Offers", NotificationManager.IMPORTANCE_LOW),
        )
    )
}

class AppMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        val orderId = message.data["orderId"] ?: return
        val intent = Intent(Intent.ACTION_VIEW, "https://example.com/orders/$orderId".toUri(), this,
            MainActivity::class.java)                                   // explicit intent
        val pending = TaskStackBuilder.create(this)                     // back চাপলে app-এর home-এ ফেরে
            .addNextIntentWithParentStack(intent)
            .getPendingIntent(orderId.hashCode(), PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)

        val notification = NotificationCompat.Builder(this, "orders")
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle(message.data["title"])
            .setContentText(message.data["body"])
            .setContentIntent(pending)
            .setAutoCancel(true)
            .build()

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS) ==
            PackageManager.PERMISSION_GRANTED
        ) {
            NotificationManagerCompat.from(this).notify(orderId.hashCode(), notification)
        }
    }

    override fun onNewToken(token: String) {
        // token বদলেছে — server-এ পাঠান (WorkManager দিয়ে, যাতে fail হলে আবার চেষ্টা হয়)
    }
}
```

কয়েকটা জিনিস খেয়াল করুন:
- `TaskStackBuilder` দিয়ে parent stack তৈরি হয়। তাই notification থেকে order screen খুলে back চাপলে user app-এর home-এ ফেরে, app থেকে বের হয়ে যায় না।
- `PendingIntent`-এ `FLAG_IMMUTABLE` দেওয়া হয়েছে। Request code হিসেবে `orderId.hashCode()`, যাতে আলাদা order-এর PendingIntent একে অপরকে overwrite না করে।
- Notify করার আগে permission check — Android 13+-এ permission না থাকলে notification যায় না।

---

#### আরও যা বলার মতো

- **Grouping** — একই ধরনের অনেক notification `setGroup()` আর একটা summary দিয়ে।
- **Chat** — `MessagingStyle` আর direct reply ([Q61](#q61))।
- **Full-screen intent** (call, alarm screen) — Android 14 থেকে শুধু calling আর alarm app এর অনুমতি পায়।
- **Test:** `adb shell cmd notification` আর Firebase console-এর test message।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি notification design করি channel ধরে। User আলাদা করে নিয়ন্ত্রণ করতে চাইতে পারে এমন প্রতিটা ধরনের জন্য একটা channel — chat, order, promotion। কারণ channel তৈরির পরে তার importance code দিয়ে বদলানো যায় না। Android 13 থেকে runtime permission লাগে, তাই আমি context-এ চাই — যেমন প্রথম order-এর পরে — app শুরুতেই না।
>
> FCM-এ আমি data message পছন্দ করি। এটা সবসময় `onMessageReceived`-এ আসে, তাই আগে database-এ লিখে নিতে পারি, তারপর deep link আর ঠিক back stack-সহ notification নিজে বানাই।
>
> High priority শুধু সেই message-এ দিই, যেটা সাথে সাথে notification দেখায়। না হলে system app-এর priority কমিয়ে দিতে পারে।

*English:*
> I design notifications around channels: one per kind of message the user might want to control separately, like chats, orders and promotions, because a channel's importance can't be changed from code after it's created. Since Android 13 posting needs a runtime permission, so I ask in context — for example after the user's first order — not at startup.
>
> For FCM I prefer data messages: they always reach `onMessageReceived`, so I can write to the database first and build the notification myself, with a deep link and a proper back stack.
>
> I use high priority only for messages that show a notification right away; otherwise the system can lower the app's priority.

**সাধারণ ভুল:**
- সব notification এক channel-এ রাখা। User promo বন্ধ করতে গিয়ে জরুরি message-ও বন্ধ করে ফেলে।
- Channel-এর importance পরে code দিয়ে বদলানোর চেষ্টা। কিছুই হয় না, কারণ তৈরির পরে এটা user-এর নিয়ন্ত্রণে।
- App শুরুতেই notification permission চাওয়া। User কারণ বোঝে না, তাই "না" বলে।
- Notification message পাঠিয়ে আশা করা background-এ `onMessageReceived` চলবে। চলে না — system নিজে দেখায়।
- **High priority-র অপব্যবহার।** High priority message এলে notification না দেখালে, system পরে message-গুলো normal priority-তে নামিয়ে দিতে পারে।

**Follow-up প্রশ্ন:** "User app force-stop করলে push আসবে?"

*বাংলায়:*
> না। Force-stop করা app-এ notification message বা data message — কোনোটাই আসে না। User আবার নিজে app খুললে তবেই message আসা শুরু হয়। তাই এটা আমি bug হিসেবে ধরি না, user-এর সিদ্ধান্ত হিসেবে ধরি।

*English:*
> No. A force-stopped app gets neither notification nor data messages. Delivery starts again only after the user opens the app. So I don't treat it as a bug — it's the user's choice.

[উপরে ফিরুন](#toc)

---

### <a id="q68"></a>Q68. Accessibility

**কত ঘন ঘন:** Common (senior-এ বাড়ছে) · **কঠিনতা:** Easy–Medium

**সংক্ষেপে:** Accessibility মানে এমন app, যেটা screen reader, বড় font বা কম দৃষ্টি নিয়েও চালানো যায়। চারটা মূল নিয়ম: TalkBack যেন প্রতিটা জিনিসের মানে বলতে পারে, touch target যথেষ্ট বড়, text user-এর font scale মানে, আর অর্থ শুধু রঙের ওপর নির্ভর করে না। Compose-এ এসব `semantics` দিয়ে হয়। এই semantics tree-ই আবার UI test-এ ব্যবহার হয়।

---

#### চারটা নিয়ম, কারণসহ

1. **TalkBack যেন মানে বলতে পারে।** Icon-এ `contentDescription` দিন। শুধু সাজানোর ছবিতে `null` দিন — না হলে TalkBack অর্থহীন কথা পড়ে সময় নষ্ট করে।
2. **Touch target কমপক্ষে ৪৮dp।** আঙুল icon-এর চেয়ে বড়। ছোট target-এ ভুল জায়গায় tap হয়।
3. **Text size user-এর font scale মানবে।** `sp` ব্যবহার করুন, height fix করবেন না। Fix করলে বড় font-এ লেখা কেটে যায়।
4. **শুধু রং দিয়ে অর্থ বোঝাবেন না**, আর contrast যথেষ্ট রাখুন। Color-blind user লাল-সবুজ আলাদা করতে পারেন না।

---

#### Compose-এ কীভাবে

- `mergeDescendants = true` দিলে পুরো row একটা TalkBack focus হয়। তা না হলে user-কে icon, title, status — প্রতিটায় আলাদা swipe করতে হয়।
- `heading()` দিলে TalkBack user heading থেকে heading-এ লাফাতে পারে।
- `stateDescription` দিয়ে state আলাদা করে বলা যায়।

```kotlin
@Composable
fun OrderRow(order: Order, onClick: () -> Unit) {
    Row(
        Modifier
            .clickable(onClickLabel = "Order দেখুন", onClick = onClick)
            .semantics(mergeDescendants = true) {}        // TalkBack পুরো row একবারে পড়বে
            .padding(16.dp),
    ) {
        Icon(Icons.Default.ShoppingBag, contentDescription = null)    // সাজানো, আলাদা মানে নেই
        Column {
            Text(order.title)
            Text(
                text = order.statusLabel,
                modifier = Modifier.semantics { stateDescription = order.statusLabel },
            )
        }
    }
}

Text("Recent orders", Modifier.semantics { heading() })     // TalkBack-এ heading ধরে লাফানো যায়

IconButton(onClick = onDelete) {                             // IconButton নিজেই ৪৮dp touch target দেয়
    Icon(Icons.Default.Delete, contentDescription = "Order মুছুন")
}
```

---

#### Checklist

- সব clickable জিনিসে বোঝার মতো label। "Button" বা "Image" না।
- Custom component-এ `Modifier.minimumInteractiveComponentSize()`।
- Font scale ২০০%-এ screen ভাঙে কি না দেখুন (Android 14-এ non-linear font scaling)।
- `Role` দিন (`Role.Button`, `Role.Switch`) — TalkBack বলবে "double-tap to toggle"।
- Error message শুধু লাল রং দিয়ে না, লেখা দিয়েও।
- **Tool:** TalkBack নিজে চালিয়ে দেখা, Accessibility Scanner app, Compose test-এ semantics দিয়ে node খোঁজা, Espresso-তে `AccessibilityChecks.enable()`।

**Flutter-এর সাথে মিল:** `Semantics` widget, `MergeSemantics`, `excludeSemantics` — একই ধারণা, প্রায় একই নাম।

---

**Interview-এ এভাবে বলুন:**

*বাংলায়:*
> আমি accessibility-কে "done"-এর অংশ ধরি, পরে করার কাজ না। Compose-এ এর মানে: অর্থপূর্ণ content description, সাজানোর ছবিতে null, `mergeDescendants` দিয়ে একটা row-কে এক TalkBack focus বানানো, আর semantics দিয়ে heading আর state চিহ্নিত করা।
>
> Touch target কমপক্ষে ৪৮dp, text-এ sp, আর বড় font scale-এও layout টিকে থাকে — Android 14-এ এটা ২০০% পর্যন্ত যায়। অর্থ কখনো শুধু রঙের ওপর নির্ভর করে না।
>
> আমি TalkBack আর Accessibility Scanner দিয়ে check করি। আর Compose test একই semantics tree ব্যবহার করে, তাই ভালো accessibility থাকলে UI test লেখাও সহজ হয়।

*English:*
> I treat accessibility as part of done, not a later task. In Compose that means meaningful content descriptions, null for decorative images, merging a row into one TalkBack focus with `mergeDescendants`, and marking headings and states with semantics.
>
> Touch targets are at least 48 dp, text uses sp and layouts survive large font scales — Android 14 goes up to 200% — and meaning never depends on color alone.
>
> I check with TalkBack and the Accessibility Scanner, and because Compose tests use the same semantics tree, good accessibility also makes UI tests easier to write.

**সাধারণ ভুল:**
- সাজানোর icon-এ description দেওয়া, বা আসল icon-এ না দেওয়া। প্রথমটায় noise, দ্বিতীয়টায় TalkBack শুধু "Button" বলে।
- Text-এর container-এ fixed height। বড় font-এ লেখা কেটে যায়।
- Error শুধু লাল border দিয়ে দেখানো। Color-blind user আর TalkBack user কেউই বোঝে না কী ভুল হয়েছে।
- Accessibility-কে release-এর আগের কাজ ভাবা। তখন পুরো screen আবার বানাতে হয়।

**Follow-up প্রশ্ন:** "Accessibility আর UI test-এর সম্পর্ক কী?"

*বাংলায়:*
> Compose test আর TalkBack একই semantics tree পড়ে। তাই test-এ আমি `onNodeWithContentDescription` বা text দিয়ে node খুঁজি, ঠিক যেভাবে TalkBack খোঁজে। কোনো node test-এ খুঁজে না পেলে, সাধারণত TalkBack user-ও সেটা ঠিকমতো পায় না।

*English:*
> Compose tests and TalkBack read the same semantics tree. So in tests I find nodes by content description or text, the same way TalkBack does. If a test can't find a node, a TalkBack user usually can't either.

[উপরে ফিরুন](#toc)

---

### <a id="q69"></a>Q69. দ্রুত প্রশ্ন: Parcelable, Binder, bound service, animation, Credential Manager

**কত ঘন ঘন:** Common · **কঠিনতা:** Easy–Medium

এগুলো সাধারণত দ্রুত প্রশ্ন হিসেবে আসে। ২–৩ বাক্যে উত্তর দিন।

#### Parcelable vs Serializable

দুইটাই object-কে Bundle বা Intent-এ পাঠানোর জন্য। `Serializable` Java reflection ব্যবহার করে — ধীর, আর অনেক garbage তৈরি করে। `Parcelable` Android-এর নিজের, দ্রুত। Kotlin-এ `@Parcelize` দিলে code নিজে তৈরি হয়। তবুও Bundle-এ ছোট জিনিস (id) পাঠান ([Q19](#q19))।

*বাংলায়:*
> আমি `Parcelable` নিই, আর `@Parcelize` দিয়ে code generate করি। `Serializable` reflection চালায়, তাই ধীর আর garbage বেশি। তবে Bundle-এ আমি পুরো object না পাঠিয়ে সাধারণত শুধু id পাঠাই।

*English:*
> I use `Parcelable` with `@Parcelize`. `Serializable` uses reflection, so it's slower and creates more garbage. But in a Bundle I usually pass just an id, not the whole object.

#### Binder কী?

Android-এর IPC — মানে দুই process-এর মধ্যে কথা বলার পথ। System service (`LocationManager`, `PackageManager`) সব Binder দিয়ে অন্য process-এ call যায়। তাই main thread থেকে অনেক system call ধীর হতে পারে। একটা transaction-এর buffer প্রায় ১ MB — `TransactionTooLargeException` এখান থেকে আসে।

*বাংলায়:*
> Binder হলো Android-এর IPC। System service-এ প্রতিটা call আসলে অন্য process-এ যায়, তাই main thread-এ এগুলো ধীর হতে পারে। Transaction buffer প্রায় ১ MB, তাই Bundle বড় হলে `TransactionTooLargeException` আসে।

*English:*
> Binder is Android's IPC. Every call to a system service actually goes to another process, so these calls can be slow on the main thread. The transaction buffer is about 1 MB, which is where `TransactionTooLargeException` comes from.

#### Bound service আর AIDL

`bindService()` দিয়ে client একটা service-এর সাথে যুক্ত হয় আর method call করে। একই app-এ `Binder` subclass ফেরত দিলেই হয়। অন্য app থেকে call করতে AIDL বা `Messenger` লাগে। শেষ client unbind করলে service বন্ধ হয়।

*বাংলায়:*
> Bound service-এ client `bindService()` দিয়ে যুক্ত হয়ে সরাসরি method call করে। একই app-এ আমি শুধু একটা `Binder` subclass ফেরত দিই। অন্য app থেকে লাগলে AIDL বা `Messenger`। শেষ client unbind করলে service নিজেই বন্ধ হয়।

*English:*
> With a bound service, the client connects through `bindService()` and calls methods directly. Inside one app I just return a `Binder` subclass; across apps I need AIDL or a `Messenger`. When the last client unbinds, the service stops.

#### Compose animation

কোন API নেবেন, তা নির্ভর করে কী animate করছেন তার ওপর:
- একটা value: `animateFloatAsState` / `animateDpAsState`।
- দেখা-লুকানো: `AnimatedVisibility`।
- Content বদল: `AnimatedContent` / `Crossfade`।
- একসাথে কয়েকটা value: `updateTransition`।
- Gesture বা নিজের নিয়ন্ত্রণ: `Animatable` (coroutine থেকে)।
- List item: `Modifier.animateItem()`।

*বাংলায়:*
> আমি কাজ দেখে API বাছি। একটা value হলে `animate*AsState`, দেখা-লুকানোয় `AnimatedVisibility`, content বদলে `AnimatedContent` বা `Crossfade`। কয়েকটা value একসাথে হলে `updateTransition`। Gesture বা পুরো নিয়ন্ত্রণ লাগলে coroutine থেকে `Animatable`। আর list item-এ `Modifier.animateItem()`।

*English:*
> I pick the API by the job. One value is `animate*AsState`, show and hide is `AnimatedVisibility`, swapping content is `AnimatedContent` or `Crossfade`. Several values together is `updateTransition`. For gestures or full control I use `Animatable` from a coroutine, and for list items `Modifier.animateItem()`.

#### View animation

`ViewPropertyAnimator` (`view.animate().alpha(0f)`), `ObjectAnimator`, `MotionLayout`। পুরনো `Animation` class-এ শুধু ছবি সরে, view-এর আসল জায়গা না। মানে view সরে গেছে দেখালেও touch পুরনো জায়গাতেই ধরা পড়ে।

*বাংলায়:*
> সাধারণ কাজে `view.animate()`, মানে `ViewPropertyAnimator`। বেশি নিয়ন্ত্রণে `ObjectAnimator`, আর জটিল transition-এ `MotionLayout`। পুরনো `Animation` class এড়াই, কারণ ওতে শুধু ছবি সরে, view-এর আসল জায়গা না।

*English:*
> For simple cases I use `view.animate()`, the `ViewPropertyAnimator`; `ObjectAnimator` for more control, and `MotionLayout` for complex transitions. I avoid the old `Animation` classes, because they only move the pixels, not the view's real position.

#### Credential Manager / passkey

Password, passkey আর "Sign in with Google" একটা API-তে। Passkey phishing ঠেকায়, কারণ private key device-এ থাকে আর শুধু আসল domain-এর জন্য কাজ করে। পুরনো Smart Lock আর পুরনো Google Sign-In API-র বদলি।

*বাংলায়:*
> Credential Manager-এ password, passkey আর "Sign in with Google" — সব একটা API-তে। এটা পুরনো Smart Lock আর পুরনো Google Sign-In API-র জায়গা নিয়েছে। আমি passkey পছন্দ করি, কারণ private key device-এই থাকে আর শুধু আসল domain-এ কাজ করে, তাই phishing হয় না।

*English:*
> Credential Manager puts passwords, passkeys and "Sign in with Google" behind one API, replacing the old Smart Lock and the old Google Sign-In API. I prefer passkeys, because the private key stays on the device and only works for the real domain, so phishing doesn't work.

#### BiometricPrompt + CryptoObject

শুধু "fingerprint সফল" boolean যথেষ্ট না। কারণ rooted device-এ বা hook করে সেই boolean বদলে দেওয়া যায়। Keystore-এ `setUserAuthenticationRequired(true)` দেওয়া key-এর `Cipher` `CryptoObject` হিসেবে দিন। Biometric সফল হলে তবেই key কাজ করে ([Q54](#q54))।

*বাংলায়:*
> শুধু success callback-এর boolean-এ আমি ভরসা করি না। Keystore-এ `setUserAuthenticationRequired(true)` দিয়ে key বানাই, আর তার `Cipher` `CryptoObject` হিসেবে `BiometricPrompt`-এ দিই। তাহলে biometric সফল না হলে key আদৌ কাজ করে না।

*English:*
> I don't trust only the boolean from the success callback. I create a Keystore key with `setUserAuthenticationRequired(true)` and pass its `Cipher` to `BiometricPrompt` as a `CryptoObject`. Then the key simply doesn't work unless the biometric check succeeds.

#### App widget

এখন **Jetpack Glance** দিয়ে Compose-এর মতো code-এ widget বানানো যায়। ভেতরে এটা `RemoteViews`-এ রূপান্তর হয়, তাই সব Compose জিনিস চলে না।

*বাংলায়:*
> নতুন widget আমি Jetpack Glance দিয়ে বানাই — লেখা Compose-এর মতো। কিন্তু ভেতরে এটা `RemoteViews` হয়ে যায়, তাই সাধারণ Compose-এর সব কিছু এখানে চলে না।

*English:*
> For new widgets I use Jetpack Glance, which reads like Compose. Under the hood it becomes `RemoteViews`, so not everything from regular Compose works there.

#### Kotlin Multiplatform (KMP)

Business logic (network, database, model) Android আর iOS-এ শেয়ার করা। Ktor, SQLDelight বা Room KMP, kotlinx.serialization। UI native রাখা যায়, অথবা Compose Multiplatform দিয়ে শেয়ার করা যায়।

*বাংলায়:*
> KMP-তে network, database আর model-এর মতো business logic Android আর iOS-এ শেয়ার হয়। সাধারণ stack হলো Ktor, SQLDelight বা Room KMP, আর kotlinx.serialization। UI native রাখা যায়, অথবা Compose Multiplatform দিয়ে শেয়ার করা যায়।

*English:*
> KMP shares business logic — network, database, models — between Android and iOS. The usual stack is Ktor, SQLDelight or Room KMP, and kotlinx.serialization. The UI can stay native, or be shared with Compose Multiplatform.

#### ART, Dalvik, JIT, AOT

ART হলো Android-এর runtime। Install-এর সময় কিছু code AOT (আগে থেকে) compile হয়, চালানোর সময় JIT, আর profile দেখে পরে আরও compile হয়। Baseline Profile এই প্রক্রিয়াকে আগে থেকে তথ্য দেয় ([Q47](#q47))।

*বাংলায়:*
> ART হলো Android-এর runtime। Install-এর সময় কিছু code AOT compile হয়, চালানোর সময় JIT চলে, আর পরে profile দেখে আরও code compile হয়। Baseline Profile আগে থেকেই বলে দেয় কোন code গরম, তাই প্রথম launch থেকেই app দ্রুত।

*English:*
> ART is Android's runtime. Some code is AOT-compiled at install, JIT runs while the app is used, and later more code is compiled based on the profile. A Baseline Profile gives this process the hot code in advance, so the app is fast from the first launch.

[উপরে ফিরুন](#toc)

---

## <a id="cheatsheet"></a>Cheat Sheet — শেষ রাতের রিভিশন

**Kotlin**
- `lateinit` = `var`, বাইরে থেকে set। `lazy` = `val`, প্রথম ব্যবহারে, thread-safe।
- Sealed + `when` = exhaustive, `else` দেবেন না।
- `out` = দেয় (covariant), `in` = নেয় (contravariant)।
- `inline` = lambda object নেই, non-local return। `reified` = runtime-এ type।
- Sequence = lazy, বড় data আর আগে থামলে।

**Coroutines / Flow**
- `suspend` ≠ background। Dispatcher thread ঠিক করে।
- Repository main-safe: `withContext(injectedDispatcher)`।
- `Job`: এক child fail → সব cancel। `SupervisorJob`: আলাদা।
- `CoroutineExceptionHandler` শুধু root-এ। `CancellationException` আবার throw।
- StateFlow = state (conflated, distinct)। Event = state হিসেবে, বা Channel।
- `stateIn(WhileSubscribed(5_000))` — rotation পার হয়, background-এ থামে।
- UI: `repeatOnLifecycle(STARTED)` / `collectAsStateWithLifecycle()`।

**Android core**
- A→B: A.onPause → B.onCreate/Start/Resume → A.onStop।
- Config change: Activity নতুন, ViewModel একই।
- Process death: ViewModel যায়, `SavedStateHandle` থাকে। Test: Home → `adb shell am kill <pkg>`।
- Fragment: `viewLifecycleOwner`, `onDestroyView`-এ binding null।
- PendingIntent: default `IMMUTABLE` (direct reply ছাড়া)।
- FGS: Android 14 থেকে type + permission। Sync/upload → WorkManager।
- Main thread block ~৫ সেকেন্ড → ANR। Frame বাজেট ১৬ ms (60 Hz)।

**Compose**
- তিন phase: composition → layout → draw। দ্রুত state পরের phase-এ পড়ুন।
- Hoist state: `value` + `onValueChange`।
- `LaunchedEffect(key)` — key ঠিক দিন। Cleanup → `DisposableEffect`।
- Strong skipping default: unstable param `===` দিয়ে তুলনা।
- Lazy list-এ `key`। Performance মাপুন release build-এ।

**Architecture / Data**
- UI → (Domain) → Data। Room = source of truth। UDF।
- UseCase শুধু rule, একাধিক source, বা reuse থাকলে।
- Hilt: compile-time। বেশিরভাগ binding unscoped।
- Token refresh: `Authenticator` + `synchronized` + আলাদা client।
- Migration test করুন। `fallbackToDestructiveMigration` = data loss।
- DataStore > SharedPreferences।
- WorkManager: guaranteed, constraint, periodic ≥ ১৫ মিনিট।

**Performance / Release / Security**
- Leak → LeakCanary। Jank → Perfetto। মাপুন → Macrobenchmark।
- Startup: `Application.onCreate` হালকা + Baseline Profile।
- Size: AAB + R8 + shrinkResources।
- Release-only crash → R8 keep rule। Mapping file upload।
- Play App Signing: upload key হারালে reset করা যায়।
- Android 15+ target + native code → 16 KB page size।
- Keystore-এ key। APK-তে রাখা secret = public।
- App Links: `assetlinks.json`-এ **app signing key**-র SHA-256।

**আরও**
- RecyclerView: bind হালকা, ListAdapter + DiffUtil, সবসময় নতুন list।
- Shared state: আগে confinement, তারপর `Mutex` (suspend), atomic। `Mutex` reentrant না।
- Backpressure: `conflate` (সর্বশেষ), `buffer` (burst), `collectLatest` (পুরনো কাজ বাতিল)।
- `invalidate()` = আবার আঁকো। `requestLayout()` = আবার measure (দামি)।
- Notification channel-এর importance code দিয়ে আর বদলায় না। FCM data message = সবসময় আপনার code।
- Accessibility: label, ৪৮dp, `sp`, শুধু রং দিয়ে না।
- Target API এখন 36। Android 17 = API 37।

[উপরে ফিরুন](#toc)

---

## <a id="ask-them"></a>Interviewer-কে কী জিজ্ঞেস করবেন

শেষে প্রশ্ন করা একটা senior signal। ২–৩টা বেছে নিন:

- "How is the Android codebase structured today — modules, Compose versus Views, and where are you heading?"
- "What does your release process look like — how often, staged rollouts, and what do you watch in vitals?"
- "What's the hardest technical problem the mobile team is facing right now?"
- "How do Android and iOS — and backend — work together on API design and features?"
- "What would success look like for this role in the first six months?"

[উপরে ফিরুন](#toc)

---

## <a id="resources"></a>ভালো resource

| Resource | কী পাবেন |
|---|---|
| [developer.android.com/topic/architecture](https://developer.android.com/topic/architecture) | Google-এর official architecture guide |
| [Now in Android (GitHub)](https://github.com/android/nowinandroid) | Modularization, Compose, Hilt, Room, test — বাস্তব উদাহরণ |
| [Kotlin coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html) | Coroutine আর Flow-এর official doc |
| [Compose performance](https://developer.android.com/develop/ui/compose/performance) | Stability, phase, best practice |
| [Android versions](https://developer.android.com/about/versions) | প্রতিটা version-এর behavior change |
| [Android vitals](https://developer.android.com/topic/performance/vitals) | ANR, crash, startup metric |
| [App security best practices](https://developer.android.com/privacy-and-security/security-tips) | Platform security |

[উপরে ফিরুন](#toc)
