number1 = int(input("enter number1 "))
number2 = int(input("enter number2 "))

#  comparison of numbers
# if number1 > number2:
#     print("more")
# elif number1 < number2:
#     print("less")
# else:
#     print("equal")

year = int(input("enter year of birth: "))


# lots of elif
if year >= 2010:
    print("generation Alpha")
elif year >= 1997:
    print("generation Z")
elif year >= 1981:
    print("Millenial")
elif year >= 1965:
    print("Generation X")
elif year >= 1946:
    print("Baby Boomer")
elif year >= 1928:
    print("Silent generation")
else:
    print("some earlier generation")

# shorter if (though less readable
print("number1 is bigger") if number1 > number2 else print("number2 is bigger") if number2 > number1 else print("they are equal")

a = 200
b = 300
c = 100

# checking two conditions
if c > b and c > a:
    print("number c is larger than the other ones")

if c > b or c > a:
    print("number c is larger then at least on of other numbers")
else:
    print("number c is not larger then at least on of other numbers")

