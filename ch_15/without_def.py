import random
user_greetings_prompts = ["Hi!","Hello!","Greetings, traveler!"]
user_info_prompts = ["What's your age? ","How old are you? ","Please tell me your age. "]
user_shopping_list_prompts = ["What's on your shopping list? ","What would you like to buy? ","What can I get you? "]
user_farewell_prompts = ["Thank you for your purchase!","Thanks! Please come again.","Thank you!"]

def get_customer_name():    
    name = input(f"{random.choice(user_greetings_prompts)} \n Please enter your name here: ")
    return name 

def get_customer_age():       
    age = int(input("Please enter your age: ")) 
    return age



def main():
    shopping_list = list()
    
    name = get_customer_name()
    print(f"Hi {name}! \n Welcome to our store!")
    age = get_customer_age()  
    while True:
        print("Please enter your item here: ")
        groceries = input()
        shopping_list.append(groceries)       
        
        if groceries == " " or groceries == "nothing":
            break
    
       
    if age < 18:
               
        number_groceries = len(shopping_list)
        seconds = (number_groceries -2) * 30 
        # if number_groceries > 1:                      
        
                                     
        if "cigarettes" in shopping_list:
            print("You cannot buy cigarettes. I will remove them from your list.")
            shopping_list = shopping_list.remove("cigarettes") 
            
        if "beer" in shopping_list:
            print("You cannot buy beer. I will remove it from your list.")
            shopping_list = shopping_list.remove("beer") 
            
        if "wine" in shopping_list:
            print("You cannot buy wine. I will remove it from your list.")
            shopping_list = shopping_list.remove("wine") 
            
        if "rum" in shopping_list:
            print("You cannot buy rum. I will remove it from your list.")
            shopping_list = shopping_list.remove("rum") 
            
        else:
            pass
        print(shopping_list)
        print(f"Thank you, {name}! \n We're really sorry but {random.choice(shopping_list)} is no longer available. \n You will have to wait 30 seconds for every item in your list. \n Please wait for {seconds} seconds. \n Have a great day, {name}!")
    # else:
        #     print("Please enter a shopping list!")
    else:
               
        number_groceries = len(shopping_list)
        seconds = (number_groceries -2) * 30 
        if number_groceries <= 1:
            print("Please enter a shopping list!")
        else:            
            print(f"Thank you, {name}! \n We're really sorry but {random.choice(shopping_list)} is no longer available. \n You will have to wait 30 seconds for every item in your list. \n Please wait for {seconds} seconds. \n Have a great day, {name}!")
    
main()

#   print(random.choice(user_shopping_list_prompts))
#         number_of_shopping_items = 0
#         while True:
#             shopping_item = input("Current item: ")
#             if shopping_item == "":
#                 break
#             number_of_shopping_items += 1
#         print(f"Your waiting time is {number_of_shopping_items * 30} seconds.")
#         print(random.choice(user_farewell_prompts))