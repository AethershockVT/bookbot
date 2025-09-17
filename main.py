import sys
from stats import count_words, count_characters, sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    chars = count_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_list(chars):
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
   # for key in chars:
    #    print(f"{key} : {chars[key]}")

main()