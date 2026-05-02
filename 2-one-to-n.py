def one_to_n(i, n):
    # if n == 0:
    #     return
    # one_to_n(n-1)
    # print(n)
    if i > n:
        return
    print(i)
    one_to_n(i+1, n)
    
one_to_n(1, 5)
# one_to_n(5)