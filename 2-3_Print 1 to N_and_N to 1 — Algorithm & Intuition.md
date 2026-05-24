## Print 1 to N / N to 1 — Algorithm & Intuition

**Problem:** Print numbers 1 to N and N to 1 using recursion.

```
one_to_n(1, 5) → 1 2 3 4 5
n_to_one(5)    → 5 4 3 2 1
```

---

### Intuition

**The Dream:** Count up (or down) without a loop.

**Key Insight:** The only difference between printing 1→N and N→1 is **when you print relative to the recursive call** — before (pre-order) or after (post-order).

---

### 1 to N — Print Before Recursing

```
def one_to_n(i, n):
    if i > n: return        ← base case
    print(i)                ← print FIRST
    one_to_n(i+1, n)        ← then recurse

Call stack:
  one_to_n(1,5): print 1, call(2,5)
  one_to_n(2,5): print 2, call(3,5)
  one_to_n(3,5): print 3, call(4,5)
  one_to_n(4,5): print 4, call(5,5)
  one_to_n(5,5): print 5, call(6,5)
  one_to_n(6,5): i>n → return
Output: 1 2 3 4 5 ✅
```

---

### N to 1 — Print Before Recursing (Counting Down)

```
def n_to_one(n):
    if n == 0: return       ← base case
    print(n)                ← print FIRST (at current n)
    n_to_one(n-1)           ← recurse with smaller n

Call stack:
  n_to_one(5): print 5, call(4)
  n_to_one(4): print 4, call(3)
  ...
  n_to_one(1): print 1, call(0)
  n_to_one(0): return
Output: 5 4 3 2 1 ✅
```

---

### The Pre-Order vs Post-Order Trick

```
Want 1→N with only ONE parameter (no i)?

def one_to_n_trick(n):
    if n == 0: return
    one_to_n_trick(n-1)     ← recurse FIRST (go to base case)
    print(n)                ← print AFTER returning (post-order)

Call stack unwinds:
  call(5) → call(4) → call(3) → call(2) → call(1) → call(0) → return
  ← print 1
  ← print 2
  ← print 3
  ← print 4
  ← print 5
Output: 1 2 3 4 5 ✅ (printing happens on the way BACK)
```

This is the most important insight in early recursion:
- **Print before call** → process in descent order
- **Print after call** → process in ascent order (reverse)

---

### The Four Patterns

```
Want N→1:  print before call, count down  ← n_to_one(n)
Want 1→N:  print before call, count up    ← one_to_n(i, n)
Want 1→N:  print after call,  count down  ← post-order trick
Want N→1:  print after call,  count up    ← post-order reverse trick
```

---

### Complexity

| | |
|---|---|
| Time | O(N) — one call per number |
| Space | O(N) — call stack depth |