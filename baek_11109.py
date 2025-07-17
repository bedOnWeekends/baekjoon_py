T = int(input())
for i in range(T):
    d, n, s, p = map(int, input().split())
    parallel = d + n * p
    serial = n * s
    result = ""
    if parallel > serial:
        result = "do not parallelize"
    elif parallel == serial:
        result = "does not matter"
    else:
        result = "parallelize"
    print(result)
