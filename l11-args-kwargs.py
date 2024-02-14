def my_function(a, b, *args, c=10, d=20, **kwargs):

    print(a, b)
    print(args)
    print(c, d)
    print(kwargs)


my_function(1, 2, 3, 4, 5, d=15, e=20, f=30, g=40)
