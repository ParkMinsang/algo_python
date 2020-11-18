n = int(input())
ch = [99999]*(4)
ch[1], ch[2], ch[3] = 0, 1, 1

if n > 4:
    ch = [999999]*(n+1)
    ch[1], ch[2], ch[3] = 0,1,1
i = 4
while i <= n:
    if i%2 == 0:
        ch[i] = min(ch[i-1]+1, ch[i//2]+1)
    if i%3 == 0:
        ch[i] = min(ch[i], ch[i-1]+1, ch[i//3]+1)
    ch[i] = min(ch[i-1]+1, ch[i])
    i += 1

print(ch[-1])
