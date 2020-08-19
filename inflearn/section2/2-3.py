n, k = map(int,input().split())
lst = list(map(int, input().split()))
num = set()

for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
        for m in range(j+1,len(lst)):
            num.add(lst[i]+lst[j]+lst[m])

num = list(num)
num.sort(reverse = True)

print(num[k-1])
