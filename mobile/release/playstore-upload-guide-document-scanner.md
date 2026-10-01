# Publishing a Flutter "Document Scanner" App to Google Play in 2026 — A Complete Guide for a Solo Bangladesh Developer (New Personal Account)

> **Project scope:** A Flutter document scanner (Microsoft Lens–style): camera capture, edge detection, PDF export, on-device OCR (Google ML Kit), banner ads (AdMob), and a one-time "Pro" in-app purchase. General adult audience — **not** a kids app. Publisher: a **new personal / individual** Google Play developer account, based in Bangladesh, created after 13 November 2023.
>
> Every figure in this report (tester counts, days, target API level, fees, review times, withholding rates, SDK versions) has been taken from adversarially-verified research and reflects **current 2026 values**. Where a commonly-cited number was found to be stale, the corrected value is used and flagged.

---

## 1. Executive Summary

Getting this app onto the Play Store is **not blocked by anything technical** — a camera/OCR/PDF scanner is simple, well within all size and format limits, and Flutter's default toolchain handles almost everything. The real work is **process and policy**:

1. **The single biggest, non-negotiable delay** is the mandatory **closed-testing gate** for new personal accounts: **at least 12 testers, opted in continuously for at least 14 days**, before you can even *apply* for production. You cannot skip, shorten, or pay your way out of this.
2. **The most common rejection cause for scanner/utility apps** is over-broad storage/media permissions (`MANAGE_EXTERNAL_STORAGE` "All files access", or `READ_MEDIA_IMAGES`). This app must **avoid all of them** and use the Android Photo Picker + Storage Access Framework instead.
3. **The most common Data safety rejection** is declaring "no data collected" while running AdMob. The ad SDK collects and **shares** the Advertising ID, IP/approximate location, and app-activity — this **must** be declared even though your OCR/scanning itself is on-device and collects nothing.
4. **Two separate money pipelines** (Google Play billing for the Pro IAP, and AdMob for ads) each need their own account, tax forms, and verification. As a non-US developer you must file **Form W-8BEN**.

Realistic end-to-end time from account creation to public launch: **~3–6 weeks**, dominated by the fixed 14-day test window plus two review passes. Out-of-pocket cost is essentially just the **US $25 one-time** developer fee (plus an optional cheap domain for your privacy policy + `app-ads.txt`).

### 1.1 End-to-End Timeline & Cost Table

| Phase | What happens | Realistic duration | Cost | Can it overlap? |
|---|---|---|---|---|
| Account creation + $25 fee | Sign up, pay one-time fee (real credit/debit card — **no prepaid/virtual cards**) | Same day | **US $25 (one-time, non-refundable)** | — |
| Identity verification (personal account) | Verify legal name, address, email, phone (OTP); government photo ID | ~1–2 business days | $0 | ✅ overlap with build |
| Payments/merchant profile + bank verification | Needed because app monetizes (ads + IAP) | **Up to ~5 days** | $0 (need a Bangladesh bank account) | ✅ start day 1 |
| Build app + store listing + all declarations | Flutter build, assets, content rating, Data safety, privacy policy | A few days–2 weeks (your effort) | $0 (optional domain ~$10–15/yr) | ✅ overlap |
| Internal testing (optional smoke test) | Up to 100 testers, instant | 1–2 days | $0 | ✅ |
| **Closed testing gate (MANDATORY)** | **≥12 testers opted-in continuously ≥14 days** | **≥14 days (hard floor)** | $0 | ⚠️ fixed, cannot shorten |
| Apply for production + production-access review | 3-part form, Google reviews | **Usually ≤7 days** (occasionally longer) | $0 | ❌ after test |
| Standard app review (first release) | Content/policy review of the release | **~7 days** officially ("up to 7 days or longer in exceptional cases"); new accounts often slower | $0 | ❌ final gate |
| **TOTAL (account → public launch)** | | **~3–6 weeks** | **≈ US $25 total** | |

> **Key scheduling advice:** run identity/payment verification, listing prep, *and* the closed test in **parallel**, not in sequence. Treating every step as strictly sequential is the classic mistake that turns a ~3-week launch into 6 weeks.

---

## 2. Account & Identity Verification

**What it is:** Opening a Google Play Console developer account as an **individual/personal** publisher.

### Requirements

