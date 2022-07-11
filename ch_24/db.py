from pathlib import Path
from typing import List, Tuple


def load_db() -> List[Tuple[int, str, str]]:
    db_path = Path("./db.txt")
    if not db_path.exists():
        raise Exception("Database file missing")
    with open(db_path, "r") as db_file:
        raw_db_content = db_file.readlines()
    db_content = []
    for raw_entry in raw_db_content:
        contents = raw_entry.strip().split("||")
        entry = (int(contents[0],contents[1],contents[2])) 
        db_content.append(entry)
    return db_content

def main():
    prompt = """
    1. Print all records
    2. Print record by id
    3. Add record
    """

    user_choice = int(input(prompt))
    
    db_data = load_db()
    if user_choice == 1:
        for entry in db_data:
        print(f"{entry[0]}, {entry[1]} with the role: {entry[2]}")
    if user_choice == 2:
        id = input(int("Please type in the id: "))


if __name__ == "main":
    main()