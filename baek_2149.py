sorted_key = list(input())
enc = list(input())

key = sorted_key.copy()
sorted_key.sort()
table = {}

cnt = len(enc) // len(sorted_key)

for i, k in enumerate(sorted_key):
    table[k + str(i)] = enc[cnt * i:cnt * i + cnt]

result = []

for i in key:
    cand = []
    for j in table.keys():
        if i in j:
            cand.append(j)
    cand.sort()
    result.append(table[cand[0]])
    table.pop(cand[0])

ans = [''] * len(enc)

for i in range(len(result)):
    for j, chara in enumerate(result[i]):
        ans[i + len(sorted_key) * j] = chara

print(''.join(ans))




