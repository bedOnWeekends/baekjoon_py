import sys

A, B = map(int, input().split())

def mult(num):
    return num * 2

def add_one(num):
    return 10 * num + 1

cnt = sys.maxsize

def calc(num, dep):
    global cnt
    if num > B:
        return
    elif num == B:
        cnt = min(cnt, dep)
        return

    calc(mult(num), dep + 1)
    calc(add_one(num), dep + 1)

calc(A, 0)

if cnt == sys.maxsize:
    print(-1)
else:
    print(cnt + 1)