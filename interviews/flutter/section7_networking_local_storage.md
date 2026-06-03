# Section 7 — Networking & Local Storage

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

This section covers **two areas**: **Networking** (talking to a server) and **Local Storage** (saving data on the phone). They go together because a good app fetches data over the network *and* stores it locally so it works offline.

---

<a id="toc"></a>

## Table of Contents

**A. HTTP clients & configuration**
1. [`http` package vs Dio](#q1) · *Very common*
2. [Timeouts & retry strategy (connect vs receive)](#q2) · *Common*

**B. Auth, interceptors & error handling**
3. [Dio interceptors — auth token, 401 refresh & retry queue](#q3) · *Very common*
4. [Global error handling & `DioException` types](#q4) · *Very common*

**C. API design & honest error modeling**
5. [REST vs GraphQL on mobile](#q5) · *Common*
6. [The Either / Result pattern](#q6) · *Common*

**D. JSON & data parsing**
7. [JSON parsing — `json_serializable` & `freezed`](#q7) · *Very common*

**E. Security & offline resilience**
8. [Certificate pinning](#q8) · *Deeper*
9. [Handling no internet connection](#q9) · *Common*

**F. Local storage options**
10. [SharedPreferences — what, thread-safety, limits](#q10) · *Very common*
11. [Hive — boxes & TypeAdapters](#q11) · *Common*
12. [SQLite / Drift — relational data](#q12) · *Common*

**G. Secure storage & encryption**
13. [flutter_secure_storage — under the hood](#q13) · *Very common*
14. [Encrypting local data](#q14) · *Deeper*

**H. Offline-first & syncing**
15. [Offline-first architecture](#q15) · *Common*
16. [Keeping local data in sync with the server](#q16) · *Deeper*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

You don't need to study all 16 questions at once. Follow these stages in order — each one builds on the last. Tick a stage off only when you can give the **short answer** without looking.

**Stage 1 — Core networking (start here).** These come up in almost every interview.
→ [Q1 http vs Dio](#q1) · [Q3 Interceptors & token refresh](#q3) · [Q4 Error handling](#q4) · [Q7 JSON parsing](#q7)

**Stage 2 — Core local storage.** Where to save data on the phone.
→ [Q10 SharedPreferences](#q10) · [Q11 Hive](#q11) · [Q12 SQLite/Drift](#q12) · [Q13 Secure storage](#q13)

**Stage 3 — Clean design & robustness.** How a senior structures the code.
→ [Q2 Timeouts & retry](#q2) · [Q6 Either/Result](#q6) · [Q9 No internet](#q9)

**Stage 4 — Depth & senior signal.**
→ [Q5 REST vs GraphQL](#q5) · [Q14 Encrypting local data](#q14) · [Q15 Offline-first](#q15)

**Stage 5 — Deep-dive tie-breakers (do last).** These separate strong seniors from the rest.
→ [Q8 Certificate pinning](#q8) · [Q16 Sync strategies](#q16)

**Short on time (1 hour before the interview)?** Just review these eight:
[Q1](#q1) · [Q3](#q3) · [Q4](#q4) · [Q7](#q7) · [Q10](#q10) · [Q11](#q11) · [Q12](#q12) · [Q13](#q13), then read the [Cheat Sheet](#cheatsheet).

---

# A. HTTP clients & configuration

---

<a id="q1"></a>
## 1. What is the difference between the `http` package and Dio? Why is Dio usually preferred in production?

> Very common · Easy–Medium

**Short answer (say this):**
"The `http` package is Dart's basic, lightweight client — great for a simple GET or POST. Dio is a full-featured client built on top of that idea, with interceptors, request cancellation, timeouts, upload/download progress, and easy retry. In a real app, the things Dio gives you for free — like auth and logging in one place — are exactly the things you'd otherwise build by hand."

**Let's understand it fully:**

**Step 1 — Think of it like two kinds of delivery service.**
The `http` package is like sending a parcel yourself: you write the address, stamp it, and check on it manually every time. Dio is like a courier company with a system: you set up the rules once (address book, tracking, retry on failure), and every parcel follows them automatically.

**Step 2 — What `http` makes you do by hand.**
With `http`, every call repeats the same setup, and you must check the status code and parse JSON yourself.

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

final response = await http.get(
  Uri.parse('https://api.example.com/users'),
  headers: {
    'Authorization': 'Bearer $token',   // repeated on every call
    'Content-Type': 'application/json',
  },
);

if (response.statusCode == 200) {
  final data = jsonDecode(response.body); // parse JSON yourself
} else {
  // handle the error yourself, every time
}
```

**Step 3 — What Dio gives you: configure once, use everywhere.**
You set base URL, timeouts, and headers one time in `BaseOptions`. The response body is already parsed.

```dart
import 'package:dio/dio.dart';

final dio = Dio(BaseOptions(
  baseUrl: 'https://api.example.com',
  connectTimeout: const Duration(seconds: 10),
  receiveTimeout: const Duration(seconds: 15),
  headers: {'Content-Type': 'application/json'},
));

final response = await dio.get('/users');
// response.data is ALREADY parsed from JSON — no jsonDecode needed
```

**Step 4 — The real difference is the feature list.**
The big win is *interceptors* (see [Q3](#q3)): cross-cutting jobs like auth, logging, and retry live in one place instead of being copy-pasted into every API call.

| Feature | `http` | Dio |
|---|---|---|
| Interceptors (request/response/error) | No | Yes |
| Cancel a request | No | Yes (`CancelToken`) |
| Timeout config | Limited | Per-request and global |
| Upload / download progress | No | Yes (`onSendProgress` / `onReceiveProgress`) |
| FormData / multipart | Manual | Built-in |
| Retry logic | Manual | Easy via interceptor |
| Base URL & default headers | Manual | Built-in (`BaseOptions`) |
| Auto JSON parsing | Manual | Built-in |

**Step 5 — When `http` is still fine.**
For a tiny app, a script, or a package that doesn't want a big dependency, `http` is perfectly good. Dio earns its place once you have auth, retries, or many endpoints.

**Why interviewers ask:** They want to know you've built real apps. Anyone who has dealt with token refresh, upload progress, or request cancellation in production knows why a thin wrapper like `http` is not enough on its own.

**Common mistake:** Saying "Dio is better because it's more popular." That's not a technical answer. Talk about interceptors, cancellation, timeouts, and progress — the actual architectural advantages.

**Follow-ups they may ask:**
- *"Can you cancel a request in Dio?"* → Yes — pass a `CancelToken` and call `token.cancel()` (useful when a user leaves a screen mid-load).
- *"Is `http` ever the right choice?"* → Yes, for very small apps or low-dependency packages where Dio's extras aren't needed.

**Related:** [Q2 — timeouts & retry](#q2) · [Q3 — interceptors](#q3)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How do you set timeouts and a retry strategy? What is the difference between connect timeout and receive timeout?

> Common · Medium

**Short answer (say this):**
"Connect timeout is how long I wait to *open* the connection to the server. Receive timeout is how long I wait for the server to *send data* after the connection is open. They protect against different failures. For retries, I only retry on timeouts and 5xx server errors, never on 4xx, and I use exponential backoff so I don't hammer a struggling server."

**Let's understand it fully:**

**Step 1 — A phone-call analogy.**
- **Connect timeout** = how long you let the phone ring before giving up. If nobody picks up in 10 seconds, the server is probably down.
- **Receive timeout** = once they pick up, how long you wait for them to actually talk. They answered, but they're silent — give up after a while.
- **Send timeout** = how long you allow yourself to finish speaking (uploading the request body). Matters most for big file uploads.

**Step 2 — Where each one sits on the timeline.**

```
  |-- connectTimeout --|                       |-- receiveTimeout --|
  |                    |                       |                    |
  DNS > TCP handshake > TLS > Send request > Server thinks > Response
       \- connection -/                    \--- receiving data ----/
        opened here                          first byte to last byte

  sendTimeout covers: |- time to upload the request body -|
```

**Step 3 — Pick sensible values.**
- *Connect timeout:* short (5–10s). Failing fast is good; retrying makes sense here.
- *Receive timeout:* match the API's real speed. A search may need 15s; a big download may need 60s.
- *Send timeout:* generous for large uploads.

```dart
final dio = Dio(BaseOptions(
  baseUrl: 'https://api.example.com',
  connectTimeout: const Duration(seconds: 8),
  receiveTimeout: const Duration(seconds: 15),
  sendTimeout: const Duration(seconds: 15),
));

// Override per request for a slow endpoint
final report = await dio.get(
  '/reports/generate',
  options: Options(receiveTimeout: const Duration(seconds: 60)),
);
```

**Step 4 — A retry interceptor with exponential backoff.**
"Exponential backoff" means each retry waits longer than the last (1s, then 2s, then 4s). This gives a busy server room to recover instead of being flooded.

```dart
import 'dart:math';

class RetryInterceptor extends Interceptor {
  final Dio dio;
  final int maxRetries;
  RetryInterceptor({required this.dio, this.maxRetries = 3});

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    if (_shouldRetry(err)) {
      final count = (err.requestOptions.extra['retryCount'] as int?) ?? 0;
      if (count < maxRetries) {
        // 1s, 2s, 4s — wait longer each time
        final delay = Duration(milliseconds: 1000 * pow(2, count).toInt());
        await Future.delayed(delay);

        err.requestOptions.extra['retryCount'] = count + 1;
        try {
          final response = await dio.fetch(err.requestOptions);
          handler.resolve(response); // success — stop here
          return;
        } catch (_) {
          // fall through to handler.next below
        }
      }
    }
    handler.next(err); // give up, pass the error on
  }

  bool _shouldRetry(DioException err) {
    return err.type == DioExceptionType.connectionTimeout ||
        err.type == DioExceptionType.receiveTimeout ||
        err.type == DioExceptionType.connectionError ||
        (err.response?.statusCode ?? 0) >= 500; // 5xx server errors
  }
}
```

**Step 5 — The golden retry rules.**
- Retry on timeouts and 5xx (the server's fault — it may recover).
- Never retry on 4xx (your request is wrong; sending it again won't help).
- Always use backoff, and cap the number of retries.

**Why interviewers ask:** It shows you understand the network lifecycle and can make trade-offs. Aggressive retries with no backoff can accidentally DDoS your own server during an outage.

**Common mistake:** Setting one big timeout (60s for everything) instead of tuning each type. Also retrying 400 or 422 — those are deterministic client errors that will fail again.

**Follow-ups they may ask:**
- *"Why exponential backoff and not a fixed delay?"* → A fixed short delay from thousands of clients all at once keeps the server down. Backoff spreads the load out.
- *"Would you add jitter?"* → Yes — a small random delay on top of backoff stops every client retrying at the exact same instant (the "thundering herd").

**Related:** [Q1 — http vs Dio](#q1) · [Q4 — error handling](#q4) · [Q3 — interceptors](#q3)

[↑ Back to top](#toc)

---

# B. Auth, interceptors & error handling

---

<a id="q3"></a>
## 3. How do Dio interceptors work? How do you inject an auth token, and handle a 401 with token refresh and a retry queue?

> Very common · Medium–Hard — the classic real-world networking question.

**Short answer (say this):**
"An interceptor sits in the middle of every request, like airport security: every request passes through `onRequest`, every response through `onResponse`, every error through `onError`. I attach the auth token in `onRequest`. For a 401, I refresh the token *once*, then replay the failed requests with the new token. The key is to use `QueuedInterceptor` so three 401s don't trigger three refreshes at the same time."

**Let's understand it fully:**

**Step 1 — The airport security analogy.**
Every passenger (request) must pass through one security checkpoint (the interceptor) before boarding. The checkpoint can stamp their pass (add a token), send them back (reject), or pull them aside (retry). Because everyone goes through the same checkpoint, you write the rule once instead of at every gate.

**Step 2 — The three hooks.**

```dart
class MyInterceptor extends Interceptor {
  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    // runs before EVERY request leaves the app
    handler.next(options); // let it continue
  }

  @override
  void onResponse(Response response, ResponseInterceptorHandler handler) {
    // runs for EVERY successful response
    handler.next(response);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    // runs for EVERY error
    handler.next(err);
  }
}
```

You always end with one of three actions: `handler.next(...)` (continue), `handler.resolve(response)` (succeed early), or `handler.reject(err)` (fail).

**Step 3 — Inject the auth token (the easy part).**

```dart
@override
void onRequest(RequestOptions options, RequestInterceptorHandler handler) async {
  final token = await _tokenStorage.getAccessToken();
  if (token != null) {
    options.headers['Authorization'] = 'Bearer $token';
  }
  handler.next(options);
}
```

**Step 4 — The hard part: a 401 and the "refresh once" problem.**
A token expires. The server replies **401 Unauthorized**. You must get a fresh token and retry. But imagine three requests fire at once and all get 401. If each one refreshes the token separately, you trigger three refreshes — a race condition that can invalidate each other's tokens.

The picture you want:

```
  Request → onRequest (attach token) → Server
                                          |
                                     401 Unauthorized
                                          |
                                   onError fires
                                          |
                            Is a refresh already running?
                             |                    |
                            YES                   NO
                             |                    |
                      wait in the queue     lock + refresh once
                             |                    |
                             |               get new token
                             |                    |
                             +→ retry all with the new token
```

**Step 5 — The fix: `QueuedInterceptor`.**
`QueuedInterceptor` runs its error handling **one at a time**. So when three 401s arrive, only the first triggers the refresh; the other two wait their turn and reuse the fresh token.

```dart
class AuthInterceptor extends QueuedInterceptor {
  final Dio _dio;
  final TokenStorage _tokenStorage;
  AuthInterceptor(this._dio, this._tokenStorage);

  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) async {
    final token = await _tokenStorage.getAccessToken();
    if (token != null) {
      options.headers['Authorization'] = 'Bearer $token';
    }
    handler.next(options);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) async {
    if (err.response?.statusCode == 401) {
      try {
        // Because this is a QueuedInterceptor, only ONE refresh runs at a time.
        final newToken = await _refreshToken();
        await _tokenStorage.saveAccessToken(newToken);

        // Replay the original request with the new token
        final options = err.requestOptions;
        options.headers['Authorization'] = 'Bearer $newToken';
        final response = await _dio.fetch(options);
        handler.resolve(response); // success — caller never sees the 401
      } catch (_) {
        await _tokenStorage.clear(); // refresh failed → force logout
        handler.reject(err);
      }
    } else {
      handler.next(err); // not a 401 — pass it on
    }
  }

  Future<String> _refreshToken() async {
    final refreshToken = await _tokenStorage.getRefreshToken();
    // IMPORTANT: a SEPARATE Dio with no auth interceptor, or you loop forever
    final freshDio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));
    final res = await freshDio.post('/auth/refresh', data: {
      'refresh_token': refreshToken,
    });
    return res.data['access_token'] as String;
  }
}

// Registration — order matters: auth first, logging after
final dio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));
dio.interceptors.add(AuthInterceptor(dio, tokenStorage));
dio.interceptors.add(LogInterceptor()); // runs after auth has added the token
```

**Step 6 — Two details that cause real bugs.**
- Use `QueuedInterceptor`, not plain `Interceptor`, or you get the multi-refresh race.
- Use a **separate** Dio instance for the refresh call. If you reuse the main `dio`, the refresh request also goes through `AuthInterceptor`, and if *it* returns 401 you get an infinite loop.

**Why interviewers ask:** Token refresh with a retry queue is one of the most common real-world challenges. They're checking whether you'd build it correctly or introduce race conditions.

**Common mistake:** Using a regular `Interceptor` (multi-refresh race), or using the same Dio instance for the refresh call (infinite loop).

**Follow-ups they may ask:**
- *"What if the refresh token itself is expired?"* → The refresh call fails, you clear storage and force the user to log in again.
- *"Where do you store the tokens?"* → In `flutter_secure_storage`, never in SharedPreferences (see [Q13](#q13)).

**Related:** [Q4 — error handling](#q4) · [Q13 — secure storage for tokens](#q13) · [Q2 — retry](#q2)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. How do you do global error handling in Dio? What are the `DioException` types?

> Very common · Medium

**Short answer (say this):**
"Global error handling means catching every network error in one place — an interceptor — so individual API calls don't repeat the same try/catch. Dio wraps all failures in a `DioException` with a `type` field telling me exactly what went wrong: timeout, no connection, bad response, cancelled, and so on. I map each type to a clear, typed app error that the UI can react to."

**Let's understand it fully:**

**Step 1 — Why centralize errors.**
Without a central place, every screen writes its own try/catch and its own "something went wrong" message. That's repetitive and inconsistent. One interceptor turns raw network errors into clean app errors for the whole app.

**Step 2 — The `DioException` types (memorize these).**

```
connectionTimeout  → could not open the connection in time
sendTimeout        → uploading the request body took too long
receiveTimeout     → server took too long to respond
badCertificate     → SSL/TLS certificate check failed
badResponse        → server replied with an error status (4xx / 5xx)
cancel             → request was cancelled (CancelToken)
connectionError    → no connection at all (DNS failure, no internet)
unknown            → anything else (e.g. a parsing error)
```

**Step 3 — Map each type to a typed app failure.**
Use a Dart 3 `sealed` class for the failure so the UI can handle every case (see [Q6](#q6) and Section 1's sealed-class question).

```dart
class GlobalErrorInterceptor extends Interceptor {
  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    final failure = _mapToFailure(err);
    // Attach the typed failure so upper layers get a clean error
    handler.next(err.copyWith(error: failure));
  }

  AppFailure _mapToFailure(DioException err) {
    switch (err.type) {
      case DioExceptionType.connectionTimeout:
      case DioExceptionType.sendTimeout:
      case DioExceptionType.receiveTimeout:
        return AppFailure.timeout('Server is taking too long. Try again.');
      case DioExceptionType.connectionError:
        return AppFailure.noConnection('No internet connection.');
      case DioExceptionType.badResponse:
        return _handleBadResponse(err.response!);
      case DioExceptionType.badCertificate:
        return AppFailure.security('Secure connection failed.');
      case DioExceptionType.cancel:
        return AppFailure.cancelled('Request was cancelled.');
      case DioExceptionType.unknown:
        return AppFailure.unexpected('Something went wrong: ${err.message}');
    }
  }

  AppFailure _handleBadResponse(Response response) {
    return switch (response.statusCode) {
      400 => AppFailure.badRequest(response.data['message'] ?? 'Invalid request'),
      401 => AppFailure.unauthorized('Session expired.'),
      403 => AppFailure.forbidden('Access denied.'),
      404 => AppFailure.notFound('Not found.'),
      422 => AppFailure.validation(response.data['errors']),
      429 => AppFailure.rateLimited('Too many requests.'),
      final code when code != null && code >= 500 =>
        AppFailure.server('Server error. Try again later.'),
      _ => AppFailure.unexpected('Error: ${response.statusCode}'),
    };
  }
}

// One typed error model the whole app understands
sealed class AppFailure {
  final String message;
  const AppFailure(this.message);

  factory AppFailure.timeout(String m) = TimeoutFailure;
  factory AppFailure.noConnection(String m) = NoConnectionFailure;
  factory AppFailure.server(String m) = ServerFailure;
  factory AppFailure.unauthorized(String m) = UnauthorizedFailure;
  factory AppFailure.forbidden(String m) = ForbiddenFailure;
  factory AppFailure.notFound(String m) = NotFoundFailure;
  factory AppFailure.badRequest(String m) = BadRequestFailure;
  factory AppFailure.validation(dynamic errors) = ValidationFailure;
  factory AppFailure.rateLimited(String m) = RateLimitedFailure;
  factory AppFailure.security(String m) = SecurityFailure;
  factory AppFailure.cancelled(String m) = CancelledFailure;
  factory AppFailure.unexpected(String m) = UnexpectedFailure;
}

class TimeoutFailure extends AppFailure { const TimeoutFailure(super.m); }
class NoConnectionFailure extends AppFailure { const NoConnectionFailure(super.m); }
// ...and one small subclass per factory above
```

**Step 4 — The payoff in the UI.**
Because the failure is typed, the screen can switch on it and show the right message and the right action (retry, offline banner, or log out) — no raw status codes leak into widgets.

**Why interviewers ask:** It shows you don't scatter try/catch everywhere. They want a central, typed error model the UI can pattern-match on.

**Common mistake:** Treating every `DioException` as one generic "network error." Each type needs a different message and recovery: retry for a timeout, an offline banner for `connectionError`, force logout for 401.

**Follow-ups they may ask:**
- *"401 vs 403?"* → 401 = not logged in / token expired (refresh or log in). 403 = logged in but not allowed (don't retry).
- *"Where do you show the message?"* → The UI layer reads the typed failure and decides; the network layer never touches widgets.

**Related:** [Q3 — interceptors & 401](#q3) · [Q6 — Either/Result](#q6) · [Q9 — offline handling](#q9)

[↑ Back to top](#toc)

---

# C. API design & honest error modeling

---

<a id="q5"></a>
## 5. What is the difference between REST and GraphQL? What are the trade-offs on mobile?

> Common · Medium

**Short answer (say this):**
"REST gives you many fixed endpoints, each returning a fixed shape of data. GraphQL gives you one endpoint where the client asks for exactly the fields it needs. GraphQL avoids over-fetching and reduces round trips, which is great on slow mobile networks. But its caching is harder and it always returns 200, so error handling is trickier. I pick based on the app, not the hype."

**Let's understand it fully:**

**Step 1 — A restaurant analogy.**
- **REST** is a fixed-menu restaurant: each dish (endpoint) comes exactly as listed. If you only want the rice, you still get the full plate.
- **GraphQL** is a build-your-own-bowl place: you tell them precisely which ingredients (fields) you want, and they hand you just that.

**Step 2 — See the shape difference.**

```
REST: many endpoints, fixed responses

  GET /users/42           → { id, name, email, avatar, bio, ... }
  GET /users/42/posts     → [{ id, title, body, createdAt, ... }]
  GET /users/42/followers → [{ id, name, avatar, ... }]
  → 3 round trips, many unused fields on mobile

GraphQL: one endpoint, you choose the fields

  POST /graphql
  query {
    user(id: 42) {
      name
      avatar
      posts(first: 5) { title }
      followersCount
    }
  }
  → 1 round trip, only the fields the screen needs
```

**Step 3 — The trade-offs that matter on mobile.**
- **Over-fetching / under-fetching:** REST returns fixed payloads (often too much). GraphQL returns exactly what you ask — important on slow connections.
- **Round trips:** A screen often needs data from several resources. REST = several calls (or a custom BFF endpoint). GraphQL = one query.
- **Caching:** REST caches easily by URL (HTTP caching). GraphQL is harder — everything is a POST to one URL, so you need a normalized cache (`graphql_flutter` or `ferry`).
- **File uploads:** REST handles multipart natively. GraphQL needs the multipart spec or a separate REST endpoint.
- **Error handling:** REST uses HTTP status codes. GraphQL almost always returns 200 and puts errors inside the body, so a global error interceptor (see [Q4](#q4)) needs to look inside the response.
- **Tooling in Flutter:** REST + Dio is mature and simple. GraphQL uses `graphql_flutter` or `ferry` — more setup and code generation, but strong type safety.

**Step 4 — Code, side by side.**

```dart
// REST with Dio: a second call for related data
final user = UserModel.fromJson((await dio.get('/users/42')).data);
final posts = (await dio.get('/users/42/posts')).data; // extra round trip

// GraphQL with graphql_flutter: one call, exact shape
const q = r'''
  query GetProfile($id: ID!) {
    user(id: $id) { name avatar posts(first: 5) { title createdAt } }
  }
''';
final result = await client.query(
  QueryOptions(document: gql(q), variables: {'id': '42'}),
);
```

**Why interviewers ask:** They're testing whether you choose tools by trade-offs, not hype. Many mobile apps are better served by REST plus a thin BFF (backend-for-frontend) than by full GraphQL.

**Common mistake:** Saying GraphQL is "always better" because it fixes over-fetching. For simple CRUD apps, its caching complexity, error quirks, and bigger query payloads can outweigh the benefits.

**Follow-ups they may ask:**
- *"What is a BFF?"* → A small backend tailored to your app that bundles several calls into one — gets REST close to GraphQL's "one call per screen" without GraphQL's complexity.
- *"How does GraphQL caching work in Flutter?"* → A normalized cache stores objects by ID so the same object is shared across queries; `ferry` and `graphql_flutter` provide this.

**Related:** [Q4 — error handling](#q4) · [Q7 — JSON parsing](#q7)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is the Either / Result pattern? Why is it better than throwing exceptions across layers?

> Common · Medium–Hard

**Short answer (say this):**
"Either (or Result) makes a function's return type honest: it says 'this returns data OR a failure.' Instead of throwing an exception that the caller might forget to catch, I return a value that forces the caller to handle both cases. I keep exceptions at the boundary — the network and database layers — and use typed return values everywhere above that."

**Let's understand it fully:**

**Step 1 — The "hidden trapdoor" problem with exceptions.**
A signature like `Future<User> getUser()` *looks* like it always returns a `User`. But it might secretly throw five different exceptions. The caller can't see that from the type and may forget to catch them — a hidden trapdoor.

```
Exception approach (hidden failure path):
  Future<User> getUser()   -- says "returns User"
                           -- but can throw several exceptions
                           -- caller may not handle any of them

Either approach (honest contract):
  Future<Either<Failure, User>> getUser()
                           -- says "returns Failure OR User"
                           -- caller MUST handle both
                           -- no hidden control flow
```

**Step 2 — A simple Either using Dart 3 sealed classes.**
`Left` carries the failure, `Right` carries the success (the convention is "right is right/correct").

```dart
sealed class Either<L, R> {
  const Either();
}
class Left<L, R> extends Either<L, R> {
  final L value;
  const Left(this.value);
}
class Right<L, R> extends Either<L, R> {
  final R value;
  const Right(this.value);
}

// A helper to handle both sides at once
extension EitherX<L, R> on Either<L, R> {
  T fold<T>(T Function(L) onLeft, T Function(R) onRight) => switch (this) {
        Left(:final value) => onLeft(value),
        Right(:final value) => onRight(value),
      };
}
```

**Step 3 — Use it in the repository (catch exceptions at the boundary).**

```dart
class UserRepository {
  final Dio _dio;
  UserRepository(this._dio);

  Future<Either<AppFailure, User>> getUser(String id) async {
    try {
      final response = await _dio.get('/users/$id');
      return Right(User.fromJson(response.data)); // success
    } on DioException catch (e) {
      return Left(_mapError(e));                   // expected failure
    } catch (e) {
      return Left(AppFailure.unexpected(e.toString()));
    }
  }

  AppFailure _mapError(DioException e) =>
      e.type == DioExceptionType.connectionError
          ? AppFailure.noConnection('No internet')
          : AppFailure.server('Server error');
}
```

**Step 4 — The caller can't ignore the failure.**

```dart
class UserCubit extends Cubit<UserState> {
  final UserRepository _repo;
  UserCubit(this._repo) : super(UserInitial());

  Future<void> loadUser(String id) async {
    emit(UserLoading());
    final result = await _repo.getUser(id);
    result.fold(
      (failure) => emit(UserError(failure.message)), // must handle
      (user) => emit(UserLoaded(user)),
    );
    // No try/catch here — the failure is a VALUE, not a surprise throw
  }
}
```

**Step 5 — When to use it (and when not to).**
Keep exceptions for truly exceptional, unexpected things and for the boundary layers. Use Either for *expected* outcomes like "user not found" or "no internet." Don't wrap tiny internal helper functions in Either — a plain throw there is fine.

**Step 6 — In production, use a tested package.**
Most teams use `fpdart` (or the older `dartz`) for a battle-tested `Either` with helpers like `map` and `flatMap`, instead of hand-rolling it.

**Why interviewers ask:** It shows you design API boundaries on purpose — exceptions for the unexpected, typed values for expected failures. That's clean-architecture thinking.

**Common mistake:** Using `Either` but then only handling the success side and ignoring the failure side. Also wrapping *everything* in Either, even where a simple throw is clearer.

**Follow-ups they may ask:**
- *"Why `Left` for failure?"* → Just a convention from functional programming: `Right` means the "right/correct" value, `Left` is the other case.
- *"Difference from a sealed Result?"* → None in spirit. A `sealed Result { Success, Failure }` is the same idea with friendlier names; Either is the generic version.

**Related:** [Q4 — typed failures](#q4) · [Q5 — REST error shapes](#q5)

[↑ Back to top](#toc)

---

# D. JSON & data parsing

---

<a id="q7"></a>
## 7. How do you parse JSON in Flutter? Compare manual parsing, `json_serializable`, and `freezed`.

> Very common · Medium

**Short answer (say this):**
"JSON arrives as a `Map<String, dynamic>`, and I turn it into a typed Dart object so the rest of the app is safe. For one or two tiny models I write `fromJson`/`toJson` by hand. For real projects I use `json_serializable` to generate that code, or `freezed` when I also want immutability, `copyWith`, and value equality for free. Hand-written parsing is where silent bugs hide."

**Let's understand it fully:**

**Step 1 — Why parse at all? (a translator analogy.)**
JSON from the server is like a letter in a foreign language: it's just text and loose key-value pairs. Parsing is hiring a translator that turns it into a proper Dart object with named, typed fields — so the compiler can check your code and autocomplete works.

**Step 2 — Manual parsing (fine for tiny models).**
You write the two methods yourself.

```dart
class User {
  final String id;
  final String name;
  final String? email; // nullable on purpose
  const User({required this.id, required this.name, this.email});

  factory User.fromJson(Map<String, dynamic> json) => User(
        id: json['id'] as String,
        name: json['name'] as String,
        email: json['email'] as String?,
      );

  Map<String, dynamic> toJson() => {'id': id, 'name': name, 'email': email};
}
```

This works, but for a model with 20 fields it's long and easy to get wrong (a typo in a key, or forgetting null safety, crashes at runtime).

**Step 3 — `json_serializable` (generate the boring code).**
You annotate the class and let the build tool write `fromJson`/`toJson`. Run `dart run build_runner build`.

```dart
import 'package:json_annotation/json_annotation.dart';
part 'user.g.dart'; // generated file

@JsonSerializable()
class User {
  final String id;
  final String name;

  @JsonKey(name: 'email_address') // map a different server key name
  final String? email;

  const User({required this.id, required this.name, this.email});

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}
```

`@JsonKey` handles snake_case server keys, defaults, and custom converters — no manual mapping mistakes.

**Step 4 — `freezed` (immutability + equality + copyWith, all generated).**
`freezed` builds on the same idea but also generates an immutable class, value-based `==`/`hashCode`, and a `copyWith`. This is ideal for state objects (it pairs perfectly with BLoC/Riverpod, see Section 1 on equality).

```dart
import 'package:freezed_annotation/freezed_annotation.dart';
part 'user.freezed.dart';
part 'user.g.dart';

@freezed
class User with _$User {
  const factory User({
    required String id,
    required String name,
    String? email,
  }) = _User;

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
}

// You get all of this for free:
final a = User(id: '1', name: 'Sara');
final b = a.copyWith(name: 'Sara Khan'); // immutable update
print(a == User(id: '1', name: 'Sara'));  // true (value equality)
```

**Step 5 — Handling nested objects and lists.**
A common interview detail: a list of objects must be mapped, not just cast.

```dart
// A field that is a list of other models:
final tags = (json['tags'] as List<dynamic>)
    .map((e) => Tag.fromJson(e as Map<String, dynamic>))
    .toList();
```

With `json_serializable` / `freezed`, this nested parsing is generated for you automatically.

**Step 6 — Quick comparison.**

| | Manual | `json_serializable` | `freezed` |
|---|---|---|---|
| Boilerplate | you write it all | generated | generated |
| Immutability | only if you add `final` | up to you | yes, built in |
| `==` / `hashCode` | by hand | by hand | generated |
| `copyWith` | by hand | no | generated |
| Best for | 1–2 tiny models | most DTOs / API models | state & domain models |

**Why interviewers ask:** To see you don't hand-write fragile parsing for big models, and that you know `freezed` gives immutability and value equality (which matters for state management rebuilds).

**Common mistake:** Casting a list with `as List<User>` instead of mapping each item with `fromJson`. Also forgetting to run `build_runner` after changing an annotated model.

**Follow-ups they may ask:**
- *"`json_serializable` vs `freezed` — when each?"* → `json_serializable` when you only need parsing. `freezed` when you also want immutability, `copyWith`, and equality (state/domain models).
- *"How do you handle a field that can be `int` or `String` from the server?"* → A custom `JsonConverter`, or normalize it in `fromJson`.

**Related:** [Q4 — typed errors](#q4) · [Q5 — GraphQL types](#q5)

[↑ Back to top](#toc)

---

# E. Security & offline resilience

---

<a id="q8"></a>
## 8. What is certificate pinning, why does it matter, and how do you do it in Flutter?

> Deeper question · Hard

**Short answer (say this):**
"Certificate pinning means my app only trusts *my* server's specific certificate or public key — not just any certificate signed by some trusted authority. It stops man-in-the-middle attacks where someone with a rogue authority certificate intercepts my HTTPS traffic. The safer style is to pin the public key, because it survives certificate renewal."

**Let's understand it fully:**

**Step 1 — The ID-card analogy.**
Normal HTTPS is like a guard who accepts any ID card issued by any government office. Pinning is like a guard who has a photo of *your* exact ID and only lets that one through. A faked-but-officially-signed ID gets in past the normal guard, but fails against the photo.

**Step 2 — What normal HTTPS checks (and the gap).**

```
Normal HTTPS (trusts any valid CA):
  App → TLS handshake → server shows a certificate
                              |
                         Signed by ANY trusted CA?
                              |
                             YES → accepted
                             (an attacker with a rogue CA cert ALSO passes)

With certificate pinning:
  App → TLS handshake → server shows a certificate
                              |
                         Does its key match the PIN baked into the app?
                              |
                             YES → accepted
                             NO  → REJECTED  (rogue cert is blocked)
```

**Step 3 — Two pinning styles.**
- **Certificate pinning:** pin the whole certificate. Simple, but you must ship an app update every time the cert rotates.
- **Public key pinning:** pin only the public key. The key usually stays the same across renewals, so the app keeps working when the cert rotates. **Preferred.**

**Step 4 — A Dart-level approach with Dio.**
You check the server certificate's fingerprint against your hardcoded pin.

```dart
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:dio/io.dart';

Dio createPinnedDio() {
  final dio = Dio(BaseOptions(baseUrl: 'https://api.example.com'));

  (dio.httpClientAdapter as IOHttpClientAdapter).createHttpClient = () {
    final client = HttpClient();
    client.badCertificateCallback = (X509Certificate cert, String host, int port) {
      const pinnedSha256 = 'A1:B2:C3:D4:...'; // your cert/key SHA-256 fingerprint
      final serverSha256 = cert.sha256Fingerprint; // (helper / computed value)
      return serverSha256 == pinnedSha256; // true = accept, false = reject
    };
    return client;
  };
  return dio;
}
```

**Step 5 — Why teams often pin in native code.**
Dart's `SecurityContext` is limited (especially for extracting the public key), so many production apps pin at the native layer — `OkHttp`'s `CertificatePinner` on Android and a `URLSession` delegate on iOS — reached through a method channel. Packages like `http_certificate_pinning` also wrap this.

**Step 6 — Always keep a backup pin.**
Pin **two** keys: the live one and a backup. If you ever need to rotate keys in an emergency, the backup pin keeps the app working until users update.

**Why interviewers ask:** To gauge your security awareness. Apps handling money, health, or auth tokens should pin. It shows you think beyond "HTTPS is enough."

**Common mistake:** Pinning the leaf certificate instead of the public key. When the cert rotates (every 90 days with Let's Encrypt), the app breaks unless you ship an update. Pin the public key, and keep a backup pin.

**Follow-ups they may ask:**
- *"Doesn't HTTPS already stop MITM?"* → Only if every trusted CA is honest and uncompromised. Pinning removes that trust-everyone assumption for your own server.
- *"Risk of pinning?"* → If you forget to ship the new pin before the cert changes, you can lock out all users. That's why you keep a backup pin and a rotation plan.

**Related:** [Q4 — badCertificate error](#q4) · [Q13 — secure storage](#q13)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. How do you handle no internet connection gracefully?

> Common · Medium

**Short answer (say this):**
"I handle it in layers: detect connectivity, tell the user without blocking them, and serve cached data when possible. One key point — `connectivity_plus` only tells me the *connection type* (wifi/mobile), not whether the internet actually works. So after it changes, I confirm with a quick real lookup before deciding I'm online."

**Let's understand it fully:**

**Step 1 — The three layers.**

```
  UI layer       → offline banner, disable/enable actions, show cached data
       |  (reads state from)
  State layer    → a ConnectivityCubit watching a connectivity stream
       |  (driven by)
  Network layer  → a Dio interceptor that falls back to cache on failure
```

**Step 2 — Detect connectivity, then verify it's real.**
The trap: being on wifi does not mean the internet works (think of an airport wifi login page). So do a tiny DNS lookup to confirm.

```dart
class ConnectivityCubit extends Cubit<ConnectivityStatus> {
  late final StreamSubscription _sub;

  ConnectivityCubit() : super(ConnectivityStatus.online) {
    _sub = Connectivity().onConnectivityChanged.listen((_) async {
      // connectivity_plus reports the INTERFACE (wifi/mobile), not real internet.
      final hasInternet = await _reallyOnline();
      emit(hasInternet ? ConnectivityStatus.online : ConnectivityStatus.offline);
    });
  }

  Future<bool> _reallyOnline() async {
    try {
      final r = await InternetAddress.lookup('example.com')
          .timeout(const Duration(seconds: 3));
      return r.isNotEmpty && r.first.rawAddress.isNotEmpty;
    } catch (_) {
      return false;
    }
  }

  @override
  Future<void> close() {
    _sub.cancel();
    return super.close();
  }
}
```

**Step 3 — Network layer: serve cache when the call fails.**
A "nearby shelf vs far warehouse" idea: the cache is the nearby shelf. If the warehouse (server) is unreachable, grab the item from the shelf instead of failing.

```dart
class OfflineCacheInterceptor extends Interceptor {
  final LocalCacheSource _cache;
  OfflineCacheInterceptor(this._cache);

  @override
  void onResponse(Response response, ResponseInterceptorHandler handler) {
    if (response.requestOptions.method == 'GET') {
      _cache.put(response.requestOptions.uri.toString(), response.data); // fill the shelf
    }
    handler.next(response);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    final isGet = err.requestOptions.method == 'GET';
    if (err.type == DioExceptionType.connectionError && isGet) {
      final cached = _cache.get(err.requestOptions.uri.toString());
      if (cached != null) {
        // Serve from the shelf instead of throwing
        handler.resolve(Response(
          requestOptions: err.requestOptions,
          data: cached,
          statusCode: 200,
          statusMessage: 'FROM_CACHE',
        ));
        return;
      }
    }
    handler.next(err);
  }
}
```

**Step 4 — UI layer: a clear, non-blocking banner.**

```dart
BlocBuilder<ConnectivityCubit, ConnectivityStatus>(
  builder: (context, status) => Column(
    children: [
      if (status == ConnectivityStatus.offline)
        const MaterialBanner(
          content: Text('You are offline. Showing cached data.'),
          actions: [SizedBox.shrink()],
          backgroundColor: Colors.orange,
        ),
      const Expanded(child: MainContent()),
    ],
  ),
);
```

**Why interviewers ask:** Mobile apps *will* lose connectivity. They want to see you designed for it — not just caught the error, but gave a degraded experience that still works.

**Common mistake:** Trusting `connectivity_plus` alone for "am I online." It reports the interface type only. You can be on wifi with no real internet — always confirm with a DNS lookup or ping.

**Follow-ups they may ask:**
- *"How do you cache the responses?"* → Hive or a simple map keyed by URL, or use `dio_cache_interceptor` which does HTTP-style caching for you.
- *"What about writes while offline?"* → Queue them locally and sync when back online — that's offline-first (see [Q15](#q15)).

**Related:** [Q4 — connectionError](#q4) · [Q15 — offline-first](#q15) · [Q11 — Hive cache](#q11)

[↑ Back to top](#toc)

---

# F. Local storage options

---

<a id="q10"></a>
## 10. What does `SharedPreferences` store? Is it thread-safe, and what are its limits?

> Very common · Easy–Medium

**Short answer (say this):**
"SharedPreferences is a small key-value store for simple settings — backed by `NSUserDefaults` on iOS and an XML file on Android. It only holds primitives: `String`, `int`, `double`, `bool`, and `List<String>`. It's safe within one isolate, has no encryption, loads the whole file into memory, and is not a database. So it's for settings, not for big or sensitive data."

**Let's understand it fully:**

**Step 1 — Think of it as a sticky note, not a filing cabinet.**
SharedPreferences is for small notes: "onboarding done = true," "language = en." It is not where you store thousands of records — that needs a real database (see [Q11](#q11), [Q12](#q12)).

**Step 2 — What it stores and where.**

```
  Dart code
     |
  SharedPreferences plugin
     |→ iOS:     NSUserDefaults (a plist file)
     |→ Android: SharedPreferences (XML in /data/data/<pkg>/shared_prefs/)
```

Only these types: `String`, `int`, `double`, `bool`, `List<String>`. No maps, no custom objects.

**Step 3 — Basic use.**

```dart
final prefs = await SharedPreferences.getInstance();

// Write
await prefs.setString('locale', 'en');
await prefs.setBool('onboarding_complete', true);
await prefs.setInt('launch_count', 5);

// Read (always provide a default)
final locale = prefs.getString('locale') ?? 'en';
final onboarded = prefs.getBool('onboarding_complete') ?? false;

// Remove
await prefs.remove('locale');
```

**Step 4 — Thread safety.**
On `getInstance()` the plugin reads the whole file into memory; writes happen asynchronously to disk. Within a single isolate it's safe. Across isolates, or if native code writes the same file, you can hit race conditions.

**Step 5 — The limits to say out loud.**
No encryption (plain text on disk), only primitives, the whole file is loaded into memory (bad if it grows large), no queries, not built for large datasets. It's a settings store, not a database.

```dart
// Storing a complex object means serializing by hand — a code smell here:
await prefs.setString('cached_user', jsonEncode(user.toJson()));
// For real objects or lists, use Hive or SQLite/Drift instead.
```

**Why interviewers ask:** To confirm you know what SharedPreferences is *for* — small, simple settings — and that you wouldn't store 10,000 products in it.

**Common mistake:** Storing sensitive data (tokens, passwords) in SharedPreferences — it's plain text. Use `flutter_secure_storage` (see [Q13](#q13)). Also serializing big JSON into it instead of using Hive or SQLite.

**Follow-ups they may ask:**
- *"How would you store a token?"* → Never here. Use `flutter_secure_storage` ([Q13](#q13)).
- *"What about a list of objects?"* → Use Hive ([Q11](#q11)) or Drift ([Q12](#q12)); SharedPreferences only holds `List<String>`.

**Related:** [Q11 — Hive](#q11) · [Q12 — SQLite/Drift](#q12) · [Q13 — secure storage](#q13)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is Hive? What are boxes and TypeAdapters, and when do you prefer it over SharedPreferences?

> Common · Medium

**Short answer (say this):**
"Hive is a fast, pure-Dart NoSQL key-value database. It's quick because it has no platform channels and stores data in binary, and it handles custom objects through TypeAdapters. A *box* is like a table — a named container of key-value pairs. A *TypeAdapter* tells Hive how to convert my object to and from binary. I prefer Hive over SharedPreferences when I need custom objects, encryption, or more than a handful of values."

**Let's understand it fully:**

**Step 1 — Hive vs SharedPreferences at a glance.**

```
  Feature           SharedPreferences      Hive
  ----------------  --------------------   --------------------
  Data types        primitives only        any (via adapters)
  Speed             slower (XML parse)      fast (binary)
  Encryption        no                      yes (AES-256)
  Platform channels yes                     no (pure Dart)
  Lazy loading      no (loads all)          yes (LazyBox)
  Custom objects    JSON workaround         native support
  Best for          simple settings         structured cache
```

**Step 2 — A box = one drawer.**
A box is a named drawer of key-value pairs. You open it, read/write, and it stays open for the app's life. Boxes can be encrypted.

**Step 3 — A TypeAdapter = the translator for your object.**
Hive stores binary, so it needs to know how to turn your `Task` into bytes and back. The `hive_generator` writes that adapter for you.

```dart
import 'package:hive/hive.dart';
part 'task.g.dart'; // generated

@HiveType(typeId: 0) // a unique ID per type — NEVER reuse a number
class Task extends HiveObject {
  @HiveField(0)
  late String title;

  @HiveField(1)
  late bool completed;

  @HiveField(2) // new fields get NEW indices; never change old ones
  late DateTime createdAt;
}
```

**Step 4 — Register the adapter, then open the box.**

```dart
void main() async {
  await Hive.initFlutter();
  Hive.registerAdapter(TaskAdapter()); // generated adapter; before opening boxes
  await Hive.openBox<Task>('tasks');
  runApp(const MyApp());
}
```

**Step 5 — CRUD (create, read, update, delete).**

```dart
final box = Hive.box<Task>('tasks');

// Create
final task = Task()
  ..title = 'Buy groceries'
  ..completed = false
  ..createdAt = DateTime.now();
await box.add(task); // auto-incrementing int key

// Read
final all = box.values.toList();
final first = box.getAt(0);

// Update (HiveObject gives .save())
task.completed = true;
await task.save();

// Delete
await task.delete();
```

**Step 6 — Encrypted box (store the key securely).**

```dart
final key = Hive.generateSecureKey();          // 32 random bytes
// IMPORTANT: keep this key in flutter_secure_storage, not in code (see Q13/Q14)
await Hive.openBox<Task>(
  'secure_tasks',
  encryptionCipher: HiveAesCipher(key),
);
```

**Step 7 — When to choose Hive over SharedPreferences.**
Custom objects, encryption needed, more than ~20 values, large datasets that need lazy loading (`LazyBox`), or you want to avoid platform-channel overhead.

**Why interviewers ask:** To check you choose storage by requirements. Hive fills the gap between "simple settings" (SharedPreferences) and "relational data" (SQLite/Drift).

**Common mistake:** Reusing a `typeId` for a different class, or changing `@HiveField` indices after release — both corrupt stored data. Also forgetting `Hive.registerAdapter(...)` before opening a typed box.

**Follow-ups they may ask:**
- *"Box vs LazyBox?"* → A `Box` keeps all values in memory; a `LazyBox` loads each value from disk only when read — better for large data.
- *"Hive vs Isar?"* → Isar is the newer database from the same author with queries and indexes; mention it to show you're current. (Hive is still widely used and simplest for key-value.)

**Related:** [Q10 — SharedPreferences](#q10) · [Q12 — SQLite/Drift](#q12) · [Q14 — encryption](#q14)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. When do you need SQLite / Drift, and how do you write basic queries in Drift?

> Common · Medium–Hard

**Short answer (say this):**
"I reach for a relational database when data has relationships (users → posts → comments), needs complex queries (joins, grouping, search), or needs transactions. Key-value stores can't efficiently answer 'all orders from the last 7 days grouped by status.' Drift is a reactive, type-safe SQLite wrapper: I define tables as Dart classes and it generates the query API, data classes, and migrations."

**Let's understand it fully:**

**Step 1 — A decision tree.**

```
  Need to store data?
       |
  Simple key-value (settings, flags)?      → SharedPreferences (Q10)
       |
  Structured objects, moderate size,
  no real relationships?                   → Hive (Q11)
       |
  Relationships, joins, complex queries,
  transactions?                            → SQLite / Drift (this question)
```

**Step 2 — Why relational, in plain terms.**
A spreadsheet with linked sheets: "posts" has an `authorId` pointing into "users." A relational database can join them and answer questions across both in one query — something a key-value store can't do efficiently.

**Step 3 — Define tables as Dart classes.**

```dart
import 'package:drift/drift.dart';
part 'database.g.dart'; // generated

class Users extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get name => text().withLength(min: 1, max: 100)();
  TextColumn get email => text().unique()();
  DateTimeColumn get createdAt => dateTime().withDefault(currentDateAndTime)();
}

class Posts extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get title => text()();
  IntColumn get authorId => integer().references(Users, #id)(); // foreign key
  BoolColumn get published => boolean().withDefault(const Constant(false))();
}
```

**Step 4 — The database class and type-safe queries.**

```dart
@DriftDatabase(tables: [Users, Posts])
class AppDatabase extends _$AppDatabase {
  AppDatabase(QueryExecutor e) : super(e);

  @override
  int get schemaVersion => 1;

  Future<List<User>> getAllUsers() => select(users).get();

  Future<User> getUserById(int id) =>
      (select(users)..where((u) => u.id.equals(id))).getSingle();

  // Reactive: emits a new list automatically whenever the table changes
  Stream<List<User>> watchAllUsers() => select(users).watch();

  Future<int> insertUser(UsersCompanion user) => into(users).insert(user);
}
```

**Step 5 — A join (posts with their author's name).**

```dart
Future<List<({Post post, String authorName})>> getPostsWithAuthors() {
  final query = select(posts).join([
    innerJoin(users, users.id.equalsExp(posts.authorId)),
  ]);
  return query.map((row) => (
    post: row.readTable(posts),
    authorName: row.readTable(users).name,
  )).get();
}
```

**Step 6 — A transaction (all-or-nothing).**
A transaction means several writes succeed together or none do — so you never end up half-saved.

```dart
Future<void> createUserWithPost(String name, String email, String title) {
  return transaction(() async {
    final userId = await into(users)
        .insert(UsersCompanion.insert(name: name, email: email));
    await into(posts)
        .insert(PostsCompanion.insert(title: title, authorId: userId));
  });
}
```

**Step 7 — Don't forget migrations.**
When you change the schema (add a column), bump `schemaVersion` and write a `MigrationStrategy`, or existing users' apps crash on the old database.

**Why interviewers ask:** To check you reach for SQLite at the right time — not forcing a key-value store into a relational role, and not using a database for simple settings.

**Common mistake:** Writing raw SQL strings instead of Drift's type-safe API (you lose compile-time checks), or skipping migrations and breaking existing users' local data on a schema change.

**Follow-ups they may ask:**
- *"Drift vs `sqflite`?"* → `sqflite` is the raw SQLite plugin (you write SQL strings). Drift is a typed, reactive layer on top with generated code and `watch()` streams.
- *"What does `watch()` give you?"* → A `Stream` that re-emits whenever the underlying data changes — perfect for a UI that updates automatically (the basis of offline-first, [Q15](#q15)).

**Related:** [Q11 — Hive](#q11) · [Q15 — offline-first](#q15) · [Q14 — SQLCipher](#q14)

[↑ Back to top](#toc)

---

# G. Secure storage & encryption

---

<a id="q13"></a>
## 13. What does `flutter_secure_storage` use under the hood, and when should you use it?

> Very common · Medium

**Short answer (say this):**
"`flutter_secure_storage` is encrypted key-value storage. On iOS it uses the Keychain; on Android it uses the Keystore to make an AES key that encrypts values in EncryptedSharedPreferences. I use it for secrets — auth tokens, refresh tokens, API keys, and the encryption key for Hive. I do *not* use it for large or frequently-read data, because encryption makes it slower than plain SharedPreferences."

**Let's understand it fully:**

**Step 1 — Think of it as a safe, not a drawer.**
SharedPreferences ([Q10](#q10)) is an open drawer — anyone who opens the file reads it. `flutter_secure_storage` is a locked safe whose key is held by the operating system's hardware-backed security. Even on a rooted phone, the contents are encrypted.

**Step 2 — What it uses on each platform.**

```
  Dart API: read / write / delete
       |
       +-------------------+-----------------+
       |                                     |
   iOS                                   Android
   Keychain (hardware-backed)            Keystore makes an AES key
                                              |
                                         EncryptedSharedPreferences
                                         (AES-256 encrypted values)
```

**Step 3 — Use it (and only) for secrets.**

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'dart:convert';

class SecureTokenStorage {
  final _storage = const FlutterSecureStorage(
    aOptions: AndroidOptions(encryptedSharedPreferences: true), // important
    iOptions: IOSOptions(accessibility: KeychainAccessibility.first_unlock),
  );

  Future<void> saveTokens({
    required String accessToken,
    required String refreshToken,
  }) async {
    await _storage.write(key: 'access_token', value: accessToken);
    await _storage.write(key: 'refresh_token', value: refreshToken);
  }

  Future<String?> getAccessToken() => _storage.read(key: 'access_token');

  Future<void> clearAll() => _storage.deleteAll(); // on logout

  // Store the Hive encryption key here (not in code) — links to Q11/Q14
  Future<void> saveHiveKey(List<int> key) =>
      _storage.write(key: 'hive_key', value: base64Encode(key));

  Future<List<int>?> getHiveKey() async {
    final v = await _storage.read(key: 'hive_key');
    return v == null ? null : base64Decode(v);
  }
}
```

**Step 4 — When NOT to use it.**
Large datasets, frequently-accessed data (encryption per read/write is slow), or plain non-sensitive settings. Those belong in SharedPreferences, Hive, or Drift.

**Why interviewers ask:** Storing tokens in plain-text SharedPreferences is a real vulnerability on rooted/jailbroken devices. They want to see you know exactly where secrets belong.

**Common mistake:** Using `flutter_secure_storage` for everything (it's slow). Also forgetting `encryptedSharedPreferences: true` on Android, which can fall back to a weaker implementation on older devices.

**Follow-ups they may ask:**
- *"What's `KeychainAccessibility.first_unlock`?"* → It controls when the value is readable — here, only after the device has been unlocked once since boot (a good balance of security and usability).
- *"Where do you store a Hive/SQLCipher key?"* → Here, in secure storage — never hardcoded in source (see [Q14](#q14)).

**Related:** [Q3 — tokens for auth](#q3) · [Q10 — SharedPreferences](#q10) · [Q14 — encryption](#q14)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. How do you encrypt local data in Flutter?

> Deeper question · Hard

**Short answer (say this):**
"I match the tool to the data. Secrets go in `flutter_secure_storage` (OS keychain/keystore). Structured objects go in an encrypted Hive box (AES-256). Relational data goes in SQLCipher via `sqflite_sqlcipher`. Arbitrary files use the `encrypt` package. The one rule that ties it all together: never hardcode the encryption key — generate it and keep it in secure storage."

**Let's understand it fully:**

**Step 1 — The key is the whole game (a lock-and-key analogy).**
Encrypting data is like locking a box. But if you tape the key to the lid (hardcoding it in code, or saving it in SharedPreferences), the lock is useless. The security depends entirely on where the key lives — and that place is the OS keychain/keystore via `flutter_secure_storage`.

**Step 2 — Pick the layer by data type.**

```
  Data type           Tool                       Encryption
  ------------------  -------------------------  ------------------------
  Secrets / tokens    flutter_secure_storage     Keychain/Keystore (OS)
  Structured objects  Hive encrypted box         AES-256 (key kept secure)
  Relational data     sqflite_sqlcipher          AES-256 on the whole DB
  Arbitrary files     encrypt / pointycastle     AES (manual)
```

**Step 3 — Strategy 1: encrypted Hive box, with the key in secure storage.**

```dart
class EncryptedHiveStorage {
  static const _secure = FlutterSecureStorage();
  static const _keyName = 'hive_aes_key';

  static Future<List<int>> _getOrCreateKey() async {
    final existing = await _secure.read(key: _keyName);
    if (existing != null) return base64Decode(existing);

    final newKey = Hive.generateSecureKey();            // 32 random bytes
    await _secure.write(key: _keyName, value: base64Encode(newKey));
    return newKey;
  }

  static Future<Box<T>> openEncryptedBox<T>(String name) async {
    final key = await _getOrCreateKey();
    return Hive.openBox<T>(name, encryptionCipher: HiveAesCipher(key));
  }
}
```

**Step 4 — Strategy 2: SQLCipher for an encrypted SQLite database.**
The whole database file is encrypted with a password you read from secure storage.

```dart
import 'package:sqflite_sqlcipher/sqflite_sqlcipher.dart';

final db = await openDatabase(
  'app.db',
  password: await secureStorage.read(key: 'db_password'), // from secure storage
  version: 1,
  onCreate: (db, _) => db.execute(
    'CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)',
  ),
);
```

**Step 5 — Strategy 3: manual file encryption with a unique IV.**
For arbitrary files, use the `encrypt` package. The IV (initialization vector) should be **unique per encryption**, and you store it alongside the ciphertext.

```dart
import 'package:encrypt/encrypt.dart' as e;
import 'dart:typed_data';

class FileEncryptor {
  final e.Encrypter _encrypter;
  FileEncryptor(List<int> keyBytes)
      : _encrypter = e.Encrypter(e.AES(e.Key(Uint8List.fromList(keyBytes))));

  ({String cipher, String iv}) encryptText(String plaintext) {
    final iv = e.IV.fromSecureRandom(16); // a NEW random IV each time
    final cipher = _encrypter.encrypt(plaintext, iv: iv).base64;
    return (cipher: cipher, iv: iv.base64); // store both
  }

  String decryptText(String cipher, String ivBase64) =>
      _encrypter.decrypt64(cipher, iv: e.IV.fromBase64(ivBase64));
}
```

**Step 6 — The principles to recite.**
Generate keys at runtime, store them in `flutter_secure_storage`, use a unique IV per operation, and prefer well-known libraries over rolling your own crypto.

**Why interviewers ask:** Data-at-rest encryption is a compliance requirement for health, finance, and government apps. They're testing whether you understand the key-management chain — encryption is only as strong as where the key is stored.

**Common mistake:** Generating a key and saving it in SharedPreferences or hardcoding it in source — then the encryption is theatre, because anyone with device access reads the key. Another mistake: reusing a static IV for AES; each encryption should use a fresh IV.

**Follow-ups they may ask:**
- *"Why a unique IV?"* → A repeated IV with the same key leaks patterns — identical plaintext blocks produce identical ciphertext, which attackers can exploit.
- *"Is the data encrypted in memory too?"* → No — encryption here is "at rest" (on disk). In memory it's plain; that's expected.

**Related:** [Q13 — secure storage](#q13) · [Q11 — encrypted Hive box](#q11) · [Q12 — SQLite](#q12)

[↑ Back to top](#toc)

---

# H. Offline-first & syncing

---

<a id="q15"></a>
## 15. How do you implement an offline-first architecture in Flutter?

> Common · Hard

**Short answer (say this):**
"Offline-first means the local database is the single source of truth for the UI. The app reads from local storage and shows it instantly, then syncs with the server in the background. Writes save locally first (marked 'pending'), the UI updates from the local stream right away, and a background sync pushes changes when the network is back. The UI never waits on the network to show data."

**Let's understand it fully:**

**Step 1 — The key shift: local DB is the truth.**
A normal app asks the server, waits, then shows data (blank screen meanwhile). Offline-first flips it: the UI watches the local database, which always has *something* to show. The network just keeps that local data fresh.

```
  Local DB (source of truth)  →  UI  (UI watches the local DB)
        |
        |  Repository writes to the local DB
        |
  Repository  →  Remote API   (fetch / sync in the background)
```

**Step 2 — The write flow.**

```
  1. User creates an item
  2. Save to local DB immediately (syncStatus = pending)
  3. UI updates instantly (from the local DB stream)
  4. Background: try to push to the server
  5. Success → syncStatus = synced
  6. Failure → keep pending, retry later
```

**Step 3 — A model that carries sync state.**
Each row remembers whether it's been pushed yet.

```dart
enum SyncStatus { pending, synced, failed }

class Task {
  final String id;
  final String title;
  final bool completed;
  final SyncStatus syncStatus;
  final DateTime updatedAt;
  const Task({
    required this.id,
    required this.title,
    required this.completed,
    required this.syncStatus,
    required this.updatedAt,
  });
}
```

**Step 4 — The repository: local first, server second.**

```dart
class TaskRepository {
  final TaskLocalSource _local;   // Drift or Hive
  final TaskRemoteSource _remote; // Dio API client

  // The UI subscribes to THIS — it always reads from the local DB
  Stream<List<Task>> watchTasks() => _local.watchAll();

  Future<void> createTask(String title) async {
    final task = Task(
      id: const Uuid().v4(),        // client-generated id, so it's offline-safe
      title: title,
      completed: false,
      syncStatus: SyncStatus.pending,
      updatedAt: DateTime.now(),
    );
    await _local.insert(task);      // UI updates instantly via the stream

    try {
      await _remote.create(task);
      await _local.updateSyncStatus(task.id, SyncStatus.synced);
    } catch (_) {
      // Stay pending; the SyncManager will retry later
    }
  }

  Future<void> refresh() async {
    try {
      final serverTasks = await _remote.fetchAll();
      await _local.upsertAll(serverTasks); // merge into local DB
    } catch (_) {
      // Offline — the UI still shows local data, no crash
    }
  }
}
```

**Step 5 — A background sync manager.**
When connectivity returns ([Q9](#q9)), push everything still pending.

```dart
class SyncManager {
  final TaskLocalSource _local;
  final TaskRemoteSource _remote;
  final ConnectivityCubit _connectivity;

  void startSync() {
    _connectivity.stream
        .where((s) => s == ConnectivityStatus.online)
        .listen((_) => _pushPending());
  }

  Future<void> _pushPending() async {
    for (final task in await _local.getByStatus(SyncStatus.pending)) {
      try {
        await _remote.upsert(task);
        await _local.updateSyncStatus(task.id, SyncStatus.synced);
      } catch (_) {
        await _local.updateSyncStatus(task.id, SyncStatus.failed);
      }
    }
  }
}
```

**Why interviewers ask:** Offline-first is expected in modern mobile apps. They want to see you can design the local-DB-as-source-of-truth pattern and manage sync state.

**Common mistake:** Making the network call the source of truth and only caching as a fallback. That's "offline-capable," not "offline-first." True offline-first means the UI never waits on the network to display data.

**Follow-ups they may ask:**
- *"Why a client-generated UUID?"* → So you can create items offline with a stable id, before the server ever assigns one — no clash when you sync.
- *"How does the UI update instantly?"* → It watches a local `Stream` (Drift's `watch()` or a Hive listenable); inserting locally emits a new list immediately.

**Related:** [Q9 — connectivity](#q9) · [Q12 — Drift watch()](#q12) · [Q16 — sync strategies](#q16)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. How do you keep local cached data in sync with the server?

> Deeper question · Hard

**Short answer (say this):**
"It depends on the conflict model and data size. The common production choice is timestamp-based delta sync: the client sends its `lastSyncedAt`, the server returns only what changed since then, and the client pushes its pending local changes. The two things that break sync are conflict resolution and non-idempotent pushes, so I plan for both."

**Let's understand it fully:**

**Step 1 — Four strategies, from simple to advanced.**

```
  1. Pull-to-refresh         → client pulls everything on demand; no conflicts.
                               Good for read-heavy, rarely-changing data.

  2. Timestamp delta sync    → client sends lastSyncedAt; server returns only
                               changes since then. Good for moderate data,
                               server is the authority. (Most common.)

  3. Event queue / changelog → client queues each mutation locally, pushes when
                               online; server applies or rejects. Offline-heavy.

  4. CRDT / operational transform → automatic merge via clever data structures.
                               For real-time collaborative editing (complex).
```

**Step 2 — Why delta sync is the usual pick.**
A "what changed since I last looked?" approach. Instead of downloading everything each time (wasteful), the client says "give me changes since 2pm" and the server sends a small list. Cheap on data and battery.

**Step 3 — The two-phase sync: push, then pull.**

```dart
class SyncService {
  final LocalDatabase _local;
  final ApiClient _remote;
  final SharedPreferences _prefs;

  Future<void> sync() async {
    await _pushLocalChanges(); // send my pending edits first
    await _pullRemoteChanges(); // then get everyone else's edits
  }

  Future<void> _pushLocalChanges() async {
    for (final item in await _local.getPending()) {
      try {
        final serverItem = await _remote.upsert(item); // server may adjust it
        await _local.upsert(serverItem.copyWith(syncStatus: SyncStatus.synced));
      } on ConflictException catch (e) {
        // Conflict → server version wins (or ask the user)
        await _local.upsert(e.serverVersion.copyWith(syncStatus: SyncStatus.synced));
      }
    }
  }

  Future<void> _pullRemoteChanges() async {
    final lastSync = _prefs.getString('last_sync_at');
    final changes = await _remote.getChanges(since: lastSync); // delta only

    for (final change in changes) {
      switch (change.type) {
        case ChangeType.upsert:
          await _local.upsert(change.item.copyWith(syncStatus: SyncStatus.synced));
        case ChangeType.delete:
          await _local.delete(change.itemId);
      }
    }
    // Save the new watermark for next time
    await _prefs.setString('last_sync_at', DateTime.now().toUtc().toIso8601String());
  }
}
```

The API contract for the pull looks like:

```
GET /items?since=2026-06-01T00:00:00Z
Response:
{
  "changes": [
    { "type": "upsert", "item": { ... }, "updatedAt": "..." },
    { "type": "delete", "itemId": "abc",  "deletedAt": "..." }
  ]
}
```

**Step 4 — Conflict resolution choices.**
When the same item changed in two places:
- *Last-write-wins:* newest `updatedAt` wins (simple, common).
- *Server-wins:* the server is always right (safe, predictable).
- *Client-wins:* dangerous, rarely used.
- *Manual merge:* show the user both versions (for important data).

**Step 5 — Make pushes idempotent.**
"Idempotent" means doing the same push twice has the same effect as once. This matters because a push can succeed on the server but the local "mark as synced" can fail — so the next sync resends it. Use a stable client id (the UUID from [Q15](#q15)) so the server recognizes the duplicate and doesn't create a second copy.

**Why interviewers ask:** Sync is where most offline architectures fall apart. They want to see you've thought about conflict resolution, partial failures mid-sync, and idempotency.

**Common mistake:** Using `createdAt` instead of `updatedAt` for delta sync — you'd miss every edit. Also non-idempotent pushes: if the local status update fails after a successful push, the next sync duplicates the item unless the server handles it gracefully.

**Follow-ups they may ask:**
- *"What if the device clock is wrong?"* → Prefer server-assigned timestamps or version numbers over the device clock for the watermark.
- *"How do you delete across devices?"* → Use "soft deletes" (a `deletedAt` flag) so the deletion itself is a change that syncs, instead of the row just vanishing.

**Related:** [Q15 — offline-first](#q15) · [Q9 — connectivity trigger](#q9) · [Q12 — local DB](#q12)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. First the quick comparison tables, then the one-line reminders.

## Quick comparison tables

**`http` vs Dio**

| | `http` | Dio |
|---|---|---|
| Setup | manual every call | configure once (`BaseOptions`) |
| Interceptors | no | yes (auth, logging, retry) |
| Cancel / progress | no | yes |
| JSON parsing | manual `jsonDecode` | automatic (`response.data`) |
| Best for | tiny apps, scripts | production apps |

**SharedPreferences vs Hive vs SQLite/Drift vs secure_storage**

| | SharedPreferences | Hive | SQLite / Drift | secure_storage |
|---|---|---|---|---|
| Shape | key-value (primitives) | key-value (objects) | relational tables | key-value (secrets) |
| Encryption | no | yes (AES) | yes (SQLCipher) | yes (OS keychain) |
| Queries / joins | no | no | yes | no |
| Speed | slow (XML) | fast (binary) | fast, indexed | slow (encrypted) |
| Best for | settings, flags | structured cache | relations, complex queries | tokens, keys, PII |

**Timeout types**

| | Meaning | Typical value |
|---|---|---|
| connectTimeout | open the connection | 5–10s |
| receiveTimeout | wait for the response data | match the API (15–60s) |
| sendTimeout | upload the request body | generous for big files |

**Sync strategies**

| Strategy | Use it for |
|---|---|
| Pull-to-refresh | read-heavy, rare changes |
| Timestamp delta sync | moderate data, server authority (most common) |
| Event queue / changelog | offline-heavy apps |
| CRDT / OT | real-time collaborative editing |

## One-line reminders

- **`http`** = manual and minimal; **Dio** = interceptors, cancellation, progress, auto-JSON. Pick Dio for real apps. ([Q1](#q1))
- **connectTimeout** = open the line; **receiveTimeout** = wait for the reply. Retry only on timeouts and 5xx, with backoff. ([Q2](#q2))
- **Interceptors** are airport security: attach the token in `onRequest`, refresh once on 401 with `QueuedInterceptor`, use a separate Dio for the refresh call. ([Q3](#q3))
- **Map every `DioException` type** to a typed `sealed` failure; don't leak raw status codes into widgets. ([Q4](#q4))
- **REST** = many fixed endpoints; **GraphQL** = one endpoint, you pick the fields. GraphQL caching and 200-always errors are the catch. ([Q5](#q5))
- **Either / Result** makes the signature honest: returns **Failure OR data**, so callers must handle both. ([Q6](#q6))
- **JSON**: write `fromJson` by hand only for tiny models; use **`json_serializable`**, or **`freezed`** when you also want immutability + equality + `copyWith`. ([Q7](#q7))
- **Certificate pinning** = trust only *your* key, not any CA. Pin the **public key** and keep a backup pin. ([Q8](#q8))
- **`connectivity_plus`** tells you the interface, not real internet — confirm with a DNS lookup; serve cache on failure. ([Q9](#q9))
- **SharedPreferences** = sticky note for small primitive settings; no encryption, loads the whole file. ([Q10](#q10))
- **Hive** = fast pure-Dart object store; a **box** is a table, a **TypeAdapter** is the translator; never reuse a `typeId`. ([Q11](#q11))
- **SQLite / Drift** = relations, joins, transactions, and reactive `watch()` streams; remember migrations. ([Q12](#q12))
- **`flutter_secure_storage`** = a safe (Keychain/Keystore) for tokens and keys; slow, so secrets only. ([Q13](#q13))
- **Encryption** is only as strong as where the key lives — generate keys, store them in secure storage, use a fresh IV. ([Q14](#q14))
- **Offline-first** = local DB is the source of truth; save locally first (pending), UI updates instantly, sync in the background. ([Q15](#q15))
- **Delta sync** sends `lastSyncedAt` and gets only changes; use `updatedAt`, resolve conflicts, make pushes idempotent. ([Q16](#q16))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers rarely stop at one question. They keep digging to test your depth. Practice answering this chain out loud — calmly, step by step:

1. *"How do you attach an auth token to every request?"* → an interceptor's `onRequest` adds the `Authorization` header.
2. *"What happens when the token expires?"* → the server returns 401; the `onError` hook refreshes the token and retries.
3. *"Three requests get 401 at the same time — what now?"* → use `QueuedInterceptor` so only one refresh runs; the others wait and reuse the new token.
4. *"Where do you store that token?"* → in `flutter_secure_storage` (Keychain/Keystore), never SharedPreferences.
5. *"The app is offline when the user acts — what then?"* → save the change locally as `pending`, show it instantly, and sync when the connection returns.

Being able to calmly go step by step like this — without guessing — is exactly what makes you sound **senior**, in both remote and BD interviews.

[↑ Back to top](#toc)
