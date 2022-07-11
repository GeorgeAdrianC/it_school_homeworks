from pathlib import Path

my_file = Path("./foo.txt")

my_file.write_text("Goodbye cruel world!")

print(my_file.read_text())