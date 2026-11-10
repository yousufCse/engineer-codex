# Flutter-এর চোখে Android আর iOS — শেখার গাইড (বাংলা)

> যিনি Flutter ভালো জানেন, অনেক আগে Java আর Activity দিয়ে Android করেছেন, কিন্তু Kotlin আর Jetpack Compose আসার পরে আর করেননি — তাঁর জন্য।
> এটা interview-এর প্রশ্নোত্তর না, **শেখার গাইড**। প্রতিটা জিনিস আগে Flutter-এ আপনি যেভাবে করেন সেভাবে দেখানো, তারপর Android-এ ঠিক সেই কাজটা।
> বইয়ে দুইটা খণ্ড: **খণ্ড ১ — Android** (অধ্যায় ০–১৪) আর **খণ্ড ২ — [iOS](#part-ios)** (iOS ০–১৩)। দুই খণ্ডই একই ছাঁচে, একই Notes app দিয়ে লেখা।
> শেখা শেষ হলে অনুশীলনের জন্য আছে [Flutter + Android + iOS Interview Prep](../../interviews/software-engineer-flutter-android-ios-bn/flutter-android-ios-interview-prep-bn.md)।

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

**পর্ব ৬ — ইঞ্জিনের ভেতরে**
- [১৩. ইঞ্জিনের ভেতরে — tap থেকে pixel, code থেকে APK](#ch13)
  - [১৩.১ UI toolkit আর Everything is a widget](#ch13-1) · [১৩.২ তিনটা runtime: JVM, ART আর Dart](#ch13-2) · [১৩.৩ App খুললে কী হয়](#ch13-3) · [১৩.৪ একটা লেখা screen-এ আসা](#ch13-4) · [১৩.৫ দুই renderer: HWUI বনাম Impeller](#ch13-5) · [১৩.৬ Gradle আর release APK](#ch13-6) · [১৩.৭ পুরো ecosystem এক ছবিতে](#ch13-7)

**শেষে**
- [১৪. শেখার পরিকল্পনা — ৪ সপ্তাহ](#ch14)
- [Flutter → Android অভিধান](#dictionary)
- [ভালো resource](#resources)

**খণ্ড ২ — iOS**
- [iOS ০. বড় ছবি — আপনার Flutter app আসলে একটা iOS app](#ios0)
  - [iOS ০.১ আপনার Flutter app আসলে একটা iOS app](#ios0-1) · [iOS ০.২ iOS-এর স্তরগুলো](#ios0-2) · [iOS ০.৩ iOS আর Android-এর বড় পার্থক্য](#ios0-3) · [iOS ০.৪ পুরো framework-এর মানচিত্র](#ios0-4)
- [iOS ১. Swift — Dart-এর পাশে](#ios1)
  - [iOS ১.১ Variable আর type](#ios1-1) · [iOS ১.২ Optional](#ios1-2) · [iOS ১.৩ Function আর closure](#ios1-3) · [iOS ১.৪ struct বনাম class — value বনাম reference](#ios1-4) · [iOS ১.৫ Memory: ARC, weak আর retain cycle](#ios1-5) · [iOS ১.৬ enum আর switch](#ios1-6) · [iOS ১.৭ Protocol আর extension](#ios1-7) · [iOS ১.৮ Generics](#ios1-8) · [iOS ১.৯ Error handling — throws, try, Result](#ios1-9) · [iOS ১.১০ Collection](#ios1-10) · [iOS ১.১১ Access control](#ios1-11) · [iOS ১.১২ Objective-C-র সাথে (চিনে রাখুন)](#ios1-12)
- [iOS ২. Async — Future, Stream, Isolate থেকে async/await, actor আর AsyncSequence](#ios2)
  - [iOS ২.১ সবচেয়ে বড় পার্থক্য: thread আর data race](#ios2-1) · [iOS ২.২ Future → async/await](#ios2-2) · [iOS ২.৩ কাজ চালু করা: Task আর task group](#ios2-3) · [iOS ২.৪ Cancellation](#ios2-4) · [iOS ২.৫ actor — এক সময়ে একজন](#ios2-5) · [iOS ২.৬ @MainActor — UI-র thread](#ios2-6) · [iOS ২.৭ Sendable আর Swift 6 strict concurrency](#ios2-7) · [iOS ২.৮ Stream → AsyncSequence আর AsyncStream](#ios2-8) · [iOS ২.৯ চিনে রাখুন: GCD, completion handler আর Combine](#ios2-9) · [iOS ২.১০ Kotlin coroutine-এর সাথে এক table, আর best approach](#ios2-10)
- [iOS ৩. Xcode project — `pubspec.yaml`-এর জায়গায়](#ios3)
  - [iOS ৩.১ Folder-এর চেহারা — Flutter-এর ios/ বনাম native project](#ios3-1) · [iOS ৩.২ Project, target, scheme, build configuration](#ios3-2) · [iOS ৩.৩ .xcconfig — build setting একটা text file-এ](#ios3-3) · [iOS ৩.৪ Flavor = scheme + configuration](#ios3-4) · [iOS ৩.৫ Swift Package Manager বনাম CocoaPods](#ios3-5) · [iOS ৩.৬ Info.plist](#ios3-6) · [iOS ৩.৭ Entitlements](#ios3-7) · [iOS ৩.৮ Deployment target আর SDK](#ios3-8)
- [iOS ৪. App lifecycle — `@main`, AppDelegate, SceneDelegate আর suspension](#ios4)
  - [iOS ৪.১ চালু হওয়া: @main থেকে প্রথম screen](#ios4-1) · [iOS ৪.২ App-এর অবস্থাগুলো](#ios4-2) · [iOS ৪.৩ scenePhase — didChangeAppLifecycleState-এর জায়গায়](#ios4-3) · [iOS ৪.৪ Background suspension আর termination](#ios4-4) · [iOS ৪.৫ State restoration — @SceneStorage](#ios4-5) · [iOS ৪.৬ Memory warning](#ios4-6) · [iOS ৪.৭ Android-এর সাথে তুলনা — কোনটা নেই, কোনটা বেশি](#ios4-7)
- [iOS ৫. SwiftUI — Widget-এর জায়গায় View](#ios5)
  - [iOS ৫.১ Widget → View](#ios5-1) · [iOS ৫.২ Layout](#ios5-2) · [iOS ৫.৩ Wrapper widget → modifier, আর ক্রমের নিয়ম](#ios5-3) · [iOS ৫.৪ ListView.builder → List আর LazyVStack](#ios5-4) · [iOS ৫.৫ setState → @State](#ios5-5) · [iOS ৫.৬ @Binding — lifting state up](#ios5-6) · [iOS ৫.৭ ChangeNotifier / Cubit → @Observable](#ios5-7) · [iOS ৫.৮ InheritedWidget / Provider → @Environment](#ios5-8) · [iOS ৫.৯ initState, dispose, StreamBuilder → .task, .onAppear, .onChange](#ios5-9) · [iOS ৫.১০ View identity — Flutter-এর Key](#ios5-10) · [iOS ৫.১১ Animation](#ios5-11) · [iOS ৫.১২ Hot reload নেই: Preview](#ios5-12) · [iOS ৫.১৩ UIKit চিনে রাখুন — UIViewController আর Auto Layout](#ios5-13)
- [iOS ৬. Navigation — `go_router`-এর জায়গায় `NavigationStack`](#ios6)
  - [iOS ৬.১ NavigationStack আর path](#ios6-1) · [iOS ৬.২ Sheet, full-screen cover আর alert](#ios6-2) · [iOS ৬.৩ Tab](#ios6-3) · [iOS ৬.৪ Deep link — onOpenURL](#ios6-4) · [iOS ৬.৫ তিন framework পাশাপাশি, আর best approach](#ios6-5)
- [iOS ৭. Architecture — Cubit থেকে `@Observable` view model](#ios7)
  - [iOS ৭.১ Layer একই থাকে](#ios7-1) · [iOS ৭.২ Cubit → @Observable view model](#ios7-2) · [iOS ৭.৩ Unidirectional data flow — state নিচে, event ওপরে](#ios7-3) · [iOS ৭.৪ get_it → init injection আর @Environment](#ios7-4) · [iOS ৭.৫ Repository layer](#ios7-5)
- [iOS ৮. Data — network, JSON, database, storage](#ios8)
  - [iOS ৮.১ dio → URLSession + async/await](#ios8-1) · [iOS ৮.২ json_serializable → Codable](#ios8-2) · [iOS ৮.৩ drift → SwiftData (আর Core Data চিনে রাখুন)](#ios8-3) · [iOS ৮.৪ shared_preferences → UserDefaults / @AppStorage](#ios8-4) · [iOS ৮.৫ flutter_secure_storage → Keychain](#ios8-5) · [iOS ৮.৬ Image: cached_network_image → AsyncImage](#ios8-6) · [iOS ৮.৭ File system আর sandbox](#ios8-7) · [iOS ৮.৮ সব একসাথে: offline-first repository](#ios8-8)
- [iOS ৯. Plugin-এর পেছনের iOS — background, notification, permission, link](#ios9)
  - [iOS ৯.১ workmanager → BGTaskScheduler (আর কেন iOS-এ এটা অন্যরকম)](#ios9-1) · [iOS ৯.২ Local notification — UNUserNotificationCenter](#ios9-2) · [iOS ৯.৩ Push notification — APNs, আর FCM-এর সাথে APNs key](#ios9-3) · [iOS ৯.৪ permission_handler → Info.plist + request API](#ios9-4) · [iOS ৯.৫ Deep link — Universal Links বনাম custom URL scheme](#ios9-5) · [iOS ৯.৬ url_launcher আর share_plus-এর পেছনে](#ios9-6)
- [iOS ১০. Testing](#ios10)
  - [iOS ১০.১ হাতিয়ারের নাম বদল](#ios10-1) · [iOS ১০.২ Swift Testing: @Test আর #expect](#ios10-2) · [iOS ১০.৩ bloc_test → @Observable view model test](#ios10-3) · [iOS ১০.৪ XCTest — চিনে রাখুন](#ios10-4) · [iOS ১০.৫ integration_test → XCUITest](#ios10-5)
- [iOS ১১. Signing আর release — certificate থেকে App Store](#ios11)
  - [iOS ১১.১ পাঁচ টুকরো: bundle id, team, certificate, provisioning profile, entitlement](#ios11-1) · [iOS ১১.২ Automatic বনাম manual signing](#ios11-2) · [iOS ১১.৩ Archive → TestFlight → App Store](#ios11-3) · [iOS ১১.৪ Review guideline-এর যে নিয়মে সবাই আটকায়](#ios11-4) · [iOS ১১.৫ Privacy manifest আর nutrition label](#ios11-5) · [iOS ১১.৬ flutter build ipa ভেতরে কী করে](#ios11-6)
- [iOS ১২. ইঞ্জিনের ভেতরে — tap থেকে pixel, code থেকে `.ipa`](#ios12)
  - [iOS ১২.১ Swift সরাসরি machine code — কোনো VM নেই](#ios12-1) · [iOS ১২.২ ARC বনাম garbage collection](#ios12-2) · [iOS ১২.৩ App খুললে কী হয় — tap থেকে প্রথম frame](#ios12-3) · [iOS ১২.৪ Rendering — Core Animation, render server, Metal](#ios12-4) · [iOS ১২.৫ Build pipeline — Xcode থেকে .app আর .ipa](#ios12-5) · [iOS ১২.৬ Android-এর পাশে, এক টেবিলে](#ios12-6)
- [iOS ১৩. iOS শেখার পরিকল্পনা — ৪ সপ্তাহ](#ios13)
  - [iOS ১৩.১ চার সপ্তাহের পরিকল্পনা](#ios13-1) · [Flutter → iOS অভিধান](#ios-dictionary) · [iOS ১৩.২ ভালো resource](#ios13-2)

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

App খোলা থেকে pixel পর্যন্ত, আর build চাপলে কী হয় — ভেতরের পুরো গল্প [অধ্যায় ১৩](#ch13)-এ।

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

## <a id="ch13"></a>১৩. ইঞ্জিনের ভেতরে — tap থেকে pixel, code থেকে APK

এতক্ষণ আমরা গাড়ি চালানো শিখলাম। এবার bonnet খুলব।

Senior interview-এ সবচেয়ে বেশি আলাদা করে দেয় এই প্রশ্নগুলো: app খুললে ভেতরে কী হয়? একটা লেখা screen-এ আসে কীভাবে? Build চাপলে কী হয়? এখানে নতুন কোনো library নেই। আছে শুধু ভেতরের যন্ত্র, আর প্রতিটা অংশে Flutter আর native Android পাশাপাশি। এই অধ্যায় বুঝলে [অধ্যায় ০](#ch0)-এর বড় ছবিটা একদম পরিষ্কার হয়ে যাবে।

### <a id="ch13-1"></a>১৩.১ "UI toolkit" আর "Everything is a widget" — কেন বলা হয়

**এক লাইনে:** Flutter শুধু UI বানানোর যন্ত্রপাতি দেয় — widget, layout, আঁকা, gesture, animation, text। OS-এর বাকি সব কাজের জন্য সে host platform-এর ওপর নির্ভর করে। তাই এটা একটা toolkit, পুরো OS framework না।

**কে কী দেয়:**

| কাজ | কে করে |
|---|---|
| Widget, layout, আঁকা, gesture, animation | Flutter |
| Text layout, image decode | Flutter engine |
| File আর network socket (`dart:io`) | Dart runtime সরাসরি OS-কে ডাকে — তাই `http` বা `dio`-তে plugin লাগে না |
| Process চালু করা আর মারা | Android (system_server, Zygote) |
| Lifecycle | Android। Flutter শুধু শোনে (`AppLifecycleState`) |
| Permission, notification, background কাজ, camera | Android। Flutter-এ plugin দিয়ে |
| Window, keyboard (IME), accessibility (TalkBack) | Android। Flutter এদের সাথে সেতু বানায় |

**Flutter-এর নিজের তিন স্তর:**

```
┌──────────────────────────────────────────────────────────┐
│ Framework (Dart)  — Material, Widgets, Rendering, Gestures │  ← আপনার code এখানে
├──────────────────────────────────────────────────────────┤
│ Engine (C++)      — Dart runtime, Impeller, text, channel  │  ← libflutter.so
├──────────────────────────────────────────────────────────┤
│ Embedder          — Android-এ FlutterActivity, FlutterView,│  ← OS-এর সাথে সেতু
│                     FlutterJNI (Java/Kotlin)               │
└──────────────────────────────────────────────────────────┘
```

Embedder বদলালেই একই toolkit iOS আর desktop-এ চলে (web-এ C++ engine-এর জায়গায় browser-এর জন্য আলাদা করে লেখা engine চলে)। Toolkit portable হয় এজন্যই। আর Android হলো উল্টো: পুরো OS, তার ওপর framework, তার ভেতরে নিজের UI system।

**"Everything is a widget" মানে কী।** পুরনো Android View-এ padding, click, background, alpha — সবই একটা View-এর property। `View` class নিজেই হাজার হাজার লাইনের। আর ক্ষমতা আসে inheritance থেকে: `TextView` → `Button` → `CompoundButton` → `CheckBox`। Flutter-এ প্রতিটা কাজ একটা আলাদা ছোট widget। একটার ভেতরে আরেকটা বসিয়ে (composition) বড় জিনিস বানান।

একই note card, তিনভাবে:

```xml
<!-- পুরনো Android View: সব কিছু একটা View-এর attribute -->
<TextView
    android:text="আজকের নোট"
    android:padding="16dp"
    android:background="@color/yellow"
    android:alpha="0.8"
    android:onClick="openNote" />
```

```dart
// Flutter: প্রতিটা কাজ আলাদা widget, বাইরে থেকে ভেতরে
Opacity(
  opacity: 0.8,
  child: GestureDetector(
    onTap: openNote,
    child: ColoredBox(
      color: Colors.yellow,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: const Text('আজকের নোট'),
      ),
    ),
  ),
)
```

```kotlin
// Compose: UI হলো composable, আর সাজানো হয় Modifier-এ — একই ক্রমে, বাইরে থেকে ভেতরে
Text(
    text = "আজকের নোট",
    modifier = Modifier
        .alpha(0.8f)
        .clickable(onClick = openNote)
        .background(Yellow)
        .padding(16.dp),
)
```

**কেন এই design:** একটাই ধারণা শিখলেই হয়। যেকোনো টুকরো বদলানো যায়। আর ছোট ছোট widget হলে rebuild সস্তা থাকে। দাম হলো nesting গভীর হয়ে যায়। Compose এখানে মাঝামাঝি: UI-টা composable, কিন্তু padding, click, background-এর মতো সাজসজ্জা Modifier-এ।

**Senior-এর সূক্ষ্ম কথা:** কথাটা ১০০% সত্য না। Widget শুধু config। `State`, `Element`, `RenderObject`, `AnimationController`, `ThemeData` — এগুলো widget না। সঠিকভাবে বললে: "UI-র প্রতিটা অংশ widget দিয়ে বর্ণনা করা হয়"।

**ফাঁদ:** "Flutter native widget-কে wrap করে" বলা। ভুল — Flutter প্রতিটা pixel নিজে আঁকে। Android জানেই না screen-এ একটা button আছে।

[উপরে ফিরুন](#toc)

### <a id="ch13-2"></a>১৩.২ তিনটা runtime: JVM, ART আর Dart

**এক লাইনে:** Computer-এ build চালায় **JVM**। Phone-এ Kotlin আর Java চালায় **ART**। Dart চালায় **Dart runtime** — debug-এ JIT-সহ পুরো VM, release-এ শুধু আগে থেকে compile করা machine code।

| কোথায় | Runtime | কী চালায় |
|---|---|---|
| আপনার computer | JVM (JDK-র ভেতরে) | Gradle, Android Gradle Plugin, Kotlin compiler, R8, Android Studio নিজে |
| আপনার computer | Dart VM | `flutter` tool নিজে (এটা Dart-এ লেখা), analyzer, `build_runner`, `flutter test` |
| Phone | ART | Activity, plugin-এর Kotlin/Java, Jetpack, Compose — সব `.dex` |
| Phone, debug build | Dart VM, JIT সহ | আপনার Dart code। Hot reload এজন্যই সম্ভব। |
| Phone, release build | Dart runtime, JIT ছাড়া | `libapp.so`-এর machine code |

**"Java runtime" — দুইটা আলাদা জিনিস গুলিয়ে যায়:**

- **JVM** Java bytecode (`.class`) চালায়, আপনার computer-এ। Gradle JVM-এর ওপর চলে। তাই Flutter project-ও JDK ছাড়া Android build করতে পারে না। নতুন Android Gradle Plugin-এর জন্য JDK 17 বা তার নতুন লাগে। Flutter default-এ Android Studio-র সাথে আসা JDK (JBR) নেয়। কোনটা নিচ্ছে, তা `flutter doctor -v`-এ দেখবেন। বদলাতে চাইলে `flutter config --jdk-dir <path>`।
- **ART** phone-এ চলে। এটা Java bytecode চালায় না, চালায় `.dex`। **Android-এ কোনো JVM নেই।**

**Kotlin code-এর যাত্রা:**

```
.kt ──kotlinc──► .class (JVM bytecode) ──D8 / R8──► classes.dex ──phone-এ──► ART
                                                                ├ interpreter: প্রথমে
                                                                ├ JIT: বেশি চলা method চলার সময় compile
                                                                └ AOT (dex2oat): profile দেখে, phone idle থাকলে
```

Baseline Profile দিলে গুরুত্বপূর্ণ code install-এর সময়ই AOT হয়ে যায়। তাই প্রথম launch থেকেই দ্রুত।

**Dart code-এর যাত্রা:**

```
debug:   .dart ──frontend_server──► kernel (.dill) ──phone-এ──► Dart VM, JIT     ← hot reload
release: .dart ──frontend_server──► kernel ──gen_snapshot──► libapp.so (ARM machine code)
```

**মজার কথা: একটা Flutter app-এ দুইটা runtime পাশাপাশি চলে।** একই process-এ ART আর Dart runtime থাকে, যাদের heap আলাদা আর garbage collector-ও আলাদা। Dart-এর object ART দেখে না, ART-এর object-ও Dart দেখে না। কথা হয় message দিয়ে (platform channel), অথবা FFI/JNI দিয়ে। এজন্যই channel দিয়ে বড় image পাঠানো দামি — data serialize করে copy হয়। আর Android Studio-র Memory Profiler-এ Dart-এর heap Java heap হিসেবে দেখায় না। ওটা দেখতে DevTools-এর Memory tab লাগে।

**ফাঁদ:** "Dart code ART-এ চলে" বা "Android-এ JVM আছে" — দুইটাই ভুল।

[উপরে ফিরুন](#toc)

### <a id="ch13-3"></a>১৩.৩ App খুললে কী হয় — tap থেকে প্রথম frame

**এক লাইনে:** Launcher system-কে বলে, system Zygote থেকে একটা নতুন process fork করে, সেই process-এ Application আর Activity তৈরি হয়, আর প্রথম frame আঁকা হলে splash সরে যায়। Flutter app-এ এর মাঝে একটা ধাপ বেশি: engine চালু করে Dart-এর `main()` চালানো।

**সব app-এর জন্য একই পথ:**

1. **Tap।** Launcher নিজেও একটা app। সে `startActivity(intent)` ডাকে। Intent-এ লেখা থাকে: "এই package-এর LAUNCHER activity খোলো"।
2. **Binder।** Call যায় `system_server` process-এ, ActivityTaskManager-এর কাছে। Binder হলো Android-এ এক process থেকে আরেক process-এ কথা বলার পথ।
3. **আগে splash।** Process তৈরি হওয়ার আগেই system Activity-র theme দেখে একটা starting window দেখায়, যাতে tap-এর সাথে সাথে user কিছু দেখে। Flutter-এ এটাই আপনার `android/app/src/main/res/values/styles.xml`-এর `LaunchTheme`।
4. **Zygote fork।** Process নেই, তাই system Zygote-কে fork করতে বলে। Zygote phone চালু হওয়ার সময় তৈরি একটা process। ART আর হাজার হাজার framework class সে আগে থেকেই load করে রেখেছে। Fork মানে এর একটা copy, আর memory share হয় copy-on-write-এ। তাই একটা তৈরি runtime খুব দ্রুত পাওয়া যায়।
5. **`ActivityThread.main()`।** এটাই নতুন process-এর আসল `main()`। এটা main thread-এ Looper চালু করে — Dart-এর event loop-এর মতো একটা message queue। তারপর system-কে জানায় "আমি তৈরি"।
6. **Application।** ক্রমটা এমন: `Application.attachBaseContext` → সব `ContentProvider.onCreate` → `Application.onCreate`। Firebase-এর মতো SDK এখানে ContentProvider দিয়ে নিজেকে init করে।
7. **Activity।** `MainActivity` তৈরি হয়, তারপর `onCreate` → `onStart` → `onResume`। একটা window তৈরি হয়ে WindowManager-এ যোগ হয়।
8. **প্রথম frame।** পরের vsync-এ measure → layout → draw। RenderThread GPU দিয়ে আঁকে, আর SurfaceFlinger সেটা screen-এ বসায়। এরপর splash সরে যায়।

**ধাপ ৭-এ এসে দুই পথ আলাদা হয়:**

- **Native (Compose):** `onCreate`-এ `setContent { }`। Compose UI tree তৈরি হয়, তারপর প্রথম frame।
- **Flutter:** `MainActivity : FlutterActivity`-এর `onCreate`-এ:
  1. একটা `FlutterEngine` তৈরি হয় (বা cache থেকে নেওয়া হয়)। `libflutter.so` load হয় — C++-এ লেখা engine।
  2. Engine নিজের thread বানায়: **platform thread** (এটাই Android-এর main thread; Flutter 3.29 থেকে Dart code-ও এখানে চলে), **raster thread** (GPU-র কাজ), আর **I/O thread** (image decode-এর মতো কাজ)।
  3. `libapp.so` খুঁজে নেয় — আপনার compile করা Dart code।
  4. `configureFlutterEngine`-এ `GeneratedPluginRegistrant` সব plugin register করে। Plugin-এর Kotlin অংশ এখানে তৈরি হয়।
  5. একটা `FlutterView` তৈরি হয়। ভেতরে আছে একটা `SurfaceView` — Android-এর কাছে চাওয়া একটা খালি জানালা, যেখানে engine নিজে আঁকবে।
  6. Dart entrypoint চলে: আপনার `main()` → `runApp()` → widget tree।
  7. Engine প্রথম frame আঁকে। ততক্ষণ Flutter Android-কে আঁকতে দেয় না, তাই splash থেকে যায়। Frame আঁকা হলেই splash সরে।

```
 tap
  │
  ▼
Launcher ──Binder──► system_server (ActivityTaskManager)
                         │  splash দেখাও (LaunchTheme)
                         │  process নেই → Zygote, fork করো
                         ▼
                  নতুন process: ActivityThread.main()   ← main thread + Looper
                         │
                         ▼
                  Application (ContentProvider → onCreate)
                         │
                         ▼
                  MainActivity.onCreate
               ┌─────────┴──────────────────────────┐
          Native (Compose)                       Flutter
          setContent { }                         FlutterEngine: libflutter.so load
               │                                 thread তৈরি, plugin register
               │                                 FlutterView (SurfaceView)
               │                                 Dart main() → runApp()
               ▼                                      ▼
          প্রথম frame (HWUI)                      প্রথম frame (Impeller)
               └─────────┬──────────────────────────┘
                         ▼
                SurfaceFlinger → screen, splash সরে
```

**Cold, warm, hot:**
- **Cold:** process নেই। উপরের পুরো পথ।
- **Warm:** process আছে, কিন্তু Activity নেই। ধাপ ৪–৬ বাদ যায়।
- **Hot:** Activity আছে, শুধু সামনে আনা হয়।

Flutter-এর cold start একটু ভারী। Engine load হয়, Dart চালু হয়, আর প্রথম frame-এর আগে `main()`-এ `runApp`-এর আগের সব `await` শেষ হতে হয়।

**ফাঁদ:** `main()`-এ `runApp`-এর আগে Firebase, database, remote config সব `await` করা। তাতে splash অনেকক্ষণ আটকে থাকে। Native-এ একই ভুল হয় `Application.onCreate`-এ। দুই জায়গাতেই নিয়ম একই: প্রথম frame-এর আগে শুধু যা না হলেই নয়, বাকিটা পরে।

[উপরে ফিরুন](#toc)

### <a id="ch13-4"></a>১৩.৪ একটা লেখা screen-এ আসা: `Text('আজকের নোট')`

**এক লাইনে:** দুই দিকেই একই চার ধাপ — বর্ণনা, মাপ, আঁকার নির্দেশ, GPU। পার্থক্য শুধু কে আঁকে: Flutter-এ Flutter-এর নিজের engine, আর native-এ Android-এর নিজের renderer।

**Flutter-এ:**

```dart
const Text('আজকের নোট')
```

1. **Widget।** `Text` একটা `StatelessWidget`। তার `build()` ফেরত দেয় `RichText`।
2. **Element আর RenderObject।** `RichText`-এর জন্য একটা element তৈরি হয়, আর সে একটা `RenderParagraph` বানায়। `Text` নিজে কিছু আঁকে না, আঁকে `RenderParagraph`।
3. **Layout।** Parent constraint দেয়, যেমন "সর্বোচ্চ ৩৬০ চওড়া"। `RenderParagraph` engine-কে লেখাটা মাপতে বলে। Engine font খোঁজে, তারপর HarfBuzz দিয়ে **shaping** করে। বাংলার জন্য এটা খুব জরুরি: "ন" আর "ো" মিলে "নো" হয়, আর যুক্তাক্ষরও এখানেই তৈরি হয়। তারপর line ভাঙে আর size ফেরত দেয়।
4. **Paint।** `RenderParagraph.paint()` canvas-এ লেখে "এই জায়গায় এই paragraph আঁকো"। এটা আসল আঁকা না। এটা একটা নির্দেশের তালিকা (display list), যেটা একটা layer-এর ভেতরে থাকে।
5. **Raster।** Layer tree raster thread-এ যায়। Impeller glyph-গুলো একটা texture-এ রাখে (glyph atlas)। তারপর GPU-কে Vulkan command দেয়: "এই texture থেকে এই অক্ষরগুলো এখানে বসাও"।
6. **Screen।** GPU `FlutterView`-এর surface-এর buffer-এ আঁকে। SurfaceFlinger সেই buffer-কে status bar আর বাকিদের সাথে মিলিয়ে display-এ পাঠায়।

**Compose-এ:**

```kotlin
Text("আজকের নোট")
```

1. **Composition।** Compose runtime function-টা চালায় আর ফল মনে রাখে (slot table-এ)। UI tree-তে একটা `LayoutNode` বসায়, সাথে text-এর জন্য একটা modifier node।
2. **Measure আর layout।** Compose Android-এর নিজের text system ডাকে: `StaticLayout`, যার ভেতরে Minikin আর HarfBuzz। Font আসে phone-এর system font থেকে (বাংলার জন্য Noto Sans Bengali), যদি না আপনি নিজের font দেন।
3. **Draw।** Android `Canvas`-এ text আঁকা হয়। এটাও আসলে recording — `AndroidComposeView`-এর `RenderNode`-এ একটা display list।
4. **RenderThread।** Main thread-এর কাজ শেষ হলে Android-এর renderer **HWUI** নিজের আলাদা thread-এ (RenderThread) display list পড়ে। তারপর Skia দিয়ে GPU command বানায় (OpenGL ES বা Vulkan)।
5. **Screen।** Window-এর surface-এ আঁকা হয় → SurfaceFlinger → display।

**পাশাপাশি:**

| ধাপ | Flutter | Compose |
|---|---|---|
| বর্ণনা | `Text` widget → `RichText` | `@Composable Text` → `LayoutNode` |
| State আর জায়গা কে রাখে | Element | Composition (slot table) |
| Text মাপে | `RenderParagraph` → engine-এর text layout + HarfBuzz | `StaticLayout` (Minikin + HarfBuzz) |
| Font | app-এর font, না পেলে system font | system font, বা app-এর font |
| আঁকার নির্দেশ | layer tree (display list) | `RenderNode`-এর display list |
| কোন thread GPU-র কাজ করে | Flutter-এর raster thread | Android-এর RenderThread |
| GPU-তে পাঠায় | Impeller (Vulkan / OpenGL ES) | HWUI → Skia (OpenGL ES / Vulkan) |
| শেষে | SurfaceFlinger | SurfaceFlinger |

**এখান থেকে বড় শিক্ষা:** Android জানে না যে Flutter-এর screen-এ একটা "Text" আছে। ওর কাছে শুধু pixel। এজন্যই TalkBack-এর জন্য Flutter আলাদা একটা semantics tree বানিয়ে Android-কে দেয়। আর Google Map বা WebView-এর মতো native View বসাতে Platform View লাগে। Compose-এর এই সমস্যা নেই, কারণ সে Android-এর নিজের UI system-এর ভেতরেই থাকে।

[উপরে ফিরুন](#toc)

### <a id="ch13-5"></a>১৩.৫ দুই renderer: HWUI বনাম Impeller, আর SurfaceFlinger

**এক লাইনে:** Native Android আঁকে **HWUI** দিয়ে (ভেতরে Skia), Flutter আঁকে নিজের **Impeller** দিয়ে। দুইজনের আঁকা ছবি শেষে **SurfaceFlinger** মিলিয়ে screen-এ পাঠায়।

**নামগুলো:**

- **HWUI (Hardware UI)।** Android framework-এর C++ renderer। এটা RenderThread-এ চলে, আর Android 9 থেকে ভেতরে Skia দিয়ে OpenGL ES বা Vulkan-এ আঁকে। পুরনো View আর Compose দুইটাই এটা ব্যবহার করে।
- **Impeller।** Flutter engine-এর নিজের renderer। এটা raster thread-এ চলে। Android 10+ (API 29) device-এ Vulkan থাকলে Vulkan ব্যবহার করে, না থাকলে OpenGL ES-এ fallback করে। আগে Flutter-ও Skia দিয়ে আঁকত।
- **SurfaceFlinger।** System-এর compositor process। প্রতিটা window নিজের buffer-এ আঁকে: আপনার app, status bar, navigation bar, keyboard। SurfaceFlinger সব buffer মিলিয়ে একটা ছবি বানায়, আর Hardware Composer (HWC) দিয়ে display-তে পাঠায়।
- **Vsync।** Display প্রতি ১৬.৭ ms (60Hz) বা ৮.৩ ms (120Hz) পর পর একটা সংকেত দেয়, "নতুন frame দাও"। Android-এ `Choreographer` এই সংকেত app-কে দেয়। Flutter engine-ও এই `Choreographer` থেকেই vsync নেয়।

```
          Native app                              Flutter app
 main thread: measure/layout/draw       platform thread: build/layout/paint (Dart)
          │ display list                           │ layer tree
          ▼                                        ▼
 RenderThread: HWUI → Skia               raster thread: Impeller
          │ OpenGL ES / Vulkan                     │ Vulkan / OpenGL ES
          ▼                                        ▼
     window-এর surface                       FlutterView-এর surface
          └─────────────────┬──────────────────────┘
                            ▼
           SurfaceFlinger (+ HWC)  ← status bar, keyboard-ও এখানে মেশে
                            ▼
                         display
```

**Impeller কেন এল:** Skia shader তৈরি করত চলার সময়ে। কোনো animation প্রথমবার চললে shader বানাতে সময় লাগত, আর frame miss হতো — একে বলে shader compilation jank। Impeller-এর সব shader engine build-এর সময়েই compile করা থাকে। তাই প্রথম frame থেকেই মসৃণ।

**Jank কোথায় খুঁজবেন:** একটা frame-এর সময়ের মধ্যে দুইটা thread-কেই কাজ শেষ করতে হয় — UI-র thread আর GPU-র thread। Flutter DevTools-এ এরা দুইটা bar: UI আর Raster। Android-এ Perfetto system trace-এ main thread আর RenderThread।

**ফাঁদ:** "Compose-ও Flutter-এর মতো নিজে আঁকে" বলা। না — Compose Android-এর View system-এর ভেতরে থাকে (একটা `AndroidComposeView`) আর HWUI দিয়েই আঁকে। তাই Compose আর পুরনো View এক screen-এ সহজে মেশে, আর Flutter-কে native View বসাতে বাড়তি কাজ করতে হয়।

[উপরে ফিরুন](#toc)

### <a id="ch13-6"></a>১৩.৬ Gradle কী করে, আর release APK বানালে কী হয়

**এক লাইনে:** Gradle একটা build automation tool। সে task-এর তালিকা বানায়, কোনটা কার আগে লাগবে ঠিক করে, আর যেটা বদলায়নি সেটা বাদ দেয়। Android Gradle Plugin (AGP) এতে Android-এর task যোগ করে। Flutter-ও Android build-এর জন্য এই Gradle-ই চালায়।

**Flutter-এ কি Gradle লাগে?** হ্যাঁ, Android-এর জন্য সবসময়। `flutter run` আর `flutter build apk` দুইটাই ভেতরে `android/` folder-এ Gradle চালায়। প্রথম `flutter run` ধীর হয় এজন্যই: Gradle download হয়, dependency download হয়, daemon চালু হয়। iOS-এ Gradle নেই। সেখানে Xcode (`xcodebuild`), আর CocoaPods বা Swift Package Manager।

**Gradle-এর তিন ধাপ:**
1. **Initialization।** `settings.gradle.kts` পড়ে দেখে কোন কোন module আছে। Flutter project-এ প্রতিটা plugin-ও একটা আলাদা module।
2. **Configuration।** প্রতিটা `build.gradle.kts` চালিয়ে task-এর graph বানায়।
3. **Execution।** যে task চাওয়া হয়েছে (যেমন `assembleRelease`), শুধু সেটা আর তার আগে যা লাগে সেগুলো চালায়। যার input বদলায়নি, সেটা "UP-TO-DATE" হিসেবে বাদ যায়।

**Gradle-এর আরও কিছু টুকরো:**
- **Wrapper:** `gradlew` আর `gradle-wrapper.properties`। Project নিজের Gradle version ঠিক করে রাখে, তাই সবাই একই version পায়।
- **Daemon:** পেছনে চলতে থাকা একটা JVM process, যাতে পরের build দ্রুত হয়।
- **Cache:** `~/.gradle/caches`-এ dependency আর build output।
- **Maven repository:** `google()` আর `mavenCentral()` থেকে library আসে — pub.dev-এর জায়গায়।

**Native: `./gradlew assembleRelease`**

1. **Manifest merge।** App আর সব library-র manifest মিলিয়ে একটা।
2. **Resource।** AAPT2 সব `res/` compile করে, আর `R` class ও `resources.arsc` বানায়।
3. **Code generation।** KSP চলে, Room আর Hilt-এর code বানায়।
4. **Compile।** `kotlinc` আর `javac` → `.class`।
5. **R8** (`isMinifyEnabled = true` দিলে)। Shrink (অব্যবহৃত code বাদ), optimize, obfuscate (নাম ছোট), আর dex — সব একসাথে → `classes.dex`। না দিলে শুধু D8 dex বানায়।
6. **Native library।** সব `.so` file জমা হয় (`lib/arm64-v8a/...`)।
7. **Package।** সব zip করে APK বানানো হয় আর align করা হয়।
8. **Sign।** Release keystore দিয়ে sign। Sign ছাড়া APK install হয় না।

ফল: `app/build/outputs/apk/release/app-release.apk`।

**Flutter: `flutter build apk --release`**

1. **Flutter tool** (Dart-এ লেখা) `pubspec.yaml` দেখে, `pub get` চালায়, আর plugin-এর তালিকা থেকে `GeneratedPluginRegistrant` আর Gradle-এর জন্য plugin list বানায়।
2. তারপর Gradle চালায়: `gradlew assembleRelease`।
3. Flutter Gradle Plugin একটা task যোগ করে (`compileFlutterBuildRelease`)। এই task আবার Flutter tool-কে ডাকে Dart অংশ build করতে:
   - **`frontend_server`:** Dart → kernel (`.dill`)। অব্যবহৃত code বাদ যায় (tree shaking)।
   - **`gen_snapshot`:** kernel → প্রতিটা ABI-র (arm64, arm, x86_64) machine code → `libapp.so`।
   - **Asset:** image, font আর `pubspec`-এর asset যায় `flutter_assets/`-এ। Material Icons font থেকে শুধু ব্যবহৃত icon রাখা হয় (icon tree shaking)।
4. বাকিটা native-এর মতোই: plugin-এর Kotlin/Java compile, R8, resource, release version-এর `libflutter.so` যোগ, package, sign।

ফল: `build/app/outputs/flutter-apk/app-release.apk`।

**APK খুলে দেখুন।** APK আসলে একটা zip। Android Studio-র APK Analyzer দিয়ে খোলা যায়:

```
app-release.apk
├── AndroidManifest.xml          (binary)
├── classes.dex                  Kotlin/Java: FlutterActivity, plugin, Jetpack
├── resources.arsc, res/         icon, LaunchTheme, string
├── lib/arm64-v8a/
│   ├── libflutter.so            Flutter engine (C++)            ← শুধু Flutter app-এ
│   └── libapp.so                আপনার Dart code, machine code  ← শুধু Flutter app-এ
├── assets/flutter_assets/       image, font, AssetManifest      ← শুধু Flutter app-এ
└── META-INF/                    signature-এর কিছু তথ্য
```

Flutter APK native-এর চেয়ে বড় হয় মূলত `libflutter.so`-র জন্য, আর প্রতিটা ABI-র জন্য আলাদা `.so` থাকার জন্য। AAB দিলে Play প্রতিটা phone-কে শুধু তার ABI-র অংশ দেয়।

**ফাঁদ:**
- **Flutter template-এ release build default-এ debug key দিয়ে sign হয়।** নিজের keystore না বসালে "release" APK আসলে debug key-তে sign হয়। Play সেটা নেয় না।
- **R8 শুধু Kotlin আর Java ছোট করে।** Dart obfuscate করতে আলাদা `--obfuscate --split-debug-info` লাগে।
- **`flutter clean` error-এর কারণ দেখায় না।** এটা `build/`, `.dart_tool/` আর কিছু generated file মোছে, কিন্তু Gradle-এর cache (`~/.gradle`) থেকে যায়। Gradle-এর error-এর আসল কারণ দেখতে `cd android && ./gradlew assembleRelease --stacktrace` চালান।

[উপরে ফিরুন](#toc)

### <a id="ch13-7"></a>১৩.৭ পুরো ecosystem এক ছবিতে

```
আপনার computer
├── Android Studio (IDE) — সাথে একটা JDK (JBR)
├── JDK → JVM: Gradle, AGP, kotlinc, KSP, R8 চালায়
├── Android SDK
│   ├── platforms/android-36/android.jar   compileSdk-এর API
│   ├── build-tools/   aapt2, d8, zipalign, apksigner
│   ├── platform-tools/   adb (phone-এর সাথে কথা)
│   ├── emulator/
│   └── ndk/   C/C++ — Flutter-এ AGP এটা দিয়ে .so strip করে
├── Flutter SDK
│   ├── flutter tool (Dart-এ লেখা)
│   ├── Dart SDK: dart, pub, analyzer, frontend_server
│   └── engine artifact: আগে থেকে build করা libflutter.so (mode × ABI), gen_snapshot
└── Package-এর উৎস: pub.dev (Dart), Maven — google(), mavenCentral() (Kotlin/Java)

Phone
├── Linux kernel — process, memory, Binder driver
├── Zygote — প্রতিটা app process এখান থেকে fork হয়
├── system_server — ActivityManager, WindowManager, PackageManager ...
├── SurfaceFlinger — screen-এর compositor
├── Google Play Services — আলাদা app (FCM, location, Play Integrity)
└── আপনার app process
    ├── ART: Activity, plugin, Jetpack
    └── (Flutter হলে) libflutter.so + libapp.so: Dart runtime, Impeller
```

**কোন tool কী, Flutter-এর পাশে:**

| Android | কাজ | Flutter-এ যা চিনতেন |
|---|---|---|
| Gradle | build চালায় | `flutter build` — যেটা ভেতরে Gradle-কেই ডাকে |
| AGP | Android build-এর নিয়ম | Flutter Gradle Plugin (AGP-এর ওপরে বসে) |
| Maven repository | library-র দোকান | pub.dev |
| `gradlew` (wrapper) | Gradle version ঠিক রাখে | FVM দিয়ে Flutter version ঠিক রাখা |
| D8 / R8 | dex বানায়, ছোট করে | `gen_snapshot`, tree shaking, `--obfuscate` |
| ART | app-এর code চালায় | Dart VM / Dart runtime |
| HWUI + Skia | UI আঁকে | Impeller |
| adb | install, log, shell | `flutter install`, `flutter logs` — ভেতরে adb |
| Logcat, Layout Inspector, Perfetto | log, UI আর performance দেখা | DevTools |

> **মনে রাখুন**
> - Flutter = UI toolkit (framework + engine + embedder)। Process, lifecycle, permission — Android-এর।
> - Computer-এ JVM চালায় build। Phone-এ ART চালায় Kotlin, আর Dart runtime চালায় Dart। Android-এ JVM নেই।
> - App খোলা: Launcher → system_server → Zygote fork → Application → Activity → প্রথম frame। Flutter-এ মাঝে engine load আর Dart `main()`।
> - Native আঁকে HWUI (ভেতরে Skia), Flutter আঁকে Impeller। দুইটাই শেষে SurfaceFlinger।
> - Flutter-এর Android build মানে Gradle। Dart অংশ `gen_snapshot` দিয়ে `libapp.so` হয়।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter একটা UI toolkit — framework, engine আর embedder। App খুললে Zygote থেকে process fork হয়, তারপর Application আর FlutterActivity তৈরি হয়। FlutterActivity engine load করে, Dart-এর main চালায়, আর Impeller দিয়ে একটা SurfaceView-তে নিজে আঁকে। Native app সেখানে Android-এর HWUI দিয়ে আঁকে। দুই ক্ষেত্রেই শেষে SurfaceFlinger ছবিটা screen-এ বসায়। Build-এ Flutter Gradle চালায়: Kotlin dex হয়ে ART-এ চলে, আর Dart AOT compile হয়ে libapp.so-তে machine code হয়।"
> - *English:* "Flutter is a UI toolkit: a framework, an engine and an embedder. When the app opens, Zygote forks a process, then the Application and FlutterActivity are created. FlutterActivity loads the engine, runs Dart's main, and draws by itself into a SurfaceView with Impeller. A native app draws with Android's HWUI instead. In both cases SurfaceFlinger puts the final image on screen. For the build, Flutter runs Gradle: Kotlin becomes dex and runs on ART, and Dart is AOT-compiled into machine code in libapp.so."

[উপরে ফিরুন](#toc)

---

## <a id="ch14"></a>১৪. শেখার পরিকল্পনা — ৪ সপ্তাহ

পড়ে শেখার চেয়ে বানিয়ে শেখা অনেক দ্রুত। আর আপনার জন্য সবচেয়ে দ্রুত পথ হলো: **যে Notes app এই বই জুড়ে দেখলেন, সেটা native-এ বানানো।** প্রতিটা অংশ Flutter-এ কীভাবে লিখতেন, তা আপনি আগেই জানেন — শুধু অনুবাদ করবেন।

| সপ্তাহ | পড়ুন | বানান |
|---|---|---|
| ১ | [০](#ch0), [১](#ch1), [২](#ch2) | [Kotlin Koans](https://play.kotlinlang.org/koans)-এর প্রথম অর্ধেক। তারপর playground-এ Notes-এর model (`data class`, `sealed`), আর একটা `Flow` দিয়ে search debounce। |
| ২ | [৩](#ch3)–[৬](#ch6) | Android Studio-তে নতুন project। Notes list, note খোলা, নতুন note-এর form — শুধু memory-র data দিয়ে। Phone ঘুরিয়ে দেখুন কী হারায়, তারপর ঠিক করুন। |
| ৩ | [৭](#ch7)–[৯](#ch9) | Navigation, ViewModel + `UiState`, Hilt। Room-এ note রাখুন। একটা fake API (বা যেকোনো free mock server) থেকে Retrofit দিয়ে sync। `adb shell am kill` দিয়ে process death test। |
| ৪ | [১০](#ch10)–[১৩](#ch13) | WorkManager দিয়ে background sync, reminder notification। ViewModel test, একটা Compose UI test। Release build-এ R8 চালু করে চালান, তারপর APK Analyzer-এ খুলে দেখুন ভেতরে কী আছে। |

**প্রতিদিনের শেষে তিনটা প্রশ্ন:**
1. আজ যেটা লিখলাম, Flutter-এ সেটা কী দিয়ে করতাম? পার্থক্যটা কোথায়, আর কেন?
2. Phone ঘোরালে বা process মরলে এটা টিকবে?
3. এটা কোন thread-এ চলছে?

এই তিন প্রশ্নের উত্তর মুখে বলতে পারলে আপনি interview-এর জন্য তৈরি। শেষে [Android Interview Prep](../../interviews/software-engineer-flutter-android-ios-bn/flutter-android-ios-interview-prep-bn.md) খুলে প্রশ্নগুলো জোরে জোরে বলে অনুশীলন করুন — ওখানে প্রতিটা উত্তর বাংলা আর English-এ আছে।

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
| Dart VM / Dart runtime | ART |
| Impeller | HWUI (ভেতরে Skia) |
| `libapp.so` (`gen_snapshot`) | `classes.dex` (D8 / R8) |
| `flutter build apk` | `./gradlew assembleRelease` (Flutter-ও ভেতরে এটাই চালায়) |
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

---

## <a id="part-ios"></a>খণ্ড ২ — iOS

এবার পাশের আরেকটা শহর। এখানেও আপনি আগে এসেছেন — প্রতিটা Flutter app-এর `ios/` folder-এ একটা পুরো iOS project আছে। খণ্ড ১-এর মতোই প্রতিটা জিনিস আগে Flutter-এ, তারপর iOS-এ (Swift, SwiftUI), আর যেখানে কাজে লাগে, Android-এর সাথে এক লাইনের তুলনা।

[উপরে ফিরুন](#toc)

---

## <a id="ios0"></a>iOS ০. বড় ছবি — আপনার Flutter app আসলে একটা iOS app

**এক লাইনে:** iOS-এও Flutter শুধু UI আঁকে আর Dart চালায়। App চালু হওয়া, lifecycle, permission, notification, background কাজ, signing — সব iOS-এর। Flutter-এ এগুলো plugin-এর আড়ালে ছিল। এখন আড়ালটা সরাব।

Android অংশে আপনি এই গল্পটা একবার পড়েছেন ([অধ্যায় ০](#ch0))। ছাঁচ একই। শুধু নামগুলো বদলাবে, আর কিছু নিয়ম আরও কড়া হবে। এই অধ্যায় বুঝলে iOS-এর বাকি সব জায়গামতো বসবে।

> **Version নিয়ে:** লেখা নভেম্বর ২০২৬-এ। তখন সর্বশেষ Xcode 27, iOS 27, Swift 6.4, আর Flutter stable 3.47। Apple প্রতি বছর জুনে (WWDC) নতুন version ঘোষণা করে, আর সেপ্টেম্বরে ছাড়ে। তাই কোনো API কোন iOS থেকে আছে, সেটা লেখার পাশে দেওয়া থাকবে।

### <a id="ios0-1"></a>iOS ০.১ আপনার Flutter app আসলে একটা iOS app

আপনার যেকোনো Flutter project-এর `ios/` folder খুলুন। ওটা একটা **পুরো Xcode project।** ভেতরে এই file-টা পাবেন (Flutter 3.41+ template):

```swift
// ios/Runner/AppDelegate.swift
import Flutter
import UIKit

@main
@objc class AppDelegate: FlutterAppDelegate, FlutterImplicitEngineDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

  // Engine তৈরি হলে এখানে plugin register হয়
  func didInitializeImplicitFlutterEngine(_ engineBridge: FlutterImplicitEngineBridge) {
    GeneratedPluginRegistrant.register(with: engineBridge.pluginRegistry)
  }
}
```

পাশে আরেকটা ছোট file:

```swift
// ios/Runner/SceneDelegate.swift
import Flutter
import UIKit

class SceneDelegate: FlutterSceneDelegate {}
```

আর `Runner/Base.lproj/Main.storyboard`-এর প্রথম screen-টা একটা `FlutterViewController`। ব্যস, এটুকুই। User যখন app-এর icon-এ tap করে:

1. iOS একটা process চালু করে। `@main` দেখে বোঝে, শুরু `AppDelegate` থেকে।
2. iOS একটা **scene** (একটা window) বানায়। `SceneDelegate` সেই window-এর দেখাশোনা করে। Window-এ বসে `Main.storyboard`-এর `FlutterViewController`।
3. `FlutterViewController` একটা **`FlutterEngine`** চালায়। Engine-এর ভেতরে Dart runtime চলে, আর আপনার `main()` call হয়। Engine তৈরি হলে `didInitializeImplicitFlutterEngine` আসে, আর সব plugin register হয়।
4. `FlutterViewController`-এর view পুরো screen জুড়ে একটা Metal surface। Flutter সেখানে নিজের widget নিজে আঁকে, **Impeller** দিয়ে। iOS-এ Flutter 3.29 থেকে Impeller-ই একমাত্র renderer। Skia আর বেছে নেওয়া যায় না।
5. Camera, Keychain, notification লাগলে Dart code **platform channel** দিয়ে Swift বা Objective-C code-কে বলে। Plugin মানে এটাই।

```
┌──────────────────────────────── iOS process (sandbox-এর ভেতরে) ──────────────────────────────┐
│                                                                                               │
│  AppDelegate (FlutterAppDelegate)      ← process-এর ঘটনা: launch, push token                  │
│  SceneDelegate (FlutterSceneDelegate)  ← window-এর ঘটনা: সামনে এল, background-এ গেল, URL খুলল  │
│                                                                                               │
│  FlutterViewController (একটা UIViewController)                                               │
│  ┌──────────────────────────────────────────┐        ┌────────────────────────────────────┐   │
│  │  FlutterEngine                           │        │  Plugin-এর iOS code (Swift / ObjC)  │   │
│  │  ┌────────────────────────────────────┐  │ channel│                                    │   │
│  │  │ Dart: widget, Bloc, dio, drift ... │◄─┼────────┼─► Keychain, UserNotifications,      │   │
│  │  └────────────────────────────────────┘  │        │   BGTaskScheduler, AVFoundation     │   │
│  │  Impeller → Metal দিয়ে নিজে আঁকে         │        └────────────────────────────────────┘   │
│  └──────────────────────────────────────────┘                                                 │
│                                                                                               │
│  iOS: lifecycle, suspension, permission, signing, sandbox ...                                 │
└───────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Build-এ কী তৈরি হয়।** `flutter build ipa` চালালে ভেতরে Xcode-এর build চলে। শেষে যে `Runner.app` তৈরি হয়, তার `Frameworks/` folder-এ দুইটা জিনিস থাকে:

| File | ভেতরে কী | Android-এ জোড়া |
|---|---|---|
| `App.framework` | আপনার Dart code, release-এ আগে থেকেই machine code-এ compile করা (AOT) | `libapp.so` |
| `Flutter.framework` | Flutter engine — Dart runtime, Impeller, text layout, channel | `libflutter.so` |

**কেন release-এ AOT বাধ্যতামূলক:** iOS কোনো সাধারণ app-কে চলার সময় নতুন machine code বানিয়ে চালাতে দেয় না। তাই Dart-এর JIT শুধু debug-এ চলে, আর debug app শুধু Xcode বা `flutter run` থেকে খোলা যায়। Release build-এ সব Dart code আগেই machine code হয়ে যায়। Hot reload তাই শুধু debug-এ।

আরও কিছু জিনিস, যা Flutter-এ থেকেও আসলে iOS-এরটাই ব্যবহার করতেন:

| Flutter-এ আপনি যা করতেন | আসলে কী ছিল |
|---|---|
| `ios/Runner/Info.plist`-এ `NSCameraUsageDescription` লেখা | iOS-এর Info.plist — permission-এর কারণ লেখা |
| Xcode-এ Team বেছে signing ঠিক করা | iOS-এর code signing আর provisioning profile |
| `ios/Podfile`, `pod install` | CocoaPods — iOS-এর পুরনো dependency manager |
| `flutter build ipa` | ভেতরে `xcodebuild archive` |
| `shared_preferences` (iOS-এ) | `UserDefaults` |
| `flutter_secure_storage` (iOS-এ) | Keychain |
| `firebase_messaging` (iOS-এ) | APNs (Apple Push Notification service) |
| `workmanager` (iOS-এ) | `BGTaskScheduler` |
| `path_provider` | App-এর sandbox-এর `Documents/`, `Library/` folder |
| `url_launcher` | `UIApplication.open(_:)` |

**তাই এখানেও শূন্য থেকে শুরু না।** পার্থক্য দুই জায়গায়:
- **UI:** Flutter নিজে আঁকে। Native iOS-এ UI-ও iOS-এর — SwiftUI (আগে UIKit)।
- **ভাষা আর runtime:** Dart-এর জায়গায় Swift। Swift সরাসরি machine code-এ compile হয়। কোনো VM নেই, garbage collector-ও নেই — memory চলে reference count দিয়ে ([iOS ১.৫](#ios1-5))।

[উপরে ফিরুন](#toc)

### <a id="ios0-2"></a>iOS ০.২ iOS-এর স্তরগুলো

iOS হলো Apple-এর operating system, আর তার ওপরে app বানানোর framework-এর স্তূপ। নিচ থেকে ওপরে:

```
┌──────────────────────────────────────────────────────────────────┐
│  আপনার app (Swift, SwiftUI, @Observable model ...)                │
├──────────────────────────────────────────────────────────────────┤
│  UI framework — SwiftUI (নতুন), UIKit (পুরনো, এখনো নিচে চলে)      │  ← "Cocoa Touch" স্তর
├──────────────────────────────────────────────────────────────────┤
│  Media — Core Animation, Metal, Core Graphics, AVFoundation      │  ← আঁকা, ছবি, শব্দ, video
├──────────────────────────────────────────────────────────────────┤
│  Core Services — Foundation, SwiftData / Core Data, Core Location,│
│  CloudKit, Network, UserNotifications ...                        │  ← data, network, location
├──────────────────────────────────────────────────────────────────┤
│  Core OS — Security (Keychain), LocalAuthentication (Face ID),   │
│  Core Bluetooth, Accelerate ...                                   │  ← hardware আর security
├──────────────────────────────────────────────────────────────────┤
│  Darwin — XNU kernel (Mach + BSD), process, thread, memory, file │  ← macOS-এর সাথে একই ভিত
└──────────────────────────────────────────────────────────────────┘
```

Android-এর স্তরের সাথে মিলিয়ে দেখুন ([০.২](#ch0-2))। একটা বড় পার্থক্য আছে, আর সেটাই আপনার রোজকার কাজে লাগবে:

- **Android-এ Jetpack আছে।** Compose, Room, ViewModel — এগুলো app-এর সাথে bundle হয়। তাই phone-এর Android version যা-ই হোক, একই code চলে।
- **iOS-এ Jetpack-এর মতো কিছু নেই।** SwiftUI, SwiftData, Observation — সব **OS-এর সাথে আসে।** iOS 17-এর phone-এ iOS 17-এর SwiftUI, iOS 18-এর phone-এ iOS 18-এর SwiftUI।

তাই iOS-এ প্রতিটা নতুন API-র পাশে লেখা থাকে, কোন iOS থেকে আছে। `@Observable` চাইলে iOS 17 লাগবে। `NavigationStack` চাইলে iOS 16। পুরনো phone সমর্থন করলে এভাবে লিখবেন:

```swift
if #available(iOS 17, *) {
    // নতুন API
} else {
    // পুরনো পথ
}
```

Android-এর `Build.VERSION.SDK_INT >= 34`-এর মতো। সুখবর হলো, iPhone user-রা খুব তাড়াতাড়ি নতুন iOS-এ যায়। তাই বেশিরভাগ app শুধু শেষ দুই-তিনটা iOS সমর্থন করে। Minimum version-কে বলে **deployment target** ([iOS ৩.৮](#ios3-8))।

**Swift runtime-ও OS-এর অংশ।** iOS 12.2 থেকে Swift-এর standard library phone-এই থাকে। তাই app-এর ভেতরে Swift runtime ভরতে হয় না।

[উপরে ফিরুন](#toc)

### <a id="ios0-3"></a>iOS ০.৩ iOS আর Android-এর বড় পার্থক্য

Android থেকে আসলে চারটা জিনিস প্রথম দিনেই ধাক্কা দেবে।

**১. Sandbox — প্রতিটা app নিজের বাক্সে।** iOS-এ প্রতিটা app-এর নিজের একটা folder আছে (`Documents/`, `Library/`, `tmp/`)। অন্য app-এর file দেখা যায় না, shared storage-এ ইচ্ছামতো লেখা যায় না। দুই app-এর মধ্যে data ভাগ করতে App Group লাগে, আর সেটা entitlement দিয়ে আগে ঘোষণা করতে হয় ([iOS ৩.৭](#ios3-7))। Android-এও sandbox আছে, কিন্তু iOS-এরটা অনেক কড়া।

**২. Background-এ app ঘুমিয়ে পড়ে (suspension)।** Android-এ background-এ কিছু কাজ চলতে পারে, আর foreground service দিয়ে অনেকক্ষণ চালানো যায়। iOS-এ user home-এ গেলে app অল্প সময় পায়। তারপর **suspend** হয় — memory-তে থাকে, কিন্তু একটা লাইন code-ও চলে না। Background-এ কাজ করতে হলে iOS-এর দেওয়া নির্দিষ্ট পথ নিতে হয় (background task, push, background mode)। আর suspend থাকা app-কে system কোনো খবর না দিয়ে মেরে দিতে পারে ([iOS ৪.৪](#ios4-4))।

**৩. একটাই store, আর প্রতিটা release-এ review।** Android-এ Play Store ছাড়াও APK দিয়ে app দেওয়া যায়। iOS-এ App Store-ই প্রায় একমাত্র পথ। কিছু অঞ্চলে (যেমন EU) আইনের কারণে বিকল্প marketplace আছে, কিন্তু বেশিরভাগ দেশে নেই। প্রতিটা নতুন version Apple-এর review পার হতে হয়। আর upload-এর জন্য নির্দিষ্ট Xcode লাগে — ২৮ এপ্রিল ২০২৬ থেকে Xcode 26 বা নতুন, iOS 26 SDK দিয়ে build।

**৪. Signing সব জায়গায়।** Android-এ debug build একটা debug key দিয়ে নিজে থেকেই sign হয়। iOS-এ নিজের phone-এ চালাতেও signing লাগে: Apple Developer account, certificate, App ID, provisioning profile। Push বা App Group চাইলে সেটা entitlement-এ লিখতে হয়, আর profile-এও থাকতে হয়। Flutter-এ Xcode-এ "Team" বেছে দিয়ে আপনি এর একটা অংশ দেখেছেন।

আরও কিছু ছোট পার্থক্য:

| বিষয় | iOS | Android |
|---|---|---|
| System back button | নেই — বাম কিনারা থেকে swipe, আর navigation bar-এর back | আছে — button বা gesture |
| Rotation বা dark mode বদল | Screen বেঁচে থাকে, শুধু layout বদলায় (Flutter-এর মতো) | Activity মরে নতুন হয় |
| অন্য app-এর সাথে কথা | URL scheme, universal link, share sheet | `Intent`, অনেক বেশি খোলা |
| Device | অল্প কয়েকটা মডেল, এক কোম্পানি | হাজারো মডেল |
| Renderer (Flutter) | Impeller, Metal-এর ওপর, একমাত্র পথ | Impeller (Vulkan বা OpenGL ES) |

[উপরে ফিরুন](#toc)

### <a id="ios0-4"></a>iOS ০.৪ পুরো framework-এর মানচিত্র

এটা iOS অংশের সবচেয়ে কাজের table। বাম দিকে কাজটা। তারপর আজকের দিনে iOS-এ যেটা নেবেন, পুরনো যেটা চিনে রাখবেন, Android-এ কী, আর Flutter-এ কী।

| কাজ | iOS — আজকের best | পুরনো iOS (চিনে রাখুন) | Android | Flutter |
|---|---|---|---|---|
| ভাষা | Swift 6 | Objective-C | Kotlin | Dart |
| UI | SwiftUI | UIKit, Storyboard, XIB | Jetpack Compose | Widget |
| List | `List`, `LazyVStack` | `UITableView`, `UICollectionView` | `LazyColumn` | `ListView.builder` |
| Screen-এর state আর logic | `@Observable` class (iOS 17+) | `ObservableObject` + `@Published`; ViewController-এ সব (MVC) | `ViewModel` + `StateFlow` | Cubit / Bloc / Notifier |
| Async কাজ | `async`/`await`, `Task` | GCD (`DispatchQueue`), completion handler | Coroutine | `Future` |
| Data stream | `AsyncSequence`, `AsyncStream` | Combine, delegate, `NotificationCenter` | `Flow` | `Stream` |
| ভাগ করা mutable state রক্ষা | `actor`, `@MainActor` | serial `DispatchQueue`, lock | `Mutex`, single-thread confinement | Isolate (memory ভাগ হয় না) |
| Navigation | `NavigationStack` (iOS 16+) | `UINavigationController`, `NavigationView` | Navigation Compose | `go_router` |
| DI | init-এ দেওয়া + `@Environment` | Singleton, Swinject | Hilt | `get_it`, Riverpod |
| Network | `URLSession` (`async`) | `URLSession` + callback, Alamofire | Retrofit + OkHttp | `dio` |
| JSON | `Codable` | `JSONSerialization` | kotlinx.serialization | `json_serializable` |
| Database | SwiftData (iOS 17+) | Core Data, সরাসরি SQLite, GRDB | Room | `drift`, `sqflite` |
| Key-value | `UserDefaults`, `@AppStorage` | একই | DataStore | `shared_preferences` |
| Secret | Keychain | একই | Keystore | `flutter_secure_storage` |
| Image | `AsyncImage` (cache লাগলে Nuke বা Kingfisher) | SDWebImage | Coil | `cached_network_image` |
| Background কাজ | `BGTaskScheduler` | Background fetch (deprecated) | WorkManager | `workmanager` |
| Local notification | UserNotifications | `UILocalNotification` (deprecated) | `NotificationCompat` | `flutter_local_notifications` |
| Push | APNs (প্রায়ই FCM-এর মাধ্যমে) | | FCM | `firebase_messaging` |
| Permission | প্রতিটা framework-এর নিজের request + Info.plist-এ কারণ | একই | Activity Result API | `permission_handler` |
| অন্য app খোলা | `openURL`, universal link | `UIApplication.openURL(_:)` | `Intent` | `url_launcher` |
| App lifecycle | SwiftUI `App` + `scenePhase` | `AppDelegate` একাই | Activity lifecycle | `AppLifecycleState` |
| Build আর dependency | Xcode + Swift Package Manager | CocoaPods, Carthage | Gradle + version catalog | `pubspec.yaml` |
| Unit test | Swift Testing (`@Test`, `#expect`) | XCTest | JUnit + `runTest` | `test`, `bloc_test` |
| UI test | XCUITest | | Compose UI test | `testWidgets`, `integration_test` |

**পুরনো কলামটা কেন:** Interview-এ, পুরনো project-এ, আর প্রায় সব Flutter plugin-এর iOS code-এ এগুলো দেখবেন। Plugin-এর iOS অংশ এখনো বেশিরভাগ UIKit, GCD আর completion handler-এ লেখা। নতুন code-এ মাঝের কলাম।

**একটা সতর্কতা:** iOS-এ "আজকের best" অনেক সময় deployment target-এর ওপর নির্ভর করে। SwiftData আর `@Observable` চাইলে iOS 17 লাগবে। iOS 16 সমর্থন করতে হলে পুরনো কলামের কিছু জিনিস এখনো লাগবে।

> **মনে রাখুন**
> - আপনার প্রতিটা Flutter app-এর `ios/` একটা পুরো Xcode project। `FlutterViewController` একটা সাধারণ `UIViewController`।
> - Dart code release-এ AOT হয়ে `App.framework`-এ যায়, engine থাকে `Flutter.framework`-এ।
> - iOS-এ Jetpack-এর মতো কিছু নেই। Framework OS-এর সাথে আসে, তাই প্রতিটা API-র একটা minimum iOS আছে।
> - চার বড় পার্থক্য: কড়া sandbox, background-এ suspension, একটাই store আর review, সব জায়গায় signing।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ Flutter একটা `FlutterViewController`-এর ভেতরে চলে। Engine একটা Metal surface-এ Impeller দিয়ে নিজে আঁকে। Release-এ Dart code AOT হয়ে `App.framework`-এ যায়, কারণ iOS JIT দিতে দেয় না। Lifecycle, permission, background কাজ সবসময় iOS-এর। তাই plugin-এর আড়ালে যা ছিল, native-এ সেটা আমি সরাসরি Swift-এ লিখি।"
> - *English:* "On iOS, Flutter runs inside a `FlutterViewController`. The engine draws on a Metal surface with Impeller. In release, Dart is compiled ahead of time into `App.framework`, because iOS doesn't allow JIT for normal apps. Lifecycle, permissions and background work always belong to iOS, so in native I write directly in Swift what plugins used to hide."

[উপরে ফিরুন](#toc)

---

## <a id="ios1"></a>iOS ১. Swift — Dart-এর পাশে

Swift পড়তে গিয়ে আপনার বারবার মনে হবে, "এটা তো চিনি।" `?`, `??`, `async`/`await`, extension, generics — সব আছে। Kotlin-এর সাথে আরও বেশি মিল। কিন্তু দুইটা জিনিস একদম নতুন, আর সেগুলোই Swift-এর প্রাণ:

- **`struct` হলো value type।** Assign করলে copy হয়। Swift-এর প্রায় সব model struct।
- **Garbage collector নেই।** Memory চলে **ARC** (reference count) দিয়ে। তাই retain cycle নিজে খেয়াল রাখতে হয়।

এই দুইটা ভালো করে বুঝলে বাকি Swift একদিনের কাজ। Android অংশে Kotlin-এর অধ্যায়টা ([অধ্যায় ১](#ch1)) পড়ে থাকলে আরও সহজ — জায়গায় জায়গায় Kotlin-ও পাশে রাখছি।

Code চালিয়ে দেখতে Xcode-এ **File → New → Playground** খুলুন। DartPad-এর মতো, লিখলেই চলে।

### <a id="ios1-1"></a>iOS ১.১ Variable আর type

**এক লাইনে:** `final` → `let`, `var` → `var`। Type পরে বসে, Kotlin-এর মতো।

```dart
// Dart
final title = 'আজকের নোট';
var count = 0;
const maxLength = 500;
String? subtitle;
```

```swift
// Swift
let title = "আজকের নোট"        // বদলানো যায় না (Dart-এর final)
var count = 0                  // বদলানো যায়
let maxLength = 500            // Swift-এ আলাদা const নেই — let-ই যথেষ্ট
var subtitle: String?          // optional, শুরুতে nil
```

```kotlin
// Kotlin
val title = "আজকের নোট"
var count = 0
```

| Dart | Swift | Kotlin |
|---|---|---|
| `final` | `let` | `val` |
| `var` | `var` | `var` |
| `const` | `let` (compile-time const আলাদা নেই) | `const val` |
| `'...'` বা `"..."` | শুধু `"..."` | শুধু `"..."` |
| `'$count টা'`, `'${note.title}'` | `"\(count) টা"`, `"\(note.title)"` | `"$count টা"` |
| `int`, `double` | `Int`, `Double` | `Int`, `Double` |
| `null` | `nil` | `null` |
| record `(1, 'a')` | tuple `(1, "a")` | `Pair` |
| `;` লাগে | লাগে না | লাগে না |

**Type বদলায় না নিজে থেকে।** Swift-এ `Int` আর `Double` যোগ করা যায় না। নিজে বদলাতে হয়:

```swift
let words = 120
let minutes = Double(words) / 200.0      // Int → Double, হাতে
```

Dart-এ `int` আর `double` দুটোই `num`, তাই যোগ চলে। Swift-এ compiler থামাবে।

**ফাঁদ — `let` মানে struct-এর জন্য পুরো জিনিস বদলানো যাবে না।** `let note = Note(...)` লিখলে `note.title = "নতুন"` লেখাও যাবে না, যদি `Note` একটা struct হয়। Dart-এ `final note` হলে শুধু variable-টা আটকায়, ভেতরের field বদলানো যায়। কারণটা [iOS ১.৪](#ios1-4)-এ।

[উপরে ফিরুন](#toc)

### <a id="ios1-2"></a>iOS ১.২ Optional

**এক লাইনে:** Dart-এর null safety-র মতোই — `String?`, `!`, `??`, `?.`। শুধু null check করার পথটা আলাদা: `if let` আর `guard let`।

**Flutter-এ আপনি যেভাবে করেন:**

```dart
String? draftTitle;

void save() {
  if (draftTitle != null) {
    repo.save(draftTitle);          // flow analysis: এখানে String হয়ে গেছে
  }
  final title = draftTitle ?? 'শিরোনাম নেই';
  final length = draftTitle?.length;
}
```

**Swift-এ একই কাজ:**

```swift
var draftTitle: String?

func save() {
    if let draftTitle {                         // nil না হলে, ভেতরে String
        repo.save(draftTitle)
    }
    let title = draftTitle ?? "শিরোনাম নেই"
    let length = draftTitle?.count              // Int?
}
```

**`guard let` — আগে বের হয়ে যাও:**

```swift
func open(noteID: UUID?) {
    guard let noteID else {                     // nil হলে এখানেই return
        showError("Note পাওয়া যায়নি")
        return
    }
    // এখান থেকে নিচে noteID একটা সাধারণ UUID
    router.show(noteID)
}
```

`guard`-এর `else`-এ ফিরে যেতেই হবে (`return`, `throw`, `break`)। Compiler নিশ্চিত করে। Dart-এ `if (x == null) return;` লিখে early return করতেন — এটা তার কড়া রূপ।

| Dart | Swift | Kotlin |
|---|---|---|
| `String?` | `String?` | `String?` |
| `x!` | `x!` | `x!!` |
| `x ?? y` | `x ?? y` | `x ?: y` |
| `x?.length` | `x?.count` | `x?.length` |
| `if (x != null) { x... }` | `if let x { x... }` | `if (x != null)` বা `x?.let { }` |
| `if (x == null) return;` | `guard let x else { return }` | `val x = x ?: return` |

**ভেতরে কীভাবে কাজ করে:** Swift-এ optional কোনো জাদু না। এটা একটা সাধারণ enum:

```swift
enum Optional<Wrapped> {
    case none           // nil
    case some(Wrapped)  // ভেতরে value আছে
}
```

`String?` আসলে `Optional<String>`। তাই optional-এর ওপর `switch`-ও করা যায়, আর `map` চলে: `draftTitle.map { $0.uppercased() }`।

**কী আলাদা:** Dart আর Kotlin `!= null` check-এর পরে নিজে type বদলে দেয় (smart cast)। Swift দেয় না। `if draftTitle != nil { draftTitle.count }` — compile হবে না। Unwrap করতে `if let` বা `guard let` লাগবেই।

**Best approach:** `guard let` দিয়ে function-এর শুরুতে সব nil বাদ দিন। বাকি code সোজা থাকে, nesting কমে।

**ফাঁদ:** `!` (force unwrap) nil পেলে app সাথে সাথে crash করে। Dart-এর `!`-এর মতোই। Production code-এ `!` দেখলে review-এ প্রশ্ন আসবে। `IBOutlet`-এর মতো কিছু পুরনো জায়গায় ছাড়া এড়িয়ে চলুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-3"></a>iOS ১.৩ Function আর closure

**এক লাইনে:** Function-এ **argument label** আছে, যেটা call করার সময় লিখতে হয়। Lambda-র নাম closure, আর শেষের closure বন্ধনীর বাইরে বসে।

**Flutter-এ:**

```dart
Note createNote({required String title, String body = ''}) { ... }

final note = createNote(title: 'বাজার', body: 'ডিম, দুধ');
final pinned = notes.where((n) => n.isPinned).toList();
```

**Swift-এ:**

```swift
func createNote(title: String, body: String = "") -> Note { ... }

let note = createNote(title: "বাজার", body: "ডিম, দুধ")
let pinned = notes.filter { $0.isPinned }
```

**Argument label — Swift-এর নিজস্ব জিনিস।** প্রতিটা parameter-এর দুইটা নাম থাকতে পারে: বাইরের label আর ভেতরের নাম।

```swift
func move(_ note: Note, to folder: Folder) { ... }
//        ↑ label নেই   ↑ label "to", ভেতরে নাম "folder"

move(note, to: archive)          // পড়তে ইংরেজি বাক্যের মতো
```

- `_` মানে call-এ label লাগবে না।
- Label না দিলে parameter-এর নামই label। তাই Swift-এ প্রায় সব argument named — Dart-এর `{required ...}`-এর মতো, কিন্তু default হিসেবে।
- Dart-এর `[ ]`-এর মতো আলাদা ঐচ্ছিক positional syntax নেই। Default value দিলেই ঐচ্ছিক — label-ওয়ালা হোক বা `_`-ওয়ালা (`func f(_ x: Int = 0)`)।

**Closure:**

```swift
// পুরো রূপ
let byDate: (Note, Note) -> Bool = { (a: Note, b: Note) -> Bool in
    return a.updatedAt > b.updatedAt
}

// ছোট রূপ: type বোঝা যায়, $0 $1 দিয়ে argument
let sorted = notes.sorted { $0.updatedAt > $1.updatedAt }

// Trailing closure: শেষ argument closure হলে বন্ধনীর বাইরে
Button("সেভ") {
    save()
}
```

| Dart | Swift | Kotlin |
|---|---|---|
| `(n) => n.isPinned` | `{ $0.isPinned }` বা `{ n in n.isPinned }` | `{ it.isPinned }` |
| `void Function(Note)` | `(Note) -> Void` | `(Note) -> Unit` |
| `{required String title}` | `title: String` (label দিয়ে) | `title: String` + named call |
| positional `[int? x]` | নেই — default value দিন | default value |

**`@escaping` — closure পরে চলবে কি না।** কোনো function closure নিয়ে পরে চালালে (রেখে দেয়, অন্য thread-এ পাঠায়), parameter-এ `@escaping` লিখতে হয়:

```swift
func fetchNotes(completion: @escaping ([Note]) -> Void) {
    // network শেষে পরে completion চলবে
}
```

Dart-এ এরকম কিছু নেই। Swift-এ লাগে, কারণ পরে চলা closure যা ধরে রাখে, তা memory-তে বেঁচে থাকে। এখানেই retain cycle-এর শুরু ([iOS ১.৫](#ios1-5))। নতুন code-এ completion handler কম লিখবেন — `async` দিয়ে লিখবেন ([iOS ২](#ios2))। কিন্তু plugin code-এ প্রচুর দেখবেন।

**ফাঁদ:** label ভুলে যাওয়া। `move(note, archive)` compile হবে না — `to:` লাগবে। প্রথম কয়েকদিন Xcode-এর autocomplete-এর ওপর ভরসা করুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-4"></a>iOS ১.৪ `struct` বনাম `class` — value বনাম reference

**এক লাইনে:** `struct` assign করলে **copy** হয়। `class` assign করলে **একই object-এর আরেকটা reference** হয় (Dart-এর সব class-এর মতো)। Swift-এ model-এর জন্য struct-ই default।

**Flutter-এ — সব class reference:**

```dart
class Note {
  Note({required this.title});
  String title;
}

final a = Note(title: 'বাজার');
final b = a;
b.title = 'অফিস';
print(a.title);    // অফিস — a আর b একই object
```

এজন্যই Dart-এ `freezed` আর `copyWith` লাগে — যাতে কেউ ভুল করে ভাগ করা object বদলে না দেয়।

**Swift-এ struct:**

```swift
struct Note: Identifiable, Hashable, Codable, Sendable {
    let id: UUID
    var title: String
    var body: String
    var isPinned = false
    var updatedAt: Date
}

var a = Note(id: UUID(), title: "বাজার", body: "", updatedAt: .now)
var b = a                 // পুরো copy
b.title = "অফিস"
print(a.title)            // বাজার — a বদলায়নি
```

একটা লাইন `struct Note` লিখেই আপনি পেলেন:
- **Memberwise initializer** — `Note(id:title:body:isPinned:updatedAt:)` নিজে থেকে তৈরি।
- **`Equatable` আর `Hashable`** — protocol-এর নাম লিখলেই compiler `==` আর hash বানিয়ে দেয়।
- **`Codable`** — JSON-এ যাওয়া-আসা, code generation ছাড়া।
- **copyWith লাগে না** — `var copy = note; copy.title = "নতুন"`। Copy-টাই নতুন value।

Kotlin-এর `data class`, Dart-এর `freezed` — দুটোর কাজ Swift-এ struct একাই করে।

**Struct-এর method যদি নিজেকে বদলায়, `mutating` লিখতে হয়:**

```swift
extension Note {
    mutating func togglePin() {
        isPinned.toggle()
        updatedAt = .now
    }
}

var note = Note(id: UUID(), title: "বাজার", body: "", updatedAt: .now)
note.togglePin()          // চলবে
let fixed = note
fixed.togglePin()         // compile error — let struct বদলানো যায় না
```

**Class কখন:**

```swift
final class NotesStore {           // final: কেউ subclass করতে পারবে না
    private var cache: [UUID: Note] = [:]
    init() {}                      // class-এ memberwise init নেই — নিজে লিখুন
}
```

| | `struct` | `class` |
|---|---|---|
| Assign করলে | copy | একই object, নতুন reference |
| Inheritance | নেই | আছে |
| Init | নিজে থেকে memberwise | নিজে লিখতে হয় |
| `let` হলে | কিছুই বদলানো যায় না | property বদলানো যায় (শুধু reference আটকে) |
| Memory | সাধারণত সস্তা, ARC-এর ঝামেলা কম | ARC দিয়ে, retain cycle সম্ভব |
| Identity (`===`) | নেই | আছে |
| Dart-এ কাছাকাছি | `freezed` model | সাধারণ class |

**ভেতরে কীভাবে কাজ করে — copy কি দামি না?** না। `Array`, `Dictionary`, `String` struct হলেও ভেতরে **copy-on-write** করে। Assign করলে ভেতরের buffer ভাগ হয়। কেউ বদলাতে গেলে তখনই আসল copy হয়। তাই ১০,০০০ note-এর array পাঠানো সস্তা।

**Best approach:** Data (Note, Folder, API response) — `struct`। যার identity আছে আর যাকে অনেকে ভাগ করে (store, repository, `@Observable` screen model) — `final class`। ভাগ করা mutable state অনেক thread থেকে ছুঁতে হলে `actor` ([iOS ২.৫](#ios2-5))।

**ফাঁদ:** struct-কে ফাংশনে পাঠিয়ে ভেতরে বদলালে বাইরে বদলায় না — copy গেছে। বাইরেরটা বদলাতে চাইলে `inout` দিন আর call-এ `&` লিখুন: `func rename(_ note: inout Note)`, `rename(&note)`। তবে বেশিরভাগ সময় নতুন value ফেরত দেওয়াই পরিষ্কার।

[উপরে ফিরুন](#toc)

### <a id="ios1-5"></a>iOS ১.৫ Memory: ARC, `weak` আর retain cycle

**এক লাইনে:** Dart আর Kotlin-এ garbage collector মাঝে মাঝে এসে অদরকারি object মুছে দেয়। Swift-এ প্রতিটা class object গোনে, কয়জন তাকে ধরে আছে। গোনা শূন্য হলেই সাথে সাথে মুছে যায়। এর নাম **ARC** (Automatic Reference Counting)।

**ভেতরে কীভাবে কাজ করে:**

```
let store = NotesStore()      // count = 1
let another = store           // count = 2
another = nil (ধরুন)          // count = 1
store শেষ হলো                 // count = 0 → deinit চলে, memory ফেরত
```

Compiler নিজেই `retain` আর `release` বসায়। আপনি কিছু লেখেন না। সুবিধা: কখন মুছবে আগে থেকে জানা যায়, GC-র মতো হঠাৎ থামা নেই। অসুবিধা: **cycle** হলে গোনা কখনো শূন্য হয় না।

**Retain cycle — দুইজন একে অপরকে ধরে আছে:**

```swift
final class NoteEditor {
    var onSave: (() -> Void)?
    var text = ""

    func setup() {
        onSave = {
            print(self.text)          // closure self-কে strong-ভাবে ধরল
        }                             // self ধরে আছে closure-কে → cycle, কেউ মরবে না
    }

    deinit { print("editor মুছে গেল") }   // কখনো print হবে না
}
```

**সমাধান — capture list-এ `[weak self]`:**

```swift
onSave = { [weak self] in
    guard let self else { return }    // editor আগেই মুছে গেলে কিছু করো না
    print(self.text)
}
```

| শব্দ | মানে | কখন |
|---|---|---|
| strong (default) | গোনায় যোগ হয় | সাধারণ সব reference |
| `weak` | গোনায় যোগ হয় না, object মুছলে নিজে `nil` হয় (তাই সবসময় optional) | delegate, পরে চলা closure-এ `self` |
| `unowned` | গোনায় যোগ হয় না, কিন্তু nil হয় না — মুছে গেলে ছুঁলে crash | শুধু যখন নিশ্চিত, object আগে মরবে না |

**কোথায় cycle সবচেয়ে বেশি হয়:**
- Class-এর property-তে রাখা closure, যেটা `self` ধরে।
- Delegate pattern — delegate property সবসময় `weak var delegate: NoteEditorDelegate?`।
- Timer, `NotificationCenter`-এর block observer।
- পুরনো Combine-এর `sink { self... }`।

**Dart-এর সাথে পার্থক্য:** Dart-এ GC cycle-ও খুঁজে মুছে দেয়। তাই Flutter-এ আপনি `StreamSubscription` cancel না করলে leak হতো, কিন্তু দুই object-এর cycle নিয়ে কখনো ভাবেননি। Swift-এ ভাবতে হবে।

**ভালো খবর:** struct আর enum ARC-এর cycle-এ পড়ে না। SwiftUI-র View struct, তাই SwiftUI code-এ `[weak self]` প্রায় লাগেই না। আর `Task { }`-এর ভেতরে `self` ধরলে task শেষ হলেই ছেড়ে দেয় — তবে অনেক লম্বা চলা task-এ (যেমন অসীম `for await` loop) এটাও leak হতে পারে।

**ফাঁদ:** `[weak self]` সব জায়গায় অন্ধভাবে বসানো। `notes.map { self.format($0) }`-এর মতো সাথে সাথে চলা (non-escaping) closure-এ cycle হয় না, `weak` লাগে না। শুধু `@escaping` closure, যেটা কোথাও রাখা হয়, সেখানে ভাবুন।

**নিজে দেখুন:** class-এ `deinit { print("...") }` লিখুন। Screen বন্ধ করার পরে print না হলে leak। Xcode-এর **Debug Memory Graph** বোতাম cycle-টা ছবিতে দেখায়।

[উপরে ফিরুন](#toc)

### <a id="ios1-6"></a>iOS ১.৬ `enum` আর `switch`

**এক লাইনে:** Swift-এর `enum` প্রতিটা case-এর সাথে আলাদা data রাখতে পারে (associated value)। Dart-এর `sealed class` বা Kotlin-এর `sealed interface`-এর কাজ এক লাইনে।

**Flutter-এ (Dart 3):**

```dart
sealed class SyncState {}
class Idle extends SyncState {}
class Syncing extends SyncState { Syncing(this.progress); final double progress; }
class Failed extends SyncState { Failed(this.message); final String message; }

String label(SyncState s) => switch (s) {
  Idle() => 'সব ঠিক আছে',
  Syncing(:final progress) => '${(progress * 100).round()}% sync হচ্ছে',
  Failed(:final message) => 'ব্যর্থ: $message',
};
```

**Swift-এ:**

```swift
enum SyncState: Equatable {
    case idle
    case syncing(progress: Double)
    case failed(message: String)
}

func label(for state: SyncState) -> String {
    switch state {
    case .idle:
        "সব ঠিক আছে"
    case .syncing(let progress):
        "\(Int(progress * 100))% sync হচ্ছে"
    case .failed(let message):
        "ব্যর্থ: \(message)"
    }
}
```

- `switch` সব case না ধরলে compile হবে না — Dart-এর exhaustive switch-এর মতো। নতুন case যোগ করলে compiler সব জায়গা দেখিয়ে দেবে।
- `break` লাগে না, এক case থেকে পরেরটায় পড়ে যায় না।
- Swift 5.9 থেকে `if` আর `switch` expression হিসেবে value ফেরত দিতে পারে — ওপরের function-এ `return` লাগেনি।
- Type জানা থাকলে `.idle` লিখলেই হয়, `SyncState.idle` লাগে না।

**Raw value-ওয়ালা সাধারণ enum:**

```swift
enum SortOrder: String, CaseIterable, Codable {
    case newest, oldest, title
}

SortOrder.allCases          // [.newest, .oldest, .title] — menu বানাতে
SortOrder(rawValue: "title") // Optional<SortOrder>
```

**`switch`-এ pattern:**

```swift
let hint = switch state {
case .syncing(let p) where p >= 1.0: "শেষ হচ্ছে"
case .syncing: "চলছে"
case .idle, .failed: ""
}
```

| Dart | Swift | Kotlin |
|---|---|---|
| `enum Sort { newest, oldest }` | `enum SortOrder { case newest, oldest }` | `enum class SortOrder` |
| `sealed class` + subclass | `enum` + associated value | `sealed interface` + `data class` |
| `switch` expression | `switch` (Swift 5.9+ expression-ও) | `when` |
| `Sort.values` | `CaseIterable` → `.allCases` | `entries` |
| `Sort.newest.name` | raw value: `.rawValue` | `.name` |

**Best approach:** Screen-এর অবস্থা (loading / loaded / error), sync-এর অবস্থা, navigation route — সব enum। Bool flag-এর জোড়া (`isLoading`, `hasError`) দিয়ে অসম্ভব অবস্থা তৈরি হয়। Enum দিলে হয় না।

**ফাঁদ:** `default:` দিয়ে সব বাকি case ধরে ফেলা। তাহলে নতুন case যোগ করলে compiler আর সতর্ক করবে না। নিজের enum-এ `default` এড়িয়ে চলুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-7"></a>iOS ১.৭ Protocol আর extension

**এক লাইনে:** `protocol` = Dart-এর `abstract interface class`, Kotlin-এর `interface`। `extension` = Dart-এর `extension`, কিন্তু অনেক বেশি ক্ষমতা — নতুন protocol মানানোও যায়।

**Flutter-এ:**

```dart
abstract interface class NotesRepository {
  Future<List<Note>> allNotes();
  Future<List<Note>> search(String text);
  Future<void> save(Note note);
}

extension NoteX on Note {
  String get preview => body.length > 80 ? '${body.substring(0, 80)}…' : body;
}
```

**Swift-এ:**

```swift
protocol NotesRepository: Sendable {
    func allNotes() async throws -> [Note]
    func search(_ text: String) async throws -> [Note]
    func save(_ note: Note) async throws
}

extension Note {
    var preview: String {
        body.count > 80 ? String(body.prefix(80)) + "…" : body
    }
}
```

**Protocol extension — default implementation:**

```swift
protocol WordCountable {
    var body: String { get }
}

extension WordCountable {
    var wordCount: Int { body.split(separator: " ").count }   // সবাই বিনা খরচে পায়
}

extension Note: WordCountable {}       // পরে, আলাদা জায়গায় protocol মানানো
```

শেষ লাইনটা Dart-এ সম্ভব না। Dart-এ class লেখার সময়েই `implements` লিখতে হয়। Swift-এ যেকোনো type-কে — এমনকি `String` বা Apple-এর type-কেও — পরে নতুন protocol মানানো যায়। একে **retroactive conformance** বলে। (অন্য module-এর type-কে অন্য module-এর protocol মানালে — যেমন Apple-এর type-কে Apple-এর protocol — Swift 6 সতর্ক করে, আর `@retroactive` লিখতে বলে — কারণ Apple পরে নিজে সেটা যোগ করলে দুইটা implementation হবে।)

**`some` আর `any` — দুইটা আলাদা জিনিস:**

```swift
// some: একটা নির্দিষ্ট type, compiler জানে কোনটা। দ্রুত।
var body: some View { Text("Notes") }

// any: যেকোনো type, যে protocol মানে। Runtime-এ বাক্সে ভরা।
let repository: any NotesRepository = RemoteNotesRepository()
```

| | `some Protocol` | `any Protocol` |
|---|---|---|
| মানে | "একটা নির্দিষ্ট type, নাম বলছি না" | "যেকোনো type, এই protocol মানলেই হলো" |
| Type কখন ঠিক হয় | compile-time | runtime |
| খরচ | কম | একটু বেশি (box, dynamic dispatch) |
| কোথায় দেখবেন | SwiftUI-র `some View` | dependency রাখার জায়গা: `let repo: any NotesRepository` |

Dart-এ সব interface type আসলে `any`-এর মতো। Swift আপনাকে বেছে নিতে দেয়।

**Best approach:** Repository, API client-এর মতো যেখানে test-এ fake লাগবে, সেখানে protocol। কিন্তু এক implementation-এর জন্য "শুধু যদি লাগে" protocol বানাবেন না। Helper (`preview`, `wordCount`) — extension-এ।

**ফাঁদ:** একটা protocol-এ `associatedtype` থাকলে (যেমন `Identifiable`-এর `ID`), আগে সেটা সাধারণ variable type হিসেবে ব্যবহার করা যেত না। Swift 5.7 থেকে `any Identifiable` লেখা যায়, কিন্তু ভেতরের associated type ব্যবহার করা ঝামেলার। এ রকম জায়গায় generics নিন।

[উপরে ফিরুন](#toc)

### <a id="ios1-8"></a>iOS ১.৮ Generics

**এক লাইনে:** Dart-এর `<T>` আর `T extends X`-এর মতোই। Constraint লেখা হয় `T: Protocol` দিয়ে, বা `where` দিয়ে।

```dart
T? findById<T extends HasId>(List<T> items, String id) =>
    items.where((e) => e.id == id).firstOrNull;
```

```swift
func find<T: Identifiable>(_ items: [T], id: T.ID) -> T? {
    items.first { $0.id == id }
}

let note = find(notes, id: selectedID)
```

**Generic type:**

```swift
enum LoadState<Value> {
    case loading
    case loaded(Value)
    case failed(String)
}

var notesState: LoadState<[Note]> = .loading
```

**`where` দিয়ে বেশি শর্ত:**

```swift
extension Array where Element == Note {
    var pinned: [Note] { filter(\.isPinned) }       // শুধু [Note]-এ পাওয়া যাবে
}
```

`\.isPinned` হলো **key path** — "Note-এর isPinned property"-র একটা reference। `{ $0.isPinned }`-এর ছোট রূপ।

| Dart | Swift | Kotlin |
|---|---|---|
| `<T extends Comparable>` | `<T: Comparable>` | `<T : Comparable<T>>` |
| একাধিক শর্ত | `<T: A & B>` বা `where T: A, T: B` | `where T : A, T : B` |
| `extension on List<Note>` | `extension Array where Element == Note` | `fun List<Note>.pinned()` |
| (নেই) | `associatedtype` — protocol-এর ভেতরের generic | (নেই, generic interface) |

**ফাঁদ:** একটা জায়গায় এক type-এর জন্য generic বানানো। আগে সাধারণ code লিখুন। দ্বিতীয়-তৃতীয় type এলে তবেই generic।

[উপরে ফিরুন](#toc)

### <a id="ios1-9"></a>iOS ১.৯ Error handling — `throws`, `try`, `Result`

**এক লাইনে:** কোন function error ছুঁড়তে পারে, সেটা Swift-এ signature-এ লেখা থাকে (`throws`)। আর call করার সময় `try` লিখতে হয়। Dart-এ যেকোনো function যেকোনো সময় throw করতে পারে, কেউ বলে দেয় না।

**Flutter-এ:**

```dart
Future<void> save(Note note) async {
  try {
    await api.upload(note);
  } on SocketException {
    queue.add(note);                  // offline — পরে পাঠাব
  } catch (e) {
    showError(e.toString());
  }
}
```

**Swift-এ:**

```swift
enum NoteError: Error {
    case emptyTitle
    case notFound(id: UUID)
    case offline
}

func validate(_ note: Note) throws(NoteError) {     // typed throws, Swift 6.0+
    guard !note.title.isEmpty else { throw .emptyTitle }
}

func save(_ note: Note) async {
    do {
        try validate(note)
        try await api.upload(note)
    } catch NoteError.offline {
        queue.append(note)
    } catch {
        showError(error.localizedDescription)        // error নামটা নিজে থেকে আসে
    }
}
```

**`try`-এর তিন রূপ:**

| লেখা | মানে | কখন |
|---|---|---|
| `try f()` | error হলে ওপরে পাঠাও | `do/catch`-এর ভেতরে, বা নিজের function `throws` হলে |
| `try? f()` | error হলে `nil` দাও | ব্যর্থ হলে কিছু যায় আসে না (cache পড়া) |
| `try! f()` | error হলে crash | প্রায় কখনো না |

**`Result` — error-কে value হিসেবে রাখা:**

```swift
let result: Result<[Note], NoteError> = .success(notes)

switch result {
case .success(let notes): show(notes)
case .failure(let error): showError(error)
}
```

`async`/`await` আসার পরে `Result` কম লাগে। এখন দেখবেন মূলত পুরনো completion handler-এ: `completion: @escaping (Result<[Note], Error>) -> Void` — প্রায় সব পুরনো plugin code-এ।

**Typed throws (Swift 6.0, ২০২৪):** `throws(NoteError)` লিখলে compiler জানে, শুধু `NoteError`-ই আসবে। সাধারণ `throws` মানে যেকোনো `Error`। App code-এ সাধারণ `throws`-ই বেশিরভাগ সময় ঠিক। Typed throws কাজে লাগে ছোট, বন্ধ জায়গায় — যেমন validation।

| Dart | Swift | Kotlin |
|---|---|---|
| যেকোনো function throw করতে পারে | শুধু `throws` লেখা function | যেকোনো function (unchecked) |
| `try { } catch (e) { }` | `do { try ... } catch { }` | `try { } catch (e: Exception) { }` |
| `on SocketException` | `catch NoteError.offline`, `catch let e as URLError` | `catch (e: IOException)` |
| `rethrow` | `catch`-এর ভেতরে `throw error` | `throw e` |
| (নেই) | `try?` → optional | `runCatching { }.getOrNull()` |

**ভেতরে কীভাবে কাজ করে:** Swift-এর error stack unwinding না। `throws` function আসলে একটা লুকানো return path দিয়ে error ফেরত দেয়। তাই throw করা সস্তা, আর `try` ছাড়া call করা compiler আটকায়।

**ফাঁদ:** `try?` দিয়ে সব error চুপ করিয়ে দেওয়া। Save ব্যর্থ হলো, user জানল না, note হারাল। Data বাঁচানোর জায়গায় `do/catch` দিন আর user-কে জানান।

[উপরে ফিরুন](#toc)

### <a id="ios1-10"></a>iOS ১.১০ Collection

**এক লাইনে:** `List` → `Array`, `Map` → `Dictionary`, `Set` → `Set`। তিনটাই struct, তাই value type — assign করলে copy (copy-on-write)।

```dart
final notes = <Note>[];
final byId = <String, Note>{};
final tags = <String>{'কাজ', 'বাজার'};

final titles = notes.where((n) => !n.isPinned).map((n) => n.title).toList();
final first = notes.firstWhereOrNull((n) => n.id == id);   // collection package
```

```swift
var notes: [Note] = []
var byID: [UUID: Note] = [:]
var tags: Set<String> = ["কাজ", "বাজার"]

let titles = notes.filter { !$0.isPinned }.map(\.title)
let first = notes.first { $0.id == id }
```

| Dart | Swift | Kotlin |
|---|---|---|
| `List<Note>` | `[Note]` (`Array<Note>`) | `List<Note>` / `MutableList` |
| `Map<String, Note>` | `[String: Note]` | `Map` / `MutableMap` |
| `.where()` | `.filter {}` | `.filter {}` |
| `.map().toList()` | `.map {}` (সাথে সাথে array দেয়) | `.map {}` |
| `.whereType<T>()` | `.compactMap { $0 as? T }` | `.filterIsInstance<T>()` |
| `.map().whereNotNull()` | `.compactMap {}` | `.mapNotNull {}` |
| `.expand()` | `.flatMap {}` | `.flatMap {}` |
| `.fold()` | `.reduce(_:_:)` | `.fold()` |
| `.firstWhere()` | `.first(where:)` | `.first {}` / `.firstOrNull {}` |
| `.any()` / `.every()` | `.contains(where:)` / `.allSatisfy {}` | `.any {}` / `.all {}` |
| `..sort((a,b) => ...)` | `.sort(by:)` (নিজেকে বদলায়) / `.sorted(by:)` (নতুন দেয়) | `.sortBy` / `.sortedBy` |
| `groupBy` (collection pkg) | `Dictionary(grouping: notes, by: \.isPinned)` | `.groupBy {}` |
| `map[key]` → nullable | `dict[key]` → optional | `map[key]` → nullable |

**Mutable বনাম immutable — কোনো আলাদা type নেই।** Kotlin-এ `List` আর `MutableList` আলাদা। Swift-এ `let notes` হলে বদলানো যায় না, `var notes` হলে যায়। ব্যস।

**ফাঁদ — index দিয়ে ঢুকলে crash:** `notes[5]` — array-এ ৫টার কম থাকলে সাথে সাথে crash, exception না। Dart-এ `RangeError` ধরা যেত। Swift-এ ধরা যায় না। `notes.first`, `notes.last` (optional দেয়) বা `indices.contains(i)` check করুন।

**ফাঁদ — Dictionary-র ক্রম নেই।** `[UUID: Note]`-এর ক্রম আগে থেকে বলা যায় না — insert-এর ক্রম থাকে না, আর বদলানোর (insert/remove) পরে বা app আবার চালালে ক্রম বদলে যেতে পারে। Dart-এর `Map` (LinkedHashMap) insertion order রাখে, Swift-এর রাখে না। ক্রম লাগলে আলাদা array রাখুন, বা sort করুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-11"></a>iOS ১.১১ Access control

**এক লাইনে:** Dart-এ শুধু দুইটা স্তর — public, আর `_` দিয়ে library-private। Swift-এ ছয়টা keyword, আর default হলো `internal` (পুরো module দেখে, বাইরে কেউ না)।

| Swift | কে দেখতে পায় | Dart-এ কাছাকাছি | Kotlin |
|---|---|---|---|
| `private` | শুধু এই `{ }`-এর ভেতর (আর একই file-এ এই type-এর extension) | `_name` | `private` |
| `fileprivate` | এই file | `_name` (Dart-এ file = library) | (নেই) |
| `internal` (default) | এই module (app target বা একটা package) | (নেই — package-এর `src/`) | `internal` |
| `package` (Swift 5.9+) | একই Swift package-এর সব module | (নেই) | (নেই) |
| `public` | সবাই দেখে, কিন্তু module-এর বাইরে subclass বা override করা যায় না | public | `public` (final class) |
| `open` | সবাই দেখে আর subclass/override করতে পারে | public | `open` |

```swift
@Observable
final class NoteEditorModel {
    private(set) var note: Note          // বাইরে পড়া যাবে, বদলানো যাবে শুধু ভেতরে
    private let repository: any NotesRepository

    init(note: Note, repository: any NotesRepository) {
        self.note = note
        self.repository = repository
    }
}
```

`private(set)` খুব কাজের: Cubit-এর `state` বাইরে শুধু পড়া যায়, ভেতরে `emit` — ঠিক সেই নিয়ম এক শব্দে।

**কখন মাথা ঘামাবেন:** App-এর এক target-এ সব কিছু `internal` থাকলেই চলে। Flutter plugin বা Swift package লিখলে বাইরের API-তে `public` লাগবে। না দিলে "cannot find in scope" error আসবে, অথচ code ঠিক আছে।

[উপরে ফিরুন](#toc)

### <a id="ios1-12"></a>iOS ১.১২ Objective-C-র সাথে (চিনে রাখুন)

Swift আসার আগে (২০১৪) iOS-এর ভাষা ছিল Objective-C। UIKit-এর ভেতরটা এখনো অনেকটা Objective-C। আর অনেক পুরনো Flutter plugin এখনো Objective-C-তে লেখা — `.h` আর `.m` file দেখবেন।

```objc
// Objective-C — চেনার জন্য
@interface NotesPlugin : NSObject<FlutterPlugin>
@end

[channel invokeMethod:@"noteSaved" arguments:@{@"id": noteId}];
```

- **Swift থেকে Objective-C ডাকা:** একই target-এ হলে **bridging header**-এ `#import` লিখুন। Flutter-এর `ios/Runner/Runner-Bridging-Header.h` ঠিক এই file। ভেতরে `#import "GeneratedPluginRegistrant.h"` — তাই Swift-এর `AppDelegate` Objective-C-র plugin registrant দেখতে পায়।
- **Objective-C থেকে Swift দেখা:** class-এ `@objc` বা `NSObject` থেকে inherit লাগে। Flutter template-এর `@objc class AppDelegate` এজন্যই।
- **Swift-এ নতুন code লিখুন।** Objective-C পড়তে পারলেই যথেষ্ট।

> **মনে রাখুন**
> - `let`/`var`, optional-এ `if let` আর `guard let`। `!` মানে nil হলে crash।
> - Model হলো `struct` — value type, assign করলে copy। Memberwise init, `Equatable`, `Codable` বিনা খরচে।
> - GC নেই, ARC আছে। Class-এ রাখা closure-এ `self` ধরলে `[weak self]`।
> - Associated value-ওয়ালা `enum` + exhaustive `switch` = Dart-এর sealed class।
> - Error signature-এ লেখা থাকে (`throws`), call-এ `try` লাগে।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Swift-এ model আমি struct দিয়ে লিখি, কারণ value type — copy হয়, ভাগ করা অবস্থা নেই, আর `Codable`, `Hashable` compiler নিজে বানায়। Identity লাগলে, যেমন store বা screen model, তখন final class। Swift-এ GC নেই, ARC আছে, তাই escaping closure-এ `self` ধরলে `[weak self]` দিই। আর state বোঝাতে associated value-ওয়ালা enum নিই, যাতে exhaustive switch অসম্ভব অবস্থা আটকায়।"
> - *English:* "In Swift I write models as structs, because they're value types — they copy, there's no shared mutable state, and the compiler gives me `Codable` and `Hashable` for free. When I need identity, like a store or a screen model, I use a final class. Swift has ARC, not a garbage collector, so I use `[weak self]` when an escaping closure captures self. And I model state with enums with associated values, so exhaustive switches rule out impossible states."

[উপরে ফিরুন](#toc)

---

## <a id="ios2"></a>iOS ২. Async — Future, Stream, Isolate থেকে async/await, actor আর AsyncSequence

সুখবর দিয়ে শুরু করি: Swift-এর `async`/`await` দেখতে প্রায় Dart-এর মতো। `Future<List<Note>>`-এর জায়গায় `async throws -> [Note]`, আর `await` একই জায়গায় বসে।

কিন্তু ভেতরের জগৎ আলাদা। Dart-এ আপনার সব code এক thread-এ চলত। Swift-এ অনেক thread, আর তারা memory ভাগ করে। তাই Swift-এ দুইটা নতুন প্রশ্ন আসে: **কোন code কোন thread-এ চলছে?** আর **একই data দুই thread একসাথে ছুঁচ্ছে কি না?** Swift 6-এর পুরো concurrency system এই দুই প্রশ্নের উত্তর compile-time-এ দেয়।

Android অংশে coroutine পড়ে থাকলে ([অধ্যায় ২](#ch2)) অনেক কিছু চেনা লাগবে। অধ্যায়ের শেষে এক table-এ তুলনা আছে।

### <a id="ios2-1"></a>iOS ২.১ সবচেয়ে বড় পার্থক্য: thread আর data race

**এক লাইনে:** Dart-এ memory ভাগ হয় না, তাই data race অসম্ভব। Swift-এ memory ভাগ হয়, তাই data race সম্ভব — আর Swift 6 compiler সেটা build-এর সময়েই ধরে।

**Flutter-এ আপনি যেভাবে ভাবেন:**
- একটা isolate, একটা thread, একটা event loop।
- `await` মানে "এই কাজ পরে চালাও", কিন্তু একই thread-এ।
- ভারী কাজ অন্য isolate-এ (`Isolate.run`)। Isolate-এর memory আলাদা, শুধু message যায়। তাই দুইজন একই variable একসাথে বদলাতে পারে না।

**iOS-এ:**
- **Main thread** — UI শুধু এখানে। Flutter-এর UI isolate-এর মতো।
- **Cooperative thread pool** — CPU core-এর সমান সংখ্যক thread। `async` কাজ এখানে চলে।
- সব thread একই memory দেখে। দুই thread একসাথে একটা `[Note]` বদলালে data নষ্ট বা crash — এর নাম **data race**।

```
Dart:                               Swift:
┌──────────── isolate ───────────┐  ┌────────────── এক process, ভাগ করা memory ─────────────┐
│ main thread: UI + আপনার code   │  │ main thread (@MainActor) ── UI, screen model          │
│ event loop, await = পরে চালাও   │  │ thread pool ─┬─ async কাজ ১                            │
└────────────────────────────────┘  │              ├─ async কাজ ২   ← একই [Note] ছুঁলে বিপদ  │
┌──── আরেক isolate (আলাদা memory)┐  │              └─ actor NoteCache — এক সময়ে এক জন       │
└────────────────────────────────┘  └───────────────────────────────────────────────────────┘
```

**Swift-এর সমাধান — তিনটা হাতিয়ার:**

| হাতিয়ার | কাজ | পরে বিস্তারিত |
|---|---|---|
| `@MainActor` | "এই code শুধু main thread-এ চলবে" | [iOS ২.৬](#ios2-6) |
| `actor` | "এই data এক সময়ে একজনই ছুঁতে পারবে" | [iOS ২.৫](#ios2-5) |
| `Sendable` | "এই value নিরাপদে অন্য thread-এ পাঠানো যায়" | [iOS ২.৭](#ios2-7) |

Swift 6 language mode-এ compiler এই তিন নিয়ম মিলিয়ে দেখে। নিয়ম ভাঙলে build-ই হবে না। Kotlin-এ coroutine-এ data race-এর দায় আপনার, compiler সাহায্য করে না। Swift-এ compiler পাহারা দেয়।

[উপরে ফিরুন](#toc)

### <a id="ios2-2"></a>iOS ২.২ `Future` → `async`/`await`

**এক লাইনে:** `Future<T>` ফেরত দেওয়া function → `async -> T`। Error ছুঁড়লে `async throws -> T`। Call-এ `try await`।

**Flutter-এ:**

```dart
Future<List<Note>> loadNotes() async {
  final response = await dio.get('/notes');
  return (response.data as List).map((e) => Note.fromJson(e)).toList();
}

// দুইটা একসাথে
final results = await Future.wait([api.notes(), api.folders()]);
```

**Swift-এ:**

```swift
func loadNotes() async throws -> [Note] {
    let (data, response) = try await URLSession.shared.data(from: notesURL)
    guard let http = response as? HTTPURLResponse, http.statusCode == 200 else {
        throw URLError(.badServerResponse)
    }
    return try JSONDecoder().decode([Note].self, from: data)
}

// দুইটা একসাথে — async let
async let notes = api.notes()
async let folders = api.folders()
let (allNotes, allFolders) = try await (notes, folders)   // দুইটাই শেষ হলে
```

| Dart | Swift | Kotlin |
|---|---|---|
| `Future<List<Note>>` | `async -> [Note]` | `suspend fun ...: List<Note>` |
| `async` (body-তে) | `async` (signature-এ) | `suspend` |
| `await f()` | `await f()` / `try await f()` | `f()` (কিছু লাগে না) |
| `Future.wait([a, b])` | `async let a = ...; async let b = ...` | `async { }` + `awaitAll` |
| `Future.value(x)` | সাধারণ return | সাধারণ return |
| `Completer` | `withCheckedContinuation` ([iOS ২.৯](#ios2-9)) | `suspendCancellableCoroutine` |

**ভেতরে কীভাবে কাজ করে:** `await` হলো একটা **suspension point**। এখানে function থেমে যায়, আর thread-টা ছেড়ে দেয় অন্য কাজের জন্য। Thread আটকে থাকে না — ঠিক Dart-এর মতো। Kotlin-এর `suspend`-এর মতোই compiler function-কে টুকরো টুকরো করে।

**কী আলাদা — `await`-এর পরে কোন thread?** Dart-এ `await`-এর পরেও একই isolate। Swift-এ:
- Function `@MainActor`-এর হলে `await`-এর পরে আবার main thread-এ ফেরে।
- Function `actor`-এর ভেতরে হলে আবার সেই actor-এ ফেরে।
- কোনো actor-এর না হলে, যেকোনো thread-এ ফিরতে পারে।

তাই "আমি এখন কোন thread-এ" প্রশ্নের উত্তর দেয় **isolation** — function কোন actor-এর। Thread-এর নাম না।

**ফাঁদ:** `await`-এর আগে আর পরে অবস্থা এক থাকবে, এটা ধরে নেওয়া। মাঝের সময়ে অন্য কাজ চলতে পারে, আর ভাগ করা state বদলে যেতে পারে ([iOS ২.৫](#ios2-5)-এর reentrancy)।

[উপরে ফিরুন](#toc)

### <a id="ios2-3"></a>iOS ২.৩ কাজ চালু করা: `Task` আর task group

**এক লাইনে:** সাধারণ (non-async) জায়গা থেকে async কাজ শুরু করতে `Task { }`। অনেকগুলো কাজ একসাথে চালাতে **task group**।

**Flutter-এ:** Button-এর `onPressed` থেকে সরাসরি async function call করতেন। Future-টা ফেলে দিলেও চলত:

```dart
onPressed: () => cubit.sync(),     // Future ফেরত দেয়, কেউ await করে না
```

**Swift-এ:** non-async জায়গা থেকে `await` লেখা যায় না। `Task` দিয়ে একটা নতুন async জগৎ খুলতে হয়:

```swift
Button("Sync") {
    Task {
        await model.sync()          // Task-এর ভেতরে await চলে
    }
}
```

SwiftUI-তে screen খোলার সময় কাজ শুরু করার আরও ভালো পথ `.task` modifier — screen চলে গেলে নিজেই cancel করে ([iOS ৫.৯](#ios5-9))।

**Task-এর তিন রকম:**

| | কী | Parent-এর cancel পায়? | Actor (thread) পায়? | কখন |
|---|---|---|---|---|
| `async let`, task group-এর child | **structured** — parent-এর ভেতরে বাঁধা | হ্যাঁ | না, আলাদা চলে | একসাথে কয়েকটা কাজ |
| `Task { }` | **unstructured** — নিজে স্বাধীন | না | হ্যাঁ, যেখানে বানানো সেখানকার | sync জায়গা থেকে async শুরু |
| `Task.detached { }` | পুরো স্বাধীন | না | না | প্রায় কখনো না |

**Task group — Notes app-এর সব note একসাথে upload:**

```swift
func uploadAll(_ notes: [Note]) async throws {
    try await withThrowingTaskGroup(of: Void.self) { group in
        for note in notes {
            group.addTask {
                try await api.upload(note)       // প্রতিটা আলাদা child task
            }
        }
        try await group.waitForAll()             // একটা fail করলে error ওপরে আসে
    }
}
```

- Group থেকে error বের হয়ে গেলে বাকি child task-গুলো **নিজে cancel** হয়।
- Group-এর `{ }` শেষ হওয়ার আগে সব child শেষ হবেই। কোনো কাজ "হারিয়ে" যায় না — এটাই **structured concurrency**।
- ফল একটা একটা করে নিতে: `for try await result in group { ... }`।

**Task-এর handle রেখে দেওয়া — search-এর উদাহরণ:**

```swift
@MainActor @Observable
final class SearchModel {
    var results: [Note] = []
    private var searchTask: Task<Void, Never>?
    private let repository: any NotesRepository

    init(repository: any NotesRepository) {
        self.repository = repository
    }

    func queryChanged(_ text: String) {
        searchTask?.cancel()                         // আগের search বাতিল
        searchTask = Task {
            try? await Task.sleep(for: .milliseconds(300))   // debounce
            guard !Task.isCancelled else { return }
            results = (try? await repository.search(text)) ?? []
        }
    }
}
```

Flutter-এ এটা আপনি `Timer` আর `CancelableOperation` দিয়ে, বা RxDart-এর `debounceTime` + `switchMap` দিয়ে করতেন।

**ফাঁদ:** `Task { }` কোনো scope-এ বাঁধা না। Screen বন্ধ হলেও চলতে থাকবে, যতক্ষণ না নিজে শেষ হয়। লম্বা কাজ হলে handle রাখুন আর `cancel()` করুন, অথবা `.task` modifier নিন।

[উপরে ফিরুন](#toc)

### <a id="ios2-4"></a>iOS ২.৪ Cancellation

**এক লাইনে:** Swift-এ cancel মানে task-এর গায়ে একটা flag লাগানো। Task নিজে check করে থামে — জোর করে মারা হয় না। Kotlin coroutine-এর মতোই cooperative।

**Flutter-এ:** Dart-এর `Future` cancel করা যায় না। আপনি `StreamSubscription.cancel()`, `CancelToken` (dio), বা একটা `bool _disposed` দিয়ে কাজ চালাতেন।

**Swift-এ:**

```swift
func importNotes(from files: [URL]) async throws -> [Note] {
    var imported: [Note] = []
    for file in files {
        try Task.checkCancellation()                // cancel হলে CancellationError ছোঁড়ে
        let note = try await parseNote(at: file)
        imported.append(note)
    }
    return imported
}

let task = Task { try await importNotes(from: files) }
task.cancel()                                       // flag লাগল
```

**কে নিজে থেকে থামে:**
- `Task.sleep` cancel হলে সাথে সাথে `CancellationError` ছোঁড়ে।
- `URLSession`-এর async API cancel হলে request বন্ধ করে error ছোঁড়ে।
- Parent cancel হলে সব structured child-ও cancel হয় (`async let`, task group)।
- SwiftUI-র `.task` modifier screen চলে গেলে cancel করে।

**কে থামে না:** আপনার নিজের লম্বা loop বা হিসাব। সেখানে নিজে `Task.isCancelled` বা `try Task.checkCancellation()` দিন।

| Dart | Swift | Kotlin |
|---|---|---|
| (Future cancel হয় না) | `task.cancel()` | `job.cancel()` |
| `_disposed` flag | `Task.isCancelled` | `isActive` |
| (নেই) | `try Task.checkCancellation()` | `ensureActive()` |
| (নেই) | `CancellationError` | `CancellationException` |
| `subscription.cancel()` | `for await` loop-এর task cancel | `collect`-এর job cancel |

**ফাঁদ:** `catch`-এ সব error ধরে "কিছু ভুল হয়েছে" দেখানো। Cancel-ও তখন error হিসেবে ধরা পড়ে, আর user অকারণে error message দেখে। `catch is CancellationError { return }` আগে দিন।

[উপরে ফিরুন](#toc)

### <a id="ios2-5"></a>iOS ২.৫ `actor` — এক সময়ে একজন

**এক লাইনে:** `actor` একটা class-এর মতো, কিন্তু তার ভেতরের data এক সময়ে শুধু একটা কাজ ছুঁতে পারে। বাইরে থেকে ডাকতে `await` লাগে, কারণ লাইনে দাঁড়াতে হতে পারে।

**Flutter-এ:** এরকম কিছু লাগেনি, কারণ এক isolate-এ সব code একে একে চলে। দুই isolate-এর memory আলাদা।

**Swift-এ — Notes app-এর memory cache:**

```swift
actor NoteCache {
    private var notes: [UUID: Note] = [:]

    func note(for id: UUID) -> Note? {
        notes[id]
    }

    func store(_ note: Note) {
        notes[note.id] = note
    }
}

let cache = NoteCache()
await cache.store(note)                    // বাইরে থেকে: await
let cached = await cache.note(for: id)
```

Actor-এর ভেতরে `notes` ছুঁতে `await` লাগে না — ভেতরের code নিজেই লাইনের মাথায়। বাইরে থেকে লাগে।

**ভেতরে কীভাবে কাজ করে:** প্রতিটা actor-এর একটা নিজের লাইন (serial executor)। বাইরের call সেই লাইনে দাঁড়ায়, একে একে চলে। Thread আটকায় না — অপেক্ষা `await`-এ হয়। পুরনো iOS-এ এই কাজ হতো serial `DispatchQueue` দিয়ে, হাতে হাতে।

**Dart-এর isolate-এর সাথে তুলনা:**

| | Dart isolate | Swift actor |
|---|---|---|
| Memory | আলাদা heap | একই heap, কিন্তু data actor-এর ভেতরে বন্ধ |
| কথা বলা | message পাঠিয়ে (copy) | `await` দিয়ে method call |
| খরচ | ভারী — নতুন isolate বানাতে সময় লাগে | হালকা — একটা object |
| কাজ | ভারী হিসাব অন্য core-এ | ভাগ করা mutable state রক্ষা |

**ফাঁদ — reentrancy।** Actor-এর ভেতরে `await` এলে actor অন্য call নিতে পারে। তাই `await`-এর পরে actor-এর state বদলে যেতে পারে:

```swift
actor TokenStore {
    private var token: String?

    func validToken() async throws -> String {
        if let token { return token }
        let fresh = try await api.refreshToken()   // এখানে অন্য call ঢুকতে পারে
        token = fresh                               // দুই call → দুইবার refresh!
        return fresh
    }
}
```

সমাধান: চলমান কাজটাকেই রেখে দিন, যাতে দ্বিতীয় call একই কাজের জন্য অপেক্ষা করে:

```swift
actor TokenStore {
    private var token: String?
    private var refreshTask: Task<String, Error>?

    func validToken() async throws -> String {
        if let token { return token }
        if let refreshTask { return try await refreshTask.value }   // চলমানটার জন্য অপেক্ষা

        let task = Task { try await api.refreshToken() }
        refreshTask = task
        defer { refreshTask = nil }
        let fresh = try await task.value
        token = fresh
        return fresh
    }
}
```

Interview-এ actor নিয়ে প্রশ্ন এলে reentrancy-র কথা বললে senior শোনায়।

**Best approach:** Repository-র cache, token store, download manager — যেখানে অনেক জায়গা থেকে একই mutable data ছোঁয়া হয়, সেখানে actor। UI-র state actor-এ না — সেটা `@MainActor`-এ।

[উপরে ফিরুন](#toc)

### <a id="ios2-6"></a>iOS ২.৬ `@MainActor` — UI-র thread

**এক লাইনে:** `@MainActor` হলো একটা বিশেষ, global actor — যার লাইন হলো main thread। কোনো class বা function-এ লিখলে সেটা শুধু main thread-এ চলবে, আর compiler সেটা নিশ্চিত করবে।

**Flutter-এ:** সব Dart code UI isolate-এ চলে, তাই "UI কোন thread থেকে update হচ্ছে" কখনো ভাবেননি।

**Swift-এ — Notes list-এর screen model:**

```swift
@MainActor
@Observable
final class NotesListModel {
    var notes: [Note] = []
    var isLoading = false
    var errorMessage: String?

    private let repository: any NotesRepository

    init(repository: any NotesRepository) {
        self.repository = repository
    }

    func load() async {
        isLoading = true
        defer { isLoading = false }
        do {
            notes = try await repository.allNotes()   // network অন্য জায়গায় চলে,
        } catch {                                      // ফল নিয়ে আবার main-এ ফেরে
            errorMessage = error.localizedDescription
        }
    }
}
```

- SwiftUI-র `View` protocol নিজেই `@MainActor` (Xcode 16 / iOS 18 SDK থেকে)। তাই view-এর body আর তার ভেতরের `Task { }` main-এ চলে।
- Screen model-কে `@MainActor` দিলে UI-র সব state main thread-এ থাকে। Cubit যেমন UI isolate-এ থাকত।
- `repository.allNotes()` যদি অন্য actor-এর বা `@concurrent` হয়, তাহলে network আর decoding main-এর বাইরে চলে। `await`-এর পরে আবার main-এ ফেরে।

**পুরনো code-এ যা দেখবেন:**

```swift
await MainActor.run { self.notes = notes }        // actor-যুগের শুরুর দিকের ধরন
DispatchQueue.main.async { self.notes = notes }   // GCD যুগ — প্রায় সব পুরনো plugin-এ
```

**ফাঁদ:** main thread-এ ভারী কাজ — বড় JSON decode, ছবি resize, হাজার note sort। UI আটকে যায়, Flutter-এ UI isolate-এ ভারী কাজ করার মতোই। এগুলো `@concurrent` function-এ পাঠান ([iOS ২.৭](#ios2-7))।

[উপরে ফিরুন](#toc)

### <a id="ios2-7"></a>iOS ২.৭ `Sendable` আর Swift 6 strict concurrency

**এক লাইনে:** `Sendable` মানে "এই value এক actor থেকে আরেক actor-এ পাঠালে data race হবে না।" Swift 6 language mode-এ compiler প্রতিটা পাঠানো value check করে।

**কোনটা Sendable:**

| Type | Sendable? |
|---|---|
| `Int`, `String`, `Date`, `UUID` | হ্যাঁ |
| struct/enum, যার সব property Sendable | হ্যাঁ (module-এর ভেতরে নিজে থেকে বোঝে; `public` type-এ লিখে দিতে হয়) |
| `actor` | হ্যাঁ — ভেতরের data নিজেই রক্ষা করে |
| `@MainActor` class | হ্যাঁ — সব কাজ main-এ |
| `final class`, শুধু `let` Sendable property | হ্যাঁ, `: Sendable` লিখলে |
| সাধারণ class, `var` property-সহ | না |

Dart-এর সাথে তুলনা: isolate-এর মধ্যে message পাঠাতে Dart value copy করে, তাই সব নিরাপদ। Swift copy করে না — তাই জানতে চায়, ভাগ করা নিরাপদ কি না।

**Swift 6 language mode — কী বদলায়:**
- Swift 5 mode-এ এই check গুলো warning (বা বন্ধ)।
- Swift 6 mode-এ (Swift 6.0, সেপ্টেম্বর ২০২৪) data race-এর সম্ভাবনা **compile error**।
- একটা project একবারে না, target ধরে ধরে Swift 6-এ নেওয়া যায়। আগে Swift 5 mode-এ "Strict Concurrency Checking = Complete" দিয়ে warning দেখে ঠিক করুন, তারপর mode বদলান।

Flutter-এর `ios/Runner` এখনো Swift 5 language mode-এ (template-এ `SWIFT_VERSION = 5.0`)। তাই Runner-এ আপনি এই error দেখবেন না, কিন্তু native project বা plugin-এ দেখবেন।

**Swift 6.2 — "approachable concurrency" (Xcode 26, সেপ্টেম্বর ২০২৫):** Swift 6 প্রথমে অনেক error দিত, আর মানুষ বিরক্ত হতো। Swift 6.2 তিনটা বদল আনল, যাতে সাধারণ app code সহজ হয়:

1. **Default actor isolation = `MainActor`।** Target-এর build setting-এ এটা দিলে, যেখানে কিছু লেখা নেই, সব code `@MainActor` ধরা হয়। মানে app ডিফল্টে single-threaded, Dart-এর মতো। Xcode 26-এ নতুন app project এভাবেই তৈরি হয়।
2. **`nonisolated async` function caller-এর জায়গায় চলে।** আগে এমন function সবসময় background-এ লাফ দিত। এখন (upcoming feature `NonisolatedNonsendingByDefault` চালু থাকলে) যে ডাকে, তার actor-এই চলে। অকারণে thread বদল আর Sendable error কমে।
3. **`@concurrent`** — "এই কাজ সত্যিই background-এ চালাও", স্পষ্ট করে বলার পথ।

এই setting-গুলো Build Settings → **Swift Compiler – Concurrency**-তে থাকে (Default Actor Isolation, Approachable Concurrency)। পুরনো project-এ নিজে থেকে বদলায় না। নতুন project খুললে একবার দেখে নিন কী চালু আছে।

**`Isolate.run` → `@concurrent`:**

```dart
// Dart
final notes = await Isolate.run(() => parseNotes(bytes));
```

```swift
// Swift 6.2+
@concurrent
func parseNotes(_ data: Data) async throws -> [Note] {
    try JSONDecoder().decode([Note].self, from: data)       // main-এর বাইরে চলে
}

let notes = try await parseNotes(data)      // MainActor model থেকে ডাকলে, ফল নিয়ে main-এ ফেরে
```

`@concurrent` শুধু `async` function-এ বসে, আর function-কে `nonisolated` করে দেয়। `Data` আর `[Note]` Sendable, তাই compiler খুশি। Dart-এর `Isolate.run`-এর চেয়ে অনেক সস্তা — নতুন isolate বা copy নেই।

**ফাঁদ — default `MainActor` হলে model-ও main-এর হয়ে যায়।** Default isolation `MainActor` দিলে `struct Note`-ও `@MainActor` ধরা হয়, আর তার `Codable` conformance-ও main-এর হয়ে যেতে পারে। তখন `@concurrent` function-এ `Note` decode করতে গেলে compiler আপত্তি করে। সমাধান: শুধু data রাখা type-কে `nonisolated struct Note: Codable, Sendable { ... }` লিখুন। Model-এর কোনো thread নেই — সে শুধু data।

**ফাঁদ — error চুপ করাতে `@unchecked Sendable` বা `nonisolated(unsafe)`।** এরা compiler-কে বলে "আমি দায় নিচ্ছি"। কিন্তু ভেতরে lock না থাকলে data race থেকেই যায়। Error এলে আগে ভাবুন: এই data কার? Main-এর হলে `@MainActor`, ভাগ করা হলে `actor`, শুধু পড়ার হলে `struct`।

[উপরে ফিরুন](#toc)

### <a id="ios2-8"></a>iOS ২.৮ `Stream` → `AsyncSequence` আর `AsyncStream`

**এক লাইনে:** Dart-এর `Stream` → Swift-এর `AsyncSequence`। `await for` → `for await`। নিজে value পাঠানোর `StreamController` → `AsyncStream`।

**Flutter-এ:**

```dart
Stream<double> syncProgress() {
  final controller = StreamController<double>();
  final token = syncClient.observeProgress((value) {
    controller.add(value);
    if (value >= 1.0) controller.close();
  });
  controller.onCancel = () => token.cancel();
  return controller.stream;
}

await for (final p in syncProgress()) {
  progress = p;
}
```

**Swift-এ:**

```swift
func syncProgress() -> AsyncStream<Double> {
    let (stream, continuation) = AsyncStream.makeStream(of: Double.self)
    let token = syncClient.observeProgress { value in      // পুরনো callback API
        continuation.yield(value)                           // controller.add
        if value >= 1.0 { continuation.finish() }           // controller.close
    }
    continuation.onTermination = { _ in token.cancel() }    // onCancel
    return stream
}

for await progress in syncProgress() {
    self.progress = progress
}
```

Error ছুঁড়তে পারে এমন stream লাগলে `AsyncThrowingStream`, আর loop হবে `for try await`।

**Apple-এর API-তে আগে থেকেই AsyncSequence:**

```swift
// file-এর লাইন একটা একটা করে
for try await line in fileURL.lines { ... }

// system notification
for await _ in NotificationCenter.default.notifications(named: UIApplication.didReceiveMemoryWarningNotification) {
    cache.removeAll()
}
```

**Operator:** `map`, `filter`, `compactMap`, `prefix` standard library-তেই আছে। `debounce`, `throttle`, `merge`, `combineLatest` আছে Apple-এর open-source package **swift-async-algorithms**-এ — RxDart-এর মতো, আলাদা dependency।

| Dart | Swift | Kotlin |
|---|---|---|
| `Stream<T>` | `AsyncSequence` (যেমন `AsyncStream<T>`) | `Flow<T>` |
| `await for` | `for await` | `collect { }` |
| `StreamController` | `AsyncStream.makeStream` | `callbackFlow` / `Channel` |
| `controller.add(x)` | `continuation.yield(x)` | `trySend(x)` |
| `controller.close()` | `continuation.finish()` | `close()` |
| `onCancel` | `continuation.onTermination` | `awaitClose { }` |
| `.map`, `.where` | `.map`, `.filter` | `.map`, `.filter` |
| RxDart `debounceTime` | swift-async-algorithms `.debounce(for:)` | `.debounce()` |
| `StreamSubscription.cancel()` | loop চালানো task cancel | collect-এর job cancel |
| broadcast stream | (built-in নেই — নিজে বানাতে হয়) | `SharedFlow` |

**কী আলাদা:**
- **Cancel করার পথ।** Dart-এ subscription cancel করেন। Swift-এ `for await` loop যে task-এ চলছে, সেই task cancel করেন। SwiftUI-র `.task`-এ loop চালালে screen চলে গেলে নিজেই থামে।
- **`AsyncStream` একজনের জন্য।** একই stream দুই জায়গা থেকে পড়বেন না — সব value দুইজনই পায় না (broadcast না) — Dart-এর single-subscription stream-এর কাছাকাছি, broadcast না।

**UI state-এর জন্য stream না।** Flutter-এ `StreamBuilder` দিয়ে UI বানাতেন। SwiftUI-তে screen-এর state রাখার পথ `@Observable` ([iOS ৫.৭](#ios5-7))। Stream কাজে লাগে ঘটনার ধারার জন্য: sync progress, database-এর বদল, socket-এর message।

**ফাঁদ:** `onTermination` না দেওয়া। Consumer চলে গেলেও পুরনো callback-এর observer চলতে থাকে — Flutter-এ `StreamController`-এর `onCancel`-এ cleanup না করার মতো leak।

[উপরে ফিরুন](#toc)

### <a id="ios2-9"></a>iOS ২.৯ চিনে রাখুন: GCD, completion handler আর Combine

নতুন code-এ এগুলো লিখবেন না। কিন্তু প্রায় প্রতিটা Flutter plugin-এর iOS অংশে, আর পুরনো project-এ, এগুলোই পাবেন।

**GCD (Grand Central Dispatch) — `DispatchQueue`:**

```swift
DispatchQueue.global(qos: .userInitiated).async {
    let notes = parse(data)                       // background thread
    DispatchQueue.main.async {
        self.notes = notes                        // UI-র কাজ main-এ
    }
}
```

`async`/`await`-এর আগে iOS-এ thread বদলানোর একমাত্র সহজ পথ ছিল এটা। Compiler কিছুই check করত না — ভুল thread থেকে UI ছুঁলে কখনো crash, কখনো অদ্ভুত bug।

**Completion handler → async — নিজের wrapper:**

Plugin লেখার সময় প্রায়ই পুরনো callback API-কে async বানাতে হবে। Dart-এর `Completer`-এর কাজ:

```swift
func fetchNotes() async throws -> [Note] {
    try await withCheckedThrowingContinuation { continuation in
        legacyClient.fetchNotes { result in        // পুরনো API: (Result<[Note], Error>) -> Void
            continuation.resume(with: result)       // ঠিক একবার resume করতে হবে
        }
    }
}
```

**ফাঁদ:** continuation **ঠিক একবার** resume করতে হবে। দুইবার করলে crash। একবারও না করলে task চিরকাল ঝুলে থাকে (Checked continuation তখন console-এ সতর্ক করে)। Dart-এ `Completer` দুইবার complete করলে error-এর মতো।

**Combine (২০১৯) — Apple-এর RxDart:**

```swift
import Combine

final class LegacySearchViewModel: ObservableObject {
    @Published var query = ""
    @Published private(set) var results: [Note] = []
    private var cancellables = Set<AnyCancellable>()

    init() {
        $query
            .debounce(for: .milliseconds(300), scheduler: RunLoop.main)
            .removeDuplicates()
            .sink { [weak self] text in self?.search(text) }
            .store(in: &cancellables)
    }

    private func search(_ text: String) { /* ... */ }
}
```

`@Published` + `ObservableObject` ছিল iOS 13–16-এর SwiftUI state। আজ তার জায়গায় `@Observable` আর async/await। Combine বাদ হয়নি, কিন্তু নতুন code-এ কম লাগে।

| পুরনো | আজ |
|---|---|
| `DispatchQueue.main.async` | `@MainActor` |
| `DispatchQueue.global().async` | `@concurrent` function, `Task` |
| serial `DispatchQueue` + lock | `actor` |
| completion handler | `async throws` |
| `DispatchGroup` | task group |
| Combine `Publisher` | `AsyncSequence` |
| `ObservableObject` + `@Published` | `@Observable` |

[উপরে ফিরুন](#toc)

### <a id="ios2-10"></a>iOS ২.১০ Kotlin coroutine-এর সাথে এক table, আর best approach

Android অংশ পড়ে থাকলে এই table একবারে সব মিলিয়ে দেবে:

| কাজ | Dart | Swift | Kotlin |
|---|---|---|---|
| Async function | `Future<T> f() async` | `func f() async -> T` | `suspend fun f(): T` |
| Sync জায়গা থেকে শুরু | সরাসরি call | `Task { }` | `scope.launch { }` |
| Screen-এর আয়ুতে বাঁধা কাজ | `dispose`-এ cancel | `.task { }` modifier | `viewModelScope`, `LaunchedEffect` |
| কয়েকটা একসাথে | `Future.wait` | `async let`, task group | `async { }` + `awaitAll`, `coroutineScope` |
| UI thread | UI isolate | `@MainActor` | `Dispatchers.Main` |
| Background-এ ভারী কাজ | `Isolate.run` | `@concurrent` function | `withContext(Dispatchers.Default)` |
| Mutable state রক্ষা | (দরকার নেই) | `actor` | `Mutex`, single-thread confinement |
| Thread-এ পাঠানো নিরাপদ? | সব copy হয় | `Sendable`, compile-time check | compiler check নেই |
| Cancel | (Future-এ নেই) | `task.cancel()`, `Task.isCancelled` | `job.cancel()`, `isActive` |
| Stream | `Stream` | `AsyncSequence` | `Flow` |
| Callback → stream | `StreamController` | `AsyncStream` | `callbackFlow` |
| Callback → একটা value | `Completer` | `withCheckedThrowingContinuation` | `suspendCancellableCoroutine` |
| UI-র observable state | `ValueNotifier`, Cubit | `@Observable` | `StateFlow` |

**সবচেয়ে বড় দুই পার্থক্য Kotlin-এর সাথে:**
- **Scope object নেই।** Kotlin-এ প্রতিটা `launch` একটা `CoroutineScope`-এ বাঁধা। Swift-এ structured কাজ (`async let`, group) function-এর ভেতরে বাঁধা, আর screen-এর আয়ু SwiftUI-র `.task` দেয়। `Task { }` কোনো scope-এ বাঁধা না।
- **Data race compiler ধরে।** Kotlin-এ ভুল dispatcher বা ভাগ করা `MutableList` নিয়ে compiler চুপ থাকে। Swift 6-এ build হবে না।

**Best approach (নভেম্বর ২০২৬):**
- নতুন app-এ default actor isolation `MainActor`, Swift 6 language mode। App ডিফল্টে single-threaded, Dart-এর মতো সরল।
- Screen model: `@MainActor @Observable final class`।
- ভারী কাজ (decode, ছবি, বড় sort): `@concurrent` function।
- অনেক জায়গা থেকে ছোঁয়া mutable data: `actor`।
- Screen খোলার কাজ: `.task { }` modifier, `Task { }` না।
- পুরনো callback API: একবার `withCheckedThrowingContinuation` বা `AsyncStream`-এ মুড়িয়ে নিন, তারপর সব জায়গায় async।

> **মনে রাখুন**
> - `Future` → `async`, `Future.wait` → `async let` বা task group, `Stream` → `AsyncSequence`।
> - Swift-এ thread আসল আর memory ভাগ হয়। `@MainActor`, `actor`, `Sendable` দিয়ে compiler data race আটকায়।
> - Cancel cooperative: `Task.isCancelled` / `checkCancellation()`। `Task { }` নিজে cancel হয় না।
> - Actor-এ `await`-এর পরে state বদলে যেতে পারে (reentrancy)।
> - Swift 6.2: default `MainActor` isolation, আর background-এর জন্য স্পষ্ট `@concurrent`।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Swift-এ async/await দেখতে Dart-এর মতো, কিন্তু Dart-এ isolate-এর memory আলাদা, আর Swift-এ thread memory ভাগ করে। তাই Swift 6 compiler `Sendable` আর actor isolation দিয়ে data race build-এর সময়েই ধরে। আমি screen model `@MainActor`-এ রাখি, ভাগ করা cache actor-এ, আর ভারী কাজ `@concurrent` function-এ। Screen-এর কাজ `.task` modifier-এ চালাই, যাতে screen চলে গেলে নিজেই cancel হয়।"
> - *English:* "Swift's async/await looks like Dart's, but Dart isolates don't share memory while Swift threads do. So the Swift 6 compiler uses `Sendable` and actor isolation to catch data races at build time. I keep screen models on the `@MainActor`, shared caches in actors, and heavy work in `@concurrent` functions. I start screen work with the `.task` modifier so it cancels itself when the screen goes away."

[উপরে ফিরুন](#toc)

---

## <a id="ios3"></a>iOS ৩. Xcode project — `pubspec.yaml`-এর জায়গায়

Flutter-এ `ios/` folder-এ ঢুকতেন শুধু ভয়ে ভয়ে — signing ঠিক করতে, Info.plist-এ একটা লাইন যোগ করতে, বা `pod install` ব্যর্থ হলে। এবার সেই folder-টাই আপনার বাড়ি। Android-এ এই ভূমিকা ছিল Gradle-এর ([অধ্যায় ৩](#ch3))। iOS-এ পুরোটা চলে Xcode project দিয়ে।

একটা জিনিস প্রথমেই জেনে রাখুন: Xcode project-এর মূল file `project.pbxproj` হাতে পড়ার মতো না। Gradle file আপনি হাতে লেখেন। Xcode project আপনি Xcode-এর UI দিয়ে বদলান, আর file-টা Xcode লেখে। তাই এই অধ্যায়ের বেশিরভাগ জিনিস "Xcode-এর কোন জায়গায় কী" — code কম।

### <a id="ios3-1"></a>iOS ৩.১ Folder-এর চেহারা — Flutter-এর `ios/` বনাম native project

**Flutter-এর `ios/`:**

```
ios/
├── Runner.xcworkspace          ← এটাই খুলবেন (CocoaPods থাকলে বাধ্যতামূলক)
├── Runner.xcodeproj            ← project: target, build setting, scheme
│   └── project.pbxproj
├── Runner/
│   ├── AppDelegate.swift
│   ├── SceneDelegate.swift
│   ├── Info.plist
│   ├── Assets.xcassets         ← app icon, ছবি
│   ├── Base.lproj/
│   │   ├── Main.storyboard     ← প্রথম screen = FlutterViewController
│   │   └── LaunchScreen.storyboard
│   ├── GeneratedPluginRegistrant.h/.m   ← flutter tool বানায়, হাত দেবেন না
│   └── Runner-Bridging-Header.h
├── Flutter/
│   ├── Debug.xcconfig          ← #include "Generated.xcconfig"
│   ├── Release.xcconfig
│   └── Generated.xcconfig      ← flutter tool লেখে: FLUTTER_ROOT, build name/number
├── RunnerTests/
└── Podfile, Podfile.lock       ← শুধু CocoaPods ব্যবহার হলে
```

**একটা নতুন native SwiftUI project (Xcode 26/27):**

```
NotesApp/
├── NotesApp.xcodeproj
└── NotesApp/
    ├── NotesApp.swift          ← @main struct NotesApp: App
    ├── ContentView.swift
    └── Assets.xcassets
```

এত ছোট কেন? দুইটা কারণ:
- **Info.plist file নেই।** Xcode 13 থেকে নতুন project-এ Info.plist-এর বেশিরভাগ key build setting-এ থাকে (`INFOPLIST_KEY_...`)। Xcode build-এর সময় file বানায়। Target → Info tab-এ দেখা আর বদলানো যায়। নিজের key (যেমন API URL) যোগ করলে Xcode তখন একটা file বানিয়ে দেয়।
- **Storyboard নেই।** SwiftUI-র `App` নিজেই window বানায়।

**Xcode 16 থেকে "folder" বনাম "group":** নতুন project-এ folder disk-এর সাথে নিজে মেলে (synchronized folder)। Finder-এ file রাখলেই project-এ চলে আসে, `project.pbxproj`-এ লাইন যোগ হয় না। ফলে git merge conflict অনেক কমে। পুরনো project-এ (Flutter-এর Runner-সহ) "group" থাকে — file যোগ করতে Xcode-এ টেনে আনতে হয়।

| Flutter / Android | iOS |
|---|---|
| `pubspec.yaml` + `android/app/build.gradle` | `project.pbxproj` (Xcode UI দিয়ে বদলান) |
| `AndroidManifest.xml` | `Info.plist` + `.entitlements` |
| `res/`, `assets/` | `Assets.xcassets` |
| `MainActivity.kt` | `AppDelegate.swift` / `@main App` |
| `pubspec.lock` | `Package.resolved` (SPM) / `Podfile.lock` |

**ফাঁদ:** CocoaPods ব্যবহার হলে `.xcodeproj` খুলে build করলে "module not found"। সবসময় `.xcworkspace` খুলুন — ওটায় আপনার project আর Pods project একসাথে থাকে।

[উপরে ফিরুন](#toc)

### <a id="ios3-2"></a>iOS ৩.২ Project, target, scheme, build configuration

**এক লাইনে:** **Target** = কী বানাবেন। **Build configuration** = কোন setting দিয়ে বানাবেন। **Scheme** = কোন বোতাম চাপলে কোন target কোন configuration-এ বানাবেন।

চারটা শব্দ, Android-এর পাশে:

| Xcode | মানে | Android-এ কাছাকাছি |
|---|---|---|
| **Project** | পুরো জিনিস: সব target, সব setting | পুরো Gradle project |
| **Target** | একটা product: app, widget extension, share extension, test bundle | একটা module (`:app`, `:feature`) |
| **Build configuration** | build setting-এর একটা সেট: Debug, Release (Flutter যোগ করে Profile) | build type: `debug`, `release` |
| **Scheme** | Run / Test / Profile / Archive — প্রতিটায় কোন target আর কোন configuration | Run configuration + build variant বেছে নেওয়া |

**Flutter-এর Runner scheme ভেতরে এরকম:**

| Action | Configuration | কখন |
|---|---|---|
| Run | Debug | Xcode-এ ▶ চাপলে |
| Test | Debug | ⌘U |
| Profile | Profile | Instruments চালালে |
| Archive | Release | App Store-এর জন্য build |

**Build setting কোথা থেকে আসে — স্তর:**

```
iOS-এর default  →  project-level setting  →  target-এর .xcconfig file  →  target-level setting
(সবচেয়ে দুর্বল)                                                  (সবচেয়ে জোরালো)
```

Xcode-এ target → Build Settings → "Levels" দেখলে প্রতিটা setting কোন স্তর থেকে এল, পাশাপাশি দেখায়। Setting ঠিক জায়গা থেকে আসছে না মনে হলে এটাই প্রথম জায়গা।

**জরুরি কয়েকটা build setting:**

| Setting | মানে | Android-এ |
|---|---|---|
| `PRODUCT_BUNDLE_IDENTIFIER` | App-এর পরিচয়, যেমন `com.byteonyx.notes` | `applicationId` |
| `MARKETING_VERSION` | User দেখে: `1.4.0` | `versionName` |
| `CURRENT_PROJECT_VERSION` | Build number: `42` | `versionCode` |
| `IPHONEOS_DEPLOYMENT_TARGET` | সবচেয়ে পুরনো যে iOS-এ চলবে | `minSdk` |
| `SWIFT_VERSION` | Swift language mode (5 বা 6) | Kotlin `languageVersion` |
| `CODE_SIGN_STYLE`, `DEVELOPMENT_TEAM` | Signing | `signingConfigs` |

Flutter-এ `pubspec.yaml`-এর `version: 1.4.0+42` লিখলে flutter tool `Generated.xcconfig`-এ `FLUTTER_BUILD_NAME=1.4.0` আর `FLUTTER_BUILD_NUMBER=42` লেখে। আর Runner-এর Info.plist সেগুলো পড়ে: `CFBundleShortVersionString = $(FLUTTER_BUILD_NAME)`। তাই Flutter app-এ version Xcode-এ না, pubspec-এ বদলান।

[উপরে ফিরুন](#toc)

### <a id="ios3-3"></a>iOS ৩.৩ `.xcconfig` — build setting একটা text file-এ

**এক লাইনে:** Build setting Xcode-এর UI-তে না রেখে একটা সাধারণ `key = value` text file-এ রাখা। Git-এ পড়া যায়, review করা যায়, merge conflict কম।

**Flutter-এ আপনি আগেই দেখেছেন:**

```
// ios/Flutter/Debug.xcconfig
#include "Generated.xcconfig"
```

CocoaPods থাকলে flutter tool এখানে আরেকটা লাইন যোগ করে: `#include? "Pods/Target Support Files/Pods-Runner/Pods-Runner.debug.xcconfig"`।

**Notes app-এর নিজের xcconfig:**

```
// Config/Shared.xcconfig
MARKETING_VERSION = 1.4.0
IPHONEOS_DEPLOYMENT_TARGET = 17.0
SWIFT_VERSION = 6.0

// Config/Dev.xcconfig
#include "Shared.xcconfig"
PRODUCT_BUNDLE_IDENTIFIER = com.byteonyx.notes.dev
APP_DISPLAY_NAME = Notes Dev
API_HOST = dev-api.byteonyx.com

// Config/Prod.xcconfig
#include "Shared.xcconfig"
PRODUCT_BUNDLE_IDENTIFIER = com.byteonyx.notes
APP_DISPLAY_NAME = Notes
API_HOST = api.byteonyx.com
```

Project → Info → Configurations-এ প্রতিটা configuration-এর পাশে কোন xcconfig, সেটা বেছে দিন।

**Code থেকে value পড়া — Info.plist হয়ে:**

```xml
<!-- Info.plist -->
<key>APIHost</key>
<string>$(API_HOST)</string>
```

```swift
let host = Bundle.main.object(forInfoDictionaryKey: "APIHost") as? String ?? ""
let baseURL = URL(string: "https://\(host)")!
```

Flutter-এর `--dart-define`-এর কাজ, কিন্তু native দিকে।

**ফাঁদ — `//` মানে comment।** xcconfig-এ `API_URL = https://api.byteonyx.com` লিখলে `//`-এর পরে সব comment হয়ে যায়, value হয় শুধু `https:`। তাই ওপরে শুধু host রেখেছি, `https://` code-এ। পুরো URL রাখতেই হলে মাঝে একটা খালি variable বসানোর পুরনো কৌশল আছে: `https:/$()/api.byteonyx.com`।

**ফাঁদ — secret xcconfig-এ না।** xcconfig-এর value Info.plist হয়ে app-এর ভেতরে খোলা text হিসেবে যায়। যে কেউ `.ipa` খুলে পড়তে পারে। API key-এর মতো secret app-এ রাখলে লুকানো যায় না — server-এ রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ios3-4"></a>iOS ৩.৪ Flavor = scheme + configuration

**এক লাইনে:** Android-এ flavor একটা শব্দ (`productFlavors`)। iOS-এ "flavor" বলে কিছু নেই। একই কাজ হয় দুইটা জিনিস মিলিয়ে: প্রতিটা flavor-এর জন্য **একটা scheme**, আর **কয়েকটা build configuration**।

**Flutter-এ আপনি যেভাবে চালান:**

```bash
flutter run --flavor dev
flutter build ipa --flavor prod
```

`--flavor dev` দিলে flutter tool Xcode-এ **`dev` নামের scheme** খোঁজে। আর সেই scheme-এর configuration-এর নাম হতে হয় `Debug-dev`, `Release-dev`, `Profile-dev`। নাম না মিললে build ব্যর্থ হয়।

**Xcode-এ ধাপগুলো (একবার করতে হয়):**

1. Project → Info → Configurations-এ Debug, Release, Profile duplicate করে নাম দিন: `Debug-dev`, `Release-dev`, `Profile-dev`, `Debug-prod`, `Release-prod`, `Profile-prod`।
2. প্রতিটা configuration-এ ঠিক xcconfig বসান (Dev বা Prod)।
3. Product → Scheme → New Scheme: `dev` আর `prod`। প্রতিটা scheme-এর Run, Test, Profile, Archive-এ নিজের configuration বেছে দিন।
4. Scheme-গুলো **Shared** করুন (Manage Schemes → Shared)। Flutter docs বলে, shared না হলে flavor ঠিকমতো কাজ করে না। আর git-এ না গেলে CI বা সহকর্মী scheme পাবে না।
5. Flavor-এর নাম ছোট হাতের অক্ষরে রাখুন (`dev`, `prod`), নইলে Flutter CLI চিনতে পারে না।

Dart-এর দিক থেকে কোন flavor চলছে জানতে `appFlavor` (`package:flutter/services.dart`) — scheme-এর নামটা দেয়।

```
                 ┌──────── scheme "dev" ─────────┐      ┌──────── scheme "prod" ────────┐
Run      ───────►  Debug-dev    (Dev.xcconfig)        │  Debug-prod    (Prod.xcconfig)
Archive  ───────►  Release-dev  (Dev.xcconfig)        │  Release-prod  (Prod.xcconfig)
Profile  ───────►  Profile-dev  (Dev.xcconfig)        │  Profile-prod  (Prod.xcconfig)
```

| Android | iOS |
|---|---|
| `productFlavors { dev { } prod { } }` | scheme `dev`, `prod` |
| `buildTypes { debug release }` | configuration Debug, Release (Flutter: + Profile) |
| build variant `devDebug` | configuration `Debug-dev` |
| `applicationIdSuffix ".dev"` | `PRODUCT_BUNDLE_IDENTIFIER` xcconfig-এ |
| `buildConfigField` | xcconfig → Info.plist → `Bundle.main` |
| flavor-এর আলাদা `google-services.json` | configuration ধরে আলাদা `GoogleService-Info.plist` (build phase script দিয়ে কপি) |

**ফাঁদ:** নতুন configuration যোগ করলে CocoaPods-এর জন্য `ios/Podfile`-এর `project 'Runner', { ... }` block-এ সেই নাম জানাতে হয় (`'Debug-dev' => :debug`, `'Profile-dev' => :release`, `'Release-dev' => :release`), আর `pod install` আবার চালাতে হয়। নইলে "xcconfig not found" warning আর অদ্ভুত build error। Swift Package Manager-এ এই ঝামেলা নেই।

[উপরে ফিরুন](#toc)

### <a id="ios3-5"></a>iOS ৩.৫ Swift Package Manager বনাম CocoaPods

**এক লাইনে:** iOS-এর `pub` হলো **Swift Package Manager (SPM)** — Apple-এর নিজের, Xcode-এর ভেতরে। CocoaPods ছিল পুরনো, community-র tool। আজ SPM-ই পথ।

**Flutter-এ:**

```yaml
# pubspec.yaml
dependencies:
  dio: ^5.0.0
```

**Native app-এ SPM — Xcode দিয়ে:** File → Add Package Dependencies → GitHub URL দিন → version rule বেছে নিন → কোন target-এ যোগ হবে বেছে নিন। Xcode এটা `project.pbxproj`-এ লেখে, আর ঠিক কোন version এল, সেটা `Package.resolved`-এ (Flutter-এর `pubspec.lock`)।

**নিজের package — `Package.swift`:**

Swift package হলো code ভাগ করার একক। Package-এর manifest Swift-এ লেখা:

```swift
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "NotesKit",
    platforms: [.iOS(.v17)],
    products: [
        .library(name: "NotesKit", targets: ["NotesKit"]),
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-async-algorithms", from: "1.0.0"),
    ],
    targets: [
        .target(
            name: "NotesKit",
            dependencies: [.product(name: "AsyncAlgorithms", package: "swift-async-algorithms")]
        ),
        .testTarget(name: "NotesKitTests", dependencies: ["NotesKit"]),
    ]
)
```

`from: "1.0.0"` মানে `1.0.0` থেকে `2.0.0`-এর আগ পর্যন্ত — Dart-এর `^1.0.0`-এর মতো।

| | `pub` | SPM | CocoaPods |
|---|---|---|---|
| Manifest | `pubspec.yaml` | `Package.swift` (package) / Xcode project (app) | `Podfile` (app), `.podspec` (library) |
| Lock | `pubspec.lock` | `Package.resolved` | `Podfile.lock` |
| কে বানায় | Dart team | Apple, Xcode-এর ভেতরে | Community, Ruby tool |
| Registry | pub.dev | সরাসরি git repo | CocoaPods trunk |
| `^1.0.0` | `^1.0.0` | `from: "1.0.0"` / `.upToNextMajor(from:)` | `'~> 1.0'` |

**Flutter-এ এখন কী হচ্ছে (নভেম্বর ২০২৬):**
- **Flutter 3.44 থেকে SPM ডিফল্টে চালু।** Flutter upgrade করে app চালালে flutter tool নিজে SPM integration যোগ করে।
- যে plugin এখনো SPM সমর্থন করে না, তার জন্য Flutter CocoaPods-এ ফিরে যায়। একটাও এমন plugin থাকলে Podfile থেকে যায়।
- **CocoaPods-এর registry (trunk) ২ ডিসেম্বর ২০২৬ থেকে read-only** — নতুন pod বা নতুন version আর publish হবে না। Flutter docs সতর্ক করছে, ভবিষ্যতে SPM বন্ধ করার option-ও থাকবে না।
- বন্ধ করার পথ (দরকার না হলে করবেন না): `pubspec.yaml`-এ `flutter: config: enable-swift-package-manager: false`।

**Best approach:** নতুন native code আর নতুন plugin — শুধু SPM। Flutter project-এ যে plugin এখনো CocoaPods-only, সেটার SPM-ওয়ালা version বা বিকল্প খুঁজুন। Plugin নিজে লিখলে `Package.swift` দিন।

**ফাঁদ:** `Package.resolved` git-এ না রাখা। তখন প্রতিটা machine আলাদা version পেতে পারে — `pubspec.lock` commit না করার মতো সমস্যা। App project-এ এটা commit করুন।

[উপরে ফিরুন](#toc)

### <a id="ios3-6"></a>iOS ৩.৬ Info.plist

**এক লাইনে:** App-এর পরিচয়পত্র — iOS app খোলার আগেই এটা পড়ে। AndroidManifest-এর একটা বড় অংশের কাজ এখানে। তবে iOS-এ কোনো component (Activity, Service) ঘোষণা করতে হয় না।

Info.plist একটা XML file, key-value-এর dictionary। Xcode-এ table-এর মতো দেখায়; ডান-click → "Open As → Source Code" দিলে XML।

**Notes app-এ যা থাকবে:**

```xml
<!-- পরিচয় -->
<key>CFBundleDisplayName</key>
<string>$(APP_DISPLAY_NAME)</string>
<key>CFBundleShortVersionString</key>
<string>$(MARKETING_VERSION)</string>
<key>CFBundleVersion</key>
<string>$(CURRENT_PROJECT_VERSION)</string>

<!-- permission-এর কারণ — না থাকলে camera ছোঁয়ার সাথে সাথে crash -->
<key>NSCameraUsageDescription</key>
<string>Note-এ ছবি যোগ করতে camera লাগবে।</string>
<key>NSPhotoLibraryAddUsageDescription</key>
<string>Note-এর ছবি Photos-এ save করতে।</string>

<!-- নিজের URL scheme: notesapp://note/42 -->
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array><string>notesapp</string></array>
  </dict>
</array>

<!-- Background-এ কী করার অনুমতি চাই -->
<key>UIBackgroundModes</key>
<array><string>remote-notification</string></array>
```

| কাজ | Android (Manifest) | iOS (Info.plist) |
|---|---|---|
| Permission | `<uses-permission>` — ঘোষণা | `NS...UsageDescription` — ঘোষণা নেই, শুধু user-কে দেখানোর কারণ |
| Deep link | `<intent-filter>` | `CFBundleURLTypes` (scheme), Associated Domains entitlement (universal link) |
| App-এর নাম, icon | `android:label`, `android:icon` | `CFBundleDisplayName`, Assets-এর AppIcon |
| Background কাজ | `<service>`, foreground service type | `UIBackgroundModes` |
| Screen ঘোষণা | `<activity>` | লাগে না |
| Scene / window | (নেই) | `UIApplicationSceneManifest` ([iOS ৪.১](#ios4-1)) |

**Permission-এর বড় পার্থক্য:** Android-এ Manifest-এ permission না লিখলে request-ই করা যায় না। iOS-এ permission-এর আলাদা ঘোষণা নেই — শুধু কারণের string। String না থাকলে, প্রথমবার camera বা photo ছুঁলেই app crash করে। Flutter-এ `image_picker` যোগ করে Info.plist-এ লাইন লিখতে ভুলে গেলে যে crash হতো, সেটাই। কারণের লেখাটাও review-এ দেখা হয় — "camera লাগবে" যথেষ্ট না, কেন লাগবে বলুন।

**Privacy manifest — `PrivacyInfo.xcprivacy` (চিনে রাখুন):** Info.plist-এর পাশে আরেকটা plist। App (আর প্রতিটা SDK) কোন data collect করে, আর কিছু নির্দিষ্ট API (যেমন `UserDefaults`, file-এর timestamp) কেন ব্যবহার করে, সেটা এখানে লিখতে হয়। ১ মে ২০২৪ থেকে নতুন app আর update-এ এই API-গুলোর কারণ না থাকলে App Store Connect upload আটকে দেয়। Flutter template-এ এই file নেই — নিজের code বা plugin এসব API ব্যবহার করলে নিজে যোগ করতে হয়। Release-এর বিস্তারিত পরের অধ্যায়গুলোতে।

[উপরে ফিরুন](#toc)

### <a id="ios3-7"></a>iOS ৩.৭ Entitlements

**এক লাইনে:** Entitlement হলো app-এর বিশেষ ক্ষমতার তালিকা — push, App Group, Keychain ভাগ করা, universal link, iCloud। এগুলো একটা `.entitlements` file-এ থাকে, আর signing-এর সময় app-এর signature-এর ভেতরে ঢুকে যায়।

Xcode-এ target → **Signing & Capabilities** → "+ Capability" চাপলে Xcode নিজে `Runner.entitlements` বানায় বা বদলায়:

```xml
<!-- Notes.entitlements -->
<key>aps-environment</key>
<string>development</string>                         <!-- push notification -->

<key>com.apple.security.application-groups</key>
<array><string>group.com.byteonyx.notes</string></array>   <!-- widget-এর সাথে data ভাগ -->

<key>com.apple.developer.associated-domains</key>
<array><string>applinks:notes.byteonyx.com</string></array> <!-- universal link -->
```

**Info.plist আর entitlement-এর পার্থক্য:**

| | Info.plist | Entitlements |
|---|---|---|
| কী | app-এর তথ্য আর অনুরোধ | app-এর ক্ষমতা |
| কে check করে | iOS, চলার সময় | iOS, signature থেকে — আর provisioning profile-এ থাকতেই হবে |
| ভুল হলে | crash বা feature কাজ করে না | install বা upload ব্যর্থ, বা feature নিঃশব্দে কাজ করে না |
| Android-এ কাছাকাছি | Manifest | (সরাসরি নেই — signature permission-এর কাছাকাছি) |

**কেন profile-এ থাকতে হয়:** Apple Developer portal-এ App ID-তে capability চালু থাকতে হয়, আর provisioning profile-এ সেটা থাকতে হয়। Xcode-এর "Automatically manage signing" এটা নিজে মেলায়। হাতে signing করলে (CI) profile নতুন করে বানাতে হয়। Signing আর release-এর পুরো গল্প পরের অধ্যায়গুলোতে।

**ফাঁদ:** Flutter-এ `firebase_messaging` যোগ করে push কাজ করছে না — প্রায়ই কারণ Push Notifications capability যোগ করা হয়নি, তাই `aps-environment` entitlement নেই। Dart-এ স্পষ্ট কারণ আসে না, শুধু token আসে না। Xcode console-এ "no valid 'aps-environment' entitlement string found" দেখলে বুঝবেন এটাই।

[উপরে ফিরুন](#toc)

### <a id="ios3-8"></a>iOS ৩.৮ Deployment target আর SDK

**এক লাইনে:** **Deployment target** = সবচেয়ে পুরনো যে iOS-এ app চলবে (Android-এর `minSdk`)। **SDK** = যে iOS version-এর SDK দিয়ে build করছেন — Xcode-এর সাথে আসে।

Android-এ তিনটা সংখ্যা ছিল ([অধ্যায় ৩](#ch3)): `minSdk`, `compileSdk`, `targetSdk`। iOS-এ মূলত দুইটা:

| Android | iOS | মানে |
|---|---|---|
| `minSdk` | Deployment target (`IPHONEOS_DEPLOYMENT_TARGET`) | এর চেয়ে পুরনো iOS-এ install-ই হবে না |
| `compileSdk` | SDK — Xcode-এর version ঠিক করে | কোন API দেখা যাবে |
| `targetSdk` | আলাদা setting নেই — SDK-ই এই কাজ করে | নতুন আচরণ চালু হবে কি না |

**শেষ লাইনটা জরুরি।** iOS-এ অনেক নতুন নিয়ম "linked-on-or-after" — মানে যে SDK দিয়ে build করছেন, তার ওপর নির্ভর করে। যেমন UIScene: iOS 26-এর পরের major release-এর SDK দিয়ে build করলে UIScene না থাকলে app launch-ই হবে না ([iOS ৪.১](#ios4-1))। তাই Xcode বদলানো মানে Android-এ `targetSdk` বাড়ানোর মতো — আচরণ বদলাতে পারে। নতুন Xcode-এ যাওয়ার পরে পুরো app একবার test করুন।

**সংখ্যাগুলো আজ (নভেম্বর ২০২৬):**
- **Flutter:** iOS 15 থেকে সমর্থন। নতুন Flutter project-এর template-এ deployment target `15.0`।
- **App Store upload:** ২৮ এপ্রিল ২০২৬ থেকে Xcode 26 বা নতুন, iOS 26 SDK দিয়ে build বাধ্যতামূলক। Apple সাধারণত প্রতি বছর বসন্তে এই নিয়ম এক ধাপ বাড়ায় — [developer.apple.com/news/upcoming-requirements](https://developer.apple.com/news/upcoming-requirements/) দেখুন।
- **নতুন native app:** `@Observable` আর SwiftData চাইলে iOS 17। বেশিরভাগ নতুন app এখন iOS 17 বা 18 থেকে শুরু করে।

**কোড-এ পুরনো iOS সামলানো:**

```swift
@available(iOS 18, *)
struct NotesTabs: View { ... }         // পুরো type শুধু iOS 18+

if #available(iOS 18, *) {
    NotesTabs()
} else {
    LegacyNotesTabs()
}
```

**Plugin-এর deployment target:** প্রতিটা plugin-এর নিজের minimum iOS আছে। App-এর deployment target তার চেয়ে কম হলে build ব্যর্থ। Flutter-এ `pod install` বা build-এর সময় deployment target নিয়ে যে error বা warning আসে, সেগুলো প্রায় সবসময় এই কারণেই।

> **মনে রাখুন**
> - Target = কী বানাবেন, configuration = কোন setting-এ, scheme = কোন বোতামে কোনটা।
> - Flutter-এর `--flavor dev` = scheme `dev` + configuration `Debug-dev` / `Release-dev` / `Profile-dev`।
> - Setting xcconfig-এ রাখুন। `//` comment, আর app-এ কোনো secret না।
> - SPM-ই পথ। Flutter 3.44 থেকে ডিফল্ট, CocoaPods trunk ২ ডিসেম্বর ২০২৬ থেকে read-only।
> - Info.plist-এ permission-এর কারণ না থাকলে crash। ক্ষমতা (push, App Group) entitlement-এ, আর profile-এ।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ flavor বলে কিছু নেই। আমি প্রতিটা environment-এর জন্য একটা shared scheme আর আলাদা build configuration বানাই, আর setting রাখি xcconfig-এ — bundle id, display name, API host। Flutter-এর `--flavor dev` ঠিক এই নামের scheme আর `Debug-dev`-এর মতো configuration খোঁজে। Dependency-র জন্য Swift Package Manager নিই, কারণ Flutter 3.44 থেকে এটাই ডিফল্ট আর CocoaPods বন্ধের পথে।"
> - *English:* "iOS has no flavors as such. I create a shared scheme per environment with its own build configurations, and keep the settings in xcconfig files — bundle id, display name, API host. Flutter's `--flavor dev` looks for exactly that scheme and configurations named like `Debug-dev`. For dependencies I use Swift Package Manager, since it's the default from Flutter 3.44 and CocoaPods is being wound down."

[উপরে ফিরুন](#toc)

---

## <a id="ios4"></a>iOS ৪. App lifecycle — `@main`, AppDelegate, SceneDelegate আর suspension

Android-এর lifecycle অধ্যায়ে ([অধ্যায় ৫](#ch5)) সবচেয়ে বড় ধাক্কা ছিল rotation-এ Activity মরে যাওয়া। iOS-এ সেই ধাক্কা নেই — rotation, dark mode, ভাষা বদলালে screen বেঁচে থাকে, শুধু layout বদলায়। ঠিক Flutter-এর মতো। স্বস্তি!

কিন্তু iOS-এর নিজের একটা ধাক্কা আছে: **background-এ গেলে app ঘুমিয়ে পড়ে।** কোনো code চলে না। আর ঘুমন্ত app-কে system কোনো খবর না দিয়ে মেরে দিতে পারে। এই অধ্যায় সেই নিয়মগুলো নিয়ে।

### <a id="ios4-1"></a>iOS ৪.১ চালু হওয়া: `@main` থেকে প্রথম screen

**এক লাইনে:** Flutter-এর `void main() => runApp(NotesApp())`-এর জায়গায় SwiftUI-তে একটা struct, যার মাথায় `@main`, আর যে `App` protocol মানে।

**Flutter-এ:**

```dart
void main() {
  runApp(const NotesApp());
}

class NotesApp extends StatelessWidget {
  const NotesApp({super.key});
  @override
  Widget build(BuildContext context) => const MaterialApp(home: NotesListScreen());
}
```

**SwiftUI-তে:**

```swift
import SwiftUI

@main
struct NotesApp: App {
    @State private var store = NotesStore()           // NotesStore একটা @Observable class; app-এর আয়ু জুড়ে বাঁচে

    var body: some Scene {
        WindowGroup {
            NotesListView()
                .environment(store)
        }
    }
}
```

- `@main` বলে দেয়, app এখান থেকে শুরু। আলাদা `main()` লেখা লাগে না।
- `App`-এর `body` widget না, **Scene** ফেরত দেয়। `WindowGroup` মানে "app-এর window" — iPhone-এ একটা, iPad-এ user একাধিক খুলতে পারে।
- `MaterialApp`-এর মতো কোনো root wrapper লাগে না। Theme, navigation সব view-এর modifier।

**Push token-এর মতো process-এর কাজ লাগলে — AppDelegate জুড়ে দেওয়া:**

```swift
final class AppDelegate: NSObject, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
    ) {
        // APNs token server-এ পাঠান
    }
}

@main
struct NotesApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate
    var body: some Scene { WindowGroup { NotesListView() } }
}
```

**UIKit-এর পুরনো পথ (চিনে রাখুন) — দুই delegate:**

```
@main AppDelegate (UIApplicationDelegate)   ← process-এর ঘটনা: launch, push token, terminate
        │
        └─ SceneDelegate (UIWindowSceneDelegate) ← প্রতিটা window-এর ঘটনা:
               scene(_:willConnectTo:options:)      window তৈরি, প্রথম ViewController বসানো
               sceneDidBecomeActive / sceneWillResignActive
               sceneWillEnterForeground / sceneDidEnterBackground
               scene(_:openURLContexts:)            deep link
```

iOS 13-এর আগে সব কিছু AppDelegate-এ ছিল। iOS 13 iPad-এ একাধিক window আনল, তাই window-এর কাজ SceneDelegate-এ সরল। SwiftUI-র `App` ভেতরে নিজেই scene-ভিত্তিক।

**UIScene এখন বাধ্যতামূলক — এবং এটা Flutter-কেও ছোঁয়:** Apple-এর TN3187 বলে, iOS 26-এর পরের major release-এর SDK দিয়ে build করলে UIScene lifecycle ছাড়া app **launch-ই হবে না।** iOS 27 SDK (Xcode 27) এখন বের হয়ে গেছে, তাই পুরনো "শুধু AppDelegate" app-এর আর সময় নেই।
- SwiftUI `App` দিয়ে বানানো app আগে থেকেই scene-ভিত্তিক — কিছু করতে হয় না।
- Flutter 3.38-এ UIScene সমর্থন এসেছে, আর **3.41 থেকে এটা ডিফল্ট।** AppDelegate-এ হাত না দিয়ে থাকলে `flutter run` বা `flutter build ios` নিজে migrate করে দেয়। এজন্যই নতুন template-এ `SceneDelegate.swift` আর `FlutterImplicitEngineDelegate` ([iOS ০.১](#ios0-1))।
- AppDelegate নিজে বদলে থাকলে হাতে migrate করতে হয়: plugin registration `didInitializeImplicitFlutterEngine`-এ সরান, Info.plist-এ `UIApplicationSceneManifest` যোগ করুন। আর `didFinishLaunchingWithOptions`-এ `FlutterViewController` ছোঁবেন না — তখনো window তৈরি হয়নি, crash হতে পারে।
- Deep link আর অন্য scene-এর ঘটনা এখন SceneDelegate-এ আসে। পুরনো plugin AppDelegate-এর `application(_:open:options:)`-এ বসে থাকলে আর ঘটনা পাবে না। `FlutterSceneDelegate` এই ঘটনাগুলো plugin-এ পৌঁছে দেয় — এজন্যই Flutter এটা subclass করতে বলে।

**ভেতরে কীভাবে কাজ করে — launch-এর ক্রম (UIKit):**
1. System process বানায়, `main()` চলে (`@main` দিয়ে Swift নিজে বানায়)।
2. `UIApplicationMain` → `UIApplication` আর আপনার AppDelegate তৈরি।
3. `application(_:willFinishLaunchingWithOptions:)` → `application(_:didFinishLaunchingWithOptions:)`।
4. Scene তৈরি → `scene(_:willConnectTo:options:)` → window আর প্রথম screen।
5. Scene সামনে আসে → `sceneDidBecomeActive`।

**Senior-এর সূক্ষ্ম কথা — prewarming:** iOS কখনো কখনো user tap করার আগেই আপনার process বানিয়ে library load করে রাখে, তারপর suspend করে দেয়। তাই "process শুরু থেকে প্রথম frame" মাপা launch time অনেক বেশি দেখাতে পারে। আর `main()`-এর আগে চলা code-এ (static initializer) এমন কিছু করবেন না, যা ধরে নেয় user এখনই app খুলছে।

[উপরে ফিরুন](#toc)

### <a id="ios4-2"></a>iOS ৪.২ App-এর অবস্থাগুলো

**এক লাইনে:** iOS-এ app পাঁচ অবস্থায় থাকতে পারে। সবচেয়ে জরুরি হলো শেষেরটা — **Suspended**, যেখানে app memory-তে আছে কিন্তু কিছুই চলে না।

```
                    user app খুলল
  Not running ──────────────────────────► Inactive ◄──────► Active
       ▲                                     │   (call, Control Center,     (সামনে, touch পাচ্ছে)
       │                                     │    app switcher, alert)
       │                                     ▼
       │                                 Background ── অল্প সময় code চলে
       │  system মেরে দিল                    │
       │  (কোনো callback নেই)                ▼
       └──────────────────────────────── Suspended ── memory-তে, কিন্তু code চলে না
```

| অবস্থা | কী হচ্ছে | Code চলে? |
|---|---|---|
| Not running | চালু হয়নি, বা মেরে ফেলা হয়েছে | না |
| Inactive | সামনে আছে, কিন্তু touch পাচ্ছে না (call এল, Control Center টানল, app switcher) | হ্যাঁ |
| Active | সামনে, touch পাচ্ছে | হ্যাঁ |
| Background | দেখা যাচ্ছে না, শেষ কাজ গোছাচ্ছে | হ্যাঁ, অল্প সময় |
| Suspended | Memory-তে ঘুমিয়ে | **না** |

**Scene-এর অবস্থা:** UIScene-এ প্রতিটা window-এর নিজের অবস্থা: Unattached → Foreground Inactive → Foreground Active → Background। iPhone-এ একটাই scene, তাই app আর scene প্রায় একসাথে চলে।

**Flutter-এর কাছে এটা কেমন দেখায়:** Flutter engine এই ঘটনাগুলো শুনে `AppLifecycleState` বানায় ([iOS ৪.৩](#ios4-3)-এর table)। Suspended-এ Flutter-এর কোনো callback আসে না — কারণ তখন Dart code-ও চলে না।

[উপরে ফিরুন](#toc)

### <a id="ios4-3"></a>iOS ৪.৩ `scenePhase` — `didChangeAppLifecycleState`-এর জায়গায়

**এক লাইনে:** SwiftUI-তে `@Environment(\.scenePhase)` পড়ুন, আর `.onChange` দিয়ে বদল শুনুন। তিনটা মান: `.active`, `.inactive`, `.background`।

**Flutter-এ:**

```dart
class _EditorState extends State<NoteEditor> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.paused) saveDraft();
    if (state == AppLifecycleState.resumed) refreshNotes();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }
}
```

**SwiftUI-তে:**

```swift
struct NoteEditorView: View {
    @Environment(\.scenePhase) private var scenePhase
    @Bindable var model: NoteEditorModel

    var body: some View {
        TextEditor(text: $model.draftText)
            .onChange(of: scenePhase) { _, newPhase in
                switch newPhase {
                case .background:
                    model.saveDraft()          // ঘুমানোর আগে save
                case .active:
                    Task { await model.refresh() }
                case .inactive:
                    break
                @unknown default:
                    break
                }
            }
    }
}
```

Observer যোগ বা বাদ দেওয়ার ঝামেলা নেই। View চলে গেলে শোনাও বন্ধ।

- কোনো view-এর ভেতরে পড়লে `scenePhase` সেই view-এর scene-এর অবস্থা দেয়।
- `App`-এর `body`-তে পড়লে সব scene মিলিয়ে একটা অবস্থা দেয় — কোনো একটা active থাকলেই `.active`।
- `@unknown default` — Apple পরে নতুন case যোগ করতে পারে, তাই compiler এটা চায়।

**তিন জগতের mapping:**

| iOS (UIKit scene) | SwiftUI `scenePhase` | Flutter `AppLifecycleState` | Android |
|---|---|---|---|
| Scene connect, `willConnectTo` | (view প্রথম দেখা যায়) | engine চালু, `resumed`-এর আগে | `onCreate` |
| `sceneWillEnterForeground` | `.inactive` | `inactive` | `onStart` |
| `sceneDidBecomeActive` | `.active` | `resumed` | `onResume` |
| `sceneWillResignActive` (call, Control Center) | `.inactive` | `inactive` | `onPause` |
| `sceneDidEnterBackground` | `.background` | `hidden` → `paused` | `onStop` |
| Suspended | (কিছু আসে না) | (কিছু আসে না) | (process cached) |
| Engine-এর সব view চলে গেছে | — | `detached` | `onDestroy` |

`hidden` অবস্থাটা iOS-এর নিজের না। Flutter 3.13 থেকে সব platform-এর state machine এক রাখতে, iOS-এ `inactive` আর `paused`-এর মাঝে Flutter নিজে `hidden` বসায়।

**Best approach:** Draft save করার জায়গা `.background`। কিন্তু শুধু এর ওপর ভরসা করবেন না — user টাইপ করার সময়েই অল্প পরপর (debounce করে) save করুন। কারণ পরের অংশে।

[উপরে ফিরুন](#toc)

### <a id="ios4-4"></a>iOS ৪.৪ Background suspension আর termination

**এক লাইনে:** Background-এ গেলে app অল্প সময় পায়, তারপর suspend। Suspended app-কে memory লাগলে system মেরে দেয় — **কোনো callback ছাড়া।** User ফিরে এলে app শূন্য থেকে চালু হয়।

**গল্পটা Notes app-এ:**
1. User একটা note লিখছে। অর্ধেক লিখে Camera app খুলল।
2. আপনার app `.background` পেল। অল্প পরেই suspend — সব Dart বা Swift code থেমে গেল।
3. Camera অনেক memory চাইল। System আপনার suspended app মেরে দিল। কোনো `applicationWillTerminate` আসেনি।
4. User ফিরে এল। App **নতুন করে launch** হলো। Memory-র সব কিছু শূন্য।

**`applicationWillTerminate`-এর ওপর ভরসা করবেন না।** Apple-এর docs স্পষ্ট বলে: background সমর্থন করা app-এ user app বন্ধ করলে এটা সাধারণত call হয় না। শুধু তখন হয়, যখন app background-এ সক্রিয়ভাবে কিছু চালাচ্ছে (suspended না) আর system মেরে দেয়। App switcher থেকে swipe করে বন্ধ করলে suspended app কোনো খবর পায় না।

**জরুরি কাজ শেষ করতে একটু সময় চাওয়া:**

```swift
@MainActor
final class DraftSaver {
    private var taskID: UIBackgroundTaskIdentifier = .invalid
    private let draftStore: DraftStore             // ধরুন একটা actor, যে draft disk-এ লেখে

    init(draftStore: DraftStore) {
        self.draftStore = draftStore
    }

    func saveBeforeSuspension() {
        taskID = UIApplication.shared.beginBackgroundTask(withName: "save-draft") { [weak self] in
            self?.finish()                         // সময় শেষ — system মারার আগে নিজে বন্ধ করুন
        }
        Task {
            await draftStore.flush()
            finish()                               // কাজ শেষ — সাথে সাথে জানান
        }
    }

    private func finish() {
        guard taskID != .invalid else { return }
        UIApplication.shared.endBackgroundTask(taskID)
        taskID = .invalid
    }
}
```

এটা "একটু বেশি সময়" — অনির্দিষ্ট না। System নিজে ঠিক করে কতক্ষণ, আর `backgroundTimeRemaining` দেখা যায়। `endBackgroundTask` না ডাকলে system app মেরে দিতে পারে।

**Background-এ নিয়মিত কাজ (sync, upload) চাইলে:** iOS-এর নির্দিষ্ট পথ — `BGTaskScheduler`, background `URLSession`, silent push, background mode। এগুলো পরের অধ্যায়গুলোতে। মূল কথা: iOS ঠিক করে কখন চালাবে, আপনি না। Android-এর WorkManager-এর চেয়েও কম নিশ্চয়তা।

| | iOS | Android | Flutter-এ যা দেখতেন |
|---|---|---|---|
| Background-এ গেলে | অল্প সময়, তারপর suspend | Process চলতে থাকে (cached), কিছু কাজ চলে | `paused` |
| মেরে ফেলা | Suspended app, কোনো callback নেই | Process death, কোনো callback নেই | কিছুই আসে না |
| লম্বা কাজ | `BGTaskScheduler`, background `URLSession` | WorkManager, foreground service | `workmanager` |
| User swipe করে বন্ধ করলে | Suspended হলে কোনো খবর নেই | একই | কিছু আসে না |

**ফাঁদ:** `.background`-এ লম্বা network call শুরু করা, শেষ হবে ভেবে। App suspend হলে call মাঝপথে থামে। Upload শেষ হওয়া জরুরি হলে background `URLSession` লাগবে।

[উপরে ফিরুন](#toc)

### <a id="ios4-5"></a>iOS ৪.৫ State restoration — `@SceneStorage`

**এক লাইনে:** System app মেরে দেওয়ার পরে user ফিরলে, iOS চায় app আগের জায়গায় ফিরুক — খোলা note, লেখা text। SwiftUI-তে ছোট UI state-এর জন্য `@SceneStorage`।

**Flutter-এ:** `RestorationMixin`, `RestorableTextEditingController`, আর `MaterialApp`-এ `restorationScopeId`। বেশিরভাগ Flutter app এটা করে না, শুরু থেকে খোলে।

**SwiftUI-তে:**

```swift
struct NotesRootView: View {
    @SceneStorage("selectedNoteID") private var selectedNoteID: String?   // কোন note খোলা ছিল
    @SceneStorage("draftText") private var draftText = ""                  // অর্ধেক লেখা

    var body: some View {
        NavigationStack {
            NotesListView(selectedNoteID: $selectedNoteID)
        }
    }
}
```

- `@State`-এর মতোই কাজ করে, কিন্তু system মান save করে, আর app নতুন করে চালু হলে ফেরত দেয়।
- **প্রতিটা scene-এর নিজের।** iPad-এ দুই window-এ দুইটা আলাদা draft।
- শুধু ছোট আর সাধারণ type: `String`, `Int`, `Bool`, `Double`, `URL`, `Data`, আর এদের `RawRepresentable` enum। Note-এর list না — শুধু id।
- কখন save হবে, তার কোনো নিশ্চয়তা নেই (Apple-এর docs নিজেই বলে)। আর scene ধ্বংস হলে data-ও মুছে যায় — যেমন user app switcher থেকে window সরিয়ে দিলে। তাই এটা "সুবিধা", data বাঁচানোর জায়গা না।
- Secret বা ব্যক্তিগত data এখানে না — Apple মানা করে।

**State কোথায় রাখবেন — এক table-এ:**

| State | কোথায় | Rotation-এ | System মারলে | User swipe করে বন্ধ করলে | Android-এ |
|---|---|---|---|---|---|
| ছোট UI state (menu খোলা কি না) | `@State` | থাকে | হারায় | হারায় | `remember` |
| ফিরে আসা উচিত এমন UI state (খোলা note-এর id, লেখা text) | `@SceneStorage` | থাকে | থাকে | হারায় | `rememberSaveable` |
| Screen-এর state আর logic | `@Observable` model | থাকে | হারায় | হারায় | `ViewModel` |
| User-এর setting | `@AppStorage` (`UserDefaults`) | থাকে | থাকে | থাকে | DataStore |
| আসল data, draft | SwiftData, file, server | থাকে | থাকে | থাকে | Room |

**Best approach:** আসল data আর অর্ধেক লেখা draft — database-এ, টাইপ করার সময়েই। কোন screen খোলা ছিল, কোন note — `@SceneStorage`-এ id। তাহলে app কীভাবে মরল, তাতে কিছু যায় আসে না।

**নিজে test করুন:**
1. Xcode থেকে app চালান। একটা note খুলে কিছু লিখুন।
2. Home-এ যান (app background-এ)।
3. Xcode-এর ■ Stop বোতাম চাপুন — এটা system-এর মেরে ফেলার মতো।
4. Home screen থেকে app আবার খুলুন।

যা হারাল, সেগুলোই bug। Android-এ `adb shell am kill`-এর কাজ এটা। (App switcher থেকে swipe করে বন্ধ করে test করবেন না — তখন iOS ইচ্ছা করেই restoration data মুছে দেয়।)

[উপরে ফিরুন](#toc)

### <a id="ios4-6"></a>iOS ৪.৬ Memory warning

**এক লাইনে:** Memory কম পড়লে iOS আগে সতর্ক করে। তখন cache ছেড়ে দিন। না ছাড়লে, বা অনেক বেশি memory নিলে, system app মেরে দেয় — foreground-এ থাকলেও।

**Flutter-এ:** `WidgetsBindingObserver.didHaveMemoryPressure()`। Flutter engine নিজেও তখন image cache কমায়।

**iOS-এ:**

```swift
// যেকোনো জায়গা থেকে — AsyncSequence হিসেবে
.task {
    let warnings = NotificationCenter.default.notifications(
        named: UIApplication.didReceiveMemoryWarningNotification
    )
    for await _ in warnings {
        thumbnailCache.removeAll()
    }
}
```

UIKit-এ: `UIApplicationDelegate.applicationDidReceiveMemoryWarning(_:)`, আর প্রতিটা `UIViewController`-এর `didReceiveMemoryWarning()`।

**ভেতরে কীভাবে কাজ করে — jetsam:** iPhone-এ swap নেই — memory disk-এ সরানো যায় না, শুধু compress হয়। Memory ফুরালে kernel-এর **jetsam** ব্যবস্থা অগ্রাধিকার দেখে process মারে — আগে suspended app, তারপর background, শেষে দরকার হলে foreground-ও। Foreground app memory-র সীমা পার হলে মারা যায়, crash log ছাড়াই। Xcode Organizer-এ এগুলো "Terminations" হিসেবে দেখা যায়।

| | iOS | Android | Flutter |
|---|---|---|---|
| সতর্কবার্তা | `didReceiveMemoryWarningNotification` | `onTrimMemory()` | `didHaveMemoryPressure()` |
| শেষ ব্যবস্থা | jetsam process মারে | Low Memory Killer | — |
| Swap | iPhone-এ নেই (compressed memory) | zRAM (compressed) | — |

**ফাঁদ:** বড় ছবি পুরো resolution-এ decode করে রাখা। একটা 12MP ছবি decode হলে প্রায় ৪৮ MB (৪ byte প্রতি pixel)। Note-এ দশটা ছবি মানে app মারা যাওয়া। Thumbnail বানিয়ে রাখুন — Flutter-এ `cacheWidth` দেওয়ার মতো।

[উপরে ফিরুন](#toc)

### <a id="ios4-7"></a>iOS ৪.৭ Android-এর সাথে তুলনা — কোনটা নেই, কোনটা বেশি

| বিষয় | Android | iOS |
|---|---|---|
| Rotation, dark mode, ভাষা বদল | Activity destroy আর নতুন তৈরি ([৫.২](#ch5-2)) | কিছু মরে না, শুধু layout/trait বদলায় |
| তাই `ViewModel`-এর মতো "rotation-এ বাঁচা" জিনিস লাগে? | হ্যাঁ | না — `@Observable` model সাধারণ object |
| Background-এ code | চলতে পারে, সীমা আছে | অল্প সময়, তারপর suspend |
| Process death | Background-এ থাকলে, callback নেই | Suspended থাকলে, callback নেই |
| ফিরে এলে system কোথায় খোলে | ঠিক আগের Activity, back stack-সহ | যা আপনি `@SceneStorage` দিয়ে ফেরান — নইলে শুরু থেকে |
| Restoration-এর বাক্স | Bundle (~১ MB) | `@SceneStorage` (ছোট রাখুন) |
| Test | `adb shell am kill` | Background + Xcode Stop |

সবচেয়ে বড় পার্থক্য পঞ্চম লাইনে। Android system নিজে back stack ফেরত দেয় আর আশা করে app ঠিক জায়গায় চলবে। iOS শুধু বাক্সটা দেয় — কী ফেরাবেন, সেটা আপনার সিদ্ধান্ত।

> **মনে রাখুন**
> - SwiftUI-তে `@main struct ...: App` + `WindowGroup`। UIKit-এ AppDelegate (process) + SceneDelegate (window)।
> - UIScene এখন বাধ্যতামূলক (TN3187)। Flutter 3.41 থেকে ডিফল্ট — পুরনো custom AppDelegate হাতে migrate করুন।
> - `scenePhase`: `.active` / `.inactive` / `.background`। Suspended-এ কিছু আসে না।
> - Suspended app-কে system নিঃশব্দে মারে। `applicationWillTerminate`-এ ভরসা না — টাইপ করার সময়েই save।
> - Rotation-এ কিছু মরে না — Android-এর বড় সমস্যাটা iOS-এ নেই।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ background-এ গেলে app অল্প সময় পায়, তারপর suspend হয়। Suspended app-কে memory লাগলে system কোনো callback ছাড়াই মেরে দেয়। তাই আমি draft টাইপ করার সময়েই database-এ save করি, আর `scenePhase` `.background` হলে শেষ flush করি — দরকার হলে `beginBackgroundTask` দিয়ে একটু সময় নিয়ে। কোন screen খোলা ছিল, সেই ছোট state `@SceneStorage`-এ রাখি। আর Flutter 3.41 থেকে iOS app-এ UIScene ডিফল্ট — নতুন SDK-তে এটা ছাড়া app launch-ই হবে না।"
> - *English:* "On iOS, an app gets a short time in the background and is then suspended. If the system needs memory, it kills a suspended app with no callback. So I save drafts to the database while the user types, and do a final flush when `scenePhase` becomes `.background`, using `beginBackgroundTask` if I need a bit more time. I keep small UI state like the open screen in `@SceneStorage`. And since Flutter 3.41, iOS apps use the UIScene lifecycle by default — with the newest SDK, an app without it won't launch."

[উপরে ফিরুন](#toc)

---

## <a id="ios5"></a>iOS ৫. SwiftUI — Widget-এর জায়গায় View

এই অধ্যায়ে আপনার Flutter-এর অভিজ্ঞতা সবচেয়ে বেশি কাজে লাগবে। SwiftUI ২০১৯-এ এসেছিল, Flutter-এর প্রায় একই সময়ে, একই ধারণা নিয়ে: **UI = f(state)।** State বদলান, framework নিজে দরকারি অংশ আবার আঁকবে।

Compose-এর অধ্যায় ([অধ্যায় ৬](#ch6)) পড়ে থাকলে দেখবেন, তিনটা framework প্রায় এক ভাষায় কথা বলে। পার্থক্য ছোট ছোট জায়গায় — আর সেগুলোতেই মানুষ আটকায়।

একটা কথা আগে: SwiftUI OS-এর সাথে আসে। তাই প্রতিটা API-র একটা minimum iOS আছে। এই অধ্যায়ের code iOS 17+ ধরে লেখা (`@Observable`-এর জন্য)। যেখানে iOS 18 লাগে, বলে দেওয়া আছে।

### <a id="ios5-1"></a>iOS ৫.১ Widget → View

**এক লাইনে:** `StatelessWidget` আর তার `build()`-এর জায়গায় একটা `struct`, যে `View` protocol মানে, আর যার একটা `body` property আছে।

**Flutter-এ:**

```dart
class NoteRow extends StatelessWidget {
  const NoteRow({super.key, required this.note});
  final Note note;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(note.title),
      subtitle: Text(note.preview, maxLines: 2),
      trailing: note.isPinned ? const Icon(Icons.push_pin) : null,
    );
  }
}
```

**SwiftUI-তে:**

```swift
struct NoteRow: View {
    let note: Note

    var body: some View {
        HStack {
            VStack(alignment: .leading, spacing: 4) {
                Text(note.title)
                    .font(.headline)
                Text(note.preview)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .lineLimit(2)
            }
            Spacer()
            if note.isPinned {
                Image(systemName: "pin.fill")
            }
        }
    }
}
```

| Flutter | SwiftUI | Compose |
|---|---|---|
| `StatelessWidget` class | `struct ...: View` | `@Composable fun` |
| `build(BuildContext)` | `var body: some View` | function body |
| constructor field | `let` property (memberwise init নিজে আসে) | parameter |
| `child:` / `children: [...]` | `{ }`-এর ভেতরে পরপর লেখা (result builder) | trailing lambda |
| `BuildContext` | নেই — দরকারি জিনিস `@Environment` দিয়ে | `CompositionLocal` |
| `const` widget | struct নিজেই সস্তা, আর SwiftUI নিজে তুলনা করে | compiler skip |
| `Icon(Icons.push_pin)` | `Image(systemName: "pin.fill")` — SF Symbols | `Icon(Icons.Default...)` |
| `if (x) widget` children-এ | `if x { View }` | `if (x) { }` |

**`some View` কেন:** `body`-এর আসল type হয় খুব লম্বা — `HStack<TupleView<(VStack<...>, Spacer, Optional<Image>)>>`। `some View` মানে "একটা নির্দিষ্ট View type, compiler জানে, আমি নাম লিখছি না" ([iOS ১.৭](#ios1-7))।

**`{ }`-এর ভেতরে পরপর View লেখা কীভাবে চলে:** `@ViewBuilder` নামের **result builder**। আপনি পরপর লিখে যান, compiler সেগুলো একটা tuple-এ জুড়ে দেয়। `if`, `if let`, `switch`, `ForEach` চলে, ছোট `let x = ...`-ও চলে। কিন্তু সাধারণ `for` loop, বা মান বদলানোর মতো অন্য statement চলে না — loop-এর জায়গায় `ForEach`, আর বাকি কাজ `body`-এর বাইরে বা আলাদা computed property-তে রাখুন।

**ভেতরে কীভাবে কাজ করে — তিন tree, Flutter-এর পাশে:**

| Flutter | SwiftUI |
|---|---|
| Widget — হালকা, অপরিবর্তনীয় বর্ণনা | View struct — হালকা value, বর্ণনা |
| Element — বেঁচে থাকে, state ধরে রাখে | SwiftUI-র ভেতরের graph (attribute graph) — view-এর identity আর state রাখে |
| RenderObject — layout আর paint | ভেতরে UIKit view আর Core Animation layer |

View struct প্রতিবার নতুন তৈরি হয়, ফেলে দেওয়া হয় — Widget-এর মতোই সস্তা। যা টিকে থাকে, সেটা SwiftUI-র ভেতরের graph। **বড় পার্থক্য:** Flutter প্রতিটা pixel নিজে আঁকে। SwiftUI শেষ পর্যন্ত Apple-এর নিজের UI system-এ আঁকে — তাই `Text` আসলে system-এর text, `List` ভেতরে UIKit-এর collection view। Accessibility, Dynamic Type, dark mode বিনা খরচে আসে।

[উপরে ফিরুন](#toc)

### <a id="ios5-2"></a>iOS ৫.২ Layout

**এক লাইনে:** `Column` → `VStack`, `Row` → `HStack`, `Stack` → `ZStack`। `Expanded` আর `SizedBox`-এর জায়গায় `Spacer()` আর `.frame()`।

**Notes app-এর header, দুই পাশে:**

```dart
Padding(
  padding: const EdgeInsets.all(16),
  child: Row(
    children: [
      const Icon(Icons.note),
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

```swift
HStack(spacing: 12) {
    Image(systemName: "note.text")
    VStack(alignment: .leading) {
        Text("আমার Notes").font(.title3)
        Text("\(count) টা note").foregroundStyle(.secondary)
    }
    Spacer()                                          // বাকি জায়গা খেয়ে ফেলে
    Button("খুঁজুন", systemImage: "magnifyingglass", action: onSearch)
        .labelStyle(.iconOnly)
}
.padding()
```

| Flutter | SwiftUI | Compose |
|---|---|---|
| `Column` | `VStack` | `Column` |
| `Row` | `HStack` | `Row` |
| `Stack` + `Positioned`/`Align` | `ZStack(alignment:)`, `.overlay`, `.background` | `Box` |
| `Expanded` | `Spacer()` বা `.frame(maxWidth: .infinity)` | `Modifier.weight(1f)` |
| `SizedBox(height: 16)` | `Spacer().frame(height: 16)` বা stack-এর `spacing:` | `Spacer(Modifier.height())` |
| `crossAxisAlignment` | `VStack(alignment: .leading)` | `horizontalAlignment` |
| `mainAxisAlignment: spaceBetween` | মাঝে `Spacer()` | `Arrangement.SpaceBetween` |
| `Center` | default — stack নিজেই মাঝে রাখে | `Box(contentAlignment = Center)` |
| `Wrap` | নিজে `Layout` protocol দিয়ে বানাতে হয় | `FlowRow` |
| `LayoutBuilder` | `GeometryReader` | `BoxWithConstraints` |
| `Scaffold` + `AppBar` | `NavigationStack` + `.navigationTitle`, `.toolbar` | `Scaffold` + `TopAppBar` |
| `SafeArea` | **default-এ চালু** — বাইরে যেতে `.ignoresSafeArea()` | `innerPadding` |
| logical pixel | point (pt) | `dp` |

**Layout কীভাবে হয় — Flutter-এর উল্টো দিক থেকে না, প্রায় একই:** Flutter-এ "constraints go down, sizes go up, parent sets position"। SwiftUI-তে: parent child-কে একটা **প্রস্তাবিত size** দেয় → child নিজের size বেছে নেয় → parent তাকে বসায়। পার্থক্য হলো, SwiftUI-তে child প্রস্তাব অগ্রাহ্য করতে পারে। `Text` সবসময় শুধু নিজের লেখার মাপ নেয়, যত জায়গাই দিন। তাই "পুরো চওড়া নাও" বলতে `.frame(maxWidth: .infinity)` লাগে।

**ফাঁদ — `VStack`-এর default spacing শূন্য না।** Flutter-এর `Column`-এ children গায়ে গায়ে থাকে। SwiftUI-র `VStack`/`HStack`-এ `spacing` না দিলে system নিজের একটা ফাঁক দেয়। Design-এর সাথে pixel মেলাতে চাইলে সবসময় `spacing:` লিখে দিন — `VStack(spacing: 0)`।

**ফাঁদ — safe area উল্টো।** Android-এ নতুন app default-এ edge-to-edge, `innerPadding` না দিলে content bar-এর নিচে চলে যায়। SwiftUI-তে উল্টো: content default-এ safe area-র ভেতরে থাকে। পুরো screen জুড়ে রং চাইলে background-এ `.ignoresSafeArea()` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios5-3"></a>iOS ৫.৩ Wrapper widget → modifier, আর ক্রমের নিয়ম

**এক লাইনে:** Flutter-এ padding, রং, tap — প্রতিটা আলাদা wrapper widget। SwiftUI-তে এগুলো view-এর পেছনে `.` দিয়ে লাগানো **modifier**। প্রতিটা modifier আগের view-টাকে মুড়ে একটা নতুন view বানায়।

**Flutter-এ:**

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

**SwiftUI-তে:**

```swift
Text(note.title)
    .padding()                    // ১. text-এর চারপাশে ফাঁক
    .background(.yellow)          // ২. ফাঁকসহ পুরোটা হলুদ
    .onTapGesture(perform: onTap) // ৩. পুরো হলুদ অংশে tap
```

**ক্রম — ভেতর থেকে বাইরে পড়ুন।** প্রথম modifier সবচেয়ে ভেতরে, শেষেরটা সবচেয়ে বাইরে:

```swift
Text("বাজার").padding().background(.yellow)   // হলুদের ভেতরে ফাঁক — Container(color, padding)
Text("বাজার").background(.yellow).padding()   // হলুদ শুধু লেখার গায়ে, বাইরে স্বচ্ছ ফাঁক
```

ওপরের প্রথম লাইনটা Flutter-এ এরকম হতো: `ColoredBox(color: yellow, child: Padding(child: Text))` — আপনি nesting ভেতর থেকে বাইরে পড়ছেন।

| Flutter wrapper | SwiftUI modifier |
|---|---|
| `Padding` | `.padding()`, `.padding(.horizontal, 16)` |
| `Container(color:)`, `ColoredBox` | `.background(.yellow)` |
| `SizedBox(width:, height:)` | `.frame(width:height:)` |
| `ClipRRect` | `.clipShape(.rect(cornerRadius: 12))` |
| `Opacity` | `.opacity(0.8)` |
| `GestureDetector(onTap:)` | `.onTapGesture { }` বা `Button` |
| `DecoratedBox` + border | `.overlay { RoundedRectangle(...).stroke() }` |
| `Theme.of(context).textTheme.titleLarge` | `.font(.title)` |
| `DefaultTextStyle` | parent-এ `.font()` দিলে ভেতরের সব `Text` পায় |

**Compose-এর সাথে একটা ছোট মজা:** Compose-এ modifier chain বাইরে থেকে ভেতরে পড়তে হয় ([৬.৩](#ch6-3)) — `Modifier.padding(16.dp).background(Yellow)`-এ padding বাইরে। SwiftUI-তে উল্টো দিক থেকে পড়ুন — `.padding().background(.yellow)`-এ background বাইরে। দুই framework-এ একই লেখা, উল্টো ছবি। নিয়মটা মনে না থাকলে Preview-তে দেখে নিন।

**Best approach:** Tap-যোগ্য জিনিসে `.onTapGesture` না দিয়ে `Button` ব্যবহার করুন। `Button` নিজে accessibility (VoiceOver-এ "button"), pressed অবস্থা, keyboard সব সামলায়। Flutter-এ `GestureDetector`-এর বদলে `InkWell` বা `TextButton` নেওয়ার মতো।

[উপরে ফিরুন](#toc)

### <a id="ios5-4"></a>iOS ৫.৪ `ListView.builder` → `List` আর `LazyVStack`

**এক লাইনে:** দুইটা পথ। `List` — iOS-এর চেনা চেহারার list, swipe-to-delete, pull-to-refresh সব তৈরি। `ScrollView` + `LazyVStack` — নিজের ডিজাইনের list, শুধু দেখা অংশ বানায়।

**Flutter-এ:**

```dart
RefreshIndicator(
  onRefresh: cubit.refresh,
  child: ListView.builder(
    itemCount: notes.length,
    itemBuilder: (context, i) => Dismissible(
      key: ValueKey(notes[i].id),
      onDismissed: (_) => cubit.delete(notes[i]),
      child: NoteRow(note: notes[i]),
    ),
  ),
)
```

**SwiftUI-তে — `List`:**

```swift
List {
    ForEach(model.notes) { note in                  // Note: Identifiable, তাই id নিজে নেয়
        NoteRow(note: note)
            .swipeActions {
                Button("মুছুন", role: .destructive) {
                    model.delete(note)
                }
            }
    }
}
.refreshable { await model.refresh() }              // pull-to-refresh, async
.overlay {
    if model.notes.isEmpty {
        ContentUnavailableView("কোনো note নেই", systemImage: "note.text")   // iOS 17+
    }
}
```

**নিজের ডিজাইন — `LazyVStack`:**

```swift
ScrollView {
    LazyVStack(spacing: 8) {
        ForEach(model.notes) { note in
            NoteCard(note: note)
        }
    }
    .padding()
}
```

| Flutter | SwiftUI | Compose |
|---|---|---|
| `ListView.builder` | `List` / `ScrollView` + `LazyVStack` | `LazyColumn` |
| horizontal `ListView` | `ScrollView(.horizontal)` + `LazyHStack` | `LazyRow` |
| `GridView.builder` | `LazyVGrid(columns:)` | `LazyVerticalGrid` |
| `ListView(children:)` (সব একসাথে) | `ScrollView` + `VStack` | `Column` + `verticalScroll` |
| `Key` / `ValueKey(id)` | `Identifiable` বা `ForEach(..., id: \.id)` | `items(key = { it.id })` |
| `RefreshIndicator` | `.refreshable { }` | `PullToRefreshBox` |
| `Dismissible` | `.swipeActions { }`, `.onDelete` | `SwipeToDismissBox` |
| `ScrollController.animateTo` | `ScrollViewReader` / `.scrollPosition(id:)` | `rememberLazyListState()` |
| `SliverAppBar` + search | `.navigationTitle` + `.searchable(text:)` | `TopAppBar` + `SearchBar` |

**কখন কোনটা:** Settings-ধরনের, iOS-এর চেনা list — `List`। Card-এর feed, নিজের ডিজাইন — `LazyVStack`। `List` নিজে অনেক কিছু দেয় (separator, selection, edit mode, swipe), কিন্তু চেহারা বদলানো কঠিন।

**ফাঁদ — `ScrollView` + `VStack`।** `VStack` lazy না। ১০০০ note থাকলে ১০০০টাই একসাথে বানায় — Flutter-এ `ListView(children: [...])`-এ বিশাল list দেওয়ার মতো। বড় list-এ সবসময় `List` বা `LazyVStack`।

**ফাঁদ — id স্থির রাখুন।** `ForEach(notes, id: \.self)` বা index দিয়ে id দিলে note বদলালে SwiftUI ভাবে এটা নতুন item — state হারায়, animation ভুল হয়। Database-এর স্থির id দিন ([iOS ৫.১০](#ios5-10))।

[উপরে ফিরুন](#toc)

### <a id="ios5-5"></a>iOS ৫.৫ `setState` → `@State`

**এক লাইনে:** `StatefulWidget`-এর field + `setState`-এর জায়গায় `@State private var`। মান বদলালেই `body` আবার চলে, আলাদা call লাগে না।

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

**SwiftUI-তে:**

```swift
struct PinButton: View {
    @State private var isPinned = false

    var body: some View {
        Button {
            isPinned.toggle()                         // setState লাগে না
        } label: {
            Image(systemName: isPinned ? "pin.fill" : "pin")
        }
    }
}
```

**View তো struct — প্রতিবার নতুন হয়। তাহলে `isPinned` টিকে থাকে কীভাবে?** `@State`-এর মান struct-এর ভেতরে থাকে না। SwiftUI নিজের graph-এ, এই view-এর identity-র সাথে বেঁধে রাখে। Struct শুধু একটা "হাতল" রাখে। Flutter-এ ঠিক এটাই হয়: Widget নতুন হয়, কিন্তু `State` object Element-এর সাথে বাঁধা থাকে, তাই টিকে থাকে। Compose-এ এই কাজটা `remember` করে।

| | Flutter | SwiftUI | Compose |
|---|---|---|---|
| Local state | `State`-এর field | `@State private var` | `remember { mutableStateOf() }` |
| বদলানো | `setState(() => x = y)` | `x = y` | `x = y` |
| কোথায় বাঁচে | Element-এর সাথে বাঁধা `State` object | SwiftUI-র graph, view identity-র সাথে | composition-এ `remember` slot |
| কে আবার চলে | `setState` যার, তার `build()` | যে `body` মানটা পড়েছে | যে composable পড়েছে |

**Best approach:** `@State` সবসময় `private`। এটা এই view-এর নিজের state — বাইরে থেকে দেওয়ার জিনিস না। বাইরের মান লাগলে `let` property, আর বদলাতে হলে `@Binding` ([iOS ৫.৬](#ios5-6))।

**ফাঁদ — `body`-তে side effect।** `body` যেকোনো সময়, যতবার খুশি চলতে পারে। Network call, analytics, বা `@State` বদলানো সরাসরি `body`-তে লিখবেন না। Flutter-এ `build()`-এ API call না করার নিয়মটাই। কাজ শুরু করার জায়গা `.task` আর `.onAppear` ([iOS ৫.৯](#ios5-9))।

[উপরে ফিরুন](#toc)

### <a id="ios5-6"></a>iOS ৫.৬ `@Binding` — lifting state up

**এক লাইনে:** Flutter-এ child-কে value আর `onChanged` callback দিতেন। SwiftUI-তে দুটো মিলিয়ে একটা জিনিস: **`Binding`** — "এই মান পড়ো, আর বদলাতে চাইলে এখানে লেখো"। `$` চিহ্ন দিয়ে বানানো হয়।

**Flutter-এ:**

```dart
class TitleField extends StatelessWidget {
  const TitleField({super.key, required this.value, required this.onChanged});
  final String value;
  final ValueChanged<String> onChanged;

  @override
  Widget build(BuildContext context) =>
      TextFormField(initialValue: value, onChanged: onChanged);
}
```

**SwiftUI-তে:**

```swift
struct TitleField: View {
    @Binding var title: String                       // মালিক না, শুধু হাতল

    var body: some View {
        TextField("শিরোনাম", text: $title)            // TextField-কে binding দিলাম
            .font(.title2)
    }
}

struct NewNoteView: View {
    @State private var title = ""                     // মালিক এখানে

    var body: some View {
        Form {
            TitleField(title: $title)                 // $ = binding পাঠাও
            Text("\(title.count) অক্ষর")              // একই মান, সাথে সাথে আপডেট
        }
    }
}
```

- `title` লিখলে মান, `$title` লিখলে binding।
- `TextField`-এর জন্য `TextEditingController` লাগে না। Binding দিলেই দুই দিকে চলে — user লিখলে মান বদলায়, কোড মান বদলালে field বদলায়।
- Preview বা test-এ binding বানাতে: `.constant("বাজার")`।

| Flutter | SwiftUI | Compose |
|---|---|---|
| `value` + `onChanged` | `@Binding var value` | `value` + `onValueChange` |
| `TextEditingController` | `TextField(text: $title)` | `TextField(value, onValueChange)` |
| parent-এ state | parent-এ `@State` | parent-এ `remember` |

**ফাঁদ:** `@Binding` আর `@State` গুলিয়ে ফেলা। Child-এ `@State var title` লিখে parent থেকে মান দিলে, প্রথম মানটাই থাকবে — parent পরে বদলালেও child-এ আসবে না। কারণ `@State` একবারই initial value নেয়, Flutter-এ `initState`-এ `widget.value` কপি করে রাখার মতো। মালিক না হলে `@Binding` বা `let`।

[উপরে ফিরুন](#toc)

### <a id="ios5-7"></a>iOS ৫.৭ `ChangeNotifier` / Cubit → `@Observable`

**এক লাইনে:** Screen-এর state আর logic রাখার class-এ `@Observable` লিখুন (iOS 17+)। View যে property পড়ে, শুধু সেটা বদলালে view আবার আঁকা হয় — `notifyListeners()` বা `emit` লাগে না।

**Flutter-এ (Cubit):**

```dart
class NotesCubit extends Cubit<NotesState> {
  NotesCubit(this._repo) : super(const NotesState.loading());
  final NotesRepository _repo;

  Future<void> load() async {
    emit(const NotesState.loading());
    try {
      emit(NotesState.loaded(await _repo.allNotes()));
    } catch (e) {
      emit(NotesState.error(e.toString()));
    }
  }
}

// UI
BlocProvider(create: (_) => NotesCubit(repo)..load(), child: const NotesScreen());
BlocBuilder<NotesCubit, NotesState>(builder: (context, state) => ...);
```

**SwiftUI-তে:**

```swift
@MainActor
@Observable
final class NotesListModel {
    enum Phase { case loading, loaded([Note]), failed(String) }

    private(set) var phase: Phase = .loading
    var searchText = ""

    private let repository: any NotesRepository

    init(repository: any NotesRepository) {
        self.repository = repository
    }

    func load() async {
        phase = .loading
        do {
            phase = .loaded(try await repository.allNotes())
        } catch {
            phase = .failed(error.localizedDescription)
        }
    }
}

struct NotesListView: View {
    @State private var model: NotesListModel          // মালিক: @State

    init(repository: any NotesRepository) {
        _model = State(initialValue: NotesListModel(repository: repository))
    }

    var body: some View {
        content
            .searchable(text: $model.searchText)       // @State-এর ভেতরের @Observable-এ $ চলে
            .task { await model.load() }               // BlocProvider-এর ..load()
    }

    @ViewBuilder
    private var content: some View {
        switch model.phase {                           // BlocBuilder-এর কাজ
        case .loading:
            ProgressView()
        case .loaded(let notes):
            List(notes) { NoteRow(note: $0) }
        case .failed(let message):
            ContentUnavailableView("ভুল হয়েছে", systemImage: "exclamationmark.triangle", description: Text(message))
        }
    }
}
```

**Model কাকে কীভাবে দেবেন — তিনটা নিয়ম:**

| অবস্থা | লিখবেন | Flutter-এ |
|---|---|---|
| এই view model-এর মালিক (বানায়, বাঁচিয়ে রাখে) | `@State private var model = ...` | `BlocProvider(create:)` |
| শুধু পড়বে | `let model: NotesListModel` বা `var model` | `context.watch` / `BlocBuilder` |
| পড়বে আর property-তে binding লাগবে (`TextField`) | `@Bindable var model: NoteEditorModel` | — |
| দূরের অনেক view-কে দেবেন | `.environment(model)` + `@Environment(NotesListModel.self)` ([iOS ৫.৮](#ios5-8)) | `BlocProvider` + `context.read` |

**ভেতরে কীভাবে কাজ করে:** `@Observable` একটা macro। এটা প্রতিটা property-র getter আর setter-এ পাহারা বসায়। `body` চলার সময় SwiftUI দেখে নেয়, ঠিক কোন কোন property পড়া হলো। পরে শুধু সেগুলো বদলালেই এই view-এর `body` আবার চলে। `searchText` বদলালে যে view শুধু `phase` পড়ে, সে আবার চলে না।

এটা `ChangeNotifier`-এর চেয়ে সূক্ষ্ম। `notifyListeners()` সব listener-কে জাগায়। BLoC-এ `buildWhen` বা `select` দিয়ে হাতে বাছতে হয়। `@Observable` এটা নিজে করে, property ধরে।

**পুরনো পথ (চিনে রাখুন, iOS 13–16):**

```swift
final class OldNotesViewModel: ObservableObject {
    @Published var notes: [Note] = []                 // বদলালে পুরো object "বদলেছে" বলে
}

@StateObject private var vm = OldNotesViewModel()    // মালিক
@ObservedObject var vm: OldNotesViewModel             // শুধু দেখে
@EnvironmentObject var vm: OldNotesViewModel          // environment থেকে
```

`ObservableObject`-এ যেকোনো `@Published` বদলালে object-টা দেখা সব view আবার চলত — `ChangeNotifier`-এর মতো মোটা দাগে। Interview-এ "`@StateObject` আর `@ObservedObject`-এর পার্থক্য" প্রায়ই আসে: প্রথমটা মালিক (একবার বানায়, বাঁচিয়ে রাখে), দ্বিতীয়টা শুধু দেখে (parent rebuild করলে নতুন object পেতে পারে)।

**Best approach (iOS 17+):** Screen-প্রতি একটা `@MainActor @Observable final class`। View-এর `@State`-এ মালিকানা। Repository init-এ দেওয়া, যাতে test-এ fake দেওয়া যায়। Architecture-এর পুরো গল্প পরের অধ্যায়গুলোতে।

**ফাঁদ — `@State`-এর initial value বারবার তৈরি হয়।** `@State private var model = NotesListModel(...)` লিখলে, parent যতবার এই view-এর struct বানায়, ততবার `NotesListModel(...)` call হয়। SwiftUI প্রথমটা রাখে, বাকিগুলো ফেলে দেয় — কিন্তু init-এর খরচ আর side effect প্রতিবার হয়। তাই model-এর `init`-এ network call বা ভারী কাজ রাখবেন না। Load করুন `.task`-এ, ওপরের মতো।

[উপরে ফিরুন](#toc)

### <a id="ios5-8"></a>iOS ৫.৮ `InheritedWidget` / Provider → `@Environment`

**এক লাইনে:** Tree-র ওপর থেকে নিচের সব view-এ কিছু পৌঁছাতে `.environment(...)` দিন, আর নিচে `@Environment` দিয়ে পড়ুন। `Theme.of(context)` আর `Provider.of(context)`-এর কাজ।

**System-এর জিনিস পড়া:**

```swift
struct NoteDetailView: View {
    @Environment(\.dismiss) private var dismiss              // Navigator.pop-এর কাজ
    @Environment(\.colorScheme) private var colorScheme      // dark mode কি না
    @Environment(\.dynamicTypeSize) private var textSize     // user-এর font size

    var body: some View {
        Button("বন্ধ") { dismiss() }
    }
}
```

**নিজের `@Observable` object পাঠানো:**

```swift
// ওপরে
NotesListView()
    .environment(store)                                     // type দিয়ে চেনা হয়

// অনেক নিচে
struct SyncBadge: View {
    @Environment(NotesStore.self) private var store

    var body: some View {
        Text(store.isSyncing ? "Sync হচ্ছে" : "সব ঠিক")
    }
}
```

**নিজের সাধারণ মান — `@Entry` (Xcode 16+):**

```swift
extension EnvironmentValues {
    @Entry var noteFontSize: Double = 17                    // default মান
}

NotesListView()
    .environment(\.noteFontSize, 20)

struct NoteBody: View {
    @Environment(\.noteFontSize) private var fontSize
    let text: String
    var body: some View { Text(text).font(.system(size: fontSize)) }
}
```

| Flutter | SwiftUI | Compose |
|---|---|---|
| `InheritedWidget` | `EnvironmentValues` + `@Entry` | `CompositionLocal` |
| `Provider` / `BlocProvider` | `.environment(object)` | `CompositionLocalProvider` |
| `context.watch<T>()` | `@Environment(T.self)` | `LocalX.current` |
| `Theme.of(context)` | `@Environment(\.colorScheme)`, `.font`, `.tint` | `MaterialTheme` |
| `Navigator.of(context).pop()` | `@Environment(\.dismiss)` | `navController.popBackStack()` |
| `MediaQuery.of(context)` | `@Environment(\.horizontalSizeClass)`, `GeometryReader` | `LocalConfiguration` |

**ফাঁদ — object না দিলে crash।** `@Environment(NotesStore.self)` পড়লেন, কিন্তু ওপরে কেউ `.environment(store)` দেয়নি — app crash করে। Flutter-এ `ProviderNotFoundException`-এর মতো, কিন্তু runtime-এ সোজা crash। Preview-তেও object দিতে ভুলবেন না।

**Best approach:** App-জোড়া জিনিস (store, setting) environment-এ। Screen-এর নিজের model init-এ সরাসরি দিন — কোন view কী চায়, পরিষ্কার থাকে।

[উপরে ফিরুন](#toc)

### <a id="ios5-9"></a>iOS ৫.৯ `initState`, `dispose`, `StreamBuilder` → `.task`, `.onAppear`, `.onChange`

**এক লাইনে:** Screen খুললে async কাজ শুরু — `.task { }`। Screen চলে গেলে সেটা **নিজেই cancel** হয়। কোনো মান বদলালে কাজ — `.onChange(of:)`। Id বদলালে কাজ আবার শুরু — `.task(id:)`।

**Flutter-এ:**

```dart
class _NoteDetailState extends State<NoteDetail> {
  StreamSubscription<Note>? _sub;

  @override
  void initState() {
    super.initState();
    _sub = repo.watchNote(widget.noteId).listen((n) => setState(() => note = n));
  }

  @override
  void didUpdateWidget(NoteDetail old) {
    super.didUpdateWidget(old);
    if (old.noteId != widget.noteId) {             // অন্য note খুলল
      _sub?.cancel();
      _sub = repo.watchNote(widget.noteId).listen((n) => setState(() => note = n));
    }
  }

  @override
  void dispose() {
    _sub?.cancel();
    super.dispose();
  }
}
```

**SwiftUI-তে — একই কাজ, একটা modifier:**

```swift
struct NoteDetailView: View {
    let noteID: UUID
    let repository: any NotesRepository
    @State private var note: Note?

    var body: some View {
        Group {
            if let note {
                Text(note.body)
            } else {
                ProgressView()
            }
        }
        .task(id: noteID) {                              // initState + didUpdateWidget + dispose
            for await latest in repository.watchNote(id: noteID) {
                note = latest
            }
        }
    }
}
```

- View দেখা দেওয়ার আগে `.task` শুরু হয়।
- View চলে গেলে task cancel — `for await` loop থামে। `dispose`-এ `cancel()` লিখতে হয় না।
- `noteID` বদলালে পুরনো task cancel হয়ে নতুনটা শুরু — `didUpdateWidget`-এর কাজ।

(`watchNote(id:)` ধরে নিচ্ছি repository-র একটা function, যেটা `AsyncStream<Note>` দেয় — [iOS ২.৮](#ios2-8)।)

| Flutter | SwiftUI | Compose |
|---|---|---|
| `initState` (async কাজ) | `.task { }` | `LaunchedEffect(Unit)` |
| `initState` (sync কাজ) | `.onAppear { }` | `LaunchedEffect` / `SideEffect` |
| `dispose` | `.task` নিজে cancel; `.onDisappear { }` | `DisposableEffect { onDispose { } }` |
| `didUpdateWidget` | `.task(id:)`, `.onChange(of:)` | `LaunchedEffect(key)` |
| `StreamBuilder` | `.task { for await ... }` + `@State` | `collectAsStateWithLifecycle()` |
| `FutureBuilder` | `.task { value = await ... }` + `@State` | `LaunchedEffect` + state |

**`.onChange` (iOS 17 রূপ):**

```swift
.onChange(of: model.searchText) { oldValue, newValue in
    analytics.log("search", newValue)
}
```

**`.onAppear` বনাম `.task`:** `.onAppear` sync, আর cancel হয় না। সেখান থেকে `Task { }` চালালে screen চলে গেলেও চলতে থাকবে। Async কাজ সবসময় `.task`-এ।

**ফাঁদ — `.onAppear` একাধিকবার চলে।** Navigation-এ পেছনে গিয়ে ফিরলে, tab বদলালে, আবার চলে। Flutter-এর `initState` একবারই চলত। "প্রথমবার শুধু" কাজ হলে model-এ একটা flag রাখুন, বা `.task`-এর ভেতরে check করুন।

[উপরে ফিরুন](#toc)

### <a id="ios5-10"></a>iOS ৫.১০ View identity — Flutter-এর `Key`

**এক লাইনে:** SwiftUI কোন view "একই" ধরে, সেটার নাম **identity**। Identity একই থাকলে `@State` টিকে থাকে আর বদল animate হয়। Identity বদলালে পুরনো view মরে, নতুন জন্মায় — state শূন্য থেকে।

দুই রকম identity:
- **Structural** — tree-তে view-এর জায়গা দিয়ে। `if`-এর এক শাখা আর `else`-এর শাখা দুইটা আলাদা জায়গা।
- **Explicit** — আপনি দেন: `ForEach`-এর id, আর `.id(...)` modifier।

**Flutter-এ মিল:** Element reuse হয় যদি একই জায়গায় একই `runtimeType` আর একই `Key` থাকে। Key বদলালে State নতুন। SwiftUI-র ধারণা হুবহু এটাই।

**ফাঁদ ১ — `if/else` দিয়ে শুধু চেহারা বদলানো:**

```swift
// খারাপ: দুইটা আলাদা view — state হারায়, animation হয় fade, move না
if note.isPinned {
    NoteRow(note: note).background(.yellow)
} else {
    NoteRow(note: note)
}

// ভালো: একই view, শুধু মান বদলায়
NoteRow(note: note)
    .background(note.isPinned ? Color.yellow : Color.clear)
```

**ফাঁদ ২ — অন্য note খুললে পুরনো state থেকে যায়:**

```swift
NoteEditorView(note: selectedNote)
    .id(selectedNote.id)          // note বদলালে editor নতুন করে জন্মায়, পুরনো draft থাকে না
```

Flutter-এ `NoteEditor(key: ValueKey(note.id))` দিয়ে ঠিক এই কাজ করতেন।

**ফাঁদ ৩ — ForEach-এ অস্থির id।** `id: \.self` (পুরো value দিয়ে) — note-এর title বদলালেই id বদলায়, row নতুন জন্মায়। Array index — মাঝে একটা মুছলে সবার id সরে যায়। সবসময় database-এর স্থির id।

[উপরে ফিরুন](#toc)

### <a id="ios5-11"></a>iOS ৫.১১ Animation

**এক লাইনে:** State বদলের সাথে `withAnimation { }` লিখলে, সেই বদলের ফলে যা যা বদলায়, সব animate হয়। Controller, ticker, `vsync` — কিছু লাগে না।

**Flutter-এ:**

```dart
AnimatedContainer(
  duration: const Duration(milliseconds: 300),
  color: isPinned ? Colors.yellow : Colors.white,
  child: NoteRow(note: note),
)
```

**SwiftUI-তে — তিন পথ:**

```swift
// ১. Explicit: এই বদলের সব প্রভাব animate করো
Button("পিন") {
    withAnimation(.spring) {
        note.isPinned.toggle()
    }
}

// ২. Implicit: এই view-এ এই মান বদলালেই animate করো
NoteRow(note: note)
    .background(note.isPinned ? Color.yellow : Color.white)
    .animation(.easeInOut(duration: 0.3), value: note.isPinned)

// ৩. Transition: view আসা-যাওয়ার animation
if showUndoBanner {
    UndoBanner()
        .transition(.move(edge: .bottom).combined(with: .opacity))
}
```

| Flutter | SwiftUI | Compose |
|---|---|---|
| `AnimatedContainer`, `AnimatedOpacity` | `.animation(_:value:)` | `animate*AsState` |
| `AnimationController` + `setState` | `withAnimation { state = ... }` | `Animatable` |
| `AnimatedSwitcher` | `if` + `.transition()` | `AnimatedContent` |
| `AnimatedList` | `List`/`ForEach`-এ `withAnimation`-এ insert/delete | `Modifier.animateItem()` |
| `Hero` | `matchedGeometryEffect`, `.navigationTransition(.zoom)` (iOS 18) | `SharedTransitionLayout` |
| `Curves.easeInOut` | `.easeInOut`, `.spring`, `.bouncy` | `tween`, `spring` |

**ভেতরে কীভাবে কাজ করে:** `withAnimation`-এর ভেতরে state বদলালে SwiftUI পুরনো আর নতুন UI-র পার্থক্য বের করে। Position, রং, opacity — যা animate করা যায়, সেগুলো মাঝের মান দিয়ে ধাপে ধাপে আঁকে। এজন্যই identity জরুরি ([iOS ৫.১০](#ios5-10)): identity একই থাকলে "move", বদলালে "এক জন গেল, আরেকজন এল" — fade।

**ফাঁদ:** `.animation(.default)` value ছাড়া লেখা — পুরনো API, deprecated। Parent-এর যেকোনো বদলে animate হয়ে অদ্ভুত লাফালাফি। সবসময় `value:` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios5-12"></a>iOS ৫.১২ Hot reload নেই: Preview

**এক লাইনে:** SwiftUI-তে Flutter-এর hot reload নেই। তার জায়গায় Xcode-এর **Preview** — code-এর পাশে view চলমান দেখায়, প্রতিটা বদলের সাথে নতুন।

```swift
#Preview("Pinned note") {
    NoteRow(note: Note(id: UUID(), title: "বাজার", body: "ডিম, দুধ, রুটি", isPinned: true, updatedAt: .now))
        .padding()
}

#Preview("Dark, বড় লেখা") {
    NotesListView(repository: FakeNotesRepository())
        .preferredColorScheme(.dark)
        .dynamicTypeSize(.xxxLarge)
}

#Preview("Editable") {
    @Previewable @State var title = "বাজার"           // Preview-এর ভেতরে state (Xcode 16+)
    TitleField(title: $title)
}
```

- এক file-এ যতগুলো `#Preview` খুশি — light/dark, ছোট/বড় font, empty/error অবস্থা।
- Preview-তে tap, scroll চলে।
- Fake repository দিন। Preview-তে আসল network নয়।

| Flutter | SwiftUI | Compose |
|---|---|---|
| Hot reload (চলমান app-এ) | Preview (আলাদা জায়গায়) | `@Preview` (+ Live Edit) |
| Widgetbook / golden test | একাধিক `#Preview` | একাধিক `@Preview` |

**বাস্তব কথা:** Preview খুব কাজের, কিন্তু বড় project-এ মাঝে মাঝে ধীর হয় বা ভেঙে যায়। কারণ প্রায়ই environment-এ object না দেওয়া, বা আসল database ছোঁয়া। View-কে ছোট রাখুন আর dependency init-এ নিন — তাহলে Preview স্থির থাকে।

[উপরে ফিরুন](#toc)

### <a id="ios5-13"></a>iOS ৫.১৩ UIKit চিনে রাখুন — `UIViewController` আর Auto Layout

SwiftUI-র আগে iOS-এর UI ছিল **UIKit** — Android-এর পুরনো View system-এর মতো, imperative। আজও অনেক app-এর বড় অংশ UIKit-এ, প্রায় সব Flutter plugin-এর UI অংশও। আর সবচেয়ে জরুরি কথা: **`FlutterViewController` নিজেই একটা `UIViewController`।** তাই UIKit না চিনলে Flutter-এর iOS দিক পুরো বোঝা যায় না।

**`UIViewController` — একটা screen, Android-এর Activity/Fragment-এর মতো:**

```swift
final class NotesViewController: UIViewController {
    private let tableView = UITableView()

    override func viewDidLoad() {                 // একবার — view তৈরি হলো (initState)
        super.viewDidLoad()
        title = "Notes"
        view.addSubview(tableView)
        tableView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([             // Auto Layout: top safe area-র সাথে, বাকি তিন কিনারা view-এর সাথে বাঁধা
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
        ])
    }

    override func viewWillAppear(_ animated: Bool) {   // প্রতিবার দেখা দেওয়ার আগে
        super.viewWillAppear(animated)
        reloadNotes()
    }
}
```

**Lifecycle-এর ক্রম:**

```
init → loadView → viewDidLoad (একবার)
      → viewWillAppear → viewIsAppearing → viewWillLayoutSubviews → viewDidLayoutSubviews → viewDidAppear
      → viewWillDisappear → viewDidDisappear
      → deinit
```

- `viewDidLoad` — একবার। Flutter-এর `initState`।
- `viewWillAppear` / `viewDidAppear` — প্রতিবার দেখা দিলে (পেছন থেকে ফিরলেও)। Navigation-এ ফিরে এলে আবার চলে।
- `viewIsAppearing` (iOS 17-এ এসেছে, Xcode 15 দিয়ে iOS 13 পর্যন্ত চলে) — size আর trait জানা, কিন্তু এখনো screen-এ দেখা যায়নি। Layout-নির্ভর কাজের সঠিক জায়গা।
- Rotation-এ কিছু মরে না — শুধু `viewWillTransition(to:with:)` আর আবার layout।

**Auto Layout এক নজরে:** View-এর জায়গা সরাসরি না দিয়ে **constraint** দেন — "এর top ওর bottom থেকে ৮ point নিচে"। System সব constraint মিলিয়ে সমীকরণ সমাধান করে frame বের করে। Constraint কম হলে view কোথায় বসবে বোঝা যায় না, বেশি বা পরস্পরবিরোধী হলে console-এ "Unable to simultaneously satisfy constraints"। Flutter-এর constraint-based layout-এর থেকে আলাদা — ওখানে parent একমুখী constraint দেয়, এখানে সবাই মিলে সমীকরণ।

**দুই জগৎ জোড়া দেওয়া — plugin লেখকের জন্য জরুরি:**

| কাজ | পথ |
|---|---|
| UIKit-এর ভেতরে SwiftUI | `UIHostingController(rootView: NoteRow(note: note))` — এটা একটা `UIViewController` |
| SwiftUI-র ভেতরে UIKit view | `UIViewRepresentable` (view), `UIViewControllerRepresentable` (controller) |
| Flutter-এর ভেতরে native view | `FlutterPlatformView` — একটা `UIView` ফেরত দেয়। SwiftUI দেখাতে চাইলে `UIHostingController`-এর `view` দিন |
| Native screen-এর ওপর Flutter | `FlutterViewController` present বা push করুন (add-to-app) |

| UIKit | SwiftUI | Flutter |
|---|---|---|
| `UIViewController` | `View` (screen-এর) | Route-এর screen widget |
| `UIView` | `View` | `Widget` / `RenderObject` |
| `UILabel`, `UIButton`, `UITextField` | `Text`, `Button`, `TextField` | `Text`, `TextButton`, `TextField` |
| `UITableView` + data source + cell reuse | `List` | `ListView.builder` |
| `UINavigationController` | `NavigationStack` | `Navigator` |
| Storyboard / XIB | (নেই) | (নেই) |
| Auto Layout constraint | Stack + frame + `Spacer` | `Row`, `Column`, `Expanded` |

> **মনে রাখুন**
> - Widget → `struct ...: View` + `body`। Wrapper widget → modifier, আর modifier ভেতর থেকে বাইরে পড়ুন।
> - `@State` (নিজের, `private`) → `@Binding` (`$` দিয়ে, অন্যের) → `@Observable` (screen model, iOS 17+) → `@Environment` (দূরের সবাই)।
> - Async কাজ `.task`-এ — screen চলে গেলে নিজে cancel। `.task(id:)` = `didUpdateWidget`।
> - Identity = Flutter-এর `Key`। `if/else`-এ চেহারা না, মান বদলান; `.id()` দিয়ে state reset।
> - `FlutterViewController` একটা `UIViewController` — UIKit-এর lifecycle আর Auto Layout চিনে রাখুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "SwiftUI-তে view একটা হালকা struct, Flutter-এর widget-এর মতো। State থাকে SwiftUI-র নিজের graph-এ, view-এর identity-র সাথে বাঁধা — Flutter-এ Element-এর সাথে State যেভাবে বাঁধা। আমি local state-এ `@State`, child-কে `@Binding`, আর screen-এর logic `@Observable` model-এ রাখি। `@Observable` property ধরে track করে, তাই শুধু যে view যে property পড়েছে, সেটাই আবার আঁকা হয়। Async কাজ `.task`-এ চালাই, যাতে view চলে গেলে নিজে cancel হয়।"
> - *English:* "In SwiftUI a view is a lightweight struct, like a Flutter widget. State lives in SwiftUI's own graph, tied to the view's identity — the way Flutter ties State to the Element. I use `@State` for local state, `@Binding` for children, and keep screen logic in an `@Observable` model. Observation tracks per property, so only views that read a changed property redraw. I start async work in `.task`, so it cancels itself when the view goes away."

[উপরে ফিরুন](#toc)

---

## <a id="ios6"></a>iOS ৬. Navigation — `go_router`-এর জায়গায় `NavigationStack`

পুরনো iOS-এ নতুন screen মানে `navigationController?.pushViewController(...)`। Data পাঠাতে property set করা, ফল আনতে delegate। SwiftUI-র প্রথম দিকের `NavigationView` আর `NavigationLink(destination:)` code থেকে navigation বের করে আনা কঠিন করত।

iOS 16 থেকে **`NavigationStack`** এসে ছবিটা বদলে দিয়েছে। Back stack এখন একটা সাধারণ array, যেটা আপনি নিজে রাখেন। Flutter-এর Navigator 2.0-এর `pages` list, বা Android-এর Navigation 3-এর back stack-এর ([অধ্যায় ৭](#ch7)) ধারণা।

### <a id="ios6-1"></a>iOS ৬.১ `NavigationStack` আর path

**এক লাইনে:** Route-গুলো একটা `enum`। Back stack হলো `[Route]` array। Push মানে `append`, pop মানে `removeLast`। কোন route-এ কোন screen, সেটা `.navigationDestination(for:)`-এ।

**Flutter-এ (go_router):**

```dart
final router = GoRouter(routes: [
  GoRoute(
    path: '/',
    builder: (_, __) => const NotesListScreen(),
    routes: [
      GoRoute(path: 'note/:id', builder: (_, s) => NoteScreen(noteId: s.pathParameters['id']!)),
      GoRoute(path: 'new', builder: (_, __) => const NewNoteScreen()),
    ],
  ),
]);

context.push('/note/42');
context.pop();
context.go('/');
```

**SwiftUI-তে:**

```swift
enum Route: Hashable, Codable {
    case note(id: UUID)
    case newNote
    case settings
}

@MainActor
@Observable
final class Router {
    var path: [Route] = []

    func push(_ route: Route) { path.append(route) }
    func pop() { _ = path.popLast() }
    func popToRoot() { path.removeAll() }
}

struct RootView: View {
    @State private var router = Router()
    let repository: any NotesRepository

    var body: some View {
        NavigationStack(path: $router.path) {
            NotesListView(repository: repository)
                .navigationTitle("Notes")
                .navigationDestination(for: Route.self) { route in
                    switch route {                                  // GoRoute-এর builder
                    case .note(let id):
                        NoteDetailView(noteID: id, repository: repository)
                    case .newNote:
                        NewNoteView()
                    case .settings:
                        SettingsView()
                    }
                }
        }
        .environment(router)
    }
}
```

**List থেকে push — দুই পথ:**

```swift
// ১. NavigationLink(value:) — tap করলে path-এ value যোগ হয়
List(notes) { note in
    NavigationLink(value: Route.note(id: note.id)) {
        NoteRow(note: note)
    }
}

// ২. Code থেকে — save শেষে, deep link-এ
router.push(.note(id: savedNote.id))
```

| go_router | SwiftUI | Navigation Compose |
|---|---|---|
| `GoRouter(routes: [...])` | `NavigationStack(path:)` + `.navigationDestination(for:)` | `NavHost { composable<Route> { } }` |
| `'/note/:id'` path | `enum Route { case note(id: UUID) }` — type-safe | `@Serializable data class NoteDetail(val id: String)` |
| `state.pathParameters['id']!` | `case .note(let id)` | `entry.toRoute<NoteDetail>()` |
| `context.push('/note/42')` | `path.append(.note(id:))` | `navController.navigate(NoteDetail(id))` |
| `context.pop()` | `path.removeLast()` বা `@Environment(\.dismiss)` | `popBackStack()` |
| `context.go('/')` | `path.removeAll()` | `popBackStack(startDestination, false)` |
| `redirect` (login) | root-এ `if isLoggedIn { ... } else { LoginView() }` | start destination বদলানো |
| `PopScope` | `.navigationBarBackButtonHidden()` + নিজের button | `BackHandler { }` |
| AppBar title | `.navigationTitle("Notes")` | `TopAppBar(title = ...)` |
| AppBar actions | `.toolbar { ToolbarItem { ... } }` | `TopAppBar(actions = ...)` |

**কী আলাদা:**
- **Back stack আপনার হাতে, একটা array।** `path`-এ যা আছে, screen-এ ঠিক তাই। Test-এ শুধু `router.path` check করলেই হয়।
- **System back button নেই।** Navigation bar-এর বাম দিকে "‹ Notes" back button, আর বাম কিনারা থেকে swipe — দুটোই `NavigationStack` নিজে দেয়, আর pop হলে `path` নিজে ছোট হয়।
- **একাধিক type-এর route চাইলে `NavigationPath`।** এটা type-erased path — ভেতরে `Route`, `Folder`, যা খুশি রাখা যায়। এক enum-এ সব route রাখলে সাধারণ array-ই সহজ।

**Best approach:**
- এক enum-এ সব route, `Hashable` আর `Codable`। Route-এ শুধু id, পুরো `Note` না — go_router আর Android-এর একই নিয়ম। Screen id নিয়ে repository থেকে load করে।
- Screen-কে `Router` না দিয়ে callback দিন (`onOpenNote: (UUID) -> Void`)। Navigation এক জায়গায় থাকে, screen Preview আর test করা সহজ হয়। ছোট app-এ environment থেকে `Router` পড়াও চলে।
- **Restoration বিনা খরচে:** `Route` `Codable` হলে পুরো `path` encode করে `@SceneStorage`-এ রাখা যায়। System app মেরে ফেললেও user ঠিক একই screen-এ ফেরে ([iOS ৪.৫](#ios4-5))।

**ফাঁদ:** `.navigationDestination(for:)` lazy container-এর (`List`, `LazyVStack`) ভেতরের row-এ লাগানো। Row তৈরি না হলে destination-ও নিবন্ধিত হয় না, আর push কাজ করে না (Xcode console-এ সতর্কবার্তা আসে)। Stack-এর root view-এ লাগান, ওপরের মতো।

[উপরে ফিরুন](#toc)

### <a id="ios6-2"></a>iOS ৬.২ Sheet, full-screen cover আর alert

**এক লাইনে:** নিচ থেকে ওঠা screen — `.sheet`। পুরো screen ঢেকে — `.fullScreenCover`। ছোট প্রশ্ন — `.alert`, `.confirmationDialog`। সবই একটা state দিয়ে চলে: state থাকলে দেখায়, `nil` বা `false` হলে বন্ধ।

**Flutter-এ:**

```dart
final saved = await showModalBottomSheet<bool>(
  context: context,
  builder: (_) => const NewNoteSheet(),
);

showDialog(
  context: context,
  builder: (_) => AlertDialog(title: const Text('মুছবেন?'), actions: [...]),
);
```

**SwiftUI-তে:**

```swift
struct NotesListScreen: View {
    @State private var isComposing = false
    @State private var editingNote: Note?           // Note: Identifiable
    @State private var noteToDelete: Note?

    var body: some View {
        NotesList(onEdit: { editingNote = $0 }, onDelete: { noteToDelete = $0 })
            .toolbar {
                Button("নতুন", systemImage: "square.and.pencil") { isComposing = true }
            }
            .sheet(isPresented: $isComposing) {      // bool দিয়ে
                NewNoteView()
                    .presentationDetents([.medium, .large])   // আধা বা পুরো উচ্চতা
            }
            .sheet(item: $editingNote) { note in     // item দিয়ে — কোন note, সেটাও আসে
                NoteEditorScreen(note: note)
            }
            .confirmationDialog(
                "Note মুছবেন?",
                isPresented: Binding(get: { noteToDelete != nil }, set: { if !$0 { noteToDelete = nil } }),
                presenting: noteToDelete
            ) { note in
                Button("মুছুন", role: .destructive) { delete(note) }
            }
    }
}
```

Sheet-এর ভেতর থেকে বন্ধ করতে:

```swift
struct NewNoteView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var text = ""

    var body: some View {
        NavigationStack {                            // sheet-এর নিজের navigation bar
            TextEditor(text: $text)
                .toolbar {
                    ToolbarItem(placement: .cancellationAction) { Button("বাতিল") { dismiss() } }
                    ToolbarItem(placement: .confirmationAction) { Button("সেভ") { save(); dismiss() } }
                }
        }
        .interactiveDismissDisabled(!text.isEmpty)   // লেখা থাকলে টেনে বন্ধ করা যাবে না
    }
}
```

| Flutter | SwiftUI | Compose |
|---|---|---|
| `showModalBottomSheet` | `.sheet` + `.presentationDetents` | `ModalBottomSheet` |
| `Navigator.push(fullscreenDialog: true)` | `.fullScreenCover` | নতুন destination |
| `showDialog(AlertDialog)` | `.alert` | `AlertDialog` |
| action sheet (`showCupertinoModalPopup`) | `.confirmationDialog` | `ModalBottomSheet` / menu |
| `Navigator.pop(context, result)` | `dismiss()` + callback বা binding দিয়ে ফল | callback |
| `await showDialog<T>()` থেকে ফল | নেই — callback বা state দিয়ে | callback |
| `PopScope(canPop: false)` | `.interactiveDismissDisabled()` | `BackHandler` |

**কী আলাদা:** Flutter-এ `showDialog` একটা function — call করে `await` করেন, ফল ফেরত আসে। SwiftUI-তে sheet একটা state-এর প্রতিফলন। ফল আসে callback বা binding দিয়ে। শুরুতে অস্বস্তি লাগে, কিন্তু সুবিধা হলো: "sheet খোলা কি না" এখন সাধারণ state, test আর restore করা যায়।

**ফাঁদ:** একই view-এ একাধিক `.sheet(isPresented:)` আর দুইটা bool একসাথে `true` — একটা দেখাবে, আরেকটা নিঃশব্দে হারাবে। এক জায়গায় অনেক রকম sheet থাকলে একটা enum দিন: `@State private var sheet: SheetKind?` আর একটাই `.sheet(item: $sheet)`।

[উপরে ফিরুন](#toc)

### <a id="ios6-3"></a>iOS ৬.৩ Tab

**এক লাইনে:** নিচের tab bar — `TabView`। iOS 18 থেকে প্রতিটা tab একটা `Tab`। প্রতিটা tab-এর ভেতরে নিজের `NavigationStack`, তাই tab বদলালে প্রতিটার back stack আলাদা থাকে।

**Flutter-এ (go_router):**

```dart
StatefulShellRoute.indexedStack(
  builder: (context, state, shell) => ScaffoldWithNavBar(shell: shell),
  branches: [
    StatefulShellBranch(routes: [GoRoute(path: '/notes', builder: ...)]),
    StatefulShellBranch(routes: [GoRoute(path: '/folders', builder: ...)]),
  ],
);
```

**SwiftUI-তে (iOS 18+):**

```swift
enum AppTab: Hashable { case notes, folders, settings }

struct MainTabView: View {
    @State private var selection: AppTab = .notes
    @State private var notesPath: [Route] = []
    @State private var foldersPath: [Route] = []

    var body: some View {
        TabView(selection: $selection) {
            Tab("Notes", systemImage: "note.text", value: AppTab.notes) {
                NavigationStack(path: $notesPath) { NotesHome() }
            }
            Tab("Folders", systemImage: "folder", value: AppTab.folders) {
                NavigationStack(path: $foldersPath) { FoldersHome() }
            }
            Tab("Settings", systemImage: "gear", value: AppTab.settings) {
                SettingsView()
            }
        }
    }
}
```

**iOS 17 বা আগে (চিনে রাখুন):**

```swift
TabView(selection: $selection) {
    NotesHome()
        .tabItem { Label("Notes", systemImage: "note.text") }
        .tag(AppTab.notes)
}
```

| go_router | SwiftUI | Compose |
|---|---|---|
| `StatefulShellRoute` | `TabView` + প্রতিটা tab-এ `NavigationStack` | `NavigationBar` + nested graph |
| branch-এর আলাদা stack | প্রতিটা tab-এর নিজের `path` | `saveState` / `restoreState` |
| `shell.goBranch(i)` | `selection = .folders` | `navigate(..) { launchSingleTop }` |
| `BottomNavigationBar` | tab bar নিজে আসে | `NavigationBar` |

- Tab বদলালে অন্য tab-এর view আর তার `@State` বেঁচে থাকে — Flutter-এর `IndexedStack`-এর মতো।
- একই tab-এ আবার tap করলে iOS-এর চেনা আচরণ: root-এ ফিরে যাওয়া। আচরণটা নিশ্চিত করতে নিজের `path` রাখুন — `notesPath.removeAll()`।

**ফাঁদ:** পুরো `TabView`-কে একটা `NavigationStack`-এর ভেতরে রাখা। তখন push করলে tab bar-সহ পুরো screen সরে যায়, আর সব tab একটা stack ভাগ করে। উল্টোটা ঠিক — `TabView` বাইরে, প্রতিটা tab-এর ভেতরে `NavigationStack`।

[উপরে ফিরুন](#toc)

### <a id="ios6-4"></a>iOS ৬.৪ Deep link — `onOpenURL`

**এক লাইনে:** বাইরে থেকে আসা URL (`notesapp://note/42` বা `https://notes.byteonyx.com/note/42`) ধরতে `.onOpenURL { url in }`। URL পড়ে `Route` বানান, আর `path`-এ বসান। Navigation যেহেতু শুধু একটা array, deep link মানে শুধু array বদলানো।

**দুই রকম link:**

| | Custom URL scheme | Universal link |
|---|---|---|
| দেখতে | `notesapp://note/42` | `https://notes.byteonyx.com/note/42` |
| ঘোষণা | Info.plist-এ `CFBundleURLTypes` ([iOS ৩.৬](#ios3-6)) | Associated Domains entitlement: `applinks:notes.byteonyx.com` ([iOS ৩.৭](#ios3-7)) |
| Server-এ | কিছু না | `https://notes.byteonyx.com/.well-known/apple-app-site-association` file |
| App না থাকলে | কিছু হয় না / error | Website খোলে |
| নিরাপত্তা | যেকোনো app একই scheme দাবি করতে পারে | Domain-এর মালিক প্রমাণ করে |
| Android-এ | custom scheme intent filter | App Links (`assetlinks.json`) |

**Best:** user-এর হাতে যাওয়া link (email, share) — universal link। App-এর নিজের ভেতরের কাজ (OAuth callback, widget থেকে খোলা) — custom scheme চলে।

**SwiftUI-তে:**

```swift
extension Route {
    init?(url: URL) {
        // notesapp://note/<id>  বা  https://notes.byteonyx.com/note/<id>
        let parts = (url.scheme == "notesapp" ? [url.host() ?? ""] : []) + url.pathComponents.filter { $0 != "/" }
        switch parts.first {
        case "note":
            guard parts.count > 1, let id = UUID(uuidString: parts[1]) else { return nil }
            self = .note(id: id)
        case "new":
            self = .newNote
        default:
            return nil
        }
    }
}

struct RootView: View {
    @State private var router = Router()

    var body: some View {
        NavigationStack(path: $router.path) {
            NotesHome()
                .navigationDestination(for: Route.self) { RouteView(route: $0) }   // ৬.১-এর switch, আলাদা view-এ
        }
        .onOpenURL { url in
            guard let route = Route(url: url) else { return }
            router.path = [route]                      // go_router-এর context.go(...)
        }
    }
}
```

`onOpenURL` custom scheme আর universal link — দুটোই ধরে। App বন্ধ থাকলে URL দিয়ে app চালু হলেও এটা call হয়।

**Flutter-এ এর পেছনে কী ঘটে:**
- Flutter-এর নিজের deep link handler ডিফল্টে চালু। iOS URL দিলে engine সেটা Flutter-এর router-এ (`go_router`) পাঠিয়ে দেয়। নিজের plugin দিয়ে deep link সামলালে Info.plist-এ `FlutterDeepLinkingEnabled` = `false` দিয়ে এটা বন্ধ করতে হয়।
- UIScene-এ যাওয়ার পরে (Flutter 3.41+ ডিফল্ট) URL আসে SceneDelegate-এ। `FlutterSceneDelegate` সেটা engine আর plugin-এ পৌঁছে দেয় ([iOS ৪.১](#ios4-1))। নিজের SceneDelegate-এ `scene(_:openURLContexts:)` override করলে `super` call করতে ভুলবেন না — নইলে Flutter link পাবে না।

| go_router | SwiftUI | Navigation Compose |
|---|---|---|
| Path থেকে নিজে route মেলায় | `onOpenURL` + নিজে URL → `Route` | `navDeepLink { uriPattern = ... }` |
| `context.go(link)` | `router.path = [route]` | `navController.handleDeepLink(intent)` |
| Info.plist / Manifest config | Info.plist + entitlement | Manifest intent filter |

**ফাঁদ:** URL-কে বিশ্বাস করা। যেকোনো app বা website `notesapp://note/...` খুলতে পারে। URL-এর id দিয়ে সরাসরি মুছে ফেলা বা কিছু পাঠানোর মতো কাজ করবেন না। শুধু screen খুলুন, আর কাজের আগে user-কে নিশ্চিত করতে দিন।

**নিজে test করুন:** Simulator-এ terminal থেকে:

```bash
xcrun simctl openurl booted "notesapp://note/6F9619FF-8B86-D011-B42D-00C04FC964FF"
```

Android-এর `adb shell am start -d "..."`-এর কাজ।

[উপরে ফিরুন](#toc)

### <a id="ios6-5"></a>iOS ৬.৫ তিন framework পাশাপাশি, আর best approach

| কাজ | Flutter (go_router) | iOS (SwiftUI) | Android (Compose) |
|---|---|---|---|
| Route-এর সংজ্ঞা | path string | `enum Route: Hashable` | `@Serializable` class |
| Back stack কার হাতে | router-এর | আপনার `[Route]` array | `NavController` (Nav3-এ আপনার list) |
| Push | `push` | `path.append` | `navigate` |
| Pop | `pop` | `removeLast` / `dismiss()` | `popBackStack` |
| Root-এ ফেরা | `go('/')` | `path.removeAll()` | `popBackStack(start, false)` |
| Modal | `showModalBottomSheet` | `.sheet` | `ModalBottomSheet` |
| Tab | `StatefulShellRoute` | `TabView` + `Tab` (iOS 18) | `NavigationBar` + nested graph |
| Deep link | ডিফল্ট handler | `onOpenURL` | `navDeepLink` |
| Back button | — | navigation bar + swipe (system বোতাম নেই) | system back |
| Process মরার পরে stack | সাধারণত হারায় | `Codable` path + `@SceneStorage` | system নিজে ফেরায় |

**Best approach (নভেম্বর ২০২৬):**
- Tab থাকলে `TabView` বাইরে, প্রতিটা tab-এ নিজের `NavigationStack(path:)`।
- সব route এক `Codable` enum-এ, argument-এ শুধু id।
- `Router` একটা `@MainActor @Observable` class। Deep link আর code — দুই দিক থেকে শুধু `path` বদলায়।
- Screen-কে callback দিন। `.navigationDestination` root-এ।
- Sheet-এর জন্য enum-ভিত্তিক `.sheet(item:)`।

> **মনে রাখুন**
> - `NavigationStack(path:)` + `.navigationDestination(for:)`। Back stack একটা সাধারণ `[Route]`।
> - Push = `append`, pop = `removeLast`, root = `removeAll`। Route-এ শুধু id।
> - Sheet আর alert state দিয়ে চলে — `await` করে ফল আসে না, callback দিয়ে আসে।
> - `TabView` বাইরে, প্রতিটা tab-এ নিজের stack।
> - Deep link: `onOpenURL` → `Route` → `path`। User-এর link-এ universal link।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি SwiftUI-তে `NavigationStack`-এ path binding দিয়ে navigation করি। সব route একটা `Hashable`, `Codable` enum, আর back stack একটা array — একটা `@Observable` router-এ রাখা। তাই push, pop, deep link সব শুধু array বদলানো, আর test-এ শুধু array check করি। Route-এ শুধু id পাঠাই, আর path `@SceneStorage`-এ রাখলে system app মারার পরেও user একই screen-এ ফেরে।"
> - *English:* "In SwiftUI I navigate with a `NavigationStack` bound to a path. All routes are one `Hashable`, `Codable` enum, and the back stack is an array kept in an `@Observable` router. So push, pop and deep links are all just array changes, and in tests I only check the array. I pass only ids in routes, and by saving the path in `@SceneStorage` the user comes back to the same screen even after the system kills the app."

[উপরে ফিরুন](#toc)

---

## <a id="ios7"></a>iOS ৭. Architecture — Cubit থেকে `@Observable` view model

Android-এর [অধ্যায় ৮](#ch8)-এ দেখেছেন, layer বদলায় না, শুধু ইট বদলায়। iOS-এও একই কথা। Presentation, domain, data — তিনটা layer থাকে। Cubit-এর জায়গায় একটা `@Observable` class। `get_it`-এর জায়গায় সাধারণ `init`। আর repository ঠিক আগের মতোই।

একটা বড় পার্থক্য আগে বলে রাখি। Android-এ ViewModel একটা বিশেষ class, কারণ rotation-এ Activity মরে যায়। iOS-এ rotation-এ কিছু মরে না। তাই iOS-এ "ViewModel" কোনো framework class না। এটা আপনার নিজের একটা সাধারণ class, যার গায়ে শুধু `@Observable` লেখা।

### <a id="ios7-1"></a>iOS ৭.১ Layer একই থাকে

```
Flutter (আপনার এখনকার)                 iOS (SwiftUI)
──────────────────────────────         ──────────────────────────────────────
presentation/                          Features/Notes/
  notes_screen.dart  (Widget)            NotesScreen.swift    (View)
  notes_cubit.dart   (Cubit)             NotesViewModel.swift (@Observable class)
  notes_state.dart   (freezed)           (আলাদা state class সাধারণত লাগে না)
domain/                                Domain/
  note.dart          (model)             Note.swift           (struct)
  notes_repository.dart (abstract)       NotesRepository.swift (protocol)
data/                                  Data/
  notes_repository_impl.dart             OfflineFirstNotesRepository.swift
  notes_api.dart     (dio)               NotesAPI.swift       (URLSession)
  notes_dao.dart     (drift)             NoteEntity.swift     (SwiftData @Model)
di/injection.dart    (get_it)          NotesApp.swift       (@main — এখানেই সব জোড়া লাগে)
```

**`freezed` state কোথায় গেল?** Flutter-এ Cubit একটা immutable state object `emit` করে। iOS-এ view model-এর property-গুলোই state। `notes`, `isLoading`, `errorMessage` — প্রতিটা আলাদা `var`। SwiftUI জানে কোন view কোন property পড়ে। সেই property বদলালে শুধু সেই view আবার আঁকা হয়। তাই সব state একটা struct-এ ভরে `copyWith` করার দরকার পড়ে না।

**UseCase নিয়ে:** Android অধ্যায়ের কথাই এখানে খাটে। যে UseCase শুধু repository-র একটা method ডাকে, সেটা বাড়তি layer। Business rule থাকলে, বা দুইটা repository মেলাতে হলে, তখন বানান।

[উপরে ফিরুন](#toc)

### <a id="ios7-2"></a>iOS ৭.২ Cubit → `@Observable` view model

**এক লাইনে:** `@Observable` লেখা একটা class-এর প্রতিটা `var` নিজেই "observable"। SwiftUI view সেটা পড়লেই subscribe হয়ে যায়। `emit` লাগে না, `notifyListeners` লাগে না।

**Flutter-এ আপনি যেভাবে করেন:**

```dart
@freezed
class NotesState with _$NotesState {
  const factory NotesState({
    @Default([]) List<Note> notes,
    @Default(false) bool isLoading,
    String? error,
  }) = _NotesState;
}

class NotesCubit extends Cubit<NotesState> {
  NotesCubit(this._repo) : super(const NotesState());
  final NotesRepository _repo;

  Future<void> load() async {
    emit(state.copyWith(isLoading: true));
    try {
      final notes = await _repo.loadNotes();
      emit(state.copyWith(notes: notes, isLoading: false));
    } catch (_) {
      emit(state.copyWith(isLoading: false, error: 'নোট আনা যায়নি'));
    }
  }

  Future<void> delete(Note note) async {
    try {
      await _repo.delete(note.id);
      emit(state.copyWith(notes: state.notes.where((n) => n.id != note.id).toList()));
    } catch (_) {
      emit(state.copyWith(error: 'মোছা যায়নি'));
    }
  }
}
```

**iOS-এ একই কাজ:**

```swift
import Observation

@MainActor                          // সব state UI thread-এ বদলাবে
@Observable
final class NotesViewModel {
    private(set) var notes: [Note] = []      // বাইরে থেকে শুধু পড়া যাবে
    private(set) var isLoading = false
    var errorMessage: String?                // alert বন্ধ করলে view এটা nil করবে

    private let repository: any NotesRepository

    init(repository: any NotesRepository) {
        self.repository = repository         // init হালকা রাখুন — কোনো কাজ শুরু না
    }

    func load() async {
        isLoading = true
        defer { isLoading = false }          // যেভাবেই বের হই, loading বন্ধ
        do {
            notes = try await repository.loadNotes()
        } catch {
            errorMessage = "নোট আনা যায়নি"
        }
    }

    func delete(_ note: Note) async {
        do {
            try await repository.delete(id: note.id)
            notes.removeAll { $0.id == note.id }
        } catch {
            errorMessage = "মোছা যায়নি"
        }
    }
}
```

View-এ এটা এভাবে বসে:

```swift
import SwiftUI

struct NotesScreen: View {
    @State private var viewModel: NotesViewModel     // view model-এর মালিক এই view

    init(repository: any NotesRepository) {
        _viewModel = State(initialValue: NotesViewModel(repository: repository))
    }

    var body: some View {
        List(viewModel.notes) { note in              // notes পড়লাম → notes বদলালে আবার আঁকা
            NoteRow(note: note)
                .swipeActions {
                    Button("মুছুন", role: .destructive) {
                        Task { await viewModel.delete(note) }
                    }
                }
        }
        .overlay {
            if viewModel.isLoading { ProgressView() }
        }
        .task { await viewModel.load() }             // screen এলে চালু, চলে গেলে cancel
    }
}
```

**কী মিলল, কী আলাদা:**

| Flutter (Cubit) | Android (ViewModel) | iOS (`@Observable`) |
|---|---|---|
| `Cubit<NotesState>` | `ViewModel` + `StateFlow<UiState>` | `@Observable` class, property-ই state |
| `emit(state.copyWith(...))` | `_state.update { it.copy(...) }` | সরাসরি `notes = ...` |
| `BlocProvider(create:)` | `hiltViewModel()` | `@State private var viewModel` |
| `BlocBuilder` | `collectAsStateWithLifecycle()` | কিছু লাগে না — `body`-তে পড়লেই হলো |
| `close()`-এ cancel | `viewModelScope` নিজে বন্ধ | `.task { }` view চলে গেলে নিজে cancel |
| Widget গেলে Cubit যায় | Rotation-এ বাঁচে | Rotation-এ কিছু মরে না; view hierarchy থেকে সরলে যায় |

**ভেতরে কীভাবে কাজ করে:**
1. `@Observable` একটা Swift **macro** ([iOS ১](#ios1))। Compile-এর সময় এটা প্রতিটা `var`-এর getter আর setter-এ লুকানো code বসায়।
2. SwiftUI `body` চালানোর সময় দেখে রাখে, কোন কোন property পড়া হলো। এটা Observation framework-এর tracking।
3. পরে সেই property-র setter চললে, SwiftUI শুধু ওই view-এর `body` আবার চালায়।
4. যে property `body`-তে পড়া হয়নি, সেটা বদলালে কিছুই আবার আঁকা হয় না। `BlocBuilder`-এর `buildWhen` হাতে লিখতে হয় না — এটা নিজে থেকেই হয়।

**Version:** `@Observable` আর Observation framework iOS 17 থেকে। তার আগের code-এ দেখবেন `ObservableObject` + `@Published` + `@StateObject`। ওটা চিনে রাখুন, নতুন code-এ না। Apple-এর [migration guide](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro) আছে।

**`@MainActor` কেন:** View model-এর state UI পড়ে, তাই state সবসময় main thread-এ বদলানো উচিত। `@MainActor` লিখলে compiler নিজেই এটা নিশ্চিত করে ([iOS ২](#ios2))। Xcode 26 থেকে নতুন project-এ default actor isolation `MainActor` চালু থাকে। তবু view model-এ `@MainActor` স্পষ্ট লিখুন। পড়তে সহজ, আর পুরনো project-এও ঠিক থাকে।

**Best approach:** প্রতিটা screen-এর জন্য একটা `@MainActor @Observable final class`। State property `private(set)`। কাজের method `async`। View model-এর মালিক screen-এর view, `@State` দিয়ে। কাজ শুরু হয় `.task`-এ, `init`-এ না।

**ফাঁদ:**
- **`@State`-এর initial value বারবার তৈরি হয়।** Parent view আবার আঁকা হলে `NotesScreen.init` আবার চলে, তাই `NotesViewModel(...)` আবার তৈরি হয়। SwiftUI প্রথমটাই রাখে, নতুনটা ফেলে দেয়। তাই view model-এর `init`-এ network call বা timer চালু করবেন না। কাজ `.task`-এ।
- **`@Observable` class-এর জন্য `@StateObject` না।** `@StateObject` পুরনো `ObservableObject`-এর জন্য। `@Observable`-এর মালিকানা `@State` দিয়ে।
- **State public `var` রাখবেন না।** তখন view নিজেই `viewModel.notes = []` লিখে দিতে পারে। Cubit-এর বাইরে থেকে `emit` করা যেমন ভুল, এটাও তেমন। `private(set)` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios7-3"></a>iOS ৭.৩ Unidirectional data flow — state নিচে, event ওপরে

**এক লাইনে:** View শুধু state দেখায় আর event পাঠায়। State বদলায় শুধু view model। Flutter-এর BLoC আর Android-এর UDF-এর মতোই।

```
        ┌──────────── state (notes, isLoading) ────────────┐
        │                                                  ▼
 NotesViewModel                                       NotesScreen (body)
        ▲                                                  │
        └──────── event: await viewModel.delete(note) ─────┘
```

**Route আর Screen ভাগ করুন।** Android-এ `NotesRoute` (ViewModel নেয়) আর `NotesScreen` (stateless) আলাদা ছিল। SwiftUI-তেও একই কাজের:

```swift
// শুধু দেখায় — preview আর test সহজ
struct NotesListView: View {
    let notes: [Note]
    let onDelete: (Note) -> Void

    var body: some View {
        List(notes) { note in
            NoteRow(note: note)
                .swipeActions {
                    Button("মুছুন", role: .destructive) { onDelete(note) }
                }
        }
    }
}

#Preview {
    NotesListView(notes: [.sample], onDelete: { _ in })   // view model ছাড়াই preview; .sample আছে iOS ১০.৩-এ
}
```

`NotesScreen` view model রাখে, আর `NotesListView`-কে data আর closure দেয়। Flutter-এর `NotesPage` আর `NotesView`-এর মতো।

**One-off event: `BlocListener` কোথায়?** Snackbar বা alert-এর মতো "একবার" জিনিস Android-এ state হিসেবে রাখতে বলা হয়েছিল ([৮.৪](#ch8-4))। SwiftUI-তে এটা আরও স্বাভাবিক, কারণ alert নিজেই একটা `Binding<Bool>` চায়:

```swift
.alert(
    "সমস্যা হয়েছে",
    isPresented: Binding(
        get: { viewModel.errorMessage != nil },
        set: { isShown in if !isShown { viewModel.errorMessage = nil } }  // বন্ধ হলে clear
    )
) {
    Button("ঠিক আছে", role: .cancel) { }
} message: {
    Text(viewModel.errorMessage ?? "")
}
```

Error state-এ থাকে। Alert বন্ধ হলে SwiftUI নিজে `false` লেখে, আর আমরা error মুছে দিই। Event হারানোর ভয় নেই।

**State বদল দেখে কিছু করতে হলে** `.onChange(of:)` ব্যবহার করুন। যেমন নতুন note লেখার screen-এ, `EditNoteViewModel`-এর `didSave` সত্যি হলে screen বন্ধ করা:

```swift
.onChange(of: viewModel.didSave) { _, didSave in
    if didSave { dismiss() }
}
```

**চিনে রাখুন — TCA:** The Composable Architecture (Point-Free) একটা জনপ্রিয় library। এটা Redux বা BLoC-এর মতো: `State`, `Action`, `Reducer`। বড় team-এর project-এ দেখবেন। শুরুতে লাগবে না।

[উপরে ফিরুন](#toc)

### <a id="ios7-4"></a>iOS ৭.৪ `get_it` → init injection আর `@Environment`

**এক লাইনে:** iOS-এ DI-এর জন্য framework লাগে না। Dependency `init`-এ দিন। App-জুড়ে লাগে এমন কিছু থাকলে `@Environment`-এ রাখুন।

**Flutter-এ:**

```dart
final getIt = GetIt.instance;

void configureDependencies() {
  getIt.registerLazySingleton<NotesApi>(() => NotesApi(Dio()));
  getIt.registerLazySingleton<NotesRepository>(
    () => NotesRepositoryImpl(getIt<NotesApi>(), getIt<AppDatabase>()),
  );
  getIt.registerFactory(() => NotesCubit(getIt<NotesRepository>()));
}
```

**iOS-এ — composition root:**

```swift
import SwiftUI
import SwiftData

@main
struct NotesApp: App {
    // এই জায়গাটাই আপনার configureDependencies()
    private let container: ModelContainer
    private let repository: OfflineFirstNotesRepository
    @State private var session = SessionStore()          // সারা app-এ লাগে

    init() {
        do {
            container = try ModelContainer(for: NoteEntity.self)
        } catch {
            fatalError("Database খোলা যায়নি: \(error)")   // এটা ছাড়া app চলতেই পারে না
        }
        let api = NotesAPI(baseURL: URL(string: "https://api.byteonyx.com")!)
        repository = OfflineFirstNotesRepository(context: container.mainContext, api: api)
    }

    var body: some Scene {
        WindowGroup {
            NotesScreen(repository: repository)          // init injection
                .environment(session)                    // environment injection
        }
        .modelContainer(container)
    }
}
```

`SessionStore` হলো একটা ছোট `@MainActor @Observable` class — কে login করেছে, তার নাম। যে view-এর দরকার, সে নিজে তুলে নেয়:

```swift
struct ProfileView: View {
    @Environment(SessionStore.self) private var session   // Provider.of<SessionStore>(context)

    var body: some View {
        Text(session.userName ?? "অতিথি")
    }
}
```

**কী মিলল, কী আলাদা:**

| `get_it` / `injectable` | Hilt (Android) | iOS |
|---|---|---|
| Runtime-এ খোঁজে (service locator) | Compile time-এ graph বানায় | সাধারণ `init` — compiler নিজেই type check করে |
| `registerLazySingleton` | `@Singleton` | `App`-এ একবার তৈরি করে সবাইকে একই object দেওয়া |
| `registerFactory` | unscoped | প্রতিবার `NotesViewModel(...)` |
| `@LazySingleton(as: Interface)` | `@Binds` | `protocol` + তার একটা implementation |
| `getIt<NotesCubit>()` | `hiltViewModel()` | `@State var viewModel = ...` |
| `Provider` / `InheritedWidget` | `CompositionLocal` | `.environment(obj)` + `@Environment(Type.self)` |
| `@Environment('test')` | `@TestInstallIn` | test-এ fake object দিয়ে `init` ডাকা |

**কোনটা কখন:**
- **Init injection** — repository, API client, view model। ৯০% ক্ষেত্রে এটাই। কোন class কী চায়, signature দেখলেই বোঝা যায়।
- **`@Environment`** — অনেক দূরের অনেক view-এর যা লাগে: login session, theme-এর মতো setting, navigation router। প্রতিটা স্তরে হাতে হাতে দিতে হলে বিরক্তিকর হতো, সেগুলো।

**চিনে রাখুন:** বড় project-এ Factory বা Point-Free-এর swift-dependencies-এর মতো DI library দেখবেন। এরা `get_it`-এর কাছাকাছি। ছোট আর মাঝারি app-এ লাগে না।

**Best approach:** `App` struct-এ একটা composition root। সেখানে একবার করে database, API, repository তৈরি করুন, আর `init` দিয়ে নিচে দিন। শুধু সত্যিকারের app-wide `@Observable` object `@Environment`-এ।

**ফাঁদ:**
- **`.environment(session)` বসাতে ভুলে গেলে crash।** `@Environment(SessionStore.self)` object না পেলে app runtime-এ crash করে। Flutter-এর "ProviderNotFoundException"-এর মতো, শুধু আরও কঠোর। Preview-তেও `.environment(...)` দিতে হয়।
- **সব কিছু `@Environment`-এ ঢোকাবেন না।** তখন কোন view কী চায়, বোঝা যায় না। এটা লুকানো global হয়ে যায় — `get_it`-কে সব জায়গা থেকে ডাকার মতো।

[উপরে ফিরুন](#toc)

### <a id="ios7-5"></a>iOS ৭.৫ Repository layer

**এক লাইনে:** Repository একটা `protocol`। View model শুধু protocol চেনে। আসল implementation database আর network জোড়া দেয়। Test-এ একটা fake দিন।

**Flutter-এ:**

```dart
abstract class NotesRepository {
  Future<List<Note>> loadNotes();
  Future<void> save(Note note);
  Future<void> delete(String id);
  Future<void> refresh();
}
```

**iOS-এ:**

```swift
import Foundation

// Domain model — সাধারণ value type, কোনো framework-এর ওপর নির্ভর করে না
struct Note: Identifiable, Equatable, Sendable {
    let id: UUID
    var title: String
    var body: String
    var updatedAt: Date
    var imageURL: URL?
}

@MainActor
protocol NotesRepository {
    func loadNotes() async throws -> [Note]
    func save(_ note: Note) async throws
    func delete(id: Note.ID) async throws
    func refresh() async throws          // server থেকে টেনে আনা
}
```

**কেন `protocol`, যখন একটাই implementation?** কারণ test-এ একটা fake লাগবে ([iOS ১০.৩](#ios10-3))। এটা "দ্বিতীয় implementation"-এর আসল প্রয়োজন। Fake ছাড়া view model test করতে হলে আসল database আর network লাগত।

**কেন `struct Note`, SwiftData-র `@Model` class না?** SwiftData-র model একটা class, database context-এর সাথে বাঁধা, আর thread-এর মধ্যে পাঠানো যায় না। View model আর UI-তে একটা সাধারণ `struct` সহজ আর নিরাপদ। Database-এর class (`NoteEntity`) data layer-এর ভেতরেই থাকে। Android-এ Room-এর `NoteEntity` আর domain-এর `Note` আলাদা ছিল — একই নকশা। আসল implementation দেখবেন [iOS ৮.৮](#ios8-8)-এ।

**`@MainActor` কেন protocol-এ?** View model `@MainActor`। Repository-ও main actor-এ থাকলে তাদের মধ্যে data পাঠাতে `Sendable`-এর ঝামেলা থাকে না। চিন্তা নেই, network call main thread আটকায় না। `await` চলার সময় main thread ছেড়ে দেওয়া হয়, আর `URLSession` নিজের thread-এ কাজ করে।

**Best approach:** Repository protocol domain-এ, implementation data-তে। Protocol-এ শুধু domain type (`Note`), কখনো `NoteEntity` বা `NoteDTO` না।

**ফাঁদ:** Repository থেকে SwiftData-র `@Model` object সরাসরি view-এ পাঠানো। কাজ চলবে, কিন্তু view তখন database-এর live object বদলাতে পারে, আর test-এ database লাগবে।

> **মনে রাখুন**
> - Layer একই। Cubit → `@MainActor @Observable final class`, freezed state → property, `get_it` → `init`।
> - View model-এর মালিক view, `@State` দিয়ে। কাজ শুরু `.task`-এ, `init`-এ না।
> - `BlocBuilder` লাগে না — `body`-তে যে property পড়বেন, শুধু সেটা বদলালেই view আবার আঁকা হয়।
> - DI: composition root `App` struct-এ। App-wide object `@Environment`-এ, বাকি সব `init`-এ।
> - Repository = `protocol` + domain `struct`। Database-এর class data layer-এর বাইরে যায় না।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "SwiftUI-তে আমি MVVM ব্যবহার করি। প্রতিটা screen-এর একটা `@MainActor @Observable` view model থাকে, যার property-গুলোই state, আর view সেটা `@State` দিয়ে রাখে। Observation framework নিজেই দেখে কোন view কোন property পড়ে, তাই শুধু দরকারি view আবার আঁকা হয়। DI-এর জন্য framework নিই না — `App` struct-এ সব তৈরি করে `init` দিয়ে দিই, আর app-wide জিনিস `@Environment`-এ। Flutter-এ Cubit আর get_it দিয়ে যে নকশা করতাম, এটা প্রায় তাই।"
> - *English:* "In SwiftUI I use MVVM. Each screen has a `@MainActor @Observable` view model whose properties are the state, and the view owns it with `@State`. The Observation framework tracks which view reads which property, so only the views that need it redraw. I don't use a DI framework — I build everything in the `App` struct and pass it through `init`, and I put truly app-wide objects in the `@Environment`. It's almost the same design I used in Flutter with Cubit and get_it."

[উপরে ফিরুন](#toc)

---

## <a id="ios8"></a>iOS ৮. Data — network, JSON, database, storage

Android-এর data অধ্যায়ে ([৯](#ch9)) প্রায় প্রতিটা কাজের জন্য একটা Jetpack বা Square-এর library ছিল। iOS-এ মজার ব্যাপার হলো, বেশিরভাগ কাজ Apple-এর নিজের SDK-তেই আছে। Network-এর জন্য `URLSession`, JSON-এর জন্য `Codable`, database-এর জন্য SwiftData, secret-এর জন্য Keychain। কোনো dependency যোগ না করেই পুরো Notes app-এর data layer বানানো যায়।

### <a id="ios8-1"></a>iOS ৮.১ `dio` → `URLSession` + `async`/`await`

**এক লাইনে:** `URLSession` হলো Apple-এর built-in HTTP client। `async`/`await` দিয়ে এক লাইনে request পাঠানো যায়। Interceptor নেই, তাই একটা ছোট wrapper নিজে লিখুন।

**Flutter-এ:**

```dart
final dio = Dio(BaseOptions(baseUrl: 'https://api.byteonyx.com/'))
  ..interceptors.add(InterceptorsWrapper(
    onRequest: (options, handler) {
      options.headers['Authorization'] = 'Bearer ${tokenStore.token}';
      handler.next(options);
    },
  ));

Future<List<NoteDto>> fetchNotes() async {
  final response = await dio.get<List<dynamic>>('notes');   // 4xx/5xx হলে DioException
  return response.data!.map((e) => NoteDto.fromJson(e as Map<String, dynamic>)).toList();
}
```

**iOS-এ:**

```swift
import Foundation

enum APIError: Error {
    case notHTTP
    case status(Int)
}

struct NotesAPI: Sendable {
    let baseURL: URL
    var session: URLSession = .shared
    var token: @Sendable () -> String? = { nil }          // Keychain থেকে token দেবে (iOS ৮.৫)

    func fetchNotes() async throws -> [NoteDTO] {
        let request = URLRequest(url: baseURL.appending(path: "notes"))
        let data = try await send(request)
        return try Self.decoder.decode([NoteDTO].self, from: data)
    }

    func upload(_ note: NoteDTO) async throws {
        var request = URLRequest(url: baseURL.appending(path: "notes/\(note.id)"))
        request.httpMethod = "PUT"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = try Self.encoder.encode(note)
        _ = try await send(request)
    }

    func delete(id: UUID) async throws {
        var request = URLRequest(url: baseURL.appending(path: "notes/\(id)"))
        request.httpMethod = "DELETE"
        _ = try await send(request)
    }

    // dio-র interceptor-এর কাজ এখানে: প্রতিটা request এই পথ দিয়ে যায়
    private func send(_ request: URLRequest) async throws -> Data {
        var request = request
        if let token = token() {
            request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
        }
        let (data, response) = try await session.data(for: request)
        guard let http = response as? HTTPURLResponse else { throw APIError.notHTTP }
        guard (200..<300).contains(http.statusCode) else {
            throw APIError.status(http.statusCode)          // URLSession নিজে এটা করে না!
        }
        return data
    }

    private static var decoder: JSONDecoder {
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        return decoder
    }

    private static var encoder: JSONEncoder {
        let encoder = JSONEncoder()
        encoder.dateEncodingStrategy = .iso8601
        return encoder
    }
}
```

**কী মিলল, কী আলাদা:**

| `dio` | Retrofit + OkHttp (Android) | `URLSession` |
|---|---|---|
| package যোগ করতে হয় | library যোগ করতে হয় | SDK-তেই আছে |
| `BaseOptions(baseUrl:)` | `Retrofit.Builder().baseUrl()` | নিজের `baseURL` property |
| Interceptor | OkHttp `Interceptor` | নেই — নিজের `send()` wrapper |
| 401-এ refresh: `QueuedInterceptor` | `Authenticator` | `send()`-এর ভেতরে status 401 ধরে refresh, তারপর আবার চেষ্টা |
| 4xx/5xx-এ exception | Retrofit `Response`/`HttpException` | **exception না** — নিজে status দেখতে হয় |
| `CancelToken` | coroutine cancel | `Task` cancel হলে request-ও cancel |
| `LogInterceptor` | `HttpLoggingInterceptor` | Xcode-এর Network instrument, বা `send()`-এ নিজের log |

**ভেতরে কীভাবে কাজ করে:** `session.data(for:)` একটা `async` function। Request চলার সময় আপনার task থেমে থাকে, কিন্তু main thread আটকায় না। আসল network-এর কাজ `URLSession` নিজের background queue-তে করে। Task cancel হলে (যেমন `.task`-এর view চলে গেলে) request-ও cancel হয়, আর `CancellationError` বা `URLError(.cancelled)` আসে। Flutter-এ `mounted` check করতেন। এখানে লাগে না।

**চিনে রাখুন — Alamofire:** iOS-এর "dio" বলা যায়। Interceptor, retry, upload progress সব আছে। পুরনো project-এ খুব দেখবেন। নতুন project-এ `async`/`await`-এর পরে `URLSession` প্রায় সব কাজের জন্য যথেষ্ট।

**Best approach:** `URLSession` + একটা ছোট `send()` wrapper, যেখানে token বসে আর status check হয়। Library শুধু তখন, যখন সত্যিই জটিল কিছু লাগে।

**ফাঁদ:**
- **404 বা 500-এ কোনো error আসে না।** `URLSession` শুধু network-এর ভুলে throw করে — internet নেই, timeout, DNS। Server 500 ফেরত দিলেও আপনি `data` পাবেন। Dio-র অভ্যাসে এটা সবচেয়ে বড় bug-এর উৎস। Status নিজে check করুন।
- **`http://` চলে না।** App Transport Security (ATS) default-এ শুধু HTTPS দেয়। Local test server-এর জন্য `Info.plist`-এ exception লাগে। Android-এর cleartext traffic নিষেধের মতো।
- **`URLSession.shared` সব কাজে না।** বড় file upload বা download, যেটা app বন্ধ হলেও চলবে, তার জন্য background session লাগে ([iOS ৯.১](#ios9-1))।

[উপরে ফিরুন](#toc)

### <a id="ios8-2"></a>iOS ৮.২ `json_serializable` → `Codable`

**এক লাইনে:** Type-এর গায়ে `Codable` লিখলেই compiler নিজে JSON-এ যাওয়া-আসার code বানিয়ে দেয়। `build_runner` লাগে না, `.g.dart` file নেই।

**Flutter-এ:**

```dart
@JsonSerializable(fieldRename: FieldRename.snake)
class NoteDto {
  NoteDto(this.id, this.title, this.body, this.updatedAt, this.imageUrl);
  final String id;
  final String title;
  final String body;
  final DateTime updatedAt;
  final String? imageUrl;

  factory NoteDto.fromJson(Map<String, dynamic> json) => _$NoteDtoFromJson(json);
  Map<String, dynamic> toJson() => _$NoteDtoToJson(this);
}
```

**iOS-এ:**

```swift
import Foundation

struct NoteDTO: Codable, Sendable {
    let id: UUID
    let title: String
    let body: String
    let updatedAt: Date
    let imageURL: URL?               // Optional — JSON-এ key না থাকলেও চলবে

    enum CodingKeys: String, CodingKey {   // সব key লিখতে হয়; নাম দিতে হয় শুধু আলাদাগুলোর
        case id, title, body
        case updatedAt = "updated_at"
        case imageURL = "image_url"
    }
}

// Domain-এর সাথে যাওয়া-আসা
extension NoteDTO {
    init(_ note: Note) {
        self.init(id: note.id, title: note.title, body: note.body,
                  updatedAt: note.updatedAt, imageURL: note.imageURL)
    }

    var asNote: Note {
        Note(id: id, title: title, body: body, updatedAt: updatedAt, imageURL: imageURL)
    }
}
```

**কী মিলল, কী আলাদা:**

| `json_serializable` | kotlinx.serialization | `Codable` |
|---|---|---|
| `build_runner` চালাতে হয় | compiler plugin | compiler নিজে, কিছু চালাতে হয় না |
| `@JsonKey(name: 'updated_at')` | `@SerialName("updated_at")` | `CodingKeys` enum |
| `fieldRename: snake` | `JsonNamingStrategy.SnakeCase` | `decoder.keyDecodingStrategy = .convertFromSnakeCase` |
| অজানা key — উপেক্ষা | `ignoreUnknownKeys = true` লাগে | default-এ উপেক্ষা |
| key নেই, field non-null → error | error | `DecodingError.keyNotFound` |
| `DateTime.parse` নিজে করে | serializer লাগে | `dateDecodingStrategy` ঠিক করতে হয় |

**ভেতরে কীভাবে কাজ করে:** `Codable` আসলে দুইটা protocol — `Decodable` আর `Encodable`। আপনি conformance লিখলে, compiler compile-এর সময় `init(from:)` আর `encode(to:)` বানিয়ে দেয়। কোনো reflection নেই, runtime-এ খোঁজাখুঁজি নেই। তাই দ্রুত। কোনো field-এর জন্য বিশেষ নিয়ম লাগলে `init(from:)` নিজে লিখতে পারেন। তখন বাকি সব field-ও হাতে লিখতে হয়।

**Best approach:** Network-এর জন্য আলাদা `NoteDTO`, app-এর ভেতরে `Note`। `CodingKeys` বা `.convertFromSnakeCase` — একটা বেছে নিয়ে পুরো project-এ সেটাই।

**ফাঁদ:**
- **Date-এর default ভুল।** `JSONDecoder`-এর default date strategy `.deferredToDate` — এটা ২০০১ সাল থেকে সেকেন্ড গোনে। Server ISO 8601 string পাঠালে decode fail করে। `.iso8601` দিন।
- **`.iso8601` পুরনো iOS-এ millisecond চেনে না।** Server `"2026-11-10T09:30:00.123Z"` পাঠালে iOS 26-এর আগের OS-এ `.iso8601` fail করে (Swift 6.2-এর Foundation থেকে fractional seconds পড়া যায়)। App পুরনো iOS-এ চললে `.custom` strategy দিয়ে fractional seconds চালু করা formatter লাগে।
- **একটা field-এর ভুলে পুরো list fail।** ১০০টা note-এর একটায় `title` null এলে পুরো `[NoteDTO]` decode-ই throw করে। যে field server কখনো বাদ দিতে পারে, সেটা Optional রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ios8-3"></a>iOS ৮.৩ `drift` → SwiftData (আর Core Data চিনে রাখুন)

**এক লাইনে:** SwiftData হলো Apple-এর database framework (iOS 17 থেকে)। Class-এর গায়ে `@Model` লিখলেই সেটা database-এর table। SQL লিখতে হয় না।

**Flutter-এ (drift):**

```dart
class Notes extends Table {
  TextColumn get id => text()();
  TextColumn get title => text()();
  TextColumn get body => text()();
  DateTimeColumn get updatedAt => dateTime()();
  BoolColumn get isSynced => boolean().withDefault(const Constant(false))();
  @override
  Set<Column> get primaryKey => {id};
}

Stream<List<Note>> watchNotes() =>
    (select(notes)..orderBy([(n) => OrderingTerm.desc(n.updatedAt)])).watch();
```

**iOS-এ (SwiftData):**

```swift
import Foundation
import SwiftData

@Model
final class NoteEntity {
    @Attribute(.unique) var id: UUID
    var title: String
    var body: String
    var updatedAt: Date
    var imageURL: URL?
    var isSynced: Bool                    // server-এ পৌঁছেছে কি না
    var markedForDeletion = false         // offline-এ মোছা, server-কে জানানো বাকি (iOS ৮.৮)

    init(id: UUID, title: String, body: String, updatedAt: Date, imageURL: URL?, isSynced: Bool) {
        self.id = id
        self.title = title
        self.body = body
        self.updatedAt = updatedAt
        self.imageURL = imageURL
        self.isSynced = isSynced
    }
}

extension NoteEntity {
    convenience init(note: Note, isSynced: Bool) {
        self.init(id: note.id, title: note.title, body: note.body,
                  updatedAt: note.updatedAt, imageURL: note.imageURL, isSynced: isSynced)
    }

    var asNote: Note {
        Note(id: id, title: title, body: body, updatedAt: updatedAt, imageURL: imageURL)
    }
}
```

**পড়া আর লেখা:**

```swift
let context = container.mainContext               // ModelContainer তৈরি হয় App-এ (iOS ৭.৪)

// select ... order by updatedAt desc
let newestFirst = FetchDescriptor<NoteEntity>(
    sortBy: [SortDescriptor(\.updatedAt, order: .reverse)]
)
let all = try context.fetch(newestFirst)

// where isSynced = false
let pending = FetchDescriptor<NoteEntity>(predicate: #Predicate { $0.isSynced == false })
let unsynced = try context.fetch(pending)

// insert, update, delete
context.insert(NoteEntity(note: newNote, isSynced: false))
all.first?.title = "নতুন শিরোনাম"                   // object বদলালেই update
context.delete(all.last!)
try context.save()
```

**`.watch()`-এর মতো জিনিস — `@Query`:** View-এর ভেতরে `@Query` লিখলে database বদলালেই list নিজে থেকে নতুন হয়ে যায়:

```swift
struct QuickNotesList: View {
    @Query(sort: \NoteEntity.updatedAt, order: .reverse) private var notes: [NoteEntity]

    var body: some View {
        List(notes) { note in Text(note.title) }
    }
}
```

এটা ছোট app-এর জন্য দারুণ। কিন্তু তখন view সরাসরি database চেনে, আর view model বা repository থাকে না। Notes app-এ sync আর test আছে, তাই আমরা repository দিয়ে পড়ব ([iOS ৮.৮](#ios8-8))। `@Query` চিনে রাখুন, Apple-এর sample-এ সব জায়গায় পাবেন।

**কী মিলল, কী আলাদা:**

| drift | Room (Android) | SwiftData |
|---|---|---|
| `Table` class | `@Entity` | `@Model` class |
| `@DriftDatabase` | `@Database` | `ModelContainer` |
| DAO / query method | `@Dao` | `ModelContext` + `FetchDescriptor` |
| `where(...)` | SQL `WHERE` | `#Predicate { ... }` (Swift-এ লেখা, compile time-এ check) |
| `.watch()` → `Stream` | `Flow` query | `@Query` (শুধু view-এ) |
| `transaction(() async {...})` | `@Transaction` | `context.transaction { }`, বা একবারে `save()` |
| `MigrationStrategy` | `Migration` | `VersionedSchema` + `SchemaMigrationPlan` |
| background isolate | `Dispatchers.IO` | `@ModelActor` |

**ভেতরে কীভাবে কাজ করে:** `@Model` একটা macro। এটা আপনার class-কে `PersistentModel` বানায়, আর প্রতিটা property-কে database-এর সাথে জুড়ে দেয়। নিচে data থাকে একটা SQLite file-এ, app-এর Application Support folder-এ। `ModelContext` হলো একটা খাতা — কী insert হলো, কী বদলাল, তার হিসাব রাখে। `save()` করলে সব একসাথে disk-এ যায়। Main context নিজেও মাঝে মাঝে auto-save করে, কিন্তু সেটার ওপর ভরসা করবেন না।

**Core Data — চিনে রাখুন:** SwiftData-র আগে ২০০৫ সাল থেকে Apple-এর database ছিল Core Data। SwiftData আসলে Core Data-র প্রমাণিত storage-এর ওপরেই বানানো। পুরনো project-এ দেখবেন:

| Core Data | SwiftData |
|---|---|
| `.xcdatamodeld` file (Xcode-এর visual editor) | `@Model` class, code-এ |
| `NSManagedObject` | `@Model` class |
| `NSPersistentContainer` | `ModelContainer` |
| `NSManagedObjectContext` | `ModelContext` |
| `NSFetchRequest` + `NSPredicate` (string) | `FetchDescriptor` + `#Predicate` (type-safe) |
| `@FetchRequest` (SwiftUI) | `@Query` |

SQL নিজে লিখতে চাইলে, drift-এর মতো অনুভূতির জন্য third-party GRDB আছে।

**Best approach:** নতুন app, minimum iOS 17 বা তার বেশি → SwiftData। Database-এর `@Model` class data layer-এ রাখুন, বাইরে domain `struct`।

**ফাঁদ:**
- **Migration ছাড়া model বদলানো।** নতুন optional property, বা default value-সহ property যোগ করলে SwiftData নিজে lightweight migration করে। কিন্তু default ছাড়া নতুন non-optional property, বা নাম বদল — তখন `ModelContainer` তৈরি হতেই error দেয়। App চালু হওয়ার পথে `try!` থাকলে সরাসরি crash। Release-এর আগে `VersionedSchema` বানিয়ে রাখুন।
- **`ModelContext` thread পার হয় না।** এটা `Sendable` না। Main context শুধু main actor-এ। Background-এ বড় import করতে `@ModelActor` দিয়ে আলাদা actor বানান — drift-এ background isolate-এ আলাদা connection-এর মতো।
- **Minimum iOS 17।** Flutter app iOS 15 থেকে চলে। কিন্তু native code-এ SwiftData বা `@Observable` নিলে আপনার minimum-ও উঠবে iOS 17-এ।

[উপরে ফিরুন](#toc)

### <a id="ios8-4"></a>iOS ৮.৪ `shared_preferences` → `UserDefaults` / `@AppStorage`

**এক লাইনে:** ছোট setting রাখার জায়গা `UserDefaults`। SwiftUI-তে `@AppStorage` দিয়ে এটা সরাসরি view-এর state হয়ে যায়।

মজার কথা: Flutter-এর `shared_preferences` iOS-এ ভেতরে `UserDefaults`-ই ব্যবহার করে। আপনি এতদিন এটাই চালিয়েছেন।

**Flutter-এ:**

```dart
final prefs = await SharedPreferences.getInstance();
await prefs.setBool('sort_by_date', true);
final sortByDate = prefs.getBool('sort_by_date') ?? false;
```

**iOS-এ:**

```swift
// View-এর বাইরে
UserDefaults.standard.set(true, forKey: "sort_by_date")
let sortByDate = UserDefaults.standard.bool(forKey: "sort_by_date")   // না থাকলে false

// View-এর ভেতরে — state-এর মতো
struct SettingsView: View {
    @AppStorage("sort_by_date") private var sortByDate = false

    var body: some View {
        Toggle("তারিখ ধরে সাজাও", isOn: $sortByDate)   // বদলালে নিজে save হয়
    }
}
```

**কী মিলল, কী আলাদা:**

| `shared_preferences` | DataStore (Android) | `UserDefaults` / `@AppStorage` |
|---|---|---|
| `await getInstance()` | `Flow`, async | synchronous — `await` লাগে না |
| বদলালে কাউকে জানায় না | `data` Flow নতুন value দেয় | `@AppStorage` আছে এমন সব view নিজে আবার আঁকা হয় |
| ভেতরে iOS-এ `UserDefaults` | Protobuf/Preferences file | একটা plist file, `Library/Preferences/`-এ |

**ভেতরে কীভাবে কাজ করে:** `UserDefaults` app চালুর পরে পুরো plist memory-তে রাখে। পড়া তাই খুব দ্রুত আর synchronous। লেখা system সময়মতো disk-এ পাঠায়। এজন্যই এটা ছোট জিনিসের জন্য — setting, flag, শেষ বার কোন tab খোলা ছিল।

**Privacy manifest:** `UserDefaults` Apple-এর "required reason API"-এর তালিকায় আছে। ব্যবহার করলে privacy manifest-এ কারণ লিখতে হয় — নিজের app-এর data পড়া-লেখার জন্য কারণের code `CA92.1` ([iOS ১১.৫](#ios11-5))।

**Best approach:** ছোট setting → `@AppStorage` (view-এ) বা `UserDefaults` (বাইরে)। Structured data → SwiftData। Secret → Keychain।

**ফাঁদ:**
- **Token বা password `UserDefaults`-এ না।** এটা একটা সাধারণ plist file — Keychain-এর মতো আলাদা সুরক্ষা নেই, আর device backup-এ যায়। Jailbreak করা phone-এ বা backup থেকে সহজে পড়া যায়।
- **বড় data না।** পুরো file memory-তে থাকে, তাই এখানে note-এর list রাখলে app-এর memory আর চালুর সময় দুটোই বাড়ে।

[উপরে ফিরুন](#toc)

### <a id="ios8-5"></a>iOS ৮.৫ `flutter_secure_storage` → Keychain

**এক লাইনে:** Keychain হলো OS-এর encrypted vault। Token, password এখানে রাখুন। আর মনে রাখুন: **app uninstall করলেও Keychain-এর data সাধারণত থেকে যায়।**

`flutter_secure_storage` iOS-এ ভেতরে ঠিক এই Keychain-ই ব্যবহার করে। Android-এ ছিল Keystore + encryption ([৯.৫](#ch9-5))। iOS-এ পুরো data-টাই OS-এর vault-এ যায়, শুধু key না।

**Flutter-এ:**

```dart
const storage = FlutterSecureStorage();
await storage.write(key: 'auth_token', value: token);
final token = await storage.read(key: 'auth_token');
```

**iOS-এ:** Keychain-এর API পুরনো C-ধাঁচের — dictionary দিয়ে query। তাই একটা ছোট wrapper লিখে রাখুন:

```swift
import Foundation
import Security

struct KeychainError: Error {
    let status: OSStatus
}

enum Keychain {
    private static let service = "com.byteonyx.notes"

    static func save(_ value: String, account: String) throws {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
        ]
        SecItemDelete(query as CFDictionary)                     // পুরনো থাকলে আগে মুছি

        var attributes = query
        attributes[kSecValueData as String] = Data(value.utf8)
        attributes[kSecAttrAccessible as String] = kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
        let status = SecItemAdd(attributes as CFDictionary, nil)
        guard status == errSecSuccess else { throw KeychainError(status: status) }
    }

    static func read(account: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne,
        ]
        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)
        guard status == errSecSuccess, let data = result as? Data else { return nil }
        return String(decoding: data, as: UTF8.self)
    }

    static func deleteAll() {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
        ]
        SecItemDelete(query as CFDictionary)
    }
}
```

**`kSecAttrAccessible...` কী:** কখন item পড়া যাবে, তা বলে দেয়। `AfterFirstUnlock` মানে phone চালু হওয়ার পরে একবার unlock হলেই পড়া যাবে — background sync-এর জন্য এটাই দরকার। `ThisDeviceOnly` মানে backup থেকে নতুন phone-এ যাবে না। Token-এর জন্য এটাই ঠিক।

**ফাঁদ — uninstall-এর পরেও থাকে:**

এটা iOS-এর সবচেয়ে বিখ্যাত ফাঁদগুলোর একটা। User app মুছে আবার install করল। App-এর database, `UserDefaults`, file — সব নতুন, খালি। কিন্তু Keychain-এ পুরনো token এখনো বসে আছে। ফল: user ভাবছে নতুন শুরু করছে, অথচ app আগের account-এ login হয়ে খোলে। অথবা পুরনো, বাতিল token দিয়ে প্রথম request-ই 401 খায়।

Android-এ এটা হয় না — uninstall করলে Keystore-এর key-ও যায়। আর মনে রাখুন, Apple কখনো লিখিতভাবে বলেনি যে Keychain item থেকে যাবে। এটা দীর্ঘদিনের আচরণ, নিশ্চয়তা না। তাই দুই দিকেই ভরসা করবেন না।

সমাধান — প্রথম launch চিনে পুরনো Keychain মুছে দিন:

```swift
// App চালুর একদম শুরুতে, যেমন NotesApp.init()-এ
private func clearKeychainAfterReinstall() {
    let key = "hasLaunchedBefore"
    guard !UserDefaults.standard.bool(forKey: key) else { return }
    Keychain.deleteAll()                              // UserDefaults নতুন, মানে নতুন install
    UserDefaults.standard.set(true, forKey: key)
}
```

`UserDefaults` uninstall-এ মুছে যায়, Keychain যায় না — এই পার্থক্যটাই এখানে কাজে লাগছে। Flutter-এ `flutter_secure_storage`-এর সাথে ঠিক একই কাজ `shared_preferences` দিয়ে করতে হয়।

**কী মিলল, কী আলাদা:**

| `flutter_secure_storage` | Android | iOS Keychain |
|---|---|---|
| `write` / `read` | Keystore-এর key + Tink দিয়ে encrypt, DataStore-এ রাখা | `SecItemAdd` / `SecItemCopyMatching` |
| uninstall-এ? | মুছে যায় | **সাধারণত থেকে যায়** |
| নতুন phone-এ? | key backup-এ যায় না | `ThisDeviceOnly` হলে যায় না, নইলে encrypted backup-এ যায় |
| দুই app-এ share | না | Keychain access group দিয়ে সম্ভব |

**Best approach:** Token আর secret → Keychain, `AfterFirstUnlockThisDeviceOnly`। প্রথম launch-এ পুরনো item মুছে দিন। Logout-এ `deleteAll()`।

[উপরে ফিরুন](#toc)

### <a id="ios8-6"></a>iOS ৮.৬ Image: `cached_network_image` → `AsyncImage`

**এক লাইনে:** `AsyncImage` হলো SwiftUI-র built-in network image (iOS 15 থেকে)। সহজ, কিন্তু নিজের image cache নেই।

**Flutter-এ:**

```dart
CachedNetworkImage(
  imageUrl: note.imageUrl,
  placeholder: (_, __) => const CircularProgressIndicator(),
  errorWidget: (_, __, ___) => const Icon(Icons.image),
  fit: BoxFit.cover,
);
```

**iOS-এ:**

```swift
AsyncImage(url: note.imageURL) { phase in
    switch phase {
    case .success(let image):
        image.resizable().scaledToFill()          // BoxFit.cover
    case .failure:
        Image(systemName: "photo")                // errorWidget
    default:
        ProgressView()                            // placeholder
    }
}
.frame(width: 64, height: 64)
.clipShape(.rect(cornerRadius: 8))
```

**কী আলাদা:**
- `cached_network_image` memory আর disk দুই জায়গায় cache করে। Android-এর Coil-ও তাই ([৯.৬](#ch9-6))। `AsyncImage`-এর নিজের কোনো image cache নেই। List-এ scroll করে ফিরে এলে আবার load হতে পারে।
- Coil view-এর মাপ দেখে ছবি ছোট করে decode করে। `AsyncImage` পুরো ছবি decode করে। 4000px ছবি 64pt thumbnail-এ দিলে পুরো memory খায়।

**চিনে রাখুন:** Nuke আর Kingfisher — iOS-এর দুই জনপ্রিয় image library। এরা cache, downsampling, prefetch সব করে। iOS-এর "cached_network_image" বলা যায়।

**Best approach:** কয়েকটা ছবি, profile picture → `AsyncImage`। ছবিতে ভরা list বা feed → Nuke বা Kingfisher।

[উপরে ফিরুন](#toc)

### <a id="ios8-7"></a>iOS ৮.৭ File system আর sandbox

**এক লাইনে:** প্রতিটা iOS app নিজের একটা বন্ধ folder-এ (sandbox) থাকে। বাইরের কিছু দেখতে পায় না, অন্য কেউও তার ভেতরে ঢুকতে পারে না। ভেতরে কয়েকটা নির্দিষ্ট folder আছে, প্রতিটার নিয়ম আলাদা।

Flutter-এ `path_provider` দিয়ে এই folder-গুলোই পেতেন। নিচের table-এ `path_provider`-এর iOS mapping তার source code দেখে মেলানো:

| Folder | কী রাখবেন | Backup-এ যায়? | System মুছতে পারে? | `path_provider` | Android-এ কাছাকাছি |
|---|---|---|---|---|---|
| `Documents/` | user-এর বানানো file (export করা note) | হ্যাঁ | না | `getApplicationDocumentsDirectory()` | `filesDir` |
| `Library/Application Support/` | app-এর নিজের data (database, attachment) | হ্যাঁ | না | `getApplicationSupportDirectory()` | `filesDir` |
| `Library/Caches/` | আবার বানানো যায় এমন জিনিস (thumbnail) | না | হ্যাঁ, জায়গা কম হলে | `getTemporaryDirectory()`, `getApplicationCacheDirectory()` | `cacheDir` |
| `tmp/` | একদম অল্প সময়ের file | না | হ্যাঁ | — | `cacheDir` |

খেয়াল করুন: iOS-এ `path_provider`-এর `getTemporaryDirectory()` আসলে `Library/Caches` দেয়, `tmp/` না।

**iOS-এ:**

```swift
// note-এর ছবি রাখা — Application Support-এ
let folder = URL.applicationSupportDirectory.appending(path: "attachments", directoryHint: .isDirectory)
try FileManager.default.createDirectory(at: folder, withIntermediateDirectories: true)  // নিজে থেকে থাকে না

let fileName = "\(note.id).jpg"
try imageData.write(to: folder.appending(path: fileName), options: .atomic)
// database-এ রাখুন শুধু fileName, পুরো path না
```

**ফাঁদ:**
- **পুরো path database-এ রাখবেন না।** App-এর container-এর path-এ একটা random অংশ থাকে, যেটা app update বা reinstall-এর পরে বদলাতে পারে। পুরো path রাখলে update-এর পরে সব ছবি "হারিয়ে" যায়। শুধু file-এর নাম রাখুন, আর প্রতিবার folder-এর সাথে জুড়ে নিন। Flutter-এও একই নিয়ম।
- **Application Support নিজে থেকে থাকে না।** প্রথমবার `createDirectory` করতে হয়। (`path_provider` এটা আপনার হয়ে করে দিত।)
- **বড় download করা জিনিস backup-এ পাঠাবেন না।** আবার download করা যায় এমন বড় file `Caches`-এ রাখুন, বা `isExcludedFromBackup` চালু করুন। iCloud backup ফুলিয়ে দিলে review-তে আটকাতে পারে।
- **Widget বা extension-এর সাথে data share** করতে sandbox-এর বাইরে একটা App Group container লাগে।

[উপরে ফিরুন](#toc)

### <a id="ios8-8"></a>iOS ৮.৮ সব একসাথে: offline-first repository

এবার পুরো অধ্যায় জোড়া লাগাই। Android-এর [৯.৮](#ch9-8)-এর মতোই নকশা: database হলো সত্যের উৎস, network শুধু database-কে update করে।

```swift
import Foundation
import SwiftData

@MainActor
final class OfflineFirstNotesRepository: NotesRepository {
    private let context: ModelContext
    private let api: NotesAPI

    init(context: ModelContext, api: NotesAPI) {
        self.context = context
        self.api = api
    }

    // UI সবসময় database থেকে পড়ে
    func loadNotes() async throws -> [Note] {
        let visible = FetchDescriptor<NoteEntity>(
            predicate: #Predicate { $0.markedForDeletion == false },
            sortBy: [SortDescriptor(\.updatedAt, order: .reverse)]
        )
        return try context.fetch(visible).map(\.asNote)
    }

    // আগে local — UI সাথে সাথে বদলায়। পরে server।
    func save(_ note: Note) async throws {
        try upsert(note, isSynced: false)
        try context.save()
        try? await pushPending()            // internet না থাকলে পরে আবার চেষ্টা হবে
    }

    // এখনই মুছি না — server-কে জানানো বাকি
    func delete(id: Note.ID) async throws {
        guard let entity = try entity(id: id) else { return }
        entity.markedForDeletion = true
        entity.isSynced = false
        try context.save()
        try? await pushPending()
    }

    // Pull-to-refresh আর background sync এটাই ডাকে
    func refresh() async throws {
        try await pushPending()                                  // আগে নিজের বদল পাঠাও
        let remote = try await api.fetchNotes()
        for dto in remote {
            if let local = try entity(id: dto.id), !local.isSynced { continue }  // local বদল আগে যাবে
            try upsert(dto.asNote, isSynced: true)
        }
        try context.save()
    }

    private func pushPending() async throws {
        let pending = FetchDescriptor<NoteEntity>(predicate: #Predicate { $0.isSynced == false })
        for entity in try context.fetch(pending) {
            if entity.markedForDeletion {
                try await api.delete(id: entity.id)
                context.delete(entity)                          // server জানল, এবার সত্যিই মুছি
            } else {
                try await api.upload(NoteDTO(entity.asNote))
                entity.isSynced = true
            }
        }
        try context.save()
    }

    private func entity(id: UUID) throws -> NoteEntity? {
        var descriptor = FetchDescriptor<NoteEntity>(predicate: #Predicate { $0.id == id })
        descriptor.fetchLimit = 1
        return try context.fetch(descriptor).first
    }

    private func upsert(_ note: Note, isSynced: Bool) throws {
        if let existing = try entity(id: note.id) {
            existing.title = note.title
            existing.body = note.body
            existing.updatedAt = note.updatedAt
            existing.imageURL = note.imageURL
            existing.isSynced = isSynced
        } else {
            context.insert(NoteEntity(note: note, isSynced: isSynced))
        }
    }
}
```

View model-এ শুধু একটা `refresh()` যোগ হয়, আর view-এ pull-to-refresh:

```swift
// NotesViewModel-এ
func refresh() async {
    try? await repository.refresh()      // network fail হলেও local data দেখাব
    await load()
}

// NotesScreen-এ
List(viewModel.notes) { ... }
    .refreshable { await viewModel.refresh() }   // RefreshIndicator
```

```
UI ◄── loadNotes() ── SwiftData (সত্যের উৎস) ◄── upsert ── URLSession (server)
                           ▲
                           └── save()/delete() সাথে সাথে লেখে; sync পরে —
                               refresh, pull-to-refresh, বা BGTask (iOS ৯.১)
```

**Android-এর সাথে একটা পার্থক্য:** Room-এর `Flow` query database বদলালে নিজে UI-তে নতুন data পাঠাত। এখানে view model প্রতিটা কাজের পরে নিজে `load()` করে। চাইলে `@Query` দিয়ে auto-update পাওয়া যায়, কিন্তু তখন view database-এর সাথে বাঁধা পড়ে। Test-যোগ্যতার জন্য আমরা এই সহজ পথ নিলাম।

**ফাঁদ:**
- **Server-এ মোছা note।** এই code server-এ মোছা note local থেকে সরায় না। আসল app-এ server থেকে "মোছা হয়েছে" তালিকা, বা `updatedSince` দিয়ে পরিবর্তনের তালিকা আনতে হয়।
- **Conflict।** দুই device-এ একই note বদলালে কে জিতবে? এখানে নিয়ম সহজ: local বদল আগে server-এ যায়, তারপর server-এর data আসে। দরকার হলে `updatedAt` মিলিয়ে সিদ্ধান্ত নিন। নিয়মটা যাই হোক, লিখে রাখুন।

> **মনে রাখুন**
> - `dio` → `URLSession`। 4xx/5xx-এ error আসে না — status নিজে দেখুন। Interceptor-এর জায়গায় নিজের `send()`।
> - `json_serializable` → `Codable`, compiler নিজে বানায়। Date strategy `.iso8601` দিন।
> - `drift` → SwiftData (iOS 17+)। `.watch()`-এর মতো `@Query`, কিন্তু শুধু view-এ। পুরনো code-এ Core Data।
> - `shared_preferences` → `UserDefaults` / `@AppStorage`। Secret → Keychain, যেটা uninstall-এর পরেও থাকতে পারে।
> - Database = সত্যের উৎস। File-এর পুরো path না, শুধু নাম রাখুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ আমার data layer offline-first: SwiftData হলো সত্যের উৎস, UI সবসময় database থেকে পড়ে, আর network শুধু database update করে। Network-এ URLSession আর async/await, সাথে একটা ছোট wrapper যেটা token বসায় আর status code check করে, কারণ URLSession 500-এ নিজে error দেয় না। JSON-এ Codable, token Keychain-এ। একটা জিনিস সবসময় মাথায় রাখি: Keychain-এর data uninstall-এর পরেও থাকতে পারে, তাই প্রথম launch-এ পুরনো item মুছে দিই।"
> - *English:* "My iOS data layer is offline-first: SwiftData is the source of truth, the UI always reads from the database, and the network only updates the database. For networking I use URLSession with async/await, plus a small wrapper that adds the token and checks the status code, because URLSession doesn't throw on a 500. I use Codable for JSON and the Keychain for tokens. One thing I always remember: Keychain data can survive an uninstall, so I clear old items on the first launch."

[উপরে ফিরুন](#toc)

---

## <a id="ios9"></a>iOS ৯. Plugin-এর পেছনের iOS — background, notification, permission, link

Flutter-এ কোনো plugin "Android-এ চলে, iOS-এ চলে না" — এই অভিযোগ আপনি নিশ্চয়ই শুনেছেন। Background task চলে না, push আসে না, permission চাওয়ার আগেই app crash। প্রায় সবসময় কারণ plugin না, কারণ iOS-এর নিয়ম। Android-এর [অধ্যায় ১০](#ch10)-এ নিয়মগুলো ছিল নমনীয়। iOS-এর নিয়ম কড়া, আর অনেক জায়গায় সিদ্ধান্ত পুরোপুরি OS-এর হাতে। এই অধ্যায়ে সেই নিয়মগুলো সামনাসামনি দেখব।

### <a id="ios9-1"></a>iOS ৯.১ `workmanager` → `BGTaskScheduler` (আর কেন iOS-এ এটা অন্যরকম)

**এক লাইনে:** iOS-এ আপনি background কাজ "চাইতে" পারেন, "চালাতে" পারেন না। `BGTaskScheduler`-কে বলেন "সুযোগ হলে আমাকে একটু সময় দিও"। কখন দেবে, আদৌ দেবে কি না — iOS ঠিক করে।

**আগে মূল কথাটা:** Android-এ app background-এ গেলেও কিছুক্ষণ চলতে পারে, আর WorkManager কথা দেয় যে কাজটা একসময় হবেই। iOS-এ app background-এ যাওয়ার কয়েক সেকেন্ডের মধ্যে **suspend** হয়ে যায় — memory-তে থাকে, কিন্তু একটা লাইনও চলে না ([iOS ৪](#ios4))। Background-এ code চালানোর একমাত্র পথ হলো iOS-এর দেওয়া নির্দিষ্ট কিছু দরজা।

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
Workmanager().registerPeriodicTask('sync-notes', 'syncNotes', frequency: const Duration(hours: 1));
```

**iOS-এ (SwiftUI):**

```swift
import SwiftUI
import BackgroundTasks

let notesRefreshTaskID = "com.byteonyx.notes.refresh"     // Info.plist-এ হুবহু এই নাম

func scheduleNotesRefresh() {
    let request = BGAppRefreshTaskRequest(identifier: notesRefreshTaskID)
    request.earliestBeginDate = .now.addingTimeInterval(15 * 60)   // "১৫ মিনিটের আগে না" — পরে কখন, iOS জানে
    try? BGTaskScheduler.shared.submit(request)
}

@main
struct NotesApp: App {
    @Environment(\.scenePhase) private var scenePhase
    private let repository: OfflineFirstNotesRepository
    // ... init() আগের মতো (iOS ৭.৪)

    var body: some Scene {
        WindowGroup {
            NotesScreen(repository: repository)
        }
        .onChange(of: scenePhase) { _, phase in
            if phase == .background { scheduleNotesRefresh() }    // background-এ যাওয়ার সময় অনুরোধ
        }
        .backgroundTask(.appRefresh(notesRefreshTaskID)) { [repository] in
            scheduleNotesRefresh()                    // periodic নিজে হয় না — প্রতিবার আবার চাইতে হয়
            try? await repository.refresh()           // সময় অল্প, শুধু জরুরি sync
        }
    }
}
```

`Info.plist`-এ দুইটা জিনিস লাগে:

```xml
<key>UIBackgroundModes</key>
<array>
    <string>fetch</string>          <!-- BGAppRefreshTask-এর জন্য -->
    <string>processing</string>     <!-- BGProcessingTask-এর জন্য -->
</array>
<key>BGTaskSchedulerPermittedIdentifiers</key>
<array>
    <string>com.byteonyx.notes.refresh</string>
</array>
```

**iOS-এর দরজাগুলো — কোন কাজে কী:**

| কাজ | iOS-এ কী নেবেন | কত সময় পায় | Android-এ কাছাকাছি |
|---|---|---|---|
| মাঝে মাঝে ছোট sync | `BGAppRefreshTask` | অল্প, প্রায় ৩০ সেকেন্ড | periodic WorkManager |
| লম্বা কাজ (database পরিষ্কার, বড় index) | `BGProcessingTask` | কয়েক মিনিট, সাধারণত phone idle আর charge-এ থাকলে | WorkManager + charging constraint |
| বড় file upload/download | background `URLSession` | app suspend হলেও OS নিজে transfer চালায় | WorkManager / DownloadManager |
| User নিজে শুরু করা লম্বা কাজ, progress দেখিয়ে | `BGContinuedProcessingTask` (iOS 26 থেকে) | কাজ শেষ বা user বাতিল না করা পর্যন্ত | Foreground service |
| App background-এ যাওয়ার মুহূর্তে কাজ শেষ করা | `beginBackgroundTask` | কয়েক সেকেন্ড বাড়তি | — |
| Server থেকে "data নতুন আছে" জানানো | silent push ([iOS ৯.৩](#ios9-3)) | অল্প, আর throttled | FCM data message |

**কেন Flutter-এর `workmanager` iOS-এ "অন্যরকম" আচরণ করে:**
1. **সময় iOS ঠিক করে।** User কখন app খোলে, battery, network — এসব দেখে iOS ঠিক করে কখন চালাবে। Plugin-এর docs নিজেই বলে, Background Fetch সাধারণত দিনে একবারের মতো চলে। `frequency: 1 hour` একটা ইচ্ছা মাত্র, কথা না।
2. **User swipe করে app বন্ধ করলে কিছুই চলে না।** App switcher থেকে সরালে, user আবার না খোলা পর্যন্ত কোনো background task আসে না। Android-এ শুধু Settings-এর "Force stop" এমন করত, iOS-এ সাধারণ swipe-ই যথেষ্ট।
3. **Native setup লাগে।** Info.plist-এ identifier, `UIBackgroundModes`, আর `AppDelegate`-এ register — এগুলো ছাড়া iOS task-ই দেয় না। Dart-এর task name আর Info.plist-এর identifier হুবহু না মিললে error।
4. **Background-এ আলাদা Flutter engine।** Task চলে একটা নতুন engine আর isolate-এ। অন্য plugin (Firebase, `shared_preferences`) ব্যবহার করতে `AppDelegate`-এ plugin registrant callback দিতে হয়।
5. **চলমান task থামানো যায় না,** আর সময় শেষ হলে iOS নিজে কাজ কেটে দেয়।

**Debug করার কৌশল:** Simulator বা device-এ iOS নিজের ইচ্ছায় চালাবে, তাই অপেক্ষা না করে Xcode-এ app pause করে debugger console-এ লিখুন:

```
e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"com.byteonyx.notes.refresh"]
```

**Best approach:** Notes app-এর sync-এর মূল ভরসা রাখুন foreground-এ: app খুললে, pull-to-refresh-এ, আর save-এর সাথে সাথে ([iOS ৮.৮](#ios8-8))। `BGAppRefreshTask` শুধু বাড়তি সুবিধা — হলে ভালো, না হলেও app ঠিক থাকে। বড় attachment upload → background `URLSession`।

**ফাঁদ:**
- **Task register দেরিতে করা।** Handler app launch শেষ হওয়ার আগেই register হতে হয়। SwiftUI-র `.backgroundTask` modifier এটা নিজে সামলায়। UIKit-এ `didFinishLaunchingWithOptions`-এ `BGTaskScheduler.shared.register(...)` ডাকতে হয়।
- **"আমার phone-এ চলে, user-এর phone-এ না"।** iOS শেখে user app কতটা ব্যবহার করে। কম ব্যবহার করা app কম সুযোগ পায়। এটা bug না, নকশা।
- **Exact সময়ে কাজ (reminder) background task দিয়ে না।** তার জন্য scheduled local notification ([iOS ৯.২](#ios9-2))।

[উপরে ফিরুন](#toc)

### <a id="ios9-2"></a>iOS ৯.২ Local notification — `UNUserNotificationCenter`

**এক লাইনে:** Notification-এর সব কাজ এক জায়গায় — `UNUserNotificationCenter`। Permission চাওয়া, schedule করা, বাতিল করা। Android-এর মতো channel বানাতে হয় না।

**Flutter-এ (`flutter_local_notifications`):**

```dart
await plugin
    .resolvePlatformSpecificImplementation<IOSFlutterLocalNotificationsPlugin>()
    ?.requestPermissions(alert: true, sound: true, badge: true);

await plugin.zonedSchedule(
  id: note.reminderId,
  title: 'নোট মনে করিয়ে দিচ্ছি',
  body: note.title,
  scheduledDate: tz.TZDateTime.from(remindAt, tz.local),
  notificationDetails: const NotificationDetails(iOS: DarwinNotificationDetails()),
  androidScheduleMode: AndroidScheduleMode.exactAllowWhileIdle,
);
```

**iOS-এ:**

```swift
import UserNotifications

func scheduleReminder(for note: Note, at date: Date) async throws {
    let center = UNUserNotificationCenter.current()

    // প্রথমবার system dialog দেখায়, পরে শুধু আগের উত্তর ফেরত দেয়
    let granted = try await center.requestAuthorization(options: [.alert, .sound, .badge])
    guard granted else { return }

    let content = UNMutableNotificationContent()
    content.title = "নোট মনে করিয়ে দিচ্ছি"
    content.body = note.title
    content.sound = .default
    content.userInfo = ["noteID": note.id.uuidString]     // tap করলে কোন note খুলবে

    let components = Calendar.current.dateComponents([.year, .month, .day, .hour, .minute], from: date)
    let trigger = UNCalendarNotificationTrigger(dateMatching: components, repeats: false)

    // একই identifier দিলে আগেরটা বদলে যায় — reminder edit করার সহজ পথ
    let request = UNNotificationRequest(identifier: note.id.uuidString, content: content, trigger: trigger)
    try await center.add(request)
}

// বাতিল
UNUserNotificationCenter.current().removePendingNotificationRequests(withIdentifiers: [note.id.uuidString])
```

**কী মিলল, কী আলাদা:**

| Android | iOS |
|---|---|
| Notification channel বানাতে হয় (Android 8+) | channel নেই; বিভাগ লাগলে `UNNotificationCategory` (action button-এর জন্য) |
| Android 13+ `POST_NOTIFICATIONS` runtime permission | `requestAuthorization` — শুরু থেকেই সবসময় |
| Exact alarm-এর আলাদা permission | calendar বা time-interval trigger, আলাদা permission নেই |
| App খোলা থাকলেও notification দেখায় | app সামনে থাকলে **default-এ দেখায় না** — delegate লাগে |

**App সামনে থাকলেও banner দেখাতে:**

```swift
final class NotificationDelegate: NSObject, UNUserNotificationCenterDelegate {
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification) async -> UNNotificationPresentationOptions {
        [.banner, .sound]
    }
}
// app চালুর সময়: UNUserNotificationCenter.current().delegate = notificationDelegate (strong reference রাখুন)
```

**Best approach:** Reminder → `UNCalendarNotificationTrigger`, identifier = note-এর id। Permission চান user যখন প্রথম reminder দেয়, app খোলার সাথে সাথে না।

**ফাঁদ:**
- **Pending notification-এর সীমা আছে।** Apple-এর engineer-রা forum-এ বলেছেন, একটা app একসাথে ৬৪টা pending request রাখতে পারে। প্রতিটা note-এ reminder দিলে সবচেয়ে কাছের কয়েকটাই schedule করুন, বাকিগুলো পরে।
- **Permission একবারই চাওয়া যায়।** User "Don't Allow" দিলে আর dialog আসবে না ([iOS ৯.৪](#ios9-4))।
- **Delegate weak।** `UNUserNotificationCenter`-এর `delegate` property weak। Delegate object কোথাও ধরে না রাখলে সাথে সাথে হারিয়ে যায়, আর foreground banner আসে না।

[উপরে ফিরুন](#toc)

### <a id="ios9-3"></a>iOS ৯.৩ Push notification — APNs, আর FCM-এর সাথে APNs key

**এক লাইনে:** iOS-এ সব push আসে Apple-এর server **APNs** দিয়ে। FCM ব্যবহার করলেও শেষ পথটা APNs। তাই Firebase-কে APNs-এর চাবি (APNs key) দিতে হয়।

**পথটা:**

```
আপনার server ──► FCM ──► APNs ──► iPhone (iOS নিজে দেখায়, app চালু থাকা লাগে না)
                  │        ▲
                  │        └── FCM আপনার দেওয়া .p8 key দিয়ে APNs-এ নিজের পরিচয় দেয়
                  └── FCM token → APNs device token (Firebase SDK APNs token FCM-কে দেয়, FCM server জোড়াটা রাখে)
```

Android-এ FCM message আসে Google Play Services দিয়ে। iOS-এ Google-এর কোনো পথ নেই। FCM শুধু একটা মধ্যস্থতাকারী, আসল পৌঁছানো APNs-এর কাজ।

**Flutter-এ (`firebase_messaging`):**

```dart
await FirebaseMessaging.instance.requestPermission();
final apnsToken = await FirebaseMessaging.instance.getAPNSToken();  // iOS-এ আগে এটা আসতে হয়
final fcmToken = await FirebaseMessaging.instance.getToken();
```

**iOS-এ (Firebase ছাড়া, সরাসরি APNs):**

```swift
import SwiftUI
import UIKit

final class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
        application.registerForRemoteNotifications()       // APNs-এর কাছে token চাও
        return true
    }

    func application(_ application: UIApplication,
                     didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
        let token = deviceToken.map { String(format: "%02x", $0) }.joined()
        // token আপনার server-এ পাঠান
    }

    func application(_ application: UIApplication,
                     didFailToRegisterForRemoteNotificationsWithError error: Error) {
        // Push capability নেই, বা Simulator-এ সমস্যা
    }
}

@main
struct NotesApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate   // SwiftUI-তে AppDelegate জোড়া
    // ...
}
```

**Setup — এগুলোর একটাও বাদ গেলে push আসে না:**
1. Xcode-এ target-এর **Signing & Capabilities** → **Push Notifications** যোগ করুন। এটা `aps-environment` entitlement বসায়।
2. Silent push লাগলে **Background Modes** → **Remote notifications**।
3. Apple Developer account-এ **Keys** → নতুন key, APNs চালু করে। একটা `.p8` file পাবেন। এটা **একবারই download করা যায়** — নিরাপদে রাখুন।
4. Firebase Console → Project settings → Cloud Messaging → Apple app-এ `.p8` file, Key ID আর Team ID দিন।

**APNs key (`.p8`) বনাম পুরনো certificate (`.p12`):**

| APNs auth key (`.p8`) | APNs certificate (`.p12`) |
|---|---|
| এক key দিয়ে team-এর সব app | প্রতিটা app-এর আলাদা |
| development আর production দুটোতেই | environment অনুযায়ী আলাদা হতে পারে |
| মেয়াদ শেষ হয় না (revoke না করলে) | প্রতি বছর নতুন করতে হয় |

**Best approach:** `.p8` APNs key, Firebase বা নিজের server — যেটাই হোক। Push-এর data-র ওপর ভরসা না করে, push এলে app খুলে server থেকে sync করুন।

**ফাঁদ:**
- **Silent push-এর ওপর ভরসা।** `content-available: 1` দেওয়া push (FCM-এর data-only message) iOS throttle করে, আর user swipe করে app বন্ধ করলে আসেই না। Android-এর FCM data message-এর মতো নির্ভরযোগ্য না।
- **Sandbox বনাম production।** Xcode থেকে চালানো debug build sandbox APNs-এর token পায়। TestFlight আর App Store build production-এর। ভুল environment-এ পাঠালে push হারিয়ে যায়।
- **Simulator-এ test:** আসল server ছাড়াই `xcrun simctl push booted com.byteonyx.notes payload.apns` দিয়ে একটা JSON payload পাঠানো যায়।

[উপরে ফিরুন](#toc)

### <a id="ios9-4"></a>iOS ৯.৪ `permission_handler` → Info.plist + request API

**এক লাইনে:** iOS-এ প্রতিটা permission-এর দুই অংশ: `Info.plist`-এ একটা "কেন লাগবে" লেখা (usage description), আর সেই framework-এর নিজের request function। লেখাটা না থাকলে API ছোঁয়ার সাথে সাথে **app crash করে।**

**Flutter-এ:**

```dart
final status = await Permission.camera.request();
if (status.isPermanentlyDenied) await openAppSettings();
```

**iOS-এ:** প্রথমে `Info.plist`:

```xml
<key>NSCameraUsageDescription</key>
<string>নোটে ছবি যোগ করতে camera লাগবে।</string>
```

তারপর code:

```swift
import AVFoundation

func ensureCameraAccess() async -> Bool {
    switch AVCaptureDevice.authorizationStatus(for: .video) {
    case .authorized:
        return true
    case .notDetermined:
        return await AVCaptureDevice.requestAccess(for: .video)   // এখানেই system dialog, জীবনে একবার
    case .denied, .restricted:
        return false                                              // dialog আর আসবে না
    @unknown default:
        return false
    }
}

// denied হলে Settings-এ পাঠান — কোনো View-এর ভেতরে
@Environment(\.openURL) private var openURL
Button("Settings খুলুন") {
    openURL(URL(string: UIApplication.openSettingsURLString)!)
}
```

**কোন permission, কোন key, কোন API:**

| কাজ | `Info.plist` key | Request API |
|---|---|---|
| Camera | `NSCameraUsageDescription` | `AVCaptureDevice.requestAccess(for: .video)` |
| Microphone (voice note) | `NSMicrophoneUsageDescription` | `AVAudioApplication.requestRecordPermission()` |
| পুরো photo library | `NSPhotoLibraryUsageDescription` | `PHPhotoLibrary.requestAuthorization(for: .readWrite)` |
| Location | `NSLocationWhenInUseUsageDescription` | `CLLocationManager().requestWhenInUseAuthorization()` |
| Notification | (key লাগে না) | `UNUserNotificationCenter.requestAuthorization` |
| Tracking (IDFA) | `NSUserTrackingUsageDescription` | `ATTrackingManager.requestTrackingAuthorization` |

**Photo বাছাইয়ে permission লাগে না।** SwiftUI-র `PhotosPicker` আলাদা system process-এ চলে, আর app শুধু user-এর বাছাই করা ছবি পায়। Notes app-এ ছবি যোগ করতে এটাই নিন। Flutter-এর `image_picker`-ও iOS-এ এই system picker ব্যবহার করে।

**Android-এর সাথে পার্থক্য:**

| Android ([১০.৪](#ch10-4)) | iOS |
|---|---|
| Manifest-এ `<uses-permission>` | `Info.plist`-এ usage description (user-কে দেখানো লেখা) |
| Manifest-এ না থাকলে request চুপচাপ fail | key না থাকলে **crash** |
| দুইবার deny-এর পরে আর dialog আসে না | **একবার** deny-এর পরেই আর আসে না |
| "Don't ask again" বোঝার জন্য rationale API | `authorizationStatus` দেখলেই বোঝা যায় |

**`permission_handler`-এর iOS setup কেন আলাদা:** Apple upload-এর সময় binary scan করে। App-এর code-এ camera API থাকলে, কিন্তু `Info.plist`-এ key না থাকলে, upload reject হয়। তাই plugin শুধু আপনার দরকারি permission-এর code compile করে। CocoaPods-এ এজন্য `Podfile`-এ macro লিখতে হতো। Swift Package Manager-এ plugin এখন নিজেই `Info.plist` পড়ে ঠিক করে।

**Best approach:** Permission চান ঠিক সেই মুহূর্তে, যখন user কাজটা করছে — "ছবি তুলুন" বোতাম চাপলে। Usage description-এ সত্যিকারের কারণ লিখুন, বাংলায় বা user-এর ভাষায়। "Camera access needed"-এর মতো অস্পষ্ট লেখা review-তে reject হতে পারে।

**ফাঁদ:**
- **Key ছাড়া API = crash, শুধু release-এ না, debug-এও।** Console-এ লেখা আসে: app privacy-sensitive data ছুঁতে চেয়েছে কিন্তু usage description নেই। Flutter-এ নতুন plugin যোগ করার পরে `ios/Runner/Info.plist` আপডেট করতে ভুলে গেলে ঠিক এটাই হয়।
- **User Settings থেকে permission কেড়ে নিলে iOS app-টা মেরে ফেলে।** পরের বার নতুন করে চালু হয়। তাই permission-এর অবস্থা memory-তে cache করে রাখবেন না, প্রতিবার দেখুন।

[উপরে ফিরুন](#toc)

### <a id="ios9-5"></a>iOS ৯.৫ Deep link — Universal Links বনাম custom URL scheme

**এক লাইনে:** দুই রকম link। Universal Link হলো আপনার website-এর সাধারণ `https://` link, যা app থাকলে app-এ খোলে। Custom scheme হলো `notes://` ধরনের নিজের বানানো link।

**Notes app-এ:** কেউ একটা note share করল: `https://notes.byteonyx.com/notes/42`। App install থাকলে সরাসরি note খুলবে, না থাকলে website।

**কী মিলল, কী আলাদা:**

| | Universal Link | Custom URL scheme |
|---|---|---|
| দেখতে | `https://notes.byteonyx.com/notes/42` | `notes://notes/42` |
| মালিকানা প্রমাণ | হ্যাঁ — domain-এ রাখা file দিয়ে | না — যেকোনো app একই scheme দাবি করতে পারে |
| App না থাকলে | browser-এ website খোলে | কিছুই হয় না, বা error |
| Setup | Associated Domains entitlement + website-এ file | `Info.plist`-এ `CFBundleURLTypes` |
| Android-এ যমজ | App Links (`autoVerify`) | intent-filter-এ নিজের scheme |

**Universal Link setup:**

১. Xcode → Signing & Capabilities → **Associated Domains** → `applinks:notes.byteonyx.com`।

২. Website-এ `https://notes.byteonyx.com/.well-known/apple-app-site-association` file রাখুন (`.json` extension ছাড়া, HTTPS-এ):

```json
{
  "applinks": {
    "details": [
      {
        "appIDs": ["ABCDE12345.com.byteonyx.notes"],
        "components": [
          { "/": "/notes/*" }
        ]
      }
    ]
  }
}
```

`ABCDE12345` হলো আপনার Team ID ([iOS ১১.১](#ios11-1))।

৩. App-এ link ধরুন:

```swift
WindowGroup {
    RootView()
        .onOpenURL { url in
            router.open(url)          // Universal Link আর custom scheme — দুটোই এখানে আসে
        }
}
```

**Flutter-এ:** Flutter 3.27 থেকে Flutter-এর নিজের deep link handling default-এ চালু (`FlutterDeepLinkingEnabled`)। তাই `go_router` link-টা সরাসরি route হিসেবে পায়। `app_links`-এর মতো plugin ব্যবহার করলে এই flag `NO` করতে হয়। Associated Domains আর website-এর file — এই দুই কাজ Flutter-এও হাতে করতে হয়।

**Best approach:** Share করা link আর email-এর link → Universal Link। Custom scheme শুধু OAuth login-এর redirect-এর মতো জায়গায়, যেখানে অন্য app-এর হাতে পড়ার ঝুঁকি কম।

**ফাঁদ:**
- **Apple-এর CDN file cache করে।** নতুন install-এ iOS file সরাসরি আপনার server থেকে না, Apple-এর CDN থেকে নেয়। Flutter docs বলে, CDN file আনতে ২৪ ঘণ্টা পর্যন্ত লাগতে পারে। তাই file বদলানোর পরেই কাজ না করলে আতঙ্কিত হবেন না।
- **Safari-র address bar-এ link লিখলে app খোলে না।** Universal Link কাজ করে link-এ tap করলে। Test করতে Notes বা Messages-এ link লিখে tap করুন, বা Simulator-এ `xcrun simctl openurl booted <url>`।
- **Personal (free) team-এ Associated Domains চলে না।** Paid developer account লাগে।

[উপরে ফিরুন](#toc)

### <a id="ios9-6"></a>iOS ৯.৬ `url_launcher` আর `share_plus`-এর পেছনে

**এক লাইনে:** `url_launcher` iOS-এ ভেতরে `UIApplication.open(_:)` (বা in-app browser-এর জন্য `SFSafariViewController`) ডাকে। `share_plus` ডাকে system share sheet — `UIActivityViewController`। SwiftUI-তে দুটোরই সহজ রূপ আছে।

**Flutter-এ:**

```dart
await launchUrl(Uri.parse('https://byteonyx.com/help'));
await SharePlus.instance.share(ShareParams(text: note.body, subject: note.title));
```

**iOS-এ (SwiftUI):**

```swift
struct NoteToolbar: View {
    let note: Note
    @Environment(\.openURL) private var openURL

    var body: some View {
        HStack {
            Button("সাহায্য") {
                openURL(URL(string: "https://byteonyx.com/help")!)      // default browser-এ খোলে (সাধারণত Safari)
            }
            ShareLink(item: note.body, subject: Text(note.title)) {    // share sheet
                Label("শেয়ার", systemImage: "square.and.arrow.up")
            }
        }
    }
}
```

**কী মিলল, কী আলাদা:**

| Flutter | Android ([১০.৫](#ch10-5)) | iOS |
|---|---|---|
| `launchUrl(https)` | `ACTION_VIEW` Intent | `openURL` / `UIApplication.open` |
| `LaunchMode.inAppBrowserView` | Custom Tabs | `SFSafariViewController` |
| `launchUrl(tel:)`, `mailto:` | `ACTION_DIAL`, `ACTION_SENDTO` | একই `openURL`, scheme অনুযায়ী Phone বা Mail খোলে |
| `canLaunchUrl` | `queries` element (Android 11+) | `LSApplicationQueriesSchemes` (Info.plist) |
| `share_plus` | `ACTION_SEND` + chooser | `ShareLink` / `UIActivityViewController` |

**ফাঁদ:**
- **`canLaunchUrl` iOS-এ `false` দেয়।** `https` ছাড়া অন্য scheme check করতে হলে `Info.plist`-এর `LSApplicationQueriesSchemes`-এ scheme-টা লিখতে হয়, নইলে উত্তর সবসময় `false`। `url_launcher`-এর README-তেও এটা লেখা। Android-এর `<queries>`-এর মতো।
- **iPad-এ share sheet popover।** iPad-এ share sheet একটা popover, যেটা কোনো একটা জায়গায় নোঙর করতে হয়। `share_plus`-এ এজন্য `sharePositionOrigin`। পুরনো version-এ এটা না দিলে iPad-এ crash হতো, এখন screen-এর মাঝখানে দেখায়। তবু ঠিক জায়গা দিন। SwiftUI-র `ShareLink` এটা নিজে সামলায়।

> **মনে রাখুন**
> - Background-এ iOS সিদ্ধান্ত নেয়। `BGTaskScheduler` অনুরোধ, কথা না। User swipe করে বন্ধ করলে কিছুই চলে না।
> - Notification: `UNUserNotificationCenter`, channel নেই, app সামনে থাকলে delegate ছাড়া banner নেই।
> - সব push APNs দিয়ে। FCM-এর জন্য `.p8` APNs key Firebase-এ দিন। Silent push-এ ভরসা না।
> - Permission = `Info.plist` usage description + framework-এর request API। Key না থাকলে crash। Dialog জীবনে একবার।
> - Share-যোগ্য link → Universal Link। `canLaunchUrl`-এর জন্য `LSApplicationQueriesSchemes`।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ app background-এ গেলে কয়েক সেকেন্ডে suspend হয়, তাই background কাজ হলো BGTaskScheduler-এর কাছে অনুরোধ — কখন চলবে iOS ঠিক করে, আর user app swipe করে বন্ধ করলে কিছুই চলে না। এজন্য Flutter-এর workmanager iOS-এ Android-এর মতো নির্ভরযোগ্য না, আর আমি sync-এর মূল ভরসা foreground-এ রাখি। Push সবসময় APNs দিয়ে আসে, FCM শুধু relay, তাই Firebase-এ APNs key দিতে হয়। Permission-এর জন্য Info.plist-এ usage description বাধ্যতামূলক, না থাকলে app crash করে।"
> - *English:* "On iOS an app gets suspended a few seconds after it goes to the background, so background work is a request to BGTaskScheduler — iOS decides when it runs, and nothing runs if the user swipes the app away. That's why Flutter's workmanager isn't as reliable on iOS as on Android, and I keep the main sync in the foreground. Push always goes through APNs; FCM is only a relay, so Firebase needs the APNs key. For permissions, the usage description in Info.plist is mandatory — without it the app crashes."

[উপরে ফিরুন](#toc)

---

## <a id="ios10"></a>iOS ১০. Testing

Test-এর দর্শন বদলায় না: fake ভালো, mock কম, behaviour test করুন। iOS-এ নতুন যা, তা হলো দুইটা test framework পাশাপাশি। পুরনো **XCTest**, আর নতুন **Swift Testing** (Xcode 16, ২০২৪ থেকে)। নতুন unit test Swift Testing-এ লিখুন। XCTest চিনে রাখুন — UI test আর পুরনো code-এ এখনো ওটাই।

### <a id="ios10-1"></a>iOS ১০.১ হাতিয়ারের নাম বদল

| Flutter | Android | iOS |
|---|---|---|
| `test()` | JUnit `@Test` | Swift Testing `@Test` |
| `group()` | test class / `@Nested` | `@Suite` struct |
| `expect(a, equals(b))` | `assertEquals(b, a)` | `#expect(a == b)` |
| `setUp()` | `@Before` | suite-এর `init()` |
| `bloc_test` | `runTest` + Turbine | `async` test — `await` করে তারপর property দেখা |
| `fake_async` | `runTest` virtual time | built-in নেই; সময় inject করুন ([নিয়ম](#ios10-3)) |
| `mocktail` | Fake, দরকারে MockK | Fake class (protocol দিয়ে) — mock library কম চলে |
| `testWidgets` | Compose UI test | সরাসরি মিল নেই — view model test + XCUITest |
| golden test | Roborazzi / Paparazzi | swift-snapshot-testing (third-party) |
| `integration_test` | instrumented test | XCUITest |
| `flutter test` | `./gradlew test` | Xcode-এ ⌘U, বা `xcodebuild test` |

**কোথায় থাকে:** Xcode project-এ test আলাদা **target**। Unit test-এর target (যেমন `NotesTests`) আর UI test-এর target (`NotesUITests`)। Flutter project-এর `ios/RunnerTests/` folder-টাও এরকম একটা native test target — platform channel বা plugin-এর Swift code test করার জন্য। Flutter-এর template এই target এখনো XCTest দিয়ে শুরু করে (`RunnerTests: XCTestCase`); চাইলে পাশে Swift Testing-এর test যোগ করা যায়।

[উপরে ফিরুন](#toc)

### <a id="ios10-2"></a>iOS ১০.২ Swift Testing: `@Test` আর `#expect`

**এক লাইনে:** যেকোনো function-এর গায়ে `@Test` দিলেই সেটা test। Check করতে একটাই macro — `#expect`। Fail হলে macro নিজেই দেখায় কোন দিকে কোন value ছিল।

**Flutter-এ:**

```dart
test('snake_case JSON থেকে note decode হয়', () {
  final dto = NoteDto.fromJson(jsonDecode(sampleJson));
  expect(dto.title, 'বাজার');
  expect(dto.imageUrl, isNull);
});
```

**iOS-এ:**

```swift
import Foundation
import Testing
@testable import Notes                 // internal জিনিসও test-এ দেখা যাবে

struct NoteDTOTests {

    @Test("snake_case JSON থেকে note decode হয়")
    func decodesSnakeCase() throws {
        let json = Data("""
        {"id": "6F9619FF-8B86-D011-B42D-00CF4FC964FF",
         "title": "বাজার", "body": "ডিম, দুধ",
         "updated_at": "2026-11-10T09:30:00Z"}
        """.utf8)
        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601

        let dto = try decoder.decode(NoteDTO.self, from: json)    // throw করলে test fail

        #expect(dto.title == "বাজার")
        #expect(dto.imageURL == nil)
    }

    @Test("ফাঁকা note চেনা যায়", arguments: ["", "   ", "\n"])  // একটা test, তিনটা input
    func blankNote(title: String) {
        let note = Note(id: UUID(), title: title, body: "", updatedAt: .now, imageURL: nil)
        #expect(note.isBlank)
    }
}
```

এখানে `isBlank` ধরে নিচ্ছি `Note`-এর একটা ছোট computed property:

```swift
extension Note {
    var isBlank: Bool {
        title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty &&
        body.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }
}
```

**কয়েকটা দরকারি জিনিস:**
- **`#require`** — না মিললে test সেখানেই থামায়। Optional খুলতেও কাজের: `let first = try #require(notes.first)`। XCTest-এর `XCTUnwrap`-এর মতো।
- **`arguments:`** — parameterized test। প্রতিটা input আলাদা test হিসেবে report হয়।
- **`@Suite`** আর struct-এর `init()` — প্রতিটা test নতুন একটা instance পায়। তাই `init`-ই আপনার `setUp`, আর test-দের মধ্যে state ভাগ হয় না।
- **Parallel default-এ।** Apple-এর docs বলে, Swift Testing suite-এর সব test default-এ parallel চালায়, XCTest একটার পর একটা চালাত। Global state ভাগ করলে test এলোমেলো fail করবে।

**Best approach:** নতুন unit test Swift Testing-এ। একটা test, একটা behaviour। নাম বাক্যে, বাংলায় লেখা যায়।

[উপরে ফিরুন](#toc)

### <a id="ios10-3"></a>iOS ১০.৩ `bloc_test` → `@Observable` view model test

**এক লাইনে:** View model-এর method `async`, তাই test-এ শুধু `await` করুন, তারপর property দেখুন। State-এর stream নেই, তাই Turbine বা `bloc_test`-এর `expect` list লাগে না।

**Flutter-এ:**

```dart
blocTest<NotesCubit, NotesState>(
  'মোছা fail হলে error দেখায়, list অক্ষত থাকে',
  build: () => NotesCubit(FakeNotesRepository(notes: [sampleNote], failOnDelete: true)),
  seed: () => NotesState(notes: [sampleNote]),
  act: (cubit) => cubit.delete(sampleNote),
  expect: () => [NotesState(notes: [sampleNote], error: 'মোছা যায়নি')],
);
```

**iOS-এ — আগে fake আর sample:**

```swift
// app target-এ রাখুন — Preview-ও এটা ব্যবহার করে (iOS ৭.৩)
extension Note {
    static let sample = Note(
        id: UUID(), title: "বাজারের তালিকা", body: "ডিম, দুধ", updatedAt: .now, imageURL: nil
    )
}

// test target-এ
enum FakeError: Error { case failed }

@MainActor
final class FakeNotesRepository: NotesRepository {
    private(set) var notes: [Note]
    private let failOnDelete: Bool

    init(notes: [Note] = [], failOnDelete: Bool = false) {
        self.notes = notes
        self.failOnDelete = failOnDelete
    }

    func loadNotes() async throws -> [Note] { notes }
    func save(_ note: Note) async throws { notes.append(note) }
    func refresh() async throws { }

    func delete(id: Note.ID) async throws {
        if failOnDelete { throw FakeError.failed }
        notes.removeAll { $0.id == id }
    }
}
```

**তারপর test:**

```swift
import Testing
@testable import Notes

@MainActor                                   // view model main actor-এ, test-ও সেখানে
struct NotesViewModelTests {

    @Test("load করলে repository-র note দেখায়")
    func loadShowsNotes() async {
        let viewModel = NotesViewModel(repository: FakeNotesRepository(notes: [.sample]))

        await viewModel.load()

        #expect(viewModel.notes == [.sample])
        #expect(viewModel.isLoading == false)
    }

    @Test("মোছা fail হলে error দেখায়, list অক্ষত থাকে")
    func failedDeleteKeepsList() async {
        let viewModel = NotesViewModel(
            repository: FakeNotesRepository(notes: [.sample], failOnDelete: true)
        )
        await viewModel.load()

        await viewModel.delete(.sample)

        #expect(viewModel.errorMessage == "মোছা যায়নি")
        #expect(viewModel.notes == [.sample])
    }

    @Test("মোছা সফল হলে note list থেকে সরে যায়")
    func deleteRemovesNote() async {
        let repository = FakeNotesRepository(notes: [.sample])
        let viewModel = NotesViewModel(repository: repository)
        await viewModel.load()

        await viewModel.delete(.sample)

        #expect(viewModel.notes.isEmpty)
        #expect(repository.notes.isEmpty)    // repository-ও সত্যিই মুছেছে
    }
}
```

**কী মিলল, কী আলাদা:**

| `bloc_test` | Android (Turbine) | iOS |
|---|---|---|
| `build:` | ViewModel তৈরি | `NotesViewModel(repository: fake)` |
| `act:` | method call | `await viewModel.delete(...)` |
| `expect: [state1, state2]` | `awaitItem()` এক এক করে | `#expect` শেষ অবস্থার ওপর |
| `fake_async` | `runTest` | নেই — সময় `init`-এ inject করুন |
| `MainDispatcherRule` লাগে না | লাগে | লাগে না — test নিজেই `@MainActor` |

**মাঝের state দেখতে চাইলে?** `bloc_test` সব state-এর ক্রম দেখাত, যেমন loading `true` তারপর `false`। এখানে `await`-এর পরে শুধু শেষ অবস্থা থাকে। মাঝের অবস্থা দেখতে fake-এ একটা "দরজা" লাগে — fake `loadNotes()`-এ থেমে থাকবে যতক্ষণ test না ছাড়ে। বেশিরভাগ ক্ষেত্রে শেষ অবস্থা দেখাই যথেষ্ট, আর সেটাই behaviour।

**সময় (`fake_async`-এর জায়গায়):** View model-এ `Date.now` বা `Task.sleep` সরাসরি না লিখে, `init`-এ একটা `now: () -> Date` বা `Clock` নিন। Test-এ নির্দিষ্ট সময় দিন। এতে test-এ সত্যিকারের অপেক্ষা থাকে না।

**ফাঁদ:**
- **`.task`-এর ভেতরের কাজ test করা।** `.task` view-এর অংশ, view model-এর না। Logic view model-এর method-এ রাখুন, view শুধু ডাকবে। তখন test সরাসরি method ডাকতে পারে।
- **`Task { }` দিয়ে method-এর ভেতরে কাজ পাঠিয়ে দেওয়া।** `func delete()` যদি ভেতরে `Task { ... }` চালায় আর নিজে সাথে সাথে ফেরে, test-এর `await` কিছুর জন্য অপেক্ষা করে না। Method `async` রাখুন, `Task` বানাক view।

[উপরে ফিরুন](#toc)

### <a id="ios10-4"></a>iOS ১০.৪ XCTest — চিনে রাখুন

**এক লাইনে:** পুরনো framework। Class-ভিত্তিক, `test` দিয়ে শুরু হওয়া method, আর অনেক রকম `XCTAssert...`।

```swift
import XCTest
@testable import Notes

final class NotesViewModelXCTests: XCTestCase {

    @MainActor
    func testLoadShowsNotes() async {
        let viewModel = NotesViewModel(repository: FakeNotesRepository(notes: [.sample]))

        await viewModel.load()

        XCTAssertEqual(viewModel.notes, [.sample])
        XCTAssertFalse(viewModel.isLoading)
    }
}
```

| XCTest | Swift Testing |
|---|---|
| `XCTestCase` subclass | যেকোনো struct, `@Suite` ঐচ্ছিক |
| method-এর নাম `test...` দিয়ে শুরু | `@Test` attribute |
| `setUp()` / `tearDown()` | `init()` / `deinit` (suite class হলে) |
| `XCTAssertEqual`, `XCTAssertTrue`, `XCTAssertNil` ... | শুধু `#expect(...)` |
| `XCTUnwrap` | `#require` |
| `XCTestExpectation` + `wait(for:)` | `async` test, বা `confirmation` |
| default-এ একটার পর একটা | default-এ parallel |
| UI test, performance test (`measure`) | — (এগুলো XCTest-এই থাকে) |

দুইটা একই target-এ, এমনকি একই file-এ পাশাপাশি থাকতে পারে। তাই পুরনো test একবারে বদলানোর দরকার নেই।

[উপরে ফিরুন](#toc)

### <a id="ios10-5"></a>iOS ১০.৫ `integration_test` → XCUITest

**এক লাইনে:** XCUITest আপনার app-কে একটা আলাদা process থেকে চালায়, আর user-এর মতো tap ও type করে। App-এর ভেতরের কিছু দেখতে পায় না, শুধু accessibility-র মাধ্যমে screen-এর জিনিস।

**Flutter-এ:**

```dart
testWidgets('নতুন note list-এ আসে', (tester) async {
  app.main();
  await tester.pumpAndSettle();
  await tester.tap(find.byKey(const Key('addNote')));
  await tester.pumpAndSettle();
  await tester.enterText(find.byKey(const Key('noteTitle')), 'বাজারের তালিকা');
  await tester.tap(find.byKey(const Key('save')));
  await tester.pumpAndSettle();
  expect(find.text('বাজারের তালিকা'), findsOneWidget);
});
```

**iOS-এ — app-এর দিকে identifier দিন (Flutter-এর `Key`-এর মতো):**

```swift
Button("নতুন নোট", systemImage: "plus") { showEditor = true }
    .accessibilityIdentifier("addNote")

TextField("শিরোনাম", text: $title)
    .accessibilityIdentifier("noteTitle")
```

**Test:**

```swift
import XCTest

final class NotesUITests: XCTestCase {

    @MainActor
    func testNewNoteAppearsInList() throws {
        let app = XCUIApplication()
        app.launchArguments = ["-ui-testing"]      // app এটা দেখে in-memory database নেবে
        app.launch()

        app.buttons["addNote"].tap()
        let title = app.textFields["noteTitle"]
        title.tap()
        title.typeText("বাজারের তালিকা")
        app.buttons["save"].tap()

        XCTAssertTrue(app.staticTexts["বাজারের তালিকা"].waitForExistence(timeout: 2))
    }
}
```

App-এর দিকে launch argument দেখে test-এর জন্য খালি database:

```swift
let isUITesting = ProcessInfo.processInfo.arguments.contains("-ui-testing")
let config = ModelConfiguration(isStoredInMemoryOnly: isUITesting)
container = try ModelContainer(for: NoteEntity.self, configurations: config)
```

**কী মিলল, কী আলাদা:**

| `integration_test` | XCUITest |
|---|---|
| একই process-এ, app-এর code ছোঁয়া যায় | আলাদা process — শুধু screen দেখা যায় |
| `find.byKey` | `app.buttons["id"]` (accessibility identifier) |
| `pumpAndSettle()` | `waitForExistence(timeout:)` |
| fake inject করা সহজ | launch argument বা environment দিয়ে app-কে বলতে হয় |

**Best approach:** অনেক view model test, অল্প কয়েকটা XCUITest — শুধু সবচেয়ে জরুরি পথে (নতুন note লেখা, খোলা, মোছা)। XCUITest ধীর আর ভঙ্গুর।

**ফাঁদ:**
- **Text দিয়ে খোঁজা।** Bangla text বদলালে বা ভাষা বদলালে test ভাঙে। `accessibilityIdentifier` দিন — user দেখে না, VoiceOver-ও পড়ে না।
- **আসল network-এ UI test।** Server ধীর হলে test flaky। Launch argument দিয়ে fake API বা in-memory data দিন।

> **মনে রাখুন**
> - নতুন unit test Swift Testing-এ: `@Test`, `#expect`, `#require`। Default-এ parallel।
> - View model test = fake repository দিয়ে বানান, `await` method, তারপর `#expect`। Turbine লাগে না।
> - XCTest চিনে রাখুন। UI test আর performance test এখনো XCTest-এ।
> - XCUITest আলাদা process থেকে চালায়। `accessibilityIdentifier` = Flutter-এর `Key`।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "নতুন unit test আমি Swift Testing-এ লিখি — @Test আর #expect, আর এটা default-এ parallel চলে। View model-এর method async, তাই test-এ fake repository দিয়ে view model বানাই, method await করি, তারপর property check করি; bloc_test-এর মতো state-এর stream লাগে না। UI test-এর জন্য XCUITest, যেটা app-কে আলাদা process থেকে accessibility identifier দিয়ে চালায়। Flutter-এর integration_test-এর মতো, কিন্তু black-box।"
> - *English:* "I write new unit tests with Swift Testing — @Test and #expect — and they run in parallel by default. View model methods are async, so in a test I build the view model with a fake repository, await the method, and then check its properties; I don't need a state stream like in bloc_test. For UI tests I use XCUITest, which drives the app from a separate process through accessibility identifiers. It's like Flutter's integration_test, but black-box."

[উপরে ফিরুন](#toc)

---

## <a id="ios11"></a>iOS ১১. Signing আর release — certificate থেকে App Store

Android-এ release মানে ছিল একটা keystore, একটা AAB, আর Play Console ([অধ্যায় ১২](#ch12))। iOS-এ টুকরো বেশি: bundle id, team, certificate, provisioning profile, entitlement। প্রথমবার এগুলো গোলমেলে লাগে। কিন্তু একবার বুঝলে দেখবেন, প্রতিটার কাজ একটাই, আর সবাই মিলে একটা প্রশ্নের উত্তর দেয়: "কে, কোন app, কোন device-এ, কী কী ক্ষমতা নিয়ে চালাতে পারবে?"

### <a id="ios11-1"></a>iOS ১১.১ পাঁচ টুকরো: bundle id, team, certificate, provisioning profile, entitlement

**এক লাইনে:** Certificate বলে **কে** sign করছে। Provisioning profile বলে **কোন app, কোন device-এ, কোন ক্ষমতা নিয়ে** চলবে। iOS দুটোই মিলিয়ে দেখে, তবেই app চালায়।

| টুকরো | কী | Android-এ কাছাকাছি |
|---|---|---|
| **Bundle ID** | app-এর স্থায়ী নাম, যেমন `com.byteonyx.notes` | `applicationId` |
| **Team** | আপনার Apple Developer account (একজন বা একটা company)। একটা ১০ অক্ষরের **Team ID** থাকে | Play Console developer account |
| **Certificate** | Apple-এর দেওয়া পরিচয়পত্র। Private key থাকে আপনার Mac-এর Keychain-এ | upload keystore |
| **Provisioning profile** | Apple-এর sign করা একটা file: এই App ID + এই certificate + (development-এ) এই device-গুলো + এই entitlement | মিল নেই |
| **Entitlement** | app-এর বিশেষ ক্ষমতা: push, Associated Domains, iCloud, App Groups | Manifest-এর কিছু permission আর feature |

**Certificate দুই রকম:**
- **Apple Development** — নিজের phone-এ Xcode থেকে চালানোর জন্য।
- **Apple Distribution** — TestFlight আর App Store-এর জন্য।

**Provisioning profile কয়েক রকম:**
- **Development** — নির্দিষ্ট কিছু registered device-এ, debug-এর জন্য।
- **Ad Hoc** — নির্দিষ্ট device-এ (সর্বোচ্চ ১০০টা প্রতি ধরনের device) release build দেওয়া।
- **App Store Connect** — TestFlight আর App Store। Device-এর তালিকা নেই, Apple নিজে বিতরণ করে।
- **Enterprise** — শুধু Enterprise Program-এর company, নিজেদের কর্মীদের জন্য।

**ভেতরে কীভাবে কাজ করে:** Build-এর সময় Xcode আপনার certificate-এর private key দিয়ে app-এর প্রতিটা binary sign করে, আর profile-টা app-এর ভেতরে `embedded.mobileprovision` নামে রেখে দেয়। Install-এর সময় iOS দেখে: signature কি profile-এর কোনো certificate-এর সাথে মেলে? Bundle ID কি মেলে? Device কি তালিকায় আছে? চাওয়া entitlement কি profile-এ অনুমোদিত? একটাও না মিললে app install বা launch হয় না।

**Android-এর সাথে সবচেয়ে বড় পার্থক্য:** Android-এ signing key-ই app-এর পরিচয়। Key হারালে (Play App Signing না থাকলে) আর update দেওয়া যায় না। iOS-এ app-এর পরিচয় হলো **Bundle ID + Team**। Distribution certificate হারালে বা মেয়াদ শেষ হলে নতুন একটা বানান — App Store-এর app-এর কিছুই হয় না। Certificate প্রতি বছর বদলায়, এটা স্বাভাবিক।

**ফাঁদ:**
- **Free Apple ID দিয়ে চালানো।** Paid account (বছরে $99) ছাড়াও নিজের phone-এ চালানো যায়, কিন্তু profile ৭ দিনে শেষ হয়, আর push, Associated Domains-এর মতো capability পাওয়া যায় না।
- **Capability Xcode-এ যোগ করে ভুলে যাওয়া যে profile-ও বদলাতে হয়।** Automatic signing এটা নিজে করে। Manual-এ নতুন profile বানাতে হয়, নইলে "entitlement profile-এ নেই" error।

[উপরে ফিরুন](#toc)

### <a id="ios11-2"></a>iOS ১১.২ Automatic বনাম manual signing

**এক লাইনে:** Automatic signing-এ Xcode নিজে certificate আর profile বানায় ও নবায়ন করে। Manual-এ আপনি নিজে বেছে দেন। নিজের Mac-এ automatic, CI-তে সাধারণত manual।

**Flutter-এ:** `ios/Runner.xcworkspace` Xcode-এ খুলে Runner target → **Signing & Capabilities**-এ "Automatically manage signing" টিক দিয়ে Team বেছে নেওয়া — এটাই আপনি সম্ভবত করেছেন। Flutter-এর docs বলে, এটা default-এ চালু, আর বেশিরভাগ app-এর জন্য যথেষ্ট।

| | Automatic | Manual |
|---|---|---|
| কে বানায় | Xcode, Apple account-এ login করে | আপনি, developer portal-এ বা tool দিয়ে |
| নতুন capability যোগ | Xcode নিজে profile আপডেট করে | নতুন profile বানাতে হয় |
| কোথায় ভালো | নিজের Mac, ছোট team | CI server, বড় team, একাধিক flavor |

**CI-তে কী হয়:** CI machine-এ কেউ Xcode-এ login করে না। তাই দুই পথ:
- **App Store Connect API key** দিয়ে `xcodebuild`-কে automatic signing করতে দেওয়া।
- **fastlane match** — certificate আর profile একটা encrypted git repo-তে রেখে সব machine-এ একই জিনিস বসানো। Codemagic-এর মতো CI নিজেও এই কাজের tool দেয়।

**Best approach:** নিজের কাজে automatic signing। CI-তে App Store Connect API key, অথবা team বড় হলে fastlane match।

[উপরে ফিরুন](#toc)

### <a id="ios11-3"></a>iOS ১১.৩ Archive → TestFlight → App Store

**এক লাইনে:** Release build-কে iOS-এ বলে **archive**। Archive থেকে একটা `.ipa` বানিয়ে App Store Connect-এ upload করেন। তারপর TestFlight-এ test, শেষে review-তে পাঠানো।

**ধাপগুলো:**

1. **App Store Connect-এ app তৈরি।** Bundle ID বেছে নিন, নাম, ভাষা, SKU দিন। (Play Console-এ নতুন app বানানোর মতো।)
2. **Version আর build number।** `CFBundleShortVersionString` = দেখানো version (`1.2.0`)। `CFBundleVersion` = build number, প্রতিটা upload-এ বাড়াতে হয়। Flutter-এ `pubspec.yaml`-এর `version: 1.2.0+5` → `1.2.0` আর `5`।
3. **Archive।** Xcode → Product → Archive (device বা "Any iOS Device" বেছে নিয়ে)। ফল একটা `.xcarchive` — ভেতরে app আর debug symbol (dSYM)।
4. **Distribute।** Xcode Organizer → Distribute App → App Store Connect। Xcode distribution certificate দিয়ে আবার sign করে upload করে।
5. **Processing।** Upload-এর পরে Apple কিছুক্ষণ build "process" করে। তারপর TestFlight-এ দেখা যায়।
6. **TestFlight।**
   - **Internal tester:** আপনার App Store Connect team-এর সর্বোচ্চ ১০০ জন। Review লাগে না।
   - **External tester:** সর্বোচ্চ ১০,০০০ জন, email বা public link দিয়ে। প্রথম build-এ Beta App Review লাগতে পারে।
   - প্রতিটা build upload-এর পর ৯০ দিন test করা যায়।
7. **Submit for Review।** Screenshot, বিবরণ, privacy তথ্য, আর review-এর জন্য একটা demo account দিন। তারপর review।
8. **Release।** Approve হলে নিজে release করুন, নির্দিষ্ট দিনে, বা ধীরে ধীরে (phased release, ৭ দিনে সবাই)।

**কী মিলল:**

| Google Play | App Store |
|---|---|
| Play Console | App Store Connect |
| AAB upload | archive থেকে `.ipa` upload |
| `versionName` / `versionCode` | `CFBundleShortVersionString` / `CFBundleVersion` |
| Internal testing track | TestFlight internal |
| Closed / open testing | TestFlight external |
| Staged rollout (%) | Phased release (৭ দিন) |
| review (সাধারণত দ্রুত, স্বয়ংক্রিয় বেশি) | মানুষের review, প্রতিটা version-এ |

**Xcode version-এর নিয়ম (নভেম্বর ২০২৬):** Apple-এর "Upcoming Requirements" পাতা অনুযায়ী, ২৮ এপ্রিল ২০২৬ থেকে App Store Connect-এ upload করতে Xcode 26 বা নতুন, আর iOS 26 SDK লাগে। Xcode 27 বের হয়েছে ১৪ সেপ্টেম্বর ২০২৬-এ। Apple প্রতি বছর বসন্তে নিয়মটা এক ধাপ তোলে, তাই upload-এর আগে [এই পাতাটা](https://developer.apple.com/news/upcoming-requirements/) দেখে নিন। একই পাতা বলে, ৯ সেপ্টেম্বর ২০২৬ থেকে upload করা app-এর minimum iOS 13 বা তার বেশি হতে হবে।

**ফাঁদ:**
- **একই build number দুইবার।** একই version-এ একই build number আবার upload করা যায় না। Flutter-এ `+5`-কে `+6` করুন, বা `--build-number` দিন।
- **Export compliance-এর প্রশ্ন প্রতিবার।** App শুধু HTTPS-এর মতো সাধারণ encryption ব্যবহার করলে `Info.plist`-এ `ITSAppUsesNonExemptEncryption` = `NO` দিন। তাহলে প্রতি build-এ প্রশ্নটা আসে না।
- **dSYM হারানো।** Crash report পড়তে archive-এর dSYM লাগে। Crashlytics ব্যবহার করলে সেটা upload হচ্ছে কি না দেখুন। Flutter-এ Dart-এর জন্য আলাদা `--split-debug-info`-এর symbol রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ios11-4"></a>iOS ১১.৪ Review guideline-এর যে নিয়মে সবাই আটকায়

**এক লাইনে:** App Store-এ প্রতিটা version একজন মানুষ review করে, Apple-এর [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) ধরে। Flutter developer-রা সাধারণত এই কয়েকটা নিয়মে আটকায়।

**১. Digital জিনিস বিক্রি = In-App Purchase (guideline 3.1.1)।** App-এর ভেতরে feature বা content খোলার জন্য — subscription, premium note theme, "Pro" version — In-App Purchase (StoreKit) ব্যবহার করতেই হবে। নিজের payment, license key, QR code দিয়ে খোলা নিষেধ। Flutter-এর `in_app_purchase` plugin iOS-এ ভেতরে StoreKit-ই চালায়।
- Physical জিনিস বা app-এর বাইরে ব্যবহার করা service (খাবার, taxi) — IAP লাগে না।
- **দেশভেদে বদলাচ্ছে।** এখনকার guideline বলে, **United States storefront**-এ বাইরের payment-এর link বা button দেওয়া যায়। অন্য দেশে নিয়ম আলাদা, আর EU-তে আলাদা ব্যবস্থা আছে। এই অংশ ঘন ঘন বদলায়, submit-এর আগে guideline-টা আবার পড়ুন।

**২. Login service (guideline 4.8) — Sign in with Apple-এর নিয়ম।** আগে নিয়ম ছিল: Google বা Facebook login দিলে Sign in with Apple-ও দিতেই হবে। **জানুয়ারি ২০২৪-এ নিয়মটা বদলেছে।** এখন guideline বলে: third-party বা social login দিয়ে user-এর মূল account বানালে, পাশাপাশি **আরেকটা সমান login option** দিতে হবে, যেটা:
- শুধু নাম আর email নেয়,
- user-কে email লুকিয়ে রাখতে দেয়,
- অনুমতি ছাড়া advertising-এর জন্য user-এর কাজকর্ম সংগ্রহ করে না।

Sign in with Apple এই তিন শর্ত পূরণ করে, তাই এটাই সবচেয়ে সহজ উত্তর। শুধু নিজের email-password login থাকলে, বা enterprise/education account-এর app হলে, এটা লাগে না।

**৩. Account বানানো গেলে মোছাও যেতে হবে (guideline 5.1.1(v))।** App-এ account খোলা গেলে, app-এর ভেতর থেকেই account delete করার পথ দিতে হবে। শুধু "email করুন" যথেষ্ট না।

**৪. আরও কয়েকটা সাধারণ কারণ:**
- **Crash বা অসম্পূর্ণ app (2.1)।** Review-এর device-এ crash করলে reject। Demo account কাজ না করলেও।
- **শুধু একটা website-এর মোড়ক (4.2)।** WebView-এ website দেখানো ছাড়া কিছু না করলে "minimum functionality"-তে reject।
- **Permission-এর লেখা অস্পষ্ট।** Usage description-এ কেন লাগবে, স্পষ্ট লিখুন ([iOS ৯.৪](#ios9-4))।

**Best approach:** প্রথম submit-এর আগে guideline-এর 2, 3.1, 4.8, 5.1 অংশ নিজে একবার পড়ুন। Review notes-এ demo account আর কোন feature কোথায়, লিখে দিন।

[উপরে ফিরুন](#toc)

### <a id="ios11-5"></a>iOS ১১.৫ Privacy manifest আর nutrition label

**এক লাইনে:** দুইটা আলাদা জিনিস। **Privacy manifest** (`PrivacyInfo.xcprivacy`) হলো app-এর ভেতরের একটা file, যেটা বলে code কী data নেয় আর কোন "সংবেদনশীল" API কেন ব্যবহার করে। **Nutrition label** হলো App Store-এর পাতায় user-কে দেখানো privacy-র সারাংশ, যেটা আপনি App Store Connect-এর "App Privacy" অংশে পূরণ করেন।

**Privacy manifest-এ কী থাকে:**

| Key | মানে |
|---|---|
| `NSPrivacyTracking` | app কি user-কে track করে (অন্য company-র data-র সাথে মিলিয়ে) |
| `NSPrivacyTrackingDomains` | tracking-এর জন্য কোন কোন domain-এ যায় |
| `NSPrivacyCollectedDataTypes` | কী কী data সংগ্রহ করে, আর কেন |
| `NSPrivacyAccessedAPITypes` | কোন "required reason API" ব্যবহার করে, আর কারণের code |

**Required reason API:** কিছু API দিয়ে device চেনা (fingerprinting) সম্ভব, তাই Apple কারণ জানতে চায়। যেমন `UserDefaults`, file-এর timestamp, system boot time, disk-এর খালি জায়গা। Notes app `UserDefaults` ব্যবহার করে নিজের setting রাখতে — কারণের code `CA92.1` ("শুধু app নিজের জন্য পড়া-লেখা")।

```xml
<key>NSPrivacyAccessedAPITypes</key>
<array>
    <dict>
        <key>NSPrivacyAccessedAPIType</key>
        <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
        <key>NSPrivacyAccessedAPITypeReasons</key>
        <array>
            <string>CA92.1</string>
        </array>
    </dict>
</array>
```

**কবে থেকে বাধ্যতামূলক:** Apple-এর পাতা অনুযায়ী ১ মে ২০২৪ থেকে, নতুন app বা update upload করতে required reason API-র কারণ ঘোষণা করতে হয় — third-party SDK-র ব্যবহারও এর মধ্যে। Apple-এর তালিকায় থাকা জনপ্রিয় SDK-কে নিজের privacy manifest আর signature নিয়ে আসতে হয়।

**Flutter-এ:** Flutter engine আর বেশিরভাগ বড় plugin (যেমন `shared_preferences`, Firebase) নিজের manifest নিয়ে আসে। আপনার Runner-এর নিজের code কোনো required reason API ছুঁলে, Xcode-এ File → New → File → **App Privacy** দিয়ে `PrivacyInfo.xcprivacy` যোগ করুন। Archive-এর পরে Xcode Organizer-এ **Generate Privacy Report** দিলে সব manifest মিলিয়ে একটা report পাবেন — nutrition label পূরণের সময় কাজে লাগে।

**Nutrition label:** App Store Connect → আপনার app → App Privacy। কোন data নেন (email, crash data, usage data), সেটা user-এর সাথে জোড়া কি না, tracking-এ ব্যবহার হয় কি না। এখানে **আপনার SDK-র সংগ্রহও** লিখতে হয় — Firebase Analytics, Crashlytics। Android-এ ঠিক এই কাজ Play Console-এর **Data safety** form।

**Tracking করলে আরেকটা নিয়ম:** অন্য company-র data-র সাথে মিলিয়ে user-কে track করলে (যেমন advertising ID দিয়ে), আগে App Tracking Transparency (ATT) dialog দিয়ে অনুমতি নিতে হয় ([iOS ৯.৪](#ios9-4)-এর `NSUserTrackingUsageDescription`)।

**ফাঁদ:** Manifest, nutrition label আর app-এর আসল আচরণ — তিনটা না মিললে review-তে প্রশ্ন ওঠে। নতুন SDK যোগ করলে তিনটাই আবার দেখুন।

[উপরে ফিরুন](#toc)

### <a id="ios11-6"></a>iOS ১১.৬ `flutter build ipa` ভেতরে কী করে

**এক লাইনে:** `flutter build ipa` আসলে Xcode-এর দুইটা command চালায়: `xcodebuild archive` আর `xcodebuild -exportArchive`। মাঝখানে Xcode-এর একটা build phase Flutter tool-কে ডেকে Dart code compile করায়।

**ধাপে ধাপে:**

1. **Flutter tool প্রস্তুতি নেয়।** `pub get` চালায়। `ios/Flutter/Generated.xcconfig` লেখে — এতে Flutter SDK-র path, `FLUTTER_BUILD_NAME`, `FLUTTER_BUILD_NUMBER` থাকে। Plugin-এর তালিকা থেকে `GeneratedPluginRegistrant` বানায়। Swift Package Manager চালু থাকলে (Flutter 3.44 থেকে default) plugin-গুলো `FlutterGeneratedPluginSwiftPackage` নামে একটা package-এ জোড়া হয়। যে plugin SPM সমর্থন করে না, তার জন্য CocoaPods-এ fallback, `pod install`।
2. **`xcodebuild archive`** — `Runner.xcworkspace`, Release configuration:
   - Runner target-এর একটা **Run Script** phase `xcode_backend.sh build` চালায়। এটা `flutter assemble`-কে ডাকে: Dart → kernel (`app.dill`) → `gen_snapshot` → ARM64 machine code → `App.framework/App`। Image আর font যায় `App.framework/flutter_assets/`-এ।
   - `swiftc` আপনার `AppDelegate`, `SceneDelegate` আর plugin-এর Swift code compile করে। Objective-C থাকলে `clang`।
   - Linker সব জোড়া লাগায়। `actool` asset catalog (app icon) compile করে।
   - "Thin Binary" phase (`xcode_backend.sh embed_and_thin`) `App.framework` আর release-এর `Flutter.framework` (engine) app-এর `Frameworks/` folder-এ বসায়।
   - প্রতিটা framework আর app sign হয়।
   - ফল: `build/ios/archive/Runner.xcarchive`।
3. **`xcodebuild -exportArchive`** — একটা `ExportOptions.plist` দিয়ে (default method `app-store`)। Distribution certificate আর profile দিয়ে আবার sign করে, আর zip করে `.ipa` বানায়। ফল: `build/ios/ipa/*.ipa`।
4. **Upload** Flutter নিজে করে না। Apple-এর **Transporter** app-এ `.ipa` টেনে দিন, অথবা Xcode Organizer-এ archive খুলে Distribute করুন। CI-তে সাধারণত App Store Connect API key দিয়ে fastlane বা CI-র নিজের tool।

**দরকারি flag:**

```bash
# pubspec-এর version বদলে দেয়; Dart-এর নাম লুকায়, symbol আলাদা রাখে
flutter build ipa --release --build-name=1.2.0 --build-number=6 \
  --obfuscate --split-debug-info=build/symbols

# App Store ছাড়া অন্য বিতরণ
flutter build ipa --export-method ad-hoc

# CI-তে, আগে থেকে রাখা export option দিয়ে
flutter build ipa --export-options-plist=ios/ExportOptions.plist
```

**ভেতরে দেখুন।** `.ipa` একটা zip। খুললে:

```
Notes.ipa
└── Payload/
    └── Runner.app/
        ├── Runner                    আপনার Swift code + plugin (Mach-O executable)
        ├── Info.plist                bundle id, version, permission-এর লেখা
        ├── embedded.mobileprovision  provisioning profile
        ├── _CodeSignature/           signature
        ├── Assets.car                compile করা asset catalog (icon)
        ├── PrivacyInfo.xcprivacy     (থাকলে)
        └── Frameworks/
            ├── Flutter.framework/    Flutter engine (C++), Impeller সহ   ← শুধু Flutter app-এ
            └── App.framework/
                ├── App               আপনার Dart code, machine code    ← শুধু Flutter app-এ
                └── flutter_assets/   image, font, AssetManifest        ← শুধু Flutter app-এ
```

Android-এর APK-র সাথে মেলান ([১৩.৬](#ch13-6)): `libflutter.so` ↔ `Flutter.framework`, `libapp.so` ↔ `App.framework/App`, `classes.dex` ↔ `Runner` executable।

**ফাঁদ:**
- **iOS-এর release Simulator-এ চলে না।** Release আর profile build শুধু আসল device-এর জন্য। Flutter tool নিজেই error দেয়।
- **CocoaPods-এর ভবিষ্যৎ।** Flutter-এর docs বলে, CocoaPods registry ২ ডিসেম্বর ২০২৬-এ স্থায়ীভাবে read-only হয়ে যাবে। যে plugin এখনো শুধু CocoaPods-এ, সেটা বদলানোর পরিকল্পনা রাখুন।
- **`flutter clean`-এর পরেও signing error।** Signing-এর আসল কারণ দেখতে `ios/Runner.xcworkspace` Xcode-এ খুলে একবার Archive চালান — Xcode অনেক স্পষ্ট error দেখায়।

> **মনে রাখুন**
> - Certificate = কে sign করছে। Provisioning profile = কোন app, কোন device, কোন entitlement। দুটো মিললে তবেই app চলে।
> - App-এর পরিচয় Bundle ID + Team, certificate না। Certificate বদলালে App Store-এর app-এর কিছু হয় না।
> - Archive → `.ipa` → App Store Connect → TestFlight (internal ১০০, external ১০,০০০, build ৯০ দিন) → review।
> - IAP digital জিনিসে বাধ্যতামূলক। Social login থাকলে privacy-বান্ধব আরেকটা login (Sign in with Apple সবচেয়ে সহজ)। Account মোছার পথ app-এর ভেতরে।
> - `flutter build ipa` = `xcodebuild archive` + `-exportArchive`। Dart যায় `App.framework`-এ, engine `Flutter.framework`-এ।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ signing-এর দুই মূল টুকরো: certificate, যেটা বলে কে sign করছে, আর provisioning profile, যেটা বলে কোন bundle id কোন device-এ কোন entitlement নিয়ে চলবে। নিজের Mac-এ automatic signing রাখি, CI-তে App Store Connect API key বা fastlane match। Release মানে archive থেকে ipa বানিয়ে App Store Connect-এ upload, TestFlight-এ test, তারপর review। flutter build ipa ভেতরে xcodebuild archive আর exportArchive চালায়, আর একটা build phase Dart code AOT compile করে App.framework বানায়।"
> - *English:* "iOS signing has two key pieces: the certificate, which says who signs, and the provisioning profile, which says which bundle ID can run on which devices with which entitlements. I use automatic signing on my Mac, and an App Store Connect API key or fastlane match on CI. A release means archiving, exporting an ipa, uploading it to App Store Connect, testing on TestFlight, and then review. flutter build ipa runs xcodebuild archive and exportArchive under the hood, and a build phase AOT-compiles the Dart code into App.framework."

[উপরে ফিরুন](#toc)

---

## <a id="ios12"></a>iOS ১২. ইঞ্জিনের ভেতরে — tap থেকে pixel, code থেকে `.ipa`

Android-এর [অধ্যায় ১৩](#ch13)-এ bonnet খুলেছিলাম: ART, Zygote, HWUI, SurfaceFlinger, Gradle। এবার iOS-এর bonnet। প্রশ্নগুলো একই — code চলে কীসের ওপর? Memory কে পরিষ্কার করে? App খুললে কী হয়? একটা pixel screen-এ আসে কীভাবে? Build চাপলে কী হয়? প্রতিটা উত্তরের পাশে থাকবে Flutter আর Android।

### <a id="ios12-1"></a>iOS ১২.১ Swift সরাসরি machine code — কোনো VM নেই

**এক লাইনে:** Swift code compile-এর সময়েই LLVM দিয়ে ARM64 machine code হয়ে যায়। Phone-এ কোনো virtual machine নেই, interpreter নেই, JIT নেই। CPU সরাসরি আপনার code চালায়।

**Swift code-এর যাত্রা:**

```
.swift ──swiftc──► AST ──► SIL (Swift Intermediate Language) ──► LLVM IR ──LLVM──► ARM64 (.o)
                            │                                                       │
                            └ এখানে ARC-এর retain/release বসে আর optimize হয়          ▼
                                                                         ld (linker) ──► Mach-O executable
```

- **SIL** হলো Swift-এর নিজের মাঝের ভাষা। Swift-এর বিশেষ optimization (generic specialization, ARC কমানো) এখানে হয়।
- **LLVM** হলো সেই একই compiler backend, যেটা C, C++, Objective-C, Rust-ও ব্যবহার করে। সে machine code বানায়।
- **Mach-O** হলো Apple-এর executable format — Linux-এর ELF বা Android-এর `.so`-র মতো।

**তাহলে "Swift runtime" কী?** একটা ছোট library: type-এর তথ্য (metadata), retain/release-এর function, dynamic cast, protocol খোঁজা। এটা VM না, শুধু সাহায্যকারী code। Swift 5-এ ABI স্থির হওয়ার পর থেকে (iOS 12.2) এই runtime OS-এর ভেতরেই থাকে, তাই আপনার app-এ আলাদা করে যায় না। পাশে Objective-C runtime-ও আছে — UIKit-এর class আর `@objc` method-এর message পাঠানো এর মাধ্যমে চলে।

**JIT কেন নেই:** iOS-এ App Store app-এর memory-তে নতুন executable code বানানো নিষেধ — প্রতিটা executable page sign করা থাকতে হয়। এজন্যই:
- **Flutter release build iOS-এ সবসময় AOT।** Android-এর মতোই, কিন্তু এখানে অন্য কোনো পথই নেই।
- **Device-এ Flutter debug (hot reload)** চলে Dart VM-এর JIT দিয়ে, Xcode-এর debugger-এর সাহায্য নিয়ে। iOS 26-এ এই নিয়ম আরও কড়া হওয়ায় Flutter-কে নিজের পদ্ধতি বদলাতে হয়েছিল। Physical device-এ debug করতে সর্বশেষ stable Flutter রাখুন।

**তিনটা runtime পাশাপাশি:**

| | Swift (iOS) | Kotlin (Android, ART) | Dart (Flutter) |
|---|---|---|---|
| Compile হয় | machine code, build-এর সময় | `.dex` bytecode | debug: kernel; release: machine code |
| Phone-এ চালায় | সরাসরি CPU + ছোট Swift runtime | ART: interpreter + JIT + AOT | debug: Dart VM (JIT); release: Dart runtime (AOT) |
| Memory | ARC ([iOS ১২.২](#ios12-2)) | garbage collector | garbage collector |
| VM আছে? | না | হ্যাঁ, ART | debug-এ হ্যাঁ, release-এ শুধু runtime |

**মজার কথা:** একটা Flutter iOS app-এ Swift/Objective-C-এর জগৎ আর Dart-এর জগৎ একই process-এ থাকে, কিন্তু heap আলাদা। Swift-এর object ARC দেখে, Dart-এর object Dart-এর GC দেখে। কথা হয় platform channel বা FFI দিয়ে। Android-এ ART আর Dart যেমন আলাদা ছিল ([১৩.২](#ch13-2)), ঠিক তেমন।

**ফাঁদ:** "Swift-ও Java-র মতো VM-এ চলে" — না। আর "Flutter iOS-এ Dart-কে Swift-এ translate করে" — তাও না। Dart নিজেই ARM64 machine code হয়, `App.framework`-এ ([iOS ১২.৫](#ios12-5))।

[উপরে ফিরুন](#toc)

### <a id="ios12-2"></a>iOS ১২.২ ARC বনাম garbage collection

**এক লাইনে:** Swift-এ কোনো garbage collector নেই। প্রতিটা class object-এর একটা গণনা থাকে — কতজন তাকে ধরে আছে। গণনা শূন্য হলে সাথে সাথে object মুক্ত। এই গণনা compiler নিজে বসায় — Automatic Reference Counting (ARC)।

**তিনজনের পদ্ধতি:**

| | Swift (ARC) | Dart | ART (Android) |
|---|---|---|---|
| কে মুক্ত করে | compiler-এর বসানো retain/release | GC | GC |
| কখন | শেষ reference যাওয়ার সাথে সাথে | GC যখন চালায় | GC যখন চালায় |
| GC pause | নেই | ছোট (নতুন object-এর জন্য দ্রুত scavenge) | ছোট (concurrent GC) |
| Cycle (A ধরে B, B ধরে A) | **leak** — নিজে ভাঙতে হয় | GC নিজে ধরে | GC নিজে ধরে |
| খরচ | প্রতিটা reference বদলে একটু কাজ | মাঝে মাঝে GC-র কাজ | মাঝে মাঝে GC-র কাজ |

**Value type-এ গণনা নেই।** `struct` আর `enum` copy হয়, তাই বেশিরভাগ ক্ষেত্রে reference count লাগে না। এজন্যই Swift-এ model `struct` রাখা জনপ্রিয় — দ্রুত আর নিরাপদ। (Struct-এর ভেতরে class বা `Array`-এর মতো জিনিস থাকলে, তাদের ভেতরের storage-এর গণনা থাকে।)

**Flutter থেকে আসা মানুষের সবচেয়ে বড় ফাঁদ — retain cycle:**

```swift
final class NoteEditor {
    var onChange: (() -> Void)?

    func start() {
        // ভুল: onChange = { self.saveDraft() }
        // editor ধরে closure-কে, closure ধরে editor-কে → গণনা কখনো শূন্য হয় না → leak

        onChange = { [weak self] in          // ঠিক: weak — ধরে, কিন্তু গণনা বাড়ায় না
            self?.saveDraft()
        }
    }

    func saveDraft() { }

    deinit { print("editor মুক্ত হলো") }    // leak থাকলে এটা কখনো চলবে না
}
```

Dart-এ এই code নিয়ে কখনো ভাবতে হয়নি — GC cycle নিজে খুঁজে বের করে। Swift-এ closure-এ `self` ধরার আগে সবসময় ভাবুন: কে কাকে ধরে আছে?

**কোথায় বেশি দেখবেন:**
- Plugin-এর `FlutterMethodChannel` handler closure-এ plugin class-কে ধরা।
- Delegate property — এজন্যই delegate প্রায় সবসময় `weak var delegate` ([iOS ৯.২](#ios9-2)-এর ফাঁদ দেখুন)।
- `weak` বনাম `unowned`: `weak` Optional, object চলে গেলে `nil` হয়। `unowned` ধরে নেয় object থাকবেই — না থাকলে crash। সন্দেহ থাকলে `weak`।

**Memory কম হলে iOS কী করে:** iOS-এ disk-এ swap নেই, memory compress করা হয়। তবু কম পড়লে **jetsam** নামের ব্যবস্থা background-এর app, এমনকি বেশি memory খাওয়া foreground app-কেও মেরে ফেলে। Android-এর low memory killer-এর মতো। তাই iOS-এ বড় ছবি বা leak সরাসরি crash হয়ে দেখা দেয়।

**Debug:** Xcode-এর **Memory Graph Debugger** (debug bar-এর একটা button) cycle-গুলো দেখায়। Instruments-এর **Leaks** আর **Allocations** — Android Studio-র Memory Profiler-এর মতো। Dart-এর heap দেখতে এখনো DevTools।

[উপরে ফিরুন](#toc)

### <a id="ios12-3"></a>iOS ১২.৩ App খুললে কী হয় — tap থেকে প্রথম frame

**এক লাইনে:** Home screen (SpringBoard) system-কে বলে, launchd একটা নতুন process চালু করে, dyld সব library জোড়ে, `main()` থেকে `UIApplicationMain` চলে, AppDelegate আর Scene তৈরি হয়, আর প্রথম frame আঁকা হলে launch screen সরে যায়। Flutter-এ মাঝে engine চালু করে Dart-এর `main()` চালানোর ধাপ।

**সব app-এর জন্য একই পথ:**

1. **Tap।** Home screen নিজেও একটা system app — **SpringBoard**। সে system-কে app খোলার অনুরোধ পাঠায়।
2. **আগে launch screen।** Process তৈরি হওয়ার আগেই iOS app-এর launch screen দেখায় — `Info.plist`-এর `UILaunchScreen`, বা `LaunchScreen.storyboard` থেকে। এটা একটা স্থির ছবির মতো, এখানে আপনার কোনো code চলে না। Android-এর starting window আর Flutter-এর `LaunchTheme`-এর মতো ([১৩.৩](#ch13-3))।
3. **Process।** **launchd** (iOS-এর সব process-এর জনক) একটা নতুন process চালু করে। Android-এর মতো Zygote-এর copy না — প্রতিবার নতুন process, নিজের sandbox-এ ([iOS ৮.৭](#ios8-7))।
4. **dyld।** Kernel আপনার Mach-O executable load করে, তারপর **dyld** (dynamic linker) কাজ শুরু করে। UIKit, SwiftUI, Foundation-এর মতো system framework আগে থেকে একটা বড় **shared cache**-এ তৈরি থাকে, তাই দ্রুত জোড়ে। আপনার নিজের framework (যেমন `Flutter.framework`) আলাদা করে load হয়। তারপর static initializer চলে।
5. **`main()` → `UIApplicationMain`।** SwiftUI-তে `@main struct NotesApp: App` লিখলে compiler একটা `main()` বানায়, যেটা ভেতরে এই কাজই করে। `UIApplicationMain` `UIApplication` object আর আপনার AppDelegate তৈরি করে, আর main thread-এ **run loop** চালু করে — Android-এর Looper বা Dart-এর event loop-এর মতো।
6. **AppDelegate।** `application(_:didFinishLaunchingWithOptions:)` চলে। SDK init, BGTask register — এগুলো এখানে।
7. **Scene।** `Info.plist`-এর scene configuration দেখে একটা `UIWindowScene` তৈরি হয়, আর SceneDelegate-এর `scene(_:willConnectTo:options:)` চলে। এখানে window আর প্রথম view controller (বা SwiftUI-র `WindowGroup`-এর content) তৈরি হয়। Apple বলেছে, iOS 26-এর পরের major release-এর SDK দিয়ে build করা app scene lifecycle না নিলে launch-ই হবে না ([iOS ৪](#ios4))।
8. **প্রথম frame।** View-এর layout আর আঁকা হয়। Run loop-এর এই ঘুরের শেষে Core Animation পরিবর্তনগুলো render server-এ পাঠায় ([iOS ১২.৪](#ios12-4))। প্রথম frame screen-এ এলে launch screen সরে যায়।

**ধাপ ৬–৭-এ এসে দুই পথ আলাদা হয়:**

- **Native (SwiftUI):** `WindowGroup { NotesScreen(...) }`-এর `body` চলে। View tree তৈরি হয়, তারপর প্রথম frame।
- **Flutter:** নতুন Flutter template-এর `AppDelegate` হলো `FlutterAppDelegate`, আর `SceneDelegate` হলো `FlutterSceneDelegate`। তারপর:
  1. Scene configuration-এর `Main` storyboard একটা **`FlutterViewController`** তৈরি করে।
  2. এটা একটা `FlutterEngine` চালু করে (template-এ "implicit engine")। `Flutter.framework` — C++-এ লেখা engine — dyld আগেই load করেছে।
  3. Engine নিজের thread বানায়: **platform thread** (এটাই iOS-এর main thread; Flutter 3.29 থেকে Dart code-ও এখানে চলে), **raster thread** (GPU-র কাজ), **I/O thread**।
  4. Engine তৈরি হলে `AppDelegate`-এর `didInitializeImplicitFlutterEngine` চলে, আর `GeneratedPluginRegistrant` সব plugin register করে। Plugin-এর Swift অংশ এখানে তৈরি হয়।
  5. Engine `App.framework` থেকে আপনার compile করা Dart code খুঁজে নেয়।
  6. Dart entrypoint চলে: `main()` → `runApp()` → widget tree।
  7. Engine প্রথম frame আঁকে। ততক্ষণ `FlutterViewController` launch screen-এর একটা copy দেখিয়ে রাখে। Frame আঁকা হলেই সেটা সরে।

```
 tap
  │
  ▼
SpringBoard ──► system: app খোলো
                  │  launch screen দেখাও (UILaunchScreen / storyboard)
                  │  launchd → নতুন process
                  ▼
           dyld: UIKit, SwiftUI (shared cache), নিজের framework load
                  │
                  ▼
           main() → UIApplicationMain → run loop (main thread)
                  │
                  ▼
           AppDelegate: didFinishLaunchingWithOptions
                  │
                  ▼
           Scene: SceneDelegate / WindowGroup
        ┌─────────┴──────────────────────────────┐
   Native (SwiftUI)                         Flutter
   WindowGroup-এর body                      FlutterSceneDelegate → FlutterViewController
        │                                   FlutterEngine চালু, thread তৈরি
        │                                   plugin register (didInitializeImplicitFlutterEngine)
        │                                   App.framework → Dart main() → runApp()
        ▼                                        ▼
   প্রথম frame (Core Animation)             প্রথম frame (Impeller → Metal)
        └─────────┬──────────────────────────────┘
                  ▼
        render server → display, launch screen সরে
```

**Cold, warm, আর pre-warming:**
- **Cold:** process নেই। উপরের পুরো পথ।
- **Warm/resume:** process memory-তে suspend হয়ে ছিল। শুধু আবার জাগানো, প্রায় সাথে সাথে।
- **Pre-warming:** iOS ব্যবহারের ধরন দেখে কখনো user tap করার আগেই app-এর process আগেভাগে চালু করে রাখে (iOS 15-এ এটা আরও বাড়ানো হয়েছে)। Apple-এর docs বলে, pre-warming `main()`-এর `UIApplicationMain` ডাকার আগ পর্যন্ত যায়। তবে developer-রা forum-এ জানিয়েছেন, বাস্তবে কখনো আরও কিছু চলে। তাই "process চালু হলো মানে user app খুলেছে" ধরে নেবেন না — analytics-এ "app open" গুনুন scene সামনে আসার পরে।

**ফাঁদ:**
- **Launch-এ বেশি কাজ।** `didFinishLaunching`-এ বা Flutter-এর `main()`-এ `runApp`-এর আগে সব `await` করলে launch screen আটকে থাকে। অনেক বেশি দেরি হলে iOS-এর **watchdog** app মেরে ফেলে — crash report-এ `0x8badf00d` code। Android-এর `Application.onCreate`-এর নিয়মই এখানে: প্রথম frame-এর আগে শুধু যা না হলেই নয়।
- **Launch screen-এ animation বা code চালানোর চেষ্টা।** Launch screen স্থির। Animated splash লাগলে সেটা আপনার প্রথম আসল screen-এ বানাতে হয়।

[উপরে ফিরুন](#toc)

### <a id="ios12-4"></a>iOS ১২.৪ Rendering — Core Animation, render server, Metal

**এক লাইনে:** Native iOS-এ প্রতিটা view-এর পেছনে একটা Core Animation **layer** থাকে। App layer-এর গাছ বানিয়ে আলাদা একটা system process — **render server** — কে পাঠায়। Render server Metal দিয়ে GPU-তে আঁকে, আর display-তে পাঠায়। Flutter এই গাছে শুধু একটা layer রাখে, আর তার ভেতরে Impeller নিজে সব আঁকে।

**নামগুলো:**

- **Core Animation (CA)।** UIKit-এর প্রতিটা `UIView`-এর পেছনে একটা `CALayer`। SwiftUI-ও শেষ পর্যন্ত এই layer-এর জগতেই আঁকে। Layer-এর গাছ (layer tree) হলো screen-এর বর্ণনা।
- **Transaction।** Main thread-এ আপনি state বদলালেন, layout হলো। Run loop-এর ঘুরের শেষে Core Animation সব পরিবর্তন একসাথে "commit" করে render server-এ পাঠায়।
- **Render server।** আলাদা একটা system process (backboardd-এর ভেতরে)। সব app-এর layer tree, status bar, keyboard — সব এখানে মেশে। Android-এর SurfaceFlinger-এর মতো কাজ, তবে এটা নিজেও layer আঁকে।
- **Metal।** Apple-এর GPU API — Android-এর Vulkan-এর জায়গায়। Render server Metal দিয়ে আঁকে।
- **Vsync।** Display প্রতি ১৬.৭ ms (60Hz) বা ৮.৩ ms (ProMotion, 120Hz) পর পর নতুন frame চায়। App এই সংকেত পায় `CADisplayLink` দিয়ে — Android-এর `Choreographer`-এর মতো।

**একটা সুন্দর ফল:** Core Animation-এর animation render server-এ চলে। তাই main thread কিছুক্ষণ ব্যস্ত থাকলেও এমন animation অনেক সময় মসৃণ থাকে। Flutter-এর animation Dart-এ চলে — UI thread আটকালে animation-ও আটকায়।

**Flutter-এ:** `FlutterViewController`-এর view হলো একটা `FlutterView`। এর layer Metal-এ আঁকার একটা layer — আজকাল default-এ Flutter-এর নিজের `FlutterMetalLayer` (`CALayer`-এর subclass; `FLTUseFlutterMetalLayer` = `NO` দিলে সাধারণ `CAMetalLayer`), যেটা `CAMetalLayer`-এর মতোই আচরণ করে কিন্তু frame-এর সময় নিয়ে আরও নিয়ন্ত্রণ দেয়। তারপর:
1. Platform thread-এ Dart: build → layout → paint → layer tree।
2. Raster thread-এ **Impeller** layer tree-কে Metal command-এ বদলায়, আর layer-এর কাছ থেকে নেওয়া একটা drawable-এ আঁকে।
3. সেই layer Core Animation-এর গাছের একটা সাধারণ layer — render server বাকিদের সাথে মিলিয়ে display-তে পাঠায়।
4. Vsync Flutter engine-ও নেয় `CADisplayLink` থেকে।

**Impeller iOS-এ:** iOS-এ Impeller default হয়েছিল Flutter 3.10-এ। Flutter 3.29 থেকে iOS backend-এ Skia পুরোপুরি সরানো, আর `FLTEnableImpeller` দিয়ে বন্ধ করার পথও নেই। তাই iOS-এ Impeller-ই একমাত্র renderer। এর সব shader আগে থেকে compile করা, তাই প্রথম animation-এ "shader compilation jank" নেই।

```
            Native (SwiftUI / UIKit)                       Flutter
 main thread: state → layout → CALayer গাছ     platform thread: build/layout/paint (Dart)
            │ CA transaction commit                        │ layer tree
            ▼                                              ▼
                                               raster thread: Impeller → Metal
                                                           │
                                               FlutterView-এর CAMetalLayer (একটা layer)
            └────────────────────┬─────────────────────────┘
                                 ▼
          render server (Metal)  ← status bar, keyboard, অন্য layer-ও এখানে মেশে
                                 ▼
                              display
```

**কী মিলল, কী আলাদা:**

| | Native iOS | Flutter on iOS | Android ([১৩.৫](#ch13-5)) |
|---|---|---|---|
| UI-র বর্ণনা | View → `CALayer` গাছ | widget → layer tree (Dart) | View/Compose → display list |
| কে GPU-তে আঁকে | render server (Core Animation) | app-এর raster thread-এ Impeller | RenderThread-এ HWUI (Skia) |
| GPU API | Metal | Metal | OpenGL ES / Vulkan |
| শেষে মেশায় | render server | render server | SurfaceFlinger |
| Vsync | `CADisplayLink` | `CADisplayLink` | `Choreographer` |

**ফাঁদ:**
- **ProMotion-এ 120Hz না পাওয়া।** iPhone-এ 60Hz-এর বেশি পেতে `Info.plist`-এ `CADisableMinimumFrameDurationOnPhone` = `true` লাগে। Flutter-এর template-এ এটা আগে থেকেই আছে। নিজে native project বানালে নিজে দিতে হয়।
- **"SwiftUI-ও Flutter-এর মতো নিজে আঁকে" ভাবা।** না — SwiftUI Apple-এর নিজের Core Animation-এর জগতের ভেতরে থাকে। তাই SwiftUI আর UIKit এক screen-এ সহজে মেশে। Flutter-কে UIKit view বসাতে Platform View (`UiKitView`) লাগে, যেটা বাড়তি composition-এর খরচ আনে।
- **iOS জানে না Flutter-এর screen-এ কী আছে।** ওর কাছে শুধু একটা layer-এর pixel। তাই VoiceOver-এর জন্য Flutter semantics tree থেকে iOS-এর accessibility element বানিয়ে দেয়।

[উপরে ফিরুন](#toc)

### <a id="ios12-5"></a>iOS ১২.৫ Build pipeline — Xcode থেকে `.app` আর `.ipa`

**এক লাইনে:** Xcode-এর build system target-এর build phase একটার পর একটা চালায়: package resolve, compile, link, resource, embed, sign। ফল একটা `.app` folder। Archive আর export করলে সেটা `.ipa`।

**Native: ⌘B বা Archive চাপলে**

1. **Package resolve।** Swift Package Manager-এর dependency download আর build ([iOS ৩](#ios3))। Android-এ Gradle-এর dependency resolve-এর মতো।
2. **Compile।** প্রতিটা module-এর Swift file `swiftc` দিয়ে, Objective-C থাকলে `clang` দিয়ে। Incremental — যা বদলায়নি, আবার compile হয় না।
3. **Link।** Apple-এর linker (`ld`) সব `.o` জোড়া লাগিয়ে একটা Mach-O executable বানায়।
4. **Resource।** `actool` asset catalog (`Assets.xcassets`) compile করে `Assets.car` বানায় — app icon, রং, ছবি। Storyboard থাকলে `ibtool`। `Info.plist`-এর `$(...)` build setting দিয়ে পূরণ হয়।
5. **Embed।** Dynamic framework (`Flutter.framework`-এর মতো) app-এর `Frameworks/` folder-এ copy হয়।
6. **Code sign।** `codesign` প্রতিটা framework আর শেষে app sign করে, entitlement বসায় ([iOS ১১.১](#ios11-1))।
7. **ফল:** `Notes.app` — আসলে একটা folder।
8. **Archive** করলে `.xcarchive` (app + dSYM), আর **export** করলে `.ipa` — `Payload/Notes.app`-এর একটা zip।

**কোথায় জমে:** সব মাঝের file থাকে `~/Library/Developer/Xcode/DerivedData/`-এ। Gradle-এর `build/` আর cache-এর মতো। অদ্ভুত build error হলে Product → **Clean Build Folder** (⇧⌘K), দরকারে DerivedData মুছে দিন।

**Xcode-এর build system নিজে:** Apple এটা ২০২৫-এ **Swift Build** নামে open source করেছে। Gradle-এর মতো task graph বানায়, কিন্তু আলাদা কোনো DSL নেই — নিয়ম আসে Xcode project-এর build settings আর build phase থেকে।

**App Store-এর দিকে:** Upload করা build থেকে App Store প্রতিটা device-এর জন্য ছোট রূপ বানায় (**App Thinning**) — যেমন শুধু সেই screen-এর মাপের ছবি। পুরনো Bitcode এখন আর নেই (Xcode 14-এ বাদ)।

**Flutter: Runner target-এ বাড়তি কী চলে**

`ios/Runner.xcodeproj`-এর Runner target-এ Flutter দুইটা **Run Script** phase যোগ করে:

1. **"Run Script"** — `xcode_backend.sh build` → `flutter assemble`:
   - **Release/profile:** Dart → kernel (`app.dill`, tree shaking সহ) → **`gen_snapshot`** → ARM64 machine code → `App.framework/App`, একটা Mach-O dynamic library। একাধিক architecture হলে `lipo` দিয়ে জোড়া।
   - **Debug:** `App.framework/App` শুধু একটা খালি stub। আপনার Dart code kernel আকারে `flutter_assets`-এ যায়, আর device-এ Dart VM সেটা JIT দিয়ে চালায় — hot reload এজন্যই সম্ভব।
   - Asset (image, font, `pubspec`-এর asset) → `App.framework/flutter_assets/`। Material Icons font থেকে শুধু ব্যবহৃত icon রাখা হয়।
2. **"Thin Binary"** — `xcode_backend.sh embed_and_thin` → `App.framework` আর build mode অনুযায়ী `Flutter.framework` app-এর `Frameworks/`-এ বসায়, আর sign করে।

বাকিটা native-এর মতোই: `AppDelegate`/`SceneDelegate` আর plugin-এর Swift code `swiftc`, link, asset catalog, sign।

```
.dart ──frontend_server──► app.dill ──gen_snapshot──► App.framework/App (ARM64)   ┐
pubspec asset ───────────────────────────────────────► App.framework/flutter_assets ├─► Runner.app/Frameworks/
Flutter SDK-র আগে থেকে build করা engine ─────────────► Flutter.framework            ┘
.swift (Runner + plugin) ──swiftc + ld──────────────► Runner.app/Runner
Assets.xcassets ──actool────────────────────────────► Runner.app/Assets.car
                                  সব শেষে codesign ──► Runner.app ──archive/export──► .ipa
```

**ফাঁদ:**
- **"Flutter iOS build মানে CocoaPods"** — আর না। Flutter 3.44 থেকে Swift Package Manager default, CocoaPods শুধু fallback ([iOS ১১.৬](#ios11-6))।
- **`flutter clean` সব মোছে না।** Xcode-এর DerivedData আলাদা। Native দিকের অদ্ভুত error-এ Xcode-এ Clean Build Folder দিন।

[উপরে ফিরুন](#toc)

### <a id="ios12-6"></a>iOS ১২.৬ Android-এর পাশে, এক টেবিলে

পুরো অধ্যায় আর Android-এর [অধ্যায় ১৩](#ch13) এক জায়গায়:

| বিষয় | iOS | Android | Flutter app-এ (দুই platform-এ) |
|---|---|---|---|
| Native ভাষা চলে | machine code (LLVM), VM নেই | `.dex`, ART-এ | Dart: release-এ AOT machine code |
| Memory | ARC — cycle নিজে ভাঙতে হয় | GC | Dart GC, native অংশ platform-এর নিয়মে |
| JIT | App Store app-এ নিষেধ | ART-এ আছে | শুধু debug-এ (hot reload) |
| App process আসে | launchd, প্রতিবার নতুন | Zygote থেকে fork | একই — platform-এর নিয়ম |
| Library জোড়ে | dyld (+ shared cache) | ART class loading, `.so` load | engine: `Flutter.framework` / `libflutter.so` |
| Entry | `main()` → `UIApplicationMain` → AppDelegate → Scene | `ActivityThread.main()` → Application → Activity | `FlutterAppDelegate` + `FlutterSceneDelegate` / `FlutterActivity` |
| Main loop | run loop | Looper | platform thread = main thread (3.29 থেকে Dart-ও সেখানে) |
| Launch screen | `UILaunchScreen` / storyboard | starting window (`LaunchTheme`) | একই, platform-এর |
| Launch-এ বেশি দেরি | watchdog মারে (`0x8badf00d`) | ANR dialog | একই |
| Native UI আঁকে | Core Animation → render server (Metal) | HWUI → Skia (GL/Vulkan) | Impeller (Metal / Vulkan, না থাকলে GL) |
| শেষে মেশায় | render server | SurfaceFlinger | একই, platform-এর |
| Vsync | `CADisplayLink` | `Choreographer` | engine সেখান থেকেই নেয় |
| Build tool | Xcode build system (`xcodebuild`) | Gradle + AGP | `flutter` tool → এই দুইটাকেই ডাকে |
| Dependency | Swift Package Manager (CocoaPods পুরনো) | Maven (Gradle) | pub.dev + এই দুই |
| Dart-এর output | `App.framework/App` | `libapp.so` | `gen_snapshot` দুটোই বানায় |
| Engine-এর file | `Flutter.framework` | `libflutter.so` | — |
| Package | `.ipa` (`Payload/X.app`) | APK / AAB | — |
| Sign | certificate + provisioning profile | keystore | platform-এর নিয়মে |
| Memory দেখা | Instruments, Memory Graph | Memory Profiler, Perfetto | Dart heap: DevTools |

> **মনে রাখুন**
> - Swift build-এর সময়েই LLVM দিয়ে machine code। VM নেই, JIT নিষেধ — তাই Flutter iOS release সবসময় AOT।
> - ARC: গণনা শূন্য হলেই মুক্ত, GC pause নেই, কিন্তু cycle নিজে ভাঙতে হয় — closure-এ `[weak self]`।
> - App খোলা: SpringBoard → launchd → dyld → `UIApplicationMain` → AppDelegate → Scene → প্রথম frame। Flutter-এ মাঝে `FlutterViewController`, engine আর Dart `main()`।
> - Native আঁকে Core Animation + render server + Metal। Flutter একটা `CAMetalLayer`-এ Impeller দিয়ে নিজে আঁকে — iOS-এ Impeller-ই একমাত্র renderer।
> - Build: swiftc → ld → actool → embed → codesign → `.app` → `.ipa`। Flutter-এর Dart যায় `App.framework`-এ, engine `Flutter.framework`-এ।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Swift সরাসরি LLVM দিয়ে machine code হয়, iOS-এ কোনো VM নেই, আর App Store app-এ JIT নিষেধ — এজন্যই Flutter-এর iOS release সবসময় AOT, Dart কোড App.framework-এ machine code হয়ে থাকে। Memory ARC দিয়ে চলে, তাই GC pause নেই, কিন্তু retain cycle নিজে weak দিয়ে ভাঙতে হয়। App খুললে launchd process চালু করে, dyld library জোড়ে, UIApplicationMain AppDelegate আর Scene বানায়; Flutter-এ FlutterViewController engine চালু করে Dart-এর main চালায়। Native UI Core Animation-এর layer tree render server-এ পাঠায়, আর Flutter একটা CAMetalLayer-এ Impeller দিয়ে Metal-এ নিজে আঁকে।"
> - *English:* "Swift is compiled straight to machine code by LLVM; there's no VM on iOS, and JIT isn't allowed for App Store apps — that's why Flutter's iOS release is always AOT, with the Dart code as machine code in App.framework. Memory is managed by ARC, so there are no GC pauses, but I have to break retain cycles myself with weak. On launch, launchd starts the process, dyld links the libraries, and UIApplicationMain creates the AppDelegate and the scene; in Flutter, the FlutterViewController starts the engine and runs Dart's main. Native UI sends a Core Animation layer tree to the render server, while Flutter draws everything itself with Impeller on Metal into a CAMetalLayer."

[উপরে ফিরুন](#toc)

---

## <a id="ios13"></a>iOS ১৩. iOS শেখার পরিকল্পনা — ৪ সপ্তাহ

Android-এর মতোই, পড়ে শেখার চেয়ে বানিয়ে শেখা অনেক দ্রুত। আর সবচেয়ে দ্রুত পথ একটাই: **এই বই জুড়ে যে Notes app দেখলেন, সেটা native iOS-এ বানানো।** প্রতিটা অংশ Flutter-এ কীভাবে লিখতেন, তা আপনি জানেন। শুধু অনুবাদ করবেন।

**আগে যা লাগবে:** একটা Mac, App Store থেকে সর্বশেষ Xcode, আর সম্ভব হলে একটা iPhone। নিজের phone-এ চালাতে free Apple ID-ই যথেষ্ট। Push, Associated Domains আর TestFlight-এর জন্য paid Apple Developer Program লাগবে ([iOS ১১.১](#ios11-1))। Project-এর minimum iOS 17 রাখুন, তাহলে `@Observable` আর SwiftData দুটোই পাবেন।

### <a id="ios13-1"></a>iOS ১৩.১ চার সপ্তাহের পরিকল্পনা

| সপ্তাহ | পড়ুন | বানান |
|---|---|---|
| ১ | [iOS ০](#ios0), [১](#ios1), [২](#ios2) | Xcode-এর Playground-এ Notes-এর model: `struct Note`, `enum` দিয়ে sort-এর ধরন, `protocol NotesRepository`। একটা `actor` দিয়ে in-memory store, আর `async`/`await` দিয়ে নকল network delay। |
| ২ | [iOS ৩](#ios3)–[৬](#ios6) | নতুন SwiftUI project। Note-এর list, note খোলা, নতুন note-এর form — শুধু memory-র data দিয়ে। `NavigationStack` দিয়ে navigation। App background-এ পাঠিয়ে আবার খুলে দেখুন কী থাকে, কী যায়। |
| ৩ | [iOS ৭](#ios7), [৮](#ios8) | `@Observable` view model, composition root-এ DI। SwiftData-তে note রাখুন। একটা free mock server থেকে `URLSession` দিয়ে sync, `Codable` দিয়ে JSON। Token Keychain-এ — তারপর app মুছে আবার install করে দেখুন token থেকে গেছে কি না। |
| ৪ | [iOS ৯](#ios9)–[১২](#ios12) | Reminder-এর local notification, `BGAppRefreshTask` দিয়ে sync (debugger command দিয়ে চালিয়ে দেখুন)। Swift Testing-এ view model test, একটা XCUITest। Archive করে TestFlight-এ পাঠান। শেষে একটা Flutter project-এ `flutter build ipa` চালিয়ে `.ipa` unzip করুন — `App.framework` আর `Flutter.framework` নিজের চোখে দেখুন। |

**প্রতিদিনের শেষে তিনটা প্রশ্ন:**
1. আজ যেটা লিখলাম, Flutter-এ সেটা কী দিয়ে করতাম? Android-এ কী দিয়ে? পার্থক্যটা কোথায়, আর কেন?
2. এটা কোন actor-এ চলছে — main actor, না অন্য কোথাও?
3. App suspend হলে, বা user swipe করে বন্ধ করলে, এটা কী হবে?

এই তিন প্রশ্নের উত্তর মুখে বলতে পারলে আপনি interview-এর জন্য তৈরি। প্রতিটা অধ্যায়ের শেষের **Interview-এ এক কথায়** box জোরে জোরে বলে অনুশীলন করুন।

[উপরে ফিরুন](#toc)

### <a id="ios-dictionary"></a>Flutter → iOS অভিধান

Interview-এর আগের রাতে শুধু এই পাতাটা। পাশে Android-ও রাখলাম, যাতে তিনটা একসাথে মনে থাকে।

**ভাষা**

| Dart | Swift | Kotlin |
|---|---|---|
| `final` / `var` / `const` | `let` / `var` / `static let` | `val` / `var` / `const val` |
| `late final x = f();` | `lazy var x = f()` | `val x by lazy { f() }` |
| `T?`, `??`, `?.`, `!` | `T?`, `??`, `?.`, `!` (একই!) | `T?`, `?:`, `?.`, `!!` |
| `if (x != null)` promotion | `if let x { }` / `guard let x else { return }` | smart cast |
| `void` / `Never` / `dynamic` | `Void` / `Never` / `Any` | `Unit` / `Nothing` / `Any?` |
| `switch` expression | `switch` (expression-ও হয়) | `when` |
| `sealed class` + subclass | associated value-সহ `enum` | `sealed class` / `sealed interface` |
| freezed / `copyWith` | `struct` (value type — copy করে বদলান) | `data class` / `copy()` |
| `==` / `hashCode` হাতে বা freezed | `Equatable` / `Hashable` (compiler বানায়) | `data class` নিজে |
| `abstract class` / `implements` | `protocol` | `interface` |
| mixin | protocol extension (default implementation) | interface default method |
| `extension X on Y` | `extension Y` | `fun Y.x()` |
| `static` | `static` | `companion object` |
| singleton | `static let shared` | `object` |
| factory constructor | `static func` বা failable `init?` | companion-এ factory |
| `typedef` | `typealias` | `typealias` |
| `try` / `catch` / `throw` | `do` / `try` / `catch` / `throws` | `try` / `catch` (checked exception নেই) |
| lazy `Iterable` | `.lazy` sequence | `Sequence` |
| `_private` | `private` / `fileprivate` / `internal` | `private` / `internal` |
| `build_runner` code gen | macro (`@Observable`, `@Model`) + compiler synthesis (`Codable`) | KSP / compiler plugin |

**Async**

| Dart | Swift | Kotlin |
|---|---|---|
| `Future<T>` + `async`/`await` | `async` function + `await` | `suspend fun` |
| `unawaited(f())` | `Task { await f() }` | `scope.launch { }` |
| `Future.wait` | `async let` / `TaskGroup` | `async { }` + `awaitAll()` |
| `Isolate.run` / `compute` | `@concurrent` function / `Task.detached` | `withContext(Dispatchers.Default)` |
| isolate-এর নিজের state | `actor` | `Mutex` / single-thread dispatcher |
| UI isolate | `@MainActor` | `Dispatchers.Main` |
| `Completer` | `withCheckedContinuation` | `suspendCancellableCoroutine` |
| `Stream` / `async*` | `AsyncSequence` / `AsyncStream` | `Flow` / `flow { }` |
| `StreamController.broadcast` | (built-in নেই) — Combine-এর `PassthroughSubject` | `SharedFlow` |
| `ValueNotifier` | `@Observable` class-এর property | `StateFlow` |
| `StreamSubscription.cancel` | `task.cancel()`, বা `.task` নিজে cancel | scope বন্ধ |
| `mounted` check | লাগে না — `.task` view-এর সাথে cancel | লাগে না — scope |
| RxDart `debounceTime` | swift-async-algorithms, বা Combine `debounce` | `debounce` |

**UI**

| Flutter | SwiftUI | Compose |
|---|---|---|
| Widget + `build()` | `View` + `body` | `@Composable` function |
| `setState` | `@State` property বদলানো | `mutableStateOf` |
| `State` object বাঁচে | `@State` | `remember { }` |
| `RestorationMixin` | `@SceneStorage` | `rememberSaveable` |
| `initState` / async load | `.task { }` / `.onAppear` | `LaunchedEffect` |
| `dispose` | `.onDisappear` (`.task` নিজে cancel) | `DisposableEffect` |
| `InheritedWidget` / Provider | `@Environment` | `CompositionLocal` |
| `Theme.of(context)` | `@Environment(\.colorScheme)`, `.tint`, `.font` | `MaterialTheme` |
| `Column` / `Row` / `Stack` | `VStack` / `HStack` / `ZStack` | `Column` / `Row` / `Box` |
| `Expanded` | `Spacer()` / `.frame(maxWidth: .infinity)` | `Modifier.weight(1f)` |
| `Padding` / `Container` / `GestureDetector` | `.padding` / `.background` / `.onTapGesture` | `Modifier.padding` / `.background` / `.clickable` |
| `ListView.builder` | `List` / `LazyVStack` | `LazyColumn` |
| `GridView` | `LazyVGrid` | `LazyVerticalGrid` |
| `PageView` | `TabView` + `.tabViewStyle(.page)` | `HorizontalPager` |
| `TextField` + controller | `TextField(text: $title)` binding | `value` + `onValueChange` |
| `FocusNode` | `@FocusState` | `FocusRequester` |
| `showDialog` / `showModalBottomSheet` | `.alert` / `.sheet` + `.presentationDetents` | `AlertDialog` / `ModalBottomSheet` |
| `AnimatedContainer` | `withAnimation { }` / `.animation(_:value:)` | `animate*AsState` |
| `Hero` | `matchedGeometryEffect` / zoom navigation transition | shared element |
| `Navigator` / `go_router` | `NavigationStack` + `navigationDestination` | Navigation Compose |
| `Image.network` / `cached_network_image` | `AsyncImage` (cache-এর জন্য Nuke/Kingfisher) | Coil `AsyncImage` |
| `Icon(Icons.add)` | `Image(systemName: "plus")` (SF Symbols) | `Icon(Icons.Default.Add)` |
| `Key('save')` (test-এর জন্য) | `.accessibilityIdentifier("save")` | `Modifier.testTag("save")` |
| Hot reload / DevTools | `#Preview` / Instruments | `@Preview` / Layout Inspector |

**App, architecture, data**

| Flutter | iOS | Android |
|---|---|---|
| `main()` + `runApp` | `@main struct App` + `WindowGroup` | `Application` + `setContent` |
| Flutter-এর host | `FlutterAppDelegate` + `FlutterSceneDelegate` + `FlutterViewController` | `FlutterActivity` |
| `WidgetsBindingObserver` | `@Environment(\.scenePhase)` | `Lifecycle` |
| Cubit / Bloc | `@MainActor @Observable` view model | `ViewModel` |
| `BlocProvider` | `@State private var viewModel` | `hiltViewModel()` |
| `BlocBuilder` | কিছু লাগে না — `body`-তে property পড়া | `collectAsStateWithLifecycle()` |
| `BlocListener` | `.onChange(of:)` / `.alert(isPresented:)` | `LaunchedEffect` + state |
| `get_it` / `injectable` | `init` injection + `@Environment` | Hilt |
| `dio` | `URLSession` (+ নিজের wrapper) | Retrofit + OkHttp |
| dio interceptor | নিজের `send()` function | `Interceptor` / `Authenticator` |
| `json_serializable` | `Codable` | kotlinx.serialization |
| `drift` / `sqflite` | SwiftData (পুরনো: Core Data) | Room |
| `.watch()` | `@Query` (view-এ) | `Flow` query |
| `shared_preferences` | `UserDefaults` / `@AppStorage` | DataStore |
| `flutter_secure_storage` | Keychain (uninstall-এর পরেও থাকতে পারে) | Keystore + Tink |
| `path_provider` | `URL.applicationSupportDirectory`, `.documentsDirectory`, `.cachesDirectory` | `filesDir` / `cacheDir` |

**Platform আর release**

| Flutter | iOS | Android |
|---|---|---|
| `workmanager` | `BGTaskScheduler` (iOS ঠিক করে কখন) | WorkManager |
| `flutter_local_notifications` | `UNUserNotificationCenter` | `NotificationCompat` + channel |
| `firebase_messaging` | APNs (FCM শুধু relay, `.p8` key লাগে) | FCM |
| `permission_handler` | `Info.plist` usage description + framework-এর request API | Activity Result API |
| `image_picker` | `PhotosPicker` (permission লাগে না) | Photo Picker |
| `url_launcher` | `openURL` / `UIApplication.open` / `SFSafariViewController` | implicit `Intent` / Custom Tabs |
| `share_plus` | `ShareLink` / `UIActivityViewController` | `ACTION_SEND` |
| deep link | Universal Links / custom URL scheme | App Links / intent-filter |
| platform channel | `FlutterMethodChannel` (Swift) | `MethodChannel` (Kotlin) |
| `pubspec.yaml` | Xcode project + Swift Package Manager | `libs.versions.toml` + `build.gradle.kts` |
| `--flavor` | scheme + build configuration | `productFlavors` |
| `--dart-define` | `.xcconfig` + `Info.plist`-এর value | `buildConfigField` |
| `flutter test` / `bloc_test` | Swift Testing (`@Test`, `#expect`) | JUnit + Turbine |
| `integration_test` | XCUITest | instrumented test |
| golden test | swift-snapshot-testing | Roborazzi / Paparazzi |
| Dart VM / Dart runtime | VM নেই — machine code + Swift runtime | ART |
| Impeller | Core Animation + Metal | HWUI (ভেতরে Skia) |
| `App.framework` (`gen_snapshot`) | app-এর Mach-O executable | `libapp.so` / `classes.dex` |
| `flutter build ipa` | `xcodebuild archive` + `-exportArchive` | `./gradlew bundleRelease` |
| keystore দিয়ে sign | certificate + provisioning profile | keystore |
| Play Console | App Store Connect | Play Console |
| internal / closed testing | TestFlight | testing track |
| Data safety form | Privacy nutrition label + privacy manifest | Data safety form |

[উপরে ফিরুন](#toc)

### <a id="ios13-2"></a>iOS ১৩.২ ভালো resource

সবগুলো official, আর প্রতিটা link নভেম্বর ২০২৬-এ খুলে দেখা।

- [Develop in Swift tutorials](https://developer.apple.com/tutorials/develop-in-swift) — Apple-এর নতুনদের পথ, SwiftUI আর SwiftData দিয়ে। প্রথম সপ্তাহের জন্য।
- [SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui) — হাতে-কলমে, ধাপে ধাপে screen বানানো।
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/) — Swift-এর official বই। Optional, enum, protocol, concurrency-র অধ্যায় আগে।
- [Swift 6 migration guide](https://www.swift.org/migration/documentation/migrationguide/) — strict concurrency-র error কেন আসে, কীভাবে ঠিক করবেন।
- [Migrating to the Observable macro](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro) — পুরনো `ObservableObject` code পড়তে আর বদলাতে।
- [SwiftData](https://developer.apple.com/documentation/swiftdata) আর [Swift Testing](https://developer.apple.com/documentation/testing) — দুইটা framework-এর official docs।
- [TN3187: UIScene lifecycle-এ যাওয়া](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) — scene lifecycle কেন বাধ্যতামূলক হচ্ছে, কীভাবে বদলাবেন।
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) আর [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/) — submit-এর আগে প্রতিবার।
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) — iOS app "iOS-এর মতো" দেখাতে।
- [Flutter for SwiftUI developers](https://docs.flutter.dev/flutter-for/swiftui-devs) — Flutter-এর official তুলনা, SwiftUI developer-দের জন্য লেখা। উল্টো দিক থেকে পড়লে আপনার জন্য একদম কাজের।
- [Flutter-এর iOS platform integration](https://docs.flutter.dev/platform-integration/ios/) আর [Platform channels](https://docs.flutter.dev/platform-integration/platform-channels) — Flutter app-এ Swift code লেখার পথ।
- [Build and release an iOS app (Flutter)](https://docs.flutter.dev/deployment/ios) — `flutter build ipa`, signing, TestFlight।

> **মনে রাখুন**
> - Notes app native-এ বানানোই সবচেয়ে দ্রুত শেখা। Minimum iOS 17 রাখুন।
> - চার সপ্তাহ: ভাষা আর async → SwiftUI আর navigation → architecture আর data → platform, test, release, internals।
> - প্রতিদিন তিন প্রশ্ন: Flutter আর Android-এ কী দিয়ে করতাম? কোন actor-এ চলছে? Suspend বা swipe হলে কী হবে?
> - Interview-এর আগের রাতে শুধু [অভিধান](#ios-dictionary)।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি Flutter-এর চোখ দিয়ে iOS শিখেছি: প্রতিটা Flutter ধারণার জন্য iOS-এ তার যমজ খুঁজেছি — Cubit থেকে @Observable view model, dio থেকে URLSession, drift থেকে SwiftData, workmanager থেকে BGTaskScheduler। তারপর একই Notes app native SwiftUI-তে বানিয়েছি, TestFlight পর্যন্ত। তাই plugin-এর ভেতরে কী হয়, আর কোন সমস্যা আসলে iOS-এর নিয়ম থেকে আসে, সেটা আমি ব্যাখ্যা করতে পারি।"
> - *English:* "I learned iOS through Flutter eyes: for every Flutter concept I found its iOS twin — Cubit to an @Observable view model, dio to URLSession, drift to SwiftData, workmanager to BGTaskScheduler. Then I built the same Notes app in native SwiftUI, all the way to TestFlight. So I can explain what happens inside a plugin, and which problems really come from iOS rules."

[উপরে ফিরুন](#toc)

---
