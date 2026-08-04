# Section 14 — Design Patterns (Gang of Four)

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. All examples in Dart with a real Flutter use case.

---

## How to use this section

Each pattern has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — the problem it solves, how it works (with Dart code), and a real Flutter use case.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected patterns · **Back to top** — return to the index.

Each pattern is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For each pattern, say the *problem it solves* first, then a one-line real example. Naming a pattern is easy; explaining *when* to use it is the senior signal.

---

<a id="toc"></a>

## Table of Contents

**A. Creational patterns** (how objects are made)
1. [Singleton](#q1) · *Very common*
2. [Factory Method](#q2) · *Very common*
3. [Abstract Factory](#q3) · *Common*
4. [Builder](#q4) · *Common*

**B. Structural patterns** (how objects are composed)
5. [Adapter](#q5) · *Common*
6. [Decorator](#q6) · *Common*
7. [Facade](#q7) · *Common*
8. [Proxy](#q8) · *Deeper*
9. [Composite](#q9) · *Common*

**C. Behavioral patterns** (how objects talk and behave)
10. [Observer](#q10) · *Very common*
11. [Strategy](#q11) · *Very common*
12. [Command](#q12) · *Common*
13. [State](#q13) · *Common*
14. [Template Method](#q14) · *Common*
15. [Iterator](#q15) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

Follow these stages. Tick a stage off only when you can give the **short answer** and a real Flutter example, without looking.

**Stage 1 — The must-knows (start here).** Asked most often.
→ [Q1 Singleton](#q1) · [Q2 Factory Method](#q2) · [Q10 Observer](#q10) · [Q11 Strategy](#q11)

**Stage 2 — The other creational & structural.**
→ [Q4 Builder](#q4) · [Q5 Adapter](#q5) · [Q6 Decorator](#q6) · [Q7 Facade](#q7)

**Stage 3 — The rest of behavioral.**
→ [Q12 Command](#q12) · [Q13 State](#q13) · [Q14 Template Method](#q14) · [Q15 Iterator](#q15)

**Stage 4 — The deeper ones.**
→ [Q3 Abstract Factory](#q3) · [Q8 Proxy](#q8) · [Q9 Composite](#q9)

**Short on time (1 hour before the interview)?** Review these six:
[Q1](#q1) · [Q2](#q2) · [Q6](#q6) · [Q10](#q10) · [Q11](#q11) · [Q13](#q13), then read the [Cheat Sheet](#cheatsheet).

---

# A. Creational patterns

---

<a id="q1"></a>
## 1. Singleton

> Very common · Easy–Medium

**Short answer (say this):**
"Singleton makes sure a class has only one instance for the whole app, and gives a single point of access to it. In Dart you use a factory constructor that always returns the same private instance. It's good for shared services like a config store or a service locator."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Some things should exist only once — one app config, one database connection, one logger. Singleton guarantees that, and lets any code reach the same instance.

**Step 2 — How it works in Dart.**

```dart
class AppConfig {
  static final AppConfig _instance = AppConfig._internal(); // the one instance
  AppConfig._internal();                  // private constructor
  factory AppConfig() => _instance;       // always returns the same one

  String baseUrl = 'https://api.example.com';
}

void main() {
  print(identical(AppConfig(), AppConfig())); // true — same object
}
```

**Step 3 — Real Flutter use case.**
`GetIt` (service locator) is itself a singleton, and `SharedPreferences.getInstance()` returns one shared instance. You also see it for an app-wide logger or analytics service.

**A caution on Dart isolates:** a singleton is one-per-isolate. If you spawn another isolate, it gets its own instance (no shared memory).

**Why interviewers ask:** It's the most famous pattern and a quick test of Dart's factory constructor.

**Common mistake:** Overusing singletons for everything (global state), which makes code hard to test and creates hidden dependencies. Prefer injecting dependencies ([DI](#q2)).

**Follow-ups they may ask:**
- *"Is it thread-safe in Dart?"* → Within one isolate, yes — Dart is single-threaded, so `static final` init is safe. Across isolates, each has its own copy.
- *"Why is a global singleton bad for testing?"* → It's hard to replace with a fake; injected dependencies are easier to mock.

**Related:** [Q2 — Factory Method](#q2) · [Q7 — Facade](#q7)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. Factory Method

> Very common · Medium

**Short answer (say this):**
"Factory Method gives a method that decides which object to create and returns it, so the caller doesn't use a constructor directly. It lets you return different subtypes based on input, without the caller knowing the concrete class. In Dart, `factory` constructors and `fromJson` are everyday examples."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Sometimes the exact class to create depends on input or conditions. You don't want callers writing `if/else` to pick a class — you hide that decision behind one method.

**Step 2 — How it works in Dart.**

```dart
abstract class Button {
  void render();
}
class AndroidButton extends Button {
  @override void render() => print('Material button');
}
class IosButton extends Button {
  @override void render() => print('Cupertino button');
}

class ButtonFactory {
  static Button create(String platform) {
    return platform == 'ios' ? IosButton() : AndroidButton(); // decision hidden
  }
}

ButtonFactory.create('ios').render(); // caller doesn't know the concrete class
```

**Step 3 — Real Flutter use case.**
`User.fromJson(...)` is a factory method — it decides how to build the object from data and could return a subtype. Returning platform-specific widgets (Material vs Cupertino) is another.

**Why interviewers ask:** It's everywhere in Dart (`factory`, `fromJson`) and tests whether you can hide object creation.

**Common mistake:** Confusing it with Abstract Factory. Factory Method makes *one* product; Abstract Factory makes *families* of related products ([Q3](#q3)).

**Follow-ups they may ask:**
- *"Factory method vs constructor?"* → A constructor always makes that class; a factory method can return a subtype, a cached object, or decide at runtime.

**Related:** [Q3 — Abstract Factory](#q3) · [Q1 — Singleton](#q1) · [Q4 — Builder](#q4)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. Abstract Factory

> Common · Medium–Hard

**Short answer (say this):**
"Abstract Factory creates whole *families* of related objects that are meant to be used together, without naming their concrete classes. A classic example is a UI kit: a light-theme factory makes light buttons and light text fields, while a dark-theme factory makes the dark versions — and they always match."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
When you have several related products that must match (all light-themed, or all iOS-styled), you don't want to pick each one separately and risk mixing them. One factory produces a matching set.

**Step 2 — How it works in Dart.**

```dart
abstract class Button {}
abstract class Checkbox {}

abstract class UIFactory {            // the abstract factory
  Button createButton();
  Checkbox createCheckbox();
}

class LightFactory implements UIFactory {
  @override Button createButton() => LightButton();
  @override Checkbox createCheckbox() => LightCheckbox();
}
class DarkFactory implements UIFactory {
  @override Button createButton() => DarkButton();
  @override Checkbox createCheckbox() => DarkCheckbox();
}

class LightButton implements Button {}
class LightCheckbox implements Checkbox {}
class DarkButton implements Button {}
class DarkCheckbox implements Checkbox {}

void buildUI(UIFactory factory) {
  factory.createButton();   // always matches...
  factory.createCheckbox(); // ...the same theme
}
```

**Step 3 — Real Flutter use case.**
Theming systems and adaptive UI kits: one factory per theme/platform produces a coordinated set of widgets, so you never mix a light button with a dark checkbox.

**Why interviewers ask:** It tests the difference between making one object (Factory Method) and a coordinated family (Abstract Factory).

**Common mistake:** Using it when a simple Factory Method would do. Abstract Factory is for *families* of products; don't add the complexity for a single product.

**Follow-ups they may ask:**
- *"Factory Method vs Abstract Factory?"* → Factory Method = one product via a method; Abstract Factory = a set of related products via an object with several methods.

**Related:** [Q2 — Factory Method](#q2) · [Q4 — Builder](#q4)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. Builder

> Common · Medium

**Short answer (say this):**
"Builder constructs a complex object step by step, instead of one huge constructor with many parameters. You set the parts you want, then call build. It's great when an object has many optional fields. Dart's cascade operator and named parameters often replace the classic Builder."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
A constructor with 10 parameters (many optional) is hard to read and error-prone. Builder lets you set only the parts you need, in a readable way, then produce the final object.

**Step 2 — How it works in Dart.**

```dart
class Pizza {
  final String size;
  final List<String> toppings;
  Pizza(this.size, this.toppings);
}

class PizzaBuilder {
  String _size = 'medium';
  final List<String> _toppings = [];

  PizzaBuilder setSize(String s) { _size = s; return this; }  // returns this → chainable
  PizzaBuilder addTopping(String t) { _toppings.add(t); return this; }
  Pizza build() => Pizza(_size, _toppings);
}

final pizza = PizzaBuilder()
    .setSize('large')
    .addTopping('cheese')
    .addTopping('mushroom')
    .build();
```

**Step 3 — Real Flutter use case.**
Flutter's named parameters already give a builder-like experience (`Container(padding: ..., color: ...)`). The cascade `..` also builds objects step by step (`Paint()..color = ...`). Classic builders appear in query builders and notification builders.

**Why interviewers ask:** It tests how you handle objects with many optional parts, and whether you know Dart's idiomatic alternatives.

**Common mistake:** Writing a verbose Builder class when Dart's named/optional parameters or cascades already solve it more simply.

**Follow-ups they may ask:**
- *"How does Dart replace Builder?"* → Named parameters for optional config, and cascades (`..`) for step-by-step setup.

**Related:** [Q2 — Factory Method](#q2) · [Q3 — Abstract Factory](#q3)

[↑ Back to top](#toc)

---

# B. Structural patterns

---

<a id="q5"></a>
## 5. Adapter

> Common · Medium

**Short answer (say this):**
"Adapter lets two incompatible interfaces work together by wrapping one so it looks like the other. It's like a travel plug adapter. You use it to fit a third-party library or legacy class into the interface your app expects, without changing either side."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Your app expects a certain interface, but a library gives a different one. Instead of rewriting your code or the library, you put an adapter in between that translates.

**Step 2 — How it works in Dart.**

```dart
// What your app expects:
abstract class PaymentProcessor {
  void pay(double amount);
}

// A third-party class with a different method name:
class StripeApi {
  void makePayment(int cents) => print('Stripe charged $cents cents');
}

// The adapter translates between them:
class StripeAdapter implements PaymentProcessor {
  final StripeApi stripe;
  StripeAdapter(this.stripe);
  @override
  void pay(double amount) => stripe.makePayment((amount * 100).round());
}

void checkout(PaymentProcessor p) => p.pay(9.99); // app code stays clean
checkout(StripeAdapter(StripeApi()));
```

**Step 3 — Real Flutter use case.**
Wrapping a third-party SDK (payments, analytics, a database) behind your own interface, so you can swap providers later without touching app code. This is also how you keep the Data layer's external types out of your Domain.

**Why interviewers ask:** It's the practical pattern for integrating external code cleanly and keeping your app decoupled from vendors.

**Common mistake:** Confusing Adapter with Facade. Adapter *changes* an interface to match what you need; Facade *simplifies* a complex set of classes ([Q7](#q7)).

**Follow-ups they may ask:**
- *"How does this help if you switch vendors?"* → Only the adapter changes; the rest of the app, which depends on your interface, stays the same.

**Related:** [Q7 — Facade](#q7) · [Q6 — Decorator](#q6)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. Decorator

> Common · Medium

**Short answer (say this):**
"Decorator adds behaviour to an object by wrapping it in another object with the same interface, instead of subclassing. Think of adding toppings to a coffee. Flutter is built on this idea — you wrap a widget in Padding, then Center, then a GestureDetector, each adding a feature."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
You want to add features to objects flexibly, in different combinations, without creating a subclass for every combination. Wrapping lets you stack features.

**Step 2 — How it works in Dart.**

```dart
abstract class Coffee {
  double cost();
  String description();
}
class PlainCoffee implements Coffee {
  @override double cost() => 2.0;
  @override String description() => 'coffee';
}

// A decorator wraps a Coffee and adds to it
class MilkDecorator implements Coffee {
  final Coffee inner;
  MilkDecorator(this.inner);
  @override double cost() => inner.cost() + 0.5;
  @override String description() => '${inner.description()} + milk';
}

Coffee order = MilkDecorator(MilkDecorator(PlainCoffee()));
print(order.description()); // coffee + milk + milk
print(order.cost());        // 3.0
```

**Step 3 — Real Flutter use case.**
The entire widget tree is decorator-style: `GestureDetector(child: Padding(child: Center(child: Text('Hi'))))`. Each wrapper adds one feature (tap handling, spacing, alignment) without subclassing `Text`.

**Why interviewers ask:** It's the pattern that explains Flutter's "everything wraps everything" composition model.

**Common mistake:** Confusing it with inheritance. Decorator wraps at runtime (flexible combinations); subclassing fixes behaviour at compile time.

**Follow-ups they may ask:**
- *"How is Flutter a decorator example?"* → Wrapping widgets (Padding, Center, Opacity) adds behaviour without subclassing the inner widget.

**Related:** [Q9 — Composite](#q9) · [Q5 — Adapter](#q5)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. Facade

> Common · Easy–Medium

**Short answer (say this):**
"Facade gives one simple interface in front of a complex set of classes, so callers don't deal with the messy details. It's like a hotel reception desk that handles everything for you. You use it to wrap several subsystems behind one easy method."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
A task might need several classes working together (auth, network, cache, parsing). Forcing every caller to wire them up is error-prone. A facade hides that behind one clean call.

**Step 2 — How it works in Dart.**

```dart
// Complex subsystems
class AuthService { String token() => 'abc'; }
class ApiService { String fetch(String token) => 'data'; }
class CacheService { void save(String data) {} }

// Facade — one simple entry point
class UserFacade {
  final _auth = AuthService();
  final _api = ApiService();
  final _cache = CacheService();

  String getUserData() {                 // one easy method
    final token = _auth.token();
    final data = _api.fetch(token);
    _cache.save(data);
    return data;
  }
}

UserFacade().getUserData(); // caller ignores all the inner steps
```

**Step 3 — Real Flutter use case.**
A repository is often a facade over several data sources (API + cache + database), exposing one `getUser()`. A "service" class wrapping multiple plugins (location + permissions + maps) is another.

**Why interviewers ask:** It tests whether you can hide complexity behind a simple, stable interface.

**Common mistake:** Confusing it with Adapter. Facade *simplifies* many classes into one interface; Adapter *converts* one interface to another ([Q5](#q5)).

**Follow-ups they may ask:**
- *"Facade vs Repository?"* → A repository is a facade specialized for data access, also hiding the data source.

**Related:** [Q5 — Adapter](#q5) · [Q1 — Singleton](#q1)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. Proxy

> Deeper · Medium–Hard

**Short answer (say this):**
"A proxy is a stand-in object that controls access to a real object — same interface, but it adds something before or after, like caching, lazy loading, or access checks. Think of a receptionist who decides whether to let you reach the manager. A lazy-loading image placeholder is a common proxy."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Sometimes you don't want to use the real object directly — maybe it's expensive to create, needs caching, or needs permission checks. A proxy wraps it and adds that control while looking identical to the real thing.

**Step 2 — How it works in Dart.**

```dart
abstract class Image {
  void display();
}
class RealImage implements Image {
  final String file;
  RealImage(this.file) { print('loading $file from disk'); } // expensive
  @override void display() => print('showing $file');
}

// Proxy delays the expensive load until it's actually needed (lazy loading)
class ImageProxy implements Image {
  final String file;
  RealImage? _real;
  ImageProxy(this.file);
  @override
  void display() {
    _real ??= RealImage(file); // create the real one only on first display
    _real!.display();
  }
}

final img = ImageProxy('photo.png'); // not loaded yet
img.display();                        // now it loads, then shows
```

**Step 3 — Real Flutter use case.**
Lazy-loading images (load only when scrolled into view), a caching proxy that returns cached data before hitting the network, or an access-control proxy that checks auth before a call.

**Why interviewers ask:** It's a deeper structural pattern that tests whether you can add cross-cutting control (caching, lazy load) transparently.

**Common mistake:** Confusing it with Decorator. Both wrap and share the interface, but Proxy *controls access* to the real object; Decorator *adds behaviour/features*.

**Follow-ups they may ask:**
- *"Types of proxy?"* → Virtual (lazy load), caching, protection (access control), remote (stands in for a remote object).

**Related:** [Q6 — Decorator](#q6) · [Q7 — Facade](#q7)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. Composite

> Common · Medium

**Short answer (say this):**
"Composite lets you treat a single object and a group of objects the same way, by giving them a common interface. Think of folders that can hold files *and* other folders. Flutter's widget tree is exactly this — a widget can be a leaf or contain other widgets, and you treat them uniformly."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
When you have a tree of objects (a part-whole hierarchy), you don't want different code for "single item" vs "group." Composite gives both the same interface, so client code is simple.

**Step 2 — How it works in Dart.**

```dart
abstract class FileSystemItem {
  int size();
}
class FileItem implements FileSystemItem {       // leaf
  final int bytes;
  FileItem(this.bytes);
  @override int size() => bytes;
}
class Folder implements FileSystemItem {          // composite
  final List<FileSystemItem> children = [];
  @override int size() => children.fold(0, (sum, c) => sum + c.size());
}

final root = Folder()
  ..children.add(FileItem(100))
  ..children.add(Folder()..children.add(FileItem(50)));
print(root.size()); // 150 — same size() call works for files and folders
```

**Step 3 — Real Flutter use case.**
The widget tree: a `Column` (composite) holds children that may be leaves (`Text`) or more composites (`Row`, `Column`). You build and traverse them uniformly. Menus and nested comment threads are other examples.

**Why interviewers ask:** It explains tree structures like the widget tree and tests uniform handling of part and whole.

**Common mistake:** Writing separate logic for single items vs groups instead of giving them one shared interface.

**Follow-ups they may ask:**
- *"How is Flutter's widget tree composite?"* → A parent widget treats each child the same, whether it's a single widget or a subtree.

**Related:** [Q6 — Decorator](#q6) · [Q15 — Iterator (traversing trees)](#q15)

[↑ Back to top](#toc)

---

# C. Behavioral patterns

---

<a id="q10"></a>
## 10. Observer

> Very common · Medium

**Short answer (say this):**
"Observer lets many objects subscribe to a subject and get notified automatically when it changes. It's like a newspaper subscription — publish once, all subscribers get it. Flutter uses this everywhere: `ChangeNotifier`/`Listenable`, `ValueNotifier`, and Streams are all Observer."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
When one object changes, several others need to react — but you don't want the subject to know each one directly. Observers subscribe; the subject just notifies "something changed."

**Step 2 — How it works in Dart.**

```dart
class Subject {
  final List<void Function(int)> _listeners = [];
  int _value = 0;

  void subscribe(void Function(int) listener) => _listeners.add(listener);

  set value(int v) {
    _value = v;
    for (final l in _listeners) l(v); // notify everyone
  }
}

final s = Subject();
s.subscribe((v) => print('A saw $v'));
s.subscribe((v) => print('B saw $v'));
s.value = 5; // both A and B are notified
```

**Step 3 — Real Flutter use case.**
`ChangeNotifier` + `notifyListeners()` (used by Provider) is Observer. `ValueNotifier`/`ValueListenableBuilder`, and Dart `Stream`s with `listen`, are all Observer — widgets subscribe and rebuild when data changes.

**Why interviewers ask:** It's the backbone of Flutter's reactive state management. Knowing it explains how `setState`-free rebuilds work.

**Common mistake:** Forgetting to unsubscribe (remove listeners / cancel stream subscriptions) in `dispose()`, causing memory leaks.

**Follow-ups they may ask:**
- *"Where is Observer in Flutter?"* → ChangeNotifier, ValueNotifier, Streams, and any `Listenable`.
- *"Push vs pull?"* → Observer usually pushes the change to subscribers.

**Related:** [Q11 — Strategy](#q11) · [Q13 — State](#q13)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. Strategy

> Very common · Medium

**Short answer (say this):**
"Strategy lets you swap an algorithm at runtime by putting each option behind a common interface. Instead of a big if/else choosing behaviour, you inject the strategy you want. Examples: different sorting methods, validation rules, or payment options."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
You have several ways to do one thing (sort, validate, pay) and want to pick or change at runtime — without a giant conditional and without editing the class each time you add a new option.

**Step 2 — How it works in Dart.**

```dart
abstract class PaymentStrategy {
  void pay(double amount);
}
class CardPayment implements PaymentStrategy {
  @override void pay(double a) => print('paid \$a by card');
}
class BkashPayment implements PaymentStrategy {
  @override void pay(double a) => print('paid \$a by bKash');
}

class Checkout {
  PaymentStrategy strategy;
  Checkout(this.strategy);
  void process(double amount) => strategy.pay(amount); // delegates to the strategy
}

Checkout(BkashPayment()).process(9.99); // swap strategies freely
```

**Step 3 — Real Flutter use case.**
Swappable repositories (real vs fake), different validation strategies for forms, sorting options in a list, or pluggable pricing rules. It pairs perfectly with dependency injection.

**Why interviewers ask:** It's the clean alternative to growing if/else chains and a favourite for showing open/closed design.

**Common mistake:** Confusing it with State. Strategy is chosen by the *caller* to do a job differently; State changes the object's behaviour as its *internal state* changes ([Q13](#q13)).

**Follow-ups they may ask:**
- *"Strategy vs simple if/else?"* → Strategy lets you add a new option by adding a class (open/closed), no editing of existing code.

**Related:** [Q13 — State](#q13) · [Q2 — Factory Method](#q2) · [Q10 — Observer](#q10)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. Command

> Common · Medium

**Short answer (say this):**
"Command turns a request into an object that holds everything needed to perform it. Because the action is now an object, you can queue it, log it, or undo it. It's like a written order ticket. The classic use is undo/redo."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
You want to treat actions as data — to store, queue, schedule, or undo them. Calling a method directly can't do that; wrapping the action in an object can.

**Step 2 — How it works in Dart.**

```dart
abstract class Command {
  void execute();
  void undo();
}

class AddTextCommand implements Command {
  final StringBuffer doc;
  final String text;
  AddTextCommand(this.doc, this.text);
  @override void execute() => doc.write(text);
  @override void undo() => print('remove "$text"'); // reverse the action
}

// An invoker can keep a history for undo/redo
final history = <Command>[];
void run(Command c) { c.execute(); history.add(c); }
void undoLast() => history.removeLast().undo();
```

**Step 3 — Real Flutter use case.**
Undo/redo in editors, action queues (e.g. offline actions replayed later), and Flutter's own `Intent`/`Action` system for keyboard shortcuts — each shortcut maps to a command-like action object.

**Why interviewers ask:** It's the standard way to implement undo/redo and action history.

**Common mistake:** Implementing undo with ad-hoc flags instead of command objects, which gets messy fast.

**Follow-ups they may ask:**
- *"How does Command enable undo?"* → Each command knows how to reverse itself; keep a stack of executed commands.

**Related:** [Q11 — Strategy](#q11) · [Q5 — Stack (undo history)](section11_data_structure_and_algorithm.md#q5)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. State

> Common · Medium

**Short answer (say this):**
"The State pattern lets an object change its behaviour when its internal state changes, as if it became a different class. Instead of big if/else on a status field, each state is its own object that knows how to behave and what state comes next. A traffic light is the classic example."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
An object behaves differently in different modes (a media player: playing, paused, stopped). Coding this as one class full of `if (status == ...)` gets tangled. The State pattern puts each mode in its own class.

**Step 2 — How it works in Dart.**

```dart
abstract class PlayerState {
  void press(MediaPlayer player);
}
class PlayingState implements PlayerState {
  @override void press(MediaPlayer p) { print('pause'); p.state = PausedState(); }
}
class PausedState implements PlayerState {
  @override void press(MediaPlayer p) { print('play'); p.state = PlayingState(); }
}

class MediaPlayer {
  PlayerState state = PausedState();
  void pressPlayPause() => state.press(this); // behaviour depends on current state
}

final player = MediaPlayer();
player.pressPlayPause(); // play
player.pressPlayPause(); // pause
```

**Step 3 — Real Flutter use case.**
Modeling screen status (loading / loaded / error) — often done with sealed classes and BLoC states, which is the State pattern in spirit. Form wizards and onboarding flows also use it.

**Why interviewers ask:** It tests handling of state machines cleanly, and overlaps with how BLoC/sealed states work.

**Common mistake:** Confusing it with Strategy. State changes behaviour based on the object's *internal* state (and states can switch themselves); Strategy is picked by the *outside* caller ([Q11](#q11)).

**Follow-ups they may ask:**
- *"How does this relate to BLoC?"* → BLoC's sealed states (Loading/Loaded/Error) are a State-pattern-style state machine.

**Related:** [Q11 — Strategy](#q11) · [Q10 — Observer](#q10)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. Template Method

> Common · Medium

**Short answer (say this):**
"Template Method defines the fixed skeleton of an algorithm in a base class, but lets subclasses fill in specific steps. The overall order is locked; only the customizable parts change. It's like a recipe where the steps are fixed but you choose the ingredients."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Several processes share the same overall steps but differ in a few. You want to write the shared skeleton once and let each variant override only the bits that differ.

**Step 2 — How it works in Dart.**

```dart
abstract class DataProcessor {
  // The template method — fixed order, calls overridable steps
  void process() {
    final raw = readData();      // step varies
    final clean = transform(raw); // step varies
    save(clean);                  // shared
  }
  String readData();            // subclass fills this in
  String transform(String raw); // subclass fills this in
  void save(String data) => print('saved: $data'); // shared default
}

class CsvProcessor extends DataProcessor {
  @override String readData() => 'a,b,c';
  @override String transform(String raw) => raw.toUpperCase();
}

CsvProcessor().process(); // runs the fixed skeleton with CSV-specific steps
```

**Step 3 — Real Flutter use case.**
`StatelessWidget`/`StatefulWidget` use a template: the framework controls the lifecycle and calls your `build()` (the step you fill in). Abstract base classes with a fixed flow and overridable hooks are everywhere.

**Why interviewers ask:** It explains how frameworks (including Flutter) give you hook methods while controlling the overall flow.

**Common mistake:** Confusing it with Strategy. Template Method uses *inheritance* (override steps); Strategy uses *composition* (inject a whole algorithm).

**Follow-ups they may ask:**
- *"How is `build()` a template method?"* → The framework runs the render pipeline (fixed) and calls your `build()` at the right moment (your step).

**Related:** [Q11 — Strategy](#q11) · [Q3 — Abstract Factory](#q3)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. Iterator

> Common · Easy–Medium

**Short answer (say this):**
"Iterator gives a standard way to go through the items of a collection one by one, without exposing how the collection stores them. Dart builds this in: anything that is `Iterable` works with `for-in`, `map`, `where`, etc. You can also make your own iterator."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Different collections (list, set, tree) store data differently. Iterator gives one common way to walk through them, so your loop code doesn't depend on the internal storage.

**Step 2 — How it works in Dart (built in).**

```dart
final items = [1, 2, 3];
for (final x in items) print(x); // the iterator is used under the hood

// Custom iterable using a generator (sync*)
Iterable<int> evens(int max) sync* {
  for (var i = 0; i <= max; i += 2) yield i; // produces values on demand
}
for (final e in evens(6)) print(e); // 0, 2, 4, 6
```

Any class can become iterable by implementing `Iterable` (or, more easily, by exposing a `sync*` generator).

**Step 3 — Real Flutter use case.**
Every `for-in` loop, `ListView.builder`'s item access, and chained collection methods (`.map().where().toList()`) rely on Dart's Iterator. You rarely write one by hand because Dart's `Iterable` and generators cover it.

**Why interviewers ask:** It tests whether you understand how Dart's collections and `for-in` actually work.

**Common mistake:** Hand-writing an iterator when a `sync*` generator or Dart's built-in `Iterable` would be far simpler.

**Follow-ups they may ask:**
- *"How do you make a class iterable?"* → Implement `Iterable<T>` (provide an `iterator`), or expose a `sync*` generator method.

**Related:** [Q9 — Composite (traversing)](#q9) · [Q3 (DSA) — Lists](section11_data_structure_and_algorithm.md#q3)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Table first, then one-line reminders.

## All 15 patterns, one line each

| Pattern | Family | One line | Flutter example |
|---|---|---|---|
| Singleton | Creational | only one instance | GetIt, SharedPreferences |
| Factory Method | Creational | a method decides which object to make | `fromJson`, platform widgets |
| Abstract Factory | Creational | makes a matching family of objects | theme/UI kits |
| Builder | Creational | build a complex object step by step | named params, cascades |
| Adapter | Structural | make two interfaces fit | wrap a 3rd-party SDK |
| Decorator | Structural | wrap to add features | Padding/Center around a widget |
| Facade | Structural | one simple front for many classes | repository over API+cache |
| Proxy | Structural | stand-in that controls access | lazy image, caching |
| Composite | Structural | treat one and many the same | the widget tree |
| Observer | Behavioral | subscribers notified on change | ChangeNotifier, Streams |
| Strategy | Behavioral | swap an algorithm at runtime | swappable repos/validators |
| Command | Behavioral | action as an object (undo) | undo/redo, action queue |
| State | Behavioral | behaviour changes with internal state | BLoC states, media player |
| Template Method | Behavioral | fixed skeleton, overridable steps | `build()` hook |
| Iterator | Behavioral | walk a collection uniformly | `for-in`, Iterable |

## Patterns people confuse

- **Factory Method vs Abstract Factory** → one product vs a matching family. ([Q2](#q2), [Q3](#q3))
- **Adapter vs Facade** → convert an interface vs simplify many classes. ([Q5](#q5), [Q7](#q7))
- **Decorator vs Proxy** → add features vs control access. ([Q6](#q6), [Q8](#q8))
- **Strategy vs State** → caller picks the algorithm vs behaviour changes with internal state. ([Q11](#q11), [Q13](#q13))
- **Strategy vs Template Method** → inject an algorithm (composition) vs override steps (inheritance). ([Q11](#q11), [Q14](#q14))

## One-line reminders

- **Creational** = how objects are made (Singleton, Factory, Abstract Factory, Builder).
- **Structural** = how objects are composed (Adapter, Decorator, Facade, Proxy, Composite).
- **Behavioral** = how objects talk and behave (Observer, Strategy, Command, State, Template Method, Iterator).
- **Flutter is decorator + composite** — widgets wrap widgets and form a tree. ([Q6](#q6), [Q9](#q9))
- **Flutter state management is Observer** — ChangeNotifier, ValueNotifier, Streams. ([Q10](#q10))
- Say the **problem each pattern solves** before naming it. That's the senior signal.

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers push from "define it" to "where have you used it." Practice out loud:

1. *"Name a pattern you use in Flutter daily."* → Observer (ChangeNotifier/Streams) and Decorator (wrapping widgets).
2. *"Show Strategy in a real case."* → swappable repositories injected via DI; add a new one without editing existing code.
3. *"Difference between Strategy and State?"* → caller picks Strategy; State switches itself based on internal state.
4. *"How would you build undo/redo?"* → Command objects on a stack, each knowing how to undo itself.
5. *"Isn't this over-engineering?"* → yes if forced; use a pattern only when it solves a real problem (judgment, not memorization).

Explaining *when* and *why* — not just *what* — is exactly what earns a senior signal, in both remote and BD interviews.

[↑ Back to top](#toc)
