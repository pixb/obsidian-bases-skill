---
name: obsidian-bases-skill
description: Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries for database-like views of notes.
license: MIT
author: Pix
version: 1.0.0
created: 2024-09-20
last_reviewed: 2024-09-20
dependencies: []
---

# /obsidian-bases-skill

Create and edit valid Obsidian Bases (`.base` files) with views, filters, formulas, and summaries for database-like views of notes.

## Trigger Examples

- "Create a base file for my tasks"
- "Make a table view of my notes"
- "Add filters to my base"
- "Create a reading list base"
- "Edit my base file"
- "Show me all important notes in a card view"

## When to Use

Activate this skill when:
- User asks to create or edit `.base` files
- User mentions "Bases", "base files", "database views", "table views", "card views"
- User wants to filter, sort, or group notes by properties
- User needs to create formulas for computed values
- User wants to display notes in table, card, list, or map formats
- User mentions "Obsidian database" or "dynamic views"

## Key Concepts

- **Views**: table, cards, list, map - how notes are displayed
- **Filters**: global and per-view filtering with and/or/not logic
- **Formulas**: computed values using built-in functions
- **Properties**: note properties, file metadata, formula results

## Quick Start

```yaml
# Basic structure
filters:
  and:
    - file.hasTag("task")

views:
  - type: table
    name: "My Tasks"
    order:
      - file.name
      - status
```

## References

- [Schema Reference](references/schema.md) - Complete YAML schema
- [Functions Reference](references/functions.md) - All available functions
- [Examples](references/examples.md) - Real-world examples

## Gotchas

- Formulas use single quotes when containing double quotes: `'if(done, "Yes", "No")'`
- Date arithmetic uses milliseconds for day calculations: `86400000`
- The `this` keyword refers to different things based on context (base file, embedding file, or active file)
- Map view requires the Maps community plugin and latitude/longitude properties
- Filter operators are case-sensitive
- Summary functions require numeric data for mathematical operations
- Property names with dots need quotes in formulas: `formula.my_formula`
- Global filters apply to ALL views; view-specific filters apply only to that view