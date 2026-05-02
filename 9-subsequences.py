def print_subsequences(arr, i, result):
    if i == len(arr):
        print(result)
        return
    
    # print_subsequences(arr, i + 1, result)
    
    result.append(arr[i])
    print_subsequences(arr, i + 1, result)
    
    result.pop()
    
    print_subsequences(arr, i + 1, result)
    
def print_subsequences_ii(arr, i, result):
    if i == len(arr):
        print(result)
        return
    
    print_subsequences(arr, i+1, result + [arr[i]])
    print_subsequences(arr, i+1, result)
    
arr = [1, 2, 3]
print_subsequences(arr, 0, [])
print("*" * 20)
print_subsequences_ii(arr, 0, [])