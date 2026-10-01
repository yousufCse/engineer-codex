# App Store Developer Accounts: Google Play and Apple

What you need to open a developer account on Google Play and the Apple App Store.
It covers both account types: **personal** and **organization (company)**.
Checked twice against the official Google and Apple pages on 2026-10-01. See [Sources](#sources).

## 1. In short

1. You need two accounts: one on Google Play and one on Apple.
2. Each store has two account types: **personal** (one person) and **organization** (a company).
3. One account can hold many apps.
4. Cost is the same for both types: Google **USD 25, one time**. Apple **USD 99 per year** (may vary by region).
5. Both stores check who you are before you can publish.

## 2. Which type to choose

| Choose | When |
|---|---|
| **Personal** | You publish apps as yourself. Hobby apps, side projects, your own small apps. |
| **Organization** | A company owns the apps. A team works on them. Or the app is in a category that needs a company (see below). |

Google **requires** an organization account for these apps (Play Console Requirements policy):

- Financial products and services: banking, loans, stock trading, investment funds, crypto wallets, crypto exchanges.
- Health apps, such as medical apps and human subjects research apps.
- Apps approved to use the VpnService class (VPN apps).
- Government apps (made by or for a government agency).

Apple says apps in highly regulated fields should come from a legal entity, not from one person (App Review Guideline 5.1.1(ix)). Apple's examples: banking and financial services, healthcare, gambling, legal cannabis, air travel and crypto exchanges. The same rule covers apps that need sensitive user information.

⚠ **A sole proprietorship counts as a person for Apple.** If your business is a one-person business and not a legal entity, Apple makes you enroll as an individual. Your own name is then shown as the seller.

## 3. Personal account

### What you need

REQUIRED
1. Your legal name and legal address.
2. Government photo ID — valid (not expired), in colour, clear, not a photocopy. For Google, the name and address must match your Google payments profile exactly. Apple may also ask for a photo ID.
3. Contact email and contact phone. The store uses them to contact you. They are not shown to users.
4. Google: a developer email. Google shows it on your store page.
5. Google: a real Android phone with Android 10 or newer, not rooted. You verify it with the Play Console mobile app.
6. Google: you must be at least 18. Apple: you must be of legal adult age in your region.
7. Apple: an Apple Account with **two-factor authentication** on. The first and last name must be your legal name.
8. Your own credit or debit card, in your name — USD 25 one time (Google), USD 99 per year (Apple). Google does not accept prepaid cards.

ONLY IN SOME COUNTRIES
9. Proof of address (Google). Bangladesh needs it for personal accounts. Accepted: photo ID with your address, utility bill, insurance statement, or credit card or bank statement. It must show your name and address exactly as in your payments profile.

The accepted documents depend on your country. Check Google's list for your country before you start.

### Steps — Google Play

1. Sign in with your Google Account.
2. Open <https://play.google.com/console/signup>.
3. Accept the Google Play Developer Distribution Agreement.
4. Pay the **USD 25** fee.
5. Choose account type **Personal**.
6. Create or link a personal Google payments profile. Google takes your legal name and address from it.
7. Enter your developer name, contact email, contact phone and developer email.
8. Verify your identity. Upload your photo ID, and proof of address if your country needs it.
9. Verify your Android phone:
   1. On Play Console (web), open **Home**.
   2. Find the task "Verify that you have access to an Android mobile device".
   3. Scan the QR code with your phone. It opens the Play Console mobile app.
   4. Sign in with the same Google Account, and tap **Verify**.
10. Verify your emails and phone with the 6-digit codes Google sends. The phone check opens only after the identity check and the phone (device) check.

The sign-up screens may show these steps in a different order.

### Steps — Apple

1. Use your Apple Account. Your first and last name must be your **legal** name. No nickname, no company name.
2. Turn on **two-factor authentication**.
3. Start at <https://developer.apple.com/programs/enroll/> and enroll as an individual. You can also enroll in the Apple Developer app.
4. Enter your email, phone and address. Apple does not accept a P.O. box.
5. Review the license agreement and pay **USD 99**. Use your own card. If the card is not yours, Apple delays the enrollment and asks for your photo ID.

### IMPORTANT for personal accounts

- **Closed test before release (Google).** New personal accounts must run a closed test with **at least 12 testers** for **at least 14 days in a row**. Only then can you apply for production. If a tester leaves and joins again, their 14 days start again. Google's review of your application usually takes 7 days or less. Plan about 3 weeks before your release date.
- **Your details are public.** Google shows your legal name, country and developer email. If you earn money on Google Play, Google also shows your full address. Some regions need more. For example, Korea also needs a public phone number. Apple shows your legal name as the seller.
- **No team on Apple.** An Apple individual account cannot add team members. You can give up to 50 people access to App Store Connect only. A Google personal account can invite other users.
- **Some apps are not allowed.** You cannot publish the app types in [section 2](#2-which-type-to-choose) from a Google personal account.
- **Moving to a company account later is possible.** See [section 5](#5-important-for-both-account-types).

## 4. Organization account

### What you need

REQUIRED
1. Registered company.
2. D-U-N-S Number — a free 9-digit company ID number from a company
   named Dun & Bradstreet. Google and Apple use it to check that our
   company is real. We request it after the company is registered.
   It can take up to 30 days.
3. Company registration document. Any accepted one:
   certificate of incorporation or registration / extract from the
   commercial register / business license / VAT registration certificate.
4. Photo ID of the person who signs for the company — valid, in colour,
   not a photocopy. Any accepted one: passport / identification card /
   driving license / permanent residence card.
5. Company website — public and working, on the company's own domain.
6. Work email on the company's domain, for the person who signs.
7. Company phone number, and one contact person's name, email and phone.
8. Public email and phone, to show on the store page.
9. Company card — USD 25 one time (Google), USD 99 per year (Apple).

ONLY IN SOME CASES
10. If the signer is not the owner/founder: a person who can confirm
    that the signer has the authority to sign (Apple).
11. A notarized copy of the company document, if Apple asks.

Notes:

1. **Legal entity (Apple).** Apple needs a legal entity, such as a corporation, a limited liability company or a limited partnership. Apple does not accept a sole proprietorship, a trade name or a branch.
2. **Documents depend on the country (Google).** The document lists in items 3 and 4 come from Google's page for Bangladesh. Check Google's list for your country.
3. **Who can sign.** Google: anyone with legal authority to represent the company, such as the CEO, a director or a legal representative. The photo ID can be from any country. Apple: the owner/founder, an executive, a senior project lead, or an employee given legal authority by a senior employee.
4. **D-U-N-S is free.** Google says it is free. Apple says it is free in most countries.
5. **Government organizations** can usually enroll without a D-U-N-S Number. Apple makes it optional. Google asks known government agencies to contact support if the sign-up asks for one.
6. **Card.** Google does not accept prepaid cards.

### Steps

#### Step 1 — Register the company

1. Register the company.
2. Get the company registration document.
3. Write down the exact legal name and address. Use the same words everywhere.

#### Step 2 — Website and work email

1. Put the company website online, on the company's own domain. It needs real content. A social media page, a page with very little content, or a domain parking page is not accepted.
2. Create the work emails on the same domain.
3. Add the website to Google Search Console. Use the same Google Account that will own the Play Console account. Then Google approves the website check automatically.

#### Step 3 — Get the D-U-N-S Number

1. Open <https://developer.apple.com/enroll/duns-lookup/> and sign in with your Apple Account.
2. Enter the legal company name, headquarters address, mailing address and your work contact details.
3. If the company is listed, note the number.
4. If it is not listed, submit the request on the same page. It is free.
5. Keep the company registration document ready. Dun & Bradstreet may contact you for more information, such as business type or number of employees.
6. Wait for the number. Apple says up to **5 business days**. If it takes more than two weeks, email Dun & Bradstreet. Google says it can take up to **30 days**.
7. After you get the number, wait up to **2 business days** before you start with Apple.

If Dun & Bradstreet does not work in your country, contact Google Play support **before** you create the Google account. Google may give you another way to verify.

#### Step 4 — Open the Google Play account

1. Sign in with the company Google Account.
2. Open <https://play.google.com/console/signup>.
3. Accept the Google Play Developer Distribution Agreement.
4. Pay the **USD 25** fee.
5. Choose account type **Organization**.
6. Create or link an organization Google payments profile with the D-U-N-S Number. Google takes the company name and address from this profile. They must match the Dun & Bradstreet record.
7. Enter the other details:
   - Developer name (the public name; it can be different from the legal name)
   - Company phone number (the one people find online or in Dun & Bradstreet; not shown on Google Play)
   - Company website
   - Contact person's name, email and phone (not shown on Google Play)
   - Public email and phone (shown on Google Play)
8. Pass Google's checks:
   1. Identity — upload the company registration document and the signer's photo ID.
   2. Website — send the website check from the **Account details** page in Play Console.
   3. Emails — 6-digit code by email.
   4. Phones — 6-digit code by text message or voice call. This opens only after the identity and website checks.

The sign-up screens may show these steps in a different order.

#### Step 5 — Open the Apple account

1. Use an Apple Account with the signer's **legal** first and last name. Apple recommends that this account uses the work email.
2. Turn on **two-factor authentication**.
3. Start at <https://developer.apple.com/programs/enroll/> and enroll as an organization.
4. Enter the legal company name, D-U-N-S Number, website and work email.
5. If the signer is not the owner/founder, give the reference person's details.
6. Apple checks the information and emails the next steps.
7. Review the license agreement and pay **USD 99**.

### IMPORTANT for organization accounts

- **The company name and address must be exactly the same everywhere.** This means the company document, the D-U-N-S record, the Google payments profile and the Apple enrollment. A small difference can fail the check.
- **If the name or address changes later, update Dun & Bradstreet first.** Google then asks you to verify the company again. If Google finds a mismatch and you do not fix it by the deadline, Google restricts the account and removes all its apps.
- **Register the company first.** The D-U-N-S Number and both accounts need a registered company.
- **Start the D-U-N-S request early.** It can take up to 30 days.
- **Apple needs the legal entity itself.** Apple does not accept a sole proprietorship, a trade name or a branch.
- **The website must be real.** It must be public, working and on the company's own domain. Neither store accepts a social media page.
- **Use company emails.** Google says the contact email and the public email should not be personal or generic emails. Google may remove your apps if the public email or phone does not work.
- **Your company details are public.** Google shows the legal name, legal address, public email and public phone. Apple shows the company's legal name as the seller.

## 5. IMPORTANT for both account types

- **Keep the Apple membership paid.** It is yearly. If it expires, your apps can no longer be downloaded, and you cannot submit apps or updates. Apps already on users' phones keep working. You can renew from 30 days before the end date. Auto-renew works only in some countries, so check your renewal date yourself.
- **Keep your details true and up to date.** If Google cannot verify your information, it may remove your developer profile and apps from Google Play. You cannot publish again until you verify.
- **Your documents must match your payments profile exactly** (Google). Check the spelling of your name and address before you upload. Edited or fake documents can get the account and all apps removed at once.
- **If you earn money on Google Play, verify your bank account.** Google removes the apps of developers with an unverified bank account. This check can take up to 5 days.
- **Turn on two-factor authentication** on the Google and Apple accounts. Whoever controls these accounts controls your apps.
- **Use an account you will keep.** For a company, do not open it on one employee's private Gmail or Apple Account. If that person leaves, you can lose access.
- **Never buy, sell or rent a developer account.** Google does not allow it. Use Google's official account transfer process.
- **Changing the account type later is possible, but it takes work:**
  - Google, personal to organization: create an organization payments profile, verify it, and link it to the account.
  - Google, organization to personal: not possible. Create a new personal account, verify it, and transfer the apps.
  - Apple, individual to organization: contact Apple support.
  - Moving an app to another Google account: send a transfer request in Play Console. Both accounts must be registered and active. A new account costs another USD 25.

## 6. Later, for each app

1. Create one app record per app in each store.
2. Privacy policy — both stores need one for every app. Google: add the link in Play Console and inside the app. It must be a public, working web page, open in all countries, and not a PDF.
3. Google: fill in the forms on the **App content** page (Monitor and improve → Policy → App content). Examples: data safety, and the health apps declaration. Google asks all developers to complete the health apps declaration.
4. Apple: fill in the **App Privacy** details in App Store Connect.
5. If the app needs a login, give the reviewers a working demo account. Both stores ask for this.
6. If users can create an account in the app, they must be able to delete it too. Both stores require this.
7. Google: check that the app's package name is registered, on the **Android developer verification** page in Play Console. Google tries to do this automatically.

⚠ **Package names (Google).** Since **30 September 2026**, Google removes apps whose package name is not registered. Check every existing app in your account.

## Sources

- Apple — [Enrollment](https://developer.apple.com/programs/enroll/) · [Enrollment help](https://developer.apple.com/help/account/membership/program-enrollment/) · [Identity verification](https://developer.apple.com/help/account/membership/identity-verification/) · [D-U-N-S](https://developer.apple.com/help/account/membership/D-U-N-S/) · [Renewal](https://developer.apple.com/help/account/membership/renewal/) · [App Store Connect users](https://developer.apple.com/help/app-store-connect/manage-your-team/add-and-edit-users) · [App privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy) · [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- Google — [Get started](https://support.google.com/googleplay/android-developer/answer/6112435) · [Required information](https://support.google.com/googleplay/android-developer/answer/13628312) · [Account types](https://support.google.com/googleplay/android-developer/answer/13634885) · [Play Console Requirements policy](https://support.google.com/googleplay/android-developer/answer/10788890) · [Verification](https://support.google.com/googleplay/android-developer/answer/10841920) · [Required documents by country](https://support.google.com/googleplay/android-developer/answer/15633622) · [Website verification](https://support.google.com/googleplay/android-developer/answer/13205715) · [Device verification](https://support.google.com/googleplay/android-developer/answer/14316361) · [Testing for new personal accounts](https://support.google.com/googleplay/android-developer/answer/14151465) · [Keeping account info up to date, and changing account type](https://support.google.com/googleplay/android-developer/answer/13634888) · [App transfer](https://support.google.com/googleplay/android-developer/answer/6230247) · [Package name registration](https://support.google.com/googleplay/android-developer/answer/16984799) · [User data policy](https://support.google.com/googleplay/android-developer/answer/10144311) · [Health policy](https://support.google.com/googleplay/android-developer/answer/16679511)
