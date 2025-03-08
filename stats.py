def word_count(string_to_count):
    return len(string_to_count.split())


def character_count(string_to_parse):
    letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
                    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
                    'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}
    book_text = string_to_parse.lower()
    for char in book_text:
        if char in letter_count:
            letter_count[char] += 1
    return letter_count

def character_count_sorted(character_count_dict):
    return dict(sorted(character_count_dict.items(), key=lambda item: item[1], reverse=True))