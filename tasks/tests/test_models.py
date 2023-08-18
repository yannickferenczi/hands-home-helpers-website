from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date

from tasks.models import Task, Employee


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test",
            password="test",
            email="test@test.com",
        )
        self.employee = Employee.objects.create(
            first_name="test f name",
            last_name="test l name",
        )

        self.task = Task.objects.create(
            name="task test",
            owner=self.user,
        )

    def test_employee_is_active(self):
        self.assertTrue(self.employee.active)

    def test_employee_full_name(self):
        self.assertEqual(self.employee.full_name, "test f name test l name")

    def test_task_is_not_done(self):
        self.assertFalse(self.task.done)

    def test_task_created_on_is_today(self):
        self.assertEqual(self.task.created_on, date.today())

    def test_task_category_is_cleaning(self):
        self.assertEqual(self.task.category, "Cleaning")

    def test_task_employee_is_none(self):
        self.assertEqual(self.task.employee, None)

    def test_task_comment_is_none(self):
        self.assertEqual(self.task.comment, None)

    def test_task_due_date_is_none(self):
        self.assertEqual(self.task.due_date, None)
