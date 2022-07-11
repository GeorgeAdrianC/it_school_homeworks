from sales_tax import add_sales_tax


def print_receipt():
    total = 85
    state = "MI"
    print(f"Total: {total}")
    print(f"After tax: {add_sales_tax(total, state)}")

print_receipt()