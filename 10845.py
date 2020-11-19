from collections import deque
import sys

n = int(sys.stdin.readline().rstrip().split()[0])
ans = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        ans.append(command[1])
    elif command[0] == 'pop':
        if ans:
            print(ans.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(ans))
    elif command[0] == 'empty':
        if ans:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if ans:
            print(ans[0])
        else:
            print(-1)
    else:
        if ans:
            print(ans[-1])
        else:
            print(-1)
