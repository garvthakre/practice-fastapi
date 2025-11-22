from fastapi import APIRouter
from controllers.notes_controller import  (create_notes,get_notes,update_notes,delete_notes)
from models.note_model import Note

router = APIRouter(prefix="/notes")
@router.post("/")
def create(note: Note):
    return create_notes(note)
@router.get("/")
def get():
    return get_notes()

@router.put("/{id}")
def update(note: Note ,id:str):
    return update_notes(note,id)

@router.delete("/{id}")
def delete(id:str):
    return delete_notes(id)
