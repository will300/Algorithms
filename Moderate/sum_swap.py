def sum_swap(arr1, arr2):
    if not arr1 or not arr2:
        return None
    diff = 0
    for elem in arr1:
        diff += elem
    for elem in arr2:
        diff -= elem
    if diff % 2 != 0:
        return None

    set1 = set(arr1)
    res = int(diff/2)
    for elem in arr2:
        elem + res
        if elem + res in set1:
            return elem + res, elem
    return None

def test_case(arr1, arr2, solution, test_func):

    output = test_func(arr1, arr2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([4, 1, 2, 1, 1, 2], [3, 6, 3, 3], (1, 3), sum_swap)
test_case([4, 1, 2, 1, 2, 2], [3, 6, 3, 3], None, sum_swap)
test_case([9, 7, 8], [1, 2], None, sum_swap)
test_case([], [], None, sum_swap)

