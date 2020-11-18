def count(x,y):
    jw,jb = 0,0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if (i+j)%2 == 1 and board[i][j] == 'B':
                jb += 1
            elif (i+j)%2 == 0 and board[i][j] == 'W':
                jw += 1
    ans = min(64-(jw+jb),jw+jb)
    return ans

h, w = map(int,input().split())
board = [list(input()) for _ in range(h)]

res = 64
for p in range(h-7):
    for q in range(w-7):
        res = min(res, count(p,q))

print(res)
