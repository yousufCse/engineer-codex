# Senior Flutter Engineer — Interview প্রস্তুতি
## সূচিপত্র ও Quick Reference Cheat Sheet

> 🇬🇧 এই ডকুমেন্টের ইংরেজি ভার্সন: [section-00-toc-cheatsheet.md](../software-engineer-flutter/section-00-toc-cheatsheet.md)

---

# PART I: সূচিপত্র

---

## Section 1: Dart Language-এর মূল বিষয়
- Null safety, sound type system, আর `?`, `!`, `??`, `late` keyword
- `var`, `final`, `const` — compile-time বনাম runtime constant
- Extension method, mixin, আর abstract class
- Generics, type inference, আর `dynamic` type
- Named, positional, আর required parameter

## Section 2: Dart Async Programming
- `Future`, `async`/`await`, আর event loop
- `Stream` — single-subscription বনাম broadcast
- `Completer` — নিজের হাতে Future control
- async code-এ error handling: `try/catch` বনাম `.catchError()`
- `Future.wait`, `Future.any`, `Future.delayed`

## Section 3: Flutter Widget Architecture
- `StatelessWidget` বনাম `StatefulWidget` — কখন আর কেন
- Widget/Element/RenderObject tree (তিনটি tree)
- `BuildContext` — এটা কী আর কেন গুরুত্বপূর্ণ
- `InheritedWidget` — data কীভাবে tree-এর নিচে ছড়ায়
- `const` constructor আর widget rebuild optimization

## Section 4: State Management
- `setState` আর কখন এটাই যথেষ্ট
- Provider — `ChangeNotifier`, `Consumer`, `Selector`
- Riverpod — `ref.watch`, `ref.read`, `ref.listen`, provider
- BLoC/Cubit — event-driven state, `StreamController`, `emit`
- Redux — store, reducer, middleware
- Project-এর আকার অনুযায়ী সঠিক approach বেছে নেওয়া

## Section 5: Flutter Rendering Pipeline
- তিনটি পর্যায়: Build → Layout → Paint
- `RenderObject` বনাম `Widget` — কার কী কাজ
- `RepaintBoundary` আর repaint আলাদা করা
- `CustomPaint` আর `Canvas` কীভাবে কাজ করে
- Layer tree আর compositing

## Section 6: Performance Optimization
- `const` widget আর widget rebuild-এর সমস্যা
- `ListView.builder` বনাম `ListView` — lazy loading
- `AutomaticKeepAliveClientMixin` — list-এ state ধরে রাখা
- `Keys` — `ValueKey`, `ObjectKey`, `GlobalKey` — কেন এগুলো গুরুত্বপূর্ণ
- `compute()` function — কাজ background isolate-এ পাঠানো
- Flutter DevTools দিয়ে profiling: CPU, memory, jank

## Section 7: Isolates ও Concurrency
- Dart-এর single-threaded model আর event loop
- Isolate কী আর thread থেকে কীভাবে আলাদা
- `Isolate.spawn` আর `compute()` দিয়ে isolate spawn করা
- `SendPort` / `ReceivePort` দিয়ে message passing
- `IsolateGroup` আর background isolate (Flutter 3+)
- কখন isolate ব্যবহার করবেন না

## Section 8: Navigation ও Routing
- `Navigator 1.0` — `push`, `pop`, `pushReplacement`, named route
- `Navigator 2.0` — `Router`, `RouteInformationParser`, `RouterDelegate`
- `go_router` — declarative routing, guard, deep linking
- Android-এ (intent filter) আর iOS-এ (universal link) deep linking
- Route-এর মধ্যে নিরাপদে argument পাঠানো

## Section 9: Networking ও HTTP
- `http` package বনাম `Dio` — feature আর tradeoff
- RESTful API call — GET, POST, PUT, DELETE pattern
- auth header, logging, আর retry logic-এর জন্য interceptor
- JSON serialization — `json_serializable`, `freezed`
- Error handling: HTTP error বনাম network error বনাম parsing error
- Certificate pinning আর HTTPS-এর best practice

