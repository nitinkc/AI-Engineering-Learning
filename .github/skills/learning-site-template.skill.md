---
name: learning-site-template-skill
description: "Skill bundle for the learning-site-template project. Contains templates and best practices for creating high-quality technical learning guides."
---

# Skill: Learning Site Template

This skill provides templates and standardized guidance for building professional, interactive technical learning sites using MkDocs Material.

## What's Included

### Project Templates
- **mkdocs.yml** — Fully configured with Material theme, Mermaid, MathJax
- **CSS** — Professional styling (abbr, diagrams, math, dark mode)
- **JavaScript** — Theme toggle, Mermaid rendering, Math execution
- **Markdown templates** — For all article types (fundamentals through advanced)

### Created Structure
```
learning-site-template/
├── mkdocs.yml
├── requirements.txt
├── README.md
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/
│   └── skills/
├── docs/
│   ├── index.md
│   ├── GETTING_STARTED.md
│   ├── _abbreviations.md
│   ├── css/extra.css
│   ├── js/ (mathjax.js, mermaid-init.js, theme-toggle.js)
│   ├── 00-introduction/
│   ├── 01-fundamentals/
│   ├── 02-intermediate/
│   ├── 03-advanced/
│   └── reference/
```

## Key Features

### 1. Professional Theme
- Material Design with blue/orange color scheme
- Automatic light/dark mode toggle
- Mobile-responsive layout
- Fast page loading & instant navigation

### 2. Rich Content Features
- ✅ Mermaid diagrams (graphs, flowcharts, mind maps)
- ✅ Math equations (KaTeX/MathJax)
- ✅ Abbreviations with hover definitions
- ✅ Collapsible Q&A blocks
- ✅ Code syntax highlighting
- ✅ Tabbed content
- ✅ Tables & comparisons

### 3. Progressive Structure
- **Fundamentals** — Beginner concepts (no prerequisites)
- **Intermediate** — Building blocks & patterns
- **Advanced** — Production patterns & optimization
- **Reference** — Quick lookup & interview prep

###4. Built-in Content Scaffolding
Agents to auto-generate:
- Complete articles from topics
- Interview Q&A blocks
- Mermaid diagram suggestions

## Best Practices Encoded

### Article Structure
Every article includes:
1. Level badge (🟢🟡🔴)
2. Pre-reading links
3. Plain-language intro
4. Main content with examples
5. Mermaid diagram(s)
6. Math with explanation (if applicable)
7. Interview Q&A blocks (2–3)
8. Abbreviations footer

### Markdown Guidelines
- Tables for comparisons (not lists)
- Blank lines before lists
- Clear hierarchies with headings
- Short, scannable paragraphs
- Links to related concepts
- Practical examples over theory

### Color Scheme (PCF Standard)
- **Primary:** Blue (#1976d2) — professional, calm
- **Accent:** Orange (#ff9800) — highlights, attention
- **Success:** Green (#2e7d32) — positive outcomes
- **Danger:** Red (#c62828) — errors, warnings

## How to Use This Template

### Quick Start
1. It's already set up — just start filling in content
2. Use the **copilot-instructions** guide for writing rules
3. Use the **agents** to scaffold articles

### Fill Content Into:
```
docs/
├── 01-fundamentals/01-core-concepts.md
├── 01-fundamentals/02-key-principles.md
├── 02-intermediate/01-building-blocks.md
├── 02-intermediate/02-practical-applications.md
├── 03-advanced/01-advanced-patterns.md
├── 03-advanced/02-production-considerations.md
└── reference/03-interview-qa.md
```

### Scaffold Articles With:
```
/fill-article-template
Topic: [Your Topic]
Section: [Fundamentals|Intermediate|Advanced]
Article Focus: [Concept to cover]
```

## Customization

### Change Colors
Edit `mkdocs.yml` theme.palette:
```yaml
primary: blue      # Change primary color
accent: orange     # Change accent color
```

### Add Custom CSS
Edit `docs/css/extra.css` — it already includes:
- Abbreviation styling
- Math block spacing
- Mermaid centering
- Table improvements
- Dark mode overrides

### Add Custom JS
Create `docs/js/custom.js` and reference in `mkdocs.yml`

## Testing & Deployment

### Local Testing
```bash
pip install -r requirements.txt
mkdocs serve
# Open http://localhost:8000
```

### Build for Deployment
```bash
mkdocs build
# Output in site/ directory
```

### Deploy Options
- GitHub Pages
- Netlify
- Vercel
- Custom hosting (upload `site/` directory)

## Included Best Practices From

This template consolidates best practices from 15+ real learning projects:
- **PCF_Learning** — Mermaid color scheme, theme toggle
- **aiDevGuide** — Math equations, executive content
- **mlDLGuide** — Advanced math, neural networks
- **Kafka-Learning** — Lab structure, practical scenarios
- **CassandraLearning** — Database concepts, consistency models
- **architectureStyle** — Abbreviations, glossary management
- And 9 more projects...

## What's NOT Included

This template is for **learning content**, not for:
- Code repositories or full projects
- API documentation (use Swagger/OpenAPI)
- Software libraries/frameworks
- Step-by-step tutorials (too prescriptive)

Use other tools for:
- API docs: Swagger/OpenAPI/Redoc
- Code tutorials: Jupyter notebooks, GitHub
- Video content: YouTube, Loom
- Interactive courses: Coursera, Udemy

## Questions?

See:
- [README.md](../../README.md) — Full overview
- [.github/copilot-instructions.md](../copilot-instructions.md) — Writing guidelines
- [docs/GETTING_STARTED.md](../../docs/GETTING_STARTED.md) — How to navigate

---

**Ready to create amazing learning content!** 🚀
