#!/usr/bin/python
from tools.timeit import timeit

problem = """A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

@timeit
def process():
    value = None
    for a in xrange(500, 0, -1):
        for b in xrange(a-1, 0, -1):
            c = 1000 - a - b
            aa = a*a
            bb = b*b
            cc = c*c
            if aa == (bb + cc):
                value = (a*b*c)
                break
        if value is not None:
            break    
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
