def my_func(*args):
    args_list = list(args)
    args_list.remove(min(args))
    return sum(args_list)


print(my_func(12.7, 324, 2343.48))
print(my_func(-100, -10000, -1000))
print(my_func(1, 2, 3, 4, 5))
