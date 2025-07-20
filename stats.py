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
def sort_on(sort_list):
    return sort_list["num"]
def sort_symbols(symbols_unsorted):
    sort_list = []
    for pair in symbols_unsorted:
        sort_list.append({"char" : pair, "num" : symbols_unsorted[pair]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
    


book_text = "Ladies and Gentlemen"
symbols_unsorted = symbol_count(book_text)
sort_symbols(symbols_unsorted)