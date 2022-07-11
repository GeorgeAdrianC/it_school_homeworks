option = input("Pick Yes (Y/y) or No (N/n): ")

while option not in "yYnN":
    print(f"{option} is not valid. Please pick y or Y for Yes or n or N for No: ")
    option = input()

if option in "yY":
    print("Your final option is yes.")
else:
    print("Your final option is no.")