n, p = map(int,input().split())
ch = [[] for _ in range(8)]
cnt = 0
for _ in range(n):
    high, frat = map(int,input().split())
    while ch[high] and ch[high][-1] > frat:
        ch[high].pop()
        cnt+=1
    if ch[high] and ch[high][-1] == frat:
        ch[high].pop()
        cnt-=1
    ch[high].append(frat)
    cnt += 1

print(cnt)
