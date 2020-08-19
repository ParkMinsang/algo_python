p, q = map(int,input().split())
num = []
for i in range(1,p+1):
    if p%i == 0:
        num.append(i)

if len(num) >= q:
    print(num[q-1])
else:
    print(-1)
