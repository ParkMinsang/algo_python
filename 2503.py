from itertools import permutations

def sol(x,y):
    js, jb = 0,0
    for i in range(3):
        if x[i] == y[i]:
            js += 1
        elif x[i] in y:
            jb += 1
    return js, jb

n = int(input())
nums = ['1','2','3','4','5','6','7','8','9']
case = list(map(''.join,permutations(nums,3)))

for i in range(n):
    num, strike, ball = map(int,input().split())
    num = str(num)
    tmp = set()

    for case_num in case:
        rs,rb = sol(num, case_num)
        if rs == strike and rb == ball:
            tmp.add(case_num)
    case = tmp

print(len(case))
