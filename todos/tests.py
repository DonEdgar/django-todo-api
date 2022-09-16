from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    """
    Creates tests based on the Todo model, to make sure entries get properly added to the models
    Also tests to make sure the string representation is the title of the model
    """
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
                title="First Todo",
                body="A body of text here"
                )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")
