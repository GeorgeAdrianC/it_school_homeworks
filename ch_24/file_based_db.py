from pathlib import Path
from typing import List, Tuple, Optional


def load_db() -> List[Tuple[int, str, str]]:
    db_path = Path("./db.txt")
    if not db_path.exists():
        raise Exception("Database file missing")
    with open(db_path, "r") as db_file:
        raw_db_content = db_file.readlines()
    db_content = []
    for raw_entry in raw_db_content:
        if raw_entry == "\n":
            continue
        contents = raw_entry.strip().split("||")
        entry = (int(contents[0]), contents[1], contents[2])
        db_content.append(entry)
    db_content.sort(key=lambda entry: entry[0])
    return db_content


def search_db(id_: int, db_data: List[Tuple[int, str, str]]) -> Optional[Tuple[int, str, str]]:
    lower_index = 0
    upper_index = len(db_data) - 1
    middle_index = 0

    while lower_index <= upper_index:
        middle_index = (upper_index + lower_index) // 2
        if db_data[middle_index][0] < id_:
            lower_index = middle_index + 1
        elif db_data[middle_index][0] > id_:
            upper_index = middle_index - 1
        else:
            return db_data[middle_index]
    return None


def save_db(db_data: List[Tuple[int, str, str]]) -> None:
    db_path = Path("./db.txt")
    if not db_path.exists():
        raise Exception("Database file missing")
    with open(db_path, "w") as db_file:
        for entry in db_data:
            db_file.write(f"{entry[0]}||{entry[1]}||{entry[2]}\n")


def print_entry(entry: Tuple[int, str, str]) -> None:
    print(f"{entry[0]}. {entry[1]} with the role: {entry[2]}")


def main():
    prompt = """
    
    1. Print all records
    2. Print record by id
    3. Add record
    4. Update record by id
    5. Delete record by id
    
    """
    
    user_choice = int(input(prompt))
    
    db_data = load_db()
    if len(db_data) == 0:
        max_id = 0
    else:
        max_id = db_data[-1][0]
    
    if user_choice == 1:
        for entry in db_data:
            print_entry(entry)

    if user_choice == 2:
        id_ = int(input("Please type in the id: "))
        entry = search_db(id_, db_data)
        if entry:
            print_entry(entry)

    if user_choice == 3:
        user_name = input("Please type in the user name: ")
        user_role = input("Please type in the user role: ")
        entry = (max_id + 1, user_name, user_role)
        db_data.append(entry)
        save_db(db_data)

    if user_choice == 4:
        id_ = int(input("Please type in the id: "))
        entry_to_update = search_db(id_, db_data)
        if entry_to_update:
            db_data.remove(entry_to_update)
            user_name = input("Please type in the new user name: ")
            user_role = input("Please type in the new user role: ")
            entry_to_update = list(entry_to_update)
            entry_to_update[1] = user_name
            entry_to_update[2] = user_role
            entry_to_update = tuple(entry_to_update)
            db_data.append(entry_to_update)
            save_db(db_data)

    if user_choice == 5:
        id_ = int(input("Please type in the id: "))
        entry_to_delete = search_db(id_, db_data)
        if entry_to_delete:
            db_data.remove(entry_to_delete)
            save_db(db_data)


if __name__ == "__main__":
    main()