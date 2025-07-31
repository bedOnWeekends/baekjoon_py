import heapq
import sys
from collections import defaultdict\

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dist = [sys.maxsize] * (V + 1)
heap = [(0, K)]
dist[K] = 0

while heap:
    weight, current = heapq.heappop(heap)

    if weight > dist[current]:
        continue

    for next_node, next_weight in graph[current]:
        next_dist = weight + next_weight

        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(heap, (next_dist, next_node))

for i in range(1, V + 1):
    print(dist[i] if dist[i] != sys.maxsize else "INF")