from sys import stdin
from copy import deepcopy

home = []
for i in range(int(stdin.readline().strip())):
    a = list(stdin.readline().strip())
    for index, j in enumerate(a):
        if j == '1':
            home.append((i,index))

def solve(start):
    dump = deepcopy(home)
    x, y = start
    for i in dump:
        x1, y1 = i
        if i in home and ((x1 == x and y1 == y-1) or (x1 == x and y1 == y+1) \
            or (x1 == x-1 and y1 == y) or (x1 == x+1 and y1 == y)):
            print(i)
            home.remove(i)
            findList[-1] = findList[-1]+1
            solve(i)
            dump = deepcopy(home)
    return

findList = []
while home:
    start = home.pop(0)
    findList.append(1)
    solve(start)
print(len(findList))
print(*sorted(findList), sep='\n')
