import heapq

N, K = map(int, input().split())

heap = [(0, N)]
visited = [False] * 100001

while heap:
    time, current = heapq.heappop(heap)

    if visited[current]:
        continue
    visited[current] = True

    if current == K:
        print(time)
        break

    if 2 * current <= 100000:
        heapq.heappush(heap, (time, 2 * current))

    if current + 1 <= 100000:
        heapq.heappush(heap, (time + 1, current + 1))

    if current - 1 >= 0:
        heapq.heappush(heap, (time + 1, current - 1))
