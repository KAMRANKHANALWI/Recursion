
# // Method : 01 - USED ARRAY MAP
def permutation(arr, curr, used, res):
    if len(curr) == len(arr):
        res.append(curr.copy())
        return
    
    for i in range(len(arr)):
        if used[i]:
            continue
        
        used[i] = True
        curr.append(arr[i])
        
        permutation(arr, curr, used, res)
        
        curr.pop()
        used[i] = False
    
    return res


arr = [1, 2, 3]
print(permutation(arr, [], [False]*len(arr), []))


# // Method : 02 - SWAP
def permute(arr, idx):
    if idx == len(arr):
        print(arr)
        return
    
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        permute(arr, idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]


permute([1,2,3], 0)

"""
# == Recursion Tree (used[] array map approach, nums=[1,2,3])

# ~
# ~                      path=[]  used=[_,_,_]
# ~                    /          |          \
# ~            pick 1           pick 2       pick 3
# ~               |               |               |
# ~         path=[1]         path=[2]         path=[3]
# ~        used=[✓,_,_]     used=[_,✓,_]    used=[_,_,✓]
# ~          /      \          /      \         /      \
# ~       pk2      pk3      pk1      pk3     pk1      pk2
# ~        |        |        |        |       |        |
# ~    [1,2]    [1,3]    [2,1]    [2,3]   [3,1]    [3,2]
# ~   [✓,✓,_]  [✓,_,✓] [✓,✓,_]  [_,✓,✓] [✓,_,✓]  [_,✓,✓]
# ~      |        |        |        |       |        |
# ~    pk3      pk2      pk3      pk1     pk2      pk1
# ~      |        |        |        |       |        |
# ~  [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]  ← save!
# ~
# ~ BACKTRACK EXAMPLE (left branch):
# ~   pick 1 → used=[✓,_,_] path=[1]
# ~   pick 2 → used=[✓,✓,_] path=[1,2]
# ~   pick 3 → used=[✓,✓,✓] path=[1,2,3] ← BASE CASE → append to result
# ~   ↩ pop 3, used[2]=False → used=[✓,✓,_] path=[1,2]
# ~   no more free elements → ↩ pop 2, used[1]=False → used=[✓,_,_] path=[1]
# ~   pick 3 → used=[✓,_,✓] path=[1,3] → continue ...                       
"""

"""
# == Recursion Tree (swap approach  nums=[1,2,3])

# ?
# ?                  [1,2,3]  idx=0
# ?                /          |         \
# ?         sw(0,0)        sw(0,1)      sw(0,2)
# ?        no change       → [2,1,3]   → [3,2,1]
# ?            |               |            |
# ?        [1,2,3]         [2,1,3]      [3,2,1]
# ?          idx=1           idx=1        idx=1
# ?         /     \         /     \       /     \
# ?     sw(1,1) sw(1,2) sw(1,1) sw(1,2) sw(1,1) sw(1,2)
# ?       noop   →[1,3,2]  noop  →[2,3,1]  noop →[3,1,2]
# ?        |        |        |       |        |       |
# ?    [1,2,3]  [1,3,2]  [2,1,3] [2,3,1]  [3,2,1] [3,1,2]
# ?      idx=2    idx=2    idx=2   idx=2    idx=2   idx=2
# ?        |        |        |       |        |       |
# ?    sw(2,2)  sw(2,2)  sw(2,2) sw(2,2)  sw(2,2) sw(2,2)
# ?        |        |        |       |        |       |
# ?    [1,2,3]  [1,3,2]  [2,1,3] [2,3,1]  [3,2,1] [3,1,2]
# ?      ✅       ✅       ✅      ✅       ✅       ✅
# ?
# ? BACKTRACK EXAMPLE (leftmost branch):
# ?   sw(0,0) → [1,2,3]  idx moves to 1
# ?   sw(1,1) → [1,2,3]  idx moves to 2
# ?   sw(2,2) → [1,2,3]  idx=3 == len → BASE CASE → save [1,2,3]
# ?   ↩ sw(2,2) again → back to [1,2,3]  (swap is its own inverse!)
# ?   ↩ sw(1,2) → [1,3,2]  try next i at level 2
# ?   sw(2,2) → [1,3,2]  BASE CASE → save [1,3,2]
# ?   ↩ sw(2,2) → [1,3,2]
# ?   ↩ sw(1,2) → [1,2,3]  restore before moving to next branch at level 1

"""