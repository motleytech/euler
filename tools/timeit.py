from time import time

def timeit(func):
    def wrapper(*args, **kw):
        stime = time()
        rv = func(*args, **kw)
        etime = time()
        return ((etime - stime), rv)
    return wrapper

        