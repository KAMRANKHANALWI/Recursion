## Print Name N Times — Algorithm & Intuition

**Problem:** Print a name exactly 5 times using recursion — no loops.

```
print_name("Kamran") →
Kamran
Kamran
Kamran
Kamran
Kamran
```

---

### Intuition

**The Dream:** Do something N times without a for-loop.

**Key Insight:** Recursion replaces iteration by passing a counter. Each call does the work once and delegates the rest to the next call.

```
print_name("Kamran", count=0)
  print "Kamran"
  print_name("Kamran", count=1)
    print "Kamran"
    print_name("Kamran", count=2)
      ...
        print_name("Kamran", count=5) → BASE CASE → return
```

---

### The Base Case

```
if count == 5: return

Without this, the function recurses forever → stack overflow.
The base case is the exit condition — every recursive function must have one.
```

---

### Call Stack Visualization

```
Frame 1: count=0 → print, call(1)
Frame 2: count=1 → print, call(2)
Frame 3: count=2 → print, call(3)
Frame 4: count=3 → print, call(4)
Frame 5: count=4 → print, call(5)
Frame 6: count=5 → BASE CASE → return
← Frame 6 pops
← Frame 5 pops
← Frame 4 pops
...
← Frame 1 pops
```

All printing happens **before** the recursive call — this is a "pre-order" pattern.

---

### This Establishes the Recursion Template

```
def recursive_function(params):
    if base_case:           ← 1. When to stop
        return

    do_work()               ← 2. Work at this level

    recursive_function(     ← 3. Smaller subproblem
        updated_params
    )
```

Every recursion problem maps to this template. The only things that change are what the base case is, what the work is, and how params shrink.

---

### Complexity

| | |
|---|---|
| Time | O(N) — N recursive calls |
| Space | O(N) — N frames on call stack |