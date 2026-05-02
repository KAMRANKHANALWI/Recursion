def permutation(s: str, ans):
    if len(s) == 0:
        print(ans)
        return
    
    seen = set()
    
    for i in range(len(s)):
        
        ch = s[i]
        
        if ch in seen:
            continue
        
        seen.add(ch)
        remaining = s[:i] + s[i+1:]
        permutation(remaining, ans + ch)
        
permutation("aab", "")
        
# == Recursion Tree for permutation("aab", "")
# ?
# ?                                          ("aab", "")
# ?                                    seen={} at this level
# ?                              /            |             \
# ?                            i=0           i=1             i=2
# ?                          ch='a'        ch='a'           ch='b'
# ?                            ✅         ✋SKIP             ✅
# ?                            /        'a' in seen={'a'}     \
# ?                      ("ab","a")                         ("aa","b")
# ?                     seen={} fresh                      seen={} fresh
# ?                     /           \                      /          \
# ?                   i=0           i=1                  i=0          i=1
# ?                 ch='a'         ch='b'               ch='a'       ch='a'
# ?                   ✅             ✅                    ✅         ✋SKIP
# ?                   /               \                   /        'a' in seen={'a'}
# ?             ("b","aa")         ("a","ab")         ("a","ba")
# ?            seen={} fresh      seen={} fresh       seen={} fresh
# ?                |                   |                   |
# ?               i=0                 i=0                 i=0
# ?             ch='b'              ch='a'              ch='a'
# ?               ✅                  ✅                  ✅
# ?               |                   |                   |
# ?          ("","aab")          ("","aba")          ("","baa")
# ?               |                   |                   |
# ?            ✅ aab             ✅ aba              ✅ baa
# ?
# ?
# ? SKIP SUMMARY:
# ? ┌─────────┬──────────────────────────────────────────────────────┐
# ? │ Level 1 │ i=1 ch='a' ✋ because seen={'a'} (i=0 added it)     │
# ? ├─────────┼──────────────────────────────────────────────────────┤
# ? │ Level 2b│ i=1 ch='a' ✋ because seen={'a'} (i=0 added it)     │
# ? └─────────┴──────────────────────────────────────────────────────┘
# ?
# ? WITHOUT seen, we'd get 6 calls (3!) but only 3 unique → seen cuts 2 branches
        
        
        