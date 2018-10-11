#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

from itertools import count, cycle
for i in count(0,2):
    if i > 20:
        break
    else:
        print(i)

count = 0
for item in cycle("XYZ"):
    if count > 7:
        break
    print(item)
    count += 1