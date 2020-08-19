n, c = map(int,input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

lt = 1
rt = lst[-1]
res = 0

def func(a):
    cnt = 1
    start = lst[0]
    for u in lst:
        if u-start>=a:
            cnt += 1
            start = u
    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if func(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
