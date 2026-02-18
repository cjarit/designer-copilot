# UApp — Search / Location Lookup Screen

## Overview
A search screen in **UApp** where the user types a query to find a location or bus stop. Results are listed below the search input. The Thai keyboard is visible at the bottom.

---

## Layout & Structure
- **Full-screen white background**
- **Top search bar**: back arrow (left) + text input field (center, active with cursor) + clear × button (right)
- **Results list**: vertical list of search results, each with an icon and text
- **First result**: "เลือกบนแผนที่" (Choose on map) — special action row with a location pin icon
- **Remaining results**: location/stop items, each with:
  - Icon (bus stop icon or building icon, orange)
  - Primary name (bold or medium weight)
  - Secondary line (nearby stop info, gray)
- **Keyboard**: Thai keyboard occupying the bottom ~40% of the screen

### Hierarchy
1. Search input (active, top)
2. "Choose on map" action row (first result, distinct)
3. Search result entries (list, equal weight)
4. Keyboard (system UI)

---

## Spacing & Padding
- **Search bar height**: ~48–52px
- **Search bar horizontal padding**: ~16px (back arrow to edge, × to edge)
- **Input text left padding**: ~12–16px from the back arrow
- **Results list top margin**: ~8–12px below the search bar
- **Result row height**: ~56–64px
- **Result icon size**: ~32–36px diameter circle
- **Icon to text gap**: ~12–16px
- **Result row horizontal padding**: ~16px
- **Row-to-row separator**: subtle line or whitespace, ~1px divider
- **Primary text to secondary text**: ~2–4px vertical gap

---

## Color Usage
- **Background**: white (#FFFFFF)
- **Search bar**: white background with a subtle bottom border or shadow
- **Back arrow**: dark gray/black, thin stroke
- **Clear ×**: gray circle with white ×
- **Input text**: black, regular
- **Cursor**: standard blue text cursor
- **"Choose on map" icon**: gray location pin — distinct from the orange bus icons
- **Bus stop icon**: orange circle with white bus icon (same system-wide marker)
- **Building icon**: orange circle with white building icon
- **Primary text**: dark/black
- **Secondary text**: gray
- **Row separators**: very light gray, subtle

---

## Typography
- **Search input text**: medium (~16–17px), regular, black — active input showing Thai characters
- **"Choose on map"**: medium (~15–16px), medium weight, dark
- **Result primary name**: medium (~15–16px), bold or semi-bold, dark
- **Result secondary text**: small (~13–14px), regular, gray — shows "ใกล้ป้าย ..." (Near stop ...)
- **Last result without secondary**: shows "ไม่มีเส้นทาง" (No route) in gray — informational label
- **Font**: same sans-serif as all other UApp screens

---

## Patterns & Components
- **Full-screen search overlay**: takes over the entire screen — no tabbar, no map visible — focused search experience
- **Back arrow to dismiss**: tap < to return to previous screen
- **Clear button (×)**: circular gray button to clear the search input
- **"Choose on map" row**: a special non-result action allowing the user to switch to map-based selection — distinct icon (pin vs. bus)
- **Icon differentiation**: different icons for bus stops vs. buildings/faculties — helps the user distinguish result types
- **Secondary context line**: "ใกล้ป้าย ..." adds useful proximity info to each result
- **No-route indicator**: one result shows "ไม่มีเส้นทาง" indicating no bus route serves that location — useful negative feedback
- **Thai keyboard integration**: standard iOS Thai keyboard — the app handles Thai input smoothly

---

## Design Principles Observed
1. **Focused search**: the full-screen takeover removes all distractions — the user is in "search mode"
2. **Immediate results**: results appear as the user types (live/incremental search) — no need to submit
3. **Helpful context**: secondary lines add location proximity info, making results more useful
4. **Action + results mixed**: "Choose on map" is an alternative action placed above results — offers an escape hatch from text search
5. **Consistent iconography**: bus stop vs. building icons match the map markers — visual consistency across contexts
6. **Negative feedback**: "ไม่มีเส้นทาง" (no route) is shown inline rather than hiding the result — transparent about coverage
