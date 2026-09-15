# UI, theme and motion

The app's design system in one place: colour, type, spacing, the shared
widgets, the UX rules a screen has to keep, and how things move.

Read it for two reasons — to add a screen here without inventing anything, and
to lift the whole system into the next app. The last section says what to copy
and in what order.

Before, every screen drew its own card, its own empty block and its own
segmented control, and nothing moved. A radius or a tint was eleven edits, and
a screen either had its data or it did not — there was nothing in between. Now
there is one of each, and blocks arrive instead of appearing.

---

## Colour

**One knob.** `AppColors.seed` is the brand. Every brand tone and every grey is
derived from it at first use by `BrandPalette`, using the design mock's Oklch
recipe: pin the lightness, cap the chroma, keep the seed's hue. Change the seed
and seventeen tones re-fit together. There is no second place to edit.

Capping chroma is not cosmetic. Carrying a vivid seed's full chroma down to a
dark tone leaves sRGB, clips per channel, and changes the hue — uncapped,
`#F0521F` arrives as a pure red.

| Tone | What it is for |
|---|---|
| `primary` | The seed as picked. Icons, graphics, rings, borders, bars, progress |
| `primaryInk` | Anything **bearing text**: brand text on paper, and any fill under a white label |
| `secondary` `#2A46C3` | Information and links. **Never a button** |
| `ink` `#181720` | The brand's near-black — headlines, dark brand surfaces |
| `tint` `#FFEFE6` | Warm paper tint for brand bands and hero blocks |
| `gradientStart` → `gradientEnd` | The app icon's own gradient |
| `gradientDeep` | Where a full-screen brand field lands, so white keeps 6.2:1 |
| `ok` `warn` `error` (+ `*Ink`, `*Container`, `on*Container`) | Status only |

Keep the `primary` / `primaryInk` split even when one seed happens to work both
ways. Vivid orange under white is 3.54:1 and fails; a codebase that blurred the
two roles would break the moment the brand moved.

**Semantics are not derived from the brand.** The brand can be anything and
"delivered" is still green. They are their own seeds through the same recipe,
pinned to hex because they never move.

**One colour still.** Brand carries every action. Rank comes from fill weight —
filled, then tonal, then outlined — never from a second hue. Green, amber and
red are statuses, never buttons.

**Surfaces carry a whisper of the brand.** `SurfaceTint.brand` is what ships:
M3 neutral-variant behaviour, chroma near zero, so the hue warms the paper
without staining it. `ThemeFlags.surfaceTint` can switch it to `none` (true
greys — honest, and flat: a merchant reads an untinted surface as a disabled
one) or `cool` (greys with a blue-grey of their own).

**Judging a look.** `ThemeFlags` holds looks-only switches — `seedOverride` and
`surfaceTint`, both `const`, both null-means-what-ships. They change no
behaviour, so they are safe in any build, and they answer a design question on
the real app instead of on a mock. They need a **hot restart**: the palette is
derived once. Leave them null in a commit unless the change *is* the decision.

**Contrast is a test, not a hope.** `test/core/app/theme/` re-runs the WCAG
rules over every seed the mock offers — brand text on every surface, each
semantic ink under a white label, each container under its `on-` tone. A seed
that would ship an illegible screen fails the suite instead of the merchant.

## Type

One scale, named by the design sheet, wired to Flutter's slots. Sizes and
weights are locked by `typography_test.dart` — if a slot moves, that list is
what it is checked against.

| Sheet | Slot | Size / weight |
|---|---|---|
| H1–H6 | `displayLarge` … `headlineSmall` | 48 / 40 / 32 / 28 / 24 / 20, w600 |
| S1, S2 | `titleLarge`, `titleMedium` | 18, 16, w600 |
| Button | `labelLarge` | 18, w500 |
| B1, B3 | `bodyLarge`, `bodyMedium` | 16, 14, w400 |
| B4 | `labelMedium` | 14, w500 |
| C1, C2 | `bodySmall`, `labelSmall` | 12, w400 / w500 |

