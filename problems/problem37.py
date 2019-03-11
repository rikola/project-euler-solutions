
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

def checkTruncation(n, primes):
    if not primes[n]:
        return False

    # Check left truncation
    cur = n
    while cur >= 10:
        stringCur  = str(cur)[1:]
        cur = int(stringCur)
        if not primes[cur]:
            return False

    cur = n
    while cur >= 10:
        cur = cur // 10
        if not primes[cur]:
            return False
    return True

limit = 1000000
primes = sieve(limit)

truncatablePrimes = []
for i in range(8, limit):
    result = checkTruncation(i, primes)
    if result:
        truncatablePrimes.append(i)

print(sum(truncatablePrimes))
