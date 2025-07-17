N, K = map(int, input().split())
table = []
own = {}
for _ in range(N):
    num, gold, silver, bronze = map(int, input().split())
    table.append([gold, silver, bronze])
    own[num] = [gold, silver, bronze]

table.sort(reverse=True)

print(table.index(own[K]) + 1)






