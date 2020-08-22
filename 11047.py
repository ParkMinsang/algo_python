n, k = map(int,input().split())
currency = [int(input()) for _ in range(n)]
res = 0
for i in range(n-1,-1,-1):
    if k//currency[i] > 0:
        res += k//currency[i]
        k -= currency[i]*(k//currency[i])

print(res)
