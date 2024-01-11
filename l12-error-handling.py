
list1 = [12, 5, 3, 4, 56, 12]

list2 = [0, 2, 3, 0, 12, 78]

for index, item in enumerate(list1):
    try:
        result = item/list2[index]
    except ZeroDivisionError:
        result = "infinity"

    print(result)

