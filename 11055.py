n = int(input())
num = list(map(int,input().split()))
dp = [0]*n
dp[0] = num[0]

for i in range(1,n):
    tmp = []
    for j in range(i):
        if num[i] > num[j]:
            tmp.append(dp[j])
    dp[i] = num[i]
    if tmp:
        dp[i] += max(tmp)

print(max(dp))
