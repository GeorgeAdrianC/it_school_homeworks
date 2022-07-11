input_ = '1||Ion Pop||Tester\n'
output = (1, "Ion Pop", "Tester")

contents = input_.strip().split("||")
print(contents)

result = (int(contents[0]), contents[1], contents[2])
print(result)
