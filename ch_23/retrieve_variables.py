import shelve


with shelve.open("foo_data") as foo_data:
    print(foo_data["owner_info"])
    print(foo_data["shopping_list"])
