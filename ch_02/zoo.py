entry_price = 0.00
total_sum = 0.00

while True:
    print("What is your age? ")
    age = input()
    if age =="" or age == " ":
        break
    age = int(age)
    if age <= 2:
        entry_price = 0.00
    elif 3<=age<=12:
        entry_price = 14.00
    elif 13<=age<=65:
        entry_price = 22.00
    elif age > 65:
        entry_price = 18.00
    
    total_sum = entry_price + total_sum 
    print(f"Right now you have to pay {total_sum}")
print(f"Your final sum is {total_sum}")


