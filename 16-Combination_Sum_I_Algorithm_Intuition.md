## Combination Sum I — Algorithm & Intuition

**Problem:** Given an array of distinct candidates, find all combinations that sum to target. Each number may be used **unlimited times**.

```
arr = [2, 3, 6, 7],  target = 7
→ [[2,2,3], [7]]
```

---

### Intuition

**The Dream:** Try every possible combination — but allow repeats and avoid duplicates.

**Key Insight:** At each index, you have two choices:
- **Pick** `arr[idx]` (stay at same index — reuse allowed) and reduce target
- **Skip** `arr[idx]` (move to next index — never come back)

Staying at the same index enables unlimited reuse of the current element.

---

### The Pick/Not-Pick Pattern (Unbounded)

```
def find_combination(idx, target, curr):
    if idx == len(arr):
        if target == 0:
            result.append(list(curr))
        return

    # PICK (stay at idx — reuse current element)
    if arr[idx] <= target:
        curr.append(arr[idx])
        find_combination(idx, target - arr[idx], curr)  ← same idx
        curr.pop()                                       ← backtrack

    # NOT PICK (move to next element)
    find_combination(idx + 1, target, curr)              ← next idx
```

---

### Recursion Tree — `[2,3,6,7]`, target=7

```
find(idx=0, rem=7, [])
├── PICK 2 → find(0, 5, [2])
│   ├── PICK 2 → find(0, 3, [2,2])
│   │   ├── PICK 2 → find(0, 1, [2,2,2])
│   │   │   ├── PICK 2: 2>1 → skip
│   │   │   └── SKIP → find(1, 1, [2,2,2])
│   │   │           → find(2, 1, [2,2,2])
│   │   │           → find(3, 1, [2,2,2])
│   │   │           → find(4, 1, [2,2,2]) → idx=end, rem≠0 → ✗
│   │   └── SKIP → find(1, 3, [2,2])
│   │               ├── PICK 3 → find(1, 0, [2,2,3]) → rem=0 ✅ ADD
│   │               └── ...
│   └── ...
└── SKIP → find(1, 7, [])
    └── ...
        └── PICK 7 → find(3, 0, [7]) → rem=0 ✅ ADD
```

---

### Why Staying at the Same Index Enables Reuse

```
Lomuto (0/1 Knapsack style):
  NOT PICK → find(idx+1, ...)   ← move on
  PICK     → find(idx-1 or idx+1, ...) ← move on after picking

Combination Sum (unbounded):
  NOT PICK → find(idx+1, ...)   ← move on
  PICK     → find(idx, ...)     ← STAY — can pick same element again

This is the same `stay at same row` trick from Coin Change DP.
```

---

### Pruning — `if arr[idx] <= target`

```
if arr[idx] <= target:
    # try picking

If the current element exceeds remaining target, picking is pointless.
This pruning avoids exploring branches guaranteed to overshoot.
Works optimally when arr is sorted (once arr[idx] > target, all further are too).
```

---

### Backtracking — `curr.pop()`

```
curr.append(arr[idx])               ← include
find_combination(idx, target-arr[idx], curr)
curr.pop()                          ← undo include before exploring skip

Without pop():
  curr would carry [2] into the skip branch
  and you'd incorrectly accumulate elements across branches.
```

---

### Combination Sum I vs II

```
Sum I:   unlimited reuse → PICK calls same idx
         no duplicates in input → no duplicate suppression needed

Sum II:  each element used once → PICK calls idx+1
         duplicates possible in input → skip arr[i]==arr[i-1] at same level
```

---

### Complexity

| | |
|---|---|
| Time | O(2^target) in worst case — exponential branches |
| Space | O(target/min_element) — max recursion depth |
