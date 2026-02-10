# Transit Design Token Structure

## Overview

This document outlines the design token structure for the Transit Figma file, focusing on the hierarchical relationship between **Brand** (primitives), **Alias** (semantic), and **Mapped Collection** (component-specific) variables.

**Status**: ✅ **ACTUAL STRUCTURE ANALYZED** - This document now reflects the actual variable structure from your Transit Figma file, extracted via the Figma REST API on January 16, 2025.

---

## 1. Variable Collection Architecture

### Three-Tier Token System

The design token structure follows a three-tier hierarchy that enables scalability, maintainability, and consistency:

```
┌─────────────────────────────────────────────────────────┐
│  TIER 1: Brand / Primitives Collection                  │
│  (Raw values - foundation layer)                      │
└─────────────────────────────────────────────────────────┘
                        │
                        │ aliased by
                        ▼
┌─────────────────────────────────────────────────────────┐
│  TIER 2: Alias / Semantic Collection                   │
│  (Contextual naming - usage layer)                     │
└─────────────────────────────────────────────────────────┘
                        │
                        │ aliased by
                        ▼
┌─────────────────────────────────────────────────────────┐
│  TIER 3: Mapped Collection                              │
│  (Component-specific - application layer)               │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Collection Details

### 2.1 Brand / Primitives Collection

**Purpose**: Stores raw, fundamental design values without semantic meaning.

**Actual Structure in Transit File**:
- **Collection Name**: `Primitives`
- **Total Variables**: 35
- **Remote**: No (local collection)
- **Modes**: 1 mode (Mode 1)

**Characteristics**:
- Contains base color ramps organized by color families
- No usage context in naming (e.g., `Color/Neutral/white`, `Color/Green/green-300`)
- Acts as the single source of truth for raw design values
- All variables are color values (RGB)

**Actual Structure**:

**Primitives Collection** (35 variables)

**Color** (35 variables)

- **Color/Blue**
  - Blue-100 : rgb(236,248,255)
  - Blue-300 : rgb(0,135,216)
  - Blue-400 : rgb(2,119,189)
- **Color/Green**
  - green-100 : rgb(225,255,213)
  - green-300 : rgb(26,188,156)
  - green-500 : rgb(54,192,0)
  - green-700 : rgb(4,131,20)
  - green-800 : rgb(0,87,51)
- **Color/Green for Route**
  - green-100 : rgb(235,253,243)
  - green-200 : rgb(198,248,222)
  - green-500 : rgb(13,107,57)
  - green-600 : rgb(8,66,35)
  - green-800 : rgb(4,34,18)
- **Color/KMITL** (University Brand Colors)
  - KMITL-100 : rgb(255,226,206)
  - KMITL-300 : rgb(243,186,156)
  - KMITL-800 : rgb(227,82,5)
- **Color/Neutral**
  - white : rgb(255,255,255)
  - black : rgb(25,25,25)
  - neutral-100 : rgb(244,244,244)
  - neutral-200 : rgb(189,189,189)
  - neutral-300 : rgb(138,138,143)
  - neutral-400 : rgb(128,128,128)
  - neutral-500 : rgb(102,102,102)
  - slategrey-100 : rgb(242,251,255)
  - slategrey-200 : rgb(188,196,204)
  - slategrey-300 : rgb(92,104,115)
- **Color/Pink**
  - Pink 300 : rgb(255,169,237)
  - Pink 400 : rgb(255,111,225)
- **Color/Primary**
  - Primary : rgb(0,129,192)
  - Primary Light : rgb(0,166,230)
  - Primary Lightest : rgb(218,244,255)
- **Color/Purple**
  - Purple 400 : rgb(91,104,246)
  - Purple 500 : rgb(68,80,209)
- **Color/Red**
  - Red-500 : rgb(216,3,3)
- **Color/yellow**
  - yellow : rgb(255,171,0)

**Modes**: 
- Mode 1 (default)

---

### 2.2 Alias / Semantic Collection

**Purpose**: Maps primitive values to semantic, context-aware names that describe usage.

**Actual Structure in Transit File**:
- **Collection Name**: `Token`
- **Total Variables**: 68
- **Remote**: No (local collection)
- **Modes**: 1 mode (Mode 1)
- **Aliases to Primitives**: 30 variables alias Primitives variables

**Characteristics**:
- Variables **alias** (reference) variables from the Primitives collection
- Named for their intended usage context (e.g., `Color/Text/Main/text-primary`, `Color/Surface/Main/surface-white`)
- Provides abstraction layer between raw values and component usage
- Changes to primitives automatically propagate through aliases
- Organized by usage category: Border, Surface, Text, System Icon

**Connection Pattern**:
```
Primitive Variable → Token Variable (via VARIABLE_ALIAS reference)
```

**Actual Structure**:
```
Token Collection (68 variables, 30 alias Primitives)
├── Color/Border/Main (10 variables aliasing Primitives)
│   ├── border-white → Primitives::Color/Neutral/white
│   ├── border-on-white → Primitives::Color/Neutral/neutral-100
│   ├── border-on-grey → Primitives::Color/Neutral/neutral-200
│   ├── border-action-item-secondary → Primitives::Color/Neutral/neutral-300
│   ├── border-dash → Primitives::Color/Neutral/neutral-400
│   ├── border-back-button → Primitives::Color/Neutral/neutral-500
│   ├── border-black → Primitives::Color/Neutral/black
│   ├── border-university-fade → Primitives::Color/KMITL/KMITL-100
│   ├── border-university-light → Primitives::Color/KMITL/KMITL-300
│   └── border-university → Primitives::Color/KMITL/KMITL-800
├── Color/Surface/Main (multiple variables)
│   ├── surface-white → Primitives::Color/Neutral/white
│   ├── surface-grey → Primitives::Color/Neutral/neutral-100
│   ├── surface-black → Primitives::Color/Neutral/black
│   └── (additional surface variables)
├── Color/Text/Main (multiple variables)
│   ├── text-primary → Primitives::Color/Neutral/black
│   ├── text-secondary → (references Primitives)
│   ├── text-university → Primitives::Color/KMITL/KMITL-800
│   └── (additional text variables)
└── Color/System Icon/Main (multiple variables)
    ├── icon-primary → Primitives::Color/Neutral/neutral-300
    ├── icon-disable → Primitives::Color/Neutral/neutral-200
    ├── icon-invert → Primitives::Color/Neutral/white
    ├── icon-black-button → Primitives::Color/Neutral/neutral-400
    ├── icon-black → Primitives::Color/Neutral/black
    ├── icon-university → Primitives::Color/KMITL/KMITL-800
    └── icon-university-secondary → Primitives::Color/KMITL/KMITL-300
