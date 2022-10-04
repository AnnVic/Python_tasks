# task №12
a = [5, 10, 15, 20, 25]


def get_list(lst: list) -> list:
    new_list = []
    new_list.append(lst[0])
    new_list.append(lst[-1])
    return new_list


print(get_list(a))

# solution 2


def get_new_list(lst: list) -> list:
    b, *_, c = lst
    return [b, c]


print(get_new_list(a))
