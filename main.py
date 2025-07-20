import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(file_path):

    with open(file_path) as book:
        book_text = book.read()
        return book_text
from stats import word_count
from stats import symbol_count
from stats import sort_symbols
def alphafinder(symbols):
    for symbol in symbols:
        char = symbol["char"]
        if char.isalpha() == True:
            print(f"{symbol["char"]}: {symbol["num"]}")
def main(file_path):
    book_text = get_book_text(file_path)
    word_number = word_count(book_text)
    symbols_unsorted = symbol_count(book_text)
    symbols = sort_symbols(symbols_unsorted)
    print("============ BOOKBOT ============ \n"
          f"Analyzing book found at {file_path}... \n "
          "----------- Word Count ---------- \n "
          f"Found {word_number} total words \n "
          "--------- Character Count ------- \n ")
    alphafinder(symbols)
    print("============= END ===============")
file_path = sys.argv[1]
main(file_path)
