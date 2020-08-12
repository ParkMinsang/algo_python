n,m = map(int,input().split())
base_board = []
ans_min = 2500

for _ in range(n):
    base_board.append(tuple(input()))

def count_work(n,m):
    count_black = 0
    count_white = 0
    for i in range(n,n+8):
        for j in range(m,m+8):
            if (i-n + j-n) %2 == 1:
                if base_board[i][j] != 'W':
                    count_black += 1
                else:
                    count_white += 1
            else :
                if base_board[i][j] != 'B':
                    count_black += 1
                else:
                    count_white += 1
    return min(count_black,count_white)

for i in range(n-7):
    for j in range(m-7):
        ans_min = min(ans_min,count_work(i,j))

print(ans_min)
