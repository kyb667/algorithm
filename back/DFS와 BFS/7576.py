from sys import stdin
from collections import deque
m, n = map(int, stdin.readline().strip().split(' '))

tomato, que = [], deque([])

for x in range(n):
    tomato.append(list(map(int, stdin.readline().strip().split(' '))))
    for y, v in enumerate(tomato[x]):
        if v == 1:
            que.append((x,y))

while que:
    x, y = que.popleft()

    for v in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        x1, y1 = v
        if 0<=x1<n and 0<=y1<m and tomato[x1][y1] == 0:
            que.append(v)
            tomato[x1][y1] = tomato[x][y] + 1

cnt = 0

for i in tomato:
    if 0 in list(set(i)):
        print(-1)
        exit(0)
    else:
        cnt = max(cnt, max(i))
print(cnt-1)