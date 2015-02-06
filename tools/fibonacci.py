#!/bin/python

def genFib(limit):
    a, b = 1, 2
    yield a
    while b < limit:
        yield b
        a, b = b, a+b

