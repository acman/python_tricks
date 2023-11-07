def binary_search(elements, target):
    left = 0
    right = len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        if elements[middle] == target:
            return middle
        elif elements[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1


if __name__ == '__main__':
    assert binary_search(list(range(10)), 5) == 5
