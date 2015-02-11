#!/usr/bin/python
from tools.timeit import timeit
from tools.general import isPalindrome

problem = """Find the largest palindrome made from the product of two 3-digit numbers."""

@timeit
def process():
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

    value = max(solutions)
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution :\n%s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)

