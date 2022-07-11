def binary_search(array, x) -> bool:
    lower_index = 0
    upper_index = len(array) - 1
    middle_index = 0

    while lower_index <= upper_index:
        middle_index = (upper_index + lower_index) // 2
        if array[middle_index] < x:
            lower_index = middle_index + 1
        elif array[middle_index] > x:
            upper_index = middle_index - 1
        else:
            return True
    return False


def re_binary_search(array, lower, upper, x) -> bool:
    if upper >= lower:
        middle = (upper + lower) // 2
        if array[middle] == x:
            return True
        elif array[middle] > x:
            return re_binary_search(array, lower, middle - 1, x)
        else:
            return re_binary_search(array, middle + 1, upper, x)
    else:
        return False


def iterative_search(array, x) -> bool:
    for i in array:
        if x == i:
            return True
    return False


def this_is_stupid():
    this_is_stupid()

array = [2, 3, 5, 11, 40, 41, 43, 52, 78, 79, 100, 120, 121]
x = 2

result = binary_search(array, x)
print(result)
result = re_binary_search(array, 0, len(array) - 1, x)
print(result)
result = iterative_search(array, x)
print(result)
