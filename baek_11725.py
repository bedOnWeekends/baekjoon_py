from collections import defaultdict, deque

N = int(input())

tree = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])
parents = [0] * (N + 1)
visited = [False] * (N + 1)
visited[1] = True

while queue:
    current = queue.popleft()
    for child in tree[current]:
        if not visited[child]:
            queue.append(child)
            parents[child] = current
            visited[child] = True

for ele in parents[2:]:
    print(ele)
