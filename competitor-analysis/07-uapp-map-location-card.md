# UApp — Map View with Location Bottom Sheet

## Overview
A full-screen map view in **UApp** showing bus route lines and stop markers, with a bottom sheet displaying a selected location's details and two action buttons (set as origin / set as destination).

---

## Layout & Structure
- **Full-screen map** as the background layer
- **Top bar overlay**: back arrow (left) + campus selector dropdown (right), floating over the map
- **Search card overlay**: origin/destination inputs floating at the top over the map
- **Map content**: bus route polyline, stop markers, building labels, a shuttle bus icon on the route
- **Navigation FAB**: compass/navigation icon button, floating right side
- **Layers FAB**: map layers icon button, below the navigation FAB
- **Bottom sheet**: slides up from the bottom with:
  - Location thumbnail (left) + name + nearby stop info (right) + dismiss × (top-right)
  - Two full-width CTA buttons stacked vertically

### Hierarchy
1. Map (spatial context, background)
2. Bottom sheet (selected location details + actions)
3. Search card (route input, top overlay)
4. FABs (map controls)

---

## Spacing & Padding
- **Top bar**: ~16px horizontal padding, floating with slight transparency/shadow
- **Search card**: same as the route details screen — ~16px padding, rounded corners
- **Bottom sheet**: ~16px horizontal padding, ~16px vertical padding
- **Thumbnail**: ~64×64px, rounded corners (~8px), left-aligned
- **Thumbnail to text gap**: ~12px
- **CTA buttons**: full-width, stacked vertically with ~8–12px gap between them
- **CTA button height**: ~48–52px each
- **FABs**: ~44–48px diameter, stacked vertically with ~12px gap, right-aligned ~16px from edge
- **Bottom sheet top to dismiss ×**: ~16px

---

## Color Usage
- **Map**: standard light map style (Google Maps-like) — white roads, light gray buildings, soft muted colors
- **Route polyline**: bright blue, thick stroke with slight curve — consistent with the route details screen
- **Bus stop markers**: orange squares with white bus icon — same as route details
- **Building markers**: orange circles with white building icon (larger, square-rounded)
- **Shuttle bus icon**: white bus on dark background, positioned on the route line showing real-time position
- **Origin button icon**: orange circle with white bus
- **Destination button icon**: red/coral circle with white bus
- **Bottom sheet background**: white, rounded top corners
- **CTA buttons**: white background with gray border/outline, dark text — secondary button style (not filled)
- **Location name text**: black, bold
- **Sub-label text**: gray, regular
- **Dismiss ×**: gray, thin
- **Navigation FAB**: white background, dark icon
- **Layers FAB**: white background, dark icon
- **Validation warning**: orange/amber icon + orange text ("กรุณาเลือกป้ายต้นทาง" — Please select origin stop)

---

## Typography
- **Location name ("คณะกันตแพทยศาสตร์")**: medium (~16–17px), bold, dark — Thai text
- **Sub-label ("ใกล้ป้าย คณะแพทยศาสตร์")**: small (~13–14px), regular, gray
- **CTA button text**: medium (~15–16px), semi-bold, dark, centered
- **Campus selector**: same as route details screen
- **Search placeholder**: same as route details screen
- **Map labels**: small (~11–12px), regular, provided by the map tile

---

## Patterns & Components
- **Bottom sheet modal**: draggable panel from the bottom — iOS-native feeling, with rounded top corners and a handle indicator
- **Location card**: thumbnail + text block — compact, informative
- **Dual CTA buttons**: two outlined buttons for choosing "set as origin" vs. "set as destination" — non-destructive, equal visual weight (neither is primary)
- **Floating map controls**: navigation + layers buttons stacked vertically on the right — common map UI pattern
- **Search card overlay**: persistent input card at the top even on the map view
- **Dismiss ×**: close the bottom sheet to return to map-only view
- **Real-time bus indicator**: shuttle icon on the route line showing current bus position

---

## Design Principles Observed
1. **Map-centric interaction**: the map is the primary canvas; all other UI overlays float on top without obscuring too much
2. **Bottom sheet pattern**: standard mobile pattern for contextual details — the user can dismiss to return to full map
3. **Equal-weight CTAs**: both "set as origin" and "set as destination" are visually equal — no bias toward either action
4. **Contextual information**: the bottom sheet shows what's relevant to the selected location (thumbnail, name, nearest stop)
5. **Consistent marker system**: orange bus stops, blue route lines — the same visual language as the route details screen
6. **Floating UI over map**: search card, nav buttons, and bottom sheet all float without a solid background bar — maximizes map visibility
