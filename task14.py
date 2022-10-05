# task №14
def get_unique_elem(array: list) -> list:
    new_list = []
    for element in array:
        if element not in new_list:
            new_list.append(element)
    return new_list


def get_unique_elem2(array: list) -> list:
    return list(set(array))


print(get_unique_elem([1, 2, 5, 2, 8, 9, 5, 9]))
print(get_unique_elem2([1, 2, 5, 2, 8, 9, 5, 9]))
