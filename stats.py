# This returns the word count of the book
def get_word_count(path_to_file):
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    for w in words:
        word_count += 1
    return word_count

#This returns the character count as a dictionary
def get_char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    characters =  file_contents
    char_dict = {}
    for c in characters:
        c = c.lower()
        if c in char_dict:
            char_dict[c] += 1 
        else:
            char_dict[c] = 1
    return char_dict

#This function sorts the list from highest count to lowest
def sort_dict(dict):
    sorted_list = []
    for c, count in dict.items():
        if c.isalpha():
            sorted_list.append({"name": c, "num": count})
        else:
            pass

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(sorted_list):
   return sorted_list["num"]

    


