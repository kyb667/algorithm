answer = []
while 1:
    num1, num2 = map(int, input().split(' '))
    if num1 == 0 and num2 == 0:
        print(*answer, sep='\n')
        break
    else:
        return_val = 'neither'
        if divmod(num1, num2)[1] == 0:
            return_val = 'multiple'
        elif divmod(num2, num1)[1] == 0:
            return_val = 'factor'
        answer.append(return_val)