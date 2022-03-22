# Generated by Django 3.2.5 on 2022-03-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_rename_user_my_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='My_Users',
        ),
    ]
