N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtrack(used, path, dep):
    if dep == M:
        print(' '.join(map(str, path)))
        return

    prev = -1
    for i in range(N):
        if not used[i] and arr[i] != prev:
            used[i] = True
            path.append(arr[i])
            prev = arr[i]
            backtrack(used, path, dep + 1)
            used[i] = False
            path.pop()



used = [False] * N
backtrack(used, [], 0)