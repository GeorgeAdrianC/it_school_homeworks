from pathlib import Path

foo_path = Path("./foo.txt")

with open(foo_path, "r") as foo_file:
    foo_content = foo_file.read()
    print(foo_content)
    foo_file.seek(7)
    foo_content_again = foo_file.read()
    print(foo_content_again)

with open(foo_path, "r") as foo_file:
    foo_content = foo_file.read(7)
    print(foo_content)
    foo_content_again = foo_file.read(11)
    print(foo_content_again)
    rest_of_content = foo_file.read()
    print(rest_of_content)