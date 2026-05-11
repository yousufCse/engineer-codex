# 📘 CHAPTER 9 — Authentication ও Authorization
### "পরিচয় নিশ্চিতকরণ এবং অনুমতি — JWT থেকে OAuth পর্যন্ত"
#### Progress: [██████████░░░░░░░░░] 50%

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 8](./chapter-08-mongoose.md) | [➡ Ch 10](./chapter-10-validation.md)

---

## Authentication vs Authorization

এই দুটো concept প্রায়ই গুলিয়ে ফেলা হয় — কিন্তু এগুলো আলাদা।

**Authentication (প্রমাণীকরণ):** "তুমি কে?" — ব্যবহারকারীর পরিচয় নিশ্চিত করা। Username/password দিয়ে login করা authentication।

**Authorization (অনুমোদন):** "তুমি কী করতে পারো?" — authenticated ব্যবহারকারীর কী access আছে সেটা নির্ধারণ। Admin সব কিছু করতে পারে, regular user শুধু নিজের data দেখতে পারে।

Authentication সবসময় Authorization-এর আগে আসে — পরিচয় না জানলে অনুমতি দেওয়া অসম্ভব।

---

## Session-based vs Token-based Authentication

**Session-based Authentication (Traditional):**

User login করলে server একটা session তৈরি করে এবং session ID browser-এর cookie-তে পাঠায়। পরের প্রতিটা request-এ browser সেই cookie পাঠায়, server session store-এ (memory বা database) session খোঁজে এবং user identify করে।

সমস্যা: Server stateful — প্রতিটা session server-এ সংরক্ষণ। Multiple server থাকলে session sharing দরকার (Redis)। Horizontal scaling জটিল।

**Token-based Authentication (Modern):**

User login করলে server একটা token তৈরি করে এবং client-এ পাঠায়। Client পরের প্রতিটা request-এ token পাঠায় (`Authorization: Bearer <token>` header)। Server token verify করে user identify করে — token type অনুযায়ী local verification বা lookup/introspection ব্যবহার হতে পারে।

সুবিধা: Stateless architecture সহজ হয়। Multiple server-এ একই signing/verification strategy ব্যবহার করে token verify করা যায়। Mobile app, third-party API-তে ভালো।

**গুরুত্বপূর্ণ nuance:** সব token database lookup ছাড়া verify করা যায় না। Self-contained token (যেমন signed JWT) অনেক ক্ষেত্রে local verification-এ কাজ করে, কিন্তু opaque/reference token হলে introspection বা token store lookup দরকার হতে পারে।

---

## JWT — JSON Web Token

JWT হলো token-based authentication-এর সবচেয়ে জনপ্রিয় standard।

একটা JWT তিনটা অংশ দিয়ে গঠিত — dot দিয়ে আলাদা:

**Header:** Algorithm এবং token type। Base64URL encoded।
```
{ "alg": "HS256", "typ": "JWT" }
```

**Payload:** Claims — user information এবং token metadata। Base64URL encoded।
```
{ "sub": "user123", "name": "Alice", "iat": 1700000000, "exp": 1700003600 }
```

**Signature:** Header এবং Payload-এর উপর secret key দিয়ে cryptographic signature।

**JWT কীভাবে কাজ করে:**

Server token তৈরির সময় header + payload + key দিয়ে signature তৈরি করে। Client token পাঠালে server signature verify করে claims (exp, nbf, aud, iss ইত্যাদি) validate করে। JWT flow-এ প্রায়ই DB lookup এড়ানো যায়, কিন্তু revocation/listing, session policy, অথবা opaque token model থাকলে lookup লাগতে পারে।

**জরুরি সতর্কতা:** Payload Base64URL encoded — encrypted নয়। যে কেউ payload decode করে content দেখতে পারে। Sensitive information (password, credit card) payload-এ রাখা উচিত নয়।

---

## JWT Signing Algorithms

**HS256 (HMAC-SHA256):** Symmetric। একটাই secret key — sign করতে এবং verify করতে। Simple কিন্তু secret সব service-এ share করতে হয়।

**RS256 (RSA-SHA256):** Asymmetric। Private key দিয়ে sign, public key দিয়ে verify। Auth service private key রাখে। অন্য service public key দিয়ে verify করতে পারে — private key share করতে হয় না।

প্র্যাক্টিক্যালি RS256/ES256-এর মতো asymmetric signing অনেক distributed system-এ সুবিধা দেয়, তবে “সব ক্ষেত্রে best” নয় — key management, performance, trust boundary, এবং architecture অনুযায়ী algorithm নির্বাচন করা উচিত।

---

## Access Token + Refresh Token Pattern

JWT-এর একটা সমস্যা — token revoke করা কঠিন। Token valid থাকাকালীন user কোনো কারণে block করলেও token দিয়ে access পাবে।

এই সমস্যার সমাধান: Short-lived access token + Long-lived refresh token।

**Access Token:** Short expiry (15 minutes - 1 hour)। API call-এ এটাই পাঠানো হয়। Expire হলে নতুন token দরকার।

**Refresh Token:** Long expiry (7-30 days)। Database-এ সংরক্ষণ। নতুন access token নিতে ব্যবহার।

নোট: এই durationগুলো fixed standard নয়; product risk, device trust, compliance policy, এবং threat model অনুযায়ী পরিবর্তন হয়।

