import random


greetings = [
    "Hi",
    "Hello",
    "Hey, how are you?"
]

user_info_prompts = [
    "Whats your age?",
    "How old are you?",
    "Please tell me your age"
]

user_shopping_list_prompt = [ 
    "Whats on your shopping list",
    "What would you like to buy?",
    "What can I get you?"
]

user_closing_remarks = [ 
    "Thank you for your purchase",
    "Bye bye baws",
    "Fenk U boi"
]

print(random.choice(greetings))

age = int(input(random.choice(user_info_prompts)))

if age<18:
    print("We do not serv underage minions")
else:
    number_of_shopping_items = 0    
    while True:
        shopping_item = input("Current item: ")
        if shopping_item == "":
            break
        number_of_shopping_items += 1
    print(f"Your waiting time is {number_of_shopping_items * 30} seconds.")
    print(random.choice(user_closing_remarks))
        