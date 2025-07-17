


N = int(input())

ans = 0

for i in range(N + 1):
    for j in range(i + 1):
        ans += i + j



print(ans)