from pathlib import Path

my_path = Path("./some_files")

print(my_path.exists())
print(my_path.is_dir())
print(my_path.is_file())

my_file_path = my_path/"text_1.txt"
print(my_file_path.exists())
print(my_file_path.is_dir())
print(my_file_path.is_file())