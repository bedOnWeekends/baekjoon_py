import sys

input = sys.stdin.readline
N = int(input())
graph = [0] * 101

for _ in range(N):
    for num in map(int, input().split()):
        graph[num] += 1

cnt = 0

for i in range(1, 99):
    for j in range(i + 1, 100):
        for k in range(j + 1, 101):
            graph[i] += 1
            graph[j] += 1
            graph[k] += 1
            for l in range(100, 0, -1):
                if graph[l] == 1:
                    if l == i or l == j or l == k:
                        cnt += 1
                        break
                    else:
                        break
            graph[i] -= 1
            graph[j] -= 1
            graph[k] -= 1

print(cnt)



