def count_subseq(arr, i, curr_sum, k):
    if i == len(arr):
        if curr_sum == k:
            return 1
        return 0
    
    left = count_subseq(arr, i + 1, curr_sum + arr[i], k)
    right = count_subseq(arr, i + 1, curr_sum, k)
    
    return left + right

arr = [1, 2, 1]
k = 2
print(count_subseq(arr, 0, 0, k))