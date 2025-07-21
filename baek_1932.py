n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = triangle[0][0]
for i in range(n - 1):
    for j in range(i + 2):
        if j == 0:
            dp[i + 1][j] = dp[i][j] + triangle[i + 1][j]
        elif j == i + 1:
            dp[i + 1][j] = dp[i][j - 1] + triangle[i + 1][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - 1]) + triangle[i + 1][j]

print(max(dp[-1]))


