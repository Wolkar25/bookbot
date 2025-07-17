def get_book_text(file_path):

    with open(file_path) as book:
        book_text = book.read()
        return book_text
from stats import word_count
def main(file_path):
    book_text = get_book_text(file_path)
    word_number = word_count(book_text)
    print(f"{word_number} words found in the document")

file_path = "books/frankenstein.txt"
main(file_path)
