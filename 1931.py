n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key = lambda x:(x[1],x[0]))

rt = lst[0][1]
res = 1
for i in range(1,n):
    if rt <= lst[i][0]:
        res += 1
        rt = lst[i][1]
print(res)
