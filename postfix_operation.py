n = list(input())
stack = []

dic = {'(':3,'+':1,'-':1,'*':2,'/':2}
ope = []

for u in n:
    if u.isdigit(): # 숫자면 무적권 넣음
        stack.append(u)
    elif u == ')':
        while ope[-1] != '(':
            stack.append(ope.pop())
        ope.pop()
    else:
        while ope and dic[ope[-1]] <= 2 and dic[u] <= dic[ope[-1]]:
            stack.append(ope.pop())
        ope.append(u)

while ope:
    stack.append(ope.pop())

print(''.join(stack))
