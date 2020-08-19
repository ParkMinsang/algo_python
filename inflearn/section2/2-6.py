n = int(input())

num = list(map(int,input().split()))
ans_max = 0
ans = 0
for i in range(n):
    sum = 0 # 각 자리 수를 합치는 공간
    s = num[i]
    while s > 0:
        sum += s%10
        s //= 10
    if ans_max < sum:
        ans_max = sum
        ans = num[i]

print(ans)
