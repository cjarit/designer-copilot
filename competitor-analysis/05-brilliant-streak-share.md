# Brilliant — Streak Celebration & Share Screen

## Overview
A gamification celebration screen in **Brilliant** showing a learning streak achievement with a share sheet at the bottom. The background is dimmed, focusing attention on the streak card and the sharing options.

---

## Layout & Structure
- **Overlay/modal on a dimmed background**: the underlying screen is visible but darkened
- **Centered streak card**: rounded card showing the streak celebration visual
- **Underlying streak summary bar**: just visible below the card, showing the streak count + gem icons
- **Bottom share sheet**: iOS-native-style share sheet with action icons

### Hierarchy
1. Streak celebration card (hero, emotional)
2. Share sheet (action)
3. Dimmed background content (context)

---

## Spacing & Padding
- **Streak card**: centered horizontally and vertically (slightly above center)
- **Card internal padding**: ~20–24px
- **Card to share sheet gap**: significant (~60–80px)
- **Share sheet internal padding**: ~16–20px horizontal, ~16px vertical
- **Share action icons**: evenly spaced horizontally with ~16–24px gaps
- **Icon to label gap**: ~8px below each icon circle

---

## Color Usage
- **Overlay background**: semi-transparent dark gray/black (~50–60% opacity) — focuses attention
- **Streak card background**: white with a subtle grid/graph pattern
- **Lightning bolt icons**: bright yellow/gold — energetic, celebratory
- **Streak number ("2")**: bold green with a gradient/3D effect — yellow-green to darker green
- **Celebration character**: green blob/mascot with sparkles — brand character
- **Sparkle/star decorations**: yellow/gold, reinforcing the celebratory mood
- **"Brilliant" brand name on card**: dark, clean text
- **Share sheet background**: white, rounded top corners
- **Share action circles**: 
  - Messages: green (iMessage green)
  - Save Image: light gray
  - More: light gray
- **"Share your streak" header**: black, bold
- **Close ×**: dark gray

---

## Typography
- **"Brilliant" text on card**: medium (~15–16px), semi-bold, centered
- **Streak number**: very large (~64–72px), extra bold, centered — dominant element
- **"day learning streak"**: medium (~16px), regular, gray, centered below the number
- **"Share your streak"**: medium (~16–17px), bold, left-aligned in the share sheet
- **Action labels**: small (~11–12px), regular, gray, centered below icons
- **Font**: same clean sans-serif as the rest of the Brilliant app

---

## Patterns & Components
- **Celebration card**: a sharable asset (designed to look good when shared on social media)
- **Grid/graph background on card**: subtle detail suggesting data/progress tracking
- **Character/mascot**: the green blob character adds personality and emotional connection
- **Lightning bolt motif**: repeated as a gamification symbol for streaks
- **iOS-style share sheet**: "Share your streak" header + row of action icons (Messages, Save Image, More)
- **Dimmed overlay**: standard modal treatment, keeps context visible while focusing on the celebration
- **3D-style number rendering**: the streak count has a slight shadow/gradient giving it dimensional depth

---

## Design Principles Observed
1. **Emotional celebration**: the entire screen is designed to make the user feel accomplished — bright colors, sparkles, mascot character
2. **Social sharing by design**: the streak card is deliberately crafted as a shareable asset with the brand name
3. **Gamification**: streaks, lightning bolts, gems — multiple reward mechanics visible
4. **Focus through dimming**: the overlay removes distractions, centering attention on the achievement
5. **Viral loop**: making sharing easy and the card visually appealing encourages social distribution
6. **Playful energy**: yellow/green palette with sparkles creates a fun, youthful tone
7. **Minimal action required**: share options are presented immediately — low friction for sharing
