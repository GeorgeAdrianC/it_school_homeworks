password = input("Please type in a password: ")
print(password)

password_length = len(password)

if password_length < 6:
    print("Very weak password.")
elif password_length >= 6 and password_length < 12:
    print("Not that weak password.")
elif password_length >= 12 and password_length < 24:
    print("Okay password.")
else:
    print("Very good password.")