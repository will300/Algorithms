def find_majority_element(arr):
    poss_maj = arr[0]
    poss_ctr = 0
    not_poss_ctr = 0
    idx = 1
    while idx < len(arr):
        num = arr[idx]
        if num == poss_maj:
            poss_ctr += 1
        else:
            not_poss_ctr += 1
        if not_poss_ctr >= poss_ctr:
            poss_maj = num
        idx += 1

    # Check if majority
    total = 0
    for num in arr:
        if num == poss_maj:
            total += 1

    return poss_maj if total > len(arr) / 2 else -1

def test_case(k, solution, test_func):

    output = test_func(k)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case([1, 2, 5, 9, 5, 9, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 7, find_majority_element)