```

**Modes**: 
- Mode 1 (default)

---

### 2.3 Mapped Collection (Component-Specific)

**Purpose**: Provides component-level tokens that map to semantic tokens for specific UI components.

**Characteristics**:
- Variables **alias** variables from the Alias/Semantic collection
- Named with component and state context (e.g., `button-background-default`, `card-border-hover`)
- Highly specific to component usage
- Maintains consistency across similar components
- Changes to semantic tokens automatically update component tokens

**Connection Pattern**:
```
Semantic Variable → Component Variable (via reference/alias)
```

**Example Structure**:
```
Mapped Collection
├── Button Tokens
│   ├── button-background-default → {alias.surface-brand}
│   ├── button-background-hover → {alias.surface-brand} (with mode variation)
│   ├── button-background-disabled → {alias.surface-elevated}
│   ├── button-text-default → {alias.text-inverse}
│   └── button-border-default → {alias.border-default}
├── Card Tokens
│   ├── card-background → {alias.surface-elevated}
│   ├── card-border → {alias.border-default}
│   ├── card-shadow → {brand.neutral-900} (with opacity)
│   └── card-text-primary → {alias.text-primary}
├── Input Tokens
│   ├── input-background → {alias.surface-background}
│   ├── input-border-default → {alias.border-default}
│   ├── input-border-focus → {alias.border-focus}
│   └── input-text → {alias.text-primary}
└── Bus Stop Tokens (Transit-specific)
    ├── bus-stop-background-origin → {alias.surface-brand}
    ├── bus-stop-background-destination → {alias.surface-brand}
    ├── bus-stop-text → {alias.text-inverse}
    └── bus-stop-border → {alias.border-default}
```

---

## 3. Connection Flow Diagram

### Complete Alias Chain Example (Actual from Transit File)

```
┌─────────────────────────────────────────────────────────────┐
│ PRIMITIVES (Brand Layer)                                    │
├─────────────────────────────────────────────────────────────┤
│ Color/Neutral/white = rgb(255,255,255)                   │
│ Color/Neutral/black = rgb(25,25,25)                      │
│ Color/Neutral/neutral-100 = rgb(244,244,244)            │
│ Color/Neutral/neutral-200 = rgb(189,189,189)            │
│ Color/KMITL/KMITL-800 = rgb(227,82,5)                    │
└─────────────────────────────────────────────────────────────┘
                        │
                        │ aliased by (VARIABLE_ALIAS)
                        ▼
