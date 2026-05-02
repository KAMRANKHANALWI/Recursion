def permutations(s, ans, res):
    if res is None:
        return []
    
    if len(s) == 0:
        res.append(ans)
        return
        
    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        permutations(remaining, ans + ch, res)
    
    return res

# s = "123"
s = "abc"
print(permutations(s, "", []))


# == Recursion Tree for permutation("abc", "")
# ?
# ?                                     ("abc", "")
# ?                                /         |          \
# ?                          i=0            i=1           i=2
# ?                          /               |               \
# ?                    ("bc","a")       ("ac","b")        ("ab","c")
# ?                   /       \          /      \           /      \
# ?                 i=0       i=1      i=0      i=1       i=0      i=1
# ?                 /           \       /          \       /          \
# ?           ("c","ab")  ("b","ac") ("c","ba") ("a","bc") ("b","ca") ("a","cb")
# ?              |             |        |           |          |           |
# ?             i=0           i=0      i=0          i=0       i=0         i=0
# ?              |             |        |           |          |           |
# ?         ("","abc")  ("","acb") ("","bac") ("","bca") ("","cab") ("","cba")
# ?              |             |        |           |          |           |
# ?           ✅ abc        ✅ acb   ✅ bac      ✅ bca     ✅ cab      ✅ cba
        