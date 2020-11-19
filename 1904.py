n = int(input())

prev1 = 1
prev2 = 2

if n <= 2:
    print(n)
else:
    for i in range(3,n+1):
        prev1, prev2 = prev2%15746, (prev1+prev2)%15746
    print(prev2%15746)
