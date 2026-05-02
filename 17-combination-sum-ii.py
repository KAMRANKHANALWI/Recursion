def combination_sum2(arr, target):
    result = []
    arr.sort()
    
    def find_combination_ii(idx, target, curr):
        if target == 0:
            result.append(list(curr))
            return

        for i in range(idx, len(arr)):
            # skip duplicates at same recursion level
            if i > idx and arr[i] == arr[i-1]:
                continue
            
            # pruning - since sorted (value > target), no point going further
            if arr[i] > target:
                break
            
            curr.append(arr[i])
            find_combination_ii(i + 1, target - arr[i], curr)
            curr.pop()
         
    find_combination_ii(0, target, [])   
    return result

arr = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination_sum2(arr, target))