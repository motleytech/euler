#!/usr/bin/python
from tools.timeit import timeit
from pprint import pprint as pp

problem = """You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

daysNonLeap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysLeap = daysNonLeap[:]
daysLeap[1] = 29

@timeit
def process():
    sundays = 0
    day = (1 + 365) % 7
    
    for x in range(1901, 2001):
        if x % 4 == 0:
            dpm = daysLeap
        else:
            dpm = daysNonLeap
        
        if x == 2000:
            dpm = dpm[:-1]
            
        for days in dpm:
            day = (day + days) % 7
            if day == 0:
                sundays += 1

    value = sundays    
    return value
    
etime, solution = process()

print "Problem :\n%s\n\n\nSolution : %s" % (problem, solution)
print "\nRunning time : %10.6f seconds" % (etime)
