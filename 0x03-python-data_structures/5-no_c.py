<<<<<<< HEAD
#!/usr/bin/python3
def no_c(my_string):
    res = []
    for x in my_string:
        if x != "c" and x != "C":
            res.append(x)
    return "".join(res)
=======
#!/usr/bin/python3
def no_c(my_string):
    res = []
    for x in my_string:
        if x != 'c' and x != 'C':
            res.append(x)
    return "".join(res)
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
