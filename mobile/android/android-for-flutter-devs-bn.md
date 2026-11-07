# Flutter-এর চোখে Android — শেখার গাইড (বাংলা)

> যিনি Flutter ভালো জানেন, অনেক আগে Java আর Activity দিয়ে Android করেছেন, কিন্তু Kotlin আর Jetpack Compose আসার পরে আর করেননি — তাঁর জন্য।
> এটা interview-এর প্রশ্নোত্তর না, **শেখার গাইড**। প্রতিটা জিনিস আগে Flutter-এ আপনি যেভাবে করেন সেভাবে দেখানো, তারপর Android-এ ঠিক সেই কাজটা।
> শেখা শেষ হলে অনুশীলনের জন্য আছে [Android Interview Prep](../../interviews/software-engineer-android-bn/android-interview-prep-bn.md)।

---

## <a id="preface"></a>শুরুর কথা

ধরুন আপনি বহু বছর একটা শহরে গাড়ি চালিয়েছেন। রাস্তা চেনেন, নিয়ম জানেন, কোন মোড়ে জ্যাম হয় সেটাও জানেন। এখন আপনাকে পাশের শহরে যেতে হবে। গাড়ি চালানো আপনাকে নতুন করে শিখতে হবে না। শিখতে হবে শুধু রাস্তার নাম, কোথায় কোন নিয়ম আলাদা, আর কোন গলিতে না ঢোকাই ভালো।

Flutter থেকে Android-এ আসা ঠিক এরকম। State, async, architecture, declarative UI, test — এগুলো আপনি আগে থেকেই জানেন। এই বই আপনাকে নতুন শহরের মানচিত্র দেবে। প্রতিটা নতুন নামের পাশে লেখা থাকবে, আপনার শহরে এটাকে কী বলে।

আর একটা মজার কথা: আপনি এই শহরে আগেও এসেছেন। প্রতিটা Flutter app Android-এর ভেতরেই চলে। শুধু এতদিন জানালার কাচ দিয়ে দেখেছেন। এবার দরজা খুলে ভেতরে ঢুকবেন।

---

## <a id="how-to-read"></a>কীভাবে পড়বেন

**প্রতিটা বিষয় একই ছাঁচে লেখা,** যাতে কিছুদূর পড়ার পরে চোখ নিজেই জানে কোথায় কী খুঁজতে হবে:

| অংশ | কী থাকে |
|---|---|
| **এক লাইনে** | জিনিসটা কী, এক বাক্যে |
| **Flutter-এ আপনি যেভাবে করেন** | আপনার চেনা Dart code |
| **Android-এ একই কাজ** | ঠিক সেই কাজ, Kotlin-এ |
| **কী মিলল, কী আলাদা** | পাশাপাশি তুলনা |
| **ভেতরে কীভাবে কাজ করে** | ধাপে ধাপে, যেখানে দরকার |
| **Best approach** | আজকের দিনে কোনটা নেবেন, আর কেন — একটাই উত্তর |
| **ফাঁদ** | যেখানে Flutter থেকে আসা মানুষ আটকায় |

প্রতিটা অধ্যায়ের শেষে দুইটা ছোট box: **মনে রাখুন** (তিন-চারটা মূল কথা) আর **Interview-এ এক কথায়** (বাংলা আর English)। Revision-এর দিন শুধু এই box-গুলো পড়লেই পুরো বইটা মনে পড়বে।

**পুরো বইয়ে একটাই উদাহরণ — একটা Notes app।** Note-এর list, একটা note খোলা, নতুন note লেখা, database-এ রাখা, server-এর সাথে sync। প্রতিটা অধ্যায় এই app-এর একটা অংশ। তাই নতুন উদাহরণ মাথায় নিতে হবে না। শুধু দেখবেন, Flutter-এ যে Notes app বানাতেন, Android-এ সেটা কীভাবে হয়।

