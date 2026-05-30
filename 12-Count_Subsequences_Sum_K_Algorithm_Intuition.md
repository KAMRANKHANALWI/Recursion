## Count Subsequences with Sum K — Algorithm & Intuition

**Problem:** Count how many subsequences of an array sum to exactly `k`.

```
arr = [1, 2, 1],  k = 2
→ 2   ([1,1] and [2])
```

---

### Intuition

**The Dream:** Count all valid paths in the recursion tree without printing them.

**Key Insight:** Same binary tree as before. At each leaf, return `1` if sum == k, else `0`. The count naturally **bubbles up** via addition — each internal node returns the sum of its two children's counts.

```
count = count(include branch) + count(exclude branch)
```

---

### The Code

```
def count_subseq(arr, i, curr_sum, k):
    if i == len(arr):
        return 1 if curr_sum == k else 0   ← leaf vote

    left  = count_subseq(arr, i+1, curr_sum + arr[i], k)  ← include
    right = count_subseq(arr, i+1, curr_sum, k)            ← exclude

    return left + right   ← total from both branches
```

No `result` list needed — we're counting, not storing subsequences.

---

### Recursion Tree with Counts — `[1,2,1]`, k=2

```
                     dfs(0, 0)
                    /          \
              dfs(1, 1)      dfs(1, 0)
             /       \       /       \
        dfs(2,3)  dfs(2,1) dfs(2,2) dfs(2,0)
        /    \    /    \    /    \    /    \
     d(3,4) d(3,3) d(3,2) d(3,1) d(3,3) d(3,2) d(3,1) d(3,0)
       0      0      1     0      0      1      0      0

Leaf values: 0,0,1,0,0,1,0,0

Bubbling up:
  dfs(2,3) = 0+0 = 0
  dfs(2,1) = 1+0 = 1
  dfs(2,2) = 0+1 = 1
  dfs(2,0) = 0+0 = 0

  dfs(1,1) = 0+1 = 1
  dfs(1,0) = 1+0 = 1

  dfs(0,0) = 1+1 = 2 ✅
```

---

### Three Variants Side by Side

```
Print ALL subsequences:    print at every leaf
Print ALL with sum k:      print at leaves where sum == k
Print ONE with sum k:      short-circuit on first True leaf
Count with sum k:          return 1 or 0 at leaf, sum up

Count is the simplest — no list management, no backtracking needed.
Just integers flowing up through the tree.
```

---

### This IS the DP Subset Count (Without Memo)

```
This recursive count function has overlapping subproblems:
  count_subseq(arr, i, curr_sum, k) is called multiple times
  with the same (i, curr_sum) arguments on different paths.

Adding memoization:
  dp = {}
  if (i, curr_sum) in dp: return dp[(i, curr_sum)]
  ...
  dp[(i, curr_sum)] = left + right

→ This becomes the DP Count Subsets problem (Knapsack repo #3).
The recursive structure is identical — memo just caches repeats.
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N) — all 2^N paths explored |
| Space | O(N) — call stack depth |

With memoization: O(N × max_sum) time and space.
