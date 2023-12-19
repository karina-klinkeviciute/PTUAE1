text = "25"

# converting text to integer
number = int(text)

print(text)

#  hexadecimal
text = "0x51"

number = int(text, 16)

#  octal
text = "0x51"

number = int(text, 16)

print(text)

print(number * 3)

number = 45

# number to string
text = str(number)

print(text * 3)

# int to float
number_float = float(number)

print(f"floating point number: {number_float}")

text = "Hello"

# if we try to convert string that is not a number into number, it shows errors
# print(int(text))

# print(float(text))
