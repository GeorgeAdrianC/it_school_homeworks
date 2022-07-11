
shopping_list = list()


while True:
    print("Please enter your shopping list here: ")
    groceries = input()

    if groceries == " " or "nothing":
        break


    shopping_list.append(groceries)

count_a = len(shopping_list)
seconds = count_a * 30 
    
    

print(seconds)
     

 
