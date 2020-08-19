n = int(input())
num = list(map(int,input().split()))

max_num = 0

def reverse(x):
    x = list(str(x))
    x.reverse()
    x = int(''.join(x))
    return x

def isPrime(x):
    global ch
    if ch[x] == 0:
        return True
    else:
        return False

for i in range(n): # 뒤집고 제일 큰 수 찾아냄
    num[i] = reverse(num[i])
    if max_num < num[i]:
        max_num = num[i]

ch = [0]*(max_num + 1) # 필요한 만큼 에라토스테네스의 체 배열 생성
ch[1] = 1
for i in range(2, max_num + 1):
    if ch[i] == 0:
        for j in range(2*i, max_num+1, i):
            ch[j] = 1

for u in num:
    if isPrime(u):
        print(u, end = ' ')
