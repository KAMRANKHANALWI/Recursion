def subsets_sums(arr):
    result = []

    def dfs(idx, curr_sum):
        if idx == len(arr):
            result.append(curr_sum)
            return

        dfs(idx + 1, curr_sum + arr[idx])
        dfs(idx + 1, curr_sum)

    dfs(0, 0)
    result.sort()
    return result


arr = [1, 2, 3]
print(subsets_sums(arr))

"""
# RECURSION TREE — subset sums  arr=[1,2,3]
#
# Pure binary tree: at each idx, LEFT = include arr[idx], RIGHT = skip arr[idx]
# Sum passed by value (int) → no backtracking needed, nothing to undo
# 2^n leaves = 2^3 = 8 leaves total
#
#                    dfs(idx=0, sum=0)
#                   /                 \
#           +arr[0]=1                skip 1
#               /                          \
#        dfs(1, sum=1)               dfs(1, sum=0)
#          /       \                   /       \
#       +2          skip2           +2          skip2
#        |            |              |            |
#    dfs(2,3)     dfs(2,1)      dfs(2,2)     dfs(2,0)
#     /    \       /    \        /    \        /    \
#   +3    skip  +3    skip    +3    skip    +3    skip
#    |      |    |      |      |      |      |      |
#  sum=6  sum=3 sum=4 sum=1  sum=5  sum=2  sum=3  sum=0
#   ✅    ✅    ✅    ✅    ✅    ✅    ✅    ✅
#
# All 8 leaves collected, then result.sort() → [0,1,2,3,3,4,5,6]
#
# KEY: idx==len(arr) is the base case → save curr_sum
#      Left child always: dfs(idx+1, curr_sum + arr[idx])  ← include
#      Right child always: dfs(idx+1, curr_sum)             ← exclude
#      No for-loop, no backtrack — completely different pattern from subsets
"""

