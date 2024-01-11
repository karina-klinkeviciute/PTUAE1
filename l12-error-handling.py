
list1 = [12, 5, 3, 4, 56, 12, 58, 45]

list2 = ["12", 2, 3, 0, "12", 78]

for index, item in enumerate(list1):
    try:
        result = item/list2[index]

    except ZeroDivisionError:
        result = "infinity"
    except TypeError:
        result = "cant divide int by string"
    except IndexError:
        result = "too many items"
    print(result)

