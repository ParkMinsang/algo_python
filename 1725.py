n = int(input())
h = [int(input()) for _ in range(n)]
ans = 0

for i in range(n):
    res = h[i]
    rowest = h[i]
    for j in range(i-1,-1,-1):
        rowest = min(rowest, h[j])
        if res > rowest*(i-j+1):
            break
        else:
            res = rowest*(i-j+1)
    ans = max(ans,res)
print(ans)
