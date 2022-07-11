# names = ["Larry", "Moe", "Shemp"]
# message = "The Three Stooges: "
# for index, name in enumerate(names):
#     if index > 0 and index != len(names) - 1:
#         message = message + ", "
#     if index == len(names) - 1:
#         message = message + " and "
#     message = message + name
# print(message)

# names = ["Larry", "Moe", "Curly"]
# message = "The Three Stooges: "
# for index, name in enumerate(names):
#     if index > 0 and index != len(names) - 1:
#         message = message + ", "
#     if index == len(names) - 1:
#         message = message + " and "
#     message = message + name
# print(message)

# def introduce_stooges(names):
#     message = "The Three Stooges: "
#     for index, name in enumerate(names):
#         if index > 0:
#             message = message + ", "
#         if index == len(names) - 1:
#             message = message + "and "
#         message = message + name
#     print(message)


# introduce_stooges(["Moe", "Larry", "Shemp"])
# introduce_stooges(["Larry", "Curly", "Moe"])

# def introduce(title, names):
#     message = f"{title}: "
#     for index, name in enumerate(names):
#         if index > 0:
#             message = message + ", "
#         if index == len(names) - 1:
#             message = message + "and "
#         message = message + name
#     print(message)

# introduce("The Three Stooges", ["Moe", "Larry", "Shemp"])
# introduce("The Three Stooges", ["Larry", "Curly", "Moe"])

# introduce("Teenage Mutant Ninja Turtles", ["Donatello", "Raphael", "Michelangelo", "Leonardo"])

# introduce("The Chipmunks", ["Alvin", "Simon", "Theodore"])


def join_names(names):
    name_string = ""
    for index, name in enumerate(names):
        if index > 0:
            name_string = name_string + ", "
        if index == len(names) - 1:
            name_string = name_string + "and "
        name_string = name_string + name
    return name_string


def introduce(title, names):
    print(f"{title}: {join_names(names)}")

introduce("The Three Stooges", ["Moe", "Larry", "Shemp"])
introduce("The Three Stooges", ["Larry", "Curly", "Moe"])

introduce("Teenage Mutant Ninja Turtles", ["Donatello", "Raphael", "Michelangelo", "Leonardo"])

introduce("The Chipmunks", ["Alvin", "Simon", "Theodore"])