**Flow:**
1. Login করলে access token + refresh token পাওয়া যায়।
2. API call-এ access token পাঠানো হয়।
3. Access token expire হলে refresh token দিয়ে নতুন access token নেওয়া হয়।
4. Logout করলে refresh token database থেকে delete করা হয় — এরপর আর নতুন access token নেওয়া যাবে না।

**Token Rotation:** প্রতিবার refresh করলে নতুন refresh token দেওয়া এবং পুরনোটা invalidate করা — refresh token চুরি হলেও সীমিত ক্ষতি।

---

## bcrypt — Password Hashing

Password কখনো plain text-এ সংরক্ষণ করা উচিত নয়। Database leak হলে সব ব্যবহারকারীর password ফাঁস।

Hash করলেও SHA-256 বা MD5 যথেষ্ট নয় — এগুলো দ্রুত। Attacker GPU দিয়ে প্রতি সেকেন্ডে বিলিয়ন hash calculate করতে পারে।

**bcrypt কেন ভালো:**

**Slow by design:** bcrypt ইচ্ছাকৃতভাবে ধীর — brute force attack কঠিন। Cost factor দিয়ে speed control করা যায়।

**Salt:** Random string যেটা password-এর সাথে যোগ করে hash করা হয়। এর ফলে একই password-এর আলাদা hash হয়। Rainbow table attack (pre-computed hash lookup) defeat করে।

**Cost Factor:** Work factor বা rounds। bcrypt লগারিদমিক — cost 10 মানে 2^10 = 1024 rounds। Cost 11 মানে 2^11 = 2048। প্রতি unit বাড়ালে computation দ্বিগুণ। Hardware দ্রুত হলে cost বাড়ানো যায়।

Production-এ cost 10-12 সাধারণত ভালো balance।

---

## OAuth 2.0 Overview

OAuth 2.0 হলো third-party authorization protocol। "Google দিয়ে login" বা "Facebook দিয়ে login" OAuth দিয়ে হয়।

Core idea: User তাদের password third-party app-কে না দিয়ে Google/Facebook-এ login করে এবং সীমিত permission grant করে।

**চারটা Roles:**
- Resource Owner: User।
- Client: আমাদের application।
- Authorization Server: Google, GitHub — token issue করে।
- Resource Server: Google API, GitHub API — protected resource।

**Authorization Code Flow:** Most secure। User Authorization Server-এ redirect, login করে permission দেয়। Authorization Code পাওয়া যায়। Code দিয়ে Access Token নেওয়া হয় (server-to-server, client-এ code না)।

**Authorization Code Flow (Modern recommendation):** Authorization Code + PKCE সবচেয়ে বেশি recommended pattern। User Authorization Server-এ redirect হয়, login/consent দেয়, তারপর browser redirect-এর মাধ্যমে client redirect endpoint-এ authorization code আসে। এরপর backend token endpoint-এ code exchange করে access token নেয় (back-channel)।

অর্থাৎ code front-channel-এ আসে, কিন্তু access token token endpoint থেকে secure back-channel-এ নেওয়া হয়।

আরও গুরুত্বপূর্ণ: modern security guidance অনুযায়ী Implicit flow এবং Resource Owner Password Credentials flow নতুন implementation-এ এড়ানো উচিত।

---

## Common Auth Vulnerabilities

**Brute Force Attack:** অনেক password try করা। Rate limiting এবং account lockout দিয়ে defend।

**Credential Stuffing:** অন্য site-এর leaked username/password দিয়ে try। Strong hashing এবং MFA।

**JWT Algorithm Confusion:** `alg: none` attack — verify না করে token accept। Library-তে expected algorithm explicit করতে হবে।

**Token Leakage:** HTTPS ব্যবহার না করলে token intercepted। সবসময় HTTPS।

**Bearer Token in URL:** Access token query string-এ পাঠানো উচিত নয়। Header (Authorization: Bearer) বা নির্দিষ্ট নিরাপদ method ব্যবহার করতে হবে, কারণ URL browser history, logs, proxy-তে leak হতে পারে।

---

## মূল উপলব্ধি

Authentication এবং Authorization backend security-র ভিত্তি। JWT-এর payload public — sensitive data রাখা যাবে না। Short-lived access token + refresh token pattern ব্যাপকভাবে ব্যবহৃত এবং refresh rotation/security controls যোগ করলে ঝুঁকি কমে। bcrypt-এর cost factor hardware-এর সাথে তাল মিলিয়ে adjust করতে হবে। OAuth social login-এর জন্য কার্যকর, তবে OAuth 2.0 security best practice (PKCE, HTTPS, strict redirect validation, query-তে token না পাঠানো) মানা বাধ্যতামূলক।

---

## JWT Structure — বিস্তারিত

JWT একটা compact, URL-safe token format (RFC 7519)। তিনটা অংশ Base64URL encode করে dot দিয়ে জোড়া দেওয়া হয়:

