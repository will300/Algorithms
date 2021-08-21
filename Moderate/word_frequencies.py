from tika import parser
from collections import Counter
import csv
import os

def word_counts(book_pdf):

    raw = parser.from_file(book_pdf)
    text = raw["content"]
    for char in "!\"*&(){}[],-'#~;:./?\n":
        text = text.replace(char, "")
    text = text.split(" ")
    word_count = Counter()
    for word in text:
        word_count[word.lower()] += 1

    word_list = sorted(list(word_count.items()), key=lambda x:x[1], reverse=True)
    
    with open(book_pdf[:-4] + "wordcount.csv", mode="w") as csv_file:
        fieldnames = ["word", "count"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word_count in word_list:
            writer.writerow({"word": word_count[0], "count": word_count[1]})

def word_freq(book_pdf, word):
    if book_pdf[:-4] + "wordcount.csv" not in os.listdir():
        word_counts(book_pdf)
    with open(book_pdf[:-4] + "wordcount.csv", mode="r") as csv_file:
        reader = csv.reader(csv_file)
        word_dict = {rows[0]: rows[1] for rows in reader}
    #print(list(word_dict.items())[0])
    return word_dict[word]


book = 'Sigmund Freud - The Interpretation of Dreams.pdf'
word = "a" 
#word_counts(book)
print(f"Frequency of \"{word}\" in {book} is {word_freq(book, word)}")
