def get_max(*args) -> int:
    max_num = args[0]
    for i in args:
        max_num = i if i > max_num else max_num

    return max_num


print(get_max(20, 7, 1, 0, 3, 6))
