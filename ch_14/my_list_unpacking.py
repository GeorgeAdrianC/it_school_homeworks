foo = [7, 9, 11]

x = foo[0]
y = foo[1]
z = foo[2]

print("Classic: ")
print(x)
print(y)
print(z)

a, b, c = foo

print("Iterative unpacking: ")
print(a)
print(b)
print(c)

d, e = foo[1:]

print("Uneven unpacking: ")
print(d)
print(e)