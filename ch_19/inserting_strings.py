name = "John"
age = 44
introduction = "Hello, my name is " + name + ". I am " + str(age) + " years old."

print(introduction)

introduction = "My name is %s. I am %s years old." % (name, age)
print(introduction)

introduction = f"My name is {name}. Next year I will be {age + 1}."
print(introduction)

names = ["John", "Mary", "Alice", "Bob", "Carol"]

for name in names:
    introduction = f"Hi, my name is {name}."
    print(introduction)

message_template = """Event %s occurred at %s, in program %s"""

messages = [("load", "15:35", "main"), ("delete", "17:35", "function_f")]

for message in messages:
    print(message_template % message)
    print(f"Event {message[0]} occurred at {message[1]}, in program {message[2]}")

