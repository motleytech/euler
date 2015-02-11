#!/bin/python
from tools.primes import genPrimes
from tools.timeit import timeit

problem = """\
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

@timeit
def process():
    # take product of primes (highest powers less than 20)
    N = 10001
    idx = 0
    for x in genPrimes():
        idx += 1
        if idx >= N:
            break
            
    return "%sth prime is %s" % (N, x) 
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution :\n%s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
