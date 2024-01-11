
list1 = [12, 5, 3, 4, 56, 12, 58, 45]

list2 = ["12", 2, 3, 0, "12", 78]

for index, item in enumerate(list1):
    try:
        result = item/list2[index]

    except ZeroDivisionError as exc:
        print(exc.args[0])
    except TypeError:
        print("cant divide int by string")
    except IndexError:
        print("too many items")
    else:
        print(result)


# for index, item in enumerate(list1):
#     try:
#         result = item/list2[index]
#
#     except (ZeroDivisionError, TypeError, IndexError) as exc:
#         result = exc.args
#
#     print(result)

