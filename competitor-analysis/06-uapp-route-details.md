# UApp — Route Details / Stop List Screen

## Overview
A bus route detail screen showing origin/destination inputs at the top, an inline map preview, route variant tabs, and a vertical list of all stops along the selected route. The app is **UApp**, a Thai transit/bus routing application.

---

## Layout & Structure
- **Single-column vertical layout**, scrollable
- **Top area**: back arrow (left) + campus/location selector dropdown (right)
- **Search card**: two input fields — origin (blue icon) and destination (red/orange icon) — with a swap button (↕) on the right
- **Inline map**: a rectangular map preview showing the bus route polyline and stop markers
- **Route tabs**: horizontal scrollable tab row — เส้นทาง A, B, C, D (Route A, B, C, D)
- **Route info header**: bus icon + "เส้นทางเดินรถ · วนรอบ" (Bus route · Loop) with first/last stop info
- **Stop list**: vertical list of stops, each row with a colored dot marker, stop name, chevron, and optional thumbnail image
- **Bottom tab bar**: 2 tabs — เส้นทางเดินรถ (Bus route) and ตารางเดินรถ (Schedule), with icons

### Hierarchy
1. Origin/destination inputs (top action area)
2. Map preview (visual context)
3. Route selector tabs (navigation)
4. Stop list (primary content)
5. Bottom tabs (secondary navigation)

---

## Spacing & Padding
- **Outer horizontal margin**: ~16px
- **Search card**: rounded container with ~12–16px internal padding, ~8–12px gap between origin and destination fields
- **Map area**: full-width, ~160–180px height, no horizontal margin (edge-to-edge)
- **Route tabs**: horizontal row with ~8–12px gap between pills, ~16px left padding
- **Route info header**: ~16px horizontal padding, ~8–12px vertical spacing from tabs
- **Stop list rows**: ~48–56px row height, ~16px left padding for the dot + text, thumbnails right-aligned
- **Stop dot (timeline)**: a vertical line connects dots, each dot ~8–10px diameter with ~4px vertical line between
- **Bottom tab bar**: ~56px height, 2-column evenly spaced

---

## Color Usage
- **Page background**: white (`#FFFFFF`)
- **Search card background**: white with subtle shadow or light border
- **Origin icon**: orange circle with white bus icon
- **Destination icon**: red/coral circle with white bus icon
- **Map polyline**: bright blue/royal blue — thick stroke showing the route path
- **Map stop markers**: orange squares with white bus icon, some with blue tint for bus stop signs
- **Active route tab ("เส้นทาง A")**: white pill with dark border/outline (selected state)
- **Inactive route tabs**: light gray background pills, no border
- **Stop list dots**: orange (start), transitioning through the route — consistent orange/amber
- **Thumbnail borders**: light gray, small rounded rectangles
- **Bottom tab active**: orange icon + text (เส้นทางเดินรถ), red/orange accent dot
- **Bottom tab inactive**: gray icon + text
- **Text**: black for stop names, gray for meta info, orange for active elements
- **Campus selector**: dark text with chevron

---

## Typography
- **Campus selector**: medium (~14–15px), regular, dark, with dropdown chevron
- **Search placeholder text**: medium (~14–15px), regular, gray
- **Route tab labels**: small (~13–14px), regular, dark
- **Route info header**: medium (~15–16px), bold, dark — with a bus icon prefix
- **First/last stop info**: small (~12–13px), regular, gray
- **Stop names**: medium (~14–15px), regular to medium weight, dark/black
- **Bottom tab labels**: small (~11–12px), regular
- **Font**: clean sans-serif — appears to be a system font or similar (supports Thai script well)

---

## Patterns & Components
- **Origin/destination input card**: rounded card with two input fields, swap icon, colored circle icons for start/end
- **Inline map preview**: non-interactive (or lightly interactive) map showing the full route
- **Horizontal pill tabs**: scrollable tab row for route variants — pill-shaped, selected state has outline/border
- **Timeline stop list**: vertical timeline with colored dots connected by a thin line — each stop is a row with name + optional thumbnail
- **Stop row chevron**: right-aligned disclosure indicator suggesting tappable rows
- **Thumbnail images**: small photos of each stop location, right-aligned in the row
- **2-tab bottom bar**: simple navigation between route view and schedule view
- **Location dropdown selector**: top-right, allows switching campus/area context

---

## Design Principles Observed
1. **Functional, information-dense layout**: this screen prioritizes showing a lot of data (map, stops, route options) in a compact space
2. **Timeline pattern for stops**: the vertical dot-and-line timeline is a standard transit UX pattern — familiar and scannable
3. **Orange as primary brand color**: orange dominates — icons, active states, markers, dots — it's the brand identity
4. **Map as context, not hero**: the map is small and serves as orientation, not the primary interaction surface
5. **Progressive disclosure**: tap a stop to see details, tap a route tab to switch variants — information is layered
6. **Bilingual readability**: Thai text is well-supported with good sizing for readability of Thai characters
