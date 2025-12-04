from django.db import models


# Create your models here.
class Note(models.Model):
    """
    Model representing a sticky note
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.title
