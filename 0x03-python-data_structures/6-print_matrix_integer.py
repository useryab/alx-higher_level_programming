<<<<<<< HEAD
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and any(matrix) is False:
        print()
    for row in matrix:
        count = 0
        for n in row:
            if count == len(row) - 1:
                print("{:d}".format(n), end="")
                print()
            else:
                print("{}".format(n), end=" ")
            count += 1
=======
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and any(matrix) is False:
        print()
    for row in matrix:
        count = 0
        for n in row:
            if count == len(row) - 1:
                print("{:d}".format(n), end="")
                print()
            else:
                print("{}".format(n), end=" ")
            count += 1
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
