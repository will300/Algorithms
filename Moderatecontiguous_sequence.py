from math import inf

def cont_seq(arr):
    # find contiguous sequence with largest sum
    start_idx, end_idx = 0, 0
    largest_sum = -inf
    seq = []
    while not (start_idx == len(arr) - 1 and end_idx == len(arr)):

        if end_idx == 0:
            current_sum = arr[0]
            end_idx += 1
        elif end_idx == len(arr):
            current_sum -= arr[start_idx]
            start_idx += 1
        else:
            end_idx += 1
            if arr[end_idx - 1] > current_sum + arr[end_idx - 1]:
                start_idx = end_idx - 1
                current_sum = arr[start_idx]
            else:
                current_sum += arr[end_idx - 1]

        if current_sum > largest_sum:
            largest_sum = current_sum
            if end_idx != len(arr):
                seq = arr[start_idx:end_idx]
            else:
                seq = arr[start_idx:]

    return seq


def test_case(arr, solution, test_func):

    output = test_func(arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([-8, 3, -2, 4, -10], [3, -2, 4], cont_seq)
test_case([-18, 13, -12, 14, -10, 11, 6, -5, 8, -9, 15, -7], [13, -12, 14, -10, 11, 6, -5, 8, -9, 15], cont_seq)
test_case([-8, 3, -9, 4, -10, 2, -18], [4], cont_seq)
