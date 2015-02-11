#!/bin/python
from time import time

startt = time()

problem = """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# take product of primes (highest powers less than 20)
solution = 19*17*16*13*11*9*7*5

endt = time()

print "%s\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (endt - startt)

