import os

from datetime import datetime

# print(dir(os))

# current working directory
print(os.getcwd())

# changing the current working directory:
os.chdir("/home/karina/work/codeacademy/")

# get directory again
print(os.getcwd())

# list files and folders form the working directory
# print(os.listdir())

# create a new directory
# os.mkdir("my_directory")
# print(os.listdir())

os.chdir("/home/karina/work/codeacademy/my_directory")

# another way to create directories - one inside another
# os.makedirs("new_directory/another_directory")

# statistics about directory.file
print(os.stat("new_directory"))

# concrete information (size) anout directory/file
print(os.stat("new_directory").st_size)

# last modified:
modified_time = os.stat("new_directory").st_mtime

modified_time = datetime.fromtimestamp(modified_time)

print(modified_time)


# opening file (not the recommended way)
file = open("my_file.txt", "w")

# writing to the file
file.write("hello world")

file.close()

# closing file
# file.close()

# working with files the recommended way

# opening file for writing
with open("my_file.txt", "w") as file:
    file.write("hi there \nanother line \nthird line")

# opening file for reading
with open("my_file.txt", "r") as file:
    file_contents = file.read()

# print(file_contents)

# opening file for reading and writing
with open("my_file.txt", "r+") as file:
    file.write("Hello again")
    text = file.read()
    print(text)

with open("my_file.txt", "w") as file:
    file.write("čia naujas tekstas")

with open("my_file.txt", "r") as file:
    text = file.read()
    print(text)

# appending to the end of file
with open("my_file.txt", "a") as file:
    file.write("\nsome text again")

# # writing in desired place
# with open("my_file.txt", "w") as file:
#     file.write("hello world")
#     file.seek(5)
#     file.write("test")

# reading all the lines in the file
with open("my_file.txt", "r") as file:
    lines = file.readlines()

# printing each line
for line in lines:
    print(line)

for line in lines:
    print(line, end="")

# reading line by line (one line at a time)
with open("my_file.txt", "r") as file:
    print(file.readline())

    print(file.readline())

# another way of reading line by line
with open("my_file.txt", "r") as file:
    for line in file:
        print(line)


with open("my_file.txt", "r") as r_file:
    with open("new_file.txt", "w") as w_file:
        for line in r_file:
            w_file.write(line)

os.chdir("/home/karina/work/codeacademy")

with open("bird-7866804_640.jpg", "rb") as r_file:
    with open("new_bird-7866804_640.jpg", "wb") as w_file:
        for line in r_file:
            w_file.write(line)
