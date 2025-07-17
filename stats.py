def word_count(book_text):
    words = book_text.split()
    return len(words) 
def symbol_count(book_text):
    symbols = {}
    book_text = book_text.lower()
    for letter in book_text:
        if letter not in symbols:
            symbols[letter] = 0
        symbols[letter] += 1
    return symbols