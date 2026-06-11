# 🐍 Python Boot Camp — Part 2: The Scalpel
### Pythonic Idioms, Comprehensions, Generators & Context Managers

> **Goal:** Move from "it works" to "it's clean, fast, and clearly written by someone who knows the language."

---

## 1. List / Dict / Set Comprehensions

The single biggest signal of Python fluency. If you're writing a `for` loop to build a list, ask yourself: can this be a comprehension?

### List Comprehension

```python
# ❌ Verbose — junior style
squares = []
for n in range(10):
    squares.append(n ** 2)

# ✅ Comprehension — Pythonic
squares = [n ** 2 for n in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# With a filter (if clause)
# ❌ Verbose
evens = []
for n in range(20):
    if n % 2 == 0:
        evens.append(n)

# ✅ Comprehension
evens = [n for n in range(20) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### Dict Comprehension

```python
names = ["alice", "bob", "charlie"]

# Build a dict mapping name → length
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'alice': 5, 'bob': 3, 'charlie': 7}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Set Comprehension

```python
words = ["apple", "banana", "avocado", "blueberry", "apricot"]

# Get unique first letters
first_letters = {word[0] for word in words}
print(first_letters)  # {'a', 'b'}  — a set, so no duplicates
```

### Nested Comprehension (Flatten a 2D list)

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ❌ Verbose
flat = []
for row in matrix:
    for val in row:
        flat.append(val)

# ✅ Comprehension
flat = [val for row in matrix for val in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> **Tip:** Nested comprehensions read left-to-right, outer loop first — same order as the nested for loops.

---

## 2. Generators — Memory-Efficient Iteration

When data is large, you don't want to build a full list in memory. Generators produce values **one at a time, on demand**.

### The `yield` keyword

```python
# This builds the ENTIRE list in memory first
def get_squares_list(n):
    return [i ** 2 for i in range(n)]

# This generates ONE value at a time — uses almost no memory
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2

# Usage looks identical from the outside
for val in get_squares_gen(1_000_000):
    print(val)  # Memory: stores only 1 value at a time
```

### Generator Expression (inline, like a comprehension)

```python
# List comprehension — stores all 1M values in RAM
squares_list = [n ** 2 for n in range(1_000_000)]

# Generator expression — uses () instead of []
squares_gen = (n ** 2 for n in range(1_000_000))

# Both work the same in a for loop or sum()
total = sum(n ** 2 for n in range(1_000_000))  # Pythonic — no intermediate list
```

### Practical example: reading a huge file

```python
# ❌ Loads entire file into RAM
def read_all(filepath):
    with open(filepath) as f:
        return f.readlines()  # entire file in memory

# ✅ Processes line by line — O(1) memory regardless of file size
def read_lines(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()

for line in read_lines("huge_log.txt"):
    process(line)
```

> **Interview line:** *"For large data pipelines, I prefer generators over lists — they're lazy, so memory usage stays constant regardless of input size."*

---

## 3. Context Managers — The `with` Statement

Any time you open a resource (file, DB connection, lock), use `with`. It guarantees cleanup even if an error occurs.

### File I/O

```python
# ❌ Manual — file leaks if an exception is raised before f.close()
f = open("data.txt", "r")
data = f.read()
f.close()

# ✅ Context manager — file is always closed, even on exception
with open("data.txt", "r") as f:
    data = f.read()
# f is closed here automatically
```

### Multiple resources at once

```python
# Read one file and write to another — both closed automatically
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

### Writing your own context manager

```python
from contextlib import contextmanager

@contextmanager
def timer(label):
    import time
    start = time.time()
    yield                          # code inside 'with' block runs here
    elapsed = time.time() - start
    print(f"{label}: {elapsed:.3f}s")

with timer("matrix multiply"):
    result = [[sum(a * b for a, b in zip(row, col))
               for col in zip(*matrix_b)]
              for row in matrix_a]
```

---

## 4. Useful Built-ins That Signal Fluency

Interviewers love to see these used naturally.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# enumerate — get index AND value (never use range(len(...)))
for i, val in enumerate(numbers):
    print(f"Index {i}: {val}")

# zip — iterate two sequences in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# sorted with key — sort by custom logic
words = ["banana", "fig", "apple", "date"]
print(sorted(words, key=len))           # ['fig', 'fig', 'date', 'apple', 'banana']
print(sorted(words, key=lambda w: w[-1]))  # sort by last letter

# any / all — readable boolean aggregation
scores = [88, 92, 71, 95]
print(all(s >= 70 for s in scores))  # True — all passing
print(any(s >= 90 for s in scores))  # True — at least one A

# collections.Counter — frequency map in one line
from collections import Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts)               # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts.most_common(2))  # [('apple', 3), ('banana', 2)]
```

---

## 5. `itertools` — Know It Exists

You don't need to memorize the whole library, but mentioning it is a green flag.

```python
import itertools

# chain — flatten iterables without building a list
combined = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(combined)  # [1, 2, 3, 4, 5, 6]

# groupby — group consecutive elements by a key
from itertools import groupby
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("c", 5)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3), ('b', 4)]
# c [('c', 5)]

# islice — take the first N items from any iterator (memory safe)
gen = (x ** 2 for x in range(1_000_000))
first_five = list(itertools.islice(gen, 5))
print(first_five)  # [0, 1, 4, 9, 16]
```

> **Interview line:** *"Before writing a custom loop, I check if `itertools` has it — it's optimized in C and handles edge cases already."*

---

## ✅ Phase 2 Checklist

- [ ] Can convert any simple `for`/`append` loop into a comprehension instantly
- [ ] Know the difference between `[...]` (list) and `(...)` (generator expression)
- [ ] Can explain *why* generators save memory (lazy evaluation, one value at a time)
- [ ] Always use `with` for file and resource handling — no exceptions
- [ ] Comfortable with `enumerate`, `zip`, `sorted(key=...)`, `any`/`all`, `Counter`
- [ ] Can name-drop `itertools` and give one example

---

*Next up → **Part 3: The Forge** — Big-O analysis, solving problems three ways, and interview performance strategy.*
