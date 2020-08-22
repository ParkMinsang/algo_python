arr = []
ans = 'YES'
for _ in range(9):
    arr += list(map(int,input().split()))

check = {1,2,3,4,5,6,7,8,9}

for i in range(9): #가로 세로 검사 껕
    comh = set()
    comv = set()
    comg = set()
    for j in range(9):
        comh.add(arr[i*9 + j])
        comv.add(arr[i + j*9])
    for m in range(3):
        for k in range(3):
            comg.add(arr[27*(i//3) + 3*i - 9*(i//3) + 9*m + k])
    if len(check - comh) != 0 or len(check - comv) != 0 or len(check - comg) != 0:
        ans = 'NO'
        break

print(ans)
