#!/usr/bin/python3
import random
<<<<<<< HEAD

number = random.randint(-10000, 10000)
lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {} is {} and is greater than 5 ".format(number, lastdigit))
elif lastdigit == 0:
    print("Last digit of {} is {} and is 0 ".format(number, lastdigit))
else:
    print(
        "Last digit of {} is {} and is less than 6 and not 0 ".format(number, lastdigit)
    )
=======
number = random.randint(-10000, 10000)
ld = ("Last digit of ")
if number >= 0:
    last = number % 10
if number < 0:
    last = number % -10
if last > 5:
    print(f"{ld}{number} is {last} and is greater than 5")
elif last == 0:
    print(f"{ld}{number} is {last} and is 0")
else:
    print(f"{ld}{number} is {last} and is less than 6 and not 0")
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
