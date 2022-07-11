name = " "
password = " "
users = "Joe, Jane, Carol"


while name not in users:
    print("Who are you? ")
    name = input()

    
        
while password != "swordfish":
    print(f"Hello, {name}. What is the password? (It is a fish).")
    password = input()


print("Access granted!")
