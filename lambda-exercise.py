import datetime

date_time = datetime.datetime.now()

# print(date_time.strftime("%H:%M:%S"))

(lambda date_time: (print(date_time.strftime("%Y")),
print(date_time.strftime("%m")),
print(date_time.strftime("%d")),
print(date_time.strftime("%H:%M:%S"))))(date_time)


a_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(a_list, key=lambda x: x[1])

print(sorted_list)

print(list(map(lambda x: x * 3, [1, 2, 5, 6])))

print(list(map(lambda x: x ** 2, [1, 2, 5, 6])))

print(list(map(lambda a, b, c: a + b + c, [1, 2], [3, 4], [5, 6])))

print(list(map(lambda a, b: (a - b), [1, 2], [3, 4])))

