def check_integers(name, *args):
    """check if all names are integers. If so, return True. Otherwise return False"""
    print(name)
    for item in args:
        # check the type if an item, and comper to an item we know is an integer
        if type(item) != type(1):
            return False

    return True

print(check_integers("Petras", 1, 2, 3))

print(check_integers("p", "o", "i", 1, 5, 9))

print(check_integers("Jonas", "1", "2"))

print((check_integers(5)))

