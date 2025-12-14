N = int(input())
arr = list(map(int, input().split()))

for i in range(N - 2, -1, -1):
    arr[i] = min(arr[i], arr[i + 1])

print(sum(arr))
