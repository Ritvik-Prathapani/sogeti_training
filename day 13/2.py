number_of_coins=int(input())
coins={}
for _ in range(number_of_coins):
    coin_input=int(input())
    if coin_input not in coins:
        coins[coin_input]=1
    else:
        coins[coin_input]+=1

for keys,value in sorted(coins.items()):
    print(keys,value)
