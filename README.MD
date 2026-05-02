# Recursion & Backtracking

Problems organised by pattern — Pick/Not-Pick, Loop + Recurse, Backtrack + Prune, Mark/Unmark, and Lexicographic/Trie-style. Solved while going through recursion systematically.

---

## Problems

### 1 — Basic Recursion

| Problem | Status |
|---|---|
| Print 1→N, N→1 | ✅ |
| Factorial | ✅ |
| Fibonacci (nth) | ✅ |
| Reverse array | ✅ |
| Palindrome check | ✅ |
| Sum of N numbers | ✅ |
| Memo vs Generate | ✅ |
| Power(x, n) — O(log n) | 🔜 |
| Binary search recursive | 🔜 |
| Rope cutting | 🔜 |

### 2 — Subsets & Subsequences

| Problem | Status |
|---|---|
| All subsequences | ✅ |
| Subsequences with sum = k | ✅ |
| Single subsequence sum = k | ✅ |
| Count subsequences sum = k | ✅ |
| Subsets sum | ✅ |
| Subsets II (duplicates) | ✅ |

### 3 — Combinations

| Problem | Status |
|---|---|
| Combination sum I (reuse allowed) | ✅ |
| Combination sum II (no reuse) | ✅ |
| Coin combination | ✅ |
| Keypad combinations | ✅ |
| Combination sum III | 🔜 |
| Letter combinations — LC 17 | 🔜 |

### 4 — Permutations

| Problem | Status |
|---|---|
| Permutations (pick approach) | ✅ |
| Permutations (swap approach) | ✅ |
| Permutations II — duplicates | ✅ |
| Permutations II — swap + dup | ✅ |
| String permutations | ✅ |
| String permutations — dups | ✅ |
| Coin permutation | ✅ |
| Next permutation | 🔜 |

### 5 — Sorting

| Problem | Status |
|---|---|
| Merge sort | ✅ |
| Quick sort — Lomuto | ✅ |
| Quick sort — Hoare | ✅ |
| Bubble sort recursive | 🔜 |

### 6 — Backtracking

| Problem | Status |
|---|---|
| N-Queens | ✅ |
| N-Queens (optimised) | ✅ |
| Sudoku solver | ✅ |
| Palindrome partitioning | ✅ |
| Rat in a maze | ✅ |
| Rat in a maze (loop variant) | ✅ |
| Tower of Hanoi | ✅ |
| Board path | ✅ |
| Maze path | ✅ |
| Rat chases cheese | ✅ |
| Word search on grid | 🔜 |
| M-coloring graph | 🔜 |
| Knight's tour | 🔜 |

### 7 — String Recursion

| Problem | Status |
|---|---|
| Generate parentheses | ✅ |
| Lexicographic numbers | ✅ |
| Coin toss — all sequences | ✅ |
| No consecutive heads | ✅ |
| Restore IP addresses | 🔜 |
| Decode ways | 🔜 |
| Wildcard matching | 🔜 |

---

## Progress

```
Basic recursion      ██████░░░░   7/10
Subsets              ██████████   6/6
Combinations         ████████░░   4/6
Permutations         █████████░   7/8
Sorting              ███████░░░   3/4
Backtracking         ███████░░░   10/13
String recursion     █████░░░░░   4/7
```

---

## Patterns

Each group above maps to one of these patterns. When a problem feels confusing, it usually comes down to picking the right one.

| Question | YES | NO |
|---|---|---|
| Does order matter? | Permutation — loop from `0` | Combination — loop from `idx` |
| Reuse allowed? | Pass `i` to next call | Pass `i+1` |
| Duplicate input? | Sort + skip `arr[i] == arr[i-1]` | No extra logic |
| Grid problem? | Mark / Unmark (4-dir DFS) | String recursion |
| Binary choice per element? | Pick / Not-Pick | Loop style |

| Pattern | What it means | Where it's used |
|---|---|---|
| **Pick / Not-Pick** | At each element: take it or skip it. Two recursive calls per level. | Subsets, subsequences, combo sum |
| **Loop + Recurse** | `for` loop tries every candidate at this level. Next iteration handles the skip — no second call needed. | Combo sum II, permutations |
| **Backtrack + Prune** | Same as loop + recurse but check validity before going deeper. Invalid? Don't enter that branch. | Generate parentheses, N-Queens, Sudoku |
| **Mark / Unmark** | On grids — mark the cell visited, recurse in 4 directions, unmark on the way back. | Rat in a maze, word search |
| **Lexicographic / Trie-style** | Treat numbers like a trie: `1` branches into `10, 11, 12...`. DFS on that trie gives lex order naturally. | Lexicographic numbers, keypad |