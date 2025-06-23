from stats import get_num_words, get_count_char, sort_char

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    
    num_words = get_num_words(book_text)
    char_count = get_count_char(book_text)
    sorted_char_count = sort_char(char_count)
    #print(f'{num_words} words found in the document')
    #print(sort_char(char_count))

    print(f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count -----------
Found {num_words} total words
--------- Character Count --------''')
    for item in sorted_char_count:
        print(item['char'],':', item['num'])

    print('============= END ===============')


if __name__ == "__main__":
    main()