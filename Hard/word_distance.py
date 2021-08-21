def find_distance(doc_string, word1, word2):
    doc = open(doc_string, "r").read()
    shortest = len(doc) + 1
    prev_word1_idx = None
    prev_word2_idx = None
    for idx, word in enumerate(doc):
        if word == word1:
            prev_word1_idx = idx
            if prev_word2_idx:
                if (prev_word1_idx - prev_word2_idx) < shortest:
                    shortest = prev_word1_idx - prev_word2_idx
        elif word == word2:
            prev_word2_idx = idx
            if prev_word1_idx:
                if (prev_word2_idx - prev_word1_idx) < shortest:
                    shortest = prev_word2_idx - prev_word1_idx
    if shortest < len(doc):
        return shortest
    return None

def test_case(k, solution, test_func):

    output = test_func(k)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")

test_case([1, 2, 5, 9, 5, 9, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], 7, find_majority_element)
