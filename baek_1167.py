import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V = int(input())

tree = defaultdict(list)

for _ in range(V):
    inp = list(map(int, input().split()))
    v = inp.pop(0)
    inp.pop(-1)
    for i in range(len(inp) // 2):
        tree[v].append((inp[2 * i], inp[2 * i + 1]))

result = [1, 0]

def dfs(visited, node, dist):
    global result

    visited[node] = True

    if dist > result[1]:
        result[0] = node
        result[1] = dist

    for n, w in tree[node]:
        if not visited[n]:
            dfs(visited, n, dist + w)

dfs([False] * (V + 1), 1, 0)
result[1] = 0
dfs([False] * (V + 1), result[0], 0)

print(result[1])
