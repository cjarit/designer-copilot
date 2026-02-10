#!/usr/bin/env python3
"""Analyze the Figma variables structure in detail"""

import json
from pathlib import Path

# Load the variables data
data_file = Path(__file__).parent / "figma-variables-export" / "variables-local.json"
with open(data_file) as f:
    data = json.load(f)

meta = data["meta"]
variables = meta["variables"]
collections = meta["variableCollections"]

# Find the main collections (Primitives, Token, etc.)
print("=" * 80)
print("COLLECTION ANALYSIS")
print("=" * 80)
print()

# Identify key collections
primitives_collections = []
token_collections = []
mapped_collections = []

for coll_id, collection in collections.items():
    name = collection.get("name", "")
    var_count = len(collection.get("variableIds", []))
    
    if "Primitive" in name or "primitive" in name.lower():
        primitives_collections.append((coll_id, collection))
    elif "Token" in name and var_count > 10:
        token_collections.append((coll_id, collection))
    else:
        mapped_collections.append((coll_id, collection))

print("📦 PRIMITIVES COLLECTIONS (Brand Layer):")
print("-" * 80)
for coll_id, coll in primitives_collections:
    print(f"  • {coll.get('name')}")
    print(f"    Variables: {len(coll.get('variableIds', []))}")
    print(f"    Remote: {coll.get('remote', False)}")
    print()

print("📦 TOKEN COLLECTIONS (Alias/Semantic Layer):")
print("-" * 80)
for coll_id, coll in token_collections:
    print(f"  • {coll.get('name')}")
    print(f"    Variables: {len(coll.get('variableIds', []))}")
    print(f"    Remote: {coll.get('remote', False)}")
    print()

print("📦 OTHER COLLECTIONS (Mapped/Component-specific):")
print("-" * 80)
for coll_id, coll in mapped_collections:
    var_count = len(coll.get("variableIds", []))
    if var_count > 0:
        print(f"  • {coll.get('name')}: {var_count} variables")
print()

# Analyze alias connections
print("=" * 80)
print("ALIAS CONNECTION ANALYSIS")
print("=" * 80)
print()

# Find the main Token collection
main_token_collection = None
for coll_id, coll in token_collections:
    if coll.get("name") == "Token" and len(coll.get("variableIds", [])) > 50:
        main_token_collection = coll_id
        break

if main_token_collection:
    print(f"Analyzing 'Token' collection (ID: {main_token_collection})")
    print("-" * 80)
    
    token_vars = [v for v in variables.values() 
                  if v.get("variableCollectionId") == main_token_collection]
    
    # Find variables that alias Primitives
    primitives_aliases = []
    for var in token_vars:
        var_name = var.get("name", "")
        values_by_mode = var.get("valuesByMode", {})
        
        for mode_id, value in values_by_mode.items():
            if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                ref_id = value.get("id")
                ref_var = variables.get(ref_id)
                if ref_var:
                    ref_collection_id = ref_var.get("variableCollectionId")
                    ref_collection = collections.get(ref_collection_id, {})
                    ref_collection_name = ref_collection.get("name", "Unknown")
                    
                    if "Primitive" in ref_collection_name:
                        primitives_aliases.append({
                            "token_var": var_name,
                            "primitive_var": ref_var.get("name", ""),
                            "collection": ref_collection_name
                        })
    
    print(f"\nFound {len(primitives_aliases)} Token → Primitives connections:")
    print()
    
    # Group by category
    by_category = {}
    for alias in primitives_aliases:
        category = alias["token_var"].split("/")[0] if "/" in alias["token_var"] else "Other"
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(alias)
    
    for category, aliases in sorted(by_category.items()):
        print(f"  {category}:")
        for alias in aliases[:5]:  # Show first 5
            print(f"    • {alias['token_var']} → {alias['collection']}::{alias['primitive_var']}")
        if len(aliases) > 5:
            print(f"    ... and {len(aliases) - 5} more")
        print()

# Find Primitives collection
primitives_collection = None
for coll_id, coll in primitives_collections:
    if "Primitives" in coll.get("name"):
        primitives_collection = coll_id
        break

if primitives_collection:
    print("=" * 80)
    print("PRIMITIVES COLLECTION STRUCTURE")
    print("=" * 80)
    print()
    
    primitives_vars = [v for v in variables.values() 
                       if v.get("variableCollectionId") == primitives_collection]
    
    # Group by category
    by_category = {}
    for var in primitives_vars:
        var_name = var.get("name", "")
        category = var_name.split("/")[0] if "/" in var_name else "Other"
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(var_name)
    
    print(f"Total variables in Primitives: {len(primitives_vars)}")
    print()
    for category, var_names in sorted(by_category.items()):
        print(f"  {category}: {len(var_names)} variables")
        for name in sorted(var_names)[:10]:  # Show first 10
            print(f"    • {name}")
        if len(var_names) > 10:
            print(f"    ... and {len(var_names) - 10} more")
        print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print(f"Total Collections: {len(collections)}")
print(f"Total Variables: {len(variables)}")
print()
print("Structure:")
print("  1. Brand/Primitives Layer: Raw color values, spacing, etc.")
print("  2. Alias/Token Layer: Semantic tokens that reference Primitives")
print("  3. Mapped Layer: Component-specific tokens (if any)")
