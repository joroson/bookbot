import sys

from stats import word_count, character_count, character_count_sorted


def read_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def generate_report(path_to_book, sorted_dict, num_words):
    report = f"============ BOOKBOT ============\n"
    report += f"Analyzing book found at {path_to_book}...\n"
    report += f"----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += f"--------- Character Count -------\n"
    for char, count in sorted_dict.items():
        if char.isalpha():
            report += f"{char}: {count}\n"
        else:
            continue
    print(report)


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = read_book(book_path)
    num_words = word_count(text)
    chars = character_count(read_book(book_path))
    sorted_dict = character_count_sorted(chars)
    print(f"{num_words} words found in the document")
    print(f"{chars}")
    print(f"{sorted_dict}")
    generate_report(book_path, sorted_dict, num_words)


main()
