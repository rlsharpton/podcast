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
  print("homework total is: {}".format(homework))
  quizzes = average(student["quizzes"])
  print("quizzes are: {}".format(quizzes))
  tests = average(student["tests"])
  print("tests are: {}".format(tests))
  results = (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)
  print("results are: {}".format(results))
  return results

print(get_average(alice))


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

    print("The grade is: {}".format(get_letter_grade(get_average(lloyd))))