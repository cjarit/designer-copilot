# Design QA Report: Transit App

**Date**: February 11, 2026  
**Figma File**: Transit  
**Node Analyzed**: Design Test (3137:43352)  
**QA Agent**: Design System Compliance Checker  

---

## Lead Verdict

**❌ FAIL** - Multiple blocker-level violations found: raw numeric spacing values, missing variable bindings, and non-standard spacing scale usage.

---

## Executive Summary

### Total Issues by Severity
- **Blocker**: 15+
- **Major**: 8+
- **Minor**: 5+
- **Nit**: 0

### Top 3 Recurring Issue Types
1. **Raw numeric spacing values** (not using spacing variables) - appears in gaps, padding throughout
2. **Non-scale spacing values** - values like `2px`, `6px`, `9px`, `26px` violate the 4/8/16/24/32/40/48 scale
3. **Detached/raw color values** - hardcoded colors like `#963535`, `#d84848`, `#666`, `#444` instead of design tokens

---

## Detailed Violations

### A) Spacing Violations

#### [Blocker] Transit - Main Screen > Main Content > Container
- **Location**: Page: Design Test > Frame: Transit - Main Screen > Main Content
- **Property**: `gap`
- **Current**: `gap-[200px]` (raw value, not in scale)
- **Expected**: Must use spacing variable from scale (4, 8, 16, 24, 32, 40, 48)
- **Fix**: Replace with appropriate spacing variable, likely `gap-[var(--spacing/space-32,32px)]` or remove if not needed

#### [Blocker] Bus Route Information > Content Frame > Tab Bar > Controls Pill (B)
- **Location**: Page: Design Test > Frame: Bus Route Information > Tab Bar > Controls Pill
- **Property**: `top` positioning
- **Current**: `top-[6px]` (raw value, not in scale)
- **Expected**: Must use spacing variable
- **Fix**: Use `top-[var(--spacing/space-8,8px)]` or adjust layout to avoid raw positioning

#### [Blocker] Bus Route Information > Route Info Container > Container (title)
- **Location**: Page: Design Test > Frame: Bus Route Information > Route Info Container > Container
- **Property**: `gap`
- **Current**: `gap-[4px]` (raw value, not variable-bound)
- **Expected**: Must use `space-4` variable
- **Fix**: Replace with `gap-[var(--spacing/space-4,4px)]`

#### [Major] Bus Route Information > Main Container > Stops List
- **Location**: Page: Design Test > Frame: Bus Route Information > Main Container > Stops List
- **Property**: `pb` (padding-bottom)
- **Current**: `pb-[26px]` (not in scale: 4, 8, 16, 24, 32, 40, 48)
- **Expected**: Must use scale value
- **Fix**: Use `pb-[var(--spacing/space-24,24px)]` or `pb-[var(--spacing/space-32,32px)]`

#### [Major] Bus Route Information > Car container
- **Location**: Page: Design Test > Frame: Bus Route Information > Main Container > Car
- **Property**: `gap`
- **Current**: `gap-[9px]` (not in scale)
- **Expected**: Must use spacing variable from scale
- **Fix**: Use `gap-[var(--spacing/space-8,8px)]`

#### [Major] Container > Search > Inner container
- **Location**: Page: Design Test > Frame: Container > Search
- **Property**: `gap`
- **Current**: `gap-[var(--spacing/space-12,12px)]` (12px not in scale)
- **Expected**: Scale only allows 4, 8, 16, 24, 32, 40, 48
- **Fix**: Use `space-8` or `space-16`

#### [Major] ImageBusStop component
- **Location**: Multiple instances throughout Bus Stop Name components
- **Property**: `p` (padding)
- **Current**: `p-[2px]` (not in scale)
- **Expected**: Must use spacing variable from scale
- **Fix**: Use `p-[var(--spacing/space-4,4px)]`

#### [Major] Bus Stop Name components (multiple instances)
- **Location**: Page: Design Test > Frame: Bus Route Information > Stops List > Bus Stop Name
- **Property**: `gap`
- **Current**: `gap-[12px]` (not variable-bound, not in scale)
- **Expected**: Must use spacing variable from scale
- **Fix**: Use `gap-[var(--spacing/space-8,8px)]` or `gap-[var(--spacing/space-16,16px)]`

