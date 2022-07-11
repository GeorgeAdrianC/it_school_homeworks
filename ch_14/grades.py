grades = [
    ["Ashley", 93],
    ["Brad", 85],
    ["Cassie", 97]
]

for entry in grades:
    name = entry[0]
    grade = entry[1]
    print(f"{name}: {grade}")


for name, grade in grades:
    print(f"{name}: {grade}")

# for index, (name, grade) in enumerate(grades):
#     print(f"{index}# {name}: {grade}")

for entry in enumerate(grades):
    print(entry)