```
ASCII Diagram — JWT Structure

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIiwibmFtZSI6IkFsaWNlIiwiaWF0IjoxNzAwMDAwMDAwLCJleHAiOjE3MDAwMDM2MDB9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
│─────────────────────────────────────────────│─────────────────────────────────────────────────────────────────────────────────────────────────────────│────────────────────────────────────────────│
              HEADER (Base64URL)                                              PAYLOAD (Base64URL)                                                    SIGNATURE
     { "alg": "HS256", "typ": "JWT" }          { "sub": "user123", "name": "Alice", "iat": 1700000000, "exp": 1700003600 }         HMAC_SHA256(header + "." + payload, secret)
```

### Header

Header দুটো field রাখে:
- `alg` — signing algorithm (যেমন `HS256`, `RS256`, `ES256`)
- `typ` — token type, সাধারণত `"JWT"`

### Payload — Claims

Payload-এ **claims** থাকে। Claims তিন ধরনের:

**Registered claims (RFC 7519 Section 4.1):**

| Claim | পূর্ণ নাম | অর্থ |
|-------|-----------|------|
| `iss` | Issuer | কোন server token তৈরি করেছে |
| `sub` | Subject | Token কার জন্য (সাধারণত user ID) |
| `aud` | Audience | Token কোন service-এর জন্য |
| `exp` | Expiration Time | Token কখন expire হবে (Unix timestamp) |
| `nbf` | Not Before | এর আগে token valid নয় |
| `iat` | Issued At | কখন token তৈরি হয়েছে |
| `jti` | JWT ID | Unique identifier (replay attack এড়াতে) |

**Public claims:** IANA JWT Claims Registry-তে register করা বা collision-resistant নাম।

**Private claims:** দুই party-র মধ্যে agreed custom claims (যেমন `role`, `permissions`)।

> ⚠️ **Critical:** Payload Base64URL encoded — এটা **encryption নয়**। যে কেউ header এবং payload decode করে পড়তে পারবে। Password, credit card number, বা যেকোনো sensitive data payload-এ রাখা নিরাপদ নয়।

### Signature

Signature তৈরি হয় এভাবে (HS256 এর ক্ষেত্রে):

```
HMAC_SHA256(
  base64url(header) + "." + base64url(payload),
  secret_key
)
```

RS256-এর ক্ষেত্রে `RSASSA-PKCS1-v1_5` algorithm দিয়ে private key ব্যবহার করে sign হয় এবং public key দিয়ে verify হয়।

Signature-এর কাজ: token tamper করা হয়েছে কিনা detect করা এবং issuer authentic কিনা নিশ্চিত করা। Signature valid হলেও payload public — confidentiality আসে না।

---

## JWT Verification — সঠিক পদ্ধতি

RFC 8725 (JWT Best Current Practices) অনুযায়ী token verify করার সময় নিচের steps follow করতে হবে:

1. **Algorithm check:** Token header-এর `alg` value অন্ধভাবে বিশ্বাস করা যাবে না। Server-এ expected algorithm explicitly configure করতে হবে।
2. **`alg: none` reject:** RFC 8725 অনুযায়ী `alg: none` সবসময় reject করতে হবে।
3. **Signature verify:** Configured algorithm এবং key দিয়ে signature validate।
4. **Claims validate:**
   - `exp` — token expire হয়নি?
   - `nbf` — token এখন valid?
   - `iss` — expected issuer?
   - `aud` — token এই service-এর জন্য?
5. **Token type check:** RFC 8725 recommends typed tokens যাতে এক context-এর token অন্য context-এ misuse না হয়।

---

## JWT Signing Algorithms — বিস্তারিত তুলনা

| Algorithm | Type | Key | ব্যবহার |
|-----------|------|-----|---------|
| `HS256` | Symmetric (HMAC) | একটাই shared secret | Simple setup, একাধিক service থাকলে secret share করতে হয় |
| `HS384` | Symmetric (HMAC) | একটাই shared secret | HS256-এর মতো, বড় hash |
| `HS512` | Symmetric (HMAC) | একটাই shared secret | HS256-এর মতো, আরও বড় hash |
| `RS256` | Asymmetric (RSA) | Private key (sign) + Public key (verify) | Auth server private key রাখে; অন্য service public key-এ verify করে |
| `RS384` | Asymmetric (RSA) | Private key + Public key | RS256-এর মতো |
| `RS512` | Asymmetric (RSA) | Private key + Public key | RS256-এর মতো |
| `ES256` | Asymmetric (ECDSA) | Private key (sign) + Public key (verify) | RS256-এর মতো সুবিধা, ছোট key size, দ্রুত |
| `PS256` | Asymmetric (RSASSA-PSS) | Private key + Public key | RSA-এর আরও secure variant |

**কোনটা বেছে নেবে?**

- Single monolith বা trusted microservices — HS256 যথেষ্ট হতে পারে, তবে secret management সাবধানে করতে হবে।
- Distributed system, multiple teams, বা public JWKS endpoint দরকার — RS256 বা ES256 বেছে নাও। ES256 ছোট token এবং দ্রুত operation দেয়।
- `alg: none` কখনোই accept করা যাবে না।

---

## OAuth 2.0 — সম্পূর্ণ বিবরণ

### OAuth 2.0 কী এবং কেন?

OAuth 2.0 (RFC 6749) হলো একটা **authorization framework** — authentication protocol নয়। এটা third-party application-কে resource owner-এর behalf-এ limited access দেওয়ার standard পদ্ধতি।

