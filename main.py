def count_words(in_string):
    words = in_string.split()
    return len(words)

def count_char(in_string):
    char_dict = {}
    in_string_lwr = in_string.lower()
    for char in in_string_lwr:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_char(file_contents))

main()
