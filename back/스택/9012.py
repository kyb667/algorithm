t = int(input())

answer = []

for _ in range(t):
    s = list(input())
    stack = []
    for i in s:
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(i)
                break
        else:
            stack.append(i)
    answer.append('NO' if stack else 'YES')

print(*answer, sep='\n')
