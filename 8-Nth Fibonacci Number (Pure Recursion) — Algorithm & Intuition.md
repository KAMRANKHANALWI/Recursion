## Nth Fibonacci Number (Pure Recursion) — Algorithm & Intuition

**Problem:** Find the Nth Fibonacci number using plain recursion.

```
fibonacci(6) → 8   (0,1,1,2,3,5,8)
```

---

### Intuition

**The Dream:** Express fib(n) directly in terms of smaller Fibonacci numbers.

**Key Insight:** fib(n) depends on exactly two smaller subproblems — fib(n-1) and fib(n-2). Two base cases handle the smallest inputs.

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
```

---

### The Problem — Exponential Blowup

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2) ← recomputed
│   │   └── fib(1)
│   └── fib(2)     ← recomputed
└── fib(3)         ← recomputed
    ├── fib(2)     ← recomputed again
    └── fib(1)
```

fib(2) computed 3 times, fib(3) twice. Time = O(2^N).

This is **why memoization exists** — the pure recursive version is the motivation for DP.

---

### Call Tree — fib(4)

```
                fib(4)
              /        \
          fib(3)       fib(2)
          /    \        /   \
       fib(2) fib(1) fib(1) fib(0)
       /    \
    fib(1) fib(0)

Leaves:  1, 1, 1, 0, 1, 0   → sum up = 3 ✅
```

---

### Two Base Cases — Why Both?

```
fib(1) = 1:  Without this, fib(2) = fib(1)+fib(0) would call fib(0)+fib(-1)
             fib(-1) is undefined → infinite recursion.

fib(0) = 0:  The sequence starts at 0.

Both are needed because the recurrence reduces by 1 AND by 2.
You need to cover both bottom cases.
```

---

### This Problem vs the DP Version

```
Pure Recursion (this file):   O(2^N) time — every subproblem recomputed
Memoization (DP repo #1):    O(N) time — cache results
Tabulation (DP repo #1):     O(N) time, O(N) space
Space Optimized (DP repo #1): O(N) time, O(1) space

This file shows WHY you need DP.
The exponential tree is the motivation — memoization just adds a cache.
```

---

### Complexity

| | |
|---|---|
| Time | O(2^N) — exponential, overlapping subproblems |
| Space | O(N) — maximum call stack depth |