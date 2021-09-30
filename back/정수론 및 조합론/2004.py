n, m = map(int, input().split(' '))

def calc(n, num):
    cnt = 0
    while n != 0:
        n //= num
        cnt += n
    return cnt

a = (calc(n, 2)-calc(m, 2)-calc(n-m, 2))
b = (calc(n, 5)-calc(m, 5)-calc(n-m, 5))
print(min(a, b))