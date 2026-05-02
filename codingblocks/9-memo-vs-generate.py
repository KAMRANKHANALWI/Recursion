# Most important distinctions in recursion/DP.

## // The Core Rule
# * ══════════════════════════════════════════════════
# * CAN I MEMOIZE? → Ask yourself ONE question:
# * "Does my subproblem depend ONLY on the index/position,
# *  or does it also depend on the PATH taken to get here?"
# * ══════════════════════════════════════════════════

# ^^ If answer depends on PATH  → Generation Problem → NO memo
# ^^ If answer depends on INDEX → Counting/Optimal   → YES memo

# ! Two Worlds of Recursion

# ## ── WORLD 1: GENERATION PROBLEMS ──────────────────
# ~  Goal: print / collect ALL possible outputs
# ~  The OUTPUT itself is part of the state
# ~  ans / path / current-string changes every call
# ~  NO two calls share the same subproblem
# ~  Memoization is useless here

# ## ── WORLD 2: COUNTING / OPTIMIZATION PROBLEMS ─────
# ~  Goal: HOW MANY ways / WHAT IS the best way
# ~  Only position/index matters
# ~  Many calls share the exact same subproblem
# ~  Memoization saves repeated work

## Generation Problems — NO Memo


# == 1. Board Path (print all paths)
def board_path(idx, n, ans=""):
    if idx == n:
        print(ans)  # ~ "111", "12", "21", "3"
        return
    if idx > n:
        return
    for i in range(1, 4):
        board_path(idx + i, n, ans + str(i))


# ~ memo key = (idx, ans) → never repeats → useless


# == 2. Keypad Combinations
keypad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs"}


def keypad_combo(keys, idx, ans=""):
    if idx == len(keys):
        print(ans)  # ~ "ad", "ae", "af", "bd"...
        return
    for ch in keypad[keys[idx]]:
        keypad_combo(keys, idx + 1, ans + ch)


# ~ ans is different every time even at same idx
# ~ reaching idx=1 via "a" vs "b" vs "c" → 3 different states


# == 3. Generate Parentheses
def gen_parens(open, close, n, ans=""):
    if open == n and close == n:
        print(ans)  # ~ "(())", "()()"
        return
    if open < n:
        gen_parens(open + 1, close, n, ans + "(")
    if close < open:
        gen_parens(open, close + 1, n, ans + ")")


# // state = (open, close, ans) → ans always unique
# // even (open=1, close=0) reached via "(" is only ever one way
# // but ans is being built so it still falls in generation world


# ~ Counting / Optimization Problems — YES Memo

# == 1. Climbing Stairs (count ways)
from functools import lru_cache


@lru_cache(maxsize=None)
def climb_stairs(n):
    # ? how many ways to climb n stairs (1 or 2 steps)
    if n <= 1:
        return 1  # --> base case
    return climb_stairs(n - 1) + climb_stairs(n - 2)


# ^^ climb_stairs(4) called multiple times → cached!
# ^^ pure fibonacci, only n matters


# == 2. Board Path COUNT (not print)
@lru_cache(maxsize=None)
def count_paths(idx, n):
    if idx == n:
        return 1
    if idx > n:
        return 0
    total = 0
    for i in range(1, 4):
        total += count_paths(idx + i, n)
    return total


# // count_paths(2, 3) always returns 1 no matter how you got to idx=2
# // SAME subproblem → cache it!


# == 3. 0/1 Knapsack (maximize value)
@lru_cache(maxsize=None)
def knapsack(idx, capacity):
    # ? only idx and remaining capacity matter
    if idx == len(weights) or capacity == 0:
        return 0
    if weights[idx] > capacity:
        return knapsack(idx + 1, capacity)
    return max(
        values[idx] + knapsack(idx + 1, capacity - weights[idx]),
        knapsack(idx + 1, capacity),
    )


# // same (idx, capacity) → same answer always → perfect for memo


# ##Your Intuition Was Right — Climb Stairs Print = Board Path


# // YES! print climb stairs IS the same pattern as board path


# ## climb stairs PRINT version (generation problem)
def climb_stairs_print(idx, n, ans=""):
    if idx == n:
        print(ans)  # --> "11", "12", "21", "111"... wait
        return  # --> actually same output as board_path!
    if idx > n:
        return
    for step in [1, 2]:  # only diff: 2 choices not 3
        climb_stairs_print(idx + step, n, ans + str(step))


# ~ climb_stairs_print(0, 3, "")
# ~ 111
# ~ 12
# ~ 21

# ^^ board_path(0, 3) with jumps 1,2,3 vs climb(0,3) with steps 1,2
# ^^ EXACT same pattern, just different number of choices!


## ## The Full Map

# * ══════════════════════════════════════════════════════════
# *   PROBLEM TYPE         MEMO?   WHY
# * ══════════════════════════════════════════════════════════
# * Print board paths       NO     ans changes every call
# * Print keypad combos     NO     ans changes every call
# * Generate parentheses    NO     ans changes every call
# * Print climb stairs      NO     same — ans changes!
# * ──────────────────────────────────────────────────────────
# * Count board paths       YES    only idx matters
# * Count climb stairs      YES    only n matters (fibonacci!)
# * 0/1 Knapsack            YES    only (idx, capacity) matters
# * Longest common subseq   YES    only (i, j) matters
# * Min coin change         YES    only (amount) matters
# * ══════════════════════════════════════════════════════════

# $  Generation  → O(branches^depth)  no savings possible
# $  Count+Memo  → O(unique states)   massive savings


## ## The Litmus Test — 3 Questions

# ? Q1: Am I building/printing a PATH or STRING as I recurse?
# ?     YES → Generation problem → NO memo

# ? Q2: Do two different calls with the SAME arguments
# ?     always return the SAME result?
# ?     YES → safe to memo
# ?     NO  → don't memo (side effects like print, or ans in state)

# ? Q3: Am I asked HOW MANY / BEST / MIN / MAX?
# ?     YES → almost always DP/memo
# ?     NO (asked to LIST/PRINT/GENERATE) → NO memo


# ## Takeaway:
# ^^ If you're BUILDING the answer as a parameter (ans, path, curr_str)
# ^^ → you're in generation world → forget memo

# ^^ If your function RETURNS a number / bool
# ^^ → you're in DP world → memo everything
