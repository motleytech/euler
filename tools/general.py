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

def factorial(n):
    if n < 2:
        return 1
    return product(xrange(2, n+1))

def nChooseR(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))
    

ones = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

tens = [
    '',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]


orders = [
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'pentillion',
    'sextrillion',
    'septillion',
    'octillion',
    'gazillion',
]

def numl1000(num):
    rv = ''
    if num >= 100:
        rv += ones[num / 100] + ' hundred'
        num = num % 100
        if num > 0:
            rv += ' and '
        
    if num == 0:
        rv += ''
    elif 1 <= num <= 9:
        rv += ones[num]
    elif 10 <= num <= 19:
        rv += teens[num - 10]
    elif 20 <= num <= 99:
        rv += tens[num / 10]
        num = num % 10
        if num > 0:
            rv += ' ' + ones[num]
    return rv

def num2words(num):
    orignum = num
    if num == 0:
        return "zero"
    words = ""
    while num > 0:
        top3 = num
        order = 0
        while top3 >= 1000:
            top3 = top3 / 1000
            order += 1
        
        if num < 100 and orignum >= 1000:
            words += " and"
        words += " " + numl1000(top3)
                
        if order > 0:
            words += " " + orders[order]
            
        num = num % pow(1000, order)
    return words
    

if __name__ == "__main__":
    x = 100002007
    print "%4s : %s" % (x, num2words(x))
	
