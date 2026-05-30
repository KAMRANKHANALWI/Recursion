## Print ONE Subsequence with Sum K — Algorithm & Intuition

**Problem:** Find and print **any one** subsequence that sums to `k`. Stop immediately after finding the first one.

```
arr = [1, 2, 1],  k = 2
→ [1, 1]   (prints first valid one found, then stops)
```

---

### Intuition

**The Dream:** Don't explore the entire tree — stop the moment you succeed.

**Key Insight:** Use the **return value as a signal**. When a valid subsequence is found, return `True` up the call stack. Every parent that receives `True` immediately returns `True` without exploring the other branch. The entire remaining recursion tree is pruned.

```
if valid_found: return True   ← short-circuit both branches
```

---

### The Code Pattern

```
def print_one_subseq(arr, i, result, curr_sum, k):
    if i == len(arr):
        if curr_sum == k:
            print(result)
            return True       ← FOUND — signal upward
        return False          ← not found at this leaf

    # Try INCLUDE
    result.append(arr[i])
    curr_sum += arr[i]
    if print_one_subseq(arr, i+1, result, curr_sum, k):
        return True           ← propagate success, DON'T try exclude

    # Try EXCLUDE (only if include didn't succeed)
    result.pop()
    curr_sum -= arr[i]
    if print_one_subseq(arr, i+1, result, curr_sum, k):
        return True

    return False              ← neither branch found anything
```

---

### Recursion Tree — What Gets Pruned

```
[1, 2, 1], k=2

                        dfs(0, 0, [])
                    /                  \
              include 1               (NEVER REACHED)
         dfs(1, 1, [1])
         /              \
       include 2        skip 2
  dfs(2, 3, [1,2])    dfs(2, 1, [1])
  → sum=3 ≠ 2          /          \
  → return False    include 1     skip 1
                  dfs(3, 2, [1,1])
                  → sum=2==k ✅
                  → print [1,1]
                  → return True  ← propagates all the way up
                                   RIGHT BRANCH NEVER EXPLORED ✅
```

---

### The `if recurse(): return True` Pattern

```
if print_one_subseq(arr, i+1, result, curr_sum, k):
    return True
```

This is the key line. It means:
- If the include branch found a solution → stop. Don't try exclude.
- If the include branch failed → fall through to try exclude.
- If exclude also fails → return False to parent.

This pattern **propagates success upward immediately** and **prunes the tree aggressively**.

---

### Print All vs Print One vs Count

```
Print ALL:   never short-circuit, explore entire tree
Print ONE:   short-circuit on first success (return True propagation)
Count:       never short-circuit, accumulate count at leaves
```

```
# Print ALL
recurse include
recurse exclude

# Print ONE
if recurse include: return True
if recurse exclude: return True
return False

# Count
return (recurse include) + (recurse exclude)
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N) worst case (no match), O(N) best case (first leaf matches) |
| Space | O(N) — call stack |
