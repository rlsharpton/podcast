#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''
a_list = []
#a_set = ()
a_dict = {}


for letter in "Hello World!":
    a_list.append(letter)
    #a_set.add(letter)
    a_dict[letter] = len(a_list)

print("List:", a_list)

list2 = [letter for letter in "Hello World!"]
a_list.append(letter)

#print("Set:", a_set)
print("Dict:", a_dict)

a_list2 = []
for letter in "Hello":
    for letter2 in "world":
        a_list2.append((letter, letter2))

print(a_list2)

new_list = []
data = [[1,2], [4,5],[6,7],[9,8]]
# for row in data:
#     for value in row:
#         new_list.append(value)

#flattened = [value for row in data for value in row]

#multidim = [[value for value in row] for row in data]

#print(flattened)
#print(multidim)

#fizzes = [x if x%3 else "fizz" for x in range(1,50)]
#print(fizzes)
#fizzes_less_buzzes = [x if x%3 else "fizz" for x in range(1,50) if x%5]
#print(fizzes_less_buzzes)

my_comp = [j for j in range(1, 100) if j % 2 == 0]
print(my_comp)

my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)

print(my_list)

my_comp_list = [x * y for x in [[20, 40, 60] for y in [2, 4, 6]]
print(my_comp_list)