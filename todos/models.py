from django.db import models

class Todo(models.Model):
    """
    The Todo model contains and entry for the title and textfield for the body of the Todo item

    Uses the str dunder method for better readability 
    """
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
