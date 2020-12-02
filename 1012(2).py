import sys
sys.setrecursionlimit(50000)
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(y,x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<m and mymap[ny][nx] == 1:
            mymap[ny][nx] = 0
            dfs(ny,nx)

t = int(input())

for _ in range(t):
    m, n, k = map(int,input().split())
    mymap = [[0]*(m) for _ in range(n)]
    need = 0
    for _ in range(k):
        x, y = map(int,input().split())
        mymap[y][x] = 1
    for i in range(n):
        for j in range(m):
            if mymap[i][j] == 1:
                need+=1
                # visited[i][j] = 1
                dfs(i,j)
                # stack = [tuple([i,j])]
                # while stack:
                #     last = stack.pop()
                #     for k in range(4):
                #         ny = last[0] + dy[k]
                #         nx = last[1] + dx[k]
                #         if 0<=ny<n and 0<=nx<m and mymap[ny][nx] == 1 and visited[ny][nx] == 0:
                #             visited[ny][nx]= 1
                #             stack.append(tuple([ny,nx]))
    print(need)
