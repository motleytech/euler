#!/usr/bin/python
from tools.timeit import timeit
from pprint import pprint as pp

problem = """215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

@timeit
def process():
    value = sum(int(x) for x in str(pow(2, 1000)))
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
