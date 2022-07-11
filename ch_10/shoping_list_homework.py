def get_customer_name():    
    name = input("Hello! \n Please enter your name here: ")
    return name 

def get_customer_age():    
    age = input("Please enter your age: ")
    return age

def get_shopping_list():
    shopping_list = list()
    
    while True:
        print("Please enter your shopping list here: ")
        groceries = input()
        shopping_list.append(groceries)       
        
        if groceries == " " or groceries == "nothing":
            break
    return shopping_list

def main():
    name = get_customer_name()
    print(f"Hi {name}! \n Welcome to our store!")
    age = get_customer_age()  
    shopping_list = get_shopping_list()        
   
    number_groceries = len(shopping_list)
    seconds = (number_groceries - 1) * 30 
    
    if number_groceries <= 1:
        print("Please enter a shopping list!")
    else:
        print(f"Thank you, {name}! \n You will have to wait 30 seconds for every item in the list. \n Please wait for {seconds} seconds. \n Have a great day!")
    

main()
          


    
