# Designer Copilot

Designer Copilot is an automated/semi-automated Design QA checker for Figma. It helps maintain design system consistency by flagging violations of agreed-upon design rules directly within the design workflow.

## 🚀 Overview

This project provides a specialized agentic workflow to walk through Figma pages, frames, and components to ensure they adhere to foundational design system requirements. It identifies mismatches in spacing, background tokens, and variable bindings, providing actionable fixes for designers and developers.

## 📏 Core Design Rules

The system checks against a set of foundational rules defined in `.agent/rules/design-qa.md`:

### 1. Spacing & Layout
- **Outer Margins**: Must be exactly **16px**.
- **Internal Spacing**: All padding, gaps, and item spacing must use **variables only**.
- **Scale**: Allowed spacing values are `4, 8, 16, 24, 32, 40, 48`.
- *Violations*: Raw numbers, off-scale values, or "detached" tokens.

### 2. Backgrounds & Surfaces
Components must use correct area-specific tokens:
- **Page Background**: `surface/page`
- **Card Background**: `surface/default`
- **Footer Background**: `surface/secondary`
- *Violations*: Any raw color or incorrect token for the specified area.

### 3. Variable Bindings
Everything must reference variables (no raw or detached values):
- Spacing & Colors
- Corner Radius & Border Width
- Typography (Size, Line-height, Weight)

## 🛠 Usage

To run a Design QA check:
1. Provide a Figma URL or node context.
2. Trigger the `/design-qa-command` workflow.
3. The agent will analyze the content and generate a report.

## 📊 Reports

Reports are generated in the `design-qa-report/` directory. Each report includes:
- **Lead Verdict**: PASS/FAIL status.
- **Grouped Issues**: Detailed list of violations by type (Severity: Blocker, Major, Minor, Nit).
- **Suggested Fixes**: Specific tokens or variables to use for correction.

---
*Maintained by the Design Systems Team.*
