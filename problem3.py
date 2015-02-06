#!/bin/python
from tools.primes import factorize

problem = """The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

num = 600851475143

factors = factorize(num)
solution = factors[-1][0]

print "%s\n\nSolution : %s" % (problem, solution)
