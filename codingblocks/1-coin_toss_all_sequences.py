def coin_sequences(n, ans):
    if n == 0:
        print(ans)
        return
    
    coin_sequences(n-1, ans + "H")
    coin_sequences(n-1, ans + "T")
    
    
coin_sequences(2, "")

print("=" * 20)

"""
Recursion tree (for n=2):

         " "
        /    \
      "H"    "T"
      / \    / \
    HH  HT  TH  TT
    
"""

def coin(n, curr):
    
    if n == 0:
        ans = "".join(curr)
        print(ans)
        return
    
    curr.append("H")
    coin(n - 1, curr)
    curr.pop()
    
    curr.append("T")
    coin(n - 1, curr)
    curr.pop()
    

coin(2, [])