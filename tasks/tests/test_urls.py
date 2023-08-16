from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tasks import views


class TestUrls(SimpleTestCase):

    def test_task_list_url_is_resolves(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func.view_class, views.TaskList)

    def test_create_task_url_is_resolves(self):
        url = reverse('add_task')
        self.assertEquals(resolve(url).func.view_class, views.TaskCreateView)

    def test_task_detail_url_is_resolves(self):
        url = reverse('task_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.TaskDetailView)

    def test_update_task_url_is_resolves(self):
        url = reverse('update_task', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.TaskUpdateView)

    def test_delete_task_url_is_resolves(self):
        url = reverse('delete_task', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.TaskDeleteView)
