def print_subseq_sum_k(arr, i, result, curr_sum, k):
    if i == len(arr):
        if curr_sum == k:
            print(result)
        return
    
    result.append(arr[i])
    print_subseq_sum_k(arr, i+1, result, curr_sum + arr[i], k)
    
    result.pop()
    print_subseq_sum_k(arr, i+1, result, curr_sum, k)
    
def print_subseq_sum_k_ii(arr, i, result, curr_sum, k):
    if i == len(arr):
        if curr_sum == k:
            print(result)
        return
    
    curr_sum += arr[i]
    result.append(arr[i])
    print_subseq_sum_k(arr, i+1, result, curr_sum, k)
    
    curr_sum -= arr[i]
    result.pop()
    print_subseq_sum_k_ii(arr, i+1, result, curr_sum, k)
    
arr = [1, 2, 1]
k = 2
print_subseq_sum_k(arr, 0, [], 0, k)
print_subseq_sum_k_ii(arr, 0, [], 0, k)