import os
import sys
from operator import itemgetter

def count_words(in_string):
    words = in_string.split()
    return len(words)

def count_char(in_string):
    char_dict = {}
    in_string_lwr = in_string.lower()
    for char in in_string_lwr:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    char_list = list(char_dict.items())
    return char_list

def main():
    if len(sys.argv) < 2:
        raise Exception('Expecting the path to assess')
    dir_path = sys.argv[1]
    if dir_path[-1] != "/":
        dir_path += "/"

    directory = os.fsencode(dir_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            with open(os.fsdecode(directory) + filename) as f:
                file_contents = f.read()
                word_count = count_words(file_contents)
                char_count = count_char(file_contents)
                char_count_sorted = sorted(char_count, key=itemgetter(1), reverse=True)
                print(f"--- Begin report of {f.name} ---\n")
                print(f"{word_count} words found in the document\n\n")
                for char, count in char_count_sorted:
                    print(f"The \'{char}\' character was found {count} times\n")
                print("--- End report ---\n")


main()
