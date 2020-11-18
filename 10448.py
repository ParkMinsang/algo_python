t = int(input())
ch = []
i = 1
while True:
    l = i*(i+1)//2
    if l > 1000:
        break
    ch.append(l)
    i += 1

for _ in range(t):
    k = int(input())
    check = 0
    for a in ch:
        if check:
            break
        for b in ch:
            if check:
                break
            for c in ch:
                if a+b+c == k:
                    check = 1
                    break
    print(check)
