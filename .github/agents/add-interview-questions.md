---
name: add-interview-questions
description: "Generate a set of interview Q&A questions for any technical topic"
temperature: 0.7
context_limit: 10000
---

# Add Interview Questions

Generate realistic interview questions and model answers for any technical topic in this learning guide.

## Invoke This Agent With

```
/add-interview-questions
Topic: [Your Topic]
Level: [Fundamentals|Intermediate|Advanced]
Count: [Number of questions, default 5]
```

**Example:**
```
/add-interview-questions
Topic: Microservices Architecture
Level: Intermediate
Count: 5
```

## Output

A list of interview questions in `??? question` syntax, ready to paste into an article:

```markdown
??? question "Q: What is [concept]?"
    **Model Answer:** [Clear answer]
    
    **Why this matters:** [Interview context]
```

---

## Format

Each question should:
- Be realistic (likely to appear in technical interviews)
- Have a concise, accurate model answer
- Explain why the interviewer asks it
- Connect to the article's content

---

## Guidelines

- 3–4 sentence answers (not essays)
- Avoid jargon or explain it
- Include numbers/metrics where relevant
- Consider follow-up questions
- Balance breadth and depth

---

## You're Done When

The returned questions:
1. Can be copy/pasted into an article
2. Use proper `??? question` syntax
3. Include 3–5 questions (or as specified)
4. Have complete, professional answers
5. Are domain-specific and realistic
