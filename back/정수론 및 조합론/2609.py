from math import gcd

num1, num2 = map(int, input().split(' '))
a = gcd(num1, num2)
print(a)
print(int((num1*num2)//a))