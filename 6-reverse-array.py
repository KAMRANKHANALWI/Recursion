def reverse_array(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse_array(arr, l+1, r-1)

arr = [1,2,3,4,5]
reverse_array(arr, 0, len(arr)-1)

def reverse_array_ii(arr, i):
    n = len(arr)
    if i == n // 2:
        return
    arr[i], arr[n-i-1] = arr[n - i - 1], arr[i]
    reverse_array_ii(arr, i+1)
    
arr2 = [2,4,6,8,10]
reverse_array_ii(arr2, 0)

print(arr)
print(arr2)