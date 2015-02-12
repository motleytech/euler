#!/usr/bin/python
from tools.timeit import timeit
from pprint import pprint as pp

problem = """The following iterative sequence is defined for the set of positive integers:

n - n/2 (n is even)
n - 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


def getChainLength(num, cl):
    if num in cl:
        return cl[num]
    else:
        if num % 2 == 0:
            return 1 + getChainLength(num / 2, cl)
        return 1 + getChainLength(3*num + 1, cl)

@timeit
def process():
    chainLength = {1: 1}
    for x in xrange(1, 1000000):
        cl = getChainLength(x, chainLength)
        chainLength[x] = cl
        
    revcl = [(cl, val) for val, cl in chainLength.items()]
    value = "Longest chain length of %s starting at %s" % max(revcl)
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)


