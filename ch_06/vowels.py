vowels = "aeiouAEIOU"
user_character = " "
user_quit = True
max_tries = 5
number_of_tries = 1

while user_character not in vowels:
    user_character = input("Please type in a letter or type in 0 to quit: ")
    if user_character == "0":
        break
    if number_of_tries < max_tries:
        break
else:
    user_quit = False

if user_quit:
    print(f"You have quitted the game")
else:
    print(f"Your vowel is {user_character}")