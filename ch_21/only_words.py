"""
In this exercise you will create a program that identifies all of the words in a string entered by the user. 
Begin by writing a function that takes a string of text as its only parameter. Your function should return a 
list of the words in the string with the punctuation marks at the edges of the words removed. The punctuation
marks that you must remove include commas, periods, question marks, hyphens, apostrophes, exclamation points, 
colons, and semicolons. Do not remove punctuation marks that appear in the middle of a words, such as the apostrophes 
used to form a contraction. For example, if your function is provided with the string "Examples of contractions
include: don't, isn't, and wouldn't." then your function should return the list ["Examples", "of", "contractions", 
"include", "don't", "isn't", "and", "wouldn't"].Write a main program that demonstrates your function. It should
read a string from the user and display all of the words in the string with the punctuation marks removed.
"""

def get_only_words(message: str) -> list:
    PUNCTUATION_MARKS= [",", ".", "?", "-", "'", '"', "!", ":", ";"]
    
    message_words = message.split()
    print(message_words)
    result = []
    for word in message_words:
        current_word = word
        if current_word[0] in PUNCTUATION_MARKS:
            current_word = current_word[1:]
        if current_word[-1] in PUNCTUATION_MARKS:
            current_word = current_word[:-1]
        result.append(current_word)

    return result


if __name__ == "__main__":
    message =  "Examples of contractions include: don't, 'isn't, and wouldn't."
    message_words = get_only_words(message)
    
    print(message_words)