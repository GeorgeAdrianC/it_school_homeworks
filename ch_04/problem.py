#Create a program that reads two integers, a and b, from the user. Your program should compute and display:

# The sum of a and b
# The difference when b is subtracted from a
# The product of a and b
# The quotient when a is divided by b
# The remainder when a is divided by b
# The result of log10 a
# The result of a^b
from math import log 
a = int(input("Please enter a value for 'a': "))
b = int(input("Please enter a value for 'b': "))
print(f"The sum of a and b: {a+b}")
print(f"The difference when b is subtracted from a: {b-a}")
print(f"The product of a and b: {a*b}")
print(f"The quotient when a is divided by b {a//b}")
print(f"The remainder when a is divided by b: {a%b}")
print(f"The result of log10 a: {log(a,10)}")
print(f"The result of a^b: {a**b}")