উদাহরণ: একটা photo-editing app তোমার Google Drive-এর photos access করতে চায়। তোমার Google password সেই app-কে না দিয়ে, তুমি Google-এ login করো এবং শুধু "Drive photos read" permission approve করো। Google একটা token দেয় — app সেটা দিয়ে শুধু photos access করতে পারে, inbox না।

### OAuth 2.0 Roles (RFC 6749 Section 1.1)

| Role | বিবরণ | উদাহরণ |
|------|-------|---------|
| Resource Owner | যার data | তুমি (user) |
| Client | যে app access চায় | Photo-editing app |
| Authorization Server | token issue করে | Google OAuth server |
| Resource Server | protected resource রাখে | Google Drive API |

Authorization Server এবং Resource Server একই সার্ভার হতে পারে বা আলাদা হতে পারে।

### OAuth 2.0 Endpoints (RFC 6749)

- **Authorization Endpoint:** Client user-কে এখানে redirect করে authorization চাইতে। Authorization Server এটা operate করে।
- **Token Endpoint:** Client এখানে code exchange করে token নেয়। Server-to-server (back-channel) communication।
- **Redirect URI:** Authorization পরে Authorization Server user-কে Client-এর এই URL-এ redirect করে।

---

## Authorization Code Flow + PKCE — সম্পূর্ণ ব্যাখ্যা

Authorization Code Flow হলো OAuth 2.0-এর সবচেয়ে secure এবং widely recommended grant type। PKCE (Proof Key for Code Exchange, RFC 7636) এর সাথে যোগ করলে public client-এও নিরাপদ।

RFC 9700 এবং OAuth 2.1 draft অনুযায়ী সমস্ত client-এর জন্য PKCE ব্যবহার করা recommended।

### Mermaid Sequence Diagram — Authorization Code + PKCE Flow

```mermaid
sequenceDiagram
    participant User as User (Browser)
    participant Client as Client App
    participant AuthServer as Authorization Server
    participant ResServer as Resource Server

    User->>Client: "Google দিয়ে login" click
    Client->>Client: code_verifier তৈরি (random, 43-128 chars)<br/>code_challenge = BASE64URL(SHA256(code_verifier))
    Client->>User: Redirect to Authorization Server<br/>?response_type=code&client_id=...&redirect_uri=...&code_challenge=...&scope=...
    User->>AuthServer: Redirect হয়ে যায়
    AuthServer->>User: Login page / Consent screen
    User->>AuthServer: Credentials দেয়, permission approve করে
    AuthServer->>User: Redirect to redirect_uri?code=AUTH_CODE&state=...
    User->>Client: Browser redirect করে, Client পায় AUTH_CODE
    Note over Client,AuthServer: Back-channel (server-to-server)
    Client->>AuthServer: POST /token<br/>code=AUTH_CODE&code_verifier=...&grant_type=authorization_code
    AuthServer->>AuthServer: SHA256(code_verifier) == code_challenge? ✓
    AuthServer->>Client: { access_token, refresh_token, expires_in }
    Client->>ResServer: GET /userinfo<br/>Authorization: Bearer access_token
    ResServer->>Client: User data
```

### ASCII Diagram — Authorization Code Flow (সরলীকৃত)

```
┌──────────┐          ┌─────────────┐        ┌──────────────────────┐        ┌───────────────┐
│  Browser │          │  Client App │        │ Authorization Server  │        │Resource Server│
└────┬─────┘          └──────┬──────┘        └──────────┬───────────┘        └───────┬───────┘
     │                       │                          │                             │
     │  Click "Login"        │                          │                             │
     │──────────────────────>│                          │                             │
     │                       │ Generate code_verifier   │                             │
     │                       │ code_challenge=SHA256(v) │                             │
     │  Redirect (front-ch.) │                          │                             │
     │<──────────────────────│                          │                             │
     │ Browser → Auth Server │                          │                             │
     │──────────────────────────────────────────────────>                             │
     │                       │                          │ Show Login/Consent          │
     │<──────────────────────────────────────────────────                             │
     │  User logs in, approves                          │                             │
     │──────────────────────────────────────────────────>                             │
     │                       │                          │                             │
     │  Redirect ?code=CODE  │                          │                             │
     │<──────────────────────────────────────────────────                             │
     │  (front-channel)      │                          │                             │
     │  Browser → Client     │                          │                             │
     │──────────────────────>│                          │                             │
     │                       │  POST /token (back-ch.)  │                             │
     │                       │  code + code_verifier    │                             │
     │                       │─────────────────────────>│                             │
     │                       │                          │ Verify PKCE ✓               │
     │                       │  { access_token,         │                             │
     │                       │    refresh_token }       │                             │
     │                       │<─────────────────────────│                             │
     │                       │                          │                             │
     │                       │  GET /resource           │                             │
     │                       │  Authorization: Bearer…  │                             │
     │                       │──────────────────────────────────────────────────────>│
     │                       │                          │            Resource data    │
     │                       │<──────────────────────────────────────────────────────│
     │                       │                          │                             │
```

### PKCE কেন দরকার?

PKCE ছাড়া Authorization Code Flow-এ একটা attack সম্ভব: যদি attacker কোনোভাবে authorization code intercept করে (malicious redirect, log leak), সে সেই code দিয়ে token নিতে পারে। PKCE এটা prevent করে কারণ token endpoint-এ `code_verifier` লাগে যেটা শুধু original client জানে।

