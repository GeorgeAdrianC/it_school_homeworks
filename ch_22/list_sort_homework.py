def sorted_list(my_list: list):
    if len(my_list) > 1:
        is_ascending = True
        is_descending = True

        for element in range(0, len(my_list)-2):
            if my_list[element] > my_list[element + 1]:
                is_ascending = False
                break
        for element in range(0, len(my_list)-2):
            if my_list[element] < my_list[element + 1]:
                is_descending = False
                break
        if is_ascending or is_descending:
            return True
        else:
            return False        
    else:
        print("Your list must have atleast 2 elements")

list_1 = [1,2,3,4,5,6]
list_2 = [6,5,4,3,2,1]
list_3 = [5,1,8,9,3,2]
list_4 = [9,5,3,0,-1,-5,-9]
list_5 = [-10,-3,-1,0,1,3,4,5]
list_6 = [2]

check_order = sorted_list(list_1)
print(check_order)
check_order = sorted_list(list_2)
print(check_order)
check_order = sorted_list(list_3)
print(check_order)
check_order = sorted_list(list_4)
print(check_order)
check_order = sorted_list(list_5)
print(check_order)
sorted_list(list_6)