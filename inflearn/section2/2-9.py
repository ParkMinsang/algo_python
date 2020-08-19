n = int(input())

money = 0

for _ in range(n):
    price = 0
    dice = list(map(int,input().split()))
    dice.sort()
    if dice[0] == dice[2]: # 3개가 동일
        price = 10000 + (dice[0]*1000)
    elif dice[0] == dice[1]: # 2개만 동일
        price = 1000 + (dice[1]*100)
    elif dice[1] == dice[2]: # 2개만 동일
        price = 1000 + (dice[1]*100)
    else: # 3개 다 다름
        price = max(dice)*100
    if price > money:
        money = price

print(money)