- **Pay the US $25 registration fee** — a **one-time, non-refundable** charge (not annual, unlike Apple's $99/year). It is unchanged as of 2026 and applies identically to a Bangladesh-based personal account. Paid during sign-up with a **credit or debit card**; **prepaid and most virtual cards are rejected** — a frequent pain point for Bangladesh developers, so use a real Visa/Mastercard. ([Play Console fee](https://support.google.com/googleplay/android-developer/answer/6112435))
- **Submit a government photo ID.** Personal accounts must provide and verify an official government photo ID. ([Identity requirements](https://support.google.com/googleplay/android-developer/answer/10841920))
- **Verify contact details:** legal name, legal address (no PO boxes), contact email, and contact phone (confirmed via one-time password). Verification is typically approved in **~1–2 business days**. ([Verification](https://support.google.com/googleplay/android-developer/answer/13628312))
- **D-U-N-S is NOT required** for personal accounts (only organizations need one).

> **Gotcha:** Your **name and address must exactly match your government ID.** Mismatches stall verification. The $25 fee is not refunded even if verification later fails.

> **Note on account type:** An *organization* account would exempt you from the closed-testing gate below — but it requires a D-U-N-S number and a registered organization, which is a different (harder) path. For a solo Bangladesh developer, the personal account + closed test is the normal route.

---

## 3. The Closed-Testing Requirement (the biggest gate)

**This is the rule that most surprises new solo developers, and the largest fixed delay in your schedule.**

Because your account is a **new personal account created after 13 November 2023**, you **cannot publish directly to Production.** Before you can even apply for production access, you must:

### The hard requirement (verified current value, 2026)

- Run a **CLOSED testing** track (internal testing does **not** count).
- Have **at least 12 testers** opted in.
- Those testers must have been **opted in for the last 14 days continuously.**

Official wording: *"At least 12 testers must be opted-in to your closed test when you apply for production access. They must have been opted-in for the last 14 days continuously."* ([Play Console Help](https://support.google.com/googleplay/android-developer/answer/14151465))

> **Corrected/updated number:** The requirement was **originally 20 testers** (introduced Nov 2023) and was **reduced to 12 on 11 December 2024**. The **14-day duration never changed** — only the count dropped. Do **not** plan around the old "20 testers" figure; **12 is the current floor.** (Google's own page confirms 12/14; the specific Dec 11 2024 date comes from corroborating community/third-party sources.)

### What actually counts

- **Adding an email is not enough.** Each tester must **open the opt-in link and accept/join with a distinct Google account.** Unaccepted invites count as **zero**. ([Set up testing](https://support.google.com/googleplay/android-developer/answer/9845334))
- Add testers via an **Email list** (fixed set of Google-account emails) or a **linked Google Group**, then share the opt-in link. You typically opt yourself in too.
- **Continuous** means the count must **stay at 12+ for the whole 14-day window.** If someone drops out and you fall below 12, the clock effectively resets. **Recruit a buffer of 15–20** to survive drop-off.
- **Testers must genuinely engage** with the app across the 14 days. Installed-but-never-opened "ghost" testers can get your production access **denied for lack of engagement**. (Note: a tester who opts in still counts even if they later uninstall — but real use is expected.)

### After the 14 days

1. Go to the Play Console **Dashboard → "Apply for production."**
2. Complete a **3-part form**: (a) tester recruitment/engagement + feedback, (b) target audience, value proposition, projected first-year installs, (c) changes made since testing + production readiness.
3. Google reviews it and emails the account owner. This **usually takes 7 days or less, but may occasionally take longer.**

> **Gotchas / common mistakes:**
> - Confusing **Internal** testing with **Closed** testing — only the closed track counts toward 12/14.
> - Thinking you're live the moment 14 days pass — you still must **apply and pass a review (~7 days)**, then pass the normal app review.
> - Using duplicate/self-only or non-Google-account emails — each tester needs a **distinct valid Google account**.

---

## 4. Technical / Build Requirements

The build rules are **identical regardless of account type or country** — Bangladesh location changes nothing here.

### Mandatory

| Requirement | Detail | Source |
|---|---|---|
| **Android App Bundle (.aab), not APK** | New apps must ship as `.aab` (since Aug 2021). Build with `flutter build appbundle --release` → `build/app/outputs/bundle/release/app-release.aab`. Do **not** upload a bare APK. (`flutter build apk` is fine for *local* testing only.) | [App Bundle FAQ](https://developer.android.com/guide/app-bundle/faq) |
| **Play App Signing** | Automatic with app bundles and effectively required. Google holds the app signing key; you keep a separate **upload key**. Just accept the default when creating the release. | [Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756) |
| **Upload keystore** | Generate once (`keytool -genkey -v -keystore upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload`), wire via `android/key.properties` + release `signingConfig`. **Back it up** — every future update must use the same upload key. | [App signing](https://developer.android.com/studio/publish/app-signing) |
| **Target API level 36 (Android 16)** | As of July 2026 new apps must target **API 35 minimum**; **from 31 August 2026 new apps/updates must target API 36 (Android 16) or higher.** Build a fresh 2026 app against **`targetSdk = 36` and `compileSdk = 36`** so it never needs resubmission. A one-time extension **to 1 November 2026** can be requested, but building at 36 avoids the question. | [Target SDK policy](https://support.google.com/googleplay/android-developer/answer/11926878) |
| **64-bit (arm64-v8a) native libs** | Required since Aug 2019. Flutter + ML Kit ship native `.so` code. Flutter includes `arm64-v8a` by default — just **don't** restrict `ndk.abiFilters` to only `armeabi-v7a`. Verify in Android Studio APK Analyzer (`lib/` folder). | [64-bit requirement](https://developer.android.com/google/play/requirements/64-bit) |
| **Strictly increasing versionCode** | Each upload needs an integer `versionCode` higher than any previous, **≤ 2,100,000,000**. In Flutter this is the `+N` in `pubspec.yaml` `version: 1.0.0+1` — bump `+N` on **every** store upload. `versionName` (the `1.0.0` part) is cosmetic and unrestricted. | [Versioning](https://developer.android.com/studio/publish/versioning) |

### Recommended / advisory

- **`minSdkVersion` 23–24.** No Play mandate, but ML Kit text recognition/OCR needs **API 21+** and some vision APIs need **23+**. Flutter's default is 21; bumping to 23–24 avoids ML Kit edge cases while keeping broad device reach. ([Target SDK](https://developer.android.com/google/play/requirements/target-sdk))
- **Upload the R8 `mapping.txt` + native debug symbols** if you enable obfuscation — gives readable crash reports. Optional but recommended.
- **Size limits are a non-issue.** Base module compressed download limit is 500 MB; a 200 MB download only triggers a non-blocking mobile-data warning. A scanner ships far under this — no Play Feature/Asset Delivery needed. ([Size limits](https://support.google.com/googleplay/android-developer/answer/9859372))

> **Gotchas:** Relying on Flutter's *default* `targetSdkVersion` (it can lag) instead of explicitly setting 36; reusing/lowering `versionCode` between uploads; losing the upload keystore (resettable via support, but blocks releases until fixed).

---

## 5. Store Listing Assets (with exact sizes)

> **Sourcing note (verified):** These pixel sizes were **independently confirmed** in a follow-up fact-check against the official Play Console specs — *"Add preview assets to showcase your app"* ([answer 9866151](https://support.google.com/googleplay/android-developer/answer/9866151)) and *"Create and set up your app"* ([answer 9859152](https://support.google.com/googleplay/android-developer/answer/9859152)). App icon **512×512, 32-bit PNG (with alpha), ≤1024 KB**; feature graphic **1024×500 (JPEG or 24-bit PNG, no alpha)**; **min 2, up to 8** screenshots per device type; title **30**, short desc **80**, full desc **4000** chars — all confirmed current. Play Console still shows the exact constraints inline at upload.

### Exact asset sizes table

| Asset | Exact size / format | Required? | Notes |
|---|---|---|---|
| **App icon** | **512 × 512 px**, 32-bit PNG (with alpha), ≤ 1 MB | Required | Do not put trademarked names/logos (e.g., "Microsoft Lens", "CamScanner") on it |
| **Feature graphic** | **1024 × 500 px**, JPG or 24-bit PNG (no alpha) | Required | Shown at top of listing |
| **Phone screenshots** | **2–8** images; PNG or JPG; each side between **320 px and 3840 px**; 16:9 or 9:16 | Required (min 2) | Show real scanning/OCR/PDF-export UI |
| **7-inch tablet screenshots** | Up to 8; same format rules | Optional (recommended for tablet reach) | |
| **10-inch tablet screenshots** | Up to 8; same format rules | Optional (recommended for tablet reach) | |
| **Promo/hi-res video** | YouTube URL | Optional | |
| **App title** | Up to **30 characters** | Required | |
| **Short description** | Up to **80 characters** | Required | |
| **Full description** | Up to **4000 characters** | Required | |

> **Verify these before upload** — Play Console shows the exact current constraints inline when you fill the listing.

### Listing content warnings (policy)

- **Do NOT copy** "Microsoft Lens", "CamScanner", other trademarked names, icons, or screenshots into your listing — impersonation/metadata violations cause rejection (see §10).
- Add your **developer website URL** in the store listing contact details — **AdMob uses it to verify app ownership** for `app-ads.txt` (see §9).

---

## 6. Content Rating (IARC questionnaire)

**Every app on Google Play must have a content rating** — Google does not allow unrated apps. Completing the **IARC** (International Age Rating Coalition) questionnaire is a **hard publish gate** inside the "App content" section. ([Content rating requirements](https://support.google.com/googleplay/android-developer/answer/9859655))

### How to do it

1. Play Console → **App content** (Policy → App content) → **Content rating → Start**.
2. Enter a **valid, monitored email** (used for the IARC certificate and any correspondence/override notices). ([Questionnaire](https://support.google.com/googleplay/android-developer/answer/188189))
3. **Select the category: "Utility, Productivity, Communication, or Other."** This is the exact current (2026) category name and the correct one — a scanner is an **app, not a game**; document creation/PDF/OCR maps here. **Do not pick a Game category.** ([Category](https://support.google.com/googleplay/android-developer/answer/6159978))
4. **Answer all content questions honestly.** For a clean scanner, violence / sexual content / profanity / drugs / gambling / horror are all **"No"**, yielding the **lowest age rating** (Everyone / PEGI 3 / USK All ages / IARC 3+).
5. **Truthfully disclose interactive elements:** the app **offers digital in-app purchases** (the one-time Pro IAP → answer **Yes**) and **contains ads**. These add informational labels but do **not** raise a scanner's age rating.
6. Review the calculated ratings and click **Submit** — ratings are issued **essentially immediately** (automated, no manual pre-approval queue for the initial rating).

One questionnaire generates ratings for **all participating boards at once**.

> **Corrected detail:** IARC now has **nine** participating authorities (not six): ESRB, PEGI, USK, ClassInd, ACB, GRAC (games only), plus **Taiwan (2023), Indonesia (2024), and Saudi Arabia/GAMR (2024)** — plus the generic IARC scale (3+, 7+, 12+, 16+, 18+) for territories without a local board. **Bangladesh has no local board**, so the **generic IARC scale** applies there. ([Participants](https://globalratings.com/participants/))

### Consequences of getting it wrong

- **Misrepresentation** can lead to app removal or suspension; updates can be rejected; authorities can override your rating after review.
- **Unrated** apps are labeled "Unrated", get restricted visibility, are blocked by parental controls, and can be removed.
- **Under-declaring** = a violation. **Over-declaring** (ticking violence/mature you don't have) needlessly inflates your age rating and shrinks your audience.

> **Consistency requirement:** Your **served ads must match the app's content rating**, and you must complete the separate **Ads** declaration. Also keep the **Target audience** declaration set to **general/adult** — a low age rating (Everyone/PEGI 3) does **not** make this a "kids app" unless you select child age bands, which you must **not** do. Re-do the questionnaire if a future update changes answers (e.g., adds chat or user-to-user sharing).

---

## 7. Data Safety + Privacy Policy

For a camera + on-device-OCR scanner with AdMob, **two things are unconditionally mandatory in 2026**: (1) the **Data safety form**, and (2) a **privacy policy** — both a Play Console link **and** a copy accessible **inside the app**.

### 7.1 The privacy policy

- **Play Console link:** post a working, public, clearly-labeled privacy-policy URL in **Store settings → Store listing → Privacy policy**. ([Privacy policy](https://support.google.com/googleplay/android-developer/answer/10144311))
- **In-app copy required too:** Because the app accesses the **camera** (sensitive), Google requires *"a privacy policy link in the designated field within Play Console, **and** a privacy policy link or text **within the app itself**."* Add it to an About/Settings screen.
- **Required contents:** developer info + a privacy contact; the types of personal/sensitive data accessed/collected/used/shared **and the parties it's shared with** (for this app: **Google/AdMob** for advertising, plus **Google Play services**); secure-handling procedures; retention & deletion policy; clearly labeled as a privacy policy.

> **Gotchas:** URL that is broken, behind a login, not public, or not clearly labeled = rejected. Providing it only in the listing but **not inside the app** = rejected. A privacy policy is **required even if the app collected zero data.**

### 7.2 The Data safety form

- **Mandatory** for every app on **closed, open, or production** tracks. Only apps **exclusively on internal testing** are exempt — so as soon as you start your closed test, the form is due. ([Data safety](https://support.google.com/googleplay/android-developer/answer/10787469))
- The form uses **14 data categories**: Location, Personal info, Financial info, Health & fitness, Messages, Photos and videos, Audio files, Files and docs, Calendar, Contacts, App activity, Web browsing, App info and performance, Device or other IDs.

### 7.3 The critical honesty nuance — declare correctly

**On-device scanning/OCR = NOT "collected."** Google's rule: *"User data … only processed locally on the user's device and not sent off device does not need to be disclosed."* ML Kit text recognition runs **fully on-device** — so your **scan images, extracted OCR text, and on-device PDFs are honestly declared as no collection/sharing.** You still complete the form; the scanner core simply reports **no data collected**.

**BUT AdMob flips you out of the "collects no data" category.** The AdMob / Google Mobile Ads SDK automatically **collects AND shares**:

| Data the AdMob SDK collects & shares | Data safety category |
|---|---|
| Android **Advertising ID**, App Set ID, account identifiers | **Device or other IDs** |
| **IP address** (used to estimate approximate location) | **Location (approximate)** / Device IDs |
| **User product interactions** (app launches, taps, video views) | **App activity** |
| **Diagnostic / performance data** | **App info and performance** |

These must be marked as **both Collected and Shared** (not merely "may share" — Google's guidance says both). All are encrypted in transit (TLS). ([AdMob data disclosure](https://developers.google.com/admob/android/next-gen/privacy/play-data-disclosure))

> **THE #1 Data safety rejection cause:** declaring **"No data collected"** while shipping AdMob. Third-party SDKs count as **your** collection/sharing. Also answer the form's **encryption-in-transit** and **data-deletion mechanism** questions for the ad-related data, and make sure the form **matches the written privacy policy exactly.**

The one-time Pro purchase is handled by Google Play Billing; if disclosed from the billing side it maps to **Purchase history / Financial info** (separate from the ads SDK).

---

## 8. Permissions & Policy Compliance

The permission surface for a scanner comes down to three principles: **(1)** every permission must be necessary for a promoted core feature at minimum scope; **(2)** broad storage/media permissions are "restricted" and a scanner **almost never qualifies**; **(3)** any unexpected data use needs an in-app prominent disclosure + consent.

### The realistic manifest for this app

Essentially just: **`CAMERA`** + **`com.google.android.gms.permission.AD_ID`** + **`INTERNET`** (+ `com.android.vending.BILLING` for the IAP). **Avoid** legacy `READ/WRITE_EXTERNAL_STORAGE` on modern target APIs.

### Do / Don't

| ✅ Do | ❌ Don't |
|---|---|
| Request **CAMERA** at runtime with a rationale — scanning is the core promoted feature, so **no Permissions Declaration Form is needed** for camera. Degrade gracefully if denied (offer import-from-file). ([Permissions](https://support.google.com/googleplay/android-developer/answer/16558241)) | **Request `MANAGE_EXTERNAL_STORAGE` ("All files access")** — this is the **#1 policy rejection for scanner/PDF/utility apps.** Its permitted uses are file managers, backup, antivirus, document *management*, etc. A scanner saving its own PDFs **does not qualify.** ([All files access](https://support.google.com/googleplay/android-developer/answer/10467955)) |
| Save PDFs/OCR output to **app-specific storage** or via the **Storage Access Framework** (`ACTION_CREATE_DOCUMENT`/`ACTION_OPEN_DOCUMENT`); use **MediaStore** for shared media. ([Scoped storage](https://support.google.com/googleplay/android-developer/answer/16935362)) | **Request `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO`** for "import from gallery." Broad access is reserved for gallery/photo-manager apps and needs a declaration (full enforcement since **28 May 2025**; non-compliant apps subject to removal). |
| Use the **Android Photo Picker** for importing an existing image — **needs no permission.** Integrate via `androidx.activity` **1.7.0+** (`PickVisualMedia`). In Flutter, `image_picker`/photo-picker plugins wrap this. ([Photo Picker](https://support.google.com/googleplay/android-developer/answer/14115180)) | Ship **leftover permissions** merged from ad/OCR SDK manifests (e.g., legacy storage, `QUERY_ALL_PACKAGES`) that no feature uses — reviewers flag over-broad/unused permissions. |
| **Declare `com.google.android.gms.permission.AD_ID`** (auto-merged by Google Mobile Ads SDK **20.4.0+**) since you target API 33+ and use ads — otherwise the ad ID is zeroed. Declare the Advertising ID under **Device or other IDs**. ([AD_ID](https://support.google.com/googleplay/android-developer/answer/6048248)) | **Target children** — that would drag in the stricter Families/COPPA regime you're avoiding. Keep imagery/wording clearly adult/general. |

### Prominent disclosure

A **separate in-app disclosure + consent** is required **only** for data use users would **not** reasonably expect. **Camera capture by a scanner IS expected → no special screen needed** for capture itself. But **if** you ever upload/back-up/share scans to a server, or add analytics/crash reporting, you must show an in-app disclosure (immediately before the request, stating what/why/how), with affirmative wording ("Agree") and at least two choices — it **cannot** live only in the privacy policy. ([Prominent disclosure](https://support.google.com/googleplay/android-developer/answer/11150561))

### Ads must be non-disruptive

- **Banner ads are explicitly permitted.**
- **Full-screen interstitials** (if you ever add them) must **not appear unexpectedly** (not on app launch, before splash, on Back press, or between every action), **must be closeable after 15 seconds** (non-closeable-after-15s interstitials are **not allowed**), and AdMob guidance caps them at **no more than one per two user actions**. Ads must not display outside the app, mimic system UI, or force clicks. ([Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753))

### Minimum & Broken Functionality

The app must **actually work end-to-end** on the reviewer's device — scan, edge-detect, OCR, and export a **working PDF** without crashing, freezing, or behaving like a thin static PDF/text viewer. Provide working test steps/credentials for any gated feature. ([Functionality policy](https://support.google.com/googleplay/android-developer/answer/9898783))

> **On restricted permissions generally:** if you ever *must* declare one, you file the **Permissions Declaration Form** with a justification and a short demo video (YouTube link preferred). **Corrected detail:** the "~30-second video limit" often quoted is **not** an official Google rule — Google specifies only the video's purpose/format, no required duration (a tight 30–60s clip is good practice). Review can take **up to several weeks**. Best practice for this scanner: **request none of these**, so you skip the path entirely. ([Declare permissions](https://support.google.com/googleplay/android-developer/answer/9214102))

---

## 9. Monetization & Tax Setup

You must stand up **two independent money pipelines**, each with its own gating steps. Completing one does **not** complete the other.

### 9.1 Pipeline A — In-app purchase (the one-time Pro unlock)

1. **Create a Google payments/merchant profile** (Play Console → Settings → Payments profile → Create). Provide legal individual name, physical address (no PO boxes), authorized contact, website, product category, support email, and statement descriptor. **Bangladesh is a supported merchant location.** ([Payments profile](https://support.google.com/googleplay/android-developer/answer/7161426))
2. **Register + verify a bank account in the same country as the profile (Bangladesh).** ⚠️ **The profile country is locked forever** and the bank account must be in that same country — pick correctly at creation. Developers with unverified bank accounts get removed from Play.
3. **Integrate Play Billing Library v8+.** Declare `com.android.vending.BILLING` in the manifest. **By 31 August 2026, new apps/updates must use Play Billing Library v8 or later** (extension to **1 November 2026** on request). A 2026 build should ship on **v8+ from the start** — if using the Flutter `in_app_purchase` plugin, ensure the version bundles Play Billing **v8+**. ([Billing](https://developer.android.com/google/play/billing) · [v8 deadline](https://developer.android.com/google/play/billing/migrate-gpblv8))
4. **Create the Pro unlock as a one-time product** (Monetize with Play → Products → **one-time products**, formerly "in-app products"). Provide:
   - **Product ID** — starts with a number or lowercase letter; only `0-9 a-z _ .`; **permanent — cannot be changed or reused** even after deletion. **Choose a stable ID like `pro_unlock` up front.**
   - **Title** (up to 55 chars, 25 recommended), **Description** (up to 200 chars), optional **512×512 PNG icon (max 1 MB)**, and price.
   - Use a standard **"buy" (durable / non-consumable)** purchase option for a lifetime unlock. **Do NOT consume the purchase in code** — acknowledge it, but consuming it would let it be repurchased and the user would lose access. Then click **Activate**. ([One-time products](https://support.google.com/googleplay/android-developer/answer/16430488) · [Create product](https://support.google.com/googleplay/android-developer/answer/1153481))
5. **Test purchases with a signed release build** on at least an internal/closed track, with **license test accounts** added — you **cannot** test IAP with a debug build.

### 9.2 Pipeline B — AdMob (banner ads)

1. **Create ONE AdMob account** (only one per publisher; a duplicate/old closed account blocks approval). It auto-creates a linked AdSense account. ([AdMob setup](https://support.google.com/admob/answer/9989980))
2. **Add the app in AdMob → link it to your Google Play listing** ("Yes, it's listed…" → search + link). Linking triggers automatic review and enables **full ad serving**; unlinked apps get limited serving.
3. **Create banner ad units.**
4. **Set your developer website in the Play listing, then publish `app-ads.txt`** at the **root of that exact domain** (`https://example.com/app-ads.txt`) using AdMob's personalized snippet (your publisher ID). Firebase Hosting is an allowed host. Allow up to 24h for crawling. ⚠️ **The domain must exactly match the website URL in your Play listing** — a subdomain, path, or different URL fails verification. ([app-ads.txt](https://support.google.com/admob/answer/9363762))
5. **Complete AdMob payment setup:** tax info, **identity + address (PIN) verification** (Google mails a physical PIN — **factor in Bangladesh postal delay**), and a payment method. Payments are issued monthly after the 21st, once you clear the payout threshold. ([AdMob payments](https://support.google.com/admob/answer/2772208))
6. **Never click your own live ads.** Use **test ad unit IDs / registered test devices** during development. Invalid traffic → withheld earnings or **permanent account ban.** Keep banners in stable, non-interactive regions (e.g., **not** next to the capture/shutter button). ([Ad policy](https://support.google.com/admob/answer/6128543))
7. **Audience/consent:** do **not** tag the app child-directed; set content/ad ratings truthfully; implement a consent solution (Google's **UMP SDK**) for GDPR regions.

### 9.3 US Tax — critical for a Bangladesh developer

- **Submit Form W-8BEN** (Certificate of Foreign Status — **individuals**, *not* the entity form W-8BEN-E) from your payments profile. This certifies you're a non-US person. ([Tax info](https://support.google.com/paymentscenter/answer/10349995))
- **If you don't file valid tax info**, Google may apply **24% backup withholding** (if info is incorrect/inaccurate) or **Chapter 3 withholding up to 30%** on applicable **US-source** earnings. So **file before earnings accrue.**
- **W-8BEN expires** and must be re-submitted (generally every ~3 years).

> **Nuance on the US–Bangladesh treaty (important, corrected):** A US–Bangladesh income tax treaty **does exist** (signed 26 Sep 2004, in force 7 Aug 2006; Article 12 caps royalty withholding at ~10%). **However**, Google Play developer payouts are normally **business profits (Article 7)**, taxable only in Bangladesh (i.e., typically **0% US tax**) unless you have a US permanent establishment — **not** royalties. So filing a W-8BEN with your **Bangladesh eTIN** and claiming treaty benefits mainly ensures you're correctly documented and avoids the 24% backup withholding; app-sale proceeds are generally **not** US-source royalties. The 30% Chapter 3 rate only bites on any US-source **royalty** portion. **This is a tax matter, not a Play policy — consult a Bangladesh tax advisor** for the final characterization.

> **Note:** US **Form 1099-K** (threshold reinstated to **>$20,000 AND >200 transactions** for 2025–2026) applies to **US persons**, not a Bangladesh-resident developer, who is instead under W-8BEN / 1042-S non-US withholding rules.

### Order of operations before you can earn

- **IAP earnings need:** verified identity → payments profile → verified bank account → submitted W-8BEN → Billing v8+ integrated → **Activated** one-time product → signed build on a test track with license testers.
- **Ad earnings need:** approved AdMob account → app linked to Play listing → ad units created → verified `app-ads.txt` → AdMob tax/identity/address (PIN) verified → payment method → payout threshold reached.

---

## 10. Release Process

### The four tracks

| Track | Purpose | Testers | Notes |
|---|---|---|---|
| **Internal** | Fast QA smoke test | Up to 100 | Instant; **does NOT satisfy the 12/14 gate** |
| **Closed** | **The mandatory production gate** | ≥12 opted-in | The 14-day requirement lives here |
| **Open** | Optional public beta | Unlimited | Discoverable on Play; not required for the gate |
| **Production** | Public launch | Everyone | Passes review before going live |

### Two reviews people confuse

1. **Production-ACCESS review** (~7 days) — after your closed test, when you "Apply for production."
2. **Standard app REVIEW** — the content/policy review of the actual release. Officially *"up to seven days or longer in exceptional cases."* **New/first-time accounts often take 7–14 days**; established accounts clear in 1–3 days.

**Both must pass before public launch.**

### Other release facts

- **Pre-launch report:** auto-generated when you upload a bundle to a **closed or open** track. Google installs it on **real devices** and crawls for crashes, security, and display issues. **Provide test credentials** if any screen gates access, or the crawler stalls. Review it before promoting. ([Pre-launch report](https://support.google.com/googleplay/android-developer/answer/9844487))
- **Staged/phased rollout is UPDATES-ONLY.** You **cannot** soft-launch a first-time publish to 10% — the **initial launch is all-at-once (100%).** Staged rollout (e.g., 10%→50%→100%, manually increased, haltable) applies to **later updates only.** ([Staged rollout](https://support.google.com/googleplay/android-developer/answer/6346149))
- **Release statuses:** Draft → Ready to send for review → In review → Ready to publish (or Rejected).

---

## 11. Top Rejection Reasons & How to Avoid Them (scanner/utility-specific)

| # | Rejection reason | How to avoid it |
|---|---|---|
| 1 | **Requesting `MANAGE_EXTERNAL_STORAGE` ("All files access")** — the single most common policy rejection for scanner/PDF/utility apps | Use **app-specific storage + Storage Access Framework + MediaStore**. A scanner doesn't qualify as a "document management" app. Request **none** of the broad storage permissions. |
| 2 | **`READ_MEDIA_IMAGES`/`READ_MEDIA_VIDEO` for "import from gallery"** | Use the permission-less **Android Photo Picker** (`PickVisualMedia`, `androidx.activity 1.7.0+`). |
| 3 | **Data safety says "no data collected" while running AdMob** | Declare the **Advertising ID, IP/approx location, App activity, diagnostics** as **Collected AND Shared**. Third-party SDKs count as your collection. |
| 4 | **Data safety form contradicts the privacy policy** | Make them describe the **same** data, uses, and sharing parties (Google/AdMob, Play services). |
| 5 | **Missing in-app privacy policy** (only in the listing) | Camera access requires the policy **both** in Play Console **and** inside the app (About/Settings). |
| 6 | **Broken/login-gated/unlabeled privacy-policy URL** | Host a public, clearly-labeled, working URL (a cheap domain or Firebase Hosting). |
| 7 | **Minimum / Broken Functionality** — crashes or acts like a thin PDF viewer | Ensure scan → edge-detect → OCR → **working PDF export** end-to-end, no crashes. Provide test steps. |
| 8 | **Disruptive ads** — interstitial on launch/Back, non-dismissible, or ads outside the app | Banners in stable regions; if you add interstitials, only at natural breaks, closeable within 15s, ≤1 per 2 actions. |
| 9 | **Leftover/over-broad permissions** merged from SDKs | Audit the merged manifest; strip anything no promoted feature uses. |
| 10 | **Impersonation / metadata** — copying "Microsoft Lens"/"CamScanner" names, icons, screenshots | Use your own original name, icon, and screenshots. |
| 11 | **Missing `AD_ID` permission on API 33+** (ad ID silently zeroed) | Use current Google Mobile Ads SDK (**20.4.0+**), which auto-merges it; declare the ad ID in Data safety. |
| 12 | **Content-rating mismatch** — saying "No" to IAP when you have the Pro unlock, or stale rating after a feature change | Answer IAP/ads truthfully; re-do the questionnaire when features change. |
| 13 | **Ghost testers** in the closed test → production access denied | Recruit **15–20** real, engaged testers; keep ≥12 continuously for 14 days. |

---

## 12. Master Pre-Launch Checklist

### Account & verification
- [ ] Paid the **US $25** one-time fee with a **real credit/debit card** (not prepaid/virtual)
- [ ] Verified legal name, address, email, phone (OTP) and submitted **government photo ID** — details match the ID
- [ ] Payments/merchant profile created, **country set correctly (Bangladesh — permanent)**, bank account verified

### Build (technical)
- [ ] `flutter build appbundle --release` produces a signed **`.aab`**
- [ ] **`targetSdk = 36`, `compileSdk = 36`** (Android 16)
- [ ] `minSdk` 23–24 (ML Kit-safe)
- [ ] **`arm64-v8a`** present (checked in APK Analyzer); `abiFilters` not restricted to 32-bit only
- [ ] `versionCode` (`+N` in pubspec) strictly higher than any prior upload
- [ ] Upload keystore generated and **backed up** (file + passwords); Play App Signing accepted
- [ ] (Recommended) R8 `mapping.txt` + native symbols uploaded

### Permissions & policy
- [ ] Manifest is essentially **`CAMERA` + `AD_ID` + `INTERNET`** (+ `BILLING`); no `MANAGE_EXTERNAL_STORAGE`, no `READ_MEDIA_*`, no legacy storage
- [ ] Import-from-gallery uses the **Android Photo Picker** (no permission)
- [ ] PDF/OCR output saved via **SAF / app-specific storage / MediaStore**
- [ ] Camera requested at runtime with rationale; graceful fallback if denied
- [ ] Ads are non-disruptive banners; no unexpected/non-closeable full-screen ads
- [ ] App works **end-to-end** (scan → edge-detect → OCR → PDF) with no crashes

### Store listing assets *(confirm exact sizes in Play Console)*
- [ ] App icon **512×512 PNG** (≤1 MB), no trademarked names/logos
- [ ] Feature graphic **1024×500**
- [ ] **2–8 phone screenshots** of real UI
- [ ] Title ≤30 chars, short desc ≤80, full desc ≤4000
- [ ] Developer **website URL** set (needed for `app-ads.txt`)

### Content rating
- [ ] IARC questionnaire completed → category **"Utility, Productivity, Communication, or Other"**
- [ ] Answered content questions honestly (all "No" → lowest rating)
- [ ] Declared **In-app purchases = Yes** and **Contains ads**
- [ ] Valid, monitored email entered for IARC; rating submitted

### Data safety & privacy
- [ ] **Data safety form** completed
- [ ] On-device OCR/scans declared as **no collection**
- [ ] AdMob data (**Advertising ID, IP/approx location, App activity, diagnostics**) declared **Collected AND Shared**
- [ ] Encryption-in-transit and data-deletion questions answered
- [ ] Privacy policy **URL in Play Console** (public, working, labeled)
- [ ] Privacy policy **also inside the app** (About/Settings)
- [ ] Form and written policy are **consistent**
- [ ] **Target audience = general/adult** (no child age bands)

### Monetization & tax
- [ ] **Play Billing v8+** integrated; `BILLING` permission declared
- [ ] Pro unlock created as **one-time "buy" (durable) product**, ID `pro_unlock` (permanent), **Activated**, **not consumed** in code
- [ ] IAP tested on a signed build with license test accounts
- [ ] **Form W-8BEN** (individual) submitted; Bangladesh **eTIN** provided for treaty claim
- [ ] One **AdMob** account; app **linked** to Play listing; banner ad units created
- [ ] **`app-ads.txt`** at the **root of the exact listing domain**, verified
- [ ] AdMob tax + **identity/address (PIN)** verified; payment method set
- [ ] Only **test ads** used in development (no self-clicks)

### Release
- [ ] Internal testing smoke test done (optional)
- [ ] **Closed test: ≥12 (ideally 15–20) real testers opted in and engaged, continuously for ≥14 days**
- [ ] Pre-launch report reviewed (test credentials provided if needed)
- [ ] **Applied for production** (3-part form completed) → passed production-access review
- [ ] Passed standard app review → **published** (first launch is 100%, all-at-once)

---

## 13. Sources

**Account & verification**
- Play Console fee / get started — https://support.google.com/googleplay/android-developer/answer/6112435
- Identity requirements — https://support.google.com/googleplay/android-developer/answer/10841920
- Account verification / timelines — https://support.google.com/googleplay/android-developer/answer/13628312

**Closed-testing requirement**
- App testing requirements for new personal accounts — https://support.google.com/googleplay/android-developer/answer/14151465
- Set up an open, closed, or internal test — https://support.google.com/googleplay/android-developer/answer/9845334
- Community guide (12-testers) — https://support.google.com/googleplay/android-developer/community-guide/255621488

**Technical / build**
- Target SDK policy — https://support.google.com/googleplay/android-developer/answer/11926878
- Target API level (rolling) — https://support.google.com/googleplay/android-developer/answer/16561298 · https://developer.android.com/google/play/requirements/target-sdk
- App Bundle FAQ / requirement — https://developer.android.com/guide/app-bundle/faq · https://support.google.com/googleplay/android-developer/answer/9859152
- 64-bit requirement — https://developer.android.com/google/play/requirements/64-bit
- Play App Signing — https://support.google.com/googleplay/android-developer/answer/9842756 · https://developer.android.com/studio/publish/app-signing
- Versioning — https://developer.android.com/studio/publish/versioning
- Size limits — https://support.google.com/googleplay/android-developer/answer/9859372

**Content rating**
- Content rating requirements — https://support.google.com/googleplay/android-developer/answer/9859655
- Content ratings — https://support.google.com/googleplay/android-developer/answer/9898843
- Questionnaire — https://support.google.com/googleplay/android-developer/answer/188189
- Category ("Utility, Productivity, Communication, or Other") — https://support.google.com/googleplay/android-developer/answer/6159978
- IARC overview — https://support.google.com/googleplay/answer/6209544 · https://globalratings.com/participants/

**Data safety & privacy**
- Data safety form — https://support.google.com/googleplay/android-developer/answer/10787469
- Privacy policy requirement — https://support.google.com/googleplay/android-developer/answer/10144311
- Declare data use — https://developer.android.com/privacy-and-security/declare-data-use
- AdMob data disclosure — https://developers.google.com/admob/android/next-gen/privacy/play-data-disclosure

**Permissions & policy**
- Permissions / minimum scope — https://support.google.com/googleplay/android-developer/answer/16558241
- All files access (`MANAGE_EXTERNAL_STORAGE`) — https://support.google.com/googleplay/android-developer/answer/10467955
- Scoped storage alternatives — https://support.google.com/googleplay/android-developer/answer/16935362
- Photo & Video Permissions policy — https://support.google.com/googleplay/android-developer/answer/14115180 · https://support.google.com/googleplay/android-developer/answer/15800983
- Android Photo Picker — https://developer.android.com/training/data-storage/shared/photo-picker
- Prominent disclosure — https://support.google.com/googleplay/android-developer/answer/11150561
- Declare permissions (restricted) — https://support.google.com/googleplay/android-developer/answer/9214102
- Advertising ID / AD_ID — https://support.google.com/googleplay/android-developer/answer/6048248
- Ads policy / Better Ads — https://support.google.com/googleplay/android-developer/answer/9857753 · https://support.google.com/googleplay/android-developer/answer/12271244
- Functionality policy — https://support.google.com/googleplay/android-developer/answer/9898783

**Monetization & tax**
- Payments profile — https://support.google.com/googleplay/android-developer/answer/7161426
- Create product / IAP — https://support.google.com/googleplay/android-developer/answer/1153481
- One-time products — https://support.google.com/googleplay/android-developer/answer/16430488 · https://developer.android.com/google/play/billing/manage-catalog
- Play Billing / v8 — https://developer.android.com/google/play/billing · https://developer.android.com/google/play/billing/deprecation-faq · https://developer.android.com/google/play/billing/migrate-gpblv8
- US tax info / withholding — https://support.google.com/paymentscenter/answer/10349995
- US–Bangladesh tax treaty — https://www.irs.gov/businesses/international-businesses/bangladesh-tax-treaty-documents
- 1099-K threshold — https://www.irs.gov/newsroom/irs-issues-faqs-on-form-1099-k-threshold-under-the-one-big-beautiful-bill-dollar-limit-reverts-to-20000
- AdMob setup / linking — https://support.google.com/admob/answer/9989980
- app-ads.txt — https://support.google.com/admob/answer/9363762
- AdMob payments — https://support.google.com/admob/answer/2772208
- AdMob policies / invalid traffic — https://support.google.com/admob/answer/6128543 · https://support.google.com/admob/answer/2753860

**Release process**
- Production-access & testing gate — https://support.google.com/googleplay/android-developer/answer/14151465
- Tracks (internal/open) — https://support.google.com/googleplay/android-developer/answer/9845334 · https://developers.google.com/android-publisher/tracks
- Staged rollout — https://support.google.com/googleplay/android-developer/answer/6346149
- Pre-launch report — https://support.google.com/googleplay/android-developer/answer/9844487
- Publish / review time — https://support.google.com/googleplay/android-developer/answer/9859751 · https://support.google.com/googleplay/android-developer/answer/9859654

---

### Verification status

This report passed a **second, independent adversarial fact-check** (15 verifiers, each trying to *refute* a hard claim against official Google sources). **Result: all 15 core claims confirmed, 0 corrections, 0 unresolved** — 12/14 testers, $25 one-time fee, target API 35 now / API 36 from 31 Aug 2026, .aab requirement, Billing v8 by 31 Aug 2026, IARC category label, `MANAGE_EXTERNAL_STORAGE` non-qualification, Photo Picker (no permission), AdMob data-safety collect+share, in-app privacy policy, interstitial-closeable-by-15s, W-8BEN + 24%/30% withholding, staged-rollout-updates-only, asset sizes, and `AD_ID`.

### Remaining caveats

- **Forward 2026 dates (API 36 → 31 Aug 2026, extension to 1 Nov 2026; Billing v8 → 31 Aug 2026):** confirmed against Google's deprecation FAQ and target-SDK policy, but some official static pages were still cache-serving prior-cycle (API 35 / 2025) wording when checked. Values match Google's documented pattern + the official "New deadline: Target API Level" notice. **Re-check the official pages close to submission.**
- **US–Bangladesh tax characterization (§9.3)** is a tax matter, not a Play policy — the treaty exists, but whether your payouts are business profits (typically 0% US tax) vs. royalties is a professional determination. Note the official page phrases the **24% backup / 30% Chapter 3** rates as flat rates (not "up to"). **Consult a Bangladesh tax advisor.**
- The **"Dec 11, 2024" reduction date** (20→12 testers) is corroborated by third-party sources; Google's own page confirms only the current 12/14 values, not the exact change date.