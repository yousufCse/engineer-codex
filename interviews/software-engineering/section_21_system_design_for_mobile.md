# Section 21 — System Design for Mobile

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. Designs use plain diagrams and key decisions, not walls of code.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a step-by-step design with a diagram and the key decisions.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** In a design question, **clarify requirements first**, then talk through architecture out loud, naming trade-offs. Interviewers grade your *reasoning and communication*, not a single "correct" diagram.

---

<a id="toc"></a>

## Table of Contents

**A. The framework**
1. [How to approach a mobile system design question](#q1) · *Very common*
2. [REST vs WebSocket for live data](#q2) · *Common*

**B. Design exercises**
3. [Design a real-time chat app](#q3) · *Common*
4. [Design an offline-first feed](#q4) · *Common*
5. [Design an authentication system](#q5) · *Very common*
6. [Design photo upload (chunked, retry, compress)](#q6) · *Common*
7. [Design push notification architecture](#q7) · *Common*
8. [Design a shopping cart](#q8) · *Common*

**C. Architecture at scale**
9. [Design for scalability](#q9) · *Common*
10. [Architect an app with 50+ screens, 10+ devs](#q10) · *Common*
11. [Design a plugin / SDK](#q11) · *Deeper*

**D. Cross-cutting concerns**
12. [API versioning & breaking changes](#q12) · *Common*
13. [App-wide error handling](#q13) · *Very common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The method (start here).**
→ [Q1 The framework](#q1) · [Q2 REST vs WebSocket](#q2)

**Stage 2 — The classic designs.**
→ [Q3 Chat](#q3) · [Q4 Offline feed](#q4) · [Q5 Authentication](#q5)

**Stage 3 — More designs.**
→ [Q6 Photo upload](#q6) · [Q7 Push notifications](#q7) · [Q8 Shopping cart](#q8)

**Stage 4 — Architecture at scale.**
→ [Q9 Scalability](#q9) · [Q10 Large app](#q10) · [Q11 Plugin/SDK](#q11)

**Stage 5 — Cross-cutting.**
→ [Q12 API versioning](#q12) · [Q13 Error handling](#q13)

**Short on time?** Review [Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q13](#q13), then the [Cheat Sheet](#cheatsheet).

---

# A. The framework

---

<a id="q1"></a>
## 1. How do you approach a system design question in a Flutter/mobile context?

> Very common · Medium

**Short answer (say this):**
"I use a simple framework: first clarify the requirements and scope, then sketch the high-level architecture, then dive into the key mobile concerns — data flow, state management, local storage, offline support, and networking. Throughout, I talk through trade-offs out loud. The goal is to show structured thinking, not memorize one right answer."

**Let's understand it fully:**

**Step 1 — Clarify first (don't jump to a solution).**
Ask questions: How many users? Real-time or not? Offline needed? Which platforms? This shows maturity and prevents designing the wrong thing.

**Step 2 — The five-step framework.**

```
1. Requirements   – functional + non-functional (scale, offline, latency)
2. High-level     – app ↔ API ↔ services ↔ database; the big boxes
3. Data flow      – how data moves; state management choice
4. Mobile concerns– local storage, offline/sync, caching, networking
5. Trade-offs     – discuss alternatives and why you chose what you did
```

**Step 3 — Emphasize the *mobile* parts.**
Mobile system design isn't just backend boxes. Spend time on: offline-first, flaky networks, battery/data limits, local caching, and state management on the device. That's what makes it a *mobile* design question.

**Step 4 — Communicate continuously.**
Think out loud, draw boxes, state assumptions, and name trade-offs ("WebSocket gives lower latency but costs a persistent connection"). The interviewer is grading your reasoning and communication.

**Why interviewers ask:** It's the meta-skill — they want to see a structured, requirements-first approach, not a memorized diagram.

**Common mistake:** Jumping straight to a solution without clarifying requirements, or ignoring mobile-specific concerns (offline, flaky network) and treating it like a pure backend question.

**Follow-ups they may ask:**
- *"What's different about mobile vs web design?"* → Offline support, unreliable networks, limited battery/data, local storage, and app lifecycle.

**Related:** [Q2 — REST vs WebSocket](#q2) · [Q3 (SDLC) — HLD vs LLD](section_19_sdlc_interview_prep.md#q3)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What are the trade-offs between REST and WebSocket for live data?

> Common · Medium

**Short answer (say this):**
"REST is request/response — the app asks, the server answers, then the connection closes. It's simple and great for most data. WebSocket keeps a single connection open for two-way, real-time messages — ideal for chat, live scores, or presence. WebSocket gives low latency but costs a persistent connection and more complexity; REST is simpler but can't push updates."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
- **REST** = sending letters: you ask, you wait, you get a reply. One exchange at a time.
- **WebSocket** = a phone call: the line stays open, both sides talk anytime.

**Step 2 — The comparison.**

| | REST | WebSocket |
|---|---|---|
| Style | request/response | persistent, two-way |
| Server push | no (must poll) | yes (instant) |
| Latency | higher | low |
| Complexity | simple | more (reconnect, heartbeat) |
| Best for | most CRUD data | chat, live updates, presence |

**Step 3 — The "in-between" options.**
- **Polling** — REST on a timer (simple, but wasteful and laggy).
- **Long polling / SSE (Server-Sent Events)** — server can push one-way without full WebSocket.
- **WebSocket** — full two-way real-time.

**Step 4 — How to choose.**
Use REST for normal data (profile, orders). Add WebSocket *only* where you need live, low-latency, two-way updates (chat, live tracking). Don't make everything a WebSocket — it adds reconnection and scaling complexity.

**Why interviewers ask:** Picking the right transport is the first decision in many designs (chat, live feeds).

**Common mistake:** Using WebSocket for everything (over-complex) or polling for true real-time needs (laggy, battery-hungry).

**Follow-ups they may ask:**
- *"How do you handle a dropped WebSocket?"* → Auto-reconnect with backoff, heartbeats to detect drops, and re-sync missed messages on reconnect.

**Related:** [Q3 — chat](#q3) · [Q7 — push notifications](#q7) · [Q1 (Networking) — http vs Dio](../flutter/section7_networking_local_storage.md#q1)

[↑ Back to top](#toc)

---

# B. Design exercises

---

<a id="q3"></a>
## 3. Design a real-time chat application in Flutter.

> Common · Hard

**Short answer (say this):**
"I'd use WebSocket for real-time messaging, a BLoC/Cubit to manage the chat state, and a local database (like Drift or Hive) to store messages for offline access and instant loading. Messages are stored locally first (optimistic), sent over the socket, and confirmed by the server. I'd handle reconnection, ordering, and delivery/read receipts."

**Let's understand it fully:**

**Step 1 — Clarify requirements.**
1-to-1 or group? Media support? Read receipts? Offline? Scale? Assume: 1-to-1 + group, text + images, read receipts, offline history.

**Step 2 — High-level architecture.**

```
Flutter app  ── WebSocket ──►  Chat server  ──►  Message DB
   │  (live messages)              │
   │                              push (FCM) for offline users
   └─ Local DB (Drift/Hive): stores messages for offline + instant load
```

**Step 3 — Key decisions.**
- **Transport** — WebSocket for live messages ([Q2](#q2)); REST for history pagination.
- **State** — BLoC/Cubit holds the message list; UI rebuilds on new messages ([Q3 State Mgmt](../flutter/section3_state_management.md#q1)).
- **Local storage** — a local DB stores all messages, so the chat loads instantly and works offline.
- **Optimistic UI** — show the message immediately as "sending", then mark "sent/delivered/read" as the server confirms.

**Step 4 — Handle the hard parts.**
- **Ordering** — use server timestamps/sequence numbers; sort by them, not arrival order.
- **Reconnection** — auto-reconnect with backoff; on reconnect, fetch messages missed while offline.
- **Offline send** — queue messages locally; send when the socket reconnects.
- **Notifications** — when the user is offline, the server sends a **push** ([Q7](#q7)).

**Step 5 — Trade-offs.**
WebSocket gives instant delivery but needs reconnection/heartbeat logic and server resources for many open connections. The local DB adds complexity but is essential for offline and instant load.

**Why interviewers ask:** Chat touches every hard mobile topic — real-time, offline, state, storage, ordering.

**Common mistake:** Forgetting offline/reconnection and message ordering, or skipping local storage (so the chat is blank without network).

**Follow-ups they may ask:**
- *"How do you guarantee message order?"* → Server-assigned sequence numbers/timestamps; sort by those.
- *"Group chat fan-out?"* → The server delivers each message to all members' connections (or queues a push for offline ones).

**Related:** [Q2 — WebSocket](#q2) · [Q4 — offline](#q4) · [Q7 — push](#q7)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. Design an offline-first news feed in Flutter.

> Common · Medium–Hard

**Short answer (say this):**
"Offline-first means the local database is the single source of truth for the UI. The app always reads from local storage (so it works instantly and offline), and a background sync fetches fresh data from the API and updates the local store. The UI just listens to the local DB and rebuilds when it changes."

**Let's understand it fully:**

**Step 1 — The core idea: local DB is the source of truth.**
The UI never waits on the network. It reads from the local database (Drift/Hive). The network's job is to *update* that database in the background.

**Step 2 — Architecture.**

```
UI  ◄── watches ──  Local DB (source of truth)  ◄── sync ──  API
                         ▲
            repository decides: read local first, refresh in background
```

**Step 3 — The flow.**
1. App opens → instantly show cached articles from the local DB.
2. In the background, fetch new articles from the API.
3. Save them to the local DB.
4. The UI is watching the DB (a reactive stream), so it updates automatically.

```dart
// Repository: local-first, then refresh
Stream<List<Article>> watchFeed() => localDb.watchArticles(); // UI binds to this
Future<void> refresh() async {
  final fresh = await api.getArticles();
  await localDb.upsertAll(fresh); // UI updates via the stream
}
```

**Step 4 — Handle the details.**
- **Pagination** — store pages locally; load more appends to the DB.
- **Stale data** — show cached immediately, refresh in background, optionally show a "updated" indicator.
- **Conflict** — for a read-only feed, server wins; for user data, decide a merge strategy.
- **Images** — cache them too (`cached_network_image`).

**Step 5 — Trade-offs.**
Offline-first gives a fast, resilient UX but adds sync complexity and storage. For a feed it's well worth it — users hate blank screens on bad networks.

**Why interviewers ask:** Offline-first is the signature mobile design pattern; it tests data flow and sync thinking.

**Common mistake:** Treating the network as the source of truth (blank screen offline), instead of reading from local storage and syncing in the background.

**Follow-ups they may ask:**
- *"How do you know what's new?"* → Use timestamps/etags or a "since" cursor so you fetch only new items.

**Related:** [Q3 — chat (offline)](#q3) · [Q15 (Networking) — offline-first](../flutter/section7_networking_local_storage.md#q15)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. Design an authentication system in Flutter (login, token storage, refresh, logout).

> Very common · Medium–Hard

**Short answer (say this):**
"The user logs in, the server returns a short-lived access token and a longer-lived refresh token, and I store both in secure storage. Every request carries the access token; when it expires (401), an interceptor uses the refresh token to get a new one and retries. Logout clears the tokens and tells the server to revoke the refresh token."

**Let's understand it fully:**

**Step 1 — The login flow.**

```
User → enter credentials → POST /login
     ← access token (short) + refresh token (long)
App  → store BOTH in secure storage (Keychain/Keystore)
```

**Step 2 — Using the token on requests.**
A Dio interceptor attaches the access token to every request:

```dart
dio.interceptors.add(InterceptorsWrapper(
  onRequest: (options, handler) async {
    final token = await secureStorage.read(key: 'access_token');
    options.headers['Authorization'] = 'Bearer $token';
    handler.next(options);
  },
));
```

**Step 3 — Silent refresh on expiry.**
When a request returns 401, the interceptor refreshes and retries — without bothering the user:

```
request → 401 → use refresh token → get new access token → retry original
       (if refresh also fails → log the user out)
```

Queue concurrent 401s so you refresh once, not many times.

**Step 4 — Logout and security.**
- **Logout** → delete tokens from secure storage AND call the server to revoke the refresh token.
- **Storage** → secure storage only ([Q3 Security](section_20_mobile_app_security.md#q3)); never SharedPreferences.
- **Tokens** → short access + refresh, optionally with rotation ([Q9 Security](section_20_mobile_app_security.md#q9)).
- **Biometric gate** → optionally require biometrics to unlock the stored token on app open.

**Step 5 — Trade-offs.**
Short tokens + refresh add interceptor complexity but greatly reduce the damage of a leaked token. The auto-refresh must handle concurrency (many requests failing 401 at once) carefully.

**Why interviewers ask:** Every app has auth; it tests secure storage, interceptors, and token lifecycle together.

**Common mistake:** Storing tokens insecurely, using one never-expiring token, or not handling the "refresh token also expired" case (must force re-login).

**Follow-ups they may ask:**
- *"Multiple requests get 401 at once?"* → Refresh once, pause other requests, then replay them with the new token.

**Related:** [Q9 (Security) — tokens](section_20_mobile_app_security.md#q9) · [Q3 (Security) — secure storage](section_20_mobile_app_security.md#q3) · [Q3 (Networking) — interceptors](../flutter/section7_networking_local_storage.md#q3)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. Design a photo upload feature (chunked upload, progress, retry, compression).

> Common · Medium–Hard

**Short answer (say this):**
"I'd compress the image first to save bandwidth, then upload it — for large files, in chunks so a failure only re-sends one chunk. I'd show progress from Dio's callback, retry failed chunks with backoff, and run the upload in a way that survives the user navigating away. The server reassembles the chunks."

**Let's understand it fully:**

**Step 1 — Compress before upload.**
A phone photo can be several MB. Compress/resize it first to cut upload time and data usage (e.g. `flutter_image_compress`), respecting quality needs.

**Step 2 — Chunked upload for large files.**
Split the file into chunks and upload each separately. If one fails, you re-send only that chunk, not the whole file.

```
file → [chunk 1][chunk 2][chunk 3] → upload each → server reassembles
       (retry only the failed chunk)
```

**Step 3 — Progress and retry.**

```dart
await dio.post('/upload', data: formData,
  onSendProgress: (sent, total) {
    final percent = sent / total; // drive a progress bar
  },
);
```

- **Progress** — use `onSendProgress` to update the UI.
- **Retry** — on a failed chunk, retry with exponential backoff; give up after N tries and let the user retry.

**Step 4 — Survive app lifecycle.**
Uploads can be slow. Consider a background upload mechanism so it continues if the user leaves the screen, and queue uploads to resume after a network drop. Mark each upload's state (pending/uploading/failed/done) locally.

**Step 5 — Trade-offs.**
Chunking + retry adds complexity but is essential for big files on flaky mobile networks. For small images, a single multipart upload is simpler and fine.

**Why interviewers ask:** It tests handling large data on unreliable networks — a real mobile challenge.

**Common mistake:** Uploading huge uncompressed files in one shot with no progress or retry, so a momentary drop loses the whole upload.

**Follow-ups they may ask:**
- *"How does the server know chunks belong together?"* → An upload/session id sent with each chunk, plus chunk index; the server reassembles by id and order.

**Related:** [Q4 — offline](#q4) · [Q2 — networking](#q2)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. Design push notification architecture end-to-end for a Flutter app.

> Common · Medium

**Short answer (say this):**
"The app registers with FCM (Firebase Cloud Messaging) and gets a device token, which it sends to my backend. When something happens, my backend tells FCM to deliver a notification to that token. The app handles notifications in three states — foreground, background, and terminated — and taps deep-link the user to the right screen."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
Push is like a postal service: it delivers to the user's door even when your app (the shop) is closed. The app gives the postal service its address (device token).

**Step 2 — The end-to-end flow.**

```
App → register with FCM → gets device token
App → send token to your backend (store it per user)
Event → your backend → calls FCM with token + payload → device shows notification
User taps → app opens / deep-links to the right screen
```

**Step 3 — Handle the three app states.**
- **Foreground** — your code shows an in-app banner (you control it).
- **Background** — the OS shows the notification; tapping opens the app.
- **Terminated** — the OS shows it; tapping cold-starts the app; read the launch payload to route correctly.

```dart
FirebaseMessaging.onMessage.listen(handleForeground);
FirebaseMessaging.onMessageOpenedApp.listen(handleTapFromBackground);
final initial = await FirebaseMessaging.instance.getInitialMessage(); // terminated tap
```

**Step 4 — Important details.**
- **Token refresh** — the device token can change; listen for `onTokenRefresh` and update the backend.
- **Permissions** — iOS (and Android 13+) require asking the user; handle denial gracefully.
- **Data vs notification messages** — "notification" messages are shown by the OS; "data" messages let your app decide. Use data messages when you need custom handling.
- **Deep linking** — the payload carries a route so a tap lands on the right screen ([Q15 Security](section_20_mobile_app_security.md#q15)).

**Why interviewers ask:** Push is in almost every app and tests platform/lifecycle understanding.

**Common mistake:** Only handling the foreground case and forgetting background/terminated, or not updating the backend when the device token refreshes (so notifications silently stop).

**Follow-ups they may ask:**
- *"How do you target one user with multiple devices?"* → Store multiple tokens per user; send to all (or use FCM topics/user-based fan-out).

**Related:** [Q3 — chat (offline push)](#q3) · [Q15 (Security) — deep links](section_20_mobile_app_security.md#q15)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. Design a shopping cart feature (state, persistence, backend sync).

> Common · Medium

**Short answer (say this):**
"The cart lives as app state (BLoC/Cubit/Riverpod) for instant UI updates, is persisted locally so it survives app restarts, and syncs to the backend so it follows the user across devices. I'd update locally first (optimistic), then sync, and handle conflicts when the same user changes the cart on two devices."

**Let's understand it fully:**

**Step 1 — Three layers.**

```
UI ◄─ state (Cubit) ◄─ local storage (survives restart) ◄─ backend (cross-device)
```

- **State** — holds the current cart; UI rebuilds on change.
- **Local persistence** — save the cart (Hive/Drift) so it's there after a restart, even offline.
- **Backend sync** — store the cart server-side so it follows the user to another device.

**Step 2 — The update flow (optimistic).**
1. User taps "add to cart" → update the Cubit state instantly (UI reflects it).
2. Save to local storage.
3. Sync to the backend in the background.
4. If the sync fails, keep it locally and retry later (offline-tolerant).

**Step 3 — Handle the tricky parts.**
- **Guest vs logged-in** — keep a local cart for guests; merge it into the server cart on login.
- **Conflicts** — same user edits the cart on two devices. Decide a strategy: last-write-wins, or merge quantities, or server-authoritative.
- **Stock/price changes** — re-validate prices and availability at checkout; don't trust the stored cart blindly.

**Step 4 — Trade-offs.**
Optimistic local-first updates feel instant and work offline, at the cost of sync/conflict handling. A purely server-backed cart is simpler but laggy and breaks offline.

**Why interviewers ask:** The cart combines state, persistence, sync, and conflicts — a compact, realistic design.

**Common mistake:** Keeping the cart only in memory (lost on restart) or only on the server (laggy, broken offline). And forgetting the guest→login merge.

**Follow-ups they may ask:**
- *"Merge guest cart on login?"* → Combine items, summing quantities for duplicates, then push the merged cart to the server.

**Related:** [Q4 — offline-first](#q4) · [Q5 — auth](#q5) · [Q1 (State Mgmt)](../flutter/section3_state_management.md#q1)

[↑ Back to top](#toc)

---

# C. Architecture at scale

---

<a id="q9"></a>
## 9. How do you design for scalability in a mobile app architecture?

> Common · Medium–Hard

**Short answer (say this):**
"Scalability for mobile means two things: the *codebase* scales to more features and developers, and the *app* handles more data/users smoothly. For the code: clean layered architecture, modular feature packages, and dependency injection. For the runtime: pagination, caching, lazy loading, efficient state management, and offloading heavy work to isolates."

**Let's understand it fully:**

**Step 1 — Two kinds of scale.**
- **Codebase scale** — many features and developers without chaos.
- **Runtime scale** — large data and many users without lag.

**Step 2 — Scaling the codebase.**
- **Layered/Clean Architecture** so concerns are separated ([Q2 Architecture](section_13_software_architecture_patterns.md#q2)).
- **Modular feature packages** so teams work in parallel ([Q10](#q10)).
- **Dependency injection** for testability and swapability.
- **Consistent patterns** so new code looks like old code.

**Step 3 — Scaling the runtime (on-device).**
- **Pagination** — never load 10,000 items at once; load pages.
- **Caching** — cache responses/images to cut network and speed up.
- **Lazy loading** — `ListView.builder`, deferred imports, build only what's visible.
- **Efficient state** — rebuild only what changed (selectors, `const`).
- **Isolates** — move heavy parsing/computation off the UI thread.

**Step 4 — Scaling the backend interaction.**
- Efficient APIs (request only needed fields; GraphQL or tailored REST).
- Backpressure/debounce on rapid user actions (search-as-you-type).
- Graceful handling of slow/failed networks.

**Why interviewers ask:** Senior/lead roles need people who design for growth, not just the first version.

**Common mistake:** Designing only for today's small data — loading everything at once, no caching — which falls over as data and users grow.

**Follow-ups they may ask:**
- *"App feels slow with a big list — what do you check?"* → Lazy building (`ListView.builder`), `const`, rebuild scope, image caching, and heavy work on the UI thread.

**Related:** [Q10 — large app](#q10) · [Q5 (Performance)](../flutter/section5_performance_optimization.md#q1) · [Q2 (Architecture)](section_13_software_architecture_patterns.md#q2)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. How would you architect a Flutter app with 50+ screens and 10+ developers?

> Common · Hard

**Short answer (say this):**
"I'd use a modular, feature-based architecture: each feature is its own package with clear boundaries, sharing common 'core' and 'domain' packages, all in a monorepo managed with melos. Inside each feature, Clean Architecture (presentation/domain/data) with DI. This lets teams work in parallel, enforces boundaries, and keeps builds and tests fast per feature."

**Let's understand it fully:**

**Step 1 — The core problem: parallel work without chaos.**
With 10+ developers, one big `lib/` folder becomes a constant source of merge conflicts and tangled dependencies. The solution is strong boundaries.

**Step 2 — Modular feature packages.**

```
app/                  (shell: wires features + navigation)
packages/
  core/               (networking, theming, utils — shared)
  domain/             (shared entities, repository interfaces)
  feature_auth/       feature_profile/   feature_orders/   ...
```

Rule: features depend on `core`/`domain`, **not on each other** ([Q13 Architecture](section_13_software_architecture_patterns.md#q13)).

**Step 3 — Inside each feature.**
Clean Architecture (presentation → domain → data) with DI ([Q2 Architecture](section_13_software_architecture_patterns.md#q2)), and a consistent state management choice across the app (e.g. BLoC) so any developer can read any feature.

**Step 4 — Tooling and process.**
- **melos** to manage the monorepo (link packages, run scripts everywhere).
- **CI** that builds/tests changed packages.
- **Shared standards** — lint rules, conventions, a design system, and clear ownership per feature.
- **Navigation** centralized (e.g. `go_router`) so features don't hard-wire to each other.

**Step 5 — Trade-offs.**
Modularization adds upfront setup and tooling complexity. For a small app it's overkill; for 50+ screens and 10+ devs it's the difference between scaling smoothly and drowning in conflicts.

**Why interviewers ask:** It's a senior/lead question about scaling teams and codebases — judgment and structure.

**Common mistake:** One giant module (everyone conflicts) or features importing each other's internals (recreating the tangle). Also, inconsistent patterns so each feature is written differently.

**Follow-ups they may ask:**
- *"How do features communicate?"* → Through shared abstractions in `core`/`domain` or an event/navigation layer in the app shell — never direct imports.

**Related:** [Q13 (Architecture) — modular](section_13_software_architecture_patterns.md#q13) · [Q12 (Architecture) — monorepo](section_13_software_architecture_patterns.md#q12) · [Q9 — scalability](#q9)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. How do you design a plugin or SDK that other Flutter apps will use?

> Deeper · Hard

**Short answer (say this):**
"An SDK is a product for *developers*, so the priorities are a clean, stable public API, great documentation, and not breaking users. I'd expose a small, well-named surface, hide internals, handle errors gracefully, support null safety and current Flutter versions, and version it with semver so breaking changes are clearly signaled."

**Let's understand it fully:**

**Step 1 — The mindset shift: your users are developers.**
With an app, the user is a person. With an SDK, the user is another developer who will be furious if you break their app. So **stability and clarity** matter above all.

**Step 2 — Design a clean public API.**
- Expose a **small surface** — only what users need; hide internals (`_private` / `src/`).
- **Clear names** and sensible defaults so it's easy to start.
- **Don't leak** third-party types through your API (wrap them), so you can change internals freely.

```dart
// Public, minimal, stable:
class PaymentSdk {
  Future<PaymentResult> pay({required double amount}) async { /* ... */ }
}
// Internals hidden in src/, not exported.
```

**Step 3 — Robustness and compatibility.**
- **Graceful errors** — return typed results/exceptions, never crash the host app.
- **Null safety** and support for current Flutter/Dart versions.
- **Platform support** — handle Android/iOS (and web if relevant) cleanly via platform channels/Pigeon.
- **No surprising side effects** — don't grab global state or assume the host's setup.

**Step 4 — Documentation, versioning, testing.**
- **Docs + examples** — an example app and clear README; SDKs live or die on docs.
- **Semantic versioning** — MAJOR for breaking changes, so users upgrade safely ([Q8 SDLC](section_19_sdlc_interview_prep.md#q8)).
- **Deprecation path** — mark old APIs `@deprecated` with guidance before removing.
- **Thorough tests** — you can't easily hotfix something installed in many apps.

**Why interviewers ask:** It tests API design maturity and empathy for other developers — a senior/staff signal.

**Common mistake:** A huge, leaky public API that exposes internals, so any internal change breaks users. Or no docs/examples, so nobody can adopt it.

**Follow-ups they may ask:**
- *"How do you make a breaking change safely?"* → Deprecate first with a migration path, bump the MAJOR version, and document the upgrade.

**Related:** [Q12 — API versioning](#q12) · [Q5 (Clean Code) — CQS / clean API](section_16_clean_code.md#q5) · [Q11 (OOP) — constructors](section_12_oop_design_principles.md#q18)

[↑ Back to top](#toc)

---

# D. Cross-cutting concerns

---

<a id="q12"></a>
## 12. What is API versioning, and how do you handle breaking API changes in a mobile app?

> Common · Medium

**Short answer (say this):**
"API versioning lets the server evolve without breaking older app versions still on users' phones. You version the API (like `/v1/`, `/v2/`) and keep old versions running until old apps age out. The key mobile constraint: you can't force everyone to update instantly, so the backend must support multiple app versions at once."

**Let's understand it fully:**

**Step 1 — Why mobile makes this hard.**
On the web, everyone gets the new version instantly. On mobile, users run **old app versions** for months. So a breaking API change would crash all those old apps — you must support old and new together.

**Step 2 — How to version.**
- **URL versioning** — `/v1/users`, `/v2/users` (most common, explicit).
- **Header versioning** — a version header.
Keep `v1` alive while old apps still use it; add `v2` for new behaviour.

```
Old app  → /v1/orders  (still works)
New app  → /v2/orders  (new fields/behaviour)
```

**Step 3 — Make changes backward-compatible when you can.**
- **Adding** a field is usually safe (old apps ignore it).
- **Removing/renaming/changing types** is breaking — that needs a new version.
- Design responses so clients tolerate unknown fields.

**Step 4 — Force-update as a last resort.**
For unavoidable breaking changes (or security), the app can check a minimum supported version on launch and show a "please update" screen. Use sparingly — it's a hard block for users.

**Why interviewers ask:** It tests awareness that mobile clients can't be updated on demand — a real-world constraint web devs often miss.

**Common mistake:** Making a breaking change to a shared endpoint and breaking every old app version in the wild.

**Follow-ups they may ask:**
- *"How long do you keep old versions?"* → Until usage of old app versions drops low enough (track it via analytics), then deprecate with notice.

**Related:** [Q8 (SDLC) — versioning](section_19_sdlc_interview_prep.md#q8) · [Q11 — SDK versioning](#q11)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. How do you design error handling across an entire Flutter app — from API failure to user-visible message?

> Very common · Medium–Hard

**Short answer (say this):**
"I handle errors in layers. The data layer catches low-level errors (network, parsing) and turns them into clear domain failures. The state layer maps those to UI states (error states). The UI shows a friendly, actionable message — never a raw exception. I also catch uncaught errors globally and report them to a crash tool."

**Let's understand it fully:**

**Step 1 — The layered flow.**

```
API/DB error → Data layer (catch, wrap) → domain Failure
            → State (Cubit emits Error state) → UI shows friendly message
```

Each layer translates the error into the right form for the next.

**Step 2 — Data layer: turn exceptions into typed failures.**
Catch raw errors (DioException, FormatException) and convert them into meaningful domain results — a sealed `Result`/`Either` or specific failure types ([Q8 Clean Code](section_16_clean_code.md#q8)).

```dart
Future<Result<User>> getUser() async {
  try {
    return Ok(await api.fetchUser());
  } on DioException catch (e) {
    return Err(e.type == DioExceptionType.connectionError
        ? NetworkFailure() : ServerFailure());
  }
}
```

**Step 3 — State layer: map failures to UI states.**
The Cubit/BLoC emits a clear error state with a user-friendly message, so the UI just renders it.

```dart
on failure → emit(FeedError('No internet. Pull to retry.'));
```

**Step 4 — UI: friendly, actionable, consistent.**
- Show a **clear message** ("No internet — pull to retry"), never a stack trace.
- Offer an **action** (retry button) where possible.
- Use **consistent** error widgets (a shared error view).

**Step 5 — Global safety net.**
Catch anything that slips through and report it:

```dart
FlutterError.onError = (details) => crashReporter.record(details);
PlatformDispatcher.instance.onError = (error, stack) { crashReporter.record(...); return true; };
```

So even unexpected crashes are logged (scrubbed of secrets, [Q5 Security](section_20_mobile_app_security.md#q5)) and the app degrades gracefully.

**Why interviewers ask:** App-wide error handling separates polished apps from fragile ones; it tests architecture and UX thinking together.

**Common mistake:** Showing raw exceptions to users, handling errors inconsistently per screen, or swallowing errors silently (no message, no report).

**Follow-ups they may ask:**
- *"Where do you catch uncaught async errors?"* → `PlatformDispatcher.instance.onError` (and `FlutterError.onError` for framework errors); report both.

**Related:** [Q8 (Clean Code) — result types](section_16_clean_code.md#q8) · [Q4 (Networking) — global error handling](../flutter/section7_networking_local_storage.md#q4) · [Q9 (SDLC) — production bugs](section_19_sdlc_interview_prep.md#q9)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## The 5-step design framework

```
1. Requirements (functional + non-functional)
2. High-level architecture (the big boxes)
3. Data flow + state management
4. Mobile concerns (offline, storage, caching, network)
5. Trade-offs (alternatives + why)
```

## Transport choice

| Need | Use |
|---|---|
| Normal CRUD data | REST |
| Live, two-way (chat, presence) | WebSocket |
| Server push when app closed | Push (FCM) |

## Design building blocks

| Concern | Go-to answer |
|---|---|
| Offline | local DB as source of truth, sync in background |
| Auth | short access + refresh tokens in secure storage |
| Big uploads | compress + chunk + retry + progress |
| Large team | modular feature packages + monorepo (melos) |
| Errors | layered: data → state → friendly UI + global catch |

## One-line reminders

- **Clarify requirements first**; talk trade-offs out loud. ([Q1](#q1))
- **REST** for most data; **WebSocket** only for real-time. ([Q2](#q2))
- **Chat** = WebSocket + local DB + optimistic UI + reconnect/ordering. ([Q3](#q3))
- **Offline-first** = local DB is the source of truth; UI watches it. ([Q4](#q4))
- **Auth** = short access + refresh tokens, secure storage, silent refresh. ([Q5](#q5))
- **Uploads** = compress, chunk, progress, retry; survive lifecycle. ([Q6](#q6))
- **Push** = FCM token → backend → handle foreground/background/terminated. ([Q7](#q7))
- **Cart** = state + local persistence + backend sync; merge on login. ([Q8](#q8))
- **Scale** = pagination, caching, lazy loading, isolates; modular code. ([Q9](#q9), [Q10](#q10))
- **SDK** = small stable API, hide internals, docs, semver. ([Q11](#q11))
- **API versioning** — mobile can't force updates; support old + new. ([Q12](#q12))
- **Errors** = data → state → friendly UI message + global crash catch. ([Q13](#q13))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Design interviews drill into trade-offs. Practice out loud:

1. *"Design chat."* → clarify first, then WebSocket + local DB + optimistic UI; discuss ordering & reconnection.
2. *"Now make it work offline."* → queue messages locally, send on reconnect, re-sync missed ones.
3. *"REST or WebSocket?"* → REST for normal data, WebSocket only where real-time is required.
4. *"50 screens, 10 devs — how do you structure it?"* → modular feature packages, monorepo with melos, enforced boundaries.
5. *"An API call fails — what does the user see?"* → a friendly, actionable message (not a stack trace), via layered error handling.

Clarifying first, then reasoning through trade-offs out loud — that *process* is what wins mobile system-design interviews, remote and BD alike.

[↑ Back to top](#toc)
