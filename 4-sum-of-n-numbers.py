def sum_of_n_numbers(n, total):
    if n == 0:
        return total
    return sum_of_n_numbers(n-1, total + n)
    
print(sum_of_n_numbers(5, 0))

'''
DRY RUN: Accumulator (Tail Recursion style)
(5,0) → (4,5) → (3,9) → (2,12) → (1,14) → (0,15) → return 15
'''


def sum_of_n_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_n_numbers(n-1)

print(sum_of_n_numbers(10))

'''
DRY RUN: Build-on-return (Classic recursion)
sum(5)
= 5 + sum(4)
= 5 + (4 + sum(3))
= 5 + (4 + (3 + sum(2)))
= ...
= 5 + 4 + 3 + 2 + 1 + 0
= 15
'''
