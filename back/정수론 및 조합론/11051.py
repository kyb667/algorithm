n, k = map(int, input().split(' '))

dp = [[1 for _ in range(k+1)] for _ in range(n+1)]

for x in range(1, k+1):
    for y in range(x+1, n+1):
        dp[y][x] = (dp[y-1][x-1] + dp[y-1][x]) % 10007

print(dp[n][k])