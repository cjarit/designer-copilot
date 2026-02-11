# Design QA Report: Transit Search

**Date:** 2026-02-11  
**Figma File:** Transit  
**Node ID:** 2340-155771  
**Node Name:** Transit - Search  
**Reviewed By:** Design QA Checker

---

## Lead Verdict

**❌ FAIL** - Multiple violations found including raw color values, incorrect background token usage, off-scale spacing values, and detached variable references.

---

## Executive Summary

The Transit Search design contains **13 total violations** across spacing, backgrounds, colors, radius, and margin categories. The most critical issues involve:

- Raw color values instead of design token variables
- Off-scale spacing values (5.805px)
- Missing outer margin on the right side
- Raw gradient colors in icon containers
- Raw radius values instead of variables

All violations must be addressed to ensure design system consistency and maintainability.

---

## Issues by Category

### 🔴 Spacing Violations

#### **[Blocker] Off-scale padding in Map Pin components**

- **Location:** Transit - Search > Search Info > Map pin (multiple instances)
- **Node IDs:** 
  - `I2340:155572;2321:22624`
  - `I2340:155622;2321:22624`
  - `I2340:155631;2321:22624`
  - `I2340:155640;2321:22624`
  - `I2340:155649;2321:22624`
  - `I2340:155658;2321:22624`
  - `I2340:155667;2321:22624`
  - `I2340:155676;2321:22624`
- **What's wrong:** Uses `p-[5.805px]` - this is a raw, off-scale value
- **Current:** `5.805px`
- **Expected:** Must use spacing scale: 4, 8, 16, 24, 32, 40, 48
- **Suggested fix:** Use `var(--spacing/space-4,4px)` or `var(--spacing/space-8,8px)`

#### **[Blocker] Asymmetric padding with zero right padding**

- **Location:** Transit - Search > Container > "ค้นหาล่าสุด" section
- **Node ID:** `2340:155568`
- **What's wrong:** Uses `pr-[var(--spacing/space-0,0px)]` - right padding is 0, creating asymmetric spacing
- **Current:** `pl-16, pr-0` (left margin 16px, right margin 0px)
- **Expected:** Consistent outer margins of 16px on both sides
- **Suggested fix:** Change to `pr-[var(--spacing/space-16,16px)]`

---

### 🔴 Background / Surface Violations

#### **[Blocker] Page background uses raw color**

- **Location:** Transit - Search > Root container
- **Node ID:** `2340:155771`
- **What's wrong:** Uses `bg-white` (raw color keyword) instead of surface variable
- **Current:** `bg-white` (raw color)
- **Expected:** `surface/page` for page background
- **Suggested fix:** Use `bg-[var(--color/surface/page)]`

#### **[Blocker] Divider uses raw hex color**

- **Location:** Transit - Search > Divider
- **Node ID:** `2340:155566`
- **What's wrong:** Uses `bg-[#f2f1f6]` - raw hex color value
- **Current:** `#f2f1f6` (raw hex)
- **Expected:** Should use a surface or border variable
- **Suggested fix:** Use `var(--color/surface/secondary)` or create a dedicated divider color variable

---

### 🔴 Variables / Color Violations

#### **[Blocker] Building icon containers use raw gradient colors**

- **Location:** Transit - Search > Search Info > Building icon containers (orange gradient)
- **Node IDs:**
  - `I2340:155570;2326:2522`
  - `I2340:155685;2326:2522`
  - `I2340:155696;2326:2522`
  - `I2340:155707;2326:2522`
  - `I2340:155740;2326:2522`
  - `I2340:155718;2326:2522`
  - `I2340:155729;2326:2522`
- **What's wrong:** Uses raw gradient colors `from-[#ffab00]` and `to-[#f80]`
- **Current:** `#ffab00`, `#f80` (raw hex colors)
- **Expected:** Must use color variables for all colors
- **Suggested fix:** Create gradient color variables:
  - `var(--color/gradient/orange-start)` for `#ffab00`
  - `var(--color/gradient/orange-end)` for `#ff8800`

#### **[Blocker] Bus icon containers use raw gradient colors**

- **Location:** Transit - Search > Search Info > Bus icon containers (gray gradient)
- **Node IDs:**
  - `I2340:155572;2321:22624`
  - `I2340:155622;2321:22624`
  - `I2340:155631;2321:22624`
  - `I2340:155640;2321:22624`
  - `I2340:155649;2321:22624`
  - `I2340:155658;2321:22624`
  - `I2340:155667;2321:22624`
  - `I2340:155676;2321:22624`
- **What's wrong:** Uses raw gradient colors `from-[#666]` and `to-[#444]`
- **Current:** `#666`, `#444` (raw hex colors)
- **Expected:** Must use color variables
- **Suggested fix:** Create gradient color variables:
  - `var(--color/gradient/gray-start)` for `#666666`
  - `var(--color/gradient/gray-end)` for `#444444`

