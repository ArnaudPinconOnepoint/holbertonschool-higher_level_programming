#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
  lastDigit = -(lastDigit)
if lastDigit > 5:
  isGreatLess = "is greater than 5"
elif lastDigit == 0:
  isGreatLess = "is 0"
else:
  isGreatLess = "is less than 6 and is not 0"
print(f"Last digit of {number} is {lastDigit} and {isGreatLess}")
