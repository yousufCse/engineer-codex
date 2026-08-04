# Section 4 — Navigation & Routing

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a detailed, step-by-step explanation with real-life examples and code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** Always give the **short answer first** (2–3 sentences), then stop. Let the interviewer ask "can you go deeper?" Speaking simply and clearly is itself a senior skill — and it works the same for both remote and BD companies.

---

<a id="toc"></a>

## Table of Contents

**A. Navigator 1.0 (the imperative stack)**
1. [Navigator 1.0 — the stack, push/pop/pushReplacement/pushAndRemoveUntil/maybePop](#q1) · *Very common*
2. [Passing data back with `pop` and awaiting a result](#q2) · *Common*
3. [Named routes — `onGenerateRoute` and `MaterialApp.routes`](#q3) · *Common*

**B. Navigator 2.0 (the declarative model)**
4. [Why Navigator 2.0 was introduced — the 3 problems it solves](#q4) · *Very common*
5. [Navigator 2.0 internals — Router, RouteInformationParser, RouterDelegate](#q5) · *Deeper*

**C. go_router (the production standard)**
6. [go_router basics — routes, subroutes, path & query parameters](#q6) · *Very common*
7. [`go()` vs `push()` vs `replace()` in go_router](#q7) · *Very common*
8. [Auth / login guard with `redirect` and `refreshListenable`](#q8) · *Very common*
9. [`ShellRoute` and `StatefulShellRoute` — persistent bottom nav](#q9) · *Very common*
10. [Named routes vs typed routes (go_router_builder)](#q10) · *Common*
11. [Passing arguments — the safe way vs the unsafe `extra`](#q11) · *Very common*
12. [Handling 404 / unknown routes](#q12) · *Common*

**D. Real-world navigation problems**
13. [Deep linking — App Links (Android) & Universal Links (iOS)](#q13) · *Common*
14. [`PopScope` — intercepting the back button](#q14) · *Very common*
15. [Navigating from outside the widget tree (Cubit / service)](#q15) · *Common*
16. [Nested navigators — why each tab needs its own stack](#q16) · *Common*
17. [Custom page transitions / animations](#q17) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 17 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — The stack basics (start here).** Almost every interview starts here.
→ [Q1 Navigator 1.0 stack](#q1) · [Q2 Return data with pop](#q2) · [Q3 Named routes](#q3)

**Stage 2 — Why declarative routing exists.** This shows you understand the *why*.
→ [Q4 Why Navigator 2.0](#q4) · [Q6 go_router basics](#q6) · [Q7 go vs push vs replace](#q7)

**Stage 3 — The real production patterns.** This is what daily work looks like.
→ [Q8 Auth guard](#q8) · [Q9 Persistent bottom nav](#q9) · [Q11 Passing arguments](#q11) · [Q14 PopScope](#q14)

**Stage 4 — Edge cases & quality.** These separate strong seniors.
→ [Q10 Typed routes](#q10) · [Q12 404 routes](#q12) · [Q13 Deep linking](#q13) · [Q15 Navigate outside the tree](#q15) · [Q16 Nested navigators](#q16) · [Q17 Custom transitions](#q17)

**Stage 5 — Deep-dive tie-breaker (do last).** Few people can explain this clearly.
→ [Q5 Navigator 2.0 internals](#q5)

**Short on time (1 hour before the interview)?** Just review these eight:
[Q1](#q1) · [Q4](#q4) · [Q6](#q6) · [Q7](#q7) · [Q8](#q8) · [Q9](#q9) · [Q11](#q11) · [Q14](#q14), then read the [Cheat Sheet](#cheatsheet).

---

# A. Navigator 1.0 (the imperative stack)

---

<a id="q1"></a>
## 1. Explain Navigator 1.0. How does the stack work? Walk through `push`, `pop`, `pushReplacement`, `pushAndRemoveUntil`, and `maybePop`.

> Very common · Easy–Medium

**Short answer (say this):**
"Navigator 1.0 keeps screens in a stack — last in, first out, like a pile of plates. `push` puts a new screen on top, `pop` removes the top one. `pushReplacement` swaps the current screen for a new one, and `pushAndRemoveUntil` clears screens below until a condition is met. `maybePop` is a safe pop that won't accidentally close the app on the root screen."

**Let's understand it fully:**

**Step 1 — The pile of plates idea.**
Think of the navigation stack as a pile of plates. You always touch the top plate first. The newest screen sits on top and is the one the user sees. The older screens stay underneath, still alive in memory.

```
Navigator stack (top = visible):

  ┌─────────────┐
  │  Screen C   │  ← top (on screen now)
  ├─────────────┤
  │  Screen B   │
  ├─────────────┤
  │  Screen A   │  ← bottom (the first/root screen)
  └─────────────┘
```

**Step 2 — `push`: put a new plate on top.**
A new screen goes on top. The old one stays underneath, untouched.

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (_) => const DetailScreen()),
);
```

**Step 3 — `pop`: remove the top plate.**
The top screen is removed, and the one below it becomes visible again.

```dart
Navigator.pop(context); // go back one screen
```

**Step 4 — `pushReplacement`: swap the top plate.**
This removes the current screen and puts a new one in its place. The stack size stays the same. This is the right tool for login → home: after logging in, the user should not be able to press back and return to the login screen.

```dart
Navigator.pushReplacement(
  context,
  MaterialPageRoute(builder: (_) => const HomeScreen()),
);
```

**Step 5 — `pushAndRemoveUntil`: push, then throw away plates below.**
This pushes a new screen and removes screens underneath until a test says "stop." Pass `(route) => false` to remove *everything* below — perfect for "go home and clear the whole stack" (for example, after logout).

```dart
Navigator.pushAndRemoveUntil(
  context,
  MaterialPageRoute(builder: (_) => const HomeScreen()),
  (route) => false, // false = remove ALL routes below the new one
);
```

```
pushAndRemoveUntil with (route) => false:

BEFORE:                      AFTER:
┌─────────────┐
│  Screen D   │              ┌─────────────┐
├─────────────┤              │    Home     │  ← pushed (only this remains)
│  Screen C   │   ───────►   └─────────────┘
├─────────────┤
│  Screen B   │
├─────────────┤
│  Screen A   │
└─────────────┘
```

**Step 6 — `maybePop`: a polite, safe pop.**
`maybePop` tries to pop, but if there is nothing below (we are on the root screen), it does nothing instead of closing the app. It also respects `PopScope`, so an "unsaved changes" guard can still block it. Use it when you are not sure the screen can be popped.

```dart
Navigator.maybePop(context); // safe: won't blow away the app on the root
```

**Why interviewers ask:** They want to see that you understand the stack as a concept, not just which method name to type. Picking the right method for "login cleanup" or "clear everything" is a senior signal.

**Common mistake:** Mixing up `pushReplacement` and `pushAndRemoveUntil`. `pushReplacement` removes only the *current* screen — everything below stays. `pushAndRemoveUntil` keeps removing until the test returns true. Another mistake is using `pop` where `maybePop` is safer (on a root screen, a raw `pop` can pop the app's last route).

**Follow-ups they may ask:**
- *"What does the predicate in `pushAndRemoveUntil` mean?"* → It's a test run on each screen below; keep popping while it returns `false`, stop when it returns `true`. `(route) => false` removes them all.
- *"Does a popped screen get rebuilt later?"* → A popped route is disposed. A pushed-over (still in the stack) route is kept alive and not rebuilt.

**Related:** [Q2 — return data with pop](#q2) · [Q7 — go vs push in go_router](#q7) · [Q16 — nested navigators](#q16)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How do you pass data back to the previous screen? How does awaiting a navigation result work?

> Common · Easy–Medium

**Short answer (say this):**
"`Navigator.push` returns a `Future` that completes when the screen is popped. So I `await` the push, and on the other screen I call `Navigator.pop(context, result)` to send a value back. It's like ordering at a counter: you wait at the counter, and the value comes back when the other screen closes."

**Let's understand it fully:**

**Step 1 — `push` gives you a Future.**
When you push a screen, you get back a `Future`. That Future stays unfinished while the new screen is open, and completes with a value the moment that screen is popped.

```dart
// Open a picker screen and wait for what the user chose
final selected = await Navigator.push<String>(
  context,
  MaterialPageRoute(builder: (_) => const PickColorScreen()),
);

// This line runs only AFTER PickColorScreen is popped
if (selected != null) {
  print('User picked $selected');
}
```

**Step 2 — `pop` sends the value back.**
On the second screen, pass the result as the second argument to `pop`. That value becomes what the awaiting Future returns.

```dart
// inside PickColorScreen
ElevatedButton(
  onPressed: () => Navigator.pop(context, 'blue'), // send 'blue' back
  child: const Text('Pick blue'),
);
```

**Step 3 — Handle the "user pressed back" case.**
If the user leaves by swiping back or tapping the system back button (not your button), no value is sent, so the result is `null`. Always plan for `null`.

```dart
final result = await Navigator.push<bool>(...);
final didConfirm = result ?? false; // back-press → treat as "no"
```

**Step 4 — The same idea in go_router.**
go_router supports this too: `push` returns a Future, and `pop` can carry a value.

```dart
final result = await context.push<String>('/pick-color');
// on the picker screen:
context.pop('blue');
```

**Why interviewers ask:** Returning a value from a screen (a picker, a confirm dialog, an edit form) is an everyday task. They want to see you know the `await push` / `pop(value)` pair and that you handle the back-press case.

**Common mistake:** Forgetting that the result can be `null` when the user backs out. Reading it as if it's always present causes a crash or wrong logic.

**Follow-ups they may ask:**
- *"What type does `push` return?"* → `Future<T?>`, where `T` is the type you pass to `pop`. It's nullable because the user can leave without sending a value.
- *"Does `showDialog` work the same way?"* → Yes. `showDialog<bool>(...)` returns a Future, and `Navigator.pop(context, true)` inside the dialog sends the result back.

**Related:** [Q1 — push/pop basics](#q1) · [Q11 — passing arguments forward](#q11)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What are named routes? How do `MaterialApp.routes` and `onGenerateRoute` work?

> Common · Medium

**Short answer (say this):**
"Named routes let me navigate using a string name like `/details` instead of building a `MaterialPageRoute` every time. I register simple routes in `MaterialApp.routes`, and use `onGenerateRoute` when I need to read arguments or decide the screen dynamically. It's the classic approach before go_router."

**Let's understand it fully:**

**Step 1 — The map of names (`routes`).**
`MaterialApp.routes` is a simple lookup table: a name maps to a builder. You navigate by name.

```dart
MaterialApp(
  initialRoute: '/',
  routes: {
    '/': (context) => const HomeScreen(),
    '/settings': (context) => const SettingsScreen(),
  },
);

// Navigate by name:
Navigator.pushNamed(context, '/settings');
```

**Step 2 — The problem `routes` can't solve well.**
The `routes` map can't easily read arguments or choose a screen based on logic (like an unknown id). For that, use `onGenerateRoute`.

**Step 3 — `onGenerateRoute`: build routes with logic.**
`onGenerateRoute` is a single function that receives the route settings (name + arguments) and returns a route. You decide what to build.

```dart
MaterialApp(
  onGenerateRoute: (settings) {
    switch (settings.name) {
      case '/':
        return MaterialPageRoute(builder: (_) => const HomeScreen());
      case '/product':
        // read the argument passed in pushNamed
        final id = settings.arguments as String;
        return MaterialPageRoute(builder: (_) => ProductScreen(id: id));
      default:
        // unknown name → a simple 404 screen
        return MaterialPageRoute(builder: (_) => const NotFoundScreen());
    }
  },
);

// Navigate and pass an argument:
Navigator.pushNamed(context, '/product', arguments: '42');
```

**Step 4 — Reading the argument safely.**
The `arguments` field is typed as `Object?`, so it is not type-safe — you must cast it, and a wrong type crashes at runtime. This weakness is one big reason go_router and typed routes exist.

```dart
final args = settings.arguments;
if (args is String) {
  return MaterialPageRoute(builder: (_) => ProductScreen(id: args));
}
return MaterialPageRoute(builder: (_) => const NotFoundScreen());
```

**Why interviewers ask:** Named routes are still common in older codebases and small apps. They want to see you know both the simple `routes` map and the more flexible `onGenerateRoute`, and that you understand the type-safety weakness.

**Common mistake:** Putting argument-reading logic in the `routes` map (it can't access arguments cleanly). Use `onGenerateRoute` for anything with arguments. Also, casting `settings.arguments` blindly and crashing when it's the wrong type.

**Follow-ups they may ask:**
- *"`onGenerateRoute` vs `onUnknownRoute`?"* → `onGenerateRoute` handles all named pushes. `onUnknownRoute` is the fallback only when `onGenerateRoute` returns null — a place for a 404 screen.
- *"Why move to go_router?"* → Named routes are string-based and untyped, and they don't handle web URLs or deep links cleanly. go_router fixes all of that ([Q6](#q6)).

**Related:** [Q1 — Navigator 1.0](#q1) · [Q6 — go_router basics](#q6) · [Q10 — typed routes](#q10)

[↑ Back to top](#toc)

---

# B. Navigator 2.0 (the declarative model)

---

<a id="q4"></a>
## 4. Why was Navigator 2.0 introduced? What problems does it solve that Navigator 1.0 couldn't?

> Very common · Medium

**Short answer (say this):**
"Navigator 1.0 is imperative — you manually push and pop one screen at a time. That breaks down for deep links, web URLs, and the back button, because there is no clean way to rebuild a whole stack from a URL. Navigator 2.0 is declarative: you describe the *whole* page stack from your app state, and Flutter figures out the transitions — the same idea as `build()` for widgets."

**Let's understand it fully:**

**Step 1 — Imperative vs declarative (the core idea).**
- **Navigator 1.0 (imperative):** you give step-by-step orders — "push A, then push B, then push C." You manage the stack by hand.
- **Navigator 2.0 (declarative):** you describe the end result — "the stack should be [A, B, C]" — and Flutter works out how to get there.

```
Navigator 1.0 (imperative):
  Link tapped → you write: push(A); push(B); push(C);
  URL changed? You parse and push manually.

Navigator 2.0 (declarative):
  URL / state changed → you declare: "the stack is [A, B, C]"
  Flutter diffs the old and new stack and animates.
```

**Step 2 — Problem 1: deep linking.**
If a user opens `myapp.com/products/42`, Navigator 1.0 has no clean way to rebuild the full path (Home → Products → Product 42). You'd need fragile manual code to push several screens in the right order. Declarative routing rebuilds the whole stack from the URL automatically.

**Step 3 — Problem 2: keeping the web URL in sync.**
On Flutter web, the browser address bar should match the current screen, and editing the URL should change the screen. Navigator 1.0 has no built-in link between the stack and the URL, so they drift apart. Navigator 2.0 connects URL and stack in both directions.

**Step 4 — Problem 3: predictable back navigation.**
The Android back button and the browser back button should always do the right thing. With Navigator 1.0 there is no single declared "this is the whole stack" to fall back on. Navigator 2.0 always knows the full intended stack, so back behaves predictably.

```dart
// Navigator 2.0 — declarative (conceptual)
Navigator(
  pages: [
    const MaterialPage(child: HomeScreen()),
    if (selectedProductId != null)
      MaterialPage(child: ProductScreen(id: selectedProductId!)),
  ],
  onDidRemovePage: (page) {
    selectedProductId = null; // update state; the stack rebuilds from it
  },
);
```

**Why interviewers ask:** They want to know if you understand *why* a tool exists, not just how to call it. Explaining the three pain points (deep links, web URL, back button) shows architectural maturity.

**Common mistake:** Saying Navigator 2.0 "replaces" Navigator 1.0. It doesn't — Navigator 1.0 is still valid and simpler for basic mobile-only apps. Also, confusing Navigator 2.0's raw API with go_router: go_router is a wrapper built *on top of* Navigator 2.0 that hides the hard parts.

**Follow-ups they may ask:**
- *"Do I write Navigator 2.0 by hand in real apps?"* → Almost never. Everyone uses go_router (or a similar package) on top of it.
- *"Is Navigator 1.0 dead?"* → No. For a small mobile-only app with simple flows, it's perfectly fine and less work.

**Related:** [Q5 — Navigator 2.0 internals](#q5) · [Q6 — go_router basics](#q6) · [Q13 — deep linking](#q13)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. Explain the core Navigator 2.0 internals — `Router`, `RouteInformationParser`, and `RouterDelegate`. What does each do?

> Deeper · Hard — a senior tie-breaker.

**Short answer (say this):**
"Navigator 2.0 has three parts that form a pipeline from the URL to the screen. The `RouteInformationParser` turns a URL string into my own route object. The `RouterDelegate` is the brain — it turns that object into a list of pages and builds the `Navigator`. The `Router` widget ties them together. In real code I let go_router implement all three for me."

**Let's understand it fully:**

**Step 1 — The pipeline: URL in, screens out.**
Picture an assembly line. A raw URL comes in one end, and a stack of screens comes out the other.

```
Platform URL / deep link
          │
          ▼
┌──────────────────────────┐
│  RouteInformationParser  │  URL string  →  your route object
└──────────┬───────────────┘
           │  (route config)
           ▼
┌──────────────────────────┐
│      RouterDelegate      │  route object  →  List<Page> + builds Navigator
│        (the brain)       │  also handles pop and notifies on change
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│        Navigator         │  renders the real widget stack
└──────────────────────────┘
```

**Step 2 — `RouteInformationParser`: translate the URL.**
It takes a `RouteInformation` (basically a URI) and returns an app-specific config object you define. It also does the reverse — turns your config back into a URL so the browser bar updates.

```dart
class AppRouteParser extends RouteInformationParser<AppRoute> {
  @override
  Future<AppRoute> parseRouteInformation(RouteInformation info) async {
    final uri = info.uri;
    // /products/42 → AppRoute(productId: '42')
    if (uri.pathSegments.length == 2 && uri.pathSegments[0] == 'products') {
      return AppRoute(productId: uri.pathSegments[1]);
    }
    return AppRoute(); // home
  }

  @override
  RouteInformation? restoreRouteInformation(AppRoute config) {
    final path = config.productId == null ? '/' : '/products/${config.productId}';
    return RouteInformation(uri: Uri.parse(path));
  }
}
```

**Step 3 — `RouterDelegate`: the brain that builds the stack.**
It holds the navigation state, builds the `Navigator` with the right list of `Page` objects, and reacts when the parser hands it a new route. The key rule: call `notifyListeners()` whenever the navigation state changes, or the UI won't update.

```dart
class AppRouterDelegate extends RouterDelegate<AppRoute>
    with ChangeNotifier, PopNavigatorRouterDelegateMixin<AppRoute> {

  String? _productId;

  @override
  final GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();

  @override
  AppRoute get currentConfiguration => AppRoute(productId: _productId);

  @override
  Future<void> setNewRoutePath(AppRoute config) async {
    _productId = config.productId; // parser gave us a new route
  }

  @override
  Widget build(BuildContext context) {
    return Navigator(
      key: navigatorKey,
      pages: [
        const MaterialPage(child: HomeScreen()),
        if (_productId != null) MaterialPage(child: ProductScreen(id: _productId!)),
      ],
      onDidRemovePage: (page) {
        _productId = null;
        notifyListeners(); // tell Flutter the state changed
      },
    );
  }
}
```

**Step 4 — `Router`: the coordinator (you rarely touch it).**
The `Router` widget sits near the top of the tree and connects the parser and delegate. You normally hand them to `MaterialApp.router(...)` and never deal with `Router` directly.

```dart
MaterialApp.router(
  routerDelegate: AppRouterDelegate(),
  routeInformationParser: AppRouteParser(),
);
```

**Step 5 — Why you should mention go_router here.**
Writing all three classes by hand is a lot of boilerplate and easy to get wrong. In production, go_router implements the parser and delegate for you. The senior move in an interview is to explain the three roles clearly, then say "and that's exactly what go_router wraps, so I use go_router."

**Why interviewers ask:** This is a depth check. They want to see you understand the architecture (parse URL → decide state → build stack), not that you memorized boilerplate.

**Common mistake:** Trying to memorize every method of the raw API. Instead, explain the three roles and be honest that you use go_router. Another classic miss: forgetting that `RouterDelegate` must call `notifyListeners()` on state changes.

**Follow-ups they may ask:**
- *"What is `currentConfiguration` for?"* → It's how the delegate reports the current route back so the URL can be updated to match.
- *"Where does go_router fit?"* → It provides a ready-made parser and delegate, so you only write a route table.

**Related:** [Q4 — why Navigator 2.0](#q4) · [Q6 — go_router basics](#q6)

[↑ Back to top](#toc)

---

# C. go_router (the production standard)

---

<a id="q6"></a>
## 6. How does go_router work? Explain route declaration, subroutes, path parameters, and query parameters.

> Very common · Medium

**Short answer (say this):**
"go_router is a declarative routing package built on Navigator 2.0. I declare my whole route tree once as a list of `GoRoute` objects, and it handles URL parsing, deep links, and browser-URL sync. Path parameters use `:name` in the path; query parameters need no declaration and come from `GoRouterState`."

**Let's understand it fully:**

**Step 1 — Routes are a tree, like a folder structure.**
You declare routes as a tree. Child routes go in a parent's `routes` list, and their paths are *added on* to the parent's path automatically.

```
Route tree:

  /                          → HomeScreen
  ├── products               → ProductListScreen      (/products)
  │   └── :productId         → ProductDetailScreen     (/products/:productId)
  │       └── reviews        → ReviewsScreen           (/products/:productId/reviews)
  └── settings               → SettingsScreen          (/settings)
```

**Step 2 — Declare the tree.**
Each `GoRoute` has a `path` and a `builder`. Subroutes nest inside `routes`.

```dart
final router = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const HomeScreen(),
      routes: [
        GoRoute(
          path: 'products', // child path is relative → becomes /products
          builder: (context, state) => const ProductListScreen(),
          routes: [
            GoRoute(
              path: ':productId', // path parameter → /products/:productId
              builder: (context, state) {
                final id = state.pathParameters['productId']!;
                return ProductDetailScreen(id: id);
              },
            ),
          ],
        ),
        GoRoute(
          path: 'settings',
          builder: (context, state) => const SettingsScreen(),
        ),
      ],
    ),
  ],
);

MaterialApp.router(routerConfig: router);
```

**Step 3 — Path parameters (`:name`): part of the address.**
A path parameter is a slot inside the URL. It's required — the route only matches if it's present. Read it from `state.pathParameters`.

```dart
context.go('/products/42'); // 42 fills the :productId slot
// inside the builder:
final id = state.pathParameters['productId']!; // '42'
```

**Step 4 — Query parameters (`?key=value`): optional extras.**
Query parameters come after `?`. They need no declaration and are usually optional, like filters or sorting. Read them from `state.uri.queryParameters`.

```dart
context.go('/products?sort=price&category=phones');
// inside the builder:
final sort = state.uri.queryParameters['sort'];         // 'price'
final category = state.uri.queryParameters['category']; // 'phones'
```

A simple rule: **path parameters identify *which* thing** (which product), **query parameters tune *how* you see it** (sorting, filtering). Both are plain strings, so both survive a web page refresh and deep links.

**Why interviewers ask:** go_router is the de facto standard for Flutter routing today. They want to see you can design a clean route tree and know the difference between path and query parameters.

**Common mistake:** Putting a leading slash on a subroute path (`'/products'` instead of `'products'`). A leading slash makes it a top-level route, not a child, and the nesting breaks.

**Follow-ups they may ask:**
- *"Why is `pathParameters['productId']` non-null here?"* → Because the route only matches when that segment exists, so the parameter is guaranteed present (hence the `!`).
- *"Where do query parameters live?"* → On `state.uri.queryParameters`, not on `pathParameters`.

**Related:** [Q7 — go vs push](#q7) · [Q11 — passing arguments](#q11) · [Q12 — 404 routes](#q12)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. In go_router, what is the difference between `go()`, `push()`, and `replace()`?

> Very common · Medium

**Short answer (say this):**
"`go()` is declarative — it rebuilds the whole stack to match the target URL. `push()` is imperative — it adds one screen on top of the current stack, like Navigator 1.0. `replace()` swaps the top screen for a new one without growing the stack. I use `go()` for normal navigation and `push()` only when I want a screen layered on top."

**Let's understand it fully:**

**Step 1 — `go()`: set the whole stack from the URL.**
`go('/products/42')` tells go_router "the stack should now match this URL." go_router rebuilds it as Home → Products → Product 42. This is the declarative, URL-first way, and it's what keeps the browser bar correct on web.

```dart
context.go('/products/42'); // stack becomes Home → Products → Product 42
```

**Step 2 — `push()`: stack one screen on top.**
`push('/products/42')` does not rebuild the stack. It just adds that one screen on top of whatever is already showing — exactly like Navigator 1.0's `push`. Use it for things that sit "above" the current flow, like a detail you can pop back from to exactly where you were.

```dart
context.push('/products/42'); // add Product 42 on top of the current stack
final result = await context.push<bool>('/confirm'); // can return a value too
```

**Step 3 — `replace()`: swap the top screen.**
`replace()` removes the current top screen and puts the new one in its place. The stack size stays the same and no new history entry is added — good for login → home where back should not return to login.

```dart
context.replace('/home'); // swap the current screen for /home
```

**Step 4 — A simple table to remember.**

| Method | What it does | Stack effect | When |
|---|---|---|---|
| `go()` | rebuild stack to match the URL | resets to the matched tree | normal navigation, web URLs, deep links |
| `push()` | add one screen on top | stack grows by one | layered screens you pop back from |
| `replace()` | swap the top screen | stack size unchanged | login → home, no back to old screen |

**Step 5 — The web gotcha with `push()`.**
On web, `push()` adds a screen that isn't fully described by the URL. If the user refreshes, that pushed screen can be lost because the URL alone doesn't rebuild it. For URL-driven screens on web, prefer `go()`.

**Why interviewers ask:** Choosing `go()` vs `push()` wrong is one of the most common go_router bugs. They want to see you understand "declarative stack rebuild" vs "imperative add on top."

**Common mistake:** Using `push()` everywhere like in Navigator 1.0, then being surprised the browser URL doesn't update or back behaves oddly. For normal navigation, `go()` is usually the right default.

**Follow-ups they may ask:**
- *"What about the `Named` versions?"* → `goNamed`, `pushNamed`, `replaceNamed` do the same thing but take a route name plus parameters instead of a raw path ([Q10](#q10)).
- *"Does `push()` return a value?"* → Yes, `context.push<T>(...)` returns a Future that completes when you `context.pop(value)` ([Q2](#q2)).

**Related:** [Q1 — Navigator 1.0 push/pop](#q1) · [Q6 — go_router basics](#q6) · [Q11 — passing arguments](#q11)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. How do you implement an auth / login guard with go_router's `redirect`?

> Very common · Medium

**Short answer (say this):**
"go_router's `redirect` callback runs before every navigation. It returns `null` to allow the navigation, or a new path to send the user somewhere else. That's the perfect place for an auth guard: if the user isn't logged in, return `/login`. To react when auth changes (like a logout), I wire up `refreshListenable` so the redirect re-runs."

**Let's understand it fully:**

**Step 1 — The bouncer at the door.**
Think of `redirect` as a bouncer who checks everyone before they enter. If you're allowed, the bouncer waves you through (`return null`). If not, the bouncer sends you elsewhere (`return '/login'`).

```
User navigates to /dashboard
          │
          ▼
   redirect() runs
   logged in?  ── no ──►  return '/login'
          │ yes
          ▼
   return null (allow)  →  DashboardScreen shows
```

**Step 2 — The basic guard.**
Read your auth state, then decide. The most important detail: you must also allow the `/login` screen itself, or you create an infinite loop.

```dart
final router = GoRouter(
  initialLocation: '/',

  // runs on EVERY navigation
  redirect: (context, state) {
    final loggedIn = context.read<AuthCubit>().state.isAuthenticated;
    final goingToLogin = state.matchedLocation == '/login';

    // not logged in and not already heading to login → go to login
    if (!loggedIn && !goingToLogin) {
      return '/login?from=${state.matchedLocation}'; // remember where they wanted to go
    }
    // already logged in but heading to login → send home
    if (loggedIn && goingToLogin) {
      return '/';
    }
    return null; // allow
  },

  routes: [
    GoRoute(path: '/', builder: (_, __) => const HomeScreen()),
    GoRoute(
      path: '/login',
      builder: (_, state) {
        final from = state.uri.queryParameters['from'] ?? '/';
        return LoginScreen(redirectTo: from);
      },
    ),
    GoRoute(path: '/dashboard', builder: (_, __) => const DashboardScreen()),
  ],
);
```

**Step 3 — Remember the original destination.**
Notice the `?from=...`. If a logged-out user tries to open `/dashboard`, you send them to login but stash where they wanted to go. After a successful login, send them back there.

```dart
void onLoginSuccess(BuildContext context, String from) {
  context.go(from); // back to the page they originally wanted
}
```

**Step 4 — React to auth changes with `refreshListenable`.**
`redirect` runs on navigation, but what if the user's token expires while they sit on a screen? `refreshListenable` re-runs the redirect whenever your auth source changes, so a logout instantly bounces them to login.

```dart
final router = GoRouter(
  refreshListenable: GoRouterRefreshStream(authCubit.stream), // re-run redirect on auth change
  redirect: (context, state) {
    // same logic as Step 2
  },
  routes: [ /* ... */ ],
);
```

`GoRouterRefreshStream` (shipped with go_router) wraps any `Stream` into a `Listenable` that go_router watches.

**Why interviewers ask:** Auth guarding is a universal requirement. They check that you handle the tricky parts: avoiding an infinite redirect loop, remembering the original destination, and reacting to logout.

**Common mistake:** Forgetting the `goingToLogin` check, which creates an infinite loop — redirect sends you to `/login`, which triggers redirect again, forever. Also, skipping `refreshListenable`, so the router never reacts when the token expires.

**Follow-ups they may ask:**
- *"Where can you put a redirect besides the top level?"* → On a single `GoRoute` too (route-level `redirect`), to guard just that branch.
- *"How do you avoid the loop in one sentence?"* → Always allow navigation *to* the login page itself by returning `null` when the target is `/login`.

**Related:** [Q12 — unknown routes](#q12) · [Q9 — shell routes](#q9) · [Q15 — navigate outside the tree](#q15)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. What is go_router's `ShellRoute`? How do you build a persistent bottom navigation bar, and how is `StatefulShellRoute` different?

> Very common · Medium–Hard

**Short answer (say this):**
"`ShellRoute` wraps child routes in a shared shell — usually a `Scaffold` with a bottom bar — so only the body changes while the bar stays put. But a plain `ShellRoute` shares one stack, so switching tabs loses each tab's state. `StatefulShellRoute.indexedStack` gives each tab its own independent stack and keeps its scroll position and history. That's what real apps use."

**Let's understand it fully:**

**Step 1 — The picture frame idea.**
A shell is like a picture frame. The frame (bottom bar) stays fixed; only the picture inside (the page) changes when you switch tabs.

```
ShellRoute layout:

┌────────────────────────────┐
│                            │
│     child route content    │  ← changes when navigating
│                            │
├────────────────────────────┤
│  Home  │ Search │ Profile  │  ← persistent shell, doesn't rebuild
└────────────────────────────┘
```

**Step 2 — A plain `ShellRoute`.**
The `builder` receives the current child and wraps it in your shell widget.

```dart
final router = GoRouter(
  initialLocation: '/home',
  routes: [
    ShellRoute(
      builder: (context, state, child) => ScaffoldWithNav(child: child),
      routes: [
        GoRoute(path: '/home', builder: (_, __) => const HomeScreen()),
        GoRoute(path: '/search', builder: (_, __) => const SearchScreen()),
        GoRoute(path: '/profile', builder: (_, __) => const ProfileScreen()),
      ],
    ),
    // routes OUTSIDE the shell have NO bottom bar (good for login)
    GoRoute(path: '/login', builder: (_, __) => const LoginScreen()),
  ],
);
```

**Step 3 — The weakness of a plain `ShellRoute`.**
A plain `ShellRoute` keeps a *single* navigation stack. So if you scroll down in Home, switch to Search, then come back, Home is reset. Each tab does not remember its own state or its own deeper screens.

**Step 4 — `StatefulShellRoute.indexedStack`: a separate stack per tab.**
This gives each tab its own branch with its own `Navigator`. Tabs stay alive in an `IndexedStack`, so scroll position and history are preserved. You switch tabs with `navigationShell.goBranch(index)`.

```dart
StatefulShellRoute.indexedStack(
  builder: (context, state, navigationShell) {
    return Scaffold(
      body: navigationShell, // shows the active branch
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: navigationShell.currentIndex,
        onTap: (index) => navigationShell.goBranch(
          index,
          // tapping the active tab again resets it to its root
          initialLocation: index == navigationShell.currentIndex,
        ),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  },
  branches: [
    StatefulShellBranch(routes: [
      GoRoute(
        path: '/home',
        builder: (_, __) => const HomeScreen(),
        routes: [
          GoRoute(
            path: 'detail/:id',
            builder: (_, state) => HomeDetailScreen(id: state.pathParameters['id']!),
          ),
        ],
      ),
    ]),
    StatefulShellBranch(routes: [
      GoRoute(path: '/search', builder: (_, __) => const SearchScreen()),
    ]),
    StatefulShellBranch(routes: [
      GoRoute(path: '/profile', builder: (_, __) => const ProfileScreen()),
    ]),
  ],
);
```

**Step 5 — Which to choose.**
- **Plain `ShellRoute`** → one shared stack. Fine when tabs don't need to remember their own deep state.
- **`StatefulShellRoute.indexedStack`** → independent stacks per tab. Use this for the classic Instagram/YouTube-style bottom nav, where each tab keeps its history and scroll.

**Why interviewers ask:** Almost every production app has a bottom nav bar. They want to see you know the difference between a shared shell and per-tab state preservation.

**Common mistake:** Using a plain `ShellRoute` when you need per-tab memory, then wondering why Home resets after switching tabs. The fix is `StatefulShellRoute.indexedStack`. Another mistake is putting the login route *inside* the shell, which wrongly shows the bottom bar on login.

**Follow-ups they may ask:**
- *"Why `IndexedStack` under the hood?"* → It keeps all tab widgets alive (just hidden), so their state and scroll survive a tab switch. A plain conditional rebuild would destroy them.
- *"How do you reset a tab to its root?"* → Pass `initialLocation: true` to `goBranch` when the tapped tab is already active.

**Related:** [Q16 — nested navigators](#q16) · [Q6 — go_router basics](#q6) · [Q8 — auth guard outside the shell](#q8)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What is the difference between named routes and typed routes (go_router_builder)?

> Common · Medium

**Short answer (say this):**
"Named routes navigate with a string name plus a map of parameters — simple, but a typo or a missing parameter only fails at runtime. Typed routes use the `go_router_builder` package: you define route classes, run `build_runner`, and get generated, compile-time-safe navigation. Named routes are fine for small apps; typed routes shine in large codebases."

**Let's understand it fully:**

**Step 1 — Named routes: navigate by a string name.**
Give each `GoRoute` a `name`, then navigate with `goNamed`. It's less brittle than raw paths (the path can change without breaking callers), but it's still string-based.

```dart
GoRoute(
  name: 'product',
  path: '/products/:id',
  builder: (context, state) => ProductScreen(id: state.pathParameters['id']!),
);

// navigate — string name, parameters in maps (no compile-time check)
context.goNamed('product', pathParameters: {'id': '42'});
```

**Step 2 — The weakness: errors hide until runtime.**
If you typo `'prodcut'`, or forget the `id` parameter, nothing complains while you code. It breaks when the user taps the button.

```
Named routes:
  context.goNamed('product', pathParameters: {'id': '42'})
  → typo the name or forget 'id'? crashes at RUNTIME

Typed routes:
  const ProductRoute(id: '42').go(context)
  → anything wrong? error at COMPILE time
```

**Step 3 — Typed routes: let the compiler check you.**
With `go_router_builder`, you describe each route as a class annotated with `@TypedGoRoute`. A code generator turns it into type-safe navigation methods.

```dart
// Step 1: define the route as a class
@TypedGoRoute<ProductRoute>(path: '/products/:id')
class ProductRoute extends GoRouteData with _$ProductRoute {
  final String id;
  const ProductRoute({required this.id});

  @override
  Widget build(BuildContext context, GoRouterState state) =>
      ProductScreen(id: id);
}

// Step 2: generate the code
//   dart run build_runner build

// Step 3: navigate — fully type-safe, compiler enforces 'id'
const ProductRoute(id: '42').go(context);
```

**Step 4 — The trade-off (this is the senior answer).**
Typed routes add `build_runner` setup, a generated file, and more boilerplate per route. For a small app that's overkill. For a large team where routes change often and a typo is expensive, the compile-time safety pays off.

**Why interviewers ask:** This tests whether you care about type safety and maintainability, and whether you can weigh a trade-off instead of declaring one approach "always best."

**Common mistake:** Saying typed routes are "better in every way." They cost build_runner overhead and boilerplate; named routes are perfectly fine for small-to-medium projects. The right answer names the trade-off.

**Follow-ups they may ask:**
- *"What does `go_router_builder` generate?"* → Extension methods and route classes that build the correct path and read parameters for you, so navigation is checked at compile time.
- *"Can you mix both?"* → Yes, but pick one style per project for consistency; mixing confuses the team.

**Related:** [Q3 — named routes in Navigator 1.0](#q3) · [Q6 — go_router basics](#q6) · [Q11 — passing arguments](#q11)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. How do you pass arguments between screens? What is the safe (typed) way versus the unsafe way?

> Very common · Medium

**Short answer (say this):**
"The safe way is path and query parameters, because they live in the URL — they survive a web refresh and work with deep links. The unsafe way is go_router's `extra`, which can carry any object but is in-memory only, so it's lost on web refresh and breaks deep links. The safest of all is typed routes, where the compiler enforces the arguments."

**Let's understand it fully:**

**Step 1 — The unsafe way: `extra`.**
`state.extra` is typed `Object?`, so you can pass any object. That feels convenient, but it has three problems: it needs a risky cast, it's not in the URL, and it's held only in memory.

```dart
// passing any object
context.go('/detail', extra: Product(id: 42, name: 'Widget'));

// receiving — must cast, can crash
GoRoute(
  path: '/detail',
  builder: (context, state) {
    final data = state.extra as Product; // crashes if null or wrong type
    return DetailScreen(data: data);
  },
);
// Problems:
//   1. the cast throws if extra is null or the wrong type
//   2. lost on web page refresh (extra is in-memory only)
//   3. not in the URL → deep linking to this screen won't work
```

**Step 2 — The safe way: path and query parameters.**
These are always strings and live in the URL, so they survive refreshes and deep links. Use a path parameter for identity and query parameters for extras.

```dart
context.go('/products/42?name=Widget');

GoRoute(
  path: '/products/:id',
  builder: (context, state) {
    final id = state.pathParameters['id']!;          // always a String
    final name = state.uri.queryParameters['name'];  // nullable String
    return ProductScreen(id: id, name: name);
  },
);
// Survives web refresh and works with deep links.
```

**Step 3 — The safest way: typed routes.**
With `go_router_builder`, arguments become real constructor fields. The compiler forces you to pass the required ones, and fields map to path/query parameters automatically.

```dart
@TypedGoRoute<ProductRoute>(path: '/products/:id')
class ProductRoute extends GoRouteData with _$ProductRoute {
  final String id;
  final String? name; // becomes a query parameter automatically
  const ProductRoute({required this.id, this.name});

  @override
  Widget build(BuildContext context, GoRouterState state) =>
      ProductScreen(id: id, name: name);
}

// compiler enforces the required 'id'
const ProductRoute(id: '42', name: 'Widget').go(context);
```

**Step 4 — When is `extra` acceptable?**
Only for mobile-only flows where the object isn't worth serializing and the screen is never deep-linked — for example, passing an already-loaded object to avoid re-fetching. Even then, always guard for `null` (a refresh or deep link can wipe it).

```dart
final data = state.extra as Product?; // nullable cast
if (data == null) return const ProductLoaderScreen(); // re-fetch fallback
```

**Why interviewers ask:** They test two things at once: awareness of type safety and awareness of web compatibility. Relying on `extra` is a classic bug that only appears once the app runs on web.

**Common mistake:** Defaulting to `extra` for everything because it's the easiest, then breaking on web refresh and deep links. Also, casting `extra` non-null and crashing when the user refreshes the page.

**Follow-ups they may ask:**
- *"Why does `extra` break on web?"* → It's stored in memory, not in the URL. A refresh reloads from the URL only, so `extra` is gone.
- *"Path vs query parameter — which for an id?"* → Path parameter for identity (`/products/:id`); query parameters for optional view settings like `?sort=price`.

**Related:** [Q6 — path & query parameters](#q6) · [Q10 — typed routes](#q10) · [Q2 — returning data back](#q2)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. How do you handle 404 / unknown routes in go_router?

> Common · Easy–Medium

**Short answer (say this):**
"go_router has an `errorBuilder` that runs whenever a navigation doesn't match any route — that's the 404 page. So a typo, a stale deep link, or a hand-edited URL on web shows a friendly screen instead of crashing. If I don't set one, go_router shows a default red error screen in debug."

**Let's understand it fully:**

**Step 1 — Why unknown routes happen.**
On web, users can type any URL. On mobile, an old marketing link or push notification might point to a screen you removed. Without handling, that path matches nothing.

**Step 2 — `errorBuilder`: your 404 screen.**
Set `errorBuilder` on the `GoRouter`. It runs for any unmatched path and gets the attempted location, so you can show a helpful message and a "go home" button.

```dart
final router = GoRouter(
  routes: [ /* ... your routes ... */ ],

  // called for ANY unmatched route
  errorBuilder: (context, state) => Scaffold(
    appBar: AppBar(title: const Text('Page not found')),
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text('404', style: TextStyle(fontSize: 64, fontWeight: FontWeight.bold)),
          const SizedBox(height: 12),
          Text('No route for: ${state.uri}'),
          const SizedBox(height: 24),
          ElevatedButton(
            onPressed: () => context.go('/'),
            child: const Text('Go home'),
          ),
        ],
      ),
    ),
  ),
);
```

**Step 3 — Or redirect old paths to new ones.**
Sometimes you don't want a 404 — you want to forward an old URL to its new home. Do that in `redirect` (which runs for *matched* routes and pattern checks), not in `errorBuilder`.

```dart
redirect: (context, state) {
  if (state.matchedLocation.startsWith('/old-products')) {
    return '/products'; // forward the renamed path
  }
  return null;
},
```

**Step 4 — `errorBuilder` vs `redirect` (don't mix them up).**
- **`redirect`** → runs for routes you *do* understand (auth guards, renamed paths). It decides where to send the user.
- **`errorBuilder`** → runs only for routes that match *nothing*. It shows the 404.

**Why interviewers ask:** Handling unknown routes gracefully is a production requirement, especially on web. They want to see you think about edge cases instead of leaving a raw error screen.

**Common mistake:** Not setting an `errorBuilder` at all, so users hit the default debug error screen. Also, confusing `errorBuilder` (unmatched routes) with `redirect` (matched routes).

**Follow-ups they may ask:**
- *"`errorBuilder` vs `errorPageBuilder`?"* → `errorBuilder` returns a widget (go_router wraps it in a page). `errorPageBuilder` lets you return a custom `Page` for a custom transition.
- *"Where do you forward renamed URLs?"* → In `redirect`, not `errorBuilder` — the path still "matches" a pattern you choose to handle.

**Related:** [Q8 — redirect for auth](#q8) · [Q6 — go_router basics](#q6) · [Q3 — onUnknownRoute in Navigator 1.0](#q3)

[↑ Back to top](#toc)

---

# D. Real-world navigation problems

---

<a id="q13"></a>
## 13. What is deep linking? How do you configure it for Android and iOS with go_router?

> Common · Medium

**Short answer (say this):**
"A deep link lets something outside the app — a browser URL, a push notification, another app — open the app straight to a specific screen instead of the home screen. go_router handles the in-app part for free once the URL arrives. The real work is the platform setup: App Links on Android and Universal Links on iOS, both backed by a verification file on your domain."

**Let's understand it fully:**

**Step 1 — What deep linking does.**
Normally tapping `https://myapp.com/products/42` opens a browser. With deep linking set up, the OS sends that URL straight into your installed app, and go_router builds the correct stack (Home → Products → Product 42).

```
User taps https://myapp.com/products/42
          │
          ▼
   OS checks the link
   app installed?  ── no ──►  open in browser
          │ yes
          ▼
   OS hands '/products/42' to your app
          │
          ▼
   go_router builds the matching page stack
```

**Step 2 — The go_router side: nothing extra.**
Your existing route tree already handles the path. go_router receives the incoming URL like any other navigation.

```dart
GoRoute(
  path: 'products/:productId',
  builder: (context, state) =>
      ProductDetailScreen(id: state.pathParameters['productId']!),
);
```

**Step 3 — Android: App Links.**
Add an intent filter to the `<activity>` in `android/app/src/main/AndroidManifest.xml`. `autoVerify="true"` tells Android to verify your domain so links open the app directly.

```xml
<activity ...>
  <intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https" android:host="myapp.com" />
  </intent-filter>
</activity>
```

Then host a `assetlinks.json` file at `https://myapp.com/.well-known/assetlinks.json` containing your app's package name and SHA-256 signing fingerprint. This is how Android proves the link belongs to your app.

**Step 4 — iOS: Universal Links.**
Add an associated domain in `ios/Runner/Runner.entitlements`:

```xml
<key>com.apple.developer.associated-domains</key>
<array>
  <string>applinks:myapp.com</string>
</array>
```

Then host an `apple-app-site-association` (AASA) file at `https://myapp.com/.well-known/apple-app-site-association`, listing your app ID and the paths it handles:

```json
{
  "applinks": {
    "details": [
      { "appID": "TEAMID.com.example.myapp", "paths": ["/products/*", "/settings"] }
    ]
  }
}
```

**Step 5 — `https` links vs custom schemes.**
A custom scheme like `myapp://product/42` is easy but unverified and won't open from a normal web page or email. Verified `https` App Links / Universal Links are the production choice because they're trusted and work from browsers.

**Why interviewers ask:** Deep linking is a must for marketing campaigns, push notifications, and web-to-app flows. They want to see you can configure both platforms, not just the Dart side.

**Common mistake:** Thinking go_router alone is enough and forgetting the platform files (AndroidManifest + assetlinks.json, entitlements + AASA). Another is mixing up custom schemes (`myapp://`) with verified `https` links — custom schemes skip verification and don't work from browsers.

**Follow-ups they may ask:**
- *"What does `autoVerify` / the AASA file actually do?"* → They let the OS confirm you really own the domain, so the link opens your app directly without a chooser dialog.
- *"How do you test a deep link locally?"* → Use `adb shell am start -a android.intent.action.VIEW -d "https://myapp.com/products/42"` on Android, or `xcrun simctl openurl booted "https://myapp.com/products/42"` on iOS Simulator.

**Related:** [Q4 — why declarative routing handles deep links](#q4) · [Q6 — go_router routes](#q6) · [Q8 — redirect runs on deep links too](#q8)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. How does `PopScope` work? How do you intercept the back button?

> Very common · Medium

**Short answer (say this):**
"`PopScope` wraps a screen and decides whether it can be popped, catching the Android back button, the iOS back swipe, and `Navigator.pop`. I set `canPop: false` to block the pop, and in `onPopInvokedWithResult` I show a confirm dialog and pop manually if the user agrees. It replaced the old, deprecated `WillPopScope`."

**Let's understand it fully:**

**Step 1 — Why intercept back at all.**
Imagine a form with unsaved changes. If the user accidentally hits back, their work is lost. `PopScope` lets you stop that and ask "Discard changes?" first.

**Step 2 — The two key parts.**
- `canPop` — a bool. `false` means "don't let system gestures or the back button pop this screen."
- `onPopInvokedWithResult` — a callback that fires when a pop is attempted. It tells you whether the pop actually happened (`didPop`).

**Step 3 — The full flow.**
When `canPop` is `false` and the user presses back, the pop is *blocked*, so `didPop` is `false` — that's your cue to show the dialog. If the user confirms, you pop manually.

```dart
class EditFormScreen extends StatefulWidget {
  const EditFormScreen({super.key});
  @override
  State<EditFormScreen> createState() => _EditFormScreenState();
}

class _EditFormScreenState extends State<EditFormScreen> {
  bool _hasUnsavedChanges = false;

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: !_hasUnsavedChanges, // block back when there are unsaved changes
      onPopInvokedWithResult: (bool didPop, Object? result) async {
        if (didPop) return; // pop already happened (canPop was true) → nothing to do

        // pop was blocked → ask the user
        final leave = await showDialog<bool>(
          context: context,
          builder: (_) => AlertDialog(
            title: const Text('Discard changes?'),
            content: const Text('You have unsaved changes.'),
            actions: [
              TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Stay')),
              TextButton(onPressed: () => Navigator.pop(context, true), child: const Text('Discard')),
            ],
          ),
        );
        if (leave == true && context.mounted) {
          Navigator.pop(context); // do the pop ourselves after confirmation
        }
      },
      child: Scaffold(
        appBar: AppBar(title: const Text('Edit form')),
        body: TextField(
          onChanged: (_) => setState(() => _hasUnsavedChanges = true),
        ),
      ),
    );
  }
}
```

**Step 4 — Why `WillPopScope` is gone.**
The old `WillPopScope` returned a `Future<bool>` to allow or block the pop. That model didn't fit Android's predictive back gesture (the peek animation as you swipe). `PopScope` decides up front via `canPop`, which works with predictive back. So always use `PopScope` now.

**Why interviewers ask:** This is extremely common in forms, checkout flows, and editors. They check that you know the modern API (`PopScope`, not `WillPopScope`) and that you read `didPop` correctly.

**Common mistake:** Still using `WillPopScope` (deprecated). And a subtle one: getting `didPop` backwards. When `canPop` is `false`, `didPop` is `false` in the callback — that's exactly when you show the dialog. If `didPop` is `true`, the pop already happened, so don't pop again.

**Follow-ups they may ask:**
- *"Why not just always set `canPop: false`?"* → Then the screen can never close by gesture, which breaks predictive back. Set `canPop` to reflect real state (e.g. `!hasUnsavedChanges`).
- *"Does this work with go_router?"* → Yes, `PopScope` works the same; the manual pop can be `context.pop()` instead of `Navigator.pop`.

**Related:** [Q1 — maybePop and the back button](#q1) · [Q2 — returning a result on pop](#q2)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. How do you navigate from outside the widget tree — for example, from a Cubit, service, or repository?

> Common · Medium

**Short answer (say this):**
"The problem is that `context.go()` needs a `BuildContext`, which doesn't exist in a Cubit or service. The cleanest answer is reactive: the Cubit emits a state, and a `BlocListener` in the UI does the navigation. If I really need to navigate without context, I keep a reference to the `GoRouter` (or a global navigator key) and call it directly. I never store a `BuildContext` in a Cubit."

**Let's understand it fully:**

**Step 1 — Why this is tricky.**
Navigation needs a `context`, but business logic (Cubits, services) lives outside the widget tree and has none. So you bridge the two without leaking the UI into your logic.

**Step 2 — Approach 1 (preferred): the UI reacts to state.**
Keep navigation in the widget tree where it belongs. The Cubit just emits a state; a `BlocListener` watches and navigates. This keeps business logic free of navigation.

```dart
// in the Cubit — no navigation, just state
class PaymentCubit extends Cubit<PaymentState> {
  PaymentCubit() : super(PaymentInitial());
  Future<void> pay() async {
    // ... process payment ...
    emit(PaymentSuccess()); // just announce success
  }
}

// in the widget — the UI decides navigation
BlocListener<PaymentCubit, PaymentState>(
  listener: (context, state) {
    if (state is PaymentSuccess) context.go('/success');
  },
  child: const PaymentForm(),
);
```

**Step 3 — Approach 2: keep a reference to the router.**
Sometimes reacting in the UI is awkward (e.g. a deep service-layer event). Then hold the `GoRouter` instance — often via a service locator like `get_it` — and call it directly. The router does not need a context.

```dart
// register once
final getIt = GetIt.instance;
getIt.registerSingleton<GoRouter>(router);

// call from anywhere — no BuildContext needed
getIt<GoRouter>().go('/success');
```

**Step 4 — Approach 3: a global navigator key.**
Create a `GlobalKey<NavigatorState>`, give it to go_router, and use it for low-level navigation (and things like dialogs) from outside the tree.

```dart
final rootNavigatorKey = GlobalKey<NavigatorState>();

final router = GoRouter(
  navigatorKey: rootNavigatorKey,
  routes: [ /* ... */ ],
);

// from outside the tree:
rootNavigatorKey.currentContext?.go('/success');
```

**Step 5 — The hard rule: never store `BuildContext`.**
Saving a `context` in a Cubit or service is dangerous — once that widget is disposed, the context is stale, and using it crashes or navigates the wrong place. It also couples your logic to Flutter. Pass the router or use the reactive listener instead.

**Why interviewers ask:** This comes up in every real project. They want to see you respect separation of concerns — ideally business logic doesn't depend on navigation — and that you know the reactive pattern is the cleanest.

**Common mistake:** Storing a `BuildContext` in a Cubit/service. It goes stale when the widget disposes and causes crashes. Also, not realizing the `GoRouter` instance can be called directly without any context.

**Follow-ups they may ask:**
- *"Which approach is cleanest architecturally?"* → The reactive `BlocListener` one — logic emits state, UI navigates. It keeps the two layers separate.
- *"When is the router-reference approach justified?"* → For cross-cutting concerns like a session-expiry handler that must redirect to login from deep in the service layer.

**Related:** [Q8 — auth redirect reacts to state](#q8) · [Q5 — the navigator key in RouterDelegate](#q5)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. When do you need nested navigators? How does a bottom navigation bar use separate navigation stacks?

> Common · Medium–Hard

**Short answer (say this):**
"You need nested navigators when different sections of the app must keep their own history. The classic case is a bottom nav bar: each tab should remember its own stack and scroll, so leaving Home (drilled into a detail) and coming back restores that detail, not the Home root. You build this with one `Navigator` per tab inside an `IndexedStack`, or `StatefulShellRoute.indexedStack` in go_router."

**Let's understand it fully:**

**Step 1 — Why one navigator isn't enough.**
A single navigator has one stack. With a bottom bar, that means switching tabs either resets history or wipes the bar. Each tab really wants its *own* stack.

```
Nested navigators — each tab owns its own stack:

Root navigator
├── Tab 0 navigator (Home)
│   ├── HomeScreen
│   └── HomeDetailScreen   ← user drilled in here
├── Tab 1 navigator (Search)
│   ├── SearchScreen
│   └── SearchResultScreen
└── Tab 2 navigator (Profile)
    └── ProfileScreen

Switching tabs just shows a different navigator.
Each tab remembers its own stack.
```

**Step 2 — The manual way: a Navigator per tab in an `IndexedStack`.**
Give each tab its own `GlobalKey<NavigatorState>` and its own `Navigator`. `IndexedStack` keeps all tabs alive (just hidden), so their state survives switching.

```dart
class MainScreen extends StatefulWidget {
  const MainScreen({super.key});
  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _index = 0;
  final _keys = [
    GlobalKey<NavigatorState>(),
    GlobalKey<NavigatorState>(),
    GlobalKey<NavigatorState>(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(
        index: _index,
        children: [
          _tabNavigator(0, const HomeScreen()),
          _tabNavigator(1, const SearchScreen()),
          _tabNavigator(2, const ProfileScreen()),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _index,
        onTap: (i) {
          if (i == _index) {
            // tapping the active tab again pops it to root
            _keys[i].currentState?.popUntil((r) => r.isFirst);
          } else {
            setState(() => _index = i);
          }
        },
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
        ],
      ),
    );
  }

  Widget _tabNavigator(int i, Widget root) => Navigator(
        key: _keys[i],
        onGenerateRoute: (_) => MaterialPageRoute(builder: (_) => root),
      );
}
```

**Step 3 — The modern way: `StatefulShellRoute.indexedStack`.**
go_router builds the same thing for you. Each branch is its own stack, kept alive in an `IndexedStack`, and you switch with `navigationShell.goBranch`. (See [Q9](#q9) for the full setup.)

```dart
StatefulShellRoute.indexedStack(
  builder: (context, state, navigationShell) => Scaffold(
    body: navigationShell,
    bottomNavigationBar: BottomNavigationBar(
      currentIndex: navigationShell.currentIndex,
      onTap: (i) => navigationShell.goBranch(i),
      items: const [ /* ... */ ],
    ),
  ),
  branches: [
    StatefulShellBranch(routes: [GoRoute(path: '/home', builder: (_, __) => const HomeScreen())]),
    StatefulShellBranch(routes: [GoRoute(path: '/search', builder: (_, __) => const SearchScreen())]),
    StatefulShellBranch(routes: [GoRoute(path: '/profile', builder: (_, __) => const ProfileScreen())]),
  ],
);
```

**Step 4 — Why `IndexedStack` specifically.**
`IndexedStack` builds all children once and just shows one at a time. A plain `Stack` or a conditional (`if index == 0`) would destroy and rebuild tabs on every switch, losing scroll position and history. `IndexedStack` is what preserves them.

**Why interviewers ask:** This is one of the most common UX patterns in mobile (Instagram, YouTube, Twitter all use it). They want to see you understand why a single navigator fails and how per-tab stacks fix it.

**Common mistake:** Using one navigator for everything and losing tab state on switch. Or forgetting `IndexedStack` and using a plain `Stack`, which rebuilds tabs and wipes their state. In go_router, the mistake is using `ShellRoute` instead of `StatefulShellRoute` and wondering why tab state doesn't persist.

**Follow-ups they may ask:**
- *"How do you 'pop to root' when re-tapping the active tab?"* → Call `popUntil((r) => r.isFirst)` on that tab's navigator key (manual), or `goBranch(i, initialLocation: true)` (go_router).
- *"ShellRoute vs StatefulShellRoute?"* → `ShellRoute` shares one stack; `StatefulShellRoute` gives each branch its own stack and keeps state ([Q9](#q9)).

**Related:** [Q9 — shell routes](#q9) · [Q1 — the Navigator stack](#q1)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. How do you create custom page transitions / animations between screens?

> Common · Medium

**Short answer (say this):**
"For Navigator 1.0, I use `PageRouteBuilder` and animate the new screen with the transition's `animation` value — a `SlideTransition` or `FadeTransition`, for example. In go_router, I return a `CustomTransitionPage` from `pageBuilder` instead of `builder`. The key idea is wrapping the child in a transition driven by the route's animation."

**Let's understand it fully:**

**Step 1 — The default transitions.**
By default Flutter uses platform transitions: `MaterialPageRoute` slides up on Android, `CupertinoPageRoute` slides in from the right on iOS. You only customize when you want something different (a fade, a scale, a slide from a specific side).

**Step 2 — Navigator 1.0: `PageRouteBuilder`.**
`PageRouteBuilder` gives you two functions: `pageBuilder` (the screen) and `transitionsBuilder` (how it animates in). The `animation` value goes from 0 to 1 as the route enters.

```dart
Navigator.push(
  context,
  PageRouteBuilder(
    pageBuilder: (context, animation, secondaryAnimation) => const DetailScreen(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      // slide in from the right
      final tween = Tween(begin: const Offset(1, 0), end: Offset.zero)
          .chain(CurveTween(curve: Curves.easeInOut));
      return SlideTransition(position: animation.drive(tween), child: child);
    },
    transitionDuration: const Duration(milliseconds: 300),
  ),
);
```

**Step 3 — go_router: `CustomTransitionPage`.**
In go_router you use `pageBuilder` (not `builder`) and return a `CustomTransitionPage`. The `transitionsBuilder` works the same as above.

```dart
GoRoute(
  path: '/details',
  pageBuilder: (context, state) => CustomTransitionPage(
    key: state.pageKey,
    child: const DetailScreen(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) =>
        FadeTransition(opacity: animation, child: child), // fade in
  ),
);
```

**Step 4 — A shared-element transition: `Hero`.**
For an image or card that should *fly* from one screen to the next, wrap both with a `Hero` using the same `tag`. Flutter animates it between routes automatically — no custom route needed.

```dart
// on the list screen
Hero(tag: 'product-42', child: Image.network(url));
// on the detail screen — same tag
Hero(tag: 'product-42', child: Image.network(url));
```

**Step 5 — Keep transitions short and consistent.**
Use durations around 200–350 ms and the same style across the app. Long or mismatched transitions feel slow and unpolished — a senior keeps them subtle.

**Why interviewers ask:** Custom transitions show you understand routes are widgets driven by an animation, and that you can polish UX without breaking navigation.

**Common mistake:** Using `builder` instead of `pageBuilder` in go_router when you need a custom transition (`builder` always uses the default). Another is forgetting `key: state.pageKey`, which helps go_router track the page correctly across rebuilds.

**Follow-ups they may ask:**
- *"What is `secondaryAnimation`?"* → It animates this screen *out* as the next screen comes in, so you can coordinate the outgoing and incoming pages.
- *"How do you match iOS vs Android default transitions per platform?"* → Use `MaterialPageRoute` / `CupertinoPageRoute`, or `Theme`'s `pageTransitionsTheme` to set per-platform builders globally.

**Related:** [Q1 — MaterialPageRoute](#q1) · [Q12 — errorPageBuilder for custom error transitions](#q12) · [Q6 — go_router routes](#q6)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**Navigator 1.0 vs Navigator 2.0**

| | Navigator 1.0 | Navigator 2.0 |
|---|---|---|
| Style | imperative (push/pop) | declarative (describe the stack) |
| Deep links | manual, fragile | rebuilt from the URL automatically |
| Web URL sync | not built in | URL ↔ stack both ways |
| In practice | fine for simple mobile apps | use go_router on top of it |

**go_router: `go` vs `push` vs `replace`**

| | `go()` | `push()` | `replace()` |
|---|---|---|---|
| Effect | rebuild stack to match URL | add one screen on top | swap the top screen |
| Stack | resets to matched tree | grows by one | size unchanged |
| Use for | normal nav, web, deep links | layered screens | login → home |

**`ShellRoute` vs `StatefulShellRoute`**

| `ShellRoute` | `StatefulShellRoute.indexedStack` |
|---|---|
| one shared stack | one stack per tab |
| tab state is lost on switch | tab state + scroll preserved |
| simple shared shell | classic bottom-nav apps |

**Passing arguments: safe vs unsafe**

| | Path / query params | `extra` |
|---|---|---|
| In the URL? | yes | no (in-memory only) |
| Survives web refresh? | yes | no |
| Deep-link friendly? | yes | no |
| Type | always String | any object (risky cast) |

**`PopScope` vs `WillPopScope`**

| `PopScope` (current) | `WillPopScope` (deprecated) |
|---|---|
| decides via `canPop` up front | returned a `Future<bool>` |
| works with predictive back | breaks predictive back |
| use this | do not use |

## One-line reminders

- **Navigator stack** = a pile of plates; `push` adds, `pop` removes, `pushReplacement` swaps the top. ([Q1](#q1))
- **`push` returns a Future**; `pop(value)` sends data back — and the result can be `null` on back-press. ([Q2](#q2))
- **Navigator 2.0** is declarative: describe the whole stack from state, for deep links and web URLs. ([Q4](#q4))
- **Parser → Delegate → Navigator**; the delegate must call `notifyListeners()`. go_router does all three. ([Q5](#q5))
- **Path params** (`:id`) identify which thing; **query params** (`?sort=`) tune how you see it. ([Q6](#q6))
- **`go()`** rebuilds the stack; **`push()`** adds one screen on top; **`replace()`** swaps the top. ([Q7](#q7))
- **Auth guard:** in `redirect`, allow `/login` to avoid loops, and use `refreshListenable` for logout. ([Q8](#q8))
- **`StatefulShellRoute.indexedStack`** keeps each tab's stack and scroll; plain `ShellRoute` doesn't. ([Q9](#q9))
- **Typed routes** (go_router_builder) catch typos at compile time; named routes fail at runtime. ([Q10](#q10))
- **Use path/query params** (URL-safe) over `extra` (lost on web refresh, breaks deep links). ([Q11](#q11))
- **`errorBuilder`** = 404 for unmatched routes; **`redirect`** = decisions for matched routes. ([Q12](#q12))
- **Deep links** need platform setup: App Links + assetlinks.json (Android), Universal Links + AASA (iOS). ([Q13](#q13))
- **`PopScope`** replaces `WillPopScope`; when blocked, `didPop` is `false` — that's when you confirm. ([Q14](#q14))
- **Never store `BuildContext`** in a Cubit; emit state and let a `BlocListener` navigate. ([Q15](#q15))
- **Each tab needs its own Navigator** inside an `IndexedStack` to keep its history and scroll. ([Q16](#q16))
- **Custom transitions:** `PageRouteBuilder` (Nav 1.0) or `CustomTransitionPage` (go_router); `Hero` for shared elements. ([Q17](#q17))

[↑ Back to top](#toc)
