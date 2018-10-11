#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

from itertools import count, accumulate
import operator

board1 = []
for i in range(5):
    x = list(("O" * 5))
    board1.append(x)

print(board1)

joe = list(accumulate(range(1, 10), operator.mul))
print(joe)