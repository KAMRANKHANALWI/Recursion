def partition(s):
    res = []
    
    def backtrack(idx, path):
        if len(s) == idx:
            res.append(list(path))
            return
        
        for i in range(idx, len(s)):
            if is_palindrome(s, idx, i):
                path.append(s[idx: i + 1])
                backtrack(i + 1, path)
                path.pop()
        
    def is_palindrome(s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1    
        return True
    
    backtrack(0, [])
    return res

s = "aabb"
print(partition(s))

"""
# RECURSION TREE — Palindrome Partitioning  s="aabb"
#
# RULE: only recurse if s[index..i] is a palindrome (two-pointer check)
# path.pop() after each recursive call = backtracking
#
#                        backtrack(0, [])
#                       /        |        \        \
#              "a" ✓         "aa" ✓      "aab" ✗  "aabb" ✗
#           bt(1,["a"])    bt(2,["aa"])   skip      skip
#            /    |   \        |     \
#          "a"✓ "ab"✗ "abb"✗  "b"✓  "bb"✓
#       bt(2,    skip   skip bt(3,  bt(4,
#       ["a","a"])      ["aa","b"]) ["aa","bb"])
#          /      \          \            \
#        "b"✓   "bb"✓        "b"✓       idx==4
#      bt(3,    bt(4,      bt(4,          ✅
#    ["a","a",  ["a","a",  ["aa","b",  ["aa","bb"]
#       "b"])     "bb"])      "b"])
#         \          \           \
#         "b"✓      idx==4      idx==4
#       bt(4,         ✅          ✅
#    ["a","a",    ["a","a",   ["aa","b","b"]
#      "b","b"])    "bb"])
#          \
#         idx==4
#           ✅
#      ["a","a","b","b"]
#
#
# Results (left to right, top to bottom):
#   ["a","a","b","b"]  ✅
#   ["a","a","bb"]     ✅
#   ["aa","b","b"]     ✅
#   ["aa","bb"]        ✅
#
# PRUNE:  "ab"  ✗  → not palindrome, no recursion
#         "abb" ✗  → not palindrome, no recursion
#         "aab" ✗  → not palindrome, no recursion
#        "aabb" ✗  → not palindrome, no recursion
#
# BACKTRACK: path.pop() after every bt() call
#   restores path to previous state before trying next substring
#
# Total: 4 valid partitions, 4 pruned branches
"""
    