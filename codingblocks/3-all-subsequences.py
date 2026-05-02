def all_subsequences(s, ans):
    if len(s) == 0:
        print(ans)
        return
    
    ch = s[0]
    # take
    all_subsequences(s[1:], ans + ch)
    # not take
    all_subsequences(s[1:], ans)
    
all_subsequences("abc", "")
    