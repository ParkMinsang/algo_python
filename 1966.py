from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    num = list(map(int,input().split()))
    check_val = sorted(num)
    cnt = 0
    dq = deque()
    for idx, val in enumerate(num):
        dq.append((idx,val))
    while dq:
        get = dq.popleft()
        if get[1] == check_val[-1]:
            cnt+=1
            check_val.pop()
            if get[0] == k:
                print(cnt)
                break
        else:
            dq.append(get)
