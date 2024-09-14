#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i < 8:
<<<<<<< HEAD
                print("{}{}, ".format(i, j), end="")
            else:
                    print("{}{}".format(i, j))
=======
                print(f"{i}{j}, ", end="")
            else:
                print(f"{i}{j}")
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
