#!/usr/bin/python
from tools.timeit import timeit

problem = """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

@timeit
def process():
    # take product of primes (highest powers less than 20)
    value = 19*17*16*13*11*9*7*5
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution :\n%s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
