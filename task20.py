def is_inside(lst: list, number: int) -> bool:
    return number in lst


print(is_inside([1, 2, 7, 9, 4], 1))

# solution binary search


def is_inside_binary(lst: list, number: int) -> bool:
    first = 0
    last = len(lst) - 1
    mid = len(lst) // 2
    while lst[mid] != number and first <= last:
        if number > lst[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
        if lst[mid] == number:
            return True
        else:
            return False


print(is_inside_binary([1, 2, 7, 9, 4], 1))
