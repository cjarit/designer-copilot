# UApp — Cross-Screen Common Patterns & Design Principles

Synthesized from 4 screens of the **UApp** transit/bus routing app.

---

## 1. Orange as the Single Brand Accent Color

Orange is the unmistakable brand color, used consistently across every screen:

| Element | Color Role |
|---------|-----------|
| Bus stop markers | Orange circle with white bus icon |
| Building markers | Orange circle with white building icon |
| Active bottom tab | Orange icon + orange text |
| Origin input icon | Orange circle |
| Timeline stop dots | Orange dots connected by a line |
| Search result icons | Orange circles |
| Validation warning | Orange icon + orange text |

Red/coral is reserved exclusively for **destination** markers — the only departure from orange, and it's used semantically (origin = orange, destination = red).

**Takeaway:** One brand color, applied everywhere. No secondary accent colors compete. The entire app "feels orange."

---

## 2. Consistent 16px Outer Margins

Every screen uses **~16px horizontal margins** for content outside the map:

- Search card: 16px from screen edges
- Stop list rows: 16px left/right padding
- Bottom sheet content: 16px padding
- Search results: 16px row padding
- Route tabs: 16px left start
- FABs: 16px from right edge

**Takeaway:** 16px is the universal outer gutter — no exceptions observed.

---

## 3. White Background + Floating Card Pattern

All non-map UI uses the same visual treatment:

- **Page background**: white (`#FFFFFF`) — clean, neutral
- **Floating cards**: white background with subtle shadow/elevation, rounded corners (~12px radius)
- **Bottom sheets**: white with rounded top corners
- **Search bars**: white with subtle border or shadow

There are no colored backgrounds, no gradients, no tinted surfaces. White is the only surface color.

**Takeaway:** The visual language is flat-white with shadow-based elevation. Cards and sheets "float" over the map or page.

---

## 4. Search Card as Persistent Navigation Element

The origin/destination search card appears on 3 of 4 screens and behaves as the app's primary navigation hub:

- **Route details**: search card at top → shows origin and destination
- **Map view**: search card floating over the map → same inputs
- **Route planning**: search card with validation state → adds inline error
- **Search screen**: transforms into a focused single-input search bar

### Consistent search card anatomy:
- Origin field: orange icon + placeholder/text
- Destination field: red icon + placeholder/text
- Swap button (↕): right side
- Dotted connector between origin and destination fields

**Takeaway:** The search card is the app's anchor component — it persists across views, adapts to context (floating overlay, full-screen input, validation state), and drives the core user flow.

---

## 5. Map-Centric Layout with Overlay UI

When a map is present (3 of 4 screens), all UI floats on top:

- **Top**: search card overlay + campus selector
- **Right side**: navigation FAB + layers FAB, vertically stacked
- **Bottom**: bottom sheet or route tabs + tab bar
- **No solid nav bars**: the map extends to the edges; UI elements float with shadows

**Takeaway:** The map is always full-bleed. UI components overlay it as floating elements, maximizing the visible map area.

---

## 6. Two-Tab Bottom Navigation

The bottom tab bar is minimal — just 2 tabs:

| Tab | Icon | Label |
|-----|------|-------|
| เส้นทางเดินรถ (Bus route) | Bus route icon (orange when active) | Primary |
| ตารางเดินรถ (Schedule) | Schedule/timetable icon | Secondary |

- Active tab: orange icon + orange text
- Inactive tab: gray icon + gray text
- Height: ~56px
- No FAB overlap (unlike Alma)

**Takeaway:** The tab bar is extremely simple — only 2 options. This keeps the bottom bar lightweight and avoids decision fatigue.

---

## 7. Horizontal Pill Tabs for Route Variants

Route variant selection uses scrollable pill-shaped tabs:

- Labels: เส้นทาง A, B, C, D (Route A, B, C, D)
- Active state: white pill with dark outline/border
- Inactive state: light gray pill, no border
- Scrollable horizontally when more than ~3 tabs
- Positioned between the map and the stop list / route info

