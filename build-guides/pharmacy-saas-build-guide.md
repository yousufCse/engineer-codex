# PharmaSaaS — AI Build Guide (Multi-Tenant Pharmacy SaaS)

**PharmaSaaS** is a web-based, multi-tenant SaaS for pharmacies: inventory management, POS (point-of-sale), batch/expiry tracking, receipts, and reports — sold to many pharmacies from **one** application. You build it with an AI coding agent (Claude Code) by pasting the prompts in this file **one step at a time**.

- **Staff web app** — React / **Next.js**: login, dashboard, inventory, purchase, POS, receipts, reports, settings. Used by pharmacy owner/staff in a browser.
- **Super-admin web app** — same Next.js app, separate area: the platform owner (you) creates pharmacies, sets plans, marks bills paid, suspends non-payers.
- **Backend** — **Node.js + NestJS** + **PostgreSQL** (Prisma ORM): REST API, JWT auth, multi-tenant isolation, business rules, transactions.

> **No mobile app.** Web only, accessed online in a browser. No Flutter, no customer-facing online ordering in v1 (designed so it can be added later without rework).

> **About this guide's language.** The prompts (the fenced blocks you paste) are in **English** on purpose — AI coding agents produce better code from English specs. The explanations around them are kept simple. Your Bangla study-doc style is for learning docs; this is a build spec.

---

## Table of contents

