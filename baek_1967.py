import sys
from collections import defaultdict

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

result = [1, 0]
def dfs(visited, node, dist):
    visited[node] = True
    if dist > result[1]:
        result[0] = node
        result[1] = dist

    for next_node, next_weight in graph[node]:
        if not visited[next_node]:
            dfs(visited, next_node, dist + next_weight)

dfs([False] * (n + 1), 1, 0)
first_node = result[0]
result = [first_node, 0]
dfs([False] * (n + 1), first_node, 0)
print(result[1])





