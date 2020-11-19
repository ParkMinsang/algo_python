n = int(input())
ch = [0]*(n+1)

ch[1] = 1
if n>1:
    ch[2]=3

for i in range(3,n+1):
    ch[i] = ch[i-1]%10007 + 2*ch[i-2]%10007

print(ch[-1]%10007)
