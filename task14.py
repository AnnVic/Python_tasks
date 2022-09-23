# task №14
def get_unique_elem(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list


def get_unique_elem2(lst):
    return list(set(lst))

print(get_unique_elem([1, 2, 5, 2, 8, 9, 5, 9]))
print(get_unique_elem2([1, 2, 5, 2, 8, 9, 5, 9]))
