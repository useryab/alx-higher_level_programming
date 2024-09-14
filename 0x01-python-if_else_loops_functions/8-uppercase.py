#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
<<<<<<< HEAD
        print("{}".format(i), end="")
=======
        print(f"{i}", end="")
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
    print()
