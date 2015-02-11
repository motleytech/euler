#!/bin/python
from time import time

startt = time()

problem = """
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# take product of primes (highest powers less than 20)
solution = sum((x*x) for x in range(1,101)) - pow(sum(range(1,101)),2)

endt = time()

print "%s\n\nSolution : %s" % (problem, -solution)
print "\nRunning time : %10.6f seconds" % (endt - startt)
