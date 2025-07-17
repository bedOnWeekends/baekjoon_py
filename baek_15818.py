N, M = map(int, input().split())
remains = map(lambda x: int(x) % M, input().split())
result = 1
for i in remains:
    result = (result * i) % M

print(result)
