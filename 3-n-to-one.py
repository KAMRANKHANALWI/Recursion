def n_to_one(n):
    if n == 0:
        return
    print(n)
    n_to_one(n-1)
    
n_to_one(5)