1. [Why this stack](#why-this-stack)
2. [What "multi-tenant" means here (read first)](#multi-tenant)
3. [Architecture at a glance](#architecture)
4. [Clean, swappable architecture (NestJS)](#clean-architecture)
5. [The data model (canonical)](#data-model)
6. [Core business rules](#business-rules)
7. [Decisions baked in](#decisions)
8. [Before you start (one-time setup)](#before-you-start)
9. [How to use this guide (the loop)](#how-to-use)
10. [Design system](#design-system)
11. [The Steps (paste these)](#the-steps)

---

<a name="why-this-stack"></a>
## 1. Why this stack

| Need | Solution | Why |
|---|---|---|
| One app serves 100+ pharmacies, data kept separate | **Multi-tenant Postgres** (`tenantId` on every row) | One codebase, one DB, isolated data — the SaaS core |
| Structured backend a solo dev can grow | **NestJS** | Modules, DI, guards, pipes — opinionated so you don't invent structure |
| Type-safe DB + easy migrations | **Prisma** + PostgreSQL | Schema in one file, auto migrations, no hand-written SQL to start |
| Login, roles, tenant isolation | **JWT** + Nest **Guards** + Prisma tenant extension | Enforced on every request, in one place |
| Money + stock must never corrupt | **Postgres transactions** + row locks | Atomic sale = no overselling, no half-written invoices |
| Data-dense admin UI (tables, POS, reports) | **Next.js (React)** | Best for dashboards; SSR ready if you add public ordering later |
| Fast forms + server state | React Query + react-hook-form + zod | Standard, well-documented, solo-friendly |

Not using Firebase. Not using Flutter. Everything is web + REST.

---

<a name="multi-tenant"></a>
## 2. What "multi-tenant" means here (READ FIRST)

Every pharmacy is a **tenant**. One app, one database, but each tenant sees only its own data.

**The strategy: shared database + `tenantId` column.**

```
sales
| id | tenantId | invoiceNo | total | createdAt |
|----|----------|-----------|-------|-----------|
| 1  | pharma-5 | INV-0001  | 150   | ...       |
| 2  | pharma-8 | INV-0001  | 200   | ...       |   <- same invoiceNo, different tenant, both fine
```

**The one rule that must never break:**

> Every tenant-scoped database query MUST be filtered by the `tenantId` of the logged-in user, taken from the **JWT token** — never from the request body. Miss it once and Pharmacy A can read Pharmacy B's data. This is the #1 security risk of a SaaS.

**How we enforce it (not by hand on every query):**
1. Login issues a JWT that contains `tenantId` + `userId` + `role`.
2. A NestJS **guard** reads the JWT and puts `tenantId` into a request-scoped `TenantContext`.
3. A **Prisma client extension** auto-injects `where: { tenantId }` on every read/write for tenant-scoped models, and auto-sets `tenantId` on create. Developers cannot forget it.
4. The **super-admin** realm is separate: platform-level tables (Tenant, PlatformAdmin, Subscription) are NOT tenant-scoped and are reachable only through a separate super-admin guard.

**Tenant resolution:** primary source is the JWT claim. Subdomain (`lazz.pharmasaas.app`) is optional and used only for branding/login routing, never as the security boundary.

---

<a name="architecture"></a>
## 3. Architecture at a glance

```mermaid
flowchart LR
  subgraph Staff["Pharmacy Staff — Next.js (browser)"]
    S1[Login]
    S2[Inventory / Batches]
    S3[Purchase / Stock-in]
    S4[POS / Sale]
    S5[Reports]
    S6[Settings / Branding]
  end
  subgraph Admin["Super-Admin — Next.js (browser)"]
    A1[Create / Suspend Pharmacy]
    A2[Plans & Manual Billing]
  end
  subgraph API["NestJS REST API"]
    G[Auth + Tenant Guard]
    M1[Catalog]
    M2[Purchase]
    M3[Inventory/FEFO]
    M4[Sales/POS]
    M5[Reports]
    M6[Super-Admin]
  end
  DB[(PostgreSQL<br/>shared, tenantId-scoped)]
  Staff -->|JWT| G
  Admin -->|JWT superadmin| G
  G --> M1 & M2 & M3 & M4 & M5 & M6
  M1 & M2 & M3 & M4 & M5 & M6 --> DB
```

---

<a name="clean-architecture"></a>
## 4. Clean, swappable architecture (NestJS)

Golden rule: **the database and framework are details.** Business rules live in services, not in controllers or Prisma calls scattered around.

**Layers (backend):**

```mermaid
flowchart TB
  CTRL["controllers<br/>HTTP in/out, validation (DTO)"]
  SVC["services<br/>business rules: FEFO, stock, billing"]
  REPO["repositories<br/>Prisma access, tenant-scoped"]
  DB["Prisma + Postgres"]
  CTRL --> SVC --> REPO --> DB
```

- **controllers** — receive requests, validate DTOs (class-validator), return responses. No business logic.
- **services** — all rules: FEFO deduction, stock checks, invoice numbering, valuation, billing status. Testable without HTTP.
- **repositories** — the only place Prisma is touched; tenant filter applied here (plus the global extension as a safety net).
- **modules** — one Nest module per domain: `AuthModule`, `TenantModule`, `SuperAdminModule`, `CatalogModule`, `SupplierModule`, `PurchaseModule`, `InventoryModule`, `SalesModule`, `ReportModule`, `SettingsModule`.

Pragmatic, not enterprise. Don't over-abstract. Interfaces only where you'd realistically swap the implementation (e.g. `ReceiptRenderer`, `Notifier`).

---

<a name="data-model"></a>
## 5. The data model (canonical)

This is the single source of truth referenced by every step below. Prisma-style, PostgreSQL.

**Platform level (NOT tenant-scoped — super-admin only):**

- `PlatformAdmin(id, name, email unique, passwordHash, role='SUPERADMIN', createdAt)`
- `Tenant(id, name, subdomain unique, status enum[TRIAL,ACTIVE,SUSPENDED], plan enum[BASIC,STANDARD,PREMIUM], trialEndsAt, createdAt)`
- `Subscription(id, tenantId -> Tenant, plan, amount numeric, billingStatus enum[PAID,DUE,OVERDUE], periodStart date, periodEnd date, validTill date, note, markedByAdminId, createdAt)`  — manual billing ledger
- `TenantSettings(tenantId PK -> Tenant, appName, logoUrl, primaryColor, secondaryColor, address, phone, receiptHeader, receiptFooter, vatPercent numeric default 0, currency default 'BDT', timezone default 'Asia/Dhaka')`

**Tenant-scoped (every row has `tenantId`, auto-filtered):**

- `User(id, tenantId, name, email, passwordHash, role enum[OWNER,MANAGER,PHARMACIST,CASHIER], status enum[ACTIVE,DISABLED], createdAt, unique(tenantId,email))`
- `Category(id, tenantId, name)`
- `Supplier(id, tenantId, name, phone, address, dueBalance numeric default 0)`
- `Product(id, tenantId, name, genericName, brand, form enum[TABLET,CAPSULE,SYRUP,INJECTION,CREAM,DROPS,OTHER], strength, unit default 'pcs', categoryId -> Category, rackLocation, reorderLevel int default 10, defaultSellPrice numeric, status enum[ACTIVE,INACTIVE], createdAt)`  — the medicine master (one row per medicine)
- `Batch(id, tenantId, productId -> Product, batchNo, expiryDate date, quantity int check(>=0), costPrice numeric, sellPrice numeric, supplierId -> Supplier, purchaseItemId, receivedAt)`  — a stock lot; a product has many batches
- `StockMovement(id, tenantId, productId, batchId, type enum[PURCHASE,SALE,ADJUSTMENT,RETURN_IN,RETURN_OUT], quantity int (signed +/-), balanceAfter int, refType, refId, note, createdByUserId, createdAt)`  — append-only ledger; source of truth for audit
- `Purchase(id, tenantId, supplierId, invoiceNo, purchaseDate, subtotal, discount numeric default 0, total, paidAmount numeric default 0, createdByUserId, createdAt)`
- `PurchaseItem(id, purchaseId -> Purchase, productId, batchNo, expiryDate, quantity, costPrice, sellPrice)`
- `Customer(id, tenantId, name, phone)`  — optional walk-in support
- `Sale(id, tenantId, invoiceNo, customerId nullable, subtotal, discountAmount default 0, vatAmount default 0, total, paidAmount, changeAmount default 0, paymentMethod enum[CASH,BKASH,CARD,DUE], status enum[COMPLETED,VOID] default COMPLETED, createdByUserId, createdAt)`
- `SaleItem(id, saleId -> Sale, productId, batchId, quantity, unitPrice, costPrice, lineDiscount default 0, lineTotal)`  — costPrice snapshotted for profit reports

`invoiceNo` is **sequential per tenant** (e.g. `INV-000123`), generated server-side.

```mermaid
erDiagram
  Tenant ||--o{ User : has
  Tenant ||--|| TenantSettings : has
  Tenant ||--o{ Subscription : billed
  Tenant ||--o{ Product : owns
  Product ||--o{ Batch : "has lots"
  Product ||--o{ SaleItem : sold_as
  Batch ||--o{ SaleItem : deducted_from
  Supplier ||--o{ Purchase : supplies
  Purchase ||--o{ PurchaseItem : contains
  Sale ||--o{ SaleItem : contains
  Product ||--o{ StockMovement : ledger
```

---

<a name="business-rules"></a>
## 6. Core business rules

These are non-negotiable; every relevant step's prompt repeats the ones it needs.

- **FEFO (First-Expire-First-Out):** when selling a product, deduct from the batch with the **nearest non-expired expiry date** that still has stock, then the next, etc. (Not FIFO — pharmacy must ship soon-to-expire stock first.)
- **No expired sales:** never deduct from a batch whose `expiryDate < today`. Expired stock is blocked from POS and flagged in reports.
- **No negative stock:** a sale that exceeds available (non-expired) stock is rejected atomically — nothing is written.
- **Atomic sale:** creating a Sale runs in ONE Postgres transaction: lock candidate batches (`FOR UPDATE`), deduct FEFO, insert Sale + SaleItems, write StockMovement rows, update Batch quantities, generate invoiceNo. Any failure rolls back the whole thing.
- **Atomic purchase:** a Purchase creates PurchaseItems, creates/updates Batches, and writes PURCHASE StockMovements in one transaction.
- **Current stock** of a product = SUM of its batches' `quantity`. (Derived; the ledger is the audit trail.)
- **Low-stock alert:** current stock ≤ `reorderLevel`.
- **Expiry alert:** any batch with `expiryDate` within N days (configurable, default 60), and `quantity > 0`.
- **Stock valuation** = SUM(`batch.quantity * batch.costPrice`) over non-expired batches.
- **Profit** on a sale line = `(unitPrice - costPrice) * quantity - lineDiscount`; costPrice comes from the batch actually deducted.
- **Tenant status gate:** if a tenant is `SUSPENDED`, staff logins are blocked (read-only or full block — your choice; default: block with a "contact admin / billing due" message). Super-admin sets this manually.
- **Roles:** OWNER (all), MANAGER (all except delete users/settings), PHARMACIST (inventory + POS), CASHIER (POS only). Enforced by a role guard.

---

<a name="decisions"></a>
## 7. Decisions baked in (change any before you start)

- Backend **NestJS + Prisma + PostgreSQL**. Frontend **Next.js (App Router) + TypeScript + Tailwind + shadcn/ui + TanStack Query + react-hook-form + zod**.
- **Monorepo** (one folder, `apps/api` + `apps/web` + `packages/shared` for shared TS types/enums).
- Multi-tenant = **shared DB + `tenantId`**, enforced by a Prisma extension (upgrade to Postgres Row-Level Security later if you want defense-in-depth).
- Auth = **email + password**, **JWT access + refresh** tokens. Separate token audiences for staff vs super-admin.
- Billing = **manual** in v1: super-admin marks a tenant's subscription PAID/DUE and sets `validTill`. No payment gateway yet.
- **No customer online ordering** in v1, but the schema (Customer, Product, Batch) is designed so it bolts on later.
- Money = `numeric` (never float). Currency **BDT** default, configurable per tenant.
- Receipts: **80mm thermal** (default) + **A4** HTML/PDF, branded from `TenantSettings`.
- **File storage = your own server** (self-hosted local disk) behind a swappable `StorageProvider` interface. Swap to S3 / Supabase / any CDN later by adding one implementation and flipping an env var — no call-site changes. No third-party storage required in v1.
- Timezone **Asia/Dhaka**; all timestamps stored UTC, displayed in tenant timezone.

---

<a name="before-you-start"></a>
## 8. Before you start (one-time setup)

1. **Install tools:** Node.js (LTS), PostgreSQL (local, or a free cloud DB like Neon/Supabase/Railway), VS Code + Claude Code, and a REST client (Postman or Thunder Client) to test the API before any UI exists.
2. **Create the project folder** `pharmasaas/` and open it in your editor.
3. Have a Postgres **connection string** ready (`postgresql://user:pass@host:5432/pharmasaas`). You'll paste it into `.env` when Step 1 asks.
4. Read sections 2, 5, 6 above once. Everything else follows from them.

---

<a name="how-to-use"></a>
## 9. How to use this guide (the loop)

1. Paste **Step 0 (Master Spec)** → the AI scaffolds the monorepo, confirms the plan. It writes **no feature code** yet.
2. Paste **Step 1** → it writes the Prisma schema + first migration → you run the migration and confirm tables exist.
3. Paste **Steps 2 → onward in order.** After each step: the AI builds, **you run and test that part** (via Postman for API steps, browser for UI steps), report issues, it fixes, then next.
4. Do **not** skip ahead. Small steps = better code and easier debugging.

**Who does what**

| You | AI |
|---|---|
| Provide Postgres URL, run migrations | Write Prisma schema, services, controllers |
| Test each endpoint (Postman) / screen (browser) | Build API modules + Next.js pages |
| Create the first super-admin + first tenant | Wire auth, tenant guard, FEFO, POS, receipts |
| Report bugs, confirm behavior | Fix, refine, add tests |

**Guardrails to repeat to the AI if it drifts:** web only (no Flutter/mobile); every tenant query filtered by `tenantId` from the JWT; money as `numeric`; secrets only in `.env`; sales and purchases in transactions; no online ordering in v1.

---

<a name="design-system"></a>
## 10. Design system (staff web)

Feel: **clean, calm, fast, medical-trustworthy.** Dense tables must stay readable; POS must be keyboard-fast.

**Color tokens** (calm teal + slate — replace with your brand later; these are also the per-tenant white-label **defaults**)

| Token | Light | Dark |
|---|---|---|
| primary | `#0E7C6B` | `#2DD4BF` |
| primary-dark | `#0B5E52` | `#14B8A6` |
| accent (totals, CTA) | `#2563EB` | `#60A5FA` |
| success | `#16A34A` | `#22C55E` |
| warning (expiry soon) | `#D97706` | `#FBBF24` |
| danger (expired, low stock) | `#DC2626` | `#F87171` |
| bg | `#FFFFFF` | `#0B1220` |
| surface | `#F5F7FA` | `#131C2E` |
| text | `#0F172A` | `#E6EDF6` |
| muted | `#64748B` | `#94A3B8` |
| border | `#E2E8F0` | `#233043` |

**Typography** — UI **Inter**; numbers/tables **tabular-nums**; Bengali labels **Hind Siliguri / Noto Sans Bengali**. Scale: h1 24/700, h2 20/600, body 14/400, table 13/500, caption 12/500.

**Layout** — left sidebar nav + top bar (tenant name/logo, user menu). Content max-width for forms, full-width for tables. 8pt spacing grid. Data tables: sticky header, zebra rows, right-aligned numbers.

**POS screen** — split layout: left = product search + cart lines; right = totals + payment. Barcode/enter-key driven. Big total, big "Complete Sale" button. Minimal mouse.

**Motion** — subtle only: 150ms transitions, toast on save (sonner). Respect `prefers-reduced-motion`. No decorative animation on data screens.

**Branding note** — primary color, logo, appName come from `TenantSettings` at runtime (white-label). Apply via CSS variables set after login; never hardcode a tenant's color.

---

<a name="the-steps"></a>
# 11. The Steps

Each step is a prompt. Copy the fenced block, paste to the AI, then do the **"After this step"** action. Steps assume the AI has the Master Spec (Step 0) in context.

---

## Step 0 — Master Spec (paste first)

```
You are a senior full-stack engineer. Build a production, multi-tenant pharmacy SaaS called "PharmaSaaS" as a TypeScript monorepo. This message is the SPEC. Do NOT write feature code yet — scaffold the repo, confirm the plan and the data model back to me, then wait for step-by-step build prompts.

## Product
A web-based, multi-tenant SaaS sold to many pharmacies. One app, one database, isolated data per pharmacy (tenant). v1 scope = pharmacy STAFF web app: inventory, purchase (stock-in), POS (sale), batch/expiry tracking (FEFO), receipts, reports, settings — PLUS a super-admin area for the platform owner to create pharmacies, set plans, and mark bills paid manually.
WEB ONLY. No mobile app, no Flutter. No customer-facing online ordering in v1 (but design the schema so it can be added later without rework).

## Monorepo layout (use a workspace: pnpm or npm workspaces)
pharmasaas/
  apps/
    api/        # NestJS backend
    web/        # Next.js (App Router) frontend
  packages/
    shared/     # shared TypeScript types + enums (roles, statuses, payment methods)
  README.md     # setup + run instructions
  .env.example

## Stack (use exactly)
- Backend: NestJS + Prisma ORM + PostgreSQL. Validation: class-validator + class-transformer. Auth: JWT (access + refresh) with passport-jwt. Password hashing: argon2 (or bcrypt). Config via @nestjs/config + .env. Testing: Jest.
- Frontend: Next.js (App Router) + TypeScript + Tailwind CSS + shadcn/ui + TanStack Query + react-hook-form + zod + axios. State from server via React Query; auth token in httpOnly cookie or memory + refresh.
- Shared: a packages/shared with enums and DTO types imported by both apps.
- File storage: a swappable StorageProvider abstraction. DEFAULT implementation = LOCAL DISK on OUR OWN SERVER (self-hosted), NOT Supabase and NOT any third-party. It must be swappable to S3/Supabase/CDN later by adding one new implementation class + one env change, with zero changes at the call sites.

## Multi-tenancy (CRITICAL — get this right)
Shared database + tenantId column on every tenant-scoped table.
- Login issues a JWT containing { userId, tenantId, role } for staff, or { adminId, role: 'SUPERADMIN' } for platform admins (separate token audience/secret).
- A NestJS request-scoped TenantContext holds the current tenantId, populated by an AuthGuard from the JWT.
- A Prisma Client extension auto-injects `where: { tenantId }` on findMany/findFirst/update/delete and auto-sets tenantId on create, for all tenant-scoped models. Developers must not be able to forget it.
- NEVER read tenantId from the request body/query — only from the verified JWT.
- Platform tables (PlatformAdmin, Tenant, Subscription) are NOT tenant-scoped and are reachable only via a separate SuperAdminGuard.
- Subdomain is optional and used only for branding/login routing, never as the security boundary.

## Data model — create exactly these (Prisma)
Platform (not tenant-scoped):
- PlatformAdmin(id, name, email @unique, passwordHash, role default 'SUPERADMIN', createdAt)
- Tenant(id, name, subdomain @unique, status enum[TRIAL,ACTIVE,SUSPENDED] default TRIAL, plan enum[BASIC,STANDARD,PREMIUM] default BASIC, trialEndsAt, createdAt)
- Subscription(id, tenantId, plan, amount Decimal, billingStatus enum[PAID,DUE,OVERDUE] default DUE, periodStart, periodEnd, validTill, note, markedByAdminId, createdAt)
- TenantSettings(tenantId @id, appName, logoUrl, primaryColor, secondaryColor, address, phone, receiptHeader, receiptFooter, vatPercent Decimal default 0, currency default 'BDT', timezone default 'Asia/Dhaka')
Tenant-scoped (tenantId on each):
- User(id, tenantId, name, email, passwordHash, role enum[OWNER,MANAGER,PHARMACIST,CASHIER], status enum[ACTIVE,DISABLED] default ACTIVE, createdAt, @@unique([tenantId, email]))
- Category(id, tenantId, name)
- Supplier(id, tenantId, name, phone, address, dueBalance Decimal default 0)
- Product(id, tenantId, name, genericName, brand, form enum[TABLET,CAPSULE,SYRUP,INJECTION,CREAM,DROPS,OTHER], strength, unit default 'pcs', categoryId, rackLocation, reorderLevel Int default 10, defaultSellPrice Decimal, status enum[ACTIVE,INACTIVE] default ACTIVE, createdAt)
- Batch(id, tenantId, productId, batchNo, expiryDate, quantity Int, costPrice Decimal, sellPrice Decimal, supplierId, purchaseItemId, receivedAt)
- StockMovement(id, tenantId, productId, batchId, type enum[PURCHASE,SALE,ADJUSTMENT,RETURN_IN,RETURN_OUT], quantity Int (signed), balanceAfter Int, refType, refId, note, createdByUserId, createdAt)  -- append-only ledger
- Purchase(id, tenantId, supplierId, invoiceNo, purchaseDate, subtotal Decimal, discount Decimal default 0, total Decimal, paidAmount Decimal default 0, createdByUserId, createdAt)
- PurchaseItem(id, purchaseId, productId, batchNo, expiryDate, quantity Int, costPrice Decimal, sellPrice Decimal)
- Customer(id, tenantId, name, phone)
- Sale(id, tenantId, invoiceNo, customerId?, subtotal Decimal, discountAmount Decimal default 0, vatAmount Decimal default 0, total Decimal, paidAmount Decimal, changeAmount Decimal default 0, paymentMethod enum[CASH,BKASH,CARD,DUE], status enum[COMPLETED,VOID] default COMPLETED, createdByUserId, createdAt)
- SaleItem(id, saleId, productId, batchId, quantity Int, unitPrice Decimal, costPrice Decimal, lineDiscount Decimal default 0, lineTotal Decimal)
Use Decimal (not Float) for all money. invoiceNo is sequential PER TENANT.

## Business rules (implement when we reach each module)
- FEFO: on sale, deduct from the nearest non-expired expiry batch first, then next.
- Never sell expired batches; never allow negative stock; reject atomically.
- Sale and Purchase each run in ONE transaction (lock rows FOR UPDATE where needed).
- Current stock = SUM(batch.quantity). Low stock = stock <= reorderLevel. Expiry alert = batch expiring within N days (default 60) with quantity > 0. Valuation = SUM(quantity*costPrice) over non-expired batches.
- Roles: OWNER(all), MANAGER(all except delete users/settings), PHARMACIST(inventory+POS), CASHIER(POS only). Enforce via a RolesGuard.
- Suspended tenant => staff login blocked with a billing-due message.

## Non-negotiable guardrails
- Web only. No Flutter, no React Native, no mobile.
- Every tenant query filtered by tenantId from the JWT, via the Prisma extension. No exceptions.
- Money as Decimal. Secrets only in .env (provide .env.example). No secrets committed.
- Consistent REST: /api/v1/... , DTOs validated, meaningful HTTP status codes, a global error filter returning { message, code }.
- File uploads go to OUR OWN SERVER (self-hosted disk) via a StorageProvider interface — never hardcode Supabase or any third-party SDK at a call site. Files are tenant-scoped and served through the authenticated API, not from an open/public directory.

## Deliver for THIS step only
1. Create the monorepo structure and workspace config.
2. Initialize apps/api (NestJS) and apps/web (Next.js) and packages/shared, wired to build.
3. Add .env.example (DATABASE_URL, JWT secrets, PORT) and a README with run instructions.
4. Echo back: the final folder tree, the confirmed data model, and the ordered list of build steps you expect. Write NO feature code, NO Prisma schema yet — that's Step 1.
```

**After this step:** confirm the folder tree and README exist; `npm install` (or `pnpm install`) runs clean; both apps start (empty). Then paste Step 1.

---

## Step 1 — Database schema + Prisma + first migration

```
Using the data model in the Master Spec, create the Prisma schema for apps/api.

Requirements:
1. Write prisma/schema.prisma with ALL platform and tenant-scoped models, enums, relations, and indexes exactly as specified. Add @@index on every tenantId, and composite indexes: Product(tenantId, name), Batch(tenantId, productId, expiryDate), Sale(tenantId, createdAt), StockMovement(tenantId, productId, createdAt).
2. Use Decimal for money, DateTime for timestamps (store UTC), Date for expiryDate/periodStart/etc.
3. Configure the Prisma datasource from env DATABASE_URL.
4. Create the initial migration and a prisma generate. Give me the exact commands to run.
5. Write a seed script (prisma/seed.ts) that creates: one PlatformAdmin (email/password from env or defaults printed to console), one demo Tenant "Demo Pharmacy" (status ACTIVE) with TenantSettings, one OWNER User for it, 3 Categories, 2 Suppliers, and ~10 Products with 1-2 Batches each (varied expiry dates, some near expiry). No real data.
6. Do NOT build the tenant Prisma extension yet — that's Step 2. Keep this step to schema + migration + seed only.

Output the schema, the commands, and the seed file. Explain any index choices in one line each.
```

**After this step:** run the migration against your Postgres; run the seed; open the DB (Prisma Studio / pgAdmin) and confirm tables + demo rows exist. Report the row counts back.

---

## Step 2 — Auth + tenant isolation (the security core)

```
Build authentication and multi-tenant isolation for apps/api. This is the security backbone — be strict.

## Staff auth
- POST /api/v1/auth/login { email, password, subdomain? }: find the User by email within the tenant (resolve tenant by subdomain if provided, else the user's tenant if email is globally unique per your seed — clarify and pick: I want email unique PER TENANT, so require subdomain OR a tenant selector; implement login as { subdomain, email, password }). Verify argon2 hash. If tenant.status = SUSPENDED, reject with 403 "Account suspended - billing due". Issue JWT access (15m) + refresh (7d) containing { userId, tenantId, role, typ:'staff' }. Return user profile + tenant branding (appName, logoUrl, primaryColor).
- POST /api/v1/auth/refresh, POST /api/v1/auth/logout.
- GET /api/v1/auth/me -> current user + tenant.

## Guards & context
- AuthGuard (passport-jwt) validates the access token, rejects staff tokens on super-admin routes and vice versa (check typ claim).
- A request-scoped TenantContext service holds { tenantId, userId, role }, populated from the JWT by the guard.
- RolesGuard + @Roles(...) decorator enforcing OWNER/MANAGER/PHARMACIST/CASHIER per route.

## Prisma tenant extension (CRITICAL)
- Build a Prisma Client extension (or middleware) that, for all TENANT-SCOPED models only, injects `where: { tenantId }` into findMany/findFirst/findUnique/update/updateMany/delete/deleteMany/count/aggregate, and sets `data.tenantId` on create/createMany, using TenantContext.tenantId.
- Platform models (PlatformAdmin, Tenant, Subscription, TenantSettings-by-admin) must be EXEMPT and only used via a super-admin path.
- If TenantContext has no tenantId on a tenant-scoped query, THROW (fail closed), never run unscoped.
- Write a unit test proving: given tenant A's context, a findMany on Product cannot return tenant B's rows, and a create cannot set a foreign tenantId from the body.

## Security hygiene
- Passwords argon2. Rate-limit login (e.g. @nestjs/throttler). Never return passwordHash. Global exception filter -> { message, code }. Validate all DTOs.

Deliver the auth module, guards, tenant context, Prisma extension, and the isolation test. Give me curl/Postman examples for login, me, refresh.
```

**After this step:** log in as the seeded OWNER via Postman, get a token, call `/auth/me`. Try to read products with tenant A's token and confirm you cannot see tenant B's data (seed a second tenant if needed). Confirm the isolation test passes.

---

## Step 3 — Super-admin area (tenants, plans, manual billing)

```
Build the super-admin (platform owner) module for apps/api. Separate auth realm from staff.

## Super-admin auth
- POST /api/v1/admin/auth/login { email, password } against PlatformAdmin. Issue a JWT with { adminId, role:'SUPERADMIN', typ:'admin' } and a DIFFERENT secret/audience than staff tokens. SuperAdminGuard accepts only typ='admin'.

## Tenant management (SuperAdminGuard only, NOT tenant-scoped)
- POST /api/v1/admin/tenants: create a Tenant { name, subdomain, plan } + default TenantSettings + the first OWNER User { name, email, tempPassword }. Return the created tenant and the owner login info. Do this in a transaction. Enforce unique subdomain and unique owner email within the tenant.
- GET /api/v1/admin/tenants (list + filters: status, plan, search), GET /:id (detail incl. current subscription + basic usage counts: users, products, sales this month).
- PATCH /api/v1/admin/tenants/:id/status { status } to ACTIVE/SUSPENDED (suspend blocks staff login).
- PATCH /api/v1/admin/tenants/:id/plan { plan }.

## Manual billing
- POST /api/v1/admin/tenants/:id/subscription { plan, amount, periodStart, periodEnd, validTill, billingStatus, note }: record a Subscription row (the manual invoice/payment). markedByAdminId = current admin.
- GET /api/v1/admin/tenants/:id/subscriptions (history).
- A helper that computes a tenant's current billing state (latest subscription: PAID and validTill>=today => good; else DUE/OVERDUE). Optionally auto-suspend when overdue past a grace period — expose as a manual action for now, not a cron.

## Rules
- All these routes bypass the tenant Prisma extension (platform models) and are reachable ONLY with a super-admin token.
- Never expose staff endpoints to admin tokens or vice versa.

Deliver the module, guard, DTOs, and Postman examples. Include a test that a staff token gets 403 on every /admin route.
```

**After this step:** log in as PlatformAdmin, create a new tenant + owner, log in as that new owner on the staff side, suspend the tenant and confirm the owner can no longer log in. Record a subscription and read the history.

---

## Step 4 — Catalog: categories, suppliers, products (medicines)

```
Build the CatalogModule and SupplierModule for apps/api (all tenant-scoped, tenant extension applies automatically).

## Categories  (roles: OWNER, MANAGER, PHARMACIST for write; all staff read)
- CRUD /api/v1/categories. Prevent delete if products reference it (return 409).

## Suppliers  (roles: OWNER, MANAGER)
- CRUD /api/v1/suppliers { name, phone, address }. dueBalance is read-only here (updated by purchases later). List with search + pagination.

## Products / medicines  (roles: OWNER, MANAGER, PHARMACIST)
- CRUD /api/v1/products with fields from the data model (name, genericName, brand, form, strength, unit, categoryId, rackLocation, reorderLevel, defaultSellPrice, status).
- GET /api/v1/products supports: search (name/generic/brand), filter by category/form/status, pagination, and each row should include computed currentStock = SUM of its batches' quantity (efficient query, not N+1).
- GET /api/v1/products/:id includes its batches (batchNo, expiryDate, quantity, costPrice, sellPrice), sorted by expiryDate asc.
- Soft behavior: setting status INACTIVE hides from POS search but keeps history. Do not hard-delete a product that has sales/batches (return 409, suggest deactivate).
- Validate: no negative prices, reorderLevel >= 0, expiry handling belongs to batches not product.

Deliver DTOs (class-validator), services with business rules, controllers, and Postman examples. Keep all queries tenant-safe (rely on the extension; still pass no tenantId from the client).
```

**After this step:** via Postman create a category, a supplier, and a few products; list products and confirm `currentStock` reflects the seeded batches; confirm you cannot delete a category in use.

---

## Step 5 — Purchase (stock-in) + batches + ledger

```
Build the PurchaseModule for apps/api. This is how stock ENTERS the system. Tenant-scoped. Roles: OWNER, MANAGER, PHARMACIST.

## Create purchase (atomic, one transaction)
POST /api/v1/purchases {
  supplierId, invoiceNo, purchaseDate, discount?, paidAmount?,
  items: [{ productId, batchNo, expiryDate, quantity, costPrice, sellPrice }]
}
In ONE Prisma transaction:
1. Validate every productId belongs to this tenant and is ACTIVE.
2. Create the Purchase + PurchaseItems. Compute subtotal (sum quantity*costPrice), total = subtotal - discount.
3. For each item: find an existing Batch by (productId, batchNo, expiryDate); if found, increment quantity; else create a new Batch (link supplierId, purchaseItemId, receivedAt=now). Update batch costPrice/sellPrice to the latest.
4. Write a StockMovement PURCHASE row per item (quantity = +qty, balanceAfter = product's new total stock, refType='PURCHASE', refId=purchase.id).
5. Update supplier.dueBalance += (total - paidAmount).
Reject the whole thing on any invalid item. Return the created purchase with items and resulting batches.

## Read
- GET /api/v1/purchases (list: filter by supplier, date range, search invoiceNo; pagination; totals).
- GET /api/v1/purchases/:id (full detail).

## Notes
- Purchases are immutable once created in v1 (no edit); to correct, do a stock ADJUSTMENT (Step 6) or a purchase return (later). State this in the response docs.
- Expiry dates in the past should warn but you may allow (return a warning flag) — pharmacies sometimes log old stock. Make it a validation warning, not a hard block; confirm with me if unsure and default to: block expiryDate < today with 422.

Deliver module, DTOs, transactional service, Postman examples. Prove atomicity: a purchase with one bad item writes nothing.
```

**After this step:** create a purchase with 2-3 items; confirm new batches appear, product `currentStock` increased, StockMovement rows written, and supplier dueBalance updated. Try a purchase with a bad productId and confirm nothing was written.

---

## Step 6 — Inventory: stock views, FEFO helper, adjustments, alerts

```
Build the InventoryModule for apps/api. Tenant-scoped. This exposes stock truth + the FEFO engine that POS will use.

## Stock views  (all staff read)
- GET /api/v1/inventory/stock: per-product currentStock (SUM batches), reorderLevel, lowStock flag, nearest expiry. Filters: lowStockOnly, search, category. Pagination.
- GET /api/v1/inventory/batches: batch-level list with product, batchNo, expiryDate, quantity, costPrice, sellPrice, daysToExpiry. Filters: productId, expiringWithinDays, expiredOnly.
- GET /api/v1/inventory/alerts: { lowStock: [...], expiringSoon: [...within N days, default 60...], expired: [...qty>0, expiryDate<today...] }.
- GET /api/v1/inventory/valuation: total = SUM(quantity*costPrice) over non-expired batches, plus breakdown by category.

## FEFO helper (used by Sales in Step 7 — build + unit-test here)
- A service method allocateFEFO(productId, quantity, tx) that returns an ordered list of { batchId, take } from non-expired batches (expiryDate >= today, quantity > 0), nearest expiry first, until quantity is satisfied. If total available < requested, throw InsufficientStock with the shortfall. It must run inside a transaction and lock the selected batch rows (SELECT ... FOR UPDATE) to prevent races.
- Unit-test: product with 3 batches (exp Jan/Mar/Jun, qty 5/5/5); requesting 8 returns take 5 from Jan + 3 from Mar; requesting 20 throws; an expired batch is skipped.

## Stock adjustment  (roles: OWNER, MANAGER)
- POST /api/v1/inventory/adjustments { batchId, quantityChange (+/-), reason }: apply the change in a transaction, never let a batch go below 0, write a StockMovement ADJUSTMENT row with balanceAfter and note=reason.

Deliver module, services, the FEFO unit tests, Postman examples. Keep it all tenant-safe.
```

**After this step:** call the alerts and valuation endpoints against seeded data; run the FEFO unit tests; do a manual adjustment and confirm the batch qty + ledger updated.

---

## Step 7 — POS / Sales (the money path, atomic)

```
Build the SalesModule for apps/api. This is the POS sale — the most important transaction. Tenant-scoped. Roles: OWNER, MANAGER, PHARMACIST, CASHIER.

## Create sale (ONE transaction, must be atomic and race-safe)
POST /api/v1/sales {
  customerId?, paymentMethod, paidAmount, discountAmount?, vatPercent? (default from TenantSettings),
  items: [{ productId, quantity, unitPrice?, lineDiscount? }]   // unitPrice defaults to product/batch sellPrice
}
In ONE Prisma transaction:
1. For each item, call allocateFEFO(productId, quantity, tx) (from Step 6). This locks batches, picks nearest-expiry non-expired stock, and splits the line across batches as needed. Reject the WHOLE sale if any item is short (return which product + shortfall), writing nothing.
2. Build SaleItem rows per (batch allocation): quantity, unitPrice, costPrice (from the batch), lineDiscount, lineTotal. One requested line may become several SaleItems if split across batches.
3. Compute subtotal = sum(lineTotal), apply discountAmount, compute vatAmount from vatPercent, total = subtotal - discount + vat. changeAmount = paidAmount - total (>=0; if paymentMethod=DUE, allow paidAmount < total and track the rest — for v1 keep DUE simple: paidAmount can be less, no customer ledger yet unless customerId given).
4. Generate invoiceNo sequential PER TENANT (e.g. a per-tenant counter row locked in the tx, format INV-000123).
5. Decrement each Batch.quantity by the allocated amount. Write a StockMovement SALE row per allocation (quantity negative, balanceAfter, refType='SALE', refId=sale.id).
6. Insert Sale + SaleItems. Return the full sale with items, batch info, and computed totals for the receipt.

## Other endpoints
- GET /api/v1/sales (list: date range, cashier, paymentMethod, search invoiceNo; pagination; totals).
- GET /api/v1/sales/:id (full detail for reprint).
- POST /api/v1/sales/:id/void (roles OWNER, MANAGER): reverse the sale in a transaction — restock each SaleItem's batch, write RETURN_IN StockMovements, set status VOID. Block if already VOID. (Keep it simple: full void only, no partial returns in v1.)
- GET /api/v1/products/search-pos?q= : fast lookup for POS (active products with currentStock>0, nearest sellPrice + batch expiry), limit 20, name/generic/brand match. Optimize for speed.

## Rules
- Never oversell, never sell expired stock, never write a partial sale. All-or-nothing.
- Concurrency: two cashiers selling the last unit — the FOR UPDATE lock in allocateFEFO must make one succeed and one get InsufficientStock. Add a test simulating this.

Deliver module, transactional service, DTOs, concurrency test, Postman examples.
```

**After this step:** make a sale via Postman; confirm batch quantities dropped by FEFO (nearest expiry first), StockMovement SALE rows written, invoiceNo incremented, totals correct. Void the sale and confirm stock restored. Try to oversell and confirm clean rejection.

---

## Step 8 — Receipts & invoices (branded, printable)

```
Build receipt/invoice generation. Backend renders data; frontend prints. Tenant-scoped, branded from TenantSettings.

## Backend (apps/api)
- GET /api/v1/sales/:id/receipt: return a normalized receipt payload = tenant branding (appName, logoUrl, address, phone, receiptHeader, receiptFooter, vatPercent, currency) + sale (invoiceNo, date in tenant timezone, cashier name, customer?, items[{ name, strength, batchNo, expiryDate, quantity, unitPrice, lineTotal }], subtotal, discount, vat, total, paid, change, paymentMethod). This single endpoint feeds both thermal and A4 rendering.
- Optional: a server-side PDF (A4) via a lib (e.g. pdfkit or puppeteer) at GET /api/v1/sales/:id/receipt.pdf — if it complicates deploy, skip and let the frontend print instead. Recommend frontend print for v1.

## Frontend (apps/web) — build the print views
- An 80mm thermal receipt component (monospace, narrow, logo optional, itemized, totals, footer) and an A4 invoice component. Both consume the receipt payload.
- A print route/modal that opens the browser print dialog with only the receipt visible (print CSS: @media print, hide app chrome). Thermal = default.
- "Reprint" from any past sale.

## Rules
- All branding from TenantSettings (white-label). Never hardcode a pharmacy's name/logo.
- Money formatting from tenant currency; dates in tenant timezone.

Deliver the receipt endpoint, the two print components, print CSS, and the reprint flow. Show a sample rendered receipt with the seeded data.
```

**After this step:** open a completed sale, print the thermal receipt (browser dialog), confirm branding, items, batch/expiry, and totals are correct; reprint an older sale.

---

## Step 9 — Reports & dashboard

```
Build the ReportModule (apps/api) and the dashboard (apps/web). Tenant-scoped. Roles: OWNER, MANAGER (read); PHARMACIST limited.

## Backend endpoints (efficient SQL/Prisma aggregates, date-range params, tenant-safe)
- GET /api/v1/reports/summary?from&to: totalSales, totalRevenue, totalProfit (sum over SaleItems of (unitPrice-costPrice)*qty - lineDiscount), salesCount, avgBasket, by paymentMethod.
- GET /api/v1/reports/sales-trend?from&to&granularity=day|week: series for a chart.
- GET /api/v1/reports/top-products?from&to&limit: by quantity and by revenue.
- GET /api/v1/reports/inventory: current valuation, lowStock count, expiringSoon count, expired count + value.
- GET /api/v1/reports/expiry?withinDays: batches expiring, grouped, with value at risk.
- GET /api/v1/reports/purchases?from&to: totals by supplier, outstanding dueBalance.
- All numbers computed from the ledger/tables, tenant-scoped, indexed.

## Frontend dashboard
- KPI cards: today's revenue, today's sales count, low-stock items, expiring-soon items (use warning/danger colors from the design system).
- A sales trend chart (recharts) and a top-products table.
- An "Alerts" panel linking to low-stock and expiry lists.
- Date-range picker driving the queries via React Query.

Follow the dataviz guidance for any chart (accessible colors, clear axes, tabular numbers). Deliver endpoints + dashboard page + Postman examples.
```

**After this step:** open the dashboard; confirm KPIs and the trend chart reflect your test sales; cross-check profit against a manual calculation on one sale.

---

## Step 10A — File uploads & storage (YOUR OWN SERVER, swappable)

```
Build a FilesModule for apps/api that handles file uploads (pharmacy logo now; prescription/product images later). Storage MUST be an abstraction whose default implementation writes to OUR OWN SERVER (local disk). It must be swappable to S3 / Supabase / any CDN later without touching call sites. Tenant-scoped and secure.

## Storage abstraction (the point of this step)
Define an interface StorageProvider with:
- save(input: { tenantId, buffer/stream, originalName, mimeType, size, folder }) -> { key, url }
- getStream(key) -> readable stream (for serving)
- getUrl(key) -> string (public or app-relative URL)
- delete(key) -> void
- exists(key) -> boolean
Bind ONE implementation via Nest DI, chosen by env STORAGE_DRIVER.

## Default implementation = LocalDiskStorageProvider (our own server)
- Writes under a configured root dir: STORAGE_LOCAL_DIR (e.g. /var/pharmasaas/uploads or ./storage in dev).
- Key layout is TENANT-SCOPED and non-guessable: `${tenantId}/${folder}/${uuid}.${ext}`. Never use the client filename on disk (prevents path traversal + collisions); keep originalName only as metadata.
- getUrl returns an APP URL like /api/v1/files/:key (served by the API), NOT a raw filesystem path and NOT an open directory. No directory listing.
- Ensure the tenant subdir exists on save; write atomically (temp file then rename).

## Future swap (document, do not build now)
- Provide stub classes S3StorageProvider and SupabaseStorageProvider implementing the SAME interface, throwing "not configured" until env is set. Show that swapping is: implement the class + set STORAGE_DRIVER=s3 (+ its env) — zero changes in FilesController/SettingsService or any caller.

## Upload endpoint (tenant-scoped, authorized)
- POST /api/v1/files (multipart, roles: OWNER, MANAGER, PHARMACIST): fields file + folder (whitelist: 'logos' | 'products' | 'prescriptions'). Uses Nest FileInterceptor (multer, memory or temp storage) then hands the buffer to StorageProvider.save with the CURRENT tenantId from TenantContext (never from the body).
- Validation: allowed mimeTypes per folder (logos/products: png,jpg,jpeg,webp,svg; prescriptions: + pdf), max size (e.g. 2MB logo, 5MB others) — reject 422 otherwise. Sanitize/verify mime by magic bytes, not just the header.
- Returns { key, url }.

## Serving endpoint (authorization enforced)
- GET /api/v1/files/:key(*) : resolve the tenantId prefix from the key and assert it equals the requester's tenantId (staff) — a user can only fetch their OWN tenant's files. Stream via StorageProvider.getStream with correct Content-Type and caching headers. 404 on missing, 403 on cross-tenant.
- (Logos may be shown pre-login on the branding screen; if you need that, add a narrow public variant GET /api/v1/files/public/logo/:tenantId that ONLY serves the logo key from TenantSettings — nothing else.)

## Config / env
- STORAGE_DRIVER=local (default) | s3 | supabase
- STORAGE_LOCAL_DIR, STORAGE_PUBLIC_BASE_URL
- Add all to .env.example with comments.

## Cleanup
- When TenantSettings.logoUrl is replaced, delete the old key via StorageProvider.delete (best-effort, don't fail the request if delete fails — log it).

Deliver: the StorageProvider interface, LocalDiskStorageProvider, the S3/Supabase stubs, FilesModule (upload + serve), DI wiring by env, validation, and Postman examples for upload + fetch + cross-tenant 403. Do NOT wire any third-party SDK as the default.
```

**After this step:** upload a logo via Postman as tenant A, fetch it back, confirm it lands under `storage/<tenantAId>/logos/...` on disk; try to fetch tenant A's file with tenant B's token and confirm 403. Confirm `STORAGE_DRIVER=local` is the default and no Supabase/S3 credentials are needed to run.

---

## Step 10 — Tenant settings, branding (white-label), user management

```
Build SettingsModule + user management (apps/api) and the settings screens (apps/web). Tenant-scoped.

## Tenant settings  (roles: OWNER; MANAGER read)
- GET/PUT /api/v1/settings: appName, logoUrl, primaryColor, secondaryColor, address, phone, receiptHeader, receiptFooter, vatPercent, currency, timezone.
- Logo upload uses the FilesModule from Step 10A (POST /api/v1/files with folder='logos', on OUR OWN SERVER via StorageProvider). Store the returned `key`/`url` in TenantSettings.logoUrl; on replace, delete the previous key. Do NOT upload logos to Supabase or any third-party.
- Validate colors (hex), vatPercent 0-100.

## Branding applied in the web app (white-label)
- After login, the app fetches branding and sets CSS variables (--primary, --secondary), document title = appName, sidebar logo. Cache it; refetch only when settings change. Never hardcode a tenant's brand.

## User management  (roles: OWNER; MANAGER can manage CASHIER/PHARMACIST only)
- CRUD /api/v1/users within the tenant: name, email, role, status. Set/reset password (temp password flow). @@unique(tenantId,email) enforced. Cannot disable the last OWNER. Cannot escalate above your own role.

Deliver endpoints, DTOs, the settings + users pages, and the runtime branding wiring. Confirm two tenants show different appName/color on the same deployment.
```

**After this step:** change the demo tenant's appName + primary color and confirm the UI updates after re-login; create a CASHIER user and confirm that user can only reach POS.

---

## Step 11 — Frontend app shell, auth, routing, POS UX polish

```
Assemble the Next.js app shell that ties the modules together (apps/web). App Router + TypeScript + Tailwind + shadcn/ui + TanStack Query + react-hook-form + zod + axios.

## Shell & auth
- Login page (subdomain, email, password) -> stores tokens (httpOnly cookie preferred; else memory + silent refresh), fetches /auth/me + branding, redirects to dashboard.
- Protected layout: left sidebar (Dashboard, Inventory, Purchase, POS, Sales, Reports, Suppliers, Settings, Users — filtered by role), top bar (tenant logo/appName, user menu, logout). Role-based nav hiding + route guards.
- Axios interceptor: attach access token, refresh on 401, redirect to login on refresh failure. Global error toasts (sonner).
- Super-admin: a separate /admin area (login + tenants list + tenant detail with plan/status/subscription actions), gated to super-admin tokens.

## POS screen (make it fast — this is used all day)
- Split layout: left = search box (autofocus, product-search-pos), results, and the cart lines (qty editable, line discount); right = customer (optional), totals (subtotal, discount, VAT, total), payment method, paid amount, change, and a big "Complete Sale (F9)". Keyboard: type-to-search, Enter adds top result, arrows to pick, F9 completes. On success -> print thermal receipt + clear cart.
- Show batch/expiry being used (FEFO) per line as read-only info.

## Data screens
- Inventory (stock table + batches + alerts tabs), Purchase (create + list), Sales (list + detail/reprint), Suppliers, using TanStack Query with proper cache invalidation after mutations.

Follow the design system (colors, tabular-nums, print CSS). Deliver the shell, POS page, and the data pages wired to the API.
```

**After this step:** do a full flow in the browser: log in → add a product → record a purchase → sell it at POS (keyboard only) → print receipt → see it in reports. Fix any rough edges before hardening.

---

## Step 12 — Security hardening + tests

```
Harden and test the whole system before deploy.

## Security
- Verify the Prisma tenant extension covers EVERY tenant-scoped model and every query method; add a test that fails if a new model is added without tenant scoping.
- Enforce HTTPS assumptions, secure/httpOnly/sameSite cookies, CORS locked to the web origin, Helmet headers, rate-limit auth + POS endpoints.
- Argon2 params sane; JWT secrets strong and from env; refresh token rotation + reuse detection.
- Authorization matrix test: for each role, assert allowed vs 403 routes. Assert staff token gets 403 on all /admin routes and vice versa.
- Input validation on every DTO; reject unknown fields (whitelist). Global error filter never leaks stack traces in prod.

## Correctness tests
- Multi-tenant isolation integration test: seed 2 tenants, assert no cross-tenant read/write is possible through any endpoint.
- Sale atomicity + FEFO + concurrency tests (two parallel sales of the last unit).
- Purchase atomicity test. Void restock test. Valuation/profit math test against known fixtures.

## Ops
- Structured logging (pino/nestjs-pino) at boundaries: auth, sale, purchase, void, admin actions, errors. Never log secrets, passwords, or full tokens.
- Health check endpoint. Basic request metrics.

Deliver the added tests and hardening. Report the final test coverage of the money paths (sales, purchase, FEFO, tenant isolation) — these must be well covered.
```

**After this step:** run the full test suite; confirm tenant isolation, sale atomicity, FEFO, and the role matrix all pass. Manually try to break tenant isolation and confirm you can't.

---

## Step 13 — Deployment

```
Prepare PharmaSaaS for production deployment. Web only.

## Backend (apps/api)
- Dockerfile for the NestJS API (multi-stage, small image). Run Prisma migrate deploy on start.
- Env: DATABASE_URL, JWT secrets, CORS origin, PORT, NODE_ENV. Provide .env.example and a checklist.

## Frontend (apps/web)
- Build the Next.js app; set the API base URL via env. Dockerfile or a platform build (Vercel or the same VPS).

## Database & ops
- Managed Postgres recommendation (Neon/Railway/RDS). Connection pooling note (pgbouncer/Prisma). DAILY automated backups + a documented restore test — pharmacy sales data loss is unacceptable.
- File storage (STORAGE_LOCAL_DIR) is on our own server: mount it as a PERSISTENT VOLUME (docker volume / host bind mount) so uploads survive container rebuilds and redeploys. Include this dir in the DAILY backup (logos, prescriptions). Note the one-line switch to S3 (STORAGE_DRIVER=s3) if you later outgrow single-server disk.
- A docker-compose for a single-VPS deploy (api + web + postgres + a reverse proxy/Caddy for HTTPS + subdomains *.pharmasaas.app). Explain how subdomain-per-tenant maps to branding (optional; login-based tenant works without it).
- Zero-downtime migration note; how to run seed for the first PlatformAdmin only.

## Go-live checklist
- Strong secrets rotated, backups verified by restore, HTTPS enforced, CORS locked, rate limits on, error monitoring (Sentry) wired, super-admin account created, one real pharmacy onboarded end-to-end.

Deliver Dockerfiles, docker-compose, the deploy README, and the go-live checklist. Do not include any secrets.
```

**After this step:** deploy to a staging server; create your super-admin; onboard one real (or pilot) pharmacy; run a full sale end-to-end over HTTPS; verify a database backup restores.

---

# What comes after v1 (roadmap, not built yet)

- **Customer online ordering** (public site + prescription upload + delivery) — the schema already supports products/batches/customers.
- **Automated subscription billing** (SSLCommerz/Stripe) replacing manual billing.
- **Barcode scanning** at POS + label printing.
- **Purchase returns / customer returns** (partial), supplier payment ledger.
- **Multi-branch** per pharmacy (add `branchId` under `tenantId`).
- **Second vertical** (supershop/garments) via the Core + Module pattern — split the medicine-specific bits (generic, batch/expiry) into a pharmacy module and add product-variant (size/color) as a garments module.

---

# One-page summary

- **It IS a SaaS** — multi-tenant: one Next.js + NestJS + Postgres app, `tenantId` on every row, auto-filtered from the JWT. That isolation is the whole game — never break it.
- **v1 = pharmacy staff web app**: catalog → purchase (stock-in) → inventory (FEFO, batch/expiry) → POS (atomic sale) → receipts → reports → settings, plus a **super-admin** area with **manual billing**.
- **Build order** = the 14 steps above (0–13), one at a time, testing after each. Sales/purchase/FEFO/tenant-isolation are transactional and must be tested hard.
- **Paste the prompts in English**, test each step, don't skip ahead.
