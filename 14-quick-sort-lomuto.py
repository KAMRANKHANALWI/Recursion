def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot_idx = partition(arr, start, end)
    quick_sort(arr, start, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, end)
    
def partition(arr, start, end):
    pivot = arr[end]
    index = start - 1
    
    for j in range(start, end):
        if arr[j] <= pivot:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
    
    index += 1
    arr[index], arr[end] = arr[end], arr[index]
    
    return index

arr = [12, 31, 35, 8, 32, 17]
print(quick_sort(arr, 0, len(arr) - 1))
print(arr)
            