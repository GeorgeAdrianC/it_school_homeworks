def gimme_a_number():
    number = input("Please enter your integer: ")
    return number

def checking_the_input():

    t = gimme_a_number()
    if type(t) == int:
        pass
    else:
        raise Exception("Please use only integres")
       
def collatz():
    
    our_nr = gimme_a_number()

    if our_nr % 2 == 0:
        print(our_nr // 2)
    else:
        print(3 * our_nr + 1) 
    
    return our_nr


collatz()
