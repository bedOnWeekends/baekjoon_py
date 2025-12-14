T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    edge = []
    for _ in range(M):
        edge.append(list(map(int, input().split())))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edge.append([S, E, -T])

    dist = [0] * (N + 1)

    for i in range(N - 1):
        for c_node, n_node, cost in edge:
            if dist[n_node] > dist[c_node] + cost:
                dist[n_node] = dist[c_node] + cost

    flag = False
    for c_node, n_node, cost in edge:
        if dist[n_node] > dist[c_node] + cost:
            flag = True
            break
    print("YES" if flag else "NO")