**Takeaway:** Pill tabs are the pattern for switching between parallel route options — compact, scannable, and familiar.

---

## 8. Timeline / Vertical Dot List for Stops

The stop list uses a classic **vertical timeline** pattern:

- Each stop = a colored dot (orange) + stop name + optional thumbnail + chevron
- Dots are connected by a thin vertical line
- First stop and last stop are labeled ("ป้ายแรก" / "ป้ายสุดท้าย")
- Thumbnails (small photos) appear right-aligned for visual context
- Rows are ~48–56px tall — comfortable touch targets

**Takeaway:** The timeline is the stop list's signature pattern — it communicates sequence, progress, and route order at a glance.

---

## 9. Bottom Sheet for Contextual Details

When the user selects a location on the map, details appear in a **bottom sheet**:

- Rounded top corners
- Thumbnail image + text (name, nearby stop)
- Dismiss × button
- Action buttons (set as origin / set as destination)
- White background, 16px padding

**Takeaway:** The bottom sheet is the standard pattern for location details — it provides context without leaving the map, and actions are immediately accessible.

---

## 10. Inline Validation, Not Modals

When the user hasn't completed a required field (e.g., origin stop), the app shows:

- Orange ⚠ icon + orange text, directly below the search card
- No modal dialogs, no toast notifications, no separate error screens
- The warning appears contextually — right where the missing input is

**Takeaway:** Validation is inline, non-blocking, and contextual. The user sees the issue exactly where they need to fix it.

---

## 11. Typography — Clean, Functional, 3-Tier Scale

All screens share the same typographic hierarchy:

| Tier | Size | Weight | Usage |
|------|------|--------|-------|
| **Title / Header** | 15–17px | Bold / semi-bold | Route info headers, location names, section headers |
| **Body / Input** | 14–15px | Regular | Stop names, search input, descriptions, placeholders |
| **Caption / Label** | 11–13px | Regular | Tab labels, map labels, meta info, sub-labels |

- **Font**: clean sans-serif, system font — good Thai script support
- **No display/hero type**: unlike the competitor apps, UApp doesn't use oversized numbers or headlines
- **Functional over decorative**: typography serves readability, not emotional impact

**Takeaway:** The type scale is utility-focused. Three clear tiers, no surprises, no decoration.

---

## 12. Consistent Iconography System

Icons follow a strict system across all screens:

| Icon | Shape | Color | Meaning |
|------|-------|-------|---------|
| Bus stop | Circle/square | Orange + white | A bus stop on a route |
| Building/Faculty | Circle | Orange + white | A named building/location |
| Origin | Circle | Orange | Starting point |
| Destination | Circle | Red/coral | Ending point |
| Location pin | Circle | Gray | "Choose on map" action |
| Navigation | Circle | White bg + dark icon | Map compass/recenter |
| Layers | Circle | White bg + dark icon | Map layer switcher |

**Takeaway:** Icons are color-coded by function, not by screen. The same icon = same meaning everywhere.

---

## Summary Table

| Pattern | Screen 1 (Route Details) | Screen 2 (Map + Sheet) | Screen 3 (Search) | Screen 4 (Route Map) |
|---------|:---:|:---:|:---:|:---:|
| Orange brand accent | ✅ | ✅ | ✅ | ✅ |
| 16px outer margins | ✅ | ✅ | ✅ | ✅ |
| White bg + floating cards | ✅ | ✅ | ✅ | ✅ |
| Search card component | ✅ | ✅ | ✅ (adapted) | ✅ |
| Map as full-bleed canvas | ✅ (inline) | ✅ | — | ✅ |
| 2-tab bottom nav | ✅ | — | — | ✅ |
| Pill tabs for routes | ✅ | — | — | ✅ |
| Timeline stop list | ✅ | — | — | — |
| Bottom sheet pattern | — | ✅ | — | — |
| Inline validation | — | — | — | ✅ |
| 3-tier type scale | ✅ | ✅ | ✅ | ✅ |
| Consistent icon system | ✅ | ✅ | ✅ | ✅ |