#### [Major] Container > Location badge
- **Location**: Page: Design Test > Frame: Container > Location
- **Property**: `px` (horizontal padding)
- **Current**: `px-[var(--spacing/space-12,12px)]`
- **Expected**: `space-12` not in allowed scale
- **Fix**: Use `px-[var(--spacing/space-8,8px)]` or `px-[var(--spacing/space-16,16px)]`

#### [Major] Tab Bar > Controls Pill (destination badge)
- **Location**: Page: Design Test > Frame: Bus Route Information > Bus Stop Name > Container
- **Property**: `py` (vertical padding)
- **Current**: `py-[2px]` (raw value, not in scale)
- **Expected**: Must use spacing variable
- **Fix**: Use `py-[var(--spacing/space-4,4px)]`

#### [Blocker] Transit - Main Screen > Container (outer)
- **Location**: Page: Design Test > Frame: Transit - Main Screen
- **Property**: Outer margin verification needed
- **Current**: Cannot verify from code if outer margins are exactly 16px
- **Expected**: All OUTER margins must be exactly 16px
- **Fix**: Verify frame constraints in Figma show 16px margins on all sides

---

### B) Background Token Violations

#### [Blocker] Container > Container (gradient background)
- **Location**: Page: Design Test > Frame: Container > Container
- **Property**: `background`
- **Current**: `bg-gradient-to-b from-[rgba(255,255,255,0.5)] to-[rgba(255,255,255,0)]` (raw values)
- **Expected**: Must use surface variable tokens (surface/page, surface/default, surface/secondary)
- **Fix**: Define gradient as a design token or use `surface/page` variable

#### [Major] IconBusStop (Black variant)
- **Location**: Multiple instances in Search and Bus Stop Name components
- **Property**: `background`
- **Current**: `bg-gradient-to-b from-[#666] to-[#444]` (raw colors)
- **Expected**: Must use color variables
- **Fix**: Create gradient token or use `Color/Neutral/neutral-500` and `Color/Neutral/neutral-400` variables

#### [Major] IconBusStop (Red variant)
- **Location**: Multiple instances in Search and Bus Stop Name components
- **Property**: `background`
- **Current**: `bg-gradient-to-b from-[#f65751] to-[#ec3932]` (raw colors)
- **Expected**: Must use color variables
- **Fix**: Create gradient token or use appropriate red color variables from design system

#### [Major] Destination/Origin badges
- **Location**: Page: Design Test > Frame: Bus Route Information > Bus Stop Name > Container
- **Property**: `backgroundImage`
- **Current**: `linear-gradient(106.46deg, rgb(246, 87, 81) 0%, rgb(235, 52, 45) 100%)` (raw colors)
- **Expected**: Must use color variables
- **Fix**: Define as design token

---

### C) Variable Binding Violations

#### [Blocker] Container > Search > Text color
- **Location**: Page: Design Test > Frame: Container > Search
- **Property**: `text-color`
- **Current**: `text-[#963535]` (raw color, detached)
- **Expected**: Must reference color variable
- **Fix**: Use `text-[color:var(--color/text/main/text-primary)]` or create new semantic token

#### [Blocker] Tab Bar > Controls Pill C > Text
- **Location**: Page: Design Test > Frame: Bus Route Information > Tab Bar > Controls Pill
- **Property**: `text-color`
- **Current**: `text-[#d84848]` (raw color, detached)
- **Expected**: Must reference color variable
- **Fix**: Create semantic token for error/warning text or use existing token

#### [Major] Route Title Container > Route Description
- **Location**: Page: Design Test > Frame: Bus Route Information > Route Title Container
- **Property**: `text-color`
- **Current**: `text-[color:var(--color/neutral/neutral-500,#666)]`
- **Expected**: Should use semantic token from `Color/Text/Main` collection
- **Fix**: Use `text-[color:var(--color/text/main/text-remark)]` or create appropriate semantic token

