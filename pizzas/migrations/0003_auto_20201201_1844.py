# Generated by Django 3.1.4 on 2020-12-02 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_auto_20201201_1830'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topping',
            new_name='Pizza',
        ),
    ]
