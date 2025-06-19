def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    print(get_book_text("books/frankenstein.txt"))

if __name__ == "__main__":
    main()