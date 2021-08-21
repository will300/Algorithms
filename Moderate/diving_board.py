def diving_board_lengths(k, short_length, long_length):

    if k == 0:
        return []

    shortest_board = k*short_length
    longest_board = k*long_length
    
    if short_length == long_length:
        return [longest_board]
    return list(range(shortest_board, longest_board + (long_length - 
                               short_length), long_length - short_length))


def test_case(k, num1, num2, solution, test_func):

    output = test_func(k, num1, num2)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case(0, 1, 2, [], diving_board_lengths)
test_case(4, 5, 5, [20], diving_board_lengths)
test_case(3, 1, 2, [3, 4, 5, 6], diving_board_lengths)
test_case(4, 1, 3, [4, 6, 8, 10, 12], diving_board_lengths)

