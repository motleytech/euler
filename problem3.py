#!/usr/bin/python
from tools.timeit import timeit
from tools.primes import factorize

problem = """The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

@timeit
def process():
    num = 600851475143
    factors = factorize(num)
    value = factors[-1][0]
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution :\n%s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
