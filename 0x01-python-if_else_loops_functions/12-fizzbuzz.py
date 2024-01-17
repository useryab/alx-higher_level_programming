#!/usr/bin/python3
def fizzbuzz():
    for int in range(1,101):
        if int % 3 == 0:
            print("Fizz ")
        elif int % 5 == 0:
            print("Buzz ")
        elif (int % 5) and (3 == 0):
            print("FizzBuzz ")
        else:
            print("{} ".format(int), end="")