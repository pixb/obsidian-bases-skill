# obsidian-bases-skill

Create and edit valid Obsidian Bases (`.base` files) with views, filters, formulas, and summaries for database-like views of notes.

## Activation

Invoke with `/obsidian-bases-skill` or naturally:

- "Create a base file for my tasks"
- "Make a table view of my notes"
- "Add filters to my base"
- "Create a reading list base"
- "Edit my base file"

## How to use this file

This is the cross-tool companion file (AAIF format). The full instructions live in [SKILL.md](SKILL.md). Read SKILL.md and follow it; treat this file as the pointer, not the instructions.

## What this skill does

This skill enables agents to:
- Create `.base` files with valid YAML structure
- Define views (table, cards, list, map) for displaying notes
- Set up global and per-view filters with and/or/not logic
- Create formulas for computed values using built-in functions
- Configure property display names and settings
- Add summary formulas for aggregations
- Embed bases in Markdown files

## File format

Obsidian Bases use `.base` extension with YAML content:

```yaml
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

## Key concepts

**Views**: table, cards, list, map - how notes are displayed

**Filters**: 
- Global: apply to all views
- Per-view: apply only to specific views
- Logic: and/or/not with nesting

**Formulas**: computed values using functions
- Date arithmetic
- String manipulation
- Conditional logic
- List operations

**Properties**:
- Note properties: from frontmatter
- File properties: file.name, file.mtime, etc.
- Formula properties: computed values

## Common patterns

### Filter by tag
```yaml
filters:
  and:
    - file.hasTag("project")
```

### Filter by folder
```yaml
filters:
  and:
    - file.inFolder("Notes")
```

### Filter by date range
```yaml
filters:
  and:
    - 'file.mtime > now() - "7d"'
```

### Conditional formulas
```yaml
formulas:
  status_icon: 'if(status == "done", "✅", "⏳")'
```

### Date formatting
```yaml
formulas:
  created: 'file.ctime.format("YYYY-MM-DD")'
```

## References

- [Schema Reference](references/schema.md) - Complete YAML schema
- [Functions Reference](references/functions.md) - All available functions
- [Examples](references/examples.md) - Real-world examples

## Platform compatibility

This skill works with:
- Claude Code
- Cursor
- Windsurf
- Copilot
- Any tool that reads SKILL.md and AGENTS.md

## Gotchas

- Formulas use single quotes when containing double quotes
- Date arithmetic uses milliseconds for day calculations (86400000)
- The `this` keyword refers to different things based on context
- Map view requires the Maps community plugin
- Filter operators are case-sensitive
- Property names with dots need quotes in formulas