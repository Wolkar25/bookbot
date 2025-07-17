path_of_file = "/home/wolkar/bootdev/bookbot/books/frankenstein.txt"

def get_book_text(path_of_file):
    
    with open(path_of_file) as book_text:
        print(book_text)