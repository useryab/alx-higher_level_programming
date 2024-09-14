<<<<<<< HEAD
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        list[idx] = element
        return list
=======
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lst = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        lst[idx] = element
        return lst
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
