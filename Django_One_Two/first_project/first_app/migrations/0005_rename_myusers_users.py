# Generated by Django 3.2.5 on 2022-03-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20220322_1538'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUsers',
            new_name='Users',
        ),
    ]
