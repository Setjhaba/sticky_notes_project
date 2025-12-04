from django.urls import path
from .views import (
    note_list,
    note_detail,
    note_create,
    note_update,
    note_delete,
)

urlpatterns = [
    # Display all notes
    path("", note_list, name="note_list"),
    # View a note by ID
    path("note/<int:pk>/", note_detail, name="note_detail"),
    # Create a new note
    path("note/new/", note_create, name="note_create"),
    # Edit an existing note
    path("note/<int:pk>/edit/", note_update, name="note_update"),
    # Delete a note
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
]
