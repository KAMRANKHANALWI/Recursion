## Merge Sort — Algorithm & Intuition

**Problem:** Sort an array using the divide-and-conquer recursive approach.

```
arr = [12, 1, 3, 2, 4, -1]
→ [-1, 1, 2, 3, 4, 12]
```

---

### Intuition

**The Dream:** Split the problem until it's trivial, then carefully combine the results.

**Key Insight:** Sorting a single element is free (it's already sorted). Merging two sorted arrays into one sorted array is cheap (O(N)). So: keep splitting until arrays are size 1, then merge your way back up.

```
DIVIDE:  split array in half recursively until size 1
CONQUER: merge two sorted halves into one sorted array
```

---

### The Two Functions

```
merge_sort(arr, low, high):
    if low >= high: return [arr[low]]    ← base: single element
    mid = (low + high) // 2
    left  = merge_sort(arr, low, mid)
    right = merge_sort(arr, mid+1, high)
    return merge_two_sorted_arr(left, right)

merge_two_sorted_arr(left, right):
    use two pointers i, j
    always pick the smaller of left[i] vs right[j]
    drain remaining elements after one side exhausts
```

---

### Recursion Tree — `[12, 1, 3, 2]`

```
                  merge_sort([12,1,3,2])
                 /                      \
    merge_sort([12,1])         merge_sort([3,2])
      /          \               /          \
 ms([12])      ms([1])       ms([3])      ms([2])
   [12]          [1]           [3]          [2]
       \        /                  \        /
      merge([12],[1])           merge([3],[2])
           [1,12]                   [2,3]
                    \              /
               merge([1,12],[2,3])
                    [1,2,3,12]
```

---

### Merge — Step by Step

```
left = [1, 12],  right = [2, 3]
i=0, j=0, result=[]

left[0]=1  < right[0]=2  → take 1,  i=1   result=[1]
left[1]=12 > right[0]=2  → take 2,  j=1   result=[1,2]
left[1]=12 > right[1]=3  → take 3,  j=2   result=[1,2,3]
j exhausted → drain left: take 12           result=[1,2,3,12] ✅
```

---

### Why Merge Sort is Stable

```
When left[i] == right[j]:
    We take from left first (left[i] < right[j] is false → else branch).

Wait — the code uses strict <:
    if left[i] < right[j]: take left
    else: take right   ← ties go to RIGHT (not stable as written!)

For stability: change condition to left[i] <= right[j] → take left on tie.
```

---

### The Key Insight — Work Happens on Merge, Not Split

```
In merge sort:
  Splitting is trivial — just compute mid, no actual work
  Merging is where all the sorting happens

Compare with Quick Sort:
  Partitioning does the real work (split is non-trivial)
  Merging is trivial (already sorted by partition)
```

---

### Merge Sort Properties

```
✅ Stable sort (if ties take left[i])
✅ Predictable O(N log N) — no worst case degradation
✅ Works well for linked lists (no random access needed)
❌ O(N) extra space for merge step (not in-place)
```

---

### Complexity

| | |
|---|---|
| Time | O(N log N) — log N levels, O(N) merge per level |
| Space | O(N) — temporary arrays in merge + O(log N) call stack |
