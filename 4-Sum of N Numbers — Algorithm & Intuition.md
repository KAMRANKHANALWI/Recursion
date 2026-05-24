## Sum of N Numbers — Algorithm & Intuition

**Problem:** Find the sum 1 + 2 + ... + N using recursion.

```
sum_of_n(5) → 15
```

---

### Intuition

**The Dream:** Add N numbers without a loop.

**Key Insight:** Two fundamentally different recursive styles exist for this problem — each teaches something important about how recursion returns values.

---

### Approach 1 — Build on Return (Classic Recursion)

```
def sum_of_n(n):
    if n == 0: return 0         ← base: nothing left to add
    return n + sum_of_n(n-1)   ← current + sum of rest
```

```
Expansion (call stack builds up):
  sum(5) = 5 + sum(4)
         = 5 + (4 + sum(3))
         = 5 + (4 + (3 + sum(2)))
         = 5 + (4 + (3 + (2 + sum(1))))
         = 5 + (4 + (3 + (2 + (1 + sum(0)))))
         = 5 + (4 + (3 + (2 + (1 + 0))))

Contraction (returning):
  = 5 + (4 + (3 + (2 + 1)))
  = 5 + (4 + (3 + 3))
  = 5 + (4 + 6)
  = 5 + 10
  = 15 ✅
```

The answer is built **on the way back up**. Each frame adds `n` to whatever came from below.

---

### Approach 2 — Accumulator (Tail Recursion Style)

```
def sum_of_n(n, total=0):
    if n == 0: return total    ← base: total holds the answer
    return sum_of_n(n-1, total + n)   ← pass running sum forward
```

```
Dry run: (5,0) → (4,5) → (3,9) → (2,12) → (1,14) → (0,15) → return 15

Each call passes the answer forward — no waiting needed.
```

---

### Classic vs Accumulator — The Core Difference

```
Classic (build on return):
  Answer assembled AFTER reaching base case, on the way back.
  Each stack frame holds a pending "n +" operation.
  NOT tail-recursive → stack frames can't be reused.

Accumulator (tail recursion):
  Answer passed FORWARD via `total` parameter.
  Base case directly returns the answer — no pending work.
  IS tail-recursive → compilers can optimize to O(1) stack.
  Python doesn't optimize TCO, but the pattern is still valuable.
```

---

### Why This Matters for DP

```
The "build on return" pattern:
  return n + sum_of_n(n-1)
  ↑ this is exactly how Fibonacci and other DP problems work.
  Each call contributes to the answer that comes back up.

The accumulator pattern:
  return sum_of_n(n-1, total + n)
  ↑ this is iterative thinking in recursive form.
  Used in tail-recursive optimization and functional programming.
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Classic | O(N) | O(N) — pending additions on stack |
| Accumulator | O(N) | O(N) — Python doesn't do TCO |