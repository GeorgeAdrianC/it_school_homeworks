files = ["orders-1.txt", "orders-2.txt", "invoices-1.txt"] 
for file in files:
    if "orders" in file: 
        print(f"Processing orders from {file}")
    else:
        print(f"Processing invoices from {file}")
