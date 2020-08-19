n, m = map(int,input().split())

if n > m: # n이 더 작게 맞춰줌 ( 같으면 상관없음)
    n,m = m,n

#몇개 있냐면
most = m-n+1

for i in range(most):
    print(i+n+1,end = ' ')
