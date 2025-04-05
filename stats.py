def get_word_count(path_to_file):
    count = 0
    with open(path_to_file) as f:

        data = f.read()

        words = data.split()

        count += len(words)
        return count
    
def get_letter_count(path_to_file):
    char_dict = {}
    with open(path_to_file) as f:

        data = f.read()
        letters = data.lower()

        for l in letters:
            if l in char_dict:
                char_dict[l] += 1
            else:
                char_dict[l] = 1

        return char_dict

def sort_char_count(char_dict):
    # Create a list to hold our dictionaries
    char_list = []
    
    # Convert the dictionary into a list of dictionaries
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    # Define a function to use as the key for sorting
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in descending order (reverse=True)
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
