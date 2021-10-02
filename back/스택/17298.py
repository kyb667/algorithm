n = int(input())
a = list(map(int, input().split(' ')))

stack, answer = [], [-1]*len(a)

for index in range(len(a)):
    val = a[index]
    while stack:
        val1 = a[stack[-1]]
        if val > val1:
            answer[stack.pop(-1)] = val
        else:
            break
    stack.append(index)

print(*answer)