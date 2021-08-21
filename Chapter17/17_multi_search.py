def multisearch(string, arr):

    mapping = {}    

    for substring in arr:
        i = 0
        while i <= len(string) - len(substring):
            
            if i == len(string) - len(substring):

                if string[i:] == substring:
                    if mapping.get(substring):
                        mapping[substring].append(i)
                    else:
                        mapping[substring] = [i]    
            else:

                if string[i:i + len(substring)] == substring:
                    if mapping.get(substring):
                        mapping[substring].append(i)
                    else:
                        mapping[substring] = [i]  
            i += 1

    return mapping  
                    

def test_case(string, arr, solution, test_func):

    output = test_func(string, arr)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case("mississippi", ["is", "ppi", "hi", "sis", "i", "ssippi"], {"is": [1, 4], "ppi": [8], "sis": [3], "i": [1, 4, 7, 10], "ssippi": [5]}, multisearch)
