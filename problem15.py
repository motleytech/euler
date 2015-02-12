#!/usr/bin/python
from tools.timeit import timeit
from pprint import pprint as pp
from tools.general import nChooseR

problem = """Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?"""

@timeit
def process():
    # This is equivalent to choosing 20 downs in a path of length 40
    # which has other 20 rights. 40C20
    value = nChooseR(40, 20)
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
