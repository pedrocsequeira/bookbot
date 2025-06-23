import os
import sys
from stats import get_num_words, get_count_char, sort_char

def get_book_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    
    num_words = get_num_words(book_text)
    char_count = get_count_char(book_text)
    sorted_char_count = sort_char(char_count)

    print(f'''============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count -----------\nFound {num_words} total words\n--------- Character Count --------''')
    for item in sorted_char_count:
        print(f'{item['char']}: {item['num']}')

    print('============= END ===============')


if __name__ == "__main__":
    main()