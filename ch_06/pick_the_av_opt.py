option = input("Pick Yes (Y,y) or No (N/n)")

while option not in "yYnN":
    print(f"{option} is not valid. \n Please pick y or Y for YES, or n or N for NO")
    option = input()

if option in "yY":
    print("You chosed YES")
else:
    print("Your final option is NO")