s = input()
n = int(input())
a = set(input() for _ in range(n))
h = []

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j] in a:
            h.append((i,j))
h.sort()
