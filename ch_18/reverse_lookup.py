
def reverse_lookup(dictionary: dict, value):
    mapping_keys = []
    for k, v in dictionary.items():
        if value == v:
            mapping_keys.append(k)
    return mapping_keys


if __name__ == "__main__":
    dictionary = {
        "a": "foo",
        "b": "bar",
        "c": "foo",
        "d": "baz"
    }

    print(reverse_lookup(dictionary, "foo"))
    print(reverse_lookup(dictionary, "bar"))
    print(reverse_lookup(dictionary, "baz"))
    print(reverse_lookup(dictionary, "oof"))