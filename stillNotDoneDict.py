#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
def average(numbers):
    total = float(sum(numbers))
    return (total / len(numbers))


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (0.1 * homework + 0.3 * quizzes + 0.6 * tests)


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score < 90 and score >= 80:
        return "B"
    elif score < 80 and score >= 70:
        return "C"
    elif score < 70 and score >= 60:
        return "D"
    else:
        return "F"

#print(get_letter_grade(get_average(lloyd)))

class_list = [lloyd, alice, tyler]

for idx in enumerate(class_list):
    print("the index is: {}".format(idx))
    #print("The val is: {}".format(val))

#print(class_list)
def get_class_average(class_list):
    results = []
    results.append(class_list[0])
    print(results[:])
    return 0
    #
    # for stud in range(0, 2):
    #     results.append(get_average(class_list[stud]))
    #
    # what_have_we_done = average(results)
    # print(what_have_we_done)
    # return average(what_have_we_done)

get_class_average(class_list)
# for tt in range(0,3):
#     print(get_average(class_list[tt]))
#     print(' ')