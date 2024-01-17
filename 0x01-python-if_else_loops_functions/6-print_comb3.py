#!/usr/bin/python3
for num in range(0, 89):
    if num >= 0 and num <= 9:
        print("0{}, ".format(num), end="")
    else:
        print("{}, ".format(num), end="")