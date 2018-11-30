#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''


board1 = []
for i in range(5):
    x = list(("O" * 5))
    board1.append(x)


def print_board(board_in):
    for item in board_in:
        print(" ".join(item))


print_board(board1)


letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)