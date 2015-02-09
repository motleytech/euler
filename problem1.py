#!/bin/python
from time import time

startt = time()

problem = """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

solution = None

solution = sum([x for x in xrange(1000) if (x % 3 == 0) or (x % 5 == 0)])

endt = time()

print "%s\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (endt - startt)

