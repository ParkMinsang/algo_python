n = int(input())
a = input()
stack = []
val = [int(input()) for _ in range(n)]

for i in range(len(a)):
    if not a[i].isalpha():
        ba = stack.pop()
        fr = stack.pop()
        if a[i] == '*':
            stack.append(fr*ba)
        elif a[i] == '/':
            stack.append(fr/ba)
        elif a[i] == '+':
            stack.append(fr+ba)
        else:
            stack.append(fr-ba)
    else:
        stack.append(val[ord(a[i])-65])
print(format(stack[-1],'.2f'))
