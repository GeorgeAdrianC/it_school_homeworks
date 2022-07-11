names = ["Alice", "Bob", "Carol"]

print(", ".join(names))

print("ABC".join(["My", "name", "is", "Simon"]))

"""
------------------------------------------------
"""

print("My name is Simon".split())

print("MyABCnameABCisABCSimon".split("ABC"))

foo = '''Dear Alice,

How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''

for row in foo.split("\n"):
    print(f"Row has {len(row)} characters")


print(foo.find("Milk"))
print(foo[foo.find("Milk"):foo.find("Please")])