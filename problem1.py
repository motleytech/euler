#!/usr/bin/python
from tools.timeit import timeit

problem = """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

@timeit
def process():
    return sum([x for x in xrange(1000) if (x % 3 == 0) or (x % 5 == 0)])
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution :\n%s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
