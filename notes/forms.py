from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and updating note instances
    """
    class Meta:
        model = Note
        fields = ["title", "content"]
