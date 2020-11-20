t = int(input())

for _ in range(t):
    n = int(input())
    cycle = [0]+list(map(int,input().split()))
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        stack = [(i,cycle[i])]
        if visited[i] == 1:
            continue
        code = True
        while code:
            j = cycle[i]
            if visited[cycle[j]] == 1:
                break
            stack.append((j,cycle[j]))
            for k in range(len(stack)):
                if stack[k][0] == stack[-1][1]:
                    cnt += (len(stack)-k)
                    code = False
            else:
                code = False
            print(stack)
    print(cnt)
