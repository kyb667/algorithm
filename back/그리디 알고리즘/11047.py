n, k = map(int, input().split(' '))
moneyList = [int(input()) for _ in range(n)]

cnt = 0
while k:
    money = moneyList.pop(-1)
    a, b = divmod(k, money)
    if a == 0:
        continue
    else:
        cnt += a
        k = b
print(cnt)