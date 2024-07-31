# import this
# import math
from math import *

# def print(*args):
#     return 'Ok'

def sqr(x):
    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    return d


a = 5
b = sqr(2)
print(a)
print(b)
# print(d)
print(globals())
