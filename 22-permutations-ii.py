def permute_unique(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            
            # already used
            if used[i]:
                continue
            
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            # pick
            used[i] = True
            path.append(nums[i])
            
            backtrack(path)
            
            # backtrack
            path.pop()
            used[i] = False
    
    backtrack([])
    return result


# Test
print(permute_unique([1,1,2]))

"""
# RECURSION TREE — used[] + duplicate-skip  nums=[1,1,2]  (sorted)
#
# PRUNE RULE: if i > 0 and nums[i]==nums[i-1] and not used[i-1]: skip
# (if same value as previous AND previous not used in THIS call → would duplicate that branch)
#
#                     path=[]  used=[_,_,_]
#                    /          |          \
#              i=0 pick1    i=1 ✗SKIP    i=2 pick2
#           used=[✓,_,_]  (1==nums[0]  used=[_,_,✓]
#                |         not used[0])       |
#           path=[1]                      path=[2]
#           used=[✓,_,_]                 used=[_,_,✓]
#            /         \                     |         \
#        i=1 pick1   i=2 pick2          i=0 pick1   i=1 ✗SKIP
#       used=[✓,✓,_] used=[✓,_,✓]    used=[✓,_,✓]  (1==nums[0]
#            |             |                |         not used[0])
#        path=[1,1]   path=[1,2]       path=[2,1]
#            |             |                |
#        i=2 pick2    i=1 pick1        i=1 pick1
#            |             |                |
#        [1,1,2] ✅   [1,2,1] ✅      [2,1,1] ✅
#
# KEY: i=1 (value=1) is skipped at root because:
#   nums[1]==nums[0] (both 1) AND used[0]==False → would create duplicate subtree
#   But under path=[1] (used[0]=True), i=1 is NOT skipped → used[0] is already True
#
# Total: 3 leaves, 2 prunes (would have been 3!=6 without dedup)
"""
