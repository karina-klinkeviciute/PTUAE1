
list1 = [12, 5, 3, 4, 56, 12, 58, 45]

list2 = [0, 2, 3, 0, "12", 78]

for index, item in enumerate(list1):
    try:
        result = item/list2[index]
        print(result)
    except ZeroDivisionError:
        print("infinitty")
    except TypeError:
        print("cant divide int by string")
    except IndexError:
        print("too many items")


