def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid_idx = len(arr)//2
    arr1 = arr[:mid_idx]
    arr2 = arr[mid_idx:]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    idx1 = 0
    idx2 = 0

    sorted_arr = []
 
    while idx1 < len(arr1) or idx2 < len(arr2):
        if idx2 == len(arr2):
            sorted_arr.append(arr1[idx1])
            idx1 += 1
        elif idx1 == len(arr1):
            sorted_arr.append(arr2[idx2])
            idx2 += 1
        elif arr1[idx1] <= arr2[idx2]:
            sorted_arr.append(arr1[idx1])
            idx1 += 1
        else:
            sorted_arr.append(arr2[idx2])
            idx2 += 1

    return sorted_arr
    

def subsort(arr):

    sorted_arr = merge_sort(arr)
    idx1, idx2 = 0, len(arr) - 1
    for x, y in zip(arr, sorted_arr):
        if not x == y:
            break
        idx1 += 1

    for x, y in zip(arr[::-1], sorted_arr[::-1]):
        if not x == y:
            break
        idx2 -= 1

    return idx1, idx2
    

def test_case(arr, solution, test_func):

    output = test_func(arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], (3, 9), subsort)
#test_case([20], subsort)
#test_case([3, 4, 5, 6], subsort)
#test_case([4, 6, 8, 10, 12], subsort)
