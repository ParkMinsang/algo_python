n = int(input())
score = list(map(int,input().split()))
mean = round(sum(score)/n)

ansMin = [100, 0, 0] #평균 차이, 점수, 번호
for i in range(n):
    if abs(round(mean-score[i])) == ansMin[0]: # 거리가 똑같을 때
        if score[i] > ansMin[1]: # 점수가 더 높으면 바꿈
            ansMin[0] = abs(round(mean-score[i]))
            ansMin[1] = score[i]
            ansMin[2] = i+1
    elif abs(round(mean-score[i])) < ansMin[0]: # 평균과 더 가까우면 바꿈
        ansMin[0] = abs(round(mean-score[i]))
        ansMin[1] = score[i]
        ansMin[2] = i+1
print(mean, ansMin[2])
