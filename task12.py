# task №12
a = [5, 10, 15, 20, 25]


def get_list(array: list) -> list:
    new_list = []
    new_list.append(array[0])
    new_list.append(array[-1])
    return new_list


print(get_list(a))

# solution 2


def get_new_list(array: list) -> list:
    b, *_, c = array
    return [b, c]


print(get_new_list(a))
