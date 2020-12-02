from collections import deque

dy = [-1,1,-2,2,-2,2,-1,1]
dx = [-2,-2,-1,-1,1,1,2,2]

t = int(input())

for _ in range(t):
    size = int(input())
    board = [[0]*size for _ in range(size)]
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    board[sy][sx] = 1

    q = deque()
    q.append((sx,sy))

    while q:
        get = q.popleft()
        x, y = get[0],get[1]
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<size and 0<= ny<size and board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                q.append((nx,ny))
        if board[ey][ex] != 0:
            print(board[ey][ex]-1)
            break
