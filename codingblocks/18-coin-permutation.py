def coin_permutaions(coins, target, amount, ans):
    if amount > target:
        return
    
    if amount == target:
        print(ans)
        return
    
    for i in range(len(coins)):
        coin_permutaions(coins, target, amount + coins[i], ans + str(coins[i]))
        
coins = [2, 3, 5]
target = 10
coin_permutaions(coins, target, 0, "")