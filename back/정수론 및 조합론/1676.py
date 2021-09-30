n = int(input())

cnt = 0

while n > 4:
    a, b = divmod(n, 5)
    if b == 0:
        cnt += 1
        if a% 5 == 0:
            c = 5
            while 1:
                if c% 5 != 0:
                    break
                else:
                    c, d = divmod(a, 5)
                    cnt += 1
                    a = c
    n = n - 5 if b == 0 else n - b

print(cnt)