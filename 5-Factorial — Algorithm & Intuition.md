## Factorial — Algorithm & Intuition

**Problem:** Compute N! = N × (N-1) × ... × 1 using recursion.

```
factorial(5) → 120   (5 × 4 × 3 × 2 × 1)
```

---

### Intuition

**The Dream:** Multiply N numbers without a loop.

**Key Insight:** N! is just N multiplied by (N-1)!. A big problem defined in terms of a slightly smaller version of itself — the essence of recursion.

```
factorial(n) = n × factorial(n-1)
factorial(0) = 1   ← base case (empty product = 1)
```

---

### Call Stack Visualization

```
factorial(5)
= 5 × factorial(4)
= 5 × (4 × factorial(3))
= 5 × (4 × (3 × factorial(2)))
= 5 × (4 × (3 × (2 × factorial(1))))
= 5 × (4 × (3 × (2 × (1 × factorial(0)))))
= 5 × (4 × (3 × (2 × (1 × 1))))   ← base case hit

Unwind:
= 5 × (4 × (3 × (2 × 1)))
= 5 × (4 × (3 × 2))
= 5 × (4 × 6)
= 5 × 24
= 120 ✅
```

---

### Why `factorial(0) = 1`?

```
Mathematical convention: empty product = 1 (neutral element of multiplication)

Practically: without this base case, factorial(-1) → factorial(-2) → ...
             infinite recursion → stack overflow.

The base case 0 is chosen because 0! = 1 is well-defined
and it's the natural stopping point (factorial isn't defined for negatives).
```

---

### Factorial vs Sum — Structural Comparison

```
sum(n)       = n + sum(n-1)   base: sum(0)=0
factorial(n) = n × fact(n-1)  base: fact(0)=1

Identical recursive structure.
Only the operator (+ vs ×) and base value (0 vs 1) differ.
The neutral element of the operation IS the base case value.
```

---

### Complexity

| | |
|---|---|
| Time | O(N) — N multiplications |
| Space | O(N) — N frames on call stack |

For large N (e.g., N=10000), Python hits recursion limit. Iterative or `math.factorial()` preferred in production.