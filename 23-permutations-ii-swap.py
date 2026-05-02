def permute_unique(nums):
    result = []
    
    def backtrack(index):
        if index == len(nums):
            result.append(nums.copy())
            return
        
        seen = set()
        
        for i in range(index, len(nums)):
            
            # skip duplicates at this level
            if nums[i] in seen:
                continue
            
            seen.add(nums[i])
            
            nums[index], nums[i] = nums[i], nums[index]
            
            backtrack(index + 1)
            
            nums[index], nums[i] = nums[i], nums[index]
    
    backtrack(0)
    return result


# Test
print(permute_unique([1,1,2]))

"""
# RECURSION TREE — swap + seen set  nums=[1,1,2]  (no sorting needed)
#
# seen={} is created FRESH at each backtrack(index) call.
# It tracks which VALUES have already been placed at position=index.
# If nums[i] is already in seen → skip (would produce duplicate branch).
#
#              backtrack(0)  nums=[1,1,2]  seen={}
#             /              |              \
#     i=0: 1∉seen       i=1: 1∈seen!    i=2: 2∉seen
#     seen={1}          ✗ SKIP          seen={1,2}
#     sw(0,0)→[1,1,2]                   sw(0,2)→[2,1,1]
#           |                                   |
#     backtrack(1)                        backtrack(1)
#     nums=[1,1,2] seen={}               nums=[2,1,1] seen={}
#      /          \                        /          \
# i=1:1∉seen  i=2:2∉seen           i=1:1∉seen    i=2:1∈seen!
# seen={1}    seen={1,2}           seen={1}       ✗ SKIP
# sw(1,1)     sw(1,2)→[1,2,1]     sw(1,1)
# →[1,1,2]                        →[2,1,1]
#      |            |                   |
# backtrack(2)  backtrack(2)       backtrack(2)
# [1,1,2]       [1,2,1]            [2,1,1]
#      |            |                   |
#  sw(2,2)      sw(2,2)            sw(2,2)
# [1,1,2] ✅  [1,2,1] ✅         [2,1,1] ✅
#
# KEY DIFFERENCE from used[] approach:
#   - No sorting required
#   - seen={} is local to each call — not shared across recursive depth
#   - Checks VALUE already tried at this level (not global used state)
#   - Under [2,1,1] at index=1: nums[2]=1 already in seen → prune
#
# Total: 3 leaves, 2 prunes
"""
