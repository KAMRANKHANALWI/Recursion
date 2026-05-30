## Permutations — Algorithm & Intuition (used[] approach)

**Problem:** Generate all permutations of a distinct integer array.

```
nums = [1, 2, 3]
→ [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

---

### Intuition

**The Dream:** Every possible ordering — N! arrangements.

**Key Insight:** A permutation picks one element per "slot". At each level, try every element that hasn't been used yet. Track which elements are in use with a `used[]` boolean array.

```
Level 0: pick any of N elements for position 0
Level 1: pick any of N-1 remaining elements for position 1
...
Level N-1: pick the last remaining element
Base case: N elements placed → one complete permutation
```

---

### The Code

```
def permutations(nums, idx, curr, result, used):
    if idx == len(nums):
        result.append(list(curr))   ← complete permutation
        return

    for i in range(len(nums)):
        if not used[i]:             ← element available?
            used[i] = True          ← mark as used
            curr.append(nums[i])    ← place it
            permutations(nums, idx+1, curr, result, used)
            curr.pop()              ← backtrack
            used[i] = False         ← unmark
```

---

### Recursion Tree — `[1, 2, 3]`

```
                  idx=0, curr=[], used=[F,F,F]
              /           |           \
          pick 1        pick 2       pick 3
      used=[T,F,F]   used=[F,T,F]  used=[F,F,T]
      curr=[1]        curr=[2]      curr=[3]
        /    \          /    \        /    \
     pk2    pk3      pk1    pk3    pk1    pk2
    [1,2]  [1,3]   [2,1]  [2,3]  [3,1]  [3,2]
      |      |       |      |      |      |
    pk3    pk2     pk3    pk1    pk2    pk1
  [1,2,3][1,3,2] [2,1,3][2,3,1][3,1,2][3,2,1]
     ✅    ✅      ✅     ✅     ✅     ✅
```

6 = 3! permutations ✅

---

### Backtracking — Three Steps

```
used[i] = True          ← 1. mark element as in-use
curr.append(nums[i])    ← 2. place element in current path
permutations(...)       ← 3. recurse with one less free element

curr.pop()              ← 4. UNDO placement
used[i] = False         ← 5. UNDO mark (free the element again)
```

Steps 4 and 5 are the backtrack — they restore state before trying the next element in the for-loop. Without them, `used` would permanently mark elements and `curr` would accumulate stale values.

---

### Why Scan All N Indices Every Level?

```
Unlike subsets (which advance idx to avoid re-using elements ahead),
permutations want any unused element from the ENTIRE array.
→ always scan from 0 to n-1
→ check used[i] to skip already-placed elements

This is the key structural difference from combinations/subsets:
  Subsets:      range(idx, n)  → only look forward
  Permutations: range(0, n)    → scan all, filter by used[]
```

---

### used[] vs Swap Approach (Problem 21)

```
used[] approach (this):
  Extra O(N) space for used array
  Preserves original array order
  More intuitive — explicitly tracks which elements are free

Swap approach (problem 21):
  No extra space for tracking
  Modifies array in-place (restored via second swap)
  Slightly trickier to reason about
```

---

### Complexity

| | |
|---|---|
| Time | O(N! × N) — N! permutations, each takes O(N) to copy |
| Space | O(N) — curr + used arrays + call stack depth |
