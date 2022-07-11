client = {
    "first_name": "John",
    "second_name": "Doe",
    "age": 34,
    "addresses": [
        {
            "line_1": "New York",
            "line_2": "Fifth Avenue, 25"
        },
        {
            "line_1": "San Francisco",
            "line_2": "Sixth Avenue, 26"
        }
    ]
}

print(f"Hi {client['first_name']}, how's the weather in {client['addresses'][0]['line_1']}?")
print(f"Hi {client['first_name']}, how's the weather in {client['addresses'][1]['line_1']}?")

print(client['addresses'][1]['line_2'])