---

## Refresh Token Flow

```mermaid
sequenceDiagram
    participant Client as Client App
    participant AuthServer as Authorization Server

    Client->>AuthServer: POST /token<br/>grant_type=refresh_token&refresh_token=OLD_RT
    AuthServer->>AuthServer: Validate refresh token (DB check)
    AuthServer->>Client: { access_token: NEW_AT, refresh_token: NEW_RT }
    Note over AuthServer: OLD_RT invalidated (rotation)
```

**Refresh Token Rotation:** প্রতিবার refresh করলে নতুন refresh token দেওয়া হয় এবং পুরনোটা invalidate হয়। যদি কোনো পুরনো refresh token reuse হয় (attacker use করছে), server detect করতে পারে এবং সব token revoke করতে পারে। এটা **refresh token theft** এর বিরুদ্ধে protection।

---

## Session vs JWT vs OAuth — তুলনা

এই তিনটা concept আলাদা layer-এ কাজ করে এবং often একসাথে ব্যবহৃত হয়।

| বিষয় | Session | JWT | OAuth 2.0 |
|-------|---------|-----|-----------|
| **কী?** | Server-side state identifier | Self-contained signed token | Authorization delegation framework |
| **উদ্দেশ্য** | User-কে authenticated রাখা | Stateless authentication/claims বহন | Third-party access delegation |
| **State** | Server-side (session store) | Client-side (token-এ সব তথ্য) | Server-side (token store) |
| **Scalability** | Sticky session বা shared store লাগে | Signing key share হলে যেকোনো server verify করতে পারে | Authorization Server centralized |
| **Revocation** | Session delete করলেই হয় | Difficult — expiry না হওয়া পর্যন্ত valid থাকে; revocation list বা short expiry দরকার | Token revocation endpoint থাকতে পারে |
| **Storage (client)** | Cookie (session ID) | Cookie বা localStorage | Access token: memory/cookie; Refresh token: httpOnly cookie |
| **Token size** | ছোট (ID only) | বড় (claims সহ) | Variable |
| **Use case** | Traditional web app | API authentication, microservices | Social login, third-party API access |
| **Standard** | কোনো formal RFC নেই | RFC 7519 | RFC 6749 |

> **গুরুত্বপূর্ণ:** OAuth 2.0 authentication protocol নয় — এটা authorization framework। Authentication-এর জন্য OAuth-এর উপরে **OpenID Connect (OIDC)** protocol ব্যবহার করা হয় যা JWT-ভিত্তিক `id_token` দেয়।

---

## OpenID Connect (OIDC) — সংক্ষিপ্ত পরিচিতি

OpenID Connect (OIDC) হলো OAuth 2.0-এর উপরে নির্মিত একটা **authentication layer**। OAuth 2.0 শুধু "access দাও" বলে — কিন্তু "কে login করছে" জানায় না। OIDC এই gap পূরণ করে।

**OIDC কী যোগ করে OAuth 2.0-এর উপরে:**

- **`id_token`:** একটা JWT যেটা user-এর identity information বহন করে (`sub`, `email`, `name` ইত্যাদি)।
- **`/userinfo` endpoint:** User information নেওয়ার standard endpoint।
- **Standard scopes:** `openid` (required), `profile`, `email`, `address`, `phone`।

"Google দিয়ে login" — যখন `openid` scope সহ OAuth flow চালাও, আসলে OIDC চলছে। Google একটা `id_token` (JWT) দেয় যেটা থেকে user-এর identity জানা যায়।

```
OAuth 2.0 alone  →  "এই token দিয়ে Google Calendar access করো"
OIDC (OAuth + id_token)  →  "এই token দিয়ে Google Calendar access করো" + "এই user হলো alice@example.com"
```

---

## JWT vs OAuth 2.0 vs Session — কোনটা কখন?

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  প্রশ্ন: তোমার কী দরকার?                                                    │
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  নিজের app-এর user authentication (login/logout)?                    │   │
│  │                                                                       │   │
│  │  Traditional web app?  ──────────────────────────>  Session + Cookie │   │
│  │                                                                       │   │
│  │  SPA / Mobile / API?   ──────────────────────────>  JWT (short-lived)│   │
│  │                                                    + Refresh Token   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  Third-party বা external service-এর resource access দরকার?           │   │
│  │  (Google, GitHub, Spotify)                                           │   │
│  │                                                                       │   │
│  │  ──────────────────────────────────────────────>  OAuth 2.0          │   │
│  │                                                   (+OIDC for login)  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Password Hashing — bcrypt vs Argon2id vs scrypt vs PBKDF2

Password plain text বা fast hash (MD5, SHA-256) দিয়ে store করা যাবে না। GPU brute force attack থেকে রক্ষার জন্য **slow, memory-hard** hashing algorithm দরকার।

OWASP Password Storage Cheat Sheet অনুযায়ী:

