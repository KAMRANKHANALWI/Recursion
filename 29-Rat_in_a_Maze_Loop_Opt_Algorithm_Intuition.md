## Rat in a Maze — Loop Optimized — Algorithm & Intuition

**Problem:** Same as problem 28 — but replace the four hardcoded direction blocks with a direction array loop.

---

### Intuition

**The Dream:** Same result as problem 28, cleaner code.

**Key Insight:** The four directions (D, L, R, U) are just offsets. Store them in arrays and loop over them — identical logic, far less repetition.

---

### The Direction Arrays

```
     D    L    R    U
di = [+1,  0,   0,  -1]   ← row offset
dj = [ 0, -1,  +1,   0]   ← col offset
dir = "DLRU"               ← matching character
```

```
For direction idx:
  nexti = i + di[idx]
  nextj = j + dj[idx]
  move  += dir[idx]
```

---

### Refactored Loop

```
def solve(i, j, move):
    if i == n-1 and j == n-1:
        res.append(move)
        return

    for idx in range(4):
        nexti = i + di[idx]
        nextj = j + dj[idx]

        if (0 <= nexti < n and 0 <= nextj < n
                and not vis[nexti][nextj]
                and maze[nexti][nextj] == 1):

            vis[i][j] = 1                         ← mark CURRENT cell
            solve(nexti, nextj, move + dir[idx])
            vis[i][j] = 0                         ← unmark CURRENT cell
```

---

### Subtle Difference — Which Cell Gets Marked?

```
Problem 28 (explicit):   marks vis[ni][nj] = 1  (next cell)
Problem 29 (loop opt):   marks vis[i][j]   = 1  (current cell)

Are these equivalent?

Problem 28:
  Before entering (ni,nj): mark (ni,nj)
  After returning: unmark (ni,nj)

Problem 29:
  Before recursing INTO (ni,nj): mark (i,j) [current]
  After returning: unmark (i,j)

Both prevent revisiting cells already in the current path.
The difference: in problem 29, (0,0) needs special handling
(it's the start, nobody marks it from outside).

In practice for this maze problem both work because:
  - The start (0,0) is always the origin and only entered once.
  - Marking current before recursing next = "you can't come back to me."
  - Marking next before entering next  = "next is now blocked to others."

Both correctly prevent cycles. The implementation in problem 29 is
slightly different but logically equivalent for this problem.
```

---

### The Loop Advantage

```
Problem 28 — 4 separate blocks:
  # down
  if i+1 < n and not vis[i+1][j] and maze[i+1][j]==1:
      vis[i+1][j] = 1
      solve(i+1, j, move+"D")
      vis[i+1][j] = 0

  # left
  if j-1 >= 0 and not vis[i][j-1] and maze[i][j-1]==1:
      ...

  # right ... # up ...

Problem 29 — one loop:
  for idx in range(4):
      ni, nj = i + di[idx], j + dj[idx]
      if 0 <= ni < n and 0 <= nj < n and not vis[ni][nj] and maze[ni][nj]==1:
          vis[i][j] = 1
          solve(ni, nj, move + dir[idx])
          vis[i][j] = 0

Same logic. 4× less code. Easy to extend to 8 directions (add diagonal offsets).
```

---

### Adding More Directions — O(1) Code Change

```
# 8-directional maze (add diagonals):
di  = [+1, 0,  0, -1, +1, +1, -1, -1]
dj  = [ 0, -1, +1, 0, +1, -1, +1, -1]
dir = "DLRUABCD"   ← name the diagonals

Loop body unchanged — just di/dj get 4 more entries.
```

---

### Complexity

| | |
|---|---|
| Time | O(4^(N²)) — same as problem 28 |
| Space | O(N²) — visited matrix + call stack |

This version has the same asymptotic complexity — the loop optimization is a code quality improvement, not a performance one.
