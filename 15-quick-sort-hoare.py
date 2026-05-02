def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_idx = hoare_partition(arr, low, high)
    quick_sort(arr, low, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, high)


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i < high and arr[i] <= pivot:
            i += 1

        while j > low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

# arr = [12, 31, 35, 8, 32, 17]
arr = [4, 2, 7, 3, 1, 6, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)