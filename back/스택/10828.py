n = int(input())

stack = []

ansList = []

for _ in range(n):
    ctrl = input()

    if 'push' in ctrl:
        stack.append(int(ctrl.split(' ')[1]))
    elif 'pop' in ctrl:
        ans = stack.pop(-1) if stack else -1
        ansList.append(ans)
    elif 'size' in ctrl:
        ans = len(stack)
        ansList.append(ans)
    elif 'empty' in ctrl:
        ans = 0 if stack else 1
        ansList.append(ans)
    elif 'top' in ctrl:
        ans = stack[-1] if stack else -1
        ansList.append(ans)

print(*ansList, sep='\n')