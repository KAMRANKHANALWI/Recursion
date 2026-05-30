## N Queens — Algorithm & Intuition

**Problem:** Place N queens on an N×N chessboard such that no two queens attack each other. Return all valid configurations.

```
n = 4  →  2 solutions:
[".Q..", "...Q", "Q...", "..Q."]
["..Q.", "Q...", "...Q", ".Q.."]
```

---

### Intuition

**The Dream:** Fill the board with N non-attacking queens.

**Key Insight:** Place queens **column by column**. In each column, try every row. Before placing, check if the position is safe (no queen attacks from the left side). If safe, place and recurse to the next column. If not, skip.

```
One queen per column → guarantees no two queens share a column.
The safety check handles row and diagonal conflicts.
```

---

### Why Column by Column?

```
Each column must have exactly one queen (N queens, N columns).
By iterating column-by-column, we automatically ensure:
  ✅ No two queens in the same column (each column gets exactly one)
  
Still need to check:
  ❌ Same row (horizontal attack)
  ❌ Upper-left diagonal
  ❌ Lower-left diagonal
  (Right side is always empty — haven't placed there yet)
```

---

### Safety Check — Only Look Left

```
def is_safe(row, col):
    # Check left in same row
    c = col
    while c >= 0:
        if board[row][c] == "Q": return False
        c -= 1

    # Check upper-left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == "Q": return False
        r -= 1; c -= 1

    # Check lower-left diagonal
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == "Q": return False
        r += 1; c -= 1

    return True
```

Only scan LEFT — the right side (columns > col) is empty, future placements handle themselves.

---

### Dry Run — n=4, col=0

```
board = [....] × 4

col=0, try row 0: is_safe(0,0)? Yes (empty board)
  Place Q at (0,0):
  [Q...]
  [....]
  [....]
  [....]
  → recurse col=1
    row=0: same row as (0,0) → False
    row=1: diagonal conflict with (0,0) → False
    row=2: is_safe(2,1)? Yes ✅
      Place Q at (2,1):
      [Q...]
      [....]
      [.Q..]
      [....]
      → recurse col=2
        row=0: same row as (0,0) → False
        row=1: is_safe(1,2)? ... (no conflict) → place
          ... → recurse col=3 → no safe row → backtrack
        row=3: is_safe(3,2)? ... → but leads to dead end
      → backtrack from (2,1)
    row=3: is_safe(3,1)? Yes ✅ → leads to solution eventually
```

---

### The Backtracking Step

```
board[row][col] = "Q"     ← place queen
solve(col + 1)             ← recurse to next column
board[row][col] = "."     ← UNDO placement (backtrack)
```

After the recursive call returns (either found a solution or dead-ended), we restore the cell to "." so we can try the next row in the same column.

---

### This Problem vs the Optimized Version (Problem 25)

```
This version (24):    scan board during is_safe() → O(N) per check
Optimized (25):       precomputed arrays for rows/diagonals → O(1) per check

The logic is identical — only the safety-check speed differs.
Always understand this version first.
```

---

### Complexity

| | |
|---|---|
| Time | O(N! × N) — N! placements, O(N) safety check each |
| Space | O(N²) — board + O(N) call stack |
