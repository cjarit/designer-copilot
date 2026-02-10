#!/usr/bin/env python3
"""
Script to fetch Figma variables and analyze the structure

Usage:
    export FIGMA_TOKEN=your_token
    python3 fetch_figma_variables.py

Or:
    python3 fetch_figma_variables.py --token your_token
"""

import os
import sys
import json
import argparse
from pathlib import Path

FILE_KEY = "ztfv92zQaf3176jp5NGl9A"

def fetch_variables(token):
    """Fetch variables from Figma API"""
    import ssl
    import urllib.request
    import urllib.error
    
    headers = {
        "X-FIGMA-TOKEN": token
    }
    
    print("Fetching Figma variables...\n")
    
    # Create output directory
    output_dir = Path(__file__).parent / "figma-variables-export"
    output_dir.mkdir(exist_ok=True)
    
    # Create SSL context that doesn't verify certificates (for sandbox environments)
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    # Fetch local variables (most detailed - includes modes and aliases)
    try:
        print("Fetching local variables...")
        req = urllib.request.Request(
            f"https://api.figma.com/v1/files/{FILE_KEY}/variables/local",
            headers=headers
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            local_data = json.loads(response.read().decode())
            
        with open(output_dir / "variables-local.json", "w") as f:
            json.dump(local_data, f, indent=2)
        print("✓ Saved variables-local.json")
        
        # Analyze structure
        analyze_structure(local_data)
        
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"Error fetching local variables: {e.code}")
        print(error_body)
        
        if e.code == 403:
            print("\nNote: Local variables endpoint requires Enterprise plan and file_variables:read scope")
            print("Trying published variables instead...\n")
            return fetch_published_variables(token, output_dir)
        else:
            return None
    
    # Also fetch published variables for comparison
    try:
        print("\nFetching published variables...")
        req = urllib.request.Request(
            f"https://api.figma.com/v1/files/{FILE_KEY}/variables/published",
            headers=headers
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            published_data = json.loads(response.read().decode())
            
        with open(output_dir / "variables-published.json", "w") as f:
            json.dump(published_data, f, indent=2)
        print("✓ Saved variables-published.json")
        
    except urllib.error.HTTPError as e:
        print(f"Note: Could not fetch published variables: {e.code}")
    
    # Fetch file data to see bound variables
    try:
        print("\nFetching file data...")
        req = urllib.request.Request(
            f"https://api.figma.com/v1/files/{FILE_KEY}",
            headers=headers
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            file_data = json.loads(response.read().decode())
            
        with open(output_dir / "file-data.json", "w") as f:
            json.dump(file_data, f, indent=2)
        print("✓ Saved file-data.json")
        
    except urllib.error.HTTPError as e:
        print(f"Note: Could not fetch file data: {e.code}")
    
    print(f"\n✓ All data saved to: {output_dir}/")
    return local_data

def fetch_published_variables(token, output_dir):
    """Fetch published variables as fallback"""
    import ssl
    import urllib.request
    import urllib.error
    
    headers = {
        "X-FIGMA-TOKEN": token
    }
    
    # Create SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    try:
        req = urllib.request.Request(
            f"https://api.figma.com/v1/files/{FILE_KEY}/variables/published",
            headers=headers
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            data = json.loads(response.read().decode())
            
        with open(output_dir / "variables-published.json", "w") as f:
            json.dump(data, f, indent=2)
        print("✓ Saved variables-published.json")
        
        analyze_published_structure(data)
        print(f"\n✓ Data saved to: {output_dir}/")
        return data
        
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"Error: {e.code}")
        print(error_body)
        return None

def analyze_structure(data):
    """Analyze the variable structure and connections"""
    print("\n" + "=" * 60)
    print("VARIABLE STRUCTURE ANALYSIS")
    print("=" * 60 + "\n")
    
    if not data.get("meta") or not data["meta"].get("variables"):
        print("No variables found in response")
        return
    
    variables = data["meta"]["variables"]
    variable_collections = data["meta"].get("variableCollections", {})
    
    print(f"Collections: {len(variable_collections)}")
    print(f"Variables: {len(variables)}\n")
    
    # Group variables by collection
    by_collection = {}
    for var_id, variable in variables.items():
        collection_id = variable.get("variableCollectionId")
        if collection_id not in by_collection:
            by_collection[collection_id] = []
        by_collection[collection_id].append(variable)
    
    # Analyze each collection
    for collection_id, collection in variable_collections.items():
        print(f"\n📦 Collection: {collection.get('name', 'Unnamed')}")
        print(f"   ID: {collection_id}")
        
        modes = collection.get("modes", {})
        if modes:
            # Modes can be a dict or list depending on API version
            if isinstance(modes, dict):
                mode_names = [mode.get("name", "Unnamed") for mode in modes.values()]
            elif isinstance(modes, list):
                mode_names = [mode.get("name", "Unnamed") if isinstance(mode, dict) else str(mode) for mode in modes]
            else:
                mode_names = [str(mode) for mode in modes]
            print(f"   Modes: {', '.join(mode_names)}")
        
        collection_vars = by_collection.get(collection_id, [])
        print(f"   Variables: {len(collection_vars)}")
        
        # Check for aliases
        aliases = []
        for var in collection_vars:
            values_by_mode = var.get("valuesByMode", {})
            for mode, value in values_by_mode.items():
                if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                    aliases.append((var, mode, value))
        
        if aliases:
            print(f"   ⚡ Aliases: {len(aliases)}")
            for var, mode, alias_value in aliases[:5]:  # Show first 5
                ref_id = alias_value.get("id", "unknown")
                ref_var = variables.get(ref_id, {})
                ref_name = ref_var.get("name", "unknown")
                ref_collection_id = ref_var.get("variableCollectionId", "unknown")
                ref_collection = variable_collections.get(ref_collection_id, {})
                ref_collection_name = ref_collection.get("name", "Unknown")
                print(f"      - {var.get('name')} ({mode}) → {ref_collection_name}::{ref_name}")
            if len(aliases) > 5:
                print(f"      ... and {len(aliases) - 5} more")
    
    # Map alias connections
    print("\n" + "=" * 60)
    print("ALIAS CONNECTIONS (Brand → Alias → Mapped)")
    print("=" * 60 + "\n")
    
    # Create a map of variable ID to variable name and collection
    var_info = {}
    for var_id, variable in variables.items():
        collection_id = variable.get("variableCollectionId", "unknown")
        collection = variable_collections.get(collection_id, {})
        var_info[var_id] = {
            "name": variable.get("name", "Unnamed"),
            "collection": collection.get("name", "Unknown")
        }
    
    # Find all alias connections
    connections = []
    for variable in variables.values():
        collection_id = variable.get("variableCollectionId", "unknown")
        collection = variable_collections.get(collection_id, {})
        collection_name = collection.get("name", "Unknown")
        var_name = variable.get("name", "Unnamed")
        
        values_by_mode = variable.get("valuesByMode", {})
        for mode, value in values_by_mode.items():
            if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
                ref_id = value.get("id")
                if ref_id in var_info:
                    ref_info = var_info[ref_id]
                    connections.append({
                        "from": f"{collection_name}::{var_name}",
                        "to": f"{ref_info['collection']}::{ref_info['name']}",
                        "mode": mode
                    })
    
    # Group and display connections
    if connections:
        for conn in connections[:20]:  # Show first 20
            print(f"{conn['from']} → {conn['to']} ({conn['mode']})")
        if len(connections) > 20:
            print(f"\n... and {len(connections) - 20} more connections")
    else:
        print("No alias connections found")

def analyze_published_structure(data):
    """Analyze published variables structure"""
    print("\n" + "=" * 60)
    print("PUBLISHED VARIABLES ANALYSIS")
    print("=" * 60 + "\n")
    
    if not data.get("meta") or not data["meta"].get("variables"):
        print("No published variables found")
        return
    
    variables = data["meta"]["variables"]
    variable_collections = data["meta"].get("variableCollections", {})
    
    print(f"Collections: {len(variable_collections)}")
    print(f"Variables: {len(variables)}\n")
    
    # Group by collection
    by_collection = {}
    for var_id, variable in variables.items():
        collection_id = variable.get("variableCollectionId")
        if collection_id not in by_collection:
            by_collection[collection_id] = []
        by_collection[collection_id].append(variable)
    
    for collection_id, collection in variable_collections.items():
        collection_vars = by_collection.get(collection_id, [])
        print(f"📦 {collection.get('name', 'Unnamed')}: {len(collection_vars)} variables")

def main():
    parser = argparse.ArgumentParser(description="Fetch and analyze Figma variables")
    parser.add_argument(
        "--token",
        help="Figma API token (or set FIGMA_TOKEN environment variable)",
        default=os.environ.get("FIGMA_TOKEN")
    )
    
    args = parser.parse_args()
    
    if not args.token:
        print("Error: FIGMA_TOKEN environment variable is required")
        print("\nTo get your token:")
        print("1. Go to https://www.figma.com/settings")
        print("2. Scroll to 'Personal access tokens'")
        print("3. Click 'Create new token'")
        print("4. Copy the token")
        print("\nThen run:")
        print("  export FIGMA_TOKEN=your_token")
        print("  python3 fetch_figma_variables.py")
        print("\nOr:")
        print("  python3 fetch_figma_variables.py --token your_token")
        sys.exit(1)
    
    result = fetch_variables(args.token)
    
    if result:
        print("\n" + "=" * 60)
        print("SUCCESS!")
        print("=" * 60)
        print("\nYou can now:")
        print("1. Review the JSON files in figma-variables-export/")
        print("2. Share the analysis output above")
        print("3. The structure will be documented in design-token-structure.md")

if __name__ == "__main__":
    main()
