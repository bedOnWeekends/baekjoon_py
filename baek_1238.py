import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        cur_dist, now = heapq.heappop(pq)

        if dist[now] < cur_dist:
            continue

        for nxt, cost in graph[now]:
            new_dist = cur_dist + cost
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))

    return dist


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))          # 원래 그래프
    reverse_graph[b].append((a, t))  # 반대 그래프

# X -> i
dist_from_x = dijkstra(X, graph, N)

# i -> X  ==  reverse_graph에서 X -> i
dist_to_x = dijkstra(X, reverse_graph, N)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, dist_to_x[i] + dist_from_x[i])

print(answer)