from itertools import permutations

big = -1000000000
small = 1000000000

n = int(input())
num, tmp = list(map(int,input().split())), [0]*n
ope = list(map(int,input().split()))
operate = []
ans = 0

for i in range(len(ope)):
    while ope[i] > 0:
        operate.append(i)
        ope[i] -= 1
do = []
for u in list(permutations(operate)):
    do.append(u)

do = list(set(do))

for i in range(len(do)):
    for k in range(len(num)):
        tmp[k] = num[k]
    for j in range(len(do[i])):
        # print(tmp,j,do[i][j])
        if do[i][j] == 0:
            tmp[j+1] = tmp[j]+tmp[j+1]
        elif do[i][j] == 1:
            tmp[j+1] = tmp[j]-tmp[j+1]
        elif do[i][j] == 2:
            tmp[j+1] = tmp[j]*tmp[j+1]
        elif do[i][j] == 3:
            if tmp[j] < 0:
                tmp[j+1] = -(-tmp[j]//tmp[j+1])
            else:
                tmp[j+1] = tmp[j]//tmp[j+1]
        if j == len(do[i])-1:
            if tmp[-1] > big:
                big = tmp[-1]
            if tmp[-1] < small:
                small = tmp[-1]
print(big)
print(small)
