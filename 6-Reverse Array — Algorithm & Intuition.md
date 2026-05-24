## Reverse Array — Algorithm & Intuition

**Problem:** Reverse an array in-place using recursion — no extra array.

```
[1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]
```

---

### Intuition

**The Dream:** Flip the array without allocating extra space.

**Key Insight:** Swap the outermost pair, then recurse inward. Two pointers moving toward the center — when they meet or cross, you're done.

---

### Approach 1 — Two Pointers (l, r)

```
def reverse_array(arr, l, r):
    if l >= r: return               ← pointers met/crossed → done
    arr[l], arr[r] = arr[r], arr[l]  ← swap outermost pair
    reverse_array(arr, l+1, r-1)   ← move both inward
```

```
arr = [1, 2, 3, 4, 5]

Call 1: l=0, r=4 → swap(1,5) → [5, 2, 3, 4, 1] → call(1,3)
Call 2: l=1, r=3 → swap(2,4) → [5, 4, 3, 2, 1] → call(2,2)
Call 3: l=2, r=2 → l>=r → return   ← middle element stays

Result: [5, 4, 3, 2, 1] ✅
```

---

### Approach 2 — Single Index (i)

```
def reverse_array_ii(arr, i):
    n = len(arr)
    if i == n // 2: return          ← halfway through → done
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]  ← swap i with mirror
    reverse_array_ii(arr, i+1)     ← move inward from left
```

```
arr = [2, 4, 6, 8, 10]  (n=5)

i=0: swap(arr[0]=2, arr[4]=10) → [10, 4, 6, 8, 2]
i=1: swap(arr[1]=4, arr[3]=8)  → [10, 8, 6, 4, 2]
i=2: i == 5//2 == 2 → return

Result: [10, 8, 6, 4, 2] ✅
```

---

### Why `n // 2` Not `n`?

```
arr = [1, 2, 3, 4, 5]  (n=5)

Swap pairs: (0,4), (1,3) → 2 swaps
Middle index 2 → no partner → stays in place.

Only need to process the first n//2 indices.
Going further would un-reverse what you already fixed.
```

---

### Two Approaches — Same Idea, Different Parameterisation

```
Approach 1 (l,r):  both ends tracked explicitly, stop when they meet
Approach 2 (i):    only left index tracked, right derived as n-i-1

Both do exactly n//2 swaps.
Approach 1 is clearer for interview whiteboarding.
Approach 2 is more concise.
```

---

### In-Place Swap in Python

```
arr[l], arr[r] = arr[r], arr[l]

Python evaluates the right side fully before assignment.
No temp variable needed — tuple packing/unpacking handles it.
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Two-pointer (l,r) | O(N/2) = O(N) | O(N/2) stack |
| Single index (i) | O(N/2) = O(N) | O(N/2) stack |