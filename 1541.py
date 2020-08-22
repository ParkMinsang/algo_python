#
# 1
#


# mod = list(input())
# equ = []
# sum = 0
# for i in range(len(mod)):
#     if mod[i].isdigit():
#         sum = sum*10 + int(mod[i])
#         if i == len(mod)-1:
#             equ.append(sum)
#     else:
#         equ.append(sum)
#         sum = 0
#         equ.append(mod[i])
#
# check = False
# res = 0
#
# for u in equ:
#     if u != '+' and u != '-':
#         if check == False:
#             res += u
#         else:
#             res -= u
#     elif u == '-':
#         check = True
#
# print(res)

#
# 2
#

b = input().split('-')

res = 0
for u in b[0].split('+'):
    res += int(u)

for u in b[1:]:
    u = u.split('+')
    for v in u:
        res -= int(v)
print(res)
