import sys
sys.setrecursionlimit(100000)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(input())
adj = [list(map(int,input().split())) for _ in range(n)]
ans = 0
highest = max(max(adj))

def dfs(y,x,h):
    visited[y][x] = 1
    for p in range(4):
        ny = y + dy[p]
        nx = x + dx[p]
        if 0<=ny<n and 0<=nx<n and adj[ny][nx]>h and visited[ny][nx] == 0:
            dfs(ny,nx,h)

for k in range(0, highest+1):
    cnt = 0
    visited = [[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj[i][j] > k and visited[i][j] == 0:
                cnt += 1
                dfs(i,j,k)
    ans = max(ans,cnt)
print(ans)
