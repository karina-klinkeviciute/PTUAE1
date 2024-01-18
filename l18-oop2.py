class Employee:
    def __init__(self, name, age, experience, salary):
        self.name = name
        self.age = age
        self.experience = experience
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.experience, self.salary)


class Engineer(Employee):
    def __init__(self, name, age, experience, salary, level):
        super().__init__(name, age, experience, salary)
        self.level = level

    def print_data(self):
        print(self.level)

class Person:
    def __init__(self, hobbies):
        self.hobbies = hobbies

    def show_hobbies(self):
        print(self.hobbies)

class Designer(Employee, Person):
    def __init__(self, name, age, experience, salary, position, hobbies):
        Employee.__init__(self, name, age, experience, salary)
        Person.__init__(self, hobbies)
        self.position = position

    def show(self):
        super().show()
        print(self.position)


engineer = Engineer("John", 52, 20, 5000, "Senior developer")

engineer.show()

engineer.print_data()

designer = Designer("Tom", 54, 10, 4000, "UI designer", "skiing")

designer.show()

designer.show_hobbies()
