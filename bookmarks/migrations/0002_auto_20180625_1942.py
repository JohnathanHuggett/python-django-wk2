# Generated by Django 2.0.6 on 2018-06-25 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookMarks',
            new_name='BookMark',
        ),
    ]