┌─────────────────────────────────────────────────────────────┐
│ TOKEN (Alias/Semantic Layer)                                │
├─────────────────────────────────────────────────────────────┤
│ Color/Border/Main/border-white → {Color/Neutral/white}      │
│ Color/Surface/Main/surface-white → {Color/Neutral/white}    │
│ Color/Text/Main/text-primary → {Color/Neutral/black}       │
│ Color/System Icon/Main/icon-university → {KMITL-800}       │
└─────────────────────────────────────────────────────────────┘
                        │
                        │ (used directly in components)
                        ▼
┌─────────────────────────────────────────────────────────────┐
│ COMPONENTS (Application Layer)                              │
├─────────────────────────────────────────────────────────────┤
│ Components use Token variables directly                     │
│ - Bus Stop components use Color/Surface/Main tokens        │
│ - Text components use Color/Text/Main tokens                │
│ - Icons use Color/System Icon/Main tokens                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Key Connection Points

### 4.1 Brand → Alias Connection

**Mechanism**: Alias variables use Figma's **variable reference** feature to point to Brand variables.

**Benefits**:
- Single source of truth: Change a brand color once, all semantic tokens update
- Mode support: Different brand modes can map to different semantic values
- Type safety: Ensures semantic tokens use appropriate primitive types

**Example**:
```
Brand Collection:
  - primary-500: #FF6600 (Color)

Alias Collection:
  - text-brand: {primary-500} ← References brand variable
```

### 4.2 Alias → Mapped Connection

**Mechanism**: Mapped variables reference Alias variables, creating a two-level abstraction.

**Benefits**:
- Semantic consistency: Components use meaningful names, not raw values
- Easy theming: Change semantic tokens to update all components
- Maintainability: Update component behavior by changing semantic layer

**Example**:
```
Alias Collection:
  - surface-brand: {primary-500} ← References brand
  - text-inverse: {neutral-0} ← References brand

Mapped Collection:
  - button-background-default: {surface-brand} ← References alias
  - button-text-default: {text-inverse} ← References alias
```

### 4.3 Mode Propagation

**How Modes Flow Through the System**:

1. **Brand Collection Modes**: Define different brand color palettes
   - Mode: "Default Brand" → primary-500 = #FF6600
   - Mode: "Brand Variant" → primary-500 = #0066FF

2. **Alias Collection Modes**: Reference brand modes, add semantic context
   - Mode: "Light" → text-primary = {neutral-900}
   - Mode: "Dark" → text-primary = {neutral-0}

3. **Mapped Collection**: Inherits modes from alias layer
   - When alias mode changes, mapped tokens automatically update

---

## 5. Variable Scoping

**Purpose**: Restrict where variables can be used to prevent misuse.

**Common Scopes**:
- **Color variables**: Can be used for fill, stroke, text color
- **Spacing variables**: Can be used for padding, margin, gap
- **Typography variables**: Can be used for font size, line height
- **Component-specific**: Limited to specific component properties

**Example**:
```
text-primary (Alias)
  - Scope: Text color only
  - Cannot be used for: Fill, Stroke

surface-background (Alias)
  - Scope: Fill only
  - Cannot be used for: Text color, Stroke
```

---

## 6. Naming Conventions

### Brand / Primitives
- Format: `{category}-{value}`
- Examples: `primary-500`, `neutral-900`, `spacing-16`
- No semantic meaning in names

### Alias / Semantic
- Format: `{context}-{usage}`
- Examples: `text-primary`, `surface-background`, `border-default`
- Describes where/how the token is used

### Mapped / Component-Specific
- Format: `{component}-{property}-{state}`
- Examples: `button-background-default`, `card-border-hover`
- Highly specific to component and state

---

## 7. Benefits of This Structure

### Scalability
- Add new components by creating mapped tokens that reference existing semantic tokens
- Add new brands by creating new modes in the brand collection

### Maintainability
- Update a brand color → All semantic tokens update → All components update
- Change semantic meaning → Components automatically reflect changes

### Consistency
- Designers use semantic names (easier to understand)
- Developers get consistent token names across components
- Prevents arbitrary value usage

### Flexibility
- Support multiple brands via modes
- Support light/dark themes via alias modes
- Easy to add new themes without duplicating tokens

---

## 8. Transit-Specific Considerations

Based on the actual Transit design file structure:

