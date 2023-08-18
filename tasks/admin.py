from django.contrib import admin

from .models import Task, Employee


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    This class displays instances of the Task model in the admin panel
    """
    list_display = (
        "due_date",
        "done",
        "owner",
        "name",
        "employee",
        "comment",
    )
    list_display_links = ("name", )
    list_editable = ("done", "comment", "employee", )
    list_filter = ("done", "due_date", "employee", "owner", )
    search_fields = ["category", "name", ]
    ordering = ["due_date", ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    This class displays instances of the Employee model in the admin panel
    """
    list_display = ("full_name", "active", )
    search_field = ("full_name", )
