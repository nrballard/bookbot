import sys
from stats import count_words, count_chars, sort_ccount

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    book = get_book_text(path)
    wc = count_words(book)
    cc = count_chars(book)
    cc_list = sort_ccount(cc)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for i in cc_list:
        print(f"{i["char"]}: {i["num"]}")
main()
