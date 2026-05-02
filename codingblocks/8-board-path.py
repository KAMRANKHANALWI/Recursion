# ══════════════════════════════════════════════════════════
#   BOARD PATH — Find All Paths from 0 to N
# ══════════════════════════════════════════════════════════

# ── PROBLEM STATEMENT ──────────────────────────────────────
# You are standing on a 1D board at position 0.
# You need to reach position N.
# At each step you can jump forward 1, 2, or 3 positions.
# Print ALL possible paths (sequences of jumps) to reach N.
#
# Constraints:
#   1 <= N <= 10
#   You can ONLY move forward (no backward steps)
#   You must land EXACTLY on N (not overshoot)

# // ┌───┬───┬───┬───┐
# // │ 0 │ 1 │ 2 │ 3 │
# // └───┴───┴───┴───┘
# //   ↑            ↑
# // start       end(n=3)

# ══════════════════════════════════════════════════════════
#   EXAMPLES
# ══════════════════════════════════════════════════════════

# ? Input:  n = 3
# ! Output:
# !   111   (jump 1 → 1 → 1)
# !   12    (jump 1 → 2)
# !   21    (jump 2 → 1)
# !   3     (jump 3 directly)

# ? Input:  n = 2
# ! Output:
# !   11    (jump 1 → 1)
# !   2     (jump 2 directly)

# ? Input:  n = 1
# ! Output:
# !   1     (only one way)

# * ══════════════════════════════════════════════════════════
# *   CODE: board_path(idx, n, ans)
# * ══════════════════════════════════════════════════════════

def board_path(idx, n, ans=""):

    # BASE CASE 1: exactly reached destination
    if idx == n:
        print(ans)
        return

    # BASE CASE 2: overshot, prune this branch
    if idx > n:
        return

    # try all 3 possible jumps from current position
    for i in range(1, 4):
        board_path(idx + i, n, ans + str(i))

board_path(0, 3, "")

def board_path2(n, idx, ans):
    if idx == n:
        print(ans)
        return
    
    if idx > n:
        return
    
    for i in range(1, n+1):
        board_path2(n, idx + i, ans + str(i))
        
board_path2(3, 0, "")

# * ══════════════════════════════════════════════════════════
# *   DRY RUN: n = 3
# * ══════════════════════════════════════════════════════════

# ==                   board_path(0, 3, "")
# ==                  /          |          \
# ==                +1          +2           +3
# ==                 |           |            |
# ==            bp(1,3,"1")  bp(2,3,"2")  bp(3,3,"3")
# ==           /    |    \       /    \         |
# ==         +1   +2   +3     +1    +2        PRINT
# ==          |    |    |      |      |        "3" ✅
# ==      bp(2) bp(3) bp(4) bp(3) bp(4)
# ==       /\     |    |      |     |
# ==      +1 +2  PRINT ❌   PRINT  ❌
# ==       |   |  "12"✅   "21"✅
# ==      bp(3) bp(4)
# ==        |     |
# ==      PRINT   ❌
# ==      "111"✅
# ==
# == Final output order: 111 → 12 → 21 → 3

# * ══════════════════════════════════════════════════════════
# *   APPROACH
# * ══════════════════════════════════════════════════════════

# ## RECURSION + PRUNING
# ^^ At every cell you have 3 choices — try all, keep valid, prune overshots
# ^^ This is literally a DFS on an implicit tree

# * ══════════════════════════════════════════════════════════
# *   EDGE CASES
# * ══════════════════════════════════════════════════════════

# ~  n = 1  → only "1" is valid
# ~  n = 0  → curr == n immediately → prints "" (empty path)
# ~  n = 10 → ≈274 paths, very slow without DP
# ~  What if jumps were 1-6 (dice)? → range(1, 7)
# ~  What if we only COUNTED paths? → return int, use DP

# * ══════════════════════════════════════════════════════════
# *   COMPLEXITY
# * ══════════════════════════════════════════════════════════

# $  Time:  O(3^n)  — 3 branches at each of n levels
# $  Space: O(n)    — recursion stack depth = n
# $
# $  With memoization (count only):
# $  Time:  O(n)    — each subproblem solved once
# $  Space: O(n)    — dp array of size n+1

# * ══════════════════════════════════════════════════════════
# *   BONUS: COUNT PATHS WITH DP (Tribonacci)
# * ══════════════════════════════════════════════════════════

# == dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# == Same problem, just COUNT — no printing needed

def count_paths(n):
    dp = [0] * (n + 1)
    dp[0] = 1               # ? 1 way to be at start

    for i in range(1, n+1):
        for jump in range(1, 4):
            if i - jump >= 0:
                dp[i] += dp[i - jump]

    return dp[n]

# ! n=3 → dp = [1, 1, 2, 4]  → answer = 4 paths
# ! n=4 → dp = [1, 1, 2, 4, 7]

# WHY MEMOIZATION FAILS HERE:
# the function has NO return value — it just prints
# ans is different for every call even at the same idx
# memo key would need (idx, ans) → defeats the purpose

# ~ Example: reaching idx=2 can happen via:
# ~   ans="11"  → board_path(2, 3, "11")
# ~   ans="2"   → board_path(2, 3, "2")
# ~ same idx, completely different ans → can't cache!

# ^^ RULE: memoization only works when the subproblem
# ^^ depends ONLY on idx (not on the path taken to get there)

# ^^ That's only true when you're COUNTING paths, not PRINTING them

# * The core difference:

# * PRINT version → ans changes every call → NO memo possible
# * COUNT version → only idx matters       → memo works perfectly

# $  Without memo: O(3^n)
# $  With memo:    O(n)    ← each idx computed only once

# ^^ If you're BUILDING the answer as a parameter (ans, path, curr_str)
# ^^ → you're in generation world → forget memo

# ^^ If your function RETURNS a number / bool
# ^^ → you're in DP world → memo everything

    