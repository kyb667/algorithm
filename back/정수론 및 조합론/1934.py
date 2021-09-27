from math import gcd

answer = []
n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split(' '))
    a = gcd(num1, num2)
    answer.append(int((num1*num2)//a))
print(*answer, sep='\n')