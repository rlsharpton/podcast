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

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result = result + numbers[i]

    return result

print(total(n))

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


# Add your function here
def flatten(lists):
    results = []
    for lst in lists:
        for item in lst:
            results.append(item)

    return results

print(flatten(n))

for countdown in 5, 4, 3, 2, 1, "hey!":
    print(countdown)