## Section 10: Local Storage ও Persistence
- `SharedPreferences` — key-value, সীমাবদ্ধতা
- `Hive` — NoSQL, দ্রুত, offline-first
- `sqflite` / `drift` — relational data
- `flutter_secure_storage` দিয়ে secure storage
- আপনার use case-এর জন্য persistence strategy বেছে নেওয়া

## Section 11: Platform Channels ও Native Integration
- `MethodChannel` — Dart থেকে native code call করা
- `EventChannel` — native থেকে Dart-এ data stream করা
- `BasicMessageChannel` — raw binary messaging
- Plugin লেখা: Android (Kotlin) + iOS (Swift) দিক
- FFI (Foreign Function Interface) — সরাসরি C library call করা

## Section 12: Animations
- `AnimationController`, `Tween`, `AnimatedBuilder`
- Implicit animation — `AnimatedContainer`, `AnimatedOpacity`, ইত্যাদি
- Explicit animation — যখন পুরো control দরকার
- `Hero` animation — shared element transition
- `Rive` আর `Lottie` — জটিল vector animation
- canvas drawing দিয়ে `CustomPainter` animation

## Section 13: Flutter-এ Testing
- Unit test — শুধু Dart logic, কোনো Flutter dependency নেই
- Widget test — `pumpWidget`, `find`, `tap`, `expect`
- Integration test — `flutter_test`, `patrol`
- `mockito` আর `mocktail` দিয়ে mocking
- Golden test — pixel-perfect UI regression
- Test coverage আর CI integration

## Section 14: Clean Architecture ও Design Patterns
- Clean Architecture-এর layer: Presentation → Domain → Data
- Repository pattern — data source আড়াল করা
- Flutter/Dart-এ SOLID principle কাজে লাগানো
- Dependency Injection — `get_it`, `injectable`
- Flutter-এ Factory, Singleton, Observer pattern
- Feature-first বনাম layer-first folder structure

## Section 15: Flutter Web ও Desktop
- Flutter Web কীভাবে render করে: CanvasKit বনাম HTML renderer
- Web-এর নিজের সীমাবদ্ধতা: isolate নেই, CORS, SEO
- Responsive design — `LayoutBuilder`, `MediaQuery`, `AdaptiveScaffold`
- Desktop-এর নিজের বিষয়: keyboard shortcut, window management, menu
- সব platform-এ code sharing-এর strategy

## Section 16: Flutter-এর জন্য CI/CD ও DevOps
- `fastlane` — build, signing, আর deployment automatic করা
- GitHub Actions / Bitrise — Flutter pipeline setup
- Code signing: Android keystore, iOS provisioning profile
- Flavor — dev, staging, production environment
- beta delivery-র জন্য Firebase App Distribution বনাম TestFlight
- Semantic versioning আর automatic version bump

## Section 17: Flutter App-এ Security
- Secret রাখা: কখনোই source code-এ নয়, `.env` + `--dart-define` ব্যবহার করুন
- `--obfuscate` আর `--split-debug-info` দিয়ে obfuscation
- MITM attack ঠেকাতে certificate pinning
- sensitive data-র জন্য `flutter_secure_storage` বনাম `SharedPreferences`
- Jailbreak/root detection-এর pattern
- OWASP Mobile Top 10 সম্পর্কে ধারণা

## Section 18: Streams ও Reactive Programming
- `Stream` বনাম `Future` — মূল পার্থক্য
- `StreamController` — stream তৈরি আর চালানো
- সাধারণ stream operator: `map`, `where`, `debounce`, `distinct`
- `RxDart` — `BehaviorSubject`, `PublishSubject`, `ReplaySubject`
- Stream-এর lifecycle: listen, pause, cancel, error handling
- Backpressure আর stream buffering

## Section 19: Accessibility ও Internationalisation
- `Semantics` widget — screen reader support
- `SemanticsLabel`, `excludeSemantics`, focus management
- i18n-এর জন্য `flutter_localizations` + ARB file
- RTL (right-to-left) ভাষার support
- Dynamic font scaling — `MediaQuery.textScaleFactor`
- TalkBack / VoiceOver দিয়ে accessibility test করা

