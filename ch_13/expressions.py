shopping_list = []

while True:
    print(f"Enter the name of the product {len(shopping_list) +1 }")
    product_name = input()
    if product_name =="":
        break
    shopping_list = shopping_list + [product_name]

print(f"The item: {shopping_list})")
for item in shopping_list:
    print(item)

