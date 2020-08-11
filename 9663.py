n = int(input())

count = 0
arr = []

def check():
    global count
    global arr
    if len(arr) == n:
        count+=1
        return
    x = len(arr)
    for y in range(n):
        for u in arr:
            if x != u[0] and y != u[1] and (x+y != u[0]+u[1]) and abs(x-u[0]) != abs(y-u[1]):
                pass
            else:
                break
        else:
            arr.append([x,y])
            check()
            arr.pop()

for i in range(n):
    arr.append([0,i])
    check()
    arr.pop()

print(count)
