n, k = map(int,input().split())
if n-k < k:
    k = n-k

denomitor = 1
molecular = 1

for i in range(n-k+1,n+1):
    denomitor *= i
    molecular *= i-n+k
    
print(denomitor//molecular%10007)
