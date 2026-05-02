def combination(arr, idx, curr, res):
    res.append(list(curr))
    
    for i in range(idx, len(arr)):
        curr.append(arr[i])
        combination(arr, i+1, curr, res)
        curr.pop()
        
    return res

arr = [1,2,3]
print(combination(arr, 0, [], []))
    
def combination_pick_non_pick(arr, idx, curr, res):
    if idx == len(arr):
        res.append(list(curr))
        return
    
    # == pick
    curr.append(arr[idx])
    combination_pick_non_pick(arr, idx + 1, curr, res)
    curr.pop()
    
    # == not pick
    combination_pick_non_pick(arr, idx + 1, curr, res)
    
    return res

print(combination_pick_non_pick(arr, 0, [], []))

"""
# == Recursion Tree (N-ary / Loop based)
# !                           []
# !               /            |            \
# !            [1]            [2]           [3]
# !          /     \            \             
# !      [1,2]    [1,3]        [2,3]         
# !       /                            
# !  [1,2,3]                        
"""

"""
# == Recursion Tree (Binary : Pick / Not Pick)
# !                []
# !           /           \
# !        [1]            []
# !       /   \         /    \
# !   [1,2]  [1]     [2]     []
# !   ...
"""


