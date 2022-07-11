from messages import first_message

message = "C:\\my\\path\\to\\program\\tests"
print(message)

message = "I don't have my last letter\b\bHello"
print(message)

message = "I don't know\rWhere I will land"
print(message)

message = "I don't know\rHi!"
print(message)

raw_message = r'This is Alices\'s cat'
print(raw_message)

raw_message = r"I don't know\rHi!"
print(raw_message)

path = r"C:\Program Files\heroku\tests"
print(path)
print(type(path))

multiline_string = '''
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob'''
print(multiline_string)

if True:
    multiline_string = '''
    Dear Alice,

    Eve's cat has been arrested for catnapping, cat burglary, and extortion.

    Sincerely,
    Bob
    '''
    print(multiline_string)

number_of_laps = 65
fastest_time = "1:42:3256"

stats_report = f"""
The fastest lap time was {fastest_time}.
The whole race was {number_of_laps} long.
"""

"""
print(stats_report)

if True:
    print(first_message)
"""

"""
This bit of code highlights how strings are working in Python
This is another comment
This is the final comment line
"""