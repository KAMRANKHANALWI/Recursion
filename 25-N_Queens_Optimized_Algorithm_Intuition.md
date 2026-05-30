## N Queens — Optimized O(1) Safety Check — Algorithm & Intuition

**Problem:** Same as N Queens — but replace the O(N) board scan with O(1) lookup using precomputed arrays.

---

### Intuition

**The Dream:** Same result as problem 24 — but faster safety checks.

**Key Insight:** Instead of scanning the board each time, maintain three boolean arrays that track which rows and diagonals are already occupied. Update them when placing/removing a queen in O(1).

---

### The Three Tracking Arrays

```
leftRow[row]                = 1 if row `row` already has a queen
lowerDiagonal[row + col]    = 1 if lower-left diagonal is occupied
upperDiagonal[n-1+col-row]  = 1 if upper-left diagonal is occupied
```

---

### The Diagonal Indices — Derivation

```
Upper-left diagonal (↖):
  All cells (r, c) on the same diagonal share the value: col - row
  Shift to make non-negative: n-1 + col - row
  Range: [0, 2n-2]

Lower-left diagonal (↙):
  All cells (r, c) on the same anti-diagonal share: row + col
  Range: [0, 2n-2]
```

```
Example: n=4
  Cell (0,0): upper = 4-1+0-0=3, lower = 0+0=0
  Cell (1,1): upper = 4-1+1-1=3, lower = 1+1=2
  → (0,0) and (1,1) are on the same upper diagonal (index 3) ✅
```

---

### The Code

```
if (leftRow[row] == 0 and
    lowerDiagonal[row + col] == 0 and
    upperDiagonal[n - 1 + col - row] == 0):

    # Place
    board[row][col] = "Q"
    leftRow[row] = 1
    lowerDiagonal[row + col] = 1
    upperDiagonal[n - 1 + col - row] = 1

    solve(col + 1)

    # Backtrack
    board[row][col] = "."
    leftRow[row] = 0
    lowerDiagonal[row + col] = 0
    upperDiagonal[n - 1 + col - row] = 0
```

---

### Speed Comparison

```
is_safe() in problem 24:
  Three while-loops scanning up to O(N) cells each
  → O(N) per safety check
  → O(N²) total per recursion level

Optimized (this):
  Three O(1) array lookups
  → O(1) per safety check
  → O(N) per recursion level

For N=12 (classical benchmark):
  Naive: millions of board scans
  Optimized: same logic, ~N× faster inner loop
```

---

### Backtracking the Arrays

```
All three arrays must be reset after backtracking:
  leftRow[row] = 0
  lowerDiagonal[row + col] = 0
  upperDiagonal[n-1+col-row] = 0

Just like board[row][col] = "." restores the board,
these resets restore the tracking state.

If any reset is forgotten → future safety checks give false positives
→ valid configurations get skipped → wrong answer.
```

---

### Why Columns Don't Need a Tracking Array

```
We place exactly one queen per column (column by column recursion).
Column `col` is never revisited — once we recurse to col+1,
we never go back and try col again.

So column conflicts are impossible by construction.
Only rows and diagonals need tracking.
```

---

### Summary — Naive vs Optimized

```
Feature         | Naive (24)         | Optimized (25)
----------------|--------------------|-------------------
Safety check    | O(N) board scan    | O(1) array lookup
Arrays used     | board only         | board + 3 tracking arrays
Space           | O(N²)              | O(N²) + O(N) arrays
Logic change    | None               | None (identical structure)
Speed           | Slower             | ~N× faster safety check
```

---

### Complexity

| | |
|---|---|
| Time | O(N!) — same placement count, O(1) check saves the constant |
| Space | O(N²) board + O(N) tracking arrays + O(N) stack |
