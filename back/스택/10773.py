from collections import deque

k = int(input())

stack = deque()

for _ in range(k):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(list(stack)) if stack else 0)
