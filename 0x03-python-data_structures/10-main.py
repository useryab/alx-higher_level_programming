<<<<<<< HEAD
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print(f"{:d} {:s} divisible by 2".format(my_list[i], \
         "is" if list_result[i] else "is not"))
    i += 1
    
=======
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(
        my_list[i], "is" if list_result[i] else "is not"))
    i += 1
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