## Section 20: Error Handling ও Observability
- `FlutterError.onError` — Flutter framework-এর error ধরা
- `PlatformDispatcher.instance.onError` — না-ধরা async error
- `Zone` — error ধরতে পুরো app মুড়ে দেওয়া
- functional error handling-এর জন্য `Either` type pattern
- Crash reporting: Firebase Crashlytics, Sentry integration
- Production-এ structured logging আর log level

## Section 21: App Architecture ও Scalability
- বড় Flutter project-এর জন্য monorepo বনাম multi-repo
- Module federation — feature package, shared package
- `melos` — multi-package Flutter monorepo চালানো
- Code generation: `build_runner`, `freezed`, `json_serializable`
- Breaking API change সামলানো — versioning strategy
- Feature flag আর remote configuration

## Section 22: Flutter Internals ও Advanced Dart
- `BuildContext` কীভাবে `Element` implement করে
- `GlobalKey` — সরাসরি widget state access আর তার performance খরচ
- Hot reload কীভাবে কাজ করে (আর কেন কখনো কখনো fail করে)
- Tree shaking আর AOT বনাম JIT compilation
- Dart VM service protocol আর DevTools-এর ভেতরের কাজ
- Scheduler আর frame pipeline: `SchedulerBinding`, `WidgetsBinding`

---
---

# PART II: QUICK REFERENCE CHEAT SHEET
### শেষ রাতের Review — এগুলো একদম মুখস্থ রাখুন

---

**Section 1: Dart Language-এর মূল বিষয়**
- `const` = compile-time constant (immutable, canonicalized); `final` = runtime constant (একবারই set হয়)।
- Null safety: `?` nullable বানায়, `!` non-null বলে দাবি করে (null হলে runtime-এ throw করে), `late` init পরে করায়।
- Mixin `with` দিয়ে ব্যবহার হয়, এর constructor থাকতে পারে না; `extends` = single inheritance; `implements` = শুধু contract।

---

**Section 2: Dart Async Programming**
- Dart single-threaded; `async/await` হলো Future-এর উপরে syntax sugar — এটা কোনো thread তৈরি করে না।
- Single-subscription stream-এ একটাই listener থাকতে পারে; broadcast stream-এ অনেক listener থাকতে পারে।
- `Completer` দিয়ে একটা Future বানিয়ে নিজে হাতে resolve করা যায় — callback API মুড়তে কাজে লাগে।

---

**Section 3: Flutter Widget Architecture**
- তিনটি tree: Widget (blueprint/immutable) → Element (lifecycle/state) → RenderObject (layout/paint)।
- `BuildContext` আসলে `Element`-ই — এটা tree-তে widget-এর অবস্থান জানে।
- `InheritedWidget` data নিচের দিকে ছড়ায়; `of(context)` call করা widget-কে dependent হিসেবে register করে (নিজে থেকেই rebuild হয়)।

---

**Section 4: State Management**
- `setState` পুরো `build()` method rebuild করে — শুধু local আর আলাদা state-এর জন্য ঠিক আছে।
- BLoC: event ভেতরে যায়, state বাইরে আসে — `StreamController` কখনোই সরাসরি expose করবেন না; `Stream` getter ব্যবহার করুন।
- Riverpod-এর `ref.watch` পরিবর্তন হলে rebuild করে; `ref.read` একবারই পড়ে (শুধু callback বা side effect-এ ব্যবহার করুন)।

---

**Section 5: Flutter Rendering Pipeline**
- ক্রম সবসময় একই: Build → Layout → Paint — layout-এর আগে paint করা যায় না।
- `RepaintBoundary` আলাদা compositing layer তৈরি করে — যে widget বারবার repaint হয়, সেটা আলাদা করতে ব্যবহার করুন।
- `RenderObject` আসল কাজটা করে (size, position, paint); `Widget` শুধু একটা configuration object।

---

**Section 6: Performance Optimization**
- `const` widget কখনোই rebuild হয় না আর memory-তে canonicalized থাকে — যেখানে সম্ভব সেখানেই ব্যবহার করুন।
- `ListView.builder` item-গুলো lazily তৈরি করে (দরকার হলে); `ListView` সব children একসাথে build করে।
- `build()`-এ কখনোই ভারী computation করবেন না — এটা UI thread-এ চলে আর frame আটকে দেয়।

