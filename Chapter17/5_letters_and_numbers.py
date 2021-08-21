def get_reference_dict(arr):

    ctr = 0
    reference = {0: [0, 0]}
    for i, elem in enumerate(arr):
        if type(elem) == int or type(elem) == float:
            ctr += 1
        elif type(elem) == str:
            ctr -= 1

        if not reference.get(ctr):
            reference[ctr ] = [i + 1, i + 1]
        else:
            reference[ctr][1] = i + 1

    return reference

def longest_balanced_subarray(arr):

    reference = get_reference_dict(arr)
    biggest_range = 0
    slice_indices = [0, 0]
    for ref in reference.keys():
        if reference[ref][1] - reference[ref][0] > biggest_range:
            slice_indices = reference[ref]
            biggest_range = reference[ref][1] - reference[ref][0]
    
    if slice_indices[1] == len(arr):
        return arr[slice_indices[0]:]
    return arr[slice_indices[0]:slice_indices[1]]

def test_case(arr, solution, test_func):

    output = test_func(arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([1, "a", "b", 4, 5, 6, "c", "d", "e", "f", "g", "h", "i", 7, 8], [1, "a", "b", 4, 5, 6, "c", "d"], longest_balanced_subarray)
