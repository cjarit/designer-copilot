# Alma — Home / Dashboard Screen

## Overview
The home dashboard of **Alma**, a nutrition/health tracking app. It shows a health score, personalization prompt, and daily macro tracking at a glance.

---

## Layout & Structure
- **Single-column vertical layout** with card-based sections
- **Top area**: centered app avatar/icon + notification badge (top-right)
- **Card 1 (Hero)**: Alma Score — circular progress ring with score number, description text, horizontal dot pagination
- **Card 2**: Coaching style personalization prompt — icon + text + dismiss (×)
- **Card 3**: Daily tracking — "Maintain weight" goal header with macro nutrient circles
- **Bottom tab bar**: 5 tabs — Home, Journal(?), Recipes(?), Food(?), Profile
- **Floating action button (FAB)**: large green "+" button centered above the tab bar

### Hierarchy
1. Score card (primary focus, largest area)
2. Personalization nudge (secondary, actionable)
3. Daily tracking summary (data-dense, glanceable)

---

## Spacing & Padding
- **Outer margin**: ~16px on both sides
- **Card padding**: ~16–20px internal padding on all sides
- **Card-to-card gap**: ~12–16px vertical spacing between cards
- **Score ring**: centered in the card with ~24px padding above and below
- **Macro circles row**: evenly spaced horizontally with ~12–16px gaps, ~8px below the "Maintain weight" header
- **Tab bar**: fixed at bottom, 5-column evenly distributed
- **FAB**: overlaps the tab bar, centered horizontally

---

## Color Usage
- **Page background**: warm beige/cream (`~#F5F0E8` or similar) — earthy, organic feel
- **Card backgrounds**: slightly lighter cream/off-white for differentiation
- **Primary accent**: olive/dark green (used for FAB, score ring active portion, app icon) — `~#3D5A2B` or similar
- **Score ring**: gradient from olive green to yellow-green for the active arc; light gray for the inactive portion
- **Macro circles**: each nutrient has its own color:
  - Calories: green fill (`~#7AB648`)
  - Protein: coral/salmon (`~#E87461`)
  - Carbs: orange (`~#E8963E`)
  - Fat: warm yellow (`~#D4C34A`)
- **Text**: dark brown/charcoal for headings, medium gray-brown for body text
- **Info icon**: small green circle with "i"
- **Notification badge**: olive green with white text
- **"Learn more" link**: brown/dark warm tone, underlined or styled as a link

---

## Typography
- **Score number**: very large (~48–56px), extra bold, dark — dominant visual element
- **"Alma Score" label**: small (~13–14px), regular, with a chevron indicating it's tappable
- **Card description**: medium (~14–15px), regular, gray-brown, centered
- **Personalization card title**: medium (~16px), bold, dark
- **Personalization card body**: small (~13–14px), regular, gray
- **"Learn more" link**: small (~13–14px), medium weight, colored
- **Macro numbers**: large (~20–24px), bold, inside circles
- **Macro unit labels**: small (~10–11px), gray, below the circles
- **Goal header**: medium (~15–16px), semi-bold, with icon
- **Font**: clean, humanist sans-serif — possibly custom or a font like Nunito/DM Sans

---

## Patterns & Components
- **Circular progress ring**: donut chart showing the score out of 100, gradient-colored arc
- **Card-based layout**: distinct cards for each content section, with rounded corners (~16px radius)
- **Dot pagination**: 2 dots below the score card suggesting a horizontally swipeable carousel
- **Personalization nudge card**: icon (brain emoji illustration) + text + dismiss × — an engagement prompt
- **Macro nutrient circles**: small circular progress indicators, each color-coded by nutrient
- **"of X" labels**: showing current/target values (e.g., "316 of 2,100")
- **Floating action button**: large, elevated circle with "+" — prominent entry point for logging food
- **Tab bar with FAB overlap**: the FAB breaks the tab bar boundary, creating visual focus

---

## Design Principles Observed
1. **Warm, organic aesthetic**: the beige/cream palette with olive green feels natural and health-focused — not clinical
2. **Glanceable data**: the score, macros, and goal are all designed for quick scanning
3. **Card-based information architecture**: clear separation of content types via cards
4. **Engagement hooks**: coaching personalization prompt encourages deeper app usage
5. **Color-coded data**: each macro nutrient has its own distinct color for instant recognition
6. **Hierarchy through size**: the score number is enormous, making it the undeniable focal point
7. **Approachable tone**: rounded shapes, warm colors, and friendly copy create a supportive feel
