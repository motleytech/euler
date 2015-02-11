#!/usr/bin/python
from tools.timeit import timeit
from pprint import pprint as pp

problem = """Problem statement goes here"""

@timeit
def process():
    value = "Solution goes here."
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
