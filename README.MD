# Recursion & Backtracking

Problems organised by pattern — Pick/Not-Pick, Loop + Recurse, Backtrack + Prune, Mark/Unmark. Each solved problem has a `.py` solution and an Algorithm & Intuition `.md` breakdown.

---

## Patterns

When a problem feels confusing, it usually comes down to picking the right pattern.

| Question | YES | NO |
|---|---|---|
| Does order matter? | Permutation — loop from `0` | Combination — loop from `idx` |
| Reuse allowed? | Pass `i` to next call | Pass `i+1` |
| Duplicate input? | Sort + skip `arr[i] == arr[i-1]` | No extra logic |
| Grid problem? | Mark / Unmark (4-dir DFS) | String / sequence recursion |
| Binary choice per element? | Pick / Not-Pick (2 calls) | Loop style (1 call per candidate) |

| Pattern | What it means | Where it appears |
|---|---|---|
| **Pick / Not-Pick** | At each element: include it or skip it. Two recursive calls per level, no loop. | Subsets, subsequences, combo sum I |
| **Loop + Recurse** | `for` loop tries every candidate at this level. One recursive call per candidate. | Combo sum II, permutations, subsets II |
| **Backtrack + Prune** | Loop + Recurse but check validity before recursing. Invalid branch? Don't enter. | N-Queens, Sudoku, palindrome partitioning |
| **Mark / Unmark** | On grids — mark cell visited, recurse in 4 dirs, unmark on return. | Rat in a maze, word search |
| **Divide & Conquer** | Split problem, solve halves independently, combine results. | Merge sort, quick sort |

---

## Problems

### 1 — Basic Recursion

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| 1 | Print name N times | Base case as exit; the recursion template | ✅ |
| 2 | Print 1→N | Print before call → descent order | ✅ |
| 3 | Print N→1 | Post-order trick: recurse first, print on the way back | ✅ |
| 4 | Sum of N numbers | Build-on-return vs accumulator (tail recursion) style | ✅ |
| 5 | Factorial | `n × fact(n-1)`; neutral element is the base case value | ✅ |
| 6 | Reverse array | Two-pointer swap inward; swap is in-place, no extra space | ✅ |
| 7 | Palindrome check | Check pair `(i, n-i-1)`, stop at midpoint | ✅ |
| 8 | Nth Fibonacci | Overlapping subproblems → O(2^N); motivation for memoization | ✅ |
| — | Power(x,n) — O(log n) | | 🔜 |
| — | Binary search recursive | | 🔜 |
| — | Rope cutting | | 🔜 |

### 2 — Subsets & Subsequences

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| 9 | Print all subsequences | Binary include/exclude tree; `result.pop()` is the backtrack | ✅ |
| 10 | Subsequences with sum = k | Same tree, filter at leaf; `curr_sum` (int) needs no pop | ✅ |
| 11 | Single subsequence sum = k | `if recurse(): return True` — prunes entire subtrees on first hit | ✅ |
| 12 | Count subsequences sum = k | Return 1/0 at leaf, sum up; identical tree to DP Count Subsets | ✅ |
| 18 | Subset sums | Pass sum by value → no backtrack; 2^N leaves, sort at end | ✅ |
| 19 | Subsets II (duplicates) | Save at call entry; sort + `i > idx` skip for dedup | ✅ |

### 3 — Combinations

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| 16 | Combination sum I (reuse allowed) | Pick calls same `idx` → unbounded reuse; same as coin change | ✅ |
| 17 | Combination sum II (no reuse) | Sort + skip `arr[i]==arr[i-1]` at same level; `i > idx` not `i > 0` | ✅ |
| — | Combination sum III | | 🔜 |
| — | Letter combinations (LC 17) | | 🔜 |

### 4 — Permutations

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| 20 | Permutations — used[] | Scan full range `(0,n)`, filter by `used[i]`; 3-step backtrack | ✅ |
| 21 | Permutations — swap | Fix element at `idx` via swap; second swap is the undo | ✅ |
| 22 | Permutations II — used[] | `not used[i-1]` prune; subtler than subset dedup | ✅ |
| 23 | Permutations II — swap + seen | Local `seen` set per call; no sorting needed | ✅ |
| — | Next permutation | | 🔜 |

### 5 — Sorting

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| 13 | Merge sort | Work happens on merge, not split; stable; O(N log N) always | ✅ |
| 14 | Quick sort — Lomuto | Last-element pivot; `index` tracks the "small zone" boundary | ✅ |
| 15 | Quick sort — Hoare | Two pointers from both ends; ~3× fewer swaps than Lomuto | ✅ |
| — | Bubble sort recursive | | 🔜 |

### 6 — Backtracking

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| 24 | N-Queens | Place column by column; only scan left in `is_safe` | ✅ |
| 25 | N-Queens (optimised) | O(N)→O(1) safety check via row/diagonal arrays | ✅ |
| 26 | Sudoku solver | Try 1–9 per empty cell; `if solve(): return True` propagation | ✅ |
| 27 | Palindrome partitioning | Prune before recursing; `idx` = start of next unpartitioned piece | ✅ |
| 28 | Rat in a maze | 4-dir DFS; `vis[][]` is path-local, reset on backtrack | ✅ |
| 29 | Rat in a maze (loop variant) | Direction arrays replace 4 hardcoded blocks; trivial to extend to 8 dirs | ✅ |
| 30 | Tower of Hanoi | 3-step recursive trust; roles of pegs swap each call; T(n) = 2^n − 1 | ✅ |
| — | Word search on grid | | 🔜 |
| — | M-coloring graph | | 🔜 |
| — | Knight's tour | | 🔜 |

### 7 — String Recursion

| # | Problem | Key Idea | Status |
|---|---------|----------|--------|
| — | Generate parentheses | Track open/close counts; prune when open > n or close > open | 🔜 |
| — | Restore IP addresses | | 🔜 |
| — | Decode ways | | 🔜 |
| — | Wildcard matching | | 🔜 |

---

## Progress

```
Basic recursion      ████████░░   8/11
Subsets              ██████████   6/6
Combinations         ████░░░░░░   2/4
Permutations         ████████░░   4/5
Sorting              ███████░░░   3/4
Backtracking         ███████░░░   7/10
String recursion     ░░░░░░░░░░   0/4
```