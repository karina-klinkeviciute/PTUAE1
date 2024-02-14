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

# print(company[5])
#
# print(company[-5])

# up to 4th character from the end
# print(company[:-4])

# reversing the string. -1 means that we are going backwards by 1 step
# print(company[::-1])

# two slices with one print
# print(f"{company[2:5]} {company[12:20]}")

words = company.split()
#
# print(words)
#
# print(company.upper())
#
# print(company.casefold())
#
# print("Šalta".lower())
#
print(company.replace("e", "E", 2).replace("d", "D"))

company = company.replace("a", "4")
company = company.replace("b", "8")
company = company.replace("c", "<")
company = company.replace("d", "|)")

print(company)

# if we need to have quotes inside
sentence = 'he said "your dog is nice"'

# if we need an apostrophe inside single quotes, we can escape it with \
sentence2 = "let's eat"
sentence4 = "let's eat"
print(sentence2)
print(sentence4)

sentence3 = 'he said "let\'s eat"'
print(sentence3)

print(len(sentence3))

a = 15

print(a)

a = 19

print(a)
