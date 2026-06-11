# 🐍 Python Boot Camp — Part 1: The Foundation
### Mutability, Data Structures & Memory References

> **Goal:** Zero tolerance for basic errors. Instant recall of the primitives that trip people up.

---

## 1. Mutability vs. Immutability

The #1 trap in interviews. Know this cold.

| Type | Mutable? | Example |
|------|----------|---------|
| `list` | ✅ Yes | `[1, 2, 3]` |
| `dict` | ✅ Yes | `{"a": 1}` |
| `set` | ✅ Yes | `{1, 2, 3}` |
| `tuple` | ❌ No | `(1, 2, 3)` |
| `str` | ❌ No | `"hello"` |
| `int/float` | ❌ No | `42` |

### Why it matters in functions

```python
# MUTABLE: list — the original IS modified
def append_item(lst, item):
    lst.append(item)

my_list = [1, 2, 3]
append_item(my_list, 99)
print(my_list)  # [1, 2, 3, 99] — CHANGED outside the function!


# IMMUTABLE: tuple — cannot be modified in place
def try_modify_tuple(t):
    # t[0] = 99  ← this raises TypeError: 'tuple' object does not support item assignment
    t = t + (99,)  # This creates a NEW tuple — original is untouched
    return t

my_tuple = (1, 2, 3)
new_tuple = try_modify_tuple(my_tuple)
print(my_tuple)   # (1, 2, 3)    — UNCHANGED
print(new_tuple)  # (1, 2, 3, 99) — new object
```

### The "accidental shared reference" trap

```python
# WRONG: Both rows point to the same list!
grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] — all rows changed!

# CORRECT: Each row is a separate object
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] — only first row changed
```

> **Interview line:** *"I'm careful with mutable defaults and shared references — Python passes objects by reference, so modifying a list inside a function mutates the original."*

---

## 2. Mutable Default Argument — The Classic Gotcha

```python
# WRONG — the default list is shared across ALL calls
def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

print(add_to_cart("apple"))   # ['apple']
print(add_to_cart("banana"))  # ['apple', 'banana']  ← bug!


# CORRECT — use None as default, create fresh list each call
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_to_cart("apple"))   # ['apple']
print(add_to_cart("banana"))  # ['banana']  ✓
```

---

## 3. Data Structures — When to Use What

### List vs. Set vs. Dict: The Decision Matrix

```python
items = ["apple", "banana", "apple", "cherry", "banana"]

# LIST — ordered, allows duplicates, use when sequence matters
shopping_list = list(items)
print(shopping_list)  # ['apple', 'banana', 'apple', 'cherry', 'banana']

# SET — unordered, no duplicates, O(1) lookup — use for existence checks
unique_items = set(items)
print(unique_items)   # {'apple', 'banana', 'cherry'}
print("apple" in unique_items)  # True — O(1) ✓

# DICT — key-value, O(1) lookup by key — use when you need association
item_count = {}
for item in items:
    item_count[item] = item_count.get(item, 0) + 1
print(item_count)  # {'apple': 2, 'banana': 2, 'cherry': 1}
```

### Time Complexity Cheat Sheet

```python
my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}
my_dict = {"a": 1, "b": 2}

# LIST
my_list.append(6)       # O(1) average — fast
my_list.insert(0, 0)    # O(N) — shifts everything
_ = 3 in my_list        # O(N) — linear scan ← slow for large data
_ = my_list[2]          # O(1) — index access is instant

# SET
_ = 3 in my_set         # O(1) — hash lookup ← always use set for "in" checks
my_set.add(6)            # O(1)

# DICT
_ = my_dict["a"]        # O(1)
_ = "a" in my_dict      # O(1)
```

> **Interview line:** *"If I need to check membership repeatedly, I'll convert to a set first — O(N) to build, but then O(1) per lookup instead of O(N)."*

---

## 4. Variables as Labels (References)

Python variables don't *contain* values — they *point* to objects in memory.

```python
a = [1, 2, 3]
b = a           # b points to the SAME list

b.append(4)
print(a)        # [1, 2, 3, 4] — a changed too!

# To get an independent copy:
c = a.copy()        # shallow copy — one level deep
# or
import copy
d = copy.deepcopy(a)  # deep copy — safe for nested structures
```

```python
# Shallow copy limitation
original = [[1, 2], [3, 4]]
shallow = original.copy()

shallow[0].append(99)
print(original)  # [[1, 2, 99], [3, 4]] — inner list still shared!

import copy
deep = copy.deepcopy(original)
deep[0].append(100)
print(original)  # [[1, 2, 99], [3, 4]] — untouched ✓
```

---

## ✅ Phase 1 Checklist

- [ ] Can explain mutable vs. immutable without hesitation
- [ ] Know the mutable default argument bug and fix
- [ ] Know when to use list vs. set vs. dict (and why)
- [ ] Can recite: list append O(1), list search O(N), set/dict lookup O(1)
- [ ] Understand shallow vs. deep copy

---

*Next up → **Part 2: The Scalpel** — Pythonic idioms, comprehensions, generators, and context managers.*
