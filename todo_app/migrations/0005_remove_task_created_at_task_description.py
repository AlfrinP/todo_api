# Generated by Django 5.0.4 on 2024-05-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
