notes = []

def create_notes(note):
    notes.append(note)
    return {"message":"Note created","note":note}

def get_notes():
    return notes

def update_notes(id:int,note):
    notes[id] = note
    return {"message":"updated","note":note}

def delete_notes(id:int):
    notes.pop(id)
    return {"message": "deleted"}
