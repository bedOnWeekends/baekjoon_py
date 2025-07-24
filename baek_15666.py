N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
history = []
def backtrack(pick, idx, dep):
    if dep == M:
        if pick not in history:
            print(' '.join(map(str, pick)))
            history.append(pick[:])
        return
    for i in range(idx, N):
        pick.append(arr[i])
        backtrack(pick, i, dep + 1)
        pick.pop()

backtrack([], 0, 0)



