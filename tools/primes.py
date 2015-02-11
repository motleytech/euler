#!/bin/python
from math import sqrt


def isPrime(x, primes=None):
    limit = int(sqrt(x))
    if primes is None:
        primes = genPrimes(limit)

    divisible = False
    for pr in primes:
        if pr > limit:
            break
        if (x % pr == 0):
            divisible = True
            break

    return (not divisible)


def genPrimes(limit=None):
    if limit is None:
        limit = 999999999
    primes = [2, 3, 5, 7]
    for x in primes:

        yield x

    for x in xrange(11, limit+1, 6):
        a = x
        if isPrime(a, primes):
            primes.append(a)
            yield a

        a = x + 2
        if isPrime(a, primes):
            primes.append(a)
            yield a


def factorize(num):
    if num < 4:
        return [(num, 1)]

    factors = []
    limit = int(sqrt(num))

    for pr in genPrimes(limit):
        facCount = 0
        while (num % pr == 0):
            facCount += 1
            num = num / pr

        if facCount > 0:
            factors.append((pr, facCount))
        if num == 1:
            break

    if num > 1:
        factors.append((num, 1))

    return factors


if __name__ == "__main__":
    from time import time
    for exp in range(2, 5):
        start = time()
        result = [x for x in genPrimes(pow(10, exp))]
        print "Time for primes upto %s = %s" % (pow(10, exp), time() - start)


    print factorize(234324)

