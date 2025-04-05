import sys

def get_book_text(path_to_file):
 with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
from stats import get_word_count, get_letter_count, sort_char_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]  # Path to the book
    
    # Get the word count
    word_count = get_word_count(path)
    
    # Get the character counts and sort them
    char_dict = get_letter_count(path)
    sorted_chars = sort_char_count(char_dict)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Call the main function
if __name__ == "__main__":
    main()