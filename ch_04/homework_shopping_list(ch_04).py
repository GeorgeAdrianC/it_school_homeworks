
name = input("Hi! Whats your name?: ")
age = input("How old are you?: ")
shopping_list = str(input("What would you like to buy?: "))
counter = int(shopping_list.count(""))

if 0.0 <= counter <= 1:
    print(f"{name}, please return with a shopping list.\n Thank you!")
elif counter > 0:
    print(f"{name}, please wait for {counter} seconds.\n Thank you for your patience!")

print(" ")