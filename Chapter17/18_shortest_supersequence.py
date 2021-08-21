def shortest_supersequence(long_arr, short_arr):

    # Move through the array testing elements for short array appearance
    # Add these elements as you go to a reference array dict with indexes
    
    # Subtract these elements as you go from a copy of short array
    # Once the copy is empty, you have found a subarray
    # Now test the next elements of the long array one by one
    # add to an array of residual elements

    short_dict:
    for i, el in enumerate(long_arr):
        if el in short_arr:
            short_dict[i] = el


    
                    

def test_case(arr1, arr2, solution, test_func):

    output = test_func(string, arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case(shortest_supersequence)
