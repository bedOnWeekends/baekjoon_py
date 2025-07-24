N, M = map(int, input().split())

for _ in range(N):
    s = input()
    stack = []
    for char in s:
        stack.append(char)
    rev = ""
    while stack:
        rev += stack.pop()
    print(rev)

