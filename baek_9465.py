import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        continue
    elif n == 2:
        print(max(arr[0][0] + arr[1][1], arr[0][1] + arr[1][0]))
        continue

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))



