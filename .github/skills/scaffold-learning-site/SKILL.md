# Skill: scaffold-learning-site

**Purpose:** Scaffold a complete MkDocs Material learning tutorial project from scratch for any technical topic — structured progressively from basics to expert level, with hover glossary, Mermaid diagrams, math rendering, dark/light mode, and interview Q&A blocks.

**Use this skill when the user says things like:**
- "Create a learning site for..."
- "Scaffold a tutorial project covering..."
- "Build a mkdocs site that teaches..."
- "I want to learn X from basics, create a site"

---

## What This Skill Produces

For any topic domain (e.g., RAG Search, Databases, Kubernetes, ML Fundamentals):

```
<project-name>/
├── mkdocs.yml                     ← Configured for Material theme
├── requirements.txt               ← All dependencies
├── README.md                      ← Project overview
├── docs/
│   ├── index.md                   ← Home/landing page
│   ├── _abbreviations.md          ← Hover glossary (30+ terms)
│   ├── GETTING_STARTED.md         ← Prerequisites & reading guide
│   ├── css/
│   │   └── extra.css              ← Custom styling
│   ├── js/
│   │   ├── mathjax.js             ← Math config
│   │   ├── mermaid-init.js        ← Diagram renderer
│   │   └── theme-toggle.js        ← Persists dark/light preference
│   ├── fundamentals/              ← Section 01: basics
│   │   └── 01-core-concepts.md
│   ├── intermediate/              ← Section 02: applied concepts
│   │   └── 01-working-together.md
│   ├── advanced/                  ← Section 03: expert topics
│   │   └── 01-advanced-patterns.md
│   └── reference/                 ← Quick reference cards
│       └── 01-cheatsheet.md
└── site/                          ← Generated output (gitignored)
```

---

## Customization Variables

When invoking, replace these tokens with the actual domain:

| Token | Example (RAG) | Example (Databases) |
|---|---|---|
| `{TOPIC}` | RAG Search & Vector Databases | Database Engineering |
| `{SLUG}` | `rag-learning` | `db-learning` |
| `{CORE_TERMS}` | embedding, cosine similarity, vector | ACID, normalization, sharding |
| `{SECTION_01}` | Foundations of Search | Database Fundamentals |
| `{SECTION_02}` | Vector Search & Retrieval | Scaling Strategies |
| `{SECTION_03}` | Production RAG Patterns | Expert & Cloud Patterns |

---

## Reference Templates

See:
- [`templates/mkdocs.yml.template`](templates/mkdocs.yml.template)
- [`templates/index.md.template`](templates/index.md.template)
- [`templates/section-summary.md.template`](templates/section-summary.md.template)
- [`templates/deep-dive.md.template`](templates/deep-dive.md.template)
- [`templates/abbreviations.md.template`](templates/abbreviations.md.template)
- [`templates/extra.css.template`](templates/extra.css.template)
- [`templates/mermaid-init.js.template`](templates/mermaid-init.js.template)
- [`templates/mathjax.js.template`](templates/mathjax.js.template)

