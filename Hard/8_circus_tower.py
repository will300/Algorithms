def largest_tower(arr):

    height_order = sorted(arr, key=lambda x:x[0])
    weight_order = sorted(arr, key=lambda x:x[1])

    height_list = []
    prev_height, prev_weight = 0, 0
    for height, weight in height_order:
        if height > prev_height and weight > prev_weight:
            height_list.append((height, weight))
            prev_height, prev_weight = height, weight

    weight_list = []
    prev_height, prev_weight = 0, 0
    for height, weight in weight_order:
        if height > prev_height and weight > prev_weight:
            weight_list.append((height, weight))
            prev_height, prev_weight = height, weight

    return max(len(height_list), len(weight_list))



def test_case(arr, solution, test_func):

    output = test_func(arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case([(50, 50), (60, 60), (70, 70), (80, 60), (90, 90)], 4, largest_tower)
test_case([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)], 6, largest_tower)
test_case([(65, 100), (70, 150), (80, 90), (75, 190), (60, 95), (68, 110)], 5, largest_tower)
