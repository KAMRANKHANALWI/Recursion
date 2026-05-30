## Tower of Hanoi — Algorithm & Intuition

**Problem:** Move N disks from source peg to destination peg using an auxiliary peg. Rules: move one disk at a time, never place a larger disk on a smaller one.

```
n=3, source='A', destination='C', auxiliary='B'

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Total: 7 moves (2^3 - 1)
```

---

### Intuition

**The Dream:** Move all N disks to destination without breaking any rule.

**Key Insight:** To move N disks from source to destination:
1. Move the top N-1 disks from source to auxiliary (using destination as helper)
2. Move the Nth (largest) disk from source to destination
3. Move the N-1 disks from auxiliary to destination (using source as helper)

```
hanoi(n, src, dest, aux):
    if n == 0: return         ← nothing to move
    hanoi(n-1, src, aux, dest)   ← step 1: move n-1 disks out of the way
    print(f"Move disk {n} from {src} to {dest}")  ← step 2: move largest
    hanoi(n-1, aux, dest, src)   ← step 3: move n-1 disks on top
```

---

### Why This Works — The Recursive Trust

```
You don't need to track every disk — just trust the recursion:
  "hanoi(n-1, ...) correctly moves n-1 disks."

Given that trust:
  Step 1: n-1 disks are now on aux. Only the largest disk is on src.
  Step 2: Move largest to dest. Dest now has only the largest disk.
  Step 3: n-1 disks move from aux to dest, landing on top of largest.
  → All n disks are on dest in correct order. ✅
```

---

### Full Recursion Tree — n=3, A→C using B

```
hanoi(3, A, C, B)
├── hanoi(2, A, B, C)          ← move top 2 from A to B
│   ├── hanoi(1, A, C, B)      ← move top 1 from A to C
│   │   └── print: disk1 A→C
│   ├── print: disk2 A→B
│   └── hanoi(1, C, B, A)      ← move top 1 from C to B
│       └── print: disk1 C→B
├── print: disk3 A→C
└── hanoi(2, B, C, A)          ← move top 2 from B to C
    ├── hanoi(1, B, A, C)
    │   └── print: disk1 B→A
    ├── print: disk2 B→C
    └── hanoi(1, A, C, B)
        └── print: disk1 A→C

Output order:
  disk1 A→C
  disk2 A→B
  disk1 C→B
  disk3 A→C   ← the largest move
  disk1 B→A
  disk2 B→C
  disk1 A→C
```

---

### The Minimum Moves Formula

```
T(n) = T(n-1) + 1 + T(n-1)
     = 2·T(n-1) + 1
     = 2^n - 1

n=1: 1 move
n=2: 3 moves
n=3: 7 moves
n=4: 15 moves
n=10: 1023 moves
n=64: 18,446,744,073,709,551,615 moves (~585 billion years at 1 move/second)
```

---

### Why Three Parameters (src, dest, aux)?

```
The roles of src, dest, aux swap at each recursive call.

hanoi(n-1, src, aux, dest):
  ↑ destination becomes auxiliary — we're building a staging area

hanoi(n-1, aux, dest, src):
  ↑ source becomes auxiliary — we're pulling from the staging area

The parameter names are roles, not fixed labels.
Each recursion redefines which peg plays which role.
```

---

### This is the Purest Recursive Problem

```
No data structures. No backtracking. No conditionals except the base case.
The solution IS the recursion — you can't "trace through" it step by step
and arrive at the same insight; you have to TRUST the recursive definition.

Tower of Hanoi is often used to teach:
  - Recursion as problem decomposition
  - Mathematical induction (proof that T(n)=2^n-1)
  - That recursion can solve things iteration finds very hard to express
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N) — exactly 2^N - 1 moves |
| Space | O(N) — call stack depth |
