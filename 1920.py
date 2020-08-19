n = int(input())
lst1 = list(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))

lst1.sort()

for u in lst2:
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt+rt)//2
        if lst1[mid] < u:
            lt = mid+1
        elif lst1[mid] > u:
            rt = mid-1
        else:
            print(1)
            break
    if lt > rt:
        print(0)
