def palindrome_1():
    n = input("Enter a 9 digit number: ")

    is_palindrome = True 

    for i in range(0, len(n) //2):
        if n[i] != n[len(n) - i -1]:
            is_palindrome = False
    if is_palindrome == True:
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")
    return n

m = palindrome_1()

def lenght():

    if len(m) <= 9:
        print("Have a great day!")
    else:
        print("Your number is greater than 9 digits.")

lenght()