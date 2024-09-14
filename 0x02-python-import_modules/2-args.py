<<<<<<< HEAD
#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if argc < 2:
        print("{} arguments.".format(argc - 1))
    else:
        if argc == 2:
            print("{} argument:".format(argc - 1))
        else:
            print("{} arguments:".format(argc - 1))
    for n in range(1, argc):
        print("{}: {}".format(n, argv[n]))
=======
#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print("{} arguments.".format(argc - 1))
    else:
        if argc == 2:
            print("{} argument:".format(argc - 1))
        else:
            print("{} arguments:".format(argc - 1))
    for n in range(1, argc):
        print("{}: {}".format(n, argv[n]))
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
