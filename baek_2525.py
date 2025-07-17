A, B = map(int, input().split())
C = int(input())

hour = A + C // 60
minute = B + C % 60

if minute >= 60:
    hour += 1
    minute -= 60

print(f"{hour % 24} {minute}")