---

**Section 7: Isolates ও Concurrency**
- Isolate-এর আলাদা memory heap থাকে — কোনো shared state নেই, শুধু message passing দিয়ে কথা হয়।
- `compute(fn, arg)` একটা সহজ wrapper — এটা isolate spawn করে আর একটা Future ফেরত দেয়।
- ছোট কাজের জন্য isolate ব্যবহার করবেন না — spawn করার খরচ আছে; 16 ms-এর বেশি CPU কাজের জন্য ব্যবহার করুন।

---

**Section 8: Navigation ও Routing**
- Navigator 1.0 imperative (push/pop); Navigator 2.0 declarative (URL-চালিত state)।
- `go_router` deep link, redirect (guard), আর nested navigation পরিষ্কারভাবে সামলায়।
- সবসময় `GoRouter.of(context).go()` আর `push()`-এর পার্থক্য বুঝে ব্যবহার করুন — `go` stack replace করে (back button থাকে না), `push` যোগ করে।

---

**Section 9: Networking ও HTTP**
- Dio-তে interceptor, cancellation, FormData, আর timeout config সরাসরি পাওয়া যায়; `http` খুবই সাধারণ।
- তিন ধরনের failure সবসময় আলাদাভাবে handle করুন: HTTP status error, network/timeout error, parse error।
- API key কখনোই Dart source-এ রাখবেন না — `--dart-define=KEY=value` ব্যবহার করুন আর `const String.fromEnvironment` দিয়ে পড়ুন।

---

**Section 10: Local Storage ও Persistence**
- `SharedPreferences` encrypted নয় — সেখানে কখনোই token, password, বা PII রাখবেন না।
- সাধারণ object-এর জন্য Hive, SQLite-এর চেয়ে দ্রুত, কারণ এটা binary আর parsing লাগে না।
- `drift` (আগের নাম moor) = type-safe SQLite, stream দিয়ে reactive query পাওয়া যায়।

---

**Section 11: Platform Channels ও Native Integration**
- `MethodChannel` async আর দুই দিকেই কাজ করে — Dart native-কে call করে, native-ও Dart-কে call করতে পারে।
- `EventChannel` native থেকে Dart-এ একটানা stream পাঠানোর জন্য (যেমন sensor, Bluetooth)।
- CPU-bound native call-এর জন্য FFI, MethodChannel-এর চেয়ে দ্রুত — কোনো serialization খরচ নেই।

---

**Section 12: Animations**
- `AnimationController` সব explicit animation চালায় — এর জন্য একটা `Ticker` লাগে (`SingleTickerProviderStateMixin` থেকে)।
- `Tween.animate(controller)` = CurvedAnimation + value mapping; `AnimatedBuilder` শুধু নিজের subtree rebuild করে।
- `Hero` animation-এর জন্য source আর destination দুই widget-এ একই `tag` লাগে।

---

**Section 13: Flutter-এ Testing**
- Unit test = শুধু Dart, Flutter নেই; widget test = `pumpWidget` + fake Flutter environment; integration test = আসল device।
- `pump()` এক frame এগিয়ে দেয়; `pumpAndSettle()` তখনই থামে যখন আর কোনো animation বা pending future থাকে না।
- Golden test pixel output-কে সংরক্ষিত একটা `.png`-এর সাথে মেলায় — CI-তে visual regression ঠেকাতে দারুণ।

---

**Section 14: Clean Architecture ও Design Patterns**
- Dependency-র নিয়ম: বাইরের layer ভেতরের layer-এর উপর নির্ভর করে; Domain layer-এ Flutter বা বাইরের কোনো dependency থাকে না।
- Repository pattern লুকিয়ে রাখে data কোথা থেকে আসছে — API, cache, না database; caller-এর তাতে কিছু যায় আসে না।
- `get_it` একটা service locator (আসল DI নয়); code generation-সহ constructor injection-এর জন্য `injectable` ব্যবহার করুন।

---

