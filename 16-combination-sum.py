def combination_sum(arr, target):
    result = []

    def find_combination(idx, target, curr_comb):
        if idx == len(arr):
            if target == 0:
                # result.append(curr_comb[:])
                # result.append(curr_comb.copy())
                result.append(list(curr_comb))
            return

        # Pick
        if arr[idx] <= target:
            curr_comb.append(arr[idx])
            find_combination(idx, target - arr[idx], curr_comb)
            curr_comb.pop()

        # Not Pick
        find_combination(idx + 1, target, curr_comb)

    find_combination(0, target, [])
    return result


arr = [2, 3, 6, 7]
target = 7
print(combination_sum(arr, target))

# def combination_sum(arr, target):
    
#     def find_combination(idx, target, curr_comb, result):
#         if idx == len(arr):
#             if target == 0:
#                 result.append(list(curr_comb))
#             return
        
#         # Pick
#         if arr[idx] <= target:
#             curr_comb.append(arr[idx])
#             find_combination(idx, target - arr[idx], curr_comb, result)
#             curr_comb.pop()
            
#         # Not Pick
#         find_combination(idx + 1, target, curr_comb, result)
    
#     result = []
#     find_combination(0, target, [], result)
#     return result

# arr = [2,3,6,7]
# target = 7
# print(combination_sum(arr, target))  # [[2, 2, 3], [7]]