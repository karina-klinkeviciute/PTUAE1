def check_integers(name, *args):

    print(name)
    for item in args:
        if type(item) != type(1):
            return False

    return True

print(check_integers("Petras", 1, 2, 3))

print(check_integers("p", "o", "i", 1, 5, 9))

print(check_integers("Jonas", "1", "2"))

print((check_integers(5)))

