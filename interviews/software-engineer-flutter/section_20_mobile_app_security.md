# Section 20 — Mobile & App Security

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. Code/config shown where it helps.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a step-by-step explanation with real examples and code.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For security, name the *threat* first, then the *defense*. "An attacker could read the token from SharedPreferences, so I use secure storage" beats just naming a tool.

---

<a id="toc"></a>

## Table of Contents

**A. Foundations**
1. [OWASP Mobile Top 10](#q1) · *Common*
2. [Encryption at rest vs in transit](#q2) · *Common*

**B. Storing secrets safely**
3. [SharedPreferences vs Secure Storage](#q3) · *Very common*
4. [Never hardcode API keys](#q4) · *Very common*
5. [Don't log sensitive data](#q5) · *Common*

**C. Network security**
6. [Certificate pinning](#q6) · *Common*
7. [Man-in-the-Middle (MITM) attacks](#q7) · *Common*
8. [SQL injection (mobile)](#q8) · *Common*

**D. Authentication**
9. [Access tokens vs refresh tokens](#q9) · *Very common*
10. [OAuth 2.0 + PKCE](#q10) · *Common*
11. [JWT — structure & verification](#q11) · *Very common*
12. [Biometric authentication](#q12) · *Common*

**E. App hardening**
13. [Code obfuscation](#q13) · *Common*
14. [Root / jailbreak detection](#q14) · *Common*
15. [Deep link hijacking](#q15) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The foundations (start here).**
→ [Q1 OWASP Top 10](#q1) · [Q2 At rest vs in transit](#q2)

**Stage 2 — Secrets (most-asked).**
→ [Q3 Secure storage](#q3) · [Q4 API keys](#q4) · [Q5 Logging](#q5)

**Stage 3 — Authentication.**
→ [Q9 Tokens](#q9) · [Q11 JWT](#q11) · [Q10 OAuth/PKCE](#q10) · [Q12 Biometrics](#q12)

**Stage 4 — Network defense.**
→ [Q6 Cert pinning](#q6) · [Q7 MITM](#q7) · [Q8 SQL injection](#q8)

**Stage 5 — App hardening.**
→ [Q13 Obfuscation](#q13) · [Q14 Root detection](#q14) · [Q15 Deep links](#q15)

**Short on time?** Review [Q1](#q1) · [Q3](#q3) · [Q4](#q4) · [Q9](#q9) · [Q11](#q11), then the [Cheat Sheet](#cheatsheet).

---

# A. Foundations

---

<a id="q1"></a>
## 1. What is the OWASP Mobile Top 10?

> Common · Medium

**Short answer (say this):**
"OWASP Mobile Top 10 is the industry-standard list of the most critical security risks in mobile apps. It covers things like insecure data storage, weak authentication, insecure communication, and poor code protection. It's the checklist every mobile security review starts from."

**Let's understand it fully:**

**Step 1 — What it is.**
OWASP (Open Worldwide Application Security Project) publishes a ranked list of the most common, dangerous mobile risks, so teams know what to defend against.

**Step 2 — The main categories (current themes).**

| Risk | In plain words |
|---|---|
| Improper credential usage | hardcoded keys, weak token handling ([Q4](#q4)) |
| Insecure data storage | secrets in plain storage ([Q3](#q3)) |
| Insecure communication | no HTTPS / no pinning ([Q6](#q6), [Q7](#q7)) |
| Insufficient authentication | weak login, no MFA ([Q9](#q9)) |
| Insufficient cryptography | weak or misused encryption ([Q2](#q2)) |
| Insecure authorization | client trusts itself for access checks |
| Poor code quality / tampering | no obfuscation/integrity checks ([Q13](#q13)) |
| Reverse engineering | easy to decompile and read ([Q13](#q13)) |
| Extraneous functionality | leftover debug/test backdoors |

**Step 3 — The recurring lesson.**
Most mobile risks come down to: **don't trust the device**, **protect data at rest and in transit**, and **never put secrets in the app**. The app runs on a device an attacker fully controls.

**Why interviewers ask:** It shows you have a structured view of mobile security, not just random tips.

**Common mistake:** Treating the client as trusted. Anything in the app can be inspected; real security checks must also live on the server.

**Follow-ups they may ask:**
- *"Which is most common in Flutter apps?"* → Insecure data storage and hardcoded secrets — both easy to get wrong.

**Related:** [Q2 — encryption](#q2) · [Q3 — secure storage](#q3) · [Q4 — API keys](#q4)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. What is the difference between encryption at rest and encryption in transit?

> Common · Easy–Medium

**Short answer (say this):**
"Encryption in transit protects data while it moves over the network — that's HTTPS/TLS. Encryption at rest protects data while it's stored on the device or server — like encrypted databases or secure storage. You need both: TLS stops eavesdropping on the wire, and at-rest encryption stops a stolen device leaking data."

**Let's understand it fully:**

**Step 1 — Two different moments to protect.**
- **In transit** — data traveling between app and server (the armored truck on the road).
- **At rest** — data sitting in storage (the locked safe in the building).

**Step 2 — In transit = HTTPS/TLS.**
All network calls must use `https://`. TLS encrypts the data so anyone intercepting the connection sees scrambled bytes, not your tokens or user data.

```dart
// Always HTTPS; never plain http for real data
final res = await dio.get('https://api.example.com/user');
```

**Step 3 — At rest = encrypted storage.**
On the device, sensitive data must be encrypted so a stolen/rooted phone doesn't leak it:
- Tokens/passwords → `flutter_secure_storage` (OS keychain/keystore) ([Q3](#q3)).
- Local databases → encrypt them (e.g. SQLCipher).

**Step 4 — You need BOTH.**
TLS alone doesn't help if the token is then saved in plain text on disk. At-rest encryption alone doesn't help if it's sent over plain HTTP. Defense in depth covers both moments.

**Why interviewers ask:** It tests whether you protect data through its whole lifecycle, not just one part.

**Common mistake:** Using HTTPS but storing the token in plain SharedPreferences — secure on the wire, exposed on the disk.

**Follow-ups they may ask:**
- *"What is TLS?"* → The protocol behind HTTPS that encrypts and authenticates the connection.

**Related:** [Q3 — secure storage](#q3) · [Q6 — certificate pinning](#q6) · [Q7 — MITM](#q7)

[↑ Back to top](#toc)

---

# B. Storing secrets safely

---

<a id="q3"></a>
## 3. Why is SharedPreferences not secure for tokens? How do you use Flutter Secure Storage?

> Very common · Medium

**Short answer (say this):**
"SharedPreferences stores data in plain text — on a rooted Android device or via backups, anyone can read it. So it must never hold tokens, passwords, or personal data. For secrets I use `flutter_secure_storage`, which saves them in the iOS Keychain and Android Keystore/EncryptedSharedPreferences, backed by OS-level encryption."

**Let's understand it fully:**

**Step 1 — Why SharedPreferences is unsafe for secrets.**
It writes to a plain XML/plist file. On a rooted/jailbroken device, or through device backups, that file can be read directly. Fine for a theme setting; never for a token.

**Step 2 — The safe option: flutter_secure_storage.**

```dart
final storage = FlutterSecureStorage();

// Save a token securely
await storage.write(key: 'auth_token', value: token);

// Read it back
final token = await storage.read(key: 'auth_token');

// Delete on logout
await storage.delete(key: 'auth_token');
```

Under the hood it uses the **iOS Keychain** and **Android Keystore** (or EncryptedSharedPreferences) — hardware-backed encryption the OS manages.

**Step 3 — What goes where.**

| Data | Storage |
|---|---|
| Tokens, passwords, PII | `flutter_secure_storage` |
| Theme, language, flags | `SharedPreferences` (fine) |
| Large structured data | encrypted database ([Q2](#q2)) |

**Step 4 — Even secure storage isn't magic.**
A fully compromised (rooted) device can sometimes still be attacked. Combine secure storage with short-lived tokens ([Q9](#q9)) so a leaked token expires fast.

**Why interviewers ask:** Insecure storage is one of the most common mobile vulnerabilities; they check you know where secrets belong.

**Common mistake:** Storing the auth token in SharedPreferences "because it's easy." That's a classic, serious leak.

**Follow-ups they may ask:**
- *"Is secure storage 100% safe?"* → No — it's much stronger, but pair it with short token lifetimes and server-side checks.

**Related:** [Q2 — at rest](#q2) · [Q9 — tokens](#q9) · [Q14 — root detection](#q14)

[↑ Back to top](#toc)

---

<a id="q4"></a>
## 4. Why should you never hardcode API keys in Flutter, and what are the secure alternatives?

> Very common · Medium

**Short answer (say this):**
"Anything compiled into the app can be extracted by decompiling it — a hardcoded key is effectively public. So never put secrets in Dart source or commit them to git. Safer options: pass build-time values with `--dart-define`, keep real secrets on a backend that the app calls, and for truly sensitive keys, never let them touch the client at all."

**Let's understand it fully:**

**Step 1 — Why hardcoding is unsafe.**
A shipped app can be unzipped and decompiled. Strings inside it — including `const apiKey = 'sk_live_...'` — can be read out. It's like writing your password on a public wall.

```dart
// NEVER do this:
const apiKey = 'sk_live_123secret'; // shipped inside the app, extractable
```

**Step 2 — Better: build-time injection with --dart-define.**
Keep keys out of source; pass them at build time (and store them in CI secrets):

```bash
flutter build apk --dart-define=API_KEY=$API_KEY
```

```dart
const apiKey = String.fromEnvironment('API_KEY'); // injected at build
```

This keeps keys out of git, but note: the value is still in the built binary, so it only suits low-sensitivity keys.

**Step 3 — Best: keep real secrets on the server.**
For anything truly sensitive (payment secrets, admin keys), the app should call *your* backend, and the backend holds the secret and talks to the third party. The secret never ships to the device.

```
App → your backend (holds the secret) → third-party API
```

**Step 4 — Also: restrict the keys.**
For keys that must be in the app (e.g. some map/analytics keys), lock them down on the provider side — restrict by app bundle ID, platform, and API scope — so a leaked key is far less useful.

**Why interviewers ask:** Hardcoded secrets are a frequent, serious leak; they want to see you understand the client can't keep secrets.

**Common mistake:** Thinking `--dart-define` or `.env` *hides* the key. It keeps it out of source control, but it's still in the binary — truly sensitive secrets belong on the server.

**Follow-ups they may ask:**
- *"You committed a key — now what?"* → Rotate it immediately (assume it's compromised) and remove it from git history ([Q14 Git](Section_17_Git_Version_Control.md#q14)).

**Related:** [Q1 — OWASP](#q1) · [Q3 — secure storage](#q3) · [Q14 (Git) — .gitignore/secrets](Section_17_Git_Version_Control.md#q14)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. Why is logging sensitive data dangerous, and how do you prevent it?

> Common · Easy–Medium

**Short answer (say this):**
"Logs are often readable on the device, captured by crash tools, or shipped to third-party services — so logging a token, password, or personal data leaks it. The fix: never log secrets, scrub sensitive fields before logging, and disable verbose logging in release builds."

**Let's understand it fully:**

**Step 1 — Why logs leak.**
- Android logcat can be read by other tools on a rooted device.
- Crash reporters (Crashlytics/Sentry) capture logs and send them off-device.
- Logs end up in dashboards many people can see.

```dart
// Dangerous: the token now sits in logs and crash reports
print('Logging in with token: $token');
```

**Step 2 — Prevent it.**
- **Never log** tokens, passwords, full card numbers, or PII.
- **Mask/scrub** sensitive fields before logging:

```dart
String mask(String s) => s.length <= 4 ? '****' : '****${s.substring(s.length - 4)}';
log('Card ending ${mask(cardNumber)}'); // logs ****1234, not the full number
```

**Step 3 — Turn down logging in release.**
Use log levels and disable debug logging in production builds, so verbose logs don't ship.

```dart
if (kDebugMode) log(detailedInfo); // only in debug builds
```

**Step 4 — Configure crash tools to scrub.**
Set up Crashlytics/Sentry to strip sensitive keys before sending, so even accidental logs don't leave the device with secrets.

**Why interviewers ask:** Accidental logging is an easy, common leak; they check you treat logs as a real attack surface.

**Common mistake:** `print`-ing request/response bodies (which contain tokens or PII) during debugging and leaving it in, or shipping verbose logs to production.

**Follow-ups they may ask:**
- *"Where do logs go in production?"* → Crash reporters and analytics — so anything logged can leave the device.

**Related:** [Q3 — secure storage](#q3) · [Q1 — OWASP](#q1)

[↑ Back to top](#toc)

---

# C. Network security

---

<a id="q6"></a>
## 6. What is certificate pinning, why does it matter, and how do you implement it with Dio?

> Common · Medium–Hard

**Short answer (say this):**
"Certificate pinning means the app only trusts a specific, known server certificate (or its public key), instead of any certificate a device trusts. It matters because it defeats man-in-the-middle attacks where an attacker installs a fake trusted certificate. In Flutter with Dio, you check the server's certificate fingerprint against a value baked into the app."

**Let's understand it fully:**

**Step 1 — The problem it solves.**
Normally, an app trusts any certificate signed by a trusted authority. But on a compromised device or network, an attacker can install a fake trusted certificate and silently read your "HTTPS" traffic ([MITM](#q7)). Pinning says "I only trust *this exact* certificate," so the fake one is rejected.

**Step 2 — A real-life picture.**
HTTPS checks "is this a valid ID card?" Pinning checks "is this *the specific person* I expect?" — much stronger.

**Step 3 — Implementing it with Dio.**

```dart
final dio = Dio();
(dio.httpClientAdapter as IOHttpClientAdapter).createHttpClient = () {
  final client = HttpClient();
  client.badCertificateCallback = (cert, host, port) {
    // Compare the server cert's fingerprint to the pinned one
    final fingerprint = sha256.convert(cert.der).toString();
    return fingerprint == expectedFingerprint; // only trust the known cert
  };
  return client;
};
```

(There are also dedicated packages and the `certificate_pinning` approach; the idea is the same — verify against a known value.)

**Step 4 — The trade-off: pin rotation.**
Certificates expire and rotate. If you pin one and it changes, the app breaks until updated. Mitigate by pinning the **public key** (more stable than the cert), pinning a backup key, and having an update path.

**Why interviewers ask:** Pinning is the main defense against MITM and shows network-security depth.

**Common mistake:** Forgetting certificate rotation — the app suddenly can't connect when the server renews its cert. Pin keys and include a backup.

**Follow-ups they may ask:**
- *"Pin the cert or the public key?"* → The public key is usually better — it survives certificate renewals.

**Related:** [Q7 — MITM](#q7) · [Q2 — in transit](#q2)

[↑ Back to top](#toc)

---

<a id="q7"></a>
## 7. What is a Man-in-the-Middle (MITM) attack, and how do you prevent it?

> Common · Medium

**Short answer (say this):**
"A MITM attack is when an attacker secretly sits between the app and the server, reading or changing the traffic — for example on a fake public Wi-Fi. You prevent it with HTTPS everywhere (so traffic is encrypted), certificate pinning (so a fake certificate is rejected), and never trusting user-installed certificates in release."

**Let's understand it fully:**

**Step 1 — A real-life picture: intercepted mail.**
Imagine someone secretly opening, reading, and resealing your letters before they reach you. A MITM attacker does that to your network traffic — you think you're talking to the server, but they're in the middle.

**Step 2 — How it happens.**
- Public/fake Wi-Fi the attacker controls.
- A malicious or fake trusted certificate installed on the device.
- Plain HTTP traffic (no encryption at all).

**Step 3 — The defenses.**
1. **HTTPS everywhere** — encrypt all traffic; never plain HTTP ([Q2](#q2)).
2. **Certificate pinning** — only trust your known certificate, so a fake one fails ([Q6](#q6)).
3. **Don't trust user-added certificates** in release (configure network security to ignore them).
4. **Validate everything server-side** — never rely on the client alone.

**Step 4 — Test it.**
Tools like Charles Proxy or mitmproxy simulate a MITM. A pinned app should *fail* to connect through them — that's how you confirm pinning works.

**Why interviewers ask:** MITM is the classic network attack; they check you know the layered defenses.

**Common mistake:** Assuming HTTPS alone is enough. HTTPS stops casual eavesdropping, but a fake trusted certificate defeats it — pinning is what stops that.

**Follow-ups they may ask:**
- *"How do you test for MITM resistance?"* → Try to proxy the app's traffic; with pinning it should refuse to connect.

**Related:** [Q6 — cert pinning](#q6) · [Q2 — in transit](#q2)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is SQL injection in a mobile context, and how do you prevent it?

> Common · Medium

**Short answer (say this):**
"SQL injection is when untrusted input is concatenated into a SQL query, letting an attacker change what the query does — read or delete data they shouldn't. In a mobile app it can hit a local SQLite database or the backend. You prevent it by always using parameterized queries (placeholders), never building SQL by string concatenation."

**Let's understand it fully:**

**Step 1 — The vulnerability.**
If you paste user input straight into a query, the input can break out and inject its own SQL.

```dart
// DANGEROUS — input is concatenated into the SQL
final name = userInput; // e.g.  ' OR '1'='1
db.rawQuery("SELECT * FROM users WHERE name = '$name'");
// becomes: ... WHERE name = '' OR '1'='1'  → returns everyone
```

**Step 2 — The fix: parameterized queries.**
Use placeholders (`?`) and pass values separately, so input is always treated as data, never as code.

```dart
// SAFE — the value is bound, not concatenated
db.rawQuery('SELECT * FROM users WHERE name = ?', [userInput]);
```

With `sqflite`, the query methods take an `whereArgs` list for exactly this reason:

```dart
db.query('users', where: 'name = ?', whereArgs: [userInput]); // safe
```

**Step 3 — Defense in depth.**
- **Always parameterize** (the main fix).
- **Validate input** (type, length, allowed characters).
- **Least privilege** — the DB user/role can only do what it needs.

**Step 4 — It applies on the backend too.**
The same rule holds for your server's database. Most ORMs parameterize by default — just don't drop down to raw concatenated SQL.

**Why interviewers ask:** It tests a fundamental input-handling habit that applies on device and server.

**Common mistake:** Building SQL with string interpolation (`'$input'`). Always use placeholders.

**Follow-ups they may ask:**
- *"Does this apply to NoSQL?"* → Yes — "NoSQL injection" exists too; never trust raw input in any query.

**Related:** [Q8 (DSA) — none] · [Q12 (Networking) — sqflite/drift](../flutter/section7_networking_local_storage.md#q12)

[↑ Back to top](#toc)

---

# D. Authentication

---

<a id="q9"></a>
## 9. What is the difference between access tokens and refresh tokens? Where do you store them?

> Very common · Medium

**Short answer (say this):**
"An access token is a short-lived key that proves who you are on each API call; a refresh token is a longer-lived key used only to get a new access token when it expires. Short access-token lifetimes limit the damage if one leaks. Both should be stored in secure storage, and when the access token expires, you silently refresh it."

**Let's understand it fully:**

**Step 1 — Two tokens, two jobs.**
- **Access token** — sent with every API request to prove identity. Short-lived (minutes to an hour).
- **Refresh token** — used *only* to obtain a new access token. Longer-lived (days/weeks).

**Step 2 — Why split them.**
If a short-lived access token leaks, it expires fast — limited damage. The longer-lived refresh token is used rarely and only against the auth server, so it's exposed far less.

**Step 3 — Where to store them.**
Both are sensitive → **secure storage** ([Q3](#q3)):

```dart
await storage.write(key: 'access_token', value: access);
await storage.write(key: 'refresh_token', value: refresh);
```

**Step 4 — Handling expiry (silent refresh).**
When an API call returns 401 (token expired), use the refresh token to get a new access token, then retry the original request. A Dio interceptor does this transparently:

```
request → 401 → use refresh token → get new access token → retry original request
```

If the refresh token itself is invalid/expired, force the user to log in again.

**Why interviewers ask:** Token handling is core to every authenticated app; they check you understand the short/long-lived split and secure storage.

**Common mistake:** Using one long-lived token forever (huge blast radius if leaked), or storing tokens in SharedPreferences.

**Follow-ups they may ask:**
- *"Refresh token rotation?"* → Issue a new refresh token each refresh and invalidate the old one, so a stolen refresh token is quickly useless.

**Related:** [Q3 — secure storage](#q3) · [Q11 — JWT](#q11) · [Q3 (Networking) — interceptor/refresh](../flutter/section7_networking_local_storage.md#q3)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. Explain the OAuth 2.0 Authorization Code + PKCE flow for mobile.

> Common · Hard

**Short answer (say this):**
"OAuth 2.0 lets a user log in via a provider (Google, Facebook) without giving the app their password. For mobile, the secure version is Authorization Code with PKCE. PKCE adds a one-time secret the app generates, so even if the authorization code is intercepted, an attacker can't exchange it for tokens without that secret."

**Let's understand it fully:**

**Step 1 — Why PKCE for mobile.**
Mobile apps can't keep a client secret (anyone can decompile the app, [Q4](#q4)). PKCE (Proof Key for Code Exchange) replaces that secret with a fresh, one-time proof generated per login — safe even without a stored secret.

**Step 2 — The flow, step by step.**

```
1. App makes a random 'code_verifier', and a 'code_challenge' = hash(verifier).
2. App opens the provider's login page, sending the code_challenge.
3. User logs in; provider redirects back with an authorization CODE.
4. App exchanges CODE + the original code_verifier for tokens.
5. Provider checks hash(verifier) == challenge → returns access + refresh tokens.
```

**Step 3 — Why interception fails.**
If an attacker steals the authorization code in step 3, they still can't complete step 4 — they don't have the `code_verifier` (it never left the app). The hash binds the code to that one login.

**Step 4 — In Flutter.**
Use a well-tested package (e.g. `flutter_appauth` or the provider's SDK) and the device's secure browser tab — don't hand-roll OAuth or use an embedded webview (which can leak credentials).

**Why interviewers ask:** OAuth/PKCE is the standard secure login for mobile; it tests deeper auth understanding.

**Common mistake:** Using an embedded WebView for the login (insecure, can capture the password) instead of the system browser / a vetted SDK; or trying to store a client secret in the app.

**Follow-ups they may ask:**
- *"Why not the Implicit flow?"* → It returns tokens directly in the redirect (less secure) and is deprecated for mobile; Authorization Code + PKCE is the recommendation.

**Related:** [Q9 — tokens](#q9) · [Q11 — JWT](#q11) · [Q4 — no client secrets](#q4)

[↑ Back to top](#toc)

---

<a id="q11"></a>
## 11. What is a JWT? Explain its structure, how to verify it, and what NOT to store in it.

> Very common · Medium

**Short answer (say this):**
"A JWT (JSON Web Token) is a signed token with three parts: header, payload, and signature, separated by dots. The signature lets the server verify the token wasn't tampered with. Crucially, the payload is only encoded, not encrypted — anyone can read it — so never put secrets or sensitive data in it."

**Let's understand it fully:**

**Step 1 — The three parts.**

```
header.payload.signature

eyJhbGc...  .  eyJzdWIi...  .  SflKxwRJ...
(algorithm)    (claims/data)   (signature)
```

- **Header** — the signing algorithm (e.g. HS256, RS256).
- **Payload** — the claims: user id, roles, expiry (`exp`).
- **Signature** — proves the token is authentic and unchanged.

**Step 2 — How verification works.**
The server re-computes the signature using its secret (or public key) over the header+payload. If it matches the token's signature, the token is genuine and untampered. The server also checks `exp` (not expired).

**Step 3 — The critical point: payload is readable.**
The payload is just Base64-encoded JSON, not encrypted. Anyone can decode it (paste it into jwt.io). So:
- **Never** put passwords, secrets, or sensitive PII in the payload.
- Only put non-secret identity info (user id, roles, expiry).

```
// Decoded payload — anyone can read this:
{ "sub": "user_123", "role": "user", "exp": 1735689600 }   // no secrets!
```

**Step 4 — Practical rules.**
- Keep them **short-lived** (use refresh tokens for longevity, [Q9](#q9)).
- Verify them **server-side** — the app shouldn't trust a JWT it can't verify.
- Store them in **secure storage** ([Q3](#q3)).

**Why interviewers ask:** JWTs are everywhere in auth; the "payload is readable" point is a favourite gotcha.

**Common mistake:** Putting sensitive data in the payload thinking it's hidden — it's only encoded, fully readable. Also, trusting a JWT without verifying its signature.

**Follow-ups they may ask:**
- *"HS256 vs RS256?"* → HS256 uses one shared secret (symmetric); RS256 uses a private/public key pair (the server signs with private, others verify with public).

**Related:** [Q9 — tokens](#q9) · [Q10 — OAuth](#q10) · [Q3 — secure storage](#q3)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. How do you handle biometric authentication in Flutter?

> Common · Medium

**Short answer (say this):**
"Biometrics (fingerprint, Face ID) authenticate the user via the device's secure hardware. In Flutter you use the `local_auth` package, which asks the OS to verify the user. Important: biometrics unlock *local* access — the actual check happens on-device, and you still need server-side auth (tokens) for real security."

**Let's understand it fully:**

**Step 1 — What biometrics do (and don't).**
They confirm "the right person is holding the phone," using the OS's secure enclave. They do **not** replace server authentication — they're a convenient local gate (e.g. to unlock the app or release a stored token).

**Step 2 — Using local_auth.**

```dart
final auth = LocalAuthentication();

final canCheck = await auth.canCheckBiometrics; // is hardware available?

final didAuth = await auth.authenticate(
  localizedReason: 'Authenticate to access your account',
  options: const AuthenticationOptions(biometricOnly: true, stickyAuth: true),
);

if (didAuth) {
  // unlock the app / read the token from secure storage
}
```

**Step 3 — The secure pattern.**
A common, safe design: the user logs in once (server auth → tokens in secure storage), then biometrics gate *access to that stored token* on later opens. The biometric result itself is just a local yes/no.

**Step 4 — Handle the edge cases.**
- No biometrics enrolled → fall back to a PIN/password.
- Biometric check can be bypassed on a rooted device → biometrics alone aren't enough; keep server-side checks.

**Why interviewers ask:** It tests practical mobile auth and the understanding that biometrics are a *local* convenience, not full security.

**Common mistake:** Treating a successful biometric check as full authentication, with no real server-side token/identity behind it.

**Follow-ups they may ask:**
- *"Where is the fingerprint stored?"* → In the device's secure hardware; your app never sees it — it only gets a yes/no.

**Related:** [Q9 — tokens](#q9) · [Q3 — secure storage](#q3)

[↑ Back to top](#toc)

---

# E. App hardening

---

<a id="q13"></a>
## 13. What is code obfuscation, and how do you enable it in Flutter?

> Common · Medium

**Short answer (say this):**
"Obfuscation scrambles your compiled code — renaming classes and methods to meaningless symbols — so it's much harder for someone to decompile and understand your app. In Flutter you enable it with `--obfuscate --split-debug-info` when building release. It raises the bar for reverse engineering, but it's not a substitute for real security."

**Let's understand it fully:**

**Step 1 — What it does.**
A release app can be decompiled. Obfuscation replaces readable names (`AuthService.refreshToken`) with gibberish (`a.b`), so the decompiled code is hard to follow — like shredding the labels on a blueprint.

**Step 2 — Enable it in Flutter.**

```bash
flutter build apk --obfuscate --split-debug-info=build/symbols
flutter build ipa --obfuscate --split-debug-info=build/symbols
```

- `--obfuscate` scrambles the Dart code.
- `--split-debug-info` saves a symbol map so you can still de-obfuscate crash reports. **Keep these symbol files** (privately) for debugging.

**Step 3 — What obfuscation is NOT.**
It makes reverse engineering *harder*, not impossible, and it does **not** hide secrets in the binary ([Q4](#q4)). A determined attacker can still analyze the app. It's one layer, not the whole defense.

**Step 4 — Combine with other layers.**
Pair it with no-hardcoded-secrets, server-side checks, and optionally integrity/root checks ([Q14](#q14)). Defense in depth.

**Why interviewers ask:** It tests practical release hardening and the realistic view that it's a deterrent, not a guarantee.

**Common mistake:** Believing obfuscation hides secrets or makes the app "secure." It raises the effort to reverse engineer; it doesn't protect data the app must contain.

**Follow-ups they may ask:**
- *"Why keep the symbol files?"* → To de-obfuscate (symbolicate) crash reports so stack traces are readable.

**Related:** [Q4 — API keys](#q4) · [Q14 — root detection](#q14)

[↑ Back to top](#toc)

---

<a id="q14"></a>
## 14. What is root / jailbreak detection, and how would you implement basic detection?

> Common · Medium

**Short answer (say this):**
"Root (Android) or jailbreak (iOS) means the device's security controls have been removed, so the OS protections you rely on (like the keystore) are weaker. Detection tries to spot such devices and react — warn the user, limit features, or block sensitive actions. In Flutter you can use packages like `flutter_jailbreak_detection`, but detection can be bypassed, so treat it as one signal, not a guarantee."

**Let's understand it fully:**

**Step 1 — Why it matters.**
On a rooted/jailbroken device, an attacker has deep access — they can read app storage, hook into the app, and bypass some OS protections. For high-security apps (banking, payments) you may want to detect this and reduce risk.

**Step 2 — How basic detection works.**
It looks for tell-tale signs: known root/jailbreak files or apps, the ability to write to protected paths, or suspicious system properties.

```dart
final isCompromised = await FlutterJailbreakDetection.jailbroken;
if (isCompromised) {
  // react: warn, limit features, or block sensitive operations
}
```

**Step 3 — How to react (proportionately).**
- **Banking/payments** — may block or restrict sensitive actions.
- **Most apps** — warn the user and continue with reduced trust.
Decide based on your app's risk level; don't lock out every power user unnecessarily.

**Step 4 — The honest caveat.**
Detection is a **cat-and-mouse game** — a determined attacker can hide root or patch out your check (since the check runs on the device they control). It raises the bar but isn't foolproof. Always keep critical security on the server.

**Why interviewers ask:** It tests realistic threat modeling — knowing both the value and the limits of client-side detection.

**Common mistake:** Trusting root detection as a hard security boundary. It's a signal that can be bypassed; the server must still enforce real security.

**Follow-ups they may ask:**
- *"Can it be bypassed?"* → Yes — the check runs on a device the attacker controls, so they can defeat it; never rely on it alone.

**Related:** [Q3 — secure storage](#q3) · [Q13 — obfuscation](#q13)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. What is deep link hijacking, and how do you secure deep links in Flutter?

> Common · Medium–Hard

**Short answer (say this):**
"Deep link hijacking is when a malicious app registers the same custom URL scheme as yours, so it can intercept links meant for your app — potentially stealing data like an OAuth code. You secure it by using verified App Links (Android) and Universal Links (iOS), which are tied to your domain and can't be claimed by another app, and by never trusting deep-link data without validation."

**Let's understand it fully:**

**Step 1 — The vulnerability with custom schemes.**
Custom schemes like `myapp://` are first-come, first-served — any app can declare it. A malicious app declaring `myapp://` might receive a link (e.g. an OAuth redirect with a code) intended for you.

**Step 2 — The fix: verified links tied to your domain.**
- **Android App Links** and **iOS Universal Links** use real `https://yourdomain.com/...` URLs, verified against a file you host on your domain (`assetlinks.json` / `apple-app-site-association`).
- Because they're tied to a domain you own, another app **can't** claim them.

**Step 3 — Validate the incoming data.**
Treat deep-link parameters as untrusted input:
- Validate and sanitize everything ([Q8](#q8)).
- For OAuth, PKCE ([Q10](#q10)) protects the code even if a link is intercepted.
- Require auth before acting on sensitive deep links (don't perform a money transfer just because a link said so).

**Step 4 — In Flutter.**
Use a router like `go_router` for deep links, configure App Links/Universal Links properly, and add a guard/redirect that checks auth before opening protected destinations.

**Why interviewers ask:** Deep links are a real mobile attack surface; it tests platform-specific security knowledge.

**Common mistake:** Relying on custom URL schemes for sensitive flows (hijackable), or trusting deep-link parameters without validation.

**Follow-ups they may ask:**
- *"App Links vs custom scheme?"* → App/Universal Links are domain-verified (can't be hijacked); custom schemes can be claimed by any app.

**Related:** [Q10 — OAuth/PKCE](#q10) · [Q8 — input validation](#q8) · [Q4 (Navigation) — deep linking](../flutter/section4_navigation_and_routing.md#q1)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## Threat → defense

| Threat | Defense |
|---|---|
| Stolen device reads token | secure storage ([Q3](#q3)) |
| Extracted hardcoded key | keep secrets on server ([Q4](#q4)) |
| Eavesdropping on network | HTTPS + cert pinning ([Q6](#q6)) |
| Fake certificate (MITM) | certificate pinning ([Q6](#q6), [Q7](#q7)) |
| Leaked long-lived token | short access + refresh tokens ([Q9](#q9)) |
| Reverse engineering | obfuscation ([Q13](#q13)) |
| Hijacked deep link | App/Universal Links ([Q15](#q15)) |
| SQL injection | parameterized queries ([Q8](#q8)) |

## At rest vs in transit

| | In transit | At rest |
|---|---|---|
| Protects | data moving over network | data stored on device |
| How | HTTPS/TLS | secure storage / encrypted DB |

## One-line reminders

- **Don't trust the client** — anything in the app can be inspected; enforce on the server. ([Q1](#q1))
- **Encrypt in transit (HTTPS) AND at rest (secure storage)** — need both. ([Q2](#q2))
- **SharedPreferences = plain text**; use `flutter_secure_storage` for secrets. ([Q3](#q3))
- **Never hardcode secrets** — they ship in the binary; keep real ones on the server. ([Q4](#q4))
- **Never log tokens/PII**; scrub and disable verbose logs in release. ([Q5](#q5))
- **Certificate pinning** defeats MITM by trusting only your known cert/key. ([Q6](#q6), [Q7](#q7))
- **Always parameterize SQL** (`?` + args); never concatenate input. ([Q8](#q8))
- **Short access token + refresh token**; both in secure storage; silent refresh on 401. ([Q9](#q9))
- **OAuth + PKCE** for mobile login; use the system browser, not a webview. ([Q10](#q10))
- **JWT payload is readable** (only encoded) — no secrets inside; verify server-side. ([Q11](#q11))
- **Biometrics = local gate**, not full auth; keep server-side tokens. ([Q12](#q12))
- **Obfuscation** raises the bar but doesn't hide secrets. ([Q13](#q13))
- **Root detection** is a signal, not a guarantee — it can be bypassed. ([Q14](#q14))
- **Use App/Universal Links** (domain-verified) so deep links can't be hijacked. ([Q15](#q15))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Security interviews probe the threat behind the tool. Practice out loud:

1. *"Where do you store the auth token?"* → secure storage (Keychain/Keystore), never SharedPreferences, with short token lifetimes.
2. *"You're using HTTPS — is that enough?"* → no; a fake trusted cert defeats it. Add certificate pinning.
3. *"Can you hide an API key in the app?"* → no; the binary can be read. Keep real secrets on the server.
4. *"A JWT carries the user's role — safe to trust on the client?"* → verify server-side; the payload is readable and the client is untrusted.
5. *"How do you secure your OAuth redirect on mobile?"* → Authorization Code + PKCE + App/Universal Links so an intercepted code is useless.

Naming the *threat* and then the *layered defense* — and stressing "don't trust the client" — is exactly the senior signal, in both remote and BD interviews.

[↑ Back to top](#toc)
