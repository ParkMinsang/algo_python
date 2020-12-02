import sys
sys.setrecursionlimit(100000)

def dfs(y,x):
    global res
    visited[y][x] = 1
    res += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<m and way[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(ny,nx)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m, k = map(int,input().split())
way = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
res = 0
ans = 0

for _ in range(k):
    r,c = map(int,input().split())
    way[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        res = 0
        if way[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
        ans = max(ans,res)
print(ans)
