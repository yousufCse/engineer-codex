# Asset-Free App Ideas — Research & Brainstorm

> **Goal:** Find the best app I can build where **AI (Claude Code) does 100% of the work** — no voice recording, no cartoon art, no licensed assets, no external designer, no third-party paid service.
> **Context:** First app on a **personal** Google Play account (needs 12 testers + 14-day closed test). Solo builder. Flutter.
> **Tone:** Open brainstorm → analysis → pick a winner.

---

## 1. The filter — what "no other source" really means

An idea passes only if **everything can be generated as code or come free from the device itself.** Let me nail the rule:

**Allowed (free, code-only):**
- Device capabilities: camera, mic, sensors (compass, accelerometer, GPS), flashlight.
- On-device ML: Google **ML Kit** (text recognition, doc scan, barcode) — free, offline, no API key.
- Pure logic: math, converters, generators, trackers.
- Programmatic UI: icons from `Icons`, shapes drawn in code, system fonts, gradients.
- Local storage: Hive / SQLite / SharedPreferences.

**NOT allowed (would need "other source"):**
- Recorded human voice (kids apps, language apps).
- Hand-drawn cartoon art / mascots / illustrations.
- Big curated content libraries (quiz banks, recipes, stories) — someone must write them.
- Live paid APIs as the core (weather, currency live rates, maps) — external dependency.

> **Insight:** The sweet spot = apps whose value comes from **processing what the user already has** (their camera, their files, their numbers), not from **content I must supply.**

---

## 2. Brain dump — every asset-free idea on the table

Raw list first, judge later. No filtering yet — just throw them out:

- **Document Scanner** (Microsoft Lens clone) — camera → crop → PDF/OCR.
- **QR & Barcode** scanner + generator.
- **Expense / Budget tracker** — offline money log + charts.
- **PDF Toolkit** — merge, split, compress, reorder, image→PDF.
- **Image Tools** — compress, resize, crop, format convert (JPG↔PNG↔WebP).
- **Calculator Suite** — BMI, age, loan/EMI, GPA, percentage, discount.
- **Password Generator + Vault** — strong passwords, encrypted local store.
- **Notes / To-do** with reminders + notifications.
- **Habit Tracker** — streaks, local, notifications.
- **Voice Recorder** — record, label, playback (device mic).
- **Unit Converter** — length, weight, temp, data, speed (static, offline).
- **Compass + Level + Flashlight** — sensor tools bundle.
- **Text Tools** — word/char count, case convert, remove duplicates, slugify.
- **Age / Date calculator** — days between, countdown to event.
- **Stopwatch + Timer + Pomodoro** — productivity clock.
- **Speedometer / GPS trip** — sensor-based.
- **Random picker / Dice / Coin flip** — decision maker.
- **Color picker / palette tool** — pick from camera, generate palettes.

That's the pool. Now score it.

---

## 3. Scoring — which ones actually win

Each idea scored 1–5 on six axes. Higher = better.

| Idea | Asset-free | AI builds 100% | Market demand | Money potential | Easy to ship (first app) | Play compliance easy | **Total /30** |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Document Scanner** | 5 | 5 | 5 | 5 | 4 | 4 | **28** |
| **PDF Toolkit** | 5 | 5 | 5 | 4 | 4 | 4 | **27** |
| **QR & Barcode** | 5 | 5 | 4 | 4 | 5 | 4 | **27** |
| **Expense Tracker** | 5 | 5 | 5 | 4 | 4 | 5 | **28** |
| **Image Tools** | 5 | 5 | 4 | 4 | 5 | 5 | **28** |
| **Calculator Suite** | 5 | 5 | 4 | 3 | 5 | 5 | **27** |
| **Password Vault** | 5 | 5 | 3 | 3 | 4 | 4 | **24** |
| **Habit Tracker** | 5 | 5 | 4 | 3 | 4 | 5 | **26** |
| **Notes / To-do** | 5 | 5 | 3 | 3 | 5 | 5 | **26** |
| **Voice Recorder** | 5 | 5 | 3 | 3 | 5 | 4 | **25** |
| **Unit Converter** | 5 | 5 | 3 | 2 | 5 | 5 | **25** |
| **Sensor Tools** | 5 | 5 | 3 | 2 | 5 | 4 | **24** |
| **Text Tools** | 5 | 5 | 2 | 2 | 5 | 5 | **24** |

> **Read:** Everything is asset-free and AI-buildable (that was the filter). The split happens on **demand + money.** Document Scanner, Expense Tracker, and Image Tools top the board.

---

## 4. The top 3 — deep dive

### 🥇 #1 — Document Scanner (Microsoft Lens style)  — WINNER

**What it does:** Point camera at a paper/receipt/ID → auto-detect edges → crop + fix perspective → clean/enhance → save as **PDF or image** → optional **OCR** (pull the text out) → share.

