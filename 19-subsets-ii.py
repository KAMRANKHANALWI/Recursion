def subsets_with_dup(nums):
    nums.sort()
    result = []
    
    def backtrack(idx, curr_sum):
        result.append(list(curr_sum))
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            
            curr_sum.append(nums[i])
            backtrack(i + 1, curr_sum)
            curr_sum.pop()
    
    backtrack(0, [])
    return result

nums = [1, 2, 2]
print(subsets_with_dup(nums))

"""
# RECURSION TREE — subsets with duplicates  nums=[1,2,2]  (sorted)
#
# Pattern: save curr at ENTRY of every call (not just leaves)
#          for-loop from idx..n, skip if i>idx and nums[i]==nums[i-1]
#          dup-skip: i>idx not i>0 — only skips dups within this call's loop
#
#              backtrack(0, [])  → save []
#              /              \               \ 
#         i=0 pick1        i=1 pick2       i=2 ✗SKIP
#              |                |           (nums[2]==nums[1], i>idx)
#    backtrack(1,[1])    backtrack(2,[2])
#    → save [1]          → save [2]
#     /          \              |
# i=1 pick2   i=2 ✗SKIP    i=2 pick2
#      |      (dup of i=1)       |
# backtrack(2,[1,2])      backtrack(3,[2,2])
# → save [1,2]            → save [2,2] ✅
#      |
#   i=2 pick2
#      |
# backtrack(3,[1,2,2])
# → save [1,2,2] ✅
#
# WHAT GETS SAVED (in order of calls):
#   []  →  [1]  →  [1,2]  →  [1,2,2]  →  [2]  →  [2,2]
#
# 2 branches pruned (i=2 at root, i=2 under [1])
# Result: [[], [1], [1,2], [1,2,2], [2], [2,2]]
"""

            
        
    