from pathlib import Path


foo_path = Path("foo.txt")
foo_file = open(foo_path)
foo_content = foo_file.read()
print(foo_content)
foo_file.close()

with open(foo_path) as foo_file:
    foo_content = foo_file.read()
    print(foo_content)

