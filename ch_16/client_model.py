client = {
    "first_name": "John",
    "second_name": "Doe",
    "age": 34,
    "address_line_1": "New York",
    "address_line_2": "Fifth Avenue, 25"
}

client_as_a_list = ["John", "Doe", 34, "New York", "Fifth Avenue, 25"]

print(f"Hi {client['first_name']}, how's the weather in {client['address_line_1']}?")
print(f"Hi {client_as_a_list[0]}, how's the weather in {client_as_a_list[3]}?")
