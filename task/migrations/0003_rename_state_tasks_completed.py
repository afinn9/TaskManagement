# Generated by Django 5.0.4 on 2024-08-12 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_tasks_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='state',
            new_name='completed',
        ),
    ]
