#!/bin/python

def product(s):
    return reduce(lambda a,b: a*b, s, 1)
    
def mysum(s, initial):
    return reduce(lambda a,b: a+b, s, initial)

def isPalindrome(num):
    num = str(num)

    lnum = len(num)
    if lnum == 1:
        return True
    elif lnum % 2 == 0:
        return num[:lnum/2] == num[lnum-1:lnum/2-1:-1]
    else:
        return num[:lnum/2] == num[lnum-1:lnum/2:-1]

if __name__ == "__main__":
    print product([1,2,3,4,5,6])
	
