class LenghtError(Exception):
    pass

def enter_code():
    code = input("enter a two letter code:")

    if len(code) != 2:
        raise LenghtError("it's not two letters")
    else:
        return code


try:
    our_code = enter_code()
    print(our_code)
except ValueError:
    print("do something")
except LenghtError as exc:
    print(exc.args)


