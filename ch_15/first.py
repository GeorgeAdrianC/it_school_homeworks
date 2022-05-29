our_list = []



while True:
    number = int(input("Write your numbers: "))
    if number != 0:
        our_list.append(number)
        print(our_list)
    else:
        break

our_list.reverse()

for row in our_list:
    print(row)