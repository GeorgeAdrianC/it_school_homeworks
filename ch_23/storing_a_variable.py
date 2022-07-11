import shelve


# something_to_save = {
#     "name": "Ion",
#     "role": "owner"
# }

something_to_save = ["bread", "water", "wine", "cheese", "ham", "grapes"]

with shelve.open("foo_data") as shelf_file:
    # shelf_file["owner_info"] = something_to_save
    shelf_file.setdefault("shopping_list", something_to_save)
