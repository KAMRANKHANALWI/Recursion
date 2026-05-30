## Palindrome Partitioning — Algorithm & Intuition

**Problem:** Given a string, return all ways to partition it such that every substring in the partition is a palindrome.

```
s = "aabb"
→ [["a","a","b","b"], ["a","a","bb"], ["aa","b","b"], ["aa","bb"]]
```

---

### Intuition

**The Dream:** Every possible way to split the string into all-palindrome pieces.

**Key Insight:** At each index `idx`, try every possible first piece `s[idx..i]`. If it's a palindrome, take it, and recurse on the rest `s[i+1:]`. If not a palindrome, skip — no point going further with an invalid piece.

```
Pruning: only recurse when s[idx..i] is a palindrome.
This is what differentiates this from plain partition-all-ways.
```

---

### The Code

```
def backtrack(idx, path):
    if idx == len(s):               ← consumed entire string
        res.append(list(path))      ← valid partition found
        return

    for i in range(idx, len(s)):
        if is_palindrome(s, idx, i):   ← try substring s[idx..i]
            path.append(s[idx:i+1])
            backtrack(i + 1, path)     ← recurse on remaining string
            path.pop()                 ← backtrack
```

---

### Recursion Tree — `s = "aabb"`

```
backtrack(0, [])
  i=0: "a"  ✓ palindrome → path=["a"]
    i=1: "a"  ✓ → path=["a","a"]
      i=2: "b"  ✓ → path=["a","a","b"]
        i=3: "b"  ✓ → path=["a","a","b","b"] ← idx=4=len → SAVE ✅
      i=3: "bb" ✓ → path=["a","a","bb"] ← idx=4 → SAVE ✅
    i=2: "ab" ✗ → skip
    i=3: "abb" ✗ → skip
  i=1: "aa" ✓ → path=["aa"]
    i=2: "b"  ✓ → path=["aa","b"]
      i=3: "b"  ✓ → SAVE ["aa","b","b"] ✅
    i=3: "bb" ✓ → SAVE ["aa","bb"] ✅
  i=2: "aab" ✗ → skip
  i=3: "aabb" ✗ → skip
```

---

### The Palindrome Check

```
def is_palindrome(s, l, r):
    while l <= r:
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True
```

Two-pointer check — O(length of substring). Called at each (idx, i) pair.

---

### Key Pattern — Pruning via Condition Before Recursing

```
Standard backtracking:
  for i in range(idx, n):
      pick s[idx..i]
      recurse
      unpick

Palindrome partitioning:
  for i in range(idx, n):
      if is_palindrome(s, idx, i):    ← PRUNE: only recurse if valid
          pick s[idx..i]
          recurse
          unpick

This is different from filtering at the BASE CASE.
Early pruning avoids entire subtrees that can never lead to a solution.
```

---

### Why `idx` Always Points to "Start of Next Piece"

```
At each call, s[0..idx-1] is already partitioned (stored in path).
s[idx..n-1] is the remaining unpartitioned string.

The for-loop tries all possible lengths for the NEXT piece.
When idx == len(s), nothing is left → full partition stored.
```

---

### Complexity

| | |
|---|---|
| Time | O(N × 2^N) — up to 2^N partitions, O(N) palindrome check each |
| Space | O(N) — call stack depth + path list |
