my_dict = {'first_name': 'James', 'last_name': 'Doe', 'email': 'jdoe@gmail.com'}
my_dict["last_name"] = "Smith"
print(my_dict)
my_dict.pop("email")
print(my_dict)
my_set = {"a", "b", "c", "c"}
my_set2 = {"a", "b", "c", "c"}
if "b" in my_set and my_set2:
    print("'b' is in both set.")
else:
    print("'b' is not in both sets.")
my_set.add("new_value")
print(my_set)
my_set.remove("c")
print(my_set)
z = my_set.intersection(my_set2)
print(z)