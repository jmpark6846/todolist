from django.test import TestCase
from .models import Todo

# Create your tests here.
class TodoModelTestCase(TestCase):
    def test_model_can_make_an_instance(self):
        old_count = Todo.objects.count()
        Todo.objects.create(title="test title", content="this is new content")
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count,new_count)

