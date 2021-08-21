def swap_in_place(arr, idx1, idx2):
    new_arr = arr[:]
    if idx1 > len(arr) - 1 or idx2 > len(arr) - 1:
        return arr
    new_arr.insert(idx1, new_arr.pop(idx2))
    #print(new_arr)
    new_arr.insert(idx2, new_arr.pop(idx1 + 1))
    return new_arr

def test_case(arr, idx1, idx2, solution, test_func):

    output = test_func(arr, idx1, idx2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([1, 2, 3, 4, 5], 1, 3, [1, 4, 3, 2, 5], swap_in_place)
test_case([1, 2, 3, 4, 5], 0, 4, [5, 2, 3, 4, 1], swap_in_place)
test_case([1, 2], 0, 1, [2, 1], swap_in_place)
test_case([], 0, 0, [], swap_in_place)
