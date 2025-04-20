# This returns the word count of the book
def get_word_count(path_to_file):
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    for w in words:
        word_count += 1
    return word_count
