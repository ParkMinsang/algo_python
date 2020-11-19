n = int(input())
ch = [999999]*(n+1)
ch[0] = 0
ch[1] = 1
if n>1:
    ch[2] = 2

for i in range(3,n+1):
    for j in range(1,i):
        if i-j**2<0:
            break
        ch[i] = min(ch[i],ch[i-j**2]+1)

print(ch[-1])
