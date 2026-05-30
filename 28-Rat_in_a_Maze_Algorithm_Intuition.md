## Rat in a Maze — Algorithm & Intuition

**Problem:** A rat starts at (0,0) in an N×N grid. Cells with value 1 are open, 0 are blocked. Find all paths from (0,0) to (N-1,N-1) moving in 4 directions (D,L,R,U), never revisiting a cell.

```
maze = [[1,0,0,0],    →  paths: ["DDRDRR", "DRDDRR"]
        [1,1,0,1],       (depends on maze structure)
        [1,1,0,0],
        [0,1,1,1]]
```

---

### Intuition

**The Dream:** Find every route from start to end without getting stuck or revisiting.

**Key Insight:** At each cell, try all 4 directions. Mark the current cell as visited so you don't revisit it. If you reach the destination, save the path. After exploring, unmark (backtrack) to let other paths use this cell.

---

### The Three Guards Before Each Move

```
For each direction (e.g., down: i+1, j):

1. In bounds:    i+1 < n and j >= 0, etc.
2. Not visited:  vis[i+1][j] == 0
3. Open cell:    maze[i+1][j] == 1

All three must pass → only then move there.
```

---

### The Code Structure

```
def solve(i, j, move):
    if i == n-1 and j == n-1:
        res.append(move)    ← destination reached, save path
        return

    for each direction (di, dj, char):
        ni, nj = i+di, j+dj
        if valid(ni, nj) and not vis[ni][nj] and maze[ni][nj]==1:
            vis[ni][nj] = 1          ← mark next cell
            solve(ni, nj, move+char) ← recurse from next cell
            vis[ni][nj] = 0          ← unmark (backtrack)
```

---

### Why Mark Before Recursing, Not After?

```
vis[ni][nj] = 1
solve(ni, nj, ...)
vis[ni][nj] = 0

We mark (ni,nj) BEFORE recursing because the recursive call
might try to revisit (ni,nj) from a different direction.
Marking prevents cycles.

After the call returns, we unmark so OTHER paths (from the current
backtracking branch) can use (ni,nj) if they approach from a different route.
```

---

### DLRU Ordering

```
The code tries directions in this fixed order:
  D (down),  L (left),  R (right),  U (up)

This determines which paths appear first in the result list.
The order is alphabetical — standard for this problem.

DLRU alphabetical: D < L < R < U ✅
```

---

### Visited Matrix — Why Needed

```
Without vis[][]:
  The rat could cycle: right→left→right→left → infinite loop

vis[][] prevents revisiting cells already in the CURRENT path.
After backtracking, vis is reset → other paths can use those cells.

This is different from a "globally visited" marker (like BFS).
Here, vis tracks cells in the CURRENT exploration path only.
```

---

### Dry Run — Small 3×3 Maze

```
maze = [[1,0,1],
        [1,1,1],
        [0,0,1]]

solve(0,0,"")
  Down to (1,0): vis[1][0]=1, solve(1,0,"D")
    Down to (2,0): maze[2][0]=0 → blocked
    Left: j-1<0 → out of bounds
    Right to (1,1): vis[1][1]=1, solve(1,1,"DR")
      Right to (1,2): vis[1][2]=1, solve(1,2,"DRR")
        Up to (0,2): vis[0][2]=1, solve(0,2,"DRRU")
          → no valid moves from (0,2) except right→OOB, up→OOB
          → backtrack
        Down to (2,2): vis[2][2]=1 → destination! save "DRRDR"... 
          wait maze[2][2]=1, i=2=n-1, j=2=n-1 → save "DRRDR" ✅
```

---

### Rat in Maze vs N Queens vs Sudoku

```
All three are constraint-satisfaction backtracking problems.

N Queens:  one queen per column, check attacks
Sudoku:    one digit per empty cell, check rows/cols/boxes
Rat Maze:  one step per direction, check bounds/visited/open

All three: try → check → recurse → undo (backtrack)
The constraint check is what varies.
```

---

### Complexity

| | |
|---|---|
| Time | O(4^(N²)) — 4 choices at each of N² cells, worst case |
| Space | O(N²) — visited matrix + O(N²) call stack |
