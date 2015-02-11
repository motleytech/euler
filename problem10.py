#!/usr/bin/python
from tools.timeit import timeit
from tools.primes import genPrimes

problem = """The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

@timeit
def process():
    value = sum(x for x in genPrimes(2000000 - 1))
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