#### **[Major] Building name text uses raw color**

- **Location:** Transit - Search > Search Info > Primary text (building names)
- **Node IDs:**
  - `I2340:155570;2321:22617`
  - `I2340:155685;2321:22617`
  - `I2340:155696;2321:22617`
  - `I2340:155707;2321:22617`
  - `I2340:155740;2321:22617`
  - `I2340:155718;2321:22617`
  - `I2340:155729;2321:22617`
- **What's wrong:** Uses `text-[#2b2f3b]` - raw hex color
- **Current:** `#2b2f3b` (raw hex)
- **Expected:** Should use text color variable
- **Suggested fix:** Use `var(--color/text/main/text-primary,#191919)` or create a new variable if `#2b2f3b` is intentionally different

#### **[Minor] Status bar time uses raw color**

- **Location:** Transit - Search > Native / Status Bar > Time
- **Node ID:** `I2340:155574;21:140`
- **What's wrong:** Uses raw color `text-[#090a0a]` instead of variable
- **Current:** `#090a0a` (raw hex)
- **Expected:** Should use text color variable
- **Suggested fix:** Use `var(--color/text/main/text-primary)` or appropriate variable

---

### 🔴 Radius Violations

#### **[Major] Icon containers use raw radius value**

- **Location:** Transit - Search > Search Info > Building icon containers
- **Node IDs:**
  - `I2340:155570;2326:2522`
  - `I2340:155685;2326:2522`
  - `I2340:155696;2326:2522`
  - `I2340:155707;2326:2522`
  - `I2340:155740;2326:2522`
  - `I2340:155718;2326:2522`
  - `I2340:155729;2326:2522`
- **What's wrong:** Uses `rounded-[10px]` - raw value instead of variable reference
- **Current:** `10px` (raw)
- **Expected:** Must reference radius variable
- **Suggested fix:** Use `var(--radius/radius-8,8px)` or define `var(--radius/radius-10,10px)` if 10px is a design system value

---

### ✅ Outer Margin Check

#### **[Pass] Search bar outer margin**

- **Location:** Transit - Search > Search component
- **Node ID:** `2340:155559`
- **Status:** ✅ **PASS**
- **Current:** `left-[16px]`
- **Expected:** 16px outer margin
- **Note:** This component correctly uses 16px outer margin

---

## Summary by Severity

| Severity | Count | Description |
|----------|-------|-------------|
| **Blocker** | 10 | Critical violations that break core design system rules |
| **Major** | 3 | Important inconsistencies that should be fixed |
| **Minor** | 1 | Small cleanup items |
| **Total** | **14** | **Total violations found** |

---

## Recommended Actions

### Immediate (Blockers)

1. **Replace all raw background colors** with proper surface variables:
   - Change `bg-white` → `bg-[var(--color/surface/page)]`
   - Change `bg-[#f2f1f6]` → `bg-[var(--color/surface/secondary)]` or create divider variable

2. **Fix off-scale spacing value**:
   - Change `p-[5.805px]` → `p-[var(--spacing/space-4,4px)]` or `p-[var(--spacing/space-8,8px)]`

3. **Add missing right outer margin**:
   - Change `pr-[var(--spacing/space-0,0px)]` → `pr-[var(--spacing/space-16,16px)]`

4. **Replace all raw gradient colors** with variables:
   - Create gradient color tokens for `#ffab00`, `#f80`, `#666`, `#444`
   - Update all icon container gradients to use these variables

5. **Replace raw text color** `#2b2f3b` with appropriate text variable

### High Priority (Major)

6. **Replace raw radius values** with radius variables:
   - Change `rounded-[10px]` → `rounded-[var(--radius/radius-10,10px)]` (after creating the variable)

7. **Fix status bar text color**:
   - Change `text-[#090a0a]` → `text-[var(--color/text/main/text-primary)]`

---

## Design System Compliance Checklist

- [ ] All spacing values use variables from the allowed scale (4, 8, 16, 24, 32, 40, 48)
- [ ] Outer margins are consistently 16px on left and right
- [ ] Background colors use appropriate surface tokens (page/default/secondary)
- [ ] All colors reference variables (no raw hex values)
- [ ] All radius values use radius variables
- [ ] All typography uses defined text color variables
- [ ] No detached variable values

---

## Next Steps

1. **Review this report** with the design team
2. **Update the Figma design** to fix all blocker issues
3. **Create missing design tokens** for gradients and any new colors
4. **Re-run Design QA** after fixes are applied
5. **Update design system documentation** if new tokens are added

---

## Reference

- **Design Token Structure:** [design-token-structure.md](file:///Users/ar687101/Documents/designer-copilot/design-token-structure.md)
- **Figma Link:** [Transit - Search](https://www.figma.com/design/ztfv92zQaf3176jp5NGl9A/Transit?node-id=2340-155771)
- **QA Date:** 2026-02-11
- **Report Generated:** 2026-02-11T14:47:38+07:00
