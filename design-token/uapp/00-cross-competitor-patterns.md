# Cross-Competitor Common Patterns & Design Principles

Synthesized from 5 screens across **Brilliant** (3 screens) and **Alma** (2 screens).

---

## 1. Layout — Single-Column, Vertically Stacked

Every screen uses a **single-column vertical layout**. There are no side-by-side panels, multi-column grids, or split views. Content flows top-to-bottom in a linear, scrollable stream.

| App | Screen | Layout |
|-----|--------|--------|
| Brilliant | Course path | Single-column node list |
| Brilliant | Paywall | Single-column headline → table → CTA |
| Brilliant | Streak share | Centered card modal |
| Alma | Dashboard | Single-column stacked cards |
| Alma | Widgets | Single-column hero → instructions |

**Takeaway:** Mobile-first means one column. Complexity is handled through vertical stacking and progressive scrolling, never horizontal complexity.

---

## 2. Spacing — Consistent 16px Outer Margins & Generous Whitespace

All screens use **~16px horizontal margins** consistently. Internal spacing is generous, with clear breathing room between sections.

- **Outer margin**: 16px (universal across all screens)
- **Card internal padding**: 16–20px
- **Section gaps**: 16–32px
- **CTA button height**: ~48px
- **Touch targets**: rows/buttons sized for comfortable tapping (~48–64px)

**Takeaway:** There's a shared baseline grid feel. Whitespace is used liberally — none of these screens feel cramped. Density is sacrificed for clarity.

---

## 3. Color Strategy — Restrained Palette + One Bold Accent

Both apps share a disciplined approach to color:

- **Base palette is minimal**: white/cream backgrounds, dark text, gray secondary text
- **One primary accent color** does the heavy lifting:
  - Brilliant → **green** (active states, highlights, CTA)
  - Alma → **olive green** (FAB, score ring, badges)
- **Additional color is purposeful**, not decorative:
  - Color-coded data categories (Alma macros: green/coral/orange/yellow)
  - Gradient treatments for premium emphasis (Brilliant paywall)
  - Celebratory yellow/gold for gamification moments (Brilliant streak)

**Takeaway:** Color is a tool, not decoration. Both apps operate on a near-monochrome base and only introduce color to direct attention, encode data, or create emotional moments.

---

## 4. Typography — Clear 3-Level Size Hierarchy

Both apps use a consistent typographic scale with 3 clearly defined tiers:

| Tier | Size | Weight | Usage |
|------|------|--------|-------|
| **Hero/Display** | 24–72px | Extra bold / bold | Score numbers, streak counts, headlines |
| **Body/Title** | 14–17px | Regular to semi-bold | Feature labels, descriptions, section headers |
| **Caption/Label** | 10–13px | Regular | Tab labels, meta text, unit labels, categories |

Other shared typography patterns:
- **Sans-serif fonts** exclusively (clean, modern, humanist style)
- **Bold weight for hierarchy**, not color — most headings are simply larger + bolder in the same dark color
- **Centered text** for hero content, **left-aligned** for lists and labels
- **Uppercase + letter-spacing** used sparingly for small category labels (Brilliant)

**Takeaway:** Type hierarchy is achieved through size and weight, not font variety. One font family, three tiers, consistent application.

---

## 5. Card-Based Content Architecture

Cards are the dominant container pattern across both apps:

- **Rounded corners**: consistently ~12–20px radius
- **Subtle background differentiation**: cards are slightly lighter or slightly different from the page background (not heavy shadows)
- **Self-contained sections**: each card wraps one distinct idea or data set
- **Consistent padding**: internal padding of 16–24px across all cards

Screens using cards: Alma dashboard (3 cards), Alma widgets (hero + step cards), Brilliant streak (celebration card), Brilliant paywall (table card area).

**Takeaway:** Cards are the universal container. They create visual grouping without heavy borders or dividers. Corner radius is generous (not sharp), and shadows are minimal or absent — background color difference is preferred.

---

## 6. Full-Width CTA Buttons — Dark, Rounded, Bottom-Positioned

Both apps use the exact same CTA button pattern:

