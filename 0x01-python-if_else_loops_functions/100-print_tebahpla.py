#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        i = i - 32
    else:
        i = i
<<<<<<< HEAD
    print("{}".format(chr(i)), end="")
=======
print(f"{i}", end="")
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
