#This returns the book as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# This returns the word count of the book
def get_word_count(path_to_file):
    word_count = 0
    words = get_book_text(path_to_file).split()
    for w in words:
        word_count += 1
    return word_count

#Prints the word count of the book to the console
def main():
    path_to_file = "books/frankenstein.txt"
    print(f"{get_word_count(path_to_file)} words found in the document")
    #return get_word_count(path_to_file)
    #print(get_book_text(path_to_file))
    #return get_book_text(path_to_file)


main()

