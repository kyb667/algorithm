from sys import stdin

n, m = map(int, stdin.readline().strip().split(' '))
treeList = list(map(int, stdin.readline().strip().split(' ')))

start, end = 0, max(treeList)
h = 0

while start <= end:
    mid = (start + end) // 2

    tree_sum = sum([i - mid for i in treeList if i - mid >= 0])

    if tree_sum < m:
        end = mid -1
        continue
    elif tree_sum >= m:
        if h < mid:
            h = mid
    start = mid + 1

print(h)