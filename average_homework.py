names = []

new_name = ""

while new_name != "0":
    new_name = input("Enter your values: ")

    if new_name != "0":
        names.append(new_name)
        
calc = [int(x) for x in names]
avg = sum(calc)/len(calc)
print(f"Your average is: {avg}")