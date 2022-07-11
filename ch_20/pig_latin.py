"""
Pig Latin is a language constructed by transforming English words. 
While the origins of the language are unknown, it is mentioned in at least two documents from
the nineteenth century, suggesting that it has existed for more than 100 years. The
following rules are used to translate English into Pig Latin:

• If the word begins with a consonant (including y), then all letters at the beginning of
the word, up to the first vowel (excluding y), are removed and then added to the end
of the word, followed by ay. For example, computer becomes omputercay
and think becomes inkthay.
• If the word begins with a vowel (not including y), then way is added to the end
of the word. For example, algorithm becomes algorithmway and office
becomes officeway.

Write a program that reads a line of text from the user. Then your program should
translate the line into Pig Latin and display the result. You may assume that the string
entered by the user only contains lowercase letters and spaces.
"""

user_text = input("Please input a text: ")

VOWELS = ["a", "e", "i", "o", "u"]

user_words = user_text.split()
pig_latin_words = []

for word in user_words:
    if word[0] in VOWELS:
        pig_latin_word = word + "way"
        pig_latin_words.append(pig_latin_word)
    else:
        move_to_end_letters = []
        remaining_letters = ""
        for index, char in enumerate(word):
            if char not in VOWELS:
                move_to_end_letters.append(char)
            else:
                remaining_letters = word[index:]
                break
        pig_latin_word = remaining_letters + "".join(move_to_end_letters) + "ay"
        pig_latin_words.append(pig_latin_word)

print(" ".join(pig_latin_words))
