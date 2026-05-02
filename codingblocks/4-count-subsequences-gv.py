count = 0

def count_subseq(s, ans):
    global count
    if len(s) == 0:
        count += 1
        return
    
    ch = s[0]
    count_subseq(s[1:], ans + ch)
    count_subseq(s[1:], ans)
    
count_subseq("abc", "")
print(count)