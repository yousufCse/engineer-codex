# Flutter-এর চোখে Android আর iOS — শেখার গাইড (বাংলা)

> এই বই তাঁর জন্য, যিনি Flutter ভালো জানেন। অনেক আগে Java আর Activity দিয়ে Android করেছেন। কিন্তু Kotlin আর Jetpack Compose আসার পরে আর Android করেননি।
> এটা interview-এর প্রশ্ন-উত্তর না, এটা একটা **শেখার গাইড**। প্রতিটা জিনিস আগে দেখানো হয়েছে Flutter-এ আপনি যেভাবে করেন। তারপর দেখানো হয়েছে Android-এ ঠিক সেই কাজটা কীভাবে হয়।
> বইয়ে দুইটা খণ্ড: **খণ্ড ১ — Android** (অধ্যায় ০–১৪) আর **খণ্ড ২ — [iOS](#part-ios)** (iOS ০–১৩)। দুই খণ্ডই একই ধাঁচে লেখা, আর দুটোতেই একই Notes app-এর উদাহরণ।
> শেখা শেষ হলে practice করার জন্য আছে [Flutter + Android + iOS Interview Prep](../../interviews/software-engineer-flutter-android-ios-bn/flutter-android-ios-interview-prep-bn.md)।

---

## <a id="preface"></a>শুরুর কথা

Flutter থেকে Android-এ এলে আপনাকে সব নতুন করে শিখতে হবে না। State, async, architecture, declarative UI, test — এগুলো আপনি আগে থেকেই জানেন। নতুন শিখতে হবে শুধু তিনটা জিনিস: Android-এ এগুলোর নাম কী, কোথায় নিয়ম আলাদা, আর কোন ভুলগুলো এড়িয়ে চলতে হয়।

এই বই প্রতিটা Android জিনিসের পাশে লিখে দেবে, Flutter-এ এটাকে কী বলে।

আরেকটা কথা: আপনি Android আগেও ব্যবহার করেছেন। প্রতিটা Flutter app Android-এর ভেতরেই চলে। এতদিন Flutter আর plugin সেই Android অংশটা আপনার কাছ থেকে লুকিয়ে রেখেছিল। এবার সেটা সরাসরি নিজে লিখবেন।

---

## <a id="big-picture"></a>আগে এটা পড়ুন — এক পাতায় পুরো ছবি

বইয়ের বাকি সব কিছু এই এক পাতার ওপর দাঁড়িয়ে। কোথাও গুলিয়ে গেলে এখানে ফিরে আসুন।

```
┌──────────── Android বা iOS (OS) ────────────────┐
│  app চালু আর বন্ধ, permission, notification,     │
│  background কাজ, storage — সব OS নিয়ন্ত্রণ করে   │
│                                                  │
│   ┌──────── আপনার Flutter app ────────┐          │
│   │  Embedder  ← OS আর engine-এর যোগাযোগ │          │
│   │  Engine    ← Dart চালায়, screen আঁকে  │          │
│   │  Dart code ← আপনার UI আর logic       │          │
│   │  Plugin    ← native API ডাকে          │          │
│   └────────────────────────────────────┘          │
└──────────────────────────────────────────────────┘
```

**ছয়টা মূল কথা:**

1. **App-এর জীবন OS নিয়ন্ত্রণ করে।** App কখন চালু হবে আর কখন বন্ধ হবে, কোন permission পাবে, notification, background কাজ — সব Android বা iOS ঠিক করে।
2. **Native app-এর UI আঁকে OS নিজে।** Android-এ আপনি Compose দিয়ে UI লেখেন, iOS-এ SwiftUI দিয়ে। Screen-এ pixel বানায় OS-এর নিজের renderer।
3. **Flutter app-ও একটা native app।** Android-এ এর একটাই Activity (`FlutterActivity`), iOS-এ একটা `FlutterViewController`। OS শুধু আঁকার জন্য একটা surface দেয়। সেই surface-এ Flutter-এর engine নিজে প্রতিটা pixel আঁকে।
4. **Flutter-এর তিন অংশ।** আপনার Dart code ঠিক করে কী দেখাবে। Engine (C++) সেই Dart code চালায় আর screen আঁকে। Embedder OS থেকে touch, lifecycle আর surface নিয়ে engine-কে দেয়।
5. **Native কাজের জন্য plugin।** Camera, notification বা location লাগলে Dart platform channel দিয়ে plugin-কে message পাঠায়। Plugin-এর Kotlin বা Swift code OS-এর API ডাকে, তারপর ফল আবার Dart-এ পাঠায়।
6. **দুই ভাষা, দুই runtime।** Android-এ Kotlin চলে ART-এ, যেটা phone-এর OS-এর অংশ। Dart চলে Dart runtime-এ, যেটা app নিজের ভেতরে (engine-এ) নিয়ে আসে। iOS-এ Swift আগেই machine code-এ compile হয়ে থাকে। Build-এর সময় Gradle (Android) বা Xcode (iOS) সব অংশ জুড়ে একটা app বানায়।

**সারকথা:** OS app চালায় আর native ক্ষমতা দেয়। Flutter নিজের engine দিয়ে UI আঁকে। Native কিছু লাগলে plugin দিয়ে OS-এর API ডাকে।

এই বইয়ে আপনি শিখবেন, plugin যে native কাজগুলো লুকিয়ে রাখত, সেগুলো native-এ নিজে কীভাবে করতে হয় — আগে Android (খণ্ড ১), তারপর iOS (খণ্ড ২)। ভেতরের পুরো যন্ত্রের বিস্তারিত আছে [অধ্যায় ১৩](#ch13) (Android) আর [iOS ১২](#ios12)-এ।

[উপরে ফিরুন](#toc)

---

## <a id="how-to-read"></a>কীভাবে পড়বেন

**প্রতিটা বিষয় একই ধাঁচে লেখা।** তাই কয়েকটা বিষয় পড়ার পরে আপনি নিজেই জানবেন, কোথায় কী খুঁজতে হবে:

| অংশ | কী থাকে |
|---|---|
| **এক লাইনে** | জিনিসটা কী, এক বাক্যে |
| **Flutter-এ আপনি যেভাবে করেন** | আপনার চেনা Dart code |
| **Android-এ একই কাজ** | ঠিক সেই কাজ, Kotlin-এ |
| **কী মিলল, কী আলাদা** | পাশাপাশি তুলনা |
| **ভেতরে কীভাবে কাজ করে** | ধাপে ধাপে, যেখানে দরকার |
| **Best approach** | আজকে কোনটা নেবেন, আর কেন — একটাই উত্তর |
| **ফাঁদ** | Flutter থেকে আসা মানুষ সাধারণত যেখানে ভুল করে |

প্রতিটা অধ্যায়ের শেষে দুইটা ছোট box আছে। একটা **মনে রাখুন** — তিন-চারটা মূল কথা। আরেকটা **Interview-এ এক কথায়** — বাংলা আর English-এ। Revision-এর দিন শুধু এই box-গুলো পড়লেই পুরো বইটা মনে পড়ে যাবে।

**পুরো বইয়ে একটাই উদাহরণ — একটা Notes app।** App-টায় আছে note-এর list, একটা note খোলা, নতুন note লেখা, database-এ রাখা, আর server-এর সাথে sync। প্রতিটা অধ্যায় এই app-এর একটা অংশ বানায়। তাই প্রতি অধ্যায়ে নতুন উদাহরণ মাথায় নিতে হবে না। আপনি শুধু দেখবেন, Flutter-এ যে Notes app বানাতেন, Android-এ সেটা কীভাবে বানানো হয়।

**শুরু থেকে ক্রম ধরে পড়ুন।** অধ্যায় ০ সবচেয়ে জরুরি। এটা বুঝলে বাকি সব সহজে মাথায় বসে যাবে। বইয়ের শেষে revision-এর জন্য একটা [Flutter → Android অভিধান](#dictionary) আছে।

> **Version নিয়ে:** বইটা লেখা নভেম্বর ২০২৬-এ। তখনকার Kotlin 2.x, Compose BOM আর Android 16/17 ধরে লেখা। Library-র নাম আর API সহজে বদলায় না, কিন্তু version number প্রায়ই বদলায়। তাই dependency যোগ করার সময় [developer.android.com](https://developer.android.com) থেকে একদম নতুন version নিন। Code-এ version-এর জায়গায় `x.x` লেখা আছে।

---

## <a id="toc"></a>সূচিপত্র

- [শুরুর কথা](#preface) · [আগে এটা পড়ুন — এক পাতায় পুরো ছবি](#big-picture) · [কীভাবে পড়বেন](#how-to-read)

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

**এক লাইনে:** Flutter শুধু UI আঁকে আর Dart code চালায়। বাকি সব কাজ Android-এর — app চালু হওয়া, lifecycle, permission, notification, background কাজ, database। Flutter-এ এগুলো আপনি plugin দিয়ে ব্যবহার করতেন। Plugin-এর ভেতরে যে Android code ছিল, এখন সেটাই আপনি নিজে লিখবেন।

এই অধ্যায়টা ভালো করে বুঝলে বাকি গাইড সহজ হয়ে যাবে।

### <a id="ch0-1"></a>০.১ আপনার Flutter app আসলে একটা Android app

আপনার যেকোনো Flutter project-এর `android/` folder খুলুন। ওটা নিজেই একটা **পুরো Android project।** ভেতরে এই file-টা পাবেন:

```kotlin
// android/app/src/main/kotlin/com/byteonyx/notes/MainActivity.kt
class MainActivity : FlutterActivity()
```

পুরো file-এ শুধু এই এক লাইন। User যখন app খোলে, তখন এই ধাপগুলো হয়:

1. Android একটা process চালু করে আর `MainActivity` তৈরি করে — যেকোনো Android app-এর মতোই।
2. `FlutterActivity` একটা **FlutterEngine** চালু করে। এই engine-এর ভেতরে Dart VM চলে। তারপর আপনার `main()` call হয়।
3. Activity পুরো screen জুড়ে একটা আঁকার জায়গা রাখে — একে surface বলে। Flutter সেই surface-এ নিজের widget নিজেই আঁকে (Skia বা Impeller দিয়ে)। Android-এর নিজের button বা text-এর কোনোটাই Flutter ব্যবহার করে না।
4. Camera, notification বা file-এর মতো কিছু লাগলে Dart code Android-এর Kotlin বা Java code-কে কাজটা করতে বলে। এই কথা বলা হয় **platform channel** দিয়ে — Dart আর native code-এর মাঝে message পাঠানোর একটা পথ। Plugin মানে এটাই: একদিকে Dart API, অন্যদিকে Android (আর iOS) code।

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

আরও কিছু জিনিস আছে, যেগুলো Flutter-এ থেকেও আপনি আসলে Android-এরটাই ব্যবহার করতেন:

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

**তাই আপনি শূন্য থেকে শুরু করছেন না।** Android-এর অর্ধেক জিনিস আপনি আগেই ব্যবহার করেছেন। শুধু সেগুলো plugin-এর আড়ালে লুকানো ছিল। এখন আড়ালটা সরিয়ে সরাসরি দেখবেন।

আসল পার্থক্য দুইটা জায়গায়:
- **UI:** Flutter-এ UI Flutter নিজে আঁকে। Native Android-এ UI-ও Android-এর নিজের — এখন Jetpack Compose, আগে ছিল XML View।
- **ভাষা আর runtime:** Dart VM-এর জায়গায় এখন Kotlin। Kotlin চলে Android-এর ART runtime-এ। ART হলো phone-এর ভেতরের সেই engine, যেটা Kotlin/Java code চালায়।

App খোলা থেকে screen-এ pixel আসা পর্যন্ত কী হয়, আর build চাপলে কী হয় — ভেতরের পুরো গল্প আছে [অধ্যায় ১৩](#ch13)-এ।

[উপরে ফিরুন](#toc)

### <a id="ch0-2"></a>০.২ Android-এর স্তরগুলো

Android নিজে একটা পুরো operating system। তার ওপরে app বানানোর একটা framework-ও আছে। নিচের ছবিটা কয়েকটা স্তর (layer) দেখায়। নিচ থেকে ওপরে পড়ুন:

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

এর মধ্যে আপনার জন্য জরুরি দুইটা স্তর:

- **Android framework (SDK):** এটা phone-এর Android version-এর সাথেই আসে। তাই Android 14-এর phone-এ পাবেন Android 14-এর API, আর Android 10-এর phone-এ Android 10-এর API। তাই নতুন কোনো API ব্যবহার করলে পুরনো phone-এর কথাও ভাবতে হয়। আপনার app সবচেয়ে পুরনো কোন version-এ চলবে, সেটা বলে দেয় `minSdk`।
- **Jetpack (AndroidX):** এগুলো Google-এর library। এগুলো আপনার app-এর ভেতরেই ঢুকে যায় (bundle হয়)। তাই phone-এর Android version যা-ই হোক, সব phone-এ এগুলো একইভাবে কাজ করে। নতুন Android-এর প্রায় সব কিছু এখানেই: Compose, Room, ViewModel। এগুলোকে pub.dev-এর official package-এর মতো ভাবতে পারেন — শুধু পার্থক্য হলো, এগুলো Google-এর নিজের বানানো।

**নিয়ম:** কোনো কাজের জন্য Jetpack-এ library থাকলে সেটাই নিন। সরাসরি পুরনো framework API নেবেন না। যেমন শুধু `Notification` না নিয়ে `NotificationCompat` (Jetpack) নিন। কারণ Compat class-গুলো পুরনো আর নতুন Android version-এর পার্থক্য নিজেই সামলে নেয়।

[উপরে ফিরুন](#toc)

### <a id="ch0-3"></a>০.৩ পুরো framework-এর মানচিত্র

এটা পুরো গাইডের সবচেয়ে কাজের table। বাম দিকে আছে কাজটা। তারপর আছে আজকে Android-এ যেটা নেবেন। পরের কলামে পুরনো Android-এর জিনিস, যা চিনে রাখা ভালো। আর একদম ডানে, Flutter-এ আপনি যেটা নিতেন।

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

**পুরনো কলামটা কেন রাখা হলো:** Interview-এ আর পুরনো project-এ এগুলো দেখবেন। আপনি যখন Java-তে Android করতেন, তখন সম্ভবত `AsyncTask`, `RecyclerView`, একাধিক Activity আর `SharedPreferences` ব্যবহার করেছেন। তবে নতুন code লিখবেন "আজকের best choice" কলাম দিয়ে।

[উপরে ফিরুন](#toc)

### <a id="ch0-4"></a>০.৪ মাথায় রাখার তিনটা বদল

**১. Platform এখন সরাসরি আপনার হাতে।** Flutter-এ plugin আপনার হয়ে Android-এর নিয়মগুলো মানত। এখন সেগুলো আপনাকেই মানতে হবে। যেমন: কোন Android version-এ কোন permission লাগে, background-এ কী চালানো যায়, notification channel কীভাবে বানাতে হয়। কাজ একটু বেশি। কিন্তু কোনো plugin-এর bug-এর জন্য আর আটকে থাকতে হবে না।

**২. Main thread আটকানো যাবে না, আর thread এখন আসল।** Dart-এ সব code একটা thread-এ চলে, আর `await` সেই thread আটকায় না। Kotlin-এ অনেকগুলো আসল thread আছে। মানে কয়েকটা কাজ সত্যিই একই সময়ে পাশাপাশি চলে। আর এই thread-গুলো একই memory share করে। ভারী কাজ অন্য thread-এ পাঠানো তাই খুব সহজ। কিন্তু main thread ৫ সেকেন্ডের বেশি আটকে থাকলে system একটা "App isn't responding" (ANR) dialog দেখায়। বিস্তারিত আছে [অধ্যায় ২](#ch2)-এ।

**৩. Screen যেকোনো সময় মরে যেতে পারে।** Flutter-এ phone ঘোরালে (rotation) widget শুধু rebuild হয়, কিন্তু `State` object বেঁচে থাকে। Android-এ তা না। Rotation, dark mode বদল বা ভাষা বদল হলে Activity পুরোটা destroy হয়, তারপর নতুন করে তৈরি হয়। আবার app background-এ থাকলে system পুরো process-টাই মেরে ফেলতে পারে। তখন memory-তে যা ছিল সব হারিয়ে যায়। তাই প্রথম দিন থেকেই ভাবতে হয়, state কোথায় রাখবেন। বিস্তারিত আছে [অধ্যায় ৫](#ch5)-এ।

> **মনে রাখুন**
> - আপনার প্রতিটা Flutter app আসলে একটা Android app, যার ভেতরে একটা `FlutterActivity` আছে। Plugin-এর ভেতরে আছে Android code।
> - Flutter নিজে শুধু UI আঁকে আর Dart চালায়। বাকি সব Android framework-এর।
> - Jetpack হলো Google-এর library, যেটা app-এর ভেতরে ঢুকে যায়। নতুন Android-এর প্রায় সব কিছু এখানে।
> - তিনটা বদল মাথায় রাখুন: platform এখন নিজের হাতে, thread এখন আসল, আর screen বা process যেকোনো সময় মরে যেতে পারে।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter একটা UI toolkit, যেটা Android-এর ভেতরে একটা Activity-তে চলে আর নিজের renderer দিয়ে আঁকে। Lifecycle, permission, background কাজ — এগুলো সবসময় Android-এরই। তাই Flutter-এ plugin-এর আড়ালে যা ব্যবহার করতাম, native-এ সেগুলো সরাসরি ব্যবহার করি।"
> - *English:* "Flutter is a UI toolkit that runs inside an Android Activity and draws with its own renderer. Lifecycle, permissions and background work always belong to Android. So in native, I use directly what plugins used to hide from me in Flutter."

[উপরে ফিরুন](#toc)

---

## <a id="ch1"></a>১. Kotlin — Dart-এর পাশে

Dart আর Kotlin দেখতে অনেকটা একই রকম। Dart বানিয়েছে Google, আর Kotlin বানিয়েছে JetBrains। দুটোই statically typed, দুটোই null-safe। দুটোতেই lambda আর extension খুব বেশি ব্যবহার হয়। প্রথম দিনের Kotlin code পড়লে আপনার মনে হবে, "আরে, এ তো প্রায় Dart, শুধু semicolon নেই আর type পেছনে বসে।"

এই অধ্যায়ে আমরা Notes app-এর model আর ছোট ছোট helper লিখব। প্রতিটা আগে Dart-এ দেখব, তারপর Kotlin-এ।

### <a id="ch1-1"></a>১.১ Variable আর type

**এক লাইনে:** Dart-এর `final` হলো Kotlin-এর `val`, আর `var` হলো `var`। Type লেখা হয় নামের পরে।

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
| `final` | `val` | মাত্র একবার value দেওয়া যায় |
| `var` | `var` | |
| `const` | `const val` | শুধু primitive আর `String`, আর শুধু top-level বা `object`-এ |
| `String name` | `name: String` | type পরে |
| `int`, `double`, `bool` | `Int`, `Double`, `Boolean` | নাম বড় হাতের অক্ষরে শুরু। `Long`, `Float`-ও আছে |
| `? :` ternary | `if ... else` | Kotlin-এ `if` নিজেই value দেয় |
| `dynamic` | নেই | সবচেয়ে কাছের হলো `Any?`, কিন্তু ব্যবহার করার আগে cast করতে হয় |
| `typedef` | `typealias` | |

**Kotlin-এ প্রায় সবকিছুই expression।** Expression মানে যেটা একটা value ফেরত দেয়। `if`, `when`, `try` — সবাই value দেয়। ঠিক Dart 3-এর switch expression-এর মতো:

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

**ফাঁদ:** Number-এর type নিজে থেকে বদলায় না। Dart-এ `int` অনেক জায়গায় নিজেই `double` হয়ে যায়। Kotlin-এ `Int` কখনো নিজে থেকে `Long` বা `Double` হয় না। আপনাকে `toLong()` বা `toDouble()` লিখে বদলাতে হয়। প্রথম সপ্তাহে এটা বিরক্ত লাগবে। পরে বুঝবেন, এটা কত bug আটকে দিচ্ছে।

**Loop:**

```kotlin
for (i in 0 until notes.size) { }           // Dart: for (var i = 0; i < notes.length; i++)
for (note in notes) { }                     // Dart: for (final note in notes)
for ((index, note) in notes.withIndex()) { }
repeat(3) { println("হ্যালো") }
```

[উপরে ফিরুন](#toc)

### <a id="ch1-2"></a>১.২ Null safety

**এক লাইনে:** Dart-এ যা শিখেছেন, প্রায় পুরোটাই একই। শুধু দুইটা চিহ্ন আলাদা।

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

**Smart cast** — এটা Dart-এর type promotion-এর মতো। Null check করার পরে compiler নিজেই ধরে নেয়, value-টা আর null না:

```kotlin
fun preview(body: String?): String {
    if (body == null) return "খালি note"
    return body.take(50)               // এখানে body আর nullable না
}
```

**কী আলাদা:**
- Smart cast কাজ করে local `val`-এ। আর এমন property-তে, যেটা check আর ব্যবহারের মাঝে বদলাতে পারে না। Class-এর `var` property-তে এটা কাজ করে না। কারণ আপনি check করার পরে, ব্যবহার করার আগেই, অন্য কোনো thread সেটা বদলে দিতে পারে। Dart-এ এই সমস্যা নেই, কারণ Dart-এ একটাই thread। সমাধান: value-টা আগে একটা local variable-এ নিন — `val current = note ?: return`।
- **Java থেকে আসা value-র কোনো গ্যারান্টি নেই।** Java-তে `?` নেই। তাই Java-র return value-কে Kotlin `String!` ধরে। এর মানে "এটা null হতে পারে কি না, জানি না"। Android SDK-র অনেক পুরনো অংশ Java-তে লেখা। তাই সেখান থেকে value এলে ধরে নিন, এটা null হতে পারে।

**Best approach:** `!!` প্রায় কখনোই লিখবেন না। লিখতে ইচ্ছা হলে একটু থামুন। সাধারণত হয় model-টাই ভুল বানানো, নয়তো `?:` দিয়ে একটা default value দেওয়া উচিত।

[উপরে ফিরুন](#toc)

### <a id="ch1-3"></a>১.৩ Function আর lambda

**এক লাইনে:** প্রায় Dart-এর মতোই। শুধু দুইটা পার্থক্য: যেকোনো argument নাম দিয়ে দেওয়া যায়, আর শেষের lambda-টা ব্র্যাকেটের বাইরে লেখা যায়।

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
- Dart-এ named parameter-এর জন্য `{}` আর `required` লাগে। Kotlin-এ call করার সময় যেকোনো parameter-কে নাম দিয়ে দেওয়া যায়। যে parameter-এর default value নেই, সেটা দিতেই হবে (required)।
- Dart-এর `void` হলো Kotlin-এর `Unit`। আর যে function কখনো return করে না (যেমন সবসময় throw করে), তার return type `Nothing` — Dart-এর `Never`-এর মতো।

**Trailing lambda — Compose বুঝতে এটা সবচেয়ে জরুরি।** কোনো function-এর শেষ parameter যদি নিজেই একটা function হয়, তাহলে সেটা `()`-এর বাইরে লেখা যায়। আর সেটাই যদি একমাত্র parameter হয়, তাহলে `()`-ও লিখতে হয় না।

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

`Column { ... }` আসলে `Column(content = { ... })`। আর `Button(...) { Text("Save") }` আসলে `Button(onClick = ..., content = { Text("Save") })`। Flutter-এ আপনি `child:` আর `children:` দিয়ে যা করতেন, Compose-এ এটা দিয়েই সেই কাজ হয়। এই একটা নিয়ম বুঝলে Compose আর অদ্ভুত লাগবে না।

**Lambda with receiver** — এখানে block-এর ভেতরে `this` মানে একটা নির্দিষ্ট object। তাই সেই object-এর function সরাসরি call করা যায়:

```kotlin
val text = buildString {        // ভেতরে this = StringBuilder
    append("শিরোনাম: ")
    append(note.title)
}
```

Gradle-এর `android { ... }` আর Compose-এর `LazyColumn { items(...) }` — দুটোই lambda with receiver। তাই এসব block-এর ভেতরে এমন function call করা যায়, যেগুলো block-এর বাইরে নেই।

[উপরে ফিরুন](#toc)

### <a id="ch1-4"></a>১.৪ Class

**এক লাইনে:** Constructor বসে class-এর নামের ঠিক পাশে। আর property লিখলেই তার getter আর setter পাওয়া যায় — তিনটা মিলে একটাই জিনিস।

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

Constructor, তিনটা field আর default value — সব প্রথম কয়েক লাইনেই। Value ঠিক আছে কি না check করতে চাইলে (validation) `init` block লিখুন:

```kotlin
class Note(val id: String, val title: String) {
    init {
        require(title.length <= 500) { "শিরোনাম বেশি লম্বা" }   // ভুল হলে IllegalArgumentException
    }
}
```

**Setter-এ logic** — এখানে `field` মানে property-র আসল value যেখানে জমা থাকে:

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

**Inheritance default-এ বন্ধ।** Dart থেকে আসা মানুষ এতে প্রথমে অবাক হয়। Dart-এ যেকোনো class extend করা যায়। কিন্তু Kotlin-এ class default-এ `final`। কাউকে extend করতে দিতে চাইলে class-এ `open` লিখতে হয়। আর যে method override করা যাবে, সেটাতেও `open` লাগে:

```kotlin
open class BaseRepository { open fun refresh() {} }
class NotesRepository : BaseRepository() { override fun refresh() {} }
```

**Interface আর mixin।** Kotlin-এর interface-এ default method লেখা যায়। কিন্তু field (state) রাখা যায় না। Dart-এর `mixin` দিয়ে আপনি state-সহ behavior জুড়তেন। Kotlin-এ সেই কাজ হয় delegation দিয়ে — মানে কাজটা অন্য একটা object-কে দিয়ে দেওয়া ([১.৯](#ch1-9))।

```kotlin
interface Syncable {
    fun sync()
    fun syncLabel() = "Sync হচ্ছে..."     // default
}
```

**Best approach:** Inheritance-এর বদলে composition নিন। মানে subclass না বানিয়ে, দরকারি object-গুলো class-এর ভেতরে রাখুন। Interface ছোট রাখুন, আর dependency নিন constructor-এ। আপনার clean architecture-এর অভ্যাসটাই এখানে কাজে লাগবে।

[উপরে ফিরুন](#toc)

### <a id="ch1-5"></a>১.৫ Model class: `data`, `sealed`, `enum`

**এক লাইনে:** `freezed` দিয়ে যা যা বানাতেন, Kotlin-এ সেগুলো ভাষার মধ্যেই আছে। আলাদা package লাগে না।

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

`data class` নিজেই `equals`, `hashCode`, `toString` আর `copy` বানিয়ে দেয়। তবে শুধু primary constructor-এর property দিয়ে — মানে class-এর নামের পাশের ব্র্যাকেটে যেগুলো লেখা।

**ফাঁদ:** `copy()` shallow copy করে। মানে ভেতরের object-গুলো নতুন করে বানায় না। তাই ভেতরে একটা `MutableList` থাকলে নতুন আর পুরনো note একই list share করে। এজন্য model-এ সবসময় `val` আর read-only `List` রাখুন।

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

- `when`-এ `else` দেবেন না। তাহলে পরে নতুন case যোগ করলে, যেসব জায়গায় সেটা handle করা হয়নি, compiler সব দেখিয়ে দেবে — Dart-এর exhaustive switch-এর মতো।
- Kotlin-এ `sealed class` আর `sealed interface` দুটোই আছে। সাধারণত `sealed interface` নিন। সব case-এ একই field লাগলে তখন `sealed class` নিন।
- যে case-এ কোনো data নেই, তার জন্য `data object` নিন। এটা পড়ার মতো একটা `toString()` দেয়।

**Enum:**

```kotlin
enum class Priority(val label: String) {
    HIGH("জরুরি"), LOW("পরে");
}

Priority.entries              // Dart: Priority.values
Priority.valueOf("HIGH")      // Dart: Priority.values.byName('high')
```

**Best approach:** সব case দেখতে একই রকম হলে → `enum`। প্রতিটা case আলাদা আলাদা data রাখলে → `sealed interface`। শুধু সাধারণ data হলে → `data class`।

**`value class` — Dart-এর extension type-এর মতো।** এটা একটা সাধারণ value-কে নিজের একটা type দেয়, যাতে দুইটা id ভুল করে বদলাবদলি না হয়:

```kotlin
@JvmInline value class NoteId(val raw: String)

fun open(id: NoteId) { }      // ভুল করে UserId দিলে compile error, কিন্তু runtime-এ শুধু String
```

[উপরে ফিরুন](#toc)

### <a id="ch1-6"></a>১.৬ `static`, singleton, factory

**এক লাইনে:** Kotlin-এ `static` keyword নেই। তার বদলে আছে `companion object`, `object` আর top-level function।

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

**Top-level function খুব বেশি ব্যবহার হয়।** Dart-এর মতোই, সবকিছু class-এর ভেতরে ঢোকাতে হয় না:

```kotlin
// NoteFormat.kt
fun formatDate(millis: Long): String = ...
```

**Best approach:** নিজে `object` দিয়ে singleton কম বানান। Repository বা service-এর singleton লাগলে Hilt-কে `@Singleton` দিয়ে বানাতে দিন ([৮.৫](#ch8-5))। তাহলে test-এ আসলটার জায়গায় অন্য একটা বসানো যায়।

[উপরে ফিরুন](#toc)

### <a id="ch1-7"></a>১.৭ Extension আর scope function

**এক লাইনে:** Extension একদম Dart-এর মতোই। Scope function হলো কয়েকটা ছোট function, যেগুলো একটা object নিয়ে একটা block চালায়। Dart-এর cascade (`..`) যে কাজ করে, এরা সেটা আর তার চেয়েও বেশি কাজ করে।

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

Dart-এর মতোই extension static ভাবে resolve হয়। মানে কোন extension call হবে, সেটা compile time-এ variable-এর type দেখে ঠিক হয়। আর extension class-এর private জিনিস দেখতে পায় না।

**পাঁচটা scope function আছে। দুইটা প্রশ্ন দিয়ে এদের মনে রাখুন:**
1. Block-এর ভেতরে object-কে কী নামে পাই — `this` না `it`?
2. Block কী ফেরত দেয় — object নিজে, না lambda-র ফল?

| Function | ভেতরে | ফেরত | কখন |
|---|---|---|---|
| `apply` | `this` | object | object বানিয়ে সাজানো (configure) — cascade-এর মতো |
| `also` | `it` | object | পাশের ছোট কাজ: log, check |
| `let` | `it` | ফল | nullable value-এর উপর কাজ |
| `run` | `this` | ফল | object-এর উপর কয়েকটা কাজ করে একটা ফল বের করা |
| `with` | `this` | ফল | `run`-এর মতোই, কিন্তু extension function না |

```kotlin
note.body?.let { body -> showPreview(body) }          // Dart: if (note.body case final body?) ...

val saved = repository.save(note)
    .also { Log.d("Notes", "saved ${it.id}") }
```

**ফাঁদ:** একটা scope function-এর ভেতরে আরেকটা দেবেন না। দুই স্তর হলেই `this` আর `it` কোনটা কী, গুলিয়ে যায়। তখন একটা সাধারণ variable নিন।

[উপরে ফিরুন](#toc)

### <a id="ch1-8"></a>১.৮ Collection

**এক লাইনে:** Operator প্রায় একই। কিন্তু Kotlin-এ "শুধু পড়া যায়" আর "বদলানোও যায়" — এই দুইটা আলাদা type।

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

**Lazy না eager:** Dart-এর `where`/`map` lazy। মানে শেষে `toList()` করলে তখনই কাজটা চলে। Kotlin-এর `List`-এর `filter`/`map` eager। মানে সাথে সাথেই একটা নতুন list বানায়। Dart-এর মতো lazy চাইলে `asSequence()` ব্যবহার করুন:

```kotlin
val firstTen = hugeList.asSequence().filter { it.isPinned }.map { it.title }.take(10).toList()
```

**Best approach:** Class-এর বাইরে সবসময় `List` দিন। ভেতরে দরকার হলে `MutableList` রাখুন। ছোট list-এ সাধারণ operator-ই যথেষ্ট। Data অনেক বড় হলে, বা operator-এর chain লম্বা হলে, `Sequence` নিন।

[উপরে ফিরুন](#toc)

### <a id="ch1-9"></a>১.৯ `late`, `lateinit`, `lazy`, `by`

**এক লাইনে:** Dart-এর `late` দুইভাবে ব্যবহার হয়। Kotlin-এ এই দুইটা আলাদা জিনিস: `lateinit` আর `lazy`।

| Dart | Kotlin | কী হয় |
|---|---|---|
| `late Database db;` | `lateinit var db: Database` | Value আপনি পরে দেবেন। তার আগে পড়লে exception হয়। বারবার value দেওয়া যায়। |
| `late final formatter = DateFormat('dd MMM');` | `val formatter by lazy { DateTimeFormatter.ofPattern("dd MMM") }` | প্রথমবার পড়ার সময় একবার তৈরি হয়। তারপর সবসময় সেটাই। বদলানো যায় না। |

```kotlin
class NotesActivity : ComponentActivity() {
    @Inject lateinit var analytics: Analytics              // Hilt পরে বসাবে

    private val formatter by lazy { DateTimeFormatter.ofPattern("dd MMM yyyy") }
}
```

- `lateinit` শুধু `var`-এ চলে, আর `Int`/`Boolean`-এ চলে না। কারণ "এখনো set হয়নি" বোঝাতে ভেতরে null রাখা হয়। কিন্তু JVM-এর primitive type null রাখতে পারে না।
- `lazy` default-এ thread-safe। মানে দুইটা thread একসাথে প্রথমবার পড়লেও block একবারই চলে।

**`by` — delegation, Android-এ সব জায়গায় দেখবেন।** `by` মানে "এই property-র কাজটা ওকে দিয়ে দিলাম":

```kotlin
val viewModel: NotesViewModel by viewModels()            // প্রথম access-এ ViewModel
var title by mutableStateOf("")                          // Compose: পড়া/লেখা state-এ যায়
val isDark by settings.isDark.collectAsStateWithLifecycle(false)
```

পুরো class-এও `by` দেওয়া যায়। Dart-এ যেখানে `mixin` নিতেন, এখানে এটা নিন:

```kotlin
class NotesRepository(logger: Logger) : Logger by logger    // Logger-এর সব method logger-কে দিল
```

**Best approach:** Value বাইরে থেকে আসলে (Hilt, `onCreate()`) → `lateinit`। Value নিজেই বানাতে পারলে, শুধু একটু পরে → `lazy`। তবে সবচেয়ে ভালো হলো value-টা constructor-এ নেওয়া। তখন এই দুটোর কোনোটাই লাগে না।

[উপরে ফিরুন](#toc)

### <a id="ch1-10"></a>১.১০ Java-র সাথে

আপনি আগে Java-তে Android করেছেন। তাই পুরনো code পড়তে এই অংশটা কাজে লাগবে। Kotlin আর Java একই project-এ পাশাপাশি থাকতে পারে। একটা আরেকটাকে সরাসরি call করতে পারে।

- **Getter/setter property হয়ে যায়:** Java-র `note.getTitle()` Kotlin-এ লেখা হয় `note.title`।
- **এক method-এর interface-এ lambda দেওয়া যায়:** `button.setOnClickListener { save() }`। Java-তে এর জন্য একটা anonymous class লিখতে হতো।
- **Checked exception নেই:** Java-র `throws IOException` Kotlin-এ ধরা বাধ্যতামূলক না। এটা সুবিধা। কিন্তু ঝুঁকিও আছে — exception ধরতে ভুলে যেতে পারেন।
- **Java থেকে Kotlin call করতে এগুলো লাগে:** `@JvmStatic` (companion-এর function-কে আসল static বানায়), `@JvmField` (getter ছাড়া সরাসরি field দেয়), `@JvmOverloads` (default parameter-এর জন্য আলাদা আলাদা overload বানায়)।

Android Studio-তে Java file খুলে **Code → Convert Java File to Kotlin File** দিলে file-টা নিজে থেকেই Kotlin-এ বদলে যায়। পুরনো Java code দেখে Kotlin শেখার এটা দারুণ উপায়। শুধু বদলানো code-এ যেসব `!!` আসে, সেগুলো হাতে ঠিক করে নিন।

> **মনে রাখুন**
> - `final` → `val`, `??` → `?:`, `!` → `!!`, `switch` → `when`, `void` → `Unit`।
> - `freezed`-এর কাজ `data class` আর `sealed interface` করে, code generation ছাড়া।
> - `static` নেই — `companion object`, `object` আর top-level function।
> - Class default-এ `final`। Collection-এর read-only আর mutable type আলাদা।
> - Trailing lambda বুঝলে Compose বোঝা সহজ হয়।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Dart থেকে Kotlin-এ আসা সহজ ছিল, কারণ null safety আর type system প্রায় একই। আমার কাছে Kotlin-এর সবচেয়ে কাজের জিনিস হলো data class, sealed interface দিয়ে exhaustive `when`, আর read-only collection — এগুলো ভুল state compile time-এই আটকে দেয়।"
> - *English:* "Moving from Dart to Kotlin was easy, because null safety and the type system are almost the same. What I find most useful in Kotlin are data classes, sealed interfaces with an exhaustive `when`, and read-only collections — they stop bad state at compile time."

[উপরে ফিরুন](#toc)

---

## <a id="ch2"></a>২. Async — Future আর Stream থেকে Coroutine আর Flow

Flutter-এ async লেখা আপনার কাছে খুব সহজ: `async`, `await`, `Stream`, `StreamBuilder`। Kotlin-এর coroutine প্রথমে একটু কঠিন মনে হয়, কারণ নতুন নাম অনেক — scope, dispatcher, job, structured concurrency। কিন্তু এগুলো সব আসলে একটা প্রশ্নের উত্তর দেয়। Dart-এ এই প্রশ্নটা আপনাকে কখনো ভাবতে হয়নি: **"এই কাজটা কোন thread-এ চলবে, আর কখন থামবে?"**

তাই এই অধ্যায় শুরু হচ্ছে thread দিয়ে।

### <a id="ch2-1"></a>২.১ সবচেয়ে বড় পার্থক্য: thread

**Dart-এ যেভাবে চলে:**
- একটা isolate-এ একটা thread আর একটা event loop থাকে।
- `await` দিলে আপনার function থামে। Event loop তখন অন্য কাজ করে। ফল এলে আবার আপনার function চলে।
- দুইটা Dart code কখনো একই মুহূর্তে একই memory ছোঁয় না। তাই lock লাগে না, race condition প্রায় হয়ই না। (Race condition মানে দুইটা কাজ একসাথে একই data বদলাতে গিয়ে ভুল ফল হওয়া।)
- ভারী CPU কাজের জন্য আলাদা isolate নেন। সেটা memory share করে না, message পাঠিয়ে কথা বলে।

**Kotlin-এ যেভাবে চলে:** অনেকগুলো আসল thread থাকে, আর সবাই একই memory দেখে। Coroutine হলো thread-এর উপরে চলা একটা হালকা কাজ। এটা মাঝপথে থামতে পারে, পরে আবার চলতে পারে। দরকার হলে এক thread থেকে আরেক thread-এ সরেও যেতে পারে।

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

এর দুইটা ফল আছে। দুটোই ভালো করে মনে রাখুন:

1. **ভারী কাজ অন্য thread-এ পাঠানো খুব সহজ।** Isolate-এর মতো data copy করতে হয় না।
2. **Shared mutable state এখন সত্যিকারের ঝুঁকি।** মানে যে data কয়েকটা thread একসাথে দেখে আর বদলাতে পারে। দুইটা coroutine দুই thread থেকে একই `MutableList` বা `var` বদলালে data নষ্ট হতে পারে। Dart-এ এই bug হয়ই না। তাই Kotlin-এ immutable data, `StateFlow.update {}`, বা `Mutex` লাগে। (Mutex একটা lock — এক সময়ে একটা coroutine-কেই ঢুকতে দেয়।)

আর সবচেয়ে জরুরি নিয়ম: **main thread আটকানো যাবে না।** Network, disk বা বড় হিসাব main thread-এ চালালে UI আটকে যায়। ৫ সেকেন্ড আটকে থাকলে ANR আসে।

[উপরে ফিরুন](#toc)

### <a id="ch2-2"></a>২.২ `Future` → `suspend`

**এক লাইনে:** যে function কোনো কিছুর জন্য অপেক্ষা করে, Dart-এ সেটা `Future` ফেরত দেয়। Kotlin-এ সেটাকে `suspend` function বানানো হয়। আর সেটা সরাসরি ফল ফেরত দেয়।

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

কোন লাইনে coroutine থামতে পারে, Android Studio সেটা বাম পাশে একটা ছোট চিহ্ন দিয়ে দেখায়। Kotlin-এ `await` লেখা থাকে না। তাই এই চিহ্ন দেখেই বুঝবেন, কোথায় থামে।

**ভেতরে কীভাবে কাজ করে:**
1. Compiler প্রতিটা suspend function-কে একটা state machine-এ বদলে দেয়। মানে function-টা কয়েকটা ধাপে ভাগ হয়। প্রতিটা থামার জায়গা একটা ধাপ।
2. থামার সময় local variable-গুলো একটা `Continuation` object-এ জমা রাখা হয়।
3. ফল এলে ঠিক সেই জায়গা থেকে function আবার চলে।

Dart-এর `async` function-ও ভেতরে প্রায় একই কাজ করে। এজন্যই হাজারটা coroutine একসাথে চালানো যায়। প্রতিটার জন্য আলাদা thread লাগে না।

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

**খেয়াল করুন:** `launch` আর `async` চালু করতে একটা **scope** লাগে (`viewModelScope.launch`)। Dart-এ যেকোনো জায়গা থেকে `Future` চালু করা যায়। কিন্তু Kotlin-এ প্রতিটা coroutine-এর একটা মালিক থাকে। কেন থাকে, সেটা পরের অংশে।

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

একবার চালু করা `Future` কেউ থামায় না। তাই `mounted` check করতে হয়, আর প্রতিটা subscription হাতে cancel করতে হয়।

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

এখানে `mounted` check নেই, `dispose`-এ cancel-ও নেই। ViewModel clear হলে `viewModelScope` বন্ধ হয়ে যায়। তখন তার ভেতরের সব coroutine নিজে থেকেই বাতিল হয়।

| Scope | কখন বন্ধ হয় | Flutter-এ কাছাকাছি |
|---|---|---|
| `viewModelScope` | ViewModel clear হলে (screen সত্যিই বন্ধ) | Cubit-এর `close()` |
| `lifecycleScope` | Activity destroy হলে | `State.dispose()` |
| `rememberCoroutineScope()` | Composable screen থেকে সরে গেলে | widget dispose |

**এই নিয়মের নাম structured concurrency:**
1. প্রতিটা coroutine একটা parent-এর ভেতরে চলে।
2. Parent বাতিল হলে সব child বাতিল।
3. Parent শেষ হয় না, যতক্ষণ সব child শেষ না হয়।
4. একটা child fail করলে parent সেটা জানতে পারে। সাধারণ scope-এ তখন বাকি child-রাও বাতিল হয়। কিন্তু `SupervisorJob` থাকলে বাকিরা চলতে থাকে। `viewModelScope` এটাই ব্যবহার করে। তাই একটা request fail করলেও ViewModel-এর অন্য কাজ থামে না।

**ফাঁদ:** `GlobalScope` ব্যবহার করবেন না। এর কোনো মালিক নেই, তাই এটা কখনো থামে না। মানে Dart-এর সেই পুরনো সমস্যা ফিরে আসে — চালু হওয়া `Future`-এর মতো, কাজটা আর থামানো যায় না। পুরো app জুড়ে চলা কাজ লাগলে Application-এ নিজের একটা scope বানান, আর Hilt দিয়ে inject করুন।

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

এখানে data copy করতে হয় না, message-ও পাঠাতে হয় না। কারণ সব thread একই memory দেখে।

| Dispatcher | কোথায় | কী কাজে |
|---|---|---|
| `Dispatchers.Main` | Main (UI) thread | UI update, ছোট কাজ |
| `Dispatchers.IO` | IO-র জন্য বড় thread pool | Network, file, database — যেখানে বেশিরভাগ সময় অপেক্ষা |
| `Dispatchers.Default` | CPU core-এর সমান thread | JSON parse, sort, image — CPU-র কাজ |

**Main-safe নিয়ম:** Main-safe মানে main thread থেকে call করলেও UI আটকায় না। নিয়মটা হলো: প্রতিটা suspend function নিজেই ঠিক করবে, তার কোন dispatcher লাগে। তাহলে যে call করে, সে যেকোনো thread থেকে চিন্তা ছাড়াই call করতে পারে।

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

**Best approach:** Retrofit আর Room-এর suspend function আগে থেকেই main-safe। তাই এগুলোকে আবার `withContext(Dispatchers.IO)`-এর ভেতরে রাখবেন না। নিজের file-এর কাজ বা CPU-র কাজে `withContext` দিন। আর dispatcher constructor-এ নিন, যাতে test-এ একটা test dispatcher দেওয়া যায়।

[উপরে ফিরুন](#toc)

### <a id="ch2-6"></a>২.৬ Cancellation

**এক লাইনে:** Coroutine-কে জোর করে থামানো হয় না। প্রতিটা থামার জায়গায় সে নিজে check করে, তাকে বাতিল করা হয়েছে কি না।

Dart-এ `Future` বাতিলই করা যায় না। Kotlin-এ যায়, কিন্তু coroutine-কেও এতে অংশ নিতে হয়। প্রতিটা suspend call (`delay`, network, `withContext`) নিজে থেকেই check করে। কিন্তু লম্বা CPU loop-এ কোনো suspend call না থাকলে, check-টা আপনাকে নিজে করতে হবে:

```kotlin
suspend fun reindex(notes: List<Note>) = withContext(Dispatchers.Default) {
    for (note in notes) {
        ensureActive()             // বাতিল হলে এখানে থামে
        index(note)
    }
}
```

**ভেতরে কীভাবে:** Suspend point মানে যে লাইনে coroutine থামতে পারে। Coroutine বাতিল করলে তার পরের suspend point-এ একটা `CancellationException` throw হয়। এই exception উপরে উঠে গিয়ে coroutine শেষ করে দেয়। এজন্যই পরের অংশের নিয়মটা জরুরি।

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

দেখতে একই রকম। কিন্তু তিনটা নিয়ম নতুন:

1. **`launch`-এর ভেতরে কেউ না ধরলে exception app crash করায়।** Dart-এ না ধরা `Future` error শুধু log হয় (zone-এর error handler-এ)। কিন্তু Kotlin-এ সেটা thread-এর uncaught exception হয়ে যায়, মানে app crash করে। `async`-এ exception জমা থাকে, আর `.await()` call করলে তখন বের হয়।
2. **`CancellationException` কখনো গিলবেন না।** মানে এটা ধরে চুপ করে রেখে দেবেন না। `catch (e: Exception)` দিয়ে সব ধরলে এটাও ধরা পড়ে। তখন coroutine বাতিল হওয়ার পরেও চলতে থাকে। তাই নির্দিষ্ট exception ধরুন (`IOException`, `HttpException`)। সব exception ধরতেই হলে, আগে এটাকে আলাদা করে ধরে আবার throw করুন:

```kotlin
} catch (e: CancellationException) {
    throw e
} catch (e: Exception) {
    _state.update { it.copy(error = "কিছু একটা ভুল হয়েছে") }
}
```

3. **`runCatching { }` সাবধানে ব্যবহার করুন।** এটাও `CancellationException` ধরে ফেলে। Suspend code-এ ব্যবহার করলে উপরের মতো সেটা আবার throw করুন।

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

**ভেতরে কীভাবে — cold মানে কী:** `countdown(10)` লিখলে কিছুই চলে না। শুধু flow-টা কী করবে, তার বর্ণনা তৈরি হয়। `collect` call করলে তখন `flow { }` block চলে। দুইজন collect করলে block দুইবার চলে, দুইজন আলাদা countdown পায়। Network call-এর flow দুইবার collect করলে দুইটা request যায়।

**ফাঁদ:** Flow শেষ না হওয়া পর্যন্ত `collect` সেখানেই থেমে থাকে। তাই একই coroutine-এ দুইটা `collect` পরপর লিখলে দ্বিতীয়টা কখনো চলে না, যদি প্রথম flow শেষ না হয়। তাই প্রতিটা collect আলাদা `launch`-এ রাখুন।

**কোন thread-এ — `flowOn`:**

```kotlin
repo.observeNotes()
    .map { notes -> notes.sortedBy { it.title } }
    .flowOn(Dispatchers.Default)     // উপরের ধাপগুলো Default-এ
    .collect { show(it) }            // collect হয় caller-এর thread-এ
```

**Room আর DataStore সরাসরি `Flow` দেয়।** Database-এ data বদলালে নতুন value নিজে থেকেই চলে আসে — drift-এর `.watch()`-এর মতো। Notes app-এর list screen ঠিক এভাবেই বানানো হবে।

[উপরে ফিরুন](#toc)

### <a id="ch2-9"></a>২.৯ `ValueNotifier` → `StateFlow`

**এক লাইনে:** `StateFlow` হলো একটা hot stream, যেটা সবসময় একটা current value ধরে রাখে। Hot মানে কেউ না শুনলেও এর value থাকে। এটা `ValueNotifier` আর Bloc-এর state stream — দুটো মিলিয়ে একটা জিনিস।

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

**কেন `update {}`, `value = value + 1` না:** ধরুন দুইটা coroutine দুই thread থেকে একই সময়ে value পড়ল। দুজনেই নিজের হিসাব করে লিখল। তখন একজনের কাজ হারিয়ে যায়। `update {}` লেখার আগে দেখে নেয়, মাঝখানে value বদলেছে কি না। বদলালে আবার চেষ্টা করে। Dart-এ thread একটাই, তাই এটা কখনো ভাবতে হয়নি।

**Cold flow থেকে StateFlow — `stateIn`:**

```kotlin
val notes: StateFlow<List<Note>> = repo.observeNotes()
    .stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = emptyList(),
    )
```

`WhileSubscribed(5_000)` মানে: কেউ না শুনলে ৫ সেকেন্ড পর database query বন্ধ করো। Rotation-এর সময় অল্প সময়ের জন্য কেউ শোনে না। কিন্তু ৫ সেকেন্ড পার হয় না, তাই query বন্ধ হয়ে আবার নতুন করে শুরু হয় না। আর app background-এ গেলে ৫ সেকেন্ড পরে কাজ সত্যিই থামে।

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

দুই পাশ প্রায় লাইন ধরে ধরে মিলে যায়। `debounce` আর `flatMapLatest`-এর জন্য `@OptIn(FlowPreview::class, ExperimentalCoroutinesApi::class)` লাগে। নামে "experimental" থাকলেও এগুলো বহু বছর ধরে production-এ নিয়মিত ব্যবহার হচ্ছে।

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

শেষ লাইনটা interview-এ প্রায়ই আসে। পুরনো যে API listener দিয়ে চলে (location update, Firebase listener), তাকে `callbackFlow { }` দিয়ে Flow বানানো যায়। Dart-এ যেমন `StreamController` দিয়ে callback-কে stream বানাতেন, ঠিক তেমন।

> **মনে রাখুন**
> - Dart-এ একটা thread। Kotlin-এ অনেক thread, আর তারা memory share করে। সব পার্থক্য এখান থেকেই আসে।
> - `Future` → `suspend fun`, `Stream` → `Flow`, `ValueNotifier` → `StateFlow`, `Isolate.run` → `withContext(Dispatchers.Default)`।
> - প্রতিটা coroutine-এর একটা scope আছে। Scope বন্ধ হলে কাজ নিজে থামে — `mounted` check বা `cancel()` লাগে না।
> - `CancellationException` গিলবেন না। `GlobalScope` না।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Coroutine-এ আমি সবসময় structured concurrency মানি: ViewModel-এর কাজ `viewModelScope`-এ, যাতে screen বন্ধ হলে সব নিজে থেকে বাতিল হয়। একবারের কাজ suspend function, বদলাতে থাকা data Flow, আর UI state StateFlow। Dart-এর সাথে বড় পার্থক্য হলো Kotlin-এ আসল thread আর shared memory, তাই আমি state immutable রাখি আর `update {}` দিয়ে বদলাই।"
> - *English:* "With coroutines I follow structured concurrency: ViewModel work runs in `viewModelScope`, so everything is cancelled when the screen goes away. One-shot work is a suspend function, changing data is a Flow, and UI state is a StateFlow. The big difference from Dart is that Kotlin has real threads and shared memory, so I keep state immutable and change it with `update {}`."

[উপরে ফিরুন](#toc)

---
## <a id="ch3"></a>৩. Project আর Gradle — `pubspec.yaml`-এর জায়গায়

Flutter-এ `pubspec.yaml` খুব সোজা একটা file। নাম, version, কয়েকটা dependency — এই তো। Android-এর Gradle প্রথম দেখায় জটিল লাগে, কারণ এতে অনেক file আর অনেক setting। ভয় পাওয়ার কিছু নেই। আপনার Flutter project-এর `android/` folder-এ এই file-গুলো সবসময়ই ছিল। এখন শুধু কোন file কী কাজ করে, সেটা চিনে নেব।

**এক লাইনে:** Flutter-এ `pubspec.yaml` একাই যে কাজ করে, Android-এ সেটা তিনটা file ভাগ করে করে:
- `settings.gradle.kts` — project-এ কোন কোন module আছে।
- `libs.versions.toml` — সব library-র version।
- `app/build.gradle.kts` — dependency আর app-এর setting।

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

**Android-এ কাজটা দুই ধাপে হয়।** প্রথমে catalog file-এ library-র নাম আর version লিখে রাখেন:

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

তারপর module-এর file-এ সেই নাম ধরে ব্যবহার করেন:

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

**কোথায় মিল, কোথায় আলাদা:**

| Flutter | Android |
|---|---|
| `dependencies:` | `implementation(...)` |
| `dev_dependencies:` | `testImplementation(...)`, `debugImplementation(...)` |
| `build_runner` + generator package | `ksp(...)` — compile-এর সময় নিজে নিজে চলে, আলাদা command দিতে হয় না |
| Flutter SDK-র version-ই সব widget-এর version ঠিক করে দেয় | **BOM** — একটা সংখ্যা দিলেই Compose-এর সব library-র মিলানো version চলে আসে |
| `flutter pub get` | Gradle sync (Android Studio-তে হাতির ছবিওয়ালা button) |

**KSP** হলো `build_runner`-এর বদলি। Room, Hilt, Moshi-র মতো library আপনার code-এর annotation দেখে নিজে code বানিয়ে দেয়। এই কাজটাই KSP করে। Flutter-এ এর জন্য আপনাকে হাতে `dart run build_runner build` চালাতে হতো। এখানে build-এর সময় এটা নিজেই চলে। পুরনো project-এ `kapt` দেখবেন। ওটাও একই কাজ করে, কিন্তু ধীরে। নতুন code-এ KSP নিন।

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
| `minSdk` | এর চেয়ে পুরনো Android-এ app install হবে না |
| `compileSdk` | কোন SDK-র API দেখে code compile হবে। নতুন API ব্যবহার করতে চাইলে এটা বাড়াতে হয়। |
| `targetSdk` | App কোন Android version-এর নিয়ম মেনে চলবে। Play Store প্রতি বছর এটা বাড়াতে বলে। আর বাড়ালে সেই version-এর নতুন behavior চালু হয়ে যায়। |

Flutter-এ এগুলো `android/app/build.gradle`-এ default হিসেবে বসানো থাকত, যেমন `flutter.minSdkVersion`। এখন কোনটা কত হবে, সেটা আপনি নিজে ঠিক করবেন।

**Best approach:** নতুন project খুলুন Android Studio-র "Empty Activity" template দিয়ে। এতে version catalog, Compose, Kotlin DSL — সব আগে থেকেই সাজানো থাকে। Gradle file একদম শুরু থেকে হাতে লিখতে হয় না।

**Module:** বড় app-এ শুধু একটা `app` module থাকে না, অনেকগুলো module থাকে। যেমন `:core:database`, `:feature:notes`। এটা Flutter-এ `packages/` folder-এ local package রাখার মতো। এতে দুইটা লাভ:
- যে module বদলেছে, শুধু সেটাই আবার build হয়।
- `internal` দিয়ে module-এর ভেতরের জিনিস বাইরে থেকে লুকিয়ে রাখা যায়।

শেখার সময় একটা module-ই যথেষ্ট।

> **মনে রাখুন**
> - `pubspec.yaml`-এর বদলে `libs.versions.toml` + `build.gradle.kts`। `build_runner`-এর বদলে KSP।
> - BOM একটা সংখ্যা দিয়েই সব Compose library-র version মিলিয়ে দেয়।
> - `minSdk`, `compileSdk`, `targetSdk` তিনটা আলাদা জিনিস। `targetSdk` বাড়ালে নতুন নিয়ম চালু হয়।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি সব dependency version catalog-এ এক জায়গায় রাখি। Compose-এর জন্য BOM ব্যবহার করি। Code generation-এর জন্য KSP নিই, কারণ এটা kapt-এর চেয়ে দ্রুত। `targetSdk` বাড়ানোর আগে আমি ওই version-এ কী কী behavior বদলেছে সেটা পড়ি, তারপর test করি।"
> - *English:* "I keep dependencies in a version catalog, use the BOM for Compose, and use KSP for code generation because it's faster than kapt. Before raising `targetSdk`, I read that version's behavior changes and test them."

[উপরে ফিরুন](#toc)

---

## <a id="ch4"></a>৪. App-এর component: Application, Activity, Manifest, Context

আপনি যখন Java-তে Android লিখতেন, তখন প্রতিটা screen ছিল একটা করে Activity। এক screen থেকে আরেক screen-এ যেতেন `startActivity` দিয়ে। এখন ছবিটা বদলে গেছে, আর অনেকটা Flutter-এর মতো হয়ে গেছে: একটাই Activity, আর তার ভেতরে পুরো app। তবে Activity, Manifest, Context — এই মূল জিনিসগুলো আগের মতোই আছে। এগুলো ছাড়া কোনো Android app চলতেই পারে না।

### <a id="ch4-1"></a>৪.১ চালু হওয়া: `main()` থেকে Activity

**এক লাইনে:** Flutter-এ `main()` আর `runApp()` যে কাজ করে, Android-এ সেটা দুই জায়গায় ভাগ হয়ে যায়:
- `Application` — পুরো app-এর জন্য একবারের setup।
- `MainActivity` — UI বসানো।

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

**ভেতরে কী হয়, ধাপে ধাপে:**
1. User app-এর icon-এ tap করে। System তখন একটা Linux process চালু করে।
2. Process-এর ভেতরে সবার আগে `Application` তৈরি হয়। এটা একটাই থাকে, process যতক্ষণ বেঁচে থাকে ততক্ষণ।
3. Manifest-এ যে Activity-কে "launcher" বলে লেখা আছে, সেটা তৈরি হয়। তারপর তার `onCreate()` চলে।
4. `setContent { }` Compose-এর UI screen-এ বসিয়ে দেয়।

[উপরে ফিরুন](#toc)

### <a id="ch4-2"></a>৪.২ Manifest

**এক লাইনে:** Manifest একটা XML file। এতে app নিজের সম্পর্কে system-কে সব জানায়। App চালানোর আগে system এই file পড়ে নেয়।

Flutter-এ permission যোগ করতে আপনি এই file-টাই খুলতেন — `android/app/src/main/AndroidManifest.xml`। এটা সেই একই file:

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

- **এতে কী থাকে:** app-এ কোন কোন component আছে, কোন permission চায়, আর কোন link বা intent ধরতে পারে। (Intent মানে system-এর কাছে পাঠানো একটা অনুরোধ, যেমন "এই link খোলো"।)
- **Library-র manifest আপনার manifest-এর সাথে মিশে যায়।** Flutter-এ plugin-এর permission নিজে থেকেই আপনার manifest-এ চলে আসত। এই মেশানোর কাজটাকেই manifest merger বলে। শেষে manifest দেখতে কেমন হলো, সেটা দেখতে Android Studio-তে Manifest খুলে নিচের **Merged Manifest** tab-এ যান। কোন library কোন permission ঢুকিয়েছে, সেটা এখানেই ধরা পড়ে।
- **`android:exported="true"`** মানে অন্য app-ও এই Activity চালু করতে পারবে। Launcher Activity-তে এটা লাগবেই। অন্য জায়গায় দরকার না থাকলে `false` দিন। এটা security-র ব্যাপার।

[উপরে ফিরুন](#toc)

### <a id="ch4-3"></a>৪.৩ চারটা component

**এক লাইনে:** একটা Android app চার রকম জিনিস দিয়ে তৈরি। চারটাই Manifest-এ লিখে দিতে হয়। Flutter-এ এদের প্রত্যেকটার কাজ কোনো না কোনো plugin করে দিত।

| Component | কাজ | Notes app-এ উদাহরণ | Flutter-এ কে করত |
|---|---|---|---|
| **Activity** | একটা window বা screen | `MainActivity` — পুরো app | `FlutterActivity` |
| **Service** | UI ছাড়া পেছনে কাজ করা | Note-এর জন্য voice recording চলছে | `audio_service`-এর মতো plugin |
| **BroadcastReceiver** | System-এ কিছু ঘটলে সেই খবর শোনা | Phone restart হলে reminder আবার set করা | `android_alarm_manager_plus` |
| **ContentProvider** | অন্য app-কে data দেওয়া; file share করা | Note-এর ছবি অন্য app-এ share করা (`FileProvider`) | `share_plus` |

**Single-Activity:** আগে প্রতিটা screen ছিল আলাদা একটা Activity। আপনিও সম্ভবত সেভাবেই লিখেছেন। এখন একটাই Activity থাকে। তার ভেতরে Compose-এর navigation দিয়ে সব screen চলে। ঠিক Flutter-এর মতো — সেখানেও একটা `FlutterActivity`-র ভেতরে Navigator সব route চালায়।

মাঝখানে একটা সময় ছিল, যখন একটা Activity-র ভেতরে **Fragment** দিয়ে screen বানানো হতো। পুরনো project-এ Fragment দেখবেন। Fragment-এর নিজের lifecycle আছে। আর Fragment-এর view, Fragment-এর আগেই destroy হয়ে যায়। নতুন Compose app-এ Fragment প্রায় লাগেই না।

[উপরে ফিরুন](#toc)

### <a id="ch4-4"></a>৪.৪ Context — `BuildContext` না

**এক লাইনে:** নাম দেখতে একই রকম, কিন্তু কাজ একদম আলাদা। `BuildContext` হলো widget tree-তে আপনার widget-এর ঠিকানা। Android-এর `Context` দিয়ে আপনি system-এর জিনিস ব্যবহার করেন — resource, system service, file, অন্য screen চালু করা।

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

Compose-এ tree-র ওপর থেকে Theme খোঁজার কাজটা করে `CompositionLocal` ([৬.৮](#ch6-8))। আর Context দরকার হলে `LocalContext.current` দিয়ে পান।

**Context দুই রকম। গুলিয়ে ফেললে memory leak হয়:**

| | Activity context | Application context |
|---|---|---|
| কতদিন বাঁচে | Activity যতক্ষণ আছে — phone ঘোরালে মরে যায় | Process যতক্ষণ আছে |
| Theme জানে কি না | হ্যাঁ | না |
| কোথায় ব্যবহার | UI, dialog, যেখানে theme লাগে | Singleton, repository, database |

**ফাঁদ:** কিছু object Activity-র চেয়ে বেশিদিন বাঁচে — যেমন singleton, ViewModel, static field। এরা কখনো Activity context ধরে রাখবে না। ধরে রাখলে কী হয়? Phone ঘোরালে পুরনো Activity-র কাজ শেষ হয়ে যায়। কিন্তু singleton তখনও তাকে ধরে আছে, তাই system তাকে memory থেকে মুছতে পারে না। পুরনো Activity আর তার পুরো screen memory-তে আটকে থাকে।

Flutter-এ dispose হওয়ার পরে `BuildContext` ব্যবহার করলে error আসে, তাই ভুলটা চোখে পড়ে। Android-এ কোনো error আসে না। App শুধু চুপচাপ memory খেতে থাকে। এই ধরনের leak খুঁজতে LeakCanary library ব্যবহার করুন।

[উপরে ফিরুন](#toc)

### <a id="ch4-5"></a>৪.৫ পুরনো View system — যা আপনি জানতেন

Interview-এ আর পুরনো code-এ এটা আসবেই। তাই একবার চোখ বুলিয়ে চিনে রাখুন। আপনি যখন Java-তে Android লিখতেন, তখন UI লেখা হতো এভাবে:

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
| `view.text = x` — হাতে বদলানো | State বদলালে নিজে বদলায় | `setState` |
| `findViewById` / ViewBinding | (লাগে না) | (লাগে না) |

**বড় পার্থক্য:** View system হলো imperative। মানে আপনি view-কে হুকুম দেন: "এখন এই text দেখাও।" Compose আর Flutter হলো declarative। মানে আপনি শুধু বলে দেন: "state এরকম হলে UI দেখতে এরকম হবে।" তাই Flutter-এ আপনি যেভাবে ভাবেন, Compose-এ ঠিক সেভাবেই ভাবতে পারবেন।

Compose আর পুরনো View একসাথেও চলতে পারে:
- পুরনো screen-এর ভেতরে Compose বসাতে `ComposeView`।
- Compose-এর ভেতরে পুরনো View (যেমন MapView) বসাতে `AndroidView`।

এটা Flutter-এর `AndroidView` (platform view)-এর মতো।

> **মনে রাখুন**
> - `main()` + `runApp()`-এর বদলে `Application` + `MainActivity.setContent { }`।
> - Manifest-এ app নিজের সব তথ্য system-কে জানায়। Library-র manifest আপনার manifest-এর সাথে মিশে যায়।
> - Component চারটা: Activity, Service, BroadcastReceiver, ContentProvider।
> - `Context` আর `BuildContext` এক জিনিস না। যে object অনেকদিন বাঁচে, তাতে Activity context রাখবেন না।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি single-Activity architecture ব্যবহার করি। একটাই Activity, আর তার ভেতরে Compose navigation দিয়ে সব screen — Flutter-এর মতোই। Context নিয়ে আমি সাবধান থাকি। ViewModel বা singleton-এ কখনো Activity context রাখি না। ওখানে Context লাগলে application context দিই।"
> - *English:* "I use a single-Activity architecture — one Activity with all screens in Compose navigation, much like Flutter. I'm careful with Context: I never keep an Activity context in a ViewModel or singleton; if I need one there, I use the application context."

[উপরে ফিরুন](#toc)

---

## <a id="ch5"></a>৫. Lifecycle, rotation আর process death

Flutter developer-রা Android-এ এসে সবচেয়ে বড় ধাক্কা খায় এই অধ্যায়ের বিষয়ে। Flutter-এ phone ঘোরালে তেমন কিছুই হয় না। Layout বদলায়, কিন্তু `State` বেঁচে থাকে। User-এর অর্ধেক লেখা note যেমন ছিল তেমনই থাকে।

Android-এ ব্যাপারটা আলাদা:
- Phone ঘোরালে আপনার Activity মরে যায়, আর তার জায়গায় নতুন একটা Activity তৈরি হয়।
- App background-এ থাকলে system কোনো খবর না দিয়েই পুরো app বন্ধ করে দিতে পারে।

শুনে ভয় লাগে। কিন্তু নিয়মগুলো জানা থাকলে সমাধান সহজ।

### <a id="ch5-1"></a>৫.১ App lifecycle

**এক লাইনে:** Flutter-এর `didChangeAppLifecycleState`-এর বদলে Android-এ আছে `Lifecycle`। এটা প্রতিটা Activity-র আলাদা আছে, আবার পুরো process-এরও একটা আছে।

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

**Activity-র ধাপগুলো, Flutter-এর পাশে রেখে:**

```
onCreate()   ─ তৈরি হলো                        (Flutter: engine চালু, initState)
onStart()    ─ screen দেখা যাচ্ছে              (AppLifecycleState.resumed-এর কাছাকাছি)
onResume()   ─ সামনে আছে, touch পাচ্ছে         (resumed)
   ··· চলছে ···
onPause()    ─ অন্য কিছু সামনে এল (dialog-ধরনের activity, multi-window)   (inactive)
onStop()     ─ আর দেখা যাচ্ছে না (home চাপা)   (paused / hidden)
onDestroy()  ─ শেষ — back চাপা, বা configuration change                 (detached)
```

- **STARTED** মানে screen দেখা যাচ্ছে। UI-র জন্য data collect করার ঠিক সময় এটাই। `collectAsStateWithLifecycle()` ঠিক এই নিয়মে চলে।
- **RESUMED** মানে screen সবার সামনে আর focus পাচ্ছে। Camera বা sensor-এর মতো জিনিস এই অবস্থায় চালু করুন।
- `onStop()`-এর পরে system যেকোনো সময় process বন্ধ করে দিতে পারে। তাই জরুরি জিনিস তার আগেই save করে ফেলুন।

শুধু জানতে চান পুরো app foreground-এ আছে নাকি background-এ? তাহলে `ProcessLifecycleOwner` ব্যবহার করুন। এটা Flutter-এর app-level lifecycle-এর সাথে বেশি মেলে।

[উপরে ফিরুন](#toc)

### <a id="ch5-2"></a>৫.২ Rotation-এ Activity মরে যায়

**এক লাইনে:** Phone ঘোরালে, dark mode চালু করলে, ভাষা বা font size বদলালে, বা window-এর মাপ বদলালে Android পুরনো Activity destroy করে নতুন একটা বানায়। একে বলে **configuration change**।

**Android এটা কেন করে:** নতুন configuration-এ আলাদা resource লাগতে পারে। যেমন landscape-এর জন্য আলাদা layout, অন্য ভাষার string, dark theme-এর রং। পুরো Activity নতুন করে বানালে সব resource নতুন করে load হয়ে যায়। Flutter এসব নিজেই সামলায়। তাই আপনাকে এটা নিয়ে কখনো ভাবতে হয়নি।

**কী হারায়:** Activity-র field, আর composable-এ `remember` দিয়ে রাখা state।

**কী বেঁচে থাকে:** ViewModel। কারণটা ধাপে ধাপে:
1. প্রতিটা Activity-র একটা `ViewModelStore` থাকে। এটা একটা map, যেখানে ওই Activity-র সব ViewModel রাখা থাকে।
2. Activity destroy হওয়ার সময় system জানে যে এটা configuration change।
3. তাই system এই store-টা ফেলে না দিয়ে নতুন Activity-কে দিয়ে দেয়।
4. ফলে নতুন Activity আগের ViewModel-টাই ফেরত পায়।

User সত্যি সত্যি back চেপে screen থেকে বের হয়ে গেলে তখন store মুছে ফেলা হয় (clear হয়)। তখন ViewModel-এর `onCleared()` চলে।

**নিজে দেখুন:** Notes app-এ `remember { mutableStateOf("") }` দিয়ে একটা text field বানান। কিছু লিখুন, তারপর phone ঘোরান। লেখাটা মুছে যাবে। এবার এর বদলে `rememberSaveable` দিন। এবার লেখাটা থেকে যাবে।

[উপরে ফিরুন](#toc)

### <a id="ch5-3"></a>৫.৩ State কোথায় রাখবেন

পুরো অধ্যায়ের সারকথা এই এক table-এ:

| State | কোথায় রাখবেন | Rotation-এ | Process death-এ | Flutter-এ |
|---|---|---|---|---|
| ছোট UI state (dropdown খোলা কি না) | `remember` | হারায় | হারায় | `State`-এর field |
| যে UI state হারানো চলবে না (লেখা text, বেছে নেওয়া tab) | `rememberSaveable` | থাকে | থাকে | `RestorationMixin` |
| Screen-এর state আর logic | `ViewModel` | থাকে | হারায় | Cubit |
| ViewModel-এর ছোট কিন্তু জরুরি state (search query, যে note edit হচ্ছে তার id) | `SavedStateHandle` | থাকে | থাকে | (নেই) |
| আসল data | Room, DataStore, server | থাকে | থাকে | drift, shared_preferences |

**Best approach:**
- আসল data সবসময় database-এ রাখুন। ViewModel সেখান থেকে পড়বে।
- User হাতে যে কাজ করছে (অর্ধেক লেখা note, search), সেটা রাখুন `SavedStateHandle` বা `rememberSaveable`-এ।

তাহলে যা-ই ঘটুক, user-এর কাজ হারাবে না।

[উপরে ফিরুন](#toc)

### <a id="ch5-4"></a>৫.৪ Process death

**এক লাইনে:** App background-এ থাকলে, memory খালি করার জন্য system পুরো process বন্ধ করে দিতে পারে। User ফিরে এলে Android app-কে ঠিক আগের screen-এ খোলে। কিন্তু memory-তে যা ছিল, সব নতুন আর খালি।

**ঘটনাটা এরকম:**
1. User Notes app-এ একটা note লিখছে। অর্ধেক লিখে ছবি তুলতে camera খুলল।
2. Camera app অনেক memory চাইল। তাই system আপনার background-এ থাকা process বন্ধ করে দিল। আপনার code-এ কোনো callback আসে না, তাই আপনি টেরও পান না।
3. User ছবি তুলে ফিরে এল। System নতুন একটা process চালু করল। তারপর **সরাসরি note লেখার screen** খুলল, আগের back stack-সহ — যেন কিছুই হয়নি।
4. কিন্তু ভেতরে সব নতুন। ViewModel নতুন, singleton নতুন, static variable খালি। শুধু `rememberSaveable` আর `SavedStateHandle`-এ রাখা জিনিসগুলো ফেরত আসে।

Flutter app-এ এটা সাধারণত "cold start"-এর মতো দেখায়, আর বেশিরভাগ app একদম শুরু থেকে খোলে। কিন্তু native Android app-এর কাছে system আশা করে, app ঠিক যেখানে ছিল সেখান থেকেই আবার চলবে।

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
- **বড় data Bundle-এ রাখবেন না।** `SavedStateHandle` আর `rememberSaveable` তাদের data Bundle নামের একটা জিনিসে save করে। Bundle-এর একটা সীমা আছে — পুরো transaction মিলিয়ে মোটামুটি ১ MB। তাই note-এর পুরো list রাখবেন না। শুধু id আর অর্ধেক লেখা text রাখুন। List পরে database থেকে আবার চলে আসবে।
- **"Splash screen-এ সব load করি, বাকি screen-গুলো singleton থেকে পড়ে"** — এই pattern process death-এর পরে crash করে। কারণ app তখন সরাসরি ভেতরের screen-এ খোলে। Splash screen চলেই না, তাই singleton খালি থাকে।

**নিজে test করুন:**
1. App চালান। একটা note-এ কিছু লিখুন। তারপর home button চাপুন।
2. Terminal-এ এটা চালান: `adb shell am kill com.byteonyx.notes`
3. Recent apps থেকে app-টা আবার খুলুন।

যা যা হারিয়ে গেল, সেগুলো সবই bug। Developer options-এ **"Don't keep activities"** চালু করেও প্রায় একই রকম test করা যায়।

> **মনে রাখুন**
> - Phone ঘোরালে Activity মরে, কিন্তু ViewModel বাঁচে। Process death-এ দুটোই মরে।
> - কোনটা কতটা টেকে, কম থেকে বেশি: `remember` < `rememberSaveable` < ViewModel < `SavedStateHandle` < database।
> - Bundle-এ শুধু ছোট জিনিস রাখুন। বড় data আসবে database থেকে।
> - প্রতিটা screen `adb shell am kill` দিয়ে test করুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Configuration change-এ ViewModel বেঁচে থাকে, কারণ ViewModelStore নতুন Activity-কে দিয়ে দেওয়া হয়। কিন্তু process death-এ ViewModel-ও চলে যায়। তাই আমি আসল data database-এ রাখি। আর user-এর অর্ধেক করা কাজ — যেমন draft বা search query — রাখি `SavedStateHandle`-এ। এটা আমি `adb shell am kill` দিয়ে test করি।"
> - *English:* "A ViewModel survives configuration changes because the ViewModelStore is handed to the new Activity, but it doesn't survive process death. So I keep real data in the database and the user's in-progress work, like a draft or a search query, in `SavedStateHandle`. I test it with `adb shell am kill`."

[উপরে ফিরুন](#toc)

---

## <a id="ch6"></a>৬. Jetpack Compose — Widget-এর জায়গায় Composable

এবার সবচেয়ে মজার অধ্যায়। আপনি যখন Java-তে Android লিখতেন, তখন UI মানে ছিল XML, `findViewById`, আর হাতে হাতে `textView.setText()`। Compose এসে এই পুরো পদ্ধতি বাদ দিয়ে দিয়েছে। আর নতুন যে পথ নিয়েছে, সেটা আপনার খুব চেনা: **UI = f(state)।** মানে, UI হলো state-এর একটা function। আপনি state বদলান। UI-র যে অংশ বদলানো দরকার, framework নিজেই সেটা আবার এঁকে দেবে।

এই অধ্যায়ে আপনার Flutter-এর অভিজ্ঞতা সবচেয়ে বেশি কাজে লাগবে। প্রায় প্রতিটা widget-এর একটা জোড়া এখানে পাবেন।

### <a id="ch6-1"></a>৬.১ Widget → Composable

**এক লাইনে:** Widget class আর তার `build()`-এর বদলে এখানে একটা সাধারণ function লেখেন। শুধু তার মাথায় `@Composable` বসিয়ে দেন।

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

**কোথায় মিল, কোথায় আলাদা:**

| Flutter | Compose |
|---|---|
| Widget class + `build()` | `@Composable` function |
| `build()` একটা widget ফেরত দেয় | Composable কিছুই ফেরত দেয় না — call করলেই UI-তে বসে যায় |
| constructor parameter | function parameter |
| `child:` / `children:` | শেষের lambda (trailing lambda) — `Card { ... }` |
| `const` দিয়ে rebuild এড়ানো | কোন function skip করা যায়, compiler নিজেই বুঝে নেয় |
| `StatelessWidget` | parameter নেয় এমন সাধারণ composable |
| `StatefulWidget` | ভেতরে `remember { mutableStateOf() }` ([৬.৫](#ch6-5)) |
| `Key` | `key(id) { }`, list-এ `items(key = { it.id })` |

**নামের নিয়ম:**
- যে composable UI বসায়, তার নাম বড় হাতের অক্ষরে শুরু হয়, আর সেটা একটা noun: `NoteCard`।
- যে composable একটা value ফেরত দেয়, তার নাম ছোট হাতের অক্ষরে শুরু হয়: `rememberScrollState()`।

**কোথা থেকে call করা যায়:** শুধু আরেকটা composable-এর ভেতর থেকে। `onClick`-এর ভেতর থেকে না, কারণ ওটা একটা সাধারণ lambda। Flutter-এ `onPressed`-এর ভেতরে widget বানালে কোনো লাভ হয় না, কিন্তু কেউ আটকায়ও না। এখানে compiler নিজেই আটকে দেয়।

**ভেতরে কী হয় — তিনটা phase:** প্রতিটা frame-এ Compose তিন ধাপে কাজ করে। এটা Flutter-এর build → layout → paint-এর মতো:
1. **Composition** — কী দেখাবে, সেটা ঠিক হয়। এই সময় আপনার function চলে।
2. **Layout** — প্রতিটা জিনিসের মাপ আর জায়গা ঠিক হয়।
3. **Drawing** — screen-এ আঁকা হয়।

State কোন phase-এ পড়া হচ্ছে, তার ওপর ঠিক হয় কোন phase আবার চালাতে হবে আর কোনটা বাদ দেওয়া যাবে। Performance-এর সময় এটা কাজে লাগবে ([৬.১৩](#ch6-13))।

[উপরে ফিরুন](#toc)

### <a id="ch6-2"></a>৬.২ Layout

**এক লাইনে:** `Column` আর `Row` একই নামে আছে। `Stack`-এর নাম এখানে `Box`। আর `Expanded`, `Padding`, `SizedBox` — এগুলো সব এখন Modifier।

**Notes app-এর একটা header, দুই framework-এ পাশাপাশি:**

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

**ফাঁদ:** নতুন Android-এ (targetSdk 35+) app default হিসেবে পুরো screen জুড়ে আঁকে। Status bar আর navigation bar-এর নিচেও আঁকে। একে edge-to-edge বলে। তাই `innerPadding` না দিলে আপনার content ওই bar-গুলোর নিচে ঢাকা পড়ে যাবে। Flutter-এ `SafeArea` যে কাজ করত, এখানে `innerPadding` সেই কাজ করে।

[উপরে ফিরুন](#toc)

### <a id="ch6-3"></a>৬.৩ Wrapper widget → Modifier

**এক লাইনে:** Flutter-এ padding, size, রং, tap — প্রতিটার জন্য একটা করে wrapper widget লাগে। Compose-এ এগুলো সব একটা chain-এ লেখা হয়। এর নাম **Modifier**।

**Flutter-এ — অনেক স্তরের tree:**

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

**Compose-এ — একটা chain:**

```kotlin
Text(
    note.title,
    modifier = Modifier
        .clickable { onTap() }
        .background(Color.Yellow)
        .padding(16.dp),
)
```

**কোনটা আগে, কোনটা পরে — এটা গুরুত্বপূর্ণ।** Modifier বাইরে থেকে ভেতরের দিকে কাজ করে, ঠিক Flutter-এর wrapper-এর মতো:

```kotlin
Modifier.padding(16.dp).background(Color.Yellow)   // = Padding(child: Container(color: yellow))
Modifier.background(Color.Yellow).padding(16.dp)   // = Container(color: yellow, padding: 16)
```

- প্রথম লাইনে হলুদ অংশটা ছোট। তার চারপাশে ফাঁকা জায়গা।
- দ্বিতীয় লাইনে ফাঁকা জায়গাটাও হলুদ।

`clickable`-এর বেলাতেও একই কথা। আগে দিলে tap করার জায়গা বড় হয়। পরে দিলে ছোট হয়।

**Best approach — modifier parameter-এর নিয়ম:** যে composable বারবার ব্যবহার হবে, সেটা একটা `modifier: Modifier = Modifier` parameter নেবে। আর এটা নিজের সবচেয়ে বাইরের (root) element-এ সবার আগে লাগাবে। তাহলে যে call করছে, সে বাইরে থেকে size বা padding দিতে পারবে। Compose-এ এটাই সবচেয়ে বেশি মানা নিয়ম। Code review-এ এটা না থাকলে প্রশ্ন উঠবে।

[উপরে ফিরুন](#toc)

### <a id="ch6-4"></a>৬.৪ `ListView.builder` → `LazyColumn`

**এক লাইনে:** `LazyColumn` শুধু screen-এ যে item-গুলো দেখা যাচ্ছে, সেগুলোই বানায় — ঠিক `ListView.builder`-এর মতো। পুরনো Android-এ এর জন্য `RecyclerView` + Adapter + ViewHolder — অনেক ঝামেলা লাগত। এখানে সব এক function-এ হয়ে যায়।

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

- `LazyColumn`-এর `{ }`-এর ভেতরে আপনি সরাসরি composable লেখেন না। ওটা একটা ছোট আলাদা ভাষা (DSL)। তাই সেখানে `item {}` আর `items()` ব্যবহার করতে হয়।
- **`key` দিন।** না দিলে কী হয়? কোনো item জায়গা বদলালে তার state (যেমন expand করা আছে কি না) ভুল item-এ চলে যায়। Animation-ও ভুল হয়। Flutter-এ `Key` না দিলে যে সমস্যা হয়, এটাও তেমন।
- List-এ আলাদা আলাদা ধরনের item থাকলে `contentType` দিন। তাহলে Compose ভেতরের জিনিস আরও ভালোভাবে আবার ব্যবহার (reuse) করতে পারে।

**ফাঁদ:** `LazyColumn`-এর ভেতরে একই দিকে scroll করা আরেকটা `LazyColumn` দেবেন না। এতে app crash করে। কারণ ভেতরেরটা অসীম উচ্চতা পায়। Flutter-এ `ListView`-এর ভেতরে `ListView` দিলে যে "unbounded height" error আসে, এটা সেরকম।

[উপরে ফিরুন](#toc)

### <a id="ch6-5"></a>৬.৫ `setState` → `mutableStateOf`

**এক লাইনে:** `StatefulWidget`-এর field আর `setState`-এর বদলে এখানে `remember { mutableStateOf() }`। Value বদলালেই UI আবার আঁকা হয়। আলাদা করে কিছু call করতে হয় না।

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

এখানে দুইটা আলাদা জিনিস একসাথে কাজ করছে:

- **`mutableStateOf(false)`** — একটা state object, যার value বদলালে Compose টের পায় (observable)। কোন কোন composable এর value পড়েছে, Compose সেটা মনে রাখে। Value বদলালে শুধু সেই composable-গুলোই আবার চলে।
- **`remember { }`** — এই state object-টাকে বারবার চলার মাঝে বাঁচিয়ে রাখে। Flutter-এ `State` object নিজেই বেঁচে থাকে, তাই তার field-ও থেকে যায়। কিন্তু Compose-এ function বারবার চলে। `remember` না দিলে প্রতিবার নতুন একটা state object তৈরি হতো। তখন `pinned` সবসময় `false` থাকত।

**ভেতরে কী হয় — recomposition বনাম rebuild:** (Composable আবার চলাকে recomposition বলে।)

| | Flutter | Compose |
|---|---|---|
| কে আবার চলে | যে widget-এ `setState` হলো, তার `build()` আর তার নিচের পুরো subtree | শুধু যে composable ওই state পড়েছে, আর যার parameter বদলেছে |
| Skip কীভাবে হয় | `const` দিয়ে, বা widget ছোট ছোট ভাগ করে | Compiler দেখে: parameter আগের মতো থাকলে skip |
| কোন ক্রমে চলে | একটার পর একটা, ক্রম মেনে | যেকোনো ক্রমে, বারবার, এমনকি মাঝপথে বাতিলও হতে পারে |

শেষ লাইনটা থেকেই সবচেয়ে জরুরি নিয়মটা আসে: **composable-এর body-তে side effect দেবেন না।** Side effect মানে এমন কাজ যা function-এর বাইরে কিছু বদলায় — network call, analytics, বাইরের কোনো variable বদলানো। এগুলো সরাসরি body-তে লিখলে প্রতিটা recomposition-এ চলবে। হয়তো সেকেন্ডে ৬০ বার! Flutter-এ `build()`-এর ভেতরে API call না করার যে নিয়ম, এখানে সেটা আরও কড়া। Side effect-এর জন্য আলাদা API আছে ([৬.৭](#ch6-7))।

**`rememberSaveable`** — এটা phone ঘোরালে আর process death-এর পরেও বেঁচে থাকে ([৫.৩](#ch5-3)):

```kotlin
var draft by rememberSaveable { mutableStateOf("") }
```

**ফাঁদ — list state:** ধরুন `mutableStateOf(mutableListOf<Note>())` লিখলেন, তারপর list-এ `add()` করলেন। Compose এটা টের পায় না। কারণ state-এর ভেতরের list object-টা একই আছে, শুধু তার ভেতরে একটা item বেড়েছে। Flutter-এ list-এ `add` করে `setState` না দিলে যেমন হয়, তেমন। সমাধান দুইটা:
- পুরো নতুন একটা list দিন: `notes = notes + newNote`।
- অথবা `mutableStateListOf()` ব্যবহার করুন।

[উপরে ফিরুন](#toc)

### <a id="ch6-6"></a>৬.৬ Lifting state up

**এক লাইনে:** Flutter-এ যাকে "lift state up" বলেন, Compose-এ তাকে বলে **state hoisting**। মানে composable নিজের ভেতরে state রাখে না। বাইরে থেকে value আর callback নেয়।

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

চিন্তাটা একই, লাভও একই। Stateless composable সহজে বারবার ব্যবহার করা যায়, আর এর preview আর test করাও সহজ। এই pattern-এর নাম **unidirectional data flow (UDF)**, মানে data একদিকেই চলে: state ওপর থেকে নিচে নামে, event নিচ থেকে ওপরে ওঠে। Bloc-এ আপনি ঠিক এটাই করতেন: state `BlocBuilder` দিয়ে নিচে আসত, event `add()` দিয়ে ওপরে যেত।

**State কতটা ওপরে তুলবেন:** যারা এই state পড়ে বা বদলায়, তাদের সবার সবচেয়ে কাছের common parent পর্যন্ত। আর যদি business logic থাকে (যেমন note save করা), তাহলে ViewModel পর্যন্ত তুলুন ([৮](#ch8))।

[উপরে ফিরুন](#toc)

### <a id="ch6-7"></a>৬.৭ `initState`, `dispose`, `StreamBuilder`

**এক লাইনে:** Widget-এর lifecycle method-এর বদলে Compose-এ আছে "effect"। Composable screen-এ এলে effect চলে। চলে গেলে effect নিজেই পরিষ্কার হয়ে যায়।

| Flutter | Compose | কখন চলে |
|---|---|---|
| `initState`-এ async কাজ | `LaunchedEffect(Unit) { }` | প্রথমবার screen-এ এলে, একবার। ভেতরে suspend code চালানো যায়। |
| `didUpdateWidget` (id বদলালে) | `LaunchedEffect(noteId) { }` | Key বদলালে আগের কাজ বাতিল হয়, তারপর নতুন করে চলে |
| `initState` + `dispose` | `DisposableEffect(key) { onDispose { } }` | কিছু register করা, পরে unregister করা |
| `onPressed`-এ async কাজ | `rememberCoroutineScope()` → `scope.launch { }` | Callback থেকে coroutine চালানো |
| `StreamBuilder` | `flow.collectAsStateWithLifecycle()` | Flow থেকে state |
| `FutureBuilder` | `produceState { value = load() }` | Suspend কাজের ফল থেকে state |
| হাতে cache করে রাখা হিসাব | `derivedStateOf { }` | অন্য state থেকে বের করা হিসাব, যেটা কম বদলায় |

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

**Compose-এ — দুইটা method একটা effect-এই হয়ে যায়:**

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

**`derivedStateOf` কখন লাগে:** যখন input খুব ঘন ঘন বদলায়, কিন্তু ফল কম বদলায়। যেমন scroll position প্রতি pixel-এ বদলায়। কিন্তু "উপরে যাও" button দেখাবে কি না — সেটা বদলায় মাত্র একবার:

```kotlin
val listState = rememberLazyListState()
val showScrollToTop by remember { derivedStateOf { listState.firstVisibleItemIndex > 0 } }
```

**Best approach:** Screen-এর data load করুন ViewModel-এর `init` বা `stateIn`-এ, `LaunchedEffect`-এ না। কেন? `LaunchedEffect`-এ load করলে phone ঘোরালে data আবার load হবে। কারণ তখন composable নতুন করে screen-এ আসে। `LaunchedEffect` রাখুন শুধু UI-র কাজের জন্য: snackbar দেখানো, animation শুরু করা, focus দেওয়া।

[উপরে ফিরুন](#toc)

### <a id="ch6-8"></a>৬.৮ `InheritedWidget` → `CompositionLocal`

**এক লাইনে:** Tree-র ওপর থেকে data নিচে পাঠানো — যেমন `Theme.of(context)` বা Provider করে — Compose-এ এই কাজ হয় `CompositionLocal` দিয়ে।

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

কিছু আগে থেকেই বানানো আছে: `LocalContext`, `LocalLifecycleOwner`, `LocalDensity`, `LocalConfiguration`। `MaterialTheme` নিজেও ভেতরে ভেতরে এটাই ব্যবহার করে।

**ফাঁদ:** এটা DI-এর বদলি না। Repository বা ViewModel এটা দিয়ে পাঠাবেন না। পাঠালে কোন composable কীসের ওপর চলে, সেটা function-এর signature দেখে আর বোঝা যায় না। এটা শুধু theme, density-র মতো "চারপাশের পরিবেশ"-এর জন্য। Business-এর জিনিস দিন parameter দিয়ে, বা Hilt দিয়ে।

`compositionLocalOf` বনাম `staticCompositionLocalOf`:
- প্রথমটায় value বদলালে শুধু যারা value-টা পড়েছে, তারাই আবার চলে।
- দ্বিতীয়টায় value বদলালে নিচের পুরো subtree আবার চলে। কিন্তু value পড়ার খরচ কম।

যে জিনিস প্রায় কখনোই বদলায় না, তার জন্য `static`-টা নিন।

[উপরে ফিরুন](#toc)

### <a id="ch6-9"></a>৬.৯ Theme

**এক লাইনে:** Material 3-এর token-গুলোর (রং, font-এর নাম) নাম Flutter আর Compose-এ প্রায় হুবহু এক। তাই আপনার theme system প্রায় সরাসরি চলে আসবে।

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
| `ColorScheme.fromSeed` | নিজে বানানো `lightColorScheme(...)`, বা Android 12+ এ wallpaper থেকে রং নিতে `dynamicLightColorScheme(context)` |
| `Theme.of(context)` | `MaterialTheme.colorScheme` / `.typography` |
| `ThemeExtension` | নিজের বানানো `CompositionLocal` |
| `MediaQuery.platformBrightnessOf` | `isSystemInDarkTheme()` |

**ফাঁদ:** `res/values/themes.xml`-এও একটা theme থাকে। সেটা শুধু window-এর জন্য — মানে Compose চালু হওয়ার ঠিক আগের মুহূর্তের background আর splash। Compose-এর ভেতরের রং আসে `MaterialTheme` থেকে। এই দুই জায়গার রং না মিললে app খোলার সময় এক ঝলক অন্য রং দেখা যায়।

[উপরে ফিরুন](#toc)

### <a id="ch6-10"></a>৬.১০ TextField

**এক লাইনে:** Flutter-এ text রাখে `TextEditingController`। Compose-এর সাধারণ `TextField`-এ text রাখেন আপনি নিজে। আপনি value দেন, আর `onValueChange`-এ নতুন value হাতে পান।

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

- **ফাঁদ:** `onValueChange`-এ নতুন value বসাতে ভুলে গেলে field-এ কিছুই লেখা যাবে না। Flutter থেকে আসা প্রায় সবাই প্রথম দিন এখানে আটকে যায়।
- **ফাঁদ:** Text যদি ViewModel-এ রাখেন, তাহলে update synchronous রাখুন, মানে সাথে সাথে value বসান। Async করে value ফেরত দিলে (debounce বা network-এর পরে) cursor লাফায়, অক্ষর হারিয়ে যায়।
- **নতুন API:** `rememberTextFieldState()` আর `TextFieldState` দিয়ে চলা `TextField`। এটা `TextEditingController`-এর অনেক কাছাকাছি। আর ওপরের cursor-এর সমস্যাটা এতে নেই। নতুন code-এ এটা দেখে নিন।
- Focus: `FocusNode`-এর বদলে `FocusRequester`। Keyboard বন্ধ করতে: `LocalFocusManager.current.clearFocus()`।

[উপরে ফিরুন](#toc)

### <a id="ch6-11"></a>৬.১১ Animation

**এক লাইনে:** এটা Flutter-এর implicit animation-এর মতোই। আপনি শুধু target value বদলান। Animation নিজে নিজে হয়।

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

Compose-এ default animation প্রায়ই `spring()`। এটা physics-এর নিয়মে চলে। তাই animation-এর মাঝপথে target বদলালেও সুন্দরভাবে নতুন দিকে ঘুরে যায়, ঝাঁকি লাগে না।

[উপরে ফিরুন](#toc)

### <a id="ch6-12"></a>৬.১২ Hot reload নেই: Preview

**এক লাইনে:** Flutter-এর মতো পুরো hot reload Compose-এ নেই। অভ্যাসের দিক থেকে এটাই সবচেয়ে বড় বদল। তার বদলে আছে `@Preview`।

```kotlin
@Preview(showBackground = true)
@Preview(uiMode = Configuration.UI_MODE_NIGHT_YES, name = "Dark")
@Composable
private fun NoteCardPreview() {
    NotesTheme { NoteCard(note = sampleNote, onClick = {}) }
}
```

- **Preview** — app না চালিয়েই Android Studio-র ভেতরে composable দেখা যায়। Light আর dark, বড় font, ছোট screen — সব পাশাপাশি দেখা যায়। Stateless composable-এ এটা সবচেয়ে ভালো চলে। State hoisting-এর এটা আরেকটা বড় লাভ। যে composable ViewModel চায়, তার preview বানানো কঠিন।
- **Live Edit** — app চলার সময় কিছু বদল সাথে সাথে দেখায়। Text, রং বা সংখ্যা বদলালে ভালো কাজ করে। কিন্তু Flutter-এর hot reload-এর মতো সব জায়গায় কাজ করে না।
- **Layout Inspector** — এটা Flutter DevTools-এর widget inspector-এর মতো। এখানে recomposition count দেখা যায়, মানে কোন composable কতবার আবার চলছে।

**Best approach:** প্রতিটা screen দুই ভাগে লিখুন:
- `NotesRoute` — এটা ViewModel নেয়।
- `NotesScreen` — এটা শুধু state আর callback নেয়।

Preview আর test লিখবেন `NotesScreen`-এর জন্য ([৮.৩](#ch8-3))।

[উপরে ফিরুন](#toc)

### <a id="ch6-13"></a>৬.১৩ Performance

শুরুতে এই কয়েকটা নিয়ম মানলেই বেশিরভাগ সমস্যা আর হয় না:

1. **Release build-এ মাপুন।** Debug build-এ Compose অনেক ধীর চলে। Flutter-এ যেমন profile mode-এ মাপেন, তেমন।
2. **List-এ `key` দিন** ([৬.৪](#ch6-4))।
3. **ভারী হিসাব `remember` করে রাখুন:** `val sorted = remember(notes) { notes.sortedBy { it.title } }`। না রাখলে প্রতিটা recomposition-এ আবার sort হবে।
4. **যে state ঘন ঘন বদলায়, সেটা যত দেরিতে পারেন পড়ুন।** Scroll বা animation-এর value দিয়ে position বদলাতে lambda modifier ব্যবহার করুন: `Modifier.offset { IntOffset(0, offset.roundToInt()) }`। তখন value পড়া হয় layout phase-এ। ফলে composition আবার চলে না।
5. **Immutable state রাখুন।** UI state-এ `data class` আর `val` ব্যবহার করুন। Kotlin 2.0.20 থেকে "strong skipping" default হিসেবে চালু। তাই এখন বেশিরভাগ সময় skip নিজেই ঠিকমতো হয়। Flutter-এ immutable state রাখার যে অভ্যাস, এখানেও সেটাই ঠিক।
6. **Baseline Profile।** এটা app-এর গুরুত্বপূর্ণ code আগে থেকেই compile করিয়ে রাখে। এতে Compose app-এর প্রথম launch আর scroll অনেক ভালো হয়।

> **মনে রাখুন**
> - Widget-এর বদলে `@Composable` function। `child`-এর বদলে trailing lambda। Wrapper widget-এর বদলে Modifier — আর Modifier কোন ক্রমে লিখছেন, সেটা গুরুত্বপূর্ণ।
> - `setState`-এর বদলে `remember { mutableStateOf() }`। `remember` না দিলে state হারিয়ে যায়।
> - Body-তে side effect দেবেন না। তার জন্য আছে `LaunchedEffect`, `DisposableEffect`, `rememberCoroutineScope`।
> - State hoisting, lift state up আর UDF — একই চিন্তা। Route আর Screen আলাদা রাখুন।
> - Hot reload নেই, কিন্তু Preview আছে।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Compose-এর চিন্তা Flutter-এর মতোই — UI হলো state-এর function। আমি screen-কে stateless রাখি আর state hoist করি। Side effect শুধু effect API-তে দিই, কারণ recomposition যেকোনো সময়, বারবার হতে পারে। Performance-এর জন্য list-এ key দিই, ভারী হিসাব remember করি, আর release build-এ মাপি।"
> - *English:* "Compose thinks like Flutter — UI is a function of state. I keep screens stateless, hoist state, and put side effects only in effect APIs, because recomposition can happen at any time and many times. For performance, I add keys to lists, remember expensive work, and measure on a release build."

[উপরে ফিরুন](#toc)

---
## <a id="ch7"></a>৭. Navigation — `go_router`-এর জায়গায়

আগে Android-এ নতুন screen খুলতে হলে নতুন একটা Activity বানাতেন, আর `startActivity(intent)` call করতেন। Data পাঠাতেন `intent.putExtra()` দিয়ে। ফল ফেরত আনতেন `onActivityResult` দিয়ে। এখন আর এভাবে করা হয় না। এখন app-এ একটাই Activity থাকে। তার ভেতরে একটা route table থাকে, ঠিক `go_router`-এর মতো।

**এক লাইনে:** `GoRouter`-এর route list-এর জায়গায় আসে `NavHost`। `context.push()`-এর জায়গায় `navController.navigate()`। আর path string-এর বদলে route হয় একটা Kotlin class, যার type compiler check করে (type-safe)।

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
| `redirect` (login check) | start destination বদলে দিন, বা ViewModel-এ check করে navigate করুন |
| `StatefulShellRoute` (bottom nav) | `NavigationBar` + nested graph, `saveState` / `restoreState` |
| `PopScope` | `BackHandler { }` |

**কী আলাদা:**
- **Route হলো একটা Kotlin class।** Argument-এর type compiler check করে। যেখানে `int` চাই, সেখানে `String` দিলে code compile-ই হবে না। go_router-এর typed route-এর মতো, কিন্তু এখানে code generation লাগে না।
- **প্রতিটা destination (মানে প্রতিটা screen)-এর নিজের ViewModel থাকে।** `NoteDetail` screen-এ `hiltViewModel()` call করলে যে ViewModel পাবেন, সেটা শুধু ওই screen-এর। Screen-টা back stack থেকে বের হয়ে গেলে তার ViewModel-ও মুছে যায় (clear হয়)। ViewModel-এর ভেতর থেকে argument পড়তে চাইলে লিখুন `savedStateHandle.toRoute<NoteDetail>()`।
- **System back button।** Android-এ system-এর নিজের একটা back আছে (button বা gesture)। iOS-এ এমন কিছু নেই। এই back-টা Navigation library নিজেই সামলায়। কিন্তু ধরুন back চাপলে "Save না করে বের হবেন?" dialog দেখাতে চান। তখন `BackHandler { }` লিখুন। এটা Flutter-এর `PopScope`-এর মতো।

**Best approach:**
- Screen-এর হাতে `navController` দেবেন না। শুধু একটা callback দিন (`onNoteClick`)। এতে navigation-এর সব logic এক জায়গায় থাকে। আর screen-টা আলাদা করে preview আর test করা যায়। Flutter-এ widget-এর ভেতরে সরাসরি `context.go()` না লিখে বাইরে থেকে callback দেওয়ার মতোই।
- **Argument-এ শুধু id পাঠান, পুরো object না।** Argument একটা Bundle-এ save হয়, আর Bundle-এর মাপের সীমা আছে। তাছাড়া system app মেরে ফেলে আবার চালু করলে (process death) পুরনো object ফেরত আসতে পারে। তাই শুধু id পাঠান, আর screen-এ সেই id দিয়ে repository থেকে data load করুন।

**Navigation 3:** ২০২৫-এর শেষে Navigation 3 নামে একটা নতুন library stable হয়েছে। এখানে back stack একটা সাধারণ list। List-টা আপনি নিজেই রাখেন আর নিজেই বদলান (`rememberNavBackStack`, `NavDisplay`)। ধারণাটা Flutter-এর Navigator 2.0-এর `pages` list-এর কাছাকাছি। নতুন project-এ দুটোই দেখতে পাবেন। শেখার সময় আগে Navigation Compose দিয়ে শুরু করুন, তারপর Nav3 দেখুন।

> **মনে রাখুন**
> - `GoRouter` → `NavHost`, path → `@Serializable` class, `push` → `navigate`।
> - প্রতিটা destination-এর নিজের ViewModel থাকে।
> - Screen-কে callback দিন, `navController` দেবেন না। Argument-এ শুধু id পাঠান।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি একটাই Activity রাখি (single-Activity), আর তাতে Navigation Compose ব্যবহার করি, type-safe route দিয়ে। Screen-কে navController দিই না, callback দিই। Argument-এ শুধু id পাঠাই। তাই system app মেরে আবার চালু করলেও (process death) data repository থেকে ঠিকঠাক আসে।"
> - *English:* "I use Navigation Compose in a single Activity with type-safe routes. I pass callbacks to screens instead of the navController, and only pass ids as arguments, so after process death the data still comes correctly from the repository."

[উপরে ফিরুন](#toc)

---

## <a id="ch8"></a>৮. Architecture — Cubit থেকে ViewModel, `get_it` থেকে Hilt

আপনি Flutter-এ clean architecture ব্যবহার করেন। তাই এই অধ্যায়ে নতুন করে কোনো ধারণা শিখতে হবে না। Presentation, domain, data — layer-গুলো একই থাকে। শুধু প্রতিটা layer যে জিনিস দিয়ে বানানো, সেগুলো আলাদা। Cubit-এর জায়গায় ViewModel, `get_it`-এর জায়গায় Hilt। একটাই নতুন জিনিস আছে: Android-এর ViewModel lifecycle জানে। মানে screen কখন চালু, কখন বন্ধ — সেটা সে বোঝে। Cubit এটা বুঝত না।

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

**UseCase নিয়ে একটা কথা:** Google-এর architecture guide বলে, domain layer **optional** — না রাখলেও চলে। কোনো UseCase যদি শুধু একটা repository method-কে ডেকে দেয়, আর কিছু না করে, তাহলে সেটা বাড়তি layer। UseCase বানান শুধু এই তিন ক্ষেত্রে:
- ভেতরে কোনো business rule আছে।
- দুইটা repository-র data একসাথে মেলাতে হয়।
- কয়েকটা ViewModel-এর একই logic লাগে।

এটা আপনার clean architecture-এর বিরুদ্ধে না। শুধু "প্রতিটা call-এর জন্য একটা UseCase" — এই নিয়মটা এখানে চলে না।

[উপরে ফিরুন](#toc)

### <a id="ch8-2"></a>৮.২ Cubit → ViewModel

**এক লাইনে:** ViewModel দেখতে Cubit-এর মতোই। তফাত দুইটা: screen ঘোরালে (rotation) ViewModel হারায় না, টিকে থাকে। আর সে নিজের coroutine scope সাথে নিয়ে আসে।

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
| `close()`-এ subscription cancel করতে হয় | লাগে না — `viewModelScope` নিজেই বন্ধ হয় |
| Widget dispose হলে Cubit-ও চলে যায় | Rotation-এ টিকে থাকে, screen সত্যিই বন্ধ হলে তবেই যায় |
| freezed state | `data class` |

**ViewModel দুইভাবে লেখা যায়:**
- **`combine` + `stateIn`** (উপরের উদাহরণের মতো): যখন state-এর বেশিরভাগটা অন্য flow থেকে আসে — যেমন database বা settings। এখানে আপনি শুধু বলে দেন state কী থেকে তৈরি হবে (declarative)। আর `WhileSubscribed` থাকায় app background-এ গেলে query নিজেই থেমে যায়।
- **`MutableStateFlow` + `update {}`**: যখন state মূলত user-এর কাজে বদলায় — যেমন form বা কয়েক ধাপের wizard। Cubit-এর `emit(copyWith)`-এর সবচেয়ে কাছের রূপ এটা:

```kotlin
private val _uiState = MutableStateFlow(EditNoteUiState())
val uiState: StateFlow<EditNoteUiState> = _uiState.asStateFlow()

fun onTitleChange(title: String) = _uiState.update { it.copy(title = title) }
```

**ফাঁদ:**
- ViewModel-এ `Context`, View বা Activity রাখবেন না। ViewModel Activity-র চেয়ে বেশিদিন বাঁচে। তাই Activity চলে গেলেও ViewModel তাকে ধরে রাখে, আর memory leak হয়। String resource লাগলে সেটা UI-তে বসে বের করুন (resolve করুন)।
- `MutableStateFlow`-কে বাইরে public রাখবেন না। রাখলে UI নিজেই state বদলে ফেলতে পারে। তখন UDF ভেঙে যায় — মানে state শুধু ViewModel থেকে নিচে নামবে, আর event শুধু UI থেকে ওপরে উঠবে, এই নিয়মটা আর থাকে না। Cubit-এ যেমন `emit` বাইরে থেকে call করা যায় না, এখানেও তেমন রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ch8-3"></a>৮.৩ `BlocBuilder` → `collectAsStateWithLifecycle`

**এক লাইনে:** Compose-এ ViewModel-এর `StateFlow` পড়া হয় `collectAsStateWithLifecycle()` দিয়ে। আর UI-কে দুই ভাগে লিখুন: Route আর Screen।

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

`NotesRoute` হলো Flutter-এর `NotesPage`-এর মতো — সে provider বসায়। `NotesScreen` হলো `NotesView`-এর মতো — সে শুধু দেখায়।

**কেন `WithLifecycle`:**
- সাধারণ `collectAsState()` app background-এ গেলেও collect করতেই থাকে।
- `collectAsStateWithLifecycle()` screen আর দেখা না গেলে (STARTED অবস্থার নিচে নামলে) collect থামিয়ে দেয়। Screen ফিরে এলে আবার শুরু করে।
- এর সাথে ViewModel-এ `stateIn(WhileSubscribed(5_000))` থাকলে আরও ভালো। তখন background-এ database query পর্যন্ত থেমে যায়।
- তুলনা করুন: Flutter-এ `BlocBuilder` app background-এ গেলেও stream শুনতে থাকে।

[উপরে ফিরুন](#toc)

### <a id="ch8-4"></a>৮.৪ `BlocListener` → one-off event

**এক লাইনে:** কিছু কাজ শুধু একবার ঘটে — যেমন snackbar দেখানো বা অন্য screen-এ যাওয়া। Google বলে, এগুলোকেও state হিসেবে রাখুন।

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

**কেন state, `SharedFlow` বা `Channel` না:** Event-কে stream-এ পাঠালে একটা সমস্যা আছে। ঠিক সেই মুহূর্তে কেউ না শুনলে event হারিয়ে যেতে পারে — যেমন তখন rotation চলছে, বা app background-এ। State এভাবে হারায় না। UI ফিরে এসে দেখে, error এখনো আছে। তখন সেটা দেখায়, তারপর clear করে দেয়। তবু অনেক team `Channel` ব্যবহার করে। Project-এ দুটোই দেখবেন। শুধু কোনটায় কী লাভ, কী ক্ষতি (trade-off) — সেটা জেনে রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ch8-5"></a>৮.৫ `get_it` → Hilt

**এক লাইনে:** Hilt একটা DI library। কোন class-এ কী dependency যাবে, সেই code সে compile-এর সময়েই বানিয়ে ফেলে। দেখতে `injectable`-এর annotation-এর মতো। কিন্তু কোনো dependency ভুল হলে app চালানোর আগেই, build-এর সময় ধরা পড়ে।

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
| `configureDependencies()` | `@HiltAndroidApp` (দরকারি code compile-এর সময় তৈরি হয়) |
| `getIt<NotesCubit>()` | `hiltViewModel()` |
| scope / environment | Component: `SingletonComponent`, `ViewModelComponent`, `ActivityComponent` |
| `@Environment('test')` | test-এ `@TestInstallIn` দিয়ে module বদলে দিন |

**`@Binds` বনাম `@Provides`:**
- Class-টা আপনার নিজের, তার constructor-এ `@Inject` আছে, আর তাকে একটা interface-এর সাথে জুড়তে হবে → `@Binds`।
- Class-টা কোনো library-র (Retrofit, OkHttp, Room), তাই তার constructor-এ আপনি হাত দিতে পারেন না → `@Provides`।

**Best approach:**
- প্রতিটা জিনিসের scope (কতদিন একই instance থাকবে) ভেবে ঠিক করুন। OkHttp, Retrofit, database, repository — এগুলো `@Singleton`। বাকিগুলো unscoped রাখুন, মানে প্রতিবার নতুন instance। সবকিছু singleton করলে memory বেশি লাগে, আর lock-এর খরচও বাড়ে।
- Interface বানান শুধু যখন সত্যিই লাগে — যেমন test-এ fake দিতে হবে, বা দুইটা আলাদা implementation আছে। নইলে `@Inject constructor` দেওয়া একটা class-ই যথেষ্ট। তখন `@Binds`-ও লাগে না।

> **মনে রাখুন**
> - Layer একই থাকে। Cubit → ViewModel, freezed state → data class, `get_it` → Hilt।
> - ViewModel rotation-এ টিকে থাকে, আর নিজের coroutine নিজেই বন্ধ করে।
> - `BlocBuilder` → `collectAsStateWithLifecycle()`। Route (যে ViewModel নেয়) আর Screen (যার নিজের state নেই) আলাদা রাখুন।
> - একবারের event-ও state হিসেবে রাখুন। দেখানো হয়ে গেলে clear করুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি UDF মানি। প্রতিটা screen-এর ViewModel একটা immutable UiState দেয়, StateFlow হিসেবে। UI সেটা lifecycle মেনে collect করে। আর user-এর event ViewModel-এ পাঠায় function call করে। DI-তে Hilt নিই। Flutter-এ injectable যা করত, Hilt তাই করে — কিন্তু ভুল থাকলে compile-এর সময়েই ধরা পড়ে। UseCase বানাই শুধু তখন, যখন সত্যিই business logic আছে।"
> - *English:* "I follow UDF: each screen's ViewModel exposes one immutable UiState as a StateFlow, the UI collects it in a lifecycle-aware way, and sends events as function calls. For DI I use Hilt — it does what injectable did in Flutter, but errors show up at compile time. I add a UseCase only when there is real business logic."

[উপরে ফিরুন](#toc)

---

## <a id="ch9"></a>৯. Data — network, JSON, database, storage

এই অধ্যায়ের প্রতিটা Android জিনিসের মতো একটা package Flutter-এও আছে। মজার কথা হলো, অনেক Flutter package আসলে এই Android library-গুলো দেখেই বানানো। Flutter-এর `retrofit` package-এর নামটাই তার প্রমাণ। তাই এই অধ্যায়টা আপনার সবচেয়ে তাড়াতাড়ি শেষ হবে।

### <a id="ch9-1"></a>৯.১ `dio` → Retrofit + OkHttp

**এক লাইনে:** Retrofit দিয়ে আপনি API-টা একটা interface হিসেবে লেখেন। OkHttp হলো তার নিচে বসা HTTP client। dio-র interceptor-এর কাজ এখানে OkHttp করে।

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
| `@RestApi` abstract class + generated `_NotesApi` | `interface` — app চলার সময় (runtime-এ) Retrofit নিজেই এর implementation বানায়, code generation লাগে না |
| `Future<List<NoteDto>>` | `suspend fun ...: List<NoteDto>` — নিজে থেকেই background-এ চলে |
| `InterceptorsWrapper` | OkHttp `Interceptor` |
| `onError`-এ 401 ধরে refresh | `Authenticator` — এটা শুধু 401 সামলানোর জন্যই বানানো |
| `DioException` | `IOException` (network), `HttpException` (4xx/5xx) |
| `LogInterceptor` | `HttpLoggingInterceptor` |

**Token refresh — `Authenticator`:**
- Server 401 দিলে OkHttp নিজেই `Authenticator`-কে ডাকে।
- সেখানে আপনি নতুন token আনেন, আর নতুন token দিয়ে একটা নতুন request ফেরত দেন। OkHttp সেই request আবার পাঠায়।
- ধরুন একসাথে পাঁচটা request 401 পেল। তখন পাঁচবার refresh হওয়া ঠিক না। তাই `synchronized` দিয়ে refresh একবারই করুন।
- Refresh করার আগে check করুন, অন্য কোনো request এর মধ্যেই token বদলে দিয়েছে কি না।

**Best approach:** Retrofit-এর exception repository-তেই ধরুন, আর নিজের বানানো error type-এ বদলে দিন। ViewModel যেন Retrofit বা `HttpException` চেনেই না। Flutter-এ যেমন `DioException`-কে repository-র বাইরে যেতে দিতেন না, ঠিক তেমন।

[উপরে ফিরুন](#toc)

### <a id="ch9-2"></a>৯.২ `json_serializable` → kotlinx.serialization

**এক লাইনে:** `@JsonSerializable` + `build_runner`-এর জায়গায় শুধু `@Serializable` লিখুন। Kotlin compiler-এর একটা plugin নিজেই দরকারি code বানিয়ে দেয়। আলাদা কোনো command চালাতে হয় না।

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
| `build_runner build` | লাগে না — compile-এর সময় নিজেই হয় |
| অজানা key — সাধারণত চুপচাপ বাদ পড়ে | default-এ **error** দেয় — তাই `ignoreUnknownKeys = true` দিন |

**ফাঁদ:**
- **`ignoreUnknownKeys = true` দিন।** না দিলে server JSON-এ একটা নতুন field যোগ করলেই পুরনো app crash করবে।
- **Gson এড়িয়ে চলুন।** পুরনো project-এ Gson দেখতে পাবেন। Gson object বানায় constructor call না করেই। ফলে দুইটা সমস্যা হয়: Kotlin-এর non-null field-এ null ঢুকে যায়, আর default value বসে না। তারপর app-এর অন্য কোথাও অদ্ভুত crash হয়। নতুন code-এ kotlinx.serialization বা Moshi ব্যবহার করুন।

[উপরে ফিরুন](#toc)

### <a id="ch9-3"></a>৯.৩ `drift` / `sqflite` → Room

**এক লাইনে:** Room হলো SQLite-এর ওপর বানানো Google-এর library। drift-এর সাথে এর মিল সবচেয়ে বেশি। এখানেও আছে table class, DAO, SQL যেটা compile-এর সময়েই check হয়, আর live query যেটা `Flow` দেয়।

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
| `Table` class | হাতে লেখা `CREATE TABLE` | `@Entity` data class |
| Database class-এর method | `db.query()` | `@Dao` interface |
| Dart DSL বা `.drift` file-এ SQL | raw SQL string | `@Query("SQL")` — compile-এর সময় check হয় |
| `.watch()` → `Stream` | (নেই) | `Flow` return type |
| `schemaVersion` + `MigrationStrategy` | `onUpgrade` | `version` + `Migration` / `@AutoMigration` |
| `build_runner` | — | KSP |

**ভেতরে কীভাবে কাজ করে — live query:** কোনো query `Flow` ফেরত দিলে Room মনে রাখে, query-টা কোন table পড়ে। পরে ওই table-এ insert, update বা delete হলে Room query-টা আবার চালায়। তারপর নতুন list emit করে। তাই Notes app-এ নতুন note save করলে list screen নিজে থেকেই update হয়। আপনাকে আলাদা করে কিছু করতে হয় না।

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

- Table-এর গঠন (schema) বদলালে `version` বাড়ান, আর একটা migration দিন। ছোট বদলে (যেমন নতুন column) `@AutoMigration` নিজেই কাজটা করে দেয়।
- Migration না দিয়ে শুধু version বাড়ালে app crash করে।
- **`fallbackToDestructiveMigration()` দিলে crash হয় না, কিন্তু user-এর সব local data মুছে যায়।** Notes app-এ এর মানে, user-এর সব note হারিয়ে যাবে। Production app-এ এটা প্রায় কখনোই দেবেন না।
- Room-এর `exportSchema` চালু রাখুন, আর schema file git-এ রাখুন। Migration test আর `@AutoMigration` এই file দেখেই কাজ করে।

**Best approach:** Database-কে **source of truth** বানান — মানে data-র আসল ঠিকানা হবে database। UI সবসময় Room-এর `Flow` দেখবে। Network শুধু Room-কে update করবে ([৯.৮](#ch9-8))।

[উপরে ফিরুন](#toc)

### <a id="ch9-4"></a>৯.৪ `shared_preferences` → DataStore

**এক লাইনে:** ছোট ছোট settings রাখার জায়গা। DataStore-এর সব কাজ async, আর সে value দেয় `Flow` হিসেবে।

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

**কী আলাদা:** Flutter-এর `getBool` value একবারই পড়ে। কিন্তু DataStore-এর `data` একটা `Flow`। Setting বদলালে যেখানে যেখানে এটা শোনা হচ্ছে, সব জায়গায় নতুন value নিজে থেকেই পৌঁছে যায়। তাই "sort by date" বদলালে list screen নিজেই আবার sort হয়। কাউকে আলাদা করে জানাতে হয় না।

**পুরনো `SharedPreferences` কেন না:** এর দুইটা সমস্যা ছিল। প্রথমবার পড়ার সময় এটা main thread-এ বসে disk পড়ত। আর `apply()` দিয়ে লেখা data, Activity বন্ধ হওয়ার সময় main thread আটকে দিতে পারত। Main thread বেশিক্ষণ আটকে থাকলে system "App isn't responding" দেখায় — একে ANR বলে। DataStore-এ এই সমস্যাগুলো নেই।

**Best approach:**
- ছোট key-value settings → DataStore Preferences।
- গোছানো (structured) বা বড় data → Room।
- DataStore-কে Hilt-এ singleton রাখুন। একই file-এর জন্য দুইটা DataStore instance বানালে exception আসে।

[উপরে ফিরুন](#toc)

### <a id="ch9-5"></a>৯.৫ `flutter_secure_storage` → Keystore

**এক লাইনে:** Token বা secret সাধারণ লেখা (plain text) হিসেবে রাখা যাবে না। Android Keystore-এ একটা key রাখুন। তারপর সেই key দিয়ে data encrypt করে রাখুন।

Flutter-এর `flutter_secure_storage` Android-এ ঠিক এটাই করে — ভেতরে Keystore ব্যবহার করে। এখন কাজটা আপনি নিজে করবেন:

- **Keystore** একটা key রাখে। এই key device থেকে বের করা যায় না। অনেক phone-এ key-টা একটা আলাদা secure hardware-এ থাকে। App key দিয়ে কাজ করাতে পারে, কিন্তু key-টা নিজে পড়তে পারে না।
- **Tink** হলো Google-এর crypto library। Tink দিয়ে সেই key ব্যবহার করে data encrypt করুন। তারপর encrypt করা data DataStore-এ রাখুন।
- পুরনো `EncryptedSharedPreferences` এখন **deprecated**। নতুন code-এ এটা ব্যবহার করবেন না।

**ফাঁদ:** Encrypt করা data device-এর backup-এ চলে যেতে পারে। কিন্তু key কখনো backup-এ যায় না। তাই নতুন phone-এ backup restore করলে data থাকবে, কিন্তু key থাকবে না — data আর decrypt করা যাবে না। এজন্য দুইটা কাজ করুন:
- Token-এর মতো জিনিস backup থেকে বাদ দিন (Manifest-এর backup rules দিয়ে)।
- Decrypt fail করলে app crash না করিয়ে user-কে আবার login করতে দিন।

[উপরে ফিরুন](#toc)

### <a id="ch9-6"></a>৯.৬ Image: `cached_network_image` → Coil

**এক লাইনে:** Network থেকে ছবি load করা, cache করা, আর মাপমতো ছোট করা — এই সব কাজ করে Coil-এর `AsyncImage`।

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

Coil ছবি cache করে দুই জায়গায় — memory-তে আর disk-এ। আর view যত বড়, ছবিটা ঠিক তত ছোট করে load করে। তাই 64dp-এর একটা thumbnail-এ 4000px-এর ছবি দেখালেও পুরো ছবির memory লাগে না। পুরনো project-এ Glide দেখতে পাবেন। Glide-ও একই কাজ করে।

[উপরে ফিরুন](#toc)

### <a id="ch9-7"></a>৯.৭ Pagination → Paging 3

**এক লাইনে:** লম্বা list একবারে না এনে পাতা পাতা করে load করা। Flutter-এ এই কাজ করত `infinite_scroll_pagination`-এর `PagingController`। Android-এ করে Paging 3 library।

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

- `PagingSource` হলো Flutter-এর সেই page request listener-এর মতো।
- `cachedIn(viewModelScope)` না দিলে screen ঘোরালেই (rotation) সব পাতা আবার load হয়।
- Offline-first app-এর জন্য আছে `RemoteMediator`। এটা network থেকে পাতা এনে Room-এ রাখে। আর UI পাতা পড়ে Room থেকে।

[উপরে ফিরুন](#toc)

### <a id="ch9-8"></a>৯.৮ সব একসাথে: offline-first repository

এবার পুরো অধ্যায়টা এক জায়গায় জুড়ে দেখি। নিচে Notes app-এর repository। Flutter-এ আর Android-এ এর নকশা একই:

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

**কেন এই নকশা:**
- Internet না থাকলেও app কাজ করে।
- Save করার সাথে সাথে user সেটা দেখতে পায়।
- Data দুই জায়গা থেকে আসে না, তাই কোনটা ঠিক — সেই ঝামেলা নেই। UI শুধু database চেনে।

Flutter-এ drift + dio দিয়ে আপনি হয়তো ঠিক এটাই বানিয়েছেন।

> **মনে রাখুন**
> - dio → Retrofit + OkHttp। Interceptor একই রকম। Token refresh করুন `Authenticator`-এ।
> - json_serializable → kotlinx.serialization, সাথে `ignoreUnknownKeys = true`। Gson না।
> - drift → Room। `Flow` query = `.watch()`। Destructive migration মানে user-এর data মুছে যাওয়া।
> - shared_preferences → DataStore। Secret → Keystore + Tink।
> - Database = source of truth।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমার data layer offline-first। Room হলো source of truth। UI তার Flow দেখে, আর network শুধু database update করে। Network-এর জন্য Retrofit আর OkHttp নিই। Token refresh করি `Authenticator` দিয়ে। JSON-এ kotlinx.serialization। Flutter-এ drift আর dio দিয়ে একই নকশা বানাতাম, তাই ধারণাটা আমার কাছে নতুন না।"
> - *English:* "My data layer is offline-first: Room is the source of truth, the UI observes its Flow, and the network only updates the database. I use Retrofit and OkHttp, with token refresh in an `Authenticator`, and kotlinx.serialization for JSON. I built the same design in Flutter with drift and dio, so the idea isn't new to me."

[উপরে ফিরুন](#toc)

---

## <a id="ch10"></a>১০. Plugin-এর পেছনের Android — background, notification, permission, intent

Flutter-এ এই অধ্যায়ের সবকিছু আপনি এক লাইনের plugin call দিয়ে সেরেছেন: `Workmanager().registerOneOffTask()`, `Permission.camera.request()`, `launchUrl()`। কখনো কখনো plugin ঠিকমতো কাজ করত না। কোনো Android version-এ notification আসত না, বা background task চলত না। এর কারণ সবসময় ছিল Android-এর কোনো নিয়ম, যেটা plugin-এর নিচে কাজ করে। এই অধ্যায়ে সেই নিয়মগুলো দেখব।

### <a id="ch10-1"></a>১০.১ `workmanager` → WorkManager

**এক লাইনে:** Flutter-এর `workmanager` plugin ভেতরে Android-এর WorkManager-কেই call করে। কিছু কাজ আছে যেটা app বন্ধ হলেও, phone restart হলেও শেষ হতেই হবে। সেই কাজের জন্য WorkManager।

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

**কী মিলল:** নাম, constraint, unique work — সব একই। কারণ plugin নিজে প্রায় কিছুই করে না, শুধু এই API-কে call করে। পার্থক্য একটাই। Flutter-এ background-এ Dart code চালাতে আলাদা একটা isolate চালু করতে হতো, তাই `callbackDispatcher` লাগত। Native-এ worker একটা সাধারণ Kotlin class।

**কোন কাজে কী:**

| কাজ | কী নেবেন |
|---|---|
| Screen খোলা থাকা পর্যন্ত | ViewModel-এ coroutine |
| App বন্ধ হলেও শেষ হতে হবে, একটু দেরি চলবে (sync, upload) | **WorkManager** |
| User এখনই দেখছে এমন লম্বা কাজ (music, recording, navigation) | Foreground Service ([১০.২](#ch10-2)) |
| ঠিক নির্দিষ্ট সময়ে (reminder) | `AlarmManager` — exact alarm-এ আলাদা permission |

**ফাঁদ — Flutter-এ আপনি যেগুলোর জন্য plugin-কে দোষ দিতেন:**
- **কাজটা ঠিক কখন চলবে, তা বলা যায় না।** Phone অনেকক্ষণ পড়ে থাকলে system battery বাঁচাতে Doze mode-এ যায়। Doze আর অন্য battery নিয়মের কারণে system কাজ পিছিয়ে দেয়। Periodic work অন্তত ১৫ মিনিট পরপর চলে, এর কম interval দেওয়া যায় না।
- একটা worker সাধারণত প্রায় ১০ মিনিট পর্যন্ত চলতে পারে। কাজ এর চেয়ে লম্বা হলে `setForeground()` দিয়ে একটা notification দেখাতে হয়।
- **User Settings থেকে app force stop করলে** WorkManager-এর কাজও বাতিল হয়ে যায়। User আবার app না খোলা পর্যন্ত কিছুই চলে না।
- কিছু phone কোম্পানি (বিশেষ করে কিছু চীনা brand) নিজেরাই আরও কড়া battery নিয়ম বসায়। এটা Android-এর নিয়মের বাইরের সমস্যা। Plugin-এর দোষ না।
- Hilt-এর dependency worker-এ দিতে `@HiltWorker` আর `@AssistedInject` লাগে।

[উপরে ফিরুন](#toc)

### <a id="ch10-2"></a>১০.২ Service

**এক লাইনে:** Service হলো এমন কাজ, যেটা কোনো UI ছাড়া চলে। এখন প্রায় সবসময় এটা হয় **foreground service** — মানে একটা notification দেখিয়ে, user-কে জানিয়ে চলে।

আগে (আপনার Java-র সময়ে) background service যখন খুশি চালানো যেত। এখন নিয়ম অনেক কড়া:

- Android 8 থেকে background-এ service চালানো প্রায় বন্ধ।
- Android 14 থেকে প্রতিটা foreground service-এর একটা **type** ঘোষণা করতে হয় (`dataSync`, `mediaPlayback`, `location`, `microphone`...), আর type অনুযায়ী আলাদা permission।
- Background থেকে foreground service চালু করা অনেক ক্ষেত্রে নিষেধ।

**Best approach:** আগে দেখুন কাজটা WorkManager দিয়ে হয় কি না। Foreground service নিন শুধু তখন, যখন user ঠিক এখনই কাজটা দেখছে বা শুনছে। যেমন Notes app-এ voice note record হওয়ার সময়।

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

- **Channel:** User প্রতিটা channel আলাদা করে বন্ধ করতে পারে। একবার channel তৈরি হয়ে গেলে code দিয়ে তার importance আর বাড়ানো যায় না (user নিজে না বদলালে শুধু কমানো যায়)। আসল নিয়ন্ত্রণ তখন user-এর, Settings থেকে। তাই প্রথমবারেই importance ঠিক করে দিন।
- **Android 13+-এ notification দেখাতে runtime permission লাগে** (`POST_NOTIFICATIONS`)। Permission না চাইলে কোনো notification দেখাবে না। Flutter-এ "notification আসে না" bug-এর একটা বড় কারণ ছিল এটা।
- **`PendingIntent`** দিয়ে আপনি system-কে অনুমতি দেন, যাতে পরে system আপনার app-এর হয়ে এই intent চালাতে পারে। সবসময় `FLAG_IMMUTABLE` দিন, যদি না সত্যিই mutable লাগে। প্রতিটা note-এর জন্য আলাদা request code দিন (`note.id.hashCode()`)। নইলে একটা PendingIntent আরেকটাকে overwrite করে দেয়।
- **FCM:** FCM-এ দুই রকম message আছে।
  - "notification" message: app background-এ থাকলে system নিজেই এটা দেখায়। তখন আপনার `onMessageReceived` call হয় না।
  - "data" message: এটা সবসময় আপনার code-এ আসে।
  - `firebase_messaging`-এ আপনি যে পার্থক্য দেখেছেন, সেটা এখান থেকেই আসে।

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
- Flutter-এ `await` করে ফল পেতেন। এখানে ফল আসে একটা callback-এ। কারণ permission dialog খোলা থাকার সময় আপনার Activity destroy হয়ে আবার নতুন করে তৈরি হতে পারে। তখনও যেন ফল ঠিক জায়গায় আসে, launcher সেটা নিজেই সামলায়।
- **"Permanently denied" জানার জন্য সরাসরি কোনো API নেই।**
  - User দুইবার "না" বললে system আর dialog দেখায় না।
  - `shouldShowRequestPermissionRationale()` বলে দেয়, এখন user-কে কারণ বোঝানো উচিত কি না।
  - `permission_handler` এসব মিলিয়ে আন্দাজ করত, `isPermanentlyDenied` কি না।
  - Native-এ এটা আপনি নিজে করবেন। User "না" বলার পরে rationale যদি `false` হয়, তাহলে user-কে Settings-এ যাওয়ার একটা পথ দিন।
- Permission দুই জায়গায় লাগে। এক, Manifest-এ `<uses-permission>` লেখা। দুই, "dangerous" permission (camera, location, notification) app চলার সময় (runtime-এ) user-এর কাছে চাওয়া।

**Best approach — আগে দেখুন permission লাগেই কি না:**
- ছবি বাছাই → **Photo Picker** (`PickVisualMedia`)। কোনো storage permission লাগে না।
- File বাছাই → `OpenDocument`। Permission লাগে না।
- শুধু একটা ছবি তোলা → `TakePicture` contract দিয়ে camera app-কে ছবি তুলতে বলুন। Manifest-এ CAMERA declare না করলে কোনো permission লাগে না। কিন্তু declare করলে তখন permission লাগে।

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
- **Implicit intent:** নির্দিষ্ট class না বলে শুধু কাজটা বলে — "এই কাজটা যে পারে, সে করুক"। যেমন browser, share, dialer। কোন app খুলবে, সেটা system বা user ঠিক করে।
- **ফাঁদ:** Android 11+-এ অন্য কোনো app install করা আছে কি না জানতে চাইলে Manifest-এ `<queries>` লাগে। না দিলে আপনার app অন্য app-এর খবর পায় না। `url_launcher`-এর `canLaunchUrl` false দেওয়ার একটা পরিচিত কারণ এটা।
- **Deep link / App Links:** বাইরের কোনো link থেকে app-এর নির্দিষ্ট screen খোলা। এর জন্য Manifest-এ `intent-filter` আর Navigation-এ `deepLinks` লাগে। `https` link যদি browser-এ না গিয়ে সরাসরি app-এ খুলতে চান, তাহলে website-এ একটা `assetlinks.json` file রাখতে হয়। সেই file-এ Play-এর app signing key-র SHA-256 দিতে হয়।

> **মনে রাখুন**
> - Flutter-এর background, notification, permission, url plugin — সবাই ভেতরে এই Android API-গুলোই call করে।
> - Background কাজ → WorkManager। কাজ চলবে, কিন্তু ঠিক কখন চলবে, তা বলা যায় না।
> - Notification: channel, Android 13+ permission, `FLAG_IMMUTABLE`।
> - Permission: Activity Result API। আগে দেখুন permission ছাড়া উপায় আছে কি না (Photo Picker)।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter-এ background কাজ আর notification plugin দিয়ে করতাম। কিন্তু কিছু ভাঙলে কারণ সবসময় ছিল plugin-এর নিচের কোনো Android নিয়ম — Doze, notification permission, বা foreground service type। Native-এ যে কাজ একটু পরে হলেও চলে (deferrable), তাতে WorkManager নিই। Permission-এ Activity Result API নিই। আর যেখানে পারি, permission ছাড়া উপায় বেছে নিই, যেমন Photo Picker।"
> - *English:* "In Flutter I used plugins for background work and notifications, but whenever something broke, the cause was always an Android rule underneath — Doze, the notification permission, foreground service types. In native, I use WorkManager for deferrable work, the Activity Result API for permissions, and pick permission-free options like the Photo Picker when I can."

[উপরে ফিরুন](#toc)

---
## <a id="ch11"></a>১১. Testing

Test কীভাবে লিখতে হয়, সেটা আপনি আগে থেকেই জানেন: fake বেশি, mock কম, আর code কী করে (behaviour) সেটা test করুন। Android-এও নিয়ম একই। শুধু tool-গুলোর নাম আলাদা।

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

- **`runTest`** হলো Flutter-এর `fake_async`-এর মতো। এখানে সময় নকল (virtual)। তাই `delay(5_000)` লিখলেও test অপেক্ষা করে না, সাথে সাথে শেষ হয়।
- **`MainDispatcherRule`** একটা ছোট JUnit rule। এটা `Dispatchers.Main`-এর জায়গায় একটা test dispatcher বসিয়ে দেয়। কারণ JVM-এ চলা test-এ আসল main thread থাকে না। এই rule না দিলে `viewModelScope` crash করে। এর code Android-এর official testing guide-এ আছে — সেখান থেকে copy করে নিন।
- **Turbine** কাজ করে `bloc_test`-এর `expect` list-এর মতো। পার্থক্য হলো, এখানে state একটা একটা করে নেন: `awaitItem()` দিয়ে।
- **ফাঁদ:** কোনো flow যদি `stateIn(WhileSubscribed)` দিয়ে বানানো হয়, তাহলে কেউ subscribe না করলে সেটা চালুই হয় না। তখন সরাসরি `.value` পড়লে আপনি শুধু শুরুর (initial) value পাবেন। তাই Turbine দিয়ে collect করে পড়ুন।
- Kotlin-এ test-এর নাম backtick-এর ভেতরে পুরো বাক্যের মতো লেখা যায়।

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

Compose test screen-এর জিনিস খোঁজে **semantics tree** দিয়ে। এই tree-তে প্রতিটা node-এর পরিচয় থাকে: তার text, content description, বা `Modifier.testTag("id")`। TalkBack (screen reader) ঠিক এই tree-টাই পড়ে। তাই app-এ accessibility ভালো দিলে test লেখাও সহজ হয়ে যায়। আর **Robolectric** ব্যবহার করলে এই UI test-ও device ছাড়া, JVM-এ, দ্রুত চলে।

> **মনে রাখুন**
> - `bloc_test`-এর জায়গায় `runTest` + Turbine। সাথে `MainDispatcherRule` লাগবেই।
> - `testWidgets`-এর জায়গায় `createComposeRule()`। Node খুঁজবেন semantics দিয়ে।
> - আগে fake, দরকার হলে তবেই mock — Flutter-এর মতোই।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "ViewModel test করি `runTest` আর Turbine দিয়ে। সাথে একটা rule দিই, যেটা main dispatcher বদলে দেয়। আসল repository-র বদলে একটা fake দিই। আমার Compose screen-গুলো stateless, তাই UI test সহজ। Semantics দিয়ে node খুঁজি, আর Robolectric দিয়ে JVM-এ চালাই।"
> - *English:* "I test ViewModels with `runTest` and Turbine, with a rule that replaces the main dispatcher, and a fake instead of the real repository. Because my Compose screens are stateless, UI tests are easy — I find nodes by semantics and run them on the JVM with Robolectric."

[উপরে ফিরুন](#toc)

---

## <a id="ch12"></a>১২. Flavor, R8, release

এই অধ্যায়টা আপনার চেনা জায়গা। Flutter-এ flavor বানাতে আপনি `android/app/build.gradle`-এ কিছু লাইন লিখেছিলেন। Native Android-এর flavor ঠিক ওই জিনিসটাই।

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

প্রতিটা flavor-এর সাথে প্রতিটা build type জোড়া লাগে। এই জোড়াকে বলে **build variant**। এখানে চারটা: `devDebug`, `devRelease`, `prodDebug`, `prodRelease`।

**R8 — release-এ crash-এর এক নম্বর কারণ।** R8 release build-এ দুইটা কাজ করে:

1. যে class আর method কোথাও ব্যবহার হয় না, সেগুলো মুছে দেয়।
2. বাকিগুলোর নাম ছোট করে দেয় (`a`, `b`)।

সমস্যা হলো reflection। কোনো library যদি চলার সময় নাম ধরে class খোঁজে (reflection), R8 সেটা আগে থেকে দেখতে পায় না। ফলে R8 ওই class মুছে দেয় বা তার নাম বদলে দেয়। তাই debug-এ সব ঠিক চলে, কিন্তু release-এ crash করে।

সমাধান হলো `proguard-rules.pro`-তে একটা `-keep` rule লেখা। এই rule R8-কে বলে "এই class-টা রেখে দাও"। kotlinx.serialization, Retrofit, Room-এর মতো ভালো library নিজের rule নিজেই সাথে দিয়ে দেয়।

Flutter app-এও plugin-এর Java/Kotlin code R8-এর ভেতর দিয়ে যায়। তাই Flutter-এ কখনো শুধু release-এ crash দেখে থাকলে, কারণ সম্ভবত এটাই ছিল।

**Best approach:** প্রতিটা release-এর আগে release build phone-এ install করে চালিয়ে দেখুন। আর Play Console-এ `mapping.txt` upload করুন। এই file-এ লেখা থাকে কোন ছোট নাম আসলে কোন class। এটা না দিলে crash report-এর stack trace পড়া যাবে না।

**Signing আর Play:** এটা আপনি জানেন। Play App Signing-এ আসল key থাকে Google-এর কাছে। আপনি sign করেন upload key দিয়ে।

- App Links-এর `assetlinks.json`-এ app signing key-র SHA-256 দিন। Upload key-র SHA-256 না।
- Play ঠিক করে দেয়, `targetSdk` কমপক্ষে কত হতে হবে। এই সংখ্যাটা প্রতি বছর বাড়ে। আপনার app-এর targetSdk বাড়ানোর আগে সেই Android version-এ কী কী behavior বদলেছে, সেটা পড়ে নিন।

> **মনে রাখুন**
> - Flutter-এর flavor আর Android-এর `productFlavors` একই জিনিস, একই file-এ।
> - `--dart-define`-এর জায়গায় Android-এ `buildConfigField`।
> - শুধু release-এ crash হলে প্রথম সন্দেহ R8। Release build চালিয়ে দেখুন, আর `mapping.txt` upload করুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter-এ flavor বানাতে গিয়ে আমি আগেই Android-এর productFlavors লিখেছি। তাই build variant আমার চেনা। Release-এ R8 চালু রাখি। প্রতিবার release build চালিয়ে test করি। আর mapping file upload করি, যাতে crash report পড়া যায়।"
> - *English:* "I already wrote Android productFlavors to set up flavors in Flutter, so build variants are familiar to me. In release I keep R8 on, test the release build every time, and upload the mapping file so crashes are readable."

[উপরে ফিরুন](#toc)

---

## <a id="ch13"></a>১৩. ইঞ্জিনের ভেতরে — tap থেকে pixel, code থেকে APK

এতক্ষণ আমরা দেখলাম কোন API দিয়ে কী লিখতে হয়। এবার দেখব, সেই code phone-এর ভেতরে আসলে কীভাবে চলে।

Senior interview-এ এই তিনটা প্রশ্ন প্রায়ই আসে। আর এগুলোর উত্তরেই senior আর junior আলাদা হয়ে যায়:

1. App খুললে ভেতরে কী কী হয়?
2. একটা লেখা screen-এ আসে কীভাবে?
3. Build চাপলে কী হয়?

এই অধ্যায়ে নতুন কোনো library নেই। আছে শুধু app চলার সময় ভেতরে কোন অংশ কী কাজ করে, সেটা। প্রতিটা অংশে Flutter আর native Android পাশাপাশি দেখাব। ধীরে পড়ুন, ধাপে ধাপে। এই অধ্যায় বুঝলে [অধ্যায় ০](#ch0)-এর বড় ছবিটা একদম পরিষ্কার হয়ে যাবে।

### <a id="ch13-1"></a>১৩.১ "UI toolkit" আর "Everything is a widget" — কেন বলা হয়

**এক লাইনে:** Flutter শুধু UI বানানোর জিনিসপত্র দেয় — widget, layout, আঁকা, gesture, animation, text। OS-এর বাকি সব কাজ করে দেয় যে platform-এর ওপর Flutter চলছে (host platform — এখানে Android)। তাই Flutter একটা UI toolkit — শুধু UI বানানোর library আর engine। এটা পুরো OS framework না।

**কে কী দেয়:**

| কাজ | কে করে |
|---|---|
| Widget, layout, আঁকা, gesture, animation | Flutter |
| Text layout, image decode | Flutter engine |
| File আর network socket (`dart:io`) | Dart runtime সরাসরি OS-কে ডাকে — তাই `http` বা `dio`-তে plugin লাগে না |
| Process চালু করা আর মারা | Android (system_server, Zygote) |
| Lifecycle | Android। Flutter শুধু শোনে (`AppLifecycleState`) |
| Permission, notification, background কাজ, camera | Android। Flutter-এ plugin দিয়ে |
| Window, keyboard (IME), accessibility (TalkBack) | Android। Flutter শুধু এদের সাথে তথ্য আদান-প্রদান করে |

**Flutter-এর নিজের তিনটা স্তর (layer):** ওপরের স্তরে আপনার code। মাঝে C++-এ লেখা engine। নিচে embedder — যে অংশটা OS-এর সাথে কথা বলে।

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

শুধু নিচের embedder-টা বদলে দিলেই একই toolkit iOS আর desktop-এ চলে। (Web-এ একটু আলাদা: সেখানে C++ engine-এর বদলে browser-এর জন্য আলাদা করে লেখা একটা engine চলে।) এজন্যই Flutter এক platform থেকে আরেক platform-এ সহজে যায় (portable)।

Android ঠিক উল্টো। Android নিজেই একটা পুরো OS। তার ওপরে framework আছে, আর সেই framework-এর ভেতরে Android-এর নিজের UI system আছে।

**"Everything is a widget" মানে কী।** আগে পুরনো Android View কীভাবে কাজ করত, সেটা দেখি:

- Padding, click, background, alpha — সবই একটা View-এর property।
- তাই `View` class নিজেই হাজার হাজার লাইনের বিশাল একটা class।
- নতুন ক্ষমতা আসে inheritance থেকে: `TextView` → `Button` → `CompoundButton` → `CheckBox`।

Flutter-এ উল্টো। প্রতিটা কাজের জন্য একটা আলাদা ছোট widget। Padding-এর জন্য একটা, click-এর জন্য একটা, রঙের জন্য একটা। একটার ভেতরে আরেকটা বসিয়ে বড় জিনিস বানান — একে বলে composition।

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

**কেন এই design:**

- শিখতে হয় একটাই ধারণা — সবকিছু widget।
- যেকোনো একটা টুকরো খুলে অন্যটা বসানো যায়।
- Widget ছোট ছোট হলে rebuild করা সস্তা থাকে।

এর দাম হলো, nesting অনেক গভীর হয়ে যায়। Compose এখানে মাঝামাঝি পথ নিয়েছে। UI-টা composable দিয়ে বানানো। কিন্তু padding, click, background-এর মতো সাজসজ্জা যায় Modifier-এ।

**Senior-এর সূক্ষ্ম কথা:** "Everything is a widget" কথাটা ১০০% সত্য না। Widget আসলে শুধু একটা config — কী দেখাতে হবে তার বর্ণনা। `State`, `Element`, `RenderObject`, `AnimationController`, `ThemeData` — এগুলো widget না। ঠিকভাবে বললে: "UI-র প্রতিটা অংশ widget দিয়ে বর্ণনা করা হয়।"

**ফাঁদ:** অনেকে বলে "Flutter native widget-কে wrap করে"। এটা ভুল। Flutter Android-এর button ব্যবহার করে না। প্রতিটা pixel Flutter নিজে আঁকে। Android জানেই না যে screen-এ একটা button আছে।

[উপরে ফিরুন](#toc)

### <a id="ch13-2"></a>১৩.২ তিনটা runtime: JVM, ART আর Dart

**এক লাইনে:** আপনার computer-এ build চালায় **JVM**। Phone-এ Kotlin আর Java code চালায় **ART**। আর Dart code চালায় **Dart runtime**। Debug-এ এটা JIT-সহ পুরো একটা VM। Release-এ এটা শুধু আগে থেকে compile করা machine code চালায়।

**আগে চারটা শব্দ পরিষ্কার করি:**

- **Runtime** — যে program আপনার code-কে চালায়। Code নিজে চলে না, কেউ একজন চালায়।
- **VM (virtual machine)** — এক ধরনের runtime। এটা এমন code পড়ে চালায়, যেটা CPU সরাসরি বোঝে না (যেমন bytecode)।
- **JIT (just-in-time)** — app চলার সময়ই code-কে machine code-এ বদলানো। সুবিধা: code বদলে সাথে সাথে চালানো যায় (hot reload)।
- **AOT (ahead-of-time)** — app চালানোর আগেই, build-এর সময় code-কে machine code-এ বদলে রাখা। সুবিধা: app খুললেই দ্রুত চলে।

| কোথায় | Runtime | কী চালায় |
|---|---|---|
| আপনার computer | JVM (JDK-র ভেতরে) | Gradle, Android Gradle Plugin, Kotlin compiler, R8, Android Studio নিজে |
| আপনার computer | Dart VM | `flutter` tool নিজে (এটা Dart-এ লেখা), analyzer, `build_runner`, `flutter test` |
| Phone | ART | Activity, plugin-এর Kotlin/Java, Jetpack, Compose — সব `.dex` |
| Phone, debug build | Dart VM, JIT সহ | আপনার Dart code। Hot reload এজন্যই সম্ভব। |
| Phone, release build | Dart runtime, JIT ছাড়া | `libapp.so`-এর machine code |

**"Java runtime" বললে দুইটা আলাদা জিনিস গুলিয়ে যায়:**

- **JVM** চলে আপনার computer-এ। এটা Java bytecode (`.class` file) চালায়।
  - Gradle নিজে JVM-এর ওপর চলে। তাই Flutter project-ও JDK ছাড়া Android build করতে পারে না।
  - নতুন Android Gradle Plugin-এর জন্য JDK 17 বা তার নতুন version লাগে।
  - Flutter নিজে থেকে Android Studio-র সাথে আসা JDK (JBR) ব্যবহার করে। কোন JDK নিচ্ছে, সেটা `flutter doctor -v` চালালে দেখবেন। বদলাতে চাইলে `flutter config --jdk-dir <path>`।
- **ART** চলে phone-এ। এটা Java bytecode চালায় না। এটা চালায় `.dex` — Android-এর নিজের bytecode format। **Android phone-এ কোনো JVM নেই।**

**Kotlin code-এর যাত্রা:** আপনার .kt file কীভাবে phone-এ চলা পর্যন্ত যায়, নিচের ছবিতে দেখুন। প্রথমে kotlinc (Kotlin compiler) এটাকে .class বানায়। তারপর D8 বা R8 সেটাকে dex বানায়। শেষে phone-এ ART সেটা চালায়।

```
.kt ──kotlinc──► .class (JVM bytecode) ──D8 / R8──► classes.dex ──phone-এ──► ART
                                                                ├ interpreter: প্রথমে
                                                                ├ JIT: বেশি চলা method চলার সময় compile
                                                                └ AOT (dex2oat): profile দেখে, phone idle থাকলে
```

ART একটা method-কে তিনভাবে চালাতে পারে, ছবির ডান দিকে যেমন দেখানো:

1. **Interpreter** — শুরুতে code লাইন ধরে ধরে পড়ে চালায়। এটা সবচেয়ে ধীর।
2. **JIT** — যে method বারবার চলে, app চলার সময়ই সেটাকে machine code বানিয়ে নেয়।
3. **AOT (dex2oat)** — phone যখন অলস থাকে (যেমন রাতে charge-এ), তখন ART দেখে কোন code বেশি চলে (profile)। সেগুলো আগে থেকেই machine code বানিয়ে রাখে।

Baseline Profile হলো আপনার দেওয়া একটা তালিকা: "এই code-গুলো গুরুত্বপূর্ণ"। এটা দিলে ওই code app install-এর সময়ই AOT হয়ে যায়। তাই app প্রথমবার খোলার সময় থেকেই দ্রুত চলে।

**Dart code-এর যাত্রা:** Dart-এ debug আর release-এর পথ আলাদা। দুই পথেই প্রথম ধাপ একই: frontend_server আপনার .dart file-কে kernel-এ বদলায়। Kernel (.dill file) হলো Dart code-এর একটা মাঝামাঝি রূপ — machine code না, কিন্তু আর source code-ও না।

```
debug:   .dart ──frontend_server──► kernel (.dill) ──phone-এ──► Dart VM, JIT     ← hot reload
release: .dart ──frontend_server──► kernel ──gen_snapshot──► libapp.so (ARM machine code)
```

- **Debug:** phone-এ kernel যায়। Dart VM সেটা JIT দিয়ে চালায়। তাই code বদলালে নতুন kernel পাঠিয়ে দিলেই চলে — এটাই hot reload।
- **Release:** gen_snapshot kernel-কে আগেই ARM machine code বানিয়ে libapp.so file-এ রাখে (AOT)। Phone-এ শুধু এই তৈরি machine code চলে।

**মজার কথা: একটা Flutter app-এ দুইটা runtime পাশাপাশি চলে।** একই process-এর ভেতরে ART আর Dart runtime দুইটাই থাকে। কিন্তু তারা একে অপরের জিনিস দেখতে পায় না:

- দুইজনের heap (object রাখার memory) আলাদা।
- দুইজনের garbage collector-ও আলাদা।
- Dart-এর object ART দেখে না। ART-এর object-ও Dart দেখে না।

তাহলে তারা কথা বলে কীভাবে? Message পাঠিয়ে (platform channel), অথবা FFI/JNI দিয়ে।

এর দুইটা ফল আছে:

1. Channel দিয়ে বড় image পাঠানো দামি। কারণ data-টা serialize করে (bytes-এ বদলে) অন্য পাশে copy করতে হয়।
2. Android Studio-র Memory Profiler-এ Dart-এর heap Java heap হিসেবে দেখায় না। Dart-এর memory দেখতে DevTools-এর Memory tab লাগে।

**ফাঁদ:** "Dart code ART-এ চলে" — ভুল। "Android-এ JVM আছে" — এটাও ভুল।

[উপরে ফিরুন](#toc)

### <a id="ch13-3"></a>১৩.৩ App খুললে কী হয় — tap থেকে প্রথম frame

**এক লাইনে:** আপনি icon-এ tap করলে চারটা জিনিস পরপর ঘটে:

1. Launcher system-কে বলে "এই app খোলো"।
2. System, Zygote থেকে একটা নতুন process বানায় (fork করে)।
3. সেই process-এ Application আর Activity তৈরি হয়।
4. প্রথম frame আঁকা হলে splash সরে যায়।

Flutter app-এ ধাপ ৩ আর ৪-এর মাঝে একটা বাড়তি ধাপ আছে: engine চালু করা, তারপর Dart-এর `main()` চালানো।

**সব app-এর জন্য একই পথ (ধাপে ধাপে):**

1. **Tap।** Launcher (home screen) নিজেও একটা সাধারণ app। আপনি tap করলে সে `startActivity(intent)` ডাকে। Intent-এ লেখা থাকে: "এই package-এর LAUNCHER activity-টা খোলো"।
2. **Binder।** এই call যায় `system_server` নামের process-এ, ActivityTaskManager-এর কাছে। Android-এ প্রতিটা app আলাদা process-এ চলে। এক process আরেক process-এর সাথে কথা বলে Binder দিয়ে।
3. **আগে splash।** App-এর process তৈরি হতে একটু সময় লাগে। তাই system অপেক্ষা করে না। সে Activity-র theme দেখে আগেই একটা starting window (splash) দেখিয়ে দেয়, যাতে tap করার সাথে সাথে user কিছু দেখে। Flutter-এ এটাই আপনার `android/app/src/main/res/values/styles.xml` file-এর `LaunchTheme`।
4. **Zygote fork।** App-এর process এখনো নেই। তাই system Zygote-কে বলে একটা copy বানাতে (fork)।
   - Zygote একটা বিশেষ process। Phone চালু হওয়ার সময়ই এটা তৈরি হয়।
   - ART আর হাজার হাজার framework class সে আগে থেকেই load করে বসে আছে।
   - Fork মানে এই process-এর একটা copy বানানো। Memory সাথে সাথে copy হয় না। দুইজন একই memory ভাগ করে। কেউ কিছু বদলালে তখন শুধু সেই অংশ copy হয় — একে বলে copy-on-write।
   - ফলে নতুন app একটা তৈরি runtime খুব দ্রুত পেয়ে যায়।
5. **`ActivityThread.main()`।** এটাই নতুন process-এর আসল `main()`। এটা main thread-এ একটা Looper চালু করে। Looper হলো একটা message queue — Dart-এর event loop-এর মতো। Main thread সারাজীবন এই queue থেকে একটা একটা কাজ নিয়ে করে। তারপর process system-কে জানায়: "আমি তৈরি"।
6. **Application।** এখানে তিনটা জিনিস এই ক্রমে চলে: `Application.attachBaseContext` → সব `ContentProvider.onCreate` → `Application.onCreate`। Firebase-এর মতো SDK এই ContentProvider ধাপে চুপচাপ নিজেকে চালু (init) করে নেয়।
7. **Activity।** `MainActivity` তৈরি হয়। তারপর চলে `onCreate` → `onStart` → `onResume`। একটা window তৈরি হয়, আর সেটা WindowManager-এ যোগ হয়।
8. **প্রথম frame।** Screen নিয়মিত একটা সংকেত দেয়, "নতুন frame দাও" — একে বলে vsync। পরের vsync-এ measure → layout → draw হয়। RenderThread GPU দিয়ে ছবিটা আঁকে। SurfaceFlinger সেটা screen-এ বসায়। এরপর splash সরে যায়।

**ধাপ ৭-এ এসে Compose আর Flutter-এর পথ আলাদা হয়ে যায়:**

- **Native (Compose):** `onCreate`-এর ভেতরে `setContent { }` চলে। Compose UI tree তৈরি হয়। তারপর প্রথম frame আঁকা হয়।
- **Flutter:** `MainActivity : FlutterActivity`-এর `onCreate`-এর ভেতরে এই সাতটা কাজ হয়:
  1. একটা `FlutterEngine` তৈরি হয় (অথবা আগে বানিয়ে রাখা cache থেকে নেওয়া হয়)। এখানে `libflutter.so` load হয়। এটাই C++-এ লেখা Flutter engine।
  2. Engine নিজের কয়েকটা thread বানায়:
     - **platform thread** — এটা আসলে Android-এর main thread। Flutter 3.29 থেকে আপনার Dart code-ও এই thread-এই চলে।
     - **raster thread** — GPU-র কাজ করে।
     - **I/O thread** — image decode-এর মতো ভারী কাজ করে।
  3. Engine `libapp.so` খুঁজে নেয়। এটাই আপনার compile করা Dart code।
  4. `configureFlutterEngine`-এর ভেতরে `GeneratedPluginRegistrant` সব plugin register করে। Plugin-এর Kotlin অংশ এখানেই তৈরি হয়।
  5. একটা `FlutterView` তৈরি হয়। এর ভেতরে একটা `SurfaceView` থাকে। এটা Android-এর কাছ থেকে নেওয়া একটা খালি আঁকার জায়গা (surface)। Android এখানে কিছু আঁকে না। Engine এখানে নিজে আঁকবে।
  6. Dart-এর শুরুর বিন্দু (entrypoint) চলে: আপনার `main()` → `runApp()` → widget tree।
  7. Engine প্রথম frame আঁকে। যতক্ষণ এই frame তৈরি না হয়, ততক্ষণ Flutter Android-কে আঁকতে দেয় না। তাই splash screen-এ থেকে যায়। Frame আঁকা হলেই splash সরে যায়।

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

**Cold, warm, hot start — তিন রকম চালু হওয়া:**
- **Cold:** app-এর process নেই। ওপরের পুরো পথ চলে।
- **Warm:** process আছে, কিন্তু Activity নেই। তাই ধাপ ৪–৬ বাদ যায়।
- **Hot:** Activity-ও আছে। শুধু সেটাকে সামনে আনা হয়।

Flutter-এর cold start native-এর চেয়ে একটু ভারী। কারণ বাড়তি তিনটা কাজ হয়: engine load হয়, Dart চালু হয়, আর প্রথম frame-এর আগে `main()`-এর ভেতরে `runApp`-এর আগের সব `await` শেষ হতে হয়।

**ফাঁদ:** অনেকে `main()`-এ `runApp`-এর আগেই Firebase, database, remote config — সব `await` করে। তাতে splash অনেকক্ষণ আটকে থাকে। Native-এ একই ভুল হয় `Application.onCreate`-এ। দুই জায়গাতেই নিয়ম একই: প্রথম frame-এর আগে শুধু সেটুকু করুন, যেটা ছাড়া একদমই চলে না। বাকিটা পরে করুন।

[উপরে ফিরুন](#toc)

### <a id="ch13-4"></a>১৩.৪ একটা লেখা screen-এ আসা: `Text('আজকের নোট')`

**এক লাইনে:** Flutter আর Compose — দুই দিকেই একই চারটা ধাপ:

1. **বর্ণনা** — কী দেখাতে হবে।
2. **মাপ** — লেখাটা কত বড়, কোথায় বসবে।
3. **আঁকার নির্দেশ** — কী কোথায় আঁকতে হবে, তার একটা তালিকা।
4. **GPU** — সেই তালিকা ধরে আসল pixel আঁকা।

পার্থক্য শুধু কে আঁকে। Flutter-এ আঁকে Flutter-এর নিজের engine। Native-এ আঁকে Android-এর নিজের renderer।

**Flutter-এ:**

```dart
const Text('আজকের নোট')
```

1. **Widget।** `Text` একটা `StatelessWidget`। তার `build()` ফেরত দেয় `RichText`।
2. **Element আর RenderObject।** `RichText`-এর জন্য একটা element তৈরি হয়, আর সে একটা `RenderParagraph` বানায়। `Text` নিজে কিছু আঁকে না, আঁকে `RenderParagraph`।
3. **Layout।** Parent একটা সীমা (constraint) দেয়, যেমন "সবচেয়ে বেশি ৩৬০ চওড়া হতে পারবে"। `RenderParagraph` তখন engine-কে বলে লেখাটা মাপতে। Engine এই কাজগুলো করে:
   - ঠিক font খুঁজে বের করে।
   - HarfBuzz দিয়ে **shaping** করে। Shaping মানে কোন অক্ষরের পাশে কোনটা বসবে, আর মিলে কী আকার নেবে, তা ঠিক করা। বাংলার জন্য এটা খুব জরুরি: "ন" আর "ো" মিলে "নো" হয়। যুক্তাক্ষরও এই ধাপেই তৈরি হয়।
   - লেখা লম্বা হলে লাইন ভাঙে।
   - শেষে লেখাটার মাপ (size) ফেরত দেয়।
4. **Paint।** `RenderParagraph.paint()` canvas-এ লেখে: "এই জায়গায় এই paragraph আঁকো"। এখানে কিন্তু আসলে কিছু আঁকা হয় না। শুধু নির্দেশের একটা তালিকা তৈরি হয় — একে বলে display list। এই তালিকা একটা layer-এর ভেতরে রাখা থাকে।
5. **Raster।** Raster মানে নির্দেশ থেকে আসল pixel বানানো। Layer tree এবার raster thread-এ যায়। Impeller প্রতিটা অক্ষরের ছবি (glyph) একটা বড় ছবিতে (texture) জমা রাখে — একে বলে glyph atlas। তারপর GPU-কে Vulkan command পাঠায়: "এই texture থেকে এই অক্ষরগুলো নিয়ে এখানে বসাও"।
6. **Screen।** GPU ছবিটা আঁকে `FlutterView`-এর surface-এর buffer-এ। Buffer মানে memory-তে রাখা একটা পুরো ছবি। SurfaceFlinger এই buffer-কে status bar আর বাকি সব window-এর সাথে মিলিয়ে display-এ পাঠায়।

**Compose-এ:**

```kotlin
Text("আজকের নোট")
```

1. **Composition।** Compose runtime আপনার function-টা চালায়, আর ফলটা মনে রাখে। এই মনে রাখার জায়গাকে বলে slot table। তারপর UI tree-তে একটা `LayoutNode` বসায়। সাথে text-এর জন্য একটা modifier node-ও বসায়।
2. **Measure আর layout।** লেখা মাপতে Compose Android-এর নিজের text system ডাকে। সেটা হলো `StaticLayout`, যার ভেতরে Minikin আর HarfBuzz কাজ করে। Font আসে phone-এর system font থেকে (বাংলার জন্য Noto Sans Bengali)। তবে আপনি নিজের font দিলে সেটাই ব্যবহার হয়।
3. **Draw।** Android `Canvas`-এ text আঁকা হয়। এখানেও আসলে কিছু আঁকা হয় না, শুধু নির্দেশ লিখে রাখা হয় (recording)। এই display list থাকে `AndroidComposeView`-এর `RenderNode`-এ।
4. **RenderThread।** Main thread-এর কাজ শেষ হলে Android-এর renderer **HWUI** কাজ শুরু করে। এটা চলে নিজের আলাদা thread-এ, যার নাম RenderThread। HWUI display list পড়ে, তারপর Skia দিয়ে GPU command বানায় (OpenGL ES বা Vulkan)।
5. **Screen।** ছবিটা window-এর surface-এ আঁকা হয় → SurfaceFlinger → display।

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

**এখান থেকে বড় শিক্ষা:** Android জানে না যে Flutter-এর screen-এ একটা "Text" আছে। Android-এর কাছে ওটা শুধু কিছু pixel। এর দুইটা ফল:

1. TalkBack নিজে থেকে লেখাটা পড়তে পারে না। তাই Flutter আলাদা একটা semantics tree বানিয়ে Android-কে দেয়।
2. Google Map বা WebView-এর মতো native View বসাতে হলে Platform View লাগে।

Compose-এর এই সমস্যা নেই। কারণ Compose Android-এর নিজের UI system-এর ভেতরেই চলে।

[উপরে ফিরুন](#toc)

### <a id="ch13-5"></a>১৩.৫ দুই renderer: HWUI বনাম Impeller, আর SurfaceFlinger

**এক লাইনে:** Native Android আঁকে **HWUI** দিয়ে (যার ভেতরে Skia)। Flutter আঁকে নিজের **Impeller** দিয়ে। দুইজনের আঁকা ছবি শেষে **SurfaceFlinger** একসাথে মিলিয়ে screen-এ পাঠায়।

**নামগুলো এক এক করে:**

- **HWUI (Hardware UI)।** Android framework-এর renderer, C++-এ লেখা। এটা RenderThread-এ চলে। Android 9 থেকে এটা ভেতরে Skia ব্যবহার করে, আর OpenGL ES বা Vulkan দিয়ে GPU-তে আঁকে। পুরনো View আর Compose — দুইটাই এই HWUI দিয়ে আঁকে।
- **Impeller।** Flutter engine-এর নিজের renderer। এটা raster thread-এ চলে। Android 10+ (API 29) device-এ Vulkan থাকলে Impeller Vulkan ব্যবহার করে। Vulkan না থাকলে OpenGL ES দিয়ে আঁকে (fallback)। আগে Flutter-ও Skia দিয়ে আঁকত।
- **SurfaceFlinger।** এটা system-এর একটা আলাদা process। এর কাজ হলো সব ছবি জোড়া লাগানো (compositor)। Screen-এ যা দেখেন, তার প্রতিটা অংশ নিজের আলাদা buffer-এ আঁকা হয়: আপনার app, status bar, navigation bar, keyboard। SurfaceFlinger এই সব buffer মিলিয়ে একটা ছবি বানায়। তারপর Hardware Composer (HWC) দিয়ে display-তে পাঠায়।
- **Vsync।** Display একটা নির্দিষ্ট সময় পর পর সংকেত দেয়: "নতুন frame দাও"। 60Hz screen-এ প্রতি ১৬.৭ ms পর পর, 120Hz screen-এ প্রতি ৮.৩ ms পর পর। Android-এ `Choreographer` এই সংকেত app-কে পৌঁছে দেয়। Flutter engine-ও এই `Choreographer` থেকেই vsync নেয়।

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

**Impeller কেন এল:** Shader হলো GPU-তে চলা ছোট program। Skia এই shader তৈরি করত app চলার সময়ে। তাই কোনো animation প্রথমবার চললে shader বানাতে সময় লাগত, আর frame সময়মতো তৈরি হতো না (frame miss)। একে বলে shader compilation jank। Impeller-এর সব shader engine build করার সময়েই compile করা থাকে। তাই প্রথম frame থেকেই animation মসৃণ চলে।

**Jank কোথায় খুঁজবেন:** প্রতিটা frame-এর জন্য বাঁধা সময় আছে (যেমন ১৬.৭ ms)। এই সময়ের মধ্যে দুইটা thread-কেই কাজ শেষ করতে হয়: UI-র thread আর GPU-র thread। যেকোনো একটা দেরি করলেই jank।

- Flutter DevTools-এ এরা দুইটা bar: UI আর Raster।
- Android-এ Perfetto system trace-এ এরা main thread আর RenderThread।

**ফাঁদ:** অনেকে বলে "Compose-ও Flutter-এর মতো নিজে আঁকে"। না। Compose Android-এর View system-এর ভেতরেই থাকে (একটা `AndroidComposeView` হিসেবে), আর HWUI দিয়েই আঁকে। এজন্য Compose আর পুরনো View এক screen-এ সহজে একসাথে চলে। কিন্তু Flutter-কে native View বসাতে বাড়তি কাজ করতে হয়।

[উপরে ফিরুন](#toc)

### <a id="ch13-6"></a>১৩.৬ Gradle কী করে, আর release APK বানালে কী হয়

**এক লাইনে:** Gradle একটা build tool। এটা তিনটা কাজ করে:

1. Build-এর জন্য কোন কোন কাজ (task) লাগবে, তার তালিকা বানায়।
2. কোন task কোনটার আগে চলবে, সেটা ঠিক করে।
3. যে task-এর input বদলায়নি, সেটা আবার চালায় না।

Android Gradle Plugin (AGP) এই Gradle-এ Android build-এর task-গুলো যোগ করে। Flutter-ও Android build করতে এই Gradle-ই চালায়।

**Flutter-এ কি Gradle লাগে?** হ্যাঁ। Android-এর জন্য সবসময় লাগে। `flutter run` আর `flutter build apk` — দুইটাই ভেতরে `android/` folder-এ Gradle চালায়। এজন্যই প্রথম `flutter run` এত ধীর হয়: Gradle download হয়, dependency download হয়, daemon চালু হয়। iOS-এ Gradle নেই। সেখানে আছে Xcode (`xcodebuild`), আর CocoaPods বা Swift Package Manager।

**Gradle তিন ধাপে চলে:**
1. **Initialization।** `settings.gradle.kts` পড়ে দেখে project-এ কোন কোন module আছে। Flutter project-এ প্রতিটা plugin-ও একটা আলাদা module।
2. **Configuration।** প্রতিটা `build.gradle.kts` চালায়, আর সব task কে কার ওপর নির্ভর করে তার একটা graph বানায়।
3. **Execution।** আপনি যে task চেয়েছেন (যেমন `assembleRelease`), শুধু সেটা চালায়। সাথে চালায় তার আগে যেগুলো লাগে। কোনো task-এর input না বদলালে সেটা "UP-TO-DATE" লিখে বাদ যায়।

**Gradle-এর আরও কিছু অংশ:**
- **Wrapper:** `gradlew` আর `gradle-wrapper.properties`। এখানে project নিজের Gradle version লিখে রাখে। তাই team-এর সবাই একই version পায়।
- **Daemon:** একটা JVM process, যেটা build শেষেও পেছনে চলতে থাকে। ফলে পরের build-এ JVM নতুন করে চালু করতে হয় না, build দ্রুত হয়।
- **Cache:** `~/.gradle/caches`-এ dependency আর build output।
- **Maven repository:** `google()` আর `mavenCentral()` থেকে library আসে — pub.dev-এর জায়গায়।

**Native: `./gradlew assembleRelease`**

1. **Manifest merge।** App আর সব library-র manifest মিলিয়ে একটা।
2. **Resource।** AAPT2 সব `res/` compile করে। তারপর `R` class আর `resources.arsc` বানায়।
3. **Code generation।** KSP চলে। এটা Room আর Hilt-এর জন্য দরকারি code নিজে লিখে দেয়।
4. **Compile।** `kotlinc` আর `javac` আপনার code-কে `.class` বানায়।
5. **R8** (যদি `isMinifyEnabled = true` দেন)। R8 একবারে চারটা কাজ করে: shrink (অব্যবহৃত code বাদ), optimize (code দ্রুত করা), obfuscate (নাম ছোট করা), আর dex বানানো। ফল: `classes.dex`। R8 চালু না থাকলে শুধু D8 চলে, আর সেটা শুধু dex বানায়।
6. **Native library।** সব `.so` file এক জায়গায় জমা হয় (`lib/arm64-v8a/...`)। .so হলো C/C++ থেকে বানানো machine code-এর file।
7. **Package।** সব কিছু zip করে APK বানানো হয়। তারপর file-গুলো memory-তে পড়ার সুবিধার জন্য সাজানো হয় (align)।
8. **Sign।** Release keystore দিয়ে APK sign করা হয়। Sign না করা APK phone-এ install হয় না।

ফল: `app/build/outputs/apk/release/app-release.apk`।

**Flutter: `flutter build apk --release`**

1. **Flutter tool** (এটা Dart-এ লেখা) প্রথমে `pubspec.yaml` পড়ে, আর `pub get` চালায়। তারপর plugin-এর তালিকা দেখে দুইটা জিনিস বানায়: `GeneratedPluginRegistrant`, আর Gradle-এর জন্য plugin-এর list।
2. তারপর Gradle চালায়: `gradlew assembleRelease`।
3. Flutter Gradle Plugin এই build-এ নিজের একটা task যোগ করে (`compileFlutterBuildRelease`)। এই task আবার Flutter tool-কে ডাকে, Dart অংশ build করার জন্য। সেখানে তিনটা কাজ হয়:
   - **`frontend_server`:** Dart code-কে kernel (`.dill`) বানায়। এই সময় যে code কোথাও ব্যবহার হয় না, সেটা বাদ যায় — একে বলে tree shaking।
   - **`gen_snapshot`:** kernel-কে machine code বানায়, প্রতিটা ABI-র জন্য আলাদা করে। ABI মানে phone-এর CPU-র ধরন (arm64, arm, x86_64)। ফল: `libapp.so`।
   - **Asset:** image, font আর `pubspec`-এ লেখা asset যায় `flutter_assets/` folder-এ। Material Icons font থেকে শুধু ব্যবহার হওয়া icon-গুলো রাখা হয় (icon tree shaking)।
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

Flutter APK native APK-এর চেয়ে বড় হয়। এর দুইটা কারণ: `libflutter.so` (পুরো engine), আর প্রতিটা ABI-র জন্য আলাদা `.so` file। AAB দিয়ে upload করলে Play প্রতিটা phone-কে শুধু তার নিজের ABI-র অংশটা পাঠায়।

**ফাঁদ:**
- **Flutter template-এ release build নিজে থেকে debug key দিয়ে sign হয়।** আপনি নিজের keystore না বসালে আপনার "release" APK আসলে debug key-তে sign হওয়া। Play এমন APK নেয় না।
- **R8 শুধু Kotlin আর Java code ছোট করে।** Dart code-এর নাম লুকাতে (obfuscate) আলাদা করে `--obfuscate --split-debug-info` দিতে হয়।
- **`flutter clean` error-এর কারণ দেখায় না।** এটা শুধু `build/`, `.dart_tool/` আর কিছু generated file মোছে। Gradle-এর cache (`~/.gradle`) থেকেই যায়। Gradle error-এর আসল কারণ দেখতে চালান: `cd android && ./gradlew assembleRelease --stacktrace`।

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
| Maven repository | যেখান থেকে library download হয় | pub.dev |
| `gradlew` (wrapper) | Gradle version ঠিক রাখে | FVM দিয়ে Flutter version ঠিক রাখা |
| D8 / R8 | dex বানায়, ছোট করে | `gen_snapshot`, tree shaking, `--obfuscate` |
| ART | app-এর code চালায় | Dart VM / Dart runtime |
| HWUI + Skia | UI আঁকে | Impeller |
| adb | install, log, shell | `flutter install`, `flutter logs` — ভেতরে adb |
| Logcat, Layout Inspector, Perfetto | log, UI আর performance দেখা | DevTools |

> **মনে রাখুন**
> - Flutter = UI toolkit (framework + engine + embedder)। Process, lifecycle, permission — Android-এর।
> - Computer-এ JVM চালায় build। Phone-এ ART চালায় Kotlin, আর Dart runtime চালায় Dart। Android-এ JVM নেই।
> - App খোলার পথ: Launcher → system_server → Zygote fork → Application → Activity → প্রথম frame। Flutter-এ এর মাঝে engine load হয়, আর Dart-এর `main()` চলে।
> - Native আঁকে HWUI দিয়ে (ভেতরে Skia)। Flutter আঁকে Impeller দিয়ে। দুইজনের ছবিই শেষে SurfaceFlinger screen-এ বসায়।
> - Flutter-এর Android build মানে Gradle build। Dart অংশটা `gen_snapshot` দিয়ে `libapp.so` হয়।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Flutter একটা UI toolkit — framework, engine আর embedder। App খুললে Zygote থেকে process fork হয়, তারপর Application আর FlutterActivity তৈরি হয়। FlutterActivity engine load করে, Dart-এর main চালায়, আর Impeller দিয়ে একটা SurfaceView-তে নিজে আঁকে। Native app সেখানে Android-এর HWUI দিয়ে আঁকে। দুই ক্ষেত্রেই শেষে SurfaceFlinger ছবিটা screen-এ বসায়। Build-এ Flutter Gradle চালায়: Kotlin dex হয়ে ART-এ চলে, আর Dart AOT compile হয়ে libapp.so-তে machine code হয়।"
> - *English:* "Flutter is a UI toolkit: a framework, an engine and an embedder. When the app opens, Zygote forks a process, then the Application and FlutterActivity are created. FlutterActivity loads the engine, runs Dart's main, and draws by itself into a SurfaceView with Impeller. A native app draws with Android's HWUI instead. In both cases SurfaceFlinger puts the final image on screen. For the build, Flutter runs Gradle: Kotlin becomes dex and runs on ART, and Dart is AOT-compiled into machine code in libapp.so."

[উপরে ফিরুন](#toc)

---

## <a id="ch14"></a>১৪. শেখার পরিকল্পনা — ৪ সপ্তাহ

শুধু পড়ার চেয়ে নিজে বানিয়ে শিখলে অনেক দ্রুত শেখা হয়। আপনার জন্য সবচেয়ে দ্রুত পথ: **এই বই জুড়ে যে Notes app দেখলেন, সেটা native-এ বানান।** প্রতিটা অংশ Flutter-এ কীভাবে লিখতেন, তা আপনি আগেই জানেন। শুধু সেটা Kotlin আর Compose-এ লিখবেন।

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

এই তিন প্রশ্নের উত্তর মুখে বলতে পারলে আপনি interview-এর জন্য তৈরি। শেষে [Android Interview Prep](../../interviews/software-engineer-flutter-android-ios-bn/flutter-android-ios-interview-prep-bn.md) খুলুন। প্রশ্নগুলোর উত্তর জোরে জোরে বলে practice করুন। ওখানে প্রতিটা উত্তর বাংলা আর English দুই ভাষায় আছে।

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
| `BuildContext` | (মিল নেই) — `Context` দিয়ে system-এর service আর resource পাওয়া যায় |
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

এবার iOS। এটাও আপনি আগে দেখেছেন — প্রতিটা Flutter app-এর `ios/` folder-এ একটা পুরো iOS project আছে। খণ্ড ১-এর মতোই এখানেও প্রতিটা জিনিস আগে Flutter-এ দেখাব, তারপর iOS-এ (Swift, SwiftUI)। যেখানে কাজে লাগে, সেখানে Android-এর সাথে এক লাইনের তুলনাও দেব।

[উপরে ফিরুন](#toc)

---

## <a id="ios0"></a>iOS ০. বড় ছবি — আপনার Flutter app আসলে একটা iOS app

**এক লাইনে:** iOS-এও Flutter শুধু UI আঁকে আর Dart code চালায়। বাকি সব iOS করে: app চালু হওয়া, lifecycle, permission, notification, background কাজ, signing। Flutter-এ এগুলো plugin-এর পেছনে লুকানো ছিল। এই খণ্ডে সেগুলো সরাসরি দেখব।

Android অংশে আপনি একই জিনিস একবার পড়েছেন ([অধ্যায় ০](#ch0))। গঠন একই। শুধু নামগুলো আলাদা, আর কিছু নিয়ম আরও কড়া। এই অধ্যায় বুঝলে iOS-এর বাকি অধ্যায়গুলো সহজ হয়ে যাবে।

> **Version নিয়ে:** এই লেখা নভেম্বর ২০২৬-এর। তখন সর্বশেষ version: Xcode 27, iOS 27, Swift 6.4, আর Flutter stable 3.47। Apple প্রতি বছর জুনে (WWDC-তে) নতুন version ঘোষণা করে, আর সেপ্টেম্বরে বের করে। তাই কোনো API কোন iOS version থেকে আছে, সেটা প্রতিটা জায়গায় পাশে লেখা থাকবে।

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

আর `Runner/Base.lproj/Main.storyboard`-এ প্রথম screen হিসেবে আছে একটা `FlutterViewController`। ব্যস, এটুকুই। User app-এর icon-এ tap করলে এই ধাপগুলো হয়:

1. iOS app-এর জন্য একটা process চালু করে। `@main` দেখে iOS বোঝে, শুরু করতে হবে `AppDelegate` থেকে।
2. iOS একটা **scene** বানায়। Scene মানে app-এর একটা window। `SceneDelegate` সেই window-এর ঘটনাগুলো সামলায়। Window-এ বসানো হয় `Main.storyboard`-এর `FlutterViewController`।
3. `FlutterViewController` একটা **`FlutterEngine`** চালায়। Engine-এর ভেতরে Dart runtime চলে, আর আপনার `main()` call হয়। Engine তৈরি হলে `didInitializeImplicitFlutterEngine` call হয়, আর সেখানে সব plugin register হয়।
4. `FlutterViewController`-এর view পুরো screen জুড়ে একটা Metal surface। (Metal হলো Apple-এর GPU API।) Flutter এই surface-এ নিজের widget নিজেই আঁকে, **Impeller** দিয়ে। iOS-এ Flutter 3.29 থেকে Impeller-ই একমাত্র renderer। Skia আর বেছে নেওয়া যায় না।
5. Camera, Keychain বা notification লাগলে Dart code **platform channel** দিয়ে Swift বা Objective-C code-কে কাজটা করতে বলে। Plugin বলতে এটাই বোঝায়।

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

**কেন release-এ AOT ছাড়া উপায় নেই:** iOS কোনো সাধারণ app-কে চলার সময় নতুন machine code বানিয়ে চালাতে দেয় না। অথচ JIT ঠিক এই কাজটাই করে। তাই:

- Dart-এর JIT শুধু debug-এ চলে। আর debug app শুধু Xcode বা `flutter run` থেকেই খোলা যায়।
- Release build-এ সব Dart code আগেই machine code হয়ে যায় (AOT)।
- এজন্যই hot reload শুধু debug-এ কাজ করে।

Flutter-এ থাকার সময়ও আপনি আসলে iOS-এর এই জিনিসগুলো ব্যবহার করতেন:

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

**তাই iOS-এও আপনি শূন্য থেকে শুরু করছেন না।** নতুন শুধু দুইটা জিনিস:
- **UI:** Flutter-এ UI Flutter নিজে আঁকে। Native iOS-এ UI-ও iOS-এর নিজের — SwiftUI (আগে ছিল UIKit)।
- **ভাষা আর runtime:** Dart-এর বদলে Swift। Swift সরাসরি machine code-এ compile হয়। এখানে কোনো VM নেই, garbage collector-ও নেই। Memory সামলানো হয় reference count দিয়ে — কতজন একটা object ব্যবহার করছে, সেটা গুনে রাখা হয়, আর গোনা শূন্য হলে object মুছে যায় ([iOS ১.৫](#ios1-5))।

[উপরে ফিরুন](#toc)

### <a id="ios0-2"></a>iOS ০.২ iOS-এর স্তরগুলো

iOS হলো Apple-এর operating system। তার ওপরে স্তরে স্তরে app বানানোর framework সাজানো। ছবিতে ওপরে আপনার app, আর সবচেয়ে নিচে kernel:

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

Android-এর স্তরগুলোর সাথে মিলিয়ে দেখুন ([০.২](#ch0-2))। একটা বড় পার্থক্য আছে। এটা আপনার রোজকার কাজে লাগবে:

- **Android-এ Jetpack আছে।** Compose, Room, ViewModel — এগুলো আপনার app-এর ভেতরেই ঢুকে যায় (bundle হয়)। তাই phone-এ Android-এর যে version-ই থাকুক, একই code চলে।
- **iOS-এ Jetpack-এর মতো কিছু নেই।** SwiftUI, SwiftData, Observation — সব **OS-এর সাথে আসে।** iOS 17-এর phone-এ চলে iOS 17-এর SwiftUI। iOS 18-এর phone-এ চলে iOS 18-এর SwiftUI।

তাই iOS-এ প্রতিটা নতুন API-র পাশে লেখা থাকে, সেটা কোন iOS থেকে আছে। যেমন `@Observable` চাইলে iOS 17 লাগবে। `NavigationStack` চাইলে iOS 16 লাগবে। পুরনো phone-ও চালাতে চাইলে এভাবে লিখবেন:

```swift
if #available(iOS 17, *) {
    // নতুন API
} else {
    // পুরনো পথ
}
```

এটা Android-এর `Build.VERSION.SDK_INT >= 34`-এর মতোই। ভালো খবর হলো, iPhone user-রা খুব তাড়াতাড়ি নতুন iOS-এ update করে। তাই বেশিরভাগ app শুধু শেষ দুই-তিনটা iOS version-এ চলে। আপনার app সবচেয়ে পুরনো যে iOS-এ চলবে, তাকে বলে **deployment target** ([iOS ৩.৮](#ios3-8))।

**Swift runtime-ও OS-এর অংশ।** iOS 12.2 থেকে Swift-এর standard library phone-এই থাকে। তাই app-এর ভেতরে Swift runtime আলাদা করে রাখতে হয় না।

[উপরে ফিরুন](#toc)

### <a id="ios0-3"></a>iOS ০.৩ iOS আর Android-এর বড় পার্থক্য

Android থেকে এলে চারটা জিনিস প্রথম দিনেই অবাক করবে।

**১. Sandbox — প্রতিটা app আলাদা, বন্ধ জায়গায়।** iOS-এ প্রতিটা app-এর নিজের একটা folder আছে (`Documents/`, `Library/`, `tmp/`)।
- অন্য app-এর file দেখা যায় না।
- Shared storage-এ ইচ্ছামতো লেখা যায় না।
- দুই app-এর মধ্যে data ভাগ করতে App Group লাগে। সেটা আগে থেকেই entitlement-এ লিখে রাখতে হয় ([iOS ৩.৭](#ios3-7))। Entitlement হলো app-এর বিশেষ অনুমতির তালিকা।

Android-এও sandbox আছে, কিন্তু iOS-এরটা অনেক বেশি কড়া।

**২. Background-এ app থেমে যায় (suspension)।** Android-এ background-এ কিছু কাজ চলতে পারে। Foreground service দিয়ে অনেকক্ষণ কাজ চালানোও যায়। iOS-এ এমন না:
- User home-এ গেলে app অল্প কিছু সময় পায়।
- তারপর app **suspend** হয়। মানে app memory-তে থাকে, কিন্তু একটা লাইন code-ও চলে না।
- Background-এ কাজ করতে হলে iOS-এর দেওয়া নির্দিষ্ট পথ নিতে হয় (background task, push, background mode)।
- Suspend থাকা app-কে system কোনো খবর না দিয়েই বন্ধ করে দিতে পারে ([iOS ৪.৪](#ios4-4))।

**৩. একটাই store, আর প্রতিটা release-এ review।** Android-এ Play Store ছাড়াও APK দিয়ে app দেওয়া যায়। iOS-এ App Store-ই প্রায় একমাত্র পথ। কিছু অঞ্চলে (যেমন EU) আইনের কারণে অন্য marketplace আছে, কিন্তু বেশিরভাগ দেশে নেই। প্রতিটা নতুন version Apple-কে review করে পাশ করাতে হয়। আর upload করতে নির্দিষ্ট Xcode লাগে: ২৮ এপ্রিল ২০২৬ থেকে Xcode 26 বা নতুন, আর build হতে হবে iOS 26 SDK দিয়ে।

**৪. সব জায়গায় signing।** Android-এ debug build নিজে থেকেই একটা debug key দিয়ে sign হয়। iOS-এ নিজের phone-এ চালাতেও signing লাগে। তার জন্য লাগে: Apple Developer account, certificate, App ID, আর provisioning profile। Push বা App Group চাইলে সেটা entitlement-এ লিখতে হয়, আর provisioning profile-এও সেটা থাকতে হয়। Flutter-এ Xcode-এ "Team" বেছে দেওয়ার সময় আপনি এর একটা অংশ দেখেছেন।

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

এটা iOS অংশের সবচেয়ে কাজের table। প্রথম কলামে কাজটা। তারপর পরপর: আজ iOS-এ কোনটা ব্যবহার করবেন, পুরনো কোনটা চিনে রাখবেন, Android-এ কী, আর Flutter-এ কী।

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

**পুরনো কলামটা কেন রাখলাম:** এগুলো আপনি interview-এ, পুরনো project-এ, আর প্রায় সব Flutter plugin-এর iOS code-এ দেখবেন। Plugin-এর iOS অংশ এখনো বেশিরভাগ UIKit, GCD আর completion handler দিয়ে লেখা। তবে নতুন code লিখবেন "আজকের best" কলাম দেখে।

**একটা সতর্কতা:** iOS-এ "আজকের best" কোনটা, সেটা অনেক সময় আপনার deployment target ঠিক করে দেয়। SwiftData আর `@Observable` চাইলে iOS 17 লাগবে। App যদি iOS 16-এও চালাতে হয়, তাহলে পুরনো কলামের কিছু জিনিস এখনো লাগবে।

> **মনে রাখুন**
> - আপনার প্রতিটা Flutter app-এর `ios/` একটা পুরো Xcode project। `FlutterViewController` একটা সাধারণ `UIViewController`।
> - Dart code release-এ AOT হয়ে `App.framework`-এ যায়, engine থাকে `Flutter.framework`-এ।
> - iOS-এ Jetpack-এর মতো কিছু নেই। Framework OS-এর সাথে আসে। তাই প্রতিটা API-র জন্য একটা সবচেয়ে কম iOS version লাগে।
> - চার বড় পার্থক্য: কড়া sandbox, background-এ suspension, একটাই store আর review, সব জায়গায় signing।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ Flutter একটা `FlutterViewController`-এর ভেতরে চলে। Engine একটা Metal surface-এ Impeller দিয়ে নিজে আঁকে। Release-এ Dart code AOT হয়ে `App.framework`-এ যায়, কারণ iOS JIT দিতে দেয় না। Lifecycle, permission, background কাজ সবসময় iOS-এর। তাই plugin-এর আড়ালে যা ছিল, native-এ সেটা আমি সরাসরি Swift-এ লিখি।"
> - *English:* "On iOS, Flutter runs inside a `FlutterViewController`. The engine draws on a Metal surface with Impeller. In release, Dart is compiled ahead of time into `App.framework`, because iOS doesn't allow JIT for normal apps. Lifecycle, permissions and background work always belong to iOS, so in native I write directly in Swift what plugins used to hide."

[উপরে ফিরুন](#toc)

---
## <a id="ios1"></a>iOS ১. Swift — Dart-এর পাশে

Swift পড়তে গিয়ে বারবার মনে হবে, "এটা তো চিনি।" `?`, `??`, `async`/`await`, extension, generics — সবই আছে। Kotlin-এর সাথে মিল আরও বেশি। তবে দুইটা জিনিস একদম নতুন। Swift বুঝতে হলে এই দুইটাই আসল:

- **`struct` হলো value type।** মানে, এক variable থেকে আরেকটায় দিলে (assign করলে) পুরো জিনিসটা copy হয়। Swift-এর প্রায় সব model struct দিয়ে লেখা।
- **Garbage collector নেই।** Memory সামলায় **ARC**। ARC গুনে রাখে, একটা object-কে কয়জন ধরে আছে (reference count)। তাই দুই object একে অপরকে ধরে রাখছে কি না (retain cycle), সেটা আপনাকেই খেয়াল রাখতে হয়।

এই দুইটা ভালো করে বুঝলে বাকি Swift শিখতে একদিনই যথেষ্ট। Android অংশে Kotlin-এর অধ্যায়টা ([অধ্যায় ১](#ch1)) পড়া থাকলে আরও সহজ লাগবে। মাঝে মাঝে Kotlin-ও পাশে রেখেছি।

Code চালিয়ে দেখতে চাইলে Xcode-এ **File → New → Playground** খুলুন। এটা DartPad-এর মতো — লিখলেই চলে।

### <a id="ios1-1"></a>iOS ১.১ Variable আর type

**এক লাইনে:** `final` → `let`, `var` → `var`। Type লেখা হয় নামের পরে, Kotlin-এর মতো।

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
| `const` | `let` (compile-time const বলে আলাদা কিছু নেই) | `const val` |
| `'...'` বা `"..."` | শুধু `"..."` | শুধু `"..."` |
| `'$count টা'`, `'${note.title}'` | `"\(count) টা"`, `"\(note.title)"` | `"$count টা"` |
| `int`, `double` | `Int`, `Double` | `Int`, `Double` |
| `null` | `nil` | `null` |
| record `(1, 'a')` | tuple `(1, "a")` | `Pair` |
| `;` লাগে | লাগে না | লাগে না |

**Type নিজে থেকে বদলায় না।** Swift-এ `Int` আর `Double` সরাসরি যোগ করা যায় না। একটাকে নিজে হাতে অন্যটায় বদলাতে হয়:

```swift
let words = 120
let minutes = Double(words) / 200.0      // Int → Double, হাতে
```

Dart-এ `int` আর `double` দুটোই `num`। তাই সেখানে যোগ করা যায়। Swift-এ compiler এখানে আটকে দেবে।

**ফাঁদ — struct `let` হলে পুরো জিনিসটাই আর বদলানো যায় না।** ধরুন `Note` একটা struct। `let note = Note(...)` লিখলে পরে `note.title = "নতুন"` লেখাও যাবে না। Dart-এ `final note` লিখলে শুধু variable-টা আটকে যায়। ভেতরের field তখনো বদলানো যায়। কেন এমন হয়, তা [iOS ১.৪](#ios1-4)-এ দেখবেন।

[উপরে ফিরুন](#toc)

### <a id="ios1-2"></a>iOS ১.২ Optional

**এক লাইনে:** Dart-এর null safety-র মতোই — `String?`, `!`, `??`, `?.`। শুধু null check করার উপায়টা আলাদা: `if let` আর `guard let`।

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

**`guard let` — শুরুতেই বের হয়ে যান:**

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

`guard`-এর `else`-এর ভেতরে function থেকে বের হতেই হবে (`return`, `throw`, `break`)। না লিখলে compiler build হতে দেয় না। Dart-এ আপনি `if (x == null) return;` লিখে আগেভাগে বের হতেন (early return)। এটা তারই কড়া নিয়মের রূপ।

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

`String?` আসলে `Optional<String>`। তাই optional-এর ওপর `switch` চালানো যায়। `map`-ও চলে: `draftTitle.map { $0.uppercased() }`।

**কী আলাদা:** Dart আর Kotlin-এ `!= null` check করার পরে compiler নিজেই type-টাকে non-null ধরে নেয় (একে smart cast বলে)। Swift এটা করে না। তাই `if draftTitle != nil { draftTitle.count }` compile হবে না। ভেতরের value বের করতে (unwrap করতে) `if let` বা `guard let` লাগবেই।

**Best approach:** Function-এর শুরুতেই `guard let` দিয়ে সব nil-এর ক্ষেত্র বাদ দিন। তাহলে বাকি code সোজা থাকে, একটার ভেতর আরেকটা block (nesting) কম হয়।

**ফাঁদ:** `!` দিয়ে জোর করে value বের করলে (force unwrap) আর nil পেলে app সাথে সাথে crash করে। Dart-এর `!`-এর মতোই। Production code-এ `!` দেখলে review-এ প্রশ্ন উঠবে। `IBOutlet`-এর মতো কিছু পুরনো জায়গা ছাড়া এটা এড়িয়ে চলুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-3"></a>iOS ১.৩ Function আর closure

**এক লাইনে:** Swift-এর function-এ **argument label** থাকে। Call করার সময় এই label লিখতে হয়। Lambda-কে এখানে closure বলে। শেষ argument closure হলে সেটা বন্ধনীর বাইরে বসে।

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

**Argument label — এটা শুধু Swift-এই আছে।** একটা parameter-এর দুইটা নাম থাকতে পারে। একটা বাইরের নাম (label), যেটা call করার সময় লেখেন। আরেকটা ভেতরের নাম, যেটা function-এর ভেতরে ব্যবহার করেন।

```swift
func move(_ note: Note, to folder: Folder) { ... }
//        ↑ label নেই   ↑ label "to", ভেতরে নাম "folder"

move(note, to: archive)          // পড়তে ইংরেজি বাক্যের মতো
```

- `_` দিলে call করার সময় label লিখতে হয় না।
- আলাদা label না দিলে parameter-এর নামটাই label হয়। তাই Swift-এ প্রায় সব argument named। Dart-এর `{required ...}`-এর মতো, কিন্তু এটাই default।
- Dart-এর `[ ]`-এর মতো optional positional parameter-এর আলাদা syntax নেই। Default value দিলেই parameter-টা optional হয়ে যায় — label থাকুক বা `_` থাকুক (`func f(_ x: Int = 0)`)।

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

**`@escaping` — closure-টা কি পরে চলবে?** কোনো function closure নিয়ে সেটা পরে চালাতে পারে। যেমন রেখে দেয়, বা অন্য thread-এ পাঠায়। তখন parameter-এ `@escaping` লিখতে হয়:

```swift
func fetchNotes(completion: @escaping ([Note]) -> Void) {
    // network শেষে পরে completion চলবে
}
```

Dart-এ এরকম কিছু নেই। Swift-এ লাগে, কারণ পরে চলবে এমন closure যা কিছু ধরে রাখে, সেগুলোও ততক্ষণ memory-তে থেকে যায়। Retain cycle এখান থেকেই শুরু হয় ([iOS ১.৫](#ios1-5))। নতুন code-এ completion handler কম লিখবেন। তার বদলে `async` দিয়ে লিখবেন ([iOS ২](#ios2))। তবে plugin code-এ completion handler প্রচুর দেখবেন।

**ফাঁদ:** label লিখতে ভুলে যাওয়া। `move(note, archive)` compile হবে না — `to:` লিখতে হবে। প্রথম কয়েকদিন Xcode-এর autocomplete দেখে লিখুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-4"></a>iOS ১.৪ `struct` বনাম `class` — value বনাম reference

**এক লাইনে:** `struct` assign করলে পুরোটা **copy** হয়। `class` assign করলে নতুন copy হয় না। শুধু **একই object-এর আরেকটা reference** তৈরি হয় — Dart-এর সব class-এর মতো। Swift-এ model লেখার স্বাভাবিক পছন্দ struct।

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

এজন্যই Dart-এ `freezed` আর `copyWith` লাগে। যাতে কেউ ভুল করে এমন object বদলে না ফেলে, যেটা আরও কেউ ব্যবহার করছে।

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

শুধু `struct Note` লিখেই আপনি এগুলো পেয়ে গেলেন:
- **Memberwise initializer** — সব property নিয়ে একটা init, `Note(id:title:body:isPinned:updatedAt:)`, নিজে থেকেই তৈরি হয়।
- **`Equatable` আর `Hashable`** — protocol-এর নাম লিখলেই compiler `==` আর hash বানিয়ে দেয়।
- **`Codable`** — JSON-এ বদলানো আর JSON থেকে ফেরানো, কোনো code generation ছাড়াই।
- **copyWith লাগে না** — `var copy = note; copy.title = "নতুন"`। Copy-টা নিজেই একটা নতুন value।

Kotlin-এর `data class` আর Dart-এর `freezed` যে কাজ করে, Swift-এ struct একাই সেটা করে।

**Struct-এর কোনো method যদি struct-টাকেই বদলায়, তাহলে `mutating` লিখতে হয়:**

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

**Class কখন নেবেন:**

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
| Init | memberwise init নিজে থেকে পাওয়া যায় | নিজে লিখতে হয় |
| `let` হলে | কিছুই বদলানো যায় না | property বদলানো যায় (শুধু reference-টা আটকে থাকে) |
| Memory | সাধারণত সস্তা, ARC-এর ঝামেলা কম | ARC দিয়ে চলে, retain cycle হতে পারে |
| Identity (`===`) | নেই | আছে |
| Dart-এ কাছাকাছি | `freezed` model | সাধারণ class |

**ভেতরে কীভাবে কাজ করে — copy কি দামি না?** না। `Array`, `Dictionary`, `String` struct হলেও ভেতরে **copy-on-write** কৌশল ব্যবহার করে। মানে:
1. Assign করলে ভেতরের data (buffer) আসলে copy হয় না, দুইজনে ভাগ করে নেয়।
2. কেউ যখন বদলাতে যায়, ঠিক তখনই আসল copy হয়।

তাই ১০,০০০ note-এর array এক জায়গা থেকে আরেক জায়গায় পাঠানোও সস্তা।

**Best approach:**
- Data (Note, Folder, API response) — `struct`।
- যার নিজের পরিচয় (identity) আছে আর যাকে অনেকে মিলে ব্যবহার করে (store, repository, `@Observable` screen model) — `final class`।
- এমন mutable state, যেটা অনেক thread থেকে ছুঁতে হয় — `actor` ([iOS ২.৫](#ios2-5))।

**ফাঁদ:** struct কোনো function-এ পাঠিয়ে ভেতরে বদলালে বাইরেরটা বদলায় না, কারণ function পেয়েছে একটা copy। বাইরেরটাই বদলাতে চাইলে parameter-এ `inout` দিন, আর call-এ `&` লিখুন: `func rename(_ note: inout Note)`, `rename(&note)`। তবে বেশিরভাগ সময় নতুন value return করাই বেশি পরিষ্কার।

[উপরে ফিরুন](#toc)

### <a id="ios1-5"></a>iOS ১.৫ Memory: ARC, `weak` আর retain cycle

**এক লাইনে:** Dart আর Kotlin-এ garbage collector মাঝে মাঝে এসে যে object আর লাগে না, সেগুলো মুছে দেয়। Swift-এ ব্যাপারটা আলাদা। প্রতিটা class object-এর জন্য গোনা হয়, কয়জন তাকে ধরে আছে। গোনা শূন্য হলেই object সাথে সাথে মুছে যায়। এর নাম **ARC** (Automatic Reference Counting)।

**ভেতরে কীভাবে কাজ করে:**

```
let store = NotesStore()      // count = 1
let another = store           // count = 2
another = nil (ধরুন)          // count = 1
store শেষ হলো                 // count = 0 → deinit চলে, memory ফেরত
```

`retain` (গোনা বাড়ানো) আর `release` (গোনা কমানো) compiler নিজেই বসিয়ে দেয়। আপনাকে কিছু লিখতে হয় না।
- সুবিধা: object কখন মুছবে, তা আগে থেকে জানা যায়। GC-র মতো হঠাৎ app থেমে যাওয়া নেই।
- অসুবিধা: দুই object একে অপরকে ধরে রাখলে (**cycle**) গোনা কখনো শূন্য হয় না। তখন কেউই মোছে না।

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

**সমাধান — capture list-এ `[weak self]`:** Closure কোন জিনিস কীভাবে ধরবে, সেটা শুরুতে square bracket-এর ভেতরে বলে দেওয়া যায়। একে capture list বলে।

```swift
onSave = { [weak self] in
    guard let self else { return }    // editor আগেই মুছে গেলে কিছু করো না
    print(self.text)
}
```

| শব্দ | মানে | কখন |
|---|---|---|
| strong (default) | গোনায় যোগ হয় | সাধারণ সব reference |
| `weak` | গোনায় যোগ হয় না। Object মুছে গেলে নিজে থেকে `nil` হয়ে যায় (তাই সবসময় optional) | delegate, পরে চলবে এমন closure-এ `self` |
| `unowned` | গোনায় যোগ হয় না, কিন্তু nil-ও হয় না। Object মুছে যাওয়ার পরে ছুঁলে crash | শুধু যখন আপনি নিশ্চিত, object আগে মুছবে না |

**Cycle সবচেয়ে বেশি হয় এই জায়গাগুলোতে:**
- Class-এর property-তে রাখা closure, যেটা `self` ধরে রাখে।
- Delegate pattern। তাই delegate property সবসময় `weak var delegate: NoteEditorDelegate?`।
- Timer, আর `NotificationCenter`-এর block দিয়ে লেখা observer।
- পুরনো Combine code-এর `sink { self... }`।

**Dart-এর সাথে পার্থক্য:** Dart-এর GC cycle-ও খুঁজে বের করে মুছে দেয়। Flutter-এ `StreamSubscription` cancel না করলে leak হতো ঠিকই। কিন্তু দুই object-এর cycle নিয়ে আপনাকে কখনো ভাবতে হয়নি। Swift-এ ভাবতে হবে।

**ভালো খবর:**
- struct আর enum ARC-এর cycle-এ পড়ে না। SwiftUI-র View হলো struct। তাই SwiftUI code-এ `[weak self]` প্রায় লাগেই না।
- `Task { }`-এর ভেতরে `self` ধরলে task শেষ হওয়ামাত্র ছেড়ে দেয়। তবে যে task অনেকক্ষণ চলে (যেমন কখনো শেষ না হওয়া `for await` loop), সেখানে এটাও leak করতে পারে।

**ফাঁদ:** না ভেবে সব জায়গায় `[weak self]` বসানো। `notes.map { self.format($0) }`-এর মতো closure সাথে সাথে চলে শেষ হয়ে যায় (non-escaping)। সেখানে cycle হয় না, `weak` লাগে না। শুধু `@escaping` closure, যেটা কোথাও রেখে দেওয়া হয়, সেখানে ভাবুন।

**নিজে দেখুন:** class-এ `deinit { print("...") }` লিখুন। Screen বন্ধ করার পরে print না হলে বুঝবেন leak হচ্ছে। Xcode-এর **Debug Memory Graph** বোতাম চাপলে cycle-টা ছবি দিয়ে দেখায়।

[উপরে ফিরুন](#toc)

### <a id="ios1-6"></a>iOS ১.৬ `enum` আর `switch`

**এক লাইনে:** Swift-এর `enum`-এর প্রতিটা case নিজের আলাদা data রাখতে পারে। এই data-কে associated value বলে। Dart-এর `sealed class` বা Kotlin-এর `sealed interface` দিয়ে যে কাজ করেন, Swift-এ সেটা এক লাইনে হয়।

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

- `switch` সব case না ধরলে compile হবে না — Dart-এর exhaustive switch-এর মতো। নতুন case যোগ করলে compiler সব জায়গা দেখিয়ে দেবে, যেখানে ঠিক করতে হবে।
- `break` লিখতে হয় না। এক case শেষ হলে নিজে থেকে পরের case-এ চলে যায় না।
- Swift 5.9 থেকে `if` আর `switch` expression হিসেবে value return করতে পারে। তাই ওপরের function-এ `return` লাগেনি।
- Type জানা থাকলে শুধু `.idle` লিখলেই হয়। `SyncState.idle` লিখতে হয় না।

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
| `switch` expression | `switch` (Swift 5.9+ থেকে expression-ও) | `when` |
| `Sort.values` | `CaseIterable` → `.allCases` | `entries` |
| `Sort.newest.name` | raw value: `.rawValue` | `.name` |

**Best approach:** Screen-এর অবস্থা (loading / loaded / error), sync-এর অবস্থা, navigation route — সবকিছুর জন্য enum নিন। কয়েকটা Bool flag দিয়ে (`isLoading`, `hasError`) অবস্থা রাখলে এমন অবস্থাও তৈরি হতে পারে, যা আসলে হওয়ার কথা না। যেমন একসাথে loading আর error দুটোই true। Enum দিলে এটা হয় না।

**ফাঁদ:** `default:` দিয়ে বাকি সব case একসাথে ধরে ফেলা। তাহলে নতুন case যোগ করলে compiler আর সতর্ক করবে না। নিজের লেখা enum-এ `default` এড়িয়ে চলুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-7"></a>iOS ১.৭ Protocol আর extension

**এক লাইনে:** `protocol` হলো Dart-এর `abstract interface class` আর Kotlin-এর `interface`। `extension` হলো Dart-এর `extension`, কিন্তু অনেক বেশি ক্ষমতা আছে। Extension দিয়ে একটা type-কে নতুন protocol-ও মানানো যায়।

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

শেষ লাইনটা Dart-এ সম্ভব না। Dart-এ class লেখার সময়েই `implements` লিখে দিতে হয়। Swift-এ যেকোনো type-কে পরে নতুন protocol মানানো যায় — এমনকি `String` বা Apple-এর কোনো type-কেও। একে **retroactive conformance** বলে।

একটা সাবধানতা আছে। অন্য module-এর type-কে অন্য module-এর protocol মানালে Swift 6 সতর্ক করে। যেমন Apple-এর type-কে Apple-এর protocol মানানো। তখন `@retroactive` লিখতে বলে। কারণ পরে Apple নিজেই সেটা যোগ করলে একই জিনিসের দুইটা implementation হয়ে যাবে।

**`some` আর `any` — দুইটা আলাদা জিনিস:**

```swift
// some: একটা নির্দিষ্ট type, compiler জানে কোনটা। দ্রুত।
var body: some View { Text("Notes") }

// any: যেকোনো type, যে protocol মানে। Runtime-এ বাক্সে ভরা।
let repository: any NotesRepository = RemoteNotesRepository()
```

| | `some Protocol` | `any Protocol` |
|---|---|---|
| মানে | "একটা নির্দিষ্ট type আছে, শুধু নামটা বলছি না" | "যেকোনো type, এই protocol মানলেই চলবে" |
| Type কখন ঠিক হয় | compile-time | runtime |
| খরচ | কম | একটু বেশি (box লাগে, method খোঁজা হয় runtime-এ) |
| কোথায় দেখবেন | SwiftUI-র `some View` | dependency রাখার জায়গায়: `let repo: any NotesRepository` |

Dart-এ সব interface type আসলে `any`-এর মতো কাজ করে। Swift আপনাকে দুইটার মধ্যে বেছে নিতে দেয়।

**Best approach:** Repository বা API client-এর মতো জায়গায়, যেখানে test-এ fake লাগবে, সেখানে protocol নিন। কিন্তু যার একটাই implementation, তার জন্য "পরে যদি লাগে" ভেবে protocol বানাবেন না। ছোট helper (`preview`, `wordCount`) extension-এ রাখুন।

**ফাঁদ:** কিছু protocol-এর ভেতরে নিজের generic type থাকে, একে `associatedtype` বলে। যেমন `Identifiable`-এর `ID`। এমন protocol আগে সাধারণ variable-এর type হিসেবে ব্যবহার করা যেত না। Swift 5.7 থেকে `any Identifiable` লেখা যায়। কিন্তু ভেতরের associated type নিয়ে কাজ করা তখনো ঝামেলার। এমন জায়গায় generics ব্যবহার করুন।

[উপরে ফিরুন](#toc)

### <a id="ios1-8"></a>iOS ১.৮ Generics

**এক লাইনে:** Dart-এর `<T>` আর `T extends X`-এর মতোই। শর্ত (constraint) লেখা হয় `T: Protocol` দিয়ে, অথবা `where` দিয়ে।

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

**`where` দিয়ে আরও শর্ত:**

```swift
extension Array where Element == Note {
    var pinned: [Note] { filter(\.isPinned) }       // শুধু [Note]-এ পাওয়া যাবে
}
```

`\.isPinned`-কে বলে **key path**। এটা "Note-এর isPinned property"-কে নির্দেশ করে। `{ $0.isPinned }` লেখার ছোট রূপ।

| Dart | Swift | Kotlin |
|---|---|---|
| `<T extends Comparable>` | `<T: Comparable>` | `<T : Comparable<T>>` |
| একের বেশি শর্ত | `<T: A & B>` বা `where T: A, T: B` | `where T : A, T : B` |
| `extension on List<Note>` | `extension Array where Element == Note` | `fun List<Note>.pinned()` |
| (নেই) | `associatedtype` — protocol-এর ভেতরের generic | (নেই, generic interface) |

**ফাঁদ:** একটা জায়গায়, একটাই type-এর জন্য generic বানানো। আগে সাধারণ code লিখুন। দ্বিতীয় বা তৃতীয় type এলে তখন generic বানান।

[উপরে ফিরুন](#toc)

### <a id="ios1-9"></a>iOS ১.৯ Error handling — `throws`, `try`, `Result`

**এক লাইনে:** Swift-এ কোন function error ছুঁড়তে পারে, সেটা signature-এই লেখা থাকে (`throws`)। আর সেই function call করার সময় `try` লিখতে হয়। Dart-এ যেকোনো function যেকোনো সময় throw করতে পারে, আগে থেকে কেউ বলে দেয় না।

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

**`try` তিনভাবে লেখা যায়:**

| লেখা | মানে | কখন |
|---|---|---|
| `try f()` | error হলে ওপরের caller-এর কাছে পাঠাও | `do/catch`-এর ভেতরে, বা নিজের function `throws` হলে |
| `try? f()` | error হলে `nil` দাও | ব্যর্থ হলেও সমস্যা নেই এমন জায়গায় (যেমন cache পড়া) |
| `try! f()` | error হলে crash | প্রায় কখনোই না |

**`Result` — error-কে একটা value হিসেবে রাখা:**

```swift
let result: Result<[Note], NoteError> = .success(notes)

switch result {
case .success(let notes): show(notes)
case .failure(let error): showError(error)
}
```

`async`/`await` আসার পরে `Result` কম লাগে। এখন এটা মূলত পুরনো completion handler-এ দেখবেন: `completion: @escaping (Result<[Note], Error>) -> Void`। প্রায় সব পুরনো plugin code-এ এটা আছে।

**Typed throws (Swift 6.0, ২০২৪):** `throws(NoteError)` লিখলে compiler জানে, শুধু `NoteError`-ই আসতে পারে। সাধারণ `throws` মানে যেকোনো `Error` আসতে পারে। App code-এ বেশিরভাগ সময় সাধারণ `throws`-ই ঠিক। Typed throws কাজে লাগে ছোট আর বন্ধ জায়গায়, যেখানে error-এর তালিকা আগে থেকে জানা — যেমন validation।

| Dart | Swift | Kotlin |
|---|---|---|
| যেকোনো function throw করতে পারে | শুধু `throws` লেখা function | যেকোনো function (unchecked) |
| `try { } catch (e) { }` | `do { try ... } catch { }` | `try { } catch (e: Exception) { }` |
| `on SocketException` | `catch NoteError.offline`, `catch let e as URLError` | `catch (e: IOException)` |
| `rethrow` | `catch`-এর ভেতরে `throw error` | `throw e` |
| (নেই) | `try?` → optional | `runCatching { }.getOrNull()` |

**ভেতরে কীভাবে কাজ করে:** অনেক ভাষায় throw করলে call stack উল্টো দিকে খুলে খুলে catch খোঁজা হয় (stack unwinding)। Swift এভাবে কাজ করে না। `throws` function আসলে একটা লুকানো return-এর পথ দিয়ে error ফেরত দেয়। তাই throw করা সস্তা। আর `try` না লিখে call করলে compiler আটকে দেয়।

**ফাঁদ:** `try?` দিয়ে সব error চুপ করিয়ে দেওয়া। ধরুন save ব্যর্থ হলো, কিন্তু user জানল না। Note-টা হারিয়ে গেল। যেখানে data save হচ্ছে, সেখানে `do/catch` দিন আর user-কে জানান।

[উপরে ফিরুন](#toc)

### <a id="ios1-10"></a>iOS ১.১০ Collection

**এক লাইনে:** `List` → `Array`, `Map` → `Dictionary`, `Set` → `Set`। তিনটাই struct, মানে value type। Assign করলে copy হয় (copy-on-write দিয়ে, তাই সস্তা)।

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
| `..sort((a,b) => ...)` | `.sort(by:)` (নিজেকেই বদলায়) / `.sorted(by:)` (নতুন array দেয়) | `.sortBy` / `.sortedBy` |
| `groupBy` (collection pkg) | `Dictionary(grouping: notes, by: \.isPinned)` | `.groupBy {}` |
| `map[key]` → nullable | `dict[key]` → optional | `map[key]` → nullable |

**Mutable আর immutable-এর জন্য আলাদা type নেই।** Kotlin-এ `List` আর `MutableList` আলাদা type। Swift-এ `let notes` হলে বদলানো যায় না, `var notes` হলে যায়। এটুকুই।

**ফাঁদ — index দিয়ে পড়তে গেলে crash:** ধরুন array-এ ৫টার কম item আছে, আর আপনি `notes[5]` পড়লেন। App সাথে সাথে crash করবে — exception আসবে না। Dart-এ `RangeError` ধরা যেত। Swift-এ এটা ধরার কোনো উপায় নেই। তাই `notes.first`, `notes.last` ব্যবহার করুন (এরা optional দেয়)। অথবা আগে `indices.contains(i)` দিয়ে check করুন।

**ফাঁদ — Dictionary-র কোনো ক্রম নেই।** `[UUID: Note]`-এ item-গুলো কোন ক্রমে আসবে, আগে থেকে বলা যায় না। যে ক্রমে insert করেছেন, সেই ক্রম থাকে না। Insert বা remove করার পরে, বা app আবার চালালে, ক্রম বদলে যেতে পারে। Dart-এর `Map` (LinkedHashMap) insert-এর ক্রম মনে রাখে। Swift-এর Dictionary রাখে না। ক্রম লাগলে আলাদা একটা array রাখুন, অথবা sort করে নিন।

[উপরে ফিরুন](#toc)

### <a id="ios1-11"></a>iOS ১.১১ Access control

**এক লাইনে:** Dart-এ মাত্র দুই রকম আছে — public, আর `_` দিয়ে library-private। Swift-এ ছয়টা keyword আছে। Default হলো `internal`: পুরো module দেখতে পায়, module-এর বাইরে কেউ না।

| Swift | কে দেখতে পায় | Dart-এ কাছাকাছি | Kotlin |
|---|---|---|---|
| `private` | শুধু এই `{ }`-এর ভেতরে (আর একই file-এ এই type-এর extension-এ) | `_name` | `private` |
| `fileprivate` | এই file | `_name` (Dart-এ একটা file-ই একটা library) | (নেই) |
| `internal` (default) | এই module (app target, বা একটা package) | (নেই — package-এর `src/`) | `internal` |
| `package` (Swift 5.9+) | একই Swift package-এর সব module | (নেই) | (নেই) |
| `public` | সবাই দেখে, কিন্তু module-এর বাইরে subclass বা override করা যায় না | public | `public` (final class) |
| `open` | সবাই দেখে, আর subclass/override-ও করতে পারে | public | `open` |

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

`private(set)` খুব কাজের জিনিস। Cubit-এ `state` বাইরে থেকে শুধু পড়া যায়, আর ভেতর থেকে `emit` করে বদলানো হয়। এই keyword এক শব্দে ঠিক এই নিয়মটাই দেয়।

**কখন এটা নিয়ে ভাববেন:** App-এর একটা target-এ সবকিছু `internal` থাকলেই চলে। কিন্তু Flutter plugin বা Swift package লিখলে বাইরে থেকে যা ব্যবহার হবে, সেখানে `public` লাগবে। না দিলে "cannot find in scope" error আসবে, যদিও code ঠিকই আছে।

[উপরে ফিরুন](#toc)

### <a id="ios1-12"></a>iOS ১.১২ Objective-C-র সাথে (চিনে রাখুন)

Swift এসেছে ২০১৪ সালে। তার আগে iOS-এর ভাষা ছিল Objective-C। UIKit-এর ভেতরের অনেকটা এখনো Objective-C-তে লেখা। অনেক পুরনো Flutter plugin-ও এখনো Objective-C-তে। সেখানে `.h` আর `.m` file দেখবেন।

```objc
// Objective-C — চেনার জন্য
@interface NotesPlugin : NSObject<FlutterPlugin>
@end

[channel invokeMethod:@"noteSaved" arguments:@{@"id": noteId}];
```

- **Swift থেকে Objective-C ব্যবহার করা:** দুটো একই target-এ থাকলে **bridging header** file-এ `#import` লিখুন। Flutter-এর `ios/Runner/Runner-Bridging-Header.h` ঠিক এই file। এর ভেতরে আছে `#import "GeneratedPluginRegistrant.h"`। তাই Swift-এ লেখা `AppDelegate` Objective-C-র plugin registrant দেখতে পায়।
- **Objective-C থেকে Swift দেখা:** Swift class-এ `@objc` লিখতে হয়, অথবা class-টাকে `NSObject` থেকে inherit করতে হয়। Flutter template-এ `@objc class AppDelegate` লেখা থাকে এজন্যই।
- **নতুন code Swift-এ লিখুন।** Objective-C পড়ে বুঝতে পারলেই যথেষ্ট।

> **মনে রাখুন**
> - `let`/`var`। Optional খুলতে `if let` আর `guard let`। `!` দিলে nil পেলে crash।
> - Model হলো `struct` — value type, assign করলে copy হয়। Memberwise init, `Equatable`, `Codable` বাড়তি কিছু না লিখেই পাওয়া যায়।
> - GC নেই, ARC আছে। Class-এ রাখা closure `self` ধরলে `[weak self]` দিন।
> - Associated value-ওয়ালা `enum` আর exhaustive `switch` মিলে Dart-এর sealed class-এর কাজ করে।
> - কোন function error ছোঁড়ে, তা signature-এ লেখা থাকে (`throws`)। Call করতে `try` লাগে।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Swift-এ আমি model struct দিয়ে লিখি। কারণ struct value type — copy হয়, তাই কেউ ভাগ করে বদলাতে পারে না। আর `Codable`, `Hashable` compiler নিজেই বানিয়ে দেয়। Identity লাগলে, যেমন store বা screen model, তখন final class নিই। Swift-এ GC নেই, ARC আছে। তাই escaping closure `self` ধরলে `[weak self]` দিই। আর state বোঝাতে associated value-ওয়ালা enum নিই। তাহলে exhaustive switch অসম্ভব অবস্থা আটকে দেয়।"
> - *English:* "In Swift I write models as structs, because they're value types — they copy, there's no shared mutable state, and the compiler gives me `Codable` and `Hashable` for free. When I need identity, like a store or a screen model, I use a final class. Swift has ARC, not a garbage collector, so I use `[weak self]` when an escaping closure captures self. And I model state with enums with associated values, so exhaustive switches rule out impossible states."

[উপরে ফিরুন](#toc)

---

## <a id="ios2"></a>iOS ২. Async — Future, Stream, Isolate থেকে async/await, actor আর AsyncSequence

শুরু করি একটা সুখবর দিয়ে। Swift-এর `async`/`await` দেখতে প্রায় Dart-এর মতোই। `Future<List<Note>>`-এর জায়গায় লিখবেন `async throws -> [Note]`। আর `await` বসে একই জায়গায়।

কিন্তু ভেতরে ব্যাপারটা আলাদা। Dart-এ আপনার সব code এক thread-এ চলত। Swift-এ অনেকগুলো thread চলে, আর তারা একই memory ভাগ করে ব্যবহার করে। তাই Swift-এ দুইটা নতুন প্রশ্ন আসে:
- **কোন code কোন thread-এ চলছে?**
- **একই data কি দুইটা thread একসাথে ছুঁচ্ছে?**

Swift 6-এর পুরো concurrency system এই দুই প্রশ্নের উত্তর দেয় compile-time-এই, মানে app চালানোর আগেই।

Android অংশে coroutine পড়া থাকলে ([অধ্যায় ২](#ch2)) অনেক কিছুই চেনা লাগবে। অধ্যায়ের শেষে একটা table-এ সব তুলনা আছে।

### <a id="ios2-1"></a>iOS ২.১ সবচেয়ে বড় পার্থক্য: thread আর data race

**এক লাইনে:** Dart-এ isolate-রা memory ভাগ করে না, তাই data race হতেই পারে না। Swift-এ thread-রা memory ভাগ করে, তাই data race হতে পারে। তবে Swift 6 compiler build-এর সময়েই সেটা ধরে ফেলে।

**Flutter-এ আপনি যেভাবে ভাবেন:**
- একটা isolate, একটা thread, একটা event loop।
- `await` মানে "এই কাজটা পরে চালাও"। কিন্তু চলবে একই thread-এ।
- ভারী কাজ পাঠান অন্য isolate-এ (`Isolate.run`)। প্রতিটা isolate-এর memory আলাদা, তাদের মধ্যে শুধু message যায়। তাই দুইজন একই variable একসাথে বদলাতে পারে না।

**iOS-এ:**
- **Main thread** — UI-র সব কাজ শুধু এখানে। Flutter-এর UI isolate-এর মতো।
- **Cooperative thread pool** — কয়েকটা thread-এর একটা দল। CPU-তে যত core, thread-ও প্রায় তত। `async` কাজগুলো এখানে চলে।
- সব thread একই memory দেখে। দুইটা thread একসাথে একটা `[Note]` বদলালে data নষ্ট হতে পারে, বা app crash করতে পারে। একেই বলে **data race**।

```
Dart:                               Swift:
┌──────────── isolate ───────────┐  ┌────────────── এক process, ভাগ করা memory ─────────────┐
│ main thread: UI + আপনার code   │  │ main thread (@MainActor) ── UI, screen model          │
│ event loop, await = পরে চালাও   │  │ thread pool ─┬─ async কাজ ১                            │
└────────────────────────────────┘  │              ├─ async কাজ ২   ← একই [Note] ছুঁলে বিপদ  │
┌──── আরেক isolate (আলাদা memory)┐  │              └─ actor NoteCache — এক সময়ে এক জন       │
└────────────────────────────────┘  └───────────────────────────────────────────────────────┘
```

**Swift-এর সমাধান — তিনটা জিনিস:**

| হাতিয়ার | কাজ | পরে বিস্তারিত |
|---|---|---|
| `@MainActor` | "এই code শুধু main thread-এ চলবে" | [iOS ২.৬](#ios2-6) |
| `actor` | "এই data এক সময়ে মাত্র একজন ছুঁতে পারবে" | [iOS ২.৫](#ios2-5) |
| `Sendable` | "এই value অন্য thread-এ পাঠালে কোনো সমস্যা হবে না" | [iOS ২.৭](#ios2-7) |

Swift 6 language mode-এ compiler এই তিনটা নিয়ম মিলিয়ে দেখে। কোনো নিয়ম ভাঙলে build-ই হবে না। Kotlin-এ coroutine-এর data race ঠেকানো পুরোটাই আপনার কাজ, compiler সাহায্য করে না। Swift-এ compiler নিজেই এটা check করে।

[উপরে ফিরুন](#toc)

### <a id="ios2-2"></a>iOS ২.২ `Future` → `async`/`await`

**এক লাইনে:** যে function `Future<T>` return করত, Swift-এ সেটা হয় `async -> T`। Error ছুঁড়তে পারলে `async throws -> T`। Call করার সময় লিখবেন `try await`।

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

**ভেতরে কীভাবে কাজ করে:** `await` হলো একটা **suspension point**, মানে থামার জায়গা। এখানে function থেমে যায়, আর thread-টা ছেড়ে দেয় যাতে অন্য কাজ চলতে পারে। Thread বসে বসে অপেক্ষা করে না — ঠিক Dart-এর মতো। Kotlin-এর `suspend`-এর মতোই compiler function-টাকে কয়েকটা টুকরোয় ভাগ করে নেয়।

**কী আলাদা — `await`-এর পরে কোন thread-এ ফিরবে?** Dart-এ `await`-এর পরেও আপনি একই isolate-এ থাকেন। Swift-এ নির্ভর করে function-টা কার:
- Function `@MainActor`-এর হলে `await`-এর পরে আবার main thread-এ ফেরে।
- Function কোনো `actor`-এর ভেতরে হলে আবার সেই actor-এ ফেরে।
- কোনো actor-এর না হলে যেকোনো thread-এ ফিরতে পারে।

তাই "আমি এখন কোন thread-এ?" — এই প্রশ্নের উত্তর thread-এর নাম দেখে পাওয়া যায় না। উত্তর পাওয়া যায় function-টা কোন actor-এর, সেটা দেখে। একে বলে **isolation**।

**ফাঁদ:** ধরে নেওয়া যে `await`-এর আগে আর পরে অবস্থা একই থাকবে। মাঝের সময়টায় অন্য কাজ চলতে পারে, আর ভাগ করা state বদলে যেতে পারে। এর নাম reentrancy ([iOS ২.৫](#ios2-5))।

[উপরে ফিরুন](#toc)

### <a id="ios2-3"></a>iOS ২.৩ কাজ চালু করা: `Task` আর task group

**এক লাইনে:** সাধারণ (async না এমন) জায়গা থেকে async কাজ শুরু করতে লাগে `Task { }`। অনেকগুলো কাজ একসাথে চালাতে লাগে **task group**।

**Flutter-এ:** Button-এর `onPressed` থেকে সরাসরি async function call করতেন। Future-টা ধরে না রাখলেও কোনো সমস্যা হতো না:

```dart
onPressed: () => cubit.sync(),     // Future ফেরত দেয়, কেউ await করে না
```

**Swift-এ:** যে জায়গা async না, সেখানে `await` লেখা যায় না। তাই `Task` দিয়ে একটা নতুন async কাজ খুলতে হয়, যার ভেতরে await লেখা চলে:

```swift
Button("Sync") {
    Task {
        await model.sync()          // Task-এর ভেতরে await চলে
    }
}
```

SwiftUI-তে screen খোলার সময় কাজ শুরু করার আরও ভালো উপায় হলো `.task` modifier। Screen চলে গেলে এটা নিজেই কাজটা cancel করে দেয় ([iOS ৫.৯](#ios5-9))।

**Task তিন রকম:**

| | কী | Parent cancel হলে এটাও cancel হয়? | যেখানে বানানো, সেই actor (thread) পায়? | কখন |
|---|---|---|---|---|
| `async let`, task group-এর child | **structured** — parent-এর সাথে বাঁধা | হ্যাঁ | না, আলাদা চলে | কয়েকটা কাজ একসাথে |
| `Task { }` | **unstructured** — নিজে স্বাধীন | না | হ্যাঁ, যেখানে বানানো সেখানকার | sync জায়গা থেকে async শুরু করতে |
| `Task.detached { }` | পুরোপুরি স্বাধীন | না | না | প্রায় কখনোই না |

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

- Group থেকে কোনো error বের হয়ে গেলে বাকি child task-গুলো **নিজে থেকেই cancel** হয়।
- Group-এর `{ }` শেষ হওয়ার আগে সব child অবশ্যই শেষ হয়। কোনো কাজ পেছনে "হারিয়ে" যায় না। এই নিয়মকেই বলে **structured concurrency**।
- ফলগুলো একটা একটা করে নিতে চাইলে: `for try await result in group { ... }`।

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

Flutter-এ এই কাজ আপনি `Timer` আর `CancelableOperation` দিয়ে করতেন। অথবা RxDart-এর `debounceTime` + `switchMap` দিয়ে।

**ফাঁদ:** `Task { }` কোনো scope-এর সাথে বাঁধা না। Screen বন্ধ হয়ে গেলেও এটা চলতে থাকে, যতক্ষণ না নিজে শেষ হয়। লম্বা কাজ হলে handle রেখে দিন আর দরকারে `cancel()` করুন। অথবা `.task` modifier ব্যবহার করুন।

[উপরে ফিরুন](#toc)

### <a id="ios2-4"></a>iOS ২.৪ Cancellation

**এক লাইনে:** Swift-এ cancel করা মানে task-এর গায়ে একটা flag লাগিয়ে দেওয়া। Task নিজে সেই flag দেখে থামে। কেউ জোর করে task-কে মেরে ফেলে না। Kotlin coroutine-এর মতোই এটা cooperative — task-কে নিজে সহযোগিতা করতে হয়।

**Flutter-এ:** Dart-এর `Future` cancel করা যায় না। তাই আপনি `StreamSubscription.cancel()`, dio-র `CancelToken`, বা একটা `bool _disposed` দিয়ে কাজ চালাতেন।

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

**যারা নিজে থেকেই থামে:**
- `Task.sleep` — cancel হলে সাথে সাথে `CancellationError` ছোঁড়ে।
- `URLSession`-এর async API — cancel হলে request বন্ধ করে error ছোঁড়ে।
- Parent cancel হলে তার সব structured child-ও cancel হয় (`async let`, task group)।
- SwiftUI-র `.task` modifier — screen চলে গেলে cancel করে।

**যারা নিজে থামে না:** আপনার নিজের লেখা লম্বা loop বা হিসাব। সেখানে মাঝে মাঝে নিজেই `Task.isCancelled` বা `try Task.checkCancellation()` দিয়ে check করুন।

| Dart | Swift | Kotlin |
|---|---|---|
| (Future cancel হয় না) | `task.cancel()` | `job.cancel()` |
| `_disposed` flag | `Task.isCancelled` | `isActive` |
| (নেই) | `try Task.checkCancellation()` | `ensureActive()` |
| (নেই) | `CancellationError` | `CancellationException` |
| `subscription.cancel()` | `for await` loop যে task-এ চলছে, তাকে cancel | `collect`-এর job cancel |

**ফাঁদ:** `catch`-এ সব error একসাথে ধরে "কিছু ভুল হয়েছে" দেখানো। তখন cancel-ও error হিসেবে ধরা পড়ে, আর user অকারণে error message দেখে। তাই সবার আগে `catch is CancellationError { return }` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios2-5"></a>iOS ২.৫ `actor` — এক সময়ে একজন

**এক লাইনে:** `actor` দেখতে class-এর মতো। পার্থক্য হলো, তার ভেতরের data এক সময়ে মাত্র একটা কাজ ছুঁতে পারে। বাইরে থেকে actor-এর কিছু ডাকতে `await` লাগে, কারণ actor তখন অন্য কাজে ব্যস্ত থাকলে অপেক্ষা করতে হতে পারে।

**Flutter-এ:** এরকম কিছু লাগেনি। এক isolate-এ সব code একটার পর একটা চলে। আর দুই isolate-এর memory আলাদা।

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

Actor-এর ভেতরের code `notes` ছুঁতে `await` লেখে না, কারণ সে তো ইতিমধ্যে actor-এর ভেতরেই চলছে, অন্য কেউ তখন data ছুঁতে পারে না। বাইরে থেকে ছুঁতে লাগে।

**ভেতরে কীভাবে কাজ করে:**
- প্রতিটা actor-এর নিজের একটা queue আছে, যেটা একবারে একটাই কাজ চালায়। একে serial executor বলে।
- বাইরের সব call সেই queue-তে জমা হয়, আর একটার পর একটা চলে।
- অপেক্ষার সময় thread আটকে থাকে না। অপেক্ষা হয় `await`-এ।
- পুরনো iOS code-এ এই কাজটা হাতে করা হতো, serial `DispatchQueue` দিয়ে।

**Dart-এর isolate-এর সাথে তুলনা:**

| | Dart isolate | Swift actor |
|---|---|---|
| Memory | আলাদা heap | একই heap, কিন্তু data actor-এর ভেতরে বন্ধ থাকে |
| কথা বলা | message পাঠিয়ে (copy হয়) | `await` দিয়ে method call |
| খরচ | ভারী — নতুন isolate বানাতে সময় লাগে | হালকা — একটা সাধারণ object |
| কাজ | ভারী হিসাব অন্য core-এ চালানো | ভাগ করা mutable state রক্ষা করা |

**ফাঁদ — reentrancy।** Actor-এর ভেতরে কোনো method `await`-এ থামলে, সেই ফাঁকে actor অন্য call নিতে পারে। একে reentrancy বলে। তাই `await`-এর পরে actor-এর state আগের মতো না-ও থাকতে পারে:

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

সমাধান: যে কাজটা এখন চলছে, সেটাকেই রেখে দিন। তাহলে দ্বিতীয় call নতুন কাজ শুরু না করে, আগের কাজটার জন্যই অপেক্ষা করবে:

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

Interview-এ actor নিয়ে প্রশ্ন এলে reentrancy-র কথা বলুন। এতে senior-এর মতো শোনায়।

**Best approach:** Repository-র cache, token store, download manager — যেখানে অনেক জায়গা থেকে একই mutable data ছোঁয়া হয়, সেখানে actor নিন। UI-র state actor-এ রাখবেন না। সেটা রাখুন `@MainActor`-এ।

[উপরে ফিরুন](#toc)

### <a id="ios2-6"></a>iOS ২.৬ `@MainActor` — UI-র thread

**এক লাইনে:** `@MainActor` একটা বিশেষ actor, যেটা পুরো app-এ একটাই (global actor)। এর সব কাজ চলে main thread-এ। কোনো class বা function-এ এটা লিখলে সেটা শুধু main thread-এ চলবে। আর compiler সেটা নিশ্চিত করবে।

**Flutter-এ:** সব Dart code UI isolate-এ চলে। তাই "UI কোন thread থেকে update হচ্ছে" — এটা নিয়ে কখনো ভাবতে হয়নি।

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

- SwiftUI-র `View` protocol নিজেই `@MainActor` (Xcode 16 / iOS 18 SDK থেকে)। তাই view-এর body, আর তার ভেতরের `Task { }`, main thread-এ চলে।
- Screen model-কে `@MainActor` দিলে UI-র সব state main thread-এ থাকে। ঠিক যেমন Cubit UI isolate-এ থাকত।
- `repository.allNotes()` যদি অন্য কোনো actor-এর হয়, বা `@concurrent` হয়, তাহলে network আর decoding main thread-এর বাইরে চলে। `await`-এর পরে আবার main-এ ফেরে।

**পুরনো code-এ যা দেখবেন:**

```swift
await MainActor.run { self.notes = notes }        // actor-যুগের শুরুর দিকের ধরন
DispatchQueue.main.async { self.notes = notes }   // GCD যুগ — প্রায় সব পুরনো plugin-এ
```

**ফাঁদ:** main thread-এ ভারী কাজ করা — বড় JSON decode, ছবি resize, হাজার note sort। এতে UI আটকে যায়। Flutter-এ UI isolate-এ ভারী কাজ করলে যা হয়, ঠিক তাই। এগুলো `@concurrent` function-এ পাঠান ([iOS ২.৭](#ios2-7))।

[উপরে ফিরুন](#toc)

### <a id="ios2-7"></a>iOS ২.৭ `Sendable` আর Swift 6 strict concurrency

**এক লাইনে:** `Sendable` মানে "এই value এক actor থেকে আরেক actor-এ পাঠালে data race হবে না।" Swift 6 language mode-এ compiler প্রতিটা পাঠানো value check করে।

**কোনটা Sendable:**

| Type | Sendable? |
|---|---|
| `Int`, `String`, `Date`, `UUID` | হ্যাঁ |
| struct/enum, যার সব property Sendable | হ্যাঁ (module-এর ভেতরে compiler নিজেই বুঝে নেয়; `public` type-এ নিজে লিখে দিতে হয়) |
| `actor` | হ্যাঁ — ভেতরের data সে নিজেই রক্ষা করে |
| `@MainActor` class | হ্যাঁ — তার সব কাজ main thread-এ হয় |
| `final class`, যার সব property `let` আর Sendable | হ্যাঁ, যদি `: Sendable` লিখে দেন |
| সাধারণ class, যার `var` property আছে | না |

Dart-এর সাথে তুলনা: এক isolate থেকে আরেক isolate-এ message পাঠালে Dart value copy করে দেয়। তাই সব নিরাপদ। Swift copy করে না। তাই সে জানতে চায়, এই value ভাগ করা নিরাপদ কি না।

**Swift 6 language mode — কী বদলায়:**
- Swift 5 mode-এ এই check-গুলো শুধু warning দেয় (বা বন্ধ থাকে)।
- Swift 6 mode-এ (Swift 6.0, সেপ্টেম্বর ২০২৪) data race হওয়ার সম্ভাবনা থাকলেই **compile error**।
- পুরো project একবারে Swift 6-এ নিতে হয় না। একটা একটা target করে নেওয়া যায়। আগে Swift 5 mode-এই "Strict Concurrency Checking = Complete" চালু করুন। Warning-গুলো দেখে ঠিক করুন। তারপর mode বদলান।

Flutter-এর `ios/Runner` এখনো Swift 5 language mode-এ চলে (template-এ `SWIFT_VERSION = 5.0`)। তাই Runner-এ এই error দেখবেন না। কিন্তু native project বা plugin-এ দেখবেন।

**Swift 6.2 — "approachable concurrency" (Xcode 26, সেপ্টেম্বর ২০২৫):** Swift 6 শুরুতে অনেক error দিত, আর মানুষ বিরক্ত হতো। তাই Swift 6.2 তিনটা বদল আনল, যাতে সাধারণ app code লেখা সহজ হয়:

1. **Default actor isolation = `MainActor`।** Target-এর build setting-এ এটা চালু করলে, যে code-এ কোনো actor লেখা নেই, সেটাকে `@MainActor` ধরা হয়। মানে app নিজে থেকে single-threaded থাকে, Dart-এর মতো। Xcode 26-এ নতুন app project এভাবেই তৈরি হয়।
2. **`nonisolated async` function যে ডাকে, তার জায়গাতেই চলে।** আগে এমন function সবসময় background thread-এ চলে যেত। এখন upcoming feature `NonisolatedNonsendingByDefault` চালু থাকলে, caller যে actor-এ আছে, function-ও সেখানেই চলে। এতে অকারণে thread বদল কমে, Sendable error-ও কমে।
3. **`@concurrent`** — "এই কাজটা সত্যিই background-এ চালাও", এটা পরিষ্কার করে বলার উপায়।

এই setting-গুলো পাবেন Build Settings → **Swift Compiler – Concurrency**-তে (Default Actor Isolation, Approachable Concurrency)। পুরনো project-এ এগুলো নিজে থেকে বদলায় না। নতুন project খুললে একবার দেখে নিন, কোনটা চালু আছে।

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

`@concurrent` শুধু `async` function-এ বসে। এটা function-টাকে `nonisolated` করে দেয়, মানে কোনো actor-এর না। `Data` আর `[Note]` দুটোই Sendable, তাই compiler কোনো আপত্তি করে না। Dart-এর `Isolate.run`-এর চেয়ে এটা অনেক সস্তা — নতুন isolate বানাতে হয় না, data copy-ও হয় না।

**ফাঁদ — default `MainActor` দিলে model-ও main-এর হয়ে যায়।** Default isolation `MainActor` দিলে `struct Note`-কেও `@MainActor` ধরা হয়। তার `Codable` conformance-ও main-এর হয়ে যেতে পারে। তখন `@concurrent` function-এ `Note` decode করতে গেলে compiler error দেয়। সমাধান: যে type শুধু data রাখে, তাকে লিখুন `nonisolated struct Note: Codable, Sendable { ... }`। Model কোনো thread-এর না — সে শুধু data।

**ফাঁদ — error চুপ করাতে `@unchecked Sendable` বা `nonisolated(unsafe)` লেখা।** এরা compiler-কে বলে, "দায়িত্ব আমার, তুমি check কোরো না।" কিন্তু ভেতরে lock না থাকলে data race থেকেই যায়। Error এলে আগে ভাবুন, এই data কার?
- Main thread-এর হলে → `@MainActor`।
- অনেকে মিলে ব্যবহার করলে → `actor`।
- শুধু পড়ার জন্য হলে → `struct`।

[উপরে ফিরুন](#toc)

### <a id="ios2-8"></a>iOS ২.৮ `Stream` → `AsyncSequence` আর `AsyncStream`

**এক লাইনে:** Dart-এর `Stream` হলো Swift-এর `AsyncSequence`। `await for` হয় `for await`। আর নিজে value পাঠানোর জন্য `StreamController`-এর বদলে আছে `AsyncStream`।

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

যে stream error ছুঁড়তে পারে, তার জন্য `AsyncThrowingStream` নিন। তখন loop লিখবেন `for try await`।

**Apple-এর অনেক API আগে থেকেই AsyncSequence দেয়:**

```swift
// file-এর লাইন একটা একটা করে
for try await line in fileURL.lines { ... }

// system notification
for await _ in NotificationCenter.default.notifications(named: UIApplication.didReceiveMemoryWarningNotification) {
    cache.removeAll()
}
```

**Operator:** `map`, `filter`, `compactMap`, `prefix` standard library-তেই আছে। কিন্তু `debounce`, `throttle`, `merge`, `combineLatest` আছে Apple-এর open-source package **swift-async-algorithms**-এ। এটা RxDart-এর মতো একটা আলাদা dependency।

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
| `StreamSubscription.cancel()` | loop যে task-এ চলছে, তাকে cancel | collect-এর job cancel |
| broadcast stream | (built-in নেই — নিজে বানাতে হয়) | `SharedFlow` |

**কী আলাদা:**
- **Cancel করার উপায়।** Dart-এ subscription cancel করেন। Swift-এ `for await` loop যে task-এর ভেতরে চলছে, সেই task cancel করেন। SwiftUI-র `.task`-এর ভেতরে loop চালালে screen চলে গেলে loop নিজেই থেমে যায়।
- **`AsyncStream` একজনের জন্য।** একই stream দুই জায়গা থেকে পড়বেন না। তাহলে দুইজনই সব value পাবে না, কারণ এটা broadcast না। এটা Dart-এর single-subscription stream-এর কাছাকাছি।

**UI state-এর জন্য stream ব্যবহার করবেন না।** Flutter-এ `StreamBuilder` দিয়ে UI বানাতেন। SwiftUI-তে screen-এর state রাখার উপায় হলো `@Observable` ([iOS ৫.৭](#ios5-7))। Stream কাজে লাগে একটার পর একটা ঘটনা আসার ক্ষেত্রে: sync-এর progress, database-এর বদল, socket-এর message।

**ফাঁদ:** `onTermination` না দেওয়া। তখন consumer চলে গেলেও পুরনো callback-এর observer চলতেই থাকে। এটা leak — Flutter-এ `StreamController`-এর `onCancel`-এ cleanup না করলে যেমন হয়।

[উপরে ফিরুন](#toc)

### <a id="ios2-9"></a>iOS ২.৯ চিনে রাখুন: GCD, completion handler আর Combine

নতুন code-এ এগুলো লিখবেন না। কিন্তু প্রায় প্রতিটা Flutter plugin-এর iOS অংশে, আর পুরনো project-এ, এগুলোই দেখবেন।

**GCD (Grand Central Dispatch) — `DispatchQueue`:**

```swift
DispatchQueue.global(qos: .userInitiated).async {
    let notes = parse(data)                       // background thread
    DispatchQueue.main.async {
        self.notes = notes                        // UI-র কাজ main-এ
    }
}
```

`async`/`await` আসার আগে iOS-এ thread বদলানোর একমাত্র সহজ উপায় ছিল এটা। Compiler কিছুই check করত না। ভুল thread থেকে UI ছুঁলে কখনো crash হতো, কখনো অদ্ভুত bug।

**Completion handler → async — নিজের wrapper:**

Plugin লেখার সময় প্রায়ই পুরনো callback API-কে async বানাতে হবে। এখানে continuation সেই কাজ করে, যা Dart-এ `Completer` করে:

```swift
func fetchNotes() async throws -> [Note] {
    try await withCheckedThrowingContinuation { continuation in
        legacyClient.fetchNotes { result in        // পুরনো API: (Result<[Note], Error>) -> Void
            continuation.resume(with: result)       // ঠিক একবার resume করতে হবে
        }
    }
}
```

**ফাঁদ:** continuation **ঠিক একবার** resume করতে হবে।
- দুইবার করলে crash।
- একবারও না করলে task চিরকাল ঝুলে থাকে। (Checked continuation তখন console-এ সতর্ক করে।)

Dart-এ `Completer` দুইবার complete করলে যেমন error হয়, এটাও তেমন।

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

iOS 13–16-এ SwiftUI-র state রাখা হতো `@Published` + `ObservableObject` দিয়ে। আজ তার জায়গায় এসেছে `@Observable` আর async/await। Combine বাদ হয়ে যায়নি, কিন্তু নতুন code-এ এটা কম লাগে।

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

Android অংশ পড়া থাকলে এই একটা table-এ সব মিলিয়ে নিতে পারবেন:

| কাজ | Dart | Swift | Kotlin |
|---|---|---|---|
| Async function | `Future<T> f() async` | `func f() async -> T` | `suspend fun f(): T` |
| Sync জায়গা থেকে শুরু | সরাসরি call | `Task { }` | `scope.launch { }` |
| Screen যতক্ষণ আছে, ততক্ষণ চলা কাজ | `dispose`-এ cancel | `.task { }` modifier | `viewModelScope`, `LaunchedEffect` |
| কয়েকটা একসাথে | `Future.wait` | `async let`, task group | `async { }` + `awaitAll`, `coroutineScope` |
| UI thread | UI isolate | `@MainActor` | `Dispatchers.Main` |
| Background-এ ভারী কাজ | `Isolate.run` | `@concurrent` function | `withContext(Dispatchers.Default)` |
| Mutable state রক্ষা | (দরকার নেই) | `actor` | `Mutex`, এক thread-এই রাখা (single-thread confinement) |
| Thread-এ পাঠানো নিরাপদ? | সব copy হয় | `Sendable`, compile-time check | compiler check করে না |
| Cancel | (Future-এ নেই) | `task.cancel()`, `Task.isCancelled` | `job.cancel()`, `isActive` |
| Stream | `Stream` | `AsyncSequence` | `Flow` |
| Callback → stream | `StreamController` | `AsyncStream` | `callbackFlow` |
| Callback → একটা value | `Completer` | `withCheckedThrowingContinuation` | `suspendCancellableCoroutine` |
| UI-র observable state | `ValueNotifier`, Cubit | `@Observable` | `StateFlow` |

**Kotlin-এর সাথে সবচেয়ে বড় দুই পার্থক্য:**
- **Scope object নেই।** Kotlin-এ প্রতিটা `launch` একটা `CoroutineScope`-এর সাথে বাঁধা। Swift-এ structured কাজ (`async let`, group) function-এর ভেতরে বাঁধা থাকে। আর screen যতক্ষণ আছে ততক্ষণ কাজ চালানোর ব্যবস্থা দেয় SwiftUI-র `.task`। `Task { }` কোনো scope-এর সাথে বাঁধা না।
- **Data race compiler ধরে।** Kotlin-এ ভুল dispatcher বা ভাগ করা `MutableList` থাকলেও compiler কিছু বলে না। Swift 6-এ build-ই হবে না।

**Best approach (নভেম্বর ২০২৬):**
- নতুন app-এ default actor isolation `MainActor` দিন, আর Swift 6 language mode নিন। তাহলে app নিজে থেকে single-threaded থাকে, Dart-এর মতো সহজ।
- Screen model: `@MainActor @Observable final class`।
- ভারী কাজ (decode, ছবি, বড় sort): `@concurrent` function।
- যে mutable data অনেক জায়গা থেকে ছোঁয়া হয়: `actor`।
- Screen খোলার সময়ের কাজ: `.task { }` modifier, `Task { }` না।
- পুরনো callback API: একবার `withCheckedThrowingContinuation` বা `AsyncStream` দিয়ে মুড়ে নিন। তারপর বাকি সব জায়গায় async ব্যবহার করুন।

> **মনে রাখুন**
> - `Future` → `async`, `Future.wait` → `async let` বা task group, `Stream` → `AsyncSequence`।
> - Swift-এ সত্যিকারের অনেক thread থাকে, আর তারা memory ভাগ করে। `@MainActor`, `actor`, `Sendable` দিয়ে compiler data race আটকায়।
> - Cancel হলো cooperative — task নিজে check করে: `Task.isCancelled` / `checkCancellation()`। `Task { }` নিজে থেকে cancel হয় না।
> - Actor-এ `await`-এর পরে state বদলে যেতে পারে (reentrancy)।
> - Swift 6.2: default `MainActor` isolation, আর background কাজের জন্য পরিষ্কার করে `@concurrent`।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Swift-এর async/await দেখতে Dart-এর মতো। কিন্তু Dart-এ isolate-দের memory আলাদা, আর Swift-এ thread-রা memory ভাগ করে। তাই Swift 6 compiler `Sendable` আর actor isolation দিয়ে build-এর সময়েই data race ধরে। আমি screen model রাখি `@MainActor`-এ, ভাগ করা cache রাখি actor-এ, আর ভারী কাজ দিই `@concurrent` function-এ। Screen-এর কাজ চালাই `.task` modifier দিয়ে, যাতে screen চলে গেলে কাজটা নিজেই cancel হয়।"
> - *English:* "Swift's async/await looks like Dart's, but Dart isolates don't share memory while Swift threads do. So the Swift 6 compiler uses `Sendable` and actor isolation to catch data races at build time. I keep screen models on the `@MainActor`, shared caches in actors, and heavy work in `@concurrent` functions. I start screen work with the `.task` modifier so it cancels itself when the screen goes away."

[উপরে ফিরুন](#toc)

---
## <a id="ios3"></a>iOS ৩. Xcode project — `pubspec.yaml`-এর জায়গায়

Flutter-এ `ios/` folder-এ আপনি খুব কম ঢুকতেন, আর ঢুকতেন একটু ভয়ে ভয়ে। হয়তো signing ঠিক করতে, Info.plist-এ একটা লাইন যোগ করতে, বা `pod install` fail করলে। এখন থেকে এই folder-টাই আপনার আসল কাজের জায়গা। Android-এ এই কাজটা করত Gradle ([অধ্যায় ৩](#ch3))। iOS-এ পুরো কাজটা চলে Xcode project দিয়ে।

শুরুতেই একটা কথা জেনে রাখুন। Xcode project-এর মূল file হলো `project.pbxproj`, আর এটা মানুষের পড়ার মতো করে লেখা না। Gradle file আপনি নিজের হাতে লেখেন। কিন্তু Xcode project আপনি বদলান Xcode-এর UI দিয়ে, আর file-টা Xcode নিজে লেখে। তাই এই অধ্যায়ে code কম। বেশিরভাগ কথা হলো "Xcode-এর কোন জায়গায় কী আছে"।

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

এটা এত ছোট কেন? কারণ দুইটা:
- **Info.plist file নেই।** Xcode 13 থেকে নতুন project-এ Info.plist-এর বেশিরভাগ key রাখা হয় build setting-এ (`INFOPLIST_KEY_...`)। Build-এর সময় Xcode নিজেই file-টা বানিয়ে নেয়। এগুলো দেখতে আর বদলাতে যাবেন Target → Info tab-এ। আপনি নিজের কোনো key (যেমন API URL) যোগ করলে, তখন Xcode একটা আসল file বানিয়ে দেয়।
- **Storyboard নেই।** SwiftUI-র `App` নিজেই window বানায়, তাই storyboard লাগে না।

**Xcode 16 থেকে "folder" বনাম "group":** নতুন project-এ project-এর folder আর disk-এর folder নিজে থেকেই মিলে থাকে। একে synchronized folder বলে। Finder-এ একটা file রাখলেই সেটা project-এ চলে আসে, `project.pbxproj`-এ কোনো লাইন যোগ হয় না। এতে git merge conflict অনেক কমে যায়। পুরনো project-এ (Flutter-এর Runner-ও এর মধ্যে) থাকে "group"। সেখানে নতুন file যোগ করতে হলে Xcode-এ টেনে এনে ছাড়তে হয়।

| Flutter / Android | iOS |
|---|---|
| `pubspec.yaml` + `android/app/build.gradle` | `project.pbxproj` (Xcode UI দিয়ে বদলান) |
| `AndroidManifest.xml` | `Info.plist` + `.entitlements` |
| `res/`, `assets/` | `Assets.xcassets` |
| `MainActivity.kt` | `AppDelegate.swift` / `@main App` |
| `pubspec.lock` | `Package.resolved` (SPM) / `Podfile.lock` |

**ফাঁদ:** CocoaPods থাকলে `.xcodeproj` খুলে build দিলে "module not found" error আসে। তাই সবসময় `.xcworkspace` খুলুন। ওটার ভেতরে আপনার project আর Pods project দুটোই একসাথে থাকে।

[উপরে ফিরুন](#toc)

### <a id="ios3-2"></a>iOS ৩.২ Project, target, scheme, build configuration

**এক লাইনে:** **Target** মানে কী বানাবেন। **Build configuration** মানে কোন setting দিয়ে বানাবেন। **Scheme** মানে কোন বোতাম চাপলে কোন target কোন configuration দিয়ে বানানো হবে।

এই চারটা শব্দ, Android-এর পাশে রেখে:

| Xcode | মানে | Android-এ কাছাকাছি |
|---|---|---|
| **Project** | পুরো জিনিসটা: সব target, সব setting | পুরো Gradle project |
| **Target** | একটা product: app, widget extension, share extension, test bundle | একটা module (`:app`, `:feature`) |
| **Build configuration** | build setting-এর একটা সেট: Debug, Release (Flutter এর সাথে Profile যোগ করে) | build type: `debug`, `release` |
| **Scheme** | Run / Test / Profile / Archive — প্রতিটা কাজে কোন target আর কোন configuration চলবে | Run configuration + build variant বেছে নেওয়া |

**Flutter-এর Runner scheme-এর ভেতরটা এরকম:**

| Action | Configuration | কখন |
|---|---|---|
| Run | Debug | Xcode-এ ▶ চাপলে |
| Test | Debug | ⌘U চাপলে |
| Profile | Profile | Instruments চালালে |
| Archive | Release | App Store-এর জন্য build করলে |

**Build setting কোথা থেকে আসে — স্তরগুলো:**

```
iOS-এর default  →  project-level setting  →  target-এর .xcconfig file  →  target-level setting
(সবচেয়ে দুর্বল)                                                  (সবচেয়ে জোরালো)
```

একই setting কয়েক জায়গায় থাকতে পারে। তখন ডানের স্তরটা জেতে। Xcode-এ target → Build Settings → "Levels" খুললে প্রতিটা setting কোন স্তর থেকে এল, সেটা পাশাপাশি দেখা যায়। কোনো setting ভুল জায়গা থেকে আসছে মনে হলে আগে এখানেই দেখুন।

**কয়েকটা জরুরি build setting:**

| Setting | মানে | Android-এ |
|---|---|---|
| `PRODUCT_BUNDLE_IDENTIFIER` | App-এর পরিচয়, যেমন `com.byteonyx.notes` | `applicationId` |
| `MARKETING_VERSION` | User যে version দেখে: `1.4.0` | `versionName` |
| `CURRENT_PROJECT_VERSION` | Build number: `42` | `versionCode` |
| `IPHONEOS_DEPLOYMENT_TARGET` | সবচেয়ে পুরনো যে iOS-এ app চলবে | `minSdk` |
| `SWIFT_VERSION` | Swift language mode (5 বা 6) | Kotlin `languageVersion` |
| `CODE_SIGN_STYLE`, `DEVELOPMENT_TEAM` | Signing | `signingConfigs` |

Flutter-এ version কীভাবে Xcode-এ পৌঁছায়, দেখুন:
1. আপনি `pubspec.yaml`-এ লেখেন `version: 1.4.0+42`।
2. flutter tool `Generated.xcconfig`-এ লেখে `FLUTTER_BUILD_NAME=1.4.0` আর `FLUTTER_BUILD_NUMBER=42`।
3. Runner-এর Info.plist এগুলো পড়ে নেয়: `CFBundleShortVersionString = $(FLUTTER_BUILD_NAME)`।

তাই Flutter app-এর version বদলাবেন pubspec-এ, Xcode-এ না।

[উপরে ফিরুন](#toc)

### <a id="ios3-3"></a>iOS ৩.৩ `.xcconfig` — build setting একটা text file-এ

**এক লাইনে:** Build setting Xcode-এর UI-তে না রেখে একটা সাধারণ `key = value` text file-এ রাখা। এতে git-এ পড়া যায়, review করা যায়, আর merge conflict কম হয়।

**Flutter-এ এটা আপনি আগেই দেখেছেন:**

```
// ios/Flutter/Debug.xcconfig
#include "Generated.xcconfig"
```

CocoaPods থাকলে flutter tool এখানে আরও একটা লাইন যোগ করে: `#include? "Pods/Target Support Files/Pods-Runner/Pods-Runner.debug.xcconfig"`।

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

এরপর Project → Info → Configurations-এ যান। সেখানে প্রতিটা configuration-এর পাশে কোন xcconfig file চলবে, সেটা বেছে দিন।

**Code থেকে value পড়া — Info.plist-এর মধ্য দিয়ে:**

```xml
<!-- Info.plist -->
<key>APIHost</key>
<string>$(API_HOST)</string>
```

```swift
let host = Bundle.main.object(forInfoDictionaryKey: "APIHost") as? String ?? ""
let baseURL = URL(string: "https://\(host)")!
```

এটা Flutter-এর `--dart-define`-এর মতো কাজ। পার্থক্য শুধু, এটা native দিকে হয়।

**ফাঁদ — xcconfig-এ `//` মানে comment।** xcconfig-এ `API_URL = https://api.byteonyx.com` লিখলে `//`-এর পরের সবকিছু comment হয়ে যায়। Value থাকে শুধু `https:`। এজন্যই ওপরে file-এ শুধু host রেখেছি, আর `https://` লিখেছি code-এ। পুরো URL রাখতেই হলে একটা পুরনো কৌশল আছে। মাঝখানে একটা খালি variable বসিয়ে দিন: `https:/$()/api.byteonyx.com`।

**ফাঁদ — secret xcconfig-এ রাখবেন না।** xcconfig-এর value Info.plist হয়ে app-এর ভেতরে খোলা text হিসেবে চলে যায়। যে কেউ `.ipa` খুলে সেটা পড়তে পারে। API key-এর মতো secret app-এর ভেতরে লুকানোর কোনো উপায় নেই। ওটা server-এ রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ios3-4"></a>iOS ৩.৪ Flavor = scheme + configuration

**এক লাইনে:** Android-এ flavor একটা আলাদা জিনিস (`productFlavors`)। iOS-এ "flavor" নামে কিছু নেই। একই কাজ হয় দুইটা জিনিস মিলিয়ে: প্রতিটা flavor-এর জন্য **একটা scheme**, আর তার সাথে **কয়েকটা build configuration**।

**Flutter-এ আপনি যেভাবে চালান:**

```bash
flutter run --flavor dev
flutter build ipa --flavor prod
```

`--flavor dev` দিলে flutter tool Xcode-এ **`dev` নামের scheme** খোঁজে। সেই scheme-এর configuration-গুলোর নামও ঠিক এরকম হতে হয়: `Debug-dev`, `Release-dev`, `Profile-dev`। নাম না মিললে build fail করে।

**Xcode-এ ধাপগুলো (একবারই করতে হয়):**

1. Project → Info → Configurations-এ যান। Debug, Release, Profile duplicate করে নাম দিন: `Debug-dev`, `Release-dev`, `Profile-dev`, `Debug-prod`, `Release-prod`, `Profile-prod`।
2. প্রতিটা configuration-এ ঠিক xcconfig বসান (Dev বা Prod)।
3. Product → Scheme → New Scheme দিয়ে দুইটা scheme বানান: `dev` আর `prod`। প্রতিটা scheme-এর Run, Test, Profile, Archive-এ তার নিজের configuration বেছে দিন।
4. Scheme-গুলো **Shared** করুন (Manage Schemes → Shared)। Flutter docs বলে, shared না করলে flavor ঠিকমতো কাজ করে না। তাছাড়া shared না হলে scheme git-এ যায় না, ফলে CI বা আপনার সহকর্মী scheme-টা পাবে না।
5. Flavor-এর নাম ছোট হাতের অক্ষরে রাখুন (`dev`, `prod`)। নইলে Flutter CLI চিনতে পারে না।

Dart code থেকে কোন flavor চলছে জানতে চাইলে `appFlavor` (`package:flutter/services.dart`) ব্যবহার করুন। এটা scheme-এর নামটা দেয়।

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
| `applicationIdSuffix ".dev"` | xcconfig-এ `PRODUCT_BUNDLE_IDENTIFIER` |
| `buildConfigField` | xcconfig → Info.plist → `Bundle.main` |
| flavor-এর আলাদা `google-services.json` | প্রতিটা configuration-এর আলাদা `GoogleService-Info.plist` (build phase script দিয়ে কপি হয়) |

**ফাঁদ:** CocoaPods থাকলে, নতুন configuration যোগ করার পর CocoaPods-কেও সেটা জানাতে হয়। `ios/Podfile`-এর `project 'Runner', { ... }` block-এ নামগুলো লিখুন (`'Debug-dev' => :debug`, `'Profile-dev' => :release`, `'Release-dev' => :release`)। তারপর আবার `pod install` চালান। এটা না করলে "xcconfig not found" warning আর অদ্ভুত সব build error আসে। Swift Package Manager-এ এই ঝামেলা নেই।

[উপরে ফিরুন](#toc)

### <a id="ios3-5"></a>iOS ৩.৫ Swift Package Manager বনাম CocoaPods

**এক লাইনে:** iOS-এর `pub` হলো **Swift Package Manager (SPM)**। এটা Apple-এর নিজের tool, Xcode-এর ভেতরেই থাকে। CocoaPods ছিল পুরনো, community-র বানানো tool। আজকের দিনে SPM-ই ঠিক পথ।

**Flutter-এ:**

```yaml
# pubspec.yaml
dependencies:
  dio: ^5.0.0
```

**Native app-এ SPM — Xcode দিয়ে:** File → Add Package Dependencies-এ যান। GitHub URL দিন। Version-এর নিয়ম বেছে নিন। তারপর কোন target-এ package যোগ হবে, সেটা বেছে নিন। Xcode এটা `project.pbxproj`-এ লিখে রাখে। আর ঠিক কোন version এল, সেটা লেখে `Package.resolved`-এ। এটা Flutter-এর `pubspec.lock`-এর মতো।

**নিজের package — `Package.swift`:**

Swift package হলো code ভাগ করার একটা একক, অনেকটা একটা Dart package-এর মতো। Package-এর manifest file Swift-এই লেখা হয়:

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

`from: "1.0.0"` মানে `1.0.0` থেকে শুরু করে `2.0.0`-এর আগ পর্যন্ত যেকোনো version। এটা Dart-এর `^1.0.0`-এর মতোই।

| | `pub` | SPM | CocoaPods |
|---|---|---|---|
| Manifest | `pubspec.yaml` | `Package.swift` (package) / Xcode project (app) | `Podfile` (app), `.podspec` (library) |
| Lock | `pubspec.lock` | `Package.resolved` | `Podfile.lock` |
| কে বানায় | Dart team | Apple, Xcode-এর ভেতরে | Community, Ruby tool |
| Registry | pub.dev | সরাসরি git repo | CocoaPods trunk |
| `^1.0.0` | `^1.0.0` | `from: "1.0.0"` / `.upToNextMajor(from:)` | `'~> 1.0'` |

**Flutter-এ এখন কী চলছে (নভেম্বর ২০২৬):**
- **Flutter 3.44 থেকে SPM ডিফল্টে চালু।** Flutter upgrade করে app চালালে flutter tool নিজেই SPM-এর সেটআপ যোগ করে দেয়।
- কোনো plugin যদি এখনো SPM support না করে, তার জন্য Flutter CocoaPods ব্যবহার করে। এমন একটা plugin থাকলেও Podfile রয়ে যায়।
- **CocoaPods-এর registry (trunk) ২ ডিসেম্বর ২০২৬ থেকে read-only হয়ে যাবে।** মানে নতুন pod বা কোনো pod-এর নতুন version আর publish হবে না। Flutter docs সাবধান করছে, সামনে SPM বন্ধ করার option-ও আর থাকবে না।
- বন্ধ করার উপায় (দরকার না হলে করবেন না): `pubspec.yaml`-এ `flutter: config: enable-swift-package-manager: false`।

**Best approach:** নতুন native code আর নতুন plugin-এ শুধু SPM ব্যবহার করুন। Flutter project-এ কোনো plugin এখনো শুধু CocoaPods-এ চললে, তার SPM-সহ version বা অন্য কোনো plugin খুঁজুন। নিজে plugin লিখলে সাথে `Package.swift` দিন।

**ফাঁদ:** `Package.resolved` git-এ না রাখা। তাহলে একেক machine একেক version পেতে পারে। এটা `pubspec.lock` commit না করার মতোই সমস্যা। App project-এ এই file commit করুন।

[উপরে ফিরুন](#toc)

### <a id="ios3-6"></a>iOS ৩.৬ Info.plist

**এক লাইনে:** Info.plist-এ থাকে app-এর পরিচয় আর মূল তথ্য। App খোলার আগেই iOS এটা পড়ে। AndroidManifest যে কাজগুলো করে, তার একটা বড় অংশ এখানে হয়। তবে iOS-এ কোনো component (Activity, Service-এর মতো) আগে থেকে জানিয়ে রাখতে হয় না।

Info.plist একটা XML file। এর ভেতরে থাকে key-value-এর একটা dictionary। Xcode-এ এটা table-এর মতো দেখায়। ডান-click করে "Open As → Source Code" দিলে আসল XML দেখা যায়।

**Notes app-এর Info.plist-এ যা থাকবে:**

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
| Permission | `<uses-permission>` — আগে জানিয়ে রাখতে হয় | `NS...UsageDescription` — আগে জানানোর কিছু নেই, শুধু user-কে দেখানোর কারণটা লিখতে হয় |
| Deep link | `<intent-filter>` | `CFBundleURLTypes` (scheme), Associated Domains entitlement (universal link) |
| App-এর নাম, icon | `android:label`, `android:icon` | `CFBundleDisplayName`, Assets-এর AppIcon |
| Background কাজ | `<service>`, foreground service type | `UIBackgroundModes` |
| Screen জানিয়ে রাখা | `<activity>` | লাগে না |
| Scene / window | (নেই) | `UIApplicationSceneManifest` ([iOS ৪.১](#ios4-1)) |

**Permission-এ বড় পার্থক্য:**
- Android-এ Manifest-এ permission না লিখলে runtime-এ request-ই করা যায় না।
- iOS-এ permission আগে জানিয়ে রাখার কিছু নেই। শুধু একটা string লাগে, যেখানে কারণটা লেখা থাকে।
- এই string না থাকলে প্রথমবার camera বা photo ছোঁয়ার সাথে সাথে app crash করে। Flutter-এ `image_picker` যোগ করে Info.plist-এ লাইন লিখতে ভুলে গেলে যে crash হতো, এটা সেটাই।
- App review-এর সময় Apple এই লেখাটাও পড়ে দেখে। শুধু "camera লাগবে" লিখলে হবে না। কেন লাগবে, সেটা বলুন।

**Privacy manifest — `PrivacyInfo.xcprivacy` (নামটা চিনে রাখুন):** এটা Info.plist-এর পাশে থাকা আরেকটা plist file। এখানে দুইটা জিনিস লিখতে হয়। এক, app (আর প্রতিটা SDK) কী কী data collect করে। দুই, কিছু নির্দিষ্ট API (যেমন `UserDefaults`, file-এর timestamp) কেন ব্যবহার করে। ১ মে ২০২৪ থেকে নতুন app বা update-এ এই API-গুলোর কারণ লেখা না থাকলে App Store Connect upload আটকে দেয়। Flutter template-এ এই file থাকে না। আপনার নিজের code বা কোনো plugin এই API-গুলো ব্যবহার করলে file-টা নিজেকে যোগ করতে হয়। Release-এর বিস্তারিত পরের অধ্যায়গুলোতে আছে।

[উপরে ফিরুন](#toc)

### <a id="ios3-7"></a>iOS ৩.৭ Entitlements

**এক লাইনে:** Entitlement হলো app-এর বিশেষ ক্ষমতাগুলোর তালিকা। যেমন push, App Group, Keychain ভাগ করা, universal link, iCloud। এগুলো একটা `.entitlements` file-এ থাকে। Signing-এর সময় এগুলো app-এর signature-এর ভেতরে ঢুকে যায়।

Xcode-এ target → **Signing & Capabilities** → "+ Capability" চাপলে Xcode নিজেই `Runner.entitlements` বানায় বা বদলায়:

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
| কে check করে | iOS, app চলার সময় | iOS, signature দেখে — আর provisioning profile-এও এটা থাকতেই হবে |
| ভুল হলে | crash হয়, বা feature কাজ করে না | install বা upload fail করে, বা feature কোনো error ছাড়াই চুপচাপ কাজ করে না |
| Android-এ কাছাকাছি | Manifest | (সরাসরি কিছু নেই — signature permission-এর কাছাকাছি) |

**Profile-এ কেন থাকতে হয়:** Apple Developer portal-এ আপনার App ID-তে capability-টা চালু থাকতে হয়। আর provisioning profile-এও সেটা থাকতে হয়। Xcode-এর "Automatically manage signing" চালু থাকলে Xcode নিজেই এগুলো মিলিয়ে নেয়। হাতে signing করলে (যেমন CI-তে) profile নতুন করে বানাতে হয়। Signing আর release-এর পুরো গল্প পরের অধ্যায়গুলোতে।

**ফাঁদ:** Flutter-এ `firebase_messaging` যোগ করলেন, কিন্তু push আসছে না। প্রায়ই এর কারণ হলো Push Notifications capability যোগ করা হয়নি, তাই `aps-environment` entitlement-ও নেই। Dart দিকে কোনো পরিষ্কার error আসে না, শুধু token আসে না। Xcode console-এ "no valid 'aps-environment' entitlement string found" দেখলে বুঝবেন, কারণ এটাই।

[উপরে ফিরুন](#toc)

### <a id="ios3-8"></a>iOS ৩.৮ Deployment target আর SDK

**এক লাইনে:** **Deployment target** মানে সবচেয়ে পুরনো যে iOS-এ app চলবে (Android-এর `minSdk`)। **SDK** মানে যে iOS version-এর SDK দিয়ে আপনি build করছেন। SDK আসে Xcode-এর সাথে।

Android-এ সংখ্যা ছিল তিনটা ([অধ্যায় ৩](#ch3)): `minSdk`, `compileSdk`, `targetSdk`। iOS-এ মূলত দুইটা:

| Android | iOS | মানে |
|---|---|---|
| `minSdk` | Deployment target (`IPHONEOS_DEPLOYMENT_TARGET`) | এর চেয়ে পুরনো iOS-এ app install-ই হবে না |
| `compileSdk` | SDK — কোন Xcode, সেটাই ঠিক করে দেয় | কোন কোন API ব্যবহার করা যাবে |
| `targetSdk` | আলাদা কোনো setting নেই — SDK-ই এই কাজ করে | নতুন আচরণ চালু হবে কি না |

**শেষ লাইনটা জরুরি।** iOS-এর অনেক নতুন নিয়ম "linked-on-or-after"। মানে নিয়মটা চালু হবে কি না, সেটা ঠিক হয় আপনি কোন SDK দিয়ে build করছেন তার ওপর। যেমন UIScene: iOS 26-এর পরের major release-এর SDK দিয়ে build করলে, app-এ UIScene না থাকলে app launch-ই হবে না ([iOS ৪.১](#ios4-1))। তাই Xcode বদলানো মানে Android-এ `targetSdk` বাড়ানোর মতো। App-এর আচরণ বদলে যেতে পারে। নতুন Xcode-এ যাওয়ার পর পুরো app একবার test করে নিন।

**আজকের সংখ্যাগুলো (নভেম্বর ২০২৬):**
- **Flutter:** iOS 15 থেকে support করে। নতুন Flutter project-এর template-এ deployment target `15.0`।
- **App Store upload:** ২৮ এপ্রিল ২০২৬ থেকে Xcode 26 বা তার নতুন version আর iOS 26 SDK দিয়ে build করা বাধ্যতামূলক। Apple সাধারণত প্রতি বছর বসন্তকালে এই নিয়ম এক ধাপ বাড়ায়। নিয়মিত [developer.apple.com/news/upcoming-requirements](https://developer.apple.com/news/upcoming-requirements/) দেখুন।
- **নতুন native app:** `@Observable` আর SwiftData চাইলে iOS 17 লাগবে। এখন বেশিরভাগ নতুন app iOS 17 বা 18 থেকে শুরু করে।

**Code-এ পুরনো iOS সামলানো:**

```swift
@available(iOS 18, *)
struct NotesTabs: View { ... }         // পুরো type শুধু iOS 18+

if #available(iOS 18, *) {
    NotesTabs()
} else {
    LegacyNotesTabs()
}
```

**Plugin-এর deployment target:** প্রতিটা plugin-এর নিজের একটা minimum iOS আছে। App-এর deployment target তার চেয়ে কম হলে build fail করে। Flutter-এ `pod install` বা build-এর সময় deployment target নিয়ে যে error বা warning আসে, সেগুলোর কারণ প্রায় সবসময় এটাই।

> **মনে রাখুন**
> - Target মানে কী বানাবেন। Configuration মানে কোন setting-এ। Scheme মানে কোন বোতামে কোনটা।
> - Flutter-এর `--flavor dev` মানে scheme `dev`, সাথে configuration `Debug-dev` / `Release-dev` / `Profile-dev`।
> - Setting রাখুন xcconfig-এ। সেখানে `//` মানে comment। আর app-এ কোনো secret রাখবেন না।
> - SPM-ই ঠিক পথ। Flutter 3.44 থেকে এটা ডিফল্ট, আর CocoaPods trunk ২ ডিসেম্বর ২০২৬ থেকে read-only।
> - Info.plist-এ permission-এর কারণ না থাকলে app crash করে। বিশেষ ক্ষমতা (push, App Group) থাকে entitlement-এ, আর profile-এও থাকতে হয়।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ flavor বলে কিছু নেই। আমি প্রতিটা environment-এর জন্য একটা shared scheme আর আলাদা build configuration বানাই। Setting রাখি xcconfig-এ — bundle id, display name, API host। Flutter-এর `--flavor dev` ঠিক এই নামের scheme খোঁজে, আর `Debug-dev`-এর মতো নামের configuration খোঁজে। Dependency-র জন্য Swift Package Manager নিই। কারণ Flutter 3.44 থেকে এটাই ডিফল্ট, আর CocoaPods বন্ধ হওয়ার পথে।"
> - *English:* "iOS has no flavors as such. I create a shared scheme per environment with its own build configurations, and keep the settings in xcconfig files — bundle id, display name, API host. Flutter's `--flavor dev` looks for exactly that scheme and configurations named like `Debug-dev`. For dependencies I use Swift Package Manager, since it's the default from Flutter 3.44 and CocoaPods is being wound down."

[উপরে ফিরুন](#toc)

---

## <a id="ios4"></a>iOS ৪. App lifecycle — `@main`, AppDelegate, SceneDelegate আর suspension

Android-এর lifecycle অধ্যায়ে ([অধ্যায় ৫](#ch5)) সবচেয়ে বড় সমস্যা ছিল একটা: phone ঘোরালেই (rotation) Activity মরে যায়। iOS-এ এই সমস্যা নেই। Rotation হোক, dark mode হোক, বা ভাষা বদলাক — screen বেঁচে থাকে, শুধু layout বদলায়। ঠিক Flutter-এর মতো।

কিন্তু iOS-এর নিজের একটা সমস্যা আছে: **app background-এ গেলে অল্প পরেই suspend হয়ে যায়।** তখন কোনো code চলে না। আর suspended app-কে system কোনো খবর না দিয়েই মেরে ফেলতে পারে। এই অধ্যায়ে এই নিয়মগুলো দেখব।

### <a id="ios4-1"></a>iOS ৪.১ চালু হওয়া: `@main` থেকে প্রথম screen

**এক লাইনে:** Flutter-এ শুরু হয় `void main() => runApp(NotesApp())` দিয়ে। SwiftUI-তে তার জায়গায় থাকে একটা struct। এর মাথায় লেখা থাকে `@main`, আর এটা `App` protocol মেনে চলে।

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

- `@main` বলে দেয়, app এখান থেকে শুরু হবে। আলাদা করে `main()` লিখতে হয় না।
- `App`-এর `body` কোনো widget ফেরত দেয় না, দেয় একটা **Scene**। Scene মানে মোটামুটি একটা window। `WindowGroup` মানে "app-এর window"। iPhone-এ window একটাই থাকে। iPad-এ user একাধিক window খুলতে পারে।
- `MaterialApp`-এর মতো কোনো root wrapper লাগে না। Theme, navigation — সব হয় view-এর modifier দিয়ে।

**Push token-এর মতো process-এর কাজ লাগলে — AppDelegate জুড়ে দিন:**

কিছু ঘটনা পুরো process-এর, কোনো window-এর না। যেমন push token পাওয়া। এগুলো আসে AppDelegate-এ। SwiftUI app-এ AppDelegate এভাবে জুড়ে দেওয়া যায়:

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

**UIKit-এর পুরনো পথ (চিনে রাখুন) — দুইটা delegate:**

```
@main AppDelegate (UIApplicationDelegate)   ← process-এর ঘটনা: launch, push token, terminate
        │
        └─ SceneDelegate (UIWindowSceneDelegate) ← প্রতিটা window-এর ঘটনা:
               scene(_:willConnectTo:options:)      window তৈরি, প্রথম ViewController বসানো
               sceneDidBecomeActive / sceneWillResignActive
               sceneWillEnterForeground / sceneDidEnterBackground
               scene(_:openURLContexts:)            deep link
```

iOS 13-এর আগে সবকিছু AppDelegate-এ থাকত। iOS 13 iPad-এ একাধিক window আনল। তাই window-এর কাজগুলো সরে গেল SceneDelegate-এ। SwiftUI-র `App` ভেতরে ভেতরে নিজেই scene দিয়ে চলে।

**UIScene এখন বাধ্যতামূলক — আর এটা Flutter-কেও ছোঁয়:** Apple-এর TN3187 বলে, iOS 26-এর পরের major release-এর SDK দিয়ে build করলে UIScene lifecycle ছাড়া app **launch-ই হবে না।** iOS 27 SDK (Xcode 27) এখন বের হয়ে গেছে। তাই যে পুরনো app শুধু AppDelegate দিয়ে চলে, তার হাতে আর সময় নেই।
- SwiftUI `App` দিয়ে বানানো app আগে থেকেই scene দিয়ে চলে। আপনাকে কিছু করতে হবে না।
- Flutter 3.38-এ UIScene support এসেছে, আর **3.41 থেকে এটা ডিফল্ট।** আপনি AppDelegate-এ হাত না দিয়ে থাকলে `flutter run` বা `flutter build ios` নিজেই migrate করে দেয়। এজন্যই নতুন template-এ `SceneDelegate.swift` আর `FlutterImplicitEngineDelegate` দেখবেন ([iOS ০.১](#ios0-1))।
- AppDelegate নিজে বদলে থাকলে হাতে migrate করতে হবে। তিনটা কাজ:
  - plugin registration সরিয়ে নিন `didInitializeImplicitFlutterEngine`-এ।
  - Info.plist-এ `UIApplicationSceneManifest` যোগ করুন।
  - `didFinishLaunchingWithOptions`-এর ভেতরে `FlutterViewController` ছোঁবেন না। তখনো window তৈরি হয়নি, তাই crash হতে পারে।
- Deep link আর scene-এর অন্য ঘটনাগুলো এখন আসে SceneDelegate-এ। কোনো পুরনো plugin যদি AppDelegate-এর `application(_:open:options:)`-এ অপেক্ষা করে, সে আর ঘটনা পাবে না। `FlutterSceneDelegate` এই ঘটনাগুলো plugin-এর কাছে পৌঁছে দেয়। এজন্যই Flutter বলে এটাকে subclass করতে।

**ভেতরে কীভাবে কাজ করে — launch-এর ধাপগুলো (UIKit):**
1. System process বানায়, আর `main()` চলে (`@main` থাকলে Swift এটা নিজেই বানিয়ে দেয়)।
2. `UIApplicationMain` চলে। এটা `UIApplication` আর আপনার AppDelegate তৈরি করে।
3. `application(_:willFinishLaunchingWithOptions:)` চলে, তারপর `application(_:didFinishLaunchingWithOptions:)`।
4. Scene তৈরি হয়, `scene(_:willConnectTo:options:)` চলে। এখানে window আর প্রথম screen বসে।
5. Scene সামনে আসে, `sceneDidBecomeActive` চলে।

**Senior-দের জন্য একটা সূক্ষ্ম কথা — prewarming:** iOS মাঝে মাঝে user tap করার আগেই আপনার process বানিয়ে রাখে। Library-গুলো load করে, তারপর process-টা suspend করে রাখে। এর দুইটা ফল:
- "Process শুরু থেকে প্রথম frame পর্যন্ত" হিসেবে launch time মাপলে সংখ্যাটা অনেক বড় দেখাতে পারে।
- `main()`-এর আগে চলা code-এ (static initializer) এমন কিছু করবেন না, যা ধরে নেয় user এই মুহূর্তে app খুলছে।

[উপরে ফিরুন](#toc)

### <a id="ios4-2"></a>iOS ৪.২ App-এর অবস্থাগুলো

**এক লাইনে:** iOS-এ একটা app পাঁচটা অবস্থার যেকোনো একটায় থাকতে পারে। সবচেয়ে জরুরি শেষেরটা — **Suspended**। তখন app memory-তে থাকে, কিন্তু কিছুই চলে না।

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
| Not running | চালুই হয়নি, বা মেরে ফেলা হয়েছে | না |
| Inactive | সামনে আছে, কিন্তু touch পাচ্ছে না (call এল, Control Center টানা হলো, app switcher খোলা) | হ্যাঁ |
| Active | সামনে আছে, touch পাচ্ছে | হ্যাঁ |
| Background | দেখা যাচ্ছে না, শেষ কাজগুলো গুছিয়ে নিচ্ছে | হ্যাঁ, অল্প সময় |
| Suspended | Memory-তে আছে, কিন্তু থেমে আছে | **না** |

**Scene-এর অবস্থা:** UIScene-এ প্রতিটা window-এর নিজের আলাদা অবস্থা থাকে: Unattached → Foreground Inactive → Foreground Active → Background। iPhone-এ scene একটাই, তাই app আর scene-এর অবস্থা প্রায় একসাথেই বদলায়।

**Flutter এটা কীভাবে দেখে:** Flutter engine এই ঘটনাগুলো শোনে, আর সেখান থেকে `AppLifecycleState` বানায় ([iOS ৪.৩](#ios4-3)-এর table দেখুন)। Suspended অবস্থায় Flutter-এ কোনো callback আসে না। কারণ তখন Dart code-ও চলে না।

[উপরে ফিরুন](#toc)

### <a id="ios4-3"></a>iOS ৪.৩ `scenePhase` — `didChangeAppLifecycleState`-এর জায়গায়

**এক লাইনে:** SwiftUI-তে `@Environment(\.scenePhase)` পড়ুন, আর `.onChange` দিয়ে এর বদল শুনুন। মান তিনটা: `.active`, `.inactive`, `.background`।

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

এখানে observer যোগ করা বা সরানোর ঝামেলা নেই। View চলে গেলে শোনাও নিজে থেকে বন্ধ হয়ে যায়।

- কোনো view-এর ভেতরে পড়লে `scenePhase` সেই view-এর scene-এর অবস্থা দেয়।
- `App`-এর `body`-তে পড়লে সব scene মিলিয়ে একটা অবস্থা দেয়। কোনো একটা scene active থাকলেই মান হয় `.active`।
- `@unknown default` কেন? Apple পরে নতুন case যোগ করতে পারে, তাই compiler এটা চায়।

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

`hidden` অবস্থাটা iOS-এর নিজের না। Flutter 3.13 থেকে চায় সব platform-এ state machine একই রকম থাকুক। তাই iOS-এ `inactive` আর `paused`-এর মাঝখানে Flutter নিজে একটা `hidden` বসিয়ে দেয়।

**Best approach:** Draft save করার ঠিক জায়গা `.background`। কিন্তু শুধু এর ওপর ভরসা করবেন না। User টাইপ করার সময়েই একটু পরপর (debounce করে) save করুন। কেন, সেটা পরের অংশে।

[উপরে ফিরুন](#toc)

### <a id="ios4-4"></a>iOS ৪.৪ Background suspension আর termination

**এক লাইনে:** Background-এ গেলে app অল্প কিছু সময় পায়, তারপর suspend হয়। এরপর system-এর memory লাগলে সে suspended app-কে মেরে ফেলে — **কোনো callback ছাড়াই।** User ফিরে এলে app একদম শূন্য থেকে চালু হয়।

**Notes app দিয়ে গল্পটা:**
1. User একটা note লিখছে। অর্ধেক লিখে Camera app খুলল।
2. আপনার app `.background` পেল। একটু পরেই suspend হলো। সব Dart বা Swift code থেমে গেল।
3. Camera অনেক memory চাইল। System আপনার suspended app মেরে ফেলল। কোনো `applicationWillTerminate` আসেনি।
4. User ফিরে এল। App **নতুন করে launch** হলো। Memory-তে যা ছিল, সব শেষ।

**`applicationWillTerminate`-এর ওপর ভরসা করবেন না।** Apple-এর docs পরিষ্কার বলে: যে app background support করে, user সেটা বন্ধ করলে এটা সাধারণত call হয় না। এটা call হয় শুধু একটা ক্ষেত্রে — app background-এ সত্যিই কিছু চালাচ্ছে (suspended না), আর তখন system তাকে মেরে ফেলে। User app switcher থেকে swipe করে বন্ধ করলে suspended app কোনো খবরই পায় না।

**জরুরি কাজ শেষ করতে একটু বেশি সময় চাওয়া:**

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

এটা শুধু "একটু বেশি সময়", যতক্ষণ খুশি না। কতক্ষণ পাবেন, সেটা system নিজে ঠিক করে। বাকি সময়টা `backgroundTimeRemaining` দিয়ে দেখা যায়। কাজ শেষে `endBackgroundTask` না ডাকলে system app মেরে ফেলতে পারে।

**Background-এ নিয়মিত কাজ (sync, upload) চাইলে:** iOS-এ এর জন্য নির্দিষ্ট কিছু পথ আছে — `BGTaskScheduler`, background `URLSession`, silent push, background mode। এগুলো পরের অধ্যায়গুলোতে দেখব। মূল কথা হলো, কাজটা কখন চলবে সেটা iOS ঠিক করে, আপনি না। Android-এর WorkManager-এর চেয়েও এখানে নিশ্চয়তা কম।

| | iOS | Android | Flutter-এ যা দেখতেন |
|---|---|---|---|
| Background-এ গেলে | অল্প সময়, তারপর suspend | Process চলতে থাকে (cached), কিছু কাজও চলে | `paused` |
| মেরে ফেলা | Suspended app, কোনো callback নেই | Process death, কোনো callback নেই | কিছুই আসে না |
| লম্বা কাজ | `BGTaskScheduler`, background `URLSession` | WorkManager, foreground service | `workmanager` |
| User swipe করে বন্ধ করলে | Suspended থাকলে কোনো খবর নেই | একই | কিছু আসে না |

**ফাঁদ:** `.background`-এ একটা লম্বা network call শুরু করা, এই ভেবে যে ওটা শেষ হবে। App suspend হলে call মাঝপথেই থেমে যায়। Upload শেষ হওয়া জরুরি হলে background `URLSession` ব্যবহার করতে হবে।

[উপরে ফিরুন](#toc)

### <a id="ios4-5"></a>iOS ৪.৫ State restoration — `@SceneStorage`

**এক লাইনে:** System app মেরে ফেলার পর user ফিরে এলে iOS চায় app আগের জায়গাতেই খুলুক — যে note খোলা ছিল, যে text লেখা ছিল। SwiftUI-তে ছোট UI state ফেরানোর জন্য আছে `@SceneStorage`।

**Flutter-এ:** এর জন্য আছে `RestorationMixin`, `RestorableTextEditingController`, আর `MaterialApp`-এ `restorationScopeId`। তবে বেশিরভাগ Flutter app এটা করে না। তারা শুরু থেকে খোলে।

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

- এটা `@State`-এর মতোই কাজ করে। পার্থক্য হলো, system মানটা save করে রাখে, আর app নতুন করে চালু হলে ফেরত দেয়।
- **প্রতিটা scene-এর নিজের আলাদা storage।** iPad-এ দুইটা window খোলা থাকলে দুইটা আলাদা draft থাকবে।
- শুধু ছোট আর সাধারণ type রাখা যায়: `String`, `Int`, `Bool`, `Double`, `URL`, `Data`, আর এদের দিয়ে বানানো `RawRepresentable` enum। পুরো note-এর list রাখবেন না, শুধু id রাখুন।
- কখন save হবে, তার কোনো নিশ্চয়তা নেই (Apple-এর docs নিজেই এটা বলে)। আর scene মুছে গেলে data-ও মুছে যায়, যেমন user app switcher থেকে window সরিয়ে দিলে। তাই এটা শুধু একটা "সুবিধা"। Data বাঁচানোর জায়গা এটা না।
- Secret বা ব্যক্তিগত data এখানে রাখবেন না। Apple এটা মানা করে।

**State কোথায় রাখবেন — এক table-এ:**

| State | কোথায় | Rotation-এ | System মারলে | User swipe করে বন্ধ করলে | Android-এ |
|---|---|---|---|---|---|
| ছোট UI state (menu খোলা কি না) | `@State` | থাকে | হারায় | হারায় | `remember` |
| যে UI state ফিরে আসা উচিত (খোলা note-এর id, লেখা text) | `@SceneStorage` | থাকে | থাকে | হারায় | `rememberSaveable` |
| Screen-এর state আর logic | `@Observable` model | থাকে | হারায় | হারায় | `ViewModel` |
| User-এর setting | `@AppStorage` (`UserDefaults`) | থাকে | থাকে | থাকে | DataStore |
| আসল data, draft | SwiftData, file, server | থাকে | থাকে | থাকে | Room |

**Best approach:** আসল data আর অর্ধেক লেখা draft রাখুন database-এ, আর save করুন টাইপ করার সময়েই। কোন screen বা কোন note খোলা ছিল, সেটার id রাখুন `@SceneStorage`-এ। তাহলে app যেভাবেই মরুক, কিছু হারাবে না।

**নিজে test করুন:**
1. Xcode থেকে app চালান। একটা note খুলে কিছু লিখুন।
2. Home screen-এ যান (app এখন background-এ)।
3. Xcode-এর ■ Stop বোতাম চাপুন। এটা system-এর app মেরে ফেলার মতোই।
4. Home screen থেকে app আবার খুলুন।

যা যা হারিয়ে গেল, সেগুলোই bug। Android-এ এই কাজটা করত `adb shell am kill`। (App switcher থেকে swipe করে বন্ধ করে test করবেন না। তখন iOS ইচ্ছা করেই restoration data মুছে দেয়।)

[উপরে ফিরুন](#toc)

### <a id="ios4-6"></a>iOS ৪.৬ Memory warning

**এক লাইনে:** Memory কমে গেলে iOS আগে সতর্ক করে। তখন cache খালি করে দিন। না দিলে, বা app অনেক বেশি memory নিলে, system app মেরে ফেলে — app সামনে (foreground-এ) থাকলেও।

**Flutter-এ:** `WidgetsBindingObserver.didHaveMemoryPressure()`। এই সময় Flutter engine নিজেও image cache ছোট করে।

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

UIKit-এ আছে `UIApplicationDelegate.applicationDidReceiveMemoryWarning(_:)`, আর প্রতিটা `UIViewController`-এর `didReceiveMemoryWarning()`।

**ভেতরে কীভাবে কাজ করে — jetsam:**
- iPhone-এ swap নেই। মানে memory-র data disk-এ সরিয়ে রাখা যায় না, শুধু compress করা যায়।
- Memory ফুরিয়ে গেলে kernel-এর **jetsam** নামের ব্যবস্থা process মারা শুরু করে। কে আগে মরবে, সেটা সে priority দেখে ঠিক করে। আগে suspended app, তারপর background app, আর শেষে দরকার হলে foreground app-ও।
- Foreground app তার memory-র সীমা পার হলে মারা যায়, কোনো crash log ছাড়াই।
- এগুলো Xcode Organizer-এ "Terminations" নামে দেখা যায়।

| | iOS | Android | Flutter |
|---|---|---|---|
| সতর্কবার্তা | `didReceiveMemoryWarningNotification` | `onTrimMemory()` | `didHaveMemoryPressure()` |
| শেষ ব্যবস্থা | jetsam process মারে | Low Memory Killer | — |
| Swap | iPhone-এ নেই (compressed memory) | zRAM (compressed) | — |

**ফাঁদ:** বড় ছবি পুরো resolution-এ decode করে memory-তে রেখে দেওয়া। একটা 12MP ছবি decode করলে প্রায় ৪৮ MB লাগে (প্রতি pixel-এ ৪ byte)। একটা note-এ দশটা ছবি মানেই app মারা যাবে। তাই thumbnail বানিয়ে রাখুন — Flutter-এ `cacheWidth` দেওয়ার মতো।

[উপরে ফিরুন](#toc)

### <a id="ios4-7"></a>iOS ৪.৭ Android-এর সাথে তুলনা — কোনটা নেই, কোনটা বেশি

| বিষয় | Android | iOS |
|---|---|---|
| Rotation, dark mode, ভাষা বদল | Activity মুছে গিয়ে নতুন করে তৈরি হয় ([৫.২](#ch5-2)) | কিছু মরে না, শুধু layout/trait বদলায় |
| তাই `ViewModel`-এর মতো "rotation-এ বেঁচে থাকা" জিনিস লাগে? | হ্যাঁ | না — `@Observable` model একটা সাধারণ object |
| Background-এ code | চলতে পারে, তবে সীমা আছে | অল্প সময়, তারপর suspend |
| Process death | Background-এ থাকলে হয়, callback নেই | Suspended থাকলে হয়, callback নেই |
| ফিরে এলে system কোথায় খোলে | ঠিক আগের Activity-তে, back stack-সহ | আপনি `@SceneStorage` দিয়ে যা ফেরান সেখানে — নইলে শুরু থেকে |
| Restoration data রাখার জায়গা | Bundle (~১ MB) | `@SceneStorage` (ছোট রাখুন) |
| Test | `adb shell am kill` | Background + Xcode Stop |

সবচেয়ে বড় পার্থক্য পঞ্চম লাইনে। Android-এ system নিজেই back stack ফিরিয়ে দেয়, আর আশা করে app ঠিক জায়গা থেকে চলবে। iOS শুধু data রাখার একটা জায়গা দেয়। কী ফেরাবেন, সেটা আপনি ঠিক করবেন।

> **মনে রাখুন**
> - SwiftUI-তে থাকে `@main struct ...: App` আর `WindowGroup`। UIKit-এ থাকে AppDelegate (process-এর জন্য) আর SceneDelegate (window-এর জন্য)।
> - UIScene এখন বাধ্যতামূলক (TN3187)। Flutter 3.41 থেকে এটা ডিফল্ট। পুরনো custom AppDelegate থাকলে হাতে migrate করুন।
> - `scenePhase`-এর মান: `.active` / `.inactive` / `.background`। Suspended অবস্থায় কিছুই আসে না।
> - Suspended app-কে system চুপচাপ মেরে ফেলে। `applicationWillTerminate`-এর ওপর ভরসা করবেন না। টাইপ করার সময়েই save করুন।
> - Rotation-এ কিছু মরে না। Android-এর বড় সমস্যাটা iOS-এ নেই।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ background-এ গেলে app অল্প সময় পায়, তারপর suspend হয়। System-এর memory লাগলে সে suspended app-কে কোনো callback ছাড়াই মেরে ফেলে। তাই আমি draft টাইপ করার সময়েই database-এ save করি। `scenePhase` `.background` হলে শেষবারের মতো flush করি, দরকার হলে `beginBackgroundTask` দিয়ে একটু সময় নিই। কোন screen খোলা ছিল, এমন ছোট state রাখি `@SceneStorage`-এ। আর Flutter 3.41 থেকে iOS app-এ UIScene ডিফল্ট। নতুন SDK-তে এটা ছাড়া app launch-ই হবে না।"
> - *English:* "On iOS, an app gets a short time in the background and is then suspended. If the system needs memory, it kills a suspended app with no callback. So I save drafts to the database while the user types, and do a final flush when `scenePhase` becomes `.background`, using `beginBackgroundTask` if I need a bit more time. I keep small UI state like the open screen in `@SceneStorage`. And since Flutter 3.41, iOS apps use the UIScene lifecycle by default — with the newest SDK, an app without it won't launch."

[উপরে ফিরুন](#toc)

---

## <a id="ios5"></a>iOS ৫. SwiftUI — Widget-এর জায়গায় View

এই অধ্যায়ে আপনার Flutter-এর অভিজ্ঞতা সবচেয়ে বেশি কাজে আসবে। SwiftUI এসেছিল ২০১৯-এ, Flutter-এর প্রায় একই সময়ে। ধারণাও একই: **UI = f(state)।** মানে আপনি শুধু state বদলান, আর যে অংশ আবার আঁকা দরকার, framework নিজেই সেটা আঁকে।

Compose-এর অধ্যায় ([অধ্যায় ৬](#ch6)) পড়ে থাকলে দেখবেন, তিনটা framework প্রায় একই ভাষায় কথা বলে। পার্থক্য শুধু ছোট ছোট জায়গায়। আর মানুষ আটকায় ঠিক ওই জায়গাগুলোতেই।

শুরুর আগে একটা কথা। SwiftUI আসে OS-এর সাথে। তাই প্রতিটা API-র একটা minimum iOS আছে। এই অধ্যায়ের code লেখা হয়েছে iOS 17+ ধরে (`@Observable`-এর জন্য)। যেখানে iOS 18 লাগবে, সেখানে বলে দেওয়া আছে।

### <a id="ios5-1"></a>iOS ৫.১ Widget → View

**এক লাইনে:** `StatelessWidget` আর তার `build()`-এর জায়গায় থাকে একটা `struct`। এটা `View` protocol মেনে চলে, আর এর একটা `body` property থাকে।

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
| constructor field | `let` property (memberwise init নিজে থেকেই আসে) | parameter |
| `child:` / `children: [...]` | `{ }`-এর ভেতরে একটার পর একটা লেখা (result builder) | trailing lambda |
| `BuildContext` | নেই — যা দরকার তা আসে `@Environment` দিয়ে | `CompositionLocal` |
| `const` widget | struct নিজেই সস্তা, আর SwiftUI নিজে তুলনা করে নেয় | compiler skip |
| `Icon(Icons.push_pin)` | `Image(systemName: "pin.fill")` — SF Symbols | `Icon(Icons.Default...)` |
| children-এর ভেতরে `if (x) widget` | `if x { View }` | `if (x) { }` |

**`some View` কেন:** `body`-এর আসল type খুব লম্বা হয়, যেমন `HStack<TupleView<(VStack<...>, Spacer, Optional<Image>)>>`। `some View` মানে: "এটা একটা নির্দিষ্ট View type। Compiler type-টা জানে, আমি শুধু নামটা লিখছি না" ([iOS ১.৭](#ios1-7))।

**`{ }`-এর ভেতরে একটার পর একটা View লিখলে কীভাবে চলে:** এটা করে `@ViewBuilder` নামের একটা **result builder**। আপনি View-গুলো পরপর লিখে যান, আর compiler সেগুলো জুড়ে একটা tuple বানায়। এর ভেতরে কী চলে আর কী চলে না:
- চলে: `if`, `if let`, `switch`, `ForEach`, আর ছোট `let x = ...`।
- চলে না: সাধারণ `for` loop, বা কোনো মান বদলানোর মতো অন্য statement।
- loop লাগলে `ForEach` লিখুন। বাকি কাজ রাখুন `body`-এর বাইরে, বা একটা আলাদা computed property-তে।

**ভেতরে কীভাবে কাজ করে — তিনটা tree, Flutter-এর পাশে রেখে:**

| Flutter | SwiftUI |
|---|---|
| Widget — হালকা বর্ণনা, বদলায় না | View struct — হালকা একটা value, শুধু বর্ণনা |
| Element — বেঁচে থাকে, state ধরে রাখে | SwiftUI-র ভেতরের graph (attribute graph) — view-এর identity আর state রাখে |
| RenderObject — layout আর paint | ভেতরে UIKit view আর Core Animation layer |

View struct প্রতিবার নতুন করে তৈরি হয়, আবার ফেলেও দেওয়া হয়। Widget-এর মতোই এটা সস্তা। যেটা টিকে থাকে, সেটা SwiftUI-র ভেতরের graph।

**বড় পার্থক্য:** Flutter প্রতিটা pixel নিজে আঁকে। SwiftUI শেষ পর্যন্ত আঁকে Apple-এর নিজের UI system দিয়ে। তাই `Text` আসলে system-এর নিজের text, আর `List`-এর ভেতরে আছে UIKit-এর collection view। এর ফলে accessibility, Dynamic Type, dark mode — এগুলো আপনি কোনো বাড়তি কাজ ছাড়াই পেয়ে যান।

[উপরে ফিরুন](#toc)

### <a id="ios5-2"></a>iOS ৫.২ Layout

**এক লাইনে:** `Column` হয়ে যায় `VStack`, `Row` হয় `HStack`, `Stack` হয় `ZStack`। আর `Expanded` ও `SizedBox`-এর জায়গায় আসে `Spacer()` আর `.frame()`।

**Notes app-এর header, দুই framework-এ:**

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
| `mainAxisAlignment: spaceBetween` | মাঝখানে `Spacer()` | `Arrangement.SpaceBetween` |
| `Center` | default — stack নিজেই মাঝখানে রাখে | `Box(contentAlignment = Center)` |
| `Wrap` | `Layout` protocol দিয়ে নিজে বানাতে হয় | `FlowRow` |
| `LayoutBuilder` | `GeometryReader` | `BoxWithConstraints` |
| `Scaffold` + `AppBar` | `NavigationStack` + `.navigationTitle`, `.toolbar` | `Scaffold` + `TopAppBar` |
| `SafeArea` | **default-এ চালু** — বাইরে যেতে `.ignoresSafeArea()` | `innerPadding` |
| logical pixel | point (pt) | `dp` |

**Layout কীভাবে হয় — Flutter-এর প্রায় একই রকম:** Flutter-এর নিয়ম আপনি জানেন: "constraints go down, sizes go up, parent sets position"। SwiftUI-তে ধাপগুলো এরকম:
1. Parent child-কে একটা size বলে দেয়। এটা একটা প্রস্তাব, হুকুম না।
2. Child নিজের size নিজে বেছে নেয়।
3. Parent তাকে জায়গামতো বসায়।

পার্থক্য হলো, SwiftUI-তে child চাইলে parent-এর বলা মাপ না মেনে নিজের মাপ নিতে পারে। যেমন `Text` সবসময় শুধু তার লেখার সমান জায়গা নেয়, আপনি যত জায়গাই দিন। তাই "পুরো চওড়া জায়গা নাও" বলতে হলে `.frame(maxWidth: .infinity)` লিখতে হয়।

**ফাঁদ — `VStack`-এর default spacing শূন্য না।** Flutter-এর `Column`-এ children একদম গায়ে গায়ে থাকে। কিন্তু SwiftUI-র `VStack`/`HStack`-এ `spacing` না দিলে system নিজে থেকে একটা ফাঁক দেয়। Design-এর সাথে pixel মিলাতে চাইলে সবসময় `spacing:` লিখে দিন, যেমন `VStack(spacing: 0)`।

**ফাঁদ — safe area উল্টো।** Android-এ নতুন app default-এ edge-to-edge হয়। `innerPadding` না দিলে content system bar-এর নিচে চলে যায়। SwiftUI-তে উল্টো: content default-এ safe area-র ভেতরেই থাকে। পুরো screen জুড়ে রং চাইলে background-এ `.ignoresSafeArea()` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios5-3"></a>iOS ৫.৩ Wrapper widget → modifier, আর ক্রমের নিয়ম

**এক লাইনে:** Flutter-এ padding, রং, tap — প্রতিটার জন্য আলাদা একটা wrapper widget লাগে। SwiftUI-তে এগুলো হলো **modifier**, যা view-এর পেছনে `.` দিয়ে লাগানো হয়। প্রতিটা modifier আগের view-টাকে মুড়ে একটা নতুন view বানায়।

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

**ক্রম — ভেতর থেকে বাইরের দিকে পড়ুন।** প্রথম modifier থাকে সবচেয়ে ভেতরে, শেষেরটা সবচেয়ে বাইরে:

```swift
Text("বাজার").padding().background(.yellow)   // হলুদের ভেতরে ফাঁক — Container(color, padding)
Text("বাজার").background(.yellow).padding()   // হলুদ শুধু লেখার গায়ে, বাইরে স্বচ্ছ ফাঁক
```

ওপরের প্রথম লাইনটা Flutter-এ লিখলে হতো `ColoredBox(color: yellow, child: Padding(child: Text))`। মানে আপনি nesting-টা ভেতর থেকে বাইরের দিকে পড়ছেন।

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
| `DefaultTextStyle` | parent-এ `.font()` দিলে ভেতরের সব `Text` সেটা পায় |

**Compose-এর সাথে একটা মজার ব্যাপার:** Compose-এ modifier chain পড়তে হয় বাইরে থেকে ভেতরে ([৬.৩](#ch6-3))। তাই `Modifier.padding(16.dp).background(Yellow)`-এ padding থাকে বাইরে। SwiftUI-তে পড়তে হয় উল্টো দিক থেকে। তাই `.padding().background(.yellow)`-এ background থাকে বাইরে। দুই framework-এ লেখা প্রায় একই, কিন্তু ছবি উল্টো। নিয়মটা মনে না থাকলে Preview-তে দেখে নিন।

**Best approach:** যে জিনিসে tap করা যায়, সেখানে `.onTapGesture` না দিয়ে `Button` ব্যবহার করুন। `Button` নিজেই অনেক কিছু সামলায়: accessibility (VoiceOver বলে "button"), চাপা অবস্থার চেহারা, keyboard। Flutter-এ `GestureDetector`-এর বদলে `InkWell` বা `TextButton` নেওয়ার মতোই।

[উপরে ফিরুন](#toc)

### <a id="ios5-4"></a>iOS ৫.৪ `ListView.builder` → `List` আর `LazyVStack`

**এক লাইনে:** পথ দুইটা।
- `List` — iOS-এর চেনা চেহারার list। swipe-to-delete, pull-to-refresh সব তৈরি করা থাকে।
- `ScrollView` + `LazyVStack` — নিজের ডিজাইনের list। শুধু যে অংশ screen-এ দেখা যাচ্ছে, সেটুকুই বানায়।

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
| `ListView(children:)` (সব একসাথে বানায়) | `ScrollView` + `VStack` | `Column` + `verticalScroll` |
| `Key` / `ValueKey(id)` | `Identifiable` বা `ForEach(..., id: \.id)` | `items(key = { it.id })` |
| `RefreshIndicator` | `.refreshable { }` | `PullToRefreshBox` |
| `Dismissible` | `.swipeActions { }`, `.onDelete` | `SwipeToDismissBox` |
| `ScrollController.animateTo` | `ScrollViewReader` / `.scrollPosition(id:)` | `rememberLazyListState()` |
| `SliverAppBar` + search | `.navigationTitle` + `.searchable(text:)` | `TopAppBar` + `SearchBar` |

**কখন কোনটা নেবেন:** Settings-এর মতো, iOS-এর চেনা চেহারার list হলে নিন `List`। Card-এর feed বা নিজের ডিজাইন হলে নিন `LazyVStack`। `List` নিজে অনেক কিছু দেয় (separator, selection, edit mode, swipe)। কিন্তু এর চেহারা বদলানো কঠিন।

**ফাঁদ — `ScrollView` + `VStack`।** `VStack` lazy না। ১০০০টা note থাকলে ১০০০টাই একসাথে বানায়। এটা Flutter-এ `ListView(children: [...])`-এ বিশাল একটা list দেওয়ার মতো। বড় list-এ সবসময় `List` বা `LazyVStack` নিন।

**ফাঁদ — id যেন না বদলায়।** `ForEach(notes, id: \.self)` লিখলে, বা index দিয়ে id দিলে, note-এর লেখা বদলালেই SwiftUI ভাবে এটা নতুন item। ফলে state হারিয়ে যায়, animation ভুল হয়। তাই database-এর id দিন, যেটা কখনো বদলায় না ([iOS ৫.১০](#ios5-10))।

[উপরে ফিরুন](#toc)

### <a id="ios5-5"></a>iOS ৫.৫ `setState` → `@State`

**এক লাইনে:** `StatefulWidget`-এর field আর `setState`-এর জায়গায় লিখুন `@State private var`। মান বদলালেই `body` আবার চলে। আলাদা কোনো call লাগে না।

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

**View তো struct, প্রতিবার নতুন করে তৈরি হয়। তাহলে `isPinned` টিকে থাকে কীভাবে?**
- `@State`-এর মান struct-এর ভেতরে থাকে না।
- SwiftUI মানটা রাখে তার নিজের graph-এ, এই view-এর identity-র সাথে বেঁধে।
- Struct-এর ভেতরে থাকে শুধু ওই মানের একটা reference।

Flutter-এও ঠিক এটাই হয়। Widget নতুন হয়, কিন্তু `State` object Element-এর সাথে বাঁধা থাকে, তাই টিকে যায়। Compose-এ এই কাজটা করে `remember`।

| | Flutter | SwiftUI | Compose |
|---|---|---|---|
| Local state | `State`-এর field | `@State private var` | `remember { mutableStateOf() }` |
| বদলানো | `setState(() => x = y)` | `x = y` | `x = y` |
| কোথায় বেঁচে থাকে | Element-এর সাথে বাঁধা `State` object | SwiftUI-র graph-এ, view identity-র সাথে | composition-এ `remember` slot |
| কে আবার চলে | যার `setState`, তার `build()` | যে `body` মানটা পড়েছে | যে composable মানটা পড়েছে |

**Best approach:** `@State` সবসময় `private` রাখুন। এটা এই view-এর নিজের state, বাইরে থেকে দেওয়ার জিনিস না। বাইরে থেকে মান লাগলে `let` property নিন। আর সেই মান বদলাতেও হলে নিন `@Binding` ([iOS ৫.৬](#ios5-6))।

**ফাঁদ — `body`-তে side effect।** `body` যেকোনো সময়, যতবার খুশি চলতে পারে। তাই network call, analytics, বা `@State` বদলানো — এগুলো সরাসরি `body`-তে লিখবেন না। এটা Flutter-এর সেই নিয়মটাই: `build()`-এ API call করবেন না। কাজ শুরু করার ঠিক জায়গা `.task` আর `.onAppear` ([iOS ৫.৯](#ios5-9))।

[উপরে ফিরুন](#toc)

### <a id="ios5-6"></a>iOS ৫.৬ `@Binding` — lifting state up

**এক লাইনে:** Flutter-এ child-কে দুইটা জিনিস দিতেন: একটা value, আর একটা `onChanged` callback। SwiftUI-তে দুটো মিলে একটাই জিনিস: **`Binding`**। এর মানে "এই মানটা পড়ো, আর বদলাতে চাইলে এখানে লেখো"। এটা বানানো হয় `$` চিহ্ন দিয়ে।

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

- `title` লিখলে পান মানটা। `$title` লিখলে পান binding।
- `TextField`-এর জন্য `TextEditingController` লাগে না। Binding দিলেই দুই দিকে কাজ করে। User লিখলে মান বদলায়, আর code মান বদলালে field-এর লেখা বদলায়।
- Preview বা test-এ একটা binding বানাতে লিখুন `.constant("বাজার")`।

| Flutter | SwiftUI | Compose |
|---|---|---|
| `value` + `onChanged` | `@Binding var value` | `value` + `onValueChange` |
| `TextEditingController` | `TextField(text: $title)` | `TextField(value, onValueChange)` |
| parent-এ state | parent-এ `@State` | parent-এ `remember` |

**ফাঁদ:** `@Binding` আর `@State` গুলিয়ে ফেলা। Child-এ `@State var title` লিখে parent থেকে মান দিলে, শুধু প্রথম মানটাই থাকবে। Parent পরে মান বদলালেও child সেটা পাবে না। কারণ `@State` initial value নেয় মাত্র একবার। এটা Flutter-এ `initState`-এ `widget.value` কপি করে রেখে দেওয়ার মতো। তাই child যদি মানের মালিক না হয়, তাহলে নিন `@Binding` বা `let`।

[উপরে ফিরুন](#toc)

### <a id="ios5-7"></a>iOS ৫.৭ `ChangeNotifier` / Cubit → `@Observable`

**এক লাইনে:** Screen-এর state আর logic যে class-এ রাখেন, তার মাথায় `@Observable` লিখুন (iOS 17+)। View যে property পড়ে, শুধু সেটা বদলালেই view আবার আঁকা হয়। `notifyListeners()` বা `emit` লাগে না।

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

**Model কাকে কীভাবে দেবেন — নিয়মগুলো:**

| অবস্থা | লিখবেন | Flutter-এ |
|---|---|---|
| এই view-ই model-এর মালিক (বানায়, বাঁচিয়ে রাখে) | `@State private var model = ...` | `BlocProvider(create:)` |
| শুধু পড়বে | `let model: NotesListModel` বা `var model` | `context.watch` / `BlocBuilder` |
| পড়বে, আর property-তে binding-ও লাগবে (`TextField`) | `@Bindable var model: NoteEditorModel` | — |
| দূরের অনেক view-কে দেবেন | `.environment(model)` + `@Environment(NotesListModel.self)` ([iOS ৫.৮](#ios5-8)) | `BlocProvider` + `context.read` |

**ভেতরে কীভাবে কাজ করে:**
1. `@Observable` একটা macro। এটা প্রতিটা property-র getter আর setter-এ নিজের code যোগ করে, যাতে কে পড়ল আর কে বদলাল তা track করা যায়।
2. `body` চলার সময় SwiftUI মনে রাখে, ঠিক কোন কোন property পড়া হলো।
3. পরে শুধু সেই property-গুলো বদলালেই এই view-এর `body` আবার চলে।

যেমন `searchText` বদলালে, যে view শুধু `phase` পড়ে, সে আবার চলে না।

এটা `ChangeNotifier`-এর চেয়ে বেশি নিখুঁত। `notifyListeners()` সব listener-কে খবর দেয়। BLoC-এ `buildWhen` বা `select` দিয়ে হাতে বেছে দিতে হয়। `@Observable` এই কাজটা নিজেই করে, প্রতিটা property আলাদা করে ধরে।

**পুরনো পথ (চিনে রাখুন, iOS 13–16):**

```swift
final class OldNotesViewModel: ObservableObject {
    @Published var notes: [Note] = []                 // বদলালে পুরো object "বদলেছে" বলে
}

@StateObject private var vm = OldNotesViewModel()    // মালিক
@ObservedObject var vm: OldNotesViewModel             // শুধু দেখে
@EnvironmentObject var vm: OldNotesViewModel          // environment থেকে
```

`ObservableObject`-এ যেকোনো একটা `@Published` বদলালেই ওই object দেখা সব view আবার চলত। কোন property বদলাল, সেটা দেখা হতো না — `ChangeNotifier`-এর মতো। Interview-এ প্রায়ই আসে "`@StateObject` আর `@ObservedObject`-এর পার্থক্য কী"। উত্তর:
- প্রথমটা মালিক। Object একবার বানায় আর বাঁচিয়ে রাখে।
- দ্বিতীয়টা শুধু দেখে। Parent rebuild করলে নতুন object পেয়ে যেতে পারে।

**Best approach (iOS 17+):**
- প্রতিটা screen-এর জন্য একটা `@MainActor @Observable final class`।
- View-এর `@State`-এ সেটার মালিকানা।
- Repository দিন init-এ, যাতে test-এ fake দেওয়া যায়।

Architecture-এর পুরো গল্প পরের অধ্যায়গুলোতে।

**ফাঁদ — `@State`-এর initial value বারবার তৈরি হয়।** ধরুন লিখলেন `@State private var model = NotesListModel(...)`। Parent যতবার এই view-এর struct বানায়, ততবার `NotesListModel(...)` call হয়। SwiftUI প্রথম object-টা রাখে, বাকিগুলো ফেলে দেয়। কিন্তু init-এর খরচ আর side effect প্রতিবারই হয়। তাই model-এর `init`-এ network call বা ভারী কাজ রাখবেন না। Load করুন `.task`-এ, ওপরের উদাহরণের মতো।

[উপরে ফিরুন](#toc)

### <a id="ios5-8"></a>iOS ৫.৮ `InheritedWidget` / Provider → `@Environment`

**এক লাইনে:** Tree-র ওপর থেকে নিচের সব view-এ কিছু পৌঁছাতে চাইলে ওপরে `.environment(...)` দিন, আর নিচে `@Environment` দিয়ে পড়ুন। এটা `Theme.of(context)` আর `Provider.of(context)`-এর কাজ করে।

**System-এর দেওয়া মান পড়া:**

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

**ফাঁদ — object না দিলে crash।** আপনি `@Environment(NotesStore.self)` পড়লেন, কিন্তু ওপরে কেউ `.environment(store)` দেয়নি। তখন app crash করে। এটা Flutter-এর `ProviderNotFoundException`-এর মতো, তবে এখানে runtime-এ সোজা crash। Preview-তেও object দিতে ভুলবেন না।

**Best approach:** পুরো app যা ব্যবহার করে (store, setting), সেগুলো environment-এ রাখুন। Screen-এর নিজের model সরাসরি init-এ দিন। তাহলে কোন view কী চায়, সেটা পরিষ্কার থাকে।

[উপরে ফিরুন](#toc)

### <a id="ios5-9"></a>iOS ৫.৯ `initState`, `dispose`, `StreamBuilder` → `.task`, `.onAppear`, `.onChange`

**এক লাইনে:**
- Screen খুললে async কাজ শুরু করতে: `.task { }`। Screen চলে গেলে কাজটা **নিজেই cancel** হয়।
- কোনো মান বদলালে কিছু করতে: `.onChange(of:)`।
- Id বদলালে কাজ আবার শুরু করতে: `.task(id:)`।

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

**SwiftUI-তে — একই কাজ, একটাই modifier দিয়ে:**

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

- View screen-এ দেখা যাওয়ার আগেই `.task` শুরু হয়।
- View চলে গেলে task cancel হয়, আর `for await` loop থেমে যায়। `dispose`-এ `cancel()` লিখতে হয় না।
- `noteID` বদলালে পুরনো task cancel হয়, আর নতুনটা শুরু হয়। এটাই `didUpdateWidget`-এর কাজ।

(এখানে ধরে নিচ্ছি `watchNote(id:)` repository-র একটা function, যেটা `AsyncStream<Note>` দেয় — [iOS ২.৮](#ios2-8)।)

| Flutter | SwiftUI | Compose |
|---|---|---|
| `initState` (async কাজ) | `.task { }` | `LaunchedEffect(Unit)` |
| `initState` (sync কাজ) | `.onAppear { }` | `LaunchedEffect` / `SideEffect` |
| `dispose` | `.task` নিজেই cancel হয়; `.onDisappear { }` | `DisposableEffect { onDispose { } }` |
| `didUpdateWidget` | `.task(id:)`, `.onChange(of:)` | `LaunchedEffect(key)` |
| `StreamBuilder` | `.task { for await ... }` + `@State` | `collectAsStateWithLifecycle()` |
| `FutureBuilder` | `.task { value = await ... }` + `@State` | `LaunchedEffect` + state |

**`.onChange` (iOS 17-এর রূপ):**

```swift
.onChange(of: model.searchText) { oldValue, newValue in
    analytics.log("search", newValue)
}
```

**`.onAppear` বনাম `.task`:** `.onAppear` sync, আর এটা cancel হয় না। এর ভেতর থেকে `Task { }` চালালে screen চলে যাওয়ার পরেও সেটা চলতে থাকবে। তাই async কাজ সবসময় `.task`-এ দিন।

**ফাঁদ — `.onAppear` একাধিকবার চলে।** Navigation-এ পেছনে গিয়ে আবার ফিরলে, বা tab বদলালে, এটা আবার চলে। অথচ Flutter-এর `initState` চলত একবারই। কোনো কাজ "শুধু প্রথমবার" করতে চাইলে model-এ একটা flag রাখুন, বা `.task`-এর ভেতরে check করুন।

[উপরে ফিরুন](#toc)

### <a id="ios5-10"></a>iOS ৫.১০ View identity — Flutter-এর `Key`

**এক লাইনে:** SwiftUI কোন view-কে "আগের সেই একই view" ধরবে, সেটাকে বলে **identity**।
- Identity একই থাকলে `@State` টিকে থাকে, আর বদলগুলো animate হয়।
- Identity বদলালে পুরনো view মুছে যায়, নতুন একটা view তৈরি হয়। State আবার শূন্য থেকে শুরু হয়।

Identity দুই রকম:
- **Structural** — tree-তে view কোন জায়গায় আছে, তা দিয়ে ঠিক হয়। `if`-এর শাখা আর `else`-এর শাখা দুইটা আলাদা জায়গা।
- **Explicit** — আপনি নিজে দেন: `ForEach`-এর id, আর `.id(...)` modifier।

**Flutter-এর সাথে মিল:** Flutter-এ Element আবার ব্যবহার হয়, যদি একই জায়গায় একই `runtimeType` আর একই `Key` থাকে। Key বদলালে State নতুন হয়। SwiftUI-র ধারণা হুবহু এটাই।

**ফাঁদ ১ — শুধু চেহারা বদলাতে `if/else` লেখা:**

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

**ফাঁদ ২ — অন্য note খুললেও পুরনো state থেকে যায়:**

```swift
NoteEditorView(note: selectedNote)
    .id(selectedNote.id)          // note বদলালে editor নতুন করে জন্মায়, পুরনো draft থাকে না
```

Flutter-এ ঠিক এই কাজটা করতেন `NoteEditor(key: ValueKey(note.id))` দিয়ে।

**ফাঁদ ৩ — ForEach-এ এমন id, যা বদলে যায়।**
- `id: \.self` দিলে পুরো value-টাই id হয়। Note-এর title বদলালেই id বদলায়, আর row নতুন করে তৈরি হয়।
- Array index দিলে, মাঝখান থেকে একটা মুছলেই পরের সবার id সরে যায়।
- তাই সবসময় database-এর id দিন, যেটা কখনো বদলায় না।

[উপরে ফিরুন](#toc)

### <a id="ios5-11"></a>iOS ৫.১১ Animation

**এক লাইনে:** State বদলানোর code-টা `withAnimation { }`-এর ভেতরে লিখুন। তাহলে সেই বদলের ফলে যা যা বদলায়, সব animate হয়। Controller, ticker, `vsync` — কিছুই লাগে না।

**Flutter-এ:**

```dart
AnimatedContainer(
  duration: const Duration(milliseconds: 300),
  color: isPinned ? Colors.yellow : Colors.white,
  child: NoteRow(note: note),
)
```

**SwiftUI-তে — তিনটা পথ:**

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
| `AnimatedList` | `List`/`ForEach`-এ `withAnimation`-এর ভেতরে insert/delete | `Modifier.animateItem()` |
| `Hero` | `matchedGeometryEffect`, `.navigationTransition(.zoom)` (iOS 18) | `SharedTransitionLayout` |
| `Curves.easeInOut` | `.easeInOut`, `.spring`, `.bouncy` | `tween`, `spring` |

**ভেতরে কীভাবে কাজ করে:** `withAnimation`-এর ভেতরে state বদলালে SwiftUI পুরনো UI আর নতুন UI-র মধ্যে পার্থক্য বের করে। Position, রং, opacity — যেগুলো animate করা যায়, সেগুলো মাঝের মানগুলো দিয়ে ধাপে ধাপে আঁকে। এজন্যই identity জরুরি ([iOS ৫.১০](#ios5-10))। Identity একই থাকলে animation হয় "move"। Identity বদলালে SwiftUI ধরে নেয় একটা view গেল আর আরেকটা এল, তাই animation হয় fade।

**ফাঁদ:** value না দিয়ে `.animation(.default)` লেখা। এটা পুরনো API, deprecated। এতে parent-এর যেকোনো বদলেই animation হয়, আর UI অদ্ভুতভাবে লাফায়। সবসময় `value:` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios5-12"></a>iOS ৫.১২ Hot reload নেই: Preview

**এক লাইনে:** SwiftUI-তে Flutter-এর মতো hot reload নেই। তার জায়গায় আছে Xcode-এর **Preview**। এটা code-এর পাশেই view-টা চালিয়ে দেখায়, আর প্রতিটা বদলের সাথে নতুন করে দেখায়।

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

- এক file-এ যতগুলো খুশি `#Preview` রাখা যায় — light/dark, ছোট/বড় font, empty/error অবস্থা।
- Preview-তে tap আর scroll করা যায়।
- Preview-তে fake repository দিন। আসল network ব্যবহার করবেন না।

| Flutter | SwiftUI | Compose |
|---|---|---|
| Hot reload (চলমান app-এর ভেতরে) | Preview (app-এর বাইরে, আলাদা জায়গায়) | `@Preview` (+ Live Edit) |
| Widgetbook / golden test | একাধিক `#Preview` | একাধিক `@Preview` |

**বাস্তব কথা:** Preview খুব কাজের। কিন্তু বড় project-এ মাঝে মাঝে এটা ধীর হয়ে যায় বা ভেঙে যায়। কারণ প্রায়ই দুইটার একটা: environment-এ object দেওয়া হয়নি, বা view আসল database ছুঁয়েছে। View ছোট রাখুন, আর dependency init-এ নিন। তাহলে Preview ঠিকঠাক চলে।

[উপরে ফিরুন](#toc)

### <a id="ios5-13"></a>iOS ৫.১৩ UIKit চিনে রাখুন — `UIViewController` আর Auto Layout

SwiftUI-র আগে iOS-এর UI framework ছিল **UIKit**। এটা imperative, Android-এর পুরনো View system-এর মতো। আজও অনেক app-এর বড় অংশ UIKit-এ লেখা। প্রায় সব Flutter plugin-এর UI অংশও UIKit-এ। আর সবচেয়ে জরুরি কথা: **`FlutterViewController` নিজেই একটা `UIViewController`।** তাই UIKit না চিনলে Flutter-এর iOS দিকটা পুরো বোঝা যায় না।

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

- `viewDidLoad` — একবারই চলে। এটা Flutter-এর `initState`।
- `viewWillAppear` / `viewDidAppear` — screen যতবার দেখা যায়, ততবার চলে। Navigation-এ পেছন থেকে ফিরে এলেও আবার চলে।
- `viewIsAppearing` (iOS 17-এ এসেছে, Xcode 15 দিয়ে build করলে iOS 13 পর্যন্ত চলে) — এই সময় size আর trait জানা থাকে, কিন্তু view এখনো screen-এ দেখা যায়নি। যে কাজ layout-এর ওপর চলে, সেটার ঠিক জায়গা এটা।
- Rotation-এ কিছু মরে না। শুধু `viewWillTransition(to:with:)` call হয়, আর layout আবার হয়।

**Auto Layout এক নজরে:**
- View-এর জায়গা সরাসরি না দিয়ে আপনি **constraint** দেন। যেমন: "এর top, ওর bottom থেকে ৮ point নিচে"।
- System সব constraint একসাথে নিয়ে একটা সমীকরণ সমাধান করে, আর প্রতিটা view-এর frame বের করে।
- Constraint কম হলে view কোথায় বসবে, system বুঝতে পারে না।
- Constraint বেশি হলে বা একটা আরেকটার বিরুদ্ধে গেলে console-এ আসে "Unable to simultaneously satisfy constraints"।

এটা Flutter-এর constraint-based layout থেকে আলাদা। Flutter-এ parent শুধু এক দিকে, নিচের দিকে constraint পাঠায়। এখানে সব constraint মিলে একটা সমীকরণ তৈরি হয়।

**দুই framework জোড়া দেওয়া — plugin লেখকদের জন্য জরুরি:**

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
> - Widget হয়ে যায় `struct ...: View` + `body`। Wrapper widget হয়ে যায় modifier। Modifier পড়ুন ভেতর থেকে বাইরের দিকে।
> - `@State` (view-এর নিজের, `private`) → `@Binding` (`$` দিয়ে, অন্যের মান) → `@Observable` (screen-এর model, iOS 17+) → `@Environment` (দূরের সব view-এর জন্য)।
> - Async কাজ `.task`-এ দিন। Screen চলে গেলে এটা নিজেই cancel হয়। `.task(id:)` হলো `didUpdateWidget`-এর কাজ।
> - Identity হলো Flutter-এর `Key`। `if/else` দিয়ে চেহারা বদলাবেন না, মান বদলান। State reset করতে `.id()` দিন।
> - `FlutterViewController` একটা `UIViewController`। তাই UIKit-এর lifecycle আর Auto Layout চিনে রাখুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "SwiftUI-তে view একটা হালকা struct, Flutter-এর widget-এর মতো। State থাকে SwiftUI-র নিজের graph-এ, view-এর identity-র সাথে বাঁধা — যেভাবে Flutter-এ State বাঁধা থাকে Element-এর সাথে। আমি local state-এ `@State` দিই, child-কে দিই `@Binding`, আর screen-এর logic রাখি `@Observable` model-এ। `@Observable` প্রতিটা property আলাদা করে track করে। তাই কোনো property বদলালে শুধু সেই view-গুলোই আবার আঁকা হয়, যারা ওটা পড়েছে। Async কাজ চালাই `.task`-এ, যাতে view চলে গেলে কাজটা নিজেই cancel হয়।"
> - *English:* "In SwiftUI a view is a lightweight struct, like a Flutter widget. State lives in SwiftUI's own graph, tied to the view's identity — the way Flutter ties State to the Element. I use `@State` for local state, `@Binding` for children, and keep screen logic in an `@Observable` model. Observation tracks per property, so only views that read a changed property redraw. I start async work in `.task`, so it cancels itself when the view goes away."

[উপরে ফিরুন](#toc)

---
## <a id="ios6"></a>iOS ৬. Navigation — `go_router`-এর জায়গায় `NavigationStack`

পুরনো iOS-এ নতুন screen খুলতে লিখতেন `navigationController?.pushViewController(...)`। নতুন screen-এ data পাঠাতে তার property set করতেন। আর ফল ফেরত আনতে delegate লাগত। SwiftUI প্রথম দিকে দিয়েছিল `NavigationView` আর `NavigationLink(destination:)`। এতে navigation-এর code view-এর ভেতরে ছড়িয়ে থাকত, আলাদা করে এক জায়গায় আনা কঠিন ছিল।

iOS 16-এ এল **`NavigationStack`**, আর ছবিটা পুরো বদলে গেল। এখন back stack একটা সাধারণ array। এই array আপনি নিজে রাখেন। ধারণাটা Flutter-এর Navigator 2.0-এর `pages` list-এর মতো। Android-এর Navigation 3-এর back stack-ও একই রকম ([অধ্যায় ৭](#ch7))।

### <a id="ios6-1"></a>iOS ৬.১ `NavigationStack` আর path

**এক লাইনে:** সব route থাকে একটা `enum`-এ। Back stack হলো একটা `[Route]` array। Push মানে array-তে `append`, pop মানে `removeLast`। কোন route-এ কোন screen খুলবে, সেটা বলে দেন `.navigationDestination(for:)`-এ।

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
- **Back stack আপনার হাতে, একটা array।** `path`-এ যা আছে, screen-এ ঠিক তাই দেখায়। তাই test-এ শুধু `router.path` check করলেই চলে।
- **System back button নেই।** Android-এর মতো আলাদা system back button iOS-এ নেই। তার বদলে `NavigationStack` নিজেই দুটো জিনিস দেয়: navigation bar-এর বাম দিকে "‹ Notes" back button, আর screen-এর বাম কিনারা থেকে swipe। User এভাবে pop করলে `path` নিজে থেকেই ছোট হয়ে যায়।
- **একাধিক type-এর route চাইলে `NavigationPath`।** এটা type-erased path, মানে এর ভেতরে আলাদা আলাদা type রাখা যায় — `Route`, `Folder`, যা খুশি। তবে সব route এক enum-এ রাখলে সাধারণ array-ই সহজ।

**Best approach:**
- সব route এক enum-এ রাখুন, আর enum-টাকে `Hashable` আর `Codable` করুন। Route-এ শুধু id পাঠান, পুরো `Note` না। go_router আর Android-এও এই একই নিয়ম। Screen id পেয়ে নিজেই repository থেকে data load করে।
- Screen-কে `Router` না দিয়ে একটা callback দিন (`onOpenNote: (UUID) -> Void`)। তাতে navigation-এর সব code এক জায়গায় থাকে। Screen-এর Preview আর test-ও সহজ হয়। ছোট app-এ screen নিজে environment থেকে `Router` পড়লেও চলে।
- **Restoration ফ্রি পাবেন:** `Route` যদি `Codable` হয়, তাহলে পুরো `path` encode করে `@SceneStorage`-এ রাখা যায়। এতে system app মেরে ফেললেও user আবার ঠিক একই screen-এ ফেরে ([iOS ৪.৫](#ios4-5))।

**ফাঁদ:** `.navigationDestination(for:)`-কে lazy container-এর (`List`, `LazyVStack`) ভেতরের কোনো row-এ লাগানো। Lazy container একটা row তখনই বানায়, যখন সেটা screen-এ আসে। Row তৈরি না হলে destination-ও register হয় না। তখন push কাজ করে না (Xcode console-এ একটা warning আসে)। তাই এটা stack-এর root view-এ লাগান, ওপরের code-এর মতো।

[উপরে ফিরুন](#toc)

### <a id="ios6-2"></a>iOS ৬.২ Sheet, full-screen cover আর alert

**এক লাইনে:** নিচ থেকে উঠে আসা screen-এর জন্য `.sheet`। পুরো screen ঢাকতে `.fullScreenCover`। ছোট কোনো প্রশ্ন করতে `.alert` বা `.confirmationDialog`। সবগুলোই একটা state দিয়ে চলে। State-এ value থাকলে দেখায়, `nil` বা `false` হলে বন্ধ হয়।

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

**কী আলাদা:** Flutter-এ `showDialog` একটা function। Call করে `await` করেন, আর ফল ফেরত আসে। SwiftUI-তে sheet হলো state-এর চেহারা — state যা বলে, screen-এ তাই দেখায়। ফল আসে callback বা binding দিয়ে। শুরুতে একটু অদ্ভুত লাগবে। কিন্তু লাভও আছে: "sheet খোলা কি না" এখন একটা সাধারণ state। এটা test করা যায়, আবার restore-ও করা যায়।

**ফাঁদ:** একই view-এ কয়েকটা `.sheet(isPresented:)` রাখলেন, আর দুইটা bool একসাথে `true` হলো। তখন একটা sheet দেখাবে, অন্যটা কোনো error ছাড়াই চুপচাপ হারিয়ে যাবে। এক জায়গায় অনেক রকম sheet লাগলে একটা enum বানান: `@State private var sheet: SheetKind?`। তারপর একটাই `.sheet(item: $sheet)` রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ios6-3"></a>iOS ৬.৩ Tab

**এক লাইনে:** নিচের tab bar-এর জন্য `TabView`। iOS 18 থেকে প্রতিটা tab একটা `Tab`। প্রতিটা tab-এর ভেতরে তার নিজের `NavigationStack` থাকে। তাই tab বদলালেও প্রতিটা tab-এর back stack আলাদা থাকে।

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

- Tab বদলালে অন্য tab-এর view আর তার `@State` মুছে যায় না, বেঁচে থাকে। ঠিক Flutter-এর `IndexedStack`-এর মতো।
- একই tab-এ আবার tap করলে iOS user আশা করে, সে root-এ ফিরে যাবে। এটা ঠিকমতো পেতে প্রতিটা tab-এর নিজের `path` রাখুন, আর তখন `notesPath.removeAll()` করুন।

**ফাঁদ:** পুরো `TabView`-কে একটা `NavigationStack`-এর ভেতরে রাখা। তখন push করলে tab bar-সহ পুরো screen সরে যায়। আর সব tab মিলে একটাই stack ব্যবহার করে। ঠিক নিয়মটা উল্টো: `TabView` থাকবে বাইরে, আর প্রতিটা tab-এর ভেতরে থাকবে `NavigationStack`।

[উপরে ফিরুন](#toc)

### <a id="ios6-4"></a>iOS ৬.৪ Deep link — `onOpenURL`

**এক লাইনে:** বাইরে থেকে URL আসতে পারে (`notesapp://note/42` বা `https://notes.byteonyx.com/note/42`)। সেটা ধরতে `.onOpenURL { url in }` লাগান। URL পড়ে একটা `Route` বানান, আর সেটা `path`-এ বসান। Navigation তো শুধু একটা array। তাই deep link মানেও শুধু array বদলানো।

**দুই রকম link:**

| | Custom URL scheme | Universal link |
|---|---|---|
| দেখতে | `notesapp://note/42` | `https://notes.byteonyx.com/note/42` |
| কোথায় লিখবেন | Info.plist-এ `CFBundleURLTypes` ([iOS ৩.৬](#ios3-6)) | Associated Domains entitlement: `applinks:notes.byteonyx.com` ([iOS ৩.৭](#ios3-7)) |
| Server-এ | কিছু না | `https://notes.byteonyx.com/.well-known/apple-app-site-association` file |
| App না থাকলে | কিছু হয় না / error | Website খোলে |
| নিরাপত্তা | অন্য যেকোনো app-ও একই scheme নিজের বলে নিতে পারে | Domain-টা যে আপনার, সেটা প্রমাণ করতে হয় |
| Android-এ | custom scheme intent filter | App Links (`assetlinks.json`) |

**Best:** user-এর হাতে যে link যায় (email, share), সেখানে universal link দিন। App-এর নিজের ভেতরের কাজে (OAuth callback, widget থেকে app খোলা) custom scheme দিলেও চলে।

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

`onOpenURL` দুই রকম link-ই ধরে — custom scheme আর universal link। App বন্ধ থাকলে URL দিয়েই app চালু হয়। তখনও এটা call হয়।

**Flutter-এ এর পেছনে কী ঘটে:**
- Flutter-এর নিজের একটা deep link handler আছে, যেটা default-এ চালু থাকে। iOS কোনো URL দিলে engine সেটা Flutter-এর router-এ (`go_router`) পাঠিয়ে দেয়। আপনি নিজের plugin দিয়ে deep link সামলালে এটা বন্ধ করতে হয়। তার জন্য Info.plist-এ `FlutterDeepLinkingEnabled` = `false` দিন।
- Flutter 3.41+ থেকে app default-এ UIScene দিয়ে চলে। তখন URL আসে SceneDelegate-এ। `FlutterSceneDelegate` সেটা engine আর plugin-এর কাছে পৌঁছে দেয় ([iOS ৪.১](#ios4-1))। নিজের SceneDelegate-এ `scene(_:openURLContexts:)` override করলে ভেতরে `super` call করতে ভুলবেন না। নইলে Flutter link-টা পাবে না।

| go_router | SwiftUI | Navigation Compose |
|---|---|---|
| Path দেখে নিজেই route খুঁজে নেয় | `onOpenURL` + URL থেকে নিজে `Route` বানানো | `navDeepLink { uriPattern = ... }` |
| `context.go(link)` | `router.path = [route]` | `navController.handleDeepLink(intent)` |
| Info.plist / Manifest config | Info.plist + entitlement | Manifest intent filter |

**ফাঁদ:** URL-কে বিশ্বাস করা। যেকোনো app বা website `notesapp://note/...` খুলতে পারে। তাই URL-এর id পেয়েই সরাসরি কোনো কাজ করবেন না — যেমন কিছু মুছে ফেলা, বা কিছু পাঠানো। শুধু screen-টা খুলুন। আসল কাজের আগে user-কে নিজে confirm করতে দিন।

**নিজে test করুন:** Simulator-এ terminal থেকে:

```bash
xcrun simctl openurl booted "notesapp://note/6F9619FF-8B86-D011-B42D-00C04FC964FF"
```

এটা Android-এর `adb shell am start -d "..."`-এর মতোই কাজ করে।

[উপরে ফিরুন](#toc)

### <a id="ios6-5"></a>iOS ৬.৫ তিন framework পাশাপাশি, আর best approach

| কাজ | Flutter (go_router) | iOS (SwiftUI) | Android (Compose) |
|---|---|---|---|
| Route কীভাবে লেখা হয় | path string | `enum Route: Hashable` | `@Serializable` class |
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
- Tab থাকলে `TabView` বাইরে রাখুন। প্রতিটা tab-এ থাকবে তার নিজের `NavigationStack(path:)`।
- সব route একটা `Codable` enum-এ। Argument-এ শুধু id।
- `Router` হবে একটা `@MainActor @Observable` class। Deep link আর code — দুই দিক থেকেই শুধু `path` বদলানো হয়।
- Screen-কে callback দিন। `.navigationDestination` লাগান root-এ।
- Sheet-এর জন্য একটা enum বানিয়ে `.sheet(item:)` ব্যবহার করুন।

> **মনে রাখুন**
> - `NavigationStack(path:)` + `.navigationDestination(for:)`। Back stack একটা সাধারণ `[Route]`।
> - Push = `append`, pop = `removeLast`, root = `removeAll`। Route-এ শুধু id।
> - Sheet আর alert চলে state দিয়ে। `await` করে ফল পাওয়া যায় না, ফল আসে callback দিয়ে।
> - `TabView` বাইরে, প্রতিটা tab-এ নিজের stack।
> - Deep link: `onOpenURL` → `Route` → `path`। User-কে যে link দেবেন, সেটা universal link হোক।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি SwiftUI-তে `NavigationStack`-এ path binding দিয়ে navigation করি। সব route একটা `Hashable`, `Codable` enum, আর back stack একটা array — একটা `@Observable` router-এ রাখা। তাই push, pop, deep link সব শুধু array বদলানো, আর test-এ শুধু array check করি। Route-এ শুধু id পাঠাই, আর path `@SceneStorage`-এ রাখলে system app মারার পরেও user একই screen-এ ফেরে।"
> - *English:* "In SwiftUI I navigate with a `NavigationStack` bound to a path. All routes are one `Hashable`, `Codable` enum, and the back stack is an array kept in an `@Observable` router. So push, pop and deep links are all just array changes, and in tests I only check the array. I pass only ids in routes, and by saving the path in `@SceneStorage` the user comes back to the same screen even after the system kills the app."

[উপরে ফিরুন](#toc)

---

## <a id="ios7"></a>iOS ৭. Architecture — Cubit থেকে `@Observable` view model

Android-এর [অধ্যায় ৮](#ch8)-এ দেখেছেন: layer বদলায় না, শুধু প্রতিটা layer-এর ভেতরের tool বদলায়। iOS-এও একই কথা। তিনটা layer থাকে — presentation, domain, data। Cubit-এর জায়গায় আসে একটা `@Observable` class। `get_it`-এর জায়গায় সাধারণ `init`। আর repository থাকে ঠিক আগের মতোই।

একটা বড় পার্থক্য আগেই বলে রাখি। Android-এ ViewModel একটা বিশেষ class। কারণ phone ঘোরালে (rotation) Activity মরে যায়, আর ViewModel সেটা পার হয়ে বেঁচে থাকে। iOS-এ rotation-এ কিছুই মরে না। তাই iOS-এ "ViewModel" নামে কোনো framework class নেই। এটা আপনার নিজের একটা সাধারণ class, যার গায়ে শুধু `@Observable` লেখা থাকে।

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

**`freezed` state কোথায় গেল?** Flutter-এ Cubit একটা immutable state object `emit` করে। iOS-এ view model-এর property-গুলোই state। `notes`, `isLoading`, `errorMessage` — প্রতিটা আলাদা একটা `var`। SwiftUI জানে, কোন view কোন property পড়ে। কোনো property বদলালে শুধু যে view সেটা পড়ে, সেটাই আবার আঁকা হয়। তাই সব state একটা struct-এ ভরে `copyWith` করার দরকার পড়ে না।

**UseCase নিয়ে:** Android অধ্যায়ের কথা এখানেও খাটে। যে UseCase শুধু repository-র একটা method ডাকে, সেটা বাড়তি layer, লাগে না। UseCase বানান তখনই, যখন তাতে business rule আছে, বা দুইটা repository-র data মেলাতে হয়।

[উপরে ফিরুন](#toc)

### <a id="ios7-2"></a>iOS ৭.২ Cubit → `@Observable` view model

**এক লাইনে:** কোনো class-এর গায়ে `@Observable` লিখলে তার প্রতিটা `var` নিজে থেকেই "observable" হয়ে যায়। SwiftUI view সেই property পড়লেই subscribe হয়ে যায়। `emit` লাগে না, `notifyListeners`-ও লাগে না।

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
1. `@Observable` একটা Swift **macro** ([iOS ১](#ios1))। Macro compile-এর সময় আপনার হয়ে code লেখে। এটা প্রতিটা `var`-এর getter আর setter-এ কিছু লুকানো code বসিয়ে দেয়।
2. SwiftUI যখন `body` চালায়, তখন খেয়াল রাখে কোন কোন property পড়া হলো। এই খেয়াল রাখার কাজটা করে Observation framework (একে tracking বলে)।
3. পরে কোনো property-র setter চললে SwiftUI শুধু সেই view-এর `body` আবার চালায়, যে view ওই property পড়েছিল।
4. যে property `body`-তে পড়া হয়নি, সেটা বদলালে কিছুই আবার আঁকা হয় না। Flutter-এ এর জন্য `BlocBuilder`-এর `buildWhen` হাতে লিখতে হতো। এখানে এটা নিজে থেকেই হয়।

**Version:** `@Observable` আর Observation framework এসেছে iOS 17-এ। তার আগের code-এ দেখবেন `ObservableObject` + `@Published` + `@StateObject`। ওটা চিনে রাখুন, কিন্তু নতুন code-এ লিখবেন না। পুরনো থেকে নতুনে যেতে Apple-এর একটা [migration guide](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro) আছে।

**`@MainActor` কেন:** View model-এর state UI পড়ে। তাই state সবসময় main thread-এ বদলানো উচিত। `@MainActor` লিখলে compiler নিজেই এটা check করে ([iOS ২](#ios2))। Xcode 26 থেকে নতুন project-এ default actor isolation `MainActor` চালু থাকে — মানে আলাদা করে কিছু না বললে code main actor-এ চলে। তবু view model-এ `@MainActor` নিজে লিখে দিন। পড়তে সহজ হয়, আর পুরনো project-এও ঠিকমতো কাজ করে।

**Best approach:** প্রতিটা screen-এর জন্য একটা `@MainActor @Observable final class` বানান। State property-গুলো `private(set)` রাখুন। কাজের method-গুলো `async` করুন। View model-এর মালিক হবে screen-এর view, `@State` দিয়ে। কাজ শুরু করুন `.task`-এ, `init`-এ না।

**ফাঁদ:**
- **`@State`-এর initial value বারবার তৈরি হয়।** Parent view আবার আঁকা হলে `NotesScreen.init` আবার চলে। তাই `NotesViewModel(...)`-ও আবার তৈরি হয়। SwiftUI প্রথমটাই রেখে দেয়, নতুনটা ফেলে দেয়। এজন্য view model-এর `init`-এ network call বা timer চালু করবেন না। সব কাজ `.task`-এ।
- **`@Observable` class-এর জন্য `@StateObject` লিখবেন না।** `@StateObject` পুরনো `ObservableObject`-এর জন্য। `@Observable` class-এর মালিক হতে `@State` দিন।
- **State-কে public `var` রাখবেন না।** তাহলে view নিজেই `viewModel.notes = []` লিখে দিতে পারবে। এটা Cubit-এর বাইরে থেকে `emit` করার মতোই ভুল। তাই `private(set)` দিন।

[উপরে ফিরুন](#toc)

### <a id="ios7-3"></a>iOS ৭.৩ Unidirectional data flow — state নিচে, event ওপরে

**এক লাইনে:** View শুধু দুটো কাজ করে: state দেখায়, আর event পাঠায়। State বদলায় শুধু view model। Flutter-এর BLoC আর Android-এর UDF-ও ঠিক এমন।

```
        ┌──────────── state (notes, isLoading) ────────────┐
        │                                                  ▼
 NotesViewModel                                       NotesScreen (body)
        ▲                                                  │
        └──────── event: await viewModel.delete(note) ─────┘
```

**Route আর Screen আলাদা করুন।** Android-এ দুইটা আলাদা ছিল: `NotesRoute` ViewModel নিত, আর `NotesScreen` ছিল stateless। SwiftUI-তেও একই কাজ করা যায়:

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

`NotesScreen` view model রাখে। সে `NotesListView`-কে শুধু data আর closure দেয়। Flutter-এ `NotesPage` আর `NotesView`-কে যেভাবে ভাগ করতেন, ঠিক তেমন।

**One-off event: `BlocListener` কোথায়?** Snackbar বা alert-এর মতো জিনিস একবারই দেখাতে হয়। Android-এ এদেরও state হিসেবে রাখতে বলা হয়েছিল ([৮.৪](#ch8-4))। SwiftUI-তে এটা আরও সহজে আসে, কারণ alert নিজেই একটা `Binding<Bool>` চায়:

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

Error থাকে state-এ। User alert বন্ধ করলে SwiftUI নিজে binding-এ `false` লেখে। তখন আমরা error মুছে দিই। তাই event হারিয়ে যাওয়ার ভয় নেই।

**State বদল দেখে কিছু করতে হলে** `.onChange(of:)` ব্যবহার করুন। ধরুন নতুন note লেখার screen। `EditNoteViewModel`-এর `didSave` সত্যি হলে আপনি screen বন্ধ করতে চান:

```swift
.onChange(of: viewModel.didSave) { _, didSave in
    if didSave { dismiss() }
}
```

**চিনে রাখুন — TCA:** The Composable Architecture (Point-Free) একটা জনপ্রিয় library। এটা Redux বা BLoC-এর মতো — `State`, `Action`, `Reducer` দিয়ে চলে। বড় team-এর project-এ দেখবেন। শুরুতে এটা লাগবে না।

[উপরে ফিরুন](#toc)

### <a id="ios7-4"></a>iOS ৭.৪ `get_it` → init injection আর `@Environment`

**এক লাইনে:** iOS-এ DI-এর জন্য কোনো framework লাগে না। Dependency সরাসরি `init`-এ পাঠান। যা পুরো app-জুড়ে লাগে, সেটা `@Environment`-এ রাখুন।

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

**iOS-এ — composition root (যে এক জায়গায় সব object তৈরি করে জোড়া লাগানো হয়):**

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

`SessionStore` হলো একটা ছোট `@MainActor @Observable` class। এতে থাকে কে login করেছে, আর তার নাম। যে view-এর এটা দরকার, সে environment থেকে নিজেই তুলে নেয়:

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
| Runtime-এ খুঁজে বের করে (service locator) | Compile time-এ dependency graph বানায় | সাধারণ `init` — compiler নিজেই type check করে |
| `registerLazySingleton` | `@Singleton` | `App`-এ একবার তৈরি করে সবাইকে একই object দেওয়া |
| `registerFactory` | unscoped | প্রতিবার `NotesViewModel(...)` |
| `@LazySingleton(as: Interface)` | `@Binds` | `protocol` + তার একটা implementation |
| `getIt<NotesCubit>()` | `hiltViewModel()` | `@State var viewModel = ...` |
| `Provider` / `InheritedWidget` | `CompositionLocal` | `.environment(obj)` + `@Environment(Type.self)` |
| `@Environment('test')` | `@TestInstallIn` | test-এ fake object দিয়ে `init` ডাকা |

**কোনটা কখন:**
- **Init injection** — repository, API client, view model-এর জন্য। ৯০% ক্ষেত্রে এটাই। কোন class কী চায়, তার signature দেখলেই বোঝা যায়।
- **`@Environment`** — যা অনেক নিচের অনেক view-এর লাগে: login session, theme-এর মতো setting, navigation router। এগুলো প্রতিটা স্তরে হাতে হাতে পাঠাতে হলে বিরক্তিকর হতো। তাই এদের জন্য environment।

**চিনে রাখুন:** বড় project-এ Factory বা Point-Free-এর swift-dependencies-এর মতো DI library দেখবেন। এগুলো `get_it`-এর কাছাকাছি। ছোট আর মাঝারি app-এ এদের দরকার নেই।

**Best approach:** `App` struct-এ একটা composition root রাখুন। সেখানে database, API, repository — প্রতিটা একবার করে তৈরি করুন। তারপর `init` দিয়ে নিচে পাঠান। `@Environment`-এ রাখুন শুধু সেই `@Observable` object, যা সত্যিই পুরো app-এ লাগে।

**ফাঁদ:**
- **`.environment(session)` বসাতে ভুলে গেলে crash।** `@Environment(SessionStore.self)` যদি object না পায়, app runtime-এ crash করে। Flutter-এর "ProviderNotFoundException"-এর মতো, তবে আরও কড়া। Preview-তেও `.environment(...)` দিতে হয়।
- **সব কিছু `@Environment`-এ ঢোকাবেন না।** তাহলে কোন view কী চায়, আর বোঝা যায় না। এটা একটা লুকানো global হয়ে যায় — যেমন সব জায়গা থেকে `get_it` ডাকা।

[উপরে ফিরুন](#toc)

### <a id="ios7-5"></a>iOS ৭.৫ Repository layer

**এক লাইনে:** Repository একটা `protocol`। View model শুধু এই protocol চেনে। আসল implementation database আর network-কে জোড়া দেয়। Test-এ তার বদলে একটা fake দিন।

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

**একটাই implementation, তবু `protocol` কেন?** কারণ test-এ একটা fake লাগবে ([iOS ১০.৩](#ios10-3))। সেই fake-ই হলো সত্যিকারের "দ্বিতীয় implementation"। Fake না থাকলে view model test করতে আসল database আর network লাগত।

**SwiftData-র `@Model` class না নিয়ে `struct Note` কেন?** SwiftData-র model একটা class। এটা database context-এর সাথে বাঁধা, আর এক thread থেকে আরেক thread-এ পাঠানো যায় না। View model আর UI-তে একটা সাধারণ `struct` সহজ, আর নিরাপদ। Database-এর class (`NoteEntity`) data layer-এর ভেতরেই থাকে। Android-এও Room-এর `NoteEntity` আর domain-এর `Note` আলাদা ছিল — নকশা একই। আসল implementation দেখবেন [iOS ৮.৮](#ios8-8)-এ।

**Protocol-এ `@MainActor` কেন?** View model `@MainActor`-এ চলে। Repository-ও main actor-এ থাকলে দুজনের মধ্যে data পাঠাতে `Sendable` নিয়ে ঝামেলা হয় না। ভয় নেই, এতে network call main thread আটকায় না। `await`-এ অপেক্ষার সময় main thread ছাড়া থাকে। আর `URLSession` নিজের thread-এ কাজ করে।

**Best approach:** Repository-র protocol থাকবে domain-এ, implementation থাকবে data-তে। Protocol-এ শুধু domain type (`Note`) ব্যবহার করুন। কখনো `NoteEntity` বা `NoteDTO` না।

**ফাঁদ:** Repository থেকে SwiftData-র `@Model` object সোজা view-এ পাঠানো। কাজ চলবে ঠিকই। কিন্তু তখন view database-এর live object নিজেই বদলে দিতে পারে। আর test করতেও database লাগবে।

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

Android-এর data অধ্যায়ে ([৯](#ch9)) প্রায় প্রতিটা কাজে Jetpack বা Square-এর একটা library লাগত। iOS-এ মজার ব্যাপার হলো, বেশিরভাগ জিনিস Apple-এর নিজের SDK-তেই আছে। Network-এ `URLSession`, JSON-এ `Codable`, database-এ SwiftData, আর secret রাখতে Keychain। কোনো বাইরের dependency ছাড়াই Notes app-এর পুরো data layer বানানো যায়।

### <a id="ios8-1"></a>iOS ৮.১ `dio` → `URLSession` + `async`/`await`

**এক লাইনে:** `URLSession` হলো Apple-এর নিজের HTTP client, SDK-তেই থাকে। `async`/`await` দিয়ে এক লাইনেই request পাঠানো যায়। এতে dio-র মতো interceptor নেই। তাই একটা ছোট wrapper নিজে লিখে নিন।

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

**ভেতরে কীভাবে কাজ করে:** `session.data(for:)` একটা `async` function। Request চলার সময় আপনার task অপেক্ষা করে, কিন্তু main thread আটকায় না। আসল network-এর কাজ `URLSession` নিজের background queue-তে করে। Task cancel হলে request-ও cancel হয় — যেমন `.task`-এর view screen থেকে চলে গেলে। তখন `CancellationError` বা `URLError(.cancelled)` আসে। Flutter-এ এর জন্য `mounted` check করতেন। এখানে সেটা লাগে না।

**চিনে রাখুন — Alamofire:** একে iOS-এর "dio" বলা যায়। Interceptor, retry, upload progress — সব আছে। পুরনো project-এ খুব দেখবেন। তবে `async`/`await` আসার পরে নতুন project-এ প্রায় সব কাজ `URLSession` দিয়েই হয়ে যায়।

**Best approach:** `URLSession` আর একটা ছোট `send()` wrapper। এই wrapper-এ token বসে, আর status check হয়। Library নিন শুধু তখন, যখন সত্যিই জটিল কিছু লাগে।

**ফাঁদ:**
- **404 বা 500-এ কোনো error আসে না।** `URLSession` throw করে শুধু network-এর সমস্যায় — internet নেই, timeout, DNS-এর ভুল। Server 500 ফেরত দিলেও আপনি `data` পেয়ে যাবেন। Dio-র অভ্যাস থেকে এখানেই সবচেয়ে বেশি bug আসে। Status নিজে check করুন।
- **`http://` চলে না।** App Transport Security (ATS) default-এ শুধু HTTPS চলতে দেয়। Local test server-এ যেতে হলে `Info.plist`-এ একটা exception দিতে হয়। Android-এ cleartext traffic বন্ধ থাকার মতোই।
- **সব কাজে `URLSession.shared` না।** বড় file upload বা download, যেটা app বন্ধ হলেও চলতে থাকবে, তার জন্য background session লাগে ([iOS ৯.১](#ios9-1))।

[উপরে ফিরুন](#toc)

### <a id="ios8-2"></a>iOS ৮.২ `json_serializable` → `Codable`

**এক লাইনে:** Type-এর গায়ে `Codable` লিখলেই হয়। JSON-এ লেখা আর JSON থেকে পড়ার code compiler নিজে বানিয়ে দেয়। `build_runner` লাগে না, `.g.dart` file-ও নেই।

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
| অজানা key — বাদ দেয় | `ignoreUnknownKeys = true` লাগে | default-এ বাদ দেয় |
| key নেই, field non-null → error | error | `DecodingError.keyNotFound` |
| `DateTime.parse` নিজে করে | serializer লাগে | `dateDecodingStrategy` নিজে set করতে হয় |

**ভেতরে কীভাবে কাজ করে:** `Codable` আসলে দুইটা protocol — `Decodable` আর `Encodable`। আপনি conformance লিখলে compiler, compile-এর সময়েই, `init(from:)` আর `encode(to:)` বানিয়ে দেয়। Runtime-এ কোনো reflection বা খোঁজাখুঁজি হয় না। তাই এটা দ্রুত। কোনো field-এর জন্য বিশেষ নিয়ম লাগলে `init(from:)` নিজে লিখতে পারেন। তবে তখন বাকি সব field-ও হাতে লিখতে হয়।

**Best approach:** Network-এর জন্য আলাদা `NoteDTO` রাখুন, app-এর ভেতরে `Note`। Key-এর নামের জন্য `CodingKeys` আর `.convertFromSnakeCase` — দুটোর একটা বেছে নিন। তারপর পুরো project-এ সেটাই চালান।

**ফাঁদ:**
- **Date-এর default ঠিক না।** `JSONDecoder`-এর default date strategy হলো `.deferredToDate`। এটা date-কে একটা সংখ্যা হিসেবে পড়ে — ২০০১ সাল থেকে কত সেকেন্ড গেছে। তাই server ISO 8601 string পাঠালে decode fail করে। `.iso8601` দিন।
- **পুরনো iOS-এ `.iso8601` millisecond চেনে না।** ধরুন server পাঠাল `"2026-11-10T09:30:00.123Z"`। iOS 26-এর আগের OS-এ `.iso8601` এটা পড়তে পারে না, fail করে। (Swift 6.2-এর Foundation থেকে fractional seconds পড়া যায়।) App পুরনো iOS-এ চললে একটা `.custom` strategy লাগে। তাতে এমন একটা formatter দিন, যার fractional seconds চালু।
- **একটা field-এর ভুলে পুরো list fail।** ধরুন ১০০টা note-এর একটায় `title` null এল। তখন পুরো `[NoteDTO]` decode-ই throw করে। যে field server কখনো বাদ দিতে পারে, সেটা Optional রাখুন।

[উপরে ফিরুন](#toc)

### <a id="ios8-3"></a>iOS ৮.৩ `drift` → SwiftData (আর Core Data চিনে রাখুন)

**এক লাইনে:** SwiftData হলো Apple-এর database framework, iOS 17 থেকে আছে। Class-এর গায়ে `@Model` লিখলেই সেটা database-এর একটা table হয়ে যায়। SQL লিখতে হয় না।

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

**`.watch()`-এর মতো জিনিস — `@Query`:** View-এর ভেতরে `@Query` লিখুন। তাহলে database বদলালেই list নিজে থেকে নতুন হয়ে যায়:

```swift
struct QuickNotesList: View {
    @Query(sort: \NoteEntity.updatedAt, order: .reverse) private var notes: [NoteEntity]

    var body: some View {
        List(notes) { note in Text(note.title) }
    }
}
```

ছোট app-এর জন্য এটা দারুণ। কিন্তু তখন view সরাসরি database চেনে। মাঝে view model বা repository থাকে না। Notes app-এ sync আর test আছে, তাই আমরা repository দিয়ে পড়ব ([iOS ৮.৮](#ios8-8))। তবে `@Query` চিনে রাখুন। Apple-এর sample-এ সব জায়গায় এটা পাবেন।

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

**ভেতরে কীভাবে কাজ করে:**
- `@Model` একটা macro। এটা আপনার class-কে `PersistentModel` বানায়, আর প্রতিটা property-কে database-এর সাথে জুড়ে দেয়।
- নিচে data থাকে একটা SQLite file-এ, app-এর Application Support folder-এ।
- `ModelContext` সব বদলের হিসাব রাখে — কী insert হলো, কী বদলাল।
- `save()` করলে সব বদল একসাথে disk-এ যায়। Main context নিজেও মাঝে মাঝে auto-save করে। কিন্তু সেটার ওপর ভরসা করবেন না।

**Core Data — চিনে রাখুন:** SwiftData-র আগে, ২০০৫ সাল থেকে, Apple-এর database ছিল Core Data। SwiftData আসলে Core Data-র পুরনো, পরীক্ষিত storage-এর ওপরেই বানানো। পুরনো project-এ এগুলো দেখবেন:

| Core Data | SwiftData |
|---|---|
| `.xcdatamodeld` file (Xcode-এর visual editor) | `@Model` class, code-এ |
| `NSManagedObject` | `@Model` class |
| `NSPersistentContainer` | `ModelContainer` |
| `NSManagedObjectContext` | `ModelContext` |
| `NSFetchRequest` + `NSPredicate` (string) | `FetchDescriptor` + `#Predicate` (type-safe) |
| `@FetchRequest` (SwiftUI) | `@Query` |

SQL নিজে লিখতে চাইলে third-party GRDB আছে। এটা ব্যবহার করতে অনেকটা drift-এর মতো লাগে।

**Best approach:** নতুন app, আর minimum iOS 17 বা তার বেশি হলে SwiftData নিন। Database-এর `@Model` class data layer-এ রাখুন। বাইরে যাবে domain `struct`।

**ফাঁদ:**
- **Migration ছাড়া model বদলানো।** নতুন optional property, বা default value-সহ property যোগ করলে SwiftData নিজেই ছোট একটা migration (lightweight migration) করে নেয়। কিন্তু default ছাড়া নতুন non-optional property যোগ করলে, বা নাম বদলালে, `ModelContainer` তৈরির সময়েই error দেয়। App চালুর পথে `try!` থাকলে app সরাসরি crash করে। তাই release-এর আগে `VersionedSchema` বানিয়ে রাখুন।
- **`ModelContext` এক thread থেকে আরেক thread-এ যায় না।** এটা `Sendable` না। Main context শুধু main actor-এ চলে। Background-এ বড় import করতে চাইলে `@ModelActor` দিয়ে আলাদা একটা actor বানান। drift-এ যেমন background isolate-এ আলাদা connection খুলতেন, এটাও তেমন।
- **Minimum iOS 17।** Flutter app iOS 15 থেকেও চলে। কিন্তু native code-এ SwiftData বা `@Observable` নিলে আপনার app-এর minimum-ও iOS 17 হয়ে যাবে।

[উপরে ফিরুন](#toc)

### <a id="ios8-4"></a>iOS ৮.৪ `shared_preferences` → `UserDefaults` / `@AppStorage`

**এক লাইনে:** ছোট setting রাখার জায়গা হলো `UserDefaults`। SwiftUI-তে `@AppStorage` দিলে এটা সরাসরি view-এর state-এর মতো কাজ করে।

মজার কথা: Flutter-এর `shared_preferences` iOS-এ ভেতরে ভেতরে `UserDefaults`-ই ব্যবহার করে। মানে এতদিন আপনি না জেনেই এটা চালিয়েছেন।

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

**ভেতরে কীভাবে কাজ করে:** App চালু হলে `UserDefaults` পুরো plist file memory-তে তুলে রাখে। তাই পড়া খুব দ্রুত, আর synchronous। লিখলে system নিজের সুবিধামতো সময়ে disk-এ লেখে। এজন্যই এটা শুধু ছোট জিনিসের জন্য — setting, flag, শেষবার কোন tab খোলা ছিল।

**Privacy manifest:** Apple কিছু API-কে "required reason API" বলে। এগুলো ব্যবহার করলে কেন করছেন, সেটা privacy manifest-এ লিখতে হয়। `UserDefaults` এই তালিকায় আছে। নিজের app-এর data পড়া-লেখার জন্য কারণের code হলো `CA92.1` ([iOS ১১.৫](#ios11-5))।

**Best approach:** ছোট setting হলে view-এ `@AppStorage`, view-এর বাইরে `UserDefaults`। গোছানো (structured) data হলে SwiftData। Secret হলে Keychain।

**ফাঁদ:**
- **Token বা password `UserDefaults`-এ রাখবেন না।** এটা একটা সাধারণ plist file। Keychain-এর মতো আলাদা সুরক্ষা নেই। আর এটা device backup-এও যায়। Jailbreak করা phone-এ, বা backup থেকে, এটা সহজেই পড়া যায়।
- **বড় data রাখবেন না।** পুরো file memory-তে থাকে। এখানে note-এর list রাখলে app-এর memory বাড়ে, আর app চালু হতেও বেশি সময় লাগে।

[উপরে ফিরুন](#toc)

### <a id="ios8-5"></a>iOS ৮.৫ `flutter_secure_storage` → Keychain

**এক লাইনে:** Keychain হলো OS-এর নিজের encrypted storage। Token আর password এখানে রাখুন। আর একটা কথা মনে রাখুন: **app uninstall করলেও Keychain-এর data সাধারণত থেকে যায়।**

`flutter_secure_storage` iOS-এ ভেতরে ঠিক এই Keychain-ই ব্যবহার করে। Android-এ এটা Keystore-এর key দিয়ে data encrypt করত ([৯.৫](#ch9-5))। সেখানে OS-এর কাছে থাকত শুধু key। iOS-এ শুধু key না, পুরো data-টাই OS-এর Keychain-এ যায়।

**Flutter-এ:**

```dart
const storage = FlutterSecureStorage();
await storage.write(key: 'auth_token', value: token);
final token = await storage.read(key: 'auth_token');
```

**iOS-এ:** Keychain-এর API পুরনো, C-এর ধাঁচে লেখা। সব query করতে হয় dictionary দিয়ে। তাই একটা ছোট wrapper লিখে রাখুন:

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

**`kSecAttrAccessible...` কী:** এটা বলে দেয়, item কখন পড়া যাবে।
- `AfterFirstUnlock` মানে: phone চালু হওয়ার পরে user একবার unlock করলেই পড়া যাবে। Background sync-এর জন্য এটাই দরকার, কারণ তখন phone lock অবস্থায় থাকতে পারে।
- `ThisDeviceOnly` মানে: backup থেকে নতুন phone-এ এই item যাবে না।

Token-এর জন্য এটাই ঠিক।

**ফাঁদ — uninstall-এর পরেও থাকে:**

এটা iOS-এর সবচেয়ে বিখ্যাত ফাঁদগুলোর একটা। ধরুন user app মুছে আবার install করল। App-এর database, `UserDefaults`, file — সব নতুন, খালি। কিন্তু Keychain-এ পুরনো token এখনো রয়ে গেছে। ফল দুই রকম হতে পারে:
- User ভাবছে নতুন করে শুরু করছে, অথচ app আগের account-এ login করা অবস্থায় খোলে।
- অথবা পুরনো, বাতিল token দিয়ে পাঠানো প্রথম request-ই 401 পায়।

Android-এ এটা হয় না। Uninstall করলে Keystore-এর key-ও মুছে যায়। আর একটা কথা: Apple কখনো লিখে বলেনি যে Keychain item থেকে যাবে। এটা অনেক দিনের আচরণ, কিন্তু guarantee না। তাই কোনো দিকেই ভরসা করবেন না — "থেকে যাবে", এটাও ধরে নেবেন না; "মুছে যাবে", এটাও না।

সমাধান: প্রথম launch চিনে নিয়ে পুরনো Keychain মুছে দিন:

```swift
// App চালুর একদম শুরুতে, যেমন NotesApp.init()-এ
private func clearKeychainAfterReinstall() {
    let key = "hasLaunchedBefore"
    guard !UserDefaults.standard.bool(forKey: key) else { return }
    Keychain.deleteAll()                              // UserDefaults নতুন, মানে নতুন install
    UserDefaults.standard.set(true, forKey: key)
}
```

এখানে একটা পার্থক্য কাজে লাগছে: uninstall-এ `UserDefaults` মুছে যায়, কিন্তু Keychain যায় না। Flutter-এও `flutter_secure_storage`-এর সাথে ঠিক এই কাজ `shared_preferences` দিয়ে করতে হয়।

**কী মিলল, কী আলাদা:**

| `flutter_secure_storage` | Android | iOS Keychain |
|---|---|---|
| `write` / `read` | Keystore-এর key + Tink দিয়ে encrypt, DataStore-এ রাখা | `SecItemAdd` / `SecItemCopyMatching` |
| uninstall-এ? | মুছে যায় | **সাধারণত থেকে যায়** |
| নতুন phone-এ? | key backup-এ যায় না | `ThisDeviceOnly` হলে যায় না, নইলে encrypted backup-এ যায় |
| দুই app-এ share | না | Keychain access group দিয়ে সম্ভব |

**Best approach:** Token আর secret রাখুন Keychain-এ, `AfterFirstUnlockThisDeviceOnly` দিয়ে। প্রথম launch-এ পুরনো item মুছে দিন। Logout-এ `deleteAll()` ডাকুন।

[উপরে ফিরুন](#toc)

### <a id="ios8-6"></a>iOS ৮.৬ Image: `cached_network_image` → `AsyncImage`

**এক লাইনে:** `AsyncImage` হলো SwiftUI-র নিজের network image (iOS 15 থেকে)। ব্যবহার সহজ, কিন্তু এর নিজের কোনো image cache নেই।

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
- `cached_network_image` ছবি cache করে দুই জায়গায় — memory আর disk। Android-এর Coil-ও তাই করে ([৯.৬](#ch9-6))। `AsyncImage`-এর নিজের কোনো image cache নেই। তাই list-এ scroll করে ফিরে এলে ছবি আবার load হতে পারে।
- Coil view-এর মাপ দেখে ছবিটা ছোট করে decode করে (একে downsampling বলে)। `AsyncImage` পুরো ছবিটাই decode করে। তাই 64pt-এর ছোট thumbnail-এ 4000px ছবি দিলেও পুরো ছবির সমান memory খরচ হয়।

**চিনে রাখুন:** Nuke আর Kingfisher হলো iOS-এর দুই জনপ্রিয় image library। এরা cache, downsampling, prefetch — সব করে। এদের iOS-এর "cached_network_image" বলা যায়।

**Best approach:** অল্প কয়েকটা ছবি বা profile picture হলে `AsyncImage`। ছবিতে ভরা list বা feed হলে Nuke বা Kingfisher।

[উপরে ফিরুন](#toc)

### <a id="ios8-7"></a>iOS ৮.৭ File system আর sandbox

**এক লাইনে:** প্রতিটা iOS app নিজের একটা বন্ধ folder-এ থাকে। একে sandbox বলে। App বাইরের কিছু দেখতে পায় না, অন্য কেউও তার ভেতরে ঢুকতে পারে না। Sandbox-এর ভেতরে কয়েকটা ঠিক করা folder আছে। প্রতিটার নিয়ম আলাদা।

Flutter-এ `path_provider` দিয়ে এই folder-গুলোই পেতেন। কোন `path_provider` function iOS-এ কোন folder দেয়, নিচের table-এ সেটা তার source code দেখে মেলানো হয়েছে:

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
- **পুরো path database-এ রাখবেন না।** App-এর container-এর path-এ একটা random অংশ থাকে। App update বা reinstall-এর পরে সেটা বদলে যেতে পারে। পুরো path রাখলে update-এর পরে সব ছবি "হারিয়ে" যায়। তাই শুধু file-এর নাম রাখুন, আর প্রতিবার folder-এর path-এর সাথে নামটা জুড়ে নিন। Flutter-এও একই নিয়ম।
- **Application Support folder শুরুতে থাকে না।** প্রথমবার `createDirectory` দিয়ে বানিয়ে নিতে হয়। (`path_provider` এটা আপনার হয়ে করে দিত।)
- **বড় download করা file backup-এ পাঠাবেন না।** যে বড় file আবার download করা যায়, সেটা `Caches`-এ রাখুন। নয়তো সেই file-এ `isExcludedFromBackup` চালু করুন। এসব file দিয়ে iCloud backup ভরে ফেললে App Review-তে app আটকে যেতে পারে।
- **Widget বা extension-এর সাথে data share** করতে sandbox-এর বাইরে একটা App Group container লাগে। এটা একটা shared folder, যেটা আপনার app আর তার extension দুজনেই পড়তে পারে।

[উপরে ফিরুন](#toc)

### <a id="ios8-8"></a>iOS ৮.৮ সব একসাথে: offline-first repository

এবার পুরো অধ্যায় জোড়া লাগাই। নকশা Android-এর [৯.৮](#ch9-8)-এর মতোই: database হলো সত্যের উৎস (source of truth)। UI সবসময় database থেকে পড়ে। Network শুধু database-কে update করে।

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

View model-এ শুধু একটা `refresh()` যোগ হয়। আর view-এ যোগ হয় pull-to-refresh:

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

**Android-এর সাথে একটা পার্থক্য:** Room-এর `Flow` query database বদলালে নিজে থেকেই UI-তে নতুন data পাঠাত। এখানে view model প্রতিটা কাজের পরে নিজে `load()` ডাকে। চাইলে `@Query` দিয়ে auto-update পাওয়া যায়। কিন্তু তখন view database-এর সাথে বাঁধা পড়ে যায়। Test সহজ রাখতে আমরা এই সহজ পথটা নিলাম।

**ফাঁদ:**
- **Server-এ মোছা note।** এই code server-এ মোছা note local database থেকে সরায় না। আসল app-এ server থেকে মোছা note-এর একটা তালিকা আনতে হয়। অথবা `updatedSince` দিয়ে, কী কী বদলেছে, তার তালিকা আনতে হয়।
- **Conflict।** দুই device-এ একই note বদলালে কার বদল থাকবে? এখানে নিয়ম সহজ: local বদল আগে server-এ যায়, তারপর server-এর data আসে। দরকার হলে `updatedAt` মিলিয়ে ঠিক করুন কোনটা থাকবে। নিয়ম যাই হোক, সেটা লিখে রাখুন।

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

"এই plugin Android-এ চলে, iOS-এ চলে না" — Flutter-এ এই কথা আপনি নিশ্চয়ই শুনেছেন। Background task চলে না। Push আসে না। Permission চাওয়ার আগেই app crash করে। প্রায় সবসময় দোষ plugin-এর না, দোষটা iOS-এর নিয়ম না জানার। Android-এর [অধ্যায় ১০](#ch10)-এ নিয়মগুলো ছিল ঢিলেঢালা। iOS-এর নিয়ম কড়া। অনেক জায়গায় কী হবে, সেটা পুরোপুরি OS ঠিক করে, আপনি না। এই অধ্যায়ে সেই নিয়মগুলো একটা একটা করে দেখব।

### <a id="ios9-1"></a>iOS ৯.১ `workmanager` → `BGTaskScheduler` (আর কেন iOS-এ এটা অন্যরকম)

**এক লাইনে:** iOS-এ background কাজ আপনি শুধু "চাইতে" পারেন, নিজে "চালাতে" পারেন না। আপনি `BGTaskScheduler`-কে বলেন, "সুযোগ পেলে আমাকে একটু সময় দিও।" কখন সময় দেবে, বা আদৌ দেবে কি না — সেটা iOS ঠিক করে।

**আগে মূল কথাটা:** Android-এ app background-এ গেলেও কিছুক্ষণ চলতে পারে। আর WorkManager কথা দেয়, কাজটা একসময় না একসময় হবেই। iOS-এ এমন না। App background-এ যাওয়ার কয়েক সেকেন্ডের মধ্যেই **suspend** হয়ে যায়। মানে app memory-তে থাকে, কিন্তু code-এর একটা লাইনও চলে না ([iOS ৪](#ios4))। Background-এ code চালানোর পথ একটাই: iOS-এর দেওয়া নির্দিষ্ট কয়েকটা background API। নিচের table-এ সেগুলো আছে।

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

**iOS-এর background API — কোন কাজে কোনটা:**

| কাজ | iOS-এ কী নেবেন | কত সময় পায় | Android-এ কাছাকাছি |
|---|---|---|---|
| মাঝে মাঝে ছোট sync | `BGAppRefreshTask` | অল্প, প্রায় ৩০ সেকেন্ড | periodic WorkManager |
| লম্বা কাজ (database পরিষ্কার, বড় index) | `BGProcessingTask` | কয়েক মিনিট, সাধারণত phone অলস পড়ে থাকলে আর charge-এ থাকলে | WorkManager + charging constraint |
| বড় file upload/download | background `URLSession` | app suspend হলেও OS নিজেই transfer চালিয়ে যায় | WorkManager / DownloadManager |
| User নিজে শুরু করা লম্বা কাজ, progress দেখিয়ে | `BGContinuedProcessingTask` (iOS 26 থেকে) | কাজ শেষ হওয়া বা user বাতিল করা পর্যন্ত | Foreground service |
| App background-এ যাওয়ার মুহূর্তে হাতের কাজ শেষ করা | `beginBackgroundTask` | কয়েক সেকেন্ড বাড়তি | — |
| Server থেকে "নতুন data আছে" জানানো | silent push ([iOS ৯.৩](#ios9-3)) | অল্প, আর iOS সংখ্যা কমিয়ে দেয় (throttle) | FCM data message |

**Flutter-এর `workmanager` iOS-এ কেন "অন্যরকম" চলে:**
1. **কখন চলবে, iOS ঠিক করে।** User কখন app খোলে, battery কেমন, network আছে কি না — এসব দেখে iOS সময় বাছে। Plugin-এর docs নিজেই বলে, Background Fetch সাধারণত দিনে মোটামুটি একবার চলে। তাই `frequency: 1 hour` শুধু আপনার ইচ্ছা, iOS-এর কথা না।
2. **User swipe করে app বন্ধ করলে কিছুই চলে না।** App switcher থেকে app সরিয়ে দিলে আর কোনো background task আসে না। User আবার app খুললে তবেই আসে। Android-এ এমন হতো শুধু Settings-এর "Force stop" চাপলে। iOS-এ সাধারণ একটা swipe-ই যথেষ্ট।
3. **Native setup লাগে।** Info.plist-এ identifier লিখতে হয়, `UIBackgroundModes` দিতে হয়, আর `AppDelegate`-এ register করতে হয়। এগুলো না থাকলে iOS task চালাতেই দেয় না। Dart-এর task name আর Info.plist-এর identifier অক্ষরে অক্ষরে না মিললে error আসে।
4. **Background-এ আলাদা Flutter engine চলে।** Task চলে একটা নতুন engine আর নতুন isolate-এ। তাই সেখানে অন্য plugin (Firebase, `shared_preferences`) ব্যবহার করতে চাইলে `AppDelegate`-এ একটা plugin registrant callback দিতে হয়।
5. **চলতে থাকা task আপনি থামাতে পারেন না।** আর সময় ফুরিয়ে গেলে iOS নিজেই কাজটা মাঝপথে কেটে দেয়।

**Debug করার কৌশল:** Simulator বা device-এ iOS নিজের মর্জিমতো task চালাবে। তাই বসে অপেক্ষা না করে Xcode-এ app pause করুন, তারপর debugger console-এ এটা লিখুন:

```
e -l objc -- (void)[[BGTaskScheduler sharedScheduler] _simulateLaunchForTaskWithIdentifier:@"com.byteonyx.notes.refresh"]
```

**Best approach:** Notes app-এর sync মূলত foreground-এ করুন। মানে: app খুললে, pull-to-refresh করলে, আর save করার সাথে সাথে ([iOS ৮.৮](#ios8-8))। `BGAppRefreshTask` শুধু বাড়তি সুবিধা। চললে ভালো, না চললেও app ঠিকঠাক চলে। বড় attachment upload করতে হলে background `URLSession` নিন।

**ফাঁদ:**
- **Task দেরিতে register করা।** App launch শেষ হওয়ার আগেই handler register করতে হয়। SwiftUI-র `.backgroundTask` modifier এটা নিজেই করে দেয়। UIKit-এ `didFinishLaunchingWithOptions`-এর ভেতরে `BGTaskScheduler.shared.register(...)` ডাকতে হয়।
- **"আমার phone-এ চলে, user-এর phone-এ চলে না।"** User app কতটা ব্যবহার করে, iOS সেটা দেখে শেখে। যে app কম খোলা হয়, সে কম সুযোগ পায়। এটা bug না, iOS ইচ্ছা করেই এমন বানিয়েছে।
- **ঠিক নির্দিষ্ট সময়ের কাজ (যেমন reminder) background task দিয়ে করবেন না।** সেটার জন্য scheduled local notification নিন ([iOS ৯.২](#ios9-2))।

[উপরে ফিরুন](#toc)

### <a id="ios9-2"></a>iOS ৯.২ Local notification — `UNUserNotificationCenter`

**এক লাইনে:** Notification-এর সব কাজ হয় এক জায়গা থেকে — `UNUserNotificationCenter`। Permission চাওয়া, schedule করা, বাতিল করা, সব এখানে। Android-এর মতো channel বানাতে হয় না।

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
| Notification channel বানাতে হয় (Android 8+) | channel নেই; ভাগ করতে চাইলে `UNNotificationCategory` (action button-এর জন্য) |
| Android 13+ `POST_NOTIFICATIONS` runtime permission | `requestAuthorization` — iOS-এ শুরু থেকেই সবসময় চাইতে হয় |
| Exact alarm-এর জন্য আলাদা permission | calendar বা time-interval trigger দিন, আলাদা permission লাগে না |
| App খোলা থাকলেও notification দেখায় | app সামনে খোলা থাকলে **নিজে থেকে দেখায় না** — delegate লাগে |

**App সামনে খোলা থাকলেও banner দেখাতে চাইলে:**

```swift
final class NotificationDelegate: NSObject, UNUserNotificationCenterDelegate {
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification) async -> UNNotificationPresentationOptions {
        [.banner, .sound]
    }
}
// app চালুর সময়: UNUserNotificationCenter.current().delegate = notificationDelegate (strong reference রাখুন)
```

**Best approach:** Reminder-এর জন্য `UNCalendarNotificationTrigger` নিন, আর identifier হিসেবে note-এর id দিন। Permission চাইবেন যখন user প্রথম reminder সেট করে। App খোলার সাথে সাথেই চাইবেন না।

**ফাঁদ:**
- **Pending notification-এর একটা সীমা আছে।** Apple-এর engineer-রা forum-এ বলেছেন, একটা app একসাথে ৬৪টা pending request রাখতে পারে। তাই অনেক note-এ reminder থাকলে, সবচেয়ে কাছের সময়ের কয়েকটাই এখন schedule করুন। বাকিগুলো পরে করুন।
- **Permission একবারই চাওয়া যায়।** User একবার "Don't Allow" চাপলে dialog আর কখনো আসবে না ([iOS ৯.৪](#ios9-4))।
- **Delegate weak।** `UNUserNotificationCenter`-এর `delegate` property weak reference রাখে। মানে delegate object-টা আপনি নিজে কোথাও ধরে না রাখলে সাথে সাথে মুছে যায়। তখন app সামনে থাকা অবস্থায় banner আর আসে না।

[উপরে ফিরুন](#toc)

### <a id="ios9-3"></a>iOS ৯.৩ Push notification — APNs, আর FCM-এর সাথে APNs key

**এক লাইনে:** iOS-এ সব push আসে Apple-এর নিজের server **APNs** (Apple Push Notification service) দিয়ে। FCM ব্যবহার করলেও phone পর্যন্ত শেষ পথটা APNs-ই। তাই Firebase-কে APNs-এর একটা চাবি (APNs key) দিতে হয়।

**পথটা:**

```
আপনার server ──► FCM ──► APNs ──► iPhone (iOS নিজে দেখায়, app চালু থাকা লাগে না)
                  │        ▲
                  │        └── FCM আপনার দেওয়া .p8 key দিয়ে APNs-এ নিজের পরিচয় দেয়
                  └── FCM token → APNs device token (Firebase SDK APNs token FCM-কে দেয়, FCM server জোড়াটা রাখে)
```

Android-এ FCM message phone-এ পৌঁছায় Google Play Services দিয়ে। iOS-এ Google-এর নিজের কোনো পথ নেই। FCM এখানে message শুধু APNs-এর কাছে পাঠিয়ে দেয়। Message phone-এ পৌঁছে দেওয়ার আসল কাজটা করে APNs।

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

**Setup — এর একটা ধাপও বাদ পড়লে push আসবে না:**
1. Xcode-এ target-এর **Signing & Capabilities**-এ গিয়ে **Push Notifications** যোগ করুন। এটা app-এ `aps-environment` entitlement বসিয়ে দেয়।
2. Silent push লাগলে **Background Modes**-এ **Remote notifications** চালু করুন।
3. Apple Developer account-এ **Keys**-এ গিয়ে APNs চালু করে একটা নতুন key বানান। একটা `.p8` file পাবেন। এই file **মাত্র একবার download করা যায়** — তাই নিরাপদ জায়গায় রেখে দিন।
4. Firebase Console → Project settings → Cloud Messaging-এ যান। সেখানে Apple app-এর ঘরে `.p8` file, Key ID আর Team ID দিন।

**APNs key (`.p8`) বনাম পুরনো certificate (`.p12`):**

| APNs auth key (`.p8`) | APNs certificate (`.p12`) |
|---|---|
| এক key দিয়েই team-এর সব app চলে | প্রতিটা app-এর জন্য আলাদা |
| development আর production দুটোতেই চলে | environment অনুযায়ী আলাদা হতে পারে |
| মেয়াদ ফুরায় না (revoke না করলে) | প্রতি বছর নতুন করতে হয় |

**Best approach:** Firebase হোক বা নিজের server — `.p8` APNs key নিন। আর push-এর ভেতরের data-র ওপর ভরসা করবেন না। Push এলে app server থেকে নিজে sync করে নিক।

**ফাঁদ:**
- **Silent push-এর ওপর ভরসা করা।** `content-available: 1` দেওয়া push (FCM-এর data-only message) iOS ইচ্ছামতো কমিয়ে দেয় (throttle করে)। আর user swipe করে app বন্ধ করলে এটা আসেই না। তাই Android-এর FCM data message-এর মতো এর ওপর ভরসা করা যায় না।
- **Sandbox বনাম production।** Xcode থেকে চালানো debug build পায় sandbox APNs-এর token। TestFlight আর App Store build পায় production-এর token। ভুল environment-এ push পাঠালে সেটা হারিয়ে যায়।
- **Simulator-এ test:** আসল server ছাড়াই `xcrun simctl push booted com.byteonyx.notes payload.apns` দিয়ে একটা JSON payload পাঠিয়ে দেখা যায়।

[উপরে ফিরুন](#toc)

### <a id="ios9-4"></a>iOS ৯.৪ `permission_handler` → Info.plist + request API

**এক লাইনে:** iOS-এ প্রতিটা permission-এর দুইটা অংশ। এক, `Info.plist`-এ একটা লেখা, যেটা user-কে বলে "এটা কেন লাগবে" (একে usage description বলে)। দুই, সেই framework-এর নিজের request function। লেখাটা না থাকলে API-তে হাত দেওয়ার সাথে সাথে **app crash করে।**

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

**ছবি বাছাই করতে permission লাগে না।** SwiftUI-র `PhotosPicker` একটা আলাদা system process-এ চলে। App পুরো library দেখতে পায় না, শুধু user যে ছবি বাছে সেটাই পায়। Notes app-এ ছবি যোগ করতে এটাই নিন। Flutter-এর `image_picker`-ও iOS-এ এই system picker-ই ব্যবহার করে।

**Android-এর সাথে পার্থক্য:**

| Android ([১০.৪](#ch10-4)) | iOS |
|---|---|
| Manifest-এ `<uses-permission>` | `Info.plist`-এ usage description (user-কে দেখানো লেখা) |
| Manifest-এ না থাকলে request চুপচাপ fail করে | key না থাকলে **crash** |
| দুইবার deny করার পরে আর dialog আসে না | **একবার** deny করলেই আর আসে না |
| "Don't ask again" বুঝতে rationale API লাগে | `authorizationStatus` দেখলেই বোঝা যায় |

**`permission_handler`-এর iOS setup কেন আলাদা:** Upload করার সময় Apple আপনার binary scan করে দেখে। Code-এ camera API আছে, কিন্তু `Info.plist`-এ key নেই — এমন হলে upload reject হয়। তাই plugin শুধু সেই permission-গুলোর code compile করে, যেগুলো আপনার দরকার। CocoaPods-এর সময় এজন্য `Podfile`-এ macro লিখতে হতো। এখন Swift Package Manager-এ plugin নিজেই `Info.plist` পড়ে ঠিক করে নেয়।

**Best approach:** Permission চান ঠিক যখন user কাজটা করছে। যেমন, user "ছবি তুলুন" বোতাম চাপলে তখন। Usage description-এ আসল কারণটা লিখুন, বাংলায় বা user-এর ভাষায়। "Camera access needed"-এর মতো ঝাপসা লেখা দিলে review-তে reject হতে পারে।

**ফাঁদ:**
- **Key ছাড়া API = crash, শুধু release-এ না, debug-এও।** Console-এ লেখা আসে: app privacy-sensitive data ছুঁতে চেয়েছে, কিন্তু usage description নেই। Flutter-এ নতুন plugin যোগ করে `ios/Runner/Info.plist` আপডেট করতে ভুলে গেলে ঠিক এটাই হয়।
- **User Settings থেকে permission তুলে নিলে iOS app-টা বন্ধ করে দেয় (kill করে)।** পরের বার app নতুন করে চালু হয়। তাই permission-এর অবস্থা memory-তে জমিয়ে (cache করে) রাখবেন না। প্রতিবার নতুন করে check করুন।

[উপরে ফিরুন](#toc)

### <a id="ios9-5"></a>iOS ৯.৫ Deep link — Universal Links বনাম custom URL scheme

**এক লাইনে:** Link দুই রকম। Universal Link হলো আপনার website-এর সাধারণ `https://` link। Phone-এ app থাকলে এটা app-এ খোলে। Custom scheme হলো `notes://`-এর মতো নিজের বানানো link।

**Notes app-এ:** ধরুন কেউ একটা note share করল: `https://notes.byteonyx.com/notes/42`। App install করা থাকলে note-টা সরাসরি app-এ খুলবে। না থাকলে website খুলবে।

**কী মিলল, কী আলাদা:**

| | Universal Link | Custom URL scheme |
|---|---|---|
| দেখতে | `https://notes.byteonyx.com/notes/42` | `notes://notes/42` |
| link-টা যে আপনার, তার প্রমাণ | আছে — domain-এ রাখা একটা file দিয়ে | নেই — যেকোনো app একই scheme নিজের বলে দাবি করতে পারে |
| App না থাকলে | browser-এ website খোলে | কিছুই হয় না, বা error |
| Setup | Associated Domains entitlement + website-এ file | `Info.plist`-এ `CFBundleURLTypes` |
| Android-এ এর জোড়া | App Links (`autoVerify`) | intent-filter-এ নিজের scheme |

**Universal Link setup:**

১. Xcode → Signing & Capabilities → **Associated Domains** → `applinks:notes.byteonyx.com`।

২. Website-এ এই ঠিকানায় একটা file রাখুন: `https://notes.byteonyx.com/.well-known/apple-app-site-association`। নামের শেষে `.json` দেবেন না, আর file-টা HTTPS দিয়ে পাওয়া যেতে হবে:

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

**Flutter-এ:** Flutter 3.27 থেকে Flutter-এর নিজের deep link handling নিজে থেকেই চালু থাকে (`FlutterDeepLinkingEnabled`)। তাই `go_router` link-টা সরাসরি একটা route হিসেবে পেয়ে যায়। `app_links`-এর মতো plugin ব্যবহার করলে এই flag `NO` করে দিতে হয়। তবে দুইটা কাজ Flutter-এও আপনাকে নিজে করতে হয়: Associated Domains যোগ করা, আর website-এ file রাখা।

**Best approach:** Share করা link আর email-এর link-এর জন্য Universal Link নিন। Custom scheme রাখুন শুধু OAuth login-এর redirect-এর মতো জায়গায়, যেখানে link অন্য app-এর হাতে পড়ার ভয় কম।

**ফাঁদ:**
- **Apple-এর CDN file জমিয়ে রাখে (cache করে)।** App নতুন install হলে iOS file-টা সরাসরি আপনার server থেকে নেয় না। নেয় Apple-এর CDN থেকে। Flutter docs বলে, CDN-এ নতুন file পৌঁছাতে ২৪ ঘণ্টা পর্যন্ত লাগতে পারে। তাই file বদলানোর সাথে সাথে কাজ না করলে ঘাবড়াবেন না।
- **Safari-র address bar-এ link লিখলে app খোলে না।** Universal Link কাজ করে শুধু link-এ tap করলে। Test করতে Notes বা Messages-এ link লিখে তাতে tap করুন। অথবা Simulator-এ `xcrun simctl openurl booted <url>` চালান।
- **Personal (free) team-এ Associated Domains চলে না।** এর জন্য paid developer account লাগে।

[উপরে ফিরুন](#toc)

### <a id="ios9-6"></a>iOS ৯.৬ `url_launcher` আর `share_plus`-এর পেছনে

**এক লাইনে:** `url_launcher` iOS-এ ভেতরে ভেতরে `UIApplication.open(_:)` ডাকে। App-এর ভেতরেই browser খুলতে চাইলে ডাকে `SFSafariViewController`। `share_plus` খোলে system-এর share sheet — `UIActivityViewController`। SwiftUI-তে দুটোরই সহজ রূপ আছে।

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
| `launchUrl(tel:)`, `mailto:` | `ACTION_DIAL`, `ACTION_SENDTO` | একই `openURL`; scheme দেখে Phone বা Mail খোলে |
| `canLaunchUrl` | `queries` element (Android 11+) | `LSApplicationQueriesSchemes` (Info.plist) |
| `share_plus` | `ACTION_SEND` + chooser | `ShareLink` / `UIActivityViewController` |

**ফাঁদ:**
- **`canLaunchUrl` iOS-এ `false` দেয়।** `https` ছাড়া অন্য কোনো scheme check করতে চাইলে সেই scheme-টা `Info.plist`-এর `LSApplicationQueriesSchemes`-এ লিখতে হয়। না লিখলে উত্তর সবসময় `false` আসে। `url_launcher`-এর README-তেও এটা লেখা আছে। এটা Android-এর `<queries>`-এর মতোই।
- **iPad-এ share sheet একটা popover।** iPad-এ share sheet ছোট একটা popover হয়ে খোলে। এটাকে screen-এর কোনো একটা জায়গার সাথে আটকে দিতে হয়। `share_plus`-এ এজন্য আছে `sharePositionOrigin`। পুরনো version-এ এটা না দিলে iPad-এ crash হতো। এখন না দিলে screen-এর মাঝখানে দেখায়। তবু ঠিক জায়গাটা দিয়ে দিন। SwiftUI-র `ShareLink` এটা নিজেই সামলায়।

> **মনে রাখুন**
> - Background-এ কী চলবে, iOS ঠিক করে। `BGTaskScheduler` একটা অনুরোধ, কোনো কথা দেওয়া না। User swipe করে app বন্ধ করলে কিছুই চলে না।
> - Notification-এর সব কাজ `UNUserNotificationCenter`-এ। Channel নেই। App সামনে খোলা থাকলে delegate ছাড়া banner আসে না।
> - সব push আসে APNs দিয়ে। FCM ব্যবহার করলে Firebase-এ `.p8` APNs key দিন। Silent push-এর ওপর ভরসা করবেন না।
> - Permission = `Info.plist`-এ usage description + framework-এর request API। Key না থাকলে crash। Dialog জীবনে একবারই আসে।
> - Share করার link-এর জন্য Universal Link। `canLaunchUrl` ঠিক উত্তর দিক, চাইলে scheme-টা `LSApplicationQueriesSchemes`-এ লিখুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS-এ app background-এ গেলে কয়েক সেকেন্ডের মধ্যে suspend হয়ে যায়। তাই background কাজ মানে BGTaskScheduler-এর কাছে একটা অনুরোধ। কখন চলবে, iOS ঠিক করে। আর user app swipe করে বন্ধ করলে কিছুই চলে না। এজন্য Flutter-এর workmanager iOS-এ Android-এর মতো ভরসার না, তাই আমি sync মূলত foreground-এ করি। Push সবসময় আসে APNs দিয়ে। FCM শুধু মাঝখান দিয়ে পাঠায় (relay), তাই Firebase-এ APNs key দিতে হয়। Permission-এর জন্য Info.plist-এ usage description দিতেই হবে, না দিলে app crash করে।"
> - *English:* "On iOS an app gets suspended a few seconds after it goes to the background, so background work is a request to BGTaskScheduler — iOS decides when it runs, and nothing runs if the user swipes the app away. That's why Flutter's workmanager isn't as reliable on iOS as on Android, and I keep the main sync in the foreground. Push always goes through APNs; FCM is only a relay, so Firebase needs the APNs key. For permissions, the usage description in Info.plist is mandatory — without it the app crashes."

[উপরে ফিরুন](#toc)

---

## <a id="ios10"></a>iOS ১০. Testing

Test লেখার মূল নিয়ম এখানেও একই: fake ব্যবহার করুন, mock কম করুন, আর behaviour test করুন। iOS-এ নতুন জিনিস হলো, দুইটা test framework পাশাপাশি চলে। একটা পুরনো **XCTest**। আরেকটা নতুন **Swift Testing** (Xcode 16, ২০২৪ থেকে)। নতুন unit test Swift Testing-এ লিখুন। তবে XCTest-ও চিনে রাখুন। UI test আর পুরনো code-এ এখনো সেটাই চলে।

### <a id="ios10-1"></a>iOS ১০.১ হাতিয়ারের নাম বদল

| Flutter | Android | iOS |
|---|---|---|
| `test()` | JUnit `@Test` | Swift Testing `@Test` |
| `group()` | test class / `@Nested` | `@Suite` struct |
| `expect(a, equals(b))` | `assertEquals(b, a)` | `#expect(a == b)` |
| `setUp()` | `@Before` | suite-এর `init()` |
| `bloc_test` | `runTest` + Turbine | `async` test — `await` করুন, তারপর property দেখুন |
| `fake_async` | `runTest` virtual time | built-in কিছু নেই; সময় বাইরে থেকে দিন (inject) ([নিয়ম](#ios10-3)) |
| `mocktail` | Fake, দরকারে MockK | Fake class (protocol দিয়ে) — mock library কম চলে |
| `testWidgets` | Compose UI test | সরাসরি জোড়া নেই — view model test + XCUITest |
| golden test | Roborazzi / Paparazzi | swift-snapshot-testing (third-party) |
| `integration_test` | instrumented test | XCUITest |
| `flutter test` | `./gradlew test` | Xcode-এ ⌘U, বা `xcodebuild test` |

**Test কোথায় থাকে:** Xcode project-এ test থাকে আলাদা **target**-এ। (Target মানে project-এর ভেতরের একটা আলাদা build-এর জিনিস।) Unit test-এর জন্য একটা target, যেমন `NotesTests`। UI test-এর জন্য আরেকটা, যেমন `NotesUITests`। Flutter project-এর `ios/RunnerTests/` folder-টাও এমন একটা native test target। এটা দিয়ে platform channel বা plugin-এর Swift code test করা হয়। Flutter-এর template এই target এখনো XCTest দিয়ে শুরু করে (`RunnerTests: XCTestCase`)। চাইলে এর পাশে Swift Testing-এর test-ও যোগ করা যায়।

[উপরে ফিরুন](#toc)

### <a id="ios10-2"></a>iOS ১০.২ Swift Testing: `@Test` আর `#expect`

**এক লাইনে:** যেকোনো function-এর ওপরে `@Test` লিখে দিলেই সেটা একটা test। Check করার জন্য macro একটাই — `#expect`। Test fail করলে macro নিজেই দেখিয়ে দেয়, দুই পাশে কোন কোন value ছিল।

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

এখানে ধরে নিচ্ছি, `isBlank` হলো `Note`-এর একটা ছোট computed property:

```swift
extension Note {
    var isBlank: Bool {
        title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty &&
        body.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }
}
```

**কয়েকটা দরকারি জিনিস:**
- **`#require`** — শর্ত না মিললে test সেখানেই থেমে যায়। Optional খুলতেও এটা কাজে লাগে: `let first = try #require(notes.first)`। এটা XCTest-এর `XCTUnwrap`-এর মতো।
- **`arguments:`** — এক test-এ অনেক input (parameterized test)। প্রতিটা input আলাদা test হিসেবে report-এ আসে।
- **`@Suite`** আর struct-এর `init()` — প্রতিটা test নিজের জন্য নতুন একটা instance পায়। তাই `init`-ই আপনার `setUp`-এর কাজ করে। আর এক test-এর state অন্য test-এ যায় না।
- **Default-এ parallel চলে।** Apple-এর docs বলে, Swift Testing একটা suite-এর সব test default-এ একসাথে (parallel) চালায়। XCTest চালাত একটার পর একটা। তাই test-গুলো যদি কোনো global state ভাগ করে, তাহলে এলোমেলোভাবে fail করবে।

**Best approach:** নতুন unit test Swift Testing-এ লিখুন। এক test-এ একটাই behaviour check করুন। Test-এর নাম পুরো বাক্যে লিখুন, চাইলে বাংলায়।

[উপরে ফিরুন](#toc)

### <a id="ios10-3"></a>iOS ১০.৩ `bloc_test` → `@Observable` view model test

**এক লাইনে:** View model-এর method `async`। তাই test-এ method-টা `await` করুন, তারপর property check করুন। এখানে state-এর কোনো stream নেই। তাই Turbine বা `bloc_test`-এর `expect` list লাগে না।

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

**মাঝের state দেখতে চাইলে?** `bloc_test` সব state ক্রম অনুযায়ী দেখাত, যেমন loading আগে `true`, তারপর `false`। এখানে `await` শেষ হলে শুধু শেষ অবস্থাটা পাওয়া যায়। মাঝের অবস্থা দেখতে হলে fake-কে থামিয়ে রাখার ব্যবস্থা লাগে। মানে fake `loadNotes()`-এর ভেতরে অপেক্ষা করবে, যতক্ষণ না test তাকে এগোতে বলে। তবে বেশিরভাগ সময় শেষ অবস্থা দেখাই যথেষ্ট। আর সেটাই আসল behaviour।

**সময় (`fake_async`-এর বদলে):** View model-এ সরাসরি `Date.now` বা `Task.sleep` লিখবেন না। তার বদলে `init`-এ একটা `now: () -> Date` বা `Clock` নিন। Test-এ একটা নির্দিষ্ট সময় দিন। এতে test-কে সত্যি সত্যি অপেক্ষা করতে হয় না।

**ফাঁদ:**
- **`.task`-এর ভেতরের কাজ test করতে চাওয়া।** `.task` view-এর অংশ, view model-এর না। তাই logic রাখুন view model-এর method-এ। View শুধু সেই method ডাকবে। তখন test-ও সরাসরি method-টা ডাকতে পারবে।
- **Method-এর ভেতরে `Task { }` দিয়ে কাজ আলাদা করে চালানো।** ধরুন `func delete()` ভেতরে একটা `Task { ... }` চালু করে, আর নিজে সাথে সাথে ফিরে আসে। তখন test-এর `await` আসল কাজের জন্য অপেক্ষা করে না। তাই method-টা `async` রাখুন। `Task` বানানোর কাজ view-এর।

[উপরে ফিরুন](#toc)

### <a id="ios10-4"></a>iOS ১০.৪ XCTest — চিনে রাখুন

**এক লাইনে:** এটা পুরনো framework। Test লিখতে হয় class-এর ভেতরে। Method-এর নাম `test` দিয়ে শুরু হতে হয়। আর check করার জন্য অনেক রকম `XCTAssert...` আছে।

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

দুইটা framework একই target-এ, এমনকি একই file-এও পাশাপাশি থাকতে পারে। তাই পুরনো সব test একবারে বদলানোর দরকার নেই।

[উপরে ফিরুন](#toc)

### <a id="ios10-5"></a>iOS ১০.৫ `integration_test` → XCUITest

**এক লাইনে:** XCUITest আপনার app-কে একটা আলাদা process থেকে চালায়। তারপর user-এর মতো tap করে, type করে। App-এর ভেতরের code বা data এটা দেখতে পায় না। শুধু screen-এ যা আছে, সেটা accessibility-র মাধ্যমে খুঁজে পায়।

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

App-এর দিকে: launch argument দেখে app test-এর জন্য একটা খালি database নেয়:

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

**Best approach:** View model test লিখুন অনেক। XCUITest লিখুন অল্প কয়েকটা, শুধু সবচেয়ে জরুরি কাজগুলোর জন্য (নতুন note লেখা, খোলা, মোছা)। কারণ XCUITest ধীর, আর ছোট পরিবর্তনেই ভেঙে যায়।

**ফাঁদ:**
- **Text দিয়ে element খোঁজা।** Bangla লেখা বা app-এর ভাষা বদলালেই test ভেঙে যায়। তার বদলে `accessibilityIdentifier` দিন। এটা user দেখে না, VoiceOver-ও পড়ে না।
- **আসল network দিয়ে UI test চালানো।** Server ধীর হলে test কখনো pass, কখনো fail করে (flaky)। Launch argument দিয়ে app-কে fake API বা in-memory data দিন।

> **মনে রাখুন**
> - নতুন unit test Swift Testing-এ: `@Test`, `#expect`, `#require`। Default-এ parallel।
> - View model test: fake repository দিয়ে view model বানান, method `await` করুন, তারপর `#expect`। Turbine লাগে না।
> - XCTest চিনে রাখুন। UI test আর performance test এখনো XCTest-এই হয়।
> - XCUITest app-কে আলাদা process থেকে চালায়। `accessibilityIdentifier` হলো Flutter-এর `Key`-এর মতো।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "নতুন unit test আমি Swift Testing-এ লিখি — @Test আর #expect দিয়ে। এটা default-এ parallel চলে। View model-এর method async, তাই test-এ fake repository দিয়ে view model বানাই, method await করি, তারপর property check করি। bloc_test-এর মতো state-এর stream লাগে না। UI test-এর জন্য XCUITest নিই। এটা app-কে আলাদা process থেকে চালায়, আর accessibility identifier দিয়ে element খোঁজে। Flutter-এর integration_test-এর মতোই, তবে black-box — মানে app-এর ভেতরটা দেখতে পায় না।"
> - *English:* "I write new unit tests with Swift Testing — @Test and #expect — and they run in parallel by default. View model methods are async, so in a test I build the view model with a fake repository, await the method, and then check its properties; I don't need a state stream like in bloc_test. For UI tests I use XCUITest, which drives the app from a separate process through accessibility identifiers. It's like Flutter's integration_test, but black-box."

[উপরে ফিরুন](#toc)

---

## <a id="ios11"></a>iOS ১১. Signing আর release — certificate থেকে App Store

Android-এ release মানে ছিল একটা keystore, একটা AAB, আর Play Console ([অধ্যায় ১২](#ch12))। iOS-এ জিনিস বেশি: bundle id, team, certificate, provisioning profile, entitlement। প্রথমবার এগুলো গুলিয়ে যায়। কিন্তু একবার বুঝলে দেখবেন, প্রতিটার কাজ মাত্র একটা। আর সবগুলো মিলে একটা প্রশ্নের উত্তর দেয়: "কে, কোন app, কোন device-এ, কী কী বিশেষ সুবিধা নিয়ে চালাতে পারবে?"

### <a id="ios11-1"></a>iOS ১১.১ পাঁচ টুকরো: bundle id, team, certificate, provisioning profile, entitlement

**এক লাইনে:** Certificate বলে **কে** sign করছে। Provisioning profile বলে **কোন app, কোন device-এ, কোন বিশেষ সুবিধা নিয়ে** চলবে। iOS দুটো মিলিয়ে দেখে। দুটো মিললে তবেই app চালায়।

| টুকরো | কী | Android-এ কাছাকাছি |
|---|---|---|
| **Bundle ID** | app-এর স্থায়ী নাম, যেমন `com.byteonyx.notes` | `applicationId` |
| **Team** | আপনার Apple Developer account (একজন মানুষ বা একটা company)। এর একটা ১০ অক্ষরের **Team ID** থাকে | Play Console developer account |
| **Certificate** | Apple-এর দেওয়া একটা file, যেটা প্রমাণ করে sign করছেন আপনি। এর private key থাকে আপনার Mac-এর Keychain-এ | upload keystore |
| **Provisioning profile** | Apple-এর sign করা একটা file। এতে লেখা থাকে: এই App ID + এই certificate + (development-এ) এই device-গুলো + এই entitlement | মিল নেই |
| **Entitlement** | app-এর বিশেষ সুবিধা: push, Associated Domains, iCloud, App Groups | Manifest-এর কিছু permission আর feature |

**Certificate দুই রকম:**
- **Apple Development** — নিজের phone-এ Xcode থেকে চালানোর জন্য।
- **Apple Distribution** — TestFlight আর App Store-এর জন্য।

**Provisioning profile কয়েক রকম:**
- **Development** — নির্দিষ্ট কিছু registered device-এ, debug-এর জন্য।
- **Ad Hoc** — নির্দিষ্ট কিছু device-এ release build দেওয়ার জন্য (প্রতি ধরনের device সর্বোচ্চ ১০০টা)।
- **App Store Connect** — TestFlight আর App Store-এর জন্য। এতে device-এর কোনো তালিকা থাকে না। Apple নিজেই app সবার কাছে পৌঁছে দেয়।
- **Enterprise** — শুধু Enterprise Program-এর company-র জন্য, নিজেদের কর্মীদের app দিতে।

**ভেতরে কীভাবে কাজ করে:**
1. Build-এর সময় Xcode আপনার certificate-এর private key দিয়ে app-এর প্রতিটা binary sign করে।
2. Profile-টা app-এর ভেতরে `embedded.mobileprovision` নামে রেখে দেয়।
3. Install-এর সময় iOS চারটা জিনিস check করে: signature কি profile-এর কোনো certificate-এর সাথে মেলে? Bundle ID কি মেলে? এই device কি তালিকায় আছে? App যে entitlement চায়, profile কি সেটার অনুমতি দেয়?
4. একটাও না মিললে app install হয় না, বা চালু হয় না।

**Android-এর সাথে সবচেয়ে বড় পার্থক্য:** Android-এ signing key-ই app-কে চেনায়। Key হারালে (Play App Signing না থাকলে) আর update দেওয়া যায় না। iOS-এ app-কে চেনায় **Bundle ID + Team**। Distribution certificate হারালে বা মেয়াদ ফুরালে নতুন একটা বানিয়ে নিন। App Store-এ থাকা app-এর কিছুই হয় না। Certificate প্রতি বছর বদলায়, এটা স্বাভাবিক।

**ফাঁদ:**
- **Free Apple ID দিয়ে চালানো।** Paid account (বছরে $99) ছাড়াও নিজের phone-এ app চালানো যায়। কিন্তু তখন profile ৭ দিনে শেষ হয়ে যায়। আর push, Associated Domains-এর মতো capability পাওয়া যায় না।
- **Xcode-এ capability যোগ করে profile বদলাতে ভুলে যাওয়া।** Automatic signing-এ Xcode এটা নিজেই করে। Manual signing-এ নতুন profile বানাতে হয়। না বানালে "entitlement profile-এ নেই" ধরনের error আসে।

[উপরে ফিরুন](#toc)

### <a id="ios11-2"></a>iOS ১১.২ Automatic বনাম manual signing

**এক লাইনে:** Automatic signing-এ Xcode নিজেই certificate আর profile বানায়, আর মেয়াদ ফুরালে নতুন করে নেয়। Manual-এ আপনি নিজে বেছে দেন কোনটা লাগবে। নিজের Mac-এ automatic চলে। CI-তে সাধারণত manual।

**Flutter-এ:** আপনি সম্ভবত এটাই করেছেন: Xcode-এ `ios/Runner.xcworkspace` খুলেছেন। তারপর Runner target → **Signing & Capabilities**-এ "Automatically manage signing" টিক দিয়ে Team বেছে নিয়েছেন। Flutter-এর docs বলে, এটা default-এ চালু থাকে, আর বেশিরভাগ app-এর জন্য এটাই যথেষ্ট।

| | Automatic | Manual |
|---|---|---|
| কে বানায় | Xcode, Apple account-এ login করে | আপনি, developer portal-এ বা tool দিয়ে |
| নতুন capability যোগ | Xcode নিজে profile আপডেট করে | নতুন profile বানাতে হয় |
| কোথায় ভালো | নিজের Mac, ছোট team | CI server, বড় team, একাধিক flavor |

**CI-তে কী হয়:** CI machine-এ কেউ Xcode-এ login করে না। তাই দুইটা পথ আছে:
- **App Store Connect API key** দিন, যাতে `xcodebuild` নিজেই automatic signing করতে পারে।
- **fastlane match** — certificate আর profile একটা encrypted git repo-তে রাখে। তারপর সব machine-এ সেই একই জিনিস বসিয়ে দেয়। Codemagic-এর মতো CI-ও নিজে এই কাজের tool দেয়।

**Best approach:** নিজের কাজে automatic signing নিন। CI-তে App Store Connect API key নিন। Team বড় হলে fastlane match।

[উপরে ফিরুন](#toc)

### <a id="ios11-3"></a>iOS ১১.৩ Archive → TestFlight → App Store

**এক লাইনে:** iOS-এ release build-কে বলে **archive**। Archive থেকে একটা `.ipa` বানিয়ে App Store Connect-এ upload করেন। তারপর TestFlight-এ test করেন। শেষে review-তে পাঠান।

**ধাপগুলো:**

1. **App Store Connect-এ app তৈরি।** Bundle ID বেছে নিন, নাম, ভাষা, SKU দিন। (Play Console-এ নতুন app বানানোর মতো।)
2. **Version আর build number।** `CFBundleShortVersionString` হলো user যে version দেখে (`1.2.0`)। `CFBundleVersion` হলো build number। প্রতিটা upload-এ এটা বাড়াতে হয়। Flutter-এ `pubspec.yaml`-এর `version: 1.2.0+5` থেকে এই দুটো আসে: `1.2.0` আর `5`।
3. **Archive।** Xcode → Product → Archive চাপুন (আগে একটা device বা "Any iOS Device" বেছে নিন)। ফল হিসেবে পাবেন একটা `.xcarchive`। এর ভেতরে থাকে app আর debug symbol (dSYM)।
4. **Distribute।** Xcode Organizer → Distribute App → App Store Connect। Xcode distribution certificate দিয়ে আবার sign করে, তারপর upload করে।
5. **Processing।** Upload-এর পরে Apple কিছুক্ষণ build-টা "process" করে। তারপর সেটা TestFlight-এ দেখা যায়।
6. **TestFlight।**
   - **Internal tester:** আপনার App Store Connect team-এর সর্বোচ্চ ১০০ জন। Review লাগে না।
   - **External tester:** সর্বোচ্চ ১০,০০০ জন, email বা public link দিয়ে। প্রথম build-এ Beta App Review লাগতে পারে।
   - প্রতিটা build upload-এর পর ৯০ দিন test করা যায়।
7. **Submit for Review।** Screenshot, বিবরণ, privacy তথ্য দিন। Reviewer-এর জন্য একটা demo account-ও দিন। তারপর review শুরু হয়।
8. **Release।** Approve হলে তিনভাবে release করা যায়: নিজে হাতে, একটা নির্দিষ্ট দিনে, বা ধীরে ধীরে (phased release — ৭ দিনে সবার কাছে পৌঁছায়)।

**কী মিলল:**

| Google Play | App Store |
|---|---|
| Play Console | App Store Connect |
| AAB upload | archive থেকে `.ipa` upload |
| `versionName` / `versionCode` | `CFBundleShortVersionString` / `CFBundleVersion` |
| Internal testing track | TestFlight internal |
| Closed / open testing | TestFlight external |
| Staged rollout (%) | Phased release (৭ দিন) |
| review (সাধারণত দ্রুত, বেশিরভাগটা automatic) | প্রতিটা version-এ মানুষ review করে |

**Xcode version-এর নিয়ম (নভেম্বর ২০২৬):** Apple-এর "Upcoming Requirements" পাতা বলে, ২৮ এপ্রিল ২০২৬ থেকে App Store Connect-এ upload করতে Xcode 26 বা তার নতুন version লাগে, সাথে iOS 26 SDK। Xcode 27 বের হয়েছে ১৪ সেপ্টেম্বর ২০২৬-এ। Apple প্রতি বছর বসন্তে এই নিয়ম এক ধাপ ওপরে তোলে। তাই upload-এর আগে [এই পাতাটা](https://developer.apple.com/news/upcoming-requirements/) একবার দেখে নিন। একই পাতা আরও বলে, ৯ সেপ্টেম্বর ২০২৬ থেকে upload করা app-এর minimum iOS হতে হবে 13 বা তার বেশি।

**ফাঁদ:**
- **একই build number দুইবার দেওয়া।** একই version-এ একই build number দিয়ে আবার upload করা যায় না। Flutter-এ `+5`-কে `+6` করুন, বা `--build-number` দিন।
- **প্রতিবার export compliance-এর প্রশ্ন আসা।** App যদি শুধু HTTPS-এর মতো সাধারণ encryption ব্যবহার করে, তাহলে `Info.plist`-এ `ITSAppUsesNonExemptEncryption` = `NO` দিন। তখন প্রতি build-এ প্রশ্নটা আর আসে না।
- **dSYM হারিয়ে ফেলা।** Crash report পড়তে archive-এর dSYM লাগে। Crashlytics ব্যবহার করলে দেখুন dSYM upload হচ্ছে কি না। Flutter-এ Dart code-এর symbol আলাদা — `--split-debug-info` দিয়ে যে symbol বের হয়, সেটাও রেখে দিন।

[উপরে ফিরুন](#toc)

### <a id="ios11-4"></a>iOS ১১.৪ Review guideline-এর যে নিয়মে সবাই আটকায়

**এক লাইনে:** App Store-এ প্রতিটা version একজন মানুষ review করে। সে Apple-এর [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) মিলিয়ে দেখে। Flutter developer-রা সাধারণত নিচের কয়েকটা নিয়মে আটকে যায়।

**১. Digital জিনিস বিক্রি করলে In-App Purchase লাগবে (guideline 3.1.1)।** App-এর ভেতরে কোনো feature বা content খুলতে টাকা নিলে In-App Purchase (StoreKit) ব্যবহার করতেই হবে। যেমন subscription, premium note theme, বা "Pro" version। নিজের payment system, license key বা QR code দিয়ে এগুলো খোলানো নিষেধ। Flutter-এর `in_app_purchase` plugin iOS-এ ভেতরে StoreKit-ই চালায়।
- Physical জিনিস বা app-এর বাইরে ব্যবহার করা service বিক্রি করলে (খাবার, taxi) IAP লাগে না।
- **দেশ অনুযায়ী নিয়ম বদলাচ্ছে।** এখনকার guideline বলে, **United States storefront**-এ বাইরের payment-এর link বা button দেওয়া যায়। অন্য দেশে নিয়ম আলাদা। EU-র জন্য আরেক রকম ব্যবস্থা আছে। এই অংশ ঘন ঘন বদলায়। তাই submit-এর আগে guideline-টা আবার পড়ে নিন।

**২. Login service-এর নিয়ম (guideline 4.8) — Sign in with Apple।** আগের নিয়ম ছিল: Google বা Facebook login দিলে Sign in with Apple-ও দিতেই হবে। **জানুয়ারি ২০২৪-এ নিয়মটা বদলেছে।** এখন guideline বলে: user-এর মূল account যদি third-party বা social login দিয়ে বানানো হয়, তাহলে পাশে **আরেকটা সমান login option** রাখতে হবে। সেই option-কে এই তিনটা শর্ত মানতে হবে:
- শুধু নাম আর email নেয়,
- user চাইলে নিজের email লুকিয়ে রাখতে পারে,
- user-এর অনুমতি ছাড়া advertising-এর জন্য তার কাজকর্মের data জমায় না।

Sign in with Apple এই তিনটা শর্তই মানে। তাই এটাই সবচেয়ে সহজ সমাধান। App-এ শুধু নিজের email-password login থাকলে, বা app-টা enterprise/education account-এর হলে, এটা লাগে না।

**৩. Account খোলা গেলে মোছাও যেতে হবে (guideline 5.1.1(v))।** App-এ account খোলা গেলে, app-এর ভেতর থেকেই account delete করার পথ দিতে হবে। শুধু "আমাদের email করুন" লিখে দিলে হবে না।

**৪. আরও কয়েকটা সাধারণ কারণ:**
- **Crash করে বা app অসম্পূর্ণ (2.1)।** Reviewer-এর device-এ crash করলে reject হয়। Demo account কাজ না করলেও reject হয়।
- **App শুধু একটা website দেখায় (4.2)।** WebView-এ website দেখানো ছাড়া app আর কিছু না করলে "minimum functionality" কারণে reject হয়।
- **Permission-এর লেখা ঝাপসা।** Usage description-এ পরিষ্কার লিখুন permission-টা কেন লাগবে ([iOS ৯.৪](#ios9-4))।

**Best approach:** প্রথমবার submit করার আগে guideline-এর 2, 3.1, 4.8 আর 5.1 অংশ নিজে একবার পড়ুন। Review notes-এ demo account দিন, আর কোন feature কোথায় আছে লিখে দিন।

[উপরে ফিরুন](#toc)

### <a id="ios11-5"></a>iOS ১১.৫ Privacy manifest আর nutrition label

**এক লাইনে:** এরা দুইটা আলাদা জিনিস।
- **Privacy manifest** (`PrivacyInfo.xcprivacy`) হলো app-এর ভেতরের একটা file। এটা বলে, code কী কী data নেয়, আর কোন "sensitive" API কেন ব্যবহার করে।
- **Nutrition label** হলো App Store-এর পাতায় user-কে দেখানো privacy-র ছোট সারাংশ। এটা আপনি App Store Connect-এর "App Privacy" অংশে পূরণ করেন।

**Privacy manifest-এ কী থাকে:**

| Key | মানে |
|---|---|
| `NSPrivacyTracking` | app কি user-কে track করে (অন্য company-র data-র সাথে মিলিয়ে) |
| `NSPrivacyTrackingDomains` | tracking-এর জন্য কোন কোন domain-এ যায় |
| `NSPrivacyCollectedDataTypes` | কী কী data নেয়, আর কেন |
| `NSPrivacyAccessedAPITypes` | কোন "required reason API" ব্যবহার করে, আর তার কারণের code |

**Required reason API:** কিছু API-র value মিলিয়ে একটা device-কে আলাদা করে চেনা যায় (একে fingerprinting বলে)। তাই এসব API কেন ব্যবহার করছেন, Apple সেটা জানতে চায়। যেমন `UserDefaults`, file-এর timestamp, system boot time, disk-এর খালি জায়গা। Notes app নিজের setting রাখতে `UserDefaults` ব্যবহার করে। তার কারণের code হলো `CA92.1` ("শুধু app নিজের জন্য পড়া-লেখা")।

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

**কবে থেকে বাধ্যতামূলক:** Apple-এর পাতা বলে, ১ মে ২০২৪ থেকে নতুন app বা update upload করতে হলে required reason API-র কারণ লিখে দিতে হয়। App-এর ভেতরের third-party SDK যে API ব্যবহার করে, সেগুলোও এর মধ্যে পড়ে। Apple-এর তালিকায় থাকা জনপ্রিয় SDK-গুলোকে নিজেদের privacy manifest আর signature সাথে নিয়ে আসতে হয়।

**Flutter-এ:** Flutter engine আর বেশিরভাগ বড় plugin (যেমন `shared_preferences`, Firebase) নিজেদের manifest সাথে নিয়ে আসে। আপনার Runner-এর নিজের code যদি কোনো required reason API ব্যবহার করে, তাহলে Xcode-এ File → New → File → **App Privacy** দিয়ে `PrivacyInfo.xcprivacy` যোগ করুন। Archive করার পরে Xcode Organizer-এ **Generate Privacy Report** চাপুন। সব manifest মিলিয়ে একটা report পাবেন। Nutrition label পূরণ করার সময় এটা কাজে লাগে।

**Nutrition label:** App Store Connect → আপনার app → App Privacy-তে গিয়ে পূরণ করুন। সেখানে বলতে হয়: কোন data নেন (email, crash data, usage data), সেই data user-এর পরিচয়ের সাথে জোড়া কি না, আর tracking-এ ব্যবহার হয় কি না। আপনার **SDK-গুলো যে data নেয়, সেটাও** এখানে লিখতে হয় — যেমন Firebase Analytics, Crashlytics। Android-এ ঠিক এই কাজটা হয় Play Console-এর **Data safety** form-এ।

**Tracking করলে আরেকটা নিয়ম:** অন্য company-র data-র সাথে মিলিয়ে user-কে track করলে (যেমন advertising ID দিয়ে), আগে user-এর অনুমতি নিতে হয়। অনুমতি নিতে হয় App Tracking Transparency (ATT) dialog দিয়ে ([iOS ৯.৪](#ios9-4)-এর `NSUserTrackingUsageDescription`)।

**ফাঁদ:** তিনটা জিনিস মিলতে হবে: manifest, nutrition label, আর app আসলে যা করে। না মিললে review-তে প্রশ্ন ওঠে। নতুন SDK যোগ করলে তিনটাই আবার check করুন।

[উপরে ফিরুন](#toc)

### <a id="ios11-6"></a>iOS ১১.৬ `flutter build ipa` ভেতরে কী করে

**এক লাইনে:** `flutter build ipa` আসলে Xcode-এর দুইটা command চালায়: `xcodebuild archive` আর `xcodebuild -exportArchive`। এর মাঝখানে Xcode-এর একটা build phase (build-এর একটা ধাপ) Flutter tool-কে ডাকে। সেই ধাপে Dart code compile হয়।

**ধাপে ধাপে:**

1. **Flutter tool আগে সব তৈরি করে নেয়।** `pub get` চালায়। `ios/Flutter/Generated.xcconfig` file লেখে — এতে থাকে Flutter SDK-র path, `FLUTTER_BUILD_NAME` আর `FLUTTER_BUILD_NUMBER`। Plugin-এর তালিকা থেকে `GeneratedPluginRegistrant` বানায়। Swift Package Manager চালু থাকলে (Flutter 3.44 থেকে এটা default) সব plugin `FlutterGeneratedPluginSwiftPackage` নামে একটা package-এ একসাথে যোগ হয়। যে plugin SPM সমর্থন করে না, সেটার জন্য CocoaPods ব্যবহার হয় (`pod install`)।
2. **`xcodebuild archive`** — `Runner.xcworkspace`, Release configuration:
   - Runner target-এর একটা **Run Script** phase `xcode_backend.sh build` চালায়। এটা `flutter assemble`-কে ডাকে। তারপর Dart code এই পথে যায়: Dart → kernel (`app.dill`) → `gen_snapshot` → ARM64 machine code → `App.framework/App`। Image আর font রাখা হয় `App.framework/flutter_assets/`-এ।
   - `swiftc` আপনার `AppDelegate`, `SceneDelegate` আর plugin-এর Swift code compile করে। Objective-C code থাকলে সেটা compile করে `clang`।
   - Linker সব অংশ জুড়ে একটা app বানায়। `actool` asset catalog (app icon) compile করে।
   - "Thin Binary" phase (`xcode_backend.sh embed_and_thin`) দুইটা জিনিস app-এর `Frameworks/` folder-এ রাখে: `App.framework` আর release-এর `Flutter.framework` (engine)।
   - প্রতিটা framework আর app sign হয়।
   - ফল: `build/ios/archive/Runner.xcarchive`।
3. **`xcodebuild -exportArchive`** — এটা একটা `ExportOptions.plist` file ব্যবহার করে (default method `app-store`)। Distribution certificate আর profile দিয়ে আবার sign করে। তারপর zip করে `.ipa` বানায়। ফল: `build/ios/ipa/*.ipa`।
4. **Upload Flutter নিজে করে না।** Apple-এর **Transporter** app-এ `.ipa` টেনে এনে ছেড়ে দিন। অথবা Xcode Organizer-এ archive খুলে Distribute করুন। CI-তে সাধারণত App Store Connect API key দিয়ে fastlane বা CI-র নিজের tool upload করে।

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

**ভেতরে দেখুন।** `.ipa` আসলে একটা zip file। খুললে এমন দেখবেন:

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

Android-এর APK-র সাথে মিলিয়ে দেখুন ([১৩.৬](#ch13-6)): `libflutter.so` ↔ `Flutter.framework`, `libapp.so` ↔ `App.framework/App`, `classes.dex` ↔ `Runner` executable।

**ফাঁদ:**
- **iOS-এর release build Simulator-এ চলে না।** Release আর profile build শুধু আসল device-এর জন্য। চেষ্টা করলে Flutter tool নিজেই error দেয়।
- **CocoaPods-এর ভবিষ্যৎ।** Flutter-এর docs বলে, ২ ডিসেম্বর ২০২৬-এ CocoaPods registry চিরদিনের জন্য read-only হয়ে যাবে। মানে সেখানে আর নতুন কিছু আসবে না। যে plugin এখনো শুধু CocoaPods-এ আছে, সেটা বদলানোর পরিকল্পনা রাখুন।
- **`flutter clean`-এর পরেও signing error থেকে যাওয়া।** Xcode-এ `ios/Runner.xcworkspace` খুলে একবার Archive চালান। Xcode signing-এর আসল কারণটা অনেক পরিষ্কার করে দেখায়।

> **মনে রাখুন**
> - Certificate বলে কে sign করছে। Provisioning profile বলে কোন app, কোন device, কোন entitlement। দুটো মিললে তবেই app চলে।
> - App-কে চেনায় Bundle ID + Team, certificate না। Certificate বদলালে App Store-এর app-এর কিছু হয় না।
> - Archive → `.ipa` → App Store Connect → TestFlight (internal ১০০, external ১০,০০০, build ৯০ দিন) → review।
> - Digital জিনিস বিক্রিতে IAP লাগবেই। Social login থাকলে privacy রক্ষা করে এমন আরেকটা login দিন (Sign in with Apple সবচেয়ে সহজ)। Account মোছার পথ app-এর ভেতরেই রাখুন।
> - `flutter build ipa` = `xcodebuild archive` + `-exportArchive`। Dart যায় `App.framework`-এ, engine `Flutter.framework`-এ।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "iOS signing-এর মূল জিনিস দুইটা। Certificate বলে কে sign করছে। Provisioning profile বলে কোন bundle id কোন device-এ কোন entitlement নিয়ে চলবে। নিজের Mac-এ আমি automatic signing রাখি। CI-তে App Store Connect API key বা fastlane match ব্যবহার করি। Release মানে: archive থেকে ipa বানাই, App Store Connect-এ upload করি, TestFlight-এ test করি, তারপর review-তে পাঠাই। flutter build ipa ভেতরে xcodebuild archive আর exportArchive চালায়। আর একটা build phase Dart code AOT compile করে App.framework বানায়।"
> - *English:* "iOS signing has two key pieces: the certificate, which says who signs, and the provisioning profile, which says which bundle ID can run on which devices with which entitlements. I use automatic signing on my Mac, and an App Store Connect API key or fastlane match on CI. A release means archiving, exporting an ipa, uploading it to App Store Connect, testing on TestFlight, and then review. flutter build ipa runs xcodebuild archive and exportArchive under the hood, and a build phase AOT-compiles the Dart code into App.framework."

[উপরে ফিরুন](#toc)

---
## <a id="ios12"></a>iOS ১২. ইঞ্জিনের ভেতরে — tap থেকে pixel, code থেকে `.ipa`

Android-এর [অধ্যায় ১৩](#ch13)-এ আমরা Android-এর ভেতরের অংশগুলো দেখেছিলাম: ART, Zygote, HWUI, SurfaceFlinger, Gradle। এবার iOS-এর ভেতরের অংশগুলো দেখব। প্রশ্নগুলো একই থাকবে:

- আপনার code কীসের ওপর চলে?
- Memory কে পরিষ্কার করে?
- App খুললে ভেতরে কী কী হয়?
- একটা pixel কীভাবে screen-এ আসে?
- Build চাপলে কী হয়?

প্রতিটা উত্তরের পাশে Flutter আর Android-এ ব্যাপারটা কেমন, সেটাও থাকবে।

এই অধ্যায়ে নতুন নাম অনেক। প্রতিটা নাম প্রথমবার আসার সময় সহজ কথায় বলে দেব সেটা কী করে।

### <a id="ios12-1"></a>iOS ১২.১ Swift সরাসরি machine code — কোনো VM নেই

**এক লাইনে:** আপনি build চাপলে, তখনই LLVM নামের compiler Swift code-কে ARM64 machine code বানিয়ে ফেলে। ARM64 হলো iPhone-এর CPU যে ভাষা বোঝে। তাই phone-এ কোনো virtual machine লাগে না, interpreter লাগে না, JIT-ও লাগে না। CPU সরাসরি আপনার code চালায়।

**Swift code কোন কোন ধাপ পার হয়:**

```
.swift ──swiftc──► AST ──► SIL (Swift Intermediate Language) ──► LLVM IR ──LLVM──► ARM64 (.o)
                            │                                                       │
                            └ এখানে ARC-এর retain/release বসে আর optimize হয়          ▼
                                                                         ld (linker) ──► Mach-O executable
```

ছবিটা বাঁ থেকে ডানে পড়ুন। নামগুলোর মানে:

- **SIL** হলো Swift-এর নিজের একটা মাঝের ভাষা। Code পুরো machine code হওয়ার আগে একবার এই রূপে আসে। Swift-এর নিজের কিছু optimization এখানেই হয় — যেমন generic code-কে নির্দিষ্ট type-এর জন্য আলাদা করে বানানো (generic specialization), আর অদরকারি retain/release বাদ দেওয়া।
- **LLVM** হলো compiler-এর শেষের অংশ (backend)। এই একই LLVM দিয়ে C, C++, Objective-C আর Rust-ও compile হয়। এটাই আসল machine code বানায়।
- **Mach-O** হলো Apple-এর executable file-এর format। Linux-এ যেমন ELF, Android-এ যেমন `.so` — তেমন।

**তাহলে "Swift runtime" জিনিসটা কী?** এটা একটা ছোট library, আর কিছু না। এর ভেতরে থাকে:

- type-এর তথ্য (metadata),
- retain/release করার function,
- dynamic cast,
- কোন type কোন protocol মানে, সেটা খুঁজে বের করার code।

এটা VM না। এটা শুধু আপনার code-কে সাহায্য করে। Swift 5 থেকে Apple-এর platform-এ ABI স্থির — মানে compile করা Swift code-এর binary-র নিয়ম আর বদলায় না, তাই নতুন Swift version এলেও পুরনো compile করা code চলতে পারে। তাই iOS 12.2 থেকে এই runtime iOS-এর ভেতরেই দেওয়া থাকে। আপনার app-এর সাথে এটা আলাদা করে পাঠাতে হয় না।

এর পাশে Objective-C runtime-ও আছে। UIKit-এর class আর `@objc` method-কে যখন ডাকা হয় (message পাঠানো হয়), সেটা এই runtime দিয়ে চলে।

**JIT কেন নেই:** JIT মানে app চলার সময় memory-তে নতুন machine code বানিয়ে চালানো। iOS-এ App Store-এর app এটা করতে পারে না। কারণ iOS-এ যে code চলবে, তার প্রতিটা page আগে থেকে sign করা থাকতে হয়। নতুন বানানো code-এর sign নেই, তাই সেটা চলতে দেয় না। এর দুইটা ফল:

- **Flutter-এর release build iOS-এ সবসময় AOT।** মানে Dart code আগেই machine code হয়ে যায়। Android-এও release AOT, কিন্তু iOS-এ এ ছাড়া অন্য কোনো পথই নেই।
- **Device-এ Flutter debug (hot reload)** চলে Dart VM-এর JIT দিয়ে। এটা সম্ভব হয় কারণ Xcode-এর debugger পাশে থেকে সাহায্য করে। iOS 26-এ এই নিয়ম আরও কড়া হয়েছে, তাই Flutter-কে নিজের পদ্ধতি বদলাতে হয়েছিল। তাই physical device-এ debug করলে সবসময় সর্বশেষ stable Flutter রাখুন।

**তিনটা runtime পাশাপাশি:**

| | Swift (iOS) | Kotlin (Android, ART) | Dart (Flutter) |
|---|---|---|---|
| কীসে compile হয় | machine code, build-এর সময়েই | `.dex` bytecode | debug: kernel; release: machine code |
| Phone-এ কে চালায় | CPU সরাসরি + ছোট Swift runtime | ART: interpreter + JIT + AOT | debug: Dart VM (JIT); release: Dart runtime (AOT) |
| Memory | ARC ([iOS ১২.২](#ios12-2)) | garbage collector | garbage collector |
| VM আছে? | না | হ্যাঁ, ART | debug-এ হ্যাঁ, release-এ শুধু runtime |

**মজার কথা:** একটা Flutter iOS app-এ দুইটা জগৎ একসাথে থাকে। একদিকে Swift/Objective-C, অন্যদিকে Dart। দুটো একই process-এ চলে, কিন্তু memory-র heap আলাদা।

- Swift-এর object দেখাশোনা করে ARC।
- Dart-এর object দেখাশোনা করে Dart-এর GC।
- দুই জগৎ কথা বলে platform channel বা FFI দিয়ে।

Android-এ ART আর Dart ঠিক এভাবেই আলাদা ছিল ([১৩.২](#ch13-2))।

**ফাঁদ:** দুইটা ভুল ধারণা খুব চলে।

- "Swift-ও Java-র মতো VM-এ চলে" — না, চলে না।
- "Flutter iOS-এ Dart-কে Swift-এ বদলে নেয়" — এটাও না। Dart নিজেই সরাসরি ARM64 machine code হয়, আর থাকে `App.framework`-এর ভেতরে ([iOS ১২.৫](#ios12-5))।

[উপরে ফিরুন](#toc)

### <a id="ios12-2"></a>iOS ১২.২ ARC বনাম garbage collection

**এক লাইনে:** Swift-এ কোনো garbage collector নেই। এর বদলে প্রতিটা class object একটা হিসাব রাখে — এই মুহূর্তে কতজন তাকে ধরে রেখেছে (reference count)। হিসাব শূন্য হলেই object-টা সাথে সাথে memory থেকে মুছে যায়। এই হিসাব বাড়ানো-কমানোর code আপনি লেখেন না, compiler নিজে বসায়। এজন্য নাম Automatic Reference Counting (ARC)।

একটু খুলে বলি:

- কেউ object-টাকে ধরলে হিসাব ১ বাড়ে — একে বলে **retain**।
- কেউ ছেড়ে দিলে হিসাব ১ কমে — একে বলে **release**।
- হিসাব ০ হলে object মুছে যায়।

**তিনজন কীভাবে memory পরিষ্কার করে:**

| | Swift (ARC) | Dart | ART (Android) |
|---|---|---|---|
| কে মুছে দেয় | compiler-এর বসানো retain/release | GC | GC |
| কখন | শেষ reference চলে যাওয়ার সাথে সাথে | GC যখন চলে | GC যখন চলে |
| GC pause | নেই | ছোট (নতুন object-এর জন্য দ্রুত scavenge) | ছোট (concurrent GC) |
| Cycle (A ধরে B-কে, B ধরে A-কে) | **leak** — নিজে ভাঙতে হয় | GC নিজে ধরে ফেলে | GC নিজে ধরে ফেলে |
| খরচ | প্রতিবার reference বদলালে একটু কাজ | মাঝে মাঝে GC-র কাজ | মাঝে মাঝে GC-র কাজ |

**Value type-এ হিসাব নেই।** `struct` আর `enum` অন্যকে দিলে তার একটা copy যায়। কেউ কাউকে "ধরে" রাখে না। তাই বেশিরভাগ সময় reference count লাগেই না। এজন্য Swift-এ model-কে `struct` বানানো খুব চলে — এটা দ্রুত, আর ভুল কম হয়। (একটা কথা: struct-এর ভেতরে যদি class বা `Array`-এর মতো জিনিস থাকে, তাহলে তাদের ভেতরের storage-এর হিসাব ঠিকই থাকে।)

**Flutter থেকে এলে সবচেয়ে বড় ফাঁদ — retain cycle:**

Retain cycle মানে দুইটা object একে অপরকে ধরে আছে। তাই কারো হিসাবই কখনো শূন্য হয় না। ফলে দুটোই memory-তে থেকে যায় — এটাই leak।

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

Dart-এ এমন code নিয়ে কখনো ভাবতে হয়নি। কারণ Dart-এর GC এমন cycle নিজেই খুঁজে বের করে মুছে দেয়। Swift-এ সেটা হয় না। তাই closure-এর ভেতরে `self` লেখার আগে সবসময় একবার ভাবুন: কে কাকে ধরে আছে?

**এই ফাঁদ কোথায় বেশি দেখবেন:**

- Plugin-এর `FlutterMethodChannel` handler-এর closure যখন plugin class-কে ধরে রাখে।
- Delegate property-তে। এজন্যই delegate প্রায় সবসময় `weak var delegate` হয় ([iOS ৯.২](#ios9-2)-এর ফাঁদ দেখুন)।
- `weak` আর `unowned`-এর পার্থক্য:
  - `weak` হলো Optional। Object চলে গেলে এটা নিজে থেকে `nil` হয়ে যায়।
  - `unowned` ধরে নেয় object সবসময় থাকবে। না থাকলে app crash করে।
  - নিশ্চিত না হলে `weak` নিন।

**Memory কম পড়লে iOS কী করে:** iOS-এ memory ভরে গেলে disk-এ সরিয়ে রাখার (swap) ব্যবস্থা নেই। iOS শুধু memory-কে চেপে ছোট করে (compress)। তাতেও না হলে **jetsam** নামের একটা ব্যবস্থা app মেরে ফেলে। আগে background-এর app মারে। দরকার হলে বেশি memory খাওয়া foreground app-কেও মারে। Android-এর low memory killer-এর মতোই। তাই iOS-এ বড় ছবি বা leak থাকলে সেটা সোজা crash হয়ে দেখা দেয়।

**Debug করবেন কীভাবে:**

- Xcode-এর **Memory Graph Debugger** — debug bar-এর একটা button। এটা cycle-গুলো ছবিতে দেখায়।
- Instruments-এর **Leaks** আর **Allocations** — Android Studio-র Memory Profiler-এর মতো।
- Dart-এর heap দেখতে আগের মতো DevTools-ই লাগবে।

[উপরে ফিরুন](#toc)

### <a id="ios12-3"></a>iOS ১২.৩ App খুললে কী হয় — tap থেকে প্রথম frame

**এক লাইনে:** আপনি icon-এ tap করলেন। তারপর পরপর এগুলো হয়:

1. Home screen (SpringBoard) system-কে বলে app খুলতে।
2. launchd একটা নতুন process চালু করে।
3. dyld দরকারি সব library জোড়া দেয়।
4. `main()` থেকে `UIApplicationMain` চলে।
5. AppDelegate আর Scene তৈরি হয়।
6. প্রথম frame আঁকা হলে launch screen সরে যায়।

Flutter-এ এর মাঝখানে একটা বাড়তি ধাপ আছে: engine চালু হয়, তারপর Dart-এর `main()` চলে।

**সব app-এর জন্য পথটা একই। ধাপে ধাপে:**

1. **Tap।** Home screen নিজেও একটা system app। এর নাম **SpringBoard**। আপনি tap করলে SpringBoard system-কে app খোলার অনুরোধ পাঠায়।
2. **আগে launch screen।** Process তৈরি হওয়ার আগেই iOS app-এর launch screen দেখিয়ে দেয়। এটা আসে `Info.plist`-এর `UILaunchScreen` থেকে, বা `LaunchScreen.storyboard` থেকে। এটা একটা স্থির ছবির মতো। এখানে আপনার কোনো code চলে না। Android-এর starting window আর Flutter-এর `LaunchTheme`-এর মতো ([১৩.৩](#ch13-3))।
3. **Process।** **launchd** হলো iOS-এর প্রথম process। iOS চালু হলে সবার আগে এটা চলে, আর বাকি process-গুলো এটাই চালু করে। launchd আপনার app-এর জন্য একটা নতুন process চালু করে। Android-এর মতো Zygote-এর copy থেকে আসে না। প্রতিবার একদম নতুন process, নিজের sandbox-এর ভেতরে ([iOS ৮.৭](#ios8-7))।
4. **dyld।** প্রথমে kernel আপনার Mach-O executable memory-তে আনে। তারপর **dyld** কাজ শুরু করে। dyld হলো dynamic linker — app-এর দরকারি library-গুলো খুঁজে এনে app-এর সাথে জোড়া দেয়।
   - UIKit, SwiftUI, Foundation-এর মতো system framework আগে থেকেই একটা বড় **shared cache**-এ তৈরি হয়ে থাকে। তাই এগুলো খুব দ্রুত জোড়া যায়।
   - আপনার নিজের framework (যেমন `Flutter.framework`) আলাদা করে load হয়।
   - সবশেষে static initializer চলে।
5. **`main()` → `UIApplicationMain`।** SwiftUI-তে আপনি `@main struct NotesApp: App` লেখেন। তখন compiler নিজেই একটা `main()` বানিয়ে দেয়, যেটা ভেতরে এই একই কাজ করে। `UIApplicationMain` তিনটা কাজ করে:
   - `UIApplication` object বানায়,
   - আপনার AppDelegate বানায়,
   - main thread-এ **run loop** চালু করে। Run loop হলো একটা চক্র, যেটা ঘুরে ঘুরে event নেয় আর কাজ করে — Android-এর Looper বা Dart-এর event loop-এর মতো।
6. **AppDelegate।** এবার `application(_:didFinishLaunchingWithOptions:)` চলে। SDK init করা, BGTask register করা — এসব কাজ এখানে হয়।
7. **Scene।** iOS `Info.plist`-এর scene configuration দেখে একটা `UIWindowScene` বানায়। তারপর SceneDelegate-এর `scene(_:willConnectTo:options:)` চলে। এখানে window তৈরি হয়, আর প্রথম view controller (বা SwiftUI-র `WindowGroup`-এর content) তৈরি হয়। একটা জরুরি কথা: Apple বলেছে, iOS 26-এর পরের major release-এর SDK দিয়ে build করা app যদি scene lifecycle না নেয়, তাহলে সেটা launch-ই হবে না ([iOS ৪](#ios4))।
8. **প্রথম frame।** View-এর layout হয়, আঁকা হয়। Run loop-এর এই চক্রের শেষে Core Animation সব পরিবর্তন render server-এ পাঠায় ([iOS ১২.৪](#ios12-4))। প্রথম frame screen-এ এলেই launch screen সরে যায়।

**ধাপ ৬–৭-এ এসে Native আর Flutter-এর পথ আলাদা হয়ে যায়:**

- **Native (SwiftUI):** `WindowGroup { NotesScreen(...) }`-এর `body` চলে। View tree তৈরি হয়। তারপর প্রথম frame।
- **Flutter:** নতুন Flutter template-এ `AppDelegate` হলো `FlutterAppDelegate`, আর `SceneDelegate` হলো `FlutterSceneDelegate`। তারপর এই ধাপগুলো:
  1. Scene configuration-এ বলা `Main` storyboard একটা **`FlutterViewController`** বানায়।
  2. এটা একটা `FlutterEngine` চালু করে। Template-এ একে "implicit engine" বলে, কারণ আপনি নিজে হাতে engine বানান না। Engine-এর code থাকে `Flutter.framework`-এ, যেটা C++-এ লেখা। dyld এটা আগেই (ধাপ ৪-এ) load করে রেখেছে।
  3. Engine নিজের thread-গুলো বানায়:
     - **platform thread** — এটাই iOS-এর main thread। Flutter 3.29 থেকে Dart code-ও এখানেই চলে।
     - **raster thread** — GPU-তে আঁকার কাজ করে।
     - **I/O thread**।
  4. Engine তৈরি হলে `AppDelegate`-এর `didInitializeImplicitFlutterEngine` চলে। তখন `GeneratedPluginRegistrant` সব plugin register করে। Plugin-এর Swift অংশ এখানেই তৈরি হয়।
  5. Engine `App.framework` থেকে আপনার compile করা Dart code খুঁজে নেয়।
  6. Dart-এর entrypoint চলে: `main()` → `runApp()` → widget tree।
  7. Engine প্রথম frame আঁকে। যতক্ষণ আঁকা শেষ হয় না, ততক্ষণ `FlutterViewController` launch screen-এর একটা copy দেখিয়ে রাখে। Frame আঁকা হলেই সেটা সরে যায়।

পুরো পথটা এক ছবিতে:

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

- **Cold launch:** App-এর process একদম নেই। তখন উপরের পুরো পথ চলে।
- **Warm launch (resume):** Process memory-তে থেমে (suspend) ছিল। iOS শুধু সেটা আবার চালু করে। প্রায় সাথে সাথে খুলে যায়।
- **Pre-warming:** iOS দেখে আপনি সাধারণত কখন কোন app খোলেন। সেই হিসাবে কখনো আপনি tap করার আগেই app-এর process চালু করে রাখে। (iOS 15-এ এটা আরও বেড়েছে।)
  - Apple-এর docs বলে, pre-warming `main()`-এর ভেতরে `UIApplicationMain` ডাকার আগ পর্যন্ত চলে, তারপর থামে।
  - কিন্তু developer-রা forum-এ জানিয়েছেন, বাস্তবে কখনো এর চেয়ে বেশি code-ও চলে।
  - তাই "process চালু হয়েছে মানে user app খুলেছে" — এমন ধরে নেবেন না। Analytics-এ "app open" গুনুন scene সামনে আসার পরে।

**ফাঁদ:**

- **Launch-এর সময় বেশি কাজ করা।** `didFinishLaunching`-এ, বা Flutter-এর `main()`-এ `runApp`-এর আগে, সব কিছু `await` করলে launch screen আটকে থাকে। দেরি খুব বেশি হলে iOS-এর **watchdog** (system-এর একটা অংশ, যেটা দেখে app সময়মতো চালু হলো কি না) app-টা মেরে ফেলে। Crash report-এ তখন `0x8badf00d` code দেখবেন। Android-এর `Application.onCreate`-এর নিয়মই এখানেও খাটে: প্রথম frame-এর আগে শুধু সেই কাজ করুন, যেটা না করলেই নয়।
- **Launch screen-এ animation বা code চালাতে চাওয়া।** Launch screen স্থির, এখানে কিছু চলে না। Animated splash চাইলে সেটা আপনার প্রথম আসল screen-এ বানাতে হবে।

[উপরে ফিরুন](#toc)

### <a id="ios12-4"></a>iOS ১২.৪ Rendering — Core Animation, render server, Metal

**এক লাইনে:** Native iOS-এ প্রতিটা view-এর পেছনে একটা Core Animation **layer** থাকে। App এই layer-গুলো দিয়ে একটা গাছ (tree) বানায়। তারপর গাছটা আলাদা একটা system process-কে পাঠায় — তার নাম **render server**। Render server Metal দিয়ে GPU-তে ছবি আঁকে, আর display-তে পাঠায়। Flutter এই গাছে মাত্র একটা layer রাখে। সেই একটা layer-এর ভেতরে Impeller নিজে সব কিছু আঁকে।

**নামগুলো, একটা একটা করে:**

- **Core Animation (CA)।** UIKit-এর প্রতিটা `UIView`-এর পেছনে একটা `CALayer` থাকে। SwiftUI-ও শেষ পর্যন্ত এই layer দিয়েই আঁকে। সব layer মিলে একটা গাছ হয় (layer tree)। এই গাছটাই বলে দেয় screen-এ কী আছে, কোথায় আছে।
- **Transaction।** Main thread-এ আপনি state বদলালেন, তারপর layout হলো। এসব পরিবর্তন সাথে সাথে পাঠানো হয় না, জমা থাকে। Run loop-এর চক্রের শেষে Core Animation জমা থাকা সব পরিবর্তন একসাথে render server-এ পাঠায়। এই পাঠানোকে বলে "commit"।
- **Render server।** এটা আলাদা একটা system process (backboardd-এর ভেতরে চলে)। সব app-এর layer tree, status bar, keyboard — সব এখানে এসে একসাথে মেশে। কাজটা Android-এর SurfaceFlinger-এর মতো। পার্থক্য হলো, render server শুধু মেশায় না, নিজেও layer আঁকে।
- **Metal।** Apple-এর GPU API। Android-এ যেখানে Vulkan, iOS-এ সেখানে Metal। Render server Metal দিয়ে আঁকে।
- **Vsync।** Display একটা নির্দিষ্ট সময় পর পর নতুন frame চায় — প্রতি ১৬.৭ ms-এ (60Hz), বা ProMotion screen-এ প্রতি ৮.৩ ms-এ (120Hz)। এই সংকেতকে vsync বলে। App এই সংকেত পায় `CADisplayLink` দিয়ে — Android-এর `Choreographer`-এর মতো।

**এর একটা সুন্দর ফল:** Core Animation-এর animation app-এ না, render server-এ চলে। তাই app-এর main thread কিছুক্ষণ ব্যস্ত থাকলেও এমন animation অনেক সময় মসৃণ থাকে। Flutter-এর animation কিন্তু Dart-এ চলে। তাই UI thread আটকে গেলে Flutter-এর animation-ও আটকে যায়।

**Flutter-এ ব্যাপারটা কেমন:** `FlutterViewController`-এর view হলো একটা `FlutterView`। এর পেছনের layer-টা Metal দিয়ে আঁকার জন্য বানানো।

- আজকাল default-এ এটা Flutter-এর নিজের `FlutterMetalLayer`। এটা `CALayer`-এর একটা subclass।
- `FLTUseFlutterMetalLayer` = `NO` দিলে এর বদলে সাধারণ `CAMetalLayer` ব্যবহার হয়।
- Flutter-এর নিজের layer-টা আচরণে `CAMetalLayer`-এর মতোই। তবে frame কখন দেখানো হবে, সেটা Flutter আরও ভালোভাবে নিয়ন্ত্রণ করতে পারে।

তারপর একটা frame এভাবে আঁকা হয়:

1. Platform thread-এ Dart চলে: build → layout → paint → layer tree।
2. Raster thread-এ **Impeller** সেই layer tree-কে Metal-এর command-এ বদলায়। তারপর layer-এর কাছ থেকে একটা drawable (GPU যে texture-এ আঁকবে, সেটা) নিয়ে তাতে আঁকে।
3. সেই layer Core Animation-এর গাছে আর দশটা layer-এর মতোই একটা সাধারণ layer। Render server বাকি সবার সাথে এটাকে মিলিয়ে display-তে পাঠায়।
4. Flutter engine-ও vsync সংকেত নেয় `CADisplayLink` থেকে।

**iOS-এ Impeller:** iOS-এ Impeller default হয়েছিল Flutter 3.10-এ। Flutter 3.29 থেকে iOS-এ Skia পুরো বাদ দেওয়া হয়েছে। এখন `FLTEnableImpeller` দিয়ে Impeller বন্ধ করার পথও নেই। তাই iOS-এ Impeller-ই একমাত্র renderer। Impeller-এর সব shader আগে থেকেই compile করা থাকে। তাই প্রথমবার animation চালালে আর "shader compilation jank" (shader বানাতে গিয়ে আটকে যাওয়া) হয় না।

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

**কোথায় মিল, কোথায় পার্থক্য:**

| | Native iOS | Flutter on iOS | Android ([১৩.৫](#ch13-5)) |
|---|---|---|---|
| UI-টা কী দিয়ে বলা হয় | View → `CALayer` গাছ | widget → layer tree (Dart) | View/Compose → display list |
| কে GPU-তে আঁকে | render server (Core Animation) | app-এর raster thread-এ Impeller | RenderThread-এ HWUI (Skia) |
| GPU API | Metal | Metal | OpenGL ES / Vulkan |
| শেষে কে সব মেশায় | render server | render server | SurfaceFlinger |
| Vsync | `CADisplayLink` | `CADisplayLink` | `Choreographer` |

**ফাঁদ:**

- **ProMotion screen-এ 120Hz না পাওয়া।** iPhone-এ 60Hz-এর বেশি পেতে `Info.plist`-এ `CADisableMinimumFrameDurationOnPhone` = `true` দিতে হয়। Flutter-এর template-এ এটা আগে থেকেই দেওয়া আছে। কিন্তু নিজে native project বানালে নিজেকে যোগ করতে হবে।
- **"SwiftUI-ও Flutter-এর মতো নিজে আঁকে" — এমন ভাবা।** না। SwiftUI Apple-এর Core Animation-এর জগতের ভেতরেই থাকে। এজন্য SwiftUI আর UIKit এক screen-এ সহজে মিশে যায়। Flutter-এ কোনো UIKit view বসাতে হলে Platform View (`UiKitView`) লাগে। এতে আলাদা করে মেশানোর (composition) বাড়তি খরচ আসে।
- **iOS জানে না Flutter-এর screen-এ কী আছে।** iOS-এর চোখে এটা শুধু একটা layer-এর pixel। Button কোথায়, text কোথায় — জানে না। তাই VoiceOver-এর জন্য Flutter নিজের semantics tree থেকে iOS-এর accessibility element বানিয়ে দেয়।

[উপরে ফিরুন](#toc)

### <a id="ios12-5"></a>iOS ১২.৫ Build pipeline — Xcode থেকে `.app` আর `.ipa`

**এক লাইনে:** প্রতিটা target-এর কিছু build phase (ধাপ) থাকে। Xcode-এর build system এগুলো একটার পর একটা চালায়: package resolve, compile, link, resource, embed, sign। শেষে পাওয়া যায় একটা `.app` folder। এটাকে archive আর export করলে হয় `.ipa`।

**Native: ⌘B বা Archive চাপলে কী হয়**

1. **Package resolve।** Swift Package Manager-এর dependency download হয়, build হয় ([iOS ৩](#ios3))। Android-এ Gradle যেভাবে dependency resolve করে, তেমন।
2. **Compile।** প্রতিটা module-এর Swift file compile হয় `swiftc` দিয়ে। Objective-C থাকলে সেটা হয় `clang` দিয়ে। এটা incremental — যে file বদলায়নি, সেটা আবার compile হয় না।
3. **Link।** Apple-এর linker (`ld`) সব `.o` file জোড়া লাগিয়ে একটা Mach-O executable বানায়।
4. **Resource।**
   - `actool` asset catalog (`Assets.xcassets`) compile করে `Assets.car` বানায়। এর ভেতরে থাকে app icon, রং, ছবি।
   - Storyboard থাকলে সেটা compile করে `ibtool`।
   - `Info.plist`-এ যেখানে `$(...)` লেখা, সেখানে build setting-এর আসল মান বসে যায়।
5. **Embed।** Dynamic framework (যেমন `Flutter.framework`) app-এর `Frameworks/` folder-এ copy হয়।
6. **Code sign।** `codesign` প্রথমে প্রতিটা framework sign করে, শেষে পুরো app sign করে। Entitlement-ও (app কোন বিশেষ ক্ষমতা পাবে, তার তালিকা) এখানে বসে ([iOS ১১.১](#ios11-1))।
7. **ফল:** `Notes.app`। নামে file মনে হলেও এটা আসলে একটা folder।
8. **Archive** করলে পাবেন `.xcarchive` (এতে থাকে app + dSYM)। তারপর **export** করলে পাবেন `.ipa` — এটা আসলে `Payload/Notes.app`-কে zip করা একটা file।

**মাঝের file কোথায় জমে:** Build-এর সময় তৈরি হওয়া সব মাঝের file থাকে `~/Library/Developer/Xcode/DerivedData/`-এ। Gradle-এর `build/` folder আর cache-এর মতো। অদ্ভুত কোনো build error এলে Product → **Clean Build Folder** (⇧⌘K) দিন। তাতেও না হলে DerivedData মুছে দিন।

**Xcode-এর build system নিজে:** Apple ২০২৫-এ এটা **Swift Build** নামে open source করেছে। Gradle-এর মতো এটাও কাজগুলোর একটা গ্রাফ (task graph) বানায়। তবে Gradle-এর মতো আলাদা কোনো DSL নেই। নিয়মগুলো আসে Xcode project-এর build settings আর build phase থেকে।

**App Store-এর দিকে:** আপনি একটা build upload করেন। App Store সেখান থেকে প্রতিটা device-এর জন্য একটা ছোট রূপ বানায় — একে বলে **App Thinning**। যেমন, প্রতিটা device শুধু তার নিজের screen-এর মাপের ছবি পায়। আগে Bitcode বলে একটা জিনিস ছিল, এখন আর নেই (Xcode 14-এ বাদ গেছে)।

**Flutter: Runner target-এ বাড়তি কী চলে**

`ios/Runner.xcodeproj`-এর Runner target-এ Flutter দুইটা **Run Script** phase যোগ করে:

1. **"Run Script"** — এটা `xcode_backend.sh build` চালায়, যেটা ভেতরে `flutter assemble` চালায়। এখানে যা হয়:
   - **Release/profile build-এ:** Dart code প্রথমে kernel হয় (`app.dill`, অদরকারি code বাদ দিয়ে — tree shaking)। তারপর **`gen_snapshot`** সেটাকে ARM64 machine code বানায়। ফল হলো `App.framework/App`, যেটা একটা Mach-O dynamic library। একাধিক architecture থাকলে `lipo` দিয়ে সেগুলো এক file-এ জোড়া হয়।
   - **Debug build-এ:** `App.framework/App` শুধু একটা খালি stub। আপনার Dart code kernel আকারে `flutter_assets`-এ যায়। Device-এ Dart VM সেটা JIT দিয়ে চালায়। এজন্যই hot reload সম্ভব হয়।
   - Asset (image, font, `pubspec`-এ দেওয়া asset) যায় `App.framework/flutter_assets/`-এ। Material Icons font থেকে শুধু যে icon-গুলো আপনি ব্যবহার করেছেন, সেগুলোই রাখা হয়।
2. **"Thin Binary"** — এটা `xcode_backend.sh embed_and_thin` চালায়। এটা `App.framework` আর build mode অনুযায়ী ঠিক `Flutter.framework` app-এর `Frameworks/`-এ বসায়, আর sign করে।

বাকি সব native-এর মতোই হয়: `AppDelegate`/`SceneDelegate` আর plugin-এর Swift code `swiftc` দিয়ে compile হয়, তারপর link, asset catalog, sign।

```
.dart ──frontend_server──► app.dill ──gen_snapshot──► App.framework/App (ARM64)   ┐
pubspec asset ───────────────────────────────────────► App.framework/flutter_assets ├─► Runner.app/Frameworks/
Flutter SDK-র আগে থেকে build করা engine ─────────────► Flutter.framework            ┘
.swift (Runner + plugin) ──swiftc + ld──────────────► Runner.app/Runner
Assets.xcassets ──actool────────────────────────────► Runner.app/Assets.car
                                  সব শেষে codesign ──► Runner.app ──archive/export──► .ipa
```

**ফাঁদ:**

- **"Flutter iOS build মানেই CocoaPods"** — এখন আর না। Flutter 3.44 থেকে Swift Package Manager default। CocoaPods শুধু বিকল্প (fallback) হিসেবে আছে ([iOS ১১.৬](#ios11-6))।
- **`flutter clean` সব কিছু মোছে না।** Xcode-এর DerivedData আলাদা জায়গায় থাকে। Native দিকে অদ্ভুত error এলে Xcode-এ Clean Build Folder-ও দিন।

[উপরে ফিরুন](#toc)

### <a id="ios12-6"></a>iOS ১২.৬ Android-এর পাশে, এক টেবিলে

পুরো অধ্যায়টা আর Android-এর [অধ্যায় ১৩](#ch13) এক জায়গায়:

| বিষয় | iOS | Android | Flutter app-এ (দুই platform-এ) |
|---|---|---|---|
| Native code কীসে চলে | machine code (LLVM), VM নেই | `.dex`, ART-এ | Dart: release-এ AOT machine code |
| Memory | ARC — cycle নিজে ভাঙতে হয় | GC | Dart GC; native অংশ platform-এর নিয়মে |
| JIT | App Store app-এ নিষেধ | ART-এ আছে | শুধু debug-এ (hot reload) |
| App-এর process কোথা থেকে আসে | launchd, প্রতিবার নতুন | Zygote থেকে fork | একই — platform-এর নিয়মে |
| Library কে জোড়ে | dyld (+ shared cache) | ART class loading, `.so` load | engine: `Flutter.framework` / `libflutter.so` |
| শুরু কোথা থেকে | `main()` → `UIApplicationMain` → AppDelegate → Scene | `ActivityThread.main()` → Application → Activity | `FlutterAppDelegate` + `FlutterSceneDelegate` / `FlutterActivity` |
| Main loop | run loop | Looper | platform thread = main thread (3.29 থেকে Dart-ও সেখানে) |
| Launch screen | `UILaunchScreen` / storyboard | starting window (`LaunchTheme`) | একই, platform-এর |
| Launch-এ বেশি দেরি হলে | watchdog মেরে ফেলে (`0x8badf00d`) | ANR dialog | একই |
| Native UI কে আঁকে | Core Animation → render server (Metal) | HWUI → Skia (GL/Vulkan) | Impeller (Metal / Vulkan, না থাকলে GL) |
| শেষে কে মেশায় | render server | SurfaceFlinger | একই, platform-এর |
| Vsync | `CADisplayLink` | `Choreographer` | engine সেখান থেকেই নেয় |
| Build tool | Xcode build system (`xcodebuild`) | Gradle + AGP | `flutter` tool → এই দুইটাকেই ডাকে |
| Dependency | Swift Package Manager (CocoaPods পুরনো) | Maven (Gradle) | pub.dev + এই দুই |
| Dart-এর output | `App.framework/App` | `libapp.so` | `gen_snapshot` দুটোই বানায় |
| Engine-এর file | `Flutter.framework` | `libflutter.so` | — |
| Package | `.ipa` (`Payload/X.app`) | APK / AAB | — |
| Sign | certificate + provisioning profile | keystore | platform-এর নিয়মে |
| Memory দেখার tool | Instruments, Memory Graph | Memory Profiler, Perfetto | Dart heap: DevTools |

> **মনে রাখুন**
> - Swift build-এর সময়েই LLVM দিয়ে machine code হয়ে যায়। VM নেই। JIT নিষেধ। তাই Flutter-এর iOS release সবসময় AOT।
> - ARC: হিসাব শূন্য হলেই object মুছে যায়, GC pause নেই। কিন্তু cycle নিজেকে ভাঙতে হয় — closure-এ `[weak self]` দিন।
> - App খোলার পথ: SpringBoard → launchd → dyld → `UIApplicationMain` → AppDelegate → Scene → প্রথম frame। Flutter-এ মাঝখানে আসে `FlutterViewController`, engine আর Dart-এর `main()`।
> - Native UI আঁকে Core Animation + render server + Metal। Flutter একটা `CAMetalLayer`-এর ভেতরে Impeller দিয়ে নিজে আঁকে। iOS-এ Impeller-ই একমাত্র renderer।
> - Build: swiftc → ld → actool → embed → codesign → `.app` → `.ipa`। Flutter-এর Dart code যায় `App.framework`-এ, আর engine থাকে `Flutter.framework`-এ।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "Swift সরাসরি LLVM দিয়ে machine code হয়। iOS-এ কোনো VM নেই, আর App Store app-এ JIT নিষেধ। এজন্যই Flutter-এর iOS release সবসময় AOT — Dart code machine code হয়ে App.framework-এ থাকে। Memory চলে ARC দিয়ে, তাই GC pause নেই। কিন্তু retain cycle আমাকে নিজে weak দিয়ে ভাঙতে হয়। App খুললে launchd process চালু করে, dyld library জোড়া দেয়, আর UIApplicationMain AppDelegate আর Scene বানায়। Flutter-এ এরপর FlutterViewController engine চালু করে Dart-এর main চালায়। Native UI তার Core Animation layer tree render server-এ পাঠায়। আর Flutter একটা CAMetalLayer-এর ভেতরে Impeller দিয়ে Metal-এ নিজে সব আঁকে।"
> - *English:* "Swift is compiled straight to machine code by LLVM; there's no VM on iOS, and JIT isn't allowed for App Store apps — that's why Flutter's iOS release is always AOT, with the Dart code as machine code in App.framework. Memory is managed by ARC, so there are no GC pauses, but I have to break retain cycles myself with weak. On launch, launchd starts the process, dyld links the libraries, and UIApplicationMain creates the AppDelegate and the scene; in Flutter, the FlutterViewController starts the engine and runs Dart's main. Native UI sends a Core Animation layer tree to the render server, while Flutter draws everything itself with Impeller on Metal into a CAMetalLayer."

[উপরে ফিরুন](#toc)

---

## <a id="ios13"></a>iOS ১৩. iOS শেখার পরিকল্পনা — ৪ সপ্তাহ

Android-এর মতোই, শুধু পড়ে শেখার চেয়ে বানিয়ে শেখা অনেক দ্রুত। আর সবচেয়ে দ্রুত পথ একটাই: **এই বই জুড়ে যে Notes app দেখলেন, সেটা native iOS-এ বানানো।** প্রতিটা অংশ Flutter-এ কীভাবে লিখতেন, সেটা আপনি জানেন। এখন শুধু সেটা iOS-এ অনুবাদ করবেন।

**শুরুর আগে যা লাগবে:**

- একটা Mac।
- App Store থেকে নামানো সর্বশেষ Xcode।
- সম্ভব হলে একটা iPhone।

নিজের phone-এ app চালাতে free Apple ID-ই যথেষ্ট। কিন্তু Push, Associated Domains আর TestFlight-এর জন্য paid Apple Developer Program লাগবে ([iOS ১১.১](#ios11-1))। Project-এর minimum iOS 17 রাখুন। তাহলে `@Observable` আর SwiftData দুটোই পাবেন।

### <a id="ios13-1"></a>iOS ১৩.১ চার সপ্তাহের পরিকল্পনা

| সপ্তাহ | পড়ুন | বানান |
|---|---|---|
| ১ | [iOS ০](#ios0), [১](#ios1), [২](#ios2) | Xcode-এর Playground-এ Notes-এর model বানান: `struct Note`, sort-এর ধরনের জন্য একটা `enum`, আর `protocol NotesRepository`। একটা `actor` দিয়ে memory-তে রাখার store বানান। `async`/`await` দিয়ে নকল network delay দিন। |
| ২ | [iOS ৩](#ios3)–[৬](#ios6) | নতুন একটা SwiftUI project খুলুন। Note-এর list, একটা note খোলা, আর নতুন note-এর form বানান — data শুধু memory-তে থাকবে। Navigation করুন `NavigationStack` দিয়ে। তারপর app background-এ পাঠিয়ে আবার খুলুন। দেখুন কী থাকে, কী হারায়। |
| ৩ | [iOS ৭](#ios7), [৮](#ios8) | `@Observable` view model বানান, আর composition root-এ DI করুন। Note রাখুন SwiftData-তে। একটা free mock server থেকে `URLSession` দিয়ে sync করুন, JSON পড়ুন `Codable` দিয়ে। Token রাখুন Keychain-এ। তারপর app মুছে আবার install করুন, দেখুন token থেকে গেছে কি না। |
| ৪ | [iOS ৯](#ios9)–[১২](#ios12) | Reminder-এর জন্য local notification দিন। `BGAppRefreshTask` দিয়ে sync করুন (debugger command দিয়ে চালিয়ে দেখুন)। Swift Testing-এ view model-এর test লিখুন, আর একটা XCUITest। Archive করে TestFlight-এ পাঠান। শেষে একটা Flutter project-এ `flutter build ipa` চালান, তারপর `.ipa` unzip করুন। `App.framework` আর `Flutter.framework` নিজের চোখে দেখুন। |

**প্রতিদিনের শেষে নিজেকে তিনটা প্রশ্ন করুন:**

1. আজ যেটা লিখলাম, Flutter-এ সেটা কী দিয়ে করতাম? Android-এ কী দিয়ে? পার্থক্যটা কোথায়, আর কেন?
2. এই code কোন actor-এ চলছে — main actor-এ, নাকি অন্য কোথাও?
3. App suspend হলে, বা user swipe করে app বন্ধ করলে, এর কী হবে?

এই তিন প্রশ্নের উত্তর মুখে বলতে পারলে আপনি interview-এর জন্য তৈরি। প্রতিটা অধ্যায়ের শেষে যে **Interview-এ এক কথায়** box আছে, সেটা জোরে জোরে বলে অনুশীলন করুন।

[উপরে ফিরুন](#toc)

### <a id="ios-dictionary"></a>Flutter → iOS অভিধান

Interview-এর আগের রাতে শুধু এই পাতাটা পড়ুন। পাশে Android-ও রেখেছি, যাতে তিনটা একসাথে মনে থাকে।

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

সবগুলো official। প্রতিটা link নভেম্বর ২০২৬-এ খুলে দেখা হয়েছে।

- [Develop in Swift tutorials](https://developer.apple.com/tutorials/develop-in-swift) — নতুনদের জন্য Apple-এর নিজের পথ, SwiftUI আর SwiftData দিয়ে। প্রথম সপ্তাহের জন্য।
- [SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui) — হাতে-কলমে, ধাপে ধাপে screen বানানো।
- [The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/) — Swift-এর official বই। Optional, enum, protocol আর concurrency-র অধ্যায়গুলো আগে পড়ুন।
- [Swift 6 migration guide](https://www.swift.org/migration/documentation/migrationguide/) — strict concurrency-র error কেন আসে, আর কীভাবে ঠিক করবেন।
- [Migrating to the Observable macro](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro) — পুরনো `ObservableObject` code পড়তে আর নতুন রূপে বদলাতে।
- [SwiftData](https://developer.apple.com/documentation/swiftdata) আর [Swift Testing](https://developer.apple.com/documentation/testing) — এই দুই framework-এর official docs।
- [TN3187: UIScene lifecycle-এ যাওয়া](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) — scene lifecycle কেন বাধ্যতামূলক হচ্ছে, আর কীভাবে বদলাবেন।
- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) আর [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/) — প্রতিবার submit করার আগে দেখে নিন।
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) — আপনার app যেন "iOS-এর মতো" দেখায়।
- [Flutter for SwiftUI developers](https://docs.flutter.dev/flutter-for/swiftui-devs) — Flutter-এর official তুলনা, SwiftUI developer-দের জন্য লেখা। আপনি এটা উল্টো দিক থেকে পড়বেন — তাতে আপনার জন্য এটা একদম কাজের।
- [Flutter-এর iOS platform integration](https://docs.flutter.dev/platform-integration/ios/) আর [Platform channels](https://docs.flutter.dev/platform-integration/platform-channels) — Flutter app-এর ভেতরে Swift code কীভাবে লিখবেন।
- [Build and release an iOS app (Flutter)](https://docs.flutter.dev/deployment/ios) — `flutter build ipa`, signing, TestFlight।

> **মনে রাখুন**
> - Notes app-টা native-এ বানানোই সবচেয়ে দ্রুত শেখার পথ। Minimum iOS 17 রাখুন।
> - চার সপ্তাহ: ভাষা আর async → SwiftUI আর navigation → architecture আর data → platform, test, release, internals।
> - প্রতিদিন তিনটা প্রশ্ন: Flutter আর Android-এ এটা কী দিয়ে করতাম? কোন actor-এ চলছে? Suspend বা swipe হলে কী হবে?
> - Interview-এর আগের রাতে শুধু [অভিধান](#ios-dictionary) পড়ুন।

> **Interview-এ এক কথায়**
> - *বাংলায়:* "আমি Flutter-এর চোখ দিয়ে iOS শিখেছি। প্রতিটা Flutter ধারণার জন্য iOS-এ তার জোড়া খুঁজেছি — Cubit-এর জায়গায় @Observable view model, dio-র জায়গায় URLSession, drift-এর জায়গায় SwiftData, workmanager-এর জায়গায় BGTaskScheduler। তারপর একই Notes app native SwiftUI-তে বানিয়েছি, TestFlight পর্যন্ত। তাই plugin-এর ভেতরে কী হয়, আর কোন সমস্যা আসলে iOS-এর নিয়ম থেকে আসে — সেটা আমি বুঝিয়ে বলতে পারি।"
> - *English:* "I learned iOS through Flutter eyes: for every Flutter concept I found its iOS twin — Cubit to an @Observable view model, dio to URLSession, drift to SwiftData, workmanager to BGTaskScheduler. Then I built the same Notes app in native SwiftUI, all the way to TestFlight. So I can explain what happens inside a plugin, and which problems really come from iOS rules."

[উপরে ফিরুন](#toc)

---
