n, m = map(int, input().split(' '))
_map = []
for x in range(n):
    _map += [(x,y) for y, v in enumerate(list(input())) if v == '1']

answer = [[int(1e9)]*m for _ in range(n)]

que = [(0,0)]
answer[0][0] = 1

while que:
    start = que.pop(0)
    x, y = start
    if start == (n-1, m-1):
        print(answer[n-1][m-1])
        break
    
    val = answer[x][y]
    for i in [(x+1, y),(x-1, y),(x,y-1),(x,y+1)]:
        if i in _map:
            if val+1 < answer[i[0]][i[1]]:
                answer[i[0]][i[1]] = val + 1
                que.append(i)
