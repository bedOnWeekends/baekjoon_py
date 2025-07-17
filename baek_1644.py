num = int(input())
is_prime = [True] * (num + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(num ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, num + 1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

def find_prime_continuous_sum(target):
    start, end = 0, 0
    current_sum = 0
    count = 0

    while end < len(primes):
        current_sum += primes[end]
        end += 1

        while current_sum > target and start < end:
            current_sum -= primes[start]
            start += 1

        if current_sum == target:
            count += 1

    return count

print(find_prime_continuous_sum(num))
