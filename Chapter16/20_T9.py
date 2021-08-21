#import nltk
from nltk.corpus import words    

#nltk.download('words')
word_list = words.words()

def create_word_trie(word_list):
    trie = {}
    node = trie
    for word in word_list:
        for i, char in enumerate(word.lower()):
            if not node.get(char):
                node[char] = {"end": False, "successors": {}}
            if i == len(word) - 1:
                node[char]["end"] = True
            node = node[char]["successors"]
        node = trie
    return trie
                
Trie = create_word_trie(word_list)

t9_dict = {1: [],
           2: ["a", "b", "c"],
           3: ["d", "e", "f"],
           4: ["g", "h", "i"],
           5: ["j", "k", "l"],
           6: ["m", "n", "o"],
           7: ["p", "q", "r", "s"],
           8: ["t", "u", "v"],
           9: ["w", "x", "y", "z"],
           0: []}

def matching_words(seq, trie=Trie, t9_dict=t9_dict):
    
    poss_words = []
    current_stems = [["", trie]]
    for j, num in enumerate(seq):
        new_stems = []
        poss = t9_dict[num]
        if not len(poss):
            return None
        for char in poss:
            for i in range(len(current_stems)):
                if current_stems[i][1].get(char):
                    if current_stems[i][1][char]["end"] == True and j == len(seq) - 1:
                        poss_words.append(current_stems[i][0] + char)
                    new_stems.append([current_stems[i][0] + char, current_stems[i][1][char]["successors"]])
        current_stems = new_stems
    
    return poss_words

def test_case(arr, test_func):

    output = test_func(arr)
    if not output:
        if not arr or (max(arr) <=1 and min(arr) >= 0):
            print(f"Passed, output: {output}") 
        else:
            print(f"Unsure, got no output for {arr}")
        return 
            
    for word in output:
        if word not in word_list:
            print(f"Failed, got unexpected output {output}")
            return        
    print(f"Passed, output: {output}")

test_case([8, 7, 3, 3], matching_words)
test_case([2, 3, 4, 5], matching_words)
test_case([6, 7, 8, 2], matching_words)
test_case([6, 2, 4, 6, 3, 7, 4, 8, 6], matching_words)
test_case([6, 8], matching_words)
test_case([2, 3, 7, 7, 9, 2, 6], matching_words)
test_case([1, 0], matching_words)
test_case([], matching_words)
