---
name: obsidian-bases-skill
description: Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating database-like views of notes, or when the user mentions Bases, table views, card views, filters, or formulas in Obsidian.
activation: /obsidian-bases-skill
license: MIT
metadata:
  created: 2024-09-20
  last_reviewed: 2024-09-20
  review_interval_days: 90
  version: 1.0.0
  author: "Pix"
  dependencies: []
provenance:
  maintainer: "Pix"
  source_references:
    - "https://help.obsidian.md/bases/syntax"
    - "https://help.obsidian.md/bases/functions"
    - "https://help.obsidian.md/bases/views"
---

# Obsidian Bases Skill

Create and edit valid Obsidian Bases (`.base` files) with views, filters, formulas, and summaries for database-like views of notes.

## When to Use

Activate this skill when:
- User asks to create or edit `.base` files
- User mentions "Bases", "base files", "database views", "table views", "card views"
- User wants to filter, sort, or group notes by properties
- User needs to create formulas for computed values
- User wants to display notes in table, card, list, or map formats
- User mentions "Obsidian database" or "dynamic views"

## Data Source

This skill works with local Obsidian vault files. No external APIs required.

**File format**: YAML-based `.base` files in Obsidian vaults

**Key concepts**:
- Views: table, cards, list, map
- Filters: global and per-view filtering with and/or/not logic
- Formulas: computed values using built-in functions
- Properties: note properties, file metadata, formula results

## Workflows

### Workflow 1: Create a Simple Table View

1. **Identify user requirements**
   - What notes to include (tags, folders, properties)
   - What columns to display
   - Sorting and grouping needs

2. **Create base file structure**
   ```yaml
   # Example: Task tracker
   filters:
     and:
       - file.hasTag("task")
       - 'file.ext == "md"'
   
   views:
     - type: table
       name: "Tasks"
       order:
         - file.name
         - status
         - priority
   ```

3. **Add formulas if needed**
   ```yaml
   formulas:
     days_until_due: 'if(due, ((date(due) - today()) / 86400000).round(0), "")'
   ```

4. **Configure property display**
   ```yaml
   properties:
     status:
       displayName: "Status"
     formula.days_until_due:
       displayName: "Days Left"
   ```

5. **Save as `.base` file**

### Workflow 2: Create Filtered Views

1. **Define filter criteria**
   ```yaml
   filters:
     or:
       - file.hasTag("book")
       - file.hasTag("article")
   ```

2. **Add view-specific filters**
   ```yaml
   views:
     - type: table
       name: "Reading List"
       filters:
         and:
           - 'status == "to-read"'
   ```

### Workflow 3: Add Formulas and Summaries

1. **Define formulas**
   ```yaml
   formulas:
     reading_time: 'if(pages, (pages * 2).toString() + " min", "")'
   ```

2. **Add summary formulas**
   ```yaml
   summaries:
     avgPages: 'values.filter(value.isType("number")).mean().round(1)'
   ```

3. **Map properties to summaries**
   ```yaml
   views:
     - type: table
       summaries:
         pages: avgPages
   ```

## Schema Reference

For complete schema documentation, see [references/schema.md](references/schema.md).

## Functions Reference

For complete function documentation, see [references/functions.md](references/functions.md).

## Examples

For complete examples, see [references/examples.md](references/examples.md).

## Errors

### Common Issues

1. **Invalid YAML syntax**
   - Check indentation (use spaces, not tabs)
   - Verify quotes are properly matched
   - Validate with YAML linter

2. **Filter not working**
   - Verify property names exist in notes
   - Check filter syntax (single vs double quotes)
   - Test with simpler filter first

3. **Formulas not computing**
   - Check function syntax
   - Verify property references
   - Test with known values

4. **Views not displaying**
   - Verify view type is valid (table, cards, list, map)
   - Check order array contains valid properties
   - Ensure filters return results

## Validations

### Before Saving

1. **YAML validation**
   ```bash
   python -c "import yaml; yaml.safe_load(open('file.base'))"
   ```

2. **Schema validation**
   - Verify required sections present
   - Check property types match
   - Validate view configurations

3. **Content validation**
   - Test filters with sample data
   - Verify formulas compute correctly
   - Check summary functions work

## Gotchas

