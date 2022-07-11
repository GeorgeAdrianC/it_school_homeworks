def gimme_a_number():
    global number
    number = int(input("Please enter your integer: "))
  
def collatz(number):    

    global number

    if number % 2 == 0:
        print(number // 2)
    else:
        print(3 * number + 1) 
    
    return number


collatz()
