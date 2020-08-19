n = int(input())
cnt = 0
score = 0
ox = list(map(int,input().split()))

for i in ox:
    if i == 0:
        cnt = 0
    else:
        cnt += 1
        score += cnt
print(score)
