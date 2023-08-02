from django.contrib import admin

from .models import Task, Employee


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "name",
        "done",
        "repeat",
    )
    list_display_links = ("name", )
    list_editable = ("done", )
    list_filter = ("done", )
    search_field = ("owner", "category", )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "active", )
    search_field = ("full_name", )
