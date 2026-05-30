## Quick Sort — Lomuto Partition — Algorithm & Intuition

**Problem:** Sort an array in-place using Quick Sort with Lomuto's partition scheme.

```
arr = [12, 31, 35, 8, 32, 17]
→ [8, 12, 17, 31, 32, 35]
```

---

### Intuition

**The Dream:** Place one element (pivot) in its exact final position, then recurse.

**Key Insight:** Pick a pivot. Rearrange so everything to its left is ≤ pivot and everything to its right is > pivot. The pivot is now **permanently placed**. Recurse on both halves.

```
Each partition call fixes exactly ONE element in its sorted position.
N calls fix all N elements.
```

---

### Lomuto Partition — Pivot = Last Element

```
def partition(arr, start, end):
    pivot = arr[end]          ← always pick last element
    index = start - 1        ← boundary of "small elements" zone

    for j in range(start, end):
        if arr[j] <= pivot:
            index += 1
            swap(arr, index, j)   ← move small element to left zone

    index += 1
    swap(arr, index, end)     ← place pivot at its correct position
    return index              ← pivot's final index
```

---

### How Lomuto Works — Visual

```
arr = [8, 32, 17, 12],  pivot = 12 (last)
index = -1 (before start)

j=0: arr[0]=8  <= 12 → index=0, swap(0,0) → [8, 32, 17, 12]
j=1: arr[1]=32 >  12 → skip
j=2: arr[2]=17 >  12 → skip

Place pivot: index=1, swap(1, end=3) → [8, 12, 17, 32]
                                              ↑ pivot in place ✅

Recurse on [8] and [17, 32]
```

---

### Full Dry Run — `[12, 31, 35, 8, 32, 17]`

```
Level 1: partition(0, 5), pivot=17, index=-1
  j=0: 12<=17 → idx=0, no change   [12, 31, 35, 8, 32, 17]
  j=1: 31>17  → skip
  j=2: 35>17  → skip
  j=3: 8<=17  → idx=1, swap(1,3)   [12, 8, 35, 31, 32, 17]
  j=4: 32>17  → skip
  Place pivot: swap(2, 5)           [12, 8, 17, 31, 32, 35]
  pivot_idx = 2

Recurse left:  [12, 8]  (0..1)
Recurse right: [31, 32, 35] (3..5) → already sorted after further recursion

Final: [8, 12, 17, 31, 32, 35] ✅
```

---

### The `index` Variable — What It Tracks

```
index = last position where a "small" element was placed

Everything in arr[start..index] is ≤ pivot.
Everything in arr[index+1..j-1] is > pivot.
arr[j..end-1] = unseen elements.

After the loop: pivot belongs at index+1.
```

---

### Lomuto vs Hoare

```
Feature          | Lomuto              | Hoare
-----------------|---------------------|--------------------
Pivot choice     | Last element        | First element
Pointers         | One (index+j)       | Two (i from left, j from right)
Swaps            | More (one per small)| Fewer (only when both wrong)
Partition range  | Returns exact index | Returns split point (not pivot pos)
Code simplicity  | Simpler             | Slightly more complex
Performance      | Slightly slower     | Slightly faster in practice
```

---

### Worst Case — Already Sorted Input

```
arr = [1, 2, 3, 4, 5], pivot always = last

Each partition puts pivot at end → one side has 0 elements, other has n-1.
Recursion depth = N → O(N²) comparisons.

Fix: random pivot selection or median-of-three.
```

---

### Complexity

| Case | Time | Space |
|---|---|---|
| Best / Average | O(N log N) | O(log N) stack |
| Worst (sorted) | O(N²) | O(N) stack |
