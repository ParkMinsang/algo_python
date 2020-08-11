from itertools import permutations

n = int(input())
arr = []
ans = 20001

for _ in range(n):
    arr.append(list(map(int,input().split())))

man = list(range(n))

pre_ateam = []
first_bteam = list(range(n//2,n))
cur_ateam = []
cur_bteam = []

def sumpower(a):
    power = 0
    for i in a:
        for j in a:
            power += arr[i][j]
    return power

for u in list(permutations(man)):
    power_ateam = -20001
    power_bteam = 20001

    cur_ateam = list(u[0:n//2])
    cur_ateam.sort()
    if cur_ateam == first_bteam:
        break
    cur_bteam = list(u[n//2:])
    cur_bteam.sort()
    if cur_ateam == pre_ateam: #이전이랑 같은 조합이면 패스
        pass
    else:
        power_ateam = sumpower(cur_ateam)
        power_bteam = sumpower(cur_bteam)

    if abs(power_ateam-power_bteam) < ans: # 두 팀의 전력차가 더 작을 때
        ans = abs(power_ateam-power_bteam)

    pre_ateam = cur_ateam

print(ans)
