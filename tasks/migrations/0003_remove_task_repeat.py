# Generated by Django 3.2.20 on 2023-08-15 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='repeat',
        ),
    ]
