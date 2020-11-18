import sys
sys.setrecursionlimit(50000)

t = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y):
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0<= nx < m and 0<= ny < n and arr[nx][ny] == 1:
            arr[nx][ny] = 0
            dfs(nx,ny)

for _ in range(t):
    m, n, k = map(int,input().split())
    cnt = 0
    arr = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        a, b = map(int,input().split())
        arr[a][b] = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = 0
                dfs(i,j)
    print(cnt)
