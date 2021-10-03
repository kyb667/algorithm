def calc(cal, a):
    l = len(cal)
    re_val = []
    for x in range(l):
        result = []
        for y in range(l):
            num = 0
            for v1, v2 in zip(cal[x], [i[y] for i in a]):
                num += (v1 * v2)
            result.append(num%1000)
        re_val.append(result)
    return re_val

def solve(a, num):
    if num == 2:
        return calc(a,a)
    elif num == 1:
        b = []
        for i in a:
            r = []
            for j in i:
                r.append(j%1000)
            b.append(r)
        return b
    cal = solve(a, num//2)
    if num%2 == 0:
        return calc(cal,cal)
    else:
        return calc(calc(cal,cal),a)

from sys import stdin
n, b = map(int, input().split(' '))

a = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(n)]

answer = solve(a, b)
for i in answer:
    print(*i, sep=' ')