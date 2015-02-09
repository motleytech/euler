#!/bin/python
from tools.general import isPalindrome
from pprint import pprint as pp
from time import time
startt = time()

problem = """Find the largest palindrome made from the product of two 3-digit numbers."""

solution = None

solutions = []
maxmin = 0

for x in xrange(1000, 99, -1):
    for y in xrange(x, 99, -1):
        value = x*y
        if isPalindrome(value):
            solutions.append((value, x, y))
            if y > maxmin:
                maxmin = y
    if x <= maxmin:
        break

endt = time()

print "%s\n\nSolution : %s" % (problem, max(solutions))
print "\nRunning time : %10.6f seconds" % (endt - startt)

