dx = [-1,0,1,0]
dy = [0,-1,0,1]

n = int(input())
map = [list(map(int,str(input()))) for _ in range(n)]
visited = [[0]*(n) for _ in range(n)]
cnt = 0
size = []
for i in range(n):
    for j in range(n):
        stack = []
        if map[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            danjicnt = 1
            visited[i][j] = 1
            stack.append(tuple([i,j]))
            while stack:
                last = stack.pop()
                for k in range(4):
                    nx = last[0]+dx[k]
                    ny = last[1]+dy[k]
                    if 0<=nx<n and 0<=ny<n and map[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        stack.append(tuple([nx,ny]))
                        danjicnt+=1
            size.append(danjicnt)
print(cnt)
size.sort()
for u in size:
    print(u)