**Gilroy is licensed and is not in this repo.** Drop the four weights into
`assets/fonts/gilroy/`, uncomment the `pubspec.yaml` block, point
`AppFonts.heading` at `gilroy`. That is the whole switch. Until then the
heading face is Plus Jakarta Sans.

`AppFonts.heading` names a face that is actually bundled, on purpose. A family
the engine cannot find falls back to the **platform's** font, not to the next
name in the list — the app would quietly render in San Francisco on one phone
and Roboto on another.

Every style carries `fontFamilyFallback: [Noto Sans Bengali]`. Neither Latin
face draws Bengali, and half this app is Bengali.

## Space, radius, elevation

Every number is in `AppSizes`. Never write a bare `8.0` in a widget.

- **Spacing** climbs `space4, 8, 12, 16, 20, 24, 32, 48, 80, 100, 200`. Screen
  padding is `space16`; a list's bottom padding is `space80` so the action
  button never sits on the last row.
- **Radius** is per component, not per screen: `buttonRadius` 8, `cardRadius`
  12, `fabRadius` 16, `bottomSheetRadius` 20, `dialogRadius` 28. The dashboard
  is softer on purpose (`dashboardCardRadius` 20, `dashboardHeroRadius` 24).
- **Elevation** is almost nowhere. A card is a hairline plus a very soft
  shadow. The one real lift is `actionBarElevation` — the bar a form pins its
  action to.

## The shared pieces

All in `lib/core/presentation/widgets/`. Import the barrel, never the file.

| Use | Widget | It replaced |
|---|---|---|
| Any card in any list | `AppSurfaceCard` | 8 hand-rolled `Container` + `BoxDecoration` copies |
| Nothing to show, or a failed load | `AppEmptyState` | 5 copies of a private `_Message` |
| One choice out of two or three | `AppSegmentedControl` | `SegmentedButton`, which cuts instead of sliding |
| A block arriving | `AppReveal` | nothing — new |
| A row in a lazy list arriving | `AppListReveal` | nothing — new |
| A figure that should count up | `CountUpText` | a plain `Text` |
| A card that gives under a press | `PressableScale` | a bare `InkWell` |
| A list with an action button over it | `CollapsingFabScaffold` | a `Scaffold` per screen, each with its own FAB |
| A text field, a dropdown, a date or time | `AppTextField`, `AppDropdown`, `AppDatePicker`, `AppTimePicker` | four different field frames |
| The optional half of a form | `ExpandableSection` | fields that were always on screen |
| Any modal sheet | `showAppSheet` / `BottomSheetHelper` | 6 `showModalBottomSheet` calls, 2 already drifted |
| A screen that grows out of a button | `ContainerTransformPage` | a plain push |
| A question, a message, a blocking wait | `AppDialog` | hand-built `AlertDialog`s |
| Any snackbar | `context.showSuccessSnackbar` / `showFailureSnackbar` | ad-hoc `SnackBar`s |

`AppSurfaceCard` is white paper (`surfaceContainerLowest`) on the app's warm
near-white page, with a hairline and a very soft shadow. Pass `onTap` and it
presses; pass `borderColor` for the one card in a list that is the default.

Profile has one of its own: `RowGroup` (`features/profile/.../row_group.dart`)
puts settings rows in a card with hairlines between them.

## The four states of a screen

Every screen that loads anything owes the merchant all four. Skipping one is
how a screen ends up looking broken on a slow network.

| State | What shows |
|---|---|
| Loading, first time | A shimmer skeleton shaped like the real content (`shimmer/shimmer_skeletons.dart`), or `AppLoadingView` |
| Loading, over existing content | Dim what is there — never blank it. See `dashboardRefreshFade` |
| Empty | `AppEmptyState` with a line that says what to do next, not "no data" |
| Failed | Blocking error → `AppEmptyState` with a Retry. Non-blocking → a failure snackbar over the content that is still good |

