def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = text.lower()
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_list(dict):
    def sort_on(items):
        return items["num"]
    
    dict_list = []
    for key in dict:
        dict_list.append({"char": key, "num": dict[key]})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    