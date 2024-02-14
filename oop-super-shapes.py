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


class BorderedShape(NicerShape):
    def __init__(self, colour, pattern, border):
        super().__init__(colour, pattern)
        self.border = border

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}, border: {self.border}"


shape = Shape("red")

print(shape)

nicer_shape = NicerShape("green", "dotted")
nicer_chape2 = NicerShape("blue", "striped")

print(nicer_shape)
print(nicer_chape2)

bordered_shape = BorderedShape("yellow", "flowers", "dashes")

print(bordered_shape)
