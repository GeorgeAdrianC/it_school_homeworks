import random
from types import NoneType
user_greetings_prompts = ["Hi!","Hello!","Greetings, traveler!"]
user_info_prompts = ["What's your age? ","How old are you? ","Please tell me your age. "]
user_shopping_list_prompts = ["What's on your shopping list? ","What would you like to buy? ","What can I get you? "]
user_farewell_prompts = ["Thank you for your purchase!","Thanks! Please come again.","Thank you!"]


name = input(f"{random.choice(user_greetings_prompts)} \n Please enter your name here: ")



age = int(input("Please enter your age: ")) 



shopping_list = list()

while True:
    print("Please enter your item here: ")
    groceries = input()
    shopping_list.append(groceries)       
    
    if groceries == " " or groceries == "nothing":
        break




print(f"Hi {name}! \n Welcome to our store!")
 
    
if age < 18:

    try:          
        number_groceries = len(shopping_list)
        seconds = (number_groceries -2) * 30 
        # if number_groceries > 1:                      
                                    
        if "cigarettes" in shopping_list:
            print("You cannot buy cigarettes. I will remove them from your list.")
            shopping_list = shopping_list.remove("cigarettes") 
            seconds = number_groceries - 1
        elif "beer" in shopping_list:
            print("You cannot buy beer. I will remove it from your list.")
            shopping_list = shopping_list.remove("beer") 
            seconds = number_groceries - 1
        elif "wine" in shopping_list:
            print("You cannot buy wine. I will remove it from your list.")
            shopping_list = shopping_list.remove("wine") 
            seconds = number_groceries - 1
        elif "rum" in shopping_list:
            print("You cannot buy rum. I will remove it from your list.")
            shopping_list = shopping_list.remove("rum") 
            seconds = number_groceries - 1
        else:
            pass
                
        print(f"We're really sorry {name}, but '{random.choice(shopping_list)}'j is no longer available. \n You will have to wait 30 seconds for every item in your list. \n Please wait for {seconds} seconds. \n Have a great day, {name}!")
#in mod normal *random.choice(shopping_list)* scoate un produs aleator din lista, dar daca varsta clientului este sub 18 ani
#si acesta alege sa cumpere un produs interzis din lista, totul merge normal, mai putin *random.choice(shopping_list)*   
    except TypeError:
        print(f"We're really sorry {name}, but one of your items is no longer available. \n You will have to wait 30 seconds for every item in your list. \n Please wait for {seconds} seconds. \n Have a great day, {name}!")
        
else:
    
    number_groceries = len(shopping_list)
    seconds = (number_groceries -2) * 30 
    if number_groceries <= 1:
        print("Please enter a shopping list!")
    else:            
        print(f"We're really sorry {name}, but {random.choice(shopping_list)} is no longer available. \n You will have to wait 30 seconds for every item in your list. \n Please wait for {seconds} seconds. \n Have a great day, {name}!")



