# task №12
a = [5, 10, 15, 20, 25]

def get_list(lst):
    new_list = []
    new_list.append(lst[0])
    new_list.append(lst[-1])
    return new_list

print(get_list(a))