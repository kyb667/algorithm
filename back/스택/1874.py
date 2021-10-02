n = int(input())

resultList = list(map(int, [input() for _ in range(n)]))

stack, answer = [], []

for i in range(1, n+1):
    if i == resultList[0]:
        resultList.pop(0)
        answer.append('+')
        answer.append('-')
        while 1:
            if stack and resultList and stack[-1] == resultList[0]:
                stack.pop()
                resultList.pop(0)
                answer.append('-')
            else:
                break
    else:
        stack.append(i)
        answer.append('+')
if not stack:
    print(*answer, sep='\n')
else:
    print('NO')
