def get_num_words(book_text):
    return len(book_text.split())

def get_count_char(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1 
    return char_count