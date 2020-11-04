# k, n = map(int,input().split())
# lst = [int(input()) for _ in range(k)]
#
# lt = 1
# rt = max(lst)
# res = 1
#
# def func(leng):
#     sum = 0
#     for u in lst:
#         sum += u//leng
#     return sum
#
# while lt <= rt:
#     mid = (lt+rt)//2
#     if func(mid) >= n:
#         res = mid
#         lt = mid+1
#     else:
#         rt = mid-1
#
# print(res)
k, n = map(int,input().split())
rope = []
for _ in range(k):
    rope.append(int(input()))

lt, rt = 1, max(rope)
res = 0

while lt <= rt:
    cnt = 0
    mt = (lt+rt)//2
    for u in rope:
        cnt += (u//mt)
    if cnt < n:
        rt = mt-1
    else:
        res = mt
        lt = mt+1
print(res)
