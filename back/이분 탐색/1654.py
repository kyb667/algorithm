from sys import stdin

k, n = map(int, stdin.readline().strip().split(' '))
lineList = [int(stdin.readline().strip()) for _ in range(k)]

start = 1
end = max(lineList)
answer = 0
while start <= end:
    mod = (start+end)//2
    valList = [ (val // mod) for val in lineList]
    sumNum = sum(valList)
    if sumNum < n:
        end = mod - 1
    elif sumNum >= n:
        if answer < mod:
            answer = mod
        start = mod +1
print(answer)
