def number_of_2s(n):

    arr = list(range(n + 1))
    num_str = ""
    for num in arr:
        num_str += str(num)

    count = 0
    for char in num_str:
        if char == "2":
            count += 1

    return count

def test_case(n, solution, test_func):

    output = test_func(n)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case(25, 9, number_of_2s)



