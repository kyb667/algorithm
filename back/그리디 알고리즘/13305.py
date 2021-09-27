n = int(input())
load_len = list(map(int, input().split(' ')))
money = list(map(int, input().split(' ')))[:n-1]

buy = 0

start, finish = 0, len(money)

while 1:
    v1, v2 = load_len[start], money[start]
    buy += v1*v2
    for j in range(start+1, n-1):
        v3 = money[j]
        if v2 < v3 :
            buy += v2 * load_len[j]
            start = j
        else:
            break
    start += 1
    if start == finish:
        print(buy)
        break