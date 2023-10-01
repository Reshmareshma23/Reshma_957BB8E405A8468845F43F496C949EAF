# Leap year
"""
year % 4 == 0 &
year % 100 != 0 --> a leap year
year % 400 == 0 --> not a leap year

"""


def isLeapYear(year):
  if (year % 4 == 0 & year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False


year = int(input("Enter the year : "))

if isLeapYear(year):
  print('{} is a leap year .'.format(year))

else:
  print('{} i not a leap year .'.format(year))