from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo

# Create your tests here.
class TodoModelTestCase(TestCase):
    def create_user(self, name, pw):
        user = User.objects.create(username=name)
        user.set_password(pw)
        user.save()
        return user

    def setUp(self):
        self.user = self.create_user('tom', '12345')
        self.client.login(username='tom', password='12345')

    def test_model_can_make_an_instance(self):
        old_count = Todo.objects.count()
        Todo.objects.create(title="test title", content="this is new content", author=self.user)
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count,new_count)



class TodoViewTestCase(TestCase):
    def create_user(self, name, pw):
        user = User.objects.create(username=name)
        user.set_password(pw)
        user.save()
        return user

    def setUp(self):
        self.user = self.create_user('tom', '12345')
        self.client.login(username='tom', password='12345')

    def test_view_can_list_todos(self):
        for i in range(0,5):
            Todo.objects.create(title="test title #{}".format(i), content="this is content #{}".format(i), author=self.user)

        res = self.client.get(reverse('todo:list'))
        self.assertEqual(res.status_code, 200)

    def test_view_can_create_a_todo(self):
        todo_data = { 'title' : 'this is new title', 'content' : 'this is content', 'author': self.user }
        res = self.client.post(reverse('todo:create'), todo_data)
        self.assertEqual(res.status_code, 302) # 생성 성공시 리다이렉트