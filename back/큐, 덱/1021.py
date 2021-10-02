from collections import deque

n, m = map(int, input().split(' '))
numList = list(map(int, input().split(' ')))

cnt = 0
que = deque(list(range(1, n+1)))

for num in numList:
    if num == que[0]:
        que.popleft()
    elif num == que[-1]:
        que.pop()
        cnt += 1
    else:
        a = que.index(num)
        b = len(que) - a
        if a < b:
            que.rotate(-a)
            que.popleft()
            cnt += a
        else:
            que.rotate(b)
            que.popleft()
            cnt += b
print(cnt)