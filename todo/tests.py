from django.test import TestCase
from todo.models import TodoEvent
# Create your tests here.


class TodoEventTest(TestCase):
    def setUp(self):
        TodoEvent.objects.create(event_name='test1')
        TodoEvent.objects.create(event_name='test2')

    def test_todo_event(self):
        todo1 = TodoEvent.objects.get(event_name='test1')
        todo2 = TodoEvent.objects.get(event_name='test2')
        self.assertEqual(todo1.event_name, 'test1')
        self.assertEqual(todo2.event_name, 'test2')
