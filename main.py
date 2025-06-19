def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def count_words(book_text):
    return len(book_text.split())

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f'{num_words} words found in the document')

if __name__ == "__main__":
    main()