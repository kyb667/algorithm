from sys import stdin

def solve(tree):
    val = list(set(sum(tree,[])))
    if len(val) == 1:
        return val[0]
    else:
        length = int(len(tree)/2)
        a, b, c, d = (0, 0), (0, length), (length, 0), (length, length)
        string = ''
        for i in [a,b,c,d]:
            start, end = i
            dump = []
            for x in range(length):
                dump.append(tree[x+start][end:end+length])
            string += solve(dump)
        return '('+string+')'

n = int(input())

tree = []

for _ in range(n):
    tree.append(list(stdin.readline().strip()))

print(solve(tree))
