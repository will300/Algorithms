from math import inf

def smallest_diff(arr1, arr2):
    diff = inf
    for i in arr1:
        for j in arr2:
            diff = min(diff, abs(i - j))
    return diff


def test_case(arr1, arr2, solution, test_func):

    output = test_func(arr1, arr2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([1, 3, 15, 11, 2], [23, 127, 235, 19, 8], 3, smallest_diff)
test_case([1, 13, 150, 112, 28], [23, 127, 235, 19, 8], 5, smallest_diff)
