# task №5
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def get_common_number(a: list, b: list) -> list:
    result_list = []

    if len(a) > len(b):
        for i in a:
            for j in b:
                if i == j:
                    result_list.append(i)
                    break
    else:
        for i in b:
            for j in a:
                if i == j:
                    result_list.append(i)
                    break
    return result_list


print(get_common_number(a, b))

# randomly generate two lists
lst = random.sample(range(1, 50), 10)
lst1 = random.sample(range(1, 50), 14)

get_common_number(lst, lst1)

# solution in one line
print(list(set(a) & set(b)))
print(list(set(lst) & set(lst1)))
