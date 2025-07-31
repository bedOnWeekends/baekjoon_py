import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
y_used = [False] * N


def is_safe(position, x, y):
    for i in range(x):
        if abs(position[i] - y) == abs(i - x):
            return False
    return True


def queen(position, x):
    global cnt

    if x == N:
        cnt += 1
        return

    for y in range(N):
        if y_used[y]:
            continue

        if is_safe(position, x, y):
            position[x] = y
            y_used[y] = True
            queen(position, x + 1)
            y_used[y] = False


queen([0] * N, 0)
print(cnt)