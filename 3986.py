n = int(input())
cnt = 0
for _ in range(n):
    stack = []
    word = input()
    for i in range(len(word)):
        if stack and stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])
    if not stack:
        cnt += 1
print(cnt)