A busy overlay waits `loaderShowDelay` (200 ms) before it appears. Most calls
answer inside that, and a spinner that flashes for 100 ms reads as a glitch,
not as work.

Shimmer is the one animation allowed to repeat, and only inside a skeleton,
which leaves the tree the moment the data lands.

## Sheet, screen, or dialog

A sheet is not a small screen. It is a short, secondary task the merchant is
still standing in the list to do.

| The task | Where it goes |
|---|---|
| Pick one out of a list, confirm, choose an action | Modal sheet |
| A yes/no question, or one message | `AppDialog` |
| Anything with a keyboard, validation, or more than three fields | A pushed screen |

The sheet cap is `AppSizes.bottomSheetMaxHeightFraction` (0.9). Needing most of
it is the sign that the thing is a screen — raising it is not the fix. The
address form was a sheet first: six fields, two dependent dropdowns and the
keyboard left two rows visible, and one drag threw the typing away with no
question asked. Parcel details went the same way: five groups pinned at three
quarters of the screen is a screen wearing a drag handle. A record the merchant
reads, comes back to, and will act on wants a route — one a notification can
open.

## Forms

A form screen owes three things a sheet cannot give:

- **Its action stays put.** The button lives in `bottomNavigationBar`, on a
  `Material` at `AppSizes.actionBarElevation`, inside `SafeArea(top: false)` —
  not at the end of the scroll where the keyboard hides it.
- **It guards its own exit.** `PopScope(canPop: false)` with a confirm when
  what is on screen differs from what was opened (`address_form_screen.dart`).
  A sheet dismisses on a drag and on a scrim tap, and neither can ask first.
- **It shares the list's state, not a copy.** A `ShellRoute` holds the cubit
  above both pages (`addresses_shell_route.dart`), so the form saves into the
  book the list is showing, and the list is refetched before the form closes.

One trap comes with that shell: the list is the **first** page inside the
shell's own `Navigator`, so it cannot pop within it and `AppBar` silently drops
its back button. Set `leading` yourself — `context.canPop() ? LeadingBack(...)
: null`, using go_router's `canPop`, not the `Navigator`'s. Android system back
is unaffected; go_router pops the whole shell.

The rest:

- Validation lives in `AppValidators`, messages in `ValidationMessages`. A
  screen never writes its own regex.
- Required fields say so with `isRequired: true`, which draws the mark. A
  disabled field says **why** in its hint — "Pick a district first" beats an
  empty grey box.
- Wrap the body in `KeyboardDismissible` so a tap outside puts the keyboard
  away.
- Dependent fields clear together. Picking a new district clears the area; an
  area from the old district would price the delivery wrong.
- Dispose every controller.

## Feedback

- **Snackbar** for something that happened and needs no answer.
  `context.showSuccessSnackbar(...)`, or `showFailureSnackbar(context, failure)`
  for a `Failure` off a cubit. Types are `success`, `error`, `warning`, `info`.
- **Dialog** for something that needs an answer. `AppDialog.confirm` returns a
  `bool`; pass `isDestructive: true` and the confirm goes red.
- **Ask before anything that cannot be undone.** Removing an address is one
  tap and the record is gone from the server, so it is a confirm first. Same
  for leaving a form with typing in it.
- **Say what happened, with the detail that identifies it.** "Parcel booked for
  Rahim Uddin" beats "Success" for a merchant booking parcels all morning.
- One listener owns a message. When a form saves through the list's cubit, the
  list shows the failure — put it in two places and it appears twice.

## Language

- Every user-facing string is an ARB key in **both** `app_localizations_en.arb`
  and `app_localizations_bn.arb`, added in the same change, then
  `./build.sh codegen`. The two key sets stay identical.
