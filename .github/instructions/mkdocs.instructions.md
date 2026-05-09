---
description: 'Auto-applied rules and solutions for MkDocs Material documentation projects'
applyTo: 'docs/**/*.md, mkdocs.yml'
---

# MkDocs Documentation Standards

These rules apply automatically whenever you edit `docs/**/*.md` or `mkdocs.yml`.

---

## Project Structure

```
project-name/
├── mkdocs.yml                    ← Master configuration
├── requirements.txt              ← Python dependencies
├── docs/
│   ├── index.md                  ← Home page
│   ├── _abbreviations.md         ← Shared glossary definitions
│   ├── css/
│   │   └── extra.css             ← Custom styling
│   ├── js/
│   │   ├── mathjax.js            ← Math config (must load BEFORE library)
│   │   ├── mermaid-init.js       ← Diagram renderer
│   │   └── theme-toggle.js       ← Persists dark/light preference
│   └── [section-folders]/
│       └── *.md files
└── site/                         ← Generated output (do not edit)
```

---

## Markdown Style Rules

- **Always add a blank line before lists** — parsers require it
- **Use 2-space indentation**, never tabs
- **Tables** are the primary structure for comparisons and reference material
- **No pipes `|`** in Mermaid node labels — use `·` instead
- **End every article** with `--8<-- "_abbreviations.md"`
- **Collapsible sections**: use `??? note "Title"` (Material admonitions) not raw `<details>` tags

### Article Templates

**Summary / Section index** (`NN-section.md`):
- Breadth-first, table-heavy, acts as entry point
- Contains `→ Deep Dive` links to child articles

**Deep-dive topic** (`NN.XX-topic.md`):
```markdown
# Topic Name — Deep Dive

> **Level:** Intermediate | Advanced
> **Pre-reading:** [NN · Parent](NN-section.md) · [NN.XX · Related](NN.XX-related.md)

---

## Section ...

---

??? question "Interview question?"
    Answer in 2–4 lines.

--8<-- "_abbreviations.md"
```

- Must include ≥1 Mermaid diagram
- Must include 2–3 interview Q&A blocks (`??? question`)
- Must end with abbreviations snippet

---

## mkdocs.yml Rules

- **Do not remove or override the `palette` toggle** — light/dark mode must remain
- Palette uses `scheme: default` (light) and `scheme: slate` (dark), both with `primary: teal` and `accent: blue`
- Add new pages under `nav:` in logical order with descriptive, capitalized titles
- Indent sub-articles under their parent section:

```yaml
nav:
  - Home: index.md
  - 01 · Foundations: 01-foundations.md
    - How It Works: 01.01-how-it-works.md
    - Deep Dive: 01.02-deep-dive.md
```

---

## Known Issues & Fixes

### Lists not rendering
Add a blank line before any list — always.

### Mermaid diagrams not rendering
Use client-side JS rendering. `mermaid-init.js` must be loaded **after** the mermaid CDN script in `extra_javascript`:
```yaml
extra_javascript:
  - https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js
  - js/mermaid-init.js
```

### Math equations not rendering
Load config file **before** the MathJax library:
```yaml
extra_javascript:
  - js/mathjax.js                # Config FIRST
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js  # Library SECOND
```

### Abbreviations not showing
- Ensure `docs/_abbreviations.md` exists with `*[TERM]: Definition` syntax
- Ensure `mkdocs.yml` has both `abbr` and `pymdownx.snippets` in `markdown_extensions`
- Include `--8<-- "_abbreviations.md"` at the bottom of every file

### Collapsible sections not styled
Add to `docs/css/extra.css` — see `details` and `details summary` rules including `[data-md-color-scheme="slate"]` overrides for dark mode.

---

## Essential Dependencies (requirements.txt)

```
mkdocs>=1.5.0
mkdocs-material>=9.5.0
pymdown-extensions>=10.8
Markdown>=3.6
```

---

## Build Commands

```bash
mkdocs serve          # Local dev at http://localhost:8000
mkdocs build          # Build static site → site/
```

---

## Abbreviations File Format (`_abbreviations.md`)

```markdown
*[API]: Application Programming Interface
*[RAG]: Retrieval-Augmented Generation
*[LLM]: Large Language Model
```

Include in each article:
```markdown
--8<-- "_abbreviations.md"
```