**Section 15: Flutter Web ও Desktop**
- CanvasKit renderer = pixel-perfect, ভারী (2MB WASM download); HTML renderer = হালকা, কম নিখুঁত।
- `LayoutBuilder` parent-এর constraint দেয়; `MediaQuery` screen-এর মাপ দেয় — responsive UI-র জন্য দুটোই ব্যবহার করুন।
- Flutter Web-এ isolate support নেই — web-এ background কাজের জন্য JS interop দিয়ে `web workers` ব্যবহার করুন।

---

**Section 16: Flutter-এর জন্য CI/CD ও DevOps**
- Flavor = আলাদা `main_dev.dart`, `main_prod.dart` entry point + Android productFlavors + iOS scheme।
- keystore বা `.p12` file কখনোই commit করবেন না — CI-র secret store ব্যবহার করুন আর build-এর সময় inject করুন।
- `fastlane match` iOS cert/profile একটা git repo-তে রাখে — team-এর সবাই একটা command দিয়েই sync করে নেন।

---

**Section 17: Flutter App-এ Security**
- `--obfuscate --split-debug-info=./symbols` reverse engineering অনেক কঠিন করে দেয়; crash symbolication-এর জন্য symbol রেখে দিন।
- Certificate pinning: app-এ expected cert hash রাখুন, না মিললে connection বাতিল করুন — এতে MITM আটকে যায়।
- `flutter_secure_storage` Android Keystore / iOS Keychain ব্যবহার করে — OS-level hardware-backed encryption।

---

**Section 18: Streams ও Reactive Programming**
- একটা `StreamController` শোনার জন্য `.stream` দেয় আর event যোগ করার জন্য `.sink` দেয় — controller নিজে কখনোই expose করবেন না।
- `BehaviorSubject` (RxDart) নতুন subscriber-কে শেষ value আবার পাঠায় — state-এর জন্য ব্যবহার করুন; `PublishSubject` তা করে না।
- `dispose()`-এ stream subscription সবসময় cancel করুন — cancel না করা subscription memory leak-এর খুব সাধারণ কারণ।

---

**Section 19: Accessibility ও Internationalisation**
- text নয় এমন widget-কে `Semantics(label: '...')` দিয়ে মুড়ে দিন, যেন screen reader সেগুলো বর্ণনা করতে পারে।
- ARB file-এ string key + অনুবাদ থাকে; `flutter gen-l10n` type-safe accessor class তৈরি করে।
- `MediaQuery.of(context).textScaleFactor` > 1 মানে user system font বড় করেছেন — আপনার layout-কে এটা সামলাতেই হবে।

---

**Section 20: Error Handling ও Observability**
- `FlutterError.onError` widget/framework-এর error ধরে; `PlatformDispatcher.instance.onError` না-সামলানো async error ধরে — দুটোই set করুন।
- `runApp()`-কে `runZonedGuarded()` দিয়ে মুড়ে দিন, যেন দুই handler ফাঁকি দেওয়া synchronous error ধরা পড়ে।
- `Either<Failure, Success>` (`dartz` থেকে) caller-কে দুই পথই handle করতে বাধ্য করে — চুপচাপ কোনো failure হয় না।

---

**Section 21: App Architecture ও Scalability**
- `melos` monorepo bootstrap করে: local package-গুলো link করে, সব package-এ একসাথে script চালায়।
- Feature package শুধু `core` আর `domain` package import করবে — অন্য feature package কখনোই সরাসরি import করবে না।
- Development-এ `build_runner watch` file বদলালেই আবার code generation চালায় — CI-র জন্য `build_runner build --delete-conflicting-outputs`।

---

**Section 22: Flutter Internals ও Advanced Dart**
- Hot reload widget tree আবার load করে, কিন্তু `initState()` বা `main()` আবার চালায় না — state ঠিক থাকে।
- AOT (Ahead of Time) = release mode-এ native ARM-এ compile হয় → দ্রুত startup, কোনো JIT খরচ নেই।
- `SchedulerBinding.instance.addPostFrameCallback()` পরের frame-এর পরে code চালায় — `Future.delayed(Duration.zero)`-এর বদলে এটা ব্যবহার করুন।

---

*Quick Reference Cheat Sheet শেষ*
