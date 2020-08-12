n = int(input())
ans = [n]

for num in range(1000001):
    tmp = num
    tmp2 = []
    while tmp > 0:
        tmp2.append(tmp%10)
        tmp //= 10
    tmp = sum(tmp2)
    if tmp+num == n:
        print(num)
        break
    if num >= n:
        print(0)
        break
