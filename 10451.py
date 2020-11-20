t = int(input())

for _ in range(t):
    n = int(input())
    p = [0]+list(map(int,input().split()))
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        start = i
        next = p[i]
        while start != next:
            visited[next] = 1
            next = p[next]
        cnt += 1
    print(cnt)
