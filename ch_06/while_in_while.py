name = ""
password = ""
while True:
    print("Who are you? ")
    name = input()
    if name != "Joe":
        continue
    while password != "swordfish":
        print("Hello, Joe! What is the password? (It is a fish.) ")
        password = input()
    break

print("Access granted.")