# print(1/0)
import sys
import warnings


class AgeTooLow(Exception):
    def __init__(self):
        self.message = "User should be at least 21 years old"




x = 1
if x > 5:
    raise Exception("x is greater than 5. It should not exceed 5")

assert ('linux' in sys.platform)

def linux_interaction():
    assert('linux' in sys.platform)
    print("something")
    print(1/0)

try:
    linux_interaction()

except AssertionError:
    print("not linux")

except ZeroDivisionError:
    print("can't divide by 0")


numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])
except IndexError:
    print("the requested index is out of range")
except KeyError:
    print("could not retrieve that value")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except:
        print("You should have entered a number")

# warnings.warn("deprecated", DeprecationWarning)

print("hi")


users_age = int(input("enter your age: "))


def eligible_for_casino():
    if users_age < 21:
        raise AgeTooLow
    else:
        print("welcome to casino")


try:
    eligible_for_casino()

except AgeTooLow:
    print("you're too young to enter casino")



