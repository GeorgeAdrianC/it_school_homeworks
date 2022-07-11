"""
The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored. 
Extend your program from earlier exercise so that it is able to check if two phrases
are anagrams. Your program should ignore capitalization, punctuation marks and
spacing when making the determination.
"""


def count_letters(string: str) -> dict:
    string_letters = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            string_letters.setdefault(char, 0)
            string_letters[char] += 1
    return string_letters


first_phrase = input("Please input the first phrase: ")
second_phrase = input("Please input the second phrase: ")

first_phrase_letters = count_letters(first_phrase)
second_phrase_letters = count_letters(second_phrase)

is_anagram = True
for char in first_phrase_letters:
    if char not in second_phrase_letters:
        is_anagram = False
        break
    if first_phrase_letters[char] != second_phrase_letters[char]:
        is_anagram = False
        break

print(is_anagram)
