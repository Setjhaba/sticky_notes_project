from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm

# Create your tests here.
def setUp(self):
    self.note = Note.objects.create(title="Test Note", content="This is a test note")

def test_note_has_title(self):
    """
    Test note object has correct title
    """
    note = Note.objects.get(id=1)
    self.assertEqual(note.title, "Test Note")

def test_note_has_content(self):
    """
    Test note object has correct content
    """
    note = Note.objects.get(id=1)
    self.assertEqual(note.content, "This is a test note")


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="This is a test note")

    def test_note_list_view(self):
        """
        Test that the note displays notes 
        """
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
     
    def test_note_detail_view(self):
        """
        Test that the note displays notes details
        """
        response = self.client.get(reverse("note_detail", args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note")

    def test_note_create_view(self):
        """
        Test to create note
        """
        response = self.client.post(reverse("note_create"), {
            "title": "New note",
            "content": "New content",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 2)
        self.assertEqual(Note.objects.last().title, "New note")

    def test_note_update_view(self):
        """"
        Test updating a note
        """
        response = self.client.post(reverse("note_update", args=[self.note.id]), {
            "title": "Updated note",
            "content": "Updated content"
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated note")

    def test_note_delete_view(self):
        """
        Test deleting a note
        """
        response = self.client.post(reverse("note_delete", args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())