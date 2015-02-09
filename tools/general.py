#!/bin/python

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
    for x in range(10, 80):
	    if isPalindrome(x):
		    print "%s" % (x)
	