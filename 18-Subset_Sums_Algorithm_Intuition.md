## Subset Sums — Algorithm & Intuition

**Problem:** Return a sorted list of the sums of all possible subsets of the array.

```
arr = [1, 2, 3]
→ [0, 1, 2, 3, 3, 4, 5, 6]
```

---

### Intuition

**The Dream:** Compute every subset sum without storing the subsets themselves.

**Key Insight:** At each index, make the binary include/exclude choice — but instead of tracking which elements you picked, just track the **running sum**. At the leaf (base case), record the sum.

```
Sums flow down as integers. No list management needed.
No backtracking — integers are passed by value.
```

---

### The Code

```
def dfs(idx, curr_sum):
    if idx == len(arr):
        result.append(curr_sum)   ← record this subset's sum
        return

    dfs(idx + 1, curr_sum + arr[idx])  ← INCLUDE: add to sum
    dfs(idx + 1, curr_sum)              ← EXCLUDE: sum unchanged
```

---

### Recursion Tree — `[1, 2, 3]`

```
                    dfs(0, 0)
                  /           \
           dfs(1, 1)         dfs(1, 0)
           /      \           /      \
       dfs(2,3) dfs(2,1)  dfs(2,2) dfs(2,0)
       /   \    /   \     /   \    /   \
   d(3,6) d(3,3) d(3,4) d(3,1) d(3,5) d(3,2) d(3,3) d(3,0)
     6      3     4      1      5      2      3      0

Collected: [6, 3, 4, 1, 5, 2, 3, 0]
After sort: [0, 1, 2, 3, 3, 4, 5, 6] ✅
```

---

### Why No Backtracking?

```
Print Subsequences (problem 9):
  result is a LIST → shared reference → must pop to undo

Subset Sums (this problem):
  curr_sum is an INT → passed by VALUE
  dfs(idx+1, curr_sum + arr[idx]) creates a NEW int
  The original curr_sum is unchanged — nothing to undo

This is the cleaner pattern when you only need aggregate values.
```

---

### Include vs Exclude Call Order

```
dfs(idx+1, curr_sum + arr[idx])  ← LEFT child: include
dfs(idx+1, curr_sum)             ← RIGHT child: exclude

Left child always includes → left subtrees tend to have larger sums.
Right child always excludes → right subtrees tend to have smaller sums.

The sort at the end handles the final ordering.
```

---

### The Recursion Tree Is a Perfect Binary Tree

```
n elements → n levels → 2^n leaves → 2^n sums

Each leaf corresponds to exactly one subset:
  Include/exclude decisions at each level form a unique binary path.
  Left=include=1, Right=exclude=0:
    Leftmost leaf (all includes): arr[0]+arr[1]+...+arr[n-1] = total sum
    Rightmost leaf (all excludes): 0 = empty subset sum
```

---

### Subset Sums vs Print Subsequences vs Count

```
Print Subsequences:  track which elements → need list + backtrack
Subset Sums:         track running sum only → int by value → no backtrack
Count with sum k:    return count from leaves → no tracking needed

Subset Sums is the middle ground — lightweight tracking, full coverage.
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N) for DFS + O(2^N log 2^N) for sort = O(N × 2^N) |
| Space | O(N) call stack + O(2^N) result list |
