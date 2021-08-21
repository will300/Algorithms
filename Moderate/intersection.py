def intersection(start1, end1, start2, end2):

    x11, y11 = start1
    x12, y12 = end1
    m1 = (y12 - y11) / (x12 - x11)
    c1 = y11 - m1*x11

    x21, y21 = start2
    x22, y22 = end2
    m2 = (y22 - y21) / (x22 - x21)
    c2 = y21 - m2*x21

    # m2*x + c2 = m1*x + c1
    x = (c1 - c2) / (m2 - m1)
    y = m1*x + c1

    if min(start1[1], end1[1]) <= y <= max(start1[1], end1[1]):
        return x, y
    else: 
        return "intersection not found"
    
    

def test_case(start1, end1, start2, end2, solution, test_func):

    tol = 0.1
    output = test_func(start1, end1, start2, end2)
    if type(solution) == str:
        if type(output) == str:
            print("Passed")
        else:
            print(f"Failed, expected {solution}, got {output}")
    elif solution[0] - tol <= output[0] <= solution[0] + tol and \
       solution[1] - tol <= output[1] <= solution[1] + tol:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case((-14, 0), (0, -7), (-4, -10), (0, 2), (-2.58, -5.71), intersection)

