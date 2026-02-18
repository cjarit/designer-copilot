# UApp — Route Planning Map View (Destination Selected)

## Overview
A map-focused route planning screen in **UApp** where a destination has been selected but the origin is still empty. The map shows the campus area with bus stops, route lines, and a selected stop highlighted. A validation message prompts the user to select an origin stop.

---

## Layout & Structure
- **Full-screen map** as the background
- **Top overlay**: back arrow (left) + campus selector dropdown (right)
- **Search card overlay**: origin field (empty, placeholder) + destination field (filled with selected stop name) + clear × + swap button ↕
- **Validation message**: orange warning icon + orange text below the search card ("กรุณาเลือกป้ายต้นทาง" — Please select origin stop)
- **Map content**: multiple bus routes shown as polylines, bus stop markers, building markers, a blue user location dot, shuttle bus icons
- **Route tabs**: horizontal scrollable pill tabs at the bottom of the map area — เส้นทาง A, B, C, D
- **Route info header**: bus icon + route type label + loop info
- **Bottom tab bar**: 2 tabs — เส้นทางเดินรถ (Bus route) and ตารางเดินรถ (Schedule)
- **Navigation FAB + Layers FAB**: floating right side

### Hierarchy
1. Search card with validation warning (action required)
2. Map with route/stop context (spatial orientation)
3. Route tabs + info (navigation)
4. Bottom tabs (section switching)

---

## Spacing & Padding
- **Search card**: ~16px horizontal padding, rounded corners (~12px radius), white background with shadow
- **Origin/destination rows**: ~48px height each, ~12px vertical gap between them
- **Validation message**: ~8px below the search card, ~16px left padding, inline with the card
- **Route tabs**: ~16px left margin, ~8–12px gap between pills, positioned at the bottom of the map
- **Route info header**: ~16px horizontal padding, ~8px gap between icon and text
- **Bottom tab bar**: ~56px height, 2-column split
- **Selected stop callout on map**: floating label with text, positioned near the stop marker
- **FABs**: right-aligned, ~16px from edge, ~44px diameter

---

## Color Usage
- **Map background**: standard light map tiles
- **Route polylines**: multiple blue lines showing different routes — varying shades/opacity to differentiate
- **Selected stop marker**: red/coral large circle with white bus icon — stands out from the orange markers, indicating the chosen destination
- **Regular stop markers**: orange circles/squares with white bus icons
- **Building markers**: orange circles with white building icons (larger)
- **User location**: blue dot (standard iOS blue location indicator)
- **Shuttle bus icons**: small bus illustrations on the route lines — green/white shuttle buses showing real-time positions
- **Validation warning**: orange icon (⚠) + orange text — clear error/attention state
- **Search card**: white background, subtle shadow
- **Origin icon**: orange circle (empty state)
- **Destination icon**: red circle (filled state, matches the selected red marker on map)
- **Route tab active**: white pill with dark text + outline
- **Route tab inactive**: gray pill, lighter text
- **Bottom tab active**: orange icon + text
- **Bottom tab inactive**: gray icon + text
- **Clear × on destination**: gray circle

---

## Typography
- **Search placeholder**: medium (~14–15px), regular, gray — "ค้นหาสถานที่/ป้ายต้นทาง"
- **Filled destination text**: medium (~14–15px), regular, dark/black — truncated with "..." if too long
- **Validation message**: small (~13–14px), regular, orange — warning tone
- **Route tab labels**: small (~13–14px), regular
- **Route info header**: medium (~15–16px), bold, dark
- **Map stop callout labels**: small (~12–13px), bold, dark on a white/translucent background pill
- **Bottom tab labels**: small (~11–12px), regular
- **Tag labels on map ("คนน้อย")**: small (~11px), regular, on a white pill — "Few people" indicating crowd level

---

## Patterns & Components
- **Inline validation**: orange warning appears immediately below the input card when required info is missing — no modal, no toast, just inline
- **Selected vs. unselected markers**: the destination stop turns red/coral (larger) while other stops remain orange — clear visual differentiation
- **Multi-route display**: multiple route polylines shown simultaneously on the map — the user can see how different routes overlap
- **Real-time shuttle indicators**: small bus icons on routes showing where shuttles currently are
- **Crowd indicator tags**: small pills on map showing crowd levels ("คนน้อย" = few people) — real-time occupancy data
- **Search card with validation state**: the card gains an additional warning row when validation fails
- **Consistent pill tabs**: same horizontal scrollable route tabs as the route details screen
- **Persistent campus selector**: the dropdown remains available across all screens

---

## Design Principles Observed
1. **Inline validation over modals**: the warning message is contextual and non-blocking — it appears exactly where the user needs to take action
2. **Color-coded states**: origin = orange, destination = red — consistent color coding across icons, markers, and inputs
3. **Real-time data on map**: shuttle positions and crowd levels are shown directly on the map — no need to navigate elsewhere
4. **Multi-route visibility**: showing overlapping routes helps users understand the transit network spatially
5. **Progressive interaction**: the user can select a destination first, then be guided to select an origin — flexible order
6. **Consistent visual language**: same orange markers, blue polylines, pill tabs, and card treatments as all other screens
