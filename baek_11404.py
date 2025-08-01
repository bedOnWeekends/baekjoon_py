import sys

n = int(input())
m = int(input())

cities = [[sys.maxsize] * n for _ in range(n)]

for i in range(n):
    cities[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cities[a - 1][b - 1] = min(cities[a - 1][b - 1], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            cities[j][k] = min(cities[j][k], cities[j][i] + cities[i][k])

for i in range(n):
    for j in range(n):
        if cities[i][j] == sys.maxsize:
            cities[i][j] = 0

for i in range(n):
    print(' '.join(map(str, cities[i])))
