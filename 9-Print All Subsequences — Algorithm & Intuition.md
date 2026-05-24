## Print All Subsequences — Algorithm & Intuition

**Problem:** Print every possible subsequence of an array (including empty). A subsequence preserves relative order but elements need not be contiguous.

```
arr = [1, 2, 3]
→ [], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]   (8 subsequences)
```

---

### Intuition

**The Dream:** Enumerate every possible inclusion/exclusion of every element.

**Key Insight:** For each element, you make a binary choice — **include it or skip it**. This creates a binary tree of decisions. Every path from root to a leaf is one subsequence.

```
At index i:
  INCLUDE arr[i] → add to result, recurse on i+1
  EXCLUDE arr[i] → don't add, recurse on i+1
```

---

### The Recursion Tree — `[1, 2, 3]`

```
                     dfs(i=0, [])
                    /              \
           include 1              skip 1
          dfs(1, [1])            dfs(1, [])
          /        \            /         \
      inc 2       skip 2    inc 2        skip 2
    dfs(2,[1,2]) dfs(2,[1]) dfs(2,[2]) dfs(2,[])
    /    \       /    \      /    \      /    \
  +3   skip  +3   skip  +3  skip  +3  skip
 [1,2,3][1,2][1,3] [1] [2,3] [2]  [3]  []
```

2^3 = 8 leaves = 8 subsequences ✅

---

### Approach 1 — In-place with Backtrack

```
def print_subsequences(arr, i, result):
    if i == len(arr):
        print(result)         ← base: index exhausted, print what we have
        return

    result.append(arr[i])               ← INCLUDE
    print_subsequences(arr, i+1, result)

    result.pop()                         ← BACKTRACK (undo include)
    print_subsequences(arr, i+1, result) ← EXCLUDE
```

The `result.pop()` is the **backtracking step** — it undoes the choice before exploring the other branch. Without it, `result` carries stale elements into the exclude branch.

---

### Approach 2 — Immutable (No Backtrack Needed)

```
def print_subsequences_ii(arr, i, result):
    if i == len(arr):
        print(result)
        return

    print_subsequences(arr, i+1, result + [arr[i]])  ← INCLUDE: new list
    print_subsequences(arr, i+1, result)              ← EXCLUDE: unchanged
```

`result + [arr[i]]` creates a **new list** — no mutation, no backtracking required. Cleaner code, but O(N) extra allocation per call.

---

### Backtrack vs Immutable — The Tradeoff

```
Backtrack (append/pop):
  One shared list → O(1) per operation
  Must undo every change → easy to forget pop → bugs
  Preferred when result list is large

Immutable (+ operator):
  New list per call → O(N) allocation per call
  Naturally safe — nothing to undo
  Cleaner code for small problems
```

---

### Why 2^N Subsequences?

```
Each of N elements has 2 choices: include or exclude.
Total = 2 × 2 × ... × 2 (N times) = 2^N
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N × N) — 2^N subsequences, each up to length N to print |
| Space | O(N) — call stack depth + result list |