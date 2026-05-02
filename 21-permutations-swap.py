def permutations(nums, idx, result):
    if idx == len(nums):
        result.append(list(nums))
        return
    
    for i in range(idx, len(nums)):
        nums[idx], nums[i] = nums[i], nums[idx]
        permutations(nums, idx + 1, result)
        nums[idx], nums[i] = nums[i], nums[idx]
        
nums = [1, 2, 3]
result = []
permutations(nums, 0, result)
print(result)

"""
# RECURSION TREE — swap approach  nums=[1,2,3]
#
#                  [1,2,3]  idx=0
#                /          |         \
#         sw(0,0)        sw(0,1)      sw(0,2)
#        no change       → [2,1,3]   → [3,2,1]
#            |               |            |
#        [1,2,3]         [2,1,3]      [3,2,1]
#          idx=1           idx=1        idx=1
#         /     \         /     \       /     \
#     sw(1,1) sw(1,2) sw(1,1) sw(1,2) sw(1,1) sw(1,2)
#       noop   →[1,3,2]  noop  →[2,3,1]  noop →[3,1,2]
#        |        |        |       |        |       |
#    [1,2,3]  [1,3,2]  [2,1,3] [2,3,1]  [3,2,1] [3,1,2]
#      idx=2    idx=2    idx=2   idx=2    idx=2   idx=2
#        |        |        |       |        |       |
#    sw(2,2)  sw(2,2)  sw(2,2) sw(2,2)  sw(2,2) sw(2,2)
#        |        |        |       |        |       |
#    [1,2,3]  [1,3,2]  [2,1,3] [2,3,1]  [3,2,1] [3,1,2]
#      ✅       ✅       ✅      ✅       ✅       ✅
#
# BACKTRACK EXAMPLE (leftmost branch):
#   sw(0,0) → [1,2,3]  idx moves to 1
#   sw(1,1) → [1,2,3]  idx moves to 2
#   sw(2,2) → [1,2,3]  idx=3 == len → BASE CASE → save [1,2,3]
#   ↩ sw(2,2) again → back to [1,2,3]  (swap is its own inverse!)
#   ↩ sw(1,2) → [1,3,2]  try next i at level 2
#   sw(2,2) → [1,3,2]  BASE CASE → save [1,3,2]
#   ↩ sw(2,2) → [1,3,2]
#   ↩ sw(1,2) → [1,2,3]  restore before moving to next branch at level 1
"""
