from sys import stdin
from collections import defaultdict
from copy import deepcopy

n = int(stdin.readline().strip())

computer_line = defaultdict(list)

check = {}

for _ in range(int(stdin.readline().strip())):
    a, b = map(int, stdin.readline().strip().split(' '))
    computer_line[a].append(b)
    computer_line[b].append(a)

    check[a] = 0
    check[b] = 0

check[1] = 1

def solve(num):
    dump = deepcopy(computer_line)
    if num in dump:
        for i in dump[num]:
            if check[i] == 0:
                check[i] = 1
                computer_line[num].remove(i)
                solve(i)
    return

solve(1)
print(sum(check.values())-1)