# Generated by Django 3.2.20 on 2023-08-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_task_repeat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Description'),
        ),
    ]