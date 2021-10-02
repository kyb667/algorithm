a, b, c = map(int, input().split(' '))

def solve(a, b):
    if b == 1:
        return a%c
    val = solve(a, b//2)

    if b%2 == 0:
        return (val * val)%c
    else:
        return (val * val * a)%c

a = solve(a, b)
print(a)