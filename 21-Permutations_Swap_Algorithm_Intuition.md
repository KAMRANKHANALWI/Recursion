## Permutations — Swap Approach — Algorithm & Intuition

**Problem:** Generate all permutations using in-place swapping — no `used[]` array needed.

```
nums = [1, 2, 3]
→ [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

---

### Intuition

**The Dream:** Same result as problem 20 — but without tracking which elements are used.

**Key Insight:** Fix one element at the current position (`idx`) by swapping each remaining element into it. After recursing, swap back (backtrack) to restore the array.

```
At position idx:
  For each i from idx to n-1:
    Swap nums[idx] with nums[i]  → element i is now "fixed" at position idx
    Recurse on idx+1             → fill positions idx+1 to n-1
    Swap back                    → restore array for next iteration
```

---

### The Code

```
def permutations(nums, idx, result):
    if idx == len(nums):
        result.append(list(nums))   ← entire array IS the permutation
        return

    for i in range(idx, len(nums)):
        nums[idx], nums[i] = nums[i], nums[idx]   ← fix element i at position idx
        permutations(nums, idx+1, result)
        nums[idx], nums[i] = nums[i], nums[idx]   ← swap back (backtrack)
```

---

### Recursion Tree — `[1, 2, 3]`

```
idx=0, nums=[1,2,3]
  i=0: sw(0,0)→[1,2,3]  → idx=1
    i=1: sw(1,1)→[1,2,3] → idx=2 → sw(2,2)→[1,2,3] ✅ save
    i=2: sw(1,2)→[1,3,2] → idx=2 → sw(2,2)→[1,3,2] ✅ save
  ↩ i=0 restored → [1,2,3]

  i=1: sw(0,1)→[2,1,3]  → idx=1
    i=1: sw(1,1)→[2,1,3] ✅ save
    i=2: sw(1,2)→[2,3,1] ✅ save
  ↩ sw(0,1)→[1,2,3] restored

  i=2: sw(0,2)→[3,2,1]  → idx=1
    i=1: sw(1,1)→[3,2,1] ✅ save
    i=2: sw(1,2)→[3,1,2] ✅ save
  ↩ sw(0,2)→[1,2,3] restored
```

---

### Why Swap is Its Own Inverse

```
swap(nums, idx, i) then swap(nums, idx, i) again → original array

This is the backtrack — swapping the same pair twice undoes the change.
No separate undo operation needed; the same line of code is the undo.
```

---

### What `idx` Represents

```
nums = [_, _, _, ...]
        ↑
       idx

"Positions 0..idx-1 are already fixed (chosen for their slots)."
"Positions idx..n-1 are still free — can be placed here."

At each level, we try placing every element from idx..n-1 at position idx.
```

---

### Swap Approach vs used[] Approach

```
Feature          | Swap               | used[]
-----------------|--------------------|--------------------
Extra space      | O(1)               | O(N) for used array
Array state      | Modified in-place  | Preserved, tracked externally
Base case save   | list(nums)         | list(curr)
Range of i       | range(idx, n)      | range(0, n)
Uniqueness       | Via seen set (p23) | Via sorted + not used[i-1] (p22)
Conceptual ease  | Trickier to trace  | More intuitive
```

---

### Does Swap Produce the Same Order as used[]?

```
Not necessarily — the order of permutations differs.
Both produce all N! permutations, just in a different sequence.
Both are correct.

[1,2,3]: both produce the same set of 6 permutations.
Order within result list may differ.
```

---

### Complexity

| | |
|---|---|
| Time | O(N! × N) — N! permutations, O(N) to copy each |
| Space | O(N) — call stack depth only (no extra tracking array) |
