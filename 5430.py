from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    x = deque(eval(input()))
    r = 0
    for i in range(len(p)):
        if p[i] == 'R':
            r += 1
        else:
            if len(x)<=0:
                print('error')
            else:
                if r%2 == 0:
                    x.popleft()
                else:
                    x.pop()
    x = list(x)
    if x:
        if r%2 == 1:
            x.reverse()
        print('[',end='')
        for u in range(len(x)):
            if u < len(x)-1:
                print(x[u],end=',')
            else:
                print(x[u],end='')
        print(']')
