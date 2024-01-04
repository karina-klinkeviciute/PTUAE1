i = 1

while i < 20:
    print(i)
    i *= 2

# while True:
#     print("hello")
#     print(i)
    # i += 1
    # if i > 10000:
    #     break

# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input) != 0:
#         break
#
# print(f"You entered {user_input}")

while True:
    secret = "secret"
    user_input = input("Enter the secret: ")
    if user_input == secret:
        print("You're in!")
        break
    else:
        print("Sorry, try again!")
