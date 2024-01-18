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

engineer = Engineer("John", 52, 20, 5000, "Senior developer")

engineer.show()

engineer.print_data()

