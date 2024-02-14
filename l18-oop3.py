class Parent:
    def __init__(self):
        self._mobile_number = "555456456"

    @property  # (getter)
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        if mobile_number.startswith("+"):
            self._mobile_number = mobile_number
        else:
            self._mobile_number = f"+{mobile_number}"


class Child(Parent):
    def show_mobile_number(self):
        print(self._mobile_number)


child = Child()
child.show_mobile_number()

obj = Parent()

print(obj._mobile_number)

print(obj.mobile_number)

obj.mobile_number = "77788999"

print(obj.mobile_number)