| Algorithm | OWASP Recommendation | বৈশিষ্ট্য | সমস্যা |
|-----------|---------------------|-----------|---------|
| **Argon2id** | ✅ Primary recommendation | Memory-hard + CPU-hard, resistant to GPU/ASIC | নতুন, সব পুরনো library-তে নেই |
| **scrypt** | ✅ Alternative | Memory-hard | Parameter tuning জটিল |
| **bcrypt** | ✅ Legacy option (যদি Argon2 না পাও) | Proven, widely supported | **72-byte input limit** (node.bcrypt.js-এ confirmed); ASIC-resistant কিন্তু memory-hard নয় |
| **PBKDF2** | ✅ যদি FIPS compliance লাগে | FIPS 140 approved | GPU attack-এ অপেক্ষাকৃত vulnerable |
| **MD5** | ❌ Never | Fast | Seconds-এ crack হয় |
| **SHA-256** | ❌ Never (password hashing-এ) | Fast | Seconds-এ crack হয় |

### bcrypt-এর 72-byte limit

`node.bcrypt.js` এবং সব standard bcrypt implementation-এ password input **72 bytes**-এ truncate হয়। অর্থাৎ 72 bytes-এর বেশি দীর্ঘ password দিলেও শুধু প্রথম 72 bytes hash হয়। OWASP এটা note করেছে এবং suggest করে যদি দীর্ঘ password support করতে চাও তাহলে bcrypt-এর আগে SHA-256/HMAC dereference করো অথবা Argon2 ব্যবহার করো।

### Argon2id Parameters (OWASP minimum)

- Memory: 19 MiB (minimum), production-এ 64 MiB বা বেশি recommended
- Iterations: 2 (minimum)
- Parallelism: 1

### bcrypt Cost Factor

- Minimum: 10 (OWASP recommendation)
- Hardware দ্রুত হলে বাড়াও — OWASP-এর guideline অনুযায়ী একটা hash calculate করতে **one second-এর কম** সময় লাগা উচিত (সার্ভারের performance অনুযায়ী tune করো)

---

## Token Storage — কোথায় রাখবে?

Token কোথায় store করবে সেটা security-র জন্য গুরুত্বপূর্ণ সিদ্ধান্ত।

### localStorage vs httpOnly Cookie

| বিষয় | localStorage | httpOnly Cookie |
|-------|-------------|-----------------|
| **XSS attack** | ⚠️ Vulnerable — JS দিয়ে read হয় | ✅ Safe — JS দিয়ে read করা যায় না |
| **CSRF attack** | ✅ Safe — auto-send হয় না | ⚠️ Vulnerable — SameSite এবং CSRF token দিয়ে mitigate করতে হয় |
| **Implementation** | সহজ | Cookie management লাগে |
| **Mobile app** | Secure storage API ব্যবহার করো | N/A |

**Recommendation:**
- Access token: Memory (JS variable) বা httpOnly cookie — localStorage এড়াও।
- Refresh token: httpOnly, Secure, SameSite=Strict (বা Lax) cookie।
- Mobile: OS-provided secure storage (iOS Keychain, Android Keystore)।

### HTTPS বাধ্যতামূলক

RFC 8996 অনুযায়ী TLS 1.0 এবং TLS 1.1 deprecated। TLS 1.2 minimum; TLS 1.3 preferred। Bearer token HTTP-তে পাঠানো মানে token plain text-এ network-এ যাচ্ছে — সম্পূর্ণ insecure।

---

## Multi-Factor Authentication (MFA)

MFA মানে authentication-এর জন্য একের বেশি independent factor ব্যবহার করা।

**তিনটা authentication factor:**

1. **Something you know** — Password, PIN
2. **Something you have** — Phone (OTP app), Hardware key (YubiKey), SMS (দুর্বল বিকল্প)
3. **Something you are** — Fingerprint, Face ID (biometrics)

MFA মানে এই factor-গুলো থেকে অন্তত দুটো ব্যবহার করা।

### TOTP — Time-based One-Time Password (RFC 6238)

Google Authenticator, Authy, Microsoft Authenticator যেভাবে কাজ করে:

```
ASCII Diagram — TOTP Flow

Setup:
  Server → User: shared secret (QR code আকারে)
  User → TOTP App: secret scan করে

Login:
  User → Server: password + current 6-digit TOTP code
  Server: HMAC-SHA1(secret, floor(current_time / 30)) → 6-digit code
  Server: user-এর code এর সাথে match? → login দাও
```

TOTP code 30 seconds-এ change হয়। Code একবার use হলে server তা mark করে রাখে (replay prevention)।

**SMS OTP কেন দুর্বল:** SIM swapping attack, SS7 network vulnerability-র কারণে SMS interception সম্ভব। NIST SP 800-63B SMS OTP-কে restricted authenticator হিসেবে list করেছে — high-value accounts-এ SMS OTP এড়ানো উচিত।

### Passkeys (WebAuthn / FIDO2)

Passkey হলো modern, phishing-resistant authentication। Public key cryptography ব্যবহার করে — password-ই নেই।

- Device-এ private key থাকে (Secure Enclave / TPM)।
- Server-এ public key থাকে।
- Login-এ device biometric বা PIN দিয়ে private key দিয়ে challenge sign করে।
- Password leak হওয়ার প্রশ্নই নেই।

---

## Auth Vulnerabilities — বিস্তারিত

### 1. JWT `alg: none` Attack

JWT header-এ `"alg": "none"` দিলে কিছু naive implementation signature verify করে না। Attacker নিজের মতো payload তৈরি করে token forge করতে পারে।

