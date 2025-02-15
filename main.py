def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def get_chars(file_contents):
    chars_dict = {}
    lowered_contents = file_contents.lower()
    chars_list = list(lowered_contents)
    for char in chars_list:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1 
    return chars_dict

def print_report(words_found, chars_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_found} words found in the document")
    for chars in chars_dict:
        if chars.isalpha():
         print(f"The '{chars}' character was found {chars_dict[chars]} times")
    print("--- End Report---")

file_contents = main()
count = word_count(file_contents)
chars_dict = get_chars(file_contents)
print_report(count, chars_dict)
