def similarity(x, y):
    return len(x.intersection(y)) / len(x.union(y))

def print_positive_similarities(docdict):
    doclist = list(docdict.items())

    for i, val_x in enumerate(doclist):
        key_x, x = val_x
        for j, val_y in enumerate(doclist[i:]):
            key_y, y = val_y
            if key_x != key_y and len(x.intersection(y)):
                print(key_x, key_y, similarity(x, y))

def test_case(docdict):

    print_positive_similarities(docdict)

test_case({13: {14, 15, 100, 9, 3},
           16: {32, 1, 9, 3, 5},
           19: {15, 29, 2, 6, 8, 7},
           24: {7, 10}})
