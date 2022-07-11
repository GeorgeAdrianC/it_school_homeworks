"""
Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. In this exercise, you will write a function that capitalizes
the appropriate characters in a string. A lowercase “i” should be replaced with an
uppercase “I” if it is both preceded and followed by a space. The first character in
the string should also be capitalized, as well as the first non-space character after a
“.”, “!” or “?”. For example, if the function is provided with the string “what time
do i have to be there? what's the address?” then it should return the string “What
time do I have to be there? What's the address?”. Include a main program that reads
a string from the user, capitalizes it using your function, and displays the result.
"""


def capitalize_string(message: str) -> str:
    result = message.replace(" i ", " I ")
    
    if len(message) > 0:
        result = result[0].upper() + result[1:]
    
    position = 0

    while position < len(message):
        if result[position] in [".", "!", "?"]:
            position = position + 1
            while position < len(message) and result[position] == " ":
                position = position + 1
            if position < len(message):
                result = result[:position] + result[position].upper() + result[position + 1:]
        position = position + 1
    return result


if __name__ == "__main__":
    message = "what time do i have to be there?    what's the address?"
    result = capitalize_string(message)
    print(result)