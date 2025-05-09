import sys

#Prints the word count of the book to the console
def main():
    arguments = sys.argv
    if (len(arguments) == 2):
        path_to_file = arguments[1]
        #path_to_file = "books/frankenstein.txt"
        test = get_char_count(path_to_file)
        sort_list = sort_dict(test)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {get_word_count(path_to_file)} total words")
        print("--------- Character Count -------")
        for i in range(0,len(sort_list)):
            print(f"{sort_list[i]["name"]}: {sort_list[i]["num"]}")
        print("============= END ===============")
    else:
        print("The path to the book is required")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    

from stats import get_word_count
from stats import get_char_count
from stats import sort_dict
from stats import sort_on


main()

