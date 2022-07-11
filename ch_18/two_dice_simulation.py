import random

def random_dices():
    dice_1= [1,2,3,4,5,6]
    dice_2= [1,2,3,4,5,6]

    random_dice_1 = random.choice(dice_1)
    random_dice_2 = random.choice(dice_2)
    both_dices = random_dice_1 + random_dice_2
    return both_dices

def dice_list():
    
    sum = []
    counter = 0
    while counter == 10:
        counter += 1
        the_dice_sum = random_dices()
        sum = the_dice_sum + sum
    print(sum) 
dice_list()


