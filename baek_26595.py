N = int(input())
a, pa, b, pb = map(int, input().split())


max_val = 0
ans_a = 0
ans_b = 0
max_cnt = N // pa
for cnt in range(max_cnt + 1):
    remain = (N - cnt * pa) // pb
    power = a * cnt + b * remain
    if power > max_val:
        max_val = power
        ans_a = cnt
        ans_b = remain

print(f'{ans_a} {ans_b}')