**ক্রমে পড়ুন।** অধ্যায় ০ সবচেয়ে জরুরি — এটা বুঝলে বাকি সব জায়গামতো বসবে। শেষে একটা [Flutter → Android অভিধান](#dictionary) আছে, revision-এর জন্য।

> **Version নিয়ে:** লেখা নভেম্বর ২০২৬-এ, Kotlin 2.x, Compose BOM আর Android 16/17 মাথায় রেখে। Library-র নাম আর API স্থির, কিন্তু version number বদলায়। Dependency দেওয়ার সময় [developer.android.com](https://developer.android.com) থেকে সর্বশেষ version নিন। Code-এ version-এর জায়গায় `x.x` লেখা।

---

## <a id="toc"></a>সূচিপত্র

- [শুরুর কথা](#preface) · [কীভাবে পড়বেন](#how-to-read)

**অধ্যায় ০ — বড় ছবি (আগে এটা)**
- [০. Android একটা পূর্ণ framework, Flutter একটা UI toolkit](#ch0)
  - [০.১ আপনার Flutter app আসলে একটা Android app](#ch0-1) · [০.২ Android-এর স্তরগুলো](#ch0-2) · [০.৩ পুরো framework-এর মানচিত্র](#ch0-3) · [০.৪ মাথায় রাখার তিনটা বদল](#ch0-4)

**পর্ব ১ — ভাষা আর async**
- [১. Kotlin — Dart-এর পাশে](#ch1)
  - [১.১ Variable আর type](#ch1-1) · [১.২ Null safety](#ch1-2) · [১.৩ Function আর lambda](#ch1-3) · [১.৪ Class](#ch1-4) · [১.৫ Model class: data, sealed, enum](#ch1-5) · [১.৬ static, singleton, factory](#ch1-6) · [১.৭ Extension আর scope function](#ch1-7) · [১.৮ Collection](#ch1-8) · [১.৯ late, lateinit, lazy, by](#ch1-9) · [১.১০ Java-র সাথে](#ch1-10)
- [২. Async — Future আর Stream থেকে Coroutine আর Flow](#ch2)
  - [২.১ সবচেয়ে বড় পার্থক্য: thread](#ch2-1) · [২.২ Future → suspend](#ch2-2) · [২.৩ কাজ চালু করা: launch, async](#ch2-3) · [২.৪ Scope: কাজ কখন থামবে](#ch2-4) · [২.৫ Isolate → Dispatcher](#ch2-5) · [২.৬ Cancellation](#ch2-6) · [২.৭ Error handling](#ch2-7) · [২.৮ Stream → Flow](#ch2-8) · [২.৯ ValueNotifier → StateFlow](#ch2-9) · [২.১০ RxDart → Flow operator](#ch2-10) · [২.১১ Async-এর best approach এক নজরে](#ch2-11)

**পর্ব ২ — Android-এর ভিত**
- [৩. Project আর Gradle — pubspec.yaml-এর জায়গায়](#ch3)
- [৪. App-এর component: Application, Activity, Manifest, Context](#ch4)
  - [৪.১ চালু হওয়া: main() থেকে Activity](#ch4-1) · [৪.২ Manifest](#ch4-2) · [৪.৩ চারটা component](#ch4-3) · [৪.৪ Context — BuildContext না](#ch4-4) · [৪.৫ পুরনো View system — যা আপনি জানতেন](#ch4-5)
- [৫. Lifecycle, rotation আর process death](#ch5)
  - [৫.১ App lifecycle](#ch5-1) · [৫.২ Rotation-এ Activity মরে যায়](#ch5-2) · [৫.৩ State কোথায় রাখবেন](#ch5-3) · [৫.৪ Process death](#ch5-4)

**পর্ব ৩ — UI**
- [৬. Jetpack Compose — Widget-এর জায়গায় Composable](#ch6)
  - [৬.১ Widget → Composable](#ch6-1) · [৬.২ Layout](#ch6-2) · [৬.৩ Wrapper widget → Modifier](#ch6-3) · [৬.৪ ListView.builder → LazyColumn](#ch6-4) · [৬.৫ setState → mutableStateOf](#ch6-5) · [৬.৬ Lifting state up](#ch6-6) · [৬.৭ initState, dispose, StreamBuilder](#ch6-7) · [৬.৮ InheritedWidget → CompositionLocal](#ch6-8) · [৬.৯ Theme](#ch6-9) · [৬.১০ TextField](#ch6-10) · [৬.১১ Animation](#ch6-11) · [৬.১২ Hot reload নেই: Preview](#ch6-12) · [৬.১৩ Performance](#ch6-13)
- [৭. Navigation — go_router-এর জায়গায়](#ch7)

**পর্ব ৪ — Architecture আর data**
- [৮. Architecture — Cubit থেকে ViewModel, get_it থেকে Hilt](#ch8)
  - [৮.১ Layer একই থাকে](#ch8-1) · [৮.২ Cubit → ViewModel](#ch8-2) · [৮.৩ BlocBuilder → collectAsStateWithLifecycle](#ch8-3) · [৮.৪ BlocListener → one-off event](#ch8-4) · [৮.৫ get_it → Hilt](#ch8-5)
- [৯. Data — network, JSON, database, storage](#ch9)
  - [৯.১ dio → Retrofit + OkHttp](#ch9-1) · [৯.২ json_serializable → kotlinx.serialization](#ch9-2) · [৯.৩ drift / sqflite → Room](#ch9-3) · [৯.৪ shared_preferences → DataStore](#ch9-4) · [৯.৫ flutter_secure_storage → Keystore](#ch9-5) · [৯.৬ Image: cached_network_image → Coil](#ch9-6) · [৯.৭ Pagination → Paging 3](#ch9-7) · [৯.৮ সব একসাথে: offline-first repository](#ch9-8)
- [১০. Plugin-এর পেছনের Android — background, notification, permission, intent](#ch10)
  - [১০.১ workmanager → WorkManager](#ch10-1) · [১০.২ Service](#ch10-2) · [১০.৩ Notification](#ch10-3) · [১০.৪ permission_handler → Activity Result API](#ch10-4) · [১০.৫ url_launcher → Intent](#ch10-5)

**পর্ব ৫ — Quality আর release**
- [১১. Testing](#ch11)
- [১২. Flavor, R8, release](#ch12)

**শেষে**
- [১৩. শেখার পরিকল্পনা — ৪ সপ্তাহ](#ch13)
- [Flutter → Android অভিধান](#dictionary)
- [ভালো resource](#resources)

---

## <a id="ch0"></a>০. Android একটা পূর্ণ framework, Flutter একটা UI toolkit

**এক লাইনে:** Flutter শুধু UI আঁকে আর Dart চালায়। বাকি সবকিছু — app চালু হওয়া, lifecycle, permission, notification, background কাজ, database — Android-এর। Flutter-এ এগুলো আপনি plugin দিয়ে ব্যবহার করতেন। Plugin-এর ভেতরে যে Android code ছিল, সেটাই এখন আপনি নিজে লিখবেন।

এই অধ্যায়টা বুঝলে বাকি গাইড সহজ হয়ে যাবে।

### <a id="ch0-1"></a>০.১ আপনার Flutter app আসলে একটা Android app

আপনার যেকোনো Flutter project-এর `android/` folder খুলুন। ওটা একটা **পুরো Android project।** ভেতরে এই file-টা পাবেন:

```kotlin
// android/app/src/main/kotlin/com/byteonyx/notes/MainActivity.kt
class MainActivity : FlutterActivity()
```

এই এক লাইনই সব। যখন user app খোলে:

1. Android একটা process চালু করে আর `MainActivity` তৈরি করে — যেকোনো Android app-এর মতোই।
2. `FlutterActivity` একটা **FlutterEngine** চালু করে। Engine-এর ভেতরে Dart VM চলে, আর আপনার `main()` call হয়।
3. Activity পুরো screen-এ একটা surface রাখে। Flutter সেই surface-এ নিজের widget নিজে আঁকে (Skia বা Impeller দিয়ে)। Android-এর button বা text-এর কোনোটাই ব্যবহার করে না।
4. Camera, notification, file-এর মতো কিছু লাগলে Dart code **platform channel** দিয়ে Android-এর Kotlin বা Java code-কে বলে। Plugin মানে এটাই: একদিকে Dart API, অন্যদিকে Android (আর iOS) code।

```
┌─────────────────────────────── Android process ───────────────────────────────┐
│                                                                                │
│   MainActivity (FlutterActivity)                                               │
│   ┌──────────────────────────────────────┐      ┌───────────────────────────┐  │
│   │  FlutterEngine                       │      │  Plugin-এর Android code    │  │
│   │  ┌────────────────────────────────┐  │ chan │  (Kotlin / Java)          │  │
│   │  │  Dart VM: আপনার widget, Bloc,  │◄─┼──────┼─► camera, notification,   │  │
│   │  │  dio, drift ...                │  │ nel  │    WorkManager, Keystore   │  │
│   │  └────────────────────────────────┘  │      └───────────────────────────┘  │
│   │  নিজের renderer দিয়ে screen আঁকে       │                                     │
│   └──────────────────────────────────────┘                                     │
│                                                                                │
│   Android framework: lifecycle, permission, notification, process kill ...     │
└────────────────────────────────────────────────────────────────────────────────┘
```

আরও কিছু জিনিস যা আপনি Flutter-এ থেকেও আসলে Android-এরটাই ব্যবহার করতেন:

| Flutter-এ আপনি যা করতেন | আসলে কী ছিল |
|---|---|
| `android/app/src/main/AndroidManifest.xml`-এ permission লেখা | Android-এর Manifest |
| `android/app/build.gradle`-এ `minSdk`, signing, flavor | Android-এর Gradle build |
| `flutter build appbundle` | ভেতরে Gradle `bundleRelease` চালায় |
| `workmanager` plugin | Android-এর WorkManager library |
| `firebase_messaging` | Android-এর FCM SDK |
| `shared_preferences` (Android-এ) | Android-এর SharedPreferences / DataStore |
| `flutter_secure_storage` (Android-এ) | Android Keystore |
| `sqflite` | Android-এর SQLite |

**তাই আপনি শূন্য থেকে শুরু করছেন না।** Android-এর অর্ধেক জিনিস আপনি আগেই ব্যবহার করেছেন, শুধু plugin-এর আড়ালে। এখন আড়ালটা সরিয়ে দেখবেন।

পার্থক্য দুইটা জায়গায়:
- **UI:** Flutter নিজে আঁকে। Native Android-এ UI-ও Android-এর — Jetpack Compose (আগে XML View)।
- **ভাষা আর runtime:** Dart VM-এর জায়গায় Kotlin, যেটা Android-এর ART runtime-এ চলে।

[উপরে ফিরুন](#toc)

### <a id="ch0-2"></a>০.২ Android-এর স্তরগুলো

Android হলো একটা পুরো operating system আর তার উপরে app বানানোর framework। নিচ থেকে উপরে:

```
┌──────────────────────────────────────────────────────────────┐
│  আপনার app (Kotlin, Compose, ViewModel ...)                   │
├──────────────────────────────────────────────────────────────┤
│  Jetpack (AndroidX) — Google-এর library: Compose, Room,       │
│  ViewModel, Navigation, WorkManager, DataStore, Paging ...    │  ← app-এর সাথে আসে
├──────────────────────────────────────────────────────────────┤
│  Android framework (SDK) — Activity, Service, Intent,         │
│  NotificationManager, PackageManager, Context ...             │  ← phone-এ আগে থেকে থাকে
├──────────────────────────────────────────────────────────────┤
│  ART (Android Runtime) — Kotlin/Java bytecode চালায়           │
├──────────────────────────────────────────────────────────────┤
│  Native library আর HAL (camera, sensor-এর driver-এর সাথে কথা) │
├──────────────────────────────────────────────────────────────┤
│  Linux kernel — process, memory, thread, security             │
└──────────────────────────────────────────────────────────────┘
```

আপনার জন্য জরুরি দুইটা স্তর:

- **Android framework (SDK):** phone-এর Android version-এর সাথে আসে। তাই Android 14-এর phone-এ Android 14-এর API, Android 10-এর phone-এ Android 10-এর। নতুন API ব্যবহার করলে পুরনো phone-এর কথা ভাবতে হয় (`minSdk`)।
- **Jetpack (AndroidX):** Google-এর library, যেগুলো আপনার app-এর সাথে bundle হয়। তাই phone-এর version যা-ই হোক, একই আচরণ। আধুনিক Android-এর প্রায় সব কিছু এখানে: Compose, Room, ViewModel। Flutter-এ pub.dev-এর official package-গুলোর মতো ভাবুন, কিন্তু Google-এর নিজের।

**নিয়ম:** কোনো কাজের জন্য Jetpack-এ library থাকলে সেটা নিন, সরাসরি পুরনো framework API না। যেমন `NotificationCompat` (Jetpack) নিন, শুধু `Notification` না — Compat class-গুলো পুরনো Android version-এর পার্থক্য নিজে সামলায়।

[উপরে ফিরুন](#toc)

### <a id="ch0-3"></a>০.৩ পুরো framework-এর মানচিত্র

এটা গাইডের সবচেয়ে কাজের table। বাম দিকে কাজটা, মাঝে আজকের দিনে Android-এ যেটা নেবেন, ডানে Flutter-এ আপনি যেটা নিতেন।

| কাজ | Android — আজকের best choice | পুরনো Android (চিনে রাখুন) | Flutter-এ |
|---|---|---|---|
| ভাষা | Kotlin | Java | Dart |
| UI | Jetpack Compose | XML layout + View | Widget |
| List | `LazyColumn` | `RecyclerView` + Adapter | `ListView.builder` |
| Screen-এর logic আর state | `ViewModel` + `StateFlow` | `ViewModel` + `LiveData`, বা Activity-তেই সব | Cubit / Bloc / Notifier |
| Async কাজ | Coroutine (`suspend`) | `AsyncTask` (মুছে ফেলা হয়েছে), RxJava, callback | `Future`, `async`/`await` |
| Data stream | `Flow` | `LiveData`, RxJava | `Stream` |
| Navigation | Navigation Compose / Navigation 3 | একাধিক Activity, Fragment transaction | `go_router`, `Navigator` |
| DI | Hilt | Dagger, হাতে বানানো | `get_it`, `injectable`, Riverpod |
| Network | Retrofit + OkHttp | `HttpURLConnection`, Volley | `dio`, `http` |
| JSON | kotlinx.serialization | Gson | `json_serializable`, `freezed` |
| Database | Room | সরাসরি `SQLiteOpenHelper` | `drift`, `sqflite`, `isar` |
| Key-value | DataStore | SharedPreferences | `shared_preferences` |
| Secret | Keystore + Tink | `EncryptedSharedPreferences` (deprecated) | `flutter_secure_storage` |
| Image | Coil | Glide, Picasso | `cached_network_image` |
| Pagination | Paging 3 | হাতে লেখা scroll listener | `infinite_scroll_pagination` |
| Background কাজ | WorkManager | `JobScheduler`, `AlarmManager`, background Service | `workmanager` plugin |
| Notification | `NotificationCompat` + channel | | `flutter_local_notifications` |
| Push | Firebase Cloud Messaging | | `firebase_messaging` |
| Permission | Activity Result API | `onRequestPermissionsResult` | `permission_handler` |
| অন্য app খোলা | `Intent` | একই | `url_launcher`, `share_plus` |
| Build | Gradle (Kotlin DSL) + version catalog | Gradle (Groovy) | `pubspec.yaml` (+ ভেতরে Gradle) |
| Unit test | JUnit + `runTest` + Turbine | JUnit | `test`, `bloc_test` |
| UI test | Compose UI test | Espresso | `testWidgets` |

**পুরনো কলামটা কেন:** Interview-এ, আর পুরনো project-এ এগুলো দেখবেন। আপনি যখন Java-তে Android করতেন, তখন সম্ভবত `AsyncTask`, `RecyclerView`, একাধিক Activity, `SharedPreferences` ব্যবহার করেছেন। নতুন code-এ মাঝের কলাম।

[উপরে ফিরুন](#toc)

### <a id="ch0-4"></a>০.৪ মাথায় রাখার তিনটা বদল

**১. Platform এখন সরাসরি আপনার হাতে।** Flutter-এ plugin আপনার হয়ে Android-এর নিয়ম মানত। এখন আপনি নিজে মানবেন: কোন Android version-এ কোন permission লাগে, background-এ কী চালানো যায়, notification channel। কাজ একটু বেশি, কিন্তু কোনো plugin-এর bug-এর জন্য আর আটকে থাকবেন না।

**২. Main thread আটকানো যাবে না, আর thread এখন আসল।** Dart-এ সব code একটা thread-এ চলে, আর `await` thread আটকায় না। Kotlin-এ অনেকগুলো আসল thread আছে, আর তারা memory শেয়ার করে। ভারী কাজ অন্য thread-এ পাঠানো খুব সহজ। কিন্তু main thread-এ ৫ সেকেন্ডের বেশি কিছু আটকে থাকলে system "App isn't responding" (ANR) dialog দেখায়। [অধ্যায় ২](#ch2)-এ বিস্তারিত।

**৩. Screen যেকোনো সময় মরে যেতে পারে।** Flutter-এ rotation হলে widget শুধু rebuild হয়, `State` object বেঁচে থাকে। Android-এ rotation, dark mode বদল, ভাষা বদল হলে Activity পুরো destroy হয়ে নতুন তৈরি হয়। আর app background-এ থাকলে system পুরো process মেরে ফেলতে পারে। তাই প্রথম দিন থেকেই ভাবতে হয়, state কোথায় রাখবেন। [অধ্যায় ৫](#ch5)-এ বিস্তারিত।

> **মনে রাখুন**
> - আপনার প্রতিটা Flutter app একটা `FlutterActivity`-ওয়ালা Android app। Plugin মানে Android code।
> - Flutter নিজে শুধু UI আঁকে আর Dart চালায়। বাকি সব Android framework-এর।
> - Jetpack হলো app-এর সাথে আসা Google-এর library। আধুনিক Android-এর প্রায় সব এখানে।
> - তিনটা বদল: platform নিজের হাতে, আসল thread, আর screen বা process যেকোনো সময় মরতে পারে।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter একটা UI toolkit, যেটা Android-এর ভেতরে একটা Activity-তে চলে আর নিজের renderer দিয়ে আঁকে। Lifecycle, permission, background কাজ — এগুলো সবসময় Android-এরই। তাই Flutter-এ plugin-এর আড়ালে যা ব্যবহার করতাম, native-এ সেগুলো সরাসরি ব্যবহার করি।"
> - *English:* "Flutter is a UI toolkit that runs inside an Android Activity and draws with its own renderer. Lifecycle, permissions and background work always belong to Android. So in native, I use directly what plugins used to hide from me in Flutter."

[উপরে ফিরুন](#toc)

---

## <a id="ch1"></a>১. Kotlin — Dart-এর পাশে

Dart আর Kotlin যেন দুই চাচাতো ভাই। একজন Google-এর বাড়িতে বড় হয়েছে, আরেকজন JetBrains-এর। দুজনেই statically typed, দুজনেই null-safe, দুজনেই lambda আর extension ভালোবাসে। প্রথম দিনের Kotlin code পড়লে আপনার মনে হবে, "আরে, এ তো প্রায় Dart, শুধু semicolon নেই আর type পেছনে বসে।"

এই অধ্যায়ে আমরা Notes app-এর model আর ছোট ছোট helper লিখব — প্রতিটা আগে Dart-এ, তারপর Kotlin-এ।

### <a id="ch1-1"></a>১.১ Variable আর type

**এক লাইনে:** `final` হলো `val`, `var` হলো `var`, আর type নামের পরে বসে।

**Flutter-এ আপনি যেভাবে লেখেন:**

```dart
final title = 'বাজারের লিস্ট';
var count = 0;
const maxLength = 500;
String? body;
final label = count > 0 ? '$count টা note' : 'কোনো note নেই';
```

**Kotlin-এ একই কথা:**

```kotlin
val title = "বাজারের লিস্ট"
var count = 0
const val MAX_LENGTH = 500          // শুধু top-level বা object-এর ভেতরে
var body: String? = null
val label = if (count > 0) "$count টা note" else "কোনো note নেই"
```

**কী মিলল, কী আলাদা:**

| Dart | Kotlin | খেয়াল করুন |
|---|---|---|
| `final` | `val` | একবার assign |
| `var` | `var` | |
| `const` | `const val` | শুধু primitive আর `String`, আর শুধু top-level বা `object`-এ |
| `String name` | `name: String` | type পরে |
| `int`, `double`, `bool` | `Int`, `Double`, `Boolean` | বড় হাতের। `Long`, `Float`-ও আছে |
| `? :` ternary | `if ... else` | Kotlin-এ `if` নিজেই value দেয় |
| `dynamic` | নেই | কাছাকাছি `Any?`, কিন্তু ব্যবহারের আগে cast লাগে |
| `typedef` | `typealias` | |

**Kotlin-এ প্রায় সবকিছুই expression।** `if`, `when`, `try` — সবাই value ফেরত দেয়। Dart 3-এর switch expression যেমন:

```dart
final color = switch (note.priority) {
  Priority.high => Colors.red,
  Priority.low => Colors.grey,
};
```

```kotlin
val color = when (note.priority) {
    Priority.HIGH -> Color.Red
    Priority.LOW -> Color.Gray
}

val words = try { body.split(" ").size } catch (e: Exception) { 0 }
```

**ফাঁদ:** Number নিজে থেকে বদলায় না। Dart-এ `int` অনেক জায়গায় `double` হয়ে যায়। Kotlin-এ `Int` কখনো নিজে `Long` বা `Double` হয় না — `toLong()`, `toDouble()` লিখতে হয়। প্রথম সপ্তাহে বিরক্ত লাগবে, তারপর বুঝবেন কত bug আটকাচ্ছে।

**Loop:**

```kotlin
for (i in 0 until notes.size) { }           // Dart: for (var i = 0; i < notes.length; i++)
for (note in notes) { }                     // Dart: for (final note in notes)
for ((index, note) in notes.withIndex()) { }
repeat(3) { println("হ্যালো") }
```

[উপরে ফিরুন](#toc)

### <a id="ch1-2"></a>১.২ Null safety

**এক লাইনে:** Dart-এ যা শিখেছেন, প্রায় হুবহু তাই। শুধু দুইটা চিহ্নের নাম আলাদা।

**Flutter-এ:**

```dart
String? body;
final length = body?.length ?? 0;
final sure = body!.length;
```

**Kotlin-এ:**

```kotlin
var body: String? = null
val length = body?.length ?: 0       // ?? → ?:  (এর নাম Elvis operator)
val sure = body!!.length             // !  → !!
```

**Smart cast** — Dart-এর type promotion:

```kotlin
fun preview(body: String?): String {
    if (body == null) return "খালি note"
    return body.take(50)               // এখানে body আর nullable না
}
```

**কী আলাদা:**
- Smart cast কাজ করে local `val`-এ, আর এমন property-তে যেটা মাঝখানে বদলাতে পারে না। Class-এর `var` property-তে কাজ করে না, কারণ check আর ব্যবহারের মাঝে অন্য thread সেটা বদলে দিতে পারে। Dart-এ এই সমস্যা নেই, কারণ Dart-এ একটাই thread। সমাধান: আগে local-এ নিন — `val current = note ?: return`।
- **Java থেকে আসা value-র কোনো গ্যারান্টি নেই।** Java-তে `?` নেই, তাই Kotlin Java-র return value-কে `String!` ধরে, মানে "জানি না"। Android SDK-র অনেক পুরনো অংশ Java-তে লেখা। সেখান থেকে value এলে নিজে null ধরে নিন।

**Best approach:** `!!` প্রায় কখনো না। লিখতে ইচ্ছা হলে থামুন — সাধারণত model-টাই ভুল, অথবা `?:` দিয়ে একটা default দেওয়া উচিত।

[উপরে ফিরুন](#toc)

### <a id="ch1-3"></a>১.৩ Function আর lambda

**এক লাইনে:** Dart-এর মতোই, কিন্তু named argument সবার জন্য খোলা, আর শেষ lambda-কে parentheses-এর বাইরে লেখা যায়।

**Flutter-এ:**

```dart
String preview(String text, {int max = 50}) => text.length > max ? '${text.substring(0, max)}...' : text;

preview(note.body, max: 30);
notes.where((n) => n.isPinned).map((n) => n.title);
```

**Kotlin-এ:**

```kotlin
fun preview(text: String, max: Int = 50): String =
    if (text.length > max) text.take(max) + "..." else text

preview(note.body, max = 30)                       // যেকোনো parameter-কে নাম দিয়ে দেওয়া যায়
notes.filter { it.isPinned }.map { it.title }      // একটা parameter হলে নাম "it"
```

**কী আলাদা:**
- Dart-এ named parameter-এর জন্য `{}` আর `required` লাগে। Kotlin-এ সব parameter-ই call করার সময় নাম দিয়ে দেওয়া যায়। Default না থাকলেই সেটা required।
- `void` হলো `Unit`। কখনো return করে না এমন function (সবসময় throw করে) ফেরত দেয় `Nothing` — Dart-এর `Never`।

**Trailing lambda — Compose বোঝার চাবি।** শেষ parameter function হলে সেটা `()`-এর বাইরে লেখা যায়। আর সেটাই একমাত্র parameter হলে `()`-ও বাদ।

```kotlin
fun onEachNote(action: (Note) -> Unit) { notes.forEach(action) }

onEachNote({ note -> println(note.title) })   // সাধারণ
onEachNote { note -> println(note.title) }    // trailing lambda — এভাবেই লেখা হয়
```

এখন এই Compose code দেখুন:

```kotlin
Column {
    Text("Notes")
    Button(onClick = { save() }) { Text("Save") }
}
```

`Column { ... }` আসলে `Column(content = { ... })`। `Button(...) { Text("Save") }` আসলে `Button(onClick = ..., content = { Text("Save") })`। Flutter-এর `child:` আর `children:`-এর জায়গায় এটাই। এই এক নিয়ম বুঝলে Compose আর অদ্ভুত লাগবে না।

**Lambda with receiver** — block-এর ভেতরে `this` একটা নির্দিষ্ট object:

```kotlin
val text = buildString {        // ভেতরে this = StringBuilder
    append("শিরোনাম: ")
    append(note.title)
}
```

Gradle-এর `android { ... }`, Compose-এর `LazyColumn { items(...) }` — সব এই জিনিস। তাই সেখানে এমন function call করা যায়, যেগুলো বাইরে নেই।

[উপরে ফিরুন](#toc)

### <a id="ch1-4"></a>১.৪ Class

**এক লাইনে:** Constructor class-এর নামের পাশেই বসে, আর property, getter, setter মিলে এক জিনিস।

**Flutter-এ:**

```dart
class Note {
  Note({required this.id, required this.title, this.body = ''});

  final String id;
  final String title;
  final String body;

  bool get isEmpty => title.isEmpty && body.isEmpty;
}
```

**Kotlin-এ:**

```kotlin
class Note(
    val id: String,
    val title: String,
    val body: String = "",
) {
    val isEmpty: Boolean
        get() = title.isEmpty() && body.isEmpty()
}
```

Constructor, তিনটা field, default value — সব প্রথম কয়েক লাইনে। Validation লাগলে `init`:

```kotlin
class Note(val id: String, val title: String) {
    init {
        require(title.length <= 500) { "শিরোনাম বেশি লম্বা" }   // ভুল হলে IllegalArgumentException
    }
}
```

**Setter-এ logic** — `field` হলো আসল storage:

```kotlin
var title: String = ""
    set(value) { field = value.trim() }
```

**Visibility:**

| Kotlin | মানে | Dart-এ |
|---|---|---|
| `public` (default) | সবাই | সাধারণ নাম |
| `private` | এই class (top-level হলে এই file) | `_name` |
| `protected` | এই class আর subclass | নেই |
| `internal` | একই Gradle module | নেই |

**Inheritance default-এ বন্ধ।** এটা Dart থেকে আসা মানুষকে প্রথমে অবাক করে। Dart-এ যেকোনো class extend করা যায়। Kotlin-এ class default-এ `final`। Extend করতে দিতে `open` লিখতে হয়, override করার method-ও `open`:

```kotlin
open class BaseRepository { open fun refresh() {} }
class NotesRepository : BaseRepository() { override fun refresh() {} }
```

**Interface আর mixin।** Kotlin-এর interface-এ default method লেখা যায়, কিন্তু field (state) রাখা যায় না। Dart-এর `mixin`-এর মতো state-সহ behavior জুড়তে Kotlin delegation ব্যবহার করে ([১.৯](#ch1-9))।

```kotlin
interface Syncable {
    fun sync()
    fun syncLabel() = "Sync হচ্ছে..."     // default
}
```

**Best approach:** Inheritance-এর চেয়ে composition। ছোট interface আর constructor-এ dependency — আপনার clean architecture-এর অভ্যাসটাই এখানে চলবে।

[উপরে ফিরুন](#toc)

### <a id="ch1-5"></a>১.৫ Model class: `data`, `sealed`, `enum`

**এক লাইনে:** `freezed` দিয়ে যা যা বানাতেন, Kotlin-এ সেগুলো ভাষার ভেতরেই আছে।

**Flutter-এ (freezed):**

```dart
@freezed
class Note with _$Note {
  const factory Note({required String id, required String title, @Default('') String body}) = _Note;
}

final edited = note.copyWith(title: 'নতুন শিরোনাম');
note == Note(id: '1', title: 'বাজার');   // freezed-এর বানানো ==
```

**Kotlin-এ — কোনো code generation ছাড়া:**

```kotlin
data class Note(val id: String, val title: String, val body: String = "")

val edited = note.copy(title = "নতুন শিরোনাম")
note == Note(id = "1", title = "বাজার")      // content দিয়ে তুলনা
println(note)                                // Note(id=1, title=বাজার, body=)
val (id, title) = note                       // destructuring
```

`data class` নিজে `equals`, `hashCode`, `toString`, `copy` বানায় — শুধু primary constructor-এর property দিয়ে।

**ফাঁদ:** `copy()` shallow। ভেতরে `MutableList` থাকলে নতুন আর পুরনো note একই list শেয়ার করে। তাই model-এ সবসময় `val` আর read-only `List`।

**Sealed — Dart 3-এর মতোই:**

```dart
sealed class SyncResult {}
class Synced extends SyncResult { Synced(this.count); final int count; }
class SyncFailed extends SyncResult { SyncFailed(this.reason); final String reason; }

final text = switch (result) {
  Synced(:final count) => '$count টা note sync হয়েছে',
  SyncFailed(:final reason) => 'হয়নি: $reason',
};
```

```kotlin
sealed interface SyncResult {
    data class Synced(val count: Int) : SyncResult
    data class Failed(val reason: String) : SyncResult
    data object Offline : SyncResult
}

val text = when (result) {
    is SyncResult.Synced -> "${result.count} টা note sync হয়েছে"   // smart cast
    is SyncResult.Failed -> "হয়নি: ${result.reason}"
    SyncResult.Offline -> "Internet নেই"
}
```

- `when`-এ `else` দেবেন না। তাহলে নতুন case যোগ করলে compiler সব জায়গা দেখিয়ে দেবে — Dart-এর exhaustive switch-এর মতো।
- Kotlin-এ `sealed class` আর `sealed interface` দুটোই আছে। সাধারণত `sealed interface` নিন। সব case-এ common field লাগলে `sealed class`।
- Data ছাড়া case-এর জন্য `data object` — সুন্দর `toString()` দেয়।

**Enum:**

```kotlin
enum class Priority(val label: String) {
    HIGH("জরুরি"), LOW("পরে");
}

Priority.entries              // Dart: Priority.values
Priority.valueOf("HIGH")      // Dart: Priority.values.byName('high')
```

**Best approach:** সব case-এর গঠন একই → `enum`। Case-গুলো আলাদা data রাখে → `sealed interface`। Plain data → `data class`।

**`value class` — Dart-এর extension type:**

```kotlin
@JvmInline value class NoteId(val raw: String)

fun open(id: NoteId) { }      // ভুল করে UserId দিলে compile error, কিন্তু runtime-এ শুধু String
```

[উপরে ফিরুন](#toc)

### <a id="ch1-6"></a>১.৬ `static`, singleton, factory

**এক লাইনে:** Kotlin-এ `static` keyword নেই। তার জায়গায় `companion object`, `object` আর top-level function।

**Flutter-এ:**

```dart
class Note {
  static const maxTitle = 100;
  factory Note.empty() => Note(id: uuid(), title: '');
}

class Analytics {
  Analytics._();
  static final instance = Analytics._();
}
```

**Kotlin-এ:**

```kotlin
data class Note(val id: String, val title: String) {
    companion object {
        const val MAX_TITLE = 100
        fun empty() = Note(id = UUID.randomUUID().toString(), title = "")   // factory
    }
}
Note.empty()

object Analytics {                    // পুরো singleton, এক লাইনে
    fun log(event: String) { }
}
Analytics.log("note_created")
```

**Top-level function খুব সাধারণ।** Dart-এর মতোই, সবকিছু class-এ ঢোকাতে হয় না:

```kotlin
// NoteFormat.kt
fun formatDate(millis: Long): String = ...
```

**Best approach:** নিজে `object` singleton কম বানান। Repository বা service singleton লাগলে Hilt-কে `@Singleton` দিয়ে বানাতে দিন ([৮.৫](#ch8-5)) — তাহলে test-এ বদলানো যায়।

[উপরে ফিরুন](#toc)

### <a id="ch1-7"></a>১.৭ Extension আর scope function

**এক লাইনে:** Extension Dart-এর মতোই। Scope function হলো Dart-এর cascade (`..`)-এর বড় পরিবার।

**Flutter-এ:**

```dart
extension NoteX on Note {
  String get preview => body.length > 50 ? '${body.substring(0, 50)}...' : body;
}

final paint = Paint()
  ..color = Colors.red
  ..strokeWidth = 2;
```

**Kotlin-এ:**

```kotlin
val Note.preview: String
    get() = if (body.length > 50) body.take(50) + "..." else body

fun Note.isOlderThan(days: Int): Boolean = ...

val paint = Paint().apply {          // Dart-এর .. cascade
    color = android.graphics.Color.RED
    strokeWidth = 2f
}
```

Dart-এর মতোই extension static ভাবে resolve হয়, আর class-এর private জিনিস দেখতে পায় না।

**পাঁচটা scope function — দুইটা প্রশ্নে মনে রাখুন:**
1. Block-এর ভেতরে object-কে কী নামে পাই — `this` না `it`?
2. Block কী ফেরত দেয় — object নিজে, না lambda-র ফল?

| Function | ভেতরে | ফেরত | কখন |
|---|---|---|---|
| `apply` | `this` | object | বানিয়ে configure করা — cascade |
| `also` | `it` | object | পাশের কাজ: log, check |
| `let` | `it` | ফল | nullable-এর উপর কাজ |
| `run` | `this` | ফল | object-এর উপর কয়েক কাজ করে একটা ফল |
| `with` | `this` | ফল | `run`-এর মতো, extension না |

```kotlin
note.body?.let { body -> showPreview(body) }          // Dart: if (note.body case final body?) ...

val saved = repository.save(note)
    .also { Log.d("Notes", "saved ${it.id}") }
```

**ফাঁদ:** একটার ভেতরে আরেকটা scope function দেবেন না। দুই স্তর হলেই `this` আর `it` গুলিয়ে যায়। তখন সাধারণ variable নিন।

[উপরে ফিরুন](#toc)

### <a id="ch1-8"></a>১.৮ Collection

**এক লাইনে:** Operator প্রায় একই। কিন্তু Kotlin-এ "পড়া যায়" আর "বদলানো যায়" দুইটা আলাদা type।

**Flutter-এ:**

```dart
final pinned = notes.where((n) => n.isPinned).toList();
final titles = notes.map((n) => n.title).toList();
final byDay = groupBy(notes, (Note n) => n.day);          // package:collection
notes.add(newNote);                                       // List সবসময় বদলানো যায়
```

**Kotlin-এ:**

```kotlin
val pinned = notes.filter { it.isPinned }
val titles = notes.map { it.title }
val byDay = notes.groupBy { it.day }                       // built-in

val notes: List<Note> = listOf()                           // read-only — add() নেই
val draft: MutableList<Note> = mutableListOf()             // বদলানো যায়
draft += newNote
```

| Dart | Kotlin |
|---|---|
| `where` | `filter` |
| `expand` | `flatMap` |
| `firstWhere(orElse:)` | `firstOrNull { }` |
| `every` | `all` |
| `fold`, `reduce`, `any`, `map` | একই নাম |
| `package:collection`-এর `groupBy` | `groupBy` (built-in) |
| (নেই) | `associateBy`, `partition`, `chunked`, `sumOf`, `maxByOrNull`, `sortedByDescending` |

```kotlin
val byId = notes.associateBy { it.id }                     // Map<String, Note>
val (pinned, others) = notes.partition { it.isPinned }
val latest = notes.maxByOrNull { it.updatedAt }
```

**Lazy না eager:** Dart-এর `where`/`map` lazy — শেষে `toList()` করলে তবে চলে। Kotlin-এর `List`-এর `filter`/`map` সাথে সাথে নতুন list বানায়। Dart-এর মতো lazy চাইলে `asSequence()`:

```kotlin
val firstTen = hugeList.asSequence().filter { it.isPinned }.map { it.title }.take(10).toList()
```

**Best approach:** বাইরে সবসময় `List` দিন, ভেতরে দরকার হলে `MutableList`। ছোট list-এ সাধারণ operator, অনেক বড় data বা লম্বা chain হলে `Sequence`।

[উপরে ফিরুন](#toc)

### <a id="ch1-9"></a>১.৯ `late`, `lateinit`, `lazy`, `by`

**এক লাইনে:** Dart-এর `late`-এর দুইটা রূপ Kotlin-এ আলাদা দুইটা জিনিস: `lateinit` আর `lazy`।

| Dart | Kotlin | কী হয় |
|---|---|---|
| `late Database db;` | `lateinit var db: Database` | আপনি পরে assign করবেন। আগে পড়লে exception। বারবার assign করা যায়। |
| `late final formatter = DateFormat('dd MMM');` | `val formatter by lazy { DateTimeFormatter.ofPattern("dd MMM") }` | প্রথম পড়ার সময় একবার তৈরি, তারপর সেটাই। বদলানো যায় না। |

```kotlin
class NotesActivity : ComponentActivity() {
    @Inject lateinit var analytics: Analytics              // Hilt পরে বসাবে

    private val formatter by lazy { DateTimeFormatter.ofPattern("dd MMM yyyy") }
}
```

- `lateinit` শুধু `var`-এ, আর `Int`/`Boolean`-এ চলে না। কারণ ভেতরে "এখনো set হয়নি" বোঝাতে null রাখা হয়, আর JVM-এর primitive null রাখতে পারে না।
- `lazy` default-এ thread-safe — দুই thread একসাথে প্রথমবার পড়লেও block একবারই চলে।

**`by` — delegation, Android-এ সব জায়গায়।** `by` মানে "এই property-র কাজ ওকে দিয়ে দিলাম":

```kotlin
val viewModel: NotesViewModel by viewModels()            // প্রথম access-এ ViewModel
var title by mutableStateOf("")                          // Compose: পড়া/লেখা state-এ যায়
val isDark by settings.isDark.collectAsStateWithLifecycle(false)
```

Class-এর উপরেও `by` — Dart-এর `mixin`-এর জায়গায়:

```kotlin
class NotesRepository(logger: Logger) : Logger by logger    // Logger-এর সব method logger-কে দিল
```

**Best approach:** Value বাইরে থেকে আসে (Hilt, `onCreate()`) → `lateinit`। নিজেই বানাতে পারেন, শুধু দেরিতে → `lazy`। তবে সবচেয়ে ভালো হলো constructor-এ নেওয়া — তখন দুটোর কোনোটাই লাগে না।

[উপরে ফিরুন](#toc)

### <a id="ch1-10"></a>১.১০ Java-র সাথে

আপনি আগে Java-তে Android করেছেন, তাই পুরনো code পড়তে এটা কাজে লাগবে। Kotlin আর Java একই project-এ পাশাপাশি থাকে, একে অপরকে সরাসরি call করে।

- **Getter/setter property হয়ে যায়:** Java-র `note.getTitle()` Kotlin-এ `note.title`।
- **এক-method interface-এ lambda:** `button.setOnClickListener { save() }`। Java-তে এটার জন্য anonymous class লাগত।
- **Checked exception নেই:** Java-র `throws IOException` Kotlin-এ ধরতে বাধ্য না। সুবিধা, কিন্তু ভুলে যাওয়ার ঝুঁকিও।
- **Java থেকে Kotlin call করতে:** `@JvmStatic` (companion-এর function-কে আসল static বানায়), `@JvmField` (getter ছাড়া field), `@JvmOverloads` (default parameter-এর জন্য overload)।

Android Studio-তে Java file খুলে **Code → Convert Java File to Kotlin File** দিলে নিজে থেকে রূপান্তর হয়। পুরনো Java code দেখে Kotlin শেখার এটা দারুণ উপায়। শুধু ফলাফলে যে `!!` আসে, সেগুলো হাতে ঠিক করুন।

> **মনে রাখুন**
> - `final` → `val`, `??` → `?:`, `!` → `!!`, `switch` → `when`, `void` → `Unit`।
> - `freezed`-এর কাজ `data class` আর `sealed interface` করে, code generation ছাড়া।
> - `static` নেই — `companion object`, `object` আর top-level function।
> - Class default-এ `final`। Collection read-only আর mutable আলাদা।
> - Trailing lambda বুঝলে Compose বোঝা সহজ।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Dart থেকে Kotlin-এ আসা সহজ ছিল, কারণ null safety আর type system প্রায় একই। আমার কাছে Kotlin-এর সবচেয়ে কাজের জিনিস হলো data class, sealed interface দিয়ে exhaustive `when`, আর read-only collection — এগুলো ভুল state compile time-এই আটকে দেয়।"
> - *English:* "Moving from Dart to Kotlin was easy, because null safety and the type system are almost the same. What I find most useful in Kotlin are data classes, sealed interfaces with an exhaustive `when`, and read-only collections — they stop bad state at compile time."

[উপরে ফিরুন](#toc)

---

## <a id="ch2"></a>২. Async — Future আর Stream থেকে Coroutine আর Flow

Flutter-এ async লেখা আপনার কাছে শ্বাস নেওয়ার মতো সহজ: `async`, `await`, `Stream`, `StreamBuilder`। Kotlin-এর coroutine প্রথমে একটু ভারী শোনায় — scope, dispatcher, job, structured concurrency। কিন্তু একবার বুঝলে দেখবেন, এগুলো সব একটা প্রশ্নের উত্তর দেয়, যেটা Dart-এ আপনাকে কখনো ভাবতে হয়নি: **"এই কাজটা কোন thread-এ চলবে, আর কখন থামবে?"**

তাই এই অধ্যায় শুরু হচ্ছে thread দিয়ে।

### <a id="ch2-1"></a>২.১ সবচেয়ে বড় পার্থক্য: thread

**Dart-এর জগৎ:** একটা isolate, তাতে একটা thread, একটা event loop। `await` দিলে আপনার function থামে, event loop অন্য কাজ ধরে, তারপর ফল এলে আবার আপনার function চলে। কখনো দুইটা Dart code একই মুহূর্তে একই memory ছোঁয় না। তাই lock নেই, race condition প্রায় নেই। ভারী CPU কাজের জন্য আলাদা isolate, যেটা memory শেয়ার করে না — message পাঠিয়ে কথা বলে।

**Kotlin-এর জগৎ:** অনেকগুলো আসল thread, আর সবাই একই memory দেখে। Coroutine হলো thread-এর উপরে একটা হালকা কাজ — থামতে পারে, আবার চলতে পারে, আর দরকার হলে এক thread থেকে আরেক thread-এ সরে যেতে পারে।

```
Dart                                   Kotlin
─────────────────────────              ──────────────────────────────────────
isolate (একটা thread)                  Main thread ── UI, ছোট কাজ
  └─ event loop                        IO pool ───── network, disk
      ├─ আপনার code                     Default pool ─ CPU-র ভারী কাজ
      ├─ await-এর পরের অংশ                   ▲
      └─ timer, I/O callback            coroutine এদের মধ্যে আসা-যাওয়া করে,
                                        আর সবাই একই memory দেখে
আলাদা isolate ─ আলাদা memory
```

এর দুইটা ফল, দুটোই মনে গেঁথে রাখুন:

1. **ভারী কাজ অন্য thread-এ পাঠানো খুব সহজ।** Isolate-এর মতো data copy করতে হয় না।
2. **Shared mutable state এখন সত্যিকারের ঝুঁকি।** দুইটা coroutine দুই thread-এ একই `MutableList` বা `var` বদলালে data নষ্ট হতে পারে। Dart-এ এই bug হয়ই না। তাই Kotlin-এ immutable data, `StateFlow.update {}`, বা `Mutex` লাগে।

আর সবার উপরে: **main thread আটকানো যাবে না।** Network, disk, বড় হিসাব main thread-এ চালালে UI জমে যায়, আর ৫ সেকেন্ডে ANR আসে।

[উপরে ফিরুন](#toc)

### <a id="ch2-2"></a>২.২ `Future` → `suspend`

**এক লাইনে:** যে function অপেক্ষা করে, Dart-এ সেটা `Future` ফেরত দেয়। Kotlin-এ সেটা `suspend` function, আর সরাসরি ফল ফেরত দেয়।

**Flutter-এ:**

```dart
Future<Note> loadNote(String id) async {
  final dto = await api.getNote(id);
  return dto.toDomain();
}

final note = await loadNote('42');
```

**Kotlin-এ:**

```kotlin
suspend fun loadNote(id: String): Note {
    val dto = api.getNote(id)          // এখানে coroutine থামে — thread আটকায় না
    return dto.toDomain()
}

val note = loadNote("42")              // await লেখা লাগে না
```

**কী মিলল, কী আলাদা:**

| Dart | Kotlin |
|---|---|
| `Future<Note>` return type | `suspend fun ...: Note` — return type-এ শুধু `Note` |
| `async` keyword | `suspend` keyword |
| `await loadNote()` | `loadNote()` — সাধারণ call-এর মতো দেখায় |
| `await` যেকোনো `async` function-এ | Suspend function call করা যায় শুধু আরেকটা suspend function বা coroutine-এর ভেতর থেকে |

Android Studio বাম পাশে একটা ছোট চিহ্ন দেখায়, কোন লাইনে coroutine থামতে পারে। `await` না থাকায় এটাই আপনার চোখ।

**ভেতরে কীভাবে কাজ করে:** Compiler প্রতিটা suspend function-কে একটা state machine বানায়। প্রতিটা থামার জায়গা একটা ধাপ। থামার সময় local variable একটা `Continuation` object-এ রাখা হয়, আর ফল এলে সেখান থেকে আবার চলে। Dart-এর `async` function-ও ভেতরে প্রায় একই কাজ করে। তাই হাজারটা coroutine চালানো যায় — প্রতিটার জন্য আলাদা thread লাগে না।

[উপরে ফিরুন](#toc)

### <a id="ch2-3"></a>২.৩ কাজ চালু করা: `launch`, `async`

**এক লাইনে:** "চালাও, ফল লাগবে না" → `launch`। "একসাথে চালাও, পরে ফল নেব" → `async`।

**Flutter-এ:**

```dart
void refresh() {
  unawaited(_repo.sync());                    // ফল লাগবে না
}

Future<Dashboard> loadDashboard() async {
  final results = await Future.wait([_repo.loadNotes(), _repo.loadTags()]);
  return Dashboard(results[0] as List<Note>, results[1] as List<Tag>);
}
```

**Kotlin-এ:**

```kotlin
fun refresh() {
    viewModelScope.launch { repo.sync() }          // ফল লাগবে না, Job ফেরত দেয়
}

suspend fun loadDashboard(): Dashboard = coroutineScope {
    val notes = async { repo.loadNotes() }         // দুইটা একসাথে শুরু
    val tags = async { repo.loadTags() }
    Dashboard(notes.await(), tags.await())         // Future.wait — কিন্তু type-safe
}
```

| Builder | ফেরত দেয় | Dart-এ কাছাকাছি |
|---|---|---|
| `launch { }` | `Job` | `unawaited(future)` |
| `async { }` | `Deferred<T>` (`.await()` দিয়ে ফল) | একটা `Future` চালু করে রাখা |
| `coroutineScope { }` | block-এর ফল | `Future.wait`-এর চারপাশের function |
| `runBlocking { }` | block-এর ফল | (নেই) — thread আটকায়, শুধু `main()` আর পুরনো test-এ |

**খেয়াল করুন:** `launch` আর `async` চালু করতে একটা **scope** লাগে (`viewModelScope.launch`)। Dart-এ যেকোনো জায়গা থেকে `Future` চালু করা যায়। Kotlin-এ প্রতিটা coroutine-এর একটা মালিক থাকে। কেন — পরের অংশে।

[উপরে ফিরুন](#toc)

### <a id="ch2-4"></a>২.৪ Scope: কাজ কখন থামবে

**এক লাইনে:** Scope হলো coroutine-এর মালিক। মালিক মরলে তার সব কাজ নিজে থেকে থামে।

**Flutter-এ সমস্যাটা আপনি চেনেন:**

```dart
class _NoteScreenState extends State<NoteScreen> {
  StreamSubscription<Note>? _sub;

  @override
  void initState() {
    super.initState();
    _sub = repo.watchNote(widget.id).listen((n) => setState(() => note = n));
    _load();                                   // screen বন্ধ হলেও এটা চলতেই থাকবে
  }

  Future<void> _load() async {
    final n = await repo.fetch(widget.id);
    if (!mounted) return;                      // এই check ভুলে গেলে crash
    setState(() => note = n);
  }

  @override
  void dispose() {
    _sub?.cancel();                            // হাতে বন্ধ করতে হয়
    super.dispose();
  }
}
```

চালু করা `Future` কেউ থামায় না। তাই `mounted` check, আর প্রতিটা subscription হাতে cancel।

**Kotlin-এ scope এটা নিজে করে:**

```kotlin
class NoteViewModel(private val repo: NotesRepository) : ViewModel() {
    fun load(id: String) {
        viewModelScope.launch {
            val note = repo.fetch(id)          // ViewModel clear হলে এই call নিজে থেকে বাতিল
            _state.update { it.copy(note = note) }
        }
    }
}
```

`mounted` check নেই, `dispose`-এ cancel নেই। ViewModel clear হলে `viewModelScope` বন্ধ হয়, আর তার ভেতরের সব coroutine বাতিল।

| Scope | কখন বন্ধ হয় | Flutter-এ কাছাকাছি |
|---|---|---|
| `viewModelScope` | ViewModel clear হলে (screen সত্যিই বন্ধ) | Cubit-এর `close()` |
| `lifecycleScope` | Activity destroy হলে | `State.dispose()` |
| `rememberCoroutineScope()` | Composable screen থেকে সরে গেলে | widget dispose |

**এই নিয়মের নাম structured concurrency:**
1. প্রতিটা coroutine একটা parent-এর ভেতরে চলে।
2. Parent বাতিল হলে সব child বাতিল।
3. Parent শেষ হয় না, যতক্ষণ সব child শেষ না হয়।
4. একটা child fail করলে parent জানে। সাধারণ scope-এ তখন বাকি child-রাও বাতিল হয়। `SupervisorJob` থাকলে বাকিরা চলতে থাকে — `viewModelScope` এটাই ব্যবহার করে, তাই একটা request fail করলে ViewModel-এর অন্য কাজ থামে না।

**ফাঁদ:** `GlobalScope` ব্যবহার করবেন না। এটা কারো সাথে বাঁধা না, তাই কখনো থামে না — Dart-এর থামানো যায় না এমন `Future`-এর সমস্যা ফিরিয়ে আনে। App-ব্যাপী কাজ লাগলে Application-এ নিজের একটা scope বানিয়ে Hilt দিয়ে inject করুন।

[উপরে ফিরুন](#toc)

### <a id="ch2-5"></a>২.৫ `Isolate` → Dispatcher

**এক লাইনে:** Dispatcher ঠিক করে coroutine কোন thread-এ চলবে। `Isolate.run` মানে Kotlin-এ `withContext(Dispatchers.Default)`।

**Flutter-এ:**

```dart
final notes = await Isolate.run(() => parseHugeJson(raw));     // বা compute(parseHugeJson, raw)
```

**Kotlin-এ:**

```kotlin
val notes = withContext(Dispatchers.Default) { parseHugeJson(raw) }
```

Data copy নেই, message passing নেই। কারণ সব thread একই memory দেখে।

| Dispatcher | কোথায় | কী কাজে |
|---|---|---|
| `Dispatchers.Main` | Main (UI) thread | UI update, ছোট কাজ |
| `Dispatchers.IO` | IO-র জন্য বড় thread pool | Network, file, database — যেখানে বেশিরভাগ সময় অপেক্ষা |
| `Dispatchers.Default` | CPU core-এর সমান thread | JSON parse, sort, image — CPU-র কাজ |

**Main-safe নিয়ম:** প্রতিটা suspend function নিজেই ঠিক করবে কোন dispatcher লাগে। তাহলে caller যেকোনো thread থেকে নিশ্চিন্তে call করতে পারে।

```kotlin
class NotesRepository(
    private val dao: NoteDao,
    private val ioDispatcher: CoroutineDispatcher = Dispatchers.IO,    // test-এ বদলানো যায়
) {
    suspend fun export(): File = withContext(ioDispatcher) {
        writeToFile(dao.getAll())
    }
}
```

**Best approach:** Retrofit আর Room-এর suspend function আগে থেকেই main-safe — এগুলোকে `withContext(Dispatchers.IO)`-এ মোড়াবেন না। নিজের file বা CPU কাজে `withContext` দিন। আর dispatcher constructor-এ নিন, যাতে test-এ test dispatcher দেওয়া যায়।

[উপরে ফিরুন](#toc)

### <a id="ch2-6"></a>২.৬ Cancellation

**এক লাইনে:** Coroutine-কে জোর করে থামানো হয় না। সে নিজে থামার জায়গায় দেখে, তাকে বাতিল করা হয়েছে কি না।

Dart-এ `Future` বাতিলই করা যায় না। Kotlin-এ যায়, কিন্তু coroutine-এর সহযোগিতা লাগে। প্রতিটা suspend call (`delay`, network, `withContext`) নিজে check করে। লম্বা CPU loop-এ suspend call না থাকলে আপনি নিজে check করুন:

```kotlin
suspend fun reindex(notes: List<Note>) = withContext(Dispatchers.Default) {
    for (note in notes) {
        ensureActive()             // বাতিল হলে এখানে থামে
        index(note)
    }
}
```

**ভেতরে কীভাবে:** বাতিল করলে coroutine-এর পরের suspend point-এ একটা `CancellationException` throw হয়। এই exception উপরে উঠে coroutine শেষ করে দেয়। এজন্যই পরের অংশের নিয়মটা জরুরি।

[উপরে ফিরুন](#toc)

### <a id="ch2-7"></a>২.৭ Error handling

**Flutter-এ:**

```dart
try {
  await repo.delete(id);
} on SocketException {
  emit(state.copyWith(error: 'Internet নেই'));
}
```

**Kotlin-এ:**

```kotlin
viewModelScope.launch {
    try {
        repo.delete(id)
    } catch (e: IOException) {
        _state.update { it.copy(error = "Internet নেই") }
    }
}
```

দেখতে একই। কিন্তু তিনটা নিয়ম নতুন:

1. **`launch`-এর ভেতরে না ধরা exception app crash করায়।** Dart-এ না ধরা `Future` error শুধু log হয় (zone-এর error handler-এ)। Kotlin-এ সেটা thread-এর uncaught exception — crash। `async`-এ exception থাকে `.await()` পর্যন্ত।
2. **`CancellationException` কখনো গিলবেন না।** `catch (e: Exception)` দিয়ে সব ধরলে এটাও ধরা পড়ে, আর coroutine বাতিল হওয়ার পরেও চলতে থাকে। নির্দিষ্ট exception ধরুন (`IOException`, `HttpException`)। সব ধরতেই হলে আগে আলাদা করে ছেড়ে দিন:

```kotlin
} catch (e: CancellationException) {
    throw e
} catch (e: Exception) {
    _state.update { it.copy(error = "কিছু একটা ভুল হয়েছে") }
}
```

3. **`runCatching { }` সাবধানে।** এটাও `CancellationException` ধরে। Suspend code-এ ব্যবহার করলে উপরের মতো আবার throw করুন।

[উপরে ফিরুন](#toc)

### <a id="ch2-8"></a>২.৮ `Stream` → `Flow`

**এক লাইনে:** `Flow` হলো Kotlin-এর `Stream`। পার্থক্য: default-এ এটা **cold** — কেউ collect না করলে কিছুই চলে না।

**Flutter-এ:**

```dart
Stream<int> countdown(int from) async* {
  for (var i = from; i >= 0; i--) {
    yield i;
    await Future.delayed(const Duration(seconds: 1));
  }
}

final sub = countdown(10).where((s) => s.isEven).map((s) => '$s সেকেন্ড').listen(print);
// পরে: sub.cancel();
```

**Kotlin-এ:**

```kotlin
fun countdown(from: Int): Flow<Int> = flow {
    for (i in from downTo 0) {
        emit(i)                   // yield
        delay(1_000)
    }
}

viewModelScope.launch {
    countdown(10)
        .filter { it % 2 == 0 }
        .map { "$it সেকেন্ড" }
        .collect { println(it) }  // listen — scope বন্ধ হলে নিজে থামে
}
```

| Dart | Kotlin |
|---|---|
| `async*` + `yield` | `flow { emit() }` |
| `.listen()` | `.collect { }` (suspend function) |
| `sub.cancel()` | scope বন্ধ হলে নিজে থেকে |
| single-subscription stream | cold `Flow` — প্রতিটা collector নিজের আলাদা run পায় |
| `StreamController.broadcast()` | `SharedFlow` |
| `StreamBuilder` | `collectAsStateWithLifecycle()` ([৬.৭](#ch6-7)) |

**ভেতরে কীভাবে — cold মানে কী:** `countdown(10)` লিখলে কিছুই চলে না। শুধু একটা "রেসিপি" তৈরি হয়। `collect` call করলে তখন `flow { }` block চলে। দুইজন collect করলে block দুইবার চলে, দুইজন আলাদা countdown পায়। Network call-এর flow দুইবার collect করলে দুইটা request যায়।

**ফাঁদ:** `collect` নিজেই suspend করে, flow শেষ না হওয়া পর্যন্ত। তাই একই coroutine-এ দুইটা `collect` পরপর লিখলে দ্বিতীয়টা কখনো চলে না। প্রতিটা collect আলাদা `launch`-এ রাখুন।

**কোন thread-এ — `flowOn`:**

```kotlin
repo.observeNotes()
    .map { notes -> notes.sortedBy { it.title } }
    .flowOn(Dispatchers.Default)     // উপরের ধাপগুলো Default-এ
    .collect { show(it) }            // collect হয় caller-এর thread-এ
```

**Room আর DataStore সরাসরি `Flow` দেয়।** Database বদলালে নতুন value নিজে থেকে আসে — drift-এর `.watch()`-এর মতো। Notes app-এর list screen ঠিক এভাবেই বানানো হবে।

[উপরে ফিরুন](#toc)

### <a id="ch2-9"></a>২.৯ `ValueNotifier` → `StateFlow`

**এক লাইনে:** `StateFlow` হলো সবসময় একটা current value রাখা hot stream — `ValueNotifier` আর Bloc-এর state stream মিলিয়ে।

**Flutter-এ:**

```dart
final count = ValueNotifier<int>(0);
count.value++;
ValueListenableBuilder(valueListenable: count, builder: (_, v, __) => Text('$v'));
```

**Kotlin-এ:**

```kotlin
class NotesViewModel : ViewModel() {
    private val _count = MutableStateFlow(0)
    val count: StateFlow<Int> = _count.asStateFlow()     // বাইরে শুধু read-only

    fun increment() = _count.update { it + 1 }           // atomic
}

// Compose-এ
val count by viewModel.count.collectAsStateWithLifecycle()
Text("$count")
```

| | `StateFlow` | `SharedFlow` |
|---|---|---|
| Flutter-এ | `ValueNotifier`, Bloc-এর state | `StreamController.broadcast()` |
| Initial value | লাগবেই | নেই |
| `.value` দিয়ে পড়া | হ্যাঁ | না (`replay` থাকলে cache থেকে পায়) |
| একই value আবার দিলে | যায় না (`equals` দিয়ে check) | যায় |
| দ্রুত অনেক value এলে | মাঝখানেরগুলো বাদ, শুধু শেষটা (conflation) | buffer অনুযায়ী |
| কাজ | UI state | কয়েকজনকে event broadcast |

**কেন `update {}`, `value = value + 1` না:** দুইটা coroutine দুই thread-এ একসাথে পড়ল, দুজনেই নিজের হিসাব লিখল — একজনের কাজ হারিয়ে গেল। `update {}` লেখার আগে দেখে নেয় মাঝখানে value বদলেছে কি না, বদলালে আবার চেষ্টা করে। Dart-এ একটা thread বলে এটা কখনো ভাবতে হয়নি।

**Cold flow থেকে StateFlow — `stateIn`:**

```kotlin
val notes: StateFlow<List<Note>> = repo.observeNotes()
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = emptyList(),
    )
```

`WhileSubscribed(5_000)` মানে: কেউ না শুনলে ৫ সেকেন্ড পর database query বন্ধ করো। Rotation-এ এক মুহূর্তের জন্য কেউ শোনে না — তখন query আবার শুরু হয় না। কিন্তু app background-এ গেলে কাজ সত্যিই থামে।

[উপরে ফিরুন](#toc)

### <a id="ch2-10"></a>২.১০ RxDart → Flow operator

**এক লাইনে:** RxDart দিয়ে যা করতেন, তার প্রায় সবই Flow-এ built-in।

| RxDart / Dart | Flow | কাজ |
|---|---|---|
| `map`, `where` | `map`, `filter` | |
| `Rx.combineLatest2` | `combine(a, b) { }` | যেকোনোটা বদলালে দুইটার শেষ value মিলিয়ে |
| `switchMap` | `flatMapLatest { }` | নতুন value এলে আগের কাজ বাতিল |
| `debounceTime` | `debounce(300)` | থামার পর অপেক্ষা |
| `distinct` | `distinctUntilChanged()` | পরপর একই value বাদ |
| `doOnData`, `onErrorResume` | `onEach`, `catch` | |

**Notes app-এর search, দুই পাশে:**

```dart
final results = _query.stream
    .debounceTime(const Duration(milliseconds: 300))
    .distinct()
    .switchMap((q) => q.isEmpty ? Stream.value(<Note>[]) : repo.search(q));
```

```kotlin
val results: StateFlow<List<Note>> = query
    .debounce(300)
    .distinctUntilChanged()
    .flatMapLatest { q -> if (q.isBlank()) flowOf(emptyList()) else repo.search(q) }
    .catch { emit(emptyList()) }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), emptyList())
```

প্রায় লাইন ধরে ধরে মিলে যায়। `debounce` আর `flatMapLatest`-এর জন্য `@OptIn(FlowPreview::class, ExperimentalCoroutinesApi::class)` লাগে। নামে "experimental" থাকলেও বহু বছর ধরে production-এ সাধারণভাবে ব্যবহার হয়।

[উপরে ফিরুন](#toc)

### <a id="ch2-11"></a>২.১১ Async-এর best approach এক নজরে

| কাজ | যা ব্যবহার করবেন |
|---|---|
| একবারের কাজ (load, save, delete) | `suspend fun` |
| বারবার বদলানো data (database, settings) | `Flow` |
| Screen-এর state | `StateFlow` (`stateIn` দিয়ে, বা `MutableStateFlow`) |
| ViewModel থেকে কাজ চালু | `viewModelScope.launch` |
| কয়েকটা কাজ একসাথে | `coroutineScope { async {} ; async {} }` |
| CPU-র ভারী কাজ | `withContext(Dispatchers.Default)` |
| নিজের file/disk কাজ | `withContext(Dispatchers.IO)` (Room/Retrofit-এ লাগে না) |
| UI-তে Flow পড়া | `collectAsStateWithLifecycle()` |
| পুরনো callback API-কে suspend বানানো | `suspendCancellableCoroutine` / `callbackFlow` |

শেষ লাইনটা interview-এ প্রায়ই আসে: পুরনো listener-ভিত্তিক API (location update, Firebase listener)-কে `callbackFlow { }` দিয়ে Flow বানানো যায়। Dart-এ `StreamController` দিয়ে callback-কে stream বানানোর মতো।

> **মনে রাখুন**
> - Dart-এ একটা thread, Kotlin-এ অনেক thread আর shared memory। এটাই সব পার্থক্যের মূল।
> - `Future` → `suspend fun`, `Stream` → `Flow`, `ValueNotifier` → `StateFlow`, `Isolate.run` → `withContext(Dispatchers.Default)`।
> - প্রতিটা coroutine-এর একটা scope আছে। Scope বন্ধ হলে কাজ নিজে থামে — `mounted` check বা `cancel()` লাগে না।
> - `CancellationException` গিলবেন না। `GlobalScope` না।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Coroutine-এ আমি সবসময় structured concurrency মানি: ViewModel-এর কাজ `viewModelScope`-এ, যাতে screen বন্ধ হলে সব নিজে থেকে বাতিল হয়। একবারের কাজ suspend function, বদলাতে থাকা data Flow, আর UI state StateFlow। Dart-এর সাথে বড় পার্থক্য হলো Kotlin-এ আসল thread আর shared memory, তাই আমি state immutable রাখি আর `update {}` দিয়ে বদলাই।"
> - *English:* "With coroutines I follow structured concurrency: ViewModel work runs in `viewModelScope`, so everything is cancelled when the screen goes away. One-shot work is a suspend function, changing data is a Flow, and UI state is a StateFlow. The big difference from Dart is that Kotlin has real threads and shared memory, so I keep state immutable and change it with `update {}`."

[উপরে ফিরুন](#toc)

---

## <a id="ch3"></a>৩. Project আর Gradle — `pubspec.yaml`-এর জায়গায়

Flutter-এ `pubspec.yaml` একটা শান্ত জায়গা। নাম, version, কয়েকটা dependency, ব্যস। Android-এর Gradle প্রথম দেখায় একটা জঙ্গলের মতো লাগে। ভয়ের কিছু নেই — আপনার Flutter project-এর `android/` folder-এ এই জঙ্গল সবসময় ছিল। এখন শুধু এর ম্যাপটা চিনে নেব।

**এক লাইনে:** `pubspec.yaml`-এর কাজ তিনটা file ভাগ করে নেয়: `settings.gradle.kts` (কোন module আছে), `libs.versions.toml` (version), আর `app/build.gradle.kts` (dependency আর app-এর setting)।

### Folder-এর চেহারা, Flutter-এর পাশে

```
Flutter project                        Android project
───────────────────────                ─────────────────────────────────────────
pubspec.yaml                           settings.gradle.kts
                                       gradle/libs.versions.toml
                                       app/build.gradle.kts
lib/                                   app/src/main/java/com/byteonyx/notes/
  main.dart                              MainActivity.kt, NotesApp.kt
  features/notes/...                     feature/notes/...
assets/                                app/src/main/res/        (drawable, values, font)
                                       app/src/main/assets/     (raw file)
test/                                  app/src/test/            (JVM test — device লাগে না)
integration_test/                      app/src/androidTest/     (device-এ চলা test)
android/app/src/main/AndroidManifest   app/src/main/AndroidManifest.xml  ← একই file
```

### `pubspec.yaml` → version catalog

**Flutter-এ:**

```yaml
dependencies:
  flutter_bloc: ^8.1.0
  dio: ^5.4.0
  drift: ^2.15.0
dev_dependencies:
  bloc_test: ^9.1.0
```

**Android-এ — দুই ধাপে।** আগে catalog-এ নাম আর version:

```toml
# gradle/libs.versions.toml
[versions]
kotlin = "2.x.x"
composeBom = "20xx.xx.xx"
room = "2.x.x"

[libraries]
androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "composeBom" }
androidx-compose-material3 = { group = "androidx.compose.material3", name = "material3" }
androidx-room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
androidx-room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
androidx-room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }

[plugins]
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
ksp = { id = "com.google.devtools.ksp", version = "x.x.x" }
```

তারপর module-এ ব্যবহার:

```kotlin
// app/build.gradle.kts
dependencies {
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.compose.material3)          // BOM থাকায় version লাগে না
    implementation(libs.androidx.room.runtime)
    implementation(libs.androidx.room.ktx)
    ksp(libs.androidx.room.compiler)                         // code generator
    testImplementation(libs.junit)
}
```

**কী মিলল, কী আলাদা:**

| Flutter | Android |
|---|---|
| `dependencies:` | `implementation(...)` |
| `dev_dependencies:` | `testImplementation(...)`, `debugImplementation(...)` |
| `build_runner` + generator package | `ksp(...)` — compile-এর সময় নিজে চলে, আলাদা command লাগে না |
| Flutter SDK version সব widget-এর version ঠিক করে | **BOM** — Compose-এর সব library-র মিলানো version একটা সংখ্যায় |
| `flutter pub get` | Gradle sync (Android Studio-র হাতি চিহ্ন) |

**KSP** — `build_runner`-এর জায়গায়। Room, Hilt, Moshi এর মতো library annotation দেখে code বানায়। Flutter-এ আপনাকে `dart run build_runner build` চালাতে হতো। এখানে build-এর সময় নিজে চলে। পুরনো project-এ `kapt` দেখবেন — একই কাজ, কিন্তু ধীর। নতুন code-এ KSP।

### তিনটা SDK সংখ্যা

```kotlin
android {
    namespace = "com.byteonyx.notes"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.byteonyx.notes"     // Play Store-এ পরিচয় — পরে বদলানো যায় না
        minSdk = 24
        targetSdk = 36
        versionCode = 1                          // pubspec-এর version: 1.0.0+1 এর "+1"
        versionName = "1.0.0"                    // "1.0.0" অংশ
    }
}
```

| সংখ্যা | মানে |
|---|---|
| `minSdk` | এর নিচের Android-এ install হবে না |
| `compileSdk` | কোন SDK-র API দেখে compile হবে। নতুন API ব্যবহার করতে এটা বাড়াতে হয়। |
| `targetSdk` | কোন Android version-এর নিয়ম মেনে app চলবে। Play Store প্রতি বছর এটা বাড়াতে বাধ্য করে, আর বাড়ালে নতুন behavior চালু হয়। |

Flutter-এ এগুলো `android/app/build.gradle`-এ `flutter.minSdkVersion` ধরনের default দিয়ে থাকত। এখন এগুলো আপনার সিদ্ধান্ত।

**Best approach:** নতুন project Android Studio-র "Empty Activity" template দিয়ে খুলুন। Version catalog, Compose, Kotlin DSL সব আগে থেকে সাজানো থাকে। Gradle হাতে শুরু থেকে লেখার দরকার নেই।

**Module:** বড় app-এ একটা `app`-এর বদলে অনেক module: `:core:database`, `:feature:notes`। Flutter-এ `packages/` folder-এ local package রাখার মতো। লাভ: বদলানো module-ই শুধু আবার build হয়, আর `internal` দিয়ে ভেতরের জিনিস লুকানো যায়। শেখার সময় একটা module যথেষ্ট।

> **মনে রাখুন**
> - `pubspec.yaml` → `libs.versions.toml` + `build.gradle.kts`। `build_runner` → KSP।
> - BOM একটা সংখ্যায় সব Compose library-র version মেলায়।
> - `minSdk`, `compileSdk`, `targetSdk` তিনটা আলাদা জিনিস। `targetSdk` বাড়ানো মানে নতুন নিয়ম চালু।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি version catalog দিয়ে সব dependency এক জায়গায় রাখি, Compose-এ BOM ব্যবহার করি, আর code generation-এ KSP নিই, কারণ kapt-এর চেয়ে দ্রুত। `targetSdk` বাড়ানোর আগে সেই version-এর behavior change পড়ে test করি।"
> - *English:* "I keep dependencies in a version catalog, use the BOM for Compose, and use KSP for code generation because it's faster than kapt. Before raising `targetSdk`, I read that version's behavior changes and test them."

[উপরে ফিরুন](#toc)

---

## <a id="ch4"></a>৪. App-এর component: Application, Activity, Manifest, Context

আপনি যখন Java-তে Android করতেন, তখন প্রতিটা screen ছিল একটা Activity, আর Activity থেকে Activity-তে `startActivity` দিয়ে লাফাতেন। আজ ছবিটা বদলেছে, আর অনেকটা Flutter-এর দিকে এসেছে: একটা Activity, তার ভেতরে পুরো app। কিন্তু Activity, Manifest, Context — এই ভিতগুলো আগের মতোই আছে। এগুলো ছাড়া কোনো Android app নড়তেই পারে না।

### <a id="ch4-1"></a>৪.১ চালু হওয়া: `main()` থেকে Activity

**এক লাইনে:** Flutter-এর `main()` + `runApp()`-এর কাজ Android-এ দুই জায়গায় ভাগ হয়: `Application` (app-ব্যাপী setup) আর `MainActivity` (UI বসানো)।

**Flutter-এ:**

```dart
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await setupDependencies();                  // get_it, Firebase ...
  runApp(const NotesApp());
}

class NotesApp extends StatelessWidget {
  const NotesApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp.router(theme: appTheme, routerConfig: router);
}
```

**Android-এ:**

```kotlin
@HiltAndroidApp                                         // Hilt-এর setup (get_it-এর জায়গায়)
class NotesApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        // App-ব্যাপী setup: logging, crash reporting
    }
}

@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {                                    // runApp-এর জায়গা
            NotesTheme {                                // MaterialApp-এর theme
                NotesNavHost()                          // routerConfig
            }
        }
    }
}
```

**ভেতরে কীভাবে কাজ করে:**
1. User icon-এ tap করে। System একটা Linux process চালু করে।
2. Process-এ প্রথমে `Application` তৈরি হয় — একটাই, process যতক্ষণ বাঁচে।
3. Manifest-এ যে Activity "launcher" হিসেবে লেখা, সেটা তৈরি হয়, `onCreate()` চলে।
4. `setContent { }` Compose UI বসায়।

[উপরে ফিরুন](#toc)

### <a id="ch4-2"></a>৪.২ Manifest

**এক লাইনে:** Manifest হলো app-এর পরিচয়পত্র। System app চালানোর আগে এটা পড়ে।

Flutter-এ আপনি এই file-এ permission যোগ করতেন — `android/app/src/main/AndroidManifest.xml`। একই file:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application
        android:name=".NotesApplication"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.Notes">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

- **কী কী থাকে:** কোন component আছে, কোন permission চায়, কোন link বা intent ধরতে পারে।
- **Library-র manifest মিশে যায়।** Flutter-এ plugin-এর permission নিজে থেকে আপনার manifest-এ চলে আসত — এটাই manifest merger। Android Studio-তে Manifest খুলে নিচের **Merged Manifest** tab-এ শেষ রূপ দেখুন। কোন library কোন permission ঢুকিয়েছে, সেটা এখানে ধরা পড়ে।
- **`android:exported="true"`** মানে অন্য app এই Activity চালু করতে পারে। Launcher Activity-তে লাগবেই। বাকি জায়গায় দরকার না থাকলে `false` — এটা security-র ব্যাপার।

[উপরে ফিরুন](#toc)

### <a id="ch4-3"></a>৪.৩ চারটা component

**এক লাইনে:** Android app চারটা জিনিস দিয়ে তৈরি, আর চারটাই Manifest-এ লিখতে হয়। Flutter-এ এদের প্রত্যেকটা কোনো না কোনো plugin চালাত।

| Component | কাজ | Notes app-এ উদাহরণ | Flutter-এ কে করত |
|---|---|---|---|
| **Activity** | একটা window বা screen | `MainActivity` — পুরো app | `FlutterActivity` |
| **Service** | UI ছাড়া কাজ | Note-এর voice recording চলছে | `audio_service` ধরনের plugin |
| **BroadcastReceiver** | System-এর ঘটনা শোনা | Phone restart হলে reminder আবার বসানো | `android_alarm_manager_plus` |
| **ContentProvider** | অন্য app-কে data দেওয়া; file share | Note-এর ছবি অন্য app-এ share (`FileProvider`) | `share_plus` |

**Single-Activity:** আগে প্রতিটা screen আলাদা Activity ছিল — আপনি সম্ভবত সেভাবেই করেছেন। এখন একটা Activity, আর তার ভেতরে Compose-এর navigation দিয়ে সব screen। ঠিক Flutter-এর মতো, যেখানে একটা `FlutterActivity`-র ভেতরে Navigator সব route চালায়। মাঝে একটা যুগ ছিল, যখন একটা Activity-র ভেতরে **Fragment** দিয়ে screen বানানো হতো। পুরনো project-এ Fragment দেখবেন — এর নিজের lifecycle আছে, আর এর view, Fragment-এর আগেই destroy হয়। নতুন Compose app-এ Fragment প্রায় লাগে না।

[উপরে ফিরুন](#toc)

### <a id="ch4-4"></a>৪.৪ Context — `BuildContext` না

**এক লাইনে:** নাম একই রকম, কিন্তু কাজ একদম আলাদা। `BuildContext` হলো widget tree-তে একটা ঠিকানা। Android-এর `Context` হলো system-এর দরজা।

**Flutter-এ `BuildContext` দিয়ে যা করেন:**

```dart
Theme.of(context).colorScheme.primary;       // tree-র উপরে Theme খোঁজা
context.read<NotesCubit>();                  // tree-র উপরে Provider খোঁজা
Navigator.of(context).push(...);
```

**Android-এ `Context` দিয়ে যা করেন:**

```kotlin
context.getString(R.string.app_name)                         // resource পড়া
context.getSystemService(NotificationManager::class.java)    // system service
context.startActivity(intent)                                // অন্য screen বা app
context.filesDir                                             // app-এর নিজের folder
```

Compose-এ Theme খোঁজার কাজ করে `CompositionLocal` ([৬.৮](#ch6-8)), আর Context পেতে `LocalContext.current`।

**দুই রকম Context — গুলিয়ে ফেললে memory leak:**

| | Activity context | Application context |
|---|---|---|
| কতদিন বাঁচে | Activity যতক্ষণ — rotation-এ মরে | Process যতক্ষণ |
| Theme জানে | হ্যাঁ | না |
| কোথায় | UI, dialog, theme লাগে এমন কাজ | Singleton, repository, database |

**ফাঁদ:** যে object Activity-র চেয়ে বেশিদিন বাঁচে (singleton, ViewModel, static field), সে কখনো Activity context ধরে রাখবে না। ধরে রাখলে rotation-এর পরে পুরনো Activity আর তার পুরো screen memory-তে আটকে থাকে। Flutter-এ `BuildContext` dispose-এর পরে ব্যবহার করলে error আসে। Android-এ কোনো error আসে না, শুধু চুপচাপ memory খেয়ে যায়। খুঁজে পেতে LeakCanary library ব্যবহার করুন।

[উপরে ফিরুন](#toc)

### <a id="ch4-5"></a>৪.৫ পুরনো View system — যা আপনি জানতেন

Interview-এ আর পুরনো code-এ এটা আসবে, তাই এক নজরে চিনে রাখুন। আপনি যখন Java-তে Android করতেন, UI লেখা হতো এভাবে:

```xml
<!-- res/layout/item_note.xml -->
<LinearLayout android:orientation="vertical" ...>
    <TextView android:id="@+id/title" ... />
    <TextView android:id="@+id/preview" ... />
</LinearLayout>
```

```kotlin
// আগে findViewById, এখন ViewBinding
val binding = ItemNoteBinding.inflate(layoutInflater)
binding.title.text = note.title           // হাতে UI বদলানো — imperative
```

| View system | Compose | Flutter |
|---|---|---|
| XML layout | `@Composable` function | Widget |
| `LinearLayout` | `Column` / `Row` | `Column` / `Row` |
| `FrameLayout` | `Box` | `Stack` |
| `ConstraintLayout` | `ConstraintLayout` (Compose-এও আছে), বা সাধারণ Row/Column | (নেই) |
| `RecyclerView` + `Adapter` + `ViewHolder` + `DiffUtil` | `LazyColumn` + `items(key = )` | `ListView.builder` |
| `view.text = x` হাতে বদলানো | State বদলালে নিজে | `setState` |
| `findViewById` / ViewBinding | (লাগে না) | (লাগে না) |

**বড় পার্থক্য:** View system imperative — আপনি view-কে বলেন "এখন এই text দেখাও"। Compose আর Flutter declarative — আপনি বলেন "state এই হলে UI এরকম দেখায়"। Flutter-এর চিন্তা তাই Compose-এ সরাসরি চলে।

Compose আর View একসাথেও চলে: পুরনো screen-এ `ComposeView` দিয়ে Compose বসানো যায়, আর Compose-এর ভেতরে `AndroidView` দিয়ে পুরনো View (যেমন MapView)। Flutter-এর `AndroidView` (platform view)-এর মতো।

> **মনে রাখুন**
> - `main()` + `runApp()` → `Application` + `MainActivity.setContent { }`।
> - Manifest = পরিচয়পত্র। Library-র manifest আপনার manifest-এ মেশে।
> - চারটা component: Activity, Service, BroadcastReceiver, ContentProvider।
> - `Context` ≠ `BuildContext`। লম্বা-জীবনের object-এ Activity context না।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি single-Activity architecture নিই — একটা Activity, ভেতরে Compose navigation দিয়ে সব screen, Flutter-এর মতোই। Context নিয়ে আমি সাবধান থাকি: ViewModel বা singleton-এ কখনো Activity context রাখি না, লাগলে application context দিই।"
> - *English:* "I use a single-Activity architecture — one Activity with all screens in Compose navigation, much like Flutter. I'm careful with Context: I never keep an Activity context in a ViewModel or singleton; if I need one there, I use the application context."

[উপরে ফিরুন](#toc)

---

## <a id="ch5"></a>৫. Lifecycle, rotation আর process death

এই অধ্যায়টা Flutter developer-দের জন্য Android-এর সবচেয়ে বড় ধাক্কা। Flutter-এ phone ঘোরালে কিছুই হয় না — layout বদলায়, `State` বেঁচে থাকে, user-এর লেখা অর্ধেক note যেমন ছিল তেমন থাকে। Android-এ phone ঘোরালে আপনার Activity মরে যায়, আর নতুন একটা জন্মায়। আর app background-এ থাকলে system পুরো app মেরে দিতে পারে — কোনো খবর না দিয়ে। শুনে ভয় লাগে, কিন্তু নিয়মগুলো জানলে সমাধান সহজ।

### <a id="ch5-1"></a>৫.১ App lifecycle

**এক লাইনে:** `didChangeAppLifecycleState`-এর জায়গায় Android-এ `Lifecycle` — Activity-রও আছে, পুরো process-এরও আছে।

**Flutter-এ:**

```dart
class _NotesState extends State<Notes> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) refreshNotes();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }
}
```

**Android-এ, Compose-এর ভেতরে:**

```kotlin
LifecycleResumeEffect(Unit) {           // screen সামনে এলে
    viewModel.refreshNotes()
    onPauseOrDispose { }                // সরে গেলে বা composable চলে গেলে
}
```

**Activity-র ধাপগুলো, Flutter-এর পাশে:**

```
onCreate()   ─ তৈরি হলো                        (Flutter: engine চালু, initState)
onStart()    ─ screen দেখা যাচ্ছে              (AppLifecycleState.resumed-এর কাছাকাছি)
onResume()   ─ সামনে আছে, touch পাচ্ছে         (resumed)
   ··· চলছে ···
onPause()    ─ অন্য কিছু সামনে এল (dialog-ধরনের activity, multi-window)   (inactive)
onStop()     ─ আর দেখা যাচ্ছে না (home চাপা)   (paused / hidden)
onDestroy()  ─ শেষ — back চাপা, বা configuration change                 (detached)
```

- **STARTED** = দেখা যাচ্ছে। UI-র data collect করার সঠিক সময়। `collectAsStateWithLifecycle()` ঠিক এটাই মানে।
- **RESUMED** = সামনে আর focus-এ। Camera, sensor-এর মতো জিনিস এখানে চালু করুন।
- `onStop()`-এর পরে system যেকোনো সময় process মারতে পারে। তাই জরুরি জিনিস তার আগেই save করুন।

পুরো app foreground-এ না background-এ — শুধু এটা জানতে `ProcessLifecycleOwner` (Flutter-এর app-level lifecycle-এর আরও কাছাকাছি)।

[উপরে ফিরুন](#toc)

### <a id="ch5-2"></a>৫.২ Rotation-এ Activity মরে যায়

**এক লাইনে:** Rotation, dark mode, ভাষা, font size, window size বদলালে Android Activity-কে destroy করে নতুন করে তৈরি করে। এর নাম **configuration change**।

**কেন Android এটা করে:** নতুন configuration-এর জন্য আলাদা resource লাগতে পারে — landscape-এর আলাদা layout, অন্য ভাষার string, dark theme-এর রং। পুরো Activity নতুন করে বানালে সব resource নতুন করে load হয়। Flutter নিজে এসব সামলায়, তাই আপনাকে কখনো ভাবতে হয়নি।

**কী হারায়:** Activity-র field, আর composable-এর `remember` করা state।

**কী বাঁচে:** ViewModel। কারণ Activity destroy হওয়ার সময় system জানে এটা configuration change, তাই Activity-র `ViewModelStore` (সব ViewModel রাখা একটা map) নতুন Activity-কে দিয়ে দেয়। নতুন Activity একই ViewModel পায়। User সত্যিই back চেপে বের হলে তখন store clear হয়, আর ViewModel-এর `onCleared()` চলে।

**নিজে দেখুন:** Notes app-এ একটা `remember { mutableStateOf("") }` দিয়ে text field বানান, কিছু লিখুন, phone ঘোরান — লেখা মুছে যাবে। তারপর `rememberSaveable` দিন — থাকবে।

[উপরে ফিরুন](#toc)

### <a id="ch5-3"></a>৫.৩ State কোথায় রাখবেন

এটা পুরো অধ্যায়ের সারাংশ। এক table-এ:

| State | কোথায় | Rotation-এ | Process death-এ | Flutter-এ |
|---|---|---|---|---|
| ছোট UI state (dropdown খোলা কি না) | `remember` | হারায় | হারায় | `State`-এর field |
| হারানো যাবে না এমন UI state (লেখা text, selected tab) | `rememberSaveable` | থাকে | থাকে | `RestorationMixin` |
| Screen-এর state আর logic | `ViewModel` | থাকে | হারায় | Cubit |
| ViewModel-এর ছোট জরুরি state (search query, edit করা note-এর id) | `SavedStateHandle` | থাকে | থাকে | (নেই) |
| আসল data | Room, DataStore, server | থাকে | থাকে | drift, shared_preferences |

**Best approach:** আসল data সবসময় database-এ। ViewModel সেখান থেকে পড়ে। আর user-এর হাতের কাজ (অর্ধেক লেখা note, search) `SavedStateHandle` বা `rememberSaveable`-এ। তাহলে কোনো পরিস্থিতিতেই user-এর কাজ হারায় না।

[উপরে ফিরুন](#toc)

### <a id="ch5-4"></a>৫.৪ Process death

**এক লাইনে:** App background-এ থাকলে memory-র জন্য system পুরো process মেরে ফেলতে পারে। User ফিরে এলে Android app-কে ঠিক আগের screen-এ খোলে, কিন্তু memory-র সব কিছু নতুন আর খালি।

**গল্পটা এরকম:**
1. User Notes app-এ একটা note লিখছে। অর্ধেক লিখে camera খুলল ছবি তুলতে।
2. Camera app অনেক memory চাইল। System আপনার background-এ থাকা process মেরে দিল। কোনো callback আসে না।
3. User ছবি তুলে ফিরে এল। System নতুন process চালু করল, আর **সরাসরি note লেখার screen** খুলল, back stack-সহ — যেন কিছুই হয়নি।
4. কিন্তু ViewModel নতুন, singleton নতুন, static variable খালি। শুধু `rememberSaveable` আর `SavedStateHandle`-এ রাখা জিনিস ফেরত আসে।

Flutter-এ এটা সাধারণত app-এর "cold start" হিসেবে ঘটে, আর বেশিরভাগ app শুরু থেকে খোলে। Android-এ native app-এর কাছে system আশা করে, সে ঠিক আগের জায়গা থেকে চলবে।

```kotlin
@HiltViewModel
class EditNoteViewModel @Inject constructor(
    private val savedState: SavedStateHandle,
    private val repo: NotesRepository,
) : ViewModel() {

    val draft: StateFlow<String> = savedState.getStateFlow("draft", "")

    fun onDraftChange(text: String) {
        savedState["draft"] = text             // process মরলেও ফেরত আসবে
    }
}
```

**ফাঁদ:**
- **বড় data Bundle-এ রাখবেন না।** `SavedStateHandle` আর `rememberSaveable` Bundle-এ save হয়, যার সীমা আছে (পুরো transaction মিলিয়ে মোটামুটি ১ MB)। Note-এর list না, শুধু id আর অর্ধেক লেখা text। List database থেকে আবার আসবে।
- **"Splash-এ সব load করি, বাকিরা singleton থেকে পড়ে"** — এই pattern process death-এ crash করে। কারণ app সরাসরি ভেতরের screen-এ খোলে, splash চলেই না।

**নিজে test করুন:**
1. App চালান, একটা note-এ কিছু লিখুন, তারপর home চাপুন।
2. Terminal-এ চালান: `adb shell am kill com.byteonyx.notes`
3. Recent apps থেকে app-টা আবার খুলুন।

যা যা হারাল, সেগুলোই bug। Developer options-এ **"Don't keep activities"** চালু করেও প্রায় একই ধরনের test করা যায়।

> **মনে রাখুন**
> - Rotation-এ Activity মরে, ViewModel বাঁচে। Process death-এ দুজনেই মরে।
> - `remember` < `rememberSaveable` < ViewModel < `SavedStateHandle` < database — কোনটা কতটা টেকে।
> - Bundle-এ শুধু ছোট জিনিস। বড় data database থেকে।
> - `adb shell am kill` দিয়ে প্রতিটা screen test করুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Configuration change-এ ViewModel বাঁচে, কারণ ViewModelStore নতুন Activity-কে দেওয়া হয়। কিন্তু process death-এ ViewModel-ও যায়। তাই আমি আসল data database-এ রাখি, আর user-এর অর্ধেক কাজ — যেমন draft বা search query — `SavedStateHandle`-এ। আর `adb shell am kill` দিয়ে test করি।"
> - *English:* "A ViewModel survives configuration changes because the ViewModelStore is handed to the new Activity, but it doesn't survive process death. So I keep real data in the database and the user's in-progress work, like a draft or a search query, in `SavedStateHandle`. I test it with `adb shell am kill`."

[উপরে ফিরুন](#toc)

---

## <a id="ch6"></a>৬. Jetpack Compose — Widget-এর জায়গায় Composable

এবার আসল আনন্দের অধ্যায়। আপনি যখন Java-তে Android করতেন, UI মানে ছিল XML, `findViewById`, আর হাতে হাতে `textView.setText()`। Compose এসে সেই পুরো জগৎ বাদ দিয়েছে, আর যে পথে এসেছে সেটা আপনার খুব চেনা: **UI = f(state)।** State বদলান, framework নিজে UI-র দরকারি অংশ আবার আঁকবে।

এই অধ্যায়ে আপনার Flutter-এর অভিজ্ঞতা সবচেয়ে বেশি কাজে লাগবে। প্রায় প্রতিটা widget-এর একটা জোড়া এখানে আছে।

### <a id="ch6-1"></a>৬.১ Widget → Composable

**এক লাইনে:** Widget class আর তার `build()`-এর জায়গায় একটা function, যার মাথায় `@Composable`।

**Flutter-এ:**

```dart
class NoteCard extends StatelessWidget {
  const NoteCard({super.key, required this.note, required this.onTap});
  final Note note;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(title: Text(note.title), subtitle: Text(note.preview), onTap: onTap),
    );
  }
}
```

**Compose-এ:**

```kotlin
@Composable
fun NoteCard(note: Note, onClick: () -> Unit, modifier: Modifier = Modifier) {
    Card(onClick = onClick, modifier = modifier) {
        ListItem(
            headlineContent = { Text(note.title) },
            supportingContent = { Text(note.preview) },
        )
    }
}
```

**কী মিলল, কী আলাদা:**

| Flutter | Compose |
|---|---|
| Widget class + `build()` | `@Composable` function |
| `build()` widget ফেরত দেয় | Composable কিছু ফেরত দেয় না — call করলেই UI-তে বসে যায় |
| constructor parameter | function parameter |
| `child:` / `children:` | trailing lambda — `Card { ... }` |
| `const` দিয়ে rebuild এড়ানো | Compiler নিজে বোঝে কোন function skip করা যায় |
| `StatelessWidget` | parameter নেওয়া সাধারণ composable |
| `StatefulWidget` | ভেতরে `remember { mutableStateOf() }` ([৬.৫](#ch6-5)) |
| `Key` | `key(id) { }`, list-এ `items(key = { it.id })` |

**নামের নিয়ম:** UI বসায় এমন composable — বড় হাতের noun: `NoteCard`। Value ফেরত দেয় এমন — ছোট হাতের: `rememberScrollState()`।

**কোথা থেকে call করা যায়:** শুধু আরেকটা composable-এর ভেতর থেকে। `onClick`-এর ভেতর থেকে না — ওটা সাধারণ lambda। Flutter-এ `onPressed`-এর ভেতরে widget বানিয়ে লাভ নেই, এখানে compiler-ই আটকায়।

**ভেতরে কীভাবে কাজ করে — তিন phase:** প্রতিটা frame-এ Compose তিন ধাপে কাজ করে, Flutter-এর build → layout → paint-এর মতো:
1. **Composition** — কী দেখাবে (আপনার function চলে)
2. **Layout** — মাপ আর জায়গা
3. **Drawing** — আঁকা

State কোন phase-এ পড়া হচ্ছে, তার উপর নির্ভর করে বাকি phase skip হতে পারে। Performance-এ এটা কাজে লাগবে ([৬.১৩](#ch6-13))।

[উপরে ফিরুন](#toc)

### <a id="ch6-2"></a>৬.২ Layout

**এক লাইনে:** `Column`, `Row` একই নামে আছে। `Stack` হলো `Box`। আর `Expanded`, `Padding`, `SizedBox` সব Modifier হয়ে গেছে।

**Notes app-এর একটা header, দুই পাশে:**

```dart
Padding(
  padding: const EdgeInsets.all(16),
  child: Row(
    crossAxisAlignment: CrossAxisAlignment.center,
    children: [
      const CircleAvatar(child: Icon(Icons.note)),
      const SizedBox(width: 12),
      Expanded(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [Text('আমার Notes', style: textTheme.titleMedium), Text('$count টা note')],
        ),
      ),
      IconButton(icon: const Icon(Icons.search), onPressed: onSearch),
    ],
  ),
)
```

```kotlin
Row(
    modifier = Modifier.fillMaxWidth().padding(16.dp),
    verticalAlignment = Alignment.CenterVertically,
    horizontalArrangement = Arrangement.spacedBy(12.dp),      // সব children-এর মাঝে ফাঁক
) {
    Icon(Icons.Default.Edit, contentDescription = null)
    Column(modifier = Modifier.weight(1f)) {                  // Expanded
        Text("আমার Notes", style = MaterialTheme.typography.titleMedium)
        Text("$count টা note")
    }
    IconButton(onClick = onSearch) { Icon(Icons.Default.Search, contentDescription = "খুঁজুন") }
}
```

| Flutter | Compose |
|---|---|
| `Column`, `Row` | `Column`, `Row` |
| `Stack` + `Positioned` / `Align` | `Box` + `Modifier.align()` |
| `Expanded` / `Flexible` | `Modifier.weight(1f)` |
| `SizedBox(height: 16)` | `Spacer(Modifier.height(16.dp))` |
| children-এর মাঝে বারবার `SizedBox`, বা `spacing:` | `Arrangement.spacedBy(12.dp)` |
| `mainAxisAlignment` | `verticalArrangement` (Column) / `horizontalArrangement` (Row) |
| `crossAxisAlignment` | `horizontalAlignment` (Column) / `verticalAlignment` (Row) |
| `Center` | `Box(contentAlignment = Alignment.Center)` |
| `Wrap` | `FlowRow` |
| `LayoutBuilder` | `BoxWithConstraints` |
| `Scaffold`, `AppBar`, `FloatingActionButton` | `Scaffold`, `TopAppBar`, `FloatingActionButton` |
| `ListTile`, `Card` | `ListItem`, `Card` |
| `SafeArea` | Scaffold-এর `innerPadding`, বা `Modifier.safeDrawingPadding()` |
| logical pixel | `dp` (text-এ `sp`) |

**Scaffold:**

```kotlin
Scaffold(
    topBar = { TopAppBar(title = { Text("Notes") }) },
    floatingActionButton = {
        FloatingActionButton(onClick = onAdd) { Icon(Icons.Default.Add, contentDescription = "নতুন note") }
    },
) { innerPadding ->
    NotesList(notes, modifier = Modifier.padding(innerPadding))
}
```

**ফাঁদ:** নতুন Android-এ (targetSdk 35+) app default-এ পুরো screen জুড়ে আঁকে — status bar আর navigation bar-এর নিচেও (edge-to-edge)। `innerPadding` না দিলে content bar-এর নিচে ঢাকা পড়বে। Flutter-এর `SafeArea` যে কাজ করত, এখানে `innerPadding` সেই কাজ করে।

[উপরে ফিরুন](#toc)

### <a id="ch6-3"></a>৬.৩ Wrapper widget → Modifier

**এক লাইনে:** Flutter-এ padding, size, রং, tap — প্রতিটার জন্য একটা wrapper widget। Compose-এ এগুলো সব একটা chain: **Modifier**।

**Flutter-এ — গভীর tree:**

```dart
GestureDetector(
  onTap: onTap,
  child: Container(
    color: Colors.yellow,
    padding: const EdgeInsets.all(16),
    child: Text(note.title),
  ),
)
```

**Compose-এ — একটা লাইন:**

```kotlin
Text(
    note.title,
    modifier = Modifier
        .clickable { onTap() }
        .background(Color.Yellow)
        .padding(16.dp),
)
```

**ক্রম গুরুত্বপূর্ণ** — Modifier বাইরে থেকে ভেতরে কাজ করে, ঠিক Flutter-এর wrapper-এর মতো:

```kotlin
Modifier.padding(16.dp).background(Color.Yellow)   // = Padding(child: Container(color: yellow))
Modifier.background(Color.Yellow).padding(16.dp)   // = Container(color: yellow, padding: 16)
```

প্রথমটায় হলুদ অংশ ছোট, চারপাশে ফাঁকা। দ্বিতীয়টায় ফাঁকটাও হলুদ। একইভাবে `clickable` আগে দিলে tap-এর জায়গা বড়, পরে দিলে ছোট।

**Best approach — modifier parameter-এর নিয়ম:** প্রতিটা reusable composable একটা `modifier: Modifier = Modifier` নেবে, আর সেটা নিজের root element-এ প্রথমে লাগাবে। তাহলে caller বাইরে থেকে size, padding দিতে পারে। Compose-এর সবচেয়ে মানা convention এটা — code review-এ এটা না থাকলে প্রশ্ন আসবে।

[উপরে ফিরুন](#toc)

### <a id="ch6-4"></a>৬.৪ `ListView.builder` → `LazyColumn`

**এক লাইনে:** `LazyColumn` শুধু screen-এ দেখা item-গুলো বানায় — ঠিক `ListView.builder`-এর মতো। পুরনো Android-এর `RecyclerView` + Adapter + ViewHolder-এর পুরো ঝামেলা এখানে এক function-এ।

**Flutter-এ:**

```dart
ListView.builder(
  padding: const EdgeInsets.all(16),
  itemCount: notes.length,
  itemBuilder: (context, i) => NoteCard(key: ValueKey(notes[i].id), note: notes[i], onTap: () => open(notes[i])),
)
```

**Compose-এ:**

```kotlin
LazyColumn(
    contentPadding = PaddingValues(16.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp),
) {
    item { Text("পিন করা", style = MaterialTheme.typography.titleSmall) }     // একটা header

    items(items = notes, key = { it.id }) { note ->                           // ValueKey(id)
        NoteCard(note = note, onClick = { open(note) })
    }
}
```

| Flutter | Compose |
|---|---|
| `ListView.builder` | `LazyColumn { items() }` |
| horizontal `ListView` | `LazyRow` |
| `GridView.builder` | `LazyVerticalGrid` |
| `CustomScrollView` + slivers | `LazyColumn`-এ `item {}`, `stickyHeader {}` |
| `PageView` | `HorizontalPager` |
| `ScrollController` | `rememberLazyListState()` |
| `SingleChildScrollView(child: Column)` | `Column(Modifier.verticalScroll(rememberScrollState()))` |

- `LazyColumn`-এর `{ }`-এর ভেতরে composable না, একটা DSL — তাই সেখানে `item {}` আর `items()`।
- **`key` দিন।** না দিলে item সরলে তার state (যেমন expand করা কি না) ভুল item-এ চলে যায়, আর animation ভুল হয় — Flutter-এ `Key` না দেওয়ার সমস্যার মতোই।
- আলাদা ধরনের item থাকলে `contentType` দিন — Compose তখন ভেতরের জিনিস ভালোভাবে reuse করতে পারে।

**ফাঁদ:** `LazyColumn`-এর ভেতরে একই দিকের আরেকটা `LazyColumn` দেবেন না — crash করে, কারণ ভেতরেরটা অসীম উচ্চতা পায়। Flutter-এ `ListView`-এর ভেতরে `ListView` দিলে "unbounded height" error-এর মতো।

[উপরে ফিরুন](#toc)

### <a id="ch6-5"></a>৬.৫ `setState` → `mutableStateOf`

**এক লাইনে:** `StatefulWidget`-এর field + `setState`-এর জায়গায় `remember { mutableStateOf() }`। Value বদলালেই UI আবার আঁকা হয়, আলাদা call লাগে না।

**Flutter-এ:**

```dart
class PinButton extends StatefulWidget {
  const PinButton({super.key});
  @override
  State<PinButton> createState() => _PinButtonState();
}

class _PinButtonState extends State<PinButton> {
  bool pinned = false;

  @override
  Widget build(BuildContext context) => IconButton(
        icon: Icon(pinned ? Icons.push_pin : Icons.push_pin_outlined),
        onPressed: () => setState(() => pinned = !pinned),
      );
}
```

**Compose-এ:**

```kotlin
@Composable
fun PinButton() {
    var pinned by remember { mutableStateOf(false) }
    // PushPin icon আসে material-icons-extended dependency থেকে

    IconButton(onClick = { pinned = !pinned }) {                       // setState লাগে না
        Icon(
            if (pinned) Icons.Filled.PushPin else Icons.Outlined.PushPin,
            contentDescription = "পিন",
        )
    }
}
```

দুইটা আলাদা জিনিস একসাথে কাজ করছে:

- **`mutableStateOf(false)`** — একটা observable box। Compose মনে রাখে, কোন composable এই box পড়েছে। Value বদলালে শুধু তারাই আবার চলে।
- **`remember { }`** — box-টাকে বাঁচিয়ে রাখে। Flutter-এ `State` object নিজেই বাঁচে, তাই field থেকে যায়। Compose-এ function বারবার চলে। `remember` ছাড়া প্রতিবার নতুন box হতো, আর `pinned` সবসময় `false` থাকত।

**ভেতরে কীভাবে কাজ করে — recomposition বনাম rebuild:**

| | Flutter | Compose |
|---|---|---|
| কে আবার চলে | `setState` যে widget-এ, তার `build()` আর নিচের subtree | শুধু যে composable box-টা পড়েছে, আর যার parameter বদলেছে |
| Skip কীভাবে | `const`, ছোট widget-এ ভাগ করা | Compiler: parameter আগের মতো থাকলে skip |
| ক্রম | ধারাবাহিক | যেকোনো ক্রমে, বারবার, মাঝপথে বাতিলও হতে পারে |

শেষ লাইনটা থেকে সবচেয়ে জরুরি নিয়ম: **composable-এর body-তে side effect দেবেন না।** Network call, analytics, বাইরের variable বদলানো সরাসরি body-তে লিখলে প্রতিটা recomposition-এ চলবে — হয়তো সেকেন্ডে ৬০ বার। Flutter-এ `build()`-এ API call না করার নিয়মটা এখানে আরও কড়া। Side effect-এর জন্য আলাদা API ([৬.৭](#ch6-7))।

**`rememberSaveable`** — rotation আর process death-এও বাঁচে ([৫.৩](#ch5-3)):

```kotlin
var draft by rememberSaveable { mutableStateOf("") }
```

**ফাঁদ — list state:** `mutableStateOf(mutableListOf<Note>())`-এ `add()` করলে Compose বুঝতে পারে না, কারণ box-এর ভেতরের list object একই থাকে। Flutter-এ list-এ `add` করে `setState` না দেওয়ার মতো। নতুন list দিন (`notes = notes + newNote`), অথবা `mutableStateListOf()`।

[উপরে ফিরুন](#toc)

### <a id="ch6-6"></a>৬.৬ Lifting state up

**এক লাইনে:** Flutter-এর "lift state up" Compose-এ **state hoisting** — composable নিজে state না রেখে value আর callback নেয়।

**Flutter-এ:**

```dart
class PinButton extends StatelessWidget {
  const PinButton({super.key, required this.pinned, required this.onChanged});
  final bool pinned;
  final ValueChanged<bool> onChanged;
  // ...
}
```

**Compose-এ:**

```kotlin
@Composable
fun PinButton(
    pinned: Boolean,                         // state নিচে আসে
    onPinnedChange: (Boolean) -> Unit,       // event উপরে যায়
    modifier: Modifier = Modifier,
) {
    IconButton(onClick = { onPinnedChange(!pinned) }, modifier = modifier) {
        Icon(if (pinned) Icons.Filled.PushPin else Icons.Outlined.PushPin, contentDescription = "পিন")
    }
}
```

একই চিন্তা, একই লাভ: stateless composable reuse, preview আর test করা সহজ। এই pattern-এর নাম **unidirectional data flow (UDF)** — state উপর থেকে নিচে, event নিচ থেকে উপরে। Bloc-এ আপনি ঠিক এটাই করতেন: state `BlocBuilder` দিয়ে নিচে, event `add()` দিয়ে উপরে।

**কতটা উপরে তুলবেন:** যারা এই state পড়ে বা বদলায়, তাদের সবচেয়ে কাছের common parent পর্যন্ত। Business logic থাকলে (note save করা) ViewModel পর্যন্ত ([৮](#ch8))।

[উপরে ফিরুন](#toc)

### <a id="ch6-7"></a>৬.৭ `initState`, `dispose`, `StreamBuilder`

**এক লাইনে:** Widget-এর lifecycle method-এর জায়গায় Compose-এ "effect" — composable screen-এ এলে চলে, চলে গেলে পরিষ্কার হয়।

| Flutter | Compose | কখন চলে |
|---|---|---|
| `initState`-এ async কাজ | `LaunchedEffect(Unit) { }` | প্রথম screen-এ এলে, একবার। ভেতরে suspend code চলে। |
| `didUpdateWidget` (id বদলালে) | `LaunchedEffect(noteId) { }` | Key বদলালে আগেরটা বাতিল, নতুন করে চলে |
| `initState` + `dispose` | `DisposableEffect(key) { onDispose { } }` | কিছু register, পরে unregister |
| `onPressed`-এ async কাজ | `rememberCoroutineScope()` → `scope.launch { }` | Callback থেকে coroutine |
| `StreamBuilder` | `flow.collectAsStateWithLifecycle()` | Flow → state |
| `FutureBuilder` | `produceState { value = load() }` | Suspend কাজের ফল → state |
| হাতে cache করা হিসাব | `derivedStateOf { }` | অন্য state থেকে হিসাব, যেটা কম বদলায় |

**Flutter-এ:**

```dart
class _NoteScreenState extends State<NoteScreen> {
  @override
  void initState() {
    super.initState();
    context.read<NoteCubit>().load(widget.noteId);
  }

  @override
  void didUpdateWidget(NoteScreen old) {
    super.didUpdateWidget(old);
    if (old.noteId != widget.noteId) context.read<NoteCubit>().load(widget.noteId);
  }
}
```

**Compose-এ — দুইটা method এক effect-এ:**

```kotlin
@Composable
fun NoteScreen(noteId: String, viewModel: NoteViewModel) {
    LaunchedEffect(noteId) {              // প্রথমবার, আর noteId বদলালে আবার
        viewModel.load(noteId)
    }

    val scope = rememberCoroutineScope()
    val snackbar = remember { SnackbarHostState() }
    Button(onClick = { scope.launch { snackbar.showSnackbar("Saved") } }) { Text("Save") }
}
```

**`derivedStateOf` কখন:** input অনেক ঘন ঘন বদলায়, ফল কম বদলায়। Scroll position প্রতি pixel-এ বদলায়, কিন্তু "উপরে যাও" button দেখাবে কি না, বদলায় একবার:

```kotlin
val listState = rememberLazyListState()
val showScrollToTop by remember { derivedStateOf { listState.firstVisibleItemIndex > 0 } }
```

**Best approach:** Screen-এর data load ViewModel-এর `init` বা `stateIn`-এ করুন, `LaunchedEffect`-এ না। `LaunchedEffect`-এ load করলে rotation-এ আবার load হয়, কারণ composable নতুন করে screen-এ আসে। `LaunchedEffect` রাখুন UI-র কাজের জন্য: snackbar দেখানো, animation শুরু, focus দেওয়া।

[উপরে ফিরুন](#toc)

### <a id="ch6-8"></a>৬.৮ `InheritedWidget` → `CompositionLocal`

**এক লাইনে:** Tree-র উপর থেকে data নিচে পাঠানো — `Theme.of(context)`, Provider-এর মতো — Compose-এ `CompositionLocal` দিয়ে।

**Flutter-এ:**

```dart
Provider<Analytics>.value(value: analytics, child: const NotesApp());
// নিচে কোথাও
context.read<Analytics>().log('note_opened');
```

**Compose-এ:**

```kotlin
val LocalAnalytics = staticCompositionLocalOf<Analytics> { error("Analytics দেওয়া হয়নি") }

CompositionLocalProvider(LocalAnalytics provides analytics) {
    NotesApp()
}

// নিচে কোথাও
val analytics = LocalAnalytics.current
```

Built-in কিছু: `LocalContext`, `LocalLifecycleOwner`, `LocalDensity`, `LocalConfiguration`। `MaterialTheme` নিজেও ভেতরে এটাই ব্যবহার করে।

**ফাঁদ:** এটা DI-র বিকল্প না। Repository বা ViewModel এটা দিয়ে পাঠাবেন না — তখন কোন composable কীসের উপর নির্ভর করে, signature দেখে বোঝা যায় না। এটা theme, density-র মতো "পরিবেশ"-এর জন্য। Business জিনিস parameter বা Hilt দিয়ে।

`compositionLocalOf` বনাম `staticCompositionLocalOf`: প্রথমটায় value বদলালে শুধু যারা পড়েছে তারা আবার চলে। দ্বিতীয়টায় পুরো subtree, কিন্তু পড়ার খরচ কম। প্রায় কখনো বদলায় না এমন জিনিসে `static`।

[উপরে ফিরুন](#toc)

### <a id="ch6-9"></a>৬.৯ Theme

**এক লাইনে:** Material 3-এর token-এর নাম Flutter আর Compose-এ প্রায় হুবহু এক। আপনার theme system সরাসরি চলে আসবে।

**Flutter-এ:**

```dart
MaterialApp(
  theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: brandOrange)),
  darkTheme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: brandOrange, brightness: Brightness.dark)),
);
Theme.of(context).colorScheme.primary;
Theme.of(context).textTheme.titleLarge;
```

**Compose-এ:**

```kotlin
@Composable
fun NotesTheme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
    val colors = if (darkTheme) darkColorScheme(primary = BrandOrange) else lightColorScheme(primary = BrandOrange)
    MaterialTheme(colorScheme = colors, typography = AppTypography, content = content)
}

MaterialTheme.colorScheme.primary
MaterialTheme.typography.titleLarge
```

| Flutter | Compose |
|---|---|
| `ThemeData` | `MaterialTheme(colorScheme, typography, shapes)` |
| `ColorScheme.fromSeed` | নিজের `lightColorScheme(...)`, বা Android 12+ এ wallpaper থেকে `dynamicLightColorScheme(context)` |
| `Theme.of(context)` | `MaterialTheme.colorScheme` / `.typography` |
| `ThemeExtension` | নিজের `CompositionLocal` |
| `MediaQuery.platformBrightnessOf` | `isSystemInDarkTheme()` |

**ফাঁদ:** `res/values/themes.xml`-এও একটা theme থাকে। সেটা শুধু window-এর — Compose চালু হওয়ার আগের মুহূর্তের background আর splash। Compose-এর রং আসে `MaterialTheme` থেকে। দুই জায়গার রং না মিললে app খোলার সময় এক ঝলক অন্য রং দেখা যায়।

[উপরে ফিরুন](#toc)

### <a id="ch6-10"></a>৬.১০ TextField

**এক লাইনে:** Flutter-এ `TextEditingController` text রাখে। Compose-এর সাধারণ `TextField`-এ text রাখেন আপনি — value দেন, `onValueChange`-এ নতুন value নেন।

**Flutter-এ:**

```dart
final _title = TextEditingController();
TextField(controller: _title, decoration: const InputDecoration(labelText: 'শিরোনাম'));
// পড়তে: _title.text
```

**Compose-এ:**

```kotlin
var title by rememberSaveable { mutableStateOf("") }

OutlinedTextField(
    value = title,
    onValueChange = { title = it },             // না লিখলে টাইপ করলেও কিছু বদলাবে না
    label = { Text("শিরোনাম") },
    singleLine = true,
    keyboardOptions = KeyboardOptions(imeAction = ImeAction.Next),
)
```

- **ফাঁদ:** `onValueChange`-এ value বসাতে ভুলে গেলে field-এ কিছুই লেখা যায় না। Flutter থেকে আসা সবাই প্রথম দিন এখানে আটকায়।
- **ফাঁদ:** ViewModel-এ text রাখলে update synchronous রাখুন। Async করে (debounce বা network-এর পরে) value ফেরত দিলে cursor লাফায়, অক্ষর হারায়।
- **নতুন API:** `rememberTextFieldState()` আর `TextFieldState`-ভিত্তিক `TextField` — এটা `TextEditingController`-এর অনেক কাছাকাছি, আর উপরের cursor সমস্যা নেই। নতুন code-এ এটা দেখে নিন।
- Focus: `FocusNode` → `FocusRequester`। Keyboard বন্ধ: `LocalFocusManager.current.clearFocus()`।

[উপরে ফিরুন](#toc)

### <a id="ch6-11"></a>৬.১১ Animation

**এক লাইনে:** Flutter-এর implicit animation-এর মতোই — target value বদলান, animation নিজে হয়।

**Flutter-এ:**

```dart
AnimatedContainer(
  duration: const Duration(milliseconds: 300),
  height: expanded ? 200 : 80,
  child: NoteBody(note),
);
AnimatedOpacity(opacity: showHint ? 1 : 0, duration: const Duration(milliseconds: 200), child: hint);
```

**Compose-এ:**

```kotlin
val height by animateDpAsState(if (expanded) 200.dp else 80.dp, label = "height")
NoteBody(note, modifier = Modifier.height(height))

AnimatedVisibility(visible = showHint) { Hint() }
```

| Flutter | Compose |
|---|---|
| `AnimatedContainer`, `TweenAnimationBuilder` | `animateDpAsState`, `animateColorAsState`, `animateFloatAsState` |
| `AnimatedOpacity` (দেখানো/লুকানো) | `AnimatedVisibility` |
| `AnimatedSwitcher` | `AnimatedContent`, `Crossfade` |
| `AnimatedSize` | `Modifier.animateContentSize()` |
| `AnimationController` | `Animatable`, `updateTransition` |
| `Hero` | Shared element (`SharedTransitionLayout`) |
| `AnimatedList` | `LazyColumn`-এর item-এ `Modifier.animateItem()` |
| `Curves.easeInOut` | `tween(300, easing = FastOutSlowInEasing)`, `spring()` |

Compose-এর default প্রায়ই `spring()` — physics-ভিত্তিক, তাই মাঝপথে target বদলালেও মসৃণভাবে ঘুরে যায়।

[উপরে ফিরুন](#toc)

### <a id="ch6-12"></a>৬.১২ Hot reload নেই: Preview

**এক লাইনে:** Flutter-এর মতো পুরো hot reload Compose-এ নেই। এটাই সবচেয়ে বড় অভ্যাসের বদল। তার জায়গায় `@Preview`।

```kotlin
@Preview(showBackground = true)
@Preview(uiMode = Configuration.UI_MODE_NIGHT_YES, name = "Dark")
@Composable
private fun NoteCardPreview() {
    NotesTheme { NoteCard(note = sampleNote, onClick = {}) }
}
```

- **Preview** — Android Studio-তে app না চালিয়েই composable দেখা, light-dark, বড় font, ছোট screen পাশাপাশি। ভালো চলে stateless composable-এ। এটাই state hoisting-এর আরেক বড় লাভ — যে composable ViewModel চায়, তার preview বানানো কঠিন।
- **Live Edit** — চলমান app-এ কিছু বদল সাথে সাথে দেখায়। Text, রং, সংখ্যা বদলে ভালো কাজ করে, কিন্তু Flutter-এর hot reload-এর মতো সব জায়গায় না।
- **Layout Inspector** — Flutter DevTools-এর widget inspector। এখানে recomposition count দেখা যায়: কোন composable কতবার আবার চলছে।

**Best approach:** প্রতিটা screen-কে দুই ভাগে লিখুন: `NotesRoute` (ViewModel নেয়) আর `NotesScreen` (শুধু state আর callback নেয়)। Preview আর test হবে `NotesScreen`-এর ([৮.৩](#ch8-3))।

[উপরে ফিরুন](#toc)

### <a id="ch6-13"></a>৬.১৩ Performance

শুরুতে এই কয়েকটা নিয়ম মানলেই বেশিরভাগ সমস্যা থাকে না:

1. **Release build-এ মাপুন।** Debug-এ Compose অনেক ধীর। Flutter-এ profile mode-এ মাপার মতো।
2. **List-এ `key`** ([৬.৪](#ch6-4))।
3. **দামি হিসাব `remember` করুন:** `val sorted = remember(notes) { notes.sortedBy { it.title } }`। নইলে প্রতি recomposition-এ sort।
4. **ঘন ঘন বদলানো state যত দেরিতে সম্ভব পড়ুন।** Scroll বা animation-এর value দিয়ে position বদলাতে lambda modifier: `Modifier.offset { IntOffset(0, offset.roundToInt()) }`। Value তখন পড়া হয় layout phase-এ, composition আবার চলে না।
5. **Immutable state।** UI state-এ `data class` আর `val`। Kotlin 2.0.20 থেকে "strong skipping" default চালু, তাই এখন বেশিরভাগ ক্ষেত্রে skip নিজেই ঠিকমতো হয়। Flutter-এ immutable state রাখার অভ্যাস এখানেও সঠিক।
6. **Baseline Profile।** App-এর গুরুত্বপূর্ণ code আগে থেকে compile করিয়ে রাখে। Compose app-এর প্রথম launch আর scroll-এ বড় পার্থক্য আনে।

> **মনে রাখুন**
> - Widget → `@Composable` function। `child` → trailing lambda। Wrapper widget → Modifier, আর Modifier-এর ক্রম গুরুত্বপূর্ণ।
> - `setState` → `remember { mutableStateOf() }`। `remember` না দিলে state হারায়।
> - Body-তে side effect না — `LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope`।
> - State hoisting = lift state up = UDF। Route আর Screen আলাদা।
> - Hot reload নেই, Preview আছে।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Compose-এর চিন্তা Flutter-এর মতোই — UI হলো state-এর function। আমি screen-কে stateless রাখি, state hoist করি, আর side effect শুধু effect API-তে দিই, কারণ recomposition যেকোনো সময়, বারবার হতে পারে। Performance-এ list-এ key দিই, দামি হিসাব remember করি, আর release build-এ মাপি।"
> - *English:* "Compose thinks like Flutter — UI is a function of state. I keep screens stateless, hoist state, and put side effects only in effect APIs, because recomposition can happen at any time and many times. For performance, I add keys to lists, remember expensive work, and measure on a release build."

[উপরে ফিরুন](#toc)

---

## <a id="ch7"></a>৭. Navigation — `go_router`-এর জায়গায়

আগে Android-এ নতুন screen মানে নতুন Activity আর `startActivity(intent)`। Data পাঠাতে `intent.putExtra()`, ফল আনতে `onActivityResult`। এখন সেই দিন শেষ। একটা Activity-র ভেতরে route table, ঠিক `go_router`-এর মতো।

**এক লাইনে:** `GoRouter`-এর route list → `NavHost`। `context.push()` → `navController.navigate()`। Path string-এর বদলে type-safe Kotlin class।

**Flutter-এ (go_router):**

```dart
final router = GoRouter(routes: [
  GoRoute(path: '/', builder: (_, __) => const NotesScreen()),
  GoRoute(
    path: '/note/:id',
    builder: (_, state) => NoteScreen(noteId: state.pathParameters['id']!),
  ),
]);

context.push('/note/42');
context.pop();
```

**Compose-এ (Navigation Compose):**

```kotlin
@Serializable object NotesList
@Serializable data class NoteDetail(val noteId: String)

@Composable
fun NotesNavHost(navController: NavHostController = rememberNavController()) {
    NavHost(navController = navController, startDestination = NotesList) {
        composable<NotesList> {
            NotesRoute(onNoteClick = { id -> navController.navigate(NoteDetail(id)) })
        }
        composable<NoteDetail> { entry ->
            val args = entry.toRoute<NoteDetail>()
            NoteDetailRoute(noteId = args.noteId, onBack = { navController.popBackStack() })
        }
    }
}
```

| go_router | Navigation Compose |
|---|---|
| `GoRouter(routes: [...])` | `NavHost { composable<Route> { } }` |
| `'/note/:id'` path | `@Serializable data class NoteDetail(val noteId: String)` |
| `state.pathParameters['id']!` | `entry.toRoute<NoteDetail>().noteId` — type-safe |
| `context.push()` / `go()` | `navController.navigate(route)` |
| `context.pop()` | `navController.popBackStack()` |
| `redirect` (login check) | start destination বদলানো, বা ViewModel-এ check করে navigate |
| `StatefulShellRoute` (bottom nav) | `NavigationBar` + nested graph, `saveState` / `restoreState` |
| `PopScope` | `BackHandler { }` |

**কী আলাদা:**
- **Route হলো Kotlin class।** Argument-এর type compiler check করে। `int` চাইলে `String` দিতে পারবেন না। go_router-এর typed route-এর মতো, কিন্তু code generation ছাড়া।
- **প্রতিটা destination-এর নিজের ViewModel scope।** `NoteDetail` screen-এ `hiltViewModel()` নিলে সেই ViewModel ওই screen-এর। Screen back stack থেকে বের হলে ViewModel clear। ViewModel-এর ভেতরে argument পড়া: `savedStateHandle.toRoute<NoteDetail>()`।
- **System back button।** Android-এ system back (button বা gesture) আছে, iOS-এ নেই। Navigation library নিজে সামলায়। "Save না করে বের হবেন?" dialog লাগলে `BackHandler { }` — Flutter-এর `PopScope`।

**Best approach:**
- Screen-কে `navController` দেবেন না, শুধু callback (`onNoteClick`)। Navigation logic এক জায়গায় থাকে, screen preview আর test করা যায়। Flutter-এ widget-এর ভেতরে সরাসরি `context.go()` না লিখে callback দেওয়ার মতো।
- **Argument-এ শুধু id পাঠান, পুরো object না।** Argument Bundle-এ save হয়, যার সীমা আছে, আর process death-এর পরে পুরনো object ফেরত আসতে পারে। Id নিয়ে repository থেকে load করুন।

**Navigation 3:** ২০২৫-এর শেষে Navigation 3 নামে নতুন library stable হয়েছে। এখানে back stack একটা সাধারণ list, যেটা আপনি নিজে রাখেন আর বদলান (`rememberNavBackStack`, `NavDisplay`)। Flutter-এর Navigator 2.0-এর `pages` list-এর ধারণার কাছাকাছি। নতুন project-এ দুটোই দেখবেন। শিখতে Navigation Compose দিয়ে শুরু করুন, তারপর Nav3।

> **মনে রাখুন**
> - `GoRouter` → `NavHost`, path → `@Serializable` class, `push` → `navigate`।
> - প্রতিটা destination-এর নিজের ViewModel।
> - Screen-এ callback দিন, `navController` না। Argument-এ শুধু id।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি single-Activity-তে Navigation Compose নিই, type-safe route দিয়ে। Screen-কে navController না দিয়ে callback দিই, আর argument-এ শুধু id পাঠাই, যাতে process death-এর পরেও data repository থেকে ঠিকঠাক আসে।"
> - *English:* "I use Navigation Compose in a single Activity with type-safe routes. I pass callbacks to screens instead of the navController, and only pass ids as arguments, so after process death the data still comes correctly from the repository."

[উপরে ফিরুন](#toc)

---

## <a id="ch8"></a>৮. Architecture — Cubit থেকে ViewModel, `get_it` থেকে Hilt

আপনি Flutter-এ clean architecture ব্যবহার করেন। এই অধ্যায়ে তাই কোনো নতুন দর্শন নেই। Presentation, domain, data — layer একই। শুধু প্রতিটা layer-এর ইট আলাদা। Cubit-এর জায়গায় ViewModel, `get_it`-এর জায়গায় Hilt। আর একটা নতুন জিনিস: Android-এর ViewModel lifecycle জানে, Cubit জানত না।

### <a id="ch8-1"></a>৮.১ Layer একই থাকে

```
Flutter (আপনার এখনকার)                 Android
──────────────────────────────         ──────────────────────────────────────
presentation/                          ui/
  notes_screen.dart  (Widget)            NotesScreen.kt   (@Composable)
  notes_cubit.dart   (Cubit)             NotesViewModel.kt (ViewModel)
  notes_state.dart   (freezed)           NotesUiState.kt  (data class)
domain/                                domain/            (শুধু দরকার হলে)
  notes_repository.dart (abstract)       NotesRepository.kt (interface)
  delete_note.dart   (UseCase)           DeleteNoteUseCase.kt
data/                                  data/
  notes_repository_impl.dart             NotesRepositoryImpl.kt
  notes_api.dart     (dio/retrofit)      NotesApi.kt      (Retrofit)
  notes_dao.dart     (drift)             NoteDao.kt       (Room)
di/injection.dart    (get_it)          di/DataModule.kt   (Hilt)
```

**UseCase নিয়ে একটা কথা:** Google-এর architecture guide-এ domain layer **optional**। যে UseCase শুধু একটা repository method forward করে, সেটা বাড়তি layer। Business rule আছে, দুইটা repository মেলাতে হয়, বা কয়েকটা ViewModel একই logic চায় — তখনই UseCase বানান। এটা আপনার clean architecture-এর বিরুদ্ধে না, শুধু "প্রতিটা call-এ একটা UseCase" নিয়মটা এখানে চলে না।

[উপরে ফিরুন](#toc)

### <a id="ch8-2"></a>৮.২ Cubit → ViewModel

**এক লাইনে:** ViewModel হলো Cubit, কিন্তু rotation-এ বাঁচে, আর নিজের coroutine scope নিয়ে আসে।

**Flutter-এ:**

```dart
@freezed
class NotesState with _$NotesState {
  const factory NotesState({
    @Default([]) List<Note> notes,
    @Default(true) bool isLoading,
    String? error,
  }) = _NotesState;
}

class NotesCubit extends Cubit<NotesState> {
  NotesCubit(this._repo) : super(const NotesState()) {
    _sub = _repo.watchNotes().listen((notes) => emit(state.copyWith(notes: notes, isLoading: false)));
  }

  final NotesRepository _repo;
  late final StreamSubscription<List<Note>> _sub;

  Future<void> delete(String id) async {
    try {
      await _repo.delete(id);
    } catch (_) {
      emit(state.copyWith(error: 'মোছা যায়নি'));
    }
  }

  void errorShown() => emit(state.copyWith(error: null));

  @override
  Future<void> close() {
    _sub.cancel();
    return super.close();
  }
}
```

**Android-এ:**

```kotlin
data class NotesUiState(
    val notes: List<Note> = emptyList(),
    val isLoading: Boolean = true,
    val error: String? = null,
)

@HiltViewModel
class NotesViewModel @Inject constructor(
    private val repo: NotesRepository,
) : ViewModel() {

    private val error = MutableStateFlow<String?>(null)

    val uiState: StateFlow<NotesUiState> =
        combine(repo.observeNotes(), error) { notes, err ->
            NotesUiState(notes = notes, isLoading = false, error = err)
        }.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), NotesUiState())

    fun delete(id: String) {
        viewModelScope.launch {
            try {
                repo.delete(id)
            } catch (e: IOException) {
                error.value = "মোছা যায়নি"
            }
        }
    }

    fun errorShown() { error.value = null }
}
```

**কী মিলল, কী আলাদা:**

| Cubit | ViewModel |
|---|---|
| `Cubit<NotesState>` | `ViewModel` + `StateFlow<NotesUiState>` |
| `emit(state.copyWith(...))` | `_state.update { it.copy(...) }`, বা `combine` + `stateIn` |
| `close()`-এ subscription cancel | লাগে না — `viewModelScope` নিজে বন্ধ হয় |
| Widget dispose হলে Cubit-ও যায় | Rotation-এ বাঁচে, screen সত্যিই বন্ধ হলে যায় |
| freezed state | `data class` |

**দুই ধরনের লেখা ViewModel-এ:**
- **`combine` + `stateIn`** (উপরের মতো): state যখন বেশিরভাগ অন্য flow থেকে আসে — database, settings। Declarative, আর `WhileSubscribed` দিয়ে background-এ query নিজে থামে।
- **`MutableStateFlow` + `update {}`**: state যখন মূলত user-এর কাজে বদলায় — form, wizard। Cubit-এর `emit(copyWith)`-এর সবচেয়ে কাছের রূপ:

```kotlin
private val _uiState = MutableStateFlow(EditNoteUiState())
val uiState: StateFlow<EditNoteUiState> = _uiState.asStateFlow()

fun onTitleChange(title: String) = _uiState.update { it.copy(title = title) }
```

**ফাঁদ:**
- ViewModel-এ `Context`, View বা Activity রাখবেন না। ViewModel Activity-র চেয়ে বেশিদিন বাঁচে, তাই leak। String resource লাগলে UI-তে resolve করুন।
- `MutableStateFlow` বাইরে public রাখবেন না। তখন UI নিজে state বদলাতে পারে, UDF ভাঙে। Cubit-এ `emit` যেমন বাইরে থেকে call করা যায় না, তেমন।

[উপরে ফিরুন](#toc)

### <a id="ch8-3"></a>৮.৩ `BlocBuilder` → `collectAsStateWithLifecycle`

**এক লাইনে:** ViewModel-এর `StateFlow` Compose-এ পড়া হয় `collectAsStateWithLifecycle()` দিয়ে। Route-Screen ভাগ করে লিখুন।

**Flutter-এ:**

```dart
class NotesPage extends StatelessWidget {
  const NotesPage({super.key});
  @override
  Widget build(BuildContext context) => BlocProvider(
        create: (_) => getIt<NotesCubit>(),
        child: BlocBuilder<NotesCubit, NotesState>(
          builder: (context, state) => NotesView(
            state: state,
            onDelete: context.read<NotesCubit>().delete,
          ),
        ),
      );
}
```

**Android-এ:**

```kotlin
@Composable
fun NotesRoute(
    onNoteClick: (String) -> Unit,
    viewModel: NotesViewModel = hiltViewModel(),           // BlocProvider + getIt
) {
    val state by viewModel.uiState.collectAsStateWithLifecycle()   // BlocBuilder
    NotesScreen(state = state, onNoteClick = onNoteClick, onDelete = viewModel::delete)
}

@Composable
fun NotesScreen(state: NotesUiState, onNoteClick: (String) -> Unit, onDelete: (String) -> Unit) {
    // শুধু state দেখায় আর event পাঠায় — stateless, preview আর test করা যায়
}
```

`NotesRoute` = Flutter-এর `NotesPage` (provider বসায়)। `NotesScreen` = `NotesView` (শুধু দেখায়)।

**কেন `WithLifecycle`:** সাধারণ `collectAsState()` app background-এ গেলেও collect করতে থাকে। `collectAsStateWithLifecycle()` screen STARTED-এর নিচে গেলে থামে, ফিরলে আবার শুরু করে। `stateIn(WhileSubscribed(5_000))`-এর সাথে মিলে background-এ database query পর্যন্ত থেমে যায়। Flutter-এ `BlocBuilder` app background-এ গেলেও stream শুনতে থাকে।

[উপরে ফিরুন](#toc)

### <a id="ch8-4"></a>৮.৪ `BlocListener` → one-off event

**এক লাইনে:** Snackbar, navigation-এর মতো "একবার ঘটবে" কাজ — Google-এর পরামর্শ হলো এগুলোকেও state হিসেবে রাখা।

**Flutter-এ:**

```dart
BlocListener<NotesCubit, NotesState>(
  listenWhen: (prev, curr) => curr.error != null && prev.error != curr.error,
  listener: (context, state) {
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(state.error!)));
    context.read<NotesCubit>().errorShown();
  },
  child: ...,
);
```

**Android-এ:**

```kotlin
val snackbar = remember { SnackbarHostState() }

LaunchedEffect(state.error) {
    state.error?.let {
        snackbar.showSnackbar(it)
        onErrorShown()                   // দেখানো হলো, state থেকে মুছে দাও
    }
}
```

**কেন state, `SharedFlow` বা `Channel` না:** Event stream-এ পাঠালে, ঠিক সেই মুহূর্তে কেউ না শুনলে (rotation চলছে, app background-এ) event হারাতে পারে। State হারায় না — UI ফিরে এসে দেখে, error এখনো আছে, দেখায়, তারপর clear করে। অনেক team তবু `Channel` ব্যবহার করে। দুটোই দেখবেন, শুধু trade-off-টা জানুন।

[উপরে ফিরুন](#toc)

### <a id="ch8-5"></a>৮.৫ `get_it` → Hilt

**এক লাইনে:** Hilt হলো compile time-এ বানানো DI। `injectable`-এর annotation-এর মতো দেখতে, কিন্তু ভুল dependency build-এই ধরা পড়ে।

**Flutter-এ (get_it + injectable):**

```dart
@LazySingleton(as: NotesRepository)
class NotesRepositoryImpl implements NotesRepository {
  NotesRepositoryImpl(this._api, this._dao);
  final NotesApi _api;
  final NoteDao _dao;
}

@module
abstract class NetworkModule {
  @lazySingleton
  Dio dio() => Dio(BaseOptions(baseUrl: 'https://api.byteonyx.com/'));
}

@injectable
class NotesCubit extends Cubit<NotesState> { NotesCubit(this._repo) : super(...); ... }

// main(): configureDependencies();
```

**Android-এ (Hilt):**

```kotlin
class NotesRepositoryImpl @Inject constructor(              // @injectable
    private val api: NotesApi,
    private val dao: NoteDao,
) : NotesRepository

@Module
@InstallIn(SingletonComponent::class)
abstract class DataModule {
    @Binds @Singleton                                         // @LazySingleton(as: ...)
    abstract fun bindNotesRepository(impl: NotesRepositoryImpl): NotesRepository
}

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {                                        // @module
    @Provides @Singleton
    fun provideRetrofit(okHttp: OkHttpClient): Retrofit =
        Retrofit.Builder().baseUrl("https://api.byteonyx.com/").client(okHttp).build()

    @Provides @Singleton
    fun provideNotesApi(retrofit: Retrofit): NotesApi = retrofit.create(NotesApi::class.java)
}

@HiltViewModel                                                // @injectable Cubit
class NotesViewModel @Inject constructor(private val repo: NotesRepository) : ViewModel()

// শুরু: Application-এ @HiltAndroidApp, Activity-তে @AndroidEntryPoint
```

| injectable / get_it | Hilt |
|---|---|
| `@injectable` | `@Inject constructor` |
| `@lazySingleton` / `@singleton` | `@Singleton` |
| `@LazySingleton(as: Interface)` | `@Binds` |
| `@module` + method | `@Module` + `@Provides` |
| `configureDependencies()` | `@HiltAndroidApp` (code compile-এর সময় তৈরি) |
| `getIt<NotesCubit>()` | `hiltViewModel()` |
| scope / environment | Component: `SingletonComponent`, `ViewModelComponent`, `ActivityComponent` |
| `@Environment('test')` | test-এ `@TestInstallIn` দিয়ে module বদলানো |

**`@Binds` বনাম `@Provides`:** নিজের class, যার constructor-এ `@Inject` আছে, আর interface-এর সাথে জুড়তে হবে → `@Binds`। Library-র class (Retrofit, OkHttp, Room), যেটার constructor আপনার না → `@Provides`।

**Best approach:**
- Scope ভেবে দিন। OkHttp, Retrofit, database, repository — `@Singleton`। বাকিরা unscoped (প্রতিবার নতুন)। সবকিছু singleton করলে memory আর lock-এর খরচ বাড়ে।
- Interface তখনই, যখন লাগে — test-এ fake দেবেন, বা দুইটা implementation আছে। নইলে শুধু `@Inject constructor` দেওয়া class-ই যথেষ্ট, `@Binds` লাগে না।

> **মনে রাখুন**
> - Layer একই। Cubit → ViewModel, freezed state → data class, `get_it` → Hilt।
> - ViewModel rotation-এ বাঁচে আর নিজে coroutine বন্ধ করে।
> - `BlocBuilder` → `collectAsStateWithLifecycle()`। Route (ViewModel নেয়) আর Screen (stateless) আলাদা।
> - One-off event state হিসেবে রাখুন, দেখানোর পরে clear।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি UDF মানি: প্রতিটা screen-এর ViewModel একটা immutable UiState দেয় StateFlow হিসেবে, UI সেটা lifecycle-aware ভাবে collect করে, আর event function call হিসেবে পাঠায়। DI-তে Hilt নিই — Flutter-এ injectable যা করত, তাই, কিন্তু ভুল compile time-এ ধরা পড়ে। UseCase শুধু তখন বানাই, যখন সত্যিই business logic আছে।"
> - *English:* "I follow UDF: each screen's ViewModel exposes one immutable UiState as a StateFlow, the UI collects it in a lifecycle-aware way, and sends events as function calls. For DI I use Hilt — it does what injectable did in Flutter, but errors show up at compile time. I add a UseCase only when there is real business logic."

[উপরে ফিরুন](#toc)

---

## <a id="ch9"></a>৯. Data — network, JSON, database, storage

এই অধ্যায়ের প্রতিটা জিনিসের একটা Flutter যমজ আছে। আর মজার কথা হলো, অনেক Flutter package আসলে এই Android library-গুলো দেখেই বানানো — Flutter-এর `retrofit` package-এর নামই তার প্রমাণ। তাই এখানে আপনি সবচেয়ে দ্রুত চলবেন।

### <a id="ch9-1"></a>৯.১ `dio` → Retrofit + OkHttp

**এক লাইনে:** Retrofit হলো API-কে একটা interface হিসেবে লেখার library। OkHttp হলো তার নিচের HTTP client — dio-র interceptor-এর কাজ এখানে।

**Flutter-এ (dio + retrofit package):**

```dart
@RestApi(baseUrl: 'https://api.byteonyx.com/')
abstract class NotesApi {
  factory NotesApi(Dio dio) = _NotesApi;

  @GET('/notes')
  Future<List<NoteDto>> getNotes({@Query('since') int? since});

  @POST('/notes')
  Future<NoteDto> create(@Body() CreateNoteRequest body);
}

dio.interceptors.add(InterceptorsWrapper(
  onRequest: (options, handler) {
    options.headers['Authorization'] = 'Bearer ${tokens.access}';
    handler.next(options);
  },
));
```

**Android-এ:**

```kotlin
interface NotesApi {
    @GET("notes")
    suspend fun getNotes(@Query("since") since: Long? = null): List<NoteDto>

    @POST("notes")
    suspend fun create(@Body body: CreateNoteRequest): NoteDto
}

val okHttp = OkHttpClient.Builder()
    .addInterceptor { chain ->                                   // dio interceptor
        val request = chain.request().newBuilder()
            .header("Authorization", "Bearer ${tokens.access}")
            .build()
        chain.proceed(request)
    }
    .authenticator(TokenAuthenticator(tokens, authApi))           // 401 এলে refresh
    .build()
```

**কী মিলল, কী আলাদা:**

| dio / retrofit (Dart) | Retrofit + OkHttp |
|---|---|
| `@RestApi` abstract class + generated `_NotesApi` | `interface` — Retrofit runtime-এ নিজে বানায়, code generation নেই |
| `Future<List<NoteDto>>` | `suspend fun ...: List<NoteDto>` — নিজে background-এ চলে |
| `InterceptorsWrapper` | OkHttp `Interceptor` |
| `onError`-এ 401 ধরে refresh | `Authenticator` — শুধু 401-এর জন্য বানানো |
| `DioException` | `IOException` (network), `HttpException` (4xx/5xx) |
| `LogInterceptor` | `HttpLoggingInterceptor` |

**Token refresh — `Authenticator`:** Server 401 দিলে OkHttp নিজে `Authenticator`-কে ডাকে। সেখানে নতুন token নিয়ে নতুন request ফেরত দিলে OkHttp আবার পাঠায়। একসাথে পাঁচটা request 401 পেলে পাঁচবার refresh যাতে না হয়, `synchronized` দিয়ে একবারই refresh করুন, আর check করুন অন্য কেউ ইতিমধ্যে token বদলে দিয়েছে কি না।

**Best approach:** Repository-তে Retrofit-এর exception ধরে নিজের error type-এ বদলান। ViewModel যেন Retrofit বা `HttpException` না চেনে — ঠিক যেমন Flutter-এ `DioException` repository-র বাইরে যেতে দিতেন না।

[উপরে ফিরুন](#toc)

### <a id="ch9-2"></a>৯.২ `json_serializable` → kotlinx.serialization

**এক লাইনে:** `@JsonSerializable` + `build_runner`-এর জায়গায় `@Serializable` — compiler plugin নিজে code বানায়, আলাদা command লাগে না।

**Flutter-এ:**

```dart
@JsonSerializable()
class NoteDto {
  NoteDto({required this.id, required this.title, this.body});
  final String id;
  @JsonKey(name: 'note_title')
  final String title;
  final String? body;

  factory NoteDto.fromJson(Map<String, dynamic> json) => _$NoteDtoFromJson(json);
  Map<String, dynamic> toJson() => _$NoteDtoToJson(this);
}
```

**Android-এ:**

```kotlin
@Serializable
data class NoteDto(
    val id: String,
    @SerialName("note_title") val title: String,
    val body: String? = null,
)

val json = Json { ignoreUnknownKeys = true }
val dto = json.decodeFromString<NoteDto>(raw)
val text = json.encodeToString(dto)

// Retrofit-এ বসানো
Retrofit.Builder()
    .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
```

| json_serializable | kotlinx.serialization |
|---|---|
| `@JsonSerializable()` | `@Serializable` |
| `@JsonKey(name:)` | `@SerialName()` |
| `@JsonKey(defaultValue:)` | Kotlin-এর default value |
| `fromJson` / `toJson` factory | `decodeFromString` / `encodeToString` |
| `build_runner build` | লাগে না — compile-এর সময় নিজে |
| অজানা key — সাধারণত চুপচাপ বাদ | default-এ **error** — তাই `ignoreUnknownKeys = true` |

**ফাঁদ:**
- **`ignoreUnknownKeys = true` দিন।** নইলে server একটা নতুন field যোগ করলেই পুরনো app crash।
- **Gson এড়িয়ে চলুন।** পুরনো project-এ Gson দেখবেন। Gson constructor call না করেই object বানায়, তাই Kotlin-এর non-null field-এ null চলে আসে আর default value বসে না — পরে কোথাও অদ্ভুত crash। নতুন code-এ kotlinx.serialization বা Moshi।

[উপরে ফিরুন](#toc)

### <a id="ch9-3"></a>৯.৩ `drift` / `sqflite` → Room

**এক লাইনে:** Room হলো SQLite-এর উপর Google-এর library — drift-এর সবচেয়ে কাছের আত্মীয়। Table class, DAO, compile time-এ check হওয়া SQL, আর live query যেটা `Flow` দেয়।

**Flutter-এ (drift):**

```dart
class Notes extends Table {
  TextColumn get id => text()();
  TextColumn get title => text()();
  IntColumn get updatedAt => integer()();
  @override
  Set<Column> get primaryKey => {id};
}

@DriftDatabase(tables: [Notes])
class AppDatabase extends _$AppDatabase {
  AppDatabase(super.e);
  @override
  int get schemaVersion => 1;

  Stream<List<NoteRow>> watchAll() =>
      (select(notes)..orderBy([(t) => OrderingTerm.desc(t.updatedAt)])).watch();

  Future<void> upsert(NotesCompanion n) => into(notes).insertOnConflictUpdate(n);
}
```

**Android-এ (Room):**

```kotlin
@Entity(tableName = "notes")
data class NoteEntity(
    @PrimaryKey val id: String,
    val title: String,
    val updatedAt: Long,
)

@Dao
interface NoteDao {
    @Query("SELECT * FROM notes ORDER BY updatedAt DESC")
    fun observeAll(): Flow<List<NoteEntity>>            // drift-এর .watch()

    @Upsert
    suspend fun upsert(note: NoteEntity)                // insertOnConflictUpdate

    @Query("DELETE FROM notes WHERE id = :id")
    suspend fun delete(id: String)
}

@Database(entities = [NoteEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun noteDao(): NoteDao
}

// Hilt-এ একবার তৈরি
@Provides @Singleton
fun provideDb(@ApplicationContext context: Context): AppDatabase =
    Room.databaseBuilder(context, AppDatabase::class.java, "notes.db").build()
```

**কী মিলল, কী আলাদা:**

| drift | sqflite | Room |
|---|---|---|
| `Table` class | হাতে `CREATE TABLE` | `@Entity` data class |
| Database class-এর method | `db.query()` | `@Dao` interface |
| Dart DSL বা `.drift` file-এ SQL | raw SQL string | `@Query("SQL")` — compile time-এ check |
| `.watch()` → `Stream` | (নেই) | `Flow` return type |
| `schemaVersion` + `MigrationStrategy` | `onUpgrade` | `version` + `Migration` / `@AutoMigration` |
| `build_runner` | — | KSP |

**ভেতরে কীভাবে — live query:** `Flow` ফেরত দেওয়া query-কে Room মনে রাখে, সে কোন table পড়ে। ওই table-এ insert, update বা delete হলে Room query আবার চালায় আর নতুন list emit করে। Notes app-এ নতুন note save করলে list screen নিজে থেকে update হয় — আপনাকে কিছু করতে হয় না।

**Migration — সাবধান:**

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE notes ADD COLUMN isPinned INTEGER NOT NULL DEFAULT 0")
    }
}

Room.databaseBuilder(context, AppDatabase::class.java, "notes.db")
    .addMigrations(MIGRATION_1_2)
    .build()
```

- Schema বদলালে `version` বাড়ান আর migration দিন। সাধারণ বদলে (নতুন column) `@AutoMigration` নিজেই কাজ করে।
- Migration ছাড়া version বাড়ালে app crash করে।
- **`fallbackToDestructiveMigration()` দিলে crash হয় না, কিন্তু user-এর সব local data মুছে যায়।** Notes app-এ এর মানে user-এর সব note হারানো। Production-এ এটা প্রায় কখনো না।
- Room-এর `exportSchema` চালু রাখুন আর schema file git-এ রাখুন — migration test আর `@AutoMigration` এটা দেখে কাজ করে।

**Best approach:** Database-কে **source of truth** বানান। UI সবসময় Room-এর `Flow` দেখে। Network শুধু Room-কে update করে ([৯.৮](#ch9-8))।

[উপরে ফিরুন](#toc)

### <a id="ch9-4"></a>৯.৪ `shared_preferences` → DataStore

**এক লাইনে:** ছোট settings রাখার জায়গা। DataStore পুরোপুরি async, আর `Flow` দেয়।

**Flutter-এ:**

```dart
final prefs = await SharedPreferences.getInstance();
await prefs.setBool('sort_by_date', true);
final sortByDate = prefs.getBool('sort_by_date') ?? false;
```

**Android-এ:**

```kotlin
val Context.settings by preferencesDataStore(name = "settings")
private val SORT_BY_DATE = booleanPreferencesKey("sort_by_date")

val sortByDate: Flow<Boolean> = context.settings.data.map { it[SORT_BY_DATE] ?: false }

suspend fun setSortByDate(value: Boolean) {
    context.settings.edit { it[SORT_BY_DATE] = value }
}
```

**কী আলাদা:** Flutter-এর `getBool` একবার পড়ে। DataStore-এর `data` একটা `Flow` — setting বদলালে সব জায়গায় নিজে থেকে নতুন value যায়। তাই "sort by date" বদলালে list screen নিজে আবার sort হয়, কাউকে জানাতে হয় না।

**পুরনো `SharedPreferences` কেন না:** এটা প্রথম read-এ main thread-এ disk পড়ত, আর `apply()`-এর লেখা Activity বন্ধের সময় main thread আটকাতে পারত — ANR। DataStore এসব সমস্যা ছাড়া।

**Best approach:** ছোট key-value settings → DataStore Preferences। Structured বা বড় data → Room। DataStore-কে Hilt-এ singleton রাখুন — একই file-এর জন্য দুইটা DataStore instance বানালে exception আসে।

[উপরে ফিরুন](#toc)

### <a id="ch9-5"></a>৯.৫ `flutter_secure_storage` → Keystore

**এক লাইনে:** Token বা secret plain text-এ রাখা যাবে না। Android Keystore-এ একটা key রাখুন, আর সেই key দিয়ে encrypt করে data রাখুন।

Flutter-এর `flutter_secure_storage` Android-এ ঠিক এটাই করে — ভেতরে Keystore। এখন আপনি নিজে করবেন:

- **Keystore** একটা key রাখে, যেটা device থেকে বের করা যায় না। অনেক phone-এ এটা আলাদা secure hardware-এ থাকে। App key ব্যবহার করতে পারে, কিন্তু key-টা পড়তে পারে না।
- **Tink** (Google-এর crypto library) দিয়ে সেই key ব্যবহার করে data encrypt করুন, তারপর DataStore-এ রাখুন।
- পুরনো `EncryptedSharedPreferences` এখন **deprecated** — নতুন code-এ না।

**ফাঁদ:** Encrypt করা data-ও device-এর backup-এ যেতে পারে, কিন্তু key backup-এ যায় না। নতুন phone-এ restore হলে data আছে, key নেই — decrypt করা যাবে না। তাই token-এর মতো জিনিস backup থেকে বাদ দিন (Manifest-এর backup rules), আর decrypt fail হলে user-কে আবার login করতে দিন।

[উপরে ফিরুন](#toc)

### <a id="ch9-6"></a>৯.৬ Image: `cached_network_image` → Coil

**এক লাইনে:** Network image load, cache, আর resize — Coil-এর `AsyncImage`।

```dart
CachedNetworkImage(imageUrl: note.imageUrl, placeholder: (_, __) => const Shimmer(), fit: BoxFit.cover);
```

```kotlin
AsyncImage(
    model = note.imageUrl,
    contentDescription = null,
    placeholder = painterResource(R.drawable.placeholder),
    contentScale = ContentScale.Crop,
    modifier = Modifier.size(64.dp).clip(RoundedCornerShape(8.dp)),
)
```

Coil memory আর disk দুই জায়গায় cache করে, আর view-এর মাপ অনুযায়ী ছবি ছোট করে load করে — তাই 4000px ছবি 64dp thumbnail-এ পুরো memory খায় না। পুরনো project-এ Glide দেখবেন, একই কাজ।

[উপরে ফিরুন](#toc)

### <a id="ch9-7"></a>৯.৭ Pagination → Paging 3

**এক লাইনে:** লম্বা list পাতা ধরে load করা — `infinite_scroll_pagination`-এর `PagingController`-এর কাজ Android-এ Paging 3 library করে।

**Flutter-এ:**

```dart
final _pagingController = PagingController<int, Note>(firstPageKey: 0);
_pagingController.addPageRequestListener((page) async {
  final items = await repo.getPage(page);
  items.isEmpty ? _pagingController.appendLastPage(items) : _pagingController.appendPage(items, page + 1);
});
```

**Android-এ:**

```kotlin
class NotesPagingSource(private val api: NotesApi) : PagingSource<Int, Note>() {
    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, Note> = try {
        val page = params.key ?: 0
        val items = api.getPage(page, params.loadSize)
        LoadResult.Page(
            data = items,
            prevKey = if (page == 0) null else page - 1,
            nextKey = if (items.isEmpty()) null else page + 1,      // null = শেষ পাতা
        )
    } catch (e: IOException) {
        LoadResult.Error(e)
    }

    override fun getRefreshKey(state: PagingState<Int, Note>): Int? =       // refresh-এর পরে কোন পাতা থেকে
        state.anchorPosition?.let { anchor ->
            state.closestPageToPosition(anchor)?.let { it.prevKey?.plus(1) ?: it.nextKey?.minus(1) }
        }
}

// ViewModel
val notes: Flow<PagingData<Note>> = Pager(PagingConfig(pageSize = 20)) { NotesPagingSource(api) }
    .flow
    .cachedIn(viewModelScope)                  // rotation-এ আবার load না

// Compose
val items = viewModel.notes.collectAsLazyPagingItems()
LazyColumn {
    items(count = items.itemCount, key = items.itemKey { it.id }) { index ->
        items[index]?.let { NoteCard(it, onClick = {}) }
    }
}
```

- `PagingSource` = আপনার page request listener।
- `cachedIn(viewModelScope)` না দিলে rotation-এ সব পাতা আবার load হয়।
- Offline-first-এর জন্য `RemoteMediator` আছে: network থেকে পাতা এনে Room-এ রাখে, আর UI Room থেকে পাতা পড়ে।

[উপরে ফিরুন](#toc)

### <a id="ch9-8"></a>৯.৮ সব একসাথে: offline-first repository

এবার পুরো অধ্যায় এক জায়গায় জোড়া লাগাই। Notes app-এর repository, Flutter আর Android-এ একই নকশায়:

```kotlin
class NotesRepositoryImpl @Inject constructor(
    private val dao: NoteDao,
    private val api: NotesApi,
) : NotesRepository {

    override fun observeNotes(): Flow<List<Note>> =
        dao.observeAll().map { rows -> rows.map { it.toDomain() } }    // UI সবসময় database দেখে

    override suspend fun refresh() {
        val remote = api.getNotes()                                    // network থেকে আনো
        remote.forEach { dao.upsert(it.toEntity()) }                   // database-এ রাখো
    }                                                                  // Flow নিজে UI-তে পৌঁছে দেবে

    override suspend fun save(note: Note) {
        dao.upsert(note.toEntity())                                    // আগে local — UI সাথে সাথে বদলায়
        enqueueSync()                                                  // পরে server-এ, WorkManager দিয়ে
    }
}
```

```
UI  ◄── Flow ── Room (source of truth) ◄── upsert ── Retrofit (server)
                      ▲
                      └── save() সাথে সাথে লেখে; sync পরে WorkManager দিয়ে
```

**কেন এই নকশা:** Internet না থাকলেও app কাজ করে। Save সাথে সাথে দেখা যায়। আর দুই জায়গা থেকে data আসার ঝামেলা নেই — UI শুধু database চেনে। Flutter-এ drift + dio দিয়ে আপনি হয়তো ঠিক এটাই বানিয়েছেন।

> **মনে রাখুন**
> - dio → Retrofit + OkHttp। Interceptor একই, token refresh-এ `Authenticator`।
> - json_serializable → kotlinx.serialization, `ignoreUnknownKeys = true`। Gson না।
> - drift → Room। `Flow` query = `.watch()`। Destructive migration মানে user-এর data মুছে যাওয়া।
> - shared_preferences → DataStore। Secret → Keystore + Tink।
> - Database = source of truth।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমার data layer offline-first: Room হলো source of truth, UI তার Flow দেখে, আর network শুধু database update করে। Network-এ Retrofit আর OkHttp, token refresh `Authenticator` দিয়ে, JSON-এ kotlinx.serialization। Flutter-এ drift আর dio দিয়ে একই নকশা করতাম, তাই ধারণাটা আমার কাছে নতুন না।"
> - *English:* "My data layer is offline-first: Room is the source of truth, the UI observes its Flow, and the network only updates the database. I use Retrofit and OkHttp, with token refresh in an `Authenticator`, and kotlinx.serialization for JSON. I built the same design in Flutter with drift and dio, so the idea isn't new to me."

[উপরে ফিরুন](#toc)

---

## <a id="ch10"></a>১০. Plugin-এর পেছনের Android — background, notification, permission, intent

Flutter-এ এই অধ্যায়ের সবকিছু আপনি এক লাইনের plugin call দিয়ে সেরেছেন: `Workmanager().registerOneOffTask()`, `Permission.camera.request()`, `launchUrl()`। আর কখনো কখনো plugin ঠিকমতো কাজ করত না — নির্দিষ্ট Android version-এ notification আসত না, background task চলত না। কারণটা সবসময় ছিল নিচের Android-এর কোনো নিয়ম। এই অধ্যায়ে সেই নিয়মগুলোর মুখোমুখি হব।

### <a id="ch10-1"></a>১০.১ `workmanager` → WorkManager

**এক লাইনে:** Flutter-এর `workmanager` plugin আসলে Android-এর WorkManager-কেই চালায়। App বন্ধ হলেও, phone restart হলেও যে কাজ শেষ হতে হবে, তার জন্য এটা।

**Flutter-এ:**

```dart
@pragma('vm:entry-point')
void callbackDispatcher() {
  Workmanager().executeTask((task, input) async {
    await syncNotes();
    return true;
  });
}

Workmanager().initialize(callbackDispatcher);
Workmanager().registerOneOffTask(
  'sync-notes', 'syncNotes',
  constraints: Constraints(networkType: NetworkType.connected),
);
```

**Android-এ:**

```kotlin
class SyncWorker(context: Context, params: WorkerParameters) : CoroutineWorker(context, params) {
    override suspend fun doWork(): Result = try {
        syncNotes()
        Result.success()                       // Dart: return true
    } catch (e: IOException) {
        Result.retry()                         // পরে আবার, ধীরে ধীরে বাড়ানো বিরতিতে
    }
}

val request = OneTimeWorkRequestBuilder<SyncWorker>()
    .setConstraints(Constraints.Builder().setRequiredNetworkType(NetworkType.CONNECTED).build())
    .build()

WorkManager.getInstance(context)
    .enqueueUniqueWork("sync-notes", ExistingWorkPolicy.KEEP, request)
```

**কী মিলল:** নাম, constraint, unique work — সব একই, কারণ plugin এই API-রই একটা পাতলা আবরণ। পার্থক্য শুধু: Flutter-এ background-এ আলাদা Dart isolate চালু করতে `callbackDispatcher` লাগত। Native-এ worker সাধারণ Kotlin class।

**কোন কাজে কী:**

| কাজ | কী নেবেন |
|---|---|
| Screen খোলা থাকা পর্যন্ত | ViewModel-এ coroutine |
| App বন্ধ হলেও শেষ হতে হবে, একটু দেরি চলবে (sync, upload) | **WorkManager** |
| User এখনই দেখছে এমন লম্বা কাজ (music, recording, navigation) | Foreground Service ([১০.২](#ch10-2)) |
| ঠিক নির্দিষ্ট সময়ে (reminder) | `AlarmManager` — exact alarm-এ আলাদা permission |

**ফাঁদ — Flutter-এ আপনি যেগুলোর জন্য plugin-কে দোষ দিতেন:**
- **ঠিক কখন চলবে, তার নিশ্চয়তা নেই।** Doze আর battery-র নিয়মে system কাজ পিছিয়ে দেয়। Periodic work-এর সর্বনিম্ন interval ১৫ মিনিট।
- একটা worker সাধারণত প্রায় ১০ মিনিট পর্যন্ত চলতে পারে। আরও লম্বা হলে `setForeground()` দিয়ে notification দেখাতে হয়।
- **User Settings থেকে force stop করলে** WorkManager-এর কাজও বাতিল, আর app আবার না খোলা পর্যন্ত কিছু চলে না।
- কিছু phone কোম্পানি (বিশেষ করে কিছু চীনা brand) নিজেরা আরও কড়া battery নিয়ম দেয়। এটা Android-এর বাইরের সমস্যা, plugin-এর না।
- Hilt-এর dependency worker-এ দিতে `@HiltWorker` আর `@AssistedInject` লাগে।

[উপরে ফিরুন](#toc)

### <a id="ch10-2"></a>১০.২ Service

**এক লাইনে:** UI ছাড়া চলা কাজ। এখন প্রায় সবসময় **foreground service** — notification দেখিয়ে, user-কে জানিয়ে।

পুরনো দিনে (আপনার Java-র সময়ে) background service যখন খুশি চালানো যেত। এখন নিয়ম কড়া:

- Android 8 থেকে background-এ service চালানো প্রায় বন্ধ।
- Android 14 থেকে প্রতিটা foreground service-এর একটা **type** ঘোষণা করতে হয় (`dataSync`, `mediaPlayback`, `location`, `microphone`...), আর type অনুযায়ী আলাদা permission।
- Background থেকে foreground service চালু করা অনেক ক্ষেত্রে নিষেধ।

**Best approach:** আগে দেখুন WorkManager দিয়ে হয় কি না। Foreground service শুধু তখন, যখন user সত্যিই এখনই কাজটা দেখছে বা শুনছে — Notes app-এ voice note recording চলার সময়, যেমন।

[উপরে ফিরুন](#toc)

### <a id="ch10-3"></a>১০.৩ Notification

**এক লাইনে:** `flutter_local_notifications` যা করত: channel বানানো, notification দেখানো, tap করলে app খোলা। Native-এ `NotificationCompat` দিয়ে।

**Flutter-এ:**

```dart
const channel = AndroidNotificationDetails('reminders', 'রিমাইন্ডার', importance: Importance.defaultImportance);
await plugin.show(note.id.hashCode, 'রিমাইন্ডার', note.title, const NotificationDetails(android: channel));
```

**Android-এ:**

```kotlin
// ১. Channel — app চালুর সময় একবার (Android 8+ এ বাধ্যতামূলক)
val channel = NotificationChannel("reminders", "রিমাইন্ডার", NotificationManager.IMPORTANCE_DEFAULT)
context.getSystemService(NotificationManager::class.java).createNotificationChannel(channel)

// ২. Tap করলে কী খুলবে
val pendingIntent = PendingIntent.getActivity(
    context, note.id.hashCode(),
    Intent(context, MainActivity::class.java).putExtra("noteId", note.id),
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
)

// ৩. দেখানো
val notification = NotificationCompat.Builder(context, "reminders")
    .setSmallIcon(R.drawable.ic_notification)
    .setContentTitle("রিমাইন্ডার")
    .setContentText(note.title)
    .setContentIntent(pendingIntent)
    .setAutoCancel(true)
    .build()

NotificationManagerCompat.from(context).notify(note.id.hashCode(), notification)
```

- **Channel:** user প্রতিটা channel আলাদা বন্ধ করতে পারে। একবার তৈরি হলে channel-এর importance code দিয়ে আর বদলানো যায় না — user-এর হাতে চলে যায়। তাই প্রথমবারেই ঠিক করে দিন।
- **Android 13+-এ notification-এর জন্য runtime permission লাগে** (`POST_NOTIFICATIONS`)। না চাইলে কিছুই দেখাবে না। Flutter-এ "notification আসে না" bug-এর বড় একটা কারণ এটা ছিল।
- **`PendingIntent`** = system-কে "পরে আমার হয়ে এই intent চালাও" বলার অনুমতি। সবসময় `FLAG_IMMUTABLE`, যদি না সত্যিই mutable লাগে। আলাদা note-এর জন্য আলাদা request code (`note.id.hashCode()`) দিন, নইলে একটা আরেকটাকে overwrite করে।
- **FCM:** "notification" message app background-এ থাকলে system নিজে দেখায়, আপনার `onMessageReceived` call হয় না। "data" message সবসময় আপনার code-এ আসে। `firebase_messaging`-এ আপনি যে পার্থক্য দেখেছেন, সেটা এখান থেকেই।

[উপরে ফিরুন](#toc)

### <a id="ch10-4"></a>১০.৪ `permission_handler` → Activity Result API

**এক লাইনে:** Permission চাওয়া, ছবি বাছাই, অন্য app থেকে ফল আনা — সব এখন এক API দিয়ে: Activity Result API।

**Flutter-এ:**

```dart
final status = await Permission.camera.request();
if (status.isGranted) {
  openCamera();
} else if (status.isPermanentlyDenied) {
  openAppSettings();
}
```

**Android-এ (Compose-এর ভেতরে):**

```kotlin
@Composable
fun AttachPhotoButton(onGranted: () -> Unit) {
    val launcher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { granted ->
        if (granted) onGranted()
    }
    Button(onClick = { launcher.launch(Manifest.permission.CAMERA) }) { Text("ছবি তুলুন") }
}
```

**কী আলাদা:**
- Flutter-এ `await` করে ফল পেতেন। এখানে ফল আসে callback-এ — কারণ permission dialog চলার সময় আপনার Activity মরে আবার জন্মাতে পারে। Launcher সেটা নিজে সামলায়।
- **"Permanently denied" বলে সরাসরি কোনো API নেই।** User দুইবার "না" বললে system আর dialog দেখায় না। `shouldShowRequestPermissionRationale()` বলে, এখন কারণ বোঝানোর সময় কি না। `permission_handler` এই সব মিলিয়ে `isPermanentlyDenied` অনুমান করত। Native-এ আপনি নিজে করবেন — "না" বলার পরে rationale `false` হলে Settings-এ পাঠানোর পথ দিন।
- Permission দুই জায়গায়: Manifest-এ `<uses-permission>`, আর "dangerous" permission (camera, location, notification) runtime-এ চাওয়া।

**Best approach — আগে দেখুন permission লাগেই কি না:**
- ছবি বাছাই → **Photo Picker** (`PickVisualMedia`)। কোনো storage permission লাগে না।
- File বাছাই → `OpenDocument`। Permission লাগে না।
- শুধু একটা ছবি তোলা → `TakePicture` contract দিয়ে camera app-কে বলা। Manifest-এ CAMERA declare না করলে permission লাগে না (declare করলে তখন লাগে)।

```kotlin
val pickImage = rememberLauncherForActivityResult(ActivityResultContracts.PickVisualMedia()) { uri ->
    uri?.let { viewModel.attachImage(it) }
}
pickImage.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
```

আপনার Java-র সময়ের `onActivityResult` আর `onRequestPermissionsResult` — দুটোই এই API দিয়ে বদলানো হয়েছে।

[উপরে ফিরুন](#toc)

### <a id="ch10-5"></a>১০.৫ `url_launcher` → Intent

**এক লাইনে:** অন্য app খোলা, share করা — Android-এর ভাষায় একটা **Intent** পাঠানো। `url_launcher` আর `share_plus` ভেতরে এটাই করে।

**Flutter-এ:**

```dart
await launchUrl(Uri.parse('https://byteonyx.com'));
await Share.share(note.body);
```

**Android-এ:**

```kotlin
val context = LocalContext.current

context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse("https://byteonyx.com")))

val send = Intent(Intent.ACTION_SEND).apply {
    type = "text/plain"
    putExtra(Intent.EXTRA_TEXT, note.body)
}
context.startActivity(Intent.createChooser(send, "Note share করুন"))
```

- **Explicit intent:** নির্দিষ্ট class চালু করে — নিজের app-এর ভেতরে (`Intent(context, MainActivity::class.java)`)।
- **Implicit intent:** "এই কাজটা যে পারে" — browser, share, dialer। কে খুলবে, system বা user ঠিক করে।
- **ফাঁদ:** Android 11+-এ অন্য কোনো app installed আছে কি না জানতে চাইলে Manifest-এ `<queries>` লাগে। নইলে আপনার app অন্য app-কে "দেখতে" পায় না। `url_launcher`-এর `canLaunchUrl` false দেওয়ার একটা পরিচিত কারণ এটা।
- **Deep link / App Links:** বাইরের link থেকে app-এর নির্দিষ্ট screen খোলা — Manifest-এ `intent-filter` আর Navigation-এ `deepLinks`। `https` link সরাসরি app-এ খুলতে website-এ `assetlinks.json` লাগে, যেখানে Play-এর app signing key-র SHA-256 দিতে হয়।

> **মনে রাখুন**
> - Flutter-এর background, notification, permission, url plugin সবাই এই Android API-গুলোই চালায়।
> - Background কাজ → WorkManager। চলবে, কিন্তু ঠিক কখন, নিশ্চয়তা নেই।
> - Notification: channel, Android 13+ permission, `FLAG_IMMUTABLE`।
> - Permission: Activity Result API। আগে দেখুন permission ছাড়া উপায় আছে কি না (Photo Picker)।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter-এ background আর notification plugin দিয়ে করতাম, কিন্তু সমস্যা হলে সবসময় নিচের Android নিয়মই কারণ ছিল — Doze, notification permission, foreground service type। Native-এ deferrable কাজে WorkManager নিই, permission-এ Activity Result API, আর যেখানে সম্ভব permission ছাড়া উপায় বেছে নিই, যেমন Photo Picker।"
> - *English:* "In Flutter I used plugins for background work and notifications, but whenever something broke, the cause was always an Android rule underneath — Doze, the notification permission, foreground service types. In native, I use WorkManager for deferrable work, the Activity Result API for permissions, and pick permission-free options like the Photo Picker when I can."

[উপরে ফিরুন](#toc)

---

## <a id="ch11"></a>১১. Testing

Test লেখার দর্শন আপনি জানেন: fake ভালো, mock কম, behaviour test করুন। এখানে শুধু হাতিয়ারগুলোর নাম বদলায়।

| Flutter | Android |
|---|---|
| `test()` | JUnit `@Test` — `src/test/`, device ছাড়া চলে |
| `expect(a, equals(b))` | `assertEquals(b, a)`, বা Truth-এর `assertThat(a).isEqualTo(b)` |
| `bloc_test` | `runTest` + Turbine |
| `fake_async` | `runTest` (virtual time) |
| `mocktail` | Fake class আগে, দরকার হলে MockK |
| `testWidgets` + `pumpWidget` | `createComposeRule()` + `setContent` |
| `find.text()` / `find.byTooltip()` | `onNodeWithText()` / `onNodeWithContentDescription()` |
| `tester.tap()` | `.performClick()` |
| golden test | screenshot test (Roborazzi, Paparazzi, Compose Preview Screenshot Testing) |
| `integration_test` | instrumented test (`src/androidTest/`) |

### `bloc_test` → ViewModel test

**Flutter-এ:**

```dart
blocTest<NotesCubit, NotesState>(
  'delete failure shows an error',
  build: () => NotesCubit(FakeNotesRepository(failOnDelete: true)),
  act: (cubit) => cubit.delete('1'),
  skip: 1,
  expect: () => [isA<NotesState>().having((s) => s.error, 'error', 'মোছা যায়নি')],
);
```

**Android-এ:**

```kotlin
class NotesViewModelTest {

    @get:Rule val mainRule = MainDispatcherRule()

    @Test
    fun `delete failure shows an error`() = runTest {
        val repo = FakeNotesRepository(failOnDelete = true)
        val viewModel = NotesViewModel(repo)

        viewModel.uiState.test {                           // Turbine
            skipItems(1)                                   // initial state
            repo.emit(listOf(sampleNote))
            assertEquals(listOf(sampleNote), awaitItem().notes)

            viewModel.delete(sampleNote.id)
            assertEquals("মোছা যায়নি", awaitItem().error)
        }
    }
}
```

- **`runTest`** = `fake_async`। `delay(5_000)` সাথে সাথে শেষ।
- **`MainDispatcherRule`** একটা ছোট JUnit rule, যেটা `Dispatchers.Main`-কে test dispatcher দিয়ে বদলায়। JVM test-এ আসল main thread নেই, তাই এটা ছাড়া `viewModelScope` crash করে। এর code Android-এর official testing guide-এ আছে — copy করে নিন।
- **Turbine** = `bloc_test`-এর `expect` list, কিন্তু এক এক করে: `awaitItem()`।
- **ফাঁদ:** `stateIn(WhileSubscribed)` দিয়ে বানানো flow-এর `.value` সরাসরি পড়লে কেউ subscribe না করায় initial value-ই থাকে। তাই Turbine দিয়ে collect করুন।
- Test-এর নাম backtick-এ বাক্যের মতো লেখা যায়।

### `testWidgets` → Compose UI test

```dart
testWidgets('pin button toggles', (tester) async {
  var pinned = false;
  await tester.pumpWidget(MaterialApp(home: PinButton(pinned: pinned, onChanged: (v) => pinned = v)));
  await tester.tap(find.byTooltip('পিন'));
  expect(pinned, isTrue);
});
```

```kotlin
class PinButtonTest {
    @get:Rule val composeRule = createComposeRule()

    @Test
    fun `pin button toggles`() {
        var pinned = false
        composeRule.setContent { PinButton(pinned = pinned, onPinnedChange = { pinned = it }) }

        composeRule.onNodeWithContentDescription("পিন").performClick()

        assertTrue(pinned)
    }
}
```

Compose test **semantics tree** দিয়ে খোঁজে — text, content description, বা `Modifier.testTag("id")`। এটা সেই tree, যেটা TalkBack (screen reader) ব্যবহার করে। তাই ভালো accessibility দিলে test লেখাও সহজ হয়। **Robolectric** দিলে এই test-ও device ছাড়া JVM-এ, দ্রুত চলে।

> **মনে রাখুন**
> - `bloc_test` → `runTest` + Turbine। `MainDispatcherRule` লাগবেই।
> - `testWidgets` → `createComposeRule()`। খোঁজা semantics দিয়ে।
> - Fake আগে, mock পরে — Flutter-এর মতোই।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "ViewModel test করি `runTest` আর Turbine দিয়ে, main dispatcher বদলানোর rule সহ, আর repository-র জায়গায় fake দিই। Compose-এ stateless screen রাখি বলে UI test সহজ — semantics দিয়ে node খুঁজি, Robolectric-এ JVM-এ চালাই।"
> - *English:* "I test ViewModels with `runTest` and Turbine, with a rule that replaces the main dispatcher, and a fake instead of the real repository. Because my Compose screens are stateless, UI tests are easy — I find nodes by semantics and run them on the JVM with Robolectric."

[উপরে ফিরুন](#toc)

---

## <a id="ch12"></a>১২. Flavor, R8, release

এখানে আপনি আসলে পুরনো বাড়িতে ফিরছেন। Flutter-এ flavor বানাতে আপনি `android/app/build.gradle`-এ যা লিখেছিলেন, সেটাই native Android-এর flavor।

**Flutter-এ flavor:** `flutter run --flavor dev`, আর `android/app/build.gradle`-এ:

```groovy
flavorDimensions "env"
productFlavors {
    dev { dimension "env"; applicationIdSuffix ".dev" }
    prod { dimension "env" }
}
```

**Native Android-এ — একই জিনিস, Kotlin DSL-এ:**

```kotlin
android {
    flavorDimensions += "env"
    productFlavors {
        create("dev") {
            dimension = "env"
            applicationIdSuffix = ".dev"             // dev আর prod একই phone-এ পাশাপাশি
            buildConfigField("String", "API_URL", "\"https://dev.api.byteonyx.com/\"")
        }
        create("prod") {
            dimension = "env"
            buildConfigField("String", "API_URL", "\"https://api.byteonyx.com/\"")
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = true                   // R8
            isShrinkResources = true                 // না-ব্যবহৃত resource বাদ (R8 লাগে)
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }

    buildFeatures { buildConfig = true }
}
```

| Flutter | Android |
|---|---|
| `--flavor dev` | `productFlavors` → Android Studio-র **Build Variants** panel |
| `--release` / `--debug` | `buildTypes` |
| `--dart-define=API_URL=...` | `buildConfigField` → code-এ `BuildConfig.API_URL` |
| `--obfuscate --split-debug-info` | R8 + `mapping.txt` |
| `flutter build appbundle` | `./gradlew bundleProdRelease` |

Flavor × build type = **build variant**: `devDebug`, `devRelease`, `prodDebug`, `prodRelease`।

**R8 — release-এ crash-এর এক নম্বর কারণ:** R8 না-ব্যবহৃত class আর method মুছে দেয়, আর নাম ছোট করে (`a`, `b`)। কিন্তু reflection দিয়ে যে class ব্যবহার হয়, R8 সেটা দেখতে পায় না। ফলে debug-এ সব ঠিক, release-এ crash। সমাধান `proguard-rules.pro`-তে `-keep` rule। kotlinx.serialization, Retrofit, Room-এর মতো ভালো library নিজের rule নিজে দেয়। Flutter app-এও plugin-এর Java/Kotlin code R8-এর ভেতর দিয়ে যায় — তাই Flutter-এ release-only crash-এর অভিজ্ঞতা থাকলে কারণ এটাই ছিল।

**Best approach:** প্রতিটা release-এর আগে release build install করে চালান। Play Console-এ `mapping.txt` upload করুন, নইলে crash report-এর stack trace পড়া যাবে না।

**Signing আর Play:** আপনি জানেন — Play App Signing-এ Google আসল key রাখে, আপনি upload key দিয়ে sign করেন। App Links-এর `assetlinks.json`-এ app signing key-র SHA-256 দিন, upload key-র না। আর Play প্রতি বছর `targetSdk`-এর নিচের সীমা বাড়ায় — বাড়ানোর আগে সেই Android version-এর behavior change পড়ুন।

> **মনে রাখুন**
> - Flutter-এর flavor = Android-এর `productFlavors`। একই file, একই জিনিস।
> - `--dart-define` → `buildConfigField`।
> - R8 = release-only crash-এর প্রধান কারণ। Release build চালিয়ে দেখুন, `mapping.txt` upload করুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter-এ flavor করতে আমি আগেই Android-এর productFlavors লিখেছি, তাই build variant আমার চেনা। Release-এ R8 চালু রাখি, প্রতিবার release build চালিয়ে test করি, আর mapping file upload করি যাতে crash পড়া যায়।"
> - *English:* "I already wrote Android productFlavors to set up flavors in Flutter, so build variants are familiar to me. In release I keep R8 on, test the release build every time, and upload the mapping file so crashes are readable."

[উপরে ফিরুন](#toc)

---

## <a id="ch13"></a>১৩. শেখার পরিকল্পনা — ৪ সপ্তাহ

পড়ে শেখার চেয়ে বানিয়ে শেখা অনেক দ্রুত। আর আপনার জন্য সবচেয়ে দ্রুত পথ হলো: **যে Notes app এই বই জুড়ে দেখলেন, সেটা native-এ বানানো।** প্রতিটা অংশ Flutter-এ কীভাবে লিখতেন, তা আপনি আগেই জানেন — শুধু অনুবাদ করবেন।

| সপ্তাহ | পড়ুন | বানান |
|---|---|---|
| ১ | [০](#ch0), [১](#ch1), [২](#ch2) | [Kotlin Koans](https://play.kotlinlang.org/koans)-এর প্রথম অর্ধেক। তারপর playground-এ Notes-এর model (`data class`, `sealed`), আর একটা `Flow` দিয়ে search debounce। |
| ২ | [৩](#ch3)–[৬](#ch6) | Android Studio-তে নতুন project। Notes list, note খোলা, নতুন note-এর form — শুধু memory-র data দিয়ে। Phone ঘুরিয়ে দেখুন কী হারায়, তারপর ঠিক করুন। |
| ৩ | [৭](#ch7)–[৯](#ch9) | Navigation, ViewModel + `UiState`, Hilt। Room-এ note রাখুন। একটা fake API (বা যেকোনো free mock server) থেকে Retrofit দিয়ে sync। `adb shell am kill` দিয়ে process death test। |
| ৪ | [১০](#ch10)–[১২](#ch12) | WorkManager দিয়ে background sync, reminder notification। ViewModel test, একটা Compose UI test। Release build-এ R8 চালু করে চালান। |

**প্রতিদিনের শেষে তিনটা প্রশ্ন:**
1. আজ যেটা লিখলাম, Flutter-এ সেটা কী দিয়ে করতাম? পার্থক্যটা কোথায়, আর কেন?
2. Phone ঘোরালে বা process মরলে এটা টিকবে?
3. এটা কোন thread-এ চলছে?

এই তিন প্রশ্নের উত্তর মুখে বলতে পারলে আপনি interview-এর জন্য তৈরি। শেষে [Android Interview Prep](../../interviews/software-engineer-android-bn/android-interview-prep-bn.md) খুলে প্রশ্নগুলো জোরে জোরে বলে অনুশীলন করুন — ওখানে প্রতিটা উত্তর বাংলা আর English-এ আছে।

[উপরে ফিরুন](#toc)

---

## <a id="dictionary"></a>Flutter → Android অভিধান

Interview-এর আগের রাতে শুধু এই পাতাটা।

**ভাষা**

| Dart | Kotlin |
|---|---|
| `final` / `var` / `const` | `val` / `var` / `const val` |
| `late T x;` | `lateinit var x: T` |
| `late final x = f();` | `val x by lazy { f() }` |
| `??` / `!` | `?:` / `!!` |
| `void` / `Never` / `dynamic` | `Unit` / `Nothing` / (নেই — কাছাকাছি `Any?`) |
| `switch` expression | `when` |
| `sealed class` | `sealed class` / `sealed interface` |
| freezed / `copyWith` | `data class` / `copy()` |
| `static` | `companion object` বা top-level |
| singleton | `object` |
| factory constructor | companion-এ factory function |
| `extension X on Y` | `fun Y.x()` |
| `..` cascade | `apply { }` |
| mixin | interface + default method, বা `by` delegation |
| `typedef` | `typealias` |
| extension type | `@JvmInline value class` |
| lazy `Iterable` | `Sequence` |
| `_private` | `private` / `internal` |
| `build_runner` | KSP / compiler plugin |

**Async**

| Dart | Kotlin |
|---|---|
| `Future<T>` + `async`/`await` | `suspend fun` |
| `unawaited(f())` | `scope.launch { }` |
| `Future.wait` | `async { }` + `await()` / `awaitAll()` |
| `Isolate.run` / `compute` | `withContext(Dispatchers.Default)` |
| `Stream` / `async*` / `yield` | `Flow` / `flow { }` / `emit` |
| `StreamController.broadcast` | `SharedFlow` |
| `ValueNotifier` | `StateFlow` |
| `StreamSubscription.cancel` | scope বন্ধ হলে নিজে |
| `mounted` check | লাগে না — scope |
| RxDart `switchMap` / `combineLatest` / `debounceTime` | `flatMapLatest` / `combine` / `debounce` |
| `StreamController` দিয়ে callback → stream | `callbackFlow` |

**UI**

| Flutter | Compose |
|---|---|
| Widget + `build()` | `@Composable` function |
| `child` / `children` | trailing lambda |
| `setState` | `mutableStateOf`-এ নতুন value |
| `State` object বাঁচে | `remember { }` |
| `RestorationMixin` | `rememberSaveable` |
| `initState` / `didUpdateWidget` | `LaunchedEffect(key)` |
| `dispose` | `DisposableEffect { onDispose { } }` |
| `StreamBuilder` / `FutureBuilder` | `collectAsStateWithLifecycle()` / `produceState` |
| `InheritedWidget` / Provider (পরিবেশ) | `CompositionLocal` |
| `Theme.of(context)` | `MaterialTheme.colorScheme` / `.typography` |
| `Column` / `Row` / `Stack` | `Column` / `Row` / `Box` |
| `Expanded` | `Modifier.weight(1f)` |
| `Padding` / `Container` / `GestureDetector` | `Modifier.padding` / `.background` / `.clickable` |
| `SizedBox` / `spacing:` | `Spacer` / `Arrangement.spacedBy` |
| `ListView.builder` / `GridView` / `PageView` | `LazyColumn` / `LazyVerticalGrid` / `HorizontalPager` |
| `TextEditingController` | `value` + `onValueChange`, বা `TextFieldState` |
| `FocusNode` | `FocusRequester` |
| `AnimatedContainer` / `AnimatedSwitcher` / `Hero` | `animate*AsState` / `AnimatedContent` / shared element |
| `PopScope` | `BackHandler` |
| `SafeArea` | `innerPadding` / `safeDrawingPadding()` |
| Hot reload / DevTools | `@Preview` + Live Edit / Layout Inspector |

**App, architecture, data**

| Flutter | Android |
|---|---|
| `main()` + `runApp` | `Application` + `MainActivity.setContent` |
| `FlutterActivity` | `ComponentActivity` |
| `BuildContext` | (মিল নেই) — `Context` হলো system-এর দরজা |
| `WidgetsBindingObserver` | `Lifecycle`, `LifecycleResumeEffect`, `ProcessLifecycleOwner` |
| `go_router` / `Navigator` | Navigation Compose / Navigation 3 |
| Cubit / Bloc / Notifier | `ViewModel` |
| `BlocProvider` / `BlocBuilder` / `BlocListener` | `hiltViewModel()` / `collectAsStateWithLifecycle()` / `LaunchedEffect` + state |
| `get_it` / `injectable` | Hilt |
| `dio` / retrofit package | Retrofit + OkHttp |
| dio interceptor / 401 refresh | `Interceptor` / `Authenticator` |
| `json_serializable` | kotlinx.serialization |
| `drift` / `sqflite` | Room |
| `.watch()` | `Flow` query |
| `shared_preferences` | DataStore |
| `flutter_secure_storage` | Keystore + Tink |
| `cached_network_image` | Coil |
| `infinite_scroll_pagination` | Paging 3 |

**Platform আর release**

| Flutter | Android |
|---|---|
| `workmanager` plugin | WorkManager |
| `flutter_local_notifications` | `NotificationCompat` + channel |
| `firebase_messaging` | FCM SDK |
| `permission_handler` | Activity Result API |
| `image_picker` | Photo Picker (`PickVisualMedia`) |
| `url_launcher` / `share_plus` | implicit `Intent` |
| platform channel | লাগে না — সরাসরি API |
| platform view (`AndroidView`) | Compose-এ `AndroidView` (একই নাম!) |
| `pubspec.yaml` | `libs.versions.toml` + `build.gradle.kts` |
| `--flavor` / `--dart-define` | `productFlavors` / `buildConfigField` |
| `--obfuscate` | R8 |
| `bloc_test` / `fake_async` | Turbine / `runTest` |
| `testWidgets` / golden | Compose UI test / screenshot test |

[উপরে ফিরুন](#toc)

---

## <a id="resources"></a>ভালো resource

- [Kotlin Koans](https://play.kotlinlang.org/koans) — browser-এ ছোট ছোট অনুশীলন। Dart থেকে Kotlin-এ আসার সবচেয়ে দ্রুত পথ।
- [Kotlin docs](https://kotlinlang.org/docs/home.html) আর [Coroutines guide](https://kotlinlang.org/docs/coroutines-guide.html) — ভাষা আর coroutine-এর official গাইড।
- [Flutter for Jetpack Compose developers](https://docs.flutter.dev/flutter-for/compose-devs) — Flutter-এর official তুলনা, Compose developer-দের জন্য লেখা। উল্টো দিক থেকে পড়লে আপনার জন্য একদম কাজের।
- [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model) — recomposition-এর মূল ধারণা।
- [Guide to app architecture](https://developer.android.com/topic/architecture) — UiState, UDF, layer — Google-এর নিজের পরামর্শ।
- [Now in Android](https://github.com/android/nowinandroid) — Google-এর বানানো পূর্ণ app। এই বইয়ের প্রায় সব pattern একসাথে, আসল code-এ।
- [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course) — codelab-গুলো হাত চালু করতে কাজের।

[উপরে ফিরুন](#toc)
