## Print All Subsequences with Sum K — Algorithm & Intuition

**Problem:** Print every subsequence of an array whose elements sum to exactly `k`.

```
arr = [1, 2, 1],  k = 2
→ [1, 1]
→ [2]
```

---

### Intuition

**The Dream:** Same as printing all subsequences — but with a filter at the leaf.

**Key Insight:** Generate all subsequences exactly as before (include/exclude at each index). At the base case, only print if `curr_sum == k`. Everything else is unchanged.

```
Same binary tree of decisions.
Only the base case adds a condition:
  if i == len(arr) AND curr_sum == k: print
```

---

### The Only Change from Subsequences

```
Subsequences (problem 9):
    if i == len(arr):
        print(result)       ← always print

Subsequences Sum K (this):
    if i == len(arr):
        if curr_sum == k:   ← conditional print
            print(result)
```

---

### Recursion Tree — `[1,2,1]`, k=2

```
                        dfs(0, sum=0, [])
                    /                     \
            +1                              skip 1
       dfs(1, 1, [1])                 dfs(1, 0, [])
       /         \                    /           \
     +2          skip 2            +2            skip 2
  dfs(2,3,[1,2]) dfs(2,1,[1])  dfs(2,2,[2])  dfs(2,0,[])
   /    \          /    \         /    \         /    \
 +1   skip      +1   skip      +1   skip      +1   skip
sum=4  3      sum=2   1      sum=3   2       sum=1   0
        ✗     [1,1]✅  ✗        ✗   [2]✅      ✗     ✗
```

Two valid subsequences: [1,1] and [2] ✅

---

### Approach 1 — Accumulate Sum Separately

```
def print_subseq_sum_k(arr, i, result, curr_sum, k):
    if i == len(arr):
        if curr_sum == k:
            print(result)
        return

    result.append(arr[i])
    print_subseq_sum_k(arr, i+1, result, curr_sum + arr[i], k)  ← include

    result.pop()
    print_subseq_sum_k(arr, i+1, result, curr_sum, k)           ← exclude
```

`curr_sum` is passed by value (int) — no need to undo it, only `result` (list) needs backtracking.

---

### Approach 2 — Modify and Restore curr_sum

```
curr_sum += arr[i]   ← add
result.append(arr[i])
recurse include...

curr_sum -= arr[i]   ← undo (explicit backtrack of sum)
result.pop()
recurse exclude...
```

This is equivalent but mutates `curr_sum` — works correctly here because integers are reassigned, not mutated. Both approaches produce the same result.

---

### Why curr_sum Doesn't Need pop()

```
result is a LIST → shared across calls → needs explicit undo (pop)
curr_sum is an INT → passed by value (or reassigned) → each branch sees its own copy

In Approach 1: curr_sum + arr[i] creates a NEW int, doesn't modify curr_sum.
In Approach 2: += then -= restores it manually.

Either way, both branches of the recursion see the correct sum.
```

---

### This is the Foundation of Count Subsets (DP)

```
Print Subseq Sum K:  base case prints if sum == k
Count Subseq Sum K:  base case returns 1 if sum == k, 0 otherwise
DP Subset Sum:       memoizes the count to avoid recomputing

The tree structure is identical. DP just adds a cache.
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N × N) — explore all 2^N paths, print costs O(N) |
| Space | O(N) — call stack + result list |