- Formulas use single quotes when containing double quotes: `'if(done, "Yes", "No")'`
- Date arithmetic uses milliseconds for day calculations: `86400000`
- The `this` keyword refers to different things based on context (base file, embedding file, or active file)
- Map view requires the Maps community plugin and latitude/longitude properties
- Filter operators are case-sensitive
- Summary functions require numeric data for mathematical operations
- Property names with dots need quotes in formulas: `formula.my_formula`
- Global filters apply to ALL views; view-specific filters apply only to that view

## Keywords

obsidian, bases, base files, database views, table views, card views, list views, map views, filters, formulas, summaries, properties, grouping, sorting, dynamic views, note organization, metadata, frontmatter, file properties, computed values

## Complete Examples

### Example 1: Task Tracker

**User request**: "Create a base to track my tasks with due dates and priorities"

**Generated base**:
```yaml
filters:
  and:
    - file.hasTag("task")
    - 'file.ext == "md"'

formulas:
  days_until_due: 'if(due, ((date(due) - today()) / 86400000).round(0), "")'
  is_overdue: 'if(due, date(due) < today() && status != "done", false)'
  priority_label: 'if(priority == 1, "🔴 High", if(priority == 2, "🟡 Medium", "🟢 Low"))'

properties:
  status:
    displayName: Status
  formula.days_until_due:
    displayName: "Days Until Due"
  formula.priority_label:
    displayName: Priority

views:
  - type: table
    name: "Active Tasks"
    filters:
      and:
        - 'status != "done"'
    order:
      - file.name
      - status
      - formula.priority_label
      - due
      - formula.days_until_due
    groupBy:
      property: status
      direction: ASC
```

### Example 2: Reading List

**User request**: "Make a base to track my reading list with books and articles"

**Generated base**:
```yaml
filters:
  or:
    - file.hasTag("book")
    - file.hasTag("article")

formulas:
  reading_time: 'if(pages, (pages * 2).toString() + " min", "")'
  status_icon: 'if(status == "reading", "📖", if(status == "done", "✅", "📚"))'

properties:
  author:
    displayName: Author
  formula.status_icon:
    displayName: ""
  formula.reading_time:
    displayName: "Est. Time"

views:
  - type: cards
    name: "Library"
    order:
      - cover
      - file.name
      - author
      - formula.status_icon

  - type: table
    name: "Reading List"
    filters:
      and:
        - 'status == "to-read"'
    order:
      - file.name
      - author
      - pages
      - formula.reading_time
```

### Example 3: Project Dashboard

**User request**: "Create a project dashboard showing all my projects with status and last updated"

**Generated base**:
```yaml
filters:
  and:
    - file.inFolder("Projects")
    - 'file.ext == "md"'

formulas:
  last_updated: 'file.mtime.relative()'
  link_count: 'file.links.length'

properties:
  formula.last_updated:
    displayName: "Updated"
  formula.link_count:
    displayName: "Links"

views:
  - type: table
    name: "All Projects"
    order:
      - file.name
      - status
      - formula.last_updated
      - formula.link_count
    groupBy:
      property: status
      direction: ASC
```

### Example 4: Daily Notes Index

**User request**: "Index my daily notes with word count estimates"

**Generated base**:
```yaml
filters:
  and:
    - file.inFolder("Daily Notes")
    - '/^\d{4}-\d{2}-\d{2}$/.matches(file.basename)'

formulas:
  word_estimate: '(file.size / 5).round(0)'
  day_of_week: 'date(file.basename).format("dddd")'

properties:
  formula.day_of_week:
    displayName: "Day"
  formula.word_estimate:
    displayName: "~Words"

views:
  - type: table
    name: "Recent Notes"
    limit: 30
    order:
      - file.name
      - formula.day_of_week
      - formula.word_estimate
      - file.mtime
```

### Example 5: Complex Filtered View

**User request**: "Show me all important notes that are either tasks or projects, but not archived"

**Generated base**:
```yaml
filters:
  and:
    - file.hasTag("important")
    - or:
        - file.hasTag("task")
        - file.hasTag("project")
    - not:
        - file.hasTag("archived")

views:
  - type: table
    name: "Important Items"
    order:
      - file.name
      - file.tags
      - file.mtime
    summaries:
      file.size: Sum