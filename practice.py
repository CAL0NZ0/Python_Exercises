# This appends a new line on an existing .txt file

# with open('practice.txt', "a") as file:
#   file.write('\nIan')

# This rounds up with 1 decimal point. It's also the equation for converting radians to degrees.

# from math import pi
# rad = 1
# def rad2deg(rad):
#   deg = round((1*rad) * (180/pi),1)
#   return deg


def relation_to_luke(name):
  if name == 'Darth Vader':
    return "Luke, I am your father."
  elif name == 'Leia':
    return "Luke, I am your sister."
  elif name == 'Han':
    return 'Luke, I am your brother in law.'
  else:
    return 'Luke, I am your droid.'
