# Function to return contents of a txt file as string
def get_book_txt(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_word_count, get_char_count, sorted_dict_list
import sys

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_txt(sys.argv[1])
    book_words = get_word_count(book_content)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    book_dict = get_char_count(book_content)
    list_of_dicts = sorted_dict_list(book_dict)
    for dict in list_of_dicts:
        val_list = list(dict.values())
        print(f"{val_list[0]}: {val_list[1]}")

main()
