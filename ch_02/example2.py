names = []

new_name = ''

# Start a loop that will run until the user enters 'quit'.
while new_name != 'quit':
    new_name = input("Enter Name, or 'quit': ")

    if new_name != 'quit':
        names.append(new_name)

calc = [int(x) for x in names]
print(calc)