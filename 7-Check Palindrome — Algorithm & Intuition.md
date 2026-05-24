## Check Palindrome — Algorithm & Intuition

**Problem:** Check if a string is a palindrome using recursion — reads the same forwards and backwards.

```
"MaDAm" → True   (case-insensitive)
"hello" → False
```

---

### Intuition

**The Dream:** Compare the string against itself without reversing it.

**Key Insight:** A palindrome has matching outermost characters. Check the pair at index `i` and its mirror `n-i-1`. Move inward until the middle — if all pairs match, it's a palindrome.

```
"madam"
  m == m ✅  →  check "ada"
    a == a ✅  →  check "d"
      d (middle) → i >= n//2 → True ✅
```

---

### The Recursive Logic

```
def check_palindrome(s, i):
    s = s.lower()           ← normalize case
    n = len(s)

    if i >= n // 2:         ← passed the middle → all pairs matched
        return True

    if s[i] != s[n-i-1]:   ← mismatch found
        return False

    return check_palindrome(s, i+1)   ← check next inner pair
```

---

### Dry Run — `"MaDAm"`

```
s = "madam", n=5

i=0: s[0]='m' == s[4]='m' ✅ → recurse(i=1)
i=1: s[1]='a' == s[3]='a' ✅ → recurse(i=2)
i=2: i=2 >= n//2=2 → return True ✅
```

---

### Dry Run — `"hello"`

```
s = "hello", n=5

i=0: s[0]='h' != s[4]='o' ❌ → return False immediately
```

---

### Why `i >= n // 2`?

```
Even length "abba" (n=4):
  Check pairs: (0,3), (1,2)
  n//2 = 2 → stop at i=2 ✅

Odd length "madam" (n=5):
  Check pairs: (0,4), (1,3)
  Middle index 2 has no partner → skip it
  n//2 = 2 → stop at i=2 ✅

>= handles both: once i reaches the midpoint, all outer pairs are verified.
```

---

### Early Termination

```
The function returns False immediately on the first mismatch.
No need to check the rest of the string.

This is the "short-circuit" pattern in recursion:
  if bad_condition: return False
  return recurse(...)

The recursive call only happens if the current check passes.
```

---

### Palindrome vs Reverse Array

```
Both use the same two-pointer idea (i and n-i-1).
Reverse Array: swaps the pair.
Palindrome:    checks the pair.
```

---

### Complexity

| | |
|---|---|
| Time | O(N/2) = O(N) |
| Space | O(N/2) — call stack depth |