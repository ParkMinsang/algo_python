n = int(input())
lst1 = list(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))

lst1.sort()
for u in lst2:
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt+rt)//2
        if lst1[mid] < u:
            lt = mid+1
        elif lst1[mid] > u:
            rt = mid-1
        else: # u 발견
            left = right = cnt = 0
            if lst1[0] == u:
                left = 0
                cnt += 1
            else:
                slt, srt = 0, n-1
                while slt <= srt: # 제일 왼쪽 편 찾기
                    smid = (slt+srt)//2
                    if lst1[smid] < u:
                        if lst1[smid+1] == u:
                            left = smid
                            break
                        else:
                            slt = smid+1
                    else:
                        srt = smid-1

            if lst1[n-1] == u:
                right = n-1
                cnt += 1
            else:
                slt, srt = 0, n-1
                while slt <= srt:
                    smid = (slt+srt)//2
                    if lst1[smid] > u:
                        if lst1[smid-1] == u:
                            right = smid
                            break
                        else:
                            srt = smid-1
                    else:
                        slt = smid+1
            print(right-left-1+cnt)
            break
    if lt > rt:
        print(0)