**Defense:** Server-এ expected algorithm hardcode করো। `none` কখনো allow করো না। RFC 8725 Section 3.1 explicitly এটা forbid করে।

### 2. JWT Algorithm Confusion (RS256 → HS256)

RS256 token verify করে public key দিয়ে। Attacker যদি `alg` পাল্টে `HS256` করে দেয় এবং public key কে HMAC secret হিসেবে ব্যবহার করে token sign করে পাঠায় — vulnerable library `alg` header বিশ্বাস করে public key দিয়ে HMAC verify করে এবং valid ভাবে।

**Defense:** Library-তে allowed algorithms explicitly configure করো।

### 3. Brute Force / Credential Stuffing

- **Brute Force:** একটা account-এর password বারবার guess করা।
- **Credential Stuffing:** অন্য site-এর leaked username+password list দিয়ে try করা।

**Defense:** Rate limiting, account lockout, CAPTCHA, MFA।

### 4. Timing Attack (Password Comparison)

`password === stored_hash` এভাবে string compare করলে timing leak হয় — মিলন কত দূর পর্যন্ত হয়েছে সেটা response time থেকে জানা যায়।

**Defense:** Constant-time comparison function ব্যবহার করো। bcrypt-এর `compare()` function এটা internally handle করে।

### 5. Insecure Direct Object Reference (IDOR)

User A লগিন করে `/api/users/456/orders` request করে User B-র data পায় — server শুধু token check করে, resource ownership check করে না।

**Defense:** প্রতিটা resource access-এ ownership বা permission explicitly check করো।

### 6. Open Redirect

OAuth redirect_uri যদি strict validate না হয় — attacker `redirect_uri=https://evil.com` দিয়ে authorization code সেদিকে redirect করাতে পারে।

**Defense:** Allowed redirect URIs server-এ pre-register করো এবং exact match করো (RFC 6749 Section 10.6)।

### 7. PKCE Bypass / Missing State Parameter

OAuth-এ `state` parameter CSRF protection দেয়। `state` না থাকলে attacker নিজের authorization session তোমার account-এ bind করতে পারে।

**Defense:** `state` parameter সবসময় ব্যবহার করো এবং verify করো। PKCE ব্যবহার করো।

---

## Express.js-এ JWT Authentication — সম্পূর্ণ Example

### Installation

```bash
npm install jsonwebtoken bcrypt
```

> Note: Production-এ Argon2id-এর জন্য `npm install argon2` consider করো।

### User Registration

```javascript
const bcrypt = require('bcrypt');
const SALT_ROUNDS = 12; // minimum 10 per OWASP

// Module load-এ একবার generate করো — timing attack protection-এর জন্য
// (sync এখানে ঠিক আছে কারণ এটা startup-এ একবারই চলে)
const DUMMY_HASH = bcrypt.hashSync('__timing_protection_dummy__', SALT_ROUNDS);

async function registerUser(username, password) {
  // bcrypt 72-byte limit — password truncation হবে না যদি ≤72 bytes
  const hash = await bcrypt.hash(password, SALT_ROUNDS);
  // DB-তে hash save করো, password নয়
  await db.users.create({ username, passwordHash: hash });
}
```

### Login + Token Issue

```javascript
const jwt = require('jsonwebtoken');

async function loginUser(username, password) {
  const user = await db.users.findOne({ username });
  if (!user) {
    // Timing attack এড়াতে user না থাকলেও একটা real bcrypt compare করো
    // DUMMY_HASH একটা valid pre-generated hash — compare() পুরো bcrypt computation করবে
    await bcrypt.compare(password, DUMMY_HASH);
    throw new Error('Invalid credentials');
  }

  const match = await bcrypt.compare(password, user.passwordHash);
  if (!match) throw new Error('Invalid credentials');

  const accessToken = jwt.sign(
    { sub: user.id, role: user.role }, // payload
    process.env.JWT_SECRET,
    {
      algorithm: 'HS256',
      expiresIn: '15m',
      issuer: 'your-app-name',
      audience: 'your-app-name',
    }
  );

  return { accessToken };
}
```

### JWT Middleware

```javascript
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.startsWith('Bearer ')
    ? authHeader.slice(7)
    : null;

  if (!token) return res.status(401).json({ error: 'Token required' });

  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET, {
      algorithms: ['HS256'], // explicit — alg:none reject হবে
      issuer: 'your-app-name',
      audience: 'your-app-name',
    });
    req.user = payload;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}
```

### Protected Route

```javascript
app.get('/api/profile', authenticateToken, (req, res) => {
  // req.user.sub = authenticated user ID
  res.json({ userId: req.user.sub, role: req.user.role });
});
```

---

## Authorization — Role-based Access Control (RBAC)

Authentication-এর পরে authorization: authenticated user কী করতে পারে?

### Simple Role Middleware

```javascript
function requireRole(...allowedRoles) {
  return (req, res, next) => {
    if (!req.user || !allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

// ব্যবহার
app.delete('/api/users/:id',
  authenticateToken,
  requireRole('admin'),
  deleteUserHandler
);
```

### RBAC vs ABAC

