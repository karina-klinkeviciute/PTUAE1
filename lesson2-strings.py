# String type operations

letter = "a"

letter2 = "b"

name = "Karina"

company = "Code Academy is great"

sentence = "I really enjoy learning python !"

age = "55 years"

age2 = "9 months"

# print(company)

name_company = name + " works at " + company

# print(name_company)

# f stands for "formated"
#  we add variables inside curly braces: {}
# f-string is the most common method of string formatting
name_company2 = f"{name} works at {company}"

name_company3 = "{0} works at {1}".format(name, company)

# print(name_company3)

# print(name_company2)

# 5th to 12th characters (Academy)
# print(company[5:12])

# Up to 4th character (Code)
# print(company[:4])

# up to 4th character from the end
# print(company[:-4])

# reversing the string. -1 means that we are going backwards by 1 step
# print(company[::-1])

# two slices with one print
# print(f"{company[2:5]} {company[12:20]}")

