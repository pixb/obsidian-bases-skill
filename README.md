# obsidian-bases-skill

Create and edit valid Obsidian Bases (`.base` files) with views, filters, formulas, and summaries for database-like views of notes.

## Installation

### Claude Code

```bash
# Clone or copy to Claude Code skills directory
cp -r obsidian-bases-skill ~/.claude/skills/
```

### Cursor

```bash
# Copy to Cursor skills directory
cp -r obsidian-bases-skill ~/.cursor/skills/
```

### Windsurf

```bash
# Copy to Windsurf skills directory
cp -r obsidian-bases-skill ~/.windsurf/skills/
```

### Copilot

```bash
# Copy to Copilot skills directory
cp -r obsidian-bases-skill ~/.copilot/skills/
```

### Manual Installation

1. Copy the `obsidian-bases-skill` directory to your agent's skills directory
2. Ensure the directory structure is preserved:
   ```
   obsidian-bases-skill/
   ├── SKILL.md
   ├── AGENTS.md
   ├── README.md
   ├── discovery.json
   └── references/
       ├── schema.md
       ├── functions.md
       └── examples.md
   ```

## Usage

Invoke the skill with natural language:

- "Create a base file for my tasks"
- "Make a table view of my notes"
- "Add filters to my base"
- "Create a reading list base"
- "Edit my base file"

## Features

- Create `.base` files with valid YAML structure
- Define views (table, cards, list, map) for displaying notes
- Set up global and per-view filters with and/or/not logic
- Create formulas for computed values using built-in functions
- Configure property display names and settings
- Add summary formulas for aggregations

## References

- [Schema Reference](references/schema.md) - Complete YAML schema
- [Functions Reference](references/functions.md) - All available functions
- [Examples](references/examples.md) - Real-world examples

## License

MIT