- Read it with `context.l10n`. Never a literal in a widget.
- Numbers a merchant reads go through `context.localizeDigits(...)` so Bengali
  gets Bengali digits. Dates are day-first.
- Bengali runs longer than English. Buttons take `minWidth`, not `width`, and
  labels get `maxLines` + ellipsis rather than a fixed box.
- Keys are named for the thing, not the screen, when the string is general —
  `unsavedChangesTitle`, not `addressUnsavedTitle` — so the next form reuses it.

## Motion

Every duration and curve is in `AppDurations`; every distance is in `AppSizes`.
Never write a `Duration` or a curve inline.

| What moves | Token | Notes |
|---|---|---|
| A block fading and lifting in | `reveal`, `revealStagger`, `revealCurve` | 380 ms, 60 ms behind the block above |
| A figure counting up | `countUp`, `countUpCurve` | 850 ms, ease-out |
| A card under a finger | `press` | 110 ms to `AppSizes.pressScale` |
| The segmented plate sliding | `dashboardRangeSlide`, `dashboardRangeCurve` | 260 ms |
| A stage's share bar growing | `dashboardShareBar` | 750 ms, slower than the count beside it |
| Numbers dimming while a range reloads | `dashboardRefreshFade` | 180 ms to 0.5 opacity |
| The action button opening / closing | `fabExpand`, `fabCollapse`, `fabLabelFade` | 300 ms out, 200 ms back |
| A form section opening / closing | `sectionOpen`, `sectionClose`, `sectionFieldsFade` | 260 / 180 ms |
| The balance peeking out | `balancePeek`, `balancePeekClose`, `balancePeekAmountFade` | 260 / 180 ms |
| A sheet coming up / going down | `sheetOpen`, `sheetClose`, and their curves | 320 / 220 ms |
| What is inside the sheet | `sheetContent`, `AppSizes.sheetContentRise` | starts at 15%, settles the last 14 px |
| A screen out of the button that opened it | `containerTransform`, `containerTransformClose` | 340 / 260 ms |
| That screen's paper and content | `containerTransformSurface`, `containerTransformContent` | button colour goes early, page arrives late |
| The notifications panel out of the bell | `notificationsPanel` and its two curves | 260 ms, one duration, two curves |
| A busy overlay | `loaderShowDelay`, `loaderOverlayFade`, `loaderCycle` | waits 200 ms before it shows at all |

Three habits run through the whole table:

**Opening is always slower than closing.** Arriving is worth watching; leaving
only has to get out of the way. Where the platform gives one duration for both
(`showGeneralDialog`), the curve carries the difference.

**Content arrives behind its container.** Every container that grows fades its
content in over the back half of the travel — `sheetContent`,
`containerTransformContent`, `fabLabelFade`, `sectionFieldsFade`. Fading from
the first frame shows a full screen of form squeezed into a button.

**A moving thing reads its parent's animation.** `_Settling` inside
`showAppSheet` reads `ModalRoute.of(context)?.animation`, so dragging a sheet
away fades its content out under the finger, not only when it is let go.

### Opening out of the control that was tapped

`ContainerTransformPage` lays the screen out at full size from the first frame
and opens a rounded window over it, from the `Rect` of the control that was
tapped. Nothing reflows while it moves — a form re-laying itself out sixty
times on the way in is why this pattern is usually done badly.

`CollapsingFabScaffold` hands its `onFabPressed` the button's own box in screen
coordinates. For anything else — a list row, a card — `originOf(context)` reads
it off the render object. Pass it as the route's `extra`; with no `Rect` the
same route returns a plain `MaterialPage`, so an entry from the drawer still
works.

Measure from a `Builder` sitting directly over the control. A list's
`itemBuilder` context belongs to the whole sliver, not to the row —
`originOf` returns null there rather than the wrong box.

The cost: the route is not opaque, so the screen underneath keeps painting
while this one is open. Worth it for a form the merchant is in for a minute.
Not for a tab.

