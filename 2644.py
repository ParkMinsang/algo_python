import sys
from collections import deque

n = int(input())
g = [[0]*(n+1) for _ in range(n+1)]

tg1, tg2 = map(int,input().split())
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    g[x][y] = 1

ans = 0
q = deque()

for k in range(1, n+1):
    if g[k][tg1] == 1:
        q.append(k)
        g[k][tg1] = 0
    if g[tg1][k] == 1:
        q.append(k)
        g[tg1][k] = 0

while q:
    ans += 1
    for i in range(len(q)):
        get = q.popleft()
        if get == tg2:
            print(ans)
            sys.exit()
        else:
            for j in range(1, n+1):
                if g[get][j] == 1:
                    q.append(j)
                    g[get][j] = 0
                if g[j][get] == 1:
                    q.append(j)
                    g[j][get] = 0
print(-1)
