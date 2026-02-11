---
description: Design check command
---

Please run a Design QA check on the Figma content I provide.

What to do:
1) Review all pages included.
2) Walk through every frame, component, and style.
3) Check against these rules:
   - Outer margin must be 16px
   - Internal spacing must use spacing variables only (no raw values)
   - Allowed spacing scale: 4, 8, 16, 24, 32, 40, 48
   - spacing/colors/radius/border/typography must always reference variables (no raw, no detached)

When you find an issue:
- Tell me where it is (page + frame/component + layer)
- Show current vs expected
- Suggest the fix (what token/variable to use)

At the end:
- Give a PASS/FAIL verdict
- Group issues by type and severity
- Return the report as a list in chat only