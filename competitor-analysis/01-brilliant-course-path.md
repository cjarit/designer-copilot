# Brilliant — Course / Learning Path Screen

## Overview
A vertically scrolling course progression screen showing lesson nodes and an "Up next" preview section. The app is **Brilliant**, an education/learning platform.

---

## Layout & Structure
- **Single-column layout**, vertically stacked
- **Top navigation bar**: back chevron (left), category label + lesson title (center), info icon (right)
- **Main content area**: scrollable vertical list of lesson nodes arranged as a skill tree / path
- **"Up next" divider**: a subtle horizontal line with "Up next" label, separating current from upcoming content
- **Bottom tab bar**: 4 tabs — Home, Courses, Leagues, More

### Hierarchy
1. Category label (small, colored, uppercase)
2. Lesson title (large, bold, black)
3. Node icons with labels underneath
4. "Up next" section repeats the category + title pattern
5. CTA button at the bottom of the upcoming section

---

## Spacing & Padding
- **Outer horizontal margin**: ~16px on both sides
- **Top bar padding**: generous vertical padding (~12–16px)
- **Node icon spacing**: large vertical gaps between nodes (~40–60px), creating a spacious, breathable feel
- **"Up next" section**: separated by ample whitespace (~24–32px above/below the divider)
- **CTA button**: full-width with ~16px horizontal padding, ~48px height, generous bottom margin before the tab bar
- **Tab bar**: fixed at the bottom, evenly distributed 4-column grid

---

## Color Usage
- **Background**: pure white (`#FFFFFF`)
- **Primary accent**: green (used for the active node icon badge, category label text) — appears to be around `#00875A` or similar
- **Category label**: bright blue-green, uppercase — strong contrast against white
- **Text**: black for titles, medium gray for descriptions and labels
- **Node icons**: gray (inactive/completed), green highlights for active/current node
- **CTA button**: dark charcoal/near-black background with white text
- **Tab bar**: light gray background, active tab icon in darker/filled style, inactive in outline gray

---

## Typography
- **Category label**: small (~11–12px), uppercase, letter-spaced, bold, colored (blue/green)
- **Lesson title**: large (~20–22px), bold/semi-bold, black, sentence case
- **Node labels**: small (~12–13px), regular weight, gray, centered below icons
- **Description text**: medium (~14–15px), regular, gray, centered
- **CTA button text**: medium (~16px), bold/semi-bold, white, centered
- **Tab bar labels**: small (~10–11px), regular, gray
- **Font family**: appears to be a clean sans-serif (likely system font or custom — possibly Nunito or similar rounded sans-serif)

---

## Patterns & Components
- **Skill tree / node map**: vertically arranged nodes with connecting lines (implied), each node is a circular icon
- **Active node badge**: green circle with an up-arrow + diamond icon, visually prominent
- **Completed/locked nodes**: grayed-out diamond shapes, smaller, less visually prominent
- **"Up next" preview**: shows the next course section inline, maintaining momentum
- **Full-width CTA button**: rounded corners (~12px radius), high contrast, drives action
- **Bottom tab bar**: standard iOS-style fixed tab bar with icon + label

---

## Design Principles Observed
1. **Progressive disclosure**: only the current + next lesson are prominent; past/locked content is muted
2. **Vertical rhythm**: consistent spacing creates a calm, guided flow downward
3. **Minimal chrome**: very little UI decoration — content-first approach
4. **Gamification**: streak/level indicators, node-based progression path
5. **Clear hierarchy**: category → title → content → CTA follows a natural reading order
6. **Restrained color palette**: mostly monochrome with a single green accent for active states
