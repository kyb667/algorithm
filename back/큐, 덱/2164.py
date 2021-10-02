from collections import deque

n = int(input())

cardList = deque(list(range(1,n+1)))

while cardList:
    a = cardList.popleft()
    if len(cardList) == 1:
        print(cardList.pop())
        break
    elif not cardList:
        print(a)
        break
    cardList.append(cardList.popleft())