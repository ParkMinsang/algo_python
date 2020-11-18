n, k = map(int,input().split())
ch=[99999]*(k+1)
coin = set()
for _ in range(n):
    a = int(input())
    if a <= k:
        coin.add(a)
        ch[a] = 1

for u in coin:
    for i in range(u,k+1):
        if 0<= i-u <= k:
            ch[i] = min(ch[i], ch[i-u]+1)

if ch[-1] != 99999:
    print(ch[-1])
else:
    print(-1)
