#!/usr/bin/env python3
"""Extract detailed structure for documentation"""

import json
from pathlib import Path
from collections import defaultdict

# Load data
data_file = Path(__file__).parent / "figma-variables-export" / "variables-local.json"
with open(data_file) as f:
    data = json.load(f)

meta = data["meta"]
variables = meta["variables"]
collections = meta["variableCollections"]

# Find main collections
primitives_id = "VariableCollectionId:228:1172"
token_id = "VariableCollectionId:228:979"

print("=" * 80)
print("DETAILED STRUCTURE FOR DOCUMENTATION")
print("=" * 80)
print()

# Primitives Collection
if primitives_id in collections:
    primitives = collections[primitives_id]
    primitives_vars = [v for v in variables.values() 
                      if v.get("variableCollectionId") == primitives_id]
    
    print("## PRIMITIVES COLLECTION (Brand Layer)")
    print(f"**Name**: {primitives.get('name')}")
    print(f"**Variables**: {len(primitives_vars)}")
    print(f"**Remote**: {primitives.get('remote', False)}")
    print()
    
    # Group by category
    by_category = defaultdict(list)
    for var in primitives_vars:
        name = var.get("name", "")
        if "/" in name:
            category = name.split("/")[0]
        else:
            category = "Other"
        by_category[category].append((name, var))
    
    print("### Categories:")
    for category in sorted(by_category.keys()):
        vars_list = by_category[category]
        print(f"\n**{category}** ({len(vars_list)} variables):")
        for name, var in sorted(vars_list):
            values = var.get("valuesByMode", {})
            if values:
                mode_id = list(values.keys())[0]
                value = values[mode_id]
                if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                    print(f"  - `{name}` → alias")
                elif isinstance(value, dict) and "r" in value:
                    r, g, b = int(value.get("r", 0) * 255), int(value.get("g", 0) * 255), int(value.get("b", 0) * 255)
                    print(f"  - `{name}` → RGB({r}, {g}, {b})")
                elif isinstance(value, (int, float)):
                    print(f"  - `{name}` → {value}")
                else:
                    print(f"  - `{name}`")
    print()

# Token Collection
if token_id in collections:
    token = collections[token_id]
    token_vars = [v for v in variables.values() 
                  if v.get("variableCollectionId") == token_id]
    
    print("## TOKEN COLLECTION (Alias/Semantic Layer)")
    print(f"**Name**: {token.get('name')}")
    print(f"**Variables**: {len(token_vars)}")
    print(f"**Remote**: {token.get('remote', False)}")
    print()
    
    # Find aliases to Primitives
    aliases_to_primitives = []
    for var in token_vars:
        name = var.get("name", "")
        values_by_mode = var.get("valuesByMode", {})
        for mode_id, value in values_by_mode.items():
            if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                ref_id = value.get("id")
                ref_var = variables.get(ref_id)
                if ref_var:
                    ref_collection_id = ref_var.get("variableCollectionId")
                    if ref_collection_id == primitives_id:
                        aliases_to_primitives.append((name, ref_var.get("name", "")))
    
    print(f"### Alias Connections to Primitives: {len(aliases_to_primitives)}")
    print()
    
    # Group by category
    by_category = defaultdict(list)
    for token_name, prim_name in aliases_to_primitives:
        if "/" in token_name:
            category = token_name.split("/")[0]
        else:
            category = "Other"
        by_category[category].append((token_name, prim_name))
    
    for category in sorted(by_category.keys()):
        aliases = by_category[category]
        print(f"**{category}** ({len(aliases)} aliases):")
        for token_name, prim_name in sorted(aliases)[:10]:
            print(f"  - `{token_name}` → `{prim_name}`")
        if len(aliases) > 10:
            print(f"  - ... and {len(aliases) - 10} more")
        print()

print("=" * 80)
print("CONNECTION SUMMARY")
print("=" * 80)
print()
print("**Brand → Alias Connection Pattern:**")
print("  Primitives (Brand) → Token (Alias/Semantic)")
print()
print(f"  - Primitives collection contains {len(primitives_vars) if primitives_id in collections else 0} raw values")
print(f"  - Token collection contains {len(token_vars) if token_id in collections else 0} semantic tokens")
print(f"  - {len(aliases_to_primitives)} Token variables alias Primitives variables")
