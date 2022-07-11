name = input("Please type in your name: ")
age = int(input("Please type in your age: "))
shopping_list = input("Please type in your shopping list: ")
waiting_time = len(shopping_list)

if waiting_time == 0:
    print("Please come back with a shopping list.")
else:
    if age < 18:
        if "cigarettes" in shopping_list:
            print("You cannot buy cigarettes. I will remove them from your list.")
            waiting_time = waiting_time - len("cigarettes")
        if "beer" in shopping_list:
            print("You cannot buy beer. I will remove it from your list.")
            waiting_time = waiting_time - len("beer")
    print(f"Your waiting time is {waiting_time} seconds.")