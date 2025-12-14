bs, bc, bo, bn = map(int, input().split())

bsn = bs + bn
bco = bc + 2 * bo

print(min(bsn // 3, bco // 6))
