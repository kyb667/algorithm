n, m = map(int, input().split(' '))
a = []
for _ in range(n):
    a.append(list(map(int, input().split(' '))))

m, k = map(int, input().split(' '))
b = []
for _ in range(m):
    b.append(list(map(int, input().split(' '))))

for x in range(n):
    result = []
    for y in range(k):
        num = 0
        for v1, v2 in zip(a[x], [i[y] for i in b]):
            num += v1 * v2
        result.append(num)
    print(*result, sep=' ')

