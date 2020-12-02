from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

n, m = map(int,input().split())
mymap = list()
for _ in range(n):
    mymap.append(list(input()))
mymap[0][0] = 1

q = deque()
q.append((0,0))

while q:
    get = q.popleft()
    y,x = get[0],get[1]
    if y==n-1 and x==m-1:
        break
    for k in range(4):
        ny = y+dy[k]
        nx = x+dx[k]
        if 0<=nx<m and 0<=ny<n and mymap[ny][nx] == '1':
            q.append((ny,nx))
            mymap[ny][nx] = mymap[y][x] + 1

print(mymap[-1][-1])

# import sys
# from collections import deque
#
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]
#
# n, m = map(int,input().split())
# mymap = list()
# ans = 0
#
# for _ in range(n):
#     mymap.append(list(map(int,input())))
#
# q = deque()
# q.append((0,0))
#
# while q:
#     ans += 1
#     print(q)
#     for _ in range(len(q)):
#         get = q.popleft()
#         y,x = get[0],get[1]
#         if y==n-1 and x==m-1:
#             print(ans)
#             sys.exit()
#         mymap[y][x] = 0
#         for k in range(4):
#             ny = y+dy[k]
#             nx = x+dx[k]
#             if 0<=nx<m and 0<=ny<n and mymap[ny][nx] == 1:
#                 q.append((ny,nx))
