def number_max(num1, num2):
    # No comparators allowed
    idx = int((num1 - num2) / abs(num1 - num2))
    return ["same", num1, num2][idx]


def test_case(num1, num2, solution, test_func):

    output = test_func(num1, num2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case(1, 3, 3, number_max)
test_case(4, 5, 5, number_max)
test_case(0, -1, 0, number_max)
test_case(1, 1, "same", number_max)

