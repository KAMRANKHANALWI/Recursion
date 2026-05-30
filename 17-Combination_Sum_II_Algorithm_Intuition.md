## Combination Sum II — Algorithm & Intuition

**Problem:** Given candidates (may contain duplicates), find all unique combinations that sum to target. Each number may be used **at most once**.

```
arr = [10, 1, 2, 7, 6, 1, 5],  target = 8
→ [[1,1,6], [1,2,5], [1,7], [2,6]]
```

---

### Intuition

**The Dream:** All unique combinations — no repeats in output even though input has duplicates.

**Key Insight:** Two rules work together:
1. Sort the array so duplicates are adjacent.
2. At each recursion level, skip an element if it's the same as the previous one at the same level.

```
Sorted: [1, 1, 2, 5, 6, 7, 10]

At the same level, once you've explored starting with arr[i]=1,
skip any future arr[i]=1 — it would produce the same combination.
```

---

### The For-Loop Pattern (Different from Combination Sum I)

```
def find_combination_ii(idx, target, curr):
    if target == 0:
        result.append(list(curr))   ← found a valid combination
        return

    for i in range(idx, len(arr)):
        # Skip duplicate at same recursion level
        if i > idx and arr[i] == arr[i-1]:
            continue

        # Pruning: sorted array → once arr[i] > target, break
        if arr[i] > target:
            break

        curr.append(arr[i])
        find_combination_ii(i + 1, target - arr[i], curr)  ← i+1: each used once
        curr.pop()
```

---

### The Duplicate Skip Rule — Deep Dive

```
if i > idx and arr[i] == arr[i-1]: continue

arr = [1, 1, 2, 5, 6, 7, 10]

At idx=0 (first call):
  i=0: arr[0]=1 → explore [1, ...]
  i=1: arr[1]=1, i>idx(0) AND arr[1]==arr[0] → SKIP
  i=2: arr[2]=2 → explore [2, ...]
  ...

Why skip? We already explored all combinations starting with 1
when i=0. Trying again with i=1 (another 1 at the same level)
would produce the exact same combinations → duplicates in output.
```

---

### Why `i > idx` Not Just `i > 0`?

```
arr = [1, 1, 2], target = 3

Without i > idx (wrong):
  At level 0: i=0 → explore [1, ...]
              i=1 → arr[1]==arr[0], skip ✅ (correct)
              ...

  But when recursing from [1] at idx=1:
    i=1: first element at this level (i == idx), must NOT skip
         We need to use the second 1 to form [1,1,2] → valid
    i=2: arr[2]=2 ≠ arr[1]=1 → don't skip anyway

  If we used `i > 0` instead of `i > idx`:
    i=1 at recursive level: i>0 AND arr[1]==arr[0] → skip ← WRONG!
    We'd miss [1,1,2] as a valid combination.

`i > idx` means: skip duplicates only within the same call's for-loop,
                 not across different recursion levels.
```

---

### Dry Run — `[1,1,2,5,6,7,10]`, target=8

```
Level 0 (idx=0):
  i=0: use 1 → recurse(idx=1, rem=7, [1])
    Level 1 (idx=1):
      i=1: use 1 → recurse(idx=2, rem=6, [1,1])
        Level 2 (idx=2):
          i=2: use 2 → recurse(idx=3, rem=4, [1,1,2]) → no combo sums to 4 from [5,6,7,10]
          i=3: use 5 → rem=1, no solution
          i=4: 6>4 → break
      i=2: use 2 → recurse(idx=3, rem=5, [1,2])
        i=3: use 5 → rem=0 ✅ → [1,2,5]
        i=4: 6>5 → break
      i=3: use 5 → recurse(rem=2, [1,5]) → nothing
      i=4: use 6 → recurse(rem=1, [1,6]) → nothing
      i=5: use 7 → rem=0 ✅ → [1,7]
      i=6: 10>7 → break
  i=1: arr[1]==arr[0], i>idx(0) → SKIP ←  avoids duplicate [1,...] paths
  i=2: use 2 → recurse(idx=3, rem=6, [2])
    i=4: use 6 → rem=0 ✅ → [2,6]
  i=3: use 5 → ...
  i=4: use 6 → ...
  i=5: use 7 → ...
  i=6: 10>8 → break
```

---

### Sort + Skip = No Duplicate Combinations

```
Sorted ensures duplicates are adjacent → easy to detect with arr[i]==arr[i-1]
Skip at same level ensures each VALUE starts at most once per level
Together: unique combinations guaranteed without a set/hashmap
```

---

### Combination Sum I vs II

```
Feature        | Sum I                    | Sum II
---------------|--------------------------|------------------------
Reuse          | Unlimited                | Each element once
Pivot call     | find(idx, ...)           | find(i+1, ...)
Duplicates     | Input has none           | Input may have dupes
Dup handling   | Not needed               | Sort + skip same-level dups
Pattern        | pick/not-pick (2 calls)  | for-loop over remaining
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N) worst case |
| Space | O(target) — recursion depth |
