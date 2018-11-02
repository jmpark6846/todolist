from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Todo
from .views import url_with_querystring

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
        self.todo = Todo.objects.create(title="test title", content="test content", author=self.user)

    def test_view_can_list_todos(self):
        for i in range(0,5):
            Todo.objects.create(title="test title #{}".format(i), content="this is content #{}".format(i), author=self.user)

        res = self.client.get(reverse('todo:list'))
        self.assertEqual(res.status_code, 200)

    def test_view_can_create_a_todo(self):
        todo_data = { 'title' : 'this is new title', 'content' : 'this is new content', 'author': self.user, 'priority':2 }
        res = self.client.post(reverse('todo:create'), todo_data)
        self.assertEqual(res.status_code, 302) # 생성 성공시 리다이렉트

    def test_view_can_view_todo_detail(self):
        res = self.client.get(reverse('todo:detail', kwargs={'pk':self.todo.pk}))
        self.assertEqual(res.status_code, 200)

    def test_view_can_update_todo(self):
        todo_data = { 'title' : 'this is new title', 'content' : 'this is new content', 'author': self.user,  'priority':2 }
        res = self.client.post(reverse('todo:update', kwargs={'pk': self.todo.pk}), todo_data)
        self.assertEqual(res.status_code, 302) # 업데이트 성공시 디테일 뷰로 리다이렉트

    def test_view_can_delete_todo(self):
        old_count = Todo.objects.count()
        self.client.delete(reverse('todo:delete', kwargs={'pk': self.todo.pk}))
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_only_owner_can_view_own_todo(self):
        self.create_user('john','1234')
        self.client.login(username='john', password='1234')

        res = self.client.delete(reverse('todo:detail', kwargs={'pk':self.todo.pk}))
        self.assertEqual(res.status_code, 404)

    def test_toggle_todo_done(self):
        res = self.client.post(reverse('todo:toggle_done', kwargs={'pk':self.todo.id}))
        self.assertEqual(res.status_code, 200)

    def test_can_sort_todolist_by_priority(self):
        Todo.objects.create(title="test title", content="test content", author=self.user, priority=3, done=False)
        Todo.objects.create(title="test title", content="test content", author=self.user, priority=2, done=False)
        Todo.objects.create(title="test title", content="test content", author=self.user, priority=1, done=False)

        url = url_with_querystring(reverse('todo:list'), sort_by='-priority')
        res = self.client.get(url)

        self.assertEqual(res.context['alive'][0].priority, 3)
        self.assertEqual(res.status_code, 200)

    def test_show_404_with_wrong_querystring_for_sort_todolist(self):
        url = url_with_querystring(reverse('todo:list'), sort_by='hahaha')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 404)
