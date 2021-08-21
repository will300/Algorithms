from math import ceil
from nltk.corpus import words
word_list = words.words()

def chunk_word_list(word_list):
    chunks = {}
    def total_words(chunk_items):
        chunk_dict = chunk_items[1]
        total = 0
        for letter in chunk_dict:
            total += len(chunk_dict[letter])
        return total

    for word in word_list:
        if not chunks.get(len(word)):
            chunks[len(word)] = {}
        if not chunks[len(word)].get(word[0]):
            chunks[len(word)][word[0]] = []
        chunks[len(word)][word[0]].append(word)
    return {k: v for k, v in sorted(chunks.items(), key=total_words)}

def try_word_chunk(chunk_length, chunk, rect_area):
    min_height = ceil(rect_area / chunk_length)
    for letter in chunk:
        for word in chunk[letter]:
            

print(list(chunk_word_list(word_list).keys()))


optimise

