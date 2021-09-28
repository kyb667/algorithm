from math import factorial

t = int(input())
loadList = [list(map(int, input().split(' '))) for _ in range(t)]

for i in loadList:
    m, n = i
    print(int(factorial(n) / (factorial(n-m) * factorial(m))))
