n = int(input())
ch = [0]*(n+1)

ch[1] = 2
if n>1:
    ch[2] = 7
if n>2:
    ch[3] = 22
sum2 = 31
for i in range(4,n+1):
    ch[n] = (ch[i-1]*2 + ch[i-2]*3)%1000000007
    sum2 += ch[i-3]*2
    for j in range(3,i+1):
        sum2 += (ch[i-j]<<1)%1000000007

print(ch[n]%1000000007)