| | RBAC (Role-Based) | ABAC (Attribute-Based) |
|-|-------------------|----------------------|
| **মডেল** | User-এর role অনুযায়ী access | User + resource + environment attribute অনুযায়ী |
| **সহজতা** | সহজ implement | জটিল |
| **নমনীয়তা** | কম | বেশি |
| **উদাহরণ** | admin, editor, viewer | "user.department == resource.department AND time.hour < 18" |

ছোট থেকে মাঝারি app-এ RBAC যথেষ্ট। Complex enterprise system-এ ABAC।

---

## Auth Flow — সম্পূর্ণ Overview Diagram

```
ASCII Diagram — Complete Auth Flow (Own App, JWT-based)

┌─────────┐     POST /login          ┌──────────────────────────────────────────┐
│  Client │ ─────────────────────── >│                Server                    │
│         │  { username, password }  │                                          │
│         │                          │  1. User lookup (DB)                     │
│         │                          │  2. bcrypt.compare(password, hash)       │
│         │                          │  3. Issue Access Token (JWT, 15m)        │
│         │                          │  4. Issue Refresh Token → save to DB     │
│         │ < ───────────────────────│                                          │
│         │  { access_token,         └──────────────────────────────────────────┘
│         │    refresh_token }
│         │
│         │     GET /api/resource         ┌──────────────────────────────────┐
│         │ ─────────────────────────────>│           Server                 │
│         │  Authorization: Bearer AT     │                                  │
│         │                               │  1. JWT verify (signature,       │
│         │                               │     exp, iss, aud)               │
│         │                               │  2. Authorization check          │
│         │ <─────────────────────────────│  3. Return resource              │
│         │  { data }                     └──────────────────────────────────┘
│         │
│         │  [AT expires]
│         │
│         │     POST /token/refresh       ┌──────────────────────────────────┐
│         │ ─────────────────────────────>│           Server                 │
│         │  { refresh_token: RT }        │                                  │
│         │                               │  1. RT lookup in DB              │
│         │                               │  2. Valid? Issue new AT + new RT │
│         │                               │  3. Invalidate old RT (rotation) │
│         │ <─────────────────────────────│                                  │
│         │  { access_token: NEW_AT,      └──────────────────────────────────┘
│         │    refresh_token: NEW_RT }
│         │
│         │     POST /logout              ┌──────────────────────────────────┐
│         │ ─────────────────────────────>│           Server                 │
│         │  { refresh_token: RT }        │  Delete RT from DB               │
│         │ <─────────────────────────────│  (AT still valid until expiry)   │
└─────────┘                               └──────────────────────────────────┘
```

---

## Security Checklist

Authentication implement করার সময় নিচের checklist follow করো:

**Password:**
- [ ] Plain text বা fast hash (MD5/SHA) store করছ না
- [ ] Argon2id বা bcrypt (cost ≥ 10) ব্যবহার করছ
- [ ] Constant-time comparison ব্যবহার করছ
- [ ] Password length limit আছে (bcrypt হলে 72-byte limit মাথায় রাখো)

**JWT:**
- [ ] `alg: none` reject করা হচ্ছে
- [ ] Algorithm explicitly configured
- [ ] `exp`, `iss`, `aud` validate করা হচ্ছে
- [ ] Sensitive data payload-এ নেই
- [ ] Short expiry (15-60 min) access token
- [ ] Secret key environment variable-এ, code-এ hardcode নয়

**Token Storage:**
- [ ] Access token localStorage-এ নেই
- [ ] Refresh token httpOnly cookie-তে
- [ ] HTTPS enforce করা হচ্ছে

**OAuth:**
- [ ] PKCE ব্যবহার করছ
- [ ] `state` parameter validate করছ
- [ ] Redirect URI server-এ registered এবং exact match
- [ ] Token query string-এ পাঠাচ্ছ না

**General:**
- [ ] Rate limiting আছে login endpoint-এ
- [ ] Error message থেকে user existence leak হচ্ছে না ("Invalid credentials" — not "User not found")
- [ ] HTTPS (TLS 1.2+) enforce করা হচ্ছে
- [ ] MFA option আছে (বিশেষত high-value accounts-এ)

---

## মূল উপলব্ধি (Updated)

Authentication শুধু "login করা" নয় — এটা একটা সম্পূর্ণ security layer।

- **Session** → Traditional web app-এ ভালো। Server stateful।
- **JWT** → Stateless API, SPA, mobile-এর জন্য ভালো। Payload public — sensitive data রাখো না। Short expiry + refresh rotation ব্যবহার করো।
- **OAuth 2.0** → Third-party resource access delegation। Authentication-এর জন্য OIDC দরকার।
- **OIDC** → OAuth 2.0-এর উপরে authentication layer। `id_token` JWT আকারে।
- **bcrypt** → Legacy কিন্তু solid। 72-byte limit জানো। Argon2id prefer করো নতুন project-এ।
- **PKCE** → Public client-এ Authorization Code Flow-এর সাথে mandatory।
- **alg: none** → সবসময় reject। Algorithm server-এ hardcode করো।
- **Token storage** → httpOnly cookie সবচেয়ে safe। localStorage XSS-এ vulnerable।
- **MFA** → Password-এর উপরে extra layer। TOTP বা Passkey।

---

[⬆ TOC](./table-of-contents.md) | [⬅ Ch 8](./chapter-08-mongoose.md) | [➡ Ch 10](./chapter-10-validation.md)
