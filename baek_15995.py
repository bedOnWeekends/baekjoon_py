a, m = map(int, input().split())

a_prime = 1
while True:
    if (a * a_prime) % m == 1:
        break
    a_prime = a_prime + 1
print(a_prime)