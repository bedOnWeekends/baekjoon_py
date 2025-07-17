import math
message = input()
N = len(message)
R = 1
for i in range(int(math.floor(math.sqrt(N)))):
    if N % (i + 1) == 0:
        R = i + 1
C = N // R
arr = [message[i:i + R] for i in range(0, len(message), R)]
ans = ''
for i in range(R):
    for ele in arr:
        ans += ele[i]

print(ans)

