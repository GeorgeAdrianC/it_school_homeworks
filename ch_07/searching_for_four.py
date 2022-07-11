for i in range(0, 11, 2):
    if i == 4:
        print("Found number 4!")
        break
    print(i)
else:
    print("Number 4 not found!")


for i in range(0, 11, 2):
    if i == 4:
        print("Number 4 is hidden.")
        continue
    print(i)