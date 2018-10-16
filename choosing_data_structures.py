#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

# example customer objects
customer1 = {'id': 'abc123', 'full_name': 'Master Yoda'}
customer2 = {'id': 'def456', 'full_name': 'Obi-Wan Kenobi'}
customer3 = {'id': 'ghi789', 'full_name': 'Anakin Skywalker'}

# collect them in a tuple
customers = (customer1, customer2, customer3)
# or collect them in a list
customers = [customer1, customer2, customer3]
# or maybe within a dictionary, they have a unique id after all
customers = {
    'abc123': customer1,
    'def456': customer2,
    'ghi789': customer3,
}

income = 15000
if income < 10000:
    tax_coefficent = 0.0
elif income < 30000:
    tax_coefficent = 0.2
elif income < 100000:
    tax_coefficent = 0.35
else:
    tax_coefficent = 0.45

print('I will pay: ', income * tax_coefficent, 'in taxes')

alert_system = 'console'

order_total = 140
discount = 25 if order_total > 100 else 0
print(order_total, discount)
alert_system.strip('')