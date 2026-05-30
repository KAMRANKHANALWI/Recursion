## Permutations II — Swap + Seen Set — Algorithm & Intuition

**Problem:** Generate all unique permutations using in-place swapping with a local `seen` set to deduplicate.

```
nums = [1, 1, 2]
→ [[1,1,2],[1,2,1],[2,1,1]]
```

---

### Intuition

**The Dream:** Same unique permutations as problem 22 — but without sorting or the `used[]` array.

**Key Insight:** At each recursion level (each value of `index`), track which VALUES have already been placed at position `index` using a local `seen` set. If the same value appears again at the same position, skip it — it would produce an identical subtree.

---

### The Code

```
def backtrack(index):
    if index == len(nums):
        result.append(nums.copy())
        return

    seen = set()                         ← fresh set per call

    for i in range(index, len(nums)):
        if nums[i] in seen:
            continue                     ← same value already tried at this position
        seen.add(nums[i])

        nums[index], nums[i] = nums[i], nums[index]   ← swap into position
        backtrack(index + 1)
        nums[index], nums[i] = nums[i], nums[index]   ← swap back
```

---

### Why `seen` is Local to Each Call

```
seen tracks: "which VALUES have I already placed at position = index?"

It is created fresh at each backtrack(index) call because
position `index` is different for each level of the tree.
What's duplicate at position 0 may be unique at position 1.

If seen were global, it would block valid choices at deeper levels.
```

---

### Recursion Tree — `[1, 1, 2]` (no sorting needed)

```
backtrack(0)  nums=[1,1,2]  seen={}
  i=0: nums[0]=1 ∉ seen → seen={1}, sw(0,0)→[1,1,2]
       backtrack(1)  nums=[1,1,2]  seen={}
         i=1: nums[1]=1 ∉ seen → seen={1}, sw(1,1)→[1,1,2]
              backtrack(2)→ sw(2,2)→[1,1,2] ✅ save
         i=2: nums[2]=2 ∉ seen → seen={1,2}, sw(1,2)→[1,2,1]
              backtrack(2)→ sw(2,2)→[1,2,1] ✅ save
              ↩ sw(1,2)→[1,1,2] restored

  i=1: nums[1]=1 ∈ seen → SKIP ✂️

  i=2: nums[2]=2 ∉ seen → seen={1,2}, sw(0,2)→[2,1,1]
       backtrack(1)  nums=[2,1,1]  seen={}
         i=1: nums[1]=1 ∉ seen → seen={1}, sw(1,1)→[2,1,1]
              backtrack(2)→[2,1,1] ✅ save
         i=2: nums[2]=1 ∈ seen → SKIP ✂️
       ↩ sw(0,2)→[1,1,2] restored

Result: [[1,1,2],[1,2,1],[2,1,1]] ✅
```

---

### Seen Set vs used[] Approach

```
Feature           | Seen Set (this)        | used[] (problem 22)
------------------|------------------------|---------------------
Sorting needed?   | No                     | Yes
Extra space       | O(N) seen sets         | O(N) used array
Dedup scope       | Per position (local)   | Per value (global)
Condition         | nums[i] in seen        | nums[i]==nums[i-1] and not used[i-1]
Conceptual model  | "already tried here"   | "ordered sibling pruning"
Array modified?   | Yes (swap + restore)   | No (curr list built separately)
```

---

### Why No Sorting Needed Here

```
used[] approach: relies on nums[i]==nums[i-1] which only detects adjacent dups
                 → needs sorting so duplicate values ARE adjacent.

seen set approach: checks the VALUE directly against previously tried values
                   at this position → works regardless of order.
                   Duplicates anywhere in the subarray are caught.
```

---

### Complexity

| | |
|---|---|
| Time | O(N! × N) worst case with pruning reducing it |
| Space | O(N) per recursion level × O(N) depth = O(N²) for seen sets |
