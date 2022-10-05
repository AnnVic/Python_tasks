def is_inside(array: list, number: int) -> bool:
    return number in array


print(is_inside([1, 2, 7, 9, 4], 1))

# solution binary search


def is_inside_binary(array: list, number: int) -> bool:
    first = 0
    last = len(array) - 1
    mid = len(array) // 2
    while array[mid] != number and first <= last:
        if number > array[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (first + last) // 2
        if array[mid] == number:
            return True
        else:
            return False


print(is_inside_binary([1, 2, 7, 9, 4], 3))
