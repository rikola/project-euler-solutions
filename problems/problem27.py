
def sieve(end):
    primes = [True] * (end+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, end+1):
        if primes[i]:
            cur = i
            while cur <= end:
                cur += i
                if cur <= end:
                    primes[cur] = False
    return primes

def quadratic(n, a, b):
    return pow(n, 2) + (a * n) + b

def countPrimes(a, b, primes):
    n = 0
    while primes[quadratic(n, a, b)]:
        n += 1
    return n


primes = sieve(1000000)

maxA = 0
maxB = 0
maxCount = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        result = countPrimes(a, b, primes)
        if result > maxCount:
            maxA = a
            maxB = b
            maxCount = result


print((maxA * maxB), maxCount)
