def count_subsequences(s, ans):
    if len(s) == 0:
        return 1
    
    ch = s[0]
    left = count_subsequences(s[1:], ans + ch)
    right = count_subsequences(s[1:], ans)
    return left + right

print(count_subsequences("abc", ""))