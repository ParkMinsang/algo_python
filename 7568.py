n = int(input())
mem = []
rank = [1]*n
for _ in range(n):
    mem.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(i+1,n):
        if mem[i][0] > mem[j][0] and mem[i][1] > mem[j][1]: #덩치가 더 큰경우
            rank[j] += 1
        elif mem[i][0] < mem[j][0] and mem[i][1] < mem[j][1]:
            rank[i] += 1
        else:
            continue

print(*rank)
