N = int(input())
dna = list(input())

conv = {
    'A': 0,
    'G': 1,
    'C': 2,
    'T': 3
}
table = [
    ['A', 'C', 'A', 'G'],
    ['C', 'G', 'T', 'A'],
    ['A', 'T', 'C', 'G'],
    ['G', 'A', 'G', 'T']
]

while len(dna) > 1:
    a = dna.pop()
    b = dna.pop()
    dna.append(table[conv[a]][conv[b]])

print(dna[0])