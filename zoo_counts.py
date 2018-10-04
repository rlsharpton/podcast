#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

import csv
from collections import Counter

counts = Counter()
with open('zoo.csv', 'rt') as fin:
    cin = csv.reader(fin)
    for num, row in enumerate(cin):
        if num > 0:
            counts[row[0]] += int(row[-1])
for animal, hush in counts.items():
    print("%10s something %10s" % (animal, hush))

