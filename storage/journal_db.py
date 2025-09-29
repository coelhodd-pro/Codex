from datetime import date
import json

def write():
    with open("/home/skygge/Codebases/Codex/data/journal.json", "r") as f:
        db = json.load(f)

    data = {
        "title": input("Title: "),
        "content": input("Content: "),
        "name": input("Name: "),
        "date": str(date.today()),
        "context": "journal"
    }

    db.append(data)

    with open("/home/skygge/Codebases/Codex/data/journal.json", "w") as f:
        json.dump(db, f, indent=4)

def read():
    title = input("Provide the title of the note: ")
    
    with open("/home/skygge/Codebases/Codex/data/journal.json", "r") as f:
        db = json.load(f)

    for data in db:
        if data["title"] == title:
            print(data)
            break
    else:
        print("Note not found.")

def show():
    with open("/home/skygge/Codebases/Codex/data/journal.json", "r") as f:
        db = json.load(f)

    for data in db:
        print(data)

def edit():
    field = input("Which field would you like to edit: ")
    field = field.lower()

    if field != "title" and field != "content" and field != "name" and field != "date" and field != "context":
        print("Invalid field.")
        return

    title = input("Provide the title of the note: ")
    with open("/home/skygge/Codebases/Codex/data/journal.json", "r") as f:
        db = json.load(f)


    for data in db:
        if data["title"] == title:
            data[field] = input("Change into >>> ")
            break
    else:
        print("Note not found.")
        return

    with open("/home/skygge/Codebases/Codex/data/journal.json", "w") as f:
        json.dump(db, f, indent=4)