**Why it wins:**
- **Zero assets.** Value = processing the user's own camera input. Nothing to draw or record.
- **On-device ML Kit** does the heavy lifting — free, offline, no API key, no server.
- **Massive, evergreen demand** — students, offices, anyone without a scanner. Huge in BD.
- **Strong money:** free with ads → **Pro unlock** (unlimited pages, no watermark, no ads, OCR export, batch scan).
- **Professional feel with zero art** — UI is clean camera + document thumbnails; looks pro by default.

**Tech (all free):**
| Feature | Package |
|---|---|
| Auto edge-detect + scan UI | `cunning_document_scanner` or `google_mlkit_document_scanner` |
| OCR (text from image) | `google_mlkit_text_recognition` (supports many scripts) |
| Make PDF | `pdf` + `printing` |
| Image enhance/crop | `image` |
| Save / share | `path_provider`, `share_plus` |
| Local library of scans | `hive` |
| Ads / Pro | `google_mobile_ads`, `in_app_purchase` |

**Watch-outs:** Camera permission → needs privacy policy + data-safety declaration. OCR quality varies by lighting (set expectations in UI).

---

### 🥈 #2 — Expense / Budget Tracker

**What:** Log income + expense, categories, monthly budget, charts, export CSV/PDF.

**Why strong:** Pure logic + local DB + charts (`fl_chart`, drawn in code). No assets, no internet, no compliance headache (no camera/location). Steady demand. Money via ads + Pro (cloud backup later, unlimited categories, PDF reports).

**Weak vs #1:** Crowded market, harder to stand out; lower "wow" than a scanner.

---

### 🥉 #3 — Image / PDF Tools bundle

**What:** Compress image, resize, crop, convert format; merge/split PDF, image→PDF.

**Why strong:** All on-device (`image`, `pdf`, `pdfx`). Super easy to ship, tiny permissions, near-zero rejection risk. People search these constantly. Money via ads + Pro (batch, higher quality).

**Weak vs #1:** Utility feel, users open it rarely (bad for the 14-day "real usage" test signal). Scanner gets opened repeatedly.

---

## 5. Final recommendation

**Build the Document Scanner first.** 🎯

Reasoning in one line: **highest demand + best monetization + 100% AI-buildable + zero assets + repeat daily use (passes the 14-day test easily) — and it naturally contains #3 (PDF/image tools) as features inside it.**

Smart move: ship the **scanner as the flagship**, then fold in PDF toolkit features as "Pro" extras. One app, two markets covered.

**Fallback / easiest-to-ship:** if you want the absolute lowest-risk first launch, do **Expense Tracker** (no camera → no permission/compliance friction). But scanner has the bigger ceiling.

---

## 6. Suggested MVP scope (Document Scanner)

Ship small, grow later.

**MVP (v1):**
1. Camera scan → auto edge detect → manual corner adjust.
2. Enhance filters (auto / B&W / color / grayscale).
3. Multi-page scan → single PDF.
4. Save to in-app library (rename, delete).
5. Share / export PDF.
6. Basic OCR → copy text.
7. Banner ad + one "Remove ads / Pro" purchase.

**v2 (later):**
- Batch scan, ID-card mode (front+back on one page), signature, watermark, folders, cloud backup, searchable OCR library.

---

## 7. Monetization plan (asset-free, kid-safe not needed here)

- **Free tier:** ads (banner + occasional interstitial after save), watermark on PDF, page limit.
- **Pro (one-time or subscription):** no ads, no watermark, unlimited pages, OCR export, batch, premium filters.
- Adults audience → **no kids-policy restrictions** → normal AdMob allowed. Easier than the kids app.

---

## 8. Play Store compliance checklist

- [ ] **Privacy Policy** (mandatory — camera use). Host free on GitHub Pages / Google Sites.
- [ ] **Data Safety form** — declare camera; if scans stay on-device, say "no data collected/shared" (strong selling point — advertise "100% offline, private").
- [ ] **Permissions:** camera only (+ storage as needed). Keep minimal.
- [ ] **Content rating:** Everyone.
- [ ] **12 testers + 14-day closed test** before production (personal account rule).

---

## 9. Why this beats the earlier ideas

| Earlier idea | Problem for "no other source" |
|---|---|
| Kids Learning (Alphabet/Bangla) | Needs **recorded voice + cartoon art** → external assets. Also strict kids policy. |
| Prayer Times | Needs prayer-calc data/logic (OK) but Qibla/azan audio + upkeep; niche vs scanner. |
| Quiz / Trivia | Needs a **written question bank** → content someone must author. |
| Recipe / Story apps | Needs **content library** → not code-generatable. |

**Document Scanner sidesteps all of it** — the user brings the content (their documents); the app just processes it.

---

## 10. Next steps

1. Confirm **Flutter SDK installed** on this machine.
2. I scaffold the Flutter project (runs immediately with camera + scan).
3. Build MVP screens: Camera → Review/Crop → PDF Save → Library.
4. You run + test → I fix → iterate.
5. Add ads + Pro → prepare Play listing → closed test → publish.

---

*Research notes — asset-free = AI can build end-to-end. Winner: **Document Scanner**. Runner-up: **Expense Tracker**. Both need zero recorded/drawn assets.*
