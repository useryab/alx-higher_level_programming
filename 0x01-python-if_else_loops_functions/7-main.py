#!/usr/bin/env python3

islower = __import__('7-islower').islower
#the code imports a function named islower from a module named 7-islower
#this function is designed to determine whether a given character is lowercase
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
