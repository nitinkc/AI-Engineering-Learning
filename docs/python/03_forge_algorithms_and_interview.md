# 🐍 Python Boot Camp — Part 3: The Forge
### Big-O Analysis, Solving Problems 3 Ways & Interview Performance

> **Goal:** Apply everything under pressure. Know not just *what* your code does, but *why* it's the right tool and how it scales.

---

## 1. Big-O — The Language of Scale

After every solution you write, you must be able to immediately say its time and space complexity. This is non-negotiable for a Forward Deployed Engineer role.

### The Essential Complexity Ladder

```
O(1)       — Constant   — dict/set lookup, list index access
O(log N)   — Log        — binary search, balanced BST operations
O(N)       — Linear     — single loop over input
O(N log N) — Linearithmic — sorting (Python's sort, merge sort)
O(N²)      — Quadratic  — nested loops — always try to eliminate
O(2^N)     — Exponential — recursive subsets — only for tiny N
```

### Recognizing complexity from code shape

```python
data = list(range(1000))

# O(1) — no loop, no recursion
def get_first(lst):
    return lst[0]

# O(N) — one loop
def find_max(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

# O(N²) — nested loops over same data — RED FLAG in interviews
def has_duplicate_slow(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):  # inner loop = O(N) per outer step
            if lst[i] == lst[j]:
                return True
    return False

# O(N) — same result, no nested loop
def has_duplicate_fast(lst):
    return len(lst) != len(set(lst))  # set construction is O(N), lookup O(1)
```

---

## 2. The Three-Solution Framework

Practice *every* problem this way. It trains you to think in optimization levels.

### Problem: Two Sum
> Given a list of integers and a target, return the indices of two numbers that add up to the target.

---

### Solution 1: Brute Force — O(N²) time, O(1) space

```python
def two_sum_brute(nums, target):
    """
    Check every pair. Simple but slow.
    Time: O(N²) — nested loops
    Space: O(1) — no extra data structures
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum_brute([2, 7, 11, 15], 9))  # [0, 1]
```

**When to mention this:** "Here's the naive O(N²) approach — it works but won't scale. Let me show you the better version."

---

### Solution 2: Optimized — O(N) time, O(N) space

```python
def two_sum_optimal(nums, target):
    """
    Use a hash map to find complements in one pass.
    Time: O(N) — single loop
    Space: O(N) — hash map stores up to N entries

    Key insight: for each num, check if (target - num) is already seen.
    """
    seen = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:          # O(1) dict lookup
            return [seen[complement], i]
        seen[num] = i

    return []

print(two_sum_optimal([2, 7, 11, 15], 9))  # [0, 1]
```

> **Interview line:** *"By trading O(N) space for a hash map, I eliminate the inner loop entirely — time drops from O(N²) to O(N). For large inputs, that's the difference between seconds and milliseconds."*

---

### Solution 3: Most Pythonic — Same complexity, idiomatic style

```python
def two_sum_pythonic(nums, target):
    """
    Same O(N) time/space, but using Python idioms clearly.
    enumerate + dict comprehension sensibility.
    """
    index_map = {num: i for i, num in enumerate(nums)}

    for i, num in enumerate(nums):
        complement = target - num
        j = index_map.get(complement)
        if j is not None and j != i:    # guard against using same element twice
            return [i, j]

    return []

print(two_sum_pythonic([2, 7, 11, 15], 9))  # [0, 1]
```

---

### Problem: Find All Palindromes in a List of Strings

```python
words = ["racecar", "hello", "level", "world", "civic", "python"]

# Solution 1 — Brute force (manual character comparison)
def is_palindrome_manual(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True

palindromes_v1 = [w for w in words if is_palindrome_manual(w)]

# Solution 2 — Optimized (slicing)
def is_palindrome(s):
    return s == s[::-1]   # O(N) time but idiomatic and clean

palindromes_v2 = [w for w in words if is_palindrome(w)]

# Solution 3 — Most Pythonic (one-liner with filter)
palindromes_v3 = list(filter(lambda w: w == w[::-1], words))

print(palindromes_v3)  # ['racecar', 'level', 'civic']
```

