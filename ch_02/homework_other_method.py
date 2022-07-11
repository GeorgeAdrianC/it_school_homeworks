print("Write a list of values for average calculus. If you want to stop type 0.")

sum_of_values = 0
number_of_values = 0
numbers = int(input("Write your list of values here: "))

if numbers == 0:
    print("You must enter a value dumbass")
else:
    while numbers != 0:
        sum_of_values = numbers + sum_of_values
        number_of_values = number_of_values + 1 
        print(f"The sum of your values is: {sum_of_values}")
        numbers = int(input("Write your values dumbass: "))
    print(f"The average of your values is {sum_of_values/(number_of_values)}")