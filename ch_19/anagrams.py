"""
Two words are anagrams if they contain all of the same letters, but in a different
order. For example, “evil” and “live” are anagrams because each contains one e, one
i, one l, and one v. Create a program that reads two strings from the user, determines
whether or not they are anagrams, and reports the result.
"""

first_word = input("Please input the first word: ")
second_word = input("Please input the second word: ")

first_word_letters = {}
second_word_letters = {}

for char in first_word:
    first_word_letters.setdefault(char, 0)
    first_word_letters[char] += 1

for char in second_word:
    second_word_letters.setdefault(char, 0)
    second_word_letters[char] += 1

is_anagram = True
for char in first_word_letters:
    if char not in second_word_letters:
        is_anagram = False
        break
    if first_word_letters[char] != second_word_letters[char]:
        is_anagram = False
        break

print(is_anagram)