N = int(input())
arr = list(map(int, input().split()))

dp = [0]
dp += [1001] * N

for i, ele in enumerate(arr):
    idx = i + 1
    for j in range(idx, 0, -1):
        if dp[j - 1] < ele < dp[j]:
            dp[j] = ele
print(max(i for i in range(N + 1) if dp[i] < 1001))