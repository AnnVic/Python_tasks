# task №5
import random


def get_list(a: list, b: list) -> list:
    result_list = []
    for i in a:
        for j in b:
            if i == j:
                result_list.append(i)
                break
    return result_list


def get_common_number(a: list, b: list) -> list:

    if len(a) > len(b):
        return get_list(a, b)
    else:
        return get_list(a, b)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(get_common_number(a, b))

# randomly generate two lists
list1 = random.sample(range(1, 50), 10)
list2 = random.sample(range(1, 50), 14)

get_common_number(list1, list2)

# solution in one line
print(list(set(a) & set(b)))
print(list(set(list1) & set(list2)))
