#!/bin/python
from tools.general import isPalindrome
from pprint import pprint as pp
from time import time
startt = time()

problem = """Find the largest palindrome made from the product of two 3-digit numbers."""

solution = None

solutions = []
maxmin = 0
N = 1000

for x in xrange(N, N/10 - 1 , -1):
    for y in xrange(x, N/10 - 1, -1):
        value = x*y
        if isPalindrome(value):
            solutions.append((value, x, y))
            if y > maxmin:
                maxmin = y
            break
    if x <= maxmin:
        break

endt = time()

print "%s\n\nSolution : %s" % (problem, max(solutions))
print "\nRunning time : %10.6f seconds" % (endt - startt)

