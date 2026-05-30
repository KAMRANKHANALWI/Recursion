## Permutations II — Unique Permutations (used[] approach) — Algorithm & Intuition

**Problem:** Generate all **unique** permutations from an array that **may contain duplicates**.

```
nums = [1, 1, 2]
→ [[1,1,2],[1,2,1],[2,1,1]]   (3 unique, not 3!=6)
```

---

### Intuition

**The Dream:** All distinct orderings — no duplicates in output despite duplicates in input.

**Key Insight:** Sort the array. Use the standard `used[]` approach from problem 20 — but add one pruning rule: if `nums[i] == nums[i-1]` and `nums[i-1]` is NOT currently used, skip `i`. This prevents identical subtrees from being explored twice at the same level.

---

### The Pruning Rule

```
if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
    continue
```

Breaking it down:

```
nums[i] == nums[i-1]:  same value as the previous element
not used[i-1]:         the previous element is NOT in the current path

→ meaning: we're about to start a new branch with nums[i]=X,
           but we already explored (or are about to explore after backtrack)
           a branch with nums[i-1]=X where i-1 was picked first.
           These two branches produce identical subtrees → skip.
```

---

### Why `not used[i-1]` Is the Key Condition

```
nums = [1a, 1b, 2]  (subscripts to distinguish the two 1s)

Without pruning: both branches "pick 1a first" and "pick 1b first"
produce the same permutations → duplicates.

Prune rule ensures: if both 1a and 1b exist, we ALWAYS pick 1a before 1b.
→ "pick 1b before 1a" (i.e., used[i-1]=False while at 1b) is skipped.

When used[i-1]=True: we're inside the "1a picked first" branch → 1b is fair game.
When used[i-1]=False: "1a NOT picked" + "trying 1b" = duplicate of some other branch.
```

---

### Recursion Tree — `[1, 1, 2]` (sorted)

```
path=[], used=[F,F,F]

  i=0: pick nums[0]=1 → used=[T,F,F], path=[1]
    i=0: used[0]=T → skip
    i=1: nums[1]==nums[0] AND not used[0]? used[0]=T → NOT skipped
         pick nums[1]=1 → path=[1,1]
      i=2: pick 2 → path=[1,1,2] ✅ save
    i=2: pick 2 → path=[1,2]
      i=0: used → skip
      i=1: nums[1]=1==nums[0]=1 AND not used[0]? used[0]=F → SKIP ✂️
      i=2: used → skip
      → only option was skipped, so path=[1,2] has only one completion
        Actually: let me redo — at path=[1,2] used=[T,F,T]:
      i=1: pick 1 → path=[1,2,1] ✅ save

  i=1: nums[1]=1==nums[0]=1 AND not used[0]? F is False → SKIP ✂️

  i=2: pick nums[2]=2 → path=[2]
    i=0: pick 1 → path=[2,1]
      i=0: used → skip
      i=1: nums[1]=1==nums[0]=1 AND not used[0]? used[0]=T → NOT skipped
           pick 1 → path=[2,1,1] ✅ save
      i=2: used → skip
    i=1: nums[1]=1==nums[0]=1 AND not used[0]? used[0]=F → SKIP ✂️
    i=2: used → skip

Result: [[1,1,2], [1,2,1], [2,1,1]] ✅  (3 unique permutations)
```

---

### Permutations I vs II

```
Perm I (distinct):  no skip rule needed
Perm II (dupes):    sort + skip when nums[i]==nums[i-1] and not used[i-1]

The `not used[i-1]` check is unique to this problem —
it's more subtle than the `i > idx` check in Subsets II.
```

---

### Complexity

| | |
|---|---|
| Time | O(N! × N) worst case — fewer with pruning |
| Space | O(N) — path + used + call stack |
