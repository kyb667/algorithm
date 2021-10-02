import sys
from collections import deque
n = int(input())

que, answer = deque(), []

for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == 'push':
        que.append(int(op[1]))
    elif op[0] == 'pop':
        print(que.popleft() if que else -1)
    elif op[0] == 'size':
        print(len(que))
    elif op[0] == 'empty':
        print(0 if que else 1)
    elif op[0] == 'front':
        print(que[0] if que else -1)
    elif op[0] == 'back':
        print(que[-1] if que else -1)