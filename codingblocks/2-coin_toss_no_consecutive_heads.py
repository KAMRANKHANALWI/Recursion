def coin_sequences_ii(n, ans):
    if n == 0:
        print(ans)
        return
    
    if len(ans) == 0 or ans[-1] != "H":
        coin_sequences_ii(n-1, ans + "H")
    coin_sequences_ii(n-1, ans + "T")
    
coin_sequences_ii(4, "")