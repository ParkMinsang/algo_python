n = int(input())
lst = list(map(int,input().split()))
lst.sort()

res = 0
for i in range(n):
    res += lst[i]*(n-i)
print(res)