- **Full-width** (minus the 16px margins)
- **Dark background** (near-black / charcoal) with **white text**
- **Rounded corners** (~12–16px radius)
- **Positioned at the bottom** of the screen or content area
- **Bold, action-oriented copy** ("Continue path", "Start my free week")

**Takeaway:** The dark full-width CTA at the bottom of the screen is a shared convention. It creates maximum contrast against white/cream backgrounds and anchors the actionable next step.

---

## 7. Minimal Chrome — Content-First UI

Both apps minimize navigation and UI decoration:

- **Nav bars are simple**: just a back arrow + centered title, or a minimal icon set
- **No heavy borders or dividers**: section separation is achieved through whitespace and card containers
- **Tab bars are understated**: small icons + labels in gray, with the active tab slightly highlighted
- **Dismiss buttons (×) are small and unobtrusive**: they exist but don't compete with content
- **No background textures or heavy gradients** in primary content areas

**Takeaway:** The UI "frame" is as invisible as possible. All visual energy goes into the actual content — scores, lessons, features, celebrations.

---

## 8. Progressive Disclosure & Visual Hierarchy

Both apps carefully control what gets attention:

- **Primary element is oversized**: the score number (Alma), streak number (Brilliant), or headline (paywall) dominates the viewport
- **Secondary content is muted**: gray text, smaller type, less visual weight
- **Inactive/unavailable items are grayed out**: locked nodes (Brilliant), "×" marks for missing features (paywall)
- **One CTA per screen**: there's never competing action buttons — one clear next step

**Takeaway:** Each screen has exactly one focal point. Everything else is intentionally secondary. The user's eye is guided, not left to wander.

---

## 9. Gamification & Engagement Mechanics

Both apps (though more prominent in Brilliant) use gamification to drive retention:

| Mechanic | Brilliant | Alma |
|----------|-----------|------|
| **Streaks** | ✅ Lightning bolts, day count, celebration | — |
| **Scores / Progress** | ✅ Node completion, skill tree | ✅ Alma Score (0–100), macro tracking |
| **Levels** | ✅ "Level 1", "Level 2" progression | — |
| **Visual rewards** | ✅ Sparkles, mascot character, gems | ✅ Progress ring fills |
| **Social sharing** | ✅ Share streak card | — |
| **Personalization prompts** | — | ✅ Coaching style nudge |

**Takeaway:** Progress visualization (rings, trees, numbers) and celebratory moments are standard retention tools. Both apps make progress feel tangible and visible.

---

## 10. Warm, Approachable Tone

Neither app feels "corporate" or clinical. Shared tonal patterns:

- **Rounded shapes everywhere**: buttons, cards, icons, progress rings — no sharp corners
- **Friendly copy**: "Continue path", "Start my free week", "Like the Alma app you love" — conversational, not formal
- **Warm color temperatures**: even Brilliant's white-base design uses warm greens; Alma is entirely warm beige/cream/olive
- **Illustrations and characters**: Alma uses emoji-style illustrations (brain icon); Brilliant uses a green mascot blob character
- **Low-pressure engagement**: prompts are dismissible (× buttons), CTAs use trial-language ("free week")

**Takeaway:** The overall feeling across both apps is supportive and encouraging — like a coach, not a tool. Design choices (roundness, warmth, tone) all reinforce this.

---

## Summary Table

| Pattern | Brilliant | Alma | Shared |
|---------|-----------|------|--------|
| Single-column layout | ✅ | ✅ | ✅ |
| 16px outer margins | ✅ | ✅ | ✅ |
| Generous whitespace | ✅ | ✅ | ✅ |
| Restrained base palette | ✅ | ✅ | ✅ |
| Green as primary accent | ✅ | ✅ | ✅ |
| 3-tier typography scale | ✅ | ✅ | ✅ |
| Sans-serif font family | ✅ | ✅ | ✅ |
| Card-based containers | ✅ | ✅ | ✅ |
| Rounded corners (12–20px) | ✅ | ✅ | ✅ |
| Dark full-width CTA button | ✅ | ✅ | ✅ |
| Minimal nav chrome | ✅ | ✅ | ✅ |
| One focal point per screen | ✅ | ✅ | ✅ |
| Progress visualization | ✅ | ✅ | ✅ |
| Warm, approachable tone | ✅ | ✅ | ✅ |
