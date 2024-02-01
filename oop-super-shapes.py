class Shape:
    def __init__(self, colour):
        self.colour = colour

    def __str__(self):
        return f"colour: {self.colour}"

class NicerShape(Shape):
    def __init__(self, colour, pattern):
        super().__init__(colour)
        self.pattern = pattern

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}, pattern: {self.pattern}"

shape = Shape("red")

print(shape)

nicer_shape = NicerShape("green", "dotted")
nicer_chape2 = NicerShape("blue", "striped")

print(nicer_shape)
print(nicer_chape2)
