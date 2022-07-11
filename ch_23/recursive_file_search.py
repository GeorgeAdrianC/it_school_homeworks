from pathlib import Path


some_files_path = Path("./some_files")

print("Text files")
all_text_files = some_files_path.glob("*.txt")
all_text_files = list(all_text_files)
print(all_text_files)

print("Text files")
rec_text_files = some_files_path.rglob("*.txt")
rec_text_files = list(rec_text_files)
print(rec_text_files)