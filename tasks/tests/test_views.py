from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from tasks.models import Task, Employee
from tasks.views import TaskUpdateView


class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test",
            password="test",
            email="test@test.com",
        )
        self.list_url = reverse('dashboard')
        self.detail_url = reverse('task_detail', args=[1])
        self.task_1 = Task.objects.create(
            name='task test',
            owner=self.user,
        )

    def test_tasklist_get(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.list_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/dashboard.html')

    def test_TaskDetailView_get(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.detail_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_detail.html')

    def test_TaskCreateView_post(self):
        self.client.login(username='test', password='test')
        url = reverse('add_task')
        response = self.client.post(url, {
            'name': 'task test 2',
            'category': "Gardening",
        })

        task_2 = Task.objects.get(id=2)
        self.assertEquals(task_2.name, 'task test 2')
