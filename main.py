from stats import get_num_words, get_count_char 

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    
    num_words = get_num_words(book_text)
    char_count = get_count_char(book_text)
    
    print(f'{num_words} words found in the document')
    print(char_count)

if __name__ == "__main__":
    main()