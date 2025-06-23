def get_num_words(book_text):
    return len(book_text.split())

def sort_on(items):
    return items["num"]

def get_count_char(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1 
    return char_count

def sort_char(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list 