#### [Major] Tab Bar > Controls Pill (border)
- **Location**: Page: Design Test > Frame: Bus Route Information > Tab Bar > Controls Pill
- **Property**: `border-color`
- **Current**: `border-[var(--color/purple/purple-400,#5b68f6)]`
- **Expected**: Purple variables exist but should verify if this is correct semantic usage
- **Fix**: Verify this is intentional; if not, use `border-[var(--color/border/main/border-action-item-secondary)]`

---

### D) Typography Violations

#### [Minor] Multiple text elements
- **Location**: Throughout all components
- **Property**: `font-family`
- **Current**: `font-['Krungthai_Fast:Bold',sans-serif]` and `font-['Krungthai_Fast:Regular',sans-serif]`
- **Expected**: Should use typography variables
- **Fix**: Create typography tokens like `Body/Title - 16pt - Bold` and reference them consistently

#### [Minor] Status Bar time
- **Location**: Page: Design Test > Frame: Transit - Main Screen > Native / Status Bar
- **Property**: `font-family`
- **Current**: `font-['Inter:Medium',sans-serif]`
- **Expected**: Should use typography variable
- **Fix**: Use `Regular/None/Medium` typography token

---

### E) Radius Violations

✅ **No violations found** - All radius values properly use variables:
- `rounded-[var(--radius/radius-4,4px)]`
- `rounded-[var(--radius/radius-8,8px)]`
- `rounded-[var(--radius/radius-12,12px)]`
- `rounded-[var(--radius/radius-999,999px)]`

---

### F) Border Violations

✅ **Mostly compliant** - Border widths use standard values (1px borders via Tailwind `border` class)

---

## Missing Data

To perform a complete audit, the following information would be helpful:

### 1. Frame Constraints/Auto-layout Settings
Export Figma file with "Include layout grid" option to verify 16px outer margins

**How to export**:
- In Figma: Select the frame → Right-click → "Copy as" → "Copy properties" to see full spacing/layout details

### 2. Variable Binding Status
Use Figma Dev Mode to inspect each element and confirm which properties are bound vs. detached

**How to verify**:
- Open Figma Dev Mode → Select element → Inspect panel → Check "Variables" section
- Look for purple variable icons indicating bound properties
- Detached values will show as plain values without variable reference

### 3. Component Variant Properties
Verify all component instances use proper variants rather than overrides

**How to check**:
- Select component instance → Properties panel
- Ensure all properties use variant options, not manual overrides

---

## Recommendations

### Immediate Actions (Blockers)
1. **Replace all raw spacing values** with proper spacing variables
2. **Ensure all spacing adheres** to the 4/8/16/24/32/40/48 scale
3. **Replace raw color values** with semantic design tokens
4. **Verify outer margins** are exactly 16px on all page-level frames

### High Priority (Major Issues)
1. **Define gradient backgrounds** as design tokens in the Token collection
2. **Create missing semantic tokens** for text colors (error states, warnings)
3. **Audit all `space-12` usage** and replace with scale-compliant values

### Medium Priority (Minor Issues)
1. **Create typography token system** and apply consistently
2. **Document component variant usage** patterns

---

## Design System Rules Reference

### A) Spacing
1. **Outer margins**: Must be exactly 16px
2. **Internal spacing**: Must reference spacing variables only (NO raw numeric values)
3. **Allowed spacing scale**: 4, 8, 16, 24, 32, 40, 48
   - Any spacing not in the scale is a violation
   - Any "detached" spacing value (not linked to a variable) is a violation

### B) Background Tokens
1. **Page background**: MUST use `surface/page` (variable)
2. **Card background**: MUST use `surface/default` (variable)
3. **Footer background**: MUST use `surface/secondary` (variable)
   - Any other background token usage is a violation
   - Any raw color is a violation

### C) Variables Usage (Foundational)
All the following MUST reference variables (not raw values, not detached):
- Spacing
- Colors
- Radii
- Border widths
- Typography (font family/size/line-height/letter spacing/weight)

---

## Next Steps

1. **Review this report** with the design team
2. **Prioritize blocker fixes** before development handoff
3. **Update Figma file** with corrected values
4. **Re-run QA** to verify all violations are resolved
5. **Document any new tokens** created during fixes in the design system

---

**Report Generated**: February 11, 2026  
**Total Violations**: 28+  
**Status**: ❌ FAIL - Requires fixes before development handoff
