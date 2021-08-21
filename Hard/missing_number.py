def dec_2_bin(decimal):
    
    power = 0
    while 2**(power+1) <= decimal:
        power += 1
    
    binary = ""
    while power >= 0:
        if 2**power <= decimal:
            binary += "1"
            decimal -= 2**power
        else:
            binary += "0"
        power -= 1
    return binary
      
def get_next_bin(binary):
    idx = len(binary) - 1
    while idx >= 0:
        if binary[idx] == "0":
            return binary[:idx] + "1" + "0"*(len(binary) - 1 - idx)
        idx -= 1
    return "1" + "0"*len(binary)

def missing_number(n, missing_idx):

    A = []
    for i in range(missing_idx):
        A.append(dec_2_bin(i)) 
    for i in range(missing_idx + 1, n + 1):
        A.append(dec_2_bin(i)) 

    next_bin = "0"
    for i, binary in enumerate(A):
        if not next_bin == binary:
            return i
        next_bin = get_next_bin(binary)
    return "No missing number"
    

def test_case(arr, m, test_func):

    output = test_func(arr, m)
    if output == m:
        print("Passed")
    else:
        print(f"Failed, expected {m}, got {output}")

test_case(7, 4, missing_number)
test_case(19, 8, missing_number)
test_case(110, 44, missing_number)



