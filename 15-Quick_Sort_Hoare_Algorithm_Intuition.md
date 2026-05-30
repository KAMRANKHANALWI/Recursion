## Quick Sort — Hoare Partition — Algorithm & Intuition

**Problem:** Sort an array in-place using Quick Sort with Hoare's partition scheme.

```
arr = [4, 2, 7, 3, 1, 6, 5]
→ [1, 2, 3, 4, 5, 6, 7]
```

---

### Intuition

**The Dream:** Same as Lomuto — pivot in place, recurse on halves. But do it with fewer swaps.

**Key Insight:** Use two pointers starting at opposite ends. Move them toward each other until they find a pair (left too large, right too small) that needs swapping. When they cross, the pivot is in the right half. Swap pivot to its boundary.

---

### Hoare Partition — Pivot = First Element

```
def hoare_partition(arr, low, high):
    pivot = arr[low]       ← first element is pivot
    i = low                ← left pointer
    j = high               ← right pointer

    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1         ← advance left past elements ≤ pivot

        while j > low and arr[j] > pivot:
            j -= 1         ← advance right past elements > pivot

        if i < j:
            swap(arr[i], arr[j])   ← wrong-side pair → swap

    swap(arr[low], arr[j])   ← place pivot at j (final boundary)
    return j
```

---

### Dry Run — `[4, 2, 7, 3, 1, 6, 5]`, pivot=4

```
pivot=4, i=0, j=6

Round 1:
  i: arr[0]=4≤4 → i=1; arr[1]=2≤4 → i=2; arr[2]=7>4 → STOP at i=2
  j: arr[6]=5>4 → j=5; arr[5]=6>4 → j=4; arr[4]=1≤4 → STOP at j=4
  i=2 < j=4 → swap(arr[2]=7, arr[4]=1) → [4, 2, 1, 3, 7, 6, 5]

Round 2:
  i: arr[2]=1≤4 → i=3; arr[3]=3≤4 → i=4; arr[4]=7>4 → STOP at i=4
  j: arr[4]=7>4 → j=3; arr[3]=3≤4 → STOP at j=3
  i=4 > j=3 → DON'T swap (i>=j, exit loop)

Place pivot: swap(arr[0]=4, arr[j=3]=3) → [3, 2, 1, 4, 7, 6, 5]
                                                     ↑ pivot 4 placed ✅

Recurse left:  [3, 2, 1]  (low=0, high=2)
Recurse right: [7, 6, 5]  (low=4, high=6)
```

---

### Key Difference from Lomuto

```
Lomuto:  j scans left→right, finds each small element, swaps it immediately
         → many small swaps

Hoare:   i and j scan from both ends toward the middle
         → only swaps wrong-side pairs (elements truly out of place)
         → ~3x fewer swaps on average
```

---

### The Subtle Boundary Condition

```
while i < high and arr[i] <= pivot: i++
while j > low  and arr[j] > pivot:  j--

Why `i < high` and `j > low`?
  Prevents i from going past high (out of bounds).
  Prevents j from going before low (past the pivot itself).

The `arr[low]` (pivot) stays at its original position until
the final swap — j eventually lands at the correct boundary.
```

---

### Why Swap `arr[low]` with `arr[j]` at the End?

```
When the loop exits (i >= j), j points to the rightmost element ≤ pivot.
This is exactly where the pivot belongs.
Swapping arr[low] (pivot) with arr[j] places pivot correctly.

After swap:
  arr[low..j-1]  all ≤ pivot
  arr[j]         = pivot (in final position)
  arr[j+1..high] all > pivot
```

---

### Lomuto vs Hoare at a Glance

```
Lomuto:   simple, pivot always ends in place, partition returns exact pivot index
Hoare:    faster (fewer swaps), j is partition point NOT pivot's final index

Recursion call difference:
  Lomuto:  quick_sort(low, pivot_idx-1) and quick_sort(pivot_idx+1, high)
  Hoare:   quick_sort(low, pivot_idx-1) and quick_sort(pivot_idx+1, high)
           (same structure, but pivot_idx from Hoare is the split, not pivot pos)
```

---

### Complexity

| Case | Time | Space |
|---|---|---|
| Best / Average | O(N log N) | O(log N) stack |
| Worst (sorted) | O(N²) | O(N) stack |
