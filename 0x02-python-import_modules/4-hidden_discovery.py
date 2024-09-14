<<<<<<< HEAD
#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for name in dir(hidden_4):
        if name[0] != "_":
            print(f"{name}")
=======
#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != '_':
            print("{}".format(name))
>>>>>>> 18089313bf331b15816d82d256d82ac0c96c6a2a
