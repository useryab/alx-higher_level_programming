#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number = number % 10
    else:
        number = (number % -10) * -1
    print(number, end="")
<<<<<<< HEAD
    return number
=======
    return (number)
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
