def calc_poss_factors(value, numa, numb):
    
    poss_pairs = []
    for blength in range(1, value//numb - numa):
        if (value - numb*blength) % numa == 0:
            alength = int((value - numb*blength)/numa)
            poss_pairs.append((alength, blength))

    return poss_pairs


def pattern_match(pattern, value):
    ## arg: pattern (type: string) e.g. aabab
    ## arg: value (type: string) e.g. catcatgocatgo

    if len(pattern) == 1:
        if len(value) > 0:
            return True

    numa = pattern.count("a")
    numb = pattern.count("b")
    poss_pairs = calc_poss_factors(len(value), numa, numb)
    if len(poss_pairs) == 0:
        return False

    for pair in poss_pairs:
        idx = 0
        prev_a, prev_b = None, None
        for char in pattern:
            if char == "a":
                if idx + pair[0] < len(value) - 1:
                    section = value[idx: idx + pair[0]]
                else:
                    section = value[idx:]

                idx += pair[0]
                if prev_a and not prev_a == section:
                    idx = 0
                    break
                prev_a = section
            else:
                if idx + pair[1] < len(value) - 1:
                    section = value[idx: idx + pair[1]]
                else:
                    section = value[idx:]

                idx += pair[1]
                if prev_b and not prev_b == section:
                    idx = 0
                    break
                prev_b = section
        if idx == len(value):
            return True
    return False
    


def test_case(pattern, value, solution, test_func):

    output = test_func(pattern, value)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


test_case("aabab", "catcatgocatgo", True, pattern_match)
