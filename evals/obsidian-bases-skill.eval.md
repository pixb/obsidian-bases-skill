# obsidian-bases-skill Evaluation

## Binary Checks

1. **Valid YAML**: Generated `.base` files parse without errors
2. **Schema Compliance**: Contains required sections (filters, views)
3. **Filter Syntax**: Filters use correct operators and logic
4. **Formula Syntax**: Formulas use correct function signatures
5. **View Configuration**: View types are valid (table, cards, list, map)
6. **Property References**: Property names match existing note properties

## Golden Cases

### Case 1: Basic Task Tracker

**Input**: "Create a base to track my tasks with due dates and priorities"

**Expected Output**:
- Filters by task tag
- Table view with status, priority, due date columns
- Formula for days until due
- Proper YAML structure

### Case 2: Reading List with Cards

**Input**: "Make a reading list view for my books and articles"

**Expected Output**:
- Filters by book or article tags
- Cards view with cover, title, author
- Formula for reading time estimate
- Status filtering capability

### Case 3: Project Dashboard

**Input**: "Create a project dashboard showing all my projects with status and last updated"

**Expected Output**:
- Filters by Projects folder
- Table view with status, last updated, link count
- Grouping by status
- Summary formulas for aggregations

### Case 4: Daily Notes Index

**Input**: "Index my daily notes with word count estimates"

**Expected Output**:
- Filters by Daily Notes folder
- Date pattern matching
- Word count estimation formula
- Recent notes limit

### Case 5: Complex Filtered View

**Input**: "Show me all important notes that are either tasks or projects, but not archived"

**Expected Output**:
- Complex filter logic (AND/OR/NOT)
- Multiple tag conditions
- Proper nesting of filter conditions

## Evaluation Criteria

- **Accuracy**: Does the output match the user's requirements?
- **Completeness**: Are all requested features included?
- **Validity**: Is the YAML structure correct?
- **Usability**: Can the user immediately use the generated base?
- **Error Handling**: Are common pitfalls avoided?

## Scoring

- **Pass**: All binary checks pass and at least 4/5 golden cases match
- **Partial Pass**: All binary checks pass but 2-3 golden cases match
- **Fail**: Any binary check fails or fewer than 2 golden cases match