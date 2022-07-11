from pathlib import Path

foo_path = Path("foo.txt")
with open(foo_path) as foo_file:
    foo_content = foo_file.readlines()
    print(foo_content)
