def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    get_char(text)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char(text):
    char_dict = {}
    lower_text = text.lower()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        char_dict.update({letter: lower_text.count(letter)})
    print(char_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()