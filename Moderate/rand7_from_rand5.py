from random import randint
from collections import Counter

def rand5():
    return randint(0, 4)

def roll_dice(vals):
    return {x[0]: rand5() for x in vals}

def num_winners(arr):
    if len(arr) == 1:
        return 1
    val = arr[0][1]
    num = 1
    for elem in arr[1:]:
        if elem[1] == val:
            num += 1
    return num

def rand7():
    result = roll_dice([(x, 0) for x in list(range(7))])
    ordered = sorted(result.items(), key=lambda x:x[1], reverse=True)
    while num_winners(ordered) != 1:
        result = roll_dice(ordered[:num_winners(ordered)])
        ordered = sorted(result.items(), key=lambda x:x[1], reverse=True)
    return ordered[0][0]

def test():

    result_dict = Counter()
    for _ in range(10000):
        result_dict[rand7()] += 1
    print(result_dict)

test()
