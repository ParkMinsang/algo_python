n,m = map(int,input().split())
lst = list(map(int,input().split()))

lt = 1
rt = max(lst)
res = 0

def func(a):
    sum = 0
    for u in lst:
        if u-a > 0:
            sum += (u-a)
    return sum

while lt <= rt:
    mid = (lt+rt)//2
    if func(mid) >= m:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
