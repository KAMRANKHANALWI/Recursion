## Subsets II (with Duplicates) — Algorithm & Intuition

**Problem:** Given an array that **may contain duplicates**, return all unique subsets.

```
nums = [1, 2, 2]
→ [[], [1], [1,2], [1,2,2], [2], [2,2]]
```

---

### Intuition

**The Dream:** Every unique subset — no duplicate subsets in output.

**Key Insight:** Sort the array so duplicates are adjacent. Use a for-loop pattern where you save the current state **at every call entry** (not just at leaves). Skip duplicate values at the same recursion level using `i > idx`.

---

### Two Differences From Subsets I

```
Subsets I  (problem 18, subset sums):
  - pick/not-pick binary tree, save ONLY at leaves
  - tracks running sum (int), no list needed

Subsets II (this problem):
  - for-loop pattern, save at ENTRY of every call
  - tracks actual elements (list), needs backtracking
  - skips duplicates at same level
```

---

### The Code Pattern

```
def backtrack(idx, curr):
    result.append(list(curr))   ← save IMMEDIATELY (this = one valid subset)

    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue            ← skip duplicate at same call level
        curr.append(nums[i])
        backtrack(i+1, curr)
        curr.pop()              ← backtrack
```

---

### Recursion Tree — `[1, 2, 2]` (sorted)

```
backtrack(0, []) → SAVE []
  i=0: pick 1 → backtrack(1, [1]) → SAVE [1]
    i=1: pick 2 → backtrack(2, [1,2]) → SAVE [1,2]
      i=2: pick 2 → backtrack(3, [1,2,2]) → SAVE [1,2,2]
    i=2: nums[2]==nums[1], i>idx(1) → SKIP ✂️
  i=1: pick 2 → backtrack(2, [2]) → SAVE [2]
    i=2: pick 2 → backtrack(3, [2,2]) → SAVE [2,2]
  i=2: nums[2]==nums[1], i>idx(0) → SKIP ✂️

Saved (in order): [], [1], [1,2], [1,2,2], [2], [2,2] ✅
```

---

### Why Save at Entry, Not Just Leaves?

```
Subsets (all sizes) = every partial path in the tree is a valid subset.
The empty set [] → save at very first call.
[1] → save when we start the backtrack(1,[1]) call.
[1,2] → save when backtrack(2,[1,2]) is called.
[1,2,2] → save at backtrack(3,[1,2,2]) (leaf, but same rule applies).

Every call = one unique subset → save immediately.
```

---

### The Duplicate Skip Rule

```
if i > idx and nums[i] == nums[i-1]: continue

i > idx:  Only skip if NOT the first element of this for-loop.
          The first element at this level MUST be tried.
          Only subsequent same-value elements create duplicates.

nums[i] == nums[i-1]:  This value was already explored at this level.
                        Exploring again = same subtree = duplicate subsets.
```

---

### Why `i > idx` Not `i > 0`?

```
nums = [1, 2, 2], sorted
At backtrack(1, [1]):  idx=1, for i from 1 to 2
  i=1: first at this level → MUST explore (pick nums[1]=2)
  i=2: i>idx(1) AND nums[2]==nums[1] → SKIP ✅

If we used i > 0 instead:
  i=1: i>0 AND nums[1]==nums[0]? No, 2≠1 → explore ✅
  i=2: i>0 AND nums[2]==nums[1]? Yes → SKIP ✅ (same result here)

For [2,2,2] with idx=0:
  i=0: first → explore
  i=1: i>idx(0) AND 2==2 → SKIP ✅
  i=2: i>idx(0) AND 2==2 → SKIP ✅

  With i>0: same result here too.

The difference shows when idx>0 and the FIRST element at that level
happens to equal its predecessor:
  nums=[1,1,2], at backtrack(1,[1]) (used first 1):
    i=1: nums[1]=1 = nums[0]=1
    With i>idx: i=1 == idx=1 → NOT skipped ✅ (allows [1,1] combination)
    With i>0:   i=1 > 0 AND 1==1 → SKIPPED ❌ (misses [1,1])
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N × N) — up to 2^N subsets, each copy costs O(N) |
| Space | O(N) call stack + O(2^N × N) result |
