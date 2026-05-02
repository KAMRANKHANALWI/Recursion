def merge_two_sorted_arr(left_arr, right_arr):
    i = 0
    j = 0
    result = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1

    return result


def merge_sort(arr, low, high):
    if not arr:
        return []
    
    if low >= high:
        return [arr[low]]

    mid = (low + high) // 2

    left_arr = merge_sort(arr, low, mid)
    right_arr = merge_sort(arr, mid + 1, high)
    return merge_two_sorted_arr(left_arr, right_arr)


arr = [12, 1, 3, 2, 4, -1]
print(merge_sort(arr, 0, len(arr) - 1))
