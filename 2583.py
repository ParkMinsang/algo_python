import sys
sys.setrecursionlimit(100000)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

m, n, k = map(int,input().split())
board = [[0]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]
find = []
for _ in range(k):
    ldx, ldy, rux, ruy = map(int,input().split())
    for i in range(ldx,rux):
        for j in range(ldy,ruy):
            board[m-j-1][i] = 1

def dfs(y,x):
    visited[y][x] = 1
    find[-1] += 1
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<m and 0<=nx<n and board[ny][nx] == 0 and visited[ny][nx] == 0:
            dfs(ny,nx)

for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and visited[i][j] == 0:
            find.append(0)
            dfs(i,j)

find.sort()
print(len(find))
print(*find)
