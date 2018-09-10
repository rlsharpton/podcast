#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

alist = [4, 2, 8, 6, 5]
blist = alist
blist[3] = 999
print(alist)

clist = [4, 2, 8, 6, 5]
dlist = clist * 3
dlist[3] = 999
print(clist)
print(dlist)
dlist.remove(6)
print(dlist)