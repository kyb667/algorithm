from collections import Counter
from functools import reduce
from operator import add, mul

n = int(input())

answer = [0]*n
for i in range(n):
    w = int(input())
    wearDict = [input().split(' ')[1] for _ in range(w)]
    wear = list(Counter(wearDict).values())
    if wear:
        answer[i] = reduce(mul, list(map(add, wear, [1]* len(wear))))-1

print(*answer, sep='\n')
