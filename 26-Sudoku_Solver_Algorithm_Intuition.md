## Sudoku Solver — Algorithm & Intuition

**Problem:** Fill a 9×9 Sudoku board (partially filled, empty cells = ".") so that every row, column, and 3×3 box contains digits 1–9 exactly once.

---

### Intuition

**The Dream:** Fill every empty cell with the right digit.

**Key Insight:** Try digits 1–9 at each empty cell. If a digit is valid (doesn't violate any Sudoku rule), place it and recurse to the next empty cell. If no digit works, backtrack and try a different digit in the previous cell.

```
solve() scans for the next empty cell.
For that cell, try '1' through '9'.
If valid → place it, recurse.
  If recursion succeeds → done (propagate True up).
  If recursion fails → unplace it, try next digit.
If no digit works → return False (trigger backtrack in parent).
If no empty cell found → board complete → return True.
```

---

### The Recursive Logic

```
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":         ← find next empty cell
                for c in '123456789':
                    if is_valid(board, i, j, c):
                        board[i][j] = c    ← try digit
                        if solve(board):   ← recurse
                            return True    ← success! propagate up
                        board[i][j] = "." ← backtrack: undo digit
                return False               ← no digit worked → fail
    return True                            ← no empty cell → solved!
```

---

### The Validity Check

```
def is_valid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:    ← column conflict
            return False
        if board[row][i] == c:    ← row conflict
            return False
        # 3×3 box check:
        box_row = 3 * (row // 3) + i // 3
        box_col = 3 * (col // 3) + i % 3
        if board[box_row][box_col] == c:
            return False
    return True
```

---

### The 3×3 Box Index Formula

```
Row of top-left corner of box:  3 * (row // 3)
Col of top-left corner of box:  3 * (col // 3)

Offset within box using i from 0..8:
  row_offset = i // 3  → 0,0,0,1,1,1,2,2,2
  col_offset = i % 3   → 0,1,2,0,1,2,0,1,2

So: board[3*(row//3) + i//3][3*(col//3) + i%3]
    visits all 9 cells in the box as i goes 0→8.
```

---

### The "Return True Propagation" Pattern

```
if solve(board):
    return True
board[i][j] = "."

This is the crucial backtracking chain:

- If inner solve() returns True → outer solve() also returns True.
- The True propagates all the way back to the first call.
- Once True is returned, NO more backtracking happens.
- The board retains its final solved state.

If we didn't check `if solve(): return True`:
  We'd backtrack even after finding the solution → empty the board!
```

---

### Backtracking Visualized (Small Scale)

```
Empty cell at (0,2):
  Try '1': invalid (row conflict) → skip
  Try '2': valid → place '2', recurse
    Empty cell at (0,5):
      Try '1': valid → place '1', recurse
        ... → eventually dead end → return False
      Try '2': ... → dead end → return False
      ...
      Try '9': → dead end → return False
    All digits failed at (0,5) → return False
  Backtrack: board[0][2] = '.'
  Try '3': valid → place '3', recurse
    ... → eventually leads to solution
```

---

### Complexity

| | |
|---|---|
| Time | O(9^M) where M = number of empty cells (at most 81) |
| Space | O(M) — recursion stack depth (one frame per empty cell) |

In practice much faster due to constraint propagation via `is_valid`.
