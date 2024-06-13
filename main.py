from operator import itemgetter
from collections import OrderedDict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_char_dict = get_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    get_char(text)
    report(sorted_char_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char(text):
    char_dict = {}
    lower_text = text.lower()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        char_dict.update({letter: lower_text.count(letter)})
    sorted_char_dict = sorted(char_dict.items(), key=itemgetter(1), reverse=True)
    sorted_char_dict = dict(sorted_char_dict)
    return sorted_char_dict

def report(sorted_char_dict):
    for key, value in sorted_char_dict.items():
        print("The ", key, "character was found ", value, " times")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()