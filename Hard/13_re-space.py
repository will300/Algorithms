from math import inf
from nltk.corpus import words
word_list = words.words()
word_list = sorted(word_list, key=lambda word:len(word), reverse=True)
longest = len(word_list[0])
word_set = set(word_list)

def respace(doc_string, idx=0, num_invalid=0, best_invalid=inf):

    if idx >= len(doc_string):
        return num_invalid

    start = idx
    while idx < len(doc_string):
        idx += 1
        if doc_string[start:idx] in word_set:
            respace(doc_string, idx, num_invalid, best_invalid)
        
        

def respace(doc_string, corpus):

    # Brute force, loop through all words in corpus
    # Scan each word along the length of the document
    # If you find an unspaced substring where all characters match the word,
    # insert spaces around that substring
    # Time complexity: O(mn), m = num words, n = doc length
    
    doc_string_list = list(doc_string)

    i = 0
    while i < len(doc_string_list):
        for word in corpus:
            length = len(word)
            if "".join(doc_string_list[i:i + length]) == word:
                doc_string_list.insert(i, " ")
                doc_string_list.insert(i + length + 1, " ")
                i += length + 1
                break
        i += 1
        print(f"Processed {i} characters of {len(doc_string)} in document")

    return "".join(doc_string_list).split(" ")

def preprocess_document(filename):
    
    doc_string = open(filename, "r").read()
    doc_string = doc_string.lower()
    doc_string_list = list(doc_string)
    punc_list = [".", ",", "!", "?", ":", ";", "-", "+", "=", "\r", "\n", \
                 "/", "*", "£", "(", ")", "[", "]" "'", "\"", " "]

    doc_string_list = list(filter(lambda l: l not in punc_list, doc_string_list))

    return doc_string_list
                
def test_case(document):

    doc_string_list = preprocess_document(document)
    doc_words = respace(doc_string_list, word_list)

    print(doc_words)
    
    unknown_chars = 0
    for word in doc_words:
        if word not in word_list:
            unknown_chars += len(word)

    print(f"{unknown_chars} unknown characters in document of length {len(doc_string_list)}")
    
test_case("test_doc.txt")