> All three are O(N·M) where N is list length and M is average word length. The difference is readability and conciseness — in Python, the idiomatic version is preferred unless there's a performance reason otherwise.

---

## 3. The "Walkthrough" Habit

Never stare silently. Talk through your logic like this before touching the keyboard:

```
"Okay, I'm given a list of N integers. I need to find X.

My first instinct is a nested loop — that's O(N²), which works for small
inputs but doesn't scale. Let me think about what data structure would help...

If I use a hash map to store {value: index} as I iterate, I can check for
the complement in O(1) instead of scanning the rest of the list. That brings
me down to O(N) time with O(N) space trade-off. For this problem, that's worth it.

Let me code that up..."
```

This is what separates elite candidates. The interviewer is evaluating your *thinking process*, not just whether you arrive at the answer.

---

## 4. Code Review Mindset — Talking About Your Own Code

After solving, practice saying this out loud:

```python
def process_orders(orders):
    """
    Find orders above threshold and return sorted by value.
    """
    THRESHOLD = 100
    filtered = [o for o in orders if o["value"] > THRESHOLD]   # O(N)
    return sorted(filtered, key=lambda o: o["value"], reverse=True)  # O(K log K)
```

**What to say:**
> *"This is O(N) for the filter pass plus O(K log K) for sorting, where K is the number of orders above the threshold — K ≤ N. So overall O(N log N) worst case. Space is O(K) for the filtered list. If orders were already sorted by value, we could binary search for the threshold cutoff and skip the sort entirely."*

That last sentence — offering an optimization you didn't implement — is what makes interviewers light up.

---

## 5. The Scenario Table — Memorize These Pivots

| Situation | What NOT to say | What to say |
|-----------|----------------|-------------|
| Explaining your solution | "I used a for loop to go through each item" | "I used a hash map for O(1) lookups, bringing the overall complexity to O(N)" |
| Getting stuck | Silence / random guessing | "I see a potential bottleneck here with the linear scan — let me think if a set would help..." |
| After it works | "It works!" | "This is O(N) time and O(N) space. If memory is constrained, I could use a two-pointer approach to get down to O(1) space." |
| Offered a follow-up | "I don't know" | "My first thought is X, but I'd want to benchmark it — the trade-off is Y vs Z." |

---

## 6. Quick Reference: Common Patterns and Their Complexities

```python
# Two pointers — O(N) time, O(1) space
def is_palindrome_two_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Sliding window — O(N) time, O(K) space
def max_sum_subarray(nums, k):
    """Sum of max contiguous subarray of size k."""
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # slide: add new, remove old
        max_sum = max(max_sum, window_sum)
    return max_sum

# Binary search — O(log N) time, O(1) space
def binary_search(sorted_list, target):
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# BFS / level-order traversal — O(N) time, O(N) space
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()      # O(1) — deque not list
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order
```

---

## ✅ Phase 3 Checklist

- [ ] Can state Big-O for any code you write without being prompted
- [ ] Can solve a problem 3 ways: brute → optimal → idiomatic
- [ ] Practice talking through your logic *before* typing
- [ ] Know: two pointers, sliding window, hash map, binary search patterns
- [ ] Can propose a follow-up optimization even after arriving at a good solution

---

## 🎯 Day-Of Reminders

1. **Think out loud.** Silence is the enemy — even "let me think about this for a second" is better than nothing.
2. **Name your complexity unprompted.** Don't wait to be asked — say it after every solution.
3. **Offer the trade-off.** "This uses O(N) space, which is fine for typical inputs — if memory were critical, here's how I'd approach it differently."
4. **Pythonic > verbose.** A comprehension or generator signals fluency. A `for` loop with `append` signals competence. Know when to use each.
5. **It's okay to iterate.** "Here's a working O(N²) solution — let me refine it" is a completely valid interview strategy.

---

*Good luck. You've got this. 🚀*
