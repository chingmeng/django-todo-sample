# Generated by Django 2.2.8 on 2020-11-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='detail',
            field=models.TextField(default='-'),
        ),
    ]