### Motion rules

**Finite only.** No animation in a screen body may repeat. A repeating one
makes `pumpAndSettle` hang, so the screen can never be tested. Shimmer is the
one exception, and only in a skeleton.

**Drop the layer when it lands.** `Opacity` and `ClipRect` composite a layer
for as long as they are in the tree. `AppReveal`, the action button's label and
the sheet's `_Settling` hand back the bare child at the ends of their travel;
do the same in anything new.

**Lists reveal the first screenful only.** `AppListReveal` stops at row 8. A
row that fades in each time it is scrolled into view reads as a stutter, not as
polish.

**Nothing expensive.** No `BackdropFilter`, no blur, no `ShaderMask`, no
`IntrinsicHeight` in a list row. One tween per block, and hoist anything that
allocates out of `build`.

**Build the style object once.** The `AnimationStyle` in `app_modal_sheet.dart`
is a top-level `final`, not a new object per sheet.

**Motion does not buy a second hue.** The brand gradient
(`AppColors.gradientDeep` → `gradientEnd`) is for a hero block and nothing
else, and it runs deep-to-bright so the words sit where white reads at 6.2:1.

**No AI-vibe decoration.** No accent stripes, no coloured glow shadows, no
gradients except when simulating a photo, a camera or a map.

## Carrying this into another app

Copy in this order — each step compiles on its own.

1. `core/resources/app_durations.dart` and `app_sizes.dart`. Tokens first;
   nothing below builds without them. Leave the numbers alone — they are tuned
   against each other.
2. `core/app/theme/` — `oklch.dart`, `brand_palette.dart`, `app_colors.dart`,
   `theme_flags.dart`, `app_theme.dart`. Then set one thing: `brandSeed`. The
   whole palette re-fits around it.
3. `test/core/app/theme/` — take the contrast tests with the palette. They are
   what stops a new brand shipping an illegible screen.
4. `core/resources/app_fonts.dart` — point `heading` and `body` at the new
   faces, keep a script fallback if the app has a second language.
5. `core/presentation/widgets/animation/` — `AppReveal`, `AppListReveal`,
   `CountUpText`, `PressableScale`. Pure Flutter, no app types.
6. `core/presentation/widgets/app_modal_sheet.dart` and
   `bottom_sheet_helper.dart` — the one door every sheet opens through.
7. `core/presentation/transitions/container_transform_page.dart` — needs
   go_router and `AppColors`.
8. `collapsing_fab_scaffold.dart`, `app_surface_card.dart`, `app_empty_state.dart`,
   the field widgets, `app_dialog.dart`, `app_snackbar.dart` — as the screens
   need them.

What does **not** travel: anything under `features/`, and the token names that
carry a screen in them (`dashboardShareBar`, `balancePeek`, `bookSuggestion*`).
Rename those for what the next app's screens actually do.

What to keep even if everything else changes: one seed, the `primary` /
`primaryInk` split, semantics that do not follow the brand, contrast in tests,
opening slower than closing, and the four states of a screen.

## What each screen got

| Screen | Now |
|---|---|
| Dashboard | Gradient balance hero, sliding range pill, icon tiles with counting figures and tinted deltas, a rail with share bars, staggered arrival |
| Parcels | Shared card, stadium status chips, first rows staggered, shared empty state; a row opens the parcel as a screen that grows out of that row |
| Transactions | Wallet card with three aligned counting figures, shared record cards |
| Profile | Tinted header card, rows grouped in cards, no more full-width dividers |
| Addresses | Shared card, sliding pill, shared empty state; the form is a screen that grows out of the add button, names the book it is filling, and asks before it throws typing away |
| Payouts | Shared card, sliding pill, shared empty state — the account form is still a sheet, and is the next one to move |
| Everywhere | One chip and bottom-nav style from the theme, one action button that opens and closes smoothly, one door for every sheet |
