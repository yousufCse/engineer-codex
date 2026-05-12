# Flutter Mobile Tech Lead — সম্পূর্ণ গাইড

### "একজন Flutter Developer থেকে Mobile Tech Lead হওয়ার বাস্তব পথ"

> **লেখার উদ্দেশ্য:** এই document টা শুধু তোমার জন্য — একজন Senior Flutter Developer যে Mobile Tech Lead হতে চায়। System Design এর গভীরে না গিয়ে, mobile-specific leadership এ focus করে সম্পূর্ণ practical roadmap।

---

<a id="toc"></a>

## 📚 Table of Contents

| # | Section |
|---|---------|
| 1 | [Tech Lead কী — সত্যিকারের সংজ্ঞা](#what-is-tech-lead) |
| 2 | [Mobile Tech Lead কি System Design শিখতে হবে?](#system-design) |
| 3 | [Mobile Tech Lead এর দায়িত্ব — সম্পূর্ণ তালিকা](#responsibilities) |
| 4 | [Technical Excellence — Flutter এ Master হওয়া](#technical-excellence) |
| 5 | [Architecture — Mobile App এর জন্য](#architecture) |
| 6 | [Code Quality ও Code Review](#code-quality) |
| 7 | [Team Leadership ও Mentoring](#team-leadership) |
| 8 | [Project Planning ও Task Management](#project-planning) |
| 9 | [Communication Skills](#communication) |
| 10 | [Performance ও Optimization](#performance) |
| 11 | [Testing Strategy](#testing) |
| 12 | [CI/CD ও DevOps — Mobile এর জন্য](#cicd) |
| 13 | [Security — Mobile App এ](#security) |
| 14 | [Release Management](#release-management) |
| 15 | [Documentation](#documentation) |
| 16 | [Hiring ও Interview নেওয়া](#hiring) |
| 17 | [১২ মাসের Roadmap](#roadmap) |
| 18 | [Resources ও Tools](#resources) |

---

<a id="what-is-tech-lead"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 1 — Tech Lead কী? সত্যিকারের সংজ্ঞা
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### সাধারণ ধারণা vs বাস্তব

অনেকে মনে করে Tech Lead মানে —
- সবচেয়ে বেশি code লেখে যে
- সবচেয়ে বেশি জানে যে
- Manager এর নিচে আরেকটা step

এই ধারণা **সম্পূর্ণ ভুল।**

### বাস্তব সংজ্ঞা

```
Tech Lead হলো সেই ব্যক্তি যে:

  নিজে ভালো code লেখে
        +
  পুরো team কে ভালো code লিখতে সক্ষম করে
        +
  Technical decisions নেয় এবং দায়িত্ব নেয়
        +
  Team ও Management এর মধ্যে bridge হিসেবে কাজ করে
```

### Tech Lead vs Team Lead — পার্থক্য

অনেক company তে এই দুটো title একসাথে থাকে, কোথাও আলাদা।

```
┌─────────────────────────────────────────────────────────┐
│  Tech Lead                   Team Lead                  │
│  ─────────────────────────   ──────────────────────── │
│  Technical decisions নেয়    People management করে      │
│  Architecture define করে    Hiring, firing এ involve    │
│  Code review করে            Performance review করে      │
│  Coding এ ৪০-৬০% time দেয়  Coding এ ২০-৩০% time দেয় │
│  Technical mentoring করে    Career growth guide করে     │
│  Technical risk manage করে  Team dynamics manage করে   │
└─────────────────────────────────────────────────────────┘
```

Mobile এ সাধারণত একজনই দুটো role পালন করে — বিশেষ করে ছোট ও মাঝারি team এ।

### Senior Developer vs Tech Lead — Mindset পার্থক্য

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  Senior Developer চিন্তা করে:                              │
│  "এই feature টা আমি কীভাবে best implement করবো?"           │
│                                                              │
│  Tech Lead চিন্তা করে:                                      │
│  "এই feature টা team মিলে কীভাবে best implement করবো       │
│   যাতে সবাই শিখতে পারে এবং deadline এ শেষ হয়?"          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### তুমি কি Ready?

Senior Flutter Developer হিসেবে তুমি technically ready। এখন দরকার:

- **Mindset shift** — "আমি" থেকে "আমরা"
- **Skill expansion** — coding এর বাইরে যাওয়া
- **Intentional practice** — leadership consciously practice করা

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="system-design"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 2 — Mobile Tech Lead কি System Design শিখতে হবে?
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### সরাসরি উত্তর

> **না — Backend System Design তোমার এখনকার priority না।**
> কিন্তু **Mobile Architecture Design** অবশ্যই শিখতে হবে।

এই দুটো সম্পূর্ণ আলাদা জিনিস।

### দুটোর পার্থক্য

```
┌──────────────────────────────────────────────────────────┐
│  Backend System Design          Mobile Architecture      │
│  ──────────────────────────     ──────────────────────  │
│  Server scaling কীভাবে         App layer কীভাবে সাজাবো │
│  Database sharding              State management কোনটা  │
│  Load balancer কোথায়           Navigation pattern       │
│  Microservices vs Monolith      Widget tree structure    │
│  Cache layer কীভাবে            Data flow কীভাবে        │
│  Message queue কোথায়           Offline support কীভাবে  │
│                                                          │
│  ← Backend Team Lead এর কাজ    ← তোমার কাজ →          │
└──────────────────────────────────────────────────────────┘
```

### Mobile Tech Lead হিসেবে তোমার System Design Knowledge

তোমাকে backend system design expert হতে হবে না। কিন্তু এটুকু বুঝতে হবে:

**১. API Design বোঝা**
Backend team যখন API design করে, তুমি mobile developer এর দৃষ্টিকোণ থেকে input দিতে পারবে।
```
"এই API response এ pagination কীভাবে হবে?"
"Offline mode এ কী data cache করা দরকার?"
"Real-time update দরকার — WebSocket নেবো না Polling?"
```

**২. Performance Implication বোঝা**
Backend এর একটা decision mobile app কে কীভাবে affect করে।
```
"এত বড় payload mobile এ slow feel দেবে"
"এই endpoint টা প্রতি second এ call হচ্ছে — battery drain হবে"
```

**৩. Integration Pattern বোঝা**
REST, GraphQL, WebSocket, gRPC — কোনটা কখন।

### Mobile Architecture Design — এটাই তোমার Focus

এটা তুমি অবশ্যই master করবে। বিস্তারিত Chapter 5 এ আছে।

```
Mobile Architecture তুমি যা জানতে হবে:

  ✅ Clean Architecture (Presentation, Domain, Data layers)
  ✅ State Management patterns (BLoC, Riverpod, Provider)
  ✅ Repository Pattern
  ✅ Dependency Injection
  ✅ Offline-first Architecture
  ✅ Navigation Architecture
  ✅ Feature-first vs Layer-first folder structure
```

### উপসংহার

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  এখন শিখবে না:      Full backend system design           │
│                      Database sharding, load balancing    │
│                      Distributed systems theory           │
│                                                           │
│  এখনই শিখবে:        Mobile app architecture              │
│                      API integration patterns             │
│                      Mobile performance optimization      │
│                      Team technical leadership            │
│                                                           │
│  ভবিষ্যতে শিখবে:    যখন Engineering Manager হবে তখন     │
│                      বা full-stack lead হবে              │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="responsibilities"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 3 — Mobile Tech Lead এর সম্পূর্ণ দায়িত্ব
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### বড় ছবি — তুমি কোথায় বসো

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Product Manager / CTO / Engineering Manager           │
│                    ↕                                    │
│            Mobile Tech Lead ← তুমি                     │
│                    ↕                                    │
│    ┌───────────────┼───────────────┐                   │
│    ↓               ↓               ↓                   │
│  Senior Dev    Mid-level Dev    Junior Dev             │
│                                                         │
│  তুমি উপরে ও নিচে দুদিকেই communicate করো             │
└─────────────────────────────────────────────────────────┘
```

### সময় কীভাবে ভাগ হবে

Industry standard অনুযায়ী Mobile Tech Lead এর সময়:

```
┌──────────────────────────────────────────────────────┐
│                                                      │
│  Coding & Technical Work        ████████░░  40-50%  │
│  Code Review                    ████░░░░░░  20-25%  │
│  Team Mentoring & Support       ███░░░░░░░  15-20%  │
│  Planning & Architecture        ██░░░░░░░░  10-15%  │
│  Meetings & Communication       ██░░░░░░░░  10-15%  │
│                                                      │
└──────────────────────────────────────────────────────┘
```

> **গুরুত্বপূর্ণ:** Tech Lead এখনো সক্রিয়ভাবে code করে। যদি তুমি coding সম্পূর্ণ ছেড়ে দাও — তুমি tech lead না, manager হয়ে যাচ্ছো।

### সম্পূর্ণ দায়িত্বের তালিকা

#### ক) Technical Responsibilities

**১. Architecture Decisions**
- App এর overall structure decide করা
- State management solution choose করা
- Package/library evaluate করা এবং approve করা
- Technical debt manage করা
- Breaking changes plan করা

**২. Code Quality Ownership**
- Coding standards define করা
- Linting rules setup করা
- Code review process চালু করা
- Refactoring prioritize করা

**৩. Technical Risk Management**
- "এই approach টা future এ problem করবে" বলতে পারা
- Third-party package dependency risk বোঝা
- Flutter/Dart version upgrade plan করা
- OS compatibility issue আগে থেকে চিহ্নিত করা

**৪. Performance Ownership**
- App startup time monitor করা
- Frame rate (jank) track করা
- Memory leak ধরা
- Battery usage optimize করা
- App size manage করা

**৫. Security**
- Sensitive data storage policy
- API key management
- Certificate pinning
- Code obfuscation

#### খ) Team Responsibilities

**১. Mentoring ও Knowledge Transfer**
- Junior developers গাইড করা
- Code review এ শেখানো
- Weekly knowledge sharing session
- Pair programming

**২. Hiring Support**
- Technical interview নেওয়া
- Code challenge তৈরি করা
- Candidate evaluate করা

**৩. Team Culture**
- Psychological safety তৈরি করা — সবাই freely কথা বলতে পারে
- Blameless culture — mistake হলে system কে blame করা, মানুষকে না
- Continuous learning encourage করা

#### গ) Process Responsibilities

**১. Sprint Planning**
- Task breakdown করা
- Estimation করা (Story points বা hours)
- Dependencies চিহ্নিত করা
- Blocker আগে থেকে চেনা

**২. Release Management**
- Release checklist manage করা
- App Store / Play Store submission coordinate করা
- Hotfix process define করা

**৩. Documentation**
- Architecture document maintain করা
- Onboarding guide তৈরি করা
- Decision log রাখা (কেন এই decision নেওয়া হয়েছে)

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="technical-excellence"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 4 — Technical Excellence — Flutter এ Master হওয়া
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### কেন Technical Excellence দরকার

Tech Lead হিসেবে তোমার technical credibility থাকতে হবে। Team যদি তোমার technical judgment এ trust না করে — তুমি effectively lead করতে পারবে না।

> **Rule:** তোমাকে team এর সবচেয়ে ভালো coder হতে হবে না। কিন্তু তোমাকে যেকোনো technical decision এর trade-off ব্যাখ্যা করতে হবে।

### Flutter Technical Depth — সম্পূর্ণ Checklist

#### ১. Dart Language — Advanced

```
✅ Sound null safety — সম্পূর্ণ বোঝা
✅ Generics — <T> type parameters
✅ Extension methods
✅ Mixins ও Abstract classes
✅ Isolates — parallel computation
✅ async/await, Future, Stream — deep understanding
✅ Const constructors — কখন কেন ব্যবহার করবে
✅ Factory constructors
✅ Operator overloading
✅ Records (Dart 3.0+)
✅ Patterns ও Pattern matching (Dart 3.0+)
✅ Sealed classes (Dart 3.0+)
```

**Isolates — কেন গুরুত্বপূর্ণ:**

```dart
// ❌ ভুল — Heavy computation main thread এ
Future<void> processLargeData(List<dynamic> data) async {
  // এটা UI thread block করবে, app freeze হবে
  final result = data.map((item) => heavyComputation(item)).toList();
}

// ✅ সঠিক — Isolate এ move করো
Future<List<ProcessedData>> processLargeData(List<dynamic> data) async {
  // compute() function automatically Isolate তে চালায়
  return await compute(heavyComputationIsolate, data);
}

// Note: compute() / Isolate.run() এ closure ও কাজ করে (Dart 2.15+ / Flutter 3.7+)
// তবে top-level function ব্যবহার করা best practice এবং Isolate.spawn() এ এখনো দরকার
List<ProcessedData> heavyComputationIsolate(List<dynamic> data) {
  return data.map((item) => heavyComputation(item)).toList();
}
```

#### ২. Flutter Framework — Deep Understanding

```
Widget Lifecycle:
✅ StatelessWidget vs StatefulWidget — কখন কোনটা
✅ initState, didChangeDependencies, build,
   didUpdateWidget, deactivate, dispose
✅ Keys — LocalKey, GlobalKey, ValueKey, ObjectKey কখন কোনটা
✅ InheritedWidget — কীভাবে কাজ করে (Provider এর ভেতরে এটা)
✅ BuildContext — কী এবং কীভাবে কাজ করে

Rendering:
✅ Three trees: Widget tree, Element tree, RenderObject tree
✅ Constraints go down, sizes go up, parent sets position
✅ CustomPainter — কখন দরকার
✅ RepaintBoundary — কখন ব্যবহার করবে
✅ Sliver — CustomScrollView এর ভেতরে

Performance Widgets:
✅ const Widget — কোথায় কোথায় দেওয়া যায়
✅ ListView.builder vs ListView — পার্থক্য
✅ AutomaticKeepAliveClientMixin — কখন দরকার
```

**Keys — সঠিক ব্যবহার:**

```dart
// ❌ ভুল — Key ছাড়া dynamic list
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => ItemWidget(item: items[index]),
)

// ✅ সঠিক — ValueKey দিয়ে Flutter কে identify করতে সাহায্য করো
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => ItemWidget(
    key: ValueKey(items[index].id), // unique identifier দাও
    item: items[index],
  ),
)
// Key না দিলে reorder/remove এ UI bug হয়
```

#### ৩. State Management — Expert Level

Tech Lead হিসেবে তোমাকে সব popular solution জানতে হবে এবং কোনটা কখন recommend করবে সেটা বলতে হবে।

```
┌────────────────────────────────────────────────────────────┐
│  Solution      কখন ব্যবহার করবে                          │
│  ──────────    ───────────────────────────────────────── │
│  setState      Simple local UI state (counter, toggle)    │
│  Provider      Simple dependency injection                │
│  Riverpod      Medium-large apps, testability দরকার      │
│  BLoC          Large apps, complex business logic         │
│  GetX          ছোট apps, দ্রুত prototype (production এ   │
│                বড় team এ avoid করো)                      │
│  MobX          Reactive programming পছন্দ করলে           │
└────────────────────────────────────────────────────────────┘
```

**Industry Standard বর্তমানে:**
- Large production apps: **BLoC** বা **Riverpod**
- Most teams: **Riverpod** (simpler API, better DX)
- Flutter community তে highly popular: **Riverpod** (Google/Flutter team কোনো নির্দিষ্ট third-party solution officially recommend করে না — সব community packages)

**BLoC Pattern — সঠিক implementation:**

```dart
// Event
abstract class ProductEvent {}
class LoadProducts extends ProductEvent {}
class SearchProducts extends ProductEvent {
  final String query;
  SearchProducts(this.query);
}

// State
abstract class ProductState {}
class ProductInitial extends ProductState {}
class ProductLoading extends ProductState {}
class ProductLoaded extends ProductState {
  final List<Product> products;
  ProductLoaded(this.products);
}
class ProductError extends ProductState {
  final String message;
  ProductError(this.message);
}

// BLoC
class ProductBloc extends Bloc<ProductEvent, ProductState> {
  final ProductRepository repository;

  ProductBloc({required this.repository}) : super(ProductInitial()) {
    on<LoadProducts>(_onLoadProducts);
    on<SearchProducts>(
      _onSearchProducts,
      // Debounce — user দ্রুত টাইপ করলে প্রতিটা keystroke এ API call না করে
      transformer: debounce(const Duration(milliseconds: 300)),
    );
  }

  Future<void> _onLoadProducts(
    LoadProducts event,
    Emitter<ProductState> emit,
  ) async {
    emit(ProductLoading());
    try {
      final products = await repository.getProducts();
      emit(ProductLoaded(products));
    } catch (e) {
      emit(ProductError(e.toString()));
    }
  }
}
```

#### ৪. Navigation — Advanced

```
✅ GoRouter — industry standard (Google recommended)
✅ Deep linking setup — Android এ Intent Filter, iOS এ URL Scheme
✅ Universal Links / App Links setup
✅ Navigation guards (authentication check)
✅ Nested navigation
✅ Tab navigation with state preservation
```

**GoRouter — Production Setup:**

```dart
final router = GoRouter(
  initialLocation: '/home',
  // Auth redirect — login না করলে login page এ যাবে
  redirect: (context, state) {
    final isLoggedIn = context.read<AuthBloc>().state is AuthAuthenticated;
    final isLoginRoute = state.matchedLocation == '/login';

    if (!isLoggedIn && !isLoginRoute) return '/login';
    if (isLoggedIn && isLoginRoute) return '/home';
    return null; // redirect নাই, এগিয়ে যাও
  },
  routes: [
    GoRoute(path: '/login', builder: (_, __) => const LoginScreen()),
    ShellRoute(
      builder: (context, state, child) => MainScaffold(child: child),
      routes: [
        GoRoute(path: '/home', builder: (_, __) => const HomeScreen()),
        GoRoute(
          path: '/product/:id',
          builder: (context, state) => ProductScreen(
            id: state.pathParameters['id']!,
          ),
        ),
      ],
    ),
  ],
);
```

#### ৫. Networking — Production Grade

```dart
// Dio setup — interceptors সহ
class ApiClient {
  late final Dio _dio;

  ApiClient({required String baseUrl, required TokenStorage tokenStorage}) {
    _dio = Dio(BaseOptions(
      baseUrl: baseUrl,
      connectTimeout: const Duration(seconds: 30),
      receiveTimeout: const Duration(seconds: 30),
    ));

    // Request interceptor — প্রতিটা request এ token যোগ করো
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await tokenStorage.getAccessToken();
          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          handler.next(options);
        },
        onError: (error, handler) async {
          // 401 হলে token refresh করো
          if (error.response?.statusCode == 401) {
            final refreshed = await _refreshToken(tokenStorage);
            if (refreshed) {
              // Original request আবার করো
              return handler.resolve(await _retry(error.requestOptions));
            }
          }
          handler.next(error);
        },
      ),
    );

    // Logging — শুধু debug mode এ
    if (kDebugMode) {
      _dio.interceptors.add(LogInterceptor(responseBody: true));
    }
  }
}
```

#### ৬. Local Storage — সঠিক Tool বেছে নেওয়া

```
┌────────────────────────────────────────────────────────────┐
│  Data Type              Best Tool                          │
│  ─────────────────      ──────────────────────────────── │
│  Simple key-value       SharedPreferences / flutter_secure_storage │
│  Sensitive data         flutter_secure_storage (encrypted) │
│  Structured data        Isar / Drift (SQLite wrapper)     │
│  Complex queries        Drift (type-safe SQL)             │
│  Real-time reactive     Isar (built-in streams)           │
│  Large files            path_provider + dart:io           │
└────────────────────────────────────────────────────────────┘
```

> **Industry Standard 2024-2025:** Isar (fast) বা Drift (SQL পছন্দ হলে)। Hive এর পরিবর্তে Isar ব্যবহার করো — same creator, better performance।

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="architecture"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 5 — Architecture — Mobile App এর জন্য
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### কেন Architecture গুরুত্বপূর্ণ

Architecture ছাড়া project শুরুতে দ্রুত চলে, কিন্তু ৬ মাস পরে:
- নতুন feature যোগ করা কঠিন হয়ে যায়
- Bug fix করতে গেলে নতুন bug আসে
- নতুন developer আসলে বুঝতে পারে না
- Testing করা প্রায় অসম্ভব হয়ে যায়

### Clean Architecture — Industry Standard

Clean Architecture সবচেয়ে বেশি ব্যবহৃত pattern Flutter এ। এটা Robert C. Martin (Uncle Bob) এর concept।

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│    ┌─────────────────────────────────────────────┐      │
│    │          Presentation Layer                 │      │
│    │    (Screens, Widgets, BLoC/Riverpod)        │      │
│    └─────────────────────────────────────────────┘      │
│                         ↕                               │
│    ┌─────────────────────────────────────────────┐      │
│    │            Domain Layer                     │      │
│    │    (Entities, Use Cases, Repository         │      │
│    │     Interfaces)                             │      │
│    └─────────────────────────────────────────────┘      │
│                         ↕                               │
│    ┌─────────────────────────────────────────────┐      │
│    │             Data Layer                      │      │
│    │    (Repository Implementations,             │      │
│    │     Remote DataSource, Local DataSource)    │      │
│    └─────────────────────────────────────────────┘      │
│                                                          │
└──────────────────────────────────────────────────────────┘

Rule: Inner layers বাইরের layer সম্পর্কে জানে না।
      Domain layer কখনো Flutter কে import করে না।
```

### Folder Structure — Feature-First (Industry Best Practice)

```
lib/
├── core/                          # সব feature এ shared
│   ├── constants/
│   │   ├── app_colors.dart
│   │   ├── app_strings.dart
│   │   └── app_dimensions.dart
│   ├── errors/
│   │   ├── exceptions.dart
│   │   └── failures.dart
│   ├── network/
│   │   ├── api_client.dart
│   │   └── network_info.dart
│   ├── utils/
│   │   ├── date_utils.dart
│   │   └── validators.dart
│   └── widgets/                   # Shared widgets
│       ├── app_button.dart
│       ├── app_text_field.dart
│       └── loading_indicator.dart
│
├── features/                      # প্রতিটা feature আলাদা
│   ├── auth/
│   │   ├── data/
│   │   │   ├── datasources/
│   │   │   │   ├── auth_remote_datasource.dart
│   │   │   │   └── auth_local_datasource.dart
│   │   │   ├── models/
│   │   │   │   └── user_model.dart
│   │   │   └── repositories/
│   │   │       └── auth_repository_impl.dart
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   │   └── user.dart
│   │   │   ├── repositories/
│   │   │   │   └── auth_repository.dart   # Abstract
│   │   │   └── usecases/
│   │   │       ├── login_usecase.dart
│   │   │       └── logout_usecase.dart
│   │   └── presentation/
│   │       ├── bloc/
│   │       │   ├── auth_bloc.dart
│   │       │   ├── auth_event.dart
│   │       │   └── auth_state.dart
│   │       ├── pages/
│   │       │   ├── login_page.dart
│   │       │   └── register_page.dart
│   │       └── widgets/
│   │           └── login_form.dart
│   │
│   └── products/
│       ├── data/
│       ├── domain/
│       └── presentation/
│
├── injection_container.dart       # Dependency Injection setup
└── main.dart
```

### Dependency Injection — get_it + injectable

```dart
// injection_container.dart

import 'package:get_it/get_it.dart';
import 'package:injectable/injectable.dart';
import 'injection_container.config.dart'; // auto-generated

final getIt = GetIt.instance;

@InjectableInit()
Future<void> configureDependencies() async => getIt.init();

// Feature: Auth
@injectable
class LoginUseCase {
  final AuthRepository repository; // interface inject হচ্ছে
  LoginUseCase(this.repository);

  Future<Either<Failure, User>> call(LoginParams params) {
    return repository.login(params.email, params.password);
  }
}

@LazySingleton(as: AuthRepository) // interface এর implementation
class AuthRepositoryImpl implements AuthRepository {
  final AuthRemoteDataSource remoteDataSource;
  final AuthLocalDataSource localDataSource;

  AuthRepositoryImpl({
    required this.remoteDataSource,
    required this.localDataSource,
  });
  // ...
}
```

### Repository Pattern — Data Layer

```dart
// domain/repositories/auth_repository.dart (Abstract — interface)
abstract class AuthRepository {
  Future<Either<Failure, User>> login(String email, String password);
  Future<Either<Failure, void>> logout();
  Future<Either<Failure, User>> getCurrentUser();
}

// data/repositories/auth_repository_impl.dart (Concrete implementation)
class AuthRepositoryImpl implements AuthRepository {
  final AuthRemoteDataSource remoteDataSource;
  final AuthLocalDataSource localDataSource;
  final NetworkInfo networkInfo;

  @override
  Future<Either<Failure, User>> login(String email, String password) async {
    // Internet আছে কিনা check করো
    if (await networkInfo.isConnected) {
      try {
        final userModel = await remoteDataSource.login(email, password);
        // Local এ cache করো
        await localDataSource.cacheUser(userModel);
        return Right(userModel.toEntity()); // Success
      } on ServerException catch (e) {
        return Left(ServerFailure(e.message)); // Error
      }
    } else {
      // Offline — local cache থেকে দাও
      try {
        final cachedUser = await localDataSource.getCachedUser();
        return Right(cachedUser.toEntity());
      } on CacheException {
        return Left(const CacheFailure('No cached data available'));
      }
    }
  }
}
```

### Either — Functional Error Handling

```dart
// dartz package ব্যবহার করো
// Either<Failure, Success>
// Left = Error, Right = Success

// BLoC এ handle করা
Future<void> _onLogin(LoginEvent event, Emitter<AuthState> emit) async {
  emit(AuthLoading());

  final result = await loginUseCase(
    LoginParams(email: event.email, password: event.password),
  );

  // fold দিয়ে দুটো case handle করো
  result.fold(
    (failure) => emit(AuthError(failure.message)),    // Left (error)
    (user)    => emit(AuthAuthenticated(user)),        // Right (success)
  );
}
```

### Offline-First Architecture

Production grade app এ offline support থাকা উচিত।

```
Offline-First Flow:

User request
     ↓
Local DB তে data আছে?
     ├── আছে → সাথে সাথে দেখাও (cached data)
     │          Background এ API call করো
     │          নতুন data এলে update করো
     └── নেই → API call করো
               Data এলে Local DB তে save করো
               UI তে দেখাও
```

```dart
// Offline-first Repository implementation
@override
Stream<Either<Failure, List<Product>>> watchProducts() async* {
  // প্রথমে local data দেখাও
  final localProducts = await localDataSource.getProducts();
  if (localProducts.isNotEmpty) {
    yield Right(localProducts.map((m) => m.toEntity()).toList());
  }

  // Background এ fresh data আনো
  if (await networkInfo.isConnected) {
    try {
      final remoteProducts = await remoteDataSource.getProducts();
      await localDataSource.cacheProducts(remoteProducts);
      yield Right(remoteProducts.map((m) => m.toEntity()).toList());
    } on ServerException catch (e) {
      yield Left(ServerFailure(e.message));
    }
  }
}
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="code-quality"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 6 — Code Quality ও Code Review
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Code Quality — Tech Lead এর Ownership

Code quality কোনো একজনের দায়িত্ব না — এটা পুরো team এর। কিন্তু **standard set করা এবং enforce করা** Tech Lead এর কাজ।

### Linting — analysis_options.yaml

```yaml
# analysis_options.yaml — project root এ রাখো
include: package:flutter_lints/flutter.yaml

analyzer:
  errors:
    # এগুলো error হিসেবে treat করো (warning না)
    missing_required_param: error
    missing_return: error
    dead_code: error
    unused_import: warning
    unused_local_variable: warning
  exclude:
    - "**/*.g.dart"        # generated files ignore করো
    - "**/*.freezed.dart"

linter:
  rules:
    # Code style
    prefer_const_constructors: true
    prefer_const_literals_to_create_immutables: true
    prefer_final_locals: true
    avoid_unnecessary_containers: true

    # Error prevention
    avoid_print: true                    # print() এর বদলে logger ব্যবহার করো
    avoid_empty_catch: true
    cancel_subscriptions: true           # Stream subscription cancel করতে হবে
    close_sinks: true                    # Sink close করতে হবে
    unawaited_futures: true              # await করা ভুলে গেলে warn করবে

    # Performance
    avoid_slow_async_io: true

    # Naming
    non_constant_identifier_names: true
    constant_identifier_names: true
```

### Code Review — সঠিক Process

#### PR (Pull Request) Template

```markdown
<!-- .github/PULL_REQUEST_TEMPLATE.md -->

## 📝 কী পরিবর্তন করা হয়েছে?
<!-- সংক্ষেপে বলো কী করা হয়েছে -->

## 🎯 কেন এই পরিবর্তন?
<!-- Business reason বা technical reason বলো -->

## 🧪 কীভাবে test করা হয়েছে?
- [ ] Unit tests লেখা হয়েছে
- [ ] Widget tests লেখা হয়েছে
- [ ] Manual testing করা হয়েছে (Android)
- [ ] Manual testing করা হয়েছে (iOS)

## 📸 Screenshots (UI change হলে)
<!-- Before / After screenshot দাও -->

## ⚠️ কোনো breaking change আছে?
<!-- হ্যাঁ বা না। থাকলে কী কী -->

## 📋 Checklist
- [ ] Code analysis pass করেছে (flutter analyze)
- [ ] সব tests pass করেছে
- [ ] Self-review করা হয়েছে
- [ ] Documentation update করা হয়েছে (যদি দরকার)
```

#### Code Review করার সময় কী দেখবে

**১. Correctness — Logic ঠিক আছে?**
```dart
// ❌ Bug: null check নেই
String getInitials(String name) {
  return name.split(' ').map((n) => n[0]).join();
  // name = "" হলে crash করবে
}

// ✅ সঠিক
String getInitials(String? name) {
  if (name == null || name.trim().isEmpty) return '';
  return name.trim()
    .split(' ')
    .where((n) => n.isNotEmpty)
    .map((n) => n[0].toUpperCase())
    .take(2) // সর্বোচ্চ ২ letter initials
    .join();
}
```

**২. Performance — Slow code আছে?**
```dart
// ❌ Performance issue: build() এ object creation
class ProductCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // প্রতিটা rebuild এ নতুন TextStyle object তৈরি হচ্ছে
    final titleStyle = TextStyle(fontSize: 16, fontWeight: FontWeight.bold);
    return Text('Product', style: titleStyle);
  }
}

// ✅ const দিয়ে একবারই তৈরি হবে
class ProductCard extends StatelessWidget {
  static const _titleStyle = TextStyle(fontSize: 16, fontWeight: FontWeight.bold);

  @override
  Widget build(BuildContext context) {
    return const Text('Product', style: _titleStyle);
  }
}
```

**৩. Security — Sensitive data expose হচ্ছে?**
```dart
// ❌ Security issue: API key hardcode
const apiKey = 'sk-live-1234567890abcdef'; // কখনো করবে না!

// ✅ Environment variable থেকে নাও
// --dart-define দিয়ে inject করো
const apiKey = String.fromEnvironment('API_KEY');
```

**৪. Readability — নতুন কেউ বুঝবে?**
```dart
// ❌ অস্পষ্ট
final x = d.p.u.n ?? 'U';

// ✅ স্পষ্ট
final displayName = currentUser.profile.username ?? 'Unknown';
```

**৫. Test Coverage — Test আছে?**

#### Code Review এর ভাষা — গুরুত্বপূর্ণ

```
❌ Toxic review:
"এই code horrible। কীভাবে এটা লিখলে?"
"এটা wrong। ঠিক করো।"

✅ Constructive review:
"এখানে একটা potential null pointer exception হতে পারে
 যদি list empty থাকে। line 42 এ isEmpty check
 যোগ করলে safe হবে।"

"এই approach কাজ করবে, কিন্তু আমরা যদি
 Repository Pattern ব্যবহার করি তাহলে testing
 অনেক সহজ হবে। একটু কথা বলি?"

"Nit: এই variable নামটা আরো descriptive হলে
 ভালো হতো। কিন্তু এটা blocker না।"
```

**Comment Prefix Convention:**
```
Blocking:   এটা fix না করলে merge হবে না
Suggestion: তোমার বিবেচনা করো, আমার recommendation
Nit:        খুব ছোট, optional improvement
Question:   আমি বুঝতে পারিনি, explain করো
Praise:     ভালো কাজ! 👍
```

### Code Standards Document

Tech Lead হিসেবে এই document টা তোমাকে তৈরি করতে হবে।

```markdown
# Mobile Team Coding Standards

## Naming Conventions
- Classes: PascalCase (ProductRepository)
- Variables/methods: camelCase (getUserById)
- Constants: lowerCamelCase (maxRetryCount) বা SCREAMING_SNAKE (API_BASE_URL)
- Files: snake_case (product_repository.dart)
- Private members: underscore prefix (_controller)

## Widget Guidelines
- প্রতিটা Widget যতটা সম্ভব const করো
- 100 লাইনের বেশি হলে Widget ভাগ করো
- build() method এ business logic রাখবে না
- Magic numbers avoid করো — named constant ব্যবহার করো

## Error Handling
- সব async method এ try-catch থাকবে
- User-facing error message meaningful হবে
- Error logger তে log করতে হবে

## Comments
- কী করছো সেটা comment করবে না — code পড়লেই বোঝা যায়
- কেন করছো সেটা comment করো — সেটাই valuable
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="team-leadership"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 7 — Team Leadership ও Mentoring
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Mentoring — সবচেয়ে impactful কাজ

Tech Lead হিসেবে তোমার সবচেয়ে বড় leverage হলো — তুমি একা ১x কাজ করতে পারো, কিন্তু ৫ জনকে ভালো করলে ৫x output পাও।

### Mentoring Framework

**১-on-1 Meeting — সপ্তাহে একবার (৩০ মিনিট)**

```
1-on-1 এর structure:

প্রথম ১০ মিনিট: তাদের কথা শোনো
  - "এই সপ্তাহে কী ভালো গেছে?"
  - "কোথায় আটকে আছো?"
  - "কী নিয়ে frustrated?"

পরের ১০ মিনিট: Technical growth
  - "এই sprint এ কী শিখলে?"
  - "কোন topic এ আরো deep dive করতে চাও?"

শেষ ১০ মিনিট: Actionable items
  - "পরের সপ্তাহে তুমি কী করবে?"
  - "আমি কীভাবে help করতে পারি?"
```

**সঠিক Mentoring Style:**

```
Situation: Junior developer একটা problem এ আটকে আছে

❌ Wrong approach (সব করে দেওয়া):
"দেখো এভাবে করো" → তুমি করে দিলে

❌ Wrong approach (ignore করা):
"তুমি বড় developer, নিজে বের করো"

✅ Right approach (Socratic method):
তুমি: "কী সমস্যা হচ্ছে?"
Dev:  "এই widget rebuild হচ্ছে না"
তুমি: "তুমি কী কী try করেছো?"
Dev:  "setState call করেছি"
তুমি: "setState কোথায় call করছো? সেই method টা কি
       সেই widget এর state এ আছে?"
Dev:  "ওহ... StatelessWidget এ setState নেই!"
তুমি: "Exactly! এখন তুমি কী করবে?"
Dev:  "StatefulWidget এ convert করবো"
→ নিজে বের করলো, শিখলো, মনে থাকবে ✅
```

### Knowledge Sharing Culture তৈরি করা

**Tech Talk — প্রতি ২ সপ্তাহে একবার**
```
Format: ৩০ মিনিট
কে করবে: Rotation — সবাই পালাক্রমে
Topic: যেকোনো technical topic যা team এর কাজে লাগবে

উদাহরণ topics:
- "আমি এই bug টা কীভাবে fix করলাম"
- "GoRouter এর নতুন features"
- "Dart 3 এর নতুন features — আমরা কীভাবে use করতে পারি"
- "আমি এই open source library টা explore করলাম"
```

**Pair Programming**
```
কখন করবে:
- Complex feature develop করার সময়
- Junior কাউকে কিছু শেখাতে
- Tricky bug solve করার সময়
- Code review এর alternative হিসেবে

Format:
- Driver: যে code লেখে
- Navigator: যে think করে, suggest করে
- ৩০ মিনিট পর পর role switch করো
```

### Psychological Safety — সবচেয়ে গুরুত্বপূর্ণ Culture

Google এর Project Aristotle research দেখিয়েছে — **Psychological Safety** হলো high-performing team এর সবচেয়ে বড় factor।

**Psychological Safety মানে:**
- কেউ ভুল করলে blame করা হবে না — solution খোঁজা হবে
- কোনো idea নিয়ে হাসাহাসি করা হবে না
- "বোকার মতো" প্রশ্ন করা যাবে
- Disagreement openly বলা যাবে

**কীভাবে তৈরি করবে:**

```
১. নিজের ভুল স্বীকার করো publicly:
   "আমি এখানে ভুল decision নিয়েছিলাম।
    পরের বার এভাবে approach করবো।"

২. "বোকা" প্রশ্নের প্রশংসা করো:
   "ভালো প্রশ্ন — আমিও এটা clearly জানতাম না।
    চলো একসাথে দেখি।"

৩. Junior এর idea কে seriously নাও:
   "তুমি এটা suggest করছো — চলো এটার
    trade-offs দেখি।"

৪. Blame করার বদলে system দেখো:
   ❌ "তুমি কেন এই bug করলে?"
   ✅ "এই bug টা catch করার জন্য আমাদের
      process এ কী missing ছিল?"
```

### Conflict Resolution

Team এ disagreement থাকবেই — এটা স্বাভাবিক এবং healthy। কিন্তু conflict manage করা Tech Lead এর কাজ।

```
Technical disagreement resolution:

Step 1: দুটো option এর pros/cons document করো
Step 2: Objective criteria দিয়ে evaluate করো
        (performance, maintainability, team skill)
Step 3: Data দিয়ে decide করো — opinion দিয়ে না
Step 4: একটা decision নাও এবং document করো
Step 5: সবাই agree না করলেও — "disagree and commit"
```

**Disagree and Commit:**
> Amazon এর culture থেকে — তুমি হয়তো একটা decision এর সাথে ১০০% agree না, কিন্তু একবার team decision নিলে সবাই সেই দিকে কাজ করে। Passive resistance বা "আমি বলেছিলাম" culture toxic।

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="project-planning"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 8 — Project Planning ও Task Management
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Feature Breakdown — Tech Lead এর কাজ

Product Manager একটা feature দেয়: *"User যেন product share করতে পারে"*

Tech Lead এর কাজ এটাকে actionable tasks এ ভাগ করা:

```
Feature: Product Share

Tasks:
  ┌─ Technical Research (0.5 day)
  │    - share_plus package evaluate করো
  │    - Deep link setup দরকার কিনা দেখো
  │
  ├─ Backend API (if needed) (1 day - Backend team)
  │    - Share link generate করার endpoint
  │
  ├─ UI Implementation (1.5 days)
  │    - Share button widget
  │    - Share bottom sheet
  │    - Platform-specific share sheet trigger
  │
  ├─ Deep Link Handling (1 day)
  │    - Shared link থেকে app open হলে product page এ navigate
  │    - App না থাকলে App Store/Play Store এ নিয়ে যাওয়া
  │
  ├─ Testing (1 day)
  │    - Unit test
  │    - Integration test
  │    - Manual test on Android + iOS
  │
  └─ Total: ~5 days (buffer সহ 7 days দাও)
```

### Estimation — সঠিকভাবে

Estimation সব সময় কঠিন। কিন্তু কিছু technique আছে।

**Planning Poker:**
```
Team সবাই মিলে estimate করে — independently।
Fibonacci: 1, 2, 3, 5, 8, 13, 21

সবাই একসাথে card দেখায়।
বড় difference থাকলে কারণ discuss করো।
Agreement না হওয়া পর্যন্ত repeat করো।

কেন ভালো: একজনের estimate অন্যকে influence করে না।
```

**T-shirt sizing (simpler):**
```
XS = অর্ধেক দিনের কম
S  = ১ দিন
M  = ২-৩ দিন
L  = ৪-৫ দিন
XL = ১ সপ্তাহের বেশি → ভাঙো

XL কোনো task যদি থাকে — সেটা অবশ্যই ছোট করো।
Too big মানে unclear requirement।
```

**Buffer যোগ করার নিয়ম:**
```
Team এর experience level:
- Mostly Junior team: estimate × 2.5
- Mixed team: estimate × 2.0
- Senior team: estimate × 1.5

কারণ: Meeting, code review, unexpected bugs,
      sick days, unclear requirements — সব
      estimate এর বাইরে।
```

### Sprint Planning — সপ্তাহে বা দুই সপ্তাহে

```
Sprint Planning Meeting Structure:

1. Previous sprint review (15 min)
   - কী শেষ হয়েছে, কী হয়নি, কেন

2. Upcoming sprint backlog review (15 min)
   - Product Manager priority দেবে
   - Tech Lead technical feasibility বলবে

3. Task breakdown (30 min)
   - বড় tasks ভাঙো
   - Dependencies চিহ্নিত করো

4. Assignment (15 min)
   - কে কী করবে
   - Skill matching করো (junior কে শেখার সুযোগ দাও)

5. Commitment (5 min)
   - Team collectively commit করে
   - Tech Lead last say রাখে — capacity অনুযায়ী
```

### Technical Debt Management

Technical debt হলো — দ্রুত করার জন্য "wrong" approach নেওয়া যেটা future এ কষ্ট দেবে।

```
Technical Debt কীভাবে manage করবে:

১. Document করো — কোথায় debt আছে
   // TODO(tech-debt): This is a workaround.
   //                  Proper fix: JIRA-1234

২. Visible করো — backlog এ রাখো
   Product Manager কে explain করো impact

৩. Budget করো — প্রতি sprint এ ২০% time
   debt reduction এর জন্য রাখো

৪. "Boy Scout Rule" follow করো:
   "যে code ছুঁলে, সেটা একটু ভালো করে যাও"
   Complete refactor না করলেও চলবে
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="communication"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 9 — Communication Skills
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### কেন Communication সবচেয়ে Underrated Skill

অনেক brilliant developer Tech Lead এ fail করে শুধু communication এর জন্য। তারা technically perfect কিন্তু:
- Management কে বোঝাতে পারে না কেন technical debt fix জরুরি
- Team কে inspire করতে পারে না
- Conflict resolve করতে পারে না
- Deadline নিয়ে realistic conversation করতে পারে না

### Upward Communication — Management এর সাথে

**Technical বিষয় Non-Technical ভাষায় বলা:**

```
❌ Technical language:
"আমাদের dependency injection পুরোপুরি ঠিক করতে হবে,
 নাহলে unit testing করা যাবে না এবং future refactoring
 এ memory leak হওয়ার risk আছে।"

✅ Business language:
"আমাদের codebase এ একটা structural problem আছে।
 এটা fix না করলে:
 - নতুন developer join করলে onboard হতে ২ সপ্তাহ বেশি লাগবে
 - প্রতিটা নতুন feature এ ২০% বেশি time লাগবে
 - Production bug এর risk ৩০% বেড়ে যাবে

 Fix করতে লাগবে ১ sprint (২ সপ্তাহ)।
 Investment vs Return: এখন ২ সপ্তাহ দিলে
 পরের ৬ মাসে প্রতি মাসে ১ সপ্তাহ save হবে।"
```

**Status Update — সংক্ষেপে এবং সত্য:**

```
Daily Standup format (max 2 minutes per person):
- কাল কী করেছি
- আজ কী করবো
- কোনো blocker আছে কিনা

Weekly Status Report format:
✅ Done: [এই সপ্তাহে কী শেষ হয়েছে]
🔄 In Progress: [চলছে কী]
⚠️ Blockers: [কী আটকে আছে, কেন]
📅 Next Week: [কী করবো]
🚨 Risks: [কোনো risk দেখছি কিনা]
```

**Bad news দেওয়ার সঠিক পদ্ধতি:**
```
সত্যি বলো — দেরি করা না:
"এই feature ৩ দিন পিছিয়ে যাচ্ছে কারণ
 আমরা একটা unexpected iOS compatibility issue
 পেয়েছি। আমরা এটা fix করছি। নতুন date: Friday।
 পরের বার এই risk আগে থেকে catch করার জন্য
 আমরা earlier device testing করবো।"
```

### Downward Communication — Team এর সাথে

**Feedback দেওয়া — SBI Model:**
```
S = Situation (কখন, কোথায়)
B = Behavior (কী করেছে — fact, opinion না)
I = Impact (এর ফলাফল কী হয়েছে)

উদাহরণ:
"গতকালের sprint review তে (S)
 তুমি client এর সামনে বললে এই feature টা
 আগামী সপ্তাহে ready হবে (B) — কিন্তু আমরা
 team এ সেটা decide করিনি। এতে client এর
 unrealistic expectation তৈরি হয়েছে (I)।

 পরের বার এরকম commitment দেওয়ার আগে
 team কে জিজ্ঞেস করবে।"
```

**Recognition দেওয়া — publicly:**
```
"আমি শেয়ার করতে চাই — [Name] এই সপ্তাহে
 একটা tricky performance issue find করেছে
 যেটা production এ বড় problem হতে পারতো।
 এটা great proactive thinking।"

Public recognition:
- Team meeting এ বলো
- Slack এ share করো
- Manager কে inform করো

Private criticism:
- সবসময় private এ — কখনো public এ না
```

### Lateral Communication — Cross-team

Mobile Tech Lead কে Backend, Design, QA team এর সাথে কথা বলতে হয়।

**API Contract Discussion — Backend team এর সাথে:**
```
Mobile developer হিসেবে তোমার voice:
- "এই response এ nested object টা
   mobile এ parse করা complex হবে।
   Flat structure হলে ভালো হতো।"
- "Pagination এ cursor-based ভালো হবে
   infinite scroll এর জন্য।"
- "Error codes গুলো consistent হওয়া দরকার —
   মোবাইলে user-facing message দেখাতে হবে।"
```

**Design handoff — Design team এর সাথে:**
```
Figma থেকে Flutter implementation এ যা দরকার:
- Component library consistent থাকা
- Responsive breakpoints define করা
- Animation duration/easing specify করা
- Dark mode variants থাকা
- Edge cases design করা (empty state, error state, loading)
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="performance"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 10 — Performance ও Optimization
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Mobile Performance — কী measure করবে

```
┌────────────────────────────────────────────────────────┐
│  Metric              Target        Tool                │
│  ──────────────────  ──────────    ─────────────────  │
│  App startup time    < 2 seconds   Flutter DevTools    │
│  Frame rate          60fps / 120fps DevTools Timeline  │
│  Memory usage        < 200MB avg   DevTools Memory     │
│  App size (release)  < 20MB ideal  flutter build       │
│  Scroll performance  No jank       DevTools            │
│  Network requests    < 3s per call Charles/Proxyman    │
└────────────────────────────────────────────────────────┘
```

### Common Performance Issues ও Solutions

**১. Jank (Frame drop) — সবচেয়ে common:**

```dart
// ❌ Problem: build() এ heavy computation
class ProductListScreen extends StatelessWidget {
  final List<Product> products;

  @override
  Widget build(BuildContext context) {
    // প্রতি rebuild এ sort হচ্ছে! O(n log n) প্রতিবার
    final sorted = products.sortedBy((p) => p.price);
    return ListView.builder(/*...*/);
  }
}

// ✅ Solution: memoize করো
class ProductListScreen extends StatefulWidget {
  final List<Product> products;
  // ...
}

class _ProductListScreenState extends State<ProductListScreen> {
  late List<Product> _sortedProducts;

  @override
  void initState() {
    super.initState();
    _sortedProducts = widget.products.sortedBy((p) => p.price);
  }

  @override
  void didUpdateWidget(ProductListScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.products != widget.products) {
      _sortedProducts = widget.products.sortedBy((p) => p.price);
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(/*_sortedProducts ব্যবহার করো*/);
  }
}
```

**২. Unnecessary Rebuilds:**

```dart
// ❌ Problem: পুরো page rebuild হচ্ছে একটা ছোট state change এ
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // Cart count change হলে পুরো HomePage rebuild হবে
    final cartCount = context.watch<CartBloc>().state.count;
    return Scaffold(
      appBar: AppBar(
        actions: [Badge(count: cartCount)], // শুধু এটা change হয়
      ),
      body: ExpensiveProductList(), // এটাও rebuild হচ্ছে! ❌
    );
  }
}

// ✅ Solution: শুধু যা change হয় সেটাকে rebuild করো
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        actions: [
          // শুধু এই widget rebuild হবে
          BlocBuilder<CartBloc, CartState>(
            buildWhen: (prev, curr) => prev.count != curr.count,
            builder: (context, state) => Badge(count: state.count),
          ),
        ],
      ),
      body: const ExpensiveProductList(), // const — rebuild হবে না
    );
  }
}
```

**৩. Image Performance:**

```dart
// ✅ Image optimization best practices
CachedNetworkImage(
  imageUrl: product.imageUrl,
  // Thumbnail দেখাও আগে, তারপর full image
  placeholder: (context, url) => const ShimmerPlaceholder(),
  errorWidget: (context, url, error) => const ErrorImageWidget(),
  // Memory cache size limit
  memCacheWidth: 300,  // pixel এ, device pixel ratio অনুযায়ী
  memCacheHeight: 300,
  fadeInDuration: const Duration(milliseconds: 300),
)

// Large image list এ — এটা critical:
ListView.builder(
  itemBuilder: (context, index) => CachedNetworkImage(
    imageUrl: images[index],
    // ছোট thumbnail URL ব্যবহার করো full URL এর বদলে
    imageUrl: getThumbnailUrl(images[index]),
  ),
)
```

**৪. App Size Optimization:**

```bash
# Release build analyze করো
flutter build apk --analyze-size
flutter build ipa --analyze-size

# সাধারণ size reduction techniques:
# 1. --split-per-abi: প্রতিটা architecture এর জন্য আলাদা APK
flutter build apk --split-per-abi

# 2. ProGuard/R8: unused code remove করে
# android/app/build.gradle এ:
# buildTypes {
#   release {
#     minifyEnabled true
#     shrinkResources true
#   }
# }

# 3. Image compression: WebP format ব্যবহার করো PNG/JPEG এর বদলে
# 4. Unused assets remove করো
# 5. --obfuscate: code obfuscation (security + size)
flutter build apk --obfuscate --split-debug-info=./debug-info
```

### Flutter DevTools — Master করো

```
Tech Lead হিসেবে DevTools এর এই sections জানতে হবে:

Performance Tab:
  - Frame chart দেখো — red frame মানে jank
  - UI thread vs Raster thread আলাদা করো
  - Timeline events বুঝতে পারো

Memory Tab:
  - Heap snapshot নাও
  - Memory leak detect করো
  - Object allocation track করো

Widget Inspector:
  - Widget tree visualize করো
  - Rebuild count দেখো
  - Performance overlay enable করো:
    showPerformanceOverlay: true (MaterialApp এ)
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="testing"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 11 — Testing Strategy
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Testing Pyramid — Mobile Version

```
                    ┌───┐
                   /  E2E \
                  / Tests  \
                 /  (少 few) \
                /─────────────\
               /  Widget Tests  \
              /   (moderate)     \
             /─────────────────────\
            /    Unit Tests          \
           /    (many, fast, cheap)   \
          /─────────────────────────────\
```

**কোন test কতটুকু লিখবে:**
```
Unit Tests:    ৭০% — Business logic, Use cases, Repositories, BLoC
Widget Tests:  ২০% — Individual widgets, screens
E2E Tests:     ১০% — Critical user journeys (login, purchase flow)
```

### Unit Testing — BLoC

```dart
// test/features/auth/presentation/bloc/auth_bloc_test.dart

void main() {
  late AuthBloc authBloc;
  late MockLoginUseCase mockLoginUseCase;

  setUp(() {
    mockLoginUseCase = MockLoginUseCase();
    authBloc = AuthBloc(loginUseCase: mockLoginUseCase);
  });

  tearDown(() {
    authBloc.close();
  });

  group('LoginEvent', () {
    final testUser = User(id: '1', email: 'test@test.com', name: 'Test');
    const testEmail = 'test@test.com';
    const testPassword = 'password123';

    blocTest<AuthBloc, AuthState>(
      'successful login emits [AuthLoading, AuthAuthenticated]',
      build: () {
        // Mock setup: login call করলে success return করবে
        when(
          () => mockLoginUseCase(
            LoginParams(email: testEmail, password: testPassword),
          ),
        ).thenAnswer((_) async => Right(testUser));
        return authBloc;
      },
      act: (bloc) => bloc.add(
        LoginEvent(email: testEmail, password: testPassword),
      ),
      expect: () => [
        AuthLoading(),
        AuthAuthenticated(testUser),
      ],
    );

    blocTest<AuthBloc, AuthState>(
      'failed login emits [AuthLoading, AuthError]',
      build: () {
        when(
          () => mockLoginUseCase(any()),
        ).thenAnswer((_) async => Left(ServerFailure('Invalid credentials')));
        return authBloc;
      },
      act: (bloc) => bloc.add(
        LoginEvent(email: testEmail, password: 'wrong'),
      ),
      expect: () => [
        AuthLoading(),
        AuthError('Invalid credentials'),
      ],
    );
  });
}
```

### Widget Testing

```dart
// test/features/auth/presentation/pages/login_page_test.dart

void main() {
  group('LoginPage', () {
    late MockAuthBloc mockAuthBloc;

    setUp(() {
      mockAuthBloc = MockAuthBloc();
      when(() => mockAuthBloc.state).thenReturn(AuthInitial());
    });

    Widget buildLoginPage() {
      return MaterialApp(
        home: BlocProvider<AuthBloc>.value(
          value: mockAuthBloc,
          child: const LoginPage(),
        ),
      );
    }

    testWidgets('shows email and password fields', (tester) async {
      await tester.pumpWidget(buildLoginPage());

      expect(find.byKey(const Key('email_field')), findsOneWidget);
      expect(find.byKey(const Key('password_field')), findsOneWidget);
      expect(find.byKey(const Key('login_button')), findsOneWidget);
    });

    testWidgets('shows loading indicator when AuthLoading', (tester) async {
      when(() => mockAuthBloc.state).thenReturn(AuthLoading());
      await tester.pumpWidget(buildLoginPage());

      expect(find.byType(CircularProgressIndicator), findsOneWidget);
      expect(find.byKey(const Key('login_button')), findsNothing);
    });

    testWidgets('calls login event when form submitted', (tester) async {
      await tester.pumpWidget(buildLoginPage());

      await tester.enterText(
        find.byKey(const Key('email_field')), 'test@test.com',
      );
      await tester.enterText(
        find.byKey(const Key('password_field')), 'password123',
      );
      await tester.tap(find.byKey(const Key('login_button')));

      verify(
        () => mockAuthBloc.add(
          LoginEvent(email: 'test@test.com', password: 'password123'),
        ),
      ).called(1);
    });
  });
}
```

### Test Coverage Goal

```bash
# Coverage report generate করো
flutter test --coverage
genhtml coverage/lcov.info -o coverage/html

# coverage/html/index.html খোলো browser এ

# Target coverage:
# Business logic (Use cases, BLoC): 90%+
# Repository: 80%+
# Widgets: 70%+
# Overall: 75%+
```

### Golden Tests — UI Regression

```dart
// UI কে pixel-perfect রাখার জন্য
testWidgets('ProductCard golden test', (tester) async {
  await tester.pumpWidget(
    MaterialApp(
      home: ProductCard(
        product: Product(
          id: '1',
          name: 'iPhone 15',
          price: 120000,
          imageUrl: 'test_image.jpg',
        ),
      ),
    ),
  );

  await expectLater(
    find.byType(ProductCard),
    matchesGoldenFile('goldens/product_card.png'),
  );
});

// প্রথমবার run করলে golden file তৈরি হবে
// পরের বার run করলে compare করবে
// UI change হলে test fail করবে — intentional change হলে update করো:
// flutter test --update-goldens
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="cicd"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 12 — CI/CD ও DevOps — Mobile এর জন্য
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Mobile CI/CD Pipeline

```
Code Push
    ↓
┌─────────────────────────────────────────────┐
│  CI Pipeline (GitHub Actions / Bitrise)     │
│                                             │
│  1. flutter pub get                         │
│  2. flutter analyze (lint check)            │
│  3. flutter test (unit + widget tests)      │
│  4. flutter build (release build)           │
│  5. Code signing                            │
└────────────────────┬────────────────────────┘
                     ↓
┌─────────────────────────────────────────────┐
│  CD Pipeline                                │
│                                             │
│  Dev branch    → Internal Testing (Firebase │
│                  App Distribution)          │
│  Main branch   → Beta (TestFlight /         │
│                  Internal Test Track)       │
│  Release tag   → Production (App Store /    │
│                  Play Store)                │
└─────────────────────────────────────────────┘
```

### GitHub Actions — Flutter CI

```yaml
# .github/workflows/flutter_ci.yml
name: Flutter CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Flutter
        uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.41.9'  # specific version pin করো
          channel: 'stable'
          cache: true  # Flutter SDK cache করো — faster

      - name: Install dependencies
        run: flutter pub get

      - name: Check formatting
        run: dart format --set-exit-if-changed .

      - name: Run analyzer
        run: flutter analyze --fatal-infos

      - name: Run tests with coverage
        run: flutter test --coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: coverage/lcov.info

  build-android:
    runs-on: ubuntu-latest
    needs: test  # test pass হলেই build হবে

    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.41.9'
          cache: true

      - name: Build APK
        run: |
          flutter build apk --release \
            --dart-define=API_URL=${{ secrets.API_URL }} \
            --dart-define=API_KEY=${{ secrets.API_KEY }}

      - name: Upload APK artifact
        uses: actions/upload-artifact@v3
        with:
          name: release-apk
          path: build/app/outputs/flutter-apk/app-release.apk
```

### Fastlane — App Store / Play Store Automation

```ruby
# fastlane/Fastfile

default_platform(:android)

platform :android do
  desc "Deploy to Play Store Internal Track"
  lane :deploy_internal do
    gradle(
      task: "bundle",
      build_type: "Release",
      properties: {
        "android.injected.signing.store.file" => ENV["KEYSTORE_PATH"],
        "android.injected.signing.store.password" => ENV["KEYSTORE_PASSWORD"],
        "android.injected.signing.key.alias" => ENV["KEY_ALIAS"],
        "android.injected.signing.key.password" => ENV["KEY_PASSWORD"],
      }
    )
    upload_to_play_store(
      track: 'internal',
      aab: 'app/build/outputs/bundle/release/app-release.aab'
    )
    slack(
      message: "✅ Android app deployed to Internal Track!",
      webhook_url: ENV["SLACK_WEBHOOK"]
    )
  end
end

platform :ios do
  desc "Deploy to TestFlight"
  lane :deploy_testflight do
    match(type: "appstore")  # Certificate ও provisioning profile
    build_ios_app(
      scheme: "Runner",
      export_method: "app-store"
    )
    upload_to_testflight(
      skip_waiting_for_build_processing: true
    )
  end
end
```

### Firebase App Distribution — Internal Testing

```yaml
# GitHub Actions এ Firebase distribution
- name: Distribute to Firebase
  uses: wzieba/Firebase-Distribution-Github-Action@v1
  with:
    appId: ${{ secrets.FIREBASE_APP_ID_ANDROID }}
    serviceCredentialsFileContent: ${{ secrets.FIREBASE_CREDENTIALS }}
    groups: internal-testers, qa-team
    file: build/app/outputs/flutter-apk/app-release.apk
    releaseNotes: |
      Build: ${{ github.run_number }}
      Branch: ${{ github.ref_name }}
      Commit: ${{ github.sha }}
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="security"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 13 — Security — Mobile App এ
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Mobile Security Checklist

#### ১. Sensitive Data Storage

```dart
// ❌ কখনো করবে না
SharedPreferences.setString('auth_token', token);
// SharedPreferences Android এ plain text XML এ save হয়

// ✅ Sensitive data এর জন্য
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

const storage = FlutterSecureStorage(
  aOptions: AndroidOptions(
    encryptedSharedPreferences: true, // AES encryption
  ),
  iOptions: IOSOptions(
    accessibility: KeychainAccessibility.first_unlock,
  ),
);

await storage.write(key: 'auth_token', value: token);
final token = await storage.read(key: 'auth_token');
```

#### ২. API Key Management

```dart
// ❌ Hardcode করবে না কখনো
const apiKey = 'sk-live-abc123'; // Git এ চলে যাবে!

// ✅ --dart-define দিয়ে inject করো
// Run command:
// flutter run --dart-define=API_KEY=your_key_here

const apiKey = String.fromEnvironment('API_KEY');

// CI/CD তে GitHub Secrets থেকে আসবে:
// flutter build apk --dart-define=API_KEY=${{ secrets.API_KEY }}
```

#### ৩. Certificate Pinning

```dart
// http_certificate_pinning package ব্যবহার করো
// MITM (Man in the Middle) attack রোধ করে

import 'package:http_certificate_pinning/http_certificate_pinning.dart';

final client = HttpClientWithCertificatePinning(
  // SHA256 fingerprint of your server's SSL certificate
  trustedCertificate: '''
    sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
  ''',
);
```

#### ৪. Code Obfuscation

```bash
# Release build এ obfuscation চালাও
flutter build apk --obfuscate --split-debug-info=./debug-symbols
flutter build ipa --obfuscate --split-debug-info=./debug-symbols

# debug-symbols আলাদা রাখো — crash report symbolicate করতে লাগবে
# কিন্তু app bundle এ include করবে না
```

#### ৫. Root/Jailbreak Detection

```dart
// flutter_jailbreak_detection package
import 'package:flutter_jailbreak_detection/flutter_jailbreak_detection.dart';

Future<void> checkDeviceSecurity() async {
  bool isJailbroken = await FlutterJailbreakDetection.jailbroken;
  bool developerMode = await FlutterJailbreakDetection.developerMode;

  if (isJailbroken) {
    // Banking/payment app হলে block করো
    // অন্য app হলে warn করো
    showSecurityWarning();
  }
}
```

#### ৬. Screenshot Prevention (Banking apps)

```dart
// android/app/src/main/kotlin/MainActivity.kt
import android.view.WindowManager

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    window.setFlags(
      WindowManager.LayoutParams.FLAG_SECURE,
      WindowManager.LayoutParams.FLAG_SECURE
    )
  }
}
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="release-management"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 14 — Release Management
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Release Process — Checklist

```
━━━━ PRE-RELEASE (1 সপ্তাহ আগে) ━━━━

Code:
□ Feature freeze — নতুন feature আর নেবো না
□ All PRs merged এবং reviewed
□ flutter analyze — 0 errors
□ All tests passing
□ Test coverage target met

Version:
□ Version number bump (pubspec.yaml)
□ Build number increment
□ Changelog update করো

Testing:
□ QA team এর sign-off
□ Regression test complete
□ Performance test — startup time, frame rate
□ Testing on real devices (minimum 2 Android + 2 iOS)
□ Edge cases test (no network, low memory, old OS)

━━━━ RELEASE DAY ━━━━

□ Tag create করো (v1.2.0)
□ Release build তৈরি করো
□ Code signing verify করো
□ App Store Connect / Play Console এ upload
□ Release notes লিখো (user-friendly)
□ Staged rollout plan করো (5% → 20% → 100%)

━━━━ POST-RELEASE ━━━━

□ Crash rate monitor করো (Firebase Crashlytics)
□ ANR rate monitor করো (Play Console)
□ User reviews check করো
□ Key metrics watch করো (retention, session length)
□ Rollback plan ready রাখো
```

### Semantic Versioning — সঠিক নিয়ম

```
MAJOR.MINOR.PATCH+BUILD

যেমন: 2.1.3+45

MAJOR: Breaking change — পুরনো data incompatible
       User কে force update করতে হবে
       যেমন: 1.0.0 → 2.0.0

MINOR: নতুন feature, backward compatible
       যেমন: 1.0.0 → 1.1.0

PATCH: Bug fix, security fix
       যেমন: 1.0.0 → 1.0.1

BUILD: Play Store / App Store build number
       সবসময় increment করতে হয়
```

### Hotfix Process

```
Production এ critical bug পাওয়া গেছে:

Step 1: Severity assess করো
        P0: App crash / data loss → immediate fix
        P1: Major feature broken → same day fix
        P2: Minor issue → next release

Step 2: Hotfix branch তৈরি করো
        git checkout -b hotfix/fix-crash-on-payment main

Step 3: Fix করো + test করো

Step 4: Expedited review
        Normal review process এর চেয়ে fast

Step 5: Deploy
        Only the fix — no other changes

Step 6: Post-mortem
        কী হয়েছিল, কেন হয়েছে, পরের বার কীভাবে আটকাবো
```

### Force Update Strategy

```dart
// Remote config থেকে minimum supported version check করো
Future<void> checkAppVersion() async {
  final remoteConfig = FirebaseRemoteConfig.instance;
  await remoteConfig.fetchAndActivate();

  final minVersion = remoteConfig.getString('min_app_version'); // "2.0.0"
  final currentVersion = await PackageInfo.fromPlatform().then(
    (info) => info.version,
  );

  if (_isVersionLower(currentVersion, minVersion)) {
    // Force update dialog দেখাও
    showForceUpdateDialog();
  }
}
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="documentation"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 15 — Documentation
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### কোন Documentation লিখতে হবে

Tech Lead হিসেবে documentation তোমার দায়িত্ব। এটা boring মনে হলেও এটা ছাড়া team scale হয় না।

#### ১. README.md — Project এর ভূমিকা

```markdown
# [App Name]

## Overview
এই app কী করে — ২-৩ sentence এ।

## Prerequisites
- Flutter 3.24.0+
- Dart 3.5.0+
- Android Studio / VS Code
- [অন্য tools]

## Getting Started

### Environment Setup
1. Repository clone করো:
   ```bash
   git clone https://github.com/org/app.git
   cd app
   ```

2. Dependencies install করো:
   ```bash
   flutter pub get
   ```

3. Environment variables setup করো:
   ```bash
   cp .env.example .env
   # .env file এ API URLs দাও
   ```

4. Run করো:
   ```bash
   flutter run --dart-define-from-file=.env
   ```

## Architecture
[Architecture diagram + brief description]
[Link to detailed architecture doc]

## Folder Structure
[Folder structure explanation]

## Contributing
[Code style, PR process, commit message format]

## Team
[Team members ও responsibilities]
```

#### ২. Architecture Decision Records (ADR)

**কেন এই decision নিলাম** — এটা document করা অনেক valuable।

```markdown
# ADR 001: State Management — BLoC এর পরিবর্তে Riverpod

## Status: Accepted

## Date: 2024-01-15

## Context
আমাদের app এ state management solution choose করতে হবে।
Current codebase এ BLoC ব্যবহার হচ্ছে।

## Options Considered
1. BLoC (current)
2. Riverpod
3. Provider

## Decision
Riverpod বেছে নেওয়া হয়েছে।

## Reasoning
- Compile-time safety: BLoC এ runtime error বেশি
- Testing সহজ: Riverpod এ override করা সহজ
- Boilerplate কম: BLoC এ Event/State class বেশি
- Team familiarity: নতুন developer দের কাছে বেশি accessible

## Trade-offs
- Migration cost: existing BLoC code migrate করতে হবে
- Learning curve: team কে নতুন pattern শিখতে হবে

## Migration Plan
- New features: Riverpod
- Existing features: gradual migration, sprint by sprint
```

#### ৩. Onboarding Guide

```markdown
# New Developer Onboarding Guide

## প্রথম দিন
- [ ] Repository access নাও
- [ ] Development environment setup করো (README দেখো)
- [ ] Codebase overview নাও (Architecture doc দেখো)
- [ ] First simple bug fix করো (good first issues label দেখো)

## প্রথম সপ্তাহ
- [ ] Architecture পুরো বোঝো
- [ ] একটা small feature implement করো
- [ ] Code review process বোঝো
- [ ] Team conventions পড়ো

## কাকে কী জিজ্ঞেস করবে
- Architecture questions: [Tech Lead নাম]
- CI/CD questions: [DevOps person]
- Design questions: [Designer]
- Product questions: [Product Manager]

## Useful Links
- Figma designs: [link]
- API documentation: [link]
- JIRA board: [link]
- Slack channels: #mobile-dev, #general
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="hiring"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 16 — Hiring ও Interview নেওয়া
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Flutter Developer Interview Framework

Tech Lead হিসেবে তোমাকে technical interview নিতে হবে।

#### Interview Structure (1 ঘণ্টা)

```
┌─────────────────────────────────────────────────────┐
│  00-10 min: Introduction ও background               │
│  10-35 min: Technical questions                     │
│  35-50 min: Live coding বা code review              │
│  50-60 min: Candidate এর প্রশ্নের উত্তর            │
└─────────────────────────────────────────────────────┘
```

#### Senior Flutter Developer এর জন্য প্রশ্ন

**Dart Fundamentals:**
```
১. Sound null safety explain করো।
   What is the difference between `?`, `!`, and `??`?

২. Isolates কী? কখন ব্যবহার করবে?
   Main Isolate থেকে কীভাবে communicate করে?

৩. `const` constructor এর সুবিধা কী?
   কোথায় কোথায় const দেওয়া যায়?

৪. Extension methods কী? একটা practical example দাও।
```

**Flutter Architecture:**
```
৫. Clean Architecture explain করো Flutter context এ।
   তিনটা layer কী কী এবং কেন?

৬. BLoC vs Riverpod — trade-offs কী কী?
   কোন situation এ কোনটা choose করবে?

৭. Widget rebuild unnecessary হলে কীভাবে prevent করবে?

৮. Keys Flutter এ কী কাজ করে?
   ValueKey, ObjectKey, GlobalKey কখন কোনটা?
```

**Performance:**
```
৯. Jank কী? কীভাবে detect করবে? কীভাবে fix করবে?

১০. App size কমানোর techniques কী কী?

১১. Memory leak Flutter এ কীভাবে হয়?
    StreamSubscription এর ক্ষেত্রে কী করতে হয়?
```

#### Live Coding Task (15 মিনিট)

```dart
// Task: এই code review করো এবং সমস্যা খুঁজে বের করো

class UserProfileScreen extends StatefulWidget {
  final String userId;
  const UserProfileScreen({required this.userId});

  @override
  State<UserProfileScreen> createState() => _UserProfileScreenState();
}

class _UserProfileScreenState extends State<UserProfileScreen> {
  User? user;
  bool isLoading = false;

  @override
  void initState() {
    super.initState();
    loadUser();
  }

  Future<void> loadUser() async {
    setState(() => isLoading = true);
    final response = await http.get(
      Uri.parse('https://api.example.com/users/${widget.userId}'),
    );
    final data = jsonDecode(response.body);
    setState(() {
      user = User.fromJson(data);
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (isLoading) return CircularProgressIndicator();
    return Column(
      children: [
        Text(user!.name),
        Text(user!.email),
        ElevatedButton(
          onPressed: loadUser,
          child: Text('Refresh'),
        ),
      ],
    );
  }
}

// Problems to find:
// 1. http directly use (should use repository/service)
// 2. No error handling
// 3. user! force unwrap — crash if null
// 4. No dispose/cancel of ongoing requests (widget unmount হলে setState call হবে)
// 5. Business logic in UI layer (violates clean architecture)
// 6. No loading center alignment
// 7. Missing const where possible
```

### Red Flags — কাকে নেবে না

```
Technical red flags:
❌ "আমি সবসময় setState ব্যবহার করি — সহজ"
   (State management বোঝে না)

❌ Error handling জিজ্ঞেস করলে blank
   (Production experience নেই)

❌ Testing এর কথা জিজ্ঞেস করলে "সময় পাই না"
   (Professional attitude নেই)

❌ "Architecture মানে শুধু folder structure"
   (Shallow understanding)

Attitude red flags:
❌ Code review কে criticism হিসেবে নেয়
❌ "আমার approach সবচেয়ে ভালো" — flexibility নেই
❌ Learning এ interest নেই
❌ Team এর সাথে কাজ করতে সমস্যা
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="roadmap"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 17 — ১২ মাসের Roadmap
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### তোমার বর্তমান অবস্থান

Senior Flutter Developer হিসেবে তোমার solid experience আছে। তুমি:
- ✅ Flutter deeply জানো
- ✅ Production apps বানিয়েছো
- ✅ Complex features implement করেছো
- ⬜ Architecture formally শেখোনি (অনেকে শেখে না)
- ⬜ Team lead করোনি formally
- ⬜ Code review process চালাওনি systematically
- ⬜ Testing culture তৈরি করোনি

### Month 1-3: Foundation শক্ত করো

```
Technical:
━━━━━━━━━
□ Clean Architecture পুরোপুরি implement করো
  Resource: "Flutter Clean Architecture" — Reso Coder (YouTube)
  Practice: বর্তমান project এর একটা feature refactor করো

□ Advanced Dart শেখো
  Resource: Dart official docs — Language tour
  Focus: Isolates, Extensions, Records, Patterns (Dart 3)

□ Riverpod বা BLoC — যেটা নেই সেটা শেখো
  Resource: Official docs + Andrea Bizzotto (YouTube)

□ Testing শুরু করো
  Target: বর্তমান project এ ৩টা Unit test লিখো
  Resource: Very Good Ventures testing series

Team:
━━━━
□ বর্তমান team এ voluntarily code review করা শুরু করো
□ একজন Junior কে weekly help করো
□ Team এ একটা knowledge sharing session দাও
```

### Month 4-6: Leadership Practice

```
Technical:
━━━━━━━━━
□ CI/CD pipeline setup করো বর্তমান project এ
  Tool: GitHub Actions + Firebase App Distribution

□ Performance audit করো বর্তমান app এ
  Tool: Flutter DevTools
  Target: Startup time, jank, memory leaks

□ Security audit করো
  Checklist: এই document এর Chapter 13

□ Architecture Decision Record লেখা শুরু করো
  প্রথম ADR: State management choice

Team:
━━━━
□ PR template তৈরি করো team এ
□ Code review guidelines লিখে share করো
□ 1-on-1 meeting শুরু করো (volunteer হিসেবে)
□ Tech talk দাও team এ — যেকোনো topic

Career:
━━━━━━
□ Manager এর সাথে কথা বলো:
  "আমি Mobile Tech Lead হতে interested।
   কী করলে সেদিকে যেতে পারবো?"
```

### Month 7-9: Ownership নাও

```
Technical:
━━━━━━━━━
□ একটা complex feature end-to-end own করো
  Architecture → Implementation → Review → Release

□ Testing coverage বাড়াও
  Target: 70%+ coverage project এ

□ Documentation শুরু করো
  - README update করো
  - Architecture doc লিখো
  - Onboarding guide তৈরি করো

Team:
━━━━
□ Junior developer কে mentor করো formally
□ Code review এর quality improve করো — constructive feedback
□ Sprint planning এ technical input বেশি দাও

Visibility:
━━━━━━━━━
□ GitHub profile active করো
□ Flutter community তে contribute করো
  (Bug report, PR, Stack Overflow answer)
□ LinkedIn এ technical posts লিখো
```

### Month 10-12: Role এর জন্য Position করো

```
Technical:
━━━━━━━━━
□ Architecture এর major decision নাও
  এবং team কে defend করতে পারো

□ Technical roadmap তৈরি করো (৬ মাসের)
  কী improve করবো, কেন, কীভাবে

□ Performance benchmarks establish করো
  Baseline metrics এবং targets

Career:
━━━━━━
□ Performance review এ clearly বলো goal
□ Tech Lead job description দেখো
  কী gap আছে সেটা identify করো

□ যদি current company তে opportunity না থাকে:
  বাইরে apply করো
  Tech Lead role এ interview দাও
  Portfolio: GitHub + architecture decisions + team impact
```

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

<a id="resources"></a>

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 Chapter 18 — Resources ও Tools
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Flutter Technical — Best Resources

```
YouTube Channels:
━━━━━━━━━━━━━━━
✅ Reso Coder — Clean Architecture, BLoC
   সেরা Flutter architecture content

✅ Andrea Bizzotto (Code with Andrea) — Riverpod, architecture
   Production-grade Flutter patterns

✅ Very Good Ventures — Testing, best practices
   Enterprise Flutter development

✅ Robert Brunhage — Flutter tips, performance

Books:
━━━━━
✅ "Flutter in Action" — Eric Windmill
✅ "Programming Flutter" — Carmine Zaccagnino

Official Docs:
━━━━━━━━━━━━
✅ flutter.dev/docs
✅ dart.dev/guides
✅ pub.dev (package documentation)

Newsletters:
━━━━━━━━━━━
✅ Flutter Weekly (flutterweekly.net)
✅ Dart Weekly
```

### Leadership — Best Resources

```
Books (সবচেয়ে important):
━━━━━━━━━━━━━━━━━━━━━━━
✅ "The Manager's Path" — Camille Fournier
   Tech Lead থেকে Engineering Manager পর্যন্ত সব।
   এটা পড়া mandatory।

✅ "An Elegant Puzzle" — Will Larson
   Engineering management এর practical guide।

✅ "Staff Engineer" — Will Larson
   Senior IC path — management না গেলেও এটা পড়ো।

✅ "The Pragmatic Programmer" — Hunt & Thomas
   Software craftsmanship — timeless।

✅ "Clean Code" — Robert C. Martin
   Code quality এর bible।

Newsletters:
━━━━━━━━━━━
✅ The Pragmatic Engineer (pragmaticengineer.com/newsletter)
   Senior engineering এর সবচেয়ে ভালো newsletter।
   Gergely Orosz লেখেন — ex-Uber engineer।

✅ LeadDev (leaddev.com)
   Tech Lead specific content।

YouTube:
━━━━━━━
✅ LeadDev YouTube channel
✅ "Tech Lead" channel — Patrick Shyu (ex-Google TL)
```

### Essential Tools

```
Development:
━━━━━━━━━━
✅ Flutter DevTools — performance, debugging
✅ VS Code + Flutter extension
✅ Android Studio (Android specific debugging)
✅ Charles Proxy / Proxyman — network debugging
✅ Flipper — debugging Swiss knife

Design:
━━━━━━
✅ Figma — design handoff
✅ Zeplin — design specs

Project Management:
━━━━━━━━━━━━━━━━
✅ Linear — modern, fast (Jira alternative)
✅ Jira — enterprise standard
✅ GitHub Projects — simple, integrated

Monitoring:
━━━━━━━━━
✅ Firebase Crashlytics — crash reporting
✅ Firebase Performance — app performance
✅ Sentry — error tracking (alternative to Crashlytics)
✅ Firebase Analytics — user behavior

CI/CD:
━━━━━
✅ GitHub Actions — free, integrated (recommended)
✅ Bitrise — mobile-specific CI/CD
✅ Codemagic — Flutter-specific CI/CD

Code Quality:
━━━━━━━━━━━
✅ Codecov — code coverage tracking
✅ SonarQube — code quality analysis
✅ Dart Code Metrics — Flutter specific metrics
```

### Flutter Essential Packages — 2024-2025

```
Architecture:
━━━━━━━━━━━
✅ flutter_bloc: ^9.x — BLoC pattern
✅ flutter_riverpod: ^3.x — Riverpod (flutter_riverpod)
✅ get_it: ^9.x — Service locator (DI)
✅ injectable: ^3.x — Code generation for DI
✅ dartz: ^0.10.x — Functional programming (Either)
✅ freezed: ^3.x — Immutable classes (code gen)

Networking:
━━━━━━━━━
✅ dio: ^5.x — HTTP client
✅ retrofit: ^4.x — Type-safe API client (code gen)
✅ connectivity_plus: ^7.x — Network connectivity

Storage:
━━━━━━━
✅ flutter_secure_storage: ^10.x — Encrypted storage
✅ shared_preferences: ^2.x — Simple key-value
✅ isar: ^3.x — Fast local database
✅ drift: ^2.x — SQLite ORM

Navigation:
━━━━━━━━━
✅ go_router: ^17.x — Official Google router

UI:
━━━
✅ cached_network_image: ^3.x — Image caching
✅ shimmer: ^3.x — Loading placeholder
✅ flutter_svg: ^2.x — SVG support

Testing:
━━━━━━━
✅ bloc_test: ^10.x — BLoC testing
✅ mocktail: ^1.x — Mocking
✅ golden_toolkit: ^0.15.x — Golden tests

Monitoring:
━━━━━━━━━
✅ firebase_crashlytics: ^5.x — Crash reporting
✅ firebase_performance: ^0.11.x — Performance
```

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## 📘 শেষ কথা — তোমার জন্য

Senior Software Engineer হিসেবে তোমার experience তোমাকে **technically ready** করেছে।

কিন্তু Tech Lead হওয়া মানে শুধু technical দক্ষতা না।

**তোমাকে যা করতে হবে:**

```
আজ থেকেই:
  → Tech Lead এর মতো আচরণ করো — title আগে না
  → Code review তে actively অংশ নাও
  → Junior কে help করো — প্রশ্ন করে, করে দিয়ে না
  → Architecture decision এ opinion দাও
  → Documentation লেখা শুরু করো

৩ মাসের মধ্যে:
  → Clean Architecture implement করো
  → CI/CD pipeline চালু করো
  → Testing শুরু করো

৬ মাসের মধ্যে:
  → Manager কে clearly বলো তোমার goal
  → Team এর technical decisions এ ownership নাও

১ বছরের মধ্যে:
  → Mobile Tech Lead হিসেবে recognized হবে
  → Title পাবে — current company তে বা নতুন জায়গায়
```

> **মনে রাখো:**
> তুমি যদি আজ Tech Lead এর মতো কাজ করো —
> কেউ তোমাকে Tech Lead বলুক বা না বলুক,
> তুমি ইতিমধ্যে Tech Lead।
> Title শুধু official recognition।

তোমার journey শুরু হোক আজ থেকেই। 🚀

---

[⬆ Table of Contents এ ফিরে যাও](#toc)

---

*এই document টা তোমার career journey এর সাথে update হতে থাকবে।*
*Version 1.2 — 2026 (updated: package versions, Flutter 3.41.9, Riverpod recommendation, Dart Isolates closures, certificate pinning package name)*
