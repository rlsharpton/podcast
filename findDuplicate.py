#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

def firstDuplicate(a):
    ''' Should return the value and index of the first duplicate. '''
    for i in a:
        y = a.count(i)
        if y >  1:
            idx = a.index(i)
            val = i
        else:
            pass
    return idx, val

my_list = [2, 3, 1, 3, 5, 2, 8, 7]
print(firstDuplicate(my_list))
#print(firstDuplicate(my_list))

class Bike:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")

red_bike = Bike('Red', 'Carbon_fiber')
blue_bike = Bike('Blue', 'Steel')

print(red_bike.color)

blue_bike.brake()

