# Generated by Django 3.2.20 on 2023-08-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Gardening', 'Gardening'), ('Cleaning', 'Cleaning'), ('Garden patch', 'Garden patch'), ('Swimming pool', 'Swimming pool'), ('Renovation and repair', 'Renovation and repair'), ('Home care', 'Home care')], default='Cleaning', max_length=50),
        ),
    ]