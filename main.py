def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def word_count(path_to_file):
    book_text = read_book(path_to_file)
    words = book_text.split()
    return len(words)


def character_count(path_to_file):
    letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0,
                    'e': 0, 'f': 0, 'g': 0, 'h': 0,
                    'i': 0, 'j': 0, 'k': 0, 'l': 0,
                    'm': 0, 'n': 0, 'o': 0, 'p': 0,
                    'q': 0, 'r': 0, 's': 0, 't': 0,
                    'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 0, 'z': 0}
    book_text = read_book(path_to_file).lower()
    for char in book_text:
        if char in letter_count:
            letter_count[char] += 1
    return letter_count


def character_report(path_to_file):
    report = f"--- Begin report of {path_to_file} ---\n"
    report += f"{word_count(path_to_file)} words found in the document.\n"
    char_dict = character_count(path_to_file)
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for char, count in sorted_char_dict.items():
        report += f"\nThe '{char}' character was found {count} times"
    report += f"\n--- End report ---"
    return report


def main():
    book_path = "books/frankenstein.txt"
    print(read_book(book_path))
    print(f"\n\n\n")
    print(word_count(book_path))
    print(f"\n\n\n")
    print(character_count(book_path))
    print(f"\n\n\n")
    print(character_report(book_path))


if __name__ == "__main__":
    main()