### Color Categories in Primitives
- **KMITL Colors**: University brand colors (KMITL-100, KMITL-300, KMITL-800) used throughout the transit system
- **Green for Route**: Specific green shades for route visualization (green-100 through green-800)
- **Neutral Colors**: Comprehensive neutral palette (white, black, neutral-100 through neutral-500, slategrey variants)
- **Primary Colors**: Main brand primary color with light variants

### Token Usage Patterns
- **Border Tokens**: Used for component borders, dividers, and UI element outlines
- **Surface Tokens**: Used for backgrounds, cards, and container fills
- **Text Tokens**: Used for all text content with semantic naming (primary, secondary, university)
- **System Icon Tokens**: Used for icon colors with state variations (primary, disable, invert, black, university)

### Connection Points
- **30 Token variables** directly alias Primitives variables
- **38 Token variables** have direct color values (not aliased)
- All alias connections use the `VARIABLE_ALIAS` type in Figma
- Changes to Primitives automatically propagate to all aliased Token variables

---

## 9. Actual Structure Summary

✅ **Verified Structure** (as of January 16, 2025):

### Collections Overview
- **Total Collections**: 16
- **Total Variables**: 150
- **Main Collections**:
  - `Primitives`: 35 variables (Brand layer)
  - `Token`: 68 variables (Alias/Semantic layer)
  - Other collections: 47 variables (various purposes)

### Key Connections Verified
- ✅ **Primitives → Token**: 30 alias connections identified
- ✅ **Connection Type**: VARIABLE_ALIAS (Figma's native alias mechanism)
- ✅ **Connection Pattern**: Token variables reference Primitives variables by ID

### Variable Distribution
- **Primitives Collection**:
  - 35 color variables
  - All are direct RGB values
  - Organized by color families (Blue, Green, KMITL, Neutral, Pink, Primary, Purple, Red, Yellow)
  
- **Token Collection**:
  - 68 variables total
  - 30 alias Primitives (44%)
  - 38 have direct values (56%)
  - Organized by usage (Border, Surface, Text, System Icon)

---

## 10. Data Collection Methods

✅ **Data Successfully Collected** (January 16, 2025)

### Method Used: Figma REST API

The variable structure was successfully extracted using the Figma REST API:

```bash
# Script used: fetch_figma_variables.py
python3 fetch_figma_variables.py --token [FIGMA_TOKEN]
```

**Data Files Generated**:
- `figma-variables-export/variables-local.json` - Complete local variables with aliases
- `figma-variables-export/variables-published.json` - Published variables
- `figma-variables-export/file-data.json` - File metadata

**Analysis Scripts**:
- `fetch_figma_variables.py` - Fetches and analyzes variables
- `analyze_structure.py` - Analyzes collection structure
- `extract_detailed_structure.py` - Extracts detailed documentation data

### Alternative Methods

If you need to update this analysis in the future:

1. **Figma REST API** (Recommended): Use the provided Python script
2. **Manual Documentation**: Open Variables panel in Figma and document changes
3. **Figma Plugin Export**: Use Tokens Studio or similar plugins to export JSON

---

## 11. Connection Mechanism Details

### How Aliases Work in Figma

In the Transit file, the connection between **Primitives** and **Token** collections uses Figma's native **VARIABLE_ALIAS** mechanism:

1. **Variable Definition**: A Token variable defines its value as a VARIABLE_ALIAS type
2. **Reference ID**: The alias contains the ID of the referenced Primitives variable
3. **Automatic Updates**: When a Primitives variable changes, all Token variables that alias it automatically update
4. **Type Safety**: Figma ensures the alias references a compatible variable type (color → color)

### Example from Actual Data

```json
{
  "name": "Color/Border/Main/border-white",
  "variableCollectionId": "VariableCollectionId:228:979",  // Token collection
  "valuesByMode": {
    "228:0": {
      "type": "VARIABLE_ALIAS",
      "id": "VariableID:228:1173"  // References Primitives::Color/Neutral/white
    }
  }
}
```

### Connection Statistics

- **Total Alias Connections**: 30 Token → Primitives
- **Connection Categories**:
  - Border: 10 connections
  - Surface: Multiple connections
  - Text: Multiple connections
  - System Icon: Multiple connections
- **Unaliased Token Variables**: 38 (have direct color values)

---

*Last Updated: January 16, 2025*  
*File: Transit Figma Design*  
*Figma File Key: ztfv92zQaf3176jp5NGl9A*  
*Figma URL: https://www.figma.com/design/ztfv92zQaf3176jp5NGl9A/Transit*  
*Analysis Method: Figma REST API (variables/local endpoint)*  
*Data Files: figma-variables-export/variables-local.json*
