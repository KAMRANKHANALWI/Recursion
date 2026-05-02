def permutations(nums, idx, curr, result, used):    
    if idx == len(nums):
        result.append(list(curr))
        return 
    
    for i in range(len(nums)):
        if not used[i]:
            used[i] = True
            curr.append(nums[i])
            permutations(nums, idx + 1, curr, result, used)
            curr.pop()
            used[i] = False
            
nums = [1, 2, 3]
result = []
permutations(nums, 0, [], result, [False] * len(nums))
print(result)

# def permutations(nums):
#     result = []
#     path = []
#     used = [False] * len(nums)

#     def backtrack():
#         # base case
#         if len(path) == len(nums):
#             result.append(path.copy())
#             return

#         for i in range(len(nums)):
#             if not used[i]:
#                 # pick
#                 used[i] = True
#                 path.append(nums[i])

#                 backtrack()

#                 # backtrack
#                 path.pop()
#                 used[i] = False

#     backtrack()
#     return result

# print(permutations([1, 2, 3]))


"""
# RECURSION TREE — used[] approach  nums=[1,2,3]
#
#                      path=[]  used=[_,_,_]
#                    /          |          \
#            pick 1           pick 2       pick 3
#               |               |               |
#         path=[1]         path=[2]         path=[3]
#        used=[✓,_,_]     used=[_,✓,_]    used=[_,_,✓]
#          /      \          /      \         /      \
#       pk2      pk3      pk1      pk3     pk1      pk2
#        |        |        |        |       |        |
#    [1,2]    [1,3]    [2,1]    [2,3]   [3,1]    [3,2]
#   [✓,✓,_]  [✓,_,✓] [✓,✓,_]  [_,✓,✓] [✓,_,✓]  [_,✓,✓]
#      |        |        |        |       |        |
#    pk3      pk2      pk3      pk1     pk2      pk1
#      |        |        |        |       |        |
#  [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]  ← save!
#
# BACKTRACK EXAMPLE (left branch):
#   pick 1 → used=[✓,_,_] path=[1]
#   pick 2 → used=[✓,✓,_] path=[1,2]
#   pick 3 → used=[✓,✓,✓] path=[1,2,3] ← BASE CASE → append to result
#   ↩ pop 3, used[2]=False → used=[✓,✓,_] path=[1,2]
#   no more free elements → ↩ pop 2, used[1]=False → used=[✓,_,_] path=[1]
#   pick 3 → used=[✓,_,✓] path=[1,3] → continue ...
"""