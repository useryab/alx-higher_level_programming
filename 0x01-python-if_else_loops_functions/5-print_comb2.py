#!/usr/bin/python3
for num in range(0, 99):
    if num >= 0 and num <= 9:
        print("0{}, ".format(num))
    else:
        print("{}, ".format(num))