from models.note import Note
import json

DATA_PATH = "/home/skygge/Codebases/Codex/data"

def load_notes(context):
    with open(f"{DATA_PATH}/{context}.json", "r") as f:
        db = json.load(f)
    return [Note.from_dict(data) for data in db]

def save_notes(context, notes):
    with open(f"{DATA_PATH}/{context}.json", "w") as f:
        json.dump([note.to_dict() for note in notes], f, indent=4)

def write(context):
    notes = load_notes(context)
    title = input("Title: ")
    content = input("Content: ")
    name = input("Name: ")

    note = Note(title, content, name, context)
    notes.append(note)
    save_notes(context, notes)

def read(context):
    notes = load_notes(context)
    title = input("Provide the title of the note: ")

    for note in notes:
        if note.title == title:
            print(f"Title: {note.title}")
            print(f"Author: {note.name}")
            print(f"Date: {note.date_created}")
            print(f"Content:\n{note.content}")
            break
    else:
        print("Note not found.")

def show(context):
    notes = load_notes(context)

    if not notes:
        print("Notes not found.")
        return

    for note in notes:
        print(f"Title: {note.title}")
        print(f"Author: {note.name}")
        print(f"Date: {note.date_created}")
        print(f"Summary: {note.summary()}")
        print(f"-" * 40)
    
def edit(context):
    notes = load_notes(context)
    title = input("Title of note to edit: ")

    for note in notes:
        if note.title == title:
            field = input("Which field (title, content, name): ").lower()
            if hasattr(note, field):
                new_value = input("New value: ")
                setattr(note, field, new_value)
                save_notes(context, notes)
                print("Note updated successfully.")
                return
            else:
                print("Invalid field.")
                return
    print("Note not found.")
