import numpy as np

def smallest_k(arr, k):

    if len(arr) == k:
        return arr

    # Randomly select a pivot index
    idx = numpy.random.randint(0, len(arr))
    pivot = arr[idx]

    # Loop over the array checking each element against the pivot
    left_arr = []
    for element in arr:
        if element <= pivot:
            left_arr.append(element)

    if len(left_arr) < k:
        left_arr = arr
    
    return smallest_k(left_arr, k)


def test_case(arr, k, solution, test_func):

    output = test_func(arr, k)
    if sorted(output) == sorted(solution):
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case([1, 2, 3, 4, 5, 6, 7], 3, [1, 2, 3], smallest_k)
test_case([6, 9, 3, 0, 12, 456, 7, 3, 5, 4, 78, 8], 6, [0, 3, 3, 4, 5, 6], smallest_k)
test_case([0, 0, 0, 0, 0, 0, 1], 2, [0, 0], smallest_k)
