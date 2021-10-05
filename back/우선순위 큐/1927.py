from sys import stdin
import heapq

n = int(stdin.readline().strip())
que = []
for _ in range(n):
    x = int(stdin.readline().strip())
    if x == 0:
        print(heapq.heappop(que) if que else 0)
    else:
        heapq.heappush(que, x)
