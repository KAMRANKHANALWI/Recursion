def print_one_subseq(arr, i, result, curr_sum, k):
    if i == len(arr):
        if curr_sum == k:
            print(result)
            return True
        return False
    
    result.append(arr[i])
    curr_sum += arr[i]
    if print_one_subseq(arr, i+1, result, curr_sum, k):
        return True
    
    result.pop()
    curr_sum -= arr[i]
    if print_one_subseq(arr, i+1, result, curr_sum, k):
        return True
    
    return False

arr = [1, 2, 1]
k = 2
print_one_subseq(arr, 0, [], 0, k)