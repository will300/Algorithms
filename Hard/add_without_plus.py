def add(val1, val2):
    mod = list(range(val1))
    mod.extend(list(range(val2)))
    return len(mod)

def test_case(val1, val2, solution, test_func):

    output = test_func(val1, val2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case(1, 2, 3, add)
