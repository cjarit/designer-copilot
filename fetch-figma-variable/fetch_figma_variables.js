#!/usr/bin/env node
/**
 * Script to fetch Figma variables and analyze the structure
 * 
 * Usage:
 *   FIGMA_TOKEN=your_token node fetch_figma_variables.js
 * 
 * Or set in environment:
 *   export FIGMA_TOKEN=your_token
 *   node fetch_figma_variables.js
 */

const FILE_KEY = "ztfv92zQaf3176jp5NGl9A";
const TOKEN = process.env.FIGMA_TOKEN;

if (!TOKEN) {
  console.error("Error: FIGMA_TOKEN environment variable is required");
  console.error("Get your token from: https://www.figma.com/settings");
  process.exit(1);
}

const headers = {
  "X-FIGMA-TOKEN": TOKEN,
};

async function fetchVariables() {
  try {
    console.log("Fetching Figma variables...\n");

    // Fetch local variables (most detailed - includes modes and aliases)
    const localResponse = await fetch(
      `https://api.figma.com/v1/files/${FILE_KEY}/variables/local`,
      { headers }
    );
    
    if (!localResponse.ok) {
      const error = await localResponse.text();
      console.error(`Error fetching local variables: ${localResponse.status}`);
      console.error(error);
      
      if (localResponse.status === 403) {
        console.error("\nNote: This endpoint requires Enterprise plan and file_variables:read scope");
        console.error("Trying published variables instead...\n");
        return await fetchPublishedVariables();
      }
      return;
    }

    const localData = await localResponse.json();
    
    // Also fetch published variables for comparison
    const publishedResponse = await fetch(
      `https://api.figma.com/v1/files/${FILE_KEY}/variables/published`,
      { headers }
    );
    
    let publishedData = null;
    if (publishedResponse.ok) {
      publishedData = await publishedResponse.json();
    }

    // Fetch file data to see bound variables
    const fileResponse = await fetch(
      `https://api.figma.com/v1/files/${FILE_KEY}`,
      { headers }
    );
    
    let fileData = null;
    if (fileResponse.ok) {
      fileData = await fileResponse.json();
    }

    // Save raw data
    const fs = require('fs');
    const path = require('path');
    
    const outputDir = path.join(__dirname, 'figma-variables-export');
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(
      path.join(outputDir, 'variables-local.json'),
      JSON.stringify(localData, null, 2)
    );
    console.log("✓ Saved variables-local.json");

    if (publishedData) {
      fs.writeFileSync(
        path.join(outputDir, 'variables-published.json'),
        JSON.stringify(publishedData, null, 2)
      );
      console.log("✓ Saved variables-published.json");
    }

    if (fileData) {
      fs.writeFileSync(
        path.join(outputDir, 'file-data.json'),
        JSON.stringify(fileData, null, 2)
      );
      console.log("✓ Saved file-data.json");
    }

    // Analyze structure
    analyzeStructure(localData);

    console.log(`\n✓ All data saved to: ${outputDir}/`);
    console.log("\nYou can now share these files or the analysis output.");

  } catch (error) {
    console.error("Error:", error.message);
    process.exit(1);
  }
}

async function fetchPublishedVariables() {
  try {
    const response = await fetch(
      `https://api.figma.com/v1/files/${FILE_KEY}/variables/published`,
      { headers }
    );

    if (!response.ok) {
      const error = await response.text();
      console.error(`Error: ${response.status}`);
      console.error(error);
      return;
    }

    const data = await response.json();
    
    const fs = require('fs');
    const path = require('path');
    const outputDir = path.join(__dirname, 'figma-variables-export');
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(
      path.join(outputDir, 'variables-published.json'),
      JSON.stringify(data, null, 2)
    );
    console.log("✓ Saved variables-published.json");
    
    analyzePublishedStructure(data);
    console.log(`\n✓ Data saved to: ${outputDir}/`);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

function analyzeStructure(data) {
  console.log("\n" + "=".repeat(60));
  console.log("VARIABLE STRUCTURE ANALYSIS");
  console.log("=".repeat(60) + "\n");

  if (!data.meta || !data.meta.variables) {
    console.log("No variables found in response");
    return;
  }

  const { variables, variableCollections } = data.meta;

  console.log(`Collections: ${Object.keys(variableCollections).length}`);
  console.log(`Variables: ${Object.keys(variables).length}\n`);

  // Group variables by collection
  const byCollection = {};
  Object.values(variables).forEach(variable => {
    const collectionId = variable.variableCollectionId;
    if (!byCollection[collectionId]) {
      byCollection[collectionId] = [];
    }
    byCollection[collectionId].push(variable);
  });

  // Analyze each collection
  Object.entries(variableCollections).forEach(([collectionId, collection]) => {
    console.log(`\n📦 Collection: ${collection.name}`);
    console.log(`   ID: ${collectionId}`);
    console.log(`   Modes: ${Object.keys(collection.modes || {}).join(", ")}`);
    console.log(`   Variables: ${(byCollection[collectionId] || []).length}`);

    const collectionVars = byCollection[collectionId] || [];
    
    // Check for aliases (variables that reference other variables)
    const aliases = collectionVars.filter(v => 
      v.valuesByMode && 
      Object.values(v.valuesByMode).some(val => 
        typeof val === 'object' && val.type === 'VARIABLE_ALIAS'
      )
    );

    if (aliases.length > 0) {
      console.log(`   ⚡ Aliases: ${aliases.length}`);
      aliases.forEach(alias => {
        Object.entries(alias.valuesByMode || {}).forEach(([mode, value]) => {
          if (typeof value === 'object' && value.type === 'VARIABLE_ALIAS') {
            console.log(`      - ${alias.name} (${mode}) → references variable ID: ${value.id}`);
          }
        });
      });
    }
  });

  // Map alias connections
  console.log("\n" + "=".repeat(60));
  console.log("ALIAS CONNECTIONS (Brand → Alias → Mapped)");
  console.log("=".repeat(60) + "\n");

  // Create a map of variable ID to variable name
  const varIdToName = {};
  Object.entries(variables).forEach(([id, variable]) => {
    varIdToName[id] = variable.name;
  });

  // Find all alias connections
  Object.values(variables).forEach(variable => {
    Object.entries(variable.valuesByMode || {}).forEach(([mode, value]) => {
      if (typeof value === 'object' && value.type === 'VARIABLE_ALIAS') {
        const referencedVar = variables[value.id];
        if (referencedVar) {
          const collectionName = variableCollections[variable.variableCollectionId]?.name || 'Unknown';
          const refCollectionName = variableCollections[referencedVar.variableCollectionId]?.name || 'Unknown';
          console.log(`${collectionName}::${variable.name} → ${refCollectionName}::${referencedVar.name}`);
        }
      }
    });
  });
}

function analyzePublishedStructure(data) {
  console.log("\n" + "=".repeat(60));
  console.log("PUBLISHED VARIABLES ANALYSIS");
  console.log("=".repeat(60) + "\n");

  if (!data.meta || !data.meta.variables) {
    console.log("No published variables found");
    return;
  }

  const { variables, variableCollections } = data.meta;
  console.log(`Collections: ${Object.keys(variableCollections).length}`);
  console.log(`Variables: ${Object.keys(variables).length}\n`);

  Object.entries(variableCollections).forEach(([collectionId, collection]) => {
    console.log(`📦 ${collection.name}`);
    const collectionVars = Object.values(variables).filter(
      v => v.variableCollectionId === collectionId
    );
    console.log(`   Variables: ${collectionVars.length}`);
  });
}

// Run
fetchVariables();
