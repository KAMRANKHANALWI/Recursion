def check_palindrome(s, i):
    s = s.lower()
    n = len(s)
    if i >= n // 2:
        return True
    
    if s[i] != s[n - i - 1]:
        return False
    
    return check_palindrome(s, i + 1)

s = "MaDAm"
print(check_palindrome(s, 0))