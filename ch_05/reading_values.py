str_var = input("Please input a word: ")
print(str_var)

int_var = int(input("Please input an integer: "))
# int_var = int("25")
# int_var = 25
# This is a message for another programmer.
print(int_var)

float_var = float(input("Please input a floating number: "))
# float_var = float("13.13")
# float_var = 13.13
print(float_var)

user_prompt = input("Please input yes or no: [y/n] ")
if user_prompt == "yes":
    user_bool_var = True
elif user_prompt == "Yes":
    user_bool_var = True
elif user_prompt == "y":
    user_bool_var = True
elif user_prompt == "Y":
    user_bool_var = True
else:
    user_bool_var = False

print(user_bool_var)

# bool_var = input("Please input a boolean value (True/False): ")
# if bool_var == "True":
#     bool_var = True
# elif bool_var == "False":
#     bool_var = False
# else:
#     bool_var = "Incorrect Boolean value"
# print(bool_var)