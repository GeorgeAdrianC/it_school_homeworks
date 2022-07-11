import os

from pathlib import Path

some_files_path = Path("./some_files")

list_of_files = os.listdir(some_files_path)

path_of_files = []
for file in list_of_files:
    path_of_files.append(some_files_path / file)

print("All files")
all_files = some_files_path.glob("*")
all_files = list(all_files)
print(all_files)

print("Text files")
all_text_files = some_files_path.glob("*.txt")
all_text_files = list(all_text_files)
print(all_text_files)

print("Pdf files")
all_pdf_files = some_files_path.glob("*.pdf")
all_pdf_files = list(all_pdf_files)
print(all_pdf_files)

print("Foo files")
foo_files = some_files_path.glob("foo_?.*")
foo_files = list(foo_files)
print(foo_files)

print("Middle X files")
x_files = some_files_path.glob("*.?x?")
x_files = list(x_files)
print(x_files)