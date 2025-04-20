#Prints the word count of the book to the console
def main():
    path_to_file = "books/frankenstein.txt"
    print(f"{get_word_count(path_to_file)} words found in the document")
    #return get_word_count(path_to_file)
    #print(get_book_text(path_to_file))
    #return get_book_text(path_to_file)

from stats import get_word_count


main()

