def get_pairs(arr1, arr2, val):
    set1 = set(arr1)
    set2 = set(arr2)
    pairs = []
    for elem in set1:
        target = val - elem
        if target in set2:
            pairs.append((elem, target))
    return pairs

def test_case(arr1, arr2, val, solution, test_func):

    output = test_func(arr1, arr2, val)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([4, 1, 2, 1, 1, 2], [3, 6, 3, 3], 8, [(2, 6)], get_pairs)
