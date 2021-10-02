sList, answer = [], []
while 1:
    s = input()
    if s == '.':
        break
    else:
        sList.append(s)

for s in sList:
    s = list(s)
    stack = []
    for i in s:
        n = ord(i)
        if n not in (93, 41, 40, 91):
            continue
        if n == 93:
            if stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                stack.append(i)
                break
        elif n == 41:
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(i)
                break
        elif n in (40, 91):
            stack.append(i)
    answer.append( 'yes' if not stack else 'no')

print(*answer, sep='\n')