#!/usr/bin/python3
def fizzbuzz():
<<<<<<< HEAD
    for int in range(1,101):
        if int % 3 == 0:
            print("Fizz ")
        elif int % 5 == 0:
            print("Buzz ")
        elif (int % 5) and (3 == 0):
            print("FizzBuzz ")
        else:
            print("{} ".format(int), end="")
=======
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        print(f"{i} ", end="")
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
