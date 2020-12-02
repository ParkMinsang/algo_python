import sys
sys.setrecursionlimit(10000)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfsnormal(y,x,g):
    normal[y][x] = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<= ny < n and 0<= nx < n and grid[ny][nx] == g and normal[ny][nx] == 0:
            dfsnormal(ny,nx,g)

def dfsblue(y,x,g):
    redisgreen[y][x] = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if grid[ny][nx]=='B' and redisgreen[ny][nx] == 0:
                dfsblue(ny,nx,g)

def dfsredgreen(y,x,g):
    redisgreen[y][x] = 1
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=ny<n and 0<=nx<n:
            if grid[ny][nx] != 'B' and redisgreen[ny][nx] == 0:
                dfsredgreen(ny,nx,g)

n = int(input())
grid = [list(input()) for _ in range(n)]
redisgreen = [[0]*(n) for _ in range(n)]
normal = [[0]*(n) for _ in range(n)]
cnt_normal = 0
cnt_redisgreen = 0

for i in range(n):
    for j in range(n):
        if normal[i][j] == 0:
            cnt_normal += 1
            dfsnormal(i,j,grid[i][j])
        if redisgreen[i][j] == 0:
            cnt_redisgreen += 1
            if grid[i][j] == 'B':
                dfsblue(i,j,grid[i][j])
            else:
                dfsredgreen(i,j,grid[i][j])

print(cnt_normal, cnt_redisgreen)
