def coin_combinations(coins, target, amount, ans, idx):
    if amount > target:
        return
    
    if amount == target:
        print(ans)
        return
    
    for i in range(idx, len(coins)):
        coin_combinations(coins, target, amount + coins[i], ans + str(coins[i]), i)

coins = [2, 3, 5]
coin_combinations(coins, 10, 0, "", 0)